"""Tiny, fixed teaching catalog: no network, shell or arbitrary file access."""

from dataclasses import dataclass
from typing import Literal

from agents import RunContextWrapper, function_tool
from pydantic import BaseModel, Field

Topic = Literal["lora", "kv_cache"]
CATALOG = {
    "lora": "LoRA 冻结基座权重，训练低秩增量；共享权重不等于消除 Adapter 执行成本。",
    "kv_cache": "KV Cache 复用历史 token 的 Key/Value，减少重复计算，但占用随序列增长的显存。",
}


@function_tool
def lookup_topic(topic: Topic) -> str:
    """Return a curated teaching note for lora or kv_cache (not a search engine)."""
    return CATALOG[topic]


@dataclass
class Learner:
    minutes: int = 20
    local_marker: str = "LOCAL_ONLY_MARKER"


@function_tool
def available_minutes(ctx: RunContextWrapper[Learner]) -> int:
    """Return the learner's time budget, without exposing other local fields."""
    return ctx.context.minutes


class StudyPlan(BaseModel):
    topic: Topic
    objective: str
    minutes: int = Field(ge=1, le=120)
    steps: list[str] = Field(min_length=1, max_length=4)
    check_question: str


PLAN = {
    "topic": "lora",
    "objective": "区分权重共享与执行复用",
    "minutes": 20,
    "steps": ["画出基座与低秩分支", "解释多 Adapter batch 的额外开销"],
    "check_question": "共享一个 BaseModel 为什么仍可能降低吞吐？",
}
