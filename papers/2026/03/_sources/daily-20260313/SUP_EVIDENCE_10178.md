# 10178 ExeVR：必要Source / actual Ch66差额 / 窄PRE

仅补充Mar12 BJT自然日。第二包精确v1完整AB/贡献准入与日级arxiv夹证复用，不重抓旧池或其他日。原件 `SUP_CORE_10178.raw/txt`，official exact-v1 `https://arxiv.org/html/2603.10178v1`，GET200 UTC2026-10-09T14:11:37。作者实际读完整§3/Alg1–3/Eq1–7、§4/Tables1–3、§5/Tables4–5、App0.A全部/App0.C必要实现文本及0.D基线接口说明；§2.2必要定位。没有像素/代码/部署复现，不认证Figure3/4/5精确点值；Fig4正文近似数字仅作者描述，不作E2E费用采用。

## 命题与实际评分

final snapshot漏进展、action/reasoning trace可带被测agent自报→原文从动作后截图组成纯visible执行视频，以instruction/video评分并报告first-mismatch interval，matched-negative task改写与变化参考token删减→需把观察证据、标签provenance和压缩保留资格分别验收。这是具体evaluator输入/监督对象变化，不因53k数据规模、modelagnostic宣传或新benchmark名准入。拟2+1+2=5：重要观察/评分接口2、单evaluator组件1、可复用约束2；不借已有sensor非authority等成熟原则抬分。实际owner知识缺口/评价边界必要深入，拟受限整合两段，待非作者Source/PRE；不预授Books或候选完成。

## 核心方法与资格

§3.1每次action后代表截图按step拼接为1FPS summary，不是原生wallclock连续录屏；step映射、采样/分辨率/上限改变可见证据。AgentNet22,625human demos/ScaleCUA约7k human-evaluatedagent/OSWorld361tasks约23k30agentrollouts，标签有人类、规则及合成不同provenance，不能称53k全human独立真值。Table1 AgentNet/ScaleCUA各50%(w/synthetic)、OSWorld32%给标签人口。

§3.2 GPT5.2将成功segment匹配interface-plausible但不满足的instruction，生成理由和首次显著不匹配reference step。人工筛negative pairs，selected audit subset称100%pass，但没有subset N/重复/审者协议，不能转成全负例可靠率、真实失败执行人口或因果blame。新instruction改目标而非对相同目标造成executionerror。主文不是执行counterfactual rerun。

§3.3/Alg1 freeze vision/projector，只训LLM；STP局部4-neighbor L2distance<τs建graph/unionfind，component size>τlarge直接drop；TTP每位置firstframe初始化、后续cos(reference,current)≤τt才keep并更新为lastdistinctreference。最后keepmask Ms AND Mt。它检测appearance变化，不保证UI语义仍然可辨、subtlegoal信息不误删，也不是所有firstframe retained（TTP保留不能越过STP AND）。App0.C帧temporallymerged原spatial mask另OR→mergedtoken，文字“任一被pruned则masked”与keepmask含义需明确；不假造已核码/精确merge实现。

§4.1 τs .3/τt .9999/large40全用；正文降低τs更aggressive的解释与Eq3–5 increasing阈值产生更多edges/大component的方向不合，隔离阈值调参recipe，不因此否定全部video/pruning方法。每token先visionencoder仍有费用，不把LLM少token当vision成本归零。

## 必要评价与直接反侧

Qwen3VL4/8B-Instruct SFT lr5e-6 cosine、8 A10080GB、modifiedLLaMAFactory；precision/batch/epochs/总train预算、onlineSLO未披露于必要主文。Evaluation heldout800→去unsolvable后789，49.94%pos/50.06%neg；Ubuntuagent10tasks200solutions、其余各200uniquepairs。未清楚声明task-level独立分割/所有synthetic父trajectory分组/agentfamily全unseen，不能授全task/policyOOD。至多100frames、720p/1FPS、长video uniformsubsample。Attribution200 firstdeviation human区间；tIoU是interval重叠，不是动作因果或全执行正确。

Table2整体84.7/82.9precision/87.7recall，但Ubuntuagent8B82.5/77.7recall非最佳（Seed85.1/85.1、Gemini3rec90），“allleading/consistentgain”不能抹去；4B MacWin90>8B89，不授模型规模单调。LLaVA总体Acc13.6与四分组约49–50不自洽，不能采用全榜精确聚合排名保证。点值描述不证明统计显著：repeat/CI未给，很多同task solutions相关。

Table3实比较已训videojudge与prompted原backbones；Tail/H+T/Full、actionhistory、one-shot、360/720p同时不同，不归因video唯一因素。0.D确认AER compactaction，SimplifiedJudge detailedaction+reasoning，SEWSM/ZeroGUI fullscreens无action、后者one-shot；作者调整webjudge提示适配GUI，未读全部prompt逐字代码，不授等价复现。Table4 4B 360→720 precision80.6→79.2，Table5 TTP-only80.3acc/81.3prec，both80.1/79.2但82.5rec，STP-only77.6/72.6；§5自己解释STP可丢弱视觉决定cue，不把联合压缩说普遍quality无损或所有指标最好。Fig4作者文字8A100训练memory/step不同，未核视觉点，不当线上GPU/E2E吞吐SLO。

App0.A重要反侧：长Ubuntuagent探索中局部失败可恢复成功，但binary compactvideo易判失败；未有足够scale的step-correctness/recovery细标，目前SFT不是已证PRM/RL闭环。仅提供可观测firstmismatch，不可声称看到每个关键状态或确定首次有害承诺；视频看不见后台文件/权限/不可见effect时须独立verifier。

## 实际唯一owner与差额

唯一 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。作者实际读当前934–958（Agent/Outcome前接、FinalPass/trajectory/luckypass与可见textDAG）及1266–1284有预算取证：现文有action/witness和只读tool取证/verifier权限，但没有“action后截图→step-index视频→instruction-conditionedoutcome/firstmismatch、同轨迹改goal负样本、lastdistinctappearance删token”的具体输入/监督身份。不是泛主题owner match。新增仅这条video evidence分支，不写Ch23pruning第二owner；tokenmask只作为评价证据有损变换限制，visionencoder/图像语义仍原owner。

拟插在“从Final Pass扩展到Trajectory...”里luckypass之后、visibletextDAG之前，两段逐字PRE如下；原stage/final verifier分支保留。工程验收建议与作者已实现相区分，不声称该study给可部署正确oracle。

### 逐字PRE

GUI轨迹还可以把评价输入从Agent自己的action与reasoning文本，换为独立记录的可见执行证据：按每次动作后的截图建立step-index视频，再让instruction-conditioned evaluator同时提出outcome判断和首次可见不匹配区间。这条分支不要求读取内部思考，但1FPS摘要是step重排而非真实wall-clock录屏，采样、分辨率与截断都属于evaluation identity。将同一成功片段配上界面上合理、却不被该片段满足的目标，可构造难负例；这是改变任务语义得到的监督人口，不是同目标实际执行失败或因果blame。人审、环境规则与合成标签须保留各自provenance，区间重叠只验可见定位，不能替代后台状态、执行权限和最终效果的独立verifier。[ExeVR必要方法与评价](https://arxiv.org/html/2603.10178v1)支持这一受限输入分支，而非所有GUI任务的完成oracle。

高分辨率视频的证据保留还要与token预算联合验收：空间大同质区域可删减，时间上可按同位置最近一次显著不同的token保留变化，而不是每帧都重复完整背景；这种appearance规则不保证任务语义无损。受限对照中，空间删减可能丢掉弱视觉但决定性的cue，联合删减也以部分precision/accuracy换recall，不能把少token直接签成无损或零费用。长探索轨迹的局部错误后来可能恢复，首次可见不匹配不能自动变成最终失败；训练、录制、vision编码、标签复核和完整请求费用另算，已训模型/不同分辨率的榜差也不单因果于视频。压缩或目标映射失准时回读未压缩截图/完整轨迹，并由环境verifier或人审裁定；终态可信、预算低的短任务仍保留便宜的final-state检查。[直接消融与恢复限制](https://arxiv.org/html/2603.10178v1)见§5和App0.A。

## 当前停止与未授范围

必要Source支持受限观察/监督分支及真实反侧，强modelagnostic/所有平台更准、因果归因、全标签可靠、压缩无损、生产费用/SLO不采用。精确恢复需要分task/父trajectory及policyOOD，完整金标/labelaudit人口与压缩/完整输入同预算对照，非必须等无关代码/图像点值。拟5分必要深入、整合两段待实际独核/root窄锁/非writer POST；作者不写Books、不自授正式candidate/报告DAY。原候选、窗口与§4冻结。

## 实际非writer POST：通过

root是这两段及本人Review note的实际writer；本日报作者未写Books。收到root必要Source/actual owner/逐字PRE通过和实际落地通知后，本作者直接读当前Ch66 934–975完整局部（Agent/Outcome、lucky-pass、两新增段、visible-text DAG、loop和后续cycle分支）及4656–4665自身Review notes；新增正文在948/950，自身注4661。又回对精确v1原件§3.1–3.2、Alg1冻结说明、§4.2完整人口/采样/tIoU、§5 Tables4–5完整点值/解释及0.A完整恢复限制，不以PRE和root评语替代正文。

两段逐字落实，前后旧分支仍在。step-index 1FPS与wall-clock分离、目标改写负例的监督身份、人审/规则/合成provenance、区间非因果/后台verifier均正确；last-distinct appearance压缩不授语义无损，precision/accuracy与recall真实取舍、局部失败后来恢复、训练/记录/vision/复核全费用与短任务final-state基线均近文。原Table5 STP 77.6而解释77.9的冲突没有被正文硬合并，阈值/OR-mask未核实现也未被采用。未核像素、代码或复现，没有把这些范围授生产oracle、全平台优势或DAY。

**本单篇实际非writer POST通过**；自身注目前仍写“待非writer实际POST”，已向root回传具体通过及位置，请root只同步本人注并释放此窄锁。正式日报同步等待root确认，不擅写共享Books。
