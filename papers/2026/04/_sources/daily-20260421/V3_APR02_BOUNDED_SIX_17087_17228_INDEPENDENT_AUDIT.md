# Apr21 六项必要采用核与一项日期隔离字段

审阅者 apr02；实际访问2026-09-27。只核作者四个指定 batch 的六个已准备家族及17224日期例外；复用此前实际读取且未变化的当前合同，本次对读 ROADMAP、Ch23预算/监督正文、Ch81外部状态分支正文、Ch49双稀疏正文、Ch21辅助损失正文。没有重扫270题摘、全部附件或发表史；没有写 Books、正式日报或作者 notes。

四项6分窄 Books 提案的 source→当前 owner 写前核通过；两项标准仅报告处置通过。此结果不等共享写许可、实际整合、写后核或日级 Gate。

## 17087 EvoComp — Ch23窄提案通过

实际 [official v1 §3.1–3.3/Alg1、Tables1–2/5](https://arxiv.org/html/2604.17087v1)：离线 gold response loss 搜索 mask，随后训练不消费 gold response 的 compressor，部署概率选 token。现 Ch23“固定预算”已有 proxy/阶段/回退，“局部监督”已有完整 teacher 与监督支持，长工具轨迹也明确答案特权；不能说书稿从未讨论特权监督。真正缺的是**同一个视觉 token selector 的构造输入、训练输入与部署输入分账**，可在预算 selector 链窄补一段，不另起算法列表。

48候选/10代仅是离线搜索，不等 compressor 无训练；每语义组保一项不是内容充分证明。Table1–2相对 dense 仍退步，Table5也非所有 loss 变体更差。必须分开标签搜索、compressor训练和线上 selector 成本/可用信息；gold loss 不是视觉真值或部署 oracle。静态/attention selector与dense回退保留。2+2+2=6深入缺口方向成立，实际写后另验。

## 17180 BranchBench — Ch81窄提案通过

实际 [v1 §5.3–5.5](https://arxiv.org/html/2604.17180v1) 与 Ch81“搜索分支必须连同权威外部状态一起分支”及 live-fork 前后：现文已真实拥有 branch identity、COW层次、creation/switch/mutation 与 evaluator revision，并且已有本 family marker，不能误报无正文。可 refine 的窄差异是**创建延迟与活跃分支查询容量分别验收**，而不是再写一般分支隔离。

单活跃分支读不随总分支数下降；多活跃分支才争固定池，独立 per-branch compute 扩量同时扩资源/费用，不能归因纯算法。point/range、mutation、quota、timeout及存储采样/不等完成步骤均限制比较。当前资源取舍段可加共享池vs独立池的 whole-loop预算分支与回退，不采用速度排行榜或“树深自然慢”。2+2+2=6窄增量通过，不重计原已存在的成熟正文为本次实写。

## 17198 Sparse Coiteration Partition — Ch49窄提案通过

实际官方 [PDF/v1 §3.1–3.3/Theorem3.1/§4.2–4.4/§5](https://arxiv.org/pdf/2604.17198v1) 可读方法/代码及反例；当前双稀疏段仅到格式、SIMT decoder、operand-sharing、accumulation，没有 coiteration 访问量的分区合同。单调/层次一致累计成本给出坐标边界，outer intersection 跳子树须先发现有效坐标，再 remap/prefix成本，不能直接用union分区代替。

代价界控制的是该成本函数，不是等 wall-clock；partition、assembly、scatter排序/reduction和metadata要进总账。SpGEMM相对cuSPARSE退步仍成立。可在双稀疏后加一窄条件分支，将实际稀疏访问/匹配坐标归属与总执行时间验收接起来；低skew/稳定格式时静态或vendor kernel仍合理。2+2+2=6缺口通过，不把通用kernel证据当LLM端到端验证。此次PDF截图入口失败、一次本地下载30秒截断，未据残缺本地文件审读；官方PDF文本已读必要范围，不声称视觉页面/实验复现通过。

## 17228 Conditional Depth Routing Auxiliary — Ch21窄提案通过

实际 [v1 §3.3、§4、§5.4/§5.6/§6](https://arxiv.org/html/2604.17228v1) 与 Ch21“Auxiliary loss是代理约束”及前面的条件深度计算：现文已有负载proxy/权重伤任务，不含计算价值teacher的**未来执行策略与实际gate预算匹配**。full/cheap当层分叉后未来全full的稳定标签，不等未来50%full策略下价值；可就近补 stability辅助与quality teacher两种有效性合同。

删除util/rank改善本配置是经验，不证明 mismatch 是唯一原因；λ未扫、on-policy oracle未对照，过强权重解释仍在。0.005非等效证明、25%两seed反向、冻结小backbone限制保留。§4有V100窄壁时而§6.5又称没有，采用已披露的窄配置并指出口径张力，不继承无壁时说法。2+2+2=6窄提案通过，不写所有aux有害或所有深层无需teacher。

## 17219 PAC-Bayes Gibbs Posterior — 5分标准仅报告通过

实际 [v1 §2–3 Assumption2/Theorem5及RLCT解释](https://arxiv.org/html/2604.17219v1)：Gibbs后验平均风险与population-risk积分是对象，不能切换成SGD点估计或Transformer发布证书。MGF/温度/解析与prior假设、RLCT计算责任限制采用；公式不令population量自动可观测。2+1+2=5标准Only合理，不假称条件理论无价值或普遍已反驳；无必须新增Books正文。

## 17221 Bilinear Mamba — 6分标准仅报告通过

实际 [v1 II-B–D、III-C、V/TableV](https://arxiv.org/html/2604.17221v1)：BIM的state-conditioned selectivity破坏这里的affine scan；GM删除这条动态依赖、改input-only gate以复得scan，不是精确等价变换。共享state本身不保证multiplicative computation，两任务排序分离是受限反例。TableV确披露RTX3080Ti/CUDA12.8/PyTorch2.10，不能再称硬件未披露；compile局部时延也不证明实时控制SLO。2+2+2=6标准Only处置合理，保留两条方法，不把库存第三分支回填v1或升级通用SSM选型。

## 17224 — 日期例外字段通过，真实owner未证明

实际 [abs/v1](https://arxiv.org/abs/2604.17224v1) Comments 为ICLR2026 Latent and Implicit Thinking Workshop；[指定OpenReview正文入口](https://openreview.net/pdf?id=ApxoeCZByZ) 本次实际返回challenge。原raw receipt确Updated `2026-04-21T00:58:32Z`、OAI `2026-04-21`，但这些不能排除更早正式家族公开。因此暂不评分/确定selected/Books，恢复只需同家族公开时间与版本身份，不扩发表史。此次只核例外/访问边界，未新核算法坐标争议，也不声称工作坊一定早发。

## 最终交付

四个窄提案写前通过、两个Standard Only通过、一项日期隔离字段通过。实际Books写入仍0（就本审计新增而言），待root共享锁/作者落笔/写后独立核。现有相关正文、先前有效证据与其它已通过审计不重做；此文件不能替代整日来源、日期或冻结分母Gate。
