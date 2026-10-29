# AdCo 整体 PRE 请求（未写 Books）

Owner `AGENT-MULTI-AGENT`，Ch82 `books/part-07-agent/82-multi-agent.md`。已读实际peer选择段及直接前后、Ch81 durable执行和Ch83协议交接。现有MACE段选择哪个peer，不承担同一worker这轮吸收proposal还是请求批评的动作选择；故是一个窄差额，非再次解释bandit/多数票。精确v1/日门/2+1+2=5与支持/反侧见EVIDENCE及reader R4。请求sole reader整体核本完整新增/独立marker/完整直接邻接/本人注，仅该两位置，不锁全章。

## 直接前邻接（完整原段）

Peer selector 只拥有委派决策，不拥有最终求解或 verifier。探索会把一部分请求交给不确定 peer，获得长期信息的
同时增加当下失败、延迟和不公平负载；短任务、不可逆动作或强 SLO 下应缩小探索甚至退回静态路由。该机制也不
证明局部选择能得到联合最优 topology，更不能据少量 peer 实验外推到超大规模多 Agent。

## 拟完整新增

选哪个同伴与怎样消费同伴反馈，还可以是两个控制对象。固定全协作或全批评容易实现；若粗过程分数能辨认局部变化，可按过往分数增量更新两种动作的收益统计，在探索预算内决定本轮吸收同伴解法还是邀请批评，再分别用上一轮分数或历史平均分数选peer。[AdCo的受限数学对照](https://arxiv.org/html/2510.18179v1#S2)支持这种动作与peer选择的分工，不证明当前推理状态已有准确价值函数或继承经典UCB保证。粗PRM并非独立真值，升级worker仍可能被多数票抵消；反复评分、通信、所有模型调用和等待均计费，局部改答数不等端到端效率。反馈失准、共享盲点或净收益不足时，保留固定小协议、独立候选与外部验答，不由更高过程分数或一致答案批准事实正确。

<!-- source-family:SF-2025-ARXIV-2510-18179 -->

## 直接后邻接（完整原段）

静态能力描述不足时，还可在真正委派前向候选的本地知识库请求一份相关性回执，而不是立即让每个Agent生成完整答案。[受限的KB探测分支](https://arxiv.org/html/2509.19599v1)先查路由缓存，再用card置信提出是否并行probe；本地检索返回的OK、KO或Partial只是这次请求下的能力证据，不是任务已完成、内容正确或调用权限。缓存应保存并消费这份有类型的判定，不能因记录非空就把旧KO/Partial变成OK；相似query还须核原principal、KB与encoder版本和失效范围，不能用embedding接近替共享权限。单一肯定只提议handoff，多个肯定仍需消歧，真实执行与outcome另验；少传正文也不排除query或回执泄露主题存在性。原对照只测合成企业题的路由，未启用语义cache，不能用准确率提高担保缓存摊销、失效正确或总体更便宜。全部卡片/KB制备、并行检索与通信、缓存维护、消歧和任务/隐私回归均计费；证据过期、回执不可信或探测预算不合时，保留固定已验小池、重新检索与澄清，不让高confidence或一个ACK自行批准委派与effect。

<!-- source-family:SF-2025-ARXIV-2509-19599 -->

## 拟本人注

在 `## Review notes` 后、原第一注之前，仅新增：

- `SF-2025-ARXIV-2510-18179` — Locke，Daily2025-10-23补Oct22；[exact-v1](https://arxiv.org/html/2510.18179v1)§2/A.1/A.5.3支持与reader R4首次必要§3–4/A.5/A.7反侧，2+1+2=5，动作选择/peer消费差额深入。保粗PRM非外部truth、状态探索/理论未来、强worker/majority反退和全部调用/通信等待费用，不采普遍鲁棒或UCB保证；未核实现/图像/复现。实际PRE/SAVE/self-read/sole actualPOST仅以本日canonical后到事实为准，不由本注预签。

未发生真实Books SAVE/自读/POST。
