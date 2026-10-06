# Daily Research — 2026-02-12

**规范：** V3
**窗口：** 2026-02-11T09:00:00+08:00 ～ 2026-02-12T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T15:59:47+08:00
**补充窗口：** 2026-02-11 ～ 2026-02-11
**窗口说明：** 用户授权仅补已有 Daily 遗漏，原窗口、候选日期、评分与有效证据冻结保留；新增按前一完整北京时间自然日 date-only 检查，不迁移旧项。原完成声明仅指原审阅；本轮补查另经root完整六部分实际DAY通过，不继承旧标签。

## 1. 结论

2026-10-08补查已由非作者root完整六部分实际DAY通过并授权完成，普通待办0。新增21个唯一家族（UniT＋20 arXiv）必要方法/关键评价/直接反侧经root独立限定核验，最终16整合、1已有覆盖、4中心保证暂缓：UniT/SCD/VW2/SOFT/Stream五项此前actualPOST及PoSH/SWE/OSI/ARK/Values/STaR/Scalpel/ACT/CoCoA/Steer/Flex十一处review_20260214实际POST全部通过，root已读逐项裁决；Harvest实际Ch36同命题覆盖、TPA/Risk/Causal/Linear争议处置通过。全篇79=原58＋新增21，原58行/评分/窗口/连续§4有效证据冻结。新增机制融入唯一owner的现有论证，所有写锁释放，未核代码或复现。三跨界日期项、later7早正文未认证线索和具体保证隔离，不评分深审绕日期，不进Books或支撑无遗漏；[具体owner差额](../_sources/daily-20260212/supplement-20261008-owner-next.md)、[实际POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)与[停点](../_sources/daily-20260212/supplement-20261008-checkpoint.md)可复查。下面原58完成声明仅为冻结原验收；本轮DAY依据独立增量裁决。

本日的重要增量不是榜单汇总，而是几个具体接口：提前计算 gradient 仍保留 global optimizer commit；离线 NVDEC prefix 路径仍受 CUDA restoration/HBM admission 限制；reward 的 DB-diff 与语义目标可能两向失配；表示、生成路径、动作 consumer 与真实提交权需要分别验收。新的局部 credit、检索前 probe、采样几何和 controller 分支均保留直接反侧，没有将代理量升级为 truth、安全或通用性能保证。

按本日有限主题发现、完整题摘准入及逐ID日期包络，最终冻结 **58 个唯一家族**：38整合、7已有覆盖、12仅报告、1暂缓。57项采用命题完成相应标准/受影响深入审阅；FLARE中心全路径递推争议已隔离为暂缓，有限单步sensor已核但不称完整Evidence保证。38项实际Books正文、完整邻接与末注均经root非作者POST通过，所有写锁释放。普通发现、必要证据、owner比较、修改及POST待办0；本篇V3机器检查与引用检查已通过，root完整六部分整日语义验收通过并授权完成态，不由作者自授完成。

原版Complete/545库存/16入选不继承，[旧原证](../_sources/daily-20260212/V3_LEGACY_README.md)保留但不作强制队列。首批16、第二批45及有界补检20条完整题摘用于实际准入校准，不等同这些数量都是当日公开论文。计数以唯一ID为准：09629明确贡献关闭而不入选；09394原为行内证据，已保留在58，不因小标题排版漏算。[本日证据停点](../_sources/daily-20260212/V3_EVIDENCE_AND_BOOKS.md)保留计数修复、真实原证与未采用claim。

## 2. 来源覆盖

原执行日2026-10-04；2026-10-08独立补查14个每日入口，不扫描Weekly组。旧有限记录有效部分复用，以下同时记录本轮明确缩窄的缺口；无历史完整目录的来源仍不支持‘无遗漏’。14每日及具名触发的有限查询/分页与停止、题摘分流和日期限制已经root实际核；21新增必要Source及Books安全终态已处理，root完整六部分DAY通过，普通待办0；历史外部目录限制保持终态隔离，不算普通未读工作或Coverage全部通过。原始补查记录与具体停点见[本轮停点](../_sources/daily-20260212/supplement-20261008-checkpoint.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | `https://openai.com/research/`及官方 Research/news；官方域 Feb11 research 查询，实际research news 141行 | 受阻 | Forum活动无原机制；registered入口重定向未作历史完整目录。该段与有限查询已处理，目录历史召回检索受限，不授整个官网零事件。 |
| SRC-ANTHROPIC | `https://www.anthropic.com/research`当前10条、官方域February2026 research查询 | 受阻 | 当前Sep/Oct首屏不能恢复历史；Feb5 Opus线索窗外，停止而非扫全部发布史。历史目录缺段隔离，不支撑无遗漏。 |
| SRC-GOOGLE-AI | DeepMind研究入口/Google2026 pubs与官方域Feb11定点查询；最后精确`variable capacity scheduling`→官方Feb11 Blog | 受阻 | 1947条pubs仅日期/主题线索，不逐项读。Aletheia/DeepThink数学科学暂缓；调度Blog核心已读，是SPAA2025理论的重释而非本窗新的LLM机制，贡献关闭。Node pubs请求connect timeout、web exactyear internal error，保留有限检查边界。 |
| SRC-META-AI | Research空提取后results page3从Feb27/26/13到Feb11 UniT、Feb10 AIRS再Jan2夹窗停止；本轮重新核官方页/当时PDF | 已检查 | UniT Feb11官方date-only符合补充自然日；web PDF点击失败后直接官方PDF取得，必要页1–12已核。原旧时刻缺口对本轮解除，未用后来arXiv稿补当时证据。 |
| SRC-QWEN | 官方retrieval API `type=qwen_ai/language=en-US`真实40条title/date；Feb16 Qwen3.5与Feb10 QwenImage2.0夹窗，返回无分页字段后停止 | 已检查 | 此原生目录切片无Feb11入口，未把repository更新称公开事件或授整个GitHub零事件。[字段](../_sources/daily-20260212/supplement-20261008-qwen.json)。 |
| SRC-DEEPSEEK | 官网/官方news有限日期段 | 已检查 | news从Jun24 V4经Feb25 DualPath、Jan28OCR2、Jan12Engram到Dec31mHC夹窗，该可读段未见本窗新入口；不以此授官网全部无遗漏。 |
| SRC-MOONSHOT | Kimi Blog26条Nov2025及更早；官方域Feb2026查询；`https://github.com/MoonshotAI`研究/infra profile与十仓库首段；限定orgFeb11/12 language model查询 | 受阻 | stale Blog与当前profile不是历史release ledger，有限替代未得窗内原始新增说明，目录历史缺段隔离。K3/AttnRes等当前材料不反灌本窗。 |
| SRC-TENCENT-HUNYUAN | Research仍无静态全部目录；本轮真实POST publicList page1/size12/renderType0、zh locale，总11全部返回，Feb13RLVR与Feb3context夹窗停止 | 受阻 | renderType0官方blog11条切片已检查无Feb11，但未证明覆盖Research全部renderType。原动态全部历史缺段仍隔离，不把Blog替代全Research。[字段](../_sources/daily-20260212/supplement-20261008-hunyuan.json)。 |
| SRC-ZAI | 本轮Research实际175行15条，从Aug26至Feb21报告/Feb11GLM5launch/Feb2OCR/Jan19夹窗；release core已有有效关闭 | 已检查 | GLM5launch仅规模/DSA复用/异步RL标签/成绩，未公开具体新机制，原事件贡献关闭复用；后来Feb21报告不倒灌。该历史段可读，原400/timeout覆盖缺口缩窄。 |
| SRC-BYTEDANCE-SEED | public_papers首20 Aug–May；本轮原生API US locale next20/40/60到Feb26–Jan26夹窗即停；Research/Feb11官方域查询；[原始毫秒及北京时间校正](../_sources/daily-20260212/supplement-20261008-seed60-date-correction.json) | 受阻 | TwD1391为北京Feb12窗外；10560/10885完整AB具体潜在贡献已读，但目录回填北京Feb11不认证先行正文，arXiv最早公告Feb12。原生目录/项目/OAI/具名primary搜索有限恢复后精确日期隔离，详[终态与重开条件](../_sources/daily-20260212/supplement-20261008-date-final.md)，不评分/core/Books。Seedance2原有效贡献关闭复用，不倒灌April稿；Research/Blog历史限制不授全站完整覆盖。 |
| SRC-BAIDU-ERNIE | ERNIE中文Blog首屏11条May9至Nov21，Feb6/Jan29夹窗 | 已检查 | 已处理该可读历史段，本窗未见研究入口；不外推所有Paddle/ERNIE发布。 |
| SRC-XIAOMI-MIMO | MiMo主页Paper Mar13/Feb3/Jan8夹窗；当前Blog15条至More，标题段177–295实际读 | 受阻 | 已处理可读Paper历史段；Blog15当前条目无日期、不支持本窗完整历史，More非可读链接，历史目录缺段隔离而非普通未读或零命中。不以paper段代替全部Blog，不倒灌当前V2.5/V2.6。 |
| SRC-MINIMAX | 英中官方Blog及窗口定点查询，M2.5 Feb12核心 | 受阻 | M2.5 launch规模/标签未给可核新机制，明确关闭；单独中文Forge核心有WindowedFIFO，不合并关闭。中文Blog Feb12 date-only与news Feb13/英文Blog Feb14冲突，日期终态隔离，不倒灌详细稿。 |
| SRC-ARXIV | 本轮四主线API start0/max60各total45/30/14/35全部返回，124occurrence/116unique；36可能相关精确v1完整题摘；CL/DC只取ID09000–10200附近相关标题有界查漏，另7完整题摘即停 | 受阻 | 本轮API成功，Submitted proxy只发现；43完整AB不自动候选，20本窗arXiv潜在贡献与日期通过，12本批贡献关闭、later10=7日期保留＋3贡献关闭、Omni日期保留分开。[具名分流](../_sources/daily-20260212/supplement-20261008-screening.md)和[日期限制](../_sources/daily-20260212/supplement-20261008-date-final.md)可复查；root已实际必要Source/代表关闭校准，CktEvo模板关闭误判仅重开该项并隔离日期；21确定候选均获得实际证据与Books处置。CL1936宽库不是全部题摘队列。 |

arXiv实际主题为language/foundation model、Transformer/MoE、训练/优化，multimodal/World Model/VLA，GPU/runtime/编译/资源/推理，以及RAG/memory/Agent协作；不把通用检索/博弈/视觉领域应用扩成队列。API排程proxy为`[202602091900 TO 202602101900]`，sort submittedDate/ascending，并非真正public过滤。官方域Feb11 transformer-runtime/world-model/retrieval-agent-memory三次搜索未得结果，搜索零不是分类零。[完整查询与停止](../_sources/daily-20260212/V3_SOURCE_SCOPE.md)保留失败与有限替代；本次20AB后不继续同义查询。

代表关闭经独立核：09063暂缓科学域；09109/09305归纳未给具体新反证；09051离线Pandas优化未服务大模型执行/新Agent可靠性；09372/09657/10116与09472组合/规模未辨识新增条件；10019 group权heuristic的token-independent不证明原目标无偏；09433 normative spec组合未给新enforcement/兼容/不可绕过边界；09629 binary level3与WASR重权是不同estimand，未给同response旧judge漏判增量。后两安全/设计信号已有定点核心核验，不按‘survey/未实现/局部’一律排除。新增20中10024/09801/09270/09621/09413/09805/09552分别track汇总、暂缓科学、社会统计、backend组合、成熟层缩放、成熟分账和未给instruction-history-turn受控边界而关闭。未被抽检的其它明确标题范围外项不称逐项独立验证。

## 3. 候选与判断

公开包络均含起不含终；每行下界来自官方最早标准排程，不将Submitted称public。登记最终ID/DOI对应本家族v1，仅作最迟上界；+1秒覆盖秒精度，绝不把registered/updated冒称真实时刻。58项Submitted分别在Feb9 19Z至Feb10 19Z批次，根逐字段/精确history及现成信号核后授完整落窗。无先行独立正文信号；有延迟只影响上界。日期原值、时区、版本和推定依据见[日期字段](../_sources/daily-20260212/V3_DATE_BOUND_FIELDS.md)。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Rollout-Training Co-Design for Efficient LLM-Based Multi-Agent Reinforcement Learning](https://arxiv.org/html/2602.09578v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:07:37+08:00 | microbatch提前gradient，完整global population后才optimizer commit/version同步；2+2+3=7 | 深入完成 | 整合：TRAIN-GRPO [Ch33 L1232](../../../../books/part-04-training-system/33-grpo.md) |
| [Efficient Remote Prefix Fetching with GPU-native Media ASICs](https://arxiv.org/html/2602.09725v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:11:12+08:00 | 离线量化prefix codec用NVDEC，waiting-fetch与running队列分开；2+2+3=7 | 深入完成 | 整合：INFER-KV-CACHE [Ch45 L1241](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments](https://arxiv.org/html/2602.09430v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:04:05+08:00 | 冻结atomic skill的terminal→next demo-initial分布桥接，controller后resume；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26 L923](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Agent World Model:Infinity Synthetic Environments for Agentic Reinforcement Learning](https://arxiv.org/html/2602.10090v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:19:55+08:00 | DB-diff幂等false-negative/错误entity false-positive，训练评估history-limit对齐；2+1+3=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33 L562](../../../../books/part-04-training-system/33-grpo.md) |
| [AgentCgroup: Understanding and Controlling OS Resources of AI Agents](https://arxiv.org/html/2602.09345v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:02:05+08:00 | agent-parent budget下tool-child cgroup，memory.high/freeze先于kill；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84 L596](../../../../books/part-07-agent/84-agent-platform.md) |
| [Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning](https://arxiv.org/html/2602.09598v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:08:06+08:00 | 有限suffix recoverability二分定位→branch credit→仅negative lowerclip放宽；2+2+3=7 | 深入完成 | 整合：TRAIN-GRPO [Ch33 L235](../../../../books/part-04-training-system/33-grpo.md) |
| [Where-to-Unmask: Ground-Truth-Guided Unmasking Order Learning for Masked Diffusion Language Models](https://arxiv.org/html/2602.09501v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:05:46+08:00 | GT-margin只训练oracle；独立planner学where order，前半planner后半Margin；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 L306](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Laplacian Heads Improve Transformers by Smoothing Token Representations](https://arxiv.org/html/2602.09297v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:00:56+08:00 | 部分head把PV改为V−PV，保留混合head与signed Wo；2+1+3=6 | 深入完成 | 整合：MODEL-SELF-ATTENTION [Ch14 L115](../../../../books/part-02-model/14-self-attention.md) |
| [Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?](https://arxiv.org/html/2602.09937v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:16:20+08:00 | opaque summary改为完整code/output/errors与goal交接的局部证据；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [On the Optimal Reasoning Length for RL-Trained Language Models](https://arxiv.org/html/2602.09591v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:07:55+08:00 | 受测不同初始化下reasoning长度可非单调，同GPUh提供有限反侧；2+1+2=5 | 标准完成 | 仅报告：Ch33 hardcap、必要步骤成本prior与长度误税已有成立条件。本项两初始化/精度不一致的局部证据不足改变通用length控制或阶段识别规则。 |
| [PABU: Progress-Aware Belief Update for Efficient LLM Agents](https://arxiv.org/html/2602.09138v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T10:57:00+08:00 | stage-progress条件attempted-actions reset，与learned observation retention分责；2+2+2=6 | 深入完成 | 整合：AGENT-CONTEXT [Ch75 L538](../../../../books/part-07-agent/75-context.md) |
| [Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge](https://arxiv.org/html/2602.09341v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:01:59+08:00 | 语义CDP sharedprefix+localbranch审计与minority-trap训练；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82 L616](../../../../books/part-07-agent/82-multi-agent.md) |
| [Rethinking Global Text Conditioning in Diffusion Transformers](https://arxiv.org/html/2602.09268v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:00:12+08:00 | pooled MLP modulation的正负方向，区别sequence attention与output CFG；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 L184](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/html/2602.09383v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:02:59+08:00 | length-matched truncation后残余2.2pp反侧不能只用长度解释；2+1+2=5 | 标准完成 | 仅报告：Ch66 format/semantic控制与length-deconfounding已承载长期judge验收条件 |
| [$n$-Musketeers: Reinforcement Learning Shapes Collaboration Among Language Models](https://arxiv.org/pdf/2602.09173v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T10:57:49+08:00 | 冻结专家无decode forward→Perceiver softprefix→policy接口；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82 L342](../../../../books/part-07-agent/82-multi-agent.md) |
| [Effective MoE-based LLM Compression by Exploiting Heterogeneous Inter-Group Experts Routing Frequency and Information Density](https://arxiv.org/html/2602.09316v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:01:24+08:00 | frequency+effective rank分配压缩rank，sharedbasis与sparse latent残差；2+1+2=5 | 深入完成 | 整合：MODEL-MOE [Ch21 L809](../../../../books/part-02-model/21-moe.md) |
| [VLM-UQBench: A Benchmark for Modality-Specific and Cross-Modality Uncertainties in Vision Language Models](https://arxiv.org/html/2602.09214v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T10:58:50+08:00 | instance perturbation下URR/HCC可与受测VLM答案错误失配；2+1+2=5 | 标准完成 | 仅报告：Ch66 semantic-neighborhood/joint UQ的sensor≠风险概率和部署slice验收已有规则 |
| [Timing and Memory Telemetry on GPUs for AI Governance](https://arxiv.org/html/2602.09369v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:02:39+08:00 | 不信任host时分资源challenge观测争用与统计residency；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72 L136](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Latent Poincaré Shaping for Agentic Reinforcement Learning](https://arxiv.org/html/2602.09375v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:02:48+08:00 | root/nearest verified-success Poincare potential作value/search target；2+2+2=6 | 深入完成 | 整合：AGENT-PLANNING [Ch79 L262](../../../../books/part-07-agent/79-planning.md) |
| [A Behavioral Fingerprint for Large Language Models: Provenance Tracking via Refusal Vectors](https://arxiv.org/html/2602.09434v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:04:11+08:00 | whitebox拒绝方向+SimHash作有限family-provenance sensor；2+2+2=6 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY [Ch59 L356](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions](https://arxiv.org/html/2602.09483v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:05:20+08:00 | instruction变化加权视觉KL与GTprefix局部alternative一步KL/ribbonmask；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [Ch29 L643](../../../../books/part-04-training-system/29-sft.md) |
| [SchröMind: Mitigating Hallucinations in Multimodal Large Language Models via Solving the Schrödinger Bridge Problem](https://arxiv.org/html/2602.09528v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:06:25+08:00 | unpaired hallucinated/factual activation分布条件drift/noise替代constant steering；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23 L864](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Knowledge Integration Decay in Search-Augmented Reasoning of Large Language Models](https://arxiv.org/html/2602.09517v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:06:09+08:00 | 文档副本在旧reasoning前编码，保留原交错history的reader双causal view；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76 L440](../../../../books/part-07-agent/76-rag.md) |
| [Advancing Block Diffusion Language Models for Test-Time Scaling](https://arxiv.org/html/2602.09555v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:07:04+08:00 | 当前block置信history调有界阈值，critic role切B1第二轮生成；2+2+2=6 | 标准完成 | 仅报告：Ch24已有confidence/remasking与role/blocksize、commit/质量分责 |
| [Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs](https://arxiv.org/html/2602.09574v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:07:31+08:00 | remaining-output budget联动PUCT/answerdepth/widening的有限证据；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [Blind denoising diffusion models and the blessings of dimensionality](https://arxiv.org/html/2602.09639v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:09:05+08:00 | blind population denoiser的noise posterior、learning/noise估计误差分账；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 L224](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [The Entropic Signature of Class Speciation in Diffusion Models](https://arxiv.org/html/2602.09651v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:09:22+08:00 | 非穷尽semantic二分likelihoodratio→distinction-specific entropy时窗诊断；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 L153](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Unsupervised Layer-Wise Dynamic Test Time Adaptation for LLMs](https://arxiv.org/html/2602.09719v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:11:02+08:00 | per-query Q/V LoRA prompt-NLL更新，gold离线学习layer/step LRscale并discard；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30 L658](../../../../books/part-04-training-system/30-lora.md) |
| [When Less is More: The LLM Scaling Paradox in Context Compression](https://arxiv.org/html/2602.09789v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:12:45+08:00 | compressedmemory同decoder重建指标与counterfactual faithfulness反向；2+1+2=5 | 标准完成 | 仅报告：Ch75压缩需按consumer验证事实可读性而非重建分数已有边界 |
| [SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding](https://arxiv.org/html/2602.09825v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:13:39+08:00 | stability-conditioned layercontrast后限制raw top20 support；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23 L1002](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/html/2602.09856v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:14:24+08:00 | GUI next-screen由renderable HTML生成，visual/action reward分开；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation](https://arxiv.org/html/2602.09878v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:14:56+08:00 | 固定future→trajectorylatent generator反传优化→TCN/residualIDM；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26 L331](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation](https://arxiv.org/pdf/2602.09849v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:14:14+08:00 | 动作expert读初始stochastic-future KV，不等待完整未来pixel；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [AdaTSQ: Pushing the Pareto Frontier of Diffusion Transformers via Temporal-Sensitivity Quantization](https://arxiv.org/html/2602.09883v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:15:04+08:00 | temporal activationbit allocation与static Fisher-timeweighted weight calibration分责；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49 L912](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Routing, Cascades, and User Choice for LLMs](https://arxiv.org/html/2602.09902v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:15:30+08:00 | provider compute+abandon与user success−latency目标不同的模型内慢化反例；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56 L1395](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations](https://arxiv.org/html/2602.09924v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:16:02+08:00 | policy-specific success label与更强reasoning但linearAUROC更弱的反侧；2+1+2=5 | 标准完成 | 仅报告：Ch56 answer-before反事实效用和Ch33 continuation-policy标签/校准≠质量已有条件 |
| [VersaViT: Enhancing MLLM Vision Backbones via Task-Guided Optimization](https://arxiv.org/html/2602.09934v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:16:16+08:00 | 同视觉骨干VQA升而dense feature退的paired consumer边界；2+1+2=5 | 标准完成 | 仅报告：Ch5任务目标与Ch23表示读出/消费权责已区分 |
| [ESTAR: Early-Stopping Token-Aware Reasoning For Efficient Inference](https://arxiv.org/html/2602.10004v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:17:55+08:00 | mid-CoT stopproposal→外部classifier acceptance，policy更新后标签刷新；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56 L197](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference](https://arxiv.org/html/2602.10021v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:18:18+08:00 | query-conditioned CPS latent训练/消费分界；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md) |
| [Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning](https://arxiv.org/html/2602.10044v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:18:50+08:00 | imagined advantage×transition logprob回写dynamics，entropy/replay拟合分账；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25 L326](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Step-resolved data attribution for looped transformers](https://arxiv.org/html/2602.10097v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:20:05+08:00 | shared body每use φ_t step-gradient累积与tensor sketch测量；2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27 L800](../../../../books/part-04-training-system/27-data.md) |
| [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/html/2602.10098v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:20:07+08:00 | 初态latent监督、teacher-forced next embedding与action消费分界；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders](https://arxiv.org/html/2602.10099v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:20:08+08:00 | sphere SLERP path/tangent/exponential update与decoder radius分责；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 L172](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Olaf-World: Orienting Latent Actions for Video World Modeling](https://arxiv.org/html/2602.10104v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:20:16+08:00 | 冻结effect-reference减少latentaction局部坐标任意性；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25 L274](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [ST4VLA: Spatially Guided Training for Vision-Language-Action Models](https://arxiv.org/html/2602.10109v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:20:23+08:00 | 空间读接口/gradient回传与co-training比例局部比较；2+2+2=6 | 标准完成 | 仅报告：空间读接口、回传更新与co-training比例的局部配方不辨识新的无冲突/梯度方向保证 |
| [Autoregressive Direct Preference Optimization](https://arxiv.org/html/2602.09533v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:06:32+08:00 | segment log-margin的sum outside logσ，反馈与token粒度分开；2+1+3=6 | 深入完成 | 整合：TRAIN-DPO [Ch34 L158](../../../../books/part-04-training-system/34-dpo.md) |
| [The Wisdom of Many Queries: Complexity-Diversity Principle for Dense Retriever Training](https://arxiv.org/html/2602.09448v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:04:31+08:00 | 同doc/Q数Diverse与Paraphrase在Novel正/2Wiki负的训练证据；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [With Argus Eyes: Assessing Retrieval Gaps via Uncertainty Scoring to Detect and Remedy Retrieval Blind Spots](https://arxiv.org/html/2602.09616v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:08:32+08:00 | fixed-retriever KG competitive probe→entity选择→preindex multiview增强；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76 L241](../../../../books/part-07-agent/76-rag.md) |
| [On the Role of Embedding Magnitude in Contrastive Learning](https://arxiv.org/html/2602.09229v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T10:59:12+08:00 | 固定query正norm推理rank不变但训练temperature/梯度变，docnorm可改rank；2+1+3=6 | 深入完成 | 整合：AGENT-RAG [Ch76 L346](../../../../books/part-07-agent/76-rag.md) |
| [Self-Supervised Learning as Discrete Communication](https://arxiv.org/html/2602.09764v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:12:09+08:00 | teacher-hardbit/student BCE训练agreement channel≠交付continuous backbone；2+1+3=6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5 L145](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Quantifying Epistemic Uncertainty in Diffusion Models](https://arxiv.org/html/2602.09170v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T10:57:45+08:00 | 单步JΣJᵀ sensor与跨层子网近似可核，sharedθ全路径递推中心未闭合；2+1+3=6 | 争议 | 暂缓：全路径递推争议，见§5 |
| [Effective Reasoning Chains Reduce Intrinsic Dimensionality](https://arxiv.org/html/2602.09276v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:00:24+08:00 | LoRA rank/module扫至共同accuracy阈值作操作capacity proxy；2+1+2=5 | 标准完成 | 仅报告：Ch30 rank/module结构与‘Rank不等本质维度’已区分理论量和操作容量 |
| [Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization](https://arxiv.org/html/2602.09331v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:01:45+08:00 | spanplaceholder原answer概率drop→重权原group advantage；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33 L219](../../../../books/part-04-training-system/33-grpo.md) |
| [Stemphonic: All-at-once Flexible Multi-stem Music Generation](https://arxiv.org/html/2602.09891v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:15:15+08:00 | independent stem graphs与group initial-noise统计coupling；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 L178](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Evaluating Disentangled Representations for Controllable Music Generation](https://arxiv.org/html/2602.10058v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:19:10+08:00 | frozen probe/transform equivariance与single-vs-concat leakage分账；2+1+2=5 | 标准完成 | 仅报告：四个测量回答不同问题，而没有decoder输出控制/听感证据 |
| [Step-Size Stability in Stochastic Optimization: A Theoretical Perspective](https://arxiv.org/html/2602.09842v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:14:04+08:00 | δ prox-surrogate stability index把名义α与effective step分开；2+1+3=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28 L329](../../../../books/part-04-training-system/28-pretraining.md) |
| [Coupled Inference in Diffusion Models for Semantic Decomposition](https://arxiv.org/html/2602.09983v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:17:26+08:00 | known analytic factor priors的denoised-product energy jointguide局部接口；2+1+2=5 | 标准完成 | 仅报告：解析已知codebook上的joint energy与restart提供局部组合求解证据，未改变长期模型学习或decoder交付控制 |
| [The Critical Horizon: Inspection Design Principles for Multi-Stage Operations and Deep Reasoning](https://arxiv.org/html/2602.09394v1) | 2026-02-11T09:00:00+08:00 ～ 2026-02-11T11:03:14+08:00 | endpoint-only testing在contractive Markov/lumpability条件下的理论边界；2+1+2=5 | 标准完成 | 仅报告：只报告endpoint-only testing的条件理论 |
| [UniT: Unified Multimodal Chain-of-Thought Test-time Scaling](https://ai.meta.com/research/publications/unit-unified-multimodal-chain-of-thought-test-time-scaling/) | 2026-02-11 | single-pass无法持续消费视觉诊断→同模型交错text/image短轨迹与预算续修→重新选择顺序修订/并行选择且不混图像计数与时延；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 workflow段后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root实际POST通过 |
| [Harvest: Adaptive Photonic Switching Schedules for Collective Communication in Scale-up Domains](https://arxiv.org/html/2602.09188v1) | 2026-02-11 | 固定collective steps不能只按aggregate demand重配→连续区间拓扑成本与重配罚时联选→重新选择少量重配/静态边界；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [Ch36重配区间与费用段](../../../../books/part-04-training-system/36-distributed-training.md)；root实际同命题No Change通过 |
| [Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/html/2602.10095v1) | 2026-02-11 | 每步重复causal历史→once-per-frame E固定context/stepwise D当前帧→重选历史摊销与近似质量；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24 DDPM采样推导后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root实际POST通过 |

评分只针对拟核原新增命题，不计借用成熟原则、主题映射或机构名称。7分三项按必要深入；5–6分标准起步，有长期owner实差额则深入其受影响机制/直接反侧，不把所有附件变强制队列。准入、证据、Books分别核，不因已有覆盖/Only降分或缩池。

| [VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/html/2602.10102v1) | 2026-02-11 | 重建code混外观→生成prior/动态code及motion条件梯度分责→重选video预训练接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25重建→inverse邻接](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；root实际POST通过 |
| [Sample-Efficient Real-World Dexterous Policy Fine-Tuning via Action-Chunked Critics and Normalizing Flows](https://arxiv.org/html/2602.09580v1) | 2026-02-11 | 动作likelihood难求/step与chunk错位→可逆NF密度和chunk价值→重选保守更新接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26 likelihood替代接口](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root实际POST通过 |
| [Towards Poisoning Robustness Certification for Natural Language Generation](https://arxiv.org/html/2602.09757v1) | 2026-02-11 | AR前缀变化→区分stability/harmful-validity与聚合粒度→重选认证对象；2+2+2=6 | 争议 | 暂缓：中心certificate目标/条件方向冲突，不采用精确radius保证；认证对象差额仅报告 |
| [Squeezing More from the Stream : Learning Representation Online for Streaming Reinforcement Learning](https://arxiv.org/html/2602.09396v1) | 2026-02-11 | 串流时间相关与aux冲突→历史正交及优化器后更新分责→重选梯度保留条件；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)串流历史/实际aux更新正交分责；root实际POST通过 |
| [A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models](https://arxiv.org/html/2602.09992v1) | 2026-02-11 | 缺直接正证的语法泛化判断→统一受限检验/认知bias反证→缩小泛化解释；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE，[Ch8 正证/剩余分布线索](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)；review_20260214实际POST通过 |
| [SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents](https://arxiv.org/html/2602.09447v1) | 2026-02-11 | bugfix成绩不能代表规格建设→长程构建与阅读proxy→重选评价人口；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 规格建设评价人口](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；review_20260214实际POST通过 |
| [OSI: One-step Inversion Excels in Extracting Diffusion Watermarks](https://arxiv.org/html/2602.09494v1) | 2026-02-11 | 全噪声重建不等bit恢复→joint sign分类目标→重选水印验证费用边界；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72 latent-sign提取目标](../../../../books/part-06-ai-infrastructure/72-security.md)；review_20260214实际POST通过 |
| [ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge](https://arxiv.org/html/2602.09839v1) | 2026-02-11 | 语义相似混推理检索→轴拆分与targeted hard negatives→分开验收检索需要；2+2+2=6 | 深入完成 | 整合：AGENT-RAG，[Ch76 两轴难负例诊断](../../../../books/part-07-agent/76-rag.md)；review_20260214实际POST通过 |
| [Are Language Models Sensitive to Morally Irrelevant Distractors?](https://arxiv.org/html/2602.09416v1) | 2026-02-11 | 固定价值标签被视作稳定→无关text/image扰动反证→重选评价条件；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 无关刺激响应稳定性](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；review_20260214实际POST通过 |
| [Risk-sensitive reinforcement learning using expectiles, shortfall risk and optimized certainty equivalent risk](https://arxiv.org/html/2602.09300v1) | 2026-02-11 | 均值PG不承载风险→隐式functional梯度/两层估计→区分有效假设与风险保证；2+1+2=5 | 争议 | 暂缓：root限定Source通过；UBSR/OCE独立score乘积中心估计争议隔离 |
| [STaR: Scalable Task-Conditioned Retrieval for Long-Horizon Multimodal Robot Memory](https://arxiv.org/html/2602.09255v1) | 2026-02-11 | 静态保留全部memory→query条件IB压缩→重选证据容量与回答损失；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY，[Ch77 空间子集/呈现压缩](../../../../books/part-07-agent/77-memory.md)；review_20260214实际POST通过 |
| [CausalGDP: Causality-Guided Diffusion Policies for Reinforcement Learning](https://arxiv.org/html/2602.09207v1) | 2026-02-11 | 无结构rewardguide→learned DAG Gaussian predictive guidance→重选引导与critic责任；2+2+2=6 | 争议 | 暂缓：root限定Source通过；因果/无偏/optimal保证隔离 |
| [Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination](https://arxiv.org/html/2602.09541v1) | 2026-02-11 | 全局单方向可能错移head→mixture/OT component局部修正→重选干预身份；2+1+2=5 | 深入完成 | 整合：MODEL-MULTI-HEAD-ATTENTION，[Ch15 head内component调节](../../../../books/part-02-model/15-multi-head-attention.md)；review_20260214实际POST通过 |
| [Breaking the Pre-Sampling Barrier: Activation-Informed Difficulty-Aware Self-Consistency](https://arxiv.org/html/2602.09438v1) | 2026-02-11 | 预采样难度判断已有调用税→prompt activation校准停止→重选SC采样预算；2+2+2=6 | 深入完成 | 整合：MODEL-SAMPLING，[Ch20 追加采样预算](../../../../books/part-02-model/20-sampling.md)；review_20260214实际POST通过 |
| [Listen to the Layers: Mitigating Hallucinations with Inter-Layer Disagreement](https://arxiv.org/html/2602.09486v1) | 2026-02-11 | 只读final confidence→interlayer disagreement gated候选选择→分开看拒答/内容保留；2+1+2=5 | 深入完成 | 整合：MODEL-SAMPLING，[Ch20 候选选择门控](../../../../books/part-02-model/20-sampling.md)；review_20260214实际POST通过 |
| [Steer2Edit: From Activation Steering to Component-Level Editing](https://arxiv.org/html/2602.09870v1) | 2026-02-11 | 每token activation干预→稀疏rank1权重编译→重选局部干预与保存语义范围；2+1+2=5 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17 局部rank-one编译](../../../../books/part-02-model/17-transformer-layer.md)；review_20260214实际POST通过 |
| [Flexible Entropy Control in RLVR with Gradient-Preserving Perspective](https://arxiv.org/html/2602.09782v1) | 2026-02-11 | 统一clip不区分token区域→概率相关阈值/阶段调度→重选梯度保留和entropy解释；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO，[Ch33 概率/阶段clip阈值](../../../../books/part-04-training-system/33-grpo.md)；review_20260214实际POST通过 |
| [Why Linear Interpretability Works: Invariant Subspaces as a Result of Architectural Constraints](https://arxiv.org/html/2602.09783v1) | 2026-02-11 | 线性可读被解释为架构必然→conditional读出与非线性反例→区分分量/整个表示；2+1+2=5 | 争议 | 暂缓：root限定Source通过；selfreference严格/近似与维数证明冲突隔离 |

## 4. 证据与知识整合

以下全部采用精确v1。每项必要方法/评价位置、配置、对照和未披露字段可复查[本日逐项必要记录](../_sources/daily-20260212/V3_EVIDENCE_AND_BOOKS.md)对应ID段；旧17尾部独立原源范围另见[ROOT_REMAINING_REVIEW](../_sources/daily-20260212/ROOT_REMAINING_REVIEW.md)。只声称实际拟采用范围已核，不宣称全文、代码运行或实验复现。成本或质量数字限相应model/workload/hardware/protocol；Not Disclosed不以相邻实验补值。

### [Rollout-Training Co-Design for Efficient LLM-Based Multi-Agent Reinforcement Learning](https://arxiv.org/html/2602.09578v1)

采用：microbatch提前gradient，完整global population后才optimizer commit/version同步。边界：完整group reward/normalizer前不能定值；7.3x对MASRL，无任务质量/收敛实测。现有TRAIN-GRPO论证尚未承载这一具体接口/适用分界，已在[Ch33机制主线 L1232](../../../../books/part-04-training-system/33-grpo.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09578v1段。

### [Efficient Remote Prefix Fetching with GPU-native Media ASICs](https://arxiv.org/html/2602.09725v1)

采用：离线量化prefix codec用NVDEC，waiting-fetch与running队列分开。边界：frame restoration仍CUDA；SM不抢占≠无HBM干扰，NVENC在线过慢不授PD。现有INFER-KV-CACHE论证尚未承载这一具体接口/适用分界，已在[Ch45机制主线 L1241](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09725v1段。

### [Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments](https://arxiv.org/html/2602.09430v1)

采用：冻结atomic skill的terminal→next demo-initial分布桥接，controller后resume。边界：20tries且生成/网络失败剔除，无formal safety；不采用化学发现结果。现有MULTIMODAL-EMBODIED-VLA论证尚未承载这一具体接口/适用分界，已在[Ch26机制主线 L923](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09430v1段。

### [Agent World Model:Infinity Synthetic Environments for Agentic Reinforcement Learning](https://arxiv.org/html/2602.10090v1)

采用：DB-diff幂等false-negative/错误entity false-positive，训练评估history-limit对齐。边界：hybrid非每项严格win，Table7仅4B；runtime修复非semantic一致性。现有TRAIN-GRPO论证尚未承载这一具体接口/适用分界，已在[Ch33机制主线 L562](../../../../books/part-04-training-system/33-grpo.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.10090v1段。

### [AgentCgroup: Understanding and Controlling OS Resources of AI Agents](https://arxiv.org/html/2602.09345v1)

采用：agent-parent budget下tool-child cgroup，memory.high/freeze先于kill。边界：patched kernel依赖，3trace×50 replay及allocation延迟非live/E2E；freeze≠effect rollback。现有AGENT-PLATFORM论证尚未承载这一具体接口/适用分界，已在[Ch84机制主线 L596](../../../../books/part-07-agent/84-agent-platform.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09345v1段。

### [Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning](https://arxiv.org/html/2602.09598v1)

采用：有限suffix recoverability二分定位→branch credit→仅negative lowerclip放宽。边界：Pass@k非真实first-error/不可恢复；同16rollout非同tokens，F表文冲突不采。现有TRAIN-GRPO论证尚未承载这一具体接口/适用分界，已在[Ch33机制主线 L235](../../../../books/part-04-training-system/33-grpo.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09598v1段。

### [Where-to-Unmask: Ground-Truth-Guided Unmasking Order Learning for Masked Diffusion Language Models](https://arxiv.org/html/2602.09501v1)

采用：GT-margin只训练oracle；独立planner学where order，前半planner后半Margin。边界：部署无GT，额外planner训练/forward，Sudoku反退；长度配置冲突保留。现有MULTIMODAL-GENERATIVE-PARADIGMS论证尚未承载这一具体接口/适用分界，已在[Ch24机制主线 L306](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09501v1段。

### [Laplacian Heads Improve Transformers by Smoothing Token Representations](https://arxiv.org/html/2602.09297v1)

采用：部分head把PV改为V−PV，保留混合head与signed Wo。边界：不授全层variance单调收缩/普适NTC；语言个别任务反退。现有MODEL-SELF-ATTENTION论证尚未承载这一具体接口/适用分界，已在[Ch14机制主线 L115](../../../../books/part-02-model/14-self-attention.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09297v1段。

### [Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?](https://arxiv.org/html/2602.09937v1)

采用：opaque summary改为完整code/output/errors与goal交接的局部证据。边界：Bank小任务局部mitigation，通信成本增；非architecture唯一因果。已有覆盖：现正文Ch82完整trace/typed evidence、ordered evidence DAG、raw-message回读和conflict fallback已经承载opaque summary不够，Bank额外token/时间证据只留日报。承载位置：[AGENT-MULTI-AGENT Ch82](../../../../books/part-07-agent/82-multi-agent.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.09937v1段。

### [On the Optimal Reasoning Length for RL-Trained Language Models](https://arxiv.org/html/2602.09591v1)

采用：受测不同初始化下reasoning长度可非单调，同GPUh提供有限反侧。边界：不同模型/精度不构因果，64K仍截断；不推出通用长度阈值。仅报告：Ch33 hardcap、必要步骤成本prior与长度误税已有成立条件。本项两初始化/精度不一致的局部证据不足改变通用length控制或阶段识别规则。必要原文定位、评价配置及反侧见本日必要记录的2602.09591v1段。

### [PABU: Progress-Aware Belief Update for Efficient LLM Agents](https://arxiv.org/html/2602.09138v1)

采用：stage-progress条件attempted-actions reset，与learned observation retention分责。边界：progress不是真实authority/Markov；联合训练评价改变且输出成本增加。现有AGENT-CONTEXT论证尚未承载这一具体接口/适用分界，已在[Ch75机制主线 L538](../../../../books/part-07-agent/75-context.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09138v1段。

### [Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge](https://arxiv.org/html/2602.09341v1)

采用：语义CDP sharedprefix+localbranch审计与minority-trap训练。边界：majority-correct反退、confidence未校准，token数仅audit非总成本。现有AGENT-MULTI-AGENT论证尚未承载这一具体接口/适用分界，已在[Ch82机制主线 L616](../../../../books/part-07-agent/82-multi-agent.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09341v1段。

### [Rethinking Global Text Conditioning in Diffusion Transformers](https://arxiv.org/html/2602.09268v1)

采用：pooled MLP modulation的正负方向，区别sequence attention与output CFG。边界：dynamic指layer非time；CLIP-free需训练，高scale/对应失败/质量反退。现有MULTIMODAL-GENERATIVE-PARADIGMS论证尚未承载这一具体接口/适用分界，已在[Ch24机制主线 L184](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09268v1段。

### [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/html/2602.09383v1)

采用：length-matched truncation后残余2.2pp反侧不能只用长度解释。边界：有限labelcheck与truncate语义变化，不授真正因果bias/全50类别安全。仅报告：Ch66 format/semantic控制与length-deconfounding已承载长期judge验收条件；残余2.2pp是有价值的局部反侧，但不是新通用bias controller。必要原文定位、评价配置及反侧见本日必要记录的2602.09383v1段。

### [$n$-Musketeers: Reinforcement Learning Shapes Collaboration Among Language Models](https://arxiv.org/pdf/2602.09173v1)

采用：冻结专家无decode forward→Perceiver softprefix→policy接口。边界：全部专家forward付费；first/last75.13/75.26与capacity混杂，不授真实动态分工。现有AGENT-MULTI-AGENT论证尚未承载这一具体接口/适用分界，已在[Ch82机制主线 L342](../../../../books/part-07-agent/82-multi-agent.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09173v1段。

### [Effective MoE-based LLM Compression by Exploiting Heterogeneous Inter-Group Experts Routing Frequency and Information Density](https://arxiv.org/html/2602.09316v1)

采用：frequency+effective rank分配压缩rank，sharedbasis与sparse latent残差。边界：PᵀP不授全维lossless，η挤占预算；quality/校准反侧非E2E吞吐。现有MODEL-MOE论证尚未承载这一具体接口/适用分界，已在[Ch21机制主线 L809](../../../../books/part-02-model/21-moe.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09316v1段。

### [VLM-UQBench: A Benchmark for Modality-Specific and Cross-Modality Uncertainties in Vision Language Models](https://arxiv.org/html/2602.09214v1)

采用：instance perturbation下URR/HCC可与受测VLM答案错误失配。边界：指标非risk calibration；crossmodal改GT不用于同标签因果比较。仅报告：Ch66 semantic-neighborhood/joint UQ的sensor≠风险概率和部署slice验收已有规则；本项URR/HCC与VLM局部反侧不增加新概率接口。必要原文定位、评价配置及反侧见本日必要记录的2602.09214v1段。

### [Timing and Memory Telemetry on GPUs for AI Governance](https://arxiv.org/html/2602.09369v1)

采用：不信任host时分资源challenge观测争用与统计residency。边界：同class outsourcing允许、notsecurebinding；60GB CHAL非低侵扰生产proof/attestation。现有PLATFORM-SECURITY论证尚未承载这一具体接口/适用分界，已在[Ch72机制主线 L136](../../../../books/part-06-ai-infrastructure/72-security.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09369v1段。

### [Latent Poincaré Shaping for Agentic Reinforcement Learning](https://arxiv.org/html/2602.09375v1)

采用：root/nearest verified-success Poincare potential作value/search target。边界：geometry非真实progress；聚合差分望远镜非stepcredit，一般policy-invariance未授。现有AGENT-PLANNING论证尚未承载这一具体接口/适用分界，已在[Ch79机制主线 L262](../../../../books/part-07-agent/79-planning.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09375v1段。

### [A Behavioral Fingerprint for Large Language Models: Provenance Tracking via Refusal Vectors](https://arxiv.org/html/2602.09434v1)

采用：whitebox拒绝方向+SimHash作有限family-provenance sensor。边界：closedset非open-set；targeted擦除未验/ZKP拟议，非身份proof/promotion。现有PLATFORM-MODEL-REGISTRY论证尚未承载这一具体接口/适用分界，已在[Ch59机制主线 L356](../../../../books/part-06-ai-infrastructure/59-model-registry.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09434v1段。

### [Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions](https://arxiv.org/html/2602.09483v1)

采用：instruction变化加权视觉KL与GTprefix局部alternative一步KL/ribbonmask。边界：非完整on-policy，355→509h和单任务反退；attention不是真因果。现有TRAIN-SFT论证尚未承载这一具体接口/适用分界，已在[Ch29机制主线 L643](../../../../books/part-04-training-system/29-sft.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09483v1段。

### [SchröMind: Mitigating Hallucinations in Multimodal Large Language Models via Solving the Schrödinger Bridge Problem](https://arxiv.org/html/2602.09528v1)

采用：unpaired hallucinated/factual activation分布条件drift/noise替代constant steering。边界：distribution proxy非truth manifold；缺配置与反退，不授无成本。现有MULTIMODAL-REPRESENTATION论证尚未承载这一具体接口/适用分界，已在[Ch23机制主线 L864](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09528v1段。

### [Knowledge Integration Decay in Search-Augmented Reasoning of Large Language Models](https://arxiv.org/html/2602.09517v1)

采用：文档副本在旧reasoning前编码，保留原交错history的reader双causal view。边界：复制context/KV成本，部分task反退；semantic文档非truth/无注入保证。现有AGENT-RAG论证尚未承载这一具体接口/适用分界，已在[Ch76机制主线 L440](../../../../books/part-07-agent/76-rag.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09517v1段。

### [Advancing Block Diffusion Language Models for Test-Time Scaling](https://arxiv.org/html/2602.09555v1)

采用：当前block置信history调有界阈值，critic role切B1第二轮生成。边界：阈值界非correctness；block/role与训练人口配方，不提供新可靠性控制律。仅报告：Ch24已有confidence/remasking与role/blocksize、commit/质量分责；BACD/TCCF是受限history阈值与二阶段配方，不提供新的可靠性条件或通用下界。必要原文定位、评价配置及反侧见本日必要记录的2602.09555v1段。

### [Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs](https://arxiv.org/html/2602.09574v1)

采用：remaining-output budget联动PUCT/answerdepth/widening的有限证据。边界：per-instance cap与redistribution人口不同，input/PRM费用非hardcap，组件反退。已有覆盖：Ch79 remaining multi-resource budget、tree selection、widen/deepen/answer/stop及critic费用已承载此选择的长期控制合同，具体ρ/virtual-child配方与受限反侧留报告。承载位置：[AGENT-PLANNING Ch79](../../../../books/part-07-agent/79-planning.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.09574v1段。

### [Blind denoising diffusion models and the blessings of dimensionality](https://arxiv.org/html/2602.09639v1)

采用：blind population denoiser的noise posterior、learning/noise估计误差分账。边界：support-projection需原support；B4初始KL与小σ0完整处方未闭合，不采用。现有MULTIMODAL-GENERATIVE-PARADIGMS论证尚未承载这一具体接口/适用分界，已在[Ch24机制主线 L224](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09639v1段。

### [The Entropic Signature of Class Speciation in Diffusion Models](https://arxiv.org/html/2602.09651v1)

采用：非穷尽semantic二分likelihoodratio→distinction-specific entropy时窗诊断。边界：prior.5/complement近似、guide后crossentropy，非commit/免费gate。现有MULTIMODAL-GENERATIVE-PARADIGMS论证尚未承载这一具体接口/适用分界，已在[Ch24机制主线 L153](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09651v1段。

### [Unsupervised Layer-Wise Dynamic Test Time Adaptation for LLMs](https://arxiv.org/html/2602.09719v1)

采用：per-query Q/V LoRA prompt-NLL更新，gold离线学习layer/step LRscale并discard。边界：非Bayes/收益保证；.05固定vs.01动态及NQ反退，反向与rollback成本。现有TRAIN-LORA论证尚未承载这一具体接口/适用分界，已在[Ch30机制主线 L658](../../../../books/part-04-training-system/30-lora.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09719v1段。

### [When Less is More: The LLM Scaling Paradox in Context Compression](https://arxiv.org/html/2602.09789v1)

采用：compressedmemory同decoder重建指标与counterfactual faithfulness反向。边界：规模非单调、rank/entropy相关非因果；T3仅.6/4/8两decoder，不泛化overwrite。仅报告：Ch75压缩需按consumer验证事实可读性而非重建分数已有边界；本项size非单调和知识覆盖反侧不足辨识新普遍规模根因。必要原文定位、评价配置及反侧见本日必要记录的2602.09789v1段。

### [SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding](https://arxiv.org/html/2602.09825v1)

采用：stability-conditioned layercontrast后限制raw top20 support。边界：stable非模型校准真值；组件/任务反退与全layer求值成本。现有MULTIMODAL-REPRESENTATION论证尚未承载这一具体接口/适用分界，已在[Ch23机制主线 L1002](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09825v1段。

### [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/html/2602.09856v1)

采用：GUI next-screen由renderable HTML生成，visual/action reward分开。边界：预测screen非hiddenappstate/真实effect；offline单步与online任务人口不混。已有覆盖：Ch25 provisional executable-delta及其真实环境提交分界已经承载renderable结构预测；新增GUI人口成绩不授hidden-state真值。承载位置：[MULTIMODAL-WORLD-MODELS Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.09856v1段。

### [MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation](https://arxiv.org/html/2602.09878v1)

采用：固定future→trajectorylatent generator反传优化→TCN/residualIDM。边界：约100次优化成本，contact near-miss/calibration失败；非可达/实时安全。现有MULTIMODAL-EMBODIED-VLA论证尚未承载这一具体接口/适用分界，已在[Ch26机制主线 L331](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09878v1段。

### [BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation](https://arxiv.org/pdf/2602.09849v1)

采用：动作expert读初始stochastic-future KV，不等待完整未来pixel。边界：image single-step非action单步；chunk输出Hz非新视觉反馈频率/安全。已有覆盖：Ch26 latent future-KV/compact register已承载动作无需先materialize完整future，保留可视化分支与训练监督/consumer分权。承载位置：[MULTIMODAL-EMBODIED-VLA Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.09849v1段。

### [AdaTSQ: Pushing the Pareto Frontier of Diffusion Transformers via Temporal-Sensitivity Quantization](https://arxiv.org/html/2602.09883v1)

采用：temporal activationbit allocation与static Fisher-timeweighted weight calibration分责。边界：bit-average非物理cap/最优Pareto；3.6vs3.1、理论FLOPs非实吞吐。现有INFER-TENSORRT-LLM论证尚未承载这一具体接口/适用分界，已在[Ch49机制主线 L912](../../../../books/part-05-inference-system/49-tensorrt-llm.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09883v1段。

### [Routing, Cascades, and User Choice for LLMs](https://arxiv.org/html/2602.09902v1)

采用：provider compute+abandon与user success−latency目标不同的模型内慢化反例。边界：固定iid/twomodel/subscription存在性；非真实厂商throttle/全cascade无效。现有INFER-SCHEDULING论证尚未承载这一具体接口/适用分界，已在[Ch56机制主线 L1395](../../../../books/part-05-inference-system/56-inference-scheduling.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09902v1段。

### [LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations](https://arxiv.org/html/2602.09924v1)

采用：policy-specific success label与更强reasoning但linearAUROC更弱的反侧。边界：linear读出弱非信息消失；cost算术不一，不授可转移校准/生产节省。仅报告：Ch56 answer-before反事实效用和Ch33 continuation-policy标签/校准≠质量已有条件；新linear-AUROC反侧无可转移成功控制接口，费用算术不采用。必要原文定位、评价配置及反侧见本日必要记录的2602.09924v1段。

### [VersaViT: Enhancing MLLM Vision Backbones via Task-Guided Optimization](https://arxiv.org/html/2602.09934v1)

采用：同视觉骨干VQA升而dense feature退的paired consumer边界。边界：表示≠encoder universally best；joint1epoch/lr已披露，不采用领域任务或全因果。仅报告：Ch5任务目标与Ch23表示读出/消费权责已区分；VQA与dense反向的局部paired证据不建立新的通用视觉骨干或领域应用机制。必要原文定位、评价配置及反侧见本日必要记录的2602.09934v1段。

### [ESTAR: Early-Stopping Token-Aware Reasoning For Efficient Inference](https://arxiv.org/html/2602.10004v1)

采用：mid-CoT stopproposal→外部classifier acceptance，policy更新后标签刷新。边界：一致/plateau非真值或tail证书；污染/branch费用与阈值质量覆盖反侧。现有INFER-SCHEDULING论证尚未承载这一具体接口/适用分界，已在[Ch56机制主线 L197](../../../../books/part-05-inference-system/56-inference-scheduling.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.10004v1段。

### [Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference](https://arxiv.org/html/2602.10021v1)

采用：query-conditioned CPS latent训练/消费分界。边界：query-aware内容非数量自适应/事实清洗；7x runtime未证留report。已有覆盖：Ch75 query-aware slots、consumer-specific压缩及future-sufficiency已承载内容选择/消费条件，DRIFT bucket固定长度与局部runtime主张不另写。承载位置：[AGENT-CONTEXT Ch75](../../../../books/part-07-agent/75-context.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.10021v1段。

### [Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning](https://arxiv.org/html/2602.10044v1)

采用：imagined advantage×transition logprob回写dynamics，entropy/replay拟合分账。边界：optimism非uncertainty/可达性；tabular不移植NN POMDP，崩坏/成本反侧。现有MULTIMODAL-WORLD-MODELS论证尚未承载这一具体接口/适用分界，已在[Ch25机制主线 L326](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.10044v1段。

### [Step-resolved data attribution for looped transformers](https://arxiv.org/html/2602.10097v1)

采用：shared body每use φ_t step-gradient累积与tensor sketch测量。边界：sum恢复body gradient-similarity非删除因果/loop progress；存储/反向成本。现有TRAIN-DATA论证尚未承载这一具体接口/适用分界，已在[Ch27机制主线 L800](../../../../books/part-04-training-system/27-data.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.10097v1段。

### [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/html/2602.10098v1)

采用：初态latent监督、teacher-forced next embedding与action消费分界。边界：ELBO/KL桥接未采，horizon/机器人budget不一，不授未来真实可达。已有覆盖：Ch25 next-embedding target/consumer与Ch26冻结forward/inverse交接共同承载训练future标签与action消费分责；不为特定Qwen/VJEPA配方另造演进。承载位置：[MULTIMODAL-WORLD-MODELS Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.10098v1段。

### [Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders](https://arxiv.org/html/2602.10099v1)

采用：sphere SLERP path/tangent/exponential update与decoder radius分责。边界：sinc/Alg2时钟未闭合不照录；非唯一几何根因/所有semantic只角度。现有MULTIMODAL-GENERATIVE-PARADIGMS论证尚未承载这一具体接口/适用分界，已在[Ch24机制主线 L172](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.10099v1段。

### [Olaf-World: Orienting Latent Actions for Video World Modeling](https://arxiv.org/html/2602.10104v1)

采用：冻结effect-reference减少latentaction局部坐标任意性。边界：mean difference望远镜非完整序列；camera/environment混淆，非真实actuator因果。现有MULTIMODAL-WORLD-MODELS论证尚未承载这一具体接口/适用分界，已在[Ch25机制主线 L274](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.10104v1段。

### [ST4VLA: Spatially Guided Training for Vision-Language-Action Models](https://arxiv.org/html/2602.10109v1)

采用：空间读接口/gradient回传与co-training比例局部比较。边界：PSS对子空间方向不敏感非无冲突；组合配方不辨识.5梯度唯一收益/scale law。仅报告：空间读接口、回传更新与co-training比例的局部配方不辨识新的无冲突/梯度方向保证；PSS和成功相关不能改变可学习表示与真实动作的现有分权。必要原文定位、评价配置及反侧见本日必要记录的2602.10109v1段。

### [Autoregressive Direct Preference Optimization](https://arxiv.org/html/2602.09533v1)

采用：segment log-margin的sum outside logσ，反馈与token粒度分开。边界：pair偏好非steptruth；prefix shift/条件partition限制，细度/输出成本反侧。现有TRAIN-DPO论证尚未承载这一具体接口/适用分界，已在[Ch34机制主线 L158](../../../../books/part-04-training-system/34-dpo.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09533v1段。

### [The Wisdom of Many Queries: Complexity-Diversity Principle for Dense Retriever Training](https://arxiv.org/html/2602.09448v1)

采用：同doc/Q数Diverse与Paraphrase在Novel正/2Wiki负的训练证据。边界：CW仅4dataset相关且重复condition；非复杂度因果/通用threshold。已有覆盖：Ch27训练quality、集合diversity与proxy反退段已经承载多样性不等普遍质量；同doc/Q数的新条件反侧留日报。承载位置：[TRAIN-DATA Ch27](../../../../books/part-04-training-system/27-data.md)。必要原文定位、评价配置及反侧见本日必要记录的2602.09448v1段。

### [With Argus Eyes: Assessing Retrieval Gaps via Uncertainty Scoring to Detect and Remedy Retrieval Blind Spots](https://arxiv.org/html/2602.09616v1)

采用：fixed-retriever KG competitive probe→entity选择→preindex multiview增强。边界：RPS非校准失败概率/truth；Jina synthesis反退/等膨胀选择未控。现有AGENT-RAG论证尚未承载这一具体接口/适用分界，已在[Ch76机制主线 L241](../../../../books/part-07-agent/76-rag.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09616v1段。

### [On the Role of Embedding Magnitude in Contrastive Learning](https://arxiv.org/html/2602.09229v1)

采用：固定query正norm推理rank不变但训练temperature/梯度变，docnorm可改rank。边界：scratch/FT异向，Dot仍对称；不授task-symmetry普遍律。现有AGENT-RAG论证尚未承载这一具体接口/适用分界，已在[Ch76机制主线 L346](../../../../books/part-07-agent/76-rag.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09229v1段。

### [Self-Supervised Learning as Discrete Communication](https://arxiv.org/html/2602.09764v1)

采用：teacher-hardbit/student BCE训练agreement channel≠交付continuous backbone。边界：logdet非离散熵/MI证明；bit/reset不单调，额外teacher费用。现有WORLDVIEW-REPRESENTATION论证尚未承载这一具体接口/适用分界，已在[Ch5机制主线 L145](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09764v1段。

### [Quantifying Epistemic Uncertainty in Diffusion Models](https://arxiv.org/html/2602.09170v1)

采用：单步JΣJᵀ sensor与跨层子网近似可核，sharedθ全路径递推中心未闭合。边界：不授calibrated epistemic；stateJacobian/cross同阶、p方向/样本冲突隔离。暂缓：中心sharedθ全路径variance递推/epistemic归因争议，最终暂缓，单步sensor的限定核验不认证完整Evidence；不进入Books。必要原文定位、评价配置及反侧见本日必要记录的2602.09170v1段。

### [Effective Reasoning Chains Reduce Intrinsic Dimensionality](https://arxiv.org/html/2602.09276v1)

采用：LoRA rank/module扫至共同accuracy阈值作操作capacity proxy。边界：非理论minimum dimension/UAT或压缩因果；人口/阈值与sweep成本。仅报告：Ch30 rank/module结构与‘Rank不等本质维度’已区分理论量和操作容量；14strategy局部sweep不提供新的跨任务minimum dimension或压缩因果律。必要原文定位、评价配置及反侧见本日必要记录的2602.09276v1段。

### [Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization](https://arxiv.org/html/2602.09331v1)

采用：spanplaceholder原answer概率drop→重权原group advantage。边界：OOD dependency非cause/正确性；负adv也重权，32–74%额外forward。现有TRAIN-GRPO论证尚未承载这一具体接口/适用分界，已在[Ch33机制主线 L219](../../../../books/part-04-training-system/33-grpo.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09331v1段。

### [Stemphonic: All-at-once Flexible Multi-stem Music Generation](https://arxiv.org/html/2602.09891v1)

采用：independent stem graphs与group initial-noise统计coupling。边界：推理同seed≠联合训练/语义；one/two/Kpass与活动通道反退。现有MULTIMODAL-GENERATIVE-PARADIGMS论证尚未承载这一具体接口/适用分界，已在[Ch24机制主线 L178](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09891v1段。

### [Evaluating Disentangled Representations for Controllable Music Generation](https://arxiv.org/html/2602.10058v1)

采用：frozen probe/transform equivariance与single-vs-concat leakage分账。边界：小Δ非independence，negativeprobe非无信息；缺decoder输出控制/听感证据。仅报告：四个测量回答不同问题，而没有decoder输出控制/听感证据；cross-branch probe反侧不把representation decomposition推进为可控生成保证。必要原文定位、评价配置及反侧见本日必要记录的2602.10058v1段。

### [Step-Size Stability in Stochastic Optimization: A Theoretical Perspective](https://arxiv.org/html/2602.09842v1)

采用：δ prox-surrogate stability index把名义α与effective step分开。边界：同state/sample非跨轨迹；A1/A2/NGN lower-model条件，非Adam/LLM普效。现有TRAIN-PRETRAINING论证尚未承载这一具体接口/适用分界，已在[Ch28机制主线 L329](../../../../books/part-04-training-system/28-pretraining.md)整合两段并保留旧方案；必要原源、owner差额与实际正文/邻接/末注均独立通过，不由POST授日级完成。必要原文定位、评价配置及反侧见本日必要记录的2602.09842v1段。

### [Coupled Inference in Diffusion Models for Semantic Decomposition](https://arxiv.org/html/2602.09983v1)

采用：known analytic factor priors的denoised-product energy jointguide局部接口。边界：DPS近似/energy非likelihood；restart不独立，不授learnedsemantic/精确posterior。仅报告：解析已知codebook上的joint energy与restart提供局部组合求解证据，未改变长期模型学习或decoder交付控制；DPS近似、不正规energy和非独立restart均保留，不因toy本身删除准入。必要原文定位、评价配置及反侧见本日必要记录的2602.09983v1段。

### [The Critical Horizon: Inspection Design Principles for Multi-Stage Operations and Deep Reasoning](https://arxiv.org/html/2602.09394v1)

采用：endpoint-only testing在contractive Markov/lumpability条件下的理论边界。边界：R-only下界未桥接全文trajectory归因；semantic多对一非严格收缩，中心claim隔离。仅报告：只报告endpoint-only testing的条件理论；R-only测试下界尚未桥接可读全文轨迹的训练归因，不能将这个中心claim整合为真实LLM诊断原则。必要原文定位、评价配置及反侧见本日必要记录的2602.09394v1段。

### [UniT: Unified Multimodal Chain-of-Thought Test-time Scaling](https://ai.meta.com/research/publications/unit-unified-multimodal-chain-of-thought-test-time-scaling/)

2026-10-08新增，采用当时官方Feb11稿而非后来arXiv扩写。§3.1多模型只造训练数据，12K过滤轨迹使部署同一Bagel模型学习verification/subgoal/content-memory交错text/image，nested CFG保留所有历史图像；§3.3 EOS抑制/强制续修与上限截断只是停止策略。§5.1 C=N仅生成图像数，排除selection/verification費且未匹配wall-clock；顺序修订与并行候选是质量/串行延迟取舍，不採2.5倍端到端加速。§5.2/Tab5为训练recipe消融，不授三行为纯因果；§5.4有hallucination退化、子目标冲突和base能力限制。标准分5但具体owner缺口需定点深入，支持与反侧足即停，不遍历其余附录。必要官方PDF页1–12已读，root独立Source/PRE/实际Ch24两段完整邻接与末注POST通过；只补统一模型内化纠正与预算/计数分工，不复制既有validator原则，不授内部检查真值、实现核验或生产保证。

### [Harvest: Adaptive Photonic Switching Schedules for Collective Communication in Scale-up Domains](https://arxiv.org/html/2602.09188v1)

新增exact-v1，采用§3–4连续固定steps区间拓扑成本与重配罚时的联合选择，不采用Algorithm1有不一致的初始化/索引作为运行实现或普遍最优。§6数值/packet仿真与8GPU/BlueField3/eSwitch仿真后追加物理切换罚时分别看，不授真实光交换生产或完整训练E2E。高罚时/小消息退回静态、All-to-All多port收益缩小等反侧保留；[必要原件与判断](../_sources/daily-20260212/supplement-20261008-harvest-review.md)可复查。root实际Source与Ch36现有§1768–1784同命题覆盖通过，No Change，不为新论文造Books diff。

### [Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/html/2602.10095v1)

新增exact-v1，采用§4–5每帧causal encoder与每denoise-step framewise decoder分责；低分辨率clean-history/高分辨率current-noisy输入适配不混，联合训练与self-rollout蒸馏均付费。Table1–3受限H100/batch1对照保留decoder深度、首帧成本和semantic退步；不同参数/训练不授matched quality普遍提速。§7残余crossframe attention与后段表示不稳定限制fixed-context近似，不授充分统计/精确joint/world-state。[必要原件与判断](../_sources/daily-20260212/supplement-20261008-scd-review.md)；root实际Source/PRE与Ch24两段/完整采样器→条件→观测约束邻接/自身末注POST通过，差额深入已落实。

### [VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/html/2602.10102v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。重建code混外观→生成prior/动态code及motion条件梯度分责→重选video预训练接口；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-videoworld2-review.md)可复查，不授实现核验或复现。整合：MULTIMODAL-WORLD-MODELS [Ch25重建→inverse邻接](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；root实际POST通过。root必要Source、owner PRE与实际POST通过，锁释放；仅本项，不授DAY。

### [Sample-Efficient Real-World Dexterous Policy Fine-Tuning via Action-Chunked Critics and Normalizing Flows](https://arxiv.org/html/2602.09580v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。动作likelihood难求/step与chunk错位→可逆NF密度和chunk价值→重选保守更新接口；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-softflow-review.md)可复查，不授实现核验或复现。整合：MULTIMODAL-EMBODIED-VLA [Ch26 likelihood替代接口](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root实际POST通过。root必要Source、owner PRE与实际POST通过，锁释放；仅本项，不授DAY。

### [Towards Poisoning Robustness Certification for Natural Language Generation](https://arxiv.org/html/2602.09757v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。AR前缀变化→区分stability/harmful-validity与聚合粒度→重选认证对象；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-tpa-review.md)可复查，不授实现核验或复现。暂缓：中心certificate目标/条件方向冲突，不采用精确radius保证；认证对象差额仅报告。审阅结果为争议，root必要Source限定通过；中心保证隔离，root认证对象仅报告/中心争议暂缓处置通过，不授争议保证或DAY。

### [Squeezing More from the Stream : Learning Representation Online for Streaming Reinforcement Learning](https://arxiv.org/html/2602.09396v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。串流时间相关与aux冲突→历史正交及优化器后更新分责→重选梯度保留条件；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-stream-review.md)可复查，不授实现核验或复现。整合：TRAIN-PRETRAINING，[Ch28串流更新投影](../../../../books/part-04-training-system/28-pretraining.md)新720/完整714–731与末注经root实际POST通过；锁释放，未核实现/复现，不授DAY。

### [A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models](https://arxiv.org/html/2602.09992v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。缺直接正证的语法泛化判断→统一受限检验/认知bias反证→缩小泛化解释；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-posh-review.md)可复查，不授实现核验或复现。整合：WORLDVIEW-LLM-INTELLIGENCE，[Ch8 正证/剩余分布线索](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)；review_20260214实际POST通过；写后核验时新53，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3统一检验保留去除直接正证后的剩余分布线索；binding抽样仍有泄漏、任务/预算不完全同构，认知bias没有稳定改善，不外推先天语法已被证伪。gap定点深入完成；只本项通过，不授DAY。

### [SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents](https://arxiv.org/html/2602.09447v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。bugfix成绩不能代表规格建设→长程构建与阅读proxy→重选评价人口；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-swe-review.md)可复查，不授实现核验或复现。整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 规格建设评价人口](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；review_20260214实际POST通过；写后核验时新430，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3.1/Table3的规格建设人口与bugfix不同；§3.3/Table6–7的Read相关量不能证明因果瓶颈，运行隐藏测试可见反馈也不等于盲验收或生产正确。gap定点深入完成；只本项通过，不授DAY。

### [OSI: One-step Inversion Excels in Extracting Diffusion Watermarks](https://arxiv.org/html/2602.09494v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。全噪声重建不等bit恢复→joint sign分类目标→重选水印验证费用边界；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-osi-review.md)可复查，不授实现核验或复现。整合：PLATFORM-SECURITY，[Ch72 latent-sign提取目标](../../../../books/part-06-ai-infrastructure/72-security.md)；review_20260214实际POST通过；写后核验时新1148，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3.2联合latent-sign分类与Table2单次A100提取费用支持目标更换，不代表整个生成链降本；AppB iid比特假设FPR不是大样本实测，更不是安全真实性。gap定点深入完成；只本项通过，不授DAY。

### [ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge](https://arxiv.org/html/2602.09839v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。语义相似混推理检索→轴拆分与targeted hard negatives→分开验收检索需要；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-ark-review.md)可复查，不授实现核验或复现。整合：AGENT-RAG，[Ch76 两轴难负例诊断](../../../../books/part-07-agent/76-rag.md)；review_20260214实际POST通过；写后核验时新294，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3.1–3.2拆分reasoning/knowledge与targeted hard negatives支持混杂诊断；§4.1 caption/per-subtype/macro对照不构成同输入完全析因，不将检索匹配升级为truth。gap定点深入完成；只本项通过，不授DAY。

### [Are Language Models Sensitive to Morally Irrelevant Distractors?](https://arxiv.org/html/2602.09416v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。固定价值标签被视作稳定→无关text/image扰动反证→重选评价条件；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-values-review.md)可复查，不授实现核验或复现。整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 无关刺激响应稳定性](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；review_20260214实际POST通过；写后核验时新547，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。两套受限choice协议与无关text/image扰动显示响应条件应配对验收；局部negative、位置/模型差异与多轮累计成本保留，不推断伦理实体或现实行动。gap定点深入完成；只本项通过，不授DAY。

### [Risk-sensitive reinforcement learning using expectiles, shortfall risk and optimized certainty equivalent risk](https://arxiv.org/html/2602.09300v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。均值PG不承载风险→隐式functional梯度/两层估计→区分有效假设与风险保证；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-risk-review.md)可复查，不授实现核验或复现。暂缓：root限定Source通过；UBSR/OCE独立score乘积中心估计争议隔离。审阅结果为争议，root必要Source限定通过；中心保证隔离，root实际owner暂缓处置通过，未写Books；重开条件见[具体争议](../_sources/daily-20260212/supplement-20261008-owner-next.md)，不授争议保证或DAY。

### [STaR: Scalable Task-Conditioned Retrieval for Long-Horizon Multimodal Robot Memory](https://arxiv.org/html/2602.09255v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。静态保留全部memory→query条件IB压缩→重选证据容量与回答损失；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-star-review.md)可复查，不授实现核验或复现。整合：AGENT-MEMORY，[Ch77 空间子集/呈现压缩](../../../../books/part-07-agent/77-memory.md)；review_20260214实际POST通过；写后核验时新391，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。IV-A/B Eq3–11只采用query空间子集筛选和cluster代表帧呈现的不同职责；错误停止式、最优性及无损充分统计隔离，原始证据指针与压缩损失仍须保留。gap定点深入完成；只本项通过，不授DAY。

### [CausalGDP: Causality-Guided Diffusion Policies for Reinforcement Learning](https://arxiv.org/html/2602.09207v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。无结构rewardguide→learned DAG Gaussian predictive guidance→重选引导与critic责任；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-causal-review.md)可复查，不授实现核验或复现。暂缓：root限定Source通过；因果/无偏/optimal保证隔离。审阅结果为争议，root必要Source限定通过；中心保证隔离，root实际owner暂缓处置通过，未写Books；重开条件见[具体争议](../_sources/daily-20260212/supplement-20261008-owner-next.md)，不授争议保证或DAY。

### [Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination](https://arxiv.org/html/2602.09541v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。全局单方向可能错移head→mixture/OT component局部修正→重选干预身份；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-scalpel-review.md)可复查，不授实现核验或复现。整合：MODEL-MULTI-HEAD-ATTENTION，[Ch15 head内component调节](../../../../books/part-02-model/15-multi-head-attention.md)；review_20260214实际POST通过；写后核验时新123，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3.4的head内mixture membership与mean校正可调局部组件概率；离线OT后的argmax映射不是在线完整Schrödinger bridge，也不证明减少幻觉即可取得真值。gap定点深入完成；只本项通过，不授DAY。

### [Breaking the Pre-Sampling Barrier: Activation-Informed Difficulty-Aware Self-Consistency](https://arxiv.org/html/2602.09438v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。预采样难度判断已有调用税→prompt activation校准停止→重选SC采样预算；2+2+2=6。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-act-review.md)可复查，不授实现核验或复现。整合：MODEL-SAMPLING，[Ch20 追加采样预算](../../../../books/part-02-model/20-sampling.md)；review_20260214实际POST通过；写后核验时新338，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3.1–3.2 prompt activation probe分配追加采样预算；新dataset仍需tau校准，§4各stop标准与抽样预算不可合并，probe训练/阈值和生成总费保留。gap定点深入完成；只本项通过，不授DAY。

### [Listen to the Layers: Mitigating Hallucinations with Inter-Layer Disagreement](https://arxiv.org/html/2602.09486v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。只读final confidence→interlayer disagreement gated候选选择→分开看拒答/内容保留；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-cocoa-review.md)可复查，不授实现核验或复现。整合：MODEL-SAMPLING，[Ch20 候选选择门控](../../../../books/part-02-model/20-sampling.md)；review_20260214实际POST通过；写后核验时新340，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3.2 Eq3–5只为已有候选选择门控；Table7 alpha0对照含搜索收益，selective populations必须与拒答/内容保留一起报告，不把层间agreement当正确性。gap定点深入完成；只本项通过，不授DAY。

### [Steer2Edit: From Activation Steering to Component-Level Editing](https://arxiv.org/html/2602.09870v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。每token activation干预→稀疏rank1权重编译→重选局部干预与保存语义范围；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-steer-review.md)可复查，不授实现核验或复现。整合：MODEL-TRANSFORMER-LAYER，[Ch17 局部rank-one编译](../../../../books/part-02-model/17-transformer-layer.md)；review_20260214实际POST通过；写后核验时新403，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。§3 rank-one编辑仅保持与输入方向正交的局部分量，不授全语义不变；AppD Mistral直接退化、效用损失与编译/干预费用靠近采用命题。gap定点深入完成；只本项通过，不授DAY。

### [Flexible Entropy Control in RLVR with Gradient-Preserving Perspective](https://arxiv.org/html/2602.09782v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。统一clip不区分token区域→概率相关阈值/阶段调度→重选梯度保留和entropy解释；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-flex-review.md)可复查，不授实现核验或复现。整合：TRAIN-GRPO，[Ch33 概率/阶段clip阈值](../../../../books/part-04-training-system/33-grpo.md)；review_20260214实际POST通过；写后核验时新199，具体原owner差额与完整邻接裁决见[owner比较](../_sources/daily-20260212/supplement-20261008-owner-next.md)及[独立POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)。Eq5–6的logit近似不授参数梯度精确entropy符号；仅采用§4概率/阶段clip调度，§5.3 passK绑定采样预算和局部条件，不授最优训练配方。gap定点深入完成；只本项通过，不授DAY。

### [Why Linear Interpretability Works: Invariant Subspaces as a Result of Architectural Constraints](https://arxiv.org/html/2602.09783v1)

新增exact-v1，公开日通过具名包络复核，不把Submitted/Updated/DataCitecreated本身当公开日。线性可读被解释为架构必然→conditional读出与非线性反例→区分分量/整个表示；2+1+2=5。作者已读支持该命题的必要方法、关键评价与直接反侧；[原件位置与受限判断](../_sources/daily-20260212/supplement-20261008-linear-review.md)可复查，不授实现核验或复现。暂缓：root限定Source通过；selfreference严格/近似与维数证明冲突隔离。审阅结果为争议，root必要Source限定通过；中心保证隔离，root实际owner暂缓处置通过，未写Books；重开条件见[具体争议](../_sources/daily-20260212/supplement-20261008-owner-next.md)，不授争议保证或DAY。

## 5. 缺口与下一步

以下日期、必要来源缺段和争议保证均为本窗终态保留项；被隔离的材料或子命题不用于正面证据、不进入Books、不支持无遗漏断言。每项的可接受替代与定点重开条件如下及所链接原件；已采用且核验通过的有限子命题不因此失效。

原58部分普通待办0，原有效验收复用。本轮21新增的扫描、准入、必要Source、owner裁决与16实际整合POST均已处理到限定终态，root完整六部分实际DAY通过并授权完成，普通待办0；完成态机器结果见§6，不把安全终态称为全部Coverage/Evidence通过。[精确停点](../_sources/daily-20260212/supplement-20261008-checkpoint.md)保存层级，不把源缺口或公式争议称普通未读。新增日期隔离OmniSafety10161、GRU-Mem10560/RLCER10885与later7：潜在贡献不等于Feb11已公开，原字段/有限恢复/具体替代见[日期终态](../_sources/daily-20260212/supplement-20261008-date-final.md)及[筛选分流](../_sources/daily-20260212/supplement-20261008-screening.md)，不评分/Source/Books绕门，不支撑无遗漏，只重开对应family日期。UniT原日期/正文限制已由自然日授权与当时官方原稿解除；以下旧保留项仍隔离。

- [FLARE2602.09170v1](https://arxiv.org/html/2602.09170v1)：中心sharedθ全路径variance递推/epistemic归因未闭合；单步JΣJᵀ和子网sensor已核但不进入Books。重开需一致state-Jacobian/sharedθ-cross递推、相对误差成立条件与同人口统计，不能靠posterior集中忽略同阶cross，也不授冲突p值。
- 新增 [Risk2602.09300v1](https://arxiv.org/html/2602.09300v1)：UBSR/OCE独立cost/score配对中心估计不支持一般risk-gradient，暂缓算法/收敛/安全保证，不写Books。需官方勘误或证明正确的配对/独立根估计构造，只重开本family估计器与Ch32目标比较。
- 新增 [CausalGDP2602.09207v1](https://arxiv.org/html/2602.09207v1)：预测DAG/Gaussian guidance可描述，r*/nextstate采样时输入责任未核、删reward权重与稳定/性能保证冲突；不授因果/无偏/生产采用，不进Books。重开需可核采样时输入/实现顺序及相关官方勘误，不修全证明。
- 新增 [Linear2602.09783v1](https://arxiv.org/html/2602.09783v1)：线性可读先验、类内零空间与严格whole-state/selfreference保证未闭合，B4只dominant近似且保留eta；暂缓无条件architecture理论，不写Books。重开需官方明确假设、剩余分量与严格/近似界。TPA中心certificate、STaR exact-stop、Flex exact-entropy保证亦分别隔离在本项§4/raw；后两只将可支持的局部接口写入，不借整合消除原争议。
- [Critical Horizon2602.09394v1](https://arxiv.org/html/2602.09394v1)：保留endpoint-only条件测试下界，全文轨迹训练归因claim隔离。重开需同一可观测域下界或实际LLM抽象/收缩证据，不用R-only结果替代Def2.4全文可观测轨迹。
- [RecursiveVLM2602.09080v1](https://arxiv.org/abs/2602.09080v1)：Submitted Feb9 17:58:23Z早于本批cutoff，registered只能给最迟上界；缺真实首公开batch或更早正文时刻，不计58、不采用Books。09063/09051/09038也更早提交，但已明确贡献/范围关闭，不为不改变处置另请求日期。
- [Thinking with Drafting2602.11731](https://arxiv.org/abs/2602.11731v1)窗外恢复线索：Seed官方PublishDate1770825600000为北京时间Feb12，arXiv事件Feb13；初次UTC date被误写为本窗Feb11，已纠正。不请求Feb11先行稿，不评分深审，不开启其真实归属日。
- [中文Forge](https://minimax.cn/blog/forge-scalable-agent-rl)：root实际原页L64–66 Feb12 date-only，与中文news Feb13/英文Blog Feb14不一致；§3.1真实WindowedFIFO可有贡献，不能合并为M2.5 launch未披露机制关闭。缺本稿最早正文public时刻/完整包络；整天不落本窗，不计58，取得只重开此family。正文可读，不冒称不可访问或未读已通过。
- 来源历史目录保留：OpenAI、Anthropic、Moonshot、Seed、MiMo等当前首屏/有限官方搜索不能恢复完整历史；Tencent动态全部入口两timeout且renderType0博客切片不足以覆盖全部Research。Qwen原生40条与ZAI可读目标历史段限制已缩窄，Meta UniT日期/正文限制已解除，不能继续列为日期隔离。恢复须具体本窗原始历史目录/官方本批记录，不能把访问失败写零命中。已完成可用有限检查，不让外部目录长期缺失成为无限扫描。

窗外线索：后来Forge详细说明、GLM5技术报告和Seedance2 April稿不倒灌launch；另SPEED2604.09557、Expert2603.00054、WebGPU2604.02344、AtomicRAG2604.20844、RouterCalibration2603.02217、AutoHarness2603.03329、CktEvo2603.08718仅后来Mar/Apr arXiv事件可认证，Submitted Feb不授public，原6有限先行正文恢复无结果，CktEvo仅现有AB/history与ID规则未给Feb11正文，不虚构其DataCite字段/查询；具名原字段/潜在delta与精确重开见[筛选记录](../_sources/daily-20260212/supplement-20261008-screening.md)。本次不开启真实归属日，不评分/全文/Books，也不创建他日/Weekly。已隔离理论/recipe争议不扩大为整篇所有结论无效。

## 6. 复核

本轮2026-10-08复核者：root（非作者）；review_20260214独立核11处实际POST。结论：通过（root已实际完整六部分增量DAY并授权完成）。root实核14每日来源实际查询/主题/分页停止及贡献理由、21拟采用/保留必要Source、日期23＋extra8原字段和具名有限隔离；11个实际owner/邻接逐字PRE及3中心争议暂缓处置通过。UniT/SCD/VW2/SOFT/Stream此前actualPOST有效，新增11处实际正文/完整邻接/本人末注经[独立逐项POST](../_sources/daily-20260212/supplement-20261008-independent-post-next.md)11/11通过，root已实际读记录；所有锁释放。原58家族/§4前缀/窗口已root逐字核不变。新增12贡献关闭及later3关闭原AB校准通过；CktEvo误模板排除已纠正为潜在评价contract且日期隔离，受影响只此1项，其余未发现共同错误理由。原冻结范围外代表抽检结果有效复用，不声称整个宽库全量筛选。root日级独核确认21新家族全部必要Source/日期/owner及实际POST、具名关闭与有限来源停点已处理到安全终态；三跨界日期项、later7、四中心暂缓及历史源缺口不授正面保证，不支撑无遗漏。以下旧“通过”仅原验收，本轮DAY以本段实际增量裁决为准。

本轮完成态机器检查：实际V3通过1份；79表行＝79唯一家族＝79证据小标题，原58表行逐字保留true、原窗口true、原连续§4前缀true，187个本地引用全部存在、报告尾随空白0。本人Books/README/补查Markdown限定unstaged与cached diff-check通过；本日完整sources限定unstaged通过，但已在index的raw原件cached检查仍有尾空白告警（4501行输出，首例acteval.json的L155空行），未改index或清洗原件，不声称完整sources cached通过。完成态首次机器检查要求§5显式“终态保留项/不用于正面证据/定点重开”，已仅补清晰隔离说明后复跑通过，未改校验器或提升任何证据权限。本任务未stage、commit、push或改共享LearningState/合同/他日报；以下旧机器结果只对应原验收。

复核者：root（非作者）；旧17普通必要原源由feb12_remaining_review独立核后root汇总。

结论：通过

root已完整实际读六部分，并复跑V3及Books/本日限定cached与unstaged diff-check；全部必要准入、证据、日期与38实际POST结果可复用，终态隔离安全，不授互联网上无遗漏或被隔离材料的正面保证。按root授权标记完成，不由作者自授日级Gate。

实际范围：首批16、第二批45与补检20完整题摘分批实际原文校准，代表关闭与有安全/设计反证信号的10019/09433/09629定点核心已核；58拟入选必要原文支持及直接反侧全部独立核，采未变有效结果不重读附件。root实际逐日期原字段/history、官方排程与先行日期例外，按58唯一ID冻结；38整合实际正文、完整相邻衔接与末注全部POST通过，7coverage/12Only/1暂缓也按具体论点核，不以缺方法名造diff。剩余明确标题范围外项按上述来源/主题/理由代表抽检，未称全量逐条验证。

计数问题已修复：小标题数曾漏掉inline09394并夹入关闭09629，逐ID最终58=38+7+12+1，未删有效准入；09934联合训练epoch/LR已按独立原源纠正；Sci-VLA/KVFetcher/09555/09229按v1题名，不继承后来名或机制。评分共同误理由也已局部纠正：09789/09924/09934/10058/09983/09394的原新增仅提供有限consumer/probe/codebook/条件测试证据，以及09591两初始化/精度混杂的长度反侧、09214 URR/HCC局部VLM sensor，Durability均3→2，各2+1+2=5；不是因Only降分，准入及实际审阅保留，未把通用foundation原则归功于本稿。

机器结果：`python3 scripts/validate_research.py --report papers/2026/02/12/README.md`通过1份V3；58表行/58唯一ID与58证据小标题一致，96个本地引用存在、尾随空白0；本日README/cache限定unstaged与cached `git diff --check`均通过。机器初次指出表头、固定状态字段及必查来源“检索受限”角色不符，已仅修报告字段：实际历史覆盖缺段改为“受阻”，辅助搜索局限仍保留，不改校验器、不扩大覆盖断言。scoped Books diffcheck已通过但不替代语义Gate；本任务未stage、commit或push，未修改共享LearningState/合同/他日。
