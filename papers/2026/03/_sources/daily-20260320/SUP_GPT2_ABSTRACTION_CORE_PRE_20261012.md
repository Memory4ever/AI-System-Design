# 2603.17475v1：训练轨迹粒度的必要证据/onePRE

root sole准备，复用本日完整题摘、原5分2+1+2、已核日期与当前身份。实际exact-v1§3.1–3.5、§4.1–4.3、§5/Limitations、必要B.1及C；不读无关文献/所有图/代码。
原证：https://arxiv.org/html/2603.17475v1 。

## 支持与直接反侧

GPT2small12层12头，OpenWebText自回归checkpoint450个/400Ksteps/batch32；主要曲线单seed，作者声明三training runs重复相关行为，不能写只有单run或三架构。测量前缀平均next-token distribution、类内JSD与类间JSD的one-sided Mann–Whitney/p<.001；不同词context并非纯词identity干预、词形等同与均匀prefix权重是协议假设。非零divergence只能说明预测不同，不证明正确类别或内部表示因果。

受测动词类中，有一对class先于item，另一对同时出现；不能概括所有严格先class后item。句法分支class在item变化可见时已出现，但relative-clause不是所有verb同步。heuristic breakpoints用前30步均值+.01，不是普适相变定义。人类认知只是解释性比较，frequency可解释ordering，作者自身保留。early“thinks”信号因替换九embedding verbs消弱，是必须保存的surface-cue反側；更大divergence不自动等语法能力。

count-based对照固定单向10token窗/add.5/stopword去除，以所见target tokens代理trainingstep，不能代表所有memorization算法或与GPT2匹配算力。tracked四prototype nouns由最终模型高prob挑出；英语单架构/局部动词任务，不授所有LLM与训练阶段。RTX/RTX A6000用于作者分析，checkpoint训练硬件/precision/全部费用/SLO未统一披露；450checkpoint储存、distribution读出/词类构造/额外对照/统计均付费，非默认全训练高频探针。

## actualowner / 逐字onePRE（未写）

`TRAIN-PRETRAINING` Ch28，实际完整“从随机参数”/PPL及135–151 PPL比较→音频任务族→目标扩展、Ch27/29入口。旧正文分平均loss与任务族及行为/表示资格，尚未解释同一任务族的类内/类间训练轨迹、同时出现例外和surfacecue反側。拟紧接“不把PPL代事实/代码等”完整段后、音频分族段前，不另Ch66重复。

即使固定任务族，也不应把所有行为当成同一条学习曲线。可在多个checkpoint上，对相同结构的前缀读取下一token分布，分别比较词项之间的类内差异和预定义类别之间的差异，检查类别共性与个体细节是同时形成、先后形成，还是仅由表面提示区分。[受限GPT-2轨迹](https://arxiv.org/html/2603.17475v1)中，部分词类共性先于词项细节出现，另一些同时出现，关系结构又分词类起步；替换固定embedding verb还消除了一个早期假信号。因此分布开始不同不等于正确抽象已经形成，观察顺序也不证明某层机制因果或人类学习过程。更多checkpoint、分布读出、构题与统计增加存储和评价费用；频率、前缀或词形支持不稳时，保留aggregate loss与独立任务基线，重做有界配对，而不从局部英语小模型宣布普遍能力阶段或据此设统一训练课程。<!-- source-family:SF-2026-ARXIV-2603-17475 -->

本人静态注：
- `SF-2026-ARXIV-2603-17475` — Daily `2026-03-20`补查；[exact-v1](https://arxiv.org/html/2603.17475v1)必要§3–5/Limitations、B.1/C。原2+1+2=5，采用class/item训练轨迹的测量粒度；保同时出现例外、surfacecue反侧、frequency/heuristic与count对照预算失配、450checkpoint/3seed单架构及全部费用。不采普适阶段、人类认知/内部因果或训练课程，未核artifact/图像/复现。

待非准备者有限Source/actualowner/onePRE；未写不计I/不授DAY。

## 非准备者有限核验（resume_mar17，2026-10-12）

实际独读exact-v1 §3.1–3.5/§4.1–4.3（L99–228）、§5/结论/Limitations（L229–250）、B.1/C（L367–375）；当前Ch28完整PPL比较→音频任务族→目标扩展L130–155实际顺读。采用的是同任务族类内/类间训练轨迹的测量接口，而非人类认知或统一阶段定律。原onePRE及静态注逐字回对，有限Source/唯一owner/PRE通过；未写未POST、不授I或DAY。

特别核§4.3仅说替换embedding verb减少effect，B.1明确报告早期spike不再出现，因此原PRE“消除了一个早期假信号”只针对这个早期spike成立，不扩大为消除所有表面线索。同时出现类/词项、不同verb类别不同起步、heuristic阈值、frequency替代解释与单英语单架构/三run限制均保留。C只核作者分析硬件/包，未核训练artifact或复现。Ch28旧PPL人口可比/音频任务族不能具体承载同族class/item轨迹及早期surface-cue反侧，原拟落点有差额；没有新增Ch66重复owner。支持和直接反侧已足停止，无需所有图或被引全文。

## 一次非writer actualPOST（resume_mar17，2026-10-12）

实际完整Ch28 L130–162 PPL条件→新145轨迹粒度→音频任务族→目标扩展顺读，末8行本人17475/OptimalSplitting/MUD邻注实际读回。新正文与原onePRE及唯一静态注逐字一致，各仅一份；采用限定与原必要反证近文，未替代PPL或迁作人类认知/统一课程。局部非writer实际POST有限通过，限定diffcheck0，不改Books注验收身份；root接纳后方计I，不授DAY。
