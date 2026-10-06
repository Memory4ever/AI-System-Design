import json
import unittest

from lab.runtime import Runtime
from lessons import basic, tools, context
from lessons import structured, collaboration, sessions, safety, workflow
from lab.domain import StudyPlan


class FirstLessons(unittest.IsolatedAsyncioTestCase):
    async def test_basic_runs_real_sdk_once(self):
        runtime = Runtime()
        result = await basic.run(runtime)
        self.assertEqual(result.final_output, "Agent 定义行为，Runner 执行循环。")
        self.assertEqual(len(runtime.models[0].calls), 1)
        runtime.assert_complete()


class AdvancedLessons(unittest.IsolatedAsyncioTestCase):
    async def test_output_is_validated_pydantic_object(self):
        runtime = Runtime()
        result = await structured.run(runtime)
        self.assertIsInstance(result.final_output, StudyPlan)
        self.assertEqual(result.final_output.minutes, 20)
        self.assertIsNotNone(runtime.models[0].first_call.output_schema)
        runtime.assert_complete()

    async def test_handoff_transfers_but_agent_tool_returns_to_manager(self):
        runtime = Runtime()
        handed, managed = await collaboration.run(runtime)
        self.assertEqual(handed.last_agent.name, "Specialist")
        self.assertEqual(managed.last_agent.name, "Manager")
        self.assertIn("handoff_output_item", [x.type for x in handed.new_items])
        self.assertIn("tool_call_output_item", [x.type for x in managed.new_items])
        runtime.assert_complete()

    async def test_session_loads_prior_turn_into_second_call(self):
        runtime = Runtime()
        await sessions.run(runtime)
        calls = runtime.models[0].calls
        self.assertEqual(len(calls[0].input), 1)
        self.assertEqual(len(calls[1].input), 3)
        self.assertIn("20 分钟", json.dumps(calls[1].input, ensure_ascii=False))
        runtime.assert_complete()

    async def test_guardrail_blocks_before_model_and_turn_limit_stops_loop(self):
        runtime = Runtime()
        report = await safety.run(runtime)
        self.assertTrue(report["blocked"])
        self.assertTrue(report["max_turns_exceeded"])
        self.assertEqual(len(runtime.models[0].calls), 0)
        self.assertEqual(len(runtime.models[1].calls), 1)
        runtime.assert_complete()

    async def test_streamed_workflow_executes_tools_and_validates_plan(self):
        runtime = Runtime()
        result = await workflow.run(runtime)
        self.assertIsInstance(result.final_output, StudyPlan)
        self.assertIn("tool:start:lookup_topic", runtime.events)
        self.assertIn("tool:end:available_minutes", runtime.events)
        self.assertIn("stream:raw_response_event", runtime.events)
        self.assertIn("stream:run_item_stream_event", runtime.events)
        self.assertEqual(len(runtime.models[0].calls), 3)
        runtime.assert_complete()

    def test_live_mode_fails_closed_without_credentials_or_model(self):
        from unittest.mock import patch

        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                Runtime(live=True)

    async def test_tool_result_reaches_next_model_call(self):
        runtime = Runtime()
        result = await tools.run(runtime)
        self.assertEqual(
            [item.type for item in result.new_items],
            ["tool_call_item", "tool_call_output_item", "message_output_item"],
        )
        observation = runtime.models[0].calls[1].input
        outputs = [x for x in observation if x.get("type") == "function_call_output"]
        self.assertIn("低秩", outputs[0]["output"])
        runtime.assert_complete()

    async def test_local_context_is_not_automatically_sent_to_model(self):
        runtime = Runtime()
        await context.run(runtime)
        calls = runtime.models[0].calls
        self.assertNotIn("LOCAL_ONLY_MARKER", json.dumps(calls[0].input))
        self.assertNotIn("LOCAL_ONLY_MARKER", calls[0].system_instructions)
        self.assertIn("20", json.dumps(calls[1].input))
        self.assertNotIn("LOCAL_ONLY_MARKER", json.dumps(calls[1].input))
        runtime.assert_complete()
