# 2602.09992v1 必要审阅（作者准备，独立 Source 尚待）

精确身份：[A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models](https://arxiv.org/html/2602.09992v1)。完整AB准入与Feb11包络root已核；评分2+1+2=5，因强“无直接证据”表述定点深入filter与反侧，支持足即停。原件poshcore/posheval/poshleak/poshfind（click anchor返回首段不当附录读完）。

拟采用：受限AR语言模型可在过滤直接例句后对部分层次语法minimal pair高于chance；提高一般语法benchmark的三种结构/recency bias却不自动改善指定稀疏构式。不是innateness已被否证、人类机制证明或大模型普遍成立。§3–7 L156–243：baby-f过滤、baby同句数替换少量QF/binding直接例，wiki对照；10M GPT2mini，30/50M GPT2small与容量变化不授纯scale因果。每设定3seed，最多100kstep早停；§7固定10epoch/句级/无warmup，Dyck额外2kstep、dependency TPT、decaying-recency分别。

关键反侧AppC L383–444：Stanza规则过过滤非真零证据；QF抽查1000/11k候选零发现而非全语料证明，binding1000/5.7k中有6个真实泄漏。作者用exempt/logophor噪声抵消并声称无法支撑泛化，但未有泄漏剔除重训因果对照；不接受“完全无直接positive”或这些泄漏必然无作用。Table8子类complexNP/reducedrelative/c-command常在或低于chance，category平均不能说每种层次泛化均成立。Table3 two-sided chi²星标包括低于chance，非可靠能力认证。

评价条件：500手工验证templated pairs/子类，句perplexity偏好非真实生成/理解行动；词交集控制但§3 top3k与AppF top5k矛盾，不采用exact词表配方。100M语料written比率更高，与10–50M不纯量差。AppE context512/batch32常规；recency另用context32/batch512（L477），比其它架构并非完全匹配。modelhardware/precision/总训练时长 Not Disclosed。Fig1人类来自不同任务/年龄/感知输入，仅背景而非同协议效能比较。§8机制多bias/多模态/其他实现皆假说；不据负结果排除所有结构bias。

Source后owner拟WORLDVIEW-WHY-MODELS-LEARN或MODEL-TRANSFORMER-LAYER中的结构归纳偏置/泛化证据；须实际同命题对比再决策，不因可联想学习章节自授长期差额。
