"""Dapr lessons use the real SDK, with only the state transport replaced."""

import json
import importlib.util
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest.mock import patch

if importlib.util.find_spec("dapr") is None:
    raise unittest.SkipTest("Dapr 选修课需要 uv sync --extra dapr --locked")

from lab.runtime import Runtime
from lab.dapr_fake import MemoryStateClient
from lessons import dapr as lessons


class DaprLessons(unittest.IsolatedAsyncioTestCase):
    async def test_state_operations_and_partitioning_without_network(self):
        with patch.object(
            socket.socket, "connect", side_effect=AssertionError("network")
        ):
            report = await lessons.state_basics()
        self.assertEqual(
            report["latest"], [{"role": "assistant", "content": "20 分钟"}]
        )
        self.assertEqual(report["other_session"], [])
        self.assertEqual(report["other_store"], [])
        self.assertEqual(report["remaining"], [])
        self.assertTrue(report["injected_client_still_open"])

    async def test_new_session_object_loads_history_into_real_runner(self):
        rt = Runtime()
        with patch.object(
            socket.socket, "connect", side_effect=AssertionError("network")
        ):
            report = await lessons.runner_history(rt)
        self.assertEqual(report["before"], 0)
        self.assertEqual(report["after"], 4)
        self.assertEqual(report["model_input_counts"], [1, 3])
        self.assertIn(
            "20 分钟", json.dumps(rt.models[0].calls[1].input, ensure_ascii=False)
        )
        rt.assert_complete()

    async def test_competing_append_survives_sdk_conflict_retry(self):
        report = await lessons.conflict_boundary()
        self.assertEqual(report["contents"], ["seed", "other writer", "my append"])
        self.assertEqual(report["conflicts"], 1)
        self.assertTrue(report["unavailable_raised"])

    async def test_fake_does_not_invent_etagless_create_guarantees(self):
        from dapr.clients.grpc._state import Concurrency, StateOptions

        client = MemoryStateClient()
        options = StateOptions(concurrency=Concurrency.first_write)
        await client.save_state("store", "key", "first", options=options)
        await client.save_state("store", "key", "second", etag="", options=options)
        self.assertEqual((await client.get_state("store", "key")).data, b"second")


class DaprCLI(unittest.TestCase):
    def command(self, *args):
        return subprocess.run(
            [sys.executable, "run_dapr.py", *args],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            timeout=20,
        )

    def test_all_defaults_to_fake_and_scripted_model(self):
        process = self.command("--all")
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(process.stdout.count("=== "), 3)
        self.assertIn("FAKE STATE", process.stdout)
        self.assertIn('"conflicts": 1', process.stdout)

    def test_sidecar_requires_explicit_single_lesson_and_safe_id(self):
        for args in [
            ["--all", "--sidecar"],
            ["--lesson", "9", "--sidecar"],
            ["--lesson", "10", "--sidecar"],
            ["--lesson", "10", "--sidecar", "--session-id", "../../private"],
        ]:
            with self.subTest(args=args):
                process = self.command(*args)
                self.assertEqual(process.returncode, 2)
                self.assertIn("usage:", process.stderr)


if __name__ == "__main__":
    unittest.main()
