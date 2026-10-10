# 11253 独立必要 Source / 评分 / 具体 NC 复核

复核者 mar13_admission_review；本包仅 2026-03-14 Daily 补充 2026-03-13 北京时间自然日的 arXiv:2603.11253v1。准备者为 mar14_supplement。本次重读当前 AGENTS、Research / Report 合同、统一 Prompt、Sources 使用说明及 Daily / arXiv 范围、本日停点和相关 owner 路由。已有效的完整题摘与十项日级日期独核复用；Submitted 不作为公开日期，未据 v2 编号另计重要事件。不写 Report、Books、State 或共享 ledger，不授 POST / DAY。

## 实际原证范围

实际读 SUP_EVIDENCE_11253.md 及 SUP_NARROW_LAST_MANIFEST_RESULT.json 的本项记录：官方 exact-v1 URL https://arxiv.org/html/2603.11253v1，GET 200，417595 bytes，UTC 2026-10-10T02:05:48.563515Z，最终 URL 不变。直读 SUP_NECESSARY_11253.raw 的标题身份，及同原响应文本 SUP_NECESSARY_11253.txt 的 306–438（II 主结果、II.1–2）、712–852（III 限制、IV.1–3）、1803–1833（S1 标签验证）、3038–3288（S4 过滤方法与 Tables S4–S5）、3291–3378（Tables S6–S7）。这些是本次实际读取，不以作者包的全稿读取范围代替。未重建 II.3–4 的词义 / topic 分析、全部词表、图像、提示附件或代码；拟采用的隐私边界不依赖其因果解释。

## 支持与直接限定

- DDO 的自报 R/D 标签和 Reddit 高参与社区用户的代理标签不是统一秘密真值。DDO 将同 user/debate 的 arguments 汇成输入；Reddit 将同 user/subreddit 的评论汇成输入。不能把 text 视为统一单条暴露粒度，也不能从两个受选人口推出全部普通用户的发生率。
- General 的分类定义及 held-out 用户过滤保留了较窄的非显式内容切片，但政治检测本身不完美：最佳 macro F1 在 DDO 约 .800、Reddit 约 .673。过滤阴性不证明所有政治语义 cue 已消失。GPT Reddit general 的 .606 单 text / .799 最大置信聚合只属于该人口与配置。
- Tables S6–S7 的异质性真实存在：DDO GPT general 单 text .608、max-confidence .670；Reddit Llama 单 text .528、majority .502、weighted .646、max-confidence .745。不能宣称所有模型或所有聚合都有收益。verbal 1–5 confidence 不是已校准概率，筛选后高分也不认证真实性。
- S1 的五作者、50 个 title+评论样本验证与社区代理标签的一致性（平均 .85、多数 .92、κ .576），不是独立核验每人的真实隐秘信念。主文明确训练数据未披露、English/US 和自选参与者限制；不能据相关推断证明个体 memorization 或唯一 causal feature。
- GPT zero-shot、Llama 格式 few-shot 的配置不同，JSON 有效率不足 100%；格式失败不是安全拒答。逐输入查询、过滤训练、聚合、人审与敏感记录治理都有成本，不补造并发、SLO 或生产费用。

Source 判定：上述受限经验边界 PASS；普遍政治属性识别、真实秘密证明、唯一因果或训练记忆归因不通过。仅评审已发表的聚合隐私证据，不开展实际个人政治画像或定向影响。

## 实际 owner 与 NC

实际顺读 Ch72（PLATFORM-SECURITY）31–67、386–436、529–555 完整相关局部及邻接；Ch71/73 的已有效职责入口复用。并非因为同主题或同 family 判 NC：

1. Ch72 46–48 已明确单条看似无害的跨步碎片对联合 observer 累计提高秘密 posterior，以及 sink trust、预算、校准和任务可用性边界。
2. 390–395 已将多条相关 embedding / 回答 / 日志 / 查询的联合 view、相关结构、查询预算和独立 posterior 风险评估列入 privacy accountant；不能以逐记录保证签发组合零风险。
3. 400–402 已将 attribute / entity / edge 回到具体 post / observation，说明 selected support 不穷尽冗余 cue；后续完整 observable-channel 局部保留 observer 权限、非 DP 保证、敏感 trace 与复测费用。
4. 535–536 的视觉隐私段已明确公开可见性、推断 / 虚构与真实身份匹配分账；低可见性不证明 memorization，输出形态或意愿不证明 secret truth。该测量纪律同样限制本稿的自报 / 社区代理标签结论。

本稿的受限设计含义——一般内容或单条 clean 标签不能证明联合观察无隐私风险，统计推断不等于真实秘密或训练记忆——已有具体长期论点承载。不存在已证的新控制接口或必需条件缺口；不将新实验冒称已写入或已吸收，也不补政治领域泛化治理段。**NC / Books 新写 0 PASS**，不是跨日报去重，也不是 EX 或最低分关闭。

## 独立评分与处置

**Design 2 + Reach 1 + Durability 2 = 5，PASS。** 增量对象是非显式在线文本与跨记录联合观察下的受限隐私边界验证；不把成熟聚合方法或一般推断原则计作新算法。影响主要在 observer inference 的审计切片，稳定的真值 / 人口 / 组合观察纪律值得保留。标准必要审阅完成，安全边界受影响部分定点核验完成；不因已有覆盖降低已经完成的审阅投入或缩去候选。结论为报告保留受限验证、已有覆盖、Books 0；无 PRE 写入要求，无实际 POST 或整日完成声明。
