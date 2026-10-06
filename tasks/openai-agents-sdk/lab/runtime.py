"""Only the model boundary changes between offline and live execution."""

import os
from pathlib import Path

from agents import ModelSettings, OpenAIResponsesModel, RunConfig, SQLiteSession
from agents import set_tracing_disabled
from agents.testing import ScriptedModel
from openai import AsyncOpenAI


class Runtime:
    def __init__(self, *, live=False, model_name=None, session_id=None, on_event=None):
        self.live = live
        self.model_name = model_name
        self.session_id = session_id
        self.models = []
        self.events = []
        self.on_event = on_event
        self.client = None
        # Disable export globally too: nested agent-as-tool runs must not leak traces.
        set_tracing_disabled(True)
        self.config = RunConfig(
            tracing_disabled=True,
            model_settings=ModelSettings(max_tokens=1200, parallel_tool_calls=False),
        )
        if live:
            key = os.environ.get("OPENAI_API_KEY", "").strip()
            if not key or not model_name:
                raise ValueError(
                    "真实调用需要 OPENAI_API_KEY 和 OPENAI_MODEL；不要把 key 发到聊天中。"
                )
            # Explicit endpoint: do not silently inherit a third-party OPENAI_BASE_URL.
            self.client = AsyncOpenAI(
                api_key=key,
                base_url="https://api.openai.com/v1",
                timeout=30.0,
                max_retries=0,
            )

    def model(self, steps):
        if self.live:
            return OpenAIResponsesModel(
                model=self.model_name, openai_client=self.client
            )
        model = ScriptedModel(steps)
        self.models.append(model)
        return model

    def session(self, lesson):
        if self.session_id is None:
            return SQLiteSession(f"memory-{lesson}")
        state_dir = Path(__file__).resolve().parents[1] / ".state"
        state_dir.mkdir(exist_ok=True)
        # IDs partition history only; they are NOT an authorization mechanism.
        return SQLiteSession(
            f"{self.session_id}:{lesson}", state_dir / "sessions.sqlite"
        )

    def assert_complete(self):
        for model in self.models:
            model.assert_complete()

    def record(self, event):
        self.events.append(event)
        if self.on_event is not None:
            self.on_event(event)

    async def close(self):
        if self.client is not None:
            await self.client.close()
