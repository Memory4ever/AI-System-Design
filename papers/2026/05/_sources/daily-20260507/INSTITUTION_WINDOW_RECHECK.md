# May07 机构每日来源窗口复查 — 作者侧

检查窗口：2026-05-06 09:00 至 2026-05-07 09:00 Asia/Shanghai。实际复查：2026-09-14。范围是当前可访问的官方历史目录及当窗/邻接条目，不重建不存在的当日查询日志。未获精确发布时间的条目不强归 09:00 截点；下列 coverage limitation 不是“0 候选且全站已关闭”。

| 来源 | 实际入口/尝试 | 结果与停止点 | 剩余边界 |
| --- | --- | --- | --- |
| OpenAI | [Research](https://openai.com/research/)、官网限定 May6/7 查询；打开 [May6 privacy guide](https://openai.com/index/how-chatgpt-protects-privacy/) 与 [B2B Signals](https://openai.com/index/introducing-b2b-signals/) | guide 是既有隐私机制说明，所连 Privacy Filter 为 Apr22；Signals 是企业采用/经济指标，不形成模型系统机制候选 | 没有重新构建完整历史目录分页；搜索无命中不证明穷尽 |
| Anthropic | [Research](https://www.anthropic.com/research)、[NLA](https://www.anthropic.com/research/natural-language-autoencoders)；[primary paper](https://transformer-circuits.pub/2026/nla/index.html) | NLA 博客只标 May7；该 family 已隔离为本日安全终态，不计入分母 | 缺不可变的 09:00 截点时间；只有取得该时间与 exact-version artifact 才重开，不能支持“全站无遗漏” |
| Google AI | [Google Research Publications](https://research.google/pubs/) 与 [DeepMind Research](https://deepmind.google/research/)、官方域 May6/7 有界查询 | 可访问入口，未找到足够日级历史覆盖证据；AI for Science 按现有暂停范围不扩池 | 历史目录/时间粒度不足，不能声称当窗全站零研究 |
| Meta AI | [Research](https://ai.meta.com/research/) 两次读取 | 两次未取得可检索正文；按受限来源检查终态记录 | 精确 endpoint 的访问/提取缺口仍是 coverage limitation，不据此推断当窗零发布 |
| Qwen | 旧官方博客跳转 [qwen.ai](https://qwen.ai/)，旧目录停留2025；官方域 May6/7 查询 | 新入口未返回研究正文，旧目录不是2026历史；按受限来源检查终态记录 | 当窗历史 coverage limitation 仍保留，不据此推断当窗零发布 |
| DeepSeek | [News](https://www.deepseek.com/news/) 实际打开 | Research 可见邻接 Feb25 DualPath / Jun24 V4；News Apr24 V4 preview / Sep10 V4.1，已越过窗口，无当窗条目 | 闭合此可见官方目录；不声称未索引页面或所有发布渠道为零 |
| Moonshot | [Kimi Platform Blog](https://platform.kimi.com/blog)、官方域日期查询 | 可见26项，最新 Nov7 2025，不能覆盖2026；按受限来源检查终态记录 | 目录陈旧的 coverage limitation 仍保留，不据此推断当窗零发布 |
| Hunyuan | [Research](https://hunyuan.tencent.com/research) 返回空正文；官方域日期查询无匹配；尝试浏览器 | 浏览器报告 No browser available；按受限来源检查终态记录 | endpoint/提取缺口仍保留；没有沿用旧04-30/05-21邻接声明，也不推断当窗零发布 |
| Z.ai | [Research](https://www.zhipuai.cn/zh/research) 两次 timeout；官方域日期查询无匹配 | 无可读取正文；按受限来源检查终态记录 | endpoint access limitation 仍保留；没有沿用旧04-29/05-20声明，也不推断当窗零发布 |
| ByteDance Seed | [Research](https://seed.bytedance.com/en/research)、[Publications](https://seed.bytedance.com/en/public_papers) 与下列实际公开 API | 总242项/13页，读取第1页与第2页直到04-08，已越过下界；05-06 TDDFT 为暂停 AI for Science，Cola DLM 留日期冲突待定 | 目录 PublishDate 为可回填日级元数据，不是 first-public timestamp；细节见下 |
| ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) 与官方日期查询 | 当前实际列表邻接 May9 / Apr30，继续到Apr15，跨越窗口；无当窗条目 | 闭合可见官方博客范围，不泛化其他渠道 |
| MiMo | [官网 Paper/Blog](https://mimo.xiaomi.com/) | Paper 8项，邻接 Jun29 MOPD / Mar13 ARL-Tangram；Paper范围无当窗项 | Blog 12卡片没有日期，Blog coverage limitation |
| MiniMax | [Blog](https://www.minimax.io/blog) 与官方域日期查询 | 实际列表从Aug/Jul/Jun到 May27、May26，继而 Mar18、Feb14；已跨窗口，无当窗条目 | 闭合可见官方博客范围，不泛化未索引渠道 |

## Seed 可复现分页与停止点

公开前端脚本 `main.08aea26b.js` 披露 `Publication=1`、`page_token=Number(offset)`、GET `/api/get_article_list_v2`。实际请求：

- [第1页，offset 0](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&page_token=0&order_desc=true)
- [第2页，offset 20](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&page_token=20&order_desc=true)
- 请求头 `x-tt-locale: US`；响应 `total=242`、第二页 `next_page_token=40`、`has_more=true`。到达窗口下界即可停止，不需要继续其余11页。

| 目录日期 | identity / 条目 | 窗口处理 |
| --- | --- | --- |
| 05-12 | 2605.13831 / Training Long-Context VLMs | 上界外 |
| 05-11 | 2605.12305 / Images in Sentences | 上界外 |
| 05-09 | 2605.09233 / Robust Sequential Decomposition | 上界外 |
| 05-06 | 2605.06489 / TDDFT Gradients | 完整摘要为化学模拟加速，AI for Science 暂停，不入分母 |
| 05-06 | 2605.06548 / Continuous Latent Diffusion Language Model | 目录日期与 arXiv v1 冲突；已隔离为本日安全终态，不入分母。只有不可变 institution first-public timestamp 把它归入本窗时才重开 |
| 05-05 | 2605.05460 / Agentic Discovery of XC Functionals | 已越过下界，AI for Science 暂停 |
| 05-03 | 2605.02134 / Video Generation with Predictive Latents | 下界外 |
| 04-30 | 2605.02657 / CARD；2605.00503 / AR image generation | 下界外 |
| 04-08 | 2604.08702 / Topological invariant | 第2页最后项，停止 |

Cola DLM 目录 `PublishDate=1778083200000`（05-06 UTC日期字段），`ArticleID=1782904790925`、`UpdateTime=1782904818000` 是7月元数据；[exact-v1 history](https://arxiv.org/abs/2605.06548v1) 为 **05-07 16:44:56 UTC submitted**。提交时间不等于公告时间，但该交叉结果足以说明目录日期不能直接当05-06已公开的证明。未发现早于本窗截点的可靠公开证据，不据后补目录回填候选。

## 跨截点隔离身份

隔离注册见 [institution-pending-identities.json](institution-pending-identities.json)。NLA 只有一条 family，May07/May08
只能引用，不能各计一个候选。Cola DLM 也只登记一个 family；548 arXiv owner batch 分母不含这两项。两者均已成为
05-07 的安全终态，不再作为 active pending；只有命中各自明确重开条件时，才由唯一 owner 日处理。隔离期间不计
Source Review 完成或 Books 整合。
