# Apr20 三项有限非作者处置复核

复核者：apr02。实际复用本轮已读且未变的必要原文，并重新打开官方 exact-v1 HTML 与 Ch27 数据监督、Ch76 图路径、Ch29 蒸馏相邻正文。只核拟采用命题、关键反证及具体 owner；未复现、未核本日日期或日级 Gate，不写 Books。

## 15675 C-Mining：5 分标准，仅报告通过

[官方 v1](https://arxiv.org/html/2604.15675v1) §3.1–3.4、§4 和 Tables1/3 的几何 seed 选择及局部对照支持报告。Eq2 对 cosine 行归一不能保证非负、非零分母，因此不能将该 entropy 普遍称合法概率熵。Table1 的 77.12→80.94 为 3.82pp，不是文字 3.13；Table3 random 分支反收益须保留。语言聚簇与专家评分不足以升级文化真值或全成本保证。Ch27 已有 actual supervision、teacher 与固定预算分权，但不称整个算法已有覆盖；受限选择机制保留报告即可。

## 15676 EvoRAG：6 分纠错深入，中央保证窄争议通过

[官方 v1](https://arxiv.org/html/2604.15676v1) §4.3 Eq3/4 为归一化路径几何均值上的效用目标；Eq5 额外乘路径概率积，不能由该目标推出。两条单边路径 p=(.2,.8)、alpha=.5、U=(1,0) 时 E=.6、V1=.16，正确导数为 −1/3，打印式为 −1/15。相同效用也不保证唯一最优，E→0 不支持统一有界 logloss。隔离 exact-gradient、唯一/稳定收敛和无条件噪声保证；不否定反馈粒度机制或局部经验。Ch76 的真实路径与事实 authority 分权不能充当全算法覆盖。暂缓采用这些中心保证，重开需一致公式/合法归一与明确假设，不展开全部附录。

## 15701 MoLSAKI：5 分标准，仅报告通过，修两处披露

[官方 v1](https://arxiv.org/html/2604.15701v1) §3、§4.6、F.2/F.3/F.5 支持相同文本/key 集合下的逐步、跨层 attention 监督；不支持任意 tokenizer/teacher 无条件对齐或 attention 因果归因。Hybrid 39.3<Unified 40.5 保留；teacher feature 生成与 materialization 不在学生 FLOPs 内。作者旧 notes 两处需纠正：F.2 明确单 NVIDIA A800、batch16，并报告三次随机运行均值，不能写硬件/重复运行均未披露；CI 仍未给。F.3 第二阶段对原先 teacher 答错的样本使用 ground-truth answer，不能把全部监督描述为只筛正确 teacher CoT。Ch29 现监督路径、估计器与 held-out 行为分权已承载采用原则，但局部 MoL 配方仍仅报告，不假称整个实现 Existing。

结论：三项窄处置通过；15701 的 F.2/F.3 披露修正须同步作者记录。除此之外无新增 Books 或本组普通复核待办，日期与全日验收不在本次范围。
