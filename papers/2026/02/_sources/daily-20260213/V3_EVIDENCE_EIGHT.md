# 8 项已校准候选：必要证据与 Books 差额提案（非日级完成）

只读精确 v1 HTML 的方法、关键评价与直接反侧。以下为作者判断，待 root 逐项必要源复核；不以已读篇幅、仅报告或 Books 已覆盖改变准入/评分。对应 raw 为 `V3_EVIDENCE_<ID>_INITIAL.txt` / `_EVAL.txt`，实际 L 范围保留在原返回。

## 2602.10300 — NCPL（6）

精确 v1 §3–4，INITIAL L111–209、EVAL L210–260：完整 source/architecture/optimizer 配置序列化，由 number encoder 与 Qwen3-1.7B regressor 预测相对 Chinchilla residual；3225 train/796 ID/1109 OOD，按 optimizer/N/D 分组，训练模型最高430M、外推至1.2B，仅 Marin/StepLaw 两个人口。数据删去不稳定/未收敛 run，不能覆盖失败配置。StepLaw OOD 的 scratch135M MAE .0199 优于 fine1.7B .0223，XGBoost .0246；Marin fine LLM 更好不意味着 LLM 回归普遍必要。高 LR OOD 仍有 bias，未验证 MoE/linear attention，预测器准备成本、硬件/精度/concurrency/SLO 不采用未披露值。

Ch7 当前 joint-hyperparameter/heldout scaling（L233–247）已说明不能只看 N/D；本次有限两源配置 regressor 不建立可外推的通用新 scaling law。提案仅报告这条替代拟合路径，而非说具体 NCPL 已写入 Books。

## 2602.10314 — PUMA（5）

INITIAL L100–181，EVAL L182–280：训练 forward masking 采用 teacher-forced、按当前模型 confidence 次序揭示正确 token，复用当前 logits，streaming chains、refresh 与 K scheduler 管理计算。理论 posterior 一致性需固定 reveal policy、single-position/完整真实 posterior；实际 multi-position 独立近似不等于精确 joint marginal。指数→线性复杂度还需可识别有限 latent family/oracle 条件，不能外推任意 LM。

125M/14层/512 hidden、TinyGSM11.8M、8H100、batch32/GPU、900k steps、3 seeds；Sudoku6.8M/2H100 是另一人口。较低 confidence threshold 和无 K scheduler 会退步；AR-init 的30k steps也计成本。iteration-to-target 不等价固定 FLOPs 或全服务收益。Ch24 当前 teacher reveal/order 与 token factorization（L278–336）没有这条 online forward-law 条件：提案窄差额是“根据模型选择揭示顺序时，训练 mask law 的 posterior-preserving 条件仍需独立成立”，并非 PUMA 名称或加速数字。若 root 确认长期差额，再定点读必要 Appendix A 证明，不遍历其他附件。

## 2602.10346 — Top-W（5）

INITIAL L81–178、EVAL L178–317、必要尾 L335–398：固定可行1-Lipschitz potential f 的 scalar score，W1+entropy−log-retained-mass 目标在 β≥λ 下有 prefix scan 解，β≤λ 时 singleton；实际 top_m=1200 与3次交替、nucleus warm start 不等于精确 OT 或 global alternating optimum。词向量距离只是语义代理，不能保证最终文本质量。

同 prompt/stop/maxlen 的 Qwen2.5-3B/Llama3.1-8B/Phi3-Mini4k、T=1/1.5/2；GPQA Llama T1 .308 低于 TopP .3281，Phi T1 与 TopH .3237 持平。GSM3 runs/GPQA4 runs，creative 3 prompts 共27 judge 比较，TopW9胜、其他8/5/5，单 GPT4o judge 不是人类通用创造力证书。转换/geometry 有开销，runtime 不采用未冻结设备、精度、batch/concurrency/SLO 的普遍数字。提案仅报告具体几何 crop 替代算法；不把成熟 sampling 原则借成已经覆盖此算法，也不以 crop optimum 授语义正确性。

## 2602.10352 — Trained SelfIE（5）

INITIAL L112–290、EVAL L309–365：冻结 LM，affine activation adapter 送入解释 prompt；scalar scale+bias 仅 d+1 参数，bias-alone 解释约85% CE 改善，full-rank 的 train/heldout 差距显示标签拟合。SAE decoded feature/Wikipedia 标签与 paraphrase/retrieval 评价不认证 activation 的真实语义。两跳桥接 probe 先筛两次1-hop及2-hop全正确，只有原数据12%；500例、每cell10 samples/T.7 中 decoded bridge 增加不证明实际 reasoning 因果使用。

Ch5 L277–309 已有 readout/objective 与 replacement-model OOD 界，但没有“训练 interpreter 的默认 prior 与 activation 证据分开验收”这一具体差额。提案窄整合，必要 null-activation 对照 Appendix J 尚需定点读，不能把作者 discussion 当已核 null 实验或展开全 SAE 附录。当前不写书。

## 2602.10371 — Simple LLM Diffing（5）

INITIAL L104–177 与必要 dataset 说明：API-only 配对1000 WildChat responses、heldout500；hypothesis 的 frequency、direction-conditional accuracy 和 accepted consistency 是不同指标。LLM clustering 对比 reader-SAE 相似频率/泛化，解释更抽象且短，SAE 对 syntax/math 仍有优势。两条方法都漏掉 test prompts 没有 elicited 的 gender ground-truth behavior，不能由 accepted hypothesis 推未发现行为的 recall。LLM judges/rating 本身需验核，不是自动审计证明。提案仅报告有限比较证据，不能以无需权重普遍取代 SAE；目前无具体 Books 新机制写入。

## 2602.10377 — Hardware Codesign（6）

INITIAL L354–472、必要 L495–570：depth/width/KV维/activated FFN ratio/稀疏度参数化 loss surrogate，再和逐 operator roofline latency 联合搜索。170 models 各10B tokens、统一 optimizer/data recipe 不是固定 FLOPs。Fig4 fit138/32 与正文120/17分割数不一致，保留争议，不采用精确泛化样本统计。数据 mixture 未公开，heldout1B/final10steps不是下游任务质量。

B1、input1024/output16、Jetson Orin FP16/INT8 的受限 latency；未冻结精确SKU/power mode/version、训练精度/重复run、concurrency/SLO，不外推生产。ρmin 的“free lunch”依赖 latency 系数对ρ不变、固定 activated width 和不受 storage/routing 等制约，不能作通用 MoE 定律。相同 recipe 下 retrained Qwen0.5B 的单 operating point PPL改善是局部证据。提案仅报告 joint empirical search；不说共同 co-design 问题不重要，不因理论/数字争议取消已经通过的准入。

## 2602.10380 — Alignment Bottleneck（6D）

INITIAL L99–123、EVAL L124–226：oracle subclaims 下区分 aligned subclaim evidence（SAE）与重复 parent evidence（SRE），并加 no-label/noisy controls。399 parent/1169 subclaims、929 train/240 test，Qwen3-14B zero-shot/T.3/3 seeds、paired bootstrap1000/McNemar；未核 parent sibling 切分，不宣称无泄漏。Oracle SAE .6268 > parent .5643，SRE .5872 未统计显著；no-label SAE .5485 < SRE .5808，分解收益依赖 granularity/label signal。重复 evidence token budget 不同，不能归为免费结构收益。

Abstention 与 refuter 关系是相关证据，未干预证明 abstention 政策因果修复。COVID balanced-accuracy delta 与表内相减不一致、MM正文/table delta 不一致，不采用冲突数值。Ch76 L1055–1085 已有 claim-region/provenance，但没有 evidence granularity 与 subclaim label 共同决定分解增益这条边界。提案窄整合，保留 oracle decomposition/标签/预算条件，不把新数据集和相关统计写成部署保证。

## 2602.10382 — Triggers Hijack（6D）

INITIAL L78–165：GAP1/8/24B、3词语言切换trigger 对10个 matched fake triggers；1000 post-cutoff FinewebEdu、20–100词context，翻译四种Latin-script语言。mean-head activation patch 的 outcome 是首 continuation token logprob，top10 threshold 任意；Jaccard .18–.66 vs近零shuffle支持受测 head 重叠，自然语言无trigger的 shared heads 提供反侧。

这不证明完整 causal path 或通用 backdoor 必用正常 circuit，正文 §4 明确 causal necessity ablation 留未来，且1B German的层位并非统一早层。无实际 mitigation 试验；ack A100/H100不等精确测量配置。提案仅报告有限 first-token 功能复用证据，不签发部署防御或安全保证；若长期功能归因链需进一步整合，必须只针对必要因果限制判断，而非全读所有head地图。

## 旧 PRE 当前正文比较收束（作者，2026-10-04）

10314：实际重读Ch24 L300–318训练顺序/部署planner，尚无adaptive forward masking law为何保持data conditional的条件。必要AppA2 END L408–422实际核：只在forward probability除匹配指示外的α_t(x_t)与clean x0无关时Bayes抵消；不采L434把1/t写成仅X函数的展示瑕疵、任意multi-position exact或复杂度承诺。拟两段放训练order后，保留gold/固定mask回退。10352：Ch5 L277–313 replacement/pruning与OOD不承载interpreter bias的null-input对照；实际AppJ L922–943用zero activation直接隔离adapter bias，SAE/Wikipedia先验不同，定性样例不授faithful causal semantic。拟两短段接faithfulness budget，分开learned label prior和activation贡献/extraadapter。10380：Ch76 L1060–1093 claim locator/provenance和控制图已有身份责任，却未解释oracle subclaim granularity×label共同作用；拟在claim证据生命周期段加两短段，只采matched oracle/no-label反退与budget税，不采用冲突delta、无泄漏或abstention因果。三项真实窄差额待root PRE授权，不因旧PRE成本保留。

最终状态同步（2026-10-04）：本组必要源与处置已独立复核。10314 Ch24、10352 Ch5、10380 Ch76实际两段、完整邻接与末注已获root非作者POST通过，锁释放；其余只采用正文所述有限Only命题。PUMA必要A2与SelfIE必要J已经实际读并在收束段限定，不再是普通附件待办；日级另验。
