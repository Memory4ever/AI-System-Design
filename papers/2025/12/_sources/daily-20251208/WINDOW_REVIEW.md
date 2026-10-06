# 12/08 独立窗口原始观察与作者停点

本轮实际执行于2026-10-02，19:18:01+08:00启动，压缩恢复后重读AGENTS、研究/报告合同、来源每日组、Prompt、ROADMAP及本日停点。窗口 `[2025-12-07T09:00:00+08:00,2025-12-08T09:00:00+08:00)`，即Dec7 01Z至Dec8 01Z；没有从Weekly或前日报候选生成本日。

## 14来源的原始窗口切片

固定历史目录只复用[原始观察](../daily-20251201/RECOVERY_NOTES.md)中的入口、实际分页及邻接字段，本日重新判窗，不复制其他日报完成结论。

- OpenAI：本日RSS原生请求403，停止同接口重复尝试；此前实际成功的1243-item原始feed在Dec4 Australia19GMT与Dec8 Virgin00GMT/enterprise04GMT/Instacart06GMT相邻。本窗只相交Virgin00GMT，后两条在本窗之后。具名官方搜索恢复正确[Oliver Byers访谈](https://openai.com/index/virgin-atlantic-oliver-byers/)，实际读完整问答核心：Codex/Enterprise部署、品牌语音concierge、人类handoff、ROI及guardrails是企业采用经验，没有新的模型/执行机制或受控反证，贡献前关闭。网页只显示Dec8；feed钟点不外推为全站首发。曾打开同名`/index/virgin-atlantic/`实际为May22 2026，明确丢弃，不用于2025判断。
- Anthropic：原始publicationList Dec4 Interviewer17Z至Dec18下一条，夹本窗；不把当前修改时间当历史first-public。
- Google：2025Blog第1页Dec4 Titans/MIRAS至Dec10 DP，DeepMind第3页Dec3 Reward Features至Nov21，按本窗独立核邻接；仅目录主题范围。
- Meta：原始第4页Dec12/Dec1/Nov19至Nov10夹本窗；AdvancedIF目录身份不改变论文首公开。
- Qwen：旧站Sep23/新站空/部署无旧列表、错误_posts404、README有限替代，不能恢复2025旧目录，安全隔离。
- DeepSeek：正确API Docs Dec1 release与后续2026邻接；错误news路径已确认重定向，不能当2025正文，未再反复请求。
- Kimi：Overview实际26项最新Nov7、changelog Nov6，本窗无具名新条目线索，不扩日常commits。
- Hunyuan：Research skeleton/浏览器超时，All API11项全2026；2025历史目录不可恢复，隔离而非零事件。
- Z.ai：Research当前All两页15/18项至Dec8 AutoGLM/Dec7 GLM-4.6V及无更多，release notes Dec8/September30邻接。08具名实际重读对象144/145正文及结构化字段，见下；历史目录和上线精度缺口保留。
- Seed：原始2025paper首20/total94/has_more，Dec15与Dec2 GR-RL/Oct22夹本窗；Blog首20/total45，Dec16与Dec2/Nov27夹本窗。只用该精确邻接，不扩94或45项库存。PublishDate常见16Z是日编码，不能当钟点。
- ERNIE：原始第2/2页至Nov7及Nov21/Dec9邻接夹窗。
- MiMo：Paper8项Oct21/Jan8，Blog15项及部署路由HSS Dec19/Safety Dec18；Flash无date、旧More历史不全，不借相邻route日期，缺口隔离。
- MiniMax：原始英文13项/中文Oct27 M2至Dec23 M2.1夹窗，没有具名事件触发Tech Blog扫描。
- arXiv：实际四组`site:arxiv.org "7 Dec 2025"`查询，分别追加`(transformer OR pretraining OR mixture-of-experts OR optimization)`、`(inference OR "KV cache" OR GPU OR compiler)`、`(multimodal OR VLA OR "world model")`、`(agent OR retrieval OR evaluation OR "reinforcement learning")`，仅发现BSFA的提交日期线索，不能宣称零公告。有界补检[cs.OS首1–25](https://arxiv.org/list/cs.OS/2025-12?skip=0&show=25)实际total23及[cs.MA首1–25](https://arxiv.org/list/cs.MA/2025-12?skip=0&show=25)total211，仅浏览这两段相关标题，不展开全月。相关精确v1题摘及决定准入所需核心已按下文逐项处置；不是全月全文审阅或Evidence验收。

## BSFA：具体增量与必要反证

[2512.07011v1](https://arxiv.org/html/2512.07011v1)实际读完整题摘、§4.1–4.4/Algorithm1、§5.1–5.2/Table1。Submitted Dec7 21:20:12Z只证明提交，不证明本窗公开。具名announced检索未恢复实际公告，有限替代[作者官方仓库](https://github.com/Danielohayon/Block-Sparse-Flash-Attention)实际读README，未得到当时正文公开时刻；当前1commit或artifact时间不能自动证明历史可见性。

原来先近似估计重要block再省QK/PV；本文保留全部精确QK，按layer/head/query-block离线阈值比较block最大值，省略不选V加载、PV及其softmax归一化贡献，并总保留causal diagonal。这是selection位置/资源取舍的具体增量，但精确QK不意味着exact dense Attention；被删block不进入normalizer。16样本校准聚合top-k阈值不是每个输入恰保留k，实测density变化，超过最大query位置复用最后阈值也需分布漂移核验。

A10080GB、CUDA12.1、FP16、BM128/BN64、Llama3.1-8B-Instruct；RULER与LongBench协议分开。10序列/长度、10次运行warmup仅限定其latency估计；TTFT不是decode/总SLO保证。Sparge对照使用INT8 QK而本方法FP16，不能把差异全归因稀疏策略；A100比较FA2不是支持Hopper结论。Table1在128K某k配置相对accuracy下降约4%，不采用仓库“总保持99%”宣传。

实际Books对读`INFER-PREFILL` Ch43 Sparse Prefill段：约62–155行已有approximate discovery、selection/index成本、exact dense FA与fallback，但未把“全部exact QK后省PV”作为该段独立分支解释；相邻Ch42约25–55行定义phase/SLO、Ch44约25–55行定义decode真实依赖。潜在补点归唯一Ch43，不在Ch14/22重复写执行机制。日期未授，当前不正面整合；恢复后可在Dense FA/discovery分支前补：精确算score后再舍弃value work也改变softmax函数，省下的PV/V读取须覆盖阈值校准、QK仍全算和误差成本；target k不是固定执行预算。此为条件草案，不冒称已有覆盖或整合完成。

## Z.ai具名身份

实际JSON parser读取原生Research RSC对象144：`createAt=2025-12-07T16:00:00.000Z`、`createdAt=2026-01-07T02:44:32.087Z`、`updatedAt=2026-04-21T04:48:35.168Z`；对象145：`createAt=2025-12-08T16:00:00.000Z`、`createdAt=2026-01-07T02:51:10.889Z`、`updatedAt=2026-04-21T04:30:38.572Z`。createAt恰是BJT次日午夜、目录却以Dec7/8编码，createdAt是迁移，不授first-public钟点。

GLM-4.6V的native image/screenshot/tool-result输入输出增量与07相同家族，具名复用已实际读取的官方card和对象正文，不增加已确认本窗分母。AutoGLM正文及[原始Blog](https://autoglm.z.ai/blog/)实际说明开源Phone Use模型、工具链、Android适配、50+App demo及模型MIT/代码Apache2.0；不是新Phone Use算法首发，历史工作从2023/24延续。[当前官方README](https://raw.githubusercontent.com/zai-org/Open-AutoGLM/main/README.md)核心实际读到ADB控制、视觉模型感知、敏感动作确认/login人工接管、第三方或自部署base-url两条路径。相对云沙箱，开放真实设备适配使screen/data backend和执行权限成为需独立配置的release contract，保留这一具体安全/部署边界，不以“开源”本身或50App准入。原Blog“隐私永远留在使用方”不覆盖使用第三方推理端点；当前README已有Harmony/iOS、后续镜像依赖及Dec9截图，不能反填Dec8精确artifact。首次上线与当时adapter/confirmation协议安全隔离；不授私有化必然隐私保证、权限实现已验或生产可用。

## OS/MA具名贡献处置

实际读取相关精确v1完整题摘，必要核心只围绕决定准入的含糊事实补读，不把23/211目录总数称当天新论文分母。OS未来提交下界核对后不继续投入当窗审阅；早号与月身份均不直接归日。

### 15个arXiv潜在家族

| 精确v1 | 原约束→具体增量→需重新考虑的选择；限制 |
| --- | --- |
| [VLCs 04320](https://arxiv.org/abs/2512.04320v1) | LibTorch/OpenMP/OpenBLAS等库并发假定独占资源或非线程安全；process内library context隔离资源和同库多实例，不改库/OS的组合执行替代直接涉及模型host runtime。不是泛OS类比；不采用2.85倍为LLM服务保证。 |
| [AgentNet++ 00614](https://arxiv.org/html/2512.00614v1) | 平面DAG协作的通信/隐私压力；§3.1–3.5层级cluster与task/expertise/resource/load路由、knowledge sharing privacy budget耦合为具体替代路径。§4.2仅援引DP composition，Gaussian敏感度与知识表示、modular secure aggregation尚须核；不把摘要收敛/隐私宣称当已证明。§5.2及§6明确重组成本、同质agent假设，不能授1000agent生产能力。 |
| [BiRouter 00740](https://arxiv.org/abs/2512.00740v1) | 固定拓扑/集中规划依赖全局信息；局部next-hop同时考虑长期importance与当前context gap，并更新reputation，潜在协作route/资源取舍，不只是“self-organizing”名称。局部摘要收益不授全局最优或攻击安全。 |
| [SocialDriveGen 01363](https://arxiv.org/abs/2512.01363v1) | 生成trajectory缺可控social preference；egoism/altruism双轴条件与轨迹生成耦合，提供action-conditioned多样性/交互约束的窄线索，不仅更好交通指标。不授真实world dynamics或安全保证。 |
| [DMAS 02410](https://arxiv.org/abs/2512.02410v1) | 集中runtime单点及不可信通信；on-chain interaction cycle与cryptographic authenticity/nonrepudiation/conditional confidentiality是具体通信协议条件。保留威胁模型/链成本核验，不把签名授内容正确或无审查保证。 |
| [Network Sheaves 03248](https://arxiv.org/abs/2512.03248v1) | 异构agent的compressed latent未共享语义；联合拓扑/orthogonal alignment map及nonconvex dictionary closed-form迭代，潜在表示/通信目标对齐机制。不因6G/小图像模型排除，也不授LLM语义压缩已验证。 |
| [AsymPuzl 03466](https://arxiv.org/abs/2512.03466v1) | 开放roleplay混合多个协作难度轴；互补部分信息puzzle控制信息不对称，详细joint feedback可劣于简单self feedback，是窄评价反证。不从新benchmark本身准入，不授任意合作反馈策略。 |
| [SRPG 03694](https://arxiv.org/html/2512.03694v1) | 强mask损坏任务逻辑；§IV-B1–3把strict sanitization与structured reconstruction分流再融合，潜在utility/privacy payload取舍。重建模型仍接触原始X，“只提数学忽略标识”是prompt而非形式隔离；ASR0局部样本不证明zero leakage，也非DP。 |
| [SEMI-CTDE 04653](https://arxiv.org/abs/2512.04653v1) | 全局集中training扩维而完全去中心化缺协调；region内参数共享/复合state-reward与region间decentralized execution提供窄学习拓扑替代，跨policy骨干/ablation线索值得核。仅交通实证，不授大模型分布式训练或所有partial observability有效。 |
| [DSCP 05447](https://arxiv.org/abs/2512.05447v1) | 邻域耦合policy不能按独立reward梯度更新；neighbors-averaged Q与geometric two-horizon无完整Q表采样、push-sum局部参数估计是具体优化/通信机制。理论假设与stationary point性质待核，不把机器人演示等同LLM/RLHF收益。 |
| [HiveMind 06432](https://arxiv.org/html/2512.06432v1) | 全Shapley coalition执行昂贵；实际读DAG-Shapley两核心：无sink/source/path联盟设value0，按层相同输入在functional determinism下memoize，之后贡献指导prompt优化。7agent128→49联盟只是该图条件，随机LLM/旁路信息/无效联盟非零时exactness未获保证；GLM4Flash temp0不自动消除所有非确定性，不采用80%为泛化节省或金融效果。 |
| [BSFA 07011](https://arxiv.org/html/2512.07011v1) | 全QK后选择value work的稀疏执行分支，具体机制/反证/owner见上；不把exact QK授exact Attention。 |
| [AgentODRL 00602](https://arxiv.org/html/2512.00602v1) | 固定worker路线与orchestrator不能只按任务总分评价；workflow/Table2中orchestrator semantic80.22低于固定Splitter84.02/Rewriter88.07，但tokens46.2M低于47.9M/49.5M，新增窄route质量/成本取舍。撤回“只有770任务分”关闭；SHACL syntax非authorization，LLM Jury非真实semantic intent。 |
| [劳动市场 04988](https://arxiv.org/html/2512.04988v1) | 模拟reward不自动反映LLM能力增益；Appendix I及共同实验条件中LLama平均低于fixed-policy baseline，是窄模型能力/reward评价负侧。环境skill training不是模型权重更新，但不能据此抹去反证；不授同token预算、相关为因果或现实经济结论。 |
| [碰撞分析 06645](https://arxiv.org/html/2512.06645v1) | 减少交通需求/禁止左转不必改善学习controller安全；IV-b/c及V中部分60/80%RV配置降需求反增碰撞，4S+10U禁左转总体反增。保留MARL干预边界反证，不因交通领域关闭；14intersection/single-direction模拟不授现实通用安全。 |

新增三项只按[Mill实际精确v1必要局部阅读](./ROOT_ADMISSION_REVIEW.md#负侧分层与精确普通差额)重开：位置分别workflow/Table2、Appendix I及共同实验条件、IV-b/c与V；作者撤回原关闭并同步集合，未重复全源，未声称本轮新增全文或复现实验。三项first-public仍未授，不进入确定落窗分母、评分或Books采用。

这些家族精确v1的Submitted字段只核版本身份；00614 Nov29、00740 Nov30、01363 Dec1、02410/03248 Dec2、03466/03694/04320 Dec3、04653 Dec4、05447 Dec5、06432 Dec6、07011 Dec7均不授公开日。有些正文后续v2已存在，只取上述v1；不声称本窗修订已审。HiveMind/04320具名announced官方域查询未返回个体公告，AutoGLM替代只恢复Dec8日粒度；当前可用历史day list/API等已验证限制，停止日期同端点循环。

### 贡献前关闭及未来下界

OS完整题摘后关闭5项：00400 TenonOS的LibOS-on-LibOS组合只在一般embedded/time-critical运行时，不建立模型形成/执行的直接约束；03279 MOST hot-data mirroring/tiering与CacheLib是通用存储机制，题摘未有模型状态/训练推理直接关系；06331 importance与priority/criticality分离针对interrupt storm经典实时系统，未建立当前模型/物理模型controller的实际交接；01594 CAEC Arm CVM共享机密内存与通用通信没有直接模型/AI平台工作负载边界，不能由“confidential”主题映射自动准入；05555 LLVM/TSan redundant instrumentation与dominance分析针对普通并发程序，未建立模型计算compiler/runtime具体变化，当前主线关系不足。不是否定这些系统机制，也未给它们性能保证。

MA完整题摘/含糊处必要核心后关闭9项（含下段05983）：00520实际架构/guardrail段主要重述已引文的planning snowball、guardian injection等风险，未新增受控反证或独立协议；01610实际§4.2/4.3、5.1/5.3为插件/annotation白名单/Controller mediator、Ray PodManager集中broker与按人数分配，population可变是框架适配，未给新的消息一致性/生命周期或权限failure机制；02682实际§3/4.2明确ESRH是概念指标、Institutional角色 deliberately abstract，验证future，未有新可检验稳定边界，不能把system safety词汇当机制；03180实际§3.4/4.1–4.2是policy-as-code、semantic telemetry、50–100未来scenario bank和red-team计划，未有新enforcement/已观测反证；03285明言研究agenda不是完整framework，只有既有gossip用于context传播的方向，未定义新语义filter/行动一致性协议。04771 epsilon-machine与diffusion互补用于ABM elder-caregiver输出分析，不改变生成模型本身目标/执行；02227把传统trading组件映为agents并给两组金融回测、02561检索/角色/keyword/controller教育组合及LLM自评，未新增当前模型主线机制或受控反例。00602/04988/06645已因上述具体方法/反证撤回原关闭，不留在该集合；不因原理由有主题关联就推倒其他有效关闭。

05983另处理原站admin substantial text overlap信号：实际读[2506.06837v1](https://arxiv.org/abs/2506.06837v1)完整题摘，作者和semantic metric compromise核心相同，Submitted Jun7只证明旧身份；当前TARK条目新增标题后缀不自动证明重要机制变化，不宣称整篇修订已审。其共同核心用embedding/LLM生成文本折中点服务人类共同文档表决，未建立本项目模型训练或LLM-agent执行的新约束，贡献前关闭；admin overlap不是withdrawal/网络失败。

OS另9项精确v1提交明确晚于本窗：12530/12615 Dec14、13047 Dec15、14946 Dec16、15028 Dec17、16238 Dec18、18436 Dec20、24637/25065 Dec31。首次arXiv公开不能早于其提交，不授真实first-public或否认作者更早原始发布，留窗外身份不深审。部分早期提取条件误把11/15/16/31中的末位日期视作1/5/6/1而输出额外摘要，最终按完整版本日期纠正，仅以上述真实下界判断，未用于当日候选。OS明确经典VM/实时/IoT/系统日志应用题名、MA科学代码应用/经典MIS与ANAC谈判题名不扩池；没有清空全211项库存。

## 作者停点与恢复

作者按Mill三项精确差额重开归并与正式同步已做，普通可执行项0，交Mill局部核验；0个确定完全落窗家族，15个arXiv潜在家族及GLM-4.6V/AutoGLM共17个具名保留项，另15项贡献前关闭（5OS、9MA、1OpenAI）。这些数不是当天新论文数或Evidence完成数。作者不自授通过、不覆盖metadata/§6；必要外部项仍按下述边界隔离。

必要个体first-public、GLM/AutoGLM当时artifact与Qwen/Hunyuan/Z.ai/MiMo历史目录均为本窗终态保留项：不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证；隔离不计Coverage/Evidence通过，也不是零事件。日期恢复只复用官方历史list/catchup400、API429、announced月精度/OAI提交字段的原始接口限制，不反复请求同一端点。官方2025假日依据只按[日期恢复](../ARXIV_DATE_RECOVERY.md)的真实排期权限，不给个体提交默认归日。

每家族仅请求一次：arXiv需对应精确v1官方历史new公告/RSS/email或可核首次正文区间；Z.ai需2025原始上线时刻或完全落窗区间及当时card/adapter/confirmation协议；历史目录需2025原始邻接段。恢复只重开该家族真实归属日及必要命题，窗口外未来下界不阻塞本窗，不全月扩扫。Books暂缓这些材料；BSFA条件草案已给精确owner与原始核心，不冒称书稿落实。
