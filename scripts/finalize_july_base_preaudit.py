#!/usr/bin/env python3
"""Merge a July base review with its fresh-context preaudit.

The output is an importable packet.  It does not edit Books, the central
receipt ledger, or a Daily report; those remain explicit caller steps.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26"
SNAPSHOT_DIR = SOURCE_DIR / "arxiv-html"


def arxiv_id(family: dict) -> str:
    match = re.search(r"arXiv:(\d{4}\.\d{4,5})v1", family["primary_identifier"], re.I)
    if not match:
        raise ValueError(f"Invalid exact-v1 identity: {family['primary_identifier']!r}")
    return match.group(1)


def repo_from_commit_url(url: str) -> str:
    parts = urlparse(url).path.strip("/").split("/")
    if len(parts) < 2:
        raise ValueError(f"Cannot derive GitHub repository from {url!r}")
    return "/".join(parts[:2])


def exact_html_locators(identifier: str, values: list[str]) -> list[str]:
    result: list[str] = []
    for value in values:
        if value.startswith(f"arXiv:{identifier}v1#"):
            value = value.replace(
                f"arXiv:{identifier}v1#",
                f"https://arxiv.org/html/{identifier}v1#",
                1,
            )
        result.append(value)
    return result


def validate_snapshot(identifier: str, path: Path, expected_sha: str, locators: list[str]) -> None:
    payload = path.read_bytes()
    actual_sha = hashlib.sha256(payload).hexdigest()
    if actual_sha != expected_sha:
        raise ValueError(f"{identifier}: SHA mismatch: {actual_sha} != {expected_sha}")
    if path.suffix != ".html":
        return
    document = payload.decode("utf-8", errors="ignore")
    anchors = set(re.findall(r'id=["\']([^"\']+)["\']', document))
    for locator in locators:
        for fragment in re.findall(
            rf"https://arxiv\.org/html/{re.escape(identifier)}v1#([^\s;]+)", locator
        ):
            if fragment not in anchors:
                raise ValueError(f"{identifier}: missing exact anchor #{fragment}")


BENCHMARK_CONTRACTS: dict[str, dict[str, str]] = {
    "2607.10987": {
        "workload": "Synthetic deterministic shared-prefix multi-agent workflows on 4-16 nodes with deterministic decoding; analytical cost model parameterized by author microbenchmarks",
        "model": "Mistral-7B; Llama-3-8B-Instruct",
        "hardware": "4-16 nodes with NVIDIA A100 40GB or 80GB GPUs, 32-64 CPU cores per node, and RDMA InfiniBand",
        "precision": "Not Disclosed",
        "input_length": "Mistral context 32,640 tokens; Llama 3 context 8,128 tokens; deterministic shared-prefix prompts",
        "output_length": "64 tokens",
        "batch": "Not Disclosed",
        "concurrency": "Workflow width 1-16 agents; serving request concurrency Not Disclosed",
        "slo": "No production latency, quality, or availability SLO",
        "evaluator": "Author-controlled system measurements and analytical cost model",
    },
    "2607.11070": {
        "workload": "Multi-turn jailbreak training on AdvBench for 260 steps and evaluation on HarmBench, StrongREJECT, and JailbreakBench; attacker/victim/judge temperatures 0.9/0/0",
        "model": "Qwen3-4B attacker; appendix Qwen2.5-3B; Llama, Qwen, Gemma, Mistral, and GPT-OSS-20B victims",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed",
        "input_length": "Up to 5 attack turns; token length Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Group size 10; serving batch Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "No production security or latency SLO",
        "evaluator": "HarmBench, StrongREJECT, and JailbreakBench evaluation protocols",
    },
    "2607.11079": {
        "workload": "Held-out synthetic and real scientific-discovery tasks using multiple-choice and open-ended questions",
        "model": "GPT-5.4; GPT-5.4 mini; Claude Sonnet 4.6; Gemini 3.1 Pro; Gemini 3.1 Flash; DeepSeek V3.2; DeepSeek R1; Qwen 3.5-397B-A17B; Qwen 3-235B-Instruct; Kimi K2.5; GLM 5; Llama 3.3-70B-Instruct; Llama-3.1-8B-Instruct; two LoRA variants of Llama-3.1-8B-Instruct",
        "hardware": "Not Disclosed; hosted-model hardware is not controlled by authors",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "No production latency or availability SLO",
        "evaluator": "MCQ accuracy; deterministic OEQ scoring with GPT-4o fallback",
    },
    "2607.11149": {
        "workload": "Six task families across eight agent-framework versions, three repetitions each, 70 controlled fresh-sandbox runs; DeepSeek-V4-Flash temperature 0",
        "model": "DeepSeek-V4-Flash provider held constant",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed",
        "input_length": "Task-dependent; Not Disclosed as a normalized token length",
        "output_length": "Task-dependent; Not Disclosed as a normalized token length",
        "batch": "One isolated run per fresh sandbox; training/serving batch Not Applicable",
        "concurrency": "Not Disclosed",
        "slo": "No production retention, latency, or recovery SLO",
        "evaluator": "Task accuracy, including deterministic exact-substring grading for selected file-QA tasks, plus logical bytes, composition, duplication, compressibility, growth, and reconstructability",
    },
    "2607.11172": {
        "workload": "3k SFT and 2.6k RL search queries with live Serper/Jina retrieval; BrowseComp, BrowseComp-ZH, and xbench-DS evaluation",
        "model": "Qwen3-30B-A3B-Thinking",
        "hardware": "16 NVIDIA H800 GPUs for SFT and 16 NVIDIA H800 GPUs for RL",
        "precision": "Not Disclosed",
        "input_length": "Maximum context 64K or 128K tokens depending on experiment",
        "output_length": "Not Disclosed",
        "batch": "SFT batch size 32 for 1 epoch; RL global batch 256 with rollout size 32 and 8 samples per prompt",
        "concurrency": "Rollout group 8 samples per prompt; serving request concurrency Not Disclosed",
        "slo": "No production search latency or availability SLO",
        "evaluator": "GPT-5.1 judge/verifier on BrowseComp, BrowseComp-ZH, and xbench-DS",
    },
    "2607.11183": {
        "workload": "Offline aligned activation mining over three models and eight text/tool datasets; 241,056 feature rows each for Qwen3.5/Qwen2.5 and 165,432 for Qwen3; feature ablation uses a stable-hash split of 7,396 samples per model and common tool test n=2,556 per model",
        "model": "Qwen3.5-9B; Qwen3-8B; Qwen2.5-7B",
        "hardware": "Not measured or Not Disclosed for serving",
        "precision": "Not Disclosed",
        "input_length": "Dataset-dependent; Not Disclosed as a normalized length",
        "output_length": "Dataset-dependent; Not Disclosed as a normalized length",
        "batch": "Qwen2.5 run batch size 64; other model-run batch sizes Not Disclosed",
        "concurrency": "Not measured",
        "slo": "Online latency, throughput, memory, and production SLO not measured",
        "evaluator": "Dataset task metrics with selected bootstrap confidence intervals",
    },
    "2607.11250": {
        "workload": "HotpotQA hard subset (600 samples, 5 rounds) and Math500/GPQA (3 rounds), with exploration in the first half and exploitation thereafter; Qwen2.5-7B-Instruct temperature 1.2, GPT-4/GPT-5 default temperature",
        "model": "Ten Qwen2.5-7B-Instruct agents for HotpotQA; GPT-5, Qwen2.5-7B-Instruct, Llama3.1-8B-Instruct, and Mistral-7B-v0.3 agents for Math500/GPQA",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed",
        "input_length": "Task-dependent; Not Disclosed as a normalized length",
        "output_length": "Maximum 2,048 tokens in all disclosed settings",
        "batch": "Not Disclosed",
        "concurrency": "Workflow width up to 10 agents; serving request concurrency Not Disclosed",
        "slo": "No production latency or coordination SLO",
        "evaluator": "Task-answer accuracy under fixed multi-round protocols",
    },
    "2607.11487": {
        "workload": "Three daily-life egocentric-memory scenarios with manually annotated ground truth and phone/glasses prototype latency measurements",
        "model": "Upstream API, embedding, retrieval, and LLM component identities Not Disclosed",
        "hardware": "Phone and smart-glasses prototype; exact device SKUs Not Disclosed in the review contract",
        "precision": "Not Disclosed",
        "input_length": "Scenario-dependent multimodal stream duration; normalized token/frame length Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Interactive single-user prototype; batch Not Applicable",
        "concurrency": "Single-user prototype; multi-user concurrency Not Evaluated",
        "slo": "P50/P90 component latency reported; no production availability or privacy SLO",
        "evaluator": "Recall@k, MRR, LLM-based answer scoring, human scoring, and prototype latency",
    },
    "2607.11498": {
        "workload": "RoboCasa simulation design ablations plus real-world VLA tasks; controlled study uses 24 tasks, 50 human demonstrations per task, 30k steps, and 50 evaluation episodes per task",
        "model": "π0.5 and SmolVLA pretrained VLA backbones; controlled study uses a PaliGemma-initialized π-style architecture with a fresh action expert",
        "hardware": "Simulation and real robot setup; full deployment compute Not Disclosed",
        "precision": "bfloat16 for π0.5/SmolVLA fine-tuning",
        "input_length": "RGB at each backbone's native resolution plus robot-centric pointmap, language instruction, and proprioception; normalized sequence length Not Disclosed",
        "output_length": "Chunk of end-effector deltas; action-chunk length Not Disclosed in the review contract",
        "batch": "Effective batch size 64 for π0.5/SmolVLA fine-tuning",
        "concurrency": "Single embodied control loop; fleet concurrency Not Evaluated",
        "slo": "Control frequency and physical-safety SLO Not Disclosed",
        "evaluator": "RoboCasa success metrics, design ablations, and real-world task success",
    },
    "2607.11505": {
        "workload": "Proxy-to-primary on-policy distillation on math and code tasks; PUST and proxy-GRPO training use temperature 1.0 and rollout count 8; proxy training runs 500 or 300 steps",
        "model": "Qwen3-1.7B and Qwen3-4B proxies; Qwen3-8B primary",
        "hardware": "8 NVIDIA A100 80GB GPUs",
        "precision": "Not Disclosed",
        "input_length": "PUST maximum prompt 1,024 or 2,048 tokens by task; proxy GRPO maximum prompt 2,048 tokens",
        "output_length": "Maximum response 16,384 tokens for PUST and proxy GRPO",
        "batch": "PUST train batch 256; proxy GRPO train/microbatch 128; rollout count 8. Mean@16/Mean@8 are evaluation sampling, not optimizer batch",
        "concurrency": "Not Disclosed",
        "slo": "No deployment latency or availability SLO",
        "evaluator": "Math/code correctness aggregated as Mean@16 or Mean@8 plus calibration ablations",
    },
    "2607.11656": {
        "workload": "ADNI, AIBL, and OASIS clinical cohorts across binary classification, multiclass classification, and cognitive prediction; final transformer training uses 7 epochs at learning rate 1e-6",
        "model": "NITROGEN and NAIM transformers; XGBoost, LightGBM, Random Forest, MA-Lasso, and MA-GBT baselines",
        "hardware": "Not Disclosed; not central to the clinical evaluation contract",
        "precision": "Not Disclosed",
        "input_length": "Patient feature sequences with heterogeneous missingness; normalized sequence length Not Disclosed",
        "output_length": "Class or cognitive prediction; generative output length Not Applicable",
        "batch": "AdamW batch size 128",
        "concurrency": "Not Applicable to the reported offline cohort evaluation",
        "slo": "No clinical deployment latency or safety SLO",
        "evaluator": "Cohort task metrics, calibration, attribution, and sufficiency tests",
    },
    "2607.11673": {
        "workload": "Module-level and end-to-end trajectory, panoramic-video, 3D Gaussian Splatting, and system-applicability evaluation",
        "model": "ABot-3DWorld 0 pipeline; exact component versions are source-version bound",
        "hardware": "Panoramic-generator inference measured on one node with 4 NVIDIA RTX 4090 GPUs; other pipeline hardware incompletely disclosed",
        "precision": "Not Disclosed",
        "input_length": "Trajectory and panoramic-video dependent; normalized length Not Disclosed",
        "output_length": "Generated trajectory/video/3D-scene dependent; normalized length Not Disclosed",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "Author-measured panoramic generation latency is about 12 minutes per scene on 4x RTX 4090; this is not a production interactive SLO",
        "evaluator": "Author-controlled module metrics, end-to-end metrics, and demonstrations",
    },
    "2607.11849": {
        "workload": "Advanced mathematical proof generation and verifier-adversarial tasks; temperature 1.0 and highest available reasoning effort unless otherwise specified",
        "model": "GPT-5.5-xhigh; GPT-5.5-high; GPT-5.2; Gemini-3.1-Pro-Preview; Claude-Opus-4.8; DeepSeek-V4-Pro; Qwen3.5-397B-A17B; Kimi-K2.6; GLM-5.2; gpt-oss-120b; Intern-S2-Preview-35B",
        "hardware": "Not Disclosed; hosted-model hardware not controlled by authors",
        "precision": "Not Disclosed",
        "input_length": "Problem-dependent; Not Disclosed as a normalized length",
        "output_length": "Maximum 64k tokens unless otherwise specified",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "No production latency or verifier false-acceptance SLO",
        "evaluator": "Expert-aligned automatic proof/verifier pipeline plus human annotation; gpt-oss-120b meta-verifier for verification outputs",
    },
    "2607.11886": {
        "workload": "AWM reinforcement learning on AlphaGRPO20k for text-to-image generation; 32 prompts per step, group size 16, 16 sampling steps with 6 sampled from the first 10 denoising steps, 380 training steps",
        "model": "BAGEL policy; Qwen3-VL-30B-A3B default SpectraReward MLLM; BAGEL understanding branch for Self-SpectraReward",
        "hardware": "32 NVIDIA A100 GPUs",
        "precision": "Not Disclosed",
        "input_length": "32 text prompts per training step; normalized prompt-token length Not Disclosed",
        "output_length": "Group size 16 images per prompt at 512 x 512 training resolution",
        "batch": "Batch size 2 with gradient accumulation 8",
        "concurrency": "Distributed training across 32 GPUs; serving request concurrency Not Evaluated",
        "slo": "No serving latency or availability SLO",
        "evaluator": "GenEval, TIIF, DPG-Bench, WISE, preference metrics, and reward-model ablations",
    },
    "2607.12227": {
        "workload": "Terminal-Bench 2.1 with the AHE exploration agent disabled; high reasoning effort; results averaged over two independent runs; code agent capped at 300 turns, debugger at 25, and meta agent at 500",
        "model": "GPT-5.4, GPT-5.4 mini, and Claude Opus 4.6 under source-version-bound API and harness configurations",
        "hardware": "Not controlled by authors",
        "precision": "Not controlled by authors",
        "input_length": "200k-token context window",
        "output_length": "Maximum 128k generated tokens per turn",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "No production latency or availability SLO",
        "evaluator": "Terminal-Bench 2.1 pass@1/pass@k and held-out-transfer protocol",
    },
}


ANALYSIS_OLD_SCHEME: dict[str, str] = {
    "2607.10987": (
        "Request-local execution and ordinary data-flow edges were reasonable while each request owned its KV, "
        "prefix reuse stayed inside one engine, and moving cache state across workers cost more than recomputation."
    ),
    "2607.11149": (
        "Token, compute, latency, and task accuracy were reasonable accounting units while agent runs were short-lived, "
        "their workspaces were disposable, and retained files or hidden stores were operational residue rather than lifecycle state."
    ),
    "2607.11250": (
        "Fixed or greedy peer selection was reasonable for short workflows when peer quality was already known, "
        "coordination rounds were scarce, and the cost of exploring an uncertain peer exceeded the expected information gain."
    ),
}


ARTIFACT_BOUNDARY: dict[str, str] = {
    "2607.11487": (
        "Not Required — repository commit was not reviewed with an event-time artifact receipt and is "
        "not part of the technical claim"
    ),
    "2607.11656": (
        "Not Required — repository commit was not reviewed with an event-time artifact receipt and is "
        "not part of the technical claim"
    ),
}


def benchmark_contract(identifier: str) -> dict[str, str]:
    try:
        return BENCHMARK_CONTRACTS[identifier]
    except KeyError as exc:
        raise ValueError(f"{identifier}: missing explicit benchmark contract") from exc


def reasoned_artifact(value: str) -> str:
    if re.search(r"https?://|doi:|arXiv:", value, re.I):
        return value
    if re.match(r"^(Not Disclosed|Not Required|No Artifact Claim)\b", value, re.I):
        return value
    return f"Not Disclosed — {value}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--preaudit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--accessed", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    base = json.loads(args.base.read_text(encoding="utf-8"))
    preaudit = json.loads(args.preaudit.read_text(encoding="utf-8"))
    if base["report_date"] != preaudit["report_date"]:
        raise ValueError("Base review and preaudit dates differ")
    if base["denominator_count"] != preaudit["denominator_count"]:
        raise ValueError("Base review and preaudit denominator counts differ")

    comparisons = {item["source_family_id"]: item for item in preaudit["family_books_comparison"]}
    deep_ids = set(preaudit["route_corrections"]["deep_complete"])
    standard_ids = set(preaudit["route_corrections"]["standard_complete"])
    selected = {
        item["source_family_id"]: item for item in preaudit["deep_analysis_selection"]["selected"]
    }
    not_selected = {
        item["source_family_id"]: item
        for item in preaudit["deep_analysis_selection"]["not_selected"]
    }
    artifact_rows = {
        item["source_family_id"]: item
        for item in preaudit["validation"].get("artifact_receipts", [])
    }
    pdf_correction = preaudit["validation"]["primary_snapshots"].get("pdf_locator_normalization")

    receipts: dict[str, dict] = {}
    family_decisions: list[dict] = []
    for family in base["families"]:
        identifier = arxiv_id(family)
        source_family_id = family["source_family_id"]
        comparison = comparisons[source_family_id]
        source_path = Path(family["local_snapshot"])
        suffix = source_path.suffix.lower()
        target_path = SNAPSHOT_DIR / f"{identifier}v1{suffix}"

        method = exact_html_locators(identifier, family["method_locators"])
        evaluation = exact_html_locators(identifier, family["evaluation_locators"])
        limitations = exact_html_locators(identifier, family["limitations_locators"])
        if pdf_correction and pdf_correction["source_family_id"] == source_family_id:
            method = pdf_correction["method"]
            evaluation = pdf_correction["evaluation"]
            limitations = pdf_correction["limitations"]
        validate_snapshot(identifier, source_path, family["sha256"], method + evaluation + limitations)

        disposition = comparison["decision"]
        if disposition.startswith("Integrate"):
            disposition = "Integrate"
        elif disposition.startswith("Weekly Only"):
            disposition = "Weekly Only — Context"
        route = "deep" if source_family_id in deep_ids else "standard"
        receipt = {
            "title": family["title"],
            "local_snapshot": str(target_path.relative_to(ROOT)),
            "sha256": family["sha256"],
            "node": comparison["stable_node_id"],
            "score": [
                family["score_v2"]["design_delta"],
                family["score_v2"]["system_reach"],
                family["score_v2"]["durability"],
            ],
            "route": route,
            "review_override": "none",
            "reviewed": f"SRC-ARXIV@arXiv:{identifier}v1",
            "method": "; ".join(method),
            "evaluation": "; ".join(evaluation),
            "limitations": "; ".join(limitations),
            "artifact": ARTIFACT_BOUNDARY.get(
                identifier, reasoned_artifact(family["artifact_locator"])
            ),
            "accessed": args.accessed,
            "delta": family["mechanism_summary"],
            "source_claim": family["claim_boundary"],
            "analysis_old": ANALYSIS_OLD_SCHEME.get(identifier, family["state_and_flow"]),
            "analysis_tradeoff": family["claim_boundary"],
            "disposition": disposition,
            "benchmark": benchmark_contract(identifier),
        }
        artifact = artifact_rows.get(source_family_id)
        if artifact:
            receipt["artifact_receipt"] = {
                "repository": repo_from_commit_url(artifact["url"]),
                "until": "2026-07-14T01:00:00Z",
                "commit": artifact["commit"],
                "commit_timestamp": artifact["commit_time"],
                "url": artifact["url"],
                "executed_at": f"{args.accessed}T00:00:00+08:00",
            }
            receipt["reviewed"] += f"; SRC-GITHUB-COMMIT@commit:{artifact['commit']}"
        receipts[identifier] = receipt

        eligibility: list[str] = []
        if sum(receipt["score"]) >= 7:
            eligibility.append("score_7_9")
        if disposition == "Integrate":
            eligibility.append("potential_books_delta")
        if source_family_id in selected:
            item = selected[source_family_id]
            decision = "selected"
            analysis_unit_id = item["analysis_unit_id"]
            reason = item["reason"]
        elif source_family_id in not_selected:
            item = not_selected[source_family_id]
            decision = "not_selected"
            analysis_unit_id = None
            reason = item["reason"]
        else:
            decision = "not_eligible"
            analysis_unit_id = None
            reason = "Standard review completed; no long-form Deep Analysis eligibility remains after Books comparison."
        family_decisions.append(
            {
                "source_family_id": source_family_id,
                "eligibility": eligibility,
                "decision": decision,
                "analysis_unit_id": analysis_unit_id,
                "reason": reason,
            }
        )

    if len(receipts) != base["denominator_count"]:
        raise ValueError("Final receipt count does not match denominator")
    packet = {
        "schema": "daily-evidence-books-final-v2.1",
        "report_date": base["report_date"],
        "coverage_window": base["strict_window"],
        "denominator_count": base["denominator_count"],
        "central_receipts": receipts,
        "closure_reviews": [],
        "deep_analysis_selection": {
            "selected_analysis_units": [
                {
                    "analysis_unit_id": item["analysis_unit_id"],
                    "selected_family": item["source_family_id"],
                    "title": item["reason"].split(":", 1)[0],
                    "reason": item["reason"],
                }
                for item in preaudit["deep_analysis_selection"]["selected"]
            ],
            "family_decisions": family_decisions,
            "selection_result": "pass",
        },
        "books_patch_queue": preaudit["books_patch_queue"],
        "unresolved": [],
        "gate_claim": "Evidence and Books writeback are serialized; Daily remains In Progress until an independent fresh-context Semantic Audit passes all required scopes.",
    }
    if args.write:
        args.output.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print(json.dumps({"date": packet["report_date"], "receipts": len(receipts)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
