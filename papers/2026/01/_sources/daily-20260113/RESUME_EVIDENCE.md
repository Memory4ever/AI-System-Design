# Jan13 续跑必要证据

收束补注：05707/05930决定性必要材料已支持恢复准入，root已实际核原方法/反侧及Ch66 110、Ch79 69–75/179承载，通过具体Existing；不是覆盖其10best或10/.7配方。Double状态分层已真实写Ch48并非作者POST通过，原全局lossless/greedy子主张隔离，causal-mask与EM accuracy不补token-law证明。当前处置、冻结50与完整验收以本日README为准，以下‘尚待’为审阅过程快照，不新建平行状态账。

窗口保持 `[2026-01-12T09:00:00+08:00,2026-01-13T09:00:00+08:00)`。本文件是日期局部证据笔记，不替代最终六部分报告；身份、准入、Evidence与Books分别核验，不自授日级Gate。作者：jan13_resume。

## AB5两项决定性补读（2026-10-03）

- [2601.05707v1](https://arxiv.org/html/2601.05707v1)：实际读§2.1–2.5、§3、§4.1–4.4、§5.1–5.2，停止于直接支持/反侧。恢复准入提案2+1+2=5：speech MICL使teacher-forced PPL改善，不足以推出直接转写可用；三个语言的直接生成WER仍高。外声学模型先产生10-best，再联合声学分数与MICL条件log-likelihood，限制最终输出在该候选支持中。Joint decoding表现更佳但每步LM评分更昂贵。仅核Phi-4/Qwen3-Omni、Khinalug/Kichwa/Mboshi；跨语言覆盖和训练总量混杂，attention是诊断而非因果解释，模型跨配置PPL不可比。新知识提案是条件打分与直接生成/候选支持的分责，不是语言应用指标。具体日期/Books/非作者终裁尚待。
- [2601.05930v1](https://arxiv.org/html/2601.05930v1)：实际读§2、§3.4、§6.2与C.4决定性方法，停止于执行人口/评价边界。恢复准入提案2+2+2=6：数据报告经代码profiling、真实执行日志再verbalization；Improvement阶段生成10个候选，以0.7置信门选择，top1真实执行。预测是裁剪候选的filter，不替代真实运行。C.4明确被跳过节点没有test ground truth，所谓decision fidelity只测已执行轨迹，不能支持“安全剪枝”或无漏最优保证。当前关系是通用ML代码搜索的预测/验证分责，不采用AI for Science领域结论，也不把“implicit world model”类比当环境动力学。具体日期、其余标准评价与Books/非作者终裁尚待。

## 日期检查原则

[arXiv官方排程](https://info.arxiv.org/help/availability.html)已核正常 Submitted batch（Jan8T19Z～Jan9T19Z）对应 Jan12 09:00北京时间；官方明确最终ID只在announcement自动分配、不能提前获得。逐ID genuine DataCite registered 提供该ID已公开的上界，不是正文首次公开分钟日志；normal v1 Submitted 与同ID registered 结合，且无具名提前repo/延期相反信号时，采用完全落窗的 `[09:00,registered换算BJT)` **推定公告区间**。推定依据及官方原句见 OFFICIAL_ANNOUNCEMENT_RULE，逐ID字段见FIRST_META、DATES2/3、DATES_AB5_RESUME、DATES_TWO_MISSING。Updated/created、PDF LastModified不单独授公开上界；新cs.CL月页此次可读但只给month listing，不能冒充日级announcement。没有遍历OAI/全年/全部版本，不授无遗漏。

## Double 必要精确性补读

定点读v1 §2.2与D.2，不展开完整理论/附件。§2.2定义 Retrieval Forward 为检索候选再由该模型验证的输出，不是原datastore phrase直接commit；D.2.1明确target causal-mask按同一prefix与逐位置前序guidance算条件分布，greedy的已验证guidance可延长，而stochastic rejection须从residual取replacement并丢弃后续guidance。D.2.2的EM accuracy有小差异，不能称逐token相同或作为distribution proof；主实验batch1，D.1高batch的Nano-Pearl不是Double已集成生产证据。必要原返回core-05524-lossless.txt；状态/采用边界待root核，不能自授通用exact性。
