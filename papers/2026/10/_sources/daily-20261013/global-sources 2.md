# 2026-10-13 Daily：七个全球官方来源检查

窗口：**2026-10-12 ～ 2026-10-12，北京时间完整自然日**。检查者：`live1013_global`；实际检查时间：2026-10-13 10:47～11:05 BJT（结束时 UTC 03:05）。本文件只收集、限定准入，不是 Report / Evidence / Books / 独立验收的完成证明。

启动实际重读 AGENTS.md、CODEX_RESEARCH_PROMPT.md、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 使用说明/每日组、ROADMAP 主线及最新暂停 checkpoint。历史补查暂停，非 Sunday，不创建 Weekly；仅 own 本文件，不修改 Books、LEARNING_STATE、索引或 Git staging。既有 `69-trace.md`、LEARNING_STATE 修改不归本任务。10-12 原记录只提供真实接口线索，不继承其 Coverage。

## 1. 实际入口、日期字段与停止

下列 7 行是总每日分母 14 中本任务负责的 7 项，不代表全日报已覆盖。日期已能夹窗的降序前缀即停；空壳、年度排序、混排或 hidden pagination 不证明零命中。未扫描每周来源、全组织旧仓库或全年论文。

| 来源 | 实际检查入口及停止位置 | 状态 / 结果 | 具体缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) → [Research index](https://openai.com/research/index/)；当前 9 张 dated 卡 Oct07两项 → Oct06两项 → Sep29两项 → Sep23 → Sep22 → Sep10。最新前缀已早于10-12，未按 Load more 扩旧池 | 已检查这一当前日期入口；未确认当窗新事件 | 无该可见前缀未处理项；不授隐藏/删项或全历史保证 |
| SRC-ANTHROPIC | [Research Publications](https://www.anthropic.com/research)当前10项：Oct12两项 → Oct09 → Oct08两项 → Oct01等；两 Oct12 原文日期/core实际读，停止在Oct09，不按 See more 扩旧池 | 已检查；2拟候选（下节），均无当前撤回/纠错提示；安全事件只深化实际受影响接口 | 作者实验协议/内部指标未全披露，不是来源日期缺口；嵌入交互图未作为独立复现 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) → [News](https://deepmind.google/blog/) 当前月级卡；唯一Oct卡 [EmbeddingGemma2原文](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) Date=Oct06；[DeepMind Publications](https://deepmind.google/research/publications/)页1共30/265、9页，日期前缀Sep16 → Sep01 → Aug26；[Google Research Blog](https://research.google/blog/)页1最新Oct07 → Oct06 → Oct05 → Oct02；[Google Pubs](https://research.google/pubs/)当前页仅年份/venue，有2027/2026，无日级首公开字段。各可日期入口窗前即停，不扩全年条目 | 可日期 Blog/DeepMind Publications 已检查；Google Pubs 本窗公开切片受阻隔离 | Pubs 的日级首次公开目录/窗口快照不可由年份排序恢复；接受官方10-12相关主题日期列表或具体首公开原文重开，不把年份目录逐项送审 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)web提取0行；一次实际HTTP替代恢复 [Blog](https://ai.meta.com/blog/) 200/205305字符与 [Publication results](https://ai.meta.com/results/?content_types%5B0%5D=publication)200/274433字符。Blog可见Jul27/21/09/07（Apr08 pinned不当最新排序）；Publication前12个日期位置Oct02×6、Sep24、Sep07、Sep06、Aug04、Jul29、Jul17，随后2019/2020混排。止于当前前缀，不向 Next/全历史扩池，不读窗外纯数学条目 | 已检查可提取当前目录段；未确认10-12事件 | Research 0行及混排/隐藏分页不支持完整当窗零研究；只有官方本窗有序列表或具体原件可定点重开 |
| SRC-QWEN | [旧主页](https://qwenlm.github.io/)明确迁移 → [新Research](https://qwen.ai/research)：web0行、HTTP200/92469字符为app壳；真实IAB一次65.2s超时/reset，停止目录恢复。替代 [官方组织](https://github.com/QwenLM)首10/59：qwen-code updatedOct13、Qwen-Image2.1 Oct12，随后MM-Plugins Oct11等；只对两窗口线索定点读 [qwen-code releases首5](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=5)、[Image commits首5](https://api.github.com/repos/QwenLM/Qwen-Image-2.1/commits?per_page=5)，已夹窗 | Research目录受阻隔离；官方GitHub替代已检查；1个拟接口候选与具名关闭/去重记录 | 动态Research当窗完整日期段仍无；不据GitHub updated替代研究公开日。接受官方日期目录/API或具体发布原件重开，不无限重复浏览器 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/) → 真实“更多” [研究与动态](https://www.deepseek.com/news/)：当前News5日期最新Sep10/Apr24；研究索引10最新Jun24/Feb25/Jan28。两前缀均早于10-12即停，不按“查看全部”扩旧池 | 已检查当前官方日期入口；未确认当窗新事件 | 不授隐藏条目/全版本史保证；官网无新窗口线索故不扩全组织或旧技术报告 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)26项完整可见列表最新2025-11-07；[官方组织](https://github.com/MoonshotAI)首10/42：kimi-code与MoonEP updatedOct12、其余≤Sep22。读 [kimi-code releases首5](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=5) 最新Sep24/23/19/18/17；[MoonEP commits首5](https://api.github.com/repos/MoonshotAI/MoonEP/commits?per_page=5) Oct12两项 → Sep20；[kimi-code commits首10](https://api.github.com/repos/MoonshotAI/kimi-code/commits?per_page=10)前5Oct12 → Oct10夹窗（首5尚未夹窗，补至10后止） | 已检查这些有限目录与受影响变更；具名贡献前EX，见下节core与root校准 | 不授整个组织未有其他发布或提交即首次研究公开；PR合并事件明确采用本窗merge口径，不把旧PR creation搬入本窗新论文 |

## 2. 拟候选：完整标题、已读核心与限定命题

Blog无独立 Abstract，已读完整核心说明而非搜索摘要；以下是忠实释义与原文位置，不复制受版权限制的整篇正文。评分先针对具体增量，待root/独立准入校准；不把映射章节或厂商热度加分。

### A1. [AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)

官方页面/目录日期2026-10-12，作者William Zhou、Daniel Freeman。读Introduction、threat modelling、A～G、必要Appendix A～C/F。拟 **2+2+2=6**：把“能设置推理服务”与“模型能在同一硬件自主闭环复制”分开测，提供能力floor与部署size ceiling尚未相交的反证边界；不是宣称已形成真实自主蠕虫。拟owner `PLATFORM-SECURITY`，Memento notes机制可交接 `AGENT-REFLECTION`/`AGENT-MEMORY`，不先改书。

已读core：15台4GB Android盒上的Gemma4-26B-A4B PP demo证明部署可行；8节点firewalled redroid/Android15试验为Llama3.1-8B部署服务，GLM5.2自身推理由外部服务器承担。未鉴权ADB使网络攻击步骤简化；4/5试验达8/8节点、1/5达7/8，不能等价为自身权重真实IoT复制。Memento交接workspace/notes；六代20 lineages成功率45%到61～84%；强advisor没有显著帮助只限该任务。作者ECI趋势预测不采用为确定日期。Appendix PP故障替换/KV重算、32k上下文预算和低并发气泡约束已读，现有部署数字不外推H100等价或公网安全。仍需标准/受影响安全证据审阅与独核，作者结果不是我们的复现。

### A2. [Strengthening our defenses against distillation attacks](https://www.anthropic.com/research/distillation-defenses)

官方页面/目录日期2026-10-12。完整读Simple defenses、Our new methods、How well、trade-offs及平台边界。拟 **2+2+2=6**：reasoning不是可自由跨组织/代际重放的普通上下文， provenance封闭与检测/重复尝试成本联动有具体接口约束，不以“安全宣称未开源”泛排。拟owner `PLATFORM-SECURITY`（reasoning访问边界），具体integration影响交接 `AGENT-CONTEXT`。

已读core：preserved thinking限制新API账户编辑先前上下文；强模型reasoning不可被旧弱模型读取，Sonnet5.5只原request组织可读。二阶段classifier针对提取请求，反复尝试限速/封号，低FPR领域拒绝也收费。作者原平台提取量前后降10～100倍；FPR<0.1%与SWE-bench full/summarized 80.4/71.8只保厂商口径。样本量、训练预算、对照混杂和精确FPR测法未披露；尚未经历高持久复杂绕过。迁移、误封/拒绝计费是实际代价；不采用国别/对手归因，不证明永久防蒸馏。安全接口变化需深入受影响部分，不能用普通摘要读完即Evidence完成。

### Q1. [feat(managed-agent): admit public foreground Shell with mandatory approval](https://github.com/QwenLM/qwen-code/pull/13674)

官方API [PR13674](https://api.github.com/repos/QwenLM/qwen-code/pulls/13674)：created_at=2026-10-08T11:08:05Z（旧首次PR），merged_at=2026-10-11T16:06:51Z，即本窗2026-10-12 BJT；本次采用合并/接口事件而非新论文。qwen-code本窗nightly载体 [v0.25.1-nightly.20261011.01d3e6d81a](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.1-nightly.20261011.01d3e6d81a) published_at=2026-10-11T22:01:32Z，即本窗；prerelease=true、draft=false。不另把载体算家族。拟 **1+2+2=5**，owner `AGENT-PLATFORM` / `PLATFORM-SECURITY`待唯一owner核。

完整core/Why/Risk已读：default-off公开Shell admission必须asking approval；stored AgentDefinition保 pinned profile/revision/digest。关admission gate只拒绝fresh执行，保原key replay及已接受的approval/cancel/settlement；公共入口不能mint保留internal TeamLead身份，也不能跨public/internal policy replay。升级reader/Harness后才可启用；publicShell生命周期、CSI/签名部署、物理quiescence及Windows尚未验收。具体增量是fresh admission与已受理settlement分离，防止关gate破坏恢复或公有创建获得internal私有策略；不宣称default-on/生产可用。此处Source仅core，尚需root必要实现/具体owner与独核。

## 3. 具名关闭、去重与未扩大队列

### M1（贡献前EX）. [Release fds and the multicast handle on Buffer construction error paths](https://github.com/MoonshotAI/MoonEP/pull/33)

[PR33 API](https://api.github.com/repos/MoonshotAI/MoonEP/pulls/33)：created_at=2026-08-29T21:17:23Z，merged_at=2026-10-12T09:18:17Z。本窗merge d86fda40329de4002e0cade6817df7b4b5512ee5，不搬旧PR首公开。完整core与[唯一文件diff](https://api.github.com/repos/MoonshotAI/MoonEP/pulls/33/files?per_page=20)实际读；root准入校准后贡献前EX、不评分：只恢复既有shareable引用全释放的成立条件，未新增资源所有权设计或反证实验，也未发现已采用Books具体错误待修。

不是泛化“finally更好”：SCM_RIGHTS拷贝的fd是当前进程plain int owner，sock.close不释放它；export fd还pin cuMemCreate allocation而非只消耗fd表。补接收异常与export/multicast construction guard，不改变success path。作者只有对master代码阅读/py_compile，未多GPU/NVLink执行错误路径；不授端到端正确性。不否认bug真实性，保存实际failure core，不新建全文实验队列。

### M2（贡献前EX）. [chore: remove unused kaos package and MCP kaos executor option](https://github.com/MoonshotAI/kimi-code/pull/4184)

[PR4184 API](https://api.github.com/repos/MoonshotAI/kimi-code/pulls/4184)：created_at=2026-10-12T08:53:53Z，merged_at=2026-10-12T10:43:56Z；commit cbd754049a114ee36d1b27675c82819e4963c692。本窗compatibility事件，完整core/behavior table已读。root准入校准后贡献前EX、不评分：废弃未可用executor保持显式拒绝，恢复成熟严格解析/不静默执行不变量；没有新的execution capability设计或已采用Books具体错误。

具体failure core：废弃executor不能直接删除schema字段，否则zod剥未知key会静默落到local execution；保字段/收窄enum显式CONFIG_INVALID。代价由旧单server NOT_IMPLEMENTED变为整配置文件不可用，SDK kaos字段/方法删除有编译迁移成本；旧legacy migration schema保留。按actual core关闭而不是因chore标签泛排；不采用作者测试为独立验证。

- **Qwen-Image2.1样例尺寸**：[518be095bdfa6efa3713af84ee36e3642e73e0c1](https://github.com/QwenLM/Qwen-Image-2.1/commit/518be095bdfa6efa3713af84ee36e3642e73e0c1)，committer10-12T09:45:30Z；实际diff仅两处1680×2512改1696×2528（32倍数）。EX：样例符合既有grid兼容条件，不改变架构、采样或新的quality/resource边界，不借模型名准入。
- **Qwen EventTransport空seam**：[PR13909](https://github.com/QwenLM/qwen-code/pull/13909)，merge10-11T16:56:03Z＝本窗。完整core/Risk：现after-commit hub先运行、future adapter隔离；adapter列表空且默认无行为变更、无broker/producer/consumer。EX：尚未交付跨节点执行机制或新的可靠性证据，仅组合接口重构，不将未来MQ2当本窗实现。
- 本窗nightly完整19条changelog核心已读，只对实际生命周期/兼容性线索定点取PR。PR13330/13892/13872/13788/13877/13673/13460实际core与Risk/日期已读，merge UTC分别10-11 08:44/11:11/11:59/14:25/14:33/15:41/14:22，均在10-11 BJT；本窗载体不把这些早公开机制包装成新论文，不否认其具体durable fence、member chain、merge-before-settle、route-scoped ceiling、bounded cancel、Hook recovery和错误分类价值。若root查到本窗实质修订只重开该事件，不无限PR历史。
- qwen-code releases首5真实顺序为nightly10-12T22:25:02Z（BJT10-13，窗后）、v0.25.1 10-11T10:20:36Z（窗前）、nightly10-11T22:01:32Z（本窗）、sdk0.1.19 10-11T11:42:33Z、desktop0.25.1 10-11T11:31:22Z（两者窗前）；同页released_at不是严格时间序，逐项读字段而非首项推零。
- **MoonEP conservative SM guard**：[PR10](https://github.com/MoonshotAI/MoonEP/pull/10)，merge10-12T09:18:01Z。完整Summary/Problem/Change/Validation已读：positive integer≤physicalSM，default=min(32,physicalSM)，不计算occupancy/cooperative launch可行值。EX：把既有通信配置提早校验，未新增通信机制/新性能边界；不以7个作者单测证明所有CUDA launch合法。
- **Kimi视频取消**：[PR4183](https://github.com/MoonshotAI/kimi-code/pull/4183)，merge10-12T09:02:18Z；完整core/behavior表及作者test范围实际读。ctx已有AbortSignal却未传uploader，补真实上传boundary、取消后rethrow禁止inline fallback，普通上传failure保fallback；作者真实挂起HTTP/engine检查不是独立复现。拟EX供root校准：既有Esc取消合同的局部实现漏接，没有新增取消协议/调度机制；不要泛排为“任何修复都无价值”，也不授physical process或全服务stop证明。
- **Kimi remote-control terminal offline**：[PR4182](https://github.com/MoonshotAI/kimi-code/pull/4182)，merge10-12T08:30:57Z；core/behavior完整读。user_requested已有stopped/lock release但foregound漏观察closed，补terminal reason退出；embedded kap-server继续可重开。EX：履行既有终态合同的局部runner wiring，非新的任务状态机/可靠性边界。
- **Kimi headers timeout配置**：[PR4092](https://github.com/MoonshotAI/kimi-code/pull/4092)，merge10-12T05:51:40Z；core/behavior完整读。header-only timeout可配，但SDK总10min仍约束单attempt min(limit,10min)，不设bodyTimeout、不改global dispatcher；SOCKS fallback与google-genai无接缝限制明示。EX：既有HTTP client参数配置/兼容性，没有新推理/Agent执行机制或跨协议性能证据。
- **Kimi progress display**：commit0a3a2fbafab473df9e9f6609f825af78d2c1ce6d/[PR4159](https://github.com/MoonshotAI/kimi-code/pull/4159) title明确desktop/web NotifyUser进度展示；题名范围前关闭为UI呈现，不推断后台行为或新增可靠性。

## 4. 限制与交接

拟候选共3家族（2标准拟6、1标准拟5），是否正式准入以root/独立校准为准；正文/core阅读不是标准审阅/Books完成。MoonEP33/Kaos4184原最低拟候选经root具体准入校准撤销，完整core与反侧保留，未以4分反推准入。三个已有限穷尽的目录保证缺口：Google Pubs日级公开切片、Meta Research/混排隐藏段、Qwen动态Research；均不支持零命中、Coverage通过或互联网无遗漏，不继续追整历史。

当前官方事件页无所读事件的撤回/删除提示；仅轻量查看已开原件，不遍历全站版本史。安全/正确性信号已限定到reasoning接口、publicShell admission、fd ownership与schema fallback，后续只审采用命题必要原证。root已收到两Anthropic core/限定条件及GitHub最低项准入消息。本任务到此停止，等待root处理Report/Books/独核，不继续其他日期或发现扫描。
