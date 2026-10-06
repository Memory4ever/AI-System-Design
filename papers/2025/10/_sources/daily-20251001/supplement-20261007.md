# 2025-10-01 增量补查（执行日 2026-10-07）

## 范围与权限

唯一作者范围为本日 README 与本目录补查原件。原窗口 `2025-09-30T09:00:00+08:00 ～ 2025-10-01T09:00:00+08:00`、原 OpenAI 七案例家族、公开时间与有效证据保留；新增只查 `2025-09-30 ～ 2025-09-30`。不创建其他日，不写 Books、State、月索引、合同或脚本，不 stage/commit/push。当前合同从主工作区读取。

启动已读原 README 全候选、SOURCE_NOTES、14 每日入口及 AGENTS/四份适用合同与 ROADMAP、当前 checkpoint。原材料只定点去重；旧复核不是本轮复核。

## 实际请求与原件

第一轮 curl 于 2026-10-07 15:09～15:12 +08:00 执行；15:12:10 +08:00 获取执行钟。统一 `curl -L --max-time 18 -sS -D <name>.headers -o <name>.raw -w HTTP/effective-url/bytes/seconds`，原件保存在 [supplement-20261007/](supplement-20261007/)。未返回正文的超时不生成正文原件；headers 保留实际响应。成功下载不等于检查历史段。

| 名称 | 实际 URL | 实际结果 |
| --- | --- | --- |
| openai-research | https://openai.com/research/ | 403，9686 bytes；不作为 Research 列表 |
| openai-rss | https://openai.com/news/rss.xml | 200，763247 bytes；XMLParser 缺依赖后改用标准库 ElementTree，1251 items，Sep30 三条 Sora 页 |
| anthropic | https://www.anthropic.com/research | 200，280299 bytes；待解码日期对象 |
| google-pubs | https://research.google/pubs/ | curl 28，18s 超时；web 回源可见当前 1–15/11597、年份过滤，不提供日级历史排序 |
| deepmind-research | https://deepmind.google/research/ | curl 28，18s 超时；web 当前目录可读，不冒充历史日段 |
| google-september | https://research.google/blog/2025/09/ | curl 28，18s 超时；web 原归档第1页12卡，Sep30两卡后Sep25，停止此处 |
| meta | https://ai.meta.com/research/ | curl 35连接重置；web零行，非零事件证明 |
| qwen | https://qwenlm.github.io/ | 200，17307 bytes；需核迁移入口，旧首页不授新日段 |
| deepseek | https://www.deepseek.com/ | 200，115583 bytes |
| kimi | https://platform.kimi.com/blog | 200，13388 bytes |
| hunyuan | https://hunyuan.tencent.com/research | 200，6893 bytes；动态壳不能记已看全部 |
| zai | https://www.zhipuai.cn/zh/research | 200，1276382 bytes |
| seed | https://seed.bytedance.com/en/research | 200，114100 bytes |
| ernie | https://ernie.baidu.com/blog/zh/ | 200，28100 bytes |
| mimo | https://mimo.xiaomi.com/ | 200，58220 bytes |
| minimax | https://www.minimax.io/blog | 200，134698 bytes |
| minimax-agent | https://agent.minimax.io/docs/techblog | 200，215743 bytes；实际重定向 https://agent.minimax.cn/docs/techblog |
| arxiv-cl-day | https://arxiv.org/list/cs.CL/2025-09-30?show=200 | 400，7392 bytes；日期路径无效，不能算0命中 |
| arxiv-cl-month | https://arxiv.org/list/cs.CL/2025-09?skip=0&show=25 | 200，46365 bytes；标题 Authors and titles for September 2025，2215项、1–25，ID升序，不是Sep30公告批次；不逐项筛全月 |

arXiv root 已反馈同日 Advanced from/to 会200表单错误；本轮不把参数当生效过滤，不用首公告年月排序、DataCite、Updated:v1或公告日程推导日批次。旧候选按授权保留日期。新增须有实际官方公告/list日证据；公开日未恢复是外部缺口，不是无命中。

## 后续实际恢复与停止点

15:14～15:31 +08:00 的原始 URL、状态、执行钟保存在 [native-recovery.json](supplement-20261007/native-recovery.json)、[last-fetch.json](supplement-20261007/last-fetch.json)、[arxiv-discovery-log.json](supplement-20261007/arxiv-discovery-log.json)、[arxiv-topic-fetch.json](supplement-20261007/arxiv-topic-fetch.json)。web 原文见 [first-web-original.json](supplement-20261007/first-web-original.json)、[google-core-web.json](supplement-20261007/google-core-web.json)。这些是工具实际返回，不是补造历史快照。

| 来源 | 本轮实际处理与停止 | 不能证明的范围 |
| --- | --- | --- |
| OpenAI | RSS 标准库解析1251项，Sep30三页合并Sora2；原七案例身份和原复核保留。当前Sora原HTML与初始PDF定点去重 | RSS不等于全站；当前页面2026停服/characters改写不回填2025 |
| Anthropic | Next Flight用JSONDecoder解码174对象、172独立记录，邻接BJT09/16、10/04，Research数组无Sep30；Sonnet4.5与Claude Code官方页另作具名去重 | Research数组不覆盖全部News；解析失败未记零命中 |
| Google | 原Sep2025 Blog首12卡止Sep25；Sep30 AlphaEvolve/PHA原核心再次读取。Google pubs默认可读1–15/11597、2025计678；DeepMind真实第2页30卡已定点恢复本日10/30→09/29边界 | Google首次公开日库存未恢复；DeepMind只selection，Blog/列表发布日不等于所链论文公开日 |
| Meta | 连接重置、web空及官方域日期窄搜无结果 | 不是历史列表零事件 |
| Qwen | 旧首页迁移到qwen.ai；真实`/api/page_config?code=research.research-list`返回60对象，逐项日期解析；最新BJT2025/12/23，前后侧09/24 Qwen3-Max与11/13 DeepResearch，无Sep30对象，无分页字段 | 配置有前后侧，未披露历史完备性；不是后侧缺失或请求失败，不能授全站零事件 |
| DeepSeek | 当前Research10项，10/21到05/14夹住本窗；News目标日前最近09/29，并非当前全部News最新；止当前列表 | 不覆盖全部GitHub直发 |
| Kimi | 官方Blog日期列表，11/07、11/06后09/16，止越窗处 | 不覆盖全部仓库release |
| Hunyuan | 当前bundle确认API；POST pageNum1/pageSize20/renderType0，默认en total9；accept-language:zh total11/11，均最早2026/02/03 | 两语言均无2025库存；API可提取但没有浏览器AX历史列表 |
| Z.ai | Research p1/p2累计18项末12/07且“没有更多”；发布说明补得Sep30 GLM4.6，核心模块与09/30保存件同字节 | Research历史段仍缺；release性能宣传不当作机制证据 |
| Seed | type1/type2、publish_year2025，page_token0/20、count20；实际返回英文内容，置顶另检，非置顶跨过09/30；type1 total94、type2本轮total45；止第二页日期定位 | 未全审年度库存；日志URL不证明US请求头/locale，PublishDate不替代论文首次公开 |
| ERNIE | Blog两页10+6条，终页1/2，09/12与10/16邻接 | 仓库直发不在此范围 |
| MiMo | 当前首页及官方异步bundle恢复Paper8项，09/19与10/21邻接；Blog15条local More不提供日期 | Blog历史日段仍缺，不能以Paper列表代替 |
| MiniMax | EN/CN Blog当前日期卡，10/27与01/15邻接；Agent原件只见2026/05/13 | Agent目标历史段未恢复 |
| arXiv | 两种日路径400；CL月列表首25/2215；Advanced首50/3126；四主题API159返回记录去重125，首批30项及等待期间增读66项完整题摘 | 没有官方Sep30日批次；未完成日窗初筛，不是125篇当天论文 |

## 日期查询有效性：实测而非参数推定

1. `/list/cs.CL/2025-09-30?show=200`和`/list/cs.CL/20250930?show=200`实际均400。月目录首25是ID升序的September库存，没有日公告分组，因此没有继续翻全月。
2. Advanced跨日请求原 URL 见 arxiv-discovery-log.json。200返回3126结果、首50；`classification-computer_science_archives=all`没有勾选真正的`classification-computer_science=y`，不得称已完成CS分类限制。实际原件只显示“originally announced September 2025”；首项当前v2 submitted2026只是当前修订字段，**它本身不能证明first-announcement过滤失败**。页尾首公告排序只有年月，因此也不能授Sep30日过滤成功。止首50，不把3126列为任务池。
3. 15:31:05 +08:00另用正确CS checkbox与同日from/to实际请求；200/30272 bytes但原HTML第350行是`End date must be later than start date`，没有有效结果集。原件 [arxiv-same-day.raw](supplement-20261007/arxiv-same-day.raw)，精确请求见 [arxiv-same-day-log.json](supplement-20261007/arxiv-same-day-log.json)。不能记0命中。
4. 官方availability帮助原件 [arxiv-help.raw](supplement-20261007/arxiv-help.raw)说明审核可能延迟、ID在公告时分配；只用于否定submitted=公开的推导和辨别ID年月，不把常规日程换算为个体日证据。DataCite、Updated:v1也不授日公告证明。
5. 四主题API实际用`submittedDate:[202509281800 TO 202509291800]`作有界恢复线索，不当作公开窗口。models(CL/LG/AI)81中返回50；systems(DC/AR/PL/OS/PF)15中15；multimodal(CV/RO)44中44；agents(IR/MA/AI/CL)90中50。具体术语与URL见arxiv-topic-fetch.json。125个独立ID并非已准入候选；models余31、agents余40未请求；不把剩余库存默认变成逐篇队列。官方日批次标题补检未能成立，主题召回仍未完成。

## 首批贡献校准与日期保留（初始提交包，裁决见末节）

初始将Sora2拟新增，定点读取09/30候选后撤回该拟新增：**同一事件已有有效审阅，不是因为Books已有主题拒收**。Sora2、Sonnet4.5、Claude Code共3家族只复用09/30归属，均不增加本日分母。前两次发到错误的2026协调线程的scope/calibration消息已明确撤回；实际native root发送被工具拒绝，未伪造校准通过。本轮向root的实质汇报通过作者任务输出留痕；初始等待状态保留为过程，当前Dewey裁决与返修见末节。

Sora初始7页PDF SHA256 `1a74678aacf0499a3b4d2ae71da9bdbb1221a8211a9c3890fe87748a5ccdcd51`与09/30原件相同，复用[09/30报告](../../../09/30/README.md)与[BOOKS_HANDOFF](../../../09/_sources/daily-20250930/BOOKS_HANDOFF.md)的精确版本/限制，不重读全部附件。初始card的cameo opt-in同意不自动支持当前blog的详细撤销范围、draft删除或characters措辞；撤回初始校准包对这些当前功能的历史外推。主工作区Ch72“内容 provenance 与身份权限”段已承载同一精确命题，本轮Books差额0，不写Books。

以下30项完整题摘实际读取，全部来自上面的本轮官方API原件（当前版本，并非冻结2025摘要）。表内仅表达**待校准的原文潜在贡献**，不照录性能、不宣称方法证实、不评分。除AMemGuard外，September ID只证明公告年月，不证明Sep30日；当前v1也不能用updated推定日归属。安全/负面/纠错项没有因局部结果或低分被跳过。

| 身份/实际版本 | 旧约束 → 原文潜在增量 → 待改变的选择 |
| --- | --- |
| 2509.25188v2 Learn2PD | 固定阈值并行解码 → 学习token稳定性与EoT → 自适应解码收益需连同filter代价核验 |
| 2509.25176v1 SIRI | 推理长度与正确率取舍 → 交替压缩/扩展rollout预算 → 是否可用训练日程改变Pareto边界 |
| 2509.25149v2 NVFP4 | FP4离群与梯度稳定性 → RHT、二维量化、随机舍入、精度例外 → 低精度训练的可行边界；comment明确Eq2 typo纠正，需精确事件正文，不能沿用修订公式冒充2025 |
| 2509.25073v1 PTG | ID准确率代表执行泛化 → 小Transformer长程序/trace系统失败 → 设计反证；不因小模型或负面排除 |
| 2509.25041v4 GRACE-MoE | 通信优化与负载均衡冲突 → grouping/replication/locality协同 → 分布式MoE的优化粒度 |
| 2509.24859v2 HARP | 同构并行计划 → 异构细粒度planner和1F1B时序 → 网络/加速器异构的调度边界 |
| 2509.24626v1 SparseServe | 稀疏attention未释放HBM容量 → HBM/DRAM working set与分层prefill → batch收益和传输抖动需一并评价 |
| 2509.24381v1 RServe | encoding解耦仍串行依赖 → intra/inter-request overlap和token budget → 多模态分阶段调度 |
| 2509.25279v2 RL in the Wild | 静态RL任务代表动态负载 → 序列偏斜、策略变化及PolyTrace → benchmark是否遗漏真实系统瓶颈 |
| 2509.25187v2 FlashI2V | 直接拼条件图造成shortcut → latent shifting/Fourier guidance → I2V条件泄漏与OOD评价 |
| 2509.25182v1 DC-VideoGen | 压缩空间更换需重训 → chunk-causal codec与AE-Adapt-V → 迁移成本是否换来端到端收益 |
| 2509.25178v3 GHOST | 固定幻觉benchmark → 主动优化无目标物图像 → 新诊断盲区；需检查攻击/人评条件 |
| 2509.25177v1 LayerCD | 视觉特征层等价使用 → 深浅层输出对比 → 解码抑制幻觉的成立条件 |
| 2509.25162v2 AlignTok | tokenizer强调低层重建 → foundation encoder三阶段语义保持 → latent语义与生成收敛取舍 |
| 2509.25003v3 ScoreMIA | 多步重建才可测成员泄漏 → 单query score统计 → 隐私审计成本和攻击假设 |
| 2509.24948v6 World-Env | 实环境不可重置 → world simulator与VLM reward/终止 → 模拟反馈不可冒充真实安全性 |
| 2509.24837v4 ZOO-Prune | attention/diversity剪枝代理 → 投影层零阶敏感度 → 剪枝评价必须含估计代价 |
| 2509.24734v1 TRIANGLE | 两两cosine不保证三模态联合对齐 → triangle-area目标 → 融合/对齐判据变化 |
| 2509.24702v2 Physical plausibility | 隐式训练物理规律 → counterfactual prompts与同步解耦guidance → 不把视觉可信度当动力学保证 |
| 2509.24695v2 SANA-Video | 长视频KV增长 → block linear constant-memory state → 状态容量与长程一致性取舍 |
| 2509.24566v2 TokenSwap | 固定目标pattern易检测 → 关系词swap与加权loss → bags-of-words安全漏检；旧09/30必要审阅可定点复用，但不把当前v2当旧v1 |
| 2509.24527v1 Dreamer4 | world model交互预测失准 → shortcut forcing与离线imagination训练 → 环境反馈、动作条件与生成视频需分开 |
| 2509.24488v1 Self-Sanitize | posthoc过滤不兼容流式 → token监控/原位repair → 时延和privacy保证需同审；旧09/30审阅只复用对应版本 |
| 2509.24359v1 DRIFT | 随机化防御梯度共识 → Jacobian/logit divergence → 必须核自适应攻击与梯度遮蔽反证；旧09/30已有必要审阅，不重复新收 |
| 2509.24368v3 DLM watermark | AR前缀watermark依赖token顺序 → 未确定context的期望watermark → 任意顺序生成与检测不变量 |
| 2509.25302v2 Self-replication | 直接指令复制造成risk混淆 → operational任务与overuse指标 → 成功率不等于失控风险；当前摘要含OpenClaw等后期语境，绝不回写2025事实 |
| 2509.24675v1 Unlearning dilemma | 拒答代表知识删除 → prompt强调可恢复与token贡献解释 → 必要安全反证，不因负面而排除 |
| 2510.02373v1 AMemGuard | 单条memory检查不捕捉情境触发 → consensus/双memory纠错 → 贡献潜在有效；官方ID公告月Oct，不可由Sept submitted搬入Sep30，关闭本窗日期而非贡献 |
| 2509.25140v2 ReasoningBank | 只存成功轨迹 → 成败策略蒸馏与memory-aware scaling → memory评价的预算/错误反馈边界 |
| 2509.25301v1 Flash-Searcher | 工具顺序链执行 → DAG依赖并行与动态图更新 → 并发收益须对齐工具/搜索预算 |

首批停点时其余95个独立ID尚未宣称完成题摘贡献筛选；等待期间继续结果见下节。没有为日期held泛读普通附件。上述API只是恢复线索，仍缺官方公告日列表及对本窗新命名机制的有界标题补检。恢复后先限定真实日批次，再对主线相关条目完整题摘，不延续宽库存队列。待校准代表拟入选是RServe/NVFP4/PTG与安全反证；在官方日归属与首批非作者校准成立前，不展开新增深审。没有候选因审阅成本被改成无贡献。

## 等待校准时继续执行（至15:44 +08:00）

收到root询问后，没有停在初始95个未读题摘。继续在同一批125个ID内做范围判断，并增读66项完整题摘，合计96项；29项只按明确范围或官方公告月份处理。没有新增全文/附录深审，仍无日级入选分母。完整题摘原件仍是四份官方API，具名已读身份见 [abstract-read-ids.json](supplement-20261007/abstract-read-ids.json)。不是从标题/关键词反推贡献；局部实验、negative、小模型、模态/训练理论仍保留潜力。

增读中不作贡献关闭的机制线索（待日归属/校准，不评分；不是已经采用的新增命题）：

- 优化/表示：XQC的critic条件数与BN/WN/CE（2509.25174）；AAPA固定discriminator anchor（25148）；RL模型/数据/算力缩放与重复数据（25300）；mean-field token多时标聚类理论（25040）；MobileLLM-R1数据重采样而非只参数数量（24945）；GAT中间监督/width-aware LR纠正GAN scaling失效（24935）；Query Circuits输入级trace/NDF（24808）；identity bridge二跳监督（24653）；SeaPO error amplification（24781）；SMoPE共享prompt的干扰/容量取舍（24483）；EOE先AdamW再expert参数演化的混合优化（24436），不是替代AdamW；CLQ校准分布、Hadamard与跨层搜索（24416）；ES全参数无反传post-training（24372）；LLaDA-MoE计算/质量替代取舍仍须可比评价，不用组合名直接证明新增机制（24389）。
- 多模态/运行时：GSM8K-V隐式视觉推理而非显式符号（25160）；Euclid几何surrogate迁移（24473）；Multilingual Text-to-SQL的语言/任务难度边界（24405）；NPU causal operators的cache/带宽瓶颈（25155）；LUMA时频双anchor（25304）；RGB-A噪声/latent分布分离（24979）；DAM双向distillation/active监督（24896）；VFL layer intervention和选层LoRA（24791）；VTPerception两阶段与感知reward（24776）；IA-VLA语言理解/控制频率分层（24768）；UI2V语义/物理评价盲点（24427）；DynaMIC误导指令识别是必要安全线索（24413）；AdaNav按action entropy触发reasoning（24387）；Vid-LLM几何prior adapter（24385）；Uni-X浅深模态梯度冲突/中间共享（24365）；FreeAction动作条件guidance与noise（24241）；VideoAR预测单位从帧到cube（24081）；Grounding IDs的表示与因果干预（24072）；LVT局部view/相对几何encoding的attention复杂度取舍（25001），没有以“3D视觉”题名机械排除。原PoseDiff（24591）已按撤回移出，只有失效稿身份留痕。
- Agent/系统理论：InfoAgent entity-tree difficulty与自托管搜索（25189）；DataMind SFT/RL可变objective、multi-turn rollout稳定性（25084）；CEL规则归纳与playbook分离（25052）；AutoPlay环境探索后生成可验证任务（25047）；ID-RAG显式identity状态（25299）；Socratic-Zero动态Teacher/Solver/Generator课程（24726）；MemGen latent memory trigger/weaver（24704）；PhysiAgent依据VLA feedback组织组件（24524）；CVP局部distribution-shift反证需对齐具体causal假设，不因只synthetic就关闭（25282）；TimeOmni/AXIS时序语义表示与训练信号（24803/24378）；Fed-Span动态拓扑的聚合/通信/收敛边界（24932），待校准其与模型系统主线的实际联系，不因跨领域题名先删。

完整題摘后具名贡献关闭18项（初始20项中Social Science按撤回分离、EQUISeg重开，见末节；Dewey已读完整题摘校准，日期未核，不泛查全文）：

- 2509.25043软件testing Roadmap：摘要提供领域整理/分类，没有指出足以改变模型系统选择的新机制或具体评价盲点证据；不是因“综述”格式本身排除。2509.24877 Social Science原taxonomy关闭已由撤回身份取代，不能继续采用旧稿。
- 2509.24422 CDT：认知分类、相关性与data-selection分数未披露足以修正现有评价解释的具体混杂/盲点机制；不采用其增分主张。
- 2509.25297 TDDev、24855 PhysicsMinions、24826 AIPOM、24515 Move MSG：核心分别为既有TDD迭代、visual/logic/review协作、图形HIL编辑、领域spec加验证反馈；摘要未建立新的执行/控制保证、失效条件或预算可比的机制归因。不是因软件、物理试题或接口题名排除，也不把工作流改写为状态术语当突破。
- 2509.24163 robotic stacking、24651 ingredient teaching：增量在任务偏好dataset/示例顺序，没有建立foundation model或通用Agent机制新边界；机器人类别未整体排除，其他VLA/控制线索继续保留。2509.24505 EQUISeg已撤销task-specific fusion关闭，完整题摘的模态退化/贡献调节链保留为日期待核潜力，详见末节。
- 2509.24597 dyslexia、24267 cycle medical image、25143 TemMed、24888 MMRQA、24739 ViPET、24231 EVLF：完整题摘将增量限定在脑障碍模拟、MRI/PET诊断/质量/visit tracking等领域研究应用；没有把该领域Data/Evaluation转入当前暂缓的AI for Science。TemMed确有临床时间推理局限，但原摘要没有建立当前主线可采用的通用模型机制结论，非仅看医疗标题关闭。
- 2509.24958 Doctor inquiry、24922 MASLegal、25286政治取向、25283人口心理：领域评价/现成量表或人群模拟比较，没有建立新的模型/系统机制、通用可验证评价协议或直接安全设计修正。局部结果本身未被否定；只是没有该项目贡献链。

初始29项的范围/月退出经必要纠错校准后分为：10个October公告月ID `2510.03293,2510.01269,2510.00063,2510.12803,2510.15917,2510.02371,2510.03283,2510.00069,2510.00060,2510.02375` 不由Sept提交搬入Sep30；18个明确标题范围外为 `2509.25077,2509.24895,2509.24866,2509.24819,2509.24800,2509.24761,2509.24655,2509.24556,2509.25284,2509.25121,2509.25044,2509.24995,2509.24875,2509.24194,2509.24185,2509.25034,2509.24978,2509.24463`，分别是领域depth/蛋白/语言应用、无线/交通/卫星/医学/水库/音乐应用或普通视觉GNN/时序模型，仅支持标题明确的范围退出，不冒充完整题摘关闭。另1项BiHDTrans 2509.24425当前官方有withdrawn信号，已读完整摘要/必要撤回说明并单列撤回，不再写作没有可见纠错线索。

原潜力列曾含PoseDiff 2509.24591；现按官方撤回排除，其视频到动作摘要只保留为失效稿身份记录，不再属于潜力或日证据请求集合，详见末节。

余下未请求的models31和agents40是已发现过宽查询库存，不是已经构成当窗相关贡献的普通待办；本窗日批次缺失仍阻碍有效公开窗口限定，不继续把全年/当月库存变成队列。恢复公告日证据后重设真实日批次和主题补检，不能宣称这些库存无遗漏。

继续机构源：15:38左右四个官方域日期查询的实际结果存 [targeted-recovery-search.json](supplement-20261007/targeted-recovery-search.json)，有旧年Meta结果/当前Hunyuan入口，不是有效日期过滤；Meta global_search?page=5搜索片段打开实际400 Timeout。DeepMind Publications `/page/2/`可读，30条日期列表中10/30→09/29相邻，没有Sep30字段；News `/blog/page/5/`只月份，定点打开邻接CodeMender/Robotics1.5原页分别10/06、09/25后止，不做全月题摘。原件见 [extra-official-lists.json](supplement-20261007/extra-official-lists.json)、[deepmind-neighbor-dates.json](supplement-20261007/deepmind-neighbor-dates.json)。DeepMind selection有限恢复不补Google Research或全站召回，列表日期不重置论文首公开。

## 具名关闭、复用与剩余请求

- GLM4.6：Sep30官方release事实已恢复，核心模块SHA256 `6dde83a7bceacd9fcb2a915ad07340ae6eecb9d8b0cf68d7a86f89368fd47b8a`与旧09/30保存模块相同。完整核心说明为更难CC-Bench/任务指标、200K及输出效率发布主张，未披露新架构、训练目标或纠正评价盲点的证据；复用既有关闭并在本轮核身份，不因机构/版本或Books覆盖排除。没有采用其性能宣传。
- Google两Blog：原核心分别是离散gadget/验证器与DS/DE/HC角色型PHA；可有方法贡献，**不因医疗题名或局部实验排除**。当前Sep30 Blog未提供独立新release/revision事件，相应介绍事件关闭；所链2509.18057/2508.20148论文首公开日仍未核，不把较早submitted当窗外证明，也未重新评价历史全文。
- 原本日七案例家族1个及其Peirce复核保留；跨日Sora/Sonnet/Claude Code三个事件去重，旧论文安全复核只作具名版本复用线索，不迁归本日。
- 外部材料请求：官方2025-09-30 arXiv公告/list，至少含实际公告日与论文ID对应，以及两Google原论文必要first-public证据；Google Research首次公开日库存、Meta、Hunyuan、Z.ai Research、MiMo Blog、MiniMax Agent历史目录。DeepMind有限selection已恢复；Qwen当前配置有前后侧但历史完备性未披露。可接受作者/机构同时发布的精确正文公开日证据作定点替代，不能以搜索参数、提交日、公告日程推导替代；三撤回不再索日以继续采用。
- 当前新收0个确定当窗家族；Dewey首校准与来源复核已获，四项返修已落实，整体未通过且待窄复查。来源扫描为真实有限检查/精确外部缺口，不授本轮完成或Coverage通过。Books没有新差额建议、没有写入，非任务量停止；最新作者停点见末节。

## 作者精确停点：Euler，2026-10-07T15:45:50+08:00

按root明确调度保存10/01自身作者停点，随后切到11/01独立Review；不是本轮完成，也不把未获校准、尚待准入后的深审或非作者复核称外部终态。Dewey将独立审本日。

实际新增确定家族0；本日旧七案例家族1保持候选/日期/评分/论证；跨日3家族去重；GLM与Google2个介绍事件合计3项拟关闭，另96完整題摘中的20项具名拟关闭待抽检。125恢复ID不是日窗分母，29条只做范围/月退出。仍缺官方公告日/历史目录；models31、agents40未请求宽库存明确不授召回，不将宽列表作为默认逐篇队列。

已执行`python3 scripts/validate_research.py --report papers/2025/10/01/README.md`通过V3接口校验；初次时间附注/双表重复ID错误已修，未改校验脚本。局部Markdown目标检查无缺失；`git diff --check`限定本日路径通过；实际diff复查旧候选行与原核心论证未变。写入范围仅本日README、supplement记录与其原件目录；无Books/State/索引/合同/脚本改写，无stage/commit/push。结构检查不替代Dewey语义验收。

可安全保存此作者停点，但不是作者READY或报告完成。恢复位置：先接收首批校准（代表RServe/NVFP4/PTG及安全反证、三事件关闭和20项抽检），取得具体日公开原件后仅重开对应线索；先限定日批次再范围/完整題摘，确认身份与必要版本后按准入深审。普通工作继续条件与外部材料请求分开，未宣称新候选Evidence或Books Gate通过。

## Dewey首校准返修与最新作者停点：Euler，2026-10-07T16:25:22+08:00

按root明确授权，11/01独立Review停点保存后切回本日作者；重新实际读取主AGENTS、当前研究/Report合同、每日来源/主题说明、统一Prompt、ROADMAP、路由checkpoint及本日完整Report/补查记录。已实际读取[Dewey首批独立复核](supplement-first-review-20261007.md)，不由Euler自审本日，不把11/01证据授本日覆盖。下面覆盖R1～R4及连带的目标日前News措辞；Report原窗口/七案例家族/日期/5分和核心论证均不改。

### R1：三撤回与有界纠错检查

作者实际解析本日四份Atom全部125个唯一ID的Comments，纠错相关命中4项：PoseDiff、Social Science、BiHDTrans与已隔离的NVFP4 Eq2 typo。定点读三份官方abs页首、Comments及history；未打开125个abs、未遍历版本史或附件。实际web工具返回保存在[euler-repair-official-web.json](supplement-20261007/euler-repair-official-web.json)，其中包括三份官方页及两Google入口首查输出；后述列表定位是实际后续open读取，不伪装成首查完整页。

| 身份/精确当前状态 | 官方证据位置 | 当前处置 |
| --- | --- | --- |
| [PoseDiff 2509.24591v2](https://arxiv.org/abs/2509.24591) | 官方162行，L8 withdrawn，L21实验设置/指标严谨性影响比较公平，L30 v2 withdrawn（2025-10-30） | 从原潜力分离为撤回排除；摘要仍有收益不恢复权限，不评分/采用 |
| [Social Science 2509.24877v3](https://arxiv.org/abs/2509.24877) | 官方162行，L8 withdrawn，L21语料、方法、框架、结论根本重构，L31 v3 withdrawn（2026-09-05） | 从原taxonomy贡献关闭分离为撤回排除，不采用旧稿 |
| [BiHDTrans 2509.24425v2](https://arxiv.org/abs/2509.24425) | 官方168行，L8 withdrawn，L23方法局限/实验缺陷，L32 v2 withdrawn（2026-09-10） | 从原19标题退出分离；作者另读当前完整摘要/必要说明，不再称无可见纠错 |

以上日期只标当前版本/撤回身份，不是本轮核定的公告公开日，不生成本窗修订事件。三项不再列入日证据请求、潜力或Books链路；旧v1可下载也不恢复失效稿结论。NVFP4纠错命题保留必要精确事件/版本请求，当前v2公式不回填2025。

### R2：Qwen实际配置边界

本轮作者再次实际解析[qwen-api.raw](supplement-20261007/qwen-api.raw)的60个`date`并转Asia/Shanghai，不依赖配置顺序：最新是Qwen-Image-Edit-2511，raw `2025-12-23T05:08:30.000Z`、BJT12/23；Sep30对象0。前侧Qwen3-Max raw `2025-09-24T04:00:00.000Z`、BJT09/24；后侧DeepResearch raw `2025-11-12T20:59:26.000Z`、BJT11/13。这里只核日期，不用小时门限筛新增。Report及当前来源表已同步；“最新止09/24、没有后侧”撤销。真正缺口是该配置是否完整保存历史事件，不是请求/解析失败，不重读60篇正文、不授全站零事件。

### R3/R4：EQUISeg重开，EOE混合优化

作者再次实际读取[CV/RO Atom](supplement-20261007/arxiv-multimodal.raw)中2509.24505v1的完整题摘：优势模态退化使整体性能受损，equal encoding、四阶段CMTB与SGM mutual guidance调节贡献并评价degraded conditions。原“task-specific fusion没有机制边界”关闭撤销；保留“依赖失衡→互引导/贡献调节→退化条件下融合选择”潜力，唯一拟owner为`MULTIMODAL-REPRESENTATION`/Ch23。当前不声称新颖、稳健已证明或可泛化；仍缺官方公开日，若落窗才定点读精确核心、balanced baseline、各模块消融、退化协议及额外代价。未因Books已有融合关闭，亦未提前作采用/已有覆盖判断。

作者再次实际读取[模型Atom](supplement-20261007/arxiv-models.raw)中2509.24436v1完整摘要：先AdamW，再当前/最佳expert tensor之间crossover、PSO和mutation。记录改为“AdamW与expert参数演化混合优化”，撤销“参数演化替代优化”；仍保留潜力，不采用作者吞吐/模型缩小数字，不返修扩读全部附件。

### 本日Google真实入口定点回源

本轮在本日上下文实际web打开[DeepMind真实第2页](https://deepmind.google/research/publications/page/2/)，后续open完整读L113～148：L115 selection、L117总265，L118～147共30卡，L118为10/30、L119为09/29，本窗Sep30位于该相邻边界而无同日卡。停止第2页，不请求更早第3～9页，不把`?page=3`当分页；根本权限仍是所列selection，不是机构全量首次公开。只读本窗定位和卡片，未深读窗外论文。

[Google pubs](https://research.google/pubs/)默认入口实际可读，首次输出710行，保存定位请求再次输出662行；两次L125均为2025计678，L372～380均为Title/Year排序与默认1～15/11597。入口可达，curl18s超时保留为执行事实而非必要入口不可读；年份/会议发表标签仍不能证明Sep30首次公开，不把678全年条目扩成队列。Report与当前来源边界已同步。实际新联网是三撤回页及这两Google入口/定位读取；其余来源沿用经Dewey核实的本日真实响应，不宣称本轮重新联网14站。定位读取实际工具输出另保存[euler-repair-google-web.json](supplement-20261007/euler-repair-google-web.json)，未制造稳定总行数/全文指纹。

### 当前归并、权限与续审位置

125恢复ID目前精确分账：75项September身份潜力（原76减PoseDiff/October AMemGuard，再加EQUISeg）、18项完整题摘贡献关闭、3项撤回、18项标题范围退出、10项October月份退出、AMemGuard 1项October恢复线索；合计125，均不等于本日候选分母。原96题摘读取范围不抹去，BiHDTrans另作必要纠错读取；Dewey原74项潜力及18项贡献关闭的受限校准可复用，不能回填历史Evidence。机构3个旧家族去重与GLM/Google三事件受限关闭维持。

实际新增确定当窗家族0、旧七案例家族1保留；撤回排除新增3、漏关重开1、EOE机制描述与Qwen事实修正；没有新增评分/Books差额或写入。现无作者尚未执行的R1～R4修正，**普通剩余是非作者对这些返修与正文自包含作窄复查**，不是外部终态，不写READY或全日完成。仍缺官方Sep30 arXiv日批次/具名公开日期、两Google论文first-public和列明机构历史库存，恢复条件沿用上节；日期未恢复前不泛读普通held全文，不扩models31/agents40宽库存。

变更仅本日README、此补查记录及新官方web原件；11/01写入仍只属于独立Review记录。本日首校准file是Dewey所有，未修改。恢复时相关路径已有其他任务暂存内容，本轮不调整索引、不stage/commit/push，保留已有dirty。机器校验与链接/diff检查在写后执行，结果另附；没有新Books/State/索引/合同/脚本改写。

写后检查（2026-10-07T16:27:36+08:00）：V3 Report接口校验通过，六节仍为1～6；限定10/01 README/补查记录与11/01独立Review的`git diff --check`无诊断。当前已核本地链接分别9/21/2个无缺失，新增Google原件链接随后同样实测存在；两份新web输出均可JSON解码为实际工具字符串。与恢复时已有暂存版本定点比较，原窗口、补充窗口、七案例候选整行（含原公开时间/评分/处置）完全相同。此为作者格式/范围检查，不是Dewey窄复查或全日验收。
