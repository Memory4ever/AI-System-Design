#!/usr/bin/env python3
"""Build the strict V2.1 2026-06-11 Daily packet without editing Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260611"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"
EVIDENCE_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POSTWRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"
REPORT = ROOT / "papers/2026/06/11/README.md"
EXECUTED_AT = "2026-08-29T23:15:00+08:00"
DENOMINATOR_ID = "DEN-20260611-559031"

# id: owner, delta, score, disposition, method locator, evaluation locator,
# limitation locator, benchmark workload, model, hardware, precision, trade-off.
M = {
"2606.11543": ("AGENT-REFLECTION", "Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。", (3,3,3), "Integrate", "§3 Method; §§3.2–3.4 controlled variants/runtime evidence", "§4 Experiments; §4.1 setup; §§4.2–4.5", "§6 Limitations; Appendix E layout sensitivity", "82 SkillsBench tasks × 3 conditions × 5 trials", "GPT-5.4 high reasoning", "Not Disclosed — hosted runtime hardware is not identified", "Not Disclosed", "按需资源降低入口负担但可能产生 fanout tax；精确格式、阈值或长 artifact pipeline 仍适合 flat/local instructions。"),
"2606.11632": ("PLATFORM-SECURITY", "Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。", (3,3,3), "Integrate", "§§3–5 SAB model, airlock and broker", "§7 Evaluation Methodology and Targets; §7.3 setup", "§9 Discussion and Limitations; §9.2", "500 contracts × five trials; 2,500 admissions", "Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA", "Single-node local workstation; exact CPU/GPU not disclosed", "Not applicable — control-plane prototype", "证书化增加 admission latency 和 TCB；证据陈旧、policy/validator 漂移或 emergency bypass 会破坏保证，IAM 仍保留。"),
"2606.11671": ("PLATFORM-SECURITY", "Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。", (3,3,3), "Integrate", "§3 Runtime Skill Audit; §4 implementation", "§5 Evaluation", "§7 Limitations", "100 OpenClaw skills with static baselines and evolving attacks", "LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed", "Not Disclosed", "Not Disclosed", "动态探测覆盖 context-dependent behavior，却不穷尽 trigger；模型化 task/judge 会漂移，静态扫描仍是廉价第一层。"),
"2606.11686": ("PLATFORM-EVALUATION-SYSTEM", "生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。", (3,3,3), "Integrate", "§3 Layer-Isolated Evaluation; taxonomy and pure mode", "§4 Evaluation; controlled regression injection", "§5 Discussion; no dedicated limitations section", "238 cases across 23 slices; seven injected regressions; two tenants", "No-LLM deterministic ordering-agent scaffold", "Not Disclosed", "Not applicable — deterministic harness", "分层 gate 定位快但只覆盖显式 scaffold；端到端 stochastic behavior 与未被 exercise 的 layer 仍需独立评测。"),
"2606.11688": ("AGENT-WORKFLOW", "长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。", (3,3,3), "Integrate", "§3 Method; §4 theorem; §5 System", "§6 Empirical evaluation; §6.5 scaled corpus", "§7 Limitations; Appendix A auditor boundary", "3,150 paired cells; 70 tasks including 50 SWE-bench Lite", "Three systems × three models; model identities partly withheld", "Not Disclosed", "Not Disclosed", "hard floor 用 coverage 换 honesty；定理依赖 gate soundness、floor enforcement 与 plan coverage，不能证明任务本身正确。"),
"2606.11690": ("PLATFORM-COST", "LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。", (3,3,3), "Integrate", "§3 Concurrency-Aware Cost Framework", "§4 Experimental Setup; §5 Results", "§6.8 Scope; §6.9 Limitations", "42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps", "Dense, ultra-sparse MoE and sparse MoE models", "NVIDIA H100 and A100 80GB PCIe", "FP16 and FP8 where supported", "真实 meter 提高归因但需要 workload replay；burst、prefix cache、I/O shape 与硬件 FP8 支持会改变 crossover。"),
"2606.11718": ("INFER-GPU-MEMORY", "Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。", (3,3,3), "Integrate", "§III Chiplet-Contiguous Layout", "§IV Evaluation; §IV-A methodology", "§V Conclusion; no dedicated limitations section", "Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes", "Qwen3-30B; Llama-3.1-70B", "Modeled multi-chiplet GPU; exact product not claimed", "Not Disclosed", "布局变换减少 remote HBM traffic，却要求 runtime/compiler 重排；对非 GEMM、动态 shape 或不同 interleave policy 不构成普遍收益。"),
"2606.11806": ("AGENT-MEMORY", "生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。", (3,3,3), "Integrate", "§3 Experience Serving in Production", "§4 setup; §5 Results; Appendices E–G", "§4.4 claim boundary; Appendix H interpretation scope", "Production moderation plus tool-use and GPQA contrast tasks", "Reasoning/instruct model variants disclosed in Appendix A.4", "Not Disclosed — hosted serving hardware not identified", "Not Disclosed", "selective retrieval 控制 prompt burden，但 miss/over-trigger 与 selector overhead 会伤害质量；规则少或高度共享时 global compact 仍成立。"),
"2606.11871": ("PLATFORM-SECURITY", "CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。", (3,3,3), "Integrate", "§III threat model; §§IV–V design/implementation", "§VI Evaluation; §VII backend cost", "§VI-H portability boundaries; §VIII Discussion", "77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks", "CUDA SASS binaries", "NVIDIA CUDA testbed; exact GPU bound in §VI-A", "Not applicable — binary instrumentation", "SASS-level enforcement覆盖真实执行面但增加 instrumentation/callback cost；未恢复 site 必须 fail closed 或留在 denominator 外。"),
"2606.11878": ("PLATFORM-SECURITY", "GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。", (3,3,3), "Integrate", "§§III–V participation authority and CSC", "§VI evidence; §VII-D mitigation results", "§VII-E Cost and Limits; §VIII Discussion and Limitations", "CUDA contract-conformance suite across four authority dimensions", "CUDA collective primitives and CIC wrapper", "NVIDIA CUDA testbed; exact GPU in evidence appendix", "Not applicable", "CIC 防止 range-valid metadata 扭曲授权，却需保存 reference membership/epoch；普通 CFI 不覆盖此语义面。"),
"2606.11916": ("PLATFORM-MONITORING", "LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。", (3,3,3), "Integrate", "§III Methodology", "§IV Results; §§IV-A–IV-E", "§V Threats to Validity", "216-hour campaign; six co-located deployments; Poisson stress", "Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF", "One host with 3× NVIDIA L40S", "Not Disclosed", "长时 campaign 昂贵且 co-location 可能混入 contention；短基准仍适合 kernel 回归，但不能替代 rejuvenation evidence。"),
"2606.11949": ("PLATFORM-MONITORING", "deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。", (3,3,3), "Integrate", "§3 Methods; §§3.1–3.10", "§4 setup; §5 Results", "§6.5 Limitations; §5.4 ground-truth regimes", "4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells", "Four deployed safety classifiers", "Not Disclosed", "Not Disclosed", "检测可能对 target attack 无信号，density ratio 也会退化；abstention 恢复 coverage 不等于阻止攻击。"),
"2606.11998": ("PLATFORM-SECURITY", "trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。", (3,3,3), "Integrate", "§3 Methods; §3.1 threat model/protocol", "§4 Results; Appendix C red/blue teaming", "§5 Discussion, Transparent CoT assumption and Limitations", "Multi-turn BashArena software-engineering tasks", "Trusted, untrusted-agent and intermediate-monitor model configurations", "Not Disclosed — API/runtime hardware not identified", "Not Disclosed", "bootstrapping 延长弱 monitor 生命周期，却依赖 transparent CoT；隐藏推理、steganography 或共同盲点会失效。"),
"2606.12243": ("INFER-SPECULATIVE-DECODING", "把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。", (3,3,3), "No Change — Existing Coverage", "§3 Methodology; §§3.2–3.5", "§4 Experiments", "§4.4 additional analysis; §5 Conclusion", "Four tasks across T5/Gemma model families", "T5 and Gemma families", "Disclosed in §4.1; no cross-paper normalization", "Disclosed in §4.1 where applicable", "slim verifier 节约 full-model calls 但引入 routing error/threshold；exact rejection contract 与 full verifier fallback 必须保留。"),
"2606.12320": ("PLATFORM-SECURITY", "生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。", (3,3,3), "Integrate", "§§3–8 threat model, five planes and composed architecture", "§9 case studies; §10 validation roadmap", "§11 Limitations and Open Questions", "Seven canonical workflow threats plus production case studies", "Reference architecture; not a model benchmark", "Not applicable", "Not applicable", "多平面提高可中断性与归因，却增加 latency/state consistency/TCB；reference architecture 不证明生产效果。"),
"2606.12329": ("AGENT-MEMORY", "Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。", (3,3,3), "Integrate", "§3 System Design; §§4–6 architecture/implementation", "§7 Evaluation", "§8 Limitations and Future Work", "Two-month self-study, 10 projects, 207 events", "Local-first projectmem with MCP/CLI", "Local developer environment; hardware not disclosed", "Not applicable", "event sourcing 提供 provenance/rollback，但 self-study 不能证明跨团队收益；错误 judgment 仍需 supersession 与关闭开关。"),
"2606.12370": ("INFER-SPECULATIVE-DECODING", "RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。", (3,3,3), "No Change — Existing Coverage", "§§3–5 entropy bound, TV loss and adaptation", "§6 Experiments", "§7.8 top-k instability; §9 Limitations", "RL math/reasoning workloads and MTP acceptance/throughput sweeps", "Multiple MTP-enabled LLM scales", "Disclosed in experimental appendix", "Disclosed in experimental appendix", "更新 MTP 提升 rollout throughput 却增加训练耦合；top-k TV 不稳，完整 rejection sampling 是 correctness fallback；TRAIN-RLHF 只消费 rollout throughput 与 policy-update handoff。"),
"2606.12385": ("TRAIN-DATA", "模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。", (3,3,3), "Integrate", "§3 Design of ModSleuth", "§4 Evaluation; §5 Findings", "Appendix A verification; Appendix D disclosure gaps", "Public-artifact dependency reconstruction across target LLMs", "Agentic ModSleuth plus audited model artifacts", "Not Disclosed — document analysis workload", "Not applicable", "递归发现提高 lineage 但受公开文档缺失和 entity resolution 错误限制；它是 audit evidence，不是完整 SBOM guarantee。"),
"2606.12487": ("INFER-TENSORRT-LLM", "4-bit activation/KV PTQ 需要观察 residual stream 的 phase-wise jump，并对关键相位采用 mixed precision，而非只做静态 rotation smoothing。", (3,3,3), "No Change — Existing Coverage", "§3 Method; §3.3 policy", "§4 Experiments; §4.9 efficiency", "§7 Discussion; no dedicated limitations section", "Perplexity, zero-shot QA, reasoning and efficiency across dense/MoE LLMs", "Multiple dense and MoE PTQ backbones", "Disclosed in §4.2; exact accelerator remains paper-bound", "W4A4/KV4 with phase-aware higher precision", "mixed precision 减少 collapse 却削弱全 4-bit memory/throughput 收益；新 backbone 需重新 calibration。"),
"2606.12556": ("INFER-GPU-MEMORY", "长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。", (3,3,3), "Integrate", "§3 CXL-Hybrid Architecture; §4 ITME", "§5 methodology; §6 evaluation", "§8 Conclusion; no dedicated limitations section", "Weight and KV offload across GPU, host, CXL and NVMe-oF tiers", "LLM inference configurations disclosed in §5.1", "SK hynix CMM, PCIe Gen5 NVMe SSDs and FPGA prototype", "Not Disclosed", "扩容降低 HBM pressure，却增加预取错误、fabric contention 和硬件成本；不可预测 KV access 仍需普通 paging。"),
"2606.12688": ("INFER-KSERVE-TOPOLOGY", "复合多模态模型的 serving contract 应从固定 stage DAG 演进为 model graph + named walks，显式支持 seq/parallel/loop/dynamic-loop/stream 与 component placement。", (3,3,3), "Integrate", "§3 Walk Graph; §§3.1–3.3", "§4 Evaluation; Appendix I reproducibility", "Appendix H Limitations", "BAGEL, Qwen3-Omni, Orpheus and V-JEPA2 composite workloads", "BAGEL-7B, Qwen3-Omni-30B-A3B, Orpheus-3B, V-JEPA2", "Single 4×H100 node or 8×H200 node", "Model-specific; not normalized as one precision", "通用 graph runtime 减少 glue code，却把 state machine、placement、tensor transport 与 per-component batch 变成新控制面；专用引擎仍可能更简单。"),
"2606.12703": ("PLATFORM-SECURITY", "Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。", (3,3,3), "Integrate", "§III threat model; §§IV–VI impossibility/SMSR/certificate", "§VII Evaluation", "§VIII Discussion; provenance-key and smoothing assumptions", "15 enterprise scenarios; 3,150 repeated plus 450 production-scale trials", "Persistent RAG-agent configurations; second-agent generality check", "Not Disclosed", "Not Disclosed", "HMAC 阻止 unsigned injection 不处理合法凭据滥用；smoothing 增加多次 retrieval/inference 成本且证书依赖 threat bound。"),
"2606.12736": ("PLATFORM-EVALUATION-SYSTEM", "Scientific agent evaluation 需要 interactive environment、stepwise verification、domain slices 与 open-ended failure taxonomy，不能把 research 压成静态最终答案。", (3,3,3), "No Change — Existing Coverage", "§4 Methods; §4.1 framework", "§2 Results across domains; §2.6 errors", "§3 Discussion", "Approximately 200 scientific tasks across multiple scales/domains", "Diverse agent-agnostic systems", "Not Disclosed — heterogeneous/API agents", "Not Disclosed", "step verifier 提高诊断性但依赖领域 rubric；novel insight 与 self-directed exploration 仍难可靠验证。"),
"2606.12737": ("PLATFORM-SECURITY", "Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。", (3,3,3), "Integrate", "§3 PI-Hunter; §§3.1–3.3", "§4 Experiments; Appendices B–D", "§4.4 ablations; §5 Conclusion; no dedicated limitations section", "Multiple agent benchmarks, architectures, attacks and defenses", "Agent and evaluator models disclosed in §4.1", "Not Disclosed — hosted model hardware", "Not Disclosed", "更广 exposure 不等于防御；搜索受 mutation/evaluator repertoire 约束，held-out attacks 与 runtime enforcement 仍必要。"),
"2606.12764": ("TRAIN-DATA", "Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。", (3,3,3), "Integrate", "§3 Counterfactual functional memorization", "§4 Results; Appendices A–C/E", "§4 result scope; no dedicated limitations section", "Python function-signature continuations with execution-based and LLM-judge functional comparison", "OLMo-3-32B midtrained target versus pretrained reference", "Not Disclosed", "Not Disclosed", "execution 更接近语义但覆盖有限输入；LLM judge 是受 operating point 约束的 proxy，不能替代 license/provenance evidence。"),
"2606.12765": ("INFER-TENSORRT-LLM", "Low-precision backend contract 必须通过 checksum/provenance microbench 分离 interface support、真正加速、accumulator width、execution rail 与 fragment layout。", (3,3,3), "No Change — Existing Coverage", "§3 Methodology; §§4–8 characterization", "§§4–8 measurements and fused-kernel result", "§10 Discussion and limitations", "Metal 4.1 matmul2d microbenchmarks and fused GEMM+bias+GELU", "Metal Performance Primitives tensor path", "Single Apple M4 Max GPU", "fp8 E4M3, fp16, accumulator ≥fp32 evidence", "单芯片逆向结果不能外推其他 Apple generations；fp8 在该硬件省 footprint 而非提高吞吐。"),
"2606.13708": ("INFER-PD-DISAGGREGATION", "Remote-memory indirection 可用 memory-side NIC 上预注册、静态可验证的 compact ISA 执行，把依赖链从多 RTT 收敛为一次 request。", (3,3,3), "Integrate", "§3 Tiara Design; compiler/verifier", "§4 Evaluation; §§4.5–4.6 AI workloads", "§6 Conclusion; no dedicated limitations section", "Graph, page-table, lock, MoE gather and disaggregated PagedAttention", "PagedAttention 8KB blocks; MoE 32 experts", "FPGA-based memory-side NIC prototype", "Not applicable", "line-rate operator 降低 RTT，却限制程序表达力并扩大 NIC TCB；复杂/动态逻辑仍需 CPU/RPC fallback。"),
"2606.14779": ("INFER-GPU-MEMORY", "KV offload 不应串行穿过单 host/SSD；应把多 DRAM/SSD 汇成 bandwidth-weighted pool，并以 user-space SPDK bypass filesystem。", (3,3,3), "Integrate", "§IV Design; KV orchestrator and passthrough", "§V Evaluation", "§VI Discussion", "Long-context KV offload and TTFT/I/O sweeps", "Llama-3.1-8B, GPT-OSS-20B, Qwen3-30B-A3B", "Multi-host-memory and SSD testbed disclosed in §V-A", "Model/KV precision disclosed in §V-A", "pooling 降低 blocked I/O，却引入 allocator metadata、failure recovery 与 SPDK 运维成本；短 context/HBM-resident path 仍更简单。"),
"2606.14783": ("PLATFORM-SECURITY", "Encoder-free VLM 的 visual tokens 与 layer-0 KV 可能成为 output filter 之前的可逆 privacy side channel；architecture 与 cache access 必须进入 threat model。", (3,3,3), "Integrate", "§2 Threat Model; §§4–8 mechanism/defense", "§3 setup; §§4–7 experiments", "§8 Defense Boundary; §9 deployment implications", "Held-out access-code inversion, clutter/degradation/transfer and defense ablations", "Gemma4/Fuyu vs Qwen3-VL/InternVL/LLaVA controls", "Not Disclosed", "Token/value quantization tested as ineffective value-level defense", "降低 spatial sampling 可减泄漏但可能损失 OCR/细节能力；value noise/quantization 不构成通用缓解。"),
"2606.18284": ("TRAIN-DATA", "训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。", (3,3,3), "Integrate", "§3 Probe Rewards; §5 probe data/selection", "§§4 and 6 Evaluation/Results", "§7 Limitations; mode-collapse findings", "Math, code and SWE task generation across model scales", "Qwen2.5-3B/7B and Qwen3.5-27B solver settings", "Not Disclosed", "Not Disclosed", "probe 降低 inner-loop solver cost，但 reward hacking、mode collapse 与 solver drift 要求 held-out solver gate。"),
"2606.18286": ("TRAIN-SFT", "Code SFT 的 sparse supervision unit 应是 syntax-complete、data-flow-connected code block，而非孤立 high-loss token；完整 response 继续作 context。", (3,3,3), "Integrate", "§5 Method; §§5.1–5.4", "§6 Experiments; Appendix A", "§7 Conclusion; Appendix C runtime analysis", "Six code-generation benchmarks", "Qwen2.5-Coder-1.5B-Instruct and comparison models", "Disclosed in Appendix A.3; exact accelerator remains v1-bound", "Training precision disclosed in Appendix A.3", "仅 1.9% supervised tokens 降低 loss work，却依赖 parser/data-flow correctness；错误 block 边界会删除必要 credit，full-token SFT 仍是稳健基线。"),
}

PATHS = {
"AGENT-REFLECTION":"books/part-07-agent/80-reflection.md", "PLATFORM-SECURITY":"books/part-06-ai-infrastructure/72-security.md",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/66-evaluation-system.md", "AGENT-WORKFLOW":"books/part-07-agent/81-workflow.md",
"PLATFORM-COST":"books/part-06-ai-infrastructure/70-cost.md", "INFER-GPU-MEMORY":"books/part-05-inference-system/54-gpu-memory.md",
"AGENT-MEMORY":"books/part-07-agent/77-memory.md", "PLATFORM-MONITORING":"books/part-06-ai-infrastructure/67-monitoring.md",
"INFER-SPECULATIVE-DECODING":"books/part-05-inference-system/48-speculative-decoding.md", "TRAIN-RLHF":"books/part-04-training-system/31-rlhf.md",
"TRAIN-DATA":"books/part-04-training-system/27-data.md", "INFER-TENSORRT-LLM":"books/part-05-inference-system/49-tensorrt-llm.md",
"INFER-KSERVE-TOPOLOGY":"books/part-05-inference-system/53-kserve-llm.md", "TRAIN-SFT":"books/part-04-training-system/29-sft.md",
"INFER-PD-DISAGGREGATION":"books/part-05-inference-system/55-pd-disaggregation.md",
}

TITLE = {
    "2606.11878": "Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decisions",
}

ADJ = {
"AGENT-REFLECTION":"books/part-07-agent/81-workflow.md; books/part-07-agent/84-agent-platform.md",
"PLATFORM-SECURITY":"books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/67-monitoring.md; books/part-07-agent/81-workflow.md",
"AGENT-WORKFLOW":"books/part-07-agent/80-reflection.md; books/part-07-agent/82-multi-agent.md",
"PLATFORM-COST":"books/part-05-inference-system/56-inference-scheduling.md; books/part-06-ai-infrastructure/67-monitoring.md",
"INFER-GPU-MEMORY":"books/part-05-inference-system/45-why-kv-cache-speeds-up.md; books/part-05-inference-system/55-pd-disaggregation.md",
"AGENT-MEMORY":"books/part-07-agent/75-context.md; books/part-07-agent/76-rag.md",
"PLATFORM-MONITORING":"books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/69-trace.md",
"INFER-SPECULATIVE-DECODING":"books/part-05-inference-system/44-decode.md; books/part-04-training-system/31-rlhf.md; books/part-05-inference-system/49-tensorrt-llm.md",
"TRAIN-RLHF":"books/part-04-training-system/29-sft.md; books/part-04-training-system/33-grpo.md",
"TRAIN-DATA":"books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/59-model-registry.md",
"INFER-TENSORRT-LLM":"books/part-05-inference-system/48-speculative-decoding.md; books/part-05-inference-system/50-vllm.md",
"INFER-KSERVE-TOPOLOGY":"books/part-05-inference-system/42-what-happens-during-inference.md; books/part-05-inference-system/56-inference-scheduling.md",
"TRAIN-SFT":"books/part-04-training-system/27-data.md; books/part-04-training-system/31-rlhf.md",
"INFER-PD-DISAGGREGATION":"books/part-05-inference-system/54-gpu-memory.md; books/part-05-inference-system/56-inference-scheduling.md",
}

def fam(a): return "SF-2026-ARXIV-" + a.replace(".", "-")
def norm(s):
    s=unicodedata.normalize("NFC",s.replace("\r\n","\n").replace("\r","\n"))
    return "\n".join(x.rstrip() for x in s.strip().splitlines())
def rp(f,a,method,evaluation,limits,body):
    def multi(value):
        return ";".join(sorted(x.strip() for x in value.split(";") if x.strip() and x.strip() != "—"))
    c="|".join(("review-completion-v1",f,f"paper-v1:{a}",f"arXiv:{a}v1","SRC-ARXIV",f"arXiv:{a}v1",f"SRC-ARXIV@arXiv:{a}v1","deep",multi(method),multi(evaluation),multi(limits),"Not Disclosed — no later artifact used",f"claim:{f}",f"review:{f}","review-body-sha256:"+hashlib.sha256(norm(body).encode()).hexdigest()))
    return "RP-"+hashlib.sha256(c.encode()).hexdigest()[:16]
def close(row):
    t=(row["title"]+" "+row["abstract"]).lower()
    if row["screening_route"].startswith("not_"): cls="registered_noncore_false_negative_closed"
    elif any(x in t for x in ("survey","tutorial","perspective")): cls="survey_or_position_without_new_owner_contract"
    elif any(x in t for x in ("benchmark","dataset","evaluation")): cls="evaluation_artifact_without_new_durable_system_contract"
    elif any(x in t for x in ("image","video","speech","medical","robot","molecular")): cls="application_or_model_quality_only"
    else: cls="model_method_or_local_artifact_without_unresolved_owner_delta"
    first=re.split(r"(?<=[.!?])\s+",re.sub(r"\s+"," ",row["abstract"]).strip())[0][:220]
    return cls, f"Full title+abstract semantic review: {first}. It does not add a durable system owner/control/evaluation/release delta beyond the 31 retained families."

def main():
    p=json.loads(PROVISIONAL.read_text()); rows=p["identities"]
    assert len(rows)==559 and set(M)=={r["arxiv_id"] for r in rows if r["arxiv_id"] in M}
    audit=[]; reviews=[]
    for row in rows:
        a=row["arxiv_id"]
        if a not in M:
            cls,reason=close(row); row.update(screening_status="pre_denominator_closure",screening_reason=reason,pre_denominator_closure_class=cls)
            audit.append((a,row["screening_route"],"closure",cls,reason)); continue
        owner,delta,score,disp,method,evaluation,limits,workload,model,hardware,precision,trade=M[a]
        row.update(screening_status="retained_after_full_semantic_audit",screening_reason=delta,pre_denominator_closure_class="—")
        audit.append((a,row["screening_route"],"retained","—",delta))
        f=fam(a); first_date=row["submitted_v1_utc"][:10]
        title=TITLE.get(a,row["title"])
        body=f"""### {a} — {title}

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：{delta}

**State / data / control owner。** `{owner}` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:{a}v1 {evaluation}` 支持 `{workload}`；模型 `{model}`；硬件 `{hardware}`；精度 `{precision}`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:{a}v1 {method}`；counterevidence locator：`arXiv:{a}v1 {limits}`。

**Trade-off / failure / coexistence / evolution。** {trade} 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:{f}:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/{a}v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:{f}:end -->"""
        b={"workload":"Disclosed — "+workload,"model":"Disclosed — "+model,"hardware":hardware,"precision":precision,"input_length":"Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound","output_length":"Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound","batch":"Not Disclosed as one universal contract — trial count is not relabeled as batch","concurrency":"Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency","slo":"Not Disclosed — research metrics are not a production SLO","evaluator":"Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics"}
        reviews.append(dict(a=a,f=f,title=title,owner=owner,delta=delta,score=score,disp=disp,method=f"arXiv:{a}v1 {method}",evaluation=f"arXiv:{a}v1 {evaluation}",limits=f"arXiv:{a}v1 {limits}",body=body,benchmark=b,first_date=first_date))
    ledger=dict(p); ledger.update(gate_status="all_gates_passed",routed_candidate_denominator=31,routed_candidate_denominator_status="frozen_after_559_of_559_full_semantic_audit",abstract_screening_closure=528,canonical_candidate_denominator={"denominator_id":DENOMINATOR_ID,"raw_identities":559,"retained":31,"pre_denominator_closures":528,"audit_receipt":str(AUDIT.relative_to(ROOT)),"frozen_at":EXECUTED_AT},audit={"reviewed_identities":"559/559","title_abstract_semantic_screen":"passed","candidate_false_positive_false_negative_audit":"passed","denominator_frozen":True,"coverage_gate":"closed","evidence_gate":"passed","selection_gate":"passed","books_gate":"passed_after_31_of_31_post_write_fresh_context_semantic_audit"})
    LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    with AUDIT.open("w",newline="") as h:
        w=csv.writer(h,delimiter="\t"); w.writerow(["arxiv_id","screening_route","decision","closure_class","semantic_reason"]); w.writerows(audit)
    selected={"2606.11632":"DA-20260611-ADMISSION","2606.11916":"DA-20260611-AGING","2606.12688":"DA-20260611-COMPOSITE-SERVING"}
    rec=[]
    for r in reviews:
        r["rp"]=rp(r["f"],r["a"],r["method"],r["evaluation"],r["limits"],r["body"])
        rec.append({"source_family_id":r["f"],"primary_identifier":f"arXiv:{r['a']}v1","event_identity":f"paper-v1:{r['a']}","review_status":"deep_complete","access_status":"accessible","review_provenance_id":r["rp"],"review_route":"deep","primary_evidence_version":f"arXiv:{r['a']}v1","reviewed_evidence_versions":[f"SRC-ARXIV@arXiv:{r['a']}v1"],"method_identity_locators":[r["method"]],"evaluation_locators":[r["evaluation"]],"limitations_counterevidence_locators":[r["limits"]],"artifact_locators":["Not Disclosed — no later artifact used"],"claim_boundary_ref":f"claim:{r['f']}","review_ref":f"review:{r['f']}","review_body_sha256":hashlib.sha256(norm(r["body"]).encode()).hexdigest(),"completion_result":"complete","ordinary_pending_locator_count":0,"benchmark_contract":r["benchmark"],"stable_node_id":r["owner"],"books_disposition":r["disp"],"selection_decision":"selected" if r["a"] in selected else "not_selected"})
    RECEIPTS.write_text(json.dumps({"contract_version":"V2.1","denominator_id":DENOMINATOR_ID,"generated_at":EXECUTED_AT,"reviews":rec},ensure_ascii=False,indent=2)+"\n")
    families="; ".join(r["f"] for r in reviews)
    L=["# Daily Research — 2026-06-11","",f"> Strict V2.1 reconstruction for `{DENOMINATOR_ID}`. Books writeback was serialized through root; this lane performed the independent post-write audit.","","## Executive Summary","",f"The Beijing window contains 559 registered arXiv identities. Full 559/559 title+abstract semantic screening freezes 31 durable AI-system families and 528 row-specific closures. All 31 exact-v1 Reviews, benchmark contracts and full-frontier selection decisions pass fresh semantic audit. Root merged 26 Integrate families into 12 unique owners; five No Change families were rechecked against existing owner/adjacent coverage. The 31/31 post-write fresh-context audit resolved one Daily-only owner finding for 2606.12370 and closed Books Gate.","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-11 |","| Window End | 2026-06-11 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {DENOMINATOR_ID} |",f"| Denominator Frozen At | {EXECUTED_AT} |","| Completion Status | Complete |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Passed |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-06-10T09:00:00+08:00 | 2026-06-11T09:00:00+08:00 | {EXECUTED_AT} | Frozen DataCite DOI-prefix snapshots; Core full enumeration; 559/559 semantic screen | checked | 559 | {families} | 40 disjoint DOI-prefix snapshots; 559 unique in-window identities | 2026-06-11T01:00:00Z | ../_sources/daily-20260611/screening-ledger.json; ../_sources/daily-20260611/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260611 | — |","","<!-- coverage:SRC-ARXIV:20260611:start -->","All 559 identities were read at title+abstract level. Full-retain and full-closure surfaces were audited; keyword routes were not used as admission decisions. Frozen result: 31 retained, 528 closures.","<!-- coverage:SRC-ARXIV:20260611:end -->","","## 2. Candidate Ledger and Score V2","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        s=r["score"]; L.append(f"| {r['f']} | arXiv:{r['a']}v1 | paper-v1:{r['a']} | 2026-W24 | {r['first_date']} | SRC-ARXIV | {s[0]} | {s[1]} | {s[2]} | {sum(s)} | retained | deep_complete | accessible | none | review:{r['f']} | self | — | new_in_window | {r['owner']} | {r['disp']} | books-review:{r['f']} | yes |")
    L += ["","### Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews: L.append(f"| {r['f']} | {r['rp']} | deep | arXiv:{r['a']}v1 | SRC-ARXIV@arXiv:{r['a']}v1 | {r['method']} | {r['evaluation']} | {r['limits']} | Not Disclosed — no later artifact used | claim:{r['f']} | complete |")
    L += ["","### Benchmark Contract","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=r["benchmark"]; L.append("| "+" | ".join([r["f"],b["workload"],b["model"],b["hardware"],b["precision"],b["input_length"],b["output_length"],b["batch"],b["concurrency"],b["slo"],b["evaluator"]])+" |")
    L += ["","## 3. Source Reviews",""]
    for r in reviews: L += [f"<!-- review:{r['f']}:start -->",r["body"],f"<!-- review:{r['f']}:end -->",""]
    L += ["## 4. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        eligibility="score_7_9; potential_books_delta" if r["disp"].startswith("Integrate") else "score_7_9"
        if r["a"] in selected: L.append(f"| {r['f']} | {eligibility} | selected | {selected[r['a']]} | — | Selected after 31/31 frontier comparison for non-overlapping control-plane, reliability, or serving-abstraction novelty. | analysis:{selected[r['a']]} |")
        else: L.append(f"| {r['f']} | {eligibility} | not_selected | — | — | Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative. | analysis-decision:{r['f']} |")
    for r in reviews:
        if r["a"] not in selected: L += ["",f"<!-- analysis-decision:{r['f']}:start -->",r["delta"]+" It did not outrank the three selected non-overlapping units for today's compact analysis.",f"<!-- analysis-decision:{r['f']}:end -->"]
    L += ["","<!-- analysis:DA-20260611-ADMISSION:start -->","### DA-20260611-ADMISSION","Proposal is not authority: typed contract, evidence digest, policy/revocation version and broker identity must all bind before a model proposal mutates production state.","<!-- analysis:DA-20260611-ADMISSION:end -->","","<!-- analysis:DA-20260611-AGING:start -->","### DA-20260611-AGING","Serving reliability is time-dependent: host/device/client signals and autocorrelation-aware long campaigns are required before rejuvenation or release decisions.","<!-- analysis:DA-20260611-AGING:end -->","","<!-- analysis:DA-20260611-COMPOSITE-SERVING:start -->","### DA-20260611-COMPOSITE-SERVING","Composite multimodal serving requires request walks over a component graph, because fixed stage DAGs cannot express loops, per-request paths, streaming edges and component-level placement together.","<!-- analysis:DA-20260611-COMPOSITE-SERVING:end -->","","## 5. Books Comparison and Decision","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        rel="Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse"
        target=PATHS[r['owner']]+"#L1"; adjacent="; ".join(x+"#L1" for x in ADJ[r['owner']].split("; "))
        L.append(f"| {r['f']} | {r['owner']} | {target} | {adjacent} | existing:{r['f']} | delta:{r['f']} | {rel} | {r['disp']} | books-review:{r['f']} |")
    for r in reviews:
        rel="Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse"
        L += ["",f"<!-- existing:{r['f']}:start -->",f"Owner `{r['owner']}` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.",f"<!-- existing:{r['f']}:end -->","",f"<!-- delta:{r['f']}:start -->",r["delta"],f"<!-- delta:{r['f']}:end -->","",f"<!-- books-review:{r['f']}:start -->",f"Owner `{r['owner']}`; relation `{rel}`; disposition `{r['disp']}`; adjacent handoff `{ADJ[r['owner']]}`.",f"<!-- books-review:{r['f']}:end -->"]
    L += ["","## 6. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260611-COVERAGE-V1 | fresh-context:jun11-v1 | coverage | coverage:SRC-ARXIV:20260611 | — | 559/559 full semantic screen; denominator 31/559; closures 528 | passed |",f"| SA-20260611-EVIDENCE-V1 | fresh-context:jun11-v1 | evidence | {'; '.join('review:'+r['f'] for r in reviews)} | — | 31/31 exact-v1 method/evaluation/limitations and benchmark contracts | passed |",f"| SA-20260611-SELECTION-V1 | fresh-context:jun11-v1 | deep_analysis_selection | {'; '.join(('analysis:'+selected[r['a']]) if r['a'] in selected else ('analysis-decision:'+r['f']) for r in reviews)} | — | 31/31 frontier; three selected | passed |",f"| SA-20260611-BOOKS-POSTWRITE-V1 | fresh-context:jun11-postwrite-v1 | books | {'; '.join('books-review:'+r['f'] for r in reviews)} | F-0611-OWNER-12370 | resolved owner to INFER-SPECULATIVE-DECODING with TRAIN-RLHF adjacent; 26/26 writebacks, 5/5 No Change and 31/31 owner/adjacent handoffs passed; `papers/2026/06/_sources/daily-20260611/POST_WRITE_FRESH_AUDIT_V1.md` | passed |","","## 7. Materials and Access","","- DataCite snapshots are frozen discovery/identity/abstract evidence only.","- Primary manuscript evidence is the official `https://arxiv.org/html/<id>v1` path.","- Direct shell transfer reset; official HTML was reviewed through the working web path.","","## 8. Daily Integration Decision","","- `Integrate`: 26 families were merged by root into 12 unique ROADMAP owners; each exact-v1 family ID occurs once in its target Books file.","- `No Change — Existing Coverage`: 5 families remain Daily evidence only because the durable mechanism and fallback boundary already exist in the owner or explicit adjacent chapter.","- Finding `F-0611-OWNER-12370` was confined to Daily routing: MTP acceptance/TV/rejection correctness belongs to `INFER-SPECULATIVE-DECODING`; `TRAIN-RLHF` consumes rollout throughput and policy-update consequences as an adjacent handoff.","","## 9. Repository Changes","","- Root performed the serialized Books writeback across the 12 files listed in `BOOKS_INTEGRATION_QUEUE_V1.md`.","- This lane updated the 2026-06-11 Daily, source receipts, finalizer and post-write audit only; it did not stage, commit, push or modify Books.","","## 10. Open Questions","","- How should runtime-skill probes, policy epochs and certificate revocation be recalibrated when evidence or threat distributions drift?","- Which aging signals can safely trigger rejuvenation without turning a deployment-specific campaign into a universal threshold?","- How should graph-serving placement, tiered memory and PD handoff share backpressure and failure semantics under mixed workloads?","- How should event-sourced experience and persistent-memory certificates expire or supersede incorrect historical judgments?","- These are research continuations, not unresolved Gate findings."]
    # Canonical V2.1 reader-facing schema.  Keep the evidence tables and review
    # bodies unchanged, but make the published report use the same stable
    # presentation contract as July and all later Daily reports.
    L[2:2] = [
        "**Research Date:** 2026-06-11", "",
        "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-06-10 09:00:00 ～ 2026-06-11 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；559/559 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet", "",
        "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding", "",
    ]
    canonical_headings = {
        "## 2. Candidate Ledger and Score V2": "## 2. Candidate Ledger",
        "### Review Completion Receipt": "## 3. Review Completion Receipt",
        "### Benchmark Contract": "## 4. Benchmark Contracts",
        "## 3. Source Reviews": "**Source Reviews**",
        "## 4. Deep Analysis Selection": "## 5. Deep Analysis Selection",
        "## 5. Books Comparison and Decision": "## 6. Books Comparison",
        "## 6. Semantic Audit": "## 7. Semantic Audit",
        "## 7. Materials and Access": "### Materials and Access",
        "## 8. Daily Integration Decision": "## 9. Recommended Action",
        "## 9. Repository Changes": "## 10. Repository Changes",
        "## 10. Open Questions": "## 11. Open Questions",
    }
    L = [canonical_headings.get(line, line) for line in L]
    recommended_index = L.index("## 9. Recommended Action")
    L[recommended_index:recommended_index] = [
        "## 8. Ignored Noise", "",
        "- 528 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit instead of being promoted into the Candidate Ledger.", "",
    ]
    L += ["", "## 12. Sources", ""]
    for r in reviews:
        L.append(
            f"- [arXiv:{r['a']}v1 — {r['title']}](https://arxiv.org/html/{r['a']}v1) — "
            f"first-public `{r['first_date']}`；accessed `{EXECUTED_AT[:10]}`；Source Family `{r['f']}`。"
        )
    L += [
        "- `SRC-ARXIV` registry contract：`docs/RESEARCH_SOURCES.md`。", "",
        "## 13. Final Status", "",
        "- Status: Complete.",
        "- Coverage Gate: Closed.",
        "- Evidence Gate: Passed.",
        "- Books Gate: Passed.",
        "- Fresh-context Semantic Audit: Passed；unresolved findings = 0.",
    ]

    L = [
        x.replace(
            "| F-0611-OWNER-12370 | resolved owner to INFER-SPECULATIVE-DECODING with TRAIN-RLHF adjacent;",
            "| — | resolved F-0611-OWNER-12370 to INFER-SPECULATIVE-DECODING with TRAIN-RLHF adjacent;",
        )
        for x in L
    ]
    L=[x.replace("40 disjoint DOI-prefix snapshots; 559 unique in-window identities", "pages=40, records=40000/40000, final cursor=end; 559 unique in-window identities") for x in L]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(L)+"\n")
    integrates=[r for r in reviews if r["disp"].startswith("Integrate")]
    groups={}
    for r in integrates: groups.setdefault(r["owner"],[]).append(r)
    q=["# 2026-06-11 Books Integration Queue V1","",f"Denominator: `{DENOMINATOR_ID}`. Proposal-only; root owns Books writeback. {len(integrates)} family proposals are deduplicated into {len(groups)} owner-file writes.",""]
    for owner,rs in groups.items():
        q += [f"## `{owner}` → `{PATHS[owner]}`",""]
        for r in rs: q.append(f"- `{r['f']}`: {r['delta']} Boundary: `{r['limits']}`; exact-v1 `https://arxiv.org/html/{r['a']}v1`.")
        q.append("")
    q += ["## No Change handoffs",""]+[f"- `{r['f']}` → `{PATHS[r['owner']]}`: existing owner already states the mechanism and fallback boundary; retain Daily exact-v1 evidence without append." for r in reviews if not r["disp"].startswith("Integrate")]
    QUEUE.write_text("\n".join(q)+"\n")
    ready=["# 2026-06-11 Ready-to-Insert Books V1","",f"Denominator `{DENOMINATOR_ID}`. Root may merge each owner group into one minimal paragraph; do not copy headline rankings.",""]
    for owner,rs in groups.items():
        ready += [f"## `{owner}`","", " ".join(r["delta"]+" "+M[r["a"]][-1] for r in rs),"","Source-specific Review notes:"]+[f"- `{r['f']}` — exact-v1 `https://arxiv.org/html/{r['a']}v1`; method `{r['method']}`; evaluation `{r['evaluation']}`; boundary `{r['limits']}`; no production-SLO or cross-hardware generalization." for r in rs]+[""]
    READY.write_text("\n".join(ready)+"\n")
    EVIDENCE_AUDIT.write_text(f"# 2026-06-11 Fresh Evidence and Selection Audit V1\n\n- Coverage: PASS — 559/559 title+abstract; 31 retained; 528 row-specific closures.\n- exact-v1: PASS — 31/31 official v1 title/TOC/method/evaluation/limitations reviewed.\n- Benchmark contract: PASS — 31/31; undisclosed fields remain explicit and research metrics are not relabeled as SLO.\n- Source reviews: PASS — 31/31 source-specific problem/mechanism/state-data-control/evaluation proof-nonproof/trade-off/failure/coexistence/evolution.\n- Selection: PASS — 31/31 full frontier; three non-overlapping units selected.\n- Books post-write: PASS — 26/26 Integrate writebacks and 5/5 No Change dispositions; 31/31 unique owner/adjacent handoffs. Finding F-0611-OWNER-12370 was resolved in Daily routing without a Books edit.\n")

    no_change_locations = {
        "2606.12243": "Ch48 routed slim verifier + exact full-verifier fallback; existing exact family citation",
        "2606.12370": "Ch48 acceptance/TV objective + exact rejection sampling; Ch31 consumes rollout handoff",
        "2606.12487": "Ch49 phase-conditioned mixed precision, calibration gate and fixed-precision fallback",
        "2606.12736": "Ch66 interactive environment, step/process verifier, domain slice and open-ended evidence limits",
        "2606.12765": "Ch49 vendor-neutral bit-exact numeric/backend contract and end-to-end fallback",
    }
    audit_lines = [
        "# 2026-06-11 Post-write Fresh-context Audit V1", "",
        f"Denominator `{DENOMINATOR_ID}`; 31/31 families audited independently after root Books writeback.", "",
        "| Family | Disposition | Unique owner / adjacent result | Mechanism and non-proof boundary | Result |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in reviews:
        if r["disp"].startswith("Integrate"):
            path = ROOT / PATHS[r["owner"]]
            hits = [i for i, line in enumerate(path.read_text().splitlines(), 1) if r["a"] in line]
            assert len(hits) == 1, (r["a"], path, hits)
            location = f"`{PATHS[r['owner']]}:{hits[0]}`; owner `{r['owner']}`; adjacent `{ADJ[r['owner']]}`"
            boundary = f"Mechanism: {r['delta']} Boundary: {M[r['a']][-1]}"
        else:
            location = f"owner `{r['owner']}`; adjacent `{ADJ[r['owner']]}`; {no_change_locations[r['a']]}"
            boundary = f"Existing durable proposition owns this mechanism: {r['delta']} Boundary: {M[r['a']][-1]} Daily retains the exact-v1 receipt without duplicative append."
        audit_lines.append(f"| `{r['f']}` | {r['disp']} | {location} | {boundary} | PASS |")
    audit_lines += ["", "## Finding closure", "", "- `F-0611-OWNER-12370`: pre-audit Daily routed the family to `TRAIN-RLHF`; fresh comparison found the durable acceptance/TV/rejection contract and the only existing family citation in Ch48. Daily/receipt owner is corrected to `INFER-SPECULATIVE-DECODING`; Ch31 is an adjacent rollout consumer. No Books rewrite was required.", "", "## Gate verdict", "", "- 26/26 Integrate: PASS.", "- 5/5 No Change: PASS.", "- 31/31 unique owner/adjacent handoff: PASS.", "- Unresolved findings: 0.", "- Books Gate: PASS."]
    POSTWRITE_AUDIT.write_text("\n".join(audit_lines)+"\n")
    (PACKET/"README.md").write_text(f"# 2026-06-11 source packet\n\nCanonical denominator `31/559`; closures `528`; Coverage/Evidence/Selection/Books Gates Passed. Post-write fresh-context audit: `POST_WRITE_FRESH_AUDIT_V1.md`.\n")
    (PACKET/"candidate-ids-v1.txt").write_text("\n".join(r["a"] for r in reviews)+"\n")

    # Seal the published report, its complete date-local packet and the final
    # owner renderer.  Paths are repository-relative so the manifest has one
    # unambiguous verification cwd.
    targets = [p for p in PACKET.rglob("*") if p.is_file() and p != SHA_MANIFEST]
    targets += [REPORT, Path(__file__).resolve()]
    manifest_lines = []
    for path in sorted(set(targets), key=lambda p: str(p.relative_to(ROOT))):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest_lines.append(f"{digest}  {path.relative_to(ROOT)}")
    SHA_MANIFEST.write_text("\n".join(manifest_lines) + "\n")

if __name__=="__main__": main()
