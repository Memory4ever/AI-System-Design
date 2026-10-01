# 2026-09-30 root 定点证据与采用说明

窗口为 `[2026-09-29T09:00:00+08:00, 2026-09-30T09:00:00+08:00)`。以下为精确 v1 原文审阅，不是实验复现。官方 09/30 新公告身份及 availability 日程推定公开为 `2026-09-30T08:00:00+08:00`；Submitted 原值不用于代替公开。当前官方事件页未见撤回信号；更早作者正文出现时优先校正，不声称穷尽互联网。

评分依次是 Design Delta / System Reach / Durability；6 分而深入，是下列明确长期缺口或设计纠错触发，不为修改 Books 升分。正文不采用速度数字，以下评价条件只限定证据。

## [Local mixing without explicit position encoding — 2609.38109v1](https://arxiv.org/html/2609.38109v1)

2+1+3=6，深入。§III–VI、Appendix A：局部混合产生矩阵 lag moment `G(d)`，Q/K 对齐才把局部相关变为 expected recency；零均值独立随机投影的期望不自动有 recency。中间 MLP/normalization 会改变传递，causal mask 已引入不对称，因此“无显式PE”等于“无顺序信息”是错误绝对句。120M/350M、12B/24B 训练 tokens、8192 长度、48条8192序列与4096-lag诊断只支持有限模型，不证明无限长度或量化迁移。Ch13 已实际修正显式PE必需的句子并补局部机制与条件；主 owner `MODEL-POSITION-ENCODING`。非作者 sep30_independent 写后复核三处条件通过。

## [STEPQuant — 2609.38169v1](https://arxiv.org/html/2609.38169v1)

2+2+3=7，深入。§2–5、Appendix F/H：相同输入/gates 下，误差随 `E_t=A_t E_(t-1)+epsilon_t` 传播；temporal retention 与 spatial readout 是不同敏感度，不是已证明统一最优乘积。当前浮点 state 更新并 readout 后量化写回下轮；packed codes/scales/pivots 必须共同 ready，双缓冲有容量代价，gate 分布近似不保证不同生成轨迹。Qwen3.8-27B/KimiLinear48B-A3B，BF16/AWQ W4，4×A800 TP4；校准32条WikiText2×2048；计时prompt128/output1024、batch32–512、3次warmup后运行、slowest-rank decode间隔，排除prefill/启动/交付，SLO未披露。state-update速度不是tokens/s，4-bit退化保留。Ch54把既有recurrent段移回减少Bytes主线并增加上述生命周期；`INFER-GPU-MEMORY`。写后独立通过。

## [evalstats — 2609.35815v1](https://arxiv.org/html/2609.35815v1)

3+2+3=8，深入。§2–6、§9.6/B1：judge agreement 不是CI/test calibration；随机MCAR人工配对残差与预测辅助估计必须绑定estimand，不能把便利样本当代表性gold。估计λ的方差及收缩改变power，小N的bootstrap CI失准不等所有bootstrap禁止。2,046个null scenarios/test、200 Monte Carlo、九检验约3.68M实例是条件模拟，不是生产可靠率；tool单factor、≥50judge/≥15human，不证明未实现paired/multirun接口。Ch66补抽样、估计、检验三者分账；`PLATFORM-EVALUATION-SYSTEM`。写后独立通过。

## [OLIVE — 2609.36246v1](https://arxiv.org/html/2609.36246v1)

2+2+2=6，深入。§2–3、§4.1–4.3、§5.1–5.2：student新prefix→teacher在自己的后续prefix采样M个token；CE只覆盖teacher continuation，不覆盖student/prompt/env observation，可text-only跨tokenizer，不需teacher logits。不是“teacher每token在student状态纠错”；不可恢复prefix及异步d=3滞后保留。RLVE9K/18 games、Qwen1.7/4B student、4BThinking teacher，cap7168/prefix4096/suffix1024、8H200；top16-KL对照不是精确全KL；Agent5Gym不同teacher及API ScienceWorld是独立配置。reasoning4B pass@8 teacher53.3/OLIVE52.2，不可用avg@8结果称全指标超teacher。Ch29的最小缺口是rollout边界与CE监督边界分离，交 sep30_evidence_check 采用；`TRAIN-SFT`。

## [Risk-aware intrinsic self-correction — 2609.35832v1](https://arxiv.org/pdf/2609.35832v1)

2+1+2=5，标准。PDF §3.1–3.3、§4.1、§6 limitations：29 open-weight模型、BoolQ/GSM8K/Corr2Cause及matched11-model/5-prompt切片；必须分ECR/EIR和初始正确率。gate在产生revision前可省生成，后验acceptance不是同样预算。作者只恢复2组GSM8K初答/修订文件；gate汇总缺对应paired records、frozen configs及disjoint IDs；相关收益仅descriptive，不作为经验证无偏gating优势。Ch80已有 `(1-A)ECR-A EIR`、verify-first和budget的具体推导，已有覆盖 `AGENT-REFLECTION`；不写入不可核的selector收益。PDF HTTP恢复后读必要章节，不把工具cache miss称正文缺失。

## [ATTUNER — 2609.36722v1](https://arxiv.org/pdf/2609.36722v1)

2+2+2=6，深入。PDF §3.1–4/Fig3–5、§5.2、Appendix D.2/E：独立cache丢跨artifact conditioning；只修位置不充分。oracle保留PIC values但读full attention rows，诊断支持query-side适配，不能证明values永远无误差。训练冻结base，只学query LoRA，在uncached/online token启用，沿原norm/RoPE，部署合并WQ；artifact KV不变，online state/newKV变化。full-context teacher响应及KL监督不是在线oracle。Qwen3-4/8B、五任务；warm-cache TTFT含load/assembly/online-prefill/first-token，不含离线构造，median而非tail/SLO（SLO未披露）。跨域TheoremQA可下降，未测三类artifact混合或其他attention，storage/transport不由此优化。Ch45增量是cache consumer适配与cache producer稳定分离；`INFER-KV-CACHE`。

## [Hidden system-prompt dates — 2609.36931v1](https://arxiv.org/html/2609.36931v1)

2+1+2=5，标准。§3–4 prompt/evaluation（§5.5仅precision/batch受限对照）：冻结其他输入并改变2024年system date，九模型/六数据集/四task types；date是确定性输入干预，不是随机采样噪声，proprietary一周调用仍有漂移风险。不是所有date总比其他CV因素强。Ch66现有run identity、完整system prompt、cohort/render、resolved-model receipt已实际要求记录此变量；已有覆盖 `PLATFORM-EVALUATION-SYSTEM`，不为新案例重建owner。

## [Correct, Don't Delete — 2609.37624v1](https://arxiv.org/html/2609.37624v1)

2+1+2=5，标准。§3.2–3.3、§4.1–4.2、§5：固定nested10/25/50% poison及25%/1712 rows，rewrite Gemini3.5FlashLite保format/length；paraphrase保misinfo但不是完美control。主rank1 LoRA单层857updates及第二Gemma配置、三seeds、56questions×20temperature1，三个judges/两个vendors；EM条件coherent>50/alignment<30且分母为coherent输出，不是全系统安全率。很多对照不确定，不能把inconclusive当等效。corrective替代在一组而非两组稳定优于clean，correction影响与attribution deletion不等价。拟补Ch27删除/纠正不同intervention及配对canary，不写“纠正普遍优于删除”；`TRAIN-DATA`。

## [Attention retrieval capacity — 2609.37879v1](https://arxiv.org/html/2609.37879v1)

2+1+3=6，深入。§2、§3.1–3.4、§4：按dense attention weights或alpha*norm(V)选TopN，保原weights不renorm，在每个长度相对原模型NLL判断依赖，不是所存事实数。128 targets，L256–2000/50docs；BABILong固定support/100contexts到4k，Qwen非单调。删除误差 `(1-M)mu_T`、renorm误差 `(1-M)(mu_T-mu_S)` 属不同干预；先全量attention后筛不证明加速。拟补Ch14 mass/value/direction和诊断干预边界；`MODEL-SELF-ATTENTION`。

## [SchurReplay — 2609.36654v1](https://arxiv.org/html/2609.36654v1)

2+2+2=6，深入。§4.1/Eq12–14、§4.2.1、§5.1/5.3、Appendix D4：future列可连续补偿时，当前group成本用Schur complement而非裸H_GG；这不是最终离散全模型最优。每个scale候选从同group-entry state私有回放真实顺序GPTQ E2M1 rounding，只有winner提交residual；candidate/row并行不改变列顺序。Qwen3.5-397B-A17B/Llama3.3-70B W4A4、255条seed42 decontam/max16384 cal；greedyT0/p1/max8192、15,461 questions/七任务评测，h8不总胜h4。拟补Ch49条件曲率+私有轨迹提交，非仅扩大scale search；`INFER-TENSORRT-LLM`。非作者指出原154,617误记，现按§5.1更正。

## [AnswerPool — 2609.37494v1](https://arxiv.org/html/2609.37494v1)

2+1+2=5，标准。§3.1–3.2/3.4、§4.1/4.3、§5：同topic N题option合并/去重/打乱，单个option只用一次使assignment耦合；与equal-sized不相关pool配对，区分多题排除收益和question-answer binding。unique valid option是前提，2/3-LLM ambiguity screening不是gold oracle。18模型/七bench+CEval，较大pool改变context和任务；jointchance `(M-N)!/M!` 不等原k^-N。未采用§3.3缺失答案变体。拟补Ch66 coupled diagnostic和task-equivalence边界，不能把新排行称原benchmark真实能力；`PLATFORM-EVALUATION-SYSTEM`。

## [ParaAnya — 2609.36522v1](https://arxiv.org/html/2609.36522v1)

2+2+2=6，深入。§2–4/Algorithm1–2：PinT迭代反复访问同timestep，cache `(xhat_t,epshat_t)`；仅miss调用UNet/更新pair，solver仍用自己的更新形式，但x与cached x不同使eps近似，非exact trajectory。τcache独立于solver convergence τ。固定model/conditioning/timestep是cache语义前提，变化失效是本项目工程推论。SD1.5半精度UNet/xformers、512²、1000COCO2017相同prompts/seed/noise，DDIM25/50/100、P16，8V10032G对8G未缓存控制；serial1GPU对8G不是同资源speedup。H100单独window/threshold消融；warmup1排除。τ=.001/.005虽省NFE反而较慢，大τ快但CLIP略降，CLIP与LPIPS不证明全部感知质量/输出等价，concurrency/SLO未披露。拟补Ch49跨迭代同timestep cache与hit-check/communication预算；`INFER-TENSORRT-LLM`。

## 贡献前关闭与日期隔离（独立纠错后）

- ER-JEPA 2609.36952：原初筛拟关闭，但非作者查到 matched-compute/token/current-batch control 隔离了旧样本replay的增量，原“成熟replay组合”理由不足，已重开为标准审阅候选，不删除反证。最终证据/owner待本项审阅闭合，不能继续计入前关闭。
- MoK2609.36070：Cursor同机制正文2026-08-04已公开，不将arXiv迟收录作新事件。
- Alignment Forecasting2609.35805：四作者正文2026-09-25已公开，不重新计本窗first-public；日期时区未披露不造精确归属。
- Environment Steering2609.35807：Aug31 NOVAS展示只是一条早期body线索，不能证明全文日期；官方精确OpenReview/作者body日期不能恢复，隔离不用于当窗候选或Books。

## ER-JEPA 重开后的标准审阅与已有覆盖

[2609.36952v1](https://arxiv.org/html/2609.36952v1)，2+1+2=5。非作者 sep30_complement_review 读§2.2/Eq5–6、§3.2–3.3、§5：保留raw source/target token pairs，用当前模型重算两视图并执行target CE+cosine JEPA，不固定复用旧hidden。SYNTH/Llama3.2-1B，六40.05–240.31PFLOPs预算、五seeds；token-matched及same-replay-loss/current-batch控制支持历史内容的局部独立作用，不能归给更多tokens或特定选样规则。2000测试轨迹的correction与retention分账；paired-view、β gridsearch及额外训练成本保留，episodic path推理移除不等训练免费。当前官方无query CL新列表第80项确认本期公告。

已有覆盖 `TRAIN-SFT` / Ch29：latent loss/CKA/cosine好转不替代heldout行为、acquisition/retention与连续checkpoint、历史replay/配方身份及双域holdout三段均实际存在。root对读这些正文后采用No Change；保留本窗局部新验证和控制，不添加JEPA命名综述或把它误路由成World Model。

## 27项他作者 Books 实际写后验收

root作为非写入者逐项对读源证据及实际增量/前后段落：sep30_independent的Purlin/Cobalt/CadenceRL、Janus/WUSH、DScale/SEED、vSkipper/SPLASH/Sieve十项；sep30_complement_review的Honeycomb/Helix/Rho/Delta-Matching/SOMA/ToolFence六项；sep30_evidence_check的LUDI/RPD/E-MoE、ThinkOPD/OLIVE、compiler、ProVer/AdviSD、MATE/MGPO/Mnemon十一项，共27项。均保持唯一owner、旧方案与局部限制。发现compiler把depth区域误写训练阶段、full-stack rank4误写full-rank末四层，已按精确§4/AppendixG.1纠正；ProVer插入造成旧milestone指代错位已重排；LUDI数字留证据笔记，正文改为适用条件下的成本分账，不以不完整性能contract宣传普遍速度。修正后实际复读通过。此结论不自验root写入的十项；它们由另外的非作者分别核，记录在各独立笔记及正式报告。

以上原“拟补”的十项现已真实落实到各 owner 正文。Correct, Don't Delete 与 AnswerPool 虽为5分，分别针对删除/纠正的干预差异、共享答案池的耦合任务与概率前提补读方法、对照和限制，满足具体长期缺口的深入审阅；不靠调高评分取得采用资格。最终五项标准审阅为 self-correction、hidden-date、ER-JEPA、MultiTalk 与 SYNTH 新对照证据。

本笔记不单独签整日Gate，正式报告及最终独立复核仍为最终入口。
