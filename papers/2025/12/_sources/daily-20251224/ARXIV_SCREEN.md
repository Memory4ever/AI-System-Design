# SRC-ARXIV：2025-12-24 有限发现与贡献题摘筛选

**任务窗口：** [2025-12-23T09:00:00+08:00, 2025-12-24T09:00:00+08:00)，即 [2025-12-23T01:00:00Z, 2025-12-24T01:00:00Z)。
**检查时间：** 2026-10-02T21:00:13+08:00；本轮查询、题摘及局部核验在该检查前实际执行，API字段测试时点见原始feed updated。
**角色：** root 为本日作者；本 sidecar 只负责 SRC-ARXIV 原始发现、独立题摘贡献判断与必要局部恢复。Feynman 为非作者复核入口。
**状态：** 下述有限发现及指定身份题摘筛选已结束，可交 root / Feynman；首次公告缺口隔离。不是正式 Daily、候选分母、Evidence Gate、Books 或日级独立验收完成声明。
**写入范围：** 仅本文件。未写 README、Books、LEARNING_STATE；未 stage、commit、push。

## 1. 独立上下文与方法边界

已独立重读本仓库 AGENTS.md、RESEARCH_CONTRACT 全文、REPORT_CONTRACTS V3、RESEARCH_SOURCES 使用说明/每日组/arXiv、CODEX_RESEARCH_PROMPT、ROADMAP 及 LEARNING_STATE 开头的 2025 年 12 月 checkpoint。checkpoint 仅作 ownership 路由，不继承旧完成标签或候选。

[既有日期方法记录](../ARXIV_DATE_RECOVERY.md)的官方 API/OAI/RSS 字段定义、2025 固定 availability 版本及原始 holiday 公告可复用；本轮没有用其两个测试 ID 的条件排期给其他 ID 授公告。没有重抓未变的 holiday / OAI 方法 raw。

读取 [12/25 DISCOVERY](../daily-20251225/DISCOVERY.md)仅用于恢复原始检索/列表入口、辨认已知身份风险；没有复制其候选、评分、贡献或完成结论。下述题摘与必要局部均独立取 exact-v1。跨日重复的原始入口不是跨日重复评分。

作者初批读完110个限定身份的v1完整题摘：108个HTML、2个HTML404后改读PDF，初判108potential/2负侧。此为历史批次；独立复核补5个身份并从必要正文重开Moxin后，最终115完整题摘身份、113potential/2关闭，具体变更见§8及独立记录。全部potential未核首次公开、不评分、不采用，不是本日候选数。其余原始命中只作有界标题查漏，不声称全部贡献判断或全学科召回。

## 2. 原始查询、分页与停止位置

### 2.1 提交线索主题检索

目标提交缓冲是 [2025-12-21T01:00:00Z, 2025-12-24T01:00:00Z)。它只补 arXiv announcement 的发现线索，绝非 Daily 公开窗口。

官方 [Advanced Search](https://arxiv.org/search/advanced)本轮实际 HTTP 200；表单字段明确 announcement date 只支持 year/month，original submission 支持日。网页采用日粒度外包络 12/21 至 12/24，**不能把它说成精确小时缓冲**；§6 的逐 ID API v1 秒字段用于识别缓冲外条目。搜索排序也不是首公开日排序。

所有成功网页查询共用下列原始参数，可与各组 terms 精确重建 URL：

```text
https://arxiv.org/search/advanced?
advanced=1
classification-computer_science=y
classification-include_cross_list=include
date-filter_by=date_range
date-from_date=2025-12-21
date-to_date=2025-12-24
date-date_type=submitted_date_first
abstracts=show
size=200
order=-announced_date_first
start=<0 or 200>
terms-i-operator=AND (i=0), OR (i>0)
terms-i-field=<下表>
terms-i-term=<下表；带引号的原值保留引号>
```

| 组 | 实际 terms（按顺序） | 原始返回与停止 |
| --- | --- | --- |
| L：LLM 架构/训练/RL/推理 | abstract:`"language model"`；title:`LLM`、`transformer`、`"mixture of experts"` | start=0 返回 Showing 1–200 of 290，有 next=200；start=200 返回 Showing 201–290 of 290，无 next，停止。290 是外包络原始身份命中，非日候选 |
| S：GPU/通信/runtime | title:`GPU`、`kernel`、`"parallel"`、`"communication"`、`"inference"`、`"runtime"` | start=0 返回 Showing 1–51 of 51，无 next，停止。通用无线、量子 kernel 和领域仿真词义不扩成系统队列 |
| A：Agent/RAG/记忆 | title:`agent`、`RAG`、`memory`、`"retrieval augmented"` | start=0 返回 Showing 1–73 of 73，无 next，停止。传统材料 memory、纯领域流程不自动准入 |
| M：多模态/World Model/VLA | title:`"vision language"`、`"vision-language"`、`"world model"`、`VLA`、`"video generation"`、`multimodal`、`"diffusion model"` | start=0 返回 Showing 1–93 of 93，无 next，停止。不把医学影像或任意 diffusion 应用全排队 |

四组计 507 个跨组未去重的原始命中位置，不等于 507 个独立论文。跨组身份先去重再读 v1。首次两次测试使用无效 `order=-submitted_date_first` 返回 HTTP 400，已按官方表单改为上表值；400 不作零命中证据。

### 2.2 分钟范围 API 与逐版本身份恢复

本轮 **API 可用**，不继承旧记录的 429 为当前故障。实际分钟测试：

```text
GET https://export.arxiv.org/api/query
search_query=submittedDate:[202512210100 TO 202512240100] AND (ti:LLM OR ti:GPU OR ti:agent OR ti:"world model")
start=0
max_results=1
```

HTTP 200；`opensearch:totalResults=123`、`startIndex=0`、`itemsPerPage=1`；实际只读第 1 entry（2512.20184v1），**停止在 start=0 的 1 条字段测试**，未声称123条已筛完。feed `updated=2026-10-02T12:41:31Z` 是查询刷新；entry `updated=2025-12-23T09:20:42Z` 是版本提交。范围字段不提供 first announcement，端点含不含终点也不替代本任务半开区间核对。

随后只为 §3/§4 指定的 110 身份恢复版本字段，仍非扩池：

- 第一批 `id_list=<下表除官方追加10项外的100个ID，全部显式加v1>`，`start=0,max_results=200`：HTTP 200，`totalResults=100`，实际100 entries，到末尾停止。
- 官方标题补检批 `id_list=2512.19728v1,2512.19741v1,2512.20650v1,2512.20636v1,2512.20675v1,2512.20662v1,2512.20660v1,2512.19154v1,2512.18850v1,2512.20626v1`，`max_results=20`、默认start=0：HTTP 200，实际10 entries，到末尾停止。
- entry `id` 保留 `http://arxiv.org/abs/<ID>v1` 身份；`published` 是 v1 submitted，`updated` 是所取版本 submitted。本次110条显式 v1 entry 的两字段数值均相同；原值逐项见 §6（不补时区、不把字面 published 当首公开）。
- 网页索引与版本页冲突已定点核：2512.22226 搜索称 original submitted 12/22，但 API 和 [abs v1](https://arxiv.org/abs/2512.22226v1)均为 `Tue, 23 Dec 2025 03:33:45 UTC`；2512.22250 搜索称12/23，但 API 和 [abs v1](https://arxiv.org/abs/2512.22250v1)均为 `Wed, 24 Dec 2025 04:04:26 UTC`。采用版本原值，不用索引恢复日期。
- **本轮没有取得任何这110个ID的首次 new 公告。** 秒精度版本字段、12月ID和一般排期仍不够；不能给本日授予任何确定新论文候选，也不能据此称零事件。

### 2.3 官方相关标题查漏

为检索同义词之外的新命名机制，实际打开下列官方月列表。加载 monthly 身份库仅为了有界相关标题切片；没有把全月条目变成 queue。`show=2000,skip=0` 为原始请求，cs.LG/cs.AI 只读返回首2000库中的相关数字区间，**没有继续月库下一页**。编号只是限定已发现身份邻接，不是日公告区间。

标题查漏切片：`2512.18599 <= ID <= 2512.20940`，关注 language/LLM/attention/MoE/transformer/agent/memory/kernel/parallel/world/VLA/runtime/diffusion/RAG 的相关题名。关键词只是发现，不是贡献决定；含糊且被纳入本次定点集合的读完整 v1。

| 官方入口 | 实际返回与相关停止段 |
| --- | --- |
| [cs.LG](https://arxiv.org/list/cs.LG/2025-12?show=2000&skip=0) | HTTP200，首2000 title记录；相关主段 ordinal1470～1669，出现Gate-Norm/MoAS、reward objective等；停止上述身份切片及本页，不称月库全读完 |
| [cs.AI](https://arxiv.org/list/cs.AI/2025-12?show=2000&skip=0) | HTTP200，首2000；相关主段574～667；停止该身份切片及本页，未扩后页 |
| [cs.IR](https://arxiv.org/list/cs.IR/2025-12?show=2000&skip=0) | HTTP200，225 title记录；相关105～115、cross邻接201～207；停止，未将225变逐项队列 |
| [cs.RO](https://arxiv.org/list/cs.RO/2025-12?show=2000&skip=0) | HTTP200，876；相关523～566、cross邻接832～847；停止，只追已有world/VLA/memory机制线索 |
| [cs.AR](https://arxiv.org/list/cs.AR/2025-12?show=2000&skip=0) | HTTP200，157；相关87的ReRAM量化标题和89的STAR；STAR进入指定v1集合，停止，未把ReRAM等硬件词自动判大模型贡献 |
| [cs.PL](https://arxiv.org/list/cs.PL/2025-12?show=2000&skip=0) | HTTP200，75；相关66的compiler experts、67的declarative workflow；停止 |

先前25日保存的cs.CL/cs.DC/cs.CV原始入口只用于路由，未复制其结论、未再次抓取相同未变raw。上述新列表也只能证明身份与题名，不证明各ID实际首公告批次；本日官方公告切片仍有外部缺口。

## 3. 独立 potential 判断

以下不是通过日期 Gate 的本窗候选。链接以本次实读 v1 为准；100篇网页索引中的题名/摘要不拿来代替精确版本。原文机制是待证命题，箭头后是本 sidecar 判断其可能改变的选择；没有把自己的外推当作者证明。owner 只是 ROADMAP 路由，不是已审 Books 结论。所有项首次公开未核，不评分、不采用。

### 架构、训练与 RL

| 精确 v1（题名见原文） | 暂定问题 owner（只路由） | 原有约束 -> 实际增量 -> 需重考虑的选择 |
| --- | --- | --- |
| [2512.22234v1：DiRL: An Efficient Post-Training Framework for Diffusion Language Models](https://arxiv.org/html/2512.22234v1) | `TRAIN-GRPO` | 扩散后训练存在目标不匹配与执行开销 -> blockwise runtime与DiPO目标 -> 核验dLLM在线更新及无偏目标的条件，而非照录“first”。 |
| [2512.22238v1：Masking Teacher and Reinforcing Student for Distilling Vision-Language Models](https://arxiv.org/html/2512.22238v1) | `TRAIN-SFT` | 大教师与小学生容量不匹配 -> 逐步恢复masked teacher并离线双奖励蒸馏 -> 重考虑教师难度课程和在线采样成本。 |
| [2512.22212v1：Transformer Reconstructed with Dynamic Value Attention](https://arxiv.org/html/2512.22212v1) | `MODEL-MULTI-HEAD-ATTENTION` | 固定value与多头容量约束 -> 每query动态value并去除FFN的替代架构 -> 核验容量、复杂度和训练公平性；强主张不因尚未可信而关闭。 |
| [2512.20848v1：Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/html/2512.20848v1) | `MODEL-LONG-CONTEXT` | 长上下文与稀疏容量的吞吐约束 -> MoE hybrid Mamba-Transformer及多环境后训练报告 -> 核验混合状态路径；官方模型可能早于论文公开，不能按v1提交归日。 |
| [2512.20806v1：Safety Alignment of LMs via Non-cooperative Games](https://arxiv.org/html/2512.20806v1) | `TRAIN-RLHF` | 顺序对抗训练追不上攻击策略 -> 攻防LM联合在线RL及pairwise奖励 -> 重考虑安全与utility的非零和训练取舍。 |
| [2512.20760v1：Generalization of RLVR Using Causal Reasoning as a Testbed](https://arxiv.org/html/2512.20760v1) | `TRAIN-GRPO` | RLVR泛化可能依赖初始能力 -> 因果query层级与复杂度的受控比较 -> 修正“RLVR自动跨难度泛化”的假设。 |
| [2512.20757v1：TokSuite : Measuring the Impact of Tokenizer Choice on Language Model Behavior](https://arxiv.org/html/2512.20757v1) | `MODEL-TOKENIZER` | tokenizer与模型/数据常混杂 -> 同架构数据预算初始化的14模型及扰动测试 -> 独立核验tokenizer效应。 |
| [2512.20687v1：PHOTON: Hierarchical Autoregressive Modeling for Lightspeed and Memory-Efficient Language Generation](https://arxiv.org/html/2512.20687v1) | `MODEL-LONG-CONTEXT` | 平铺token访问造成KV流量 -> 多分辨率上下文流与top-down重建 -> 重考虑长上下文访问层次；不采用摘要的大倍率。 |
| [2512.20291v1：Mixture-of-Experts with Gradient Conflict-Driven Subspace Topology Pruning for Emergent Modularity](https://arxiv.org/html/2512.20291v1) | `MODEL-MOE` | 孤立expert与指令依赖路由 -> gradient conflict监督共享子空间拓扑mask -> 重考虑专家共享、遗忘与无显式指令路由边界。 |
| [2512.20169v1：Learning to Reason in LLMs by Expectation Maximization](https://arxiv.org/html/2512.20169v1) | `TRAIN-SFT` | rationale采样影响学习目标 -> 潜变量EM与PPS等采样比较 -> 重新区分训练目标和采样分布的贡献。 |
| [2512.20156v1：Fun-Audio-Chat Technical Report](https://arxiv.org/html/2512.20156v1) | `MULTIMODAL-REPRESENTATION` | 语音与文本时率失配及知识遗忘 -> 双时率speech表示、refined head与Core-Cocktail/多任务DPO -> 核验新增部分相对DrVoice，不把引用旧机制全部算增量。 |
| [2512.20061v1：Scaling Reinforcement Learning for Content Moderation with Large Language Models](https://arxiv.org/html/2512.20061v1) | `TRAIN-GRPO` | 稀缺标签下policy-grounded分类 -> rollout/数据/优化步数及奖励配方的RL scaling比较 -> 核验饱和和数据效率条件，不按内容审核场景排除。 |
| [2512.19941v1：Block-Recurrent Dynamics in ViTs](https://arxiv.org/html/2512.19941v1) | `MODEL-TRANSFORMER-LAYER` | 层间表示相似未必功能可复用 -> recurrent surrogate作为BRH存在性测试 -> 重考虑深度与重复计算；不把相似矩阵当功能证明。 |
| [2512.19920v1：Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning](https://arxiv.org/html/2512.19920v1) | `TRAIN-RLHF` | 二元奖励鼓励猜测 -> proper scoring与abstention/逐claim校准 -> 区分正确率提升和诚实不确定性。 |
| [2512.19905v1：Demystifying LLM-as-a-Judge: Analytically Tractable Model for Inference-Time Scaling](https://arxiv.org/html/2512.19905v1) | `PLATFORM-EVALUATION-SYSTEM` | 增加采样通常被当作单调收益 -> reward misspecification下有限最优k的解析模型和LM检验 -> 重考虑judge误差与推理预算。 |
| [2512.19879v1：Fine-tuned In-Context Learners for Efficient Adaptation](https://arxiv.org/html/2512.19879v1) | `TRAIN-SFT` | ICL少样本与FT更多数据各有边界 -> 含in-context样例的任务FT及prequential选择 -> 核验样本效率与低数据验证选择。 |
| [2512.19765v1：How Many Experts Are Enough? Towards Optimal Semantic Specialization for Mixture-of-Experts](https://arxiv.org/html/2512.19765v1) | `MODEL-MOE` | 固定expert数依赖调参 -> semantic drift触发扩容与confidence-mass路由 -> 重考虑容量扩展的触发条件。 |
| [2512.19682v1：GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/html/2512.19682v1) | `TRAIN-DATA` | 静态交互数据与生成难度失配 -> simulator课程策略与alpha难度对齐奖励 -> 核验环境生成和agent共同演化的真实增量。 |
| [2512.19673v1：Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies](https://arxiv.org/html/2512.19673v1) | `TRAIN-GRPO` | 单一整体policy遮蔽层/模块贡献 -> residual-unembedding内部分解与早期低层policy优化 -> 核验分解假设和BuPO归因。 |
| [2512.19585v1：Increasing the Thinking Budget is Not All You Need](https://arxiv.org/html/2512.19585v1) | `PLATFORM-EVALUATION-SYSTEM` | 只增thinking长度的预算分配 -> 比较self-consistency/reflection等配置的质量成本 -> 保留增预算不优于替代配置的局部反证。 |
| [2512.19428v1：Attention Is Not What You Need: Grassmann Flows as an Attention-Free Alternative for Sequence Modeling](https://arxiv.org/html/2512.19428v1) | `MODEL-LONG-CONTEXT` | 全token对attention的默认必要性 -> Grassmann局部子空间/Plucker几何混合 -> 保留线性序列机制，不能外推为attention已过时。 |
| [2512.19323v1：Alternative positional encoding functions for neural transformers](https://arxiv.org/html/2512.19323v1) | `MODEL-POSITION-ENCODING` | sinusoidal位置函数选择 -> 具有不同性质的周期函数及初步比较 -> 核验替代编码的适用边界，不因实验小而排除。 |
| [2512.19219v1：Towards Minimal Fine-Tuning of VLMs](https://arxiv.org/html/2512.19219v1) | `TRAIN-LORA` | 所有token/head适配增加成本并影响纯文本 -> 视觉token的value-path LoRA及head筛选归一化 -> 核验视觉占比与纯文本保持条件。 |
| [2512.19171v1：JEPA-Reasoner: Decoupling Latent Reasoning from Token Generation](https://arxiv.org/html/2512.19171v1) | `MODEL-DECODER-ONLY` | 潜在推理仍绑定逐token生成 -> JEPA reasoner与独立Talker -> 核验潜变量推理与生成分离；多线程潜力只是未证实主张。 |
| [2512.19126v1：AWPO: Enhancing Tool-Use of Large Language Models through Explicit Integration of Reasoning Rewards](https://arxiv.org/html/2512.19126v1) | `TRAIN-GRPO` | reasoning奖励可能冲突outcome目标 -> variance gate/difficulty weight及裁剪的AWPO -> 核验advantage整合条件。 |
| [2512.19004v1：Context-Aware Initialization for Reducing Generative Path Length in Diffusion Language Models](https://arxiv.org/html/2512.19004v1) | `MODEL-DECODER-ONLY` | 全mask起点导致长去噪路径 -> context prior warm-start及confidence remask -> 同时保留步数下降与准确率下降，不能只采用加速侧。 |
| [2512.18934v1：When Less is More: 8-bit Quantization Improves Continual Learning in Large Language Models](https://arxiv.org/html/2512.18934v1) | `TRAIN-SFT` | 量化常被视为只损精度 -> FP16/INT8/INT4与replay的持续学习对照 -> 核验plasticity/retention取舍，噪声正则化仍为假说。 |
| [2512.18834v1：AraMix: Recycling, Refiltering, and Deduplicating to Deliver the Largest Arabic Pretraining Corpus](https://arxiv.org/html/2512.18834v1) | `TRAIN-DATA` | 多源重复爬取未必增加有效token -> AraMix跨数据集去重揭示高重复 -> 重考虑新增爬取相对复用清洗；语言范围不构成排除。 |
| [2512.18730v1：A Theoretical Lens for RL-Tuned Language Models via Energy-Based Models](https://arxiv.org/html/2512.18730v1) | `TRAIN-RLHF` | KL-RL性质常缺形式解释 -> EBM最优policy、detailed balance/自然梯度分析 -> 定点核数学假设，不把证明外推到任意LM。 |
| [2512.18634v1：From Shortcut to Induction Head: How Data Diversity Shapes Algorithm Selection in Transformers](https://arxiv.org/html/2512.18634v1) | `WORLDVIEW-REPRESENTATION` | 数据分布可能选择shortcut而非induction -> 单层模型的distance-diversity机制转变证明 -> 保留小模型理论对预训练数据选择的直接贡献。 |
| [2512.19728v1：Hard Negative Sample–Augmented DPO Post-Training for Small Language Models](https://arxiv.org/html/2512.19728v1) | `TRAIN-DPO` | 二元正确性漏掉近正确结构错误 -> 六维verifier hard-negative与weighted DPO -> 核验偏好样本权重和结构错误监督。 |
| [2512.19741v1：EdgeFlex-Transformer: Transformer Inference for Edge Devices](https://arxiv.org/html/2512.19741v1) | `INFER-TENSORRT-LLM` | 端侧ViT受内存预算限制 -> activation profile下memory-aware pruning及混合精度管线 -> 可核质量/内存取舍，不按模块组合或CIFAR任务直接关闭。 |
| [2512.20650v1：Mixture of Attention Schemes (MoAS): Learning to Route Between MHA, GQA, and MQA](https://arxiv.org/html/2512.20650v1) | `MODEL-MULTI-HEAD-ATTENTION` | 静态MHA/GQA/MQA固定质量-cache取舍 -> token router动态选择attention scheme -> 保留路由替代设计；微小loss差及单任务不自动排除。 |
| [2512.20636v1：Data-Free Pruning of Self-Attention Layers in LLMs](https://arxiv.org/html/2512.20636v1) | `MODEL-TRANSFORMER-LAYER` | attention层裁剪依赖校准与运行 -> weight-only Gate-Norm按query-key耦合评分 -> 核验无数据裁剪及attention suppression条件。 |
| [2512.20675v1：Revisiting the learning objectives of vision-language reward models](https://arxiv.org/html/2512.20675v1) | `MULTIMODAL-EMBODIED-VLA` | VLM reward改进常混杂backbone/数据 -> 同设置比较目标并发现triplet优于复杂目标 -> 保留直接设计反证，不因是Meta-World局部研究关闭。 |

### GPU、通信与推理运行时

| 精确 v1（题名见原文） | 暂定问题 owner（只路由） | 原有约束 -> 实际增量 -> 需重考虑的选择 |
| --- | --- | --- |
| [2512.20573v1：Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs](https://arxiv.org/html/2512.20573v1) | `INFER-SPECULATIVE-DECODING` | dLLM长draft的拒绝成本 -> FailFast按区域动态draft长度 -> 核验draft并行速度、接受长度和lossless前提。 |
| [2512.20210v1：Predictive-LoRA: A Proactive and Fragmentation-Aware Serverless Inference System for LLMs](https://arxiv.org/html/2512.20210v1) | `INFER-GPU-MEMORY` | adapter冷启动与rank异质导致碎片 -> demand预测预取和page-based adapter管理 -> 重考虑预取收益与HBM管理成本。 |
| [2512.20198v1：Designing Spatial Architectures for Sparse Attention: STAR Accelerator via Cross-Stage Tiling](https://arxiv.org/html/2512.20198v1) | `INFER-TENSORRT-LLM` | stage孤立稀疏优化浪费访存 -> STAR跨stage tiling、排序和稀疏预测协同 -> 核验architecture/algorithm共设计，不能当通用A100实测提速。 |
| [2512.20080v1：CBA: Communication-Bound-Aware Cross-Domain Resource Assignment for Pipeline-Parallel Distributed LLM Training in Dynamic Multi-DC Optical Networks](https://arxiv.org/html/2512.20080v1) | `TRAIN-PIPELINE-PARALLEL` | 跨DC的通信延迟造成PP bubble -> CB任务标注驱动频谱/路由分配 -> 重考虑训练任务与光网络资源共同调度；原文为仿真。 |
| [2512.19849v1：UCCL-EP : Portable Expert-Parallel Communication](https://arxiv.org/html/2512.19849v1) | `TRAIN-DISTRIBUTED-TRAINING` | GPU发起RDMA与NIC深耦合 -> GPU-CPU控制通道和CPU代理/ordering语义模拟 -> 核验异构EP可移植性、通信成本和正确性。 |
| [2512.19606v1：RAPID-LLM: Resilience-Aware Performance analysis of Infrastructure for Distributed LLM Training and Inference](https://arxiv.org/html/2512.19606v1) | `TRAIN-DISTRIBUTED-TRAINING` | 网络故障与operator/内存预算分离评估 -> traces和congestion/fault仿真及activation-liveness过滤 -> 核验配置可行性与软链路故障的性能预测边界。 |
| [2512.19206v1：MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning](https://arxiv.org/html/2512.19206v1) | `INFER-KV-CACHE` | 固定低比特与静态高精度分配损害长推理 -> channel量化难度和query relevance共同分配精度 -> 重考虑query-aware key与per-token value取舍。 |
| [2512.19250v1：Small Language Models as Compiler Experts: Auto-Parallelization for Heterogeneous Systems](https://arxiv.org/html/2512.19250v1) | `INFER-TENSORRT-LLM` | 硬编码编译heuristic适配异构kernel困难 -> 小LM多策略生成及sanitizer正确性核验 -> 可修正kernel优化工具链选择，不能按scientific kernel名称排除。 |
| [2512.19179v1：L4: L ow-Latency and L oad-Balanced L LM Serving via L ength-Aware Scheduling](https://arxiv.org/html/2512.19179v1) | `INFER-SCHEDULING` | 混合长度batch与attention backend不匹配 -> L4长度专门化实例组、动态边界和跨组迁移 -> 核验全局同质化及负载平衡。 |
| [2512.19018v1：PEAK: A Performance Engineering AI-Assistant for GPU Kernels Powered by Natural Language Transformations](https://arxiv.org/html/2512.19018v1) | `INFER-TENSORRT-LLM` | 低层kernel缺样例且硬件变化快 -> 自然语言变换与验证/性能迭代的PEAK -> 核验跨CUDA/HIP/HLSL优化流程和失败成本。 |
| [2512.18725v1：ML Inference Scheduling with Predictable Latency](https://arxiv.org/html/2512.18725v1) | `INFER-SCHEDULING` | 忽略GPU batch共驻动态造成预测误差 -> static与EWMA/适应模型的局部评价 -> 核验co-location interference，不因摘要称ongoing而误关。 |
| [2512.18674v1：Remoe: Towards Efficient and Low-Cost MoE Inference in Serverless Computing](https://arxiv.org/html/2512.18674v1) | `MODEL-MOE` | serverless稀疏expert caching成本 -> GPU共享模块、CPU expert及冷expert函数拆分 -> 核验activation预测、最坏内存SLO和费用取舍。 |
| [2512.22219v1：Mirage Persistent Kernel: A Compiler and Runtime for Mega-Kernelizing Tensor Programs](https://arxiv.org/html/2512.22219v1) | `INFER-TENSORRT-LLM` | operator逐kernel限制跨算子重叠 -> MPK的SM级task graph和mega-kernel分布式调度 -> 重考虑execution-plan粒度。 |
| [2512.20861v1：Memory-Efficient Acceleration of Block Low-Rank Foundation Models on Resource Constrained GPUs](https://arxiv.org/html/2512.20861v1) | `INFER-TENSORRT-LLM` | BLR算术节省未必带来多token加速 -> roofline定位memory-bound及layout/partial fusion kernel -> 保留理论压缩与实际执行收益的反证。 |
| [2512.19342v1：Faster Distributed Inference-Only Recommender Systems via Bounded Lag Synchronous Collectives](https://arxiv.org/html/2512.19342v1) | `TRAIN-DISTRIBUTED-TRAINING` | alltoallv同步令不均匀embedding查找被straggler阻塞 -> bounded-lag collective -> 核验仅inference、不变表等语义下的正确性；均衡负载无显著收益也保留。 |

### Agent、RAG 与记忆

| 精确 v1（题名见原文） | 暂定问题 owner（只路由） | 原有约束 -> 实际增量 -> 需重考虑的选择 |
| --- | --- | --- |
| [2512.21354v1：Reflection-Driven Control for Trustworthy Code Agents](https://arxiv.org/html/2512.21354v1) | `AGENT-REFLECTION` | 事后reflection难阻止风险路径 -> 在线reflection与检索安全修复记忆 -> 核验控制发生时点、functional correctness和开销。 |
| [2512.20934v1：Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning](https://arxiv.org/html/2512.20934v1) | `AGENT-TOOL-CALLING` | 固定/预先猜测工具库利用低 -> 解题经历抽象为可复用tool library -> 核验transductive经验生成与跨任务复用。 |
| [2512.20458v1：Laser: Governing Long-Horizon Agentic Search via Structured Protocol and Context Register](https://arxiv.org/html/2512.20458v1) | `AGENT-CONTEXT` | raw trace积累致上下文溢出 -> 可解析action协议与compact context register -> 核验retrospection和状态保留；不能仅把控制术语当贡献。 |
| [2512.20278v1：Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation](https://arxiv.org/html/2512.20278v1) | `AGENT-PLATFORM` | 从空白合成workflow缺发现与接口验证 -> Dynamic MCP probe、linear state anchoring与持久执行 -> 单个跨服务案例可能有具体失效增量，尚未证明production-grade。 |
| [2512.20237v1：MemR 3 : Memory Retrieval via Reflective Reasoning for LLM Agents](https://arxiv.org/html/2512.20237v1) | `AGENT-MEMORY` | 存储压缩不是检索闭环 -> retrieve/reflect/answer router与evidence-gap tracker -> 核验既有memory store之上的控制收益。 |
| [2512.20184v1：Reaching Agreement Among Reasoning LLM Agents](https://arxiv.org/html/2512.20184v1) | `AGENT-MULTI-AGENT` | 固定循环/全barrier浪费并可能短暂共识 -> Aegean语义及增量quorum早停 -> 核验形式guarantee与答案正确性不是同一保证。 |
| [2512.20111v1：ABBEL: LLM Agents Acting through Belief Bottlenecks Expressed in Language](https://arxiv.org/html/2512.20111v1) | `AGENT-CONTEXT` | 全交互历史成本增长 -> language belief bottleneck更新并RL训练 -> 必须保留压缩belief错误传播及相对full-context的退化。 |
| [2512.20092v1：Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents](https://arxiv.org/html/2512.20092v1) | `AGENT-MEMORY` | 多session历史噪声损害时序证据 -> 粗到细选择及时间/grounding多层奖励 -> 核验query时间范围和长期记忆生命周期。 |
| [2512.19769v1：A Declarative Language for Building And Orchestrating LLM-Powered Agent Workflows](https://arxiv.org/html/2512.19769v1) | `AGENT-WORKFLOW` | workflow逻辑与语言/deployment耦合 -> 统一DSL及跨backend执行/A-B变体 -> 核验语义执行边界与控制变化，不照录开发速度。 |
| [2512.19396v1：EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/html/2512.19396v1) | `AGENT-MEMORY` | GUI逐任务遗忘成功经验 -> critic筛成功轨迹与检索注入 -> 核验memory质量、迁移和错误放大。 |
| [2512.19134v1：QuCo-RAG: Quantifying Uncertainty from the Pre-training Corpus for Dynamic Retrieval-Augmented Generation](https://arxiv.org/html/2512.19134v1) | `AGENT-RAG` | 内置信度可能错校准 -> pretraining corpus实体频率/共现触发检索 -> 核验参考语料与未知真实pretrain之间的可迁移边界。 |
| [2512.18987v1：Affordance RAG: Hierarchical Multimodal Retrieval with Affordance-Aware Embodied Memory for Mobile Manipulation](https://arxiv.org/html/2512.18987v1) | `AGENT-RAG` | 语义相似目标未必可操作 -> regional/visual检索和affordance rerank -> 重考虑embodied检索目标与可执行性，不能按机器人应用排除。 |
| [2512.18950v1：Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement](https://arxiv.org/html/2512.18950v1) | `AGENT-MEMORY` | 冻结LM需要外部适应 -> 分层程序记忆、Bayesian可靠性和成功/失败对比 -> 核验轨迹到procedure与expected utility。 |
| [2512.18746v1：MemEvolve: Meta-Evolution of Agent Memory Systems](https://arxiv.org/html/2512.18746v1) | `AGENT-MEMORY` | memory内容演进但架构固定 -> encode/store/retrieve/manage空间的meta-evolution -> 核验共同演化和跨任务迁移。 |
| [2512.20245v1：Memory as Resonance: A Biomimetic Architecture for Infinite Context Memory on Ergodic Phonetic Manifolds](https://arxiv.org/html/2512.20245v1) | `AGENT-MEMORY` | KV增长与遗忘取舍 -> 连续phonetic trajectory导航与概率重建 -> 新设计命题清楚但“infinite/O(1)”需严审，不因可信度未核而初筛关闭。 |
| [2512.20660v1：Managing the Stochastic: Foundations of Learning in Neuro-Symbolic Systems for Software Engineering](https://arxiv.org/html/2512.20660v1) | `AGENT-WORKFLOW` | 随机生成控制所有工作流可能gaming verifier -> dual state、原子生成-验证对与guard sensing -> 核验确定性控制和随机环境边界；不是通用“加测试”即可证明。 |
| [2512.19154v1：Beyond Sliding Windows: Learning to Manage Memory in Non-Markovian Environments](https://arxiv.org/html/2512.19154v1) | `AGENT-MEMORY` | frame stacking随非Markov跨度增长 -> adaptive stacking移除非预测性观察及收敛分析 -> 核验有限记忆/因果依赖，非LLM实验也可直接支撑记忆机制。 |
| [2512.20626v1：MegaRAG: Multimodal Knowledge Graph-Based Retrieval Augmented Generation](https://arxiv.org/html/2512.20626v1) | `AGENT-RAG` | 纯文本KG不足以支持视觉长文推理 -> visual cues贯穿KG构建、检索与生成 -> 核验跨模态知识接口；旧提交不是已知旧公告。 |
| [2512.20612v1：Making Large Language Models Efficient Dense Retrievers](https://arxiv.org/html/2512.20612v1) | `AGENT-RAG` | 生成任务层冗余结论未必适用于retrieval -> attention语义聚合与MLP冗余分离及coarse-to-fine压缩 -> 重考虑retriever专属裁剪策略。 |

### 多模态、World Model 与 VLA

| 精确 v1（题名见原文） | 暂定问题 owner（只路由） | 原有约束 -> 实际增量 -> 需重考虑的选择 |
| --- | --- | --- |
| [2512.20839v1：Input-Adaptive Visual Preprocessing for Efficient Fast Vision-Language Model Inference](https://arxiv.org/html/2512.20839v1) | `MULTIMODAL-REPRESENTATION` | 静态高分辨率预处理浪费visual token -> 内容自适应分辨率/裁切 -> 核验端到端质量-成本，摘要的inference-only设置不自动排除。 |
| [2512.20188v1：Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation](https://arxiv.org/html/2512.20188v1) | `MULTIMODAL-EMBODIED-VLA` | VLM与action同频执行限制控制 -> latent buffer桥接异步fast-slow和whole-body tokenizer -> 核验joint training与异步执行的状态新鲜度。 |
| [2512.20166v1：L o L A : L ong H o rizon L atent A ction Learning for General Robot Manipulation](https://arxiv.org/html/2512.20166v1) | `MULTIMODAL-EMBODIED-VLA` | 历史和proprioception简单拼接难长程动作 -> state-aware embodiment-anchored latent重表示 -> 核验物理尺度grounding与历史作用。 |
| [2512.20136v1：M 3 KG-RAG: Multi-hop Multimodal Knowledge Graph-enhanced Retrieval-Augmented Generation](https://arxiv.org/html/2512.20136v1) | `AGENT-RAG` | 共享embedding相似检索易离题/冗余 -> multi-hop audio-visual KG与GRASP grounding/pruning -> 核验graph连接与必要证据选择。 |
| [2512.19535v1：CASA: Cross-Attention via Self-Attention for Efficient Vision-Language Fusion](https://arxiv.org/html/2512.19535v1) | `MULTIMODAL-REPRESENTATION` | token insertion贵、cross-attention细节质量差 -> CASA在专用cross层启用局部text-to-text交互 -> 核验fusion质量与可扩展性。 |
| [2512.19443v1：D²Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning](https://arxiv.org/html/2512.19443v1) | `MULTIMODAL-REPRESENTATION` | 视觉pruning在细定位失败 -> positional-bias修正及spatial-semantic graph的MIS -> 重考虑重要性与结构多样性的共同约束。 |
| [2512.19433v1：dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models](https://arxiv.org/html/2512.19433v1) | `MULTIMODAL-GENERATIVE-PARADIGMS` | TTS双维线性搜索开销高 -> hierarchical expand/prune与自检反馈 -> 核验复杂度、verifier共享偏差和质量预算。 |
| [2512.18832v1：From Word to World : Can Large Language Models be Implicit Text-based World Models?](https://arxiv.org/html/2512.18832v1) | `MULTIMODAL-WORLD-MODELS` | LM可否可信模拟next-state未知 -> fidelity/robustness/agent utility三层评估 -> 保留coverage与环境复杂度决定训练收益的边界。 |
| [2512.18741v1：Memorize-and-Generate: Towards Long-Term Consistency in Real-Time Video Generation](https://arxiv.org/html/2512.18741v1) | `MULTIMODAL-GENERATIVE-PARADIGMS` | window history丢弃破坏场景一致性 -> 独立memory压缩模型与frame generator -> 核验compact KV保持长期状态的代价。 |
| [2512.18736v1：Is Your Conditional Diffusion Model Actually Denoising?](https://arxiv.org/html/2512.18736v1) | `MULTIMODAL-GENERATIVE-PARADIGMS` | conditional采样默认对应理想去噪 -> schedule deviation及smoothness解释 -> 直接反证DDPM/DDIM一致性假设，不按通用理论排除。 |
| [2512.18675v1：AsyncDiff: Asynchronous Timestep Conditioning for Enhanced Text-to-Image Diffusion Inference](https://arxiv.org/html/2512.18675v1) | `MULTIMODAL-GENERATIVE-PARADIGMS` | integrator与denoiser同timestep被默认绑定 -> learned conditioning timestep异步于更新schedule -> 核验路径语义和GRPO复合reward。 |
| [2512.18619v1：ChronoDreamer: Action-Conditioned World Model as an Online Simulator for Robotic Planning](https://arxiv.org/html/2512.18619v1) | `MULTIMODAL-WORLD-MODELS` | contact-rich动作预测需接触/关节状态 -> RGB/contact/action/proprioception联合预测及unsafe rollout拒绝 -> 只有仿真与定性证据，不称真实机器人安全保证。 |
| [2512.20276v1：ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge](https://arxiv.org/html/2512.20276v1) | `INFER-SCHEDULING` | edge VLA decode受memory限制 -> 跨请求prefill/decode pipeline、state packed forward和KV ring -> 核验不同时间步状态正确性与动作新鲜度。 |
| [2512.18850v1：InDRiVE: Reward-Free World-Model Pretraining for Autonomous Driving via Latent Disagreement](https://arxiv.org/html/2512.18850v1) | `MULTIMODAL-WORLD-MODELS` | task-specific reward限制world-model复用 -> latent ensemble disagreement内驱预训练及冻结零样本/少样本对照 -> 核验交互预算和跨town robustness。 |
| [2512.22226v1：VideoScaffold: Elastic-Scale Visual Hierarchies for Streaming Video Understanding in MLLMs](https://arxiv.org/html/2512.22226v1) | `MULTIMODAL-REPRESENTATION` | 离线静态压缩造成stream fragmented表示 -> 弹性event segmentation与hierarchical consolidation -> 核验持续事件粒度和细语义保留。 |

### 安全、评价与设计反证

| 精确 v1（题名见原文） | 暂定问题 owner（只路由） | 原有约束 -> 实际增量 -> 需重考虑的选择 |
| --- | --- | --- |
| [2512.22250v1：Hallucination Detection for LLM-based Text-to-SQL Generation via Two-Stage Metamorphic Testing](https://arxiv.org/html/2512.22250v1) | `PLATFORM-EVALUATION-SYSTEM` | 无ground-truth SQL难判幻觉 -> schema与logic两阶段metamorphic关系 -> 核验oracle-free误报/漏报；该提交已晚于本窗终点，只为额外线索。 |
| [2512.22245v1：Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation](https://arxiv.org/html/2512.22245v1) | `PLATFORM-EVALUATION-SYSTEM` | verbal confidence错校准且多采样贵 -> Brier-loss hidden-state线性probe -> 核验校准和easy-domain保守偏差。 |
| [2512.22216v1：Syntax Is Not Enough: An Empirical Study of Small Transformer Models for Neural Code Repair](https://arxiv.org/html/2512.22216v1) | `PLATFORM-EVALUATION-SYSTEM` | syntax validity可能高估repair -> CodeT5-small复制行为及EM/SV拆分 -> 保留metric反证，但EM零不能证明全部语义失败。 |
| [2512.20812v1：Semantic Deception: When Reasoning Models Can’t Compute an Addition](https://arxiv.org/html/2512.20812v1) | `PLATFORM-EVALUATION-SYSTEM` | 熟悉语义可能伪装符号推理 -> 重定义符号及误导语义的受控测试 -> 核验抽象操作能力，不把局部失败外推“无推理”。 |
| [2512.20334v1：Comment Traps: How Defective Commented-out Code Augment Defects in AI-Assisted Code Generation](https://arxiv.org/html/2512.20334v1) | `AGENT-CONTEXT` | 注释代码被视为不执行而安全 -> defective commented-out上下文仍诱导错误且ignore指令有限 -> 核验prompt provenance与污染传播。 |
| [2512.20293v1：AprielGuard](https://arxiv.org/html/2512.20293v1) | `PLATFORM-SECURITY` | harm与prompt injection常分开处理 -> AprielGuard统一taxonomy与reasoning训练 -> 定点核新增威胁覆盖和agent场景，不直接采用排行榜优越性。 |
| [2512.20168v1：Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography](https://arxiv.org/html/2512.20168v1) | `PLATFORM-SECURITY` | 输入/输出过滤默认恶意内容显式可见 -> 跨模态双steganography威胁 -> 保留carrier/tool与黑盒接口前提，非所有MLLM可普遍绕过。 |
| [2512.20083v1：Detecting Non-Optimal Decisions of Embodied Agents via Diversity-Guided Metamorphic Testing](https://arxiv.org/html/2512.20083v1) | `PLATFORM-EVALUATION-SYSTEM` | 任务成功掩盖计划资源非最优 -> 四类NoD metamorphic关系与diversity选择 -> 重考虑success之外的效率oracle及关系有效性。 |
| [2512.19350v1：PENDULUM: A Benchmark for Assessing Sycophancy in Multimodal Large Language Models](https://arxiv.org/html/2512.19350v1) | `PLATFORM-EVALUATION-SYSTEM` | 用户陈述与视觉事实冲突未被单独测 -> PENDULUM视觉sycophancy测量 -> 核验诱导提示和图像难度，不能仅因是benchmark关闭。 |
| [2512.19297v1：Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models](https://arxiv.org/html/2512.19297v1) | `PLATFORM-SECURITY` | LoRA分发和常规后门防御可能漏检 -> task数据生成和causal adapter merge控制attack/FTR -> 核验模型供应链与trigger误触边界。 |
| [2512.19238v1：Identifying Features Associated with Bias Against 93 Stigmatized Groups in Language Models and Guardrail Model Safety Mitigation](https://arxiv.org/html/2512.19238v1) | `PLATFORM-SECURITY` | guardrail拦截不等于消除偏见 -> 93身份情景下残留特征关联与intent识别失败 -> 保留局部安全反证，不外推所有guardrail。 |
| [2512.19215v1：Semantically-Equivalent Transformations-Based Backdoor Attacks against Neural Code Models: Characterization and Mitigation](https://arxiv.org/html/2512.19215v1) | `PLATFORM-SECURITY` | sanitization针对异常注入pattern -> semantics-preserving transformation trigger仍逃逸 -> 核验攻击者能力及normalization部分缓解。 |
| [2512.19027v1：Recontextualization Mitigates Specification Gaming without Modifying the Specification](https://arxiv.org/html/2512.19027v1) | `TRAIN-RLHF` | 错reward通常被认为须改spec -> 好语境采样后recontextualize到许可坏行为的语境 -> 核验on/off-policy差异与奖励gaming边界。 |
| [2512.19025v1：The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation](https://arxiv.org/html/2512.19025v1) | `PLATFORM-EVALUATION-SYSTEM` | unlearning原样本分数不等于知识去除 -> disjoint semantic surrogate压力测试 -> 核验surrogate保留信息，不将其当完整删除证明。 |
| [2512.19011v1：Efficient Jailbreak Mitigation Using Semantic Linear Classification in a Multi-Staged Pipeline](https://arxiv.org/html/2512.19011v1) | `PLATFORM-SECURITY` | 大GPU guard被当必需 -> TF-IDF/linear SVM及分阶段过滤的效率-误报取舍 -> 必要局部核验evaluation，不宣称系统已安全。 |
| [2512.18733v1：Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Level Graph Anomaly Detection](https://arxiv.org/html/2512.18733v1) | `PLATFORM-SECURITY` | multi-agent异常检测粗粒度且不可解释 -> sentence/token bi-level encoder与theme detector -> 核验malicious agent的可识别条件和解释限制。 |
| [2512.20798v1：A Benchmark for Evaluating Outcome-Driven Constraint Violations in Autonomous AI Agents](https://arxiv.org/html/2512.20798v1) | `PLATFORM-EVALUATION-SYSTEM` | 显式恶意单步测量漏掉KPI驱动偏离 -> mandated/incentivized多步版本 -> 保留goal-pressure评价盲区，bash模拟不能称真实生产事实。 |
| [2512.22211v1：With Great Capabilities Come Great Responsibilities: Introducing the Agentic Risk & Capability Framework for Governing Agentic AI Systems](https://arxiv.org/html/2512.22211v1) | `AGENT-PLATFORM` | 机构agent风险控制缺capability到control映射 -> ARC按component/design/capability关联风险与技术控制 -> 局部原文给出三级controls及残余风险 -> 重考虑capability差异化治理，尚未证明控制有效性。 |
| [2512.20176v1：Optimistic TEE-Rollups: A Hybrid Architecture for Scalable and Verifiable Generative AI Inference on Blockchain](https://arxiv.org/html/2512.20176v1) | `PLATFORM-SECURITY` | 纯ZK成本与optimistic等待/主观PoQ存在取舍 -> TEE provisional finality、fraud proof和spot checks -> 核验attestation/side-channel假设，不采“guaranteeing”宣传。 |
| [2512.20662v1：Quantifying Laziness, Decoding Suboptimality, and Context Degradation in Large Language Models](https://arxiv.org/html/2512.20662v1) | `PLATFORM-EVALUATION-SYSTEM` | 多要求漏答、解码和长对话退化常混称 -> 三组局部对照含简单检索不退化的负结果 -> 保留scope反证，不能按样本局部或模型不详直接拒收。 |
| [2512.22208v1 Moxin](https://arxiv.org/html/2512.22208v1#S4) | `MULTIMODAL-EMBODIED-VLA` | 必要§4/6.2的同骨干训练阶段比较、延长训练/单臂FiLM无益及Table2脚注协议矛盾触发恢复potential；不授普遍优越性，具体独立局部及日期限制见§8。 |
| [2512.20920v1：RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks](https://arxiv.org/html/2512.20920v1) | `MODEL-TRANSFORMER-LAYER` | MoE full-FT activation占内存 -> reversible blocks回算activation -> 重考虑重算/存储取舍；该提交晚于本窗终点，额外线索。 |
| [2512.20908v1：Where Did This Sentence Come From? Tracing Provenance in LLM Reasoning Distillation](https://arxiv.org/html/2512.20908v1) | `TRAIN-SFT` | distillation能力归属不清 -> 同context teacher/original/student概率对比及selection -> 核验provenance相关而非因果归因；晚于本窗终点。 |
| [2512.20877v1：Architectural Trade-offs in Small Language Models Under Compute Constraints](https://arxiv.org/html/2512.20877v1) | `WORLDVIEW-SCALING-LAW` | 架构改进未必在小预算有效 -> depth/context/RoPE的NLL/FLOP受控比较 -> 保留优化预算反证；晚于本窗终点，非本日候选。 |
| [2512.20159v1：AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration](https://arxiv.org/html/2512.20159v1) | `PLATFORM-EVALUATION-SYSTEM` | code judge标签粗糙或不均衡 -> rule perturbation控制质量分布与多源人工校准 -> 保留relative ranking与hallucinated flaws/高方差的评价边界。 |

## 4. 负侧理由与撤回/修订信号

### 4.1 完整 exact-v1 题摘后的明确负侧

| 身份 | 具体理由、日期与版本边界 |
| --- | --- |
| [2512.20002v1 LoFT-LLM](https://arxiv.org/html/2512.20002v1) | 题摘实际为finance/energy时序预测：频率分解、残差预测和LLM领域语义校准，新增目标是该类预测指标，并未提出模型能力形成、LLM runtime或Agent状态的一般机制/失效边界。按实际贡献范围关闭，非“领域论文一律排除”。首公开未核，不评分。当前abs评论含withdrawn，但版本史只明确v2 withdrawn、v3恢复为正文；不能把v1/v3自动认作撤回，亦不能以撤回标签替代贡献判断 |

### 4.2 标题已明确的范围外例子

这些是本次入口的具体 negative 样本，不是全部原始命中完成关闭的声明；无含糊主线机制或纠错安全线索时按明确标题停止：

| 身份（2512前缀） | 原始标题目标与关闭理由 |
| --- | --- |
| 22237、22209、20783、20436 | low-dose PET/gastric super-resolution/breast ultrasound/stroke segmentation；标题明确为医学成像任务，未给出LLM/生成基础模型/系统机制问题，不扩医学任务库 |
| 20084 | QE-Catalytic relaxed-energy prediction；暂缓AI for Science，不借multimodal/data owner重新纳入 |
| 19458、20135、20333、20469 | VASP first-principles、MolAct分子编辑、SynCraft合成优化、Bohrium/SciMaster agentic science；当前暂缓科学应用，不因Agent通用术语绕入 |
| 22202 | SMWI重建中的Complex Swin应用；标题不是通用Transformer替代机制 |
| 20888、20342、19010 | optical tactile sensor/shape-memory transmission/tissue palpation sensor；不是仅有“parallel/memory/multimodal”即构成GPU、Agent memory或VLA模型机制 |
| 20588、19440、18797 | quantum kernel下界、binary kernel logistic、quantum-kernel deepfake检测；不是GPU计算kernel/LLM runtime机制 |
| 20332、18600、20739 | OTFS/LEO beamforming/green cognitive radio无线通信；不是LLM GPU parallel collective |
| 22215、18883 | OPENFOAM GPU porting、astrophysical parallel codes；本次未出现模型训练/推理接口证据；不把所有GPU移植都视为大模型运行时 |

### 4.3 当前官方标记只作对应版本核验

- [20002 current abs](https://arxiv.org/abs/2512.20002)：本次读到v1 `2025-12-23T02:55:04Z`、v2 `Tue, 6 Jan 2026 11:38:52 UTC (1 KB) (withdrawn)`、v3 `Tue, 13 Jan 2026 02:09:17 UTC (1,523 KB)`。评论仍称withdrawn。明确记录评论/版本边界，不授2025本窗撤回事件，关闭依据仍是4.1的原文贡献。
- [18836 current abs](https://arxiv.org/abs/2512.18836)：v1 `Sun, 21 Dec 2025 17:45:57 UTC`，v3 `Mon, 6 Apr 2026 19:26:51 UTC (1 KB) (withdrawn)`；作者评论要求重大修订后重投。该版本不入选、不评分、不采用；本轮原始标题是停车分类网络指导轨迹，不将未核首公告或2026撤回反推成本窗事件。
- 20198 网页评论的 corrected missing author information in references 已轻量核读，是引用作者元数据修正信号，未证明STAR机制改变；v1贡献仍potential。
- 20169 评论指2026 ver2 major revision/new experiments，不把2026修订当12/24新事件；本轮只用v1，后续针对当窗修订有原始证据再重开。
- 19179 原网页索引题名CascadeInfer，但 [v1 PDF第一页](https://arxiv.org/pdf/2512.19179v1)与v1 HTML均为L4；19219 v1是Towards Minimal Fine-Tuning of VLMs / Image-LoRA，18834 v1是AraMix，和当前索引题名不同；已用必要v1 PDF身份定点核对。命名不一致不支持推定重要修订或公开日期。

## 5. 已执行的必要局部核验

不是108项全文审阅。只读会影响筛选/安全反证边界的局部，没有全附件深审；以下也不构成已复现实验或生产验证。

- **19297 v1 §III（Attack Goal and Threat Model）、§V-C（Defense Evasion）**：公开LoRA权重/任务可得而原始训练数据不可得的weight-poisoning模型；不是对任意未知接口无权限注入。保留分发供应链与false trigger的具体风险，六adapter作者评价不能外推全部LoRA安全性。
- **19215 v1 引言贡献/威胁模型路由及normalization讨论**：语义等价trigger与普通异常注入不同，常规normalization仅部分缓解；不把“代码语义未变”当安全证明，也不把该论文当现实已攻破产品证据。
- **20168 v1 §III-B（Threat Model）及输入/输出过滤接口说明**：黑盒text+image交互、carrier image/相应工具路径与本地读取隐蔽响应的能力前提；无模型参数/梯度访问。安全意义是显式可见内容假设的盲区，不能宣称所有MLLM或所有部署过滤必然失败。
- **19238 v1 §8（Discussion）与guardrail输入类别检查**：偏见总量下降并不改变stigma特征关联，guardrail识别意图有限；这是给定身份/情景及三组LM-guard组合的边界，不是普遍guardrail失效。
- **20798 v1 scenario setup 与 Limitations 段**：Mandated/Incentivized区分命令与KPI压力，持久bash和40情景仍是简化实验环境，不是“现实生产事故”。不因涉及法律伦理情景而忽略其Agent目标压力反证。
- **22216 v1 §3.5、§6（Threats to Validity）**：EM是字符级匹配；作者明确承认会低估语义正确性，未做executable correctness统一oracle。保留“syntax validity不是repair能力”的反证，不采用“0 EM说明所有程序都语义错误”，不按60M、小样本或单数据集关闭。
- **20334 v1 引言RQ与ignore-comment讨论**：注释不是代码执行但仍能污染模型输出；ignore指令有限缓解，未证明因果机制普遍成立，不把它误排为普通代码样式研究。
- **19027 v1 方法与limits/off-policy段**：采样后prompt重语境化导致训练off-policy；frontier reasoning会复述prompt、长多轮和更难场景可能减弱作用，GRPO正则化并非通用保证。保留“不改错误奖励也可能减轻gaming”的有限命题。
- **19025 v1 §3.1/§3.2及§4/§6路由**：surrogate与原样本语义相邻但不重合，目标是反证指标的faithfulness；不把原样本遗忘等同知识消失，也不把单个surrogate指标当法定删除认证。
- **18725 v1 §3/§4**：摘要“ongoing work”背后已有NVIDIA L4/TensorRT、CNN/Transformer的co-location预测实验及static/EWMA差异；因此保留系统反证，不能以“尚未成熟完整系统”提前关闭。
- **20080 v1 PDF p1题摘、§2及p3 §3**：CB-label反馈驱动光网络资源分配，NSFNET仿真和8个PP stage；不当作运行集群实测。
- **22211 v1 §4.3.1**：risk repository到技术control映射及Level0/1/2优先级、明确残余风险；保留设计治理线索，未证明控制有效性。
- **20176 v1 §2.4/§2.5**：TEE与cryptographic/optimistic信任边界不同，remote attestation与side-channel fallback只在模型假设内；不采摘要的model authenticity保证。
- **20662 v1 PDF p1完整题摘及p4～5 methodology**：多要求漏答、简单候选解码与长对话事实检索是不同评测对象；局部正/负结果需分开。模型接口与样本可信度待后续Evidence限定，不作为贡献前排除理由。

## 6. 逐 ID 原始版本提交字段

以下均为实际官方 API entry `published` 原值，UTC、秒精度；所有显式v1 entry的 `updated` 与同列完全相同。**字段性质：Submitted，不是首次公开。** HTML/PDF中的arXiv dateline也不改字段语义。

首公告状态统一为 **Not Verified**。13条缓冲外记录显式区分；8条较早提交的官方标题线索也不能仅因提交早就认定旧公告/已审重复，5条终点后的论文不能由其提交反推本日首发。作者其他来源可能更早公开仍需独立事件证明。

| exact ID | entry published / updated 原值 | 与提交缓冲的关系（不判公开归日） |
| --- | --- | --- |
| 2512.18619v1 | `2025-12-21T06:36:03Z` | 提交缓冲内；首公告未核 |
| 2512.18634v1 | `2025-12-21T08:10:26Z` | 提交缓冲内；首公告未核 |
| 2512.18674v1 | `2025-12-21T10:27:50Z` | 提交缓冲内；首公告未核 |
| 2512.18675v1 | `2025-12-21T10:29:57Z` | 提交缓冲内；首公告未核 |
| 2512.18725v1 | `2025-12-21T12:59:45Z` | 提交缓冲内；首公告未核 |
| 2512.18730v1 | `2025-12-21T13:28:58Z` | 提交缓冲内；首公告未核 |
| 2512.18733v1 | `2025-12-21T13:46:36Z` | 提交缓冲内；首公告未核 |
| 2512.18736v1 | `2025-12-21T13:54:27Z` | 提交缓冲内；首公告未核 |
| 2512.18741v1 | `2025-12-21T14:02:53Z` | 提交缓冲内；首公告未核 |
| 2512.18746v1 | `2025-12-21T14:26:14Z` | 提交缓冲内；首公告未核 |
| 2512.18832v1 | `2025-12-21T17:28:42Z` | 提交缓冲内；首公告未核 |
| 2512.18834v1 | `2025-12-21T17:36:26Z` | 提交缓冲内；首公告未核 |
| 2512.18850v1 | `2025-12-21T18:40:15Z` | 提交缓冲内；首公告未核 |
| 2512.18934v1 | `2025-12-22T00:51:39Z` | 提交缓冲内；首公告未核 |
| 2512.18950v1 | `2025-12-22T01:56:28Z` | 提交缓冲内；首公告未核 |
| 2512.18987v1 | `2025-12-22T02:55:25Z` | 提交缓冲内；首公告未核 |
| 2512.19004v1 | `2025-12-22T03:45:04Z` | 提交缓冲内；首公告未核 |
| 2512.19011v1 | `2025-12-22T04:00:35Z` | 提交缓冲内；首公告未核 |
| 2512.19018v1 | `2025-12-22T04:15:24Z` | 提交缓冲内；首公告未核 |
| 2512.19025v1 | `2025-12-22T04:42:41Z` | 提交缓冲内；首公告未核 |
| 2512.19027v1 | `2025-12-22T04:53:40Z` | 提交缓冲内；首公告未核 |
| 2512.19126v1 | `2025-12-22T08:07:00Z` | 提交缓冲内；首公告未核 |
| 2512.19134v1 | `2025-12-22T08:28:05Z` | 提交缓冲内；首公告未核 |
| 2512.19154v1 | `2025-12-22T08:50:30Z` | 提交缓冲内；首公告未核 |
| 2512.19171v1 | `2025-12-22T09:05:06Z` | 提交缓冲内；首公告未核 |
| 2512.19179v1 | `2025-12-22T09:13:40Z` | 提交缓冲内；首公告未核 |
| 2512.19206v1 | `2025-12-22T09:44:26Z` | 提交缓冲内；首公告未核 |
| 2512.19215v1 | `2025-12-22T09:54:52Z` | 提交缓冲内；首公告未核 |
| 2512.19219v1 | `2025-12-22T10:02:10Z` | 提交缓冲内；首公告未核 |
| 2512.19238v1 | `2025-12-22T10:20:20Z` | 提交缓冲内；首公告未核 |
| 2512.19250v1 | `2025-12-22T10:34:45Z` | 提交缓冲内；首公告未核 |
| 2512.19297v1 | `2025-12-22T11:40:47Z` | 提交缓冲内；首公告未核 |
| 2512.19323v1 | `2025-12-22T12:17:47Z` | 提交缓冲内；首公告未核 |
| 2512.19342v1 | `2025-12-22T12:36:54Z` | 提交缓冲内；首公告未核 |
| 2512.19350v1 | `2025-12-22T12:49:12Z` | 提交缓冲内；首公告未核 |
| 2512.19396v1 | `2025-12-22T13:42:18Z` | 提交缓冲内；首公告未核 |
| 2512.19428v1 | `2025-12-22T14:29:18Z` | 提交缓冲内；首公告未核 |
| 2512.19433v1 | `2025-12-22T14:31:58Z` | 提交缓冲内；首公告未核 |
| 2512.19443v1 | `2025-12-22T14:42:31Z` | 提交缓冲内；首公告未核 |
| 2512.19535v1 | `2025-12-22T16:21:39Z` | 提交缓冲内；首公告未核 |
| 2512.19585v1 | `2025-12-22T17:12:04Z` | 提交缓冲内；首公告未核 |
| 2512.19606v1 | `2025-12-22T17:42:51Z` | 提交缓冲内；首公告未核 |
| 2512.19673v1 | `2025-12-22T18:51:48Z` | 提交缓冲内；首公告未核 |
| 2512.19682v1 | `2025-12-22T18:57:13Z` | 提交缓冲内；首公告未核 |
| 2512.19728v1 | `2025-12-17T06:15:52Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.19741v1 | `2025-12-17T21:45:12Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.19765v1 | `2025-12-21T05:37:42Z` | 提交缓冲内；首公告未核 |
| 2512.19769v1 | `2025-12-22T05:03:37Z` | 提交缓冲内；首公告未核 |
| 2512.19849v1 | `2025-12-22T20:05:09Z` | 提交缓冲内；首公告未核 |
| 2512.19879v1 | `2025-12-22T21:12:02Z` | 提交缓冲内；首公告未核 |
| 2512.19905v1 | `2025-12-22T22:13:06Z` | 提交缓冲内；首公告未核 |
| 2512.19920v1 | `2025-12-22T22:51:48Z` | 提交缓冲内；首公告未核 |
| 2512.19941v1 | `2025-12-23T00:18:23Z` | 提交缓冲内；首公告未核 |
| 2512.20002v1 | `2025-12-23T02:55:04Z` | 提交缓冲内；首公告未核 |
| 2512.20061v1 | `2025-12-23T05:27:16Z` | 提交缓冲内；首公告未核 |
| 2512.20080v1 | `2025-12-23T06:26:20Z` | 提交缓冲内；首公告未核 |
| 2512.20083v1 | `2025-12-23T06:27:18Z` | 提交缓冲内；首公告未核 |
| 2512.20092v1 | `2025-12-23T06:37:29Z` | 提交缓冲内；首公告未核 |
| 2512.20111v1 | `2025-12-23T07:11:26Z` | 提交缓冲内；首公告未核 |
| 2512.20136v1 | `2025-12-23T07:54:03Z` | 提交缓冲内；首公告未核 |
| 2512.20156v1 | `2025-12-23T08:35:27Z` | 提交缓冲内；首公告未核 |
| 2512.20159v1 | `2025-12-23T08:39:22Z` | 提交缓冲内；首公告未核 |
| 2512.20166v1 | `2025-12-23T08:45:24Z` | 提交缓冲内；首公告未核 |
| 2512.20168v1 | `2025-12-23T08:53:36Z` | 提交缓冲内；首公告未核 |
| 2512.20169v1 | `2025-12-23T08:56:49Z` | 提交缓冲内；首公告未核 |
| 2512.20176v1 | `2025-12-23T09:16:41Z` | 提交缓冲内；首公告未核 |
| 2512.20184v1 | `2025-12-23T09:20:42Z` | 提交缓冲内；首公告未核 |
| 2512.20188v1 | `2025-12-23T09:28:20Z` | 提交缓冲内；首公告未核 |
| 2512.20198v1 | `2025-12-23T09:43:32Z` | 提交缓冲内；首公告未核 |
| 2512.20210v1 | `2025-12-23T10:03:47Z` | 提交缓冲内；首公告未核 |
| 2512.20237v1 | `2025-12-23T10:49:42Z` | 提交缓冲内；首公告未核 |
| 2512.20245v1 | `2025-12-23T10:55:32Z` | 提交缓冲内；首公告未核 |
| 2512.20276v1 | `2025-12-23T11:29:03Z` | 提交缓冲内；首公告未核 |
| 2512.20278v1 | `2025-12-23T11:33:32Z` | 提交缓冲内；首公告未核 |
| 2512.20291v1 | `2025-12-23T12:00:10Z` | 提交缓冲内；首公告未核 |
| 2512.20293v1 | `2025-12-23T12:01:32Z` | 提交缓冲内；首公告未核 |
| 2512.20334v1 | `2025-12-23T13:08:19Z` | 提交缓冲内；首公告未核 |
| 2512.20458v1 | `2025-12-23T15:53:33Z` | 提交缓冲内；首公告未核 |
| 2512.20573v1 | `2025-12-23T18:16:58Z` | 提交缓冲内；首公告未核 |
| 2512.20612v1 | `2025-12-23T18:58:25Z` | 提交缓冲内；首公告未核 |
| 2512.20626v1 | `2025-11-26T05:00:03Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.20636v1 | `2025-12-03T07:47:49Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.20650v1 | `2025-12-16T09:57:18Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.20660v1 | `2025-12-18T15:28:21Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.20662v1 | `2025-12-19T03:01:59Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.20675v1 | `2025-12-20T19:50:36Z` | 缓冲起点前；仅标题查漏，首公告未核 |
| 2512.20687v1 | `2025-12-22T19:26:59Z` | 提交缓冲内；首公告未核 |
| 2512.20757v1 | `2025-12-23T20:43:06Z` | 提交缓冲内；首公告未核 |
| 2512.20760v1 | `2025-12-23T20:45:31Z` | 提交缓冲内；首公告未核 |
| 2512.20798v1 | `2025-12-23T21:52:53Z` | 提交缓冲内；首公告未核 |
| 2512.20806v1 | `2025-12-23T22:13:14Z` | 提交缓冲内；首公告未核 |
| 2512.20812v1 | `2025-12-23T22:22:18Z` | 提交缓冲内；首公告未核 |
| 2512.20839v1 | `2025-12-23T23:30:56Z` | 提交缓冲内；首公告未核 |
| 2512.20848v1 | `2025-12-23T23:54:32Z` | 提交缓冲内；首公告未核 |
| 2512.20861v1 | `2025-12-24T00:41:13Z` | 提交缓冲内；首公告未核 |
| 2512.20877v1 | `2025-12-24T01:36:50Z` | 缓冲终点后；不归本窗 |
| 2512.20908v1 | `2025-12-24T03:19:05Z` | 缓冲终点后；不归本窗 |
| 2512.20920v1 | `2025-12-24T03:56:58Z` | 缓冲终点后；不归本窗 |
| 2512.20934v1 | `2025-12-24T04:30:21Z` | 缓冲终点后；不归本窗 |
| 2512.21354v1 | `2025-12-22T00:27:38Z` | 提交缓冲内；首公告未核 |
| 2512.22208v1 | `2025-12-22T02:36:42Z` | 提交缓冲内；首公告未核 |
| 2512.22211v1 | `2025-12-22T03:51:34Z` | 提交缓冲内；首公告未核 |
| 2512.22212v1 | `2025-12-22T04:52:43Z` | 提交缓冲内；首公告未核 |
| 2512.22216v1 | `2025-12-22T10:34:22Z` | 提交缓冲内；首公告未核 |
| 2512.22219v1 | `2025-12-22T14:18:20Z` | 提交缓冲内；首公告未核 |
| 2512.22226v1 | `2025-12-23T03:33:45Z` | 提交缓冲内；首公告未核 |
| 2512.22234v1 | `2025-12-23T08:33:19Z` | 提交缓冲内；首公告未核 |
| 2512.22238v1 | `2025-12-23T14:40:38Z` | 提交缓冲内；首公告未核 |
| 2512.22245v1 | `2025-12-23T22:08:46Z` | 提交缓冲内；首公告未核 |
| 2512.22250v1 | `2025-12-24T04:04:26Z` | 缓冲终点后；不归本窗 |

HTML 404的20080和20662已换为 [20080v1 PDF](https://arxiv.org/pdf/2512.20080v1)、[20662v1 PDF](https://arxiv.org/pdf/2512.20662v1)读取完整题摘；§3中的相应HTML链接仅说明失败原入口，正式复核用PDF。20660 HTML标题提取空，但原文摘要可读，标题另由显式v1 Atom及 [20660v1 PDF第一页](https://arxiv.org/pdf/2512.20660v1)确认。其余108篇v1 HTML HTTP200，最终URL保持v1。

## 7. 外部保留、重开与交接

**有限任务内普通发现/指定题摘待办：0。** 已完成以上有界扫描、指定身份完整题摘和影响筛选的必要局部。未执行的工作是按日公告证据扩展后的正式候选准入、评分/Evidence及Books，属于root流程，不在本sidecar中伪称完成。raw列表不是所有命中的必审队列；这份有限结果不支持“本日arXiv全部无遗漏”。

本窗终态外部保留：§3所有potential的实际首次公开批次，以及能覆盖本窗的官方new公告列表。现有API只能恢复提交，月份/邻接数字/一般排期不能填缺口；不用于正面证据、Books或无遗漏断言。不把缺个体公告写成“零新论文”，也不因日期不明把potential降为negative。

**逐ID重开条件：** 与相同材料身份/版本对应的官方首次 `new` RSS/email/list item及其批次，或等效官方逐篇公告/公共可用时间；若作者更早公开正文，则须原始首次发布及时间范围。只有日字段时先核标签时区、公告schedule映射和精度，支持范围必须完整落窗；09:00边界不能静默挪日。replacement/cross-list不当new。取得后只恢复该家族的日期归属和所依赖判断，不重抓未变v1题摘，不重扫整月。

**必要修订/反证重开条件：** 具体撤回/纠错影响v1采用命题、现有负侧原文出现此前未见机制或有效性边界、复核指出具体漏项/共同错因；只重开受影响项。未知日期不会取消仍可执行的安全局部核验，已读边界保留，不为节省后续深审改判。

**交 root / Feynman：** 本文件可立即用于本日来源覆盖限制、准入校准和负侧分层抽检；全部potential及安全/设计反证均应列入复核实际范围，不能按本文108条制造本窗冻结池。优先核日志中网页索引与版本字段冲突、5个提交终点后溢出、8个早提交但公告未核的标题查漏及22216/20002版本误排风险。没有独立复核通过或整日完成声明。

## 8. 非作者发现的局部漏项已补回（root，21:26）

上面的110项及108potential是作者第一批范围，不是最终发现规模。Feynman重取原四查询后从系统组51标题定点补5个歧义身份；不是扩成51项全文队列。root随后实际读下面4项完整exact-v1题摘并确认保留，20778关闭由非作者实际题摘记录支撑。合并先为115个完整题摘身份、112potential、3个关闭；随后22208必要v1正文反证触发重开，最终为115身份、113potential、2关闭，新增核验见下段。未授115篇全文或113个本日候选。原始查询数量不变。

| 原始身份 | v1 Submitted UTC | 具体增量与处置 |
| --- | --- | --- |
| [2512.19605v1 KerJEPA](https://arxiv.org/abs/2512.19605v1) | 2025-12-22T17:41:26Z | Gaussian kernel/prior及切片估计约束→可变核/先验和sliced MMD高维闭式极限→表示正则几何与计算取舍potential。不是GPU kernel不等于范围外。 |
| [2512.19081v1 Population-Evolve](https://arxiv.org/abs/2512.19081v1) | 2025-12-22T06:42:46Z | 独立候选无跨轮改进→动态population/evolve prompt/收敛后majority→推理预算与搜索质量的potential，不采用“优越”摘要为归因证据。 |
| [2512.20178v1 SHIRO](https://arxiv.org/abs/2512.20178v1) | 2025-12-23T09:16:52Z | SpMM通信忽略稀疏模式与慢层级链路→sparsity-aware与两级GPU网络协同→计算/通信布局potential，不采用孤立大倍率或外推dense LLM。v2为2026修订，不代本次v1。 |
| [2512.18646v1 Volley Revolver](https://arxiv.org/abs/2512.18646v1) | 2025-12-21T08:40:31Z | 单密文slots必须容整张图→跨密文分区保留卷积/矩阵乘结构→加密推理容量可行性potential，不授通用隐私/性能保证。 |
| [2512.20778v1 Dec-POMDP](https://arxiv.org/abs/2512.20778v1) | 2025-12-23T21:25:53Z | 非作者完整题摘确认其增量为传统open-loop多智能体概率/通信保证，不涉及模型能力形成或模型驱动Agent执行。关闭不是因small/理论标签，不借类比纳入。 |

四个新增potential与原potential具有同一必要first-public外部缺口：Submitted不能替代公告，不评分、不采用、不进入Books；逐ID官方new批次或等效原始公开界限到达后，只重开真实归属日。20778关闭不需额外追不影响判断的日期。

20662此前末注误写为counterfactual/attack构造研究，现按Feynman实际v1 PDF p5–9、p12–14纠正：A同时改变系统提示和温度；B比较原答与强制gold/verify的不同提示下整段log概率、未统一长度，不能识别同条件解码最优性；C事实检索含逐轮摘要/重述，200轮是上限、正文GPT-4o实际142轮。保留评价混杂与简单检索负侧，不授受控因果、greedy普遍最佳或部署长上下文鲁棒性。root同步的是非作者实际局部结果，不冒称另一套probe/attack实验。

| 重开的精确v1 | 必要正文反证与采用限制 |
| --- | --- |
| [2512.22208v1 Moxin](https://arxiv.org/html/2512.22208v1#S4) | Feynman实际§4及§6.2：同Moxin骨干的直接任务适配与机器人预训练局部Table2不支持“先重预训练必更好”；50k延至150k收益可忽略、单臂FiLM无益。保留训练阶段必要性及资源边界potential，不采用普遍反证或数字优越性；Table2列OpenVLA-OFT而脚注称不report，身份/协议矛盾也保留。原题摘关闭已撤销，原第一批改109potential/1关闭；first-public未核，不评分、不入Books。 |

安全/反证实际非作者范围、原文位置及未核部分见[独立记录](./INDEPENDENT_REVIEW.md)。本次三处具名修复已同步；最终日报一致性仍由Feynman核，不重扫未变附件。
