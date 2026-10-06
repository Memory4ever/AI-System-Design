# 12/31 非作者定点准入复核

复核者：Gibbs，非本日作者、非Books写入者。执行时间：2026-10-02T19:54:24+08:00至19:59:02+08:00；随后整理本记录。窗口为 `[2025-12-30T09:00:00+08:00,2025-12-31T09:00:00+08:00)`。

已独立重读AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES使用说明/每日组及主题范围、Prompt、ROADMAP、本日README、ADMISSION与OFFICIAL_CORE。只核用户指定的9项重开和2项机构判断；没有重扫来源、全部86项或完整版本史，没有用作者已读标签代替本轮原文访问。只写本文件，不改metadata、Books或state。

## 结论与准确差额

9项撤回成熟组合/摘要无控制的关闭后，均有可保留的具体方法或局部评价线索；不要求恢复成原关闭，也不因此授予Evidence完成。Qwen-Image-2512的具体贡献关闭有效；HY-MT1.5的2-bit offset/QAT保留为设计potential有效，不能写成已经验证或已发布的2-bit实现。

**需要修正2处准入表述**：24571把检索分块与独立语法服务分开；23294把source/channel“分拆对照”收窄为实际存在的channel KB消融。其余采用限制如下，不新增候选/读文配额。这是局部复核结果，不是12/31日Gate；其余来源、日期表与分层负侧由root汇总。

## 九项实际打开位置与判断

### 2512.24609：collaborative RL

实际打开[exact v1 PDF](https://arxiv.org/pdf/2512.24609v1)印刷页2–3的§II-C/D、页4的§III-C、页5的Table II与§IV相关限制。原文确实提出leave-one-out team credit、冗余交流惩罚及按batch缩放奖励；Table II列去group baseline、去coordination cost和local-only reward，足以保留具体credit/资源路径potential。

边界：§II-C没有展开反事实奖励如何生成，Table II不单独隔离batch normalization。不能把文字“without current move”当已核验counterfactual estimator，或将去成本消融推广为所有协作更可靠；保留原ADMISSION的实现/归因未决。未运行代码，未视觉审读PDF图表，仅读取PDF可提取文本与表格。

### 2512.24571：SynRAG

实际打开[exact v1 HTML](https://arxiv.org/html/2512.24571v1)§III-1至III-4、§IV-B/C及§V。检索是500字符/100重叠的普通分块、top-5；AQL四类组件和YARA-L组件来自另一个syntax service，并作为生成上下文。§IV-C另报告85%无需语法修改可执行，直接限定“保证语法”的宣传。

**修正**：ADMISSION“语法component分段检索”应改为“文档分块检索与组件化syntax service共同条件化生成”。保留词面评分、可执行和意图正确不等价的窄potential；BLEU/ROUGE不是语义证明，85%也不是检出正确率。未见此局部方法给出token级形式grammar enforcement，不写成约束解码已实现；40条人工spec、两平台和组件联合改变未隔离归因。

### 2512.24120：architecture generation

实际打开[exact v1 HTML](https://arxiv.org/html/2512.24120v1)§3.2/Algorithm1、§5.1/5.2/Table1/Figure2文字说明、§5.6及Conclusion的Limitations。支持example数量与生成成功、数据集分布导致aggregate混杂、hash不识别semantic equivalence，具体反证准入有效。

边界：n=6只生成7个模型，但正文同时写97%与99.8% failure，当前不选择一个精确失败率；context dilution/冲突/token耗尽是作者解释，未分别控制，不能当测出统一context容量上限。单epoch和随机example条件下，n=3不是普遍最优；不采用100x或估算GPU小时。无需因这些限制恢复关闭。

### 2512.24113：CogRec

实际打开[exact v1 HTML](https://arxiv.org/html/2512.24113v1)Neuro-Symbolic Bridge/From LLM to Soar、Ablation Study与Learning Curve Analysis。有response解析为condition/action再chunk成production rule的路径，并明确分别去LLM-bootstrap、chunking及Soar；保持chunking关闭后不能积累规则、重复LLM调用的窄机制/评价potential。

边界：Figure3/4相关正文已读，未取得可单独视觉核验的曲线数值，不照录下降幅度。这里的online learning是符号规则积累，不是LLM参数更新；解释可追踪不证明规则真值，错误持久化/回滚尚未核验。当前ADMISSION已留rule质量未决，无必要撤销准入。

### 2512.24613：group deliberation

实际打开[exact v1 PDF](https://arxiv.org/pdf/2512.24613v1)页2的§II-A/B Eq1–4、§II-D，以及页3的§III-B/C、页4的§III-D.2/Figure4文字说明。Gaussian task embedding modulation及self-game权重更新是具体proposal，非只有三角色名；去self-play/retrieval/reward与single-agent的局部消融支持继续核验。

边界：Sfact的embedding相似不等于事实蕴含；离散生成到权重梯度的实现未展开。Cons由五次输出重叠衡量，不是独立truth；GPT-3.5顺序baseline无共享/压缩/pruning，不能把联合收益归因“improved PPO”。页2截图请求Cache miss，未声称视觉公式或Figure4核验；保留设计potential，不采用收敛、可靠性或算法正确保证。

### 2512.23480：software supply chain

实际打开[exact v1 HTML](https://arxiv.org/html/2512.23480v1)§VI-F，定点连读§IV-E/F与§IV-G。原文明确去ledger不影响detection、去LLM影响recall、去RL影响false-positive/latency；审计与检测分工的具体可检验主张，足以维持窄potential，而非按成熟组合删除。

边界：VI-F是短段消融主张，未给对应样本分母、逐variant表或重复不确定性；不写成已证实的归因。permissioned BFT/RBAC/Merkle描述不证明ledger输入真实、授权正确或绝对trust；MCP接口存在也不授credential revocation/自动修复已安全。ADMISSION已有这些必要限制，不要求无关全文。

### 2512.23366：AGRO-SQL

实际打开[exact v1 HTML](https://arxiv.org/html/2512.23366v1)§3.1、§4.2及§6/7。DAG数据库augmentation针对偶然execution正确、prediction/gold分歧触发Gen-as-Check审计是具体监督构造路径；§6直接承认execution equivalence不保证NL faithfulness，维持窄数据/评价potential。

边界：不采用zero-noise/完全消除logic noise。 runnable DB成本、长尾schema覆盖和read-only/access control仍是必要条件；此局部检查没有隔离augmentation各部分的实验归因，也未证明生产SQL安全。ADMISSION无需恢复关闭或补授Evidence。

### 2512.23320：MESA-MIG

实际打开[exact v1 HTML](https://arxiv.org/html/2512.23320v1)§3.4、§4.1/4.2的Table1、§4.4；另核§4.2的VA测量定义。去Verb/Composition/Color/Style各自呈不同metric下降模式，支持属性条件化的窄quality/diversity potential，不只是音乐应用分数。

边界：单agent删除的aggregate比较不证明匹配总token/模型调用预算或无交互效应的纯因果；应把ADMISSION“局部可归因验证”理解为作者消融线索，而非已控全部替代解释。VA相似在§3.4写归一化Euclidean、§4.2写cosine，协议不一致；实际Table3也不支持所有correlation都提高。保留反证，未授情感真值或通用多Agent优越性。

### 2512.23294：SemCom

实际打开[exact v1 HTML](https://arxiv.org/html/2512.23294v1)§IV-B1–3、IV-C及Figure4 caption/对应结果文字。LVM描述→CLIP检索source prior，与entropy/SNR/上一action输入RL rate controller，是具体codec/资源联合设计；不因综述形式关闭。

**修正**：四个baseline中只有AKB-JSCC w/o CKB明确隔离channel KB，没有w/o source KB的完全factorial消融；ADMISSION“source KB与channel KB分拆对照”不能授双侧独立归因。40,000训练/504测试、AWGN、训练SNR10dB及JPEG+LDPC CBR0.035对其他0.03的条件须保留。不授foundation model协作/跨无线环境通用增益；Figure4图像入口失败，仅核caption/文字，未读取曲线数值。

## 两项机构原文

### Qwen-Image-2512

实际打开[官方HF模型卡](https://huggingface.co/Qwen/Qwen-Image-2512)Introduction、Model Performance、Quick Start、Showcase文字与Citation；[Blog](https://qwen.ai/blog?id=qwen-image-2512)本轮仍0行，停止。HF实有三类能力更新、万余盲评和同prompt示例；代码为DiffusionPipeline/50步/CFG4，引用2508.02324。该公开核心没有独立的新训练/采样方法、受控failure边界或安全/兼容性变更证据，维持本材料贡献关闭。

这是对已公开core的具体判断，不声称模型无学术价值/绝无未披露机制，亦不把缺实验细节普遍当排除理由。未视觉评审showcase、不复读August整篇、不需要为该关闭追first-public。

### HY-MT1.5 2-bit

实际打开[2512.24092 exact v1 HTML](https://arxiv.org/html/2512.24092v1)§2.4，并只为确定证据边界连读§3.5/Table4。针对小模型分布增加offset、带bias的对称2-bit QAT及per-channel粒度，是可改变表示/校准选择的具体proposal，准入potential有效，非整个翻译pipeline准入。

§2.4说2BIT权重将来发布；Table4只有原模型、FP8与Int4，不存在本轮已核2-bit对照。不能从FP8/Int4成绩证明offset/QAT有效，更不能授2-bit kernel、端侧资源或无精度损失；量化公式、offset学习/折叠、activation/KV精度与训练预算仍未展开。这些是采用前缺口，不抹去具体设计线索；日期仍隔离，不评分或写Books。

## 交还root

本轮指定11项局部原文访问及准入判断已执行；两处准确措辞修正见上，root需纳入最终归并。其他局部限制用于限定potential与重开后的采用命题，不能被写成这些实验/安全已经通过。没有请求无差别全文或继续同接口日期恢复；没有补造first-public。

局部支持九项重开、Qwen关闭和HY-MT设计potential，**不代表**来源覆盖、个体归日、证据审阅、Books或整日通过。日级metadata/§6与最终Gate仍由root维护。
