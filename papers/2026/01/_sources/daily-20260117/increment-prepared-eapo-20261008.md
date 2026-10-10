# EAPO10306：agreement-selected RM refresh 的有限接口

exact-v1 https://arxiv.org/html/2601.10306v1；已完整AB准入校准，拟2+1+2=5标准。必要原源increment-eapo-method-20261008.json（§2.2–3.3/§4）、increment-eapo-eval-20261008.json（§5.1–5.4）、increment-eapo-appendix-20261008.json（AppA成本/协议与B局部NIAH），current轻检increment-eapo-current-20261008.json。不是所有references/附录队列，不采后v2未读机制。

机制：EAR把analysis/逐字evidence/reason/answer分阶段，格式错误立即结束余reward；RM同一次消费本query的rollout evidence集合，整数1–5再normalization是group相对信号，tie/细节未完整，不补执行recipe。Ra是LLM judge对GT semantic一致，不是现实真值。policy同时消费format/evidence/outcome加权信号。RM每20RLsteps用recent policy样本refresh，但只准入高RM分+答对、低RM分+答错，agreement-selected population；错证据恰好答对仍可能高分入选，分歧样本被丢弃而非修复，不能自证evidence正确/泛化或把outcome反推每步truth。

必要支持/反侧：§5.1 Qwen3-30BA3BThinking固定设置比较outcomeGRPO与staticRM，static约50step饱和/full继续只是局部曲线，不授matched总成本或普遍训练收敛。§5.2 N6 BoN的oracle是gold-conditioned Gemini evidence的最大ROUGE-L Recall，69→74%/60steps是该排序proxy吻合，不是human process truth；没有据此认证新证据绝对正确。β.3 peak63.1但β.5回59.2；局部EvidenceError17.7→13.5/ReasonError20.7→15.4作者judgelabel无完整N/CI，不证明evidence唯一瓶颈或全部causal。初始oracle/tressampling有gold-answer参与且额外beam/critic费用，63% ceiling是受限理想辅助，不可部署复现全guarantee。

费用：AppA VeRL温度1/120k输入+8k输出/G6/globalbatch64/mini32/LR2e−6，16H20 90GB；作者报告30B RL约72 GPUhours/14B40 GPUhours与RM SFT约2 GPUhours，不写72wallhours或所有refresh/生成/teacher总账已覆盖。Rollout、组内RM、gold-answer judge、周期SFT、静态对照与回归都计入采用条件，precision/完整refresh累计费用、seed/CI/端到端SLO NotDisclosed。NIAH仅披露网格无error，非全context绝对检索保证。

日期：increment-datacite-10306-20261008.json Submitted Jan15T11:40:57Z、Updated-v1 Jan16T01:38:54Z、formalIDregistered Jan16T02:52:13Z，与已核official normalannouncement下界/ID只随announcement赋予上界，普通未提前公开条件下Jan16自然日；不是单字段证明firstpublic。当前abs v2Apr20、同题无可见withdraw/correction/safety标注；必要v1原文未指直接更早同全文，不宣称已查全互联网。

actual Books作者顺读Ch31:170–206（candidate distribution漂移/闭环，Preference Admission保被拒绝数据及selectedmass/support反侧）、1059–1091（process信号权限/计数与generator条件、RM/policy/evaluator分离与独立holdout/回退）；Ch33:375–399是另一prefix probe/loop supervision不借题相同当Existing。现Ch31有成熟refresh与selected admission偏差约束，但未明确本篇两轴高证据分×答对/低分×答错局部filter，不能把主题覆盖授具体Existing。拟标准OnlyReport：保本文agreement-filter实例、staticRM/BoN局部证据和可能self-confirming支持域，不因该recipe新名新增长期段；若root认定对outcome到process的准入关系确有长期差额，可在Ch31 candidate_distribution后或Admission邻接提唯一窄gap，需独立PRE/锁后才写。当前不自授最终Books或DAY。
