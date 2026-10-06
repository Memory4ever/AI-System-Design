# 第十一批：余含糊线索的一次决定核心

仅02/18窗口；题摘与一次核心判断，不是必要审阅已完成或冻结候选。精确日期和当前撤回轻查尚未完成，不先计当窗候选。未读无关附件不等材料缺失。

| ID | 已读实际原文 | 原有约束→原文实际增量→选择 | 准入判断 |
| --- | --- | --- | --- |
| 14147 LaViDa-R1 | V3_BODY_2602.14147.txt:65–66题摘、107–162核心 | likelihood proxy给不同mask人口不同权重→互补mask使每token恰掩一次并将1/t改w=1，改变surrogate；answer-forcing改变零reward组人口→区分覆盖/方差与真实likelihood/onpolicy身份，非SFT/RL混合贡献。 | 拟准入2+2+2=6，目标/采样接口深入；ELBO等号不认证精确likelihood |
| 14370 attention tipping | V3_BODY_2602.14370.txt:40–42题摘、65–89核心 | 静态相关难决定何时切换→coarse dominant-pair显式自续token与basin dotproduct切换条件→核预测n*人口/真实projection，不采所有安全失效同因。 | 拟准入2+1+2=5，解释性条件深入 |
| 14452 WiSparse | V3_BODY_2602.14452.txt:50–60题摘、130–172核心 | activation幅度剪通道忽略output映射→weight-column norm可调指数、固定threshold且token-adaptive mask→改变selector质量/代价；evolutionary+greedy组合非新增本身。 | 拟准入2+1+2=5，标准必要评价 |
| 14468 LACONIC | V3_BODY_2602.14468.txt:65–66题摘、91–117/145–181核心 | 线性cost奖励已短响应更短→primal只罚超额，dual用signed mean-length且λ ceiling保护correct-long排序→区别average约束、tail目标与真实GRPO，非CMDP/adaptiveλ名字。 | 拟准入2+1+2=5，目标/理论深入；ideal exact maximizer非神经GRPO证书 |
| 14577 DriveFine | V3_BODY_2602.14577.txt:73–75题摘、121–174核心 | 生成后不能改unmask动作，直接alltoken loss改生成objective→复制末n块refiner、隔离共享/生成梯度并手动branch，anchor-relative reward纠偏→核收益与共享费用/实环境边界。 | 拟准入2+1+2=5，具体objective人口非MoE+RL配方 |
| 14606 selection governance | V3_BODY_2602.14606.txt:137–142题摘、290–450/490–507/607–625核心 | candidate/action authority分开已有合理原则→CEFL外置、filter/clamp/Pareto/diversity/lottery与commit-reveal串接，未新增受控机制或其成立条件；SRI是经验频率→不能仅称selection sovereignty升级成熟权限组合。 | 贡献关闭，不因缺普遍证明/金融领域/低可信 |
| 14777 self-awareness/realignment | V3_BODY_2602.14777.txt:52–53题摘、71–103核心 | 单checkpoint自报不能判断训练后行为→同模型misalign→same-domain realign并独立诱发behavior测量，自报随修复降但mini/nano仍较坏→区分动态诊断相关与认证修复。 | 拟准入2+1+2=5，安全测量条件深入，非selfreport足以oversight |
| 15028 privacy/context | V3_BODY_2602.15028.pdf.txt:6–34题摘、407–447/916–954核心 | 泄漏需对应observable use/transmit→本privacy实为PII计数/aggregate多选识别，理论是固定m/IID有限moment的attention分母稀释，无新执行/泄漏条件→不能把长ctx检索困难换privacy标签准入。 | 贡献关闭，留MCQ≠实际泄漏安全边界供独核，不否认数据集价值 |
| 14299 Moltbook | V3_BODY_2602.14299.txt:92–102完整当前题摘、108–115定义 | 惯性/互动强度非社会适应充分条件→新观察指标未新增可归因memory干预或执行机制→观测稳定不能混为shared-memory设计反证。 | 贡献关闭，日期未核不另追历史；HTML显示Aug24版本异常，不计当窗原文 |

root准入校准待核；本批只有明确potential才进入日期与必要审阅，不以8份可得HTML逐篇全附件。

## 定点日期身份/公开交集（author核，root待核）

各自`V3_DATACITE_2602.<ID>.json`的doi/url/title与v1字段绑定，Created公开登记上界不是Updated。逐项v1Submitted严格晚于Fri02/13T19Z且不晚于Mon02/16T19Z，按已独核官方公告规则得到最早Tue02/17T01Z；以Created秒bucket+1s为排除终点。每项推定`[2026-02-17T09:00+08,Created+1s+08)`完全落窗。不是邻ID/整段inventory推批；Available月份不用。九项此前在第9/10及本批完整题摘已读，若实际提前artifact家族信号仍需单独处置。

| ID | v1Submitted Z原值 | v1Updated Z原值（不作首公开） | Created Z原值 | Registered Z原值 |
| --- | --- | --- | --- | --- |
| 13840 | 2026-02-14T18:07:51Z | 2026-02-17T01:36:52Z | 2026-02-17T04:01:33.000Z | 2026-02-17T04:01:33.000Z |
| 14178 | 2026-02-15T15:07:19Z | 2026-02-17T01:58:49Z | 2026-02-17T04:09:32.000Z | 2026-02-17T04:09:33.000Z |
| 14445 | 2026-02-16T03:58:12Z | 2026-02-17T02:15:00Z | 2026-02-17T04:16:18.000Z | 2026-02-17T04:16:19.000Z |
| 14147 | 2026-02-15T13:52:45Z | 2026-02-17T01:56:32Z | 2026-02-17T04:08:46.000Z | 2026-02-17T04:08:47.000Z |
| 14370 | 2026-02-16T00:43:56Z | 2026-02-17T02:10:16Z | 2026-02-17T04:14:21.000Z | 2026-02-17T04:14:21.000Z |
| 14452 | 2026-02-16T04:18:36Z | 2026-02-17T02:15:22Z | 2026-02-17T04:16:29.000Z | 2026-02-17T04:16:30.000Z |
| 14468 | 2026-02-16T05:09:40Z | 2026-02-17T02:16:23Z | 2026-02-17T04:16:56.000Z | 2026-02-17T04:16:58.000Z |
| 14577 | 2026-02-16T09:13:52Z | 2026-02-17T02:23:12Z | 2026-02-17T04:19:55.000Z | 2026-02-17T04:19:55.000Z |
| 14777 | 2026-02-16T14:29:46Z | 2026-02-17T02:37:24Z | 2026-02-17T04:25:03.000Z | 2026-02-17T04:25:03.000Z |
| 13547 | 2026-02-14T01:41:17Z | 2026-02-17T01:16:05Z | 2026-02-17T03:54:11.000Z | 2026-02-17T03:54:12.000Z |
| 13697 | 2026-02-14T09:38:57Z | 2026-02-17T01:28:49Z | 2026-02-17T03:57:59.000Z | 2026-02-17T03:58:00.000Z |

当前官方abs已有限轻查30个本日明确potential（第五9、第六10、第9两potential、第10三potential及本批6），raw为`V3_CURRENT_ABS_<ID>.html`；withdraw/retract/erratum/corrigendum无命中，唯一correction命中14577只是题摘self-correction，经原頁101–150实际确认，无withdraw信号。不作全version差比或所有安全全文证书。
