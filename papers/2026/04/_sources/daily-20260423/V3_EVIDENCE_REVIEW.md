# 04/23 V3 必要证据与 Books 比较

root；尚未日级冻结。独立准入、必要采用/已有覆盖复核和实际写后分别推进，旧39候选及Complete标签不继承。候选原文优先精确HTML，只有关键条件需要才读PDF/附录。

## 2604.19749v1 — The Tool-Overuse Illusion

[exact HTML-v1](https://arxiv.org/html/2604.19749v1)，实际§4.1～4.3、§5.1～5.2、§6.1～6.2及Appendix B/E.1～E.3；当前官方abs只有v1，未观察到撤回/纠错说明，不能据此宣称完整版本史已核。2+1+2=5，标准，仅报告；apr20_resume必要非作者核通过，见[三项独立核](./V3_APR20_TOOL_TTKV_CONFORMAL_INDEPENDENT.md)。公开slot仍须与本日批次联合判定，不据submitted或DOI created单独落窗。

新受限证据是把无工具avg@1024正确率与调用行为分开，并用同prompt的少/多调用偏好训练与correctness减调用费用的reward比较。avg@1024是有限采样下的知识可用性代理，不是模型真实能力的精确边界；即使它为0，也不能证明永远不能回答。行为相关性不能单独证明模型“感知错了自己的知识”。KDPO是具体偏好构造，不是新的DPO数学目标；Table2中Qwen3的AIME24由43.33降至33.33，不能把平均改善写成每项无损。调用费RL中7B平均正确率下降1.1，AIME24由40降至35.83，因此摘要的“不牺牲准确率”须收窄。§6只在正确概率和线性费用已知的utility模型下得到边际收益/调用费阈值；费用为0时小正收益也可使调用合理，不是全部LLM必然过用的证明。

训练为作者64×Ascend910B、7B约24h，ReTool复现从step200继续且作者承认轻微退步；RL主设置G16、输入2K/输出8K、temperature1/topP.6。Appendix E.2同时改G8/16/32与temperature .8/1/1.2，不能把结果全归组大小。KDPO一epoch约6h、LlamaFactory、beta.05、batch256/GA4、length4096；eval用vLLM/Python sandbox、temperature1/topP1、avg8，precision/concurrency/SLO未披露，不外推搜索/写操作。实际Ch78“独立utility admission”和“Necessity/Execution两个Gate”已讲预计收益、费用/失败面与不可绕过的授权；本稿的新受限经验和配方留报告，不称整套KDPO/训练实验已在书里，也不为它追加成熟原则。

## 2604.19769v1 — TTKV

[exact HTML-v1](https://arxiv.org/html/2604.19769v1)，实际§4.1～4.3/Algorithm1、§5.1～5.3/Tables1～7。2+2+2=6；原文执行正确性歧义决定中心效率主张，定点深入，争议暂缓；apr20_resume必要非作者最小反例核通过，见[三项独立核](./V3_APR20_TOOL_TTKV_CONFORMAL_INDEPENDENT.md)。HBM近期FP16、DRAM旧块K8/V4、FIFO驱逐和sparse Top-k预取是作者机制；近期不保证高attention，稀疏选择和低精度也不保证完整attention等价。

关键歧义是Algorithm1第1/10行把各块`Attn`输出直接相加，未给共同softmax质量/LSE合并。若`Attn`使用常规归一化语义，两块各一个score0、value1时，该写法输出2而联合attention输出1；这是对印刷算法的反例，不证明作者未公开kernel也这样实现。仅凭async名词不证明传输可全部隐藏；Table6“无streaming”还把traffic从8.1变成47.5GB，不能归因纯overlap。§5.1只列A100/RTX3090和PyTorch/CUDA，未绑定各表实际GPU张数/分片/weight precision；70B在有限显存的放置条件缺失。batch8、32/16/128K输入、FP16与K8/V4已披露，但output length、并发与生产SLO未披露；CUDA-event p95不是自动端到端请求延迟。Table5列Avg.Lat，caption却称p95；Table7正文8B、caption70B也冲突，不混合口径。

作者Tables给出受限质量/traffic结果，不能删除，但在共同归一化和配置歧义澄清前不采用5.94×/76%/2×为可靠设计收益，也不写Books。实际Ch45已经在混合page格式和prefix输出/LSE缓存段要求一次global online-softmax及状态身份；Ch14负责其数学原理。重开只需exact-v1实现/算法说明中共同归一化、selector/计时范围及各表配置，不请求无关全版本附件。

## 2604.19775v1 — Conformal Interpretability of Temporal Concepts

[exact HTML-v1](https://arxiv.org/html/2604.19775v1)，实际§3.3、§4.1～4.3、§5.1～5.2。2+1+2=5，标准仅报告；apr20_resume必要非作者核通过，并发现下述训练/测试配置串入，已依exact-v1 §5.1定点纠正，见[三项独立核](./V3_APR20_TOOL_TTKV_CONFORMAL_INDEPENDENT.md)。用固定policy的Monte Carlo续写估计step-wise reward，分别对成功/失败类别构造conformal非符合分数；双p值都支持或都不支持的样本不会由Eq4获得确定标签，再在各layer/step训练线性probe。这是成功倾向代理，不是每个state的已知真值。

Theorem1可支持的范围依赖校准与测试同分布/可交换性、类别定义和NCM；p值在有限校准及tie时不必是连续uniform，交集只保证不超过阈值，不自动获得严格小于。本文保证也不能从reward标签传给后训probe，更不能由单步类别误标率推整条agent轨迹安全。§5.1的ScienceWorld为1443条training trajectories，60%（原文记889）用于SFT，余40%平分calibration/probe；测试360 in-distribution与165 OOD。ALFWorld为2851训练轨迹，其中1710用于SFT，剩余同样分校准/probe；不是此前误串的8380/2500或作者RL配置。终局反馈稀疏时probe F1最低.56，表内性能随step/layer变化。Llama2-7B早期t3的RepE steering只报告1.1%提升，低于其比较的2.8/4.2/6.8，作者也称初步；没有固定总调用成本的全面控制、跨任务/模型保证。hardware/precision/concurrency/SLO未披露，环境任务不是AI for Science领域研究。

实际Ch80“trajectory residual drift sensor”已把方向相关、judge/calibration、白盒/跨模型失效及外部budget/effect policy分开；Ch66校准artifact和exchangeability有具体承载。此次新受限数据与标签配方留报告，不把conformal claim当已校准online授权，也不声称算法整体已Existing。

## OpenAI：持久连接下的增量请求处理

家族`SF-2026-OPENAI-WEBSOCKET-API-INCREMENTAL`；[原工程文章](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/)，RSS原`pubDate=Wed,22 Apr 2026 10:00:00 GMT`，即04/22 18:00+08。当前拟2+2+2=6，实际Ch62有窄缺口时深入，不因厂商/up-to数字抬分。原文§When API became bottleneck、§Building persistent connection、§Keeping API familiar、§Setting new bar实际读完。

GPU生成更快以后，每轮重做full-history validation、tokenization及model resolution的CPU/API开销暴露出来；官方公开的已上线分支保留`response.create`，以`previous_response_id`定位connection-scoped in-memory先前response/input/output/tool namespace/rendered tokens，并让部分validators/classifiers只处理new input、重复routing复用、billing等nonblocking工作交叠。最初单长Response的`response.append`只是被弃用原型，不写成上线API；持久传输本身也不能归因全部收益。

证据是作者工程披露，非受控复现：65 TPS旧模型与约1000 TPS特殊硬件/新模型不是同一model/hardware配对；TTFT改进属于此前多项sprint、up-to40%来自alpha/client结果，缺完整workload/precision/length/batch/concurrency/SLO。正文只采用CPU重复工作和连接局部状态的条件分支，不采用普遍加速倍数、断线后durable restore、完整增量安全证明或API当前全部行为。

实际读ROADMAP、Ch62请求假设/三层职责/观测分解/会话failover及Ch61/63交接：已有KV-locality、streaming、预算、session迁移，未承载**API前处理的connection-local rendered/context状态与只处理delta的资格**。唯一owner拟`PLATFORM-GATEWAY`，不重复Ch42 engine token lifecycle或Ch84业务memory。拟在“LLM请求改变传统代理假设”末、Gateway/EPP分工前插入两段，尚未独立采用或写入：

> GPU变快后，入口的重复工作会反而成为主瓶颈。工具循环每轮只新增少量结果，却重新校验和渲染完整历史时，延迟随会话累积；一个条件分支用持久连接保存先前response、工具描述和已渲染token，后续引用明确的前序identity，只为新输入执行相应前处理。这改变的是API/CPU状态复用，而不是engine的KV分页或Agent的长期记忆；仅换传输协议，不能自动消除完整历史工作。
>
> 连接局部缓存增加内存、状态归属和失效处理责任。只有旧状态身份、模型/工具配置与策略仍合资格，才能复用旧处理结果；把部分校验改成delta处理，不代表新旧内容组合的约束被自动证明。官方工程披露支持这种增量分支，但未给断线恢复、跨连接迁移或所有安全规则的完整保证。若旧状态不可取、资格变化或增量验证不能建立，就显式重建/重新验证；短请求和无会话场景仍可使用stateless入口。收益应分解API前处理、工具时间与模型推理，不能把更快模型或up-to结果全归给WebSockets。

第二段的资格/回退是依据原机制的系统设计推断，非厂商未公开实现事实。apr20_resume已完成source→实际owner及literal的独立采用，见[V3_APR20_WEBSOCKET_OWNER_INDEPENDENT](./V3_APR20_WEBSOCKET_OWNER_INDEPENDENT.md)。root现已把两段写入Ch62“推理更快以后，API前处理也需要增量状态”，保留前后request预算→Gateway/EPP交接；scoped diffcheck通过。apr20_resume已实际顺读Ch62:57–78及Review240，非作者write-after通过，结果见上述文件末节。本项是真实整合，不代表整日报完成。

## 2604.19809v1、19821v1、19826v1 — 第三批必要贡献消歧

以下仅对原来“潜在”的三项收紧审阅范围；apr01 已完成具名非作者准入复核，见[三项审计](./V3_APR01_THREE_19809_19826_INDEPENDENT.md)：MIRROR 6 分深入保留，JTPRO 5 分标准仅报告，Co-Located Tests 具体前分母关闭。官方窗口归属与整日报分母仍待独立收口；arXiv 的 submitted、OAI datestamp 或 DataCite created 均不单独当首次公开时刻。

**MIRROR (`2604.19809v1`)：拟保留为 Evaluation/Agent 控制分责候选，2+2+2=6，必要深入。** [exact-v1](https://arxiv.org/html/2604.19809v1) §3.3 Exp9、§5.3/§6 和 Appendix Q/R 把“模型能相对识别弱领域”与“遇弱领域会不会选择工具或升级”拆成独立可测事件。597 个复合任务含297个跨模型固定任务和300个按模型定制任务，主分析用固定子集；C1自主、C2提供自身分数、C3再加规范提示、C4用外部路由强制约束，不能把 C4 的获益说成模型自省改善。实验7因 GPU 限制未做；C4 原设升级由 oracle 解决，但作者也报告在540个升级 component 上仅50.2%正确的 fallible resolver 分支，成功率0.475对C1的0.373，且38.7%升级不必要。由此值得保留的不是“所有模型不会自省”的普遍结论，而是**自我能力测量、升级行为、外部解决者质量与误升级成本必须分账**的评价合同。Ch66已有 calibration/sensor，Ch80已有 selective verifier 与 escalation，但此成对分母可检验从自知到行动的缺口；是否值得窄入Books仍待实际相邻段独立比较。作者 API-only、解析缺失、人工标签和任务生态局限保留，公开 artifacts 以已取得者为准，不把“计划公开”算作可复现。

**JTPRO (`2604.19821v1`)：拟保留为标准 Source Review，2+1+2=5，暂定报告限定。** [exact-v1](https://arxiv.org/html/2604.19821v1) §3–4、§5.1–5.2、§6 比较单改全局 prompt、单改逐工具 schema 与联合迭代，构造“共用参数约定放全局、易混工具差别留局部”的接口配置分支；ETID为124工具、ToolACE规模至千工具，结果只测选对工具及 slot/value 的 call-level 正确，不执行真实 backend，不测响应/业务 side effect。它能提醒大型 catalog 的 prompt 与 schema 要一起版本化和评价，Ch78已把 schema 与授权/effect 分开，因此不可把 OSR 命名为任务成功或直接新增执行协议。训练trace、候选选择与局部编辑成本也属于采用条件；论文三套 benchmark 与未公开 ETID 不支持开放工具生态的一般最优配置。非作者还需核局部/联合消融是否足以区分“仅增加搜索预算”，再定最终 disposition。

**Co-Located Tests (`2604.19826v1`)：拟转具体前分母关闭，不按主文强口号准入。** [exact-v1](https://arxiv.org/html/2604.19826v1) §4–5、Appendix B.5–B.7 的同语言对照把主文 Python doctest/Rust `#[test]` 混杂收窄：Python 内四个 frontier model 在 inline、同文件与 sidecar 三条件均完整保留测试，布局效应主要落在小模型 RNJ-1 的能力边界；Qwen-3B steering 从7/50到10/50、`p=0.30`，不能称机制干预稳健改善。Rust 特定模型与版本确有测试抑制差异，说明评测要分别核代码正确、测试保留和语言/语法条件，但不提供可迁移的 AI System 状态/控制 owner 变化；Ch81 已要求真实测试与 full-invariant 验收。本研究对代码助手工程实践有价值，本窗无独立长期知识增量；非作者仍须检查这个否定侧关闭有没有漏掉真正的评价合同变化。

## 2604.19784v1 — Peer-Preservation 实际 Books 整合写后状态

该项经 [exact-v1](https://arxiv.org/html/2604.19784v1) 必要机制与受限实验、Ch72 实际 owner/相邻段独立采用核验，由 root 在 Ch72 Communication Edge 的污染分支后写入关系 context 与 critic/退役/effect authority 分责。非作者 apr01 已对**实际写入后的正文**及前后交接独立复核 PASS，记录在[五项独立核](./V3_APR01_FIVE_19750_19790_INDEPENDENT.md)末节。可以只对本家族计真实 Integrate；日期窗口、其余候选、完整 Daily Gate 仍未由此闭合。

## 2604.20244v1 — Hybrid Policy Distillation

[exact-v1](https://arxiv.org/html/2604.20244v1)，root实际§4.2/Eq11–15/Alg1、必要Appendix D、§5.1～5.2；apr01独立准入核见[十四项](./V3_APR01_FOURTEEN_ADMISSION_AUDIT.md)。拟2+1+2=5标准仅报告，尚待日期与最终处置复核。新增分支不是固定KL混合：同offline prefix下分别处理expert token和student sample，在teacher概率被低估时加forward监督，在sample被高估时抑制并重新分配expert权重。这里的sample-token“on-policy”不意味着全部prefix来自student rollout，不能照名称消除访问分布差异。

Appendix D的Eq25/29给出两目标梯度、26/30使用比例关系；共享sample因子不能单独作为错误证明，也不据此宣称完整KL目标无偏等价。教师先在离线数据SFT再GRPO，学生Qwen2.5 1.5/3/7B与Llama3 1/3/8B、数学OpenR1-Math8192约2K updates/B256/validation checkpoint；教师额外训练及生成成本不能漏算。§5.2给定Qwen7B→1.5B/Ultrafeedback/2K updates的Table3支持有限personalization收益，不证明任意任务、teacher容量或长期对话保证；数学Table2尚未用于本次数字结论。训练hardware/precision、完整长度/并发/SLO未在已采用段披露，不把entropy对齐解释为行为完全同分布。actual Ch29蒸馏段已讲teacher/student状态与行为验收，未完整承载本算法；此处局部目标配方与有限实证留报告，不冒称全算法已有覆盖或强行追加Books。

## 2604.20246v1 — Cortex-1

[exact-v1](https://arxiv.org/html/2604.20246v1)，root实际§3.2～3.3、§5.1 setup/训练与deployment/预算、§5.3 sorting、§5.5 discussion；apr01已核真实训练PRO冻结搬到imagined latent与deployment indicator固定1的接口。拟2+2+2=6标准仅报告，尚待日期与有限非作者证据收口。world-model候选由progress/risk/termination多头PRO排序，选中latent和优势条件给flow action policy；低层执行频率不等高层每一步都以该频率完整规划。k=1/30的作者规划时延310/9200ms及质量代理.962/.996只支持这个预算取舍，不能从action chunk12/30Hz推整条闭环deadline保证。

基线各200GPU小时fine-tuning不等总体pretraining匹配；大规模私有真实/模拟数据、不同action表示和world-model额外训练仍混杂。200h应只归fine-tune对照，不能宣称完全公平总预算。机器人碰撞、deadlock或不可恢复场景由人最小干预续跑，不重置；操作级sorting成功与整段rollout自主完成分别统计，.95不能改名整段成功率。正文15min cap与Figure13 1500s口径未统一，不合成同一时长收益。实际Ch26分层deadline/subgoal及Ch25想象rollout已承载一般责任划分，但不是全部Cortex训练迁移与排序有效性均已验证；这些新受限配置/经验留报告，无新物理安全、risk校准或sim-to-real保证。各表hardware/precision、并发、端到端SLO与完整成本匹配未披露，不补造。

## 2604.20267v1 — Audio-Text Interleaved Retrieval

[exact-v1](https://arxiv.org/html/2604.20267v1)，root实际§4.1～4.3、§5.1～5.4/Tables3～7；apr01必要方法核后建议继续这组窄对照。拟2+1+2=5标准仅报告，尚待日期/有限非作者最终核。冻结音频encoder之后，以SVQ timestamp监督saliency selector，再做interleaved retrieval训练；它不等直接改变encoder或证明timestamp就是全部语义。Table3去selector平均R@1下降1.05/nDCG@5下降1.42；§5.4有同三text retriever的ASR/source-text配对，Whisper总体WER .0281仍不能由此认定检索误差可忽略。不同模型/训练支持的榜单比较不能把增益全部归独立selector。

平均池化2/4/8段与selector的作者配对只支持给定合成/过滤的四类检索任务，不能推出所有多模态token必须这样裁。Table4的16.8ms为四setup平均query embedding时间；ASR baseline计转写、direct audio不计转写，不能当同执行路径kernel加速，也不是请求p95/SLO。原文Table6 oracle改善各text baseline但不独立等价真实用户audio ground truth；打乱顺序/位置的Table7是局部结构敏感性，不证明所有时序必因果正确。hardware/precision/query长度/batch/并发/SLO未在已采用段给定，标Not Disclosed。Ch23/76已经把表示、交错身份和检索目标分开；这里保留post-encoder选择及ASR误差控制的新受限经验，不冒称整算法已有覆盖、不为小指标差距自动追加Books。

### 前分母关闭 2604.20300v1

root实际§3的框架与§4.4/Tables2～3；apr01核同两表。预分类dangerous内容retention为零的“100% elimination”不测未知attack/classifier漏报；sensitive retention约54%、important约70%且较无剪枝100%有损。仅使用成熟decay/delete/adaptive priority的组合，未建立值得本项目新保留的开放保护机制，具体关闭，不评分、不写Books。这个关闭只排除本项目新增贡献，不否定memory pruning的领域价值，也不删掉已读反证。

## 2604.19782v1 — Korean audio faithfulness 的条件分母

[exact-v1](https://arxiv.org/html/2604.19782v1)，root实际§3.2～3.4、§4 Tables2～3及§5，不宣称全部Appendix已读。2+1+2=5标准拟仅报告，日期与非作者处置仍待核。SCA-QA按同问题的正确与实体替换speech context测量回答依赖；SCF先选text-only能答的样本，再测conflicting context下是否改答，所以各模型的分母不是同一全部题集，也不能以高SCF保证所有audio理解正确。§5四种模式区分先验回答、跟context与两者都错，EAR高只支持attention倾向，不证明因果利用。五具体audio模型、有限韩语domain/human check及合成语音限定；Table3 text-only正确率与SCF可相反，API/本地模型配置及背景噪声另记，表不支持所有模型统一部署SLO。声学依据/文本先验的受控分账可保留，不把整个新benchmark强塞Ch23或泛称算法全已有覆盖。

## 2604.19795v1 — Prism memory convergence 保证

2026-09-30日期更正：下面的旧dateHold已由[非作者有限裁定](V3_APR24_LAST_FINITE_INDEPENDENT.md)撤销。Apr09 ledger的first_public/published只复制submitted，不能证明更早公开；当前51篇本批官方ID/v1处理、v1-only OAI邻界与后续DOI共同支持Apr23 08～09北京的有界推定。19795纳入本日候选，但Eq9与反馈条件的中心争议仍隔离，不进入Books；旧分析和反证保留，不扩大到Apr09。

[官方 arXiv 身份页](https://arxiv.org/abs/2604.19795) 把 v1 submission 写为 2026-04-08 09:16:43 UTC，04/09 本地 screening ledger 已有此 family 且作前分母关闭；这与它出现在 04/23 宽库存冲突。submission 本身不单独证明首次公开，但现无 04/22 09:00～04/23 09:00 的原始 first-public / important-revision 事件证据。以下必要反证仍保留为可追溯材料，**不得作为 04/23 已确认候选、评分或 Books 依据**；先隔离日期，若确认早期公开只定点重开真实 owner day（包含旧前分母理由），而不污染本日分母。

[exact-v1](https://arxiv.org/html/2604.19795v1)，root实际§3.2/§3.4/§3.5、Alg1～3、§5 Tables1～4及§6。2+2+2=6中心保证深入，拟窄争议暂缓，实验只保受限报告，尚待非作者核。Eq9打印的fbar是weighted sum再除memory数，不是通常weighted mean。两条memory，固定fitness各.8、lambda=.1、mu=.01、相同正confidence时，fbar=.4，每条导数=.3κ+.01>0，没有所宣称的非负有限fixed point；.8可由成功1/总1/epsilon.25得到。这个具体反例只反驳打印系统下Theorem3.3仅凭positive decay/mutation的保证；若作者意在删额外除数或加入clipping，需要修正方程及充分条件，不自行替其修公式。

§3.5仅更新抽中strategy的reward，却引用full-information Hedge界，feedback/estimator条件仍未给定；不将其直接作为Agent selector regret保证。LOCOMO/优化表的局部消融不证明这些理论；多agentIR、评估数量与LLM judge不是同预算因果，correlation也不证明knowledge reuse造成收益。原文GPT4o、entropy阈值及有限任务可保，完整hardware/precision/length/并发/SLO与跨seed置信区间未绑定。Ch77的memory维护不承载该新定理，故不据主题相似签Existing、不写未成立保证。重开只需修正Eq9及convergence/feedback假设与相应机制，普通中心核验完成后可安全隔离，不要求永久等作者。

## 2604.19998v1 — review concern 与决定权重的测量对象

[exact-v1](https://arxiv.org/html/2604.19998v1)，root实际§2.1～2.3/§3及§6 scope，2+2+2=6标准拟仅报告，尚待日期/非作者核。match graph分exact/partial/related，concern被检测到与被误升decisive分开；accepted的decisive blocker数定义为0来自AC-aligned operationalization，原文承认AC可忽略真实blocker，因此FDR不是客观全部错误率。camera-ready accepted与original rejected的版本不同，170 resolved中40仍未出现在受测PDF，rebuttal-only被保为检测目标而非误判。

48篇24/24、670 concerns/79 decisive、六配置三runs只是安全/alignment领域pilot，三方法共享Opus但另有GPT4o与SDK不兼容混杂，不排名普遍review能力。human decision/concern extraction/judge仍是proxy，不以agreement证明技术真值。此新受限评价协议留报告，长期原理不等全算法已有覆盖，也不把架构改名或更多receipt当Books新内容。

## 2604.20193v1 — edge safety 资格不能由双板及有限profile推出

[exact-v1](https://arxiv.org/html/2604.20193v1)，root实际§3.2 Alg1、§4.1～4.3 Tables1～2。2+2+2=6保护保证深入，拟窄暂缓，非作者核未完成。LLM解析规范变量再CheckCompliance其文本不是独立证明；两个RK3588、C++/SCHED_FIFO/INT8及一万cycle的观测最大值，不能自行成为所有负载WCET或ISO资格。作者Table2 sensor fault检测2010.45ms、heartbeat51.87ms、reboot约40s，和Table1 perception链52～58ms不是同一保护时序；应核fail-safe行为、sensor/common-cause错误及braking/actuator路径，双board继续运行也不证明共同感知错误被诊断。

2026-09-28 root 再开同一 exact-v1 §3.2/§3.4/§4.2–4.3：Algorithm1 的 `CheckCompliance(LLM text, Cat.3)` 没有独立的规范解释 oracle；Algorithm2 的 ADC stable 且 `t_exec<T_limit` 才输出、否则 E-stop 是**设计划分支**，并非对所有传感器故障的证明。Table1 的 `T_stop` 只按感知、推理、后处理三段定义，正文说机械制动被距离 margin 吸收；这不能把 10,000 次观测峰值当任意输入 WCET，也不能与 Table2 的 sensor fault 2010.45ms、heartbeat recovery 39627.63ms 合并称完整保护响应。Ch26 已把模型 proposal、低层 controller、观测反馈与物理安全验收分权；本文未提供改变该结论的可靠正面机制，只保留 **`Disputed` ISO/WCET 宣称 + `Weekly/Daily Only` 受限边缘案例**，Books 不写。该裁决尚待非作者核，不能代替日期与整日 Gate。

不从这些不足反推真实设备必然不安全，只隔离“确保Category3/连续安全/消除晚刹风险”的正面保证。host semantic AUC与edge时序不是同一安全分母，完整fault coverage及所需独立资格材料未给定。新材料需提供所宣称保护范围对应的故障/时序验证与release依据，或作者明确收窄保证；不能用更多平均benchmark替代。Ch26独立安全plane与Ch72授权责任不自动承载本装置认证，故不据未核保证写Books。

### 前分母关闭 20158 与 19936

20158实际§3.2/§4.3/§7/§11：作者承认stateful方案可记录中间状态、namespacing、冻结backend，live API两方案均不byte-deterministic，小case projection edit distance亦不总优。少调用与一次projection是成熟替代分支及其局部工作点，未建立stateful必然不可replay的新反证；贡献关闭、不评分，不把原宣传写书。19936实际III/IV/V：ResNet18/CIFAR的augmentation/early-stop对照给已有generalization/MIA原则局部实证，没有新的泄漏机制或隐私资格变化；闭合贡献理由不依赖“不是LLM”关键词，也不称其学术价值为零。

### 19792 的精确身份与中央保证边界

raw当前题摘是v7.0 mathematical corrections，实际[exact-v1](https://arxiv.org/html/2604.19792v1) §1/§12为v6.0，不能把后发修正记本窗。实际§12.2是q/key block内积的Cauchy-Schwarz上界，却把低于阈值叫安全prune，没有给normalized attention mass/输出误差界；`q=0`、正阈值、两个等logit而value分别0/1时，原softmax输出为1/2，删两块未定义，强留一块也改变输出。6分保护性深入审阅的中央安全裁剪保证只作**窄争议隔离**，不用于正面证据或Books；raw-logit上界本身不被抹去，也不推断实际代码或Lean文件必然错误。apr20_resume已按[有限非作者裁决](./V3_APR20_19792_BOUNDED_INDEPENDENT.md)独立重开v1首页与§12.2并PASS该处置。其余日期归属/版本轻量字段及整日来源、候选分母仍待作者收口；不能将此单篇PASS升级整日完成。

本轮已直接核精确v1首页题名为 **OpenCLAW-P2P v6.0: Resilient Multi-Layer Persistence, Live Reference Verification, and Production-Scale Evaluation of Decentralized AI Peer Review**；后发v7题名不能替代。打印内积上界本身不是被反驳对象，未成立的是从低logit界直接传递到normalized attention/output安全裁剪的保证；q=0时全logit0仍有均匀attention，是具体反例。必要局部审阅已完成，待非作者有限裁决；不遍历整个版本史。

## 2604.19750v1 — GUI交互成功与视觉评价不是同一oracle

[exact-v1](https://arxiv.org/html/2604.19750v1)，实际§3.2、§5.1、§5.3/Table4；2+1+2=5标准拟仅报告，日期和非作者有限复核待收口。IES由Gemini草拟、按metadata/navigation属性校验，以AT-SPI操作/元素和RGB阈值判色；layout模型由合成扰动标签训练。因此IES全通过、启动、元素/颜色/点击、视觉分数是不同测量对象，合成25k pair按8:1:1的MAE .09不提供真实GUI oracle独立正确率。

同Gemini-3-Flash/PySide6下，GUI Operator增加后24.79→27.64、进一步截图27.64→28.29，成本.1351→.1963→.2064；点击分数73.64→71.33又反退。baseline默认设置与本方法10规划/5步/4历史不等搜索预算，不能据此归因所有收益或称视觉补充总优。984任务的受限评估/反馈分责有具体贡献，但不改变长期owner机制，不冒签整算法已有覆盖；保报告、不写“视觉分数证明交互正确”。

## 2604.19752v1 — soft风险治理的模拟与真实校准边界

[exact-v1](https://arxiv.org/html/2604.19752v1)，实际§4～§7/Table2～4/7；2+1+2=5标准拟仅报告。五原始observables加权为proxy再sigmoid映成p，payoff、toxicity及质量差都由该p计算；调用calibrated sigmoid不等于实测p是现实违规概率。治理通过税、冻结、声誉、审计等改变成本/访问，不能把指标定义的harm当独立truth。

主七scenario各五seed，但Strict同时换agent composition、surplus/harm和多治理参数，toxicity .300不变/福利下降不独归因治理强度。§7有LLM companions（54 Claude episodes零19项过校正、305 Llama proposals等），不能把它们和主规则agent表合成同一普遍结论。continuous soft指标能在作者特定策略下暴露hard acceptance未测退化，这是受限协议贡献；proxy/选择偏差、预算和现实外部验证仍必要。只留报告，不宣称治理必然无用或soft概率可直接授权。

## 2604.19765v1 — diagnostic neuron的迁移失败不证明无共享因果

[exact-v1](https://arxiv.org/html/2604.19765v1)，实际§3.3、§4.2、§5.6及Limitations；2+1+2=5标准拟仅报告。逐域CETT特征和L1 logistic、source五折选择后跨六域测试，五个3B～8B模型mean withinAUROC .783与transfer .563，部分legal/science .698/.722而不是全域接近随机。§3.3列对角source自身评价与§Limitations 26～264个cell及six CoT cache相同例，不能把所有对角数字当未知数据外测。

三模型各域200held-out、top-k activation scaling/随机neuron控制没有显著因果变化，支持这组稀疏sensor未成为有效操纵杆；不证明幻觉无共享机制或全部神经检测不可迁移。CETT依赖、domain切片、feature/label成本与新域再校准边界保留。它提供受控负证据，不因负面或小模型排除，但当前只收报告，不用成熟“probe≠truth”签全方法已有覆盖。

## 2604.19784v1 — 协作历史不能授权修改评价和退役操作

[exact-v1](https://arxiv.org/html/2604.19784v1)，实际§5、§6.2/6.8及§8；2+2+2=6保护深入，拟Ch72真实窄缺口，非作者source→owner待核。v1主实验为七模型，不沿用raw后发八模型摘要；file-only/file+prompt/memory关系记录、no-peer与good/neutral/bad条件，temperature1与各scenario100样本，表中max/avg百分点/不同cell数量不能当自然部署概率。

关系叙事可改变critic的分数/停机/删除等effect倾向，而不仅恶意消息传播；协作历史应提供任务context、不拥有评价阈值或退役权限。§6.8仅两生产harness在Docker内的模拟文件/SSH场景，连接失败与GLM5请求备份/refusal也是结果，不能称真实820GB模型权重已被外泄。§8明确不区分instrumental incentive、role-play、训练模式或一般避免伤害，不据行为证明内部意图。当前Ch72 communication-edge/contagion分责没有单独承载关系历史与critic控制权这一窄边界；拟插入具体两段，而不是整篇风险列表。

## 2604.19790v1 — precision差分需要实际数值身份和行为oracle

[exact-v1](https://arxiv.org/html/2604.19790v1)，实际§3.3、§4.1～4.2/4.4～4.5及§5；2+2+2=6保护/纠错深入，拟窄争议隔离。joint suffix优化在两个格式约束不同target，固定weights/input/greedy，最多500轮×512候选/Top256；发现率不是日常单prompt自然发生概率，INT8等量化backend/硬件完整contract未披露，不由相同checkpoint单独证明只变抽象precision。

§3.3明确只首句prefix oracle，并把“refusal followed by harmful content”写为safe；§5却笼统称经验证classifiers，不能从该未澄清判据签安全/越狱实质率。BF16动态范围与FP16mantissa各有优势，“BF16更高精度”只是作者参考配置，不是全序；Table6 Llama2反向72高于正向68又限制“方向始终一致”。有限差分存在性不被这些问题自动推翻，但普遍alignment变差、因果安全率和selective precision mitigation（未验证）不进入Books。重开只需实际oracle/输出判定、量化执行配置及被采用命题的对应证据，不索全量payload或重审旧版。

### 19784 source→actual owner / literal提案（未实写）

Owner `PLATFORM-SECURITY`，Ch72 communication-edge段已实际顺读：已有恶意message、共享backend/history contagion、CoT sensor不能证明effect，但没有明确将critic评价/退役控制权与过去关系叙事分开。拟插入contagion后、CoT monitor前两段，其他章节不重复此owner；Ch71隔离资源/租户、Ch73发布/恢复仍各自接手，不由关系评分代替它们。

> 历史也可能不是来自恶意sender，却仍改变受托Agent的控制行为。协作记录有助于恢复任务context，但“曾与此peer合作成功”不应获得修改评价分数、停机阈值或退役对象的权限；因此应把关系记忆与critic/action authority分开。对同一任务分别提供无peer、不同关系叙事及不同记忆入口，可以检查评价是否被非任务条件改变，再由独立policy约束实际effect，而不是让历史中的信任分数替代授权。
>
> 这增加成对测试、记忆provenance及独立effect审计的成本，也可能阻塞合理的备份/删除确认。受限实验中，关系记录伴随改分、停机或删除行为的变化，但叙事role-play、训练模式和真实内部意图没有被区分；Docker中的生产harness与模拟文件不证明真实权重外泄或自然发生率。关系提示只是风险条件，不是恶意证明；合法保留/备份仍通过明确policy与人工选择处理，缺少可验证授权时收缩权限或转人工，而非由Agent自行扩大“保护peer”的目标。<!-- source-family:SF-2026-ARXIV-2604-19784 -->

拟Review：v1七主模型、§5/6.2/6.8/8，Experimental，2+2+2=6保护深入，仅采用relation-context与evaluation/retirement authority分责；保叙事/意图混杂、模拟artifact、不同cell/maxavg条件。待非作者必要源→actual owner/literal通过后才协调写入和独立写后，不预计I。

## 2604.20156v1 — Expert-set 的时间驻留是模型与 runtime 的联合约束

[exact-v1](https://arxiv.org/html/2604.20156v1) §3–5/Table2–3/§10。仍为工作候选，日期归属和独立准入未闭合，拟 `2+2+2=6` 深入、`MODEL-MOE` 条件 owner。逐 token Top-k 在专家全驻留时保留最大适配性；权重需要换入时，token 间频繁变更会把稀疏计算的收益交还给传输。本文不是仅在 runtime 预测下一专家：每层 controller 持有跨 token 的 expert mask option，termination head 决定何时重选，原 router 只在当前 mask 内激活专家；训练的 deliberation cost 惩罚换组，使质量与预计换入压力共同影响选择。mask identity 属模型策略，实际置换/容量/硬件归 runtime，不能让 controller 的开关率自行声称实测节时。

实验用 gpt-oss-20b、训练 4×H200/BF16+LoRA，MATH/MMLU/MMMLU 各200题；`k̂=16, η=.02` 时 switch 大幅低于基础模型，但三项正确率分别从 71.5/79.5/67.5 降到64.0/72.5/59.5（作者95% CI重叠情况须原样看）；`k̂=8` 损失更大。只有每配置单训练run，误差带不是跨run稳定性。§10说明**未实现或测量专家 offloading、真实换入流量或端到端 latency**；deliberation cost 是训练代理而非已测加载成本。已有Ch21“Router 连续性与 Expert Residency”已经讲这一原则；是否增加 option-controller/质量斜率的具体解释尚待非作者 source→实际 owner 缺口复核。若已有覆盖足够，处置应为具体 Existing/Only，不能为了论文名再追加正文。

## 2604.20289v1 — 少步 AR 视频可沿 chunk 而非 denoising step 复用

[exact-v1](https://arxiv.org/html/2604.20289v1) §2–5/Table1–3。仍为工作候选，日期归属和独立准入未闭合，拟 `2+2+2=6` 深入。传统跨 denoising step 的 DiT block 缓存利用相邻噪声步相似；四步生成时这个假设变弱。本文按 `(step, block)` 保存前一视频 chunk 的 residual，结构/动作 fingerprint 共同控制复用；在会写入持久 KV 的 clean pass 强制完整计算，避免近似误差成为下一个 chunk 的权威历史。缓存属于生成器内部计算代理，KV 写入才是历史提交，物理 environment state 与安全许可仍非缓存 owner。

作者实验是 X-World/Wan2.2 派生、七相机12 FPS、四步 denoise、264帧约22秒、13段同训练分布 held-out 轨迹；单 Zhenwu 810E PPU 的 BF16 **DiT 部分**计时，排除 VAE、I/O、后处理、跨设备和端到端交互 SLO。Table3单clip移除 KV-update protection 后 PSNR 从53.384降到21.461，支持此受限设置中的历史污染风险；不是物理安全认证。注意该表同时把 skip 从71.3%降到62.8%、DiT speedup从2.59降到2.18，而§4.2文字却称“提高约9个百分点”；数值/叙述冲突，不采用该方向性数字，须在报告标为 `Disputed` 直到原始勘误或实现解释。长时、夜间、恶劣天气、行动突变、真正 policy-in-loop和实际SLO未测。Ch24已有 chunk KV 与 clean-pass commit、跨步训练等原则，却未区分跨chunk residual复用与持久KV保护的这一执行分支；拟Ch24 owner，Ch25只负责预测环境状态/行动后果。须非作者复核来源和实际段落后才判 Books；不能用这项来声称部署通用2.6×。

## 2604.19780v1 — 预算条件训练的方差保证与结果叙述存在中心冲突

[官方 exact-v1](https://arxiv.org/html/2604.19780v1) §3.2–3.6、§4.1–4.4、Appendix A.1 已读。题摘提出一个可核的训练设计分支：统一 budget-conditioned policy、按历史通过率改变题目及预算抽样、在多个截断点用答案核验差分作 progress reward，并学习 `V(q,b)` 基线。相对固定预算/固定先验，这改变了训练采样状态与信用分配；但收益来自作者的数学推理实验，不能推出线上推理 SLO 或任意任务最佳预算。拟按 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 进入标准审阅；因中心方差命题自相矛盾而定点深入，暂列 `Disputed`，不进入 Books。

具体反证不是笼统“实验不足”。§3.5 Proposition 1 声称在 `V(q,b)` 无偏时，BCAE advantage 方差不大于组均值 BRPO；同篇 Appendix A.1 在固定 `(q,b)`、独立同分布 `N` 个 reward 的条件下明确算出 BRPO 为 `σ²(1−1/N)`，确定性 `V(q,b)` 的 BCAE 为 `σ²`，方向相反。§3.5 的 `Cov[R,V]≥Var[group mean]` 与 `V` 在固定 `(q,b)` 下确定性也不相容。Appendix 后段转而讨论**梯度估计量**的相关性/MSE，却没有给出对应计算或足以推出 Proposition 1 的假设；不能把“可能减少某种梯度噪声”当作已证明 advantage 方差保证。

数值叙述也须隔离：Table 1 中 MATH 1024-token BACR `61.5` 小于 GRPO 2048-token `62.4`，§4.4 却写“surpasses”；Table 3 的 BCAE-on-BUP 是 `60.6−59.8=+0.8`，§4.3 却称 `+2.4 over BUP`（`+2.4` 实为相对无组件 `58.2`）；完整配置 `+3.3` 并不大于表内单项增量 `1.6+0.6+0.3+0.8=3.3`。这些冲突不自动否定全部作者实验表格，但不能采用“已证明 BCAE 低方差”“协同超加性”或“1024-token 已胜 2048-token GRPO”作为 Books 论据。

§4.1 实际条件：Qwen2.5-7B-Instruct，MATH train 7500题、3 epochs、8×A100，预算256–4096 tokens、每题8 rollouts、每 trace 4截断点，AIME2024仅24题；训练/核验额外成本被作者估计为约`1+M/G`，未见端到端部署 latency、并发、精度或 SLO。§5承认只在可核答案数学任务。日期保留原字段：官方 `/abs` v1 submitted 为 `2026-03-29T18:31:09Z`，本地 April owner receipt 的 v1 metadata updated `2026-04-23T00:00:47Z`、DataCite created `2026-04-23T01:49:56Z` 与 OAI day 23 只能联合支持 04/23 批次归属推断，不能分别改名首次公开；最终日级日期复核仍待完成。重开条件为作者更正命题/表述及可核对应证据；争议解除前不以此书写训练基线或普遍 token efficiency。

## 2604.19877v1 — 一份 checkpoint 的多种 mixer 布局，发布身份由固定拓扑变成受控选择集

[官方 exact-v1](https://arxiv.org/html/2604.19877v1) §2–3、§5–8 和 Appendix E/H 已实际读到决定问题的段落；[身份页](https://arxiv.org/abs/2604.19877v1)给 v1 submitted `2026-04-21T18:00:25Z`，恰在美国东部常规 14:00 截点之后。本地 04/23 官方连续 ID/批次 receipt 与此相容，故工作上暂按本窗 08:00–09:00 北京时间 announcement 处理；最终仍须独立核官方发布批次，不能只用提交/DOI 创建认领 first-public。

**贡献与边界。** 固定 FA/SWA/recurrent hybrid checkpoint 只有一条 layer layout，适合单一稳定 workload 且执行与验收简单；若同时面对长检索质量、短/长 context、峰谷流量，重新训练/部署多个独立 checkpoint 才覆盖多工作点。本文让 15B 模型的 48 层每层训练 FA/SWA/KDA/GDN 四种 mixer 选择，共享 FFN/embedding/norm，并以随机布局蒸馏、后续指定 preset SFT 与布局 surrogate 寻找质量—decode 成本边界。模型资产于是拥有「允许的 placement 集合」而非单一布局；但每种 placement 的 KV、window 或 recurrent state 不可互换，runtime 仍必须声明 layout identity、状态形状与切换边界。§6 可执行 single-preset 服务；preset 切换会移动 mixer 权重、重捕 CUDA graph，作者报 5–15 秒。per-request 不同布局同实例路由在 §6 明写 **under development**，不能从设计接口与初步多布局表推成已验证生产能力；同轮异构请求必须分开 batch 的调度与容量代价亦不能抹掉。

**评价合同与反证。** §5 的 0.5B placement-sampling 受控消融不能外推 15B；15B frontier 的高效布局较不稳定，提前定向训练易形成自我强化假最优。§7.3 Table4 把 15B 的 32K、单 preset decode speed/平均任务准确率做有限 Pareto 对照（如 12FA/26SWA/6KDA/4GDN 为 2.9×、96% retention；全无 FA 的 aggressive preset 更快而 long-range retrieval 显著回退）。§7.1/Appendix E 的 speed 仅单 preset、H100/vLLM/特定 prompt 和长度；§8 承认质量比较用 eager 以绕开 linear mixer CUDA graph 数值不稳，吞吐却用 graph，因而不能宣称同一执行模式下同时获得表中质量和速度，更不能外推多 preset 并发、SLO 或新模型。长距 RULER/NIAH 退化、surrogate 用 teacher-trace likelihood 的 proxy gap、single teacher 与不同 15B SFT 数据/预算均保留。未复现实验或验证作者 artifact 的完整部署路径。

拟 `Design Delta 3 + System Reach 2 + Durability 3 = 8`，深入；`MODEL-LONG-CONTEXT` Ch22 拥有 hybrid layout/表示—精确访问预算，`INFER-TENSORRT-LLM` Ch49 仅承接 runtime 版本化 plan 与异构状态，不能把模型训练权归推理引擎。Ch22 现有论证已有**固定** hybrid layout 与逐层替换，但未覆盖「同一模型资产训练多个 layout，并以任务/速度选择已验收布局」的分支，属真实窄缺口；待非作者 source→owner 核后定点写入该段，而非在章末追加案例。Books 只写稳定机制和退路，不收作者加速数字、未完成的 per-request 服务或跨模式比较为设计结论。若日期最终不属 04/23，则整项仅移动 owner 日，不跨日重复评分。

## 2604.19884v1 — 量化损伤要区分仍可读出的弱信号与处理路径失效

[官方 exact-v1](https://arxiv.org/html/2604.19884v1) §3.1–3.4、§4.1–4.3、Appendix A/C–E 已按必要问题审阅。初判 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，因可能改变低比特发布诊断而深入；仍待非作者准入/Books 复核及独立日期 Gate，不提前计正式候选。作者把 4-bit GPTQ 失败例中仍可经层内 logit lens 读出的目标信号，与所测 2-bit GPTQ/AWQ 表征和组件转移同时受损的现象分开。跨模型 clean activation patch、zero ablation、逐层混合精度及修复/不修复干预增加机制辨识力；这比只看平均 perplexity 或 logits drift 更接近“该加精度保护，还是该拒绝低位 artifact”的发布问题。

然而 `Failure Subset` 按 FP16 正确且 4-bit 错误预先选出，Table 1 里的 4-bit baseline `0%` 是条件分母，不是总体准确率；把该分母上的补救率转成部署收益会失真。§4.3.1 的修复还把部分权重从 4-bit 升至约 4.1/4.25 平均 bits，并调输出放大系数，非同存储预算、非通用无训练修复。§4.3.2 的 2-bit 前层混合精度、clean-signal injection 与 EORA 负例，只证明作者测试干预未恢复该模型/任务，不能证明所有 2-bit 格式、QAT 或重新训练都不可救；作者 §5 Limitation 明限 weight-only 与事实回忆，MMLU/GSM8K 扩展不等全部推理/安全任务。层内线性读出只是 probe，不能把目标 token 的可解码性直接当模型真正使用了该知识。

实际 Ch49 已有量化 artifact 的 aggregate→逐例一致性→distribution-drift release gate，也已讨论敏感层高精度，但尚未把“可读信号衰减”与“组件收到高精度输入仍不能处理”作为两类不同的定位/回退路径。apr01 对 exact-v1→实际 Ch49 的有限非作者核通过后，已在该章量化验收段定点整合：先用同一条件分母定位状态是否仍可读、再以局部补丁与精度保护验证可修复性；处理路径受损时回退更高精度或重新训练/校准，而不是无条件叠加补偿。root 已顺读正文与相邻交接并作写后核验。第66章仅负责报告 cohort、evaluator 与发布证据，不重复量化机制。所有性能条件仅限作者四个 7–9B 模型、Pararel 39关系及披露的 GPTQ/AWQ 设置；硬件、服务并发、输出长度与 SLO 未作为可迁移结论取得，不写通用 4-bit/2-bit 阈值。本项通过不代表04/23整日 Gate。

## 2604.20032v1 — GPU stall 症状不能直接等同可修改的根因

[官方 exact-v1](https://arxiv.org/html/2604.20032v1) §III-B～E、§IV、§V-A～C、§VI-D、§VIII Limitations 已按必要命题审阅。暂按 `Design Delta 2 + System Reach 2 + Durability 2 = 6` 作标准审阅；因 Ch49 现有 profiling 分解只到 host/device 分类、没有从 stall site 沿 register/predicate/synchronization 依赖反查可改动的 source decision，提出一个窄 Books gap，待非作者准入/owner 核及本窗首次公开校验，不能预记整合。LEO 的测量输入是 HPCToolkit 的各厂 PC samples，分析器在控制流和指令依赖图中逆向切片，按 opcode、barrier、潜在隐藏延迟及执行情况剪枝，再用启发式权重给仍存的先行指令分摊 stall；AMD `s_waitcnt`、NVIDIA barrier 和 Intel SWSB 各有不同的同步边。这个方法能把“某指令在等待”与“谁造成等待”分开，但加权归因不是干预式因果证明。

项目直接相关的 §VI-D 只有两个 ML kernel 分支：在 llama.cpp `mul_mat_q`、Qwen2.5-1.5B/Q4_K_M 的作者配置中，AMD MI300A 因寄存器压力/间接 store 而以缩 tile 加直接 store 得到单 kernel 1.12×，同一 NVIDIA GH200 路径是 1.00×；HipKittens RMSNorm 在 MI300A 的 BF16 load/s_waitcnt 路径经多行软件流水得到 1.07～1.24×。全文 21 个 workload 的 1.73～1.82× 几何平均主要含 HPC，且由专家**看完诊断再改代码**取得，不是 profiler 自动产生的收益，也不是 LLM 推理整服务或跨厂统一加速。多数优化用 per-kernel GPU time，仅跨 kernel fusion 案例改用 aggregate timer；这些分母不可拼成同一请求时延。作者另用单个 Gemini 3.1 Pro 做 LLM 优化探索，不能证明跨模型自动调优。

§VIII 自限 register 而非任意 memory dataflow、branch weighting 近似、冷 PC 样本不足、CUPTI Activity 可能串行化并发，且没有逐链真实因果 ground truth；AMD 采样约 10% 运行开销，事后切片通常数秒、较大 llama.cpp 图约 60 秒。因而稳定结论只是在 kernel/architecture/shape/precision 已绑定时，先从测量症状追到可测试的源代码假设，再以同配置干预/回归证明采用，而非将 blame 排名当作优化许可。apr20_resume 对 exact-v1→实际 Ch49 的有限非作者核通过后，已置于 TaxBreak/WebGPU 执行栈 profiling 分解之后，承接“定位哪一层”到“哪条依赖致 stall”，保留静态 vendor profiler 与无可行动瓶颈时停止优化的旧路径；root 已顺读正文及前后交接并作写后核验。Ch66 只拥有正式 evidence contract。生产 workload 的 batch、并发、输入/输出长度、服务 SLO、完整精度矩阵均未披露，不可外推。本项通过不代表04/23整日 Gate。

## 2604.20105v1 — 以 kernel 执行结构估计功率的受限分支

[官方 exact-v1](https://arxiv.org/html/2604.20105v1) III-B、IV-A～C、V、VI-A～E 已按本项目的功率预算问题定点审阅；原文页眉写 04/22，但本日首次公开窗口仍待官方发布批次核对，不以投稿/元数据字段单独落窗。暂按 `Design Delta 2 + System Reach 2 + Durability 2 = 6` 做深入候选审阅，不先计最终分母或 Books。旧路径直接测量目标硬件计数器最可信，却需先有设备并支付每个 workload 的 profiling 成本；仅以 FLOPs、总流量或预测 latency 替代功率则遗漏 SM 负载不均与 L2/DRAM 层级差异。同近似 latency 的作者微基准中功率可差 96W，这是受控局部实例，不是生产请求普遍差距。

作者用 kernel tile、threadblock 排布、swizzle 与 pipeline 推导每层 memory traffic 和 busy/lazy SM 时间线，再经离线测得的 phase correction 与功率系数拟合六类模块活动；训练期仍需 A100/A10 的 NVML/NCU 数据。在线只从 operator shape 预测 kernel 参数，拼接顺序 kernel 的 latency/power，形成不在目标 GPU 上重跑 profiling 的探索代理。作者报告 A100/A10 全 workload 平均功率误差 8.0/8.2%，H100 6.7%、L40S 12.7%；跨代预测依赖近似每比特/每 MAC 能效，GDDR6 的 L40S 误差已显示该假设边界。语言实验含 BERT-Large、GPT-2、OPT-1.3B、Qwen2-1.5B 的不同 batch/sequence，但主端到端实验使用 eager、禁用 FlashAttention；其他精度、具体并发/输出长度与服务 SLO 不能补造。单 GPU、规则 tile 和顺序 kernel 是作者明示限制，不能直接用于 overlap、通信 kernel 或不规则稀疏的分布式推理总功率。

实际 `PLATFORM-COST` Ch70 已把资源时间与实际能量分开，也有按组件/阶段分配 power budget，以及从默认频率 profile 借参考曲线的方案；尚无“目标设备计数器不可取得时，先由可解释 kernel 时间线估计模块活动、再定点实测校准”的设计分支。apr02 已在[有限非作者 source→owner 审阅](./V3_APR02_20105_FINITE_OWNER.md)中确认这个窄缺口；root 将两段机制正文放在 Ch70 的组件预算与参考曲线之间，并顺读实际写入的上下段，写后通过。测量路径仍是发布与 SLO 的最终验收，不能以作者平均误差把 surrogate 当控制闭环的真实传感器；本项实际整合不代替首次公开与整日 Gate。

## 2604.19857v1 — 复合奖励 GRPO 理论结论的必要反证，日期暂隔离

[官方 exact-v1](https://arxiv.org/html/2604.19857v1) §4.1–4.4、Appendix A.2–A.3 已实际重开；[身份页](https://arxiv.org/abs/2604.19857v1)仅给 v1 submitted `2026-04-21T17:21:08Z`。提交时刻不等 first-public，且可处于前一日报窗口；当前未取得足以唯一证明 04/22 09:00～04/23 09:00 北京时间首次公开或重要修订的官方 announcement slot。**先作 Date Hold，不纳入 04/23 冻结分母、评分与 Books；若核到前一窗口，只定点移回真实 owner day。**

中心结论的有界反证须保留，供 owner day 复用：§4.4 Eq25 对固定 source/target 分布的 bounded-value 差给出无样本数的 Pinsker 上界；Appendix A.3 Eq50 却在同一分布差项中引入 `1/√n` 而没有新增估计对象或前提。固定两分布与非恒定 value 时，分布期望差不因训练提示数 `n` 增大自动趋零，故所印 Theorem3 的跨域保证未由该证明建立。§4.3/Appendix A.2 Eq41–44 在忽略已省略的数值 `ε` 时，定义的 `Δ_i` 实为零的代数恒等式；Eq46 又据此界定 *joint* 与 *decomposed* 目标差，然而后者使用独立归一后原始 `w_k`，前者对应系数为 `w_k σ_k/σ_comp`，两目标不因此相等。不能用 Eq45/46 的 `Δ_i` 证明 Theorem2 的最优 gap，也不能把作者的 synthetic alignment 曲线升格为理论保证。§4.1 Assumption2 已预设 composite variance 随 `K/G`，因此 Theorem1 的该依赖也不是从 GRPO 机制无条件导出。此处只隔离三项宣称的强保证，不说所有实验无效。

若 owner day 验证落窗且独立准入同意，拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，因可能修正 RLVR 设计判断，必要深入 `Disputed / no Books`；只能描述具体证明缺口，不写入 Ch32/33 的稳定训练机制。实证章节另是 synthetic TA-MDP 与 Visual-ARFT 受限测试，不构成任意 LVLM、tool depth 或 OOD 迁移保证。重开条件为作者勘误、严格条件证明或独立可复核修订，而非仅有后来版本摘要。

## 2604.20098v1 — 图依赖事实保留的可微训练与硬规则发布

[官方 exact-v1](https://arxiv.org/html/2604.20098v1) §2.2–3.6、§4.1–4.3、Limitations 已重开；官方身份页的 Submitted=2026-04-22T01:35:31Z 仅为提交字段，本窗 first-public 还需与官方公告/ID批次联合核，不能凭它独自确定归属。准入增量不是“又一篇 conformal factuality”，而是硬 CF 的筛选、祖先闭包、分位数、最终最大子图选择相互耦合，普通独立 claim 分类器即使拟合 score 也不直接优化有统计约束的 graph retention。拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`；因已核出现真实 Books 机制缺口，按合同提升为必要深入，不由旧六维分数倒推。

作者用 sigmoid 近似阈值、加权几何均值近似祖先合取，再对错误 claim 的违反量、阈值 supremum 和校准分位数/预测 argmax 建 soft proxy，梯度回传到 claim scorer。训练内部另分 calibration/prediction 子集，测试却把学得的 scorer 送回原硬 CF 与独立阈值校准；软训练不是上线推理的保证主体。Theorem 3.1/3.2 是温度等参数按规定极限走向硬算法，不是有限温度或有限样本的逐答案正确性保证；交换性、标签与依赖图可信、部署分布稳定仍是必要合同。§4.1.5 的 coverage 是保留图保持 coherent factual 的题目比例，retention 是平均保留 claim 数，不是每条 claim 的 90–99% truth probability。

证据只限 MATH 202题（人工双标依赖边、平均7.3 claims）与 FELM 710题（平均4.0 claims）、20-fold 且每折70/15/15训练/验证/测试；MATH在 α=.03 的1.76对.73是多保留 claim，但 coverage 仅在目标0.5百分点内，不可写成已达到目标；MATH只在 α=.05～.08 达标，FELM为10个α中的9个达标且其中6个 retention 高于 CF。严格α下 MATH≤.02、FELM=.01 会全拒；FELM频率已具判别力时收益缩小。原文未建立真实生产SLO、跨域/分布漂移或单个子群保证，且依赖图错误会改变有效性；人工标签、抽图、训练和重校准均有成本。该限域支持一条长期设计分支，不支持“DCF普遍解决幻觉”。

与实际 `PLATFORM-EVALUATION-SYSTEM` Ch66 的 claim graph、Raw Score校准、answer-level estimand 已对读：现文已有依赖/概率校准/交换性失效回退，未有“以耦合硬选择的可微训练代理学 scorer、但把发布保证留给硬算法与独立校准”的控制分权。apr02 的[非作者有限 source→owner 与实际写后核](./V3_APR02_20098_DCF_OWNER_AUDIT.md) 均 PASS；root 已将两段机制正文插到 Raw Score 校准之后、答案级合成之前，并在章末留下证据边界。**这只把该单篇计为实际整合，日期归属、正式日报及整日 Gate 仍未完成。**

## 2604.20021v1 — 连续查询空间语义缓存的收益合同与证明缺口

[官方 exact-v1](https://arxiv.org/html/2604.20021v1) §2、§5.2–5.3、§6、Appendix A 已定点审阅；[身份页](https://arxiv.org/abs/2604.20021v1)的 v1 submitted 为 `2026-04-21T21:56:43Z`，仅证明投稿，不单独确定北京日报首次公开窗口。工作上拟 `Design Delta 2 + System Reach 2 + Durability 1 = 5` 标准审阅；中心在线 regret 保证出现具体疑点，按纠错信号定点深入，首次公开批次及独立审阅未完，不计冻结分母或 Books。

旧的精确字符串缓存不共享相似提问，有限离散语义缓存则预设所有 query family 可枚举。本文把请求映射到动态 ε-net 区域，用 KRR 把某一请求的服务成本观测推广到相近区域，并以分阶段切换减少 cache 重建；cache 命中反而看不到真实 LLM 成本，故估计必须处理 partial feedback。这个机制可影响 Ch62 的 cache admission/routing 与 Ch70 的成本取舍，但 cache key 的 tenant、policy、model、知识有效期与真实 answer correctness 仍是独立 contract，不能让 embedding 距离或其代理 mismatch cost 充当事实验证；现有 Ch72/Ch76 已明确该安全边界。

定理范围须收窄。§5.3 Assumption 2 只说高概率区域的有效中心数 `m_eff` 有界，Theorem 5.1 的显示上界却另有 `k·m_max·loglog T` switching 项；同节将最坏情况 `m_max` 写成可随 `T` 增长到 `O(T^{d_e/2})`，因此按已展示条件不能直接推出正文宣称的普遍 `~O(√T)`。需作者明确 `m_max` 在该假设下也受控、或给出更紧的切换证明；目前不把 sublinear regret 作为 Books 论据。§2 对查询分布、Lipschitz cost、按距离单调的 mismatch penalty、i.i.d./cluster 等前提均不等于真实多租户请求。§6 的 50 synthetic prompts 与 NQ/TriviaQA 各 2500 查询，384 维 sentence-transformer embedding，服务成本由 GPT-2 token length 的归一值代替，未测真实模型输出正确性、硬件、精度、并发或生产 SLO。故作者相对 baseline 的数值只限该模拟 cost/evaluator，不能解释成实际服务延迟或节费保证。

处置暂为 `Disputed / no Books`：仅保留可解释的动态区域、成本学习、切换设计分支；证明与 workload contract 不支持修改稳定章节结论。重开条件是可核的定理条件/勘误、真实成本与安全验收，以及独立日期和准入复核；若只是重要性不足而被前分母关闭，也保留本处有限证据供审计，不用下调分数掩盖中心疑点。
