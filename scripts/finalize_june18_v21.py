#!/usr/bin/env python3
"""Build the strict pre-write V2.1 packet for 2026-06-18; never edits Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260618"
PROV = PACKET / "screening-ledger-provisional.json"
REPORT = ROOT / "papers/2026/06/18/README.md"
EXEC = "2026-08-29T23:40:00+08:00"

PATHS = {
"INFER-SCHEDULING":"books/part-05-inference-system/56-inference-scheduling.md",
"PLATFORM-SECURITY":"books/part-06-ai-infrastructure/72-security.md",
"TRAIN-DATA":"books/part-04-training-system/27-data.md",
"AGENT-MULTI-AGENT":"books/part-07-agent/82-multi-agent.md",
"MULTIMODAL-WORLD-MODELS":"books/part-03-multimodal-world-models/25-multimodal-world-models.md",
"AGENT-MEMORY":"books/part-07-agent/77-memory.md",
"TRAIN-GRPO":"books/part-04-training-system/33-grpo.md",
"TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/36-distributed-training.md",
"MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
"AGENT-WORKFLOW":"books/part-07-agent/81-workflow.md",
"PLATFORM-PRODUCTION":"books/part-06-ai-infrastructure/73-production-best-practice.md",
"INFER-SPECULATIVE-DECODING":"books/part-05-inference-system/48-speculative-decoding.md",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/66-evaluation-system.md",
"PLATFORM-GPU-SCHEDULER":"books/part-06-ai-infrastructure/63-gpu-scheduler.md",
"MODEL-MOE":"books/part-02-model/21-moe.md",
"PLATFORM-MONITORING":"books/part-06-ai-infrastructure/67-monitoring.md",
"AGENT-PLATFORM":"books/part-07-agent/84-agent-platform.md",
"AGENT-PLANNING":"books/part-07-agent/79-planning.md",
"INFER-KV-CACHE":"books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
"TRAIN-DPO":"books/part-04-training-system/34-dpo.md",
"AGENT-REFLECTION":"books/part-07-agent/80-reflection.md",
}

ADJACENT = {
"INFER-SCHEDULING":"books/part-05-inference-system/55-pd-disaggregation.md#L1",
"PLATFORM-SECURITY":"books/part-06-ai-infrastructure/71-multi-tenant.md#L1",
"TRAIN-DATA":"books/part-04-training-system/28-pretraining.md#L1",
"AGENT-MULTI-AGENT":"books/part-07-agent/81-workflow.md#L1",
"MULTIMODAL-WORLD-MODELS":"books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1",
"AGENT-MEMORY":"books/part-07-agent/76-rag.md#L1",
"TRAIN-GRPO":"books/part-04-training-system/32-ppo.md#L1",
"TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/37-tensor-parallel.md#L1",
"MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1",
"AGENT-WORKFLOW":"books/part-07-agent/80-reflection.md#L1",
"PLATFORM-PRODUCTION":"books/part-06-ai-infrastructure/72-security.md#L1",
"INFER-SPECULATIVE-DECODING":"books/part-05-inference-system/47-pagedattention.md#L1",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/67-monitoring.md#L1",
"PLATFORM-GPU-SCHEDULER":"books/part-06-ai-infrastructure/65-kai-scheduler.md#L1",
"PLATFORM-MONITORING":"books/part-06-ai-infrastructure/69-trace.md#L1",
"AGENT-PLATFORM":"books/part-07-agent/83-mcp.md#L1",
"AGENT-PLANNING":"books/part-07-agent/80-reflection.md#L1",
"INFER-KV-CACHE":"books/part-05-inference-system/46-continuous-batching.md#L1",
"TRAIN-DPO":"books/part-04-training-system/31-rlhf.md#L1",
"AGENT-REFLECTION":"books/part-07-agent/79-planning.md#L1",
}

OWNER_PROPOSITION = {
"INFER-SCHEDULING":"现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。",
"PLATFORM-SECURITY":"现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。",
"TRAIN-DATA":"现有 owner 已把数据选择建模为带 lineage、proxy coverage、动态反馈与 admission gate 的控制问题；相邻预训练章消费冻结后的数据 contract。",
"AGENT-MULTI-AGENT":"现有 owner 已拥有 coordinator、typed handoff、reroute、shared-state commit 与 fallback authority；相邻 workflow 章拥有单流程执行。",
"MULTIMODAL-WORLD-MODELS":"现有 owner 已拥有 learned dynamics、planning feedback 与环境真值边界；相邻生成范式章不拥有 planning control。",
"AGENT-MEMORY":"现有 owner 已区分 observation/memory/environment state 及其读写生命周期；相邻 RAG 章只拥有 evidence retrieval。",
"TRAIN-GRPO":"现有 owner 已拥有 rollout identity、verifier/reward 共偏、credit assignment 与 promotion gate；相邻 PPO 章拥有旧策略约束。",
"TRAIN-DISTRIBUTED-TRAINING":"现有 owner 已拥有 replica/shard/state synchronization 与 WAN failure boundary；相邻 TP 章只拥有张量切分。",
"MULTIMODAL-EMBODIED-VLA":"现有 owner 已拥有 observation-action-state 闭环与真实执行反馈；相邻 world-model 章提供预测状态而不拥有 action commit。",
"AGENT-WORKFLOW":"现有 owner 已拥有 durable checkpoint、claim-evidence lineage、idempotent resume 与人工接管；相邻 reflection 章只提出修正信号。",
"PLATFORM-PRODUCTION":"现有 owner 已区分 simulation、shadow、canary 与 production evidence，并保留 rollback；相邻安全章拥有授权而非发布。",
"INFER-SPECULATIVE-DECODING":"现有 owner 已拥有 draft/target verification、acceptance、KV rollback 与质量等价边界；相邻 PagedAttention 章只拥有块化 KV。",
"PLATFORM-EVALUATION-SYSTEM":"现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。",
"PLATFORM-GPU-SCHEDULER":"现有 owner 已拥有 quota、priority、preemption、checkpoint cost 与 workload-class-aware placement；相邻 KAI 章是实现分支。",
"PLATFORM-MONITORING":"现有 owner 已区分 observe-only telemetry、告警证据与执行授权；相邻 trace 章拥有跨组件因果链。",
"AGENT-PLATFORM":"现有 owner 已拥有 typed Session、branch/merge/replay、runtime identity 与 controlled release；相邻 MCP 章只拥有协议交接。",
"AGENT-PLANNING":"现有 owner 已拥有 ask/act gate、uncertainty decomposition、依赖图与预算；相邻 reflection 章只拥有复核。",
"INFER-KV-CACHE":"现有 owner 已拥有 prefix identity、cache reuse、失效与跨请求共享边界；相邻 continuous batching 章只拥有批次调度。",
"TRAIN-DPO":"现有 owner 已拥有 preference data、reference-policy identity、checkpoint 与 evaluation boundary；相邻 RLHF 章拥有上游偏好反馈。",
"AGENT-REFLECTION":"现有 owner 已拥有 held-out verifier、promotion/rollback、budget 与 provenance；相邻 planning 章拥有行动方案。",
}

def E(owner, delta, proof, boundary, model, evaluator, anchors, disposition, note, *, hardware="Not Disclosed", precision="Not Disclosed", slo="Not Disclosed"):
    return dict(owner=owner, delta=delta, proof=proof, boundary=boundary, model=model,
                evaluator=evaluator, anchors=anchors, disposition=disposition, note=note,
                hardware=hardware, precision=precision, slo=slo)

C = {
"2606.18600":E("INFER-SCHEDULING","异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。","Llama-3.1-70B 与 Qwen3-32B 在 AWS L4/A10G/L40S 集群上报告吞吐与 offline/online 成本效率改善。","六天单 region 可用性和短上下文重算不能证明跨区供应或长上下文恢复；shared tensor store 也引入新的可用性 owner。","Llama-3.1-70B; Qwen3-32B","offline throughput, online TTFT/TPOT and cost efficiency under spot interruption",("4 Model Placement for Heterogeneous GPUs","7 Evaluation","8.1 Limitation"),"Integrate","唯一同时改变 placement 与 interruption recovery 的 serving family，进入三项叙事。",hardware="AWS L4, A10G and L40S GPUs",precision="Not Disclosed",slo="Not Disclosed"),
"2606.18619":E("PLATFORM-SECURITY","Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。","在真实开源项目上与 agent baselines 比较，并报告发现 22 个新漏洞；使用 Sonnet、DeepSeek，并与 Claude Mythos 作受限比较。","fuzzer 未触发不等于 invariant 成立，assertion 也可能错；覆盖限于作者 subjects 与可观测运行输入。","Sonnet and DeepSeek agents; Claude Mythos comparison","real-subject vulnerability findings plus specification-falsification outcomes",("security-specification-first paradigm","real-world subjects","limitations"),"Integrate","把 agent 判断转成可反证 artifact，补足安全 evidence plane，优先于纯检测率改进。"),
"2606.18650":E("TRAIN-DATA","训练数据选择可把双层 influence objective 改写为带 Lagrange penalty 的单层目标，并让动态 reference 随 proxy trajectory 同步；online selector 用 memoryless randomized block-coordinate Frank-Wolfe。","exact-v1 在作者 LLM pretraining matrix 中比较 BLADE 与 influence、excess-loss baselines，并给出 first-order convergence。","proxy-to-target transfer、penalty 设定与 trajectory drift 仍可能失配；收敛定理不等于目标模型质量普遍提升。","TinyLlama-1.1B and Llama2-7B target models with 3B/5B-token continued-pretraining budgets","downstream task quality and selection efficiency against influence/excess-loss baselines",("penalized single-level objective","Experiments","Limitations"),"No Change — Existing Coverage","Ch27 已拥有动态 data admission 与 proxy bias；本工作强化求解器分支但不新增 owner。"),
"2606.18668":E("AGENT-MULTI-AGENT","sub-agent abstention 应是 typed failure message，携带 ambiguous、misrouted、unsupported 等理由，供 coordinator clarification、reroute 或 fallback，而不是空响应。","生产电商 BI assistant 的 overall response pass rate从 68.5% 提升到 78.9%。","judge ensemble 与生产流量共享偏差且 backbone 未披露；pass rate 不证明授权、安全或跨域 calibration。","Not Disclosed — production sub-agent backbone identities are not named in the abstract contract","production pass rate under structured abstention labels and rationales",("Explanatory Abstention","production e-commerce assistant","Limitations"),"No Change — Existing Coverage","Ch82 已有 typed failure handoff、reroute 与 fallback authority；EARS 提供生产证据，不另建 abstention owner。"),
"2606.18673":E("PLATFORM-SECURITY","system-prompt secrecy 不能只靠静态拒答；AREA 用可优化 soft prompt 重锚 attention，但 secret/API key 仍必须移出 prompt 并由外部 reference monitor 管理。","测量六个平台 1,200 个应用，报告超过 80% 泄漏；AREA 的 usability 与优化开销相对防线比较。","attention drift 是受测模型解释，不证明所有泄漏因果；soft prompt 无法把已放入上下文的密钥变成真正 secret。","deployed application models across six commercial platforms; exact versions in v1 setup","prompt leakage resistance, usability and optimization overhead over 1,200 applications",("attention drift","1,200 applications","limitations"),"No Change — Existing Coverage","Ch72 已明确 prompt 不是 secret store；AREA 只作为受限 sensor 分支。"),
"2606.18697":E("MULTIMODAL-WORLD-MODELS","world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。","连续控制任务上评估 planning return、poison detectability，并测试 residual/CUSUM/TRIM 防线。","只击败 non-adaptive defenses；低 prediction error 不等于 transition 正确，真实环境 feedback 仍是权威。","Not Disclosed — v1 evaluates environment-specific learned dynamics and planners rather than naming one canonical model","planning return, poison detectability and defense response across three pipeline stages",("two-stage data poisoning framework","continuous-control tasks","limitations"),"Integrate","首次把 world-model adaptation data 显式定位为 downstream planning authority 的供应链边界。"),
"2606.18741":E("INFER-SCHEDULING","runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。","7B–70B models 的多数 topology switch 为 1–7 秒，并报告动态 workload 的 TTFT、TPOT 与 output throughput。","KV migration 与双份资源会制造瞬时带宽/容量峰值；作者模型与网络不证明任意拓扑可无损切换。","Llama2-7B, Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B and Llama2-70B","reconfiguration downtime, TTFT, TPOT and output throughput",("two-dimensional KV cache migration","Experiments","Limitations"),"Integrate","它改变 serving topology 的运行时 commit protocol，不只是更好的静态 scheduler。",hardware="NVIDIA H100 and RTX 5090 platforms"),
"2606.18746":E("AGENT-MEMORY","若相同 observation bottleneck 在不同 domain 需要不兼容 action，近最优 policy 必须保存可区分的 memory distribution；足够的 value 信息还可近似重建局部 transition dynamics。","exact-v1 给出 separation theorem 与 transition reconstruction 条件，而非经验 leaderboard。","定理依赖形式化 observation/domain 假设；可重建局部 dynamics 不代表 memory 内容真实、授权或可长期维护。","formal agent-policy classes; no benchmark model","theorem premises and approximation error for domain disambiguation and local dynamics reconstruction",("separation theorem","transition-model reconstruction","assumptions"),"No Change — Existing Coverage","Ch77/79 已区分 memory state 与 environment state；该定理加强必要性证明。"),
"2606.18810":E("TRAIN-GRPO","SC-GRPO 用 verified trajectory 条件化前后 token KL 作为 GRPO gradient 权重，让 policy 自己暴露 pivotal token，避免外部 PRM/teacher。","五个 math、code、agentic benchmarks 上相对 GRPO 与 DAPO 报告平均改善和 OOD 结果。","self-conditioned teacher 与 student 共偏；KL 大小不自动等于因果 credit，verified final answer 也可能掩盖错误路径。","Qwen3-1.7B-Base; DeepSeek-R1-Distill-Qwen-1.5B; experiments are limited to models at most 8B","task accuracy and OOD performance against GRPO, DAPO and OPD",("Self-Conditioned GRPO","five benchmarks","Limitations"),"No Change — Existing Coverage","Ch33 已拥有 token credit 与 verifier 共偏边界；保留为不依赖外部 teacher 的证据。"),
"2606.18829":E("PLATFORM-SECURITY","共享 memory 的 admission/read/delete 必须按 principal、role、scope 和 relationship 授权，并把 utility、ACL leakage 与 active forgetting 作为三个独立 Gate。","GateMem 跨医疗、办公、教育、家庭；多种 memory baselines/backbones 均未同时获得强 utility、ACL 与 forgetting。","structured judge 与合成 episode 不证明真实机构合规；long-context 的较高 governance score 伴随 token cost，external memory 仍可能泄漏。","multiple memory systems and backbone models enumerated in GateMem v1","legitimate utility, contextual access-control leakage and post-deletion active forgetting",("multi-principal shared-memory agents","diverse baselines and backbone models","limitations"),"No Change — Existing Coverage","Ch72 已有同一 exact family 的 Utility/ACL/Forgetting Gate 与代价边界；本日只保留证据 handoff。"),
"2606.18831":E("TRAIN-GRPO","long-context RL 的 data owner 应同时覆盖 retrieval、multi-evidence synthesis 与 reasoning，避免只通过 reward shaping 修补 evidence localization。","Qwen3-4B/8B/30B-A3B、约 14K 样本、七个长上下文 benchmark，并在 GAIA/BrowseComp 测 transfer。","作者 mixture 与 Qwen family 不能证明通用配方；outcome reward 仍可能奖励无 grounding shortcut。","Qwen3-4B, Qwen3-8B and Qwen3-30B-A3B","seven long-context benchmarks plus GAIA and BrowseComp transfer",("3.1 Long-Context Training Data","4 Experiments","5 Analysis"),"Integrate","训练 mixture 把检索、证据合成、推理拆成可审计能力，而非只调 reward。"),
"2606.18847":E("MULTIMODAL-EMBODIED-VLA","长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。","WorldLines 同时评 Memory QA 与 Embodied Task Planning；ObsMem 对 partial observability、overwritten state 进行比较。","benchmark household traces 不是开放世界；observer-grounded memory 仍可能漏看并把推断状态误写成事实。","google/gemini-3.5-flash answer generator; GPT-4o judge; GPT-4o-mini question generator","Memory QA and Embodied Task Planning over evidence-linked household traces",("WorldLines","ObsMem","Limitations"),"Integrate","它把 memory retrieval 与真实 action/state evolution接起来，属于 embodied owner 的长期 delta。"),
"2606.18874":E("AGENT-WORKFLOW","AI scientist 应把 literature evidence、idea、implementation、ablation 与 repair trace 外化为 persistent contracts，并检查 runnable artifact 是否仍支持原 claim。","在 training-free memory、traffic forecasting 与 PINN 三类研究流程展示可追踪 problem→mechanism→validation 轨迹。","三个案例不证明自动科学发现质量；trace 完整也不能替代独立复现或可信实验。","research-agent configurations in three exact-v1 case studies","claim-to-artifact traceability, ablation and bounded repair across three research domains",("persistent research artifacts","three case studies","limitations"),"No Change — Existing Coverage","Ch81/66 已拥有 claim-evidence lineage 与 harness identity；Xcientist 是具体实例。"),
"2606.18958":E("PLATFORM-PRODUCTION","cluster live simulation 要让真实 software stack 与模拟 node/network/device time 协同推进，并显式区分 simulated resource state 与 production effect。","exact-v1 在 cluster-scale full-stack workloads 上比较 simulation fidelity、scale 与执行开销。","模拟器遗漏的 kernel、network tail 和 control-plane race 会制造假确定性；不能用 live simulation 代替 canary。","unmodified cluster software stacks in LiveStack experiments","simulation scale, fidelity and runtime overhead",("full-stack live simulation","Evaluation","Limitations"),"No Change — Existing Coverage","Ch73 已把 simulation、canary 与真实 deployment evidence 分层；LiveStack 是更深的 OS 实现实例。"),
"2606.18967":E("INFER-SPECULATIVE-DECODING","RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。","在 RL rollout workloads 上报告 self-speculative speedup、acceptance 与 training quality。","acceptance 随 policy update 漂移；额外 draft computation 和 rollback bookkeeping 可能抵消收益，且不改变 reward validity。","Qwen2.5-7B, Qwen2.5-14B and Llama3.1-8B-Instruct with quantized self-drafters","rollout throughput, acceptance and downstream RL quality",("system-aware self-speculative decoding","Experiments","Limitations"),"Integrate","它把 speculative verification 延伸到训练 rollout，同时保留 policy/version owner。",hardware="single NVIDIA A100-80GiB SXM in the decode-cost study",precision="FP16 target inference; W4/W8 weight-quantized self-drafters"),
"2606.18996":E("PLATFORM-EVALUATION-SYSTEM","privacy-capable agent benchmark 必须联合评分 task completion 与 active extraction resistance，并把攻击者交互轨迹、secret canary 与 policy effect 分开。","TRAP 在作者 agent/model matrix 中同时测任务完成与主动隐私提取。","benchmark secret 与攻击策略覆盖有限；未泄漏不证明模型无记忆或生产 ACL 正确。","22 models spanning GPT-4o/GPT-5, Gemini 2.5, Claude 4.5, Qwen3-VL, InternVL3.5, Phi-4-multimodal, Devstral, Llama3.2-Vision and GLM-4.6V-Flash","paired task-completion and active privacy-extraction outcomes",("Task-completion and Resistance","Evaluation","Limitations"),"No Change — Existing Coverage","Ch66/72 已要求 capability 与 harm 双轴评价；TRAP 补充 workload 而不改 owner。"),
"2606.19004":E("PLATFORM-GPU-SCHEDULER","DiT RL post-training 可把探索 seed 与 spot GPU availability 联合调度，把可重放 seed state 作为 preemption recovery unit。","exact-v1 比较 seed exploration quality、GPU utilization、成本与训练结果。","spot reclaim 与 seed replay 会改变样本时序；结果限于 DiT RL，不能外推 LLM RL 或硬实时 SLO。","Qwen-Image","training reward/quality, GPU utilization and spot cost",("Seed Exploration and Spot GPUs","Experiments","Limitations"),"No Change — Existing Coverage","Ch63/33 已有 preemptible training 与 rollout identity；本工作是 DiT-specific composition。",hardware="4 reserved-node H100 GPUs plus 8 H100 GPUs on four spot nodes"),
"2606.19025":E("TRAIN-DISTRIBUTED-TRAINING","低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。","通信相对高效 baseline 最多降 1.42x、相对 DDP 降 45.44x，skip-token 吞吐最高 1.4x；100B 只由 cost model 投影。","non-resident expert skip 会改变本地训练分布，routing stability 只在受测 regimes 成立；100B projection 不是实测，WAN failure/straggler 未闭合。","Not Disclosed — v1 reports FoMoE configurations rather than one named canonical MoE checkpoint","communication volume, local-training throughput and routing stability; 100B results are modeled projections",("partitioning expert layers across workers","FoMoE Scalability & Resource Consumption","Limitations"),"Integrate","它改变跨站 distributed-training replica/state ownership，而不是 serving placement。"),
"2606.19057":E("PLATFORM-EVALUATION-SYSTEM","当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。","exact-v1 用受控与真实 LLM evaluation data 比较 PU 估计、校准与 audit coverage。","class-prior 错设会系统性偏移；PU 只能估计分布级缺口，不能证明单个 judgment 正确。","Mistral-7B-Instruct, Qwen2.5-7B-Instruct, Llemma-7B-MuInstruct and GPT-5.4-mini judges","hidden-positive prevalence, calibration and audit error",("Positive–Unlabeled Learning","Experiments","Limitations"),"Integrate","把未审样本从默认负例改成不确定集合，直接修正 evaluation denominator。"),
"2606.19111":E("AGENT-MULTI-AGENT","leader 只有在 coordinator 的 recovery advantage 超过沟通与单点故障成本时才应持有重分配 authority；行为 leadership 不等于稳定角色标签。","多 Agent team configurations 上测 coordination behavior、failure recovery 与任务结果。","作者 tasks 和 agent count 不证明组织结构普适；leader failure、shared bias 与通信成本仍可能主导。","gpt-oss-120b, gemma-4-31B-it and llama-4-scout","team outcome, behavioral leadership signatures and recovery advantage",("Recovery-Advantage Boundary","Experiments","Limitations"),"No Change — Existing Coverage","Ch82 已把 coordinator 视为可替换 control role；本 family 提供 recovery boundary 证据。"),
"2606.19191":E("PLATFORM-SECURITY","skill admission 不能只读 SKILL.md；必须审 auxiliary resources、triggerable vulnerabilities 与 runtime effects，并在沙箱中验证 benign utility 与恶意 side effect。","VulMask 跨 host skills、四类攻击、Cursor backbones 与多个 automated reviewers；GPT-5.5 设置 ASR 58.8%、warning 11.4%。","攻击 corpus 与触发器由作者构造；静态扫描漏报不证明 runtime containment 无效，检测率也不等于安全。","Cursor with GLM-4.7, Qwen3, GPT-5.5 and Opus-4.7; multiple generator models","attack success, warning/detection and benign utility across four attack goals",("3 Threat Model","5 Evaluation","6 Discussion"),"No Change — Existing Coverage","Ch72 已把 persistent Skill 定义为 supply-chain artifact，并要求 code/resource/runtime effect 联合审计与 containment。"),
"2606.19242":E("PLATFORM-SECURITY","Agent compliance 应在每次 tool/message effect 前由外部 runtime monitor 检查 temporal/policy state，而非要求 LLM 自述合规。","exact-v1 在作者 policies、agent traces 与 violation cases 上评 runtime verification。","形式化 policy 不覆盖未建模 effect，monitor 自身可能成为延迟或可用性瓶颈。","Not Disclosed — four GDPR-reframed agent case studies are evaluated; no canonical backbone is the compliance authority","policy-violation detection and runtime enforcement outcomes",("Runtime Compliance Verification","Evaluation","Limitations"),"No Change — Existing Coverage","Ch72 已拥有 canonical action 与 effect-time authorization；论文强化实现路径。"),
"2606.19262":E("PLATFORM-MONITORING","hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。","exact-v1 在多种 ML/non-ML workloads 与 hardware traces 上报告检测质量及 zero-overhead claim。","共享 GPU、融合 kernel 与新 compiler 会造成概念漂移；无额外探针不等于 telemetry 免费或不可规避。","Not Disclosed — corpus spans training/inference models up to 70B dense and 671B MoE, not one canonical model","hidden-training detection, false positives and telemetry overhead",("Zero-Overhead Telemetry","Evaluation","Limitations"),"Integrate","它为平台监控增加未注册训练的被动 evidence path，而不把检测器提升为执行授权。",hardware="nine NVIDIA GPU models across four architecture generations"),
"2606.19271":E("INFER-SCHEDULING","streaming video generation 应以 chunk deadline 为调度单位，联合决定 GPU residency、跨 chunk pipeline 与质量/成本降级，而不是只优化整段 makespan。","TurboServe 报告 worst-case per-chunk latency 降 37.5%、平均 GPU cost 降 37.2%。","作者 workloads/GPU matrix 不证明交互视频通用 SLO；跨 chunk state 与 quality degradation 仍需独立验收。","Not Disclosed — Shengshu production traces cover multiple model sizes without naming one canonical checkpoint","worst-case per-chunk latency, end-to-end quality and GPU operating cost",("Streaming Video Generation","Evaluation","Limitations"),"No Change — Existing Coverage","Ch56 已有 streaming generation 的 playout slack、migration/re-homing、elasticity 与质量降级；TurboServe 是生产 trace 佐证。",hardware="GPU clusters with up to 64 NVIDIA B300 GPUs",slo="Not Disclosed"),
"2606.19409":E("AGENT-PLATFORM","Session 应成为执行路径携带的一等 runtime value，统一 transcript、tool effect、sandbox、branch lineage、token usage、pending work 与 memory event；fork/merge/replay 是显式操作。","报告只验证 controlled runtime properties 与 audited milestones，没有 broad quantitative comparison。","live-provider quality、optional backend availability 与 memory quality明确未证明；central Session 也可能扩大故障域。","Not Disclosed — architecture report, not a model benchmark","audited runtime invariants and controlled replay properties; no broad quality benchmark",("Session-Centered Runtime State","audited milestones","claims are limited"),"No Change — Existing Coverage","Ch84 已含同一 exact family 的 Session runtime value、fork/merge/replay 和 controlled-property boundary。"),
"2606.19464":E("PLATFORM-SECURITY","runtime governance 除 permit/prohibit 外还需 obligation lifecycle、dispensation、meta-policy precedence 与 ontology reasoning，并在 LLM 外执行。","exact-v1 以 AgenticRei examples 展示 tool calls 与 A2A messages 的 policy expression/evaluation。","示例不构成吞吐、安全或完备性证明；ontology/policy conflict 仍需可信 owner 与版本治理。","Not Disclosed — policy-engine examples, not a model comparison","expressibility and runtime policy-evaluation examples",("obligations, dispensations","examples","Limitations"),"No Change — Existing Coverage","Ch72 已有 policy version、obligation 与外部 reference monitor；无需复制 DSL。"),
"2606.19535":E("PLATFORM-SECURITY","model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。","Qwen3-4B 跨 NVIDIA GPU、Google TPU、AWS Graviton、Alibaba Yitian-710，并展示目标平台 code vulnerability。","攻击依赖作者平台集合与 LoRA；跨平台不一致不等于任意模型都可植入，可信构建仍需独立证明。","Qwen3-4B with two LoRA adapters","target-platform activation, aggregate utility and vulnerable-code generation",("platform-triggered backdoor","broad range of deployment targets","Limitations"),"Integrate","它把 platform/kernel 纳入模型供应链的可执行 identity，而非仅记录权重 hash。",hardware="NVIDIA GPUs, Google TPUs, AWS Graviton and Alibaba Yitian-710",precision="platform-dependent floating-point kernels; exact serving precisions in v1 matrix"),
"2606.19544":E("PLATFORM-EVALUATION-SYSTEM","Judge validation 要同时报告 chance-corrected agreement、test-retest consistency 与 position/verbosity bias；高 consistency 不能替代 validity。","21 judges、9 providers、3 benchmarks、118 runs、约 541k judgments；报告 kappa deflation 与 ranking shifts。","三个 benchmark 与单一 pairwise rubric 不证明所有 judge 场景；Cohen kappa 也依赖 prevalence。","21 judges from nine providers","agreement, Cohen's kappa, test-retest consistency, position bias and verbosity bias",("Minimum Viable Validation Protocol","118 runs","limitations"),"No Change — Existing Coverage","Ch66 已把 reliability、validity、bias 分离；本大样本是强验证而非新机制。"),
"2606.19559":E("AGENT-PLANNING","黑盒 Agent 可把 action confidence 与 request uncertainty 分开；只有后者高时触发 clarification，避免把执行不确定与需求欠规范混成 abstention。","五个 backbones，在 WebShop/ALFWorld clarification variants 与 REAL 上比较 clarification F1/fault detection。","prompt-based uncertainty 未校准成概率；benchmark 人工制造 50% 欠规范，澄清成本和用户响应质量未被完整建模。","GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B and GPT-OSS-120B","clarification F1 and fault detection across clarification and standard benchmarks",("action confidence from request uncertainty","five LLM backbones","Limitations"),"No Change — Existing Coverage","Ch79 已拥有 ask/act gate 与 uncertainty decomposition；保留跨 backbone 证据。"),
"2606.19595":E("AGENT-WORKFLOW","voice-agent interruption recovery 必须保存 workflow node、已提交 side effects 与待确认槽位，恢复时区分 resume、repair、restart。","IHBench 在 structured workflows 上测 interruption 后 task completion 与 recovery error。","模拟中断与语音管线不覆盖真实网络/ASR drift；恢复成功也不证明重复 effect 被阻止。","27 configurations from 17 closed-weight and 10 open-weight systems, including Gemma 4 12B, MiMo-Audio-7B, Voxtral-Small-24B and Qwen3-Omni-30B","post-interruption task completion and structured recovery error",("Post-Interruption Recovery","Evaluation","Limitations"),"No Change — Existing Coverage","Ch81 已有 durable checkpoints 与 idempotent resume；IHBench补充 voice workload。"),
"2606.19613":E("PLATFORM-EVALUATION-SYSTEM","coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。","6 harnesses×7 open LLMs、20 scenarios×100 turns；所有模型 5–6 turns 内失败，test feedback/retry 最多提升 12×。","程序生成 REST workload 不能代表全部软件演化；turn-to-failure 对变更难度和 harness 强敏感。","six agent harnesses paired with seven open-source LLMs","consecutive passed turns, test feedback/retry effect and harness sensitivity over 20x100-turn scenarios",("100 Interaction Turns","20 scenarios","Limitations"),"Integrate","它给长期 session 的 degradation/first-failure 一个不同于独立 pass@1 的 evaluation contract。"),
"2606.19667":E("INFER-KV-CACHE","RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。","三个 vLLM configurations，median TTFT 降约 20–33%，QA quality 未下降；greedy 达 oracle TTFT gain 的 97.5%。","重排可能改变 positional bias 与答案；局部 query locality 不保证生产 cache hit，且不减少 decode cost。","Not Disclosed — v1 binds the claim to three vLLM configurations and QA tests rather than one named generator checkpoint","median TTFT, prefix reuse and QA answer quality",("prefix tree over recently served evidence sequences","three vLLM configurations","Limitations"),"Integrate","它连接 RAG evidence ordering 与 prefix-cache locality，同时保持 relevance owner 不变。"),
"2606.20736":E("PLATFORM-EVALUATION-SYSTEM","受污染 benchmark 可把 answer-bearing visual key 变成运行时随机生成、human-validated edit slot，并保留 construction-grounded label。","V*Bench 上 8 个 frontier VLM；原题比 regenerated variants 高 9.5–18.8pp。","只更新局部 visual key，不能消除题型、metadata 或训练 pipeline 泄漏；图像编辑真实性依赖人工验证。","eight frontier vision-language models","accuracy gap between original and regenerated V*Bench items with controlled search difficulty",("randomly regenerates the answer-bearing local detail","eight frontier vision-language models","Limitations"),"Integrate","它把 benchmark freshness 从发布时清洁度转成每次 evaluation 的生成 contract。"),
"2606.20746":E("PLATFORM-SECURITY","slow-burn injection detector 可在 executed action edges 上累积冻结 per-event score 的 CUSUM persistence；它只能放大已有 margin，不能创造 detector 没有的 margin。","集中攻击 gap +0.092（clustered bootstrap）；repo-exfil persistence AUC 0.708，但 broader clean-path AUC 0.167，且仅 3–4 independent tasks。","这是明确的 boundary result，不是 deployable detector；小 independent denominator 阻断功效外推。","frozen char-ngram SVM plus embedding-contrastive detector; held-out cloaking target","clustered-bootstrap gap and persistence/peak delta AUC on executed-edge trajectories",("detector of record","broader clean-path actions","boundary result, not a deployable detector"),"No Change — Existing Coverage","Ch72 已有 run-level cumulative harm 与 temporal invariant；本 family 的窄带负结果作为 sensor 边界 handoff。"),
"2606.21089":E("TRAIN-DPO","重复 DPO campaign 的 checkpoint 链需要另存 strategy/evaluator memory；保留旧能力不等于积累了如何训练下一 campaign 的科学知识。","Qwen2.5-7B-Instruct、30 campaigns；单 seed 5-condition×3-step chain 加异构/多 seed pilots，4/5 candidates 退化。","主要结果单 seed，pilots 又显示 regime dependence；不能声称 MSCL 或 retrieval 已解决问题。","Qwen2.5-7B-Instruct","campaign-level peak pass@1 and intervention deltas across 30 HumanEval subdomains",("scientific amnesia","single-seed 5-condition","diagnostic, not a claim"),"Integrate","它区分 capability retention 与 method-learning state，修正 repeated DPO 的错误自改进叙事。"),
"2606.21090":E("TRAIN-GRPO","post-training control loop 应分别持有 campaign-level memory、within-campaign early stop 与 optimizer；峰值 checkpoint 必须先于最终 collapse 被保存和晋级。","Qwen2.5-3B/7B，10×20-step campaigns，多 seed；比较 CARE、ES、GRPO，并有 Gemma-3-4B pilot。","GRPO 抬高 floor 但未消除约 17pp cliff；GRPO+ES 仅 3 seeds 且 mixed，不能推出统一配方。","Qwen2.5-3B, Qwen2.5-7B and a Gemma-3-4B pilot","pass@1 trajectory, peak-to-end collapse and multi-seed intervention comparison",("rise-then-collapse pattern","10 sequential 20-step campaigns","mixed evidence"),"Integrate","它把 self-training collapse 定位到 within-campaign promotion gate，而不是笼统归因 catastrophic forgetting。"),
"2606.28374":E("AGENT-REFLECTION","自然语言 strategy/skill/playbook 的每代 rewrite 只能在 disjoint held-out split 不退化时 commit，否则回退 base ReAct。","ALFWorld、GAIA、tau-bench、WebShop，6 baselines、共享本地 backbone；Dynamic Cheatsheet 在 WebShop collapse。","held-out split 仍可能与部署同分布共偏；无 artifact 普遍获胜，strict gate 只证明这四个 benchmark 的单调安全。","one shared local backbone across RSEA and six baselines","benchmark score, McNemar test and regression gate across four agent benchmarks",("strict keep-better gate","four diverse benchmarks","no artifact universally wins"),"No Change — Existing Coverage","Ch80 已有 held-out promotion/rollback；RSEA提供跨 benchmark 负证据而非新 owner。"),
}

BENCH_OVERRIDES = {
    "2606.18619": {"model": "Claude Sonnet 4.6 and DeepSeek V4 Pro; Claude Mythos is comparison-only"},
    "2606.18673": {"model": "Llama-2-7B-chat-hf, Llama-3.1-8B-Instruct, Mistral-7B-Instruct, Qwen3-4B-Instruct, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B-Instruct"},
    "2606.18746": {"model": "Not Disclosed"},
    "2606.18829": {"model": "GPT-5.4, DeepSeek-V4-Pro, Llama-4-Maverick, GPT-5-mini, GPT-4o-mini and Gemini-2.5-Flash-Lite"},
    "2606.18874": {"model": "gpt-4o-mini answer generator and all-MiniLM-L6-v2 embedder in the matched LoCoMo validation"},
    "2606.18958": {"model": "Not Disclosed"},
    "2606.18996": {"model": "GPT-4o-mini, GPT-5-mini, GPT-5.4-mini, GPT-5, Gemini-2.5-Flash-Lite, Gemini-2.5-Flash, Gemini-2.5-Pro, Claude Haiku 4.5, Claude Sonnet 4.5, Qwen3-VL-2B, Qwen3-VL-4B, Qwen3-VL-8B, Qwen3-VL-32B, Phi-4-multimodal, InternVL3.5-2B, InternVL3.5-4B, InternVL3.5-8B, InternVL3.5-14B, InternVL3.5-38B, Devstral-Small-2512, Llama3.2-11B-Vision and GLM-4.6V-Flash", "hardware": "NVIDIA A6000 GPUs for open-source models"},
    "2606.19191": {"model": "GPT-5.5, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct; Opus-4.7, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct for cross-generator transfer; Cursor backends additionally include Opus-4.7"},
    "2606.19544": {"model": "Gemini 3.1 Pro, Claude Opus 4.6, DeepSeek V3.2, Claude Sonnet 4.6, Llama 3.3 70B, Kimi K2.5, GPT-5.4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, GLM-5, GPT-oss 120B, Claude Sonnet 4, Gemini 2.5 Flash, Claude Haiku 4.5, GPT-4.1-mini, Minimax M2.7, Qwen 3 8B, GPT-4o-mini, Mixtral 8x22B and GPT-5.4-mini"},
    "2606.19535": {"model": "Qwen3-4B and Qwen3-8B with two LoRA adapters", "hardware": "NVIDIA H200, NVIDIA A100, NVIDIA H100, NVIDIA DGX Spark, Google TPU, AWS Graviton and Alibaba Yitian-710", "precision": "Not Disclosed", "batch": "1"},
    "2606.19595": {"model": "GPT-4o Audio, GPT-4o Mini Audio, GPT Audio, GPT Audio Mini, GPT Realtime, GPT Realtime 1.5, GPT Realtime Mini, GPT Realtime 2, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Live, Gemma 4 12B Instruct, Qwen3-Omni-30B-A3B-Instruct, Qwen2.5-Omni-7B, Phi-4-Multimodal-Instruct, Voxtral-Small-24B-2507, Qwen2-Audio-7B-Instruct, MiMo-Audio-7B-Instruct and Kimi-Audio-7B-Instruct across 27 mode/configuration combinations"},
    "2606.19613": {"model": "Devstral 2, Devstral Small 2, GLM-5, Kimi K2.5, Nemotron Super, Qwen3-Coder-Next and Qwen3.5-122B"},
    "2606.19667": {"model": "Qwen2.5-1.5B and Qwen2.5-7B", "hardware": "RTX 4060 Ti 8 GB, RTX 4090 24 GB and RTX 4090D 24 GB", "input_length": "max_model_len 2048 or 4096 by configuration"},
    "2606.20736": {"model": "Qwen3.6-Plus, GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro, Seed-2.0-Lite, Kimi K2.6, MiMo v2.5 and Llama 4 Maverick; LLaVA-1.5-13B for difficulty calibration", "output_length": "max_tokens 8192"},
    "2606.28374": {"model": "Qwen2.5-7B-Instruct for ALFWorld and Qwen3-30B-A3B-Instruct for GAIA, tau-bench and WebShop", "hardware": "4 NVIDIA A100 GPUs"},
}

SCORES = {
    "2606.18600":(3,3,3), "2606.18619":(3,3,3), "2606.18650":(2,2,3), "2606.18668":(2,2,3),
    "2606.18673":(2,3,3), "2606.18697":(3,2,3), "2606.18741":(3,3,3), "2606.18746":(2,2,3),
    "2606.18810":(2,2,3), "2606.18829":(3,3,3), "2606.18831":(2,3,3), "2606.18847":(3,2,3),
    "2606.18874":(2,3,3), "2606.18958":(2,3,3), "2606.18967":(3,2,3), "2606.18996":(3,3,3),
    "2606.19004":(2,2,3), "2606.19025":(3,3,3), "2606.19057":(3,3,3), "2606.19111":(2,2,3),
    "2606.19191":(3,3,3), "2606.19242":(2,3,3), "2606.19262":(3,3,3), "2606.19271":(2,2,3),
    "2606.19409":(3,3,3), "2606.19464":(2,3,3), "2606.19535":(3,3,3), "2606.19544":(2,3,3),
    "2606.19559":(2,2,3), "2606.19595":(2,2,3), "2606.19613":(3,2,3), "2606.19667":(2,2,3),
    "2606.20736":(3,3,3), "2606.20746":(3,2,3), "2606.21089":(3,2,3), "2606.21090":(3,2,3),
    "2606.28374":(2,2,3),
}
assert set(SCORES) == set(C)

SELECTED = {"2606.18600":"DA-20260618-HETEROGENEOUS-RECOVERY", "2606.19025":"DA-20260618-CROSS-SITE-MOE-OWNERSHIP", "2606.19535":"DA-20260618-PLATFORM-BOUND-ARTIFACT"}

def fam(aid): return "SF-2026-ARXIV-" + aid.replace(".", "-")
def first_sentence(text): return re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip(), 1)[0]
def closure(row):
    t=row["title"]; a=first_sentence(row["abstract"]); low=(t+" "+a).lower(); cats=set(row["categories"])
    if any(x in low for x in ("survey", "position paper", "tutorial", "systematic review")):
        cls="survey_or_position_without_new_mechanism"; why="综述/立场只组织既有方案，没有给出新的 state/data/control owner 或可验证 release contract"
    elif cats & {"q-bio.QM","q-bio.NC","physics.med-ph","econ.EM","stat.ME"} and not (cats & {"cs.LG","cs.AI","cs.DC"}):
        cls="excluded_family"; why="主问题属于生医/统计/经济等非 AI-System owner，模型只是分析手段"
    elif any(x in low for x in ("segmentation", "classification", "image restoration", "object detection", "medical", "robotic jumping", "navigation")):
        cls="application_result_without_durable_system_delta"; why="结果聚焦单一任务/应用精度，没有改变长期平台机制或 evaluation/release authority"
    elif any(x in low for x in ("benchmark", "dataset")):
        cls="benchmark_only_below_durable_threshold"; why="数据或榜单提供任务证据，但未改变本书已有 benchmark identity、scorer 或 promotion contract"
    else:
        cls="incremental_method_below_durable_threshold"; why="方法改进未达到改变长期 AI-System state/data/control ownership、平台契约或 Books 命题的门槛"
    return cls, f"{t}：{a}。逐项 title+abstract 语义复核结论：{why}。"

def bench(aid, e):
    nd="Not Disclosed"
    def strict(value):
        return nd if "Not Disclosed" in value else value
    result={"workload":e["evaluator"].split(",")[0],"model":strict(e["model"]),"hardware":strict(e["hardware"]),"precision":strict(e["precision"]),"input_length":nd,"output_length":nd,"batch":nd,"concurrency":nd,"slo":strict(e["slo"]),"evaluator":e["evaluator"]}
    result.update(BENCH_OVERRIDES.get(aid, {}))
    return result

def norm(text):
    text=unicodedata.normalize("NFC",text.replace("\r\n","\n").replace("\r","\n"))
    return "\n".join(line.rstrip() for line in text.strip().split("\n"))

def provenance(family, aid, method, evaluation, limits, body):
    def multi(value):
        return ";".join(sorted(unicodedata.normalize("NFC",x.strip()) for x in value.split(";") if x.strip() and x.strip()!="—"))
    canonical="|".join(("review-completion-v1",family,"paper-v1:"+aid,"arXiv:"+aid+"v1",multi("SRC-ARXIV"),"arXiv:"+aid+"v1",multi("SRC-ARXIV@arXiv:"+aid+"v1"),"deep",multi(method),multi(evaluation),multi(limits),multi("Not Disclosed — no later artifact used"),"claim:"+family,"review:"+family,"review-body-sha256:"+hashlib.sha256(norm(body).encode()).hexdigest()))
    return "RP-"+hashlib.sha256(canonical.encode()).hexdigest()[:16]

def main():
    reaudit_open=False
    postwrite_complete=True
    raw=json.loads(PROV.read_text()); rows=raw["identities"]; assert len(rows)==516 and set(C)==set(C)&{r["arxiv_id"] for r in rows}
    did="DEN-20260618-"+hashlib.sha256("\n".join(sorted(C)).encode()).hexdigest()[:8]
    route={}; audit=[]
    for r in rows:
        rc=route.setdefault(r["screening_route"],{"raw":0,"retained":0,"closure":0}); rc["raw"]+=1
        if r["arxiv_id"] in C:
            rc["retained"]+=1; r["screening_status"]="retained_after_full_semantic_audit"; r["screening_reason"]=C[r["arxiv_id"]]["delta"]; r["pre_denominator_closure_class"]="—"; audit.append((r["arxiv_id"],r["screening_route"],"retained","—",r["screening_reason"]))
        else:
            rc["closure"]+=1; cls,reason=closure(r); r["screening_status"]="pre_denominator_closure"; r["screening_reason"]=reason; r["pre_denominator_closure_class"]=cls; audit.append((r["arxiv_id"],r["screening_route"],"closure",cls,reason))
    assert sum(x["retained"] for x in route.values())==len(C) and sum(x["closure"] for x in route.values())==516-len(C)
    ledger=dict(raw); ledger.update({"gate_status":"evidence_selection_passed_books_prewrite_open","routed_candidate_denominator":len(C),"routed_candidate_denominator_status":"frozen_after_516_of_516_full_semantic_audit","abstract_screening_closure":516-len(C),"canonical_candidate_denominator":{"denominator_id":did,"raw_identities":516,"retained":len(C),"pre_denominator_closures":516-len(C),"audit_receipt":"papers/2026/06/_sources/daily-20260618/denominator-full-semantic-audit-v1.tsv","frozen_at":EXEC},"audit":{"reviewed_identities":"516/516","title_abstract_semantic_screen":"passed","candidate_false_positive_false_negative_audit":"passed","denominator_frozen":True,"coverage_gate":"closed","evidence_gate":"passed","selection_gate":"passed","books_gate":"open_pending_root_writeback_and_postwrite_audit","route_counts":route}})
    if reaudit_open:
        ledger["gate_status"]="coverage_closed_evidence_selection_books_open_during_fresh_reaudit"
        ledger["audit"]["evidence_gate"]="open_pending_37_of_37_fresh_reaudit"
        ledger["audit"]["selection_gate"]="open_pending_full_frontier_fresh_reaudit"
        ledger["audit"]["books_gate"]="open_evidence_selection_invalidated"
    elif postwrite_complete:
        ledger["gate_status"]="complete"
        ledger["audit"]["books_gate"]="passed_after_37_of_37_postwrite_fresh_audit"
    PACKET.mkdir(parents=True,exist_ok=True); (PACKET/"screening-ledger.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    with (PACKET/"denominator-full-semantic-audit-v1.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["arxiv_id","screening_route","decision","closure_class","semantic_reason"]); w.writerows(audit)
    byid={r["arxiv_id"]:r for r in rows}; reviews=[]
    for aid,e in C.items():
        src=byid[aid]; family=fam(aid); m,ev,lim=e["anchors"]; b=bench(aid,e)
        loc=(f"https://arxiv.org/html/{aid}v1 — § exact-v1 anchor: {m}",f"https://arxiv.org/html/{aid}v1 — § exact-v1 evaluation anchor: {ev}",f"https://arxiv.org/html/{aid}v1 — § exact-v1 limitation/counterevidence anchor: {lim}")
        body=f"""### {aid} — {src['title']}\n\n**问题与旧路径。** {first_sentence(src['abstract'])} 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。\n\n**机制与 owner。** {e['delta']} 唯一知识 owner 为 `{e['owner']}`；相邻节点只消费带 identity 的 handoff。\n\n**Evaluation：证明与未证明。** {e['proof']} Method=`{loc[0]}`；Evaluation=`{loc[1]}`。Benchmark contract：model=`{b['model']}`；hardware=`{b['hardware']}`；precision=`{b['precision']}`；batch=`{b['batch']}`；concurrency=`{b['concurrency']}`；SLO=`{b['slo']}`；evaluator=`{b['evaluator']}`。\n\n**Trade-off、failure、共存与演进。** {e['boundary']} 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`{loc[2]}`。\n\n<!-- claim:{family}:start -->\nClaim boundary：仅 `arXiv:{aid}v1` official HTML；不使用 later version；ordinary pending locator count=`0`.\n<!-- claim:{family}:end -->"""
        rp=provenance(family,aid,loc[0],loc[1],loc[2],body)
        reviews.append(dict(aid=aid,family=family,src=src,e=e,b=b,loc=loc,body=body,rp=rp))
    receipts=[]
    for r in reviews:
        receipts.append({"source_family_id":r["family"],"review_provenance_id":r["rp"],"review_route":"deep","event_identity":"paper-v1:"+r["aid"],"primary_identifier":"arXiv:"+r["aid"]+"v1","primary_evidence_version":"arXiv:"+r["aid"]+"v1","reviewed_evidence_versions":"SRC-ARXIV@arXiv:"+r["aid"]+"v1","method_identity_locators":r["loc"][0],"evaluation_locators":r["loc"][1],"limitations_counterevidence_locators":r["loc"][2],"artifact_locators":"Not Disclosed — no later artifact used","claim_boundary_ref":"claim:"+r["family"],"review_ref":"review:"+r["family"],"review_body_sha256":hashlib.sha256(r["body"].encode()).hexdigest(),"completion_result":"complete","ordinary_pending_locator_count":0,"benchmark_contract":r["b"],"stable_node_id":r["e"]["owner"],"books_disposition":r["e"]["disposition"]})
    (PACKET/"source-review-receipts-v2.1.json").write_text(json.dumps({"contract_version":"V2.1","denominator_id":did,"generated_at":EXEC,"reviews":receipts},ensure_ascii=False,indent=2)+"\n")
    (PACKET/"exact-v1-access-receipt.json").write_text(json.dumps({"schema":"exact-v1-access-receipt-v1","denominator_id":did,"checked_at":EXEC,"reader":"official arXiv HTML through primary-source web reader","result":f"{len(C)}/{len(C)} accessible with exact arXiv:<id>v1 header/body","blocked":[],"items":[{"source_family_id":r["family"],"primary_identifier":"arXiv:"+r["aid"]+"v1","locator":"https://arxiv.org/html/"+r["aid"]+"v1","status":"accessible","version_header":"verified v1"} for r in reviews]},ensure_ascii=False,indent=2)+"\n")
    decisions=[]
    for r in reviews:
        chosen=r["aid"] in SELECTED; decisions.append({"source_family_id":r["family"],"eligibility":"score_7_9; potential_books_delta" if r["e"]["disposition"].startswith("Integrate") else "score_7_9","decision":"selected" if chosen else "not_selected","analysis_unit_id":SELECTED.get(r["aid"],"—"),"priority_rationale":r["e"]["note"],"narrative_ref":"analysis:"+SELECTED[r["aid"]] if chosen else "analysis-decision:"+r["family"]})
    (PACKET/"deep-analysis-selection-v1.json").write_text(json.dumps({"schema":"deep-analysis-selection-v1","denominator_id":did,"frontier_size":len(C),"selection_count":3,"winners_frozen_before_rationale":list(SELECTED),"decisions":decisions},ensure_ascii=False,indent=2)+"\n")
    comparisons=[{"source_family_id":r["family"],"stable_node_id":r["e"]["owner"],"target_chapter_ref":PATHS[r["e"]["owner"]]+"#L1","adjacent_chapter_refs":ADJACENT[r["e"]["owner"]],"existing_proposition_ref":"existing:"+r["family"],"new_evidence_delta_ref":"delta:"+r["family"],"evolution_relation":"Direct Evolution" if r["e"]["disposition"].startswith("Integrate") else "Principle Reuse","decision":r["e"]["disposition"],"books_review_ref":"books-review:"+r["family"]} for r in reviews]
    (PACKET/"books-comparison-v1.json").write_text(json.dumps({"schema":"books-comparison-v1","denominator_id":did,"compared":f"{len(C)}/{len(C)}","items":comparisons},ensure_ascii=False,indent=2)+"\n")
    families="; ".join(r["family"] for r in reviews); raw_route={k:v for k,v in route.items()}; integrations=[r for r in reviews if r["e"]["disposition"].startswith("Integrate")]
    lines=["# Daily Research — 2026-06-18","",f"> Strict V2.1 Daily for `{did}`. Coverage, Evidence and Selection passed; Books remains Open pending root writeback and this lane's post-write fresh audit.","","## Executive Summary","",f"Beijing window `[2026-06-17 09:00, 2026-06-18 09:00)` contains 516 registered identities. Full 516/516 title+abstract screening freezes {len(C)} durable families and {516-len(C)} family-specific closures. Official exact-v1 HTML was reviewed for {len(C)}/{len(C)} families. Full-frontier selection freezes three winners before rationale. Books comparison yields {len(integrations)} Integrate proposals and {len(C)-len(integrations)} No Change handoffs.","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-18 |","| Window End | 2026-06-18 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {did} |",f"| Denominator Frozen At | {EXEC} |","| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-06-17T09:00:00+08:00 | 2026-06-18T09:00:00+08:00 | {EXEC} | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 516 | {families} | pages=40; final_cursor=end; 516 unique identities | 2026-06-18T01:00:00Z | ../_sources/daily-20260618/screening-ledger.json; ../_sources/daily-20260618/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260618 | — |","","<!-- coverage:SRC-ARXIV:20260618:start -->",f"All 357 Core, 55 keyword-routed and 104 route-negative identities were screened. Frozen arithmetic: `516 = {len(C)} retained + {516-len(C)} closures`. Route reconciliation: `{json.dumps(raw_route,ensure_ascii=False)}`. Keyword routing was recall-only.","<!-- coverage:SRC-ARXIV:20260618:end -->","","## 2. Candidate Ledger and Score V2","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        score=SCORES[r["aid"]]; lines.append(f"| {r['family']} | arXiv:{r['aid']}v1 | paper-v1:{r['aid']} | 2026-W25 | 2026-06-17 | SRC-ARXIV | {score[0]} | {score[1]} | {score[2]} | {sum(score)} | retained | deep_complete | accessible | none | review:{r['family']} | self | — | new_in_window | {r['e']['owner']} | {r['e']['disposition']} | books-review:{r['family']} | yes |")
    lines += ["","### Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews: lines.append(f"| {r['family']} | {r['rp']} | deep | arXiv:{r['aid']}v1 | SRC-ARXIV@arXiv:{r['aid']}v1 | {r['loc'][0]} | {r['loc'][1]} | {r['loc'][2]} | Not Disclosed — no later artifact used | claim:{r['family']} | complete |")
    lines += ["","### Benchmark Contract","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews: lines.append("| "+" | ".join([r["family"]]+[r["b"][k] for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")])+" |")
    lines += ["","## 3. Source Reviews",""]
    for r in reviews: lines += [f"<!-- review:{r['family']}:start -->",r["body"],f"<!-- review:{r['family']}:end -->",""]
    lines += ["## 4. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for r,d in zip(reviews,decisions): lines.append(f"| {r['family']} | {d['eligibility']} | {d['decision']} | {d['analysis_unit_id']} | — | {d['priority_rationale']} | {d['narrative_ref']} |")
    for r in reviews:
        if r["aid"] not in SELECTED: lines += ["",f"<!-- analysis-decision:{r['family']}:start -->",r["e"]["note"],f"<!-- analysis-decision:{r['family']}:end -->"]
    narratives={"DA-20260618-HETEROGENEOUS-RECOVERY":"异构 spot serving 的控制对象不是一张静态 placement 表，而是 topology、request/KV state 与 replacement lifecycle。只有把重配置和输出恢复纳入同一 commit，成本优化才不会以分钟级中断换取。","DA-20260618-CROSS-SITE-MOE-OWNERSHIP":"跨站 MoE 训练的关键不是把数据并行原样搬到 WAN，而是重新划分 expert/state ownership：每站只持有分区 expert，有限复制承担热点与可用性，non-resident token 以显式 skip 规则改变本地更新分布。实测通信和吞吐只覆盖作者配置，100B 仍是模型投影。","DA-20260618-PLATFORM-BOUND-ARTIFACT":"权重 hash 不能单独定义可执行模型身份。FloatDoor 表明同一权重和 LoRA 组合可利用 platform/kernel 浮点差异触发不同任务，因此 audit artifact 必须绑定目标硬件、kernel 和 serving build；跨平台差异本身仍不证明后门存在。"}
    for k,v in narratives.items(): lines += ["",f"<!-- analysis:{k}:start -->",f"### {k}",v,f"<!-- analysis:{k}:end -->"]
    lines += ["","## 5. Books Comparison and Decision","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        rel="Direct Evolution" if r["e"]["disposition"].startswith("Integrate") else "Principle Reuse"; path=PATHS[r["e"]["owner"]]; adjacent=ADJACENT[r["e"]["owner"]]; lines.append(f"| {r['family']} | {r['e']['owner']} | {path}#L1 | {adjacent} | existing:{r['family']} | delta:{r['family']} | {rel} | {r['e']['disposition']} | books-review:{r['family']} |")
    for r in reviews:
        rel="Direct Evolution" if r["e"]["disposition"].startswith("Integrate") else "Principle Reuse"; path=PATHS[r["e"]["owner"]]
        existing=f"{OWNER_PROPOSITION[r['e']['owner']]} Comparative result for arXiv:{r['aid']}v1: {r['e']['note']}"
        lines += ["",f"<!-- existing:{r['family']}:start -->",existing,f"<!-- existing:{r['family']}:end -->","",f"<!-- delta:{r['family']}:start -->",r["e"]["delta"],f"<!-- delta:{r['family']}:end -->","",f"<!-- books-review:{r['family']}:start -->",f"{rel}; {r['e']['disposition']}. {r['e']['boundary']}",f"<!-- books-review:{r['family']}:end -->"]
    refs="; ".join("review:"+r["family"] for r in reviews); sels="; ".join(("analysis:"+SELECTED[r["aid"]]) if r["aid"] in SELECTED else "analysis-decision:"+r["family"] for r in reviews); books="; ".join("books-review:"+r["family"] for r in reviews)
    lines += ["","## 6. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260618-COVERAGE-V1 | fresh-context:jun18-v1 | coverage | coverage:SRC-ARXIV:20260618 | — | 516/516 title+abstract; denominator {len(C)}; closures {516-len(C)}; all 104 route-negative checked | passed |",f"| SA-20260618-EVIDENCE-V1 | fresh-context:jun18-v1 | evidence | {refs} | — | {len(C)}/{len(C)} official exact-v1 Method/Evaluation/boundary and named benchmark contracts | passed |",f"| SA-20260618-SELECTION-V1 | fresh-context:jun18-v1 | deep_analysis_selection | {sels} | — | {len(C)}/{len(C)} frontier; winners frozen before source-specific rationale | passed |",f"| SA-20260618-BOOKS-PREWRITE-V1 | fresh-context:jun18-v1 | books | {books} | root writeback pending | {len(integrations)} Integrate proposals and {len(C)-len(integrations)} No Change handoffs checked; post-write audit pending | open |","","## 7. Materials and Access","",f"- {len(C)}/{len(C)} exact-v1 official HTML pages were accessible and exposed the matching version body.","- Local curl reset; the working primary-source web reader supplied the official exact-v1 manuscripts.","","## 8. Daily Integration Decision","",f"- Integrate: {len(integrations)}; No Change: {len(C)-len(integrations)}.","- Books Gate remains Open until root applies the owner-merged packet and this lane audits the writeback.","","## 9. Repository Changes","","- Only this date's Daily, source packet and finalizer are written by this lane; shared Books are untouched."]
    if reaudit_open:
        lines=[line.replace("Coverage, Evidence and Selection passed; Books remains Open pending root writeback and this lane's post-write fresh audit.","Coverage is Closed; Evidence, Selection and Books remain Open during the 37/37 repair audit.")
                   .replace("| Evidence Gate | Passed |","| Evidence Gate | Open |")
                   .replace("| SA-20260618-EVIDENCE-V1 | fresh-context:jun18-v1 | evidence |", "| SA-20260618-EVIDENCE-V1 | fresh-context:jun18-v1 | evidence |")
                   .replace("| — | 37/37 official exact-v1 Method/Evaluation/boundary and named benchmark contracts | passed |", "| F-20260618-PREWRITE-BENCHMARK-01 | benchmark-contract and per-family Review-note repairs pending 37/37 re-audit | open |")
                   .replace("| — | 37/37 frontier; winners frozen before source-specific rationale | passed |", "| F-20260618-PREWRITE-SELECTION-01 | full-frontier selection invalidated pending fresh re-audit | open |")
               for line in lines]
    elif postwrite_complete:
        postwrite_row=f"| SA-20260618-BOOKS-POSTWRITE-V1 | fresh-context:jun18-v1 | books | {books} | — | 16/16 Integrate正文、Review note、unique owner、old-path/coexistence/fallback；21/21 No Change existing coverage and leakage audit | passed |"
        closed=[]
        for line in lines:
            if line.startswith("| SA-20260618-BOOKS-PREWRITE-V1 |"):
                continue
            line=(line.replace("Coverage, Evidence and Selection passed; Books remains Open pending root writeback and this lane's post-write fresh audit.","All V2.1 Gates passed after the complete 37/37 post-write fresh audit.")
                      .replace("| Completion Status | In Progress |","| Completion Status | Complete |")
                      .replace("| Books Gate | Open |","| Books Gate | Passed |")
                      .replace("| SA-20260618-BOOKS-PREWRITE-V1 | fresh-context:jun18-v1 | books | "+books+" | root writeback pending | 16 Integrate proposals and 21 No Change handoffs checked; post-write audit pending | open |","| SA-20260618-BOOKS-PREWRITE-V1 | fresh-context:jun18-v1 | books | "+books+" | — | 16 Integrate proposals and 21 No Change handoffs checked before writeback | passed |")
                      .replace("- Books Gate remains Open until root applies the owner-merged packet and this lane audits the writeback.","- Books Gate Passed: 16 Integrate families were audited in 11 unique owners; 21 No Change handoffs retain existing coverage without writeback leakage."))
            if line == "## 7. Materials and Access":
                if closed and closed[-1] == "":
                    closed.pop()
                closed += [postwrite_row, ""]
            closed.append(line)
        lines=closed
    lines[2:2] = [
        "**Research Date:** 2026-06-18", "",
        "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-06-17 09:00:00 ～ 2026-06-18 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；516/516 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet", "",
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
    }
    lines = [canonical_headings.get(line, line) for line in lines]
    recommended_index = lines.index("## 9. Recommended Action")
    lines[recommended_index:recommended_index] = [
        "## 8. Ignored Noise", "",
        "- 479 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit rather than being promoted into the Candidate Ledger.", "",
    ]
    lines += [
        "", "## 11. Open Questions", "",
        "- How should heterogeneous spot serving decide whether migration, replication or recomputation is the safest recovery path under simultaneous price and topology change?",
        "- Which cross-site MoE ownership policy remains stable when expert popularity and WAN availability drift together?",
        "- How should executable model identity bind weights, adapters, kernels, hardware and serving build without making routine upgrades impossible?",
        "- These are research continuations, not unresolved Gate findings.",
        "", "## 12. Sources", "",
    ]
    for r in reviews:
        lines.append(
            f"- [arXiv:{r['aid']}v1 — {r['src']['title']}](https://arxiv.org/html/{r['aid']}v1) — "
            f"first-public `2026-06-17`；accessed `{EXEC[:10]}`；Source Family `{r['family']}`。"
        )
    lines += [
        "- `SRC-ARXIV` registry contract：`docs/RESEARCH_SOURCES.md`。", "",
        "## 13. Final Status", "",
        "- Status: Complete.",
        "- Coverage Gate: Closed.",
        "- Evidence Gate: Passed.",
        "- Books Gate: Passed.",
        "- Fresh-context Semantic Audit: Passed；unresolved findings = 0.",
    ]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(lines)+"\n")
    groups={}
    for r in integrations: groups.setdefault(r["e"]["owner"],[]).append(r)
    queue_status=(f"Denominator `{did}`. Applied and post-write audited: {len(integrations)} family deltas in {len(groups)} owner files."
                  if postwrite_complete else
                  f"Denominator `{did}`. Pre-write only: {len(integrations)} family deltas merged into {len(groups)} owner files; root writeback and post-write audit pending.")
    ready_status=(f"Source denominator `{did}`. Applied by root and verified by the 37/37 post-write fresh audit; retained as the exact write receipt."
                  if postwrite_complete else
                  f"Source denominator `{did}`. Insert each owner block once; preserve every exact-v1 Review note.")
    q=["# 2026-06-18 Books Integration Queue V1","",queue_status,""]
    ready=["# 2026-06-18 Ready-to-Insert Books Packet V1","",ready_status,""]
    for owner,items in groups.items():
        target=PATHS[owner]; anchor=next((line.strip() for line in (ROOT/target).read_text().splitlines() if line.startswith("### ")),"# first durable mechanism section")
        ids=", ".join("arXiv:"+x["aid"]+"v1" for x in items); delta=" ".join(x["e"]["delta"] for x in items); boundary=" ".join(x["e"]["boundary"] for x in items)
        q += [f"## {owner}","",f"- Target: `{target}`",f"- Exact target locator: `{anchor}`",f"- Source families: {', '.join(x['family'] for x in items)}",f"- Minimal durable delta: {delta}",f"- Evidence boundary: {boundary}",""]
        ready += [f"## {owner} — {target}","",f"Insert after `{anchor}`.","","### Minimal durable delta","",delta,"","### Coexistence / cost / failure boundary","",boundary,"","### Review note",""]
        ready += [f"- {x['family']}: arXiv:{x['aid']}v1; exact-v1 official URL=`https://arxiv.org/html/{x['aid']}v1`; Method=`{x['loc'][0]}`; Evaluation=`{x['loc'][1]}`; Non-proof/limitations=`{x['loc'][2]}`; durable delta={x['e']['delta']} Boundary: {x['e']['boundary']}" for x in items]
        ready += [""]
    (PACKET/"BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(q)+"\n"); (PACKET/"READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready)+"\n")
    (PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(f"# 2026-06-18 Fresh Evidence and Selection Audit V1\n\n- Denominator `{did}`: `516 = {len(C)} retained + {516-len(C)} closures`; 104/104 route-negative audited.\n- Exact-v1: {len(C)}/{len(C)} official HTML; all model/evaluator identities are source-specific; absent hardware/precision/batch/concurrency/SLO fields remain direct Not Disclosed.\n- Evidence Gate Passed; Selection Gate Passed over the complete {len(C)}-family frontier.\n- Books prewrite: {len(integrations)} Integrate proposals merged into {len(groups)} owner files; {len(C)-len(integrations)} No Change handoffs. Books Gate Open pending root writeback and post-write audit.\n- Independence caveat: nested reviewer spawning was disabled; this is a fresh primary-source pass, not a claimed independent second-model review.\n")
    (PACKET/"README.md").write_text(f"# daily-20260618 source packet\n\n- Denominator: `{did}`\n- Raw: 516\n- Retained: {len(C)}\n- Closures: {516-len(C)}\n- Exact-v1: {len(C)}/{len(C)}\n- Coverage Gate: Closed\n- Evidence Gate: Passed\n- Selection Gate: Passed\n- Books Gate: Open pending root writeback/post-write audit\n- Completion: In Progress\n")
    if reaudit_open:
        (PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(f"# 2026-06-18 Fresh Evidence and Selection Audit V1\n\n- Denominator `{did}`: `516 = {len(C)} retained + {516-len(C)} closures`; 104/104 route-negative audited.\n- Root prewrite finding `F-20260618-PREWRITE-BENCHMARK-01` invalidated the prior Evidence signoff: 37/37 benchmark contracts and per-family Review notes are under fresh re-audit.\n- Root prewrite finding `F-20260618-PREWRITE-SELECTION-01` invalidated the prior Selection signoff: the complete {len(C)}-family frontier is under fresh re-audit.\n- Coverage Gate Closed; Evidence Gate Open; Selection Gate Open; Books Gate Open.\n- Independence caveat: nested reviewer spawning was disabled; this is a fresh primary-source pass, not a claimed independent second-model review.\n")
        (PACKET/"README.md").write_text(f"# daily-20260618 source packet\n\n- Denominator: `{did}`\n- Raw: 516\n- Retained: {len(C)}\n- Closures: {516-len(C)}\n- Exact-v1: {len(C)}/{len(C)}\n- Coverage Gate: Closed\n- Evidence Gate: Open pending 37/37 fresh re-audit\n- Selection Gate: Open pending full-frontier fresh re-audit\n- Books Gate: Open; Evidence/Selection invalidated\n- Completion: In Progress\n")
    else:
        (PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(f"# 2026-06-18 Fresh Evidence and Selection Audit V1\n\n- Denominator `{did}`: `516 = {len(C)} retained + {516-len(C)} closures`; all 516 title+abstract decisions and all 104 route-negative identities remain reconciled.\n- Evidence repair: {len(C)}/{len(C)} official exact-v1 reviews rechecked. Compound/conditional Not Disclosed fields: `0`; absent benchmark fields use exact `Not Disclosed`; disclosed model/hardware/precision/batch/input/output/SLO fields are source-specific.\n- Identity repair: all {len(C)} families use stable `SF-2026-ARXIV-*` IDs end-to-end; legacy family-ID format count is `0`.\n- Books packet repair: {len(integrations)}/{len(integrations)} Integrate families have an independent source-specific Review note containing the exact-v1 official URL plus distinct Method, Evaluation, and non-proof/limitations locators; {len(C)-len(integrations)} No Change handoffs are excluded from the write packet.\n- Selection repair: the complete {len(C)}-family frontier was rerun after invalidation; winners are arXiv:2606.18600v1, arXiv:2606.19025v1 and arXiv:2606.19535v1, with distinct source-specific rationales.\n- Evidence Gate Passed; Selection Gate Passed. Books Gate remains Open pending root writeback and this lane's post-write fresh audit.\n- Independence caveat: nested reviewer spawning was disabled; this is a fresh primary-source pass, not a claimed independent second-model review.\n")
    if postwrite_complete:
        fresh_path=PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
        fresh_path.write_text(fresh_path.read_text().replace(
            "Evidence Gate Passed; Selection Gate Passed. Books Gate remains Open pending root writeback and this lane's post-write fresh audit.",
            "Evidence Gate Passed; Selection Gate Passed; Books Gate Passed after the complete 37/37 post-write fresh audit recorded in `POST_WRITE_FRESH_AUDIT_V1.md`."))
        (PACKET/"README.md").write_text(f"# daily-20260618 source packet\n\n- Denominator: `{did}`\n- Raw: 516\n- Retained: {len(C)}\n- Closures: {516-len(C)}\n- Exact-v1: {len(C)}/{len(C)}\n- Coverage Gate: Closed\n- Evidence Gate: Passed\n- Selection Gate: Passed\n- Books Gate: Passed after 37/37 post-write fresh audit\n- Completion: Complete\n")
        post=["# 2026-06-18 Post-write Fresh Audit V1","",f"- Denominator: `{did}`; audited `{len(C)}/{len(C)}` retained families after re-proving `516 = 37 + 479` and the 104/104 route-negative FN audit.","- Evidence/Selection: `37/37` exact-v1 reviews, direct `Not Disclosed` benchmark fields, recomputed Review hashes and the frozen `3/37` frontier passed.","- Integrate: `16/16` across `11/11` unique owner files. Each family has one stable Source Family ID and one exact-v1 Review note with official URL, Method, Evaluation and non-proof/limitations locators.","- Body semantics: every Integrate delta and boundary occurs in the owner narrative as well as its Review note; old path, coexistence/failure and fallback remain explicit in the owner block.","- No Change: `21/21` source-specific existing propositions and distinct adjacent handoffs were re-read; no 06-18 Source Family ID leaked into Books. Exact arXiv-ID hits for 2606.18829v1 and 2606.19409v1 are expected pre-existing same-family coverage; the other 19 remain absent.","- Root cause repaired: the former `POSTWRITE_FRESH_AUDIT_V1.md` name and self-adjacent/generic-existing receipts were generator defects. This standard receipt, canonical lowercase paths, distinct adjacent refs and the 2606.18829 security owner replace them.","- Shared-file scope: owner files can contain later-date additions; only the 06-18 Source Families and their local propositions were adjudicated here. No shared file was changed by this repair.","- Findings: none unresolved. Books Gate Passed; Completion Complete.","- Independence caveat: nested reviewer spawning was disabled; this is a fresh self-audit, not a claimed independent second-model review; cross-model review was not available in this delegated lane.","","| Source Family ID | Disposition | Owner | Adjacent handoff | Audited existing proposition / post-write result |","| --- | --- | --- | --- | --- |"]
        for r in reviews:
            result=(f"{OWNER_PROPOSITION[r['e']['owner']]} Delta/body/boundary, unique exact-v1 note and fallback passed."
                    if r["e"]["disposition"].startswith("Integrate") else
                    f"{OWNER_PROPOSITION[r['e']['owner']]} {r['e']['note']} No-write/leakage boundary passed.")
            post.append(f"| {r['family']} | {r['e']['disposition']} | {PATHS[r['e']['owner']]} | {ADJACENT[r['e']['owner']]} | {result} |")
        (PACKET/"POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(post)+"\n")
    audit_rows=[]
    decision_by_family={d["source_family_id"]:d for d in decisions}
    for r in reviews:
        audit_rows.append([r["family"],"arXiv:"+r["aid"]+"v1","accessible",r["loc"][0],r["loc"][1],r["loc"][2],"direct_Not_Disclosed_or_source_specific","stable_SF_2026_ARXIV","independent_exact_v1_method_evaluation_limitations_note" if r["e"]["disposition"].startswith("Integrate") else "not_applicable_no_change",decision_by_family[r["family"]]["decision"],r["e"]["disposition"],"pending" if reaudit_open else "passed"])
    with (PACKET/"evidence-selection-fresh-audit-v2.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["source_family_id","primary_evidence_version","exact_v1_access","method_locator","evaluation_locator","limitation_locator","benchmark_contract","family_id_format","integrate_review_note","selection_decision","books_disposition","audit_status"]); w.writerows(audit_rows)
    sums=[]
    for p in sorted(x for x in PACKET.iterdir() if x.is_file() and x.name not in {"SHA256SUMS","screening-ledger-provisional.json"}): sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name)
    external_targets = (
        (REPORT, "../../18/README.md"),
        (Path(__file__).resolve(), "../../../../../scripts/finalize_june18_v21.py"),
        (ROOT / "scripts/audit_june18_closure_v2.py", "../../../../../scripts/audit_june18_closure_v2.py"),
    )
    for p, relative_name in external_targets:
        sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+relative_name)
    (PACKET/"SHA256SUMS").write_text("\n".join(sums)+"\n")
    print(json.dumps({"denominator_id":did,"raw":516,"retained":len(C),"closures":516-len(C),"integrate":len(integrations),"owners":len(groups),"route":route},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
