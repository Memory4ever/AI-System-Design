# 2025-09-01 首批准入独立校准

复核者：Codex，受委派的 09/01～05 独立非作者复核者；主线程为作者。

检查时间：2026-10-06T11:38:52+08:00。此记录只校准贡献潜力与入口，**不是最终 DAY，通过潜力不等于落窗、证据通过或正面采用**。没有修改日报、Books、月度状态或模型，没有 stage、commit、push。

## 1. 本次实际范围

启动时重读当前 `AGENTS.md`、`CODEX_RESEARCH_PROMPT.md`、`docs/RESEARCH_CONTRACT.md`、`docs/REPORT_CONTRACTS.md`、`docs/RESEARCH_SOURCES.md` 使用说明/每日/arXiv主题、`ROADMAP.md` 与 `docs/LEARNING_STATE.md` 的本月 checkpoint。只加载 09/01 材料，没有加载 09/02～05 或其他日期论文上下文。

- 读取本日四份 `arxiv-*.request.json` 的实际查询、窗口、执行时间、分页参数；读取 `fetch_sources.py`，没有执行或改写作者抓取脚本。
- 结构化解析四份 XML 的 feed 字段、全部 80 条身份，归并 69 个唯一家族；这不是 69 篇完整题摘审阅。
- 完整读取指定 12 篇 XML 原始题摘：7 篇潜力样本、4 篇范围外样本、1 篇理论边界样本。其余 **57/69 家族未作语义复核**。
- 定点打开这 12 篇的官方 arXiv 事件页。10 篇精确 v1 abs 页可得；21143v1、21320v1 abs 请求失败，随后分别用 21143v1 PDF 与 21320 当前 abs 页补查。没有把失败响应当作零命中。
- 21143 额外实际读取精确 v1 PDF 完整题摘，以及 Dataset、Experiments、Evaluation 与 Results 文字；未核图像/曲线、代码或实验复现。
- 21186 额外实际读取标注 v1 的 HTML 引言/范围/§2～3.3，以及精确 v1 PDF 的对应公式和 §4.1～4.2。没有遍历 §5～6 或引用文献。PDF 两次截图均失败，公式依据是 PDF 文本和 HTML 交叉读取，不宣称已视觉核图。
- 其他 10 篇没有读方法全文、实验表格、附录或代码。机构来源 `.raw` 未作语义审阅；本次不能验收全部每日来源、全部拟入选、Books 或最终报告。

本次在实际打开的官方事件页已读部分未见撤回/纠错/安全提示；这个观察不等于穷尽网站，也不排除未检查部分存在提示。21186 的设计反证是复核计算所得，见下文。

## 2. 查询与日期：当前不能授 Coverage 或落窗

| 缓存 | totalResults | startIndex | entries/itemsPerPage | 实际停止 |
| --- | ---: | ---: | ---: | --- |
| [arxiv-model.xml](./arxiv-model.xml) | 32 | 0 | 20/20 | 只返回第 1～20 条 |
| [arxiv-systems.xml](./arxiv-systems.xml) | 59 | 0 | 20/20 | 只返回第 1～20 条 |
| [arxiv-agents.xml](./arxiv-agents.xml) | 58 | 0 | 20/20 | 只返回第 1～20 条 |
| [arxiv-multimodal.xml](./arxiv-multimodal.xml) | 58 | 0 | 20/20 | 只返回第 1～20 条 |

共 80 个返回条目、69 个唯一家族；四个 total 相加不能得到唯一总量，也不能反推当窗论文量。尾部尚未覆盖，但**不要求把这四个过宽查询的尾部全变成逐项关闭队列**。应先窄修，明确旧入口未完成，新入口按真实分页记录覆盖。

目标窗口为 `[2025-08-31T09:00:00+08:00, 2025-09-01T09:00:00+08:00)`，即 UTC `[2025-08-31T01:00:00Z, 2025-09-01T01:00:00Z)`。四个请求实际用的是 `submittedDate:[20250828180000 TO 20250829180000]`，只能作发现切片，不能当公开窗口。API `published` 与版本页的 Submitted 时间只证明记录中的提交字段，**不证明首次公开时刻**。

以下保留 XML 原值，不将其改名为公开时间；所有 12 篇本次均未确认落窗：

| ID | XML版本 | XML published（UTC，提交线索） | XML updated（UTC） | 精确版本问题 |
| --- | --- | --- | --- | --- |
| 2508.21141 | v2 | 2025-08-28T18:18:19Z | 2025-09-09T09:54:15Z | 已读 v1 abs 题摘；深审仍须 v1 正文 |
| 2508.21143 | v4 | 2025-08-28T18:22:38Z | 2026-10-02T14:47:53Z | 已恢复 v1 PDF；在线无版本页返回 v3，不能替代 v4/v1 |
| 2508.21181 | v1 | 2025-08-28T19:45:36Z | 2025-08-28T19:45:36Z | 明确范围外；日期不影响此处排除 |
| 2508.21186 | v1 | 2025-08-28T20:00:22Z | 2025-08-28T20:00:22Z | HTML页内日期为2026-08-24，PDF页内为2025-09-01；均不能证明公开日期 |
| 2508.21188 | v2 | 2025-08-28T20:02:10Z | 2025-09-02T16:27:24Z | v1标题不同；已读 v1 abs，深审须 v1 正文 |
| 2508.21206 | v1 | 2025-08-28T20:48:38Z | 2025-08-28T20:48:38Z | 题摘潜力；方法/对照未读 |
| 2508.21228 | v1 | 2025-08-28T21:39:53Z | 2025-08-28T21:39:53Z | 题摘潜力；方法/对照未读 |
| 2508.21254 | v1 | 2025-08-28T22:55:15Z | 2025-08-28T22:55:15Z | 明确范围外；日期不影响此处排除 |
| 2508.21257 | v1 | 2025-08-28T23:03:35Z | 2025-08-28T23:03:35Z | 明确范围外；日期不影响此处排除 |
| 2508.21300 | v1 | 2025-08-29T01:45:09Z | 2025-08-29T01:45:09Z | 题摘潜力；方法/对照未读 |
| 2508.21320 | v1 | 2025-08-29T04:13:42Z | 2025-08-29T04:13:42Z | 明确范围外；日期不影响此处排除 |
| 2508.21324 | v1 | 2025-08-29T04:42:17Z | 2025-08-29T04:42:17Z | 题摘潜力；方法/对照未读 |

拟入选/理论争议项要用官方历史公开列表/公告及必要版本历史确认首公开事件，并保留时区、精度和证据支持的上下界。提交 cutoff、惯例、PDF页内日期、索引登记日或后来会议发表均不能单独完成此证明；只有整个公开区间落窗才授落窗。若可用原始入口仍无法建立界限，作者应隔离为具体日期缺口，不能填造时刻或说当天无论文。四篇已明确范围外样本不因无关日期继续追查。

## 3. 七篇有具体贡献潜力：允许推进核验，不授正面采用

下列 owner 仅为 ROADMAP 路由，不是 Books 已有覆盖判定；未读取 Books 正文，不评分。

| 材料与原始读取位置（XML条目从1计） | 约束 → 原文增量 → 需重考的选择 | 后续必须核的反侧与最小边界 |
| --- | --- | --- |
| [2508.21141v1：Adaptive LLM Routing under Budget Constraints](https://arxiv.org/abs/2508.21141v1)，model#1；缓存为v2 | 完整 query-model 最优标签昂贵且流量变化 → 共享 query/model embedding、偏好先验加在线 contextual-bandit 反馈与预算策略 → 是否以部分反馈替代穷举监督路由。有具体学习/预算机制，`PLATFORM-GATEWAY` 路由潜力通过。 | 精确v1正文；离线偏好收集和预热成本、bandit反馈可得性/延迟/噪声、探索损失、预算是否每请求/累计、knapsack近似、相同成本质量约束下与监督路由/静态策略比较。不得推成无监督最优或预算硬保证。 |
| [2508.21143v1：Can Multimodal LLMs Solve the Basic Perception Problems of Percept-V?](https://arxiv.org/pdf/2508.21143v1)，agents#2；缓存为v4 | 复杂多模态成绩不直接证明基础感知 → 程序生成的简单图形任务按问题规模变化检验失败 → 评价中应分离基础感知、规模与高层推理。负结果有具体评价盲区，`PLATFORM-EVALUATION-SYSTEM` 潜力通过。 | v1摘要写7200图，Dataset/Experiments文字为30×200=6000，须对表/生成器核清；已读协议为零样本、temperature=0、1000输出token、格式错误计错、全对式list/set评价。规模效应可能混合输出长度、计数/推理及格式错误，不能直接归因感知或训练表示。缓存中的微调收益/迁移限制不由本次v1读取建立；不能移植为2025结论。 |
| [2508.21206v1：Enhancing Robustness of Autoregressive Language Models against Orthographic Attacks via Pixel-based Approach](https://arxiv.org/abs/2508.21206v1)，model#5 | 字符扰动可能破坏subword表示 → 把词渲染成图像、以pixel表示接入生成LM → tokenizer/输入表示的鲁棒性与成本取舍。有直接表示替代，`MODEL-TOKENIZER` 潜力通过，不是普通SST-2应用。 | 核字体/字形覆盖、词切分、相似字攻击与真实噪声、同参数/训练数据/算力对照、干净质量、序列长度及渲染开销。摘要将损伤归因OOV是待核的作者解释，不能据此说所有subword系统都有字面OOV或pixel方案已解决多语言安全。 |
| [2508.21228v1：Decoding Memories: An Efficient Pipeline for Self-Consistency Hallucination Detection](https://arxiv.org/abs/2508.21228v1)，model#6、agents#10 | 多响应一致性检测重复生成成本高 → 共享前缀冗余分析、selective inference与annealed decoding → 生成成本与检测保真能否兼顾。`INFER-DECODE` 潜力通过；不是“又一个幻觉检测器”就关闭。 | 精确v1的选择/退火规则、复用是否改变独立采样及多样性、误检/漏检、阈值和分布外AUROC、端到端开销、基线已有缓存、长度/硬件/batch。摘要的up-to加速不是通用收益，更不证明生成事实可靠或向RL/推理直接可迁移。 |
| [2508.21324v1：Distribution-Aware Feature Selection for SAEs](https://arxiv.org/abs/2508.21324v1)，model#12 | BatchTopK可能由高幅值特征主导 → 按列范数/熵限定候选池后选择、用l调节共享结构与重构 → 字典激活选择不是单一最佳预算。`WORLDVIEW-REPRESENTATION` 潜力通过，不能以Pythia-160M或无普适最优排除。 | 精确v1中token/feature选择轴及预算、Norm/entropy评分、稀有特征指标、重构/下游/解释性是否同一约束、l的消融及seed。局部取舍可成立，但不能将重构改善当解释真实性、将稀有高幅值一律当坏特征或外推大模型。 |
| [2508.21188v1：Model-Task Alignment Drives Distinct RL Outcomes](https://arxiv.org/abs/2508.21188v1)，systems#7；缓存v2改题为Mirage or Method? | 单样本、弱奖励、负样本训练的惊人结果可能依赖已有能力 → 以基础模型pass@k刻画model-task alignment并比较失效区间 → 应按起始可解性核评价简化RL配方。`TRAIN-GRPO` 反证潜力通过，已有RL主题或负结果不构成排除。 | 精确v1模型/任务/pass@k的k与采样协议、训练/rollout/评估预算、奖励配置、同难度分层和因果替代解释；不能把pass@k等同普适对齐程度，也不推成标准RL在所有困难任务均有效。v2改题/更新不自动等于重要修订。 |
| [2508.21300v1：Improving Fisher Information Estimation and Efficiency for LoRA-based LLM Unlearning](https://arxiv.org/abs/2508.21300v1)，systems#20 | FILA参数定位依赖全模型访问且Fisher假设受疑 → VILA修改重要性估计并减小定位/更新范围 → LoRA遗忘的定位成本与有效性边界需核。`TRAIN-LORA` 潜力通过，有具体估计和参数机制。 | 核被违反/修复的Fisher假设、近似误差、访问全参数与只更新adapter的区别、预计算/存储/端到端成本、forget/retain质量、relearning及泄漏攻击、同基线配置。参数效率/训练倍率不能当总体成本或可验证隐私擦除保证。 |

这七项只是当前题摘已建立值得审查的命题。日期不清不消除潜力；只缺实验细节不应退回排除。深审后可收窄、争议或基于新证据改判，但不能因为访问困难/深审费时/主题已有而缩池。

## 4. 四篇范围外抽检

全部读过完整题摘，不宣称作者原筛选全量正确。没有主线程排除账本可对照，因此这是独立判断而非声称修复已落实。

| 材料/读取位置 | 排除的具体依据，不是否认学术贡献 |
| --- | --- |
| [2508.21254v1：Reverse Imaging for Wide-spectrum Generalization of Cardiac MRI Segmentation](https://arxiv.org/abs/2508.21254v1)，multimodal#9 | spin-property逆问题、医学序列合成与心脏MRI分割泛化是领域机制；diffusion作为spin先验不建立通用基础模型/生成系统机制。本阶段不以Data/Representation owner重新引入医学科学应用。 |
| [2508.21257v1：PHD: Personalized 3D Human Body Fitting with Point Diffusion](https://arxiv.org/abs/2508.21257v1)，multimodal#11 | 个体体型标定、条件3D pose先验与拟合损失改进HMR精度，含具体领域贡献；题摘未显示多模态基础模型、world transition或VLA控制机制，不因3D/Transformer/diffusion词自动纳入。 |
| [2508.21320v1：Multi-Ontology Integration with Dual-Axis Propagation for Medical Concept Representation](https://arxiv.org/abs/2508.21320)，model#11 | LLM/graph-RAG初始化加医疗本体内外传播，收益落在EHR/稀有病预测，未建立通用LLM RAG或模型能力形成的新边界；范围外。没有因为含LLM/RAG就授`AGENT-RAG`。 |
| [2508.21181v1：FUTURE: Flexible Unlearning for Tree Ensemble](https://arxiv.org/abs/2508.21181v1)，multimodal#7 | 概率近似使不可微树集成可梯度遗忘，有算法贡献；但题摘没建立对当前模型能力/LLM系统设计的直接约束或理论迁移，不能以“unlearning同主题”纳入。本理由是机制对象/关系，不是小模型或非Transformer一刀切。 |

上述只覆盖这四种排除理由/样本。若后续存在同理由排除的其他直接模型机制或反证，需定点扩查受影响集合，不能用这四项样本证明全部57项排除正确。

## 5. 21186：理论边界与具体正确性反侧

[2508.21186v1](https://arxiv.org/pdf/2508.21186v1) 直接讨论next-token输出分布，不能因为“理论”“没有benchmark”排除；可能有贡献的命题是固定logits下的动力学、温度和截断边界。经典Gibbs/softmax推导的重述本身不够准入，作者新增动力学命题则必须核数学。

实际重点读取：PDF印刷页5的§3.1式(3.1)/(3.2)与一阶条件，页6的§3.2，页7的§3.3，页8的Thm.4.1及Cor.4.4；HTML对应章节交叉核。网页HTML页内日期与PDF日期不同，不靠HTML标签宣称内容全部是2025原稿；本反侧已在精确v1 PDF文本中确认同样的目标/更新式/ODE/收敛主张。截图失败未隐瞒。

复核者推导（不是作者结果）：

1. 原文熵正则KL-prox目标 `p·s + T H(p) - KL(p||q)/eta` 的一阶条件给出
   `p_i ∝ q_i^(1/(1+eta*T)) * exp(eta*s_i/(1+eta*T))`，不是式(3.2)的 `q_i * exp(eta*s_i/T)`。少掉的熵作用不能由归一化常数吸收。
2. 对原文ODE `dp_i/dt = p_i*(s_i-E_p[s])/T`，取 `s=(1,0), T=1`。softmax约为 `(0.731059,0.268941)`，代回ODE导数为 `(0.196612,-0.196612)`，**不是平衡点**。从均匀初值的精确解为 `p_1(t)=1/(1+exp(-t))`，趋向argmax，不是有限温度softmax。实际本地计算核了这组数值；这是公式反例，不是LLM实验或复现。
3. 熵正则正确流要有与 `-T log p_i` 有关的项；改变T同时改变softmax终点，所以“只重参数化时间且同一softmax终点”的合并主张也不能直接采用。固定support的讨论不覆盖跨生成步骤变化的nucleus集合或隐藏态/训练动力学。

因此本项不能作为正面理论证据。**不以“已有主题/普通理论”关闭，也不在此自授最终排除**：这是中心主张的具体正确性信号，主线程应保留争议/反侧，深入受影响内容，并核是否有官方修正。重开需要修正目标与更新式、可验证的含熵证明或能消解上述反例的精确原版本；另仍需真实公开时间证据。页内“September 1, 2025”不能用来解决日期依赖。

## 6. 可执行窄修：保留四条有界主题线，不转成全分类队列

实际入口偏宽的原因：model把attention/embedding独立作锚；systems把training/inference/parallel独立作锚；agents无模型锚的memory/reasoning；multimodal中的world/diffusion不限对象。已读样本证实医疗embedding、树模型、MRI diffusion/HMR等可被带入。不是查询命中就要逐项深审。

下面是给作者的替换查询提案，**本复核者未执行、未验证返回量或召回率**。仍用现有提交切片作发现，不宣称它等于本窗公开切片；只替换四组topic predicate，不修改合同、作者文件或日期证据。每条附 `AND submittedDate:[20250828180000 TO 20250829180000]`，URL编码后交给现有API入口。

### model

```text
(cat:cs.CL OR cat:cs.LG) AND ((ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:"foundation model" OR abs:"foundation model") AND (ti:transformer OR abs:transformer OR ti:attention OR abs:attention OR ti:tokenizer OR abs:tokenizer OR ti:embedding OR abs:embedding OR ti:optimization OR abs:optimization OR ti:pretraining OR abs:pretraining OR ti:unlearning OR abs:unlearning) OR ti:"sparse autoencoder" OR abs:"sparse autoencoder" OR ti:SAE OR ti:SAEs OR ti:"next-token" OR abs:"next-token")
```

保留小模型SAE与next-token理论入口；不用“大模型参数规模”作范围门槛。本日12篇已知线索在旧缓存中可重用，不因新查询未召回而丢弃。

### systems

```text
(cat:cs.DC OR cat:cs.LG OR cat:cs.PF OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS) AND ((ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR abs:transformer) AND (ti:inference OR abs:inference OR ti:training OR abs:training OR ti:cache OR abs:cache OR ti:parallel OR abs:parallel OR ti:routing OR abs:routing OR ti:communication OR abs:communication OR ti:kernel OR abs:kernel) OR (ti:GPU OR abs:GPU) AND (ti:"model training" OR abs:"model training" OR ti:"model inference" OR abs:"model inference"))
```

新增系统分类仅在这个明确的模型/GPU主题predicate下补检，不加载这些分类的全部论文。若GPU通用编译/通信标题有直接模型线索，可定点补摘，不扩大为通用系统审阅。

### agents / post-training reasoning

```text
(cat:cs.CL OR cat:cs.AI OR cat:cs.IR OR cat:cs.LG OR cat:cs.MA) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:"foundation model" OR abs:"foundation model") AND (ti:agent OR abs:agent OR ti:memory OR abs:memory OR ti:reasoning OR abs:reasoning OR ti:"tool use" OR abs:"tool use" OR ti:"tool calling" OR abs:"tool calling" OR ti:"retrieval augmented" OR abs:"retrieval augmented" OR ti:RL OR abs:"reinforcement learning" OR ti:reward OR abs:reward)
```

这条保留21188式后训练反证，不将通用reasoning或传统multi-agent博弈全纳入。LINKO仍可能命中，语义范围筛选照常执行，不用医疗词一刀切NOT排除可能含通用机制的研究。

### multimodal

```text
(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.CL) AND (ti:"multimodal language model" OR abs:"multimodal language model" OR ti:"vision language model" OR abs:"vision language model" OR ti:MLLM OR abs:MLLM OR ti:"foundation model" OR abs:"foundation model" OR ti:"world model" OR abs:"world model" OR ti:"vision language action" OR abs:"vision language action" OR ti:VLA OR abs:VLA OR (ti:diffusion OR abs:diffusion OR ti:"flow matching" OR abs:"flow matching") AND (ti:"image generation" OR abs:"image generation" OR ti:"video generation" OR abs:"video generation" OR ti:"language model" OR abs:"language model" OR ti:"generative model" OR abs:"generative model"))
```

用短语替换裸world；diffusion与生成对象配对而不全扫医学/姿态diffusion。生成机制用新命名时由下面的标题补检兜底，不能声称这个术语集合全召回。

执行/停止办法：四条窄查询按20条分页，保存每页的start/total/返回条数和执行时间；重叠家族先归并。只能在确实页读完后写该有限查询已检查，错误/截断留具体停止点。不要补齐旧过宽total尾部来制造Coverage。

有界补检：只在**目标历史公告批次**的官方分类标题列表浏览项目相关标题；只对含糊/相关标题读摘要，明确领域应用不扩审。记录实际分类、批次、页范围/停止点，不能把整月list或当前recent当目标批次，不能让全部分类条目进入关闭队列。本次12条已知线索继续保留，窄修只重开受过宽/截断或错误排除理由影响的集合；不推倒其他有效工作。

## 7. 向主线程的校准结论与交接

首批12篇潜力/范围校准已完成：**7篇有具体贡献潜力、4篇范围外、1篇直接相关但中心数学主张有反例需争议审阅**。校准不是评分、证据终审、Books决定或09/01 DAY；未授任何论文落窗或正面采用。

主线程仍需执行窄修/来源处理、精确v1必要证据阅读、真实公开日期确认及候选/Books处置；其中21143不可照搬最新摘要，21186不可以metadata登记或PDF页内日期补造公开时刻。未读57家族不代表漏收57候选，也不代表已全部排除。

等待主线程准备好的09/01～05各自日报后再逐日执行最终DAY。每次换日先重读当前合同/来源规则，只加载当前日窗口、材料和停点；本记录未变化的校准结论可复用，新拟入选与具体改判仍须覆盖。最终DAY要实际检查作者六部分、有限来源停止、全部拟入选、反侧/分层排除样本及Books决定/实际写入。本复核者不会写日报状态或Books。
