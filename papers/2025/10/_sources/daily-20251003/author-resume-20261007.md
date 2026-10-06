# Oct03 FIRST返修、有限日期恢复与作者READY

作者：Helmholtz / Codex。记录：2026-10-07T22:24:12+08:00。仅新增窗口2025-10-02自然日；原09:00窗口、候选日期/评分及有效审阅不动。本次恢复重读main AGENTS、Research/Report合同、Sources使用说明/每日14源/arXiv、Prompt、ROADMAP与State路由及本日材料。没有catchup、其他日期/Weekly、共享写入或Git写操作。

**AUTHOR READY，非DAY。** 已落实Huygens [FIRST具名返修](review-supplement-20261007.md) R1/R2及九处必要核心边界，完成本日有限日期恢复。当前18题摘为17贡献潜力/1贡献关闭；正式新增候选、评分、正面Evidence采用、Books提案/写入均0。作者普通研究/报告待办0，尚须非作者核实际差额与DAY，README保持进行中。原 [15P/3C首批作者快照](first-calibration-supplement-20261007.md)原样保留，不回写抹掉误判。

## 1. R1实际改判及受影响集合

| 精确身份 | 原作者判断 → 当前处置 | 实际增量、最小支持范围与唯一拟owner |
| --- | --- | --- |
| [VIS-ReAct 2510.02157v1](supplement-20261007/abs-2510.02157v1.txt) | C → P；当前arXiv事件晚于补充日 | 复用Huygens实际读v1 §3–5：程序提取相邻workspace的cluster/highlight/note变化，联合旧报告/变化/当前workspace规划局部编辑。整篇重生成的无关改写与只送delta的上下文丢失 → delta提取与保留上下文的更新接口 → 输入选择/局部编辑范围需重考虑。35对workspace、单模型/单数据集；直接LLM比较不可靠、连续局部编辑积累杂乱、真实意图匹配未知，不授通用一致性。AGENT-CONTEXT |
| [LadderMoE 2510.01651v1](supplement-20261007/abs-2510.01651v1.txt) | C → P；首公开日保留 | 复用Huygens实际读v1 §3.2、§5.1、§5.4–5.5：class token与平均池化图像token作路由，ladder-side top-k专家经可学习gate逐层融合，冻结CLIP、训练adapter/router/gate/decoder。异质输入适配 → 侧路稀疏专家/融合 → 更新位置/专家分配有局部设计增量。无等预算PEFT或通用吞吐证明，稀有类别过滤/非均匀激活保留，OSF与专家数消融不授资源收益。MODEL-MOE |
| [MIMIC 2510.01635v1](supplement-20261007/abs-2510.01635v1.txt) | C保持 | Huygens完整题摘确认persona引导playstyle多样性/游戏覆盖与完成率，未辨识超过策略组合的新执行机制或有成立条件的质量/资源边界。不以游戏、小模型、未知日关闭；未新增日期请求 |

同类误关闭检查限首批3个C，Huygens已全核，作者接受两重开、一保持。原15P全部保留，不因深审成本或日期未知缩池；340月库存不成为逐项队列。30旧身份的去重分母按FIRST澄清为旧8个Atom中的106发现身份：28在原94题摘，01571/02567仅旧发现重叠，不能称已经AB审阅的重复。

## 2. R2中心争议及九处必要core复用

作者实际读回FIRST的R1/R2、§3和日期/来源范围，复用**Huygens实际读取的9个精确v1官方HTML指定章节**；本轮作者没有重抓/重读这9篇全文，没有新增9份HTTP原件，也不声称代码、实验或论文整体Evidence完成。下面是当前禁止强采用/最小支持边界，不是正面采纳后的降分。

### [PSR 2510.01270v1](https://arxiv.org/html/2510.01270v1)

复用§3.2、§4.1–4.5、Limitations。training-free仅基础LLM，MLP轮数预测器仍需训练；最小轮数公式与首次harmful flag标签不等同，**最优安全轮数暂不采用**。§4.2称N=8所有攻击<30%，Table2 Llama3.1-8B-Instruct/CodeChameleon为70.71%，两侧同时保留，不以正文概括消去表反证。二元自评漏判、推理成本和有限攻击范围限制结论；不采用统一低ASR、自适应防御或生产安全保证。保留反思/回退与计算分配潜力，PLATFORM-SECURITY只是拟路由，不是Books已有覆盖。强采用重开需同版本公式/标签澄清、表文冲突解决及拟采用攻击/预算/效用边界；日期恢复不自动解决中心争议。

### [Support Basis 2510.01643v1](https://arxiv.org/html/2510.01643v1)

复用Theorem1.4/1.5、D.3–D.4、G.1、I.1/I.5 Eq44。独立sub-Gaussian单阈值与多阈值/sketch分别承载，后者误差/运行时依赖B、epsilon等，**不采用无条件固定精度近线性/GPU吞吐**。I.1定义b为最小绝对entry，Eq44却以exp(b²)下界归一化项；Huygens推断反例n=2,d=1、Q两行1、K两行-2使b=1、D=2exp(-2)<2exp(1)。这是复核者对该步骤的反例，不是原文实验，也不证明全部路线失败。G.1负epsilon与后文正参数冲突保留。**通用有符号输入定理正面采用隔离**，不以未知日关闭稀疏大项/稠密小项分解潜力。现只有Huygens官方v1 HTML定点核；若拟采用该通用定理，才重开对应PDF证明步骤/作者澄清及依赖结论，不要求现阶段重复全文。MODEL-SELF-ATTENTION拟owner；可供root了解禁止强采用证据，本轮无可写Books正面差额。

其余七处core：两项重开见§1，另五项如下，均保留Huygens实际位置及限制：

| 精确版本 / 复用已读位置 | 当前最小支持与不可采用边界 |
| --- | --- |
| [Privacy 01645 §3.1–3.5、§4.1–4.3](https://arxiv.org/html/2510.01645v1) | 训练记忆、服务存储、RAG/Agent IO、属性推断/聚合是不同风险面；1322为选定8类会议/GPT4.1分类及小样本人核，不等实际威胁发生率。未独立核新闻/法律/服务政策，不采纳预训练泄漏无重大风险的概括 |
| [Quagmires 01624 §2.1–2.2、§3.1–3.2、§4.1及§4.2相关段](https://arxiv.org/html/2510.01624v1) | 数据量/epoch/LR、RL最佳checkpoint与重复例预算需区分；非全部等计算。大k pass/heldout loss预测相关不等因果或普遍规则；仅保留局部配方影响后续RL的反侧 |
| [A-MemGuard 02373 §3.2、§4.1–4.2、§5.1–5.3及§5.4相关表](https://arxiv.org/html/2510.02373v1) | 少数污染/多数可信是前提，共识非独立真值，lesson回写仍有误反馈；Table1 ASRr/ASRt、Table2间接攻击、Table3效用分开。95%不授全部指标/攻击保证，未授自适应串谋安全 |
| [HiSpec 01336 §3.1–3.3、Algorithms1/2、§4–6](https://arxiv.org/html/2510.01336v1) | 中间接受仅缓冲，最终target验证后commit；reject剪KV/hidden state和后缀，周期验证不等跳过最终验证。须训练early-exit层，4H100/HF局部负载非服务吞吐；TopPredictions不证明任意随机采样分布等价 |
| [CLAST 01994 §III-A/B、§IV、§V-A/V-C、§VII](https://arxiv.org/html/2510.01994v1) | LLM注释/名称+AST受限回写，完整重写破坏测试；RQ1为4开源Java项目两类各500测试，非工业RQ1全验证。方法名写入启发式/局部四指标保持不等任意程序语义证明 |

其余6个未知日潜力（M2PO、Optimal Stopping、SCRIBES、IRL Reward、CASAL、Dynamic MoE）未称必要core已读，也不采用摘要数字或强结论；目前没有日级候选或Books采用依赖，深审只在具名日期成立/拟采用命题出现后定点重开，不把日期保留池变强制全文队列。xLSTM/Action Video当前事件晚于日窗，亦未假装深审完成。

## 3. 14身份的实际有限日期恢复

先结构化检查既存14个精确v1 abs原响应的Comments/外链：作者原文直接代码线索仅AMemGuard，arXivLabs/引用工具/基金页不是作者发布。随后实际执行：

- [官方API 14精确v1](supplement-20261007/resume-date-api14.raw)：`id_list`逐项列下表14身份、start0/max_results14；200、实际返回14/14，不翻页。读取identity/published/Comments/journal_ref/link字段；published与既存submitted一致，没有首公告日字段，不能当首次公开证据。Comments的EMNLP/ASE接受也非公开日。
- 五次辅助搜索工具调用，共20个实际query（首14身份、PSR/CLAST第二个同身份query及4具名入口导航）；每query只工具首批、无翻页，返回为各调用合并结果，不虚报各query命中数。真实输入/执行时刻/完整工具返回：[1](supplement-20261007/resume-date-search-1.json)、[2](supplement-20261007/resume-date-search-2.json)、[3](supplement-20261007/resume-date-search-3.json)、[4](supplement-20261007/resume-date-search-4.json)、[5](supplement-20261007/resume-date-search-5.json)。仅身份导航，索引Published/爬取/提交或后出版本不授归属；CLAST缩写query额外返回无关缩写页未采用，不扩来源扫描。
- 实际回到五个具名primary入口：HiSpec作者publication、AMemGuard作者仓库、PSR作者仓库、PSR ACL出版页、CLAST ASE论文事件页，分别保存`resume-date-{hispec-author,amemguard-repo,psr-repo,psr-acl,clast-ase}.{raw,request.json,txt}`。只读同身份日期/公开说明和身份链接，不读全仓库代码、不下载新PDF或扫描会议批次。HiSpec仅2025年，两个仓库没有可采用带日期首次论文公开说明；PSR出版月2025-11，CLAST会议展示2025-11-19均不证明首次正文公开日，也不据此关闭潜力。作者CV年份/文件名、第三方Oct2条目及仓库commit不授公开日。

实际原入口：[HiSpec作者](https://avinkumarut.github.io/publications/)、[AMemGuard仓库](https://github.com/TangciuYueng/AMemGuard/)、[PSR仓库](https://github.com/VietHoang1512/PSR)、[PSR ACL](https://aclanthology.org/2025.findings-emnlp.503/)、[CLAST ASE](https://conf.researchr.org/details/ase-2025/ase-2025-papers/111/Clarifying-Semantics-of-In-Context-Examples-for-Unit-Test-Generation)。真实API参数和URL在[API请求记录](supplement-20261007/resume-date-api14.request.json)，这五页各只执行一请求、无历史分页/代码遍历；没有将所有会议条目列为队列。

本次新增 **6 HTTP请求全部200**，实际起止`2026-10-07T14:19:19.047692+00:00`～`2026-10-07T14:21:15.683089+00:00`，原字节/URL/执行时刻/hash逐项request保存。前一阶段61请求及其59/2统计不覆盖；合并为67请求65个200/2个403，另两阶段辅助查询分别保留。没有API失败/空响应、未读后页或未知日期伪装访问故障；本次不重抓14源/18题摘/九core/340库存。

| 日期保留身份（均v1、P保持） | 真实同身份恢复与停止 |
| --- | --- |
| [01161 M2PO](supplement-20261007/abs-2510.01161v1.txt) | API + 搜索1/5首批；第三方后出引用/RFC非作者首公开，停此 |
| [01270 PSR](supplement-20261007/abs-2510.01270v1.txt) | API + 搜索1/4/5、作者仓库及ACL单论文页；November出版月非首次公开，停此 |
| [01336 HiSpec](supplement-20261007/abs-2510.01336v1.txt) | API + 搜索1、作者publication对应项仅年度，停此 |
| [01394 Optimal Stopping](supplement-20261007/abs-2510.01394v1.txt) | API + 搜索1；作者CV线索只有in-submission2025，未据年恢复具体日，停此 |
| [01624 Quagmires](supplement-20261007/abs-2510.01624v1.txt) | API + 搜索2；索引日期和后出他人引用非原公开证据，停此 |
| [01643 Support Basis](supplement-20261007/abs-2510.01643v1.txt) | API + 搜索2；索引现v2/他人引用非精确v1首公开，停此，中心争议另隔离 |
| [01645 Privacy](supplement-20261007/abs-2510.01645v1.txt) | API + 搜索2；第三方/HF提交型日期非首次公告，停此 |
| [01832 SCRIBES](supplement-20261007/abs-2510.01832v1.txt) | API + 搜索2/5；未返回可采用的同身份Meta带日期发布入口，搜索空不授无事件，停此 |
| [01857 IRL Reward](supplement-20261007/abs-2510.01857v1.txt) | API + 搜索3；后出作者lab奖项页非v1首公开日，未借新版题名覆盖，停此 |
| [01994 CLAST](supplement-20261007/abs-2510.01994v1.txt) | API + 搜索3/4/5、ASE单论文事件页；11/19展示不是首次公开，停此 |
| [02324 CASAL](supplement-20261007/abs-2510.02324v1.txt) | API + 搜索3；HF Sep25与submitted一致、作者CV月/年非具体公开日，停此 |
| [02345 Dynamic MoE](supplement-20261007/abs-2510.02345v1.txt) | API + 搜索3；索引现v4日期/2026作者表不覆盖v1，停此 |
| [02373 A-MemGuard](supplement-20261007/abs-2510.02373v1.txt) | API + 搜索4、作者仓库对应论文；HF Sep29提交型日期、ICML2026接受均不授v1首公开，停此 |
| [01651 LadderMoE](supplement-20261007/abs-2510.01651v1.txt) | API + 搜索4；第三方Oct2提交型条目/年度目录非首公告，停此，贡献按R1重开 |

当前17P =上述14首公开日未知 + 02228/02287/02157三个当前arXiv事件已经BJT10/03提交。后者只在出现同身份更早作者公开稿的真实线索时核那个事件，本轮未对其漫查更早全网。日期不足只隔离当日准入，不改P为C，不记零命中、不为凑候选改日期。

## 4. 安全终态建议与精确重开

上述14项已完成当前具名可用有界入口的必要恢复；没有可采用首公开具体日。建议非作者DAY核本次执行后，将其置**本窗终态保留项**，不是Coverage/Evidence通过。每身份仅一请求：同身份官方历史公告/带日期作者原稿或发布，或能完全落入本日的公开日期范围。材料到达只重开该身份日期准入；落窗成立再评分、证据与具体owner正文比较，中心争议仍另须解决。未知日不关闭贡献，也不授当日候选、正面Evidence、Books、无遗漏或性能/安全保证。

PSR/Support Basis中心强结论按§2独立隔离，不把可读争议包装成外部故障；缺日期不消去反证。Huygens必要反侧阅读已实际完成并复用，非尚未读全文的托辞。Support Basis若不拟正面采用通用定理，则本轮无额外PDF普通待办。17P未采用，不对全部潜力机械全文审阅。

14每日源原有限检查/实际停止及原历史限制保持README §2，不重跑或授全召回；PASTA artifact卡与RBAC未变核心复用Huygens §4与旧root/Euler各自已核范围，旧94/23不重读。Books0的原因是没有日级成立且证据支持的拟采用命题；**未开展owner/邻接正文比较，不称已有覆盖、逐篇No Change或Books无遗漏**。潜力唯一owner不是共享书写入许可或具体覆盖证明。

## 5. 交Huygens的实际DAY差额

请只核R1两重开/17P1C与14未知日3晚事件、R2两中心争议及九core边界真实复用、6新HTTP/五组搜索的具名日期停止、README六节当前结果及隔离/Books0理由。18题摘与此前61请求/八Advanced及旧有效结果复用，不重读18/94/23或340库存，不扩其他日。原作者快照与review不改。作者READY不自署FIRST或DAY通过。

静态/V3、本地links与scoped diff写后结果在本节末追加；没有将机器检查当语义验收。

### 写后核：2026-10-07T22:30:24+08:00

README V3校验通过。新增来源行最初使用本地证据链接、后改同搜索入口触发重复来源，均仅格式错误；最终以实际HiSpec作者入口标表外并链接具名证据，未改公共校验器/合同。README、作者READY和作者停点的本地引用/尾空白/NUL检查无错误；67份HTTP原字节/长度/SHA256与request一致（65个200、2个403）。限定README与本日_sources的diff-check无错误，实际读回限定diff；tracked差额统计只显示README，不误报未tracked原件没有写入。

本次保护的475份既有本日_sources文件逐项hash比较，唯一改变为按计划添加最新停点的`supplement-20261007.md`；其余474份不变，包括原首批判断、Huygens review、运行前副本、61旧阶段原件和原独立结果。本次新增为本作者READY及23个resume-date文件（6×原响应/请求/文本+5组工具返回），不覆盖旧原件。检查只读，未stage/commit/push，未写共享Books/State/合同/索引或其他日期。

供root转交Huygens的实际停点就是本文件§1–5及README六节；工具可见任务列表未提供可确认的Huygens接收线程，未向未知线程发送、未声称已代替非作者DAY。普通作者工作已结束，非作者未裁决前保持进行中。
