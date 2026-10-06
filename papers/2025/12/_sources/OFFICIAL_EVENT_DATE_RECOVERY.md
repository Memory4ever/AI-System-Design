# 四个已知官方事件的日期恢复 sidecar

**检查时间：** 2026-10-02T18:06:25+08:00（取证结束，非事件公开时间）。
**授权范围：** 仅核验下列四个已知事件的日期；不发现新论文，不建立 arXiv 新池，不修改 Daily、Books、索引或学习状态。
**目标窗口：** `[2025-12-16T09:00:00+08:00, 2025-12-17T09:00:00+08:00)`，等价于 `[2025-12-16T01:00:00Z, 2025-12-17T01:00:00Z)`。
**依据：** 已读取根目录 `AGENTS.md` 与 [Report 合同 §2、§3](../../../../docs/REPORT_CONTRACTS.md)。日字段的时区不明、或其整天范围只与窗口相交，均不能作为确定落窗证据；有界范围必须完全包含于窗口。

## 结论及采用边界

| 已知事件 | 本次恢复结果 | 可采用的时间证据 | 不可据此宣称 |
| --- | --- | --- | --- |
| Anthropic alignment-faking mitigations | 原站首次公开时刻/完全落窗范围不可恢复 | 原站仅显示 `Dec 16, 2025`，无时区 | 原站首次公开落窗、北京时间整天日期或零命中 |
| Meta SAM Audio | 同事件官方公告时刻已恢复；指定研究页首次上线仍不可恢复 | 官方 X 公告字段为 `2025-12-16T17:26:10.000Z`，即 `2025-12-17T01:26:10+08:00`，公告本身落窗 | 研究页首次上线等于公告时间；整个材料家族最早公开一定落窗 |
| Meta PE-AV | 指定研究页首次公开时刻/完全落窗范围不可恢复 | 原页仅显示 `December 16, 2025`，无时区；找到较晚官方社交帖的定位线索但未取得原始日期字段 | 将 SAM Audio 帖中泛称的 encoder 自动视作 PE-AV 精确首发；采用转载时间归窗 |
| Seedance 1.5 pro 官方 Blog | 官网声明的 Blog 发布时刻已恢复并落窗 | `ArticleMeta.PublishDate=1765882058000`，即 `2025-12-16T10:47:38Z` / `2025-12-16T18:47:38+08:00`；官方前端明确使用 `Asia/Shanghai` | arXiv 首次公开、模型所有渠道的全球最早公开，或不可篡改的历史上线审计 |

这是日期证据交付，不是四项材料的贡献审阅、Daily 独立验收或 Books 判断。作者可采用已恢复的 **Blog 发布事件** 或 **官方公告事件** 时间，但不能把它们无说明替换为研究页/论文的首次公开时间。对严格要求原站首次公开的项，SAM Audio 也仍是缺口。

## 1. Anthropic

原始入口：[alignment-faking mitigations](https://alignment.anthropic.com/2025/alignment-faking-mitigations/)。

### 原始字段

原站 HTTP GET 成功（200）；检查原始 HTML 中的 metadata、JSON-LD、日期字段与 feed 声明：

```html
<div>Dec 16, 2025</div>
```

- 当次完整响应未找到 `datePublished`、`dateModified` 或发布日期 meta；没有 `application/ld+json` 脚本。
- 日期仅是作者区域的展示文字，没有时分秒或 offset。不能假定 UTC、美国当地时区或北京时间。
- 原始响应 SHA-256：`8764fc936d21c5ac0b11515dc3c504e6a33917cdfb9180ad0055a67e4b7b652e`（按 UTF-8 编码计算）。这是本次响应的识别信息，不是历史公开时间。

### 有限替代路径与停点

1. [官方博客首页](https://alignment.anthropic.com/) 原始 HTML 可读，没有发现 RSS/Atom 声明或相关 feed 链接。
2. 两个常规 feed 路径各检查一次：[feed.xml](https://alignment.anthropic.com/feed.xml)、[rss.xml](https://alignment.anthropic.com/rss.xml)，均返回 404 HTML；它们只是探测路径，不是存在过历史 feed 的证明。
3. 对确切 slug/标题的官方 X 定点搜索未恢复可验证的同事件机构帖。搜索不命中不证明机构从未发帖。
4. 定位到[同名作者 linkpost](https://www.alignmentforum.org/posts/czMaDFGAbjhWYdKmo/towards-training-time-mitigations-for-alignment-faking-in-rl)，页面提取显示同一批作者、原站 linkpost 与 `16th Dec 2025`。该页面原始 GET 返回 429，未取得机器可读的带时区发布字段；未重试。它属于作者渠道，不等于机构官方发布记录；目前只有日字段，不能收窄首公开范围。

**终态：** 当前有限可用原始路径内不可恢复，隔离为日期保留项，不支持确定当窗候选或覆盖通过。

**重开条件：** 获得指定原站的带 offset 发布字段、同事件官方历史 RSS/Atom 的 `pubDate`/`published`，或可核验身份及链接的官方公告原始时间字段。若只能获得较晚公告，需要另有首发下界证据，才能声称原站首公开范围完全落窗；作者 linkpost 时间本身不能提供这个下界。只重开本事件，不扫描新池。

## 2. Meta SAM Audio

原始入口：[SAM Audio 研究页](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)。

### 研究页日期字段

原始 HTTP 直连失败（Node fetch 失败；一次 curl 在 20 秒超时，HTTP 状态 000）。随后浏览器成功打开指定页面，检查 **当前页面 DOM 内的 HTML/metadata/JSON-LD**，而非声称取得原始 HTTP 响应：

```html
<p class="_8w6f _8wl0 _8w6h">December 16, 2025</p>
```

当次 DOM 无 JSON-LD 脚本、无 `<time>`，未找到 `datePublished`、`dateModified`、`publish_time`、`publication_date` 或日期类 meta；未发现 RSS/Atom link 声明。DOM 检查不排除历史版本或本次无法取得的服务端响应曾有其他字段。日字段时区仍未恢复。

### 同事件官方社交证据

原始入口：[AI at Meta 官方 SAM Audio 公告](https://x.com/AIatMeta/status/2000980784425931067)。该账号在 Meta 研究页页脚有官方链接。第三方页面只用于定位此帖 URL，未采用其日期；随后已在 X 原始页面验证账号、SAM Audio 公告身份和字段。

浏览器打开此帖后，实际 DOM 字段为：

```html
<meta property="article:published_time" content="2025-12-16T17:26:10.000Z" nonce="">
<meta property="article:author" content="https://x.com/AIatMeta" nonce="">
```

- 公告文字明确介绍 SAM Audio，并宣布向社区分享；这是同一项目的官方发布公告，不是第三方报道。
- `Z` 明确表示 UTC；换算为 `2025-12-17T01:26:10+08:00`，位于目标窗口内。
- 页面可见时间为 `1:26 · 2025年12月17日`；归窗使用上述 UTC meta，**不依赖浏览器本地时间文字**。当次没有 JSON-LD 或 `<time>` 字段。
- 公告指向 [go.meta.me/568e5d](https://go.meta.me/568e5d)，网页读取确认重定向到[官方 SAM Audio 项目页](https://ai.meta.com/research/samaudio/)；项目页提取没有正文，浏览器导航超时，因此停止，不把项目页视为已完成日期核验。

**适用边界：** 已恢复的是这一条官方公告的发布时刻，不是指定研究页首次上线时刻。公告证明此时已公开，但不能排除在窗口起点之前已公开；因此单凭公告不能构造研究页首公开的完整落窗范围。也不自动把材料家族再次计作新论文。

**重开条件：** 若作者只需记录该公告事件，直接引用此原始 UTC 字段即可，不必继续重试。若需要原站/材料家族首公开，补指定研究页的权威发布字段或带时区历史 RSS，或获得能同时约束首发下界和上界、且完全落窗的官方历史证据；只重开 SAM Audio。

## 3. Meta PE-AV

原始入口：[PE-AV 研究页](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)。

### 实际字段与检查边界

原始 HTTP 直连 Node fetch 失败。网页提取与浏览器均成功访问指定页；当前 DOM 的实际日期为：

```html
<p class="_8w6f _8wl0 _8w6h">December 16, 2025</p>
```

当次 DOM 无 JSON-LD、无 `<time>`、无日期类 meta；未找到 `datePublished`、`dateModified`、`publish_time`、`publication_date`，或内嵌脚本的明确发表时间字段；未发现 RSS/Atom link 声明。没有取得原始 HTTP HTML，不将 DOM 的阴性结果表述为所有服务端/历史字段均不存在。

### 有限官方替代线索

- §2 的 SAM Audio 官方帖提到一项 perception encoder，但该帖本身未给出 PE-AV 精确身份。因此 **不把 SAM Audio 帖的时间直接授予 PE-AV**。
- 定点搜索定位到一条 PE-AV 较晚官方帖线索：[AIatMeta/status/2001698702961053750](https://x.com/AIatMeta/status/2001698702961053750)。定位来源为[转载页面](https://blockchain.news/flashnews/meta-open-sources-pe-av-engine-powering-sam-audio-s-state-of-the-art-separation-what-traders-should-know-about-this-multimodal-ai-release)的 JSON-LD `isBasedOn`，实际值即上述官方 URL。
- 转载 JSON-LD 的 `datePublished=2025-12-18T08:58:00Z` 属于 **转载自身**，不是 Meta 原始发表字段，不采用它归窗，也不采用转载摘要证明官方帖内容。
- 官方帖原始 Node GET 失败；网页读取返回 403。未恢复该帖的原始内容/时间字段，停止重试。即便以后证实该公告在 12 月 18 日，也不能用较晚推广/公告替代 12 月 16 日研究页的首次公开时间。

**终态：** 当前不可恢复原站首次公开时刻或完整落窗范围；日期保留，不是证明窗外，也不是零命中。

**重开条件：** 指定研究页的带时区发布元数据或官方历史 RSS；或精确点名 PE-AV 且关联同一研究页的官方公告原始时间字段。要证明首次公开，仍需避免将后续宣传帖当首发，并取得必要下界。只定点重开此页/该帖，不扩展成 Meta 新论文扫描。

## 4. Seedance 1.5 pro 官方 Blog

原始入口：[Seedance 1.5 pro 官方发布 Blog](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)。

### 原始 HTML 的机器可读数据

原站 HTTP GET 成功（200）。原始 HTML 没有日期类 meta 或 JSON-LD，但有官方路由数据脚本 `window._ROUTER_DATA`。本次通过 JSON 解析读取，不从展示日字段猜时间：

```text
window._ROUTER_DATA.loaderData["(locale$)/blog/(id)/page"].data
  .article.SubArticle.ArticleMeta.ID = 1817
  .article.SubArticle.ArticleMeta.ArticleID = 1765883631909
  .article.SubArticle.ArticleMeta.ArticleType = 2
  .article.SubArticle.ArticleMeta.PublishDate = 1765882058000
  .article.SubArticle.ArticleMeta.UpdateTime = 1788415475000
  .article.SubArticle.ArticleMeta.StatusEn = 2
  .article.SubArticle.ArticleMeta.StatusZh = 2
  .article.SubArticle.ArticleSubContentEn.TitleKey =
    sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro
```

条目标题与精确 slug 对应用户指定 Blog。原始页面展示 `2025-12-16`；这项文字只作交叉检查，不是归窗依据。一次原始响应 SHA-256 为 `e7208475ebe2df5fc1cf251dfb7c78232102b713c783d06350495fe4aae817ed`（按 UTF-8 编码计算）；后续独立解析再次取得相同 `PublishDate`。

### 官方前端字段解释与时区

从该页实际 `<script src>` 获取[官方前端 main.897993d4.js](https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/deploy/flow/ai_official_website/88329/static/js/main.897993d4.js)，HTTP 200。该资产 SHA-256：`d8edcecbc1f4ae249e191f5333f54a38194ed27f1a91f0dc2b1c3061450ff08a`。

在模块 `39131` 内，导出 `pp` 实际对应 `T`，代码明确为：

```javascript
var R="Asia/Shanghai";
function T(e){return l()(e).tz(R)}
l().extend(p()),l().extend(u()),l().tz.setDefault(R);
```

Blog 展示日期的代码调用 `pp(...PublishDate).format("YYYY-MM-DD")`。这支持该数值是前端消费的时间戳、展示时区为 `Asia/Shanghai`，而不是从公司所在地作假设。以毫秒 epoch 解释并换算得到：

```text
1765882058000 ms since Unix epoch
= 2025-12-16T10:47:38.000Z
= 2025-12-16T18:47:38+08:00
```

该时刻严格位于目标窗口内。字段及转换支持 **官网所声明的该 Blog 发布事件时间**；此结论不依赖 HTTP `Date`、抓取时间、repo commit、`ArticleID` 或 `UpdateTime`。

**边界：** `PublishDate` 是当前官方发布元数据，未取得不可变历史上线日志，不能证明字段从未被编辑，也不证明所有渠道最早公开。不得移作 arXiv 个体公告时间、技术报告首次公开时间或模型首次对外可用时间。前端时区仅在此站得到验证，不外推给 Anthropic 或 Meta。

**重开条件：** 对官网声明的 Blog 发布事件，无需日期补证。若作者要求更强的历史首次上线/跨渠道最早公开证明，只补该 Blog 同事件官方历史 feed、公告或发布日志；不得以论文提交记录替代，也不顺带建立 arXiv 新池。

## 停止与交付

- 已完成有限路径日期调查；所有阴性结论仅限实际检查入口，不声称穷尽互联网或机构历史发布渠道。
- 外部不可恢复项已有明确适用限制与定点重开条件，当前不继续重试。
- 原始证据 URL、DOM/JSON 字段路径和必要值集中保留在本 sidecar；未另写 HTML、JSON、附件或其他 repo 文件。
- 无 Daily/Books 编辑，无候选扩池，无 stage、commit、push；报告作者自行协调采用事件身份与首次公开边界。
