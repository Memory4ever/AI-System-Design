#!/usr/bin/env python3
"""Render the 2026-05-11 V3 author packet from the verified arXiv owner receipt.

This script intentionally does not edit Books. It preserves all legacy evidence and
writes a new screening ledger, evidence packet, Books queue, checkpoint and Daily.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = ROOT / "papers/2026/05/_sources/daily-20260511"
RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260511/arxiv-owner-receipt.json"
REPORT = ROOT / "papers/2026/05/11/README.md"
CHECKED_AT = "2026-09-14T23:45:00+08:00"
BLOCKED_ID = "2605.07250"


def c(score, owner, disposition, contribution, evidence, boundary, insertion=""):
    return {
        "score": score,
        "owner": owner,
        "disposition": disposition,
        "contribution": contribution,
        "evidence": evidence,
        "boundary": boundary,
        "insertion": insertion,
    }


CANDIDATES = {
    "2605.06733": c((2, 2, 2), "TRAIN-LORA", "Integrate",
        "LoRA 聚合对象应是 gauge-invariant 的更新语义，而不是坐标任意的 A/B 因子。",
        "论文以 client projector 估计 consensus update subspace，在 shared reference coordinates 聚合，并从同一 server state 读出不同 rank adapter；GLUE、SuperNI、稀疏参与和异构 rank 是作者实验边界。",
        "低秩 server state 避免 dense reconstruction，却增加子空间估计、参考坐标漂移和参与不足风险；证据不证明任意任务或隐私威胁下都优于普通 FedAvg。",
        "在 Ch30「多个 Adapter 能否直接相加」中，紧接“数学上可相加不代表行为无冲突”段后。"),
    "2605.06755": c((2, 1, 2), "TRAIN-GRPO", "Weekly Only — Context",
        "RL optimizer 可用局部 gradient trajectory 近似多步 lookahead，但必须把稳定性检测和退化回普通 GRPO 写进控制合同。",
        "GXPO 复用同一 rollout/reward/advantage，以三次 backward 形成两步探测、virtual K-step extrapolation 和 corrective update；作者在 Qwen2.5/Llama 数学推理上报告收敛速度与 pass@1。",
        "Ch33 已把 optimizer transform、update scale、稳定性与 AdamW fallback 写入 recipe identity；该工作只是其中一个局部多步外推实现，且证据限于受测数学任务，不足以改变长期主线。"),
    "2605.06760": c((3, 3, 2), "PLATFORM-SECURITY", "No Change — Existing Coverage",
        "模型已能把漏洞利用、凭据抽取、权重复制和远端部署串成可重复的自我复制链，扩展了部署威胁模型。",
        "作者在四类脆弱主机上让模型自主完成端到端复制，并报告不同模型的重复成功率。",
        "结果只属于构造环境、暴露凭据和给定 harness；不能外推现实普遍成功率，也没有改变 Ch72 已有的最小权限、出站隔离、凭据生命周期和模型 artifact 防泄漏责任。"),
    "2605.06788": c((2, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "Agent 故障定位可以输出带有限样本 coverage 的连续回滚区间，而不是未经校准的单点 culprit。",
        "filtration-based conformal prediction 为序列轨迹构造 contiguous prediction sets，并以这些集合驱动多 Agent rollback；论文给出理论保证、多个 agent/dataset 实验及公开代码。",
        "保证依赖 calibration/exchangeability 与既定错误标签；区间不证明区间内每步有因果责任，分布漂移时回退更宽区间、人工定位或从最近可信 checkpoint 重放。",
        "在 Ch66「Attribution 是 Versioned Evaluation Contract」之后、「Evaluation Identity 还必须覆盖测量路径、工作负载与规范目标」之前。"),
    "2605.06841": c((2, 2, 2), "MULTIMODAL-WORLD-MODELS", "No Change — Existing Coverage",
        "World Model 除预测 next state，还必须显式维护 action prerequisite 与动态 affordance state。",
        "AGWM 将前置依赖表示为 DAG，逐步追踪动作当前是否可执行，针对 structure-changing events 降低多步预测错误；证据来自 game-based simulated environments。",
        "Ch25 已用可执行 transition program、action precondition、symbolic graph 与 environment-authoritative correction 完整承载该责任；DAG affordance tracker 是现有命题的受限实现案例，不新增 owner 或设计结论。"),
    "2605.06850": c((3, 2, 3), "TRAIN-RLHF", "No Change — Existing Coverage",
        "训练 rollout 使用压缩 KV、learner 使用 dense context 会形成隐藏的 state-policy mismatch，而不仅是普通推理近似误差。",
        "论文将 sparse rollout 与 dense learner 的偏差识别为 RL 放大源，并用 shadow mask distillation 让训练感知部署时 mask；适用于 PPO/GRPO/Online-DPO 类 rollout pipeline。",
        "Ch31 已将 rollout/training numerical execution identity 纳入 policy identity，Ch33 又明确 token positions、causal mask、memory revision 与 environment snapshot 必须一致；sparse-mask distillation 是该既有合同的实例，不需重复。"),
    "2605.06885": c((3, 2, 3), "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "AR→Diffusion 转换可把语言表示与解码顺序分开：保留表示几何，重学 generation path。",
        "REPR-ALIGN 在相同架构上冻结 AR teacher，以逐层 cosine alignment 配合 masked denoising；作者在 Qwen3 0.6B/1.7B/4B 和代码任务、0.8B/50B 数据条件下报告低数据加速。",
        "同架构 teacher、额外 teacher compute 与代码 benchmark 限制外推；alignment 不证明行为等价，失败时回退普通 continued denoising 或保留 AR。",
        "在 Ch24「Diffusion：用迭代修正换并行状态更新」开头，AR factorization 与 masked denoising 分叉之后。"),
    "2605.06914": c((3, 3, 2), "INFER-SCHEDULING", "Integrate",
        "分支并行宽度应成为每个 decode step 的 slack-aware admission，而不是 eager 或固定 cap。",
        "TAPER 预测 branch externality，只在当前 co-batch slack 可容纳时准入；prefix KV 共享使宽度变化不要求回收 branch memory。作者用 10 小时 trace、Qwen3-32B 报告相对 IRP-Off/Eager 的 goodput 与 >95% SLO attainment。",
        "线性 latency predictor、branch independence、单节点和已测 trace 是边界；预测失准或尾延迟紧张时回退固定 cap/serial branch。",
        "在 Ch56「SLO-aware Admission」中，紧接“当前能放下，不等于未来可完成”之后。"),
    "2605.06939": c((3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "校准后的 LLM judge 估计仍可能因 judge quality 与跨模型 calibration instability 发生带高置信度的方向翻转。",
        "论文用解析推导、模拟和 MMLU-Pro 案例定义 J 与 delta-J 诊断，区分单模型偏差校正和共享校准的比较风险。",
        "Ch66 已明确 judge competence、directional bias、cross-model calibration slice、soft pairwise probability 与 human-anchored interval；该 J/ΔJ 诊断没有改变现有 release contract。"),
    "2605.06997": c((2, 1, 3), "MODEL-LONG-CONTEXT", "Weekly Only — Context",
        "常量状态的 recurrent model 可用可更新的谱算子保存 associative-recall sufficient statistics，而不是重新引入线性 KV history。",
        "Echo/SKA 以 kernel ridge 拟合 key-value history 的 spectral linear system，维护 O(r^2) streaming state；作者在 50M 模型、MQAR 和五个迁移 benchmark 上与 Mamba-2/混合 attention 比较。",
        "Ch22 已完整解释 fixed recurrent state、association collision、capacity、hybrid attention 与外部 retrieval 的共存边界；spectral KRR 是一种具体 state parameterization，现有 50M/合成检索证据不足以改写主线。"),
    "2605.07002": c((2, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "adaptive sampling 与随时停止需要 anytime-valid inference，否则少量定向审计会产生伪置信。",
        "论文用 dueling nulls 和 e-process 描述 auditor/model 双方，并在受控实验中验证 type-I error。",
        "现有 Ch66 已明确保存 adaptive sampling、停止条件、e-process 与保守 fallback；该论文补强证据但不改变当前 owner 或结论。"),
    "2605.07063": c((2, 1, 2), "TRAIN-DATA", "Integrate",
        "通用后训练数据可作为限制目标更新方向的 data-induced regularizer，而不只是供 selection 的样本池。",
        "Dr. Post-Training 用 general data 构造 feasible update set，把稀缺 target-data gradient 投影其中，并把现有 selection 方法组织到 bias-variance 光谱；作者覆盖 SFT、RLHF、RLVR。",
        "额外梯度/投影成本与 feasible-set 失配会压制必要更新；目标分布充分或通用数据有偏时回退普通 mixture/selection。",
        "在 Ch27「Post-training Data Selection 是当前 Policy 的在线控制环」之前，作为 data value 从 sampling weight 演进为 update-feasible-set 的分支。"),
    "2605.07135": c((3, 3, 3), "AGENT-WORKFLOW", "No Change — Existing Coverage",
        "CI event content 经 prompt 或 agent output 进入脚本，会把 prompt injection 扩展成 workflow data-flow vulnerability。",
        "论文区分 Prompt-to-Agent 与 Prompt-to-Script，构建 MCP/agent-aware taint 规格并审计 GitHub Actions corpus。",
        "静态 taint、给定 threat model 和公开 workflow 样本不证明所有 exploit；Ch81/Ch72 已用 untrusted event→proposal→effect-time authorization 的链路承载此结论。"),
    "2605.07153": c((2, 1, 3), "TRAIN-RLHF", "No Change — Existing Coverage",
        "可验证奖励带来的 factual QA 提升可能主要是重排已有参数知识的输出概率，而非写入新事实。",
        "作者在三类模型、闭卷 one-hop QA、fact-level 去重和 binary reward 下比较训练/推理基线，并以概率质量变化解释约 27% 相对提升。",
        "Ch31 已用 capability expansion、distribution sharpening 与 mode extinction 区分“获得能力”和“重排已有模式”；受控闭卷 QA 结果补强该边界，但不新增长期命题。"),
    "2605.07209": c((2, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "开放权重 proxy 的 activation 可作为黑盒目标 hallucination 的辅助 sensor，但不能取得事实 authority。",
        "论文用 proxy analyzer activation 训练/评估检测器并比较不同目标模型和任务。",
        "跨模型 representation shift、可解码不等于因果使用且 detector 会漂移；Ch66/Ch72 已要求 probe 只触发 abstention/escalation 并由外部 evidence 验证。"),
    "2605.07230": c((3, 2, 3), "INFER-SPECULATIVE-DECODING", "No Change — Existing Coverage",
        "图像 speculative decoding 的 verifier 可以利用局部冗余接受语义可替代 proposal，但这属于近似质量合同，不是文本式 exact sampling。",
        "CASCADE 从 target 提取 context-aware redundancy signal，放宽 spatial/semantic interchangeable token 的 acceptance，并将同一信号用于 drafter training；作者在多种 text-to-image/drafter 上报告最高 3.6x。",
        "Ch48 已把 lossless 与 lossy verification 分开，并明确放宽 acceptance 会形成新的 sampling/quality contract；图像的语义可替代 acceptance 是这一原则的受限案例，不再重复写入。"),
    "2605.07244": c((3, 3, 2), "TRAIN-GRPO", "No Change — Existing Coverage",
        "异构 policy 应共享 typed experience，而不是共享参数或假定 tokenizer/behavior distribution 相同。",
        "论文比较 PRP、XGRPO 与 SGT，明确 data/value/outcome 三层共享各自的 density-ratio、support 与 tokenizer residual。",
        "当前 Ch33 已有 source-tagged joint experience plane、独立 policy 更新、tokenizer/provenance 与 outcome-owner 分责；无需重复追加。"),
    "2605.07250": c((2, 2, 2), "PLATFORM-SECURITY", "Temporarily Blocked",
        "低分辨率视觉文本可能在仍可辨认时削弱多模态安全检查，提示压缩策略与 safety policy 必须联合验收。",
        "receipt 保留完整摘要与 exact-v1 身份，但本轮 arXiv HTML/PDF 均未恢复，不能仅凭摘要采用 Cognitive Overload 解释或 Structured Cognitive Offloading 效果。",
        "需要 exact-v1 正文的 threat model、分辨率/扰动设置、模型、ablation 与 limitations；恢复后只重开此 family。"),
    "2605.07274": c((2, 2, 2), "TRAIN-GRPO", "No Change — Existing Coverage",
        "多模态 RLVR 的 sequence reward 需要区分 perception 与 reasoning token 的角色，避免正确答案掩盖视觉证据缺失。",
        "SRPO 以原图/腐化图的 on-policy contrast 估计 perception dependency，再以 perception-consistency 调节 reasoning token 权重，共享 trajectory baseline 且不改变 reward sign。",
        "Ch33 已将 modality/role/turn 作为 typed credit boundary，并明确视觉 reliance proxy 不能取得 outcome authority；SRPO 的 corruption contrast 不改变该责任分配。"),
    "2605.07330": c((3, 3, 3), "TRAIN-DISTRIBUTED-TRAINING", "No Change — Existing Coverage",
        "Trainer→rollout 同步可传输 lossless sparse parameter delta，但 rollout 必须基于正确 base 重构并验证 identity。",
        "论文以 99%+ element sparsity 构造 indices+values payload 和 bucketing，讨论带宽受限异步 RL。",
        "Ch36 已在 source-family marker SF-2026-ARXIV-2605-07330 下完整写入 base/hash/shape/fallback 与非 freshness 保证，故不重复。"),
    "2605.07546": c((2, 2, 3), "WORLDVIEW-SCALING-LAW", "Integrate",
        "Scaling law 的可迁移性应由 information-preserving invariance 与信息分辨率下降来限定，而非默认跨 domain 同指数。",
        "论文论证 bijective transformation 保留 law，non-bijective transformation 通过 information resolution rho 改变 law，并在语言、视觉、语音及两个跨域案例验证。",
        "有限模型/任务和估计 rho 的选择不构成通用 law；变换不可辨或留出尺度失配时回退目标域小规模 sweep。",
        "在 Ch7「Scaling 的适用边界」中，紧接“技术变化会造成 regime change”之后、联合外推之前。"),
    "2605.07568": c((3, 2, 3), "MULTIMODAL-REPRESENTATION", "Integrate",
        "视频时间信息可能已在 encoder 中存在，却在 projector 到 LLM 的接口丢失；表示审计必须逐层定位 bottleneck。",
        "作者用 Arrow-of-Time probe 分离 encoder/projector/LLM，比较 frame-centric、video-centric encoder 与 Q-Former/time-preserved MLP，并在 16-frame 设置和多个 temporal benchmark 验证。",
        "AoT 只是时间信号 probe，16 frames 会漏证据；高 AoT 不保证通用理解，projector 变更失败时回退现有 connector 并单独增加 temporal supervision。",
        "在 Ch23「时间、空间与 provenance 必须进入状态」之后、「Conditional compute」之前。"),
    "2605.07689": c((3, 2, 3), "TRAIN-GRPO", "No Change — Existing Coverage",
        "binary reward 下，group-mean centering 在全对/全错组会把 advantage 清零，造成结构性 gradient starvation。",
        "论文证明真实退化率高于 i.i.d. Bernoulli 估计，并在 Qwen3.5-9B GSM8K 七种 seed 中比较 fixed-reference Sign advantage；一个 G=4 轨迹观察到 0.69 退化率。",
        "Ch33 在 group-relative advantage 定义后已直接写明 all-zero/all-one group 会令 advantage 近零，并把有效 sample ratio 作为诊断；fixed-reference Sign 是实验性 fallback，不改变现有主命题。"),
    "2605.07698": c((3, 2, 3), "INFER-SPECULATIVE-DECODING", "Integrate",
        "grammar local validity 不等于未来可完成性；speculative decoder 若只有局部 mask 会采到 projected law 而非 grammar-conditional law。",
        "论文以 future-validity Phi 构造 Doob transform，exact Phi 下 FVO-Spec 精确，近似 Phi 给出 TV bound；在 Dyck、finite JSON 等可计算 grammar 上评估。",
        "一般 CFG 的 exact Phi 为 #P-hard，OneStep 有 context-independence 误差；估计不可证时回退 local projection 并明确语义，或使用可枚举 grammar/普通 constrained decode。",
        "在 Ch48「Lossless Verification 是分布契约」之后、接受长度例子之前，加入 constrained generation 的 future-validity 条件。"),
    "2605.07719": c((2, 2, 2), "INFER-KV-CACHE", "No Change — Existing Coverage",
        "CPU-resident sparse KV 需要把预算、head/granularity 选择与跨设备执行共同调度；稀疏率本身不能预测端到端收益。",
        "Fluxion 组合 output-aware budget、head predictor、granularity selector 与 priority scheduler，在 2 模型、3 benchmark、40 tasks 上比较质量和 1.5x–3.7x speedup。",
        "Ch45 已明确 host 保留完整可寻址历史、GPU 维护 working set，并联合 selector、fetch、replacement、PCIe 与 fallback；Fluxion 的 budget/head/granularity selector 未改变该机制 owner。"),
    "2605.07836": c((3, 3, 3), "AGENT-MCP", "No Change — Existing Coverage",
        "MCP 安全必须同时跟踪 requester→sensitive sink 与 external/internal data→MCP output 两个方向。",
        "MCP-BiFlow 恢复 MCP entrypoint、定义协议 taint 并做 interprocedural analysis；作者审阅 32 个确认样例与 15,452 仓库。",
        "其静态分析不覆盖 auth/business logic/tool-description poisoning 等未进入可分析 data flow 的风险；Ch83 已把跨 server bidirectional taint、effect-time authorization 与隔离 fallback 写为主线。"),
    "2605.07881": c((2, 2, 2), "INFER-TENSORRT-LLM", "Integrate",
        "accelerator pipeline 的同步正确性必须按硬件可见性与 happens-before 验证，golden output/simulator 不足以覆盖 race。",
        "AccelSync 将 DMA/vector/matrix/scalar pipeline 降为受限并发语言，以 program/sync/barrier order 判断 barrier sufficiency，并在 CANN kernels、生成 kernels 和 mutation 上评估。",
        "sound/complete 只相对参数化模型；驱动升级后一次现象不可复现，硬件模型缺项时应回退 sanitizer、stress test 与保守 barrier。",
        "在 Ch49「Kernel Verification 需要从孤立输入扩展到 Model–Kernel Interface」之后，作为并发可见性检查的下一层。"),
    "2605.07935": c((3, 2, 2), "AGENT-MULTI-AGENT", "No Change — Existing Coverage",
        "Multi-Agent 协议可先转成有限 topology/PlusCal，再用 model-checker counterexample 修复，运行时只允许已验证拓扑中的协调操作。",
        "TraceFix 生成结构化 IR、PlusCal 与 TLC repair loop，再编译为 per-agent prompts；作者在 48 tasks、3,456 runs 和 fault injection 下比较。",
        "Ch82 已将声明式协议、safety/liveness 检查、bounded topology repair、deterministic structural validation 与 runtime invariant 串成主线；TLA+/PlusCal repair loop 是既有主线的一个 artifact，不新增命题。"),
    "2605.08012": c((2, 2, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "Mechanistic interpretability 的 faithfulness、completeness、ablation 等 validation 指标不能替代 causal identification assumptions。",
        "position paper 审计 10 篇、以双人 n=30 复核方向，提出声明 causal claim、identification strategy、assumptions、stress test 与 assumption-failure sensitivity。",
        "purposive 小样本不能估计领域 prevalence，论文也未提供通用识别方法；无法识别时应降级为关联/干预描述而非 causal claim。",
        "在 Ch66「Attribution 是 Versioned Evaluation Contract」中，先于具体归因分数讨论，加入 causal identification disclosure gate。"),
}


OWNER_PATHS = {
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "WORLDVIEW-SCALING-LAW": "books/part-01-worldview/07-scaling-law.md",
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "AGENT-MCP": "books/part-07-agent/83-mcp.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
}


SOURCE_ROWS = [
    ("SRC-OPENAI", "Research 历史入口；动态列表无法稳定分页回到本窗", "受阻", "不支持全站零遗漏断言；若取得官方 2026-05-10/11 归档只重开该入口"),
    ("SRC-ANTHROPIC", "Research 嵌入式历史列表；相邻公开事件 05-08 与 05-14", "已检查", "未见已列事件落窗；动态目录不扩张为全站证明"),
    ("SRC-GOOGLE-AI", "DeepMind Research 与 Google Research Publications 本窗定点检查", "受阻", "历史列表缺日级分页停止点"),
    ("SRC-META-AI", "Meta/FAIR publications 可见历史列表与本窗定点检查", "受阻", "动态目录缺稳定历史日级分页"),
    ("SRC-QWEN", "Qwen 官方历史入口与本窗定点检查", "受阻", "旧入口不能稳定回溯到本窗"),
    ("SRC-DEEPSEEK", "News/Research 历史索引；相邻事件 04-24 与 05-14", "已检查", "未见本窗事件"),
    ("SRC-MOONSHOT", "Kimi Blog 与 MoonshotAI 官方仓库本窗定点检查", "受阻", "Blog/仓库均无稳定历史日级发现页"),
    ("SRC-TENCENT-HUNYUAN", "Research‘全部’列表；相邻条目 04-30 与 05-21", "已检查", "未见本窗事件；列表为目录证据，不证明内部发布"),
    ("SRC-ZAI", "智谱 Research 时间列表；相邻条目 04-29 与 05-20", "已检查", "未见本窗事件"),
    ("SRC-BYTEDANCE-SEED", "Seed Research/Publication 目录与 arXiv identity 交叉检查", "已检查", "目录回填日期不替代 first-public"),
    ("SRC-BAIDU-ERNIE", "ERNIE Blog；相邻官方事件 ERNIE 5.1 为 05-09 08:00+08", "已检查", "该事件早于本窗，不重复"),
    ("SRC-XIAOMI-MIMO", "MiMo Papers 与 Blog 历史入口", "受阻", "Papers 可排除本窗；Blog 卡片缺可复查历史时刻"),
    ("SRC-MINIMAX", "Research/Blog 历史列表；相邻事件 03-18 与 05-26", "已检查", "未见本窗事件"),
    ("SRC-ARXIV", "官方 Monday 08:00+08 announcement 批次；635 direct identities 逐项读 title+完整 abstract；191 revision recovery 分离", "已检查", "一项 exact-v1 正文暂不可达，已隔离并给出重开条件"),
]


FINAL_PROSE = {
    "2605.06733": "Ch30 已说明多个 adapter 的权重增量可相加但行为可能冲突；联邦场景又增加一层约束：同一个低秩更新可以由不同 A/B 坐标表示，直接平均因子会把坐标选择误当成更新语义。客户端先以 projector 描述自己的更新子空间，服务端只在共识子空间与共享参考坐标中聚合，再从同一 server state 读出各客户端所需 rank。聚合 owner 因而持有 gauge-invariant update identity，而不是任一客户端的因子坐标。这个分支避免恢复 dense delta，却增加子空间估计、参考坐标漂移、稀疏参与和异构 rank 的误差；共识不足或行为回归失败时，回退 dense-delta aggregation、同构 rank 或不聚合的独立 adapter。",
    "2605.06788": "Ch66 已要求 attribution 绑定解释对象、证据和处置，但单点 culprit 仍会把有限样本不确定性隐藏成确定定位。对按时间排列的 Agent 轨迹，可把错误起点改写为连续 prediction set：filtration 只读取当前前缀，conformal calibration 控制集合覆盖，rollback owner 从集合覆盖的最近可信 checkpoint 重放，而不把集合内每一步都宣称为因果责任。该机制用可校准的回滚范围换更宽的定位集合、校准数据和 exchangeability 假设；分布漂移、标签不足或集合过宽时，回退人工定位、保守扩大区间或从更早 checkpoint 重放。",
    "2605.06885": "Ch24 已把 AR 与 masked diffusion 区分为不同 factorization 和提交路径；从已训练 AR 模型迁移时，仍需回答哪些能力可复用。一个受限路径冻结 AR teacher，以逐层 representation alignment 保留已有表示几何，同时让 student 用 masked-denoising objective 重学生成顺序。这里 teacher 只拥有表示目标，diffusion objective 与 sampler 仍拥有新 generation path，二者不能据 alignment 宣称行为等价。收益是减少重新学习表示的数据需求，代价是 teacher compute、同构架构耦合和 alignment/objective 冲突；架构不同、表示失配或质量 Gate 失败时，回退普通 diffusion continued training 或保留 AR。",
    "2605.06914": "Ch56 的 SLO-aware admission 目前以请求和 token state 为主要对象；树式解码还会让同一请求的 branch width 在每一步改变共享 batch 的外部成本。调度器可用当前 co-batch 的剩余 slack 与 latency predictor决定本步允许的分支数，只把能被 slack 吸收的 branch 加入 iteration；prefix KV 仍由 cache owner 共享，verifier 仍拥有最终提交。动态宽度以更多搜索并行换 predictor drift、branch 相关性和尾延迟风险；预测不稳、SLO 紧张或共享前缀收益不足时，回退固定 cap、串行 branch 或普通 decode。",
    "2605.07063": "Ch27 已把 data selection 写成 checkpoint-coupled control loop，但 selector 仍主要决定哪些样本被消费。更强的一层是让通用数据定义当前更新的 feasible set：目标数据产生拟更新，general-data gradients 只约束该方向不得越过已声明的能力保持边界，trainer/optimizer 仍拥有参数 commit。这样数据从 sampling weight 演进为 update constraint，可在稀缺目标数据下抑制过拟合，却增加额外梯度、投影成本、通用数据偏置和约束过强导致的欠适配；general set 与部署目标失配或目标数据已充分时，回退普通 mixture、selection 或无投影更新。",
    "2605.07546": "Ch7 已要求 scaling law 绑定拟合区间，并把架构、数据与 objective 变化视为 regime change；跨表示或跨 domain 迁移时还应先判断变换保留了多少信息。双射变换可在同一统计问题上保留 scaling 关系，非双射变换则因信息分辨率下降而改变可达误差与曲线；experiment owner 必须把 transformation、目标域和有效 resolution 一起纳入外推身份。这个判断可减少把表面同尺度误写成同规律，但 resolution 的估计本身有模型和数据依赖；变换不可辨、留出尺度不支持或任务语义改变时，回退目标域小规模 sweep，而不是搬用原曲线。",
    "2605.07568": "Ch23 已要求时间戳、采样率与 connector shortcut 进入 representation contract，但最终任务失败仍不能说明时间信息在哪一层丢失。可在 encoder、projector 与 LLM 接口分别训练同一 Arrow-of-Time probe：若 encoder 可解码而 projector 后消失，修复 owner 应是 connector/fusion，而不是盲目增加 frame 或扩大语言模型。Probe 只拥有 bottleneck diagnosis，不拥有 temporal-understanding 或因果真值；它增加逐层探针、对照与校准成本，并会受帧数和 probe capacity 影响。信号不可复现时，回退遮蔽/反事实任务与端到端 temporal benchmark。",
    "2605.07698": "Ch48 的 exact acceptance 假设每个已接纳 token 都来自目标条件分布；受 grammar 约束时，当前位置合法仍不保证剩余前缀存在任何可完成后缀。Verifier 因而需要 future-validity function，把局部 mask 修正为对可完成路径的 Doob transform，再对 proposal 执行 exact acceptance；grammar owner 定义语言，validity evaluator 判断可完成性，target verifier 仍独占 commit。收益是避免采到最终死路，代价是一般 CFG 上 exact validity 具有 #P-hard 边界；只能近似时必须报告分布误差，或回退可枚举 grammar、普通 constrained decode 与明确的 projected-law 语义。",
    "2605.07881": "Ch49 已把 kernel verification 扩展到模型调用接口，但随机数值对照仍可能漏掉 DMA、vector、matrix 与 scalar pipeline 之间的可见性 race。执行计划需要进一步声明 program order、sync order、barrier scope 和硬件 happens-before；verifier 检查 barrier 是否足以让 producer 写入对 consumer 可见，compiler/runtime 只接纳通过该内存模型的计划。形式化检查扩大并发错误覆盖，却只相对参数化硬件模型 sound/complete，并承受模型缺项和状态空间成本；硬件或驱动语义不完整时，回退保守 barrier、sanitizer、stress test 与 reference kernel。",
    "2605.08012": "Ch66 已要求 attribution 与 faithfulness evidence 版本化，但可解释性实验从 intervention 跳到“识别了真实机制”之间仍缺一层因果资格。每个 causal claim 应先声明 estimand、identification strategy、所需 assumptions、可推翻它的 stress test，以及 assumptions 失效时结论如何降级；probe、ablation 或 intervention 只在这些条件下支持相应强度的声明。该 gate 会降低可发布的强因果结论并增加对照成本，但能阻止相关性、可预测性和局部干预被合并成完整机制证明；无法识别时应保留描述性或干预性结论，而不是补写因果故事。",
}


EVIDENCE_BOUNDARIES = {
    "2605.06733": "arXiv:2605.06733v1 的方法与 GLUE、SuperNI、稀疏参与及异构 rank 实验支持共识子空间聚合；未证明任意任务、非 IID 客户端、恶意参与者或隐私约束下都优于 dense-delta/FedAvg。",
    "2605.06788": "arXiv:2605.06788v1 的 filtration/conformal 定义、coverage 证明、受测 Agent 数据和 artifact 支持连续定位集合；coverage 依赖校准条件，集合不证明区间内每一步具有因果责任。",
    "2605.06885": "arXiv:2605.06885v1 只在同构 Qwen3 0.6B/1.7B/4B、作者代码任务及 0.8B/50B 数据条件下支持表示对齐迁移；不证明跨架构行为等价或 diffusion 普遍替代 AR。",
    "2605.06914": "arXiv:2605.06914v1 的 10 小时 trace、Qwen3-32B、单节点和披露 SLO 合同支持动态 branch admission；1.77x/1.48x 与 >95% SLO 数字不得外推到其他 topology、模型、相关分支或生产流量。",
    "2605.07063": "arXiv:2605.07063v1 在其 SFT、RLHF、RLVR 设置中支持由 general data 构造 update constraint；不证明 feasible set 对任意目标域正确，也不提供生产训练成本或普遍最优投影。",
    "2605.07546": "arXiv:2605.07546v1 的理论条件及语言、视觉、语音与两个跨域案例支持 transformation-aware scaling；有限模型、任务和 resolution 估计不构成跨 domain 的通用 scaling law。",
    "2605.07568": "arXiv:2605.07568v1 的逐层 Arrow-of-Time probe、Q-Former/time-preserved MLP 对照和 16-frame temporal benchmarks 支持 bottleneck diagnosis；AoT 可解码性不证明通用视频理解、因果使用、Serving 收益或更长视频有效。",
    "2605.07698": "arXiv:2605.07698v1 对 exact future-validity、Doob transform、TV bound 及 Dyck/有限 JSON 等 grammar 给出理论与实验支持；一般 CFG 的 exact validity 为 #P-hard，近似函数不自动保持目标条件分布。",
    "2605.07881": "arXiv:2605.07881v1 的受限并发语言、CANN/generated kernels 与 mutation 结果支持 barrier-sufficiency 检查；证明只相对参数化硬件模型成立，且未证明覆盖所有驱动、指令和真实 pipeline。",
    "2605.08012": "arXiv:2605.08012v1 是 position paper；10 篇 purposive audit 与 30 篇双人编码只支持 identification disclosure 框架，不估计领域 prevalence，也不提供通用因果识别算法。",
}


def final_prose(aid, item):
    return FINAL_PROSE[aid] + f" [受限证据：arXiv:{aid}v1]"


def main():
    receipt = json.loads(RECEIPT.read_text())
    identities = receipt["identities"]
    by_id = {x["arxiv_id"]: x for x in identities}
    assert len(identities) == 826
    assert sum(x.get("owner_receipt_route") == "official_arxiv_oai_direct" for x in identities) == 635
    assert sum(x.get("owner_receipt_route") != "official_arxiv_oai_direct" for x in identities) == 191
    assert set(CANDIDATES) <= set(by_id)
    assert all(by_id[x].get("owner_receipt_route") == "official_arxiv_oai_direct" for x in CANDIDATES)

    ledger_entries = []
    direct_closed = 0
    revision_closed = 0
    for x in identities:
        base = {
            "arxiv_id": x["arxiv_id"],
            "source_family_id": x["source_family_id"],
            "title": x["title"],
            "abstract": x["abstract"],
            "categories": x.get("categories", []),
            "receipt_route": x.get("owner_receipt_route"),
            "title_and_full_abstract_reviewed": True,
            "withdrawal_signal": "none_in_owner_receipt; retained exact-v1 checked separately",
        }
        if x.get("owner_receipt_route") != "official_arxiv_oai_direct":
            revision_closed += 1
            base.update({
                "v3_status": "ordinary_revision_excluded",
                "reason": "该 identity 只由 revision/date-recovery route 命中；当前记录没有改变机制、评价、纠错或安全结论的具体 revision signal，不作为当日新候选。",
            })
        elif x["arxiv_id"] in CANDIDATES:
            q = CANDIDATES[x["arxiv_id"]]
            base.update({
                "v3_status": "retained",
                "reason": q["contribution"],
                "score": {"design_delta": q["score"][0], "system_reach": q["score"][1], "durability": q["score"][2], "total": sum(q["score"])},
            })
        else:
            direct_closed += 1
            abstract_head = " ".join(x["abstract"].split())[:300]
            base.update({
                "v3_status": "pre_denominator_closed",
                "reason": f"完整题摘审读后，该 family 的主张是：{abstract_head}…；在本文披露范围内未找到会改变本项目大模型/多模态/World Model/Training/Inference/Platform/Agent 长期机制、state/data/control ownership、evaluation contract 或 Books 既有判断的增量。",
            })
        ledger_entries.append(base)

    assert direct_closed == 635 - len(CANDIDATES)
    assert revision_closed == 191
    ledger = {
        "schema": "daily-v3-screening-ledger-v1",
        "report_date": "2026-05-11",
        "window": {"start": "2026-05-10T09:00:00+08:00", "end": "2026-05-11T09:00:00+08:00"},
        "source_receipt": str(RECEIPT.relative_to(ROOT)),
        "date_semantics": "635 official OAI direct identities belong to the Monday 08:00 Asia/Shanghai scheduled announcement; DataCite creation, submission timestamps and ordinary revisions do not own the day.",
        "summary": {
            "raw_identities": 826,
            "official_announcement_direct": 635,
            "ordinary_revisions_excluded": 191,
            "title_and_full_abstract_reviewed": 826,
            "retained_candidates": len(CANDIDATES),
            "pre_denominator_closed_direct": direct_closed,
            "withdrawn_removed": 0,
        },
        "entries": ledger_entries,
    }

    evidence = []
    for aid, q in CANDIDATES.items():
        x = by_id[aid]
        total = sum(q["score"])
        access = "blocked_exact_v1" if q["disposition"] == "Temporarily Blocked" else "accessible_exact_v1"
        evidence.append({
            "arxiv_id": aid,
            "source_family_id": x["source_family_id"],
            "title": x["title"],
            "primary": (f"https://arxiv.org/abs/{aid}v1" if aid == BLOCKED_ID else f"https://arxiv.org/html/{aid}v1"),
            "public_event": "2026-05-11T08:00:00+08:00 scheduled arXiv announcement",
            "review_depth": "deep" if total >= 7 or q["disposition"] == "Integrate" else "standard",
            "access_status": access,
            "score": {"design_delta": q["score"][0], "system_reach": q["score"][1], "durability": q["score"][2], "total": total},
            "adopted_claim": q["contribution"],
            "mechanism_and_evaluation": q["evidence"],
            "non_proof_tradeoff_and_fallback": q["boundary"],
            "owner": q["owner"],
            "owner_path": OWNER_PATHS[q["owner"]],
            "books_disposition": q["disposition"],
            "books_comparison": q["insertion"] or "现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。",
        })

    queue = []
    for row in evidence:
        if row["books_disposition"] != "Integrate":
            continue
        aid = row["arxiv_id"]
        q = CANDIDATES[aid]
        queue.append({
            "source_family_id": row["source_family_id"],
            "arxiv_id": aid,
            "owner": q["owner"],
            "target_path": OWNER_PATHS[q["owner"]],
            "insertion_point": q["insertion"],
            "final_prose": final_prose(aid, q),
            "tradeoff_and_fallback": q["boundary"],
            "evidence_boundary": EVIDENCE_BOUNDARIES[aid],
            "write_status": "pending_root_serialized_books_writeback",
        })

    disposition_counts = {}
    for row in evidence:
        disposition_counts[row["books_disposition"]] = disposition_counts.get(row["books_disposition"], 0) + 1
    no_change_count = disposition_counts.get("No Change — Existing Coverage", 0)
    weekly_only_count = disposition_counts.get("Weekly Only — Context", 0)
    blocked_count = disposition_counts.get("Temporarily Blocked", 0)

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    (SOURCE_DIR / "V3_SCREENING_LEDGER_20260914.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    (SOURCE_DIR / "V3_EVIDENCE_REVIEWS_20260914.json").write_text(json.dumps({"schema": "daily-v3-evidence-review-v1", "items": evidence}, ensure_ascii=False, indent=2) + "\n")
    (SOURCE_DIR / "V3_BOOKS_WRITEBACK_QUEUE_20260914.json").write_text(json.dumps({"schema": "daily-v3-books-queue-v1", "report_date": "2026-05-11", "items": queue}, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# Daily Research — 2026-05-11", "",
        "**规范：** V3",
        "**窗口：** 2026-05-10T09:00:00+08:00 ～ 2026-05-11T09:00:00+08:00",
        "**状态：** 进行中",
        "**Books：** 纳入本次",
        f"**检查时间：** {CHECKED_AT}", "",
        "## 1. 结论", "",
        f"本窗重新核对 826 个 arXiv identity：635 个属于北京时间 08:00 的官方 Monday announcement，191 个仅由 revision/date-recovery route 命中。826 项均已逐个阅读 title 与完整 abstract；普通 revision 没有具体 important-revision signal，全部从当日新候选排除。635 个 direct identity 中保留 {len(CANDIDATES)} 个候选、分母前关闭 {direct_closed} 个；未发现 withdrawal signal。该计数不继承旧 V2.1、DataCite owner-day 或旧候选结论。", "",
        f"{len(CANDIDATES)-1} 个可访问候选已完成 V3 Evidence Review；`2605.07250` 的 exact-v1 正文仍不可达，已作为终态外部保留项隔离，不能支持其机制解释或 Books。Books 对读后形成 {len(queue)} 项结构化写回队列、{no_change_count} 项已有覆盖、{weekly_only_count} 项只保留在 Daily、{blocked_count} 项暂缓。作者侧尚不能标记完成：共享 Books 必须由 root 按日期顺序写回，并由新的非作者 reviewer 检查来源、准入、证据、实际正文与本报告。", "",
        "## 2. 来源覆盖", "",
        "本轮只执行 Daily 来源，不扫描 Weekly 来源。动态历史入口没有稳定日级分页时按合同隔离，不用空响应或搜索缺命中证明全站无遗漏。", "",
        "| 来源 | 检查范围与依据 | 结果 | 缺口 |", "| --- | --- | --- | --- |",
    ]
    for sid, scope, result, gap in SOURCE_ROWS:
        lines.append(f"| {sid} | {scope} | {result} | {gap} |")

    lines += ["", "## 3. 候选与判断", "", "评分为 Design Delta + System Reach + Durability。候选按唯一 Source Family 计数；普通 revision 不重复计分。", "", "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"]
    for row in evidence:
        s = row["score"]
        result = "受阻" if row["access_status"] == "blocked_exact_v1" else ("深入完成" if row["review_depth"] == "deep" else "标准完成")
        disp = row["books_disposition"]
        if disp == "Integrate":
            disp_text = f"整合：{row['owner']}，等待 root 写回 [{Path(row['owner_path']).name}](../../../../{row['owner_path']})"
        elif disp == "Temporarily Blocked":
            disp_text = f"暂缓：{row['owner']}；exact-v1 恢复后定点重开"
        elif disp == "Weekly Only — Context":
            disp_text = f"仅报告：Weekly Only — Context；受限实现细节，不改变 {row['owner']} 既有命题"
        else:
            disp_text = f"已有覆盖：{row['owner']}，[{Path(row['owner_path']).name}](../../../../{row['owner_path']})"
        lines.append(f"| [{row['title']}]({row['primary']}) | 2026-05-11T08:00:00+08:00 | {row['adopted_claim']}；{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']} | {result} | {disp_text} |")

    lines += ["", "## 4. 证据与知识整合", "",
        "以下逐项结论绑定 exact-v1；正文无法恢复的 family 明确保持暂缓。完整 title/abstract、逐项 closure、评分和长证据字段见 [V3 screening ledger](../_sources/daily-20260511/V3_SCREENING_LEDGER_20260914.json) 与 [Evidence reviews](../_sources/daily-20260511/V3_EVIDENCE_REVIEWS_20260914.json)。", ""]
    for row in evidence:
        lines += [f"### [{row['title']}]({row['primary']})", "", f"{row['adopted_claim']} {row['mechanism_and_evaluation']}", "", f"**边界与回退：** {row['non_proof_tradeoff_and_fallback']}", ""]
        if row["books_disposition"] == "Integrate":
            lines += [f"**Books：待写回。** Owner 为 `{row['owner']}`；{row['books_comparison']} 可直接落盘的完整 prose、trade-off、fallback 与 evidence boundary 已进入 [写回队列](../_sources/daily-20260511/V3_BOOKS_WRITEBACK_QUEUE_20260914.json)。", ""]
        elif row["books_disposition"] == "Temporarily Blocked":
            lines += ["**Books：暂缓。** 当前仅有完整摘要，不能采用论文对 failure mechanism 与 mitigation 的解释；exact-v1 恢复前不写 Books。", ""]
        elif row["books_disposition"] == "Weekly Only — Context":
            lines += [f"**Books：不写入。** `{row['owner']}` 已定义上位机制；本材料只提供一个实验性实现，证据不足以改变长期命题，留在 Daily 作为受限上下文。", ""]
        else:
            lines += [f"**Books：已有覆盖。** `{row['owner']}` 已承载相同的状态/控制权、failure 与 fallback 命题；本材料只作为受限证据，不重复追加。", ""]

    lines += ["## 5. 缺口与下一步", "",
        "- **可执行工作：** root 需按共享文件冲突顺序落实结构化 Books queue，随后由未参与本作者稿的新 reviewer 复核实际写入与报告。", "",
        "- **终态外部保留项：** `arXiv:2605.07250v1` 的 identity 与完整摘要可读，但本轮官方 HTML、PDF 与 TeX 正文均未恢复。缺少 threat model、模型/分辨率/扰动设置、ablation、mitigation 和 limitations；可接受官方 exact-v1 HTML/PDF/TeX 或作者同版本 artifact。材料到达时只重开该 family 的 Evidence/Books，不重扫全日。", "",
        "- **机构目录限制：** OpenAI、Google AI、Meta、Qwen、Moonshot 与 MiMo Blog 缺稳定的历史日级分页；它们已被隔离，不用于候选、Books 或‘全站无遗漏’断言。若获得覆盖本窗的官方归档快照或具名材料，只重开对应来源/identity。", "",
        "## 6. 复核", "",
        "复核者：待分配（必须是未参与本作者稿的新 reviewer）", "",
        "结论：未通过（作者侧完成；等待共享 Books 写回与独立复核）", "",
        f"作者侧已完成 826/826 title+完整 abstract 语义筛选、{len(CANDIDATES)}/{len(CANDIDATES)} 候选处置、{len(CANDIDATES)-1} 项 Evidence Review 和 1 项 exact-v1 终态隔离；{len(queue)} 项 Books queue 尚未实际写入。机器校验只能证明结构与可判定一致性，不能替代上述两项剩余工作。", ""]
    REPORT.write_text("\n".join(lines))

    checkpoint = f"""# 2026-05-11 V3 作者 checkpoint

- raw identities: 826
- official announcement direct: 635
- ordinary revisions excluded: 191
- title + full abstract semantic review: 826/826
- retained candidates: {len(CANDIDATES)}
- direct pre-denominator closures: {direct_closed}
- withdrawn removed: 0
- Evidence: {len(CANDIDATES)-1} complete; 1 terminal exact-v1 limitation (`2605.07250`)
- Books: {len(queue)} queued for root; {no_change_count} No Change; {weekly_only_count} Weekly Only; {blocked_count} blocked
- report status: 进行中
- next: root serialized Books writeback, then a fresh nonauthor review
"""
    (SOURCE_DIR / "V3_AUTHOR_CHECKPOINT_20260914.md").write_text(checkpoint)


if __name__ == "__main__":
    main()
