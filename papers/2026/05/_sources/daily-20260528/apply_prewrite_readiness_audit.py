#!/usr/bin/env python3
"""Apply the independent 2026-05-28 Books pre-write readiness decision."""

from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[4]
QUEUE_PATH = BASE / "books-writeback-queue-final.json"
AUDIT_PATH = BASE / "prewrite-readiness-audit.json"
MARKDOWN_PATH = BASE / "BOOKS_WRITEBACK_QUEUE-FINAL.md"
FRESH_AUDIT_PATH = BASE / "fresh-context-independent-audit.json"
COMPARISON_PATH = BASE / "books-current-content-comparison.json"
README_PATH = ROOT / "papers/2026/05/28/README.md"


def load(path: Path):
    return json.loads(path.read_text())


audit = load(AUDIT_PATH)
queue_doc = load(QUEUE_PATH)
decisions = {item["arxiv_id"]: item for item in audit["items"]}
old_items = {item["arxiv_id"]: item for item in queue_doc["items"]}

deltas = {
    "2605.27825": "Agent memory is a distinct privacy unit from training data or a static RAG corpus: correlated, compressed runtime memories can be probed repeatedly. Bind black/gray/white-box access, query-family identity, correlated-probe aggregation and parametric-prior confounding to the membership audit.",
    "2605.28053": "When generation mutates request-owned TTT state, batching correctness requires owner, version and READ/WRITE effect on every step; batch only compatible phases and commit each update only to its owning request.",
    "2605.28095": "For throughput-oriented offline inference, replace fully replicated DP weights with a layer-owned intra-node pool: stream weights to large-batch peers (WaS) or send small-tail activations to the owner (CaS), trading idle fabric bandwidth for HBM/KV capacity.",
    "2605.28201": "Prompt injection can persist through session context, memory or reusable skills and activate under a later benign query. Preserve write-time origin/taint and revalidate state at read/use time instead of treating interaction end as the security boundary.",
    "2605.28433": "Treat role self-modification as a versioned proposal: commit only if capability, communication, validation, aggregation and output-protocol contracts remain satisfied; otherwise retain the prior role/topology.",
    "2605.28617": "Typed recursive program holes let model-generated code shape agent control flow while whole-action type checking, capability bounds and reject-before-effect semantics keep the runtime authoritative; well-typed remains distinct from correct.",
    "2605.28632": "Watermark provenance depends on the integrity of the PRNG/seed path, not only output-side statistics. Version and attest entropy-source/PRNG state because seed-layer manipulation can preserve or amplify the watermark while evading content-side detectors.",
    "2605.28704": "Reduction order and bounded-ulp activation implementations are part of floating-point model semantics. Bind them with precision and kernel plan in the execution artifact; finite-domain representability does not establish deterministic outputs or deployment quality.",
    "2605.28760": "Zeroth-order fine-tuning is an optimizer alternative whose repeated perturbed forward scoring can be inference-dominated. The training owner retains perturbation, objective and update commit; a serving runtime may supply the forward executor without becoming the optimizer authority.",
    "2605.29082": "Carry tenant scope, policy signals and audit receipts on an infrastructure-owned out-of-band channel outside the agent read/write path; the agent proposes work, while control/evidence planes enforce and record authoritative transitions."
}

new_items = []
for arxiv_id, old in old_items.items():
    decision = decisions[arxiv_id]
    if decision["decision"] != "Integrate":
        continue
    item = dict(old)
    item["owner_node"] = decision["owner_node"]
    item["evolution_relation"] = decision["evolution_relation"]
    item["writeback_delta"] = deltas[arxiv_id]
    item["readiness_audit_ref"] = "prewrite-readiness-audit.json"
    if arxiv_id == "2605.28760":
        item["owner_path"] = "books/part-04-training-system/28-pretraining.md"
        item["adjacent_paths"] = [
            "books/part-04-training-system/27-data.md",
            "books/part-04-training-system/29-sft.md",
        ]
    new_items.append(item)

queue_doc["items"] = new_items
queue_doc["readiness_audit"] = {
    "input_queue": 17,
    "final_queue": len(new_items),
    "artifact": "prewrite-readiness-audit.json",
    "books_gate": "Open",
}
QUEUE_PATH.write_text(json.dumps(queue_doc, ensure_ascii=False, indent=2) + "\n")

lines = [
    "# 2026-05-28 Books Writeback Queue — Independent Final",
    "",
    "共享 Books 尚未修改；17 项 provisional queue 经 fresh-context readiness audit 后保留 10 项。",
    "",
    "| Source Family | Owner | Target | Relation | Durable delta |",
    "| --- | --- | --- | --- | --- |",
]
for item in new_items:
    lines.append(
        f"| {item['source_family_id']} | `{item['owner_node']}` | `{item['owner_path']}` | "
        f"{item['evolution_relation']} | {item['writeback_delta']} |"
    )
lines.extend(
    [
        "",
        "## Removed after current-Books challenge",
        "",
        "| Source Family | Final disposition | Reason |",
        "| --- | --- | --- |",
    ]
)
for decision in audit["items"]:
    if decision["decision"] == "Integrate":
        continue
    lines.append(
        f"| SF-2026-ARXIV-{decision['arxiv_id'].replace('.', '-')} | "
        f"{decision['decision']} | {decision['rationale']} |"
    )
MARKDOWN_PATH.write_text("\n".join(lines) + "\n")

fresh = load(FRESH_AUDIT_PATH)
fresh["books"] = {
    "provisional_integrate": 17,
    "final_integrate": len(new_items),
    "removed_after_readiness_audit": [
        item["arxiv_id"] for item in audit["items"] if item["decision"] != "Integrate"
    ],
    "owner_corrections": {
        "2605.28760": {
            "from": "TRAIN-LORA",
            "to": "TRAIN-PRETRAINING",
            "reason": "zeroth-order optimizer/runtime boundary is not a LoRA parameterization question",
        }
    },
    "final_queue": [item["arxiv_id"] for item in new_items],
    "gate": "Open",
    "next_condition": "root serial writeback followed by independent post-write semantic audit",
}
fresh["readiness_audit"] = "prewrite-readiness-audit.json"
fresh["resolution"] = (
    "Coverage and Evidence remain closed/passed. Fresh-context Books readiness reduced the "
    "provisional queue from 17 to 10 and corrected one owner; Books remains Open."
)
FRESH_AUDIT_PATH.write_text(json.dumps(fresh, ensure_ascii=False, indent=2) + "\n")

comparison = load(COMPARISON_PATH)
for item in comparison["items"]:
    arxiv_id = item["arxiv_id"]
    if arxiv_id not in decisions:
        continue
    decision = decisions[arxiv_id]
    item["decision"] = decision["decision"]
    item["evolution_relation"] = decision["evolution_relation"]
    item["existing_proposition"] = decision["rationale"]
    if decision["decision"] == "Integrate":
        item["new_evidence_delta"] = deltas[arxiv_id]
    if arxiv_id == "2605.28760":
        item["owner_node"] = "TRAIN-PRETRAINING"
        item["owner_path"] = "books/part-04-training-system/28-pretraining.md"
        item["adjacent_paths"] = [
            "books/part-04-training-system/27-data.md",
            "books/part-04-training-system/29-sft.md",
        ]
    owner_text = (ROOT / item["owner_path"]).read_text()
    item["owner_sha256"] = hashlib.sha256(owner_text.encode()).hexdigest()
    item["owner_sections_reviewed"] = re.findall(r"^##\s+(.+)$", owner_text, re.M)
    adjacent_sections = {}
    adjacent_hashes = {}
    for adjacent in item["adjacent_paths"]:
        adjacent_text = (ROOT / adjacent).read_text()
        adjacent_sections[adjacent] = re.findall(r"^##\s+(.+)$", adjacent_text, re.M)
        adjacent_hashes[adjacent] = hashlib.sha256(adjacent_text.encode()).hexdigest()
    item["adjacent_sections_reviewed"] = adjacent_sections
    item["adjacent_sha256"] = adjacent_hashes
    item["reviewer"] = "may2026-day03-fresh-context-readiness"
comparison["readiness_audit"] = {
    "artifact": "prewrite-readiness-audit.json",
    "provisional_integrate": 17,
    "final_integrate": len(new_items),
}
COMPARISON_PATH.write_text(json.dumps(comparison, ensure_ascii=False, indent=2) + "\n")

readme = README_PATH.read_text()
readme = readme.replace("root-writeback-ready Books queue=17", "root-writeback-ready Books queue=10")
readme = readme.replace("17 项已 current owner+adjacent compare", "10 项已通过 fresh-context current owner+adjacent readiness audit")
readme = readme.replace("Root 按日期序列串行写入 17 项 final Books queue。", "Root 按日期序列串行写入 10 项 independent final Books queue。")
readme = readme.replace("17 项 root queue 完成串行写回后", "10 项 independent final queue 完成串行写回后")
readme = readme.replace("与 17 项 root-writeback-ready queue", "与 10 项 root-writeback-ready queue")
readme = readme.replace("三项 Deep Analysis 与 17 项 root-writeback-ready queue", "三项 Deep Analysis 与 10 项 independent root-writeback-ready queue")

removed_ids = {item["arxiv_id"] for item in audit["items"] if item["decision"] != "Integrate"}
for arxiv_id in removed_ids:
    sfid = f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"
    pattern = re.compile(rf"(^\| {re.escape(sfid)} \|.*? \|) Integrate (\| books-review:{re.escape(sfid)} \| no \|$)", re.M)
    readme, n = pattern.subn(r"\1 No Change — Existing Coverage \2", readme)
    if n == 0 and f"| {sfid} |" in readme and "No Change — Existing Coverage | books-review:" + sfid in readme:
        n = 1
    if n != 1:
        raise RuntimeError(f"README candidate row update failed for {arxiv_id}: {n}")
    block = re.compile(
        rf"(<!-- delta:{re.escape(sfid)}:start -->.*?<!-- delta:{re.escape(sfid)}:end -->) Decision=`Integrate`",
        re.S,
    )
    readme, n = block.subn(r"\1 Decision=`No Change — Existing Coverage`", readme)
    if n == 0 and f"Decision=`No Change — Existing Coverage`" in readme:
        n = 1
    if n != 1:
        raise RuntimeError(f"README Books block update failed for {arxiv_id}: {n}")
    mapping = re.compile(
        rf"(^\| {re.escape(sfid)} \|.*? \|) Integrate (\| books-review:{re.escape(sfid)} \|$)",
        re.M,
    )
    readme, _ = mapping.subn(r"\1 No Change — Existing Coverage \2", readme)

sfid = "SF-2026-ARXIV-2605-28760"
pattern = re.compile(rf"(^\| {re.escape(sfid)} \|.*? \|) TRAIN-LORA (\| Integrate \|)", re.M)
readme, n = pattern.subn(r"\1 TRAIN-PRETRAINING \2", readme)
if n == 0 and "| SF-2026-ARXIV-2605-28760 |" in readme and "| TRAIN-PRETRAINING | Integrate |" in readme:
    n = 1
if n != 1:
    raise RuntimeError(f"README owner update failed for 2605.28760: {n}")
old_mapping = "| SF-2026-ARXIV-2605-28760 | TRAIN-LORA | books/part-04-training-system/30-lora.md#chapter-30 | books/part-04-training-system/29-sft.md#chapter-29;books/part-04-training-system/31-rlhf.md#chapter-31 |"
new_mapping = "| SF-2026-ARXIV-2605-28760 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 |"
readme = readme.replace(old_mapping, new_mapping)
readme = readme.replace(
    "已顺读 owner `books/part-04-training-system/30-lora.md` 的 17 个 H2 与相邻章节 ['books/part-04-training-system/29-sft.md', 'books/part-04-training-system/31-rlhf.md']；当前 owner 负责 `TRAIN-LORA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。",
    "已顺读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；zeroth-order fine-tuning 改变 optimizer/update runtime 而非 LoRA 参数化，最终 owner 纠正为 `TRAIN-PRETRAINING`。",
)

readme = readme.replace(
    "Fresh-context adversarial pass 复核了全部 747 identity 的 denominator 边界、112 项 exact-v1 claim boundary、Top-3 选择与 current Books owner；没有普通 pending。",
    "Fresh-context adversarial pass 复核了全部 747 identity 的 denominator 边界与 112 项 exact-v1 claim boundary；随后对 17 项 provisional Books queue 重读 exact-v1、current owner 与相邻章节，最终保留 10 项、降级 7 项，并将 2605.28760 从 TRAIN-LORA 纠正为 TRAIN-PRETRAINING；没有普通 pending。",
)
readme = readme.replace(
    "- 17 项 root queue 完成串行写回后，是否全部通过不同 reviewer 的 post-write audit？",
    "- 10 项 independent final queue 完成串行写回后，是否全部通过不同 reviewer 的 post-write audit？",
)
if "prewrite-readiness-audit.json" not in readme:
    readme = readme.replace(
        "## 10. Repository Changes",
        "## 10. Repository Changes\n\n- 新增 `prewrite-readiness-audit.json`，将 provisional Books queue 从 17 项收紧为 10 项；7 项改为 `No Change — Existing Coverage`，并纠正 2605.28760 的 owner。",
    )
README_PATH.write_text(readme)

print(json.dumps({"final_queue": len(new_items), "removed": 17 - len(new_items)}, ensure_ascii=False))
