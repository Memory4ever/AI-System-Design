"""教学用状态传输替身，不是 Dapr sidecar，也不提供磁盘持久化或 TTL。"""

from dataclasses import dataclass
import json


@dataclass
class StateResponse:
    data: bytes = b""
    etag: str = ""


class MemoryStateClient:
    """只实现 DaprSession 用到的三个状态 API；用于观察 SDK，而非复刻 Dapr。"""

    def __init__(self):
        self.state = {}
        self.revision = 0
        self.events = []
        self.closed = False
        self.unavailable = False
        self.competing_item = None
        self.conflicts = 0

    def check_available(self):
        if self.unavailable:
            raise ConnectionError("teaching state store unavailable")

    def commit(self, identity, value):
        self.revision += 1
        payload = value.encode("utf-8") if isinstance(value, str) else value
        self.state[identity] = StateResponse(payload, str(self.revision))

    async def get_state(self, store_name, key, state_metadata=None):
        self.check_available()
        response = self.state.get((store_name, key), StateResponse())
        self.events.append(f"GET {store_name}/{key} etag={response.etag or 'absent'}")
        return response

    async def save_state(
        self, store_name, key, value, state_metadata=None, options=None, etag=None
    ):
        self.check_available()
        identity = (store_name, key)
        # 第 11 课：在 SDK 读后、写前插入另一个写者，确定性制造 stale ETag。
        if key.endswith(":messages") and self.competing_item is not None:
            messages = json.loads(self.state[identity].data)
            messages.append(json.dumps(self.competing_item))
            self.competing_item = None
            self.commit(identity, json.dumps(messages))
        current = self.state.get(identity, StateResponse())
        concurrency = getattr(getattr(options, "concurrency", None), "name", None)
        self.events.append(f"SAVE {store_name}/{key} etag={etag or 'absent'}")
        # 只有真实 ETag 才做条件写；无 ETag 是 last-write-wins，不能当成 CAS-create。
        # Source: https://docs.dapr.io/reference/api/state_api/#concurrency
        if concurrency == "first_write" and etag and etag != current.etag:
            self.conflicts += 1
            raise RuntimeError("etag mismatch: teaching concurrent writer")
        self.commit(identity, value)

    async def delete_state(self, store_name, key, options=None):
        self.check_available()
        self.events.append(f"DELETE {store_name}/{key}")
        self.state.pop((store_name, key), None)

    async def close(self):
        self.closed = True
