# SSP / CoMoVi / STEM — 必要原源与owner差额待root核

官方exact-v1缓存按ID，normalSubmitted/正常公告条件+registered上界落窗，原字段date JSON；未核代码或复现。

## 10589 SSP — 拟2+2+2=6，安全failure replay gap深入，拟Ch72两短段

实际§3 L95–214/Alg1：同policy分别attacker/defender，externaljudge1–5score转互补reward；互补不证明sharedparameter minimax稳定/防degenerate，若lambda=1同一pairedtrajectory reward和为常数，不能由写下的maxsum自行证两role更新。本文未披露具体RL trainer/role-gradient stop边界，采用范围只Alg1 failure storage/replay接口。attacker低reward存goal，defender低reward存attackprompt，两pool分责；prior `(1−reward)+c sqrt(logN/(n+1))`，N文字是poolsize而非totalreplaycounter；当前policy重新生成/评估并覆盖oldreward，过threshold eviction，只是judge-relative resolved非安全事实，也无所有失败被保留保证。

实际4.1/4.2 L531–533/661–710、Table4L808–818、A/B L1353–1380、Lim965–967：5000初始goals，声称test目标过滤；8A100/B8/3iterations/AdamW1e−6/tau两role.5/csqrt2，3trials/t-test.01但具体variance/各对照budget未逐列。externaljudgename/modelversion未明确，ASR score≥3和OR-Bench误拒为条件指标，不授safetytruth。SSP OR仍25.3/24.6/24.1%，capability均值不授逐task无损；Table4 prose说全向量最低但表尾fullMistralGCG8.5高w/oUCB等，不能采用全面占优。文本Mistral3/Gemini3.0fast身份与citedversions混乱，不补模型identity；精度/完整训练rollout/GPUhour/端到端预算/未来longitudinal ND。A/B只足以限定replay接口，不用optionalcode缺失阻塞算法事实。

当前 `PLATFORM-SECURITY` Ch72L559当前policy生成failurefrontier→guard筛选→dataaugmentation及独立releasegate，但无role-specific failureobject/两pool的current-policy复评与evict。拟此后两段仅这三个具体接口，不采用已验证minimax/RL配方/长期自动安全/真实性；replayselection/同源judge/错evict/保留randomaudit与independentgate、训练费用近正文。需root必要核+窄锁；得判断不扩attackcase/proof。

## 10632 CoMoVi — 拟2+2+2=6，joint-denoise接口gap深入，拟Ch24两短段

实际§3L97–154 Eq3–11：SMPL normal+part RGB proxy经冻结WanVAE，motionbranch先domain-adapt，copiedfullWan2.2-I2V5B与video branch同denoiseloop；firstcondition无noise，3Dqueries按VAE temporalratio4对齐fusedlatent K/V，另supervisedSMPLhead。**Eq6给motionbranch下个block的是原x_motion，不是x_fused；RGB融合作3Dhead，motion经zerolinear进video。** 不采泛bidirectional motiondenoiser steering，4.5直接把fused送motionbranch反退正支持这一分责。Eq2RedList[r]/[r+1]可能邻part/signalias，normal/part编码不授可逆3Dcodec或无歧义；不用作者“preserve”认证SMPL truth。

实际§4.1–4.5 L257–267/347–403、supplementL1200–1230：24A10040G/B1accum4/6000step/ZeRO3/AdamW2e−5/BF16，704×1280/81frames16fps，FlowUnipc50/CFG6、280s peraccum/15min per5svideo。50KpseudoCameraHMR+smoothing/Gemini2.5text/filter不是真实motiongroundtruth；MotionX++手分split有训练overlap risk，VBench去dynamicdegree不覆盖完整运动。20inferences/95%CI是motionevaluation不是20trainingseed；baselines条件/模型/训练预算不同，不能单因果全归fullcopy。Table4VideoJAM/VACE及directfused对照只supports受限保留latentprior/接口，不能证明所有distributedcopy丢prior。实际只用co-denoise consumer接口，不授humanphysics或新worldmodel/动作安全。

当前 `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24L166–174采样time/budget及motionexternalcleanscaffold，不含**两个noisy producer共同denoise+单独3Dhead消费fusedlatent**区别cleanControlNet。拟motion scaffold后两段，冻结conditioning/noise/currentconsumer，readout ≠ exactmotion/physicalauthority、teacherlabel和两branch训练/15min费用近正文；普通I2V+poseextraction/cleangivencontrol共存。唯一ownerCh24，不把RGBnormalcodec另抄Ch23。需root源/owner核后窄锁。

## 10639 STEM — 拟2+2+2=6，staticaddress/contextgate/offload gap深入，拟Ch16两短段

实际§3.1L146–160 Eq4 `Wd(SiLU(Wg*x)⊙U_layer[token])`：替up而保contextgate/down，不是从FFN消灭context或全tokenlookup。PLE只附加窄表，STEM替up；4.4L592–600 gate替换退、保up加表无增益，局部控制支持分责，不授所有width最优。静态table是token/layer-indexed address，angularspread/国家token交换只是所测局部现象，不授fact全因果owner/安全知识编辑。

实际§3.4/4.1L332–355、Table3/4与§4.4：CPUoffload按已知inputids预取，batchdedup、LFU；decode nexttoken必须等当前fullforward后才知道，不授跨token提前预取。Table V*dff*nlayer及optimizerstates增memory，trainingtable独立shard/CPUoptimizerwriteback未完整优化，作者明确nextiteration；reported>80%LFU是条件hit率未给generaltrace/latency协议，不采用数值性能保证。FLOPs理论layercounts/ROI准确率除FLOPs不等GPUtime/E2E经济价值。

350M/1B controlledtrainingtokens/activeFLOPs（strictlySTEM较少），MoE按总param近配非全activebudget相同；1TOLMoMix，midtrain65/5/30，32kcontextextension改变recipe，gate/down保context但不授all-longtask无损。hardware/precision/E2E系统timing/cachebandwidth/repeatedlatency未完整披露。唯一采用staticup-address保contextgate及input-knownprefetch条件；不采用“interpretability因果/无性能代价/近常数latency”。

当前 `MODEL-FFN` Ch16L184–206拥有dense/gated cost和两分支函数/训练取舍，L244–259知识关联非数据库；无tokenindexed up替换保contextgate与CPUprefetch取决于token可知接口。拟SwiGLU成本后两段，table/tokenizer/layeridentity、gating及decodeunknown/storage/训练预算近正文；runtimecache分责简述不另写Ch49。需root必要源/owner核窄锁。
