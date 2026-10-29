"""09–11: 保留真实 DaprSession，只把网络/状态库边界替换成教学 fake。

对照安装版本 0.24.0 的 agents/extensions/memory/dapr_session.py。
官方入口：https://openai.github.io/openai-agents-python/sessions/#dapr-sessions
"""

from agents import Agent, Runner
from agents.extensions.memory import DaprSession
from agents.testing import assistant_message

from lab.dapr_fake import MemoryStateClient

STORE = "agentslab"


async def state_basics():
    client = MemoryStateClient()
    # store 是 sidecar 中 Component 的名字，不是数据库 URL；session_id 是会话分区。
    session = DaprSession("lesson09", state_store_name=STORE, dapr_client=client)
    try:
        await session.add_items(
            [
                {"role": "user", "content": "我有 20 分钟"},
                {"role": "assistant", "content": "20 分钟"},
            ]
        )
        # limit 只限制返回的 item 数量，不删除已存历史，也不是 token 预算。
        latest = await session.get_items(limit=1)
        other_session = DaprSession("other", state_store_name=STORE, dapr_client=client)
        other_store = DaprSession(
            "lesson09", state_store_name="other", dapr_client=client
        )
        report = {
            "latest": latest,
            "other_session": await other_session.get_items(),
            "other_store": await other_store.get_items(),
            "popped": await session.pop_item(),
        }
        # 这里只清理 fake 中自己创建的教学数据，不接触用户真实会话。
        await session.clear_session()
        report["remaining"] = await session.get_items()
        await session.close()
        # 注入 client 时生命周期归调用方；close(session) 并不 close(client)。
        report["injected_client_still_open"] = not client.closed
        report["state_events"] = client.events
        return report
    finally:
        await client.close()


async def runner_history(rt, session_factory=None):
    client = None
    if session_factory is None:
        client = MemoryStateClient()

        def session_factory():
            return DaprSession("lesson10", state_store_name=STORE, dapr_client=client)

    agent = Agent(
        name="DaprTutor",
        instructions="读取历史中的学习预算，简短回答。",
        model=rt.model(
            [
                [assistant_message("记住了，你有 20 分钟。")],
                [assistant_message("你之前说有 20 分钟。")],
            ]
        ),
    )
    try:
        async with session_factory() as first:
            before = len(await first.get_items())
            await Runner.run(
                agent,
                "我有 20 分钟学习 Dapr。",
                session=first,
                run_config=rt.config,
                max_turns=2,
            )
        # 第二个 Python Session 对象并不复制第一个对象的字段。
        # Runner 通过相同 store / session_id 重新读历史，再追加当前输入。
        async with session_factory() as reopened:
            result = await Runner.run(
                agent,
                "我之前说有多少时间？",
                session=reopened,
                run_config=rt.config,
                max_turns=2,
            )
            after = len(await reopened.get_items())
        return {
            "before": before,
            "after": after,
            "model_input_counts": [len(call.input) for call in rt.models[-1].calls],
            "output": result.final_output,
            "state_events": client.events if client else [],
        }
    finally:
        if client is not None:
            await client.close()


async def conflict_boundary():
    client = MemoryStateClient()
    session = DaprSession("lesson11", state_store_name=STORE, dapr_client=client)
    try:
        # 先创建 key，获得真实非空 ETag；不把首次无 ETag 创建误当成排他写。
        await session.add_items([{"role": "user", "content": "seed"}])
        client.competing_item = {"role": "user", "content": "other writer"}
        # 真正执行重读/重算/重试的是 SDK；fake 只制造一次冲突。
        await session.add_items([{"role": "user", "content": "my append"}])
        contents = [item["content"] for item in await session.get_items()]
        client.unavailable = True
        unavailable_raised = False
        try:
            await session.get_items()
        except ConnectionError:
            unavailable_raised = True
        return {
            "contents": contents,
            "conflicts": client.conflicts,
            "unavailable_raised": unavailable_raised,
            "state_events": client.events,
        }
    finally:
        await client.close()
