# 2026-03-09 来源遗漏补查（2026-10-09）

作者：supplement_20260309。补充窗口：2026-03-08 ～ 2026-03-08（北京时间自然日）。只 own 本日 README 与本目录。原 72 行 V3 已验收现状为冻结基线，不恢复 legacy，不打开旧 15+3 队列，不扩其他日期/Weekly/年份，不写 Books/LS/index，不 stage/commit/push。

## 1. 冻结与有效审阅

[冻结 baseline](./SUP_BASELINE_20261009.md)为11159字节，SHA256 `92490ae58becb4a628d4a1f3f9c31dd79595e568963e4d72bff5343820005de2`，与本轮启动 README 相同。原窗口03/08T09→03/09T09、零确定候选、连续§4及原 D1/H1保留，旧 root Source/日期隔离审阅仍有效，不等于本轮补查 DAY。原[来源记录](./V3_SOURCE_AND_DATE.md)中已读的邻接日期 metadata 可对新的03/08日做窄比较；不复用 legacy54/527筛选、评分或审阅标签。

启动已读 AGENTS、当前研究/Report合同、Prompt、ROADMAP、来源使用/Daily/arxiv/recovery与2026路由。本轮压缩恢复误用较宽文件区间，工具输出带入了Weekly表和LS2025段；没有执行这些来源/年份的扫描或任务，后续仅目标段，不声称从未加载。Books只读了相关上下文及Ch23连续/离散、rate–distortion与邻接接口，Ch24核心生成责任；未写 Books。

## 2. 14 Daily 来源与实际停止

以下有限 metadata 的具体字段/入口及旧读数见原来源记录；旧标题/题摘和审阅不扩池。既有相邻日期跨越03/08，自然日窄核不改变旧时间裁决。下表的“复用”不代表本轮重新抓了相同列表，更不代表全机构历史覆盖。

| 来源 | 实际本轮范围与停止 | 结果/局限 |
| --- | --- | --- |
| SRC-OPENAI | 新抓官方RSS [原响应](./SUP_OPENAI.raw)，按pubDate核03/08自然日无行；原精选和相邻03/09Promptfoo保持窗外 | 已检查有限feed；不证明删去历史 |
| SRC-ANTHROPIC | 复用Research内PublicResearch原日期邻接03/06→03/13；03/08不在条目中，目标段停止 | 已检查有限公开目录 |
| SRC-GOOGLE-AI | 复用DeepMind page3跨Feb～May、GoogleResearch March archive两页2/2；邻接03/06→03/10，03/08无Blog行；pubs日级目录原缺口仍在；补搜限定官方2026/Mar8仅噪声，未采用其他年份 | Blog有限段已检查；pubs历史目录受阻 |
| SRC-META-AI | 原Research空响应/日期入口缺口；本轮curl连接重置，官方域名Mar8/2026有界补检无可用当日原始目录 | 受阻，不由搜索无结果证明零发布 |
| SRC-QWEN | 复用公共article/retrieval type=qwen_ai/en-US 40/40，display/published两个原字段邻接02/16→03/19；独立比较03/08 | 已检查可见40，不推隐藏/删除历史 |
| SRC-DEEPSEEK | 复用Research10邻接02/25→06/24与News5；本轮官方域名精确日补检无恢复ViewAll历史 | Research有限段已检查；News隐藏段仍缺 |
| SRC-MOONSHOT | 复用kimi.com/en/blog19可见行，02/09→04/20相邻段；03/08无行 | 已检查有限目录，不沿用旧platform永久gap |
| SRC-TENCENT-HUNYUAN | 复用publicList renderType0/page1/size20全可见11/11，02/13→04/23；定点发现官方HY-WorldPlay News March8 WorldCompass artifact，本记录§5处理 | 有新增artifact事件；11/11不保证GitHub事件全覆盖 |
| SRC-ZAI | 复用Research可见有限相邻02/21→03/15；SeeMore未知未扩队列 | 已检查有限可见段 |
| SRC-BYTEDANCE-SEED | 复用get_article_list_v2 2026papers offsets0/20与blog offset0，papers03/02→03/12、blog02/14→04/01越窗停止 | 已检查目标有限切片，不扫82/242总表 |
| SRC-BAIDU-ERNIE | 复用blog两页十可见行，02/06→04/15跨03/08；不扫更老段 | 已检查有限目录 |
| SRC-XIAOMI-MIMO | 复用Paper8邻接02/03→03/13；Blog15无日期与已恢复有限frontmatter不足对日；本轮官方域名03/08补检未恢复 | Paper有限段已检查；Blog当日映射受阻 |
| SRC-MINIMAX | 复用中文redirect目录13行，02/12→03/18；Agent技术目录Apr27不归入03/08 | 已检查有限目录 |
| SRC-ARXIV | 三个主题提交发现查询start0/max100，各返回35/21/9且total一致，无未处理分页；65出现/59唯一题名，实际42唯一完整当前题摘，分解在§4 | 首公开日不足；不是59全文队列或42 Evidence |

## 3. 查询、日期语义与停止

发现提交跨度UTC `202603071600～202603081559` 对应03/08北京时间自然日，使用`encodeURIComponent`编码完整查询。MAIN：CL/LG/AI + language/transformer/agent/optimization/foundation/MoE；MULTI：CV/RO + multimodal/diffusion/world/vision-language/VLA；SYSTEM：DC/AR/PL/OS/PF/IR/MA + language/GPU/transformer/agent/memory/retrieval/expert。原始XML：[MAIN](./SUP_API_MAIN_CORRECT.raw)、[MULTI](./SUP_API_MULTI_CORRECT.raw)、[SYSTEM](./SUP_API_SYSTEM_CORRECT.raw)。三组均已读完整返回题名，实际total分别35/21/9，少于100，无next页可执行工作；跨组去重59。只选择可能主线相关项读42完整当前摘要，其余17题名明确领域/应用或通用空间索引，不声称读了其摘要。没有按比例/配额留存。

首轮手动URL编码漏掉upper bound中的“20”，响应实际echo `202603071600 TO 2603081559`，total16543及Mar9越界项；该响应无Coverage/零命中权限。[首轮失效响应](./SUP_API_MAIN.raw)、[诊断](./SUP_API_DIAG.raw)与单日/advanced失败仍留存，但不是服务器改写证据，也没有按16543继续分页。正确三组只授提交发现；API `published`、Submitted、Updated、注册日期均不等于first-public。

原arxiv availability说明普通公告Sunday–Thursday美国Eastern20时；03/08北京时间自然日没有普通公告机会（03/08Eastern周日20对应03/09BJT），只解释日程，不推“零研究”。本轮仍按原始官方/作者事件恢复：MSR具体两文、Compression项目精确历史、HY-WorldPlay、Karpathy官方仓库、CSA官方说明。精确日补检没有恢复其他必要当日首公开正文，后续只请求具名身份，不扩一周或全年。必要日期材料得不到时不读全文绕日期；已多读Compression v1 core保留但不正面采用。

## 4. 实际42完整题摘逐条分解

以下是贡献筛选，不是确定当窗候选清单。版本是API实际返回；v2/v3摘要只作为家族潜力线索，不冒充03/08当时v1。34项有具体潜在机制/评价差额但必要first-public/当时精确版本未证；7项具体EX；1项旧结果撤回。不评分日期保留项。34项恢复需求统一见§6。

| 精确发现身份 | 摘要新增内容与本次处置 |
| --- | --- |
| 2603.07300v2 AutoResearch-RL（恢复v1题摘） | root指出current admin withdrawal后，官方current明确v2 withdrawn/acceptable-submission政策违规；v2不入选、不评分、不进入Books，非访问故障。官方v1只写“newer version withdrawn”，v1仍可用且题摘相同，不能把v2撤回外推整family；仅v1中PPO实验meta-learner/受限收敛潜力与必要公开日、有效性尚未确认，留v1日期/版本/有效性隔离，不采用保证。原响应见SUP_WEB_NINETEENTH.json |
| 2603.07335v1 VisualScratchpad | 推理中以视觉概念分析作scratchpad，可能改变视觉中间证据接口；日期保留 |
| 2603.07360v1 Yerkes-Dodson agents | 环境压力与协作非单调关系的局部实验可能修正multi-agent配置选择，不因小仿真排除；日期保留 |
| 2603.07379v1 Agentic RAG SoK | POMDP化、planning/retrieval/memory/tool分类和研究方向；未见新增执行机制、经验证的新有效性条件或设计反证，具体EX；不采用其安全保证 |
| 2603.07389v1 MARIGOLD | 双层优化降低多任务gradient balancing成本，潜在改变训练梯度分配而非仅框架名；日期保留 |
| 2603.07392v1 OAKS | 知识流在线适应评价可能暴露静态知识测评遗漏的适应边界；日期保留 |
| 2603.07404v1 LoRA-SP | 能量/SVD引导VLA LoRA容量与singular-value路由，改变适配容量分配；日期保留 |
| 2603.07416v1 DualSpec | Search entropy与Visit容量不同speculation方式及semantic verifier，改变agent action预执行收益条件；日期保留 |
| 2603.07431v2 OrthoFormer | 隐状态instrumental variable/control-function与梯度隔离，理论机制可能改变因果混杂判断；日期/版本保留 |
| 2603.07432v1 mobile-agent generalization | instance/template/app级泛化拆分，可能修正online RL对移动Agent泛化的评价结论；日期保留 |
| 2603.07433v2 Data Agent | 数据选择的端到端动态复合奖励优化，改变选数据loop而非静态质量打分；日期/版本保留 |
| 2603.07461v1 Dual-Stream | 小语言模型分流head/mixing的可解释性与质量取舍；不因29M模型排除，日期保留 |
| 2603.18029v1 per-layer supervision | 分层监督形成可验证模块接口，可能改变“模块化”由probe自证的判断；日期保留 |
| 2603.07474v2 taxonomic generalization | 跨模态分类泛化与相似度counterfactual比较可能改变视觉/语言贡献归因；日期/版本保留 |
| 2603.18030v2 Quine | Agent作为POSIX进程、生命周期与IPC原语，潜在改变runtime执行/身份界面；日期/版本保留 |
| 2603.07482v1 LateFusion | 架构stream independence与解释责任，潜在改变混合隐藏状态的可归因性；日期保留 |
| 2603.07496v2 HAE（另读v1） | v1将威胁按认知/执行/群体分层、评价现有防御并提research gaps；分类和倡议本身无新验证的机制/有效性条件，EX；不声称已有defense实现 |
| 2603.07523v3 FRONT | frequency transform one-shot知识传递，潜在KD容量/训练代价替代方案；当时版本未知，日期/版本保留 |
| 2603.07528v2 TableMind++ | 不确定性驱动程序化tool agent，潜在改变工具推理失败路径；日期/版本保留 |
| 2603.15658v1 store routing | memory stores成本敏感路由及oracle coverage边界，潜在改变memory检索选择；日期保留 |
| 2603.07599v1 StyleBench | 多轮speech情绪/速度/音量/音高强度控制评价轴，不凭新增benchmark数量准入，潜在控制评价盲区仍值得恢复；日期保留 |
| 2603.07607v1 MAS-H2 | Kubernetes CPU应用的战略/预测/执行分层及pod/node规划，没有模型训练/推理负载或新LLM agent机制；普通cloud控制方案不因agent标签或系统类比进入主线，具体范围EX |
| 2603.07615v3 Compression（另读v1 core） | 单信号LoRA函数/共享hash向量作为payload替代latent，有明确表示机制潜力；MSR目录日期无法绑定当日v1全文，日期/版本保留，不进入Books |
| 2603.07654v1 FedCEF | 非凸复合优化的proximal压缩、error feedback/control variates可能改变通信与收敛取舍；理论不自动排除，日期保留 |
| 2603.07430v1 DTPSR | global/local与frequency文本先验分责改变diffusion条件输入；日期保留 |
| 2603.07476v1 EVLF | 生成dataset distillation的早/晚视觉语言fusion，潜在改变数据合成时融合选择；日期保留 |
| 2603.07484v1 HSC-VLA | high-level任务mask过滤场景给diffusion低层policy，潜在改变clutter→grounding失败接口；不是仅引用86.7%数字，日期保留 |
| 2603.07540v1 UniLongGen | 长interleaved图文中的active visual-context污染与curation，不只是扩大context长度；日期保留 |
| 2603.07545v1 DreamSAC | Hamiltonian/world model中的symmetry exploration/curiosity，服务模型动力学与控制机制，不因物理语义自动作AI for Science；日期保留 |
| 2603.07619v2 overthinking | VLM反侧/confounder propagation可能修正“更多推理更可靠”，负面结果不排除；日期/版本保留 |
| 2603.07647v1 TempoFit | 冻结VLA按层temporal KV检索和norm约束，潜在改变长程记忆适配兼容；日期保留 |
| 2603.07659v2 SCI VLM | 多轮self-critical/counterfactual推理及model-specific鲁棒评价，潜在适用条件而非通用保证；日期/版本保留 |
| 2603.07697v1 MMDM | joint/pose层Kinematic Attention Aggregation学习可复用motion priors，可能改变motion生成/修复表示；日期保留 |
| 2603.07700v1 TDM-R1 | 不可微reward surrogate与逐step确定信号，改变few-step diffusion强化学习接口；日期保留 |
| 2603.07456v2 UAV EPG | UAV拓扑/功率领域优化，LLM只生成utility权重；不是LLM自身规划或系统机制增量，具体范围EX |
| 2603.23533v3 MDKeyChunker（另读v1） | 当前官方AB/Comments明确v1-v2 results withdrawn；只排除旧结果采用/评分，不误称整个v1撤回；Oct2 v3不填Mar8证据。root独立核此纠错信号通过 |
| 2603.07683v1 microarchitecture thesis | 轻量ML预测prefetch/off-chip/load重复，摘要未建立服务LLM计算的workload/设计边界；一般CPU研究不以系统类比引入，具体范围EX |
| 2603.07685v2 Megatron Core MoE | parallel folding与跨stack co-design可能改变attention/expert布局与资源取舍；日期/版本保留，未常规扫描Weekly Megatron源 |

四项题名初排经root指出含糊后定点恢复完整AB：07448与19284撤销标题EX并保留具体机制潜力，07618与07650读后给具体理由关闭；未扩大其余题名队列。实际API42题摘＝34潜力+7 EX+1结果撤回；加表外MicroCoder1潜力，共35具名日期/版本项。

| 补读精确身份 | 完整AB后具体判断 |
| --- | --- |
| 2603.07448v1 calibrated tabular Transformer | 离散context词表+adaptive Gaussian labels及ordering/time-delta/calibration消融可改变Transformer表示与校准选择；撤销按tabular标题EX，日期保留 |
| 2603.19284v1 CDEoH | 显式category-diversity population management抑制LLM搜索早收敛，改变搜索人口而非只领域任务成绩；撤销标题EX，日期保留 |
| 2603.07618v1 SMAT | 既有curriculum按human gait/设备重量/稳定human下助力/共同训练四阶段应用，MyoAssist/26肌肉及5subjects证明特定助力，不提出新基础模型/优化算法或一般训练有效条件；读完整AB后贡献EX，不因外骨骼标签单独关闭 |
| 2603.07650v1 off-world exploration | GP interest/risk beliefs+AOI路径规划与lunar仿真，没有learned dynamics/LM/VLA新机制；传统领域规划范围EX，不以物理场景单独排除 |

另17唯一题名关闭只按标题范围，不声称完整题摘：07299物理symmetry发现、07370mmWave、23531政治stance应用、07444经济研究、07472大肠杆菌AI for Science、07521sketch识别、07572工业时序应用、12287船舶轨迹描述；07294鸟类助手、07361wildfire、07403牙科caption、07443medical agent、07489snapshot成像restoration、07504医学shape、07562脑肿瘤world model、07652shape对应应用、07517一般spatial index。已知明确标题的领域应用不因LM/agent/diffusion标签进主线；其中未披露安全/纠错信号，若后续有直接主线机制反例仅重开受影响项。

除API42，还实际读MicroCoder、IPI、WorldCompass三个独立完整论文题摘用于身份/日期或直接引用恢复（后两是窗外依赖，不算新增候选）；Compression官方摘要与API是同家族，不重复题摘计数。CSA、HY-WorldPlay、autoresearch核心官方说明不是论文题摘数量。旧18没有重新读入本池。

## 5. 具体官方事件、反侧与有限恢复

### WorldCompass artifact（确定03/08事件）

[HY-WorldPlay官方News](https://github.com/Tencent-Hunyuan/HY-WorldPlay)明确2026-03-08开源WorldPlay-8B RL后训练代码WorldCompass；当前[worldcompass README](https://github.com/Tencent-Hunyuan/HY-WorldPlay/blob/main/worldcompass/README.md)是使用说明，有数据latents/随机camera action/多GPU与96GB前提以及BF16 VAE可能不稳定，不能替代当日精确代码。原[论文2602.09022](https://arxiv.org/abs/2602.09022)的clip-level rollout/互补reward/negative-aware机制属早先论文，不因artifact发布搬到03/08或重复创新评分。

本次增量仅“作者宣告实现入口公开、可尝试复现”的版本事实；Design Delta1（局部实现可用）+System Reach1（一个world-model后训练组件）+Durability1（版本事实）=3，已关闭/仅报告。不授代码机制已核验、性能重现或生产/硬件普适保证，Books新写0。root准入校准接受这种受限VersionFact。定点在本日baseline、原来源记录和02/10、02/11正式Report查WorldCompass/ID/HY-WorldPlay均无命中，只说明这些已处理记录没有相同artifact事件；没有以全库无命中冒充绝无旧家族。当前Repo/README web证据留[原响应](./SUP_WEB_SEVENTH.json)与[恢复](./SUP_WEB_NINTH.json)。

精确快照有界尝试：commits path=worldcompass至03/09T00Z空，README path最近2commit分别93e866…03/09T08:58Z及4d527b…03/09T12:12Z（[原响应](./SUP_WORLDCOMPASS_LATEST_COMMITS.raw)）；旧快照cache miss。后提交不推翻官方Mar8日期，但无法证明当时具体实现。日期无需追时刻，无无限clone/遍历，缺当时代码不阻塞仅报告版本事实。

### CSA安全说明（贡献EX，非因机构身份排除）

[官方HTML](https://labs.cloudsecurityalliance.org/research/csa-research-note-image-prompt-injection-multimodal-llm-2026/)明示Published March8；[原响应](./SUP_CSA.raw)。完整核心和直接引用IPI题摘已读；Security Analysis/Defense/Recommendations是文献转述与成熟多层防御建议，无新实验或经验证的新有效性条件，具体EX。root实际全149行独立核此判断；不采用说明中的作者benchmark或全VLM架构/安全保证，不为补量扩读14references。PDF“unofficial AI-assisted”仅限制官方权威角色，不单独构成贡献排除。被引用[IPI2603.03637v1](https://arxiv.org/abs/2603.03637v1)题摘的GPT4-turbo/COCO/12策略范围不能被转述成跨GPT4V/Claude/Gemini/LLaVA成立，原FLLM2025论文身份也不搬到本窗。

### Autoresearch（首次事件窗前；本窗普通维护无新机制）

[官方repo](https://github.com/karpathy/autoresearch)核心是改train.py、固定5分钟、保留/丢弃val_bpb结果的实验loop；官方[36 commits](./SUP_AUTORESEARCH_COMMITS.raw)earliest b11d6f…2026-03-06T21:58Z为03/07BJT，secondary“Mar8launch”不改首公开。03/08BJT的docs/固定val shard/traceback instruction/download workers普通维护不证明新验证条件；不采用以后NaN修复。只核本窗相关dates和必要program，不展开每条历史PR。

### MSR两文：目录不等当日精确全文

[MicroCoder-GRPO / Breaking Training Bottlenecks官网](https://www.microsoft.com/en-us/research/publication/breaking-training-bottlenecks-effective-and-stable-reinforcement-learning-for-coding-models/)只作有界表外恢复，实际官方[HTML](./SUP_MSR_MICROCODER.raw)datePublished=03/16，搜索目录“Mar8”不优先；无当日first-public正文，作为日期/版本线索，不由03/16目录断言论文从未更早公开，不冒称已审重复。需要2603.07777首次公开作者正文及当时版本；此次仅恢复官网目录身份，未将其加入提交跨度34项或本日确定候选。

[Compression官网](https://www.microsoft.com/en-us/research/publication/compression-as-adaptation-implicit-visual-representation-with-diffusion-foundation-models/)[HTML](./SUP_MSR_COMPRESSION.raw)datePublished=03/08但dateModified=06/23，当前指向无版本arxiv，不能证明03/08精确全文可用；作者当前[project page](https://compressionasadaptation.github.io/)Paper实际跳v3。官方project [commit响应](./SUP_COMPRESSION_PROJECT_COMMITS.raw)100条已越过目标段进入2020模板，停止不按100全读、不过度分页；恢复[Mar7 index的API原文](./SUP_COMPRESSION_PROJECT_MAR7_API.raw)，完整6508字节只有题名/作者、Paper/arXiv/Code空href，无机制正文。不能以当前v3或提交Mar8冒充当日v1全文，root日期/版本隔离校准通过。

已读[exact-v1 HTML](https://arxiv.org/html/2603.07615v1)[原响应](./SUP_CORE_COMPRESSION.raw)方法3.1～3.3、评价4及相关E配置：per-signal frozen diffusion LoRA/hash vector、entropy/quantization、编码端importance-selection额外indices；局部UVG/HEVC832×480×81感知压缩与PSNR/text失真反侧，重编码成本且无生产codec保障。Ch23现有rate–distortion/decoder identity尚不拥有这种adaptation-as-payload具体机制；潜在差额成立，root题摘校准认为若当日全文成立可score6。但日期/精确版本未过，不评分、不授Evidence完成、不写Books，所读core只保留恢复材料，不作为本日新结论。无需为了已隔离项追加无关证明/全附件。

## 6. 本窗精确外部材料需求与普通停点

新增34项日期/版本请求（同一家族只一次）：07300、07335、07360、07389、07392、07404、07416、07431、07432、07433、07461、07448、19284、18029、07474、18030、07482、07523、07528、15658、07599、07615、07654、07430、07476、07484、07540、07545、07619、07647、07659、07697、07700、07685（均2603前缀）。需要各具体家族2026-03-08首次公开正文的官方announcement membership、dated作者稿/项目原始记录，及该日对应精确版本；当时可能v1的名称不等于已确认v1公开。可接受原始官方公开批次、原作者repository可绑定当日正文的快照/发布说明，不接受Submitted/Updated/注册/推荐日、无全文的题摘目录或后来v2/v3。Compression特别需要Mar8 MSR正文链接/作者稿可用记录，Mar7空href和Mar8目录现状不足；恢复仅具体版本，重审相关机制及真实Books差额。34项不用于正面证据、评分、Books、Coverage通过或无遗漏。

新增H2来源请求只针对03/08：Meta Research日级原目录/归档；Google Research pubs当日公开论文目录；MiMo Blog15无date卡的当日原始映射；DeepSeek News ViewAll目标日隐藏段。旧H1与此重叠的材料一次请求，不重复重扫；可接受这些入口当日snapshot/API/body+日期。官方域名补搜出现别的年份仅噪声未采用。缺口不作零命中。

普通待办0。root非作者增量DAY语义通过：实际读正式六部分、42 API完整题摘和四条标题修复、CSA必要核心与官方WorldCompass March8 News、07300 Admin原说明/23533结果撤回，核14有限源查询/停止、date-only自然日与旧行/连续§4冻结。42题摘全部独读，17明确标题项未称全AB独审；其他原始入口复用有效记录，不冒称全抓取/原正文逐条复核。追加07300当前v2撤回轻量处理通过：v2退出链、官方仍可用v1仅隔离，不整family删除/遍历版本史；相同v1题摘不增加家族数。34 API潜力+表外MicroCoder1＝35具名保留，非候选/Evidence；确定新增WorldCompass artifact1仅报告，Books新写0。正式完成态V3、26处本地引用、原窗口/0候选/连续§4冻结及限定unstaged/cached diff-check实际通过，安全终态不授全Coverage/Evidence或无遗漏。没有Books写锁、LS/index改动或stage/commit/push；仅负责本日结束，不自领下一日。
