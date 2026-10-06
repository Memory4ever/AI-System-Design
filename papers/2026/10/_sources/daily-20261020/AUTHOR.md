# 2026-10-20 Daily 作者：当日原始检查

作者 `daily_20261020_author`；独立复核者 root，本文不代签。
窗口为北京时间 2026-10-19 自然日，抓取启动 2026-10-20 09:21 +08。
仅写本日 README 与本目录；不写 Books，不续历史、不补 Weekly，不 stage/commit/push。

## 入口与方法

本日重新完整读取 AGENTS、研究合同、Report 合同、Prompt、每日来源与 arXiv 路由、ROADMAP。
采用 daily-research-closure 的来源、准入、证据、Books 和最终验收分层。
`fetch_sources.py` 首轮按清单顺序依次获取13机构（Google双入口），后续仅有限官方备选及已知条目日期恢复；每请求15秒，未无限重试。
每个 `*.request.json` 独立保存请求时刻、实际 URL、状态及错误；`*.raw.html` 为响应实体，扩展名不保证实际为HTML；`*.visible.txt`是机械提取，不等于已审全文。
arXiv交给独立单日助理，不重复整月或整类扫描。昨日材料只用来恢复公开URL/解析方式，未复用昨日覆盖结论。

## 第一批来源与停止位置

| ID | 实际入口与停止依据 | 目前结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research403；官方RSS原件1300项，逐pubDate转Asia/Shanghai，Oct19唯一“Advancing coding in low-resource programming languages”，最新Oct19 12:00GMT | 该RSS已检查；正文HTTP403但web成功读取全文核心；不能以RSS担保所有渠道 |
| SRC-ANTHROPIC | Research Publications首10实际日期Oct16至Oct8，停See more前 | 本页无Oct19；quantum circuits明确科学应用不扩正文 |
| SRC-GOOGLE-AI | DeepMind研究总览+Blog首6个Oct卡；Google Research Blog首屏最新Oct16；出版目录重试200但仅年份/页码 | Blog有限范围已检查；出版目录不证明日覆盖。5个相关Oct原页web日期为Argon/安全/机器人Oct13、EmbeddingGemma2 Oct6、scam Oct14，antimicrobial明确AI for Science不追日期 |
| SRC-META-AI | Research静态响应61字壳；官方Blog Latest News与Posts首10，最新Jul27，停Next前 | Blog有限页已查；Research独立论文目录保留覆盖缺口，不拿Blog替代全目录 |
| SRC-QWEN | 旧GitHub blog首5最新Sep23 2025；新Research静态4字，web0行 | 动态Research覆盖受阻；三具体空模板ID见下，均不算研究身份/日期证据 |
| SRC-DEEPSEEK | 主页产品导航→官方ChangeLog，首项Oct17下接Sep10 | 无Oct19事件；近邻V4.1-Flash1017不搬日期，不复查性能正文 |
| SRC-MOONSHOT | Platform Blog首屏最新Nov7 2025，全部可见26；GitHub API rate-limit403，网页EOF | 新研究GitHub子范围未覆盖；What'sNew URL误拼404已识别，改正确公开路径继续，不拿404封口 |
| SRC-TENCENT-HUNYUAN | Research静态4字，web0行；GitHub首10/88按Last updated，Hy-Memory/UniRL显示Oct19更新 | 更新时间不是公开事件；Research“全部”未获得动态列表，独立覆盖保留，不把壳推零或更新当release |
| SRC-ZAI | Research“全部/时间排序”首15实际从Aug26至Dec9 2025，停查看更多前；HTTP与web一致 | 首批无Oct19，不扩旧页 |
| SRC-BYTEDANCE-SEED | Research featured Blog5从Aug5向前；Public Papers首1/13页标1–20/246，实际18题名日期从Sep28至May26 | 显式Newest→oldest到窗前停止，不遍历246；/en/blog返回空壳但非有效Blog覆盖依据 |
| SRC-BAIDU-ERNIE | 官方Blog首页首10最新May9至Nov21 2025，停下一页2/2前 | 首页无Oct19，不扩旧页 |
| SRC-XIAOMI-MIMO | Paper8项最新Jun29；Blog首15没有日期，正在对14个非明确科学应用项重新取实际原页日期 | 普通日期待办，未宣称已完成或外部受阻；第3项新材料研发明确范围外 |
| SRC-MINIMAX | Research首13最新Oct19 M3.1 Flash，次Aug13，末Oct27 2025；Agent Tech Blog完整3条，正在核日期 | 本窗1新发布，核心完整读后拟贡献排除（非访问受阻） |

## 准入校准请求 A1

OpenAI本窗新事件拟准入：跨语言长程编码容易受接口差异干扰，MultiLangBench通过数据库产物/SQL共同验收；另将COBOL迁移的行为保持与新软件功能构建区分。若成立，改变的是评价契约和成功定义，不是由排行榜证明训练机制。建议2+1+2=5标准审阅；root尚未返回准入，不提前写标准完成。

MiniMax M3.1 Flash：本日官方发布已核日期，完整核心唯一推理机制说明为更激进稀疏，但没有稀疏具体形式、HW、batch/concurrency、SLO、精度或质量匹配对照；其他为榜单、价格与吞吐宣传。拟排除长期贡献，不评分、不Books，等待root校准。

代表排除供root分层抽检：Anthropic quantum circuits、DeepMind antimicrobial、新材料MiMo为明确AI for Science；DeepSeek Oct17为窗外发布；Meta Genesis为科学应用且窗外。标题清楚者按合同停止，不做全文队列。

## Qwen具体恢复（只作缺口，不列候选）

定向发现查询 `site:qwen.ai/blog "2026/10/19"`；首页返回3个具名空模板：
`https://qwen.ai/blog?id=qwen3-8-omni-flash`、`https://qwen.ai/blog?id=qwen3.8Bloomberg`、`https://qwen.ai/blog?id=99f0335c4ad9`。
搜索抽取都只有2026/10/19、undefined minute、0 words；对三个精确原URL分别web open均0行。
模板日期与slug不能建立研究身份、贡献或首公开日期。保留动态Research及这三个ID，不支持候选/Books/“零发布”。恢复条件是原域可读标题/完整核心与实际公开日期；不无限逆向猜API。

## web实际原文定位（辅助HTTP受限，不继承历史）

- OpenAI [官方正文](https://openai.com/index/low-resource-programming-languages/)：Oct19；§1共同数据库验收接口，§2 COBOL隐藏测试输出等价及仍需专家/业务规则测试。HTTP403不否定web实际可读原文。
- Google [Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)、[安全](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)、[机器人](https://developers.googleblog.com/gemini-4-argon-for-robotics/)均Oct13；[EmbeddingGemma2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)Oct6；[scam](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)Oct14。只确认日期，不将窗外全文内容纳本日证据。

## 未完

普通可执行：MiMo14日期恢复、Moonshot正确What'sNew、OpenAI准入后必要artifact与具体Books判断、arXiv汇合、报告六节、root独核。
外部覆盖子范围暂保留：Meta Research、Qwen动态、Hunyuan动态、Google publication日级、Moonshot GitHub。尚未经过root日级验收，不把这些全部称终态。

## 恢复后的有限差额（oct20_author_resume，2026-10-20）

重新实读本日AGENTS、Prompt、研究/Report合同、来源使用说明与每日组、ROADMAP及相关checkpoint；当前root明确限定仅Oct20 Daily，历史不续。沿用daily-research-closure分层，未继承任何旧完成声明。本作者仅own本日README/本文/机构原件，不写Books、Learning State或ARXIV文件。

1. **MiMo日期普通待办已完成。** 实际顺读14个非明确科学应用原页的日期：`mimo_tool` Sep27 2026、`mimo_v26` Sep22 2026、`mimo_horizon` Jun10、`mimo_speed` Jun8、`mimo_inference` May30、`mimo_asr`/`mimo_tts25` April 2026（原月精度，未补日）、`mimo_pro25` Apr27、`mimo_25` Apr22、`mimo_pro`/`mimo_omni`/`mimo_tts` Mar18、`mimo_hss` Dec22 2025、`mimo_flash` Dec16 2025。全部在窗前，不读窗外机制全文作为本日贡献。Sep27工具重复纠错信号保留窗外身份，不将其当无纠错或搬入Oct19。Paper8项与Blog15首屏、More前为实际停止位置；非全站遍历。
2. **Moonshot错误路径已排除，正确原页已检查。** `kimi_correct.request.json`确认`https://www.kimi.com/code/docs/en/kimi-code/whats-new.html`在01:31:29UTC起请求200，实读正文首段最新Desktop1.1.0/CLI2.2.0均Oct14 2026，随后已至Sep。没有Oct19。本页不能替代GitHub研究目录；后者403/EOF缺段继续保留。
3. **MiniMax Agent Tech Blog3日期已完成。** 实读原件完整入口：Oct8、Sep22、Sep19 2026，无Oct19，不扩旧文。M3.1 Flash原文全核心实读及root准入排除通过；未评分、不Books。
4. **准入校准root已返回。** OpenAI实际2+1+2=5准入；MiniMax稀疏未披露具体形式/配置排除通过。已完成层不重做。其它排除仍需按Report合同独立分层抽检，不自签全部通过。
5. **OpenAI标准证据范围已完成（待独核）。** 本作者经web实际顺读官方文章核心§1–2与限制，及`openai_multilang_artifact.raw.html`完整README。后者读取URL为`https://raw.githubusercontent.com/openai/MultiLangBench/main/README.md`，请求200、3282bytes；是读取时main而非历史commit核验。SQLite3.40.1、TCL51k可转换24k、默认哈希前缀272tests、60s超时、目标语言拒绝、环境清除SQLite及无网、input DB→candidate query→realSQLite validation契约均实读。未运行runner/测试/复现；COBOL隐藏测试未公开，不授生产等价保证。官方性能未做独立复现，采评价契约，不用排名归因训练机制。
6. **先交付有效可读报告。** 本日六节README已建立“进行中”，机构1候选，arXiv计数明确待汇合；OpenAI具体Books比较/独核普通待办，不将其伪装外部受阻。动态源缺段单独隔离，不支持候选或无遗漏。作者未写任何Books。

剩余普通：root提供arXiv汇合包与OpenAI具体Books决定，合入六节并由非作者独核、机械校验。外部覆盖保留项继续以README §5为当前自包含恢复入口，不以昨日覆盖代替。

### 机构slice交接

root随后实读OpenAI artifact全文及Ch66实际688/702/1895附近，独立通过5分标准审阅与具体已有覆盖：从规格构建不继承bugfix排名；跨语言固定语义并在真实目标语言/库版本独立执行；SQL结果语义/NULL/timeout/执行引擎归评价合同。本作者实际读回相同局部，README §1/3/4/5/6已同步，不写Books。初稿V3通过，README/AUTHOR ownership现释放给root；完整日报独立验收未通过，不预支动态源全覆盖。下一slice转ARXIV_MULTIMODAL.md/mm_assets，与机构完成层分开。
