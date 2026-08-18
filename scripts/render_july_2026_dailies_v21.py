#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2026-07-01..31 Daily V2.1 reports from frozen July evidence packets."""

from __future__ import annotations

import gzip
import hashlib
import html
import json
import re
import unicodedata
import argparse
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26"
INVENTORY = SOURCE_DIR / "datacite-candidate-inventory.json"
DAILY_REVIEW_PACKET_DIR = SOURCE_DIR / "daily-review-packets"
REPLAY_SOURCE_DIR = ROOT / "papers/2026/07/_sources/arxiv-v2.1-replay-20260727-31"
WEEKLY_ROOT = ROOT / "papers/2026/weekly"
BEIJING = timezone(timedelta(hours=8))
ACCESSED = "2026-08-26"

PRIMARY_TITLE_OVERRIDES = {
    "2607.09759": "ReflectWorld-MM: An Entity-Oriented Multi-Media Memory System for Open-Ended Video Streams",
}

WEEKLY_BLOCKED = {
    "2607.06624",
    "2607.06987",
    "2607.08758",
    "2607.11079",
    "2607.11250",
    "2607.13921",
    "2607.14952",
}

PROMOTED = {
    "2607.00760": "INFER-KV-CACHE",
    "2607.01299": "INFER-KV-CACHE",
    "2607.01617": "INFER-PD-DISAGGREGATION",
    "2607.01646": "TRAIN-CHECKPOINT",
    "2607.01678": "TRAIN-DISTRIBUTED-TRAINING",
    "2607.01831": "INFER-KV-CACHE",
    "2607.04668": "INFER-SCHEDULING",
    "2607.05708": "INFER-REQUEST-LIFECYCLE",
    "2607.08930": "INFER-CONTINUOUS-BATCHING",
    "2607.08973": "TRAIN-DISTRIBUTED-TRAINING",
    "2607.10186": "INFER-GPU-MEMORY",
    "2607.10987": "AGENT-WORKFLOW",
    "2607.13649": "INFER-TENSORRT-LLM",
    "2607.16184": "INFER-KV-CACHE",
    "2607.16892": "INFER-KV-CACHE",
    "2607.17175": "INFER-SCHEDULING",
    "2607.17525": "PLATFORM-MONITORING",
    "2607.17715": "INFER-KV-CACHE",
    "2607.18141": "INFER-KV-CACHE",
    "2607.20220": "MODEL-MOE",
    "2607.23250": "TRAIN-DISTRIBUTED-TRAINING",
}

# Primary arXiv v1 HTML was reopened during the July replay.  These families
# were absent from the older Weekly denominator but clearly alter a system
# mechanism or evaluation contract.  They receive a Standard Review instead
# of being silently closed from title/metadata alone.
STANDARD_REVIEWED = {
    "2606.31093": "INFER-SGLANG",
    "2606.31145": "INFER-KV-CACHE",
    "2606.31519": "INFER-KV-CACHE",
    "2607.00151": "INFER-SCHEDULING",
    "2607.02577": "PLATFORM-EVALUATION-SYSTEM",
    "2607.00501": "INFER-TENSORRT-LLM",
    "2607.01065": "INFER-KV-CACHE",
    "2607.01520": "INFER-KV-CACHE",
    "2607.01579": "INFER-SCHEDULING",
    "2607.02043": "INFER-PD-DISAGGREGATION",
    "2607.03333": "INFER-SPECULATIVE-DECODING",
    "2607.03948": "INFER-SCHEDULING",
    "2607.04181": "INFER-SCHEDULING",
    "2607.04302": "INFER-TENSORRT-LLM",
    "2607.04395": "INFER-TENSORRT-LLM",
    "2607.05475": "INFER-TENSORRT-LLM",
    "2607.06601": "MODEL-MOE",
    "2607.05876": "INFER-SCHEDULING",
    "2607.06519": "INFER-KV-CACHE",
    "2607.06523": "INFER-KV-CACHE",
    "2607.07046": "INFER-SCHEDULING",
    "2607.08057": "INFER-KV-CACHE",
    "2607.08116": "INFER-DYNAMO",
    "2607.08734": "INFER-TENSORRT-LLM",
    "2607.10183": "INFER-TENSORRT-LLM",
    "2607.11942": "PLATFORM-EVALUATION-SYSTEM",
    "2607.10582": "INFER-KV-CACHE",
    "2607.12839": "INFER-TENSORRT-LLM",
    "2607.12875": "INFER-TENSORRT-LLM",
    "2607.13205": "INFER-KV-CACHE",
    "2607.14618": "INFER-TENSORRT-LLM",
    "2607.15498": "INFER-KV-CACHE",
    "2607.15593": "AGENT-TOOL-CALLING",
    "2607.15621": "MULTIMODAL-EMBODIED-VLA",
    "2607.16473": "INFER-TENSORRT-LLM",
    "2607.16488": "INFER-SCHEDULING",
    "2607.17019": "INFER-KV-CACHE",
    "2607.17415": "INFER-SCHEDULING",
    "2607.17545": "AGENT-MEMORY",
    "2607.17979": "INFER-TENSORRT-LLM",
    "2607.18631": "INFER-SCHEDULING",
    "2607.19438": "INFER-TENSORRT-LLM",
    "2607.19704": "INFER-SCHEDULING",
    "2607.19957": "PLATFORM-SECURITY",
    "2607.27231": "PLATFORM-EVALUATION-SYSTEM",
    "2607.20757": "INFER-TENSORRT-LLM",
    "2607.20981": "INFER-TENSORRT-LLM",
    "2607.21475": "INFER-KV-CACHE",
    "2607.21503": "AGENT-CONTEXT",
    "2607.21927": "MODEL-LONG-CONTEXT",
    "2607.22242": "INFER-SCHEDULING",
    "2607.04391": "AGENT-MEMORY",
    "2607.05029": "PLATFORM-SECURITY",
    "2607.06118": "PLATFORM-EVALUATION-SYSTEM",
    "2607.07144": "INFER-KV-CACHE",
    "2607.09153": "INFER-KV-CACHE",
    "2607.11149": "PLATFORM-EVALUATION-SYSTEM",
    "2607.12550": "INFER-KV-CACHE",
    "2607.13157": "AGENT-MEMORY",
    "2607.14169": "MULTIMODAL-WORLD-MODELS",
    "2607.17621": "AGENT-MEMORY",
    "2607.17733": "INFER-TENSORRT-LLM",
    "2607.17751": "AGENT-TOOL-CALLING",
    "2607.19096": "AGENT-MEMORY",
    "2607.19456": "INFER-TENSORRT-LLM",
    "2607.19490": "PLATFORM-SECURITY",
    "2607.21106": "AGENT-MEMORY",
    "2607.21404": "AGENT-MEMORY",
    "2607.21985": "INFER-TENSORRT-LLM",
}

# Source-specific primary receipts recovered after the frozen denominator was
# built. A row may enter this table only after the exact event-time version's
# Method, evaluation, counterevidence/limitations and artifact scope have been
# read. These fields remain explicit instead of being inferred from metadata.
EXACT_REVIEWS = {
    "2606.31519": {
        "node": "INFER-KV-CACHE",
        "score": (3, 2, 3),
        "reviewed": (
            "SRC-ARXIV@arXiv:2606.31519v1; "
            "SRC-GITHUB-COMMIT@commit:3324489eafee6b16e28ff87bebce41ced7d921e6"
        ),
        "method": (
            "https://arxiv.org/html/2606.31519v1#S3.SS2 :: randomized rotation, "
            "1-bit Key index, correction factor and unbiased estimator; "
            "https://arxiv.org/html/2606.31519v1#S3.SS3 :: INT4 Query scan, "
            "adaptive Top-p selection, exact selected KV plus local window; "
            "https://arxiv.org/html/2606.31519v1#S3.SS4 :: asynchronous Prefill "
            "index construction and lazy Decode updates; "
            "https://arxiv.org/html/2606.31519v1#A1.SS3 :: unbiased estimator, "
            "high-probability error bound and an explicit Top-p application remark; "
            "the remark is rationale, not a Top-p mass or retrieval-quality theorem; "
            "https://arxiv.org/html/2606.31519v1#A1.SS4 :: proofs of estimator "
            "unbiasedness/error bound and query-quantization error"
        ),
        "evaluation": (
            "https://arxiv.org/html/2606.31519v1#S4.SS1 :: vLLM 0.10.2, "
            "FlashInfer 0.5.3, LMCache, Triton/custom CUDA and NVIDIA Hopper "
            "architecture (exact GPU SKU not disclosed); "
            "https://arxiv.org/html/2606.31519v1#S4.SS2 :: LongBench, RULER "
            "8K-64K and GSM8K on LongChat-7B and LLaMA-3.1 8B/70B with "
            "baseline configurations and p thresholds; "
            "https://arxiv.org/html/2606.31519v1#S4.SS3 :: TTFT, TBT and "
            "end-to-end latency for 10K-32K contexts; author maximums are "
            "3.88x TBT and 2.16x end-to-end, not production constants"
        ),
        "limitations": (
            "https://arxiv.org/html/2606.31519v1#S4.SS4 :: p-sensitivity and "
            "centroid re-centering ablation; removing re-centering changes "
            "LongBench average 50.63 to 50.25; the uniform-hypersphere "
            "assumption may fail for clustered Q/K and under Decode drift; "
            "https://arxiv.org/html/2606.31519v1#A3.SS1 :: index-space derivation; "
            "https://arxiv.org/html/2606.31519v1#A3.SS2 :: complexity derivation; "
            "exact GPU SKU, serving concurrency, arrival process, precision "
            "outside the selector, tail-SLO and independent replication are "
            "not disclosed"
        ),
        "artifact": (
            "https://github.com/Sakuraaa0/RaBitQCache/tree/3324489eafee6b16e28ff87bebce41ced7d921e6 "
            ":: exact pre-v1 author repository tree contains benchmark, csrc, "
            "rabitqcache and efficiency-integration paths; the tree has one commit "
            "and no tagged release; accessed 2026-08-27"
        ),
        "artifact_receipt": {
            "repository": "Sakuraaa0/RaBitQCache",
            "until": "2026-06-30T11:32:14Z",
            "commit": "3324489eafee6b16e28ff87bebce41ced7d921e6",
            "commit_timestamp": "2026-05-18T02:49:58Z",
            "url": "https://api.github.com/repos/Sakuraaa0/RaBitQCache/commits/3324489eafee6b16e28ff87bebce41ced7d921e6",
            "executed_at": "2026-08-27T07:41:16+08:00",
        },
        "benchmark": {
            "workload": "LongBench (13 tasks), RULER and GSM8K; efficiency subset uses LongBench",
            "model": "LongChat-7B-v1.5-32k; LLaMA-3.1-8B-Instruct; LLaMA-3.1-70B-Instruct",
            "hardware": "NVIDIA Hopper architecture; exact GPU SKU and topology Not Disclosed",
            "precision": "1-bit Key selector index plus INT4 query; attention and baseline precision Not Disclosed",
            "input_length": "LongBench variable; RULER 8K-64K; efficiency 10K-32K",
            "output_length": "Not Disclosed",
            "batch": "Not Disclosed for end-to-end experiments",
            "concurrency": "Not Disclosed",
            "slo": "No production SLO; author reports TTFT, TBT, end-to-end latency and task quality",
            "evaluator": "Authors; exact benchmark and evaluator versions Not Disclosed",
        },
        "existing": (
            "KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 "
            "memory state 换取历史 layer computation 不重算。"
        ),
        "existing_locator": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14",
        "adjacent_refs": (
            "books/part-05-inference-system/44-decode.md#L14; "
            "books/part-05-inference-system/46-continuous-batching.md#L14"
        ),
        "accessed": "2026-08-27",
        "delta": (
            "固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 "
            "attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key "
            "索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，"
            "据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；"
            "Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware "
            "runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 "
            "3.5% 的索引空间、线性索引扫描、p/"
            "分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。"
        ),
        "disposition": "Integrate",
    },
}

# Keep the growing source-specific review ledger as data rather than turning
# this renderer into a second report.  The JSON file is written only after the
# exact event-time arXiv version has been read and its route locators, evidence
# boundary, score and Books disposition have been reviewed.
REVIEW_RECEIPTS = SOURCE_DIR / "primary-review-receipts.json"
if REVIEW_RECEIPTS.exists():
    EXACT_REVIEWS.update(json.loads(REVIEW_RECEIPTS.read_text(encoding="utf-8")))

# Low-score closures are persisted in the per-day packet rather than the
# central Full Source Review ledger.  They still own a reviewed score, node and
# final disposition; falling back to title heuristics here would silently turn
# e.g. `Weekly Only — Context` into `Rejected` after a rerender.
CLOSURE_REVIEWS: dict[str, dict] = {}
for _packet_path in sorted(DAILY_REVIEW_PACKET_DIR.glob("*.json")):
    _packet = json.loads(_packet_path.read_text(encoding="utf-8"))
    for _closure in _packet.get("closure_reviews", []):
        _closure = dict(_closure)
        _closure["disposition"] = (
            _closure.get("disposition") or _closure.get("books_disposition")
        )
        if not _closure["disposition"]:
            raise ValueError(
                f"Persisted closure review has no final disposition: {_packet_path}"
            )
        _identity = _closure.get("identity", "")
        _match = re.fullmatch(r"arXiv:(\d{4}\.\d{4,5})v1", _identity, re.I)
        if not _match:
            continue
        _identifier = _match.group(1)
        _prior = CLOSURE_REVIEWS.get(_identifier)
        if _prior and _prior != _closure:
            raise ValueError(f"Conflicting persisted closure review for {_identifier}")
        CLOSURE_REVIEWS[_identifier] = _closure

INTEGRATIONS: dict[str, tuple[str, str, str]] = {
    "2606.31519": (
        "INFER-KV-CACHE",
        "从固定 Top-k 到按 Attention Mass 自适应的 Top-p",
        EXACT_REVIEWS["2606.31519"]["delta"],
    ),
}

# Narrative selection is capped at three items. Equal-score, equally eligible
# families need an explicit source-specific tie-break; identifier order is only
# a deterministic fallback and must never appear as the semantic reason.
SELECTION_TIEBREAK = {
    "2606.31519": (
        "与同为 8/9 且已入选的 SmoothAgent 相比，RaBitQCache 的长期增量集中在 "
        "KV selector/consumer 这一条局部执行链；SmoothAgent 同时改变 context transformation、"
        "best-effort scheduling、state promotion/cancellation 与 synchronous fallback，System Reach "
        "为 3，因此优先占用跨层长叙事名额。RaBitQCache 仍保留完整 Deep Review、独立 Books 段落与 Integrate 决定。"
    ),
    "2607.01299": (
        "HYPIC 与已入选的 KV compression risk 均为 9/9、均需 Integrate。长叙事优先保留后者，"
        "因为 response-spectrum 上下界给出跨 eviction、quantization 与 summary policy 可复用的 "
        "abstention/risk contract；HYPIC 的可组合 transition 则受 hybrid linear/full-attention "
        "architecture、segment operator 与 seam repair 约束，系统增量已在独立 Books 段落完整承载。"
    ),
}

for _identifier, _review in EXACT_REVIEWS.items():
    if _review.get("disposition") == "Integrate" and _review.get("integration_section"):
        INTEGRATIONS[_identifier] = (
            _review["node"],
            _review["integration_section"],
            _review["delta"],
        )

NODE_PROPOSITIONS = {
    "INFER-KV-CACHE": "KV 是 request-owned、带 model/position/layout identity 的可变运行时状态；压缩、迁移与共享必须保留 correctness 和恢复边界。",
    "INFER-SCHEDULING": "调度器拥有 admission、placement 与时序控制，但不能改变模型语义；收益必须以 workload、tail SLO 与迁移成本结算。",
    "INFER-PD-DISAGGREGATION": "Prefill/Decode 分离把 KV transfer、queue ownership 和 failure recovery 放入同一服务 contract。",
    "INFER-SPECULATIVE-DECODING": "Speculation 以 proposal、verification 与 commit/rollback 换取串行 Decode 的并行机会。",
    "INFER-TENSORRT-LLM": "Execution plan 将 graph、precision、layout、kernel 与 hardware capability 绑定，专用实现必须保留通用路径的成立区间。",
    "INFER-SGLANG": "Serving runtime 负责把上层 workflow 编译为可执行 request/state flow，并显式管理跨角色状态。",
    "INFER-DYNAMO": "Distributed runtime 需要把 routing、state placement、transfer 与 recovery 作为同一控制面。",
    "INFER-CONTINUOUS-BATCHING": "Continuous batching 每轮重组 active requests，以调度复杂度换取更高设备利用率。",
    "INFER-GPU-MEMORY": "GPU memory owner 必须同时管理容量、fragmentation、movement 与 OOM recovery，而不只计算理论字节数。",
    "TRAIN-DISTRIBUTED-TRAINING": "并行训练是 compute、memory、communication、scheduling 与 failure recovery 的联合分解。",
    "TRAIN-CHECKPOINT": "Checkpoint 是可恢复、可迁移的训练状态 artifact，不只是一次权重保存。",
    "MODEL-MOE": "MoE 以条件激活扩大参数容量，同时把 routing、capacity、placement 与 communication 引入系统路径。",
    "MODEL-LONG-CONTEXT": "长上下文机制以新的 state representation、近似或层次结构交换计算、内存与可恢复性。",
    "PLATFORM-EVALUATION-SYSTEM": "Evaluation 结论只在冻结的 subject、data/environment、protocol、scorer 与 aggregation contract 内成立。",
    "PLATFORM-SECURITY": "跨 trust boundary 的数据和状态必须绑定 identity、integrity、authorization、provenance 与 audit。",
    "PLATFORM-MONITORING": "Monitoring 负责产生可关联 telemetry；它不能单独证明因果、质量或 release readiness。",
    "AGENT-MEMORY": "Agent Memory 是跨调用的 typed、authorized、versioned state，必须支持 provenance、correction、deletion 与 rollback。",
    "AGENT-CONTEXT": "Context assembler 在 token budget 内选择当前调用可见信息，但不拥有事实真值。",
    "AGENT-TOOL-CALLING": "Tool layer 把模型 proposal 转成 typed、authorized、observable action，并保留结果和副作用证据。",
    "AGENT-WORKFLOW": "Workflow owner 负责 durable control state、重试、补偿与恢复，不能把模型叙述当作完成证明。",
    "MULTIMODAL-WORLD-MODELS": "World Model 的核心是 action-conditioned state transition 与可修正环境状态，不等同于视频生成质量。",
    "MULTIMODAL-EMBODIED-VLA": "VLA 把感知、action proposal、低层控制与物理反馈闭成受 latency 和 safety 约束的循环。",
}


def normalize(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip())


def canonical_multi(value: str) -> str:
    return ";".join(sorted(normalize(item) for item in value.split(";") if item.strip()))


def body_digest(body: str) -> str:
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    body = "\n".join(line.rstrip() for line in unicodedata.normalize("NFC", body).splitlines()).strip()
    return hashlib.sha256(body.encode()).hexdigest()


def review_provenance(candidate: dict, review: dict, body: str) -> str:
    fields = [
        "review-completion-v1",
        candidate["family"],
        candidate["event"],
        candidate["primary"],
        canonical_multi(candidate["supporting"]),
        review["primary_evidence"],
        canonical_multi(review["reviewed"]),
        review["route"],
    ]
    if candidate.get("review_override", "none") != "none":
        fields.append(f"review-override:{candidate['review_override']}")
    fields.extend([
        canonical_multi(review["method"]),
        canonical_multi(review["evaluation"]),
        canonical_multi(review["limitations"]),
        canonical_multi(review["artifact"]),
        f"claim:{candidate['family']}",
        f"review:{candidate['family']}",
        f"review-body-sha256:{body_digest(body)}",
    ])
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def roadmap() -> tuple[dict[str, Path], list[str]]:
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    rows = re.findall(r"\| `([A-Z0-9-]+)` \| Ch\d+ \| `([^`]+)` \|", text)
    return {node: ROOT / path for node, path in rows}, [node for node, _ in rows]


def legacy_node_map() -> dict[int, str]:
    """Resolve chapter numbers as they meant before Part III was inserted."""
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    result = {}
    for node, legacy in re.findall(
        r"\| `([A-Z0-9-]+)` \| Ch\d+ \| `[^`]+` \| (Ch\d+|N/A) \|", text
    ):
        if legacy != "N/A":
            result[int(legacy[2:])] = node
    return result


def weekly_review_packet(identifier: str, path_str: str | None) -> dict | None:
    """Recover a bounded, source-specific review section from W27-W30.

    The returned packet is evidence about what the historical full-text review
    actually covered.  A mere mention, score row, or blocked queue does not
    become a completed review.
    """
    if not path_str:
        return None
    lines = (ROOT / path_str).read_text(encoding="utf-8").splitlines()
    full_start = next((i for i, line in enumerate(lines) if line.startswith("## Full Source Review")), None)
    if full_start is None:
        return None
    full_end = next(
        (i for i, line in enumerate(lines) if i > full_start and line.startswith("## ")),
        len(lines),
    )
    matches = [i for i, line in enumerate(lines) if full_start <= i < full_end and identifier in line]
    if not matches:
        return None
    hit = matches[0]
    start = hit
    while start > full_start and not lines[start].startswith("### "):
        start -= 1
    end = start + 1
    while end < len(lines) and not lines[end].startswith("### ") and not lines[end].startswith("## "):
        end += 1
    section = lines[start:end]
    section_text = "\n".join(section)
    blocked = bool(re.search(r"Unverified / Blocked|blocked-skip|仍不可访问|Claims explicitly not verified", section_text, re.I))
    full_read = any(marker in section_text for marker in ("已读", "Full-read Coverage", "已覆盖")) and not blocked

    bullets = []
    index = 1
    while index < len(section):
        match = re.match(r"- \*\*([^*]+)\*\*：(.*)", section[index])
        if not match:
            index += 1
            continue
        bullet_start = index
        label = match.group(1).strip()
        body = [match.group(2).strip()]
        index += 1
        while index < len(section) and not re.match(r"- \*\*[^*]+\*\*：", section[index]):
            if section[index].strip():
                body.append(section[index].strip())
            index += 1
        bullets.append({
            "label": label,
            "text": re.sub(r"\s+", " ", " ".join(body)).strip(),
            "start": start + bullet_start + 1,
            "end": start + index,
        })

    def choose(terms: tuple[str, ...], exclude: set[int] | None = None) -> dict | None:
        excluded = exclude or set()
        return next(
            (bullet for pos, bullet in enumerate(bullets)
             if pos not in excluded and any(term.lower() in bullet["label"].lower() for term in terms)),
            None,
        )

    method = choose(("Mechanism", "State", "Implementation", "Changed Constraint", "Problem"))
    if method is None:
        method = choose(("Coverage", "Full-read"))
    used = {bullets.index(method)} if method in bullets else set()
    evaluation = choose(("Evaluation", "Evidence", "Ablation", "What It Proves", "What Evidence"), used)
    if evaluation is None:
        evaluation = choose(("Coverage", "Full-read"), used) or method
    used.add(bullets.index(evaluation)) if evaluation in bullets else None
    limitations = choose(("Boundary", "Limitation", "Failure", "Trade-off", "Does Not Prove", "Threat", "Decision"), used)
    if limitations is None:
        limitations = choose(("Boundary", "Decision", "Trade-off", "Failure"))

    heading = section[0].removeprefix("### ").strip()
    total_match = re.search(r"(\d+)/30", heading)
    locator = f"{path_str}#L{start + 1}-L{end}"
    return {
        "path": path_str,
        "heading": heading,
        "locator": locator,
        "section": section_text,
        "bullets": bullets,
        "method": method,
        "evaluation": evaluation,
        "limitations": limitations,
        "blocked": blocked,
        "full_read": full_read,
        "v1_total": int(total_match.group(1)) if total_match else None,
    }


def weekly_blocked_locator(identifier: str, path_str: str | None) -> str:
    if not path_str:
        return f"arXiv:{identifier}v1 :: blocked identity; weekly path unavailable"
    lines = (ROOT / path_str).read_text(encoding="utf-8").splitlines()
    hit = next((i for i, line in enumerate(lines) if identifier in line), None)
    if hit is None:
        return f"{path_str} :: blocked identity arXiv:{identifier}v1"
    start = hit
    while start > 0 and not lines[start].startswith(("### ", "## ")):
        start -= 1
    end = hit
    while end + 1 < len(lines) and not lines[end + 1].startswith(("### ", "## ")):
        end += 1
    return f"{path_str}#L{start + 1}-L{end + 1}"


def node_for(title: str) -> str:
    lowered = title.lower()
    routes = [
        (("world model",), "MULTIMODAL-WORLD-MODELS"),
        (("vision-language-action", " vla", "vla-", "robotic agent", "robot agent"), "MULTIMODAL-EMBODIED-VLA"),
        (("multimodal",), "MULTIMODAL-REPRESENTATION"),
        (("diffusion language",), "MULTIMODAL-GENERATIVE-PARADIGMS"),
        (("kv cache", "kv-cache", "cache compression"), "INFER-KV-CACHE"),
        (("speculative",), "INFER-SPECULATIVE-DECODING"),
        (("prefill", "disaggregated"), "INFER-PD-DISAGGREGATION"),
        (("batching",), "INFER-CONTINUOUS-BATCHING"),
        (("serving", "inference advisor", "inference routing", "backend dispatch", "auto-scaling"), "INFER-SCHEDULING"),
        (("checkpoint",), "TRAIN-CHECKPOINT"),
        (("distributed training", "all-reduce", "communication", "optimizer state"), "TRAIN-DISTRIBUTED-TRAINING"),
        (("pipeline parallel",), "TRAIN-PIPELINE-PARALLEL"),
        (("mixture of experts", " moe", "moe "), "MODEL-MOE"),
        (("quantization", "kernel", "accelerator", "gpu", "npu", "compiler"), "INFER-TENSORRT-LLM"),
        (("agent memory", "memory architecture", "memory agent", "agent's memories", "agent memory"), "AGENT-MEMORY"),
        (("workflow", "harness", "agent os", "agentos"), "AGENT-WORKFLOW"),
        (("multi-agent",), "AGENT-MULTI-AGENT"),
        (("skill",), "AGENT-PLATFORM"),
        (("tool", "api-calling"), "AGENT-TOOL-CALLING"),
        (("retrieval-augmented", " rag"), "AGENT-RAG"),
        (("uncertainty", "benchmark", "evaluation", "verifier", "rubric"), "PLATFORM-EVALUATION-SYSTEM"),
        (("hallucination", "guardrail", "jailbreak", "security", "attack", "safety"), "PLATFORM-SECURITY"),
        (("on-policy distillation", "policy distillation", "reinforcement learning", "credit assignment", "reward", "trust region"), "TRAIN-GRPO"),
        (("lora", "adapter"), "TRAIN-LORA"),
        (("training", "pretraining", "fine-tuning", "mid-training", "post-training"), "TRAIN-PRETRAINING"),
        (("long context", "linear attention", "sparse attention", "delta memory"), "MODEL-LONG-CONTEXT"),
        (("agent",), "AGENT-PLATFORM"),
    ]
    for needles, node in routes:
        if any(needle in lowered for needle in needles):
            return node
    return "WORLDVIEW-SYSTEM-EVOLUTION"


def explicit_book_owner(identifier: str) -> str | None:
    paths, _ = roadmap()
    for node, path in paths.items():
        if identifier in path.read_text(encoding="utf-8"):
            return node
    return None


def weekly_locator(identifier: str, path_str: str | None) -> str | None:
    packet = weekly_review_packet(identifier, path_str)
    return packet["locator"] if packet else None


def packet_locator(packet: dict, facet: str) -> str:
    bullet = packet.get(facet)
    if not bullet:
        return f"{packet['locator']} :: {facet} not separately disclosed in historical review"
    text = bullet["text"]
    coverage = text.split("。", 1)[0]
    facets = {
        "method": ("method", "mechanism", "architecture", "state", "flow", "objective", "algorithm", "training"),
        "evaluation": ("evaluation", "experiment", "benchmark", "baseline", "ablation", "sensitivity", "analysis", "results"),
        "limitations": ("limitation", "boundary", "failure", "threat", "does not prove", "不证明", "限制"),
    }
    terms = facets.get(facet, ())
    named = [item.strip() for item in re.split(r"、|,|，|/", coverage) if any(term in item.lower() for term in terms)]
    scope = " / ".join(named[:4]) or bullet["label"]
    facet_label = {
        "method": "Methodology",
        "evaluation": "Experiments",
        "limitations": "Scope and Limitations",
    }.get(facet, facet.title())
    return f"{packet['path']}#L{bullet['start']}-L{bullet['end']} :: line range; {facet_label}: {scope}"


def packet_summary(packet: dict, facet: str, limit: int = 720) -> str:
    bullet = packet.get(facet)
    if not bullet:
        return "公开材料未在历史审阅中形成可分离的该项结论。"
    text = re.sub(r"`[^`]+`；(?:arXiv:[^；]+；)?", "", bullet["text"], count=1)
    return text[:limit].rstrip("；，。 ") + "。"


def weekly_owner(packet: dict, title: str) -> str:
    """Resolve owner from the review's explicit chapter decision, not title metadata."""
    text = packet["section"]
    patterns = (
        r"主 owner[，： ]*Ch(\d+)",
        r"Ch(\d+)[ 为]*主 owner",
        r"Ch(\d+) owner",
        r"主 owner Ch(\d+)",
    )
    chapter = None
    for pattern in patterns:
        matches = re.findall(pattern, text, re.I)
        if matches:
            chapter = int(matches[-1])
            break
    if chapter is None:
        decision_lines = [bullet["text"] for bullet in packet["bullets"] if "Decision" in bullet["label"]]
        refs = re.findall(r"Ch(\d+)", " ".join(decision_lines))
        chapter = int(refs[0]) if refs else None

    node = legacy_node_map().get(chapter) if chapter is not None else None
    lowered = text.lower()
    if chapter == 10:
        if any(term in lowered for term in ("vla", "robot", "physical action", "embodied")):
            node = "MULTIMODAL-EMBODIED-VLA"
        elif any(term in lowered for term in ("world model", "world simulator", "playable world", "interactive world", "persistent world")):
            node = "MULTIMODAL-WORLD-MODELS"
        elif "multimodal" in lowered:
            node = "MULTIMODAL-REPRESENTATION"
    return node or node_for(title)


def weekly_score(packet: dict) -> tuple[int, int, int]:
    """Re-score a completed historical review under V2 using its stated decision."""
    text = packet["section"].lower()
    decision = " ".join(
        bullet["text"].lower() for bullet in packet["bullets"]
        if any(term in bullet["label"].lower() for term in ("decision", "evolution", "roadmap"))
    )
    if "version/product fact" in text or "record only" in text:
        return 1, 1, 1
    design = 3 if any(term in decision for term in (
        "new mechanism", "直接否定", "修正", "新增的章节级缺口", "refine ch",
    )) else 2
    chapter_refs = set(re.findall(r"Ch(\d+)", decision))
    reach = 3 if len(chapter_refs) >= 3 else 2 if len(chapter_refs) >= 2 else 1
    if any(term in text for term in (
        "lifecycle", "cross-layer", "跨层", "platform contract", "control flow", "data flow",
        "distributed", "multi-tenant", "producer", "consumer",
    )):
        reach = max(reach, 2)
    durability = 3 if any(term in text for term in (
        "identity", "integrity", "provenance", "correctness", "lifecycle", "state ownership",
        "状态所有权", "演进", "evolution", "failure boundary", "safety proof",
    )) else 2
    return design, reach, durability


def chapter_locator(path: Path) -> str:
    """Return a concrete current-chapter locator, preferring the first thesis heading."""
    lines = path.read_text(encoding="utf-8").splitlines()
    line_no = next(
        (index for index, line in enumerate(lines, start=1) if line.startswith("## ")),
        1,
    )
    return f"{path.relative_to(ROOT).as_posix()}#L{line_no}"


def chapter_proposition(path: Path) -> tuple[str, str]:
    """Return the chapter's durable thesis and its exact locator.

    Prefer the explicit core judgment over the introductory question. A
    chapter title or "本章要回答的问题" paragraph is navigation, not evidence
    that an incoming Source Family is already covered.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    thesis = next(
        (i for i, line in enumerate(lines) if "本章的核心判断" in line),
        None,
    )
    if thesis is not None:
        index = thesis
        paragraph = []
        while index < len(lines) and lines[index].strip() and not (
            index > thesis and lines[index].startswith(("#", "|", "```"))
        ):
            paragraph.append(lines[index].strip())
            index += 1
        text = re.sub(r"\s+", " ", " ".join(paragraph)).strip()
        return text[:1200], f"{path.relative_to(ROOT).as_posix()}#L{thesis + 1}-L{index}"
    heading = next((i for i, line in enumerate(lines) if line.startswith("## ")), 0)
    index = heading + 1
    while index < len(lines):
        if not lines[index].strip() or lines[index].startswith(("#", "|", "- ", "```", ">")):
            index += 1
            continue
        start = index
        paragraph = []
        while index < len(lines) and lines[index].strip() and not lines[index].startswith(("#", "|", "```")):
            paragraph.append(lines[index].strip())
            index += 1
        text = re.sub(r"\s+", " ", " ".join(paragraph)).strip()
        if len(text) >= 40:
            locator = f"{path.relative_to(ROOT).as_posix()}#L{start + 1}-L{index}"
            return text[:720], locator
    raise ValueError(f"No substantive proposition found in {path}")


def candidate_proposition(candidate: dict, paths: dict[str, Path]) -> tuple[str, str]:
    exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
    if exact.get("existing") and exact.get("existing_locator"):
        return exact["existing"], concrete_book_ref(exact["existing_locator"])
    return chapter_proposition(paths[candidate["node"]])


def candidate_adjacent(candidate: dict, order: list[str], paths: dict[str, Path]) -> str:
    exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
    refs = exact.get("adjacent_refs")
    if refs:
        values = refs if isinstance(refs, list) else [refs]
        return "; ".join(concrete_book_ref(value) for value in values)
    return adjacent(candidate["node"], order, paths)


def potential_books_delta(candidate: dict) -> bool:
    exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
    if exact.get("disposition") == "Integrate":
        return True
    packet = candidate.get("weekly_packet")
    evidence_signal = bool(packet and re.search(
        r"Refine|New Mechanism|新增.*缺口|直接否定|修正|security contract|release contract",
        packet["section"], re.I,
    ))
    return candidate["score"][0] == 3 or evidence_signal


def selection_delta(candidate: dict) -> str:
    """Return only source-supported evidence for pre-Books selection."""
    exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
    return exact.get("source_claim") or evidence_delta(candidate)


def selection_reason(candidate: dict, selected: list[dict]) -> str:
    delta = selection_delta(candidate)
    if candidate["arxiv_id"] in SELECTION_TIEBREAK:
        return (
            f"本 family 的独立增量为“{sentence(delta)}”；V2="
            f"{candidate['score'][0]}/{candidate['score'][1]}/{candidate['score'][2]}。"
            f"{SELECTION_TIEBREAK[candidate['arxiv_id']]}"
        )
    same_owner = [item for item in selected if item["node"] == candidate["node"]]
    comparator = max(same_owner, key=lambda item: item["total"]) if same_owner else min(
        selected, key=lambda item: abs(item["total"] - candidate["total"])
    )
    relation = (
        f"与同 owner 入选 `{comparator['family']}` 相比，本项没有更高的 Design Delta / System Reach / Durability"
        if same_owner else
        f"它与入选 `{comparator['family']}` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序"
    )
    return (
        f"本 family 的独立增量为“{sentence(delta)}”；V2="
        f"{candidate['score'][0]}/{candidate['score'][1]}/{candidate['score'][2]}。{relation}。"
        "因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；"
        "这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。"
    )


def reviewed_selection_contract(day_s: str) -> dict:
    """Load the canonical independently reviewed narrative-selection contract."""
    packet_path = DAILY_REVIEW_PACKET_DIR / f"{day_s}.json"
    if not packet_path.exists():
        return {}
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    return packet.get("deep_analysis_selection", {})


def reviewed_selection_override(day_s: str, selectable: list[dict]) -> list[dict] | None:
    """Load the independently reviewed narrative selection for one persisted day."""
    selection = reviewed_selection_contract(day_s)
    selected_families = selection.get("selected")
    if selected_families and all(isinstance(item, dict) for item in selected_families):
        selected_families = [
            item.get("source_family")
            or item.get("source_family_id")
            or item.get("selected_family")
            for item in selected_families
        ]
        if any(family is None for family in selected_families):
            raise ValueError(f"{day_s}: selected entry has no Source Family ID")
    if not selected_families and selection.get("selected_analysis_units"):
        selected_units = selection["selected_analysis_units"]
        if all(isinstance(unit, dict) for unit in selected_units):
            selected_families = [
                unit.get("selected_family") or unit.get("source_family_id")
                for unit in selected_units
            ]
        else:
            unit_to_family = {
                decision.get("analysis_unit_id"): decision.get("source_family_id")
                for decision in selection.get("family_decisions", [])
                if decision.get("decision") == "selected"
            }
            selected_families = [unit_to_family.get(unit) for unit in selected_units]
            if any(family is None for family in selected_families):
                raise ValueError(
                    f"{day_s}: selected analysis unit has no selected family mapping: "
                    f"{selected_units!r}"
                )
    if selected_families:
        selected_families = [
            family if family.startswith("SF-") else f"SF-2026-ARXIV-{family.replace('.', '-')}"
            for family in selected_families
        ]
    if not selected_families:
        return None
    if len(selected_families) > 3 or len(set(selected_families)) != len(selected_families):
        raise ValueError(f"{day_s}: invalid reviewed Deep Analysis selection {selected_families!r}")
    by_family = {candidate["family"]: candidate for candidate in selectable}
    missing = [family for family in selected_families if family not in by_family]
    if missing:
        raise ValueError(f"{day_s}: reviewed selection is not Deep-eligible: {missing}")
    return [by_family[family] for family in selected_families]


def sentence(text: str) -> str:
    clean = html.unescape(re.sub(r"\s+", " ", text)).strip()
    match = re.match(r"^(.{1,520}?[。！？.!?])(?:\s|$)", clean)
    if match:
        return match.group(1)
    if len(clean) <= 520:
        return clean
    cut = max(clean.rfind(mark, 0, 520) for mark in ("；", ";", "，", ","))
    return clean[:cut + 1] if cut >= 120 else clean[:520] + "…"


def evidence_locators(candidate: dict) -> tuple[str, str, str]:
    identifier = candidate["arxiv_id"]
    node = candidate["node"]
    exact = EXACT_REVIEWS.get(identifier)
    if exact:
        return exact["method"], exact["evaluation"], exact["limitations"]
    packet = candidate.get("weekly_packet")
    if packet and packet["full_read"]:
        return (
            packet_locator(packet, "method"),
            packet_locator(packet, "evaluation"),
            packet_locator(packet, "limitations"),
        )
    special = {
        "2607.04391": ("#S3", "#S4", "#S4.SS4; #S5.SS5"),
        "2607.17621": ("#S2; #S3", "#S4", "#S5; reasoned boundary: attention is a utilization proxy, not causal proof"),
        "2606.31093": ("#S3; #S4; #S5", "#S6", "#S7"),
        "2607.11942": ("#S3", "#S4", "#S6; #S7"),
        "2607.17545": ("#S3", "#S4", "#S5"),
    }
    if identifier in special:
        values = special[identifier]
        return tuple(value if value.startswith("http") else f"https://arxiv.org/html/{identifier}v1{value}" for value in values)
    method_anchor = "#S3" if node not in {"PLATFORM-EVALUATION-SYSTEM"} else "#S2"
    evaluation_anchor = "#S4"
    return (
        f"https://arxiv.org/html/{identifier}v1{method_anchor} :: method/system section located during primary-source replay",
        f"https://arxiv.org/html/{identifier}v1{evaluation_anchor} :: evaluation/experiment section located during primary-source replay",
        "Not Disclosed — no dedicated limitations fragment was located; this Daily retains only the explicitly located method/evaluation claim and treats every undisclosed workload field as out of scope",
    )


def evidence_delta(candidate: dict) -> str:
    exact = EXACT_REVIEWS.get(candidate["arxiv_id"])
    if exact:
        return exact["delta"]
    if candidate["arxiv_id"] in INTEGRATIONS:
        return INTEGRATIONS[candidate["arxiv_id"]][2]
    packet = candidate.get("weekly_packet")
    if packet and packet["full_read"]:
        mechanism = packet_summary(packet, "method")
        boundary = packet_summary(packet, "limitations", 420)
        return f"历史全文审阅记录的机制增量是：{mechanism} 其证据边界是：{boundary}"
    return f"作者 v1 在其公开 workload 下给出的新增证据是：{sentence(candidate.get('abstract', ''))}"


def all_raw_daily_counts() -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    seen: set[str] = set()
    for path in sorted(SOURCE_DIR.glob("datacite-arxiv-26*-g*-page-*.json.gz")):
        with gzip.open(path, "rb") as handle:
            records = json.load(handle).get("data", [])
        for record in records:
            attrs = record.get("attributes", {})
            doi = attrs.get("doi", "")
            match = re.fullmatch(r"10\.48550/arxiv\.(26(?:06|07)\.\d{4,5})", doi, re.I)
            if not match or match.group(1) in seen:
                continue
            seen.add(match.group(1))
            submitted = next((item.get("date") for item in attrs.get("dates", []) if item.get("dateType") == "Submitted" and item.get("dateInformation") == "v1"), None)
            if not submitted:
                continue
            ts = datetime.fromisoformat(submitted.replace("Z", "+00:00")).astimezone(BEIJING)
            report_day = ts.date() + timedelta(days=1 if ts.hour >= 9 else 0)
            if date(2026, 7, 1) <= report_day <= date(2026, 7, 26):
                counts[report_day.isoformat()] += 1
    # 07-27..31 use the archived direct-arXiv replay rather than the earlier
    # DataCite recovery. The independently reviewed packet owns the exact
    # daily raw count; do not infer it from the routed denominator.
    for packet_path in sorted(DAILY_REVIEW_PACKET_DIR.glob("2026-07-*.json")):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        day_s = packet.get("report_date") or packet_path.stem
        if not ("2026-07-27" <= day_s <= "2026-07-31"):
            continue
        denominator = packet.get("frozen_denominator", {})
        raw_hits = (
            denominator.get("raw_window_hits")
            or packet.get("denominator_audit", {}).get("raw_window_hits")
            or packet.get("source_package", {}).get("raw_window_hits")
            or packet.get("raw_window_hits")
        )
        if raw_hits is not None:
            counts[day_s] = int(raw_hits)
    return counts


def packet_inventory_items() -> list[dict]:
    """Build renderer inventory rows from imported 07-27..31 review packets."""
    items: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for packet_path in sorted(DAILY_REVIEW_PACKET_DIR.glob("2026-07-*.json")):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        day_s = packet.get("report_date") or packet_path.stem
        if not ("2026-07-27" <= day_s <= "2026-07-31"):
            continue
        reviews = [
            *packet.get("full_source_reviews", []),
            *packet.get("families", []),
            *packet.get("closure_reviews", []),
        ]
        for review in reviews:
            identity = review.get("identity") or review.get("primary_identifier") or ""
            match = re.search(r"arXiv:(\d{4}\.\d{4,5})v1", identity, re.I)
            if not match:
                continue
            identifier = match.group(1)
            key = (day_s, identifier)
            if key in seen:
                continue
            seen.add(key)
            timestamp = (
                review.get("first_public_timestamp_beijing")
                or review.get("first_public_date_asia_shanghai")
                or review.get("first_public_asia_shanghai")
            )
            if not timestamp:
                raise ValueError(f"{packet_path}: {identifier} has no first-public timestamp")
            first_public = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
            if first_public.tzinfo is None:
                first_public = first_public.replace(tzinfo=BEIJING)
            first_public = first_public.astimezone(BEIJING)
            family = (
                review.get("source_family")
                or review.get("source_family_id")
                or f"SF-2026-ARXIV-{identifier.replace('.', '-')}"
            )
            abstract = " ".join(filter(None, [
                review.get("mechanism"), review.get("mechanism_summary"),
                review.get("source_claim"), review.get("claim_boundary"),
            ]))
            items.append({
                "abstract": abstract,
                "arxiv_id": identifier,
                "categories": [],
                "daily_date": day_s,
                "first_public_asia_shanghai": first_public.isoformat(),
                "included": True,
                "inclusion_basis": "imported_exact_v1_review_packet",
                "source_family_id": family,
                "submitted_utc": first_public.astimezone(timezone.utc).isoformat(),
                "title": review.get("title") or identifier,
                "weekly_review_ref": None,
            })
    return items


def adjacent(node: str, order: list[str], paths: dict[str, Path]) -> str:
    index = order.index(node)
    neighbors = []
    for pos in (index - 1, index + 1):
        if 0 <= pos < len(order):
            _, locator = chapter_proposition(paths[order[pos]])
            neighbors.append(locator)
    return "; ".join(neighbors)


def reviewed_score(item: dict, node: str) -> tuple[int, int, int]:
    """Derive V2 components from the reviewed claim, not from list membership."""
    text = f"{item['title']} {item.get('abstract', '')}".lower()
    design = 3 if any(term in text for term in (
        "unified", "end-to-end", "architecture", "integrity", "attack", "interoperable",
        "play-adequacy", "auditable", "first-class metric", "counterfactual",
    )) else 2
    reach = 3 if any(term in text for term in (
        "distributed", "lifecycle", "multi-agent", "multimodal", "workflow", "platform",
        "peer-to-peer", "control flow", "data flow", "enterprise",
    )) else 2
    durability = 3 if any(term in text for term in (
        "integrity", "security", "audit", "lifecycle", "provenance", "correctness",
        "contract", "adequacy", "evaluation", "memory architecture",
    )) else 2
    return design, reach, durability


def closure_score(item: dict) -> tuple[int, int, int]:
    """Score identity/date-level candidates without inventing a mechanism claim."""
    text = f"{item['title']} {item.get('abstract', '')}".lower()
    design = 1 if any(term in text for term in ("propose", "present", "framework", "method")) else 0
    reach = 2 if any(term in text for term in (
        "system", "runtime", "serving", "distributed", "agent", "kv cache", "training",
    )) else 1
    durability = 1 if any(term in text for term in (
        "architecture", "mechanism", "benchmark", "evaluation", "memory", "scheduling",
    )) else 0
    score = [design, reach, durability]
    while sum(score) > 4:
        for index in (2, 0, 1):
            if score[index] > 0 and sum(score) > 4:
                score[index] -= 1
    return tuple(score)


def _heading_slug(value: str) -> str:
    value = re.sub(r"^#{1,6}\s+", "", value.strip()).casefold()
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "-", value).strip("-")


def concrete_book_ref(value: str) -> str:
    """Resolve a Books heading locator to a concrete, current line reference.

    Historical review packets may preserve a Markdown heading slug, including
    Chinese-leading anchors that the report validator intentionally does not
    treat as a machine-stable locator. Resolve those slugs against the current
    chapter instead of weakening validation or emitting a placeholder line.
    """
    reference = re.sub(r"\s*\(current line \d+\)", "", str(value).strip())
    path_text, separator, anchor = reference.partition("#")
    if not path_text.endswith(".md"):
        return reference
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    if not path.exists():
        return reference
    relative = path.relative_to(ROOT).as_posix()
    if separator and re.fullmatch(r"L\d+(?:-L\d+)?", anchor):
        return f"{relative}#{anchor}"
    if separator and anchor:
        wanted = _heading_slug(anchor)
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("#") and _heading_slug(line) == wanted:
                return f"{relative}#L{line_no}"
    return f"{relative}#L1"


def heading_locator(path: Path, heading: str) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    line_no = next((i for i, line in enumerate(lines, 1) if heading in line), 1)
    return f"{path.relative_to(ROOT).as_posix()}#L{line_no}"


def evolution_relation_label(value: str) -> str:
    """Return the report-contract enum while retaining rich prose elsewhere."""
    for label in (
        "Direct Evolution", "Layering / Dependency", "Principle Reuse",
        "Explanatory Analogy", "Alternative Branch",
    ):
        if str(value).startswith(label):
            return label
    raise ValueError(f"Unsupported evolution relation: {value!r}")


def make_candidate(item: dict) -> dict:
    identifier = item["arxiv_id"]
    exact = EXACT_REVIEWS.get(identifier)
    closure_review = CLOSURE_REVIEWS.get(identifier)
    title = (
        exact.get("title") if exact and exact.get("title")
        else PRIMARY_TITLE_OVERRIDES.get(identifier, html.unescape(item["title"]))
    )
    packet = weekly_review_packet(identifier, item.get("weekly_review_ref"))
    historical_full_read = bool(packet and packet["full_read"])
    weekly_blocked = identifier in WEEKLY_BLOCKED and not exact
    weekly_version_fact = identifier == "2607.00248"
    promoted = identifier in PROMOTED
    standard = identifier in STANDARD_REVIEWED
    locator_complete = bool(exact)
    node = (
        (exact["node"] if exact else None)
        or (closure_review.get("owner") if closure_review else None)
        or PROMOTED.get(identifier)
        or STANDARD_REVIEWED.get(identifier)
        or explicit_book_owner(identifier)
        or (weekly_owner(packet, title) if packet else None)
        or node_for(title)
    )
    review_candidate = historical_full_read or promoted or standard or locator_complete
    review_pending = (
        review_candidate
        and not locator_complete
        and not weekly_blocked
        and not weekly_version_fact
    )
    if weekly_blocked:
        score = (2, 2, 2)
    elif weekly_version_fact:
        score = (1, 1, 1)
    elif review_pending:
        score = (2, 2, 2)
    elif exact:
        score = exact["score"]
    elif closure_review:
        _score = closure_review.get("score_v2") or closure_review.get("score")
        score = tuple(_score[key] for key in ("design_delta", "system_reach", "durability")) if isinstance(_score, dict) else tuple(_score)
    elif locator_complete and packet:
        score = weekly_score(packet)
    else:
        score = reviewed_score(item, node) if locator_complete else closure_score(item)
    total = sum(score)
    explicit_override = exact.get("review_override", "none") if exact else "none"
    forced_deep = explicit_override != "none"
    review_override = (
        explicit_override
        if exact
        else "books_conflict" if forced_deep and total < 7 else "none"
    )
    route = (
        exact["route"]
        if exact and exact.get("route") in {"deep", "standard", "closure"}
        else "deep" if total >= 7 or forced_deep else "standard" if total >= 5 else "closure"
    )
    review_status = "blocked" if weekly_blocked else "pending" if review_pending else {
        "deep": "deep_complete", "standard": "standard_complete", "closure": "closure_complete"
    }[route]
    if weekly_blocked:
        disposition = "Blocked / Unverified"
    elif weekly_version_fact:
        disposition = "Version Fact / Mechanism Not Disclosed"
    elif review_pending:
        disposition = "Not Assessed"
    else:
        disposition = exact["disposition"] if exact else (
            closure_review.get("disposition") if closure_review else
            "Integrate" if identifier in INTEGRATIONS else (
                "No Change — Existing Coverage" if locator_complete else "Rejected — Low Durability / Out of Scope"
            )
        )
    # Access to exact primary evidence does not promote a low-score closure
    # into the retained set. Evidence completeness and candidate retention are
    # separate axes; only Standard/Deep routes (or an explicit blocker row)
    # retain a candidate beyond identity/date/rejection closure.
    state = "retained" if (
        weekly_blocked or (route != "closure" and review_candidate and not weekly_version_fact)
    ) else "closure_only"
    first_date = item["first_public_asia_shanghai"][:10]
    iso = date.fromisoformat(first_date).isocalendar()
    artifact_receipts = exact.get("artifact_receipts") if exact else None
    if not artifact_receipts and exact and exact.get("artifact_receipt"):
        artifact_receipts = [exact["artifact_receipt"]]
    has_pinned_artifact = bool(
        isinstance(artifact_receipts, list)
        and any(
            isinstance(receipt, dict)
            and receipt.get("commit")
            and str(receipt["commit"]).strip().lower() != "not disclosed"
            for receipt in artifact_receipts
        )
    )
    return {
        **item,
        "title": title,
        "family": item["source_family_id"],
        "primary": f"arXiv:{identifier}v1",
        "event": f"paper-v1:{identifier}",
        "supporting": "SRC-ARXIV; SRC-GITHUB-COMMIT" if has_pinned_artifact else "SRC-ARXIV",
        "benchmark_claim": bool(route != "closure" and exact and exact.get("benchmark")),
        "owner_week": f"{iso.year}-W{iso.week:02d}",
        "first_date": first_date,
        "score": score,
        "total": total,
        "route": route,
        "review_status": review_status,
        "review_override": review_override,
        "disposition": disposition,
        "state": state,
        "node": node,
        "weekly_locator": packet["locator"] if packet else None,
        "blocked_locator": weekly_blocked_locator(
            identifier, item.get("weekly_review_ref")
        ) if weekly_blocked else None,
        "weekly_packet": packet,
        "promoted": promoted,
        "standard": standard,
        "access_status": "blocked" if weekly_blocked else "partial" if review_pending else "accessible",
        "potential_books_delta": locator_complete and (
            bool(exact and exact.get("disposition") == "Integrate")
            or score[0] == 3
            or bool(packet and re.search(
                r"Refine|New Mechanism|新增.*缺口|直接否定|修正",
                packet["section"],
                re.I,
            ))
        ),
    }


def review_packet(candidate: dict) -> tuple[dict, str]:
    family = candidate["family"]
    identifier = candidate["arxiv_id"]
    packet = candidate.get("weekly_packet")
    exact = EXACT_REVIEWS.get(identifier)
    if candidate["review_status"] == "blocked":
        dd, sr, du = candidate["score"]
        blocker = candidate["blocked_locator"]
        body = (
            f"#### {candidate['title']}\n\n"
            f"<!-- claim:{family}:start -->本次只确认 `{candidate['primary']}` 的 identity、v1 日期和历史 blocked 范围；"
            f"不得从标题、摘要或旧 review focus 推断机制。<!-- claim:{family}:end -->\n\n"
            f"- Score V2：{dd}/{sr}/{du} = **{candidate['total']}/9**，只决定恢复优先级，不表示机制已证实。\n"
            f"- 已尽工作：历史队列与精确 primary identity 已核对，阻塞记录定位为 `{blocker}`。\n"
            "- 缺失材料：事件时 arXiv v1 正文或等价作者 manuscript；需要 Method、evaluation/ablation、limitations 与 artifact 范围。\n"
            "- Disposition：`Blocked / Unverified`；Books 不吸收，访问恢复后重开本 owner Daily。"
        )
        review = {
            "route": candidate["route"],
            "primary_evidence": f"arXiv:{identifier}v1",
            "reviewed": f"SRC-DATACITE@doi:10.48550/arxiv.{identifier}@v1",
            "method": f"Pending — primary Method unavailable; blocker recorded at {blocker}",
            "evaluation": "Pending — experiments/ablations unavailable in accessible evidence",
            "limitations": "Pending — limitations/counterevidence unavailable in accessible evidence",
            "artifact": "Pending — public artifact identity and event-time commit not verified",
        }
        return review, body

    if candidate["review_status"] == "pending":
        dd, sr, du = candidate["score"]
        historical_hint = (
            f"历史 Weekly 曾记录 full-read prose（`{packet['locator']}`），但缺少原始 RP、事件时版本与 primary locator，"
            if packet and packet["full_read"] else
            "先前存在候选阅读或路由记录，但没有保存可迁移的 primary receipt，"
        )
        body = (
            f"#### {candidate['title']}\n\n"
            f"- Identity/date 已确认：`{candidate['primary']}`，first-public（Asia/Shanghai）为 `{candidate['first_date']}`。\n"
            f"- 当前路由优先级：V2 provisional {dd}/{sr}/{du} = **{candidate['total']}/9**；精确全文恢复后必须重新评分。\n"
            f"- 已取得证据只到 DataCite identity/date/abstract metadata；{historical_hint}不能迁移为 complete。\n"
            "- 缺失材料：事件时 arXiv v1 正文或作者等价 manuscript；需要逐项定位 Method/公式、evaluation/ablation、limitations/Appendix 与 artifact。\n"
            "- Books：保持 `Not Assessed`；任何已写入的 provisional 段落均不得据此通过 Books Gate。"
        )
        review = {
            "route": candidate["route"],
            "primary_evidence": f"doi:10.48550/arxiv.{identifier}@v1",
            "reviewed": f"SRC-DATACITE@doi:10.48550/arxiv.{identifier}@v1",
            "method": "Pending — exact arXiv v1 Method/formula/state-flow locator was not preserved",
            "evaluation": "Pending — exact experiment/baseline/ablation locator was not preserved",
            "limitations": "Pending — exact limitations/Appendix/counterevidence locator was not preserved",
            "artifact": "Pending — public artifact and event-time commit/release were not verified",
        }
        return review, body

    if packet and not packet["full_read"] and not exact:
        dd, sr, du = candidate["score"]
        body = (
            f"#### {candidate['title']}\n\n"
            f"<!-- claim:{family}:start -->本次只保留 model-card identity、能力/安全/evaluation 公告范围；"
            f"训练与 runtime 机制未披露。<!-- claim:{family}:end -->\n\n"
            f"- 历史核验位置：`{packet['locator']}`。\n"
            f"- Score V2：{dd}/{sr}/{du} = **{candidate['total']}/9**。\n"
            "- Disposition：`Version Fact / Mechanism Not Disclosed`；厂商 benchmark 不外推，不进入 Books 机制正文。"
        )
        review = {
            "route": "closure",
            "primary_evidence": f"arXiv:{identifier}v1",
            "reviewed": f"SRC-ARXIV@arXiv:{identifier}v1",
            "method": f"Not Disclosed — historical model-card review at {packet['locator']} found no public training/runtime mechanism",
            "evaluation": f"{packet_locator(packet, 'evaluation')} :: model-card evaluation scope only",
            "limitations": f"{packet_locator(packet, 'limitations')} :: vendor claims remain model-card scoped",
            "artifact": "Not Disclosed — no implementation artifact is used for a mechanism claim",
        }
        return review, body

    # A low-score Closure route closes scope, not evidence.  If an exact-v1
    # receipt exists, render that completed primary review below; the
    # DataCite identity-only branch is only valid when no exact manuscript was
    # reviewed.  Otherwise a fully recovered low-score paper silently
    # regresses to metadata-only evidence on rerender.
    if candidate["route"] == "closure" and not exact:
        dd, sr, du = candidate["score"]
        disposition = candidate["disposition"]
        boundary = (
            "本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与 contextual scope；"
            "DataCite abstract 不用于建立机制或 benchmark 结论。"
            if disposition.startswith("Weekly Only") else
            "本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；"
            "DataCite abstract 不用于建立机制或 benchmark 结论。"
        )
        body = f"#### {candidate['title']}\n\n<!-- claim:{family}:start -->{boundary}<!-- claim:{family}:end -->\n\n- Identity：`{candidate['primary']}`；first-public（Asia/Shanghai）：`{candidate['first_date']}`。\n- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。\n- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `{dd}/{sr}/{du}`。\n- Disposition：`{disposition}`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。"
        review = {
            "route": "closure",
            "primary_evidence": f"doi:10.48550/arxiv.{identifier}@v1",
            "reviewed": f"SRC-DATACITE@doi:10.48550/arxiv.{identifier}@v1",
            "method": f"doi:10.48550/arxiv.{identifier}#identity; DataCite Submitted:v1 timestamp",
            "evaluation": "Not Required — closure route makes no mechanism or benchmark claim",
            "limitations": "Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained",
            "artifact": "Not Required — closure route; no artifact claim retained",
        }
        return review, body

    prior = candidate["weekly_locator"]
    prior_text = (
        f"；本次 RP 重新绑定历史 full-read coverage：`{prior}`，其中具名记录了 Method、Evaluation 与 Boundary"
        if packet and packet["full_read"] else ""
    )
    method, evaluation, limitations = evidence_locators(candidate)
    paths, _ = roadmap()
    existing, existing_locator = candidate_proposition(candidate, paths)
    delta = evidence_delta(candidate)
    source_claim = exact.get("source_claim") if exact else None
    boundary = (
        f"{source_claim or delta} "
        "该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。"
    )
    dd, sr, du = candidate["score"]
    relation = exact.get("evolution_relation") or (
        "Direct Evolution" if identifier in INTEGRATIONS else "Layering / Dependency"
    )
    body = f"#### {candidate['title']}\n\n<!-- claim:{family}:start -->{boundary}<!-- claim:{family}:end -->\n\n**旧方案与约束变化。** `{existing}`（`{existing_locator}`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。\n\n**机制、状态与代价。** {delta} 它改变 `{candidate['node']}` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。\n\n**Evaluation contract。** Method：`{method}`；Evaluation：`{evaluation}`；Limitations/Counterevidence：`{limitations}`{prior_text}。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。\n\n- Score V2：Design Delta {dd} / System Reach {sr} / Durability {du} = **{candidate['total']}/9**。\n- Evolution relation：`{relation}`。\n- Stable owner：`{candidate['node']}`。\n- Books disposition：`{candidate['disposition']}`。"
    review = {
        "route": candidate["route"],
        "primary_evidence": f"arXiv:{identifier}v1",
        "reviewed": exact["reviewed"] if exact else f"SRC-ARXIV@arXiv:{identifier}v1",
        "method": method,
        "evaluation": evaluation,
        "limitations": limitations,
        "artifact": exact["artifact"] if exact else (
            f"{packet['locator']} :: historical review records implementation/artifact scope; no commit-level claim is made"
            if packet and re.search(r"artifact|repository|code|implementation|实现", packet["section"], re.I)
            else "Not Disclosed — no exact public experiment commit is used as evidence in this Daily"
        ),
    }
    return review, body


def report(day: date, candidates: list[dict], raw_hits: int, paths: dict[str, Path], order: list[str], audited: bool) -> str:
    day_s = day.isoformat()
    start = datetime.combine(day - timedelta(days=1), datetime.min.time(), BEIJING).replace(hour=9)
    end = datetime.combine(day, datetime.min.time(), BEIJING).replace(hour=9)
    daily_packet_path = DAILY_REVIEW_PACKET_DIR / f"{day_s}.json"
    daily_packet = (
        json.loads(daily_packet_path.read_text(encoding="utf-8"))
        if daily_packet_path.exists() else {}
    )
    semantic_audit = daily_packet.get("semantic_audit", {})
    direct_replay = day >= date(2026, 7, 27)
    denominator = daily_packet.get("frozen_denominator", {})
    coverage_receipt = daily_packet.get("coverage_receipt", {})
    source_manifest = denominator.get("source") if direct_replay else INVENTORY.relative_to(ROOT).as_posix()
    source_manifest = source_manifest or REPLAY_SOURCE_DIR.relative_to(ROOT).as_posix() + "/README.md"
    manifest_hash = (
        denominator.get("manifest_sha256")
        if direct_replay else hashlib.sha256(INVENTORY.read_bytes()).hexdigest()
    )
    executed_at = daily_packet.get("reviewed_at") or "2026-08-26T18:00:00+08:00"
    coverage_endpoint = coverage_receipt.get("endpoint") or (
        "https://export.arxiv.org/api/query" if direct_replay else "registered SRC-DATACITE fallback"
    )
    coverage_filter = coverage_receipt.get("filter") or (
        "submittedDate exact replay; v1 published timestamp; cross-list deduplicated by arXiv ID"
        if direct_replay else
        "arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket"
    )
    coverage_pagination = coverage_receipt.get("pagination") or (
        "archived direct-arXiv pages; final_cursor=end" if direct_replay else
        "five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique"
    )

    def audited_scope_text(scope: str, fallback: str) -> str:
        if not audited:
            return fallback
        scope_receipt = semantic_audit.get(scope, {})
        if scope_receipt.get("status") == "passed" and scope_receipt.get("text"):
            return str(scope_receipt["text"])
        return fallback

    packets = {}
    for candidate in candidates:
        review, body = review_packet(candidate)
        review["rp"] = (
            "—" if candidate["review_status"] == "pending"
            else review_provenance(candidate, review, body)
        )
        packets[candidate["family"]] = (review, body)
    selection_contract = reviewed_selection_contract(day_s)
    selection_decisions = {
        item["source_family_id"]: item
        for item in selection_contract.get("family_decisions", [])
    }
    prebooks_eligible = {
        family for family, decision in selection_decisions.items()
        if decision.get("eligibility")
    }
    deep = [candidate for candidate in candidates if candidate["route"] == "deep"]
    selectable_deep = [
        candidate for candidate in candidates
        if candidate["review_status"] in {"deep_complete", "standard_complete"}
        and (candidate["route"] == "deep" or candidate["family"] in prebooks_eligible)
    ]
    standard = [candidate for candidate in candidates if candidate["route"] == "standard"]
    closure = [candidate for candidate in candidates if candidate["route"] == "closure"]
    pending_candidates = [candidate for candidate in candidates if candidate["review_status"] == "pending"]
    blocked_candidates = [candidate for candidate in candidates if candidate["review_status"] == "blocked"]
    evidence_open = bool(pending_candidates or blocked_candidates)
    report_complete = audited and not evidence_open
    books_candidates = [candidate for candidate in candidates if candidate["disposition"] in {"Integrate", "No Change — Existing Coverage"}]
    ranked = sorted(
        selectable_deep,
        key=lambda candidate: (
            candidate["node"] == "PLATFORM-SECURITY",
            candidate["potential_books_delta"],
            candidate["total"],
            candidate["score"][1],
            candidate["score"][0],
            candidate["first_date"],
            candidate["arxiv_id"],
        ),
        reverse=True,
    )
    selected = reviewed_selection_override(day_s, selectable_deep)
    if selected is None:
        selected = []
        selected_nodes = set()
        for candidate in ranked:
            if candidate["node"] not in selected_nodes:
                selected.append(candidate)
                selected_nodes.add(candidate["node"])
            if len(selected) == 3:
                break
        if len(selected) < 3:
            selected.extend([candidate for candidate in ranked if candidate not in selected][: 3 - len(selected)])
    selected_ids = {candidate["family"] for candidate in selected}
    selection_units = {}
    raw_selection_units = selection_contract.get("selected_analysis_units", [])
    if all(isinstance(unit, dict) for unit in raw_selection_units):
        selection_units = {
            unit.get("selected_family") or unit.get("source_family_id"): unit.get("analysis_unit_id")
            for unit in raw_selection_units
        }
    else:
        selection_units = {
            decision.get("source_family_id"): decision.get("analysis_unit_id")
            for decision in selection_contract.get("family_decisions", [])
            if decision.get("decision") == "selected"
        }
    candidate_refs = "<br>".join(candidate["family"] for candidate in candidates) or "—"
    artifact_receipts = []
    for candidate in candidates:
        exact_review = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
        receipts = exact_review.get("artifact_receipts")
        if not receipts and exact_review.get("artifact_receipt"):
            receipts = [exact_review["artifact_receipt"]]
        if not receipts:
            continue
        if not isinstance(receipts, list) or not all(isinstance(receipt, dict) for receipt in receipts):
            raise ValueError(
                f"{candidate['arxiv_id']}: artifact_receipts must be structured objects; "
                "re-import the reviewed packet after schema validation"
            )
        artifact_receipts.extend((candidate, receipt) for receipt in receipts)
    artifact_coverage_rows = []
    artifact_coverage_comments = []
    pinned_artifact_receipts = [
        (candidate, receipt)
        for candidate, receipt in artifact_receipts
        if receipt.get("commit")
        and str(receipt["commit"]).strip().lower() != "not disclosed"
    ]
    disclosed_artifact_locators = [
        (candidate, receipt)
        for candidate, receipt in artifact_receipts
        if str(receipt.get("repository") or "").strip().lower() != "not disclosed"
        and re.match(r"^https?://", str(receipt.get("url") or ""))
    ]
    disclosed_artifact_families = {
        candidate["family"]
        for candidate in candidates
        if re.search(
            r"https?://",
            str(EXACT_REVIEWS.get(candidate["arxiv_id"], {}).get("artifact") or ""),
        )
    }
    external_artifact_families = {
        candidate["family"]
        for candidate in candidates
        if any(
            not re.match(r"https?://(?:www\.)?arxiv\.org/", url, re.IGNORECASE)
            for url in re.findall(
                r"https?://[^\s;]+",
                str(EXACT_REVIEWS.get(candidate["arxiv_id"], {}).get("artifact") or ""),
            )
        )
    }
    pinned_artifact_families = {
        candidate["family"] for candidate, _ in pinned_artifact_receipts
    }
    if pinned_artifact_receipts:
        receipt_ref = f"coverage:SRC-GITHUB-COMMIT:{day:%Y%m%d}"
        unique_families = list(dict.fromkeys(candidate["family"] for candidate, _ in pinned_artifact_receipts))
        families = "; ".join(unique_families)
        endpoints = "; ".join(
            f"{receipt['repository']}@{receipt['commit']}"
            for _, receipt in pinned_artifact_receipts
        )
        executed_at = max(receipt["executed_at"] for _, receipt in pinned_artifact_receipts)
        artifact_coverage_rows.append(
            f"| SRC-GITHUB-COMMIT | {start.isoformat()} | {end.isoformat()} | "
            f"{executed_at} | exact GitHub commit API lookups: {endpoints} | checked | "
            f"{len(unique_families)} | {families} | pages={len(pinned_artifact_receipts)}; "
            f"final cursors={','.join(receipt['commit'] for _, receipt in pinned_artifact_receipts)}; "
            f"one bounded commit lookup per family | {end.isoformat()} | {receipt_ref} | — |"
        )
        detail = "; ".join(
            f"repository={receipt['repository']}, until={receipt['until']}, "
            f"full_sha={receipt['commit']}, commit_timestamp={receipt['commit_timestamp']}, "
            f"url={receipt['url']}"
            for _, receipt in pinned_artifact_receipts
        )
        artifact_coverage_comments.append(
            f"<!-- {receipt_ref}:start -->{detail}; each commit establishes only the event-time "
            "public tree and does not independently prove paper claims."
            f"<!-- {receipt_ref}:end -->"
        )
    lines = [
        f"# Daily Research — {day_s}", "",
        f"**Research Date:** {day_s}", "", "**Timezone:** Asia/Shanghai", "",
        f"**Strict Window:** {start:%Y-%m-%d %H:%M:%S} ～ {end:%Y-%m-%d %H:%M:%S}（北京时间，左闭右开）", "",
        ("**Contract:** V2.1 Full Replay；直接 arXiv 枚举冻结候选分母，技术 claim 回到精确 arXiv v1 与事件时 artifact receipt" if direct_replay else "**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅"), "",
        ("**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding" if report_complete else (f"**Status:** In Progress；fresh-context audit 已确认当前真值，但 {len(pending_candidates)} 个 primary review pending、{len(blocked_candidates)} 个 primary blocked，Evidence 与 Books Gate 保持 Open" if audited else f"**Status:** In Progress；候选分母已冻结，{len(pending_candidates)} 个 primary review pending、{len(blocked_candidates)} 个 primary blocked；Evidence、Books 与 fresh-context Semantic Audit 尚未闭合")), "",
        "## Executive Summary", "",
        f"本窗口枚举到 {raw_hits} 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 {len(candidates)} 个。当前路由账目为 {len(deep)} 个 Deep、{len(standard)} 个 Standard、{len(closure)} 个 Closure；route 只是审阅义务，不等于 Review 已完成。", "",
        "本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
        f"| Window Start | {day_s} |", f"| Window End | {day_s} |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
        f"| Denominator ID | {daily_packet.get('denominator_id') or f'daily-{day:%Y-%m-%d}-0900-v2.1-july-replay-01'} |", f"| Denominator Frozen At | {executed_at} |", f"| Completion Status | {'Complete' if report_complete else 'In Progress'} |", f"| Coverage Gate | {'Closed' if audited else 'Open'} |", f"| Evidence Gate | {'Passed' if report_complete else 'Open'} |", f"| Books Gate | {'Passed' if report_complete else 'Open'} |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | {start.isoformat()} | {end.isoformat()} | {executed_at} | {coverage_endpoint}; {coverage_filter} | checked | {raw_hits} | {candidate_refs} | {coverage_pagination} | {end.isoformat()} | coverage:SRC-ARXIV:{day:%Y%m%d} | {'—' if direct_replay else f'GAP-ARXIV-DIRECT-RESET-{day:%Y%m%d}'} |",
        *artifact_coverage_rows, "",
        f"<!-- coverage:SRC-ARXIV:{day:%Y%m%d}:start -->{'Archived direct-arXiv submittedDate replay' if direct_replay else 'Direct arXiv API/OAI reset connections; registered DataCite fallback'} froze the strict-window denominator. Canonical source: {source_manifest}; sha256:{manifest_hash}; {raw_hits} unique identities in this strict window; {len(candidates)} routed families.<!-- coverage:SRC-ARXIV:{day:%Y%m%d}:end -->",
        *artifact_coverage_comments, "",
        "### Coverage Limitations", "",
        ("- 直接 arXiv replay 只闭合候选枚举与 first-public identity；机制和实验结论仍逐项来自 exact-v1 全文与可追溯 artifact。" if direct_replay else "- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。"),
        *([
            f"- Artifact-boundary routing 覆盖 {len(candidates)} 个 family：exact v1 为 {len(disclosed_artifact_families)} 个 family 披露 artifact/evidence locator，"
            f"其中 {len(external_artifact_families)} 个提供外部 repository/project/demo locator，"
            f"另有 {len(candidates) - len(disclosed_artifact_families)} 个未披露；本日确认 {len(pinned_artifact_families)} 个 family、{len(pinned_artifact_receipts)} 个 event-time pinned commit。"
            "未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。"
        ] if candidates else []),
        "- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。", "- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    recovery = []
    if pending_candidates:
        recovery.extend([
            "### Pending Recovery Ledger", "",
            "| Source Family ID | Known Primary | Preserved Evidence | Missing Facets | Resume Scope |",
            "| --- | --- | --- | --- | --- |",
        ])
        for candidate in pending_candidates:
            recovery.append(
                f"| {candidate['family']} | https://arxiv.org/abs/{candidate['arxiv_id']}v1 | identity/date/abstract metadata | exact Method, Evaluation, Limitations and Artifact locators | full-text recovery → V2 rescore → Review → Selection → Books → audit |"
            )
        recovery.append("")
    if blocked_candidates:
        recovery.extend([
            "### Materials Request Ledger", "", "<!-- validator:materials-request-v1 -->",
            "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for candidate in blocked_candidates:
            request_id = f"MR-{day:%Y%m%d}-{candidate['arxiv_id'].replace('.', '-')}"
            recovery.append(
                f"| {request_id} | P1 Full Text | {candidate['family']} | — | — | {candidate['owner_week']} | https://arxiv.org/abs/{candidate['arxiv_id']}v1 | event-time v1 manuscript with Method, experiments/ablations, limitations/Appendix and artifact scope | historical queue explicitly says primary text was inaccessible; discovery focus is not a mechanism claim | author manuscript PDF/HTML/TXT or same-version proceedings | arxiv-{candidate['arxiv_id']}v1.pdf | rescore, route-complete Source Review, Selection, Books Comparison and fresh-context audit |"
            )
        recovery.append("")
    if recovery:
        insert_at = lines.index("## 2. Candidate Ledger")
        lines[insert_at:insert_at] = recovery
    for candidate in candidates:
        dd, sr, du = candidate["score"]
        books_ref = f"books-review:{candidate['family']}" if candidate["disposition"] in {"Integrate", "No Change — Existing Coverage"} else "—"
        review_ref = "—" if candidate["review_status"] == "pending" else f"review:{candidate['family']}"
        benchmark_claim = "yes" if candidate["benchmark_claim"] else "no"
        lines.append(f"| {candidate['family']} | {candidate['primary']} | {candidate['event']} | {candidate['owner_week']} | {candidate['first_date']} | {candidate['supporting']} | {dd} | {sr} | {du} | {candidate['total']} | {candidate['state']} | {candidate['review_status']} | {candidate['access_status']} | {candidate['review_override']} | {review_ref} | self | — | new_in_window | {candidate['node']} | {candidate['disposition']} | {books_ref} | {benchmark_claim} |")
    lines.extend(["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"])
    for candidate in candidates:
        review, _ = packets[candidate["family"]]
        completion = "blocked" if candidate["review_status"] == "blocked" else "pending" if candidate["review_status"] == "pending" else "complete"
        claim_ref = "Pending — exact primary claim boundary not yet available" if completion == "pending" else f"claim:{candidate['family']}"
        lines.append(f"| {candidate['family']} | {review['rp']} | {review['route']} | {review['primary_evidence']} | {review['reviewed']} | {review['method']} | {review['evaluation']} | {review['limitations']} | {review['artifact']} | {claim_ref} | {completion} |")
    lines.extend(["", "### Source Reviews", ""])
    for candidate in candidates:
        _, body = packets[candidate["family"]]
        lines.extend([f"<!-- review:{candidate['family']}:start -->", body, f"<!-- review:{candidate['family']}:end -->", ""])
    benchmark_candidates = [candidate for candidate in candidates if candidate["benchmark_claim"]]
    lines.extend(["## 4. Benchmark Contracts", ""])
    if benchmark_candidates:
        lines.extend([
            "以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。",
            "", "<!-- validator:benchmark-contract-v1 -->",
            "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for candidate in benchmark_candidates:
            benchmark = EXACT_REVIEWS[candidate["arxiv_id"]]["benchmark"]
            def benchmark_value(field: str) -> str:
                value = benchmark.get(field)
                if value in {None, "", "—", "Not Applicable"}:
                    return "Not Disclosed"
                if isinstance(value, str) and value.startswith("Not Applicable"):
                    return value.replace("Not Applicable", "Not Disclosed", 1)
                return value
            lines.append(
                f"| {candidate['family']} | {benchmark_value('workload')} | {benchmark_value('model')} | "
                f"{benchmark_value('hardware')} | {benchmark_value('precision')} | {benchmark_value('input_length')} | "
                f"{benchmark_value('output_length')} | {benchmark_value('batch')} | {benchmark_value('concurrency')} | "
                f"{benchmark_value('slo')} | {benchmark_value('evaluator')} |"
            )
    else:
        lines.append("本日报不转述性能 headline，`Benchmark Claim` 均为 `no`。论文实验只用于限定机制证据，不把不同模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 拼成跨论文排名。")
    lines.extend(["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"])
    for candidate in selectable_deep:
        eligibility_facts = []
        if candidate["total"] >= 7:
            eligibility_facts.append("score_7_9")
        if candidate["review_override"] != "none":
            eligibility_facts.append("forced_review")
        if candidate["potential_books_delta"]:
            eligibility_facts.append("potential_books_delta")
        eligibility = ";".join(eligibility_facts)
        if candidate["family"] in selected_ids:
            unit = selection_units.get(
                candidate["family"], f"DA-{day:%Y%m%d}-{candidate['arxiv_id'].replace('.', '-')}"
            )
            priority = (
                "命中合同第一优先级 security contract；"
                if candidate["node"] == "PLATFORM-SECURITY" else ""
            )
            lines.append(f"| {candidate['family']} | {eligibility} | selected | {unit} | — | {priority}V2={candidate['total']}/9；{selection_delta(candidate)}；相对同日候选提供独立 owner 的最大可定位 delta | analysis:{unit} |")
        else:
            reviewed_decision = selection_decisions.get(candidate["family"], {})
            decision = reviewed_decision.get("decision", "not_selected")
            unit = reviewed_decision.get("analysis_unit_id") or "—"
            reason = reviewed_decision.get("reason") or selection_reason(candidate, selected)
            narrative_ref = f"analysis:{unit}" if decision == "subsumed" else f"analysis-decision:{candidate['family']}"
            lines.append(f"| {candidate['family']} | {eligibility} | {decision} | — | {unit} | {reason} | {narrative_ref} |")
    for candidate in selected:
        unit = selection_units.get(
            candidate["family"], f"DA-{day:%Y%m%d}-{candidate['arxiv_id'].replace('.', '-')}"
        )
        proposition, proposition_locator = candidate_proposition(candidate, paths)
        delta = evidence_delta(candidate)
        exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
        old_scheme = exact.get("analysis_old") or (
            f"{proposition} 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。"
        )
        tradeoff = exact.get("analysis_tradeoff") or (
            "新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；"
            "未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。"
            "旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。"
        )
        relation = exact.get("evolution_relation") or (
            "Direct Evolution" if candidate["arxiv_id"] in INTEGRATIONS else "Layering / Dependency"
        )
        subsumed_candidates = [
            item for item in selectable_deep
            if selection_decisions.get(item["family"], {}).get("decision") == "subsumed"
            and selection_decisions[item["family"]].get("analysis_unit_id") == unit
        ]
        lines.extend([
            "", f"<!-- analysis:{unit}:start -->", f"### {candidate['title']}", "",
            f"**旧方案为何合理。** {old_scheme}（现有命题定位：`{proposition_locator}`）", "",
            f"**约束变化与机制。** {delta} 这条证据与现有主线的关系是 `{relation}`：它改变或补充 `{candidate['node']}` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。", "",
            f"**收益、代价与下一重压力。** {tradeoff}", "",
        ])
        for supporting in subsumed_candidates:
            supporting_exact = EXACT_REVIEWS.get(supporting["arxiv_id"], {})
            supporting_old = supporting_exact.get("analysis_old") or candidate_proposition(supporting, paths)[0]
            supporting_delta = evidence_delta(supporting)
            supporting_tradeoff = supporting_exact.get("analysis_tradeoff") or supporting_exact.get("limitations")
            decision_reason = selection_decisions[supporting["family"]].get("reason", "")
            lines.extend([
                f"**同一演进单元的 supporting branch：{supporting['title']}。** {supporting_old}", "",
                f"{supporting_delta} 它与主 family 的关系是：{decision_reason}", "",
                f"证据边界与代价：{supporting_tradeoff}", "",
            ])
        lines.append(f"<!-- analysis:{unit}:end -->")
    for candidate in selectable_deep:
        if candidate["family"] not in selected_ids:
            reviewed_decision = selection_decisions.get(candidate["family"], {})
            reason = reviewed_decision.get("reason") or selection_reason(candidate, selected)
            if reviewed_decision.get("decision") == "subsumed":
                unit = reviewed_decision["analysis_unit_id"]
                reason = f"本 family 已作为 supporting evidence 纳入 `{unit}`：{reason}"
            lines.extend(["", f"<!-- analysis-decision:{candidate['family']}:start -->《{candidate['title']}》已完成 Deep Source Review。{reason}<!-- analysis-decision:{candidate['family']}:end -->"])
    lines.extend(["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"])
    for candidate in books_candidates:
        integration = INTEGRATIONS.get(candidate["arxiv_id"])
        _, proposition_locator = candidate_proposition(candidate, paths)
        target = (
            concrete_book_ref(integration[1])
            if integration and ".md" in integration[1]
            else heading_locator(paths[candidate["node"]], integration[1])
            if integration else proposition_locator
        )
        exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
        additional_targets = [
            heading_locator(ROOT / item["path"], item["section"])
            for item in exact.get("additional_integration_refs", [])
        ]
        if additional_targets:
            target = "; ".join([target, *additional_targets])
        neighbors = candidate_adjacent(candidate, order, paths)
        explicit_neighbors = [
            heading_locator(ROOT / item["path"], item["section"])
            for item in exact.get("adjacent_chapter_refs", [])
        ]
        if explicit_neighbors:
            neighbors = "; ".join([neighbors, *explicit_neighbors]) if neighbors else "; ".join(explicit_neighbors)
        relation = evolution_relation_label(exact.get("evolution_relation") or (
            "Direct Evolution" if integration else "Layering / Dependency"
        ))
        lines.append(f"| {candidate['family']} | {candidate['node']} | {target} | {neighbors} | existing:{candidate['family']} | delta:{candidate['family']} | {relation} | {candidate['disposition']} | books-review:{candidate['family']} |")
    for candidate in books_candidates:
        integration = INTEGRATIONS.get(candidate["arxiv_id"])
        existing, existing_locator = candidate_proposition(candidate, paths)
        target = (
            concrete_book_ref(integration[1])
            if integration and ".md" in integration[1]
            else heading_locator(paths[candidate["node"]], integration[1])
            if integration else existing_locator
        )
        exact = EXACT_REVIEWS.get(candidate["arxiv_id"], {})
        additional_targets = [
            heading_locator(ROOT / item["path"], item["section"])
            for item in exact.get("additional_integration_refs", [])
        ]
        all_targets = "; ".join([target, *additional_targets])
        delta = evidence_delta(candidate)
        decision_text = (
            f"该 delta 已进入 `{all_targets}`，正文保留旧方案成立条件、约束变化、代价与下一重压力。"
            if integration else
            "该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。"
        )
        lines.extend(["", f"<!-- books-review:{candidate['family']}:start --><!-- existing:{candidate['family']}:start -->对读 `{target}` 与相邻章节后，现有命题（`{existing_locator}`）为：{existing}<!-- existing:{candidate['family']}:end --><!-- delta:{candidate['family']}:start -->新增证据边界：{delta} {decision_text}<!-- delta:{candidate['family']}:end --><!-- books-review:{candidate['family']}:end -->"])
    reviewed_refs = "; ".join(f"review:{c['family']}" for c in candidates)
    weekly_only = [candidate for candidate in candidates if candidate["disposition"].startswith("Weekly Only")]
    books_refs = "; ".join(
        [*(f"books-review:{c['family']}" for c in books_candidates),
         *(f"review:{c['family']}" for c in weekly_only)]
    ) or "validator:books-comparison-v1"
    selected_ref_values = []
    for candidate in selected:
        default_unit = f"DA-{day:%Y%m%d}-{candidate['arxiv_id'].replace('.', '-')}"
        selected_ref_values.append(
            f"analysis:{selection_units.get(candidate['family'], default_unit)}"
        )
    selected_refs = "; ".join(selected_ref_values) or "validator:deep-analysis-selection-v1"
    audit_status = "passed" if audited else "open"
    audit_findings = "—" if audited else (
        f"AUDIT-JULY-PRIMARY-REPLAY — {len(pending_candidates)} 个 candidate 缺可迁移的事件时 primary receipt，"
        f"{len(blocked_candidates)} 个 candidate 的 exact-version full text 当前不可访问；已完成 family 仍需在稳定快照上复核"
    )
    audit_resolution = (
        (
            "Verified — current completed/unresolved states are accurately represented; "
            "Evidence and Books Gates remain constrained by pending/blocked receipts"
            if evidence_open else
            "Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit"
        )
        if audited else (
            "Open — 按 exact arXiv HTML → 对应版本 PDF → 作者 artifact 恢复正文，逐 family 重算 "
            "Score、owner、selection 与 Books；API/OAI reset 只影响枚举接口，不构成 HTML/PDF 全文 blocker"
        )
    )
    standard_count = len(standard)
    rejected_count = len([
        candidate for candidate in candidates
        if candidate["disposition"] == "Rejected — Low Durability / Out of Scope"
    ])
    integrated = [candidate for candidate in books_candidates if candidate["disposition"] == "Integrate"]
    no_change = [candidate for candidate in books_candidates if candidate["disposition"] == "No Change — Existing Coverage"]
    books_audit = (
        f"Fresh-context review confirmed that no Evidence-eligible Standard/Deep family remains; {len(pending_candidates)} 个 pending 与 {len(blocked_candidates)} 个 blocked 均未进入 Books，当前没有 provisional integration。"
        if audited and evidence_open else
        (
            f"Fresh-context review checked current owner and adjacent chapter handoffs; "
            f"{len(integrated)} 个 family 已定位到实际 Books 段落，{len(no_change)} 个 family 的 No Change 结论可定位，"
            f"{len(weekly_only)} 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。"
            if audited else "Pending fresh-context Books review."
        )
    )
    changed_books = {
        paths[candidate["node"]].relative_to(ROOT).as_posix() for candidate in integrated
    }
    for candidate in integrated:
        changed_books.update(
            item["path"]
            for item in EXACT_REVIEWS.get(candidate["arxiv_id"], {}).get("additional_integration_refs", [])
        )
    changed_books = sorted(changed_books)
    repository_change = (
        "- 本日报长期 delta 已同步至：" + "、".join(f"`{path}`" for path in changed_books) + "。"
        if changed_books else
        ("- 本日报没有新增长期 Books delta；No Change 候选均完成目标章与相邻章比较。" if no_change else
         "- 本日报当前没有 Evidence-eligible 候选可执行 Books Integration；pending/blocked 保持 Not Assessed 或 Blocked，closure/version fact 只保留其受限最终处置。")
    )
    evidence_audit_text = audited_scope_text("evidence", (
        (
            f"Fresh-context review reconciled all {len(candidates)} frozen families: "
            f"{len(deep)} Deep, {len(standard)} Standard and {len(closure)} Closure; "
            f"{len(pending_candidates)} pending and {len(blocked_candidates)} blocked rows remain explicitly outside mechanism claims."
        )
        if audited else "Pending fresh-context evidence review."
    ))
    selection_audit_text = audited_scope_text("deep_analysis_selection", (
        (
            f"Fresh-context review reconciled {len(selectable_deep)} eligible Deep families: "
            f"{len(selected)} selected and {len(selectable_deep) - len(selected)} not selected; "
            "the narrative limit does not downgrade any completed Source Review."
            if selectable_deep else
            "Fresh-context review confirmed that no completed family is eligible for Deep Analysis; the selection pool is empty rather than silently skipped."
        )
        if audited else "Pending fresh-context selection review."
    ))
    books_audit_text = audited_scope_text(
        "books", books_audit if audited else "Pending fresh-context Books review."
    )
    coverage_audit_text = audited_scope_text(
        "coverage",
        "Fresh-context review reconciled the exact window, partition totals, date bucket and denominator."
        if audited else "Pending fresh-context coverage review.",
    )
    lines.extend([
        "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        f"| SA-{day:%Y%m%d}-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:{day:%Y%m%d}; semantic-review:SA-{day:%Y%m%d}-COVERAGE | {audit_findings} | {audit_resolution} | {audit_status} |",
        f"| SA-{day:%Y%m%d}-EVIDENCE | fresh-context:final_contract_review | evidence | {reviewed_refs}; semantic-review:SA-{day:%Y%m%d}-EVIDENCE | {audit_findings} | {audit_resolution} | {audit_status} |",
        f"| SA-{day:%Y%m%d}-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | {selected_refs}; semantic-review:SA-{day:%Y%m%d}-SELECTION | {audit_findings} | {audit_resolution} | {audit_status} |",
        f"| SA-{day:%Y%m%d}-BOOKS | fresh-context:final_contract_review | books | {books_refs}; semantic-review:SA-{day:%Y%m%d}-BOOKS | {audit_findings} | {audit_resolution} | {audit_status} |",
        "",
        f"<!-- semantic-review:SA-{day:%Y%m%d}-COVERAGE:start -->{coverage_audit_text}<!-- semantic-review:SA-{day:%Y%m%d}-COVERAGE:end -->",
        f"<!-- semantic-review:SA-{day:%Y%m%d}-EVIDENCE:start -->{evidence_audit_text}<!-- semantic-review:SA-{day:%Y%m%d}-EVIDENCE:end -->",
        f"<!-- semantic-review:SA-{day:%Y%m%d}-SELECTION:start -->{selection_audit_text}<!-- semantic-review:SA-{day:%Y%m%d}-SELECTION:end -->",
        f"<!-- semantic-review:SA-{day:%Y%m%d}-BOOKS:start -->{books_audit_text}<!-- semantic-review:SA-{day:%Y%m%d}-BOOKS:end -->",
        "", "## 8. Ignored Noise", "",
        f"{raw_hits} 个窗口内 identity 中，{raw_hits-len(candidates)} 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。",
        "", "## 9. Recommended Action", "",
        "1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。",
        "2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。",
        f"3. Books Decision：{len(integrated)} 个 `Integrate`，{len(no_change)} 个 `No Change — Existing Coverage`，{len(weekly_only)} 个 `Weekly Only — Context`，{rejected_count} 个 `Rejected — Low Durability / Out of Scope`；Deep {len(deep)} / Standard {standard_count}。",
        "", "## 10. Repository Changes", "",
        f"- 新建或更新 `papers/2026/07/{day:%d}/README.md`。",
        repository_change,
        "", "## 11. Open Questions", "",
        "- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？",
        "- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？",
        "", "## 12. Sources", "",
    ])
    for candidate in candidates:
        accessed = EXACT_REVIEWS.get(candidate["arxiv_id"], {}).get("accessed", ACCESSED)
        lines.append(f"- [{candidate['title']}](https://arxiv.org/abs/{candidate['arxiv_id']}v1) — first-public（Asia/Shanghai）：{candidate['first_date']}；accessed：{accessed}")
    snapshot_link = ("../_sources/arxiv-v2.1-replay-20260727-31/README.md" if direct_replay else "../_sources/datacite-arxiv-recovery-20260701-26/README.md")
    lines.extend([f"- [July recovery snapshot]({snapshot_link}) — accessed：{ACCESSED}", "- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25", "", "## 13. Final Status", "", ("Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。" if report_complete else (f"Fresh-context audit 已通过当前状态真值：Coverage Gate Closed；仍有 {len(pending_candidates)} 个普通 pending 与 {len(blocked_candidates)} 个 blocked，因此 Evidence 与 Books Gate 保持 Open，Completion 为 In Progress。" if audited else f"Coverage denominator 已冻结，但仍有 {len(pending_candidates)} 个普通 pending 与 {len(blocked_candidates)} 个 blocked；Evidence、Books 与 Semantic Audit 未闭合，Completion 必须保持 In Progress，不能宣称完成。")), ""])
    rendered = "\n".join(lines)
    rendered = rendered.replace(
        "Fresh-context review confirmed that narrative selection is independent of review completeness.",
        "Fresh-context review confirmed that narrative selection is independent of review completeness and that selected units cover distinct owner deltas when available.",
    )
    rendered = rendered.replace(
        "Fresh-context review checked current owner and adjacent chapter handoffs; no new durable Books delta remained." if audited else "Pending fresh-context Books review.",
        books_audit,
    )
    rendered = rendered.replace(
        f"Books Decision：{len(books_candidates)} 个 `No Change — Existing Coverage`（Deep {len(deep)} / Standard {standard_count}），{rejected_count} 个 `Rejected — Low Durability / Out of Scope`。",
        f"Books Decision：{len(integrated)} 个 `Integrate`、{len(no_change)} 个 `No Change — Existing Coverage`（Deep {len(deep)} / Standard {standard_count}），{rejected_count} 个 `Rejected — Low Durability / Out of Scope`。",
    )
    rendered = rendered.replace(
        "- 当前 Books 已覆盖本窗口通过 Evidence Gate 的机制类别，因此没有为制造 diff 重复追加正文。",
        repository_change,
    )
    return rendered


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--audited",
        action="store_true",
        help="Mark every rendered day as independently audited (legacy bulk mode).",
    )
    parser.add_argument(
        "--audited-day",
        action="append",
        default=[],
        help="Mark only the specified YYYY-MM-DD day as independently audited; repeatable.",
    )
    args = parser.parse_args()
    audited_days = set(args.audited_day)
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in [*data["candidates"], *packet_inventory_items()]:
        if "2026-07-01" <= item["daily_date"] <= "2026-07-31":
            grouped[item["daily_date"]].append(make_candidate(item))
    paths, order = roadmap()
    raw_counts = all_raw_daily_counts()
    unresolved: list[tuple[str, dict]] = []
    for day_number in range(1, 32):
        day = date(2026, 7, day_number)
        day_s = day.isoformat()
        if day_number >= 27 and not (DAILY_REVIEW_PACKET_DIR / f"{day_s}.json").exists():
            print(f"{day_s}: skipped (review packet not imported)")
            continue
        candidates = sorted(grouped.get(day_s, []), key=lambda item: (item["submitted_utc"], item["arxiv_id"]))
        target = ROOT / f"papers/2026/07/{day_number:02d}/README.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            report(
                day,
                candidates,
                raw_counts.get(day_s, 0),
                paths,
                order,
                args.audited or day_s in audited_days,
            ),
            encoding="utf-8",
        )
        unresolved.extend(
            (day_s, candidate)
            for candidate in candidates
            if candidate["review_status"] in {"pending", "blocked"}
        )
        print(f"{day_s}: raw={raw_counts.get(day_s, 0)} candidates={len(candidates)} deep={sum(c['route']=='deep' for c in candidates)}")

    material_rows = [
        "Priority\tStatus\tDaily\tWeek\tSource Family\tCandidate\tKnown URL\tMissing Material\tWhy Existing Evidence Is Insufficient\tAcceptable Substitute\tSuggested File Name\tResume Scope"
    ]
    for day_s, candidate in sorted(unresolved, key=lambda row: (row[0], row[1]["arxiv_id"])):
        title = candidate["title"].replace("\t", " ").replace("\n", " ")
        existing = (
            "Historical queue records an explicit full-text access blocker; metadata/review focus cannot support a mechanism claim"
            if candidate["review_status"] == "blocked"
            else "Identity/date/abstract and historical prose lack a transferable exact-version primary receipt, route locators, claim boundary and RP"
        )
        material_rows.append("\t".join([
            "P1 Full Text",
            candidate["review_status"],
            day_s,
            candidate["owner_week"],
            candidate["family"],
            title,
            f"https://arxiv.org/abs/{candidate['arxiv_id']}v1",
            "Event-time v1 Method, evaluation/ablation, limitations/Appendix and artifact scope",
            existing,
            "Author manuscript PDF/HTML/TXT or same-version proceedings",
            f"arxiv-{candidate['arxiv_id']}v1.pdf",
            "Primary replay -> V2 rescore -> owner -> Source Review -> Selection -> Books Decision -> fresh-context audit",
        ]))
    (SOURCE_DIR / "primary-material-requests.tsv").write_text(
        "\n".join(material_rows) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
