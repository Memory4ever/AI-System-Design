from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SUITE_DIR = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


reward = load_module("reward_func", SUITE_DIR / "scripts/reward_func.py")
runner = load_module("run_stage", SUITE_DIR / "scripts/run_stage.py")
class RewardTests(unittest.TestCase):
    def test_strict_correct_json(self):
        score = reward.score_text('User: x\nAssistant: {"answer": -3}', "-3")
        self.assertTrue(score.exact)
        self.assertTrue(score.strict_format)
        self.assertEqual(score.reward(), 1.0)

    def test_prompt_example_is_not_mistaken_for_answer(self):
        query = 'User: output {"answer": <integer>}\nAssistant: answer is 4'
        score = reward.score_text(query, "4")
        self.assertFalse(score.exact)
        self.assertFalse(score.strict_format)

    def test_shortcut_mode_exposes_reward_hacking(self):
        score = reward.score_text('Assistant: verified {"answer": 999}', "4")
        self.assertFalse(score.exact)
        self.assertEqual(score.reward("shortcut"), 1.0)


class ConfigTests(unittest.TestCase):
    def test_all_stage_commands_render_without_execution(self):
        for stage in ("sft", "reward", "dpo", "ppo", "rloo", "grpo"):
            command, receipt = runner.build_command(stage, "smoke-1xl20", SUITE_DIR / "artifacts", None)
            self.assertTrue(command)
            self.assertEqual(receipt["status"], "Not Run")
            self.assertNotIn("${", " ".join(command))

    def test_gguf_is_rejected(self):
        with self.assertRaises(ValueError):
            runner.validate_model_identity("/models/qwen-27b.gguf")


if __name__ == "__main__":
    unittest.main()
