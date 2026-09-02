# 给 4090 笔记本 Codex 的部署任务

请在这台 4090 笔记本上配置一个只负责本地模型推理的 Ollama 节点，供另一台电脑上的 ProvenanceBench 通过局域网调用。不要把 ProvenanceBench 项目、实验日志或 runtime 搬到本机。

## 目标

- 安装并验证 Ollama。
- 至少准备两个本地模型：`qwen3:8b` 和一个不同家族的 7B/8B 模型，例如 `llama3.1:8b` 或 `mistral:7b`。
- Ollama 仅监听可信局域网，不暴露到公网。
- 返回本机局域网 IP、模型名称和健康检查结果。

## 执行步骤

1. 安装 Ollama，并确认：

```bash
ollama --version
```

2. 下载模型：

```bash
ollama pull qwen3:8b
ollama pull llama3.1:8b
```

如果某个模型名称不可用，选择同规模的本地 Llama/Mistral 模型，并记录准确名称。

3. 启动局域网服务。

Linux/macOS：

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Windows PowerShell：

```powershell
$env:OLLAMA_HOST="0.0.0.0:11434"
ollama serve
```

如果 Ollama 已经作为系统服务运行，使用对应的环境变量配置方式重启服务，不要同时启动两个实例。

4. 配置防火墙，仅允许实验主机访问 TCP `11434`。不要关闭防火墙，也不要配置公网端口转发。

5. 验证：

```bash
curl http://127.0.0.1:11434/api/tags
```

并记录局域网 IP，例如 `192.168.1.100`。

## 回传给实验主机的信息

```text
OLLAMA_BASE_URL=http://<LAN-IP>:11434
AVAILABLE_MODELS=<准确的模型名称列表>
HEALTH_CHECK=/api/tags 返回 HTTP 200
```

## 安全和实验约束

- 只允许实验主机访问 Ollama。
- 不使用商业 API，不上传实验数据。
- 不修改模型 temperature；ProvenanceBench 会固定 `temperature=0`。
- 不在 4090 上执行工具副作用；模型只返回动作选择，授权和工具执行由实验主机完成。
- 保持模型名称、量化版本、Ollama 版本可查询，以便写入实验日志。
