# May07 自然日增量补查

作者：root；本轮启动并重读当前 AGENTS/研究合同/Report合同/每日来源/统一Prompt/ROADMAP。窗口仅 **2026-05-06 ～ 2026-05-06（北京时间）**，不启动Live、Weekly、2025。旧160候选整行、日期评分、小时窗及原连续§4保留；[逐字基线](baseline-before-supplement-20261018.md) SHA256：`a660e3f0d2e3376f2ca354a88388435fbf93208aeb02a6418286be66570a7f2a`。当前补查进行中，不继承原完成声明。

## 1. 发现入口与实际范围

机构13源由[组A](SUP_ORG_A_20261018.md)/[组B](SUP_ORG_B_20261018.md)分别保留真实入口、分页/停止位、核心说明与限制，当前无确定新增机构候选。Meta日级历史目录、Google Research论文日级切片未恢复，不是零发布；Qwen/Kimi/Hunyuan/Zai/MiMo等已真实恢复，不沿用旧访问失败。

arXiv实际尝试官方 `https://arxiv.org/list/cs.CL/2605?show=2000`、cs.LG/cs.DC同路由，返回404；export API submittedDate限定May04～05及模型/GPU主题查询不可访问。四个官方域限定May06的KV/language-model/world-model/GPU查询未恢复新正文，搜索空不证明零论文。

随后只把本地 `../datacite-arxiv-202605-v2/doi-prefix-2605-*-page-01.json.gz` 当恢复线索：投影没有 registered/state/client 字段，最初按registered筛选得到空是schema不足，不是零命中。按v1 Updated=May06定位12个项目相关分类的432个唯一元数据身份；这**不是432篇已证May06公开论文或待全文队列**。与2026当前Report表按ID对照116个已出现身份、316个未出现，前者不自动等于全部同事件已审重复。root只浏览这316个标题用于有界主题查漏，实际选择下述48项读完整题摘；未选标题不冒称逐项语义关闭。题摘投影可能含后续版本，拟采用均回exact-v1；不以Updated/Created决定公告日。宽目录停止于这一具名集合，不扩大为全分类审计。

完整题摘实际读取48项：02904/02930/02950/02967/03096/03135/03222/03231/03255/03268/03276/03313/03359/03403/03438/03452/03465/03491/03517/03555/03561/03562/03566/03588/03598/03601/03652/03686/03722/03816/03820/03838/03846/03847/03866/03877/03884/03900/03927/03950/03983/03986/03989/04013/04019/04040/04044/04045（均2605前缀）。一次35项工具输出截断后，已将缺失14项分两小批实际补读，未把截断算已读。

## 2. 准入校准、具体关闭与撤回

独立[reader R1/R5](SUP_REVIEW_20261018.md)覆盖具名拟入选及代表关闭，不冒称316/432全量。SigLoMa原拟C已按visible-face/solid-angle weighted PCA的测度桥改P，Bifrost按竖向scale/显式reference接口保P；EDL按synthetic-only loss预训练数据依赖边界恢复准入，非evolution名称即贡献。03268的因果建模框架尚未连接模型能力形成或可操作学习/控制设计，按具体范围关闭，不因其retina/gene例子一律排除理论。

其余关闭理由（无评分；不为不影响处置的日期另追材料）：

- 02904 StateSMix：SSM+n-gram/arithmetic coding的受限文件压缩组合，未给出改变训练/历史状态选择的新边界；非因小模型关闭。02967 AutoRAGTuner：组件注册/图指针+Bayesian调参，胜default和代码改动量未给出检索可靠性或调参成立条件。03231 cotomiAct：lazy截图/diff/bestN/知识板组合，子集得分不分离机制。03555 MILE：frozen base/per-task LoRA/prototype路由的分割适配未给出新的隔离/路由可辨边界。四项R1实核。
- 03255 CoreBeliefs：对话压力稳定性benchmark与人类认知类比，没有新的内部机制或可控可靠性条件。03276 VEBench：编辑知识与选片定位QA新任务，未揭示独立可归因的多模态模型机制。
- 03465 FINER-SQL：GRPO叠加验证轨迹/SQL原子操作重叠的任务reward组合，题摘未给出新的credit或泛化有效条件。03491：自动驾驶BC/GAIL在PGD下的领域鲁棒比较，未抽离可改写本项目判断的新设计边界。
- 03561：GPU诊断/跨MPI拓扑可视化的GAMESS工作流，未建立模型训练/推理runtime新机制。03652 AniMatrix：anime标签编码/dual attention/curriculum/domainDPO组合，专业风格偏好得分不足以单独改写通用生成取舍。03686 NNGPT：LoRA代码分类预测哪个数据集更合适，未给新架构选择机制或泛化条件。
- 03816：Brier的calibration/resolution分解与AUC做2x2命名；reader定点core核到实证复用前文，没有新负面校准适用条件，保具体关闭。03838 TRACE：四层分责/指标映射/计算简约比框架，未给新的可执行协议或受验证保证。03847 MechanicalConscience：约束可行域最小修改与监督过滤表述，题摘未说明超出现有constrained-control的执行机制或有效条件。
- 03900：context-dependent多目标纲领与实现路线，未给可核验的新目标选择机制/边界。03927 StateVLM：bbox辅助监督与不改AR推理的任务训练组合，未分离新增状态推断保证。03950 UnAC：视觉focus/抽象/逐步自检prompt组合，benchmark改善不足以证明新检查可靠性。
- 03983 MPI Sessions：题摘明示EuroMPI2025先前正式发表线索，不是May06首次事件；不按2026arXiv登记重计，不由此宣称旧事件已全文审。03986：planner/agent推荐/两阶段检索/critique模块组合，recall未建立新执行可靠性。03989：经验路由skill包装既有Adaptive-RAG，固定pool nDCG不提供新证据语义。
- 04019：红队攻击/transform/scorer工具目录和编排，案例宣传未披露新security contract/可比可靠性边界。04040：离散draft+自批评→diffusion条件的组合，题摘未分离新generation/verification因果条件。04044：共享Transformer与modality backbones统一2D/3D对应任务，未给新的坐标身份或对齐条件。04045：AVI综述归纳token/fusion/generation/训练路线，未新增反证或可归因设计条件。

**2605.03562 HeadQ** 当前官方abstract明确伦理原因withdrawn，reader已实际核v3/作者说明；仅此必要原始排除，不入选、不评分、不进入Books，不保留selected。未重读撤回正文。

## 3. 新增日期原件（非Created推断）

root真实GET `https://api.datacite.org/dois/10.48550/arxiv.<ID>` 的14条完整单DOI响应，核record_id=doi、client=`arxiv.content`、publisher=arXiv、state=findable及唯一Submitted/v1，调用现有publication_date_envelope。13项最早界均May06 00:00Z，registered晚界也同BJT日，组合限定arXiv公告May06，不证明全球首次公开或正文历史。日期规则适用性复用当前合同官方2025版依据，不重复追时刻。

| ID | Submitted v1 UTC | registered UTC原字段 | 结果 |
| --- | --- | --- | --- |
| 2605.02930 | 2026-04-27T18:07:58Z | 2026-05-06T01:42:15.000Z | earliestApr29，跨日未决 |
| 2605.03135 | 2026-05-04T20:19:21Z | 2026-05-06T01:47:12.000Z | May06 bounded |
| 2605.03268 | 2026-05-05T01:40:14Z | 2026-05-06T01:50:25.000Z | May06 bounded；但贡献关闭 |
| 2605.03313 | 2026-05-05T02:57:46Z | 2026-05-06T01:51:30.000Z | May06 bounded |
| 2605.03359 | 2026-05-05T04:37:00Z | 2026-05-06T01:52:36.000Z | May06 bounded |
| 2605.03438 | 2026-05-05T07:19:06Z | 2026-05-06T01:54:29.000Z | May06 bounded |
| 2605.03566 | 2026-05-05T09:40:01Z | 2026-05-06T01:57:37.000Z | May06 bounded |
| 2605.03588 | 2026-05-05T10:03:12Z | 2026-05-06T01:58:09.000Z | May06 bounded；当前section4纠错须处理 |
| 2605.03598 | 2026-05-05T10:18:53Z | 2026-05-06T01:58:24.000Z | May06 bounded |
| 2605.03601 | 2026-05-05T10:25:28Z | 2026-05-06T01:58:28.000Z | May06 bounded |
| 2605.03820 | 2026-05-05T14:48:52Z | 2026-05-06T02:03:50.000Z | May06 bounded |
| 2605.03866 | 2026-05-05T15:27:27Z | 2026-05-06T02:04:58.000Z | May06 bounded |
| 2605.03877 | 2026-05-05T15:37:50Z | 2026-05-06T02:05:14.000Z | May06 bounded |
| 2605.04013 | 2026-05-05T17:36:29Z | 2026-05-06T02:08:31.000Z | May06 bounded |

reader R1另7项有效May06组合及KAHM02950跨日，原字段/原URL见其唯一记录。KAHM与02930保潜在贡献而不计确定当窗分母；直接官方列表路由共同失败后保具名日期恢复，不无限追假想发布渠道。03722随后已由B§8.1实取同DOI/arxiv.content/findable/唯一v1：Submitted May05 13:08:18Z、registered May06 02:01:24.000Z，组合bounded May06；不再列普通日期待办。日期具名核验不改变原160表。

## 4. root必要原证

### 2605.03135v1 — instance-level cost

[exact-v1](https://arxiv.org/html/2605.03135v1) §3.2–3.6/§4.1–4.2/Table1–2实际读：NEC=sum(cost×错误)/sum(cost)，vote log-odds、阈值距离及LLM rating只是三种cost构造，不自动等真实危害。80/10/10切分、10seeds/95%CI，text/image/tabular/frozen或finetuned头，重加权并非一致改善；iNaturalist frozen反退。§3.2 regret/min/sign有明显排版或定义冲突，不能照抄为可执行regret公式；只采独立清楚的Eq1测量及有限对照，不授临床/安全成本真值、普遍加权收益或部署SLO。2+1+2=5；必要Source已读，待非作者独核/实际owner比较。

### 2605.03313v1 — bounded adversarial gradients

[exact-v1](https://arxiv.org/html/2605.03313v1) §1–3.3/4.2/5实际读。非无偏噪声：每次reply与真梯度距离≤ε，可有偏/对抗；凸L-smooth且已知最小解norm≤R时，Thm2构造两不可区分1D函数支持εR/2最坏误差下界，不能由更多查询消除；未知R的有限query不可达不等于“即使精确梯度无限查询也不行”。AGP-opt 4ε停点和步长1/(2L)与5εR上界依赖自身前提，不外推LLM。§5把sigmoid平方误差称凸并不能一般成立，实验又关闭理论early-stop，故实验不能认证全定理/实际LLM隐私或Byzantine能力。2+1+2=5，仅拟保凸oracle偏差floor及假设，不采全部算法/实验保证；待非作者独核/owner。

### 2605.03598v1 — multi-hop regularization

[exact-v1](https://arxiv.org/html/2605.03598v1) §3.1–3.3/§4/§6实际读。表示诊断用normalized W的有限hop和，任务长L限定2～L+1；训练正则则原W且1～L+1，避免靠增大归一化因子虚降罚项。10个1层RNN、16hidden、4modules、合成平均/开关信号、200epochs/10β对照；不能把signed-path抵消叫实际删边，亦不是nonlinear神经元完整Jacobian或Transformer因果解释。leaky-cascade先验、有限horizon与额外matrix powers成本是代价；保留weight-L1用于参数稀疏的原目标。2+1+2=5；必要Source已读，待非作者独核/owner。

## 5. 当时停点（后续已推进，非当前待办）

机构有限补查完成但不授全Coverage；新增具名准入/Source分批进行，尚未冻结最终候选与Books处置。A负责HyPA/Sensitivity/GRPO及第二批03359/03820/03877/03866，B负责Bifrost/SigLoMa/LDM及第二批03438/03566/04013/03722，reader独核准入与必要Source/纠错，root拥有Report/Books/LS。普通Source/Books/日级验收尚未完成，不能改成外部终态或加日级计数。

## 6. 当前汇总及实际写后复核（待整份日报DAY）

48唯一完整题摘最终为19确定May06候选、2跨日潜力、1撤回、2早期事件线索、24贡献关闭。19＝17受限机制实际整合/2中心争议；旧160逐字冻结、原小时窗和连续原§4保持，总179。准入与证据的改判均保存，未因工作量或现书覆盖缩池；03722已实际有效日期，03866据具体早正文关闭，不再当新首发。24关闭中reader实际独核14题摘/必要core，另外10项未独立逐题摘，精确名单R17；不能称48/316全量独核。

17家族唯一owner为Ch4/5/23/24/26/28/30/33/49/55/66，共11章。root本次独立实际打开并对读reader作者的ReLU Thm4.11/Remark4.12、Cartan v2§4.1–4.2/Remark4.1、QKVShare exact-v1 PDF§4.2/6–7，及B的EDL III/IV、Bifrost III-C/D/IV、SigLoMa§3.2/Table1、LDM Thm1/A7.1、Mantis Eq9/A2、compiler III/TI–II、CDS条件path/共轭W1；只接纳本日报的窄命题，未验证全部附件/代码/复现。

root实际读Ch4 ReLU、Ch24 Cartan/CDS、Ch49 compiler全部新增段、完整两侧及本人来源注，非作者POST通过：open集非a.e.、v2后来纠错非首发、known-density初始化/积分、编译依赖/端口与CPU旧路径都保留。其余13项实际POST由reader R12–16执行（含Ch28尺度缺失真实修复读回），root消费其具体结果，非仅作者声明。root自身新来源注只含原证/证据边界，LDM已把泛称variable covariance改为input/state-dependent，允许时间依赖不误排。

19新增与相应§4/Books具体位置已写进当前Report；源表只1套14每日＋1具名触发OpenReview。初稿把原160与19新表之间插说明而打断Markdown表，已移除中间说明/空行形成一个连续179行表，不另加重复表头，也不修改原160行。V3已实际通过；205本地引用零缺失、fence偶数，冻结基线SHA/连续原§4和160行实际比较通过；限定unstaged/cached检查与最终DAY仍按当前实际结果，不沿用旧全绿。

CPSC/DMGD中心保证不授正面Evidence/Books；KAHM/02930日期与机构历史缺段具名隔离，无普通Source或Books待办。随后非Report作者R18六部分DAY及02:37:45完成态R19 FINAL均已真实通过；root实际读回R19后同步127/279。本日报当前209本地引用0缺失，V3、19日期工具测试、冻结比较与限定两层diffcheck通过；旧41/42窗口回归限制不冒称全绿。全部本日Books窄位及三个子任务ownership已释放；转fresh05-08，不复用本日语义上下文。未stage/commit/push。

