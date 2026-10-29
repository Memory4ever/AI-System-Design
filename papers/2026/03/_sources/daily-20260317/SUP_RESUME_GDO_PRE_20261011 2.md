# GDO12478：必要Source/actual owner与逐字PRE拟案

仅本17补03/16。完整AB/日级身份/去重复用；resume_mar17实际[exact-v1](https://arxiv.org/html/2603.12478v1) §2.1–2.4/Eq1–11、§3.1–3.5/Tables1–5、Appendix A–D/Table6。2+1+2=5，冻结probe的video-dependence描述符与admissibility分离具体差额深入。当前abs显示v2/v3较晚事件但未给具体纠错/撤回说明，版本号本身不触发全版本重读；未核artifact/复现。

## 支持/反侧

六描述符：flow运动幅度、同一q/y在冻结Qwen3-VL-8B有无video的loss差、question-only temporal judgment、多次decode Jaccard、exp(video teacherforced loss)、text/vision/source coverage。均proxy：video loss下降不认证真实时序依赖/正确答案，flow可无关，Jaccard一致不认证真值，question判断不等video确需时间。shared fixed heuristic scorer区别于四goal预设的budget/video ratio/VDSpositive/sourcefloor/temporalquota，分stratum topk reservoir分阶段填满并贯穿dup/QA-per-video cap；不是四scorer、全局最优或learned reward。

LLaVA-OneVision+LLaVA-Video短视频/image池、Qwen3-VL8B/8H20/global8、固定oneepochtrain/eval，但12.9/42.9/33.3/53.3k四subset和512k control不匹配sample/token/训练steps，总descriptor probe/重复decode/flow/clustering/搜索费用未计。不称≥10x墙钟或同compute；precision/visualsample/完整optimizer及servingSLO未披露、不补造。MinLoss/Diverse LVBench负，Temp MVBench负；Table4 Ego多分支退步；Table5移除VDS/PPL/joint在MLVU反而改善，多个goal同变size/video/temporalfloor不授单temporal因果或单调跨任务最好。baseline称每goal10|Sg|但实验统一512k，不能将其自动当四等ratio对照；one fixed endpoint/displayed peak-match不证明训练seed收敛、无统计不确定性。作者声称test identity/answers不入scoring；本轮未核corpus overlap/实现，不能声称leakage已清除。

## actual owner与PRE

Ch27 160–202 data controlplane、250–285 filter/proxy/retention/问答specificity、1267–1275 recipe search/selector全费已具体覆盖普遍data选择及成本原则，不因此拟NC所有增量。尚缺同q/y有无video的冻结probe差额，以及shared ranking与goal-admissibility在static builder分责；Ch28/29开篇与Ch23/24模态表示/生成不拥有subset。唯一TRAIN-DATA。拟在qualityfilter retention说明后/指令视觉表示选择前插两段，未授锁未写：

多模态选样还要区分“答案容易拟合”和“给出的模态确实改变了监督”。一个受限分支对相同question与target answer冻结probe，分别计算有、无video条件的loss，以差值提出video-dependence信号，再与运动、问题级时间需求、答案稳定性和来源覆盖等描述符共同排名。差值只说明该probe在这两种条件下的响应，不认证真实时序依赖、答案正确或独立因果；高motion和多次回答一致也不能签发样本真值。原始row、video/frame采样、target、probe与各描述符版本须共同保存。<!-- source-family:SF-2026-ARXIV-2603-12478 -->

排名之后还要决定哪些样本允许组成训练集合：可以保持同一个scorer，用目标相关的video比例、时间信号最低覆盖、来源floor与分层quota约束选择，而不是把单分数Top-k当成完整mixture。[GDO的有限对照](https://arxiv.org/html/2603.12478v1)支持这种偏好与admissibility分责，但四配置还同时改变子集大小，短video/image训练池对超长video的支持仍有限，部分任务和消融会反退。双条件probe、多次decode、flow/聚类、筛选搜索与后续训练全计费，较少samples或更早达到某个参考分数不等于总compute/墙钟更少。描述符失准、长尾覆盖或净预算回归时，应保留随机/分层集合、原完整池与冻结mixture，并用独立held-out训练结果验收，不让选择器代替trainer objective。<!-- source-family:SF-2026-ARXIV-2603-12478 -->
