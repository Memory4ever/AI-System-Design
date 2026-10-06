# 2025-10-08 作者安全停点

仅本日窗口`[2025-10-07T09:00:00+08:00,2025-10-08T09:00:00+08:00)`。作者Mill，不是独立验收。最新：Peirce FINAL §6已实际窄修写后DAY通过；作者据此同步日报完成/§6通过，普通研究/独立复核/Books待写0。下方交付段的“待窄复查”为先前作者快照，由本句与CURRENT_STOP替代；保留项权限不变，root写后接口校验仍独立执行。

## 定点恢复实读

实际请求/时间/返回原件见[recovery_manifest](recovery_manifest.json)，不是制造的执行收据。

- DeepSeek：[原入口](https://www.deepseek.com/news/)及[原件](deepseek_news.raw)。实际读可见5动态与10研究条目日期/标题，研究索引本窗相邻为2025-05-14 Insights into DeepSeek-V3与2025-10-21 DeepSeek-OCR，动态相邻09-29 V3.2-Exp与12-01 V3.2。当前列表未显示10-07/08事件。“查看全部”无独立href，不称全历史完备；停止可见列表，不读全年正文。
- Z.ai：[本日own bundle](zai_page_bundle.js)中LoadMore把`page`写入URLSearchParams并router.push；实际[page2](https://www.zhipuai.cn/zh/research?page=2)和[原件](zai_page2.raw)有18累计条目、末项2025-12-07 GLM-4.6V、“没有更多”。已解决普通分页恢复，仍缺2025-10历史段，不把首屏15条当末页，也不拿release notes代论文索引。
- Seed：[本日bundle](seed_bundle.js)与官方接口；真实`article_type=1&publish_year=2025&count=20&order_desc=false&page_token=0/20/40/60/80`，请求头`x-tt-locale: US`。原件[0](seed_locale_pub0.json)、[20](seed_locale_pub20.json)、[40](seed_locale_pub40.json)、[60](seed_locale_pub60.json)、[80](seed_locale_pub80.json)。实际只浏览日期/标题定位本窗，前四has_more=true，末页false/next空，total94；响应条目19/15/19/19/13与total字段不直接相等，不制造“94篇均审”分母。末页相邻09-22 MEF/ByteWrist与10-09 Function Tokens，后者原PublishDate1759939200000（UTC10-08 16:00）为目录日期值，不冒称首次公开瞬间；不属本日候选，未读其摘要。本日论文列表缺失的普通问题已修复，年度题摘没有转队列。
- Google pubs：[修正主题入口](https://research.google/pubs/?category=2025&search=language%20model)及[原件](google_pubs_2025_llm.raw)，实际2025结果1–15/37。旧`year=2025`未生效；修正后仍只有年/会议而非本窗first-public时刻。停止首15标题查漏线索，不读全年37项/676库存；没有把整页内嵌摘要视为已完成初筛。Blog原历史两页独立处理，不能填pubs缺口。

## FIRST反馈落实

实际读[Peirce FIRST](FIRST_INDEPENDENT_REVIEW.md)并保留其范围。作者校准后读回发布HTML的How it works/How we approached safety，和[必要原文存档](necessary_core_links.json)当前card物理p4–5全部安全/限制段。必要安全反侧独立核查已有效，不重读全37页OpenAI PDF。

Gemini最小采用命题为当前官方对该发布产品的控制分工说明，6分不变；注入、误解、不可逆误动作/泄露、敏感输出与不可绕过确认均留在报告。current updated2/card、2026修改HTML、新版Gemini3.x文档不能证明不可变2025API，安全服务不能等同完备reference monitor或fail-closed保证。无安全效果/跨harness性能采用。

实际读owner [Ch72 sensor/authority分层](../../../../../books/part-06-ai-infrastructure/72-security.md#learned-security-sensor-与-reference-monitor-必须分层)以及邻接[Ch78 side-effect控制](../../../../../books/part-07-agent/78-tool-calling.md#side-effect-class-决定控制)：现有正文已区分风险建议、policy解释、独立gate执行，以及high-impact approval/idempotency/scope。发布实例没有提供改变该链的可验证长期差额，作者仅报告/No Change，0提案、0写入；不是以覆盖主题排除候选。

OpenAI仅关闭Oct7主发布core新增贡献，不把Oct1七case页当整PDFfirst-public，不称同事件重复/整PDF已审。必要Russian与Stop News反侧命题有界复用；当前PDF窗后mtime不是重要修订或first-public。历史PDF原版事实不采用、不进入Books，若未来依赖才恢复对应历史字节/官方说明。

## 交付边界

本日作者工作安全停点：确认候选1、作者必要安全审阅1、Books提案0/写入0。Peirce FINAL已实际通过必要Evidence/Books决定及有限来源、分层反侧，报告仍进行中/§6未通过；仅剩R-ARXIV返修变化的非作者窄复查。旧坏范围是手拼编码截掉上界年份的请求错误，不是服务无端重写。实际用urlencode请求12位`202510060000 TO 202510072359`、限定cs.CL/cs.LG transformer、start0/max20/ascending，HTTP200、total72/返回20；真实[请求记录](arxiv_corrected_request.json)与[原Atom](arxiv_corrected_max20.xml)已保存。首20 published字段范围为10-06 01:08:34Z至16:19:57Z，停止此页，不将截断提交线索当first-public/覆盖分母或新全文队列。外部历史目录与VecInfer/S2R日期保留项已隔离，不作正面证据/Books/无事件或无遗漏断言。未写共享Books/index/state，未stage/commit/push。
