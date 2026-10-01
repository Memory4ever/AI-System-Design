# Apr21 最后七项有界非作者采用核验

审阅者 apr02；检查时间 2026-09-27T15:35:10+08:00。复用已实际读取且未变化的当前 AGENTS、研究/Report 合同和统一入口；本次实际读两份作者 batch、七篇官方 v1 必要方法/关键实验，并对读 ROADMAP owner 与 Ch72 Safety Repair、Ch76 Reranking、Ch23 full-duplex 的真实正文。没有重扫270题摘、全部附件或全年来源；没有修改作者报告、作者 notes 或 Books。

此为七项单篇 source→owner/处置核验，不是日期、完整分母、全来源或日级 Gate。三项窄 Books gap 通过写前采用核，仍需共享锁、实际落笔与写后非作者核；不能计为已整合。四项标准仅报告处置通过；另两项只核撤回/日期隔离字段。

## 逐项裁决

### 2604.17207 — 5分，标准仅报告：通过

实际 [v1 §4.1–4.4/§5](https://arxiv.org/html/2604.17207v1)：评的是 reference support 上 reward selector 的 regret，不是随机软策略或任意 reference 下概率最高动作。compact reward class、统一正 gap、可实现反馈及精确优化限制真实存在；实验 current/reference 各采一个，与理论 iid current-policy slate 不同。有限线性模拟不能承担 LLM 的训练成本/普遍 O(1) 结论。作者保留不同评价对象、拒绝部署外推合理，不将条件定理泛判错误，也不伪称 Books 已逐字承载。

### 2604.17210 — 6分，安全/知识缺口深入：Ch72窄提案通过

实际 [v1 §3 Eq2–3/Alg1](https://arxiv.org/html/2604.17210v1) 与 [abs/v1](https://arxiv.org/abs/2604.17210v1)：冻结 base，比较同一上下文的预选拒绝 token logits，并与任务 CE 联合优化；abs 题名无 HTML 后缀 Preservation，采用 abs 身份。Ch72 当前 Safety Repair 真正承载 attribution→mask/reweight→行为验收，未承载选择性输出锚的对象边界。

可写一窄段：只锚若干 logits 不锚全词表归一化，更不证明序列拒绝；额外 base forward、tokenizer/模板及 λ 都是 artifact/成本责任。少数 logit 不变、其他 logit 上升时其概率下降是审阅者数学推断，不冒充作者受控实验。保留数据/KL/adapter 与最终 safety/utility Gate；不采用“确保安全保持”的无条件口号。

### 2604.17211 — 6分，标准仅报告：通过

实际 [v1 §3.3/Alg1](https://arxiv.org/html/2604.17211v1)：single-stream waveform 的逐帧 LS 来自音频 provenance，LLM speaking 队列单调消费，microphone listening 队列用滚动尾部，混合窗口按此前尾状态拼接。该实现是有贡献的因果输入接口，不应仅因 avatar 标签排除；但 provenance 不证明语义听取或中断 authority。Ch23 已有在线 channel routing/不可撤回输出主线，其 motion/FiLM 实现保留报告即可，不说整个算法已覆盖或 FPS 代表完整系统 SLO。

### 2604.17215 — 6分，安全/知识缺口深入：Ch72窄提案通过

实际 [v1 §3.2/§4 Alg1/Table5、E.6](https://arxiv.org/html/2604.17215v1)：loss 中段预筛，计算候选逐样本梯度，再按与 median norm 的距离取原 batch 的固定比例。它改变监督支持，而 clipping 只改变保留样本的幅度；Ch72 attribution mask 一般原则未明确这组选择职责与 coverage 成本。可在选择性锚后补该分支，不复制方法摘要。

中等 norm 不等安全内容或正确方向；末层相关不能定唯一原因，middle 非显著不能证明无效。表中能力退步、比例非单调与单 H100/Dolly 的额外训练时间限制成立；不把丢弃多数样本写成同比例省算力或普遍安全阈值。保持独立 behavior Gate。

### 2604.17237 — 6分，知识缺口深入：Ch76窄提案通过

实际 [v1 §2.1–2.5/§3.1–3.4](https://arxiv.org/html/2604.17237v1)：标签选择 heads、连续 attention preference objective 和最深所选层截断为同一训练/交付链。Ch76 当前 cross-encoder/生成 reranker→packing 主线没有监督中间读出与执行停点联合 artifact 责任，是真实窄差异，而非仅换算法名。

可补排序交付物分支，绑定权重/head选择/query布局/截层及实际成本；截层只保持所选读出，不承诺 full-model/QA 等价。211 query 派生大量 pair、baseline 上下文差异及监督 reranker 未全面比较要保留；100%格式成功不是 relevance 真值或因果解释。写入应拆开原首段“Packing还要处理”的引句，不能插断其列表。

### 2604.17244 — 6分，标准仅报告：通过

实际 [v1 §4 Eq3–5/Alg1](https://arxiv.org/html/2604.17244v1)：行动候选生成/去重与序列 logprob 代理采样确不同于 token 温度，但代理不是环境信息增益。Eq3 可为负，原 [0,1] 分数声明不成立；softmax 对实数有效，所以不能据此否定其经验。限定任务/额外调用与负例保留，暂不升级为通用探索控制；不以主题相同宣称完整 Existing。

### 2604.17248 — 5分，标准仅报告：通过

实际 [v1 §2/§3](https://arxiv.org/html/2604.17248v1)：真实语音开放输出经 Qwen3-8B 抽取，使用内容控制的 nTVD 与标签置换，v1 确为11模型。Advisory 少量人工抽取核验不延伸到全部任务、HR结果或公平真值；重复说话人/句子与 demographic-irrelevance 假设均限制指标解释。显著分布差异不是全部有害变化或声学因果，不能直接比较不同数据 MCQ 幅度。受限测量保留报告合理，无新增 Books 要求。

## 两项关闭/隔离字段

- **17238**：[当前官方 abs](https://arxiv.org/abs/2604.17238) 实际显示 withdrawn by Jiaqi Zhao，v2 为2026-04-25；不把披露适当性解释为数据错误或全部攻击证伪。实际只读检索 Books 与 Apr21 README 未命中该身份。当前不 selected/评分/Books，必要原始处置依据保留，不读论文正文或新增清理。
- **17249**：[官方 abs/v1](https://arxiv.org/abs/2604.17249v1) Submitted 不是公开时刻。本次实际读取原 raw receipt，该家族 `v1_updated_timestamp_revision_metadata_only=2026-04-21T01:00:06Z` 且 OAI数组为空。此字段不能单独证明晚首发，却不足以支持本窗此前的处理上界组合，精确日期隔离合理；不伪造0分或领域关闭，不为恢复日期审全部正文/版本史。本核验没有重新证明其真实 first-public owner。

## 交付边界

七项为3个窄 Books 提案通过、4个标准仅报告通过；撤回关闭与单项日期隔离各1。审阅者没有写共享正文、复现实验或签日级 Gate。剩余采用工作为协调3个真实写入及写后核验；整日来源、日期和完整候选集合仍由日期 owner 与日级非作者验收。
