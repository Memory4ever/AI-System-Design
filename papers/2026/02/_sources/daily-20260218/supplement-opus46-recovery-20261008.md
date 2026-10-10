# Opus4.6必要日期恢复：有限失败记录

身份：Anthropic Claude Opus4.6 HLE with tools更正。官方current card URL https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd.pdf；官方news https://www.anthropic.com/news/claude-opus-4-6 。

本轮可见索引changelog提示February17：HLE with tools 53.1→53.0，改进作弊检测标出先前遗漏3项；news同样修正脚注明确February23。相互冲突，未确认为Feb17重要修订事件。原响应保留在supplement-official-west-20261008.json、supplement-date-recovery-20261008.json等。

必要PDF获取：web返回400；urllib访问403。一次25秒curl仅收到约2.7MB，后一次60秒有限恢复收到约5.3MB仍不完整，pypdf报告EOF marker not found，未得到可核完整card/changelog正文。不得把失败或索引全文片段记为已读必要PDF，也不继续全附件/修订历史循环。

终态：必要日期冲突和原件访问受阻，独立外部保留；不记新增确定当窗候选、不评分、不进Books、不作性能或完整coverage保证。重开只需绑定该更正的官方当日card artifact，或官方明确说明Feb17与Feb23对应不同事件及其原始版本。当前card Updated与搜索Published标签不能解决首公开日期。

