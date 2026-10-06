# 2025-10-03 DAY 独立复核

复核者：Euler / Codex，非作者 Huygens。窗口 `[2025-10-02T09:00:00+08:00,2025-10-03T09:00:00+08:00)`。切换前已保存15作者停点；fresh实际读取AGENTS、当前Research/Report、Sources使用说明/每日/按需/arXiv、Prompt、ROADMAP及最新10月路由，仅加载03材料。

**最新结论：通过。** 2026-10-05T09:12:37+08:00，Euler实际完成R1/R2非作者窄POST，原DAY有效范围复用。正式候选0、正面Evidence完成0、Books提案/写入0的隔离成立；root FIRST五潜力及三排除不重复全文。作者可据本结论同步README完成态，随后检查最终正文；不把日期隔离授为正面Evidence或无遗漏。

## R1/R2 窄POST

本次fresh按03窗口重读当前治理上下文，只核两项返修与相关README/CURRENT_STOP，不重审23核心或94题摘。实际回读01688v1原文本195–222行与CORE_BOUNDARIES对应句：240样本、两位医学专家、kappa0.8091、Spearman0.8129及p<0.0001一致；支持受限任务评价一致性，不称没有人类验证，也不推广泛临床等价。R1通过。

实际解析SEARCH_REPAIR_RAW原JSON的执行时间2026-10-04T23:21:05Z、四条search_query、response_length=long及14项原返回标题/来源；与SCREENING四条字符串、07:21:05+08时间、仅首批停止一致。旧A/B/C输入不能恢复的限制保留；新查询不按旧结果猜造，域外社区/诉讼结果未当官方研究，Meta/Qwen/MiniMax无相关返回不作零事件。README来源行及§5/6仍正确限定窄回核。R2通过。此补证不新增候选/Evidence/Books。

下方保留原DAY发现及实际阅读边界作历史依据，原“待窄修”表述不覆盖顶部最新结论。没有新共同误判或需要扩池重审的信号。

## 需要作者窄修

1. **R1：Format Inertia的人类验证不能省略。** [原精确v1 §4.1](core-2510.01688v1.text.txt)第200–213行实际报告：240样本、两位医学专家、Cohen kappa 0.8091、human/LLM Spearman 0.8129。CORE_BOUNDARIES现有“LLMjudge未验证对医学专家等价”若指广泛临床等价可以成立，但单独这样写会使读者误解为没有人类验证。请补明作者确做这个有限、约束任务的验证，同时保留§Limitations的医学领域、相关性及外推限制；不需新论文/附件，也不升级日期或Evidence。
2. **R2：辅助搜索实际query缺失。** day3searchA/B/C保存了真实结果，SCREENING/README仅说明official域、Oct2主题及首批停止；原响应不含search_query输入。请从本任务真实调用恢复实际查询字符串与分组/首批停止范围到SCREENING，不能按结果猜造。若输入已不可恢复，只对缺失的同日窄主题有限重执行并保存新输入、原响应及时间，旧响应照保留，不扩分类/月/年。arXiv四主题/标题补检及机构HTTP/API的URL参数已有真实记录，不需重做。

返修后只回核R1句子与R2查询记录及相关README变化；其他已核范围复用。没有要求79潜力全文或所有Books owner。

## 原来源与范围核查

实际读本日README、SCREENING、CURRENT_STOP、CORE_BOUNDARIES、FIRST与发现/恢复脚本，并核各原请求receipt及下列原数据切片。HTTP 200、下载或抽取成功本身不是阅读或覆盖证明。

| 来源 | 本次实际核查与判断 |
| --- | --- |
| SRC-OPENAI | Research 403原记录；day3searchA中Wrtn原官方完整核心及日本政策说明，前者persona/路由/业务指标未辨识可比机制增量，后者合作政策；RBAC原正文见下。辅助query需R2补齐，不作无遗漏 |
| SRC-ANTHROPIC | 原Research Flight的Sep15 20:33 UTC/Oct3 18:31 UTC邻接字段，own bundle7的本地`N=p?j:j?.slice(0,10)`及SeeMore，不把首10条当末页；只核日期边界，不把171条变正文队列 |
| SRC-GOOGLE-AI | 原DeepMind selected publications page2的Oct30/Sep29边界；独立Google pubs正确`search=language%20model&category=2025`响应1–15/37、1/3，年度精度不作日公开；own October Blog page2/2的Oct7/Oct2/Oct1及PASTA原core/旧v1摘要，不扩37全文 |
| SRC-META-AI | 原Research原件及抽取仅当前标题，receipt200不消除历史缺段；辅助搜索不作零事件。R2适用 |
| SRC-QWEN | 原Blog五条日期Sep23至Jul24及Next，旧可见段不证明迁移后历史无事件。R2适用 |
| SRC-DEEPSEEK | 原/news/文本的独立Research Oct21/May14及News Dec1/Sep29边界；own恢复非只主页模型导航，未把31旧条目变摘要队列 |
| SRC-MOONSHOT | 原Blog27条中的Sep16/Nov6邻接；org per_page100请求仅身份，不当历史release或公开时间 |
| SRC-TENCENT-HUNYUAN | 原Research动态壳、实际browser有限失败作者记录；官方publicList原JSON total9/list9及时间字段均2026，停止page1，历史2025隔离，不用当前空历史证明无事件 |
| SRC-ZAI | own bundle实际`URLSearchParams.set("page",nextPage)`；page2原Flight nextPage3/hasMore false、Dec7 16:00 UTC最早，实际分页不是首15当末页；10月缺段隔离 |
| SRC-BYTEDANCE-SEED | own恢复脚本的US头、两类原JSON各分页：papers tokens0/20/40/60/80返回19/15/19/19/13，total94，末false；Blog17/18/6、total49、末false。原PublishDate的Sep21 16:00/Oct8 16:00 UTC与Sep8 16:00/Oct22 16:00 UTC邻接；可见85/41差额不当零事件 |
| SRC-BAIDU-ERNIE | 原Blog/page2原文的Oct16/Sep12邻接，不因GitHub可见就回填公开时刻 |
| SRC-XIAOMI-MIMO | 原Paper八日期May12/Jun4/Sep19/Oct21及2026四条，own bundle More为展示展开，不是历史翻页；不逐审窗外正文 |
| SRC-MINIMAX | 英/中文Blog原日期尾段及独立Agent Tech Blog 2026May13当前入口；历史缺段隔离，不假定Agent尚不存在。R2适用 |
| SRC-ARXIV | 实际四个窄主题查询、start0/max40及model tail40；原Atom40+4/9/25/24，与total44/9/25/24相符。CL/CV/DC/PL/IR仅skip0/show25月标题补检；原日announcement查询被格式限制拒绝，不作零事件。精确v1 Atom80+3+11去重94；不把submitted/Atom published当first-public |

未扫描每周来源，未新增按需全站扫描。四主题与相关标题有限导航是发现范围，不授全分类/全年召回。原响应的94题摘未在本次全部重读。

## 必要核心实际读到哪里

以下均为本日原精确v1抽取文本相应正文节；RNG使用已存精确PDF及其真实web PDF读取文本，未把HTML错误页当正文。只确认安全/设计反侧及准入消歧，不授完整Evidence或复现。

| 精确身份 | 本次实际必要节与采用边界 |
| --- | --- |
| 2510.21740v1 | §3.1–3.2、4.5–4.6：3968/768简单图、三模型probe与handoff解释；高密度ensemble GT坐标反而伤害，不等绝对信息丢失或通用修复 |
| 2510.02185v1 | §5.1–5.2相关评价、5.4：1555/336/1311、Gemini2.5Pro与固定trials/fuzz预算；crash-only、API成本代理、小human样本限制 |
| 2510.01598v1 | PDF §2.3–2.4、Conclusion及Methods100kHz/16MTJ：10k64×64 GAN、LPIPS<0.3、class6 18.6×；不等LLM jailbreak验证，百万cell能耗/吞吐是外推 |
| 2510.02194v1 | §2两阶段、3.1与评价定义、A.2：安全expert与router分工；not-rated5安全率容纳1–4分，不保证adaptive安全 |
| 2510.02091v1 | §2、3–4相关任务及6.1：Qwen/Llama、loglik与生成评价的层裁剪差异；不外推所有depth无用 |
| 2510.01631v1 | §4.1–4.1.2、Limitations：正文600/70k GPUh、100M–3B/200B、单生成器和单轮；未证frontier/safety/多代稳定 |
| 2510.01569v1 | §4.1、Limitations、A.3：SafetyBench/TRIDENT/insider、训练与judge；teacher知识和inverse结构未完全解耦 |
| 2510.01586v1 | §5.1：三agent三拓扑、300攻击池、ASR/contagion分开；“4000 from MATH500”歧义保留，不代作者修数据 |
| 2510.01549v1 | §5开头/5.1、6：SD1.5/SDXL、DDIM100×50；KL surrogate与CMMD是代理，复杂OOD/紧度开放，不以reward当quality |
| 2510.01670v1 | §2.3、3开头：BGD intent与Completion分开、o4mini judge、15步及R1输入差异；不把意图当危害完成 |
| 2510.02554v1 | §3.2–3.3、4.1–4.2：name/description非schema、10轮搜索/100queries；BSR搜索最好选择率不是恶意执行率 |
| 2510.02418v1 | §4.1、5.2数据构造、7：213/109/98、同BrowserUse及R1无图；BothBad排除、captcha20+200和平台特定限制 |
| 2510.01688v1 | §4.1、Limitations：8k/40医生、100profiles、受限医学任务；补核200–213的人类验证产生R1，不否定有限支持也不授临床等价 |
| 2510.02230v1 | §4.1–4.2：QwenMath/Llama、40k四bench；pass1与pass256分离，训练中负干扰是此设置证据，不是无条件RL定理 |
| 2510.02204v1 | §4.1–4.2：1800分层样本、deterministic GTA、双expert仅同意/非NA；agreement受选择限制，reasoning grounding与action EM不同 |
| 2510.01642v1 | §III-C–D与必要模型设置：模拟replay2poses/三任务、131k+56k、10帧三视角；不等真实生产控制安全 |
| 2510.01539v1 | §4.1：同构code/math hidden vs revealed变量；未审理论假设，不授所有OOD因果定理 |
| 2510.02209v1 | §3.1、4.4：20DJIA/82天/32k/3seeds及排序随窗口反转；后发布模型回顾交易的知识泄漏是复核推断，不当已控或可盈利证明 |
| 2510.05154v1 | §2.2、3.1、7：3000/4500/10美国主题、human/LLM相关<.4；有限主观任务，不外推所有judge失效 |
| 2510.01925v1 | §VI-C/D2、B：survey也有新增PRM对照；6×2policy、MATH500/T.7/beam4/MCTS4、official与32trial混用限制，正确性排名不充分预测下游 |
| 2510.02483v1 | §1、2.1–2.5：框架优化未给具体方法，H200、SlimPajama、BF16/ZeRO1/batch256与GPU能耗边界；不因未披露/数字争议排潜力 |
| 2510.01609v1 | §III-C–D：state/recent-performance MLP softmax权重与complexity分层，确有消歧后的adaptive潜力；不授生产LLM成本 |
| 2510.02292v1 | §3、4.1–4.2：hooks之外八模型middle/last表示、两层MLP512、kfold/random-label；表示测量不等机制因果解释 |

另实际读RBAC完整write-up及原页面start_at/published_at字段：事故与generic公告可落窗，事后根因正文仍无公开时刻，不进入Books。实际读PASTA Blog核心及2412.10419v1完整摘要：EM/RL/slate与人/模拟轨迹旧稿已有，无辨识新方法修订；artifact真实首次公开仍未证，不能回填旧日。

## 分层样本与终态

复用root三具名完整題摘排除：ImageNet-Think、AccurateRAG、IoDResearch。本次另在原exact-v1 Atom实际读REBot、NVIDIA AI Aerial、LLM4Rec三份完整题摘，分别核应用检索组合、无线DSP/CNN GPU范围、推荐五组件与局部指标未辨识新边界。合计6/12完整题摘贡献排除样本；其余6个贡献排除及12标题范围关闭未逐一重读，不称全量排除验证。未发现“小模型/局部/负面/综述/已有主题”共同漏收理由。

79日期潜力、RBAC正文日期与具名历史缺段均不作正面Evidence/Books/零事件/安全性能或无遗漏保证。0正式候选时无需所有owner正文；报告没有把未比较的79篇写成逐篇已有覆盖。共享Books实际写入0，作者未提出长期差额，无Books实际修改需要验收。仅R1/R2及随后非作者窄写后核可执行，其余外部保留项有README §5精确重开条件，不要求互联网穷尽。

V3当前进行中报告接口校验实际通过；限定`git diff --check`实际通过（本日目录untracked，不能用此替代未跟踪文件检查/语义）。本复核只写独立FINAL，不修改Huygens报告或root FIRST，不授Euler作者14完成，不stage/commit/push/clean。
