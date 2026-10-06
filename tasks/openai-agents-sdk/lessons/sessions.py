"""06: sessions persist conversation items, not all Python application state."""

from agents import Agent, Runner
from agents.testing import assistant_message


async def run(rt):
    agent = Agent(
        name="SessionTutor",
        instructions="记住对话中的学习预算，用简短中文回答。",
        model=rt.model(
            [
                [assistant_message("记住了，你今天有 20 分钟。")],
                [assistant_message("你刚才说今天有 20 分钟。")],
            ]
        ),
    )
    session = rt.session("06")
    try:
        await Runner.run(
            agent,
            "我今天有 20 分钟学习 LoRA。",
            session=session,
            run_config=rt.config,
            max_turns=3,
        )
        result = await Runner.run(
            agent,
            "我刚才说有多少时间？",
            session=session,
            run_config=rt.config,
            max_turns=3,
        )
        rt.record(f"session:items:{len(await session.get_items())}")
        return result
    finally:
        session.close()
