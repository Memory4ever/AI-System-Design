# Daily Research — 2026-03-07

**规范：** V3
**窗口：** 2026-03-06T09:00:00+08:00 ～ 2026-03-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T22:53:34+08:00

## 1. 结论

本轮按当前合同独立处理本日，冻结19唯一候选家族（2官方、17arXiv）：14深入完成、2标准完成、1关闭，CSV/DBC两中心主张争议隔离。8处Books实际整合且全部实际写后独立复核通过、6处具体已有覆盖、2仅报告、3暂缓；root非作者日级Gate通过，普通待办0。此前2家族“最终分母”撤回，未继承旧593身份/31候选池、旧评分或完成标签。

14个Daily源均有实际有限检查和停止点，必要历史子入口仍精确隔离，不能称全源正面Coverage或无遗漏。27个完整v1题摘信号中26项由官方ID公告分配规则、真实Submitted最早下界与实际arxiv.content findable registered上界组成完全落窗range，其中17准入、9具体准入前关闭；不是登记时刻等于首公开。AGF二月提交下界不同仍日期隔离，BrowseComp/card纠错与Descript仍相交day-only。日期原字段与具体改判见[日期恢复](../_sources/daily-20260307/V3_DATE_RECOVERY.md)，原文与Books范围见[证据笔记](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。重要变化是监督/梯度/推导顺序不能由表面等价推断，以及缓存生命周期会改变memory成本比较。

## 2. 来源覆盖

所有日期段指执行时当前可见目录，不冒充历史网页快照。范围限定模型形成、多模态、训练/推理、平台与模型驱动Agent；未扩Weekly或整月审读。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)与官方[RSS](https://openai.com/news/rss.xml)，实际筛06/07Mar三项并读相关官方核心；限定日/模型系统主题补检 | 已检查 | RSS可见记录而非全站保证；Descript零点/day-only首公开隔离 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)嵌入publishedOn，Feb25→Mar05经济影响→Mar06Firefox/Exploit→Mar13diff-tool；Engineering本日补检及两原文 | 受阻 | Firefox确时可采用；BrowseComp/两card纠错只有Mar06相交日，不能赋予00Z首公开 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)当前精选、[Research pubs](https://research.google/pubs/)year索引；03/06～07模型/多模态/训练/推理限定官方域补检及WAXAL核心 | 受阻 | 未恢复本窗历史论文/DeepMind日级发布段；WAXAL贡献已明确关闭，不另追日期 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)返回0行；03/06～07模型架构/训练有限官方域补检 | 受阻 | 空页及无检索命中不能证明零事件；缺历史Research段 |
| SRC-QWEN | [旧Blog](https://qwenlm.github.io/)首屏2025/09/23→07/24；重定向qwen.ai/blog0行及03/06～07有限补检 | 受阻 | 本窗2026官方目录未恢复，不扩所有PR |
| SRC-DEEPSEEK | [Research/News](https://www.deepseek.com/en/news/)Research10项，Feb25→Jun24；News首5项Dec01→Apr24，View All停止 | 受阻 | 可见Research段已查；News隐藏历史及API子入口未恢复，不以首屏证明完整 |
| SRC-MOONSHOT | [官方新Research Blog](https://www.kimi.com/en/blog/)完整可见19项至Mooncake，Feb09→Apr20相邻 | 已检查 | 当前可见Research无本窗条目，不证明被删除历史或全机构；旧platform Blog不替代新入口 |
| SRC-TENCENT-HUNYUAN | 官方JS实际publicList“全部”page1,size20,renderType0，11/11；独立按本窗读[共享原始恢复](../_sources/V3_HUNYUAN_LIST_RECOVERY.md) | 已检查 | 当前可见display Feb13→Apr23无March；publishedAt与display不互替首公开 |
| SRC-ZAI | Research首可见页Aug26→Dec09，Feb21→Mar15相邻，到查看更多停止；[原始恢复](../_sources/V3_OFFICIAL_DIRECTORY_RECOVERY.md) | 已检查 | 本窗位于可见相邻日期间；未遍历更旧页，不称全机构历史 |
| SRC-BYTEDANCE-SEED | Research/Blog当前精选，Publication Apr11→Jan27；public_papers首20/242,page1of13至May14；日/主题补检 | 受阻 | 未恢复Blog/论文历史日级段，不把242项变逐项审阅队列 |
| SRC-BAIDU-ERNIE | ERNIE Blog可见Apr15→Feb06，本窗在相邻段；共2页更旧页止2025；日/主题补检 | 已检查 | 当前可见目录限定范围，无全机构保证 |
| SRC-XIAOMI-MIMO | 官网Paper8项Mar13→Feb03→Jan08；Blog15项无日期、More停止；日/主题补检 | 受阻 | Paper段已查；Blog的历史日期和More段未恢复 |
| SRC-MINIMAX | Blog可见到2025/10/27，Mar18→Feb14→Feb12相邻及日/主题补检 | 已检查 | 当前可见日期段无本窗新记录，不扩大历年Tech Blog |
| SRC-ARXIV | [官方列表](https://arxiv.org/)有界主题查询；March月页offset2500仅首50标题、相关完整v1题摘；具名27项实际DOI接口复合日期恢复 | 已检查 | 26项完全落窗range与具体贡献裁决；AGF二月Submitted下界仍不足，单项日期隔离；只签有限主题/标题段，不宣称全学科召回 |

具体查询、原始值与停止依据集中在[当日停止点](../_sources/daily-20260307/V3_SOURCE_CHECKPOINT.md)。这张表不以搜索首页或空响应签署历史无遗漏。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Partnering with Mozilla to improve Firefox’s security](https://www.anthropic.com/news/mozilla-firefox-security) | 2026-03-06T18:30:00+08:00 | 已知CVE复现可能含训练接触 → 当前未知漏洞与漏洞移除/功能保持两verifier及primitive-exploit分账 → 不用发现数或测试通过替代攻击链/merge判断；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Codex Security: now in research preview](https://openai.com/index/codex-security-now-in-research-preview) | 2026-03-06T18:00:00+08:00 | 原threat-model→scan→sandbox→patch已存在 → 可编辑threat model及criticality反馈影响后续scan → 本版本风险语境成为持续输入；1 + 2 + 1 = 4 | 已关闭 | 仅报告：明确版本行为，未披露足以归因FP收益的新可验证机制 |
| [Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction](https://arxiv.org/abs/2603.04783v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 完整单轮能解而多轮惯性失效 → 模型特定支持集与完整条件reference anchor → 训练更新须保留outcome真值；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Diffusion Policy through Conditional Proximal Policy Optimization](https://arxiv.org/abs/2603.04790v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 隐式action密度难求 → conditional Gaussian PPO后flow蒸馏 → 保留拟合代价、全期望不授clip等价；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling](https://arxiv.org/abs/2603.04791v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | rolling forecast反复走backbone → future-offset latent按depth推进、head保留推理 → 重新比较误差与执行预算；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限TS formation实验，联合配置不能授通用生成优势 |
| [Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator](https://arxiv.org/abs/2603.04797v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 读历史KV与写last-block路径不同 → full/last动态placement → memory分配同时验token-load与mesh代价；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm](https://arxiv.org/abs/2603.04799v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 逐row调用成本 → cluster sample/vote与fallback → 确認节省所需概率和稀有项条件；2 + 2 + 3 = 7 | 争议 | 暂缓：LLM-output一致性与task-error保证及概率条件未对齐 |
| [MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models](https://arxiv.org/abs/2603.04800v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 不同modal scales不能共享一份Qweight → text-base与whitened低rank残差 → 分账校准/运行mask和输出模态；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Guiding Diffusion-based Reconstruction with Contrastive Signals for Balanced Visual Representation](https://arxiv.org/abs/2603.04803v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 原feature对比与重建冲突 → predicted-noise空间/两阶段冻结 → supervision接入位置不只是loss权重；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents](https://arxiv.org/abs/2603.04814v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 写一次事实应更省的推定 → static-history cache交点与任务差异 → 生命周期成本而非统一memory赢家；3 + 2 + 2 = 7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Scaling Laws for Reranking in Information Retrieval](https://arxiv.org/abs/2603.04816v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 连续诊断应更平滑的推定 → Contrastive Entropy与NDCG的exposure趋势不同 → ordering与score-margin分开拟合；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | forward等价误作训练等价 → basis诱导gradient几何、nested与complementary分离 → refinement不凭容量批准；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-FFN，[Ch16](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [From Unfamiliar to Familiar: Detecting Pre-training Data via Gradient Deviations in Large Language Models](https://arxiv.org/abs/2603.04828v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | likelihood受频率混杂 → 不更新target的白盒gradient sensor → membership仍需distribution校准而非污染认证；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Design Behaviour Codes (DBCs): A Taxonomy-Driven Layered Governance Benchmark for Large Language Models](https://arxiv.org/abs/2603.04837v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | weak单policy不易区分behavior风险 → layered controls与三臂反证 → judge风险定义必须与uncertainty分开；2 + 2 + 2 = 6 | 争议 | 暂缓：中心RER把uncertainty disclosure计risk，与无negative-transfer冲突 |
| [Hyperbolic Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.04848v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 跨geometry距离量值不适配 → 邻域排序监督实验 → 不把distance matching当唯一跨空间目标；2 + 1 + 2 = 5 | 标准完成 | 暂缓：仅采用表示监督实验，training gradient路径未支持必要机制 |
| [Why Is RLHF Alignment Shallow? A Gradient Analysis](https://arxiv.org/abs/2603.04851v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | sequence harm广播应全位置施压的推定 → conditional harm horizon限制梯度 → 恢复事件必须另定义；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [On Multi-Step Theorem Prediction via Non-Parametric Structural Priors](https://arxiv.org/abs/2603.04852v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | retrieval覆盖误作保持推导顺序 → matched executor下TPG额外收益 → support/precedence/verifier分权；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-PLANNING，[Ch79](../../../../books/part-07-agent/79-planning.md) |
| [FireBench: Evaluating Instruction Following in Enterprise and API-Driven LLM Applications](https://arxiv.org/abs/2603.04857v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 标准chat格式达标误作接口稳健 → 同题格式扰动与分维结果 → parser/任务/拒答分账；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Osmosis Distillation: Model Hijacking with the Fewest Samples](https://arxiv.org/abs/2603.04859v1) | 2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00 | 压缩asset保留utility误作安全 → 少样本蒸馏保留隐藏task → 表面/clean质量不代行为验收；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |

arXiv全部采用精确v1；日期列为完全落窗半开区间，不是Submitted或registered精确发布。原字段及复合推定在[日期恢复](../_sources/daily-20260307/V3_DATE_RECOVERY.md)。6分中RLSTA/DCR/rerank/KAN/TPG确认长期缺口，GDS/DBC/Osmosis具安全/评价变化，均定点深入，不用分数限制必要审阅。CSV/DBC仍属于候选，但争议命题不用于正面收益/Books；9个准入前关闭项不评分。

## 4. 证据与知识整合

### [Partnering with Mozilla to improve Firefox’s security](https://www.anthropic.com/news/mozilla-firefox-security)

采用2026-10-01实际取得的官方HTML核心（历史CVE/未知漏洞、primitive exploits、patching task verifiers）与[Mozilla官方维护者说明](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)的对应验证段，不声称获取不可变March快照。Anthropic的published_time、JSONLD datePublished和time dateTime同为2026-03-06T10:30:00.000Z，支持该研究报告事件落窗；当前modified_time为Sep09，不用它移动首次报告时间。当前页未标出影响拟采用命题的具体纠错，未遍历全版本。

先在历史Firefox CVEs上复现存在训练接触混杂；转向当时未报告的现版本漏洞只针对这一已知CVE泄漏路径，不证明所有污染排除。首例由三位研究者在独立VM核验；随后Mozilla允许批量提交crashing inputs，112 reports并不等于112安全漏洞。Mozilla确认14个high-severity、22 CVEs及90个其他bug，支持可重放testcase和maintainer独立triage，不是完整召回或生产发生率。

漏洞发现与利用评价有不同对象。作者在数百尝试、约4000美元API预算下得到两个primitive exploits，但有意移除了browser sandbox等安全特性；缺精确每项试验分母、模型预算和完整受控比较（Not Disclosed）。不能将22 CVEs读成22条可运行攻击链，不能把作者“防守优势/成本数量级”概括外推为普遍定律。本文只采用阶段区分与环境边界，不提供攻击步骤或自主攻击能力保证。

补丁回路分别检验原bug还能否触发、正常功能是否保持；通过两项是plausible patch的最低必要条件，官方仍要求维护者按外部贡献同等审阅。这里的回归检查不是语义完备性或merge权限。两来源当前修复状态保留差异：Anthropic称多数已在Firefox148修复、其余后续版本；Mozilla称全部22安全bug在最新版本已修复。不能合并成同一冻结版本状态。

Books **No Change**：Ch66“从答案评分到可执行证据”已要求artifact+environment+trace，实际执行攻击链与自然语言描述分账，绑定软件/patch/network/budget/verdict并保留sandbox差异；“Compound Artifact需要Preservation Contract”已经分开请求变化与未请求行为保持，并由专家承担开放语义residual，当前verifier不能自签任意下游有效。污染段还明确一次扫描不证明未接触。具体对应为正文1669～1698与2875～2877；[Ch65](../../../../books/part-06-ai-infrastructure/65-kai-scheduler.md)交接execution artifact/evidence，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md)仅观察状态、不定义quality。新受限验证增强现有论点，无需重复追加论文段落；root已实际核必要原文、具体No Change及日级Gate，通过。

### [Codex Security: now in research preview](https://openai.com/index/codex-security-now-in-research-preview)

实际读官方“How Codex Security works”三步及feedback段；为确认事件增量只对读旧[Aardvark](https://openai.com/index/introducing-aardvark/)“Analysis/Commit scanning/Validation/Patching”。旧正文已有repository threat model、sandbox验证和human-reviewed patch，因此改名与整套流程不是新增机制。

本次官方新核心明确threat model可编辑，用户改变finding criticality后可用于修正risk context及未来scan；仅采用这项版本行为。84%噪声降幅为单例，90%severity过报与50%FP变化是厂商beta汇总；没有受控数据、实现归因、模型/扫描预算、各项精确分母或不确定性（Not Disclosed），不归因为editable threat model，也不称复现。14 CVEs与大规模commit数不被重新打高分，未扩成逐CVE安全队列。

Books仅报告：还不足以增加一条稳定的新机制解释。可配置上下文、反馈和人工验收属于已有原则，本次证据只支持版本相关语境行为，不声明实现或部署能力已验。

### [Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction](https://arxiv.org/abs/2603.04783v1)

精确v1 §5.1/Eq2以目标模型完整单轮表现优于原多轮历史筛选支持集；§5.2/Eqs4–5对同一completion在完整合并条件下作frozen-reference likelihood anchor，仍由outcome verifier提供真值。§6/Table1及AppendixA.3/B的合成GSM8K800、3B～7B模型和matched GRPO预算支持局部惯性修正；Qwen2.5-7B refinement .822低于GRPO .836、未过滤消融下降，不能泛化所有多轮失败。

整合TRAIN-GRPO Ch33 sequence reward邻接两短段（source-family:arxiv:2603.04783v1，195–197）与章末note；旧广播/process credit与positive-only anchor继续共存。预筛和reference scoring不免费，不采用主动澄清保证。root必要原文/正文邻接POST通过。

完整必要证据、配置与未采用项见[证据笔记 §3](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Diffusion Policy through Conditional Proximal Policy Optimization](https://arxiv.org/abs/2603.04790v1)

精确v1 §3.1–3.3先用冻结reference的a0构造conditional Gaussian PPO，再flow-matching拟合marginal policy；AppendixA全期望identity不证明clipped目标等价或单调改善。§4.2 Ant相同1k epochs下PPO4.68min/4202MB，CPPO8/16steps为8.05/9.31min/4306MB；Isaac八任务五seeds不授免费LLM迁移，DPPO预训练对照不同。

整合TRAIN-PPO Ch32 ratio后两短段（arxiv:2603.04790v1，195–197）与note；保留conditional/marginal身份、额外蒸馏和拟合误差，旧显式density PPO仍合理。root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §4](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling](https://arxiv.org/abs/2603.04791v1)

精确v1 §3.2的future-offset latent沿depth推进、head保留在推理，不读取ground-truth future。§4/§5.2同时改变uniform→近horizon加权、RoPE与MoE/STP组织；24MoE+16STP和40block NTP/MTP只匹配block数量，不等参数/compute。约1.032T时间点及GIFT泄漏清理属于作者数据声明，未独立复现。

仅报告受限TS formation实验：与MODEL-DECODER-ONLY Ch18 235–251概念clock/MTP实际比较，现有段落不是TimeSTP解释，但联合配置尚不足以归因通用生成设计优势。Figure12 caption称same backbone但§5.2拓扑有异，不采用matched全预算/通用LLM速度。没有按领域标签排除，也不为制造diff纳入语言token或world transition结论；root已实际读必要机制/shift-remove反例，标准/仅报告通过。

完整必要证据、配置与未采用项见[证据笔记 §5](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator](https://arxiv.org/abs/2603.04797v1)

精确v1 §IV–V/Alg2在CPU request/block identity和固定backing地址下，full历史KV按token-load后优先远mesh中心；last可写block优先接近归约终点并计path-volume。KV传输完成才decode admission。§VI八设备TP8/EP8、FP16、变长Poisson负载；A100/SGLang/FlashInfer是测量，Helios/Ramulator2/BookSim/HotSpot是模拟，均匀MoE routing未含不均衡。

整合INFER-GPU-MEMORY Ch54 near-memory段两短段（arxiv:2603.04797v1，484–486）与note，保留GPU prefill瓶颈、小block碎片/mesh成本及成熟HBM路径。作者倍数不授已交付硬件或生产SLO；root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §6](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm](https://arxiv.org/abs/2603.04799v1)

精确v1 §3 cluster/sample/vote、recluster与linear fallback有成本选择增量。§3.3/Theorem3.3却以LLM输出M(t,e)的均值代表individual error，Corollary3.4及proof归一/概率对象不一致；输出一致性不证明任务gold正确。§4.1–4.4十二query中rare-positive CB-Q1在lb .15退步，lb .01后约半数linear，去recluster还同时改threshold，不能作纯因果归因。

暂缓中心sublinear task-error保证，不作正面性能或Books证据；保留候选7分与已读反证，不称访问故障。root实际核理论冲突及安全隔离通过；只在推导勘误/明确概率条件和oracle校准到达后重开。

完整必要证据、配置与未采用项见[证据笔记 §7](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models](https://arxiv.org/abs/2603.04800v1)

精确v1 §4针对不同SmW无法共享一份量化weight，选text-base Q(StW)，在activation-whitened度量上对其他modality residual作低rank output correction；给定校准X/r的近似不证明差异天然low-rank。§5.1–5.5仅Thinker Qwen2.5-VL/Omni、W4A8/W8A8及对应WER/视觉任务，Talker/codecs不在同一低比特证明中。

已有覆盖INFER-TENSORRT-LLM Ch49“Distribution-conditioned Quantization”实际1214–1270已经解释共享weight与modal scale、whitened conditional residual、text-base/token-mask、rank/calibration/runtime及fallback，不复制第二份机制。kernel速度不代E2E goodput或交错/audio-output免费；root必要原文与Ch49实际No Change通过。

完整必要证据、配置与未采用项见[证据笔记 §8](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Guiding Diffusion-based Reconstruction with Contrastive Signals for Balanced Visual Representation](https://arxiv.org/abs/2603.04803v1)

精确v1 §4.1原CLIP feature的contrastive/reconstruction负cos冲突；§4.2先冻结encoder/denoiser训projector，再冻结projector，通过predicted-noise空间对比训练encoder并保留GT noise目标。§4.3依赖mapping regularity、negative separation和norm假设。§5.1 CC3M/A10080/SD2.1、LoRA16/batch16/4600steps与GenHancer denoiser预算不同；§5.4/Table4的两阶段对照及SDXL条件错配退步限制普遍性。

整合MULTIMODAL-REPRESENTATION Ch23 weighted-loss段邻接两短段（arxiv:2603.04803v1，492–494）与note，补监督接入空间/训练顺序而不替换普通加权和独立重建。生成训练成本与noise非truth保留；root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §9](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents](https://arxiv.org/abs/2603.04814v1)

精确v1 §3 Mem0分段/抽取/reader与long-context raw timestamp reader不同，同类GPT5mini三票judge不是独立人类校准。§4.2–4.4静态write-once/many-read与LC后续90%cached-input折扣造成交点；500Q有504或664实际calls含retry，500k context成本外推不是该长度实测。线上history更新、cache失效、storage和并发tail未评估。

整合AGENT-MEMORY Ch77 late-construction后两短段（arxiv:2603.04814v1，340–342）与note，旧memory压缩/构造链保留，新增static history生命周期与重试分账；不授通用N10交点/现价或统一memory赢家。root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §10](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Scaling Laws for Reranking in Information Retrieval](https://arxiv.org/abs/2603.04816v1)

精确v1 §4.2的CE是Contrastive Entropy：BM25 top100/64 negatives、normalized score上的positive softmax负log诊断，不是training cross-entropy，作者NDCG本来primary。§5/§6.2 Ettin17M～1B、MSMARCO100k queries一epoch中pairwise CE与NDCG的exposure趋势不同，支持score-margin与ordering估计对象分离，不证明margin变化因果。held-out checkpoint/exposure不等new unique data；§7仅TREC六集，§8MRR与摘要冲突不采用。

整合AGENT-RAG Ch76 reranking段邻接两短段（arxiv:2603.04816v1，397–399）与note；原representation/ordering分工保留，新增诊断估计对象/数据exposure的受限比较，不写universal scaling law或loss代泛化质量。root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §11](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827v1)

精确v1 §3/Eqs16–17 fixed-knot spline与power-ReLU可forward-equivalent，但basis变换引入gradient metric；§4/Def1/Eq22 transfer保持coarse函数不保证优化路径，§4.3还需complementary fine modes。§5.1同FLOPs/L-BFGS/五初始化的函数回归中ReLU .0110→.0106、spline .00165→.0000367且std .0000719，不授任意optimizer深网加速；不采用PINN领域应用或旁支Eq19。

整合MODEL-FFN Ch16 gate-conditioning后两短段（arxiv:2603.04827v1，202–204）与note：补forward等价与参数化训练几何、transfer与relaxation区别，保留原MLP/条件机制。root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §12](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [From Unfamiliar to Familiar: Detecting Pre-training Data via Gradient Deviations in Large Language Models](https://arxiv.org/abs/2603.04828v1)

精确v1 §4 LoRA B=0时取B逐sample gradient特征、不更新target；MLP仍需要membership labels，fine-tuning-free不等无监督。§5.4.3 Wiki年份token删除.96→.84、§5.4.4跨dataset .66/.68，不能排所有频率/chronology混杂或授closed-model认证。五公开dataset/五2.7B～7B models下AUROC/TPR@5%FPR为作者结果。

已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66 detector revision/distribution、model/reference/threshold/FP-FN、Unknown≠Negative及接触不授分数增益的实际论点（4187–4199、2891–2893）承载窄采用边界。white-box membership sensor不改写benchmark真值；root实际原文与owner No Change通过。

完整必要证据、配置与未采用项见[证据笔记 §13](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Design Behaviour Codes (DBCs): A Taxonomy-Driven Layered Governance Benchmark for Large Language Models](https://arxiv.org/abs/2603.04837v1)

精确v1官方14page PDF已恢复，§4.3/4.4三臂控制与judge评估存在配置/rubric欠缺，κ>.7只证明agreement。§5.5无negative-transfer却§6.2将uncertainty disclosure计risk而RER负面，中心估计对象不一致；150controls或36.8%不自动为安全机制贡献。

暂缓中心风险主张，已有PDF不称transport阻塞；不得采用风险百分比/法规认证或进入Books。root实际核必要原文与隔离通过，重开需deidentified三臂逐项结果、judge/rubric/human anchor或erratum。

完整必要证据、配置与未采用项见[证据笔记 §14](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Hyperbolic Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.04848v1)

精确v1 §3.3不是仅hyperbolic模块：Euclidean图像与Lorentz表示的距离量值不可直接对应，改作top-K邻域排序监督。§4.5同设置Euclidean MAE*68.22、本文71.11、去rank67.72；去inter-view loss71.00，不能夸大次要差异。3DMOV200k/五视角、100epochs/八4090、RVT四evaluation runs不是四训练seeds。

标准审阅采用受限表示监督实验；两次argsort梯度路径未说明，不授可导实现/因果保证。MULTIMODAL-REPRESENTATION Ch23已有geometry/语义身份但不承载该新训练条件，故暂缓必要机制而非因5分机械仅报告；伪代码/gradient说明为重开条件。CVPR撤稿不误作arXiv撤回。root已实际核必要原文和标准/暂缓边界，通过。

完整必要证据、配置与未采用项见[证据笔记 §15](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Why Is RLHF Alignment Shallow? A Gradient Analysis](https://arxiv.org/abs/2603.04851v1)

精确v1 §3–10 fixed-prompt/known terminal harm下Doob innovation与conditional covariance导出harm horizon；零position期望贡献不消sharedθ跨位置耦合，AppA.2–4 late KL可非零。recovery event需指定token集合/adversarial-prefix Q/positive p_min；Fisher与small-λ局部条件不授任意training path。§11不跨representation depth、spurious RM、prompt聚合、single-turn/finite capacity边界。

已有覆盖TRAIN-RLHF Ch31实际408–430已逐条件解释martingale/horizon/recovery与共享耦合、sequence fallback及部署不安全保证。不是凭理论主题或旧评分No Change；root实际原文/owner核通过。

完整必要证据、配置与未采用项见[证据笔记 §16](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [On Multi-Step Theorem Prediction via Non-Parametric Structural Priors](https://arxiv.org/abs/2603.04852v1)

精确v1 §3历史trace TPG频率是proposal prior，当前symbolic state和executor决定合法性。PDF§4.1/§4.3/Table3均用GT formal1400 inputs/600s、同GPT5mini iterative executor：RAG72.64/Hard22.95，RAG+TPG84.42/Hard40.98，足以反驳检索覆盖已保持顺序。Table6 K15/30/100/200揭示support不足；局部precedence≠global depth，多次calls成本主导，没有上游视觉/解析保证。

整合AGENT-PLANNING Ch79 pruning后两短段（arxiv:2603.04852v1，177–179）与note，保留旧retrieval与executor路径，新增support/precedence/verifier分权及具体matched反证。root实际POST通过。

完整必要证据、配置与未采用项见[证据笔记 §17](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [FireBench: Evaluating Instruction Following in Enterprise and API-Driven LLM Applications](https://arxiv.org/abs/2603.04857v1)

精确v1 §3/§4同题boxed{}与boxed[]等format扰动暴露chat表现不等API contract；四集25题×21formats应2100而正文1000，聚合分母不采用。MHPP100×3=300、ordered/ranking各200分开；confidence两独立calls不授逐item联合校准。局部format下降不证明training memorization因果，模型reasoning/temperature预算不完全匹配。

已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66实际375–381已要求task语义等价variants审计、raw/parse/abstain分账及预算/cost，采用反证不再复制第二份正文。不删候选、不把程序化parser当所有语义真值。root必要原文与Ch66实际No Change通过。

完整必要证据、配置与未采用项见[证据笔记 §18](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

### [Osmosis Distillation: Model Hijacking with the Fewest Samples](https://arxiv.org/abs/2603.04859v1)

精确v1 §III–V provider只控制外来压缩training asset，camouflage/trajectory distillation保留原与隐藏task；victim weights/optimizer不受攻击者控制。六图像数据、ResNet18/VGG16、IPC50、singleA100与对照原data50%不是matched sample/compute，t-SNE不授不可检测，无blind human study。Foundation关系只限消费蒸馏训练asset，不声称LLM后门已验证。

已有覆盖TRAIN-DATA Ch27实际166已写蒸馏表面良性≠行为安全、teacher/sample/student身份和behavioral canary；Ch72实际61–65提供clean utility≠安全及强度分账的交接，唯一owner仍Ch27。不复写攻击recipe或生产安全保证。root必要原文与Ch27/72实际No Change通过。

完整必要证据、配置与未采用项见[证据笔记 §19](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。

## 5. 缺口与下一步

普通待办0。27项日期接口已实际恢复，26完全落窗信号已逐项完成贡献裁决，19冻结候选均达到所需审阅及Books处置；八处实际整合的POST和root非作者日级Gate均已通过。以下只是本窗终态保留项，不是已证明的正面Coverage/Evidence。

本窗终态保留项不用于正面证据、Books、性能/安全保证或覆盖断言。继续有限恢复已无可取得的必要材料，重开条件如下：

- **CSV 2603.04799v1**：[v1中心理论](https://arxiv.org/html/2603.04799v1)用LLM输出的总体均值代表individual error，Theorem3.3/Corollary3.4及proof的概率对象与归一不一致，不能采用sublinear task-error保证。必要理论及关键评价已实际读，不是访问故障；可接受推导勘误、明确总体/逐item概率条件及受控oracle/gold校准，仅重开误差保证，不采用宣传倍数或写Books。
- **DBC 2603.04837v1**：[官方PDF](https://arxiv.org/pdf/2603.04837v1)已取得，§4.4 judge身份变量/rubric不充分，§5.5无negative-transfer与§6.2把uncertainty disclosure计risk冲突。中心风险结论暂缓，不授风险降幅/法规认证；可接受deidentified逐项三臂结果、judge配置/rubric及独立人类锚定或erratum，只恢复风险估计对象与该结论。
- **HyperMVP 2603.04848v1**：[v1§3.3/§4.5](https://arxiv.org/html/2603.04848v1)可支持距离量值与邻域排序不同的受限表示监督实验，但两次离散argsort的梯度路径未说明，不能采用可导实现或因果保证，也不能因5分机械仅报告。暂缓该Books机制；需要作者伪代码/实现或可验证gradient说明。会议撤稿不误作arXiv撤回。
- **BrowseComp及Opus/Sonnet4.6 March6 card纠错同家族**：[官方blog](https://www.anthropic.com/engineering/eval-awareness-browsecomp)正文Mar06与00Z疑日归一；dated changelog仅March6。潜在反证是encrypted answer获取/文本mirror绕过binary限制及过程合法性与正确答案分离，绝非“只改card数字”负侧。工程页无可见feed，精确slug/官方X有限日期补检未取到更细时间。需要官方首发RSS/带时区时刻或完全落窗区间；有日期后只审安全评价定义、纠错估计对象与限制，不扩模型全篇。Opus multi重跑11项8项合法成功，single3项直接记错；Sonnet对应11项5项、single9项直接记错。两种调整协议不能合并成同一估计对象；当前尚不采用这些结果。
- **Descript**：[官方核心](https://openai.com/index/descript)明确字幕与dubbing的意义/时长双约束差异；不能按客户案例标签关闭。RSS原值Fri06Mar00GMT（08BJT）在左端前，但整齐零点可能日归一，正式页只有Mar06。缺实际首公开时刻/完全落窗范围；暂不作精确窗外事件或当窗候选。
- **AGF 2603.04805v1**：二月Submitted不能套用其余26项的三月最早公告下界，注册上界仍不能单独证实完全落窗。缺具体首公开公告或能够限定落窗的官方公开记录；仅隔离此项。其余26项的实际复合range及普通贡献/证据工作见[日期恢复](../_sources/daily-20260307/V3_DATE_RECOVERY.md)与[具名表](../_sources/daily-20260307/V3_SOURCE_CHECKPOINT.md#具名潜在贡献--日期恢复后待裁决)，不再使用旧“27项全部日期隔离”理由。
- **历史子目录**：Google Research/DeepMind、Meta Research、Qwen新Blog、DeepSeek隐藏News/API、Seed历史Blog/论文段、MiMo Blog的必要本窗段如第2节。可接受能限定本窗的官方历史目录/API原始数据或原文首发列表；到达后只恢复该源该段，不把网页总条数变全文队列。现有有限查询不能证明零事件。

明确关闭的WAXAL、Balyasny、SparkTales、EchoGuard、WhisperAlign、SCoUT及标题明确范围外样本保留[实际理由](../_sources/daily-20260307/V3_SOURCE_CHECKPOINT.md#明确关闭样本)，不为不影响处置的日期另建请求。发现具体纠错或主线反例才重开受影响材料。

## 6. 复核

复核者：root（独立于本报告作者mar03_v3）。
结论：通过

root实际检查14来源的有限入口/停止点、官方ID/最早公告/注册上界的复合日期、全部19候选的准入与必要证据/Books处置，以及八处实际正文和前后衔接POST。6处No Change、Timer/Codex仅报告、CSV/DBC中心争议及HyperMVP必要实现暂缓均通过。BrowseComp重要纠错、Descript及AGF保持日期隔离；历史子目录限制不算正面Coverage或无遗漏。

负侧分层实际复核：26落窗信号中9个准入前关闭项抽检polarization 04817、SADCA 04839、MCal 04831完整题摘及决定准入的定点说明；VISA等其余6项复用已有具体准入校准，不称本轮无差别重读所有附件。有安全/设计反证信号的GDS/shallow/DBC/Osmosis及Fire/Hyper未因标签或已有覆盖而误排。额外WAXAL、Balyasny、SparkTales、EchoGuard、WhisperAlign、SCoUT按已记录的具名核心/题摘范围及准入校准复用；标题明确范围外只作有限标题检查。MCal末轮撤回“已有affine所以不新”理由，改为解释对象f→tilde f、clean-f proxy、不匹配mask rate与没有原f依赖的独立反证；未审全部50标题的全文或整月库存。

具体原字段、原文位置和权限见[证据笔记](../_sources/daily-20260307/V3_EVIDENCE_NOTES.md)。本次V3 validate_research校验通过；报告与三份V3源文件本地链接0 broken，限定八Books/日报范围git diff --check通过。机器结果仅验格式/一致性，不代日级语义验收。保留原始材料及未知来源的未跟踪“ 2”副本，未stage、commit或push。
