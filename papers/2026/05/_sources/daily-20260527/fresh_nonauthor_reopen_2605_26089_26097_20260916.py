#!/usr/bin/env python3
"""Bounded fresh-review repair for two 2026-05-27 closure false negatives.

This script changes only the frozen 692-identity projection and its Daily
artifacts.  Shared Books files are deliberately left to root serialization.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/27/README.md"


def load(name: str):
    return json.loads((HERE / name).read_text())


def dump(name: str, value) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


REOPENED = {
    "2605.26089": {
        "source_family_id": "SF-2026-ARXIV-2605-26089",
        "title": "Channel-wise Vector Quantization",
        "proposition": (
            "视觉离散表示的 quantization axis 也是 representation contract：从局部 patch vector 改为覆盖整张特征图的 channel map，"
            "会把 token identity、序列长度和自回归顺序一起改写；channel 本身无天然顺序，必须由 nested dropout 学出可截断的 coarse-to-fine ordering。"
        ),
        "method": "§3.1 Channel-wise Vector Quantization; §3.2 Channel-wise Autoregressive Generation; Appendix B nested channel dropout",
        "evaluation": "§4.1–§4.3 reconstruction/generation, matched VQ comparisons, codebook/dropout ablations; Appendices C–E",
        "limitations": "§5 Future Works and Appendix D: image-only evidence, fixed/mapped spatial codeword shape, variable-resolution resampling, no video or unified understanding validation",
        "boundary": (
            "exact-v1 证明的是作者在 ImageNet reconstruction、披露的 text-to-image data/model 与 matched token-budget 实验中，"
            "channel-wise lookup 可提高 codebook utilization，nested dropout 可诱导所测 coarse-to-fine AR order；它不证明 channel token 天然有序、"
            "普遍优于 patch token，也不覆盖视频、统一理解、生产吞吐或跨分辨率无损迁移。ordering、resampler 或 generation quality 回归时应回退 patch/grid token、"
            "普通 VQ/1D tokenizer 或独立生成路径。"
        ),
        "score": {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8},
        "owner_node": "MULTIMODAL-REPRESENTATION",
        "owner_path": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
        "adjacent_paths": [
            "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
            "books/part-02-model/17-transformer.md",
        ],
        "existing": (
            "Ch23 已覆盖 patch/grid、离散 codebook、分层 residual 表示、codebook collapse、position-indexed capacity 与 rate–distortion，"
            "但没有把 quantization axis 从 spatial patch 改到 global channel 后的 token identity、无天然顺序及 learned ordering 写成替代分支。"
        ),
        "difference": (
            "新增的是 representation unit 与 generation factorization 的联动：channel codeword 携带整幅空间结构，nested dropout 才赋予 coarse-to-fine 顺序；"
            "收益、空间局部性损失、resampling 和回退必须在同一 contract 中表达。"
        ),
        "anchor": "### 离散表示",
        "proposed_delta": (
            "在 patch-wise VQ 后增加 channel-wise alternative：量化轴由每个空间位置的 feature vector 改成整幅 channel map；"
            "明确 channel 无天然顺序，nested dropout 只是学习 ordering 的机制，不能把作者 benchmark 写成通用优越性。"
        ),
        "trade_off": "更短的一维 channel sequence 与较高 codebook utilization，换取全局 codeword、learned ordering、resampling 和空间局部性治理成本。",
        "failure_mode": "ordering 未形成、resampler 漂移或全局 channel 混叠会让 coarse-to-fine 截断和生成同时失效。",
        "fallback": "回退 patch/grid VQ、普通 1D tokenizer、独立 diffusion decoder，或在不要求 AR ordering 时保留连续 feature。",
    },
    "2605.26097": {
        "source_family_id": "SF-2026-ARXIV-2605-26097",
        "title": "Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay",
        "proposition": (
            "continual SFT 的遗忘不是只靠减小 learning rate 就能解决：retention signal、剩余模型容量与优化速度共同决定可行域。"
            "冻结 reference model 的自生成样本加 token-level KL 可在有剩余容量时支持较高学习率，而容量接近饱和仍构成不可由 replay 消除的下界。"
        ),
        "method": "§2 self-generated replay and token-level KL; §3 capacity saturation; §4 learning-rate/compute trade-off; §5 instruction-tuned model case",
        "evaluation": "Figures 2–9: controlled English/Spanish/Depo studies, model-size/token sweeps, LR/replay wall-time study, Llama-3.2-1B-Instruct on Verilog",
        "limitations": "§7 Limitations: mostly one new task, majority models <=46M, only Figure 9 at 1B scale, capacity measured through proxies",
        "boundary": (
            "exact-v1 支持作者的 controlled language mixtures、单任务 fine-tuning 与 Llama-3.2-1B-Instruct/Verilog slice 中，"
            "frozen-reference self-generated replay + KL、剩余容量和 learning rate 共同影响遗忘；它不证明 BOS samples 覆盖真实 pretraining distribution，"
            "不覆盖多任务持续学习、frontier scale 或生产安全回归，也没有直接测量模型信息容量。replay distribution、retain slices 或容量 proxy 失效时，"
            "应回退可信 pretraining/domain replay、较低 LR、adapter/扩容或停止更新。"
        ),
        "score": {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8},
        "owner_node": "TRAIN-SFT",
        "owner_path": "books/part-04-training-system/29-sft.md",
        "adjacent_paths": [
            "books/part-04-training-system/28-pretraining.md",
            "books/part-04-training-system/30-lora.md",
        ],
        "existing": (
            "Ch29 已列出混入 pretraining/domain data、降低 update magnitude、adapter 与早停，并说明 trainable subspace 和 optimizer continuity 会改变遗忘；"
            "但未把 replay retention signal、capacity saturation 下界与 learning-rate/step compute trade-off 合成同一设计分支。"
        ),
        "difference": (
            "新增的是三变量边界：低 LR 只用更多 steps 换较少 drift；自生成 replay 可在有余量时解除速度—遗忘冲突；"
            "接近容量饱和时 replay 仍不能凭空创造可塑性。"
        ),
        "anchor": "## Catastrophic forgetting 与能力回退",
        "proposed_delta": (
            "在灾难性遗忘缓解列表后增加 retention signal × spare capacity × optimization speed 的联合判断；"
            "冻结 reference 的自生成 replay/KL 是无法访问原预训练数据时的条件分支，不是无条件自举，也不能越过容量下界。"
        ),
        "trade_off": "生成 replay、reference forward 与 KL 增加训练计算和 artifact lineage，换取较高 LR 下的旧分布约束。",
        "failure_mode": "BOS samples 不代表原分布、reference 已带偏差、容量已饱和或 retain slices 太窄时，会掩盖而非消除遗忘。",
        "fallback": "回退真实 pretraining/domain replay、降低 LR/早停、adapter/扩容，或拒绝继续吸收新任务。",
    },
}


screening = load("screening-outcomes-v3.json")
assert screening["raw_identity_count"] == 692
assert screening["retained_count"] == 92
found = set()
for item in screening["items"]:
    aid = item["arxiv_id"]
    if aid not in REOPENED:
        continue
    assert item["screening_status"] == "pre_denominator_closure"
    found.add(aid)
    item["screening_status"] = "retained"
    item["screening_reason"] = (
        "fresh non-author closure challenge reopened this family without expanding source/date scope: "
        + REOPENED[aid]["proposition"]
        + "；official exact-v1 HTML review bounded the claim and Books decision."
    )
assert found == set(REOPENED)
screening["retained_count"] = 94
screening["pre_denominator_closure_count"] = 598
screening["conservation"] = "692 = 94 retained + 598 pre-denominator closure + 0 withdrawn"
challenge = screening["false_positive_negative_challenge"]
challenge["retained_after_rebuild"] = 94
challenge["closure_count_after_challenge"] = 598
challenge["fresh_reviewer_reopened"] = sorted(set(challenge.get("fresh_reviewer_reopened", [])) | set(REOPENED))
dump("screening-outcomes-v3.json", screening)


evidence = load("evidence-review-v3.json")
assert evidence["count"] == 92
assert not ({item["arxiv_id"] for item in evidence["items"]} & set(REOPENED))
for aid, spec in REOPENED.items():
    evidence["items"].append({
        "arxiv_id": aid,
        "source_family_id": spec["source_family_id"],
        "title": spec["title"],
        "primary_evidence_version": f"arXiv:{aid}v1",
        "retrieval_route": "official arXiv exact-v1 HTML",
        "method_locator": spec["method"],
        "evaluation_locator": spec["evaluation"],
        "limitations_locator": spec["limitations"],
        "claim_boundary": spec["boundary"],
        "adopted_proposition": spec["proposition"],
        "score": spec["score"],
        "review_depth": "deep",
        "completion_result": "complete",
        "owner_node": spec["owner_node"],
        "books_decision": "Integrate",
        "evidence_reuse_basis": "fresh non-author reopened a frozen-corpus closure and reviewed official exact-v1 HTML",
    })
evidence["items"].sort(key=lambda item: item["arxiv_id"])
evidence["count"] = 94
evidence["deep_complete_count"] = 94
evidence["score_distribution"] = {"7": 22, "8": 62, "9": 10}
dump("evidence-review-v3.json", evidence)
dump("exact-v1-review-packet.json", {
    "schema": "daily-exact-v1-review-packet-v3",
    "report_date": "2026-05-27",
    "items": evidence["items"],
})


books = load("books-comparison-v3.json")
assert books["count"] == 92
assert not ({item["arxiv_id"] for item in books["items"]} & set(REOPENED))
for aid, spec in REOPENED.items():
    books["items"].append({
        "arxiv_id": aid,
        "source_family_id": spec["source_family_id"],
        "owner_node": spec["owner_node"],
        "owner_path": spec["owner_path"],
        "adjacent_paths": spec["adjacent_paths"],
        "adopted_proposition": spec["proposition"],
        "existing_proposition": spec["existing"],
        "coverage_anchor": spec["anchor"],
        "coverage_difference": spec["difference"],
        "evidence_boundary": spec["boundary"],
        "decision": "Integrate",
        "binding_marker": None,
        "author_check": "Fresh reviewer found a durable delta absent from current main body; root serialized writeback and a new fresh semantic review are required.",
    })
books["items"].sort(key=lambda item: item["arxiv_id"])
books["count"] = 94
books["pending_integrate_count"] = 2
dump("books-comparison-v3.json", books)
dump("books-current-content-comparison.json", books)


queue = load("root-books-writeback-queue-v3.json")
assert queue["pending_count"] == 0
assert not ({item["arxiv_id"] for item in queue["items"]} & set(REOPENED))
for aid, spec in REOPENED.items():
    queue["items"].append({
        "arxiv_id": aid,
        "source_family_id": spec["source_family_id"],
        "owner": "root",
        "owner_node": spec["owner_node"],
        "target_path": spec["owner_path"],
        "unique_anchor": spec["anchor"],
        "adopted_proposition": spec["proposition"],
        "proposed_delta": spec["proposed_delta"],
        "evidence_boundary": spec["boundary"],
        "trade_off": spec["trade_off"],
        "failure_mode": spec["failure_mode"],
        "fallback": spec["fallback"],
        "exact_v1_locators": {
            "method": spec["method"],
            "evaluation": spec["evaluation"],
            "limitations": spec["limitations"],
        },
        "status": "pending_root_serialized_writeback",
    })
queue["items"].sort(key=lambda item: item["arxiv_id"])
queue["status"] = "two bounded root writebacks pending; then new fresh non-author review"
queue["pending_count"] = 2
queue["note"] = (
    "Earlier bindings remain applied_pending_fresh_review. Fresh closure challenge reopened 2605.26089 and 2605.26097; "
    "only these two bounded shared-Books writes are pending."
)
dump("root-books-writeback-queue-v3.json", queue)


coverage = load("source-coverage-v3.json")
for source in coverage["sources"]:
    if source["source_id"] == "SRC-ARXIV":
        source["limitation"] = "691 arXiv raw = 93 retained + 598 closure"
dump("source-coverage-v3.json", coverage)


audit = load("author-adversarial-audit-v3.json")
audit["status"] = "fresh_review_found_two_closure_false_negatives_pending_root_writeback_and_new_fresh_review"
audit["challenges"]["false_negative"] = (
    "Fresh challenge additionally reopened 2605.26089 and 2605.26097 from the frozen closure partition; no source/date expansion occurred."
)
audit["challenges"]["evidence"] = "94 exact-v1/page records have method, evaluation and limitations/counterevidence locators"
audit["challenges"]["books"] = "59 Applied + 33 No Change + 2 bounded Integrate pending root writeback"
audit["gates"]["candidate_denominator"] = "BOUNDED_REPAIR_APPLIED_PENDING_NEW_FRESH_REVIEW"
audit["gates"]["evidence"] = "BOUNDED_REPAIR_APPLIED_PENDING_NEW_FRESH_REVIEW"
audit["gates"]["books"] = "TWO_BOUNDED_ROOT_WRITEBACKS_PENDING"
audit["gates"]["fresh_non_author"] = "REPAIR_AUTHOR_CANNOT_SELF_SIGN"
dump("author-adversarial-audit-v3.json", audit)


table_rows = """| [2605.26089 Channel-wise Vector Quantization](https://arxiv.org/html/2605.26089v1) | 2026-05-27T08:00:00+08:00 | 视觉离散表示的 quantization axis 也是 representation contract：patch vector 改为 global channel map 后，token identity、序列长度与 AR ordering 一起变化；3+2+3=8 | 深入完成 | 待 root 串行整合：[章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：MULTIMODAL-REPRESENTATION |
| [2605.26097 Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay](https://arxiv.org/html/2605.26097v1) | 2026-05-27T08:00:00+08:00 | retention signal、剩余容量与优化速度共同决定 continual SFT 的遗忘边界；自生成 replay 不能越过容量下界；3+2+3=8 | 深入完成 | 待 root 串行整合：[章节](../../../../books/part-04-training-system/29-sft.md)：TRAIN-SFT |
"""

deep_sections = """### [2605.26089 Channel-wise Vector Quantization](https://arxiv.org/html/2605.26089v1)

- **为什么进入 denominator：** 它改变视觉 token 的基本量化轴，使 representation identity、序列 factorization 与生成顺序成为同一个系统合同，而非单一任务精度增量。
- **方法定位：** §3.1 Channel-wise Vector Quantization；§3.2 Channel-wise Autoregressive Generation；Appendix B nested channel dropout。
- **评价定位：** §4.1–§4.3 reconstruction/generation、matched VQ comparisons、codebook/dropout ablations；Appendices C–E。
- **限制/反证：** §5 与 Appendix D 只给 image 设置；channel 没有天然顺序，variable resolution 依赖额外 resampling，视频和统一理解仍未证明。
- **证据边界与回退：** exact-v1 只支持作者披露数据、模型和 matched token-budget；不能宣称 channel token 普遍优于 patch token。ordering、resampler 或 generation quality 回归时回退 patch/grid VQ、普通 1D tokenizer 或独立生成路径。
- **Books：** `Integrate`；owner=`MULTIMODAL-REPRESENTATION` / Ch23；等待 root 串行写入后由另一 fresh reviewer 验收。

### [2605.26097 Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay](https://arxiv.org/html/2605.26097v1)

- **为什么进入 denominator：** 它把 continual SFT 的 retention signal、剩余容量与 learning-rate/step compute 放进同一可证伪设计边界，修正“只要降低 LR 或加 replay 就能防遗忘”的过度简化。
- **方法定位：** §2 self-generated replay/KL；§3 capacity saturation；§4 LR/compute trade-off；§5 instruction-tuned case。
- **评价定位：** Figures 2–9 的 controlled mixtures、容量/LR sweeps 与 Llama-3.2-1B-Instruct/Verilog slice。
- **限制/反证：** §7 明确多数实验 ≤46M、主要为一个新任务，只有 Figure 9 达 1B；capacity 只由 proxy 间接测量。
- **证据边界与回退：** exact-v1 不证明 BOS samples 覆盖真实 pretraining distribution，也不覆盖多任务、frontier scale 或生产安全回归。retain slices、replay distribution 或容量 proxy 失效时，回退真实 replay、低 LR/早停、adapter/扩容或停止更新。
- **Books：** `Integrate`；owner=`TRAIN-SFT` / Ch29；等待 root 串行写入后由另一 fresh reviewer 验收。

"""

text = REPORT.read_text()
replacements = {
    "692 = 92 retained + 600 pre-denominator closure + 0 withdrawn": "692 = 94 retained + 598 pre-denominator closure + 0 withdrawn",
    "92 项均完成 exact-v1/官方技术页深入审阅": "94 项均完成 exact-v1/官方技术页深入审阅",
    "92 deep + 0 standard + 0 blocked": "94 deep + 0 standard + 0 blocked",
    "22 score7 + 60 score8 + 10 score9": "22 score7 + 62 score8 + 10 score9",
    "59 Applied + 33 No Change + 0 pending Integrate": "59 Applied + 33 No Change + 2 pending Integrate",
    "691 arXiv raw = 91 retained + 600 closure": "691 arXiv raw = 93 retained + 598 closure",
    "Fresh 终审只重开 `2605.26099`，没有扩窗或扩源。": "Fresh 终审在冻结分母内又重开 `2605.26089` 与 `2605.26097`，没有扩窗或扩源。",
}
for old, new in replacements.items():
    assert old in text, old
    text = text.replace(old, new)

table_anchor = "| [2605.26099 Language Models Need Sleep](https://arxiv.org/html/2605.26099v1)"
assert text.count(table_anchor) == 1
text = text.replace(table_anchor, table_rows + table_anchor)

section_anchor = "### [2605.26099 Language Models Need Sleep](https://arxiv.org/html/2605.26099v1)"
assert text.count(section_anchor) == 1
text = text.replace(section_anchor, deep_sections + section_anchor)

gap_start = text.index("## 5. 缺口与下一步")
review_start = text.index("## 6. 复核", gap_start)
text = text[:gap_start] + """## 5. 缺口与下一步

Evidence 无 access blocker。fresh closure challenge 在冻结 692 owner corpus 内追加恢复 `2605.26089` 与 `2605.26097`，没有扩日期或来源；两项 exact-v1 已完成，但都形成真实 Books delta，root queue 因而有 2 个串行写入 pending。此前 `2605.26099` 的 Ch22 paired marker 已覆盖完整命题，并明确区分论文支持与项目对 atomic commit/recovery 的系统推导，本轮复核通过。Meta 与 MiMo 的来源级限制保持隔离，不参与正面 no-hit 断言。

""" + text[review_start:]

review_start = text.index("## 6. 复核")
text = text[:review_start] + """## 6. 复核

- **复核者：** fresh non-author；未参与此前 denominator/Evidence rebuild 或 root Books 写回。
- **结论：** 未通过最终 Gate。Ch22 的 `2605.26099` exact-v1、paired marker、证据/推导边界、trade-off、failure 与 fallback 均通过；但 598 closure 挑战发现 `2605.26089`、`2605.26097` 两个高置信 false negative，已做有界恢复。
- **当前账目：** `692=94 retained+598 closure`；`94 deep`；`59 Applied + 33 No Change + 2 pending Integrate`；root queue=`2 pending`。
- **独立性边界：** 本 reviewer 已修改被审对象，不能自签 Complete。root 只需按 queue 串行写 Ch23/Ch29；完成后必须由另一 fresh non-author 验证两处正文 binding、canonical 投影与本日全部 Gate。
- **收据：** [`FRESH_NONAUTHOR_V3_BOUNDED_FAIL_2605_26089_26097_20260916.md`](../_sources/daily-20260527/FRESH_NONAUTHOR_V3_BOUNDED_FAIL_2605_26089_26097_20260916.md)。
"""
REPORT.write_text(text)


receipt = HERE / "FRESH_NONAUTHOR_V3_BOUNDED_FAIL_2605_26089_26097_20260916.md"
receipt.write_text("""# 2026-05-27 Fresh Non-Author Bounded Failure Receipt

## Scope

Only the frozen 692 identities, 92 existing deep reviews, 59 Applied bindings, 33 No Change decisions, and the exact-v1/Ch22 binding for `2605.26099` were reviewed. No source or date window was expanded.

## Result

- `2605.26099 Language Models Need Sleep`: PASS. The paired Ch22 marker covers the whole adopted mechanism, bounds exact-v1 evidence, and labels atomic commit/recovery as project inference rather than paper fact.
- `2605.26089 Channel-wise Vector Quantization`: closure false negative. Exact-v1 changes representation unit, artifact identity and AR factorization; restored as score 8 and `Integrate` to `MULTIMODAL-REPRESENTATION`.
- `2605.26097 Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay`: closure false negative. Exact-v1 joins retention signal, capacity lower bound and LR/compute trade-off; restored as score 8 and `Integrate` to `TRAIN-SFT`.

## Projection

`692 = 94 retained + 598 closure`; Evidence=`94 deep`; Books=`59 Applied + 33 No Change + 2 pending Integrate`; root queue=`2 pending`.

## Gate

FAIL / repair pending. This reviewer modified the audited artifacts and therefore cannot self-sign Complete. Root must serialize the two Books writes; a different fresh non-author must then verify the bindings and canonical projection.
""")

print("bounded repair prepared: 94 candidates, two root Books writes pending")
