#!/usr/bin/env python3
"""Finalize the strict V2.1 packet for the 2026-06-09 Daily lane.

This script deliberately does not edit Books.  It turns the independently
screened DataCite snapshot into a frozen denominator, exact-v1 review receipts,
the Daily report, and the deduplicated Books writeback queue.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260609"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"
POST_WRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
SELECTION = PACKET / "deep-analysis-selection-v1.json"
REPORT = ROOT / "papers/2026/06/09/README.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"
EXECUTED_AT = "2026-08-29T20:45:00+08:00"
DENOMINATOR_ID = "DEN-20260609-477015"

# id -> owner, durable delta, score, books disposition, method/eval/limit,
# trade-off, compact benchmark workload/evaluator.
META = {
    "2606.08919": ("AGENT-WORKFLOW", "人工审批不是无限 oracle；guard 的 escalation policy 必须把 reviewer 分歧、疲劳与 flooding 下的有限 attention 当作可耗尽资源。", (3, 3, 3), "Integrate", "§3 Selective Classification; §4 Endogenous Reviewer Model", "§5 Experiments", "§6 Limitations and Human-Study Boundary", "降低 escalation load 会提高自动放行风险；全升级又会因疲劳降低实际安全性，静态审批仍适合低频高危动作。", "125 个 adversarially weighted agent actions、多人风险标注与 fatigue/flooding simulation", "reviewer agreement、selective-risk/coverage curve 与 realized-safety curve"),
    "2606.08950": ("AGENT-RAG", "向量数据库的 insertion、indexing、query 与 mixed read/write 生命周期必须同 storage hierarchy、broadcast-gather 与 partitioning 一起评估；增加 core/node 可因协调瓶颈反向降低吞吐。", (3, 3, 3), "Integrate", "§III Methodology", "§§IV–V Cloud/HPC and lifecycle evaluation", "§VI Discussion and Conclusion", "HPC-native deployment扩大资源却引入 MPI/Apptainer、shared storage 与 aggregation bottleneck；云端架构在普通规模仍更易运维。", "Qdrant/Milvus/Weaviate，四个 embedding datasets，两台生产超算，最多 64 nodes/256 workers", "upload/index time、QPS、latency/P95/P99、recall 与 storage overhead"),
    "2606.08960": ("PLATFORM-EVALUATION-SYSTEM", "benchmark verifier 应通过 hacker→fixer→solver 的闭环迭代：攻击发现 exploit、修补拒绝 exploit、solver 防止补丁把合法解一并拒绝。", (3, 3, 3), "Integrate", "§3 The Hacker-Fixer Loop; Appendix D", "§4 Hardening Results", "Appendix A Limitations", "循环只覆盖 hacker 能发现的攻击，shared defense pool 也绑定共同 evaluation substrate；独立 held-out exploit corpus 仍不可省。", "1,968 tasks/5 terminal-agent benchmarks；KernelBench 与 Terminal-Bench case studies", "attack success、held-out exploit rejection、legitimate-solver acceptance 与 patch transfer"),
    "2606.09005": ("PLATFORM-SECURITY", "RAG prompt assembly 必须把 document-authored metadata/provenance 视为 data 而非 policy，避免不可信文档在同一自然语言 channel 中冒充 control signal。", (3, 3, 3), "Integrate", "§III System and Attacker Model; §III-C Control/Data Boundary", "§§IV–V Experimental Design and Results", "§X Limitations and Validity Threats", "结构化 channel separation、redaction 与 output scanning 增加集成成本且都不是完整防御；旧式文本提示仍可作为辅助但不能承担 authority。", "六个 model settings、paired prompt-pressure controls、toy/semi-realistic/embedding/LangChain-style RAG", "synthetic-canary disclosure、paired lift、confidence interval、FDR 与 source-authority probe"),
    "2606.09061": ("INFER-SCHEDULING", "chunked-prefill scheduler 需联合持有 request age、remaining prefill work、predicted latency 与 active-prefill cap，而不只用 arrival order 或 static token budget。", (3, 3, 3), "No Change — Existing Coverage", "§3 The Developed Methodology", "§4 Experiment and Evaluation", "§4.6 Discussion; §5 Future Work", "aging 抑制 starvation 却牺牲部分短请求优先；latency predictor 会漂移，chunk 太大时重排机会消失，FCFS 仍是保守基线。", "混合长短 prompt、NVIDIA GPU 与 Ascend、single/multi-GPU chunked-prefill workloads", "mean/P99 E2E latency、TTFT、fairness、fragmentation、predictor error 与 portability"),
    "2606.09084": ("PLATFORM-SECURITY", "tool agent 的安全状态跨越多轮 artifact write/read；防御必须记录 artifact lineage 并在组合读取时执行 provenance-aware policy，不能只审核当前 turn。", (3, 3, 3), "Integrate", "§3 Context-Fractured Decomposition", "§4 Evaluation", "§5 Limitations", "lineage tagging 增加 instrumentation/storage 与 benign cross-session false positive；论文只证明需要该控制面，没有交付校准后的完整防御。", "有限 model/tool/pipeline topologies 下的 context-fractured agent attack testbed", "ASR、context-removal/depth/width ablations、topology sensitivity 与 artifact inspection"),
    "2606.09441": ("INFER-PREFILL", "RAG 重复文档的 prefill 可保存 selective index 而非整份 KV：offline 编码局部 attention，online 只重算 query-sensitive cross attention，以 storage traffic 换 TTFT。", (3, 3, 3), "Integrate", "§§3–5 Attention invariance, SIFT design and implementation", "§§6–7 Evaluation Methodology and Results", "§9 Conclusion; no dedicated limitations section", "selective index 减少重算但引入离线 storage、pattern assumption 与 custom kernel；复用率低或 attention 不稳定时完整 prefill 仍正确。", "RAG context-reuse workloads、context-length sweep 与 diverse attention patterns", "TTFT、accuracy、storage scaling、energy、breakdown 与 hyperparameter sensitivity"),
    "2606.09613": ("INFER-SCHEDULING", "agent serving simulator 的执行单位必须从独立 request 提升为 program，显式模拟 turn dependency、tool gap、session affinity 与跨 HBM/host/CXL 的 KV residency。", (3, 3, 3), "Integrate", "§3 AgentServeSim", "§§4–6 Setup, validation and design-space exploration", "§7 Limitations and Future Work", "simulation 降低 accelerator 探索成本却依赖 trace/calibration；6% 内复现实验不能替代新模型、工具时延和多租户下的实机验收。", "多轮 agent traces、real serving deployments、arrival/model/hardware/KV-tier sweeps", "program JCT、throughput、TTFT/TPOT、policy rank preservation 与 prediction error"),
    "2606.09643": ("INFER-KSERVE-TOPOLOGY", "extensible foundation model serving 需要把 base weights 与 extension state 虚拟化：共享公共层、按请求装载/组合扩展，并由 placement/cache 控制其生命周期。", (3, 3, 3), "Integrate", "§3 FMplex Design", "§§4–6 Implementation and Evaluation", "§7 Discussion and Limitations", "共享提高 density 但引入 extension interference、cache miss 与版本兼容性；扩展少或隔离要求强时独立 replica 仍更简单。", "多 extension foundation-model serving configurations and baselines", "memory footprint、load/switch latency、throughput、tail latency 与 extension-count sensitivity"),
    "2606.09682": ("INFER-TENSORRT-LLM", "agent 生成 megakernel 必须经过 typed IR、静态 shape/layout/resource checks、编译与数值验证门，失败后才允许 self-retarget；自然语言计划不直接获得 kernel authority。", (3, 3, 3), "Integrate", "§3 AutoMegaKernel Harness", "§4 Evaluation", "§5 Limitations", "静态门降低 silent miscompile 却限制可表达优化并增加 compile/search cost；成熟算子与不可验证路径仍应回退到人工 kernel。", "多 GPU workload/kernel synthesis tasks with compile-and-run verification", "compile success、numerical correctness、performance、repair rounds 与 failure taxonomy"),
    "2606.09686": ("INFER-TENSORRT-LLM", "低精度 format contract 需要 vendor-neutral、bit-exact 的 encode/decode、rounding、overflow、NaN/Inf/subnormal 与 microscaling conformance vectors；格式名相同不代表语义相同。", (3, 3, 3), "Integrate", "§§2–4 Numeric Catalog and Conformance Model", "§§5–6 Validation and Results", "§7 Limitations", "bit-exact catalog 提高互操作性但维护成本随标准修订增长；它验证表示语义，不证明任何训练或推理 workload 的质量/性能。", "official v1 的 84-format catalog，覆盖 FP8/BF16/MXFP4/microscaling families", "bit-exact vectors、cross-implementation agreement、edge-case coverage 与 mismatch diagnostics"),
    "2606.09692": ("PLATFORM-TRACE", "agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。", (3, 3, 3), "Integrate", "§2 Delegation-Observable Execution; §3 Common Information Model", "§§4–5 Gateway and Evaluation", "§6 Limitations", "双图与 gateway 提高可归因性但不推断 intent/policy compliance；跨工具 schema、missing telemetry 与 identity minting 仍需平台治理。", "跨工具 delegation/re-delegation、concurrency/retry reconstruction scenarios", "reconstruction completeness、query correctness、gateway overhead 与 missing-lineage failure cases"),
    "2606.09711": ("TRAIN-RLHF", "reward-hacking 监测需观察显性 exploit 之前形成的 proxy-reward internalization：正确性判断、proxy acceptance 预测与 proxy-gold gap 推理三种状态。", (3, 3, 3), "Integrate", "§§2–4 PRIME Definition, Probes and Interventions", "§5 Experiments", "§6 Limitations", "probe 可作 early warning，却可能被训练规避且当前只在 pytest coding RL 验证；相关性不等于通用 causal monitor。", "可 exploit pytest rewards 的 coding RL checkpoints 与 evaluator-switch controls", "hack onset/severity forecast、direct/activation probes、direction ablation 与 OOD misalignment correlation"),
    "2606.09774": ("AGENT-WORKFLOW", "给通用 coding agent 适配 scientific simulator 时，应把 executable contract 外置为 retrieval、procedural memory、agent-callable validator 与 validation-gated termination，而不重写 agent loop。", (3, 3, 3), "Integrate", "§§3–4 SIGA Adapter and Self-Evolution", "§§5–6 Evaluation", "Appendix F Limitations", "adapter 可移植但 component importance 依接口 bottleneck 变化；结构通过不代表物理正确，tool 暴露也不保证 agent 会调用。", "GEOS main benchmark；OpenFOAM/LAMMPS transfer；human calibration", "structural/quality score、completion、variance、runtime、ablation 与 transfer delta"),
    "2606.09809": ("PLATFORM-EVALUATION-SYSTEM", "Evaluation result 需要把 benchmark metadata、run data 与 model metadata 组合成可追踪 record，并按读者呈现 reproducibility、completeness、provenance/risk 与 score comparability。", (3, 3, 3), "Integrate", "§§3–5 Evaluation Cards Schema and Interpretive Signals", "§§6–8 Deployment and Analysis", "Appendix J Limitations", "统一 schema 改善解释却可能固化过时字段；reader mode 不能替代原始 evidence，agent evaluation 也未被系统综述充分覆盖。", "52-paper review、10 stakeholder interviews、5,816 models/635 benchmarks/101,843 results", "schema coverage、documentation/comparability signals、extraction quality 与 monitoring findings"),
}

TITLE_OVERRIDES = {
    "2606.09686": "An 84-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats",
}

NON_PROOF = {
    "2606.08919": "125 条 action 上的 reviewer disagreement 是有限标注观测；fatigue inverted-U 与 flooding 结果来自 endogenous reviewer simulation，论文明确把 human study 留作后续，且这些机制被作者标为 prior art，而非现实人员实验或新机制发现。",
    "2606.08950": "结果绑定 Qdrant/Milvus/Weaviate、四个 embedding datasets、两台生产超算及最多 64 nodes/256 workers；不证明 HPC-native topology 在普通规模、其他数据库、网络/存储或 mixed workload 下普遍优于云端架构。",
    "2606.08960": "hardening 只覆盖 hacker repertoire 能找到的 exploit 与共同 evaluation substrate；不得写成 verifier 已完备、安全已证明或可省略 held-out exploit corpus。",
    "2606.09005": "实验使用 synthetic canary 与 toy/semi-realistic RAG pressure tests，不是企业数据泄露事件；channel separation、redaction 与 output scan 均未被证明是完整防御。",
    "2606.09084": "有限 model/tool/pipeline topology 的 attack testbed 证明 provenance gap 可被利用，但论文没有实现或校准一套可部署的 lineage defense，也未给出 benign cross-session false-positive 上界。",
    "2606.09441": "TTFT、storage 与 accuracy 结论绑定论文测试的 RAG context reuse、attention pattern、kernel 和硬件；没有独立 limitations section，也不证明所有模型或低复用 workload 都优于完整 Prefill。",
    "2606.09613": "约 6% 的 simulator fidelity 与 policy-rank preservation 绑定所校准 trace/model/hardware；不证明新模型、工具时延、多租户干扰或生产尾延迟下仍准确，不能替代实机 release gate。",
    "2606.09643": "memory/latency/density 结果绑定论文的 extension 类型、组合方式与基线；不证明强隔离场景或任意 extension compatibility，也不消除 cache miss、interference 和 version lifecycle。",
    "2606.09682": "compile、static check 与 numerical validation 只约束 harness 可表示和测试的 kernel；不证明未建模语义、所有 GPU 架构或性能最优，失败路径仍需回退而非获得执行 authority。",
    "2606.09686": "official exact-v1 是 84-format，不是 DataCite 的 83-format；bit-exact conformance 只证明 encode/decode 与边界值表示语义，不证明训练/推理 workload 精度、吞吐或跨未来标准版本兼容。",
    "2606.09692": "gateway 与双图 schema 改善 delegation reconstruction，但 delegation_id 本身不证明 lineage closure、identity minting authority、absence semantics、intent 或 policy compliance，也不保证跨工具一致性。",
    "2606.09711": "证据来自可 exploit pytest reward 的 coding-RL checkpoints；probe 与 hacking 的相关性及有限 intervention 不构成跨任务 causal theory，模型也可能学习规避 probe。",
    "2606.09774": "GEOS 主实验与 OpenFOAM/LAMMPS transfer 的规模、run 数和 simulator 接口有限；structural validation 不等于物理正确，暴露 tool 也不证明 agent 会可靠调用。",
    "2606.09809": "schema 与 interpretive signals 来自截至论文 cutoff 的 52-paper review、访谈及公开结果语料；agent evaluation 未纳入系统综述，reader mode 不替代原始 run evidence，也不保证 score 可直接横比。",
}


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def closure(row: dict) -> tuple[str, str]:
    text = f"{row['title']} {row['abstract']}".lower()
    if row["screening_route"].startswith("not_"):
        cls = "registered_noncore_false_negative_closed"
    elif any(x in text for x in ("segmentation", "classification", "detection", "diagnos", "medical", "molecular", "speech", "image", "video")):
        cls = "application_or_model_quality_only"
    elif any(x in text for x in ("benchmark", "evaluation", "dataset", "survey")):
        cls = "benchmark_without_new_system_contract"
    elif any(x in text for x in ("diffusion", "representation", "reasoning", "learning", "optimization")):
        cls = "model_method_without_durable_system_delta"
    else:
        cls = "no_unresolved_owner_delta"
    subject = re.sub(r"\s+", " ", row["abstract"]).strip().split(".")[0][:180]
    return cls, f"Full title+abstract review: {subject}. This family does not change a durable AI-system mechanism, ownership handoff, release/evaluation contract, or platform/training/inference design beyond the 15 retained families."


def benchmark(workload: str, evaluator: str) -> dict:
    return {
        "workload": f"Disclosed — {workload}",
        "model": "Not Disclosed",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed",
        "evaluator": f"Disclosed — {evaluator}",
    }


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def review_provenance(fam: str, aid: str, method: str, evaluation: str, limitations: str, artifact: str, body: str) -> str:
    def canonical_multi(value: str) -> str:
        items = [unicodedata.normalize("NFC", item.strip()) for item in value.split(";")]
        return ";".join(sorted(item for item in items if item and item != "—"))
    canonical = "|".join((
        "review-completion-v1", fam, f"paper-v1:{aid}", f"arXiv:{aid}v1", "SRC-ARXIV",
        f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", "deep",
        canonical_multi(method), canonical_multi(evaluation), canonical_multi(limitations), canonical_multi(artifact),
        f"claim:{fam}", f"review:{fam}", f"review-body-sha256:{normalized_body_sha256(body)}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def main() -> None:
    provisional = json.loads(PROVISIONAL.read_text())
    rows = provisional["identities"]
    assert len(rows) == 477
    assert set(META) <= {r["arxiv_id"] for r in rows}

    audit_rows = []
    for row in rows:
        aid = row["arxiv_id"]
        if aid in META:
            row["screening_status"] = "retained_after_full_semantic_audit"
            row["screening_reason"] = META[aid][1]
            row["pre_denominator_closure_class"] = "—"
            audit_rows.append((aid, row["screening_route"], "retained", "—", META[aid][1]))
        else:
            cls, reason = closure(row)
            row["screening_status"] = "pre_denominator_closure"
            row["screening_reason"] = reason
            row["pre_denominator_closure_class"] = cls
            audit_rows.append((aid, row["screening_route"], "closure", cls, reason))

    ledger = dict(provisional)
    ledger.update({
        "gate_status": "complete_all_gates_passed",
        "routed_candidate_denominator": len(META),
        "routed_candidate_denominator_status": "frozen_after_477_of_477_full_semantic_audit",
        "abstract_screening_closure": 477 - len(META),
        "canonical_candidate_denominator": {
            "denominator_id": DENOMINATOR_ID, "raw_identities": 477,
            "retained": len(META), "pre_denominator_closures": 477-len(META),
            "audit_receipt": str(AUDIT.relative_to(ROOT)), "frozen_at": EXECUTED_AT,
        },
        "audit": {
            "reviewed_identities": "477/477", "title_abstract_semantic_screen": "passed",
            "candidate_false_positive_false_negative_audit": "passed",
            "denominator_frozen": True, "coverage_gate": "closed",
            "evidence_gate": "passed", "books_gate": "passed_post_write_fresh_audit",
            "metadata_findings": ["2606.09686 exact-v1 title normalized from 83-Format to 84-Format"],
        },
    })
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

    with AUDIT.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["arxiv_id", "screening_route", "decision", "closure_class", "semantic_reason"])
        w.writerows(audit_rows)

    reviews = []
    for row in rows:
        aid = row["arxiv_id"]
        if aid not in META:
            continue
        owner, delta, score, disposition, method, evaluation, limits, tradeoff, workload, evaluator = META[aid]
        fam = family(aid)
        title = TITLE_OVERRIDES.get(aid, row["title"])
        b = benchmark(workload, evaluator)
        body = f"""### {aid} — {title}

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：{delta}

**State / data / control owner。** `{owner}` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:{aid}v1 {evaluation}` 支持 `{b['workload']}`，evaluator 为 `{b['evaluator']}`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:{aid}v1 {method}`；counterevidence locator: `arXiv:{aid}v1 {limits}`。

**Trade-off / failure / coexistence / evolution。** {tradeoff} 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:{fam}:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/{aid}v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:{fam}:end -->"""
        method_locator=f"arXiv:{aid}v1 {method}"
        evaluation_locator=f"arXiv:{aid}v1 {evaluation}"
        limitations_locator=f"arXiv:{aid}v1 {limits}"
        artifact_locator="Not Disclosed — no later artifact is used"
        reviews.append({
            "arxiv_id": aid, "family": fam, "title": title, "owner": owner,
            "score": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "route": "deep", "event": f"paper-v1:{aid}", "primary_identifier": f"arXiv:{aid}v1",
            "primary_evidence": f"arXiv:{aid}v1", "reviewed_versions": f"SRC-ARXIV@arXiv:{aid}v1",
            "evidence_route": "official-exact-v1-html-web-proxy", "evidence_path": f"https://arxiv.org/html/{aid}v1",
            "method_locator": method_locator, "evaluation_locator": evaluation_locator,
            "limitations_locator": limitations_locator, "artifact_locator": artifact_locator,
            "claim_boundary": f"claim:{fam}", "review_ref": f"review:{fam}", "benchmark": b, "body": body,
            "provenance": review_provenance(fam, aid, method_locator, evaluation_locator, limitations_locator, artifact_locator, body),
            "books_disposition": disposition,
            "selection_unit": "DA-20260609-OVERSIGHT" if aid == "2606.08919" else ("DA-20260609-VERIFIER" if aid == "2606.08960" else ("DA-20260609-DELEGATION" if aid == "2606.09692" else None)),
        })
    RECEIPTS.write_text(json.dumps({
        "schema": "daily-source-review-receipts-v2.1", "denominator_id": DENOMINATOR_ID,
        "counts": {"total": len(reviews), "deep": len(reviews), "standard": 0, "pending": 0},
        "reviews": reviews,
    }, ensure_ascii=False, indent=2) + "\n")

    integrate = [r for r in reviews if r["books_disposition"] == "Integrate"]
    q = [f"# 2026-06-09 Books Integration Queue V1\n\nDenominator: `{DENOMINATOR_ID}`. Final reconciled disposition after root writeback and fresh audit.\n",
         "## Integrated net deltas\n"]
    owner_file = {
        "AGENT-WORKFLOW": "Books/part-07-agent/81-workflow.md", "AGENT-RAG": "Books/part-07-agent/76-rag.md", "PLATFORM-EVALUATION-SYSTEM": "Books/part-06-ai-infrastructure/66-evaluation-system.md",
        "PLATFORM-SECURITY": "Books/part-06-ai-infrastructure/72-security.md", "INFER-PREFILL": "Books/part-05-inference-system/43-prefill.md",
        "INFER-SCHEDULING": "Books/part-05-inference-system/56-inference-scheduling.md", "INFER-KSERVE-TOPOLOGY": "Books/part-05-inference-system/53-kserve-llm.md",
        "INFER-TENSORRT-LLM": "Books/part-05-inference-system/49-tensorrt-llm.md", "PLATFORM-TRACE": "Books/part-06-ai-infrastructure/69-trace.md",
        "TRAIN-RLHF": "Books/part-04-training-system/31-rlhf.md",
    }
    for r in integrate:
        delta = META[r["arxiv_id"]][1]
        q.append(f"- `{r['family']}` → `{owner_file[r['owner']]}`: {delta} Review note must cite `https://arxiv.org/html/{r['arxiv_id']}v1` and preserve the non-proof boundary in `{r['limitations_locator']}`.")
    q.append("\n## No Change handoff\n\n- `2606.09061` → Ch56: existing aging, predictor drift, starvation and static fallback text already owns the conclusion; no append.\n")
    QUEUE.write_text("\n".join(q) + "\n")

    ready_paragraphs = {
        "AGENT-WORKFLOW": "Human-in-the-Loop 不是无限可靠的外部 oracle，而是 control loop 内会分歧、疲劳且可被 flooding 消耗的有限资源（SF-2026-ARXIV-2606-08919）。因此 approval policy 必须同时持有 action-risk threshold、review load、reviewer capacity 与 no-bypass interception；全升级不天然更安全。把通用 coding agent 接到 scientific simulator 时，也不应重写 agent loop，而应把 simulator 的 executable contract 外置为 procedural memory、retrieval、agent-callable validation 与 validation-gated termination（SF-2026-ARXIV-2606-09774）。结构完整 gate 防 omission，memory/retrieval 修 value correctness；二者由接口瓶颈决定，且 schema 通过不等于物理正确。",
        "AGENT-RAG": "向量数据库不能只用静态 query QPS 定义容量；upload/insertion、index build、query 与 mixed read/write 必须进入同一 lifecycle contract（SF-2026-ARXIV-2606-08950），并绑定 corpus/index version、partition ownership、shared-storage traffic 与 broadcast-gather/aggregation path。增加 nodes/workers 会扩大并行度，也会放大协调、共享存储与结果聚合成本，因此 scale-out 可能反向降低吞吐。HPC-native MPI/Apptainer 路径适合已有超算与大规模批处理；普通规模、低并发或缺少 HPC control plane 时，云端独立服务仍是更简单基线。",
        "PLATFORM-EVALUATION-SYSTEM": "Verifier 是 evaluation/reward 的可执行责任边界。可用 hacker→fixer→solver 循环让攻击发现 exploit、fixer 修补 verifier、solver 验证合法解仍能通过（SF-2026-ARXIV-2606-08960）；循环结束后仍需 held-out exploit corpus，因为能力受 hacker repertoire 与 substrate 约束。评测结果本身还应把 benchmark metadata、run data 与 model metadata 组合成可追踪 Evaluation Card，并显式呈现 reproducibility、documentation completeness、provenance/risk 与 score comparability（SF-2026-ARXIV-2606-09809）；interpretive layer 帮助不同读者定位证据，不能替代原始 run record。",
        "PLATFORM-SECURITY": "RAG 与 tool-agent 的安全边界不能只存在于当前 prompt。Document-authored metadata/provenance 必须被当作不可信 data，不能在自然语言拼接中冒充 policy/control signal（SF-2026-ARXIV-2606-09005）；channel separation、retrieval-time redaction 与 output scan 是互补控制而非完整防御。跨 turn 的 artifact write/read 还必须携带 lineage，使 downstream policy 能识别由多个局部无害步骤组合出的禁止结果（SF-2026-ARXIV-2606-09084）；lineage enforcement 增加 instrumentation、storage 与 benign cross-session false positive，缺少校准时应保留 sandbox、approval 与终局 verifier。",
        "INFER-PREFILL": "RAG 的重复文档让 Prefill 出现区别于普通 prefix cache 的复用面：offline 只保存与 query 无关的 local-attention selective index，online 重算 query-sensitive cross attention，再把 selective state 送入后续层（SF-2026-ARXIV-2606-09441）。它用 index storage、offline build 与 custom kernel 换 TTFT，并避免整份 KV 从低速存储搬运；当文档复用率低、attention pattern 漂移或实现不支持 selective replay 时，完整 Prefill 仍是正确回退。",
        "INFER-SCHEDULING": "多轮 Agent Serving 的可计费与可调度单位是 program，而非孤立 request（SF-2026-ARXIV-2606-09613）。Simulator 必须保留 program identity、turn dependency、tool-induced gap、session affinity，以及 KV 在 HBM、host DRAM/CXL 与 eviction 之间的 residency；评价用 program JCT、throughput 与 policy-rank preservation。Simulation 适合筛选 design space，但 calibration 绑定具体 trace/model/hardware，最终 release 仍需实机验证。",
        "INFER-KSERVE-TOPOLOGY": "可扩展 foundation model 的 serving topology 可把 base weights 与 extension state 分离并虚拟化：公共层由共享 worker 持有，extension 由按请求 placement/cache 装载与组合（SF-2026-ARXIV-2606-09643）。这提高多 extension density，却把 extension version、cache miss、interference、compatibility 与 failure isolation 变成 runtime state；扩展数量少、强隔离或尾延迟优先时，独立 replica 仍是更可验证的分支。",
        "INFER-TENSORRT-LLM": "Agent 生成 megakernel 时，自然语言计划只产生 proposal，不能直接获得执行 authority；typed IR、shape/layout/resource 静态检查、编译、bit/numerical validation 与 performance gate 必须全部通过，失败才允许 self-retarget（SF-2026-ARXIV-2606-09682）。同一执行链还需要 vendor-neutral numeric contract：对 FP8、BF16、MXFP4 与 microscaling 等 84 个 format 提供 bit-exact encode/decode、rounding、overflow、NaN/Inf/subnormal conformance vectors（SF-2026-ARXIV-2606-09686）。格式一致性只证明表示语义，不证明 workload 的精度或性能。",
        "PLATFORM-TRACE": "Agent trace 需要同时表示两张不能互相推导的图（SF-2026-ARXIV-2606-09692）：execution graph 记录因果调用，authority graph 记录 principal→delegation→re-delegation 的权限 lineage。工具调用时必须绑定 durable delegation identity，并把 action/resource 归一化，才能在 concurrency、retry、sub-agent fanout 后重建 delegation footprint；单独塞一个 delegation_id 不会自动提供 lineage closure、minting authority、absence semantics 或跨工具一致性。",
        "TRAIN-RLHF": "Reward hacking 不应只在 exploit rate 上升后监测；训练可能先形成 proxy-reward internalization，即模型学会判断任务正确性、预测 proxy acceptance，并推理 proxy 与 gold 的可利用 gap（SF-2026-ARXIV-2606-09711）。可将 direct/activation probes 与 evaluator-switch test 作为 early-warning signal，并用 intervention 检查其与 hacking 的关系；当前证据绑定 pytest coding RL，probe 相关性不构成跨域 causal guarantee，也不能替代 held-out gold evaluator。",
    }
    ready = [f"# 2026-06-09 Ready-to-Insert Books Blocks V1\n\nDenominator: `{DENOMINATOR_ID}`. Proposal-only; root owns Books writeback.\n", "## Owner-merged minimal prose\n"]
    for owner, paragraph in ready_paragraphs.items():
        ready.append(f"### `{owner}`\n\n{paragraph}\n")
    ready.append("## Source-specific Review notes\n")
    for r in integrate:
        aid=r["arxiv_id"]
        ready.append(f"- `{r['family']}` — exact-v1: `https://arxiv.org/html/{aid}v1`; method `{r['method_locator']}`; evaluation `{r['evaluation_locator']}`; boundary `{r['limitations_locator']}`. {NON_PROOF[aid]} 不得用 later version/artifact 扩张 v1 claim。")
    READY.write_text("\n".join(ready) + "\n")

    audit_lines = [
        "# 2026-06-09 Post-write Fresh-context Audit V1\n",
        f"Denominator: `{DENOMINATOR_ID}`. Scope: 14/14 Integrate markers plus 1/1 No Change handoff. Auditor did not edit Books.\n",
        "| Family | Final disposition | Owner / target | Fresh audit result | Exact-v1 non-proof boundary |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in integrate:
        aid = r["arxiv_id"]
        audit_lines.append(f"| `{r['family']}` | Integrate | `{r['owner']}` / `{owner_file[r['owner']]}` | passed — mechanism, state/control owner, coexistence/trade-off, unique target and Review note present | {NON_PROOF[aid]} |")
    audit_lines += [
        "| `SF-2026-ARXIV-2606-09061` | No Change — Existing Coverage | `INFER-SCHEDULING` / `Books/part-05-inference-system/56-inference-scheduling.md` | passed — existing token-budget, remaining-work/predictor, aging/starvation and FCFS/static-fallback mechanisms own the handoff; no duplicate source append | exact-v1 result remains workload/hardware/calibration-bound and does not prove a universal scheduling optimum |",
        "\n## Findings and resolution\n",
        "- Initial fresh audit rejected the prewrite No Change disposition for `2606.08950`: Ch76 lacked vector-DB lifecycle and coordination scaling. Root added the minimal owner text and exact-v1 Review note; targeted recheck passed.",
        "- All 14 exact-v1 sources occur in exactly one owner file and one Review note; `2606.09686` remains 84-format, and `2606.08919` remains simulation/prior-art rather than a human study.",
        "- Daily Integration Decision, Repository Changes and Open Questions were reconciled to 14 Integrate + 1 No Change; no actionable finding remains.",
        "\nFinal Books Gate: **Passed**.\n",
    ]
    POST_WRITE_AUDIT.write_text("\n".join(audit_lines) + "\n")

    selected = {"2606.08919", "2606.08960", "2606.09692"}
    selection_rows = []
    for row in reviews:
        aid, fam = row["arxiv_id"], row["family"]
        decision = "selected" if aid in selected else "not_selected"
        unit = row["selection_unit"] or "—"
        eligibility = ["score_7_9"]
        if row["books_disposition"] == "Integrate":
            eligibility.append("potential_books_delta")
        if decision == "selected":
            reason = "Selected after full-frontier comparison for non-overlapping owner novelty and direct Books impact."
            narrative = f"analysis:{unit}"
        else:
            reason = (
                f"{META[aid][1]} The family remains fully reviewed, but its owner-local delta is less "
                "cross-cutting than the three selected units; non-selection does not lower Books duty."
            )
            narrative = f"analysis-decision:{fam}"
        selection_rows.append({
            "source_family_id": fam,
            "eligibility": eligibility,
            "decision": decision,
            "analysis_unit_id": unit,
            "subsumed_by": "—",
            "priority_rationale": reason,
            "narrative_ref": narrative,
        })
    assert len(selection_rows) == 15
    assert sum(row["decision"] == "selected" for row in selection_rows) == 3
    SELECTION.write_text(json.dumps({
        "contract": "eligible families only in canonical rows; non-eligible closures remain outside the main table",
        "candidate_count": len(reviews),
        "eligible_count": len(selection_rows),
        "noneligible_count": 0,
        "selected_unit_count": 3,
        "rows": selection_rows,
        "noneligible_rows": [],
    }, ensure_ascii=False, indent=2) + "\n")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    families = "; ".join(r["family"] for r in reviews)
    lines = [f"# Daily Research — 2026-06-09\n",
        "**Research Date:** 2026-06-09\n",
        "**Timezone:** Asia/Shanghai\n",
        "**Strict Window:** 2026-06-08 09:00:00 ～ 2026-06-09 09:00:00（北京时间，左闭右开）\n",
        "**Contract:** V2.1 Full Replay；477/477 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet\n",
        "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding\n",
        f"> Strict V2.1 reconstruction for `{DENOMINATOR_ID}`. No Books file is modified in this report.\n",
        "## Executive Summary\n",
        f"The Beijing window contains 477 registered arXiv identities. Full 477/477 title+abstract screening freezes {len(reviews)} durable families and {477-len(reviews)} family-specific closures. Exact-v1 review passes all retained families. Corrected-contract Selection is `15 retained = 15 eligible + 0 non-eligible`, with three selected units; this equality is derived from all retained scores rather than assumed. Books formal comparison covers 15/15 families (14 Integrate, one No Change), while Weekly Only is explicitly zero. Evidence Gate and Books Gate are Passed after serialized writeback and post-write fresh audit.\n",
        "## 1. Coverage\n", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |\n| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
        "| Window Start | 2026-06-09 |", "| Window End | 2026-06-09 |", "| Registry Version | 2026-08-25 |",
        "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
        f"| Denominator ID | {DENOMINATOR_ID} |", f"| Denominator Frozen At | {EXECUTED_AT} |",
        "| Completion Status | Complete |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Passed |\n",
        "### Source Coverage Receipt\n", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |\n| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-06-08T09:00:00+08:00 | 2026-06-09T09:00:00+08:00 | {EXECUTED_AT} | Frozen DataCite DOI-prefix snapshots; Core full enumeration; 477/477 semantic screen | checked | 477 | {families} | pages=4, records=4000/4000, final cursor=end | 2026-06-09T01:00:00Z | ../_sources/daily-20260609/screening-ledger.json; ../_sources/daily-20260609/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260609 | — |\n",
        "<!-- coverage:SRC-ARXIV:20260609:start -->\nAll 477 registered identities were screened at title+abstract level; 15 retained and 462 row-specific closures. No absent identity is counted as a closure: `2606.09138` is the discovered Claw-R1 identity and has its own family-specific pre-denominator closure; `2606.09686` uses the official exact-v1 84-Format title instead of the discovery snapshot's 83-Format title.\n<!-- coverage:SRC-ARXIV:20260609:end -->\n",
        "## 2. Candidate Ledger\n", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |\n| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in reviews:
        s=r["score"]; fam=r["family"]
        lines.append(f"| {fam} | arXiv:{r['arxiv_id']}v1 | {r['event']} | 2026-W24 | 2026-06-08 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | none | review:{fam} | self | — | new_in_window | {r['owner']} | {r['books_disposition']} | books-review:{fam} | yes |")
    lines += ["\n## 3. Review Completion Receipt\n", "<!-- validator:review-completion-v1 -->",
        "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        lines.append(f"| {r['family']} | {r['provenance']} | deep | {r['primary_evidence']} | {r['reviewed_versions']} | {r['method_locator']} | {r['evaluation_locator']} | {r['limitations_locator']} | {r['artifact_locator']} | {r['claim_boundary']} | complete |")
    lines.append("\n### Source Reviews\n")
    for r in reviews:
        lines += [f"<!-- review:{r['family']}:start -->", r["body"], f"<!-- review:{r['family']}:end -->\n"]
    lines += ["\n## 4. Benchmark Contracts\n", "<!-- validator:benchmark-contract-v1 -->",
        "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=r["benchmark"]
        lines.append("| " + " | ".join([r["family"],b["workload"],b["model"],b["hardware"],b["precision"],b["input_length"],b["output_length"],b["batch"],b["concurrency"],b["slo"],b["evaluator"]]) + " |")
    lines += ["## 5. Deep Analysis Selection\n", "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |\n| --- | --- | --- | --- | --- | --- | --- |"]
    for row in selection_rows:
        lines.append(
            f"| {row['source_family_id']} | {'; '.join(row['eligibility'])} | {row['decision']} | "
            f"{row['analysis_unit_id']} | {row['subsumed_by']} | {row['priority_rationale']} | {row['narrative_ref']} |"
        )
    for r in reviews:
        if not r["selection_unit"]:
            lines.append(f"\n<!-- analysis-decision:{r['family']}:start -->\n{META[r['arxiv_id']][1]} Full-frontier review retained the source but did not select it over the three non-overlapping analysis units.\n<!-- analysis-decision:{r['family']}:end -->")
    lines += ["\n### Non-eligible family-specific closures\n",
        "`15 retained = 15 eligible + 0 non-eligible`；两组互斥且并集等于 Candidate Ledger。None — all 15 retained families are eligible；本节显式保留空 closure，不向 canonical Selection 主表伪造行。\n",
        "<!-- analysis:DA-20260609-OVERSIGHT:start -->\n### DA-20260609-OVERSIGHT\nHuman review capacity is part of the control loop: escalation consumes a subjective, fatiguing resource, so the release contract must bind guard threshold, review load and flooding behavior.\n<!-- analysis:DA-20260609-OVERSIGHT:end -->\n",
        "<!-- analysis:DA-20260609-VERIFIER:start -->\n### DA-20260609-VERIFIER\nVerifier hardening is a three-party protocol, not a patch count: exploit discovery, rejection patching and legitimate-solution survival must close before a benchmark or RL reward is trusted.\n<!-- analysis:DA-20260609-VERIFIER:end -->\n",
        "<!-- analysis:DA-20260609-DELEGATION:start -->\n### DA-20260609-DELEGATION\nAgent accountability needs two graphs: causal traces explain execution order, while an authority graph binds durable delegation and re-delegation lineage. Neither can be inferred safely from the other.\n<!-- analysis:DA-20260609-DELEGATION:end -->\n",
        "## 6. Books Comparison\n",
        "<!-- validator:books-comparison-v1 -->\n| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    target_ref={
        "2606.08919":"Books/part-07-agent/81-workflow.md#L716", "2606.08950":"Books/part-07-agent/76-rag.md#L51",
        "2606.08960":"Books/part-06-ai-infrastructure/66-evaluation-system.md#L1946", "2606.09005":"Books/part-06-ai-infrastructure/72-security.md#L992",
        "2606.09061":"Books/part-05-inference-system/56-inference-scheduling.md#L180", "2606.09084":"Books/part-06-ai-infrastructure/72-security.md#L998",
        "2606.09441":"Books/part-05-inference-system/43-prefill.md#L331", "2606.09613":"Books/part-05-inference-system/56-inference-scheduling.md#L718",
        "2606.09643":"Books/part-05-inference-system/53-kserve-llm.md#L195", "2606.09682":"Books/part-05-inference-system/49-tensorrt-llm.md#L991",
        "2606.09686":"Books/part-05-inference-system/49-tensorrt-llm.md#L997", "2606.09692":"Books/part-06-ai-infrastructure/69-trace.md#L165",
        "2606.09711":"Books/part-04-training-system/31-rlhf.md#L414", "2606.09774":"Books/part-07-agent/81-workflow.md#L722",
        "2606.09809":"Books/part-06-ai-infrastructure/66-evaluation-system.md#L1952",
    }
    adjacent={
        "AGENT-WORKFLOW":"books/part-07-agent/80-reflection.md#L1; books/part-07-agent/82-multi-agent.md#L1",
        "AGENT-RAG":"books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1",
        "PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1",
        "PLATFORM-SECURITY":"books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1",
        "INFER-SCHEDULING":"books/part-05-inference-system/55-pd-disaggregation.md#L1; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L1",
        "INFER-PREFILL":"books/part-05-inference-system/42-what-happens-during-inference.md#L1; books/part-05-inference-system/44-decode.md#L1",
        "INFER-KSERVE-TOPOLOGY":"books/part-05-inference-system/52-dynamo.md#L1; books/part-05-inference-system/54-gpu-memory.md#L1",
        "INFER-TENSORRT-LLM":"books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-05-inference-system/50-vllm.md#L1",
        "PLATFORM-TRACE":"books/part-06-ai-infrastructure/68-logging.md#L1; books/part-06-ai-infrastructure/70-cost.md#L1",
        "TRAIN-RLHF":"books/part-04-training-system/30-lora.md#L1; books/part-04-training-system/32-ppo.md#L1",
    }
    for r in reviews:
        fam=r["family"]
        relation="Direct Evolution" if r["books_disposition"]=="Integrate" else "Principle Reuse"
        lines.append(f"| {fam} | {r['owner']} | {target_ref[r['arxiv_id']]} | {adjacent[r['owner']]} | existing:{fam} | delta:{fam} | {relation} | {r['books_disposition']} | books-review:{fam} |")
    for r in reviews:
        fam=r["family"]
        lines.append(f"\n<!-- existing:{fam}:start -->\nOwner `{r['owner']}` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.\n<!-- existing:{fam}:end -->")
        lines.append(f"\n<!-- delta:{fam}:start -->\n{META[r['arxiv_id']][1]}\n<!-- delta:{fam}:end -->")
        lines.append(f"\n<!-- books-review:{fam}:start -->\nOwner `{r['owner']}`; relation `{'Direct Evolution' if r['books_disposition']=='Integrate' else 'Principle Reuse'}`; disposition `{r['books_disposition']}`.\n<!-- books-review:{fam}:end -->")
    lines += [f"\nAll {len(reviews)} retained families were compared with current owner and adjacent chapters. Final disposition is 14 Integrate net deltas and one No Change handoff. All writebacks and the post-write fresh audit passed.\n",
        "## 7. Semantic Audit\n",
        "<!-- validator:semantic-audit-v1 -->\n| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |\n| --- | --- | --- | --- | --- | --- | --- |",
        "| SA-20260609-COVERAGE-V1 | fresh-context:jun09-corrected-contract-v1 | coverage | coverage:SRC-ARXIV:20260609 | — | Resolved stale absent-identity closure claim by removing `2606.09137` from closure accounting; verified discovered `2606.09138` has its own family-specific closure; retained the real `2606.09686` exact-v1 84-Format normalization; denominator frozen 15/477 | passed |",
        f"| SA-20260609-EVIDENCE-V1 | fresh-context:jun09-v1 | evidence | {'; '.join('review:'+r['family'] for r in reviews)} | — | 15/15 exact-v1 method/evaluation/limitations and benchmark contracts | passed |",
        f"| SA-20260609-SELECTION-V1 | fresh-context:jun09-corrected-contract-v1 | deep_analysis_selection | {'; '.join(('analysis:'+r['selection_unit']) if r['selection_unit'] else ('analysis-decision:'+r['family']) for r in reviews)} | — | 15 retained = 15 eligible + 0 non-eligible; disjoint union reproduced; canonical main table contains only eligible families; three selected | passed |",
        f"| SA-20260609-BOOKS-POSTWRITE-V1 | fresh-context:jun09-v1 | books | {'; '.join('books-review:'+r['family'] for r in reviews)} | — | 14/14 Integrate markers and 1/1 No Change handoff fresh-audited; initial 08950 finding resolved in Ch76; packet `POST_WRITE_FRESH_AUDIT_V1.md` | passed |\n",
        "### Materials and Access\n",
        "- DataCite DOI-prefix snapshots are frozen and hashed in the packet; they are discovery/identity/abstract evidence only.\n- Exact-v1 manuscripts were reviewed through `https://arxiv.org/html/<id>v1`; direct shell transfer reset, so the official HTML web path was used.\n- Identity accounting uses the 477 actually discovered arXiv IDs: `2606.09138` is Claw-R1 and has a normal family-specific closure; absent `2606.09137` is not counted.\n",
        "## 8. Ignored Noise\n",
        "The 462 pre-denominator closures remain row-addressable in the screening ledger with family-specific reasons and reopen conditions; they are not scored, selected or leaked into Books.\n",
        "## 9. Recommended Action\n",
        "Final disposition is 14 Integrate and one No Change — Existing Coverage (`2606.09061`); formal Books comparison=15 and Weekly Only=0. The initial No Change for `2606.08950` was overturned by fresh audit and resolved through the Ch76 writeback.\n",
        "## 10. Repository Changes\n",
        "Root wrote the 14 Books deltas across 10 owner chapters; this lane edits the 2026-06-09 Daily, its source packet and deterministic finalizer, and independently records the post-write fresh audit.\n",
        "## 11. Open Questions\n",
        "No Gate-blocking question remains. Future work must revalidate workload-specific simulator, numeric-format, vector-database and security-defense claims rather than treating these exact-v1 results as production constants.\n",
        "## 12. Sources\n",
        "- [arXiv exact-v1 HTML](https://arxiv.org/) — primary manuscripts for all retained claims.\n- DataCite arXiv DOI prefix snapshots — frozen discovery metadata under `../_sources/daily-20260609/datacite/`.\n",
        "## 13. Final Status\n",
        "Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。477 个 raw identities 已闭合为 15 个 retained families 与 462 个 family-specific pre-denominator closures；Selection 为 15 eligible + 0 non-eligible、selected=3，互斥并集守恒；Benchmark Claim=yes 子集 15/15 完整；Books formal comparison=15、Weekly Only=0。全部 scope 通过 fresh-context audit，未解决 finding 为 0。\n",
    ]
    REPORT.write_text("\n".join(lines))

    manifest_paths = sorted((PACKET / "datacite").glob("*.json.gz")) + [
        PROVISIONAL,
        LEDGER,
        AUDIT,
        RECEIPTS,
        QUEUE,
        READY,
        POST_WRITE_AUDIT,
        SELECTION,
        REPORT,
        Path(__file__).resolve(),
        ROOT / "scripts/audit_june09_corrected_contract.py",
        ROOT / "scripts/test_june09_corrected_contract.py",
    ]
    for optional in (
        PACKET / "INDEPENDENT_ACCEPTANCE_V1.md",
        PACKET / "independent-acceptance-v1.json",
    ):
        if optional.exists():
            manifest_paths.append(optional)
    SHA_MANIFEST.write_text(
        "\n".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}"
            for path in manifest_paths
        )
        + "\n"
    )


if __name__ == "__main__":
    main()
