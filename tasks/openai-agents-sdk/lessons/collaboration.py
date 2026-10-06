"""05: same specialist capability, two different control-flow contracts."""

from agents import Agent, Runner, handoff
from agents.testing import assistant_message, function_call


# 本课用同一个问题对比两条执行路径；两次 Runner.run 是独立实验，并非串成一条对话：
#   handoff：Router → Specialist → 用户（专家接管，Router 不再回来总结）
#   as_tool：Manager → [调用 SpecialistTool → 返回工具结果] → Manager → 用户
# 它们都是 SDK 在当前应用内编排的 Agent，不代表自动启动独立进程或远程服务。
# 官方机制说明：https://developers.openai.com/api/docs/guides/agents/orchestration
async def run(rt):
    # rt 是 lab/runtime.py 的 Runtime。默认离线时，rt.model(steps) 创建脚本模型：
    # 外层列表的每一项对应一次模型调用，内层列表是该次调用返回的消息/工具调用。
    # assistant_message(...) 模拟模型回答，function_call(...) 模拟模型提出调用请求；
    # 后者不是直接执行 Python 函数，真正的交接/工具执行仍由 Runner 完成。
    # --live 时这些预设 steps 被忽略，改由真实模型根据 instructions 决策。

    # ① Handoff：先定义接手工作的专家。这里只创建 Agent，尚未执行模型调用。
    specialist = Agent(
        name="Specialist",
        instructions="用中文简述 KV Cache 的计算/显存取舍。",
        model=rt.model([[assistant_message("KV Cache 用显存换历史计算复用。")]]),
    )
    router = Agent(
        name="Router",
        instructions="把请求交接给 Specialist，不自行回答。",
        # 注册允许交接的目标，并指定模型看到的交接工具名称。
        # 注册本身不触发交接；Router 的模型必须实际请求调用这个名称。
        handoffs=[handoff(specialist, tool_name_override="transfer_to_specialist")],
        model=rt.model(
            [
                [
                    # 无额外业务参数，所以传 {}；call_id 用来关联调用与其结果。
                    function_call("transfer_to_specialist", {}, call_id="handoff-1"),
                ]
            ]
        ),
    )
    # Runner 先调用 Router；收到交接请求后切换到 Specialist，继续同一个 run。
    # 本例没有过滤历史，专家会接到已有对话；其最终回答直接成为 handed.final_output。
    # await 等待整个 run 结束；max_turns=4 限制模型调用轮数，不是限制 4 个 Agent。
    handed = await Runner.run(
        router, "解释 KV Cache。", run_config=rt.config, max_turns=4
    )

    # ② Agent-as-Tool：专家只提供子任务结果，Manager 保留最终回答权。
    # 重新建实例是为了隔离离线脚本：上一个专家的预设回答已被消费。
    # 不是说真实应用里的 Agent 每次使用后都必须重建。
    helper = Agent(
        name="SpecialistTool",
        instructions="用中文简述 KV Cache 的计算/显存取舍。",
        model=rt.model([[assistant_message("KV Cache 用显存换历史计算复用。")]]),
    )
    # as_tool() 把 Agent 包装成可注册的工具，此处仍未运行专家。
    # 工具被调用时，SDK 启动嵌套的专家 run，再把其输出作为工具结果交回 Manager。
    # 这里的 max_turns=3 只约束专家子 run；外层 Manager 有自己的轮数限制。
    consult = helper.as_tool(
        tool_name="consult_specialist",
        tool_description="咨询 KV Cache 专家。",
        run_config=rt.config,
        max_turns=3,
    )
    manager = Agent(
        name="Manager",
        # 注意这里放在 tools，而不是 handoffs：咨询专家，不转交整段对话的控制权。
        tools=[consult],
        instructions="先调用 consult_specialist 咨询专家，再自行总结并给出学习建议。",
        model=rt.model(
            [
                [
                    # Manager 第一次模型调用：发出咨询请求。
                    # input 是专家子 run 的输入文本，不是 Python 的 input()。
                    function_call(
                        "consult_specialist",
                        {"input": "解释 KV Cache。"},
                        call_id="consult-1",
                    )
                ],
                [
                    # Manager 第二次模型调用：Runner 已把专家结果加入其输入历史，
                    # Manager 据此组织面向用户的最终回答，而非直接退出给专家。
                    assistant_message(
                        "专家指出它用显存换计算；建议先估算每 token 的缓存大小。"
                    )
                ],
            ]
        ),
    )
    # 外层执行顺序：Manager 调模型 → 执行 consult（内部跑专家）→ Manager 再调模型。
    managed = await Runner.run(
        manager, "解释 KV Cache 并给我学习建议。", run_config=rt.config, max_turns=4
    )
    # 可从结果验证差异：handed.last_agent.name == "Specialist"，
    # managed.last_agent.name == "Manager"；两者 final_output 也来自不同的回答者。
    return handed, managed
