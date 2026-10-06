# 02/20 第六批有限必要包：16069 / 16075 / 16154 / 16189

作者实际读以下精确v1核心、关键比较与直接限制，准入及必要source/actual owner已root非作者PRE通过。最新：16069具体已有覆盖、16189仅报告；16075 Ch49:823/2724与16154 Ch33:233/2869实际正文/完整邻接/末注POST通过，窄锁释放。以下拟写语句保留为写前推理，不替最新终态；本日阶段24必要/16POST，不授全日。提取位置统一为同目录 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。代码未核、未复现。

## 身份、日期和当前说明

当前abs原页完整题摘/Comments/history实际读，保存 `V3_CURRENT_ABS_2602.<ID>.html`。16154/16189当前v1；16069 current-v2摘要把agent通常<20k改为20k–30k并去128kheadline，采用v1也不据长度相关授因果；16075 current-v2仅页面所示ASPLOS/May Fourth说明，无所示具体纠错/撤回或新增机制信号。不为版本号展开所有revision。

| ID | v1 Submitted UTC | Registered UTC | 北京公开区间（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16069 | 2026-02-17T22:51:40Z | 2026-02-19T02:37:30Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:37:31+08:00 |
| 16075 | 2026-02-17T22:57:55Z | 2026-02-19T02:37:38Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:37:39+08:00 |
| 16154 | 2026-02-18T02:55:55Z | 2026-02-19T02:39:31Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:32+08:00 |
| 16189 | 2026-02-18T05:17:44Z | 2026-02-19T02:40:21Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:40:22+08:00 |

Registered原值来自既存同ID DataCite raw；Submitted只给首公开下界，Registered+1秒依首批官方公告/DOI bridge给公开上界，不声称其定义等于正文发布。Created/Updated不授日期。

## [The Limits of Long-Context Reasoning in Automated Bug Fixing](https://arxiv.org/html/2602.16069v1)

2+2+2=6，设计反侧深入。实际§2.1（62–77）100 SWE-bench Verified、bash-only mini-SWE-agent线性history，DeepSeek R1-0528/Qwen3-32B成功/失败mean tokens8538/15554与8854/17627；GPT5nano31% sanity不等所有harness配置效度证明。成功较短只是任务难度/失败重试等混杂的相关，不能采‘decomposition是主要因果来源’。§2.2（79–83）同100样本BM25+gold-relevant-file injection构造64k/128k，报告64k Qwen3Coder7%、GPTnano0与malformed diff/nonexistent file；原文‘inject golden patches’措辞与说明的gold-relevant files有歧义，不进一步断言答案无泄漏，也不把perfect retrieval recall当全部工程oracle或128k结果。无匹配短context single-shot或agent×context长度factorial，所以两路线差额不唯一归长context；model/Qwen版本也不同。§3（126–128）宽泛SWE不适合context评价收窄为受测协议，无所有LLM普遍上限。精度/hardware/API解码预算与重复统计Not Disclosed，不引用独立实测速度。

actual `MODEL-LONG-CONTEXT` [Ch22](../../../../../books/part-02-model/22-long-context.md):99–103明确retrieval不等跨段/代码依赖使用；969区分窗口与retrieval，994–996有external context program及query/stop/intermediate pollution；1079–1083还要求任务结构/密度冻结。拟已有覆盖这些真实条件，局部SWE失败仅报告，不为单个64k数字或缺patch配方改书，不授作者因果/通用上限。

## [DARTH-PUM: A Hybrid Processing-Using-Memory Architecture](https://arxiv.org/html/2602.16075v1)

2+2+2=6。实际§4（307–331）analog ACE与Boolean DCE tile；§4.1（347–370）partial products边传边shift，等transfer complete再add，ADC产率对齐DCE每cycle row write并摊销warmup/cooldown，非‘把两个模块同放内存就免费’。§4.2（390–442）arbiter令MVM reduction不可被新digital指令穿插，pipeline-reserve使tmp-buffer不覆盖live寄存器，IIU table/counter展开重复ADD而非前端逐项issue，analog row/digital column需transpose。§5.2（588–597）attention动态矩阵写analog昂贵，整个attention在DCE/FFN在ACE，归一等由IBERT算法数字实现；并非LLM AR decode实测。

§6（623–651，706–725）MASTODON+CrossSim/MILO建模1GHz/15nm等面积CPU面积2.57cm²，SAR/ramp不同容量4.1/3.7GB，CPU i7与4090真机但PUM是模拟；CNN/LLM encoder/密码三workload不直接合并为foundationmodel服务。§7.1（726–751）LLM encoder71%时间non-MVM仍逊application-specific SFU；主文45.6×与摘要40.8×不同，不采用headline数。§7.5（792–806）CrossSim详细只模型programming noise+parasitics，read noise/drift/stuck/process仍需chip metrology；CNN75.4相等不认证encoder质量，完整可靠性future。精确encoder尺寸/序列/数值协议在已采用位置未披露，Not Disclosed，不授芯片/生产SLO。

actual `INFER-TENSORRT-LLM` [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md):816–821已解释CIM写代价/驻留及静态analog+数字SFU/pipeline，不能再重复‘混合更好’；未承载**用通用Boolean array替专用SFU时，partial-product transfer/shift/add、producer-consumer rate与live-buffer reserve共同保证一条MVM执行的边界**。拟若root认可一自然段接821后，仅这个dataflow差额与71%non-MVM/fabrication反側、旧SFU/GPU共存；未写。

## [Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution](https://arxiv.org/html/2602.16154v1)

2+2+2=6。实际§2.2–2.4（151–198）：speaker trace按newline切25/50/75%，3listeners只看prefix继续生成，reward是所有listener答案与speaker原答案matching计数（可共同答错）；fullrank GRPO后另训LoRA answer-only masked SFT再merge，非同一combined reward也非对reasoning参数无影响。Eq2 lambda等listener数，但match最多3×3=9，不能称两尺度自动相等。测试只speaker，训练额外listener续写仍付费。

§3.1–3.2（201–227、373–378）：1250 BBH/3epoch Qwen3-14B与Phi4，listener Ministral/Phi4/Qwen；评估BBEH过滤120MC、MuSR murder250、ZLB3259/FOLIO202。hint usage只在答案随hint改变子集、token detector，不是全样本truth或内部faithfulness；AOC按20%截断/注错，响应依赖proxy不是causal computation证书。§3.4（393–403）match-only提升hint却降acc，correctness-only反侧，joint reward冲突；§4（536–581）3same/1random listener受限消融，1random计算更少，不授异构单因素全收益；643–654 FOLIO in-domain样本1000 vsBBH1250，accuracy更好但hint降到base下，无通用Pareto。AppA（1055–1062）G5/b64、TP4、KL/entropy.001、LoRA32/128/drop.05/5epoch，混合A6000/A100/H100，precision/seeds/总GPU时间Not Disclosed。

actual `TRAIN-GRPO` [Ch33](../../../../../books/part-04-training-system/33-grpo.md):215–231已有终局与process/PRM信号权限及成本；237 evidence-step也明确不识别真实内部。这里不是重复‘过程要评估’，差额是**多个listener消费partial trace的匹配reward与答案正确监督分开成RL→answer-only SFT，且一致性不授truth/faithfulness**。拟最多一段接231后/特权目标233前，保留额外listener预算、hint/AOC有限与outcome-only旧方案；不重复Ch29通用SFT数学。未写。

## [Beyond Learning: A Training-Free Alternative to Model Adaptation](https://arxiv.org/html/2602.16189v1)

2+1+2=5，标准必要审。实际§3.1–3.3（119–169）：只nn.Linear leaf/name+shape相同，排embedding/norm/head；last-generated-token postlinear L1均幅跨input/step的源靶差排topK，再复制weight+bias/dtype无优化。结构相容不证明功能坐标、激活差也不识别唯一因果模块。§4.1（203–231）MATH500仅抽50，SEED42 greedy，max_new_tokens32/64/128/256/512、K8/16/32/64/128；按每配置先测source/target再选较强→较弱，缺独立diagnostic/select/test人口说明。§4.2（232–289，427–462）BestK也是该条件最大test-accuracy；6→12即多3/50样本，300%gap来自source-target差2个百分点，不普遍capacity翻倍。K非单调、equalbase recovery分母0；Gemma64tokens0增益。§4.3/5（470–488）更广域/heterogeneous compatibilityfuture；没有random-K/all-copy/匹配校准budget对照支撑LAE比一般module replacement更优，也没retain/safety suite授其‘保留大部分旧功能’。

actual `TRAIN-LORA` [Ch30](../../../../../books/part-04-training-system/30-lora.md):579–593已有composition admission、同backbone坐标、activation建proposal但不证function/causality与独立quality gate；Ch29:727–744已有专家独立/合并与retention。局部直接拷贝方法可报告，不把没有topK recipe当Books知识缺口；拟仅报告，避免把50题上best-K恢复写成可发布rollback。若root裁具体direct-copy选择仍需长期窄解释，仅审该已读边界，不扩全部迁移实验。
