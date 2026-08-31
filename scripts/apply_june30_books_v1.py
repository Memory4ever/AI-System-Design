#!/usr/bin/env python3
"""Idempotently apply the reviewed 2026-06-30 Books packet under root's lock."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Insert:
    family: str
    target: str
    body_anchor: str
    body: str
    review: str

    @property
    def body_start(self) -> str:
        return f"<!-- body-source:{self.family} -->"

    @property
    def body_end(self) -> str:
        return "<!-- june30-body:end -->"

    @property
    def review_start(self) -> str:
        return "<!-- june30-review:start -->"

    @property
    def review_end(self) -> str:
        return "<!-- june30-review:end -->"

    @property
    def legacy_markers(self) -> tuple[str, str, str, str]:
        """Markers emitted by the first locked run before the count invariant fired."""
        return (
            f"<!-- june30-body:{self.family}:start -->",
            f"<!-- june30-body:{self.family}:end -->",
            f"<!-- june30-review:{self.family}:start -->",
            f"<!-- june30-review:{self.family}:end -->",
        )


INSERTS = (
    Insert(
        family="SF-2026-ARXIV-2606-30788",
        target="books/part-07-agent/77-memory.md",
        body_anchor="### Hierarchical Skill 不是固定 Taxonomy，而是 Retrieval Plan",
        body=(
            "把一条文本记忆删除，或直接修改模型权重，在状态单一时曾经可以近似实现遗忘。多模态关联和分阶段学习让事实可从图像、关系边或后续 safety state 中恢复，粗粒度 unlearning 还会误伤公共技能。memory owner 因而要持有跨模态 provenance graph，并把可撤销私有状态隔离到 process sidecar；收益是可验证删除与选择性撤销，代价是额外 lineage、sidecar 生命周期和残留扫描。证据不证明任意架构都能完全遗忘；provenance 不完整时隔离实体并保留人工审计，原始删除和重训作为高成本 fallback 共存。"
        ),
        review=(
            "- **SF-2026-ARXIV-2606-30788 / arXiv:2606.30788v1**：用 process sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。Method=`arXiv:2606.30788v1 — §3 Method; §Safety post-training.; §Sensitivity through training.`；Evaluation=`arXiv:2606.30788v1 — §2 Setting and evaluation; §5 Experiments; §5.1 Setup`，模型为 Qwen-2.5-0.5B/1.5B-Instruct 与 Llama-3.2-1B-Instruct；Non-proof=`arXiv:2606.30788v1 — §6 Discussion and limitations; §7 Conclusion; §B.7 Boundary cases for the second-order frontier`，不证明其他模型、任务或生产 SLO 的完全遗忘；Hardware/Precision/Input length/Output length/Batch/Concurrency/SLO/Evaluator=`Not Disclosed`；Artifact=`Not Disclosed — no later artifact used`。若 provenance、实体边界或 validation-selected edit 不成立，隔离实体并转人工审计，保留原始删除或重训 fallback。"
        ),
    ),
    Insert(
        family="SF-2026-ARXIV-2606-30616",
        target="books/part-07-agent/84-agent-platform.md",
        body_anchor="## Policy 与 Agent Identity",
        body=(
            "靠增加参数获得通用能力，在交互 horizon 短且工具面有限时曾经有效。长程 Agent 的瓶颈转为知识—动作轨迹、领域路由 teacher 与 on-policy distillation，平台需持有 atomic ability graph、horizon budget、teacher route 和失败轨迹。收益是小模型以更长执行链覆盖任务，代价是工具成本、错误累积与训练基础设施复杂度。35B 结果不证明参数规模不再重要；预算或校验不足时缩短 horizon 并转交强模型或人工。"
        ),
        review=(
            "- **SF-2026-ARXIV-2606-30616 / arXiv:2606.30616v1**：以更长工具交互 horizon、领域 teacher route 与 on-policy distillation 替代单纯参数扩展。Method=`arXiv:2606.30616v1 — §2 Knowledge-Guided General Agent Training with Specialized Teachers; §4 Three-stage Training Recipe; §4.2 Domain-level Teacher Training`；Evaluation=`arXiv:2606.30616v1 — §5 Experimental Results; §5.1 Evaluation Setting; §5.2 Results and Observations`，主指标 pass@1、每题最多 300 turns，论文同时报告 Qwen3.5-35B-A3B 官方与复现结果；Non-proof=`arXiv:2606.30616v1 — §6 Limitation and Future Work`，不证明参数规模不再重要或其他模型、任务、生产 SLO 可外推；Hardware/Precision/Input length/Output length/Batch/Concurrency/SLO=`Not Disclosed`；Artifact=`Not Disclosed — no later artifact used`。若 horizon budget、teacher identity、工具校验或失败轨迹不完整，则缩短 horizon 并转交强模型或人工。"
        ),
    ),
)


def all_books() -> dict[Path, str]:
    return {path: path.read_text() for path in (ROOT / "books").rglob("*.md")}


def main() -> None:
    snapshots = all_books()
    proposed: dict[Path, str] = {}

    # Validate the whole two-owner state before any mutation.
    for item in INSERTS:
        target = ROOT / item.target
        text = snapshots[target]
        family_hits = [path for path, content in snapshots.items() if item.family in content]
        marker_counts = [
            text.count(item.body_start),
            text.count(item.body_end),
            text.count(item.review_start),
            text.count(item.review_end),
        ]

        if marker_counts == [1, 1, 1, 1]:
            if family_hits != [target] or text.count(item.family) != 2:
                raise AssertionError(f"{item.family}: invalid idempotent state")
            if text.count(item.body) != 1 or text.count(item.review) != 1:
                raise AssertionError(f"{item.family}: markers exist but reviewed content drifted")
            continue

        legacy_counts = [text.count(marker) for marker in item.legacy_markers]
        if legacy_counts == [1, 1, 1, 1] and text.count(item.body) == 1 and text.count(item.review) == 1:
            updated = text
            for old, new in zip(
                item.legacy_markers,
                (item.body_start, item.body_end, item.review_start, item.review_end),
            ):
                updated = updated.replace(old, new, 1)
            proposed[target] = updated
            continue

        if any(marker_counts) or any(legacy_counts) or family_hits:
            raise AssertionError(
                f"{item.family}: partial/foreign state; markers={marker_counts}, "
                f"legacy={legacy_counts}, hits={family_hits}"
            )
        if text.count(item.body_anchor) != 1:
            raise AssertionError(f"{item.family}: body anchor is not unique")
        if text.count("## Review notes\n") != 1:
            raise AssertionError(f"{item.family}: Review notes anchor is not unique")

        body_block = f"{item.body_start}\n\n{item.body}\n\n{item.body_end}\n\n"
        review_block = f"{item.review_start}\n{item.review}\n{item.review_end}\n\n"
        updated = text.replace(item.body_anchor, body_block + item.body_anchor, 1)
        updated = updated.replace("## Review notes\n", "## Review notes\n\n" + review_block, 1)
        proposed[target] = updated

    for path, content in proposed.items():
        path.write_text(content)

    after = all_books()
    for item in INSERTS:
        target = ROOT / item.target
        text = after[target]
        hits = [path for path, content in after.items() if item.family in content]
        if hits != [target] or text.count(item.family) != 2:
            raise AssertionError(f"{item.family}: post-write owner uniqueness failure: {hits}")
        for value in (item.body_start, item.body_end, item.review_start, item.review_end, item.body, item.review):
            if text.count(value) != 1:
                raise AssertionError(f"{item.family}: post-write block count failure")

    print(f"06-30 Books applied/verified: {len(INSERTS)} families in {len(proposed)} newly written owners")


if __name__ == "__main__":
    main()
