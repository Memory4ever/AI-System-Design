# OpenAI Agents SDK：从一次调用到完整学习助手

状态：可运行学习示例，不是生产服务；不自动改变 Books 或章节掌握度。

用一个“小型 AI System 学习教练”贯穿八课：查询固定教材卡片、读取学习时间、生成可检查的计划。每课只增加一个主要概念，最后串成完整流程。采用 Python；只需基础 Python 和模型 API 概念，不需要先学其他 Agent 框架。

这里学习的是 **OpenAI Agents SDK**：Agent 循环运行在自己的 Python 进程中，不是把部署、鉴权、存储都交给托管 Agents API。[官方 SDK 定位](https://developers.openai.com/api/docs/guides/agents/sdk)

## 先在五分钟内跑起来

要求：Python 3.11+、[uv](https://docs.astral.sh/uv/)。本机验证使用 Python 3.11.17。依赖固定为 `openai-agents==0.24.0`，传递依赖由 `uv.lock` 锁定。

```bash
cd /Users/apple/Documents/Work/PycharmProject/AI-System-Design/tasks/openai-agents-sdk
uv sync --locked --python 3.11
uv run --locked python run.py --lesson 1
uv run --locked python run.py --lesson 2
```

默认 **不需要 API key、不访问模型 API、不上传 trace**。首次安装依赖仍需网络。没有 uv 时也可以在独立 Python 3.11+ 虚拟环境中安装 `openai-agents==0.24.0` 再运行 `python run.py`，但这不等价于按 lockfile 固定全部依赖。

第 2 课应观察到：

```text
last_agent: CatalogTutor
items: tool_call_item -> tool_call_output_item -> message_output_item
```

这证明工具调用穿过了 SDK 执行链，不证明模型会正确选择工具。

全部离线演练和测试：

```bash
uv run --locked python run.py --all
uv run --locked python -m unittest discover -s tests -v
```

## 按这个顺序学习

详细讲解、预测题、改动实验和自测在 [逐课教程](./WALKTHROUGH.md)。不要一上来只读最后一课。

| 课 | 本次增加的能力 | 源码入口 | 你要能解释的问题 |
| --- | --- | --- | --- |
| 1 | Agent / Runner / Result | [basic.py](./lessons/basic.py) | 为什么 Agent 不是“模型对象”？ |
| 2 | Function Tool 与循环 | [tools.py](./lessons/tools.py) | 谁真正执行 Python 函数？ |
| 3 | 本地 Context | [context.py](./lessons/context.py) | 本地变量如何变成模型可见信息？ |
| 4 | Pydantic 输出契约 | [structured.py](./lessons/structured.py) | 格式正确为什么仍可能答错？ |
| 5 | Handoff / Agent-as-Tool | [collaboration.py](./lessons/collaboration.py) | 谁继续拥有最终回答？ |
| 6 | SQLite Session | [sessions.py](./lessons/sessions.py) | 下一轮的历史从哪里来？ |
| 7 | 护栏与失败边界 | [safety.py](./lessons/safety.py) | 拦截、循环上限、超时分别限制什么？ |
| 8 | Streaming / Hooks / 完整助手 | [workflow.py](./lessons/workflow.py) | 怎样看见执行过程并验证结果？ |

每课约 15～25 分钟，可分三次完成：1～3、4～6、7～8。这是建议学习节奏，不是课程效果保证。

## 离线与真实调用究竟差在哪里

`lab/runtime.py` 只负责选择模型、运行配置和会话位置，不重新实现 SDK。

```text
同一套 Agent / Runner / tools / schema / session / guardrail
                         |
                  Runtime.model(...)
                   /             \
       SDK ScriptedModel       OpenAIResponsesModel
       固定的模型输出脚本         真正的模型 API
```

离线使用 SDK 自带的 `agents.testing.ScriptedModel`。脚本规定“模型请求调用什么、最后输出什么”；工具执行、参数验证、交接、状态和事件由真实 SDK 完成。

因此，修改离线 prompt **不会自动改变脚本答案**。要测试另一条流程，必须同时调整脚本和断言；`assert_complete()` 检查没有遗漏脚本步骤，脚本耗尽后额外调用会失败。它是控制流实验，不是假装接入了一个智能模型。

## 再开启真实 API

先完成第 1～4 课的离线实验。真实模式会发送教学问题、模型可见历史和工具结果到 OpenAI，并可能计费；只使用公开教学数据。

在本机终端设置 `OPENAI_API_KEY`，不要发到聊天里，也不要写入代码、README 或 shell 历史。zsh 可以用隐藏输入：

```bash
read -rs 'OPENAI_API_KEY?OpenAI API key: '
export OPENAI_API_KEY
export OPENAI_MODEL='替换为你的 API 项目可用的模型 ID'
uv run --locked python run.py --lesson 1 --live
```

模型选择由你明确给出，示例不假设某个型号可用。第 2/3/5/8 课要求 function calling，第 4/8 课要求相应的结构化输出支持。示例不设置 temperature，避免把模型特定参数混入基础课。

确认第 1 课成功后，再逐课运行，例如：

```bash
uv run --locked python run.py --lesson 8 --live
```

`--all --live` 被拒绝，避免意外批量计费；第 7 课仅离线，避免为故意循环付费。真实输出不要求逐字匹配离线文本，但应检查实际 `items`、`last_agent` 和计划内容，不能把“模型没有报错”当作完成了工具使用。

本例固定使用 OpenAI Responses API 端点，不继承 `OPENAI_BASE_URL`，也不自动接入 DeepSeek 等第三方。第三方兼容性应作为后续独立实验验证，而不是通过改一个地址就宣称全部能力可用。

## 会话与安全默认值

默认会话只在内存中，程序退出即丢失。显式指定 ID 才保存到本专题的 `.state/sessions.sqlite`：

```bash
uv run --locked python run.py --lesson 6 --session-id learner_a
```

重复运行会继续追加历史，因此第一次是 4 条会话 item，后续会更多。不同课有独立后缀；换 ID 可开始另一段历史。ID 分区不是鉴权，SQLite 是本地明文，禁止存入公司私有材料、凭据或其他人的会话。程序只在 `finally` 中关闭连接，不会自动删除历史。

安全约束直接落实在代码中：

- 只有两个只读教学工具：固定主题卡片、时间预算；没有 shell、任意路径读取或写业务系统能力。
- 输入主题限定为 `lora` / `kv_cache`；工具参数、输出对象有 schema 校验。
- trace 导出默认全局关闭，包含嵌套 Agent-as-Tool；事件日志只显示类型和工具名。没有配置 API key 也能跑离线课。
- 单课本地等待上限 90 秒、真实请求超时 30 秒、HTTP 自动重试关闭；各 run 有 `max_turns`，嵌套 run 单独设限，模型输出上限配置为 1200 tokens/次。

这些限制**不是严格总费用上限**。输入历史也计入消费；一个 turn 可能产生多个工具请求，嵌套 run 有自己的循环预算；网络超时或取消本地等待，不保证远端未执行、未计费。请另设项目预算/告警并检查实际 usage。1200 tokens 对部分推理任务可能不足，遇到截断先核对原因，不要盲目重试或无限加预算。

护栏用 `[BLOCK_DEMO]` 标记演示机制，**不是**通用 prompt injection 防御。把本例改成有副作用的工具之前，还需要真实权限校验、人工审批、幂等与审计；prompt 不承担授权。

## 排错与验证边界

| 现象 | 先查什么 |
| --- | --- |
| `No module named agents` / 无 testing API | 是否在本目录用锁定环境启动，而不是系统 Python 3.9？ |
| `UnexpectedModelCall` / `UnconsumedModelSteps` | 是否修改了流程，却没同步更新离线脚本和测试？ |
| 配置错误，退出码 2 | 是否同时设置了 key 和模型 ID？是否误用 `--all --live`？ |
| `AuthenticationError` / `PermissionDeniedError` / `NotFoundError` | 核对凭据、项目权限与模型 ID；不要打印密钥排查。 |
| `RateLimitError` / API 网络错误 | 检查 API 项目限额、服务状态和网络；示例不自动重试。 |
| `ModelBehaviorError` | 是否输出截断、schema 不匹配或出现非法工具参数？先对照该课契约。 |
| `MaxTurnsExceeded` / `TimeoutError` | 第 7 课为预期失败；其他课检查循环原因和执行事件。 |
| 只有事件名、没有逐 token 文本 | 有意如此：第 8 课观测事件生命周期，最后展示完整且校验后的输出。 |

入口默认只打印异常类型，不输出 API 响应体或堆栈，避免把敏感请求内容带入日志。需要深入排查时，在本机断点调试 SDK 边界；不要分享未脱敏的请求、响应或会话文件。

实际执行证据与官方资料见 [SOURCES.md](./SOURCES.md)。离线测试覆盖 SDK 控制流，不能证明真实模型能力、API 权限、延迟、费用、第三方兼容性或生产安全。示例不包含 MCP、语音、沙箱、生产部署或审批恢复；不要把“完整教学闭环”理解成“SDK 全 API 图鉴”。
