# Gemini 3：单项证据与 Books 决定送审

作者：Dalton。仅此项必要Evidence/OnlyReport已由root非作者实际通过，见 [独立记录](./GEMINI_INDEPENDENT_REVIEW.md)，不是19日日级ready；报告状态仍进行中。以下为受影响API证据与具体owner比较，未改Books、不授POST。

## 日期、身份与版本

- 官方发布：[Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)。实际raw [google_gemini3.html](./google_gemini3.html) L49–56：NewsArticle、mainEntityOfPage、headline完整对应，`datePublished=2025-11-18T16:00:00+00:00`，BJT `2025-11-19T00:00:00+08:00`，完全落本窗。
- 同raw L56 `dateModified=2026-03-19T17:52:32.737752+00:00`。日期元数据证明发布事件归属，不自动认证当前所有linked docs/model cards是发布日版本。本项不采用后来model card、3.1或Interactions协议。
- 开发者公告：[Start building with Gemini 3](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-developers/)，本日实际核心记录 [WEB_GEMINI_DEVELOPER.txt](./WEB_GEMINI_DEVELOPER.txt) 文件L154–155/L183–184（其中网页定位L262–263/L292–293；网页当前行号已发生两行漂移，不用行号替代内容身份）。这是官方版本变更说明，不是客户端行为复现。
- 官方cookbook精确提交 `de43f20bf165b1be8a71ed769c4cee08034e96c6`，commit message `Gemini 3 (#1037)`；[有限5条提交查询raw](./gemini_cookbook_thinking_commits.json)和receipt保留 `until=2025-11-19T01:00:00Z`、`per_page=5`。提交时间 `2025-11-18T16:00:28Z`仅用于版本定位，不当作public push证据或替代发布事件时间。
- 精确源 [Get_started_thinking.ipynb](https://github.com/google-gemini/cookbook/blob/de43f20bf165b1be8a71ed769c4cee08034e96c6/quickstarts/Get_started_thinking.ipynb) 的GitHub Contents原始响应保存在 [gemini_thinking_contents_de43f20.json](./gemini_thinking_contents_de43f20.json)；base64 notebook的 `Thinking level for Gemini 3` / `Migrating from thinking_budget to thinking_level` markdown及对应代码已实际读取。raw.githubusercontent一次连接reset，改用Contents API成功；不重试失败路径。

## 实际增量与采用边界

旧多轮客户端可能只把可读text与function arguments重新序列化；官方本次明确宣布更严格的thought-signature验证，并把它关联到跨轮保持模型thoughts。采用命题只是：**升级到当时Gemini 3 Pro API须重新核对多轮状态携带合同，不能假定旧客户端的文本/参数重建已充分兼容。**这是版本兼容性要求，不证明signature是业务授权、真实解释或可审计的完整推理。

发布日cookbook支持更窄且可查的参数协议：`gemini-3-pro-preview`的thinking level仅列low/high，high为默认，动态过程仍可少用token；旧`thinking_budget`仍支持。代码使用`types.ThinkingConfig(thinking_level=thinking_level, include_thoughts=True)`。这不支持固定token承诺、普遍低延迟或质量最优；本项不采用当前指南的minimal/medium、两参数同传400、temperature建议等后来具体规则。media-resolution在发布说明中确认新增控制，但未恢复发布日完整枚举/默认，不补造。

同公告另明确：Grounding with Google Search及URL context现在可以和structured outputs组合。只采用接口组合支持，不推导检索事实正确、schema语义正确或agent可靠性。client-side bash仅让模型提出shell commands；hosted server-side bash当时仅early-access partners、GA coming soon。不能把模型提议当执行许可，也不能把早期托管功能写成GA或全局安全保证。

## 对照、反侧与有限恢复

这是接口变化，不需要以SOTA分数证明兼容性命题。版本对照来自官方发布说明的`stricter validation`与精确cookbook的旧budget仍兼容；不声称已经调用API验证有效/无效请求。

精确同提交 [Function_calling.ipynb](https://github.com/google-gemini/cookbook/blob/de43f20bf165b1be8a71ed769c4cee08034e96c6/quickstarts/Function_calling.ipynb) 的 [Contents raw](./gemini_function_contents_de43f20.json) cells16/18/28/35–36/53已定点读。手动分支把原始`part`放入model Content并返回FunctionResponse，末尾要求stateless调用携带完整history；但该示例没有explicit signature规则，也不能据此证明所有SDK路径会保留签名或已支持Gemini 3。

当前官方developer guide实际已更新2026-09-23，采用`gemini-3.1-pro-preview`及Interactions/stateful previous_interaction_id：[WEB_GEMINI_CURRENT_TARGET.txt](./WEB_GEMINI_CURRENT_TARGET.txt)。旧thought-signatures URL亦发生移动。两者明确不当作发布日协议。搜索得到Nov19及以后客户端issue，仅作恢复线索，不加入本窗事件，不用第三方复述认证当时规则。

有限恢复停止于：发布公告 + 发布日精确thinking notebook + 同提交手动function-history例。**并行/顺序function parts的签名位置、哪些缺失触发400、dummy signature绕过、跨模型复制、服务端内部状态格式仍不采用。**若需要这些具体命题，只在取得发布日官方guide snapshot或当时精确SDK实现/官方测试时重开；不是因为这些未得就关闭已经支持的版本变更事实。

轻量纠错检查：本次打开官方事件页未见针对上述协议段的撤回/勘误公告；存在后改metadata与活文档替换信号，已处理为版本隔离。未遍历全站或完整历史，不能声称永久无纠错。

## Owner具体差额与建议

已读Books context、ROADMAP、Ch75相关正文/交接及Ch74/76相邻开头；共享Books只读，未写。

- 唯一主要owner `AGENT-CONTEXT`：[Ch75 Context](../../../../../books/part-07-agent/75-context.md) `Context 是一次调用的可见状态`列conversation/tool schemas/results/workflow state；`Context Compression 必须保留执行状态，而不只是语义`要求versioned state、scope/expiry/source/frontier，以及paired-state regression。它实际承载一般状态保留与压缩正确性，但**不是Gemini opaque-signature的具体协议覆盖**。
- [Ch74 Prompt](../../../../../books/part-07-agent/74-prompt.md)已经区分versioned runtime input和执行语义；[Ch76 RAG](../../../../../books/part-07-agent/76-rag.md)持有evidence/provenance。因此工具组合支持不应改写成事实正确或新RAG机制。
- `AGENT-TOOL-CALLING`：[Ch78](../../../../../books/part-07-agent/78-tool-calling.md) `Tool Contract` / `模型输出只是 Proposal`实际规定model intent → schema validation → authorization → policy validation → execution，真实principal而非模型字段决定权限。bash proposal≠execution authorization在这里已有具体覆盖；此成熟原则不计入Gemini增量分。

**仅报告已获root非作者通过，不请求Books写锁。**本次具体差额是发布日供应商兼容性与能力组合事实，并未公开signature内部机制或新增可验证的长期状态算法。Ch75的一般原则仍成立；不另造SOTA章、signature配方缺口，亦不重复Ch78授权链。实际写入0，无POST，不因此授日级通过。

评分保持 `2 + 2 + 1 = 5`，对象是本次版本接口变化；因实际兼容性变化，深入受影响说明/精确版本，而非只做摘要审阅。采用的有限命题已读足，不声称实验/SDK/生产验证。

## Root实际核验点

1. HTML L49–56的事件身份、timezone及改版边界；BJT00:00确在19日窗口。
2. 发布公告实际支持strict-validation变更、tool/schema组合和early-access bash；不能扩成signature安全/GA。
3. 精确thinking notebook的low/high及旧budget兼容，commit不等public push；current guide确不用于历史协议。
4. Ch75一般state保留与opaque协议差异、Ch78授权链具体已有覆盖；是否接受仅报告，无须为了配额改书。

2026-10-04 root独立协调反馈：11/01已独立完成1/30；19日11方向首批准入校准不等日级完成。本包优先交root单项Evidence/Books核验，其他普通待办继续。这是root协调回传，不归因为人类新指令。

2026-10-04后续root实际回传：已核原HTML身份/日期、developer目标段、精确thinking/function两个notebook关键cells、Ch75状态及Ch78授权链；OnlyReport倾向接受，正式notes尚待回传。实际检查范围可复用，但作者不据“倾向”自授最终Evidence/Books或日级通过。未确认落窗潜在项保留理由与最小日期请求，允许有限恢复后精确隔离；中心纠错/冲突必要反侧仍处理，不把未读全文统一当普通待办。

随后正式 [GEMINI_INDEPENDENT_REVIEW.md](./GEMINI_INDEPENDENT_REVIEW.md)已实际读取：root于2026-10-04T15:53:55+08:00通过限定命题与OnlyReport。上段保留先前回传阶段，不覆盖此最终单项结果；日级及其余材料仍未通过。
