# Live 2026-10-09：每日机构入口与有限停止

窗口仅2026-10-08完整BJT自然日。当前入口检查不等于全网召回；日期含糊/空页面不算零命中。只保留当窗具体贡献，不把宽目录逐项变成审阅队列。作者 supplement_20260312；OpenAI与Qwen必要PR及Anthropic独立核见 [root记录](independent-review.md)。

| 来源 | 本轮实际入口、停止位置 | 当前结果/局限 |
| --- | --- | --- |
| OpenAI | root实际[Research index](https://openai.com/research/index/)首屏Oct7两项→Oct6两项→Sep29 | 当前dated入口窗前停止，不授全网无遗漏 |
| Anthropic | [Research](https://www.anthropic.com/research)两项Oct8→Oct1；作者与root独立必要全文/FAQ | 1候选OSS Scanner、1具体EX sky；[原证/PRE](anthropic-core.md) |
| Google AI | [DeepMind Research](https://deepmind.google/research/)及[blog](https://deepmind.google/blog/)当前页；EmbeddingGemma2官方原件Oct6。[Google Research blog](https://research.google/blog/)Oct7→Oct6→Oct5→Oct2→Sep29 | 当前dated blog入口窗前停止。pubs第1页15/11600按年份，含2027，不能当首公开日；不扫描全年目录。定点Oct8查询无结果不是零命中证明 |
| Meta AI | research空响应，恢复[blog](https://ai.meta.com/blog/)latest Jul27→Jul21→Jul9→Jul7（Apr8 pinned不作排序首项）；[publication结果](https://ai.meta.com/results/?content_types%5B0%5D=publication)当前11个dated位置Oct2→Sep24→Sep7→Sep6→Aug4→Jul29→Jul17，随后2019/2018混排停止 | 当前切片未出现Oct8，不把混排目录或空research授完整历史覆盖；定点Oct8搜索无结果不独证零 |
| Qwen | [原博客](https://qwenlm.github.io/)5条旧项并指向新目录；[新research](https://qwen.ai/research)两次web空、官方HTML为公共app壳，IAB实际51.9s超时/reset。精确[nightly](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0-nightly.20261007.8003d28042)完整release API | carrier published_at Oct7UTC22:01:24=Oct8BJT、非draft/prerelease；窗前PR first-public不搬入，具体EX待独核见[qwen记录](qwen-nightly.md)。停止重复目录恢复，精确隔离；HTML overlay expiry Aug10非文章日期 |
| DeepSeek | [homepage](https://www.deepseek.com/)及[news](https://www.deepseek.com/news/)当前列表Sep10V4.1→Apr24V4→Dec1/2025 | 首旧日期停止，不展开旧技术或commit |
| Moonshot | [Kimi blog](https://platform.kimi.com/blog)当前26标题，最新Nov7/2025→Nov6；[MoonshotAI](https://github.com/MoonshotAI)当前10/42 repos，kimi-code Updated Oct8只是机会；精确kimi-code releases API前5 published Sep24→Sep23→Sep19→Sep18→Sep17 | release首项窗前停止；updated不是首公开，未逐repo/PR扩池 |
| Tencent Hunyuan | [Research](https://hunyuan.tencent.com/research)web超时；子任务IAB省略visibility后34.7s超时/reset，root独立37.8s超时；官方HTML壳及一次公共bootstrap未恢复研究列表 | 必要当前目录有访问缺口，停止重复，不记零。接受官方带日期本窗完整列表/快照重开，不做代码考古；壳build日期非研究公开日 |
| Z.ai | [Research](https://www.z.ai/research)中文当前Aug26→Aug14→Jun16；[release notes](https://docs.z.ai/release-notes/new-released)Aug26→Aug18→Jun16 | 两当前dated入口窗前停止 |
| ByteDance Seed | [EN research](https://seed.bytedance.com/en/research)当前news与无日SeedRealtime原件Aug5；[EN papers](https://seed.bytedance.com/en/public_papers)Newest→oldest页1共20/242，Aug18→Aug12→Aug6→Jul23→May14；实际[中文research](https://seed.bytedance.com/zh/research)/[中文papers](https://seed.bytedance.com/zh/public_papers)同前段日期，中文SeedRealtime实际原件Aug5 | 当前双locale前段窗前停止，不扫13页、不外推全历史一致；默认无locale URL实际redirect EN，中文单独核过 |
| Baidu ERNIE | [blog首页](https://ernie.baidu.com/blog/zh/)web超时后官方HTML恢复May9→Apr30→Apr15→Feb6→Jan29；[publication](https://ernie.baidu.com/blog/zh/publication/)4项仅年份（2025/2026） | 当前news页1/2首旧停止；年份不证当窗日，不把4项做新版待办 |
| Xiaomi MiMo | [homepage](https://mimo.xiaomi.com/)Paper8有日最新Jun29→Mar13→Feb3→Jan8；Blog15标题无日。一次公共bootstrap route定点恢复前段tool-call-repetition Sep27；实际V2.6链接链[/mimo-v2-6](https://mimo.xiaomi.com/mimo-v2-6)→[官方article](https://mimo.xiaomi.com/mimo-v2-6/article)Sep22；[materials原件](https://mimo.xiaomi.com/mimo-v2-6-material-research)Sep21；code-long-horizon Jun10 | 当前前段均窗前，停止不授15个逐项候选或全目录零。先前猜/blog/mimo-v2-6失败不算有效材料；采用真实route/link链，日期有界恢复后不审窗外机制 |
| MiniMax | [EN blog](https://www.minimax.io/blog)及CN官方HTML当前13dated文章前段Aug13→Jul31→Jun9；[Agent techblog](https://agent.minimax.io/docs/techblog)Oct8→Sep22→Sep19 | Oct8 workflow完整核心实际读，root窄准入5分通过；必要owner差额/PRE继续。其余dated入口窗前停止 |

本轮不扫描每周来源、不新建Weekly。机构有限入口已到上述真实停止；随后root已实际Qwen载体具体EX独校准、MiniMax/OSS必要Source/PRE/actualPOST通过，机构分支当前普通待办0。Hunyuan/Qwen新研究目录为已有限穷尽的具名来源保证缺口，不据此声明全网召回或把arXiv普通未读外部化。root已完整核本记录的入口/停止范围及随后中文Seed/MiMo有限原件日期，不授整日Gate。
