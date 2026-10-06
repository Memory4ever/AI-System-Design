# Autocurriculum18325：必要Source/实际owner/最小PRE

resume_mar18准备，非准备者未裁；仅03-21补BJT03/20，原65完整AB/root准入校准有效，不新query，不写Books/自授safe/DAY。

## 身份、日期与拟采用增量

[official exact-v1](https://arxiv.org/abs/2603.18325v1)完整AB/header/history已实际读，v1 Submitted03/18T22:17:22Z、当前v2Aug27，无具体withdraw/correction/accepted信号，不以版本号扩revisiondiff。真实[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2603.18325)created03/20T02:10:00Z、registered01Z、statefindable；v1 Updated03/20T00:20:45Z与Available2026-03不同字段，不把submitted/updated作为公告精确时刻。同本批官方availability＋注册夹证，只作BJT20 arXiv日级事件限定推断，不证明别处无先稿。

完整AB具体准入：全题都请求昂贵teacher CoT→按当前答案集成的verifier反馈重加权，只在受选prompt查询teacher/训练新的weak model→可把teacher监督与筛题/集成/部署费用分开，不再把少teacher trace等同singlemodel全费用节省。拟2+2+2=6，增量跨teacher监督、学习器与outcome aggregate的消费边界，不给boosting成熟原则/机构/摘要“exponential”加分。

## 必要原证与直接反侧

实际[exact-v1 HTML](https://arxiv.org/html/2603.18325v1)§2–5/Algorithms1–5/Eqs1–11/Theorems3.3/3.6/4.5、Remarks3.4–3.7/4.4；B.1 test-error decomposition与B.1.1 CoT数量组合、B.3 partial-coverage/B.4预算组合定点读到。未遍全部39页证明/C各lemma/无关参考/后来PartII，不核代码/复现，不宣全部定理证明无误。关键机制、权限及直接反侧够即停。

- 理论设定是固定T的autoregressive、最后一个token为答案、完美binary outcome verifier、可实现class中存在完美π*，iid prompt pool。Teacher oracle提供π*正确CoT，不是普通会犯错的API teacher。无prompt难度分布假设不等没有teacher/verifier/class假设。
- Deterministic Alg1分不相交prompt pool阶段，保持旧model集合；Alg2按当前各model正确次数rank和Eq5的boosting权重做rejection sampling，只查询受选prompt的teacher CoT，base learner须达到该重加权分布上的constant accuracy。不是简单只挑最难题，也不保证每个新model在原分布不引入错误。输出是答案plurality的improper outcome-level ensemble，不是将所有旧模型自动压为一个新checkpoint。
- Theorem3.3在deterministic/unique-final-answer/realizable条件下，teacher CoT调用从约d/ε到d×polylog(1/ε…)；prompt人口仍约d/ε，筛题/verifier和训练没有随CoT查询消失。B.1 potential/testerror分解允许某轮样本不足但小权重贡献，非每轮必能修好最难题；B.1.1 teacher查询是Σ|Dout^j|受每轮常数精度base learner阈值约束。不是现实LLM单模型更强的实测。
- Remark3.5若目标要求完整CoT逐token匹配，上述低查询界退回约d/ε；终点oracle不能监督未查询的中间轨迹。正确答案也不认证过程truth、faithfulness或执行安全。
- Stochastic Theorem3.6只在1−ε prompt质量上给≥3/5 outcome成功概率；Alg3返回各model outcome的uniform mixture，MonteCarlo rank估计额外rollout。提升为高准确率的Remark3.7须unique-answer和多独立sample的consensusvote，增加推理预算。不能把pass@k/多数投票保证记为singlepass@1保证。Eq8正文用≥4/5 indicator称loss，符号不采作可实现优化recipe。
- RL Alg4仍是固定reference sequence coverage＋去重、高prob阈值和正确answer的rejection-filtering，再用loss membership的ERMoracle学新model，不是PPO/GRPO直接gradient更新。每prompt须有指定正确trace概率≥1/Cseq；即使所有正确最终答案有支持，也不自动保证π*某一完整trace达到此门。
- Theorem4.5在deterministic/unique/realizable/coverage前提下将rollout计数中的coverage项与目标accuracy项加法分开；B.4参考调用为Σm|Dout^j|、learner筛题调用累计约kn，而optimization是k次ERMoracle，不是把完整优化器计算计入“compute”。B.4 verifier文字m|Dprompt|与前面learner k|Dprompt|不对齐，不采精确verifier式或零费用保证；采用分责接口不认证该计数recipe。
- Limitations明确fixedreference不含coverage自我扩张；no-coverage prompt过滤直接放弃；online PPO/GRPO co-evolving分布、noise/learnedverifier都是开放问题。本文未做现实LLM训练/硬件walltime/qualitymatched端到端对照；model/hardware/precision/batch/concurrency/SLO不适用其抽象定理，部署成本Not Disclosed而非0。

## Actual唯一owner与差额

sole `TRAIN-SFT`，[actualCh29](../../../../books/part-04-training-system/29-sft.md)169–220完整读取：190 LLM4Cov从同drafts挑失败状态、teacher修复并stageSFT及全费回退；192失败前缀NTP、194成功生成/全部yes-no评价任务，199–214少数据/trajectory/heldout边界。这里已有“低分优先非普遍最优/同数量非等teacher预算”，但没有“verifier-ranked ensemble决定teacher查询、constant-accuracy weak learner和answer-only aggregation”的具体监督接口；不借已有成熟费用边界假claim被纠错。actualCh33 136–153真实rollout/admission前后分责、Ch27生成课程入口仅路由，不承接teacher query/returned SFT asset；Ch28/30开篇交接已读。建议soleCh29在LLM4Cov段完整后、失败文本成为监督target前一段；不另写Ch27/33/推理vote。

## 一段literal PRE（未授写）

当真实 outcome 验证明显比取得完整教师推理便宜时，还可把“选哪些题请求示教”与“最终交付哪个模型”分开。一个[受限自课程构造](https://arxiv.org/html/2603.18325v1)保存已训练模型的答案集成，按验证器测得的当前正确次数重加权 prompt，再只为受选题请求教师 CoT、训练在该条件分布上达到常数准确率的新模型；交付的是多模型答案聚合，不是一次微调后自动得到等价单模型。它在可实现模型类、完美 outcome verifier 与正确教师等条件下减少教师轨迹查询，但筛题、模型训练、集成状态和推理调用仍付费；保证针对最终答案，若要求完整轨迹匹配就不能继承同一示教节省。随机模型还需区分多数 prompt 上的成功概率、额外抽样投票和单次回答质量。固定 reference 的拒绝采样分支同样依赖正确轨迹的 sequence coverage，不能由该构造推出线上 GRPO、覆盖扩张或带噪 judge 的普遍收益。教师/验证器不可靠、支持域不够或集成总成本不合算时，保留 verified demonstrations、均匀或分层监督与独立 held-out 回归，不只按教师调用数批准训练产物。<!-- source-family:SF-2026-ARXIV-2603-18325 -->

静态注：- `SF-2026-ARXIV-2603-18325`：[Autocurriculum exact-v1](https://arxiv.org/html/2603.18325v1)，必要§2–5/Algorithms1–5/Theorems3.3/3.6/4.5/相关Remarks及B.1/B.3/B.4关键组合。仅verifier引导教师查询与outcome ensemble分责，保realizable/完美teacher/verifier、终点非完整轨迹、stochastic vote、sequence coverage和ERMoracle费用；不授精确计数recipe、完整证明认证、单模型等价、PPO/GRPO或真实硬件加速，未核实现/复现。

## 非准备者必要 Source / actual owner / PRE 裁定

root 实际读取 exact-v1 §2、§3.1–3.4（补齐SS3完整Algorithms1–2、Theorem3.3、Eq3–7、Remark3.5与图示反侧），§4完整Problem4.1/Definition4.2/Algorithm4与SS2完整Theorem4.5/Algorithm5，§5全部直接限制。独立DataCite真实created03-20T02:10:00/registered01及v1Submitted/Updated与后v2字段，与本日availability归属依据相容，仍不冒别处绝无先稿。实际Ch29完整169–218及单独188–196相邻段，原literal一PRE/static逐字核对；有限Source/具体soleowner差额/PRE PASS，保持6分。未认证全部证明、精确verifier调用式或硬件训练效果，不需为此遍历其余附录。

output是improper answer-level ensemble，weak learner按重加权分布训练而非每轮原分布全面改善；新增模型也可引入错误。完美teacher/verifier、可实现与unique-answer的适用条件近文，完整CoT匹配不能继承低示教界；固定reference的coverage既不扩张，也不包含online PPO/GRPO。原文compute只计rollout，不含优化器及全部部署费用。现有LLM4Cov承载失败状态采样，却未承载验证器决定教师查询和交付集成的分责接口，不能作泛化NC。必要支持与直接反侧足够此有限采用即止。

授resume_mar18 soleCh29在原LLM4Cov完整段后/失败文本NTP前窄写原一PRE与本人static；未计actualI/safe/DAY，写后由root一次实际nonwriter完整局部/注POST，方可归并。

## 实际写后独立复核

root非writer实际完整Ch29 183–205与末六行，核新192及本人1480static对原literal/PRE与必要Source；LLM4Cov→教师查询与交付模型分责→失败NTP/yes-no三角色交接未删旧机制，理论假设、答案聚合非单checkpoint、全费用和回退近文，未把original本文低查询界转成真实训练收益。本人静态注准确保留所读深度与未核范围，marker/static各唯一。scoped diffcheck无输出；有限actualPOST PASS，可接纳I/释放Ch29，不授本日DAY。

## 授锁后作者实际写入（待nonwriter POST）

原literal一PRE已实际Ch29 L192，LLM4Cov原190后/失败前缀NTP现194前；自身静态注1480。作者实际完整184–202新旧邻接与最后五行本人/邻注回读，正文与注逐字原PRE，单body marker/单本人注，scoped git diff --check空。不改其他family/书注验收身份；当前锁交root一次实际nonwriter POST，尚不计safe/DAY。
