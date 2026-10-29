# 2026-02-15 有限来源遗漏补查

作者：supplement_20260215。检查2026-10-08T16:06:21+08:00。
本次只补279现存2026 Daily中的本日；补充Feb14完整北京自然日，只按公开日期；原1候选、原09:00窗口、评分和连续原§4冻结。启动完整读取AGENTS/Research/Report/SOURCES使用+每日+arxiv、Prompt、ROADMAP/本日相关LS路由；未加载其他Daily/Weekly材料。

## 原件与入口

- [entry](supplement-entry-20261008.json)：14每日源首入口（Google两个），及arxiv公告政策。原始返回为JSON编码字符串，可按JSON文本打开；保留工具Source、URL、行号与错误，不把缺正文当已读。
- [west](supplement-west-20261008.json)：西方日期查询；Google Feb归档、Meta page3等入口。
- [east1](supplement-east1-20261008.json)：Qwen/DeepSeek/Kimi/Hunyuan日期查询（无搜索结果），及Google/ZAI/MiniMax目录位置。
- [east2](supplement-east2-20261008.json)：Seed/ZAI/ERNIE/MiMo日期查询、DeepSeek news、Seed public_papers page1、中英Forge。
- [tail](supplement-tail-20261008.json)：Meta/MiniMax/Moonshot/DeepMind有限query，中英Forge日期、Seed发布核心、HF作者身份。
- [calibration-original](supplement-calibration-original-20261008.json)：Meta Feb邻接全段、Qwen博客0行/仓库身份、Forge必要方法与原文链接。
- [recover](supplement-recover-20261008.json)：Google论文/ERNIE/MiMo/Qwen有限恢复，ERNIE日期段、Qwen迁站与AgentTechBlog。
- [准入校准包](supplement-admission-20261008.md)：旧First Proof、Seed2.0有效EX、Forge/Qwen潜在贡献与新Academy范围关闭。
- [冻结基线](supplement-baseline-20261008.md)：编辑前完整本日报，只用于原1行/窗口/原§4冻结比较，不另建候选账本。

## 查询原式与停止

每个query只处理返回的当日相关线索，不把搜索引擎日期筛选当官方公开日。第一批：

- site:openai.com/index/ "February 14, 2026"
- site:anthropic.com/research "February" "2026" after:2026-02-13 before:2026-02-15
- site:deepmind.google "February 14" "2026"
- site:research.google "February 14" "2026" training model

第二批：

- site:qwen.ai "2026/02/14" OR "2026-02-14"
- site:deepseek.com "2026-02-14" OR "February 14"
- site:platform.kimi.com/blog "2026-02-14" OR "February 14"
- site:hunyuan.tencent.com/research "2026-02-14" OR "02-14"

第三批：

- site:seed.bytedance.com "2026-02-14"
- site:zhipuai.cn "2026/02/14" OR "2026-02-14"
- site:ernie.baidu.com/blog "2026-02-14"
- site:mimo.xiaomi.com "2026-02-14"

第四批：

- site:ai.meta.com "February 14" "2026"
- site:minimax.io/blog "2026-02-14"
- site:github.com/MoonshotAI "2026-02-14"
- site:deepmind.google/blog after:2026-02-13 before:2026-02-15 model

有限恢复：

- site:research.google/pubs "2026-02-14" OR "February 14, 2026"
- site:ernie.baidu.com/blog/zh/ "2026年2月"
- site:mimo.xiaomi.com "February" "2026"
- site:qwen.ai/blog "qwen3.5" "2026"

返回后来/旧年日期结果不进入逐项题摘或全文队列；本轮未生成新的arxiv论文池。常规公告窗口完整处于美国东部周五/六，官方availability L172包括新稿、替换、撤回与交叉分类；不扩月目录或90日catchup。此政策不能证明作者其他平台没有发布。

分页/日期停止均在README§2自包含：OpenAI首面Sep22、Anthropic Sep4；Google Feb17→Feb11；Meta page3 Feb26→Feb13→Feb11（后续旧年不处理）；ZAI Feb21→Feb11→Feb2；DeepSeek Feb25→Jan28→Jan12；ERNIE Feb6→Jan29；MiMo Feb3→Jan8；Moonshot Overview最新Nov7 2025；MiniMax首面Forge Feb14→M2.5 Feb12→Jan27。Seed paper列表实际page1 1–20/242/Page1of13止May14，Next是纯文本不是可点击链接，未声称读到Feb段。原有效Seed2.0初筛可复用，当前June30 Model Card及April主页变化不倒灌。

Hunyuan动态列表：web Internal Error；按来源要求浏览器一次创建2026-10-08超时91.5167秒，错误明确自动审批未完成并允许一次重试；重试38.2212秒timeout/kernel reset。没有读到列表，未绕过审批/使用间接访问，不记0。旧V3有效11条列表和GradLoc公开字段保持有效复用。本輪新目录受阻与旧轮检查有效区分。

## 结论与恢复边界

新增确定候选0；原1/旧分数/审阅处置不变。旧有效Seed2.0排除复用，新增Academy清晰业务采用内容范围关闭，不评分。Forge/Qwen仍非确定窗内候选，不评分、不采用；其具体方法潜力不被主题模板关闭。只保留日期或重要变更的必要请求，不要求时分秒。

外部保留：原OpenAI/Anthropic/Google/DeepMind/Moonshot/MiMo历史段与Forge/Qwen；本轮新增明确记录Hunyuan动态审批故障、Seed Feb论文段及MiniMaxAgentTechBlog15行导航。恢复需要仅Feb14官方日期列表/归档，或Forge/Qwen准确公开日期/真实本日重要变更，不扩窗口/月份。保留项不支撑Coverage、候选、Books或零遗漏。

Books新写0；原First Proof处置复用，不需要共享owner写锁。作者扫描/筛选/写回已结束，待root非作者首包与六部分DAY复核；没有自授补查完成。

## 本地校验

进行中态V3通过；原窗口、原1候选行与连续原§4逐字比较通过；README的9个本地引用存在；本日限定unstaged/cached diff-check均通过（cached本日没有新变化）。首次校验曾因将原/新来源放为两张重复ID表失败，原因已定位并合为每源一行；旧源事实完整保留在冻结基线/V3_NOTES，不影响候选与原§4。机器检查不替代语义复核。
