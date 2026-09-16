#!/usr/bin/env python3
"""Close the remaining 2026-05-07 author-side exact-v1 review work.

This script only rewrites date-owned report/evidence artifacts.  Shared Books,
month indexes and LEARNING_STATE remain root-owned.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "07" / "README.md"
PACKET = ROOT / "exact-v1-review-packet-v3-author-repair.json"
LEDGER = ROOT / "screening-ledger-v3-author-repair.json"

REVIEWS = {
"2605.04808": dict(method=("§3.1–3.2；§4.2", "DTap 将风险 policy、模拟工具环境、victim agent 与可验证 effect judge 分开；DTap-Red 从 policy 推导恶意目标并组合 prompt/tool/skill/environment 注入。"), evaluation=("§6.1–6.3；Appendix A–P", "14 个领域、50 余模拟环境，2,503 个 direct/indirect tasks，覆盖四类 agent framework 与披露 backbone；matched attack generator 的高 ASR 是受控上界。"), limitations=("§3.1；§6.1；§7", "环境与 judge 均为作者模拟/实现；100% ASR 来自 GPT-5.1+OpenAI Agents SDK 的匹配生成设置，不是生产攻击率，也不证明所有真实工具副作用被复现。"), score=(2,2,2), disposition="已有覆盖", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="Ch66 已要求冻结环境 revision、真实 transition/effect receipt，并把模拟器与 judge 限定为测量工具；本材料补充实例但不改变该命题。"),
"2605.04830": dict(method=("§1.1；§3.1–3.5", "用 conditional/unconditional score gap 诊断 symmetry breaking，用 global/截断局部 score gap 诊断 nonlocality，再以 forward-backward 与时间窗切换检验最终样本影响。"), evaluation=("§3；Appendix C", "ImageNet DiT-XL 与 SD3-medium，在披露 sampler/noise levels 下比较 instantaneous 与 integrated probes；SD3 window 实验因成本仅 62 个样本。"), limitations=("Appendix D", "只覆盖两个 DiT 系统；截断 attention 只是近似 local denoiser；并发 critical windows 是经验观察，不是普适定理。"), score=(2,1,2), disposition="整合", owner="MULTIMODAL-GENERATIVE-PARADIGMS", chapter="../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", comparison="Ch24 已比较 factorization、correction 与 commit，但缺少按生成时间识别 conditioning/global communication 何时真正 load-bearing 的诊断分支；需最小补写。"),
"2605.04897": dict(method=("§2–3", "六层 retrieval-centered pipeline 保留 verbatim events，再在 ingestion、post-ingestion 与 query-time 分阶段检索；SQLite/CPU 是实现选择而非 memory 定义。"), evaluation=("§4；Tables 1–3", "LoCoMo、LongMemEval、BEAM-1M 使用统一 harness、top-k window 与 gpt-4o-mini 三次多数 judge；LoCoMo 另做 56 配置检索消融。"), limitations=("Limitations", "所有 benchmark 都关闭 encoding gate；未验证数周/月真实历史；semantic-match judge 比 strict match 宽松，绝对分数不可直接跨论文比较。"), score=(2,1,2), disposition="已有覆盖", owner="AGENT-MEMORY", chapter="../../../../books/part-07-agent/77-memory.md", comparison="Ch77 已把 immutable episode、derived view、retriever 与 truth authority 分离，并明确保存不等于可召回；本架构是受限实现案例。"),
"2605.04901": dict(method=("§4", "攻击者跨查询对齐 shuffled intermediate activations，消去 permutation ambiguity 后逐层恢复暴露路径上的权重。"), evaluation=("§5.1–5.3", "在 Pythia-70M/GPT-2 及论文两种暴露设置上报告表示对齐与权重恢复误差；private-matmul 变体的 Wqk 恢复仍未解决。"), limitations=("Limitations", "只在小模型验证，规模增大时恢复精度下降；不覆盖所有 secure-inference 协议、side channel 或生产攻击预算。"), score=(3,2,2), disposition="整合", owner="PLATFORM-SECURITY", chapter="../../../../books/part-06-ai-infrastructure/72-security.md", comparison="Ch72 已有该 exact-v1 的 semantic-body binding，明确 permutation 不是 confidentiality proof，并保留小模型/查询预算边界；无需新增正文。"),
"2605.04913": dict(method=("§3–4", "在 midpoint 截断 task gradient：后半段学习任务，前半段以 bottleneck 重建 stop-gradient 输入 embedding；先更新前部再重算并 detach boundary activation。"), evaluation=("§5–6", "在披露的 4B–8B SFT/GRPO 设置中比较质量、显存和 policy-update 时间，并以 32B 做可扩展性检查；k=2/k=4 是有限切分消融。"), limitations=("§6；Appendix", "feature reconstruction 只约束接口兼容，不保证保留全部下游信息；额外 forward、midpoint 选择与跨层协同可能抵消收益。"), score=(2,2,2), disposition="整合", owner="TRAIN-RLHF", chapter="../../../../books/part-04-training-system/31-rlhf.md", comparison="Ch31 已写 midpoint、两阶段更新、stale boundary 与完整 backprop fallback，并有该 family marker；无需新增正文。"),
"2605.04920": dict(method=("§3", "将组合任务的监督从 token imitation 改为 outcome-level GRPO，并比较 binary 与 composite reward，直接检验训练组合到未见组合的迁移。"), evaluation=("§4–5", "四个 compositional benchmark、两个模型，SFT/GRPO 与 reward 变体对照；总体 binary reward 接近 composite，而困难 split 上存在互补差异。"), limitations=("§6", "证据限四个构造任务和简单 reward family；RL 计算更高，结果不证明 outcome reward 普遍优于过程监督。"), score=(2,1,2), disposition="已有覆盖", owner="TRAIN-GRPO", chapter="../../../../books/part-04-training-system/33-grpo.md", comparison="Ch33 已按 outcome 可验证性、credit horizon 与 execution replay 讨论何时选择 terminal/group reward；该结果未改变现有条件分支。"),
"2605.04956": dict(method=("§3–4", "KernelBenchX 将 kernel 任务按 15 类组织，用两阶段 correctness filter 排除随机碰巧通过，再在相同语义门后测硬件效率与 portability。"), evaluation=("§5–6", "176 个任务、六类 GPU、五种生成/修复方法；区分 compile、correctness、speedup 与跨架构表现，并观察迭代修复提高正确率却可能降低性能。"), limitations=("§6–7", "这是作者 benchmark 与给定 toolchains/models 的结果；不能把 microbenchmark speedup 外推端到端模型，也不证明测试覆盖等于形式正确。"), score=(3,2,2), disposition="整合", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="Ch66 已有 kernel interface gate，但缺少 compile→semantic correctness→hardware efficiency→portability 四段失败分类及 repair trade-off；owner 从执行引擎纠正为 Evaluation。"),
"2605.04971": dict(method=("§3–5", "把跨层 representation geometry 分解为 residual 引起的 gradient coherence 与非线性引起的 rotational symmetry breaking；用 rotation-equivariant 非线性构造反例。"), evaluation=("§6；Appendix", "toy MLP 多 seed、小型 34M Transformer 单 seed与若干预训练模型表征统计；前者检验机制，后者只观察几何模式。"), limitations=("§6–7", "小模型和受控任务不能证明大模型训练的因果动力学；预训练快照上的相关几何不等于训练期机制。"), score=(2,1,2), disposition="整合", owner="MODEL-TRANSFORMER-LAYER", chapter="../../../../books/part-02-model/17-transformer-layer.md", comparison="Ch17 分别解释 residual 与 nonlinearity，但缺少二者对跨层方向连续性的分工和 rotation-equivariant 反例；需窄化补写而非宣称普适几何定律。"),
"2605.04972": dict(method=("§3", "在同一主观任务中分别改变 expert identity、样本、时间与评价维度，并比较 prompting、fine-tuning 与 weight edit 是否吸收专家判断。"), evaluation=("§4–5", "九名专家、一个任务、一个 base model 和披露对齐方法；criteria/rationale 的加入并未稳定改善所有维度。"), limitations=("§6", "单任务、九专家、单模型/编辑方法；disagreement 可能来自真实价值差异，不能把少数意见当模型错误或通用 alignment failure。"), score=(2,1,2), disposition="已有覆盖", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="Ch66/Ch31 已把 rubric、rater identity、disagreement 与 release authority 分离；该小样本结果只提供受限反例。"),
"2605.04984": dict(method=("§3", "从每个 turn state 采样 future answers，按语义聚类形成 outcome-potential distribution，以 reliability-weighted cluster mass 的相邻差分生成 turn reward。"), evaluation=("§4", "Qwen3-4B/8B 在七个 search-QA benchmark 上比较 outcome、turn credit 与组件消融；训练不使用 gold verifier，但可靠性/聚类器仍是代理。"), limitations=("§5–6", "只覆盖有可聚类短答案的 search QA；开放代码/长 artifact 没有稳定 outcome identity，self-induced reliability 可能共享模型偏差。"), score=(2,1,2), disposition="整合", owner="TRAIN-RLHF", chapter="../../../../books/part-04-training-system/31-rlhf.md", comparison="Ch31 已写 outcome-potential、语义 cluster、可靠性代理和 terminal/execution fallback，并绑定该 family；无需新增正文。"),
"2605.04992": dict(method=("§3", "NeWTral 在 paired unsafe/safe adapters 上训练 layer-wise/MoE weight translator，将新 unsafe adapter 映射到较安全的 aligned adapter。"), evaluation=("§4–5", "八个技术域、最高 72B 模型，联合比较 safety 与 utility；zero-shot 指新 adapter 的部署映射，不代表 translator 从未使用安全数据。"), limitations=("§6", "不能消除全部 unsafe output；结构新颖域的泛化未证，训练依赖 paired adapters 与 safety data，repair 还可能损伤能力。"), score=(3,2,2), disposition="整合", owner="PLATFORM-SECURITY", chapter="../../../../books/part-06-ai-infrastructure/72-security.md", comparison="Ch72 已将 weight-space repair 定义为带 regression/rollback 的发布分支，并有该 family marker；无需新增正文。"),
"2605.04995": dict(method=("§2–5", "在 ReLU realizability 约束下构造四类任务，分别展示 adaptivity 优势保持、消失、出现或反转，分离查询策略与表示可实现性。"), evaluation=("理论构造与证明", "结论来自四个显式函数族/查询模型的近似界，不是 agent benchmark 或生产 tool-use 实验。"), limitations=("§6", "构造只说明 adaptivity 与 realizability 没有单调关系；不提供开放环境中的成本、噪声、工具副作用或模型选择结论。"), score=(2,1,2), disposition="已有覆盖", owner="AGENT-PLANNING", chapter="../../../../books/part-07-agent/79-planning.md", comparison="Ch79 已把 adaptive search 设为有观测价值、预算与 verifier 条件的分支，并保留 static plan；理论构造强化边界但不改变 owner 结论。"),
"2605.05003": dict(method=("§3", "把 reward model 在 bias、safety、morality 与 ethical reasoning 上的 pairwise preference 分开测，比较 criteria 与 context faithfulness 的冲突。"), evaluation=("§4–5", "五个公开 reward models 与两个 instruct proxies；部分数据是定向构造诊断，不是客观 correctness gold，也不测下游 policy。"), limitations=("Limitations", "英语与来源规范有限，社会价值标签依赖语境/人群；reward preference 不能直接推出部署行为或内部机制。"), score=(2,1,2), disposition="已有覆盖", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="Ch66/Ch31 已要求 rubric/rater/domain 版本化并禁止 scalar reward 取得 truth authority；无新增长期机制。"),
"2605.05007": dict(method=("§3–4", "单一 causal orchestrator 联合决定是否分解、分解深度及 worker/model+primitive 路由；SFT 后用 verifier-gated Agentic-GRPO 学习选择性委派。"), evaluation=("§5", "22 个 baseline、13 个 benchmark，联合报告准确率与成本；worker catalog、API 能力与价格是实验快照。"), limitations=("§6", "单 orchestrator 与固定 worker 集不证明任意多 Agent 拓扑收益；API 漂移、共享工具状态、权限和副作用未由 benchmark 解决。"), score=(2,2,2), disposition="整合", owner="AGENT-MULTI-AGENT", chapter="../../../../books/part-07-agent/82-multi-agent.md", comparison="Ch82 已有该 family 的选择性 delegation 段，保存 single-agent baseline、router 误判与权限/验证边界；无需新增正文。"),
"2605.05026": dict(method=("§3–4", "以生成轨迹的 local intrinsic dimension 作为结构不稳定 proxy，并用 intrinsic-quality correction 抑制 LID 虚高。"), evaluation=("§5", "toy/image datasets、作者 diffusion models 与人评比较 structural hallucination；结果绑定所选 estimator、采样与视觉标签。"), limitations=("§6", "结构幻觉定义与人评主观，LID 是相关诊断而非因果或事实 verifier；质量、diversity 与 correction 的权衡尚未闭合。"), score=(2,1,2), disposition="仅报告", owner="MULTIMODAL-GENERATIVE-PARADIGMS", chapter="../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", comparison="受限 detector/correction 案例未改变 Ch24 的 factorization、state 与 commit 主线；保留日报证据，不新增正文。"),
"2605.05058": dict(method=("§III", "Security Cube 将 jailbreak robustness 拆成 attacker、defender、judge 三轴，并为 attack/defense/judge family 建立组合评价。"), evaluation=("§IV", "13 attacks、5 defenses、4 judges 及披露模型配置；排名与 ASR 只对相应组合有效。"), limitations=("§V", "SoK/作者实验是 2023–2025 方法快照；选择的攻击、防御与 judge 不能穷尽开放威胁，也不能证明单一配置生产安全。"), score=(2,1,2), disposition="已有覆盖", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="Ch66/Ch72 已要求 threat model、attack、defense、judge、model 和 effect receipt 分权记录；taxonomy 不构成额外机制 owner。"),
"2605.05066": dict(method=("§2–6；Theorems", "在 OSP 抽象下证明长序列系统不能同时保持长度无关的单步计算、固定有限状态与随历史增长的精确随机关联召回；容量通过有限精度信息量进入下界。"), evaluation=("§7", "d=64、2-layer 的 synthetic associative recall 五组实验用于检验边界趋势；52 架构分类只是渐近性质映射，不是统一 benchmark。"), limitations=("§8.4", "经验规模很小且任务为 worst-case random KV；常数、近似召回、分布结构和更强压缩可能改变实际 operating point，不否定 workload-specific architecture。"), score=(3,2,3), disposition="整合", owner="MODEL-LONG-CONTEXT", chapter="../../../../books/part-02-model/22-long-context.md", comparison="Ch22 已列 KV、固定状态与检索分支，但缺少三者不可同时无代价成立的统一 capacity trade-off；需作为边界定理写入而非架构排名。"),
"2605.05090": dict(method=("§3", "对 base/intervention model 生成配对响应，先提出自然语言 side-effect 假设，再用独立 discriminative validation、对照与 FDR 筛选。"), evaluation=("§4–5", "先在已知合成行为验证召回，再覆盖 reasoning distillation、ROME editing 与 unlearning interventions；测的是发现/验证协议而非实时监控。"), limitations=("Limitations", "发现依赖 prompt bank，稀有/对抗性行为会漏检；discriminator/model shared bias 与计算成本限制开放分布结论。"), score=(3,2,2), disposition="整合", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="Ch66 已将 intervention side-effect、paired slices、对照 artifact 与 rollback 写入 release gate，并绑定该 family；无需新增正文。"),
"2605.05103": dict(method=("§2", "将语料句向量 delta 拟合为局部 Gaussian concept field，用相对场的 z-distance 量生成文本对语料概念轨迹的偏离。"), evaluation=("§3–4", "在 CFR groundedness、Gutenberg novelty 与受控 LLM rewrites 上比较分离能力；该量依赖 embedding、corpus 和局部校准。"), limitations=("§5", "corpus-attributable drift 不等于事实错误；黑盒可追溯性不消除 domain/embedding bias，也未给跨语料稳定阈值。"), score=(2,1,2), disposition="仅报告", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="这是特定表示空间的 detector，不改变 Ch66 已有 grounding/evidence authority；不把语料距离升级为真值判断。"),
"2605.05115": dict(method=("§3–4", "分别拟合 activation 与 behavior manifold，用 pullback metric 求 geodesic intervention，并与线性 activation steering 比较路径偏离。"), evaluation=("§5", "简单语言属性任务与一个 Mountain Car recurrent world-model 案例；只验证受控概念/小模型上的路径差异。"), limitations=("§6", "依赖可拟合低维 manifold 与 chosen behavior metric；简单任务不证明大模型复杂能力的通用安全 steering。"), score=(2,1,2), disposition="仅报告", owner="MODEL-TRANSFORMER-LAYER", chapter="../../../../books/part-02-model/17-transformer-layer.md", comparison="受限 representation-control 案例，没有足够证据改写 Ch17 的层级机制；原 owner 从 Self-Attention 收窄为 Transformer Layer，但不写 Books。"),
"2605.05134": dict(method=("§3", "分别拟合 correct/hallucinated token-embedding dynamics 的 Koopman transition，以 differential residual 和小量标注校准单次输出阈值。"), evaluation=("§4", "在 HaluEval 等披露数据/模型上比较检测 AUROC/成本；需要训练期 regime labels 与可得 embedding。"), limitations=("§5", "只能检测不能纠正；阈值、embedding 与域迁移决定 false positives，单次低 residual 不构成 factuality guarantee。"), score=(2,1,2), disposition="仅报告", owner="PLATFORM-EVALUATION-SYSTEM", chapter="../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", comparison="特定 hallucination sensor 未改变 Ch66 对外部 evidence、校准与 abstention 的长期结论；不进入正文。"),
"2605.05138": dict(method=("§3", "Agent 从 action/observation history 编写可执行 Python world model，用已见 transition 回放验证并修订，再在模型上 rollout 计划。"), evaluation=("§4", "ARC-AGI-3 的 25 个公开游戏，主要每局一次 fresh run，解出 7 个且 RHAE 分布不均；私有游戏和跨环境泛化未测。"), limitations=("§5", "scripted controller/fixed API 与公开环境可能形成 harness-specific prior；通过历史 transition 不证明未来模型正确，代码执行还新增 sandbox 风险。"), score=(2,2,2), disposition="整合", owner="MULTIMODAL-WORLD-MODELS", chapter="../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md", comparison="Ch25 已讨论 latent dynamics 与 planning coupling，但缺少可执行、可反证 world hypothesis 作为 symbolic branch 及其 sandbox/overfit 边界；需最小补写。"),
"2605.05170": dict(method=("§2", "Agent 在固定 harness 中构建 RTL/accelerator，并用 Python reference、testbench、cycle trace 与 timing feedback 迭代实现。"), evaluation=("§2.1–3", "四个设计案例含 TurboQuant accelerator；一个 80 小时长任务观察 human-review bottleneck、过度复杂修复与激进 goal setting。"), limitations=("§4.2", "案例不实现通用 constraint-revision、milestone commit 或 release authority 协议，也不证明自治硬件设计跨任务可靠。"), score=(2,2,2), disposition="整合", owner="AGENT-PLATFORM", chapter="../../../../books/part-07-agent/84-agent-platform.md", comparison="Ch84 已有该 exact-v1 正文绑定，区分 implementation、verification 与 human commit authority；无需新增正文。"),
"2605.05176": dict(method=("§3–5", "证明 attention 可构造多项式/spline features，再由后续层执行 least-squares，从而把 nonlinear ICL 分成特征生成与在线求解。"), evaluation=("§6", "合成 nonlinear regression、多种 context/training sizes 与三 seed 数值实验检验误差趋势。"), limitations=("§7；Appendix", "结论依赖 polynomial/spline approximability 与特定 sum-based attention construction；不证明预训练 LLM 普遍按该算法执行 ICL。"), score=(2,1,2), disposition="整合", owner="MODEL-SELF-ATTENTION", chapter="../../../../books/part-02-model/14-self-attention.md", comparison="Ch14 解释 attention 的内容路由与加权聚合，但缺少“attention 先生成非线性 feature、后层再在线拟合”的受限理论分支；需明确构造性而非通用解释。"),
"2605.05185": dict(method=("§4.2；Appendix B", "Fatal-aware GRPO 将不可恢复 tool transition 识别为 fatal step，以 one-sided advantage clamping 避免失败 token 梯度支配，同时保留可恢复步骤学习。"), evaluation=("§5", "Qwen3-VL 8B/30B-A3B/32B 在七个搜索 benchmark 上比较 SFT/RL 与 fatal-aware 组件消融。"), limitations=("Limitations", "search ranking/fetch/summarization 漂移增加 reward variance；专有 judge、外部 API 与单一训练 recipe 限制归因，视觉中间操作未单独评分。"), score=(2,2,2), disposition="已有覆盖", owner="AGENT-WORKFLOW", chapter="../../../../books/part-07-agent/81-workflow.md", comparison="Ch81 已按 recoverable/fatal transition、environment authority、retry/rollback 与 evidence receipt 组织 workflow；训练时 clamping 是受限实现，不改变 workflow owner。"),
"2605.05189": dict(method=("§2–5", "对 isotropic Gaussian key-value 证明 top-1 读取需要 d²≈n log n，并提出 Tail-Average Margin 将目标改为受控候选列表；TAM 的完整渐近依赖 leave-one-out/postulates。"), evaluation=("§5.3", "数值实验检验 top-1 与 TAM 的相变/score profile；小-tail 外推到 top-1 明确仍是 conjecture。"), limitations=("§4.2–5.4", "结论限线性记忆、Gaussian associations 与论文读取准则；listwise 降门槛是改变 correctness contract，不是免费增加精确容量。"), score=(3,1,3), disposition="整合", owner="MODEL-LONG-CONTEXT", chapter="../../../../books/part-02-model/22-long-context.md", comparison="Ch22 讨论 state capacity 与 retrieval，却未明确容量数字依赖 top-1/listwise 读取契约；需把读取准则作为容量 owner 的组成部分。"),
"2605.05191": dict(method=("§3.1–3.4", "Context-ReAct 在 reasoning/tool loop 中加入 Skip、Compress、Rollback、Snippet、Delete 五种 meta-operation；Compress 的表达完备性与专门操作的效率分开论证。"), evaluation=("§4", "BrowseComp/中文子集等四个 benchmark、LongSeeker-30B，部分集合各采样 200 问；比较 append-only/coarse curation 与原子操作。"), limitations=("§5", "仅 SFT synthetic trajectories，无 rejection/RL；表达完备不证明事实保真、检索正确或开放 workflow 的 rollback 语义。"), score=(2,1,2), disposition="已有覆盖", owner="AGENT-CONTEXT", chapter="../../../../books/part-07-agent/75-context.md", comparison="Ch75 已分 active、compressed、recoverable state，保留 summary lineage、回读和不可把可恢复等同找对证据；五操作是实现词汇。"),
"2605.05204": dict(method=("§2.2", "同一 step-distilled diffusion model 在 student 自身 few-step rollout 上训练：student 只见文本，teacher 同时见目标图像与 prompt 的 multimodal feature。"), evaluation=("§3", "LoRA 与 full fine-tuning 覆盖新 concept/style/domain preference，并比较 vanilla SFT 与组件消融；质量结论绑定作者模型、数据与评价。"), limitations=("§4", "约 4× FLOPs、2× iteration time；依赖 encoder/base model 的 in-context teacher 能力，teacher 在 multimodal condition 下失败时训练也失败。"), score=(2,2,2), disposition="整合", owner="TRAIN-SFT", chapter="../../../../books/part-04-training-system/29-sft.md", comparison="Ch29 已说明 SFT 的 off-policy/遗忘边界，但缺少 few-step diffusion 中 student-rollout + privileged same-model teacher 的连续适配分支；需和 Ch24 handoff。"),
}

CLOSED = {
"2605.04911": "通用 tabular data synthesis 的跨数据预训练与隐私经验取舍；不改变 LLM 数据、训练、推理或平台的状态/控制 owner，且没有形式 DP 保证。",
"2605.04932": "传统 frozen predictor 在低秩动态 covariate shift 下的 Jacobian bound；可作一般 ML 类比，但没有 LLM/AI-system workload 或 release contract 的直接证据。",
"2605.04946": "training-time BatchNorm 对小型 piecewise-affine/ReLU 网络区域几何的结果；Transformer 主线使用 LayerNorm/RMSNorm，未提供 LLM 机制或系统设计增量。",
"2605.05084": "DomainBed 图像 UDA 的 MMD/CORAL batch-order 降方差；属于领域适配采样优化，未改变本项目的大模型数据或训练合同。",
"2605.05123": "通用 continuous-control offline-to-online RL 的候选 policy/OPE/UCB 预算分配；没有 RLHF/RLVR、语言策略或 AI platform 的直接机制证据。",
"2605.05151": "PatchTST 时间序列预测的 SAE/superposition 负结果；只约束 time-series Transformer 的一个 FFN hook，不能改变 LLM 表征或 Transformer 通用机制结论。",
}


def evidence_block(item: dict, r: dict) -> str:
    m, e, l = r["method"], r["evaluation"], r["limitations"]
    return (
        f"### [{item['title']}](https://arxiv.org/html/{item['arxiv_id']}v1)\n\n"
        f"- **Method**（{m[0]}）：{m[1]}\n"
        f"- **Key evaluation**（{e[0]}）：{e[1]}\n"
        f"- **Direct limitation**（{l[0]}）：{l[1]}\n"
        f"- **采用边界**：{item['claim_boundary']}\n"
        f"- **审阅/Books**：exact-v1 Source Review 完成；{r['comparison']} 最终处置：{r['disposition']}。\n"
    )


packet = json.loads(PACKET.read_text())
ledger = json.loads(LEDGER.read_text())
items = {x["arxiv_id"]: x for x in packet["items"]}
identities = {x["arxiv_id"]: x for x in ledger["identities"]}
assert set(REVIEWS) | set(CLOSED) == {
    aid for aid, item in items.items() if item.get("review_result") == "pending"
}

closed_packet = list(packet.get("superseded_closed_items", []))
for aid, reason in CLOSED.items():
    old = items.pop(aid)
    closed_packet.append({
        "arxiv_id": aid,
        "title": old["title"],
        "review_result": "pre_denominator_closed_after_exact_v1_review",
        "closure_reason": reason,
        "preserved_evidence": old.get("superseded_auto_extraction"),
    })
    row = identities[aid]
    row["screening_status"] = "pre_denominator_closed"
    row["screening_reason"] = reason
    row["review_status"] = "closed_after_exact_v1_scope_review"
    row["access_status"] = "exact_v1_reviewed"
    row["integration_disposition"] = "Rejected — Out of Scope"
    row["score_v2_superseded"] = row.pop("score_v2", None)
    row["owner_node_superseded"] = row.pop("owner_node", None)
    row["owner_chapter_superseded"] = row.pop("owner_chapter", None)
    row.pop("books_pending_question", None)

for aid, r in REVIEWS.items():
    item = items[aid]
    item["method"] = {"locator": r["method"][0], "evidence": r["method"][1]}
    item["evaluation"] = {"locator": r["evaluation"][0], "evidence": r["evaluation"][1]}
    item["limitations"] = {"locator": r["limitations"][0], "evidence": r["limitations"][1]}
    item["review_result"] = "source_review_complete"
    item["books_disposition"] = r["disposition"]
    item["owner_node"] = r["owner"]
    item["score_v2"] = {"design_delta": r["score"][0], "system_reach": r["score"][1], "durability": r["score"][2], "total": sum(r["score"])}
    item["books_comparison"] = r["comparison"]
    item["review_gap"] = "无；作者侧证据与 Books 比较完成。"
    row = identities[aid]
    row["review_status"] = "source_review_complete"
    row["access_status"] = "exact_v1_reviewed"
    row["integration_disposition"] = r["disposition"]
    row["owner_node"] = r["owner"]
    row["owner_chapter"] = r["chapter"]
    row["score_v2"] = {"design_delta": r["score"][0], "system_reach": r["score"][1], "durability": r["score"][2], "total": sum(r["score"])}
    row["books_comparison"] = r["comparison"]
    row.pop("books_pending_question", None)

packet["items"] = [x for x in packet["items"] if x["arxiv_id"] not in CLOSED]
packet["superseded_closed_items"] = closed_packet
packet["source_review_complete"] = 133
packet["disputed"] = 4
packet["pending"] = 0
packet["status"] = "Remaining 34-item exact-v1 author batch complete; this batch's root writeback and new non-author review pending"

ledger["candidate_denominator_provisional"] = 137
ledger["pre_denominator_closures"] = 410
ledger["source_review_complete"] = 133
ledger["source_review_disputed"] = 4
ledger["source_review_pending"] = 0
ledger["disputed"] = 4
ledger["pending"] = 0
ledger["status"] = "Remaining 34-item author batch complete; root Books writeback and new non-author review pending"
ledger["denominator_after_exact_v1_scope_recheck"] = 137
ledger["new_scope_closures"] = sorted(CLOSED)

PACKET.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

text = REPORT.read_text()
for aid in CLOSED:
    text = re.sub(rf"^\| \[[^\]]+\]\(https://arxiv\.org/(?:html|abs)/{re.escape(aid)}(?:v1)?\).*\n", "", text, flags=re.M)

for aid, r in REVIEWS.items():
    item = items[aid]
    score = r["score"]
    decision = f"{r['disposition']}：{r['comparison']}（`{r['owner']}`，[章节]({r['chapter']})）"
    row_pattern = rf"^\| \[[^\]]+\]\(https://arxiv\.org/(?:html|abs)/{re.escape(aid)}(?:v1)?\).*\n"
    new_row = (f"| [{item['title']}](https://arxiv.org/html/{aid}v1) | 2026-05-07T08:00:00+08:00 | "
               f"{item['claim_boundary']}；**{score[0]} + {score[1]} + {score[2]} = {sum(score)}** | "
               f"{'深入完成' if sum(score) >= 7 else '标准完成'} | {decision} |\n")
    text, n = re.subn(row_pattern, new_row, text, count=1, flags=re.M)
    assert n == 1, aid

for aid in CLOSED:
    title = re.escape(identities[aid]["title"])
    text = re.sub(rf"^### \[{title}\]\(https://arxiv\.org/(?:html|abs)/{re.escape(aid)}(?:v1)?\)\n.*?(?=^### |^## 5\.)", "", text, flags=re.M | re.S)
for aid, r in REVIEWS.items():
    title = re.escape(items[aid]["title"])
    block = evidence_block(items[aid], r) + "\n"
    text, n = re.subn(rf"^### \[{title}\]\(https://arxiv\.org/(?:html|abs)/{re.escape(aid)}(?:v1)?\)\n.*?(?=^### |^## 5\.)", block, text, count=1, flags=re.M | re.S)
    assert n == 1, (aid, n)

text = text.replace("**548 = 143 候选 + 404 关闭 + 1 撤回排除**", "**548 = 137 候选 + 410 关闭 + 1 撤回排除**")
text = text.replace("当前重新落地 **105 项 Source Review 完成、4 项争议、34 项待定点审阅/纠正**；其中 9 项已有可回读的 Books 正文，其他 Books 比较/写回仍是可执行工作。", "当前作者侧已落地 **133 项 Source Review 完成、4 项争议、0 项待审**；本轮 exact-v1 scope recheck 将 6 项一般 ML 局部研究移至有理由的 pre-denominator closure。本轮 34 项中的 28 个保留候选已逐项完成 Books 比较，仍有 8 项新增/修订及 1 项错误来源删除需要 root 串行写回，之后还需新非作者复核。")

start = text.index("## 5. 缺口与下一步")
end = text.index("## 6. 复核")
section5 = """## 5. 缺口与下一步

作者侧无可继续的 Source Review：34 项 exact-v1 全部取得并定点审阅，其中 28 项保留、6 项因项目范围复核移入 pre-denominator closure；没有 access blocker 或材料请求。4 项争议（2605.04069、2605.04243、2605.04295、2605.05029）保持隔离，不支持 Books。

共享写回仍未完成：8 项需新增/修订 Books，1 项需删除此前由范围外材料写入的专属来源绑定。精确节点、旧命题、最小增量、证据边界与相邻衔接见[Books 写回队列](../_sources/daily-20260507/BOOKS_WRITEBACK_QUEUE.md)。作者未修改共享 Books；root 写回后必须重做实际正文与相邻章节检查。

本报告仍为“进行中”：至少还需 root Books 写回和新的非作者语义复核；本轮队列只覆盖原 34 项剩余批次，不得把作者自检或 validator 当作整日最终通过。

"""
text = text[:start] + section5 + text[end:]
text = re.sub(r"### 作者暂停交接（2026-09-14 20:12）.*\Z", """### 作者侧交接（2026-09-14）

原 34 项剩余批次的 exact-v1 证据与 Books comparison 已结束；全日 Evidence 账面为 **133 完成 / 4 争议 / 0 待审**，活跃分母 **137**，无 exact-v1 材料受阻。本批先执行 date-local 队列中的 8 项新增/修订与 1 项删除；新的非作者 reviewer 还需核对全日既有 disposition 与实际 Books，完成前状态保持进行中。
""", text, flags=re.S)
REPORT.write_text(text)

print("updated", REPORT)
print("active", len(packet["items"]), "complete", packet["source_review_complete"], "disputed", packet["disputed"], "pending", packet["pending"])
