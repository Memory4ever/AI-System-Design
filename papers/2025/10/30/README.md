# Daily Research — 2025-10-30

**规范：** V3
**窗口：** 2025-10-29T09:00:00+08:00 ～ 2025-10-30T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T09:09:54+08:00

## 1. 结论

确定落窗正式候选2家族：Anthropic内部状态自述实验披露7分、OpenAI OWL技术披露6分；Mill实际FIRST/必要Evidence复核通过，深入完成1、标准完成1，只采用下述窄命题。root已在Ch5窄整合1家族，两段/交接/末注由Mill非写入者于08:18:27实际POST通过；OWL仅报告、写入0。Mill于09:00:42实际通过作者窄变化及最终DAY，作者仅同步独立结论，不自审。

十四每日来源本日独立有限处理。arXiv三个收窄主题提交切片27/4/19、去重46仅是线索；实际读相关完整题摘36，必要安全/设计反侧v1九项；不将相交日名、submitted/API published、后续收录时间当首次公开。Google PPI原方法/隐私反侧已窄读但日期未确认，保持隔离。Mill已核九反侧、PPI、有限来源与分层样本；普通研究、Books写入/POST和独立DAY均到停止。

## 2. 来源覆盖

原件与真实请求在 [本日目录](../_sources/daily-20251030/)，实际查询/阅读/停止在 [有限筛选](../_sources/daily-20251030/SCREENING.md)。raw/text仅定位，不作全读收据。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)首查403；官方news/rss.xml按UTC[10/29 01:00,10/30 01:00)过滤1245项，唯一OWL 10/30 00:00Z；原Blog必要架构/Agent mode读到停点 | 已检查 | RSS不是完整Research覆盖；Blog性能未披露完整运行配置 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)及内嵌publishedOn，本窗introspection=10/29 01:20Z；原Blog及链接原研究必要方法/控制/限制/Revision log | 已检查 | 原研究当前含2026/01/01修订，不冒充2025全文；初版prompt若拟采用须快照 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)后旧?page=2同页非真实分页；Mill本日正确[/page/2/](https://deepmind.google/research/publications/page/2/)curl20s失败后web恢复10/30Personhood→09/29邻界，完整题摘贡献关闭；[pubs](https://research.google/pubs/)旧year/query非正确过滤，Mill本日独立[category/search](https://research.google/pubs/?category=2025&search=language%20model)curl20s HTTP000/0bytes超时、一次web失败；[October Blog](https://www.research.google/blog/2025/10/)仅10/29→30→31邻接 | 受阻 | pubs正确请求有限失败，无响应raw，Blog不代pubs；DeepMind普通分页已修复不留hold；PPI日名未确证落窗 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)当前Muse壳；官方域名10/29日期与模型主题有界补检，停止本次query | 受阻 | 没恢复2025 Research历史正文/日级段；搜索无命中不等无事件 |
| SRC-QWEN | [旧Blog](https://qwenlm.github.io/)09/23迁移提示后实际qwen.ai壳；本窗官方域名补检只得其他日期 | 受阻 | 迁移后的历史目录数据未提取，未扩全年 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)沿实际/news/到研究10项；10/21 OCR→11/01 LPLB，动态5项09/29→12/01，停止邻接段 | 已检查 | 查看全部无href，当前切片不保证所有直发事件，非主页壳直接hold |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)26条日期卡09/16→11/06邻接；MoonshotAI组织首页只定位仓库，不把Updated当历史发布 | 已检查 | org首页不覆盖全部历史release |
| SRC-TENCENT-HUNYUAN | [Research首查](https://hunyuan.tencent.com/research)动态壳；实际浏览器一次15秒请求超时/kernel reset；官方publicList中文POST pageNum1/pageSize20/renderType0，total/list11最早2026/02；org/T1定点入口 | 受阻 | 2025历史段缺失；浏览器失败不是覆盖成功，不继续无限重试 |
| SRC-ZAI | [Research首查](https://www.zhipuai.cn/zh/research)后实际?page=2，累计18项最早12/07且没有更多；官方new-released说明09/30→12/08 | 受阻 | 10月Research段缺失；release notes不替代Research，未把首15条当末页 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)/public_papers首查；own get_article_list_v2 article_type1、US/year2025升序token80 total94/false，10/22后至12/02；type2 token20 total45/true/next40，10/23→11/27；token40末false | 已检查 | 仅日期/身份定位，目录PublishDate非首公开；未全年度题摘或补全附件 |
| SRC-BAIDU-ERNIE | [技术Blog](https://ernie.baidu.com/blog/zh/)实际1/2页，页2末，10/16→11/07邻接 | 已检查 | Blog不保证所有仓库直发 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)首查；实际index映射async/6159.4efb0769.js恢复八Paper日期，最近10/21；错误少async请求404已保留 | 已检查 | More不是历史分页，没有完整历史保证 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)与minimaxi.com/blog日期切片10/27→12/23；独立agent.minimax.io/docs/techblog及原生.md目前2026/05/13 | 已检查 | 主Blog不代Agent，Agent2025历史段缺失 |
| SRC-ARXIV | [API](https://export.arxiv.org/api/query)12分类三主线主题，submittedDate[202510281800 TO 202510291800]、start0/max50，27/4/19均不足50即止，去重46；官方availability与cs.CL月首50相关标题补检 | 已检查 | 名义批次节律非ID实际first-public；必要日期缺口隔离，不授当日46篇/零事件/无遗漏 |

按需只触发已定位Google PPI原论文2510.21684v1及Anthropic链接原研究；未扫描每周组/会议全站。两辅助query原字符串及结果限制见SCREENING，不授历史Coverage。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Signs of introspection in large language models](https://www.anthropic.com/research/introspection) | 2025-10-29T09:20:00+08:00 | 自述难区分内部读取与编造 → 内态干预/先检测再说词与prefill对照提供受限诊断 → 检验内态因果通道而非由输出反推；2+2+3=7 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，局部自述诊断与失败边界两段，Mill实际POST通过 |
| [How we built OWL](https://openai.com/index/building-chatgpt-atlas/) | 2025-10-30T08:00:00+08:00 | 自动事件可触发privileged浏览器动作、共享登录态可能泄漏 → renderer-only Agent输入与每会话StoragePartition → 分别界定输入权限/状态隔离；2+2+2=6 | 标准完成 | 仅报告：具体Chromium实现披露，不支持新的长期安全保证，写入0 |

两时间分别来自原Research CMS publishedOn和官方RSS pubDate原字段，支持本次披露事件，不证明关联论文/产品或权重的全网首次公开。校准包见 [FIRST_CALIBRATION](../_sources/daily-20251030/FIRST_CALIBRATION.md)。未定日期潜力不进入此表、不评分。

## 4. 证据与知识整合

### [Signs of introspection in large language models](https://www.anthropic.com/research/introspection)

本次披露及[链接原研究](https://transformer-circuits.pub/2025/introspection/index.html)必要位置见SCREENING。只保留可检验的内态→自述关系：concept vector、层/强度、先检测再说词、无注入/随机概念/后续turn注入控制，不能从正确说词证明意识或完整机制。有限prompt、人工设置扰动、Sonnet4 judge、不同post-training身份及“最佳层”选择限制外推；未测Sonnet4.5。原研究2026/01/01新增实验/修正prompt标签不可移为2025事件，依赖原始文字的子命题保持未采用。

实际前置对读 [WORLDVIEW-REPRESENTATION / Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)175–224：已有probe/patching不等完整因果解释，尚缺“模型自述来自自身输出反推还是受控内态通道”的诊断区分；邻接Ch4/6拥有学习条件和routing。root已将这一窄差额整合为Ch5 260/262两段及Review notes末注518（`SF-2025-ANTHROPIC-INTROSPECTION`），作者本次实际顺读233–281与末注确认。固定可见输入、相关/随机概念、时机与复述控制支持受控局部内态通道；多数失败、层/强度搜索、提示/输出偏置/干预损伤和未定位完整元认知表示近处保留，不引出意识或可靠生产自审。实际整合1家族，Mill非写入者08:18:27核两段/Ch4–6交接/末注POST通过，root已同步末注。仅此写入归于本日，不验收其他既有脏书稿。

原研究2026新增“若否则任选概念”prompt及修正的transcription/grader精确文字未采用；不把整个Alternative Prompts章节都误称2026新增，不把最佳约20%当自然成功率或0/100当总体零误报。采用的是2025 Blog已披露且Revision log未列为新增的诊断命题，未核实现或复现实验。

### [How we built OWL](https://openai.com/index/building-chatgpt-atlas/)

实际原Blog§How OWL works/Input events/Agent mode：弹窗合成到模型画面；普通未处理事件返回客户端重合成NSEvent，Agent事件则renderer-only，两路径不能合并。logged-out会话独立内存StoragePartition并结束清除。它是厂商实现说明，不证明攻击覆盖、源码已核或生产non-bypassability；startup/百tab性能缺hardware、batch、concurrency、SLO及完整evaluator（Not Disclosed），不采用宣传倍数。Atlas前周已发布，Oct30是此次架构披露，不把Oct21产品事件再算首次。

实际 [PLATFORM-SECURITY / Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)正文1203–1247及2550–2570已有external executor authority、GUI真实effect/dispatch身份与per-run隔离；Ch71/73交接是跨面tenant identity/production evidence。[AGENT-TOOL-CALLING / Ch78](../../../../books/part-07-agent/78-tool-calling.md)正文158–188已有surface/provider身份及最窄接口，邻接Ch77/79分开状态/计划。Mill实际对读确认最终仅报告具体Chromium实现；不声称已有覆盖该API，也未建立新的长期保证/差额，写入0，不强造diff。

Google PPI与九项arXiv安全/反侧的实际核心和未证明内容在SCREENING。因日期未落窗，均不成为正面Evidence或Books采用，不把必要阅读数当审阅完成家族数。

## 5. 缺口与下一步

可执行剩余：无。Mill于2026-10-05T09:00:42+08:00实际通过两正式审阅/实际Ch5整合1/OWL仅报告、Google正确参数失败与DeepMind真实page2恢复的变化回核及DAY，并重读Ch5正文/已同步末注。FIRST、两项必要Evidence、九反侧/PPI/有限源与分层样本有效不重跑；Books已写且POST通过，无待PRE/写入或末注同步。

本窗终态保留项（不用于正面证据、不进入Books、不支持无遗漏或性能/安全保证）：Google pubs日级历史、Meta/Qwen历史目录、Hunyuan2025段、Z.ai10月段、MiniMax Agent历史段；各缺对应官方历史导出/公告而非普通首页恢复，有限恢复已执行。DeepMind真实page2已恢复、Personhood贡献关闭，撤销其普通待办/hold。材料到达时只重开§2对应来源，不扩全年。

日期身份保留：Google PPI原Blog仅10/30日名相交、其关联2510.21684v1无本窗首公开依据；arXiv46线索中SCREENING具名潜力/九项必要反侧缺官方历史公告或完全落窗bounds。可接受对应官方当时公告、项目有时区发布或确切原正文可访问bounds；只重开该ID日期与准入，不因submitted/DataCite变更采用。明确贡献已关闭项不另请求日期。

Anthropic如拟采用初版prompt/2026新增实验以外的精确复现子命题，需2025原快照及与Revision log的定点对照；当前材料不能证明这些初版实现细节，其他未变化的披露/必要反侧可复用。不遍历完整版本史。

## 6. 复核

复核者：Mill（非作者）

结论：通过

Mill实际FIRST/必要Evidence通过（7/6分，深入1/标准1），DAY已核14源有限停止、全部九必要精确v1与PPI、7个分层关闭样本，未对全部36题摘或附件逐项二次读取。Ch5两段/邻接/末注08:18:27 POST通过，OWL仅报告不写。Mill FINAL于09:00:42实际通读08:50:32作者六部分与变化停点，重读Ch5 250–269、512–519及root已同步末注后裁最终DAY通过。作者仅同步非作者结论，机器结构检查不替语义，终态保留项权限未扩大。
