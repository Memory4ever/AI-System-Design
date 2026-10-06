"""04: validate the output contract instead of parsing prose."""

import json

from agents import Agent, Runner
from agents.testing import assistant_message

from lab.domain import PLAN, StudyPlan


async def run(rt):
    agent = Agent(
        name="Planner",
        output_type=StudyPlan,
        instructions="为 lora 生成 20 分钟学习计划，最多四步，并附一个理解检查问题。",
        model=rt.model([[assistant_message(json.dumps(PLAN, ensure_ascii=False))]]),
    )
    return await Runner.run(
        agent, "我想理解多 LoRA 推理。", run_config=rt.config, max_turns=3
    )
