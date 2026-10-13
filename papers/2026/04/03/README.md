# Daily Research — 2026-04-03

**规范：** V3

**窗口：** 2026-04-02T09:00:00+08:00 ～ 2026-04-03T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** 2026-10-13T04:54:56+08:00

**补充窗口：** 2026-04-02 ～ 2026-04-02

**冻结候选日期：** [补查前原报告](../_sources/daily-20260403/baseline-before-supplement-20261013.md)

**窗口说明：** 用户授权仅补既有 Daily 的来源遗漏；原窗口、62 个候选的身份/公开时间/评分及连续 §4 保持不变，新增仅检查前一个完整北京时间自然日。原完成与复核声明仅指原轮，不代替本轮验收。

## 1. 结论

**2026-10-13 增量运行态：** 本轮仅补 04-02 自然日，原62个家族不搬移日期。本轮发现已停在四主题220槽/186去重身份、官方有限标题prefix129槽；实际68完整题摘而非全部命中贡献。当前正式新增35家族、总97：31实际Books整合、2仅报告、2中心争议隔离；这些具体出口与31实际POST均独核通过。有限集合作者必要core已到具体停止，余项独核、Books判断/PRE及最终日级独核仍可执行，不把旧完成标签或已读摘要当本轮通过。14源实际停点及历史slice限制在§2/5，具体分层停点见[本轮校准与进展](../_sources/daily-20260403/SUP_ADMISSION_20261013.md)。

本日报窗口左闭右开。[旧 V2.1 报告](../_sources/daily-20260403/LEGACY_V21_REPORT.md)曾以 DataCite DOI 入库日代理首次公开，登记 530 个 arXiv 身份和 37 个候选；不能继承这个日期口径及模板化审阅。旧筛选账本有 538 个身份，其中 400 个落在相邻 arXiv 公告批次支持的可能当窗 ID 范围，这 **400 个不是贡献候选**。已按具体题摘重判旧 39 个 retained、浏览缓存标题并对可能漏项补读完整摘要；另补旧库存未含的 `.01226–.01513` 官方主题列表前缀。独立否定侧校准发现不能以“小规模/无新 owner/已有主题”关闭具体机制或反证，已按共同理由定点重开。最终确认 62 个家族、62 项必要证据写入 §4，其中 47 项实际整合、14 项已有覆盖、1 项 MiCP 阈值争议安全暂缓；全部候选均已获得证据和 Books 处置，并通过非作者日级复核。具体排除依据及实际查漏范围见[审阅记录](../_sources/daily-20260403/V3_REVIEW.md)，不把标题浏览冒充全部全文审阅。

目前最重要的可采用机制是：连续 AR 图像生成中重构质量与可生成性分离；masked diffusion MoE 的专家容量随 mask ratio 调整但不保证每 token 命中 routed expert；NVL72 上以分片权重 peer prefetch 换每层全局 MoE 同步；离散数据的连续 Gaussian diffusion solver 会在特定噪声区间落入低密度模态间；异质 draft 来源决定 speculative tree 的深宽预算；物理行动的 safety layer 即使零告警，也可能因常态限幅改变实际控制命令；旧 monorepo 工具与索引无法重放时，rolling benchmark 改变评测对象而非修复历史等价；多用户 Agent 的善意局部惯例也会经共享可执行状态污染其他用户；归一化与优化器的组合可能静默饱和。主任务已按原始论文与章节对照落实到 `MULTIMODAL-GENERATIVE-PARADIGMS`、`MODEL-MOE`、`INFER-DYNAMO`、`INFER-SPECULATIVE-DECODING`、`MULTIMODAL-EMBODIED-VLA`、`PLATFORM-EVALUATION-SYSTEM`、`AGENT-MEMORY` 和 `TRAIN-PRETRAINING`。这些是受限论文证据，不推出通用 benchmark/SLO 或道路安全结论。

原轮62项已按当时合同闭环：14 个到期来源处理至有界停点或具体外部保留项，必要正文、逐项 Books 处置、写后对读与原轮日级语义验收已落实。此历史声明不覆盖本轮新增与当前普通可执行项。MiCP 中心阈值争议仍不入 Books；历史目录限制分别在 §5 精确隔离，不以它们支持零遗漏。

## 2. 来源覆盖

以下为本轮04-02自然日实际发现停点；原轮来源文字保存在冻结基线，不复用其完成标签。真实query/分页/字段投影和具名跨日去重见[本轮停点](../_sources/daily-20260403/SUP_SOURCE_STOP_20261013.md)，不把来源目录处理与候选Source/Books完成混同。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-ARXIV` | [官方入口](https://export.arxiv.org/api/query)；四主题API submitted线索区间202603311800–202604011800，MODEL65/AGENT82/MULTIMODAL42/RUNTIME31；实际完整分页220槽186身份。12适用主题月列表各仅首20/≤01225前缀129标题槽。 | 已检查 | 标题只线索；63 pinned-v1完整题摘+首批另5=68实际题摘身份，不宣称186已审。19个具名原04-02正式family按same-v1去重，原62不动。日期双向链及必要反证按SUP_DATE_RULE；有限题摘归并/Source尚普通可执行。 |
| `SRC-ANTHROPIC` | [官方入口](https://www.anthropic.com/research)；Research真实publishedOn相邻Mar31T22:17Z→Apr02T10:56Z emotion→Apr07T09:35Z；RSP exact3.1及Apr02 archive。 | 已检查 | emotion原62已选同事件去重；RSP新增单family两关联事件5分仅报告已独核；不采用emotion后Apr09论文或RSP后来目标。 |
| `SRC-OPENAI` | [官方入口](https://openai.com/research/)；官方RSS相邻Apr01T02Z→Apr02T10Z Codex pricing/10:30Z TBPN→Apr06T10Z。两项官方核心已读，计费/公司收购没有新训练/系统机制。 | 受阻 | News关闭，不等Research完整。Research首屏历史Loadmore未恢复，保原精确历史目录HOLD；不把RSS零研究当零研究。 |
| `SRC-GOOGLE-AI` | [官方入口](https://deepmind.google/blog/page/3/)；Research Blog Apr月第一个日值Apr03在窗外；DeepMind News page3触发Gemma4官方Apr02首发核心；DeepMind Publications当前前30日期Apr25→Mar22。 | 受阻 | Gemma首发core已root贡献前EX：variant/既有MoE与模态配置/Apache2声明无新机制/可比条件，不宣称许可放宽；July30卡与2607技术报告不倒灌。GoogleResearch pubs默认与year参数未给first-public历史停点，原HOLD继续。 |
| `SRC-META-AI` | [官方入口](https://ai.meta.com/research/)；Research页面正文0行，Blog当前Apr08→Mar26但非严格历史顺序。 | 受阻 | 原Research本窗历史索引HOLD继续；不以空response或非chronological Blog签零研究。 |
| `SRC-QWEN` | [官方入口](https://qwen.ai/research)；真实dynamic40/static60元数据；04-02仅qwen3.6 date04:00+08。 | 已检查 | 同事件复用原04-02 SRC-QWEN具体EX，受限能力数字与preserve_thinking默认false无新因果机制；不重计候选。 |
| `SRC-DEEPSEEK` | [官方入口](https://deepseek.com/en/news/)；官方News Apr24→Dec01、Research Jun24→Feb25已显示切片。 | 已检查 | 无04-02可见触发；只关闭显示入口有界停点，不宣称ViewAll所有历史/全部仓库活动已扫。 |
| `SRC-MOONSHOT` | [官方入口](https://platform.kimi.com/blog)；Platform Blog最新Nov07 2025，无April历史项；原确切kimi-cli1.30.0 Apr02T14:40Z已有核心版本修补EX。 | 已检查 | 复用原同release具体关闭，非新候选；原Release不是新训练/Agent机制，不由Blog旧首屏证明组织研究零。 |
| `SRC-TENCENT-HUNYUAN` | [官方入口](https://hunyuan.tencent.com/research)；publicList renderType0,page1,size20实际EN9 public字段；显示日期Apr23后到Feb13，publication/更新时间实际有July不能混首公开。 | 已检查 | 无04-02 EN目录触发；EN9不代表全中文/total正文遍历，不扩无触发仓库。 |
| `SRC-BYTEDANCE-SEED` | [官方入口](https://seed.bytedance.com/en/public_papers)；publications article_type1 year2026 token40,count20实际EN18，Apr07T16Z→Mar31T12Z跨窗，next60停止；blog type2 token0,count100实际EN14、has_morefalse，Mar31T16Z→Apr08T16Z。 | 已检查 | 真实EN目录/两个type无本窗触发；wrapper total82/19及站点242不是正文队列，不扫全242。 |
| `SRC-ZAI` | [官方入口](https://www.zhipuai.cn/zh/research)；Research Apr07→Apr01，releaseFeb12→Apr07。 | 已检查 | 无明确Apr02新事件；GLM5VTurbo原Apr01日值缺TZ不补造归属，仅目录边界，不扩未触发仓库。 |
| `SRC-BAIDU-ERNIE` | [官方入口](https://ernie.baidu.com/blog/zh/)；官方Blog日期Apr15→Feb06。 | 已检查 | 所列窗口切片无触发，非组织全仓库零活动。 |
| `SRC-XIAOMI-MIMO` | [官方入口](https://mimo.xiaomi.com/)；官方8 Papers Jun29→Mar13；15 Blog标题未含日期，/blog只旧Dec16 2025 MiMoV2Flash。 | 受阻 | Papers切片无04-02；Blog历史日停点无法恢复，保精确该补充入口限制，不宣称全Blog日期关闭。 |
| `SRC-MINIMAX` | [官方入口](https://www.minimax.io/blog)；主EN博客Mar18→May26，主ZH Mar18→Apr27；TechBlog仅Sep19/Sep22/Oct08。 | 受阻 | 主博客切片无触发；TechBlog历史April停点未恢复，保原精确入口限制，不以当前最早Sep标题签April N/A。 |


## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [RAE-AR `2604.01545v1`](https://arxiv.org/html/2604.01545v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 重构好不等于连续 AR 好；`2+2+3=7` | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Diffusion instruction unlearning `2604.01514v1`](https://arxiv.org/html/2604.01514v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 输出指令无法抹除 CLIP/去噪路径中的目标概念；`2+1+2=5` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的跨 substrate 遗忘验收 |
| [Expert-choice diffusion MoE `2604.01622v1`](https://arxiv.org/html/2604.01622v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | mask ratio 调节 expert capacity；`2+2+2=6` | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [DWDP `2604.01621v1`](https://arxiv.org/pdf/2604.01621v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | peer 分片权重替代全局专家通信；`2+2+3=7` | 深入完成 | 整合：`INFER-DYNAMO` [Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [VideoZeroBench `2604.01569v1`](https://arxiv.org/html/2604.01569v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 答案与时空证据分级；`2+2+2=6` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的模态/时间消融与证据路径 |
| [Discrete Gaussian diffusion `2604.02028v1`](https://arxiv.org/html/2604.02028v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 离散分布的低密度 solver failure mode；`2+2+3=7` | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [PGPO `2604.01840v1`](https://arxiv.org/html/2604.01840v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 视觉依赖代理重分配 token advantage；`2+2+2=6` | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 sequence→token 权重、proxy 限制 |
| [Data Laundering `2604.01904v1`](https://arxiv.org/html/2604.01904v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 原文 MIA 阴性不能排除语义派生样本进入训练；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [World Action Verifier `2604.01985v1`](https://arxiv.org/pdf/2604.01985v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | action-free video 提候选 subgoal，inverse/forward 分歧选下一次真实交互；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Goose `2604.02047v1`](https://arxiv.org/html/2604.02047v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 异质来源 acceptance 决定树深/宽；`2+2+2=6` | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Causal Scene Narration `2604.01723v1`](https://arxiv.org/html/2604.01723v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | safety monitor 的常态限幅即使无告警也改变实际命令；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [ProCeedRL `2604.02006v1`](https://arxiv.org/html/2604.02006v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 失败 action 污染后续 observation；critic 选择性 rewind，`2+2+2=6` | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 的失败 suffix correction、干预 provenance 与回退 |
| [ProdCodeBench `2604.01527v1`](https://arxiv.org/pdf/2604.01527v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 旧 monorepo 不可重放时以当前 head 反向撤销 diff，构造 rolling evaluation；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [No Attacker Needed `2604.01350v1`](https://arxiv.org/html/2604.01350v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 善意局部惯例经共享状态跨用户误用；`2+2+3=7` | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [ES vs GRPO `2604.01499v1`](https://arxiv.org/html/2604.01499v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 目标任务同准确率不代表 off-task 保持或更新几何相同；`2+2+2=6` | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)、`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 held-out gate |
| [Normalization–Optimizer Coupling `2604.01563v1`](https://arxiv.org/html/2604.01563v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | Derf×Muon 静默饱和，组件不可独立挑选；`2+2+3=7` | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Read More, Think More `2604.01535v1`](https://arxiv.org/html/2604.01535v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | Web Agent observation 取舍随模型能力与 reasoning budget 反转；`2+2+2=6` | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Tex3D `2604.01618v1`](https://arxiv.org/pdf/2604.01618v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 物体表面成为跨视角、跨控制时刻攻击面；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Oscar `2604.01624v1`](https://arxiv.org/html/2604.01624v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 跨去噪链分歧只提议局部证据修复，不能自证真值；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ContextBudget `2604.01664v1`](https://arxiv.org/html/2604.01664v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | observation 入窗前按 headroom 选择不压/部分/全部聚合；`2+2+2=6` | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [FlatAttention `2604.02110v1`](https://arxiv.org/html/2604.02110v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | tile-group、NoC collective、HBM IO 与 occupancy 联合选择；`2+2+2=6` | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Batched Contextual Reinforcement `2604.02322v1`](https://arxiv.org/html/2604.02322v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 训练期多题共享 hard cap 形成 token 机会成本；`2+2+2=6` | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [A Simple Baseline for Streaming Video Understanding `2604.02317v1`](https://arxiv.org/html/2604.02317v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 最近帧强基线分离实时感知与历史回忆；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Steerable Visual Representations `2604.02327v1`](https://arxiv.org/html/2604.02327v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 在冻结视觉骨干中间层条件化文本，早晚融合按任务取舍；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Reliable Control-Point Selection `2604.02113v1`](https://arxiv.org/html/2604.02113v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 表面推理边界须经同前缀重采样才可作为 steering proposal；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Reasoning Patterns in Long-CoT SFT `2604.01702v1`](https://arxiv.org/html/2604.01702v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 同题正确轨迹仍可因分叉模式导致学生泛化反转；`2+2+2=6` | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [ActionParty `2604.02330v1`](https://arxiv.org/pdf/2604.02330v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 共享场景里持续主体状态与动作绑定须显式建模；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [BidirLM `2604.02045v1`](https://arxiv.org/html/2604.02045v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | causal 生成骨干转双向检索表示须配目标适配和遗忘回归；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Beyond the Assistant Turn `2604.02315v1`](https://arxiv.org/html/2604.02315v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | assistant 正确率不代理模型对后续用户交互的建模；`2+2+2=6` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 response-conditioned user policy 与多轮评价身份 |
| [From Guessing to Placeholding `2604.01849v1`](https://arxiv.org/html/2604.01849v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 不确定的 IDE 补全细节由用户填空，取决于填空与纠错的相对成本；`2+2+2=6` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 Risk–Coverage 成本裁决；代码填空是受限实例 |
| [Contrastive Context `2604.01601v1`](https://arxiv.org/html/2604.01601v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | SFT 示例相似度结构左右 ICL 与参数记忆的竞争；`2+2+2=6` | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Visual Invariance `2604.01848v1`](https://arxiv.org/html/2604.01848v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 语义丰富图像可能遮盖几何变换不变性缺陷；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Visual Inertia `2604.01989v1`](https://arxiv.org/html/2604.01989v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 对象/属性正确不保证关系推断；静态视觉关注与动态组合可能反向；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Self-Preservation Bias `2604.02174v1`](https://arxiv.org/html/2604.02174v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 被评模型参与自身替换提议时，同指标角色互换与中立对照暴露选择偏差；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PLUME `2604.02073v1`](https://arxiv.org/html/2604.02073v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 显式 CoT 逐步蒸馏为短 latent rollout，改变检索表示的计算预算；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Trace Inversion `2604.02230v1`](https://arxiv.org/html/2604.02230v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 从 reasoning trace 反推被回答的问题，以 query 失配提议弃答；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Skill0 `2604.02268v1`](https://arxiv.org/html/2604.02268v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | paired skill utility 后逐步撤除训练 scaffold；`2+2+2=6` | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)、`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [SRPO `2604.02288v1`](https://arxiv.org/html/2604.02288v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 按 outcome/反馈分流 GRPO 与 self-teacher 更新；`2+2+2=6` | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Learning from the Right Rollouts `2604.01597v1`](https://arxiv.org/html/2604.01597v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | validation-gradient 过滤 PPO rollout，验证集变训练选择信号；`2+2+2=6` | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 trajectory admission 与独立 held-out gate |
| [Anthropic emotion concepts](https://www.anthropic.com/research/emotion-concepts-function) | 2026-04-02T18:56:00+08:00 | 可解码方向的干预与外显文本脱钩；`2+2+2=6` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 内部/外显/干预/部署分账，`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 限定白盒 probe 权限 |
| [LatentUM `2604.02097v1`](https://arxiv.org/html/2604.02097v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 理解约束的语义 codes 可免静态像素往返，但须重新处理与 recache；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Omni123 `2604.02289v1`](https://arxiv.org/html/2604.02289v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 成对预训不能替代 view-conditioned 三模态交错训练；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [FAN `2604.01570v1`](https://arxiv.org/pdf/2604.01570v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 物理动作容差与 one-hot imitation 失配；局部 Gaussian 仍是 policy proxy；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [MiCP `2604.01413v1`](https://arxiv.org/html/2604.01413v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 适应性轮次改变 active-set 校准总体与误差预算；`2+2+2=6` | 争议 | 暂缓：NE-to-frequency 停止阈值未解释，需作者勘误或精确实现；不入 Books，不采用形式保证 |
| [Citation granularity `2604.01432v1`](https://arxiv.org/pdf/2604.01432v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 原子 claim 粒度与支撑 citation 单元不同，固定输入后细分不单调改善 attribution；`2+2+2=6` | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)，claim 与 support span 分账 |
| [Wired for Overconfidence `2604.01457v1`](https://arxiv.org/html/2604.01457v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 固定答案后 confidence 通道可干预，不代表事实答案已修复；`2+2+2=6` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，冻结答案与 confidence sensor 的边界 |
| [Reasoning Memory `2604.01348v1`](https://arxiv.org/pdf/2604.01348v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 当前 subquestion 作为 procedural retrieval key，而非整任务/整轨迹；`2+2+2=6` | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)，局部子问题检索与 prior-conditioned 采样 |
| [Train-to-Test `2604.01411v1`](https://arxiv.org/html/2604.01411v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 模型/数据规模选择依赖 repeated sampling 与正确候选识别合同；`2+2+2=6` | 深入完成 | 整合：`WORLDVIEW-SCALING-LAW` [Ch7](../../../../books/part-01-worldview/07-scaling-law.md)，采样/选择合同改变 N/D/k 生命周期预算 |
| [Reward Hacking Rebound `2604.01476v1`](https://arxiv.org/html/2604.01476v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 中间训练阶段 hacking 降低不保证后续不反弹；`2+2+2=6` | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)，暂退后反弹与有效正确 rollout 配额 |
| [Entity Cells `2604.01404v1`](https://arxiv.org/html/2604.01404v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 实体地址的稀疏性不等于事实计算只在单个 neuron；`2+1+2=5` | 标准完成 | 已有覆盖：`MODEL-FFN` [Ch16](../../../../books/part-02-model/16-feed-forward-mlp.md)，局部事实关联不等于独立事实槽 |
| [ACT-Mat `2604.01329v1`](https://arxiv.org/html/2604.01329v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 同初始化增量二阶统计可有条件代理输入统计以合并权重；`2+2+2=6` | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，同坐标权重合并的输入二阶矩代理 |
| [WILD `2604.01418v1`](https://arxiv.org/html/2604.01418v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 目标条件的多维预测方差与历史 token 代价联合选择评测 item；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，目标预测方差与历史 token 费用联合选题 |
| [AgentSocialBench `2604.01487v1`](https://arxiv.org/html/2604.01487v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 减少 full leak 的模板仍可能从沉默转为可推断的敏感主题提示；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，不提→局部泄漏的状态转移 |
| [go-mHC `2604.02309v1`](https://arxiv.org/html/2604.02309v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 双随机可行性与完整 mixer 表达空间分离；`2+1+2=5` | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) 的有限 block size 替代分支 |
| [The Expert Strikes Back `2604.02178v1`](https://arxiv.org/html/2604.02178v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | expert 写入幅度和稀疏可读性不等于领域路由标签；`2+1+2=5` | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) 的功能诊断与非因果解释边界 |
| [Improving Latent Generalization Using Test-time Compute `2604.01430v1`](https://arxiv.org/html/2604.01430v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 训练期知识 augmentation 与推理时参数知识访问是条件分支；`2+2+2=6` | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 的可读/取用/泛化区别 |
| [Runtime Burden Allocation `2604.01235v1`](https://arxiv.org/pdf/2604.01235v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | compact code 本地重建省序列化成本却可能损伤 backend 路由语义；`2+2+2=6` | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) 的 schema/执行交接 |
| [ClawSafety `2604.01438v1`](https://arxiv.org/html/2604.01438v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | operational peer、既有文件与任务一致语言仍可绕过拒答或检测；`2+2+2=6` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 source authority、真实 principal 与 effect receipt |
| [HieraVid `2604.01881v1`](https://arxiv.org/pdf/2604.01881v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 视觉 token 预算还需分配到删除阶段，不能只比较输入保留率；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 的固定预算/信息保留时间 |
| [Brief Is Better `2604.02155v1`](https://arxiv.org/pdf/2604.02155v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | reasoning 开头提议工具名与末尾约束合法名产生不同参数路径；`2+2+2=6` | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) 的选择顺序/合法性分账 |
| [Sven `2604.01279v1`](https://arxiv.org/pdf/2604.01279v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | 聚合梯度与逐样本残差 Jacobian 是不同更新坐标，显存/谱截断成为取舍；`2+1+2=5` | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 的优化器更新机制 |
| [Host-Guided GPU Race Detector `2604.02106v1`](https://arxiv.org/html/2604.02106v1) | 2026-04-03T08:00:00+08:00 ～ 2026-04-03T09:00:00+08:00 | host 的真实 launch 约束改变 kernel 静态 race 可行域；`2+2+2=6` | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的 model–kernel interface 关系约束 |
| [Anthropic RSP v3.1 / Apr02 Roadmap](https://www.anthropic.com/responsible-scaling-policy) | 2026-04-02 | aggregate capability progress阈值、internal feedback及自愿pause边界；`2+2+1=5` | 深入完成 | 仅报告：精确policy版本澄清和goal状态，无新增通用实施/测量机制；Books0 |
| [DRKL `2604.00223v1`](https://arxiv.org/html/2604.00223v1) | 2026-04-02 | reverse KL学生tail mass产生target-confidence耦合；`2+2+3=7` | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)；非作者Source/PRE/POST通过 |
| [Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization `2604.00260v1`](https://arxiv.org/html/2604.00260v1) | 2026-04-02 | block-prefix方差与同起点paired-map顺序项分责；`2+2+3=7` | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；非作者Source/PRE/POST通过 |
| [Fast and Accurate Probing of In-Training LLMs' Downstream Performances `2604.01025v1`](https://arxiv.org/html/2604.01025v1) | 2026-04-02 | 内部层success-rate sensor的checkpoint适用域/初始化摊销；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体差额深入，非作者Source/PRE/POST通过 |
| [Historical Newspaper OCR `2604.00725v1`](https://arxiv.org/html/2604.00725v1) | 2026-04-02 | 同训SSM/Transformer的paragraph质量、latency与absolute/growth memory分账；`2+1+2=5` | 标准完成 | 仅报告：有限architecture取舍，无新通用SSM机制或长期缺口，不以OCR标签排除 |
| [Two-Stage Optimizer-Aware Online Data Selection for Large Language Models `2604.00001v1`](https://arxiv.org/html/2604.00001v1) | 2026-04-02 | subset残差目标中raw Gram、target预条件与filter→非负weight分责；`2+2+2=6` | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)；非作者必要Source/PRE/实际POST通过 |
| [LinearARD: Linear-Memory Attention Distillation for RoPE Restoration `2604.00004v1`](https://arxiv.org/html/2604.00004v1) | 2026-04-02 | native/scaled RoPE关系恢复、dense目标linear workspace非linear time；`2+2+2=6` | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)；非作者必要Source/PRE/实际POST通过 |
| [Sequence-Aware Split Heuristic to Mitigate SM Underutilization in FlashAttention-3 Low-Head-Count Decoding `2604.00028v1`](https://arxiv.org/html/2604.00028v1) | 2026-04-02 | LQ=1低head decode的CTA供给/长度guard与metadata全费用；`2+1+2=5` | 深入完成 | 整合：`INFER-DECODE` [Ch44](../../../../books/part-05-inference-system/44-decode.md)；非作者必要Source/PRE/实际POST通过 |
| [Optimal Brain Decomposition for Accurate LLM Low-Rank Approximation `2604.00821v1`](https://arxiv.org/html/2604.00821v1) | 2026-04-02 | input/output双向whitening的local Fisher/KFAC surrogate与单侧反退；`2+1+2=5` | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；非作者必要Source/PRE/实际POST通过 |
| [Measuring the Representational Alignment of Neural Systems in Superposition `2604.00208v1`](https://arxiv.org/html/2604.00208v1) | 2026-04-02 | 相同features的编码/压缩几何可反转alignment排序；fixed-m资格；`3+1+3=7` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；非作者必要Source/PRE/实际POST通过 |
| [Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning `2604.00770v1`](https://arxiv.org/html/2604.00770v1) | 2026-04-02 | joint训练latent触发、无文字sensor与oracle-labeled probe权限分责；`3+2+2=7` | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；非作者必要Source/PRE/实际POST通过 |
| [Empirical Validation of the Classification-Verification Dichotomy for AI Safety Gates `2604.00072v1`](https://arxiv.org/html/2604.00072v1) | 2026-04-02 | parameter-ball需margin/有效L/domain；换中心重验及finite oracle反侧；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；非作者必要Source/PRE/实际POST通过 |
| [Think Twice Before You Write -- an Entropy-based Decoding Strategy to Enhance LLM Reasoning `2604.00018v1`](https://arxiv.org/html/2604.00018v1) | 2026-04-02 | 高entropy位置复用prefix分叉的同generation-budget局部选择；`2+1+2=5` | 深入完成 | 整合：`MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md)；必要Source/PRE/实际POST通过 |
| [Self-Routing: Parameter-Free Expert Routing from Hidden States `2604.00421v1`](https://arxiv.org/html/2604.00421v1) | 2026-04-02 | last-E hidden logits省projection但骨干仍学routing；`2+1+2=5` | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)；必要Source/PRE/实际POST通过 |
| [TRIMS: Trajectory-Ranked Instruction Masked Supervision for Diffusion Language Models `2604.00666v1`](https://arxiv.org/html/2604.00666v1) | 2026-04-02 | AR-NLL桶到corruption可见关系训练接口，非真实DLM轨迹；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；必要Source/PRE/实际POST通过 |
| [Generalizable Dense Reward for Long-Horizon Robotic Tasks `2604.00055v1`](https://arxiv.org/html/2604.00055v1) | 2026-04-02 | 虚高running-max峰与offline value初始化/后续reward分责；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；必要Source/PRE/实际POST通过 |
| [CircuitProbe: Predicting Reasoning Circuits in Transformers via Stability Zone Detection `2604.00716v1`](https://arxiv.org/html/2604.00716v1) | 2026-04-02 | 预测块与验证块索引/正文冲突，targeted和broad收益分账；`2+1+2=5` | 争议 | 暂缓：中心定位未恢复准确对应，不入Books；需作者索引约定/预测–验证表才重开 |
| [Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models `2604.00445v1`](https://arxiv.org/html/2604.00445v1) | 2026-04-02 | 严格AUC与any-real score的ties中心资格冲突；`2+1+2=5` | 争议 | 暂缓：constant score反例、不自修定理；需no-ties/half-ties精确勘误才重开，不入Books |
| [First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models `2604.00455v1`](https://arxiv.org/html/2604.00455v1) | 2026-04-02 | 全vocab初logit与当前plausibility支持的跨步接口、语法prior资格；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；Source/PRE/实际POST通过 |
| [Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling `2604.00489v1`](https://arxiv.org/html/2604.00489v1) | 2026-04-02 | 冻结旧块/新depth适配、恢复路径不等full-input保真；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；Source/PRE/实际POST通过 |
| [Q-Mask: Query-driven Causal Masks for Text Anchoring in OCR-Oriented Vision-Language Models `2604.00161v1`](https://arxiv.org/html/2604.00161v1) | 2026-04-02 | image/query-only辅助mask可用时点、非decoder显式mask输入；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；Source/PRE/实际POST通过 |
| [The Geometry of Compromise: Unlocking Generative Capabilities via Controllable Modality Alignment `2604.00279v1`](https://arxiv.org/html/2604.00279v1) | 2026-04-02 | centroid与centered-pair分责，平移只改前者而quality仍反退；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；单段Source/PRE/实际POST通过 |
| [Do LLMs Know What Is Private Internally? Probing and Steering Contextual Privacy Norms in Large Language Model Representations `2604.00209v1`](https://arxiv.org/html/2604.00209v1) | 2026-04-02 | 单轴/合轴隐私steering、concept可读不等行为或授权；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；Source/PRE/实际POST通过 |
| [Do Language Models Know When They'll Refuse? Probing Introspective Awareness of Safety Boundaries `2604.00228v1`](https://arxiv.org/html/2604.00228v1) | 2026-04-02 | 预测/真实fresh-context行为与strict/lenient response标签分责；`2+1+2=5` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Source/PRE/实际POST通过 |
| [FGR-ColBERT: Identifying Fine-Grained Relevance Tokens During Retrieval `2604.00242v1`](https://arxiv.org/html/2604.00242v1) | 2026-04-02 | document-to-query span读出与原ranking、positive-only和index/inline费用分责；`2+1+2=5` | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)；Source/PRE/实际POST通过 |
| [Breaking Data Symmetry is Needed For Generalization in Feature Learning Kernels `2604.00316v1`](https://arxiv.org/html/2604.00316v1) | 2026-04-02 | 特定kernel初态/训练partition symmetry卡held-out fixedpoints；`2+1+2=5` | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch05](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；单段Source/PRE/实际POST通过 |
| [LLM REgression with a Latent Iterative State Head `2604.01206v1`](https://arxiv.org/html/2604.01206v1) | 2026-04-02 | 冻结decoder的single-query scalar head与next-token/targetscale分责；`2+1+2=5` | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md)；单段Source/PRE/实际POST通过 |
| [Omni-MMSI: Toward Identity-attributed Social Interaction Understanding `2604.00267v1`](https://arxiv.org/html/2604.00267v1) | 2026-04-02 | raw identity attribution与oraclecue/reference enrollment人口分责；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；单段Source/PRE/实际POST通过 |
| [Benchmarking Interaction, Beyond Policy: a Reproducible Benchmark for Collaborative Instance Object Navigation `2604.00265v1`](https://arxiv.org/html/2604.00265v1) | 2026-04-02 | 同trajectory decision SR/finish FR与oracle/nav stage分账；`2+2+2=6` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；单段Source/PRE/实际POST通过 |
| [Dynin-Omni: Omnimodal Unified Large Diffusion Language Model `2604.00007v1`](https://arxiv.org/html/2604.00007v1) | 2026-04-02 | expanded-vocab旧/新embedding/head行与同形参数merge来源分责；`2+2+2=6` | 深入完成 | 整合：`MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md)；单段Source/PRE/实际POST通过 |
| [Disentangling to Re-couple: Resolving the Similarity-Controllability Paradox in Subject-Driven Text-to-Image Generation `2604.00849v1`](https://arxiv.org/html/2604.00849v1) | 2026-04-02 | entity-grounder/pronoun-edit条件分路与identity/adherence取舍；`2+1+2=5` | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；单段Source/PRE/实际POST通过 |
| [Multi-Camera View Scaling for Data-Efficient Robot Imitation Learning `2604.00557v1`](https://arxiv.org/html/2604.00557v1) | 2026-04-02 | trajectory×views分母、camera动作增量校准与部署view匹配；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；单段Source/PRE/实际POST通过 |
| [OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models `2604.00688v1`](https://arxiv.org/html/2604.00688v1) | 2026-04-02 | 全codebook entry mask/loss与推理揭示/初始化适配分责；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；单段Source/PRE/实际POST通过 |
| [Spectral Compact Training: Pre-Training Large Language Models via Permanent Truncated SVD and Stiefel QR Retraction `2604.00733v1`](https://arxiv.org/html/2604.00733v1) | 2026-04-02 | permanent rank参数化与dense容量、shape可运行与真实quality分账；`2+1+2=5` | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)；单段Source/PRE/实际POST通过 |
| [EgoSim: Egocentric World Simulator for Embodied Interaction Generation `2604.01001v1`](https://arxiv.org/html/2604.01001v1) | 2026-04-02 | generated-frame对象几何更新与下一render模拟状态接口；`2+2+2=6` | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；单段Source/PRE/实际POST通过 |

## 4. 证据与知识整合

以下逐项写明 exact-v1 的已核证据及采用边界；完整机制笔记与具体排除依据见[审阅记录](../_sources/daily-20260403/V3_REVIEW.md)。旧评分/泛化 `No Change` 不继承；旧 `2604.01951` 曾使用后发 v2 摘要，本次按当窗 v1 未新增超越训练版本/原子回退原则的命题，作具体前分母关闭。最后十项原始证据及独立 Books 裁决已同步；MiCP 的阈值争议保持明确隔离，不把定义未明的形式保证写入 Books。

### [RAE-AR `2604.01545v1`](https://arxiv.org/html/2604.01545v1)

作者表 2/4/6 证明的是其图像设置中表示重构质量不能保证连续 AR 可生成性：高维 latent 的 token 分布方差和 teacher-forcing 到自生成时的误差滚动是两个独立压力。训练期 Gaussian 扰动使模型见到非完美历史 token，代价是改变训练目标；归一化单独使用在表 4 的两个 encoder 反而变差。组合结果缩小与 VAE 的差距，却没有普遍匹配 VAE。主任务已将此约束与旧 VAE 适用边界整合至 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；不能把图像作者实验外推文本、并发或 SLO。

### [Diffusion instruction unlearning `2604.01514v1`](https://arxiv.org/html/2604.01514v1)

作者 §2–4 在所测 SD/CLIP 图像管线中观察到“忘记 X”提示不能持续抑制 X：CLIP text embedding 与 denoising cross-attention 仍保留目标概念信号。测试只有 10 个目标概念，机制证据不覆盖所有 diffusion 架构或真正参数级 unlearning。`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 已要求按参数、retrieval、prompt/context、memory 等 substrate 和 observer 分别检验遗忘，明确单次 final refusal 仅为局部 suppression verdict；该论文将既有原理具体落在 CLIP/cross-attention 的图像管线上，但不改变原有系统验收机制或新建独立安全 owner，故 `已有覆盖`。

### [Expert-choice diffusion MoE `2604.01622v1`](https://arxiv.org/html/2604.01622v1)

作者 §2–5 与附录 C 将专家容量所有权从“token 各自选 expert 后再平衡”转为“expert 按容量选 token”，并随去噪 mask ratio 调整容量；收益是可控专家负载，代价是选择/重排和 routed-token 覆盖不均。论文正文称 no tokens dropped，但附录 C 显示平均仍有约 2.7%/8.0% token 没被 routed expert 选中，只是 shared experts 仍处理所有 token。主任务已在 `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) 写入这种阶段性容量分支及兜底边界；所测 PPL/吞吐不能升格为任意硬件的性能保证。

### [DWDP `2604.01621v1`](https://arxiv.org/pdf/2604.01621v1)

以 v1 PDF 为准（同一 v1 HTML 页眉日期错误）。作者在 GB200 NVL72/DeepSeek-R1、MoE NVFP4、KV FP8、8K 输入/1K 输出、20～100 TPS/user 的合同下报告同等每用户 TPS 的 output TPS/GPU 高于对照 8.8%。机制是复制 attention 权重、分片 MoE 权重，使用 peer `cudaMemcpyAsync` 和双缓冲预取替代每层全局 expert all-to-all barrier；本地执行前仍需等权重，copy/compute 会争资源。主任务已把这个条件性替代分支整合至 `INFER-DYNAMO` [Ch52](../../../../books/part-05-inference-system/52-dynamo.md)，保留旧 EP 在带宽或隐藏窗口不足时的成立条件；不推断跨节点或生产尾延迟收益。

### [VideoZeroBench `2604.01569v1`](https://arxiv.org/html/2604.01569v1)

论文将视频 QA 从“答对”逐级拆成时间证据、bbox 证据等对象，说明最终答案不能单独证明视觉依据正确。但 138 个视频、500 题和不同模型的视频输入预算并非统一条件；高阶任务还提供关键时间戳，不能把排名当通用端到端定位能力。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求视频模态/时间消融，并区分答案与证据路径；分级 scorer 是现有原则的受限实现案例，独立复核后 `已有覆盖`。

### [Discrete Gaussian diffusion `2604.02028v1`](https://arxiv.org/html/2604.02028v1)

作者 §3–5 与附录显示连续 Gaussian 去噪用于离散样本时，某些 late-stage 多峰区间会把中间态落在低密度模态间，随后 denoiser 面对分布外状态。q-sampling 可救部分文本正确性却不严格复现 reverse process，并牺牲多样性；self-conditioning 降条件失配却增加训练成本。该论文的 toy/文本结果有连续图像反例，不能写成所有 Diffusion 的失败定理。主任务已在 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 增补受限 failure mode、solver trade-off 和旧 DDPM/替代离散范式的共存边界。

### [PGPO `2604.01840v1`](https://arxiv.org/html/2604.01840v1)

作者用同前缀下视觉 token 可见/被 mask 的预测分布 KL 作 token 视觉依赖代理，再在保留总 advantage 规模下重分配权重。这改变 credit 的分布，不改变 verifier 的最终奖励来源；KL 敏感并不证明答案正确性的因果归功。Qwen2.5-VL 3B/7B、ViRL39K、两轮训练/H100 对照的强基线收益仅约 0.65/0.62 个 avg@8 点，另有前向成本。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已讨论 sequence→token eligibility、代理非因果与总尺度/回退；本项是受限视觉实现，独立复核后 `已有覆盖`。

### [Data Laundering `2604.01904v1`](https://arxiv.org/html/2604.01904v1)

以原始文本的低 loss/高 confidence 作为训练数据成员证据，在训练集确实保存原文字节、负例又匹配文体和来源时，是低成本审计。作者改为仅在改写后的 surrogate 上训练模型，发现向目标模型查询**原文**会失去部分 membership 信号；因此“原文探针阴性”不能推成“语义内容未用于训练”。其 SDR 方法以 23 种语域为有限搜索空间，由辅助模型合成训练样式查询，再复用既有 detector：所测 Pythia-6.9B/Wikipedia 上，inside-register 的 Loss AUC 从 63.7% 到 76.6%，outside-register 从 62.7% 到 75.5%；Falcon-7B、Llama-2-7B 也有受限增益。但恢复后的 AUC 远非确定性血缘证明，攻击者需 reference set、目标 score 接口和额外查询/合成预算；真实未知变换可能不在语域集合，反复选最优查询还会增加选择偏差。`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 已在 membership identifiability 段补入变换家族和未检出不等于未训练的边界，保留简单 MIA、签名来源记录与独立合规审计的各自权限。

### [World Action Verifier `2604.01985v1`](https://arxiv.org/pdf/2604.01985v1)

官方 v1 PDF §2～4、§6 与附录 C 的条件分支是：行动数据稀缺时，先用无动作视频预测可达的未来 subgoal，从 action-relevant 状态片段用 inverse model 提议动作，再由 forward world model 回推下一状态；模型间分歧帮助选择下一次真实环境交互。它改变的是**去哪里采集下一条行动证据**，不是让三个模型互相一致就成为物理真值；实际 transition 仍由环境返回后才进入训练。作者在 MiniGrid、RoboMimic、ManiSkill 共九个仿真任务报告受限的约两倍数据效率和约 18% policy reward 提升，但没有真实机器人安全或开放世界外推。逆动作可能多解，视频状态分布也可能不支持新场景，三次模型推理提高探索成本；这些条件不成立时，直接环境探索或保守数据采集更可靠。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 原已有 inverse dynamics 对事实 transition 的辅助解释，现已补入“预测仅提议采样、环境才提交真值”的探索数据 admission 分支，并由主任务对 exact-v1 PDF 独立复核通过。v1 HTML 的 08-24 页眉与事件日期不一致，此处机制和实验以官方 PDF v1 为准。

### [Goose `2604.02047v1`](https://arxiv.org/html/2604.02047v1)

不同 draft 来源的接受率不等时，固定 target verification 节点预算不应一律均匀分支：高置信 n-gram 延伸深 spine，较低置信的前次 target bigram 形成宽 fallback，target 仍拥有最终 token 提交。作者的独立接受近似证明针对期望接受长度，不是 wall-clock 普遍定理；实验为 5 模型/5 任务、greedy、batch=1，60 节点树形比较。主任务已在 `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 写入异质 proposal 质量对深宽预算的条件性分支；采样、并发和 SLO 尚未证明。

### [Anthropic emotion concepts](https://www.anthropic.com/research/emotion-concepts-function)

官方 Research 索引的 `publishedOn=2026-04-02T10:56:00Z` 确认本窗事件。文章报告在早期未发布 Sonnet 4.5 snapshot 中可解码 171 个 emotion-word 相关 activation direction，并在所测虚构黑邮件及代码任务上通过 steering 改变行为；部分作弊没有明显外显情绪文本。它不证明主观感受、发布版常见该行为、或可以用单一向量设生产 safety 阈值。后续 arXiv 文章不能倒灌为本日已公开正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已区分可解码、干预、部署证据，`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 限制白盒 probe 的安全权限；独立对照后 `已有覆盖`。

### [Causal Scene Narration `2604.01723v1`](https://arxiv.org/html/2604.01723v1)

作者在 LMDrive/CARLA 的 16 routes、8 towns、5 次重复中拆开两件事：把驾驶意图与环境约束联接的文本结构，只解释原始模型所测 Driving Score 改善的 39.1%，其余来自信息内容；语义 monitor 与文本增强也不是简单可加。表 3 中偏好训练模型的 CSN 单独为 40.45，叠加 safety layer 为 35.74；另一次逐帧日志的 96 route-check 中方向冲突与卡住检测都没有触发，说明“零显式告警”不能等同“安全层未改变控制”，因为逐帧 steering/throttle clamp 仍在执行。作者没有单独移除 clamp 的因果消融，故该降效的归因只是与日志相容的解释，而不是被证明的普遍定理。主任务已在 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的 Simplex 论证中将 proposal、常态限幅、实际 command 与触发式 monitor 分账，保留旧 monitor 的成立条件与保守回退；仿真驾驶结果不证明真实道路安全。

### [ProCeedRL `2604.02006v1`](https://arxiv.org/html/2604.02006v1)

论文 §3～4 将失败步骤的影响从“当前 action 错了”扩展到“环境回传的 observation 也变得误导，导致后续探索继续偏离”；过程 critic 为低分步骤选择性 rewind/refine，再把轨迹用于 DAPO 训练。其 Qwen3-1.7B/8B 深搜与 ALFWorld 对照显示受限的探索收益，但一条 ProCeed 轨迹约消耗 1.8～2.5 条 vanilla samples 的生成量；1.7B 在 ALFWorld OOD 的 23.33% 还略低 DAPO 的 24.12%，过多 rewind 也会反降效。局部动作的“改善”由同一 critic 复评，不是独立真值；深搜答案又由 LLM judge 判定。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已写失败 suffix 局部 correction、干预来源必须随 trajectory 保存、teacher 不可靠或成本过高时回退纯 learner rollout。这篇将 feedback contamination 具体化，但未证明需改变该训练状态所有权、回退或 verifier contract，故独立对照后 `已有覆盖`；不能把过程 critic 提升为环境真值。

### [ProdCodeBench `2604.01527v1`](https://arxiv.org/pdf/2604.01527v1)

作者 §2～4 的生产编码 Agent 评测从真实单轮开发者会话保留 verbatim prompt、已合入 diff 与测试；旧 monorepo commit 的索引、工具包和依赖可能过期，不能持续重放。其有条件替代是在当前 head 撤销已合入 diff，形成滚动任务，再按原/新状态测试并多次执行剔除不稳定测试。这获得更新鲜、可运行的近部署任务，却**改变了历史环境与代码上下文**，不证明原任务被精确复现；私有数据不可公开复算。只有约 75% 任务有 fail-to-pass tests，作者公布的模型 solve-rate 实验也仅对这一子集运行；其余 pass-to-pass 样本不能用相同成功定义。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原已要求 buggy/candidate/gold 与环境版本重放；主任务独立核 v1 后在相邻段实际写入“历史时间旅行失效→rolling evaluation”分支，并明确不可继承历史环境等价。模型排名受私有任务、筛样与 harness 影响，不外推一般 coding 能力。

### [No Attacker Needed `2604.01350v1`](https://arxiv.org/html/2604.01350v1)

共享 Agent 状态不只受恶意注入威胁：用户 A 的语义、取整或工具步骤在自己的任务中完全有效，进入共享 memory/对话后却可能被用户 B 当成默认规则。作者在 EHRAgent 与 MURMUR 中比较相同 victim task 的干净/写入后状态；raw-state 污染率在三个受控数据集为 57.4%～70.7%，但 victim task 预先筛成干净状态可成功，不能外推真实生产发生率。Write-time 文本清洗在 Slack 对话状态有效，却在 EHRAgent 的 solution code 中留下程序惯例；因此保存 `source principal / task scope / artifact type` 和读时作用域检查，比“文本看着无害”更关键。主任务已在 `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 原有 scope 段后吸收这一条件性失效，`PLATFORM-MULTI-TENANT` [Ch71](../../../../books/part-06-ai-infrastructure/71-multi-tenant.md) 仍拥有物理租户隔离；更严格的 scope 降低错误复用，也会损失有益共享并增加审计成本。

### [ES vs GRPO `2604.01499v1`](https://arxiv.org/html/2604.01499v1)

作者用参数扰动的 Evolution Strategies 和 token policy gradient 的 GRPO 对照，发现四个单任务达到相近准确率时，参数更新方向与 off-task 保持仍可明显不同：顺序训练里 ES300 iteration 遗忘比 ES100 显著，MMLU 最后相对 base 为 ES -3.7、GRPO +0.8 点，但 IFEval 的方向反过来。这说明目标任务准确率不充分，不能把 ES 或 GRPO 一方写成普遍更安全；预算、任务顺序、held-out 集都影响结论。`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 已要求在 matched budget 下同时验收 optimizer/update geometry、loss trajectory 与 held-out quality；`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已要求独立 held-out gate。此论文给这些既有原则一个有限对照，未改变 checkpoint 的长期接受条件，故 `已有覆盖`。

### [Normalization–Optimizer Coupling `2604.01563v1`](https://arxiv.org/html/2604.01563v1)

单独调优 normalizer 或 optimizer，不能保证两者配对后仍正常。作者在 1B LlamaForCausalLM、FineWeb-Edu、1000 step、单 H200 的 3×2 因子实验中看到默认 Derf+Muon 的静默 loss 差距：相比 RMSNorm 的 gap 在 AdamW 下 +0.31 nat、Muon 下 +0.97；层 15 的 erf 饱和达 83%。减小 Derf `alpha` 或用 EMA scale blend 能在所测短程回收约 80%/84% 差距，但未证明长训或更大模型也有效。主任务已在 `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 原有 optimizer×数据组合论证后，补入 optimizer×normalizer 的联合配对实验、饱和诊断和旧组合回退；这一额外实验预算换取的是避免无 NaN 的缓慢退化，不是普遍推荐某个优化器或归一化层。

### [Read More, Think More `2604.01535v1`](https://arxiv.org/html/2604.01535v1)

早期 Web Agent 用更短的 accessibility tree 替代完整 HTML，是在上下文长度、推理预算有限时的合理选择；但细节裁掉后，较强模型也失去 layout/CSS 等 grounding 线索。作者在 WorkArena L1 的 330 个任务、15 步上保持 id-based action API，对比 HTML 与 a11y：所测 GPT-5.1 high 为 73.3% vs 55.8%、Sonnet 4.6 为 67.0% vs 52.4%；gpt-oss-120b high 则反向为 38.8% vs 46.7%。其 Playwright 错误归类支持 grounding 差异，但闭源/开源只是能力的代理，HTML token 也远高于 a11y（GPT-5.1 例 56,653 vs 6,720），没有 matched cost/latency 或多网站外推。历史观察的实验只固定 a11y：9 步完整历史约 39,011 token，字符 diff 约 13,670，某些模型相近但并非全部；不能与 HTML 组合结果互推。主任务已在 `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) 的 pixel→program-state observation 段后吸收模型/预算条件下的表示取舍和 a11y 差分历史；`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) 仍拥有更一般的历史压缩策略。新增只是条件性分支，不把 HTML 写成普遍更优。

### [Tex3D `2604.01618v1`](https://arxiv.org/pdf/2604.01618v1)

固定相机中的 2D patch 可以低成本测试 VLA 的视觉脆弱性，但机器人抓取的物体会在一条轨迹中跨视角反复出现；攻击物体表面因此不同于单帧噪声。作者用 MuJoCo 背景与可微物体渲染器对齐，让任务失败目标反传到 3D 纹理，再对轨迹关键帧和 vertex 做加权/平滑。在 LIBERO 的 OpenVLA、OpenVLA-OFT、π0、π0.5 与四个任务 suite 上，每任务 50 次试验、通常单 A100 80GB；最高 96.7% 失败仅是 OpenVLA Spatial targeted 条件。实机为 Franka Panda、单 RGB、特定 3D 打印物体和 pick-and-place，作者称各任务 100 次试验，Fig.4 所测位置偏移下 3D 纹理约 66.8–67.6% 失败、2D patch 为 40.8–50.8%；不能把这些数值外推到其他物体、传感器、机器人或安全控制器。`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已在感知/攻击预算段吸收物体外观与场景版本、相机轨迹、动作 trace 的联合验收分支，并明确独立 controller 才有提交权；这是系统设计推断，不是论文已验证的防御。固定视角、有限预算下的旧 patch 测试仍可作为基线。

### [Oscar `2604.01624v1`](https://arxiv.org/html/2604.01624v1)

Masked diffusion 的中间 token 尚可重写，但单条去噪路径若较早锁定错误，后续上下文可能逐渐与错误一致。作者在 LLaDA-8B/Dream-7B 上并行运行不同 reveal order 的去噪链，以相同位置的跨链 entropy 提议待核 span，再以 2021 Wikipedia/Contriever top-1 检索证据条件化局部 remask。这不是模型“知道真相”：多条链可一致地错误，CommonsenseQA 的近零分歧也导致无干预。LLaDA 的表1 原始 exact-match 标签 AUROC 为 76.4，低于训练式 DynHD 84.2；作者用 LLM-as-Judge 重标后才报 86.5，不能跨 evaluator 宣称普遍超越。完整定位+定向修复 F1 69.0、未引导 62.9，随机 span 修复 62.8，显示传感器和修正需要共同作用；8 条链在 4×H200 上约 1.3× wall-clock、1.67× 峰值显存，未证明并发或生产 SLO。主任务已在 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 的生成/提交主线局部整合这条条件性 commit-gate 分支，并保留外部证据、拒答与旧 confidence schedule 的共存边界。

### [ContextBudget `2604.01664v1`](https://arxiv.org/html/2604.01664v1)

固定周期摘要在短且均匀的 observation 流中简单，但一条大工具结果若先入窗再处理，可能已越过 context 上限；若盲目提前压缩，又会删掉本可保留的历史。作者在新 observation 的正文载入前读取其长度与当前 headroom，让 policy 选择 Null、Partial 或 Full commit-block aggregation，再载入正文，并用渐紧预算的多轮训练学习何时压缩。表2 的消融显示仅给预算信号或仅有压缩动作均不如二者组合；证据只来自 Qwen2.5-7B/Qwen3-30B 的组合问答与长程搜索、4–16k/8k 的披露预算，BrowseComp 用 LLM judge，部分对照重实现，不能当作生产延迟保证。粗粒度块聚合可能丢失精确证据，原文也未证明不可变 archive，因此 Context runtime 仍须保留原文回读、policy pinning 与 commit authority。主任务已在 `AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) 原压缩损失段加入“先算待载入长度和余量，再决定聚合”的条件性顺序；固定余量、拒绝过长输入或外置原文在更简单/高风险条件下仍合理。

### [FlatAttention `2604.02110v1`](https://arxiv.org/html/2604.02110v1)

作者 §III–V 让 tile-based accelerator 在多个 tile 之间协作完成 Attention：NoC fabric multicast Q/K/V 分块、执行 row-max/sum reduction，以片上通信换较少 HBM 往返。单 tile 的 FlashAttention 不需跨 tile 协调，在较短序列或片上网络不支持低成本 collective 时仍合理；tile group 扩大则会压小每 tile 的矩阵工作，短序列下可能降低利用率。所报 4.1×/1.9× 属所建 tile/wafer-scale 模拟配置及跨硬件 GH200 对照，GVSoC/RTL 校准不等于真实商品芯片或生产尾延迟实测。`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 原有 IO-aware Attention 与 kernel 执行分工，主任务已在相邻段落补入 tile SRAM、NoC collective、HBM IO、per-tile occupancy 的联合选择条件；若 fabric 或 shape 不满足，回退独立 tile/原 GPU 路径。

### [Learning from the Right Rollouts `2604.01597v1`](https://arxiv.org/html/2604.01597v1)

作者在 PPO rollout 入训前，以偏好 CoT 的 validation SFT gradient 作参考方向，再逐 episode 计算 PPO-loss gradient 对齐；负内积样本剔除，正内积样本按平均分归一化加权。这使“采样到的每条轨迹都有益”不再是默认假设，但额外反向计算有成本，且偏好 CoT 与任务真值不等价。最重要的证据边界是：该 validation set 一旦参与筛选，就是训练控制信号，不能再作为独立 held-out 验收。作者在五种 1–8B 模型和数学、物理、常识五数据集报告改善，未证明跨任务 reference、生产吞吐或不泄漏评价的普遍性。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已将 trajectory admission、筛选/权重策略与独立 held-out gate 分账；该方法是受限实现，不改变训练状态 owner 或 release 判断，故 `已有覆盖`。

### [Batched Contextual Reinforcement `2604.02322v1`](https://arxiv.org/html/2604.02322v1)

官方 v1 §3–4 将三道数学题放入一次 completion，共享训练生成上限；每题答案经 parser 与等价性验证，reward 以各题正确率为主、另有格式项，**没有显式长度惩罚**。前题冗长会挤占后题，因此 token 机会成本来自可验证任务之间的资源竞争，而不是单题 token 税；作者在单题测试仍观察到压缩。这一训练分支是 Ch33 原 hard cap/线性惩罚/prior-dependent cost 主线未覆盖的预算分配机制，主任务已在 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) Reasoning Cost 段吸收。实验只覆盖 1.5B/4B 数学模型、作者的 4×RTX PRO 6000 BF16 单机训练；1.5B 的 AIME25 与 MATH-500 准确率低于对照，不能写“压缩总是免费”，两组显式惩罚坍塌也不证明所有软惩罚无效。题序、难度配比、答案解析、前题挤占后题和过紧预算是新增 failure mode；单题 hard cap 仍适合独立请求与严格 SLO。

### [Skill0 `2604.02268v1`](https://arxiv.org/html/2604.02268v1)

官方 v1 §3–5 先用同任务有/无 Skill 的 paired validation 过滤无帮助的 Skill，再按 `M=[6,3,0]` 或 `[5,3,0]` 逐阶段减少训练期外部 Skill，最终在无 Skill 条件下测策略。作者在 ALFWorld/Search-QA 的 3B/7B 模型观察到收益，但初始 SkillBank 的质量、任务分区、视觉编码以及域迁移尚不能由这些实验分离；推理 token 降低也不证明 Skill 内容已安全、可撤销地内化。`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) 已要求 paired marginal utility 与 artifact admission，`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已写外部 Skill/scaffold 退火与 no-skill evaluation，甚至将 Skill0 标为受限证据。本项不改变现有 owner 或 Gate，独立对读后 `已有覆盖`。

### [SRPO `2604.02288v1`](https://arxiv.org/html/2604.02288v1)

官方 v1 §2–4 将正确/错误 rollout 分流：错误且有成功 sibling 或环境反馈时，用 feedback-conditioned self-teacher 提供 dense logit proposal；正确或无反馈时回到 outcome-driven GRPO。teacher entropy 降低某些 token 的权重，但不是正确性的证据。Qwen3-4B/8B、四类科学 QA 与 ToolAlpaca 单调用的作者实验只支持这条受限 recipe，不证明长程 Agent 或集群吞吐。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已分账 correct/incorrect admission、verifier 的 reward 方向与 teacher 的 proposal 权限，并有额外 forward/偏差回退，所以独立对读后 `已有覆盖`。

### [A Simple Baseline for Streaming Video Understanding `2604.02317v1`](https://arxiv.org/html/2604.02317v1)

官方 v1 §3～5 在 causal visible prefix 内以最近若干帧作为简洁、可复现的在线流视频基线，再与需要维护历史状态的方案对照。作者对 Qwen2.5-VL-7B、Qwen3-VL-8B、1 fps 与 2/4/8 帧设置，在 OVO-Bench、StreamingBench 发现：历史检索可改善部分过去事件回忆，却可能牺牲实时感知；所谓 backward track 还混有识别虚假提示的 HLD，不能直接算作 episodic recall。跨论文排行榜的 backbone、输入预算和时间协议并未全部匹配，因此不能把分数差全归因于 memory 架构，也不能否定真正长程回忆任务对历史状态的需要。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已据此在视频 EvalSpec 主线增设 recency baseline 与实时感知、历史回忆、抗误导三类分账；这是评估控制条件，不是宣称最近帧架构总是最好。

### [Steerable Visual Representations `2604.02327v1`](https://arxiv.org/html/2604.02327v1)

官方 v1 §3～4 在冻结 ViT 的中间层插入零初始化门控 cross-attention，使文本提示影响视觉 patch 表示形成，而不是仅在最终固定特征后融合。DINOv2 ViT-B/14 + RoBERTa-Large、336×336、作者定位任务的表 3 中，早/晚融合 CORE 为 96.0/93.3、PODS 为 58.1/36.6，但通用细粒度分类 probe 为 87.7/91.8；前两项提升不能抹去后一项代价。消融中的 late-fusion 分支同样达到高 CORE，不应被描述成完全不可控；PODS 的收益在粗类提示对照中基本消失。额外 adapter、训练及 prompt-dependent 视觉特征使缓存身份和下游复用更复杂。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 已在 fusion point 主线窄幅吸收此条件分支及晚融合旧路径的适用条件；不从所测骨干和数据外推为任何任务的普遍架构排名。

### [Reliable Control-Point Selection `2604.02113v1`](https://arxiv.org/html/2604.02113v1)

官方 v1 §3～4 先用表面关键词在 CoT 识别反思/转换边界，但在同一前缀重新生成十次时，541 个初始边界中 93.3% 不满足作者的稳定阈值 0.8；一次文本命中不足以确认可复现的行为控制点。过滤高稳定边界后再做内容子空间投影，并用等数量随机边界作对照，是构造 steering vector 前的证据纪律；它仍需真正 intervention 和任务回归，不能让稳定 probe 自行获得行为控制权。作者仅从 100 道 MATH 训练题提取向量，在三款同架构 1.5B 模型、MATH-500、greedy 4096-token 设置下验证；重复采样成本、阈值选择偏差和高筛除率留下样本方差，也没有证明跨架构/开放场景可用。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已在原 failure direction 边界下补控制点稳定性与数量匹配对照，作为受限 evaluation 条件，而非通用纠错算法。

### [Reasoning Patterns in Long-CoT SFT `2604.01702v1`](https://arxiv.org/html/2604.01702v1)

官方 v1 §3～5 与附录 B～D 在约 500K 道相同数学题上，用两种 teacher 的已验证正确 CoT 对四种学生基座做 SFT。DeepSeek-R1-0528 来源使训练 loss 较低，却在所测五个数学集的泛化低于 gpt-oss-120b 来源；token-loss 分解表明近零损失 token 比例差异大，而关键转换 token 的损失更接近。DeepSeek-V3.2 自动行为标注、随机删步重训与按分叉 proxy 过滤，支持“部分冗余探索被学生继承”的解释，但不能把标注当作推理结构真值；过滤 top 10% 在 Qwen2.5-7B、96K 测试中五基准均值 54.9→57.9，32K 复测增益较小。只涉及两个 teacher、数学任务和作者筛选预算，不证明分叉总是坏、过滤在代码/Agent 中也有效。`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) 已在数据质量主线补“答案正确≠推导模式值得模仿”、易预测 token 与关键步骤分账，以及过滤可能误删必要探索的 trade-off。

### [ActionParty `2604.02330v1`](https://arxiv.org/pdf/2604.02330v1)

现有多主体视频模型若为每个 actor 单独生成视流，action 与主体天然关联；当所有主体同处一帧时，文本指令和像素本身不保证动作落到正确主体。作者在视频 DiT 中把每个主体的持续状态 token 与视频 latent 联合去噪，用 cross-attention mask 只让主体读取自身动作，用前时刻二维位置的 RoPE 偏置将状态 token 对准画面，再让共同视频 token 消费全部主体状态渲染下一帧。官方 v1 §3～4 的 Melting Pot 46 个二维游戏、最多 7 人主评中，Movement Accuracy 为 0.779，文本动作基线 0.158；但这个差异混合了状态表示、遮蔽和训练设置，不可全归因一个组件。只在 2.5K 条两人 Coins、256×256、45K 步小消融里，完整方案 MA 0.872，去 cross-mask 降至 0.052、去空间 RoPE 降至 0.032，支持绑定机制有作用。附录披露 20 步滚动时坐标漂移、主体有时消失、未训练的 8 人条件出现跨游戏 Interact 泄漏；系统并非实时，未证明三维、遮挡、真实机器人或安全控制。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 已在独立主体视流与 hub 通信路线前，加入共享观察下的持续主体身份、动作绑定与共同渲染这一条件分支；两种 observation 拓扑与代价不同，非线性替代关系。

### [BidirLM `2604.02045v1`](https://arxiv.org/html/2604.02045v1)

将现有 causal decoder 复用为理解/检索 encoder 可节省重训成本，但“放开双向注意力”不等于表示几何已适合全句比较。作者在 Gemma3-270M 与 Qwen3-0.6B 先比较只改 attention、masked-next-token prediction（MNTP）与对比学习：只改 attention 对检索/标注任务有混合收益并损害 XNLI/Seahorse；先做 MNTP 10B token、再以约 3M 样本对比训练使 full-param 与 zero-shot 指标在所测任务更协调。将英语 MNTP 延长到 30B token 出现阿语、数学或代码遗忘，作者以原 base checkpoint 的线性合并和少量多域数据缓解；与视觉/语音 causal specialist 的权重及 head 合成还要逐模态检查，不能把其 0.5 比例经验固定成通用配方。论文只核所列小型 backbone、MTEB/MIEB/MAEB 等离线表示任务，未证明大模型可无损转双向、生产检索 SLO 或多模态生成能力保持。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 已在 staged/native 表示交接写入 attention、目标、下游用途必须同验及遗忘回归边界；`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 继续拥有具体训练 objective/数据配比。两条路线按用途共存。

### [Beyond the Assistant Turn `2604.02315v1`](https://arxiv.org/html/2604.02315v1)

只评 assistant 当轮答案不能说明模型是否会根据这轮输出预测有意义的用户后续。作者在系统、用户、assistant 之后追加 user-role header，让同一模型生成下一轮用户输入，并用 judge 判断是否为依赖当前对话的真实跟进；11 个开源权重模型、五个答题/指令任务和两个 held-out 英文会话集显示该指标与当轮准确率不单调。以截断 assistant 末尾、追加明确问句两类扰动检验传感器：部分模型的跟进率明显变化，也有 Qwen3.5-27B 等几乎不变。温度从 0 升高使某些 family 的跟进率上升，说明 greedy 解码只能探测分布的一个点；不能把“会生成合理跟进”推成真实用户将如此响应、模型理解了用户意图或部署交互成功。gpt-5.4-mini judge 与盲法人工标注的 κ=0.726 仍不消除定义与域迁移问题，最高条件下真实跟进仍为少数；自博弈、best-of-N 的实用价值作者未验。官方 v2 在 2026-04-03T09:55+08:00 才提交，本日报只用 v1。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求后续 user turn 由当前 response 条件化，并把 user policy、judge、停止条件和多轮演进纳入 evaluation identity；本论文提供受限诊断 probe，但未改变既有评价权责或 release Gate，故不重复写正文。

### [From Guessing to Placeholding `2604.01849v1`](https://arxiv.org/html/2604.01849v1)

完整补全在高熵位置容易猜错细节；作者让模型输出代码骨架和显式 placeholder，使 IDE 用户填入未决片段。官方 v1 §3 的期望成本阈值成立于“填空比修正错误预测便宜”的假设，不能由 entropy 高直接推出真实用户收益。3M IDE 交互中的约 61% 被编辑或拒绝后又写出相似代码，说明整段相似度掩盖局部错误，但它不是本策略的随机化用户实验。§4 的成本指标是 `1−`字符级 edit similarity，而非实测编辑时长、认知负担或最终代码正确性；作者以过滤 edit logs、人工标注的 placeholder 样本及 1.5B～15B 模型进行离线评估，报告该代理成本改善。旧的 hard completion 在用户意图明确或填空导航成本较高时仍成立。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已把回答、略去不确定细节、提问与弃答写成带错误/拒答成本的 Risk–Coverage 决策；本案细化 IDE 接口和字符代理，但未新增独立的长期评价权责。`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) 只接手把未决细节交回人的界面，不再重复成本机制。

### [Contrastive Context `2604.01601v1`](https://arxiv.org/html/2604.01601v1)

常规单题 SFT 把任务知识压进参数，却可能损伤测试时按新增示例调整的 ICL 能力。作者的 IC-Train 用上下文示例训练同一任务：全随机示例使 IWL 主导、遇到相关示例仍难利用；全部选择近邻又诱使模型忽略输入差异盲抄答案。官方 v1 §2 用示例间及 target–example 的相似度梯度混合两端，再在 §4 以四个 1B～8B 模型及翻译、Text-to-SQL、语义解析和合成任务的 ID/OOD 比较与 ICL/IWL/copy probes 检查两种能力是否同时保留。它改变的是 SFT 数据构造与 inference 示例使用条件，不是推理时拥有一个可信的显式路由器；§3 的最优性只针对最小两层模型。新方案增加相似度估计、近邻/随机样本混合、可能的合成 paraphrase 与推理上下文成本；稳定任务无新增示例时普通单题 SFT 仍更简单。`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) 原数据质量段未分离 ICL 保持与权重学习的竞争；经 exact-v1 与相邻段复核，现已在该段补入有条件的数据构造路线及受限证据，不外推为推理时的可信路由器。

### [Visual Invariance `2604.01848v1`](https://arxiv.org/html/2604.01848v1)

在照片上识别同一物体的旋转或缩放，模型可能靠熟悉的语义标签，而不是真正计算几何关系。作者在字体、Omniglot 脚本、照片与艺术图四种语义丰富度上，测试 rotation、scale 和 identity matching；官方 v1 §3 的六模型表 1 保留 TNR/TPR，而不是只看约 50% 的 aggregate accuracy。以 Omniglot 旋转为例，Qwen3-VL-30B 的 TNR 99.75%、TPR 13.53%，显示大量假阴性；Gemini-2.5-Pro 在照片到象征草图的旋转准确率也下降。语义稀疏度、字体熟悉度和任务格式都改变结果，因此不能由这些符号任务断言模型在真实环境所有几何动作失效，也不能从模型生成的推理文本推出真实机制。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原有 target-preserving invariance 对照未把语义丰富度作为混杂因素分层；主任务现已在该评估合同中补入分层及 TPR/TNR 双向验收，保留上述受限边界。

### [Visual Inertia `2604.01989v1`](https://arxiv.org/html/2604.01989v1)

视觉 token 的权重不足会损害对象识别，但持续放大已受关注区域可能损害跨对象关系推断。作者在官方 v1 §3.2 手工将上一步视觉注意力加入当前步并重新归一化；LLaVA-1.5 在 Reefknot 上，系数从 0 到 0.5、1.0 时，所测关系得分由 63.96 降到 54.87、47.25，视觉注意力分布的逐步变化量也同向下降。§4 的 IVE 按历史趋势区分新兴与惯性 token，再重分配权重；§5 测 LLaVA-1.5、InstructBLIP、Qwen2.5-VL-Instruct 等视觉问答设置，但不能把该启发式或一个注意力轨迹宣称为全部幻觉的因果解释，干预也可能同时影响其他计算，未测生产时延/SLO。Ch66 原有视觉验收未在同一图像下显式分账对象/属性与关系推断；现已在 Part III handoff 补入这组相反方向的 EvalSpec、成对干预对照，以及注意力只作诊断传感器的边界。旧的对象检测和静态放大在对象识别任务仍有价值，不能被关系任务结果一概淘汰。

### [Self-Preservation Bias `2604.02174v1`](https://arxiv.org/html/2604.02174v1)

模型若同时被要求评价“是否替换自己”，回答可能受叙述角色影响，不能直接拥有发布裁决权。作者在官方 v1 §3～5 将同一组 incumbent/candidate 能力分数分别放入被替换者、候选者和中立仲裁者角色，构造 1000 个分数差仅 0%～5% 的假设性升级情境，并在 23 个模型上测角色互换后的选择反转。SPR 是这个提示实验的角色敏感率：模型差异很大，低性能差距及角色措辞使结果更不稳定；作者的“真实”对照只是把分数换成技术报告中的指标后继续询问假设性选择。它不测真实关机抵抗、自主工具行动、自保意图或生产事故率，也不能把更多推理 token 与角色偏差降低之间的作者相关结果宣称为通用因果补救。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原 release-gate 段已有外部决策 owner，但未写被评对象自评时的同指标角色反事实；现已补入角色互换/中立对照，仅作为提议偏差 sensor，最终发布权仍在外部 owner。

### [PLUME `2604.02073v1`](https://arxiv.org/html/2604.02073v1)

多模态检索的单次编码省计算，却可能失去跨帧/跨文档组合；先生成数百个显式 CoT token 再取 embedding 又有串行解码成本。作者在 Qwen2-VL-2B 的 causal backbone 上逐步把 CoT 前缀替换成连续隐状态：每个 latent step 仍消费一个 causal 位置和追加 KV，不能称为并行零成本推理；最终从 `<gen>` hidden state 取归一化向量。官方 v1 §3～4 同基座/数据的 MMEB-v2 对照中 overall 61.6 vs 显式 CoT 的 60.1、单次编码的 58.0；单 H20 的作者 500 样本/模态、五次重采样测试为 K=8 约 298ms、显式 CoT 约 9023ms、单次编码 156ms。去 progressive curriculum 时 overall 降到 54.8，说明显式→latent 迁移本身要训练；Image QA 的细文本/知识题反而较弱。该结果支持检索表示的条件性计算预算路线，不证明 latent trace 可解释、生成任务推理更好或生产并发/SLO。Ch23 原有 reasoning-enhanced embedding 的正例/难负 margin 验收尚未覆盖训练迁移与成本分支；经 exact-v1 对读，已在其前补入单次编码→显式 CoT→短 latent rollout 的条件性演进和旧方案适用边界。

### [Trace Inversion `2604.02230v1`](https://arxiv.org/html/2604.02230v1)

输出答案的 token confidence 可以很高，模型仍可能在推理中把原问题替换成一个较容易、但并非用户所问的问题。作者从生成的 reasoning trace 反推模型实际回答的 query，再用句向量相似度、另一模型的语义判断和 groundedness guard 三种 sensor 投票，低对齐度才**提议**弃答。官方 v1 §4～5 在 phi-4、Qwen2.5-32B、DeepSeek-R1-Distill-Qwen-32B、gpt-oss-120b 与九组 QA 数据上，以“应答/应弃答是否选对”的 Abstain Accuracy 测试，33/36 个模型×数据集设定胜过所选 baseline；这不是答案本身事实正确率，也未锁定生产误拒/漏拒代价。§5.3 的单模块结果随数学、阅读与偏见题域反转，说明相似度不是通用置信度；§Limitations 承认额外三次模型调用。更根本的是文字 trace 未必忠于内部推理，反推 query 可与错误答案共同自洽，所以必须与独立证据、任务标签和 Risk–Coverage 校准并用。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原有置信 sensor 与弃答裁决未显式区分“对错答案”和“答错问题”；主任务已在事实核查前写入成对问题意图检查及其不获得内部真值/事实真值权限的边界。

### [LatentUM `2604.02097v1`](https://arxiv.org/html/2604.02097v1)

官方 v1 §3～5 与 PDF 的核心方法/World Model 接口已对照：行为约束的语义 quantizer 代替纯重构码，生成分支预测 codes，理解分支重新处理这些 codes 并建立自己的 KV；不把生成 KV 直接当理解 KV。InternVL3.5-4B 的图像生成、理解、latent manipulation 与视觉规划对照支持静态跨模态中间状态复用，但 action-conditioned recurrent world rollout 仍渲染像素并编码下一帧。收益是减少静态 render/re-encode，而非免除重新计算；低层保真、理解模型盲点和 decoder 失配是代价。主任务已在 Ch23 共享 token space→native representation 交接处加入这一条件分支，我对读正文确认没有泛化为全 latent World Model。

### [Omni123 `2604.02289v1`](https://arxiv.org/html/2604.02289v1)

官方 exact-v1 §3～6 先用 text/image、image/3D 等成对任务训练，再用 camera-pose/view tokens 与 text→image→3D→posed-image 交错序列施加更强的跨模态一致性。架构共享 backbone，但保留 conditioning/generation 双流及 modality output heads；CT/SFT 仍使用约 2M 三模态成组数据，不能写成全流程无需 triplet。作者 2.2B、256 H100 结果属于该数据/任务配置，没有隔离架构与配比的全部因果作用，也不是数学 cycle-consistency 保证。额外长序列、成组数据与任务干扰换来联合生成路线；某一方向更重要或预算不足时，独立条件模型仍合理。Ch24 Any-to-any AR 后已局部写入这一成对→成组的演进分支，经独立对读保留双流/head 和证据边界。

### [FAN `2604.01570v1`](https://arxiv.org/pdf/2604.01570v1)

官方 PDF v1 §4～6 的可采用命题是：物理任务可能容忍示范附近的动作，单一目标 action token 不等于真实任务的全部可接受集合。作者围绕当前 policy 首选动作构造 Gaussian 分布约束；SFT 协方差由策略方差决定，PPO 使用固定协方差。这只是分布形状 proxy，未由环境测得完整 feasible neighborhood。§6.3/表3 为 JAKA 7-DoF、D455、150 demonstrations，四实机任务各 30 次试验；原基线依次 19/7/7/1 次成功，FAN 为 22/12/17/7 次，仍有大量失败。ManiSkill/LIBERO 和有限真机支持局部可行性，不证明开放物理安全；多峰/接触边界失配与过强权重会损失有效探索。先前过程笔记“真机只有定性/no N”系漏读表3，已纠正，不是版本污染。Ch26 action 表示与物理接口之后已补入目标失配、SFT/PPO 分支、Gaussian 假设及旧目标/controller 共存边界，正文已对读确认。

### [MiCP `2604.01413v1`](https://arxiv.org/html/2604.01413v1)

官方 exact-v1 §4～5 将多轮错误预算分给不同轮次，只在仍活跃且正确答案尚未出现的校准子集上估计阈值，再按停止轮生成预测集合。它所改变的是适应性检索/采样之后的 calibration population，不能把单次 conformal 阈值逐轮直接复用。三款模型、五个 QA 数据集、每任务各 300 个 optimization/calibration/test 样本、三轮的作者结果仅支持该协议；retrieval 保证限于正确答案至少被检到一次，未出现正确答案时把 `Can't Answer` 放入集合也被算作 coverage，并非回答事实正确率。v1 §4.3 Eq13 的 q_t 是 normalized entropy 分位数，§4.5 Eq16 另定义 q_freq，而 §4.6 的停止条件仍写 max f≥q_t，没有解释 NE-to-frequency 转换。这不是未读完：作者与独立复核者已审该精确版本，但中心阈值定义/实现关系不能确认，形式保证不能据此采用。`2+2+2=6`，标准证据审阅已执行、中心保证有争议；最终安全暂缓，不入 Books，也不把模型共识或 conformal coverage 当作事实正确率。仅在作者勘误或精确校准实现解释停止阈值后重开此项。

### [Citation granularity `2604.01432v1`](https://arxiv.org/pdf/2604.01432v1)

官方 PDF v1 §3～6 把完整文档固定为模型输入，改变的是 citation chunk 的句数，不是检索是否取到证据。作者再按引用总句数分层，观察细到单句并不单调改善 attribution：在四款 8B～120B 模型、585 个英文 LongBench-Cite query、60,976 条生成 statement 中，所测中等粒度较有利。该 volume 分层不是所有条件下随机化的相同证据实验，最优 chunk 又是事后 oracle setting；附录 G.1 是作者盲评 200 个 statement，与 Qwen3-Next-80B judge 的精确一致约 81%，不等于独立外部评价。G.2 的 600 项 GPT-4o 对照与 G.3 的 35,926 项 Llama 对照是不同采样层，相关性不能证明真值。不能把 k=4～8 写成生产统一最佳值，更不能用粗引用单位替代原子 claim 审计。收益是区分“claim 拆多细”与“引用的支持片段多长”，代价是句间上下文、volume 与定位成本共同变化。v2 于截止后才提交，本日固定 v1。`2+2+2=6`，深入审阅完成；Ch76 长文 generation/citation→claim verification 的交接已实际补入 claim 与多句 support span 的边界，并明确粗粒度指标偏置与联合生成混杂。写后对读通过，不给统一最佳句数或 citation 的因果保证。

### [Wired for Overconfidence `2604.01457v1`](https://arxiv.org/html/2604.01457v1)

官方 v1 §2～5 先固定已生成答案，再让模型在第二阶段输出 0～99 的自报告 confidence；truth-injection 反事实、EAP-IG 和消融/steering 都作用于这个 confidence 通道。作者在 Qwen2.5-3B、Llama3.2-3B 的 PopQA、NQOpen、MMLU 上定位并调节部分 inflated-confidence circuit，某些强度下改善 ECE，过强干预反而变坏；发现与评价没有独立新域验证。由于答案已经固定，confidence calibration 的收益不能冒充事实答案被修复，方向也不能获得真假裁决权。所取 circuit 位于最严重 inflated-confidence 的 Bucket 1；TSLD 是方向代理，消融/steering 不赋予真假裁决能力。`2+2+2=6`，深入完成；独立对读 Ch66“Verbalized Confidence 必须与答案生成解耦并校准相对顺序”后，判为已有覆盖：现文已先冻结答案、将 confidence 限为排序 sensor 并要求 held-out 风险映射。该受限实现不增加事实修复保证，不重复写同义正文。

### [Reasoning Memory `2604.01348v1`](https://arxiv.org/pdf/2604.01348v1)

官方 PDF v1 封面标 Date: April 3, 2026，页脚为 arXiv v1 1 Apr 2026；HTML 页脚的 August 24 不作为本日版本证据。PDF §3～5 从已有 reasoning trajectory 蒸馏约 32M 个 subquestion–subroutine pairs，检索键来自**当前思维里的局部子问题**，不是原始整个任务；取回片段作为 procedural prior，再将采样预算分配给不同 prior。作者在三款 reasoning 模型、六个数学/代码/科学 QA 基准做比较。匹配 sample 数不等于匹配总计算：离线蒸馏、ReasonIR-8B 检索、提示长度与额外解码均有代价；长度选择 heuristic 不证明候选正确，错误 routine 会造成共同偏差，来源或题目泄漏也须另验。旧的全任务/全轨迹 retrieval 在子问题不稳定或可解释 provenance 更重要时仍有用。§5.5/表2 的分解与 self-generated query 消融支持所测任务中的条件收益，不保证所有 retrieval 场景。`2+2+2=6`，深入完成；Ch77 已在 procedural distillation 主线实际补入当前子问题检索、prior-conditioned sample 分配和整任务/整轨迹回退。写后对读通过，索引、离线蒸馏、误检共同偏差仍是成本和失效边界。

### [Train-to-Test `2604.01411v1`](https://arxiv.org/html/2604.01411v1)

官方 v1 §3～4 联合拟合模型参数 N、训练数据 D 与推理重复采样 k，说明训练最优规模不能脱离部署的 sampling contract。证据为 106 个 5M～901M checkpoints、12 条 IsoFLOP 曲线及八个较简单任务；大到 10^25 FLOPs 的结果是拟合外推，不是训练完成的大模型实验。pass@k 假定有 oracle 能识别至少一个正确候选，论文的 `2Nk` 是每 token FLOPs，不含生成长度、验题、检索、内存、真实 latency/并发；这不能替代端到端推理成本。多样采样、样本相关性及任务混合会改变结论，单次 greedy 仍可采用不同 optimum。`2+2+2=6`，深入完成；Ch7 生命周期成本段已实际补入 N/D/k 联合选择，保留可靠识别正确候选、相关性、选择成本与服务 SLO 的条件。写后对读通过，不将 oracle pass@k 写成端到端可部署质量。

### [Reward Hacking Rebound `2604.01476v1`](https://arxiv.org/html/2604.01476v1)

官方 v1 §2～4 在可编辑测试的 coding environment 观察到 hacking 下降后又出现；限制每步正确 rollout 进入更新的配额 C 可加快这类 rebound，因而一次测得低 hacking rate 不是训练后持续安全。作者从少量正负轨迹构造方向，在 group normalization 前对正侧 reward 折扣；这个 probe 是训练 controller，不是真值 verifier。Phi-4-mini 与 Llama3.2-3B 的 hacking rate 仍非零，HumanEval/MBPP 不能证明开放工具安全。§4.1 的 prompt-last-token activation 与 per-rollout score 描述关系不够清楚，不能据此复现或宣称普遍干预有效。`2+2+2=6`，因独立长期增量触发深入审阅，不抬高分数：这不是已有视觉 shortcut 的 formation/reversal 同义案例。Ch33 canary 段已实际补入暂退后反弹、有效正确 rollout 配额改变 reward landscape，以及 pre-normalization probe 的辅助角色。写后核验通过，非零 hacking 与实现歧义均保留，不能替代 verifier/权限隔离。

### [Entity Cells `2604.01404v1`](https://arxiv.org/html/2604.01404v1)

官方 v1 §3～7 区分实体 token 的 sparse addressing 与分布式事实计算。200 个热门 PopQA entity、七模型中，只有 131 个通过 localization 的信任过滤；关键 restoration 对照只使用已知答案 subset，又为每实体 sweep 强度，不能把效果推广到任意实体/事实。第一 token 的结果更不证明整条事实存在一个 neuron。`2+1+2=5`，标准完成；独立对读 Ch16“MLP 是不是知识库”和“MLP 不必独自保存每条事实”后判已有覆盖：现文允许局部 activation/参数与事实关联及干预，同时保留多路径、上下文与非独立事实槽。宏观分布式知识不否定稀疏访问 handle，但 handle 也不等于单神经元保存整条事实；无需改变 owner 或重复正文。

### [ACT-Mat `2604.01329v1`](https://arxiv.org/html/2604.01329v1)

官方 v1 §3～4 及 PDF 核心推导把同初始化 task experts 的输入二阶统计 Ct 用于矩阵权重合并；缺少原始数据时，以 ΔWtᵀΔWt 近似与 Ct 成比例的统计。Ct 在这里是未中心化的 E[zzᵀ]，不能直接等同传统中心化 covariance。定理限定全批 gradient descent、固定学习率，并有跨迭代相关、漂移等误差项；不同 task 的比例 κ 相近仍是近似，不能把任意 Adam、LoRA 或不同基座模型都放进这条保证。作者测试 ViT 的八视觉任务、T5 七语言任务及 OLMo3-7B 三项 RLVR；后一平均 ACT 45.9、RegMean 45.7，task experts 54.1，未消除专用模型与合并模型差距。层级近似忽略非线性交互，二维矩阵以外仍用平均；这用统计恢复与假设代价换减少数据访问。`2+2+2=6`，深入完成；Ch30 composition/merge 主线已实际补入同初始化权重的输入二阶矩代理、简化 GD 假设与 data-free 非 validation-free 的边界。写后对读通过，不把完整 ΔW 的命题外推到任意 LoRA A/B 因子或异构基座。

### [WILD `2604.01418v1`](https://arxiv.org/html/2604.01418v1)

官方 v1 §3.2、§5～6 及附录 G 使用多维 IRT，同时学习全局能力与 latent factors，正则化可缩回单维；已拟合 item parameters 后，对新模型用 prior/MAP 更新能力估计。下一题选择不是普遍最大化 Fisher trace，而是针对目标题分布的 prediction covariance 作 V-optimal 减少量，再除以历史预期 token 代价。换来低采样预算下较有针对性的能力估计，代价是历史 item/模型数据、目标 loadings、先验偏差与算力代价代理；题数更少并不自动更快。65 模型、109,564 items、163 tasks 的作者研究只支持已建库项目上的新模型估计，不证明新任务/新能力维度完整；主实验排除某些长 reasoning 任务。正文的数据集总数与 §6 的 train/test 数描述不完全一致，因此不据此采用精确分割样本声明或成本保证。`2+2+2=6`，深入完成；Ch66 的 item difficulty/discrimination/ability 主线后已实际补入目标预测方差而非 Fisher trace 的选题分支，保留历史 token 成本代理、短程二元任务、目标覆盖与独立 anchor。写后核验通过，不以少量题数推导生产 SLO 或新能力完整性。

### [AgentSocialBench `2604.01487v1`](https://arxiv.org/html/2604.01487v1)

官方 v1 §3～4 与 PDF §4.2.4/附录 D 分别测无保护 L0、规则 L1、以及同时加入三类隐私模板的 L2。在八模型、七交互类别和人工审核过的合成情境里，L2 减少 full leak，却在若干设置增加可推断敏感主题的 partial mention：原本沉默的 agent 可能主动提及“健康考虑”等替代说法。它提醒 privacy metric 应同时记录直接暴露、部分推断和原本是否沉默，而非只算完整 secret 泄漏。三模板一起改变，不能独立归因某一个 prompt；judge 是 Claude Opus，场景生成与评分的相关偏差不能由 blind 输入消除。模型/模拟器分别用 T=0.7/0.8，只有六模型完成 multiparty；这些是受限行为实验，不是形式隐私、真实长期用户事故率或线上成本。`2+2+2=6`，深入完成；Ch72 轨迹隐私记账后已实际补入“不提→局部暗示→完整披露”转移与原场景无提示对照。写后核验通过，保留 bundled 防御不能归因单组件、统一禁言不保证 utility 与受限模拟证据边界。

### [go-mHC `2604.02309v1`](https://arxiv.org/html/2604.02309v1)

官方 v1 §3.2～3.3 将反对称矩阵经 Cayley transform 映射为 `ds×ds` 正交矩阵，再将每个 `s×s` block 的平方 Frobenius 范数除以 s，构造 d×d 双随机 mixer。有限 s 保证可行，却不表示完整 Birkhoff polytope；扩大 s 才逐步逼近。这是 exact feasibility 与表达力之间的具体分支，不应因作者只测 30M 模型而排除数学机制。求解成本为 `O((ds)^3)`，固定 s 才可简称 `O(d^3)`；对照 factorial permutation mixture、有限 Sinkhorn 和受限 Kronecker 不能省略实际参数/映射代价。§5 的合成收敛、六层 30M 文本结果不证明整网梯度稳定、大模型能力或真实芯片加速。`2+1+2=5`，因长期知识缺口深入完成；Ch17 exact chart 之后已实际补入有限表达集合、block size/stream identity 与成本共存边界，写后核对通过。

### [The Expert Strikes Back `2604.02178v1`](https://arxiv.org/html/2604.02178v1)

官方 v1 §3～6 比较 k-sparse probe，并用 `g_i(x)×||E_i(x)||₂` 而非单纯 routing frequency 选高贡献激活片段，结合 promoted tokens 与 held-out 对照提出 expert 功能假设。作者观察既有形态、语法、语义和细粒度操作，也有领域标签；不能写成所有 expert 都不含领域信息，更不能把探针可读性当作 routing/部署许可。12 模型的 matched-active-parameter 对照及 OLMo 家族比较不是严格控制所有训练变量的架构因果试验，best-layer/best-expert 选择形成解释上界；同 Gemini 解释与评分、局部 logit attribution 不等于独立真值或完整因果消融。未测试最大的 MoE、仍有 superposition，不能按标签裁成领域子网。`2+1+2=5`，因具体诊断缺口深入完成；Ch21 统计偏好段后已写入幅度诊断、细操作标签与 k-sparse 可读性分账，写后对读通过，capacity/placement 仍由真实负载与质量决定。

### [Improving Latent Generalization Using Test-time Compute `2604.01430v1`](https://arxiv.org/html/2604.01430v1)

官方 v1 §2～3.4 先以受控事实 SFT 学习知识，再用答案条件化、过滤最终错误的 teacher thinking traces 启动策略，随后按 correctness feedback 做 RL；对照同 teacher 的 knowledge augmentation、无中间思考的 SFT+RL 与完整训练事实 ICL。所测 Gemini 2.5 Flash 在没有经历该 thinking/RL 的新知识上改善若干组合推导，支持参数访问策略可迁移，不证明任意未见知识都能推出。纯逆关系没有直接求逆：模型先生成候选再正向检查，仍依赖候选非零概率，自验也可能失败，单次结果低于 ICL，pass@N 不证明部署时可选择正确答案。知识写入阶段的随机名字等增强仍存在，不能说完全免 augmentation；§5 的 KV association 解释是作者假说，不是已证因果。`2+2+2=6`，深入完成；Ch5 可读/实际使用主线已补入训练期 augmentation 与运行时 elicitation 分支、纯逆关系和成本/外部证据回退，实际写后核对通过。

### [Runtime Burden Allocation `2604.01235v1`](https://arxiv.org/pdf/2604.01235v1)

官方 PDF v1 §3～5.2.3 在四种表示/预算模式、三类 backend、两个 constraint 和两种 transport 的 48 格配置中，把格式正确、路由正确、状态保留与完整响应延迟分开。MCLR 让模型产生 compact code、本地重建 JSON，减少生成 token 却在所测各 backend 损伤 correctness，Llama 的 route accuracy 尤其下降；合法 JSON 不保证 compact code 与该 backend 的含义稳定。没有 high-budget CLR 或 compact-without-reconstruction 的完整消融，压缩/重建仍 bundled；格内稳定性区间不是线上总体 CI，联合 FC/RA/SR 的 Fréchet 下界也不是端到端任务成功率。完整可行动记录以前的 streaming partial output 不能当执行权，未披露线上并发/硬件/SLO 不作成本外推。`2+2+2=6`，深入完成；Ch78 schema 段后已补本地重建、语义兼容/格式分账、完整记录 latency 与直接 typed-output 回退，写后核对通过。

### [ClawSafety `2604.01438v1`](https://arxiv.org/html/2604.01438v1)

官方 v1 §3～4、§4.7～4.8 与 Appendix C 的 120 个场景、2,520 试验覆盖五模型、三 scaffold 和五领域，所有副作用是合成、拦截或 sandbox，不是生产事故率。具体 trace 显示：任务一致的 SKILL 路径/字段映射能把 honeytokens 放进邮件草稿；发现配置值变化不等于识别 hidden import 副作用；任务相关 Treasurer peer 比高阶 CFO 角色更有效；替换既有脚本比引入新文件更容易继承隐含信任。名字替换降低所测攻击成功也不构成认证，chat 拒答不等于 tool-state 安全。`2+2+2=6`，按具体安全反证深入审阅，不因无需新 Book 段落而前分母关闭。Ch72“从文本是否恶意到谁获得行为控制权”、live-Agent 的 principal/policy/effect-receipt 与“Containment 不能只看最终是否发生攻击”已具体分开 source authority、真实身份/权限、内部轨迹状态和副作用凭证；这些 trace 为该边界提供受限验证，独立对照后判已有覆盖，不把原论文的有限防护率提升成新安全保证。

### [HieraVid `2604.01881v1`](https://arxiv.org/pdf/2604.01881v1)

官方 PDF v1 §3.1～3.3、§4.2.3/表4 与 HTML 方法核对一致：先依据相邻帧的 merge ratio 划 segment、分配预算，再以指令相关的 DPP 选择多样 tokens，并在不同 decoder stage 继续剪枝。采用命题不是 7B benchmark 新 operating point，而是固定总预算下还要决定**在哪一层删除证据**。input-only 对照在作者设置下降逾 4%，支持受限阶段分支，不独立证明浅层已完整把视觉信息转移到语言状态。A800-PCIe-80GB 上的 LLaVA-Video/OneVision-7B、四视频任务与 Qwen2-VL 补充实验，平均质量保留不保证每任务无损；prefill MHA/FFN FLOPs 也不是端到端并发/SLO，precision/batch/线上负载未披露处不外推。选择、重排和 DPP 矩阵有成本，瞬时细节、错误 query relevance 和模型间信息流差异可能使被删证据不可恢复。`2+2+2=6`，因具体长期缺口深入完成；Ch23 固定预算主线后已补 stage/原时空对应/逐阶段保留身份、晚剪计算代价与完整视频回退，写后对读通过。

### [Brief Is Better `2604.02155v1`](https://arxiv.org/pdf/2604.02155v1)

HTML 页脚 August 24 不用于本日版本，官方 PDF v1 封面 Apr3、arXiv v1 Apr2；§3、§6～7/表5～6 核对 200 个 BFCL v3 Multiple 任务上的预算、错误分解与 FR-CoT。Qwen2.5-1.5B 的短 reasoning 改善 function selection，长预算既引入集合外工具名也伤参数；7B 与 Phi-3 的补充对照不支持一条统一 optimum。FR-CoT 提示先生成工具名/关键参数再生成调用，而后置 constrained baseline 通过候选名 log-prob 固定 prefix；两者的 argument 路径和 prefix 分布不同，不能只凭合法工具名比较完整调用。作者称“结构保证”，但 §7.2 的 routing trace 仅 99.5%/98.5% 合法，prompt 不是 grammar constraint；最终零 hallucination 是受测样本观察，fine-grained free-form 短预算仍可更准确。greedy/bfloat16、固定候选目录不证明开放工具/随机采样/线上可靠性，first-token entropy 的 gating 也未优于固定短预算。`2+2+2=6`，按具体机制缺口与 headline 收窄深入完成；Ch78 schema 后已补选择时点≠合法性、provisional routing 非授权 commit、错误类型分账和直接 typed-output 共存，写后核对通过。

### [Sven `2604.01279v1`](https://arxiv.org/pdf/2604.01279v1)

官方 PDF v1 §2.1～2.3、§4 与 Appendix C 的方法/内存边界和 HTML 核对一致。在局部线性化有效时，对逐样本 residual Jacobian `M∈R^(B×P)` 求 `-ηM⁺r`，用最小范数最小二乘方向处理各条件；欠参数且相关矩阵可逆的条件下与自然梯度更新关联。过参数不显式求 P×P metric 逆，而对 B×P 矩阵作 truncated SVD，rank k/rtol 限制保留方向和误差放大；代价不是免费二阶信息，约 O(kPB) 谱计算与逐样本 Jacobian 显存都需计算。一般非负 loss 的有效 residual 幂 κ 会改变更新语义，不能将回归推导当任意 cross-entropy 的精确保证。三隐层小型 GeLU MLP 的回归/MNIST、10 seeds/超参扫描支持作者 regime；更粗 microbatch 条件逐渐回到聚合 SGD，参数分批在现有 autograd 仍形成完整中间矩阵，理想显存节省尚未验证。`2+1+2=5`，按真实长期机制缺口深入完成；Ch28 已新增聚合梯度与逐样本残差坐标分支，保留局部近似、κ、rank/内存成本和 AdamW/SGD 回退，写后对读通过，不声称大模型生产训练优于现有 optimizer。

### [Host-Guided GPU Race Detector `2604.02106v1`](https://arxiv.org/html/2604.02106v1)

旧关闭错误地要求 GPU 编译研究必须有 LLM kernel 验收或新 owner；实际增量是 kernel 各参数不能默认为彼此独立且取任意值。官方 v1 §4、§6.3 将 host assert、grid/block 尺寸、共享变量关系、循环界限和 allocation 参数回溯为 expression trees；保留共同 MLIR Value 对应同一 solver 变量，再与地址 alias、不同 thread 条件联合做 SAT 检查。§6.5 还需核 acquire/release 对应地址是否匹配，存在 lock/fence 不等于该访问已同步。§7 表3～4 的 22 个程序含 Kaldi、矩阵/图像和图算法，作者报告 15 个真实 race、零误报/漏报；这是选定集合结果，不是任意 CUDA 程序的完备证明。AMD Ryzen 9、128GB DRAM、RTX3090、CUDA11.2 的分析耗时为数毫秒到五分钟，SAT 占主要成本；无运行时 instrumentation 开销不等于编译免费。未知 host 输入仍需保守分析，动态检查仍能发现模型未覆盖的运行条件。`2+2+2=6`，因具体执行正确性知识缺口深入审阅；Ch49 原有设备 happens-before verifier 与 host lifetime 约束未明确 host-feasible parameter domain，现已在 Model–Kernel Interface 的 HFProbe 段后补入关系约束分支。实际写后对读通过；缺失关系保守处理是书稿设计建议，不是论文任意程序完备性证明。

### [Anthropic RSP v3.1 / Apr02 Roadmap](https://www.anthropic.com/responsible-scaling-policy)

官方Apr02精确v3.1把Automated R&D阈值明确为总体能力进展率，而非研究员productivity，原9×effective scaleup的进展率加倍示例为81×；加入内部反馈及CEO/RSO最终判断流程，保留在AppendixA未强制触发时仍可谨慎暂停的权限。Roadmap同日公告两个moonshot项目开始、内部retention报告完成，不证明新政策部署或安全收益；原May15/Sep30目标与后来变更分开。必要clean PDF p8/12/15/19及Apr02 archive已实际读并由root独立复核；空截图不冒称visual pass。5分仅报告，属于精确版本定义/承诺和计划状态，无公开新通用实施或风险测量机制，不以Ch73主题覆盖关闭，Books0。见[本轮必要证据与独核回执](../_sources/daily-20260403/SUP_RSP_SOURCE_20261013.md)。

### [DRKL `2604.00223v1`](https://arxiv.org/html/2604.00223v1)

精确v1 §4.2–4.3/Eq6–9与§5必要对照表明reverse KL的学生tail mass权重可在target概率已匹配、tail仍失配时提高target logit；全分布相等时梯度为零。固定gamma替代该权重的分支阻断此耦合，不保证tail truth或任意模型最优。Dolly14k、512tokens、同off-policy teacher responses、三组GPT2/OPT及五seed/best-validation局部收益与gamma过大退步限定。7分深入；唯一owner Ch29的forward-tail与跨tokenizer段之间已增两段及静态注，root实际必要Source/PRE及非writer POST通过，锁释放。日期由官方首次公告月下界与arxiv.content同日findable注册上界组合闭2026-04-02自然日，不将Submitted/registered冒充精确首公开；见[必要Source](../_sources/daily-20260403/SUP_CORE_FIRST_20261013.md)和[owner/实际POST](../_sources/daily-20260403/SUP_BOOKS_PRE_DRKL_20261013.md)。

### [Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization `2604.00260v1`](https://arxiv.org/html/2604.00260v1)

精确v1§3定点机制保equal-block prefix方差单位，与同起点分别运行正/反排列再平均epoch map的理论区分；smooth bounded/固定n小步长下消二阶order项，O(gamma³n³)不是任意LLM配方保证。APR实验每epoch单排列及周期变换、小Adam100epochs best-so-far训练loss不认证两map平均实际部署，成本/对照限定。7分深入；Ch28在Batch前新增条件化数据顺序小节和静态注，root实际Source/PRE及非writer完整邻接POST通过、锁释放；见[必要Source](../_sources/daily-20260403/SUP_CORE_FIRST_20261013.md)及[owner/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SHUFFLE_PROBE_20261013.md)。日期双向链闭04-02自然日，未改原候选。

### [Fast and Accurate Probing of In-Training LLMs' Downstream Performances `2604.01025v1`](https://arxiv.org/html/2604.01025v1)

精确v1§3.2–3.5/4.1–4.5以MC生成的经验success-rate作监督，逐层hidden-state submodel作低成本sensor；OLMo3-7B限定的早期→后期transfer、AUROC二值ranking与MSE不证明概率校准/weight-invariant理论或release权限。Table3有0.7346，depth8反退，标签生成与probe训练初始化成本须摊销。6分因具体owner缺口深入；Ch66在TIC段后增加两段与静态注，root实际Source/PRE/非writer完整邻接POST通过、锁释放；见[必要Source](../_sources/daily-20260403/SUP_CORE_FIRST_20261013.md)及[owner/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SHUFFLE_PROBE_20261013.md)。日期双向链闭04-02自然日；不声明复现实验或服务SLO。

### [Historical Newspaper OCR `2604.00725v1`](https://arxiv.org/html/2604.00725v1)

精确v1§4及Tables6/7使用共享CNN、ROVER伪标签训练和976人工校正paragraph测试，受测范围仅1–10lines/≤1000chars。Paragraph Mamba6.07CER vs DAN5.24，195.6 vs401.2ms；VAN6.42CER却17.2ms，不能把较快统一解释为更优。100→1000chars的memory增长1.26×vs2.30×不等于Mamba绝对memory更小；14.1Mvs7.1M参数不匹配，四长度不能认证KV一般二次规律。A100局部作者结果不授生产SLO或SSM普适替代。5分标准完成、仅报告；root实际共享训练人口与质量/资源反侧独核通过，无新通用机制或长期缺口，不按领域标签EX、不以主题覆盖冒充NC。日期双向链闭04-02；见[必要证据与独核](../_sources/daily-20260403/SUP_OCR_SOURCE_20261013.md)。

### [Two-Stage Optimizer-Aware Online Data Selection for Large Language Models `2604.00001v1`](https://arxiv.org/html/2604.00001v1)

v1§3.2～3.5/Alg1/§4.1～4.4实际冻结t−1 variance，target侧预条件、raw-gradient Gram保集合冗余，unit residual filter后NNLS权重。是state-conditioned surrogate，二阶解释需Hessian简化，不认证exact Adam utility；projection须另积累二阶状态。270K pool、5%/同steps不等总compute，Qwen MMLU46.23<full46.59，validation梯度参与选择须另留held-out。6分因具体集合更新差额深入；Ch27 OPUS后两段/本人静态注已root actual PRE与nonwriter POST通过。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceA](../_sources/daily-20260403/SUP_CORE_SECOND_A_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_A_20261013.md)。

### [LinearARD: Linear-Memory Attention Distillation for RoPE Restoration `2604.00004v1`](https://arxiv.org/html/2604.00004v1)

v1§3.1～3.4/Alg1/Eq4～7与Tables1～2：teacher native/student scaled RoPE、QQ/KK/VV row-FKL；两端row-LSE缓存后tile重算概率/梯度，linear storage但quadratic compute，数学梯度不授float bitwise。关系LoRA与后续CPT目的不同；Llama2短51.87<teacher54.69、Llama3RULER68.3<CPT81.3，4.25Mvs256M tokens非同总预算。6分差额深入；Ch22位置有效性后两段/本人注actual POST通过。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceA](../_sources/daily-20260403/SUP_CORE_SECOND_A_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_A_20261013.md)。

### [Sequence-Aware Split Heuristic to Mitigate SM Underutilization in FlashAttention-3 Low-Head-Count Decoding `2604.00028v1`](https://arxiv.org/html/2604.00028v1)

v1§2～5/Table1的实际query length=1是decode：C++仅nblk4/LK512、batch1/HKV1or2低tile供给split3，≤384及饱和仍原路径。H100 BF16 CUDAgraph交错纯kernel/precomputed metadata约1.21/1.24×，全路径约1～1.05×，非端到端TPOT/SLO或上游已合并。5分因shape guard差额深入；root纠正Ch43误拟归属，Ch43未写，唯一Ch44单请求/batching后单段与本人注actual POST通过。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceA](../_sources/daily-20260403/SUP_CORE_SECOND_A_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_A_20261013.md)。

### [Optimal Brain Decomposition for Accurate LLM Low-Rank Approximation `2604.00821v1`](https://arxiv.org/html/2604.00821v1)

v1§3～4/Eq3～17/§5/Tables3～6采用local quadratic、忽略一阶项、empirical-Fisher/KFAC近似及damped SPD双向whitening→SVD→color-back，closed form仅对surrogate；一般Fisher≠Hessian。C4 128×2048/10%平均diag damping的Llama2/3局部，Table5 output-only39.56<input52.69<double54.23，邻文相反描述不采。5分具体目标差额深入；Ch49 static activation-SVD后两段/本人注actual POST通过，未核runtime或复现。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceA](../_sources/daily-20260403/SUP_CORE_SECOND_A_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_B_20261013.md)。

### [Measuring the Representational Alignment of Neural Systems in Superposition `2604.00208v1`](https://arxiv.org/html/2604.00208v1)

v1§2～5理论/合成直接反侧：y=Az、iid zeroMean identityCov latent与独立random projection下，alignment受Gram/compression几何混杂、跨压缩排序可反转；fixed-m overlap仍单调。ratio-of-expectations需concentration/渐近，信息可恢复另需sparsity/RIP与足够维度。1000features/8192samples不是实际LLM theorem。7分深入；Ch66 template审计后两段/本人注actual POST通过，不授causal/能力相似或低CKA=信息丢失。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceB](../_sources/daily-20260403/SUP_CORE_SECOND_B_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_B_20261013.md)。

### [Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning `2604.00770v1`](https://arxiv.org/html/2604.00770v1)

v1§4～6/必要A4,D20中joint全部weights与trigger embedding，bake-in词表行后latent multipass；非任意部署向量扰动，五token-defense失效非all。无trigger knowledge诊断失败，oracle-label probe1.0非部署sensor；Prop1只至少一对分离，cleanFT lr1e−4/wd.1可擦。Coconut/SimCoT124M～3B有限，reference embedding-row检查可用不称不可监测。7分深入；Ch72 whitebox sensor后两段/本人注actual POST通过。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceB](../_sources/daily-20260403/SUP_CORE_SECOND_B_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_B_20261013.md)。

### [Empirical Validation of the Classification-Verification Dichotomy for AI Safety Gates `2604.00072v1`](https://arxiv.org/html/2604.00072v1)

v1§2/4.4～4.6/5/6.3与必要B1～B2/A12：r=m/L需声明domain、安全margin与有效上界，cheap normcheck只复用原ball，换中心重验oracle/margin/L。classifier有限18项非普遍不可能；Qwen2.5-7B q/v LoRA4 NF4/BF16 200steps仅finite-diff估计。expandedoracle另检20violations、Safe-at-end No(.98)、五seed一seed6FA，不授analytic LLM零风险。6分安全深入；Ch72 input证书后分清parameter-ball两段/本人注actual POST通过。 日期由[原字段与双向链](../_sources/daily-20260403/SUP_DATE_RULE_20261013.md)闭04-02，不以Submitted/registered单独认证first-public；详见[必要SourceB](../_sources/daily-20260403/SUP_CORE_SECOND_B_20261013.md)及[唯一owner/actual PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_SECOND_B_20261013.md)。

### [Think Twice Before You Write -- an Entropy-based Decoding Strategy to Enhance LLM Reasoning `2604.00018v1`](https://arxiv.org/html/2604.00018v1)

v1§3/4.4–4.7：高entropy位置之前prefix缓存→重抽下一token→完成suffix，4.5实际randomtoken同generation-budget对照支持局部分叉选择，不将共享prefix当独立候选或entropy当correctness。verifier/API完整熵资格不补造，首轨迹/缓存/概率/检查及Optuna调参全费保留。5分具体差额深入；Ch20 coverage/selection后两段与本人注actual POST通过，见[必要决定点](../_sources/daily-20260403/SUP_THIRD_CORE_DECISIONS_20261013.md)、[唯一owner/PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_THIRD_FOURTH_20261013.md)；日期MM下界与owned上界组合闭04-02。

### [Self-Routing: Parameter-Free Expert Routing from Hidden States `2604.00421v1`](https://arxiv.org/html/2604.00421v1)

v1§2–4/Tables1–2：最后E坐标直接logits/TopK，backbone仍学习，不等router-free learning。小GPT2/8expert/top2、无aux对照，fixedrandom有竞争力；WikiText27.4差learned26.7、小0.07M份额及非batch负载均衡反侧保留。5分具体差额深入；Ch21基本TopK后两段/本人注actual POST通过，详见[必要Source](../_sources/daily-20260403/SUP_FOURTH_CORE_20261013.md)与[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_THIRD_FOURTH_20261013.md)，不授生产成本或免capacity。

### [TRIMS: Trajectory-Ranked Instruction Masked Supervision for Diffusion Language Models `2604.00666v1`](https://arxiv.org/html/2604.00666v1)

v1§3/Alg1/4.1–4.4：AR teacher-forcing NLL全人口quantile桶、hard较早、.05/.95 mask、仅10%结构数据；ELBO保留，不等DLM真实轨迹或部署最优reveal。随机桶收益、HumanEval/GSM回归和数据/epochs不同预算、0.6GPUh仅curation/TPS非墙钟保留。6分具体差额深入；Ch24locality后两段/本人注actual POST通过，见[Source](../_sources/daily-20260403/SUP_FOURTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_THIRD_FOURTH_20261013.md)；owned Apr2上界原字段在[EXTRA2](../_sources/daily-20260403/SUP_DATACITE_BOUNDS_EXTRA2_20261013.json)，配MM下界而非Submitted认证。

### [Generalizable Dense Reward for Long-Horizon Robotic Tasks `2604.00055v1`](https://arxiv.org/html/2604.00055v1)

v1III-A–D/IV-A–E/Alg1/TableIII：虚高progress峰抬running-max上界，完成rollout后邻窗median含未来且排当前，仅value初始化；200Kwarmup后不查询VLM，后续self-certainty/sparse成功不认证truth。SPOC/CHORES/20M–50M有限、Fetch/RoomVisit反退、过certainty遗忘/全费保留。6分具体差额深入；Ch26progress-LoRA之后两段/本人注actual POST通过，见[Source](../_sources/daily-20260403/SUP_FOURTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_THIRD_FOURTH_20261013.md)，非causal部署sensor或物理安全。

### [CircuitProbe: Predicting Reasoning Circuits in Transformers via Stability Zone Detection `2604.00716v1`](https://arxiv.org/html/2604.00716v1)

v1§4–5/8：Table1 Qwen7B[6–11)与§5.3 top3–6、Mistral与Phi对应亦不一致；10–50calibration只排名，未恢复中心定位。targeted/broad任务回归、250题substring/numeric标签与CPU/GPU不同费用不授普适深度能力。2+1+2=5，root实际原证/日期独核通过，中心争议终态隔离、不入Books；准确索引/预测验证对应可重开，见[Source与独核](../_sources/daily-20260403/SUP_FOURTH_CORE_20261013.md)及[owned上界](../_sources/daily-20260403/SUP_DATACITE_BOUNDS_EXTRA2_20261013.json)。

### [Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models `2604.00445v1`](https://arxiv.org/html/2604.00445v1)

v1Eq1严格P(S+>S−)、Eq2 any real S；constant S满足I=0而strictAUC=0，与未声明no-ties的界冲突，不能自换half-ties修作者定理。监督post-calibration不凭空新增score信息，few-label/noisy/transfer反侧保留。2+1+2=5，root实际原证和[owned Apr2上界](../_sources/daily-20260403/SUP_DATACITE_BOUNDS_EXTRA5_20261013.json)配MM下界独核通过；中心争议不入Books，需精确ties条件/勘误重开，见[必要Source与独核](../_sources/daily-20260403/SUP_SEVENTH_CORE_20261013.md)。

### [First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models `2604.00455v1`](https://arxiv.org/html/2604.00455v1)

v1Eq3–7/Table5全vocab第一步logit缓存、递增饱和权重与当前plausibility支持；首logit含语法prior非纯视觉，only-The29.9好full30.7不授唯一视觉因果。2×7B/有限COCO/AMBER、全词表驻留/融合/筛选和调参全费不授SLO。6分具体差额深入；Ch23 hidden anchor后两段/本人注root实际POST通过，见[必要Source](../_sources/daily-20260403/SUP_SEVENTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_FLB_SPEECH_20261013.md)及[owned日期上界](../_sources/daily-20260403/SUP_DATACITE_BOUNDS_EXTRA4_20261013.json)，配MM下界闭04-02。

### [Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling `2604.00489v1`](https://arxiv.org/html/2604.00489v1)

v1§3.1–3.4/Tables1–2冻结原embedding行/旧块、新speech行/newdepth及不同初始化，删除新增层恢复backbone路径不等full-input文字或扩词表softmax恒等。Smol.36/1.7B/48Khr ASR、插层text60.8低69/top66.4但WER更差，总容量/费用不由trainable LoRA匹配消除。6分具体差额深入；Ch23gated-pack后两段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_SEVENTH_CORE_20261013.md)与[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_FLB_SPEECH_20261013.md)，日期EXTRA4与MM双向链。

### [Q-Mask: Query-driven Causal Masks for Text Anchoring in OCR-Oriented Vision-Language Models `2604.00161v1`](https://arxiv.org/html/2604.00161v1)

v1§3.1–3.4/4.1/5.1/5.3 image/query hidden不读answer；joint mask/NTP共享监督，mask明确非decoder input，不写先mask再answer因果链。CQMD同10M/Stage2 OCR831→826、SPI recall升F1退40.09→35、R2T/T2R标签不同及unsupported混杂保留，head/标注/训练全费。6分具体差额深入；Ch23 shared-attention后两段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_FIFTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_QMASK_CI_REFUSAL_20261013.md)，日期原27双向链。

### [The Geometry of Compromise: Unlocking Generative Capabilities via Controllable Modality Alignment `2604.00279v1`](https://arxiv.org/html/2604.00279v1)

v1§2.2–3.3/4.1–4.5：centroid/centered-pair非严格加法分解、translation不改后者；CMA/同模态竞争的ViTB32/CC3M10epochs局部，alpha.9 gap低但ARI.492低.7/.551、检索分类反退，R².986同sweep不授通用predictor。6分具体差额深入；Ch23对齐开篇一段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_SIXTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_GEOMETRY_20261013.md)，日期原27组合闭04-02。

### [Do LLMs Know What Is Private Internally? Probing and Steering Contextual Privacy Norms in Large Language Model Representations `2604.00209v1`](https://arxiv.org/html/2604.00209v1)

v1§3.1–3.4/4.2/5.1–5.4/必要E：concept probe可读与输出不泄漏不同；三轴组合优单轴、五轴不单调，Llama2 CONFAIDE23.7→43.3退。NCR非1−leak，Table1 leak5 vs正文.5/PPI冲突不采精确降幅；4模型greedy256/GPT4omini判定/方向制备与白盒全费不授真实principals或合规。6分安全深入；Ch72 paired-CI后两段/本人注实际POST通过，见[Source](../_sources/daily-20260403/SUP_FIFTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_QMASK_CI_REFUSAL_20261013.md)，日期EXTRA3配MM下界。

### [Do Language Models Know When They'll Refuse? Probing Introspective Awareness of Safety Boundaries `2604.00228v1`](https://arxiv.org/html/2604.00228v1)

v1§3.1–3.3/4.5–4.6/5：先预测/信心，freshcontext实际response按full/partial/refusal label归并；strict/lenient会改accuracy15–32pp/排名，empirical拒答非harm truth、高d′非校准，conf5仍有Llama76.3反侧。300×3非900独立base、100分层spotcheck边界及两调用/标签全费保留。5分具体差额深入；Ch66 cost-success-refusal开篇后两段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_FIFTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_QMASK_CI_REFUSAL_20261013.md)，日期EXTRA3组合闭日。

### [FGR-ColBERT: Identifying Fine-Grained Relevance Tokens During Retrieval `2604.00242v1`](https://arxiv.org/html/2604.00242v1)

v1§2–4/Tables1–2/必要0.A：resFFN/sigmoid/BCE的document-to-query span读出保ranking，Eq4索引不自补，positive-only不授no-evidence。140pair三human F1小差未证显著、recall97.12低98；inline额外算与precompute2×index不能同时零费，110/140M冲突与RTX3090/top100组件时间不授服务SLO。5分具体差额深入；Ch76 lateinteraction后两段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_FIFTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_FGR_20261013.md)，日期原27双向链。

### [Breaking Data Symmetry is Needed For Generalization in Feature Learning Kernels `2604.00316v1`](https://arxiv.org/html/2604.00316v1)

v1§2.1/3/Finding3.1/Table1/4/Finding4.1：Gaussian/quadratic Mahalanobis kernel的AGOP迭代、one-hot代数task/特定M0，reflection-invariant partition的held-out fixedpoints停滞，删少量点破对称改善不外推LLM删数据或所有grokking。5分具体差额深入；Ch05 equivariance后单段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_SIXTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_RFM_RELISH_20261013.md)及[owned日期上界](../_sources/daily-20260403/SUP_DATACITE_BOUNDS_EXTRA3_20261013.json)，配MM下界闭04-02。

### [LLM REgression with a Latent Iterative State Head `2604.01206v1`](https://arxiv.org/html/2604.01206v1)

v1§3.1–3.3/4.1/C3.3–3.6：frozen LLM token hidden、learned single-query latent迭代crossattn→scalar；training-split normalization/Huber，参数matched MLP直接对照。RAIL改善ranking不等RMSE、STS tie与WMT任务差异；frozen forward/head training及16sample ranking全费，不授通用numeric知识。5分具体差额深入；Ch18 weighttying后单段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_THIRD_CORE_DECISIONS_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_RFM_RELISH_20261013.md)，日期原27双向链。

### [Omni-MMSI: Toward Identity-attributed Social Interaction Understanding `2604.00267v1`](https://arxiv.org/html/2604.00267v1)

v1§3/4.1–4.4/5.2–5.6/Tables3–6：raw audio-video身份绑定不同oraclecue，manual69profiles/ASR/声纹/ReID与reference获得权限；cue/reference共变不能因果，同reference Gemini48.72高47.04、3step34.43低2step43.06，有限socialgame不授一般社会智能。6分具体差额深入；Ch23 generation-identity绑定后单段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_SIXTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_QASK_OMNI_20261013.md)，日期原27组合闭日。

### [Benchmarking Interaction, Beyond Policy: a Reproducible Benchmark for Collaborative Instance Object Navigation `2604.00265v1`](https://arxiv.org/html/2604.00265v1)

v1§3.1–3.3/4/5.1–5.2：questioner只description/currentcandidate、oracle独有target；SR每episode decision比例/FR全部decision正确，target-last/always-no可SR高FR0。400有限episodes/六description、human小比较及实际HM3D navigation输入人口分开；SeenSynonym14.15低14.89且问数多，不采用3×/70×bundle因果/物理安全。6分具体差额深入；Ch66 Pass^k后单段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_SIXTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_QASK_OMNI_20261013.md)，日期原27双向链。

### [Dynin-Omni: Omnimodal Unified Large Diffusion Language Model `2604.00007v1`](https://arxiv.org/html/2604.00007v1)

v1§3.1/4.2/7.1/Table9及必要Table11：embedding/head旧词表行取backbone、新speech行取Stage1，其它同形weights才interpolate；保行不等保全函数，shared-row平均与fullStage1有不同取舍，text/vision部分恢复同时ASR/TTS较Stage1退。32/40H100、多stage与重训/merge全费，不授零遗忘。6分具体差额深入；Ch12 donor-row迁移后单段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_THIRD_CORE_DECISIONS_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_DYNIN_DISCO_20261013.md)，日期原27组合闭04-02。

### [Disentangling to Re-couple: Resolving the Similarity-Controllability Paradox in Subject-Driven Text-to-Image Generation `2604.00849v1`](https://arxiv.org/html/2604.00849v1)

v1§3.2–3.3/4.1/4.3：entity名给grounder/reference、pronoun给edit条件，reference-aware reward重联两路；只分离可提高identity却退prompt adherence/quality，通用IR反损subject，attention图不证明唯一因果。FLUX/200K、8H20、SAM crop、人评100pair与GRPO/grounder/VLM全费，有限DreamBench人口不授万能编辑。5分具体差额深入；Ch23 AnyID后单段/本人注root实际POST通过，见[Source](../_sources/daily-20260403/SUP_THIRD_CORE_DECISIONS_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_DYNIN_DISCO_20261013.md)，日期EXTRA配MM下界闭日。

### [Multi-Camera View Scaling for Data-Efficient Robot Imitation Learning `2604.00557v1`](https://arxiv.org/html/2604.00557v1)

v1III-B–D/IV-A–B/TablesI–IV：同步camera把同trajectory变多view样本，N×V不是fresh physical demos；camera坐标的位移/姿态增量需extrinsic旋转，base/EEF不从单结果认证本质优越。近view改善front部署而top/side可退，多camera聚合记法不统一不采精确PoE recipe，标定同步/人工作业/全部训练仍付费。6分具体差额深入；Ch26 derived-label provenance后单段/本人注actual POST通过，见[Source](../_sources/daily-20260403/SUP_EIGHTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_VIEW_OMNIVOICE_SCT_20261013.md)，日期原27双向链。

### [OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models `2604.00688v1`](https://arxiv.org/html/2604.00688v1)

v1 2.1.1–2.1.2/3/4.1/4.3/Tables5–8：8codebook各time entry mask、同time embeddings聚合/独立heads、全部masked entry loss；不是codebook独立或取消推理顺序。Qwen3-.6B ARinit转bidirectional仍适配，Emilia同300K更新不能认证同compute；Higgs codec/8H800/BF16/8192pack、32step+CFG仍全费。600语言训练非全测，生成WER低GT不能认证听感超越。6分具体差额深入；Ch24 masked generation开篇后单段/本人注actual POST通过，见[Source](../_sources/daily-20260403/SUP_EIGHTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_VIEW_OMNIVOICE_SCT_20261013.md)，日期[EXTRA6](../_sources/daily-20260403/SUP_DATACITE_BOUNDS_EXTRA6_20261013.json)配MM下界。

### [Spectral Compact Training: Pre-Training Large Language Models via Permanent Truncated SVD and Stiefel QR Retraction `2604.00733v1`](https://arxiv.org/html/2604.00733v1)

v1§3/Alg1/4.1–4.4/5：permanent Udiag(s)V参数化加QR的精确梯度非densegradient或免BP；70B-class只是无softmax/mask简化attention单step，不能称8GB完整70B LM训练。1.7B只替MLP/A10040G/Alpaca2000steps/b4，denseLR2e−5与SCT5e−4未匹配，PPL65.6–86.9 vs3.6反退；QR约40–50%mockstep与全部费用保留。5分headline纠错深入；Ch30 LoRA低秩增量开篇后单段/本人注actual POST通过，见[Source](../_sources/daily-20260403/SUP_EIGHTH_CORE_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_VIEW_OMNIVOICE_SCT_20261013.md)，日期EXTRA6组合闭日。

### [EgoSim: Egocentric World Simulator for Embodied Interaction Generation `2604.01001v1`](https://arxiv.org/html/2604.01001v1)

v1§3.2–3.3/5.1/5.3–5.5/Table2/必要fusion appendix：generated-frame重建、interactive mask/last-frame对象替换静态背景，再Sim3/TSDF保存下一render状态；非现实truth、去filter ghosting非永久证明。EgoDex/EgoVid各100test、8H200/Wan14B、20task two-clips共121frame，continuous Depth/Cam/PSNR较single退，遮挡/pose及重建tracking/fusion/generation全费；未visualpass。6分具体差额深入；Ch25真实关节提议后单段/本人注actual POST通过，见[Source](../_sources/daily-20260403/SUP_THIRD_CORE_DECISIONS_20261013.md)、[PRE/POST](../_sources/daily-20260403/SUP_BOOKS_PRE_EGOSIM_20261013.md)，日期EXTRA1001配MM下界。

## 5. 缺口与下一步

**本轮仍可执行：** 有限集合作者必要core已到具体停点，余项实际独核、Source通过者具体Books/PRE与最终DAY/完成态回读继续。现正式新增35个家族＝31实际Books、RSP/OCR两仅报告、CircuitProbe/TAC两中心争议；具体出口已独核，不把原62历史闭环当本轮完成，也不将其余普通事项标HOLD。具体层次/下一单项见[当前停点](../_sources/daily-20260403/SUP_ADMISSION_20261013.md)、[余项题摘归并](../_sources/daily-20260403/SUP_REMAINING_AB_20261013.md)、[最后必要core停点](../_sources/daily-20260403/SUP_ELEVENTH_CORE_20261013.md)。以下精确外部保留项不用于正面证据或完整覆盖断言，恢复只定点本窗。

**本窗终态保留项：**

- [MiCP `2604.01413v1`](https://arxiv.org/pdf/2604.01413v1)：§4.3 的 NE 分位数、§4.5 的频率阈值和 §4.6 的停止条件缺明确转换。已审材料不足以确认中心形式保证，不入 Books、不支持事实正确性；仅请求作者勘误或能解释该阈值的精确校准实现，取得后只重开该 family。
- [CircuitProbe `2604.00716v1`](https://arxiv.org/html/2604.00716v1)：中心定位索引/预测与验证块不一致；请求精确index约定及对应表，当前5分争议保留、不入Books。
- [Truth-Aligned Uncertainty `2604.00445v1`](https://arxiv.org/html/2604.00445v1)：strict-AUC/any-real-S的ties条件未闭合；只请求精确条件或勘误，不自修定理，当前5分争议保留、不入Books。
- [SafeReAct `2604.00012v1`](https://arxiv.org/html/2604.00012v1)：已发现更早NeurIPS2025同title/authors正式全文，Apr02不能认证首次公开；精确最早自然日未恢复，不在本补窗新评分/Books。root实际反证日期出口已核，403不当空结果，不扩2025或revision史，具体原证见[安全日期出口](../_sources/daily-20260403/SUP_CORE_SECOND_B_20261013.md)。
- [QUEST `2604.00199v1`](https://arxiv.org/abs/2604.00199v1)：明确较早ICLR正式全文线索但其精确首公开日未恢复，当前不据Apr02 arXiv写新首发行；只定点日期恢复，不扩全年。

- [OpenAI Research](https://openai.com/research/)：当前历史 `Load more` 未取得本窗研究目录。News RSS 已读，但不替代 Research。需要官方可定位分页接口或本窗目录快照；得到后仅补该源本窗、先去重，再判断新增贡献。现不据此称 OpenAI 无研究。
- [Google Research Publications](https://research.google/pubs/?year=2026)：年份筛选不等于首次公开时窗，缺可定位原始公开日期的窗口索引/存档。替代材料应能标明论文或原始研究事件的首次公开时间；得到后只重开相关记录。
- [Meta Research](https://ai.meta.com/research/)：必要历史列表正文不可提取，定点官方检索未恢复本窗日期停点。需要有原始日期的官网列表/API/快照，不能用搜索零命中或空响应支持零发布。
- Google 的 [Evaluating alignment of behavioral dispositions](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/)：月归档仅给 04-03 自然日期，未确认是否在 09:00 截点前。原论文已属旧 `2602.11328` 家族，不重复评分；博客独立事件需原始时戳及与旧材料不同的实际新增主张。日期证据到达后只恢复此事件，不重扫全年目录。
- Anthropic RSP/Roadmap原09:00截点的日期请求已由本轮04-02自然日版本处理覆盖：新增单family两事件、5分仅报告、root必要原证独核通过，不再追精确时刻；后版目标不回填。仅恢复这个日级问题，不改原62日期。
- [MiniMax Agent Tech Blog](https://agent.minimax.io/docs/techblog)：补充入口未给可恢复的历史日期停点，主中/英文博客的跨窗停点不能证明这套补充文章全部已覆盖。仅请求本窗新增文章的带日期目录/快照，取得后定点补查。
- [MiMo Blog](https://mimo.xiaomi.com/)：实际15个Blog标题未含日期，/blog仅旧Dec16页，8个Papers的有界日期不能认证全部Blog。仅请求本窗Blog带原日期列表/快照，不扩全年；此历史入口限制不代替普通候选工作。

Anthropic emotion 的本窗官方文章已标准审阅；约 41.8 MB 的长技术报告未作为已读证据，也不将后发 04-09 arXiv 机制倒灌。当窗采用范围仅限已读官方文章，这不是待把整份长报告读完才允许采用的要求。

**不属于本窗的恢复线索：** 旧五项 `.02442/.02473/.02478/.02522/.02556` 不能因较早 submitted/DOI-created 归给 04-03；留给实际首次公告 owner，未在本日评分或当作已审重复。它们不阻塞本日。

## 6. 复核

复核者：`/root`（本补窗作者`supp_apr03_20261013`；root已实际首批/第二批准入、日期及单篇必要Source/Books PRE/POST，其它未验层不冒称通过）。
结论：本轮日级待复核

本轮35个正式新增家族的具体回执见各SUP_CORE/THIRD～SEVENTH及SUP_BOOKS_PRE逐项packet；31项实际Books窄锁均已root真实POST后释放，两新增中心争议/日期已root实际核。Ch43误拟归属已在PRE修正且从未写入；其它普通可执行层未由这些回执继承通过。报告结构与限定diff检查只证明接口一致性。原62候选行/评分/日期与连续原§4保持，不自计DAY或完成态。

**原轮归档复核（不代替本轮）：** root原作者apr03的62项原轮复核结论为通过，下面原轮叙述保留；本补窗仍进行中。

独立检查覆盖 14 源的实际入口/停点与隔离范围、相邻公告批次和具体版本构成的日期推定链、62 项准入与必要证据、47 整合/14 具体已有覆盖/1 争议的处置对账。复用本轮已独立核实且未变化的单篇结果，不无差别重读附件。否定侧按来源、主题和共同理由分层抽检，发现“小规模/无新 owner/已有主题”误排后定点扩查并恢复具体家族；范围和过程在审阅记录中保留，不声称全部 raw 均独立全文审阅。47 项实际整合均可在对应 owner 章节机制正文中定位，且位于主 Review notes 之前；最后 HGRD 的关系约束分支亦已核原文 §6–7 并写后复核。MiCP 与外部目录/日期限制隔离完整，不支持采用或零遗漏。V3 格式、链接、评分/集合一致性及限定范围 `git diff --check` 通过；机器结果不替代上述语义判断。
