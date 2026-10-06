# 2025-11-12 GPT-5.1 必要证据与 owner 决定

作者：Noether。准备：2026-10-04T21:00:17+08:00。供 root 独立核 Books 决定；不是 DAY 或写后 POST。仅本日一个家族，未写共享 Books。

## 已成立的日期与证据权限

[官方原 RSS](openai.xml) release/Addendum 两条 `Wed, 12 Nov 2025 00:00:00 GMT`，均为 BJT `2025-11-12T08:00:00+08:00`。采用官方发布字段，不反填正文日粒度时刻。[Ohm FIRST](FIRST_INDEPENDENT_REVIEW.md)20:33:29实际通过同家族准入、RSS落窗及2025必要核心，20:53:26重申无需空查。以后仅真实带时区且冲突的原公告到达才重开日期依赖。发布与card不计两家族，受限方向评分 `2+1+2=5`，不相加为10。

原锚点：[发布原响应](12-first-original.txt)L156–161、403–421；[2025五页card原文本](12-gpt51-pdf-date.txt)§1–3/Tables1–3及[Hub原响应](12-core-headers.txt)。当前恢复实际重新读取上述发布段、card全核心与表列，没有使用后续API配置。截图接口只有引用，未像素核表；没有模型执行/复现。

## 方向一：按问题重新分配思考成本

新增事实是 Instant 可以选择先思考，Thinking 在代表性ChatGPT任务分布、双方Standard thinking条件下，最快任务约2x快、最慢约2x慢。它反驳“本版本所有请求单向加速”，并不证明每个困难任务的边际计算收益、固定质量速度提升、scheduler实现或生产SLO。原core未披露gate算法、训练目标、hardware、precision、输入输出长度、batch/concurrency、endpoint、SLO，均为 Not Disclosed；Auto是继续既有路由，API仍是later this week。

实际读取 [Ch42](../../../../../books/part-05-inference-system/42-what-happens-during-inference.md)L235–270及收尾：L251预算进入request contract、改变decode路径/成本/deadline/质量分布；admission批准上限、runtime执行，固定预算仍为可预测延迟基线。L257–261要求benchmark绑定完整workload/SLO，不允许把脱离配置的倍数迁移为系统收益。[Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)L184–204已有monitor提议、scheduler在校准/budget/SLO下控制continue/verify/route/abstain，并保留误校准/额外调用及固定预算回退。相邻Ch43开篇实际区分Prefill的状态/计算工作，不是适应性思考门控owner。

**作者决定：仅报告，主owner线索 `INFER-REQUEST-LIFECYCLE`，Ch56仅交接。** 本次确有版本级条件行为增量，但没有足以修改当前预算权责、边际收益校准条件或具体调度机制的新证据。保留2x/2x对照而不写入长期正文，不是因名称缺位、已有成熟原则或无实验细节关闭准入。若以后披露新的gate/受控质量成本取舍，只重开Ch42预算段及必要Ch56交接。

## 方向二：逐基线安全反侧

Table1 not_unsafe越高越好。Thinking对GPT5不止厂商prose提及的harassment/hate/sexual下降：另含illicit/non-violent、violence、sexual/minors、illicit/violent、self-harm/intent、self-harm/instructions、emotional reliance下降。Instant对Oct3的sexual、violence、sexual/minors、mental health、emotional reliance下降；不能用对Aug15的改善替换基线。Table2 Thinking `.974→.967`，Table3 Thinking self-harm `.976→.936`，都是该grader/输入协议下的局部事实，不当全攻击安全保证。

困难生产离线集刻意选旧模型错误、长对话可能已有历史不良行为，不代表平均线上prevalence。线上A/B的低基率、小样本与宽误差不能抹除离线退步；Thinking emotional reliance离线下降而线上有高置信改善，同样是不同人口，不强行统一。原card不披露足以独立复算的逐项样本、原输出/所有误差数值；只能保存作者报告的方向及权限。风险类别和主要mitigation沿用既有addendum/GPT5，非本次首次发明。

实际读取 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)L187–215完整对象身份段、L468–505分布/样本假设、L553–582切片/相关性与不确定性、L3085–3100 Offline/Shadow/Canary/Online边界、L3158–3189 Release Gate，以及Evaluation/Observability交接；相邻Ch65开篇是集群调度，Ch67开篇明确质量标准由Evaluation定义。当前正文具体禁止 `candidate_overall_score >= baseline` 抵消局部高风险回归，区分absolute/relative/non-inferiority/improvement；离线不证明真实流量与低频风险，online也不自动优于offline。

**作者决定：仅报告，owner `PLATFORM-EVALUATION-SYSTEM`。** 新表是具体版本负证据，支持并实例化当前相对基线、关键安全切片和人口分账的论证，没有推翻该论证、识别新测量盲区或新增可执行评价机制。保留反证不意味着必须新增一段模型榜表；亦不称所有安全机制已有覆盖。若新原始配对数据/勘误显示当前gate条件有新失效路径，重开Ch66完整对象、分布及Release Gate三处，不拓展全card附件。

## 独立接点与停止

实际读到[Ohm THIRD](THIRD_INDEPENDENT_REVIEW.md)21:02:19 §3：其已独立读取Books治理、Ch42/56/66具体论点及Ch43/67交接，支持仅报告、拟共享差额0。作者本记录对照一致，最终采用两方向仅报告。无需Books写入请求或POST；若root发现具体新长期边界，仅给具体差额/位置并由root唯一写入。FIRST证据通过可复用，THIRD窄修/其余118普通题摘分层校准及14来源/六部分仍单独待独立，不能借此给DAY盖章。
