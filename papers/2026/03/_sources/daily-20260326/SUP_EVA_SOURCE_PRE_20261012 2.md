# EVA necessarySource/sole Ch23差额与两PRE

2026-10-12。[2603.22918v1](https://arxiv.org/html/2603.22918v1)，原2+1+3=6/date25不改。actual必要§3.1–3.3/Eq1–5、§4.1–4.5/T1–3、§5限制、6.1–6.5与6.6反思规则直接支持/反侧已读；未逐图/代码/复现。known具体信息获取gap后深入，不扩所有RL目标/附件。

## 支持与关键反侧

query-only s0（尚未读visual）先提出start/end/nframes/resize，逐轮jpg帧→summary/plan/action/reflection→继续或回答。具体增量不是给成熟Agent换名，而是时间窗、密度与空间分辨率同时可调且第一次不被预采样帧默认绑定；后续仍可选择global低res→local高res或直接uniformdense。resize是下采样不由zoom词认证发现对象；§3states h/F为belief不是事实。queryonlyplanner也会先验选错/遗漏，§5unseen/noisyquery失败，不采§6.1“只有planning才能reliably”保证。

SFT Qwen2.5VL72Bteacher、llava-video/CGbench并有experience/reasoninghints与reflector；KTO chosen63%/rejected37%由judge选不足视觉仍回答的轨迹，不能视为真正grounding标签；GRPO收失败示例再由teacher为HDVILA未见video造OEQA。原10K/11K/9.6KOE+1.1KMC只是数据身份，独立decontamination/随机seed未披露，不自动可复现。CSV同base只看lastretrievedimages，judge与agent都答对可仍依共享prior，不能保证全部support；ROUGE不是语义真值，wrongtoolcall+.05与guess.20/.25比较本身不证明rewardhacking被消除。先KTO后GRPO主要stage对照也改变数据/预算，非顺序唯一根因。

Qwen2.5VL7B SFT2epoch/B8lr2e-6，KTO同lrβ.1；GRPO1epoch/B64/8rollout/lr1e-6/32H100。评估vLLM/jpg/original720P，baseline minpixel1280×28×28/max16384×28×28，实际帧数可因resize变化，所谓等效帧用650tokens/frame估算不是真实同帧预算。Precision、inferencehardware、batch/concurrency、完整视频解码/工具latency/SLO Not Disclosed。T1EVA51.0/10.3K与§4.2 51.8/6.2K冲突；T2诸GRPO55.0/68.3/48.4/60.2/43.3与正文55.1/60.5/59.9/38.1不合；T3body36.7vs37.2，保两口径不抄统一增益。T2KTO在VideoMMELong45.1< SFT45.8、T3IMC39.5<VideoR141.7/MHR27.1<31.0等，不授allbench/component全胜。

6.4 SAH5仍高于多baseline0.2/2.2/3.1；其In/Out合成指标不证明全部幻觉机制唯一，故不采用降低SAH为足够grounding保证。§4.4用少visualtokens推runtime不随rounds增长，未实测wallclock，必须加planner decode/重复prefill、jpgextract/resize/回传、teacher制备/三stage训练与评价，不能由tokens授全费净加速。6.6reflector需要metadata duration/question，规则在global无信息时增密/分辨率、fps≤1，只是训练制备heuristic不当全部线上guard。

## actual owner gap/原锚

actualCh23完整700–754前后预算压缩→boundedcrop claim观察→图表定位/再读→任务可靠性，以及1018–1043完整长视频FlexMem/streamadmission→主动time/rate/modality读取→DAVE标签→EXTRAS两检索→queryjointsampler→regioninteraction链已读；Ch24/25开篇与23末handoff有效复用。这些已有具体主动读取及成本/充分性边界，仍没有query-only首轮提出时间窗×密度×空间resize联合接口，并让uniformdense作为动作分支而非预先帧条件的差额。仅sole MULTIMODAL-REPRESENTATION Ch23消费信息取得合同；训练三stage只是支持来源，不重复Ch29/31/33RL机制、视频生成Ch24或Agentworkflow双owner。

拟在1018节完整主动观察第一段（最后“固定读取仍更简单可靠。”）之后、原“主动观察还需要把训练时的‘值得再读’标签…”之前插以下两段及本人静态注。未独核/root锁/写入/POST。

## 两逐字PRE

读取动作还可以同时决定时间窗、采样密度与空间分辨率，而不只选择下一段视频。一个受限分支在首轮只给模型问题和视频时长，让它先提出这些参数；取得帧后才更新描述与后续计划，必要时扩大全局低分辨率观察，或缩到局部提高密度与分辨率。均匀密集读取仍可作为该动作空间的一条分支，并不因 planning-first 被淘汰。query-only 初态避免预先采帧固定预算，却也让首次选择更依赖语言先验；时间窗与 resize 一起决定哪些事件和细节实际可见，计划正确的格式不能认证未读内容无关。<!-- source-family:SF-2026-ARXIV-2603-22918 -->

要学会何时继续看，训练轨迹可以包含不足证据仍回答、密度与窗口错配等失败，再以成功轨迹和任务反馈校正；但同模型判断、最后一轮帧答对与词面答案重合，都只是监督代理，不取得独立 grounding 权威。更多轮次可能少读视觉 tokens，同时增加重复推理、视频解码、resize 与工具往返，三阶段训练和 teacher 数据制备也付费；等效帧数不是实际读取人口，少 tokens 不保证请求更快。面对 noisy query、短暂事件遗漏或质量—总预算失配，应增加观察、回读原片段、保留固定密集采样或不提交答案，不让规划与反思自行签发证据充分性。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-22918` — [EVA exact-v1](https://arxiv.org/html/2603.22918v1)必要§3–5/Eq1–5/T1–3与6.1–6.6；仅query-only初态与时间窗/密度/resize联合取得接口。保共享judge/ROUGE、训练数据和stage预算混杂、文表身份冲突/等效帧非实际人口、noisequery与所有制备/训练/读取费用；不采完整rewardrecipe、充分grounding、全胜或端到端加速保证，未核code/逐图/复现。
