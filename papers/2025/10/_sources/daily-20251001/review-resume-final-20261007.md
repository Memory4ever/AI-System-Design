# 2025-10-01 增量补查最终独立复核

复核者：Codex，本会话此前负责 Nov01 作者工作；非 Oct01 原作者、返修者或 Advanced-resume 写入会话。不冒用 Dewey / Peirce 身份。
复核检查时间：2026-10-07T17:16:53+08:00；写后检查见末节。
对象：[Oct01 日报](../../01/README.md)、[返修记录](supplement-20261007.md)、[Dewey 首校准](supplement-first-review-20261007.md)、[Advanced 续跑](advanced-resume-20261007.md)及其实际原件。
原窗口：2025-09-30T09:00:00+08:00 ～ 2025-10-01T09:00:00+08:00。补充窗口：2025-09-30 ～ 2025-09-30。

**最终日级结论：通过。2025-10-01 本轮增量补查达到含明确隔离外部保留项的日级安全终态；未发现尚需作者继续扫描、校准、证据审阅或修改 Books 的普通研究待办。**

此结论不是全部 Coverage / Evidence 正面通过，也不证明全站、全月或互联网无遗漏。原候选仍为七案例页发布的一个家族，原日期、`2+1+2=5`、有效深入审阅与仅报告处置冻结；新增确定当窗家族、评分、深入 Evidence、Books 写入均为 0。日报当前“进行中 / 未通过”是尚未同步本文件的作者字段，不能解释为本复核未通过；按用户授权，本轮不代改 README、Books、State 或索引，也不声称 root 已同步日级或月度计数。

## 1. 当前合同、独立性与复用范围

本轮重读 main 工作树 `AGENTS.md`、`CODEX_RESEARCH_PROMPT.md`、研究合同、Report 合同、来源清单使用说明/每日 14 组/arXiv 主题说明、`ROADMAP.md` 与 State 最新相关路由，并读取当日报告及上述停点。只复核 Oct01，不启动其他日期、Weekly 或每周来源扫描。没有调用 catchup，没有执行 Git 写操作。

依据研究合同 §7 与 Report 合同 §3.6，复用 [Peirce 最终复核 §8](FINAL_INDEPENDENT_REVIEW.md#8-窄修写后复查与最终通过)中未变化的七案例必要核心、日期权、5 分及 Books 决定；复用 Dewey 对未受返修影响的 74 项潜力、18 项完整题摘关闭和机构核心的有限校准。复用不是本轮重新打开所有原页、96 份题摘、PDF 或附件，也不把先前的日级通过自动授予本轮新增工作。

本轮直接读取全部 23 项新增完整题摘，另读 EQUISeg / EOE 原 Atom 完整摘要、6 项旧完整题摘关闭样本和 12 项未选月库存完整题摘；核 4 个旧标题范围样本及 3 个 October 身份样本。结构化核原件和当前官方撤回页的实际范围如下，不宣称全量全文或实验复现。

## 2. 全部返修与旧候选冻结

| 返修 | 非作者实际依据 | 裁决 |
| --- | --- | --- |
| R1：三撤回分离 | 本轮直接打开官方 [PoseDiff](https://arxiv.org/abs/2509.24591)、[Social Science](https://arxiv.org/abs/2509.24877)、[BiHDTrans](https://arxiv.org/abs/2509.24425) 当前 abs；分别核页首、Comments 与 history | 通过。2509.24591v2 是比较公平性/实验严谨性问题，2509.24877v3 是语料、方法、框架、结论根本重构，2509.24425v2 是方法局限/实验设置缺陷。三项均已退出潜力或普通关闭集合，不入选/评分/Books，不用旧稿仍可下载恢复采用，不再索日以继续采用失效结论 |
| R2：Qwen 日期边界 | 直接解析 `supplement-20261007/qwen-api.raw` 的全部 60 个日期并转北京时间 | 通过。最新为 2025-12-23 Qwen-Image-Edit-2511；目标日前最近 09-24 Qwen3-Max，后侧 11-13 DeepResearch；返回对象 Sep30 为 0。真正缺口为配置历史完备性，不是缺后侧或请求失败；不授全站零事件 |
| R3：EQUISeg 重开 | 直接读 CV/RO Atom 的 2509.24505v1 完整摘要 | 通过。优势模态退化、equal encoding、四阶段 CMTB、SGM 互引导构成可核的失衡/贡献调节链，不能以 segmentation 或局部实验关闭。保留 `MULTIMODAL-REPRESENTATION` 潜力及日期门；不提前证明新颖性、稳健性或迁移，落窗后再核 baseline、消融、退化协议和代价 |
| R4：EOE 机制纠正 | 直接读模型 Atom 的 2509.24436v1 完整摘要 | 通过。明确先 AdamW，再在当前/最佳 expert tensor 间进行 crossover、PSO、mutation；是混合优化而非替代 AdamW。未采用吞吐、模型缩小或质量结论 |
| DeepSeek News 与 Google 入口连带措辞 | 对照当前正文、实际请求记录及 `euler-repair-google-web.json` 解码后的定位输出 | 通过。09/29 只是目标日前最近 News；Google pubs 可达而 curl 超时仍保留为请求事实；DeepMind 真实第 2 页是有限 selection，不是全机构首公开库存 |

三撤回本轮官方位置：PoseDiff L8/L21/L30；Social Science L8/L21/L31；BiHDTrans L8/L23/L32。这里的位置来自本轮实际 web 输出；版本撤回/修订日期不是本轮确认的历史公告公开日。未遍历三个家族的旧全文或全部版本。

原四 Atom 共 159 返回、125 唯一 ID；本轮独立复算其身份集合，并定点核纠错信号。当前分账为 75 项 September 潜力、18 项完整题摘贡献关闭、3 项撤回、18 项标题范围退出、10 项 October 月份退出、AMemGuard 1 项 October 恢复线索，合计 125；不是本日候选分母。未发现三撤回仍混入 75 潜力的现行断言。

用只读的当前暂存版本与工作树定点比较：原窗口、补充窗口、唯一候选整行完全相同，包括 `2025-10-01T08:00:00+08:00`、5 分、深入完成、仅报告。原 case 公开日权仍来自七 RSS / 官方 case 页，不授整份 PDF 的历史 first-public、历史字节或全文已审。

## 3. 新 Advanced / API / 月表发现权限

本轮不重新请求全部查询，而是直接解析保存 HTML、请求 JSON、Atom 原件并复算身份，避免把作者归并 JSON 当作独立证明。

- 表单原件明确 announcement date 只支持年/月；真正 CS checkbox 为 `classification-computer_science=y`，并 include cross-list。原版和 `repair/` 两批六主题均 HTTP200 / no results，不能作为有效零命中。`boundary/` 的跨月上界响应才恢复了 September 公告月；不推断空响应服务端原因，也不把上界当日筛选。
- 六页实际请求保留 UTC 执行钟；作者本轮发现请求范围为 2026-10-07 08:44:48 至 08:51:01 UTC，FP8 定点回源另记 08:54:19 UTC。这些不是论文公开日。本复核新增联网仅为第 2/5 节四个官方 abs 页；没有伪称重新联网 14 站。

| 实际主题 | 原件复算 | 实际停止权限 |
| --- | --- | --- |
| `"large language model"` AND inference | 50/427；末 2509.24189 | start=0；原 HTML 的 Next 指向 start=50，未请求，不授全查询召回 |
| `"language model"` AND quantization | 50/63；末 2509.09550 | start=0；Next=50，余 13 未请求，不变成必审队列 |
| `"language model"` AND `"reinforcement learning"` | 50/331；末 2509.24776 | start=0；Next=50，未请求，不授全月召回 |
| title=`"world model"` | 39/39；末 2509.00559 | 返回无下一页；题名发现不等于 39 项贡献/Evidence 完成 |
| title=memory AND agent | 25/25；末 2509.01987 | 返回无下一页；未选标题没有被自动判成无贡献 |
| title=multimodal AND `"foundation model"` | 23/23；末 2509.01360 | 返回无下一页；领域词本身不授或撤销准入 |

六页原件共 237 条、227 唯一身份，全部行有 `originally announced September 2025`；不能推 Sep30。官方月表短路径 404 后改为 `/list/cs.CL/2025-09?skip=2115&show=100`，原 HTML 实际 100 对 dt/dd，编号 2116～2215，全为 cross-list，首 2509.23962、末 2509.26628；2215 是月计数，不是当日分母。停止末页，不翻前 2115 项。月表请求记录中的通用 Advanced parser `rows=0` 不是月表空列表，实际 dt/dd 已独立恢复 100。

六页与该月表并集 **309**；和旧 125 的交集 **27**；集合差 **282**，与保存归并集合逐 ID 相符。RServe 对照为旧 2509.24381，不因当前摘要称 REDServe 新增家族。7 个具名 API 请求返回 7 个唯一 entry，无分页；23 项全部不在旧 125 中。16 项 Advanced 完整摘要、标题及精确版本 span ID 与原 HTML 相符，7 项 API 的完整 summary / ID 版本与 Atom 相符；未把截断摘要或提交字段当历史日证据。

## 4. 全部 23 项新增题摘校准

**23/23 有限准入潜力及隔离边界通过；不是 23 项正式当窗候选或 Evidence 通过。** 以下均直接读完整摘要并核精确当前身份，owner 只作 ROADMAP 路由。共同限制为缺具体公开日，且当前修订摘要不回填 2025 v1；不评分、不采用结果、不进入 Books。日期恢复后只定点核该事件版本及必要方法/反侧，不重跑整月。

| 精确已读版本 | 独立校准的最小增量与必要反侧 | 唯一拟 owner |
| --- | --- | --- |
| 2509.23958v1 RLIR | 从生成视频逆推动作作为奖励代理；须核 action-following oracle、代理误差和预算，不能采用“首个”或收益数字 | `MULTIMODAL-WORLD-MODELS` |
| 2509.24116v2 GLoW | trajectory frontier 与 multi-path advantage reflection 处理 hard exploration；不能把文本游戏规划直接等同环境动力学，需比较交互/搜索预算 | `AGENT-PLANNING` |
| 2509.24418v2 GSPR | 跨 policy taxonomy 的 reasoning/RL，而非只扩大类别；安全迁移、错误解释、token 成本未核 | `PLATFORM-SECURITY` |
| 2509.24804v1 DyMoDreamer | inter-frame mask 与 categorical modulation 进入 RSSM；需控制动态特征、表示容量及样本预算 | `MULTIMODAL-WORLD-MODELS` |
| 2509.24832v2 SemShareKV | token embedding LSH / RoPE 的近似 KV 共享；语义相似不证明缓存状态等价，误差/位置/成本仍待核 | `INFER-KV-CACHE` |
| 2509.24957v1 DUCHESS | activation probe 控制 terminate/duplicate/continue 与难度调度；须同准确率比较 probing 与端到端 branch 成本 | `INFER-SCHEDULING` |
| 2509.24967v4 SecInfer | system-prompt 多路径采样、target-task 聚合；必须保留自适应攻击、误拒和额外 compute，不授安全保证 | `PLATFORM-SECURITY` |
| 2509.25050v2 AWM | DDPO noisy matching 的解释及 advantage 加权 matching；理论条件/梯度方差/公平预算未审 | `TRAIN-RLHF` |
| 2509.25175v3 EasySteer | vLLM steering 的执行/扩展接口线索；目前框架、模块和倍率不足以证明运行时机制增量或 production-ready，落窗后需窄读决定准入的执行核心 | `INFER-VLLM` |
| 2509.25448v3 LLMPrint | 已发布模型的 optimized injection fingerprint 与 verification；需核统计假设、后处理和误报，不采用“近零”保证 | `PLATFORM-SECURITY` |
| 2509.25598v1 PPR/ReNorm | principle 过程评价和 outcome/process 归一化；局部步骤分数与最终效果须分账 | `TRAIN-RLHF` |
| 2509.25678v4 Interaction-aware MoE | 跨流时间间隔依赖进入 interaction-type routing；有表示机制潜力，不能只因临床场景排除，也不采用临床结果 | `MULTIMODAL-REPRESENTATION` |
| 2509.25689v1 Collaborative Compression | 严格内存下 expert pruning / mixed precision / activation 联合取舍；组合、103GB 或“首次部署”不证明质量/容量边界已成立 | `INFER-TENSORRT-LLM` |
| 2509.25762v2 OPPO | intra-step chunk streaming、inter-step 延后长 generation；需核权重陈旧度、PPO 语义、尾延迟与收敛代价 | `TRAIN-RLHF` |
| 2509.25911v1 Mem-alpha | RL 训练 memory 保存/组织/更新，用全历史下游 QA 奖励；信息损失和长程/训练预算未核 | `AGENT-MEMORY` |
| 2509.26114v1 Clip-Low/High | clipping 自身熵偏置与随机 reward 反证；不能把熵变化全部归因有效奖励，证明条件及探索收益待审 | `TRAIN-GRPO` |
| 2509.23962v1 CANON | 按 entropy/length 重分组、组间/组内 advantage，避免预设单向先验；不采用 Pareto 结果 | `TRAIN-GRPO` |
| 2509.24203v2 Group-relative off-policy | 不预设数据分布的推导、更新正则/数据整形；理论 off-policy 解释不证明任意陈旧采样可用，v2 新实验不回填旧事件 | `TRAIN-GRPO` |
| 2509.24269v1 AdvChain | temptation/hesitation 纠偏而非只模仿完美 CoT；须同时审 harmful compliance 与 over-refusal | `PLATFORM-SECURITY` |
| 2509.24393v2 Corrective Intervention | 最终答复安全不代表可见 trace 安全，替换 compliance 步骤构造 preference pairs；关键步骤/信号归因未核 | `PLATFORM-SECURITY` |
| 2509.25133v1 SIREN | top-p / peak-entropy mask 与 self-anchor 限制探索位置，反对无差别全局熵增；多样性、预算和训练稳定性待核 | `TRAIN-GRPO` |
| 2509.25624v3 STAC | 执行验证的多步 tool chaining、closed-loop 诱导及自适应防御失效；当前 ToolShield/结果不回填 v1，不采用 ASR | `PLATFORM-SECURITY` |
| 2509.26354v2 Misevolution | model/memory/tool/workflow 自更新的安全漂移；经验性反侧不等于所有 self-evolution 必然失效或缓解已有效 | `PLATFORM-SECURITY` |

全部 7 项具名安全潜力与 GRPO off-policy / SIREN / clipping 设计反证已覆盖，未以负面结果、局部实验、Books 已有主题或深审成本缩池。EasySteer 的“是否实际达到机制准入”与一般实验可信度明确分开，未偷偷升为已准入；在日证据恢复前它不承担候选/Evidence/Books 权限。

## 5. NVFP4 与 FP8 撤回/恢复争议

本轮轻量核六页 227 身份的现有 Comments，确认 NVFP4 2509.25149 的 Eq2 typo / 作者与 related-work 更新，以及 FP8 2509.22536 的撤回信号；不把这种有界检查称为所有版本史无纠错。NVFP4 当前纠正公式不能替代 2025 精确事件，原隔离继续有效。

本轮直接打开 [FP8 官方当前页](https://arxiv.org/abs/2509.22536)：L8 当前 v5，L19 仍说明数据处理 bug 使实验/结论不能继续认可；L28 v2 标 withdrawn，L29～31 有 v3/v4/v5 正文记录，页首当前 v5 未标 withdrawn。**返修包将其单列撤回/恢复状态争议，裁决通过。** 不声称全部版本被官方撤回，也不凭后续正文或下载链接宣称已修复。

当前不得准入、评分、采用 lossless/速度/显存等结果或写 Books；它不是普通缺日 held，更不是访问故障。重开须作者/官方明确撤回适用版本、修复情况及对应有效证据，必要时再读受影响实验；无需为证明当前争议存在泛读五个版本或仓库。本轮未发现本日报有该版本的采用链路，无需修改共享 Books；原作者精确检索“未命中”不被扩大成全仓间接引用已审。

## 6. 代表排除与未选月库存抽检

旧 18 项完整题摘贡献关闭中，本轮重新读 **6 项**：TDDev 2509.25297、Move MSG 2509.24515、CDT 2509.24422、dyslexia 2509.24597、TemMed 2509.25143、MMRQA 2509.24888，覆盖 Agent workflow、评价分类、表示扰动与医疗任务。未发现共同错误理由需重开该集合；其余 12 项复用 Dewey 的完整题摘受限校准，不声称本轮重读。

- TDDev / Move MSG 有 TDD、spec 与验证反馈，不是“没有反馈”；当前题摘主要建立既有流程在相应任务的应用，尚未建立新的执行保证、失效边界或可归因控制机制，维持最小关闭理由。
- CDT 的分类、相关性和 data-selection 改善不自动修正评价盲点；dyslexia 的 VWF ablation 是真实机制实验，但其拟保留结论仍限定脑障碍模拟。TemMed 确有时间医学图像推理失败，MMRQA 有 acquisition-aware signal / LoRA 融合，不能删掉这些事实；有限关闭没有把全部多模态或医疗题名排除。EQUISeg 已专门重开，不沿用这种领域关闭理由。

旧标题范围退出抽检 **4/18**：2509.24895 蛋白表示形状、2509.24761 EEG neural representation、2509.24978 physics exploration、2509.24463 higher-voice harmony；只核题名/Comments 的原有限退出，不授其全文已审。October 身份抽检 **3**：2510.00063、2510.02375、2510.02373 AMemGuard；月份不能授具体日，但不能由 September 提交搬入补充窗；后者继续保留安全恢复线索，不被判无贡献。其他标题范围项未重新读完整摘要，未扩成强制队列。

新月库存未选题名不是作者的正式贡献排除。本轮按六主题分层另读 **12 项完整题摘**，不改变作者“23 新题摘”的统计，也不把这 12 项补记为已完成历史 Evidence：

| 样本及实际身份 | 独立检查边界 |
| --- | --- |
| 2509.25848 More Thought, Less Accuracy | visual forgetting / VAPO 的推理与感知冲突不能按负面关闭；保留具体日期/事件恢复线索，不采用效果 |
| 2509.21173 Less Precise Can Be More Reliable | 量化影响校准/OOD/noise 与 covariate shift 的不同反侧应保留，不得概括“量化全面更可靠” |
| 2509.15206 Fair-GPTQ | fairness constraint / rounding 是机制线索，不是只看 accuracy 的量化评价；不采用公平性保证 |
| 2509.24210 BeyondBench | 算法生成、deterministic oracle 与 contamination 解释有评价潜力；巨大实例空间不证明绝无污染 |
| 2509.26345 SafeBehavior | intention / introspection / revision 的安全流程线索；摘要不证明自适应攻击下有效或具有 authority |
| 2509.18382 Safety and Skill Under Compute Constraints | 长度限制/量化/安全取舍是必要反侧，不以降本主题代替安全核验 |
| 2509.26534 Datacenter Lifecycle TCO | build/refresh/operation 联合取舍有系统线索；不采用 TCO 数字，不因没列入 23 就判无贡献 |
| 2509.18284 Improved Modality Dropout | learnable modality tokens / fused contrastive 表示有 missingness 线索，不能仅因 disease detection 题名退出 |
| 2509.25518 Mechanical Thrombectomy World Model | 摘要为 TD-MPC2 在血管导航与 SAC 的领域比较，有限范围样本，不采用医疗效果或推广为新通用 world-model 机制 |
| 2509.22321 Distributed Associative Memory | 原文 agents 是分布式在线优化主体，不因此自动变成 LLM Agent memory；保留 scope 边界，不采用理论保证 |
| 2509.24840 Cell2Text | scRNA-seq 的领域生成/解释任务，未证明通用模型系统差额；不纳入暂缓 AI for Science |
| 2509.23927 FUSAR-KLIP | SAR/geoscience data、knowledge alignment 与组合训练线索；不能只凭领域名宣称无机制，本轮未作正式贡献关闭或采用 |

前 8 项及 FUSAR-KLIP 的未定贡献，不构成被作者错误关闭后必须返修的候选：当前正文明确其余月标题只是恢复库存，并未排除、纳入或采用。本文件保存上述具体反侧与非采用边界；公开日未确认，不纳入本窗分母，不授 Books，不要求清空其他月份库存。其余未选月摘要、全部未请求页和普通附件未审，不能把抽检称全量验证。

## 7. 每日来源与日级终态

14 个到期来源均有现行正文行。未变化原始响应/停止的语义复核复用 Dewey，不声称本轮重新联网或解析全部机构正文；本轮直接核 R2 Qwen、Google 新定位原件及第 3 节 arXiv 差额。

| 来源 | 可接受的实际停止 / 不授范围 |
| --- | --- |
| OpenAI | RSS1251 项与 Sora 初始 card 定点去重；七 case 的有效证据复用，不授整 PDF 首公开/全文或全站零事件 |
| Anthropic | Research174 对象/172 身份的日期切片；Sonnet/Code 具名去重，不把数组当全部 News |
| Google AI | Blog 首12卡止 Sep25、两 Sep30 core；DeepMind 第2页30卡 10/30→09/29 后止，News第5页邻接止；pubs默认1～15/11597、2025计678不是 first-public，未把年度条目逐项排队 |
| Meta | 连接重置与 global_search page5 实际400 Timeout，不把片段当历史列表或零事件 |
| Qwen | 全60配置日期，目标日前后侧已核；未披露历史完备性，隔离不授全站召回 |
| DeepSeek | Research10条跨窗、News目标日前09/29；止当前列表，不授全部仓库直发 |
| Moonshot | Blog11/07、11/06→09/16，止越窗处，不授全部 release |
| Hunyuan | 真API page1/20，en9、zh11，最早2026/02/03；历史2025段未返回，成功响应不等于历史覆盖 |
| Z.ai | Research两页18项末12/07；GLM4.6具名核心有限关闭复用，不补造 Research 历史段 |
| Seed | type1/type2 2025 页0/20，置顶另检、非置顶跨窗后止；94/45不是全文分母，URL不证明locale，PublishDate不重置 first-public |
| ERNIE | Blog两页10+6、终页1/2，10/16→09/12；有限列表，不授全部仓库直发 |
| MiMo | Paper8项09/19→10/21，Blog15项无日期、local More；不能用论文表替代 Blog 历史日段 |
| MiniMax | EN/CN Blog10/27→01/15，Agent仅2026/05/13；Agent目标历史段隔离 |
| arXiv | 实际主题页/月表/API边界见第3节；不能以 submitted、API published、月份或一般排期授 Sep30 公开日；未请求页不默认成为逐项关闭工作 |

有限已检查 6 源、外部必要历史/日证据仍隔离 8 源；数量不是 14 源全 Coverage 通过。GLM 发布核心及两 Google Blog 独立新增事件关闭复用 Dewey；Google 所链论文 2509.18057 / 2508.20148 first-public 未定，不能称确定窗外或原论文已审。

唯一拟保留正式家族的全部必要安全/纠错反侧及 Books 决定保留有效独核。另定点读当前 Ch66“从目标到证据”与 proxy 分账、Ch72“局部合理动作会累积成有害轨迹”和“跨会话分解”正文：原 owner 判断仍有实际承载内容。case 局部观测/自身纠错没有新增通用测量、检测或控制算法，**仅报告**成立，不把它换成只有章节名的“已有覆盖”。没有本任务 Books 修改或新增长期差额需要 POST；23 项的拟 owner 不代表长期差额已证实，不生成伪 Books 提案。

### 精确恢复条件

普通研究待办已由本轮非作者复核关闭。机构必要历史段、Google两原论文 first-public、原75与新23潜力的具体日证据继续作为外部终态保留项；本轮额外抽检中未定相关身份沿相同非采用边界保留。需要含ID与实际公开日期的当期官方公告/列表/快照，或作者/机构可确认精确正文公开日的原件；只核日期，不请求精确时刻。到达后只重开对应身份/事件版本的准入与必要 Evidence，不重新扫描整月或其他日期。

三撤回保持非采用；FP8 按第5节有效性澄清条件而非日请求重开。所有保留项均不支撑正面证据、Books、无遗漏或性能/安全保证。没有把“未读普通全文”称为外部材料不可达，没有用旧失败或90天限制停止有界历史发现。

**作者/root 可以据本文件同步 Oct01 本轮复核为通过、日报状态为完成；无需再请求一轮对未变化内容的语义复核。同步是作者维护工作，本复核文件不代写或证明它已执行。只授 Oct01，不授任何其他日、Weekly 或月度完成。**

## 8. 写后检查

本轮已实际运行 Oct01 V3 Report 校验：1 份通过，明确只证明接口一致性，不替代上述语义裁决。旧窗口/补充窗口/候选整行的只读冻结比较通过；新增文件前已确认指定路径不存在，不覆盖旧复核或原件。

本轮唯一新增/修改工作区文件为本文件。只读 Git 不调整已有 staged/unstaged 内容；未 stage、commit、push 或执行其他 Git 写操作。

写后检查时间：2026-10-07T17:21:06+08:00。已读回裁决与范围；5 个本地引用目标全部存在，23 项校准行与 14 来源行数量准确。新文件对空文件的 `git diff --no-index --check` 无空白诊断（新增差异返回 1）；指定复核文件为未暂存新文件。作者 README 仍保持原来的 MM 状态，本轮没有代改或暂存它。这些检查不扩大语义、来源或外部保留项权限。
