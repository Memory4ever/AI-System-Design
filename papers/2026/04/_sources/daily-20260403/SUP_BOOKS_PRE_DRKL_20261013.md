# DRKL：唯一 owner / 逐字 PRE 窄锁申请

Source7分root实际独核通过；未授锁、未写Books。已加载ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、2026 LS路由，以及Ch29 distillation完整局部邻接、Ch28 KL-direction分责/收束与Ch30开篇交接。

唯一owner `TRAIN-SFT` / `books/part-04-training-system/29-sft.md`。现Ch29有gold target修正及forward KL TopK/tail监督：保普通F-KL分解和teacher tail mass加强；Ch28拥有prefix provenance/KL方向通用合同，不复制这里具体target-tail coupling公式。差额是reverse KL中学生tail mass作为权重，导致tail未匹配时target logit仍有压力；forward KL段无法替代此条件化解释。

## 完整前锚（保留不改）

放大 tail 并不证明教师尾部语义更正确，低熵位置 tail 很小、K 过大时高熵噪声的权重反而增加。[Tail-Aware Distillation v1 的有限对照](https://arxiv.org/html/2602.20816v1)支持共同数据/目标下的局部收益与 K 饱和反侧，不认证每一步 tail 总量单调、任意学生收敛或所有任务改善。该路径仍支付完整两模型 forward、概率处理及训练成本，名义 FLOPs 不等总显存/latency；应分别验收 held-out KL、校准与下游行为。Tail 估计/分母不稳、教师偏差放大或收益退步时，保留普通温度/全词表 KD 与原 student，可信 gold 可用时继续采用上述有标签分支。<!-- source-family:SF-2026-ARXIV-2602-20816 -->

## 拟新增两段（逐字 PRE）

Reverse KL 的 target/tail 分账又有不同的耦合。固定相同词表与prefix，令m为reference target，将其余概率归一为p_hat、q_hat；KL(q||p)恰为target-vs-rest二值KL加(1−q_m)KL(q_hat||p_hat)。后项对学生target logit的梯度是−q_m(1−q_m)KL(q_hat||p_hat)：仅target概率相等、tail仍失配时，梯度下降仍会提高target logit；全分布相等时则为零，不能写成教师已被完整匹配后RKL仍必然过度自信。一个条件分支保留二值RKL，却用固定gamma替代学生tail mass，让tail mismatch不再通过这条权重路径提高target confidence；它改变监督耦合，不认证tail语义正确或所有学生都有足够capacity。

[DRKL精确v1的必要机制与对照](https://arxiv.org/html/2604.00223v1)只支持Dolly14k、512token、三组GPT2/OPT teacher/student、同一off-policy teacher responses及训练超参下的局部fidelity/diversity收益。五seed与best-validation checkpoint不等于通用最优目标，gamma过大仍退步；teacher forward、完整词表概率与gamma调节都需计费，不能从局部per-step时间认证全训练省费。应分别保留target/tail KL、生成多样性、校准与held-out行为；tail监督失准或权重导致回归时，保留原RKL/FKL、较弱gamma与原student，而不是用更低KL自签能力。<!-- source-family:SF-2026-ARXIV-2604-00223 -->

## 完整后锚（保留不改）

跨 tokenizer 蒸馏还要先解决监督坐标：同一文本在两端具有不同词表和序列长度，不能按 token 索引直接比较概率。一条分支先用可学习 attention/projector 将两端 hidden states 映入对方输出空间，再分别以 student entropy、投影 teacher 的最大概率及 teacher entropy 提议 token 权重，并以 Soft-DTW 为序列匹配增加单调路径约束；attention entropy 还能提议软 band 宽度，但软惩罚不等于跳过完整 cost matrix，也不认证语义一一对应。词表、prefix、双空间映射、权重与路径共同定义监督，entropy/max-probability 只是代理，不证明学生已懂或教师正确。[受限跨分词对照](https://arxiv.org/html/2602.21669v1)中，band/gate 部分任务退步，强化 DSKD 基线也高于原完整方案；同 batch 的训练步从 .35s/26.38GB 到 .45s/29.92GB，额外 teacher forward、projector warm-up、路径求值与校准均付费，generation seeds 不等于重复训练。映射失配、教师错误被放大或 held-out 行为回归时，保留 sequence-level／统一蒸馏与原 student，不能用更低对齐损失代替任务验收。<!-- source-family:SF-2026-ARXIV-2602-21669 -->

## 本人末注 PRE

- `SF-2026-ARXIV-2604-00223` — Daily2026-04-03补窗；exact-v1 §4.2–4.3/Eq6–9/§5.1–5.3，2+2+3=7。target-only match与full match区分，固定gamma阻断student-tail权重路径；同off-policy teacher responses、Dolly14k/512token、GPT2/OPT三对、五seed/best-val及gamma退化限定。root非作者必要Source通过；此注不自授PRE/POST/DAY，未核artifact或复现。

申请只写上述两段与本人末注，完整前后锚不得改；如root更适合Ch28 owner请先裁决，不跨owner复制。

## 实际独核与写后回执

root实际读Ch29 285–305、Ch28 216–225及Ch30开篇，PRE通过授Ch29指定两段/本人注窄锁，要求正文明确p teacher/q student及m reference非truth，末注只静态证据。作者已按上述修正写入并顺读291–307邻接；root非writer实际读295–307完整邻接、300/302正文和1508本人注，POST PASS，释放锁。forward-tail/跨tokenizer衔接、条件公式、gamma退化与费用边界通过；不授全日、不重写Books注进程状态。作者仅此获锁的Ch29两段及本人注发生Books修改。
