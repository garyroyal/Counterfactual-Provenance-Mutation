"""Run and log the first deterministic paired experiment."""

from pathlib import Path

from .experiment_log import ExperimentLogger
from .scenarios import paired_scenarios, run_scenario


def main(output_dir: str | Path = "artifacts/demo") -> None:
    logger = ExperimentLogger(output_dir)
    print("scenario,protected,utility,attack_success,leak,blocked")
    for scenario in paired_scenarios():
        baseline = run_scenario(scenario, protected=False)
        baseline_record = logger.record(
            experiment="paired-delivery-channel",
            condition="no-authorization",
            scenario=scenario.name,
            metrics={
                "utility": baseline.metrics.utility,
                "attack_success": baseline.metrics.attack_success,
                "sensitive_data_leak": baseline.metrics.sensitive_data_leak,
                "unauthorized_side_effect": baseline.metrics.unauthorized_side_effect,
                "blocked_actions": baseline.metrics.blocked_actions,
                "policy_violations": baseline.metrics.policy_violations,
            },
            notes="Reference runtime with no authorization gate.",
        )
        protected = run_scenario(scenario, protected=True)
        logger.record(
            experiment="paired-delivery-channel",
            condition="source-aware-authorization",
            scenario=scenario.name,
            defense="source-aware-authorization",
            baseline_id=baseline_record.record_id,
            metrics={
                "utility": protected.metrics.utility,
                "attack_success": protected.metrics.attack_success,
                "sensitive_data_leak": protected.metrics.sensitive_data_leak,
                "unauthorized_side_effect": protected.metrics.unauthorized_side_effect,
                "blocked_actions": protected.metrics.blocked_actions,
                "policy_violations": protected.metrics.policy_violations,
            },
            notes="Only the external side effect is gated; the read-only task remains executable.",
        )
        for protected_flag, result in ((False, baseline), (True, protected)):
            metrics = result.metrics
            print(
                f"{scenario.name},{protected_flag},{metrics.utility},{metrics.attack_success},"
                f"{metrics.sensitive_data_leak},{metrics.blocked_actions}"
            )
    logger.lesson(
        experiment="paired-delivery-channel",
        observation="同一攻击语义在三个交付通道中均触发了未保护运行时的外部发送。",
        evidence=("experiments.jsonl: exp-0001..exp-0006", "report.md: paired-delivery-channel"),
        conclusion="来源感知授权可以在保持读取任务 Utility 的同时阻断未授权外部副作用。",
        confidence="low",
        follow_up="在多个模型和来源变换节点上重复，并加入明确授权的合法副作用任务。",
    )
    logger.write_report()
    logger.write_lessons_report()
    print(f"logged_to={Path(output_dir).resolve()}")


if __name__ == "__main__":
    main()
