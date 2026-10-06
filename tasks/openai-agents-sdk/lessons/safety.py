"""07: deterministic negative tests; deliberately no paid loop demonstration."""

from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    MaxTurnsExceeded,
    Runner,
    input_guardrail,
)
from agents.testing import function_call

from lab.domain import lookup_topic


@input_guardrail(run_in_parallel=False)
async def teaching_guardrail(ctx, agent, user_input):
    # This marker is a reproducible teaching case, NOT a prompt-injection detector.
    blocked = isinstance(user_input, str) and "[BLOCK_DEMO]" in user_input
    return GuardrailFunctionOutput(
        output_info={"rule": "demo-marker", "blocked": blocked},
        tripwire_triggered=blocked,
    )


async def run(rt):
    if rt.live:
        raise ValueError("第 7 课故意触发失败，仅允许离线运行。")
    agent = Agent(
        name="GuardedTutor", model=rt.model([]), input_guardrails=[teaching_guardrail]
    )
    report = {"blocked": False, "max_turns_exceeded": False}
    try:
        await Runner.run(agent, "[BLOCK_DEMO]", run_config=rt.config, max_turns=2)
    except InputGuardrailTripwireTriggered:
        report["blocked"] = True

    looping = Agent(
        name="LoopTutor",
        tools=[lookup_topic],
        model=rt.model(
            [
                [
                    function_call("lookup_topic", {"topic": "lora"}, call_id="loop-1"),
                ]
            ]
        ),
    )
    try:
        await Runner.run(looping, "查询后还要继续。", run_config=rt.config, max_turns=1)
    except MaxTurnsExceeded:
        report["max_turns_exceeded"] = True
    return report
