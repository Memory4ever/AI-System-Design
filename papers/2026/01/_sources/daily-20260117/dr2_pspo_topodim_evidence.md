# DR2Seg / PSPO / TopoDIM：必要证据与采用范围待 root 核

均已完整题摘和决定性方法由root准入；以下exact-v1必要源/关键评价/直接反侧作者已实际读，未复现或核artifact。日期采用正常Submitted cohort+正常公告且无先行原全文条件，register只给秒精度上界，非Submitted/Updated当public。

## 09981 DR2Seg — 2+2+2=6，标准/监督构造owner差额深入

actual primary §3 L112–169/§4 L362–456、Table6/7 L459–497及结论499–508。同MLLM first(I,Q)→reason/description/answer，second(I,D)替换原query；Rdesc=I[A2=A*]明确使用gold，不是无标签自认证。Second成功仅表示该图+该description在此decoder足以恢复答案，不证明R1 faithful/唯一因果。length比较N2<N1加入绝对anchor，total=(base+Rdesc)×conditionalLength；group所有acc=0时关闭长度项，不等任意task长度越短越好。理论高variance/信息论不采用为真实CoT因果。

Qwen2.5VL7B+SAM2Large，VisionReasoner7k一epoch、ReasonSeg239五epoch，GRPO G8/B16/LR1e-6/WD.01；inference仅firstpass不跑secondvalidator。Table3 local gIoU64.9→67.6→68.5，anchor25反增length/掉质量，Table6 3B gIoU65.5>60.8但cIoU56.8<57.2，gamma .1 gIoU68.9>.05 68.5但cIoU64.9<65.8；不是均优。§4defaultN0=40而Table4最佳写45，不能自补唯一复现配置。SAM3额外API-IoU换rewardconsumer不与SAM2boxpoint直接归因。hardware/precision/seed/双pass完整训练费用/真实e2etime ND，tokens节省非GPU预算。支持target-description重建reward接口，不授自动忠实/完全自监督。

actual TRAIN-GRPO Ch33 §SequenceReward L205–251已有process/outcome分账与压缩teachertrace，但没用同图+删除原query的secondpass gold反馈description、只first部署以及group失败关闭length的具体conditional监督。拟两段放RLSeg/DRT压缩reward附近或process节末，owner不写Ch66第二机制。需root确认具体差额/必要源后授锁；非要求证明所有segmentation理论。

SubmittedJan15T01:48:45Z/UpdatedJan16T01:13:16Z/created02:44:06/reg07→BJTJan16[09:00:00,10:44:08)。

## 10029 PaperScout / PSPO — 2+1+2=5，标准已读；拟 OnlyReport

actual §3 L106–188/§4.1 protocol308–316/§4.4+limits350–399、A533–556、B558–565。每次完整response含reason+toolcalls为action，ratio是全部token概率比乘积而非GSPO几何均值；criticV(prompt)和GAE按一次interaction transition，reward top3新paper relevance−重复penalty，valuepretrain100/runningmeanvariance/asymclip复用成熟组件不另加分。selector“True”概率不是校准relevance truth，累积topk/threshold/repeat目标也不无条件等全pop relevant recall；papersearch是policy/retrieval系统非AI4Science成果。

Qwen3-4B-Instruct2507/4A800/actor1e-6critic1e-5/perGPU4；Auto33551/1000/1000、Real50test；20paper observation，三轮池不变停止，selectorPASA7B/τ.01，最终τ.5。PSPO RealRecall.574 vsGSPO.557/PPO.537；没有单因子critic/ratio/returnnormalizer拆分，较小gradnorm和criticloss不是唯一稳定性因果；exactmatch gold不完整，三judge共识2629/3000不等true labels。precision/seed/总训练与搜索/API/e2e费用未披露，不授通用tokenvssequence噪声定律。

actual TRAIN-GRPO Ch33 L518–526已明确ratio粒度、normalization和loss权重不同；L663–665 segment-transition value/advantage/ratio与verifier/边界owner具体承载；L442附近critic/GAE已承载。PaperScout局部rawproduct/toolretrieval recipe可报告，但不足以新增长期机制链，不假称正文已有该实验，也不将已准入5分降/删；拟标准完成OnlyReport请root终裁。

SubmittedJan15T03:21:21Z/UpdatedJan16T01:17:12Z/created=reg02:45:27→BJTJan16[09:00:00,10:45:28)。

## 10120 TopoDIM — 2+1+2=5，标准已读；拟 OnlyReport

actual §3 L122–170/§4.1–4.3 L350–381/Table3+ablation398–429/limits446–450，A–C765–795/Dtoken表与E830–875。中心typedgraph生成→各pair marginal KL蒸馏localMLP，不能由edge marginal匹配授联合图分布/globaloptimality。Eq6称AR但softmax只显示pair hidden，依赖图history主要mask；不是完整historyconditioning实现已核。condition/debate DAG、feedback任意边优先且不计degree、visited移除；“one-shot”指topology proposal，不取消任务协作轮次/反馈循环runtime。Mask后归一与跨Agent一致edge协调实现未披露，不补无死锁/隐私保证。

5agents；40/80训练及localdistill，MiniLM384/temperature2→.5/LR.01；localGemma/GPTOSS RTX4090 Ollama与DeepSeekAPI，precision/quant/totaltime ND，120B实际部署配置不猜。AppendixC AIME23–25 all用于training/evaluation、test50，split避免重叠未披露；MMLU153 test，LiveCodeBenchMay23–Mar24。Token表不含全部priorGPT5/encoder/distill与测latency，未见seed/CI；random topology和prior同时改变结构/类型，非独立pairKL因果。不同heterogeneous随机组合可反退，matched总预算/部署可行性不足，不采46.41%通用节省/单任务全优。

actual AGENT-MULTI-AGENT Ch82 L175–190已拥有proposal/budget/runtime与node/model/edge/protocol/backbone分责，DAG不授内部looptermination。新增localpairKL缺联合约束恢复/独立对照的长期可采用条件，中心recipe可报告但不以“decentral”授保证；拟5分标准OnlyReport请root终裁，不冒Existing原实验或抹准入。

SubmittedJan15T07:05:04Z/UpdatedJan16T01:25:08Z/created=reg02:47:41→BJTJan16[09:00:00,10:47:42)。
