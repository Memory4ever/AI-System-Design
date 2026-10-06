# 2025-11-20 Qwen 动态入口有限停点

作者Dalton；2026-10-04约17:49–17:51 BJT实际执行。原入口 `https://qwenlm.github.io/` 只显示September及更早旧博客；实际点击Research为 `https://qwen.ai/research`，web提取0行。原响应见 `WEB_DAILY_05_08.json` / `WEB_DAILY_BOUNDARIES.json`，本日实际下载 `qwen_research.html` 为200但只有动态页面，不认证文章目录。

本次在已reset的CUA以唯一入口调用 `cua.createBrowserTab("iab", "https://qwen.ai/research", {visible:false})`，timeout_ms=60000。实际工具83.9458秒后返回 `js execution timed out; kernel reset, rerun your request`。没有返回tab身份、DOM、页面状态或截图；不能声称浏览器看见零条目，也不能将工具超时归因服务器无内容。未重复相同空路径。

本窗目标研究列表作为终态保留项，不能支持候选、Books、正面Coverage或无遗漏。最小替代是官方目标历史目录/可核的原始文章列表响应及事件日期；到达后只重开Qwen本窗切片。没有扫描其他月份论文或新增全文队列。
