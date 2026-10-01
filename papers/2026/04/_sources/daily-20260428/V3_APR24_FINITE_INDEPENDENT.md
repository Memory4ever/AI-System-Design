# 04/28 有限非作者终判与写后复核

复核者：`apr24_close`，不是本日报或这些 Books 新段的作者。按当前 AGENTS、Research/Report 合同、Sources 每日范围、统一 Prompt 和 ROADMAP 恢复。仅处理最终矩阵 65 身份及 13 个已认可子集；945/845/111/88 都不是候选或全文队列。原有身份、v1 和命题未变的 root 独立证据复用，新增段落实际读正文与邻接，不按作者 note 自签。本页是有限汇总，不是全日通过收据；正式报告与机械/日级终核仍须后续完成。

## 分母与有限改判

13 子集复用本日 ROOT_* 记录：22782、22783、23467 的 source/实写，22981、23036、23073、23080、23205 的具体 Existing，23108、23150、23577、23051 的 source/写后。24618 另直接核官方 v1 §3–4、A.3–A.4 与实际 Ch66：270 无提示场景不等于 1485 valid continuation（256 seeds×3 cuts×2 reasoning modes 原1536，删除无效）；7% 是受测 continuation 条件分母，3 epochs/Opus4.7 1 epoch，未观察不等于零风险。写后通过。

矩阵原 9 个拟前关中，24542 与24579 必须恢复，其他7维持具体前关。因此在其它身份不变时最终为 **71=13+65−7** 家族。不是给原始库存设保留率。

- 24542：官方 v1 §3.1–3.3/§6/AppE 的 all-layer LW 对 N−3 单层、detector-aware 同攻击对照，改变 sensor 深度覆盖选择；不能以“全层实例/已有 probe”遮掉真实受限新取舍。5安全深入/仅报告；FPR12–22%、λ=5 VPI residual76.5% 保留，不写普遍防护。
- 24579：官方 v1 §III–V/VIII-B 的 first-passage 共同 estimand、拟合及拒绝不合格模型是真数学测量对象；只有合成验证不单独否定理论贡献。5标准/仅报告；KS未拒绝不证真实 Agent Markov，真实 trace、独立性及映射完整性未证明，不作 operational certificate。
- 22985：已直接核官方 v1 §3–4 的 AST 等价/semantic-token sensor、混合 AUROC 与 calibration 不同及 invalid3.4% 排除。当前 Ch66 schema/uncertainty/slice 合同未实际写出这两个特定方法，不能把泛主题作 Existing；5标准/仅报告，受限 FC 实验不改通用 effect authority。
- 23747：直接核 v1 §2.1/2.2/Table2。纠错必须5深入，非标准；当前 Ch36 DP 的 aggregate g/检查 token normalization 不足承载全部 micro 梯度到 CPU optimizer owner 及全 rank/全 micro loss sum/count 先归并的两个具体失效。授2窄段；DeepSpeed0.18.9/OpenRLHF0.9.10、ID/OOD反向及跨方法控制未齐必须保留。未写/未写后不能登记整合。
- 24013、24622、24708、24608：原 Only 理由遗漏实际调度、训练初始化、异参数共享梯度、逐 query head readout 的选择差额，均5深入整合；不因未改变通用 authority 将真实机制降成配方。23210/24203 为5安全深入Only，24320/24763 为5标准Only，均保受限评价与反例。

## 全矩阵 source→actual owner 终判

以下 source 命题已经有限核，不再需要无差别重读附件。每项原必要笔记入口在 V3_FINAL_DECISION_MATRIX.md；原文采用均 exact-v1，必要公式/证明已定点直接读。定位不是用 source marker 代替正文。

| 组 | 已核家族与实际 owner/窄命题 |
| --- | --- |
| Ch17/22/28 | 23434 bounded activation 的 T/P×架构 regularization/capacity 边界，阈值不自动 controller；24432 chunk direct→summary 的完整可见性 handoff、三段 cache、非无损；22778 activation transient vs weight persistent，谱值不继承方向，warmup42.7%表现差非失败率。 |
| Ch24/26 | 23552 teacher初始化后蒸馏仍重塑 near-copy、SSCD非privacy；23994 NF/FA候选未来依赖非真实未来；23121视觉drift正则+每flow步双velocity成本；24447同cycle旧KV早步/newKV晚步；24391位移重映射后复用/新视野强刷；24086历史pose→当前ego、LiDAR为CMDP cost非已实现hardveto；24622 learned endpoint posterior/variance训练与一次refine非旧cache。 |
| Ch31/33/36 | 22785 selection-feedback与jointcollab归因不同；23838不同权重pipeline multiplex vs同pipeline tailmerge/KVrecompute；23318 opposing-set span/Sinkhorn×原adv非因果；23333 MCsolvability probe BCE与policy margin分开；24003短窗截断混杂+正确低conf/错误高conf双mask；24005 teacher成功prefix导航 vs student短prefix扩展；24013 AG本地slice先算/RS外送partial先算仍wait；24708异θ求grad却同步同平均gradient，周期参数均值非LocalSGD；24088 RMS α/FWHT/absmax s两metadata、lossy codec成本。 |
| Ch49/76 | 23475 ranking score与保护集不同artifact；23798 un-sum-renorm monoid只merge无减法逆元、不降总二次work；24008互补sample weighted-channel coverage非per-channel scale，1−1/e只coverage surrogate；24040同表format→retrieval rank而非reader attention；24608逐query subset readout非底层skip计算，跨域退步/label/router成本。 |
| Ch66 | 22891 competence/selfPIR/NullPIR三对象非纯因果；23099总体S与failureX不同，posterior mean≠实题库S*；23455同incident症状/后台fault、87corpus25test；23488训练来源×验收来源非自然作弊率；24300gold支持集×实际帧预算、5%visibility协议；23321target-modality admissibility与semantic rank；22937dev FP/FN checker-set ADD/REMOVE/REPLACE→冻结heldout；24401None/fragment/full同题，3–4%只AN内。 |
| Ch72/81 | 23374 memoryread恢复lineage/sink显隐control事后audit非线上授权；23459PR/ER/HA/HT×benign双机会分母与环境反向；23283earliest incompatible K/X frontier、nondecreasing可ties、无worldundo；24222task跨API vs API参数经验、Reflector修订/weight非FIFO、doc/effect独立。 |

具体 Existing 通过：23178 Ch66 judge身份/展示顺序/style与任务先校准，CoT/swap非通则；23581 Ch69 immutable trace→dependency graph→backward slice→reproduce/abstain，低分parent非因果；23711 Ch72当前context可观测/攻击者查询权限、非训练MIA；23781 Ch66 Living-world/ClawMark 已有exogenous loud/silent mutation、clock/backend/post-turn invariant；23853 **Ch69 TraceCard唯一owner**，preserve/prune/repair需behavior+cost receipt（非Ch66/84主题）；23932 Ch36 WAN pseudoACK/segmentedfeedback/destinationbudget，ns3非生产；23950 Ch23早/晚可见信息+sink/diversity/完整回读，foreground非truth；23987 Ch66 model+task calibration双Gate，exchangeability/分类受限；24074 Ch66 EvalSpec prompt-variant distribution/spread，非真实harm率；24594 Ch84 retrieval→Load/Abstain→paired marginal utility，goldpresent不等loading/utility。没有强迫这些项再造 diff。

四个争议终态充分：22879 computationalZK不推出Shannon1bit/多次谓词泄露；22888 printed P/R/F1算术与聚合不自洽；23584 cosine拒绝后的替换码不独立、MINE下界非privacy上界；24118 Alg1拒绝T→改写T′→直接ExecuteT′没有再次audit。只隔离这些printed中心主张，非全篇/所有经验无效、非已验证实现漏洞；重开需相应修补证明/指标分母/再审协议，不无限读实现树。

7前关：22871程序攻击搜索在当前Ch72 adaptive Skill revision/mutation/oracle/预算下未新增独立有效性条件（三臂多部件/单dev不是一般因果选择证据）；23238词标记句删除身份已纠正，保answer不证trace utility/transfer，旧proxy梯度不再采用；23941端侧grounder/data配方的离线action匹配不改proposal→effect合同；24198 active DataPRM三值与可恢复探索/silent错误在Ch66实际state-diff/neutral/verifiedbadtransition已有，40.89/44不能作确定收益；24583 exactspan subtract αabsAdv正样本减正/负样本更负，PRM/高α反例仍是既有spancredit+visualoracle+retry；24715 dense→hybrid逐层probe/蒸馏/long-context校准已有、NoPE/gating不自动迁移；24764 geometry proxy与动态/画质多目标recipe未超现Ch24 metricgeometry/gate/退化回退。3额外分层负例23466 CuTile/Triton跨GPU排序反向、24441静态GUI outcome选择非执行effect、24647层异质配额/InfoNCE queryfree proxy均维持具体前关。普通无信号库存未全量验真；root已独立9负例复用。

## 实际写后状态

已实际读正文+邻接且窄命题通过：24618、23121、23333、24447、23318、24003、24005、24391、23838、24008、24013、23374、23459、23475、24040。22778的42.7%表现差、23798的monoid只merge修复后实际再验通过。最近24086/24622/24708/24088/23434/24432/24608、Ch66八处及最后22785/23994/23552/24222/23283命题通过；纯衔接修复待最后实际确认：24608不能打断Packing引导与list，23434/24622/23321/23283移到不匹配标题前，23488移到CHERRL收尾后，24432明确partial-chunk两端盲区。作者已通知大部修复，但本页不把通知代替actual。

普通余项仅：23747两段实际落笔及独立写后、上述位置修复复读、正式71条自包含Report/来源日期与机械/日级检查。真正外部5来源date/bodyHold按本日具名有限恢复记录隔离，不伪装以上ordinary工作。已认可有界08–09日期组合不视为精确公告日志；不扩大日窗。没有修改本日作者报告、Books、共享索引或LEARNING_STATE，没有stage/commit/push。
