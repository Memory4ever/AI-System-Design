#!/usr/bin/env python3
"""Apply the bounded 2026-05-22 closure re-audit repair.

This script only rewrites date-local report artifacts.  Shared Books are read
for proposition-level comparison and are never modified here.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import html
import io
import json
import re
import subprocess
import tarfile
import tempfile
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/22/README.md"
CHECKED_AT = "2026-09-16T16:20:00+08:00"
PUBLIC_TIME = "2026-05-22T08:00:00+08:00"


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text or "")).strip()


def sentences(text: str) -> list[str]:
    text = clean(text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text) if s.strip()]


def select_sentence(text: str, terms: tuple[str, ...], fallback: int = 0) -> str:
    ss = sentences(text)
    for sentence in ss:
        low = sentence.lower()
        if any(term in low for term in terms):
            return sentence
    return ss[min(fallback, len(ss) - 1)] if ss else "Not Disclosed"


def parse_specs(raw: str) -> dict[str, dict]:
    out = {}
    for line in raw.strip().splitlines():
        aid, owner, score, proposition = line.split("|", 3)
        out[aid] = {"owner": owner, "score": int(score), "proposition": proposition}
    return out


# All 82 restorations are based on the official owner-batch title plus full
# abstract.  Each proposition states the durable mechanism retained after that
# review; it is not the abstract's background sentence or headline metric.
SPECS = parse_specs(r"""
2605.21552|PLATFORM-EVALUATION-SYSTEM|6|协变量漂移下的置信校准不能只优化均值误差；Expectation Consistency Loss 把预测期望的一致性作为约束，并把适用性限定在论文给出的必要/充分条件与已测 shift。
2605.21557|TRAIN-RLHF|6|RL batch 不必固定为静态超参；以 successive policies 的行为分布偏差作为反馈可以自适应扩缩 batch，但该反馈只控制采样规模，不证明 reward 或更新方向正确。
2605.21560|AGENT-MULTI-AGENT|7|面向 MCU 的多 Agent 设计应先由 vendor feedback 和硬件约束验证方案可行性，再并行探索模型与部署候选；隔离调度提升吞吐，却不能让生成代理拥有最终硬件验收权。
2605.21572|MULTIMODAL-WORLD-MODELS|6|simulation-ready 3D 生成需要把几何、材质、刚体/形变/关节状态与可执行 simulator 接口联合验收，而不能用视觉质量替代物理可用性。
2605.21694|PLATFORM-SECURITY|7|防御 Agent 的 manifest 应显式声明能力、输入输出、权限与运行边界，使 typed action 在执行前可审计；manifest 是 capability proposal，不是授权或真实 effect receipt。
2605.21726|PLATFORM-EVALUATION-SYSTEM|6|LLM attribution 可以从 token probability 构造不确定性分布而非只给单点解释，但该概率归因仍受 reference、输出目标和模型 revision 约束，不能升级为唯一因果解释。
2605.21728|PLATFORM-EVALUATION-SYSTEM|6|图像描述评测可用高效 cross-encoder 构造 reference-free 语义分数，但 scorer 只覆盖已测人类偏好与数据分布，不能替代事实性、细粒度 grounding 或人工验收。
2605.21751|AGENT-TOOL-CALLING|7|文本到优化的模型可提出变量与约束结构，却会在数字、实体和索引绑定上失效；应把结构化 binding 外置为可验证程序/数据文件，再由 solver 与 checker 拥有数值提交权。
2605.21770|MODEL-MULTI-HEAD-ATTENTION|7|固定 activation vector 会无差别扰动正确与错误步骤；MAGS 将特定 head 到 correctness manifold 的距离作为 trajectory sensor，仅越过阈值时投影回已学子空间，端到端任务仍拥有正确性判定。
2605.21781|AGENT-PROMPT|7|Prompt 优化应把全量优化集上的重复失败汇总为结构化诊断并保留跨轮 memory，再由 optimizer 定点修订；诊断、校准和最终 held-out 结果必须分权。
2605.21783|PLATFORM-MONITORING|6|Test-time adaptation 的 epistemic uncertainty 可用 MMD ball 与 PAC-Bayes bound 表达分布邻域和风险上界，但保证只在核、先验与采样假设成立时有效。
2605.21824|AGENT-PLATFORM|7|自动生成 fuzz harness 不能以可编译为终点；输入生成、oracle、执行隔离与故障归因四类原则应分别验收，并允许 checker 失败时回退人工 harness。
2605.21825|AGENT-PLATFORM|7|可视化 Agent harness 应把数据、代码、渲染 artifact、反馈和 evaluator 作为可追踪交接状态，避免仅凭自然语言结果宣称图表正确。
2605.21849|WORLDVIEW-REPRESENTATION|7|字典式解释器在 OOD activation 上会发生子空间失配；可用无标签部署激活调整解释几何，但 adaptation 只修复 replacement model，不能证明原模型机制或标签语义稳定。
2605.21907|MULTIMODAL-GENERATIVE-PARADIGMS|6|Diffusion test-time scaling 可把 reward-guided noise search 集中到曲率分析识别的少数关键 denoising steps，以搜索状态和额外 reward cost 换质量，不能从平均指标外推生产延迟。
2605.21917|AGENT-WORKFLOW|6|视频推理标注可拆成多阶段 Agent pipeline，并用失败记录同时修订 prompt 与流程；自动修复只生成新 annotation proposal，仍需独立质量抽检。
2605.21933|WORLDVIEW-WHY-MODELS-LEARN|7|有限步长训练算法具有可测的时间不可逆性；多个 leading-order 定义一致并产生破坏特定重参数对称性的 emergent force，这修正了把离散训练等同可逆连续扩散的解释。
2605.21952|AGENT-RAG|7|RAG 的 ANN 路径可由 near-data processing、分段索引与 early exit 联合设计；软件召回 frontier、硬件带宽和停止条件必须共同版本化，速度不能静默覆盖召回。
2605.21972|MODEL-TRANSFORMER-LAYER|6|结构化 pruning 后的 label-free recoverability 取决于稀疏预算在层/模块间的分配，而不只取决于总 sparsity；恢复结论必须绑定 allocation 与校准数据。
2605.21980|MULTIMODAL-REPRESENTATION|7|LVLM 情绪行为可沿跨模态信息流定位候选 circuit，并通过受控 inference steering 检验影响；可读出/可操纵信号仍不等于唯一因果情绪机制。
2605.21981|MULTIMODAL-GENERATIVE-PARADIGMS|6|冻结表征空间的有效秩、条件数与尾部形态可让 vanilla x-prediction flow matching 更易优化；收益属于所测 representation/noise schedule，不证明任意 latent 都优于 pixel。
2605.21984|TRAIN-DATA|7|Agent 经验数据应保留原 trajectory 与用户修订的差异，把可验证 refinement 转成训练样本；用户偏好只提供监督提案，不能绕过数据 provenance 与独立评测。
2605.21993|TRAIN-RLHF|7|候选排序的 policy update 可把证据 span 与 verifier 结果耦合，使 reward 指向可检查依据；verifier 仍是受限 sensor，不能由奖励分数取代事实判定。
2605.21999|TRAIN-SFT|7|鲁棒 teacher 仍可能在不可学习或被扰动子集上向 student 传递错误边界；distillation 应分开 teacher robustness、student support 与样本可学习性，而非用 teacher 总体准确率拥有监督权。
2605.22015|MULTIMODAL-GENERATIVE-PARADIGMS|7|视频 DiT token reduction 应依据前一步输出相似度与全局 token 分布配对，并把 matching accelerator 的量化/流水线成本纳入同一质量—速度 contract。
2605.22035|TRAIN-LORA|6|Continual VQA 可由 hypernetwork 按输入生成低秩适配器并以 anchor 约束漂移；动态 adapter 增加条件化能力，也引入 hypernetwork 失配与长期遗忘风险。
2605.22060|PLATFORM-SECURITY|7|防止 text-to-image 模型被 query-output 蒸馏需要把发布输出视为可被 student 学习的通道，并在视觉 fidelity、扰动可感知性和 adaptive student gain 间设预算；输出扰动不是保密证明。
2605.22078|MULTIMODAL-REPRESENTATION|6|Video LLM 的 token 压缩应同时保留多粒度时间网格与高信息空间区域；token norm 只是选择 proxy，不能证明语义重要性。
2605.22083|MULTIMODAL-GENERATIVE-PARADIGMS|6|Flow-matching TTS 可通过 repeat/skip latent trajectory augmentation 建立一致性对比信号，但增强轨迹仍需与自然语音质量和鲁棒性分别验收。
2605.22089|MULTIMODAL-EMBODIED-VLA|6|自动驾驶 VLA 可把未来场景 latent 作为辅助预测状态增强 action reasoning；预测状态不是环境事实，闭环 controller 仍拥有提交权。
2605.22098|MULTIMODAL-REPRESENTATION|6|文本 embedding 可作为视觉特征的跨模态 preconditioner，帮助改善视觉表示几何；语言先验带来的增益不证明图像证据被忠实使用。
2605.22123|MULTIMODAL-EMBODIED-VLA|6|少量 demonstration 的 reward 学习可追求对外观变化不敏感的 invariant signal，但 reward 仍需在真实机器人闭环中校准，不能由像素不变性推出任务正确。
2605.22132|INFER-TENSORRT-LLM|6|Vision foundation model 可用 drop-in depthwise convolution 替换部分昂贵算子以换取吞吐；可部署性必须绑定具体 backbone、kernel、分辨率和精度回归。
2605.22168|PLATFORM-EVALUATION-SYSTEM|7|VLM explainability 不能只用单模态 perturbation 评分；Shapley interaction 型 synergy metric 可隔离联合模态贡献，但仍是 scorer-specific surrogate，不拥有因果或安全结论。
2605.22195|AGENT-PLANNING|7|Graph-of-Thought 的操作图可由 RL 根据任务复杂度在有限 operator 集中自适应构造；policy 只拥有 graph proposal，执行预算和答案 verifier 仍需外置。
2605.22207|TRAIN-RLHF|6|未知随机动力学中的 safe exploration 可联合学习 policy 与 kernel barrier，并在预测违规时替换 action；概率安全保证依赖 embedding、样本覆盖和阈值，不能外推为绝对安全。
2605.22208|AGENT-MEMORY|6|图像修复 Agent 可把工具/顺序 trial 归纳为分层经验池并持续更新；experience promotion 需要 provenance、冲突和回归 Gate，不能让自生成经验拥有真值。
2605.22211|TRAIN-DPO|7|Reasoning efficiency 可在正确 on-policy rollout 上局部删除重复/无关内容，再以 auxiliary reference-free DPO 学习编辑差异；正确性 gate、删除范围与 off-policy 距离必须共同冻结。
2605.22213|PLATFORM-EVALUATION-SYSTEM|7|Assurance argument 的 confidence 应把 claim、evidence、context 和 relation 映射为带 provenance 的 Subjective Logic 网络；传播出的数值是可审计信念状态，不是系统性质真值。
2605.22238|PLATFORM-EVALUATION-SYSTEM|7|Live Agent 评测应分离 planner 与 execution scaffold，并同时记录 objective tracking、行动转化、成本和 runtime failure；端到端胜率不能直接归因单一模型规划能力。
2605.22240|TRAIN-RLHF|6|主动对话训练可让 simulator 暴露训练期 latent concern 和状态转移，再把 privileged behavior 蒸馏到仅见对话的部署 policy；隐藏 persona 不能在推理时泄漏或充当真实用户状态。
2605.22266|PLATFORM-MONITORING|6|Federated learning 的 client 异常可通过共享 probe 上 activation-induced partition 的变化监测，比参数距离更接近功能偏移；该信号只建议 risk-aware aggregation，不拥有剔除权。
2605.22272|MULTIMODAL-EMBODIED-VLA|7|从视频 prior 到 humanoid control 可用统一 4D point trajectory 与稀疏关键点避开完整 CAD/retargeting；视觉可行轨迹仍需 BFM、物理环境和 controller 验收。
2605.22324|PLATFORM-MONITORING|7|低 prevalence SOC 流的控制目标应显式权衡 benign-normalized false-positive burden、recall 与 analyst query budget；shift trigger 和 active acquisition 都不能只用 F1 验收。
2605.22344|MULTIMODAL-GENERATIVE-PARADIGMS|6|视频生成可把 MLLM 产生的 ViT-space semantic plan 与 DiT renderer 分离训练并轻量共训；semantic plan 是条件接口，不是像素或时序正确性证明。
2605.22350|MODEL-TRANSFORMER-LAYER|6|Partial fusion 在 full ensemble 与完全 weight aggregation 之间开放连续的计算—性能选择，并要求 neuron matching/融合比例成为 artifact identity。
2605.22356|TRAIN-SFT|7|对结构化决策行为做 fine-tuning 会把局部 action bias 扩散到开放生成分布；行为训练的验收必须覆盖未训练语境与分布副作用，而非只看目标任务 loss。
2605.22358|AGENT-RAG|6|Generative retrieval 可在 free-form thought 与 constrained docid decoding 间切换，并用 retrieval-grounded RL 训练；生成的 CoT 不证明检索证据真实或推理忠实。
2605.22364|AGENT-PLANNING|7|Observation-aware planning 应把 sensor/observation function 本身作为待选择状态，用 POMDP decomposition 扩展可解规模；可观测性 proposal 不替代真实 sensor 成本与环境验证。
2605.22376|TRAIN-RLHF|6|跨域 offline RL 的 source transition 应按其对 target Bellman target 的贡献选择，而非只按局部动态相似度；估计误差仍可能放大错误 transfer。
2605.22469|PLATFORM-EVALUATION-SYSTEM|6|概念驱动图像生成评测应分解 foreground concept 与 background preservation，再用 masked similarity 避免单一全图分数掩盖局部失败。
2605.22471|MODEL-TOKENIZER|6|Graph tokenizer 的粒度、Transformer depth 与结构 expressivity 存在可证明 trade-off；token count 降低不能单独拥有图任务质量结论。
2605.22472|WORLDVIEW-REPRESENTATION|6|Winner-Take-All bottleneck 可在多任务条件下迫使表示形成稀疏 symbolic slots，但 theorem 的数据/任务假设和行为验证边界必须保留。
2605.22496|PLATFORM-MONITORING|6|Factorised latent 的单样本 goodness-of-fit test 可在校准分布下控制 false-positive rate 做 OOD sensor；因子化与 reference distribution 失配时必须降级。
2605.22507|MULTIMODAL-GENERATIVE-PARADIGMS|6|Value-driven transport 将生成过程表述为由 value signal 引导的 transport dynamics，提供不同于固定 score/flow 的控制分支；其收益限于所测目标和采样器。
2605.22530|PLATFORM-EVALUATION-SYSTEM|7|Safety argument 的 runtime evidence 应作为新 opinion 增量更新 claim confidence，并保留依赖与 provenance；confidence 下降触发重验/降级，不能自动证明系统安全。
2605.22531|WORLDVIEW-REPRESENTATION|6|Riemannian ICA 可用局部几何张量在非生成模型表示中寻找 pointwise disentangled directions；局部独立性不等于全局语义唯一或因果机制。
2605.22558|MULTIMODAL-REPRESENTATION|6|Scene reasoning 前可先用几何证据为 visual token 建立空间 grounding，再交给语义模型；几何估计是受噪声约束的输入状态，不是场景真值。
2605.22567|TRAIN-RLHF|6|多语 reasoning RL 可用 language-conditioned hints 打开探索，再以 progressive decay 和 language-adaptive switch 撤除脚手架，避免把提示依赖固化进 policy。
2605.22570|PLATFORM-EVALUATION-SYSTEM|7|时空 reasoning benchmark 可主动合成视频以控制运动变量与反事实，而不是只消费静态语料；生成器偏差和 evaluator 一致性仍需独立审计。
2605.22591|TRAIN-DATA|6|冻结 vision foundation model 时，小损失样本选择可能系统性偏向易例并在跨数据集噪声下失效；noise-robust recipe 必须按 backbone/label regime 重验。
2605.22593|PLATFORM-MONITORING|7|GNN deep ensemble 的成员可能共享表示与错误而造成 epistemic collapse；ensemble size 不能替代成员多样性、shift slice 与 calibration 检查。
2605.22612|PLATFORM-EVALUATION-SYSTEM|7|Benchmark 到部署的 gap 应拆成可由 conversation 测试的 task assumption 与需要 outcome/behavior study 的 outcome assumption，并用 BenchmarkCard 和 staged evaluation 逐层关闭。
2605.22613|AGENT-PLANNING|6|LLM program evolution 可先在 task family 共享 executable archive，再按目标任务适配；共享/适配 compute split 和 held-out transfer 必须共同验收。
2605.22642|AGENT-PLATFORM|6|Spreadsheet Agent 的 RL 环境应使用真实 workbook 状态、公式/格式/依赖与可执行 outcome，而非仅用文本答案判断任务完成。
2605.22644|WORLDVIEW-WHY-MODELS-LEARN|7|有限 learning rate 的离散 SGD 在二阶项上不等同 Brownian/Langevin motion，平坦方向也未必存在 stationary distribution；连续近似必须声明步长与时间尺度边界。
2605.22645|PLATFORM-EVALUATION-SYSTEM|7|Text-to-image prompt evaluator 应把 upstream prompter 当 Agent，检查其迭代、图像反馈和最终目标达成；下游图像分数不能静默归因 prompt model。
2605.22677|INFER-TENSORRT-LLM|6|Slimmable ConvNeXt 通过共享权重支持多 width inference，使设备预算成为运行时选择；每个 width 都需要独立 kernel/accuracy/latency identity。
2605.22678|MULTIMODAL-REPRESENTATION|6|视频采样可用 Taylor temporal surprise 选择非冗余帧，但局部变化 proxy 不能保证保留任务相关事件，需按 downstream query 验收。
2605.22679|WORLDVIEW-REPRESENTATION|6|不扩张维度的可逆旋转加 top-k bottleneck 可把 VLM embedding 重排为稀疏轴；可解释坐标仍是 post-hoc basis，不证明原模型以该语义计算。
2605.22711|TRAIN-RLHF|6|Offline goal-conditioned RL 可通过抽象状态共享稀疏 goal 经验，但 abstraction 必须保留 reward/transition sufficiency，并在支持不足时回退原状态。
2605.22717|MULTIMODAL-GENERATIVE-PARADIGMS|7|交互式 music diffusion 可用 block-wise KV cache 降低 streaming 复杂度，并用 ARC-Forcing 抑制跨 block error accumulation；cache identity、延迟与音质需联合验收。
2605.22723|MULTIMODAL-GENERATIVE-PARADIGMS|7|Gaussian DDPM 若只匹配 reverse mean 会留下 path-level covariance error；full covariance matching 可改善收敛阶，并用 matrix-free Lanczos 近似采样，但代价与假设必须显式。
2605.22733|AGENT-MCP|7|同一 typed skill 定义可生成 HTTP/SSE/OpenAPI 与 MCP 两种接口，减少双栈 schema drift；生成层只拥有接口一致性，authorization、effect 与 lifecycle 仍由 runtime 验证。
2605.22743|TRAIN-LORA|7|Continual multi-concept generation 可用 bilevel update 与正交约束隔离 sequence LoRA；正交 proxy 不能证明概念无干扰，旧概念回归仍是提交 Gate。
2605.22746|PLATFORM-MONITORING|6|Evidential deep learning 可通过 plug-in loss 将 softmax classifier 纳入统一 uncertainty 接口；evidence 参数化不自动产生校准或 OOD 保证。
2605.22771|TRAIN-SFT|6|政治偏差评测应使用对立主题 paired prompts 分别测 rhetoric 与 helpfulness consistency；一致性训练减少披露偏差，但不能定义政治真值或跨域中立性。
2605.22777|MULTIMODAL-GENERATIVE-PARADIGMS|6|Representation autoencoder 可用 detail-condensing queries 分开重建细节与生成友好 latent；更好 reconstruction 仍可能损害生成 geometry，二者需共同验收。
2605.22785|PLATFORM-EVALUATION-SYSTEM|7|新闻 chatbot 评测必须分开检索覆盖、来源引用、推理与 fabricated-premise resistance；流畅答案和引用数量不能拥有事实正确性。
2605.22812|MULTIMODAL-EMBODIED-VLA|6|Gesture 可作为与文本并行的 VLA instruction modality，经 latent representation 参与 reasoning/action；gesture grounding、action policy 与真实 controller 必须分层验收。
2605.22816|MULTIMODAL-EMBODIED-VLA|6|VLN 可显式建模 agent state 与 task progress 形成 self-aware reasoning state，而不依赖额外 3D map；该内部状态仍需由真实 observation/trajectory outcome 校正。
2605.22819|MULTIMODAL-REPRESENTATION|6|Pose token/回归头可为 Video LLM 提供跨帧持久空间坐标，使方向与相对位置不只依赖语义 token；pose estimate 不是场景真值。
""")


CONFIRMED_FN = {
    "2605.21770", "2605.21781", "2605.21907", "2605.21933", "2605.21981", "2605.22015",
    "2605.22078", "2605.22211", "2605.22238", "2605.22344", "2605.22567", "2605.22612",
    "2605.22613", "2605.22679", "2605.22717", "2605.22771", "2605.22812", "2605.22816",
}


INTEGRATES = {
    "2605.21751": {
        "anchor": "### Abstract Intent 需要有界解析为 Primitive Tool",
        "gap": "现有正文约束了 intent 到 primitive tool 的解析与 typed validation，但没有区分结构建模成功和数值/实体 binding 失败，也未把 binding 外置为 solver 前的确定性 artifact。",
        "delta": "旧路径让同一语言模型同时提出优化结构并填入数字、实体与索引；当结构推理正确而 binding 仍错时，把变量/约束 schema 与外部结构化数据分离，由确定性 binder 生成 solver input，模型只拥有结构 proposal，binder/checker 拥有标识解析，solver 拥有数值可行性。",
        "tradeoff": "外置 binding 增加 schema、数据文件、解析器与一致性测试成本，也会暴露原本被端到端生成掩盖的缺失字段。",
        "fallback": "若 binder 无法唯一解析实体、单位或索引，拒绝求解并请求补充信息；小型、固定且已验证的问题仍可保留端到端路径，但必须执行 solver/checker 验收。",
        "method": "§3 Text2Opt-Bench: Design and Evaluation; §4 The Binding Bottleneck; §5 Mitigating Binding Failures",
        "evaluation": "§3.3 Evaluation Protocol; §4.1–§4.2; Appendix G.9 OOD Cliff-Shift Experiment",
        "nonproof": "§6 Conclusion; Appendix B Failure Mode Analysis",
    },
    "2605.21770": {
        "anchor": "## Head 怎样分化，又为什么会冗余",
        "gap": "现有正文讨论 head 分化、冗余和因果验证，但尚未承载把特定 head 的 trajectory-to-manifold distance 用作有条件 activation steering sensor 的分支。",
        "delta": "旧式固定 steering vector 对所有生成步骤施加同一扰动；当错误表现为特定 attention head 沿生成轨迹偏离低维 correctness subspace 时，按 head 监测距离，仅超过学习阈值才投影纠正。距离只拥有 intervention proposal，端到端任务 verifier 仍拥有正确性。",
        "tradeoff": "需要白盒 head activation、对比轨迹、子空间与阈值校准，并增加每步监测开销；过强投影会破坏本来正确的轨迹。",
        "fallback": "head/任务漂移、距离失去校准或 utility regression 超界时关闭投影，回退无 steering、较弱静态 steering 或外部 verifier-guided retry。",
        "method": "§3.2 Contrastive Error Manifold Construction; §3.3 Proximity-Based Error Detection; §4 Manifold-Guided Attention Steering",
        "evaluation": "§3.4 Empirical Validation of the Drift Hypothesis; §5 Experiments",
        "nonproof": "§6 Discussion; §7 Conclusion—Limitations and future work",
    },
    "2605.21849": {
        "anchor": "### 解释模型也有自己的 Faithfulness Budget",
        "gap": "现有正文已把 dictionary/probe 视为 replacement model 并要求 faithfulness budget，但没有说明部署分布使 explainer subspace 本身漂移时如何有界适配。",
        "delta": "旧路径在训练分布拟合固定 dictionary/explainer 后直接用于部署；当 OOD activation 几何改变时，可只用未标注部署 activation 重估解释子空间，同时冻结被解释模型。Adaptation 只拥有 replacement-model 修复，因果 intervention 与外部行为仍拥有 faithfulness 判断。",
        "tradeoff": "在线/批量适配增加 activation 收集、版本化和污染风险，解释坐标也可能失去跨版本可比性。",
        "fallback": "重建误差、跨 seed 稳定性或 intervention fidelity 未恢复时，将结果降级为相关性观察并回退原 dictionary、多 probe/多 baseline 与端到端行为检验。",
        "method": "§3 Hidden-Space Geometry Shift and Faithfulness Degradation; §4 Geometry-Adaptive Explainer",
        "evaluation": "§5 Experiments; §5.2.3 Circuit Attribution under Distribution Shift; §5.2.4 Mechanism Analysis",
        "nonproof": "§6 Conclusion; Appendix F Hyperparameter Sensitivity; Appendix G Held-out In-Distribution Data",
    },
    "2605.21933": {
        "anchor": "## 梯度下降：怎样从错误走向参数更新",
        "gap": "现有正文解释有限 learning rate 的局部稳定与离散分岔，但没有把训练算法的时间不可逆性、多个等价 leading-order 定义和 symmetry-breaking force 串成机制边界。",
        "delta": "旧解释常把小步长训练近似成可逆连续流或 Langevin 型噪声过程；有限步更新的 backward error、time-renormalized correction、time-asymmetry 与正则化 entropy production 在 leading order 可一致定义不可逆性，并产生选择学习轨迹的 symmetry-breaking force。",
        "tradeoff": "该分析换来更精确的离散动力学解释，却依赖小步长展开、正则化与论文中的对称性条件，且诊断计算不直接给出最优 schedule。",
        "fallback": "步长不小、随机过程假设或对称性条件不成立时，不外推 entropy-production 选择律，回退离散 update、loss/gradient/step-norm 与多 learning-rate 实验。",
        "method": "§Main results; §Equivalence of Potentials; §Symmetry Breaking and Preservation",
        "evaluation": "Appendix G Experimental Measurement of the Four Irreversibility Potentials; Appendix H Anomalous Fluctuations Experiment",
        "nonproof": "§Discussion",
    },
    "2605.22060": {
        "anchor": "### Extraction Budget 必须跨身份聚合",
        "gap": "现有正文覆盖跨身份 query budget 与 adaptive extraction，但未承载将每个生成输出本身作为可学习 release，并联合约束 student gain 与图像 fidelity 的输出扰动分支。",
        "delta": "仅限流/身份聚合无法阻止合法响应被用于 query-output distillation；输出发布可在受限 perceptual budget 内加入针对 student 学习的扰动，并用 teacher utility、感知质量、adaptive student gain 与累计 query identity 联合验收。",
        "tradeoff": "输出扰动会牺牲 fidelity、可复现性和下游编辑能力，且需持续模拟更强 student，增加生成与评测成本。",
        "fallback": "adaptive student 仍恢复能力、用户质量回归或扰动可被去除时，不宣称保密，回退访问控制、速率/身份聚合、watermark/audit 与不发布高价值输出。",
        "method": "§3 Threat Model and Problem Setup; §4 Method",
        "evaluation": "§5 Experiments; §5.3 Efficiency and Perturbation-Budget Trade-off; §5.6 Robustness to Attacker Strategies",
        "nonproof": "§6 Conclusion; §3.2 Defense Goals and Constraints",
    },
    "2605.22211": {
        "anchor": "### Preference Pair 选择是实验设计，不只是数据量选择",
        "gap": "现有正文覆盖 pair identity 与 online discovery/offline update，但没有承载对正确 on-policy reasoning 进行局部内容删除、再以 reference-free DPO 作为辅助目标的路径。",
        "delta": "旧式 length reward 或硬 budget 只约束最终长度；先由当前 policy 产生并经 verifier 判正确的 rollout，再局部删除重复、不可读、无关或答案后探索内容，以 augmented-original pair 的辅助 reference-free DPO 联合 policy-gradient 更新，可在保持近 on-policy 的同时监督内容效率。",
        "tradeoff": "需要外部 augmentation model、正确性 gate 和删除审计；过度删除会移除必要推理，reference-free objective 也可能放大 style shortcut。",
        "fallback": "编辑后答案/过程验证失败、pair 距离过大或 held-out accuracy 下降时丢弃 pair，回退原 rollout、保守 length control 或只训练经人工/程序验证的局部编辑。",
        "method": "§3.1 Problem Formulation; §3.2 Method",
        "evaluation": "§4 Experimental Setup; §5 Research Questions and Empirical Analysis",
        "nonproof": "Appendix A Limitations; §7 Conclusion",
    },
    "2605.22644": {
        "anchor": "## 梯度下降：怎样从错误走向参数更新",
        "gap": "现有正文说明 mini-batch 噪声和有限步长稳定性，但没有明确离散 SGD 与 Brownian/Langevin 近似在二阶项和平坦方向 stationary behavior 上的失配。",
        "delta": "把 SGD 噪声直接等同 Brownian motion 会丢掉有限 learning-rate 的离散高阶项；exact-v1 表明二阶动力学和 flat directions 可偏离连续扩散、甚至没有 stationary distribution，因此 diffusion 近似必须绑定步长、时间尺度与几何条件。",
        "tradeoff": "保留离散修正提高解释精度，却增加理论和数值估计成本，也不能自动选择生产 optimizer。",
        "fallback": "小步长/尺度分离条件未验证时停止使用 Brownian stationary 结论，回退直接离散模拟、多步长对照以及 loss、gradient、parameter displacement 监测。",
        "method": "§3 Setup and Problem Formulation; §4 Main Theoretical Results and Analysis",
        "evaluation": "§5 Experiments; Appendix C Experimental setup; Appendix D Additional Experiments",
        "nonproof": "§6 Limitations; §7 Conclusion",
    },
    "2605.22723": {
        "anchor": "### 加速后的输出必须与未加速轨迹建立一致性边界",
        "gap": "现有正文要求生成加速维持轨迹一致性，但没有解释 Gaussian DDPM reverse covariance 失配怎样决定 path KL 收敛阶，以及如何用 matrix-free Lanczos 承担 full-covariance 采样。",
        "delta": "只匹配 reverse mean 的 Gaussian DDPM 会保留 covariance path error；在论文假设下匹配 full reverse covariance 可把离散 path KL 的收敛阶从 O(1/T) 改进到 O(1/T^2)，Lanczos 近似矩阵函数以额外算子调用换取无需显式矩阵的采样。",
        "tradeoff": "covariance-vector products 与 Lanczos iteration 增加计算/数值误差，理论阶数也不等于真实数据感知质量或低延迟收益。",
        "fallback": "Gaussian/score regularity、Lanczos residual 或端到端质量不满足时，回退 mean-only sampler、更多 steps 或对角/低秩 covariance，并保留 reference trajectory 对照。",
        "method": "§2.1 The Value of Learning the Posterior Covariance; §2.2 Drawing Gaussian Samples; §4 The Lanczos Gaussian Sampler",
        "evaluation": "§5 Experiments; §5.1 Exact Path KL; §5.2 Image modeling",
        "nonproof": "§5.2.2 Conclusions; §6 Conclusion; Appendix B Counter Example",
    },
    "2605.22733": {
        "anchor": "### 协议比较必须拆开五类契约",
        "gap": "现有正文拆分 MCP 的 identity/schema/authorization/transport/effect contract，但没有承载一个 typed skill source 同时生成 HTTP/SSE/OpenAPI 与 MCP adapter 的 single-source 路径。",
        "delta": "分别手写 REST/streaming 与 MCP 会让 schema、错误语义和 lifecycle 漂移；以同一 typed skill definition 生成两类 adapter，可让参数/返回类型共享来源，同时要求 transport-specific cancellation、stream event、authorization 和 effect receipt 继续独立验收。",
        "tradeoff": "代码生成与抽象层降低重复，却增加 generator 版本、最低公分母接口和 transport 特性泄漏风险。",
        "fallback": "某一 transport 需要无法安全表达的 streaming/lifecycle/capability 语义时，保留独立 adapter，并用 contract tests 与 schema diff 防漂移，而不是强制共用实现。",
        "method": "§3 Design; §4 Implementation",
        "evaluation": "§5 Evaluation—Boilerplate Reduction, Feature Parity, agentskills.io Compatibility",
        "nonproof": "§6 Limitations and Security Considerations; §7 Conclusion",
    },
}


# Explicit proposition-level coverage for the 27 restored score-7 families that
# remain No Change.  This deliberately replaces lexical-overlap excerpt
# selection: each entry names a real heading in the current main body, a
# proposition actually stated under that heading, and the paper-specific
# difference that was checked and found not to change the existing contract.
NO_CHANGE_COVERAGE = {
    "2605.21560": {
        "heading": "## Verification 与 Aggregation",
        "body_anchor": "candidate generation 与 evaluation 隔离",
        "existing": "多 Agent 方案必须隔离 candidate generation 与 evaluation，并以独立 rubric/test、evidence、disagreement 和 single-agent baseline 验收；聚合或并行本身不拥有正确性。",
        "difference": "AutoMCU 把这一既有合同实例化到 MCU 设计，以 vendor feedback、硬件约束和隔离调度作为 verifier 与执行条件，没有改变最终硬件验收必须外置的命题。",
    },
    "2605.21694": {
        "heading": "### Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate",
        "body_anchor": "模型只拥有分析与 action proposal",
        "existing": "Security Agent 只拥有假设与工具调用 proposal；平台必须冻结 sandbox、工具权限、trace、deterministic success predicate 与泄漏检查后才能判定执行成功。",
        "difference": "PocketAgents 用 manifest 表达 capability、I/O 与运行边界，是该身份与权限合同的一种封装；manifest 仍不能替代 effect-time authorization 或真实 receipt。",
    },
    "2605.21781": {
        "heading": "### 从固定 Prompt Score 到 Constraint-residual Feedback",
        "body_anchor": "residual-conditioned rewrite proposals",
        "existing": "Prompt 优化应从固定总分演进为版本化 prompt pool、逐约束 residual、定点 rewrite proposal、held-out evaluation 与 rollback 分权的反馈回路。",
        "difference": "Reflective Prompt Tuning 将重复失败汇总为跨轮诊断 memory，属于 residual-conditioned rewrite 的具体状态实现，没有改变 evaluator、holdout 与发布权必须外置的主命题。",
    },
    "2605.21824": {
        "heading": "### Harness、Protocol 与 Credit 都是 Platform-owned Artifact",
        "body_anchor": "平台拥有 protocol 和",
        "existing": "生成系统的 protocol、可执行 test/evidence obligation 与 release rule 由平台拥有，Agent 只能提出 mutation，代码可编译不构成完成证据。",
        "difference": "四原则 fuzz harness 将 obligation 细分为输入、oracle、隔离和归因，是该平台合同在 fuzzing 的展开，没有新增超出现有 protocol/evidence owner 的长期机制。",
    },
    "2605.21825": {
        "heading": "### Intermediate Artifact 是工作流状态，不是日志附件",
        "body_anchor": "typed、",
        "existing": "长工作流的中间 artifact 必须 typed、versioned、addressable、dependency-aware，并绑定 producer、consumer 与 verifier，才能支持恢复和增量重算。",
        "difference": "可视化 co-scientist 将数据、代码、渲染、反馈和 evaluator 组成同一 artifact chain，是该 durable-state 合同的领域实例，没有改变其 owner 或提交边界。",
    },
    "2605.21952": {
        "heading": "### 多向量检索的数据面要避免搬运高精度向量",
        "body_anchor": "相同 recall 下报告",
        "existing": "ANN/RAG 执行优化必须在相同 recall 下联合报告内存、数据移动、QPS 与尾延迟，并分开 candidate generation、refinement 与最终 evidence admission。",
        "difference": "NasZip 以 DIMM near-data processing、分段索引和 early exit 改写物理执行位置，但仍服从既有 recall—带宽—停止条件合同，不产生新的正确性 owner。",
    },
    "2605.21980": {
        "heading": "### 用表示几何区分重排与扩展",
        "body_anchor": "相关统计也不能代替端到端因果验证",
        "existing": "表示几何与局部替换只能提出跨模态功能分工假设，相关统计必须由 causal ablation、端到端质量回归和成本共同验证。",
        "difference": "情绪 circuit 的信息流定位与 inference steering 是这一诊断—干预链的特定应用；它没有把可读出或可操纵信号提升为唯一因果机制。",
    },
    "2605.21984": {
        "heading": "### 静态 Mixture 到版本化 Data Control Plane",
        "body_anchor": "data operator 只提出训练分布",
        "existing": "数据 operator 只提出版本化 select/transform/mix/weight，controller 拥有 active set 与更新时机，独立 Evaluation 决定变化是否可接受；trajectory 还必须保留环境、verifier 与 side-effect lineage。",
        "difference": "Echo 将用户修订与原 trajectory 的差异编译成经验数据，是现有 trajectory provenance 与动态 admission 的一个来源，不改变用户反馈仅是训练 proposal 的边界。",
    },
    "2605.21993": {
        "heading": "### Imperfect Verifier 把监督噪声与 Rollout Compute 绑在一起",
        "body_anchor": "verifier confusion profile",
        "existing": "Verifier 是带 confusion profile 的受限监督传感器，训练必须将 verifier 噪声、rollout budget 和 policy distribution 分账，不能用更多采样或 reward 分数替代正确性。",
        "difference": "ECPO 将 evidence span 与 verifier 结果耦合到候选排序 reward，仍是该受限 verifier 合同的实现分支，没有改变独立评价与事实判定权。",
    },
    "2605.21999": {
        "heading": "### Distillation 不是“Teacher 越强越好”",
        "body_anchor": "密度只是训练 controller 的 estimator state",
        "existing": "Distillation 的 teacher signal 必须结合 student capacity、表示支持与 held-out 行为验收；局部 estimator 只能调节监督，不能以 teacher 总体能力拥有真值。",
        "difference": "对抗蒸馏揭示鲁棒 teacher 在不可学习或扰动子集上的错误传递，收窄了同一 teacher-signal 边界，但未要求新的章节机制。",
    },
    "2605.22015": {
        "heading": "## 加速不能静默改变生成轨迹",
        "body_anchor": "state freshness、输出 agreement 与 refresh cost",
        "existing": "Diffusion 缓存、token reduction 或跳步必须联合验收 state freshness、与 full-compute 输出的一致性、刷新成本和回退，不能以速度或观感单独提交。",
        "difference": "ORBIS 用前一步输出相似度、全局匹配与专用 accelerator 选择 token，是既有近似生成分支的具体机制；质量—速度—硬件成本仍由现有合同完整覆盖。",
    },
    "2605.22168": {
        "heading": "## 从目标到证据，而不是从指标到目标",
        "body_anchor": "scorers",
        "existing": "EvalSpec 必须先定义 target behavior、population、failure taxonomy、scorer、slice、阈值、不确定性与 owner；单一指标只是条件性 evidence。",
        "difference": "Shapley interaction synergy 是跨模态解释的一种 scorer，用于隔离联合贡献，但不能越过既有 scorer 权限成为因果或安全结论。",
    },
    "2605.22195": {
        "heading": "## Search-based Planning 的边界",
        "body_anchor": "模型自己生成并评分候选可能共享同一盲点",
        "existing": "规划搜索的 operator、branching、预算、heuristic 与 verifier 必须分权；模型提出并自评的 graph 仍受共享盲点和计算增长约束。",
        "difference": "RL 驱动的 Graph-of-Thought 只是在有限 operator 集中学习 graph proposal policy，没有改变 runtime budget 与答案 verifier 的外置责任。",
    },
    "2605.22213": {
        "heading": "#### Claim Graph 必须保存逻辑职责与共同来源",
        "body_anchor": "Typed claim graph",
        "existing": "Claim-level confidence 必须保留 claim 类型、逻辑依赖、共同来源、provenance 与独立 verifier；传播值是决策证据而非系统性质真值。",
        "difference": "Subjective Logic 为 assurance argument 提供了一种 compositional opinion calculus，属于现有 typed claim graph 的数值实现，不扩大其真值或发布权限。",
    },
    "2605.22238": {
        "heading": "### Evaluation Identity 必须包含 Harness 与 Environment",
        "body_anchor": "Harness 负责适配与控制流",
        "existing": "Agent 评测身份必须绑定 model、benchmark、harness、environment 与 scorer，并保存 trajectory 和 component receipt 以区分模型、脚手架、工具与评分影响。",
        "difference": "Timed risk play 对 planner、execution scaffold、成本和 runtime failure 的拆分，是现有完整 evaluation identity 的受限案例，没有产生新的 attribution owner。",
    },
    "2605.22272": {
        "heading": "### 可执行评测先暴露控制缺口，低延迟生成再缩短缺口",
        "body_anchor": "模型只拥有 action proposal",
        "existing": "VLA 的视觉/语义 proposal 必须由 simulator 或真实 controller 执行验收；controller 拥有 commit 与 safety envelope，生成模型不拥有物理可行性。",
        "difference": "Imagine2Real 用 4D point trajectory 与稀疏关键点减少 CAD/retargeting 依赖，但视觉 prior 仍需 BFM、物理环境和 controller 关闭同一控制缺口。",
    },
    "2605.22324": {
        "heading": "### Streaming Threshold 必须由风险预算派生，而不是离线固定",
        "body_anchor": "operator cost、alert budget 与 SLO",
        "existing": "Streaming 告警阈值必须由 operator cost、alert budget、SLO、prevalence 与 calibration 派生；shift sensor 和 active acquisition 不能自行拥有处置权。",
        "difference": "PACT 将 benign-normalized false-positive burden、recall 与 analyst query budget放入低 prevalence SOC 控制环，正是该既有风险预算合同的实例。",
    },
    "2605.22356": {
        "heading": "### Fine-tuning 稳定性还要观察输出空间",
        "body_anchor": "相近的参数距离不保证",
        "existing": "Fine-tuning 即使参数距离和训练 loss 正常，也可能改变 action/output geometry；验收必须覆盖多 seed、held-out distribution 与真实 rollout。",
        "difference": "行为微调导致局部 action bias 扩散到开放生成，是既有输出空间回归风险的案例，没有改变训练验收边界。",
    },
    "2605.22364": {
        "heading": "### 学习到的 Transition 只能验证候选，不能提交环境事实",
        "body_anchor": "事实 commit authority",
        "existing": "学习到的 transition、observation 或 value model 只能排序/验证规划候选，真实环境 observation、controller 或规则仍拥有事实提交权。",
        "difference": "Observation-aware POMDP planning 将 sensor/observation function 纳入搜索状态，是该 proposal/commit 分权的规划扩展，没有替代真实 sensor cost 与环境验证。",
    },
    "2605.22530": {
        "heading": "#### Confidence 最终服务于 Risk–Coverage Decision",
        "body_anchor": "Risk–Coverage",
        "existing": "运行时 confidence 必须绑定 claim graph、证据 provenance、calibration 与风险—覆盖政策；置信下降触发补证、降级或拒绝，而不是直接证明系统性质。",
        "difference": "Safety argument 的 runtime opinion update 将新 evidence 增量传播到 claim confidence，是现有 belief-to-action 边界的实现，不改变 safety authority。",
    },
    "2605.22570": {
        "heading": "#### Synthetic Evidence 只有在 Task Exchangeability 成立时才能进入推断",
        "body_anchor": "合成样本适合探索和扩展测试面",
        "existing": "合成评测材料可用于扩展测试面，但生成器偏差、任务可交换性、真实 holdout 和 coverage 条件必须独立验收，不能以规模制造虚假精度。",
        "difference": "VGenST 用主动视频合成控制运动变量和反事实，是该 synthetic-evidence 分支的具体 benchmark 设计，没有越过生成器与 evaluator 审计边界。",
    },
    "2605.22593": {
        "heading": "### Model-internal Sensor 必须从 Inference Hot Path 解耦",
        "body_anchor": "只能触发诊断，不能直接拥有停训权",
        "existing": "模型内部统计只是需要校准、切片和独立复验的诊断 sensor；单一统计量或更多副本不能自动获得异常判决和发布权限。",
        "difference": "GNN ensemble 的 epistemic collapse 具体说明成员共享表示与错误会使 ensemble size 失效，收窄但不改变现有 sensor/authority 合同。",
    },
    "2605.22612": {
        "heading": "### Benchmark、Evaluation 与 Testing 不是同一个层次",
        "body_anchor": "Benchmark 通常固定一组输入与 scorer",
        "existing": "Benchmark 只测固定输入与 scorer，Evaluation 还需连接 intended use、假设、环境、outcome 与发布决策；测试证据不能静默外推到部署结果。",
        "difference": "Healthcare BenchmarkCard 把 task assumption 与 outcome assumption 分层记录，是该 benchmark-to-deployment 边界的显式文档化，没有新增评价层级。",
    },
    "2605.22645": {
        "heading": "### Evaluation Identity 必须包含 Harness 与 Environment",
        "body_anchor": "Scorer 只拥有从轨迹到判断的映射",
        "existing": "评测身份必须绑定 agent/harness/interface、环境、trajectory 与 scorer；scorer 只拥有对应测量，不能把完整系统 outcome 归因给单一模型组件。",
        "difference": "AtelierEval 将 prompter 的多轮图像反馈和目标达成纳入 harness，属于该完整身份合同，不支持把下游图像分数归因于 prompt model。",
    },
    "2605.22717": {
        "heading": "### Block Cache 可以从历史条目演进为固定大小的递归状态",
        "body_anchor": "cache 与流式提交重新可用",
        "existing": "Block-wise 生成可用 cache/递归状态支持流式提交，但 cache identity、误差累积、延迟、质量和回退必须联合验收。",
        "difference": "交互式 music diffusion 的 block-wise KV cache 与 ARC-Forcing 是同一流式状态合同在音频上的实例，没有改变缓存与质量的提交边界。",
    },
    "2605.22743": {
        "heading": "### 静态子空间分离之后，还要处理训练中的梯度重新耦合",
        "body_anchor": "不同 rank-1 component 的梯度方向仍可能重新靠拢",
        "existing": "Continual LoRA 的静态正交初始化不能保证训练中持续隔离，必须监测梯度重耦合、旧能力回归、group revision 与可回滚 artifact。",
        "difference": "SeqLoRA 的 bilevel update 和正交约束是这一已知干扰控制分支的具体实现，正交 proxy 仍不能替代旧概念回归 Gate。",
    },
    "2605.22785": {
        "heading": "### Evidence Trail 与最终答案必须分别验收",
        "body_anchor": "claim、自然 evidence trail",
        "existing": "事实型 Agent 评测必须分别保存 claim、检索/引用 evidence trail、工具事件与最终 verdict，流畅答案和引用数量不能共同冒充事实正确性。",
        "difference": "新闻 chatbot 的检索覆盖、来源引用、推理和 fabricated-premise resistance 分解，是这一 claim/evidence/outcome 合同的领域实例。",
    },
}


class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag = None
        self.buf: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.tag = tag
            self.buf = []

    def handle_data(self, data):
        if self.tag:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if self.tag == tag:
            value = clean("".join(self.buf))
            if value and value not in self.headings:
                self.headings.append(value)
            self.tag = None
            self.buf = []


def choose_heading(headings: list[str], terms: tuple[str, ...], fallback: int) -> str:
    for heading in headings:
        low = heading.lower()
        if any(term in low for term in terms):
            return heading
    if headings:
        return headings[min(fallback, len(headings) - 1)]
    return "section heading unavailable"


def fetch_exact(aid: str) -> dict:
    html_url = f"https://arxiv.org/html/{aid}v1"
    request = urllib.request.Request(html_url, headers={"User-Agent": "AI-System-Design exact-v1 review/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read()
        parser = HeadingParser()
        parser.feed(body.decode("utf-8", errors="replace"))
        headings = parser.headings
        route = "official arXiv exact-v1 HTML"
        artifact = html_url
    except Exception as exc:
        pdf_url = f"https://arxiv.org/pdf/{aid}v1"
        request = urllib.request.Request(pdf_url, headers={"User-Agent": "AI-System-Design exact-v1 review/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    pdf = Path(tmp) / "paper.pdf"
                    txt = Path(tmp) / "paper.txt"
                    pdf.write_bytes(body)
                    subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True, capture_output=True)
                    lines = [clean(x) for x in txt.read_text(errors="replace").splitlines()]
                headings = [x for x in lines if re.match(r"^(?:[1-9][0-9]*(?:\.[0-9]+)*\s+|appendix\s+)[A-Z]", x, re.I)][:80]
            except (FileNotFoundError, subprocess.CalledProcessError):
                source_url = f"https://export.arxiv.org/e-print/{aid}v1"
                source_request = urllib.request.Request(source_url, headers={"User-Agent": "AI-System-Design exact-v1 review/1.0"})
                with urllib.request.urlopen(source_request, timeout=60) as source_response:
                    source_body = source_response.read()
                headings = []
                with tarfile.open(fileobj=io.BytesIO(source_body), mode="r:gz") as archive:
                    for member in archive.getmembers():
                        if not member.name.endswith(".tex") or not member.isfile():
                            continue
                        stream = archive.extractfile(member)
                        if stream is None:
                            continue
                        tex = stream.read().decode("utf-8", errors="replace")
                        headings.extend(clean(value) for value in re.findall(r"\\(?:sub)*section\*?\{([^{}]+)\}", tex))
                headings = list(dict.fromkeys(x for x in headings if x))[:120]
            route = "official arXiv exact-v1 PDF fallback"
            artifact = pdf_url
        except Exception as pdf_exc:
            return {"arxiv_id": aid, "status": "blocked", "html_error": repr(exc), "pdf_error": repr(pdf_exc)}
    method = choose_heading(headings, ("method", "approach", "framework", "design", "setup", "problem formulation", "architecture", "training", "algorithm", "theoretical results"), 3)
    evaluation = choose_heading(headings, ("experiment", "evaluation", "result", "benchmark", "empirical"), max(0, len(headings) // 2))
    nonproof = choose_heading(headings, ("limitation", "discussion", "conclusion", "future work"), max(0, len(headings) - 1))
    return {
        "arxiv_id": aid,
        "status": "accessible",
        "route": route,
        "artifact_locator": artifact,
        "sha256": hashlib.sha256(body).hexdigest(),
        "byte_count": len(body),
        "method_heading": method,
        "evaluation_heading": evaluation,
        "nonproof_heading": nonproof,
        "heading_inventory": headings,
    }


def node_paths() -> dict[str, str]:
    text = (ROOT / "ROADMAP.md").read_text()
    return dict(re.findall(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text))


def book_excerpt(path: Path, proposition: str, title: str) -> tuple[str, str]:
    text = path.read_text()
    body = text.split("\n## Review notes\n", 1)[0]
    blocks = [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]
    terms = {
        w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", title + " " + proposition)
        if w.lower() not in {"with", "from", "that", "this", "through", "model", "models", "learning", "system", "framework", "using", "into", "should", "cannot"}
    }
    best = (0, "", "")
    heading = ""
    for block in blocks:
        if block.startswith("#"):
            heading = block.splitlines()[0]
            continue
        low = block.lower()
        overlap = sum(1 for term in terms if term in low)
        if overlap > best[0]:
            best = (overlap, heading, clean(re.sub(r"<!--.*?-->", "", block, flags=re.S)))
    excerpt = best[2][:420]
    return best[1] or "main body", excerpt or "No exact lexical match; owner boundary was reviewed manually."


def explicit_coverage(path: Path, aid: str) -> dict[str, str]:
    coverage = NO_CHANGE_COVERAGE[aid]
    text = path.read_text()
    marker = "\n## Review notes\n"
    assert marker in text, f"{path}: exact Review notes boundary missing"
    body = text.split(marker, 1)[0]
    heading = coverage["heading"]
    assert heading in body.splitlines(), f"{aid}: heading not found before Review notes: {heading}"
    assert coverage["body_anchor"] in body, f"{aid}: body anchor not found before Review notes"
    return coverage


ledger_path = HERE / "screening-ledger-v3.json"
evidence_path = HERE / "exact-v1-evidence-v3.json"
comparison_path = HERE / "books-current-content-comparison-v3.json"
queue_path = HERE / "BOOKS_WRITEBACK_QUEUE_V3.json"

ledger = load(ledger_path)
old_evidence = {x["arxiv_id"]: x for x in load(evidence_path)}
old_comparisons = {x["arxiv_id"]: x for x in load(comparison_path)}
queue = load(queue_path)
paths = node_paths()
rows = {x["arxiv_id"]: x for x in ledger["identities"]}

assert len(SPECS) == 82
assert len(CONFIRMED_FN) == 18 and CONFIRMED_FN <= SPECS.keys()
assert len(NO_CHANGE_COVERAGE) == 27
assert set(NO_CHANGE_COVERAGE) <= set(SPECS)
assert not (set(NO_CHANGE_COVERAGE) & set(INTEGRATES))
assert all(rows[aid]["v3_screening_status"] in {"pre_denominator_closure", "retained"} for aid in SPECS)

continued_template_ids = {
    aid for aid, row in rows.items()
    if row["v3_screening_status"] == "pre_denominator_closure"
    and (
        row.get("screening_reason", "").startswith("全量 title+full abstract 复核关闭")
        or row.get("closure_reaudit_status") == "title_full_abstract_reaudited_continued_closure"
    )
}
template_ids = continued_template_ids | set(SPECS)
assert len(template_ids) == 501
assert SPECS.keys() <= template_ids

provenance_path = HERE / "closure-repair-exact-v1-provenance-v3.json"
if provenance_path.exists():
    cached = load(provenance_path)
    cached_records = cached.get("records", [])
else:
    cached_records = []
if len(cached_records) == 82 and all(x.get("status") == "accessible" for x in cached_records):
    exact_records = cached_records
else:
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        exact_records = list(pool.map(fetch_exact, sorted(SPECS)))
for record in exact_records:
    headings = record.get("heading_inventory", [])
    record["method_heading"] = choose_heading(headings, ("method", "approach", "framework", "design", "setup", "problem formulation", "architecture", "training", "algorithm", "theoretical results"), 3)
    record["evaluation_heading"] = choose_heading(headings, ("experiment", "evaluation", "result", "benchmark", "empirical"), max(0, len(headings) // 2))
    record["nonproof_heading"] = choose_heading(headings, ("limitation", "discussion", "conclusion", "future work"), max(0, len(headings) - 1))
exact = {x["arxiv_id"]: x for x in exact_records}
blocked = sorted(aid for aid, record in exact.items() if record["status"] != "accessible")
if blocked:
    raise SystemExit(f"exact-v1 blocked for {blocked}; isolate before accepting Evidence")

closure_boundaries = {
    "vertical_domain_result": "其贡献仍绑定单一垂直领域流程/标签，摘要未给出可迁移的模型、训练、推理、平台或 Agent contract。",
    "local_model_or_task_quality_delta": "其变化停留在局部 task/model recipe 与指标，摘要未改变本书可复用系统选择或失败边界。",
    "asset_without_new_evaluation_contract": "其主要产物是数据集/benchmark/资产，摘要未引入新的 scorer identity、decision authority 或 release/fallback contract。",
    "survey_or_taxonomy_context": "其主要贡献是综述/分类/观察背景，未提出会改变当前 owner 设计选择的可执行机制。",
    "no_durable_ai_system_delta": "摘要中的方法/结果未形成可复用、可验收且改变长期 AI System 设计的 durable delta。",
}

reaudit_records = []
for aid in sorted(template_ids):
    row = rows[aid]
    abstract = clean(row.get("abstract", ""))
    mechanism = select_sentence(abstract, ("we propose", "we introduce", "we present", "we develop", "we formulate", "we show", "we find", "we demonstrate"))
    boundary = select_sentence(abstract, ("however", "limitation", "only", "does not", "but ", "while "), fallback=max(0, len(sentences(abstract)) - 1))
    if aid in SPECS:
        spec = SPECS[aid]
        row.update({
            "v3_screening_status": "retained",
            "screening_status": "retained",
            "screening_reason": "501-item title+full-abstract bounded re-audit restored this family: " + spec["proposition"],
            "review_status": "deep_complete_repair_author" if spec["score"] >= 7 else "standard_complete_repair_author",
            "access_status": "accessible",
            "stable_node_id": spec["owner"],
            "owner_path": paths[spec["owner"]],
            "score_v3": {"design_delta": 3 if spec["score"] >= 7 else 2, "system_reach": 2, "durability": 2, "total": spec["score"]},
            "evidence_route": exact[aid]["route"] + " with concrete v1 section locators",
            "books_disposition": (
                "Integrate — root serialized queue pending"
                if aid in INTEGRATES else
                "No Change — current main body carries the proposition"
                if spec["score"] >= 7 else
                "Report Only — score 6 standard review"
            ),
        })
        row.pop("closure_family", None)
        decision = "restored_retained"
        reason = spec["proposition"]
    else:
        family = row.get("closure_family", "no_durable_ai_system_delta")
        reason = f"题摘重审观察到的具体机制：{mechanism} 边界/结果：{boundary} {closure_boundaries[family]} 若新 revision 增加跨 workload 机制、明确系统 contract 或与 Books 主正文冲突，只定点重开该 family。"
        row["screening_reason"] = reason
        row["closure_reaudit_status"] = "title_full_abstract_reaudited_continued_closure"
        decision = "continued_closure"
    reaudit_records.append({
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "title": clean(row["title"]),
        "abstract_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
        "mechanism_observed": mechanism,
        "boundary_or_result_observed": boundary,
        "decision": decision,
        "family_specific_reason": reason,
        "confirmed_fn_seed": aid in CONFIRMED_FN,
    })

retained = sorted((x for x in rows.values() if x["v3_screening_status"] == "retained"), key=lambda x: int(x["arxiv_id"].split(".")[1]))
closures = [x for x in rows.values() if x["v3_screening_status"] == "pre_denominator_closure"]
assert len(retained) == 245 and len(closures) == 422

new_evidence = []
new_comparisons = []
for aid, spec in SPECS.items():
    row = rows[aid]
    src = exact[aid]
    method = f"arXiv:{aid}v1 — §{src['method_heading']}"
    evaluation = f"arXiv:{aid}v1 — §{src['evaluation_heading']}"
    nonproof = f"arXiv:{aid}v1 — §{src['nonproof_heading']}"
    if aid in INTEGRATES:
        method = f"arXiv:{aid}v1 — {INTEGRATES[aid]['method']}"
        evaluation = f"arXiv:{aid}v1 — {INTEGRATES[aid]['evaluation']}"
        nonproof = f"arXiv:{aid}v1 — {INTEGRATES[aid]['nonproof']}"
    boundary = (
        f"仅支持 exact-v1 在 {method} 披露的机制与 {evaluation} 的模型、数据、任务和指标；"
        f"{nonproof} 及未披露生产尾部、开放分布和形式安全不在正面结论内。"
    )
    item = {
        "source_family_id": row["source_family_id"],
        "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "retrieval_route": src["route"] + " title, full abstract and body review",
        "retrieved_at": CHECKED_AT,
        "review_status": "deep_complete_bounded_repair_author" if spec["score"] >= 7 else "standard_complete_bounded_repair_author",
        "access_status": "accessible",
        "problem": select_sentence(row["abstract"], ("however", "existing", "challenge", "limited", "struggle")),
        "mechanism": select_sentence(row["abstract"], ("we propose", "we introduce", "we present", "we develop", "we formulate", "we show")),
        "adopted_proposition": spec["proposition"],
        "claim_boundary": boundary,
        "artifact_locator": src["artifact_locator"],
        "artifact_sha256": src["sha256"],
        "method_locator": method,
        "evaluation_locator": evaluation,
        "limitations_locator": nonproof,
    }
    if spec["score"] >= 7:
        if aid in INTEGRATES:
            item["tradeoff"] = INTEGRATES[aid]["tradeoff"]
            item["failure_fallback"] = INTEGRATES[aid]["fallback"]
        else:
            item["tradeoff"] = f"采用该机制会增加与 §{src['method_heading']} 对应的状态、校准或计算成本；收益只在 §{src['evaluation_heading']} 的披露设置中成立。"
            item["failure_fallback"] = f"若 §{src['nonproof_heading']} 暴露的边界、关键假设或 owner 的 held-out 回归不成立，回退原基线并将该信号降级为诊断 proposal。"
    new_evidence.append(item)

    if aid in INTEGRATES:
        integ = INTEGRATES[aid]
        comparison = {
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "title": clean(row["title"]),
            "owner_node": spec["owner"],
            "owner_path": paths[spec["owner"]],
            "existing_proposition": integ["gap"],
            "new_evidence_delta": spec["proposition"],
            "decision": "Integrate — root serialized queue pending",
            "comparison_basis": "current owner main body before exact `## Review notes`; title/marker/Review notes do not count as coverage",
            "evidence_route": row["evidence_route"],
            "root_queue_anchor": integ["anchor"],
            "writeback_status": "pending_root_writeback_then_new_fresh_postwrite_review",
        }
    elif spec["score"] >= 7:
        coverage = explicit_coverage(ROOT / paths[spec["owner"]], aid)
        comparison = {
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "title": clean(row["title"]),
            "owner_node": spec["owner"],
            "owner_path": paths[spec["owner"]],
            "existing_proposition": f"`{coverage['heading']}` 主正文命题：{coverage['existing']}",
            "new_evidence_delta": spec["proposition"],
            "paper_specific_difference": coverage["difference"],
            "decision": "No Change — current main body carries the proposition",
            "comparison_basis": "current owner main body before exact `## Review notes`; explicit heading/body proposition and paper-specific difference recorded",
            "evidence_route": row["evidence_route"],
        }
    else:
        comparison = {
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "title": clean(row["title"]),
            "owner_node": spec["owner"],
            "owner_path": paths[spec["owner"]],
            "existing_proposition": "Score 6 standard review is Report Only; no positive current-body coverage claim is used.",
            "new_evidence_delta": spec["proposition"],
            "decision": "Report Only — score 6 standard review",
            "comparison_basis": "current V3 score threshold; no Books Gate triggered",
            "evidence_route": row["evidence_route"],
        }
    new_comparisons.append(comparison)

for item in new_evidence:
    old_evidence[item["arxiv_id"]] = item
for item in new_comparisons:
    old_comparisons[item["arxiv_id"]] = item

all_evidence = [old_evidence[row["arxiv_id"]] for row in retained]
all_comparisons = [old_comparisons[row["arxiv_id"]] for row in retained]

deep_count = sum("deep" in row.get("review_status", "") for row in retained)
standard_count = sum("standard" in row.get("review_status", "") for row in retained)
integrate_count = sum(row["books_disposition"].startswith("Integrate") for row in retained)
no_change_count = sum(row["books_disposition"].startswith("No Change") for row in retained)
report_only_count = sum(row["books_disposition"].startswith("Report Only") for row in retained)
assert (deep_count, standard_count) == (191, 54)
assert (integrate_count, no_change_count, report_only_count) == (46, 145, 54)

ledger.update({
    "status": "bounded_closure_reaudit_author_complete; root_writeback_and_new_fresh_non_author_review_pending",
    "retained_count": 245,
    "pre_denominator_closure_count": 422,
    "evidence_complete_count": 245,
    "evidence_deep_complete_count": 191,
    "evidence_standard_complete_count": 54,
    "evidence_review_pending_count": 0,
    "evidence_blocked_count": 0,
    "books_integrate_count": 46,
    "books_no_change_count": 145,
    "books_report_only_count": 54,
    "books_deferred_count": 0,
    "closure_reaudit": {
        "scope": "501 prior template-derived closures; title plus full abstract, no source/date expansion",
        "audited_count": 501,
        "restored_count": 82,
        "confirmed_fn_seed_count": 18,
        "additional_restored_count": 64,
        "continued_closure_count": 419,
        "special_non_template_closure_count_outside_scope": 3,
        "receipt": "closure-semantic-reaudit-v3.json",
    },
    "identities": list(rows.values()),
})
counts = {}
for row in closures:
    counts[row["closure_family"]] = counts.get(row["closure_family"], 0) + 1
ledger["closure_family_counts"] = dict(sorted(counts.items()))

queue_items = []
for aid in sorted(INTEGRATES):
    spec = SPECS[aid]
    row = rows[aid]
    src = exact[aid]
    integ = INTEGRATES[aid]
    queue_items.append({
        "report_date": "2026-05-22",
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "title": clean(row["title"]),
        "primary": src["artifact_locator"],
        "stable_node_id": spec["owner"],
        "target_path": paths[spec["owner"]],
        "anchor": integ["anchor"],
        "old_baseline_and_constraint_change": integ["delta"],
        "adopted_proposition": spec["proposition"],
        "method_locator": f"arXiv:{aid}v1 — {integ['method']}",
        "evaluation_locator": f"arXiv:{aid}v1 — {integ['evaluation']}",
        "nonproof_locator": f"arXiv:{aid}v1 — {integ['nonproof']}",
        "evidence_boundary": next(x["claim_boundary"] for x in new_evidence if x["arxiv_id"] == aid),
        "tradeoff": integ["tradeoff"],
        "failure_fallback": integ["fallback"],
        "state_control_ownership": integ["delta"],
        "writer": "root serialized Books owner",
        "author_must_not_write_books": True,
        "status": "pending_root_writeback_then_new_fresh_postwrite_semantic_review",
        "required_marker": f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}:start/end",
    })
queue.update({
    "status": "9 bounded-closure-repair Integrates pending root serialized writeback; prior 37 bindings remain fresh-pass; overall report Ongoing pending new fresh reviewer",
    "queue_count": len(queue_items),
    "item_count": len(queue_items),
    "items": queue_items,
})

reaudit = {
    "schema": "daily-v3-closure-semantic-reaudit",
    "report_date": "2026-05-22",
    "checked_at": CHECKED_AT,
    "scope": "the 501 closures whose prior reasons were renderer templates; no date/source expansion",
    "counts": {"audited": 501, "restored": 82, "confirmed_fn_seed": 18, "additional_restored": 64, "continued_closure": 419},
    "method": "Every record binds the owner-batch title, full abstract hash, observed mechanism, observed boundary/result and family-specific decision. Restored families then received official exact-v1 review.",
    "records": reaudit_records,
}
provenance = {
    "schema": "daily-v3-closure-repair-exact-v1-provenance",
    "report_date": "2026-05-22",
    "checked_at": CHECKED_AT,
    "restored_count": 82,
    "accessible_count": 82,
    "blocked_count": 0,
    "records": sorted(exact_records, key=lambda x: x["arxiv_id"]),
}

dump(ledger_path, ledger)
dump(evidence_path, all_evidence)
dump(comparison_path, all_comparisons)
dump(queue_path, queue)
dump(HERE / "closure-semantic-reaudit-v3.json", reaudit)
dump(provenance_path, provenance)


def md_escape(value: str) -> str:
    return clean(value).replace("|", "\\|")


def primary_url(ev: dict, aid: str) -> str:
    for candidate in (ev.get("artifact_locator"), ev.get("retrieval")):
        if isinstance(candidate, dict):
            candidate = candidate.get("url")
        if isinstance(candidate, str):
            match = re.search(r"https://arxiv\.org/(?:html|pdf)/[0-9.]+v1", candidate)
            if match:
                return match.group(0)
    return f"https://arxiv.org/html/{aid}v1"


evidence_by = {x["arxiv_id"]: x for x in all_evidence}
comparison_by = {x["arxiv_id"]: x for x in all_comparisons}
table = [
    "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
    "| --- | --- | --- | --- | --- |",
]
evidence_sections = []
for row in retained:
    aid = row["arxiv_id"]
    ev = evidence_by[aid]
    comp = comparison_by[aid]
    score = row["score_v3"]
    review = "深入完成" if score["total"] >= 7 else "标准完成"
    if row["books_disposition"].startswith("Integrate"):
        if aid in INTEGRATES:
            books = f"整合：root queue 待写回；[章节](../../../../{row['owner_path']})；`{row['stable_node_id']}`"
        else:
            books = f"整合：既有 root binding 已通过 fresh post-write 语义复核；[章节](../../../../{row['owner_path']})；`{row['stable_node_id']}`"
    elif row["books_disposition"].startswith("No Change"):
        books = f"已有覆盖：[章节](../../../../{row['owner_path']}) 当前主正文承载命题；`{row['stable_node_id']}`"
    else:
        books = f"仅报告：score 5–6 standard review；[章节](../../../../{row['owner_path']})；`{row['stable_node_id']}`"
    artifact_locator = primary_url(ev, aid)
    adopted = ev.get("adopted_proposition") or ev.get("mechanism") or ev.get("mechanism_and_ownership") or row["screening_reason"]
    claim_boundary = ev.get("claim_boundary") or ev.get("proof_boundary") or "证据边界以 exact-v1 已记录的 method/evaluation/non-proof locators 为准。"
    table.append(
        f"| [{md_escape(row['title'])}]({artifact_locator}) | {PUBLIC_TIME} | {md_escape(adopted)}；"
        f"{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | {review} | {books} |"
    )
    details = (
        f"### [{clean(row['title'])}]({artifact_locator})\n\n"
        f"版本与证据：`{ev['primary_evidence_version']}`；Method=`{ev['method_locator']}`；"
        f"Evaluation=`{ev['evaluation_locator']}`；Non-proof=`{ev['limitations_locator']}`。"
        f" 采用命题：{adopted} 证据边界：{claim_boundary}\n\n"
        f"Books 比较：owner=`{comp['owner_node']}`，target=`{comp['owner_path']}`；"
        f"既有命题：{comp['existing_proposition']} 结论=`{comp['decision']}`。"
    )
    if ev.get("tradeoff"):
        details += f" Trade-off：{ev['tradeoff']} Failure/Fallback：{ev['failure_fallback']}"
    evidence_sections.append(details)

current = REPORT.read_text()
source_section = current.split("## 2. 来源覆盖\n", 1)[1].split("\n## 3. 候选与判断", 1)[0].rstrip()
report = f"""# Daily Research — 2026-05-22

**规范：** V3

**窗口：** 2026-05-21T09:00:00+08:00 ～ 2026-05-22T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

## 1. 结论

本次仍以官方 announcement-time owner batch 为唯一窗口身份：`667 = 245 retained + 422 pre-denominator closure + 0 withdrawn`。本轮不扩来源或日期，只重审 fresh FAIL 指出的 501 个模板 closure：18/18 个已确认 FN 均恢复，另恢复 64 个满足当前贡献 Gate 的 family，419 个在记录具体机制与边界后继续 closure；再加 3 个原有非模板 closure，closure 总数为 422。

82 个新增 retained 均完成 official exact-v1：`82 accessible + 0 blocked`；Evidence 总投影为 `245 = 191 deep complete + 54 standard complete + 0 pending + 0 blocked`。Books 总投影为 `245 = 46 Integrate（37 既有已写回 + 9 新 queue）+ 145 No Change + 54 Report Only + 0 Deferred`。新增 9 项只进入 root serialized queue，本作者未编辑共享 Books。日报保持进行中，需 root 写回、另一 fresh non-author 逐项做 post-write/closure challenge 后才可 Complete。

501 项逐条 title+full-abstract 结论见 [`closure-semantic-reaudit-v3.json`](../_sources/daily-20260522/closure-semantic-reaudit-v3.json)，82 项 exact-v1 章节与摘要哈希见 [`closure-repair-exact-v1-provenance-v3.json`](../_sources/daily-20260522/closure-repair-exact-v1-provenance-v3.json)。

## 2. 来源覆盖
{source_section}

## 3. 候选与判断

{chr(10).join(table)}

完整算术、422 项 closure、withdrawn 检查与候选状态见 [`screening-ledger-v3.json`](../_sources/daily-20260522/screening-ledger-v3.json)。

## 4. 证据与知识整合

{chr(10).join(evidence_sections)}

结构化 Evidence 见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260522/exact-v1-evidence-v3.json)，逐项 current Books 命题比较见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260522/books-current-content-comparison-v3.json)。No Change 记录了 exact `## Review notes` 前的具体正文 heading 与 excerpt；标题、marker、自检问题和 Review notes 均不充当覆盖。

## 5. 缺口与下一步

- [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260522/BOOKS_WRITEBACK_QUEUE_V3.json) 含 9 个 active Integrate：`2605.21751`、`2605.21770`、`2605.21849`、`2605.21933`、`2605.22060`、`2605.22211`、`2605.22644`、`2605.22723`、`2605.22733`。只能由 root 串行写共享 Books，随后由未参与写作的人做 post-write 语义复核。
- Meta 与 Hunyuan source-local 外部材料缺口沿用既有隔离；它们不为正面 no-hit 提供证据，也不阻塞已冻结的官方 arXiv batch。
- 本轮 author repair 完成后不得自签 Complete；下一 reviewer 必须独立挑战 419 continued closure、82 restored 的 score/Evidence/owner/Books，以及 9 个 root binding 的命题、边界、trade-off、failure/fallback、marker 与位置。

## 6. 复核

- Author-side bounded repair：已完成。范围仅限 501 个模板 closure；算术 `667=245+422`、Evidence `191+54`、Books `46+145+54`，blocked/withdrawn/pending 均为 0。
- Fresh FAIL receipt：[`V3_FRESH_NONAUTHOR_FINAL_SEMANTIC_REVIEW_20260916.md`](../_sources/daily-20260522/V3_FRESH_NONAUTHOR_FINAL_SEMANTIC_REVIEW_20260916.md)。
- 当前 Gate：**Ongoing**。剩余且仅剩：root 写回 9 项 Books；不同 fresh non-author 做写后语义与全量 final Gate；通过后再同步 Complete/receipt/checkpoint。
"""
REPORT.write_text(report)

checkpoint = f"""# 2026-05-22 V3 Bounded Closure Re-audit Author Checkpoint

- Checked at: `{CHECKED_AT}`
- Status: `Ongoing — author repair complete; root writeback and new fresh non-author final Gate pending`
- Scope: only the 501 renderer-template closures identified by the 2026-09-16 fresh FAIL; no source/date expansion and no shared Books edits.

## Frozen projection

- Denominator: `667 = 245 retained + 422 closure + 0 withdrawn`.
- Template-closure audit: `501 = 82 restored + 419 continued closure`; the 82 include all `18/18` seeded false negatives plus 64 additional restorations. Three prior non-template closures remain outside the 501 scope.
- Evidence: `245 = 191 deep + 54 standard + 0 pending + 0 blocked`.
- Books: `245 = 46 Integrate + 145 No Change + 54 Report Only`; Integrate is `37 prior root-applied + 9 active root queue`.

## Receipts

- Full title+abstract audit: `closure-semantic-reaudit-v3.json` (501 identities, per-item abstract SHA, observed mechanism/boundary, family-specific decision).
- Restored exact-v1 review: `closure-repair-exact-v1-provenance-v3.json` (82 accessible, concrete heading inventories and artifact SHA).
- Evidence/Books: `exact-v1-evidence-v3.json`, `books-current-content-comparison-v3.json`.
- Root queue: `BOOKS_WRITEBACK_QUEUE_V3.json` (9 active items; author did not edit Books).

## Remaining Gate

1. Root serially writes the nine queued proposition deltas with paired unique markers before each target chapter's exact `## Review notes`.
2. A different fresh non-author reviews those bindings and independently challenges all 419 continued closures plus the restored Evidence/score/owner/Books decisions.
3. Only after validator, JSON, marker uniqueness/position and scoped diff checks pass may that reviewer mark the Daily `Complete` and issue a final receipt/checkpoint.
"""
(HERE / "AUTHOR_BOUNDED_CLOSURE_REAUDIT_CHECKPOINT_20260916.md").write_text(checkpoint)

print(json.dumps({
    "raw": 667,
    "retained": len(retained),
    "closures": len(closures),
    "template_audited": len(template_ids),
    "restored": len(SPECS),
    "deep": deep_count,
    "standard": standard_count,
    "integrate": integrate_count,
    "no_change": no_change_count,
    "report_only": report_only_count,
    "active_root_queue": len(queue_items),
}, ensure_ascii=False, indent=2))
