# CoVerRL17775：共识伪标签与同模型验证的训练回路 / 必要准备

resume_review17_18，2026-10-12，仅03-20补03-19，author明确sole分配。actual README94/八Agent§47–51已核正确ID **2603.17775v1**，不是另一篇RVV/xDSL17800；原2+2+2=6、准入/date§5有效复用，不由Submitted单独证明落窗。本稿不自Source/PRE PASS/safe/DAY，交author非准备者必要裁。

## 1. 已实际必要Source与停止

[exact-v1 HTML](https://arxiv.org/html/2603.17775v1)完整AB/关键引言L68–103，§3/Eq1–3 L112–151，§4设置/主评价/T1–4 L152–272；A直接预算/clip差别L353–391，B Algorithm1完整L392–447，D直接消融/样本与reward统计L548–588。current abs8–30同题九作者、完整AB、v2与Comments仅project/code实际轻量核；无具体重要纠错说明，不机械重读v2或全diff。HTML日期模板Aug24不搬材料归属。只偶然返回并读到C末L524–544，不用它签全证明；未读完整C、case图像、References、代码/复现。支持本接口及直接反侧足即止，不扩query或附件。

## 2. 实际回路与残余失效

同一policy切generator/verifier角色：同题采样按答案频率划majority正集和其他负集；只对正集至多M条验证，正判断严格超过一半才保留**题目及关联训练集**，不是逐条删除所有错误轨迹。正集目标为Correct；负侧取最低频答案，采同数量verification目标为Incorrect。判负触发K条修订，生成/修订的正确reward仍按原majority伪答案，不是外部真值。format与accuracy相加，不能混为独立correctness。正verification不同solution prefix但共享answer，AA-GRPO将其并组；其他生成/负verification/每个correction集按各自group。该分组改变条件人口，不与同prompt组自动等价或无偏。

因此多数答案若错而verifier也接受，错误仍保留并奖励；真实正确的稀少答案也可能被负监督。给同模型两个角色不构成独立truth oracle。B最低频负集的选择对Y−为空/全一致、tie和零std的完整guard没有给出，不采用精确全输入recipe；本文并非因此整体无贡献。拟采有限伪标签准入和角色/分组分责，不采必然逃离共识陷阱、保持多样性/稳定性或自验即正确。若要重开这些强主张，只一次请求共错/稀少真答案/all-consensus下的分组与guard记录、保留/拒绝人口以及独立gold评价，不为全部代码/版本史建立队列。

## 3. 关键对照 / 直接反侧 / 成本

MATH训练，Qwen3-1.7B-Base thinking、Llama3.2-3B-Instruct、Qwen2.5-7B；MATH500/AMC/AIME24与GPQA-Diamond，16不同generation平均first/final（后者verify/revise后），不是16独立训练seeds。T1作者有限主表均比TTRL高，但T2 Llama GPQA selfverification56.9→55.2反退，不能把55→85当所有模型/benchmark提升或独立真值。RewardBench只mathprm、部分leaderboard来自外部，不授同配置大模型替代。图3–8仅必要caption/正文观察，不冒像素读、独立内部机制或全checkpoint保证。

TTRL首轮64采32训练；CoVer32采16，后续verification/correction全用，M8/K6。clip-high .28对TTRL .2，A8Kprompt/2Kresponse、temp1/validation.6、lr5e−7与KL同披露，但全token、各role/过滤成本、硬件/precision/并发/墙钟/SLO/训练重复与CI未闭合。D3 total perstep约2172–2467对2048，只是样本量“comparable”，不是严格总费/compute等预算；角色样本长度亦不同。全原路径、验证、修订、过滤及独立评价都计费。

T4去AA组同时改为单一positive solution随机采样，不能将收益唯一归并组；TTRL+PAG还同时改变PPO/GRPO与归一，all-reject collapse不单独证明balance充分。D1不选最低频负例时MATHfinal72.0>71.9、AMC39.8>38.6；D2叠固定过滤有升退，GPQA31.6<33.6。因此不用部分消融认证唯一最优、全任务无损或“每role一直>90%”；D3 Qwen7B verification.8688/correction.8518/total.8768即限制这种泛化。保有限实验支持，不降分或虚NC。

## 4. actual唯一owner / 差额 / 两literal PRE

sole `TRAIN-GRPO`，[Ch33](../../../../../books/part-04-training-system/33-grpo.md)：actual完整50–86同prompt/reward源/latent共识/CRAFT及164–205 clipping实际读；Ch32/34入口1–24实际交接。已覆盖一致性不是真值、latent同错及条件group原则；缺同policy两角色以多数答案训练verifier、反向控制题目准入与答案anchor分组的闭环责任。本拟原72 latent一致性成本/回退完整段后、74有安全标签的prototype分支前两短段，不复制新算法库存或DPO推导；非preparer可裁specific NC/缩稿。

没有外部答案时，另一条受限分支让同一 policy 交替生成解法与验证解法：先以多数答案产生伪标签，再由 verifier 对多数集合的有限样本判断，只有多数验证接受才保留该题进入训练；多数集合作正监督，另一答案作负监督，判负的解法可再产生修订。[有限双角色训练](https://arxiv.org/html/2603.17775v1)把伪标签选择和模型更新连成回路，却没有创造独立真值。修订仍按原伪答案领奖；若多数答案与 verifier 同错，错误可继续被强化，少数正确解也可能被当负例。应分别保留原答案频率、验证判断、保留/拒绝人口与独立正确性检查，不以“相互改进”名称签发可靠自监督。<!-- source-family:SF-2026-ARXIV-2603-17775 -->

这里的组也不一定共享同一 prompt：正 verification 可以在不同解法 prefix 下按同一答案 anchor 合组，其他角色仍各自归一；题目过滤和分组同时改变训练支持，不能把组内标准化读成独立、无偏或稳定性保证。原对照的采样数、后续验证/修订预算与 clipping 不同，消融也有质量反退和共同干预；训练、过滤、修订及独立评价均须计入成本。共错、答案人口退化或 verifier 失准时，保留可核 gold/outcome 信号、原同 prompt GRPO 和明确的过滤记录，而不是继续用更高共识或同模型自验作为正确性发布条件。<!-- source-family:SF-2026-ARXIV-2603-17775 -->

静态源注：

- `SF-2026-ARXIV-2603-17775` — [CoVerRL exact-v1](https://arxiv.org/html/2603.17775v1)必要§3–4/Eq1–3/T1–4、A预算、B Algorithm1及D直接消融/样本统计。仅多数伪标签→同policy验证/题目过滤→双角色更新及answer-anchor分组的有限接口；保共错/稀少真答案风险、反退、预算/clip与分组消融混杂、全费用。未采独立truth、必破trap、精确全输入guard/隐式DPO或普遍稳定保证；未核代码、全部理论图像或复现。

## 5. 待非准备者裁

交resume_mar17一次必要Source/actualowner/两literal+static；准备者不自核或计safe，root未授family锁不写Books/Report/LS，不授DAY。只恢复实际受影响命题，不重复全部附件。

2026-10-12 resume_mar17 非preparer实际必要Source/PRE有限PASS：独读exact-v1§3/Eq1–3 L112–151、§4设置/主T1–4与直接消融L152–272、A预算/clip L353–391、B Algorithm1 L392–447与D1–3直接反侧/样本统计L548–588；current abs同题九作者/v2项目说明实际轻量读，未见具体纠错，不机械全diff。返回的C部分不授完整证明或DPO等价。实际Ch33完整50–86及clipping164–205、Ch32/34入口1–24，逐字两PRE和static回对。多数验证严格大于半数是题目准入，非逐路径可靠过滤；负侧最低频与原多数修订reward、跨prefix正verification组均与原证一致。共同错误/稀少真答案、空负集/零std guards不授recipe；T2 Llama GPQA反退、T4 AA消融同时改单positive采样、D3 Qwen7B各role低于90%、采样与clip预算差额保持。原具体闭环不由旧latent一致性/同prompt原则完整承载，允许sole TRAIN-GRPO原latent回退段后两段有限分采；原6不变。未写未POST不计safe/DAY，待root窄锁；未核代码/全理论/复现。

## 6. root授权后的实际窄写 / writer检查

root明确授resume_review17_18 sole Ch33 family17775两literal/static锁后，实际顺读现latent成本/回退完整段→CRAFT邻接，再仅原两PRE写正文74/76与末static3240。writer实际完整64–95及3234–3240本人/CRAFT/AR-CoPO/RewardFlow邻注回读，与§4 literal一致；scoped实际差额仅本family两段及一静态注六新增行，文件diff-check0，其他既有/并发内容保留，不代验收。写者读回不是nonwriterPOST，交resume_mar17一次真实POST，root接纳后释放；不计safe或DAY、不改静态身份。

## 7. 一次非writer实际POST

2026-10-12 resume_mar17实际顺读Ch33完整60–99与3232–3240本人/CRAFT/AR-CoPO/RewardFlow静态注邻接，逐字回对§4两literal PRE及§5有效必要原证，有限POST通过。新74/76准确区分多数伪标签、同policy多数验证的题目准入、负侧修订仍沿原伪答案与跨prefix answer-anchor分组；共错/稀少真答案、支持人口/预算/clip差额、独立正确性及全费用边界近文保留。前接latent共识失败/回退、后接有安全标签的prototype分支与同prompt原则，没有把同模型验证当独立truth或因果保证；本人3240范围与未核代码/完整理论/复现准确。只验收本family实际两段/完整邻接/静态注，未改Books或注身份，不自授DAY；交root接纳与释放Ch33窄锁。
