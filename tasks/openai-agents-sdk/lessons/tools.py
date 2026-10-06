"""02: model requests a function; SDK executes Python and feeds the result back."""

from agents import Agent, Runner
from agents.testing import assistant_message, function_call

from lab.domain import lookup_topic


async def run(rt):
    model = rt.model(
        [
            [function_call("lookup_topic", {"topic": "lora"}, call_id="lookup-1")],
            [assistant_message("LoRA 训练低秩增量；共享基座并不消除额外执行。")],
        ]
    )
    agent = Agent(
        name="CatalogTutor",
        model=model,
        tools=[lookup_topic],
        instructions="先调用 lookup_topic 查询 lora，再用中文解释，不能假装已经查询。",
    )
    return await Runner.run(
        agent, "请查询教材中的 LoRA 定义。", run_config=rt.config, max_turns=4
    )
