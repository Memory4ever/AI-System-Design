# 04/15 八项普通 Books 待办：精确采用提案

## 2026-09-27 实际写后验收

复核者 root，非本批正文写入者。八项必要 source→owner 的窄增量已经逐项实际核验；本轮顺读真实正文及两侧交接：Ch72 的 membership 分账与安全格式/行为身份，Ch23 的备用视觉状态与声学训练目标，Ch66 的固定 probe disagreement 切片与能力匹配阶段 witness，Ch24 的 detached 局部轨迹训练支持，Ch49 的全块累加/选择性统计更新。正文均不靠论文名或 source marker 替代机制，不在 Review notes 后加正文。

12342、12359、12358、12506、12373、12447、12617、12798 八项实际写后通过。采用范围、对照条件、代价、明确反例与旧路线 fallback 与必要 v1 一致：不把筛选参与当训练成员、校准零空间当全域保持、备用回收当证据充分、JSON 当因果解耦、条件 AUC 当全样本风险、near-hazard 当意图、局部 target 当普遍 Bayes 真值、实数 shift 抵消当有限精度安全。未复现实验。可以同步真实 Integrate 与章末证据状态，释放 Ch72/23/66/24/49 本批写锁；全日实际整合增至22项、普通 Books 待办降至0。17项争议、必要正文及日期/来源隔离和最终独立日级 Gate 仍须明确处置，不由本次小组通过预支。

下文“尚未写入”“当前锁不可用”为本批写前历史，不再作为普通待办。

作者：apr01。检查时间：2026-09-27T11:25:13+08:00。本轮重读当前 AGENTS、统一 Prompt、三份研究合同与 ROADMAP；窗口仍为 `[2026-04-14T09:00:00+08:00,2026-04-15T09:00:00+08:00)`。

这八项必要原文已有本日日报 §4 的具体记录，本轮定点重新打开官方 exact-v1 HTML、重读拟采用方法及真实 owner 的相邻正文。均保持原 `2+2+2=6`、真实知识缺口/保护合同深入例外，不靠抬分推进。以下提案保留原始边界；实际采用阶段见末尾，不把写前通过等同写后验收。当前 Ch49、Ch36 由其他日期独占，不写它们。

## 本轮实际落笔与非作者核验

| 家族 | 实际正文位置 | 非作者范围 | 当前处置 |
| --- | --- | --- | --- |
| 12342 CoLA | Ch72 Membership，变换家族之后/分类器之前：训练成员与筛选参与者的 I/E/O 分账、可观测接口、Unknown 与 DP 边界 | root 实际重开必要原文与 owner；顺读新增两段及前后交接通过 | Integrate；未复现实验，不代表日 Gate |
| 12359 SteerEdit | Ch72 模型文件，内部 bucket 之后/Prompt Injection 之前：数据格式不等行为可信、校准 null 与小奇异值近似、独立行为回归 | root 必要源与 owner、实际两段及邻接写后通过 | Integrate；未复现实验，不代表日 Gate |
| 12358 DSTP | Ch23 几何稳定/实际删除之后、主动取证之前：备用 visual state/短期 union/回预算与局部 softmax 代理边界 | root 必要源/owner与实际两段及邻接写后通过 | root 必要源/owner及实际两段相邻交接写后通过；Integrate，未复现实验，非日 Gate |
| 12506 UAS | Ch23 语义锚点 provenance 之后/collision 之前：target 支持声学维度与 schema/预算/ASR 取舍 | root 必要源/owner与实际两段及邻接写后通过 | root 必要源/owner及实际两段相邻交接写后通过；Integrate，未复现实验，非日 Gate |

八项全部已实际写入并通过 root 写后独立核；普通 Books 待办0。本日尚待独立日级 Gate，不预先冻结或 Complete。

## 2604.12342v1 CoLA → PLATFORM-SECURITY / Ch72

- 原文：[exact-v1](https://arxiv.org/html/2604.12342v1) §3.1–3.2、§4.1–4.2、§5.1–5.3；官方 abs/v1 同题，无撤回标记。§3 明确定义训练成员 `I`、参与筛选但未训练 `E`、未参加 `O`，与本日既存版本记录一致。
- 实际对照：Ch72 `Membership Signal 必须先通过可识别性审计` 已有低 loss 的 nuisance/controls、变换家族、privacy unit；后面的 DP 小节有 adjacency，但尚未区分 **训练成员与筛选参与者**。Ch27 负责数据筛选，不双写攻击/隐私解释。
- 精确插入：上述 Membership 小节的变换家族两段之后、Safety-classifier 条件分支之前。两段说明少量入选数据降低训练开销但不自动缩小整个 pipeline 隐私对象；成员审计分别比较 `I` vs `E∪O` 与 `I∪E` vs `O`，筛选元数据/目标输出的 observable scope 一并声明。
- 采用边界：受限 vision 与小型 language 模型的 AUC/TPR 是统计 sensor，不识别真实个人、不提供 DP；side-channel selector/ratio 与纯 black-box clustering 的条件不同，重叠窗口不证明独立试验。新增成本为筛选血缘与对照恢复，证据不足保持 Unknown，正式保证仍交 adjacency/accountant。

## 2604.12358v1 DSTP → MULTIMODAL-REPRESENTATION / Ch23

- 原文：[exact-v1](https://arxiv.org/html/2604.12358v1) §3.1–3.2、§4.1–4.2、§5.1–5.4；v2 提交在本窗后，不作版本比较。
- 实际对照：Ch23 `固定预算要先分配信息责任，再选择具体 Token` 已有按层剪枝、替换≠删读路径、主动 crop；没有 **生成时从备用视觉集合恢复并短期维持原/新 union** 的状态生命周期。Ch45 只交接存储后 KV 身份，不能宣称换 token 就重放旧语言历史。
- 精确插入：该小节最后的 `几何稳定不等于功能可删除` 两段之后、`固定表示之后，可以按未决 Claim 主动补充 Observation` 之前。解释 static prefill 选择仍适合证据需求稳定的短回答；长推理可能需要新视觉线索，discard→reserve→attention-proxy trigger→短期 union→恢复预算是另一路径。
- 采用边界：attention 与难度相关不是因果真值，触发器可能漏检；备用存储、k～2k 临时集合、重排/读取和语言 KV 一致性增加成本。两类 VLM/L40S 结果中 TPS 与总延迟并非全面改善，不写普遍加速或 exact 历史恢复；无法承受备用状态或验证不通过时保留静态高预算/完整输入。

## 2604.12359v1 SteerEdit → PLATFORM-SECURITY / Ch72

- 原文：[exact-v1](https://arxiv.org/html/2604.12359v1) §4、§5.1–5.4 Eq5–12、§6.1–6.5；本轮重读 Eq8–12 与 calibration、StrongREJECT/keyword FR 的区别。
- 实际对照：Ch72 `模型文件与训练代码是不可信输入` 管加载权限/serialization，`Intermediate-state Canary` 管训练 stage；均不表达 **安全格式仍可携带把表示 steering 编译进 MLP 参数的后门**。这是已具有 checkpoint 写权限的威胁，不能称突破 sandbox。
- 精确插入：模型文件小节最后 `内部 account 也可能被滥用` 之后、Prompt Injection 主节之前。先解释数据型格式解决代码执行而非模型行为可信；再说明 trigger/clean calibration keys 与 down-projection 编辑、small-singular approximation 及校准域外失效。
- 采用边界：严格 null 只作用于声明的校准 keys；实际 smallest-singular 不是全 clean 零扰动，正则 least-squares 不自动精确 trigger 映射。prefix keyword 同意不是持续有害输出，utility 切片有退步。artifact lineage、独立行为回归及 trigger-neighborhood 测试是工程要求，不写作者已验证防御。

## 2604.12373v1 Masked by Consensus → PLATFORM-EVALUATION-SYSTEM / Ch66

- 原文：[exact-v1](https://arxiv.org/html/2604.12373v1) §3.1–3.5、§4.1–4.3、§5.3/7；本轮重读 self/external 定义、disagreement 仅测试不重训与 nested probe setup。
- 实际对照：Ch66 `从 Raw Score 到可定位、可校准的 Claim Sensor` 已有 label/judge/模型身份，后节区分可读出与干预；尚未分开 **self 与 peer 的完整样本和 correctness-disagreement 切片比较**。
- 精确插入：Claim Sensor 现最后成本/fallback 段之后、`可解码 Failure Direction 不拥有自动纠错权` 之前。全样本同错/同对可掩蔽差异；保持训练集/target label 不变，仅按 pair disagreement 切片测试，并同步总体覆盖/样本数。
- 采用边界：条件 AUC 不与全样本 AUC 混分母，不在完美反相关子集重训。事实/数学任务结果不同；限定所测 peers、hidden states、probes，不证明内部自知、因果可访问或优于所有外部观察者。增加 peer forward/label/slicing 成本，生产路径仍按实际 calibration 与风险覆盖验收。

## 2604.12447v1 HazardArena → PLATFORM-EVALUATION-SYSTEM / Ch66

- 原文：[exact-v1](https://arxiv.org/html/2604.12447v1) §3.2–3.3、§4.1–4.4、必要 Appendix D 事件定义。safe/unsafe twins 保持 motor requirements，commit 为 attempt 后、任务特定 pre-IPE 配置，不是数据库提交语义。
- 实际对照：Ch26 `Safety envelope` 已有 controller/safety authority；Ch66 `Outcome Witness 决定分数能够声明到哪里` 已有环境事实与运行结果，但未显式区分 **危险终态零成功与执行不能造成的假安全**。测量 canonical owner 应为 Ch66，不把 twin 构造、全 benchmark 或 SOL 配方堆进 Ch26。
- 精确插入：Ch66 Outcome Witness 的环境效标论证内，以同动作要求 safe/unsafe 成对测能力，再分账 attempt→task-specific near-hazard→terminal predicate。Ch26 仅需要既有 Evaluation handoff，不另造完整机制段。
- 采用边界：matched twins 控制声明的场景，语义/视觉与资产构造仍有限；stage 事件由 simulator 可观察 predicates 拥有，不是内部意图/真实物理安全证明。新增 instrumentation/资产构造成本，低风险 smoke test 仍可用终态指标；SOL/未发生终态不自动授安全保证。

## 2604.12617v1 SOAR → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

- 原文：[exact-v1](https://arxiv.org/html/2604.12617v1) §2.3 Eq6–15/Alg1、§3.1–3.5；本轮重读 detached CFG Euler、same-noise re-noising 与 clean-anchor target。
- 实际对照：Ch24 continuous Gaussian→discrete 已有不同采样更新/self-conditioning，`Correction` 只概括 provisional token 修订；本项是 **连续图像/flow 的训练 support 改变**，不是文本 sampler 同义改写。
- 精确插入：`Diffusion：用迭代修正换并行状态更新` 基础代价之后、`连续高斯去噪迁往离散文本时` 之前。两段从 forward-noise SFT 的训练状态与自生成状态不匹配，解释当前模型单步 stopgrad rollout→同 noise 重加噪→监督回 clean anchor，并区分 terminal-reward RL。
- 采用边界：局部构造可定义 target，不证明任意偏轨迹状态唯一 Bayes 真值或完整推理分布覆盖；多 auxiliary points、CFG forward 与权重增加训练成本。SD3.5 的 restricted pairs/steps/reward-specific 选择不支持同 total compute，fresh-noise 与多分支不是全切片更优。稳定 SFT/sampler 已满足质量时仍保留简单方案。

## 2604.12506v1 UAS → MULTIMODAL-REPRESENTATION / Ch23

- 原文：[exact-v1](https://arxiv.org/html/2604.12506v1) §2–3/§4.3/§5.2–5.4、必要 AppE–G。已有具体 recipe/config 记录复用，本轮重读 caption 对照与 ASR JSON 税；不再展开全部音频附件。
- 实际对照：Ch23 `语义锚点不是原模态的替代品` 解释读取/表示边界；native/staged 训练主线尚未说明 **ASR transcript-only supervision 不能直接奖励韵律/说话人/环境声目标**。
- 精确插入：该语义锚点小节的 provenance/fallback 段之后、Representation collision 之前。补训练目标责任：文本 transcript 作为内容监督合理，需更多声学能力时将内容、paralinguistics、events 作为显式字段或独立任务，让 encoder/projector/backbone 按真实 target 覆盖验收。
- 采用边界：structured schema 是一个目标支持分支，不因 JSON 就保证正交解耦；相同 synthetic source 与 caption 的受限对照不隔离标签密度/语法/总成本。主说话人/英中、重叠 speaker、ASR WER 小代价保留；内容-only 任务仍可选简单 ASR，禁止所有理解/生成无 trade-off 宣传。

## 2604.12798v1 VFA → INFER-TENSORRT-LLM / Ch49

- 原文：[exact-v1](https://arxiv.org/html/2604.12798v1) §3.1/Algorithm1、§4/§5.2–5.5；本轮核 Alg1 17–27：sink/local 更新真实 rowmax，其余冻结 shift，仍累加所有块 numerator/denominator。另行 VSA sparse 分支不得混作 VFA。
- 实际对照：Ch14 解释 online-softmax/IO；Ch49 numerical-plan 中已有 paired quantized P/容差不可互换，却缺 **matrix 已高效时 scalar/vector 统计更新成为瓶颈** 的执行分支。
- 精确插入：Ch49 数值验收主线内、`量化前先诊断分布` 之前，两段解释 key 摘要初始 shift→sink/local 优先→选择性更新而非删块，real-arithmetic 相同 shift 会消去，但有限精度仍须验 overflow/underflow、rounding 与工作负载质量。
- 采用边界：sabsmax 摘要不是所有 query score 的上界；增量摘要、重排与启动成本计入。只报告 operator/pipeline 相对吞吐与有限 greedy 任务，不采用普遍 equal-quality/SLO，HumanEval 回退保留；数值条件不通过时恢复完整 rowmax/更高精度。本轮已获 Ch49 窄写锁、实际落笔并通过非作者写后；原写前锁等待已终结。

## 提交与验收

八项采用与实际写后核验已完成，见顶部 root 非作者记录；14 个此前真实 Integrate 与其通过记录保持有效。本日123工作项全部有作者侧处置、22真实整合、普通待办0；分母仍须日级独立 Gate 才冻结，不预先 Complete。
