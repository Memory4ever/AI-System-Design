# EOSER/ASS/CJ-GRPO：Sep28原作者code-release单篇包

## 1. 准备即交的事件事实

本日actual从精确v1完整AB的原code链接进入[原作者仓库](https://github.com/yjyddq/EOSER-ASS-RL)，README Updates实际明确09-28-2025发布该研究代码、09-30-2025发布paper，03-09-2026是后来loss-backward省GPU-memory变更。Citation同四作者/2509.23924，原paper链接同家族。**Sep28是代码release原作者date-only事件，不是Submitted所授arXiv first；Sep30论文发布/2026优化分责，不要求额外TZ或同PDFbytes。** 当前代码/README不能不经具体版本核验就当全部Sep28原实现。

本篇已保存FIRST§8的精确v1完整题摘与current角色，24小批尚待reader。AR rollout/优化按token概率分解不适合MDLM的noncausal路径→CJ-GRPO轨迹一致性与EOS early rejection/ascending step-size→diffusion采样/优化路径和质量/step预算。若事件身份及准入通过，拟2+1+2=5，仅这条具体局部机制，不借成熟GRPO或release名加分。必要方法/评价、正确性反侧与具体owner仍普通，未先formal/完成Source/Books。

请root内部即时供Feynman单篇核原Sep28 release事件权限/窄准入与评分提案，不等其它35未知日或全Source。本人继续必要v1与release适用域；无Books锁/写入、不发送UI线程消息，不预支DAY/FINAL或计数。

## 2. 必要历史artifact已经有限取得（新变化层）

Feynman§12事件/5分与必要v1/当前采样反侧已actual读回，直接复用。为避免把current实现投回当日，仅官方repo commits API以Sep28BJT末界为until、per_page3取得三条README提交，未遍历历史。选最晚返回commit [549e094ed5ef5924fa20c24614d29e4ad1ec71b3](https://github.com/yjyddq/EOSER-ASS-RL/commit/549e094ed5ef5924fa20c24614d29e4ad1ec71b3)，author/committer均Sep27T17:38:49Z＝Sep28BJT；**commit时间只选artifact，日门仍以原作者发布声明，非repo创建/提交日期自动当公开。** [请求](SUP_curl-eoser-release-commits_20261013.request.json)200/exit0、9556bytes。

精确commit [README](https://github.com/yjyddq/EOSER-ASS-RL/blob/549e094ed5ef5924fa20c24614d29e4ad1ec71b3/README.md)实际4436bytes，已有Sep28发布code、paper仍TBD；根tree只读README/cj-grpo/eval身份，未下载dataset/权重或别后端。[原README](SUP_curl-eoser-release-readme_20261013.raw)、[根tree](SUP_curl-eoser-release-tree_20261013.raw)、[CJ目录tree](SUP_curl-eoser-release-cj-tree_20261013.raw)均200/exit0。具体两个发布版文件eval/generate.py 22688bytes、cj-grpo/cj_grpo_trainer_eoser_ass.py 38826bytes取得200/exit0，只下述必要函数/接口实际读，未声称全部代码审计/运行。

## 3. 受影响机制/兼容域

[精确v1](https://arxiv.org/html/2509.23924v1)§3.2–3.4/Eqs4–11/Alg1 actual读：EOSER仅降低EOS候选提交confidence，不硬禁止EOS、不重归一化完整vocab；ASS按1,2,4…末补一token，末token不必EOS。CJ在实际partially-masked状态求当步新unmask位置的条件概率，再用组终奖构造advantage。不是只拿最终全填序列重算概率。score5仅这些局部非因果路径/状态对象与采样budget选择，非普适PPO定理。

发布版[generate.py](https://github.com/yjyddq/EOSER-ASS-RL/blob/549e094ed5ef5924fa20c24614d29e4ad1ec71b3/eval/generate.py) sampling/ass_sampling/get_num_transfer_tokens_ass actual读：先sample candidate token，再给其EOS confidence乘衰减，top-k提交的是位置选择，不修改候选token为non-EOS。**发布版ass_sampling已经用累计 `(2^(s+1)-1)/2^S`，而原论文Eq7是单步 `2^s/2^S`/末 `(2^s+1)/2^S`。** 所以该差额不只是后来current变更；精确recipe仍不能拼合。L128/S7/.01→1末步原Eq7 .512734375、发布code .992265625，均非1；这个纯标量计算不是GPU或完整运行验收，不写ASS末步完全恢复EOS概率。

发布版[trainer](https://github.com/yjyddq/EOSER-ASS-RL/blob/549e094ed5ef5924fa20c24614d29e4ad1ec71b3/cj-grpo/cj_grpo_trainer_eoser_ass.py)实际85–151、414–493、560–594：保存每步masked sequence与本步新unmask positions；求值使用前一masked state logits和下一步targets，loss按本步positions选择、token均值后step均值、clipped ratio/KL。保持状态/位置对象是可采用的接口事实；**token logprob并不包含top-k位置选择的完整joint law，均值/clip/组中心化不认证无偏或ordinary PPO exact。** 参数、行为策略、mask/位置、schedule、loss权重、reference必须共同固定；2026memory优化不纳当日实现。

Feynman§14–15实际新兼容限定已读回，作者又actual顺读原trainer659–755对应位置：计算group std但advantage仅`rewards-mean`，没有除std，不能把论文Alg1归一方式说成此发布实现。生成first-EOS-inclusive completion_mask，但loss只乘unmask_positions、不交该mask；reward解码整个completion_ids/skip_special_tokens。因此**不授自动剔除EOS后所有位置/文本、整套paper-code等价或joint-law无偏**；也未证明padding独占收益/否定masked-state接口。这两限定留必要正文，不因No Change删反侧。

## 4. 评价与关键反侧（有限标准＋正确性深入）

§4.1–4.4/Tables1–3、AppendixB/D已实际读并复用Feynman§12：LLaDA-8B-Instruct，GSM8K/MATH500/Countdown3numbers/Sudoku4×4，0shot/greedy、L128/256及对应block/steps；group6、beta.04、epsilon.5、rollout Gumbel temp1、batch48/accum2、任务分别训练，训练自由推理和training-free decoding分账。论文硬件/完整E2E latency/precision/seed/完整SLO为Not Disclosed；原README命令8GPU不授型号、等总费或已复现。

Table1 math仍偏向Semi-AR：L256/S128 GSM8K CJ+EOSER77.75低于diffu-GRPO79.91与CJ+SemiAR84.29，planning改善不能概括全task。Table2 L256/S8 CJ+EOSER+ASS math53.22/22.20与planning59.38/50.32是少step人口，不能合并原128step质量成同质量净加速。Table3只L128/block64/S32局部三轨迹对照，支持条件状态选择的经验信号，不完整隔离所有预算/路径变化。B承认状态存储随S与训练费增加；D的数学串行/规划并行解释只是作者直觉，不作因果或所有模型判断。`O(log L)`只step/state份数，单份序列长/词表/前后向和所有存储仍付费。精确gamma recipe/joint-selection无偏/普遍质量或速度均不正面采用，但不删除状态接口与已读局部反侧。

## 5. 实际owner比较提案：具体已有覆盖，不写Books

按当前ROADMAP unique owner为TRAIN-GRPO/Ch33：拟长期采用仅**在生成时真实masked状态、当步新提交位置、behavior/current/ref与loss reduction共同固定，不以终态完整串概率代替该对象，也不由token surrogate签发joint-law无偏**。本次actual顺读[Ch33](../../../../../books/part-04-training-system/33-grpo.md)开篇objective/artifact职责，以及当前2594–2617完整局部：2603有冻结masked state、已填作context/仅action positions更新；2605联合冻结state/mask/behavior/evaluator/全费与净训练效率；2607–2611区分confidence-dependent selection score、full-trajectory推导与实际top-k；2613 surrogate权重/人口不是exact sequence likelihood。**所需采用限制已经由具体正文承载，不是因同名或主题相似说No Change。** 原source-family标签/别2026note不归本任务，不改这些正文/注。

Ch32开篇AR prefix-state/token ratio负责其原对象，Ch34开篇offline preference/reference分责，不把MDLM的mask轨迹新配方当二者等价。Ch24当前123–135多轮forward/mutable/commit/schedule质量延迟与Training / Inference mismatch完整邻接内1387–1389人工mask对实际schedule状态已有覆盖（原1379定位因并发漂移，只据同一语义锚点）；本次EOS衰减/指数schedule只作为release具体上下文，recipe冲突和无净加速不形成新的长期保证。提案Books **已有覆盖：TRAIN-GRPO具体Ch33**；EOS/ASS具体版本说明留报告，精确recipe安全隔离，不新增Ch24/33 note、不制造另一owner或预签POST。必要Books背景/理念/写作/相关State与邻接已读，未取得写锁，也没有写Books。

请Feynman只核本§2新的历史绑定、§3受影响兼容/recipe分责与§5实际owner NoChange；已过事件/5分/v1评价不重跑。可用层准备即交，日门其它潜力仍普通，非DAY/FINAL/计数。

## 6. 实际owner结果采用归并

已actual读Feynman§13完整owner比较：本次最终采用与该节限定完全一致，Books具体已有覆盖/No Change：TRAIN-GRPO Ch33真实masked-state/本步action位置、EOS条件与少step不等总费；Ch24相关状态/commit/stop职责是交接，不另立重复owner。上述§5作者保存真实比较，不认为书中已有完整EOSER gamma/CJ实现，软EOS也不等VOID。README已按原Sep28code-release/5分、必要受影响域与具体NoChange同步正式新增1（旧ACP1＋新1＝2），Books实际新写0/无锁/无POST义务。

Feynman§14–15已actual核§2–3历史绑定/累计gamma初版事实与最终Source/No Change通过，作者已只并入std/EOS两必要限定；精确recipe冲突仅受影响域隔离，未把paper发布时间搬Sep28或把论文/代码混成无条件正确实现。Ch24行号因并发漂移，以Training / Inference mismatch语义锚点及reader当前1387–1395实际承载为准，不回滚别日修改。完整六节DAY§18真实通过，作者仅保存完成态供实际FINAL，后者/root接纳尚未发生，不重复原评价/owner或预增计数。
