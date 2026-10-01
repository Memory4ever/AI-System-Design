# 2026-04-10 V3 题摘准入与证据记录

## 当前有效状态（后文旧过程状态不作为验收）

README已同步70项唯一当窗工作候选：34实际Books整合、17具体已有覆盖、15仅报告、4争议；70表行与70证据小节一致。07831/07962/08118、QaRL07853及最后DACS07911/ATLAS08044的必要官方原文、实际正文及相邻衔接已获root非作者PASS。最终身份对账已结束，作者侧普通准入/证据/Books待办=0；等待日级非作者Gate后冻结，不让587原始身份变为深审队列。

### 最后旧身份对账与最小消歧

原旧retain中14个身份需要对账，完整摘要已逐项读，不继承旧tag。

- 07681：HPC科学工作流/MCP-Parsl与MOF筛选应用；AI for Science暂不在本阶段，题摘的planner/executor/tool组合未提供独立runtime机制或通用设计反证，前分母关闭。不是按无法映射ROADMAP关闭。
- 08224：externalization综述将weights/context/skills/harness串联，题摘未提出独立可验证的新机制、反证或可改变既有设计判断的条件，前分母关闭。
- 07551：此前§4.6–4.8六责任层catalog与static/runtime/isolation/decision分类已具体关闭，本轮不丢失也不重复深读。
- 07833：必要读§6/7.1/7.6/8.2，manifest/admission→watcher→recovery为成熟外置治理组合；Gazebo UR5e mobile-base人工违规/检测概率受profile sensitivity设定，不是实机安全率或新的低层控制保证。Ch26 Simplex/低层控制共存及Ch72sensor/authority、effect-time边界已承载；这一受限组合实现未改变具体设计选择，前分母关闭，保留来源而不采用量化headline。
- 07911 DACS：必要读§3.1–3.2、§6、§7.3–7.4。registry-only与Focused(ai)工作视图切换改变orchestrator本次steering可读内容，不同于仅选择层级拓扑；他人紧凑status不等权限隔离。正常串行/urgent保存partial抢占、resume，interrupt收益未独立消融；真实Agent仅Haiku4.5/N3或5/低决策密度，agent-ID引用不等有害污染。2+2+2=6、知识缺口深入，拟Ch82窄正文，等待实际落实和写后复核。
- 08044 ATLAS：必要读§3.1–3.4/§4.2–4.3/§5。不能概括为未经校准的纯模拟：§3.4作者报告3D testchip/TDTR材料与模型对照，设计空间结论仍依赖HotSpot/Ramulator2/BookSim2及固定inter-device bandwidth模型。channel granularity的row-locality/parallelism反向与channel/MC面积/thermal-power挤占compute是具体条件分支，cloud/edge optimum不同。2+2+2=6、知识缺口深入，拟Ch54 capacity-knee段后的联动约束，不采通用16channel最优、生产可部署或全面仿真准确性保证。
- 08075 DualPool：§2 EMA bytes-per-token+max-output/容量过滤/load spillover，§3 Eq6含两次ceil而Eq7去ceil，λ=.5、μH=1、μS=2、α=.5给Ghom=1/Gdual=2，真实saving=-1但Eq7=.25。反驳always-help与conservative lower-bound的无条件断言，不否定连续大规模近似和所有实验。§4仅Vidur校准模拟，shortpool同时改变context、Nseq、batch-token设置。2+2+2=6、中心设计反证深入，争议暂缓，不入Books；重开需保留离散fleet/利用率条件的成本式及独立配置对照。
- 08178 Plan-RewardBench：§3.1–3.4固定task/toolenv/history比较轨迹，natural/perturbed/rule negatives与judge-panel/meta-review；worst unsafe episode决定rubric label而非按长benign prefix投票，§4–5包含盲重试、未更新约束、末端违规被平均印象盖住。6分标准已有覆盖：Ch66 deterministic-first/fulltrace/rubric/scorer分权与Ch72 Containment传播/授权/effect阶段已有具体边界。LLM偏好标签仍非外部任务真值，English text-only、非均衡安全切片及待公开artifact不能证明通用RM可靠性。

上述early自身v1 Updated原始字段（UTC 2026-04-10）：07833=00:29:06、07911=00:34:00、08044=00:42:56、08075=00:45:27、08178=00:50:20。只与永久ID公告赋号、常规slot和已核连续批界共同支持明示08～09推断，不将字段单独当发布时间。

### 日期逐家族隔离（不按整批否定）

七个旧retain已读完整摘要，以下自身Updated字段跨截点，不能继承早批的推断上界；也不能把Updated晚直接等同公开晚。需逐家族更早官方artifact/目录公开链后重开，不先评分或改Books：

| 身份 | 原始v1 Updated（2026-04-10 UTC） | 保留贡献线索与范围 |
| --- | --- | --- |
| 08369 TrACE | 01:01:47 | inter-rollout action agreement与自适应控制器，agreement不是verifier；未确认首公开窗。 |
| 08377 SkillClaw | 01:02:14 | collective cross-user trajectory/skill更新；需核shared-skill写入权与跨用户证据，而非默认可信。 |
| 08401 SAVeR | 01:04:05 | precommit belief self-audit与persona选择；自审不获得事实验证权。 |
| 08426 KV offloading | 01:05:33 | context-intensive Text2JSON下近似低秩/landmark可能不如简单offload，负面贡献信号保留。 |
| 08451 MIG partitioning | 01:06:31 | 静态partition仍受共享功率/thermal与NVLink C2C影响，资源隔离反证线索保留。 |
| 08455 KnowUBench | 01:06:40 | 隐藏偏好、澄清/同意、拒绝后约束可能改变evaluation contract。 |
| 08545 Metis-HDPO | 01:10:39 | 正确轨迹条件下的效率偏好与单scalar reward不同，需确认owner与训练边界。 |

原始字段可复查`../arxiv-owner-replay-20260903/datacite-created/2026-04-10-page-01.json`及`page-02.json`；它们不是单独的公开证明。旧09731/16469与Nexus09258、Google ConvApparel独立事件仍按日报精确日期缺口隔离，不拉本日scope去补全年。

### 最新12项与QaRL的证据终态

07712/07747/07754/07791/07914/08046标准或安全必要审阅后为受限仅报告；07769/07776/07835具体Existing覆盖在README §4；07831/07962/08118实际写入Ch72/72/49并获root source+write-after PASS。QaRL07853在Ch33 FP8/master之后已实际写一段，仅算术/artifact identity增量；root必要源及写后PASS，TBPO ratio/log-clip张力不作信任域保证。其余53项已通过的单篇证据不重读。DACS/ATLAS最后两处正文已实际写入Ch82/54并获root PASS，完整题摘与PDFv1必要机制交叉核过；08075中心离散成本反例独立成立，08178已有覆盖论点定位完成。70身份作者对账结束，日级非作者Gate仍待root，不预称整日报完成。

作者 apr03；检查于2026-09-26。窗口为北京时间04/09 09:00～04/10 09:00。587仅是旧原始身份库存，不是候选分母；旧 ledger 的关闭理由和高分不继承。完整题摘来自[原始库存](../arxiv-owner-replay-20260903/20260410/arxiv-owner-receipt.json)，拟采用命题须再核官方 exact-v1。以下是分批工作判断，日期、必要证据与独立校准完成前不冻结候选。评分是提议的三维组件，不用分数倒推准入。

## 首批具体增量（尚待单篇 Gate）

| 身份 | 原约束 → 原材料增量 → 待核设计判断 |
| --- | --- |
| 07874 Valve | operator/iteration boundary 才能恢复，长 Prefill 突发响应慢；channel pause→quarantine→失效 IDs→框架重算打通 compute/memory 移交，无 fault 与内容有效不等价；2+2+2=6，长期缺口深入完成。官方 PDF §4–5 与 Ch56 实际正文已过 root 写后复核；整合。 |
| 07815 AsyncTLS | 每步同步粗细选择把搬运留在关键路径；上一轮 block candidates 供当前 fine selection、当前 coarse 预取下一步，改变候选消费时点；2+2+2=6，长期缺口深入完成。官方 PDF §4–5 与 Ch22 实际正文已过 root 写后复核；整合。 |
| 07853 QaRL | fake-quant/master 对齐不代表真正低 bit forward 算术一致；materialized 权重直接发布可改变训练/服务数值身份。2+2+2=6，已读 §3–4；仅拟采用算术/发布分支。长度归一 surrogate 与 ratio/log clipping 张力不写正面保证；Ch33 root 协调。 |

## 前缀题摘工作判断

以下37项完整标题和摘要已实际读完；不是仅关键词筛选，也不是全文已审。清楚潜在贡献的进入必要证据审阅；准入事实本身含糊的只读对应方法，不默认扩入分母。贡献关闭不冒充日期已核。

| 身份 | 初筛判断与具体依据 |
| --- | --- |
| 07363 Benchmark Shadows | 定点确认：受控 benchmark-aligned 与 coverage-expanded 数据可能改变结构 rank 与测量对象；需最窄实验确认不是仅验证已知 benchmark leakage，未先保留。 |
| 07380 Lifecycle Spectral Edge | 拟保留5：weight decay 的表示压缩可逆而算法行为保留，flatness 与 axis perturbation/可读信息分开；可能修正“压缩就是遗忘/低曲率就是无作用”的优化解释，必要实验待核。 |
| 07386 Label Leakage | 拟保留6+安全深入：遗忘目标类别可通过原模型/aux model 差异或反演推断，需核删除内容与删除操作信息泄漏是不同保护对象，而非只报告一般 MIA。 |
| 07392 Event Retrieve Action | 关闭：UAV事件检索再给 manoeuvre 权重，是既有非参数经验复用的任务适配；题摘未分離新的可恢复状态、控制可行性或组件收益条件。 |
| 07398 Identity Illusion | 关闭：七条提示降低拟人化文本比例和输出长度；未测答案质量、用户信任或真实自主行为，只能证明表述风格干预，不能支撑模型行为可靠性设计。 |
| 07402 LocalOpt/ReCoAR | 拟保留6：局部窗口减少训练成本但改变滚动误差，representation-continuity regularization 针对这一接口；需核何时局部训练保住 rollout 一致性及其代价。 |
| 07403 RefineRAG | 定点安全核：macro/micro毒化+反馈优化是已知检索攻击路线；需查是否揭露词/文档 admission 中独立的新失效路径，再判准入，非因安全关键词自动留。 |
| 07404 Score Shocks | 拟保留5：VE score 的热方程/Burgers对应与双模混合边界的误差放大可能给出具体 score/solver 适用边界；只核证明前提，不因一般 PDE 推到所有生成模型。 |
| 07405 Conservation Breaking | 拟保留5：bias-free ReLU 梯度流的不平衡守恒与离散步长二阶漂移分开，可能改变用连续理论解释深网更新的有效条件；必要推导待核。 |
| 07415 SubSearch | 定点准入：摘要只说 intrinsic process reward，未显示它新增什么可检查机制；仅读 reward 定义/对照后决定，不默认深读。 |
| 07422 MUSIC | 关闭：合成数据、视觉 CoT 与布局组合提升 multi-subject ICL；题摘未隔离新 identity/control 保证或旧方案失效条件，不因 subject 数量增多保留。 |
| 07426 GIRL | 拟保留5：frozen visual grounding 与 latent uncertainty 控制 trust region，可能改变 imagination 步的可提交范围；只核实际信号、界和任务条件。 |
| 07428 RAPO | 关闭：graph diffusion 的延迟伤害/环境 scar 不是基础模型、模型 Infra 或 learned world model 主线；不能以长期 reward 或 state类比取代项目关系。 |
| 07430 HY-Embodied0.5 | 定点准入/身份去重：MoT/latent tokens/self-evolution 不能凭模型发布自动留；需核 actual representation/action 接口是否有独立增量及是否早期官方事件已审。 |
| 07466 Byte-Level CTD | 拟保留6：teacher vocab distribution→byte probability/student auxiliary head可改变跨tokenizer蒸馏接口，不只是模型指标；需核位置/对齐和混合任务边界。 |
| 07467 Lexical Tone | 拟保留5：SSL latent 可编码声调而量化单位损失它，多个quantizer与residual分支提供表示压缩≠任务信息保留反证；限普通音段/超音段条件，不外推所有音频。 |
| 07484 ConsistRM | 定点准入：temporal answer pseudo-label 与 critique consistency 可能改变 self-training target 稳定性；需确认时间一致性奖励不是一般投票/自洽的重述，不以1.5%指标留。 |
| 07487 CLEAR | 拟保留6：经验检索→对比轨迹反思的SFT scaffold→执行Agent reward训练Context生成器，改变context构造目标与参数owner；需核上下游reward耦合/新任务迁移代价。 |
| 07506 ReflectRM | 关闭：统一response/analysis preference加reflection选择可靠分析，题摘仍以自评解析优化judge；未给新的独立truth或反偏有效性条件，+3.7/+10.2本身不把成熟process/outcome组合变知识增量。 |
| 07518 DLR | 拟保留6：按文本premise动态提取连续视觉latents，再用球面Gaussian policy探索；改变visual evidence→reasoning载体与训练探索接口，需核三阶段训练与真实grounding。 |
| 07523 FILCO | 定点准入：统一/多个独立 accelerator 的runtime granularity可能改变隔离/映射选择，但“可重构更快”本身不足；只读实际compose/state控制点。 |
| 07526 RL ASIC | 定点准入：joint architecture/memory/operator placement本来是成熟联合搜索；只核是否新增可复用可行性约束/设计反证，模拟PPA工作点不自动入选。 |
| 07536 TRUSTDESC | 拟保留6+安全深入：trusted tool description从实现slice→生成→动态任务验证，针对隐式虚假能力描述，而非仅检测恶意文字；需核工具可执行行为与description claim的绑定边界。 |
| 07559 DCVerse | 关闭：数据中心冷却DRL与digital twin/pre-eval/expert组合，研究控制领域应用而非基础模型训练/服务机制；冷却节能不直接证明 AI Infra调度增量。 |
| 07569 Learning Is Forgetting | 定点准入：IB与模型压缩新证据是否真实测到objective-conditioned信息选择，还是对既有压缩观点作不可识别估计；不默认采用“optimally compressed”定理。 |
| 07583 CAMO | 关闭：少数类boost/校准/ensemble在两个领域分类数据提升macroF1，题摘未给改变LLM evaluation独立性或有效性的机制/反证；“domain-neutral”是作者外推，不作准入依据。 |
| 07590 DCD | 关闭：层级domain/document routing+chunk/hybridretrieval/guardrail是成熟RAG组合；synthetic应用改善未拆出新admission/evidence有效条件。 |
| 07592 FESTS | 拟保留5：空间时序逻辑编译成可匹配video log并生成有解释的监督，改变data truth owner/表示grounding接口；需核结构化日志前提与解释是否仅训练标签，不以F1量级留。 |
| 07593 Too Long | 关闭：expert数学数据中prompt/solution长度与失败相关，难度调节后弱相关；没有分离length因果或新测量修正，不能新增“越长越难”的普遍解释。 |
| 07603 Implicit Regularization | 关闭：MNIST/CIFAR按多seed重复batch/flatness/NTK/double-descent/lotteryticket成熟现象，没有新的机制/界或重要既有判断反证；不因小模型排除，而因本次只是复现组合。 |
| 07634 VSAS | 拟保留6：同步/异步在线视觉指标把timeliness与temporal consistency从offlineQA分离，buffer/resolution对照可能改变streaming验收合同；需核clock与output timing。 |
| 07645 PRIME | 定点后关闭：§3.2/4.1/4.2 的三类经验、LLM整理/四种编辑算子、冻结模型检索是已有外部Memory路线。新增成本主张缺探索/整理GPT-4o/API和部署token成本的匹配合同，GRPO绝对表现更高、4B←8B只同Qwen家族；未改变现有外部经验可逆/参数更新成本选择，不按‘无新authority’机械拒绝。 |
| 07650 Entangled Judges | 拟保留6：easy-task共错权重和方向信息gain测出跨模型关联，并在disjointbenchmark关联judge over-endorsement；需核dependence测量/重权方案，不能用family不同当独立证据。 |
| 07655 Guardian Advisor | 拟保留6+安全深入：hardgate→risk+explanation advisory重推保留base spec，改变阻断权/风险提示关系；需核overrefusal与safety能否分开，非单向安全更强。 |
| 07658 PoST | 保留2+1+2=5，理论争议深入：有限decay channels的有序重参数化与position stretch为具体分支，但exact PDF v1的Prop4.5可构造反例，p定义/Algorithm1也不一致；不采用minimax/零开销保证，拟暂缓Books直至勘误。 |
| 07663 SAGE | 拟保留6：embedding稀疏高方差令轻状态hybrid退回Adam，bounded adaptive scale替代其状态路径；需核scale bound对方向/收敛实际能保证什么。 |
| 07666 Noisy Verifier | 拟保留6+反证深入：可控制噪声与model-noise下RL对moderate error有有限鲁棒性，可能修正“必须perfect verifier才可训练”；需核highprecision与accuracy/selection差异，AI-for-Science任务不作为项目贡献主体。 |

以上评分/处置不是最终日报表；仅真实保留项继续必要原文，定点准入完成即停止该项扩读。独立误收/漏收校准尚未完成，37项不能称已全量通过。

## 首批准入独立校准与必要证据

root 实际读四项正向及四项负向题摘后，确认 07466/07467/07658/07666 有可核具体机制或反证，不等于证据成立；07603/07559 关闭成立，07593 的关联不构成新增设计边界，但不以缺因果为统一准入门槛。07645 按上行补查成本与任务对照后具体关闭。该八样本不外推587原始身份。

- [07466 官方 PDF v1](https://arxiv.org/pdf/2604.07466v1)：§3.1–3.2/4/5 与 Table1–3 支持 teacher byte 概率近似、student 训练期辅助 head、token CE 与卸载接口；实际是10个并行byte heads、超过10bytes只监督前10，非内部byte AR。IFEval显著退化、BPE→byte整体能力下降和任务排序反转使“统一byte坐标”不等于无损能力转移。Ch29现有概率投影路线尚缺辅助训练接口分支，已交root定点对读，未预称整合。
- [07467 官方 HTML v1](https://arxiv.org/html/2604.07467v1)：§2–4 固定HuBERT/数据，对latent与quantizer中心向量做vowel phone/tone probe。量化后tone可丢失，RVQ/residual和mean pooling并非自动修复；词汇tone不可默认归为不重要声学细节。限Mandarin AISHELL/Yoruba单说话人语料、MFA对齐、非sandhi和非端到端生成；码数相近不证明等bitrate。PDF本次入口失败，未冒称已读PDF；HTML必要段可用，拟Ch23窄反例交root复核。
- [07666 官方 HTML v1](https://arxiv.org/html/2604.07666v1)：§3–5/6.3与Limitations分离受控对称重采样噪声和模型verifier误差；MBPP三tests的pass-rate不是完整程序正确性，best与final不能混写。p≤.15的局部鲁棒性主要为整组rollout噪声，Table1同p不同结构并不完全相同；4B/30B模型verifier高recall但precision不同，没有独立FPR/FNR因子实验，不能推出普遍优先precision阈值。Ch33已有相关/trigger误差路线，正在判断窄幅增量或真实已有覆盖。
- [07658 官方 PDF v1](https://arxiv.org/pdf/2604.07658v1)：已定点对读§2.2、§4.2–4.4、§5与§6/limitations，不扩完整附录。PDF第12页Prop4.5沿用HTML错误：取θ=1、softplus(c)=1、δ均为c，则p=(1,2,3)满足声明域，但μ23=2√6/5≈.9798大于其全局上界μ12=2√2/3≈.9428；“最坏相邻pair是1/2”的步骤方向错误。§2.2定义p=-logw，§4.4累计正gap为算术p，而Algorithm1再取d=-exp(p)，不能将两种p坐标混作已证明的几何谱。§4.3位置stretch只有指定谱/边界/信息分配条件，离散滚动积与局部固定gate近似还依赖s≪t。§5.2实际增加O(LN)操作、不等零walltime；Table2 GLA64K、Table4 RWKV平均有退步，180/440M、4–9Btokens与NIAH不能证明任意recurrence/规模无损。保留5分、争议深入终态建议：暂缓，不将中心理论保证或未分离的实现经验写入Books；可接受的重开材料为作者统一p坐标、修正coherence界并明确理论与实际算子的连接/评价。Ch22已有衰减状态与长度分账，当前不以这篇争议自动新增正面保证。

07466/07467两处正文已经按root授权实际写入Ch29/Ch23，正文位于Review notes前；root必要原文/实际正文非作者对读已通过，日报已同步整合终态。原“尚等复核”仅为先前checkpoint，不代表当前状态。

07666：root实际写入Ch33相关误差段，apr03独立对读exact-v1 §3–5/6.3、Table1/Limitations与实际正文，随机重采样/固定偏差、group结构、best/final、precision混杂界限成立。MBPP三tests只是测试合同，不保证完整程序语义；已建议root把“真实task outcome”按此收窄。五项单篇整合不替代整日Gate。

日期补核：07466自身v1Updated=2026-04-10T00:03:14Z，07467=00:03:18Z，07658=00:14:57Z；结合PID公告赋号、常规slot及连续相邻批界支持明示推断的北京时间08:00～09:00范围，不将这些字段直接改名公开时间。PoST争议终态已同步日报；不以submitted或DOI created独立定归属。

## 本轮有界来源与新增必要证据

- Qwen两官方API本次实取：`page_config?code=research.research-list`为60项array，最晚2025-12-23T05:08:30Z；`v2/article/retrieval?type=qwen_ai&language=en-US`的data.articles为40项，邻域04/02T04:00+08、04/15T10:00+08、04/18T10:00+08，无本窗目录项。实际目录拼接路径此前已核，本次字段与停点再次确认；完成这一来源，不外推未列作者稿。web工具接口读取失败，curl直接官方API恢复成功；不是用空响应证明无更新。
- 07380 exact HTML v1 §2–6/9/10.4：150K Dyck、1.5M SCAN、三seed、W5 attention-update SVD。Table1同post-grok checkpoint降WD恢复linear R²而task准确率变化较小；Ch5已有信息存在/读出/使用，Ch28现全局WD交互尚缺这一表示可读性schedule分支。已获root独占授权，实际写入Ch28该段后两段及Review notes，5分knowledge-gap深入。随机移除只同维数非范数匹配，小ε扰动不等整投影移除；不采alignment导致grokking、统一阶段梯度比例或frontier schedule。待root非作者写后，不预称终态。
- 07405 exact PDF v1第5页Theorem6 Eq7和proof：S=diag(p)-ppᵀ的最大特征值不等max p_k(1-p_k)。二分类p=(.9,.1)给S=.09[[1,-1],[-1,1]]，最大特征值.18>作者界.09；取单样本J=I即可反例GN bound。原文还将GN近似与一般Hessian混用，不能证明中心CE谱压缩/τ保证。保留无bias homogeneous ReLU相邻rescaling守恒与离散η²梯度不平衡恒等式的局部证据，不因这些正确事实绕过中心争议。拟2+1+2=5争议深入/暂缓，待root独立确认；自身v1Updated00:01:24Z支持同组合推断，不用submitted定归属。
- 07386 exact HTML v1 §III–VI：仅post-unlearning分类模型参数/输出即可检测删除类别，不证明原秘密样本恢复或LLM开放接口。LeNet/ResNet18、四个10类数据集，Eq12对全部classes计算ASR，忘1/3类时多数‘均未忘’基线为90%/70%，不是文中统一50%；单类BB约77%不能据此声称超越多数基线。辅助head参数法依赖同feature坐标、inversion依赖probability vectors与已知label space；理论白化相同Σ/类正交不推出一般深网。正在与Ch72具体删除/observer命题对读，只采用可支持最窄判断；5分安全深入，中心有效性和隐私目标需限定。
- Anthropic Trustworthy Agents官方核心已读：model/harness/tools/environment与plan/action oversight、多层prompt-injection防御是已有原则的产品实施叙述；没有新的可定位机制、设计边界或独立实验合同，文中链接旧framework不成为本日新论文。本身按贡献前分母关闭，保留2026-04-09T16:34Z官网publishedOn与实际正文，不宣称未披露安全保证；已交root作否定侧校准。

## 当前已落实的终态与来源恢复

07380的Ch28正文已由root独立写后通过；07405的官方Theorem6/Eq7二分类反例也由root独立确认。日报现阶段8项=6真实整合+2争议暂缓，仍非冻结分母，剩余普通工作继续。

Google实际恢复的停点：[DeepMind Blog page3](https://deepmind.google/blog/page/3/)（真正路径不是`?page=3`）七条April项目逐页日期分别04/30、27、23、22、15、14、02；没有04/09～10项目。[DeepMind Publications](https://deepmind.google/research/publications/)首屏04/22→03/22已跨窗，不再沿用失败结论。Google Research[April归档](https://research.google/blog/2026/04/)04/13→04/09 ConvApparel→04/08，ConvApparel所链[ACL正文身份](https://aclanthology.org/2026.eacl-long.244/)标March2026，不能把4月博客当新论文首公开；博客独立新事件仅日级日期尚不能确认09:00截点。Google Research Publications年度列表可读，但没有恢复本窗日期索引，精确保留其历史目录限制。

Meta[Blog首页](https://ai.meta.com/blog/)与[page2](https://ai.meta.com/blog/?page=2)恢复：首页Apr08两项及Apr06，page2最新Mar27，未见本窗项目。首页featured顺序并非纯倒序，实际检查两页的日期而不是拿首项当停点；Research仍空正文、Publications点击工具失败，只隔离研究目录，不称全源零更新。

07386对读Ch72『Privacy Boundary必须覆盖全部Observable Channels』和secret-substrate/observer正文：现有方法要求指定被保护信息与可见通道，但没有与‘忘记哪个类别’完全同义的实证。该论文可作为删除意图与样本恢复不同的受限案例；然而全部10类ASR以50%为随机基线不适合忘1/3类任务，必须用90%/70%多数基线。root独立核Eq12、§VI与TableV–VIII后确认5分安全深入、仅报告终态，非假称完整已有覆盖或泛化LLM隐私；README已同步。

## 两项新增正文与来源收口（本轮恢复）

07402自身v1Updated=00:01:21Z、07487=00:04:15Z，与既有公告赋号/slot/连续批界支持明示推断08～09，不将Updated直接当公开秒数。Ch24的完整前向/局部loss梯度窗口与Ch75的独立context generator训练owner两处真实正文已由apr03按授权写入；root实际读exact-v1必要方法/评价/反证及正文后均通过，具体消息裁决已收到，README表和证据同步整合。07402不采邻state正则为完整Jacobian/全局Lipschitz保证；07487没有RL-only全因子且六轨迹与generator成本未匹配，executor冻结和授权边界保留。

Seed1657 Nexus：官方API PublishDate=1775750400000（04/09T16Z），ArticleID=1782982764131、UpdateTime=1782982793000均为07/02；唯一论文链接未版本2604.09258 PDF。官方abs/v1提交04/10T12:17:18Z，在截点之后；CMS后建记录不能证明其全文本窗已公开。具体日期保留，不评分、不把后出正文倒灌；重开需截点前正文artifact/官方历史发布链。论文目录页20/40和Blog type2页0/20有界停点已处理，不能称全源零更新。

OpenAI RSS实际当窗Axios公告=04/10T00Z：已读官方What Happened/Remediation，软件工作流依赖入侵、签名证书/撤销/轮换是成熟供应链处置，未新增LLM模型或Infra机制；root明确支持前分母关闭，不因security标签强制准入。Research/Index历史Load more仍无法到达，仅此研究目录精确受阻；RSS不是其替代。

## 必要证据小批次：07404 / 07518 / 07536 / 07592

本批最新裁决覆盖下方审阅时状态：07404 Ch24与07536 Ch78两处实际正文均由root原文/写后独立通过；07518核心密度争议经root独立核，暂缓Books；07426实现6分标准仅报告、中心保证精确隔离；07592五分标准仅报告。README已同步这五项，不表示分母冻结或整日报完成。

- 07536 TrustDesc：实际读官方HTMLv1 §4.1–4.3/§5–6及Ch78 ToolContract、相邻Ch77/79交接，root授权Ch78窄幅新增两段。源码里有某feature而dispatch未传参不可达，不能把整个库摘要成工具能力；真实entry/callsite slice→生成→任务执行/LLM judge声明修订是具体增量。LLM debloat非sound、库调用不展开、假定显式注入过滤、52tools/12servers/208合成任务以及adaptive15轮44.7–67.4%非零选择均保留；测试通过不保证远端诚实。2+2+2=6安全/知识缺口深入，正文实际落盘、共享锁释放，root写后待核，不提前整合终态。
- 07518 DLR：官方PDFv1第5页Eq6/10与HTML一致；高斯噪声后径向投影所诱导的球面密度必须积分径向r，不能直接采用固定半径z的Euclidean Gaussian ratio。二维σ=1、μold=(1,0)、μnew=(0,1)、z=(1,0)均满足域：真正ratio为I(0)/I(1)，I(a)=∫₀∞r exp(−r²/2+ar)dr；I(0)=1，I(1)=1+√(2π)e^(1/2)Φ(1)=4.4770518117，ratio=.2233612748，而Eq10=e^(−1)=.3678794412。此为作者sampling与密度识别的直接反例，不证明实际训练全部无效；需要sampler/density实现说明或明确surrogate勘误。题摘架构的premise→continuous visual evidence→rationale、两owner/placeholder反传可核，SigLIP frozen attention不是groundtruthoracle，Qwen3-VL8B四图像基准greedy pass1/后三项2048长度、非视频/embodied和缺等预算界限保留。拟6争议深入，policy密度/保证安全暂缓，受限实现与中心理论分开，待root独立核。
- 07404 ScoreShocks：已读exactHTML §4、§5.4、§6.1–6.3/§7.1/§11.2–11.3。s=∇logp的heat/Burgers对应、指定正smooth binary heat decomposition的tanh界面恒等式成立；对称两高斯在低噪声modeboundary局部扰动扩增可解析，不能把中心轨迹界推成所有样本或真实network。§11的solver调步/score诊断是建议，尚无trained模型速度/质量验证；尚需与Ch24必要局部正文对读决定最窄Books处置，不扩其全理论。
- 07592 FESTS：实际读HTMLv1 §3–6。∃绑定同一object跨帧，区别每帧各出现任意car；formal matcher对预标注perception log产生query/match/explanation监督不是原图perception真值。180scenes×126frames×7sensors，15人工querytemplates、27Koutputs、单Qwen2.5-3B，NL→SpRE自动翻译缺失。C1无解释SFT与C2新增PPO/解释reward混合，不分离解释因果或通用video能力；headline生成label无需crowd不消除输入humanlabels。拟2+1+2=5标准受限报告，尚待root裁决是否具体长期增量需进入正文；不因仅benchmark名称准入。

## 本轮必要证据与实际 Books 增量

- [FILCO 07523 PDF v1](https://arxiv.org/pdf/2604.07523v1)：§2.1–2.5/§3/§4.1–4.4，固定MM原子、FMU一维双缓冲视图与角色、CU块/存储循环partition、预连线控制，不是任意动态物理互连。Ch49执行计划章已按授权在recurrent路径后写两段及Review notes；FP32 VCK190/AIE与作者RSN解析比较保留边界，不采用全局最优或GPU/LLM serving保证。2+2+2=6知识缺口深入；写锁释放，待root独立写后审查。自身v1Updated=00:05:55Z，结合既有永久ID公告赋号/slot/连续批界仅支持明示推定的08～09范围。
- [SAGE 07663 PDF v1](https://arxiv.org/pdf/2604.07663v1)：Algorithm1/§3.1–3.4/§4.1–4.4/Table2/AppA2，保留完整embedding momentum，额外column统计仅O(d)，相对RMS阻尼不保证方向/最终质量。Ch28 optimizer-state主线已实际写两段及Review notes；dense UnitNorm配对混杂、0.6B Lion更好、Pure两方法失败、1D设置歧义均保留。2+2+2=6知识缺口深入；锁已释放，待root独立写后。自身v1Updated=00:15:33Z支持上述组合推断而非独立公开时间。
- [ASIC RL 07526 HTML v1](https://arxiv.org/html/2604.07526v1)：§3.3–3.10/§4.1/4.3/4.13/4.14/5.4，联合mesh/core/partition和分析PPA是可保留的受限设计探索；LLama8B FP16表9 batch3/seq2048与industry表20每用户1K不同合同、29809tok/s/51W为分析估算非实芯片，SAC与随机/grid单seed。2+2+1=5标准仅报告，root已认可，不以局部仿真点改变生产设计判断。v1Updated=00:06:18Z，仍按组合推定区间。
- [Learning Is Forgetting 07569 HTML v1](https://arxiv.org/html/2604.07569v1)：§2.2/§3 Eq2–6/§4/AppE8，角度归一/随机softpartition/层均值熵及n-gram backoff是固定C4/Tulu token上下文代理，非真实latent信息量。47模型六family六任务相关性不证明因果或信息瓶颈最优；footnote1 DPI饱和与实际IB frontier不能等同，停止/选择只是待验证提议。2+1+2=5标准仅报告，root已认可；Ch5压缩/记忆共存正文不是相同代理的新验证，故不假称已有覆盖。v1Updated=00:08:15Z按组合推定。

## 安全、在线视频与 Judge 依赖小批次

以下历史待核语句由本段的实际独立结果覆盖，不删除原审计过程：FILCO、修正后的SAGE（Table2胜者为全参数Lion）、VSAS、SubSearch、ConsistRM均已获root必要原文/实际正文写后PASS。它们已同步本日日报整合行，但不代替日级来源/分母Gate。SHIELD与Blink两处真实正文已按独占授权写入Ch54/56并释放锁，等待root写后核；没有将原始587条变为全文审阅队列。

## 生命周期、放置与证据合同小批次（2026-09-26续）

- 07394 Flux：官方HTMLv1 §3、§4.3/Table1、AppC.3，prefix/suffix条件router在prefill固定各层full/sparse路线，decode消费冻结路线与相应KV；路线变更不自动兼容旧KV。Ch22实际“Conditional Attention的route粒度”129–146行已解释这一机制、A80080GB/BF16/batch1及end-to-end prefill与kernel-only decode分账，故拟2+2+2=6标准已有覆盖。RULER切片低于dense，§3.2约束符号张力不作普遍优化保证。自身v1Updated00:01:09Z仅在公告赋号/slot/邻界组合下支持08～09推断。
- 07396 SHIELD：exactPDFv1 §II–IV/Alg1/TableII，QO/KV生命周期与BF16 sign/exponent/mantissa分银行，标准/放宽/无刷新不同保护策略。3T retention/DESTINY模型、H100seq2048 lifetime和随机mantissa故障注入是不同证据，不能证明实NPU整机35%节能；TableII有任务退步。Ch54生命周期表后已实际写入最窄分支，2+2+2=6知识缺口深入，待root写后。
- 07609 Blink：exactPDFv1 §4、§6.1–6.4、§7，host startup provisioning、DPU ARM HTTP/tokenization/RDMA、GPU persistent scheduler batching/KV/devicegraphloop；设备launch额度窗口续接保持状态。singleH10096GB/BlueField3/FP16/ShareGPTmean1019→463、1–32req/s，chunkedprefill/prefixcache/CPUoffloading禁用，多GPU仅未来工作。Ch56hostcapacity之后实际两段；2+3+2=7深入，待root写后，不与Ch49仅host-fed operator descriptor混同。
- 07472 Fast Heterogeneous Serving：HTMLv1 §3、§4.1–4.3的GH/AGH联合model/tier/TP/PP/route，M1/M3移除可失去feasibility；六querytype、六Llama1–70B、十GPUtier、FP16/INT8/INT4为模拟设置，latency/errors analytic而非生产测量。rolling在高波动有效、低波动不优，GH ordering重求不改变，AGH<10s与headline subsecond张力不采用。Ch56“先冻结可实现域，再排序候选计划”与“Admission也可以联合选择ModelQuantizationPlacement”实际正文承载feasible域/预测身份/在线反馈，不需重复；拟6标准已有覆盖。
- 07595 Reasoning Graphs（后元摘要名ROZA）：已核exactPDFv1 §3–5，item identity→历史evaluation→decision_ref→verified-correct结果过滤→used/rejected profile注入/检索图；§5明确没有实验结果。不能从较晚元摘要继承10.6pp/真实性或确定性提升，历史正确结果也不证明当前query的证据适配；coldstart/identity/shift/token成本明确。拟6标准仅报告，保留新控制分支假设而不假称已验证或同主题已有覆盖。
- 07622 DIVERSED：HTMLv1 §2–3/§4/AppC.1–2，ν=w(x)p+(1−w(x))q acceptance/residual采样保ν而非target p；训练小weighthead同时优化outcome与overlap。端点文字与Eq4相反不继承，质量/跨任务切片退步；八A10040GB、三个modelpair、draft3/5/7、输出128/384/512、temperature0/1，生产并发/SLO未披露。Ch48LosslessVerification后的RelaxedDecodingPolicy已把分布改变、质量shift与rollback列为不同contract；拟6标准已有覆盖，不把高acceptance宣称lossless。
- 07667 Conformal Social Choice：HTMLv1 §3.3–3.5/§4/§5.2–5.3，三模型四轮verbalprob线性池化，经每域每轮50/50groundtruth校准，singleton自动/多项/空集转review。交换性只保marginalsetcoverage，不保单例或singleton准确率；固定round覆盖亦不自动证明自适应stop-policy覆盖。MMLU-Pro八域、BedrockHaiku4.5/DeepSeekR1/Qwen3-32B，硬件/精度/SLO未披露。Ch66Conformalinterval/RiskCoverage与Ch82correlatedconsensus具体正文已承载，应记录受限案例不重复CP保证，拟6标准已有覆盖。
- 07551 MCP-DPT：完整题摘后定点§4.6–4.8核：六层责任×静态/runtime/isolation/decision分类及现有系统catalog；不是新攻击实验或防御效果独立测量。原文明确static不等runtime、isolation不识别intent，这些成熟边界不足新增本项目机制，前分母关闭；不按security关键词强制保留，也不把coveragecheckmark当安全保证。

- [RefineRAG 07403 PDF v1](https://arxiv.org/pdf/2604.07403v1)：§3–5/Table1/4/§6.2，外部语料攻击、冻结关键错误答案语义的MLM替词与proxy检索优化可把retrieval和target-answer分开；低语法错误/重复率不是已测防御绕过，PPL劣于blackbox基线。100 NQ+100 MSMARCO、五污染文档、Contriever/两7B victims/A10080GB及有限transfer，无生产防御充分性。2+2+2=6安全深入，拟已有覆盖：Ch72 provenance-bearing atomic claim boundary、poisoning exposure/reasoning/contradiction/non-answer分账，具体词级攻击不改该长期安全选择；root待独立裁决。
- [Guardian-as-an-Advisor 07655 PDF v1](https://arxiv.org/pdf/2604.07655v1)：§3.3–3.4/§4.2–4.4/AppE，label+explanation→原输入或prepend建议→generator不是强制安全gate。训练LLMjudge要求label/解释一致不提供外部安全真值；并行可能中断重推，低有害率均值代价不等任意SLO。PDF训练硬件为两节点各8GH200，latency图注原措辞另保留，不统一成额外精确设备数。2+2+2=6安全深入，拟已有覆盖：Ch72『Safety Assessment 与 Generation 可以分离，但 Authority 不变』实际已区分assessment、gateway、context注入和latency。AppE硬约束/小compliance假设不证明自然解码普遍不降安全；root待裁决。
- [VSAS 07634 HTML v1](https://arxiv.org/html/2604.07634v1)：§3.2.2 Algorithm1/§3.3/§4.1–4.3，独立camera producer与模型consumer/有界最新帧缓冲，空时点carry-forward上一回答；consistency升高可来自回答变慢而非更正确。H100/bf16按模型1/2/4卡、1FPS camera/600buffer/64context，API包含网络，模型与memory policy亦影响结果。2+2+2=6知识缺口深入提案Ch66现在线视频EvalSpec后补墙钟与staleness/consistency分账；不同于仅比较历史memory/recency。PDF入口当前错误，不冒称读过PDF；HTML关键段可读，root待非作者证据/实际写入决定。
- [Behavioral Entanglement 07650 PDF v1](https://arxiv.org/pdf/2604.07650v1)：§3 Eq1–12/§3.3/§4.1–4.4。模型群本身产生difficulty，M=2独立Bernoulli(.5)时d=.5强制互补，残差积=-.25；因此该经验difficulty下的独立null不由无共享来源自动成立。均值为零也不能独立保证有限样本精确sign-flip；需合适对称/渐近/交叉估计条件。两个disjoint1000 MMLU-Pro子集、18models/3judges重权是受限实现，可记录但不从行为依赖识别隐含谱系。2+2+2=6标准仅报告建议，独立性/检验保证单独隔离；非否定全部观察或启发式重权。标题与HTML匹配exact PDF v1，未进行完整版本历史比较；root待裁决。

## 最新终态同步（47项阶段表，非冻结分母）

此前过程中的待核语句由本段和README当前表覆盖，不删除原审计：SHIELD07396、Blink07609、TrajGuard07727、Symbiotic07753、GRASS07808、PolicyLong07809、DMax08302、Lego08123、Alloc08133的必要官方原文/真实正文写后均已获root独立PASS。24真实整合、11具体已有覆盖、9受限报告、3争议=47；尚须余潜在项贡献收口与日级非作者Gate。

新增表项自身v1Updated均早于01:00Z：07363=00:00:24、07394=00:01:09、07396=00:01:12、07403=00:01:22、07429=00:02:14、07430=00:02:16、07472=00:03:27、07595=00:09:39、07609=00:10:57、07622=00:12:03、07655=00:14:48、07667=00:15:42、07716=00:19:45、07727=00:20:58、07753=00:23:44、07775=00:25:53、07789=00:27:12、07808=00:28:19、07809=00:28:24、07988=00:39:44、08123=00:47:53、08133=00:48:09、08302=00:57:59。日期均为2026-04-10 UTC，自身元字段结合永久ID公告赋号/官方slot/连续批界仅支持明示推断08～09，不等字段直接证明公告动作。原始字段在上方链接的owner receipt中可核；late个体不继承这一范围。

07363准确身份是Benchmark Shadows，不是distributed HF系统；此前即时沟通的错误简称已纠正，未落入日报/Books。已再读exact-v1 §4–7：A–D主要谱proxy、外部model同时变data/optimizer，去重四类升而GeneralLLM降；选择6标准仅报告，不将coverage/rank proxy当普适泛化因果。其余新增具体证据/已有章节命题现在在README §4自包含，不用旧template代替。

## 日级否定侧定点复核与事实纠正

root 独立必要源核查维持三项前分母关闭，不是按范围窄或没有新 owner 关闭：07422 的 §3.1.2/3.2/3.3/4.3/4.4/D.3 为 8×8 category grid、SAM2/box 与 CLIP fallback、SEED-X plan→generation、CLIP best-N 及 nested removal CC/P/CoT；属于已有 layout conditioning/plan+best-N 的多主体适配，未分离新的设计边界。07506 的 §3.1–3.3/4.2 使用正确 prediction 派生 analysis preference，八条 rollout 的最低10% log-prob anchor 与 meta-judge winner vote；是过程/结果监督加自筛投票 recipe，没有独立 process truth 或新评价有效性证据。07833 的 §6.3/7.1–7.4/7.10–12 为 typed-request admission、runtime watcher、recovery/audit 成熟组合，概率 profile simulation 未验证真实机器人/人，没有新增可定位长期边界。已读位置与具体理由可复用，不扩大为全587条全文审阅。

07754 作者又直接核 exact-v1 Data Collection、Table2 与 Appendix D.1：MisQA 是13类共390条训练样本，而非39K；README §4已纠正并明确它与1900条测试题不同。其余方法/评价边界不变，不据此更改准入或 Books 处置。此同步不代替 root 最后日级独立 Gate。
