# 2026-04-07 V3 重审工作记录（进行中）

目标窗口：`[2026-04-06T09:00:00+08:00, 2026-04-07T09:00:00+08:00)`。本文件是过程证据，不是报告完成声明；`README.md` 的 V2.1 `Complete/Passed` 不可继承。

## 日期归属：先纠正旧库存的两种时间

[arXiv 公告说明](https://info.arxiv.org/help/availability.html)明确：永久 ID 在公告时分配，通常美国东部时间周日到周四 20:00 公告，投稿可以因审核延期。2026-04-06 美东 20:00 对应北京时间 2026-04-07 08:00，落在本窗；`Submitted`、DataCite `created` 和后续 `Updated` 任一字段都不能单独当作首次公开时刻。

对 [2604.03231](https://api.datacite.org/dois/10.48550/arxiv.2604.03231)→[2604.03232](https://api.datacite.org/dois/10.48550/arxiv.2604.03232) 的相邻 ID：前者 DOI created=`2026-04-06T01:45:01Z`，v1 Updated=`2026-04-06T00:51:19Z`；后者 created=`2026-04-07T02:36:29Z`，v1 Updated=`2026-04-07T00:00:04Z`。对 [2604.04934](https://api.datacite.org/dois/10.48550/arxiv.2604.04934)→[2604.04935](https://api.datacite.org/dois/10.48550/arxiv.2604.04935)：前者 created=`2026-04-07T03:17:11Z`，v1 Updated=`2026-04-07T01:43:24Z`；后者 created=`2026-04-08T01:55:20Z`，v1 Updated=`2026-04-08T00:00:04Z`。首、中、末段另抽 `03258`、`04334`、`04895`、`04929`，created 与 v1 Updated 同向。因而连续 ID `2604.03232`～`2604.04934` 与本窗 08:00 公告批次相容，`04935+` 属下一批；这是有边界的批次推断，**不是逐篇秒级公告证明**。具体例外、撤回和修订须独立标注。

旧 `inventory.json` 以 v1 submitted 时间圈入 `04334`～`05292`，故既漏了本窗较早 ID，又混入下一批。旧 `README.md` 以 DOI created 归属的 90 个候选也未按 V3 贡献口径复核。旧 `screening-ledger-final.json` 自称 66 个候选，但反复使用“改变 state/control ownership 或 evaluation contract”的通用句且存在错误章节映射；不可按 `fresh-context` 字段复用。旧库存仅是发现线索。正式报告在 14 来源和分母校准前保持进行中。

## 题摘准入首批校准

以下是独立阅读旧库存中的完整题摘后的暂判，不是全文或 Books 决定：

| 家族 | 初判 | 具体理由 |
| --- | --- | --- |
| [GENSERVE 2604.04335v1](https://arxiv.org/abs/2604.04335v1) | 拟入选 | 图像/视频扩散共置的逐步可抢占点、动态并行与 SLO 调度，可能改变生成式 serving 的调度状态与 admission 设计；需核 Method、实验配置和是否已被 Ch56 覆盖。 |
| [ShieldNet 2604.04426v1](https://arxiv.org/abs/2604.04426v1) | 拟入选 | 将 Agent 工具供应链防护的证据面从工具文本/trace 推到真实网络行为，可能改变安全监测部署点；需核 MITM 威胁模型和误报、绕过边界。 |
| [GPU execution-idle 2604.04745v1](https://arxiv.org/abs/2604.04745v1) | 拟入选 | 可见 GPU 利用率低但功耗高的执行中状态，可能修正能耗核算与降频/负载平衡 trade-off；需核遥测定义和受测集群代表性。 |
| [DeltaTok 2604.04913v1](https://arxiv.org/abs/2604.04913v1) | 拟入选 | 帧间视觉特征差分压成单 token，使多未来生成的计算合约改变；需核预测目标、token 化损失与评估任务。 |
| [RoboPhD 2604.04347v1](https://arxiv.org/abs/2604.04347v1) | 暂缓准入判断 | 同预算不同 agent 优化范式比较可能修正 evaluation-budget 选择，但题摘的“首个比较”及 3/4 优势未说明随机性/调参公平性；先定点核方法与实验是否有可迁移边界。 |
| [SuperLocalMemory 2604.04514v1](https://arxiv.org/abs/2604.04514v1) | 拟排除 | 七通道、遗忘曲线等是具体产品组合与 benchmark 主张；题摘自身还给出前版 74.8% 到本版 70.4% 的质量代价，但暂未显示改变 Books 已有的记忆 provenance/派生状态论点。若有可定位反证再重开。 |
| [LEO collaborative inference 2604.04654v1](https://arxiv.org/abs/2604.04654v1) | 拟排除 | 卫星网络的特定内存/链路约束下组合模型拆分、流水线与压缩；初筛未看到超出既有分布式推理状态/通信权衡的新可迁移机制。 |
| [OpenWorldLib 2604.04707v1](https://arxiv.org/abs/2604.04707v1) | 拟排除 | 主要是定义、任务分类与统一代码库，没有在题摘中给出可核的新 world-state transition 机制或实验证据。 |
| [Hardware governance 2604.04712v1](https://arxiv.org/abs/2604.04712v1) | 拟排除 | 是监管可行性分类和政策场景，未改变当前大模型系统的实现/评价/发布控制契约；旧表错误映射到 speculative decoding。 |

上述保留/排除仍需非作者准入校准，尤其检查“仅仅有项目相关术语被误收”和“局部但有真实反证被误排”；不以固定保留率裁决。下一步先完成 14 个每日来源的本窗有界扫描，并针对官方 03232～04934 批次按主线主题补检。

## 每日机构来源：已取得的有界停点

本段是截至本次重审的入口证据，不将页面更新或 CMS `createAt` 充当首发日，也不把列表无命中推断为作者未在其他渠道发稿。

| 来源 | 实际检查和窗口结论 | 边界 |
| --- | --- | --- |
| Anthropic | [Research](https://www.anthropic.com/research) HTML 的 `publishedOn` 历史条目中，邻近项是 `2026-04-02T10:56Z`、`2026-04-07T09:35Z`、`2026-04-09T16:34Z`；04/07 09:35Z = 北京时间 17:35，已过本窗截点。 | 以页面嵌入的公开时间字段为准；不能把 04/07 日期直接纳入本窗。 |
| Qwen | 官方动态 [retrieval API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 40 项与 [旧静态 Research 列表](https://qwen.ai/api/page_config?code=research.research-list) 60 项交叉；动态项 04/02 04:00+08 后跳至 04/15 10:00+08。 | 列表层无本窗新文章，仍不证明作者稿无 arXiv 条目。 |
| 腾讯混元 | [官网 Research 公开列表 API](https://api.hunyuan.tencent.com/api/blog/publicList) `POST {"pageNum":1,"pageSize":100,"renderType":0}` 返回 9/9；相邻 04/23 与 02/13 之间无条目。 | 仅该公开列表。 |
| 字节 Seed | [论文目录公开 API](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=40) 带 `x-tt-locale: US`，页 40 的相邻时间为 04/07 16:00Z 与 03/31 12:00Z；04/07 16:00Z 是北京时间 04/08 00:00，已过本窗。页 0、20、40、60 查到越过窗口边界。 | 官方目录时间可能是站点入库/显示时间；外链 arXiv 首发仍须归其本身批次。 |
| Google Research Blog | [2026 年 4 月归档](https://research.google/blog/2026/04/) 完整可见条目按 04/29、22、21、16、13、09、08、03 排序；04/03→04/08 之间无 Blog 条目。 | 不涵盖 DeepMind/Google Publications 的全部投稿；后者另查或列限制。 |
| DeepSeek | [研究与动态索引](https://www.deepseek.com/news/) 的研究条目邻近为 2026/06/24 DeepSeek-V4 与 2026/02/25 DualPath，动态条目邻近为 04/24 V4 preview 与 2025/12/01 V3.2。 | 目前页面显示“查看全部”，尚未得到全部历史列表停点，暂不写全站零命中。 |
| Meta | [AI at Meta Blog](https://ai.meta.com/blog) 可见 04/06 的 Alta Daily/SAM 应用案例、04/08 的 Muse Spark/评估文章；前者是领域应用且缺精确发布时间，题目/正文足以作范围排除。 | [Research](https://ai.meta.com/research/) 页面没有可读历史条目，需隔离该子入口，不宣称全部 Meta 研究零遗漏。 |
| OpenAI | [04/06 Safety Fellowship 公告](https://openai.com/index/introducing-openai-safety-fellowship/) 是人才项目，不是模型/系统研究；Research/Publications sitemap 可读但 `lastmod` 不是首发字段。 | 尚未取得该窗历史 Research/Publications 的可靠分页停点，需精确隔离。 |
| 百度 ERNIE | [官方 Blog](https://ernie.baidu.com/blog/zh/) 可见相邻 04/15 ERNIE-Image 与 02/06 ERNIE 5.0；04/07 无显示文章。 | 仓库重要 release 尚待定点核。 |
| 智谱 Z.ai | [官方 Research 文章 157](https://www.zhipuai.cn/zh/research/157) 显示 2026/04/07 16:00 的 GLM-5.1 版本公告，已晚于当天 09:00；原文是型号能力与作者 benchmark 陈述，不披露足够 Method/受控证据。 | 页面未明示时区；即使按北京本地时间也在截点外，CMS `createAt` 不当首发。若时区不同且能落窗需重开日期。 |
| Moonshot/Kimi | [Platform Blog](https://platform.kimi.com/blog) 的可见历史列表最新为 2025/11/07，未覆盖 2026/04。 | 不能据此声称 04/07 零研究；官方 GitHub release 仍需定点。 |

尚待完整处理：小米 MiMo、MiniMax 四入口与上述仓库的窗口内重要 release，以及 Google DeepMind Publications 精确停点。OpenAI/Meta/Kimi 的外部目录限制可按合同隔离，但不能写成已检查无命中。

补检后更新（2026-09-26）：[MiMo 官网 Paper 列表](https://mimo.xiaomi.com/) 可见从 2026-06-29 跳到 2026-03-13，无 04/07 本窗论文；同页 Blog 不显示日期，不据其判零。[MiniMax 英文 Research 列表](https://www.minimax.io/blog) 可见从 2026-05-26 跳到 2026-03-18，无本窗公开条目；[中文页](https://www.minimax.cn/blog) 当前抓取只显示频道说明，[Agent Tech Blog 索引](https://agent.minimax.io/docs/llms.txt) 当前仅列一篇 Agent Team 文章，未给历史发表时间，二者按子入口限制隔离。[GitHub 官方 releases API](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100) 定点检查 XiaomiMiMo/MiMo、MiMo-VL、MiMo-V2-Flash、MiniMax-AI/MiniMax-M2、M2.5、One-RL-to-See-Them-All、MoonshotAI/Kimi-K2、MoBA、PaddlePaddle/ERNIE、zai-org/GLM-5：前八及 GLM-5 当下无 GitHub Release 条目，ERNIE 唯一可见 release 为 2025-06-30。此检查仅覆盖这些仓库的 release API，不包含 ordinary commits 或未列仓库，不推断其全部研究零命中。

## 已完成的单篇 exact-v1 小批次：GenServe

- 身份与归属：[GenServe `2604.04335v1`](https://arxiv.org/html/2604.04335v1)，属于上文 `03232`～`04934` 的有界公告批次推断；HTML 页眉的 `06 Apr 2026` 不能直接换成北京日报日期。未见此 v1 撤回标记。与其他网站/列表转载按同一 Source Family 去重。
- 初筛贡献：Ch56 已讨论 LLM 抢占、视频播放 slack 和 DiT 的 step work，但未把共置 T2I/T2V 的两套 deadline、可恢复 VideoState、图像组批与视频 sequence parallelism 当作同一个调度决策；这是一条有条件的系统设计分支，不是“扩散推理更快”的单点数字。
- Method §3–4：T2I 短请求在 FCFS 下被长视频阻塞；纯短作业优先又可能使视频过期。调度器在 denoising step 边界对视频暂停/恢复，保留 latent、mask、prompt embedding 与 step index；图像用截止时间组批，视频可调 SP degree，有限 GPU 上以可达 deadline 数及 slack 比较候选动作。前提是两套模型权重能在所测 GPU 上共驻、step 状态确实可恢复；不能照搬自回归 KV 调度。
- 实现与评价 §5–6：作者用 Diffusers、Wan、xFuser 实现；单机 8×RTX PRO 6000 Blackwell 96GB，SD3.5 Medium 2.5B 与 Wan2.2 T2V5B，合成 100-request Poisson/bursty traces，图像/视频比 20:80、50:50、80:20，视频 81 帧；截止时间按离线运行时长乘 `1.5×σ` 构造（`σ=0.8–1.3`）。精度、真实用户流量、跨节点拓扑与生产 tail-SLO 不由这些实验证明。
- 关键消融与反证 §6.2–6.3：skewed resolution、balanced mix、24 req/min、`σ=1` 下，FCFS 的 overall/image/video SAR 为 `20/20/20%`；仅加入视频抢占为 `39/68/10%`；加 DP solver 为 `58/94/22%`；再加 SP switching 为 `63/94/32%`。视频尾延迟在 default configuration 的 p99 为 GenServe `229s`、FCFS `166s`，说明优化总体命中率可能牺牲已超时的长视频，不可宣称两类请求无条件同时改善。
- 机制边界：预创建 communicator、GPU 上保留 VideoState 与同卡共载是作者实现条件；低负载下 solver 增益较小，静态 GPU 池或简单 reservation 在稳定负载或不可靠恢复时仍成立。作者 benchmark 未证明生产多租户、安全隔离、资源漂移或图像质量无损。
- Books 对读：唯一 owner 为 `INFER-SCHEDULING` Ch56。主任务已在该章 progress-state 论证后写入窄幅段落；本日作者独立对读 HTML v1 §4/§6.1–6.3 与 Ch56 新段，确认机制、条件和负面证据均准确。日报最终候选及整合状态仍待分母/来源 Gate 冻结后同步；此单篇不能把全日标完成。

## 全批标题复核与旧 Books 标记一致性（进行中）

本次已按 `2604.03232`～`2604.04934` 的 854 个原始身份连续查看全部标题；旧 90 个 retained 的完整题摘另行重读。标题复核是查漏入口，不能代替含糊条目的完整摘要，也不能自动把命中词的材料纳入分母。旧 764 个排除项中，`03444`、`03537`、`03616`、`03962` 的完整题摘已明确给出需要重审的模型、结构化输出或流式安全机制；还需定点核 `03253`、`03257`、`03263`、`03266`、`03340`、`03632`、`03855`、`03890`、`04199`、`04207`、`04281`、`04461`、`04580`、`04648`、`04767` 等。它们是待裁决身份，不是已入选或已完成全文审阅。旧候选中的网络控制面、区块链、通用 SNN 与行业应用等则需逐项审查能否满足当前项目贡献门槛，不能因原报告曾写 Books 就沿用。

Books 中对旧 90 家族的下列三个标记已精确定位，待独立准入判断后由共享文件 owner 定点修复，**本日不自行删改**：

| 家族 | Books 现状 | V3 待判的真实增量与风险 |
| --- | --- | --- |
| `2604.03539` CB-VER | Ch73 `books/part-06-ai-infrastructure/73-production-best-practice.md:75–84` 是机制正文，`:288` 是 Review note。 | 原文研究通用网络控制面的 eventual-stability proof；若仅因能类比 AI 平台控制面而保留，则触犯“类比不足以准入”。Books 正文承认不证明 AI 平台端到端正确，但是否需要将该段降为原理类比或移除，由共享 owner 裁决。 |
| `2604.03997` Ledger-State Stigmergy | Ch82 `books/part-07-agent/82-multi-agent.md:289–295` 是正文，`:953` 是 Review note。 | 原文讨论链上自治软件 agent 的 ledger-state coordination，不直接测 LLM Agent；durable state / commit 的原则可能可迁移，但必须证明超出本章已有 workflow owner 论点的独立增量，不能只凭类比准入。 |
| `2604.04712` Hardware-Level Governance | Ch72 `books/part-06-ai-infrastructure/72-security.md:91–105` 是正文，`:2699` 是 Review note。 | 原文是不同 adversary tier 下硬件治理可行性 taxonomy；Ch72 的 threat-tier attestation contract 确与安全边界相关，但论文未提供设备实现或部署实验。是否留为受限治理/威胁模型证据而非“机制实现”，待 Source Review。 |

### 旧 90 项题摘重筛：前 30 项

这里“继续审阅”只表示题摘已给出可定位的设计/评价增量，尚不表示全文、评分或 Books 已通过；“前分母关闭”表示完整题摘不支持本项目需要的长期增量。后续证据可以修正这些初判。

| ID | V3 初判 | 题摘层具体理由 |
| --- | --- | --- |
| 2604.03258 | 前分母关闭 | 软激活稀疏加低秩是特定压缩组合；题摘未分离出超出现有低秩/剪枝权衡的新系统边界。 |
| 2604.03270 | 继续审阅 | 预计算 KV 注入有因果 mask 下的精确条件与模板失配反证，会改变知识交付的 token/state 合约。 |
| 2604.03295 | 前分母关闭 | 多 Agent 数量与长期记忆的规模比较虽相关，但摘要主要提出概念视角与系统组合，未给新责任边界或可验证机制。 |
| 2604.03362 | 继续审阅 | 从真实失败报告构造 repo-grounded 行为 fuzzing，将 coding-agent 评价从固定任务成功扩至故障模式再现。 |
| 2604.03414 | 前分母关闭 | 视频 token 压缩的 kernel redundancy/时间间隔选择属于局部压缩优化；未改表示身份或跨模态状态的既有判断。 |
| 2604.03420 | 前分母关闭 | ViT 图像分类的 donor→receiver 权重算术对 3-bit PTQ 有实验，但当前证据未触及本项目大模型量化方案的适用边界。 |
| 2604.03425 | 继续审阅 | FHE Transformer 长序列跨 GPU 的 RNS 依赖与通信/复制 trade-off，可能改变隐私推理的并行设计。 |
| 2604.03430 | 前分母关闭 | “Cognitive Fabric”将多 Agent 中间层功能打包，摘要未给独立可检验的新控制状态或失败边界。 |
| 2604.03465 | 继续审阅 | Web Agent 工具收益的规模/可比性与副作用受控比较，可能修正“高级工具必然改善”判断。 |
| 2604.03527 | 前分母关闭 | 为模型路由附审计解释是已知治理原则的实现；题摘未提供改变路由选择或错误成本模型的新证据。 |
| 2604.03539 | 待定点裁决 | 原文是网络 control-plane eventual property 的模块化 proof，非 LLM/AI 平台实测；需对读 Ch73 旧正文是否只是类比，不能仅因已写 Books 而保留。 |
| 2604.03588 | 待定点裁决 | 目标条件下对同一经历编码冲突观点，可能挑战 Agent memory 单一事实视图；需核是否只是多视图检索已有机制。 |
| 2604.03591 | 前分母关闭 | HPC GPU 负载功耗分类是宽泛集群画像，本窗 04745 更具体检验执行中闲置能耗；此项摘要未显示额外可迁移控制边界。 |
| 2604.03592 | 继续审阅 | 多语言 MoE 专家隔离与层间聚散给路由/子网适配具体机制证据，不只是多语榜单。 |
| 2604.03598 | 前分母关闭 | 250 prompt 的注入类别效果比较可作安全背景，但未见新的跨边界控制或具有强外推性的防御判断。 |
| 2604.03626 | 前分母关闭 | FPGA 上 SNN 硬件与本书大模型计算主线不同；仅有节能类比不构成准入。 |
| 2604.03656 | 前分母关闭 | GEO 营销平台的“确定性”多 Agent 路由推断未给独立受控证据，也不属于当前系统设计主线。 |
| 2604.03675 | 继续审阅 | Agentic search 的 outcome-only 稀疏奖励与中间 proxy 偏差之间提出 outcome-aligned 过程信用分配，可能改变搜索 Agent 训练判断。 |
| 2604.03676 | 继续审阅 | 14 retriever 的冷启动、延迟分布、扰动和成功置信度同测，可能修正 LLM 检索器质量优先的成本判断。 |
| 2604.03679 | 继续审阅 | 静态思维压缩造成不可逆细节损失，显式自适应记忆管理可能改变推理期间 state retention 选择。 |
| 2604.03714 | 前分母关闭 | 一般自治系统 SLEEC/ASM 执行框架尚未建立 LLM/Agent 特有的授权或状态失效路径。 |
| 2604.03809 | 待定点裁决 | 三个同模型 Agent 推理轨迹相似可能挑战投票独立性，但目前仅 100 道 GSM8K；需查对照与方差是否足以修正评估合同。 |
| 2604.03820 | 前分母关闭 | 质性研究 Chrome 插件的逐段留痕是特定领域应用，未改变 AI System evidence provenance 主线。 |
| 2604.03870 | 继续审阅 | 多 Agent 框架的间接注入利用隐藏系统交互，若攻击链可复核，会改变 tool/trust-boundary 安全评价。 |
| 2604.03904 | 前分母关闭 | 黑盒口头 confidence + abstain payoff 属已知选择性回答激励组合，题摘未分离新校准或保证边界。 |
| 2604.03925 | 待定点裁决 | 符号 posterior 外置可保护私有互动数据并分离语义/概率 owner，但离散假设及 Dirichlet aggregation 是否优于已有外部状态需核。 |
| 2604.03933 | 前分母关闭 | Elasticsearch 专用 SRE Agent 的十一阶段自动化主张未在题摘建立可迁移 incident-control 证据。 |
| 2604.03950 | 前分母关闭 | MXFP 注意力 diagonal tile 是特定 kernel/硬件 operating point；未呈现改变本书执行计划原则的独立机制。 |
| 2604.03956 | 继续审阅 | VLA 忘却的行为可能跨视觉/投影/动作层，提出不同于文本单层 unlearning 的物理安全约束。 |
| 2604.03964 | 前分母关闭 | Science 资源→技能库处于当前明确暂缓的 AI for Science 范围，不能借 Agent 章节自动准入。 |

### 旧 90 项题摘重筛：中间 30 项

| ID | V3 初判 | 题摘层具体理由 |
| --- | --- | --- |
| 2604.03968 | 继续审阅 | 同模型充当攻击者与监测者可共谋，结构化多维监测若有可复核对照会改变单分数安全门。 |
| 2604.03997 | 待定点裁决 | 链上自治 agent 的 ledger 间接协作是形式语义，不是 LLM Agent 部署；须核 Ch82 的 durable commit 是否只是原理类比。 |
| 2604.04013 | 前分母关闭 | Lloyd-Max 条件下重整激活量化是局部 PTQ 方案，摘要未改变精度/校准/部署已知权衡。 |
| 2604.04035 | 继续审阅 | denied action 的反馈影响后续“良性”工具调用，超出扁平数据 provenance，可能改变 reference monitor 因果责任。 |
| 2604.04043 | 待定点裁决 | 少样本语义污染反驳早先结论，但需核 5 个文化数字、模型能力阈值及外推范围后判断安全设计增量。 |
| 2604.04060 | 前分母关闭 | 防守/诱导/取证三 Agent 组合是多轮攻击场景的工作流包装，题摘未显示比现有 stateful guard 更强的独立失效机理。 |
| 2604.04074 | 前分母关闭 | 科学论文审稿中的 claim extraction 与执行是 AI for Science 领域流程；现阶段不因有 Evidence 术语纳入。 |
| 2604.04131 | 待定点裁决 | 先编 workflow 再 guarded execution/按需 repair 与既有 durable workflow owner 接近；需核是否有可迁移新的判错/恢复边界。 |
| 2604.04142 | 继续审阅 | flow-matching 的 on-policy GRPO 样本成本与 replay 分布漂移，通过序列重要性校正形成新的 post-training 分支。 |
| 2604.04161 | 继续审阅 | VLA 固定 action chunk 在反应性和模式跳变之间冲突，动态长度改变物理闭环控制频率。 |
| 2604.04190 | 前分母关闭 | KG triple verification 的 schema/tool 混合是特定知识图谱应用，未改变通用 RAG/证据身份契约。 |
| 2604.04202 | 继续审阅 | 动态信息环境、冲突来源和用户纠正的隐藏 ground truth 可能补足静态 Agent benchmark 的有效性缺口。 |
| 2604.04220 | 前分母关闭 | 预测市场时间点上的模型排名/检索增益属于特定经济决策任务，未提供可迁移 Agent 评价合同。 |
| 2604.04226 | 前分母关闭 | repository 转 Agent 的新 benchmark 限于 Agentic Web 设定，题摘未证明现有 coding-agent 评价盲区。 |
| 2604.04230 | 继续审阅 | MoE router 训练阶段的拥塞/专门化轨迹可能修正静态 load-balance 理解。 |
| 2604.04238 | 前分母关闭 | 编译器与 LLM 协作优化一般程序，非大模型 compiler/runtime 本身，不能以“compiler”关键词映射 INFER-EXECUTION。 |
| 2604.04247 | 继续审阅 | 单 Agent prompt learning 扩到并行 trace 汇聚可能改变经验更新的冲突/选择机制，需核实际控制权。 |
| 2604.04253 | 继续审阅 | 3D-stacked near-memory 把带宽瓶颈移向 logic-die compute，可能改变 decode 硬件/调度协同判断。 |
| 2604.04261 | 继续审阅 | 联邦 RLHF 的平均与最差组聚合权衡触及 preference owner 和公平约束，需要核算法/实验边界。 |
| 2604.04269 | 前分母关闭 | Agentic IR 立场稿主要归纳 trajectory integrity 既有原则，缺独立机制或新测量。 |
| 2604.04323 | 继续审阅 | 现实技能搜索/选择与理想化手工精准供给 benchmark 的差异，可能改变 Skill 评估合同。 |
| 2604.04335 | 继续审阅 | 图像/视频 diffusion deadline 共置调度已完成 exact-v1 小批次审读；Books Ch56 已独立核。 |
| 2604.04347 | 待定点裁决 | 同 seed/信息/预算的 Agent evolution 比较可修正优化方案选择；需核随机性和 evaluation-budget 对齐。 |
| 2604.04373 | 待定点裁决 | test-time context 中蒸馏经验以减少搜索浪费，需确认是否超出现有 Agent memory/经验检索原则。 |
| 2604.04399 | 继续审阅 | GUI Agent 长视觉轨迹的分层诊断可能补足终局二值 verdict 的评价盲区。 |
| 2604.04410 | 继续审阅 | 偏好模型假设失效下的 density-ratio consistency 与稳定训练可能改变 DPO 类分支的适用前提。 |
| 2604.04426 | 继续审阅 | 第三方 MCP 工具的供应链恶意行为出现在网络层，若实验可核会改变 Agent 安全监测部署点。 |
| 2604.04451 | 继续审阅 | 4-step video DiT 使请求内缓存失效，跨请求 cache reuse 可能改变生成服务缓存身份与质量风险。 |
| 2604.04503 | 前分母关闭 | Manager/Planner/Executor 加压缩轨迹 memory 是熟悉的 Agent 组件组合，题摘未分离独立可验证的新状态边界。 |
| 2604.04514 | 前分母关闭 | 七通道本地记忆和遗忘曲线是产品组合；题摘自身显示 benchmark 下降，未证明长期记忆契约变化。 |

### 旧 90 项题摘重筛：末 30 项

| ID | V3 初判 | 题摘层具体理由 |
| --- | --- | --- |
| 2604.04522 | 继续审阅 | 人类授权经多 Agent 委托链的 principal/scope/provenance 绑定是独立的可审计控制契约。 |
| 2604.04523 | 前分母关闭 | DRAM-PIM 的 LUT 容量换算力为局部电路 operating point；未改本书现有推理数据流/调度方案。 |
| 2604.04532 | 继续审阅 | Judge 的评估语言与 backbone 交互导致排名反转，可能改变跨语言 Agent 评价的有效性条件。 |
| 2604.04561 | 继续审阅 | 约万次真实沙箱攻击的 prompt-condition taxonomy 若有可复核控制，可能纠正“泛化高危 Agent”安全边界。 |
| 2604.04651 | 前分母关闭 | 小模型搜索 Agent 微调改善调用频率/幻觉是特定任务学习方案，摘要未显示新的 search-control owner。 |
| 2604.04654 | 前分母关闭 | LEO 卫星链路下拆分模型、流水线与压缩属特定环境组合，未提供超出既有 distributed inference 状态/通信权衡的新机制。 |
| 2604.04660 | 前分母关闭 | append-only memory、supervised processes、git recovery 等是长活 Agent 的现有控制组合，摘要未隔离单项新因果证据。 |
| 2604.04664 | 前分母关闭 | ROS/VLA 分层框架处理机器人长期任务，但题摘主要集成既有语义/物理组件，未给新的物理闭环控制条件。 |
| 2604.04701 | 前分母关闭 | NPU 上 outlier 分解和混合→统一整数精度是特定量化实现，题摘未推翻已有精度/硬件适配原则。 |
| 2604.04707 | 前分母关闭 | World Model 定义、分类与代码库未给 action-conditioned transition 的独立新机制/反证。 |
| 2604.04712 | 待定点裁决 | adversary-tier 可行性 taxonomy 可能限定 Ch72 硬件证明结论；须判它是长期安全合同证据还是仅政策综述。 |
| 2604.04722 | 前分母关闭 | 端侧 KV bit 分配属已有重要性量化设计的局部启发式，不改变缓存 identity/fallback。 |
| 2604.04743 | 前分母关闭 | “幻觉 basin”是任务相关 latent 几何解释，题摘未证明可用于系统级事实校准或可信拒答。 |
| 2604.04745 | 继续审阅 | GPU 在进程执行期近零可见活动却仍高功耗，可能修正资源/能耗核算和降频控制条件。 |
| 2604.04750 | 继续审阅 | 3D DRAM stack 中并行/调度与互连/热设计耦合的性能模型可能改变分布式 decode 的硬件选择。 |
| 2604.04759 | 继续审阅 | 本地高权限个人 Agent 的 Capability/Identity/Knowledge 持久态安全评价可能暴露沙箱评估盲区。 |
| 2604.04783 | 继续审阅 | TFHE PBS 为加密 LLM 非线性层提供高精度 GPU path，需核与 03425 FHE 并行路线的独立设计增量。 |
| 2604.04804 | 前分母关闭 | 从经验生成可复用 Skill 库的多级蒸馏流程，题摘未区别于既有 Agent skill lifecycle 的状态所有权。 |
| 2604.04806 | 前分母关闭 | 用 LLM 维持跨请求状态来测试微服务依赖，是一般软件测试场景而非本项目 AI 平台或 Agent 评价机制。 |
| 2604.04820 | 前分母关闭 | CLI/Skill/MCP 的 ANX 协议组合未给超出现有 typed tool/authorization contract 的受控机制。 |
| 2604.04847 | 继续审阅 | 真实语音犹豫、连续 API 与打断处理同测，可能补足 full-duplex Agent 工具使用评价合同。 |
| 2604.04853 | 待定点裁决 | 原对话全量保留可避免抽取记忆丢真值，但需核是否超出 Ch77 已有 provenance/derived memory 边界。 |
| 2604.04855 | 继续审阅 | root-start rollout 与 prefix-query access 的理论可识别性区别，可能改变自回归 post-training 数据/Oracle 权限判断。 |
| 2604.04872 | 继续审阅 | MLE Agent RL 的真实 pipeline 验证过贵，synthetic sandbox 可能改变可验证反馈/计算预算的训练合同。 |
| 2604.04894 | 继续审阅 | RLVR 中粗放 entropy 奖励与优势符号不对称调节的探索/错误传播 trade-off，需要核方法和消融。 |
| 2604.04895 | 前分母关闭 | LLM Agent 参与联邦学习编排是静态策略→Agent 的通用替换，题摘未隔离新训练控制/系统保证。 |
| 2604.04901 | 前分母关闭 | 文件系统行为轨迹用于个性化是新数据场景，但题摘未建立不同于现有 memory provenance/隐私界线的机制。 |
| 2604.04913 | 继续审阅 | 视觉特征帧差压为单 token 改写生成式 world model 的计算与状态表示合约。 |
| 2604.04921 | 继续审阅 | pre-RoPE Q/K 稳定中心若属实，可能修正用近期 post-RoPE query 估 KV 重要性的假设。 |
| 2604.04929 | 前分母关闭 | 输出 token 数影响 VLM 端到端 latency 属已有成本认识，模拟数据未隔离新的多 Agent 推理机制。 |

### 旧排除集反向查漏：完整题摘定点裁决第一批

这批材料曾被旧账本用相同“局部增量”理由排除；本表逐项重新判断原文对本书的具体问题。`继续审阅`仍不是 Full Source Review；全文可能推翻题摘声称。

| ID | V3 初判 | 具体差异/关闭理由 |
| --- | --- | --- |
| 2604.03253 | 待定点裁决 | 代码执行轨迹 SFT+RLVR 改善自验证，但须确认区别于常规 execution feedback 的训练目标。 |
| 2604.03257 | 继续审阅 | 小量人工金标准、大量有偏 LLM judge 与已知 judge 约束联合估计失败率，可能改变评估发布证据的校准合同。 |
| 2604.03263 | 前分母关闭 | 158M、4K context 下局部 attention+慢记忆组合无足以修正长上下文状态设计的跨模型证据。 |
| 2604.03266 | 待定点裁决 | 冻结视频特征下多 Agent 离散瓶颈得到潜在物理属性协议，需判断是否超出特定合成环境的表征发现。 |
| 2604.03316 | 继续审阅 | 视觉 sink 同时提供全局先验和压制局部证据，可能改变多模态 token 选择/对齐假设。 |
| 2604.03340 | 继续审阅 | 视频 latent action 的 identity/inverse/cycle 约束减少未来帧泄漏与运动量错标，可能改变 VLA 数据的动作表示。 |
| 2604.03444 | 继续审阅 | 对照 Olmo 3 7B 的 hybrid GDN 模型把表达能力与训练 scaling 关联，而非只声称 decode memory 优势；旧“局部 benchmark”排除失实。 |
| 2604.03446 | 前分母关闭 | cross-operator attention dataflow 穷举/剪枝是 accelerator 映射特定优化，题摘未修正 kernel execution owner 的通用结论。 |
| 2604.03515 | 继续审阅 | 固定 commit 的 13 个 coding-agent scaffold 源码对照区分 loop、tool、状态与资源，而非按模型能力分类，可能修正 Agent 平台评估粒度。 |
| 2604.03537 | 继续审阅 | 离散 diffusion 的词表树祖先分解改变预测 head 的参数与训练显存分配，不只是多一个 benchmark。 |
| 2604.03571 | 待定点裁决 | 选择性忘却推理 trace 中敏感片段并保留结构，需核替代 trace 是否导致漏忘或证据污染。 |
| 2604.03616 | 继续审阅 | 结构化输出的能力损失主要由格式指令而非约束采样导致，直接挑战“只优化 constrained decoder”设计。 |
| 2604.03632 | 前分母关闭 | 跨尝试成功/失败和历史最佳 repo 状态是已有 durable workflow/经验复用组合；题摘未给新控制边界。 |
| 2604.03674 | 前分母关闭 | few-step DiT 的学习式 token 缓存比手工稀疏更快，但暂为局部质量-成本 operating point，不改缓存 identity。 |
| 2604.03855 | 待定点裁决 | semantic streaming CEP 的状态ful pattern 可能改变 AI 平台事件处理；当前仅演示，需核无对照的边界。 |
| 2604.03890 | 继续审阅 | 机器人 LLM 后门在自然语言阶段不传播、在结构化动作 JSON 阶段传播，直接改变物理 action boundary 检查位置。 |
| 2604.03962 | 继续审阅 | 流式 guard 从“已越界前缀检测”改为预估后续伤害的 rollout 监督，改变低延迟阻断时机。 |
| 2604.04199 | 前分母关闭 | 2047 个表格数据集的 iid 泄漏分类是一般 ML 评价；其 selection leakage 方向已知，不能直接外推到 LLM benchmark。 |
| 2604.04207 | 继续审阅 | VLM reasoning 可在正确率提高时丢失视觉证据，任务条件化低熵/低注视 veto 可能修正单一文本置信度评价。 |
| 2604.04281 | 前分母关闭 | TinyStories 小规模宽度增生 warm start 在确定/随机续训胜者不同，是受限反例，尚不足改变本项目大模型训练决策。 |
| 2604.04356 | 待定点裁决 | expert merge 比 pruning 保持性能，但 MC/生成校准集 mix 决定前沿；需核是否超出现有量化/路由校准原则。 |
| 2604.04461 | 继续审阅 | 仅 student 施加 DP-SGD、teacher 提供其 on-policy continuation 目标，可能改变私有压缩的 privacy/compute ownership。 |
| 2604.04580 | 继续审阅 | code/test 配对共同搜索可修正 coding Agent 把固定测试当完整真值的评估与验收合同。 |
| 2604.04648 | 继续审阅 | BoN 随 N 增大可能 exploit reward model；以典型响应误差作 pessimistic penalty 提供新的风险-探索分支。 |
| 2604.04767 | 继续审阅 | 零奖励困难 RLVR 题改写成同答案选择/填空，再回迁开放题，改变 curriculum 的可学习信号条件。 |

### 反向找回证据小批次：03444 / 03537 / 03616 / 03962

- **2604.03444v1（Olmo Hybrid）**：重开 [exact-v1](https://arxiv.org/html/2604.03444v1) §2–5、Table 1–2 和消融。与 Olmo 3 的 7B/6T 预训练对照把 75% sliding-window attention 换为可有负特征值的 GDN、保留 3:1 交错 attention；形状为了相近参数/吞吐调整，不能称所有变量完全相同。较少训练 tokens 达到同 loss/MMLU 不等于 wall-clock 加速，Code/GenQA 及部分 held-out 项退步，DPO 也非全面收益。理论 state-based recall 比较依赖计算复杂度假设；不能将训练收益完全归因于该定理。Ch22 已有 GDN 的写入/擦除与全局 attention 互补，本次真正增量是受控 scaling 与表达性/任务退步的条件化证据，而非再写一段“hybrid更好”。拟 2+2+3=7，深入完成，Books 等根任务实际写入与独立核验。
- **2604.03537v1（TDLM）**：重开 [exact-v1](https://arxiv.org/html/2604.03537v1) §3–4、Table 1–2 与 level-weight 消融。词表递归 K-means 等深叶子树把 flat head 改成 parent-conditioned child prediction，forward 到祖先、reverse 向 children，跨层 ELBO 分解不等于直接沿用 hierarchical softmax 的训练目标。OWT、序列512不packing、131B训练tokens，small/base head减少后重配更深attention层；4×24GB RTX3090约束下比较显存/吞吐。small PPL不及HDLM，base略好；binary深树的coarse-level ELBO更大，强行增加高层权重反而退步，512采样steps均分两层胜过过量给粗层。未证明大型语言模型、长上下文或实际服务SLO收益。Ch24现有masked/层级diffusion解释需对照是否缺少“预测空间分解→head资源重配→层间误差/采样预算”的机制分支。拟2+1+2=5；标准审阅完成，如整合则补深入采用核验。
- **2604.03616v1（The Format Tax）**：重开 [exact-v1](https://arxiv.org/html/2604.03616v1) §3–7、Table 5 与 Appendix评测声明。完整prompt/few-shot/task/GCD factorial；6 open3B–32B模型、4API、MATH500/GPQA198/ZebraLogic500/WritingBench500、JSON/XML/Markdown/LaTeX。同prompt比较GCD，72 cells中显著39、prompt-alone36、GCD15；不是39/72都来自GCD。两轮先freeform再reformat降低损失但增加调用、latency与约双tokens；thinking在部分任务退步，WritingBench不成立。MATH依赖gpt-5.4-nano等价judge，writing依赖gpt-5.2，不是人工绝对真值。只测呈现格式，作者明确禁止外推编码正确性约束的tool arguments/code/test generation。Ch20目前区分penalty/grammar mask但仍主要讨论decoder屏蔽，可加入上游prompt竞争与生成/格式化分离的条件分支；Ch78仅handoff、不承载外推。拟2+2+2=6；因拟修正文中因果解释，深入完成。
- **2604.03962v1（StreamGuard）**：重开 [exact-v1](https://arxiv.org/html/2604.03962v1) §2–5、Table 3–5、Appendix E。监督目标是给定prompt/prefix、proposal continuation分布下终局伤害judge的期望，不把unsafe-final标签粗贴所有前缀；MC rollout与linear head形成预测式sensor。Llama1/3/8B并迁移Gemma/Qwen tokenizer，3seeds；on-time定义at/before unsafe sentence end，response_loc全unsafe令precision100%，不能读成通用零误报。max reduction更早阻断却FPR更高，mean作平衡。H100、HF StaticCache、1024-token prefix后1024步、100runs；70B两卡，2.4–9.5ms仅steady-state配对，不是多租户端到端保证。guard score受generator/judge/rollout覆盖限制，不是事实正确率或安全authority，外部authorization/buffer/commit gate仍需保留。Ch72已有streaming sentence-commit；本次可能增量是“检测已越界→预测future harm”的监督/误阻断分支。拟2+2+2=6，安全采用命题深入完成；等待根任务实际Books判定。

这些证据小批次尚不能证明全日分母完成；未审材料仍为待办，不当作外部受阻。

### 第二轮定点准入裁决（完整题摘；少数必要段落）

| ID | 裁决 | 原文增量或具体关闭理由 |
| --- | --- | --- |
| 2604.03539 | 前分母关闭 | CB-VER研究网络控制面eventually-stable证明；无LLM、训练/推理平台直接研究，本书连接只能是类比。旧Ch73源绑定待根任务定点纠正。 |
| 2604.03997 | 前分母关闭 | 原文明确是区块链keepers/arbitrage bots的ledger形式映射，不是LLM Multi-Agent的模型/执行机制；不能借自治软件agent同名准入。旧Ch82源绑定交根任务。 |
| 2604.04712 | 前分母关闭 | 20项硬件治理成熟度与政策场景taxonomy，未给新证明/实现/测量来解决计算attestation的具体技术分歧。对主题有关但不足贡献门槛；旧Ch72绑定交根任务。 |
| 2604.03925 | 前分母关闭 | recommendation中外置离散Bayes posterior与LLM entropy加权是成熟概率更新/语义组合，题摘未识别新增保证或跨轮状态失效边界。 |
| 2604.03588 | 保留待审 | 多目标memory不共享唯一ontology、Dung attack graph可保留未消解冲突，改变memory query阶段的“必选一个真值”假设；proof-of-concept不等于生产有效性。 |
| 2604.03809 | 保留待审 | 同模型role committee的相似度/effective rank依赖embedding encoder，且hint-sharing强于diversity权重、收益与run variance同阶；这是对独立投票/潜在通信proxy的具体反证。 |
| 2604.04043 | 保留待审 | few-shot numeric content与nonsense结构对照反驳“只fine-tune才有污染”的边界；要审受测模型/样本与能力阈值，不外推所有prompts。 |
| 2604.04131 | 保留待审 | profile→guarded operator→verify→bounded repair把推理调用数量约束为2/3，并保留online-adaptation时ReAct更好的条件；需要核bounded-repair假设与实际比较。 |
| 2604.04347 | 保留待审 | 同seed/信息/1500evaluation预算比較Elo/Pareto/greedy，可能修正Agent优化评估budget的选择；不以“首个比较”准入。 |
| 2604.04373 | 保留待审 | 本次必要正文补读显示记忆规模非单调、relevance/diversity权衡与concept-group retrieval，而非只有“总结经验”；但HTML缺少主结果section/图编号，采用结论须以PDF补核。 |
| 2604.04853 | 保留待审 | 六维消融把query/retrieval阶段与ingestion收益拆开，可修正只优化抽取记忆的优先级；保留episodes本身是既有原则，不能当新突破。 |
| 2604.03253 | 保留待审 | 将execution output预测与题目求解训练为两个互补objective，区分真实运行反馈与自身模拟反馈，需核自验证何时引入相关错误。 |
| 2604.03266 | 保留待审 | 冻结视频prior、通信离散瓶颈与多agent/带宽/帧数对照，干预潜在物理属性，能限定world-state可表达内容；不是一般物理应用指标。 |
| 2604.03571 | 保留待审 | 目标从final answer扩到CoT敏感片段，placeholder/feature-replacement同时要求保留推理结构；须核遗忘probe/残余泄漏而非宣称删训练样本即遗忘。 |
| 2604.03855 | 保留，标准证据已读 | exact-v1§3把LLM抽取的typed/timestamped event交给per-entity NFA；negation强制within，窗口结束才可接受，隔离概率提取与确定性时序。256 clinical notes/5patterns/三模型只测该输入，不能称一般实时正确保证。 |
| 2604.04356 | 保留待审 | router-weighted expert merging相对删除expert保留参数信息，MC/GEN前沿依赖校准mix；需核Pareto预算和压缩同条件。 |

### 标题全览后第二批反向查漏（完整题摘）

| ID | 裁决 | 原文增量或具体关闭理由 |
| --- | --- | --- |
| 2604.03242 | 保留待审 | 长Agent安全trajectory中latent Extractor+原轨迹Reasoner的联合监督，区别有损显式summarize-then-judge；需审sparse evidence与消融。 |
| 2604.03244 | 保留待审 | OpenEval item-level10M responses/155K items使construct validity可检查，需核实际纠错实例，不能只沿用“应发布数据”的立场。 |
| 2604.03302 | 前分母关闭 | continuum physics新任务与simulator多任务fine-tune主要提供领域操作点，题摘未改变world-state/action transition或物理闭环机制。 |
| 2604.03472 | 保留待审 | proposer reward collapse下硬、非定常vocabulary mask改变self-play课程探索可行域，而非只加entropy奖励；需核多样性/solver受控收益。 |
| 2604.03551 | 前分母关闭 | agent PR merge-conflict数据集量化常见软件集成问题，未新增LLM生成/评价/协作控制机制；不将27.67%直接外推Agent质量。 |
| 2604.03556 | 保留待审 | vision encoder的三阶段processing与focus阶段局部抑制可能补足hallucination的因果解释，不能只取新降低指标。 |
| 2604.03610 | 前分母关闭 | 用crash/debugger进行hypothesis→probe→patch验证是既有dynamic-tool闭环在C/C++修复的组合；题摘无新控制边界或受控因果隔离。 |
| 2604.03647 | 独立反向抽检恢复；标准审阅完成 | 原“单类几何+成熟组合”拒绝理由过宽，不能否定固定prefix局部重采样改变proposal、母集合/重采样集合频率ratio连续reward的可复用设计分支。exact-v1 Eq6–8及AppA.2.4/Table5已核，评分2+1+2=5；具体Books终态见下方局部重开记录，不复用原拒绝裁决。 |
| 2604.03677 | 保留待审 | dLM双向infilling受SFT response-only masking而非架构限制，full-sequence masking改变training/inference可用能力；明确可测试的设计反证。 |
| 2604.03754 | 保留待审 | truth-direction universality受layer/task/difficulty/prompt指令变化限制，直接反驳单一probe当通用truth authority。 |
| 2604.03764 | 保留待审 | attention pattern learned proxy跨模型适用与干预强度导致collapse，可改变interpretability probe的有效性/因果界限，须核代码场景与统计。 |
| 2604.03922 | 保留待审 | generated test的正误循环依赖被LOO-AUC ranking consistency替代；理论oracle近似有average-quality假设，需核相关测试/代码错误是否破坏保证。 |
| 2604.04385 | 保留待审 | 12模型interchange/knockout对照分离低DLA gate与深amplifier，ablation缩弱不等于没有因果gate；可能改变alignment测量方法。 |
| 2604.04418 | 保留待审 | error verifiability测rater识别答案正误而非被解释说服，accuracy/scaling不保证可核验性；与人类对照须核estimand。 |
| 2604.04565 | 前分母关闭 | Answer/Ask/Abstain planner与information-state SFT是既有选择性问答组合；题摘不足支持“只能通过training”的普遍断言。 |
| 2604.04863 | 前分母关闭 | patch-level统计+hidden feature检测对象hallucination为局部实现；题摘未分离新的grounding机制或修正已有视觉证据分散/伪相关边界。 |
| 2604.04930 | 前分母关闭 | intermediate-confidence trajectory early stop是现有动态halting分支的局部实现；题摘没有新增校准保证、失效条件或可复用控制机制。 |

### 已证旧审阅污染，不作复用

旧 `exact-v1-review-packet.json` 的 `2604.04399`（GUIDE）把GUI trajectory evaluator写成memory write/read/evict owner，Method引用§2.3 related work、Evaluation引用§2.2 background，正文重复模板trade-off。因此只复用身份和可核原始HTML，不能继承旧review_complete、score或已有覆盖。所有本次保留项围绕实际命题重新核必要Method/评价/关键反证；没有阅读全文的普通待办不标受阻。

### 已完成必要正文审阅的小批次（不等于全日报完成）

以下均重新打开对应 exact-v1 HTML，读取所列方法、实验及关键反证；共享 Books 的实际写入由根任务协调，尚未实际核对的仍是待办，不以提案替代整合。

- **2604.03270v1 / Knowledge Packs**：[原文](https://arxiv.org/html/2604.03270v1) §2–5、limitations。Exact-prefix KV 等价要求 checkpoint、canonical chat template、position 与 causal prefix 相同；把两份独立前缀缓存直接拼接不等价，既有 RoPE 位置也不能只靠旋转修复缺失的 conditioning。作者实际 bank routing 是 top fact 文本重新 prefill：4 MB/5K facts 主要存 text+embedding，不是预生成 KV 容量；“zero token”不免除 attention 的 context、内存或位置约束。Qwen3/Llama3.1-8B、FP16、A100-80GB、700 HotpotQA 同前缀实验支持缓存等价，100 样本 accumulation 与15 coding tasks steering 不支持一般事实或能力保证。Ch45 已有 prefix/checkpoint/template/position identity 和失败回退，倾向已有覆盖；value steering 仅保留受限实验，不扩写成“知识包可替代上下文”。拟2+2+2=6，深入完成（纠正宣传口径）。
- **2604.03362v1 / ABTest**：[原文](https://arxiv.org/html/2604.03362v1) §3–5。400 bug reports 归为47 interaction patterns×128 action types，兼容组合647tests；固定 repo workspace 执行后用JSON/artifact checks标记，再人工确认。Claude/Codex/Gemini五配置共3235次单次运行，1573flags中642人工确认，40.8%为检测precision，不是Agent错误率；368 minor failures 也不是严重安全事故。Ch66 outcome witness 已区分判定链，但从已知 bug pattern×action 生成交互测试且将检测 precision 单独验收是具体增量。拟2+2+2=6，采用需根任务核对并落实正文，不能用现有review note代替。
- **2604.03425v1 / AEGIS**：[原文](https://arxiv.org/html/2604.03425v1) §4–5。联合token-coherent/modulus-coherent ciphertext layout、RNS slice reduction与operator reorder来隐藏comm；PyTorch FX compiler生成加密执行计划。BERT-Base/SST-2而非LLM decode，128-bit CKKS、N=2^16、slots=2^15、Q=35/P=4/boot14；2×A6000-48GB NVLink与4×A100-40GB，后者2048输入端到端仍约5036s。GPU移植Cinnamon/Hydra排除原ASIC/ISA/interconnect特性，不能当完整硬件同预算比较。Ch72已有FHE隐私分支，潜在增量是加密layout与通信执行计划共同编译，不是FHE总体实用性结论。拟2+2+2=6，安全采用深入审阅，待根任务判定。
- **2604.03465v1 / The Tool Illusion**：[原文](https://arxiv.org/html/2604.03465v1) §3–4。WALT、SkillWeaver、Hybrid-Agent与五backbone、两webbench对照，tool synthesis的模型/使用者能力差、UI-state-dependent control和library retrieval/inspection开销决定收益；多工具不等于更广任务覆盖。任务与站点范围受限；不是禁止Tools或证明工具无效。Ch78已有compositional selector，但封装颗粒度、工具library上下文税与剩余reasoning ownership的条件对照值得核验。拟2+2+2=6，待根任务实际增量裁决。
- **2604.03855v1 / VectraFlow**：[原文](https://arxiv.org/html/2604.03855v1) §3–5、limitations。LLM生成typed/timestamped events，entity key下NFA维护Take/Ignore/Proceed；共享rule编译、隔离instance state，skip-till-any-match，否定要求within且窗尾才接受。256 clinical notes/5patterns、GPT-4o-mini与Qwen3-8/4B；full-context baseline GPT F1=.675、14.6M tokens，semantic-pattern retrieval约3.1M、F1=.848/.862/.822。这是语义抽取与确定性时序分工的机制证据，不是医学方法；未披露一般stream lateness/watermark、生产latency或抽取真值保证。Ch81已有temporal verifier，但否定有限窗与probabilistic extraction隔离为具体分支。拟2+2+2=6，标准完成，采用则深入核验。
- **2604.03592v1 / RISE**：[原文](https://arxiv.org/html/2604.03592v1) §3–5、Appendix C。同类任务的多语言routing frequency/weight profiles决定浅/中/深expert选择；target语言exclusive浅/深与中层共享不同，冻结未选expert与router。Qwen3-30B-A3B/Phi-3.5-MoE、single H200、BF16、3epochs、batch2×acc8、lr2e-5；128/6144和16/512只减少gradient/optimizer state，不消除全部resident weights/activations。Appendix C exact preservation要求固定router且routing支持集不相交，不是现实所有语言无干扰定理。Table3 Phi Bengali46.89低于TopK49.51，target gains不证明总优；Table5 pruning也使多种其他语言大幅下降，不能照抄“causally language-exclusive”。Ch21现有capacity/routing主线未明确参数更新域应随层级language overlap校准，拟2+1+2=5；需据这些反证收窄整合命题。
- **2604.03675v1 / PRAISE**：[原文](https://arxiv.org/html/2604.03675v1) §3–4、Appendix A。旧题摘“OASES”是后发版本污染，本文必须绑定v1标题PRAISE。每个search prefix另生成answer，与gold answer做EM/F1；相邻prefix answer性能差形成turn-end reward，主答案另得terminal reward。复用prefix-answer sample本身也得terminal reward，shared policy同时训练search/answer；因此不是把模型自信当reward或额外真实search transitions。Qwen2.5-7B、verl、E5/Wikipedia、α=.5；freeze evaluator或只拿policy做未专训evaluator退步，14B无process reward也可能受损。PPO可消费不同prefix token-level rewards，GRPO需同state groups、逐turn会放大rollout成本；不是PPO普遍优于GRPO。GPU/precision/服务SLO未披露。Ch32已有MC/TD conditional reward coherence与counterfactual resets，本例新增同轨迹prefix answer复用及shared evaluator drift的条件分支。拟2+2+2=6，采用需根任务落实。
- **2604.03676v1 / Retrievers Cost Study**：[原文](https://arxiv.org/html/2604.03676v1) §3.5、§5–6。BRIGHT12tasks/14retrievers，4×H100-80GB、FP16、CUDA12.4/Torch2.8/Transformers4.57、median3runs。文档embedding缓存时query测量不含index build或生成reasoning query成本，因此轻encoder长query附加推理近零不能称整个augmentation免费。长文保留/short chunking改变语料与证据覆盖，不能只归因encoder参数；数学/代码query全五扩写源退步。BM25 fusion可伤强retriever、DAT退步；top1score预测gold in top-k AUROC仅.508–.611为discrimination，不是概率校准。Ch76已有query-dialect、packing/coverage、score≠truth及hybrid分支；待具体对读后倾向已有覆盖，拟2+2+2=6、标准完成。
- **2604.03679v1 / LightThinker++**：[原文](https://arxiv.org/html/2604.03679v1) §3–4、Appendix C。Commit形成summary/raw关联，Expand/Fold控制visibility，不把raw永久丢弃；无Expand/Fold消融与同dataset训练对照支持可逆控制的局部分支。Qwen3-30B-A3B-Thinking、8GPU/3epochs；Vanilla6625trajectories与3677分解为42633instances的数据不等预算，lr/batch/max sequence也不同，不能把全部性能差归因memory mechanism。Timing总concurrency32，但TokenSkip按batch32而其他按question-level32，比较依赖serving实现。Ch77“从不可逆Summary到可切换Raw/Summary Visibility”正文已直接承载相同论点与backtracking/thrashing/provenance边界；已有覆盖 `AGENT-MEMORY`，拟2+2+2=6，标准完成。

本批发现的v1标题污染、RISE target-language比较与跨语言pruning反证均已隔离，不沿用旧模板主张。待办仍包括其他暂存保留项的必要正文、最终分母与独立日级Gate；目前不存在全日完成声明。

### 安全 / 物理闭环 / 路由证据小批次

- **2604.03870v1**：[原文](https://arxiv.org/html/2604.03870v1) §3.1–3.3、Table1/3/4。AgentDojo Banking改造为16tasks×9objectives×4IPI=576scenarios，九open backbones；统计behavior/entropy部分只在hijacked failures上，不是所有请求分布。RepE从baseline aligned/hijacked paired traces取hidden state，按格式筛选后80/20train/test并选layer；tool-input位置通常强于function-call，但Llama cosine例外。高AUC/TPR@FPR5%没有adaptive攻击、不同suite或真正production阻断保证。Ch72已有learned sensor与deterministic action authorization分权，本结果为该既有分支的局部位置/阈值证据；拟2+2+2=6，安全深入完成，倾向已有覆盖，不把“robust circuit breaker”升级为安全证明。
- **2604.03956v1 / VLA-Forget**：[原文](https://arxiv.org/html/2604.03956v1) §3–4、Table4、Appendix B/D。Forget/retain gradients和ratio选择vision/projector/upper action-backbone层，依次LoRA编辑并用PCGrad避免目标冲突；近邻boundary set只降低浅遗忘，不构成erasure。OpenVLA-7B/pi0fast、OXE/PushT、BF16或FP16、rank16；GA可更强forget却伤utility，去retain term亦伤TSR。正文5seeds与Appendix“final should3seeds”、4000instances与5000/1200/1200、FC定义CE与表中指标口径未完整对齐；hardware只写single modern GPU，不能复述宣传百分比为确定受控结论。保留机制为approximate分阶段编辑，但尚不足新增physical safety结论；Ch72已有多substrate probe/retain-utility边界。拟2+1+2=5，标准完成，仅报告且列证据限制，不把这些统计冲突变成普通待审。
- **2604.03968v1 / TraceGuard**：[原文](https://arxiv.org/html/2604.03968v1) §3–5、Table2/5、limitations。五维每步独立LLM calls+七stateful heuristics+intent analyzer，trajectory换ID清状态；independent calls不证明独立误差。BashArena/ClaudeSonnet4/GPT4.1-mini，519样本的bash_heuristic在threshold.3 safety82.1%/usefulness69.2%、.5为70.8%/93.9%。Table5分权100%只对应earlier run阈值.3 n=20、.5 86% n=7，不能与519合并。5或6API calls、手调weights、nonadaptive attack。Ch69现“519样本支持separation-of-duties”需修正；拟3+2+2=7，深入完成，根任务协调纠错，尚未核实际修订。
- **2604.04035v1 / Causality Laundering**：[原文](https://arxiv.org/html/2604.04035v1) §2.5/3.7/7/9.2–3。拒绝结果本身可泄露秘密，但所谓Counterfactual edge仅denied action→下一tool call的时间邻接heuristic，既误拒紧邻良性动作又漏延迟chain，不是perfect causal inference。Min-reachable trust依赖真实field provenance/ingestion labels，不能自授declassification。三人工攻击场景只比较flat citation与graph其余policy layers固定，没有frontier LLM benchmark；AppleM4Pro48GB、warmup后median100次、session数十tools/数百nodes的<1ms不外推长histories。Ch72既有Deny-disclosure段应明确temporal approximation，拟3+2+2=7，纠错深入完成，待根任务改写核验。
- **2604.04142v1 / OP-GRPO**：[原文](https://arxiv.org/html/2604.04142v1) §4–5、ablation。每condition至多一个最高reward且衰减老样本，mixed group用G−1fresh+1buffer；保留current/old per-step clip，用old/off的sequence correction另外加权，避免clip错误参照旧buffer policy。低noise方差趋零使importance ratios病态，off-policy只复用前段、末段当前policy重生成。Reward筛选及group相对优势意味着实验稳定不等于unbiased，较高buffer比例也发散。SD3.5-M/Wan2.1-1.4B、EvalGen/text规则/PickScore及unseen quality metrics；“34.2%steps”不等于同wall-clock/质量普遍无损，GPU/precision等未见完整声明。Ch33 off-policy ratio主线需对读其flow-matching低noise分支；拟2+2+2=6，采用深入核验，待具体Books裁决。
- **2604.04161v1 / Adaptive Action Chunking**：[原文](https://arxiv.org/html/2604.04161v1) §4、§5.1.2/5.1.5/5.2。N并行samples估continuous covariance entropy+gripper discrete entropy，Eq5取平均entropy的最大增量点并设下限ξ，不是校准风险分数。GR00TN1.5、冻结Eagle2/projector仅训diffusion-head，8×A800mixed precision；LIBERO40tasks各50rollouts/RoboCasa100rollouts，实机Realman+Mycobot两个RGB视角、50demos/任务、20trials/任务、600steps上限。SingleA800样本1/20/40推理83/106/157ms，Table4 success随samples非严格单调，不能沿正文称continuously提高。下限避免jerky mode跳变，却扩大open-loop；样本entropy可能错过共同偏差，不是安全guarantee。Ch26固定chunk/observation freshness可补统计proposal决定commit horizon的条件分支；拟2+2+2=6，采用深入完成，待根任务。
- **2604.04202v1 / ClawArena**：[原文](https://arxiv.org/html/2604.04202v1) §2–3、Appendix B。hidden Layer0经多渠道噪声/冲突与staged updates产生可追溯ground truth，MC set-selection、belief revision graded、silent preference checks、executable workspace checks分开。64scenarios/1879rounds/365updates，但cross-framework只startup-outage一scenario，cross-model12scenarios337rounds；MC前者per-option、后者exact-match，不可横比range推断模型比框架重要。Table4标GPT5.1、正文说5.2，identity口径不一致；3.5pp单配置subset差不能证明所有模型representativeness。Ch66已有动态信息/可执行witness测量，机制可作为受限例证，框架与模型排名仅报告；拟2+2+2=6，标准完成，最终采用待具体章节对读。
- **2604.04230v1 / Three Phases of Expert Routing**：[原文](https://arxiv.org/html/2604.04230v1) §2–6/8。Mean-field game用router logits估reduced preference而非独立expert quality；static MFG等temperature softmax，independent cluster-softmax L1=.133比coupledMFG .146更好。OLMoE20checkpoints50texts和OpenMoE6checkpoints30texts支持effective congestion非单调轨迹；后者还有dormant phase，不宜写同三个阶段普遍成立。Dense softmax模型top1 out-of-scope，continuation bound8–35倍实误差，线性congestion假设不涵盖hard capacity。只能把拟合参数作为diagnostic，不证明调balance loss会提高模型质量；Ch21已有routing dynamics/负载与specialization分开，倾向已有覆盖或仅报告。拟2+1+2=5，标准完成。

### Evaluator / Context / Safety 第二小批次

- **2604.04247v1 / Combee**：[原文](https://arxiv.org/html/2604.04247v1) §3–4。sqrt(batch)组内再组间聚合、重复reflection后shuffle平衡位置偏差；LLM reduce并非数学上可交换/结合的scan。Batch profile用power-law delay和plateau阈值选择并行数，仍同步提交下一context。Ch77“并行经验汇总需要Bounded Fan-in与Context Version”实际正文已写worker局部证据→curator提交、parent version、冲突、同源错误与sequential共存；不是仅Review note。拟2+2+2=6，标准完成，已有覆盖；不把trial profile当通用最优规模。
- **2604.04261v1 / APPA**：[原文](https://arxiv.org/html/2604.04261v1) §3、实验及Appendix训练配置。冻结PluralLLM在各group本地数据上提供reward vectors，不传模型参数/梯度供fed averaging；中央PPO按历史EMA(.8)、reverse softmax(T=.1)、FI阈值(.99)调权。低且相等reward也能FI=1，fairness score不是质量。GLOBALQA/OQA，Gemma2-2B/Llama3.2-3B/Qwen3-.6B；SFT BF16、PPO NF4/BF16 LoRA-r16、maxseq500/response60，三A100节点并行不同实验、每run单卡，不是分布式训练证据。Ch31“Pluralistic Aggregation”body的“客户端贡献更新”有歧义，拟3+2+2=7纠错深入，待根任务修正后同步。
- **2604.04323v1 / Skills in the Wild**：[原文](https://arxiv.org/html/2604.04323v1) §3–4、Appendix B。强制载入→自动选择→检索curated/noncurated分阶段；SkillBench/TerminalBench、ClaudeOpus4.6/KimiK2.5/Qwen3.5、Harbor Docker三run。非curated对Qwen/Kimi可低于baseline，query-specific修订受starting artifact相关性限制；GPT5.4 coverage judge相关性不是因果验证。Timeout设定模型不同，不把排名当同预算比较。需对读Ch84实际Skill lifecycle而非不存在的Skill章节；拟2+2+2=6标准完成，暂未冻结Books处置。
- **2604.04399v1 / GUIDE**：[原文](https://arxiv.org/html/2604.04399v1) §3–4、消融。Action-text segmentation→VLM用subtask截图/全局目标评分→LLM聚合可恢复错误，不是memory-write机制，也不是hard AND所有subtask。Gemini3Flash/o4mini，932条ecommerce(345success/587fail)、5–80steps，AgentRewardBench1302/Android480；去seg74.14低于naive85.61因prompt专为subtask，去summary87.41/recall69.28对full95.80/93.62。200subtask单annotatorκ=.89不证明整体真值；implicit business norms未输入时仍错误。JSON最多retry10，须计调用成本。Ch66需具体比较“recoverable subtask evidence聚合≠逐步失败即终局失败”；拟2+2+2=6，采用前须深入核验。
- **2604.04426v1 / ShieldNet**：[PDF原文](https://arxiv.org/pdf/2604.04426v1) pp4–9。HTML标v1却显示August24封面，故本次Method/结果以April7封面的PDF v1为准，版本污染隔离。MITM系统proxy+PCAP并blockUDP443限制QUIC，将解密HTTP插回typed时间事件；Qwen3-.6B SFT对event窗口识别网络副作用。10k+MCP tools/25techniques用canary确认activation，6k训练、heldout17servercategories/3techniques。Table2 any-trace FPR.022/F1.998；Table3 per-PCAP FPR.008/F1.995、时间overhead21.38%，不得混口径或称零成本；不解密FPR.896。检测是已观察effects，不能防止已发生exfiltration；host-local行为/其他协议不覆盖。MITM权限、隐私、证书与deterministic egress authority仍必要。Hardware/precision Not Disclosed。拟2+2+2=6，安全深入完成，待Ch72实际网络sensor段对读。

### 已落实 Books 修订的独立对读

报告作者已对读根任务新写的Ch22 Olmo、Ch69 TraceGuard、Ch72 ARM机制正文与上述exact-v1，三处限制与原文一致。Olmo少tokens≠wall-clock、TraceGuard519组合detector实验与分权20/7样本分开、ARM时间启发式FP/延迟FN和三个手工场景均真实写入。Ch69旧Review note仍有519分权混称，已通知根任务同步；该处修正前不能将书稿一致性算完。

### 当前已审项的共享 Books 精确待裁决清单

这不是新增owner列表，也不是要求每篇新增正文；根任务须按实际缺口决定整合/已有覆盖。已读上下文保持复用。

| Family | 当前body比较与尚缺命题 | Primary采用位置 | 当前下一步 |
| --- | --- | --- | --- |
| 2604.04261 | Ch31 Pluralistic Aggregation的“客户端贡献更新”应明确冻结PluralLLM产生reward vectors、中央PPO，而不是参数fed averaging；FI可在低reward时接近1 | §3、实验、Appendix训练配置 | 纠错；根任务共享写 |
| 2604.03537 | Ch24已有层级/并行生成，但未见词表树parent-conditioned head→显存重新配置→层间ELBO与step预算取舍 | §3–4、Table1/2、level-weight消融 | 对读是否已有覆盖，否则窄幅机制 |
| 2604.03616 | Ch20 grammar mask/格式验收已有，未区分上游格式prompt tax与decoder mask因果、freeform→reformat的双调用分支 | §3–7、Table5、评测Appendix | 拟补有条件分支；禁外推tool/code语义 |
| 2604.03962 | Ch72流式sentence commit已有，未明确用continuation rollout预测future harm而非unsafe终局标签复制到prefix | §2–5、Table3–5、AppendixE | 可补预测sensor及FPR/延迟，不提高authority |
| 2604.03362 | Ch66 outcome witness已有；bug-pattern×action交互自动造测试与低人工precision的输入fuzz边界尚需对读 | §3–5、limitations | 先根任务裁决已有覆盖/新分支 |
| 2604.03425 | Ch72明文边界/转换已有；具体CKKS layout与GPU重排只是实现例证，未必值得新body | §4–5、长seq成本/消融 | 可仅报告或已有覆盖，非强制新增 |
| 2604.03855 | Ch81 durable temporal state已有；LLM抽取typed events→per-entity NFA、negation必须bounded within才可判accept的分层尚需比较 | §3–5 | 核现有actualbody，若无再补小分支 |
| 2604.03592 | Ch21 routing/profile已有，特定语言更新层/共享层的gradient ownership条件（fixedrouter/disjoint支持才严格保留）尚需比较 | §3–5、AppendixC | 不把语言label当exclusive proof |
| 2604.03675 | Ch32 MC/TD credit已有；prefix相邻短答案差分复用与同一policy评自身偏差、PPO/GRPO不同state组别是否新命题 | §3–4、AppendixA | 先具体owner裁决 |
| 2604.04142 | Ch33 stale buffer/correction已有；flow低noise重要性比病态及suffix当前policy重采样为特定分支 | §4–5、buffer比例ablation | 对读后小分支或已有覆盖 |
| 2604.04161 | Ch26 action chunk/freshness已有；多proposal entropy增量决定commit horizon，不是校准risk且下限增openloop | §4、§5.1.2/5.1.5/5.2 | 对读后小分支或已有覆盖 |
| 2604.04399 | Ch66 Trajectory Judge已有action/observed effect层，未必已有recoverable subtask评判与终局aggregation不等于hardAND | §3–4、w/oSeg/w/oSummary消融 | 原旧GUIDE模板无效；实际比较后决定 |
| 2604.04426 | Ch72 egress authorization已有；MITM/PCAP网络effect sensor是已发生effect的检测，不等前置阻断 | PDF v1 pp4–9、Table2/3 | 不同protocol/hostlocal盲区受限新例证 |

另已实际对读确认：Tool Illusion在Ch78“Interface Granularity：不是Tool越多越有能力”正文与catalog context tax完整承载；Skills in the Wild在Ch66“Skill必须在真实Control Path中评估”正文完整列强制载入→选择→检索→适配及no-skill退步。两项分别已有覆盖AGENT-TOOL-CALLING/PLATFORM-EVALUATION-SYSTEM，不再请求重复新增。

### 成本、授权与评价小批次

- **2604.04410v1 / RDRO**：[原文](https://arxiv.org/html/2604.04410v1) §3.1–3.4、§5、Appendix F。Preferred与nonpreferred支持不同使ordinary ratio不稳，relative ratio `p+/(αp+ +(1−α)p−)`限制在[0,1/α]；gradient系数有界不等于所有参数梯度有界，consistency依赖population risk/可表示目标，finite-sample bound仍有函数类/样本前提。Qwen2.5Instruct1.5/3B、Llama3Instruct3/8B，UF-G6088/9644和MIX14K6750/6750、TRL/AdamW1epoch lr5e−7batch128/clip1、8H10080/ZeRO3、三seed，AlpacaEval GPT4Turbo length-controlled judge。UF-G多数改善，MIX14K非全胜且多α与DDRO无显著差；需全标binary偏好，理论不是人类偏好普遍正确保证。拟2+1+2=5标准完成；Ch34需对读population preference objective与ratio稳定分支。
- **2604.04522v1 / HDP**：[PDF](https://arxiv.org/pdf/2604.04522v1) pp4–7/§3–4。Root把principal/scope/session/expiry签名，每hop签此前chain并检查seq/maxhops；v0.1实际全部签名共用issuer key，multi-key仅未来计划，与摘要multi-party-signing须分开。Scope含自然语言intent但semantic action validation明示应用层责任；签名不证明人真正同意、scope语义正确、key uncompromised或不泄露token内容。Offline不查revocation用expiry/session替代，chain变长增bytes/验证成本。需继续读§5–7与既有Ch72delegation body后给处置，暂不声称深审完成。
- **2604.04532v1 / Multilingual DevAI**：[原文](https://arxiv.org/html/2604.04532v1) §3–5/7。固定55tasks/三developer frameworks同artifact与judge pipeline，在五种语言六backbones测requirement verdict，paired Wilcoxon/Holm/95%bootstrap支持judge-language排名变化，不是重新运行solver质量差异。缺multilingual人类gold、terminationmetadata不全、cost fields全0；runtime/tokens只proxy。均值std为task variation不可当多次运行误差；低baseline会压缩语言差异。Ch66已有evaluator language/construct identity，拟2+1+2=5标准完成，倾向已有覆盖，具体正文对读待同步。
- **2604.04561v1 / Prompt Condition Exploitation**：[原文](https://arxiv.org/html/2604.04561v1) §2–5/8.5。Ephemeral Docker无network/mount，37promptconditions同safetyinstruction，编程题+人工埋三类test bypass；五主backbonesn45–50/cell、两个时间快照模型，Fisher/Clopper–Pearson/Bonferroni。只有三goalreframing在Claude单模型校正后显著；checkhidden不通过单模型校正，不能称全部12心理维度机制成立。判定是关键词toolcall而非完整harm detector；自然配置、其他攻击和GPT4.1零结果归因未证，traces仅每条件5补采样。Ch72已有goal-preservinginjection与独立authorization，拟2+2+2=6安全深入完成；保留限定测试结果，不能新造“模型免疫”。
- **2604.04745v1 / GPU Execution-Idle**：[原文](https://arxiv.org/html/2604.04745v1) §2.1–2.3/4.3/4.5/5.1/5.3。756GPU学术Slurm整卡、31days1Hz遥测；residentjob同时compute/memory<5%、communication<1GB/s且持续5s形成execution-idle，缺信号省略不可当0。19.17%时间/10.67%能量的分母是in-execution排除deepidle，不是全机房。Keyword job分类/通信前序聚类只相关不是原因。Llama13B/vLLM/L40S回放公开到达和长度；8GPUpacking可令energy56%而avgSM相近。1175s同request总量的3s触发/5s冷却降频：SM-only平均power−22%、p95+29%；SM+memory−34%、p95+160%，不能外推SLO。Ch70已有idle allocation计费但未分resident-executionidle/deepidle的能量与utility，拟2+2+3=7深入完成，拟PLATFORM-COST局部整合。
- **2604.04750v1 / DeepStack**：[原文](https://arxiv.org/html/2604.04750v1) §3.1–3.3、4.2、5.1/5.6。Graph→area/thermal合法hardware→TP/EP/SP/CP/DP/FSDP/PP→peroperator tiling/collectives联合搜索，漏EP会令硬件选择也变，不只是软件latency。MoE routing取trace、activation/KV/10%reserve筛配置；分层top5%prune不是全局最优证明。H100/B200实机仅校准kernel/runtime模型；3Dstack性能是7nm/固定area25600mm²建模，H100*/H200*缩放非当前市售卡直比；Llama70/405、DeepSeek/QwenA16W8/16、input/output1024/batch1–1024。Ch49已有execution-plan联合模型/硬件约束，是否新增DSE模型误差/不可逆设计branch需具体对读，拟2+2+2=6标准完成。
- **2604.04759v1 / CIK State Poisoning**：[原文](https://arxiv.org/html/2604.04759v1) §3/4、AppendixA/D/E。OpenClaw四backbones/12手工impact每model88cases，Knowledge/Identity/Capability分别改memory/profile/executable；success仅attackrelevantaction且无confirmation，不等真实损失。Phase2部分用preloadedpoison独立测，不能与Phase1相乘偷算end-to-end；Skill主动加载能改善context-mediated但execpayload仍高，passive安装弱。仅一个platform、prompt级防御、无crossdimensionchain，原textalert不替代sandbox/signing。Ch72已有Skill描述vscode/activatedpath与derivedmemory不能授权，拟2+2+2=6安全深入完成，倾向已有覆盖，定点对读待同步。

GPUExecution-Idle新增Books提案唯一owner为PLATFORM-COST/Ch70“有效Utilization必须包含空闲分配”；Ch67只handoff遥测，不重复承载账目机制。待根任务独立判断及落笔。

- **2604.04783v1 / TIGER**：[PDF](https://arxiv.org/pdf/2604.04783v1) pp3–4/7–9、TableIV–VII。WoP-PBS三keyspace加numerical补精度、radix4 fixedpoint32/34bits；offlineschedule只保留requiredpartialproducts，inter/intrainput PBS合批再按profile192–320拆batch，较大batch反而cache/memory瓶颈。RTX6000Ada48GB/XeonGold5320/4TBDRAM对16threadCPU-WoP与保留其他优化的GPU-FBT。GELU/Softmax/LayerNorm7.17/16.68/17.05×是operator对CPU；所谓endtoend15.54×是单GPT2block估算985.66s且98.5%nonlinear，不是完整autoregressiveLLM实测。MultiGPU只是discussion未运行，block转换CKKS↔TFHE需计成本。拟2+2+2=6安全标准审阅完成；与AEGIS不同的exact LUT/nonlinear精度分支可支持已有Ch72“隐私不是开关”的受限实现，不把millisecondserving可用性写入Books。
- **2604.04522v1 / HDP审阅补全**：PDF§5–7明确v0.1issuer同key只能证明hop由issuer记录，不证明namedagent亲签；token pii移除会破坏rootsig，只能标audit-only。Same-session未过期stolen replay未被完全消除；标准化仅individualIETFsubmission非WG采纳，声称<2ms没有文中受控测试。对读Ch72“多跳Delegation必须保留HumanPrincipal”现正文已明确issuer-vs-delegate、scope、expiry/离线revocation取舍和semanticvalidation。拟2+2+2=6，安全深入完成，已有覆盖PLATFORM-SECURITY，而不是继续无界核protocolimplementation。
- **APPA实际写后复核**：Ch31本次修订正文准确改成广播rollout→冻结本地predictor+fewshot→rewardvectors→中央policyupdate，明确不等参数fedaverage或DP。与exact-v1§3.1/3.2/ Figure1一致。Books决定整合TRAIN-RLHF，写入PluralisticAggregation原段。Ch69Reviewnote519/20/7已根任务同步纠正，TraceGuard书稿一致性小批次完成。

- **GPU Execution-Idle实际写后复核**：Ch70“执行中闲置与Deep Idle不能合并核算”正文已准确区分驻留状态、活动、板级功率与池平均SM；packing/clock分支均保留尾延迟、cooldown和默认频率回退。缺失计数器不当零是平台采用规则，不是作者宣称已测全组件。正文未照搬省电比例，756GPU/31days、秒级、板级、回放与未建立SLO保证均明确。与exact-v1§2/4–5一致，Books决定整合PLATFORM-COST，源family marker实际存在。

### 反向查漏候选的必要证据（持续进行，非整日验收）

- **2604.04913v1 / DeltaTok**：[原文](https://arxiv.org/pdf/2604.04913v1) §3.2–3.4、4.1–4.4、Appendix A–D。冻结DINOv3 ViT-B feature、previous feature-conditioned tokenizer将变化压成一个连续delta token；预测器只在delta历史上运行，但decoder恢复空间feature仍依赖上一feature map，black-frame首token是绝对anchor。BoM取K噪声proposal中最近GT，仅best分支训练，不保证样本概率/覆盖真实distribution（Appendix D明确承认）；delta重建和predictor两类误差可跨步累积。4frame context，~0.2s单步/~0.6s三步，20samples分别报告best与先平均feature的mean，不能只用oracle-best证明可靠预测。4Mvideo、512²/300Kiter主结果和256²/100K消融不同；DINO-world原代码/数据未公开所以为自行复现，跨architecture附录保留VSPW下降0.2。TableB predictor GFLOPs不含共享backbone/encoder及每样本decoder，不能把全系统缩成one-token成本。Hardware/precision/concurrency/SLO未披露。非action-conditioned、非physical safety。拟2+2+3=7深入完成；Ch25一般latent dynamics缺少delta-history与reconstruction-anchor分权及BoM概率边界，待根任务具体正文裁决。
- **2604.04921v1 / TriAttention**：[原文](https://arxiv.org/html/2604.04921v1) §3–5、Appendix A/E。Pre-RoPE Q-center及按频率query norm离线统计，trigonometric future-offset score与低concentration norm complement，周期128decoded tokens驱动prune；不同架构/calibration/revision不能直接共用统计。四reasoning模型，A10080 BF16/FA2，GPT-OSS使用H100/FA3；max32768、temperature.6/topP.95、AIME8samples/MATH500一次，defaultKV2048而DS-Llama/MATH500512。Table4 Qwen3-8B同AIME25 40.8%时2.5×吞吐绑定3072budget，不外推服务并发/SLO；depth18+recursive benchmark开始低于FullKV。Coding→reasoning校准是一个迁移对照，不证明任意域内在不变；dedicatedkernel未实现。拟2+2+2=6标准完成。Ch45“Pre-RoPE Calibration与Workload-semantic Selection是两条正交路线”已实际承载distance-sensitive/norm/calibrationrevision/updatecadence/pagedmapping边界，倾向已有覆盖INFER-KV-CACHE，不重复新写相同分支。
- **2604.04894v1 / AsymGRPO**：[原文](https://arxiv.org/html/2604.04894v1) §2–4、Appendix C/E、Limitations。二值reward组准确率p分别调正负advantage `(1−p)/p` 与反比的指数，β=.5恢复GRPO、0为常数基线；βpos=.9/βneg=.4人为固定，不是学到逐token真值。理论省略完整PPOclip语义，positive/negative-only与反向曲线消融支持作者数学设置中的方向性，不证明任意reward都应同处理。4H100/verl/Qwen2.5-Math1.5B与Qwen3-4B nonthinking/MATH7500、G8；Qwen3global128/minibatch64/max4096/lr2e−6。主结果MATH500选择最佳checkpoint，Avg5/Avg10和temperature.4不同于曲线greedy，59.36vs56.50不是多seed误差界。Ch33已有token entropy-flow onpolicy条件，但本例组成功率对正/负轨迹的非对称modulation须与该正文具体对读；拟2+1+2=5标准完成，不能只借“熵”重复整合。
- **2604.03257v1 / Judge噪声CMLE**：[原文](https://arxiv.org/html/2604.03257v1) §3–5、约束实现说明。少量人工gold与大量noisy judge标签联合估计failure rate、TPR/FPR；CMLE用先验区间换低方差但区间误指定有bias风险，UMLE不要求这些anchor。实测Jigsaw nM50/nJ10000、Qwen2.5-.5classifier/Llama3.1-8judge，transfer仅同model in-domain HateSpeech锚点.948/.063与目标.939/.053；全数据reference约束不是实际零成本oracle，未测任意域外安全。Projected gradient固定200steps/lr1e−6与启动labelbudget需计入。拟2+2+2=6标准完成；Ch66 judge校准已承认gold anchor与分布漂移，CMLE区间借方差与偏差的具体分支待实际owner对读，不声称无偏普适保证。
- **2604.03677v1 / Full-sequence masking**：[原文](https://arxiv.org/html/2604.03677v1) §2–5。SFT只maskresponse会训练出prompt不宜被反向infilling的条件偏差；fullsequence随机mask prompt+response、全maskedtokenloss，后接response-only细化为条件分支。Fewshot已知response反推prompt，多候选用fewshot验收后固定复用，不是test逐题用gold泄漏。LLaDA/Dream、SummEval/GSM8K；本文§3.3叙述64.8而Table1 publicLLaDA prepend69.8且不同case含义不能合并；FS+RO不同template/receiver未全面更优，§4.2叙述数值与表亦有不一致，不照录宣传。Bidirectional结构不能独立保证SFT后可用能力。拟2+1+3=6标准完成；潜在TRAIN-SFT知识增量是mask support决定可执行generation direction，待Books具体比较。
- **2604.03754v1 / Truth direction边界**：[原文](https://arxiv.org/html/2604.03754v1) §3–6、B.5/C。Layer-wise linearprobe同任务高AUROC不代表跨task/prompt；早层affirmative→negated可反向，polarity方向非truth，arithmetic晚层、复杂counting纠缠。Ask-correct改变方向/出现层，一部分跨任务改善但F3–F5仍失败；长度control与多model附录只支持受测语言/任务，不能升级通用truthsensor或授权决策。拟2+1+3=6标准完成；Ch66“Self-report、Behavior Probe与Deployment Outcome”/“Activation Oracle Confidence也要校准”已有probe条件性，需对读是否新增task×layer×prompt交互，不按AUROC当真值。
- **2604.03764v1 / AP-MAE**：[原文](https://arxiv.org/html/2604.03764v1) §3–6、§8。固定256length attention矩阵lognormalized后ViTmaskedautoencoder、DBSCANpattern聚类，SC2 3/7/15B跨模型reconstructionloss可比不等因果电路；归一化前后loss不可直接比。后续intervention聚焦code结构，较强注入会collapse；限任务/模型/长度，attentionpattern矩阵同shape也不证明可迁移语义/输出正确。拟2+1+2=5标准审阅，必要干预§6尚待定点补读，不伪称已经核全部因果结果。
- **2604.03922v1 / ACES**：[原文](https://arxiv.org/html/2604.03922v1) §2–4、Assumption4。Code×generated-test passmatrix的LOO-AUC避免一条test给自己的排序打分；余下testaggregate仍须better-thanrandom才保持informativeness符号。Closedform保证不是无标签识别truth通用定理，optimizedjointweight仅实证改善。GPT3.5Turbo同pool约200code×500test，HumanEval164/+164/MBPP427；hard区无method超过1/14，MBPPPass5仍低directinference，oracleassumption分析用真实labels而生产不可知。Hardcases需额外静态/规范真值，不以consensus授权代码。拟2+2+2=6标准完成；Ch66 testoracle/ correlatedevidence原则已有，是否需要LOOtest-ranking分支由根裁决。
- **2604.04385v1 / Trigger vs carrier**：[原文](https://arxiv.org/html/2604.04385v1) §3–6。跨2–32B九model/六labs n120 matchedprompts，DLA输出低不等上游gate无因果；interchange/knockoutcascade/nullheads拆trigger与amplifier。Qwen scaling necessity1.1→3.2而ablation弱，跨世代tophead不稳定；3judge2400outputs、语言对照仅n16、safety/politicalrouting限定，MLP未feature分解、onecipherencoding不证明全部alignment。拟2+1+3=6标准完成；Ch14“可解码不等于单点拥有因果控制权”可能已有覆盖，需要对读actualbody，不把政治内容作领域扩池。
- **2604.04418v1 / Error Verifiability**：[原文](https://arxiv.org/html/2604.04418v1) §3–8、Limitations、Appendix K。AnswerOnly基线×答案正确性形成TP/TN/FP/FN四cell，Answer+Justification正确核验率均匀聚合，避免90%correct分布下blindaccept伪高。AO-CoT/directAJ两个protocol经有限math人类样本κ.481/.501选定，仍不是完整人类等价。Tulu3.1/OLMo2后训练与跨modelaccuracy不保证errorverifiability，数学反省rephrase在factualQA不迁移；固定finalanswer只改justification，不可把说服度当truth。拟2+2+3=7深入完成；Ch66 claim/credibility机制已多但四cellbaselineconditioning为可明确新增的评价合同，待根actualbody审定。
- **2604.03809v1 / DALC**：[原文](https://arxiv.org/html/2604.03809v1) §2–3、§6。三角色同Qwen2.5模型，128tokenrationale/temperature.7，nomic768维sentenceembedding；GramSchmidt强制cos0/rank3却14BGSM8K83<raw87，SVD几乎不改高相关。第一agent保留导致orderbias；3×300charhint、两encoder诊断会改变优势，n100/1–5points处于1–3runvariance内，未做全factorial，不证明embedding正交=独立reasoning。拟2+1+2=5标准完成，Ch82若已明确多角色与同源错误/独立证据，判已有覆盖而非新增几何投票recipe。
- **2604.04043v1 / Semantic Contamination**：[PDF](https://arxiv.org/pdf/2604.04043v1) pp1–5。HTMLv1封面August24与PDFv1April7不符，采用PDF精确v1。三Claude snapshot、temperature.5、10primingconditions×100trials，随机五数字order后dinnerparty20figures；customregex+手工semantic类别的darkhits，不是广义harm or jailbreakrate。Nonsenseformatcontrol支持内容/格式两因素可能，但smallmodel缺representation和capabilitygated仅作者推测，无内部probe/模型同预算因果对照；Opus比Sonnet幅度弱，不能写能力越强必更不安全。拟2+1+2=5，安全深入完成；Ch72/74已有untrustedexample污染与authority边界，倾向仅报告受限现象或已有覆盖，不采用普遍scaling结论。
- **2604.04131v1 / Profile–Then–Reason**：[原文](https://arxiv.org/html/2604.04131v1) §2.2、Proposition2.2、§3。LLM先profile有限workflow、deterministicroute/execution/verifier，最多一次repair，再末端reason；“确定性”明示每operator deterministic前提，不证明semanticplan正确。四backbones×六benchmark共24pair，PTR16胜，但HotpotQA四model均输react，高observationdependence仍react；meanlatency/APIprice不构成tailSLO，需冻结providerrevision。拟2+2+2=6标准完成；Ch81typedworkflow/repair与动态planning回退可能已完整承载，不因formalnotation强写新架构。
- **2604.04347v1 / RoboPhD**：[原文](https://arxiv.org/html/2604.04347v1) §3–4。同1500evaluations四任务比较evolution+ASI，threeagents×20sameexamplespairwiseElo与DeepFocus；KotH不是只去掉Elo（session/ASI结构保留，Autoresearch单continuoussession不同），GEPA3example/API而Robo20/ClaudeCode，工具权限与sampling预算混杂。ARC/SQL/financialQA/cloudscheduling四任务支持受限优化recipe，不证明整个auto-research架构优越；paper自承KotH竞争接近。拟2+1+2=5标准审阅，Table2/关键消融结果尚待补读，不能只因“首个比较”采用。
- **2604.04373v1 / Experience Decoction**：[原文](https://arxiv.org/html/2604.04373v1) §2.1–2.2与后续ablation。Flatmemory每题一个successfultrajectory、Qwen3Embedding4BtopK，SeedOSS36B/GPTOSS20B，math/WebShop/SWE；avg_m质量与生成tokens或交互steps分别测，不把shortertrajectory当wallclock。单纯换organization不足，decoctedexperience保留可复用策略仍受writerbias/失败missing影响。细分recipe与负面对照尚待补读，普通待办不是外部受阻。
- **2604.04853v1 / MemMachine — 前分母改判关闭**：[原文](https://arxiv.org/html/2604.04853v1) §4–5.6已定点核准入。Rawepisode/profile、sentenceembedding→邻turncontext→rerank、LLM直接/chain/fanout路由、最多3rewrite是成熟组合；“embedding不能任何singlequery解dependency”无一般证明，confidence≥.8未概率校准。Table3含LoCoMo/EpBench退步，poolnoise改变索引分布而非新statecontrol。题摘原以“latebinding”准入，方法补读后未发现超出Ch76 queryplanning/Ch77 provenance与derivedprofile的长期新命题；具体改判理由保留，不为降低工作量或Books已有而删证据。此项不进入最终候选、不给最终V2评分，旧名/先前队列保留供审计。

### 必要证据收束（继续处理，不是日级完成）

- **2604.03764v1 / AP-MAE 补审**：§7.1–7.2明确按各任务CatBoost SHAP选正/负/中性heads，置零并以随机同数量heads对照，记录原正确变错与原错变对的净差；少量干预改善、再增加会令所有原正确样本变错，任务间阈值和方差大。作者将此解释为竞争/次级circuits，但明示尚需研究；§8仅Java、256length、pattern发现不提供完整机制解释。因此2+1+2=5标准完成，解释边界而非部署优化建议；需对读Ch14因果控制权正文后最终Books判断。此前§6的待补读定位应修正为§7干预。
- **2604.04347v1 / RoboPhD 补审**：§4.2–4.3/Table2–4实读。四任务1500evaluation预算，ARC/SQL/FinQA的solver/API限额不相同，KotH在ARC65.8→67.0胜，Autoresearch在无LLM的cloudscheduling胜；RoboPhD与KotH接近不是统计支配。将validation200减100增加探索在八配对均改善，但未证明validation应永远为0；DeepFocus四任务改善仍缺多seed可靠差值，底层工具/sampling批量不齐。2+1+2=5标准完成，受限比较仅报告，不把“首次”或代码行数当新长期架构。
- **2604.03890v1 / Structured robotic backdoors**：[原文](https://arxiv.org/html/2604.03890v1) III-A–D/IV-A–D。ROS2 JSON→cmd_vel的执行桥，poisoned LoRA把触发词绑定最终结构化命令，区别仅污染自然语言reasoning且后续JSON转换未传播。四7–9B受害模型、Llama3-8B verifier，Turtlesim与Yahboom实车；平均ASR约83%→20%但不是零，DeepSeek微调后latency波动被排除，不能把剩下稳定模型延迟称全模型结果。GPU/precision/seed及逐模型样本量未见完整披露。安全深入完成2+2+2=6；长期命题是输出schema正确不代表命令授权、verifier增加反馈延迟且不能提供硬安全，需与Ch26/72已承载边界对读，不能把一种ROS部署推广全部VLA。
- **2604.04847v1 / Speech Tool Benchmark**：[原文](https://arxiv.org/html/2604.04847v1) §3–4/Limitations。100人类utterances/12speakers含非母语、21self-correction与30s静默环境声；四mockAPI域且本地工具零latency、六LiveKit pipeline。toolF1、argument judge、allrequiredtask与turnlatency分开；跨cloud region/network仍混入“model latency”，不能作厂商模型纯因果排行。2+2+2=6标准审阅；拟Ch66已有duplex与tool/effect评价覆盖，需完成结果与actualbody对照。
- **2604.04855v1 / Reset理论**：[原文](https://arxiv.org/html/2604.04855v1) 核心构造和保证。无reset时隐藏fragile path只凭root rollout遇到稀有reachable state；local reset可逐prefix验证，改变探索sample complexity。有限状态、可重置、可观测/判定success的oracle条件不能移成任意真实Agent环境可回滚。2+2+2=6，理论假设及正文对应尚需定点收束，不以缺benchmark判无价值。
- **2604.04872v1 / SandMLE**：[PDF](https://arxiv.org/pdf/2604.04872v1) Method/evaluation。60seed task→848synthetic/64validation，生成小数据的hiddenrule/spec/evaluator并执行sanitycheck，不是把原benchmark缩小；format/execution/median/medals复合reward及GRPO80step。Qwen3-8/14/30B，MLElite22easy与MLEDojo62heldout，测试24GPUhour/turn30；短history溢出loop是失败边界。196.17→14.31s为训练synthetic相对seed执行成本，不是同测试工作负载端到端加速。2+2+2=6标准完成；Ch81“合成环境先生成契约再生成反馈”实际已有build/repair与verifierbias的完整分工，已有覆盖AGENT-WORKFLOW，不重复写新环境容器。
- **2604.04253v1 / Near-memory processor**：[原文](https://arxiv.org/html/2604.04253v1) §4–6。3Dlogicdie重新分配compute/buffer，7nmFP16模型以800MHz与fixed1GHz比较，必须考虑成本归一化而非把sim当芯片实测；GPU比较亦模型。2+2+2=6标准审阅，仍需§6.6关键代价定点核验。
- **2604.04451v1 / Chorus**：[原文](https://arxiv.org/html/2604.04451v1) Method/评测。相同/近邻prompt用CLIP语义早期full/middle regional/late none跨请求cache，TGAA编辑局部latent；Wan1.3/14B四步与50step、4H20/A100。VidProM50k中选一个cluster2000、warm/arrival半分及cachehit150，受限非全真实arrival分布。CLIP31.758→30.798质量下降不能叫无损；理想1.45ratio实测1.23。2+2+2=6标准完成，待Ch45缓存identity/quality与Ch24多步代价的actualbody比较，非普遍KV复用。
- **2604.03242v1 / DRAFT**：[原文](https://arxiv.org/html/2604.03242v1) 核心Method/消融。Extractor LoRA输出compact latent加原始trajectory给Reasoner，而非显式摘要彻底替代原轨迹；跨模型用projection，16尾token相对头部/更多token有对照。四backbones与长trajectory稀疏安全证据任务受限，latent并非忠实可读解释；需要读取实际评价结果后定稿。拟2+2+2=6。
- **2604.03244v1 / OpenEval**：[原文](https://arxiv.org/html/2604.03244v1) Method/数据合同。10Mitemresponses/155Kitems，MMLU旧56K与MMLUPro新10K分开；CTTdifficulty/discrimination、SVD/GLRM揭示task簇，不把benchmark总分当单一能力。需收束§5实际发现而非仅采“应发布细粒度数据”立场，拟2+2+2=6。
- **2604.03253v1 / Self-execution**：[原文](https://arxiv.org/html/2604.03253v1) Method/评测。联合prediction+code SFT/RL，最佳K候选先由self-prediction验publictests再一次fix；12.2KCodeContests→143K正确solution，privatehiddenLCB287/DMC282/CruxEval，输出reward权重.8。公私测试和oracle预测误差必须分开；拟2+2+2=6，实际反证待定点核。
- **2604.03316v1 / Visual sink**：[原文](https://arxiv.org/html/2604.03316v1) Method/消融。冻结backbone用4096→64→2MLP识别视觉sink，two-groupkeyscale不等mask；10Ktraining/2epoch、300GQA LLaVA/OneVision不同visionencoder。Oracle11scale/任务不是可部署选择，singlelayer有负任务、greedy多层非普遍提升。拟2+1+2=5，需收束关键eval而不是推断所有sink有害。
- **2604.03340v1 / AC-LAM**：[原文](https://arxiv.org/html/2604.03340v1) Method。Latent inverse/cycle与scene-wise actionadditivity、FDM+frozenEMA避免collapse，短同scene范围内局部近似而非全局可交换动作，旋转反例不能消失。拟2+2+2=6，尚需受控实验§4结果。
- **2604.03472v1 / Vocab Dropout**：[原文](https://arxiv.org/html/2604.03472v1) Method/消融。RZero proposer/solver交替GRPO、batchBernoulli硬mask非format词，改变可行词表而非entropy bonus；训练/推理mismatch8→4会伤1.4，instruct混合不是全胜。拟2+1+2=5，需实际§5.1设置与关键α边界后结案。
- **2604.03515v1 / Coding Scaffold**：[原文](https://arxiv.org/html/2604.03515v1) 分类/方法与限制。13publicrepos中22scaffolds由单analyst按9→12维归类，registeredtools不等实际capabilities、topology不等loopdriver。没有受控架构效应，SWE分数含模型/API混杂；2+1+2=5标准完成，仅报告受限实现分类，不能把taxonomy当采用某架构的依据。
- **2604.03266v1 / Emergent communication**：[原文](https://arxiv.org/html/2604.03266v1) 方法/实验。冻结DINOv2/VJEPA2、2×5符号Gumbelmessage，80seed中54%按后验PosDis>.4分为compositional；这不是预注册普遍概率。最好code93.8/新训练92.2/holistic87.5含选择效应，CIFAR未见27%vschance20/rawNN50、真实Physics101/CoPhy外推条件不同。通信重组冻结feature，不证明新perception或普遍causal representation。2+1+2=5标准完成，仅报告受限世界模型机制例证，尚不足改长期设计。
- **2604.03556v1 / Visual focus**：[原文](https://arxiv.org/html/2604.03556v1) 方法。Diffuse→focus→rediffuse三阶段随encoder/CLSvsavg估计变化，focus局部mask可降CHAIR但不是attention相关性自动成为因果truth；oracleTopK与DPP部署区分。拟2+1+2=5，关键评测/干预尚需补读。
- **2604.03571v1 / FRUL**：[原文](https://arxiv.org/html/2604.03571v1) Method/评测。多LLM定位敏感CoT→benign替代→feature replacement加retaingradient，TOFU4K虚构人物与19.7K真实biomedicalprivacy任务，不恢复AIforScience科学发现。Llama3.2-1B/NemotronNano8B，低ROUGE不证明参数擦除及所有multihop攻击成功防御。2+2+2=6安全采用需要deep，ablation/recovery仍待定点核。
- **2604.04207v1 / Visual entropy**：[原文](https://arxiv.org/html/2604.04207v1) Method/评测。900items分层人工bbox、2700modelruns，Qwen3VL2/8Thinking、GLM4.6VFlash，100heldoutVisualCoT为architecture-specific layercalibration。Top20normalizedentropy不等全分布、fulltrace9cells失败，cumulativegrounding与任务类型有关；因果未证明。2+1+2=5标准审阅，需最后风险边界对读。
- **2604.04356v1 / REAM**：[原文](https://arxiv.org/html/2604.04356v1) Method/消融。Router-weightedactivation expertmerging相对丢弃保持参数信息，但calibrationmix决定MC/GEN前沿；512→384experts与code-heavy/AIME提升只属Qwen3CoderNext受测条件。移去sequentialmerge GEN72.9→69.0、稀有expert域外重要性不能由平均activation否定。2+2+2=6标准审阅，methodhead为空尚须定位正文段落，不伪称代码已验证。
- **2604.04461v1 / DP-OPD**：[原文](https://arxiv.org/html/2604.04461v1) §3–4。PublicGPT2Large774M teacher/DistilGPT82M student，私有prompt的onpolicy mixtureλ.5与teacherforcedstates、β.5GKD、perexampleDP-SGDclip1/ε2/δ1Naccountant。TeacherAPI看到私有prompt仍在studentrelease DP外，不能声称整链路private。Yelp1.9M/BigPatent200K128seq，部分baseline是此前发表数而非同budgetrerun；5vs40epoch差异明确。2+2+2=6，必要privacy假设定点收束后安全deep，拟Ch72既有DP权重发布与私有推理分权已有覆盖。
- **2604.04580v1 / Code–test co-evolution**：[原文](https://arxiv.org/html/2604.04580v1) §2.3.1–5。同时进化code/test，交叉执行passmatrix和consensusfitness、semanticcrossover+elite保证的是内部fitness非spec正确，Docker/ASTfaultlocalization限制搜索范围。测试生成仍会与patch共谋，simplebugs成本可更差；拟2+2+2=6，关键实验待收束。
- **2604.04648v1 / Caution**：[原文](https://arxiv.org/html/2604.04648v1) §2–3、AppendixC。冻结RMfeature作为target而非随机RNDtarget，典型baseoutput上训练predictor，predictionerror惩罚BoN的OOD候选。理论线性reward与适当网络/假设只是proof-of-concept，不是任意RM的概率校准；GSMtrain→MATH/BBH外域，pessimism-only可胜RM+penalty、3bootstrap不是3独立training。2+2+2=6标准完成，需Ch56selectingrisk具体已有body对照。
- **2604.04767v1 / CogDRIFT**：[原文](https://arxiv.org/html/2604.04767v1) Method/Table1。Pass64=0的8.9K仍含unsolvable，GPT5.4三samplemajority与gold一致筛出958，不能沿摘要说完全nostrongteacher。MC4→MC10→cloze→open改变提示特权与词表，τ.5逐题promotion，pass64零不证明零成功概率/凭空新knowledge。Qwen3-4B2507/Llama3.2-3、六bench中AIME25 Qwen41.71→40.28退步。2+1+2=5标准完成；Ch33adaptivecurriculum已有，局部支持集变化若需采用须深审具体分支，不从挑选效应推广泛突破。

### 上述待办的定点收束与已有正文比较

- **03316 Visual sink**：§4–5.3/Table1–2已补。Learnedgate并无oracletasklabels，32layers独立训练，greedystacking后的收益小于各层之和，前序gate改变后序输入分布；增加L19会降、再增L6改善，不能写可独立相加。2+1+2=5标准完成，受限局部门控例证仅报告，未建立超出Ch23 encoder/fusion与Ch14 attention诊断的长期新采用规则。
- **03340 AC-LAM**：§4.1–4.4及A.2已補读Implementation/PolicySetup/Results/DesignFactors/Findings。过滤较大robotrotation以使same-scene短时间加法近似合理；共同Villa-X/PaliGemma3B/15Ksteps/batch512、50%ID+50%Bridge，不是大模型全局actiongroup定律。PreVQ运动量校准较好而additivity较弱，IDM无stopgrad崩溃/错误位置explode，FDM更稳；新loss收益有simulation与realrobot对照但不证明所有motion闭环。2+2+2=6标准完成，是否在Ch26补局部compositional representation分支由具体正文差异裁决。
- **03472 Vocab Dropout**：§5.1/6.1/Ablations/B.3已补。2H200/verl/vLLM、baseQwen3-4/8B、五iteration、三seed；85%/75%词表retain不能反写成drop率。最终checkpoint固定避免bestposthoc；4B75%多样性上升却solver36.5<38.3、85%39.3改善，capacitymatched8B收益较好，crossscale和instruct失效。Mask是allowed_token_ids可行域约束，不是单纯entropyreward。2+1+2=5标准完成；Ch33已有“探索增加不保证可学课程”的主线，对读硬mask新分支是否值得采用。
- **04373 Experience Decoction**：HTML v1可读文本缺PDF v1的§3–5主体、把§3置为Concluding Remarks，故收束机制/关键反证采用[PDF v1](https://arxiv.org/pdf/2604.04373v1) pp4–8、HTML AppendixC.2仅辅佐实现。Flat→lesson→kmeans代表entry与concepttree，数学rawtrajectory稍好、WebShop/SWElesson更好；中间memory规模sweetspot而retrievalrelevance随总量单调，二者不能等同。Entropy→length上界依赖统一h>0熵率下界，r=.91并不证明truthquality、因果或上界tight；qualityproxy相关仅r=.2518，不能作通用confidence。经验只保留有至少一正反馈的问题，有survivorshipbias，未计总训练/整合成本。2+2+2=6标准完成；Ch77“从原始轨迹到派生策略”与“late construction”已承载原轨迹/派生lesson、噪声、不同任务与provenance/失效/回读，拟已有覆盖AGENT-MEMORY，不采用作者“低熵即好”的普适解释。
- **04253 Near-memory processor**：§6.1.3/6.6已补。FP16/7nmASAP7、netlist+simulation能量与ScaleSim/Ramulator/lookupreplay；8device TP=8且共同H100prefill，MoE仍TP避免与EP变化混淆。固定4096PE时square化减filterbuffer却增activationbuffer，dense和MoE形状偏好不同；非制造芯片或生产SLO。2+2+2=6标准完成，硬件execution-plan可作为受限DSE例证，待Ch49已有shape/memory联合约束对照。
- **04847 Speech Tool Benchmark**：§4–5/Limitations已补。固定六endpoints同audio/localzeroAPI，argument与response采用GPT4o、taskpass要求全部tool/arguments。Filler/firstword/firstcall/factualcompletion四时刻分开，Gemini3.1快但22/100无响应；作者把cloudnetwork和region混杂保留，因此不能从均延迟估生产SLO或state rollback能力原因。2+2+2=6标准完成；Ch66“Duplex Agent Evaluation要联合测Timing与Content”及三态合同已有端点、输入流、interrupt、content/latency条件，已有覆盖PLATFORM-EVALUATION-SYSTEM，仅排行/延迟范围留日报。
- **03764 AP-MAE / 04385 Trigger–Carrier**：已实际对读Ch14“可解码不等于单点拥有因果控制权”的probe→single/multiposition→causaltracing/端到端回退。前者5、后者6标准完成，各自pattern/knockout是受限诊断证据，既有正文已覆盖读出/必要/充分/多点控制的层级，不为新任务复制一套因果owner。两项已有覆盖MODEL-SELF-ATTENTION。
- **03754 Truth-direction**：已对读Ch66“可解码Failure Direction不拥有自动纠错权”和activationoracle/taskcalibration段；probe含预测信息不代表干预解耦、需targetmodel/task×prompt×layer/slice校准和行为回归，本例不提供独立部署truthauthority。2+1+3=6标准完成，已有覆盖PLATFORM-EVALUATION-SYSTEM。
- **03809 DALC**：已对读Ch82“Verification与Aggregation”“同根报告可以帮助读懂证据，却不能按独立观察累加”。Embedding正交未消同root误差，n100小差/一到三run不足新几何置信保证。2+1+2=5标准完成，已有覆盖AGENT-MULTI-AGENT。
- **03556 Visual focus**：§5Models/Baselines/DPPconfiguration/Quantitative/InferenceEfficiency与D.4已补。Architecture-specific mask60/35/65/40%，greedyencoderfocusintervention可降CHAIR但Qwen/InternVL POPE及F1部分下降；平均attention不是truth，选取DPP/硬mask保CLS。相对PGD AUE开销减少但GPU/并发/SLO未披露，不沿“negligible”写无成本。2+1+2=5标准完成，仅报告受限hallucination operatingpoint与互补decoder方法，不推广所有visualtokens或越过事实验证。
- **04356 REAM**：§4实际子段aggregatedsimilarity/pseudopruning/permutation/sequential及§5Setup/Ablation已补。按gateweightedactivation+weight共同Hungarianalignment，保护centroids再吸收低saliency、很多singleton；前层合并后重算后层calibration避免stalestats，1→1.5hour为Qwen30B作者一次性实测成本。10mixture无finetune并有MC/GEN前沿、remove各部件对照；routerfrequency不同importance，OOD稀有expert与calibration失配受限。2+2+2=6标准完成，拟Ch21仅目前需补“artifact压缩不同于runtime route裁剪”实际owner差异，非全模型最佳压缩。
- **04461 DP-OPD**：§3.4及WhatConsumesPrivacy/Algorithm1/§4.3/4.9已补，冻结teacher只作为每example内部loss，DP会计保护唯一releasedstudent；publicteacher/rollout查询若外泄私有prompt不受studentDP保证，controlcodes敏感性亦未解决。Onpolicy交互以现teacher固定与每步DPcompatibleclip/noise为前提，不推出任意APIpipeline guarantee。2+2+2=6安全深入完成；需对读Ch72实际DP发布/私有推理正文后给已有覆盖或窄补。

### 最后一批关键反证与理论对象纠正

- **03571 FRUL**：§4.2和消融已补。TOFU4K与19.7K医学隐私样本、Llama3.2-1B/Nemotron8B；reasoning与finalanswer分别对重训模型计算ROUGE差距，不能由低ROUGE推断知识已经从参数擦除。3%forget子集CoT替代可缩小重训差距，遗忘gradient过强则retain效用下降，retain-gradient缓解；未证明对抗恢复、所有推理路径或可组合隐私保证。2+2+2=6安全深入完成。采用范围仅输出行为与retain/forget双轴，不把作者“低分说明不知道”写入Books。
- **03253 Self-execution**：§6.2–6.4/Table3–6与§8已补。普通Qwen3-32B/CWM仅在推理时套self-RLEF scaffold，多项pass指标下降；联合训练后的改善不能归因于多轮模板本身。DMC公测初错修对17.0%、初对改错1.2%，私测分别10.4%/5.0%，模拟执行的可见测试与隐测正确性并不相同。Oracle real execution仍较强；大整数/复杂运算和单文件竞赛题边界，不证明repository执行等价。2+2+2=6标准完成，需把learned simulator限定为有误差的反馈sensor，不获得真实执行oracle的权威。
- **04207 Visual entropy**：§5.4–5.5/§6及AppendixH.2已补。三模型×三数据集、18方向迁移，视觉engagement与长度耦合但非相同信号；加入视觉特征部分迁移明显下降，不能把九格attention衰减转成普遍hallucination因果。底5%vision veto后重新放宽entropy阈值以恢复coverage，不能把拒绝更多当同coverage收益。任务需要持续视觉参照时才可能增益，任务识别在部署前尚待解决；2B–8B/300items每域、attention相关性与小角落样本限制。2+1+2=5标准完成，拟已有Ch66条件化监测/校准承载，而非全局视觉熵阈值。
- **04580 Code–test co-evolution**：§3.2–3.3/§4.1–4.3/§5.2及limitations已补。DeepSeek-V3-0324、population10/最多5代，SWE-benchLite300/SWT276，隐藏测试/goldenpatch是评价oracle而非搜索时可用真值；多数baseline是旧论文/leaderboard，不是同prompt/预算重跑。去TestAgent在三代39.33→33.33，有受限component证据，但跨模型主表不证明算法普遍优越；每实例成本1.11美元与其他模型成本不能合为机制因果。共进化的consensus/elite只保内部fitness，不能防code/test同错；简单bugs可增加成本。2+2+2=6标准完成，需与Ch81 actualbody的implementation/checker分权对读。
- **04855 Generator Access**：§2.1–2.2/§3及Theorem3–4已补，纠正前段“环境reset”的过宽叙述：对象是固定prompt、有限词表与有限horizon的autoregressive prefix tree。No-reset回复可含已访问prefix的全部logits，仍受未到达稀有prefix的可达性屏障；chosen-prefix只沿已构造节点逐token延伸即可改变查询复杂度。隐藏路径分布以固定概率gap区分正确child，结论依赖条件采样oracle与构造族，非任意真实环境回滚；top1在另一分支构造中又可丢失识别所需信息。未把math-stripped抽取中的空公式当精确复杂度证明，报告只采用原文定理有明确条件支持的质性区别。2+2+2=6，理论标准完成；拟Ch33区分prefix control与prefix observation，采用前根任务独立原公式复核。

- **03244 OpenEval定稿证据**：[PDF v1](https://arxiv.org/pdf/2604.03244v1) pp4–7/§5.1–5.2/§6与HTML定点交叉。旧10M/155K库存字段不用；PDF v1§6为225Kitems、64bench、8Mresponses，与HTML相同，不能把这项误称为HTML污染。66旧模型×567MMLU items与72新模型×1000Pro items的CTT difficulty依赖被测模型样本，不能跨组直接比较；BabiQA三个factor簇由answer-key解释，提示测到了作答偏好而非单一deduction。GLRM的MMLU-Pro四因子由GPT5初标再人工修订，外部相关仅描述性、非定论或因果能力本体。2+2+2=6标准完成，待根任务裁决Ch66 item-occurrence identity/内部构念诊断是否尚缺，不以公开数据量自动写Books。
- **03922 ACES补审**：§4.2–4.3及Assumption4再次核原文。仅passmatrix主表HumanEval收益不能略过MBPPPass5仍低directinference；Hard区全部方法≤1/14，average-test质量假设在真实部署未知，不能用LOO消除所有相关错误。标准完成2+2+2=6；独立testing truth与ranking owner需分离。LOO-AUC的具体估计分支是否对Ch66现有testoracle/consensus增加长期命题交根任务裁决。
- **本批已有覆盖实际正文**：03571→Ch72“Unlearning必须分开参数擦除与推理拒答”已管理恢复性/retain utility/有限probe非删除证明；04461→Ch72“DP先定义被保护对象”已分model-release/public outputs与private inference、明确adjacency/clip/accountant及不替代access control；04759→Ch72“Agent自己的Instruction/Config/Memory也是受保护资产”及“Harness Backdoor”已管理跨run activation与write-lineage、不凭Agent自解释升级policy；04750/04253→Ch49“ChipletPool与ExecutionPlan必须联合演化”和“按算子数据移动placement”已管理jointDSE、model误差、模拟非silicon与保守runtime回退；03676→Ch76“Reranking与ContextPacking”“Query Robustness”“Logical/Physical Plan”实际body已分relevance/coverage/成本、扩写风险和backendprofile。各项均为当前具体命题已有覆盖，不是根据论文名称或Review note判定。
- **本批非候选规模核验**：73暂存家族逐项打开官方`abs/<ID>v1`做精确标题与可见撤回标记检查，73个响应均取得citation_title，未出现“This paper has been withdrawn”。这是所查官方版本页的轻量核验，不声称所有勘误/版本史均已查完。PRAISE、Full-Duplex-Bench-v3等标题绑定当前v1，旧摘要/后发title不作为证明。

- **03242 DRAFT定稿证据**：§4.1–4.2/§5/Limitations/E.4已补。QwenGuard4B/Qwen4/8B/Llama3.1-8B四backbones，对vanilla/SFT-LoRA/AgentAuditor比较；ExplicitReasoning用GPT5.2显式摘要后judge，模型/成本不齐，不能把其差值单归latent本身。AuraGen完全synthetic，ASSE/RJudge含LLM+human标签；avg-seeds/stdev声称未见seed数量完整披露。Extractor仍联合原trajectory，16尾tokens较合适，去任一模块下降；tSNE可分不能证明attention稀释是因果。漏检跨步骤hijack/destination/不可逆writes，误检正常security词；没有验证实际权限、ratelimit、多租户或层级控制。2+2+2=6安全深入完成，只作为监测证据，latent并非可读忠实解释，等待根任务Ch66 sensor正文必要性裁决。

- **2604.03588v1 / Rashomon Memory**：[exact-v1](https://arxiv.org/html/2604.03588v1) §2–4/ObservationsAndLimitations。各观点拥有OWL/RDF子图，query-dependent Dung attack graph允许selection/composition/conflict surfacing，不能强迫把无法消解观点当统一真值。ClaudeSonnet4.6 temperature0、三perspectives/八observations/四queries，37次encoding calls/query最多7次；无RAG/raw-memory定量baseline，没有规模或interactive latency证明，attack质量依赖prompt且无法保证无全面相互攻击。2+1+2=5标准完成，仅报告受限proof-of-concept/多观点表示，不把这些四query提升为新的可靠memory采用契约。

### 恢复后的真实收束位置（不代替非作者验收）

本日README现已完整整理为V3六部分。854是宽召回的原始唯一身份；旧90项题摘和旧排除集42项定点题摘已经按贡献门槛复查。73项暂存家族各有精确版本的最低必要证据说明，但不因此计为73项独立证实的贡献。03616完成非作者采用后，当前Books为7项真实写入并写后核验、27项具体已有覆盖、11项仅报告、28项普通采用裁决待办，分母仍待非作者终审。

恢复后对读了Ch72的“Prompt Injection与Tool Boundary”“Instruction Hierarchy必须携带Authenticated Provenance”“Context Reconstruction不能提升Principal Authority”，将04043的已有覆盖限定为推理时上下文风险与独立effect授权；Claude快照/dark-hit/scaling猜想仅留日报。又对读Ch66“Pairwise Verdict需要Configuration Envelope”“Judge Agreement不是单一数字”，将04532的已有覆盖绑定judge语言/模板/scale/pooling，不归因于solver能力。这些实际正文比较已补入日报，不以Review note代替正文。

SRC-ARXIV扫描标已检查，候选/Books未终态仍在§1/5/6列明。8个外部历史子入口按具体入口隔离，并非8个候选缺全文，不可相互代替。03616完成非作者采用后，scoped validator仍有28项尚未获得Books合同终态；日期范围、评分Total、链接/标题结构未报错，scoped diff check通过。当前状态仍为进行中，不能为消除机器错误把普通待办改成“暂缓”。

### 最新非作者准入复核：分母未冻结

`apr01` 核对14来源/日期链，完整读当前73项题摘并按压缩、量化、kernel、学习反证、安全与领域/综述理由抽检28项排除题摘；不是全raw摘要或全文验收。854完整题摘库实际为 `../arxiv-owner-replay-20260903/20260407/arxiv-owner-receipt.json` 的 `identities[]`（03232～04934）；旧screening/status不构成当前V3证明。必须重开准入的13项为`03258 SoLA`组件贡献与低秩分配、`03414 KiToke`全视频冗余/时间合并、`03420 Quantization Vector`donor差分迁移及负迁移/oracle调幅边界、`03950 DMA`分区精度与融合执行、`04013 RUQuant`分布变换与中点偏差、`04701 MUXQ`辅助矩阵/outlier、`04722 Adaptive KV`位宽controller、`03263 LPC-SM`局部注意力/slow memory/novelty写入、`03446 MMEE`跨算子dataflow搜索、`03674 DiffSparse`逐层稀疏/DP/训练分支、`04281 Width Growth`warm-start随机性反证、`04743 Hallucination Basins`任务间latent诊断、`04863 Token Grounding`局部grounding与分散弱相关。另`04238 Compiler–LLM Cooperation`、`03591 Minos`、`04523 LOCALUT`需具体范围/增量裁决。它们是执行待办，不是自动候选、自动Books或材料受阻。

原关闭理由中的“必须改变identity”“必须跨模型/大模型”“局部实现无价值”超出合同，应以原文实际增量及具体Books命题重判，不将全部854转换成全文队列。`.03515 Inside the Scaffold`从候选前关闭：13repos/22scaffolds、单analyst9→12维源码taxonomy仅提供实现参照；registered tools≠实际能力、topology≠loop driver未形成新的受控设计反证/独立机制或评价合同，SWE结果混模型/API。原文/方法/限制证据继续保留，不再维持旧5分仅报告；作者与独立审计一致，root据此同步72工作家族，7整合/27已有覆盖/10仅报告/28Books待办。安全关闭`.03598`应明确victim为rule-based simulation而非真实LLM；`.04060`按Ch72受控decoy/belief-update成本的具体成熟覆盖关闭，而非三Agent包装。MiniMax中文Blog有界日期目录已恢复05/25→04/27→03/18，仅Agent Tech Blog的历史缺口保留。日级Gate仍未通过。

### 03616 受限书稿写入，非作者采用通过

根任务批准本日作者独占 `books/part-02-model/20-sampling.md` 的本项局部写入。已完整对读 Sampling 正文及 Ch19/21 交接，原正文只把格式约束主要解释为 token-selection 层的 mask，缺少上游格式请求改变条件分布的独立比较。现于“Logit penalties 与约束的边界”内部、Stateful Exact Conditioning 之前新增“格式损失要先定位在 Prompt，还是 Decoder”：固定任务/模型区分 freeform、format-prompt 无 mask、同 prompt 加 mask，分测合规与内容正确；呈现型格式可比较两调用 freeform→reformat，但须计调用/tokens/延迟及重格式化改错，不等同单调用 thinking。编码正确性的 code/tests/tool arguments 不能套用该呈现实验，Ch78仍拥有参数语义和执行授权，简单抽取/低延迟/鲁棒模型保持单调用与grammar共存。

依据 [2604.03616v1](https://arxiv.org/html/2604.03616v1) §3–7、Table5、AppendixG/I。72个条件组合中39显著变化不等于39均由GCD导致：36涉及prompt-alone、15涉及GCD且存在重叠；正文未搬用这个比例为一般伤害结论。两调用在42/72改善、2项退步，thinking亦有退步，WritingBench不能推出一般收益。原实验仅6个3B–32B开源模型/4个API、四任务/四呈现格式，数学/写作LLM judge不是绝对真值；未复现代码、生产配置/SLO未披露。实际正文及末尾Review notes均已保存，作者写后对读与该文件diff check通过。root已独立重开exact-v1 Table1/§4.2–4.3/Table5/AppD/E及相邻Ch20，确认上述机制、两调用例外及代码/工具正确性不外推边界，批准本项Integrate。日报已同步7项实际整合/27已有覆盖/11仅报告/28普通待办；本项独立通过不替代日级Gate。本日作者按根指令完成此单项同步后停止，不接新日期。

### 16个准入重开的完整题摘重判（证据审阅尚在推进）

续跑重新完整读取当前AGENTS、三合同与统一Prompt，仅处理root指定的16个身份，不重扫854或其他日期。完整题摘先从854身份库读取，再打开各自官方`abs/2604.<ID>v1`核精确版本；03420库存摘要污染已以官方v1替代。此批目前均存在具体待核验增量，以下是准入理由，不是最终分母/证据通过或Books决定；不能将同一旧关闭理由复制到新结果。

| ID及exact-v1 | 原约束→实际增量→需要核验的选择 |
| --- | --- |
| [03258 SoLA](https://arxiv.org/abs/2604.03258v1) | 非零激活使硬剪枝与统一低秩截断各有损失；保留高贡献FFN通道并对其余/不同矩阵自适应分配rank，需核验同压缩预算是否应按组件贡献而非统一rank处理。 |
| [03414 KiToke](https://arxiv.org/abs/2604.03414v1) | 逐帧/片段压缩不能识别全视频重复；全局kernel冗余选择加时间区间merge，需核验极低token预算下全局多样性与时序完整性的独立成本/收益。 |
| [03420 Quantization Vector](https://arxiv.org/abs/2604.03420v1) | receiver侧QAT要求本地训练；donor的权重差分可迁移PTQ鲁棒性，需核验迁移与负迁移/调幅依赖的边界。官方v1只主张ViT与最高60%抗噪声改善，不继承库存后发摘要的22任务、60个accuracy points或严格对称性定理。 |
| [03950 DMA](https://arxiv.org/abs/2604.03950v1) | 一致低位attention会受局部精度要求限制；对角tile与远程tile分配不同MXFP精度并融合，需核验精度分区如何影响kernel和生成质量，而不是只保留B200加速数字。 |
| [04013 RUQuant](https://arxiv.org/abs/2604.04013v1) | uniform量化的区间中点并非非均匀激活的Lloyd–Max中心；block正交变换再global反射校准，需核验变换如何修正分布而非声称所有rotation天然最优。 |
| [04701 MUXQ](https://arxiv.org/abs/2604.04701v1) | outlier浮点旁路不适合INT型NPU；低秩辅助矩阵把异常贡献改写成统一整数结构，需核验追加计算与量化误差的交换。GPT2实验规模不构成排除理由。 |
| [04722 Adaptive KV](https://arxiv.org/abs/2604.04722v1) | 固定KV位宽不能按token重要性调整误差预算；轻量特征controller在2/4/8/16bit之间决策，需核验learned policy的成本、精度变化和是否真降低端到端decode延迟。 |
| [03263 LPC-SM](https://arxiv.org/abs/2604.03263v1) | local interaction与长期state可拆分；local attention、predictive correction和slow-memory novelty写入的分工及消融，需核验长期状态更新策略，不把158M/4096实验称普遍长上下文能力。 |
| [03446 MMEE](https://arxiv.org/abs/2604.03446v1) | attention逐算子搜索忽略跨算子buffer/顺序；矩阵编码并行枚举与analytic模型/pruning，需核验跨算子联合dataflow能否以可控搜索成本改变执行计划。 |
| [03674 DiffSparse](https://arxiv.org/abs/2604.03674v1) | few-step DiT的固定cache与必需full-step限制收益；learned逐层sparsity结合DP和两阶段训练，需核验省掉full-step的条件及训练/推理成本交换。 |
| [04281 Width Growth](https://arxiv.org/abs/2604.04281v1) | function preservation/早期离开clone子空间不必等价更好warm start；复制完整optimizer/scheduler状态后在确定/随机continuation得不同排序，需核验选择信号的regime/lag条件。 |
| [04743 Hallucination Basins](https://arxiv.org/abs/2604.04743v1) | 统一latent真假分隔假设可能失败；factoid与summary/misconception任务的几何重叠不同，需核验task-conditioned诊断与steering边界，不凭basin类比证明因果。 |
| [04863 Token Grounding](https://arxiv.org/abs/2604.04863v1) | whole-image相关性可由分散弱关联累积而虚高；局部patch定位和语义对齐特征判hallucination，需核验局部结构是否补global score盲区及sensor错误。 |
| [04238 Compiler–LLM](https://arxiv.org/abs/2604.04238v1) | 限定单一抽象层与只加parallel sample可能错配优化预算；compiler/LLM跨source/IR/assembly反馈与受控预算消融，需核验层级搜索/迭代分配规则。§3.3将compiler calls记0成本，不能据此说真实执行免费。 |
| [03591 Minos](https://arxiv.org/abs/2604.03591v1) | 应用名/单一utilization不能预测DVFS响应；低成本profiling联合power/performance分类迁移，需核验最近邻与LLM phase之间的边界。必要正文Table1/§7确含Llama2/3和prefill/decode，不按genericHPC直接排除。 |
| [04523 LoCaLUT](https://arxiv.org/abs/2604.04523v1) | low-logic PIM可用容量替MAC但LUT膨胀；canonicalization/reorder-LUT/slice-streaming以buffer容量换lookup并行，需核验空间/索引计算成本与prefill/decode适用范围。§VI-A/J确有BERT与OPT125M，非仅无关DNN应用。 |

本批官方精确版本页面未见撤回提示；这只是所查事件页范围的轻量检查，不宣称全版本史或所有勘误均无。明确潜在贡献的进入必要证据审阅，尚不能把16项全部称审阅完成或最终整合。日期继续使用本日有界公告批次范围及逐篇例外核验，submitted字段不改名为first-public。

### 日期反证对旧批次推断的定点纠正

非作者日期lane的[专用审计](V3_DATE_RECONCILIATION.md)确认本文件此前“整批08～09范围”不足成立：末端04934的DataCite版本Updated为北京09:43，且Updated/created与公开动作缺官方映射。原始字段仍保留，但上文所有确证式批次推断均已撤回为恢复线索，不据此机械迁移到04/08。报告72行公开时间和来源/结论已经纠正为归属待核。方法证据、评分和真实Books正文存在不因此失效，**本日当窗采用、候选冻结与日期Gate未验**；新16项仍只proposed，不新增正面Books。日期材料缺口与28项普通Books裁决、16项准入必要审阅分别维护，不能互相替代。

### 重开项首批必要证据与具体 Books 差异（日期终审前的 proposed）

#### 有据日期推断的局部恢复与明确例外

后续非作者一致性复核允许有据区间推断，不要求逐篇成功日志；前节对整个批次的撤回不能扩成所有家族均不可采用。本轮从 `../arxiv-owner-replay-20260903/20260407/arxiv-owner-receipt.json` 的持久原始字段逐项核对：03258/03414/03420/03950/04013/03446/03674/03591 自身 `v1_updated_timestamp_revision_metadata_only` 分别为 04/07 UTC 00:00:45、00:06:37、00:06:57、00:46:20、00:49:27、00:08:37、00:27:45、00:20:15。它们与连续 ID、相邻批界、OAI 日期及官方 Monday 20:00 EDT slot 共同支持 **推断** 北京08～09的当窗区间；Updated 并未被定义为首次公开动作，DOI created 也不是单独归属依据。仍待独立日期 lane 的最终核对。

04701=01:30:14Z、04722=01:32:00Z、04281=01:04:47Z、04743=01:33:09Z、04863=01:40:06Z、04238=01:02:40Z、04523=01:19:38Z 均跨本窗截止；03263 的版本字段更晚至04/11、03675至05/08。它们不能凭同批首项自动写入当窗候选，暂为有证据的贡献工作草稿/日期保留项，不机械移至下一日。方法审阅与新旧反证继续保留，日期异常不伪装成普通审阅完成。

03677 自身00:28:15Z，邻03676=00:28:14Z、03679=00:28:38Z，三者连续批次与官方 slot/OAI 日期相容且无所见晚字段例外，按相同标准作推断08～09；04410自身01:12:00Z不满足该推断，仍须更早公开依据。

#### Ch29 实际增量与 Ch34 暂存拟稿

**03677 / TRAIN-SFT**：按根任务授权，已在 Ch29“是否应对 Prompt 也计算 loss”之后写入“Loss 位置与 Corruption Support 是两个不同决定”。正文分清现有 AR loss mask 与 diffusion 输入破坏分布；联合 prompt/response corruption 重建可支持反向 prompt infilling，随后 response-only refinement 只是可选任务分支。保留额外训练/容量预算、任务/模板并非全胜、few-shot选择后固定测试、不借测试目标答案的边界；第24章拥有 denoising 范式，第29章拥有 SFT 分布匹配。依据重新打开的 exact-v1 §2.2、§3.1–3.2、§4–5，§3.3/Table1及§4.2口径差异未合为数字结论。Ch28 objective→Ch29数据/监督→Ch30更新表示的交接已对读，scoped diff check通过；root 已独立重开 §2.2/3.1/3.2/4.1–4.3 并对读真实正文，单篇采用通过。日期仍遵循有据批次区间推断，不把 Updated 当作公开动作。

**04410 / TRAIN-DPO**：只保存拟稿，不改共享Books，日期01:12Z仍未通过。当日 exact-v1 §3.1–3.4/§5/AppendixF与Ch34“Preference Scale”“Probability-geometry Gate”对读后的最小差异是相对混合密度的bounded ratio，不是已有beta scale或rejected-gradient gate。拟在后者与“DPO移除什么系统复杂度”之间加入：

> 当 chosen 与 rejected 的支持分布重叠很少时，直接估计两者比值可能把极少数样本变成异常强的更新信号。可以先把比较对象改为 chosen 与正负样本的混合分布：`p+/(alpha*p+ +(1-alpha)*p-)`，在 `alpha>0` 时该比值不超过 `1/alpha`。这约束的是 density-ratio 的数值范围及相应梯度系数，不保证任意参数梯度或整个训练轨迹有界，也不证明偏好标签真实。
>
> 混合比率用可调 `alpha` 与新的目标表达换估计稳定性；人口分布下的一致性依赖目标可表达等假设，不能写成有限样本、人类偏好或部署安全保证。它与原DPO属于条件替代分支，而非新一代必然取代旧目标。原DPO在数据支持充分、估计稳定且recipe已验证时仍更简单；混合目标仍要验chosen/rejected likelihood、KL和行为结果。

审阅范围Qwen2.5-1.5/3B、Llama3-3/8B，UF-G/MIX14K，TRL/AdamW一epoch、lr5e-7、batch128、clip1、8H10080GB/ZeRO3；三seed和AlpacaEval/GPT4Turbo LC不证明全部数据必胜。MIX的反例与部分DDRO差异不显著保留，待日期与非作者采用裁决后才能实际写入。

独立日期 lane 正核验批次末端 `Updated` 字段语义；因此以下是证据与章内比较，不把尚未确认的批次范围写成逐篇首次公开事实，也不新增正面 Books 采用。旧筛选表中的四条关闭理由已被本节的实际机制证据推翻，不再据“小优化/单硬件/ViT”拒绝。

- **03258 SoLA**：[exact-v1](https://arxiv.org/html/2604.03258v1)，Method、Table4、Prime Neurons 消融和 Inference Efficiency。非零 SiLU 不支持把低幅度通道直接硬剪；保留高贡献 FFN 通道，剩余块用 activation-whitened SVD，并在同内存预算下按保留奇异值能量选择各矩阵 rank。rank 取16倍数；整数问题由贪心得到次优解，不是全局最优。Table4 的 Llama2-13B/20% 配置 PPL 从uniform6.18到adaptive6.52，说明自适应并非每个指标必胜；Prime比例与校准样本仍是recipe。质量覆盖Llama2-7/13/70B、Mistral7B、WikiText2/zero-shot常识/5-shotMMLU；效率只是RTX4090上序列2048对应矩阵操作、10^3次中位数，不是端到端Serving、concurrency或SLO，precision未在该段披露。评分拟 **2+1+2=5**，标准必要证据完成；Ch54“减少Bytes”只是压缩类别，Ch49“双稀疏/量化不自动加速”也未解释高贡献原块与剩余低秩的分工及统一预算rank分配。提出 **INFER-TENSORRT-LLM / Ch49** 压缩执行分支，需独立采用审阅及日期确认；不报实际整合。
- **03414 KiToke**：[exact-v1](https://arxiv.org/html/2604.03414v1) §3.2–3.4、§4.1、Tables4–6、AppendixB.1。全视频kernel冗余得分经pivotal sampling避免TopK把同一相似簇全删；帧差分的绝对量/局部对比/相对比例定内容区间，只在区间内merge，非重新发明merge。Table5含10seeds/CIs，Table6区间与weighted merge联合消融支持各自贡献；阈值用100视频/分位和轻量搜索，不能称无需校准。LLaVA-OneVision32帧6272tokens、LLaVA-Video64帧及Qwen3VL至128帧，四video任务/A100；Table4压缩13.1ms+LLM53.1ms=66.2ms而非只报后者，10%保留均分58.2vs59.1，1%进一步退步。precision/batch/concurrency/SLO未披露；信息不可逆、稀有瞬时证据仍有风险。拟 **2+1+2=5** 标准证据完成。Ch23“固定预算先分信息责任”“Temporal aliasing”已有事件覆盖/分阶段裁剪，却未区分全局冗余选择与禁止跨内容区间合并这两层控制；提出 **MULTIMODAL-REPRESENTATION / Ch23** 对应段内窄分支，而非添加论文列表。待日期和非作者采用。
- **03420 Quantization Vector**：[exact-v1](https://arxiv.org/html/2604.03420v1) §4–7。同架构、同pretrained初始化的 donor普通微调/QAT差分，乘lambda加到receiver后再做3bit per-channel对称weight-only模拟PTQ；bias/norm/patch/head保持高精度，无rotation/smoothing。lambda=1有负迁移；§6.2 receiver test-set oracle sweep只展示经验上界，不能说部署已zero-shot选好幅度或“方向普适”；现实held-out calibration是作者建议，仍待验证。范围ViT任务，未证明LLM/kernel加速、硬件、batch/concurrency/SLO。精确v1题摘已经纠正旧库存后发摘要污染。拟 **2+1+2=5** 标准证据完成；Ch49“Post-quantization Recovery”是token动态补偿、“Anchor Artifact”是同anchor派生格式，均不覆盖跨任务donor差分的坐标兼容、负迁移与oracle幅度依赖。提出 **INFER-TENSORRT-LLM / Ch49** 静态量化artifact恢复的实验性替代分支；不把ViT结果外推LLM，也不报实际整合。
- **03950 DMA**：[exact-v1](https://arxiv.org/html/2604.03950v1) §4–6、Algorithm1/Table3及tile消融。causal tile的近对角QK用MXFP8、远处MXFP4，V保FP16；融合双份量化、编码、packing和scale转换以避免预处理吃掉kernel节省。OnlineSoftmax复用并不使量化attention精确等价；对角窗是近邻敏感性代理，远距离检索可失败。单B200/Triton，Llama3.1-8B/3.2-3B、LongBench2.5K–30K，与PyTorchBF16 SDPA比较；Table3 passage_retrieval_en在3B为80→37，平均升分不能盖住任务退步。batch/concurrency/生产SLO未披露，不能把kernel吞吐称全服务收益。拟 **2+1+2=5** 标准证据完成；Ch49“FlashAttention”及“量化前诊断分布”分别覆盖IO/tile与channel变换，未覆盖sequence tile近远精度分区及双格式预处理融合成本。提出 **INFER-TENSORRT-LLM / Ch49** 在attention执行主线的窄分支，待日期/非作者采用。

- **04013 RUQuant**：[exact-v1](https://arxiv.org/html/2604.04013v1) §3–5、Eq13、Tables4–6。uniform bin的centroid条件不等于只控制outlier最大值；block Householder/Givens先调整激活分布，再可选学习global reflection以最小化Transformer block output discrepancy。§5.2区分不优化reflection参数的RUQuant与较慢的+fine-tune，不能把“约一分钟”归于两阶段梯度训练。Llama1 7–30B、Llama2 7/13B、Llama3 8B；WikiText2校准128×2048、C4/WikiText2/5任务、W4A4/W6A6、softmax未量化、L20校准；Table4的LH仅微小收益且有部署代价，Table6是3090、prefill2048、batch1/4/16的layer-wise时间，不是完整服务/SLO。拟 **2+1+2=5** 标准证据完成；Ch49“量化前先诊断分布/Rotation Scope”已有group与变换次数，却没有uniform midpoint失配的centroid解释及output-loss校准这条条件分支。提出 **INFER-TENSORRT-LLM / Ch49** Numeric Plan内最小增量；保持普通rotation共存，待日期/非作者采用。
- **04701 MUXQ**：[exact-v1](https://arxiv.org/html/2604.04701v1) §3.2–3.3、§4/ Tables1–2。Body将outlier缩小，Aux保存选中列，输出按`Ybody+(2^exp−1)Yaux`重构；这是integer-compatible的辅助乘法/重组，不是免费误差消除，也不是学得任意rank的SVD。exp=1可两路相加，exp=2有额外重组；大于6的outlier规则继承LLM.int8。GPT2 .1/.3/.7B、WikiText2、RTX3080/12GB、absmax、5–8bit activation及4–8bitweight；§4.3明确fake quantization，不含真正INT kernel、latency/power/NPU实测。6bit时MUXQ质量可明显弱于FP16 outlier bypass，不能说普遍优于LLM.int8。拟 **2+1+2=5** 标准证据完成；Ch49“integer-only boundary”拥有部署条件，却未说明用额外整数aux分解替代高精度异常旁路的收益/成本。提出 **INFER-TENSORRT-LLM / Ch49** 分支，仅机制可采用，硬件加速待验证，待日期/非作者采用。
- **04722 Adaptive KV**：[exact-v1](https://arxiv.org/html/2604.04722v1) §3.4–3.8/§4。四维feature输入128隐藏宽度三层MLP，以bitlabel交叉熵及class-wise latency/quality期望训练，append前选2/4/8/16bit；80/20是token样本划分，不能自动证明跨context泛化。RTX4090/24GB、SmolLM135M/360M/1.7B、HellaSwag/OBQA/ARC-C；§4.1写ms/token，Table3写s/token，数值单位无法据现文统一，且未披露长度/batch/concurrency与packed异精度kernel/controller端到端分账。Table4使用其他模型文献分数，不能把换backbone优势归给该controller。理论“Pareto/导数更大”式不构成可验证的普遍收益证明。拟 **2+1+2=5**，已深入读冲突必要段；建议 **争议 / 暂缓：INFER-KV-CACHE Ch45**，不写Books、不支持性能数字。重开需作者明确时间单位/测量路径、bitlabel构造和所测decode contract；原文及具体限制足以安全隔离，不把它算普通未读完。
- **03263 LPC-SM**：[exact-v1](https://arxiv.org/html/2604.03263v1) §3、§4.2、§5/Tables2–4。local attention维护局部读取，fast state逐token、slow state按chunk写；ONT把相对旧slow state的正交novelty放大，partial-chunk state需训练/生成顺序一致。correction controller learnable sparse ratio与多个auxloss并存，不能把所有收益归slow memory。158M StageA去ONT/predictive/stop均更低LM loss、去slow-memory只差0.32%，并使token/s从6798变21938；六个teacher-forced delayed-key prompts里去slow memory也稍好，远非普遍长程记忆优势。匹配checkpoint/corpus/budget的StageB adaptive vsfixed sparsity支持一个较窄的控制反证，StageC4096只证明该训练运行完成，不能证明全面长上下文优势。拟 **2+1+2=5** 标准证据完成；Ch22已有hybrid优化与检索职责分拆，但未隔离本组ONT/slow-memory效益，**仅报告**保留matched adaptive-control结果与组件反证，不把弱证据架构全套写成长期新设计；后续更大/独立任务反证出现再定点重开，不因小规模本身拒绝。

- **03446 MMEE**：[exact-v1](https://arxiv.org/html/2604.03446v1) §III–VI、VII-A–E。跨算子保留tile只有与计算顺序/loop boundary匹配才消DRAM重读；softmax前的partial sum不可任意跨传播。Pseudo nested-loop共同表达tiling、compute order、buffer层级和recompute，离线symbolic domination pruning再用query矩阵枚举。所谓最优限于§V声明模型与枚举空间：能耗假设计算量不随映射变化，latency取compute/DRAM瓶颈；不保证真实accelerator全局最优。1410 Timeloop对照为intra-operator模型核验，不等于fusion实机验证。两个NVDLA/TPU-like模拟配置（4 arrays、1/4MB、60/128GB/s、1GHz、28nm能耗表），BERT512–16K/GPT3-13B/PaLM62B training/prefill；无生产decode/batch/concurrency/SLO。TileFlow其order/buffer搜索预固化、runtime仅MCTS tiling；Chimera为TileFlow重现，不能写所有baseline同成本独立实现。Pareto稀疏、recompute对PaLM有利而BERT/GPT未明显同益；buffer可容纳全部矩阵时差异消失。拟 **2+1+2=5** 标准证据完成。Ch49“Layout Plan跨算子/单独验Cost Model”已分solver与估价，“联合Tensor Lifetime”已说fusion，但未解释**buffer保留与compute ordering必须共同选**及recompute作为同空间条件分支；提出该两段内最小增量，数字不入Books，待非作者采用。
- **03674 DiffSparse**：[exact-v1](https://arxiv.org/html/2604.03674v1) §3.2、§4.1–4.3、AppendixA.4–A.6。learned layer×step×candidate-rate成本矩阵经DP分配全局sparsity，token-ranking为可替换组件；STE+teacher/student LPIPS蒸馏更新成本模型，两阶段先保full-step warm start再合step/layer成本重新分配。DP约30秒是离线且训练4–10小时，推理使用预计算配置，不是实时动态求解器；最优针对预测成本与离散空间，不是质量全局最优。PixArtα20step/FLUXschnell4/DiT-XL2-50及Wan1.3B，10K COCO/WebVid captions/类别条件、无GT图像训练，作者报8 MI250“80GB”不额外证明硬件规格；COCO30K、ImageNet50K、VBench950prompt/4750video/256²/2秒8fps。Wan§4.1为25steps而结果Table3为20，需按各自口径，不合成统一服务claim；DiT FID2.26→2.81退步。两阶段比单阶段受测FID较好，更细候选0.125反而较差；512²迁移是受限模型实验，训练token memory仍贵。precision/batch/concurrency/SLO未披露。拟 **2+1+2=5** 标准证据完成。Ch49已有静态template/cache误差guard与runtime chunk调度，但不含**训练期全局误差/稀疏预算分配→静态部署artifact**和取消固定full-step的learned条件分支；建议在“Execution Plan联合Tensor Lifetime”原diffusion段内窄补，不增加通用SLO保证。待日期/非作者采用。

- **04281 Width Growth**：[exact-v1](https://arxiv.org/html/2604.04281v1) §3–6/9。候选是weight+AdamW moments+scheduler的完整状态；clone扩宽保持函数，reference-slice扩宽亦可保持却避免对称clone。TinyStories decoder6层256→512、8.46M parent、context256、BPE8192、AdamW lr3e-4、有效batch48/12288tokens；seed0全池与seed1缩小池。16step两regime均exactcopy较好；128step deterministic reference-slice较好，stochastic则exactcopy继续较好。后者将shuffled order与新增dropout=.1捆绑，不能归因某一种噪声；没有重复continuation/CIs或前沿规模证明。零步KL/loss可打平不同后续轨迹，16step AUC错过全部deterministic后发翻转；escape并非通用selector。拟 **2+1+2=5** 标准证据完成。Ch28实际“模型结构扩容”已经持有parameter/optimizer/schedule联合迁移、symmetry lock、function不证明trajectory，覆盖主机制；本材料真正补的是**不能默认asymmetric rewarm或escape更好，selector budget应匹配continuation regime**的受控反证。建议窄纠正现有扩宽段而非另加growth摘要；但自身01:04:47Z跨截点，本日不采用，作为日期保留项保存确切提案。
- **04743 Hallucination Basins**：[exact-v1](https://arxiv.org/html/2604.04743v1) §5.1–5.5/§8、AppendixC/E/F。uninformative prompts构造reference state，centroid/covariance按70/30训练切片冻结、三random splits与bootstrap只评受限AUROC；truth标签来自数据集，不把latent风险当真值。任务几何差别和模型差别明显，summary/misconception并非统一可分basin；理论依赖attention均匀/局部Jacobian收缩等假设，未证明真实Transformer全局吸引子。§8.3 steering会改变下游状态，但报告的P(hall)是trained classifier输出，不能直接当生成答案真实错误率改善。RTX4060 laptop8GB、所列1–8B模型/短任务，部分过滤后有效样本少；长上下文/大模型/closedAPI不可外推。拟 **2+1+2=5** 标准证据完成。Ch66“可解码Failure Direction不拥有自动纠错权”和task/slice校准已持有probe预测≠独立干预、控制生存/端到端行为边界；本例是受限task-conditioned诊断证据，拟**已有覆盖**而非统一latent truth机制。日期01:33:09Z未通过，不入确定候选或本日采用。

#### 普通 Books 待办的实际正文裁决补充

**写后独立复核 checkpoint（不等于日级 Gate）**：03677 已在 Ch29 实际写入并通过 root 非作者来源/相邻正文复核；03258/03420/03950/04013/03446/03674 已在 Ch49 各自原论证内写入并通过必要 exact-v1 与真实正文复核，其中03674按反馈纠正为共同稀疏率/跳算预算约束下最小化预测重构代价；03414/03591/03253/03855分别写入Ch23/70/78/81并通过同类复核，03414按反馈收窄为inverse-kernel-density top-k保留可能遗漏重复簇、加权采样降低风险而不保证覆盖。这11项可同步实际整合，但分母、日期例外隔离、其他普通采用裁决与全日日级非作者Gate仍未闭合。没有运行作者实验。

当前剩余早字段普通采用裁决为03362/03425/03592/04142/04161/03257/03340/03537/03962/03242/03922。前8项已有必要原文审阅，已向root发送具体缺口/owner提案，尚待授权写入；后3项具体已有覆盖理由如下。晚字段例外保留证据与拟稿而不获得本日采用权，不以全批日期受阻隐藏这些可执行待办。

- **03962 StreamGuard — 已有覆盖建议**：Ch66“Counterfactual Localization 只能定位风险转折，不能读取真实意图”实际正文已要求固定前缀、重复continuation、冻结generator与judge及限制风险sensor权；Ch72“Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence”已拥有buffer、released bytes、abort及最终fence。因此用未来harm rollout训练线性head是受限sensor实现，不需要新建authority机制。canonical PLATFORM-SECURITY，Ch66为测量handoff。仅unsafe subset计算的response_loc precision=100%不能泛化为全流零误报，70B/H100 StaticCache steady-state 2.4–9.5ms不能当生产SLO，具体实验继续保留日报。
- **03242 DRAFT — 已有覆盖建议**：Ch66“从 Raw Score 到可定位、可校准的 Claim Sensor”及“可解码 Failure Direction 不拥有自动纠错权”已经分开内部状态、监督标签、模型专用校准、原始证据和独立authority。16个tail latent queries联合raw trajectory是sensor实现；AuraGen合成/LLM审判和模型不同的显式reasoning对照不证明latent faithful或通用压缩最优，t-SNE不是因果证据。用本篇作受限验证，当前无需追加产品摘要。
- **03922 ACES — 已有覆盖建议**：Ch66“相关采样会抬高 Coverage，却压低 Selection 上限”与独立task tests/heldout验收段已区分候选相关错、selector、独立correctness。LOO AUC避免自己的test结果直接自评，是受限ranking estimator；其平均test质量better-than-random前提不能从生成测试自动取得，也不消除相关错误。MBPP Pass5劣于直接选择、Hard最多1/14的反例保留报告，不把内部一致性升级为真值或置信概率。

- **03591 Minos**：[exact-v1](https://arxiv.org/html/2604.03591v1) §4.1–4.3、§5.1–5.3、§7.1/7.4/8。两个近邻分别消费power/TDP分布和kernel-duration-weighted SM/DRAM特征，默认频率只profile一次新负载，再借reference的frequency-scaling曲线；offline簇是解释层，runtime只需近邻，不混称cluster直接拥有决策。功率目标可选择p90，性能目标单独约束允许退化，QwenMoE的两个近邻不同。MI300X8卡节点192GB、1300–2100MHz cap实测；A100 PCIe40GB节点只有utilization研究，因无权限未做相同cap，不能宣称跨厂商控制验证。energy delta/1–2ms+EMA来自噪声取舍，边界idle截去，不等于整机账；Llama2/3 vLLM batch1/8/32，训练torchtune32/64，QwenMoE case batch32。Qwen功率预测约5%超目标，是反例而非hard bound；PerfCentric两例守5%不证明线上tailSLO。§8明确跨vendor计数器不等价，phase/input/model漂移不能自动借同近邻。拟 **2+1+2=5** 标准证据完成；Ch70“执行中闲置/Deep Idle”和“组件/阶段Power Budget”没有双profile-neighbor借频率曲线机制，建议后者内窄补，profile identity/失败回退是平台采用推论而非作者已保证。日期有据推断可恢复，待root非作者采用/共享Books。
- **04863 Token Grounding**：[exact-v1](https://arxiv.org/html/2604.04863v1) §3.2–3.3/4.1–4.3、Appendix6/8/11。ADS从top-patches做8-connected blob及background entropy；CGC另用token/patch top-k cosine alignment，两者并非同一特征：紧凑attention仍可语义错配，分散attention也可能匹配对象。Layer向量送XGB/RF/MLP监督分类，不获得真值权威；中层最佳的定性叙述也不能代替Table6中all-layer更好的具体配置。4000 COCO2014 images按image90/10、GPT4o+caption/object label；POPE hallucination217/3556约6.1%，F1=.41/AUC=.75远非可靠拒绝所有假对象。三个7/8B模型、hyperparameter validation、top-percent敏感和融合消融支持互补信号；Table2/4主结果口径不同不合并，作者“所有metrics/models最佳”与局部格不完全一致。GPU/precision/length/batch/concurrency/SLO/在线feature成本未披露。拟 **2+1+2=5** 标准证据完成。Ch66已有typed span sensor、model-specific calibration/OOD representation与detector分账，却未直接解释“空间紧凑与语义grounding需两轴”分支，拟精确机制增量可作proposal；自身01:40:06Z目前日期隔离，不写本日正面Books。

- **03244 OpenEval**：再对读Ch66“Benchmark相关性应分解共同构念与生态噪声”实际正文，已区分shared factors、task-specific variance、metadata effects与非因果解释，原始逐benchmark保留；本篇cohort-dependent CTT与answer-key簇为受限构念诊断实例，没有需要新增的设计owner。建议**已有覆盖**，具体正确数据225Kitems/64bench/8Mresponses与反证继续保留日报，不以规模制造书稿diff。
- **03253 Self-execution**：对读Ch78“编译器反馈可以前移，但仍是受限Authority”，它当前只有真实compiler syntax/type诊断，不含 learned execution simulator的反馈角色；建议在同一authority分支补“模拟执行只生成可错的sensor，不能获得真实execution oracle权威，scaffold-alone不证明训练效果”。exact-v1 §6.2–6.4/Table3–6已核真实执行更强、模板单用会降、私测初对改错5%与初错修对10.4%，只单文件竞赛，不推广repo。评分6，拟**整合**待root落笔/非作者采用。
- **04580 Code–test co-evolution**：对读Ch81“在搜索候选之前先编译contract”及EvaluatorDrivenSearch实际body，已包含candidate/test共同错误、evaluator不是真值、独立holdout/权威、预算和谱系；paper的consensus+elite控制内部fitness未突破该contract。建议**已有覆盖**，受测交叉测试组件收益与不同模型/旧leaderboard比较限制留日报。日期01:22:54Z仍隔离，不支持本日采用。
- **03855 VectraFlow**：Ch81有typed流程IR/temporal state但目前没有“否定必须finite within，窗尾才可accept；LLM抽取与每entity确定NFA分权”的具体论点。建议root在可执行contract原论证里窄补，不沿256clinical notes推一般stream watermark/late event guarantee。自身00:40:27Z+批次推断可当窗，评分6且方法/评测/局限证据已完成，待共享写入与非作者采用。

- **04238 ACCLAIM**：[exact-v1](https://arxiv.org/html/2604.04238v1) §3.3–3.5、4.1–4.2/4.5、5.2–5.3。LLM层级agent提出程序/IR/assembly候选，编译器和隐藏reference测试拥有本组correctness筛选；测试是LLM生成有限输入并与原程序输出对比，不是语义等价证明，translation validation仍是未来工作。预算对agent调用计unit cost、compiler调用按0处理，不能当真实wall-clock成本；同预算探索宽度beta和feedback迭代alpha会改变结果，受测100程序中4×1优于2×2和1×4，不支持所有任务默认多迭代更好。CodeNet先过滤编译/测试生成/有效case数与优化空间后剩564题、10samples；clang18.1.3-O3、96-core Xeon8275CL/1TB、Claude3.7SonnetBedrock、单题1h上限，不外推LLM-serving或全程序正确性。反复执行artifact才可能摊销优化成本，一次性程序仍可不值得搜索。拟 **2+1+2=5** 标准必要证据完成。Ch81“在搜索候选之前先把问题编译成可执行contract”及EvaluatorDrivenSearch已拥有候选、预算、有限oracle、heldout和晋级责任，Ch66“Search方法的排名必须覆盖预算形状”正文已要求width×depth/frontier与相邻预算而非单点排序；本篇提供该原则的受限编译案例，拟**已有覆盖**，不新增产品摘要。自身Updated/v1=01:02:40Z不支持本窗区间，保留为精确日期异常，不以旧评分或提交日期采用。
- **04523 LoCaLUT**：[exact-v1](https://arxiv.org/html/2604.04523v1) III-A、IV-A–D、V-A/B、VI-A/G/I/J和VII-B。operation-packed LUT用指数增长的表容量代算术，联合排序activation与weight保inner-product；host产生排序activation/permutation，PIM用额外reordering LUT减少unpack/repack，再保持activation选择、只把相关canonical/reordering列slice搬到SRAM跨weight rows复用。它不是只把整数matmul放近内存：pack degree必须联合LUT容量、slice搬运与重复lookup选，复用不足时buffer-resident小表仍合理。IV-D一阶模型明确仅计LUT路径，VI-I在W2A2会因未计input load预测偏差；VI-G residual index计算比LUT access更大，reordering访问仍占kernel6.9%，省算术不等于省索引。32UPMEMranks×64banks、2048PE、每PE64MBDRAM/64KBSRAM、SDK2023.2.0/XeonGold5215；BERTbase/OPT125M/ViT不同W1A3/W1A4/W2A2/W4A4及max128任务，host仍做非矩阵与聚合，半bank/buffer给LUT造成multi-job容量限制。LTC是适配UPMEM实现，不是与原硬件公平横比；高bitwidth/低reuse可能不如算术，bs32–512与prefill/decode实验未给生产concurrency/SLO。拟 **2+1+2=5** 标准必要证据完成。Ch49“FractionalPrecision→physical layout”和“数学表示决定state materialization与异构划分”实际正文覆盖布局/放置原则，但尚未说明**把算术换成离线表后，容量/索引/host转换/分层reuse共同决定执行计划**的具体分支；提出该主线内最小机制补充，而非加入加速比例。自身01:19:38Z为日期异常，当前只保留提案，不实际Books采用。

### 最新作者收束 checkpoint

本轮已将旧72项工作表按逐家族早/晚字段分为37/35，独立准入重开的16项另分8/8。于是88个贡献工作家族中，45项支持有据当窗区间，43项隔离日期上界；854为raw唯一身份，未声称全部摘要或全文已读。README仅§3–4承载45当窗候选与证据，43项逐ID原始日期/重开条件放§5，完整审阅工作不删除、不机械移日。

root许可新增8项已实际写入：03362/03257→Ch66，03425→Ch49（不再原Ch72 canonical），03592→Ch21，03340/04161→Ch26，03537→Ch24，04142→Ch33。作者已对真实论证与必要exact-v1核验；root反馈后将AEGIS收窄为modulus-chain placement优先、token coherence其次，RISE改为经验activation frequency/specificity ratio/shared CV/绝对频次，AC-LAM默认FDM-form与IDM stop-gradient对照分清，future leakage仅proxy。根任务正做非作者写后采用复核，这8项暂缓不是材料受阻；其余11项新写入的源/正文非作者复核已通过。

三项03962/03242/03922按上面实际body对照同步已有覆盖，03244 OpenEval亦同步已有覆盖。当前45项为15整合通过、16已有覆盖、6仅报告、8实际写后待独立核验；预计8项通过后为23/16/6，但当前不预记最终通过。scoped validator与diff check通过，日级语义Gate仍未结束。所有本轮共享章ownership已释放，未stage/commit/push，未改全局LS/月度索引或其他日期。

### 非作者采用复核已收束，等待日级 Gate

root已完成03362/03257/03425/03592/03340/04161/03537/04142八项必要原文、实际正文与相邻论证独立复核。AEGIS的placement hierarchy、RISE的activation frequency已按反馈修正；04161的83/106/157ms绑定GR00T N1.5、LIBERO、single A800，推理precision/实时控制SLO未披露；03362补§3.5过滤不完整run，flags不能估计所有执行的failure prevalence。八个Review notes同步独立复核通过，仍明确未复现实验。45项终态为23整合、16已有覆盖、6仅报告，普通审阅/Books待办为0；43日期保留项与8来源缺口仍精确隔离。本日状态仍进行中，等待apr03非作者日级Gate，不将单篇通过冒充整日通过。

### 日级反向抽检局部恢复：03647 CSRS

apr03的非作者抽检指出原“单类几何+成熟组合”前分母拒绝不能成立；本轮只恢复此家族，不重审既有45项。完整exact-v1题摘与[必要原文](https://arxiv.org/html/2604.03647v1) §3.1–3.2.2、Eq6–8、§4、Tables1–4、AppA.2.4–A.6已核。工作评分 **Design Delta2 + System Reach1 + Durability2 =5**，标准审阅完成、Experimental、未复现实验。

母轨迹n=8，各在floor(.7×长度)截断后局部重采样m=5，新增40条；这改变条件proposal而不是把48条都当独立全局探索。Eq7在母/重采样合集估答案base frequency，Eq8再以局部重采样frequency/base frequency的ratio经tanh有界调整reward；该频率变化是局部稳定性proxy，不是真值oracle。固定.7不是已识别semantic pivot，AppA.6承认错误prefix可继续产生稳定错误；视觉高斯扰动也依赖语义不变假设。§3.1变分分布的contrast factor减缓只在理想reward-gap模型成立，未证明实际clipped神经GRPO无collapse或会收敛到正确答案。

Qwen2.5-VL7BInstruct，Geometry3K/GeoQA/MMR1训练，四视觉数学benchmark；8A80080GB，veRL/vLLM、15epoch、trainbatch256、prompt/response上限1024/1536、PPOmini64/micro8、AdamW1e-6；precision、生产concurrency/SLO与seed不确定性未披露。Table3增加局部重采样数量并非单调，Table4 .7最优也不单调；Table5分SFR/RRM/VSP有组件增量，但MajorityVote行恰与Table1未训练base相同、不同于Table1 MM-UPT，不能合并成同一个强baseline或同总采样预算的因果证明。AppA.3跨模型结果仍是此受测分布。

日期自身v1 Updated字段2026-04-07T00:25:30Z早于01:00Z，联合连续ID/OAI/邻界与官方slot支持本窗08:00～09:00有界推断；DOI created=02:46:16Z及submitted=04/04都不作首发。既有Ch33“Verifier Error可能在组内相关”“Exploration必须与Verified Progress对齐”已承载共同偏差与proxy不能担任truth authority，但没有完整承载此局部重采样frequency-ratio方案。不能以主题相同强记已有覆盖。root认可 **仅报告**：真实连续reward/proposal新分支保留，但同预算归因与MajorityVote/MM-UPT口径不一致不足以采用稳定选择，不为扩Books自动升级审阅。明确baseline勘误/同预算证据到达后仅重开该采用判断。

最终工作集89=46有据当窗+43日期隔离；本日正式46=23实际整合（单篇非作者采用通过）+16具体已有覆盖+7仅报告，普通pending为0。854 raw全标题与定点完整题摘范围不变，14来源/8精确外部缺口不变。apr03独立最终日级Gate通过，核对46唯一候选与46证据标题集合、评分、23真实Books落点和03647具体仅报告反证；复用原45有效审阅、不无差别重读附件。作者已同步README状态/§6，不声称隔离项已获证明、零遗漏或实验复现。当前合同安全终态：完成。机器校验及scoped diff检查通过，未stage/commit/push。
