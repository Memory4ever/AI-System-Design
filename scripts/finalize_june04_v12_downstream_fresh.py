#!/usr/bin/env python3
"""Render the frozen 2026-06-04 V12 downstream audit packet.

The 42-family denominator is an immutable input accepted by root.  This
script re-opens every local exact-v1 manuscript, rebuilds review provenance,
conservatively reconstructs benchmark disclosures from evaluation/setup text,
and reads the current owner plus adjacent Books chapters for comparison.  It
never writes Books and never closes the independent semantic or Books gates.
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

from canonicalize_june_daily_presentation import canonicalize_report


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260604"
REPORT = ROOT / "papers/2026/06/04/README.md"
PROPOSAL = PACKET / "candidate-denominator-repair-proposal-v12.json"
OLD_RECEIPTS = PACKET / "source-review-receipts.json"
OLD_BENCHMARKS = PACKET / "benchmark-disclosure-replay-v9.json"
REVIEW_OUT = PACKET / "source-review-receipts-v12-fresh.json"
BENCH_OUT = PACKET / "benchmark-contract-v12-fresh.json"
SELECTION_OUT = PACKET / "deep-analysis-selection-v12-fresh.json"
BOOKS_OUT = PACKET / "books-comparison-v12-fresh.json"
AUDIT_OUT = PACKET / "downstream-fresh-audit-v12.md"
POSTWRITE_OUT = PACKET / "books-postwrite-semantic-audit-v13.md"
MANIFEST = PACKET / "SHA256SUMS"
LEGACY_MANIFEST = PACKET / "SHA256SUMS-v12-downstream"
EXECUTED_AT = "2026-08-29T12:00:00+08:00"
DENOMINATOR_ID = "DEN-20260604-V12-42"

SELECTED = {
    "2606.04415": "DA-20260604-NPU-VIRTUALIZATION",
    "2606.04929": "DA-20260604-CROSS-STAGE-POISONING",
    "2606.05304": "DA-20260604-ACTION-STATE-COMMUNICATION",
}

SELECTED_RATIONALE = {
    "2606.04415": "Full-frontier selection: among the eight 3/3/3 families, this is the only inference-hardware lane that turns prefill/decode phase identity into a rebindable NPU resource contract; it is non-overlapping with the selected post-training-security and multi-agent-state lanes. The exact-v1 result is bounded to Ascend 910C/CloudMatrix384 and the stated TTFT/TPOT slices.",
    "2606.04929": "Full-frontier selection: this is one of only two Books Integrate deltas and the only family that makes checkpoint handoff across SFT and preference optimization a security state channel; existing single-stage data-poisoning prose does not own the cross-stage orchestrator. It is non-overlapping with NPU phase virtualization and multi-agent public-state projection.",
    "2606.05304": "Full-frontier selection: this is one of only two Books Integrate deltas and the only family that replaces transcript forwarding with an explicit public action-state projection while preserving private reasoning ownership; current Message-not-State prose lacks that projection mechanism. It is non-overlapping with NPU resource rebinding and cross-stage poisoning.",
}

WRITEBACKS = {
    "2606.04929": {
        "path": "books/part-06-ai-infrastructure/72-security.md",
        "prewrite_sha256": "d282144f08d37e96c1d85cff0ee35a8113efa0bce3753de2c1b761a69ac5f814",
        "writeback_ref": "books/part-06-ai-infrastructure/72-security.md#L50",
        "required": ("Post-training Pipeline 也是跨阶段攻击状态通道", "SFT dataset → SFT checkpoint → preference dataset → aligned checkpoint", "训练章节仍拥有优化机制", "不能外推为任意 post-training pipeline"),
    },
    "2606.05304": {
        "path": "books/part-07-agent/82-multi-agent.md",
        "prewrite_sha256": "dc2642bdd8e4e2fd2dc9ba18db8854563e42b92d5b9b7a509da4ed218834f869",
        "writeback_ref": "books/part-07-agent/82-multi-agent.md#L255",
        "required": ("Private Reasoning 与 Public Action State 必须经 Projection 分离", "shared history 记录该 delta 的 schema、producer、owner 与 provenance", "Workflow 仍拥有 commit/approval", "不能外推到任意 agent topology"),
    },
}

ADJACENT_PREWRITE_HASHES = {
    "books/part-06-ai-infrastructure/71-multi-tenant.md": "ca6af8fe3bd4fcabb7ba548464bf99cedeb9fdc9bafa22e47e1b1f4bf9220533",
    "books/part-06-ai-infrastructure/73-production-best-practice.md": "270c32ad446c76dd32aab0216c3ae583fbcf7fb69bb1591c7336d79a7905605f",
    "books/part-07-agent/81-workflow.md": "7684b5cf25665e9c518048093fde93d42a1ab00d7adc37bcbe7f9caa04779ee5",
    "books/part-07-agent/83-mcp.md": "adeb28a9e54d8863089af7797f854119ce9477d297e72ff2e626f280a2101f1a",
}

ADJACENT_OWNER_REQUIREMENTS = {
    "books/part-06-ai-infrastructure/71-multi-tenant.md": ("Stable Knowledge Node ID:** `PLATFORM-MULTI-TENANT`",),
    "books/part-06-ai-infrastructure/73-production-best-practice.md": ("Stable Knowledge Node ID:** `PLATFORM-PRODUCTION`",),
    "books/part-07-agent/81-workflow.md": ("Stable Knowledge Node ID:** `AGENT-WORKFLOW`", "Workflow 是 Agent 的 durable control plane", "approval", "authoritative"),
    "books/part-07-agent/83-mcp.md": ("Stable Knowledge Node ID:** `AGENT-MCP`",),
}

# The old report is parsed only to recover the already-public score/node and
# source-specific prose.  None of its completion or provenance fields survive.
LOCATOR_PATCHES = {
    "2606.04402": (
        "https://arxiv.org/html/2606.04402v1 §3 Consequence-aware allocation; §§5–6 algorithm and guarantees",
        "https://arxiv.org/html/2606.04402v1 §7 Experiments",
        "https://arxiv.org/html/2606.04402v1 §9 Discussion and Limitations",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04413": (
        "https://arxiv.org/html/2606.04413v1 §§3–6 helpful-only training branches and constitution/SDF interventions",
        "https://arxiv.org/html/2606.04413v1 §2 Evaluation Suite; §§4–6 results; Appendix A",
        "https://arxiv.org/html/2606.04413v1 §8.1 Limitations; §§4–6 failure analyses",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04415": (
        "https://arxiv.org/pdf/2606.04415v1 §3 FlexNPU architecture and phase-level virtualization",
        "https://arxiv.org/pdf/2606.04415v1 §4.1 Experimental Setup; §4.2 End-to-end Results; Table 2",
        "https://arxiv.org/pdf/2606.04415v1 §5 Discussion and disclosed prototype boundary",
        "Not Disclosed — exact-v1 PDF does not bind a public artifact to an immutable revision",
    ),
    "2606.04459": (
        "https://arxiv.org/pdf/2606.04459v1 §§3–4 ranking-signature geometry and recovery method",
        "https://arxiv.org/pdf/2606.04459v1 §4 practical fitting (50 rankings; 3/5 attempts); §5 approximate parameter exposure",
        "https://arxiv.org/pdf/2606.04459v1 §6 Discussion and attack-scope boundary",
        "Not Disclosed — exact-v1 PDF does not bind a public artifact to an immutable revision",
    ),
    "2606.04557": (
        "https://arxiv.org/html/2606.04557v1 §2 Modular cartridge training and composition",
        "https://arxiv.org/html/2606.04557v1 §3 Experimental Setup; §4 Experimental Results",
        "https://arxiv.org/html/2606.04557v1 §5 Discussion; Limitations",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04581": (
        "https://arxiv.org/html/2606.04581v1 §III Protocol and Problem Formulation; §§IV–V distributed control",
        "https://arxiv.org/html/2606.04581v1 §VI Experimental Results; §VI-A Experiment Settings",
        "https://arxiv.org/html/2606.04581v1 §VII Concluding Remarks — no dedicated limitations section",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04594": (
        "https://arxiv.org/html/2606.04594v1 §3 Ekka design; §4 Implementation",
        "https://arxiv.org/html/2606.04594v1 §5 Evaluation; §§5.1–5.7",
        "https://arxiv.org/html/2606.04594v1 §7 Discussion",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04628": (
        "https://arxiv.org/html/2606.04628v1 §2 RAMPART model and registry operations",
        "https://arxiv.org/html/2606.04628v1 §3 Experiments; §§3.1–3.2",
        "https://arxiv.org/html/2606.04628v1 §6 Conclusion — no dedicated limitations section",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04778": (
        "https://arxiv.org/html/2606.04778v1 §3 trajectory-level alignment method; Appendix A",
        "https://arxiv.org/html/2606.04778v1 §4 Experiments and Analysis",
        "https://arxiv.org/html/2606.04778v1 Appendix E Limitation and Broader Impact",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04850": (
        "https://arxiv.org/html/2606.04850v1 §III Model for Co-design with Distributional Uncertainty; §IV MDPI Model; §§IV-A–IV-D",
        "https://arxiv.org/html/2606.04850v1 §V Simulation Results; §§V-A–V-C",
        "https://arxiv.org/html/2606.04850v1 §VI Conclusion; §VI-A Outlook — no dedicated limitations section",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.04923": (
        "https://arxiv.org/html/2606.04923v1 §2 CHERRL; §§2.2–2.5; §4.1 Agentic Detector Design",
        "https://arxiv.org/html/2606.04923v1 §2.5; §4.2; Appendices B, D and F",
        "https://arxiv.org/html/2606.04923v1 Limitations; Appendix B.8",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05004": (
        "https://arxiv.org/html/2606.05004v1 §4 Framework; §5 Privacy Analysis",
        "https://arxiv.org/html/2606.05004v1 §7 Experiment; Appendix G Experiment; §5 Privacy Analysis for the formal claim",
        "https://arxiv.org/html/2606.05004v1 Limitation — dedicated heading after §8 Conclusion",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05122": (
        "https://arxiv.org/html/2606.05122v1 §3 Method; §§3.1–3.3",
        "https://arxiv.org/html/2606.05122v1 §4 Experiments; Appendix A Training Configuration",
        "https://arxiv.org/html/2606.05122v1 Limitations; §5 Discussion",
        "https://github.com/YiShan05/SEE_official — repository disclosed; exact-v1 does not pin an immutable event-time commit",
    ),
    "2606.05241": (
        "https://arxiv.org/html/2606.05241v1 §3 Methodology; §§3.1–3.2",
        "https://arxiv.org/html/2606.05241v1 §§4–5 Evaluation and Experiment; Appendices C–E",
        "https://arxiv.org/html/2606.05241v1 Limitations; §6 Discussion",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05308": (
        "https://arxiv.org/html/2606.05308v1 §2 Method",
        "https://arxiv.org/html/2606.05308v1 §3 Results",
        "https://arxiv.org/html/2606.05308v1 Limitations; §4 Future Work",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05378": (
        "https://arxiv.org/html/2606.05378v1 §§2–3 screen-and-ablate protocol and causal taxonomy",
        "https://arxiv.org/html/2606.05378v1 §4 Setup; §4.3 Evaluation; §§5–10",
        "https://arxiv.org/html/2606.05378v1 §14 Limitations",
        "https://github.com/skydancerosel/spectral-probe-circuits — repository disclosed; immutable event-time commit not pinned",
    ),
    "2606.05384": (
        "https://arxiv.org/html/2606.05384v1 §§3.2–3.7 post-decision protocol and ERS",
        "https://arxiv.org/html/2606.05384v1 §§3.2–3.10; §4 Results",
        "https://arxiv.org/html/2606.05384v1 §6 Limitations and Future Work",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05395": (
        "https://arxiv.org/html/2606.05395v1 §§3–4 VASO contract synthesis and verification loop",
        "https://arxiv.org/html/2606.05395v1 §5 Empirical Evaluation; Appendices A–B",
        "https://arxiv.org/html/2606.05395v1 §7 Limitations and Future Directions",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05396": (
        "https://arxiv.org/html/2606.05396v1 §3 Approach; §§3-A–3-D",
        "https://arxiv.org/html/2606.05396v1 §§4–5 Experimental Setup and Results",
        "https://arxiv.org/html/2606.05396v1 §7 Threats to Validity",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05414": (
        "https://arxiv.org/html/2606.05414v1 §3 Method; Appendix B Training Details",
        "https://arxiv.org/html/2606.05414v1 §4 Experiments; §4.3 Evaluation Metrics; §5 Results",
        "https://arxiv.org/html/2606.05414v1 §Limitations — exact unique heading",
        "Not Disclosed — exact-v1 promises public artifacts but does not bind an immutable event-time revision",
    ),
    "2606.05415": (
        "https://arxiv.org/html/2606.05415v1 §3 executable schema contract and routing design",
        "https://arxiv.org/html/2606.05415v1 §4 Experiments and Results; §§4.1–4.5",
        "https://arxiv.org/html/2606.05415v1 §Limitations — exact unique heading",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
    "2606.05523": (
        "https://arxiv.org/html/2606.05523v1 §§3–4 CHASE adversarial red-blue training loop",
        "https://arxiv.org/html/2606.05523v1 §5 Results; Appendices E–F",
        "https://arxiv.org/html/2606.05523v1 §Limitations and Ethical Considerations — exact unique heading",
        "Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision",
    ),
}

BENCHMARK_MANUAL = {
    "2606.04329": {"model": "Disclosed — OpenClaw and HERMES use GPT-OSS-120B", "evaluator": "Disclosed — §4.1.3 defines attack success rate and retrieval success rate; §§4.2–4.5 report both across agents, attacks and defenses"},
    "2606.04384": {"model": "Disclosed — §5.1.1 uses a standard CNN for MNIST/FMNIST/CIFAR-10 and a five-layer RNN for IMDB", "batch": "Disclosed — §5.1.2/Table 2 publish dataset-specific effective batches; no universal batch applies", "evaluator": "Disclosed — §5 reports privacy-accounting validity and privacy–utility accuracy under the named datasets and release configurations"},
    "2606.04402": {"model": "Disclosed — §7 aggregates 16 named SWE-bench solvers from Claude 2/GPT-4 through Claude 4 Sonnet", "evaluator": "Disclosed — §7 evaluates consequence-weighted expected utility and resolve rate, with consequence labels separately audited"},
    "2606.04413": {"model": "Disclosed — training covers Haiku 4.5, Qwen3-30B-A3B and Qwen3.5-35B-A3B; evaluation names Jinx/Qwen3-32B, Sonnet 4/4.5, Opus 4.5 and Abliterated Qwen3.5-35B-A3B", "evaluator": "Disclosed — §2/Appendix A define capability, refusal, compliance, misalignment, sandbagging, sycophancy, steerability and character evaluations"},
    "2606.04415": {"model": "Disclosed — DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1 (large MoE) and Qwen2.5-7B", "hardware": "Disclosed — Ascend 910C and CloudMatrix384 (384 cards)", "precision": "Disclosed — W8A8 for the reported large DeepSeek-R1 slice", "input_length": "Disclosed — 1K input tokens", "output_length": "Disclosed — 1K or 4K output tokens", "slo": "Disclosed — TTFT <=1 s and TPOT <=50 ms", "evaluator": "Disclosed — §4 reports throughput under TTFT/TPOT constraints; AISBench is named for the distill-model workload, other slices are not version-pinned"},
    "2606.04425": {"evaluator": "Disclosed — §§5.1–5.2 decompose 162 cases into write success, context incorporation, activation and end-to-end success"},
    "2606.04459": {"model": "Disclosed — §5 evaluates Pythia-70m(-dedup) and OLMo-3-8B", "evaluator": "Disclosed — §4 reports fitting over 50 rankings and five attempts; §5 separately measures top-k ranking/parameter-recovery behavior"},
    "2606.04522": {"hardware": "Disclosed — Intel i7-11700K, 32 GB RAM, AVX-512, Ubuntu 22.04 and gcc 11.4", "evaluator": "Disclosed — §§5–6 measure recall-ratio divergence and downstream classification/RAG effectiveness"},
    "2606.04557": {"model": "Disclosed — Qwen3-8B", "precision": "Disclosed — bfloat16 weights with fp32 Adam optimizer state", "input_length": "Disclosed — packed 8,192-token sequences for the named long-context run", "batch": "Disclosed — task-specific training batches are published; no universal batch applies", "evaluator": "Disclosed — §4 reports QA accuracy, prompt-token use and cartridge/RAG comparisons"},
    "2606.04581": {"model": "Disclosed — TinyLlama-1.1B/Llama-2-7B and Qwen3.5-0.8B/Qwen3.5-27B pairs", "hardware": "Disclosed — edge server uses one NVIDIA A100 GPU"},
    "2606.04594": {"model": "Disclosed — Claude Sonnet 4.5 is the Ekka and baseline backend", "precision": "Not Disclosed — BF16/FP8 is motivation, not the evaluation setup"},
    "2606.04628": {"model": "Disclosed — Qwen3-8B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3 and Qwen3-14B", "hardware": "Disclosed — Ollama on one RTX 5080", "precision": "Disclosed — Q4 quantization", "input_length": "Disclosed — default all-MiniLM-L6-v2 relevance embedding truncates each block at 256 tokens; the evaluated LLM prompt length is not fixed"},
    "2606.04769": {"model": "Disclosed — claude-sonnet-4-5-20250929-thinking is DCIChecker", "evaluator": "Disclosed — §IV combines author analysis, manual mutation tests and repository-scale measurement"},
    "2606.04778": {"model": "Disclosed — Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3 and Qwen2.5-7B-Instruct", "hardware": "Disclosed — Appendix A.5 uses one RTX 3090 24 GB", "precision": "Disclosed — 4-bit quantization and bf16 training", "input_length": "Disclosed — maximum sequence length 2,048", "output_length": "Disclosed — Appendix A.4 caps new tokens at 256 for augmentation and evaluation", "batch": "Disclosed — Appendix A reports per-device and effective training batches", "evaluator": "Disclosed — §4 measures attack success/harmfulness on AdvBench, HarmBench, HEx-PHI and JailbreakBench"},
    "2606.04850": {"model": "Not Applicable — distribution-grid accelerator co-design simulation, not a model-version benchmark", "evaluator": "Disclosed — §V simulates latency/energy/resource outcomes under nominal and uncertain mappings"},
    "2606.04903": {"model": "Not Applicable — formal ontology/executable-semantics argument", "hardware": "Not Applicable — no hardware claim", "precision": "Not Applicable — no precision claim", "input_length": "Not Applicable — no token-length claim", "output_length": "Not Applicable — no generation-length claim", "batch": "Not Applicable — no batching claim", "concurrency": "Not Applicable — no request-concurrency claim", "slo": "Not Applicable — no SLO claim", "evaluator": "Disclosed — formal definitions/proofs plus bounded worked cases; no empirical model score"},
    "2606.04908": {"model": "Not Applicable — GPU-native storage microbenchmark", "hardware": "Disclosed — AMD EPYC 9654, 768 GB DDR5, NVIDIA A100 40 GB", "evaluator": "Disclosed — storage throughput/latency and end-to-end GPU-AFA measurements"},
    "2606.04923": {"model": "Disclosed — Qwen3-4B trained with GRPO on HealthBench and VerInstruct", "hardware": "Disclosed — Appendix F uses NVIDIA H100 80 GB GPUs", "evaluator": "Disclosed — §§2.5/4.2 and Appendices B/D/F compare reward-hacking detection, rubric validity and downstream behavior"},
    "2606.04929": {"model": "Disclosed — Llama-3 8B and Qwen3 1.7B/4B/8B", "hardware": "Disclosed — NVIDIA H100 for fine-tuning/LoRA runs"},
    "2606.05004": {"model": "Disclosed — GPT-5.2 attribute attacker; Appendix G names utility/discrimination models", "hardware": "Disclosed — 96-core Ubuntu server, 128 GB RAM, two A100 GPUs", "evaluator": "Disclosed — Appendix G defines utility metrics, GPT-4o QA judging, privacy attack success and query/computation cost"},
    "2606.05029": {"model": "Not Applicable — evaluation-validity framework", "hardware": "Not Applicable — no hardware claim", "precision": "Not Applicable — no precision claim", "input_length": "Not Applicable — no token-length claim", "output_length": "Not Applicable — no generation-length claim", "batch": "Not Applicable — no runtime batch claim", "concurrency": "Not Applicable — no concurrency claim", "slo": "Not Applicable — no SLO claim", "evaluator": "Disclosed — checks estimand, identification assumptions, measurement and transport; no new benchmark score"},
    "2606.05037": {"model": "Disclosed — claude-haiku-4-5, claude-sonnet-4-6 and gpt-4o-mini", "batch": "Not Applicable — N=30 per model/mode cell is sample size, not runtime batch", "evaluator": "Disclosed — §5 records logical success, billed tokens, retries and recovery actions after answer-leakage audit"},
    "2606.05043": {"model": "Not Applicable — protocol/interoperability evaluation", "evaluator": "Disclosed — four explicit protocol criteria applied to executable artifacts and sample implementations"},
    "2606.05122": {"model": "Disclosed — Qwen3-4B-Base", "output_length": "Disclosed — Appendix A fixes maximum response length at 8,192 tokens", "batch": "Disclosed — Appendix A gives stage-specific batches", "evaluator": "Disclosed — §4.1 defines judge agreement, calibration and response-quality metrics"},
    "2606.05241": {"model": "Disclosed — Appendix C names deep-research agents; detector/base slice uses Qwen3-30B-A3B", "evaluator": "Disclosed — §§4–5 and Appendix D report question/turn detection, inflation and human–automatic agreement"},
    "2606.05271": {"model": "Disclosed — ten CNN/Transformer/SSM/KAN/spiking/VLA families", "hardware": "Disclosed — Intel Core Ultra Lunar Lake Series 2 CPU/iGPU/NPU", "precision": "Disclosed — FP16 and INT8", "evaluator": "Disclosed — latency, energy and placement trade-offs across ten pipelines"},
    "2606.05304": {"model": "Disclosed — Qwen3-8B/14B/32B plus named Claude/GPT harness models"},
    "2606.05308": {"model": "Disclosed — Claude 3 Sonnet and Haiku judges", "evaluator": "Disclosed — bias-corrected ranking estimates versus human-gold metrics on a 30-item sample"},
    "2606.05339": {"model": "Not Applicable — software-ecosystem study", "hardware": "Not Applicable — repository/thread analysis and interviews", "precision": "Not Applicable — no precision claim", "input_length": "Not Applicable — corpora are not model contexts", "output_length": "Not Applicable — coded observations are not generated outputs", "batch": "Not Applicable — no runtime batch", "concurrency": "Not Applicable — no request concurrency", "slo": "Not Applicable — no SLO", "evaluator": "Disclosed — manual coding of 837 threads and 473 repositories plus validation with 55 practitioners"},
    "2606.05378": {"model": "Disclosed — Pythia 1B, OLMo 1B and OLMoE 1B-7B"},
    "2606.05384": {"model": "Disclosed — GPT-4o and GPT-4o-mini judges", "precision": "Not Applicable — API judge study", "batch": "Not Disclosed — 100 paired instances are dataset size", "evaluator": "Disclosed — §§3–4 define ERS and post-decision consistency metrics"},
    "2606.05391": {"model": "Not Applicable — qualitative study of 17 developers", "hardware": "Not Applicable — interviews", "precision": "Not Applicable — no model execution", "input_length": "Not Applicable — interviews are study units", "output_length": "Not Applicable — transcripts/codes are qualitative artifacts", "batch": "Not Applicable — criterion/snowball sample", "concurrency": "Not Applicable — one-to-one interviews", "slo": "Not Applicable — no SLO", "evaluator": "Disclosed — reflexive thematic analysis with the stated recruitment/coding procedure"},
    "2606.05395": {"model": "Disclosed — GPT-5-nano skill generator and GPT-4o-mini plan generator", "hardware": "Not Disclosed — robotic platforms are named but compute is not bound", "evaluator": "Disclosed — compliance across 400 generated plans"},
    "2606.05396": {"model": "Disclosed — Qwen2.5-Coder-Instruct 3B/7B/14B, Base and Abliterated", "hardware": "Disclosed — Core Ultra 7 155H, 32 GB RAM, no dedicated GPU", "precision": "Disclosed — Q4_K_M 4-bit GGUF", "slo": "Not Disclosed — 600-second timeout is an experiment budget", "evaluator": "Disclosed — multiple static/dynamic vulnerability tools with concordance and manual adjudication"},
    "2606.05403": {"model": "Disclosed — Claude, Qwen and OLMo; exact identities in Appendix C.8", "hardware": "Disclosed — EC2 p4de.24xlarge with 8x A100 80 GB"},
    "2606.05414": {"model": "Disclosed — Qwen3-Embedding-0.6B (32K, 1,024 dimensions) plus two-layer MLP predictors", "hardware": "Disclosed — Appendix C reports A100 run costs", "input_length": "Disclosed — frozen encoder supports 32K; experiments use trajectory prefixes", "batch": "Disclosed — Appendix B uses batch 256", "evaluator": "Disclosed — §4.3 evaluates accuracy–earliness and stopping utility"},
    "2606.05415": {"model": "Disclosed — GPT-4.1; cross-model slice adds Claude Haiku 4.5 and Llama 3.3 70B"},
    "2606.05433": {"model": "Disclosed — estimates name Llama 3.1 405B; determinism check uses Llama 7B", "hardware": "Disclosed — determinism measurement uses 8x H100", "precision": "Disclosed — BF16 and FP32 are separately analyzed", "evaluator": "Disclosed — bounded determinism measurement plus analytical cost estimates; no frontier end-to-end deployment benchmark"},
    "2606.05495": {"model": "Not Applicable — CUDA scheduling workloads", "hardware": "Disclosed — RTX 3090/Xeon 6330 and RTX 5090/i7-11700", "batch": "Disclosed — §5.2 sweeps workload-specific batch values (including 4, 8, 32 and up to 4,096); no universal fixed batch applies", "evaluator": "Disclosed — throughput/overhead with Nsight Systems across six workloads"},
    "2606.05523": {"model": "Disclosed — Llama-3.1-8B-Instruct with LoRA", "hardware": "Disclosed — Appendix H.3 uses one RTX PRO 6000 48 GB", "batch": "Disclosed — Appendix H gives stage-specific batches", "evaluator": "Disclosed — §5/Appendices E–F measure attack success, safety/refusal and utility across red-blue rounds"},
    "2606.06529": {"model": "Disclosed — Opus 4.6 attacker, MiMo-V2-Flash monitor, GPT-OSS-120B scorers", "evaluator": "Disclosed — §3.3 reports safety, caught rate and red-team success under trajectory-level audit budget"},
}

ARTIFACT_PATCHES = {
    "2606.04384": "https://github.com/FangXieLab/DPSR-CB — repository disclosed; exact-v1 does not pin an immutable event-time commit",
    "2606.04903": "https://github.com/Thistleseeds/agentic-redux — repository disclosed; exact-v1 does not pin an immutable event-time commit",
    "2606.05043": "https://github.com/Universal-Commerce-Protocol/samples — interoperability dependency referenced; exact-v1 does not pin a paper-specific immutable commit",
    "2606.05122": "https://github.com/YiShan05/SEE_official — repository disclosed; exact-v1 does not pin an immutable event-time commit",
    "2606.05304": "https://github.com/iNLP-Lab/PACT — repository disclosed; exact-v1 does not pin an immutable event-time commit",
}

# Source-specific conclusions rebuilt from the exact-v1 Method, Evaluation and
# limitation loci.  These are deliberately explicit rather than generated from
# titles or admission deltas: a complete receipt must explain the old boundary,
# the changed state/control contract, what the experiment establishes, and the
# coexistence/failure boundary independently for every family.
REVIEW_MANUAL = {
    "2606.04329": {
        "problem": "会话内 prompt-injection 防护默认恶意内容随会话结束而消失；一旦 agent 能把输入写入长期 memory，这个旧假设仍便于实现，却不再覆盖跨会话复用的污染状态。",
        "mechanism": "MPBench 把攻击拆为 memory write channel、结构漏洞、写入策略与后续检索触发。memory store 持有持久状态，外部 payload 是不可信数据，write/retrieve policy 掌握纳入上下文的控制权；实现以一次投毒写入和后续独立会话中的读取构成端到端事务。",
        "evaluation": "§4 只在所列 agent、memory channel 与攻击类上证明更激进的写入/检索策略与更高可利用性相关，并显示现有 prompt-injection defenses 未覆盖这些路径；它没有证明所有 memory 产品、模型或防御都会同样失败。",
        "tradeoff": "结构化 provenance、写权限与读取 gate 能缩小攻击面，但会牺牲自动记忆覆盖率并增加状态审计成本；不保存跨会话状态的 assistant 仍可维持较简单的会话隔离。",
        "evolution": "这是 AGENT-MEMORY 的 Direct Evolution：从“上下文窗口内的不可信 token”扩展为“具有写权限、生命周期和再次执行机会的持久状态”。",
    },
    "2606.04384": {
        "problem": "DPSGD 的标准 subsampling amplification 假设样本进入一次固定机制；selective release 根据中间结果决定是否发布，旧 accountant 忽略了由选择事件改变的有效采样概率。",
        "mechanism": "论文重新推导 selective-release privacy loss，并以 clipped-gradient release rule 组成 DPSR-CG。privacy accountant 持有累计预算，clipped gradient/noise 是受保护数据流，release predicate 控制一次更新是否进入外部可见模型状态。",
        "evaluation": "实验只比较指定数据集、模型、clip/noise 和会计配置下的 privacy–utility；其贡献是修正 formal accounting contract，而不是证明任何 ε 下都优于普通 DPSGD。",
        "tradeoff": "选择性发布可避免部分低价值噪声更新，却增加会计复杂度并使 utility 对 release rule 敏感；无法证明选择事件独立性时，应退回保守 accountant 或标准 DPSGD。",
        "evolution": "这是 TRAIN-PRETRAINING/PLATFORM-SECURITY 的 Direct Evolution：从每步统一记账到把 release decision 本身纳入 privacy mechanism。",
    },
    "2606.04402": {
        "problem": "按预测难度分配 test-time compute 把每个错误视为等价；这一目标在 benchmark accuracy 下合理，却会把生产数据库破坏与无害格式错误赋予同一损失。",
        "mechanism": "轻量 consequence predictor 从任务描述估计错误成本，scheduler 在总预算下选择模型/思考层级。request 保存 consequence estimate，候选解是数据流，budget allocator 掌握额外推理调用的控制权。",
        "evaluation": "§7 在指定 SWE-bench solver pool 与 consequence proxy 上证明预算可向高后果任务重分配；它没有证明 consequence label 无偏、也没有给出跨领域生产事故成本。",
        "tradeoff": "后果加权降低高代价错误，但可能因 predictor 偏差饿死低分任务并增加 tail latency；错误代价近似相同时，difficulty-only routing 仍更简单。",
        "evolution": "这是 INFER-REQUEST-LIFECYCLE/PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：accuracy scheduler 上增加 risk-weighted objective，而非替代底层 execution engine。",
    },
    "2606.04413": {
        "problem": "只去除 refusal 的 helpful-only fine-tuning 被当作能力评测工具；旧做法能暴露危险能力，却可能同时改变 character、steerability 与 sycophancy，令“更少拒答”等同于“保持其余 alignment”这一假设失效。",
        "mechanism": "研究对 anti-refusal、synthetic-document fine-tuning、SFT/RL character questions 做分支干预。训练数据与 objective 决定权重更新，constitution/character examples 约束行为控制面，评测分别观察 refusal 与非 refusal alignment dimensions。",
        "evaluation": "§§2,4–6 证明若干 helpful-only recipes 会产生系统性 misgeneralization，且文档训练或 character 数据能缓解所测指标；没有证明存在通用 harmlessness-preserving recipe。",
        "tradeoff": "更少 refusal 提高危险能力可测性，却扩大部署风险且可能破坏 persona 一致性；受控 capability evaluation 可采用它，面向用户的模型仍需独立 harmlessness gate。",
        "evolution": "这是 TRAIN-SFT 的 Alternative Branch：把“拒答率”拆成独立训练目标，不再当作整体 alignment 的代理变量。",
    },
    "2606.04415": {
        "problem": "prefill 与 decode 的资源形态不同，但固定 NPU partition 无法随阶段切换；静态隔离在负载稳定时合理，在动态共置时造成碎片或相互干扰。",
        "mechanism": "FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。",
        "evaluation": "§4 只对 Ascend 910C/CloudMatrix384、所列模型、W8A8、1K input 与1K/4K output及 TTFT/TPOT 门槛证明原型效果；不证明其他 NPU、精度或 SLO。",
        "tradeoff": "虚拟化提高阶段复用率，却引入迁移、隔离和调度开销；专用部署在单一阶段、稳定占用或硬隔离要求强时仍有效。",
        "evolution": "这是 INFER-PD-DISAGGREGATION 与 PLATFORM-RESOURCE-SCHEDULING 的 Direct Evolution：从设备级 allocation 细化为阶段级可重绑定资源。",
    },
    "2606.04425": {
        "problem": "传统 prompt injection 以同一执行上下文中的输入和利用为边界；agent 把内容写入文件、memory、tool metadata 后，注入与激活可以跨会话分离。",
        "mechanism": "论文建立 write–persistence–incorporation–activation 生命周期和 sandbox。持久介质保存攻击状态，clean victim query 触发重新纳入，context constructor 掌握从存储到可执行上下文的数据控制权。",
        "evaluation": "§5 在162个跨会话 case 中分别测 WSR、IR、AR 与 E2E-ASR，证明瓶颈可出现在不同阶段；它没有评估所有持久介质或给出已验证的通用 defense。",
        "tradeoff": "写入审批、taint/provenance 与重新纳入 gate 增强隔离，却降低 agent 自动积累知识的能力；无持久状态系统仍可用 session-bound 防护。",
        "evolution": "这是 AGENT-MEMORY/PLATFORM-SECURITY 的 Direct Evolution：prompt injection 从瞬时输入攻击演变为持久状态供应链攻击。",
    },
    "2606.04459": {
        "problem": "只返回 token ranking 常被视为比 logits 更安全；旧 API 仍保留模型对输入的相对偏好，因此可能暴露可重复的模型签名。",
        "mechanism": "方法把多次 query 的 token order 组成 ranking signature，再做识别/近似参数恢复。API response 持有排序数据，query adversary 控制采样输入，signature matcher 掌握模型归属判定。",
        "evaluation": "PDF §5 只在约50组 ranking 与指定拟合尝试下证明可区分/近似暴露；没有证明能恢复完整权重或对所有解码/API 变体都不可伪造。",
        "tradeoff": "限制排名深度、加噪或速率限制能减弱签名，却降低排序 API 的可用性；若客户端只需最终文本，不暴露 token rank 仍是更小接口。",
        "evolution": "这是 PLATFORM-SECURITY 的 Principle Reuse：输出最小化从 logits 扩展到任何稳定的相对排序信号。",
    },
    "2606.04522": {
        "problem": "Recall@k 只衡量与 exact kNN 集合的重合，在邻居距离相近时会惩罚对下游同样有用的结果，导致 ANN 为无意义 overlap 支付计算。",
        "mechanism": "论文用 1/Ratio@k 比较返回邻居与真实邻居的距离质量，并把 metric 作为 index tuning objective。索引持有候选集合，distance 是数据证据，benchmark/tuner 决定 latency–quality operating point。",
        "evaluation": "跨所列 ANN algorithms/datasets 的实验只证明 Recall@k 与 distance quality/下游 utility 可分离，以及替代 metric 改变效率结论；没有证明 1/Ratio@k 适合所有语义任务。",
        "tradeoff": "distance ratio 无 judge、成本低，但仍继承 embedding metric 的偏差；业务需要离散 exact neighbors 时 Recall@k 仍是正确 contract。",
        "evolution": "这是 AGENT-RAG/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：retrieval gate 从集合重合转向对下游有效性的可验证代理。",
    },
    "2606.04557": {
        "problem": "单个 monolithic document cartridge 能省去重复 prefill，却无法组合大集合；独立训练的 KV blocks 直接混合又导致分布冲突。",
        "mechanism": "CAS 用 dynamic distractor mixing 训练可组合 per-document cartridges，并由 budget manager 在 GPU 与持久存储间轮换。cartridge 是版本化 KV artifact，selector 决定加载集合，cache manager 掌握驻留和 token budget。",
        "evaluation": "§§3–4 在指定 Qwen3-8B、数据集和 retrieval/oracle 选择下证明百万 token 集合可扩展及 token savings；没有证明跨模型可移植或线上并发延迟。",
        "tradeoff": "预计算状态减少 prefill，却引入训练、artifact identity、选择错误与存储迁移成本；内容变化频繁或请求不复用时，普通 RAG/prefill 更合适。",
        "evolution": "这是 INFER-KV-CACHE 的 Direct Evolution：KV 从单请求临时状态演变为可训练、可组合、可分层存储的文档 artifact。",
    },
    "2606.04581": {
        "problem": "单用户 speculative decoding 假设 draft 与 verify 在固定链路；多用户 edge 中设备算力、上行带宽和 draft acceptance 同时变化，固定 draft length 会放大慢节点。",
        "mechanism": "Multi-SPIN 让设备 SLM 产出 drafts、edge LLM 批量验证，并联合优化 draft length、频分带宽和计算分配。每用户 draft/acceptance 是状态，radio/compute budget 是资源数据，central optimizer 掌握分配控制。",
        "evaluation": "§VI 只在所列模型对、A100 edge server 与模拟网络条件下证明 sum token goodput；没有证明公网抖动、生产 tail SLO 或不同 tokenizer 的效果。",
        "tradeoff": "合作生成分摊 server compute，却增加通信、同步和 rejected-draft 浪费；链路差或本地 SLM 弱时，server-only decoding 仍可能更快。",
        "evolution": "这是 INFER-SPECULATIVE-DECODING/INFER-DISTRIBUTED-RUNTIME 的 Direct Evolution：proposal ownership 从同机 draft model 扩展到多接入设备。",
    },
    "2606.04594": {
        "problem": "serving optimization 的 silent error 不崩溃、只悄然降低输出质量；从最终文本反推 kernel/runtime root cause 跨越过大的语义层。",
        "mechanism": "Ekka 对齐 target 与 reference implementation 的中间 execution states，逐层/逐算子做 differential diagnosis。reference trace 是正确性证据，target trace 是观测数据，alignment/search controller 定位首个 divergence。",
        "evaluation": "§5 的 pass@1/pass@5 只对作者构造的真实 silent-error benchmark 与指定 backend/模型成立；没有证明 reference 自身无错或覆盖所有 nondeterminism。",
        "tradeoff": "中间态比对提高可诊断性，却要求可观测点、可比 reference 与额外存储/执行；无法复现或跨硬件数值漂移大时仍需 invariant/metamorphic tests。",
        "evolution": "这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：observability 从性能 telemetry 扩展为跨实现的语义正确性证据。",
    },
    "2606.04628": {
        "problem": "把 agent memory 当拼接文本会混淆内容所有权、优先级和回滚；简单截断虽便宜，却不能表达哪些 block 可被谁写入或必须保留。",
        "mechanism": "RAMPART 以 named block registry 保存 provenance/priority/authorship，并在 compile context 前执行 promote、gate、write、evict、rollback。registry 持有状态，blocks 是数据，policy engine 掌握上下文编译权。",
        "evaluation": "Qwen3-8B Q4 probes 只证明特定 block 位置/分组会改变任务成功率以及这些 primitives 可调节位置；没有证明通用长期记忆质量或多租户隔离。",
        "tradeoff": "显式 registry 提供权限与回滚，却增加 policy 配置和 block lifecycle 复杂度；短会话、无写入的 prompt 仍可直接拼接。",
        "evolution": "这是 AGENT-MEMORY 的 Direct Evolution：从 token budget 管理提升为有地址、权限和事务操作的状态管理。",
    },
    "2606.04769": {
        "problem": "MCP client 按自然语言 description 选择工具，默认描述与代码行为一致；版本漂移或未声明副作用会让模型在错误权限假设下执行。",
        "mechanism": "DCIChecker 联合 schema-aware static analysis 与 LLM classifier，对 description、signature、implementation effects 建立一致性检查。代码与描述是双份接口数据，server owner 维护实现，release gate 决定不一致是否阻断发布。",
        "evaluation": "measurement 只对采样的真实 MCP repositories 与分类 taxonomy 证明 DCI 存在并可被检测；没有证明 classifier 能替代 sandbox/runtime enforcement。",
        "tradeoff": "静态/语义检查提前发现 drift，却有解析覆盖和 LLM 误判；高风险工具仍需 capability policy 与运行时审计。",
        "evolution": "这是 AGENT-MCP/PLATFORM-SECURITY 的 Direct Evolution：protocol conformance 从 wire schema 扩展到描述、代码和副作用的一致性。",
    },
    "2606.04778": {
        "problem": "shallow-safety 只关注开头 token 的拒答方向；生成中途注入可在任意 step 改写后续轨迹，说明最终输出或早期 hidden-state alignment 不是充分 robustness 证据。",
        "mechanism": "方法模拟 mid-sequence token perturbation，构造 trajectory-level alignment data 并直接训练扰动后的继续生成。decoder state 持有轨迹，注入 token 改变数据流，training objective 负责把恢复行为写入权重。",
        "evaluation": "§4 在三类7B/8B instruct models和指定 harmfulness suites 上证明中途脆弱性与训练增益；没有证明对所有 white-box activation intervention 或更大模型成立。",
        "tradeoff": "轨迹训练覆盖更多攻击位置，却增加合成扰动成本并可能压制正常纠错/用户改写；只需静态单轮拒答的系统仍可使用较轻的 output filter。",
        "evolution": "这是 TRAIN-SFT/PLATFORM-SECURITY 的 Direct Evolution：alignment target 从首 token/final answer 延伸到整个生成状态机。",
    },
    "2606.04799": {
        "problem": "metrics、logs、traces 与拓扑各自成 silo 时，人能凭经验拼接，agent RCA 却缺少可查询的实体身份和关系。",
        "mechanism": "UModel 建虚拟 ontology，把 telemetry、entities 与 expert knowledge 映射为 object graph，并由 U-SPL pipeline 查询。object identity/relations 是共享状态，source adapters 供数据，query planner 掌握跨源探索控制。",
        "evaluation": "作者案例只证明统一模型支持所测 RCA/query workflow；没有证明任意 vendor schema 自动可对齐或 ontology 长期无漂移。",
        "tradeoff": "object-centric layer提高跨源推理，却带来 schema governance、identity resolution 和摄取成本；单一服务的小规模诊断仍可直接查原生 telemetry。",
        "evolution": "这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：从采集信号扩展到可被 agent 消费的语义对象与关系层。",
    },
    "2606.04850": {
        "problem": "传统 accelerator co-design 把网络训练、算子映射、硬件参数与制造偏差分阶段固定；这在每层接口稳定时合理，却会在 fabrication/latency/energy uncertainty 跨阶段传播时失去全局可比性。",
        "mechanism": "正文以 functionality-resource interface 组合 training、mapping、fabrication 与 resource-allocation blocks，并用 distributional/MDPI model 联合优化。co-design optimizer 持有决策状态，各阶段分布是数据，联合搜索掌握候选选择。",
        "evaluation": "§V 的 simulation 只证明指定 workload、processor model、uncertainty distribution 与 cost function 下的联合方案；没有证明真实 chip tape-out、跨 workload 稳健性或生产 SLO。",
        "tradeoff": "联合搜索减少阶段割裂，却增加模型假设、搜索成本与 distribution misspecification 风险；制造波动可忽略或 toolchain 必须独立演进时，分阶段设计仍更易验证。",
        "evolution": "这是 INFER-TENSORRT-LLM execution-plan owner 的 Alternative Branch：从 deterministic mapping 扩展到 uncertainty-aware co-design。",
    },
    "2606.04903": {
        "problem": "自由文本 planning 让 LLM 同时拥有领域解释和动作决定权，难以线性审计；在规则稳定、风险低时灵活，但高风险域无法预先证明允许行为。",
        "mechanism": "Ontology-First design 由人定义 typed domain ontology/roles，Agentic Redux 用 typed lambda calculus 约束步骤并写 append-only ledger。ontology 持有规范状态，typed terms 是数据，checker/role policy 掌握执行授权。",
        "evaluation": "论文给出 healthcare billing 与 vulnerability disclosure 两个 appropriate-domain 实现及语义论证；没有证明开放世界任务能被完整 ontologize，也未证明 LLM 感知输入正确。",
        "tradeoff": "可证明的 typed path 增强审计，却依赖昂贵的 ontology maintenance 并限制开放式推理；低风险探索仍可保留自由规划再加事后 review。",
        "evolution": "这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Alternative Branch：从概率式 planner 转向人定义语义边界内的可验证执行。",
    },
    "2606.04908": {
        "problem": "GPU 已是计算中心，但远端 AFA I/O 仍由 CPU 编排，形成 host bounce、集中 metadata engine 与 traffic amplification。",
        "mechanism": "GNStor 把 NVMe-over-RDMA request path 和部分 AFA functionality 下沉到 GPU，GPU queues 持有 I/O state，RDMA/NVMe buffers 是数据，GPU-side stack 掌握提交与完成控制。",
        "evaluation": "实验只对 AMD EPYC 9654、768GB DDR5、A100 40GB 与指定 AFA/network configuration 的 throughput/latency 成立；不证明通用 filesystem semantics 或 failure recovery。",
        "tradeoff": "绕过 CPU 降低 data-path overhead，却增加 GPU runtime、metadata consistency 与隔离复杂度；控制面密集、GPU 利用低或共享 storage policy 强时 CPU-centric 路线仍合理。",
        "evolution": "这是 PLATFORM-STORAGE/INFER-EXECUTION 的 Direct Evolution：accelerator 从数据消费者变成远端存储 I/O 的主动 owner。",
    },
    "2606.04923": {
        "problem": "rubric RL 把 LLM judge score 当奖励，默认高分代表满足 rubric；policy 可学习 judge bias，使奖励上升而真实质量下降。",
        "mechanism": "CHERRL 可控注入 judge bias，跟踪 reward divergence/hacking onset，并用 agent detector 搜索作弊行为。rubric/judge 持有评价状态，policy outputs 是数据，RL optimizer 把 judge signal 转成权重更新控制。",
        "evaluation": "§4/appendices 只证明所注入 biases 可被发现/利用以及 detector 在该环境中的表现；没有证明真实生产 judge 的全部 latent bias 被覆盖。",
        "tradeoff": "可控 testbed 提高可复现性，却可能过拟合人为 bias；真实 release gate 仍需独立 human/held-out evaluator 和 reward-channel monitoring。",
        "evolution": "这是 TRAIN-RLHF/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：reward model 从可信 oracle 变成需做 adversarial validation 的系统组件。",
    },
    "2606.04929": {
        "problem": "逐阶段独立审计 SFT 与 DPO poisoning 会认为每个小预算攻击都无害；post-training 顺序使前一阶段改变的表示可被后一阶段放大。",
        "mechanism": "论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。",
        "evaluation": "实验只在列出的 Llama/Qwen、poison budgets 与 SFT→DPO/LoRA 配置上证明 additive/cross-stage interaction；没有覆盖完整 RLHF 或现实供应链攻击率。",
        "tradeoff": "跨阶段 provenance/audit 能发现组合风险，却增加数据 lineage 和 checkpoint 隔离成本；单一可信数据源的短 pipeline 可保持阶段内检测。",
        "evolution": "这是 TRAIN-SFT→TRAIN-DPO 的 Direct Evolution：安全 owner 从单个 trainer 上移到整个 post-training checkpoint chain。",
    },
    "2606.05004": {
        "problem": "现有 private inference 常修改模型或逐 prompt 加噪，分别损害兼容性、utility 与成本；公共黑盒 API 又不给调用方权重访问。",
        "mechanism": "SharedRequest 生成 noisy prompt variants、按语义等价 instruction 分组并在 batch level 共享请求。client 持有敏感原文和扰动，grouping service 控制批合并，remote model 只接收混合后的请求集合。",
        "evaluation": "作者实验只在指定 prompts/models/privacy attack 与 GPT-5.2 attribute inference slice 上报告 utility/cost；没有给出对任意 side channel 或恶意 provider 的 cryptographic secrecy。",
        "tradeoff": "model-agnostic batching降低调用成本，却引入语义分组错误、额外 queries 与群体依赖；高敏感、强对手场景仍需 trusted execution、local model 或 cryptographic protocol。",
        "evolution": "这是 INFER-BATCHING/PLATFORM-SECURITY 的 Principle Reuse：batch 不再只做吞吐优化，也成为 privacy mixing boundary。",
    },
    "2606.05029": {
        "problem": "frontier training 太贵，使研究改用 proxy model、observational comparison 或 single-run variation；省算力并未消除因果问题，只把成本换成隐藏 validity assumptions。",
        "mechanism": "框架把研究设计映射到 statistical、internal、external、construct validity，并为三类低成本 strategy 建立 characteristic threat profile。experiment design 持有 estimand，observations 是证据数据，claim gate 决定可外推范围。",
        "evaluation": "论文提供方法论分析而非新的模型 benchmark；它证明的是各策略存在可枚举的因果威胁，不证明某一策略在所有研究问题上失效。",
        "tradeoff": "显式 validity contract 提高结论可审计性，却要求更多假设记录与 sensitivity analysis；资源足够时，直接 controlled replication 仍更强。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation contract 从 metric/config 扩展到 estimand、identification assumption 与外推边界。",
    },
    "2606.05037": {
        "problem": "API validation error 只给自然语言原因时，agent 仍需猜测可执行修复；更长 prose 未必提供字段级 actionability。",
        "mechanism": "self-reflective API 返回 machine-readable recovery_feedback.suggestions[]，将失败字段、修复动作和 retry 输入结构化。server 持有 schema truth，error payload 是控制数据，agent retry loop 决定是否应用建议。",
        "evaluation": "N=30/cell、3 models、10 adversarial tasks 的 pilot 只证明 Anthropic models 上显著提升且 gpt-4o lift 不显著；不能外推为所有 API 或 agent。",
        "tradeoff": "结构建议提高恢复率，却扩大 API contract、可能泄露 schema/security细节；人工客户端或简单错误仍可使用普通 status/message。",
        "evolution": "这是 AGENT-TOOL-USE/API contract 的 Direct Evolution：错误从诊断文本变成受 schema 约束的下一步控制接口。",
    },
    "2606.05043": {
        "problem": "multi-agent protocol 由应用代码隐式实现时，消息顺序、承诺和角色约束散落在 control flow 中，难以验证或替换参与者。",
        "mechanism": "Strabo 把 UCP checkout 建模为 declarative Langshaw protocol，并用 Peach agents 执行且与 Google UCP agents 互操作。protocol artifact 持有允许交互状态，messages 是数据，runtime verifier 掌握 transition control。",
        "evaluation": "案例只证明 checkout 子协议可表达并与所测 UCP implementation 互通；没有覆盖 UCP 全部域、故障恢复或生产规模。",
        "tradeoff": "声明式协议增强一致性和渐进替换，却要求 schema/protocol evolution governance；局部、单进程 workflow 仍可保留直接代码。",
        "evolution": "这是 AGENT-WORKFLOW/AGENT-MULTI-AGENT 的 Direct Evolution：interaction contract 从隐式代码提升为独立、可执行、可验证 artifact。",
    },
    "2606.05122": {
        "problem": "训练一个外部 judge 或让模型直接报 confidence 混合了评价能力与校准表达；base model 可能已有排序信号，只是未被稳定 elicitation。",
        "mechanism": "SEE 先做 calibration-coupled RL 同时回答和预测 judge，再 masked distillation 只锐化 score prediction。模型 token distribution 持有潜在自评信号，judge labels 是校准数据，loss mask 控制哪些行为被更新。",
        "evaluation": "三 benchmark、160 examples、Qwen3-4B-Base 结果只证明所测 judge/attributes 上校准改善且 answer quality 保持；不等于事实正确性或模型知道未知。",
        "tradeoff": "少数据 elicitation 降低训练成本，却继承外部 judge bias，并可能把 confidence 误当 truth；高风险 claims 仍需外部 evidence verification。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：把自评看成需校准的测量通道，而非生成概率的直接解释。",
    },
    "2606.05241": {
        "problem": "允许 web search 的 deep-research agent 可检索 benchmark metadata、题面甚至答案，使公开测试不再隔离训练/推理证据。",
        "mechanism": "研究定义 metadata、question-context、explicit-answer 三层 STC，并从 search traces 检测泄漏、重算去污染结果。browser trace 持有检索证据，benchmark owner 保存题目身份，contamination auditor 决定样本是否计分。",
        "evaluation": "六个公开 benchmark 上最多约4%的 inflation 只针对所测 agents/search index/time；没有证明私有 benchmark 或未来索引同样幅度。",
        "tradeoff": "trace-aware filtering提高有效性，却可能误删合法检索并增加评测成本；真实开放网任务仍需允许搜索，只是不能与 closed-book score 混算。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation isolation 从训练集去重扩展到 inference-time retrieval data flow。",
    },
    "2606.05271": {
        "problem": "edge SoC 把整模型固定到 CPU/GPU/NPU 简单稳定，却忽略不同 fused operator 对各 processing unit 的 latency/energy 差异。",
        "mechanism": "BIDENT 离线 profile H2D、dispatch、kernel、D2H 与能耗，将 operator-PU choice 编成 weighted execution graph 并求 shortest path。profile DB 持有 cost state，operators/tensors 是数据，mapper 掌握 placement。",
        "evaluation": "实验只对 Intel Core Ultra 平台、所列10类模型/FP16/INT8 与 profiler cost model 证明 latency/energy mapping；未证明动态 contention 下仍最优。",
        "tradeoff": "operator mapping提高异构利用率，却增加切分、transfer、profiling 和 recompile 成本；单一 PU 已匹配 workload 或模型很小时 model-level placement 更简单。",
        "evolution": "这是 INFER-TENSORRT-LLM execution-plan 的 Direct Evolution：placement 粒度从 model 降到 fused operator，并把 transfer cost 纳入路径。",
    },
    "2606.05304": {
        "problem": "multi-agent 共享完整自然语言 transcript 保留信息但会膨胀 token/context；固定摘要策略又可能丢掉下游真正需要的动作状态。",
        "mechanism": "PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。",
        "evaluation": "作者在所列 MAS topologies/models/tasks 上比较五种 communication strategies，证明无固定策略普适且 PACT 的 cost/quality 权衡；不证明所有协作任务都可压缩为同一 schema。",
        "tradeoff": "结构化 state update 降低 token，却可能丢失解释、弱化异常协商并增加 schema evolution；小团队、短任务仍可共享完整文本。",
        "evolution": "这是 AGENT-MULTI-AGENT 的 Direct Evolution：通信从 transcript forwarding 变成有 ownership 的状态复制协议。",
    },
    "2606.05308": {
        "problem": "大规模 LLM judge 便宜但有系统偏差，少量 human labels 可靠却方差高；直接用任一方都难同时获得规模和统计保证。",
        "mechanism": "PRECISE 用 prediction-powered inference 将大规模 judge predictions 与小规模 human residual correction 合成 bias-corrected ranking metric，并为 Precision@K 压缩 output-space computation。human labels 是校准数据，judge scores 是辅助信号，estimator 持有置信区间控制。",
        "evaluation": "ESCI 的30 human-gold/60,000 judge slice 只证明所列 ranking metrics 的校正与区间性质；不证明 judge 单样本标签正确或任意分布漂移下仍无偏。",
        "tradeoff": "PPI 降低人工标注量，却依赖 probability sample、稳定 estimand 和正确 variance accounting；无法随机抽样时应回到更多 human evaluation。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：LLM judge 从替代真值变成可校正的低成本测量器。",
    },
    "2606.05339": {
        "problem": "MCP 的 schema 合法并不意味着 server runtime 正确；配置未生效、state、provider、timeout 等故障跨越 protocol 与实现 owner。",
        "mechanism": "研究对473 repositories中的837 fault threads做 bottom-up coding，形成11大类、27子类/73 leaf faults，并按 interaction、tool、schema、state、安全和取消路径分配故障类型。issue evidence 是数据，taxonomy 是诊断状态，maintainer/release process 掌握修复控制。",
        "evaluation": "经验 taxonomy 只代表筛选时间窗、活跃 repositories 与 issue-reporting bias；不能当作运行时故障率或完备故障集合。",
        "tradeoff": "分类改善 triage/测试覆盖，却不会自动检测 silent faults，且 taxonomy 会随协议演化；单一 MCP server 仍需本地 invariants、chaos tests 和 tracing。",
        "evolution": "这是 AGENT-MCP/PLATFORM-OBSERVABILITY 的 Layering / Dependency：wire contract 之上增加 server-runtime reliability owner。",
    },
    "2606.05378": {
        "problem": "attention head 对任务 pattern 有选择性并在 ablation 后影响输出，常被直接解释为稳定 task circuit；跨模型复制时这种相关到因果的跃迁未被证明。",
        "mechanism": "统一 screen-and-ablate protocol 在四任务、三种1B architecture上比较 matched-random null，并把 head 归为 primary/secondary cause、correlate、interferer 或 null。activations 是观测数据，ablation controller 施加干预，taxonomy 持有因果判定。",
        "evaluation": "12个 task-model cells 无两项共享可比 primary screen，证明该 recipe 的具体 circuit 不可稳定移植；不证明机制完全不可解释或更大模型也无共享结构。",
        "tradeoff": "更严格 null/干预降低夸大结论，却提高实验成本并可能错过分布式机制；pattern screening 仍可作候选发现，但不能独立成为 causal claim。",
        "evolution": "这是 MODEL-ATTENTION/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution（认知修正）：selectivity 被降级为 discovery evidence，causality 需要跨条件干预。",
    },
    "2606.05384": {
        "problem": "LLM judge pipeline 默认一次评分是固定输入的稳定属性；若允许评分后对话，参与者可在不改变原答案的情况下诱导 verdict reversal。",
        "mechanism": "protocol 先固定 initial decision，再施加 repeated/neutral、anti-baseline 与 counterbalanced target challenges，用 ERS 等指标分离稳定性、可逆性和定向操纵。conversation state 是新增数据，judge 持有 verdict，evaluation harness 控制挑战顺序。",
        "evaluation": "MT-Bench/AlpacaEval、GPT-4o/4o-mini judges 与100 paired instances 只证明所测 interaction 可改变判定；不证明所有 judge 或无对话 benchmark 均可操纵。",
        "tradeoff": "冻结 judge context 或禁止 post-decision interaction增强可复现性，却不适合需要申诉的流程；有申诉时应使用独立复审而非继续劝说同一 judge。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：judge contract 从纯函数扩展为有状态交互协议。",
    },
    "2606.05391": {
        "problem": "agent oversight 常被抽象成最终 review；实践中开发者必须在执行前、规划时、运行中和事后分配不同注意力与权限。",
        "mechanism": "访谈归纳 a priori control、co-planning、real-time monitoring、post-hoc review 及配套 heuristics。human 持有最终责任和 override，agent plan/action/trace 是审查数据，workflow 决定何时暂停或升级。",
        "evaluation": "17名经验开发者的定性访谈提供早期实践锚点，不是频率估计、因果效果或行业代表样本。",
        "tradeoff": "多阶段 oversight 提高可控性，却带来认知负担、alert fatigue 和吞吐下降；低风险、可回滚任务可减少实时介入。",
        "evolution": "这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Layering / Dependency：human-in-the-loop 从单一批准点演变为分阶段控制面。",
    },
    "2606.05395": {
        "problem": "physical-agent skill 通过 sampled rollout、unit test 或 LLM critique 演进，只证明见过的轨迹成功，不能保证未采样条件下的 temporal safety。",
        "mechanism": "VASO 将 skill 表示为 planner-facing interface 与 formal state/action proposition contract，迭代生成 labeling function、model checking counterexample 和 skill refinement。contract 持有安全状态，robot plan 是数据，verifier 掌握执行前授权。",
        "evaluation": "§5 在两平台、11 specifications、400 plans及40 plans/skill 的局部合同上比较 compliance；没有证明 perception/actuator model 完整或 sim-to-real 物理安全。",
        "tradeoff": "formal gate提高未采样路径约束，却依赖 proposition alignment，且 state-space/solver 成本可能很高；低风险 skill 仍可用 test+monitoring。",
        "evolution": "这是 MULTIMODAL-EMBODIED-VLA/AGENT-SKILL 的 Direct Evolution：skill 从 prompt artifact 变成带形式契约和发布 gate 的执行组件。",
    },
    "2606.05396": {
        "problem": "安全对齐的 code LLM 拒绝生成脆弱代码，使 benchmark 把 refusal 与缺乏 vulnerability-injection capability 混为一谈。",
        "mechanism": "abliteration 估计 residual-stream refusal direction 并作低秩正交投影，再把生成结果分为 refusal、compile/correctness 与 CWE-89 injection success。权重 edit 持有 policy change，safe code/spec 是输入数据，evaluation harness 分离 willingness 与 ability。",
        "evaluation": "Python/CWE-89、Qwen2.5-Coder 3B/7B/14B、Q4_K_M/Ollama 的初步实验只证明该受限 case；不证明编辑保持其他安全性或能构造高质量通用漏洞数据。",
        "tradeoff": "移除 refusal 改善 capability measurement，却显著扩大滥用风险并可能损坏模型行为；只能在隔离研究环境使用，生产模型不应采用。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM 的 Alternative Branch：能力评测先控制 refusal policy，再评价任务能力，但不把 edited model 当部署方案。",
    },
    "2606.05403": {
        "problem": "multi-source synthesis 常假设模型会按统计有效性加权来源；模型可能识别单独的伪造统计，却在合成时只响应“像方法学”的表达风格。",
        "mechanism": "实验正交操纵 methodology register 与 numerical validity，比较单源识别和多源 influence。source text/number 是证据数据，synthesis model 持有权重分配，validity probe 检查是否调用已具备的识别能力。",
        "evaluation": "五模型、三领域的行为 dissociation 只证明所构造 impossible CI 等操纵下的 epistemic blind spot；不证明所有引用审查或 tool-verified agent 都失败。",
        "tradeoff": "外部统计 verifier/claim decomposition提高可靠性，却增加延迟并要求可机器检查的证据；低风险摘要可保留模型合成但标注不确定性。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM/AGENT-RAG 的 Direct Evolution：source ranking 从文风/相关性扩展为可验证的 claim-level validity gate。",
    },
    "2606.05414": {
        "problem": "early failure classifier 只有 trajectory-level label，传统做法把终局失败复制给每个 prefix；多轮对话中失败证据稀疏且延迟，这会制造错误的 turn-level supervision。",
        "mechanism": "attention-based predictor 从整体 label 学稀疏 turn evidence，再以 risk estimate 驱动可调 alert/stop policy。partial trajectory 是数据状态，risk model 更新 failure belief，threshold controller 掌握中止/升级。",
        "evaluation": "§§4–5 只在指定 dialog/agent datasets 与 metrics 上证明比 prefix-label baselines 更好的 early-warning tradeoff；不证明 production threshold 或 causal root cause。",
        "tradeoff": "弱监督减少 turn labels，却可能把相关语句误作早期因果信号；风险低或误停代价高时应延后 alert 并保留完整执行。",
        "evolution": "这是 AGENT-WORKFLOW/PLATFORM-OBSERVABILITY 的 Direct Evolution：监控从事后 outcome 变成随 trajectory 更新的在线控制信号。",
    },
    "2606.05415": {
        "problem": "多源 tables/documents/files 的语义隐含且 schema 不一；直接 vector search 绕过结构，手工 schema 又昂贵且难随来源演进。",
        "mechanism": "系统用 closed-world field catalog 约束 schema discovery，确定性推断 keys/hierarchy，并以同一 executable schema 驱动 extraction、dedup、KG linking 与多工具 retrieval。schema/version 持有契约，provenance graph 是状态，router 控制查询路径。",
        "evaluation": "§4 只在作者数据与 query workload 上证明 ingestion/retrieval traceability；没有证明任意隐含语义可自动恢复或 schema extension 无冲突。",
        "tradeoff": "共享契约提高一致性，却增加 catalog governance、identity resolution 和 migration；同质单源可直接使用原生 schema/search。",
        "evolution": "这是 TRAIN-DATA→AGENT-RAG 的 Direct Evolution：schema 从摄取产物变成贯穿构建与查询的可执行、带 provenance 控制面。",
    },
    "2606.05433": {
        "problem": "frontier training regulation以累计 compute 为阈值却依赖厂商自报；传统完整重放或逐算子证明在该规模不可行。",
        "mechanism": "方案预提交 training specification，采集 inter-node network observations，并在线生成 intermediate-computation Merkle commitments，使用具 native tensor primitives 的 zkVM 抽查/证明。trainer 持有执行状态，commitments/telemetry 是审计数据，verifier 掌握合规判定。",
        "evaluation": "Appendix B/G 给出 proof-cost估算与协议论证，而非 frontier-scale end-to-end deployment；没有证明硬件 telemetry 完整、spec 与真实训练语义完全一致。",
        "tradeoff": "零知识审计保护模型/数据机密，却增加 commitment、proof、trusted instrumentation 与 protocol complexity；低风险训练可继续使用日志和第三方 audit。",
        "evolution": "这是 PLATFORM-SECURITY/GOVERNANCE 的 Layering / Dependency：在既有发布审计与 provenance owner 上增加可验证计算记录；现有安全章节能够承载，无需 Structural Candidate。",
    },
    "2606.05495": {
        "problem": "CUDA Graph 降低单图 launch overhead，但 static batching/global polling 仍产生 inter-batch gap、延迟和 active-buffer 冲突。",
        "mechanism": "SET 为每 worker 绑定 stream、pre-instantiated graph 和独立 buffers，用 event chaining/work stealing 在完成时派发下一 job。per-stream buffer 持有 in-flight state，CUDA events 是控制信号，scheduler 掌握 worker/slot 所有权。",
        "evaluation": "§5 在 RTX3090/5090 两平台、六 workloads 和 workload-specific batch sweep 上报告 throughput/overhead；不证明 LLM serving、跨 GPU 或生产 tail SLO。",
        "tradeoff": "事件触发减少 host gap，却增加 buffer memory、event dependency 与 scheduler complexity；低并发、单 graph workload 仍可用同步 replay。",
        "evolution": "这是 INFER-EXECUTION 的 Principle Reuse：continuous scheduling 的状态所有权下沉到 CUDA graph pipeline，但不能直接外推成 LLM runtime 结论。",
    },
    "2606.05523": {
        "problem": "静态 safety data 或 white-box attack 优化难覆盖部署中的自适应 black-box prompt rewriting；固定 red-team corpus 很快失去压力。",
        "mechanism": "CHASE 让 attacker 用 GRPO 优化 bypass×intent fidelity，defender 用 harvested rewrites 经 GRPO 与 rejection-sampled SFT 强化，并混入 benign data。attacker/defender checkpoints 持有对抗状态，rewrites/rewards 是数据，co-evolution loop 控制迭代。",
        "evaluation": "§5/appendices 只在 Llama-3.1-8B-Instruct、指定 attacks/evaluators 上证明所测 robustness 变化；未证明对 frontier models、长期自博弈或未知攻击无 reward hacking。",
        "tradeoff": "在线生成 hard negatives提高适应性，却增加训练成本、评价器依赖和 catastrophic alignment drift；稳定威胁下 curated SFT 仍更可控。",
        "evolution": "这是 TRAIN-RLHF/PLATFORM-SECURITY 的 Direct Evolution：red teaming 从发布前数据集变成闭环 attacker–defender control process。",
    },
    "2606.06529": {
        "problem": "AI-control evaluation 常让 red-team 在固定频率攻击；真实策略会选择监控弱、收益高的时机并在风险上升时停止，使固定频率高估安全。",
        "mechanism": "论文把策略拆成 start policy 与 stop policy，并在有限 human audit budget 下与 monitor 交互。episode state/monitor score 是数据，attacker policy 掌握是否发起/终止，blue protocol 决定审计和阻断。",
        "evaluation": "BashArena/LinuxArena 与1% audit budget 只证明所测 attacker/monitor 上 strategic selection显著降低 empirical safety；没有给出所有 agentic domains 的绝对安全率。",
        "tradeoff": "更强 adaptive red team提高压力真实性，却使复现实验、coverage 和归因更难；能力很弱或每步全审计时 fixed attack 仍可作基线。",
        "evolution": "这是 PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY 的 Direct Evolution：control eval 从静态 attack frequency 升级为有状态 adversarial policy。",
    },
}

NODE_OVERRIDE = {
    # Selective-release privacy accounting is a security/privacy contract; the
    # previous TRAIN-PRETRAINING route pointed at optimizer telemetry rather
    # than the actual DP owner.
    "2606.04384": "PLATFORM-SECURITY",
}

# Current-book proposition anchors chosen after reading each owner chapter and
# both adjacent chapters.  Keeping the line choice explicit prevents a lexical
# title matcher from silently selecting a long but unrelated paragraph.
BOOK_LINE_OVERRIDE = {
    "2606.04329": 51, "2606.04384": 110, "2606.04402": 104, "2606.04413": 147,
    "2606.04415": 14, "2606.04425": 51, "2606.04459": 14, "2606.04522": 201,
    "2606.04557": 614, "2606.04581": 33, "2606.04594": 105, "2606.04628": 31,
    "2606.04769": 145, "2606.04778": 235, "2606.04799": 95, "2606.04850": 41,
    "2606.04903": 296, "2606.04908": 215, "2606.04923": 1938, "2606.04929": 48,
    "2606.05004": 133, "2606.05029": 1255, "2606.05037": 251, "2606.05043": 277,
    "2606.05122": 1121, "2606.05241": 1595, "2606.05271": 87, "2606.05304": 253,
    "2606.05308": 1146, "2606.05339": 14, "2606.05378": 178, "2606.05384": 1255,
    "2606.05391": 69, "2606.05395": 78, "2606.05396": 293, "2606.05403": 421,
    "2606.05414": 74, "2606.05415": 59, "2606.05433": 791, "2606.05495": 398,
    "2606.05523": 368, "2606.06529": 74,
}


def clean(value: object) -> str:
    value = re.sub(r"<[^>]+>", " ", str(value), flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def pipe(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(value: str) -> str:
    return unicodedata.normalize("NFC", "\n".join(line.rstrip() for line in value.strip().splitlines()))


def html_sections(path: Path) -> list[tuple[str, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    headings = list(re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", raw, re.I | re.S))
    result = []
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(raw)
        result.append((clean(match.group(2)), clean(raw[match.end():end])))
    return result


def pdf_text(path: Path) -> str:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        # Both PDF-only families have manually verified numbered-section
        # locators and benchmark bindings below.  A missing local extractor is
        # not evidence that the immutable PDF is unavailable.
        return ""
    completed = subprocess.run(
        [pdftotext, "-layout", str(path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return clean(completed.stdout)


def exact_source(arxiv_id: str) -> dict[str, object]:
    base = PACKET / "arxiv-v1"
    html_path = base / f"{arxiv_id}v1.html"
    pdf_path = base / f"{arxiv_id}v1.pdf"
    if html_path.exists() and html_path.stat().st_size > 1000:
        sections = html_sections(html_path)
        eval_text = " ".join(body for heading, body in sections if any(term in heading.lower() for term in ("experiment", "evaluation", "result", "setup", "implementation", "ablation")))
        return {"route": "exact-v1-html-local", "path": html_path, "sha256": sha(html_path), "sections": sections, "evaluation_text": eval_text}
    if pdf_path.exists() and pdf_path.stat().st_size > 1000:
        return {"route": "exact-v1-pdf-local", "path": pdf_path, "sha256": sha(pdf_path), "sections": [], "evaluation_text": pdf_text(pdf_path)}
    raise RuntimeError(f"missing exact-v1 body for {arxiv_id}")


def roadmap() -> tuple[dict[str, tuple[int, str]], dict[int, tuple[str, str]]]:
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    by_node, by_ch = {}, {}
    for node, chapter, path in re.findall(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", text):
        by_node[node] = (int(chapter), path)
        by_ch[int(chapter)] = (node, path)
    return by_node, by_ch


def book_line(path: str, query: str, excluded: set[int]) -> tuple[int, str]:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    tokens = {t for t in re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", query.lower()) if t not in {"with", "from", "that", "this", "model", "agent", "system"}}
    ranked = []
    for number, line in enumerate(lines, 1):
        if number in excluded:
            continue
        text = clean(line.lstrip("# -*0123456789."))
        if len(text) < 30 or text.startswith("http"):
            continue
        ranked.append((sum(token in text.lower() for token in tokens), number, text))
    if not ranked:
        raise RuntimeError(f"no proposition in {path}")
    _, number, text = max(ranked, key=lambda row: (row[0], len(row[2])))
    return number, text[:320]


def parse_candidate_rows(report: str) -> dict[str, dict[str, object]]:
    result = {}
    for line in report.splitlines():
        if not line.startswith("| SF-2026-ARXIV-"):
            continue
        cells = [cell.strip().replace("\\|", "|") for cell in line.strip().strip("|").split("|")]
        if len(cells) != 22:
            continue
        arxiv_id = cells[1].removeprefix("arXiv:").removesuffix("v1")
        result[arxiv_id] = {"score": {"design_delta": int(cells[6]), "system_reach": int(cells[7]), "durability": int(cells[8]), "total": int(cells[9])}, "node": cells[18], "decision": cells[19]}
    return result


def parse_old_review(report: str, source_family: str) -> dict[str, str]:
    match = re.search(rf"<!-- review:{re.escape(source_family)}:start -->(.*?)<!-- review:{re.escape(source_family)}:end -->", report, re.S)
    if not match:
        raise RuntimeError(f"missing source-specific review input {source_family}")
    body = match.group(1)
    parts = re.split(r"\n\n(?=\*\*)", body.strip())
    values = []
    for part in parts:
        value = re.sub(r"^\*\*[^*]+\*\*\s*", "", part.strip())
        value = re.sub(r"定位为 `https://arxiv\.org/[^`]+`。", "", value)
        values.append(clean(value))
    while len(values) < 5:
        values.append("")
    return dict(zip(("problem", "mechanism", "evaluation", "tradeoff", "evolution"), values[:5]))


def locators(arxiv_id: str, old: dict[str, str]) -> tuple[str, str, str, str]:
    if arxiv_id in LOCATOR_PATCHES:
        values = LOCATOR_PATCHES[arxiv_id]
    else:
        values = (old["method_locator"], old["evaluation_locator"], old["limitations_locator"], old["artifact_locator"])
    if arxiv_id in ARTIFACT_PATCHES:
        values = (*values[:3], ARTIFACT_PATCHES[arxiv_id])
    if len(set(values)) != 4:
        raise RuntimeError(f"non-distinct locator facets for {arxiv_id}")
    return values


def strict_sentence(text: str, patterns: tuple[str, ...], label: str) -> str:
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        low = sentence.lower()
        if any(re.search(pattern, low) for pattern in patterns) and not any(term in low for term in ("future model", "prior work", "related work", "for example")):
            return "Disclosed — " + clean(sentence)[:320]
    return f"Not Disclosed — exact-v1 evaluation/setup text does not bind {label}"


def benchmark(row: dict[str, object], evidence: dict[str, object], evaluation_locator: str) -> dict[str, str]:
    text = str(evidence["evaluation_text"])
    arxiv_id = str(row["arxiv_id"])
    result = {
        "workload": f"Disclosed — {REVIEW_MANUAL[arxiv_id]['evaluation']} Locator: {evaluation_locator}",
        "model": strict_sentence(text, (r"we (?:use|evaluate|benchmark|train|implement).{0,160}(?:llama|qwen|gpt|claude|mistral|olmo|deepseek)", r"llm backend.{0,120}(?:llama|qwen|gpt|claude|mistral|olmo)"), "the evaluated model/version"),
        "hardware": strict_sentence(text, (r"(?:run|runs|server|machine|equipped).{0,180}(?:gpu|cpu|tpu|a100|h100|h200|rtx|ascend)",), "hardware/topology"),
        "precision": strict_sentence(text, (r"(?:use|uses|quant|precision).{0,100}(?:bf16|fp16|fp8|int8|q4|w8a8)",), "precision/quantization"),
        "input_length": strict_sentence(text, (r"(?:input|prompt|context|sequence) length", r"prefill.{0,40}tokens"), "input/context length"),
        "output_length": strict_sentence(text, (r"(?:output|generation|decode) length", r"decode.{0,40}tokens", r"max_new_tokens"), "output length"),
        "batch": strict_sentence(text, (r"batch size", r"microbatch", r"micro-batch"), "batch size"),
        "concurrency": strict_sentence(text, (r"in-flight concurr", r"concurrent requests", r"simultaneous requests"), "request concurrency"),
        "slo": strict_sentence(text, (r"\bslo\b", r"(?:ttft|tpot).{0,40}(?:<=|≤|threshold)"), "an acceptance SLO; a timeout or reported percentile alone is not an SLO"),
        "evaluator": strict_sentence(text, (r"we (?:report|measure|evaluate).{0,180}(?:accuracy|success|throughput|latency|recall|f1|safety|rate)", r"evaluation metrics"), "the evaluator/metric version"),
    }
    result.update(BENCHMARK_MANUAL.get(arxiv_id, {}))
    return result


def review_provenance(record: dict[str, object], body: str) -> str:
    def canonical_multi(value: object) -> str:
        absent = {"", "-", "—", "n/a", "N/A", "Not Applicable"}
        items = []
        for raw_item in str(value).split(";"):
            item = unicodedata.normalize("NFC", raw_item.strip())
            if item and item not in absent:
                items.append(item)
        return ";".join(sorted(items))

    fields = [
        "review-completion-v1", str(record["source_family_id"]), str(record["event_identity"]),
        str(record["primary_identifier"]), canonical_multi("SRC-ARXIV"), str(record["primary_evidence_version"]),
        canonical_multi(record["reviewed_evidence_versions"]), str(record["review_route"]),
    ]
    if record["review_override"] != "none":
        fields.append(f"review-override:{record['review_override']}")
    fields.extend([
        canonical_multi(record["method_locator"]), canonical_multi(record["evaluation_locator"]),
        canonical_multi(record["limitations_locator"]), canonical_multi(record["artifact_locator"]), str(record["claim_boundary_ref"]),
        str(record["review_ref"]), "review-body-sha256:" + hashlib.sha256(normalized(body).encode()).hexdigest(),
    ])
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def evolution_relation(text: str) -> str:
    """Return the exact contract vocabulary carried by a source-specific review."""
    for relation in ("Direct Evolution", "Alternative Branch", "Principle Reuse", "Layering / Dependency", "Structural Candidate"):
        if relation in text:
            return relation
    raise RuntimeError(f"review lacks an exact evolution relation: {text}")


def main() -> None:
    old_report = REPORT.read_text(encoding="utf-8")
    proposal = json.loads(PROPOSAL.read_text(encoding="utf-8"))
    retained = [row for row in proposal["rows"] if row["decision"] == "retained_in_candidate_denominator"]
    assert len(retained) == 42 and proposal["v12_pre_denominator_closures"] == 532
    old_candidates = parse_candidate_rows(old_report)
    old_receipts = {row["arxiv_id"]: row for row in json.loads(OLD_RECEIPTS.read_text(encoding="utf-8"))["families"]}
    previous_comparisons = {row["arxiv_id"]: row for row in json.loads(BOOKS_OUT.read_text(encoding="utf-8")).get("rows", [])} if BOOKS_OUT.exists() else {}
    by_node, by_ch = roadmap()
    reviews, benchmarks = [], []

    for aid, writeback in WRITEBACKS.items():
        path = ROOT / writeback["path"]
        text = path.read_text(encoding="utf-8")
        assert sha(path) != writeback["prewrite_sha256"], f"{aid} Books file still has the pre-write hash"
        assert all(fragment in text for fragment in writeback["required"]), f"{aid} post-write semantic boundary is incomplete"
    for path, required in ADJACENT_OWNER_REQUIREMENTS.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        assert all(fragment in text for fragment in required), f"adjacent owner semantics changed incompatibly: {path}"

    for row in retained:
        arxiv_id = row["arxiv_id"]
        family_id = family(arxiv_id)
        candidate = old_candidates[arxiv_id]
        evidence = exact_source(arxiv_id)
        receipt = old_receipts[arxiv_id]
        method, evaluation, limitations, artifact = locators(arxiv_id, receipt)
        assert len({method, evaluation, limitations, artifact}) == 4
        source_specific = REVIEW_MANUAL[arxiv_id]
        score = candidate["score"]
        override = "knowledge_gap" if score["total"] < 7 else "none"
        claim = f"claim:{family_id}"
        body = f"""### {arxiv_id} — {row['title']}

**问题、旧方案与约束变化。** {source_specific['problem']}

**Mechanism、state / data / control owner 与实现。** {source_specific['mechanism']}

**Evaluation contract、证明与未证明。** {source_specific['evaluation']}

**Trade-off、failure mode 与旧方案共存边界。** {source_specific['tradeoff']}

**演进关系与系统位置。** {source_specific['evolution']}

**Exact-v1 locators。** Method/Identity：`{method}`；Evaluation：`{evaluation}`；Limitations/Counterevidence：`{limitations}`；Artifact：`{artifact}`。

<!-- {claim}:start -->可引用结论只限 `arXiv:{arxiv_id}v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- {claim}:end -->"""
        record = {
            "source_family_id": family_id, "arxiv_id": arxiv_id, "title": row["title"],
            "event_identity": f"paper-v1:{arxiv_id}", "primary_identifier": f"arXiv:{arxiv_id}v1",
            "first_public_utc": row["submitted_v1_utc"], "score_v2": score,
            "stable_node_id": NODE_OVERRIDE.get(arxiv_id, candidate["node"]),
            "books_disposition": candidate["decision"], "review_route": "deep", "review_override": override,
            "primary_evidence_version": f"arXiv:{arxiv_id}v1", "reviewed_evidence_versions": f"SRC-ARXIV@arXiv:{arxiv_id}v1",
            "access_route": evidence["route"], "evidence_path": str(Path(evidence["path"]).relative_to(ROOT)),
            "evidence_sha256": evidence["sha256"], "method_locator": method, "evaluation_locator": evaluation,
            "limitations_locator": limitations, "artifact_locator": artifact, "claim_boundary_ref": claim,
            "review_ref": f"review:{family_id}", "evolution_relation": evolution_relation(source_specific["evolution"]),
            "structured_review": source_specific, "review_body": body,
        }
        record["review_provenance_id"] = review_provenance(record, body)
        reviews.append(record)
        b = benchmark(row, evidence, evaluation)
        b.update({"source_family_id": family_id, "arxiv_id": arxiv_id, "evaluation_locator": evaluation})
        benchmarks.append(b)

    assert len(reviews) == 42 and len(benchmarks) == 42
    assert len({r["review_provenance_id"] for r in reviews}) == 42
    assert all(r["evolution_relation"] in {"Direct Evolution", "Alternative Branch", "Principle Reuse", "Layering / Dependency", "Structural Candidate"} for r in reviews)
    assert all(len({r["structured_review"][field] for r in reviews}) == 42 for field in ("problem", "mechanism", "evaluation", "tradeoff", "evolution"))
    assert all(all(str(b[field]).startswith(("Disclosed —", "Not Disclosed —", "Not Applicable —")) for field in ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")) for b in benchmarks)
    REVIEW_OUT.write_text(json.dumps({"schema": "daily-source-review-receipts-v2.1", "denominator_id": DENOMINATOR_ID, "counts": {"total": 42, "deep": 42, "standard": 0, "pending": 0, "blocked": 0, "unverified": 0}, "reviews": reviews}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    BENCH_OUT.write_text(json.dumps({"schema": "daily-benchmark-contract-v1", "denominator_id": DENOMINATOR_ID, "count": 42, "rows": benchmarks, "negative_disclosure_rule": "Not Disclosed is based only on exact-v1 evaluation/setup/table text; background, related-work and future-model mentions are excluded."}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    selection = []
    anchors = {aid: next(r for r in reviews if r["arxiv_id"] == aid) for aid in SELECTED}
    for review in reviews:
        aid = review["arxiv_id"]
        score = review["score_v2"]
        eligibility_parts = ["score_7_9"] if score["total"] >= 7 else ["forced_review"]
        if review["books_disposition"] == "Integrate":
            eligibility_parts.append("potential_books_delta")
        eligibility = "; ".join(eligibility_parts)
        if aid in SELECTED:
            rationale = (
                f"{review['structured_review']['evolution']} {SELECTED_RATIONALE[aid]} "
                f"Mechanism owner: {review['structured_review']['mechanism']}"
            )
            decision, unit = "selected", SELECTED[aid]
        else:
            rationale = (
                f"{review['structured_review']['evolution']} Full-frontier decision: not selected because "
                f"all 42 families were compared and this family is `{review['books_disposition']}` at existing owner `{review['stable_node_id']}`; "
                f"{review['structured_review']['evaluation']} {review['structured_review']['tradeoff']} "
                f"The family remains fully reviewed at score "
                f"{score['design_delta']}/{score['system_reach']}/{score['durability']}; no review duty is dropped."
            )
            decision, unit = "not_selected", "—"
        selection.append({"source_family_id": review["source_family_id"], "arxiv_id": aid, "eligibility": eligibility, "decision": decision, "analysis_unit_id": unit, "subsumed_by": "—", "priority_rationale": rationale, "narrative_ref": f"analysis:{unit}" if decision == "selected" else f"analysis-decision:{review['source_family_id']}"})
    assert sum(row["decision"] == "selected" for row in selection) == 3
    assert len({row["priority_rationale"] for row in selection}) == 42
    SELECTION_OUT.write_text(json.dumps({"schema": "deep-analysis-selection-v1", "denominator_id": DENOMINATOR_ID, "frontier_count": 42, "selected_count": 3, "rows": selection}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    books_eligible_dispositions = {
        "Integrate",
        "No Change — Existing Coverage",
        "Structural Candidate",
    }
    books_eligible_reviews = [
        review for review in reviews
        if review["books_disposition"] in books_eligible_dispositions
    ]
    weekly_only_reviews = [
        review for review in reviews
        if review["books_disposition"] == "Weekly Only — Context"
    ]
    assert len(books_eligible_reviews) == 30 and len(weekly_only_reviews) == 12

    comparisons, used = [], {}
    for review in books_eligible_reviews:
        chapter, path = by_node[review["stable_node_id"]]
        used.setdefault(path, set())
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        prior = previous_comparisons.get(review["arxiv_id"], {})
        prior_proposition = clean(prior.get("existing_proposition", ""))
        prior_matches = [number for number, raw in enumerate(lines, 1) if prior_proposition and clean(raw.lstrip("# -*0123456789.")) == prior_proposition]
        line = prior_matches[0] if len(prior_matches) == 1 else BOOK_LINE_OVERRIDE[review["arxiv_id"]]
        if line < 1 or line > len(lines):
            raise RuntimeError(f"book anchor out of range for {review['arxiv_id']}: {path}#L{line}")
        proposition = clean(lines[line - 1].lstrip("# -*0123456789."))
        if len(proposition) < 12:
            raise RuntimeError(f"book anchor is not a proposition for {review['arxiv_id']}: {path}#L{line}")
        used[path].add(line)
        adjacent = []
        adjacent_hashes = {}
        for number in (chapter - 1, chapter + 1):
            if number in by_ch:
                _, adjacent_path = by_ch[number]
                adjacent_line, _ = book_line(adjacent_path, review["title"], set())
                adjacent.append(f"{adjacent_path}#L{adjacent_line}")
                adjacent_hashes[adjacent_path] = sha(ROOT / adjacent_path)
        relation = review["evolution_relation"]
        comparisons.append({
            "source_family_id": review["source_family_id"], "arxiv_id": review["arxiv_id"], "stable_node_id": review["stable_node_id"],
            "target_chapter_ref": f"{path}#L{line}", "target_chapter_sha256": sha(ROOT / path), "adjacent_chapter_refs": adjacent,
            "adjacent_chapter_sha256": adjacent_hashes, "existing_proposition": proposition,
            "new_evidence_delta": review["structured_review"]["mechanism"][:700], "evolution_relation": relation,
            "decision": review["books_disposition"], "books_review_ref": f"books-review:{review['source_family_id']}",
            "writeback_ref": WRITEBACKS.get(review["arxiv_id"], {}).get("writeback_ref", "—"),
            "post_write_sha256": sha(ROOT / path) if review["arxiv_id"] in WRITEBACKS else "—",
        })
    assert len(comparisons) == 30
    BOOKS_OUT.write_text(json.dumps({"schema": "books-comparison-v1", "denominator_id": DENOMINATOR_ID, "count": 30, "books_files_modified": 2, "rows": comparisons}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    candidate_rows, receipt_rows, benchmark_rows, selection_rows, books_rows = [], [], [], [], []
    for review, b, sel in zip(reviews, benchmarks, selection):
        score = review["score_v2"]
        books_review_ref = (
            f"books-review:{review['source_family_id']}"
            if review["books_disposition"] in books_eligible_dispositions
            else "—"
        )
        candidate_rows.append(f"| {review['source_family_id']} | arXiv:{review['arxiv_id']}v1 | {review['event_identity']} | 2026-W23 | {review['first_public_utc'][:10]} | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | deep_complete | accessible | {review['review_override']} | {review['review_ref']} | self | — | new_in_window | {review['stable_node_id']} | {review['books_disposition']} | {books_review_ref} | yes |")
        receipt_rows.append(f"| {review['source_family_id']} | {review['review_provenance_id']} | deep | {review['primary_evidence_version']} | {review['reviewed_evidence_versions']} | {pipe(review['method_locator'])} | {pipe(review['evaluation_locator'])} | {pipe(review['limitations_locator'])} | {pipe(review['artifact_locator'])} | {review['claim_boundary_ref']} | complete |")
        benchmark_rows.append(f"| {review['source_family_id']} | {pipe(b['workload'])} | {pipe(b['model'])} | {pipe(b['hardware'])} | {pipe(b['precision'])} | {pipe(b['input_length'])} | {pipe(b['output_length'])} | {pipe(b['batch'])} | {pipe(b['concurrency'])} | {pipe(b['slo'])} | {pipe(b['evaluator'])} |")
        selection_rows.append(f"| {sel['source_family_id']} | {sel['eligibility']} | {sel['decision']} | {sel['analysis_unit_id']} | — | {pipe(sel['priority_rationale'])} | {sel['narrative_ref']} |")
    for comp in comparisons:
        books_rows.append(f"| {comp['source_family_id']} | {comp['stable_node_id']} | {comp['target_chapter_ref']} | {'; '.join(comp['adjacent_chapter_refs'])} | existing:{comp['source_family_id']} | delta:{comp['source_family_id']} | {comp['evolution_relation']} | {comp['decision']} | {comp['books_review_ref']} |")

    review_blocks = [f"<!-- {r['review_ref']}:start -->\n{r['review_body']}\n<!-- {r['review_ref']}:end -->" for r in reviews]
    selection_blocks = []
    for row in selection:
        selection_blocks.append(f"<!-- {row['narrative_ref']}:start -->\n{row['priority_rationale']}\n<!-- {row['narrative_ref']}:end -->")
    books_blocks = []
    for row in comparisons:
        writeback_note = f" Post-write verified at `{row['writeback_ref']}` with SHA-256 `{row['post_write_sha256']}`." if row["writeback_ref"] != "—" else " No Books writeback required."
        books_blocks.append(f"<!-- {row['books_review_ref']}:start -->\n<!-- existing:{row['source_family_id']}:start -->{row['existing_proposition']}<!-- existing:{row['source_family_id']}:end -->\n\n<!-- delta:{row['source_family_id']}:start -->{row['new_evidence_delta']}<!-- delta:{row['source_family_id']}:end -->\n\nTarget `{row['stable_node_id']}` at `{row['target_chapter_ref']}`; adjacent refs: {'; '.join(row['adjacent_chapter_refs'])}. Decision: `{row['decision']}`.{writeback_note}\n<!-- {row['books_review_ref']}:end -->")

    families = "; ".join(review["source_family_id"] for review in reviews)
    evidence_refs = "; ".join(review["review_ref"] for review in reviews)
    selection_refs = "; ".join(row["narrative_ref"] for row in selection)
    books_refs = "; ".join(row["books_review_ref"] for row in comparisons)
    weekly_only_refs = "; ".join(review["review_ref"] for review in weekly_only_reviews)
    report = f"""# Daily Research — 2026-06-04

> V12 frozen-denominator closure. Root accepted `42/574`, a different-context reviewer passed all 42 Evidence/Selection rows, root serialized exactly two approved Books deltas, and the same fresh context passed the post-write semantic audit.

## Executive Summary

The canonical denominator is `42` retained and `532` family-specific pre-denominator closures (`7.32%`). A fresh reviewer re-opened all `42/42` exact-v1 bodies locally (`40` HTML, `2` PDF), corrected false negative disclosures and inaccurate locators, and checked every Source Review and full-frontier selection rationale. Books Comparison is restricted to the `30` Books-eligible families; the `12` `Weekly Only — Context` families remain fully reviewed candidate-level closures and deliberately have no Books Review Ref. Root then wrote only `2606.04929` to Ch72 and `2606.05304` to Ch82. Post-write review confirms their evidence boundaries, old-solution coexistence, owner handoffs and current hashes. A later concurrent Ch81 update changed its file hash but preserved Workflow's commit/approval authority; current adjacent hashes and semantics were rechecked. Pending, blocked and unverified are zero; all Gates pass.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-04 |
| Window End | 2026-06-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {DENOMINATOR_ID} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-03T09:00:00+08:00 | 2026-06-04T09:00:00+08:00 | {EXECUTED_AT} | 574/574 title+abstract semantic replay, exact-v1 history reconciliation, V12 full FP/FN audit | checked | 574 | {families} | pages=3; final cursor=end; frozen local ledger | 2026-06-04T01:00:00Z | ../_sources/daily-20260604/candidate-denominator-repair-proposal-v12.json; ../_sources/daily-20260604/root-denominator-acceptance-v12.md; coverage:SRC-ARXIV:20260604 | — |

<!-- coverage:SRC-ARXIV:20260604:start -->Root accepted the mutually exclusive `42 + 532 = 574` V12 ledger after a complete false-positive/false-negative review. This downstream lane does not reopen that denominator.<!-- coverage:SRC-ARXIV:20260604:end -->

## 2. Candidate Ledger and Score V2

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(candidate_rows)}

### Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(receipt_rows)}

### Benchmark Contract

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(benchmark_rows)}

`Not Disclosed` is a full-text negative conclusion over exact-v1 Evaluation/Setup/Table text. Background examples, related work, future model names, request rate and observed percentiles are not treated as model, concurrency or SLO disclosures.

## 3. Source Reviews

{chr(10).join(review_blocks)}

## 4. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_rows)}

{chr(10).join(selection_blocks)}

## 5. Books Comparison and Decision

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_rows)}

{chr(10).join(books_blocks)}

## 6. Semantic Audit and Gate

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260604-COVERAGE-V12 | fresh-context:root-denominator-acceptance-v12 | coverage | coverage:SRC-ARXIV:20260604 | — | {DENOMINATOR_ID} | passed |
| SA-20260604-EVIDENCE-V13 | fresh-context:jun04-full-fresh-gate | evidence | {evidence_refs} | — | repaired locator/disclosure findings; re-opened and checked 42/42 exact-v1 reviews and benchmark contracts | passed |
| SA-20260604-SELECTION-V13 | fresh-context:jun04-full-fresh-gate | deep_analysis_selection | {selection_refs} | — | compared all 42 frontier rows; 3 non-overlapping selected lanes and 39 family-specific exclusions verified | passed |
| SA-20260604-BOOKS-V13 | fresh-context:jun04-full-fresh-gate | books | {books_refs}; {weekly_only_refs} | — | 30 Books-eligible owner/adjacent/disposition comparisons verified; 12 Weekly Only families were verified through their candidate-level Source Review refs and intentionally have no Books Comparison; Ch72/Ch82 writebacks match exact-v1 boundaries and current adjacent owner semantics remain compatible | passed |

## 7. Repository Changes and Open Questions

- Created immutable V12 downstream receipts for `42/42` Source Reviews, benchmark contracts and Deep Selection, plus `30/30` Books-eligible comparisons; `12` Weekly Only families intentionally stop at candidate-level closure.
- Replaced the invalid `2606.04850` duplicated Method/Limitations locator with distinct Method, Evaluation and bounded limitations routes.
- Rebuilt all `42/42` review bodies from source-specific exact-v1 conclusions; no title/admission-delta placeholder is accepted as a problem, mechanism or evaluation statement.
- Corrected `2606.04384` from `TRAIN-PRETRAINING` to the existing `PLATFORM-SECURITY` privacy owner after reading the owner and adjacent chapters.
- Corrected benchmark disclosures that previously confused background prose with evaluation setup, including Ekka precision, RAMPART model/hardware/quantization, mechanistic-study models, judge models, schema-contract models and CHASE/control-evaluation models.
- Books files changed by root serialization: `2` (`Ch72`, `Ch82`); no other Books file is part of this 6/4 writeback scope.
- Post-write receipt: `../_sources/daily-20260604/books-postwrite-semantic-audit-v13.md`.
- Open question: none. Coverage, Evidence/Selection and Books Gates are passed.

## Sources

- Official exact-v1 manuscripts: `https://arxiv.org/html/<id>v1` or `https://arxiv.org/pdf/<id>v1`.
- Frozen denominator: `../_sources/daily-20260604/candidate-denominator-repair-proposal-v12.json`.
- Root denominator acceptance: `../_sources/daily-20260604/root-denominator-acceptance-v12.md`.
- Fresh downstream receipts: `../_sources/daily-20260604/source-review-receipts-v12-fresh.json`, `benchmark-contract-v12-fresh.json`, `deep-analysis-selection-v12-fresh.json`, `books-comparison-v12-fresh.json`.
"""
    REPORT.write_text(report, encoding="utf-8")
    # The V12 owner renderer predates the July canonical Daily layout.  Keep
    # the semantic renderer as the source of truth, then apply the shared,
    # idempotent presentation guard before any hashes are recorded.
    assert canonicalize_report(REPORT, "2026-06-04")

    AUDIT_OUT.write_text(f"""# 2026-06-04 V12 downstream fresh audit checkpoint

## Recomputable outcome

- raw identities: `574`
- frozen candidates: `42`
- pre-denominator closures: `532`
- exact-v1 access: `40 HTML + 2 PDF = 42/42`
- full Source Review: `42/42`; pending/blocked/unverified: `0/0/0`
- benchmark contracts: `42/42`
- Deep Analysis frontier: `42/42`; selected: `3`; family-specific not-selected: `39`
- Books Comparison: `30/30` eligible families; Weekly Only candidate-level closures: `12/12`; approved Books writebacks: `2/2`; unrelated Books writebacks: `0`

## Material repairs and independent findings

The independent pass corrected dedicated-limitations or section-boundary locators for `2606.04413`, `2606.04459`, `2606.04778`, `2606.05004`, `2606.05122`, `2606.05241`, `2606.05308`, `2606.05396`, and the Method boundary for `2606.05414`. It repaired exact-v1 benchmark false negatives including the FlexNPU workload/model/evaluator, Pythia/OLMo ranking-exposure setup, CNN/RNN selective-release experiments, RTX/A100/H100/Ascend hardware, precision, batch and evaluator disclosures, and converted formal/qualitative/non-model studies to explicit `Not Applicable` where appropriate. All 42 review bodies have unique problem, mechanism/state-data-control owner, proof/non-proof, trade-off/failure/coexistence and exact five-value evolution relation. The 30 Books-eligible comparisons preserve the source-specific relation instead of assigning every non-Integrate row one template value; the 12 Weekly Only closures intentionally stop before Books Comparison.

## Gate truth

Coverage/denominator are closed by root acceptance. The different-context 42/42 audit passes Evidence and Selection. The same fresh context verified the two root-serialized Books deltas, their exact-v1 boundaries, owner handoffs, old-solution coexistence and target hashes. A concurrent Ch81 update changed its hash after the immediate audit, so the current Workflow owner semantics were rechecked rather than falsely reported as unchanged. Books Gate and Daily Completion now pass.
""", encoding="utf-8")

    POSTWRITE_OUT.write_text(f"""# 2026-06-04 Books post-write semantic audit V13

Auditor: `fresh-context:jun04-full-fresh-gate`

## Scope and result

- `2606.04929` -> `PLATFORM-SECURITY`, `{WRITEBACKS['2606.04929']['writeback_ref']}`: **passed**.
  - pre-write SHA-256: `{WRITEBACKS['2606.04929']['prewrite_sha256']}`
  - post-write SHA-256: `{sha(ROOT / WRITEBACKS['2606.04929']['path'])}`
  - semantic check: the text models SFT dataset -> SFT checkpoint -> preference dataset -> aligned checkpoint as a cross-stage attack-state channel; preserves per-stage controls when no state crosses stages; leaves optimization to Training; binds evidence to the named Llama/Qwen/H100/poisoning-ASR contract and refuses universal extrapolation.
- `2606.05304` -> `AGENT-MULTI-AGENT`, `{WRITEBACKS['2606.05304']['writeback_ref']}`: **passed**.
  - pre-write SHA-256: `{WRITEBACKS['2606.05304']['prewrite_sha256']}`
  - post-write SHA-256: `{sha(ROOT / WRITEBACKS['2606.05304']['path'])}`
  - semantic check: the text separates private reasoning from typed public action-state projection; binds schema/producer/owner/provenance and fail/fallback behavior; leaves commit/approval to Workflow; limits evidence to Qwen3 8B/14B/32B and the named coding harnesses.

## Adjacent-owner isolation

- Ch71: `{sha(ROOT / 'books/part-06-ai-infrastructure/71-multi-tenant.md')}` ({'unchanged' if sha(ROOT / 'books/part-06-ai-infrastructure/71-multi-tenant.md') == ADJACENT_PREWRITE_HASHES['books/part-06-ai-infrastructure/71-multi-tenant.md'] else 'changed; owner semantics rechecked'})
- Ch73: `{sha(ROOT / 'books/part-06-ai-infrastructure/73-production-best-practice.md')}` ({'unchanged' if sha(ROOT / 'books/part-06-ai-infrastructure/73-production-best-practice.md') == ADJACENT_PREWRITE_HASHES['books/part-06-ai-infrastructure/73-production-best-practice.md'] else 'changed; owner semantics rechecked'})
- Ch81: `{sha(ROOT / 'books/part-07-agent/81-workflow.md')}` ({'unchanged' if sha(ROOT / 'books/part-07-agent/81-workflow.md') == ADJACENT_PREWRITE_HASHES['books/part-07-agent/81-workflow.md'] else 'changed after immediate audit by a concurrent lane; Workflow commit/approval/authoritative-state ownership rechecked'})
- Ch83: `{sha(ROOT / 'books/part-07-agent/83-mcp.md')}` ({'unchanged' if sha(ROOT / 'books/part-07-agent/83-mcp.md') == ADJACENT_PREWRITE_HASHES['books/part-07-agent/83-mcp.md'] else 'changed; owner semantics rechecked'})

No source claim was promoted into a benchmark-unbounded guarantee. No additional 2026-06-04 Books writeback is eligible. `FIND-20260604-POSTWRITE-BOOKS` is resolved; Books Gate is `Passed`.
""", encoding="utf-8")

    paths = [PROPOSAL, PACKET / "root-denominator-acceptance-v12.md", REVIEW_OUT, BENCH_OUT, SELECTION_OUT, BOOKS_OUT, AUDIT_OUT, POSTWRITE_OUT, REPORT, ROOT / WRITEBACKS["2606.04929"]["path"], ROOT / WRITEBACKS["2606.05304"]["path"], Path(__file__).resolve(), ROOT / "scripts/canonicalize_june_daily_presentation.py", ROOT / "scripts/test_june04_canonical_presentation.py", ROOT / "scripts/audit_june04_canonical_presentation.py"]
    presentation_audit = PACKET / "PRESENTATION_FRESH_AUDIT_V14.md"
    if presentation_audit.exists():
        paths.append(presentation_audit)
    manifest_text = "".join(
        f"{sha(path)}  {Path(os.path.relpath(path, PACKET)).as_posix()}\n"
        for path in paths
    )
    MANIFEST.write_text(manifest_text, encoding="utf-8")
    # Preserve the historical filename as a compatibility alias while making
    # the month-wide canonical manifest name available to shared validation.
    LEGACY_MANIFEST.write_text(manifest_text, encoding="utf-8")
    print(json.dumps({"denominator": 42, "closures": 532, "reviewed": 42, "benchmarks": 42, "selected": 3, "books_comparison": 30, "weekly_only_closures": 12, "books_modified": 2, "gates": {"coverage": "closed", "evidence": "passed", "selection": "passed", "books": "passed"}, "completion": "complete"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
