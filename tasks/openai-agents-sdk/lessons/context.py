"""03: application dependencies are not automatically model-visible messages."""

from agents import Agent, Runner
from agents.testing import assistant_message, function_call

from lab.domain import Learner, available_minutes


async def run(rt):
    agent = Agent[Learner](
        name="ContextTutor",
        tools=[available_minutes],
        instructions="先用 available_minutes 读取时间预算，再给出一句学习建议。",
        model=rt.model(
            [
                [function_call("available_minutes", {}, call_id="budget-1")],
                [assistant_message("今天有 20 分钟，先学 LoRA 的权重和执行边界。")],
            ]
        ),
    )
    return await Runner.run(
        agent,
        "我今天应该怎么安排？",
        context=Learner(),
        run_config=rt.config,
        max_turns=4,
    )
