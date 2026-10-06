# May04 三项必要证据与身份差额

作者jul21_incremental；仅May03 BJT自然日遗漏。以下是具名必要恢复，不是三项确定当窗候选或完整Evidence验收；公开日期门仍缺。准备单篇直接交Anscombe，不等其他日，不写Books。

## 01706：修订说明与噪声配方的实际边界

[精确v1](https://arxiv.org/abs/2505.01706v1) Comments明确更新摘要、算法与实验；可见history仅v1。实际取得[HTML v1](https://arxiv.org/html/2505.01706v1)及当前HTML，均200、295079 bytes，逐字节相同；[PDF v1](https://arxiv.org/pdf/2505.01706v1)200、1794418 bytes、15页。该检查只说明当前可取得载体，不证明历史公开当天正文相同、也不虚构v2/撤回。原件为`SUP_html-dpo-{v1,current}_20261011.*`、`SUP_dpo-pdf-v1_20261011.*`。

作者实际窄读HTML §4.2/4.3/5.5/6和Appendix D Algorithm1；PDF首页与p14算法确认载体符号。提取位置见`SUP_dpo-{S4.SS2,S4.SS3,S5.SS5,S6,A4}_20261011.txt`和`SUP_dpo-pdf-page14_20261011.txt`。复核者另外实际PDF p5/p14见独核§8。

- 本稿在既有2D-DPO上处理segment-score扰动，δ从U(0,1)采样，分别降低preferred、提高rejected分数，因而不是任意标注噪声或一般安全目标；aspect-level翻转/混合噪声仍future work。
- §4.2 Eq11分子两项打印同一loss，不能照录为已证无偏校正。正文§4.3目标为负log，Appendix D第12行累加正log、第17行按下降更新；PDF p14同样，不能声称算法与优化目标已一致或实现正确。
- Table2局部robust行45.625%高于带噪2D-DPO37.188%，但仍低于vanilla DPO58.854%。不据此采用优于DPO、完全不受噪声影响、通用稳健保证；此处数字仅识别反侧，不提升为日报benchmark结论。

处置：保留`TRAIN-DPO`窄P（具体噪声训练目标/配方及限制），不把符号争议当成熟原则EX。官方精确ID首公告查询仅May2025，不能采用PDF/HTML内部May03或citation_online_date代替公告公开日。Books暂缓：当窗事件未证，且无偏/算法一致性桥不成立；恢复需具名公开日和作者纠正原式/实现对照，届时只审拟采用命题，不全版diff。

## 04637：出版身份冲突，不等于出版入口永久不可访问

[arXiv v1](https://arxiv.org/abs/2505.04637v1) Related DOI为`10.5121/csit.2025.150807`。精确HTML404后实际恢复[PDF v1](https://arxiv.org/pdf/2505.04637v1)，200、1142456 bytes、13页：Dongxing Yu，Sanda University，多模态adaptive token boundary论文，首页pp89–101；正文§3.2.2/必要配置已由Anscombe读，实际框架有sigmoid boundary/层次表示/contrastive alignment，不因此声称token序列实现、GPT-4V公开实现或完整预算已验证。

命令请求DOI返回404，出版方www/nonwww PDF请求403，分别保留`SUP_adaptive-related-doi`、`SUP_adaptive-original`、`SUP_adaptive-original-nonwww`请求记录。**这些失败只属于相应入口与访问层**。随后作者使用web实际成功打开[出版方原PDF](https://aircconline.com/csit/papers/vol15/csit150807.pdf)，2026-10-11在线读取首页p0：音乐/歌词Flutter应用、Yuting Gao与Ang Li、pp91–101、11页，同一DOI。Anscombe再次独立web读取首页确认不同身份（独核§8），不是继承搜索摘要或当前作者的标签。

出版方只用于这条具名身份核验，未把另一篇音乐论文加入研究队列、未通读或采用其系统结论。证据已经能够确认两份当前原件身份不同；**未确认哪一方元数据有误，不推断撤稿、造假、该多模态稿的正式发表日或窗前首次公开**。

处置：保留Ch23 token粒度框架窄P，必要出版身份/首次公开日期隔离，Books暂缓；精确ID查询仅May2025。出版方或作者澄清此DOI与题名作者的对应可解决正式发表身份；若独立可靠原证已确认该精确arXiv正文的公开日与身份，则可仅恢复PDF支持的有限框架，不机械要求DOI澄清才允许审v1。不得用另一篇的2025卷期或页码授当窗身份。HTML仍不可用不阻塞PDF可支持的有限框架事实，但不绕过日期门。

## 02858：旧共同反侧与新的联合结构诊断分开

admin overlap具名[旧2407.08323v1](https://arxiv.org/abs/2407.08323v1)，不是撤回。作者实际完整旧AB及旧HTML§1/§5.1必要段，与[新2505.02858v1](https://arxiv.org/html/2505.02858v1)§5.5（Tables8–9、Fig8）/§6比较；原件`SUP_synthetic-{old-abs,old-html,new-html}_20261011.*`及具名section提取保留。Anscombe独核§7.1已有同一窄读，未要求重读全部附录。

旧稿明确单篇看似合理而集合tag复用过低，不能把这个共同反侧全称本稿首次贡献。新稿§5.5具体以NER构造entity-post二部图、按三平台degree-vector比较共同实体分布，区分高频/低频实体差额；§6也自称旧工作的extension，增加MPTM与多个LLM比较。因此不因text overlap全关，保留`TRAIN-DATA`联合结构诊断的窄P，不宣称旧稿无价值或新稿全部方法新颖。

局部实验对prompt无一致普遍优劣，模型/平台差额不能归因唯一算法。§6明确未处理privacy/legal、未测downstream utility；不把fidelity、较低tag复用或NER匹配当隐私/下游质量保证。该原件发表于哪一日仍未确认；官方精确ID查询只给May2025，不能从两年ID或submitted推日。

处置：共同旧反侧不重计，新NER/MPTM比较作为待核事件潜力保留、Books暂缓。恢复需新具体命题的首次公开日/版本身份；如有更早公开相同NER诊断，只对这一命题去重，不推倒其他有效筛选。未为证明不存在旧诊断遍历旧全文/版本全集。

## 当前独核交接

作者提交上述三项给非作者核精确原件/采用边界。单篇必要内容现可复用，不需要重做75AB。日期和04637身份的恢复入口有限处理完毕后，放入本日一次性精确请求；未有任何一项确定落May03，不先评分、不写Books。日级source和六节仍须实际独核，本文不能代签DAY。
