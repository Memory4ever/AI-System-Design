# Noisy RLVR 2603.16140：必要原证与具体 owner 差额

作者 resume_mar18，仅03-19补03-18自然日。准入新增是重新核验名义错误标签与matched-question clean/noisy对照修正噪声容忍结论，3+2+3=8，不借一般数据质量原则评分。[精确v1](https://arxiv.org/html/2603.16140v1)必要§2–6/§7–8直接边界与A1–A5/C文字已实际读；不核代码/复现或遍全部图像附件。B两份prompt在HTML仅引导文字，未采用精确prompt或声称实现重放。

## 必要 Source / 支持与关键反侧

§2/Eq1和§3.2区分标注错误与每次随机reward翻转：deterministic verifier面对question-dependent错误gold，与i.i.d. reward flip不是同一人口；同error rate不能移交算法假设。§3.3：Qwen2.5-Math-7B原错误回答池的20项初始人工抽样8实际正确是小样本，不把40%当全池。GPT-5 Pro取得可能多答案，math-verify加GPT-5语义judge、100随机项人工检查并两轮迭代prompt。最终100项零观察judge错误不是整个池真值；作者≤3%@95% CP上界未声明单/双侧，自己的数学检查单侧约2.95%、双侧约3.62%，不照录精确置信保证。9%题干gold不足；总去掉16.4%后12769相同题干分别配clean、noisy、random标签。选择/修复与judge仍可能共源、缺跨独立审计，故“真正100%错”只按该协议限定。

§4：Qwen2.5-Math-7B，batch64/group16/lr5e-7，clean/noisy/format3epochs，random提前停2epochs。数学reward math-verify二值与boxed格式控制，greedy temperature0测试MATH500/AIME24–25/AMC23–24；多次采样pass@k另分责，不从greedy抬升推导能力覆盖。必要文字支持clean对noisy约8.5–10pp、format可更好与pure random低于base的受限结论；response缩短不证明导致能力下降。C按全benchmark平均准确率决定600step/3epoch，存在用评价监测停点的选择边界；random不同训练时长不称匹配总费。

§5/A3–5：Dr.GRPO/TIS/PGFC/DAPO/SAPO与ordinary GRPO，TIS/DAPO upper.28/lower.2、overlong2048/penalty1、TISIScap2，SAPO positive1/negative1.05；PGFC给定已知true noise rate是oracle条件，不能作为线上可估计率保证。50%noise下“没有算法同时在三benchmark超过2pp”不等每算法/每切片没有改善；局部可胜GRPO，不能写一切算法无法补噪声。clean仍局部上界、pass@k未稳定恢复支持协议内反证，不授普遍不可能性或clip因果。

§3.3/§6/C：BIRD随机600中372需改、两位作者复核及分歧追加检查按原叙述，不外推整个BIRD错误率；相同question原/纠正标签对照。多轮SQL和database交互，reward执行结果相等1、缺solution tags−1、其他0；batch64/G16/lr5e-5/LoRAr32/10epochs。SQL停止看训练reward而非mini-dev，以免单集过拟合。Arcwise已纠161/498的mini-dev再作者复核、greedy评估；执行结果相等不证明所有数据库状态的SQL语义等价。所测Qwen3-235B-A22B-Instruct-2507/DeepSeek-V3.1/Qwen3-32B/GPT-OSS120B-A5/Llama3.3-70B，clean对original5.7–12.1pp、PGFC对clean仍5.1–16.3pp且GPTOSS有更差反侧；不归为所有任务或所有noise type规律。

§3.4：≤7B SkyRL/4A100/EPYC7J13/64cores/512GB；>7B Tinker LoRA，完整library版本、precision、每大模型硬件、math LoRA rank、rollout长度/temperature与重复训练seed/CI、端到端token/墙钟成本/服务I/O/concurrency/SLO Not Disclosed。作者实验是训练/评价，不授生产或自己已复现。结论采用：鲁棒性对照须独立审计gold有效集合、verifier与噪声结构、固定题干并分账预算/单次和多样本结果；不采全文普遍“current methods cannot compensate”。

## Actual sole TRAIN-GRPO 与 PRE

已重载ROADMAP与Books合同/上下文/学习理念/写法、LS路由。实际Ch33 50–92/714–754完整 reward→group和verifier-error局部，Ch32/34开篇，Ch27 310–347对应修复/删除交接已读。Ch33 730–752已有组内相关、随机翻转vs固定偏差与policy visitation，不重复这些一般论点；Ch27修复/删除支持保留同输入但不完整承载RLVR噪声容忍实验中“名义wrong pool其实接受其他有效答案”的gold/verifier校准责任。具体缺口是**先核gold有效答案集合与question-matched标注反证，再判断clip/noise correction可否替代数据核验**。唯一owner TRAIN-GRPO，不复制数据pipeline或平台benchmark。

拟插Ch33原相关性例子之后、原“不完美verifier也不等于无法训练”之前；一段及静态来源注。未获独核/窄锁，未写。

### 一段逐字 PRE

测噪声容忍前，还要检查被称作“错误标签”的池是否真与有效答案集合互斥。错误的参考答案、parser 拒绝另一种正确表述与每次随机翻转 reward，是不同信号；先用独立核验修正题干和可接受 gold，保留同一题干的原标注、纠正标注、格式 reward 与随机噪声对照，再在冻结 verifier、更新配方及完整预算下比较，才能判断噪声修正是否在恢复方向，而非利用残留正确监督。一个[受限数学与 Text2SQL 对照](https://arxiv.org/html/2603.16140v1)在重新检查名义错误标签后，所测 clipping 与 noise-correction 变体未稳定追平 clean 标注，不能推广成所有不完美 verifier 都无法学习；judge 的有限抽核、oracle 噪声率和部分不同训练时长也限制结论。Gold 复核、生成/判分、训练与独立评价均付费，greedy 准确率与多次采样覆盖分账；零观察审计错误不等整个池无误，执行结果相等也不等完整 SQL 语义。标注或 correction 假设未验时，保留可信 gold、原 outcome-GRPO 与隔离可疑样本，不用组内标准化或更强 clipping 替标签自行认证。<!-- source-family:SF-2026-ARXIV-2603-16140 -->

### 静态来源注

- `SF-2026-ARXIV-2603-16140` — [exact-v1](https://arxiv.org/html/2603.16140v1)必要§2–6/A1–5/C文字；matched-question gold核验与噪声结构、格式控制/greedy及pass@k分责。有限judge抽核、oracle noise rate、数学停点/不同random时长和SQL执行等价边界保留，不授100%真值、普遍算法不可能性或生产保障；未核代码/复现，未采用HTML未呈现的精确prompt。

## 非写入者 actualPOST（root）

必要Source/PRE沿用resume_review17_18本日正式独核，本root不再重复附件。实际回读Ch33 715–770的完整采样→verifier相关性→有效gold→不完美verifier分支→错误结构邻接，以及章末本人静态注和Tangram/PISmith/TTRL邻注；新741逐字等于通过PRE，静态注精确v1与采用边界准确。插入点先限定“名义错误”对照，再承接不完美verifier仍能学习，未把局部clipping反证升级普遍不可能性，零审计错误/SQL执行/预算边界近文。actualPOST PASS，Ch33窄锁释放，本family可计实际整合，不代替本日日级验收。
