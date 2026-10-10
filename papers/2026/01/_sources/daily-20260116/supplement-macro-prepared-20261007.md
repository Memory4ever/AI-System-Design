# 01-16 / MACRO-LLM 决定性原证与 owner 差额

root 已实际必要源与owner PRE通过并授Ch82窄锁；作者两段174/176与自身1342note写完、实际150–210完整邻接顺读，root独立实际157–190完整邻接、新正文及自身note POST通过，锁释放。未授日级Gate。

`2601.09295v1` 原HTML、abs及exactDOI保存在supplement-20261007。v1submitted Jan14T08:54:55Z只发现；正常公告政策BJTJan15下界，registered Jan15T02:42:44Z公共存在上界，**非registered=first-public**。论文没有直接作者project/release链接，仅旧外部simulator引用；未作全网追史。

## 决定性贡献

§3.3/C改变的共享对象是neighbor的`(weighted mean μ, weighted variance σ², total weight W)`；用weighted Welford/明确disjoint-set merger把自身状态并入，化成virtual node textual prompt，与来自neighbor的具体action proposals一起进入下一轮confidence-weighted regenerate→rollout verification。不是只给既有三模块新名字。相比全raw observation共享，统计对象主动丢失个体身份、关系与尾部；原文没规定overlap lineage去重或误差bound，因此不能由合并得到真实global state或安全consensus。

§3.2/B实际候选最多10attempt×k horizon，当前步严格约束，后续放宽且t+1之后reward binary；不把LLM预测、约束式检查或attempt exhaustion最后best candidate当未来真实安全保证。§3.4所谓semantic gradient是reward下降触发的textual strategy rewrite，cosine transition scalar只是prompt强度，不是可证明数值梯度。

## 三维必要审阅与反侧

- Core§3.1–3.4/B/C、§4.1/4.2/4.5/4.6、Tables1/3、G/H/I已实际读。
- GPT4o-2024-08-06,temp.3/top-p1,OpenAIlib1.75,local4×3090；SUMO1.21，8车默认60s、0.5sstep，8/16/24/32车扩展。CACC headway改善但Table1catch-up速度RMSE `.897` 差于LAMEN`.648`/DMPO`.534`，slowdown`3.325`差于DPPO`3.121`/DMPO`3.059`（ToMBelief为`4.681`，原笔记误录已纠正）；不授多指标普遍优。LLMbaseline同GPT4o/interface，prompt适配非全部预算相同，trial/seeds/errorbars及完整latency未披露。
- G的per-agent `O(d·r·M)`仅degree、rounds、message定长且忽略stochasticity；total network traffic仍至少随N变化，固定统计长度也不授真实latency/SLO。MACRO完整episode与MARL重训时长不等于部署policy inference比较。保留planner、通信、rollout verification、retry、Python和API费用；AppendixI spatial/actionidentity/format failures揭示structured sender/receiver与deterministic arithmetic是必要外部consumer，不是prompt自动可靠。
- 不采用疫情应用的临床/政策外推。仅把通用局部统计协作分支写Ch82，2+2+2=6，明确真实meanfield对象gap故必要深入。

## 实际 owner 与邻接

已读Ch82开头至L250；当前Peer/Debate讨论同证据vote/独立性，接Blackboardtypedartifact，再接pipeline与topology admission。未有局部观察的`μ/σ²/W`带raw membership/统计损失的协作对象及需要哪层验证。精确差额不是再加“多Agent付费”，而是共享统计与proposal有不同权限/失效信息，compressed view不能冒充global observation。

### 拟两段：Peer/Debate后、Blackboard前（待root窄锁）

环境中的 Agent 各自只能看到局部状态时，完整共享观察容易保留个体和关系，却支付更多通信与上下文；另一条分支让邻居同时交换具体动作提议和定长的加权均值、方差、总权重，再把这些统计合并为一个 virtual-node 视图，参与下一轮提议与 rollout 检查。[MACRO-LLM 的受限机制](https://arxiv.org/html/2601.09295v1)改变了共享对象，而不只是增加讨论轮数：统计提供局部群体特征，动作提议仍需匹配 sender/receiver 和当前约束。统计聚合会丢失个体身份、关联与尾部；重叠集合若无 membership/lineage 去重，更不能当成精确全局观察或安全共识。<!-- source-family:SF-2026-ARXIV-2601-09295 -->

压缩视图能限制每次读入大小，却不免去多轮通信、候选 rollout、确定性计算、格式重试和模型等待；固定 degree/round/message 的每 Agent 复杂度也不证明整网常数成本或实时控制。原文小规模 SUMO platoon 的 headway 与速度指标有取舍，预测后续状态及放宽的远期约束不授物理安全；API 延迟、数值与身份错误仍需要外部检查。关系或尾部决定结果、统计支持不明、验证/延迟预算不足时，应回读相关原始观察、保留确定性 controller 与较少轮局部协作；可集中且预算允许时，完整共享视图继续合理，不由 virtual node 自动升级全局状态。
