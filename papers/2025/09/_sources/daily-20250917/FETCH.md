# 2025-09-17 原始请求记录

最新窄补：CN MiniMax本日独立20秒请求HTTP200/144114bytes，原minimax-cn-recovery.raw，正文13条Oct27→Jan15越下界停止，旧目录泛化缺口撤回。antischeming真实链接精确scheming-2509.15541v1.html单次20秒HTTP200/2077557bytes，完整题摘/目录实际读，未称方法/附录已审或该v1已于17公开。Google learnyourway-2509.13348v1.html单次20秒HTTP200/119782bytes，只为贡献含糊点读§2–4；实际差额在FIRST_BATCH，原响应/失败全部保留。

仅本日窗口2025-09-16T09:00+08至09-17T09:00+08；不继承别日来源结论。2026-10-06T11:55+08启动，各成功原响应保存同目录*.raw。

OpenAI Research首请求11:55:44 HTTP403。随后顺序请求（每次curl8秒有界）：

```text
{"name": "anthropic", "url": "https://www.anthropic.com/research", "time": "2026-10-06T03:55:46.725439+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "deepmind", "url": "https://deepmind.google/research/", "time": "2026-10-06T03:55:51.951432+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "google-pubs", "url": "https://research.google/pubs/", "time": "2026-10-06T03:55:59.976293+00:00", "exit": 28, "status": "HTTP=000", "error": "curl: (28) Connection timed out after 8006 milliseconds"}
{"name": "google-month", "url": "https://research.google/blog/2025/09/", "time": "2026-10-06T03:56:08.007892+00:00", "exit": 28, "status": "HTTP=000", "error": "curl: (28) Connection timed out after 8006 milliseconds"}
{"name": "meta", "url": "https://ai.meta.com/research/", "time": "2026-10-06T03:56:16.031971+00:00", "exit": 28, "status": "HTTP=000", "error": "curl: (28) Connection timed out after 8002 milliseconds"}
{"name": "qwen", "url": "https://qwenlm.github.io/", "time": "2026-10-06T03:56:16.543161+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "deepseek", "url": "https://www.deepseek.com/", "time": "2026-10-06T03:56:16.687691+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "kimi", "url": "https://platform.kimi.com/blog", "time": "2026-10-06T03:56:17.035043+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "hunyuan", "url": "https://hunyuan.tencent.com/research", "time": "2026-10-06T03:56:17.262685+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "zai", "url": "https://www.zhipuai.cn/zh/research", "time": "2026-10-06T03:56:18.248939+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "zai-page2", "url": "https://www.zhipuai.cn/zh/research?page=2", "time": "2026-10-06T03:56:18.963689+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "seed", "url": "https://seed.bytedance.com/en/research", "time": "2026-10-06T03:56:19.296628+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "seed-papers", "url": "https://seed.bytedance.com/en/public_papers", "time": "2026-10-06T03:56:19.735415+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "seed-blog-api", "url": "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true", "time": "2026-10-06T03:56:19.954180+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "seed-paper-api", "url": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true", "time": "2026-10-06T03:56:20.178505+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "ernie", "url": "https://ernie.baidu.com/blog/zh/", "time": "2026-10-06T03:56:20.475541+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "ernie-page2", "url": "https://ernie.baidu.com/blog/zh/page/2/", "time": "2026-10-06T03:56:20.853914+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "mimo", "url": "https://mimo.xiaomi.com/", "time": "2026-10-06T03:56:21.263697+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "minimax", "url": "https://www.minimax.io/blog", "time": "2026-10-06T03:56:23.323120+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "minimax-cn", "url": "https://www.minimaxi.com/blog", "time": "2026-10-06T03:56:24.462895+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "minimax-agent", "url": "https://agent.minimax.io/docs/techblog", "time": "2026-10-06T03:56:25.224539+00:00", "exit": 0, "status": "HTTP=200", "error": ""}
{"name": "hunyuan-api", "exit": 0, "status": "HTTP=200", "error": ""}
```

arXiv首查submittedDate:[202509151800 TO 202509161800]，language model训练/推理/attention/reasoning/alignment/memory、LLM、Transformer、WorldModel、VLA、FoundationModel、GPU model、diffusion cache/generation/policy，start0/max200/ascending；35秒超时无响应，未计覆盖。窄重试同区间ti:LLM/transformer/diffusion/language model/agent，25秒；具体结果另记，不把APIpublished当first-public。web API/日列表/月列表恢复在17arxivrestore/17core0原记录，失败不记0。停止条件是主题查询实际返回到totalResults或可用路线已有限失败；分类宽月表只查漏不作逐篇队列。
