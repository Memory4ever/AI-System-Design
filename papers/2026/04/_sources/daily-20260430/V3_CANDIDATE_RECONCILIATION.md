# 2026-04-30 V3 贡献分母归并工作表（未冻结）

窗口为 `[2026-04-29T09:00:00+08:00, 2026-04-30T09:00:00+08:00)`。`2604.25919–26952` 的 1034 个 exact ID 是有据公告批次推断下的**原始身份库存**，不是 1034 篇已语义筛选的题摘、候选或全文审阅量。这里仅归并 [`V3_ARXIV_SCREENING_NOTES.md`](V3_ARXIV_SCREENING_NOTES.md) 中已有的完整题摘及必要 exact-v1 判断；更早的暂定语句被后面的定点复核覆盖。原工作集合中 `25925` 因更早同题全文线索、`26365` 因作者 02/22 已载同题名与 L²P 机制的公开主页版本线索，均转为具名首次公开/家族归属隔离；`26220` 的受控模拟未改变 Ch72 已有的轨迹 posterior 泄漏与任务效用分账，转为具名前分母关闭。另 `26889/26940/26951` 的 v1 处理字段晚于本窗 09:00 截点，官方逐篇公开上界未得，先作具名日期未核隔离；这些字段不反证实际晚公开。可继续评估本窗归属的暂为 **33 家族：2 已实际 Integrate、14 拟 gap、1 已核 Existing、11 拟 Only、3 中心 Disputed、2 Books 差额待判**，另有 ZAI 一家族已实际写后通过。这仍非冻结候选分母；日期隔离项的机制证据可保留，但不在本日报正面评分或写 Books。其余高风险题名补查的安全/形式化线索还在具名准入校准，不机械加入。所有“拟”均非独立 Books 采用或日级 Gate。

库存来源不能混称一张收据：暂留的 `26391`（`cs.IT`）与 `26706`（`math.ST`）不在旧 `arxiv-owner-receipt.json` 的 `identities[]` 中，实际由本日 `arxiv-api-enumeration.json` 的 exact-ID 补检取得完整题摘与 v1 身份；官方 abs-v1 分别列 04/29 08:00:40Z、14:15:40Z 为 **Submitted**，不是首次公开。两项与其它家族同样只依公告槽、连续编号与邻界作 04/30 08:00～09:00 北京的有据推断；不能用旧 owner receipt 覆盖数或 Submitted 单证证明其落窗。若独立贡献审阅不通过，按具体理由移出工作集而保留此发现路径。

对下列暂定 33 家族逐 ID 回查旧原始 receipt 的 v1 revision metadata，31 项确有条目且 `Updated` 均落在 `2026-04-30T00:00:22Z–00:58:37Z`；缺席的正是上述 `26391/26706`，已由 API exact-ID 补件取得题摘。这个核对只排除了“33 中另有被旧收据遗漏或处理字段跨 01:00Z”的账面问题，**不是** 31 项的逐篇首次公开证明，也不提高两项补件的日期精度。仍须把 `26889/26940/26951` 的截点后字段与更早同家族例外分开隔离。

## 已有明确长期差额，待非作者 source→owner 与 Books 裁决

| Family | 唯一拟 owner 与本轮最窄新增命题 | 当前边界 |
| --- | --- | --- |
| `26039` | Ch49 同一 MoE batch 的实际 expert histogram 进入 CTA-grid/config 选择 | 单 H200、vLLM eager、顺序请求；不得推广并发 SLO |
| `26052` | Ch66 对同一 prompt/response 独立标风险等级，按输入风险追踪方向性变化 | 两模型不同 prompt 分布，非跨模型因果比较 |
| `26074` | Ch54 host→SMEM 的 TMA 直取与 HBM staging 分支 | 硬件特性和 offload 比率决定收益；不能泛化所有 PCIe |
| `26102` | Ch81 viewer / planner / editor 的 context 与格式错误分账 | 额外调用与修复结果需同账验收 |
| `26180` | Ch66 聚合 claim 的量词类型决定查询、停止和 tuple-lineage 证据 | 16 条人工检查 claim；ground truth 非形式真值 |
| `26197` | Ch77 稳定业务/授权树同时限定候选 scope 与 leaf→ancestor 重算域 | LLM 摘要不等事实无损；ACL 变动和生产 tail 未证 |
| `26256` | Ch33 多 policy version 的 rollout DP group 生命周期及同版本 KV 迁移 | stale window、transfer、内存成本；受限公开训练设置 |
| `26274` | Ch72 审批过的良性 tool trace 编成执行前 pDFA；profile 修订也是权限变化 | 开放场景/字符串同义词可绕，O(1) 不含全部 guard 成本 |
| `26294` | Ch36 单设备轴折叠 TP/SP 的参数—激活驻留与通信交换 | 大规模主表多为 forward throughput，不是全训练提速 |
| `26557` | Ch54 同一 NVMe 容量的 page-cache 与 direct-LBA 路径选择 | pinned DRAM 仍在路径；不是任意运行中热迁移 |
| `26694` | Ch26 浅 action / 深 video 去噪时训练必须覆盖异步 timestep 与 clean-action 条件 | 固定观测窗/受限真机，非通用实时控制保证 |
| `26779` | Ch33 RL rollout 的 draft 训练信号与 target policy loss 隔离 | 235B 为模拟；接受率不等训练步加速 |
| `26837` | Ch54 sparse attention selector/runtime 分权与两级 metadata 工作集 | 算法/质量与 runtime 对照须分账；TPOT 有反向结果 |
| `26604` | Ch36 enrollment target population 与轮次 participation 的两级 inclusion，不等于已入组 worker 的到达频率 | 仅 synthetic FL logistic；ignorability/positivity/propensity 可估条件，非 LLM 实测 |

这些是有明确命题的**作者拟采用队列**，不是已写 Books 的清单。原六项局部实现问题经本日必要原文/实际 owner 收束：`25975` CapKV 的 logdet/leverage 是旧 Ch45 future-query eviction 的受限理论 proxy，暂 5 分仅报告；`26209` HPD 的条件独立字段并行是 AVE 专用 factorization，暂 5 分仅报告 Ch48；`26378` CoQuant 的同算子 W/A 量化扰动联合高精度子空间相对 Ch49 现有二阶分配仍可能改变校准准则，保 5 分 source→owner 非作者待核；`26508` 渐进视觉 latent 按预测重建误差逐段发是 Ch23 固定 edge-split 之外的有限 read-time 控制，保 5 分仅报告待非作者核其端到端证据缺口；`26511` Tatemae 的同压力无/有监控 tool-choice 配对是 Ch66 安全评价的候选切片，保 5 分且保护性深入、Books 待非作者核；`26752` 多模态 MTP head 的视觉占位 token 只支持 0.5B auxiliary loss、无任务/传输量或时延对照，故改具名前闭。六项不再称普通未读。智谱《Scaling Pain》的 Ch54/55 两个官方发布机制已另获 root 非作者实际写后 PASS，属于机构来源家族，不计为 arXiv ID。

## 已作条件性候选判断，但不提 Books 正面写入

- 已实际整合：`26340` DMEP 的一次性 expert/optimizer-state 物理裁除、gate 重排与后阶段关闭 balancing loss 已进入 Ch30 旧可回滚 mask 后，root 的[必要源—owner 边界复核](V3_ROOT_TWO_BOOKS_BOUNDARY_FINITE.md)与[实际写后复核](V3_ROOT_26340_CH30_WRITE_AFTER.md)均通过；不是一般在线漂移阈值触发或全程训练提速。
- 已实际整合：`26622` OCR-Memory 的图像只负责 `(image, segment)` 定位、原文日志负责确定性回读，已进入 Ch77 原纯视觉压缩风险之后；root 的[写前源—owner 核](V3_ROOT_26622_CH77_SOURCE_TO_OWNER.md)和 apr01 的[非写入者实际正文/邻接核](V3_APR01_26622_CH77_WRITE_AFTER.md)通过，章末 Review note 亦已补齐。它不证明定位正确、答案真值或端到端成本必降。
- 具名 Existing / 现文承载的受限证据：`26505` Ch72 的同 batch 动态 scale 跨租户 logit side channel，root 已按[实际原文与正文](V3_ROOT_TWO_BOOKS_BOUNDARY_FINITE.md)独立通过；不称其全部攻击条件已在书稿复现。`26091/26412/26687/26733/26881` 已按最新贡献前置复核转具名关闭；它们的原必要方法与负边界仍在筛选笔记，不因已覆盖主题而机械取消其受限案例价值。
- 标准仅报告或受限条件线索：`25975` logdet KV surrogate、`26103` 模拟 PNM、`26209` 条件独立字段并行、`26508` 渐进视觉 latent 读时停止、`26649` reasoning-step 检索 checkpoint、`26768` task/fact LoRA 资产拆分、`26821` 3D bank 模拟、`26848` 预测几何调制 action-only/联合生成的注意力。`26848` Table 4 的同表示门控开关对照提供受限设计分支，但 Ch26 已有预测状态仅作动作提案、外部 observation/controller 掌握执行真值；目前它更像该接口的局部 actuator，不足另添通用正文。`26167` 的逐请求连续 embedding 安全输入须按保护性深入边界判断，暂报 Ch72 而非认定 moderation 分数等于真安全。`26139` 的 D-LLM 隐状态检测仅局部改善已定义的只读诊断、未改变 truth owner 或成本—质量边界，连同 `26128/26326/26495/26503/26573/26666/26752` 改具名前闭；原 exact-v1 受限证据不删。这里不凭 5 分自动保留最终分母。
- 高风险题名补查恢复的理论线索：`26391` 异质共谋集合×两跳多服务器 topology 改最小 key/通信率，仅有严格有限域与无误广播模型，拟 5 标准仅报告 Ch36；`26706` 黑盒选中目标的置信集合可在受控 TV/互信息泄漏下有 noncoverage 上界，拟 5 标准仅报告 Ch66，尚无模型评估中的 leakage 校准。两项均非作者待核，不能从纯数学学科标签硬关，也不能因理论可写公式就加 Books 或发布保证。
- 中心争议，Books 暂缓：`25931` PHC 的 `G*` 标签身份与“任意后验信号”互信息定理、`26130` reward-lens 精确分项和与 final nonlinear norm 的冲突、`26525` PRAG 排序噪声/虚拟邻接接口。`26951` TIDE 的中心 Bernoulli 交叉熵/KL 争议另保留在日期隔离项；不在能证明本窗上界前计此日候选。需非作者定点核中心公式，不否定所有局部实验，也不正面写 Books。

## 两项已具名准入、Books 差额待非作者判断

- `26378` CoQuant：5 分标准，Ch49 同一线性算子 W/A 双量化误差进入高精度保护子空间；已有二阶敏感度段部分承载，具体校准准则是否足以改正文待核。没有专用 kernel，不采速度收益。
- `26511` Tatemae：5 分保护性深入，Ch66 同一压力下只改变监控/训练声明的 tool-action 配对分母；prompt 内 JSON/XML 选择未真实执行，理由标签不是内部欺骗动机真值。是否超现有 sandbagging elicitation 切片待核。

## 首次公开/家族身份隔离（不计本窗正面候选）

- `25925` SpecTr-GBV：arXiv [exact-v1](https://arxiv.org/abs/2604.25925v1) 标 04/01 提交，并在本批赋得 2604.25925；这两者都不是单独的首次公开证据。另有同题、摘要相近且同多 draft×block verification 方法的 [ICLR 2026 OpenReview 匿名全文](https://openreview.net/pdf?id=5FAUpLjndj)。[ICLR 官方 Author Guide](https://iclr.cc/Conferences/2026/AuthorGuide) 给出 2025-09-24 投稿截止和 2025-11-11 reviews/public discussion，但当前 OpenReview forum/API 被验证挑战挡住，尚未取得本件 exact 发布时刻。官方 OpenReview 全文的更早身份线索足以暂停将 arXiv April ID 当本窗新首发；不能仅凭会议一般时间推断本件在 2025 已公开。原 Ch48 方法/成本证据保留，Books 不正面写；定点重开只需该 forum 的公开日期及与 v1 的同家族映射，不查完整版本史。
- `26365` L²P：arXiv [exact-v1](https://arxiv.org/abs/2604.26365v1) 提交于 04/29 07:22 UTC，OAI `created=04/29`、`updated/datestamp=04/30` 与本批公告处理链相容，但不能独证家族首发。共同作者 Rui Huang 的[公开主页 2026-02-22 版本](https://github.com/RuiHuangAI/RuiHuangAI.github.io/blob/f110b276ae138d1204e585bf2eb42df18d6aa8d4/_pages/about.md)已列完全同题名、同九作者和 L²P 可学习线性预测、50 样本/20 秒核心机制；[对应 commit](https://github.com/RuiHuangAI/RuiHuangAI.github.io/commit/f110b276ae138d1204e585bf2eb42df18d6aa8d4)的作者/提交时间均为 02/22 08:41:50 UTC。Git commit 时间不自动等于网页首次公开时刻，但这是足以隔离本窗新家族判断的更早身份线索。原 exact-v1/Ch24 差额及 root [独立采用核](V3_ROOT_26365_FINITE_INDEPENDENT.md)保留，**04/30 不评分、不写 Books**；仅在取得作者页该版本的可核公开时间或其它更早/本窗首次公开证据后，定点决定历史归属。
- `26889/26940/26951`：三个 [arXiv exact-v1 摘要页](https://arxiv.org/abs/2604.26940v1)分别只给 04/29 Submitted，不能给 04/30 09:00 北京前的首次公开上界；当前保存的 v1 `Updated` 字段依次为 `2026-04-30T01:01:07Z`、`01:03:27Z`、`01:03:51Z`，DataCite 初建依次为 `02:09:45Z`、`02:11:09Z`、`02:11:29Z`。相邻已核 `26837` 为 `00:57:55Z`、`26848` 为 `00:58:37Z`；结合常规 20:00 EDT 公告槽仍不能证明三篇逐一在本窗结束前公开，也不能从处理时间反推实际一定晚公开。`26889` 的 driver command-stream 诊断、`26940` 的学生 top-K 限定教师 token selector 和 `26951` TIDE 的理论争议均保留在原筛选笔记，**日期未核、不评分、不写本日报 Books**。恢复条件是官方可核的本批逐篇公告列表/该身份上线时刻，或同等能限定首次公开早于 04/30 09:00 北京的记录；不展开所有版本史。

## 具名前分母关闭与待最小消歧

筛选笔记已经逐项写出具体关闭理由的代表族包括 `25921/25922/25928/25930/26020/26024/26091/26106/26118/26120/26148/26152/26170/26173/26176/26181/26182/26206/26243/26258/26334/26347/26355/26360/26382/26388/26412/26460/26469/26470/26687/26689/26733/26815/26841/26866/26881/26904`。`26334` 还存在早公开 Zenodo artifact 的家族归属例外；`26157` 当前家族已撤回，均不作为本窗正面候选。这不是对其它 raw ID 的全量关闭声明。

`26220` When Agents Shop for You 曾被暂留为 5 分 Only，现按贡献前置规则具名关闭：官方 PDF-v1 的六档 verbal persona 既作为行为生成条件又构造目标 WTP 档位，同一耳机模拟、同一 Claude Haiku buyer/seller/inference、60×6 轮次不足隔离实际人类未说出的偏好；去价格文字后 within-25% 只有 9/360，支持角色行为是可观察线索，但不能支撑“真实 WTP 近一比一恢复”。Ch72 的 Agent Privacy 已明确跨 turn/recipient 的 posterior leakage、秘密定义与任务 utility trade-off；本篇未给会改变允许行为或预算 owner 的新受控证据。保留这一受限案例与重开条件（真实私有目标、独立模型/商品/任务匹配，及与现有轨迹预算门槛同台比较），不以小样本本身作排除硬门槛。

高风险题名定点抽查具体关闭 `26217/26313/26394/26427/26838/26857/26479`；`26391/26706` 已从最小理论贡献消歧进入作者暂定 Only 工作集，不因非 LLM 或一般数学标签硬关，非作者核前不称正式候选。原始完整题摘、必要 exact-v1 与 Ch36/49/66/72/78/84 差额见筛选笔记末节；不能把这一小组说成安全类全量审阅。`26809` 的异步遗忘版本发布与永久删除保证存在中心疑问，**暂不计入当前 33 工作数或正面 Books**，已提交非作者定点裁决；若确认其纠错贡献及当窗归属再具名恢复，不能因医疗图像应用直接前闭。另在“医疗/局部场景”共享关闭理由的有界复核中，`26283` 暂倾向具体前闭，但 `26288` 的人工光标轨迹监督反向 saliency 证据、`26324` 以公开生成器提供合成训练支持而非对已到梯度重加权，均保留为**最小非作者准入消歧**；细节及反例在筛选笔记末节，两项都尚未加入 33 工作数。

**仍可执行的最小问题**：上述十项已在筛选笔记最后一节具名收口，`26419/26483/26503/26553/26569/26573/26644/26923` 前闭，`26604/26940` 条件性 source→owner 队列；原六项局部机制也已按前述裁出有界处置，`26378/26511` 仍待非作者真差额判断。其余拟候选需补非作者准入/必要 exact-v1/owner，随后核日期例外、正式六部分与来源限制。这是受影响题摘的有限消歧集，**不是** 1034 raw 的全文配额。窗外 `26953–27045` 的早读线索不得进入本日分母。

## 快速准入合同的后续覆盖判断（非作者待核，不改上方 33 暂数）

前面的 `25975/26103/26821` 暂定 `Only` 文字是历史工作判断。[筛选笔记的最新有界对读](V3_ARXIV_SCREENING_NOTES.md#快速合同再剪枝三个受限代理是否真的改变现有选择)分别比较了 CapKV 近似信息代理、AMMA 模拟 PNM、Voxel 模拟 3D bank 与 Ch45/49 的真实选择：三者有局部技术事实和值得保存的反例，但现有证据尚未使 current owner 的 eviction、execution-plan 或硬件验证分支出现新的长期决定。作者建议**具名前分母关闭**，保留原 source/反证和可重开条件；不能仅因有 Books 主题前闭，也不能以未造实芯作为普遍门槛。该建议已合批交 root 非作者贡献裁决，未获结果前本工作表 `33` 和正式日报 `4` 均保持原账，不把待判写成已通过 Gate。
