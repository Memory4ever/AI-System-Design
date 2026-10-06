# 2026-01-01 Daily：增量来源补查

作者：supp_jan01。执行日期：2026-10-07（Asia/Shanghai）。独立复核：待 root。

## 范围与约束

本次仅补查本日报前一完整自然日 **2025-12-31 ～ 2025-12-31**。用户授权保留原日报窗口、已有候选、原归属、评分及有效审阅；旧完成状态不代表本轮已验收。本文件为原始补查与交接，不修改 README、Books、Learning State，不 stage/commit/push。

启动重读 AGENTS.md、CODEX_RESEARCH_PROMPT.md、两份研究/Report 合同、来源使用说明和每日分组、ROADMAP、本日 README 与本日原始目录；Books 比较另读 Project Context、Learning Philosophy、Writing Guide、最新相关 checkpoint、Ch17 当前相关正文及 Ch16/18 交接。按当前合同仅判断公开日期；官方日期标签可用，不补造时刻，arXiv Submitted/Updated 仍不等于 public。

本輪重查当前原始入口并重新解释可核原始日期切片，不继承旧“零命中”结论；未把全年目录、跨类列表或搜索命中变成逐项深审队列。旧原始记录保留，下表明确哪些实时重查、哪些复用其原字段/目录观察。

## 14 个每日来源：实际入口与停止点

搜索均为一批结果、未分页。目标只限定模型/学习/多模态、训练推理系统、平台可靠性与 Agent 机制，不扫描暂缓 AI for Science 或每周源。

| 来源 | 本轮实际原始切片与停止点 | 结果及限定 |
| --- | --- | --- |
| SRC-OPENAI | 实时打开 [Research](https://openai.com/research/) 首屏；RSS 本轮网页读取不支持 text/xml、直接读取 403。重新核 [institution-date-recovery.jsonl](./institution-date-recovery.jsonl) 的官方 RSS 原字段：1243 个 metadata 的相邻记录为 Dec22 00:00 GMT → Jan2 10:00 GMT；只重判这对邻接所界定的 Dec31 日期切片，不读全年正文。目标日期搜索见下节。 | 有界目录已检查；Dec31 不在现存原字段相邻事件中。实时 RSS 刷新受限，不把当前首屏或搜索空值当零事件证据；若补查必须采用更新后的历史 RSS，可用官方 Dec31 dated export 定点替代。 |
| SRC-ANTHROPIC | 实时打开 [Research](https://www.anthropic.com/research) 当前页；直接 HTML 刷新 403。重新核同一 jsonl 的 174 个 publishedOn 原字段，目标邻接 Dec19 19:45Z bloom → Jan8 00:00Z critical-infrastructure-defense，无跨 Dec31 日界记录。 | 原字段有限日期切片已检查，不由当前页面推广全机构覆盖；embedded metadata 刷新受限但已有相邻日期可核。 |
| SRC-GOOGLE-AI | 实时打开 [DeepMind Research](https://deepmind.google/research/) 当前首屏（最新九月研究/科学混排）和 [Google publications](https://research.google/pubs/) 默认列表（2025 年计数677），停在这两个入口；另目标日官方域第一批搜索。 | 当前有界入口已检查；默认出版列表无 Dec31 日级批次，历史 Dec31 模型/系统事件目录仍未恢复，不将科学混排扩池。 |
| SRC-META-AI | 实时打开 [Research](https://ai.meta.com/research/)，抽取0行；目标日期官方域搜索仅出现作者主页含2022年Dec31、2025其他日期条目，未形成当日列表。 | 原始入口受阻；缺 Dec31 模型/训练/推理/Agent 研究切片，0行不是0论文。 |
| SRC-QWEN | 实时打开 [旧博客](https://qwenlm.github.io/)：首屏最新Sep23，指向新站；[新站 Blog](https://qwen.ai/blog)抽取0行。目标Dec31搜索一批；复用 [institutional-preclosures.md](./institutional-preclosures.md) 指定的 Qwen-Image-2512 完整 card 核心及原日期标签。 | 新站目标历史目录受阻。具体 card 已有效排除：画质/文本更新未披露改变长期机制的增量；不因缺时刻重开日期，不重复评分。 |
| SRC-DEEPSEEK | 实时 [News](https://www.deepseek.com/news/) 研究索引10项，停于可见列表；目标邻段 Jan12 Engram → **Dec31 mHC** → Dec2 V3.2。定点打开 [mHC exact-v1](https://arxiv.org/html/2512.24880v1)完整题摘与必要 §3–5；停止于与已有采用命题直接有关内容。 | 已检查；官方 Dec31 日期可采用，旧日期 hold 解除。mHC 已在 Jan02 有有效同事件审阅，跨日报去重复用，不新增/不评分/不移动。 |
| SRC-MOONSHOT | 实时 [Blog](https://platform.kimi.com/blog) 26条，最新Nov7/6，末条2024-05-29，无下一页；复用本日 preclosures 中官方 CLI changelog Dec29 v0.69 → Dec31 v0.70 → Jan4 v0.71/72 核心。 | 有界列表已检查，CLI0.70仅输出选择/video输入能力，不改变执行/推理机制或可靠性判断；有效贡献前关闭复用，不评分。 |
| SRC-TENCENT-HUNYUAN | 实时 [Research](https://hunyuan.tencent.com/research) 抽取0行；浏览器创建核查30秒超时。复查 [hunyuan-directory.md](./hunyuan-directory.md) 真实“全部”11项浏览器观察，2026-09-22→02-03，无旧分页；目标日官方域搜索一批。 | 历史Dec31原始切片仍受阻。已有11项不是本日论文队列，也不是2025年末目录；缺官方目标日历史目录/API或具名当日原文。 |
| SRC-ZAI | 实时 [Research](https://www.zhipuai.cn/zh/research)可见15日期项，Jan19/13 → Dec10/9，停于“查看更多”；不声称其后已读。目标日期官方域搜索一批。 | 已检查当前有界研究页及日界邻段，未见Dec31条目。只声明该切片；“查看更多”不扩张为全站待办。 |
| SRC-BYTEDANCE-SEED | 实时官方 API `get_article_list_v2?article_type=1/2&publish_year=2025&count=20&page_token=0&order_desc=true`，header `x-tt-locale: US`。两类实际各18项，has_more=true、next_page_token=20；日期顺序已到June，顶项论文ID1323 PublishDate=1765728000000（北京时间Dec15），博客ID2141=1766505600000（北京时间Dec24）。停在token0，已越过Dec31向下边界，不为has_more遍历全年。2026侧仅复查本日 [API原字段](./seed-api-date-slice.jsonl) token0正序邻接Jan20论文/Feb12博客。 | 目标目录切片已检查，未见Dec31事件。UTC转换Dec14/23不是官方北京日期，采用原字段及目录口径；不将PublishDate造为首公开秒级时刻。 |
| SRC-BAIDU-ERNIE | 实时 [Blog](https://ernie.baidu.com/blog/zh/)10项，Jan8 → Dec23/9 → Nov21；停于下一页2/2链接之前，当前已跨目标日；目标日官方域搜索一批。 | 当前有界日期切片已检查，未见Dec31条目；无需为更早分页扩扫正文，不宣称已删除事件不存在。 |
| SRC-XIAOMI-MIMO | 实时 [Paper/Blog](https://mimo.xiaomi.com/)完整可见Paper8标题及Blog15标题，Paper Jan8 report → Oct21 router-RL，停在当前列表；Blog多数无日期，目标日官方域搜索一批。 | Paper有界日期切片已检查。无日期Blog无法定位Dec31，保留具体日期目录限制，不将其内容或标题列成候选，不索要逐篇无关文章的时刻。 |
| SRC-MINIMAX | 实时 [Blog](https://www.minimax.io/blog)当前可见列表（Aug13→Jan27→Dec23→Oct27），目标日英文/中文官方域各一批搜索；实际命中均为2026财报引用Dec31会计期。停在当前页与搜索首批。 | 当前研究Blog有界日界切片已检查，无Dec31条目。财报期不是研究公开日，范围关闭；不由搜索结果外推历史完整性。 |
| SRC-ARXIV | 复查本日 [holiday原始依据](./arxiv-holiday-date.md)：Dec30 ET无新投稿公开公告，下批Dec31 20:00 EST=Jan1北京日期；因此新增扫描自然日Dec31无scheduled新稿批次。原文实时两次抓取失败（429/内部错误），[availability](https://info.arxiv.org/help/availability.html)实时可读，确认Submitted≠public。定点重开旧两项revision日期：TTT-E2E v2、KernelEvolve v2 abs；同时复查 [screening](./screening.md) 四主题 start0/max150缓冲与既有完整题摘身份，仅作为先行原文/修订线索，不全分类逐项关闭。 | 新稿公告日期边界可复用已核的实际假期原始证据，不是只靠一般周表。具体两项revision的实际public日期仍缺，不以版本号、Submitted/Updated或文件大小判断实质修订。 |

## 本轮搜索原始范围

全部为2026-10-07执行，一批即停。查询的日期表达不是准入证据；以官方原文日期和题摘贡献判定。

- Google：`site:deepmind.google "December 31, 2025"`；`site:research.google "December 31, 2025" language model`。
- Meta/Qwen：`site:ai.meta.com "December 31" "2025"`；`site:qwen.ai "2025/12/31"`；`site:qwen.ai/blog "2025/12/31"`。Meta结果为其他年份/其他日期作者页，Qwen无可确认目标条目。
- Hunyuan/ZAI/ERNIE/MiMo：分别 `site:hunyuan.tencent.com "2025-12-31"`、`site:zhipuai.cn "2025/12/31"`、`site:ernie.baidu.com/blog "2025-12-31"`、`site:mimo.xiaomi.com "2025-12-31"`。返回空批次，非零事件证明。
- Moonshot/Seed：`site:platform.kimi.com "2025年12月31日"`；`site:seed.bytedance.com "2025/12/31"`。无可确认目标事件，具体CLI/API分别按上表处理。
- MiniMax：`site:minimax.io/blog "December 31, 2025"`；`site:minimaxi.com "2025-12-31"`。财报/招股材料以目标日为会计期、正文为2026发布，不属研究机制贡献，不扩展财务审阅。
- OpenAI/Anthropic/DeepSeek：`site:openai.com "December 31, 2025" research model`；`site:anthropic.com "December 31, 2025"`；`site:deepseek.com "2025 年 12 月 31 日"`。OpenAI结果漂移至Community：图像示例、个人多模型经验、role-aware数据库中间层经验、podcast提案均不是OpenAI Research公开事件；未提供新的原始研究/受控设计证据，不据此扩池。DeepSeek采用原始索引，不以检索片段证明日期。

## 日期 hold 解除与跨日报去重：mHC

本轮实时官方索引保留原始日期字段 **“2025 年 12 月 31 日”**，按当前合同使用官方公开日期，无需时区/时分秒。这解除旧本日“缺官方首公开时区/区间”的 hold；不声称arXiv也在Dec31公告，也不捏造官方先行秒级时间。

家族 `SF-2026-ARXIV-2512-24880` 已在 [Jan02候选及§4](../../02/README.md)以同一 `2512.24880v1` 完成深入审阅与整合。本轮只定点复核身份、采用命题和未决边界，没有重评原 `2+2+3=7`。mHC完整题摘明确的约束增量为：多流HC混合改变carry传播→双随机约束与执行优化→重新区分局部carry守恒和整网稳定；准入不靠机构名或主题关联。

证据核对止于v1 Intro Eqs3–4、§3.2、§4.1–4.3、§5.1–5.4；没有可见撤回/纠错标记，不宣称全版本史无标记。理论carry条件不等于任意向量identity或完整Jacobian保证；20轮投影近似须保留跨层误差。作者3B/9B/27B MoE、n=4、context4096只支持其受限预训练比较；未复现实验，不把6.7%外推为普遍代价。

Books **No Change / 已有覆盖**：唯一owner `MODEL-TRANSFORMER-LAYER`，Ch17“多流混合还要保留哪些几何约束”正文452–469已有read/carry/write、均匀方向/流均值、矩阵乘积封闭、差异方向可收缩、完整Jacobian及有限Sinkhorn/I/O边界；Review notes 的同家族736行保存精确版本及条件。相邻Ch16/18的接口仍一致。无需为解除报告日期hold重写相同知识；不新增Books产出或搬移Jan02原候选。

本日补查新增候选 **0**；去重复用已审家族 **1**；重评分 **0**；Books写入 **0**。两项revision日期未确定，不计候选或完成审阅；上述计数不是所有旧宽列表的筛选分母。

## 精确外部保留项

1. Google、Meta、Qwen、Hunyuan目标日目录：上表具名入口不能恢复Dec31模型/系统研究切片；替代为对应官方日期列表/API、发布批次，或具名当日原稿。只重开目标机构Dec31切片，不要求证明整个机构无隐藏/已删除文章；当前有限入口检查不支持“全机构无遗漏”。
2. MiMo无日期Blog：缺目标日官方日期目录或具体相关文章的官方公开日期；只有出现具体贡献线索才定点补摘要/正文，不把15条无日期标题转成全文队列。
3. [TTT-E2E 2512.23675v2](https://arxiv.org/abs/2512.23675v2) 与 [KernelEvolve 2512.23236v2](https://arxiv.org/abs/2512.23236v2)：本轮原页分别仍为Submitted/revised Dec31/Dec30；需要该精确revision的官方实际公告日期或作者公开记录，且出现实质变化时才审其delta。metadata、版本号、same-size不足以确认落窗或重要性。未确定事件不评分、不用其性能作正面证据、不进Books。若证据到达仅重开其受影响版本/日期。原两项hold保留，不冒称已处理修订。

一般“是否还有所有作者先行镜像”不是新增具体材料请求：没有具名线索时不为穷尽性扩扫。mHC旧日期hold已解除，不再请求其精确时刻。

## 可直接并入 README 的补充文字（交 root）

开头增加：

`**窗口说明：** 用户授权仅补遗漏；保留原窗口、已有候选、原归属、评分和有效审阅。`

`**补充窗口：** 2025-12-31 ～ 2025-12-31`

§1增加：

> 2026-10-07 增量补查已检查每日14个来源的有界官方目录/目标日期切片和实际搜索停止点，未扫描每周源；新增候选0、跨日报有效审阅去重复用1、重评分0、Books写入0。[补查依据](../_sources/daily-20260101/supplement-20261007.md)区分实时入口与可核原字段复用，列明无法恢复的具体历史目录和两项revision日期。mHC官方研究索引明确标2025-12-31，按当前日期合同解除旧时区/时刻hold；同一精确v1已在[Jan02](../../01/02/README.md)深入审阅并整合到MODEL-TRANSFORMER-LAYER，依用户授权保留其原候选与归属，本日不重复列为候选、评分或书稿产出。

§4增加：

> 补查采用DeepSeek官方日级公开标签，而非arXiv提交日期；这是一项日期口径缺口解除，不改变已有mHC研究结论。Ch17“多流混合还要保留哪些几何约束”具体承载read/carry/write、理想carry守恒不等于任意identity/整网稳定，以及有限Sinkhorn和执行成本边界，故本次Books为已有覆盖/No Change。旧原始证据保留，Jan02精确版本审阅及原评分不移动、不重做。

§5注明：

> 旧mHC精确时区/时刻请求已被本轮官方公开日期证据解除；其历史说明保留为旧口径记录，不再作为当前阻塞。现存外部保留项以补查原始记录“精确外部保留项”为准：不能恢复的具名目录与两项revision公开日期，不用于候选、Books或无遗漏断言。没有具名线索的所有先行镜像不再形成穷尽性请求。

作者仅提交有界扫描、去重与Books比较供独立审查；**未自授本轮完成/验收**。root应独核mHC官方字段、Jan02同版本及Ch17具体承载、14行检查边界、代表性排除与外部限制，再决定落README与复核结论。
