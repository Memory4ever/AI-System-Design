#!/usr/bin/env python3
"""Apply the bounded author repair requested by the post-write final review.

Scope is deliberately fixed to 14 false-negative closures, 191 owner-day
recovery identities, and two non-contract Books dispositions.  This script
does not edit Books.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/11/README.md"
LEDGER = SOURCE_DIR / "V3_SCREENING_LEDGER_20260914.json"
EVIDENCE = SOURCE_DIR / "V3_EVIDENCE_REVIEWS_20260914.json"
QUEUE = SOURCE_DIR / "V3_BOOKS_WRITEBACK_QUEUE_20260914.json"
OFFICIAL_BASIS = SOURCE_DIR / "V3_ORDINARY_RECOVERY_OFFICIAL_BASIS_20260915.json"
COMPARISON = SOURCE_DIR / "V3_POSTWRITE_AUTHOR_BOOKS_COMPARISON_20260915.json"
ROOT_QUEUE = SOURCE_DIR / "V3_POSTWRITE_AUTHOR_ROOT_QUEUE_20260915.md"
CHECKPOINT = SOURCE_DIR / "V3_POSTWRITE_AUTHOR_REPAIR_CHECKPOINT_20260915.md"

CHECKED_AT = "2026-09-15T23:20:00+08:00"
PUBLIC_EVENT = "2026-05-11T08:00:00+08:00 scheduled arXiv announcement"

OWNER_PATHS = {
    "MODEL-MOE": "books/part-02-model/21-moe.md",
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
}


def spec(score, owner, disposition, claim, mechanism, boundary, comparison, locators, artifact):
    return {
        "score": score,
        "owner": owner,
        "disposition": disposition,
        "claim": claim,
        "mechanism": mechanism,
        "boundary": boundary,
        "comparison": comparison,
        "locators": locators,
        "artifact": artifact,
    }


REOPEN = {
    "2605.06672": spec(
        (3, 2, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "Reasoning-model 的多选题位置偏差必须按 reasoning trajectory length 与 direct/CoT mode 分层，不能把随机换序后的单一平均值当作 order robustness。",
        "作者在 13 个 reasoning-mode 配置、MMLU/ARC-C/GPQA 上以 matched-pair PBS、partial correlation、commitment change point 与 truncation continuation probe 检查长度累积效应；12/13 配置在控制 accuracy 后仍呈正相关。",
        "证据限多选题、所测模型与可见 CoT；truncation continuation 是受控干预，不证明任意长推理都因同一机制变差。成本是每题多次换序和轨迹探测；非 MCQ、短轨迹或无法读 CoT 时回退普通顺序随机化、直接答案对照和外部 verifier。",
        "Ch66 已要求随机交换候选顺序并审计 judge position bias，却未把 examinee 自身的 position bias 与 reasoning length、direct/CoT mode 和 truncation probe 绑定为一个 evaluation slice；存在命题级增量。",
        ("§3 Method；§3.1 Matched-Pair Evaluation Protocol", "§4 Experimental Setup；§5 Results；Figure 1–4；Table 1–2", "§6 Discussion；Limitations；§7 Conclusion"),
        "not disclosed in exact-v1 for the adopted evaluation mechanism",
    ),
    "2605.06708": spec(
        (3, 3, 3), "MULTIMODAL-REPRESENTATION", "Integrate",
        "把文本渲染成图像进行长上下文压缩时，路由依据应是任务相关信息损失而不是 token compression ratio；precision、coverage 与高成本区域的再编码必须分别可见。",
        "论文把文本/视觉 token 表为经验测度，将 ViT patch encoder 写成 push-forward map，并把 transport cost 分解为 patch 内聚合的 precision cost 与跨 patch fragmentation 的 coverage cost；label-free probe 决定 text/visual path，foveation 对高成本区域提高分辨率。",
        "实验限 Qwen3-4B、24 个 NLP 数据集与作者渲染/阈值；label-free cost 仍可能错路由，foveation 在大规模下收益不均。视觉通道未校准、高风险逐字证据或版式漂移时回退原始文本与 source-linked region readback。",
        "Ch23 已说明 modality token budget 与共享容量，却没有把 visual-text compression 视为带 precision/coverage loss 的 modality transport，并据此形成可回退的 per-instance route；存在命题级增量。",
        ("§3 Method；§3.2 routing；§3.3 foveation", "§4 Experiments；§4.1–§4.3；Table 1–3", "Scope and limitations；Appendix G Limitations of Foveation at Scale"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.06865": spec(
        (3, 2, 3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
        "闭源模型的数据使用审计可以把 dataset-level statistical carrier 与黑盒生成输出的检测统计绑定，但检测只提供 provenance evidence，不等于逐样本或法律归因。",
        "作者随机选择 word pairs，以 rephrasing 提高 dataset 中的共现频率，再对目标模型生成文本的 pair co-occurrence 做统计检验；在多模型、三类 benchmark、partial contamination 与文本扰动下报告 p-value 和 utility。",
        "证明依赖随机 key、独立性/生成分布与特定 fine-tuning 设置；未命中不能证明未使用，命中也会受自然共现、后续训练和攻击影响。无法保守校准 FPR/功效时回退 lineage、controlled retraining、membership/dataset inference 组合证据与 Unknown。",
        "Ch72 已把 dataset usage inference / natural identifier、method version、observer capability、false-positive boundary 和 provenance non-authority 写成长期合同；Ch66 也已要求 contamination detector 在 scale/distribution 下重校准。该方法是现有命题的具体 carrier。",
        ("§2 Problem formulation；§4 Our method", "§5 Experiment；§5.1–§5.4；Table 1–4", "§6 Limitation；§7 Conclusion"),
        "no implementation repository disclosed in exact-v1",
    ),
    "2605.06892": spec(
        (3, 3, 2), "MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage",
        "连续 diffusion token 的收敛速度不同时，可以按 token group 分配异质 step budget，并让 active queries 读取同步的全局 KV、未激活 token 用缓存 velocity 前进。",
        "HSA 将时空 latent tokens 分组并给每组不同 step divisor；每步仅 active tokens 做 QKV，fresh K/V 覆盖 cache 后对全体 K/V attention，Cached Euler 用最近 velocity 更新全部 token；作者在 Wan-2.1/2.2 视频生成下比较质量与 runtime。",
        "stale K/V 与 cached velocity 会在敏感早晚阶段累积误差，分组策略和缓存窗口依赖模型/视频分布；论文未证明任意 DiT 或 production tail-SLO。漂移时回退全 token/full-step FM 或更保守固定 schedule。",
        "Ch24 已把不同 token 的收敛速度、token-local dynamic schedule、denoiser/KV-like cache、state/step identity、quality budget 与 full recompute fallback 写入同一主线；HSA 是连续视频 diffusion 的受限实现，不新增长期 owner。",
        ("§2 Method；Figure 1；§2.5 caching window", "§3 Experiments；§3.2–§3.3；Table 1；Figure 3–5", "§5 Conclusion；Appendix F Broader Impacts, Safeguards, and Licenses；作者模型/视频范围"),
        "project page disclosed: https://ernestchu.github.io/hsa ; no immutable implementation commit adopted",
    ),
    "2605.07114": spec(
        (2, 2, 2), "TRAIN-GRPO", "No Change — Existing Coverage",
        "固定总 rollout budget 下，group-based RLVR 应依据当前 prompt 至少再命中一次正确样本的后验效用分配额外 rollouts，而不是每题固定 group size。",
        "HORA 先取统一 G0 pre-rollouts，以 beta-binomial posterior 估计 hit utility，再优化第二阶段增量分配并生成 variable-size groups；reward evaluation 与 downstream group-relative estimator 保持不变。",
        "命中效用依赖二元可验证 reward、prior 与同一步样本；选择会改变 prompt distribution，且不证明更高 pass@K 等同训练收益。prior/能力漂移或 verifier 不可靠时回退固定 group、随机 coverage slice 与静态 curriculum。",
        "Ch33 已明确 group size 依赖当前成功率，并让 success rate、输出分歧和难度只拥有 rollout allocation proposal，保留 selection-bias 审计与固定 group fallback；HORA 是该既有命题的后验实现。",
        ("§3 Hit Utility and HORA；Algorithm 1", "§4 Experiments；§4.1–§4.2；Table 1；Figure 2–4", "§5 Conclusion and Discussion；Appendix A Limitations and Broader Impact"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07134": spec(
        (2, 2, 3), "AGENT-CONTEXT", "Integrate",
        "Web Agent 的观察压缩应保留页面功能区域与跨步 transition，而不是只截断 element-level AXTree；selector 必须提供可恢复的全页回退。",
        "Region4Web 把 AXTree 元素划分成功能区域并做 semantic abstraction；PageDigest 按任务选择区域、维护同页增量变化，并在选择不足时用 view_all 恢复。作者在 WebArena 812 tasks、四个 backbone 与两类 agent 方法上评估。",
        "功能分区、同页判定和 auxiliary selector 会受动态 DOM、隐藏状态、URL/页面迁移与模型错误影响；压缩不拥有页面真值。高风险操作、selector 不确定或页面 identity 变化时回退完整 AXTree/DOM 与重新观察。",
        "Ch75 有 source-linked bounded renderer、page/section selection 与 raw-artifact fallback，但没有将 Web observation 的 functional-region identity 和跨步 incremental digest 写入 Context contract；存在命题级增量。",
        ("§3.1 Problem Formulation；§3–§4 Region4Web / PageDigest", "§5 Experiments；§5.1–§5.2；Appendix C–G", "Appendix A Limitations and Future Work；Appendix B Broader Impacts"),
        "public implementation disclosed: https://github.com/kwondu/region4web ; exact-v1 does not freeze a commit",
    ),
    "2605.07164": spec(
        (3, 2, 2), "AGENT-MEMORY", "No Change — Existing Coverage",
        "Experience memory 的 serving policy 必须能在推理过程中决定是否、何时检索经验，不能把 initialization-only 或 always-on injection 当默认最优。",
        "ExpWeave/ExpWeaver 将 experience retrieval 交织进 decision process，以 prompting 或 GRPO policy 选择使用时点；作者在 ReasoningBank/SkillRL/G-Memory、ALFWorld/WebShop 上报告质量与检索次数。",
        "选择器会漏取关键经验或反复取回噪声，收益依赖 experience quality、task 和 agent；RL reward 也可能把少调用误当成功。低规模、关键经验必须可见或策略未校准时回退 global injection、无经验 baseline 或显式人工规则。",
        "Ch77 已直接要求按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，并联合 quality、prompt cost、latency 和 break-even；该论文不改变既有长期命题。",
        ("§3 ExpWeave / ExpWeaver；Figure 1", "§4.1–§4.3；§5.1；Figure 2–5；Table 1", "§5 Analysis and Discussions；Appendix A Limitations and Impact Statement"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07182": spec(
        (3, 2, 2), "INFER-SCHEDULING", "Integrate",
        "同一 elastic checkpoint 可暴露多个 nested submodel，但运行时仍须按 reasoning phase 单独选择 model slice，并把 slice、phase 与精度写入请求执行身份。",
        "Star Elastic 在一次 post-training 中沿 SSM/channel/MoE/FFN 轴训练 nested submodels，以 differentiable router、curriculum distillation 和 zero-shot extraction 形成多个预算点；推理在 thinking/answering phase 选择不同子模型，并扩展到 NVFP4/FP8。",
        "证据限 Nemotron Nano family、160B-token post-training 与作者 benchmark/H100-vLLM 测量；router/slice 可能随任务漂移，嵌套会耦合模型质量，跨 phase 切换还需要兼容 KV/state。无法验证 slice identity 或 crossover 时回退固定 parent / 独立 checkpoint。",
        "Ch56 管理 reasoning budget 与 mode routing，但没有表达一个 checkpoint 内的 architecture slice 可按 thinking/answering phase 切换，以及由此产生的 model/KV/precision identity；存在命题级增量。",
        ("§2.2 Elastic Formulation；Figure 2；Appendix F", "§4 Experiments；§4.1–§4.5；Table 1–3；Figure 1/3", "Conclusions；作者模型、硬件、量化与估算范围；无独立 Limitations 标题"),
        "related Megatron-LM/NeMo dependencies disclosed; no dedicated immutable Star Elastic artifact adopted",
    ),
    "2605.07234": spec(
        (2, 2, 2), "INFER-KV-CACHE", "No Change — Existing Coverage",
        "KV eviction utility 应同时观察 attention map、projected value 与 inter-head interaction，并把 head-local score 变为 layer/model-wide 可比较预算。",
        "LaProx 将 eviction 写成 output-aware layer-wise matrix-multiplication approximation，利用 attention 与 projected value 的乘积近似 token contribution，再生成全局可比 score 做 model-wide selection；作者在 LongBench/NIAH 19 datasets 上测质量与效率。",
        "矩阵近似与全局排序依赖模型、层、长上下文分布和 prefill-only compression，极端 budget 下仍有 silent quality loss；物理 layout/continuous batching 未证明。score 未校准时回退 recent window、head/layer heuristic 或 FullKV。",
        "Ch45 已把 utility eviction、per-layer surrogate、variable per-head cache、layer-wise heterogeneous budget、physical fragmentation 和 FullKV fallback 写入同一命题；LaProx 的 output-aware score 是具体实现。",
        ("§4 Methodology；Algorithm 1–2", "§5 Experiments；§5.1–§5.4；Figure 2–3；Table 1", "§6 Conclusion；Appendix E Limitations"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07238": spec(
        (3, 3, 3), "INFER-SCHEDULING", "No Change — Existing Coverage",
        "Workflow-DAG scheduler 应同时评价当前 assignment 与它为下游留下的 model residency、parent-output locality、prefix reuse 和 device reachability。",
        "FATE 以 CP-SAT-backed frontier planner、horizon-aware scoring、bounded multi-device shard execution 和 state-conditional cost，反复在 ready frontier 上做 post-decision planning；作者在 real-DAG 与 controlled prefix-reuse benchmark 上比较 makespan/P95。",
        "future-state cost 依赖可见 DAG、代价估计和有限 horizon，CP-SAT/多设备 shard 会增加控制开销；动态 Agent 边、fairness、故障和生产 tail 未证明。图或 state stale 时回退 myopic ready-queue、RR/HEFT 或 locality heuristic。",
        "Ch56 已把 workflow post-decision state、longest-remaining-path、downstream prefix reuse、migration/preemption cost 和 task aging 合并为 owner 命题，并保留 synthetic DAG/fairness/tail 边界；FATE 不新增长期知识。",
        ("§2 Problem Formulation；§3 Method；Algorithm 1", "§4 Experiments；§4.1–§4.3；Table 1–3；Figure 2", "§6 Limitations；§7 Conclusion；Appendix D.7 Broader Impacts"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07242": spec(
        (3, 3, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
        "Memory source 被删除、纠正或接口迁移后，repair 必须先隔离受影响 descendants，再只发布经过 predecessor-closure 验证的 successor。",
        "MemoRepair 先撤下 invalidated descendants，以 retained support 和 staged repaired predecessors 生成 successor，再把发布选择化为 maximum-weight predecessor closure 并用一次 s-t min-cut 求解；ToolBench/MemoryArena 实验假设完整 influence provenance。",
        "完整 provenance、repair operator 正确性和固定 scalarized cost 是强前提；撤下会降低可用性，外部 side effect 不可由 memory repair 撤销。链路不全时回退 quarantine、append-only evidence、全量重建或人工裁决。",
        "Ch77 已要求沿 ancestry 标记 descendants，把 memory/execution disposition 分离，做 dependency tracing、independent-support check、selective replay 和 predecessor-aware eviction；MemoRepair 是该既有 cascade-repair 命题的优化实例。",
        ("§2 Method；§2.1 Problem Setup；Algorithm 1", "§3 Experiments；§3.2–§3.4；Table 1–3；Figure 2", "§5 Limitations and Conclusion"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07260": spec(
        (3, 2, 3), "MODEL-MOE", "Integrate",
        "Top-k router score 不能被视为 route utility；冻结模型下的 matched-compute counterfactual routes 应成为诊断 fragile-token misrouting 的独立证据。",
        "作者对每个 token 比较标准 route 与 sampled equal-compute alternatives，以 verified reasoning trajectory 中 realized next-token probability 评分；在四个 MoE family 与多类 reasoning task 上观察 fragile tokens 的标准 route 与可达更优 route 分离，并做 final-layer router-only update。",
        "counterfactual 只覆盖采样到的 routes，realized-token probability 不是序列级或因果 utility，verified trajectory 又有选择偏差；在线枚举成本高。诊断应保持离线/受控，无法复现时回退标准 top-k、load/quality audit 与端到端 matched-compute evaluation。",
        "Ch21 已解释 router probability、load balance、variable-k 与 matched-compute gate，但没有保存 executed-only loss 导致的 counterfactual blind spot，也没有把 fragile-token route alternatives 作为 routing-quality audit；存在命题级增量。",
        ("§3 Method / Analysis Protocol；§3.1；Figure 1–2", "§4–§6；Table 1–4；router-only update on AIME/HMMT", "Limitations；§7 Conclusion；sampled-route / realized-token scope"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07313": spec(
        (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "Agent memory 的可扩展性声明必须条件化于 agent、memory interface、irrelevant-session scale 与 interaction budget，并报告 usable-scale boundary。",
        "协议固定 query evidence，只逐级加入未标注为任务证据的 irrelevant sessions，记录 agent-memory trajectories，并报告 budget-compliant reliability、P90 memory-call burden、failure-regime decomposition 与 reliability threshold breakdown onset。",
        "irrelevant-session 标注、固定 evidence、budget 与 threshold 都是评测构造；LongMemEval/LoCoMo 和受测 interface 不能代表开放生产 memory。它增加多尺度 rerun 成本；样本或调用日志不足时回退固定 snapshot，但必须收窄 scalability claim。",
        "Ch66 有 scale/distribution slice 与 budgeted evaluation，Ch77 有 construction/retrieval/reader decomposition，却都未将 evidence-preserving memory growth、tail call burden 和 usable-scale onset 组合成明确的 memory scalability contract；存在命题级增量。",
        ("§3 Scale-Conditioned Agent–Memory Evaluation；Figure 1", "§4 Experimental Setup；§5 Results；Table 1–2；Figure 2–4", "§6 Discussion and Limitations；§7 Conclusion"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
    "2605.07414": spec(
        (3, 3, 3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
        "Tool-calling T2I Agent 的安全面必须覆盖 individually benign steps 组合成 harmful output 的 orchestration-level attack，而不是只检查单轮 prompt。",
        "OrchJail 从成功 jailbreak tool-call traces 学习 prompt wording 与高风险 orchestration pattern 的关系，以多目标评分引导 fuzzing，在代表性 tool-calling T2I agents 上比较 attack success、图像 fidelity、query cost 与 defenses。",
        "这是 offensive search evidence，不证明覆盖所有工具链或能直接形成 production detector；target agent、image judge 与 defense 均会漂移，fuzzing 还可能产生真实有害内容。高风险环境应回退独立 reference monitor、cumulative intent gate、tool allowlist、sandbox 与人工复核。",
        "Ch72 已明确 Agent safety gate 要跨 benign-looking subtasks 保存 cumulative intent/state，并测试 decomposition graph 是否完成有害目标，也覆盖 cross-modal joint risk 与 multi-step tool-chain effects；OrchJail 是现有命题的 T2I 攻击实例。",
        ("§3 Threat Model；§4 Approach；§4.1–§4.1.4", "§5 Experiment；§5.1–§5.4；Table 1–4", "§3 Threat Model；§6 Conclusion；未提供完整 defense completeness 保证"),
        "no dedicated public implementation artifact disclosed in exact-v1",
    ),
}


QUEUE_PAYLOADS = {
    "2605.06672": (
        "Ch66 scorer / position-bias 段，在普通顺序随机化之后。",
        "多选题 evaluation 不能只随机一次选项顺序并汇总平均值；reasoning-capable model 还可能随可见推理轨迹增长累积位置偏差。EvalSpec 应同时冻结 option permutation、direct/CoT mode、trajectory-length slice 与 truncation-probe protocol，分别报告准确率和 Position Bias Score。这样能区分直接答案的 baseline bias 与长推理中新出现的 accumulated bias，却需要每题多次运行、轨迹解析和更高 token 成本，也只在多选题与披露模型上有受限证据。非 MCQ、短轨迹或 CoT 不可见时继续使用普通换序、直接答案对照和外部 verifier，不能把更长思考当成 order robustness 保证。 [受限证据：arXiv:2605.06672v1]",
    ),
    "2605.06708": (
        "Ch23 modality identity / token-budget 主线中，加入 visual-text compression route。",
        "把长文本渲染为图像能减少 decoder tokens，但 compression ratio 不是任务信息保真度。表示 owner 应把 visual encoder 写成带损失的 modality transport，分别记录 patch 内聚合造成的 precision cost、跨 patch fragmentation 造成的 coverage cost，并让 per-instance router 在 text/visual path 间选择；高成本区域可以提高分辨率重新编码。该分支用额外 probe、渲染版本和 foveation pass 换 token 减少，也会因版式、分辨率和任务变化静默错路由。高风险逐字证据、cost 未校准或 visual path 退化时回退原始文本和 source-linked region readback。 [受限证据：arXiv:2605.06708v1]",
    ),
    "2605.07134": (
        "Ch75 bounded renderer / structured selection 段，加入 Web functional-region identity。",
        "Web observation 只按 element-level AXTree 截断时，页面功能结构和跨步变化都保持隐式。Context renderer 可以先把同一页面的元素绑定成功能区域，再按 task 维护增量 PageDigest；selector 只产生可见区域 proposal，原始 AXTree/DOM 与页面 revision 仍是 authority，并提供 view_all / full re-observation 回退。它以 region partition、辅助模型和 transition bookkeeping 换较短 observation，却会在动态 DOM、隐藏状态、URL 迁移或错误同页判定下删掉关键控件。页面 identity 改变、高风险操作或 selector 不确定时必须回退完整观察。 [受限证据：arXiv:2605.07134v1]",
    ),
    "2605.07182": (
        "Ch56 reasoning-budget / model routing 主线中，加入 phase-scoped elastic slice。",
        "一个 checkpoint 暴露多个 nested submodel 时，预算控制不再只是生成多少 token，还包括 thinking 与 answering phase 各自执行哪个 architecture slice。Scheduler 应把 checkpoint revision、slice mask、phase、precision、KV/state compatibility 与切换 receipt 绑定；model router 只提出预算点，runtime 验证该 slice 可执行。它用一次 elastic post-training 和共享权重换多预算部署，却新增 slice interference、路由漂移、量化差异与 phase-switch 状态兼容问题。crossover 未校准、KV 不兼容或关键任务时回退固定 parent / 独立 checkpoint。 [受限证据：arXiv:2605.07182v1]",
    ),
    "2605.07260": (
        "Ch21 Router 的 quality/load 主线，在 matched-compute gate 前加入 counterfactual route audit。",
        "Top-k router 的高 score 只说明被选择，不证明该 route 对当前 token 最有用；标准 LM loss 也只观察 executed route。受控审计可冻结模型和 token，在相同 active-expert 预算下采样替代 routes，用 realized-token probability 与序列 outcome 分开比较，特别检查 fragile tokens 是否存在 router-reachable 的更优路径。这个 counterfactual 只覆盖采样集合，单 token 概率不是因果或序列级 utility，在线枚举也过于昂贵；因此它只拥有诊断和 router-update proposal，最终验收仍需端到端 matched-compute rerun。证据不足时回退标准 top-k、load balance 与质量回归。 [受限证据：arXiv:2605.07260v1]",
    ),
    "2605.07313": (
        "Ch66 memory / agent evaluation slice 中，加入 scale-conditioned usable boundary。",
        "固定 snapshot 的 memory accuracy 不能支持 scalable-memory claim。更可审计的协议应对每个 query 固定任务证据，只增加 irrelevant sessions，并把 agent revision、memory interface、scale ladder 与 interaction budget 绑定；同时报告 budget-compliant reliability、尾部 memory-call burden、wrong-within-budget / budget-exhaustion 分解和 usable-scale onset。它用多尺度重复运行与完整 trajectory logging 换取更真实的容量边界，但依赖 irrelevant-session 标注、阈值与 benchmark 构造。日志或样本不足时仍可报告固定 snapshot，只能明确收窄为该规模结果，不能外推长期可用性。 [受限证据：arXiv:2605.07313v1]",
    ),
}


LATER_SIGNALS = {
    "2605.06738": "later v2 official comment says substantial revision, new Combined Evidence Protocol, deployment evidence, and supersedes v1; outside this owner-day event and must be reviewed on its own event date",
    "2605.06772": "later v2 official comment says expanded experiments; outside this owner-day event and must be reviewed on its own event date",
    "2605.07210": "later v2 official comment says updated analysis, ablation, benchmark, and storage/latency isolation; outside this owner-day event and must be reviewed on its own event date",
    "2605.07527": "later v2 official comment says result errors were corrected; outside this owner-day event and must be reviewed on its own event date",
    "2605.07818": "later v2 official comment says the accelerator was enhanced by an adaptive-geometry method; outside this owner-day event and must be reviewed on its own event date",
    "2605.08051": "later v2 official comment says substantially revised; outside this owner-day event, while its astronomy-domain closure remains unchanged for exact-v1",
}


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def disposition_label(item, queue_status):
    disposition = item["books_disposition"]
    owner = item["owner"]
    path = item["owner_path"]
    rel = "../../../../" + path
    if disposition == "Integrate":
        status = queue_status.get(item["arxiv_id"], "")
        suffix = (
            "等待 root 串行写回"
            if status == "pending_root_serialized_books_writeback"
            else "已存在 Books 正文"
        )
        return f"整合：`{owner}`，[{Path(path).name}]({rel})；{suffix}"
    if disposition == "No Change — Existing Coverage":
        return f"已有覆盖：`{owner}`，[{Path(path).name}]({rel})"
    if disposition == "仅报告":
        return f"仅报告：`{owner}`；不改变长期知识"
    raise ValueError(f"unexpected disposition: {disposition}")


def main():
    ledger = load(LEDGER)
    evidence_doc = load(EVIDENCE)
    queue_doc = load(QUEUE)
    official_doc = load(OFFICIAL_BASIS)

    ledger_by_id = {item["arxiv_id"]: item for item in ledger["entries"]}
    evidence_by_id = {item["arxiv_id"]: item for item in evidence_doc["items"]}
    queue_by_id = {item["arxiv_id"]: item for item in queue_doc["items"]}
    official_by_id = {item["arxiv_id"]: item for item in official_doc["items"]}

    assert len(ledger_by_id) == 826
    assert len(evidence_by_id) == 60
    assert len(official_by_id) == 191
    assert set(REOPEN).isdisjoint(evidence_by_id)

    for arxiv_id, data in REOPEN.items():
        entry = ledger_by_id[arxiv_id]
        entry["v3_status"] = "retained"
        entry["withdrawal_signal"] = "none_on_official_abs_page_checked_2026-09-15; exact-v1 accessible"
        entry["reason"] = (
            "按 post-write fresh review 的精确清单重开；完整题名与摘要显示长期 AI System 增量："
            + data["claim"]
        )
        score = data["score"]
        evidence_by_id[arxiv_id] = {
            "arxiv_id": arxiv_id,
            "source_family_id": entry["source_family_id"],
            "title": entry["title"],
            "primary": f"https://arxiv.org/html/{arxiv_id}v1",
            "public_event": PUBLIC_EVENT,
            "review_depth": "deep" if sum(score) >= 7 or data["disposition"] == "Integrate" else "standard",
            "access_status": "accessible_exact_v1",
            "withdrawal_status": "not_withdrawn_on_official_abs_page_checked_2026-09-15",
            "score": {
                "design_delta": score[0],
                "system_reach": score[1],
                "durability": score[2],
                "total": sum(score),
            },
            "adopted_claim": data["claim"],
            "mechanism_and_evaluation": data["mechanism"],
            "non_proof_tradeoff_and_fallback": data["boundary"],
            "owner": data["owner"],
            "owner_path": OWNER_PATHS[data["owner"]],
            "books_disposition": data["disposition"],
            "books_comparison": data["comparison"],
            "evidence_locators": {
                "method": data["locators"][0],
                "evaluation": data["locators"][1],
                "limitations_and_non_proof": data["locators"][2],
            },
            "artifact_status": data["artifact"],
            "reviewed_at": CHECKED_AT,
        }

    for arxiv_id in ("2605.06755", "2605.06997"):
        evidence_by_id[arxiv_id]["books_disposition"] = "仅报告"
        evidence_by_id[arxiv_id]["books_comparison"] = (
            "现有正文已承载同一长期命题；本条只报告受限版本事实与上下文，不形成 Books 增量。"
        )
        evidence_by_id[arxiv_id]["reviewed_at"] = CHECKED_AT

    recovery_entries = [
        item
        for item in ledger["entries"]
        if item["receipt_route"] == "datacite_initial_created_owner_proxy"
    ]
    assert len(recovery_entries) == 191
    for entry in recovery_entries:
        arxiv_id = entry["arxiv_id"]
        basis = official_by_id[arxiv_id]
        entry["v3_status"] = "owner_event_recovery_closed"
        entry["exact_event_version"] = basis["exact_review_version"]
        entry["official_version_event_comment_basis_ref"] = (
            "V3_ORDINARY_RECOVERY_OFFICIAL_BASIS_20260915.json#" + arxiv_id
        )
        entry["owner_event_basis"] = basis["owner_event_basis"]
        entry["current_official_version_at_check"] = basis["current_version_at_check"]
        entry["official_comments_at_check"] = basis["official_comments_at_check"]
        entry["withdrawal_signal"] = "none_on_current_official_abs_page_checked_2026-09-15"
        if arxiv_id == "2605.07267":
            entry["v3_status"] = "official_withdrawal_closed"
            entry["withdrawal_signal"] = (
                "current official arXiv comment: withdrawn for privacy, permission, and attribution review"
            )
            entry["current_signal_assessment"] = (
                "withdrawal closes candidate, score, and Books eligibility; exact-v1 is not adopted"
            )
            entry["reason"] = (
                "官方当前 arXiv 页明确声明作者撤回，以复核 privacy、permission 与 attribution；"
                "按合同不入候选、不评分、不进 Books。"
            )
        elif arxiv_id in LATER_SIGNALS:
            entry["current_signal_assessment"] = LATER_SIGNALS[arxiv_id]
            entry["reason"] = (
                entry["reason"]
                + "；本窗采用 exact-v1 owner event。官方页另有后续修订信号，已逐项记录并明确归属后续事件日，"
                "不再断言其为 non-important revision。"
            )
        else:
            entry["current_signal_assessment"] = (
                "current official version/comment adds no concrete withdrawal, correction, security, "
                "or mechanism/evaluation change owned by this event; generic version/acceptance/page-count "
                "metadata is not an importance trigger"
            )
            entry["reason"] = (
                entry["reason"]
                + "；exact-v1、owner-date、current version/history 与 Comments 已逐项绑定；"
                "当前官方说明未给出属于本窗的撤回、纠错、安全或机制/评价变化。"
            )

    for arxiv_id, payload in QUEUE_PAYLOADS.items():
        item = evidence_by_id[arxiv_id]
        insertion_point, final_prose = payload
        queue_by_id[arxiv_id] = {
            "source_family_id": item["source_family_id"],
            "arxiv_id": arxiv_id,
            "owner": item["owner"],
            "target_path": item["owner_path"],
            "insertion_point": insertion_point,
            "final_prose": final_prose,
            "tradeoff_and_fallback": item["non_proof_tradeoff_and_fallback"],
            "evidence_boundary": (
                f"{item['primary']}；Method={item['evidence_locators']['method']}；"
                f"Evaluation={item['evidence_locators']['evaluation']}；"
                f"non-proof={item['evidence_locators']['limitations_and_non_proof']}；"
                f"Artifact={item['artifact_status']}。"
            ),
            "write_status": "pending_root_serialized_books_writeback",
        }

    items = [evidence_by_id[key] for key in sorted(evidence_by_id)]
    queue_items = [queue_by_id[key] for key in sorted(queue_by_id)]
    assert len(items) == 74
    assert len(queue_items) == 26
    assert all(item["access_status"].startswith("accessible_exact_v1") for item in items)
    assert all(
        item["score"]["design_delta"]
        + item["score"]["system_reach"]
        + item["score"]["durability"]
        == item["score"]["total"]
        for item in items
    )
    direct_retained = sum(
        item["receipt_route"] == "official_arxiv_oai_direct"
        and item["v3_status"] in {"retained", "retained_candidate"}
        for item in ledger["entries"]
    )
    direct_closed = sum(
        item["receipt_route"] == "official_arxiv_oai_direct"
        and item["v3_status"] == "pre_denominator_closed"
        for item in ledger["entries"]
    )
    recovery_closed = sum(
        item["receipt_route"] == "datacite_initial_created_owner_proxy"
        and item["v3_status"] in {"owner_event_recovery_closed", "official_withdrawal_closed"}
        for item in ledger["entries"]
    )
    assert (direct_retained, direct_closed, recovery_closed) == (74, 561, 191)
    dispositions = Counter(item["books_disposition"] for item in items)
    assert dispositions == Counter(
        {"Integrate": 26, "No Change — Existing Coverage": 46, "仅报告": 2}
    )
    pending = [
        item
        for item in queue_items
        if item["write_status"] == "pending_root_serialized_books_writeback"
    ]
    assert {item["arxiv_id"] for item in pending} == set(QUEUE_PAYLOADS)

    ledger["schema"] = "ai-system-design.v3-screening-ledger.postwrite-author-repair"
    ledger["summary"].pop("ordinary_revisions_excluded", None)
    ledger["summary"].update(
        {
            "owner_day_recovery_closed": 191,
            "retained_candidates": 74,
            "pre_denominator_closed_direct": 561,
            "withdrawn_removed": 1,
            "evidence_accessible_exact_v1": 74,
            "false_negatives_restored": 45,
            "books_integrate": 26,
            "books_no_change": 46,
            "books_report_only": 2,
            "books_applied": 20,
            "books_pending_root": 6,
        }
    )
    ledger["postwrite_author_repair"] = {
        "review_basis": "V3_FRESH_NONAUTHOR_POSTWRITE_FINAL_REVIEW_20260915.md",
        "reopened_false_negatives": sorted(REOPEN),
        "ordinary_recovery_official_basis": "V3_ORDINARY_RECOVERY_OFFICIAL_BASIS_20260915.json",
        "ordinary_recovery_count": 191,
        "current_withdrawal_closed": ["2605.07267"],
        "later_event_signals_not_owned_by_this_window": sorted(LATER_SIGNALS),
        "normalized_report_only_dispositions": ["2605.06755", "2605.06997"],
        "new_root_queue": sorted(QUEUE_PAYLOADS),
        "checked_at": CHECKED_AT,
        "state": "Ongoing; author cannot self-sign Complete",
    }

    dump(LEDGER, ledger)
    dump(
        EVIDENCE,
        {
            "schema": "ai-system-design.v3-evidence-review.postwrite-author-repair",
            "report_date": "2026-05-11",
            "reviewed_at": CHECKED_AT,
            "items": items,
        },
    )
    dump(
        QUEUE,
        {
            "schema": "ai-system-design.v3-books-writeback-queue.root-serialized",
            "report_date": "2026-05-11",
            "status": "20_applied_6_pending_root_writeback_then_fresh_review",
            "items": queue_items,
        },
    )
    dump(
        COMPARISON,
        {
            "schema": "ai-system-design.v3-postwrite-author-books-comparison",
            "report_date": "2026-05-11",
            "reviewed_at": CHECKED_AT,
            "scope": sorted(REOPEN),
            "items": [
                {
                    "arxiv_id": arxiv_id,
                    "source_family_id": evidence_by_id[arxiv_id]["source_family_id"],
                    "owner": evidence_by_id[arxiv_id]["owner"],
                    "owner_path": evidence_by_id[arxiv_id]["owner_path"],
                    "disposition": evidence_by_id[arxiv_id]["books_disposition"],
                    "adopted_claim": evidence_by_id[arxiv_id]["adopted_claim"],
                    "proposition_level_comparison": evidence_by_id[arxiv_id]["books_comparison"],
                }
                for arxiv_id in sorted(REOPEN)
            ],
        },
    )

    queue_status = {item["arxiv_id"]: item["write_status"] for item in queue_items}
    source_rows = [
        ("SRC-OPENAI", "Research 历史入口；动态列表无法稳定分页回到本窗", "受阻", "隔离：不支持全站零遗漏；取得本窗官方归档时才重开"),
        ("SRC-ANTHROPIC", "Research 历史列表；相邻公开事件 05-08 与 05-14", "已检查", "未见已列事件落窗；不扩张为全站证明"),
        ("SRC-GOOGLE-AI", "DeepMind/Google Research 本窗定点检查", "受阻", "历史列表缺日级稳定停止点；隔离"),
        ("SRC-META-AI", "Meta/FAIR publications 本窗定点检查", "受阻", "动态目录缺日级稳定分页；隔离"),
        ("SRC-QWEN", "Qwen 官方历史入口本窗定点检查", "受阻", "旧入口不能稳定回溯；隔离"),
        ("SRC-DEEPSEEK", "News/Research；相邻事件 04-24 与 05-14", "已检查", "未见本窗事件"),
        ("SRC-MOONSHOT", "Kimi Blog 与官方仓库本窗定点检查", "受阻", "无稳定历史日级发现页；隔离"),
        ("SRC-TENCENT-HUNYUAN", "Research‘全部’列表；相邻条目 04-30 与 05-21", "已检查", "未见本窗事件"),
        ("SRC-ZAI", "智谱 Research；相邻条目 04-29 与 05-20", "已检查", "未见本窗事件"),
        ("SRC-BYTEDANCE-SEED", "Seed Research/Publication 与 arXiv identity 交叉检查", "已检查", "目录回填日不替代首次公开"),
        ("SRC-BAIDU-ERNIE", "ERNIE Blog；相邻事件 05-09 08:00+08", "已检查", "早于本窗，不重复"),
        ("SRC-XIAOMI-MIMO", "MiMo Papers 与 Blog 历史入口", "受阻", "Papers 可排除；Blog 缺稳定历史时刻；隔离"),
        ("SRC-MINIMAX", "Research/Blog；相邻事件 03-18 与 05-26", "已检查", "未见本窗事件"),
        ("SRC-ARXIV", "冻结 826 identity：635 official-announcement direct + 191 owner-day recovery；191/191 已绑定官方 abs version/history/Comments；74 candidate exact-v1 Evidence Review", "已检查", "1 项 current withdrawal 已关闭；6 项 later revision signal 归属后续事件日，不冒充本窗 revision"),
    ]
    report = [
        "# Daily Research — 2026-05-11",
        "",
        "**规范：** V3",
        "**窗口：** 2026-05-10T09:00:00+08:00 ～ 2026-05-11T09:00:00+08:00",
        "**状态：** 进行中",
        "**Books：** 纳入本次",
        f"**检查时间：** {CHECKED_AT}",
        "",
        "## 1. 结论",
        "",
        "本轮只处理 post-write fresh review 点名的三组失败项，没有扩窗、扩来源或扩大冻结的 826 identity 分母。14 个 false-negative closure 经完整题名/摘要、exact-v1 locator、withdrawal 与当前 Books owner 对照后全部进入候选；direct 算术更新为 635 = 74 candidate + 561 pre-denominator closure。",
        "",
        "191 个 DataCite owner-day recovery 已逐项绑定官方 arXiv exact-v1、current version、submission history 与 Comments。它们不再被笼统称作‘无重要修订’：`2605.07267` 依据当前官方撤回声明关闭；6 个明确后续修订/纠错信号被记录为后续事件日责任，其余只在 official comment 未给出具体机制、评价、纠错、安全或撤回变化的窄意义上关闭。本轮未重筛或扩张这 191 项。",
        "",
        "当前 74 个候选均有 exact-v1 Evidence Review；Books 判断为 26 Integrate、46 No Change、2 仅报告。原有 20 个 Integrate 已写入 Books；新增 6 个 Integrate 只生成 root 队列，本作者未编辑 Books。`2605.06755`、`2605.06997` 已从非合同 `Weekly Only — Context` 统一为合同内‘仅报告’。Daily 保持进行中，等待 root 写回与新的非作者 fresh-context reviewer。",
        "",
        "## 2. 来源覆盖",
        "",
        "本轮沿用冻结来源与窗口，只返修点名项目；下列 coverage 不构成新的全量来源重放。",
        "",
        "| 来源 | 检查范围与依据 | 结果 | 缺口 |",
        "| --- | --- | --- | --- |",
    ]
    report.extend(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in source_rows)
    report += [
        "",
        "## 3. 候选与判断",
        "",
        "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in items:
        score = item["score"]
        report.append(
            f"| [{item['title']}]({item['primary']}) | 2026-05-11T08:00:00+08:00 | "
            f"{item['adopted_claim']}；{score['design_delta']} + {score['system_reach']} + "
            f"{score['durability']} = {score['total']} | "
            f"{'深入完成' if item['review_depth'] == 'deep' else '标准完成'} | "
            f"{disposition_label(item, queue_status)} |"
        )
    report += [
        "",
        "## 4. 证据与知识整合",
        "",
        "详细筛选理由见 [screening ledger](../_sources/daily-20260511/V3_SCREENING_LEDGER_20260914.json)，逐项证据见 [Evidence reviews](../_sources/daily-20260511/V3_EVIDENCE_REVIEWS_20260914.json)，本轮 14 项 Books 对照见 [post-write comparison](../_sources/daily-20260511/V3_POSTWRITE_AUTHOR_BOOKS_COMPARISON_20260915.json)，191 项版本/日期/Comments 依据见 [official basis](../_sources/daily-20260511/V3_ORDINARY_RECOVERY_OFFICIAL_BASIS_20260915.json)。",
        "",
    ]
    for item in items:
        locators = item["evidence_locators"]
        report += [
            f"### [{item['title']}]({item['primary']})",
            "",
            f"**采用命题：** {item['adopted_claim']}",
            "",
            f"**机制与评价：** {item['mechanism_and_evaluation']}",
            "",
            f"**证据位置：** Method：{locators['method']}；Evaluation：{locators['evaluation']}；Limitations / non-proof：{locators['limitations_and_non_proof']}。Artifact：{item['artifact_status']}。",
            "",
            f"**未证明、代价与回退：** {item['non_proof_tradeoff_and_fallback']}",
            "",
            f"**Books 比较：** {item['books_comparison']}",
            "",
            f"**最终处置：** {disposition_label(item, queue_status)}。",
            "",
        ]
    report += [
        "## 5. 缺口与下一步",
        "",
        "本次有界作者返修已完成，但 Complete Gate 尚未满足：",
        "",
        "1. root 按目标文件冲突顺序写入 `2605.06672`、`2605.06708`、`2605.07134`、`2605.07182`、`2605.07260`、`2605.07313` 六个 queue item；本作者不编辑 Books。",
        "2. 后续事件日 owner 分别处理 `2605.06738`、`2605.06772`、`2605.07210`、`2605.07527`、`2605.07818`、`2605.08051` 的官方后续修订信号；它们不计作 2026-05-11 的新 revision event。",
        "3. root 写回后由未参与本轮返修的新 reviewer 做 fresh-context 终审，复核 826 = 74 + 561 + 191、14 项 Evidence/Books 判断、191 项 official basis、2 项仅报告枚举与 26 项实际 Books 状态。",
        "",
        "## 6. 复核",
        "",
        "**复核者：** 等待新的非作者 reviewer（本次作者不能自签）",
        "",
        "**结论：** 未通过 Complete Gate（有界作者返修完成；等待 6 项 root 写回与 fresh review）",
        "",
        "机器校验只能证明 JSON、评分、分母算术、版本 basis 引用、唯一 owner、链接字段与 Markdown 结构一致；不能替代 Books 写回或独立语义复核。",
        "",
        "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews 与 root queue；新增 191 项 official basis、本轮 comparison、root synthesis、提取脚本和 author checkpoint。未编辑 Books，未 stage、commit 或 push。",
        "",
    ]
    REPORT.write_text("\n".join(report))

    ROOT_QUEUE.write_text(
        "\n".join(
            [
                "# 2026-05-11 post-write 作者返修：root Books 队列",
                "",
                "本文件只汇总新增六项；权威 prose、位置与 evidence boundary 位于 `V3_BOOKS_WRITEBACK_QUEUE_20260914.json`。",
                "",
                *[
                    f"- `{arxiv_id}` → `{evidence_by_id[arxiv_id]['owner']}` / `{evidence_by_id[arxiv_id]['owner_path']}`：{QUEUE_PAYLOADS[arxiv_id][0]}"
                    for arxiv_id in sorted(QUEUE_PAYLOADS)
                ],
                "",
                "作者侧未编辑 Books。root 写回后仍需新的非作者 fresh-context reviewer；当前 Daily 必须保持 Ongoing。",
                "",
            ]
        )
    )
    CHECKPOINT.write_text(
        "\n".join(
            [
                "# 2026-05-11 post-write 有界作者返修 checkpoint",
                "",
                f"- checked at: {CHECKED_AT}",
                "- scope: 14 false-negative closures + 191 owner-day recovery official basis + 2 non-contract dispositions；未扩窗/扩源/扩分母",
                "- denominator: 826 = 74 candidates + 561 direct closures + 191 owner-day recovery closures",
                "- 14 FN: 14/14 title+abstract semantic review、exact-v1 locators、withdrawal、Evidence 与 Books Decision 完成",
                "- 191 basis: 191/191 official arXiv current version、submission history、Comments 与 owner-date receipt 已绑定",
                "- current withdrawal: 2605.07267 依官方声明关闭；不评分、不进 Books",
                "- later signals: 2605.06738 / 06772 / 07210 / 07527 / 07818 / 08051 明确归属后续事件日",
                "- disposition: 26 Integrate / 46 No Change / 2 仅报告",
                "- Books: 20 已写入 / 6 pending root；本作者未编辑 Books",
                "- normalized: 2605.06755 / 2605.06997 → 仅报告",
                "- state: Ongoing；作者不自签，等待 root 写回与新的非作者 fresh review",
                "",
            ]
        )
    )


if __name__ == "__main__":
    main()
