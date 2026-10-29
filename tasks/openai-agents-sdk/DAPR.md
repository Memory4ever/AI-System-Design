# Dapr 选修课：把 Agent 的会话状态移出 Python 进程

建议先完成第 6 课 Session，再按 9 → 10 → 11 学习。每课先预测、运行、对照事件，再改一个变量。源码有中文注释；这里不是 Dapr 全 API 图鉴，也不是生产部署方案。

## 先建立一张心智地图

单进程时，把历史放进 SQLite 很直接。应用增加 worker 后，问题变成：谁能读到历史、怎么配置共享状态库、并发更新会不会丢失？可以直接使用 Redis/Postgres 客户端或 SDK 的其他 Session 后端；**不必为了 Agent 强行引入 Dapr**。

Dapr（Distributed Application Runtime）把状态管理、服务调用、Pub/Sub、Workflow 等分布式能力暴露成 HTTP/gRPC API；sidecar 是与应用并行运行的 `daprd` 进程，不是 Python 中的 Agent 对象。[Dapr building blocks](https://docs.dapr.io/concepts/building-blocks-concept/)、[sidecar 架构](https://docs.dapr.io/concepts/dapr-services/sidecar/)

本课程只使用其中的 **State Management**：

```text
应用进程
  Agent：指令、模型、工具配置
  Runner：读历史 → 调模型/工具 → 保存新 item
     │ Session 协议
  DaprSession：会话 item ↔ key/value
     │ Dapr Python client：本例状态 API 走 gRPC
     ▼
本机 daprd sidecar
     │ 名为 agentslab 的 Component，type=state.redis
     ▼
Redis：实际保存数据（持久化、复制、备份另行配置）
```

`state_store_name="agentslab"` 对应 YAML 的 `metadata.name`，不是 Redis URL。Redis 地址属于 Component；`session_id` 选择对话；Dapr `app-id` 又是应用标识，默认还会参与底层状态 key 的命名。它们不是同一个 ID。[状态 API key scheme](https://docs.dapr.io/reference/api/state_api/#key-scheme)

价值在于应用面向统一状态 API、组件负责后端连接；代价是多一跳、sidecar 生命周期、组件配置和更多故障边界。更换 Component 不等于自动搬迁数据，也不保证不同后端的 TTL、一致性、ETag、容量与延迟完全一致。已有共享数据库方案合适时，直接连接可能更简单。

## 安装与运行：先不启动任何服务

保持主教程的 `openai-agents==0.24.0`；Dapr 是可选 extra，依赖版本写入同一份 `uv.lock`：

```bash
cd /Users/apple/Documents/Work/PycharmProject/AI-System-Design/tasks/openai-agents-sdk
uv sync --locked --extra dapr --python 3.11
uv run --locked --extra dapr python run_dapr.py --lesson 9
uv run --locked --extra dapr python run_dapr.py --lesson 10
uv run --locked --extra dapr python run_dapr.py --lesson 11
```

也可 `uv run --locked --extra dapr python run_dapr.py --all`。原 `run.py` 仍只运行 1～8 课；不把额外服务依赖悄悄加进原八课。

默认是真 `DaprSession` + 真 `Runner` + SDK `ScriptedModel`，只把 Dapr 状态传输替换成 [MemoryStateClient](./lab/dapr_fake.py)。不需要 API key，不访问模型或 Dapr 网络服务，不上传 SDK trace。安装依赖仍需网络。**fake 在程序退出时丢失数据，不实现 TTL、复制、鉴权或完整 Dapr 协议。**

## 第 9 课：从 Session 操作看见 key/value

入口：[state_basics](./lessons/dapr.py)。先预测：存两条 item 后，`get_items(limit=1)` 会不会删除第一条？`close()` 会不会清空会话？

运行后应看到：

```text
GET agentslab/lesson09:messages etag=absent
SAVE agentslab/lesson09:messages etag=absent
GET agentslab/lesson09:metadata etag=absent
SAVE agentslab/lesson09:metadata etag=absent
```

对照锁定 SDK 的实现：历史序列化到 `<session_id>:messages`，时间等派生信息在 `<session_id>:metadata`。`add_items()` 读出历史，再写回扩展后的列表；不是一条消息对应一个独立数据库行。它们是版本相关实现细节，不要让业务代码直接依赖这些内部 key。

观察返回值：

- `latest` 只有最后一条；`limit` 限制返回的 item 数量，不是 token 预算，不会自动裁剪库内历史。当前实现仍需读取整个 messages 值。
- `other_session` / `other_store` 为空，说明会话与 store 分区不同。fake 不模拟 Dapr app-id 前缀；任何 ID 都不是用户认证或租户授权。
- `pop_item()` 移走最后一个 item，不一定是一整轮问答，更不撤销已经执行的业务工具。
- `clear_session()` 删除当前会话的两个 key；本课只操作 fake。两个删除不是本例承诺的跨 key 事务。
- 注入 client 时，`session.close()` 不关闭它；调用方负责最终 `client.close()`。`from_address()` 则创建并拥有 client，退出 `async with` 后该 Session 对象不可再用。关闭连接不等于删除状态。

小实验：把 `limit=1` 改成 `2`，先写下预期，再运行。再把另一个 Session 的 ID 改成 `lesson09`，观察它会不会读到同一历史。

自测：如果只知道一个 session ID 就能读取其历史，缺少的安全控制应该在谁那里？答案是应用授权与状态库/sidecar 访问控制，而不是换一个更难猜的 ID。

## 第 10 课：新建 Session 对象，为什么还能继续对话？

入口：[runner_history](./lessons/dapr.py)。第一轮告诉教练“有 20 分钟”，关闭第一对象；第二轮创建同 store、同 ID 的新对象，只提交新问题。

预测第二次模型调用的输入条数。默认空 fake 的结果应是：

```json
{"before": 0, "after": 4, "model_input_counts": [1, 3]}
```

第一轮输入 1 条 user item，完成后保存 user + assistant；第二轮是这 2 条历史加 1 条新输入，所以模型看到 3 条。第二轮结束再新增 2 条，库里共 4 条。[SDK conversation strategies](https://developers.openai.com/api/docs/guides/agents/running-agents#choose-one-conversation-strategy)

这不是模型“记住”了 Python 变量，而是 Runner 经 Session 重新取得历史。不要同时手工把完整旧历史塞进新输入，否则可能重复上下文。DaprSession 不负责检索知识库、修改模型权重或决定哪些记忆最重要。

固定答案来自 ScriptedModel，**只看“20 分钟”的答案不能证明历史传递成功**。测试会检查模型实际输入中含第一轮内容；事件展示实际状态读写。

小实验：把第二个对象改成不同 session ID，预测输入会退回几条。离线答案仍由脚本规定，不会自动变聪明；应该检查模型输入，而不是把固定文本当成记忆能力。

默认只证明“新 Python 对象读到共享 fake 的历史”，**不证明重启进程后仍在**。真实持久化需要下面的可选实验。

## 第 11 课：ETag 能保护什么，不能保护什么？

入口：[conflict_boundary](./lessons/dapr.py)。先存 `seed`，让 messages key 已有 ETag；然后在本次读后、写前插入另一个写者。

```text
A 读到 revision 1
B 写入 other writer，revision 变为 3
A 带旧 ETag 写入 → 冲突
SDK 重读最新历史 → 重新追加 my append → 写入
最终：seed / other writer / my append
```

revision 中间还包含 metadata 写入，所以不必连续。输出 `conflicts=1`，同时保留两个写者的 item，才是本课要观察的结果。fake 只制造冲突，重读与重试来自真实 SDK。锁定版本对识别出的写冲突做有界重试；持续冲突或其他错误仍可能失败，不应写无上限重试循环。

ETag 是“我基于哪个版本更新”的乐观并发条件，不是分布式锁。Dapr 官方约定无 ETag 写入按 last-write-wins；所以本课先创建 key，**不能把本次结果外推为首次并发创建不会丢写**。[Dapr concurrency](https://docs.dapr.io/reference/api/state_api/#concurrency)

更重要的是：两个请求仍可能都先读到同一历史，各自生成回答。单次 append 防丢写，不代表整段 `读历史 → 调模型/工具 → 保存` 已串行。SDK 的对象内锁也不是跨进程 turn 锁；同一会话多请求需应用排队或其他明确协调策略。

最后故意让 fake 后端不可用，观察 `unavailable_raised=true`：读取失败不会在本课自动变成空历史成功。真实系统要区分不存在、超时、不可用、损坏；不能为了“继续回答”而悄悄换新会话。存储确认也可能处于未知状态，盲目重试整个业务动作会重复执行。

小实验：注释 `client.competing_item = ...` 那一行，预测 `conflicts` 与历史，再运行；完成后恢复。不要把故障注入接到真实业务库。

以下边界只做源码/资料解释，不是 fake 验收结果：

| 选项或对象 | 实际含义 | 不意味着 |
| --- | --- | --- |
| `ttl=3600` | 写入状态时请求后端 TTL | 所有后端都支持；关闭进程立即清除；固定从首次创建起算 |
| `ttl=None` | 此 SDK 不发送每次写入的 TTL 值 | 覆盖数据库已有的全局过期策略 |
| `consistency="strong"` | 锁定版本在写/删选项上请求 strong；依赖后端 | 自动获得线性一致的整轮对话；其读 metadata 不等同 wire-level 强一致读字段 |
| DaprSession | 保存会话 item 与派生 metadata | 自动保存任意本地 Context、Python 栈、工具副作用、审批 checkpoint |
| Dapr Workflow | 独立的持久化执行机制 | 传入 `session=` 就已经启用了 Workflow |

TTL 的有效性与重新写入后的过期行为需按实际组件验证；SDK 的 messages/metadata 也不是一个事务。Workflow 即使支持恢复，也需要业务设计幂等，不能把外部工具一律当成 exactly-once。[TTL](https://docs.dapr.io/developing-applications/building-blocks/state-management/state-store-ttl/)、[Dapr building blocks](https://docs.dapr.io/concepts/building-blocks-concept/)

## 可选实操：换回真实 sidecar，模型仍离线

**本次未执行这一层。** 当前机器未发现 Dapr CLI；没有替你安装系统服务、运行 `dapr init`、启动容器或使用公司 Redis。下面是待你准备环境后执行的实验步骤，不是已成功部署记录。

先按 [官方自托管安装指南](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-with-docker/) 准备 Dapr CLI/runtime 与专用教学 Redis。`dapr init` 会写本机 Dapr 配置并启动依赖；请先了解这些变化，不要在生产环境照搬。组件 [agentslab.yaml](./dapr/components/agentslab.yaml) 假设 Redis 是本机 `127.0.0.1:6379`、无密码，仅适合隔离的本机公开教学数据；不要指向业务库或暴露端口到公网。

确认组件配置与本机环境一致后，在本目录执行：

```bash
uv sync --locked --extra dapr
dapr run --app-id agents-sdk-dapr-lab --resources-path ./dapr/components \
  --dapr-http-port 3500 --dapr-grpc-port 50001 \
  -- .venv/bin/python run_dapr.py --lesson 10 --sidecar --session-id learner_a
```

这里只消费状态 API，不监听业务端口，因此不用 `--app-port`。CLI 参数依据 [dapr run reference](https://docs.dapr.io/reference/cli/dapr-run/)。Python 端固定 gRPC `127.0.0.1:50001`，并在 Dapr 导入前固定 HTTP health endpoint 为 `http://127.0.0.1:3500`；两端口用途不同，健康检查成功也不保证组件读写成功。入口配置健康等待与状态 API 请求超时，另有协程 30 秒限时；同步构造器的健康检查不受 asyncio 取消精确控制，不能宣称严格总耗时上限。

只接受第 10 课单独使用 `--sidecar`，且必须显式传教学 ID；实际 Session ID 加 `agents-lab-dapr:` 前缀，TTL 请求为 3600 秒。不自动清空历史，也没有真实库删除命令。日志只打印公开教学答案、item 数量；无需 API key，没有真实 LLM 调用。Dapr 自身的日志/遥测策略另由你的运行环境决定。

同一命令运行两次：在组件、app-id、ID、Redis 未变化且数据未过期时，第一次预期 `before=0, after=4`，第二次 `before=4, after=8`。这才检验跨 Python 进程的状态延续。若已有同 ID 数据，第一次不一定从 0 开始。换 ID 应开始另一段历史；换 app-id 默认可能进入另一 key 命名空间。

这仍不证明 Redis 故障后不丢数据：关闭/重启 sidecar、重启 Redis、丢失 Redis 容器存储是三个不同实验，后两者取决于 Redis 持久化和部署设置。不要用业务数据做破坏性验证。

| 现象 | 先核对 |
| --- | --- |
| optional dependency 错误 | 是否加了 `--extra dapr`？只 `uv run` 可能同步回基础依赖集。 |
| HTTP health 超时 | sidecar 是否启动、HTTP 3500 是否正确、端口是否被占用？ |
| gRPC 不可用 | Python 与 sidecar 的 50001 是否匹配？ |
| state store 不存在/初始化失败 | 是否加载 `dapr/components`；组件名是否是 `agentslab`；Redis 是否可连接？ |
| 第二次历史为空 | store、app-id、session ID、TTL、Redis 实例与持久化是否变化？ |
| 吞吐变差/历史越来越大 | 测量状态 RPC、整个 messages 值的读改写、模型输入长度；共享状态不是免费性能优化。 |

## 自己验收，而不是只看日志“没报错”

```bash
uv run --locked --extra dapr python -m unittest discover -s tests -p test_dapr_lessons.py -v
```

测试包括禁网的状态操作、Runner 实际模型输入、冲突重试后历史、无 ETag 写入边界、CLI 默认模式与参数约束。fake 不能验收真实后端；sidecar 路径还需你按上面的前后计数实测。版本、来源和本次执行范围见 [SOURCES.md](./SOURCES.md)。
