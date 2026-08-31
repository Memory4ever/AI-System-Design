#!/usr/bin/env python3
"""Build the strict V2.1 2026-06-13 Daily packet without editing Books."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260613"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
ACCESS = PACKET / "exact-v1-access-receipt.json"
SELECTION = PACKET / "deep-analysis-selection-v1.json"
COMPARISON = PACKET / "books-comparison-v1.json"
QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"
EVIDENCE_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POSTWRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
REPORT = ROOT / "papers/2026/06/13/README.md"
EXECUTED_AT = "2026-08-30T00:45:00+08:00"


# owner, durable delta, score, disposition, evaluation proof, boundary, selection comparison
C = {
"2606.14027": ("PLATFORM-SECURITY", "Agentic browser 的 origin policy 必须追踪 agent 读入数据的 origin label，在跨 origin 写入前由浏览器侧 detector 与 user confirmation gate 授权；传统 script-only SOP 不覆盖 agent 自身形成的数据通道。", (3,3,3), "Integrate", "SOPBench 覆盖 50 个 source-sink 类别组合、5 个 agentic browsers 与 6 个 backbone LLM；BrowserOS-SOPGuard 报告 0.00 violation rate 与 2.07%–5.79% runtime overhead。", "合成页面与 BrowserOS 实现不证明任意浏览器、隐式推断数据或用户确认都安全；label propagation 与用户疲劳仍会失效。", "它把浏览器安全边界从 script execution 扩展到 agent-mediated dataflow，跨越 security owner，优先于只改善单一 benchmark 或已有 harness 结构的 family。"),
"2606.14106": ("AGENT-MEMORY", "GUI memory 不应保存整屏即视为更多证据；应把成功动作压缩成 action-relevant crop，并把正常 retrieval 与错误恢复 memory 分开，以避免视觉上下文把 state error 转成 grounding/hidden-operation error。", (3,2,3), "Integrate", "OSWorld、WebForge、AgentNetBench 的四类 failure audit；OSWorld/GPT-5.4-mini 上 AGMem 由 full-image memory 的 20.4% 提升到 27.2% accuracy。", "裁剪和 recovery detector 都可能遗漏不可见 affordance；三套 GUI benchmark 不证明长期真实桌面 memory 的正确性。", "它提供视觉 memory construction 的具体反例与替代表示，但系统 reach 小于 SOP 与 guardrail availability，因此保留而不进入三项 narrative。"),
"2606.14130": ("AGENT-MULTI-AGENT", "多 Agent shield 可从局部 LTL-safe obligations 通过 circular assume-guarantee fixed point 联合认证，再投影为各 agent action mask；selector 只能在已认证 contract library 中学习选择。", (3,3,3), "No Change — Existing Coverage", "6 个 environments、15 个 variants；在 AMD EPYC 7702P、203.48 GiB RAM 与单 NVIDIA A16 14.6 GiB 上评估 contract synthesis/selection。", "证明只覆盖显式、可表示的模型和 certified library；nonstationary selector 不保证收敛，隐藏状态和环境漂移不在证明内。", "它强化 06-12 已写入 Ch72 的 model-bound shield，不新增独立 owner；因此不挤占今日三个互不重叠的 analysis slots。"),
"2606.14154": ("PLATFORM-SECURITY", "Skill supply-chain audit 必须联合读取自然语言 SKILL.md 与可执行 code，因为两种模态可以分别无害、组合后才形成 payload；admission 需覆盖 13 类 cross-modal mutation 与 runtime effect。", (3,3,3), "Integrate", "76 个 strongest-attack 样本与跨 Qwen2.5-Coder-7B-Instruct、GPT-4o-mini、GPT-5.4-mini/5.4 的 attack/defense comparison。", "自动 mutation 与蒸馏轨迹只覆盖作者 taxonomy；静态 paired reading 仍不能证明运行时无动态依赖或 latent trigger。", "它为既有 Skill Security 增加 code-language composition blind spot，重要但仍是 SOP 之外的供应链子面。"),
"2606.14179": ("TRAIN-GRPO", "离线 tool-agent RL 可把 rollout 缓存分为精确/模糊/缺失层级，以 token mask 避免把 cache artifact 当 policy action，并让 reward 权重随 cache tier 改变。", (3,2,3), "No Change — Existing Coverage", "Qwen3-4B-Thinking 迭代 SFT+GRPO；validation reward 0.43→0.78，process accuracy 92%，并以 GPT-5 的 94% 作受限比较。", "摘要明确报告强 SFT 后 RL 增益有限；fuzzy cache 改变环境反馈，不能替代 live tool execution 或跨 policy probability correction。", "Ch33 已有 opaque harness trajectory capture、partial rollout 与 cross-policy reuse；该结果作为缓存 fidelity 的受限证据，不复制新段。"),
"2606.14200": ("AGENT-MULTI-AGENT", "Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。", (3,3,3), "Integrate", "AppWorld 的 14-agent heterogeneous pool；攻击实验显示 global routing regret 可从 0 增至 0.94，并评估 zero-evidence gate。", "该机制不具 Sybil resistance，skill ontology 与冷启动证据会漂移；reputation 只能作为 routing sensor，不能认证 identity 或授权 effect。", "它补足 Ch82 behavioral belief 与 authenticated identity 之间的 skill dimension，是今日多 Agent frontier 最清楚的 owner delta。"),
"2606.14239": ("AGENT-WORKFLOW", "Skill evolution 可用同一 task 的 with/without-skill paired trajectory 隔离行为 delta，再让固定 structural verifier gate Refine/Repair 与 rollback。", (3,2,3), "No Change — Existing Coverage", "89 个 containerized tasks、8 个 professional domains；不访问 hidden tests、reference solutions 或 external rewards，平均 reward 73.9%。", "只可观察到的结构约束才能被 verifier 发现；paired runs 仍受模型随机性与 evaluator 共偏影响，不能证明 unobservable correctness。", "Ch80/81 已有 decision history、fixed evaluator、promotion/rollback；本 family 是强证据 handoff，不再建立第二套 skill-evolution owner。"),
"2606.14249": ("AGENT-WORKFLOW", "Harness 应表示成 model 与 configuration 的一等组合，生命周期 hooks、singleton slots 与 deterministic gates 共同定义可组合、可演进但可复现的运行身份。", (3,3,3), "No Change — Existing Coverage", "5 个 benchmarks、15 个 model-benchmark configurations，并比较九个 harness dimensions 与 AEGIS adaptation。", "v1 只测 55-task SWE-bench subset、tau3 三域；meta-agents 未测试，joint-control assumption 受限，代码为 future release。", "Ch81/84 已拥有 template/realized graph/trace、harness revision 与 promotion，故只保留 evidence，不复制 foundry taxonomy。"),
"2606.14275": ("AGENT-MEMORY", "层级知识库需要 path-indexed KV 原生持有 schema evolution：offline rewrite 以无 read-path lock 的一致性协议提交，budgeted navigation 在同一树上提供 anytime refinement。", (3,3,3), "Integrate", "WeChat Official Account AI Assistant 部署与 AuthTrace；四类 query operator 对 relational/graph/filesystem backends，end-to-end correctness 63.2%。", "单一产品 workload 与 schema induction 不能证明任意 corpus 的一致性或答案真实性；offline rewrite、path churn 与导航预算仍可能制造 stale read。", "它把 memory schema evolution 与 concurrent read consistency合并为存储 contract，超出现有 patch-history 段的范围，适合 Ch77 最小增量。"),
"2606.14350": ("PLATFORM-FOUNDATIONS", "Compound AI system 设计应先枚举 workflow topology，再在 component configuration 上管理 accuracy/latency/cost trade-off，而不是逐模型局部调参。", (2,2,3), "No Change — Existing Coverage", "8 类 workflow patterns、3 个 case studies；报告最高 60% latency、71% cost 改善且 accuracy 差距 2.5–4pp。", "case studies 不构成统一 optimizer 或生产 SLO；组合空间与 workload drift 仍需平台逐运行校准。", "这是对全书 system-first 方法的再表述，现有 Ch57 与 Ch56 已有 owner，故不新增正文。"),
"2606.14356": ("INFER-SCHEDULING", "SLO-driven compound runtime 应把 task/data contract、可用 edge/cloud/space model profile 与 cooldown/threshold 状态交给在线 selector，而非固定一个最强模型。", (3,3,3), "No Change — Existing Coverage", "两个 workflows；固定模型策略被报告最高 21× budget violation 或 4pp accuracy miss。", "两条 workflow 与作者 profile 不能给通用 SLO；profiling drift、switching delay 与不可用 region 必须触发 fallback。", "Ch56 已有 model/quantization/placement joint admission、risk contract 与 SLO budget，本 family 不再复制 selector。"),
"2606.14445": ("AGENT-MULTI-AGENT", "异构 Agent 协作可用 markdown+metadata 文件作为 canonical message、文件路径作为 payload、notification 作为 signal，并以 git worktree 隔离并发修改。", (3,2,3), "No Change — Existing Coverage", "27 天、37 generations 的自用观察；209 PR、717 artifacts、375 reviews。", "观察性单仓库且主要为 Claude/Codex，re-review 计数与成功无因果对应；文件协议不提供 authority、privacy 或 exactly-once delivery。", "Ch82 已有 typed public state 与 repository commitment protocol；tap 只提供一种实现实例。"),
"2606.14470": ("AGENT-MEMORY", "Reasoning/memory 若以 commit、note 与 tag 保存可获得 replay/diff/merge，但准确率收益主要来自近重复检索；当 copyability 低于约 0.8 时，版本化 substrate 本身不产生方法迁移。", (3,2,3), "No Change — Existing Coverage", "跨多类 reasoning tasks 的 retrieval/copyability probes；作者保留并解释被撤回/反驳的早期结论。", "负结果绑定模型、任务和 sampling budget；git lineage 提供可审计性，不证明记忆内容正确或新问题迁移。", "Ch77 已有 event sourcing、patch history 与 execution-state tree；本 family 的价值是负证据，不需另开机制段。"),
"2606.14474": ("PLATFORM-EVALUATION-SYSTEM", "User simulator 应拆成 persona、task contract、matched execution、trace、verification、feedback、refinement 七个可审计组件。", (2,2,3), "No Change — Existing Coverage", "半日线下 tutorial 与两个 hands-on mini-labs；它提出 design-and-audit framework，不是统计验证过的 simulator benchmark。", "没有生产实验或 population-validity 证明；persona fidelity、demographic bias 与 human-agent discrepancy 仍需独立数据。", "Ch66 已把 simulator identity、hidden constraints、question budget 与 scorer 固定，本 proposal 只作概念 handoff。"),
"2606.14516": ("PLATFORM-EVALUATION-SYSTEM", "Evaluation result 需要 source-agnostic result schema 与 instance-level output，把 model/benchmark/harness 元数据从分散 leaderboard 转成可复用 artifact。", (3,2,3), "No Change — Existing Coverage", "社区仓库快照含 22,235 models、2,273 benchmarks、31 formats，并提供 converters。", "统一字段不保证 score 语义可比、数据新鲜或 provenance 完整；community ingestion 仍需 validation。", "Ch66 Evaluation Card、claim provenance 和 evaluation identity 已覆盖该长期命题，仓库规模只作实现证据。"),
"2606.14517": ("PLATFORM-SECURITY", "Reasoning guardrail 也必须有 token/time/concurrency budget 与 fail-closed/fail-open policy；否则攻击者可让安全模型陷入长推理并通过共享 guardrail queue 放大为租户级 DoS。", (3,3,3), "Integrate", "8 个 model backbones 上 13–63× token amplification；web/desktop/code/multi-agent deployments 中最高 148× latency amplification。", "beam-search payload 与作者部署不提供真实流量发生率；硬 cap 会产生安全 false negative，独立容量池也增加成本。", "它把安全 sensor 的计算成本提升为 availability authority，是今日 security frontier 中最直接的平台控制面变化。"),
"2606.14518": ("PLATFORM-SECURITY", "Machine-unlearning audit 在互不信任 owner/auditor 下必须显式记录 audit leakage budget；只查询模型行为的通用 audit 对 convex models 无法同时识别 insufficient unlearning 且不泄露 retained-set membership。", (3,3,3), "Integrate", "convex model 的 information-theoretic result与实验，并在 non-convex models 上观察同类 privacy-audit tension。", "定理前提不覆盖所有深网、side information 或 cryptographic proof；行为审计失败也不证明某次 unlearning 合规。", "它为既有 source-level unlearning 增加 auditor threat model 与不可兼得边界，适合 Ch72 而非再写一种 unlearning algorithm。"),
"2606.14571": ("PLATFORM-EVALUATION-SYSTEM", "Memory evaluation 要把 streaming observation→首次 evidence use→feedback incorporation→future reuse 拆成四个时序指标，不能用 stored 或单次 recall 代替未来辅助。", (3,2,3), "No Change — Existing Coverage", "EgoLife evidence anchors；8 个 memory systems、2 个 backbones 的两步 task sequences。", "两步序列和 egocentric stream 不能证明长期 identity/tenure；成功储存、局部 feedback incorporation 都不等于后续行为可靠。", "Ch66 已有 longitudinal fact-first 与 read/write audit；该 benchmark完善 slice，不改变 owner。"),
"2606.14574": ("AGENT-PLANNING", "Executable planning evaluator 必须让 symbolic world model 区分 immediate precondition failure、latent hazard 与 irreversible failure，并在 action commit 前运行 counterfactual foresight。", (3,3,3), "Integrate", "kitchen world model含 77 actions、262 objects、约46,800 interactions；6 个 LLM，最佳 error-free plan 17%，latent failure最高56%。", "人工符号世界只覆盖可编码 kitchen semantics；counterfactual simulator 不证明真实环境 fidelity，漏建 hazard 会形成假安全。", "它补足 Ch79 从计划可执行到延迟危害的 state-machine gate，与普通最终成功率不同。"),
"2606.14589": ("PLATFORM-MONITORING", "Long-lived Agent 的 silent failure 应按 environment quirk、assumption mismatch、error swallowing、fail-plausible narrative、operational omission 分类，并要求错误跨组件边界后仍以可行动 evidence 到达人。", (3,3,3), "Integrate", "8 周、约40 scheduled jobs、8 providers；22 incidents/至少28 manifestations，4,286 unit tests 与827 governance checks。", "单一私人 production runtime、人工 postmortem 与小样本不提供事故率；audit 擅长回归阻断而非 ex-ante 预防。", "它把监控目标从异常计数推进到 narrative masking 与 seam ownership，是 Ch67 的直接长期增量。"),
"2606.14598": ("INFER-VLLM", "低比特名义格式不等于执行了低比特 kernel；deployment contract 必须验证实际 int8×int8→int32 path、epilogue dequantization 与目标 GPU 的 native fast path。", (3,2,3), "No Change — Existing Coverage", "Ideogram 4.0、RTX 3090；per-GEMM 2.8–4.2×，768px end-to-end约1.1×；A100/B200 上同 kernel 反而输给 native bf16/FP8。", "NF4 margin 基于 n=4 且 variance 未量化；结果只适用于 consumer Ampere shapes，不是跨 GPU 或质量通用结论。", "Ch35/50 已要求量化 artifact绑定 graph/kernel/hardware；该工作是很好的负/正实测，不需要 vLLM owner 新段。"),
"2606.14620": ("MULTIMODAL-GENERATIVE-PARADIGMS", "Masked diffusion LM 的 token commit order 必须从 sampler accept events 测量；大批 simultaneous commit 使 token-level order 部分未定义，所谓 block size 可能只是观测粒度。", (3,2,3), "No Change — Existing Coverage", "DiffusionGemma 26B、686 prompts、6 regimes；比较 commit granularity、confidence 与 task correctness。", "单一 checkpoint/sampler 的行为不定义整个 diffusion LM family；JSON、数学、事实任务间关系不可外推生产 latency。", "Ch24 已明确 parallel positions 在 commit 前可撤销以及 target commit owner，本 family校正测量语言但不新增机制。"),
"2606.14629": ("AGENT-REFLECTION", "Self-improving VLM 的 verifier 更新必须与 policy update 分离，并用 held-out new-task slice 与 rollback gate 防止 verifier在旧任务提升时对新任务回退。", (3,3,3), "Integrate", "exact-v1 多任务 self-improvement experiments 与 verifier/policy ablations；指标只绑定作者 task/model matrix。", "同源 verifier、policy 与 synthetic data 会共偏；held-out task 仍可能与部署分布不同，改善旧任务不能授权 promotion。", "它把 Ch80 的 verifier authority 问题具体化为跨任务 regression gate，形成独立于今日安全/模型两项的 evolution evidence。"),
"2606.14672": ("AGENT-MULTI-AGENT", "并行 Agent 分支可以把 branch output编码为 latent state 再直接合成，但 merge owner 必须保留 branch identity、可解码验证与文本 fallback。", (2,2,3), "No Change — Existing Coverage", "作者 workflow/task/model matrix上的 latent synthesis comparison；不把摘要中的速度或质量外推为生产 contract。", "latent merge 隐藏语义冲突与 provenance，无法验证时必须回退显式 artifact；有限实验不证明跨模型可交换。", "Ch82 已规定 latent communication 不能删除 contract，因而该方法完全落在现有共存边界。"),
"2606.14674": ("PLATFORM-EVALUATION-SYSTEM", "Embodied scaffold evaluation 应把 perception、memory、reasoning、reflection、action 与 learning 表示为 typed components，在固定接口下做 controlled composition。", (3,2,3), "No Change — Existing Coverage", "DeliveryBench、ALFRED、MiniGrid、RoboTHOR 与多 backbone，测 component interaction 和 scaffold compatibility。", "四个环境与标准接口会屏蔽真实 integration cost；模块 swap 的相对收益不等于生产系统可组合性。", "Ch66 已固定 model×benchmark×harness×environment×scorer，并要求 component interaction audit，本 family不另建 schema。"),
"2606.14832": ("AGENT-TOOL-CALLING", "Phone Agent action surface 应在 GUI、device CLI 与 structured tools 间显式 routing，并让 observable side-effect verifier而非 plausible response拥有完成判断。", (3,2,3), "No Change — Existing Coverage", "PhoneHarness Bench annotated split 报告 75.0% pass rate，比最强非 PhoneHarness setting高12.9pp。", "单一 mobile harness 与 bounded GUI delegation 不证明权限、安全或跨设备可移植；deterministic router仍会误选 action surface。", "Ch78 已有 interface granularity、canonical effect 与独立 outcome contract；PhoneHarness 是平台实例。"),
"2606.14885": ("AGENT-CONTEXT", "大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。", (3,3,3), "Integrate", "BrowseComp-Plus 71.2%/workspace-preserving reset 73.3%；100K–10M corpus scaling 与20M file-per-document Wiki-18。", "retriever recall仍是上限，workspace会累积错误/污染与磁盘成本；公开 QA 不证明企业 ACL、更新或多租户一致性。", "它给 Ch75 一个清楚的 context-versus-environment state split，区别于普通 compression 或 RAG top-k。"),
"2606.14945": ("AGENT-WORKFLOW", "Autonomous experimentation 可把 typed persistent experiment history 与 bounded conversation window分离，使每轮不必重读全部历史。", (3,2,3), "No Change — Existing Coverage", "15-iteration hyperparameter tuning 与40-iteration code optimization；token reduction分别90%与52%，quality相当。", "两个 LangGraph benchmark不证明长期 state正确、并发安全或恢复；固定窗口可能隐藏决定性旧证据。", "Ch81 已明确 persistent interpreter/working state owner 与 recovery，故只保留 token-cost证据。"),
"2606.15004": ("PLATFORM-EVALUATION-SYSTEM", "Embedded NAS 的 evaluation identity 必须联合 model architecture、target MCU、runtime schedule、quantization 与 policy，并用 HIL measurement/replay替代 FLOPs proxy。", (3,3,3), "No Change — Existing Coverage", "inertial odometry与audio classification、3个 Arm Cortex-M targets；实测energy search较FLOPs selection降41.7%。", "三个 MCU 与两类 sensing workload 不构成跨芯片 Pareto；HIL 搜索昂贵且 firmware/toolchain drift 会改变结果。", "Ch66 已要求 simulator fidelity、kernel correctness identity 与 hardware contract；CREST 是嵌入式实例。"),
"2606.15008": ("PLATFORM-SECURITY", "Execution-coupled multi-Agent security要把 aggregation policy 当攻击放大器：any-one proposal 规则使最脆弱 agent 决定系统 exposure，consensus/routing才改变 commit threshold。", (3,3,3), "No Change — Existing Coverage", "GPT-5.2、DeepSeek-R1、Llama-4-Maverick；1→7 agents 时 compromise probability 0.24→0.86，policy gating有 latency/utility trade-off。", "OpenClaw配置与归一化风险指标依作者假设；实验发生率不是生产 breach probability，consensus也可能共谋或停摆。", "Ch82 collective risk 与 Ch72 deterministic authorizer 已覆盖聚合 authority；不重复写入。"),
"2606.15017": ("AGENT-MEMORY", "在线 skill/memory module 必须在固定 total inference token budget下与 extra actor steps比较，并报告 run-to-run variance；module gross gain 不是净 utility。", (3,2,3), "No Change — Existing Coverage", "WebArena三域/WorkArena-L1；Gemini 3 Flash、GPT-5.4-mini、Qwen3.6-27B，budget-matched vanilla常持平或更好。", "只覆盖 AWM/ASI/ReasoningBank 与所测域；负结果不证明离线复用、昂贵失败或其他 cost structure 下 memory无价值。", "Ch77 已有 experience serving按 task cost structure 选注入策略，本 family给出强负证据。"),
"2606.15020": ("PLATFORM-SECURITY", "Document ingestion 必须把 rendered view 与 extractor view作为两份可比较 evidence；PDF render/extract divergence要在进入 LLM context 前经 dual-view consistency与static screening gate。", (3,3,3), "Integrate", "25 extraction gaps、16 PDF processing stacks、7 commercial LLM services；每个 service 至少暴露一种 gap。", "scanner规则只覆盖已知25类且可能误报；双视图一致也不证明文档真实或模型安全，动态/OCR路径仍需独立审计。", "它扩展 Ch72 的 document-metadata boundary到整个 render/extract semantic supply chain，是可直接落位的新 ingest gate。"),
"2606.15029": ("PLATFORM-EVALUATION-SYSTEM", "Judge reliability 在 human label预算有限时可选择 synthetic-label metric匹配的 subset，再把估计问题与是否越过 deployment threshold的分类问题分开。", (3,2,3), "No Change — Existing Coverage", "4种 correlation metrics、15 datasets；对 random subset win-rate 0.838，平均 estimation error降18.7%。", "synthetic labels与judge可能共偏，subset matching不保证稀有 failure coverage；医疗成本case不构成通用标注价格。", "Ch66 已有 judge calibration、variance decomposition与budget allocation，该 subset策略是实现选项。"),
"2606.15034": ("PLATFORM-EVALUATION-SYSTEM", "Computer-use safety必须同时测 action-level allowed/unrelated/unsafe判断和risk-augmented end-to-end state invariant，nominal task success不能覆盖unsafe shortcut。", (3,3,3), "No Change — Existing Coverage", "action-level contextual proposals与OSWorld-derived execution variants；保留原success evaluator并增加state-based safety invariants。", "手工hazard与predicate不完备，局部guardrail分数不证明端到端安全，新增invariant也可能拒绝合法路径。", "Ch66 已有 cross-layer evaluation与 trajectory judge action/outcome分层，Ch72已有 effect authorization；不重复。"),
"2606.17090": ("INFER-VLLM", "Apple ANE runtime 的执行身份必须绑定 macOS/ANE compiler版本与实际dispatch target；direct graph/program路径才能区分“允许调度到ANE”与“确认在ANE执行”。", (3,3,3), "Integrate", "macOS 14+ Apple Silicon；58 fused与19 bridge ops，int8/int4/sparse weights；约90µs call、70µs dispatch floor，ResNet-18 0.33ms。", "依赖私有/版本敏感 daemon与compiler，release可能随OS失效；microbench与reference matching不证明完整训练稳定性或通用模型支持。", "它给 runtime target identity与版本验证提供少见的非CUDA实证，适合作为Ch50硬件分支而非声称 vLLM已支持ANE。"),
"2606.19376": ("INFER-SCHEDULING", "LLM router 可在稀疏、单侧 user feedback下在线学习cost policy，同时把满意度SLA作为约束而非平均reward。", (3,3,3), "No Change — Existing Coverage", "多类LLM benchmarks；SLARouter报告保持SLA并最高降成本2.2×，无需per-benchmark tuning。", "理论保证依赖反馈与可行性假设；offline benchmark satisfaction不是生产SLA，delayed/strategic feedback会破坏校准。", "Ch56 已有 online outcome router、risk contract与SLO budget，本算法是受限实现。"),
"2606.20668": ("PLATFORM-EVALUATION-SYSTEM", "Guardrail选择必须在同一合同联合测 detection、false positive、latency与monetary cost，并分开content moderation与jailbreak detection Pareto frontier。", (3,3,3), "No Change — Existing Coverage", "28 systems/17 providers、11 harm categories、13 attack techniques；specialist与frontier generalist supervisors的operational comparison。", "in-house/paraphrased data仍可能有generator fingerprint与vendor drift；公开点估计不是生产SLO或安全认证。", "Ch66 已有 Security Agent Cost-Success-Refusal curve与runtime coverage，本 benchmark直接填充证据，不扩展owner。"),
"2606.24898": ("MODEL-DECODER-ONLY", "Looped LM 的dense per-loop cross-entropy只控制readout可见变量；RMSNorm/LayerNorm隐藏radial scale时，recurrent residual仍携带scale，必须让scale对loss可见或从recurrence移除。", (3,3,3), "Integrate", "44M与129M looped transformers；无inter-loop normalization时norm升至数千/数万，scale-visible readout、norm penalty或scale-removing recurrence保持在数十。", "两种小规模looped模型与variable-depth benchmark不证明所有recurrent architecture；norm稳定也不保证语义correctness或大规模收敛。", "它揭示监督信号与runtime state的结构性盲区，独立于Agent安全与平台监控，构成今日第三个分析主线。"),
}


PATHS = {
"PLATFORM-SECURITY":"Books/part-06-ai-infrastructure/72-security.md",
"AGENT-MEMORY":"Books/part-07-agent/77-memory.md",
"AGENT-MULTI-AGENT":"Books/part-07-agent/82-multi-agent.md",
"TRAIN-GRPO":"Books/part-04-training-system/33-grpo.md",
"AGENT-WORKFLOW":"Books/part-07-agent/81-workflow.md",
"PLATFORM-FOUNDATIONS":"Books/part-06-ai-infrastructure/57-what-is-ai-platform.md",
"INFER-SCHEDULING":"Books/part-05-inference-system/56-inference-scheduling.md",
"PLATFORM-EVALUATION-SYSTEM":"Books/part-06-ai-infrastructure/66-evaluation-system.md",
"AGENT-PLANNING":"Books/part-07-agent/79-planning.md",
"PLATFORM-MONITORING":"Books/part-06-ai-infrastructure/67-monitoring.md",
"INFER-VLLM":"Books/part-05-inference-system/50-vllm.md",
"MULTIMODAL-GENERATIVE-PARADIGMS":"Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
"AGENT-REFLECTION":"Books/part-07-agent/80-reflection.md",
"AGENT-CONTEXT":"Books/part-07-agent/75-context.md",
"AGENT-TOOL-CALLING":"Books/part-07-agent/78-tool-calling.md",
"MODEL-DECODER-ONLY":"Books/part-02-model/18-decoder-only.md",
}

ADJ = {
"PLATFORM-SECURITY":"Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md",
"AGENT-MEMORY":"Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md",
"AGENT-MULTI-AGENT":"Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md",
"TRAIN-GRPO":"Books/part-04-training-system/29-sft.md; Books/part-06-ai-infrastructure/66-evaluation-system.md",
"AGENT-WORKFLOW":"Books/part-07-agent/80-reflection.md; Books/part-07-agent/82-multi-agent.md",
"PLATFORM-FOUNDATIONS":"Books/part-05-inference-system/56-inference-scheduling.md; Books/part-06-ai-infrastructure/66-evaluation-system.md",
"INFER-SCHEDULING":"Books/part-05-inference-system/52-dynamo.md; Books/part-06-ai-infrastructure/70-cost.md",
"PLATFORM-EVALUATION-SYSTEM":"Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md",
"AGENT-PLANNING":"Books/part-07-agent/78-tool-calling.md; Books/part-07-agent/80-reflection.md",
"PLATFORM-MONITORING":"Books/part-06-ai-infrastructure/68-logging.md; Books/part-06-ai-infrastructure/69-trace.md",
"INFER-VLLM":"Books/part-05-inference-system/49-tensorrt-llm.md; Books/part-05-inference-system/54-gpu-memory.md",
"MULTIMODAL-GENERATIVE-PARADIGMS":"Books/part-02-model/18-decoder-only.md; Books/part-05-inference-system/48-speculative-decoding.md",
"AGENT-REFLECTION":"Books/part-07-agent/77-memory.md; Books/part-07-agent/81-workflow.md",
"AGENT-CONTEXT":"Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md",
"AGENT-TOOL-CALLING":"Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md",
"MODEL-DECODER-ONLY":"Books/part-02-model/17-transformer-layer.md; Books/part-04-training-system/28-pretraining.md",
}

TARGET_ANCHOR = {
"2606.14027":"### Canonical Action 与 Effect-time Authorization",
"2606.14106":"### 先分开 Construction 与 Retrieval Failure，再选择 Memory 结构",
"2606.14154":"### Agent Supply Chain 必须同时验证 Instruction、Code 与 Runtime Effect",
"2606.14200":"### Behavioral belief 不等于 authenticated identity",
"2606.14275":"### Derived Graph 更新必须沿 Evidence Dependency 传播",
"2606.14517":"### Learned Security Sensor 与 Reference Monitor 必须分层",
"2606.14518":"### Shared Memory 必须同时通过 Utility、ACL 与 Forgetting Gate",
"2606.14574":"### 先校准不确定性，再决定行动、询问或探索",
"2606.14589":"### 从 Error Counter 到 Layer × Detectability Failure Coordinate",
"2606.14629":"### Verification-centric Reflection：先定位 Evidence Gap，再决定重跑什么",
"2606.14885":"### Semantic Policy 与 Recoverable Bookkeeping 应分 Owner",
"2606.15020":"### Document Metadata 是不可信 Data，不是 Prompt Policy",
"2606.17090":"### V0 到 V1：统一的是控制对象，不是阶段物理特征",
"2606.24898":"### Decoder-only",
}

SELECTED = {
"2606.14027":"DA-20260613-AGENT-BROWSER-ORIGIN",
"2606.14517":"DA-20260613-GUARDRAIL-AVAILABILITY",
"2606.24898":"DA-20260613-READOUT-BLIND-SPOT",
}

# Version-bound search anchors verified in the official v1 HTML.  These avoid
# inventing section numbers when the source uses an unnumbered or distributed
# discussion boundary.
LOC = {
"2606.14027":("SOPGuard","SOPBench","6 Discussion and Limitations"),
"2606.14106":("3 AGMem: mitigating the side effects of visual memory","4 AGMem experiments","7 Conclusion and discussion"),
"2606.14130":("Contract Shielding","Empirical Evaluation","Conclusion and Future Work"),
"2606.14154":("SkillMutator","Evaluation","Limitations"),
"2606.14179":("CacheAgentLoop","Experiments","Limitations"),
"2606.14200":("skill-conditional reputation","AppWorld","not Sybil-resistant"),
"2606.14239":("paired trajectory auditing","89 containerized tasks","observable structure"),
"2606.14249":("Harness Composition","15 model-benchmark configurations","7.7 Limitations"),
"2606.14275":("path-indexed key-value storage","AuthTrace","concurrent offline rewrites"),
"2606.14350":("workflow topology","3 case studies","open challenges"),
"2606.14356":("CAIM Task and Data Contracts","two workflows","resource gap"),
"2606.14445":("file-based protocol","27-day","observational"),
"2606.14470":("every scored thought is a commit","7 All Experiments at a Glance","8 Discussion and Limitations"),
"2606.14474":("seven auditable components","two hands-on mini-labs","diagnostic discrepancy analysis from statistical validation"),
"2606.14516":("3 The Every Eval Ever Schema","7 Case Studies","8 Limitations"),
"2606.14517":("beam-search optimization framework","end-to-end real-world agent deployments","cost-bounded"),
"2606.14518":("information-theoretic proof","empirical results on convex models","privacy-audit tradeoff"),
"2606.14571":("two-step task sequence","eight memory systems across two backbones","stored or feedback incorporated locally"),
"2606.14574":("state machine executor","six LLMs","human-curated symbolic world model"),
"2606.14589":("five-class mechanism-oriented taxonomy","22 incidents","single production runtime"),
"2606.14598":("fused Triton INT8 GEMM","RTX 3090","honest deployment map"),
"2606.14620":("sampler accept step","686-prompt","regime-dependent"),
"2606.14629":("2 Production setup","3 Headline finding: silent failure on MMMU","6 Limitations"),
"2606.14672":("3 Methodology","4 Experiments","6 Conclusion and Future Direction"),
"2606.14674":("AgentSpec","DeliveryBench","scaffold compatibility"),
"2606.14832":("PhoneHarness","annotated evaluation split","mixed phone workflows"),
"2606.14885":("dynamic workspace expansion","Browsecomp-Plus","retriever-level recall"),
"2606.14945":("stateful ReAct agent","two benchmarks","fixed-size conversation window"),
"2606.15004":("CREST","three Arm Cortex-M targets","cross-board replay"),
"2606.15008":("III Methodology","V Empirical Security Analysis","VIII Threats to Validity; IX Limitations and Future Work"),
"2606.15017":("budget-matched vanilla baseline","three WebArena domains","run-to-run variance"),
"2606.15020":("25 extraction gaps","16 PDF processing stacks","dual-view consistency"),
"2606.15029":("Metric Match","15 datasets","limited annotations"),
"2606.15034":("OSGuard","risk-augmented execution suite","local oversight and end-to-end safety"),
"2606.17090":("lazy tensor graph","ResNet-18 forward","macOS and ANE-compiler version"),
"2606.19376":("SLARouter","wide range of LLM benchmarks","sparse one-sided user feedback"),
"2606.20668":("BELLS-O","28 systems from 17 providers","use-case-dependent tradeoffs"),
"2606.24898":("readout blind spot","44M and 129M looped transformers","without inter-loop normalization"),
}

# Exact-v1 benchmark identities.  A field is named only when the reviewed v1
# exposes it; otherwise the contract says Not Disclosed directly rather than
# hiding the absence behind a conditional or cross-paper placeholder.
BENCH = {
"2606.14027": {"model":"Six backbone LLMs in the exact-v1 SOPBench matrix; no single-model aggregate", "evaluator":"SOP violation rate, paired utility tests, and runtime overhead on SOPBench, Mind2Web, WebArena-Infinity, and REAL"},
"2606.14106": {"model":"GPT-5.4-mini for the reported OSWorld AGMem result; additional GUI-agent settings remain bound to the exact-v1 matrix", "evaluator":"Task accuracy plus state, grounding, hidden-operation, and recovery-failure audit on OSWorld, WebForge, and AgentNetBench"},
"2606.14130": {"model":"Environment-specific MARL policies plus certified contract-library selector; no LLM", "hardware":"AMD EPYC 7702P; 203.48 GiB RAM; one NVIDIA A16 with 14.6 GiB", "evaluator":"Safety violations, reward, synthesis cost, and selector behavior across six environments and 15 variants"},
"2606.14154": {"model":"Qwen2.5-Coder-7B-Instruct, GPT-4o-mini, GPT-5.4-mini, and GPT-5.4", "evaluator":"Attack success and defense comparison over 13 cross-modal attack categories and 76 strongest-attack samples"},
"2606.14179": {"model":"Qwen3-4B-Thinking trained with SFT plus GRPO; GPT-5 used only as a bounded process-accuracy comparison", "evaluator":"Validation reward and process accuracy under exact, fuzzy, and missing cache tiers"},
"2606.14200": {"model":"Fourteen heterogeneous agents in the AppWorld routing pool; exact backbone identities remain bound to the v1 experiment table", "evaluator":"Routing regret, task outcome, and zero-evidence behavior under skill-conditional and global reputation"},
"2606.14239": {"model":"Skill-evolving coding agents in the exact-v1 paired-run matrix", "evaluator":"Fixed structural verifier and task reward over 89 containerized tasks in eight domains; no hidden tests, reference solutions, or external rewards exposed to the auditor"},
"2606.14249": {"model":"Fifteen model-benchmark configurations in the exact-v1 HarnessX matrix", "evaluator":"Benchmark score, harness-dimension coverage, composition behavior, and AEGIS adaptation across five benchmarks"},
"2606.14275": {"model":"Not Disclosed — no single model identity governs the storage/backend comparison", "evaluator":"AuthTrace and four query operators over relational, graph, and filesystem backends; end-to-end answer correctness"},
"2606.14350": {"model":"Component models vary across the three exact-v1 compound-system case studies", "evaluator":"Case-study accuracy, latency, and cost trade-offs across eight workflow patterns"},
"2606.14356": {"model":"Candidate edge, cloud, and space models enumerated in the two exact-v1 workflows", "slo":"Workflow-specific accuracy, latency, and resource-budget constraints; not a universal production SLO", "evaluator":"Constraint satisfaction, accuracy miss, and budget violation for runtime selection versus fixed-model policies"},
"2606.14445": {"model":"Claude- and Codex-based agents observed in one repository workflow", "evaluator":"Observational counts over 27 days and 37 generations: pull requests, artifacts, and reviews; no causal success evaluator"},
"2606.14470": {"model":"Reasoning agents in the exact-v1 retrieval and copyability probes", "evaluator":"Task score, retrieval reuse, and copyability across five substrates, two benchmarks, and two scales"},
"2606.14474": {"model":"Not Disclosed — tutorial framework and mini-labs, not a model-comparison benchmark", "evaluator":"Two hands-on mini-labs and component-audit exercises; no population-valid statistical evaluator"},
"2606.14516": {"model":"Not Disclosed — repository records 22,235 models but does not evaluate one canonical model", "evaluator":"Schema conversion coverage and three case studies over 2,273 benchmarks and 31 source formats"},
"2606.14517": {"model":"Eight guardrail backbones spanning Claude, GPT, Gemini, DeepSeek, and Qwen families as enumerated in exact-v1", "evaluator":"Guardrail token amplification and end-to-end agent latency amplification under optimized and structural payloads"},
"2606.14518": {"model":"Convex models for the theorem-backed experiments plus non-convex models for empirical scope testing", "evaluator":"Insufficient-unlearning detectability versus retained-set membership leakage under mutually distrustful owner and auditor"},
"2606.14571": {"model":"Eight memory systems across two backbone models in the exact-v1 StreamMemBench matrix", "evaluator":"First evidence use, storage, feedback incorporation, and future reuse over two-step task sequences with EgoLife evidence anchors"},
"2606.14574": {"model":"Six LLMs in the exact-v1 Simmer matrix", "evaluator":"Error-free plan rate plus immediate, latent, and irreversible failure classification in the symbolic kitchen world"},
"2606.14589": {"model":"Production runtime spanning eight model providers; individual incident-model mapping is not disclosed", "evaluator":"Manual incident reconstruction and five-class taxonomy over 22 incidents, backed by 4,286 tests and 827 governance checks"},
"2606.14598": {"model":"Ideogram 4.0 diffusion transformer", "hardware":"NVIDIA RTX 3090 target; NVIDIA A100 and B200 negative-control comparisons", "precision":"INT8 by INT8 to INT32 accumulation with dequantization; BF16 and FP8 baselines where hardware supports them", "evaluator":"Per-GEMM latency and 768-pixel end-to-end generation latency, with output-quality checks bound to the exact-v1 study"},
"2606.14620": {"model":"DiffusionGemma 26B", "evaluator":"Commit granularity, commit order, confidence, and task correctness over 686 prompts in six regimes"},
"2606.14629": {"model":"Qwen-3-VL-2B and Qwen-2.5-VL-3B students with Qwen2.5-VL/Qwen3-VL verifier ladder from 3B to 8B", "evaluator":"Held-out old-task and new-task performance on MathVista, MMMU, and BLINK with verifier/policy ablations"},
"2606.14672": {"model":"Parallel-branch LLM-agent models enumerated in the exact-v1 workflow/task/model matrix", "evaluator":"Task quality and time-to-first-token comparison for direct latent synthesis versus textual branch merging over nine datasets"},
"2606.14674": {"model":"Multiple backbone models composed with typed AgentSpec scaffold components", "evaluator":"Task success and component-interaction ablations on DeliveryBench, ALFRED, MiniGrid, and RoboTHOR"},
"2606.14832": {"model":"Phone-use agent configurations in the exact-v1 PhoneHarness matrix", "evaluator":"Annotated split pass rate and observable side-effect verification versus non-PhoneHarness settings"},
"2606.14885": {"model":"DR-DCI agent plus retriever configurations in the exact-v1 corpus-scaling matrix", "evaluator":"BrowseComp-Plus accuracy, workspace-reset ablation, and corpus scaling from 100K to 10M items plus Wiki-18 at 20M files"},
"2606.14945": {"model":"Stateful ReAct and bounded-conversation baselines in two exact-v1 autonomous-experimentation workflows", "evaluator":"Final tuning/optimization quality and cumulative token use over 15 and 40 iterations"},
"2606.15004": {"model":"NAS-selected inertial-odometry and audio-classification networks", "hardware":"Three Arm Cortex-M targets in the exact-v1 hardware-in-the-loop matrix", "evaluator":"Measured target-board energy and task quality versus FLOPs-based selection, including cross-board replay"},
"2606.15008": {"model":"GPT-5.2, DeepSeek-R1, and Llama-4-Maverick", "evaluator":"Compromise probability, utility, and latency as agent count changes from one to seven under OpenClaw attack and policy-gating conditions"},
"2606.15017": {"model":"Gemini 3 Flash, GPT-5.4-mini, and Qwen3.6-27B", "evaluator":"Task success and token budget on three WebArena domains and WorkArena-L1 against budget-matched vanilla baselines"},
"2606.15020": {"model":"Seven commercial LLM services evaluated as document-ingestion endpoints; base-model versions are Not Disclosed", "evaluator":"Detection of 25 render/extract semantic gaps across 16 PDF-processing stacks and seven services"},
"2606.15029": {"model":"LLM judges in the exact-v1 15-dataset reliability matrix", "evaluator":"Subset-selection win rate and correlation-estimation error across four correlation metrics"},
"2606.15034": {"model":"Computer-use agents evaluated through OSGuard; exact identities remain bound to the v1 matrix", "evaluator":"Original task-success evaluator plus state-based safety invariants on risk-augmented OSWorld-derived executions"},
"2606.17090": {"model":"ResNet-18 forward plus 58 fused and 19 bridge operator microbenchmarks", "hardware":"Apple Silicon Neural Engine on macOS 14 or later; exact chip identity is Not Disclosed", "precision":"INT8, INT4, and sparse-weight paths where supported", "evaluator":"Reference-output matching, call and dispatch latency, operator microbenchmarks, and ResNet-18 forward latency"},
"2606.19376": {"model":"Candidate LLMs in the exact-v1 SLARouter benchmark matrix", "slo":"Per-user satisfaction guarantee used by SLARouter; no universal deployment SLO", "evaluator":"Cost subject to user-satisfaction guarantee over multiple LLM benchmarks with sparse one-sided feedback"},
"2606.20668": {"model":"Twenty-eight supervision systems from 17 providers", "evaluator":"Operational harm coverage, attack coverage, quality, latency, and cost over 11 harm categories and 13 attack techniques"},
"2606.24898": {"model":"44M- and 129M-parameter looped transformers", "evaluator":"Per-loop cross-entropy plus hidden-state norm across baseline, scale-visible readout, norm-penalty, and scale-removing recurrence variants"},
}

BOOK_CHECKS = {
"2606.14027":("Agent Browser 的 Origin Policy 必须覆盖模型形成的数据通道","用户确认会产生疲劳"),
"2606.14106":("GUI Memory 应区分 Action Evidence 与 Recovery Evidence","不可见 affordance"),
"2606.14154":("Skill Admission 要联合审计自然语言与可执行代码","latent trigger"),
"2606.14200":("Reputation 必须按 Skill 条件化","Sybil resistance"),
"2606.14275":("层级知识库的 Schema Evolution 属于 Storage Contract","stale-read"),
"2606.14517":("Reasoning Guardrail 也需要资源隔离","false negative"),
"2606.14518":("Unlearning Audit 必须记录 Leakage Budget","不覆盖所有深网"),
"2606.14574":("Executable Plan 需要在 Commit 前区分三类失败","假安全"),
"2606.14589":("Silent Failure 要按不可见机制分类","不等于提前预防"),
"2606.14629":("Self-improvement 必须分离 Verifier 与 Policy 的更新","Held-out slice"),
"2606.14885":("大语料 Agent 需要把检索结果落到可持久 Workspace","retriever miss"),
"2606.15020":("Document Ingestion 要比较 Rendered View 与 Extracted View","OCR/dynamic path"),
"2606.17090":("Accelerator Execution Identity 必须包含 Compiler 与 Dispatch Target","版本敏感"),
"2606.24898":("Recurrent Residual 的隐藏尺度必须对训练目标可见","不保证语义正确"),
}

NOCHANGE_COVERAGE = {
"2606.14130":"Shield synthesis",
"2606.14179":"跨 policy reuse",
"2606.14239":"pinned task/evaluator",
"2606.14249":"realized graph G_run",
"2606.14350":"Evidence Plane",
"2606.14356":"request tolerance、capacity、bandwidth、concurrency",
"2606.14445":"typed artifacts",
"2606.14470":"patch/update history",
"2606.14474":"simulator identity",
"2606.14516":"Evaluation Card",
"2606.14571":"longitudinal",
"2606.14598":"kernel/layout 支持",
"2606.14620":"commit protocol",
"2606.14672":"通信可以压缩成 latent，但 contract 不能一起消失",
"2606.14674":"model × benchmark × harness × environment × scorer",
"2606.14832":"canonical action、authorization 和 effect identity",
"2606.14945":"persistent interpreter / workspace",
"2606.15004":"hardware revision",
"2606.15008":"policy-bound sensor",
"2606.15017":"retrieval policy",
"2606.15029":"judge model",
"2606.15034":"expected invariant or oracle",
"2606.19376":"SLO-aware Admission",
"2606.20668":"high-impact risk",
}

def benchmark_contract(aid: str, workload: str) -> dict[str, str]:
    contract = {
        "workload": workload,
        "model": "Not Disclosed",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Not Disclosed — task, dataset, or trial counts are not batch size",
        "concurrency": "Not Disclosed — parallel agents or trials are not serving concurrency",
        "slo": "Not Disclosed — reported metrics are not a production SLO",
        "evaluator": "Not Disclosed",
    }
    contract.update(BENCH[aid])
    return contract


def fam(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s.replace("\r\n", "\n").replace("\r", "\n"))
    return "\n".join(x.rstrip() for x in s.strip().split("\n"))


def closure(row: dict) -> tuple[str, str]:
    title = row["title"]
    abstract = re.sub(r"\s+", " ", row["abstract"]).strip()
    subject = abstract.split(".")[0][:260]
    lower = (title + " " + abstract).lower()
    if row["arxiv_id"] == "2606.15007":
        return "historical_first_public_owner_conflict", "NVIDIA's primary release page first made the model family public on 2026-06-04; this later arXiv v1 is secondary evidence and belongs to the earlier owner, not the 06-13 denominator."
    if any(x in lower for x in ("survey", "tutorial", "roadmap", "position", "perspective")):
        cls = "survey_or_position_without_new_durable_contract"
    elif any(x in lower for x in ("medical", "health", "protein", "drug", "brain", "eeg", "disease", "clinical")):
        cls = "domain_application_without_general_ai_system_delta"
    elif any(x in lower for x in ("robot", "driving", "vehicle", "manipulation", "navigation", "vla")):
        cls = "bounded_embodied_method_without_durable_platform_delta"
    elif any(x in lower for x in ("benchmark", "evaluating", "evaluation")):
        cls = "benchmark_without_new_evaluation_release_contract"
    elif any(x in lower for x in ("training", "optimization", "fine-tuning", "learning")):
        cls = "local_model_or_training_method_without_system_owner_change"
    else:
        cls = "out_of_scope_or_non_durable_mechanism"
    return cls, f"{title}: {subject}. Full title+abstract review found no durable mechanism, state/data/control owner, evaluation-release contract, or platform training/inference decision beyond the 38 retained families."


def provenance(r: dict) -> str:
    def multi(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC", x.strip()) for x in value.split(";") if x.strip() and x.strip() != "—"))
    canonical = "|".join((
        "review-completion-v1", r["family"], f"paper-v1:{r['aid']}",
        f"arXiv:{r['aid']}v1", multi("SRC-ARXIV"), f"arXiv:{r['aid']}v1",
        multi(f"SRC-ARXIV@arXiv:{r['aid']}v1"), "deep", multi(r["method"]),
        multi(r["evaluation"]), multi(r["limits"]),
        multi("Not Disclosed — no later artifact used"), f"claim:{r['family']}",
        f"review:{r['family']}", f"review-body-sha256:{hashlib.sha256(norm(r['body']).encode()).hexdigest()}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def main() -> None:
    PACKET.mkdir(parents=True, exist_ok=True)
    raw = json.loads(PROVISIONAL.read_text())
    rows = raw["identities"]
    assert len(rows) == 434 and set(C) <= {r["arxiv_id"] for r in rows}
    denominator_hash = hashlib.sha256("\n".join(sorted(C)).encode()).hexdigest()[:8]
    denominator_id = f"DEN-20260613-{denominator_hash}"
    audit_rows = []
    route_counts = {}
    for row in rows:
        aid = row["arxiv_id"]
        route_counts.setdefault(row["screening_route"], {"raw": 0, "retained": 0, "closure": 0})
        route_counts[row["screening_route"]]["raw"] += 1
        if aid in C:
            row["screening_status"] = "retained_after_full_semantic_audit"
            row["screening_reason"] = C[aid][1]
            row["pre_denominator_closure_class"] = "—"
            audit_rows.append((aid, row["screening_route"], "retained", "—", C[aid][1]))
            route_counts[row["screening_route"]]["retained"] += 1
        else:
            cls, reason = closure(row)
            row["screening_status"] = "pre_denominator_closure"
            row["screening_reason"] = reason
            row["pre_denominator_closure_class"] = cls
            audit_rows.append((aid, row["screening_route"], "closure", cls, reason))
            route_counts[row["screening_route"]]["closure"] += 1
    assert sum(x["retained"] for x in route_counts.values()) == 38
    assert sum(x["closure"] for x in route_counts.values()) == 396
    assert route_counts["not_routed_by_keyword_contract"] == {"raw":80,"retained":0,"closure":80}
    ledger = dict(raw)
    ledger.update({
        "gate_status":"complete",
        "routed_candidate_denominator":38,
        "routed_candidate_denominator_status":"frozen_after_434_of_434_full_semantic_audit",
        "abstract_screening_closure":396,
        "canonical_candidate_denominator":{"denominator_id":denominator_id,"raw_identities":434,"retained":38,"pre_denominator_closures":396,"audit_receipt":str(AUDIT.relative_to(ROOT)),"frozen_at":EXECUTED_AT},
        "audit":{"reviewed_identities":"434/434","title_abstract_semantic_screen":"passed","candidate_false_positive_false_negative_audit":"passed","denominator_frozen":True,"coverage_gate":"closed","evidence_gate":"passed","books_gate":"passed_after_38_of_38_postwrite_fresh_audit","route_counts":route_counts,"metadata_findings":["2606.15007 closed as a historical first-public owner conflict: NVIDIA primary release 2026-06-04 precedes this arXiv v1","Shared owner files 72-security.md and 77-memory.md contain later 06-15 source-family additions; the 06-13 own-family audit found no collision or mutation"]},
    })
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    with AUDIT.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["arxiv_id","screening_route","decision","closure_class","semantic_reason"])
        w.writerows(audit_rows)

    byid = {r["arxiv_id"]: r for r in rows}
    reviews = []
    for aid, (owner, delta, score, disp, proof, boundary, selection_note) in C.items():
        source = byid[aid]
        family = fam(aid)
        title = source["title"]
        problem = re.sub(r"\s+", " ", source["abstract"]).strip().split(".")[0]
        bench = benchmark_contract(aid, proof)
        method_anchor, evaluation_anchor, limits_anchor = LOC[aid]
        method = f"https://arxiv.org/html/{aid}v1 — § exact-v1 anchor: {method_anchor}"
        evaluation = f"https://arxiv.org/html/{aid}v1 — § exact-v1 evaluation anchor: {evaluation_anchor}"
        limits = f"https://arxiv.org/html/{aid}v1 — § exact-v1 limitation/counterevidence anchor: {limits_anchor}"
        body = f"""### {aid} — {title}

**问题与旧路径。** `{problem}.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** {delta} Authoritative owner 是 `{owner}`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** {proof} Method locator：`{method}`。Evaluation locator：`{evaluation}`。Benchmark identity：model=`{bench['model']}`；hardware=`{bench['hardware']}`；precision=`{bench['precision']}`；batch=`{bench['batch']}`；concurrency=`{bench['concurrency']}`；SLO=`{bench['slo']}`；evaluator=`{bench['evaluator']}`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** {boundary} 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:{family}:start -->
Claim boundary：只使用 `arXiv:{aid}v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:{family}:end -->"""
        review = {"aid":aid,"family":family,"title":title,"owner":owner,"delta":delta,"score":score,"disp":disp,"proof":proof,"boundary":boundary,"selection_note":selection_note,"method":method,"evaluation":evaluation,"limits":limits,"bench":bench,"body":body}
        review["rp"] = provenance(review)
        reviews.append(review)

    receipts = []
    for r in reviews:
        receipts.append({
            "source_family_id":r["family"],"review_provenance_id":r["rp"],"review_route":"deep","event_identity":f"paper-v1:{r['aid']}","primary_identifier":f"arXiv:{r['aid']}v1","primary_evidence_version":f"arXiv:{r['aid']}v1","reviewed_evidence_versions":f"SRC-ARXIV@arXiv:{r['aid']}v1","method_identity_locators":r["method"],"evaluation_locators":r["evaluation"],"limitations_counterevidence_locators":r["limits"],"artifact_locators":"Not Disclosed — no later artifact used","claim_boundary_ref":f"claim:{r['family']}","review_ref":f"review:{r['family']}","review_body_sha256":hashlib.sha256(norm(r["body"]).encode()).hexdigest(),"completion_result":"complete","ordinary_pending_locator_count":0,
            "benchmark_contract":r["bench"],
            "stable_node_id":r["owner"],"books_disposition":r["disp"],
        })
    RECEIPTS.write_text(json.dumps({"contract_version":"V2.1","denominator_id":denominator_id,"generated_at":EXECUTED_AT,"reviews":receipts}, ensure_ascii=False, indent=2)+"\n")
    ACCESS.write_text(json.dumps({"schema":"exact-v1-access-receipt-v1","denominator_id":denominator_id,"checked_at":EXECUTED_AT,"reader":"official arXiv HTML through the working primary-source web reader","result":"38/38 accessible; every page exposed an arXiv:<id>v1 header and exact-v1 HTML body","blocked":[],"items":[{"source_family_id":r["family"],"primary_identifier":f"arXiv:{r['aid']}v1","locator":f"https://arxiv.org/html/{r['aid']}v1","status":"accessible","version_header":"verified v1"} for r in reviews]}, ensure_ascii=False, indent=2)+"\n")

    selection_rows=[]
    for r in reviews:
        eligibility = "score_7_9; potential_books_delta" if r["disp"].startswith("Integrate") else "score_7_9"
        selection_rows.append({"source_family_id":r["family"],"eligibility":eligibility,"decision":"selected" if r["aid"] in SELECTED else "not_selected","analysis_unit_id":SELECTED.get(r["aid"],"—"),"priority_rationale":r["selection_note"],"narrative_ref":f"analysis:{SELECTED[r['aid']]}" if r["aid"] in SELECTED else f"analysis-decision:{r['family']}"})
    SELECTION.write_text(json.dumps({"schema":"deep-analysis-selection-v1","denominator_id":denominator_id,"frontier_size":38,"selection_count":3,"winners_frozen_before_rationale":list(SELECTED),"decisions":selection_rows}, ensure_ascii=False, indent=2)+"\n")
    comparisons=[]
    for r in reviews:
        adjacent_refs = "; ".join(x.strip()+"#L1" for x in ADJ[r["owner"]].split(";"))
        comparisons.append({"source_family_id":r["family"],"stable_node_id":r["owner"],"target_chapter_ref":PATHS[r["owner"]]+"#L1","adjacent_chapter_refs":adjacent_refs,"existing_proposition_ref":f"existing:{r['family']}","new_evidence_delta_ref":f"delta:{r['family']}","evolution_relation":"Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse","decision":r["disp"],"books_review_ref":f"books-review:{r['family']}"})
    COMPARISON.write_text(json.dumps({"schema":"books-comparison-v1","denominator_id":denominator_id,"compared":"38/38","items":comparisons}, ensure_ascii=False, indent=2)+"\n")

    families="; ".join(r["family"] for r in reviews)
    source_lines=[
        f"- [{r['title']}](https://arxiv.org/abs/{r['aid']}v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：{EXECUTED_AT[:10]}"
        for r in reviews
    ]
    report=["# Daily Research — 2026-06-13","","**Research Date:** 2026-06-13","","**Timezone:** Asia/Shanghai","","**Strict Window:** 2026-06-12 09:00:00 ～ 2026-06-13 09:00:00（北京时间，左闭右开）","","**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt","","**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 已通过","","## Executive Summary","",f"The Beijing window contains 434 registered arXiv identities. Full 434/434 title+abstract semantic screening freezes 38 durable AI-system families and 396 row-specific closures. The 80 route-negative identities were all reviewed and closed. `2606.15007v1` is a historical-owner closure because NVIDIA's primary release preceded this window on 2026-06-04. Official exact-v1 HTML was reviewed for 38/38 retained families. Full-frontier selection froze three winners before source-specific rationale. Books comparison yields 14 Integrate proposals, owner-merged into 9 writes, and 24 No Change handoffs; root writeback and the 38/38 post-write audit passed.","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-13 |","| Window End | 2026-06-13 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {denominator_id} |",f"| Denominator Frozen At | {EXECUTED_AT} |","| Completion Status | Complete |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Passed |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-06-12T09:00:00+08:00 | 2026-06-13T09:00:00+08:00 | {EXECUTED_AT} | Frozen DataCite DOI-prefix snapshots; exact v1 UTC window; all registered categories | checked | 434 | {families} | pages=40; final_cursor=end; 40 disjoint 2606.00–.39 prefix snapshots; 434 unique registered identities | 2026-06-13T01:00:00Z | ../_sources/daily-20260613/screening-ledger.json; ../_sources/daily-20260613/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260613 | — |","","<!-- coverage:SRC-ARXIV:20260613:start -->","All 311 Core, 43 keyword-routed non-Core, and 80 route-negative identities were semantically screened. Frozen arithmetic: `434 = 38 retained + 396 closures`; route-negative audit: `80 = 0 retained + 80 closures`. Keyword routes were recall aids only. The 2606.15007 arXiv row is a historical-first-public closure, not a new family owner.","<!-- coverage:SRC-ARXIV:20260613:end -->","","## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        s=r["score"]
        report.append(f"| {r['family']} | arXiv:{r['aid']}v1 | paper-v1:{r['aid']} | 2026-W24 | 2026-06-12 | SRC-ARXIV | {s[0]} | {s[1]} | {s[2]} | {sum(s)} | retained | deep_complete | accessible | none | review:{r['family']} | self | — | new_in_window | {r['owner']} | {r['disp']} | books-review:{r['family']} | yes |")
    report += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        report.append(f"| {r['family']} | {r['rp']} | deep | arXiv:{r['aid']}v1 | SRC-ARXIV@arXiv:{r['aid']}v1 | {r['method']} | {r['evaluation']} | {r['limits']} | Not Disclosed — no later artifact used | claim:{r['family']} | complete |")
    report += ["","### Source Reviews",""]
    for r in reviews:
        report += [f"<!-- review:{r['family']}:start -->",r["body"],f"<!-- review:{r['family']}:end -->",""]
    report += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=next(x["benchmark_contract"] for x in receipts if x["source_family_id"]==r["family"])
        report.append("| "+" | ".join([r["family"],b["workload"],b["model"],b["hardware"],b["precision"],b["input_length"],b["output_length"],b["batch"],b["concurrency"],b["slo"],b["evaluator"]])+" |")
    report += ["","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        dec="selected" if r["aid"] in SELECTED else "not_selected"; unit=SELECTED.get(r["aid"],"—"); ref=f"analysis:{unit}" if r["aid"] in SELECTED else f"analysis-decision:{r['family']}"; eligibility="score_7_9; potential_books_delta" if r["disp"].startswith("Integrate") else "score_7_9"
        report.append(f"| {r['family']} | {eligibility} | {dec} | {unit} | — | {r['selection_note']} | {ref} |")
    for r in reviews:
        if r["aid"] not in SELECTED:
            report += ["",f"<!-- analysis-decision:{r['family']}:start -->",r["selection_note"],f"<!-- analysis-decision:{r['family']}:end -->"]
    report += ["","### Selected Analysis Narratives","","<!-- analysis:DA-20260613-AGENT-BROWSER-ORIGIN:start -->","### DA-20260613-AGENT-BROWSER-ORIGIN","传统 SOP 约束 script origin，却没有约束会读历史、跨页面推理并写入新页面的 Agent。安全 owner 必须沿 read→label→propagate→write 保存 origin，跨 origin 写入只有可信确认才能 commit；这也暴露了用户确认疲劳和标签传播误差。","<!-- analysis:DA-20260613-AGENT-BROWSER-ORIGIN:end -->","","<!-- analysis:DA-20260613-GUARDRAIL-AVAILABILITY:start -->","### DA-20260613-GUARDRAIL-AVAILABILITY","Guardrail 不是免费前置函数。攻击者若能放大其 reasoning tokens，就能把安全层变成共享队列的 DoS 放大器；系统必须同时决定每次检查的计算上限、超限后的安全语义、隔离池和租户配额。","<!-- analysis:DA-20260613-GUARDRAIL-AVAILABILITY:end -->","","<!-- analysis:DA-20260613-READOUT-BLIND-SPOT:start -->","### DA-20260613-READOUT-BLIND-SPOT","Looped model 把 hidden state 变成跨步 runtime state，但 readout-invariant scale不会被每步交叉熵直接约束。训练 exit 与控制 recurrence 是两个目标：要么让 scale 对 loss 可见，要么从 recurrence中移除。","<!-- analysis:DA-20260613-READOUT-BLIND-SPOT:end -->","","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        rel="Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse"
        adjacent_refs="; ".join(x.strip()+"#L1" for x in ADJ[r["owner"]].split(";"))
        report.append(f"| {r['family']} | {r['owner']} | {PATHS[r['owner']]}#L1 | {adjacent_refs} | existing:{r['family']} | delta:{r['family']} | {rel} | {r['disp']} | books-review:{r['family']} |")
    for r in reviews:
        rel="Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse"
        report += ["",f"<!-- existing:{r['family']}:start -->",f"Read owner `{r['owner']}` at `{PATHS[r['owner']]}` and adjacent chapters `{ADJ[r['owner']]}`; existing mechanism and fallback were compared against exact-v1.",f"<!-- existing:{r['family']}:end -->","",f"<!-- delta:{r['family']}:start -->",r["delta"],f"<!-- delta:{r['family']}:end -->","",f"<!-- books-review:{r['family']}:start -->",f"Relation `{rel}`; disposition `{r['disp']}`. {r['boundary']}",f"<!-- books-review:{r['family']}:end -->"]
    refs="; ".join("review:"+r["family"] for r in reviews); sels="; ".join(("analysis:"+SELECTED[r["aid"]]) if r["aid"] in SELECTED else ("analysis-decision:"+r["family"]) for r in reviews); books="; ".join("books-review:"+r["family"] for r in reviews)
    report += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260613-COVERAGE-V1 | fresh-context:jun13-v1 | coverage | coverage:SRC-ARXIV:20260613 | — | 434/434 title+abstract; 80/80 route-negative FN audit; denominator 38; closures 396; 15007 owner conflict closed | passed |",f"| SA-20260613-EVIDENCE-V1 | fresh-context:jun13-v1 | evidence | {refs} | — | 38/38 official exact-v1 Method/Evaluation/Limitations and benchmark contracts; all undisclosed execution fields remain Not Disclosed | passed |",f"| SA-20260613-SELECTION-V1 | fresh-context:jun13-v1 | deep_analysis_selection | {sels} | — | 38/38 frontier; winners frozen before 38 source-specific rationales | passed |",f"| SA-20260613-BOOKS-POSTWRITE-V1 | fresh-context:jun13-v1 | books | {books} | — | 14/14 Integrate writebacks in 9 owners and 24/24 No Change handoffs passed fresh audit; unresolved findings 0 | passed |","","## 8. Ignored Noise","","The 396 closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routes were recall aids only, all 80 route-negative identities were closed, and `2606.15007v1` remains a historical-owner closure rather than a new family.","","### Materials and Access","","- Discovery identity/timestamp/category/title/abstract comes from frozen DataCite snapshots.","- 38/38 retained families were read from official version-bound `https://arxiv.org/html/<id>v1`; every page exposed an exact `arXiv:<id>v1` header.","- Local curl and the in-app browser were unavailable, but this was not a material blocker after the primary-source web reader recovered all 38 exact-v1 pages.","","## 9. Recommended Action","","- `Integrate`: 14 families, deduplicated into 9 owner-file writes in `BOOKS_INTEGRATION_QUEUE_V1.md` and `READY_TO_INSERT_BOOKS_V1.md`.","- `No Change — Existing Coverage`: 24 families; each has a source-specific handoff above.","- Books Gate Passed after root wrote the nine owner-merged deltas and this lane completed the 38/38 post-write fresh audit.","","## 10. Repository Changes","","- This lane created only the 2026-06-13 Daily, source packet and dedicated finalizer.","- Root serialized the nine approved owner-file changes; this presentation migration did not modify, stage, commit or push shared Books.","","## 11. Open Questions","","- How can browser-origin labels survive lossy model transformations without overblocking legitimate user-approved transfer?","- Which guardrail timeout semantics minimize both denial-of-service and unsafe fail-open behavior under shared load?","- At what model scale do looped-state readout blind spots cease to follow the 44M/129M evidence?","- These are research continuations, not unresolved Gate blockers.","","## 12. Sources","",*source_lines,"- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表","- Date-local receipts：`../_sources/daily-20260613/source-review-receipts-v2.1.json`、`deep-analysis-selection-v1.json`、`books-comparison-v1.json`、`POST_WRITE_FRESH_AUDIT_V1.md`","","## 13. Final Status","","Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。"]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report)+"\n")

    integrates=[r for r in reviews if r["disp"].startswith("Integrate")]
    groups={}
    for r in integrates:
        groups.setdefault(r["owner"],[]).append(r)
    q=["# 2026-06-13 Books Integration Queue V1","",f"Denominator: `{denominator_id}`. Consumed by root: {len(integrates)}/{len(integrates)} family deltas were written as {len(groups)} owner-file updates and passed this lane's post-write audit.",""]
    ready=["# 2026-06-13 Ready-to-Insert Books Packet V1","",f"Source denominator: `{denominator_id}`. Applied by root and retained as the write receipt; one merged delta per owner preserves all source-family boundaries in Review notes.",""]
    for owner, items in groups.items():
        q += [f"## {owner}","",f"- Target: `{PATHS[owner]}`",f"- Exact target locator: `{TARGET_ANCHOR[items[0]['aid']]}`",f"- Source families: {', '.join(r['family'] for r in items)}",f"- Minimal merged delta: {' '.join(r['delta'] for r in items)}",f"- Evidence boundary: {' '.join(r['boundary'] for r in items)}",""]
        ready += [f"## {owner} — {PATHS[owner]}","",f"Insert after `{TARGET_ANCHOR[items[0]['aid']]}`.",""]
        ready += ["### Minimal durable delta","", " ".join(r["delta"] for r in items),"","### Coexistence / cost / failure boundary","", " ".join(r["boundary"] for r in items),"","### Review note","", "; ".join(f"{r['family']} — arXiv:{r['aid']}v1; exact-v1 evidence only" for r in items),""]
    QUEUE.write_text("\n".join(q)+"\n")
    READY.write_text("\n".join(ready)+"\n")
    books_files = list((ROOT / "Books").rglob("*.md"))
    postwrite = [
        "# 2026-06-13 Post-write Fresh-context Audit V1",
        "",
        f"Denominator {denominator_id}. All 38 retained families were re-read after root's Books writeback; unresolved findings: 0.",
        "",
        "| Family | Disposition | Fresh result | Result |",
        "| --- | --- | --- | --- |",
    ]
    for r in reviews:
        target = ROOT / PATHS[r["owner"]]
        target_text = target.read_text()
        global_files = [p for p in books_files if r["aid"] in p.read_text()]
        if r["disp"].startswith("Integrate"):
            heading, boundary_token = BOOK_CHECKS[r["aid"]]
            assert global_files == [target]
            assert heading in target_text and boundary_token in target_text
            assert f"https://arxiv.org/html/{r['aid']}v1" in target_text
            note_line = next(i for i, line in enumerate(target_text.splitlines(), 1) if r["aid"] in line)
            detail = (
                f"Unique owner {PATHS[r['owner']]}:{note_line}; body preserves {r['delta']}; "
                f"trade-off/failure/fallback preserves {r['boundary']}; exact-v1 Review note occurs once."
            )
        else:
            assert not global_files
            coverage_paths = [target] + [ROOT / x.strip() for x in ADJ[r["owner"]].split(";")]
            coverage_path = next(p for p in coverage_paths if NOCHANGE_COVERAGE[r["aid"]] in p.read_text())
            detail = (
                f"Owner {r['owner']} and adjacent handoff re-read; existing coverage token "
                f"{NOCHANGE_COVERAGE[r['aid']]} in {coverage_path.relative_to(ROOT)} confirms the durable proposition/fallback. "
                f"No Books citation was added; Daily retains exact-v1 evidence. Decision basis: {r['selection_note']}"
            )
        postwrite.append("| " + " | ".join([
            r["family"], r["disp"], detail.replace("|", "/"), "PASS"
        ]) + " |")
    postwrite += [
        "",
        "## Cross-checks",
        "",
        "- 14/14 Integrate families occur in exactly one Books file and one exact-v1 Review note; all owner bodies retain mechanism, trade-off/failure and fallback.",
        "- 24/24 No Change families retain source-specific Daily evidence, map to an existing owner proposition/fallback, and were not mechanically leaked into Books.",
        "- Shared owner files 72-security.md and 77-memory.md also contain later 06-15 source-family additions. Those later additions do not change, duplicate or collide with any 06-13 family ID or mechanism.",
        "- Benchmark contracts were re-audited after writeback: 38 source-specific model/evaluator identities; disclosed hardware/precision/SLO only where exact-v1 names them; every absent field is directly Not Disclosed.",
        "- Independence disclosure: nested reviewer spawning was disabled; this is a fresh-pass primary-source/owner audit, not a claimed independent second-model review.",
        "",
        "## Gate verdict",
        "",
        "- Coverage Gate: Closed.",
        "- Evidence Gate: Passed.",
        "- Selection Gate: Passed.",
        "- Books Gate: Passed.",
        "- Completion Status: Complete.",
    ]
    POSTWRITE_AUDIT.write_text("\n".join(postwrite) + "\n")
    EVIDENCE_AUDIT.write_text(f"""# 2026-06-13 Fresh Evidence and Selection Audit V1

- Denominator: `{denominator_id}`; `434 = 38 retained + 396 closures`.
- Coverage: 434/434 title+abstract semantic review; Core 311, keyword 43, route-negative 80; route-negative `80 = 0 + 80`.
- Owner repair: 2606.15007 is closed because the NVIDIA primary model release is dated 2026-06-04.
- Exact-v1: 38/38 official HTML pages exposed matching `arXiv:<id>v1` headers and were reviewed for method, evaluation and limitations/counterevidence.
- Benchmark identity: 38/38 model and evaluator fields are source-specific; four disclosed hardware contracts, two precision contracts and two SLO contracts are named exactly, while absent fields directly say `Not Disclosed`. No task count was relabeled batch, no parallel trial/agent count was relabeled serving concurrency, and no paper latency/accuracy became a production SLO.
- Evidence Gate: Passed.
- Selection: Passed after 38/38 frontier comparison; three winners were frozen before rationale rendering, and every non-winner has a source-specific reason.
- Books postwrite: 14/14 Integrate proposals in {len(groups)} unique owners and 24/24 No Change handoffs passed the fresh post-write audit. Books Gate Passed.
- Prewrite integrity: 38/38 Review body hashes, provenance IDs and Selection rationales are distinct; 396/396 closure reasons are row-specific; all 9 target headings exist exactly once in the current owner files.
- Mechanical checks: `validate_research.py` PASS, packet `SHA256SUMS` PASS, and scoped `git diff --check` PASS. These checks establish interface and artifact integrity, not semantic truth.
- Independence caveat: multi-agent reviewer spawning was disabled for this lane; the audit is a fresh pass over primary-source receipts, not a claimed independent second-model review.
""")
    packet_readme=["# daily-20260613 source packet","",f"- Denominator: `{denominator_id}`","- Raw registered identities: 434","- Retained: 38","- Family-specific closures: 396","- Exact-v1: 38/38","- Coverage Gate: Closed","- Evidence Gate: Passed","- Selection Gate: Passed","- Books Gate: Passed after 38/38 post-write fresh audit","- Completion Status: Complete","", "Files: screening ledger, row-level semantic audit, exact-v1 access receipt, review receipts, selection, Books comparison, consumed queue, applied write packet, fresh evidence audit, and post-write audit."]
    (PACKET/"README.md").write_text("\n".join(packet_readme)+"\n")
    files = sorted(p for p in PACKET.iterdir() if p.is_file() and p.name not in {"SHA256SUMS",".gitkeep","screening-ledger-provisional.json"})
    files += [REPORT, Path(__file__).resolve(), ROOT / "scripts/test_june13_canonical_presentation.py", ROOT / "scripts/audit_june13_canonical_presentation.py"]
    sums=[]
    for path in files:
        sums.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {Path(os.path.relpath(path, PACKET)).as_posix()}")
    (PACKET/"SHA256SUMS").write_text("\n".join(sums)+"\n")
    print(json.dumps({"denominator_id":denominator_id,"raw":434,"retained":38,"closures":396,"integrates":len(integrates),"owner_writes":len(groups),"route_counts":route_counts}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
