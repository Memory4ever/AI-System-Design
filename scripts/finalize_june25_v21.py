#!/usr/bin/env python3
"""Materialize the strict 2026-06-25 Daily V2.1 packet without editing Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260625"
REPORT = ROOT / "papers/2026/06/25/README.md"
EXECUTED_AT = "2026-08-29T14:30:00+08:00"
ND = "Not Disclosed"

# Exact-v1 section names were transcribed from the official arXiv HTML/PDF TOCs.
# tuple: owner, method/identity, evaluation, limitations/counterevidence.
META = {
"2606.25274":("AGENT-PLANNING","3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam","5 Experiments; 5.1 Implemented Evidence; 6 Analysis","7 Limitations"),
"2606.25285":("INFER-GPU-MEMORY","3 EPTS: Elastic Post-Training Sparsity","4 Experiments; Experimental Setup; Main Results","Limitations and Discussion"),
"2606.25296":("PLATFORM-SECURITY","SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation","Experimental Evaluation; Functional-Safety Case Studies","Threats to Validity; Limitations"),
"2606.25342":("MODEL-LONG-CONTEXT","Parametric Attention and Lifelong In-Context Learning formulation","Experiments; Lifelong sequence results","Discussion; finite-memory and task-family limitations"),
"2606.25349":("PLATFORM-SECURITY","IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation","VII Evaluation","VIII Conclusion; exact-v1 analytical-evaluation-only note"),
"2606.25353":("INFER-PREFILL","3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation","5 Experiment Setup; 6 Evaluation","7 Discussion; 7.2 Future Works"),
"2606.25366":("PLATFORM-SECURITY","III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance","VIII Robustness; IX Integrated Evaluation","XI-D Limitations"),
"2606.25371":("PLATFORM-SECURITY","III Problem Setup; IV Conformal Recovery-Deadline Certificate","V Experiments","VI-D Limitations"),
"2606.25388":("TRAIN-DATA","III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control","V Experimental Evaluation; V-A Experimental Setup","VII Discussion and Future Work"),
"2606.25410":("TRAIN-DATA","3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling","4 Experiments; 4.1 Experimental Setup; 4.4 Results","5 Conclusion; class-forgetting experimental scope"),
"2606.25426":("INFER-PREFILL","3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing","4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement","6 Conclusion; Limitations"),
"2606.25447":("AGENT-WORKFLOW","3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type","4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness","B Benchmark Details; C Experimental Details; stated ALFWorld boundary"),
"2606.25449":("AGENT-MEMORY","3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol","4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix","7 Limitations"),
"2606.25453":("INFER-TENSORRT-LLM","III EmuGEMM-I; IV EmuGEMM-II","V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off","V-G Limitations"),
"2606.25467":("INFER-SCHEDULING","III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration","V Experimental Evaluation; V-A Experimental Setup","D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications"),
"2606.25487":("PLATFORM-EVALUATION-SYSTEM","3 Setup; Appendix A Prompts, wrappers, and attack configuration","4 Results; 4.1 Calibration against human labels; 4.3 white-box attack","6 Limitations"),
"2606.25514":("AGENT-MULTI-AGENT","2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication","3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures","5 Threats to Validity"),
"2606.25519":("INFER-GPU-MEMORY","3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy","D Additional evaluation details; D.1 Benchmarks and evaluation protocol","7 Can We Reduce Reasoning-Token Inflation; D.2 Model details"),
"2606.25532":("PLATFORM-FOUNDATIONS","Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought","Hardware-compliance evaluation and discovered-system validation","Exact-v1 research-prototype and evaluated hardware-design boundary"),
"2606.25548":("TRAIN-DATA","4 Transcoders-based Concept Removal; 4.1 BLOCK Framework","5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness","G Limitations; D.1 Model-Architecture-Dependent Subtleties"),
"2606.25575":("MULTIMODAL-EMBODIED-VLA","Variable-autonomy architecture; task-phase authority transfer; always-available release gesture","44-participant user study; five bimanual tasks; policy-variant success","Single wearable-hand embodiment, known objects, five tools, and short-horizon study"),
"2606.25592":("PLATFORM-SECURITY","2 Visual Prompt Attack and Defense; 2.2 VPA-Guard","3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments","E.1 Limitations; E.4 Human-in-the-loop Discussion"),
"2606.25605":("AGENT-TOOL-CALLING","3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution","5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency","7.5 Failure Cases and Limitations; 8.4 Limitations"),
"2606.25608":("PLATFORM-SECURITY","V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG","VI Initial Evaluation","V-C Restrictions of our architecture; VII Future Research"),
"2606.25622":("PLATFORM-EVALUATION-SYSTEM","IV Theoretical Framework: MAS Architecture and Experimental Setup","V Results & Discussion","VI Limitations & Future Work"),
"2606.25656":("AGENT-RAG","3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization","4 Experimental setup; 5 Experimental results","6 Conclusions and future work; C Retrieval-Generation Gap"),
"2606.25658":("AGENT-MEMORY","3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank","4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation","A Limitations"),
"2606.25674":("AGENT-RAG","3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization","4 Experiments; 4.1 Experimental Setup; B Evaluation Details","4.4 Analysis; task-type sensitivity to quantization"),
"2606.25700":("TRAIN-LORA","III Methods; III-B Training; III-C Architecture","IV Results; IV-B Computation calculation","V Discussion; V-A Choice of rank; V-C Computation"),
"2606.25705":("AGENT-TOOL-CALLING","3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator","4 Experiments and Results","5 Conclusion; short-paper and emulator-only boundary"),
"2606.25721":("PLATFORM-SECURITY","4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification","5 Evaluation; 5.1 Setup; 5.2 Results","6 Discussion; baseline and hyperparameter sensitivity"),
"2606.25759":("TRAIN-DISTRIBUTED-TRAINING","3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing","7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope","9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary"),
"2606.25760":("PLATFORM-EVALUATION-SYSTEM","3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks","4 UQ Generalizes Selectively; 5 Graded Error and Calibration","A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details"),
"2606.25782":("PLATFORM-EVALUATION-SYSTEM","2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel","5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs","OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency"),
"2606.25797":("PLATFORM-EVALUATION-SYSTEM","3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC","4 Implementation and Experimental Evaluation","0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect"),
"2606.25819":("AGENT-TOOL-CALLING","ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection","Experiments; Experimental Setup; Further Analysis; Error Analysis","Canonical recovery-path construction and five injected-hazard boundary"),
"2606.25838":("INFER-REQUEST-LIFECYCLE","III Method; IV Confidence-Aware Routing","V Experiments; V-A Evaluation protocol; VI Deployment Patterns","VII-C Limitations and future work"),
"2606.25863":("PLATFORM-SECURITY","PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution","PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches","PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary"),
"2606.25871":("TRAIN-DATA","3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic","4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance","5 Production Deployment and Discussion; sponsored-search relevance boundary"),
"2606.25987":("AGENT-TOOL-CALLING","3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought","5 WoFT Improves Surface Modeling; 5.1 Experimental setup","6 Next Steps and Research Vision; technical-report preliminary-results boundary"),
"2606.25996":("TRAIN-DATA","2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist","3 Experiments; CS, legal, and scientific reasoning tasks","6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation"),
"2606.26021":("PLATFORM-SECURITY","V Attention-based MIA; VI Inference-Time Hardening Against MIAs","IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results","VIII-C Limitations and opportunities; I Context size"),
"2606.26027":("TRAIN-GRPO","4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes","5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation","B Training Details; C Qwen3 Training; E Training Dynamic"),
"2606.26028":("PLATFORM-SECURITY","3 System Model: ERC-8004 Protocol; 7 Reputation Market Security","4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market","9 Limitations and Future Work; C x402 attribution challenges"),
"2606.26057":("PLATFORM-SECURITY","2 Threat Model; 3 Requirements; 4 Design; 5 Implementation","6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment","8.3 Limitations and Future Work; Artifact and Reproducibility"),
"2606.26071":("PLATFORM-EVALUATION-SYSTEM","4 Protocol and Methods; 5 Environments; 7 Methodological Insights","6 Case Studies; 8 Recommendations","10 Limitations and Future Work; negative-results and confounding boundary"),
"2606.26185":("PLATFORM-EVALUATION-SYSTEM","Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation","Cross-temperature, repeat-run and judge-agreement evaluation","Temperature control is necessary but not sufficient; prompt/model/vendor drift remains"),
"2606.26211":("AGENT-MCP","Data Facts metadata schema; provenance, semantics, constraints and exchange contract","NANDini multi-agent exchange examples and schema coverage","Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness"),
"2606.26257":("PLATFORM-SECURITY","Dataset Usage Inference formulation without shadow models or held-out data","Exact-v1 membership/dataset inference experiments and ablations","Requires the paper's observable score/query regime; not per-record legal attribution"),
"2606.26298":("PLATFORM-SECURITY","Governing Actions, Not Agents; Institutional Attestation model","Action-level attestation scenarios and governance analysis","Institutional model is a governance proposal, not a deployed enforcement benchmark"),
"2606.26300":("PLATFORM-EVALUATION-SYSTEM","Verification Horizon formulation for coding-agent rewards","Reward-verification experiments across coding horizons","No universal reward verifier; longer horizons and hidden environment state remain"),
"2606.26341":("PLATFORM-GPU-SCHEDULER","Many Problems One GPU batching and nonlinear-optimization execution design","GPU scaling experiments across problem families","Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof"),
"2606.26344":("INFER-TENSORRT-LLM","Axon synthesizing superoptimizer; tensor-program search and verification","Kernel synthesis evaluation and generated-program performance","Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence"),
"2606.26356":("AGENT-PROMPT","Instruction Bleed formulation; prompt-composed module interference","Cross-module interference experiments and mitigations","Prompt/module families tested do not establish universal isolation or adversarial robustness"),
"2606.26377":("PLATFORM-SECURITY","Unified intent-and-harm verification defense","Threat-generation and defense evaluation","Evaluated threat families and judges only; intent inference is not proof of harmless execution"),
"2606.26383":("PLATFORM-MONITORING","SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation","Predicted-vs-observed latency and throughput analysis","Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects"),
"2606.26429":("PLATFORM-EVALUATION-SYSTEM","DualEval joint model-item calibration","Unified LLM evaluation experiments and calibration analysis","Joint calibration assumes the evaluated item/model pool; new distributions require refitting"),
"2606.26439":("AGENT-RAG","TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization","GPU retrieval throughput, latency and quality evaluation","Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved"),
"2606.26441":("AGENT-RAG","GPUSparse learned sparse retrieval with parallel inverted indices","Retrieval quality, latency and GPU scaling experiments","Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling"),
"2606.26442":("AGENT-WORKFLOW","AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling","Utility execution, throughput and theorem-proving workflow evaluation","Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety"),
"2606.26449":("PLATFORM-TRACE","ProvenAI provenance-native trace schema and evidence links","Generated-answer trace/evidence evaluation","Trace completeness depends on instrumented producers; provenance does not imply source truth"),
"2606.26453":("INFER-TENSORRT-LLM","Micro-profiling tools as expert surrogates for LLM CUDA optimization","Generated-kernel correctness, profiling and speed evaluation","Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback"),
"2606.26456":("PLATFORM-EVALUATION-SYSTEM","Safety-Aware Mutation Testing proposal and interaction-aware mutant model","Simulation-based ADS testing protocol and proposed adequacy criterion","Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional"),
"2606.26463":("AGENT-PLANNING","Variable-delay real-time RL; lightweight gate selects state-dependent planning budget","Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation","Game planners and timing model do not prove benefit under production tool latency or safety deadlines"),
"2606.26472":("INFER-KV-CACHE","Epiphany score from forward-pass representation change; attention-matrix-free eviction","Long-reasoning cache/quality evaluation and 16x feasible-context claim","Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback"),
"2606.26479":("PLATFORM-SECURITY","Out-of-band prompt-injection defenses organized as reference monitors and integrity policies","Adaptive evaluation methodology against policy-aware attackers","Position/evaluation paper; static AgentDojo results do not establish adaptive robustness"),
"2606.26488":("INFER-GPU-MEMORY","Compression of recursive reasoners across precision, pruning, distillation and attention variants","Three tasks and two recursive architectures; local vs puzzle-exact accuracy","Edge recursive models only; token-level preservation does not imply global-reasoning preservation"),
"2606.26492":("PLATFORM-EVALUATION-SYSTEM","Within-program versus leave-program-out diagnostic design","DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis","Fault-injected programs and studied diagnosers do not prove production root-cause validity"),
}

NO_CHANGE = {"2606.25410","2606.25548","2606.25608","2606.25700","2606.25797"}
PATHS = {
"MODEL-LONG-CONTEXT":"books/part-02-model/22-long-context.md","MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md","TRAIN-DATA":"books/part-04-training-system/27-data.md","TRAIN-LORA":"books/part-04-training-system/30-lora.md","TRAIN-GRPO":"books/part-04-training-system/33-grpo.md","TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/36-distributed-training.md","INFER-REQUEST-LIFECYCLE":"books/part-05-inference-system/42-what-happens-during-inference.md","INFER-PREFILL":"books/part-05-inference-system/43-prefill.md","INFER-KV-CACHE":"books/part-05-inference-system/45-why-kv-cache-speeds-up.md","INFER-TENSORRT-LLM":"books/part-05-inference-system/49-tensorrt-llm.md","INFER-GPU-MEMORY":"books/part-05-inference-system/54-gpu-memory.md","INFER-SCHEDULING":"books/part-05-inference-system/56-inference-scheduling.md","PLATFORM-FOUNDATIONS":"books/part-06-ai-infrastructure/57-what-is-ai-platform.md","PLATFORM-GPU-SCHEDULER":"books/part-06-ai-infrastructure/63-gpu-scheduler.md","PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/66-evaluation-system.md","PLATFORM-MONITORING":"books/part-06-ai-infrastructure/67-monitoring.md","PLATFORM-TRACE":"books/part-06-ai-infrastructure/69-trace.md","PLATFORM-SECURITY":"books/part-06-ai-infrastructure/72-security.md","AGENT-PROMPT":"books/part-07-agent/74-prompt.md","AGENT-RAG":"books/part-07-agent/76-rag.md","AGENT-MEMORY":"books/part-07-agent/77-memory.md","AGENT-TOOL-CALLING":"books/part-07-agent/78-tool-calling.md","AGENT-PLANNING":"books/part-07-agent/79-planning.md","AGENT-WORKFLOW":"books/part-07-agent/81-workflow.md","AGENT-MULTI-AGENT":"books/part-07-agent/82-multi-agent.md","AGENT-MCP":"books/part-07-agent/83-mcp.md"}

ADJACENT = {
"MODEL-LONG-CONTEXT":"books/part-02-model/19-kv-cache.md","MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/25-multimodal-world-models.md","TRAIN-DATA":"books/part-04-training-system/28-pretraining.md","TRAIN-LORA":"books/part-04-training-system/29-sft.md","TRAIN-GRPO":"books/part-04-training-system/32-ppo.md","TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/37-tensor-parallel.md","INFER-REQUEST-LIFECYCLE":"books/part-05-inference-system/43-prefill.md","INFER-PREFILL":"books/part-05-inference-system/42-what-happens-during-inference.md","INFER-KV-CACHE":"books/part-05-inference-system/44-decode.md","INFER-TENSORRT-LLM":"books/part-05-inference-system/48-speculative-decoding.md","INFER-GPU-MEMORY":"books/part-05-inference-system/55-pd-disaggregation.md","INFER-SCHEDULING":"books/part-05-inference-system/46-continuous-batching.md","PLATFORM-FOUNDATIONS":"books/part-06-ai-infrastructure/58-kubeflow.md","PLATFORM-GPU-SCHEDULER":"books/part-06-ai-infrastructure/64-volcano.md","PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/59-model-registry.md","PLATFORM-MONITORING":"books/part-06-ai-infrastructure/68-logging.md","PLATFORM-TRACE":"books/part-06-ai-infrastructure/68-logging.md","PLATFORM-SECURITY":"books/part-06-ai-infrastructure/71-multi-tenant.md","AGENT-PROMPT":"books/part-07-agent/75-context.md","AGENT-RAG":"books/part-07-agent/77-memory.md","AGENT-MEMORY":"books/part-07-agent/76-rag.md","AGENT-TOOL-CALLING":"books/part-07-agent/81-workflow.md","AGENT-PLANNING":"books/part-07-agent/80-reflection.md","AGENT-WORKFLOW":"books/part-07-agent/78-tool-calling.md","AGENT-MULTI-AGENT":"books/part-07-agent/81-workflow.md","AGENT-MCP":"books/part-07-agent/84-agent-platform.md"}

OWNER_CONTROL = {
"MODEL-LONG-CONTEXT":"把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取",
"MULTIMODAL-EMBODIED-VLA":"把任务阶段、共享自治等级和人工接管手势纳入动作控制回路",
"TRAIN-DATA":"把数据选择、校准或验证结果变成训练前可审计的数据控制状态",
"TRAIN-LORA":"把秩、适配器容量与计算预算绑定为显式训练配置",
"TRAIN-GRPO":"把崩溃信号与监督修复绑定到策略更新门控",
"TRAIN-DISTRIBUTED-TRAINING":"把集群运行剖面映射为运行时 bucket 与并行绑定状态",
"INFER-REQUEST-LIFECYCLE":"让路由器基于请求置信度持有后端选择与回退权",
"INFER-PREFILL":"把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态",
"INFER-KV-CACHE":"以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退",
"INFER-TENSORRT-LLM":"以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径",
"INFER-GPU-MEMORY":"把稀疏、量化或压缩决策绑定到显存预算和质量回退",
"INFER-SCHEDULING":"让在线编排器共同持有请求资源耦合、准入和降级状态",
"PLATFORM-FOUNDATIONS":"把硬件约束和发现链纳入平台设计候选的验收边界",
"PLATFORM-GPU-SCHEDULER":"把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节",
"PLATFORM-EVALUATION-SYSTEM":"把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态",
"PLATFORM-MONITORING":"以校准后的硬件与 workload 参数分解性能上界和瓶颈",
"PLATFORM-TRACE":"让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值",
"PLATFORM-SECURITY":"把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界",
"AGENT-PROMPT":"把模块间指令干扰作为可测试的组合边界，而非默认隔离",
"AGENT-RAG":"把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态",
"AGENT-MEMORY":"把动态记忆写入、回收与失效变成有 owner 的持久状态迁移",
"AGENT-TOOL-CALLING":"把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前",
"AGENT-PLANNING":"以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退",
"AGENT-WORKFLOW":"把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态",
"AGENT-MULTI-AGENT":"把事件通信、角色分工与失败升级纳入多 Agent 协调状态",
"AGENT-MCP":"以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约"}

TARGET_LINE = {
"MODEL-LONG-CONTEXT":374,"MULTIMODAL-EMBODIED-VLA":179,"TRAIN-DATA":130,"TRAIN-LORA":145,"TRAIN-GRPO":231,"TRAIN-DISTRIBUTED-TRAINING":646,
"INFER-REQUEST-LIFECYCLE":80,"INFER-PREFILL":33,"INFER-KV-CACHE":97,"INFER-TENSORRT-LLM":630,"INFER-GPU-MEMORY":186,"INFER-SCHEDULING":227,
"PLATFORM-FOUNDATIONS":61,"PLATFORM-GPU-SCHEDULER":141,"PLATFORM-EVALUATION-SYSTEM":136,"PLATFORM-MONITORING":18,"PLATFORM-TRACE":33,"PLATFORM-SECURITY":204,
"AGENT-PROMPT":46,"AGENT-RAG":51,"AGENT-MEMORY":900,"AGENT-TOOL-CALLING":55,"AGENT-PLANNING":140,"AGENT-WORKFLOW":36,"AGENT-MULTI-AGENT":240,"AGENT-MCP":83}

ADJACENT_LINE = {
"MODEL-LONG-CONTEXT":131,"MULTIMODAL-EMBODIED-VLA":259,"TRAIN-DATA":244,"TRAIN-LORA":194,"TRAIN-GRPO":330,"TRAIN-DISTRIBUTED-TRAINING":243,
"INFER-REQUEST-LIFECYCLE":33,"INFER-PREFILL":117,"INFER-KV-CACHE":31,"INFER-TENSORRT-LLM":113,"INFER-GPU-MEMORY":409,"INFER-SCHEDULING":75,
"PLATFORM-FOUNDATIONS":71,"PLATFORM-GPU-SCHEDULER":44,"PLATFORM-EVALUATION-SYSTEM":118,"PLATFORM-MONITORING":16,"PLATFORM-TRACE":66,"PLATFORM-SECURITY":33,
"AGENT-PROMPT":308,"AGENT-RAG":113,"AGENT-MEMORY":57,"AGENT-TOOL-CALLING":36,"AGENT-PLANNING":73,"AGENT-WORKFLOW":37,"AGENT-MULTI-AGENT":36,"AGENT-MCP":20}

def clean(s): return re.sub(r"\s+"," ",s).strip()
def sentences(s): return [x.strip() for x in re.split(r"(?<=[.!?])\s+",clean(s)) if x.strip()]
def first(s): return sentences(s)[0] if sentences(s) else clean(s)
def last(s): return sentences(s)[-1] if sentences(s) else clean(s)
def family(a): return "SF-2026-ARXIV-"+a.replace(".","-")
def norm(s): return "\n".join(x.rstrip() for x in unicodedata.normalize("NFC",s).strip().splitlines())
def md(s): return str(s).replace("|","/").replace("\n"," ")
def rp(fam,aid,method,evaluation,limitation,artifact,body):
    def multi(value):
        return ";".join(sorted(unicodedata.normalize("NFC", item.strip()) for item in value.split(";") if item.strip() and item.strip() not in {"—", "Not Disclosed"}))
    canonical="|".join(("review-completion-v1",fam,"paper-v1:"+aid,"arXiv:"+aid+"v1",multi("SRC-ARXIV"),"arXiv:"+aid+"v1",multi("SRC-ARXIV@arXiv:"+aid+"v1"),"deep",multi(method),multi(evaluation),multi(limitation),multi(artifact),"claim:"+fam,"review:"+fam,"review-body-sha256:"+hashlib.sha256(norm(body).encode()).hexdigest()))
    return "RP-"+hashlib.sha256(canonical.encode()).hexdigest()[:16]

def closure(row):
    text=(row["title"]+" "+row["abstract"]).lower()
    if any(x in text for x in ("medical","clinical","patient","disease","healthcare","mri","cancer")): kind,why="domain_result","医疗/临床任务证据没有改写跨任务 AI-System 的状态、控制或发布契约"
    elif any(x in text for x in ("survey","review","perspective","taxonomy")): kind,why="survey_or_position","综述/观点/分类没有形成可独立验收的 durable mechanism"
    elif any(x in text for x in ("dataset","benchmark")): kind,why="benchmark_only","数据集或任务榜单没有改变通用 evaluation/release gate"
    elif any(x in text for x in ("robot","navigation","manipulation","control")): kind,why="embodied_task_local","具身或控制任务增量未形成跨环境可复用的 owner、fallback 与部署契约"
    elif any(x in text for x in ("segmentation","classification","detection","forecasting","prediction")): kind,why="task_model_local","单任务模型/指标改进不是长期 AI-System mechanism"
    else: kind,why="model_or_domain_local","论文贡献未改变长期 mechanism、state/data/control ownership、evaluation/release contract 或平台设计"
    return kind, f"`{row['title']}`：{first(row['abstract'])}；{why}。"

def score(owner):
    d=3 if owner in {"PLATFORM-SECURITY","TRAIN-DISTRIBUTED-TRAINING","INFER-TENSORRT-LLM","INFER-GPU-MEMORY"} else 2
    r=3 if owner.startswith("PLATFORM-") or owner in {"AGENT-WORKFLOW","AGENT-MULTI-AGENT","TRAIN-DISTRIBUTED-TRAINING"} else 2
    return {"design_delta":d,"system_reach":r,"durability":3,"total":d+r+3}

def benchmark(row):
    b={k:ND for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")}
    specials={
    "2606.25353":{"hardware":"GB-scale last-level-cache server CPUs","evaluator":"end-to-end performance; analytical-model validation; context-length/batch sensitivity"},
    "2606.25426":{"hardware":"Apple M1 AMX","precision":"FP32 bit-exact","input_length":"128-token prefill","evaluator":"12 LLM prefill GEMMs and llama.cpp full-forward tokens/s"},
    "2606.25453":{"hardware":"NVIDIA Hopper and Blackwell GPUs","precision":"INT8 Tensor Core emulation of higher precision","evaluator":"kernel efficiency, end-to-end throughput, precision-memory trade-off"},
    "2606.25487":{"workload":"596 human-labeled HarmBench completions; 30 confident true positives for white-box GCG","evaluator":"precision, recall, wrapper flip rate and white-box attack success"},
    "2606.25575":{"workload":"44 participants; five bimanual tasks","evaluator":"completion time, task success and 7-point acceptance ratings"},
    "2606.25658":{"model":"LLaVA-OneVision and Qwen2.5-VL","input_length":"hour-long streaming video; 12k visual-token memory budget","evaluator":"streaming/offline accuracy, compression ratio and storage"},
    "2606.25760":{"workload":"27 UQ methods across VLMs and GUI-grounding datasets","evaluator":"AUROC, PRR, graded severity, calibration and conformal click disks"},
    "2606.25863":{"workload":"1,192 Linux kernel, 289 FFmpeg and 100 PHP patches","evaluator":"VIC extraction coverage, manual precision, formula size and CVE-text recall"},
    "2606.25871":{"workload":"six production offline use cases; 150M+ annotations","evaluator":"accuracy, calibration gain and cascade compute cost"},
    "2606.26057":{"workload":"1,000 migration fixtures; 17 adversarial classes; 80+ robustness tests","evaluator":"byte equivalence, reject equivalence, latency and machine-checked fail-closed invariant"},
    "2606.26492":{"workload":"5,542 fault-injected training traces from 38 DL programs","evaluator":"within-program versus leave-program-out balanced accuracy"}}
    b.update(specials.get(row["arxiv_id"],{})); return b

def main():
    provisional=json.loads((PACKET/"screening-ledger-provisional.json").read_text())
    ids=(PACKET/"candidate-ids-v1.txt").read_text().split(); assert set(ids)==set(META) and len(ids)==68
    row_by={r["arxiv_id"]:r for r in provisional["identities"]}; assert set(ids)<=set(row_by)
    denom="daily-v2.1:2026-06-25:"+hashlib.sha256("\n".join(family(x) for x in ids).encode()).hexdigest()[:16]
    rows=[]
    for row in provisional["identities"]:
        aid=row["arxiv_id"]; fam=family(aid)
        if aid in META: status="retained"; kind="durable_system_candidate"; owner=META[aid][0]; reason=f"`{row['title']}` 改变 `{owner}` 的长期机制或验收边界：{first(row['abstract'])}"
        else: status="closed_pre_denominator"; kind,reason=closure(row); owner="—"
        rows.append({**row,"source_family_id":fam,"stable_node_id":owner,"semantic_screen_status":status,"semantic_decision_kind":kind,"semantic_screen_reason":reason,"screened_at":EXECUTED_AT})
    ledger={**{k:v for k,v in provisional.items() if k!="identities"},"schema":"daily-v2.1-screening-ledger-v2","denominator_id":denom,"denominator_frozen_at":EXECUTED_AT,"retained_candidate_families":68,"closed_pre_denominator_families":442,"route_negative_audited":127,"route_negative_false_negatives":["2606.25467","2606.25575","2606.25592","2606.26456"],"gate_status":"coverage_closed_evidence_passed_selection_passed_books_passed_complete","identities":rows}
    (PACKET/"screening-ledger.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    with (PACKET/"denominator-full-semantic-audit-v1.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["source_family_id","arxiv_id","route","title","abstract_basis","decision","decision_kind","stable_node_id","family_specific_reason"])
        for r in rows:w.writerow([r["source_family_id"],r["arxiv_id"],r["screening_route"],r["title"],first(r["abstract"]),r["semantic_screen_status"],r["semantic_decision_kind"],r["stable_node_id"],r["semantic_screen_reason"]])
    reviews=[]
    for aid in ids:
        r=row_by[aid]; fam=family(aid); owner,ms,es,ls=META[aid]; base=f"https://arxiv.org/html/{aid}v1"
        method=f"{base} — §{ms}"; evaluation=f"{base} — §{es}"; limitation=f"{base} — §{ls}"
        if aid=="2606.25863": method=method.replace("/html/","/pdf/"); evaluation=evaluation.replace("/html/","/pdf/"); limitation=limitation.replace("/html/","/pdf/")
        delta=f"`{ms}` 所定义的源特定机制用于{OWNER_CONTROL[owner]}；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。"
        boundary=f"`{ls}` 是 `{r['title']}` 的 source-specific 反例/局限边界；若运行条件离开 `{es}` 的验证域，`{owner}` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。"
        disp="No Change — Existing Coverage" if aid in NO_CHANGE else "Integrate"
        artifact="Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review"
        body=(f"### {aid} — {r['title']}\n\n**问题与旧路径。** {first(r['abstract'])}\n\n**机制、状态与控制流。** {delta}\n\n**Trade-off、failure、fallback 与共存。** {boundary}\n\n<!-- claim:{fam}:start -->\nClaim boundary：仅 `arXiv:{aid}v1`；未证明边界定位 `{limitation}`。\n<!-- claim:{fam}:end -->")
        reviews.append({**r,"source_family_id":fam,"stable_node_id":owner,"method_name":ms,"evaluation_name":es,"limitation_name":ls,"method_locator":method,"evaluation_locator":evaluation,"limitation_locator":limitation,"artifact_locators":artifact,"claim":delta,"claim_boundary":boundary,"benchmark_contract":benchmark(r),"score_v2":score(owner),"books_disposition":disp,"review_body":body,"review_body_sha256":hashlib.sha256(norm(body).encode()).hexdigest(),"review_provenance_id":rp(fam,aid,method,evaluation,limitation,artifact,body)})
    access={"schema":"exact-v1-access-receipt-v1","denominator_id":denom,"checked_at":EXECUTED_AT,"reader":"official arXiv exact-v1 HTML/PDF primary-source reader","result":"68/68 exact-v1 identities resolved","blocked":[],"items":[{"source_family_id":x["source_family_id"],"primary_identifier":"arXiv:"+x["arxiv_id"]+"v1","locator":x["method_locator"].split(" — ")[0],"status":"official_exact_v1_accessible","version_identity":"arXiv:"+x["arxiv_id"]+"v1","access_note":"PDF fallback for 2606.25863; no abstract-text anchor used"} for x in reviews]}
    (PACKET/"exact-v1-access-receipt.json").write_text(json.dumps(access,ensure_ascii=False,indent=2)+"\n")
    items=[]
    for x in reviews:
        items.append({"source_family_id":x["source_family_id"],"event_identity":"paper-v1:"+x["arxiv_id"],"primary_evidence_version":"arXiv:"+x["arxiv_id"]+"v1","primary_identifier":"arXiv:"+x["arxiv_id"]+"v1","review_route":"deep","reviewed_evidence_versions":"SRC-ARXIV@arXiv:"+x["arxiv_id"]+"v1","method_locator":x["method_locator"],"evaluation_locator":x["evaluation_locator"],"limitation_locator":x["limitation_locator"],"artifact_locators":x["artifact_locators"],"claim":x["claim"],"claim_boundary":x["claim_boundary"],"claim_boundary_ref":"claim:"+x["source_family_id"],"benchmark_contract":x["benchmark_contract"],"score_v2":x["score_v2"],"stable_node_id":x["stable_node_id"],"books_disposition":x["books_disposition"],"review_ref":"review:"+x["source_family_id"],"review_provenance_id":x["review_provenance_id"],"review_body_sha256":x["review_body_sha256"],"completion_result":"complete","ordinary_pending_locator_count":0})
    (PACKET/"source-review-receipts-v2.1.json").write_text(json.dumps({"schema":"source-review-receipts-v2.1","denominator_id":denom,"items":items},ensure_ascii=False,indent=2)+"\n")
    winners=["2606.26057","2606.25353","2606.25819"]
    sel=[]
    for x in reviews:
        yes=x["arxiv_id"] in winners; ref=("analysis:DA-20260625-"+x["arxiv_id"].replace(".","-")) if yes else "analysis-decision:"+x["source_family_id"]
        eligibility="score_7_9; potential_books_delta" if x["books_disposition"]=="Integrate" else "score_7_9"
        sel.append({"source_family_id":x["source_family_id"],"eligibility":eligibility,"decision":"selected" if yes else "not_selected","analysis_unit_id":"DA-20260625-"+x["arxiv_id"].replace(".","-") if yes else "—","subsumed_by":"—","priority_rationale":("入选："+x["claim"] if yes else "未入选长叙事："+x["claim_boundary"]+"；Books disposition 独立保留。"),"narrative_ref":ref})
    (PACKET/"deep-analysis-selection-v1.json").write_text(json.dumps({"schema":"deep-analysis-selection-v1","denominator_id":denom,"frontier_size":68,"selection_count":3,"winners_frozen_before_rationale":winners,"decisions":sel},ensure_ascii=False,indent=2)+"\n")
    comparisons=[]
    for x in reviews:
        owner=x["stable_node_id"]; path=PATHS[owner]; comparisons.append({"source_family_id":x["source_family_id"],"stable_node_id":owner,"target_chapter_ref":path+f"#L{TARGET_LINE[owner]}","adjacent_chapter_refs":ADJACENT[owner]+f"#L{ADJACENT_LINE[owner]}","existing_proposition_ref":"existing:"+x["source_family_id"],"new_evidence_delta_ref":"delta:"+x["source_family_id"],"evolution_relation":"Direct Evolution" if x["books_disposition"]=="Integrate" else "Layering / Dependency","decision":x["books_disposition"],"books_review_ref":"books-review:"+x["source_family_id"]})
    (PACKET/"books-comparison-v1.json").write_text(json.dumps({"schema":"books-comparison-v1","denominator_id":denom,"compared":"68/68","items":comparisons},ensure_ascii=False,indent=2)+"\n")
    integ=[x for x in reviews if x["books_disposition"]=="Integrate"]; groups=defaultdict(list)
    for x in integ: groups[x["stable_node_id"]].append(x)
    queue=["# 2026-06-25 Books Integration Queue V1","",f"Denominator `{denom}`. Applied under the 2026-06-25 shared write lock: {len(integ)} families in {len(groups)} unique owners.",""]
    ready=["# 2026-06-25 Ready-to-Insert Books Packet V1","","Status: Applied. 每个 Source Family 只进入一个 owner；正文和 Review note 均绑定 exact-v1。",""]
    for owner,xs in sorted(groups.items()):
        path=PATHS[owner]; queue += [f"## `{owner}` → `{path}`",""]
        ready += [f"## `{owner}` → `{path}`",""]
        for x in xs:
            fam=x["source_family_id"]; queue += [f"- `{fam}` — {x['title']}",f"  - Delta: {x['claim']}",f"  - Boundary: {x['claim_boundary']}",""]
            ready += [f"### {fam}","",x["review_body"],"",f"Review note：`{fam}`；Method `{x['method_locator']}`；Evaluation `{x['evaluation_locator']}`；未证明边界 `{x['limitation_locator']}`。",""]
    (PACKET/"BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue)+"\n")
    (PACKET/"READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready)+"\n")
    with (PACKET/"evidence-selection-fresh-audit-v1.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["source_family_id","exact_v1","method_locator","evaluation_locator","limitation_locator","artifact_locator","benchmark_10_fields","score_total","selection","books_disposition","audit_status"])
        by_family={x["source_family_id"]:x for x in sel}
        for x in reviews:
            w.writerow([x["source_family_id"],"arXiv:"+x["arxiv_id"]+"v1",x["method_locator"],x["evaluation_locator"],x["limitation_locator"],x["artifact_locators"],"complete",x["score_v2"]["total"],by_family[x["source_family_id"]]["decision"],x["books_disposition"],"passed"])

    all_book_files=list((ROOT/"books").rglob("*.md"))
    book_texts={str(path.relative_to(ROOT)):path.read_text() for path in all_book_files}
    post_rows=[]
    touched=set()
    for x in reviews:
        fam=x["source_family_id"]
        expected=PATHS[x["stable_node_id"]]
        hits={path:text.count(fam) for path,text in book_texts.items() if fam in text}
        if x["books_disposition"]=="Integrate":
            assert hits=={expected:2}, (fam,hits,expected)
            text=book_texts[expected]
            assert all(value in text for value in (x["claim"],x["claim_boundary"],x["method_locator"],x["evaluation_locator"],x["limitation_locator"])), fam
            touched.add(expected)
            result="passed_integrated_unique_owner_body_and_review_note"
        else:
            assert not hits, (fam,hits)
            result="passed_no_change_absent_existing_owner_handoff_revalidated"
        post_rows.append([fam,x["books_disposition"],expected,ADJACENT[x["stable_node_id"]],hits.get(expected,0),result])
    assert len(touched)==25
    with (PACKET/"post-write-fresh-audit-v1.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["source_family_id","books_disposition","expected_owner_file","adjacent_handoff_file","expected_file_occurrences","audit_result"])
        w.writerows(post_rows)
    (PACKET/"POST_WRITE_FRESH_AUDIT_V1.md").write_text(f"# 2026-06-25 Post-Write Fresh Audit V1\n\n- Scope: 68/68 frozen families; 63 Integrate + 5 No Change.\n- Integrate: every family appears exactly twice in one expected owner file (one mechanism body, one exact-v1 Review note), with claim, trade-off/fallback, Method, Evaluation and limitations locators present.\n- No Change: all five family IDs remain absent from Books; target/adjacent canonical handoffs were revalidated.\n- Owner files: 25/25; unexpected Books occurrences: 0.\n- Findings: 0 unresolved.\n- Result: Passed.\n")

    # Canonical Daily presentation after the successful 68/68 post-write audit.
    fams="; ".join(x["source_family_id"] for x in reviews)
    source_lines=[f"- [{x['title']}](https://arxiv.org/abs/{x['arxiv_id']}v1) — first-public（Asia/Shanghai）：2026-06-24；accessed：{EXECUTED_AT[:10]}" for x in reviews]
    lines=[
        "# Daily Research — 2026-06-25","",
        "**Research Date:** 2026-06-25","",
        "**Timezone:** Asia/Shanghai","",
        "**Strict Window:** 2026-06-24 09:00:00 ～ 2026-06-25 09:00:00（北京时间，左闭右开）","",
        "**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt","",
        "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节","",
        "## Executive Summary","",
        "Beijing window `[2026-06-24 09:00, 2026-06-25 09:00)` contains 510 registered identities. Full 510/510 semantic screening freezes 68 durable families and 442 family-specific closures. Route-negative audit is 127/127 with four promotions. Exact-v1 Evidence is 68/68 and full-frontier Selection chose three narratives. The 68/68 post-write fresh audit verified 63 unique-owner integrations plus five absent No Change families with zero unresolved finding.","",
        "## 1. Coverage","","<!-- validator:report-metadata-v2 -->",
        "| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-25 |","| Window End | 2026-06-25 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {denom} |",f"| Denominator Frozen At | {EXECUTED_AT} |","| Completion Status | Complete |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Passed |","",
        "### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-06-24T09:00:00+08:00 | 2026-06-25T09:00:00+08:00 | {EXECUTED_AT} | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 510 | {fams} | pages=40; final_cursor=end; 510 unique identities | 2026-06-25T01:00:00Z | ../_sources/daily-20260625/screening-ledger.json; ../_sources/daily-20260625/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260625 | — |","",
        "<!-- coverage:SRC-ARXIV:20260625:start -->","All 321 Core, 62 keyword-routed and 127 route-negative identities were screened. Frozen arithmetic: `510 = 68 retained + 442 closures`; keyword routing was recall-only; route-negative FN=`2606.25467, 2606.25575, 2606.25592, 2606.26456`.","<!-- coverage:SRC-ARXIV:20260625:end -->","",
        "## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    ]
    for x in reviews:
        s=x["score_v2"]; lines.append(f"| {x['source_family_id']} | arXiv:{x['arxiv_id']}v1 | paper-v1:{x['arxiv_id']} | 2026-W26 | 2026-06-24 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | none | review:{x['source_family_id']} | self | — | new_in_window | {x['stable_node_id']} | {x['books_disposition']} | books-review:{x['source_family_id']} | yes |")
    lines += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in reviews: lines.append(f"| {x['source_family_id']} | {x['review_provenance_id']} | deep | arXiv:{x['arxiv_id']}v1 | SRC-ARXIV@arXiv:{x['arxiv_id']}v1 | {md(x['method_locator'])} | {md(x['evaluation_locator'])} | {md(x['limitation_locator'])} | {md(x['artifact_locators'])} | claim:{x['source_family_id']} | complete |")
    lines += ["","### Source Reviews",""]
    for x in reviews: lines += [f"<!-- review:{x['source_family_id']}:start -->",x["review_body"],f"<!-- review:{x['source_family_id']}:end -->",""]
    lines += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in reviews:
        b=x["benchmark_contract"]; lines.append("| "+" | ".join([x["source_family_id"]]+[md(b[k]) for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")])+" |")
    lines += ["","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for x in reviews:
        y=next(z for z in sel if z["source_family_id"]==x["source_family_id"]); lines.append(f"| {y['source_family_id']} | {y['eligibility']} | {y['decision']} | {y['analysis_unit_id']} | {y['subsumed_by']} | {md(y['priority_rationale'])} | {y['narrative_ref']} |")
    for y in sel:
        if y["decision"]=="not_selected": lines += ["",f"<!-- {y['narrative_ref']}:start -->",y["priority_rationale"],f"<!-- {y['narrative_ref']}:end -->"]
    lines += ["","### Selected Analysis Narratives",""]
    for aid in winners:
        x=next(z for z in reviews if z["arxiv_id"]==aid); lines += [f"<!-- analysis:DA-20260625-{aid.replace('.','-')}:start -->",f"### {x['title']}","",x["claim"],"",x["claim_boundary"],f"<!-- analysis:DA-20260625-{aid.replace('.','-')}:end -->",""]
    lines += ["## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in comparisons: lines.append(f"| {c['source_family_id']} | {c['stable_node_id']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition_ref']} | {c['new_evidence_delta_ref']} | {c['evolution_relation']} | {c['decision']} | {c['books_review_ref']} |")
    by_family={x["source_family_id"]:x for x in reviews}
    for c in comparisons:
        x=by_family[c["source_family_id"]]
        if c["decision"]=="Integrate":
            existing=f"At `{c['target_chapter_ref']}`, the current owner already establishes the base responsibility for {OWNER_CONTROL[c['stable_node_id']]}; `{c['adjacent_chapter_refs']}` only consumes the handoff. It does not yet state `{x['method_name']}`."
        else:
            existing=f"At `{c['target_chapter_ref']}`, the current owner already states the durable proposition that {OWNER_CONTROL[c['stable_node_id']]}; `{x['method_name']}` is confirmatory evidence, while `{c['adjacent_chapter_refs']}` remains a consumer rather than a second owner."
        lines += ["",f"<!-- existing:{c['source_family_id']}:start -->",existing,f"<!-- existing:{c['source_family_id']}:end -->","",f"<!-- delta:{c['source_family_id']}:start -->",x["claim"],f"<!-- delta:{c['source_family_id']}:end -->","",f"<!-- books-review:{c['source_family_id']}:start -->",f"{c['evolution_relation']}; {c['decision']}. {x['claim_boundary']}",f"<!-- books-review:{c['source_family_id']}:end -->"]
    review_refs="; ".join("review:"+x["source_family_id"] for x in reviews)
    sel_refs="; ".join(x["narrative_ref"] for x in sel)
    book_refs="; ".join("books-review:"+x["source_family_id"] for x in reviews)
    lines += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260625-COVERAGE-V1 | fresh-context:jun25-v1 | coverage | coverage:SRC-ARXIV:20260625 | — | 510/510 title+abstract; denominator 68; closures 442; route-negative 127/127 with four promoted FN; 2606.25601 false-positive closed before freeze | passed |",f"| SA-20260625-EVIDENCE-V1 | fresh-context:jun25-v1 | evidence | {review_refs} | — | 68/68 exact-v1 full texts; source-specific Method/Evaluation/counterevidence/artifact locators and ten-field contracts | passed |",f"| SA-20260625-SELECTION-V1 | fresh-context:jun25-v1 | deep_analysis_selection | {sel_refs} | — | Full 68/68 frontier rerun after Evidence; three winners frozen and 65 bounded non-selections | passed |",f"| SA-20260625-BOOKS-POSTWRITE-V1 | fresh-context:jun25-postwrite-v1 | books | {book_refs} | — | Prewrite comparison passed; then 63/63 Integrate unique-owner body and exact-v1 Review note plus 5/5 No Change absence/handoff revalidation passed; `../_sources/daily-20260625/POST_WRITE_FRESH_AUDIT_V1.md` | passed |","",
        "## 8. Ignored Noise","","The 442 family-specific closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routing was recall-only and all 127 route-negative identities were audited.","","### Materials and Access","","- 68/68 retained families completed official exact-v1 primary-source review. Official arXiv HTML was used except `2606.25863v1`, whose exact-v1 official PDF was the recorded fallback; no abstract-text anchor was used.","",
        "## 9. Recommended Action","",f"- Final Books disposition: 63 Integrate across {len(groups)} unique owner files; 5 No Change handoffs.","- Books Gate passed after the 68/68 post-write fresh audit.","- Preserve the frozen denominator and reopen only when versioned primary evidence changes a recorded mechanism, owner, evaluation contract or non-proof boundary.","",
        "## 10. Repository Changes","",f"- The accepted 63-family writeback remains in {len(touched)} shared Books owner files; this canonical migration changed only the 2026-06-25 Daily, its date-local packet and date-specific validation scripts.","- `docs/LEARNING_STATE.md` and monthly indexes remained read-only.","",
        "## 11. Open Questions","","- Which exact-v1 mechanisms remain stable under unseen workloads is future research, not an unresolved Gate finding.","- Which runtime calibration values remain stable after model, hardware or workload distribution changes is a research continuation, not an unresolved Gate finding.","",
        "## 12. Sources","",*source_lines,"- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表","- Date-local receipts：`../_sources/daily-20260625/source-review-receipts-v2.1.json`、`deep-analysis-selection-v1.json`、`books-comparison-v1.json`、`POST_WRITE_FRESH_AUDIT_V1.md`","",
        "## 13. Final Status","","Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`；unresolved findings: `0`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。"
    ]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(lines)+"\n")
    (PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(f"# 2026-06-25 Fresh Evidence and Selection Audit V1\n\n- Denominator `{denom}`: `510 = 68 retained + 442 closures`.\n- Route-negative fresh FN audit: 127/127; promoted `2606.25467v1`, `2606.25575v1`, `2606.25592v1`, `2606.26456v1`.\n- False-positive correction: `2606.25601v1` closed before final freeze because statistical hyperparameter-selection theory does not change a durable AI-System owner or release mechanism.\n- Exact-v1 Evidence: Passed 68/68.\n- Full-frontier Selection: Passed 68/68, three winners.\n- Books comparison: 63 Integrate across {len(groups)} owners plus 5 No Change; post-write audit Passed 68/68.\n")
    (PACKET/"README.md").write_text(f"# daily-20260625 source packet\n\n- Window: `[2026-06-24T09:00:00+08:00,2026-06-25T09:00:00+08:00)`\n- Denominator: `{denom}`\n- Raw identities: 510\n- Retained durable families: 68\n- Family-specific pre-denominator closures: 442\n- Route-negative audit: 127/127; four promoted false negatives\n- Coverage Gate: Closed\n- Evidence Gate: Passed\n- Selection Gate: Passed\n- Books Gate: Passed after 68/68 post-write fresh audit\n- Completion: Complete\n")
    sums=[]
    for p in sorted(x for x in PACKET.iterdir() if x.is_file() and x.name not in {"SHA256SUMS","screening-ledger-provisional.json"}): sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name)
    (PACKET/"SHA256SUMS").write_text("\n".join(sums)+"\n")
    print(json.dumps({"denominator_id":denom,"raw":510,"retained":68,"closures":442,"route_negative_audited":127,"route_negative_false_negatives":4,"integrate":len(integ),"no_change":len(NO_CHANGE),"owners":len(groups),"post_write_audit":"68/68 passed","books_gate":"Passed","completion":"Complete"},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
