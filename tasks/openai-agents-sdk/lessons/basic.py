"""01: Agent is configuration; Runner performs the execution."""

from agents import Agent, Runner
from agents.testing import assistant_message


async def run(rt):
    agent = Agent(
        name="Tutor",
        instructions="用一句中文说明 Agent 与 Runner 的区别。",
        model=rt.model([[assistant_message("Agent 定义行为，Runner 执行循环。")]]),
    )
    return await Runner.run(
        agent, "Agent 和 Runner 分别做什么？", run_config=rt.config, max_turns=3
    )
