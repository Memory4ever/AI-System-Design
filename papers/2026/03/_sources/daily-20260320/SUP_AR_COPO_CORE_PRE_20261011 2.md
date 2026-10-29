# AR-CoPO17461：pivot邻域探索与参考候选重放

resume_mar17，2026-10-11，仅03-20补03/19。本日第六批准入、日级夹证与2+2+2=6有效复用；不是新的query或跨日家族。恢复实际重读适用合同、Sources/Prompt/完整ROADMAP、本日README/STOP与Books约束。本文只准备必要Source/actualowner/两literal PRE，交非准备者裁；未自授PASS、未写Books/计safe或DAY。

## 1. 必要原证与停止

实际[exact-v1](https://arxiv.org/html/2603.17461v1)§2.2–3.3/Eq1–4/Alg1 L79–160、§4/T1–3与直接反侧161–238、结论239–241、仅附录关键配置/T4及第二底座反側242–261。前文L56–78只必要few-step/CM探索动机。图只读正文/图题，未冒像素差异或训练曲线精确值；未读references、全部图、代码或其他旧版。当前official Comments的ECCV说明已准入时轻量核验，无明确机制/纠错信号要求全版本diff。支持和关键反侧够下面有限接口即停止。

## 2. 采用的训练接口与强桥隔离

先共享自产历史h到随机pivot p；只在p初始噪声构造G个邻域候选，每条分支完整续写并解码后获得sequence reward；重放所保存p轨迹，仅该chunk反传，CM的距离定义在clean预测hat-x0空间而不是把它当真实transition概率。组内softmax距离是训练surrogate，和部署原sampler分布分开；参考/noise/policy/历史KV及reward身份须共同保存。

L115共享其他初始/solver噪声是common-random控制，但L116“除p外全部视频相同”并不由此成立：后续chunk消费改变后的h。例如p的输出a不同，下一chunk deterministic f(h,epsilon)=a+epsilon，即使epsilon共享，下一chunk仍不同。sequence reward对pivot扰动包含其后续传播效应，不是pivot自身的独立即时credit或全局唯一因果。只采用受限fork/更新边界，不抹去原文强宣称或把全篇改EX/假NC。

另一分支冻结initialization reference的100组候选/reward，current重算anchor并在缓存候选内更新；两个独立LoRA分别on-policy与reference-replay，再加权合并。ratio clipping是surrogate目标，不直接给硬trust region、零stale bias或原连续sampler的全部概率比保证；PPO式min项并非显式参数约束，负advantage一侧也不能由clip名义推出每个ratio始终有界。训练对象/旧policy与reference、replay人口和合并参数须分别验收，不采用精确全配方或普遍稳定定理。

## 3. 有限评价、直接反侧与全费

训练MovieGen Video Bench、VideoAlign TA/VQ/MQ三reward，独立名称的VBench测量另报但不是已证明无reward hacking/无数据重叠的审计。Self-Forcing及附录Causal-Forcing；LoRA rank64/alpha128、24GPUs（型号未披露）、G12、lr1e-5、anchor4、100reference组、100iterations、每iteration两updates、sigma.5/clip1e-4已披露，不写全部配置ND。必要段未披露完整model size、precision、resolution/frames/chunks/T、训练/评测prompt人口split与重复/CI、solver差异匹配、合并后端与端到端latency/tail/SLO。

T1 Self-Forcing on-policy VBench Total82.15→81.99、Semantic71.27→70.71；semi VQ3.80→3.70/MQ1.68→1.60/Overall7.76→7.61；merged Semantic70.55低于71.27，Total82.17相比82.15只.02，无CI不可授无损。T2是TA-only，不能混同T1三reward；on-policy TA2.28→2.63却MQ1.68→.25/Total82.15→79.26，no-clip参考分支也退，支持分验proxy与外部质量而不是证明clip完整稳定。

T3合并从0到1提高Overall7.61→8.33同时Total82.45→81.99，.8选用是在该已测表中按两aggregate选择，不是所有切片保持。T4 Causal-Forcing所选.5 Semantic70.70略高于70.35，但Total82.25低于base82.28；正文“both benchmarks最佳/consistent gains”须限定，semi又MQ1.42低于1.43。第二底座尺度变化及这些反侧保留，不授默认.8跨模型/普遍质量保持。未核图像或人评实现，VideoAlign分数不是本人独立人类偏好验收。

共享prefix只节省重复前缀；G条后续完整rollout、VAE解码/三个reward、存储与current replay、两套adapter训练和合并仍计费。单chunk反传不等总GPU费用或每请求在线速度；必要段没有完整吞吐/时延/峰值memory与wallclock比较。一次强命题请求只为固定prompt/split与noise/历史传播trace、surrogate/old-reference概率对象与staleness、matching全预算/质量分项及合并后的独立评价；本有限接口不依赖先取得这些强保证。

## 4. actual sole owner 与两 literal PRE（待非准备者裁）

实际[Ch33](../../../../../books/part-04-training-system/33-grpo.md)完整330–398，其中typed内部credit、cross-trajectory transition surrogate及TurningPoint ODE continuation已覆盖一般内部credit，却未承载few-step CM在pivot初始噪声fork/共享后续noise、sequence reward只更新pivot与冻结reference候选单独adapter合并的具体分责。[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)650–682仅少步sampler/历史传播交接；Ch32/34入口只PPO/DPO责任。不复制生成配方到Ch24或一般LoRA合并到Ch30。sole拟`TRAIN-GRPO`原TurningPoint两个完整段371之后、GRPO成本标题373之前，两段构成探索和部署质量验收交接。

少步AR生成的探索还可放在一个pivot chunk的初始噪声，而不强行把全部采样改为SDE：先共享自产历史，在pivot附近构造多个噪声候选，各分支完整续写后取得终局评分；保存pivot轨迹，只对该chunk重放反传，用当前clean预测到旧候选的距离softmax构造训练surrogate。部署仍使用原少步sampler，这个有限候选分布不是其真实transition概率。共享其他噪声只减少随机混杂，改变pivot也会通过历史影响后续内容，终局差额不能说成仅该段自身的独立即时credit。history、noise、候选policy/reward与replay版本应绑定，不由局部更新范围宣布唯一因果归因。<!-- source-family:SF-2026-ARXIV-2603-17461 -->

[pivot探索与参考候选重放的有限对照](https://arxiv.org/html/2603.17461v1)还把固定reference候选的更新与当前policy探索分开训练，再合并两套adapter。clipped surrogate不自签硬trust region或旧候选始终有效，合并后也要重新验收质量：局部reward改善仍伴随语义/运动切片反退，所选尺度的aggregate保持不等所有任务无损。完整分支续写、解码/reward、候选存储、replay与两套训练都付费，少反传一个chunk不等全部成本更低。代理失配、历史传播或合并质量退步时，保留reference/原sampler、减小合并尺度或用普通终局/可靠过程评价，不让单个reward分数替部署质量签发通过。<!-- source-family:SF-2026-ARXIV-2603-17461 -->

静态注：

- `SF-2026-ARXIV-2603-17461` — [AR-CoPO exact-v1](https://arxiv.org/html/2603.17461v1)必要§3/Eq1–4/Alg1、§4/T1–3与附录配置/T4。仅pivot初始噪声fork、sequence reward/current clean-distance surrogate局部更新与reference候选独立adapter分采；保共享noise非后续内容相同、clip非硬trust/完整概率、合并/TA与第二底座反退和全费用，不采唯一因果、精确recipe、无损/免费或生产速度；未核代码/复现。

准备完成交非preparer一次必要Source/actualsole/literal裁，不自PASS或写Books。

## 非准备者必要 Source / actual owner / PRE 裁定

root 实际读 exact-v1 §3.1–3.3关键 fork/clean-distance surrogate/参考候选接口、§4 Tables1–3及附录 Table4/配置的直接反侧。独立 DataCite created/registered03-19T02:32:49Z、v1 Updated03-19T00:55:03Z 与本批公开日夹证相容，后v2事件不代替本v1或自动触发全版本比较。共享其余随机噪声不固定后续历史条件，因此 L116 强宣称不采；clip 是 surrogate 非硬 trust-region。Table1/2/3/4 各质量口径和合并尺度反退实际存在，局部接口可独立分采，不授完整因果信用或全成本收益。

实际 Ch33 345–390完整交接和两 PRE/static 逐字核：已有内部 credit/ODE 续推尚缺 CM pivot 初始噪声 fork 与冻结 reference 候选分别训练/合并的责任边界，可在 TurningPoint 完整后/成本标题前承接。必要 Source/date、actual差额及两PRE PASS，6分保持；授权 resume_mar17 sole Ch33 两段及本人静态注窄写，root 写后一次 actual 完整局部/末注 POST。未实际写入不计 Integrate，整日 DAY 尚未授予。

## 窄锁后 writer 实际读回

resume_mar17仅按root已通过的两literal PRE/static，实际写Ch33 373/375及本人3230；完整357–396与3222–3230实际顺读，TurningPoint完整后/GRPO成本前责任链和原静态邻注保留。两段及自身注与原PRE逐字一致，scoped本family diff仅该三处，限定diffcheck0。当前旧表/其他日期Books修改不触碰，无过程身份回写。交root一次非writer actualPOST，未自己授POST/safe/DAY。

## 非写入者实际 POST（2026-10-12）

root 实际完整顺读 Ch33 357–397 及末尾自身/邻注，回对有效必要 Source 与两 literal PRE/static。两段确接在 ODE continuation 的内部 credit 边界之后、GRPO 完整成本之前：pivot 初始噪声探索、终局评分、局部重放与 reference 候选分支分责准确；共享 noise 非后续内容固定、surrogate 非真实 transition 概率、clip 非硬 trust region、合并质量反退与全费仍在正文。正文和本人静态注与 PRE 一致，旧内部 credit、TurningPoint 与成本段保留。一次 nonwriter actual POST PASS，root 接纳实际整合并释放 Ch33 本 family 窄锁；6分保持，不授整日 DAY、唯一因果或生产性能。
