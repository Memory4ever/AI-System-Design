# PrivEsc17673：必要 Source 与 sole Ch33 差额准备

准备者：resume20_reader_new。仅本03-20补03-19已准入普通family；原5＝2+1+2、原公开日期/窗口保持，不重准入或增加修订family。此文件为准备，不是独立 Source/PRE PASS；交 resume20_author_new 非preparer核，Books写入仍须 root 唯一窄锁与一次非writer actualPOST。

## 1. 精确版本与受影响范围

首次公开证据复用本日旧独核的身份/日期/准入，实际必要读 [v1](https://arxiv.org/html/2603.17673v1) III-A–E（94–138）、IV（139–155）、V/VI（169–202）、VII及必要cost说明。当前 [abs](https://arxiv.org/abs/2603.17673) 为2026-07-03 v2，四作者与ID相同，但标题、teacher、训练/成本配置及headline结果实际改变。headline为v1 95.8%/比较API Claude Opus4.6/>100x 改为 v2 93.3%/比较API Claude Opus4.7/>80x；两Claude是评价对照，不是teacher。轨迹teacher另从v1 Arcee Trinity-Large-Preview改为v2 DeepSeek V4 Flash，新增trace/reward消融，不能只将版本变化记无信号。只续 [exact-v2](https://arxiv.org/html/2603.17673v2) III-A–D/Eq1–6（140–217）、IV（218–239）、V-A–D（259–313）、VI/VII（314–332）、A必要calibration及TablesV–X（447–533）；不全版本diff，不读所有interaction/prompt附件，不核artifact、代码或复现。v2作为原family受影响结论的纠偏依赖，不把July内容迁为03-19新的公开事件、不重复评分。

## 2. 必要机制、比较、直接反侧与费用

- 固定harness定义round为一次模型调用及其工具执行，可在同一round并发多call；一次run从新isolated container开始，到独立验证目标或cap结束。v2以目标端每run随机canary验证终态，不以工具文字/子环境特权状态自报成功。该评价的120 valid runs＝12固定scenario×每格10次，primary20round/max60，是per-run budgeted success，不是best-of-k；共享12scenario的人口不能由run-level WilsonCI扩成未知环境覆盖。
- v1成功teacher轨迹→SFT→自身交互RL不是新算法；v2 teacher更换、2000/200 balanced traces、6种guided/unguided×reasoning形式，在procedural holdout选择。TableII/IX同SFT设置/500holdout runs：unguided-long73.2高于guided-long65.2；trace长度/探索与hidden信息同时变化，不能唯一归因为reasoning文字或宣布所有privilegedteacher无用。组内标准差/异步clip实现只记录披露，未证明精确GRPO/AIPO等价或收敛。
- procedural训练10family与静态eval按具体值/trace排除分离；v2还声明train/holdout不同parameter pools。共享canonical结构、近family任务不证明预训练无污染；10covered、1无directanalog、1withheld-family必须分别解释。v2 headline112/120，8失败全在withheld-family，2/10@20与3/10@60；局部4B可行性不是普遍OOD可靠性或真实安全。旧v1数字不覆盖v2新recipe。
- v2 Eq1–6保verified outcome为核心；round shaping只成功episode按首次成功round附加有界奖励，却把并行fan-out藏进一次round。cost shaping亦仅成功episode附加[0,1]项、lambda=.1；C加总逐LLM与每个tool的clipped measured latency，tool并行仍相加，不等于wall-clock、完整账费或生产SLO。per-call clip/Cref由训练前100timing traces（74success）校准，H100 concurrency与服务负载进入reward身份；0/74校准饱和与0.38%训练饱和是该配置统计，不证明所有负载无失真或最优策略不变。interface罚每episode至多一次，与成功判据分责。
- 同SFT初始化、1000step四reward比较在procedural holdout选checkpoint。TableX peak/final分别Outcome88/83、+Round90/75、+Cost90/87、+Round+Cost87/79；round早期收益后反退，cost也非完全稳定，不按point estimate授普遍显著优胜。作者shortcut/reward-hacking解释是与轨迹形态相容的解释，不是唯一内部因果证明；更换reward后必须重验heldout，不能由更少round自签更高效或可靠。
- v2 Qwen家族vLLM BF16/32k/context、2048output，API128k/200k与sampling/reasoning不同；本地commodity仅inference。SFT4H100约1h41、RL4H100约11.5h deployed step300/1000，成本不只单卡推理。A cost为RTX5090/concurrency16 batched serving、50%util/amortization+electricity估算，明示排除orchestration/Docker/tool latency/download/cold-start；按budget20每runcost除success率。$120.80一次selected训练spend/约700success摊销不是teacher、6-way/SFT/rank/LR/reward搜索、环境生成/holdout/全部失败与维护的TCO。v1 RTX4090无batch测量与v2不能拼成同一倍率。全部比较保留作者setup估算性质，不核未来价格、实际流量、尾延迟或第三方部署。
- 所有必要读取只是有界isolated研究评价，未执行任何攻击、访问真实第三方系统或采用payload。Books不落攻击步骤，只落reward measurement接口、评价人口与成本分责。

## 3. Actual唯一owner差额与原两PRE

实际读 ROADMAP/PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、本日最新路由与 Ch33开篇/703–734 verifier、930–1025 measurement→reasoningcost、2362–2426 tool feedback/conditioning/compute、Ch32/34入口。Ch70当前resource_time、total experiment family cost、state-dependent Agent work、good_request与successful_goal分母、utilization/idle已经承载成本原理，不重复另写Ch70；Ch78工具效用不负责RL reward变换。本family sole `TRAIN-GRPO` / Ch33：原Measurement完整930–962后、长上下文RL标题964前。旧正文有测量噪声/正确性gate，但没有round同单位隐藏parallel fan-out→成功门控call-latency shaping→独立holdout反退这条具体界面链。只增加以下两段，沿measurement而非领域/算法名堆砌；原pureRL/multi-stage与后续artifact主线保留。

### 正文PRE 1

交互预算的单位也可能藏住被优化的资源：若一次 round 是一条模型回复及其全部并行工具调用，减少 round 不等于减少工具执行、模型时间或账费。可保留独立验证的终局 outcome，再只对成功 episode 加入有界效率 shaping；一条受限分支按每次模型与每个工具的实测 latency 分别截断后相加，让同 round 的 fan-out 仍付出代价。这个和是资源占用代理，不是并行执行的 wall-clock 或完整服务成本；clip、参考预算、负载与并发校准都进入 reward identity，不能由“真实计时”忽略基础设施噪声。<!-- source-family:SF-2026-ARXIV-2603-17673 -->

### 正文PRE 2

换成更贴近资源的 shaping 仍需验证 policy，而不是只看训练分数。[PrivEsc 的当前受影响消融](https://arxiv.org/html/2603.17673v2)中，round 奖励的早期收益随后退到 outcome-only 以下，latency 分支也未完全保持峰值；这是固定4B、procedural holdout和工具接口下的反侧，不证明计时奖励普遍优胜或最优策略不变。训练选择与静态终评保持分离，并按既定预算、目标端成功谓词和未见 family 分别验收；已覆盖场景高成功率不授未知环境可靠性。环境、teacher traces、校准、各 reward 搜索与失败 rollout 都付费，单卡 serving 估算不覆盖训练和工具TCO。接口或资源代理失配时，保留原 outcome-only、明确硬预算与独立终态检查，不由更短轨迹批准部署。<!-- source-family:SF-2026-ARXIV-2603-17673 -->

### 静态PRE

- `PrivEsc17673 / SF-2026-ARXIV-2603-17673`：[v1](https://arxiv.org/html/2603.17673v1)接口/训练/固定预算评价与成本、[v2](https://arxiv.org/html/2603.17673v2)受影响III-D/Eq1–6、V-B/TableX、A校准/计时设置/费用经必要有限读取；sole `TRAIN-GRPO` 两段只采用round合并parallel fan-out与成功门控clipped call-latency shaping的分责，保holdout反退/计时噪声、未知family失败、预算/CI人口与全费用。不采用旧headline/跨版本倍率、完整算法等价、最优策略/普遍可靠或真实安全；无artifact核验/复现/攻击执行。独立Source/PRE与实际POST状态只由原packet对应节记录，未完成不得计整合。

## 4. 交接

两literal/static只是prepared，resume20_reader_new不自核、不自授窄锁、不写Books或计I/DAY。交作者非preparer必要Source/actualowner/PRE有限核；通过后root协调唯一Ch33 narrow writer与一次非writer实际完整邻接/本人及邻注POST。原5/date与受影响July依赖分账不变。

## 5. 非准备者必要 Source / actual owner / 两PRE有限核

2026-10-12，resume20_author_new（非本packet准备者）实际回读v1 III-A/C/D、v2 III-A–D/Eq1–6、V-A–D和A必要calibration/配置/TablesIX–X，复用原准入/date层，不全版本diff或展开攻击/prompt附件。v1 teacher Arcee Trinity-Large-Preview与v2 III-C/Teacher Inference的DeepSeek V4 Flash已核；原§1把Claude角色混为teacher的notes经指出后已改，Claude4.6/4.7只作评价API。此纠偏不改变两个literal或静态PRE，也不把July修订迁成本补日事件。

Eq3/4的成功门控、逐模型/每工具latency截断和相加，与round藏parallel fan-out的差额成立；Eq6四reward共享终局项，interface penalty每episode一次，不采用原文“uniform term不影响ranking”作为不同policy环境状态下的保证。TableX的round90→75、outcome88→83、cost90→87是必要直接反侧，正文正确保holdout反退而未将§VI“holds peak”升格。固定12×10 valid runs与withheld-family八次失败、训练选择不使用static final人口及所有费用分责支持原两PRE；计时不是TCO、并行wall-clock或policy-invariance证书。

actual sole `TRAIN-GRPO` Ch33 917–969完整顺读：Measurement930–962正确性gate/噪声/校准原论点之后、长上下文RL标题之前承接两段，保原论证和后续context verifier分责；邻Ch32/34入口与Ch33本人/邻注末12已读。正文不含攻击步骤，不写Ch70既有TCO原理。两literal/static有限PASS；尚未写Books，不计I或DAY，root授具体Ch33窄锁后方可写，写后只做一次非writer实际邻接/本人末注POST。

## 6. root窄锁下writer落实

2026-10-12 root接纳§5采用资格并授本family soleCh33锁，resume20_author_new按§3两literal/static写964/966与本人3254。writer实际Measurement930–982完整邻接与3242–3254本人/邻注顺读：噪声校准→round/resource单位→独立holdout反退→context是否使用的不同verifier主线保留；两literal/static各唯一一次。限定diffcheck0，无攻击步骤、外部执行或第二owner，不stage/commit/push。准备者reader作为非writer仅做一次实际完整邻接/本人注POST；独立Source由§5非准备者提供，不循环身份静态注，不预I/DAY。

## 7. resume20_reader_new一次非writer实际POST

本packet准备者在此仅作为非writer核实际变更；必要Source/PRE采用资格复用作者非preparer§5，不自核源。实际完整Ch33 930–992 Measurement全部→原两新964/966→长上下文RL完整context论点/下节标题，以及3242–3254本人与全部局部邻注顺读。两literal/static机械逐字唯一各1（964/966/3254），限定六新增/cached与unstaged check0；噪声校准到round单位及call-resource shaping，再交接context使用的不同验收对象，原verifier/measurement链完整。v2依赖/旧family date、success门控、clip/并行wall-clock与TCO不等、holdout反退/withheldfamily及全费仍近文，未写攻击步骤或第二owner。**一次有限actualPOST PASS**，交root接纳释放Ch33，不自计I/DAY，不重Source或循环改static身份。
