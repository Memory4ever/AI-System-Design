# 2026-03-03 V3 来源与准入停点

作者：mar03_v3。检查时间：2026-10-01T12:19:40Z。窗口固定为2026-03-02T09:00:00+08:00～2026-03-03T09:00:00+08:00，含左不含右。
已完整重读AGENTS、三个研究权威合同、CODEX_RESEARCH_PROMPT、ROADMAP和LEARNING_STATE顶部本轮checkpoint。未读取Weekly；旧候选、评分、EffectiveDate豁免、日程推定的零命中不复用。旧原始HTML/XML仅作身份与可核实原文线索，旧报告保存在[V3_LEGACY_REPORT.md](./V3_LEGACY_REPORT.md)，其旧Gate不支持本次状态。

## 一、有限来源范围与停止位置

十四个每日来源均有实际入口动作。未扫描每周或未经触发的按需来源。以下“无本窗确定候选”不是全源零命中证明；历史日期/目录限制在正式日报隔离。搜索只辅助发现，不授正文或日期权限。

| 来源 | 实际入口/检查段 | 有限结果与停止点 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)当前页；定点官方域搜索 `"March 2, 2026" research model` 和Mar03同义表达 | 当前页不恢复March历史cursor；搜索找到GPT-5.3 Instant System Card，已读HTML§3.1/PDF pp.1–3，保留日期冲突。公司“Department of War agreement update Mar02”非模型训练/系统机制，标题已明确范围外，不跟进协议全文。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)首屏与Publications当前十条至Aug28；official-domain `"March 2, 2026" OR "March 3, 2026" model training` | 日期主题查询没有返回相关本窗原始发布；首屏不是历史穷尽，March研究段保留具体目录限制，未以旧September收据证明无命中。 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)、[Research pubs](https://research.google/pubs/)当前页、[model cards](https://deepmind.google/models/model-cards/)，两日期+language model查询 | modelcards明确Flash-Lite Mar03，读其官方card核心和发布blog。Research pubs条目仅2026年份不能分派本窗，不把当前全年列表变为论文队列；历史主题段限制保留。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)当前入口；两日期官方域主题检索 | 页面正文0行，检索无本窗官方线索；不能授研究段覆盖通过，隔离历史可读目录缺口。 |
| SRC-QWEN | [旧blog](https://qwenlm.github.io/)首页至2025Jul24，迁移提示到[新blog](https://qwen.ai/blog)；[Qwen Code Mar03](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-03-03/)核心；[模型官方repo](https://github.com/QwenLM/Qwen3.5)News；9B/2B官方card | 旧首页非March目录；新blog0行。Mar03 Code汇总与四个PR原始行为/日期已定点关闭；News明确Mar02四个小尺寸发布，完整读9B/2B核心说明、Overview、相关语言/视觉表后关闭贡献。不要把4型号算4家族。未重扫HF平台。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)、[updates](https://api-docs.deepseek.com/updates)；两日期官方域查询 | updates web超时后curl取得完整可读日期段，2025Dec01→2026Apr24之间无条目，故这个官方更新日志段已检查；其他未公开研究不作无遗漏断言。 |
| SRC-MOONSHOT | 先读[platform旧blog](https://platform.kimi.com/blog)完整Overview至2024May29、官方GitHub身份与两日期查询；后读root的[官方新Research目录恢复](../V3_OFFICIAL_DIRECTORY_RECOVERY.md)，原入口[www.kimi.com/en/blog](https://www.kimi.com/en/blog/) | 新Research可见19条完整到2024/06/26Mooncake，无可见未完成分页。限定本日对读，邻接Feb09 Agent Swarm与Apr20 Kimi K2.6均窗外，没有March条目。撤回因旧platform停于2025而保留的必要Research缺口；仅授当前可见目录段，不授全机构历史保证。 |
| SRC-TENCENT-HUNYUAN | [官方Research首查](https://hunyuan.tencent.com/research)web0行；CUA；两日期官方域及官方GitHub主题检索；随后读root的[官方JS/API目录恢复](../V3_HUNYUAN_LIST_RECOVERY.md) | CUA有限恢复失败后未重复扩站；root从页面实际JS恢复publicList，renderType0,page1,size20返回total11、11/11。独立对读本日窗口，相邻display为Feb13 RLVR clipping与Apr23 Hy3 preview，均窗外；当前publishedAt也无March值，但二字段不能当首公开互替。当前有限“全部”目录已检查，不再保留动态入口终态阻塞，也不授全机构历史无遗漏。 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)“全部”时间排序当前页；两日期官方域检索 | 可读条目跨Mar15 GLM5Turbo→Feb21 GLM5报告，已检查这个邻接日期段无Mar02/03条目；不点击“查看更多”扩入更早年份，不授全站研究无遗漏。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)当前Blog/Publication；[public_papers](https://seed.bytedance.com/en/public_papers)1–20/242、Page1/13；两日期+Seed主题检索 | Research出版可读段Apr11→Jan27无Mar02/03；public_papers第一页截止May14，动态Next page无可复查历史链接，未遍历13页。搜索只恢复Feb14 Seed2.0、Feb13 Seedream，明确窗外；March论文历史分页缺口隔离。 |
| SRC-BAIDU-ERNIE | [技术blog](https://ernie.baidu.com/blog/zh/)当前页；两日期+language model官方域检索 | 可读日期段Apr15→Feb06无Mar02/03发布；无相关修订信号，不跟进其他月份；该博客日期段已检查。 |
| SRC-XIAOMI-MIMO | [Paper/Blog主页](https://mimo.xiaomi.com/)Paper列表；[官方GitHub](https://github.com/XiaomiMiMo)身份入口；两日期+MiMo/attention检索 | Paper相邻条目Mar13 ARL-Tangram→Feb03 HySparse→Jan08 V2Flash，无Mar02/03；Blog不能恢复历史日段，论文目录已检查但Blog子入口限制隔离。 |
| SRC-MINIMAX | [Research Blog](https://www.minimax.io/blog)可读列表，至2025Oct27；两日期官方域主题检索 | Mar18 M2.7→Feb14 Forge→Feb12 M2.5邻接跨过本窗。搜索只找到邻月与后续材料，不纳入本窗，不扫News商业活动。 |
| SRC-ARXIV | [March cs月表](https://arxiv.org/list/cs/2026-03)1–50标题补检；[February尾页](https://arxiv.org/list/cs/2026-02?skip=13900&show=50)13901–13905；官方advanced/availability；4组主题搜索；四项exact-v1题摘 | 月表不能授daily批次。只核相关命名机制，不关闭全分类库存。三项潜在贡献日期隔离；DUEL由Submitted与公告下界排本窗，不再日期隔离。另保左端公告槽位/跨月身份缺口，见下文。 |

本次arXiv主题查询为四组：
1. `site:arxiv.org "March 2 2026" ("language model" OR Transformer OR MoE OR "reinforcement learning")`，对应cs.CL/LG训练/模型主题；
2. `site:arxiv.org "March 2 2026" ("multimodal" OR "world model" OR "vision-language-action")`，对应cs.CV/RO；
3. `site:arxiv.org "March 2 2026" ("LLM" OR "GPU") (kernel OR compiler OR parallel OR memory OR serving)`，对应cs.DC/AR/PL/OS/PF；
4. `site:arxiv.org "March 2 2026" ("agent" OR "retrieval" OR "tool") ("language" OR "LLM")`，对应cs.AI/IR/MA。
结果只出现窗外EXO-200数据发布（领域科学应用且Sep28），不作为本窗原文命中。搜索首页不足以支持召回；本次没有“12分类全量完成”的断言。

## 二、首批负侧校准与关闭理由

root非作者已批准Qwen Code与小尺寸Qwen两个关闭判断；未在准入前给分。Gemini初读产品机制的整家族negative在安全尾部补读后已撤回；root批准窄安全评价边界潜在贡献，见§三。此改判源于实际负向证据与比较条件，不是“safety标签”自动入选。

### Qwen Code Mar03产品汇总

已读全部核心功能/Important Fixes；明确修复信号没有因标题而跳过。四项定点API原始元数据：
- [#1756](https://github.com/QwenLM/qwen-code/pull/1756)：raw MCP client/onprogress→TUI/SDK progress；created Feb08T07:48:53Z，merged Feb11T03:07:21Z。
- [#1791](https://github.com/QwenLM/qwen-code/pull/1791)：识别TPM错误后固定1min重试；created Feb10T15:51:54Z，merged Feb13T09:34:05Z。
- [#1825](https://github.com/QwenLM/qwen-code/pull/1825)：per-round AbortController与单个外部取消转发，避免多轮listener累积；created Feb12T15:26:21Z，merged Feb13T13:39:02Z。
- [#1796](https://github.com/QwenLM/qwen-code/pull/1796)：Promise.race解除ESC后的slash-command等待链、非“后台工作已cancelled”保证；created Feb11T03:29:59Z，merged Feb27T13:32:13Z。

原始接口/修复早于本窗。Mar03网页为旧功能汇总，不产生第二次首公开或重要修订；Insight/session analytics、clipboard、node-pty→xterm→Playwright截图为工具集成说明，未给新增可靠性条件或评价边界。关闭本次事件，不声称这些历史修复没有长期价值，也不冒充历史论文已审去重。

### Qwen3.5小尺寸发布家族

[官方repo News](https://github.com/QwenLM/Qwen3.5)当前重定向Qwen3.8，仍保留2026-03-02 News，9B/4B/2B/.8B为一个尺寸发布家族。已读[9B](https://huggingface.co/Qwen/Qwen3.5-9B)与[2B](https://huggingface.co/Qwen/Qwen3.5-2B)官方card核心：
Overview给dense FFN、3×GatedDeltaNet+1×GatedAttention层比例、MTP、context与参数；2B建议原型/定向微调。Highlights沿用Qwen3.5家族设计，不能把通用MoE宣传套到dense FFN。
表格有不同模型/Thinking与NonThinking质量分，但未给同预算架构反事实、资源测量或尺寸下hybrid失效/成立新边界；因此新artifact+参数/score不足以建立本次稳定知识增量。贡献关闭，不把HF createdAt/lastModified当public日期；未实施推理、未复现benchmark。

## 三、具名日期保留，不纳入候选分母

### Gemini 3.1 Flash-Lite：负侧补读后改判

[官方card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/)Model Information/Data将机制指回Gemini3Pro；[发布blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)价格/速度、thinking旋钮与质量表本身未建立可归因设计边界。这只关闭产品性能命题，不能覆盖安全尾部。
实际补读Ethics and Content Safety的评价定义与限制：内部自动content-policy测试相对2.5Flash-Lite的image/text/multilingual项分别-21.7%/-1.18%/-1.84%；官方称这是性能绝对百分比变化，并非原始违规率。flag人工抽查多为误报或非严重内容；独立人工红队描述相对2.5Flash相近或改善（基线不是2.5Flash-Lite），child-safety达到内部launch门槛。由于查询集与自动误报/漏报判定改进，当前结果不能与旧card数字直接比较。
窄潜在贡献：自动指标回退、人工严重性判定和跨eval版本可比性是不同证据，单一通过率不能独立作发布判断；人工结果也不抹去自动回退。Frontier评估用更强3.1Pro做代理，不提供此模型独立普适安全保证。不声称已证明实际图像伤害增加，也不拿红队叙述证明绝对安全。
完整核心与必要安全段已读，root据新增证据撤回整家族无贡献结论。card/blog均只Mar03日级、未给timezone/instant，公开范围只与本窗相交，不能完全定位。不评分、不列正式候选、不Books；请求官方带timezone首次公开记录或明确范围，取得后只重开此窄评价命题（PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY候选owner，未对读Books不认定差额）。

### GPT-5.3 Instant System Card

[HTML](https://deploymentsafety.openai.com/gpt-5-3-instant/safety)Published March2；[原PDF](https://deploymentsafety.openai.com/gpt-5-3-instant/gpt-5-3-instant.pdf)封面March3。两者没有timezone/instant，必要归属冲突未解。
实际贡献信号是§3.1及PDFTables1/2：动态多轮对话随模型输出演化，有别于静态末回应安全检查；厂商报sexual/self-harm相对5.2的回退，同时online实验没见self-harm增加。困难production-derived集的not_unsafe不是平均生产风险，offline/online不能相互取消。采用须读评价定义/限制，不只复制card参数。
目前仅准入信号/定点证据，不列正式候选、不评分、不以安全改进写Books。请求官方first-public记录或具有timezone的发布日志，足以把整个公开范围定位于本窗或明确窗外；取得后只重开该家族（PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY候选owner，最终owner待实际Books对读）。

### arXiv三项日期保留与一项窗外排除

以下从当次官方月表标题和保留raw身份定点恢复，已读完整exact-v1题摘及当前版本提示，没有声明全文审阅完成：
- [2603.00026v1 ActMem](https://arxiv.org/abs/2603.00026v1)：memory fact retrieval→causal/semantic graph与implicit-constraint/conflict reasoning，潜在AGENT-MEMORY贡献；Submitted Feb04T00:54:53Z；旧registry_updated_v1=Mar03T01:00:38Z、DOIcreated=Mar03T04:37:22Z。
- [2603.00030v1 SimpleTool](https://arxiv.org/abs/2603.00030v1)：利用structured-token冗余与参数弱依赖，special-token压缩联合并行生成；潜在AGENT-TOOL-CALLING/INFER-DECODE设计增量；Submitted Feb04T08:58:27Z；旧updated=Mar03T01:00:45Z、DOIcreated=Mar03T04:37:27Z。
- [2603.00040v1 Attn-QAT](https://arxiv.org/abs/2603.00040v1)：FP4 forward+高精度FA backward的失配，提出低精度反向重算与gradient precision前提修正；潜在INFER-TENSORRT-LLM/训练数值机制增量；Submitted Feb09T04:46:21Z；旧updated=Mar03T01:00:59Z、DOIcreated=Mar03T04:37:41Z。
- [2603.01367v1 DUEL](https://arxiv.org/abs/2603.01367v1)：deterministic unmask order下test-time likelihood，挑战训练ELBO作为MDM sampler比较指标；潜在MULTIMODAL-GENERATIVE-PARADIGMS贡献；Submitted Mar02T01:56:03Z；旧updated=Mar03T02:32:28Z、DOIcreated=Mar03T05:08:21Z。非本日日期保留：实际Submitted晚于Sunday20EST（Mar02T01:00Z），按[官方availability规则](https://info.arxiv.org/help/availability.html)最早常规公告不早于Mar03T09:00BJT，本窗不含右端，足以排本窗。这是公告下界，不授实际公告时刻；不依赖DOIcreated。作为窗外查漏线索按真实事件日恢复，不在本日请求更多日期。

Submitted、API updated、DataCite registration均非具体first-public列表。旧recovery自动announcement=Mar03T09:00，只是policy映射，不能授当日实际公告无偏移。“March membership+日程”也未证明Mar02左端槽位没有February ID或旧ID事件。
请求前三个Feb Submitted ID对应的官方first-announcement记录（实际公告列表/订阅公告）和Mar01EST20→Mar02BJT09槽位的主题列表；这些身份不能套DUEL的Submitted下界排除。可接受官方availability-log提供完全落窗的公开范围；取得后按事件真实归属定点重开，不做全月audit。
`https://arxiv.org/list/cs/pastweek?year=2026&month=3&day=3`实际返回“Authors and titles for March2026”，链接转月表，不支持day批次。[官方advanced form](https://arxiv.org/search/advanced)明确announcement filter只year/month granularity。Feb尾页5标题仅补查边界身份，2602.24270仍只Submitted Feb27T18:40:51Z；未当作公告证据。
旧XML submitted-time1142 inventory不用于public分母，未把其中所有分类条目逐一送审。

## 四、终态范围与普通待办

确定当窗候选0；贡献关闭2个机构家族；具名潜在贡献日期保留5个家族（2官方card+3arxiv），不用于正面Evidence、Books或“零命中/无遗漏”；DUEL窗外公告下界排除，不纳本日日期请求。混元当前“全部”11/11与Kimi Research19条目录恢复均已限定本日对读，不再列动态目录终态限制。
Books无安全可采用的当窗增量，未写Books/LEARNING_STATE/索引。他日原文不读取扩池，只有窗口边界上述定点检查。
普通扫描、筛选、必要定点消歧已到有限停止点；V3校验（含本地链接）与本日git diff --check均通过。仍需root非作者日级Gate及其后状态同步。外部历史限制恢复条件见正式§5，不将其升级为普通待办或假通过。
未stage/commit/push；结束此日后等待新分配。
