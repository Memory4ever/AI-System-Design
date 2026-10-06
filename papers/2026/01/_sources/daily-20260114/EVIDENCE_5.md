# Jan14 整日抽查的五项定点恢复

本文件仅补此前标题库存中的五个具体漏收风险，不扩大334线索为逐项队列。21完整题摘=原16+新增5，12已处置集合不作配额。五份exact-v1题摘见RESUME_FIVE_AB/CORE_INDEX；必要HTML原返回均JSON string，用`jq -r '.'`读。原始DataCite字段见RESUME_FIVE_DATE_FIELDS.jsonl；它们只联合已核公告规则界定条件公开区间，不冒称first-public日志。root已实际校准五题摘贡献/原分；RoRA、Sky、Speech必要源→owner差额及Sink具体Existing已通过。Ch30/63/66与Ch33各窄正文+末注实际写后root非作者POST通过，所有共享窄锁释放；五DateFields条件日期已root实际核，root最终独立日Gate通过。

## 2601.06305v1 — Why LoRA Fails to Forget

拟2+2+2=6；基座继承有利于任务保留，但不等从poisoned base消除trigger；低rank之外须分更新强度、方向、clean/ASR两人口。必要§3/4.2/5与A.1/A.2：CORE_INDEX L78–132、RESUME_RORA_CORE L156–195/417–449、EXTRA_0 L359–365。RoRA是基座dropout、原谱soft penalty与top3 layer rescale的有限recipe；pretrained谱不是真实trigger subspace oracle。RTX5060Ti16GB/309024GB，BERT/RoBERTa/Llama，BadNet/InSent、SST2/CR/CoLA，rank8/16、FT20/5epochs和参数搜索；若干baseline引用旧论文，其他结果best-of-runs，不授等预算平均效应，precision/runtime/fullcost Not Disclosed。大scale会损clean，部分变体ASR仍高。

Prop4.2 A1原≤-rho_bd，A.2 Eq16误换为≥，故阈值保证单隔离：C2,d1,x=xtrig1，Wpre=(-1/√2,+1/√2)^T、Δ=-Wpre，谱范数均1；rho_bd=.1/rho_cl1/rho_tr0满足原A1/A2，s=.2>.1阈值但margin=-.8√2仍负。不开全附件审计，不因此删除有限recipe。重开该保证仅需有效坏margin下界/作者勘误及多层模型适用条件。目标`TRAIN-LORA` Ch30:98–107继承基座后窄差额，不复写rank通则。

Eq10 U/V未标截断维度，Fig2 top32是观察分析；限定find `truncat` 无命中见RESUME_RORA_BASIS，并不证明作者实现不存在任何截断。完整正交U/V会使soft penalty等于factor norm，故不补造实际top-k/trigger避让实现，不把图上相关性授予方向oracle。Ch30新增107与末注814只写继承风险/强度方向审计/受限尝试和重测对照，root必要原源及owner已核，实际正文/邻接/末注POST通过。

## 2601.06329v1 — On the Fallacy of Global Token Perplexity in Spoken Language Model Evaluation

拟2+1+2=5；混合语义/声学globalNLL不必拥有局部声学一致性测量权。必要§3/4/5.2–5.3/Limitations：RESUME_SPEECH_CORE L103–140，EXTRA_1 L169–180，IDENTITY L211–212。共享prefix后0.5s窗口的conditional NLL与减无prompt NLL分别改变评价人口/校正对象；实际生成MOS与embedding judge是另接口，不互授真值。SALMon六属性，9model×50sample×5annotators；judge按同benchmark prompt资格选择，不能授跨域独立judge或社会真值。局部方法也可能损害HuBERT人口，compound shift未测；新增judge/双score成本，modelGPU/precision/concurrency/fullcost Not Disclosed。目标`PLATFORM-EVALUATION-SYSTEM` Ch66:80–116 EvalSpec具体metric人口差额，或只报告有限recipe，待独立Books裁决。

## 2601.06520v1 — SkyNomad

拟2+2+3=7；单region price/availability不足，跨region需将spot寿命、coldstart、egress与deadline剩余进度同账。必要§4.1–4.7、§5、§6.1–6.2.5：RESUME_SKYNOMAD_CORE L171–321，EXTRA_0 L325–377，SKYNOMAD_EVAL L393–460。单固定gang、periodic checkpoint、事先已知P、ready速度1与d界、od alwaysavailable前提限定；probe/virtual-instance/survival是预测不是预约承诺，risk/egress/hysteresis成本真实付费。AWS Qwen3-4B/14B，4L4/8A100/4A10G，同期开baselines，30hwork/45hdeadline，100/500GB，6mincoldstart；GCP H10014day与AWSV100 trace sim20jobs，不能照录headline全局最优10%，实际部分11/12%。无slack全fallback、one-region无选择增益、多region饱和、大checkpoint放大迁移成本；precision/trainingbatch/fullquality Not Disclosed，调度收益不证明模型质量变化。目标`PLATFORM-GPU-SCHEDULER` Ch63:84–95 restart效用后一窄段，不承担Ch35checkpoint correctness。

## 2601.06787v1 — Garbage Attention

拟2+1+2=5；BOS attention sink只是head候选代理，功能须受限任务ablation验证，不从head mask推生产加速。必要§3–4/6/7/8/Limitations：RESUME_SINK_CORE L118–153/184–237与EXTRA_1 L239–276。MMLU初始decoding attention用于calibration；head通过WO对应slice zero实现，维持shape并非kernel物理删除；block剪枝与head不同、首尾保留。GQA Gemma3-4B/Llama3.1-8B/Qwen3-4B，4096max、WikiText及八任务mixedshots、baselineGQA重实现。Llama block25%大退步且TopDown高于作者方法，headPPL与downstream排名错位；hardware/precision/calibrationbudget/fullruntime Not Disclosed。softmax 1/T不自动推出BOS权重必1/T，现象只有限观测。拟只采用proxy/functional/effective-execution三层分责，`MODEL-MULTI-HEAD-ATTENTION` Ch15:111–119已有具体覆盖，不声称已有exact scoring recipe；待root实际裁决。

root已实际核WO-zero/固定shape和有限ablation，Ch15 head冗余段111–119具体承载proxy≠功能/生产加速分责，Existing通过，不写重复正文或新增源注。

## 2601.07182v1 — PRPO

拟2+2+2=6；sequence broadcast粗credit之外，entropy分段PRM local项与组内outcome shift拥有不同权力。必要§3/4/6/7及B/C：RESUME_PRPO_CORE L80–150/201–226，EXTRA_2 L239–251/300–436。AF=zprocess+beta，固定0.5/0.289基于[0,1]的uniform prior不是实际PRM概率校准；entropy峰不是必然语义边界，formalcollapse本人也承认incomplete，不采用无collapse保证。8H200policy+8H200PRM，batch128/8rollouts/2048tokens，MATH12k earlystop epochs差异；AIME/AMC mean32和MATH greedy不合并。random/uniform split大退步，AIME2025有反退，PRM服务器增加step时间且总预算不同，precision/fullcost Not Disclosed。目标`TRAIN-GRPO` Ch33:195–199 coarse broadcast后一窄段，保outcome-only/可靠process共存。
