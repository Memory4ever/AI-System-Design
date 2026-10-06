# 11/19 指定来源入口有限补检

执行者Codex/Ohm，非原作者Dalton；这是来源补检及获授权的报告同步，不是独立日级验收。实际工具clock：2026-10-04T17:18:47+08:00（09:18:47 UTC）。窗口UTC [2025-11-18T01:00:00Z, 2025-11-19T01:00:00Z)。只核MiniMax Agent Tech入口、Anthropic原目录隐藏记录、Z.ai目标历史分页；不重审TDD+CI核心、其余潜在项附件或owner。

## MiniMax Agent Tech：入口已实际核，2025历史不能由当前页恢复

- [合同入口](https://agent.minimax.io/docs/techblog) web返回英文空导航；原生GET200实际重定向 `agent.minimax.cn/docs/techblog`。同路径 `.md` 与 `llms.txt` 各GET200，原文件和请求时间见 [HTML receipt](ohm-agent-tech.html.receipt.json)、[Markdown](ohm-agent-tech.md)、[index](ohm-agent-index.txt)。
- Markdown实际只有一个技术条目，日期2026-05-13、Agent Team；index只有techblog首页和agent-team一个技术正文链接。web英文index同样只有该正文链接，但不能把英文索引与中文日期拼成2025版本身份。
- 停止在该首页、等价Markdown与实际索引，不盲抓不存在的旧slug，也不为2026窗外文章展开机制/附件。它与EN/CN模型博客是独立入口，旧CN13条日期边界不能替代这里。
- 当前可见入口检查已结束；2025-11目标技术目录缺段作为有限历史保留。最小重开材料为官方2025目标段目录/当时techblog快照及其实际公开日期。没有证明当时无文章，不支持全机构零命中、正面Coverage或无遗漏。

## Anthropic：原Research目标段已恢复

- 原首页GET200，保存 [HTML](ohm-anthropic.html) 与 [receipt](ohm-anthropic.html.receipt.json)。web `See more` 实际仍返同首页10条；未把这个无变化响应当分页成功。
- 按Next Flight JSON解码原页面的 `_type=publicationList`、`directory.value=research`、实际 `posts` 数组171条；同组件另一个字符串引用不是第二组列表。解码依据见 [脚本](inspect-entry-supplement.mjs) 与 [structured raw](ohm-anthropic.html.extracted.json)。只查看目标月标题/日期/slug字段，不把171条变题摘队列。
- 目标附近原字段：Nov25 productivity gains；Nov24 prompt-injection defenses；Nov21 reward hacking `publishedOn=2025-11-21T14:32:00.000Z`；Nov12 Project Fetch `2025-11-12T18:19:00.000Z`；Nov4 deprecation commitments。用实际时间字段过滤本窗无条目。上下最近为Nov21与Nov12，而非只检News三则推定Research。
- 该当前目录目标日期区间已检查，原“Research历史段未恢复”撤销。停止本页结构化目标段，不读窗外核心、不扫其余年份；只支持当前列出的目录，不认证删除/未列材料或历史版本无遗漏。`publishedOn`只用于当前目录区间，不据此反推其他日报候选或重授Project Fetch日期Gate。

## Z.ai：真实分页可恢复，执行后仅当前18条，历史仍缺

- [首查Research](https://www.zhipuai.cn/zh/research)原生GET200；Flight组件 `blogsItems` 15条、`nextPage=2`、`hasMore=true`、`initialTag=all`。字段是 `createAt`，不是CMS `createdAt`，不能混作首次公开证明；顺序有2026/2025日期交错，未声称严格日期排序。
- IAB本次实际30秒超时。没有把浏览器失败立即称外部缺段：按组件 `$L17`的模块84243映射，只定点取Research自身 [page bundle](ohm-zai-research.js) 与映射support bundle，两者200。分页按钮明确 `URLSearchParams.set("page", nextPage)`、router.push，所以 `?page=2` 是原站真实入口，不是猜测API。
- 该页原生GET200，[receipt](ohm-zai-p2.html.receipt.json)，结构化响应累计18条，前15条与首页ID相同；新增145 AutoGLM `2025-12-08T16:00:00Z`、144 GLM-4.6V `2025-12-07T16:00:00Z`、143 GLM-4.7 `2025-12-21T16:00:00Z`。实际 `nextPage=3` 但 `hasMore=false`，停止第2页，不请求第3页。完整字段见 [extracted](ohm-zai-p2.html.extracted.json)。
- 当前Research列表分页已耗尽，最早可见 `createAt` 为Dec7，未恢复Nov18历史段；不能由当前18条证明历史无条目，也不能以release notes代替Research。保留最小请求为官方2025目标历史目录/原始历史列表响应，不再把已执行的“查看更多”列普通待办。
- web尝试 `z.ai/blog` 为404错误路由，不计Research覆盖；web `zhipuai.cn/zh/research?page=2`不可访问，但原生已成功，不能继续引用web失败声称分页不可执行。请求原记录见 [entry web](ohm-entry-web.json)、[index web](ohm-index-web.json)。

## 同步与未检查范围

已读root [NEGATIVE_INDEPENDENT_REVIEW](NEGATIVE_INDEPENDENT_REVIEW.md)，仅同步其实际裁决：Intuit/Foundry/Rwanda/Hope/NeuroLex五项新增关闭通过；FLOWER/Fuse此前两项通过。Intuit旧WEB_OPENAI_TAIL只有元信息，本次官方core由root实际补读，不冒充本补检者已再读。Microsoft/NVIDIA合作未在该新增抽检复读，仍沿作者具体投资/容量/未实现codesign理由，不授八项全部重新亲核。

TDD+CI12823撤销“成熟组合即关闭”，改潜在小模型/跨语种推理预算边界日期隔离；18篇论文 = 原11 + 窄尾6 + TDD1，另Codex-Max非论文方向1。98%只为best20B/best120B比值，不是绝对准确率；公开单测、隐藏评测、至多五次修复、单函数限制与无matched端到端预算保留，不授普遍替代、节省资源、Evidence或Books。实际v1§3–6由root核，此处未重复附件/owner。

本补检不审其余11来源、不处理20、不改共享Books/state/月索引。剩余普通工作是root有限来源整体终态及最终六部分日级Gate；这里不授完成。
