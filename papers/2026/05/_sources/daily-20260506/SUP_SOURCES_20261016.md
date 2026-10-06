# 2026-05-06 唯一补查记录

作者：`/root/supp_may06_author`；仅补 2026-05-05 北京时间自然日。原137候选、评分、日期、09:00小时窗及连续原§4保留；完整运行前快照为 `baseline-before-supplement-20261016.md`。不改共享Books/LS/index，不stage/commit/push。

## A1 启动与准入待独核

已完整重读AGENTS、当前RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、RESEARCH_SOURCES使用说明/每日/arXiv、ROADMAP与LS任务路由。使用daily-research-closure，现行合同优先于技能中的旧exact-v1/分母冻结措辞。当前进行中，不预支DAY或完成。

### 同事件去重（非作者root已实际核准）

- [MSM官方Blog](https://alignment.anthropic.com/2026/msm/)标05-05，完整核心讨论了相同AFT数据而不同spec的OOD泛化、41M MSM token与高样本CoT饱和限制；与[05-05旧02087证据](../../05/README.md)同事件，Ch28已有versioned behavior spec→midtraining→AFT→heldout链及误规范/非runtime enforcement边界。复用有效审阅，新增0，不改旧日期评分。
- [MRC官方Blog](https://openai.com/index/mrc-supercomputer-networking/)标05-05，核心为多plane packet spraying、每包最终地址支持乱序、丢包path退出/probe、trimming区分destination congestion、静态SRv6；与[05-07原04333证据](../../07/README.md)同机制family同事件。root已actual核原§4和Ch36唯一owner主判断；Blog无实质修订/反证，不新评分或造Books diff。

### 有界arXiv发现与准入准备

12个官方历史分类月列表真实请求得到404/timeout/cache miss（SUP_API_B2、SUP_ROUTE_B1、SUP_ARXIV_B1），不作为历史0。关键词主题查询只返回少量窗外线索，未用Submitted作公开日。既有May namespace原件00–03前缀只按May05的v1 Updated字段找发现线索；该字段不独立证明公开日。一次regex主题投影过宽，已停止，不把467条原命中或322 ledger-unseen变为逐项工作队列；SUP_ARXIV_TOPIC及SUP_BOUNDED_B2是截断无效投影，不支持任何分母/覆盖/日期断言。

有界标题浏览保留下列18条可能改变主线解释/设计的具名核验点，02038已经05-05原报告同事件去重，其余17完整题摘集中在SUP_NAMED_AB，官方exact-v1 abs及当前修订/撤回信号集中SUP_ABS_B1、SUP_TAIL_B3及随后原件。没有因关键词、章节映射、单benchmark、组合模块而自动入选。宽列表其余不变强制队列；本日尚未完成日期与准入独核。

|身份|原约束→题摘实际增量→影响判断（待独核，不是审阅完成）|
|---|---|
|00941|单步flow不确定性常需额外头/多次采样→线性interpolant的Tweedie协方差恒等式→核验posterior不确定性与velocity divergence的权限；May1早提交到May5登记跨日，日期资格先保留|
|01973|固定FFN非线性难按文本条件适配→hypernetwork预测SwiGLU beta→把条件控制移到FFN gate而非逐任务finetune；拟MODEL-FFN|
|01627|singular coefficient magnitude未必等于task loss贡献→Taylor敏感度+曲率与Hutchinson估计选basis→改变低秩压缩删basis准则；拟INFER-TENSORRT-LLM|
|01203|math PRM表现被外推到通用过程判断→knowledge/computation错误检测互补失效→核验PRM适用域；通用逻辑评价不是科学应用，不能因science字眼硬排|
|01107|硬kNN图邻域跳变影响表示比较→diffusion class-chain/Markov quotient条件与平滑扰动→核验表示几何观测的有效条件；小模型/CIFAR本身不排除|
|01711|attention全局建模被等同显式二次聚合→动态参数化MLP替代全局表示→核验线性路径能承载何种全局信息；视觉架构不因非LLM硬排|
|01324|小MLLM RL可能强化perceptual shortcut→训练bias model并以repulsive CDPO纠偏→核验数据偏置与reward目标的因果权限|
|01424|加模态未必增可泛化信息→pairwise metric learning上/下界的modality granularity条件→核验可否支撑多模态表示的长期有效条件|
|01256|base adapter事后并入instruct模型不受target引导→instruct confidence引导base LoRA后transfer→核验任务能力与instruction retention的更新归属|
|01229|raw cross-attention被读成内容对齐→非内容token/vocabulary sink遮蔽关系→核验可解释性测量的具体反例而非只翻译准确率|
|01158|只计final pretraining低估生命周期成本→Olmo3 rollout与失败/试验运行能耗拆分→核验推理型后训练资源预算是否改变；不是单绝对数字|
|01061|per-sample MoE routing被视作task隔离→expert内梯度冲突/FedAvg破坏正交与per-expert梯度subspace→核验遗忘保护条件|
|02073|reward函数人定可能错配reasoning→search优化reward的机制待完整题摘关闭/准入，不因RL+搜索组合自动入选|
|02598|职业暴露按静态task表现→RL可学习性作测量；是否只有社会/职业应用、无模型设计增量须语义判断|
|02111|deep network谱/几何关系→必须读清具体理论假设及改变何种表示判断，不因理论标题排除|
|02108|同上，独立identity不假定与II重复，先核正文必要贡献|
|01742|NAS+ToMe+fp16用于IC缺陷分类→题摘目前仅组合/性能数，拟排除；没有新交互机制或归因条件|

首批准入与代表排除提交root独核；明确通过者再评分及必要Source，不因读全文费时或Books已有主题缩池。

## R1 root非作者首批准入与日期校准

root实际打开01973v1、01627v1、01742v1官方abs并读完整题摘与精确版本/历史，非只看metadata当前摘要。01973把文本条件转成SwiGLU β、以FFN非线性而非逐任务权重更新承载条件，01627从重学singular coefficient幅度转向预计删basis的task-loss增量及曲率估计，均有具体设计准则差额，准入通过；各5分建议只决定必要Source最低投入，不预授方法结论、Books或性能。01742明确为AutoFormer+ToMe+fp16及工业任务部署，题摘未给新的交互机制/成立条件或足以修正设计的反证，具体贡献前关闭通过，不因半导体领域或视觉模型简单排除。

root实际读当前官方availability公告表L185–186，并纠正自己先前把周末接收截止记成Sunday14的错误提示：官方为Thu14–Fri14→Sun20，Fri14–Mon14→Mon20。按01973/01627真实v1字段，前者Sunday13:13EDT、后者Saturday18:35EDT均最早MondayMay04 20EDT＝May05 BJT08；精确DataCite同身份arxiv.content/findable registered上界均May05。root实际分别运行现有只读日期工具，两者完整区间bounded May05；工具未改，原件由作者实际取得，官方abs v1字段独立吻合。00941 Friday00:25EDT属于前一接收段，最早May04、上界May05跨日，不能择目标日；只保日期请求，不先深审/评分。此具名校准不泛化其他14，按各真实字段复算，无需重复抓取既有效原件或扩月。当前只有准入/日期层通过，不授Source/Books/DAY。

## A2 具名日期组合实际测试

root提出周末下界复查后，作者actual重读[官方公告表](https://info.arxiv.org/help/availability.html)：Thursday14–Friday14→Sunday20；Friday14–Monday14→Monday20。当前本地工具逐原件运行：

- `SUP_DATE_2605.00941_20261016.raw.json`：精确doi，arxiv.content/findable，唯一v1 Submitted `2026-05-01T04:25:00Z`，registered `2026-05-05T03:00:32.000Z`；工具最早 `2026-05-04T00:00:00Z`，跨May04/05，unresolved/cross_bjt_dates。不是以Updated硬落May05。候选资格隔离，需实际日公告/作者早稿公开日期才能重开。
- `SUP_DATE_2605.01973_20261016.raw.json`：同身份与client/state条件，唯一v1 Submitted `2026-05-03T17:13:45Z`，registered `2026-05-05T03:27:05.000Z`；工具最早 `2026-05-05T00:00:00Z`，整个区间08:00–11:27BJT都在May05，bounded。Sunday13:13EDT并不归Sunday20公告；它在Friday14–Monday14接收段。只证conditional arXiv公告日，不证全球first-public。
- `SUP_DATE_2605.01627_20261016.raw.json`：唯一v1 `2026-05-02T22:35:02Z`，registered `2026-05-05T03:18:20.000Z`，同一Monday20下界；待root日期校准核准后继续贡献核验。

原件去掉重复base64 XML但其余DataCite字段/relationships未改写。2025-01-06官方规则快照链接本次web cache miss保留SUP_RULE；合同已核准可复用历史规则，后续若需用原公共raw核同一表，仅定点规则不扩论文/版本史。A1“周末合证可落窗”不作一般断言，仅上述actual区间支持个案。

root随后的独核明确纠正自己的Sunday14口头提示，actual官方表和现工具一致，01973合证有效、00941跨日保留，不把共同误提示扩为全17隔离。作者也随后直接curl取得2025-01-06 raw规则正文（相同Thu14–Fri14/Sun20、Fri14–Mon14/Mon20及公告前不发ID），成功恢复不是长期外部缺口。

## A3 14每日源有界检查与真实停止位

本次检查时点2026-10-16 +08:00；历史网页当前表现不反推当时完整性。所有查询/失败和原件在同目录SUP_WEB_B0–3、SUP_MORE_B0–2、SUP_API_B0–2、SUP_ROUTE_B0–2、SUP_ARXIV_B0–1、SUP_DISC_B0–2、SUP_TAIL_B0–3。带Warning的超长投影与空壳不能证明覆盖；已另存足够小的成功关键原件。14到期源均已真实发起有界检查，仍不等于所有历史段正面覆盖。

|Source|实际入口、主题与停止位|结果/限制|
|---|---|---|
|SRC-OPENAI|Research当前页及官方域名May5 research查询；具体MRC、5.5Instant核心、YouthSafety与广告题名|MRC同事件去重复用；Instant主要产品表现/个性化控制、未披露可归因机制；Youth/广告为政策商业范围，不评分。Research历史完整分页隔离，不声称无遗漏|
|SRC-ANTHROPIC|Research当前页及官方域名May5；直读alignment.anthropic MSM全部核心、Safety Roadmap的May5两处修订说明|MSM同事件；Roadmap只调整数据保留goal/安全研发目标日期，未披露新控制或安全保证，关闭。Research当前最新10不是May历史0|
|SRC-GOOGLE-AI|DeepMind研究页/Research publications及两个官方域名May5+language model限定检索|仅当前focus/年份目录与无关科学项，不把搜索空当历史0；May5精确publications与Blog历史段不可恢复，终态隔离|
|SRC-META-AI|官方Research static空壳及官方域名May5研究query|当前空壳不证明历史0；历史研究目录段隔离|
|SRC-QWEN|旧入口→qwen.ai/research空壳→真实article/retrieval en-US投影（SUP_ROUTE_B0）|当前回传40条唯一条目，邻近Apr30 Qwen-Scope与May19 LiveTranslate；返回目录中无May5，不能证明删除/未返回历史段。SUP_API_B0截断不用作依据|
|SRC-DEEPSEEK|官网+官方updates完整日期段；May5域名query|updates相邻Apr24/Jul31，无May5条目；官网当前focus不证明研究全史，未公开/删除段不授覆盖|
|SRC-MOONSHOT|Kimi Blog首屏全列和changelog，May5官方域名及MoonshotAI定点检索|Blog/changelog停在2025-11且无本次May5可核历史段，精确隔离，不把过时目录当2026无事件|
|SRC-TENCENT-HUNYUAN|Research空壳后publicList实际POST page1 size100 renderType0/lang zh；9条total9，回传lang en原样保留|Apr30 context到Jul07 Hy3相邻；本次返回slice无May5。publicAt/displayPublishTime不同，不倒推早期公开；缺失语言/已删除历史隔离，不宣称全站无遗漏|
|SRC-ZAI|Research时间排序首屏至2025-12及官方release notes、May5域名query|相邻Apr29 ScalingPain/May20 ZCube；此回传研究段无May5，普通news/法律应用不纳本项目；不扩整个GitHub|
|SRC-BYTEDANCE-SEED|Research+public_papers网页；从本次JS发现get_article_list_v2，paper type1带x-tt-localeUS，publish_year2026/count20，offset0→20读到Apr15；Blog type2 offset0 total20/has_morefalse|paper回传18+20条（total86不是当日数），May06科学发现/M04视频为两侧，May05无主线题名；May06科学题名在暂缓范围外不读全文。Blog15可见条到Feb，Jun18/Apr22夹May5；本次空array type0和缺locale返回不作0证据。PublishDate为目录标注日期，不自动证明全球first-public；不扩剩余Apr前分页|
|SRC-BAIDU-ERNIE|Blog中文第一页全11条到2025-11，页面2/2链接在尾|Apr30/May9相邻，目标May5段无条目；不为窗口读取更旧页|
|SRC-XIAOMI-MIMO|官网Paper全部8条、Blog15条及More入口可见；May5域名定点搜索|Paper Mar13/Jun29相邻，Blog没有日期/More历史段无法恢复，精确隔离；不以Paper排除Blog事件|
|SRC-MINIMAX|中英文Blog和Agent Tech Blog实际页；May5日期限定query|英文Mar18/May26夹窗，中文当前页只导航、Agent技术目录无可核May5段；英文段未见项，中文/Agent历史片段隔离|
|SRC-ARXIV|12分类历史月列表+主题query实际执行；本窗May05 v1 Updated metadata仅topic发现，当前仅18具名点并定点2026同事件去重；公开日另用精确abs/DataCite合证|月列表不可恢复，不授标题补检Coverage；467 regex投影过宽已收窄，非候选队列。14具名DataCite原件actual工具boundedMay05，00941跨日；01742/02598拟明确贡献/范围关闭，02038同事件去重。准入/Source仍普通进行中，未写0候选或源全覆盖|

无Weekly发现扫描；本轮未触发额外会议/框架release按需全扫。可用官方必要单篇证据不因其站点扫描频率受限而拒绝。

## A4 首两项必要Source与具体owner/PRE（作者prepared，非独核通过）

已加载Books所需PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、ROADMAP/LS及Ch16/49实际目标与两侧交接。只提出窄段，不自行写共享Books。

### 01973 — 2+1+2=5，标准必要审阅完成，长期采用所需具体机制补读

原v1 §5.1/Eq8–10、§5.3：冻结base weights；条件文本复用embedding作为query，layer latent作为key/value做低维cross-attention，加layer embedding后生成逐层SwiGLU控制偏移，训练的是hypernetwork，不是每次输入再优化base。§6.1–6.5/Tables4–7：Llama3.1-8B-Instruct、R128、3.41M可训练参数，Persona/AdaptSum/CrossFit&UnifiedQA/SNI及未见style/task；prompt/layer embedding/L2消融说明控制器组成有作用。T6有引用外文baseline，GSM8K/HE/MBPP本方法可低于若干对照，不能把overall average写成逐任务占优。A7为2048seq/up to48A100；精度、完整训练/推理墙钟、并发/SLO、独立重复不充分披露，不采用速度或任意条件可靠性。B2坏例明确persona/sentiment失败。root指出后作者actual补读§5.3 footnote及A2详细实现：实际用Swish_(1+beta)，末tanh约束的是相对1的偏移，beta=0回原模型；原“正beta与tanh冲突”提示撤回，不是中心争议。A2给对beta的局部导数界，仍不授整个hypernetwork/LLM全局稳定性；无需版本diff。

具体owner `MODEL-FFN`。当前Ch16 SwiGLU之后仅说明Gate依赖当前token、更多projection付费；尚无外部条件控制activation slope且controller可能读取上下文的分支。拟在以下实际逐字PRE与后继标题之间增一段：

PRE：`Gate 允许模型根据当前 token state 动态调节哪些 candidate features 通过。代价是多一个 `d_model x d_ff` projection，因此实际模型常调整 `d_ff`，在参数预算下比较，而不是保持所有维度不变。`

后继：`## 参数量与 FLOPs`

拟正文（A6之后经root纠正并actual补读修订）：当同一基础模型要随任务、风格或persona切换时，还可固定主权重，把条件控制放到activation的斜率：以条件文本作为query、当前层状态作为key/value做低维cross-attention，加层身份后生成相对1的偏移beta，再以`x*sigmoid((1+beta)*x)`控制SwiGLU gate，beta=0回到原SiLU。给定控制量后的FFN仍逐位置执行，但控制器读取条件与序列状态，整条适配路径不能再被描述成只有当前token的局部非线性。这以新增控制器、条件版本耦合和每层执行开销换少量可训练参数；冻结base不保证不遗忘或遵从任意persona，条件错配、held-out任务退步或额外费用不合时，保留原SiLU/普通prompt或独立适配。有限Llama/Mistral对照仅证明这条控制接口可行，不授普遍优势或推理加速。[受限证据](https://arxiv.org/html/2605.01973v1) `<!-- source-family:SF-2026-ARXIV-2605-01973 -->`

### 01627 — 2+1+2=5，标准必要审阅完成，长期采用所需具体机制补读

原v1 §3.1.1/Eq重要性、Alg1：删rank-one basis即sigma_i置零，以`-sigma_i E[g_i]+sigma_i^2 E[H_ii]/2`排序，symmetric Rademacher扰动差梯度估计Hessian diagonal；保留candidate pool使部分大系数未估曲率，不是全部basis穷尽最优。§3.2/A2：Taylor余项需C2/Hessian-Lipschitz，独立probe消去cross terms是在期望，不是有限样本无偏精确保证；谱powerlaw才给维数无关方差形式，中间层Hessian可负。B1同时给epsilon下界却用min cap的配方，不把其通用精确epsilon recipe写入Books。§4.1–4.2/C1对照SVD/FWSVD/ASVD/Basel；Llama2-7B/GSM8K/MATH，各方法均先任务微调→压缩→后微调；浅压缩相近，深压缩quality差异受该完整pipeline限定，不外推其它任务、无数据PTQ或Serving提速。硬件/精度/完整墙钟/seed/并发/SLO在必要段NotDisclosed，未运行代码/复现。原件SUP_SR_B1–4；current exact-v1 abs未遇撤回或实质修正信号，不遍历v2。

具体owner `INFER-TENSORRT-LLM`。Ch49已有activation-aware目标、empiricalFisher与重构混合、AA-SVD和TP低秩布局；都没有把“所删singular basis对task loss的局部增量”与“保留奇异值大小”区分为可付费选择器。拟在原AA-SVD两段之前增一段，不移动其他源：

PRE：`低秩因子化也要区分重构参照和实际输入。上游已压缩后，当前层收到的 X'不同于原模型的 X；保持 W'X接近WX、保持W'X'接近WX'，以及用W'X'追原WX，是三个不同的局部目标，不能只以“SVD误差”合并。可在有限校准集上按顺序拟合，再以完整 block输出共同修复 factors与局部Norm参数；这是付费的局部适配，不是任意输入上的函数等价。<!-- source-family:SF-2026-ARXIV-2604-02119 -->`

该PRE保留逐字不改；拟新增放在PRE之前（即MOONSHOT末段之后、AA-SVD首段之前）：按奇异值或重新学得的系数大小保留basis，是数据与准备预算较少时的简单低秩选择；若目标任务损失对不同方向的敏感度不随系数单调变化，可把删去一个basis视为将其系数置零，用一阶敏感度和二阶曲率近似这次删除的损失增量。对称随机扰动下的梯度差可估计所需Hessian对角，却引入额外profiling、数值扰动、样本方差及候选池偏置；多个basis共同删除还有交互与Taylor余项，局部排序不是全局最优证明。有限数学任务的前后微调pipeline支持质量/模型大小取舍，不证明无恢复压缩或runtime加速；预算不足、任务迁移或估计不稳定时，保留简单幅值/重构选择和更高rank。[BSI受限证据](https://arxiv.org/html/2605.01627v1) `<!-- source-family:SF-2026-ARXIV-2605-01627 -->`

以上两个Prepared PRE待root实际Source/owner/PRE独核与窄写授权；当前Books未写，未称整合。

## R2 root首两项必要Source、具体owner与修后PRE

root实际打开01973精确v1 §3.2、5.1–5.3、A2：层状态e_l来自本层Transformer，Eq9明确条件embedding作query、层latent作key/value；额外cross-attention确使适配路径不能整体当逐token局部FFN。§5.3脚注与A2 Eq14明确实际使用1+beta的偏移参数化，beta=0回原SiLU；不能仅凭§5.1的正斜率与tanh就断言实现矛盾，作者需修A4相应表述。root实际读Ch16标准FFN至SwiGLU完整论证及参数/FLOPs交接，A4单段差额成立；限采用外部条件/层状态控制activation slope，修为相对1的偏移控制，明确q/k/v方向，不采通用稳定性、抗遗忘或速度保证。授此修后单段及本人章末注窄位，不授POST。

root实际打开01627精确v1 §3.1.1/Algorithm1、3.2关键假设、4.1–4.2：重要性是删basis的局部Taylor近似，有限扰动/候选池付费；所有对照均含任务前微调和压缩后微调，小压缩近似、大压缩分离，不授无恢复PTQ或runtime收益。实际读Ch49 MOONSHOT完整两段、AA-SVD完整两段与DeInfer交接；A4拟段在MOONSHOT末段之后/AA-SVD首段之前，补系数大小与task-loss删除敏感度的分责，非重复重构目标。May05 RCO指定窄位已root C2 POST释放，现授BSI此单段及本人注窄位；不得改RCO或其他旧正文。作者保存后发真实位置，待root非writer POST。此两项采用只限已核局部命题，不授整日验收。

## R3 root余12完整精确题摘准入及一代表排除

root实际逐一读取本日13份SUP_EXACT_AB原件的完整Abstract与版本记录。01107的贡献是共同平滑operator观测相对硬邻域跳变的测量边界；01203为过程评价跨错误类型迁移反证；01711为全局descriptor生成固定大小动态参数的替代架构；01324改变bias-reference排斥目标；01424尝试给模态互补/函数类条件；01256把目标instruct的confidence置于base-LoRA训练前端；01229对cross-attention观测有效性提出反证；01158改变生命周期成本统计边界；01061直接挑战sample routing等参数隔离；02073改变reward生成/训练/反馈搜索；02108/02111分别处理同一operator链谱预算与额外physical-channel证书，不能因系列名相似合并。A5具体准入/三维提案均与拟核命题匹配；小模型/理论结果并非仅AI相关，亦不借章映射倒推贡献。此为全部12准入校准，不授Source/Books。

02598完整题摘是职业任务rubric/专家校准的政策估计指数，没有实际训练可学习性或优化/系统新机制，支持A5贡献前关闭；不将职业可训练性词汇映射为本项目训练结论，也不为不影响处置的日期另造请求。01203题摘中的http URL抽取断句只作发现，A6已有精确正文必要原证，不把损坏AB当实验结果。已知三项中心反证仍须实际必要段独核，不因Source费时删候选。

## R4 root首两Books实际写后复核

root非writer实际顺读Ch16保存单段、前方完整SwiGLU定义与Gate取舍、后方参数/FLOPs及本人末注：条件query/层状态key-value、相对1偏移及beta0退回均落实，新增controller使整体路径非逐token局部的边界和全部费用近置。另实际顺读Ch49 BSI单段、MOONSHOT完整前文、AA-SVD完整后文/DeInfer交接及本人末注，局部loss敏感度与系数幅值区别已落，Taylor交互、有限估计和前后微调限制没有被省略。两项真实POST通过，指定Ch16/Ch49单段及本人注窄位均释放，作者仅行政同步已发生事实并读回，不授整日完成。

## R5 root三项中心争议的必要原证独核

root实际逐段读本地已保存精确v1原文：01424 §2、P3.19/T3.20；01229 §3.2/Table1、3.4、4.1/4.3、5.1/Table2、6.2；02073 III-E1–3、III-F/Algorithm1、III-H、IV-E、V-A。不是复述A6。01424同一经验风险差在嵌套exact ERM下≤0，T3.20却给允许参数下的正下界，prose还把差的方向解释反；01229表中content9–17%、language1.5–2%与两正文30–35%/40–45%不合，定义cos-to-uniform越高越分散却据generated较低值推更diffuse，且无词表/位置因果控制；02073全部50trial与7ensemble同test选择并反馈，随机5对照不隔离ranked feedback，重跑seed/对固定test bootstrap不能恢复独立泛化。支持各自A6的争议隔离，保原准入/6或5分，不写Books、不将隔离算Evidence通过。重开各自所缺：一致定理及假设、可复查测量和受控归因、独立holdout及匹配搜索对照。有限有效定义可以保存，但不借成熟原则另制造Books diff。

## R6 root余九项必要原证、具体owner与八窄位PRE

root实际读取本地保存的精确v1必要段：01107 Definition1/Theorem2、硬kNN反侧、§6.2/7；01203 §3.1/3.3、4.1/4.3/Table4及限制；01711 §3.1–4、动态块频率消融与结论；01324 §3.4.1–2/Eq6/Table2、4.1/4.3与C1；01256 §3.1–3、4.3、5.2/5.6及限制；01158 §3.1/3.3、共享训练分支、4.2–4.3及power profiles；01061 III-B、IV-B/Prop4证明、IV-C、V-C/D及A-D初值/增量条件；02108 §6 operator-chain测量权限与02111 D4.3/T4.12/D8.3/P8.7/P8.10/§10.3。以上原文支持A6收窄命题，不表示所有附录、代码、图像或实验已复现。

实际逐字读A7全部八拟段及目标完整局部：Ch5第四层内部分析至第五层线上闭环；Ch14 latent/polynomial至projection-free；Ch66 transformation stability的PRM两段至规则verifier；Ch33 clipped objective/reference KL停止条件至正负clip；Ch30持续expert更新至固定rank、merge标题与后继资产论证；Ch70成本等式至adaptation；Ch17 I+JF/Residual边界至几何责任与Norm。各差额分别为共同平滑观测、域/首错校准、固定descriptor动态参数、具名bias-policy repulsion、target-conditioned训练/merge、共同projector线性聚合、共享生命周期计量与估算、谱链/物理证书分层；不只靠章主题映射，近文保留反退/费用/适用边界。

授A7八个指定单段及各本人末注窄位：01107 Ch5、01203 Ch66、01711 Ch14、01324 Ch33、01256与01061 Ch30两处、01158 Ch70、02108+02111 Ch17同一段双source。不得更改既有论证或别人的注，尤其Ch5 May05潜在encoding-probe位不同，写前重读当前文件。准备稿保持具体公式/条件权限，不把任何源包装为普遍质量、遗忘或稳定性保证。写后需root真实POST，不预授DAY；三争议项另按R5隔离，不给Book lease。

## R7 root余九源实际正文写后复核与全部lease释放

root非writer实际逐段顺读八处保存正文及完整前后邻接：Ch5内部分析至线上闭环、Ch66 PRM transformation至规则verifier、Ch14 polynomial至projection-free、Ch33 KL停止至正负clip、Ch30 expert持续更新至固定rank及merge资产、Ch70训练成本等式至adaptation、Ch17真实Jacobian至几何/Norm；并实际逐项读九源本人Review notes。均与R6/A7采用稿一致，具体机制、有限条件、反退/失效与全费用近置，双GSA分清谱链和物理证书而非静态曲线认证。没有在Review notes后追加机制，没有覆盖旧正文。八处真实POST通过，九源指定窄位全部释放；作者可只行政同步已发生事实并读回。连同R4，11新增整合已落实，三争议按R5隔离；尚待报告六部分实际DAY/完成态FINAL，不预签整日。

## R8 root六部分日级独立验收

root作为补查非报告作者，实际读取保存后的开头/§1、本轮14行候选及日期说明、全部新增§4证据、§5与§6；旧137的身份/日期/评分/有效证据只冻结复用，不重跑。实际复核A3十四每日来源入口、主题与停止范围，确认467/322宽投影已撤销为无效发现而非待审队列，机构历史缺段及00941日期请求被隔离，不把不可恢复段记零或全Coverage。另逐原件读取十五份SUP_DATE的DOI、client、findable、唯一v1Submitted与registered字段，14确实最早/最晚同May05，00941跨日；没有靠Updated/created字段选择目标日。

全部14准入/评分、必要Source/直接反侧与最终Books逐项闭合：11有限整合共10段9章，R4/R7实际非writer正文/完整邻接/本人注POST通过；3中心争议R5明示不支持正面证据/Books，精确重开条件可定位。01742/02598两个不同原因排除已实际完整题摘独核，MSM/MRC具名原证与具体旧owner有效去重；其他明确负侧按官方技术/产品/政策及真实返回slice分层，不声称全历史题名已独核。实际读回本人注行政同步并核报告一致性，无剩余普通扫描、Source、PRE或POST工作，只有完成态字段保存与FINAL待办。

root实跑V3通过，冻结比较原137整行/原小时窗口和连续原§4均保持；310本地引用无缺失，报告/SUP及九章限定unstaged diff-check通过。机器通过仅证明接口/保存，不替代本段实际语义复核。日级结论通过，可由作者保存完成态/§1/5/6真实状态，不得删除隔离项或写全Coverage/Evidence；完成态仍须一次实际FINAL，不预签。用户要求本日期完成后暂停，不接新日；无stage/commit/push。

## R9 root完成态实际FINAL

root实际读回2026-10-16T18:00:35+08:00保存的完成态开头、§1/5/6：14新增＝11受限整合/3争议隔离，9章10段均真实POST；00941及逐源历史缺段继续不支持正面证据/Books/无遗漏，不把它们变为Evidence或Coverage通过。无剩余普通工作；旧137的日期评分与连续有效证据保持，未以历史通过冒充新增验收。完成态V3与本日README/SUP限定cached/unstaged diff-check实际通过，root只验本日补查及必要受影响Books，不宣称全树或全年完成。FINAL通过，本日作者ownership/所有窄lease释放。按用户要求不接新日期；root仅等当前May05收口后保存总checkpoint并暂停。无stage/commit/push。

## A5 余项逐原v1题摘准入准备（待非作者校准）

本次直接curl每个官方exact-v1 abs，取完整Abstract/Submission history保存在 `SUP_EXACT_AB_2605.*_20261016.raw.txt`；并actual阅读完整题摘及当前修订/撤回提示，未遇撤回、纠错或重要修订说明。字符串检查仅辅助定位，作者实际语义判断不由False标签替代。01107的v1是synthetic+MNIST、不是metadata当前v2的CIFAR/ResNet；后续采用只准v1。其余具名结论与A1具体增量相符；不把本次恢复的完整AB当Evidence Review完成。

|identity|准入/评分提案|改变的具体判断与必要审阅|
|---|---|---|
|01107|入选2+1+2=5；WORLDVIEW-REPRESENTATION|从硬kNN邻域比较改为同Gaussian diffusion operator的平滑观测；MNIST/平衡共享协方差条件需核，非LLM理论硬排|
|01203|入选2+1+2=5；PLATFORM-EVALUATION-SYSTEM|PRM跨知识/计算错误能力不等价，通用过程评价修正外推；science/logic是reasoning evaluator而非科学应用|
|01711|入选2+2+2=6；MODEL-SELF-ATTENTION|动态参数MLP压缩全局状态提供显式attention替代设计，需核表达/成本与Vision→causal不可外推边界|
|01324|入选2+1+2=5；TRAIN-GRPO|bias model repulsion引入不同RL更新目标并针对shortcut，需核消融与数据/compute可比，不因“causal”字眼授因果|
|01424|入选2+1+2=5；MULTIMODAL-REPRESENTATION|pairwise metric学习界把模态数量与细粒度/互补条件区分，需核具体函数类/边界，不因理论或非LLM硬排|
|01256|入选2+1+2=5；TRAIN-LORA|instruct target confidence在base LoRA训练时介入而非只在merge末端，需核target/general能力反侧|
|01229|入选3+1+2=6；MODEL-SELF-ATTENTION，设计反证深入|cross-attention raw权重的非内容sink使对齐测量失真；核vocab位置归因、过滤适用边界，不把filtered proxy当真实因果|
|01158|入选2+2+3=7；PLATFORM-COST|Olmo3完整开发/rollout账本修正只计final training预算，需核能耗估算方法/失误运行口径，不把单比例普遍化|
|01061|入选3+2+2=7；TRAIN-LORA，设计反证深入|sample routing不等task隔离、shared projector在FedAvg线性条件保正交，需核rank/空域消耗与直接消融|
|02073|入选2+1+2=5；TRAIN-GRPO|reward本身可搜索并反馈ranked summaries，random5-reward崩塌为直接归因线索；但在GSM8K test选reward导致有效性争议，需必要方法/控制后收窄，不照录headline|
|02108|入选2+1+2=5；MODEL-TRANSFORMER-LAYER|nearidentity residual Jacobian chain的谱漂移需要slack/残差/归一化条件，不从static spectrum猜稳定性；核rigidity假设|
|02111|入选2+1+2=5；MODEL-TRANSFORMER-LAYER|dominant-window截断与physical channel transport的margin certificate不同，需核有限矩阵测量不能代完整证书；不自动与I去重|
|02598|排除，不评分|LLM+RL专家rubric估职业training feasibility/劳动政策指数，没有实际训练可学习性实验或模型/优化/系统新机制，不从职业暴露映射Ch66/33；日期不再另造请求|

明确在scope内的理论/小模型结果按同两入口判断。若必要Source反驳中心主张，将保原贡献/分数与具体争议，不靠降分/删候选代替。

## A6 余12项必要Source作者审阅（待root实际独核；不是Books授权）

以下均实际读官方exact-v1 HTML中支撑采用命题的方法/必要假设、直接对照和反侧，而非只依据当前metadata摘要；完整下载不冒充全文通读。必要原文为本目录`SUP_TEXT_2605.*_20261016.raw.json`，01203/01061/02111以`COMPLETE`文件为准，初次空壳不作证据。未遍历版本史/无关附件；exact-v1 abs本次未遇明确撤回/实质纠错提示。只采用下述有限命题，数值不是跨pipeline保证。首两项BSI C1后续actual补读：仅结果Table1，不含硬件/精度/完整墙钟；BSI各点model size不同，不写所有压缩点逐点胜出。

### 01107 — 标准5分；表示几何观测的operator合同

v1方法/平衡Gaussian分析、Lipschitz定理、synthetic与MNIST实验和discussion实际读：同一feature cloud构造Gaussian affinity、row-normalized Markov operator与diffusion generator，再由同一operator派生transport/spectral/boundary/local指标；平衡共享协方差给的是mean-field coarse class chain的期望affinity比值，不擅自视为任意经验row-normalized chain的精确Markov quotient。固定epsilon、有界R的连续扰动常数含`exp(R²/epsilon)`，小带宽可病态；平滑不等于任务正确、语义因果或训练稳定。实验10seeds/Student-t CI，MNIST前馈；固定训练初始bandwidth、跨宽度共同中心/RMS归一化控制scale，Transformer/token/attention operator尚属future。可采用差额是表示比较须固定样本身份/标签、feature归一化、带宽与operator，不能以不同kNN图的跳变等同表示突变。当前v2 CIFAR/ResNet不得回填v1。

### 01203 — 标准5分；过程评价能力的域/错误类型权限

§3数据构造/标注/任务、§4协议/T3/T4/阈值与limitations实际读：任务是首个错误step索引或-1，不是完整每步验证；9域、15生成模型，3annotators+交叉复核，去掉无多数及错误最终答案却人工全步正确的约15%，因此是consensus-selected题集。Table2总和3595而prose3600，保留差异不捏合；“F1”是正确/错误case accuracy的harmonic mean，不是普通class F1。scalar PRM每域40个balanced dev定阈值并从eval排除，有额外域内校准预算；LLM默认thinkingoff，open3runs/closed1sample。T3显示math PRM到通用knowledge/computation不同失效；§4.3 prose把FN两边重复是笔误，T4所列top4支持PRM较高FN、LLM较高FP，不泛化全部模型。只学术reasoning首错任务，不授任意真实工作流可靠性。拟owner Ch66需具体核当前覆盖。

### 01711 — 标准6分；动态参数替代attention的表达/成本边界

§3–5方法、dynamic design对照/频率消融、ImageNet与效率及limitations实际读：把attention写成query→K^T→Softmax→V时动态隐藏宽仍为N、并未消除二次费用；随后用固定大小全局descriptor预测动态线性/卷积参数，是替代架构，不是attention函数的无损代数化简。global pooling/correlation descriptor、bilateral activation、spatial predictor与可选AAP组成具体控制接口；默认每三block插入动态块、MLP只首线性动态，更多动态块不单调好且可underfit。ImageNet1K从头300epoch、batch2048、8RTX3090；throughput RTX3090，高分辨率收益但224下T型3515img/s低于DeiT-T3661，不写普遍快。memory/perf不等causal LM能力；vision以外未验证，参数生成影响梯度与训练稳定。拟Ch14替代分支须保留descriptor瓶颈与全局统计不等逐query内容寻址。

### 01324 — 标准5分；参考分布反向KL的身份与强度

方法/诊断CLEVRER-cf、主实验/直接对照/β消融、训练协议/limits actual：小MLLM GRPO可提升observational却降低inferential；先只用observational训练bias policy500steps，再冻结并在主policy clipped-GRPO中加正β KL(policy||bias)的repulsion500steps。不是把“causal”标签当识别证明。Qwen2.5VL3B、2RTXA6000、G8、lr1e-6、β.01；train16frames与eval32frames、pixel预算不同，crosspaper baseline不授完全同pipeline。purpose-bias repulsion优于直接base self-repel/好model reference/KL-min，对照说明参考分布身份不可省略；β.1 CLEVRER62.2低于β.01的79.1，过repel损害有效知识。7B增益更小，SCM是条件化分析不是实际无混杂干预。可采用特定shortcut-reference+强度/数据预算边界，不采用通用因果推理提升。

### 01424 — 5分保留；中心理论争议，深入必要反证后暂缓Books

§2数据iid、sharedlatent/realizability、有界Lipschitz loss与projection闭包；§3 pairwise decoupling、函数类/复杂度界及P3.19/T3.20必要证明实际读。理论无benchmark不是缺陷；问题是同一嵌套class的exact ERM：P3.19给`empiricalRisk(M)-empiricalRisk(N)<=0`，T3.20却对M>N/D>1及允许的大K给此差≥严格正的复杂度差；未提供能解除同一符号冲突的额外假设。常值task或无关新增模态可令两边ERM同为0，嵌套本身不保证严格gain。L3.15有限参数空间到T3.18连续diagonal metric的cardinality桥接也未清楚，公式1/n却prose说1/sqrt(n)，不采用具体rate。保有效class inclusion与pairwise依赖需处理这一普通条件，但本文主严格收益定理未成立；保候选/原5分，中心命题争议暂缓，非理论难审关闭，待root实际原段独核。

### 01256 — 标准5分；base-LoRA训练受target confidence控制

方法/四模型math协议、GIFT-BaseT/merge/ShadowFT对照、general能力与标注cost/limits actual：同base与instruct lineage，base上训adapter后并入instruct；离线一次用target instruct teacher给reference token probability，直接未归一化confidence-weighted CE，无full distribution KL或训练中teacher调用。teacher概率不是正确性oracle，可能压低有效新domain低概率token。math2k NuminaMath-CoT、四base、r64/alpha128/drop.05/batch256/lr2e-4/1epoch2048；Avg@16不是pass@16。base teacher弱于instruct teacher，Llama/Qwen两家general MMLU/IFEval有限保留，不授一切指令不遗忘。2k标注RTX4090bs1约2m/<22GB，文件11.9MB vs2.9MB；不是free、不是完整训练提速。医疗结果不纳暂缓AIforScience，只采用math/指令分支。拟Ch30把目标模型lineage/confidence artifact与merge更新归属说清。

### 01229 — 6分保留；设计反证深入，测量与归因中心争议

NLLB200600M、1000英语句/四非洲语、12层16头及4非非洲语200句，方法/T1/teacherforced-vs-generated/归因讨论actual。special/punctuation/lang过滤后归一化只改观测proxy，不改模型attention运算。Table1 EOS78–87%、lang1.5–2%、content9–17%；§4.3/§6.2却写content30–35%/lang40–45%。§5.1 to-uniform cosine teacher36.7→70.7、generated28.7→53.8，generated的更低cos不能支持“更diffuse”解释；§7又说raw inflation95%，例值方向并不吻合。vocab-over-position中心归因没有位置/词表受控干预，§3.4本身承认EOS边界位置可能性；8语不授200语普遍律。保候选/原6分，中心解释争议、暂缓Books；不能以“attention不总是解释”泛主题NC掩盖具体问题，待root独核。

### 01158 — 深入7分；生命周期与分支成本归属

功率测量/换算、Olmo3 stage与硬件、最终vs开发账本/rollout诊断、估算限制actual。GPU测量乘1.74IT与PUE1.2；碳.332kg/kWh、offsite水1.29L/kWh、onsite0是该closed-loop站点假设，embodied用4year估计非manufacturer LCA。7B/32B Think/Instruct共享pretrain/mid/longcontext/ThinkSFT，branch后分别列后训练；Frontier MI250X synthetic data与Texas Jupiter H100训练区分。32B Think后训练约17x能耗但token33x，不能说每token17x低效。rollout87%后训能耗有generation600W近似，与trainer130–220W/75%idle测量不同权限；>10ktoken/32768max等尾长使generator是瓶颈，不推广所有GPU。开发82.2%gpuhours/80.9%energy是本组织成功/失败迭代账本，不是行业常数。可采用成本范围须纳共享run分摊/数据生成/探索失败/排队idle并标测量vs估算来源，拟Ch70具体核owner差额。

### 01061 — 深入7分；routing隔离反证与共同projector条件

§III诊断、§IV全过程、同预算ablation、实现/必要A-D/A-E证明actual：polarized top1 routing仍43/45 taskpair gradientcos≤0，冻结router并不消失遗忘，直接反证sample routing等task参数隔离。按expert维护routing-weighted gradient covariance，server对各client factor与carry-over做thinSVD同一basis，再broadcast、双边投影；FedAvg保orthogonality的可靠一步是**各client对同一P的线性组合**，不能换独立localP仍宣称成立。BilLoRA具体保护是对所保留subspace/投影残差的条件命题，A-D有taskstart B=0强条件，remark给受限h∈range(U) increment；A-E最后把这个推广成整个R算子双侧为0未由相同条件自动推出，故不采用全算子/零遗忘定理。warmup投影混合非严格投影，top-k截断丢方向、共享basis和nullspace均有budget费，router冻住牺牲再分配。CoIN6/Long10、LLaVA7B/13B与Qwen7B，5clientsDirichlet.3，4A10080GB、r8E4、oneFedAvgRound/localepoch、3seeds；TableIII另β.1不能混成同一setup。per-expert/PE-FOSU/freeze/one-sided直接ablation支持有限机制，<3%FLOPs非全wallclock。拟Ch30只写共同projector的更新协议与残余边界。

### 02073 — 标准5分；search过程可运行，但独立泛化/反馈归因未证明

III方法完整、IV直接base-only/random5/seed/format审计及limits actual：Llama3.2-3B 4bit、r32、G4、batch4、500step，每trial重置adapter；KimiK2每轮10个共5轮生成Python reward，经AST/import/probe检查（不授安全沙箱证明），与3个固定base reward相加，不是替换正确性奖励。**所有50个trial在GSM8K test1319上ranking，并将test的F1/acc summary反馈下轮，7个ensemble仍用同test选best**；它已成为搜索开发集，bootstrap/McNemar/新增seed不恢复独立holdout。random5崩塌只能说明所抽组合危险，不隔离ranked反馈vs一次同池best selection/feedbackless搜索。structural reward行数/regex不证明reasoning因果正确，正确样本更多行不排除其它hack；diversevsranked微差低于seedspread作者也承认。40h5090只是该搜索预算。保5分/标准，中心独立泛化与反馈归因争议，暂缓Books，不追加与采用命题无关附件。

### 02108 / 02111 — 各标准5分；谱测量权限分两层而非一图成定理

I实际读ResidualJacobian定义、exactpowerlaw/Frobenius归一化、slack/combinedmargin、chartresidual、T4.16/4.17与nearidentity命题/反向边界、§6protocol/conclusion。近identity generator有界给局部budget O(1/L)，不自动给powerlaw chart品质；top-radial control不等full-Cartan path，后者另付residualvariation；staticW不是I+DF(x)的Jacobian除非声明线性化/identity桥接。经验checkpoint静态spectral fit只验证一部分条件，不证明训练学到了全域稳定/rigidity。可采用operator身份/normalization/chart/slack须共同报告的判断。

II实际读D4.3不同latent/source-mode/physical坐标、T4.12完整/截断transport界及证明、D8.3事前extractionprotocol、staticradius、P8.7/8.10、§10完整数值证书/随机null与限制。source/target tail energy与operatornorm给Frobenius截断误差是有限矩阵确定性命题；源mode列不等physicalinput列。可视化聚类需固定rankwindow、rowgroup/support/tiebreak，不可后择排列当结构证书；activecolumn gaps、core-overlap/noise margin、rowenergy/profile gaps和fulltransport truncation error须真填数，heatmap亮块/partialmeasurement不能替代完整ICM membership。I与II非同事件重复：前者谱坐标transport预算，后者额外angular/physical证书。拟Ch17若当前缺此权限分层可同窄段承载两源，若已有具体充分覆盖再NC，不先泛主题消掉。

## A7 其余9项具体owner差额与逐字PRE提案（尚未授权写入）

actual读取各目标完整局部/两侧交接及相邻章节开头，保持Ch5解释、Ch14算子、Ch17层链、Ch30更新资产、Ch33目标、Ch66测量、Ch70成本分工。不把通用“需验证”当NC；以下仅9项中必要Source支持的机制/条件差额，root可按具体原文否决或收窄。

### 01107 / WORLDVIEW-REPRESENTATION / Ch5

实际位置447–487“工程上怎样验证模型学到了什么”已有basis-invariant功能比较/causal干预，却没有用同一distance-kernel operator构造多个几何读数、及bandwidth/硬邻域不连续造成观测变化的具体分支。拟在PRE之前增一段（PRE逐字保留）：

PRE：`第五层是线上闭环。持续记录输入分布、输出质量、拒答、工具失败和用户反馈，并把异常关联到模型、数据、prompt、runtime 和版本。Observability 告诉我们变化发生在哪里，Evaluation 才判断变化是否有害。`

拟正文：内部几何比较还须固定测量算子。把同一批样本的 feature 先转成 Gaussian affinity、再行归一为 diffusion operator，可以让局部混合、谱和类别间流动共享一个参照；相对硬 kNN，连续核避免把邻居排序跨界直接当成表示突变，但带宽过小、尺度变化或标签划分仍会让读数病态。样本身份、中心/RMS 归一化、带宽与 class aggregation 应共同保存；平衡共享协方差下的 mean-field 分析与 synthetic/MNIST 对照不证明任意经验图是精确 Markov quotient，更不证明几何平滑即任务正确。构图和谱/扰动诊断均付费，条件失配时保留简单距离、行为测试与因果干预，不让一组同源指标互相认证。[必要证据](https://arxiv.org/html/2605.01107v1) `<!-- source-family:SF-2026-ARXIV-2605-01107 -->`

### 01203 / PLATFORM-EVALUATION-SYSTEM / Ch66

实际2217–2239已有transformation稳定与FP/FN sensor合同，没有首错定位能力随knowledge/computation域迁移、每域scalar阈值需额外calibration的具体接口。拟放在以下PRE标题前，承接原PRM两段与marker之后：

PRE：`规则型答案 verifier 也需要同样的双向测试：对声明支持的输入形式，使用保持数学含义的改写检查误拒，`

拟正文：Transformation 稳定之外，还要测试过程判断的知识域与错误类型迁移。数学 trace 上训练的 PRM，不必能定位常识或逻辑链的首个错误；知识缺失与计算错误应分别保留正/负例，不能只把总体分数搬到新域。连续 scalar score 要转成首错索引时，还需声明逐域阈值的 dev 人口和费用；阈值校准有效不等于模型已有通用逐步验证能力。[GRBen 的受限比较](https://arxiv.org/html/2605.01203v1)采用人工共识筛选、首错/-1任务，PRM 与 LLM verifier 的漏检/误报取舍不同，不能由某一类胜出替代另一类权限。标注、分步、阈值和长 trace 调用均计费；新域或错误类型未支持时返回 unknown，并保留独立 outcome verifier，不让 math benchmark 成绩批准通用过程奖励。`<!-- source-family:SF-2026-ARXIV-2605-01203 -->`

### 01711 / MODEL-SELF-ATTENTION / Ch14

实际446–482已有latent slots、polynomial共享状态、projection-free kernel与fixed Fourier，不含固定全局descriptor→动态权重作用逐token的路径。拟放在原polynomial两段后、下列PRE标题前；保原latent/polynomial证据：

PRE：`### Projection-free Kernel Attention 是另一种归纳偏置`

拟正文：固定宽度的全局接口还可用于生成参数，而非直接保存被读取的 Value：先由 pooling 或相关统计形成 descriptor，再预测少量动态线性/卷积权重，让各 token 消费同一组条件参数。把 attention 写成动态 MLP 时，其隐藏宽仍是序列长度；改为固定 descriptor 才减少长度增长，也同时限制可传递的关系，不是既有 softmax 的无损重排。[WeightFormer 的视觉对照](https://arxiv.org/html/2605.01711v1)只在稀疏插入动态块时取得有限质量/成本平衡，更多动态块可 underfit，224 分辨率吞吐也非总优；不能外推 causal LM 寻址或通用加速。descriptor、权重生成、训练与目标后端都付费；需精确逐 query 寻址、动态训练不稳或净费退步时，保留 Q/K/V、latent 或已验混合层。`<!-- source-family:SF-2026-ARXIV-2605-01711 -->`

### 01324 / TRAIN-GRPO / Ch33

实际clipped objective既有reference KL保持漂移与共同clip gate；后文teacher attraction/repulsion多为OPD正确错误context，非另训observational-bias policy再对其反向KL。拟放在以下PRE标题前，承接KL停止条件段后：

PRE：`### 正负 Advantage 不必共享同一 Clipping Contract`

拟正文：Reference 也可承载要主动避开的分布，但这会改变其职责。若 RL 正在放大只靠观察线索的 shortcut，可先用该类样本训练并冻结 bias policy，再在 reward surrogate 之外增加相对它的 KL repulsion；它不是约束漂移的 reference KL，也不是以错误答案为真值。所避开的分布必须具名，直接远离原 base 或任意强模型不具有同样含义。[受限视频推理对照](https://arxiv.org/html/2605.01324v1)中参考身份与 repulsion 强度都影响结果，强度过大还会抹去有用知识；因果语言不替代受控归因。额外 bias training、两分布评分和强度搜索均计费，shortcut 诊断不成立或 held-out 能力退步时，保留普通 KL 约束、数据修正与 outcome RL，不授通用去偏或稳定提升。`<!-- source-family:SF-2026-ARXIV-2605-01324 -->`

### 01256 / TRAIN-LORA / Ch30

实际488–502讨论merge/teacher adapter身份、prefix资产，但没有在base更新时用最终target instruct的tokenconfidence引导，再merge到同lineage target。拟在下列PRE之前增一段，位于Merge标题之后：

PRE：`量化存储中的原位学习会产生第三种资产边界：对外仍是整数 cell/served artifact，内部却通过累积 delta、scale 或校正状态改变实际函数。同一编码字节或同一基础 checkpoint 因此不再保证同行为；registry 必须绑定更新状态、写入规则、校准和回滚点。它减少独立 adapter 的数据移动，却增加硬件特化、可复现与耐久性风险；更新频繁或审计优先时，显式 LoRA/adapter 仍更清晰。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20873 -->`

拟正文：若 adapter 先在 base 上训练、最终却并入同 lineage 的 instruct 模型，训练目标还可提前读最终 target 的偏好：离线用冻结 target 对 reference tokens 评分，以其概率直接加权 base 上的 CE，再将得到的 LoRA delta 加到 target，而不是只在末端做无引导合并。这里保存的是 target-conditioned 权重 artifact，不是完整分布蒸馏或 token 正确性标签；低概率也可能是值得学习的新知识。[GIFT 的有限数学/指令对照](https://arxiv.org/html/2605.01256v1)支持此分支，却不保证任意 base/instruct 配对或所有指令保留。Base/target revision、tokenizer、prefix、confidence 与 merge scale 须共同绑定，一次离线标注和后续回归照计；lineage 失配、低置信新知识被压制或保留能力退步时，保留普通 LoRA、直接目标适配与独立 adapter。
`<!-- source-family:SF-2026-ARXIV-2605-01256 -->`

### 01061 / TRAIN-LORA / Ch30

实际323–352已有zero-init/rankcomponent regroup，却没有跨client共同projector的聚合不变量。拟放在下列PRE标题前，位于现多模态四路更新mask段之后：

PRE：`### 固定 Rank 下，压缩距离还要回到行为影响`

拟正文：Polarized routing 也不等于 task 参数隔离：多个任务仍会更新同一 expert 内相冲突的方向，冻结 router 只冻结流量分配。一个持续联邦分支按 expert 累积 routing-weighted gradient covariance，在 server 汇总旧 basis 与 client 低秩统计，再把同一保护 basis 发回各 client；只有它们针对共同 projector 处理更新，线性 FedAvg 才保留相应正交条件，独立 local projector 不能继承这一结论。双边 LoRA 投影还须区分对受保护输入/输出分量的残差约束与整个算子不变，不能据此宣布零遗忘。[PRISM 的有限对照](https://arxiv.org/html/2605.01061v1)支持共同 basis 与 per-expert 粒度，未证明任意任务隔离；截断丢方向、warmup、统计/SVD/通信及空域耗尽均付费。共同 basis 不可信、新任务容量不足或完整质量回退时，保留独立 adapters/replay、较宽预算或普通更新。
`<!-- source-family:SF-2026-ARXIV-2605-01061 -->`

### 01158 / PLATFORM-COST / Ch70

实际32–84已有totalexperimentfamilycost，400后蒸馏ledger已有共享teacher分摊；差额不是“多计失败”重述，而是共享多branch生命周期、rollout/trainer闲置与计量→设施估算转换分责。拟在下列PRE标题前，成本等式之后：

PRE：`### Adaptation 不是单一路径，而是受预算约束的组合决策`

拟正文：后训练账本还应把共享阶段与分支费用分开：同一 pretraining/midtraining 可供多个 Think/Instruct 产物复用，不能各自重复计全额，也不能只报告最终成功分支而隐藏开发试验、数据生成与失败运行。在线 RL 则要把 rollout generator 与 trainer 分别计量；长回答使 trainer 等待时，低功率不表示整个训练便宜。[Olmo3 的生命周期账本](https://arxiv.org/html/2605.01158v1)给出这一反侧，但 generation 近似功率、实测 GPU 功率、IT multiplier/PUE 与碳水地域系数不是同一证据层，作者比例不应变成行业常数。测量窗口、共享分摊和估算假设增加维护成本；上游账本或系数不可得时逐项标 unknown，保留窄口径 final-run 与 marginal 成本，不拼出精确生命周期总数。`<!-- source-family:SF-2026-ARXIV-2605-01158 -->`

### 02108+02111 / MODEL-TRANSFORMER-LAYER / Ch17

actual267–310先推I+JF，再讲几何相干与NormJacobian；尚无谱chart/slack vs physicalmargin的两层证书。拟两项共用一段，放在下列PRE之前，紧接Residual解释、不覆盖04971：

PRE：`Residual 与非线性还承担两种不同的几何责任。Residual identity path 让相邻层的表示和梯度方向更容易保持相干；非线性则必须真正打破仅由坐标旋转造成的等价方向，网络才能沿深度形成新的可区分变换。因而“存在激活函数”并不充分：若非线性仍保持 rotation equivariance，它可以保留梯度传播，却未必打破所需对称性。`

拟正文：谱曲线也必须绑定这条真实 Jacobian 链，不能把 static weight 的奇异值拟合直接当 `I+J_F(x)` 的传播证书。一类条件分析分别需要归一化、power-law chart 误差、局部 transport budget 与 non-backtracking slack；near-identity scaling 只控制其中的 budget，不自动保证 chart 品质或整条谱路径。进一步从主导谱窗口谈物理 channel 结构，又须声明 transport 的行/列究竟是 physical coordinates 还是 source modes，固定 extraction/rank/support 规则，并核截断误差、core-overlap/noise 与各类 margin。后择排列的热图亮块和部分 checkpoint 测量不能替代完整证书。[谱坐标条件](https://arxiv.org/html/2605.02108v1)与[物理结构条件](https://arxiv.org/html/2605.02111v1)因此是两层不同权限，不是普遍训练稳定或机制因果。SVD、Jacobian/误差测量和规则敏感性均计费，条件不足时回到实际梯度、loss 与任务回归，保留原 residual/Norm 路径。`<!-- source-family:SF-2026-ARXIV-2605-02108; source-family:SF-2026-ARXIV-2605-02111 -->`

## A8 已保存事实与作者交DAY状态

root R4/R7实际独立POST通过后，作者只行政同步九章10条本人注（GSA一注两源，共11），并逐条actual读回，没有改采用正文或其它作者注。README六部分已融入补窗14源/14候选/必要证据；11整合、3争议终态保留、00941日期跨日隔离；状态仍进行中等root DAY。旧137/小时窗不变、旧§4整块连续，旧完成/复核明确历史。

2026-10-16T17:56:10+08:00实测：V3通过；原137行逐字、原§4连续逐字、原窗口原样保留，新14行；310本地引用/42唯一文件无缺失；本日README/SUP及9章限定diff-check通过。首次接口枚举/重复表头/冻结字段/H3结构问题已修，未改日期工具/校验器/合同或旧候选来passing。本日cached numstat为空；未stage/unstage/commit/push，不覆盖并发2025。

用户要求本批日期收口后checkpoint暂停；仅交本日DAY/完成态FINAL，不自跳日期/扩源/附件；共享LS/索引/checkpoint由root协调。
