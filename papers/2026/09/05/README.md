# Daily Research — 2026-09-05

**规范：** V3
**窗口：** 2026-09-04T09:00:00+08:00 ～ 2026-09-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T11:32:46+08:00

## 1. 结论

按本次认可的准入尺度，三个已确认本窗材料家族中保留两个：Agent 工具的权限与生命周期重要修订、分布式权重更新示例的正确性修订。FLT campaign本轮排除：其规模案例没有隔离改变本项目长期机制的新结论，AI for Science也不在当前范围；旧证据留在原始记录，不进入本轮候选。arXiv 本窗没有计划内公告批次，不能把 Friday Sep04 的列表重新计算成周末新论文。

两项受影响保证已有精确代码证据与独立核查，本轮对读实际Books落点后保留：Kimi的长期原则已有覆盖；checkpoint-engine的确定性分片前提已存在于Checkpoint章节，不重复追加。新增厂商入口已补查；MiMo与MiniMax日期恢复后可排除窗外旧文。Google两篇首次公开日期及浑元目录限制已隔离为不支持当窗候选、Books或无遗漏断言的终态保留项；本次正式文本与新增来源已通过独立复核。

## 2. 来源覆盖

本轮入口、分页停止位置、原始字段与限制见新来源与证据记录。已保存的原始材料只作为内容证据，不复用旧候选或评分。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 当前 [Research index](https://openai.com/research/index/) 最近 Sep03，按日期检查到 Jul15；RSS 本轮403，以可达研究列表交叉原始1169条XML。范围限公开入口，不声称覆盖内部发布 | 已检查 | 无 |
| SRC-ANTHROPIC | 当前 [Research](https://www.anthropic.com/research) 列表 Sep04 FLT、其次Aug28；官方列表实体提供精确 publishedOn | 已检查 | 无 |
| SRC-GOOGLE-AI | [DeepMind Blog](https://deepmind.google/blog/)四个September条目逐个核对日期；DeepMind publications最新Sep01、Research Blog最新Sep03；年度目录16页236身份，经原始出版日期、实际公开观察与贡献筛选缩小到两项。详见定点核查 | 受阻 | 116安全prompt hardening、118 HCRG code migration的官方页面仅标2026，无原论文链接或日期；最早已取得公开观察在本窗内，不能确定首发是否本窗 |
| SRC-META-AI | [官方publication](https://ai.meta.com/results/?content_types%5B0%5D=publication)结果页1、2，第二页已到May；Sep06新卡Text-Audiobox对应Sep04已公告arXiv家族，不重复准入；卡片上架时刻不明不改变首次公开归属 | 已检查 | 无 |
| SRC-QWEN | [英中官方API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)各37项，完整解析extra.date；最新Sep03 10:00+08，双语按同一材料去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 当前官网研究入口与[官方updates](https://api-docs.deepseek.com/zh-cn/updates/)，最新Aug21、随后Aug13与Jul31；常驻模型链接不作为新事件 | 已检查 | 无 |
| SRC-MOONSHOT | 两个官方Blog、[43个公开仓库](https://api.github.com/orgs/MoonshotAI/repos?per_page=100&type=public&sort=pushed&direction=desc&page=1)release首页逐一检查：38空、5个非空页均跨到窗口之前。0.41.0为唯一本窗release；另由checkpoint-engine活动触发两个merge核查；release、merge与pushed_at不等同 | 已检查 | 无 |
| SRC-ARXIV | 当前四主类列表最近Friday Sep04；[官方日程](https://info.arxiv.org/help/availability.html)周五、周六美东不公告，含new/cross/replacement等。这里只确认公告流程范围，不宣称全网无论文 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)下方“全部”列表；用户截图九行最上Aug28，早于本窗；自动正文提取空响应，浏览器连续超时 | 受阻 | 可见九行不是完整目录；需本窗条目链接或完整最新列表，不能按空响应判零 |
| SRC-ZAI | [研究时间列表](https://www.zhipuai.cn/zh/research)最新Aug26，随后Aug14/Jun16并跨到2025；见共享检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)/Blog/Publications当前首屏依日期到Aug05/Jul06以下；未命中本窗，入口和停止点见共享检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [官方博客](https://ernie.baidu.com/blog/zh/)首页最新May09，随后Apr30/Feb09，已越过本窗起点 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)区最新Jun29；Blog相同标题/route在官方frontmatter和iframe中恢复为六月或更早；MiMo Code0.1.14的独立release归Sep03 | 已检查 | 无 |
| SRC-MINIMAX | [中英研究列表](https://www.minimax.io/blog)最新Aug13；官方Markdown技术目录Agent Team为May13，读取外壳问题已恢复；见共享检查和原始下载 | 已检查 | 无 |

Google 新增 CSIG 的原始 DOI 出版日为 Aug11，不能因目录由235变236就算新论文。Meta 的 Sep06 卡片对应 arXiv:2609.03992v1，首次公告在 Sep04 08:00+08，由该日报处理。本窗未出现其他周级来源的具体触发，FLT artifact 属于同一材料的证据链。

## 3. 候选与判断

评分按 Design Delta + System Reach + Durability。修订的多个 PR 不增加家族数。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.41.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.41.0) | 2026-09-04T11:01:07Z | important_revision；与0.40同家族，不重复评分；实际改变危险命令保护、后台问题和恢复授权，Deep override | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) 的状态生命周期及恢复后的继续授权 |
| [checkpoint-engine #103 / #105](https://github.com/MoonshotAI/checkpoint-engine/pull/103) | 2026-09-04T09:59:29Z | 本窗两个merge归同一正确性修订家族；表列首个merge，另一个精确时间见正文；2 + 2 + 1 = 5，对受影响正确性保证Deep override；范围仅官方update example | 深入完成 | 整合：TRAIN-CHECKPOINT，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md) 的事务提交前提与单文件发布边界 |

## 4. 证据与知识整合

### [Kimi Code 0.41.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.41.0)

家族：SF-2026-MOONSHOT-KIMI-CODE-0-40。本次release commit为 `95478e8c7ba248fd2470d5bb151555ec7fedd19d`，不继承0.40的审阅结果。深入范围限三个真实行为变化；模式重命名和UI修复不作为重要性证据。

- `dangerous-command-ask` 在auto模式返回undefined，跳过这个内置guard；不等于所有policy无条件允许，也不证明外部隔离消失。
- detached问题不再绑定原turn，因此可跨turn等待；显式abort/dismiss及agent/session生命周期仍适用。直接回答内联上限为16,000 bytes，超过时回到文件或preview路径，不能写成所有回答都直接投递。
- 恢复subagent先验证持久元数据、对象类型、parent owner和运行状态。重建后仅当profile没有pinned permission mode时才采用调用者当前mode；固定profile是明确例外。

这些结论来自具体PR与固定源码，独立核查位置见新复核记录，不是本轮运行测试或生产安全证明。长任务需要脱离短turn，但更长的状态寿命会增加过期权限和悬挂任务风险；恢复内部状态不能代替继续授权，也不自动提供exactly-once。

**Books：已有覆盖。** AGENT-PLATFORM 的“Serving结束不等于Agent任务结束”区分KV、Context、AgentRun和Memory；“执行连续性”要求核验外部状态、副作用以及Policy plane的继续授权。AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md) 已区分proposal、authorization、policy与approval。具体auto选择、pinned例外与16,000 bytes上限属于此版本事实，保留日报即可，不改成跨产品规则。

### [checkpoint-engine #103 / #105](https://github.com/MoonshotAI/checkpoint-engine/pull/103)

家族：SF-2026-MOONSHOT-CHECKPOINT-ENGINE。#103在 `2026-09-04T09:59:29Z` 合入 `fee5a53e673d5865dd8770347a22fc3eee541158`；#105在 `2026-09-04T14:06:24Z` 合入 `03126b8130e79e44f1869c7ff9e809300fb12cb9`，两个事件均落窗并已审阅。#103首次讨论在Aug24，当前latest release仍是Jul04的v0.4.2。

逐rank切分本地文件列表看似简单，但不同枚举顺序会产生重复和遗漏。#103先排序再切片，其正反序枚举测试针对相同文件集合；不能推导各节点文件集合或内容一致。#105在目标同目录写临时metadata、flush和fsync文件后replace，避免单文件截断可见；没有目录fsync、全体weights联合事务、多writer协调或远端文件系统保证。PR文字中“更清晰load错误”没有对应实际patch，本轮拒绝采用。

**Books：整合。** Ch35原先已有共同step、manifest验证和原子提交，但“each rank writes owned shards”未展开ownership如何在枚举差异下失效。现已在“Checkpoint应像事务一样提交”中用两个rank/四个文件的例子补足共同集合、稳定排序与完整性验证的关系，并收窄单文件发布的保证；自检与primary入口同步。知识owner仍为TRAIN-CHECKPOINT，没有新增独立框架小节。代码只作静态核验，未执行作者测试。

## 5. 缺口与下一步

外部日期/入口限制如下；它们已隔离为本窗终态保留项，不支持当窗候选、Books或无遗漏断言。共用材料只请求一次，见共享来源记录：

- 浑元Research“全部”完整列表或本窗新增条目的官方链接/页面导出。现有用户截图只覆盖九条窗外记录；自动提取和浏览器超时，不据此假定完整目录无更新。

- [Securing Multi-Agent Systems: An Empirical Analysis of Security Prompt Hardening and Residual Risks](https://research.google/pubs/securing-multi-agent-systems-an-empirical-analysis-of-security-prompt-hardening-and-residual-risks/)：具名prompt-hardening对照与多轮残余风险值得候选判断，但官方只有年份，无下载或稳定论文标识。
- [Beyond Vector Similarity: Hierarchical Context-Aware Graph RAG vs Standard RAG in Enterprise Code Migration](https://research.google/pubs/beyond-vector-similarity-hierarchical-context-aware-graph-rag-vs-standard-rag-in-enterprise-code-migration/)：依赖图上下文与结构质量/复杂度取舍有具体增量，但同样无法确定首次公开日。

已检查官方详情、Crossref、DataCite及精确标题/作者检索，未取得匹配日期；Scholar、arXiv API和历史快照失败不作无结果证据。需要其中任一项的带日期原始发表记录，或证明在Sep04 09:00+08以前已公开的同身份记录；材料到达时只定点重开对应身份和归属判断。没有用GCS对象创建时间冒充公开日期，也没有把两项未经归属和正文审阅的内容计入两个正式候选或写入Books。具体路径见来源核查。

两项候选的证据与Books落点、新增来源处理和本次正式文本均已通过独立复核；剩余工作仅为上述外部材料恢复。本轮排除FLT不删除既有原始研究证据。

## 6. 复核

复核者：`/root/screen_sep01`；本次独立复核。
结论：通过

已确认候选的证据与Books判断、来源处理和独立复核均完成；外部日期/目录限制有精确重开条件且未被用作正面证据，因此本窗完整闭环。

本次重新筛选保留Kimi和checkpoint-engine，复用既有独立精确证据中固定源码、pinned例外、16,000 bytes与example边界的核查。主智能体及本次独立复核者对读Ch35事务提交和Ch84继续授权的实际段落，内容仍承载上述窄命题，无重复Books追加。旧记录包含FLT的准入意见及旧八来源范围，不作为本轮整日验收；当前14来源、FLT排除、外部缺口及正式文本已经独立确认。
