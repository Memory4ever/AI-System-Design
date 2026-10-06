"""08: a complete, bounded study-planner workflow with observable events."""

import json

from agents import Agent, RunHooks, Runner
from agents.testing import assistant_message, function_call

from lab.domain import PLAN, Learner, StudyPlan, available_minutes, lookup_topic
from lessons.safety import teaching_guardrail


class Timeline(RunHooks):
    def __init__(self, record):
        self.record = record

    async def on_tool_start(self, context, agent, tool):
        self.record(f"tool:start:{tool.name}")

    async def on_tool_end(self, context, agent, tool, result):
        # Log event metadata only, not arguments, results or local user fields.
        self.record(f"tool:end:{tool.name}")


async def run(rt):
    agent = Agent[Learner](
        name="StudyCoach",
        instructions=(
            "你是 AI System 学习教练。必须先 lookup_topic 查询 lora，"
            "再 available_minutes 查询预算；根据两者制定中文计划。"
            "不访问教材之外的文件，不声称完成了任何真实实验。"
        ),
        tools=[lookup_topic, available_minutes],
        output_type=StudyPlan,
        input_guardrails=[teaching_guardrail],
        model=rt.model(
            [
                [function_call("lookup_topic", {"topic": "lora"}, call_id="plan-1")],
                [function_call("available_minutes", {}, call_id="plan-2")],
                [assistant_message(json.dumps(PLAN, ensure_ascii=False))],
            ]
        ),
    )
    session = rt.session("08")
    try:
        result = Runner.run_streamed(
            agent,
            "为我制定理解多 LoRA 推理的学习计划。",
            context=Learner(),
            session=session,
            hooks=Timeline(rt.record),
            run_config=rt.config,
            max_turns=6,
        )
        # Consume to completion before accessing final_output/usage or closing SQLite.
        async for event in result.stream_events():
            rt.record(f"stream:{event.type}")
        return result
    finally:
        session.close()
