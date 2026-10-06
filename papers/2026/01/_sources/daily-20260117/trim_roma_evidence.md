# TRIM / ROMA：标准与 actual owner 处置待 root 核

root已完整AB准入6=2+2+2；actual exact-v1缓存已读必要机制/关键评价/直接反侧，不复现。正常Submitted cohort/Jan16T01Z公告且无先行全文条件公开范围如末，不把Submitted当public。

## 10245 TRIM

actual §3–4 L93–155（double-newline step，weak先提议→accept或strong只替换本step→交回weak）；§5 Table1 L155–249/主要设置结果L355–393、A L598–645、B1L651–667、D1L908–961/E962–982/G1046–1070。PRM current/minprior+tokencount/stepindex是noisy观测，RL MLP或KDE后验/POMDP决定regenerate；S1=earliererrorirrecoverable是显式建模假设，不认证现实reasoning不能修复。smallprefix provisional再替换，非已commit内容静默改写、非speculative target exactsampler。

Qwen2.5 3B+Claude3.7Sonnet API、MathPRM7B；AIME约50/50alternateyear，MATH7500→500，AggPPO actorcritic2×128tanh/LR1e−4/clip.2/GAE.95，stepscap30；POMDP ProcessBench/OmniMATHhumanlabel与next-stepaccuracy拟合，SARSOP每step求解或beliefheuristic，约5s/次，只hypothetical LUT不能写zeroactualrouterlatency。CPT95%是达到**弱强模型分数gap的95%**，不是95%accuracy；strongdecode token cost忽略weak/PRM/prefill/solver费用，API主实验未实施chunkprefill/KVoverlap（G明确），不由claim推工程实现。

Table1高预算Agg可优POMDP，低预算POMDP优，非全budget胜。D1全接管较贵只支持单步替换取舍，不能说sufficient/optimal通用；E仅leftpadding人为noise+Agg训练再测，非不变router对所有miscalibration稳健。A另2H100/vLLMprefixcache的1.5B+7/32B本地Thr，不是Claude主协议；32Bthreshold.1/.7latency6.21/12.10 vs17.10但质量随threshold变，不能合并API的净quality/latency。precision/concurrency/maxlength/seed/APIcheckpoint以及totaltraincost未披露。

actual `INFER-SCHEDULING` Ch56 L256–282已有版本/KV边界，284–293TrigReason异常触发替换/return与token不是wallclock；没有本步PRM+累积风险/成本→可恢复性belief选择，不将POMDP成熟原理计新分。拟TrigReason后、token-spanrelay前两段，将step proposal→PRM sensor→belief/cost决策分账，保irrecoverability/PRMnoise/solver/APIvslocalbudget边界和原threshold/单model退路。必要G/B1与A/D1足够，不展开其余domain附件。

日期SubmittedJan15T10:06:06Z、UpdatedJan16T01:34:12Z、created02:50:44Z/registered02:50:45Z→BJTJan16[09:00:00,10:50:46)。

## 10323 ROMA

actual §3 L173–214、§4 L215–244/5.1、5.3/limitsL760–774、Table5L440–456、Table9L1184–1229、A5L1415–1419。每1秒video/audio构成unit，video2fps/max65536pixels，同unitvideo固定timeID/audio40ms，TMRoPE跨unit最大ID延续；LMhead旁2layerMLP从last4layerslearnedpooling→speaktiming。stage1reactiveQA适配流式模板，stage2timingweightedBCE+QA语言loss（方法imbalance比率，实际wpos3），frozenencoders/其余finetune。persistentKV只编码新unit但非无限history，25token≈1s分段/unfinishedeot/下一unit续写是pipelined realtime approximation，.3697s只是unitencode平均非从观察到完成响应的latency，inference设备/精度ND。

32H20训练/B512/32K，LR/seed/totalwallclock/推理concurrency ND。videoMME/spokenquery/gpt4o与textquery其他task不直接相加；triggerintervalsuccess并不验证安全/真实交付，静态ranking不是online及时通知。两stage/mixed、K1/4、silencetoken控制支持训练timing分责，但Table5K1VideoMME34.56高完整33.30，Ego55.4低Qwen58.4；Table9 wpos4F1YouCook35.55>default35.21，wpos2GPT部件可高却time差，不是统一最佳。limitedevent/dataset/syntheticspokenqueries/finitecontext，长时/音视频错位/隐私授权仍限制，不授生产品质/实时保证。

拟 **已有覆盖**（请root终裁）：`MULTIMODAL-REPRESENTATION` Ch23 L783–805实际已有timestamp/speaker/observationrevision/interruptfrontier、prefix实际到达≠deadline、独立hiddenstate trigger只提replytiming而runtime持commit/cancel、阈值/false trigger/固定窗口及外部turntaking退路；由此已承载本篇可采用的同步表示/时机与内容分责，不冒该正文已包含ROMA具体1s/40ms/K4/两stage实验。新局部recipe与反侧留报告；若root认为streamtemplate→timing联合监督是独立长期缺口，可限定两段在memory/trigger后，不复制旧timestamp/authority段。此处保持6分标准审阅，不因已有覆盖删候选/降分。

日期SubmittedJan15T12:09:04Z、UpdatedJan16T01:39:59Z、created/registered02:52:37Z→BJTJan16[09:00:00,10:52:38)。
