# 第十五包：AB9前四项必要核心与实际owner（待非作者PRE）

只续已校准的具名潜力22817/831/868/871，不扩库存。精确v1完整题摘/必要HTML与当前官方Comments实际读；FETCH_AB9_CORE保留执行2026-10-05T20:19:00～03Z。当前Comments分别为ICLR2026、无、无、无，未見撤回/纠错信号；不默认修订diff。22831发现题名/多benchmark摘要与原v1不同，只重新绑定本项到原pilot，不采用发现稿BBQ/DailyDilemmas及78%等headline。

## 同ID日期

原abs v1 Submitted均为02/26UTC，晚于02/25 19:00Z，官方POLICY给首公开下界02/27 09:00+08。sameID registered恢复已存在上界，秒精度+1秒取半开区间，不说是首公告/技术原源。全部落本窗。

| ID | submitted UTC | registered UTC | 公开区间+08（左含右不含） |
| --- | --- | --- | --- |
| 22817 | 02/26 09:58:10 | 02/27 02:55:24 | 02/27 09:00:00～10:55:25 |
| 22831 | 02/26 10:17:57 | 02/27 02:55:46 | 02/27 09:00:00～10:55:47 |
| 22868 | 02/26 11:08:11 | 02/27 02:56:46 | 02/27 09:00:00～10:56:47 |
| 22871 | 02/26 11:08:39 | 02/27 02:56:50 | 02/27 09:00:00～10:56:51 |

## 22817 HGPO，2+1+3=6，建议Existing Ch33

原blocks21–57/59–78/119–125实际读。旧stepgroup仅current-state相同，memory历史不同造成比较人口错位；原Eq3–7按相同state后缀逐级嵌套分组，w_k∝(k+1)^α固定函数，α默认1并跳过zero-advantage组，**非learned uncertainty自适应**。state suffix只为所写group proxy；prompt还含actions/stepcount，不能由相同observations认证完整effective-prompt相同。K越大oracle组小，利用率下降；原3test seeds/Qwen2.5 1.5/7B、ALFWorld/WebShop、GiGPO同新verl-agent/超参直接控制，K2去层级在WebShop可更好、uniformα0亦部分更好，7B K4 OOD/taskscore有反退，非always superior。

局部理论/预算隔离：Prop4.1/52–55所写Var=sum(w²v)漏嵌套估计器covariance；例如A0=A1=同一均值0方差1的X、w=.5，满足所列bias/variance序但实际Var1而公式.5。只隔离该variance等式及由独立性偷渡的保证，经验分支不整项D，不遍历AppendixBproof。原72称额外.425/.472s小于.001%，但Common约282–298s，前者约.14～.15%而不是所写值；保表秒值，不能授该比例。2/4H100、160iterations、response512、prompt2048/4096、G8×16env、max50/30、γ.95、训练temp1/val.4、rule-based reward10/0及invalid−.1；precision未披露，hash/storage/rollout/调参非免费。

实际owner `TRAIN-GRPO` Ch33 1477–1498完整邻接已读，尤其1485–1487已具体承载current observation相似却history不可比→层级membership/behavior-policy identity，以及样本变小、variance、hash/fragmentation成本与trajectory/critic退路；2548旧note不替代实际正文。采用的长期命题已由正文覆盖，建议Existing/NoChange，只在日报保固定权重/原经验切片/两处局部冲突，不为HGPO论文名制造gap。

## 22831 Moral Preferences of LLMs Under Directed Contextual Influence，2+1+3=6，拟Ch66窄差额

原v1 blocks15–61/63–92/104–124/151–154、277–282、302–307实际读，原题名不同于发现稿。pilot trolley forced binary，5demographic、人数1～10、7cues matched A/B，base/A/B、顺序均衡，每comparison8次；5families，reasoning低effort或step-by-step不同开关，不能合为同预算/内部原因。binomial/z/Wald α.05，未采用通用false-discovery保证。baseline近.5仍有asymmetry与backfire，reasoning降低多数cue敏感但放大fewshot；irrelevant grammar保留对照支持semantic/format分责但非全surface控制。原77约40%与figure79近三分一口径不合，不采用精确总体比例。

valid-choice为分母、refusal删除且retry；Llama局部invalid51/48%，Qwenfewshot不同方向9.2vs41.2/14.6vs61.3等，故conditional preference不代表全部请求effect。CoT由Gemini3FlashPreview classifier/多数分类，taxonomy又来自Claude，不读取隐藏意图或拒绝cue就无影响；约8样本choice差噪声、pilot/artificial/eval-awareness、规范可取方向须由外部policy判断。硬件precision/总APItokencost未披露，不授生产安全或道德真值。

实际owner `PLATFORM-EVALUATION-SYSTEM` Ch66 150–179 source-modality truth/self-report与179–208 capability/monitor pressure、joint/conditional/不可识别完整邻接已读。它们承载self-report无truth，但缺**baseline/A/B direction-flip将neutrality与双向response分开、valid/refusal人口随cue变**的具体测量选择。拟在同压力paired-condition附近仅一段＋ownnote，保方向反退与refusal denominator、classifier权限/成本/普通baseline共存；不以一般偏好理论或道德benchmark名造gap。未写，待窄lease。

## 22868 ReMix，2+1+3=6，拟Ch24窄差额

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；未提交soft/MASK与hard commit分责，JS reset非correctness/进度保证。2+1+3=6，Ch24自身末注1770；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：blocks30–51/65–70/85–87；未提交M/C与hard T分责、JS只重置未提交状态；阈值/全路径费用与不保证进展。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

原blocks23–51/53–70/77–80/85–87实际读（41–58因输出截断已定点补读）。M/C/T三态：未提交位置用β Wᵀp+(1−β)MASK；adaptive nucleus min(2pmax,.9)，遗漏mass回MASK；confidence>.8才hard argmax，连续两轮JS>.1～.4才未提交C→MASK。**已T不撤回**，不是correctness reject/原分布exactness。discrete-trained网络读soft状态存在distribution shift，β过大/阈值过宽质量退；Table3 block64 GSM微退，非allquality lossless。Alg1 while只以全T结束，恒定低confidence输出即可不终止，未写硬max/强制progress；只隔离伪码generaltermination保证，不断言实际code会hang或全算法D。

LLaDA8B/MMaDA8B、gen256/block128 semiAR，语言8A100其余8RTX3090、WINO协议；VL GPT4omini/CIDEr不同评估，seed/batch/dtype/concurrency/SLO未披露。β.4/.5/.6选点，qual/speed按具体slice；runtime单GSM profile2.52s中mix.14+reject.09=9.12%非zerooverhead。maintable不同step列不当成per-forward时延，更不授生产并发。

实际owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 410–445已完整读：现08302是**self-predicted双输入训练+top1 soft/mask、已有位置重写**，不是冻结旧模型/full-nucleus tentative distribution/JS rollback。1400 entropy soft/hard是reward模型gradient接口，不能替代本generation state消费。拟在soft-state/revision邻接仅一段：只对未提交位置软通信与JS-reset、分布失配/无hard-progress保证/有限校准及成本，fallback保守mask/AR；不授消除allcontradiction。未写待lease。

## 22871 Diffusion Stitching，2+2+2=6，拟同Ch24一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；PRM原prefix限定、stitch后AR重算；chronology非依赖证书与总预算。2+2+2=6，Ch24自身末注1772；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：§3–4、blocks27–47/50–65/74–83；PRM prefix限定、stitch后AR重算；chronology非依赖证书、总预算与单path回退。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

原blocks23–53/55–99/109–117实际读。N4独立diff traces、PRM原**本trace prefix**评分、保aboveδ步骤＋best geometric-mean整trace/answer anchor，再按原stepindex拼接(score annotated)供AR重新解答；不同trace prefix变了，chronological order不认证跨trace dependency成立，best anchor/PRM分数都不是truth。原47明确gaps/contradiction，因此**不是speculative token逐位验证**。Math QwenPRM7B/Qwen2.5Math solver，code AceCoderRM/7Bcoder、HumanEval用NLrationale而MBPP代码行；Table6具体PRM按task不同，不能统称同一codeoracle。

同solver AllCoT/BestCoT/above/anchor控制支撑selection/recompute增量；pool缺正确subderivation、PRM错删/错高anchor均实际失败。温度/γ不同，baseline部分摘TiDAR、不同模型能力不因果归拼接；moreN GSM4→6/8微退，而“并行不增加延迟”不授总GPU/通信免费。原74声称包括diff/PRM/AR forward，Table4只写最长diff+solver，两口径不可合并为统一compute比。固定512/4gen具体metrics，all_gather/content驻留/PRM/AR/context费全部计入，hardware/dtype/batch/seeds/SLO未披露，不采用统一1.8×/原分布保真保证。

实际Ch24 410–445的同chain mutable/reject分支与本**跨离散trace substep evidence→AR consumer重算**不同，834 causal prefix验证亦不同；Ch8 282–320宽轨迹proposal/selector已读，只留认知handoff不重复新生成接口。拟Ch24 soft-state之后窄一段：探索/打分/拼接/重算四种权限与matched-solver control，强调PRM原prefix分数不可直接迁移/额外forward和负侧；不用AR solver文本被称verification而赋真值。未写待lease。

本包提案1E3I，全未获root实际PRE/写后复核，不计safe；已有35safe不变。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22831：原必要blocks35–61/82–85/104–111/116–124及采用相关prepared控制/反侧与actual owner独核；Ch66正文206/完整190–216/own5675 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
