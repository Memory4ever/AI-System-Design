"""Negative cases and executable CLI checks, with no external model calls."""

import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from agents import Agent, ModelBehaviorError, Runner, SQLiteSession
from agents.testing import ScriptedModel, assistant_message, function_call

from lab.domain import PLAN, StudyPlan, lookup_topic
from lab.runtime import Runtime
from lessons import (
    basic,
    collaboration,
    context,
    safety,
    sessions,
    structured,
    tools,
    workflow,
)

ROOT = Path(__file__).resolve().parents[1]


class Boundaries(unittest.IsolatedAsyncioTestCase):
    async def test_all_lessons_work_when_network_connections_are_forbidden(self):
        with patch.object(
            socket.socket, "connect", side_effect=AssertionError("network forbidden")
        ):
            for lesson in [
                basic,
                tools,
                context,
                structured,
                collaboration,
                sessions,
                safety,
                workflow,
            ]:
                runtime = Runtime()
                await lesson.run(runtime)
                runtime.assert_complete()

    async def test_invalid_structured_output_is_not_silently_accepted(self):
        runtime = Runtime()
        bad = dict(PLAN, minutes=0)
        model = ScriptedModel([[assistant_message(json.dumps(bad))]])
        with self.assertRaises(ModelBehaviorError):
            await Runner.run(
                Agent(name="BadPlanner", model=model, output_type=StudyPlan),
                "test",
                run_config=runtime.config,
                max_turns=2,
            )

    async def test_invalid_tool_argument_does_not_access_arbitrary_path(self):
        runtime = Runtime()
        model = ScriptedModel(
            [
                [
                    function_call(
                        "lookup_topic", {"topic": "../../private"}, call_id="bad"
                    )
                ],
                [assistant_message("参数不合法，不能查询。")],
            ]
        )
        result = await Runner.run(
            Agent(name="Tutor", model=model, tools=[lookup_topic]),
            "test",
            run_config=runtime.config,
            max_turns=3,
        )
        outputs = [
            item for item in result.new_items if item.type == "tool_call_output_item"
        ]
        self.assertIn("error", outputs[0].output.lower())
        self.assertNotIn("../../private", outputs[0].output)
        model.assert_complete()

    async def test_sqlite_persists_and_session_ids_partition_history(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.sqlite"
            first = SQLiteSession("learner-a", path)
            await first.add_items(
                [{"role": "user", "content": "public teaching fixture"}]
            )
            first.close()
            reopened = SQLiteSession("learner-a", path)
            other = SQLiteSession("learner-b", path)
            try:
                self.assertEqual(len(await reopened.get_items()), 1)
                self.assertEqual(await other.get_items(), [])
            finally:
                reopened.close()
                other.close()


class CommandLine(unittest.TestCase):
    def command(self, *args):
        env = {
            key: value
            for key, value in os.environ.items()
            if key not in {"OPENAI_API_KEY", "OPENAI_MODEL"}
        }
        return subprocess.run(
            [sys.executable, "run.py", *args],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )

    def test_all_without_key(self):
        process = self.command("--all")
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(process.stdout.count("=== "), 8)
        self.assertIn("OFFLINE", process.stdout)

    def test_live_without_key_fails_before_network(self):
        process = self.command("--lesson", "1", "--live")
        self.assertEqual(process.returncode, 2)
        self.assertIn("OPENAI_API_KEY", process.stderr)

    def test_live_all_is_rejected(self):
        self.assertEqual(self.command("--all", "--live").returncode, 2)

    def test_invalid_session_id_is_rejected(self):
        self.assertEqual(self.command("--session-id", "../../escape").returncode, 2)
