# 资料、版本与验收边界

核对日期：2026-10-19。官方文档用于机制定位；具体 Python 签名同时对照实际安装的 `openai-agents==0.24.0` 公共接口与官方源码。没有把托管 Agents API 的 Sessions/SDK 示例混入这里。

## Primary sources

- [Agents SDK 概览](https://developers.openai.com/api/docs/guides/agents/sdk)：应用侧执行循环与托管产品的职责边界。
- [SDK Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)：Python `Agent`、`Runner.run`、`function_tool` 和 handoffs。
- [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)：handoff 转移 ownership、agent-as-tool 保留管理者控制。
- [Results and state](https://developers.openai.com/api/docs/guides/agents/results)：最终输出、历史与恢复状态不是同一个对象。
- [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)：自动校验和有副作用动作的人工审批。
- [官方 Python 仓库](https://github.com/openai/openai-agents-python)：重点对照 `src/agents/testing/model.py`、`src/agents/agent.py`、`src/agents/run.py`、`src/agents/memory/sqlite_session.py` 和 `src/agents/guardrail.py`。
- [官方 testing 文档](https://github.com/openai/openai-agents-python/blob/main/docs/testing.md)：ScriptedModel 替换模型边界，真实 SDK 执行工具/交接/会话。
- [官方 Context 文档](https://github.com/openai/openai-agents-python/blob/main/docs/context.md)：应用 Context 与模型上下文的分离。
- [官方运行文档](https://github.com/openai/openai-agents-python/blob/main/docs/running_agents.md)：循环、streaming、异常、运行配置。

仓库 `main` 链接会演进；本例的可复现依据是本地 `pyproject.toml` 与 `uv.lock`，不是假定未来文档与当前代码永远一致。直接依赖只有 `openai-agents`；Pydantic/OpenAI 等传递版本以 lockfile 为准。

## 本次实际验证

验证环境：macOS arm64、Python 3.11.17；`openai-agents 0.24.0`、`openai 3.35.1`、`pydantic 2.14.1`。在独立环境与本专题 `.venv` 安装运行，不改系统 Python。

```bash
uv sync --locked --python 3.11
uv run --locked python run.py --all
uv run --locked python -m unittest discover -s tests -v
```

执行结果：八课离线演练全部完成（共 17 次合成模型调用），17 项自动测试通过；源码编译、Ruff 未定义/未使用符号检查、依赖兼容性检查及本专题 Markdown 本地链接/代码围栏/空白检查通过。`pip-audit` 对当前安装依赖报告未发现已知漏洞，这不是无漏洞保证。未将合成调用统计当作模型能力或性能测试。

验收层次：

| 层次 | 本次可证明 | 不可外推 |
| --- | --- | --- |
| 八课离线运行 | 真实 SDK 控制流、实际本地工具、结构化结果、会话与事件链 | 模型智能、真实路由可靠性、回答事实正确性 |
| 负例测试 | 非法输出不接受、非法工具参数进入错误路径、护栏零模型调用、循环限额生效 | 通用攻击检测或生产授权安全 |
| 禁网测试 | 八课在拦截 socket connect 时仍可完成 | 安装依赖无需网络、真实模式不访问网络 |
| CLI 测试 | 无 key 离线运行、真实模式缺配置/批量运行被拒绝 | 某个账户已获模型访问权限 |
| SQLite 临时文件测试 | 重开可读取历史、不同会话 ID 不混入同一查询 | 数据加密、多租户鉴权、任意规模性能 |

真实 OpenAI API、计费、服务端 trace、DeepSeek/其他兼容服务：**本次没有执行验收**。没有用用户凭据试调用，没有产生真实模型调用费用。

## 最小威胁边界

资产是 API 凭据、可见历史与调用预算。外部模型输出按不可信数据处理，只能选择 schema 约束的教学主题；不将其用作命令、路径或 SQL。API key 仅供客户端认证，不进入 instructions、工具结果或日志。工具只读固定卡片与显式预算字段。

本地持久化为可选明文 SQLite；只有公开练习数据适合放入此例。不会因为 Pydantic、护栏或 session ID 存在，就宣称拥有事实保证、安全沙箱或真实鉴权。
