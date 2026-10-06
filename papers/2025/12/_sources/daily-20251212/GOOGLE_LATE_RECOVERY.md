# 12/12 Google晚恢复准入请求

2026-10-02T19:34:00+08:00。13日独立检查发现精确发布两篇落12窗，故只重开本日Google受影响项；先前作者普通0不再包含这次晚恢复。

原HTML实际HTTP200，两篇`NewsArticle.datePublished=2025-12-11T17:00:00+00:00`，BJT12/12 01:00；Interactions modified17:12:20.625361Z，DeepResearch modified17:09:48.161070Z。article:published_time只有12/11日标签，不如JSONLD精度，不补造时刻。

1. [Interactions API](https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api/)完整核心已读：可选server-side state、typed/interleaved history、background execution和remote MCP，旧generateContent适合stateless且继续生产支持。旧request-response不能承载长循环所有状态→发布API将history和长运行责任可交服务端→需要区分可检索interaction对象与业务任务完成/取消/重试合同。具体接口增量潜在准入，不以新API名或宣称cache降本入选。当前文档会变，初始博客只支持所披露职责，不推幂等/持久/授权/retention已实现；未运行API。请root校准owner为Ch83协议接口还是Ch84平台state，作者继续实际对读。
2. [Deep Research / DeepSearchQA](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/)完整核心已读：900 causal-chain任务/17field，要求exhaustive answer sets，将单答案成功改为precision与recall共同验收；200prompt上的pass8/pass1不是相同预算单跑质量。可能改变research agent完整性评价，不能仅“新benchmark”关闭，也不能用宣传排名准入。主模型/训练细节未披露，不新增RL算法。需技术稿精确版本/评价条件与Ch66对读；暂不采用性能数值。未来MCP/图表/Vertex能力不写成当时已实现。

## 必要证据与Books提案

2026-10-02T19:39:00+08:00。两家族各2+2+2=6；API标准，DeepSearchQA因已确认评价知识缺口深入必要内容，分数不变。API完整核心不含幂等/持久/取消回滚保证，不跑API、不采cache提速。实际Ch84 52–96的四对象、typed Item/Turn、服务端回读及terminal evidence充分承载职责分离；Ch83 100–108五轴/245–257远端对象映射作相邻交接，Ch82执行与委派分工不变。因此拟已有覆盖`AGENT-PLATFORM`，No Change，不是仅目录主题相似。

DeepSearchQA原技术稿16页首页12/11，实际读§1–3、§4关键评价/失败、§5限制；精确事实和不采用性能边界同步README。只采用final answer-set测量协议，不声称当前PDF文件已历史字节冻结，不采用后来榜单。§3集合关系、§2三人独立gold验证/时锚、§5无trajectory和web drift足以支持下述最小命题。Ch66 910–912已有必要信息→可替代chunk映射/partial vscomplete，不等final entity-set/多余答案；Ch65资源公平、Ch67观测分工不接管scorer。

目标唯一owner `PLATFORM-EVALUATION-SYSTEM`，拟在Ch66 RAG前两段后、exposure/copy baseline之前局部补入，不覆盖已有段：

> 取得全部必要信息还不等于交付完整答案。输出合同要求列出所有实体时，应将归一化后的答案集合与固定gold集合比较，分别记录遗漏、额外项、完全无正确项和严格集合相等；平均F1诊断部分质量，不能替代“完整且无多余项”的任务验收。实体去重、同义匹配和截止时刻是scorer合同的一部分，retrieval recall也不能自行证明最终答案已交付。
>
> 这类验收增加gold穷尽、实体匹配和网页变化复核成本，LLM语义judge仍需独立抽检；仅输出集合不能解释可靠过程或排除幸运。单一确定答案任务保留低成本exact-match基线；gold无法稳定穷尽时，收窄范围/截止时刻或保留Unknown，不从高recall宣称搜索空间已穷尽。DeepSearchQA只为这条测量取舍提供受限原始案例，不授其排行、预算优势或生产保证。

原始支持位置：技术稿§2 Quality Verification、§3.1–3.2集合/语义judge、§4 Metric Divergence、§5.1。这是从协议推得的工程论证，不新增未披露stop算法。准入校准、共享Books写入/POST由root协调，作者不冒称落实。其他有效source/133题摘层保持，不全日重跑。
## 实际Books落实补充

2026-10-02T20:25:31+08:00作者再次实际对读Ch66新段/前后及来源末注：root已在RAG gold审计与exposure诊断之间写入两自然段，当前918/920行，稳定绑定`SF-2025-GOOGLE-DEEPSEARCHQA`。采用规范化最终答案集合、逐题P/R/F1与strict equality区分、gold与matcher维护及仅结果评价的边界，不搬排名/性能数。Popper真实非写入者POST于2026-10-02T20:24:04+08:00通过，实际source→两段→前后/Ch65/67范围见[ROOT_ADMISSION_REVIEW](./ROOT_ADMISSION_REVIEW.md)。不是作者独立验收，也不授日级通过。上方保留原始发现/提案过程，不再把整合写成尚未落盘。
