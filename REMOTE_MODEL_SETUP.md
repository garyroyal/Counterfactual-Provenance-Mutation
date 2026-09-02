# 4090 笔记本局域网模型节点

## 推荐架构

```text
当前电脑：ProvenanceBench 调度、runtime、日志、统计、dashboard
        |
        | HTTP / 局域网
        v
4090 笔记本：Ollama 或 vLLM，仅负责模型推理
```

多 Agent 不等于多模型。同一 `qwen3:4b` 的多个角色适合研究 delegation、handoff 和 provenance 传播，但不能作为跨模型泛化证据。

## 4090 端使用 Ollama

1. 安装 Ollama。
2. 拉取一个当前电脑不适合运行的模型，例如：

```bash
ollama pull qwen3:8b
ollama pull llama3.1:8b
```

3. 仅在可信局域网中监听所有网卡：

Linux/macOS：

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Windows PowerShell：

```powershell
$env:OLLAMA_HOST="0.0.0.0:11434"
ollama serve
```

4. 在防火墙中只允许当前电脑访问 TCP 11434。不要把未认证的 Ollama 端口暴露到公网。

5. 查询 4090 笔记本的局域网 IP，例如 `192.168.1.100`。

## 当前电脑验证连接

```bash
curl http://192.168.1.100:11434/api/tags
```

运行单模型实验：

```bash
cd provenance_agent_eval
PYTHONPATH=. python3 -m provenance_agent_eval.model_demo \
  --model qwen3:8b \
  --base-url http://192.168.1.100:11434 \
  --matrix matched-laundering \
  --repetitions 20 \
  --output-dir artifacts/model-qwen3-8b-remote-v1
```

运行多 endpoint 配置：

```bash
cp model_endpoints.example.json model_endpoints.json
# 修改远端 IP 和实际模型名称
PYTHONPATH=. python3 -m provenance_agent_eval.multi_model_demo \
  --config model_endpoints.json \
  --matrix matched-laundering \
  --repetitions 20 \
  --output-root artifacts/multi-model-remote-v1
```

## 实验设计建议

- 当前 Mac：`qwen3:4b`、`llama3.2:3b`，用于小模型跨家族基线。
- 4090：优先 `qwen3:8b` 和一个 7B/8B Llama/Mistral 家族模型。
- 所有模型使用完全相同的 case、攻击变体、temperature 和解析器。
- 模型只输出动作选择；授权和工具执行始终在当前电脑的 ProvenanceBench runtime 中完成。
- 每个模型输出到独立目录，不共享或覆盖 JSONL。
