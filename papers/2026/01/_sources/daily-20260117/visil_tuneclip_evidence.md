# 必要证据与owner差额：09851 / 09859

未复现；root独立原源→owner待验，未写。

## ViSIL — 2601.09851v1

[exact-v1](https://arxiv.org/html/2601.09851v1)，`2601.09851v1-primary.txt`实际§3.2–3.6/4.1–4.3/5.1–5.4（108–273）。评分2+2+2=6只采跨text/keyframe摘要的**固定VLM/文本proxy信息保留sensor**，不采精确信息论或hallucinationfree真值。Eq3在原HTML的PMI分母与标准条件PMI不一致；Eq4条件压掉summary假设V~是原V完全含的信息，不覆盖summaryhallucination。替换完整视频为caption C、最多20keyword独立概率乘积与3runs几何均值又是proxy；C没有证明完整capture、外部caption/scoremodel也不能过滤所有hallucination。故不写成raw-video完整信息或任意API普遍logprob可得。

Gemini2.5Procaption/summary/QA、GPT5keywords、Gemini2.0Flashscorer，keyframes<=3；MVBenchEpR/LongVideoBenchSSS，VQA logistic关联N162/N458，人VQA37participants8videos/score分析N110、correspondence29participants6videos、Latin-square单次观看不含scrubbing。beta负关联只局部/observational，不证明跨模型calibration或更高因果summaryutility；模型间分数作者也称不可比。Token+proxy选择不计caption/keyword/score前置调用全成本。摘要样本outlier排除与有限主题限制。

直接反侧：3-image相对1-image在人correspondence更容易忽略文本错误（作者accuracydrop43.10% vs8.62%），视觉错位又让LLMjudge到50%；更多visualcontext不自动同时提升accuracy和错误发现。人类有限样本不普遍外推。Audio未测，不作为fullmultimodalrate；tokenload非endtoendservingspeed。只采用“summary信息保留proxy”与“grounding inconsistency detection”必须独立验收，保留fullinput/human/unknown退路。

日期SubmittedJan14T20:14:47Z(v1)、UpdatedJan16T01:04:41Z(v1)、created02:40:58Z/registered02:40:59Z；原字段见all_date_fields。正常公告+registered秒精度upper条件BJT[Jan16 09:00,10:41:00)，不借v2当前版本公开时刻。

Ch66 `PLATFORM-EVALUATION-SYSTEM`实际599–631已有video可见证据/模态时间shortcut及naturalcaptionverification；**不承载条件caption-loglikelihood差作为跨format保留proxy与视觉增量可遮蔽文本错误的双对象**。拟video评估小节在599标题后、audio必要性前两段；与captionclaimverification现正文并列，不重复sampling owner。已读当前Ch66对应原body/首尾/65/67交接；待窄锁。

## TuneCLIP — 2601.09859v1

[exact-v1](https://arxiv.org/html/2601.09859v1)，`2601.09859v1-primary.txt`实际§4.1Algorithm1/4.2Equation8–9（113–169）、§5/5.1 Tables1–3（183–302），AppendixD/E/F（902–945）、H/I Tables17–19（1462–1590）。拟2+2+3=7，新增frozen-weight warmstart统计与margin停止负例排斥的**continuedcontrastiveadaptation条件分支**，不借成熟Adam/SogCLR/hinge升分。

OSR在固定θ0上run5epoch，恢复first/secondgradientmoment和SogCLR每pair的u_x/u_z统计，不是恢复未知原pretrainingoptimizerstate或更新权重/LRwarmup。随后HGCL5epoch用[sneg-spos+m]_+²，gap满足m即zero gradient（不是负例logit越大越不处罚）；m太大仍排假负例、太小真负例不够分离。理论只作动机不采用stationarity/convergence定理，必要实现以Algorithm1/2为准。

OpenAI/LAIONViTB32/16/SigLIPB16+H14，DFN12/60M，224px，8GPU A10040/H10080，DDP全局2048/4096，AdamW.9/.98/LR~1e-5、temperaturecheckpoint固定、m~.1。ImageNet1k选bestmodel，38DataComp、retrievalCOCO/Flickr分测；非盲holdout增益/跨全图文distribution保证。Table2fullstate相对只m/v仅小increment，需明确主要moment贡献；HGCL在SSFT受益而supervisedFlickr GCL更强，不能改为hinge普遍好。DFNvsCC12M同时变数据，classification/DataComp净增各不同，不作单一false-negative因果proof。Top5negative/Btm90–100语义只是proxy，不是真实false-negativelabel。

Cost2stage1.5–2xwallclock，Table18OSR4.27h/HGCL4.35h vsFastCLIP4.21h（B16），不是免费的warmup。Table19largebatchfrozenwarmup和MomentumSGD两个替代有optimizer变化，不能把全部gain唯一归u统计。无独立seedCI、genericLLM/productionretrievalfreshness未验证。warmstats增加forward/backward、dataindexed u状态与数据/weight/objective兼容身份；已有匹配optimizerstate可保留真实resume，明确负例时保留standardGCL，不稳定回退冻结encoder或原contrastivebaseline。

日期原SubmittedJan14T20:38:36Z(v1)、UpdatedJan16T01:05:15Z(v1)、created02:41:09Z/registered02:41:10Z；原字段见all_date_fields，normalcohort+registered秒精度upper条件BJT[Jan16 09:00,10:41:11)，不拿Submitted/Updated作public。

具体owner Ch23 `MULTIMODAL-REPRESENTATION`实际478–516contrastive/caption/reconstructionmultiobjective，hardnegative margin及temperature/geometry已有；**未承载open-weight continuedcontrastive adaptation丢训练统计、frozen-weight统计恢复与supervised/SSFT负例身份的不同margin条件**。拟511混合校准之前两段（negativegradient段后），optimizergenericresume只交Ch35，不重复其定义。已读Ch22/24交接；root原源→owner核后再授Ch23窄锁。
