# 四项改判潜力的有限必要证据与owner

四项必要证据/actual owner已root非作者复核通过：22103 Ch69正文132/完整邻接124–143/own421；21646 Ch23正文47/完整邻接37–55/own1319；21497 Ch23正文561/完整邻接547–571/own1321均PRE及实际POST通过、窄锁释放。22150在Ch23共享读出/更新权/容量的实际论证已有覆盖。下列保留作者实际源/评价/反侧与写前差额，不扩全附件；未核代码/复现，非日级Gate。

## 22103 PASTA: A Modular Program Analysis Tool Framework for Accelerators — 2+2+2=6，具体collector布局深入

[v1](https://arxiv.org/html/2602.22103v1) blocks32–41/82–104/124–130。仅API统一不准入；actual34–35把每次instruction/memoryaccess的GPUtracebuffer导CPU分析、满buffer stall，改GPU-resident collect-and-analyze helper。102详细实现是memoryobject→accesscount map launch传GPU，instrumentedmemoryaccess在device计数，kernel结束只回传map；该working-set回答每kernel访问的对象，不是原地址流的lossless因果trace。95–98的max单kernelWS也不替代跨并发live-memory峰值/完整HBM容量。

同memoryobject访问分析的CS-CPU/CS-GPU及NVBit-CPU比较，A100/RTX3060、AlexNet/RN18/34/BERT/GPT2/Whisper inference/training；CPUbaseline通常singlethread、NVBit还dump/parseSASS，故941/13006倍等headline不能作GPU位置唯一因果或任意优化profiler倍数。103–104 collection/analysis在GPU fused，正确分母是完整profile收集/传输/分析时间而不是untouchedmodel吞吐。127承认type/volume决定不可预测overhead，126的4MB是example非全workload上界；helper/atomics/驻留会扰动原任务时序，passive不改数据不是零干扰。

PLATFORM-TRACE Ch69 actual99–132拥有采样偏差、metrics/logs/trace及serialization/propagation/collectorqueue/export/storage成本；actual72–74已有CPython↔GPU语义身份与memoryprofile范围，但没有“fine事件只需聚合指标时，将分析移到device并返回summary，避免rawtrace满buffer传输，同时明确lossy evidence类型”的collector替代。拟在Instrumentation overhead段后一个窄段，保留完整rawtrace/CPU分析适用域、GPU资源扰动/丢原事件限制、scope/identity、同event/evaluator总费对照与常规采样回退，不授零overhead/productionSLO。邻Ch68/70尚需开篇/收尾实际读后写。

## 22150 CoLoGen — 2+1+2=5，具体shared-capacity反侧标准

[v1](https://arxiv.org/html/2602.22150v1) blocks17–47/60–75，原EX建议保留在V3_CLARIFY；根据Table5 actual70改潜力，不归因LoRA/MoE为新原理。Singleconcept/localization、joint、progressive各两benchmark：MagicBrush conceptCLIP-T.302而joint.269，DreamBench jointCLIP-I.795/DINO.679低于无两representation.808/.683；CoLoGen.825/.714。概念/定位共享同空间仍可相互干扰，不能以单任务有益推出joint有益。

61–63分stage200k/200k/400k/50k/200ksteps，globalbatch256/128，routerdensity1或.8/usageaux0或.5随phase变；正文未证明Table5joint/staged的总token/compute、router条件完全matched。Table5只是bundle的受限反侧，不归因单独staging、容量分责因果或concept/localization可独立解码。CLIP/DINO是surrogate非编辑正确性，有限定性不授subjectidentity/安全。

拟具体已有覆盖MULTIMODAL-REPRESENTATION Ch23 actual916–925：晚融合专用容量与早交互共享竞争，中间共享交互/专用FFN容量；随后实际generation warmup可前向读共享expert但暂停反向写，再释放/限制梯度、不同LR，明确单模态高LR本身也退化、shielding不授唯一因果。该正文已承载本项能支持的“forward共享/更新权/容量分别选择+matched控制否定全部归因冲突”，不为CoLoGen加recipe段。

## 21646 Synthetic speech-guided translation — 2+1+2=5，表示收益与新增信息分开

[v1](https://arxiv.org/html/2602.21646v1) blocks19–53/54–62/89–97。Whisper-large-v3 frozenencoder→80query Qformer768+MLP→GemmaX2-28-9B，CosyVoice2由同一输入text生成speech。4A10080GB AdamW1e−4/1kwarmup，train underweek不完整总費；positive selffilter是成熟方法不计贡献。Table5 actual90，同CoVoST2六方向：Text38.5BLEU/88.7COMET，text+authentic40/89、text+synthetic40/89，单AS31.7/83.8、SS32.7/85.4。支持该模型synthetic可以作为辅助表示替代AS，不能说合成speech提供新的原说话者/环境prosody；TTS增加模型prior与compute，不是外部independentevidence。真实pairedtext已将内容输入，natural/synthetic相近不证明speech完全无信息。

Table6 Khmer COMET83.6低于baseline84.2、自filterBLEU提高但COMET退，不能只selectmean或授108方向普赢。Evaluator spBLEUflores200/COMET及vLLMgreedy相同，model/训练混杂不将更大textLLM对比当speech唯一因果。

拟MULTIMODAL-REPRESENTATION Ch23actual37–49同tokenbudget丢信息思想实验附近窄段：由同一输入派生新模态可以改变decoder能读出的表示，不代表新增environment observation；保留sourceidentity与TTS/modelprior，分别验任务收益/真实额外信息，synthetic不可充独立fact；追加encoder/TTS费用、text-only/真实speech回退。具体声学生成机制仍Ch24不双写。请root判本段或已有覆盖，不由翻译领域单独EX。

## 21497 Evidence-Calibrated Reasoning Decoding — 2+2+2=6，score控制接口深入

[v1](https://arxiv.org/html/2602.21497v1) blocks19–52/57–81，root36–48核心已实际读。Prefix-wise averageevidence代替bestprefixmin、knee-truncatedcandidate在mass-conserving候选score内混合；低margin时GRIT拿image+prefix-tail+候选（无原问题）选w*并把sentence追加池，bbox只是annotation从未重新编码入score。原Eq10全词表总质量α+(1−α)P(C)非1，不能把rawmargin阈值授normalizedconfidence或概率校准。Argmax受限proposal可用，candidate外真token不能恢复；相同图/模型派生sentence不是独立真值或实际多view acquisition。

Table3 source65/71 supervisor37→40.7、genericQwen3Bdecider43.7/GRIT47.9、GRITalone30.1，支持分配角色而不由强perceiver说明全部gain。Samebudget替代decoding的生成/deciderquery未严格等費，不能授唯一mechanismcausality。H20-NVLink73/76–81每问题基时3.24–12.92s、平均单call1.12–1.46s，δ≈.08只是作者曲线elbow，额外call可更快增加而accuracy饱和/波动；rawscore失校准/caption同误回退原decode/独立完整图像核验。

拟MULTIMODAL-REPRESENTATION Ch23 actual545–559已主动crop再原图read/gate、582–594已derivedcaption辅助/原图保identity、1072–1083已有tokenuncertainty选择层contrast但未承载“candidate约束decider的same-image局部选择→文本pool复用vs原图新observation”的接口分权。可在主动observation旁单窄段，不称coords=crop/证据校准truth，finiteargmaxscore与supportgate及cost/refallback近文。若现有成熟pool+gating已经覆盖增量请root裁Existing；不再复制初筛术语。
