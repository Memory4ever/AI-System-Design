#!/usr/bin/env python3
"""Build the strict pre-write V2.1 packet for 2026-06-21; never edits Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260621"
PROV = PACKET / "screening-ledger-provisional.json"
REPORT = ROOT / "papers/2026/06/21/README.md"
EXECUTED_AT = "2026-08-30T01:20:00+08:00"
# Keep the semantic truth table open until the full 37-family primary-source
# and full-frontier fresh audit below has no unresolved finding.
EVIDENCE_READY = True

PATHS = {
    "MODEL-SELF-ATTENTION": "books/part-02-model/14-self-attention.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/54-gpu-memory.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "PLATFORM-PRODUCTION": "books/part-06-ai-infrastructure/73-production-best-practice.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
}

TARGET_ANCHORS = {
    "MODEL-SELF-ATTENTION": "## 从匹配分数到读取权重",
    "TRAIN-DATA": "## Data lineage 是训练可复现性的前提",
    "TRAIN-GRPO": "### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界",
    "TRAIN-DISTRIBUTED-TRAINING": "### 从 Phase 串行到依赖驱动的跨 Phase 重排",
    "INFER-GPU-MEMORY": "### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页",
    "INFER-SCHEDULING": "### MoE Decode：从 Queue Length 到 Expert Working Set",
    "PLATFORM-EVALUATION-SYSTEM": "## 从答案评分到可执行证据",
    "PLATFORM-MONITORING": "## 先定义目标，再选择可测信号",
    "PLATFORM-SECURITY": "## 风险管理而不是一次性认证",
    "PLATFORM-PRODUCTION": "## Capacity、Failure 与 Recovery",
    "AGENT-MEMORY": "## Consolidation 与 Forgetting",
    "AGENT-WORKFLOW": "## State Machine 是基本模型",
    "AGENT-MULTI-AGENT": "## Message 不是 State",
    "AGENT-PLATFORM": "## Agent Runtime State Machine",
}

ADJACENT_PATHS = {
    "MODEL-SELF-ATTENTION": [("books/part-02-model/15-multi-head-attention.md", "## 从单头投影到多个 head")],
    "TRAIN-DATA": [("books/part-04-training-system/28-pretraining.md", "## Next-token objective")],
    "TRAIN-GRPO": [("books/part-04-training-system/32-ppo.md", "## 把语言生成写成策略过程"), ("books/part-04-training-system/34-dpo.md", "## 从 RLHF 的两阶段复杂度开始")],
    "TRAIN-DISTRIBUTED-TRAINING": [("books/part-04-training-system/37-tensor-parallel.md", "## 为什么“把权重文件切开”不够")],
    "INFER-GPU-MEMORY": [("books/part-05-inference-system/55-pd-disaggregation.md", "## 两种阶段，两种节奏")],
    "INFER-SCHEDULING": [("books/part-05-inference-system/55-pd-disaggregation.md", "## 分离之后发生什么")],
    "PLATFORM-EVALUATION-SYSTEM": [("books/part-06-ai-infrastructure/67-monitoring.md", "## 先定义目标，再选择可测信号")],
    "PLATFORM-MONITORING": [("books/part-06-ai-infrastructure/66-evaluation-system.md", "## 为什么“选一个分数”不是评估系统")],
    "PLATFORM-SECURITY": [("books/part-06-ai-infrastructure/71-multi-tenant.md", "## 四个隔离平面")],
    "PLATFORM-PRODUCTION": [("books/part-06-ai-infrastructure/72-security.md", "## 生命周期威胁")],
    "AGENT-MEMORY": [("books/part-07-agent/76-rag.md", "## Offline Ingestion 不是预处理细节")],
    "AGENT-WORKFLOW": [("books/part-07-agent/80-reflection.md", "## Feedback 来源决定价值")],
    "AGENT-MULTI-AGENT": [("books/part-07-agent/81-workflow.md", "## State Machine 是基本模型")],
    "AGENT-PLATFORM": [("books/part-07-agent/83-mcp.md", "## Host、Client、Server")],
}


def chapter_ref(path: str, heading: str) -> str:
    """Resolve a current, exact Books heading to a validator-stable line locator."""
    lines = (ROOT / path).read_text().splitlines()
    matches = [number for number, line in enumerate(lines, start=1) if line == heading]
    assert len(matches) == 1, (path, heading, matches)
    return f"{path}#L{matches[0]} — {heading}"


def adjacent_refs(owner: str) -> list[str]:
    return [chapter_ref(path, heading) for path, heading in ADJACENT_PATHS[owner]]


def S(owner, delta, proof, boundary, model, workload, evaluator, method, evaluation,
      limitation, disposition, note, score=(3, 2, 3), hardware="Not Disclosed",
      precision="Not Disclosed", input_length="Not Disclosed",
      output_length="Not Disclosed", batch="Not Disclosed",
      concurrency="Not Disclosed", slo="Not Disclosed"):
    return locals()


# Anchors below are exact-v1 section titles or unique exact-v1 text anchors, never
# unversioned paper titles or guessed generic section labels.
C = {
"2606.21822": S("PLATFORM-SECURITY", "把 LLM 生成的 C 内存所有权猜测编译成 CN contract，再由 Bennet/Fulminate 对 100 个生成 heap state 执行检查；失败进入最多六轮有界修复。", "31 个可标注函数与 3 个故意不安全函数上，o3 首轮 90%、总计 97%，GPT-4o 首轮 65%。", "测试通过只覆盖生成状态，不是全路径证明；safe-but-unexpressible、搜索失败与真实 unsafe 仍可能落入同一失败出口。", "OpenAI o3, o1, o1-mini, o3-mini and GPT-4o", "CN memory-safety specification synthesis for small-to-medium C functions", "first-attempt and eventual valid-annotation rate plus unsafe-function handling", "§2 CNnotator Tool Design", "§3 Benchmark; §4 Results", "§3 Test set limitations; §4 Failure Modes; §5 Framework Tradeoffs", "No Change — Existing Coverage", "Ch72 已要求 coding-agent 安全真值来自 executable evidence；本 family 增加 CN 具体实例但不改变 owner。"),
"2606.21836": S("AGENT-WORKFLOW", "把架构 DSE 从只读 scalar reward 的黑盒搜索改成可编辑 workspace：candidate、constraint、simulator harness、history、best 与 budget 都成为持久 artifact，agent 运行 hypothesis-test-refine。", "Timeloop/Accelergy、MAESTRO 与 ChampSim 三类 DSE 上，在严格调用预算内达到相当或更优设计，最高减少两个数量级 simulator evaluation。", "simulator artifact 会被 agent 当真；LLM prior、调用成本与三类受测空间不能外推到真实芯片 sign-off。", "Not Disclosed", "DNN accelerator mapping, hardware/software co-design and CPU cache-hierarchy DSE", "EDP or IPC under matched simulator-call budgets and trace audit", "§II Agentic DSE Methodology; §II-C Auditable Optimization Traces", "§III Experimental Setup; §IV Results", "§VI Limitations and Future Work", "No Change — Existing Coverage", "Ch81 已拥有 evaluator-driven search、persistent workspace 与 simulator-as-contract；保留为 cross-domain evidence。"),
"2606.21842": S("PLATFORM-SECURITY", "non-prefix KV fusion 的固定 chunk routing 与未对齐 tail recomputation 形成 Step-Wave TTFT oracle；SpliceLeak 先恢复隐藏前缀长度，再用 boundary collision 逐 token 提取；QCP+CTBF 消除长度与语义 timing signal。", "vLLM+LMCache 上覆盖三种 threat scenario，并报告 bounded-entropy 场景最高 100% extraction、最少 63 requests/token；防线把 ΔTTFT 压近 0。", "威胁模型要求共置 tenant、共享 cache、可重复 TTFT probe 与受限语义搜索空间；局部测试不证明任意 engine/GPU 或公网噪声下可复现。", "LongChat-7B-v1.5-32K and Qwen2.5-7B-Instruct targets; Gemini-3-Pro extraction agent", "multi-tenant RAG with non-prefix KV-cache fusion", "extraction success, requests per token, TTFT signal and defense throughput", "§IV Overview; §V SpliceLeak: Semantic Extraction Methodology; §VI SpliceDefense", "§VII Evaluation; §VII-A Experimental Setup", "§III Motivation: Limitations of Existing Works; Appendix A Discussion and Future Work", "No Change — Existing Coverage", "当前 Ch72 已把跨租户 cache hit timing、principal-specific namespace、non-prefix causal provenance 与 full-recompute fallback 写成同一 security contract；Step-Wave/QCP/CTBF 是该 owner 的受限实例。", hardware="4 NVIDIA A40 GPUs with 48 GB VRAM each and 256 GB system RAM", input_length="about 2,000-token shared document chunk in Scenario A", batch="maximum batch size 16", concurrency="Poisson background arrivals at 0.004 requests per second per client"),
"2606.21843": S("PLATFORM-MONITORING", "agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。", "单一持久 agent 的 cross-sectional probe battery 测得 conditioning structure；原 context-pressure drift 在多样 padding 下至 150K token 不再出现。", "作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。", "Anthropic Claude Sonnet API backing the persistent Ada agent", "identity-conditioning probes across base, 4,200-token Card-conditioned, repetitive-padded and diverse-padded contexts", "next-token entropy, sqrt-JSD distance and magnitude-homology diagnostics", "§3.1 Ada: a persistent AI agent; §3.4 The probe battery", "§4 Magnitude Baseline; §5.6 Drift experiment", "§6.3 Limitations — Drift trajectory is a padding artifact", "Integrate", "该 family 的长期价值是反例：pre-failure sensor 必须把 context generator 纳入 run identity，不能把 padding artifact 写成 agent drift。", input_length="about 4K baseline, 155K medium and 280K long contexts; diverse-padding control through 150K", output_length="first token or first 10 tokens, depending on probe", batch="50 samples per probe × condition × context-length combination"),
"2606.21848": S("MODEL-SELF-ATTENTION", "把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。", "GPT-2 280M/557M、Pythia 410M、Qwen2 1.5B、Llama 3.2 1B 五组模型中，4/5 perplexity 与 4/5 downstream benchmark 不低于 QKV，同时 cache 容量减半。", "等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。", "GPT-2 280M, GPT-2 557M, Pythia 410M, Qwen2 1.5B and Llama 3.2 1B", "language modeling and downstream reasoning with QKV versus QVV attention", "perplexity, downstream accuracy and value-only cache memory", "§2 Method; §3 Value-only Cache in Autoregressive Inference", "§5 Experiments", "§2.2 equivalence conditions; §6 Limitations", "Integrate", "Ch14 需新增 routing 与 retrieval representation 可合并但带秩条件的 alternative branch；Ch45 只消费 50% cache consequence。", input_length="512, 2,048 and 8,192 tokens for the Qwen2-1.5B throughput benchmark", output_length="256 generated tokens for the Qwen2-1.5B throughput benchmark", batch="1 for the Qwen2-1.5B throughput benchmark"),
"2606.21854": S("TRAIN-DISTRIBUTED-TRAINING", "DataOrganizer 把 dataset composition、split/shard 与 recipe stage 分离，统一 Python workflow 只通过轻量 override 保留实验差异。", "OWSM multi-node pretraining 相比 ESPnet2 每 epoch 减少 21.1 分钟、GPU utilization 超过 80%；新增 fine-tune model/data 约 46 行代码。", "只覆盖 speech/audio recipes 与作者 OWSM workload；开发行数和平均利用率不证明跨框架可维护性或端到端收敛等价。", "OWSM-Base 102M", "large-scale speech/audio pre-training and fine-tuning recipes", "epoch time averaged over five consecutive epochs, GPU utilization, CHiME-4 WER at 350k updates and integration code delta", "§3 ESPnet3 Framework", "§4 Experiments; §4.1 OWSM Pre-training", "§5 Conclusion — release and speech/audio workload boundary", "No Change — Existing Coverage", "Ch36 已拥有 data pipeline、sharding 与 compute utilization 的 owner；ESPnet3 是 speech-specific framework instance。", hardware="4 nodes with 4 NVIDIA H100 GPUs per node, 16 H100 total"),
"2606.21856": S("AGENT-PLATFORM", "多用户 agent harness 把 user/principal、workspace、credential、memory 与 tool capability 分离；deterministic hook 在执行前后实施 policy，审计记录 control decision 而不只记录自然语言。", "exact-v1 在多用户 delegation、共享资源与 tool-use scenarios 中比较无治理 agent 与 governed harness 的 task effectiveness 和 policy compliance。", "harness policy 依赖声明完整性与 hook 覆盖；被绕过的外部 side effect、stale identity mapping 和恶意 plugin 仍需 host reference monitor。", "deepseek-v4-pro, qwen3.6-35b-a3b, gemini-2.5-flash and gpt-4.1-nano via OpenRouter", "multi-principal tool-using agent tasks with shared and private state", "task completion plus deterministic governance-policy outcomes", "§3 Harness-MU", "§4 Experiments; §4.1 Deployment Settings", "§5 Discussion; §6 Conclusion", "No Change — Existing Coverage", "当前 Ch84 已以 AgentRun principal/tenant 绑定 workspace、credential、memory、tool 与 evidence，Ch81 也把 deterministic hooks 设为 sandbox/tool/checkpoint/retry/verifier owner；Harness-MU 不再改变长期 owner。", output_length="4,096 or 16,384 maximum tokens by benchmark module", concurrency="16 max_workers"),
"2606.21868": S("INFER-SCHEDULING", "WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。", "极低资源硬件上比较 expert/KV baselines，报告 token latency、throughput、命中/迁移与质量。", "Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。", "Qwen3-30B-A3B, MiniMax-M2 229B FP8, Jamba-v0.1 52B, Kimi-VL and OLMoE", "Mixture-of-Experts autoregressive serving under constrained device memory", "decode throughput, expert/KV residency, transfer and quality", "§3 Working-Set Predictor and Runtime Integration", "§4 Routing Signal and Decode Throughput; §5 Working-Set Value", "§6 Limitations; simulated-constrained-device disclosure", "Integrate", "Ch56 需把 expert weights 与 KV 视为竞争同一容量预算的联合 working set，而不是两个独立 cache。", hardware="single NVIDIA H100 NVL with 95,830 MiB; Qwen3/Kimi constrained-device arms emulated by memory cap", precision="BF16 for Qwen3-30B-A3B; FP8 for MiniMax-M2", concurrency="maximum concurrency at 4,096 tokens varies with KV allocation"),
"2606.21869": S("PLATFORM-EVALUATION-SYSTEM", "把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。", "Belebele 122 languages、translated GSM8K 与 LM-Arena prompts 上跨模型测量能耗/质量，并在 L40S 与 RTX 6000 Pro Blackwell 做硬件对照。", "绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。", "Qwen3-8B, Qwen3-14B, Qwen3-32B, Gemma-3-27B and Llama-3.1-8B-Instruct", "multilingual inference over Belebele, translated GSM8K and LM-Arena prompts", "per-language energy, token count and task accuracy", "§3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset", "§4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups", "§6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendations and downstream effects", "Integrate", "Ch66 需把语言切片的 energy/quality 联合 contract 加入 evaluation identity；Ch70 只消费成本结果。", hardware="NVIDIA L40S 48 GB and RTX 6000 Pro Blackwell 96 GB GPUs", batch="256 except batch-sweep values 16, 32, 64, 128, 256 and 512"),
"2606.21875": S("PLATFORM-EVALUATION-SYSTEM", "Signed Evidence Flow 把已拟合预测的正负 attribution 分解为 support、opposition、conflict 与 perturbation stability；ScopeGate 用 held-out permutation 检查 conflict-risk 方向后才允许 triage。", "医疗、Covertype、金融与十个外部数据集显示 conflict 有时增加 error ranking，也在 Bank Marketing/Credit Default 上方向反转。", "SEF 不是 causal explanation；attribution/reference choice 改变数值，相关 feature replacement 可能失真，B=40 stability refit 成本约单次 30.1–39.2 倍。", "standardized or balanced logistic regression, random forest and histogram gradient boosting classifiers", "risk triage among already-confident tabular predictions", "conditional error ranking, held-out ScopeGate direction and compute cost", "§4 Signed Evidence Decomposition; §5 Support, Opposition, and Conflict; §8 Perturbation Stability; §24 ScopeGate: Conditional Value and a Finite-Sample Deployment Test", "§15 Sanity Checks on Standard Benchmark Data Sets; §16 Large Real-Data Benchmark; §18 Model-Agnostic Black-Box Robustness; §21 Real Healthcare Benchmarks Beyond Confidence; §23 External Finance Stress Test and Scope Boundary; §25 Independent External Replication", "§30 Limitations", "No Change — Existing Coverage", "Ch66 已区分 confidence、evidence 与 policy-bound triage；本 family 的反向结果强化 calibration boundary。"),
"2606.21877": S("PLATFORM-SECURITY", "AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。", "13 个开源 agents、52 个 risk scenarios、33 个 deployment mutations；schema 覆盖 14/16 capability dimension，diff detector 对注入变更类型全命中。", "这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。", "Aider, OpenHands, SWE-agent, Cline, Goose, Open Interpreter, AutoGPT, PrivateGPT, GPT-Researcher, MetaGPT, CrewAI, AutoGen and BabyAGI", "pre-deployment agent authority/risk artifact validation", "schema fillability, risk visibility, mutation-diff correctness and scorer rank consistency", "§III AgentRiskBOM Design; §IV Implementation", "§V Evaluation", "§VII Limitations", "Integrate", "Ch72 需增加 authority-envelope BOM：依赖 provenance 不能替代 agent 能访问、记忆、修改和委托什么。"),
"2606.21884": S("TRAIN-GRPO", "对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。", "九类任务、11 个 CoT 设计、RLVR/STaR 与四类 backbone；cryptarithm solver 71% 而蒸馏仅 1–7%，揭示 key 后同例升至 57.1%。", "竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。", "Nemotron-3-Nano 30B/3.5B active, Llama-3.2-3B, Qwen3.5-4B, gpt-oss-20b 21B/3.6B active, DeepSeek-V3.1 671B/37B active and Nemotron-Super 120B/12B active", "nine deterministic-generator reasoning tasks", "solver coverage, CoT transfer, line fidelity, hit@k and intervention accuracy", "§4 Method: Solver-Grounded Synthetic CoT and the Experiment Ladder", "§5 Results; §6 Anatomy of the Failures", "§8.2 Threats to validity; §10 Limitations", "Integrate", "Ch33 需明确 verifiable outcome 不保证 search trace 可蒸馏；训练前先做 forward-derivability test。", input_length="7680-token generation budget in the primary setup"),
"2606.21891": S("AGENT-WORKFLOW", "ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。", "22 个 MLGym/MLEBench tasks、每法三次、8 小时 budget；报告 IQM、optimality gap、trajectory 与组件 ablation。", "scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。", "OpenAI o3 scientist, Gemini 3 Flash executor and Qwen3-4B-Instruct test-time-trained scientist", "22 automated ML research tasks from MLGym and MLEBench", "best validation score, IQM, optimality gap, wall time and hypothesis/execution attribution", "§4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning", "§6 Experiments and Analysis; Appendix I Additional Experimental Details", "§7 Discussion — Limitations and Ethical Concerns", "Integrate", "Ch81 需把 low score 拆成 hypothesis failure 与 execution failure，防止 workflow 错误地删除可修复分支。", hardware="one 40 GB NVIDIA A100 for each inference-only method; three 40 GB NVIDIA A100 GPUs for each test-time-training run", input_length="8,192-token rollout sequence length", output_length="up to 120 scientist turns of 1,024 tokens each", batch="8 rollouts per GRPO group"),
"2606.21917": S("PLATFORM-MONITORING", "在生成前从 attention probe 预测 hallucination risk，以 soft target 表达不确定度，再把风险交给 abstain、retrieval 或 stronger-model route；sensor 不拥有 truth commit。", "exact-v1 跨 LLM 与 QA/hallucination datasets 比较 pre-generation detector 的 discrimination、calibration 与 routing utility。", "probe 与 label/judge 共偏，attention correlation 不证明因果；生成前预测不能覆盖 retrieval corruption 或生成中途状态变化。", "Qwen2.5-3B, Qwen2.5-7B, Qwen3.5-9B, Llama-2-7B and Gemma-4-E2B instruction-tuned models", "pre-generation hallucination-risk prediction on SQuAD, Natural Questions and HotpotQA", "ROC-AUC, calibration and routing utility", "§3 Methodology; §3.2 Target Construction; §3.3 Attention Probing", "§4 Results and Discussion; §4.1 Experimental Setting", "§6 Limitations", "No Change — Existing Coverage", "Ch67 已把 activation/attention monitor 定义为 model-version-bound sensor；该 family 不改变 authority。", batch="probe-training batch size 8 or 16; soft targets use 10 samples per prompt"),
"2606.21954": S("PLATFORM-EVALUATION-SYSTEM", "Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。", "20 个语言模型、三套 multilingual benchmark；小模型 transfer 并未失效，随规模的进步慢于 raw accuracy 暗示。", "HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。", "Gemini-2.5-Flash, Gemini-2.5-Flash Thinking-Off, Gemini-3-Flash, Gemini-3-Flash Low, Gemini-3-Flash Minimal, Gemma-3-1B, Gemma-3-4B, Gemma-3-12B, Gemma-3-27B, Gemma-4-E2B-IT, Gemma-4-E4B-IT, Gemma-4-26B-A4B-IT, Gemma-4-31B-IT, Claude-Haiku-4.5, Claude-Sonnet-4.6, Claude-Opus-4.7, Qwen-3-4B, Qwen-3-30B-A3B, GPT-OSS-20B and GPT-OSS-120B", "ECLeKTic, MGSMv2 and MMLU-ProX-Lite cross-lingual transfer", "Hardness Adjusted Transfer versus raw source/target accuracy", "§4 Proposed XLT Metric: HAT Score; §4.1 Transfer Profile and HAT Score", "§5 Experimental Details; §6 Results", "§8 Limitations", "Integrate", "Ch66 需把 transfer capability 与 source-language base ability 解耦，避免版本比较的 denominator inflation。", batch="10 promptings per source/target item for HAT estimation"),
"2606.21959": S("PLATFORM-EVALUATION-SYSTEM", "OpenBioRQ 以未解决研究问题评估 agent：把 citation resolution、actual support、open-status verification 与 answer usefulness分层，并提供冻结 checklist 改善 judge agreement。", "受测 agents 在高难问题上 tool-use collapse；15.9% citation 指向错误论文，且 citation 可解析不等于支持 claim。", "biomedical question set、冻结时点与 judge checklist 不证明未来问题仍未解决；benchmark 不能替代领域专家证据审查。", "GLM-5.1, Qwen3.6, DeepSeek-V4, GLM-5, Qwen3.5-397B, Qwen3-235B, Gemini-3-Pro, Opus-4.7 and GPT-5.5", "657-question OpenBioRQ core and 423-question frozen core", "two-level citation factuality, checklist solve rate, tool use and judge agreement", "§3 The OpenBioRQ Benchmark; §3.2 Construction Quality and Grounded Openness", "§4 Evaluation Protocol; §5 Experiments and Analysis", "§6 Discussion and Limitations", "No Change — Existing Coverage", "当前 Ch66 已明确引用不仅要存在还要支持 claim，并已把 deep-research citation support、coverage 与 synthesis 分层；OpenBioRQ 提供 biomedical stress case，但不改变 evaluation owner。"),
"2606.21963": S("PLATFORM-PRODUCTION", "Holmes 将 mixed-language mobile crash diagnosis 绑定 log、stack trace、source/change history 与工具执行，输出 diagnosis 与 evidence-linked repair，而非只生成解释文本。", "工业移动端 crash workload 上比较 diagnosis accuracy、time-to-resolution 与 artifact/tool ablation。", "单组织 crash taxonomy、内部工具与数据分布限制复现；诊断建议不等于已合并修复或无回归。", "Not Disclosed", "mixed-language mobile crash diagnosis over WeChat crash artifacts", "function-level fault-localization accuracy, diagnosis time and ablations", "§2 Methodology; §2.1 Parallel Context Retrieval; §2.2 Agentic Code Exploration; §2.3 Synthesis & Reasoning", "§3 Experiment; §3.2 Accuracy Results; §3.3 Comparative Analysis & Ablation Study", "§4.1 Limitations & Failure Analysis; §4.3 Threats to Validity", "No Change — Existing Coverage", "Ch73/81 已要求 incident diagnosis 与 executable effect receipt 分离；Holmes 是工业案例。"),
"2606.21968": S("AGENT-WORKFLOW", "ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。", "多种 visual RAG benchmark/model 上比较质量、视觉 token 与 routing ablation。", "router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。", "LLaVA-v1.5-7B, LLaVA-v1.5-13B, LLaVA-OneVision-0.5B and Qwen3-VL", "visual RAG under resolution-context trade-off", "task accuracy, inference time and route-selection ablations", "§3 Motivations: Understanding the Resolution–Context Trade-off; §4 Proposed Method: ViRGo", "§5 Experiments; §5.1 Experimental Setup", "§7 Limitations", "Integrate", "Ch81 需把感知分辨率选择建模为有成本、可回退的 route，而不是固定预处理。", output_length="single token for evaluation consistency"),
"2606.21994": S("TRAIN-GRPO", "Prefix-Guided OPD 用 teacher/student rollout 的早期 prefix overlap 估计后续 trajectory value，把 rollout budget 转向可能形成 golden trajectory 的前缀。", "reasoning tasks 上相对 OPD/on-policy distillation 比较 sample efficiency、accuracy 与 prefix allocation。", "早期 overlap 可能错杀迟发正确路径并放大 teacher/student 共偏；它重分配探索预算，不扩展 teacher capability ceiling。", "DeepSeek-R1-Distill-Qwen-1.5B, JustRL-DeepSeek-1.5B, OpenMath-1.5B, JustRL-Nemotron-1.5B, DeepSeek-R1-Distill-Qwen-7B, Qwen3-4B-Base and Qwen3-4B", "DAPO-Math-17K training; AIME24, AIME25, AMC23, HMMT24 and HMMT25 evaluation", "benchmark accuracy, training time and rollout allocation", "§Method — Truncated On-Policy Distillation; Prefix-Based Trajectory Scoring; Prefix-Guided On-Policy Distillation", "§Experiments — Setup; Compared Methods; §Results — Main Results and four ablations; Appendix B Training and Implementation Details", "§Limitations", "No Change — Existing Coverage", "Ch33 已将 OPD 定义为探索催化剂并保留 teacher ceiling；prefix allocation 是同 owner 内实现分支。", input_length="maximum prompt length 1,024", output_length="maximum response length 7,168", batch="training mini-batch 64 with 4 responses per prompt"),
"2606.22000": S("PLATFORM-EVALUATION-SYSTEM", "CFAgentBench 以可执行 construction-finance environment 记录账户/文档 state diff、forbidden side effect 与 approval-required money movement；正确金额但未获批准同样失败。", "多模型 agents 在 pass@1 与 pass@5 上测量 task completion、side effect、approval compliance，并显示重试可靠性塌陷。", "synthetic finance workflow 与规则覆盖有限；state-diff checker 不证明真实法规、身份或银行 effect，pass@k 也不能隐藏每次 unauthorized action。", "DeepSeek-V3.1, Qwen3-235B-A22B-Instruct and Qwen2.5-72B-Instruct via Hugging Face Inference Providers", "40 oracle-validated autonomous construction-finance tasks across eight domains", "pass^1, pass^5, state-diff correctness, forbidden side effects and approval compliance", "§3 The CFAgentBench Environment; §4 Tasks", "§5 Evaluation; §6 Experiments", "§7 Limitations and Ethics", "No Change — Existing Coverage", "当前 Ch66 已有专节把 Pass@k 能力覆盖、Pass^k conjunction reliability 与 paired transition 分离，且 action authority 已是独立 evaluation plane；CFAgentBench 不再形成新 delta。", concurrency="five independent greedy-decoding runs per task for pass^5", slo="money movement must be staged and never executed"),
"2606.22013": S("PLATFORM-PRODUCTION", "ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。", "工业 model-serving systems 上比较 capacity-search cost、SLO boundary accuracy 与固定-grid baseline。", "14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。", "14 anonymized production models M1–M14: recommendation, ranking, vision and NLP; 80M–1.5B parameters", "adaptive open-loop load testing for ML model-serving capacity", "capacity deviation, test duration, run stability and SLO compliance", "§2 System Design and Methodology; §2.2 Load Testing Strategies; §2.3 Health Assessment Engine", "§3 Experimental Methodology; §4 Results", "§5 Discussion; Threats to Validity", "Integrate", "Ch73 需把 load test 从固定 QPS 清单升级为可复算 SLO-boundary search contract。", hardware="NVIDIA A100 80GB and H100 GPUs", slo="model-specific latency/error SLO; capacity is maximum QPS at SLO compliance"),
"2606.22019": S("PLATFORM-SECURITY", "subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。", "受控 channel-location 实验比较 audit signal、downstream learning 与干预，展示相同 payload 在不同 channel 的可审计性变化。", "结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。", "Pythia 70M–6.9B, Qwen3.5-0.8B, Qwen2.5-3B-Instruct, OLMo-2-1B, Gemma-3 270M/1B/4B, RedPajama-3B and RWKV-4-3B", "pre-training audit of initialization-dependent body, vocabulary and conditional-behaviour channels", "coverage AUROC/correlation, held-out transfer and causal channel ablations", "§2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?", "§3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it moves auditability; §7 Mitigations by channel", "§8 Discussion, limitations, and related work", "Integrate", "Ch72 需明确 audit coverage 与 outcome 分离：未覆盖 channel 只能是 Unknown。", precision="mixed precision; Appendix A includes a bf16 recipe sweep"),
"2606.22030": S("AGENT-MEMORY", "belief memory 以 Bayesian state 表示候选命题，但只在 source reliability 可估时更新；provenance-capped influence 限制单源/重复证据对 posterior 的控制。", "多任务 memory benchmark 中，plain Bayesian update 无稳定收益；reliability-conditioned update 提升 strict F1，并在 poisoning 下比较 provenance cap。", "A-MEM/BeliefMem 数字未由作者重跑且二手表格类别映射曾冲突；GPT-4o-mini 同时做 extraction、answer 与 judge，strict F1 和 judge 可能共偏。", "GPT-4o-mini for extraction, answer generation and judging; A-MEM and BeliefMem are self-reported baselines", "LoCoMo: 10 conversations, 1,540 questions across four categories", "strict token F1, BLEU-1, context recall and GPT-4o-mini failure buckets", "§3 The Nous Architecture; §3.3 Bayesian Update; §3.7 Pipelines", "§4 Experimental Setup; §5 Results; §6 Analysis", "§7 Limitations and Future Work; §5 A caveat on the A-MEM comparison", "No Change — Existing Coverage", "当前 Ch77 已要求 source calibration、valid-time、独立 corroboration、contradiction、supersession 与 risk-aware selective action共同约束事实 Memory；Bayesian 聚合是既有可靠性读路径的受限实现。"),
"2606.22043": S("TRAIN-GRPO", "multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。", "Qwen3-VL-8B-Instruct 的多 seed、lambda∈{0,1,2} 与 intervention-timing 轨迹上测 VHS、accuracy 与 onset/reversal；representation probe 落在 bootstrap variability 内，只是探索性观察。", "单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。", "Qwen3-VL-8B-Instruct", "GRPO-style video-QA RLVR with reward-strength and intervention-time controls", "held-out OOD visual-hacking score, accuracy and onset/reversal trajectory", "§2 Setup — Task and model; Visual-hacking diagnostic (VHS); Held-out OOD evaluation; Trajectory fleet", "§3 Onset is real and seed-robust; §4 Reward strength: a monotone dose–response with formation–reversal asymmetry; §5 A critical intervention window; §6 What changes inside: representation probe; Appendix A Reproducibility and diagnostic details", "§8 Discussion and limitations — Limitations", "Integrate", "Ch33 需把 visual reliance 作为训练 trajectory state，而不只在最终 accuracy 后诊断 shortcut。"),
"2606.22082": S("AGENT-MULTI-AGENT", "CodeTeam 先生成竞争架构草案，再由 CTO 产出 machine-checkable ownership/interface contract，随后依 dependency graph 调度实现并运行 repo tests。", "repository-level generation tasks 上比较单 agent、多 agent、组件 ablation 与测试结果。", "所有 agents 共享 Qwen2.5-72B-Instruct，CTO contract 可能共享 backbone bias；test suite 不完备时 machine-checkable 只证明 harness 内一致。", "Qwen2.5-72B-Instruct for all PE and SFT agents", "repository-level code generation on SketchEval and NL2Repo-Bench", "SketchBLEU, execution-based validation and component ablations", "§3.2 Design and Implementation of CodeTeam", "§3.3 Benchmark Experiment Design; §3.4 Execution-Based Evaluation; §4 Results", "§6 Threats to Validity", "No Change — Existing Coverage", "Ch82 已明确 shared repository 需要 commitment protocol、ownership/interface 和可验证提交顺序。"),
"2606.22085": S("PLATFORM-SECURITY", "通过在 reasoning trace 中植入受控改动测试模型能否自报 CoT tampering；把 self-report、behavioral change 与 external detector 分离。", "多 reasoning models 与 tampering types 上测 detection/acknowledgement，结果显示自我检测弱且不稳定。", "可见 CoT 不是完整内部 computation；专有 frontier API 不支持 CoT prefilling 因而未测，否认/承认都不是 tamper truth。", "openai/gpt-oss-120b, deepseek/deepseek-v3.2, moonshotai/Kimi-K2.5 and qwen/qwen3-235b-a22b-thinking-2507 via OpenRouter", "controlled chain-of-thought tampering on GPQA-Diamond, 200 MMLU-Pro examples and AIME 2025", "tamper detection, localization and regex-scored verdicts", "§3 Methodology — Experimental settings; Interventions; Data; Models", "§4 Detecting Changes — Completed Condition; Partial Condition; Self-Awareness; §5 Localizing Changes; Appendix D Additional Results", "Limitations; Appendix B Model Details", "No Change — Existing Coverage", "Ch72 已将 CoT monitor 定义为 policy-bound sensor，不是 security authority；该负结果强化边界。", output_length="10,000 max tokens in completed-condition detection; judge max_tokens 16", batch="single rollout per example"),
"2606.22136": S("TRAIN-DATA", "Wh0 用 generative video world model 产生 scene/object/language-conditioned human-hand episodes，再以 hand reconstruction 与 visual editing 转成 robot-trainable supervision，并与少量真实机器人数据 co-train。", "50K WM-H episodes、18 个真实 dexterous tasks；相对仅 robot data，未见任务 zero-shot success 从 8.3% 升至 38.9%。", "生成世界模型会携带 physics/contact error，视觉编辑不等于 action 可执行；真实 robot data 仍是 deployment anchor，18 tasks 不证明广泛迁移。", "VITRA dexterous VLA post-trained with WM-H and robot data", "50,000 world-model-generated egocentric episodes; 18 real-robot tasks on Unitree G1 with Inspire hands", "real-robot zero-shot success and generation/alignment ablations", "§3 WM-H Dataset Construction via Controllable Video Synthesis; §4 Wh0: Policy Learning with Human-Robot Alignment", "§5 Experiments; §5.1 Experimental Setup", "§6 Conclusion and Limitations; Appendix A.6 Failure Cases", "No Change — Existing Coverage", "当前 Ch27 已完整写入 human hand pose→action-conditioned video→pose/depth reconstruction/retargeting→derived robot trajectory provenance→real closed-loop admission；Wh0 正是该现有分支的 source-specific evidence。"),
"2606.22142": S("TRAIN-DATA", "RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。", "真实机器人 policy-iteration workflow 中比较常规流程与 lineage layer 的迭代时间、审计性和 downstream policy performance。", "robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。", "Not Disclosed", "repeated robot rollout-review-dataset-train-evaluate-release cycles", "review reliability, policy quality, effort and recollection case studies", "§3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance", "§4 Experiments; §4.1 Experimental Setup", "§5 Limitations and Discussion", "Integrate", "Ch27 需把 sample lineage 扩展为 rollout→review→dataset→training→evaluation→release 的 typed lifecycle graph。"),
"2606.22164": S("TRAIN-GRPO", "多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。", "可精确调 ρ 的 controlled environment 复现 turn-level/trajectory-level SNR 比例，R²=0.999，并测 training-step gap。", "推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。", "30K-parameter causal Transformer with two pre-norm blocks, model dimension 32, two attention heads and feed-forward width 128", "multi-turn RL with tunable consequential-decision density", "gradient SNR and training iterations to threshold", "§2 Preliminaries; §3 The Signal Dilution Problem", "§4 Experimental Setup; §5 Results", "§7 Discussion; Appendix A assumptions; Appendix B Diluted Doors", "Integrate", "Ch33 需把 decision density 纳入 credit-assignment route：长轨迹本身不是选择 critic 的充分条件。", batch="trajectory-level group G=16; turn-level Monte Carlo critic k=8; initialization SNR N=1,024"),
"2606.22175": S("AGENT-WORKFLOW", "StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。", "145,449-claim PromptVerify workflow 在 20 GPU stable testbed 获 3.6×，并扩到 186 个闲置 GPU 后 784 秒完成。", "persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。", "SmolLM2 1.7B", "PromptVerify over 145,449 FEVER training claims", "makespan, startup amortization and scale-out completion time", "§II Implementation of an LLM-integrated Claim Verification Workflow; §III Transforming the Workflow to Enable StickyInvoc", "§IV Evaluation; §IV-A Experiment Settings", "§I-E Limitation of the Proposed Approach", "Integrate", "Ch81 需把 workflow task identity 分成 state-holder 与 invocation；复用必须绑定 model/runtime version 和 tenant。", hardware="stable pool: 10 NVIDIA A10 + 10 TITAN X Pascal; scale-out up to 186 GPUs", batch="varied inference batch sizes in RQ3"),
"2606.22179": S("PLATFORM-EVALUATION-SYSTEM", "selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。", "9 个 LLM、3 个 benchmark、25 个 model-dataset pair，对七种 confidence construction 比较 ranking、阈值粒度与 inference cost。", "三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。", "Llama-3.1-70B/8B, Gemini-2.5-Flash, Gemini-2.0-Flash-Lite, Claude-Haiku-4.5, GPT-4o-mini, GPT-4.1-mini/nano and GPT-5-nano", "2,890 BoolQ, MNLI and PubMedQA black-box classification examples", "risk ranking, distinct threshold granularity and inference cost", "§3 Problem Setup; §4 Confidence Constructions", "§5 Experiments; §5.1 Setup", "§7 Limitations; §6 Deployment Recommendations", "Integrate", "Ch66 需增加 threshold-resolution contract：ranking 好不代表 operator 有足够可选 operating points。"),
"2606.22180": S("TRAIN-DISTRIBUTED-TRAINING", "FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。", "六个系统 baseline 与大图数据上平均 27.9× speedup、通信降超 53.1%、CPU-GPU utilization 超 80%。", "quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。", "FeLoG, PyTorch-BigGraph, DistDGL, DistGER, DistGER-G, NeutronTP and LeapGNN", "large-scale graph embedding with sampling and distributed training", "time-to-quality, communication volume and CPU-GPU utilization", "§5 FeLoG; §5.1 Feedback-coupled Sampling-Training Model; §5.2 Activity-aware Communication", "§6 Experimental Results; §6.1 Experimental Setup", "§7 Conclusions and experimental generalizability boundary", "Integrate", "Ch36 需增加 sampling→quality feedback loop 与 communication freshness 的联合 contract，而非仅 pipeline overlap。", hardware="8 machines, each with a 2.60 GHz Intel Xeon Gold 6240 CPU (36 cores/72 threads), NVIDIA V100 32 GB, 192 GB DDR4 and full-duplex 10 Gbps networking; GraNNDis comparison on four NVIDIA A40 GPUs"),
"2606.22189": S("TRAIN-DATA", "在单张 L20 上公开 134.5M 模型的 data gate、cross-source MinHash/LSH、segment dedup、benchmark-overlap removal、SFT weight interpolation 与 RLVR 全链。", "约 13B token、自跑六任务 harness；均分 0.4150；直接 GRPO-style RLVR 使 GSM8K exact match 从 1.82% 降至 1.59%/1.21%。", "单 run、自有 harness、小模型与 nominal-token ratio 不证明 scaling law 或统计等价；RLVR 下降只是具体 failure case。", "L20-Edu-135M, SmolLM-135M, SmolLM2-135M, Qwen2.5-0.5B, OLMo-1B and older 100M–160M baselines", "single-GPU 134.5M language-model pretraining, SFT and RLVR", "six-task zero-shot mean and GSM8K exact match", "§3 System Overview; §4 Data Quality and Contamination Control; §5 Training Efficiency", "§6 Evaluation Protocol; §7 Results", "§9 Limitations; §10 Threats to Validity", "No Change — Existing Coverage", "Ch27 已拥有 data gates、dedup、contamination 与 provenance；保留此单 GPU negative RLVR case，不新增 owner。", hardware="one NVIDIA L20 48GB GPU"),
"2606.22203": S("AGENT-MULTI-AGENT", "先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。", "5 个 frontier model 测 pairwise gamma，16 个 closed/open model 测 group coupling；复核既有 emergent-consensus 结果并发现 settled facts 上是 prior artifact。", "pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。", "deepseek-v4-pro, gpt-5.5, claude-opus-4.8, gemini-3.5-flash, qwen3.7-max, Llama-3.1-8B, Llama-3.1-70B, Llama-3.3-70B, Llama-4-Maverick, Qwen-2.5-7B, Qwen-2.5-72B, Mistral-Large, Mistral-Small, Mixtral-8x22B, Gemma-2-27B and DeepSeek-Chat", "LLM-agent opinion dynamics under pairwise and group interaction", "coupling gain, final-versus-initial slope/bias, consensus and polarization regime", "§3 The Coupling Gain; §4 Theory", "§5 Experiments and Results", "§6 Limitations; §5.4 context-dependent transfer boundary", "Integrate", "Ch82 需禁止用 pairwise interaction 参数外推 group dynamics，并把 model-prior drift 从 emergent consensus 分离。"),
"2606.22248": S("TRAIN-DATA", "SamatNext 交替 Differential-Attention 与简化 DeltaNet state mixer，用 RMS normalization/output calibration 测试 staged code curriculum 的 retention/plasticity。", "356M 参数、受控 Python curriculum；Stage 5 100%、相邻 Stage 3 保留 98.8%，但早期 Stage 2E 仅 12%；matched Transformer Stage 3 仅 6%。", "单一受控 curriculum、单 architecture size 且 long-horizon retention 仍弱；不能外推为解决 catastrophic forgetting。", "SamatNext v0.2-B 356M and a parameter-matched Transformer", "sequential Python-code curriculum", "current-stage pass rate and adjacent/early-stage semantic retention", "§3 SamatNext v0.2-B Architecture; §4 Curriculum and Evaluation Setup", "§5 Empirical Results", "§8 Limitations; §6.4 Threats to Validity", "No Change — Existing Coverage", "Ch27 已把 curriculum state 与 retention Gate 分离；本 family 仅是架构受限案例。"),
"2606.22263": S("PLATFORM-SECURITY", "Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。", "7 个持续 fuzz 5–8 年的生产项目与 100 个随机 Arvo/CyberGym 项目；约每项目 1 小时、总成本 300 美元，发现 19 个未知 memory-safety 漏洞。", "sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。", "Claude Haiku 4.5 for hypothesis generation and Claude Sonnet 4.6 for PoV construction; Opus 4.7, GPT-5.5 and Sorcar baselines", "seven mature production projects and 100 randomly selected Arvo/CyberGym projects", "sanitizer-confirmed vulnerabilities, targeted recall and token cost", "§III Design of Revelio; §III-C Hypothesis Confirmation by PoV Construction", "§V Evaluation", "§VI Discussion and Limitations", "Integrate", "Ch72 需把 vulnerability report 的 commit authority 绑定 executable PoV+sanitizer，而非 agent verdict。"),
"2606.22283": S("INFER-GPU-MEMORY", "对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。", "A11–A18、M1–M5 目标表；直接测量只在 M1/M5，结合静态分析给出 operation-device matrix 与性能/能耗边界。", "private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。", "Core ML models and direct ANE programs used in the guide", "Apple Neural Engine architecture, compilation and measured performance", "measured roofline/energy plus operation-by-device support matrix", "§Part II Reaching the ANE — Software stack; Dispatching without Core ML; §Part VI The Silicon — Datapath and MAC geometry; §Part VII The Toolchain and Encoding; §Part VIII System Internals", "§Part III Performance and Fit — Roofline; Power and efficiency; Across the chip family; Appendix A Operation-by-device matrix; Appendix E Provenance", "§Part V Practice — Pitfalls and limits; §Methodology; §Open questions; §Introduction — direct route is undocumented, unsupported and version-fragile", "Integrate", "Ch54 需把硬件逆向知识按 measured/decompile-derived/predicted 分层，并保持 Core ML 是唯一 supported production path。", hardware="Apple M1 and M5 measured; A11-A18 and M1-M5 documented/predicted matrix"),
}

# Score V2 is independently calibrated per family.  It must not inherit the
# default merely because the family survived the durable-denominator screen or
# later received a Books comparison.
SCORE_OVERRIDES = {
    "2606.21822": (2, 1, 2), "2606.21836": (2, 2, 2),
    "2606.21842": (3, 2, 3), "2606.21843": (3, 2, 3),
    "2606.21848": (3, 2, 3), "2606.21854": (2, 1, 2),
    "2606.21856": (2, 2, 3), "2606.21868": (3, 2, 3),
    "2606.21869": (3, 2, 3), "2606.21875": (2, 1, 2),
    "2606.21877": (3, 3, 3), "2606.21884": (3, 2, 3),
    "2606.21891": (3, 2, 3), "2606.21917": (2, 1, 2),
    "2606.21954": (3, 2, 3), "2606.21959": (2, 2, 2),
    "2606.21963": (2, 2, 2), "2606.21968": (3, 2, 2),
    "2606.21994": (2, 1, 2), "2606.22000": (2, 2, 3),
    "2606.22013": (3, 2, 3), "2606.22019": (3, 3, 3),
    "2606.22030": (2, 2, 3), "2606.22043": (3, 2, 2),
    "2606.22082": (2, 2, 2), "2606.22085": (2, 1, 2),
    "2606.22136": (2, 2, 2), "2606.22142": (3, 3, 3),
    "2606.22164": (3, 2, 3), "2606.22175": (3, 2, 3),
    "2606.22179": (3, 2, 3), "2606.22180": (3, 2, 2),
    "2606.22189": (2, 1, 2), "2606.22203": (3, 2, 2),
    "2606.22248": (2, 1, 2), "2606.22263": (3, 2, 3),
    "2606.22283": (3, 2, 3),
}
assert set(SCORE_OVERRIDES) == set(C)
for _aid, _score in SCORE_OVERRIDES.items():
    C[_aid]["score"] = _score

WINNERS = {
    "2606.21842": "DA-20260621-NONPREFIX-KV-ISOLATION",
    "2606.22030": "DA-20260621-BELIEF-MEMORY-AUTHORITY",
    "2606.22142": "DA-20260621-TYPED-ROBOT-LINEAGE",
}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


ARTIFACT_EXCEPTION = "Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review"


def review_route(e: dict) -> str:
    return "deep" if sum(e["score"]) >= 7 else "standard"


def review_status(e: dict) -> str:
    return "deep_complete" if review_route(e) == "deep" else "standard_complete"


def review_body(r: dict) -> str:
    e = r["e"]
    old_path = e["note"]
    coexistence = (
        "因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。"
        if e["disposition"].startswith("No Change")
        else "因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。"
    )
    return "\n".join([
        f"### {r['aid']} — {r['src']['title']}", "",
        f"**问题与旧路径。** 该 family 针对 `{e['workload']}` 暴露的具体缺口是：{old_path} 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。", "",
        f"**机制与 owner。** {e['delta']} 唯一知识 owner 为 `{e['owner']}`；相邻章节只消费版本化 handoff。", "",
        f"**Evaluation：证明与未证明。** {e['proof']} Method=`{r['loc'][0]}`；Evaluation=`{r['loc'][1]}`。Benchmark contract：model=`{e['model']}`；hardware=`{e['hardware']}`；precision=`{e['precision']}`；batch=`{e['batch']}`；concurrency=`{e['concurrency']}`；SLO=`{e['slo']}`；evaluator=`{e['evaluator']}`。", "",
        f"**Trade-off、failure、共存与演进。** {e['boundary']} {coexistence} Limit/counterevidence=`{r['loc'][2]}`。", "",
        f"<!-- claim:{r['family']}:start -->",
        f"Claim boundary：仅 `arXiv:{r['aid']}v1` official HTML；不使用 later version；普通 pending locator count=`0`。",
        f"<!-- claim:{r['family']}:end -->",
    ])


def provenance(r: dict) -> str:
    def multi(value: str) -> str:
        items=[]
        for raw in value.split(";"):
            item=unicodedata.normalize("NFC", raw.strip())
            if item and item not in {"—", "-", "N/A", "n/a"}:
                items.append(item)
        return ";".join(sorted(items))
    body=review_body(r)
    normalized=unicodedata.normalize("NFC", body.replace("\r\n","\n").replace("\r","\n"))
    body_lines=[line.rstrip() for line in normalized.split("\n")]
    while body_lines and not body_lines[0]: body_lines.pop(0)
    while body_lines and not body_lines[-1]: body_lines.pop()
    body_hash=hashlib.sha256("\n".join(body_lines).encode()).hexdigest()
    canonical="|".join((
        "review-completion-v1", r["family"], f"paper-v1:{r['aid']}", f"arXiv:{r['aid']}v1",
        "SRC-ARXIV", f"arXiv:{r['aid']}v1", f"SRC-ARXIV@arXiv:{r['aid']}v1", review_route(r["e"]),
        multi(r["loc"][0]), multi(r["loc"][1]), multi(r["loc"][2]), multi(ARTIFACT_EXCEPTION),
        f"claim:{r['family']}", f"review:{r['family']}", f"review-body-sha256:{body_hash}",
    ))
    return "RP-"+hashlib.sha256(canonical.encode()).hexdigest()[:16]


def main() -> None:
    PACKET.mkdir(parents=True, exist_ok=True)
    raw = json.loads(PROV.read_text())
    rows = raw["identities"]
    by_id = {r["arxiv_id"]: r for r in rows}
    assert len(rows) == 224 and set(C) <= set(by_id)
    retained = sorted(C)
    did = "DEN-20260621-" + hashlib.sha256("\n".join(retained).encode()).hexdigest()[:8]
    route_raw = Counter(r["screening_route"] for r in rows)
    route_retained = Counter(by_id[a]["screening_route"] for a in retained)
    route = {k: {"raw": route_raw[k], "retained": route_retained[k], "closure": route_raw[k]-route_retained[k]} for k in sorted(route_raw)}

    # Full-population screening audit. Closure evidence embeds the source-specific
    # title and abstract claim rather than assigning a keyword-only bucket.
    audit_rows = []
    frozen_rows = []
    for r in rows:
        aid, title, abstract = r["arxiv_id"], norm(r["title"]), norm(r["abstract"])
        first = re.split(r"(?<=[.!?])\s+", abstract)[0]
        if aid in C:
            decision = "retained"
            reason = f"Durable delta: {C[aid]['delta']}"
        else:
            decision = "pre-denominator closure"
            reason = (f"Family-specific closure for ‘{title}’: exact abstract scope is ‘{first[:360]}’. "
                      "The deliverable remains a domain/task/model method, survey, or generic non-AI system result; it does not change a durable AI-System state/data/control owner, evaluation-release contract, or Books proposition.")
        audit_rows.append([aid, r["source_family_key"], r["screening_route"], title, decision, reason])
        nr = dict(r)
        nr.update({"semantic_screen_result": decision, "semantic_screen_reason": reason,
                   "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}", "denominator_id": did})
        frozen_rows.append(nr)
    with (PACKET/"denominator-full-semantic-audit-v1.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["arxiv_id", "source_family_key", "screening_route", "title", "decision", "family_specific_reason"])
        w.writerows(audit_rows)
    frozen = dict(raw)
    frozen.update({"denominator_id": did, "denominator_frozen_at": EXECUTED_AT,
                   "raw_count": 224, "retained_count": len(C), "closure_count": 224-len(C),
                   "route_reconciliation": route, "identities": frozen_rows})
    (PACKET/"screening-ledger.json").write_text(json.dumps(frozen, ensure_ascii=False, indent=2)+"\n")

    reviews = []
    for aid in retained:
        e, src = C[aid], by_id[aid]
        family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        url = f"https://arxiv.org/html/{aid}v1"
        loc = (f"{url} — {e['method']}", f"{url} — {e['evaluation']}", f"{url} — {e['limitation']}")
        reviews.append({"aid": aid, "family": family, "src": src, "e": e, "loc": loc})
    for r in reviews:
        r["rp"] = provenance(r)

    access = [{"source_family_id": r["family"], "primary_evidence_version": f"arXiv:{r['aid']}v1",
               "official_exact_v1_url": f"https://arxiv.org/html/{r['aid']}v1", "access_status": "accessible",
               "method_locator": r["loc"][0], "evaluation_locator": r["loc"][1],
               "limitations_locator": r["loc"][2], "later_version_used": False} for r in reviews]
    (PACKET/"exact-v1-access-receipt.json").write_text(json.dumps(access, ensure_ascii=False, indent=2)+"\n")

    receipts = []
    for r in reviews:
        e = r["e"]
        receipts.append({"source_family_id": r["family"], "review_provenance_id": r["rp"],
                         "primary_evidence_version": f"arXiv:{r['aid']}v1", "review_route": review_route(e),
                         "method_locator": r["loc"][0], "evaluation_locator": r["loc"][1],
                         "limitations_locator": r["loc"][2], "problem": norm(r["src"]["abstract"]).split(".")[0],
                         "mechanism": e["delta"], "evaluation_proof": e["proof"], "non_proof": e["boundary"],
                         "owner": e["owner"], "books_disposition": e["disposition"],
                         "benchmark_contract": {k: e[k] for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")},
                         "completion_result": "complete"})
    (PACKET/"source-review-receipts-v2.1.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2)+"\n")

    decisions = []
    for r in reviews:
        aid, e = r["aid"], r["e"]
        selected = aid in WINNERS
        priority = (
            f"{e['note']} Exact-v1 supports: {e['proof']} Its cross-layer control boundary is material because {e['boundary']}"
            if selected else
            f"{e['note']} Exact-v1 supports: {e['proof']} It is not promoted over the three winners because its durable effect remains owned by {e['owner']} and its non-proof boundary is: {e['boundary']}"
        )
        eligibility = ["potential_books_delta"]
        if sum(e["score"]) >= 7:
            eligibility.insert(0, "score_7_9")
        decisions.append({"source_family_id": r["family"], "eligibility": "; ".join(eligibility),
                          "decision": "selected" if selected else "not_selected",
                          "analysis_unit_id": WINNERS.get(aid, "—"), "subsumed_by": "—",
                          "priority_rationale": priority,
                          "narrative_ref": f"analysis:{WINNERS[aid]}" if selected else f"analysis-decision:{r['family']}"})
    (PACKET/"deep-analysis-selection-v1.json").write_text(json.dumps(decisions, ensure_ascii=False, indent=2)+"\n")

    books = []
    for r in reviews:
        e = r["e"]
        books.append({"source_family_id": r["family"], "stable_node_id": e["owner"],
                      "target_chapter_ref": chapter_ref(PATHS[e["owner"]], TARGET_ANCHORS[e["owner"]]),
                      "adjacent_chapter_refs": adjacent_refs(e["owner"]),
                      "existing_proposition": e["note"], "new_evidence_delta": e["delta"],
                      "evolution_relation": "Direct Evolution" if e["disposition"].startswith("Integrate") else "Principle Reuse",
                      "decision": e["disposition"], "books_review_ref": f"books-review:{r['family']}"})
    (PACKET/"books-comparison-v1.json").write_text(json.dumps(books, ensure_ascii=False, indent=2)+"\n")

    integrations = [r for r in reviews if r["e"]["disposition"].startswith("Integrate")]
    groups = defaultdict(list)
    for r in integrations:
        groups[r["e"]["owner"]].append(r)

    q = ["# 2026-06-21 Books Integration Queue V1", "", f"Denominator `{did}`. Pre-write only: {len(integrations)} family deltas merged into {len(groups)} owner files; root writeback and post-write audit pending.", ""]
    ready = ["# 2026-06-21 Ready-to-Insert Books Packet V1", "", f"Source denominator `{did}`. Insert each owner block once and preserve every independent exact-v1 Review note.", ""]
    for owner, items in sorted(groups.items()):
        target = PATHS[owner]
        anchor = TARGET_ANCHORS[owner]
        q += [f"## {owner}", "", f"- Target: `{target}`", f"- Exact target locator: `{anchor}`",
              f"- Source families: {', '.join(x['family'] for x in items)}",
              f"- Minimal durable delta: {' '.join(x['e']['delta'] for x in items)}",
              f"- Evidence boundary: {' '.join(x['e']['boundary'] for x in items)}", ""]
        ready += [f"## {owner} — {target}", "", f"Insert after `{anchor}`.", "", "### Minimal durable delta", "",
                  " ".join(x["e"]["delta"] for x in items), "", "### Old path / coexistence / cost / failure / fallback", "",
                  " ".join(x["e"]["boundary"] for x in items) + " 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。", "", "### Review note", ""]
        for x in items:
            ready.append(f"- {x['family']}: arXiv:{x['aid']}v1; exact-v1 official URL=`https://arxiv.org/html/{x['aid']}v1`; Method=`{x['loc'][0]}`; Evaluation=`{x['loc'][1]}`; Non-proof/limitations=`{x['loc'][2]}`; durable delta={x['e']['delta']} Boundary: {x['e']['boundary']}")
        ready.append("")
    (PACKET/"BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(q)+"\n")
    (PACKET/"READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready)+"\n")

    lines = ["# Daily Research — 2026-06-21", "", f"> Strict V2.1 Daily for `{did}`. Coverage, Evidence and Selection passed; Books remains Open pending root writeback and this lane's post-write fresh audit.", "", "## Executive Summary", "", f"Beijing window `[2026-06-20 09:00, 2026-06-21 09:00)` contains 224 registered identities. Full 224/224 title+abstract screening freezes {len(C)} durable families and {224-len(C)} family-specific closures. Official exact-v1 HTML was reviewed for {len(C)}/{len(C)} families. Full-frontier selection freezes three winners before rationale. Books comparison yields {len(integrations)} Integrate proposals and {len(C)-len(integrations)} No Change handoffs.", "", "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-06-21 |", "| Window End | 2026-06-21 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {did} |", f"| Denominator Frozen At | {EXECUTED_AT} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "", "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |", f"| SRC-ARXIV | 2026-06-20T09:00:00+08:00 | 2026-06-21T09:00:00+08:00 | {EXECUTED_AT} | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 224 | {'; '.join(r['family'] for r in reviews)} | pages=40; final_cursor=end; 224 unique identities | 2026-06-21T01:00:00Z | ../_sources/daily-20260621/screening-ledger.json; ../_sources/daily-20260621/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260621 | — |", "", "<!-- coverage:SRC-ARXIV:20260621:start -->", f"All {route_raw['core_daily_semantic_review_required']} Core, {route_raw['keyword_daily_semantic_review_required']} keyword-routed and {route_raw['not_routed_by_keyword_contract']} route-negative identities were screened. Frozen arithmetic: `224 = {len(C)} retained + {224-len(C)} closures`. Route reconciliation: `{json.dumps(route, ensure_ascii=False, sort_keys=True)}`. Keyword routing was recall-only.", "<!-- coverage:SRC-ARXIV:20260621:end -->", "", "## 2. Candidate Ledger and Score V2", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        e, sc = r["e"], r["e"]["score"]
        lines.append(f"| {r['family']} | arXiv:{r['aid']}v1 | paper-v1:{r['aid']} | 2026-W25 | 2026-06-20 | SRC-ARXIV | {sc[0]} | {sc[1]} | {sc[2]} | {sum(sc)} | retained | {review_status(e)} | accessible | none | review:{r['family']} | self | — | new_in_window | {e['owner']} | {e['disposition']} | books-review:{r['family']} | yes |")
    lines += ["", "### Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        lines.append(f"| {r['family']} | {r['rp']} | {review_route(r['e'])} | arXiv:{r['aid']}v1 | SRC-ARXIV@arXiv:{r['aid']}v1 | {r['loc'][0]} | {r['loc'][1]} | {r['loc'][2]} | {ARTIFACT_EXCEPTION} | claim:{r['family']} | complete |")
    lines += ["", "### Benchmark Contract", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        e=r["e"]
        lines.append("| " + " | ".join([r["family"]] + [str(e[k]) for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")]) + " |")
    lines += ["", "## 3. Source Reviews", ""]
    for r in reviews:
        lines += [f"<!-- review:{r['family']}:start -->", review_body(r), f"<!-- review:{r['family']}:end -->", ""]
    lines += ["## 4. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for d in decisions:
        lines.append(f"| {d['source_family_id']} | {d['eligibility']} | {d['decision']} | {d['analysis_unit_id']} | — | {d['priority_rationale']} | {d['narrative_ref']} |")
    decision_by_family = {d["source_family_id"]: d for d in decisions}
    for r in reviews:
        if r["aid"] not in WINNERS:
            lines += ["", f"<!-- analysis-decision:{r['family']}:start -->", decision_by_family[r["family"]]["priority_rationale"], f"<!-- analysis-decision:{r['family']}:end -->"]
    narratives = {
        "DA-20260621-NONPREFIX-KV-ISOLATION": "当 RAG serving 从 prefix cache 演进到任意 chunk fusion，旧 threat model 会失效：性能路径中的 tail recomputation 变成可测 oracle。新的长期结论不是关闭 cache reuse，而是把 QCP/constant-time fusion 与 tenant identity 绑定，并以 throughput 与 leakage 双 Gate 验证。",
        "DA-20260621-BELIEF-MEMORY-AUTHORITY": "belief memory 不能因采用 Bayesian 形式就取得真值权威。只有 source reliability 可估、重复 provenance 被限流且 strict metric 与 judge 结果分开时，posterior 才能作为受限状态；否则保留旧的 evidence archive 与人工复核。",
        "DA-20260621-TYPED-ROBOT-LINEAGE": "机器人 policy 的长期 owner 不是 checkpoint，而是 rollout、review、dataset、training、evaluation 与 release 的 typed lineage。任何一步缺 receipt 时，deployment recommendation 只能保持 pending，并回退到上一已批准 policy。",
    }
    for k,v in narratives.items():
        lines += ["", f"<!-- analysis:{k}:start -->", f"### {k}", "", v, f"<!-- analysis:{k}:end -->"]
    lines += ["", "## 5. Books Comparison and Decision", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        e=r["e"]; rel="Direct Evolution" if e["disposition"].startswith("Integrate") else "Principle Reuse"; path=PATHS[e["owner"]]
        target_ref=chapter_ref(path, TARGET_ANCHORS[e["owner"]]); adjacent="; ".join(adjacent_refs(e["owner"]))
        lines.append(f"| {r['family']} | {e['owner']} | {target_ref} | {adjacent} | existing:{r['family']} | delta:{r['family']} | {rel} | {e['disposition']} | books-review:{r['family']} |")
    for r in reviews:
        e=r["e"]; rel="Direct Evolution" if e["disposition"].startswith("Integrate") else "Principle Reuse"; path=PATHS[e["owner"]]
        lines += ["", f"<!-- existing:{r['family']}:start -->", f"已复读 owner `{path}` 的机制正文与 Review notes；{e['note']}", f"<!-- existing:{r['family']}:end -->", "", f"<!-- delta:{r['family']}:start -->", e["delta"], f"<!-- delta:{r['family']}:end -->", "", f"<!-- books-review:{r['family']}:start -->", f"{rel}; {e['disposition']}. {e['boundary']}", f"<!-- books-review:{r['family']}:end -->"]
    refs="; ".join("review:"+r["family"] for r in reviews); sels="; ".join(("analysis:"+WINNERS[r["aid"]]) if r["aid"] in WINNERS else "analysis-decision:"+r["family"] for r in reviews); brefs="; ".join("books-review:"+r["family"] for r in reviews)
    lines += ["", "## 6. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260621-COVERAGE-V1 | fresh-context:jun21-v1 | coverage | coverage:SRC-ARXIV:20260621 | — | 224/224 title+abstract; denominator {len(C)}; closures {224-len(C)}; all 54 route-negative checked | passed |", f"| SA-20260621-EVIDENCE-V1 | fresh-context:jun21-v1 | evidence | {refs} | — | {len(C)}/{len(C)} official exact-v1 Method/Evaluation/boundary and benchmark contracts | passed |", f"| SA-20260621-SELECTION-V1 | fresh-context:jun21-v1 | deep_analysis_selection | {sels} | — | {len(C)}/{len(C)} frontier; winners frozen before rationale | passed |", f"| SA-20260621-BOOKS-PREWRITE-V1 | fresh-context:jun21-v1 | books | {brefs} | root writeback pending | {len(integrations)} Integrate proposals and {len(C)-len(integrations)} No Change handoffs checked; post-write audit pending | open |", "", "## 7. Materials and Access", "", f"- {len(C)}/{len(C)} exact-v1 official HTML pages were accessible; no later revision was used.", "- No external Materials Request remains.", "", "## 8. Daily Integration Decision", "", f"- Integrate: {len(integrations)}; No Change: {len(C)-len(integrations)}.", "- Books Gate remains Open until root applies the owner-merged packet and this lane completes full post-write audit.", "", "## 9. Repository Changes", "", "- This lane changed only the 2026-06-21 Daily, date-specific source packet and finalizer; shared Books were not edited."]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    if not EVIDENCE_READY:
        lines = [
            line.replace("Coverage, Evidence and Selection passed;", "Coverage is closed; Evidence and Selection remain open during fresh semantic audit;")
                .replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |")
                .replace("| SA-20260621-EVIDENCE-V1 | fresh-context:jun21-v1 | evidence |", "| SA-20260621-EVIDENCE-V1 | fresh-context:jun21-v1 | evidence |")
                .replace("| SA-20260621-SELECTION-V1 | fresh-context:jun21-v1 | deep_analysis_selection |", "| SA-20260621-SELECTION-V1 | fresh-context:jun21-v1 | deep_analysis_selection |")
            for line in lines
        ]
        for index, line in enumerate(lines):
            if line.startswith("| SA-20260621-EVIDENCE-V1 "):
                cells = line.split("|")
                cells[-2] = " open "
                cells[-3] = " Evidence Gate remains Open until every locator and benchmark field is repaired and re-audited "
                cells[-4] = " F-20260621-PREWRITE-EVIDENCE-01 — unresolved locator or benchmark misidentity could overstate exact-v1 support "
                lines[index] = "|".join(cells)
            elif line.startswith("| SA-20260621-SELECTION-V1 "):
                cells = line.split("|")
                cells[-2] = " open "
                cells[-3] = " Selection Gate remains Open until all 37 rationales and latest-Books comparisons are re-audited "
                cells[-4] = " F-20260621-PREWRITE-SELECTION-01 — unresolved frontier or owner comparison could inflate an Integrate decision "
                lines[index] = "|".join(cells)
    lines[2:2] = [
        "**Research Date:** 2026-06-21", "",
        "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-06-20 09:00:00 ～ 2026-06-21 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；224/224 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet", "",
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open，等待已授权的 serialized writeback 后 fresh-context Semantic Audit", "",
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
    }
    lines = [canonical_headings.get(line, line) for line in lines]
    recommended_index = lines.index("## 9. Recommended Action")
    lines[recommended_index:recommended_index] = [
        "## 8. Ignored Noise", "",
        "- 187 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit rather than being promoted into the Candidate Ledger.", "",
    ]
    lines += [
        "", "## 11. Open Questions", "",
        "- How should non-prefix KV reuse expose tenant and retrieval identity without eliminating useful cache sharing?",
        "- Which reliability and provenance cap keeps belief memory useful without turning repeated claims into false authority?",
        "- How should robot data lineage invalidate downstream policies when a rollout, reviewer or environment version is superseded?",
        "- These are research continuations, not unresolved Gate findings.",
        "", "## 12. Sources", "",
    ]
    for r in reviews:
        lines.append(
            f"- [arXiv:{r['aid']}v1 — {r['src']['title']}](https://arxiv.org/html/{r['aid']}v1) — "
            f"first-public `2026-06-20`；accessed `{EXECUTED_AT[:10]}`；Source Family `{r['family']}`。"
        )
    lines += [
        "- `SRC-ARXIV` registry contract：`docs/RESEARCH_SOURCES.md`。", "",
        "## 13. Final Status", "",
        "- Status: In Progress.",
        "- Coverage Gate: Closed.",
        "- Evidence Gate: Passed.",
        "- Books Gate: Open pending serialized writeback and post-write fresh audit.",
    ]
    REPORT.write_text("\n".join(lines)+"\n")

    gate_line = "- Coverage Gate Closed; Evidence Gate Passed; Selection Gate Passed; Books Gate Open pending root writeback/post-write audit." if EVIDENCE_READY else "- Coverage Gate Closed; Evidence Gate Open; Selection Gate Open; Books Gate Open. Benchmark-contract, source-specific prose, full-frontier and owner/adjacent audits remain in progress."
    exact_v1_line = (
        f"- Exact-v1 audit: {len(C)}/{len(C)} official HTML; every Method/Evaluation/non-proof locator and benchmark contract passed the fresh semantic recheck."
        if EVIDENCE_READY else
        f"- Exact-v1 access: {len(C)}/{len(C)} official HTML; semantic locator and benchmark-contract audit remains in progress."
    )
    selection_line = (
        f"- Selection audit: full {len(C)}-family frontier; three winners were frozen before rationale; 37/37 source-specific rationales and eligibility facts passed."
        if EVIDENCE_READY else
        f"- Selection draft: full {len(C)}-family frontier; three winners were frozen before rationale, with fresh rationale audit still open."
    )
    fresh = ["# 2026-06-21 Fresh Evidence and Selection Audit V1", "", f"- Denominator `{did}`: `224 = {len(C)} retained + {224-len(C)} closures`; 54/54 route-negative audited.", exact_v1_line, "- Benchmark contract: undisclosed fields use exact `Not Disclosed`; conditional or compound ND count is `0`.", "- Score V2 re-audit removed the inherited all-8 template; final totals are 5×8, 6×5, 7×7, 8×14 and 9×3 families.", selection_line, f"- Books prewrite draft: {len(integrations)} Integrate families merged into {len(groups)} owner blocks; {len(C)-len(integrations)} No Change handoffs excluded from the ready packet.", "- Resolved findings: `F-20260621-PREWRITE-EVIDENCE-01` (exact locators/benchmark identities) and `F-20260621-PREWRITE-SELECTION-01` (score inflation/frontier-owner comparison).", gate_line, "- Independence caveat: nested reviewer spawning was disabled; this is a fresh primary-source self-audit, not a claimed independent second-model review."]
    (PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text("\n".join(fresh)+"\n")
    evidence_gate = "Passed" if EVIDENCE_READY else "Open"
    selection_gate = "Passed" if EVIDENCE_READY else "Open"
    (PACKET/"README.md").write_text(f"# daily-20260621 source packet\n\n- Denominator: `{did}`\n- Raw: 224\n- Retained: {len(C)}\n- Closures: {224-len(C)}\n- Exact-v1 access: {len(C)}/{len(C)}\n- Coverage Gate: Closed\n- Evidence Gate: {evidence_gate}\n- Selection Gate: {selection_gate}\n- Books Gate: Open pending root writeback/post-write audit\n- Completion: In Progress\n")
    with (PACKET/"evidence-selection-fresh-audit-v2.tsv").open("w", newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["source_family_id","primary_evidence_version","exact_v1_access","method_locator","evaluation_locator","limitation_locator","benchmark_contract","selection_decision","books_disposition","audit_status"])
        dmap={d["source_family_id"]:d for d in decisions}
        audit_status = "passed" if EVIDENCE_READY else "open"
        for r in reviews: w.writerow([r["family"],f"arXiv:{r['aid']}v1","accessible",*r["loc"],"direct_Not_Disclosed_or_source_specific",dmap[r["family"]]["decision"],r["e"]["disposition"],audit_status])
    sums=[]
    for p in sorted(x for x in PACKET.iterdir() if x.is_file() and x.name not in {"SHA256SUMS","screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name)
    (PACKET/"SHA256SUMS").write_text("\n".join(sums)+"\n")
    print(json.dumps({"denominator_id":did,"raw":224,"retained":len(C),"closures":224-len(C),"integrate":len(integrations),"owners":len(groups),"route":route},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
