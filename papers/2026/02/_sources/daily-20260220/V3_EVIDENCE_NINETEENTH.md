# 02/20 第十九有限证据包：MMA / Jury / AREG

当前仅这三项，延续本日同一有限潜力集合，不重排435库存。使用本地 exact-v1 HTML 经 `V3_extract_html.py | awk 'NF' | nl -ba` 定点阅读；无实现运行/复现。官方v1事件页轻查身份/可见说明：16493仍v1，16610后续May28v2不借用，16639只用本次v1身份；可见页未示撤回/纠错告示，不遍历完整版本史。日期沿首包已root独核announcement→same-ID DOI桥接，下界均2026-02-19T09:00:00+08:00；Registered加1秒上界分别16493 **10:47:31**、16610 **10:50:31**、16639 **10:51:13**，半开范围均落本窗。原Submitted/Registered见各`V3_DATACITE_2602.ID.json`，不称注册为精确公告点。

## 2602.16493v1 — MMA: Multimodal Memory Agent

**2+2+2=6；标准必要方法/比较及直接限制完成，拟已有覆盖；尚待root独核。**

原abs69/77、core137–247、eval283–305/308–350实际读。Source为predefined prior、Time为half-life decay、Consensus为邻居confidence×cosine的加权和，再clip；这是heuristic retrieval reweight，不是校准truth概率。Eq4通过其他item confidence递归依赖；本轮不声称其迭代/收敛实现已验证。Cosine正负仅相似度，不自动识别语义矛盾或独立corroboration。

FEVER first500/三seed比较保局部raw约59.9和seedstd，不能由三seed宣称一般统计保证；LoCoMo sparse上st去Consensus更好。MMA-Bench生成10session/约六个月叙事，在reliable-A/unreliable-B先验中放入视觉反转/模糊/无证据四type；text mode是oracle captions，vision mode rawimages，不将其差异全归内部视觉bias。GPT4.1mini fullcontext、MIRIX/MMA retrievalcontext不是相同证据量。有限ablation中Full TypeA视觉50%、去Source/Time0%；Full TypeD CoRe=-0.38，去Consensus=-0.69，但Text→Vision Full0.69→-0.38仍退步。Baseline TypeD=1可来自未检到相关证据，不能让仅Unknown标签认证正确理由；response rationale也不证明隐藏机制。Strict consensus在稀疏证据环境有代价，post-retrieval不能补未召回证据，作者直接§Limitations承认这两项。未采用“safetycritical superior”或“visualbias必由某层继承”中心宣传为因果。

关键差额实际比较 **AGENT-MEMORY Ch77:960及945–970邻接**：正文已明确post-retrieval reliability / selective action、source calibration / validtime / independentcorroboration / contradiction / supersession，heuristic非truth probability，且没有单一consensus规则占优。该段实际已承载本篇可保留的长期命题；不宣称MMA全部公式或完整benchmark已有。具体收益与四type/视觉反侧留本报告；无必要新Books正文。性能硬件/precision/端到端latency、batch/concurrency/SLO未披露，本项不是吞吐研究。

## 2602.16610v1 — Who can we trust? LLM-as-a-jury for Comparative Assessment

**2+1+2=5；具体无标签比较接口缺口受影响深入，拟窄整合；尚待root独核。**

完整AB58，§3.2/3.3 111–154、setup157–169、results351–378、459–460、540–547及必要judge配置1108–1109实际读。成熟BT本身不算新贡献；实际差额是多judge同pair softprob不先均值，而同时拟合item-skill与judge-specific正scale：P_k(i>j)=sigmoid((s_i-s_j)/σ_k)。若全judge同scale，对item梯度等价先平均prob，不能刻画judge异质性；多个scale是comparative noise/distcrimination的相对proxy，不提供无标签外部真值。加常数到s，或同时正缩放s/σ，保持预测；本轮逻辑说明绝对unit不可识别，不能把1/σ当校准正确率。Singlejudge scale可吸入s，relative区别需multi-judge与连通比较支撑；共同bias、错误但自洽多数不被该fit自动去除。

SummEval100articles×16summaries、TopicalChat60contexts×6responses、四aspect；每context N(N−1)有向comparisons。八instructionjudges（Llama3.1-8B/3.2-3B、Mistral7Bv0.3、Phi3.5mini、Qwen2.5-3B/7B、DeepSeekLLM7B、Gemma2-9B），yes/no logits取prob，humanlabels仅测每context SRC再平均，不用于fit calibration。相同pair池比较AvgProb/softBT/hardBT/BTσ及aspectvariant；localSRC改善不授其他pool正确。原hard/soft关系有环境依赖：TopicalChatENG highnoise、hardBTσ局部胜soft，aspect-specific更复杂并非单调更好；Mistral cycle反例说明CycleRate不唯一解释收益。1/σ与humanSRC/cycle correlation仅此数据描述，impact明确shared/systematicbias未消除。未披露足够重复run/CI、fit优化/scale约束、hardware/precision或完整调用/fit端到端成本，不采用通用排名/生产效率保证；不为必要命题遍历无关附件。

实际 **PLATFORM-EVALUATION-SYSTEM Ch66:291–304与316–333** 已局部→BT/Elo、human residual区间、prompt-specific latent quality、能力/bias和有限panel预算，**未承载多judge同pair的无标签joint relative-scale fit**。拟紧接第291段加一段条件分支：缺human标注时保逐judge pairprob，jointfit itemrank与relative discrimination，不先平均；该signal只是测量模型下的内部可解释性，不是truth，外部anchor/报告Unknown/人工分支仍在。保存judge/prompt、同pair图与pool、额外comparisons/fit及参数尺度；不会用posterior高置信授release。独有接口有长期意义，不提Structural Candidate。

## 2602.16639v1 — AREG

**2+1+2=5；标准完成，拟仅报告；尚待root独核。**

复用once-core§1/3；补读154–258、312–340及directlimits544–573。八models、Jan2026OpenRouter snapshot；56orderedpairs×5rounds=280games，最多10turn、perdialogturn1024token，双方T0.7；Grok4.1Fast T0 arbiter读全部history/privateledger，把explicit即时新承诺转Δ金额，conditional/future/ambiguous为0，delta扣除已有金额。这个“金融转账”是模拟自然语言commitment的judge状态，不是真实payment receipt；T0不能证明endpoint确定性或判定为真。45随机transcripts人工零异常与96.1%自报confidence不授整池无误；singlejudge/stylebias、English/charity93.8%和snapshot限制原AppendixA直接承认。

分开C-Elo/V-Elo符合角色不对称；ρ=0.33只在八模型/该game人口，有限样本无量化不确定性不能推内在能力普遍独立。All-V>C还受pairedzero-sum/角色成本与rating更新口径影响，不授全领域防御强于说服；三次commit与singleask观察61.4/22.2是已发生轨迹的posthoc切片，不是随机干预“增量要求”的因果收益。虚拟账本及自动裁决也不证明真实effect或授权。

实际 **PLATFORM-EVALUATION-SYSTEM Ch66:60能力/Policy分账、318–320 slice/异质性/聚合限制、4298起 exposure→执行→环境结果→独立adjudication** 及 **AGENT-MULTI-AGENT Ch82:565–596** 已不同角色/对手/恶意peer与failure分账。此次charity/localtournament负相关是测量盲区的有限证据，未建立长期角色识别或可靠执行新接口；不因一项新game/dualElo配方或待写具体金额模型强造Bookgap，拟仅报告而非“完整benchmark已有”。preserve潜力/原证，不因NoDiff排除本篇。

## 批次边界

只请求这三项必要source→owner/处置独核，16610须PRE后取得Ch66窄段及自身note具体写锁；其他两项无Books修改。当前日仍73root已授终态、23普通未完；本包三项尚不计终态。作者没有共享锁，没有stage/commit/push。

### root 独立审阅与实际写后结果

以上为送审时快照。root 实际核16493 confidence §3.2/有限反侧与Ch77:954–966，已有覆盖限定通过；16639 tournament/single judge/45人工审样与英语charity限制，仅报告通过；16610 §3.3/Eq12–13、§4/5.2/impact 与Ch66:285–306，必要PRE通过并授一段及自身末注窄锁。作者实际写入Ch66:293及末注，顺读完整邻接；root实际独核body293、289–303邻接及自身末注5580，POST通过，锁释放。当前76终态＝45实际整合POST、11争议隔离、5具体已有、15仅报告；普通余20，不授整日完成。
