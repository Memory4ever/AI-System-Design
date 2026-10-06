# 02/20 第五批普通必要停点：15997 / 16054 / 16132

最新：root已实际核三个精确原源/关键反側及具体owner比较，必要PRE通过。15997按协议限定负例仅报告；16054既有具体覆盖；16132已落实Ch24:1203一段与1861自身末注，root实际正文/完整1190–1210邻接/末注POST通过。第五三项处理闭合，累计20必要、14真实整合POST；不冻结全日候选、不授整日。以下“拟/待PRE”保留过程理由，以本段最新处置为准。未核实现/复现；提取行号仍同目录 `V3_extract_html.py < exact-v1原HTML | awk 'NF' | nl -ba`。

## 当前身份与日期

三个 current abs 已实际读完整题摘、Comments及当前页展示history，保存在 `V3_CURRENT_ABS_2602.<ID>.html`。16054/16132均v1，无页面所示影响采用的纠错/撤回信号；不由此保证全历史无标记。15997当前v4 explicit significant rewrite及新增Pythia任务信号，已仅定点核v4 §4.6，见下，不扩所有revision。

同ID DOI Registered原字段都在 `V3_DATACITE_2602.<ID>.json`。沿首批官方桥接，Submitted只给下界02/19T09:00+08，Registered+1s给秒精度公开上界推定：

| ID | v1 Submitted UTC | Registered UTC | 本窗公开范围（北京，含起不含止） |
| --- | --- | --- | --- |
| 15997 | 2026-02-17T20:39:02Z | 2026-02-19T02:35:48Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:35:49+08:00 |
| 16054 | 2026-02-17T22:08:16Z | 2026-02-19T02:37:09Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:37:10+08:00 |
| 16132 | 2026-02-18T01:53:29Z | 2026-02-19T02:39:01Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:02+08:00 |

## [Anatomy of Capability Emergence: Scale-Invariant Representation Collapse and Top-Down Reorganization in Neural Networks exact-v1](https://arxiv.org/html/2602.15997v1)

2+1+2=5，几何monitor评价反侧深入。v1 §3.2（176–208）RankMe是hidden activation矩阵归一奇异值的entropy effective rank，task-specific final-layer200样本；其他Fisher/Hessian/LLC测量对象和成本不同。§3.3（209–214）算法training-distribution诊断与Pythia外部probe不等：160M/410M154 checkpoints，2.8B仅50K–80K的17 targeted checkpoints，probe16–200样本。§4.5（388–403）coarse difficulty相关ρ=.57–.90不等fine timing，within-easy27%、ordering-swap26%，相关层级不能当新能力预警器；§4.6（404–410）七旧benchmark中无一致Pythia task precursor，不推出所有自然语言任务没有前兆。§5（421）120task-level/model events依赖、约40独立task×scale观察，top-down temporal precedence非干预因果，大模型/复杂任务开放。

current-v4题摘与inventory已改成capacity/difficulty解释，不属于本窗。因其实际significant rewrite/新实验影响旧负侧的外推，仅定点实际读 [v4 §4.6](https://arxiv.org/html/2602.15997v4#S4.SS6)（510–525）：2.8B扩为72全轨迹checks，额外screen7 benchmarks选late BBH logical deduction，不同于原syllogistic Logical probe；报告49K gap，七旧benchmark仍negative。故本日只保**原probe/窗口下negative与粗/细预测不等**，不采v1推断‘task-training alignment为必要条件’，也不借v4positive移日期。新版条件只限制旧判断的采用权限，留其真实修订事件，不开展窗外候选或全部版本历史。

actual `WORLDVIEW-LLM-INTELLIGENCE` [Ch8](../../../../../books/part-01-worldview/08-why-llms-show-intelligence.md):312–316已明确预先冻结signal/anchor/窗口/false-alarm与独立seed，前兆不是充分原因/发布许可；[Ch28](../../../../../books/part-04-training-system/28-pretraining.md):596–601已拥有spectrum sensor、漂移/预算、非最终质量预测。拟仅报告此协议限定反例并指已有覆盖，不把缺RankMe配方当gap；新版不授正面本窗证据。准入理由已从later AB改回v1可支持negative protocol，待root独校此局部变化。

## [CLAA: Cross-Layer Attention Aggregation for Accelerating LLM Prefill exact-v1](https://arxiv.org/html/2602.16054v1)

2+1+2=5。实际§3/Alg1（126–170）所谓oracle是本模型对full prompt生成的greedy answer query→prompt key attention，max层/头、mean生成位置、pooling；不是标注正确答案/信息因果真值。oracle emulation给早层KV剪但hidden完整、prune层剪sequence；应匹配architecture，而不是一个通用数学上界。§4.2（178–184）前m4层不压KV，最后W8 prompt query做importance，连续n层max，在lp永久prune；不是共享后层selector indices。

§5.1（504–515）3/8/12B，LongBench/NIAH/RULER，HF+FA2/单A10080GB/greedy；同keep rate用于prefill sequence与decode KV，W8/pool7/lp15/n4，SpecPrefill draft1B与主模型有family/能力差异，不把它失败授所有lookahead失效。§5.3（626–631）CLAA TriviaQA92.37>‘oracle’91.43，直接不采普遍upper bound/causal token truth。§5.4（632–636）10Kprompt/32output headline39%TTFT（约900→550ms）是该单请求条件，early full KV .3GB vs oracle .1，GemFilter保full-cache-index .1keep仍1.3GB，decode16 vs19–20tps，有实现配置反侧。

§5.6（711–719）n1→2 local controlled益，高keep n4趋稳但10%keep n2峰/volatile，不授窗口越大越优。§6（720–724）summarization importance随生成变，static ranking/multiturn原turn失效，scoring<2% TTFT已计入。支持跨层证据聚合和early compression boundary的局部条件，不证明attention即ground truth或n4普适。

actual `INFER-PREFILL` [Ch43](../../../../../books/part-05-inference-system/43-prefill.md):159–177已拥有cross-layer critical-token stability、质量校准/漂移/failed selection、永久token-pruning depth与full-before/twopass预算，不能把CLAA说成另一个indices reuse。拟仅报告受限对照/层不稳定证据，具体已有support/深度/预算解释覆盖，无需仅为max recipe写书；若root确认跨层聚合这一策略有尚未承载的必要选择差额，可再一窄段，但未授共享写。

## [CHAI: CacHe Attention Inference for text2video exact-v1](https://arxiv.org/html/2602.16132v1)

2+2+2=6。§3.2（103–109）entity-match旧视频latent提供K/V，当前prompt调制latent提供Q，替spatial self-attention，仅steps2/3/4首block；step1 Q噪声不复用，同步后续blocks可能注噪，只限first block。不是输出视频精确缓存或重训模型。§3.3（119–125）miss走full30steps，hit用fast8；LRU同时删latent与vector index，cached-state/schema必须同步。

§4（137–145）OpenSora1.2/H100/3s240px；Spacy3.8.11实体/LongCLIP/Faiss1.13，VBench692prompt一视频/12维 vs VidProM1000仅6维。Main VBench预置所有CHAI entity命中，NIRVANA-VID只有75%wholeprompt命中，基线30 vs hit8，**不能把3.35×全部归cache-attention或普遍hit率**。§4.2（151–158）另时序VidProM先100cache→1000新prompt/10%容量，entity52% vswhole14.7%hit，7.63s vs12.59s(1.65×)，是更实际的bounded protocol仍无production负载/SLO证明。

§4.3（160–171）240px每entry三latent~1.3MB，100Kprompt list cache-size curves，完整index/embedding驻留成本未量化；§4.4（172–176）AdaCache与CHAI不同cross/intra条件，miss无reuse时intra仍成立。§6（194–202）highres storage、多个entry融合和cross+intra joint尚future；不授质量精确保留、身份/安全无污染或部署ready。

actual `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md):1190–1203已有同trajectory mutable cache/selector/error预算，101的reference branch已有reference与generated-history权限分开；两处都没有**跨request entity-hit旧latent只作KV、new Q保当前prompt的非exact条件接口**。拟最多一段接mutable-cache路线，把exact-state复用与semantic donor proposal分开；cache identity/索引eviction/steps/window/质量污染/额外lookup成本、miss完整path共存，PRE待root，无实际写。

## 普通下一步

三项最小源已足够上述拟命题和关键反側；15997局部准入因精确版本纠偏需root复核，16054既有coverage/局部经验不强行gap，16132只申请上述cross-request条件差额。不得把尚未PRE当外部材料阻塞，其他本日准入/必要证据仍普通可执行。
