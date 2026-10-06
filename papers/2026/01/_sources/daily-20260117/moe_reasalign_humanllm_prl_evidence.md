# 四项必要差额：待 root 定点核

以下各 exact `2601.<id>v1-primary.txt` 已缓存；root 已完整AB准入。仅实际列明段，不要求非作者读无关附件。未核实现/复现。日期 normalcohort+正常公告Jan16T01Z/无已知先行全文条件成立才用完全落窗范围；Submitted/Updated不当 public。

## 10159 — domain activation 与 routing sensitivity 分账（6=2+2+2）

actual §2.2 L97–130（activationrate/CWAS 与 pre-softmax unit perturbation→outputKL）；§3.1 L132–145/3.2 L146–225（same frozenmodel up/down router）；§3.3必要token边界L313–314、limitationsL325–326/C1L612–613。关键非同义：常被某domain选中不证明它对输出有同等作用，unit gate扰动只测该层/输入/扰动定义的敏感性，改变topk及其他expert相对权重，不是isolated expert causal semantics。Eq1写−p logp没有所述Bernoulli补项，§2高CWAS与§3“低CWAS专业”口径冲突，不采精确selector阈值、expert ontology或driver causal总保证。Table1 Math上domain/driver up数值相同，MMLU则不同；routerLoRA同时训练不是free inference-only。headline acrossmodels/allgains受局部表限制。

三checkpointMixtral8×7B/DeepSeek16Bbase/Qwen1.5MoEA2.7B，三个语料SA/MMLU/GSM8K，frozenrouter perturb作者A100/A40但称RTXA100口径异常不采精确设备归因；precision/seed/完整wallclock/perturbcalibration及selectioneval独立性未披露。token位置统计未matched词面/长度/position因子，不授句首driver定律。SubmittedJan15T07:59:17Z，UpdatedJan16T01:27:53Z，created02:48:37/registered02:48:38→BJT Jan16 [09:00:00,10:48:39)。

actualowner `MODEL-MOE` Ch21 L122–126已有loadproxy≠semantics、L409–423已有load/value及frozenrouter行为改变；没直接把domain选中频率与定义明确的routinglogit perturb-output sensitivity配对。拟122–126后两短段：分别测原routingfreq和frozen-input gate perturboutput，单位敏感不认定functionalcausal专家；保topk/耦合/selector口径/更多probe成本和原router退路。Ch21首/20尾/22首已actual读。请定点§2.2+Table1/limits及owner判断；不需更多heatmap。

## 10173 — ReasAlign 意图保持训练与局部 path selector（6=2+2+2，安全深入）

actual §3–4 L82–116；§5setup L128–141；§5.3–5.7/Table1 L147–201；limitsL205–206。sixfield合成SQuADquery/context/gold +TaskTrackertrigger+BeaverTailssafe/unsafeinjections，teacherGPT4omini看到highlighted注入与expectedtarget后产problem/reason/final，LoRA学user-intentcontinuity；aligned-vs-hijacked pairedtrajectory以DPO训练logicjudge，每step N候选judge选1。judge scalar/formula/steps实现未披露，不能称DPO训练即“逻辑真值”或beamsearch保持用户所有约束；注入safe也不是trustedauthorinstruction。

Table1 final-answer-only vsreasoning：underattack ASR下降但无attack SEPutility98.9→98.0，trace训练目标/长度改变不隔离内部reasoningcause。N1→5SEP固定更强预算，N3default；费用§5.7只统计成功任务token且N1，不认证N3端到端匹配。Llama3.1-8B LoRA B4/3ep/Adamweightdecay LR2e−5/input8192；Qwen2.5-14B附加局部AgentDojo/InjecAgent非zeroASR，低8B能力导致低utility/低ASR并存。hardware/precision/seed/totalteacherjudgecost未披露。threat只trusteduser/externaltextpublicinterfaces，不coverage恶意user/其它modality。SubmittedJan15T08:23:38Z，UpdatedJan16T01:28:38Z，created02:48:59/registered02:49:00→BJT Jan16 [09:00:00,10:49:01)。

actualowner `PLATFORM-SECURITY` Ch72 policybound sensor L560–576、tracefaithfulness L813附近与goalalignment≠auth L633–641；L1308–1310 adversarialtraining/monitor 分责没有此明确safe-injection/user-intent aligned/hijacked监督与stepselector接口。拟 Ch72 goalalignment段前两段，写训练信号不是effectauthorization、外部有用指令可作为证据不升级权限；反侧/成功conditional成本/teacherhighlights限制相邻。Ch72首/71尾/73首actual读；等现TSFlow POST释放才写。root定点§4与Table1/Ncost足够，不扩大unsafeprompt附件。

## 10198 — HumanLLM simulation fidelity≠social desirability（5=2+1+2，owner差额深入）

actual §3.3–4.2 L214–267、§5.5 L428–437、limitsL442–452、D1L888–900、E3L961–1009；C2L842–886仅配置。pattern/scenechecklist分别目标人格trait表现与组合condition行为，GPT5mini ternary(+1/0/−1)再mean。20scenario/三专家与同GPT5mini holistic对照，案例负面attributionbias被holistic低分却checklist/human高；不把value-neutral rubric当人类psychologicaltruth或checklist≠normativebias天然隔离。scenario/checklist均synthetic，构念局限WEIRD、评判工具同源、20小样本未给CI/盲化selection，r.91不是全部模型/人口效度；physactions/innerthoughts是生成文本不证明内部cognition。

244patterns/11359scenes来源结构，训练10265scenes/30543Human samples加OpenThoughts30543与CoSER15272，76K 4:4:2混合；8B/32B Qwen3fullSFT2ep/LR5e−6/B2×grad8/max6144/BF16/ZeRO3offload，硬件/totaltraining/judgewallclock未披露。ID50/OOD50/Mixed994，OOD8leastfrequency按syntheticcondition分，不认证实际unknownhumanpopulation。SubmittedJan15T08:56:53Z，UpdatedJan16T01:30:21Z，created/registered02:49:36→BJT Jan16 [09:00:00,10:49:37)。

actualowner `PLATFORM-EVALUATION-SYSTEM` Ch66 L1017–1027原selfreport/behavior/deployment与PVNI construct已有，不含同负面trait output的simulation-vs-desirability评价目标。拟 PVNI两段之后、人机manipulation之前两段，分开rolefidelity和prosocal/safety，可同output分别验，不以负面人格演得像签部署安全；相邻20human/rubricpopulation/cost边界，human/真实behavior保留。Ch65/67交接和Ch66owner已actual，不因现persona关键词就授已有覆盖。

## 10201 — PRL exact-v1 future-KL policy signal（7=3+1+3）

actual §3.1 L74–91、§3.2/3.3 L198–254、Alg1 L255–308、§4setup L312–318、局部Tables4/5与limitsL442–484、BTable6 L756–780。正式v1标题 Processing Reward Learning，v2 May新title不倒填事件。只采Alg1：outcome先group标准化A，冻结reference π0，currentpolicy logπ/π0构成从t至tail的sum/η，stopgrad(A−sum)成为每tokenclippedratio credit；不是PRM对语义步骤正确性认证。当前π不是πstar，§3.2 all-completion equality只宣称optimal条件，不能从实现继承普遍无偏、exact objective或everypath正确。

bodyfinal式额外−βKL，而Alg1无该term/Table6 KLloss0，明确采用Algorithm版本而不自行合并；Table6 η100–300/step256，AppendixA proof在HTML absent且引用空label。只为了判断依赖曾有限officialPDF：systempdftotext不存在，bundledpypdf已可用但35s官方响应520436/553843截断；root指示停止恢复，仅未采用proof，不冒Blocked，不扩大其它version或自补证明。必要证明不作为采用正证据。

Qwen2.5Math1.5/7B+Llama3.2-1/3B、约150KNuminaMath，MathVerify，4H100约15h/run，B128/minibatch256/G5/LR1e−6/max1024/3072；precision/seed/evalT及逐方法总预算未披露。weightedavg@8与pass@8不是同指标、pass@8不认证解空间严格扩大。Table4 7B shortstep16/64(71.19/70.27)低GRPO72.12，25672.38；1.5B newline66.31反高fixed25665.86，step不是universal语义粒度。groupnorm-beforevsafterKL Table5局部相同51.42不证明orderequivalence。

SubmittedJan15T09:01:53Z、UpdatedJan16T01:30:43Z、created02:49:40/registered02:49:41→BJT Jan16 [09:00:00,10:49:42)。actualowner `TRAIN-GRPO` Ch33 L206–215 outcome同A与PRPOsegmentation，没有fixedreference suffixlogratio控制接口；L68已有paramdependentreward≠detach等价。拟原sequence advantage说明后、PRPO之前两段，仅采实现接口/局部反側、必要更长reference scoring与普通GRPO退路，不将未核proof或rulelabeltruth融书。Ch32/34交接actual读；等VZero POST放Ch33才写。root定点Alg1/4.3/BTable6及owner决定，不需通用proof。
