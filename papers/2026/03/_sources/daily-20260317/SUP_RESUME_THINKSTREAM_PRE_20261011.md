# ThinkStream12938：必要原证与两段PRE（待独核/未写）

仅本17补03/16自然日；完整exact-v1题摘、日级实体夹证及具名去重准入有效复用。resume_mar17实际必要[exact-v1](https://arxiv.org/html/2603.12938v1)§3–6/Eq1–7/Tables1–7、A.1/Alg1/A.2/B/C/D，E在HTML空块，以[同v1 PDF](https://arxiv.org/pdf/2603.12938v1)p23–24恢复。当前abs仅v1/无已给出的具体撤回或勘误信号，不冒称全网无纠错。2+2+2=6，混合保留状态/训练到runtime边界具体差额深入，不给一般cache原则增分；未核artifact/复现。

## 必要证据与反侧

每chunk vt先生短rt，再silent或response ct；推理不是暂停观察后的完整batch CoT。§4.1 Eq3明确视觉τ=max(1,t−W+1)..t，推理/动作文本τ=1..t全保留；视觉有界不意味着总KV/上下文有界。§4.1声称effective context稳定、Conclusion boundedmemory不能从慢增长推成常数：每chunk只要平均生成非零文本，总textKV仍随chunks增加。这是本轮公式分析，不是实测memoryleak/代码必错。只采原式有限混合状态分支，不授无限stream固定memory/latency或压缩无损。

Eq4符号全history不代表runtime保留全部原图；实际消费必须按RCSM可见状态理解。Alg1是ActiveChunks≥W时先prune再prefill/newdecode，当前visual窗有限；主文oldest vt−W与Eq3边界文字不一，不采用精确off-by-one recipe。A.1用静态KV/CUDAGraph decode与inplace shift eviction，variablelength视觉prefill eager，FlashAttention kvcache/FlashInfer sampling；物理搬移不证明旧KV重新拥有当前position/visibility，未给完整position rebasing或token layout规格，不认证完整执行实现。A.2训练FlexAttention模拟相同RCSM mask/Liger，支撑需要训练可见性与部署保留一致。

§4.2 G完整stream trajectories、clipped/KL与accuracy+format+time三项相加，accuracy只按答案匹配；time=max(0,1−|tresp−tgt|/w)并无正确性gate，错误但及时/合法格式仍可获这些分数。rho粒度/全部超参未说明，不采精确GRPO实现，答案/格式/时间reward不验证内部CoT事实或真正证据充分，更不授physical action authority。

数据110k cold/9kRL，PySceneDetect→Qwen3VL235B segmentcaptions→39情景/QA→CoT。PDFp24明确NoFuturePeeking只能引用时间≤Tthink的caption/user，不能错误记“无因果提示”；但一次生成看到整个caption/conversation，提示约束不是独立prefix泄漏审计。p23输出仅user的模板与文字dialoguehistory不完全对齐，不采用完整数据生成recipe。公开方法既有因果约束意图与训练mask，不认证所有合成样本都满足因果/时间真值。

Qwen2.5VL3B/附录7B，训练8H20/AdamW/coldbatch64 lr1e−5/RLbatch8 G8 lr2e−7/2FPS nativeDynamicResolution；steps/epochs/precision/seed及完整pipeline费用未披露。Tables1–3不同backbone、训练/资产/输入和外部baseline预算不构成samecompute公平；若干slice反退，OVO ATR StreamForest71.55>69.82、Streaming CT Dispider45.80>45.21；附录同7B OVO EPM51.52→51.17反退；58.59属32B对照，不能混作同7B原值，不把平均增益变成全部旧能力保持。

Table4（文字误指Table5）0/5/10/20/30tokens-per-sec中20:OVOBW52.3/380ms、30:52.6/505ms；30并非更好延迟，20不是普遍最优。Table5 30s窗OVOBW51.6低20s52.3，增加视觉不单调。Table6 caption48.7低noMemory56.9、coldCoT60.5/RL64.8，memory内容/额外训练预算变化，caption不是同tokens/同training的独立压缩因果消融。短窗+派生文本有限收益，不授所有历史充分性。

§6.3作者batch1 154.07vs30.06tokens/s、batch8 766.87vs276.10有限backend比较；动态图/graph/eviction多项同时变化，不是RCSM单因素；设备/precision/输入输出实际分布/并发/tailSLO/完整生成与训练费用未绑定（8H20只明确训练，不回填推理hw）。有限视频长度下<0.5s曲线不是无限流/硬实时保证，decode吞吐与端到端按2FPS负载分开。新增captioner/合成审核、SFT/RL/视觉编码、每chunk推理输出、shift/gather、长期textKV与独立任务回归都计费。

## Actual owner与具体差额

实际Ch19 195–261已读depth/value最小状态及position/slot/visibility；Ch45开篇handoff、Ch23派生modality身份定点搜索作边界，不新增该章owner。实际Ch22 95–123容量/读取合同、215–280稀疏/immutableprefix近期reasoning/anchor，304–306三段summaryhandoff已读：现prefix+recentreasoning是截旧推理，不含保全部派生reasoningtext而只滑densevideo的反向保留；summaryhandoff不等持续生成可错的symbolic状态。唯一MODEL-LONG-CONTEXT拥有哪个历史继续可寻址/派生状态容量选择；不是Ch19物理cachelayout、Ch23一般派生来源、Ch77 Agentmemory lifecycle。拟接Ch22 PrefixSliding限定最后一段后、ContextAnchor前，仅以下两段。

## 两段逐字PRE

滑动窗口也可以只作用于密集的观测表示，而不同时删除模型已经生成的工作文本。一条流式视频分支在每个chunk到达后生成短推理及回答或silent标记，保留近期视觉K/V，同时把全部已生成的推理、回答K/V留作较稀疏的历史条件。它与“固定task prefix＋近期推理窗口”的取舍相反：早期细粒度视觉退出直接读取，生成文本继续可寻址；文本只是当时模型的解释、事件概括或假说，不是原图、事实真值或未来query必需信息的无损替身。训练attention可见性和部署保留/淘汰规则必须一致，物理搬移也不能静默改写旧状态的位置身份。<!-- source-family:SF-2026-ARXIV-2603-12938 -->

这个分支只给视觉状态一个窗口上界，并未给总缓存常数上界：只要每chunk继续产生文本，累计文本K/V仍增长；生成较慢不等固定大小。[ThinkStream的有限消融](https://arxiv.org/html/2603.12938v1)中，推理预算和视觉窗口都有质量/延迟取舍，普通caption memory还会退步，不能据有限平均收益授全部历史充分性、事实保持或无限流实时保证。视频caption与合成审校、可见性训练、每chunk视觉编码/推理、cache搬移和长期文本读取均计费；时间/格式/答案reward分别验收，不替内部推理真实性签字。精确回看、派生错误累积或长期容量不适配时，保留原视觉回读/检索、更大直接窗口或独立校验，并为文本历史另定截断/压缩策略再做任务回归，不让观测压缩自行获得安全或发言授权。<!-- source-family:SF-2026-ARXIV-2603-12938 -->

未授Books锁，Source/actualowner/PRE待独核。中心无限/总有界headline明确反证收窄，不借一般textmemory原则或旧source摘要计NC/已完成。
