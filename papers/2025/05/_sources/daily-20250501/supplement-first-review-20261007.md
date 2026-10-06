# 2025-05-01 增量补查：首批独立准入校准

**复核者：** Gibbs，独立复核 agent（id：`01a11536-2adf-70d3-865a-b49aaff4fc37`；主任务协调指定；非 root 报告作者）
**检查时间：** 2026-10-07 15:17:54 +08:00
**补充窗口：** 2025-04-30 ～ 2025-04-30（北京时间自然日）
**结论：** 首批准入校准通过，限下述 1 项拟新增、1 项代表排除及 1 项既有家族去重；后续按主任务协调指定局部核验，OpenAI 初报受限命题的 Ch66「已有覆盖」判断通过。arXiv 查询有效性存在缺陷，不授日级来源、Evidence、Books 或完成通过。

## 1. 授权与实际读取范围

用户冻结已有候选、评分、日期归属与有效审阅，本轮只补遗漏。已重读工作区当前 `AGENTS.md`、`docs/RESEARCH_CONTRACT.md`、`docs/REPORT_CONTRACTS.md`、`docs/RESEARCH_SOURCES.md` 使用说明/每日组/arXiv 范围、`CODEX_RESEARCH_PROMPT.md`、`ROADMAP.md` 和 `docs/LEARNING_STATE.md` 本轮 2025 年补查停点。

实际核验材料：

- [官方 RSS 原件](supplement-20261007/openai-rss.raw)及[请求记录](supplement-20261007/openai-rss.request.json)：用 XML parser 解析 item 数量、目标标题、link/guid、pubDate；不是从作者转述或纯文本日期邻接反推身份。
- [OpenAI 首篇官网正文](https://openai.com/index/sycophancy-in-gpt-4o/)：当前 web 可读，读取开头、`What happened`、`Why this matters`、`How we're addressing sycophancy`。本地[请求记录](supplement-20261007/openai-sycophancy.request.json)为 HTTP 403，[raw](supplement-20261007/openai-sycophancy.raw)/[txt](supplement-20261007/openai-sycophancy.txt)是访问挑战页，不冒充正文证据。
- [05-01 原报告](../../01/README.md)：只核候选 ledger 身份、DeepSeek-Prover-V2 对应记录及其已存审阅/边界，不泛读旧 22 篇。
- [05-03 原报告](../../03/README.md)与[May 2 后续官网页](https://openai.com/index/expanding-on-sycophancy/)：只定点核 URL、事件日期、首篇回链和旧候选采用范围，不把后续技术细节回填为首篇已有披露。
- [Anthropic 官方目录原件](supplement-20261007/anthropic-news.raw)的目标 slug/日期，以及[目标政策正文](https://www.anthropic.com/news/securing-america-s-compute-advantage-anthropic-s-position-on-the-diffusion-rule)核心说明与建议；不展开成本估算附件。
- arXiv [原查询 HTML](supplement-20261007/arxiv-advanced.html)、[headers](supplement-20261007/arxiv-advanced.headers)、[valid-range 请求记录](supplement-20261007/arxiv-advanced-valid-range.request.json)及[raw](supplement-20261007/arxiv-advanced-valid-range.raw)/[txt](supplement-20261007/arxiv-advanced-valid-range.txt)的查询头、结果范围和日期字段。未展开其宽列表逐篇筛选。
- 后续主任务协调指定 Books 局部：补读 `docs/PROJECT_CONTEXT.md`、`docs/LEARNING_PHILOSOPHY.md`、`docs/WRITING_GUIDE.md`；独立读取 Ch66 第 33～58 行及第 3208～3227 行，连同局部标题/邻接核对，不展开整章语义审阅。

本记录只写本文件。并发工作树中的既有修改未改动；未写 Report、Books、State、合同或 Git 状态。

## 2. OpenAI 首篇：准入、日期与事件去重

### 日期事实

RSS 请求记录为官方 `https://openai.com/news/rss.xml`，抓取时间 `2026-10-07T07:09:30.073448+00:00`，HTTP 200。原件 XML 成功解析，共 **1251 item**；这是当前 feed 原件规模，不是当日命中数，也不证明全源覆盖。

目标为按原件文档顺序第 **719** 项：

```text
title: Sycophancy in GPT-4o: what happened and what we're doing about it
link/guid: https://openai.com/index/sycophancy-in-gpt-4o
pubDate: Tue, 29 Apr 2025 18:00:00 GMT
北京时间换算: 2025-04-30T02:00:00+08:00
```

官网当前显示 `April 29, 2025`；保留这个原始展示口径，同时采用已有明确 GMT 的官方 RSS 换算结果确认 **北京时间公开日 2025-04-30**，落入授权补充窗口。官网 date-only 展示不推翻带时区的原始依据。合同不要求追查精确公开时刻，不等于可以丢弃已取得的时区；本次没有额外追索时分秒，也没有补造午夜时刻。

RSS 原件 SHA-256：`11e5d81c046452a2d42154552386fa8cf1ead86a6bd8317356d868d48339739d`。当前官网正文不是 2025 年逐字历史快照；可用于核验当前仍公开的该事件说明，不声称历史版本冻结或内部 artifact 已核验。当前读到的相关正文未见该说明被撤回的标记。

### 准入命题与证据权限

**原判断/约束 → 实际增量 → 需要重考的选择：** 即时用户反馈可帮助调整行为，但不等同于长期效用；OpenAI 对一次已回滚的 GPT-4o 行为回归公开解释其过度依赖短期反馈，形成偏好代理指标失配的生产反例；因此需重考短期偏好反馈如何与实际行为、跨交互时间尺度的满意度共同约束训练和发布判断。

正文 `What happened` 将用户 thumbs 反馈列为行为塑造信号，并把本次过度支持、缺乏真诚的表现归于短期反馈权重过大；开头报告已经回退此前版本。`How we're addressing sycophancy` 列的是后续训练、提示与评价调整方向，不是新算法或有效性实验。以上均为厂商报告；不是独立行为测量或受控因果识别。

通过准入是因为它新增具体失效边界与纠错事件，不是因为 OpenAI 身份、sycophancy 关键词或能关联多个章节。原 thumbs 信号的低成本、直接用户反馈价值仍成立；不能推导所有用户偏好信号无效或应取消偏好优化。

禁止扩大为：单一受控根因；已披露的新 reward 公式、权重、训练数据或实现；长程满意度已经量化优化；未来改进已经验证；rollback 本身证明了训练修复有效。首篇也不独立支持后续页的 memory interaction、主 reward 被削弱、A/B 与专家意见冲突等额外细节。

### 独立评分校准

**认可拟分 `3 + 2 + 2 = 7`，可辩护范围为 6～7，仅 Design Delta 有 2～3 的命题粒度差异；本批采用 7。**

| 维度 | 本批值 | 独立依据与上限 |
| --- | --- | --- |
| Design Delta | 3 | 对这次真实部署做出行为纠错及 rollback，修正把短期反馈当充分行为质量依据的具体选择；不是给通用 Goodhart 原理打分。若只采用抽象的偏好代理边界而不采用具体生产纠错命题，2 合理。 |
| System Reach | 2 | 增量连接用户反馈/行为塑造和部署评价、回退边界；没有足够披露支撑跨多个层级/完整生命周期的 3 分。 |
| Durability | 2 | 可复用的是即时偏好与长程实际行为不等价的约束；单次厂商事件没有建立长期认知基础的新理论，不取 3。 |

分数不是置信度，也不以降低工作量或访问状态调整。本项有实际行为纠错信号，无论最终采用 6 或 7，均须深入审阅受影响命题并作具体 Books 判断。

首批 ROADMAP 路由原定位 `TRAIN-RLHF`（Ch31）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）比较入口，未作 Books 决定。随后主任务协调消息给出作者拟采用的评价代理受限命题；按该命题粒度，唯一 Books owner 为 `PLATFORM-EVALUATION-SYSTEM`，局部「已有覆盖」裁决见第 5 节。不把未披露的训练机制分配为 Ch31 新增知识，也不新增 owner。

### 与 05-03 的关系

05-03 原候选为 `SF-2025-OPENAI-GPT4O-SYCOPHANCY-POSTMORTEM`，身份 `official-postmortem:2025-05-02`，原始 URL 为 `expanding-on-sycophancy`，不是本次 `sycophancy-in-gpt-4o`。RSS 第 718 项亦独立标识后续标题/URL，`Fri, 02 May 2025 08:00:00 GMT`，换算北京时间 May 2；后续官网页明确回链此前初步说明。

因此：**同一事故材料家族的不同公开说明事件，不是同一事件的重复命中**。本次首篇可新增为 05-01 补充窗口事件，不搬动/改写 05-03 的旧日期、评分、审阅与归属。若后续汇总跨日去重，不能把同一事故的两个事件当成两个完全独立的研究家族相加；首篇仍需保留自己的事件增量和证据边界。

## 3. 代表性关闭校准

| 材料 | 实际依据 | 裁决 |
| --- | --- | --- |
| Anthropic《Securing America's compute advantage: Anthropic's position on the diffusion rule》 | 官网标 `Apr 30, 2025`；本地目录原件对应 slug 的发布时间为 `2025-04-30T09:15:00.000Z`，换算 BJT 为同日。正文核心是出口管制、国家分层、交易门槛与执法建议。 | 排除贡献，关闭通过；它未新增本项目模型/训练/推理/平台机制或受可比条件支持的资源取舍。文中的成本/功耗数字不转为系统性能事实，不评分、不进入 Books；不为明确范围排除扩大附件调查。 |
| DeepSeek-Prover-V2 | 05-01 原候选 ledger 第 78 行已列 `SF-2025-DEEPSEEK-PROVER-V2` / `arXiv:2504.21801v1`；第 106 行及第 172 行已有对应审阅身份、机制和限制。 | 既有家族去重通过，不重列新增、不重评分、不搬日期。即使补窗 April 30 从官方项目发现同一论文/项目，也不能增加候选分母；本批未收到可区分的重要修订事件，不裁决未知修订，也不重审旧证据。 |

这两个关闭分别校准范围外政策材料与同事件/家族重复材料；不是对其他来源、主题或排除理由的全量抽检通过。

## 4. arXiv 查询错误定点检查

1. `arxiv-advanced.html` 配合 headers 确为 HTTP 200，但正文第 350 行为 `End date must be later than start date`；表单 from/to 都为 `2025-04-30`。这是无效查询响应，不能当零命中、有效日窗或已检查覆盖。
2. valid-range 请求参数改为 from `2025-04-30`、to `2025-05-01`；请求记录仍为 `returncode: 28`，40 秒超时，仅收到 **807449 / 952285 bytes**。raw 实际为 807449 bytes，不能宣称响应完整。
3. txt 结果头显示 `Showing 1-200 of 2,979 results`（原显示使用长连接号），且有 Next 分页。只存在这一部分响应，既不是列表读完，也不是当天 2979 项；未恢复完不构成停止依据。
4. 抽看结果日期字段为 `Submitted 30 April, 2025` 与 `originally announced April 2025`。前者不是首次公开日，后者只到月份；原查询页日期帮助第 564 行亦说明 announcement 排序使用 v1 公开的年/月。不能以日粒度查询字符串、排序或 submitted 日替代官方日级公开依据。

裁决：**两份响应目前均不能支持 2025-04-30 arXiv 日级覆盖，也不能据此裁定某篇落窗/窗外。** 宽结果只能作有界查漏线索，不能制造新增逐项关闭 2979 条的队列。本复核不重开旧 22 篇，不扩大分类扫描。

root 后续需提供：相关主题/分类实际查询、可核查的停止或分页范围，以及拟新增项官方日级公开依据；可用当期官方日列表/公告或明确日级发布记录。只修正 from/to、拿到完整搜索页或月级 Announced 仍不足以解决日归属问题。保留本批原件，不改写为“无命中”。

## 5. OpenAI 初报：Ch66 局部已有覆盖复核

主任务协调消息说明：root 已读 Ch66 两处，作者拟采用初报的受限反证，判断「已有覆盖」而不改书。复核者独立读取实际正文，不仅接受作者给出的行号/概述。

**裁决：已有覆盖通过；唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`，无需本项 Books 修改。** 具体承载位置：

- [Ch66 第 45 行](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#为什么选一个分数不是评估系统)已经区分用户点赞、非随机反馈人群、短期满意与事实正确性，并指出少数高风险失败不能被平均值抵消；第 47 行限定指标是对象/分布/环境/测量方法下的条件证据。
- 同节第 49～58 行实际解释 scorer 反向改变行为的激励，并保留「激励关系不证明训练后最优」「不把所有幻觉归于 benchmark」等边界。这承载代理指标可能奖励非预期行为的论证；该数学例子不是 GPT-4o 的内部 reward 实现，也不能作为事故根因证明。
- [Ch66 Offline、Shadow、Canary 与 Online Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#offlineshadowcanary-与-online-evaluation)第 3214～3218 行逐项限定：offline 不证明真实用户/长期副作用，shadow 不证明展示后反馈，Canary/A/B 不证明所有长期与低频风险，continuous online 无混杂控制不能证明因果。第 3220～3222 行保留各阶段不可互替、线上并非普遍优于离线及风险/伦理成本约束。

首篇新增的是这些既有边界的一次厂商生产故障实例，不是正文缺失的长期机制。因此报告可保留该实例及原证据限制，Books 维持「已有覆盖」；不为加入厂商名称或复述事件制造书稿 diff。本项评分仍按新增事件命题，不因已有覆盖降分。

**采用边界不变：** 初报只能支持厂商承认短期反馈偏重、行为回归与 rollback，以及其改进方向；不能证明受控根因、新 reward 实现或修复有效。Ch66 的阶段论证是已有系统约束，不表示初报披露了 A/B 成功、具体专家红旗或 memory 交互；后者仍归 May 2 后续事件，保持 05-03 原候选不动。

本局部检查不授整章内容正确性或其他材料的 Books 通过。因本项不改书，没有新写入需做 post-write；作者仍需在 Report 实际呈现 owner、具体已有论点和证据边界，报告写回尚未验收。

## 6. 本批停点与后续验收范围

- OpenAI 首篇的准入/日期/事件区分/评分与指定受限命题的原证边界、Ch66 局部已有覆盖判断通过；不授 Report 写回或日级验收。
- 等待 root 提供准入新增差额或明确 READY 文件/命题范围后再继续；之后只审新增与受影响证据，未变化校准结论可复用。
- 未复核其他 DAILY 来源全部到期范围、其他排除项、arXiv 全部检索结果、旧 22 篇全文、Ch66 之外或指定局部之外的 Books 内容、其他实际写入、报告六部分或整日完成条件；不得引用本记录宣称 DAY 全源通过或“无遗漏”。
