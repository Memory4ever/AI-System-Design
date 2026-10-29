# 逐课理解：先预测，再运行，再解释

每课都使用 `uv run --locked python run.py --lesson N`。先读对应小文件，再运行；不要把 shared runtime 当成必须先学会的框架。所有“预期”默认指锁定版本下的离线教学脚本，真实模型另行检查。

完成第 6 课后，可转入 [Dapr 选修课 9～11](./DAPR.md)，理解如何把同一个 Session 协议接到 sidecar / 状态库。它有独立入口，原八课无需安装 Dapr extra。

## 第 1 课：先把 Agent、模型、Runner 拆开

读 [basic.py](./lessons/basic.py)。关键只看四件事：

```python
agent = Agent(name="Tutor", instructions="...", model=...)
result = await Runner.run(agent, "用户问题", max_turns=3, run_config=...)
print(result.final_output)
print(result.last_agent.name)
```

`Agent` 是 instructions、工具、模型和输出契约等配置的组合；模型负责生成候选回复/调用；`Runner` 驱动循环，最终返回结果。创建 Agent 不等于已经发起一次推理。[官方快速入门](https://developers.openai.com/api/docs/guides/agents/quickstart)

先预测：没有工具时，需要几次模型调用？运行后检查 `message_output_item` 和总调用次数 1。

动手：只改 `instructions` 再离线运行，答案不会自己变化，因为 `assistant_message(...)` 是模型边界脚本。再修改这条脚本，观察输出变化。进入真实模式时不再使用脚本回复。

自测：为什么 `result.final_output` 不是原始 HTTP response？为什么不能根据这课证明模型理解了 Agent？

## 第 2 课：工具不是“把一个函数名写进 prompt”

读 [tools.py](./lessons/tools.py) 和 [domain.py](./lab/domain.py) 的 `lookup_topic`。

```text
用户问题
→ 模型输出 function_call(name, arguments)
→ SDK 验证参数、执行本地 Python 工具
→ 工具结果进入下一次模型输入
→ 模型输出最终消息
```

`@function_tool` 从函数签名和说明构建工具接口。模型只提出调用；真正读字典的是 Python 进程。工具结果不会天然等于最终答案，默认还有下一轮模型处理。

先预测：本课两个模型脚本步骤之间有没有真实 Python 执行？运行后检查三个 item；测试还会检查第二次模型输入包含“低秩”。这比直接调用 `lookup_topic` 的 Python 函数更接近实际运行链。

动手：同时把请求参数与 prompt 改成 `kv_cache`，观察真实工具结果；同步改最终脚本答案。故意给出不存在的主题，观察参数验证错误如何成为工具结果。不要让离线最终脚本继续伪装成功。

自测：哪一步引入业务副作用？如果工具是扣款，能否只靠 instructions 防止重复扣款？

## 第 3 课：本地 Context 不等于上下文窗口

读 [context.py](./lessons/context.py)。`Learner` 含时间预算与仅供测试的 `local_marker`。`Runner.run(..., context=Learner())` 把对象交给应用侧工具/回调；它不会自动把整个对象放进模型消息。

`available_minutes(ctx: RunContextWrapper[Learner])` 只返回 `minutes`。**返回值**才通过工具结果变成模型可见信息；没有把 `local_marker` 返回出去。

先预测：第一次模型输入能否看到 20？第二次为什么能看到？检查测试中的 `calls[0]` / `calls[1]`。留意：预算确实被工具公开了，本例并不意味着工具能返回任意敏感字段。

动手：改 `Learner(minutes=10)`；工具结果会变成 10，但离线最终文本仍可能写 20。这个反例正好说明“控制流跑通”和“最终回答忠实于工具结果”是两项不同验证。真实模式也应测试后者。

自测：数据库连接、租户授权信息适合放在哪一侧？如果把 Context 全部转 JSON 返回给模型，会失去哪条边界？

## 第 4 课：输出契约不只是“请返回 JSON”

读 [structured.py](./lessons/structured.py) 和 `StudyPlan`。`output_type=StudyPlan` 让结果进入结构化输出/验证路径；`final_output` 是 Pydantic 对象，业务代码不用从散文中正则抓字段。

字段限制包括主题枚举、时间范围、步骤数量。但 schema 不知道“20 分钟是否真适合该学习者”，更不知道教材结论是否正确。

先预测：`minutes=0`、缺少 `topic`、超过四步分别会怎样？运行本课，再执行测试中的非法输出用例。

动手：增加一个必填字段，然后**同时**修改模型脚本、真实输出要求和测试。只改 JSON 外观而不更新契约，会造成什么失败？

自测：结构有效、事实正确、工具结果忠实、学习效果良好，为什么要分别验收？

## 第 5 课：两种多 Agent 机制，控制权不同

读 [collaboration.py](./lessons/collaboration.py)。两条路径顺序运行，不是并行竞速。

| 机制 | 控制流 | 本课最终 `last_agent` |
| --- | --- | --- |
| `handoff(specialist)` | Router → Specialist → 最终回答 | `Specialist` |
| `specialist.as_tool(...)` | Manager → 子 run → 工具结果 → Manager 总结 | `Manager` |

Handoff 是下一段对话的 ownership 转移，不是“专家回答后必然自动回 Router”；Agent-as-Tool 是管理者调用一个有边界的子能力。子 run 仍可能使用模型和工具，不是免费函数。[官方编排边界](https://developers.openai.com/api/docs/guides/agents/orchestration)

先预测：交接路径需要 2 次模型调用，管理者路径需要 3 次。运行后查看两个 `last_agent` 与 `handoff_output_item` / `tool_call_output_item`。

动手：把“由专家直接答复”和“由主 Agent 综合多个结果”各举一个工作例子，再选择机制。不要因为有两个角色就默认必须多 Agent。

自测：handoff 后下一轮要继续专家，应选择谁作为 starting agent？本例是否给两个 Agent 进程隔离、独立权限或独立 Context？答案是否定的，名称不同不是安全隔离。

## 第 6 课：记忆必须有明确 owner

读 [sessions.py](./lessons/sessions.py)。两次 run 复用同一个 `SQLiteSession`，第二次输入会加载第一轮用户消息和助手回复。与之不同，第 3 课的 Python Context 不是默认对话存储。

先预测：全新会话第二次模型输入有几项？这里是 3 项：上轮 user、上轮 assistant、本轮 user。完成第二轮后，会话存了 4 项。

动手：用 `--session-id learner_a` 连跑两次，观察条目数增加；再换 `learner_b`。这是历史分区实验，不是多租户鉴权实验。持久化测试会在临时 SQLite 文件中验证关闭后重开，而不是只验证同一个内存对象。

自测：如果自己先拼全部历史，又让 session 加历史，会有什么重复风险？为什么不能用“模型记住了”替代存储、保留期限与历史裁剪的设计？

## 第 7 课：故意失败一次

读 [safety.py](./lessons/safety.py)。本课在一个明确的测试标记上触发 input guardrail，再让工具调用不能在 `max_turns=1` 内形成最终答案。

预期结果：

```json
{"blocked": true, "max_turns_exceeded": true}
```

第一条路径 `run_in_parallel=False`，拦截发生在主模型运行前，测试断言模型调用为 0。第二条路径已经执行一次工具调用，随后 SDK 抛出 `MaxTurnsExceeded`；循环上限不是事务回滚，不能撤销此前工具副作用。

动手：去掉 `[BLOCK_DEMO]` 需要为该路径添加合法模型回复脚本；只删标记但保留空脚本，会触发 `UnexpectedModelCall`。这表明拦截分支确实被绕开了，不是模型“忘了拒绝”。

自测：自动校验与人工审批有什么不同？最终输出护栏能否撤销已发生的写操作？为什么一个关键词 demo 不是安全产品？[官方护栏与审批职责](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)

## 第 8 课：完整学习助手与可观察运行

读 [workflow.py](./lessons/workflow.py)。这次组合已经学过的机制，不额外引入不必要的多 Agent：

```text
输入护栏 → 学习教练
             → 查询 LoRA 教材 → 读取本地时间预算
             → 生成 StudyPlan → SDK 校验 → 展示计划
        SQLiteSession 保存本课历史
        Hooks 观察工具开始/结束；stream_events 消费执行事件
```

运行 `--lesson 8`，预期离线脚本调用模型 3 次，输出一个 20 分钟计划。运行期间打印事件类型/工具名；流消费结束后才读取最终 Pydantic 结果。`raw_response_event` 是模型响应层事件，`run_item_stream_event` 是 SDK 转换出的运行 item 事件，不是每条事件都等于一个文本 token。[运行结果与状态](https://developers.openai.com/api/docs/guides/agents/results)

`RunHooks` 是应用回调，tracing 是另一条观测/导出机制。本例关闭 trace，不把本地事件日志误称为服务端 trace 验收。后续若启用导出，先决定哪些输入输出可以离开本机、保存多久以及谁可以查看。

动手：先让预算工具返回 10，再要求计划时间与之相同。离线时调整脚本及断言，真实时建立一组 10/20/30 分钟样例，分别评估调用是否发生、结果是否忠实、教学内容是否有用。不要拿固定脚本的 100% 测试通过率宣传模型准确率。

最后闭卷解释：把这套助手交付给多人长期使用，你还缺身份认证、真实授权、预算治理、历史保留、幂等重试、评估集和生产监控中的哪些能力？SDK 帮你组织执行，不替你承担这些系统责任。
