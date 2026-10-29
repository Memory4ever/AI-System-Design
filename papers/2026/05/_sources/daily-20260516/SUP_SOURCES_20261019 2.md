# 2026-05-16 增量来源补查（唯一进度记录）

## A1 — 边界、原件与当前停点

作者：`may16_supp_author`；独立复核者及 Books 窄位协调：`root`。执行日2026-10-19；仅补北京时间2026-05-15完整自然日。用户明确要求保留旧归属、候选整行/评分/公开时间、原09:00小时窗及有效证据，不从Weekly反推。原1候选Charon、原连续§4冻结；本日前完整原件为[baseline](baseline-before-supplement-20261019.md)，实际由现稿原文经apply_patch保存。

已重读AGENTS、当前研究/Report合同、Prompt、ROADMAP、Sources每日及arXiv/恢复说明，LS仅采用134/279路由。按using-agent-skills与daily-research-closure分层复用，不把检索、候选、Source、Books或验收混同。现稿格式为写作基准；未取得可用个人风格检索工具，不宣称检索风格匹配。只改本日报、本日_sources及获协调Books窄位；不stage/commit/push。

原来源记录的arXiv零项依据采用created代理，不可作为本轮May15覆盖证据。原Charon为May16官方目录事件，保留旧归属，不计May15新增。

## A2 — 实际查询与有界查漏

- 官方月列表尝试 `https://arxiv.org/list/cs.CL/2605?skip=0&show=2000`、`cs.LG`同参数返回404；`cs.CL/2026-05?show=2000`超时。误开的pastweek只返回当前10月目录，不采用任何条目；已停，不扩Live。
- DataCite `query=prefix:10.48550 AND registered:[2026-05-14T16:00:00Z TO 2026-05-15T15:59:59Z]&page[size]=1000`返回截断非完整JSON，不作覆盖/零命中依据。单DOI API可访问，拟入选项逐一有限恢复真实原字段与公告日组合，不用created代替registered。
- 复用既有May15 created原始679身份目录仅作标题查漏（不作已落窗，也不逐项AB关闭）。在现有May metadata标题中检索language model/LLM/Transformer/Attention/reasoning/Agent/vision-language/World Model/diffusion/GPU/inference/pretrain/fine-tune/quantization/retrieval/MoE/kernel/foundation model/RL/multimodal/VLA，得250标题线索；这不是候选数或工作队列。原95冻结身份仅机械抽取相邻日baseline §3作同事件去重，其中55与标题线索重合，未读相邻日研究正文，不搬归属。
- 有界标题语义检查排开明确医学/科学/一般通信或统计方程应用，不把这些命中计候选；对相关或含糊者分批完整题摘并做具体贡献判断。
- 机构旧记录指出May15 08:00三项OpenAI与Seed UAM在原09:00起点外，本次分别核原始核心内容。OpenAI个人理财、Databricks、Academy三篇已实际打开；Seed目录 `?view_from=speech`给UAM May15、Charon May16；无全站历史扫描。

## A3 — 首批准入与代表性排除（待root校准）

**拟入：UAM, arXiv 2605.15735。** 已读官方完整题摘及当前版本栏。旧约束是同一VLM表征同时承担语义与低层控制造成fine-tuning干扰；原文新增并行Dorsal Expert、生成先验初始化和visual-dynamics中间目标，不冻结、不VL replay的action-only训练，因而需要重新比较冻结/replay与结构分离的保语义取舍。不是因VLA主题映射而收。日期候选依据是Seed目录2026-05-15；arXiv v1提交May15 08:45:37UTC只作 provenance，不作公开日期。当前v2 May18只显示修订，无已见撤回/纠错标记；必要全文/修订具体影响尚待，不先标深入完成。作者主页/项目线索另定点核更早正文。

**代表排除：**

- [个人理财产品](https://openai.com/index/personal-finance-chatgpt/)：读初始发布核心及privacy/evaluation说明，新增是连接账户、专属memory与专家评估的产品能力；未披露可复用新机制或足以改变既有memory/权限/评测选择的可比证据，79/82.5及50专家没有公开任务/预算对照足以支持新设计结论。后续6月/10月更新不计May15；不因为金融应用而一概排除，而是本篇实际增量不足。
- [Databricks](https://openai.com/index/databricks/)：读全部核心，50%/46%是OfficeQA Pro单协议表现和上架案例；扫描解析错误向后传播没有新的归因控制/机制或盲区证据，不能据宣传数进入候选。
- [Academy operations workflows](https://openai.com/academy/chatgpt-work/how-business-operations-teams-use-codex/)：核心是既有agent生成业务产物的教学用法，未提出执行机制、失效边界或系统新证据，分母前关闭。当前改名不当作May15技术修订。

以上排除不评分；无需为已明确不贡献的材料继续追精确小时或全文附件。arXiv首批五篇完整题摘原件在[calibration](SUP_ABSTRACT_CALIBRATION_20261019.json)，待作者逐项语义判断与root校准；其余来源尚普通未完成，未作终态或Coverage通过。

## A4 — 首批arXiv完整题摘具体判断

首批五篇由既有metadata恢复完整题摘，不将current摘要当v1逐字稿；拟采用证据转精确v1，修订只核实际影响。

- **13974 Massive Activations 拟入**：激活离群通道过去常作为数值异常/量化负担处理→文中对少数巨激活通道做破坏对照、空间聚类和跨prompt transport，提出其承担语义因果载体→改变DiT哪些通道可安全压缩/编辑的选择。暂拟2+2+3=7，需核零置干预是否只是整体幅度/随机同规模对照、分量输运边界，不先采普遍因果论。
- **14054 MoCA 拟入**：结果奖励无法辨别视觉提取还是逻辑错误→blindfolded reasoning proxy与structured verbal verification分离perception奖励，再做modality-aware credit→需要重新考虑给VLM统一reward还是分模态归因。暂拟2+2+3=7；必要证据为代理能否隔离reasoner能力、同预算对照与结构验证覆盖，不因题摘没细节关闭。
- **14194 GradShield 拟入**：看似良性SFT数据也可能破坏安全→逐样本Finetuning Implicit Harmfulness Score和adaptive threshold在微调前筛数据→需比较仅按内容过滤与按参数影响筛选。暂拟2+2+2=6；安全设计反证信号触发深入受影响域，ASR<6%不先采作安全保证。
- **14270 OSI 拟入**：文生图概念遗漏通常直接调注意力/提示→线性probe识别text-token遗漏信号并放大干预，评FLUX.1-dev/SD3.5-medium→要重新考虑文本表征里可检测信号与生成过程补偿的接口。暂拟2+1+2=5；需核probe目标泄漏、同预算/多概念干预与质量代价。
- **13850 Two-Dimensional Agent Patterns 未决初筛**：不是因taxonomy即排除。题摘声称两轴28 pattern、四领域描述覆盖和五条empirical selection laws；如果只是对现有经验的重新命名与未验证映射，则不足；若给出能修正具体设计条件的反证则继续。只定点看law建立依据与实例，不把整篇变深审。v1提交March16而MayID/Updated不提供May15公开证明；贡献可先判断，未作为确定候选。

以上四篇与UAM是首批拟入，不是全部候选；须root独立准入校准后展开必要Source；没有候选配额或固定保留率。剩余有界题名线索按具体主题语义处理，先不扩大全文投入。

## A5 — B1完整题摘语义判断（待独核）

[B1原件](SUP_ABSTRACT_B1_20261019.json)15项已逐项读完整题摘；仅作准入，不预支Source完成。

| 身份 | 旧约束→实际增量→改变判断 / 具体关闭理由 | 初筛 |
| --- | --- | --- |
|13909 TERMS-Bench|deal rate饱和掩盖策略失败→隐藏对手状态对agent不可见但对evaluator已知的Bayesian环境与oracle gap→从对打排名改为belief/cue/compliance可归因诊断；7分暂拟2+2+3|拟入|
|14028 Pix/Word|视觉encoder丢细节→pixel embedding/color folding/global conditional attention approximation→比较不用固定视觉encoder的离散表示；小模型非排除理由，scaling信念不采用；5分暂拟2+1+2|拟入|
|14047 ScalarNorm|同一scalar approximation难拟各层且需重训→GP异构逐层函数+posttraining realignment→比较全局reduction与逐层近似误差/访存；当前注释v2重跑GP/FLOP/knee，需核与v1所采域区别；7分暂拟2+2+3|拟入，修订信号必核|
|14068 CurveBench|视觉简单不意味着层级关系精确→完整containment-tree输出和复杂度分层呈现失败→可核是否确实暴露旧视觉问答不测的结构一致性；只新756图/低分不够；5分暂拟2+1+2|拟入，核评价增量|
|14084 CRANE|thinking checkpoint推理强却损tool格式→Thinking-Instruct delta经Taylor gate/格式关键方向投影→无训练合并应保哪种行为；7分暂拟2+2+3|拟入|
|14087 Toxicity replication|显式toxicity近满分不保证隐式鲁棒→同DExperts显式/隐式对照和10倍延迟报告→改变部署时把表面安全率当低代价鲁棒的判断；6分暂拟2+2+2，安全反证需深入相应域|拟入|
|14125 PolarProbe|关系是否只分散不可解释→距离/方向分别拟存在/类型，五域与新实体关系外推、结构规模退化→限制线性可读关系与模型实际推理能力的等同；7分暂拟2+2+3|拟入|
|14211 ASH|无label互联网视频难当动作监督→自身轨迹训练IDM再反推视频动作、卡住时自改进与keyframe记忆→改变长程agent依赖固定示范/奖励的选择；7分暂拟2+2+3|拟入|
|14340 ASR pseudo-audio|纯文本域适配缺声学上下文→speech-text alignment生成pseudo-audio prompts→比较只改LLM与跨模态prompt适配；5分暂拟2+1+2|拟入|
|14350 DRATS|多任务失衡不只梯度冲突→把交互分配写成worst return-gap minimax并自适应采难任务→改变固定均分interaction预算；7分暂拟2+2+3；MetaWorld非领域应用排除|拟入|
|14358 MinimalCore|长CoT不等于全部步骤必要→greedy删步与答案/分布保持、局部不可约和跨模型保留→区分解释trace冗余与实际因果计算；7分暂拟2+2+3|拟入|
|14359 RQ-MoE|输入依赖码本串行decode→two-level MoE+dual-stream分离instruction与quantization→改变向量压缩表达力与解码并行取舍；6分暂拟2+2+2|拟入|
|14366 SemanticRL|低资源SFT表面模仿伤通用能力→embedding semantic reward的GRPO对照→比较奖励空间与保留效应，不将藏语任务本身当贡献；6分暂拟2+1+3|拟入|
|14386 Darwin|固定架构逐参数平均限制合并→14维genome、layer diagnostic trust、heterogeneous mapper→核跨Transformer/Mamba何种可执行映射及搜索预算，排名不贡献；6分暂拟2+2+2|拟入|
|14398 ChronoAgentic|视频latent rollout无法强制接触约束→代码场景+deterministic物理check反复修复→显式物理状态替代纯视频生成的验证取舍；6分暂拟2+2+2；80已选demo/非等预算比较不支持普遍优越|拟入|

日期仅四首批DOI已拿到真实单条原件（SUP_DC_2605.{13974,14054,14194,14270}_20261019.json），其余逐项必要恢复尚普通；Source不在完成层。上述分数均对新增命题暂拟，最终若采用域收窄按实际命题解释，不以工作量或Books处置改分。

## A6 — root R2校准与13974必要Source / 逐字PRE

root已独立实读首批五题摘、UAM当前题摘/history与Seed目标页、三OpenAI核心，R2通过13974/14054/14194/14270/UAM的潜力准入和三OpenAI具体排除，13850仅定点law依据。13974/14054按目前局部采用命题调整为2+1+2=5，14270=5、14194=6/安全受影响深入保持；UAM初拟5但必须先核官方事件核心和精确版本资格。此校准只对应这些具名命题，不设全日5分或6分上限；A5其余数值仍暂拟，按本篇原文实际命题逐项判断，不复制统一分。

13974实际读取[exactv1](https://arxiv.org/html/2605.13974v1)§3.1–3.3/Eq1–5、§4.1/Table1、§4.2/Table2与AppendixD直接限制，current abs仅列July7 v2及project无具名纠错/撤回信号，不遍历版本史。日期原件[DC13974](SUP_DC_2605.13974_20261019.json)：v1 Submitted=2026-05-13T18:00:12Z，America/New_York当时EDT，after Wed14:00 cutoff故最早May15 00:00Z；client=arxiv.content/publisher arXiv/state=findable，同DOI registered=May15 02:01:12.000Z作最晚上界。完整可能区间May15北京时间08:00–10:01，同一自然日，未把registered当pub；未见具体更早正文线索。

**必要Source判断**：§3在每sample/layer/stream/token平均绝对值选top/bottom k，zero intervention同时施于所有层/步；这支持受测DiT对所选通道敏感，不能从等通道数而不等能量对照宣布已证明唯一semantic cause。空间实验1,600 GenAI-Bench prompts、BiRefNet伪分割、FLUX.2-klein、k=12，mIoU约0.5相对bottom约0.2；不是对象身份/part-level分割。transport用同initial noise的source/target，M=spatial mask×channel mask，只替换选中层坐标并全denoising steps使用；实际编辑选k=1024（SANA512），与诊断12不混同。3,515对来自703带scene属性的prompt再各配5对，是已选人口。Table1相对interpolation/无mask支持局部联合proxy取舍，但single prompt文本对齐更高，Table2 MAs相对TokenVerse多个CLIP-T退步（如FLUX1dev82.5→75.3），不能采“无损/全指标优越”。图像条件参考轨迹还需TokenVerse逐example MLP优化或native image condition，不是全流程无训练。AppendixD明确不解释稀疏通道何以产生、不识别其各自编码，mask只前景/背景且source生成错误会继承。未核代码、未复现，不采安全继承保证或墙钟省费；正文足够支持一条有边界内部控制接口，stop。

**实际owner/邻接**：已读当前Ch24内部guidance段（pooled modulation→frequency logits→共同timestep造成cosine混杂→DPP多样性），Ch23开篇representation contract与Ch25开篇observed/belief/imagined职责。唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`；不是Ch23重建量化机制，也不让Ch25接管普通生成内部控制。现稿已有“低幅度不可随便剪”的反侧，但尚未承载同种子双轨迹的channel×spatial transport、诊断/编辑k分离及重建轨迹费用，具体差额需深入并入原论证。拟2+1+2=5；必要Books接口已深入到上述关键反侧。

**逐字PRE（未获窄位，不写Books）：** 在Ch24现有以“检查 pooled 条件时，还须先分开语义 `y` 与共同 timestep `t`”开头、source-family2602-21596结尾的完整自然段之后，且在“对同一 prompt 联合生成多个视频时”自然段之前，增以下唯一自然段，其余不动：

> 通道诊断还可提供另一种内部控制接口，而不只判断哪些坐标能剪掉：在同一生成器、相同初始噪声的两条条件轨迹中，按层和stream选高统计量通道，再将源轨迹的坐标写入目标；图像stream另乘前景空间mask，保留其余激活。[受限DiT干预](https://arxiv.org/html/2605.13974v1)支持这种语义transport，但同数量通道的置零不等能量匹配的唯一因果证明，前景mask也不识别对象身份或part结构；诊断用的小k与实际编辑选取的更大k必须分开。中层与mask改善部分联合代理，文本对齐仍可能下降，源轨迹的错误也会继承。两条完整轨迹、激活驻留、选层/选k与mask均付费，图像参考还可能需要逐例重建优化，不能一概称全流程无训练。层坐标、条件、源质量或费用失配时，保留原prompt/CFG、已验收的显式mask编辑与独立输出验收，不由稀疏通道或局部替换签发精确概念解耦、像素不变或普遍省费。<!-- source-family:SF-2026-ARXIV-2605-13974 -->

拟本人Review note：`SF-2026-ARXIV-2605-13974` — Daily05-16补May15；exactv1§3.1–3.3/Eq1–5、§4/T1–2与AppendixD必要域，2+1+2=5/内部transport具体差额深入。保top/bottom能量混杂、k12/1024分责、mask粗粒度、CLIP-T反退/source错误继承和双轨迹/重建全费；不采唯一因果/精确解耦/全流程无训练或速度保证，未核实现/复现。等待root必要Source/owner/PRE独核及指定窄位，不预填POST。

## A7 — 14054必要Source与逐字PRE（待root）

14054实际读[exactv1](https://arxiv.org/html/2605.14054v1)§2.1–2.5、§3.1–3.3/T1–4、AppendixF1–2与必要限制；v1题名为Rewarding Perception for **Vision-Language** Reasoning，current摘要题名Multimodal不同，采用精确v1不静默混合。日期原件[DC14054](SUP_DC_2605.14054_20261019.json)同client/findable/身份规则，v1 May13 19:23:53Z、最早May15 00:00Z、registered May15 02:03:03Z，完整合界同北京May15；registered只是上界。

原文将recognition与think显式段落化，PV让Qwen2.5-Instruct14B在不读图时用question+识别文本回答；RO最终答案、RP该代理是否答对，R=RO+λRP后减同题group均值。这里式中没有除std，描述“normalized”不补全未给项。仅RO=0时按RP路由视觉token：RP1加αprotect|A|，RP0减αpunish|A|。RP不是真实感知标签，也不保证RO0的A必负，更不自动保advantage符号/共享参数隔离。SVV是语言模型按结构提示判断，不是确定性algorithmic execution；也不把gold answer持有的human sufficiency评价当无泄漏perception真值。

评价用Qwen2.5-VL7B、PV/OV同14B，T2同数据/底座局部消融支持视觉/文档部分收益，但full MMMU54.8低于outcomeonly55.3、MathVista73.8低于74.4；不能采所有能力无seesaw。Human test979、3标注majority，T3 false negative90/979=9.19%、FP44/979=4.49%；代理并非完美。关键反证是RP false-negative会落到“加强处罚”RP0分支，原文称protect正好缓解false negatives并不由式子推出；此robust归因主张**不采用并终态争议隔离**，不妨碍采用门控本身及其错误传播边界。T4 verbal verifier273 pairs、T0.7五次一致性92.3%不是deterministic；F1数据取自training+test不能当纯held-out。GPU、precision、全部训练steps/rollouts与端到端PV/SVV预算未完整披露，Not Disclosed，未核实现/复现。只采用有界proxy→token-routing接口，stop不遍历附录。

已读当前 `TRAIN-GRPO` Ch33置信分段→视觉伪certainty→PACE→suffixcredit的完整局部邻接及Ch32/34开篇；现有09529为mask/KL自报confidence而非image-blind外部solver的binary门，故这里有具体差额。只将信用路由机制与资格反侧写Ch33，不复制表征/平台章节。分数2+1+2=5，具体知识差额深入。

**逐字PRE**：Ch33以“信用落点另可仅在视觉描述段”开头、终至“不由自报置信替答案、policy或effect验收。”的完整自然段后，且“另一条 token 重权路径同时改变 teacher 的视觉与提示条件”之前，增加以下唯一段：

> 视觉信用还可由另一份image-blind求解读出来提议：让外部文本reasoner只读取问题与模型生成的视觉描述、不读取图像，以其能否答对提供二值代理，再与最终outcome reward组合；最终失败时，只对视觉描述tokens按该代理减弱或加强原group advantage。[受限模态门控](https://arxiv.org/html/2605.14054v1)改变的是proxy与信用落点，不把文本可解认证成真实感知充分，也不保证失败轨迹的组内advantage必负。代理false-negative可能反而触发加强处罚，不能由“保护”名称签发对oracle噪声的鲁棒；分段loss也不隔离共享参数。结构提示的LLM verifier仍会随机误判，有限同底座消融存在推理子任务反退，不能采所有能力同步改善。额外reasoner/verifier、完整rollout、parser与训练均付费；代理支持域、门控方向或真实质量不稳时，保留普通outcome信用、可信视觉标签或独立过程验证，不让更细路由自行拥有真实错误原因。<!-- source-family:SF-2026-ARXIV-2605-14054 -->

拟本人Review note：`SF-2026-ARXIV-2605-14054` — Daily05-16补May15；exactv1§2/T1–4/F1–2必要域，2+1+2=5/imageblind binary proxy→视觉token门差额深入。保无std式、RO0非必负、false-negative加强惩罚反证、SVV非确定、T2子任务退步/F1 train+test/全部额外费用；不采robust归因/全能力无损，未核实现/复现。待root必要Source/owner/PRE与窄位，未写POST。

## A8 — UAM原始对象恢复（尚未Source终态）

按root允许的具名同材料原件复用，只机械抽官方`get_article_list_v2`返回中ArticleMeta.ID=1625的唯一对象，保存[UAM1625](SUP_SEED_UAM1625_20261019.json)，不读取相邻日其他研究。PublishDate=1778774400000即May15北京00:00，官方完整题摘包含本轮采用的潜力机制、Author/ArticleID1782904319221/TitleKey及arxivPDF2605.15735身份；它支持官方目录公告日期和核心，不证明arxiv当日公开或当时已可下载全文。当前未带筛选首页HTML无UAM，`?view_from=speech`web投影列May15，属动态投影差异，非immutable快照。[官方detail](https://seed.bytedance.com/en/public_papers/uam-a-dual-stream-perspective-on-forgetting-in-vla-training)工具不可达，目录原始对象仍有正文摘要，不能冒称detail读完。arXiv exactv1已可访问，作为后续证据而非本窗arxiv命中；作者当前主页链接具名project，未提供更早公开日期，继续只核这一具体项目线索。

## A9 — 14194必要Source与逐字PRE（待root）

[GradShield exactv1](https://arxiv.org/html/2605.14194v1)已实读§3/Eq1–5/Alg1、§4/T1–5、A2–A7必要proxy/评价/失败；只看AppendixB假设与引理入口，不采完整理论等价/保证。当前v2 Jun5未见撤回/具名纠错信号；源current题摘只作信号，不覆盖v1。日期[DC14194](SUP_DC_2605.14194_20261019.json)client arxiv.content/findable/publisher arXiv，同唯一v1 May13 23:19:55Z，最早May15 00:00Z至registered May15 02:06:19Z，完整区间同北京May15。无具体更早稿线索，不扩历史。

FIHS理想定义是leave-one-out终局safety差，实做改为初始checkpoint的样本更新方向与一条held-out harmful prompt之可微safety proxy梯度内积；proxy=首token logit(I)-logit(Sure)，不是内容审核标签，更非所有潜在有害性的真值。Alg1先全数据微调/测safety，不过才打分筛后再微调；Gaussian/GMM猜阈值并按safety/utility放松界搜索，不是一次静态分类零训练成本。选择subset与每步更新保护应分开，不能把Ch29逐步投影当本篇实现。

评价主要Llama3.1-8B，utility1000+harmful100、LoRA r8 α32 batch8，explicit3epoch/1e-4、IDshift5epoch/3e-4，IDshift五seed；ASR在100 AdvBench上按无拒绝关键词计数，另GPT4.1 HS和100taskcase utility。T3部分utility低于nodefense或safeinstr；T4高污染90%第二轮ASR.25、A7 I-prefix仍.07，不能采用ASR恒<6%或完备safe guarantee。A4单probe对9probe平均相关.92只在500给定样本/10probe，非覆盖全部安全方向。A6 compromised reference失去可分性，明确不能修复已失守模型；§3.1还不考虑backdoor/cipher绕评价。缺全GPU/precision/端到端同预算cost，记Not Disclosed；未核实现/复现。采用是训练效应筛选接口与资格限定，而不是营销safe/binary-search全局收敛保证；safety命题受影响域已深入，stop。

已读 `TRAIN-DATA` Ch27“内容无害不等于更新无害”完整小节及前后跨语言过滤/derivedlabel，再核Ch29 safety-gradient SVD投影段确认职责差异。现Ch27 compliancevector projection并非FIHS的单probe更新内积与重训选阈值，因此具体差额放这里，不改Ch29。2+2+2=6：机制是筛选；Reach2来自数据接纳与实际微调/安全utility回路跨界，Durability2保持受限proxy不是安全基础定律。

**逐字PRE**：在Ch27现有source-family2606-00160独立注释之后、以“派生监督还可能把原本没有标签写权限的来源”开头段之前，增加唯一段：

> 预测训练效应也可使用梯度，而不是只在表示空间比较compliance方向：在初始checkpoint，取候选样本的loss梯度经optimizer映射后的方向，与安全probe可微分数的梯度作内积，再按safety与utility试训结果选择过滤阈值。[GradShield的受限分支](https://arxiv.org/html/2605.14194v1)实际用首token的拒答/顺从logit差作proxy，单probe和初态近似不能替代理想leave-one-out终局效应，也不等于trainer每步都投影安全冲突。初始模型必须仍有可信对齐；已失守reference会使筛选退化，backdoor与绕评价的cipher也不在其保证内。高污染、多轮过滤及起始词干预仍有有害输出，拒绝关键词ASR不认证真实安全，部分utility也会下降。梯度提取、首次试训、阈值搜索后的重训与独立安全检查均计费；probe、checkpoint或目标人口失配时，保留内容过滤、冻结小规模canary与独立red-team，不由低proxy分或找到阈值直接签收安全模型。<!-- source-family:SF-2026-ARXIV-2605-14194 -->

拟本人Review note：`SF-2026-ARXIV-2605-14194` — Daily05-16补May15；exactv1§3/Eq1–5/Alg1、§4/T1–5、A2–A7必要，2+2+2=6/safety受影响深入。保单probe初态/tokenproxy近似、Alg1试训重训费用、ASR关键词/90%污染.25与I-prefix.07、compromised reference失效、backdoor/cipher不覆盖和utility反侧；不采完备safety/总降费/完整理论保证，未核实现/复现。待root必要Source/owner/PRE与窄位，未预填POST。

## A10 — B2完整题摘判断（待root校准）

[B2原件](SUP_ABSTRACT_B2_20261019.json)15完整题摘已实际读（首次工具输出截断后已重读完整本地原件），没有把未读末项当筛完。暂拟分数只对应下列命题，证据层不先完成。

| 身份 | 原约束→增量→选择 / 关闭理由 | 初筛 |
| --- | --- | --- |
|14418 GreatPretender|单次ASR受生成/评价随机性影响→重复成功约束与CASgen/eval→改变攻击是否稳定可复用和跨文可比；2+2+2=6/安全反证深入|拟入|
|14443 PromptPolicies|冻结blackbox每次在线prompt搜索贵→小prompter经scalar+textcritique对比经验蒸馏→比较离线优化与serving单次prompt提案，需同worker/全部搜索预算；2+2+2=6|拟入|
|14448 TWN|全输入CoT贵且可误导embedding→双LoRA/接口detach+selfsupervised逐输入路由→比较共享底座/独立reasoner及查询按需生成；2+2+2=6|拟入|
|14450 Rerank|listwise长CoT边际收益→quality/token Pareto筛teacher轨迹自蒸馏→改变检索reranker预算选择，不把少token当墙钟；2+1+2=5|拟入|
|14461 ClickRemoval|用户click→selfattention调制实现无manualmask removal；需定点核心判断它是新控制条件/干预机制还是现有编辑算法软件封装，当前不因open-source或task收|初筛必要核心未决|
|14465 TABALIGN|planner与executor无cell grounding协议→maskedDLM binarycell计划与小verifier读attention overlap→比较planner的双向表示与任务执行验证；2+2+2=6，attention不是读取因果|拟入|
|14488 Deepchecks|完整题摘只有RAG评价、rootcause和monitoring的通用能力清单；没有新增判据、失败归因控制或实际机制/证据修正既有RAG评测选择。不是因为框架或厂商标签，而是实际所述增量不足|具体排除，不评分|
|14513 HEART|headmask跨step稳定/稀疏敏感度不同→QKdrift按head刷新+frequencyvelocityerror预算阈值→比较mask重算成本与误差预算，Wan/Hunyuan需实证约束；2+2+2=6|拟入|
|14517 IntentFidelity|holistic高分不等具体intent各维保留→结构promptablation/人评给出splitzone反例→改变只看总体对齐分的验收；2+2+2=6|拟入|
|14530 MaskPrior|diffusionVLM并行不免重复/视觉脱落→maskprior suppression+monotonicRoPE干预→比较unmask次序/位置偏置与grounding；2+1+2=5|拟入|
|14531 MantaLM|AR不可逆与diffusion成本→HJB控制视角+latentflow/globalintegraloperator→需核是否真改变architecture/控制律或只是重新命名；原摘要有具名模型机制潜力，2+1+2=5，不先采optimal理论|拟入|
|14535 GeographyPatching|完整extendedabstract只说用activationpatching研究relativegeographicspace，未说明发现或新probe/反证会改变何种解释；不因局部/extendedabstract排，而是未有具体可核贡献|具体排除，不评分|
|14549 CSLibPremise|结构图rerank应更好这一假定→strictimport/source-order人口、sourceproxy与Leanexpression对照及noRecall10收益→修正结构集中不等检索可用/证明依赖真值；2+2+2=6，负结果可入|拟入|
|14558 ActFocus|长think/短action同token权重→rewardvariance相关energy诊断、reasoningdownweight/actionuncertainty重分→比较action瓶颈下信用资源分配；2+2+2=6，不采无额外runtime|拟入|
|14561 PSAO|分句加humanreadableimportance注释，最优搜索方法尚future；需一次核心决定域核它是否有能修正intent/optcost的可比证据，而非仅提示加权的proofconcept；不从原prompt候选存在推出不退化|初筛必要核心未决|

本批实际15行：11拟入、2排除、2未决。日期/当前事件信号/必要Source尚普通；未展开待独校准项附件。

## A11 — 13974指定窄位实际保存，待root POST

root R3实际必要Source/日期/current/owner/邻接与A6逐字PRE通过后授Ch24指定21596完整段后→DPP前唯一段及本人注。作者已按批准稿实际保存该段与本人注，实际顺读完整两侧自然段，限定unstaged `git diff --check`通过；未写其他Books段、未stage/commit/push。尚待root非writer实际POST，不提前标生效或Books完成。

13850决定域一次核验已完成：exactv1§6.1–6.2/T5与§7.1只把四个业务场景的约束/选型示例重述为五law（例如seconds→Chain、volume→FanOut），未给计量实验、对照/反例或新执行机制，论文自己将贡献定位为两既有轴的命名组合。这个具体增量不足以修正既有选择，不因taxonomy名直接排除，但本篇**分母前排除**，不评分、不再追日期（v1 March提交/MayID不足May公开）；current题摘的27→28命名数量不构成重要修订，不采sandbox保证bounded damage等未证强说法。

## A12 — 14270必要Source与逐字PRE（待root）

[OSI exactv1](https://arxiv.org/html/2605.14270v1)实际读§3.1–3.2/§4/Eq5–7、§5/T2–6、§7限制及必要AppendixE1–2/F/T A2–5。日期[DC14270](SUP_DC_2605.14270_20261019.json)真实原字段按合证已实跑bounded May15；current仅acceptedICML/后续版本无具名纠错信号，未对全部版本重审。v1方法不是线上probe报警后才干预：离线以Mask2Former与BLIP-VQA一致的最终图像presence标签，四比一train/validation，保中间timesteps训练/选heads；均值absence减meanpresence得δ，按projectionstd缩放，向concepttoken的key作固定方向shift。头/时间窗预先选定，推理并非逐样本实时probe gate。

FLUX.1dev/SD3.5medium、30step、CFG3.5/7，top300/100heads、α5/7.5、前15step，object/attribute spans由规则或Llama3.1-8B提取。头的probe可读性不等唯一因果；early最终label不对齐，F以0.772/0.838 early/intermediate支持有限迁移但不能消灭分布shift。T4随机方向也部分改善（6object.30对base.18），Allheads在3object.74高于作者.71；不能说所选方向/heads全设置唯一最优。T2 SD3.5 nonspatial.3159低于TACA.3164，fiveobject.46低于.47；E A2 SD3.5质量与FLUX部分CompBench指标反退，A3只object干预使FLUX color.7678低于base.7923。§7明确overgeneration、二值label不覆盖美感/相对数量。离线probe训练、direction/层窗校准、span提取和全sampler有费用，不把backbone不微调当无训练/免费；GPU/precision/batch/concurrency/SLO与端到端费用Not Disclosed，不采production speed。关键反证已足，stop。

实际Ch24/Ch23/25邻接复用A6有效层；另完整读Ch24 pooledmodulation两段→frequencylogit两段。现稿没有固定offline omission direction→concept-key/timewindow的接口；与13974同章不同机制，前者跨source轨迹transport，OSI是offline统计方向，不能合并为一算法。2+1+2=5，具体接口差额深入。

**逐字PRE**：Ch24以“全局 modulation 不保证语义解耦”开头并以source-family2602-09268结尾完整自然段之后、以“条件读取内部还可以选择不同的干预坐标”开头段之前，增唯一段：

> 条件坐标也可以由离线遗漏诊断来选，而不直接改全局modulation：以最终生成图像的二值presence标签，在中间去噪状态训练probe/选head，再取“遗漏均值−存在均值”的归一方向，按尺度写入目标词的key。[受限OSI对照](https://arxiv.org/html/2605.14270v1)在预选head和早期时间窗固定施加该shift，不是每步由probe确认缺失后才触发。最终标签与早期状态可能失配，probe可读不证明唯一语义因果；随机方向也有局部收益，全部heads和其他方法在部分设置更好。更强干预可过生成，部分画质/属性指标仍退步，二值label也不覆盖主观美感或相对数量。Probe训练、方向与时间窗校准、目标span提取和完整采样均付费；标签、key接口或质量不可靠时，保留原条件、较保守guidance与独立内容核验，不由无需微调backbone签发全流程无训练、无损或普遍省费。<!-- source-family:SF-2026-ARXIV-2605-14270 -->

拟本人Review note：`SF-2026-ARXIV-2605-14270` — Daily05-16补May15；exactv1§3–5/Eq5–7/T2–6/§7与E/F必要，2+1+2=5/offline direction→concept-key固定窗接口差额深入。保离线probe非online gate、early标签shift、random/Allhead与基线反侧、overgeneration/画质反退及训练/校准/span全费；不采唯一因果/全流程免训练/无损/生产速度，未核实现/复现。待root必要Source/owner/PRE及窄位，未预填POST。

## A13 — B3完整题摘具体判断（待root校准）

[B3原件](SUP_ABSTRACT_B3_20261019.json)15项完整题摘已实际读。本批不由应用标签定生死，逐项新增命题如下。

| 身份 | 原约束→实际增量→改变选择 / 关闭理由 | 初筛 |
| --- | --- | --- |
|14563 MemDocAgent|依赖遍历+共享RepoMemory read/write/verify，摘要未说明verify权威/一致性不变量；需一次决定域核是否超出常规依赖排序与共享上下文组合，任务均分本身不够|必要核心未决|
|14581 VisualAggregation|单向量省存储但可能丢数字变动→只改single-digit诊断/patch对照识别texturedominance→改变visualRAG是否可安全pool至单向量；2+2+2=6|拟入|
|14598 DSSP|短观测不能解历史歧义→SSM压全历史并以dynamicsaux训练+近期观察分层condition→比较持续状态与短窗actionpolicy，2+2+2=6|拟入|
|14619 SliceGraph|finalanswer ensemble合并丢过程差异→activation稀疏Jaccard互kNN+BCC+blindedannotation/matchednull→区分同答案多策略与重复抽样，2+1+2=5|拟入|
|14634 RustPrint|函数级迁移丢架构intent→源码文档blueprint、输出文档差异+翻译tests修复→比较显式中间artifact与直接迁移；2+2+2=6，翻译test不自动独立|拟入|
|14635 MultiEmo|单candidate emotion标注可误评多情绪输出→20annotator分布标签+dominant/distribution对照与judge不足→修正主观多label evaluation人口；2+1+2=5|拟入|
|14664 MiVE|统一VLM只末层丢空间细节→分层VLM特征送unifiedselfattnDiT→比较语义/空间condition深度，2+1+2=5，不从unified宣称无modalitygap|拟入|
|14686 ReMIA|读完整摘要：对象为tabular synthetic generator的两次训练relative-source分类隐私度量，未给foundation/语言/多模态训练或系统的新机制/理论连接；仅可类比本书privacy不足，非因小模型硬排|范围排除，不评分|
|14696 EponaV2|只nextframe监督不等规划scene足够→预测可decode几何/语义未来表示+flowGRPO→比较WM辅助预测目标与planning；2+2+2=6|拟入|
|14704 SceneFunRI|可见证据以外的functionalobject定位→完整场景转不可见region任务/三类prompt，潜在暴露observation不足条件；需核唯一位置label是否从图像可辨/不确定性和旧任务何处失效，仅新855例低分不够|必要核心未决|
|14709 InterleavedVisualReasoner|统一理解/生成不等复杂指令可操作→按complexity/capability选直接/反思/计划并stepreward/complexitypenalty→比较固定reasoning策略与按需路径；2+2+2=6|拟入|
|14712 IntentVLA|当前obs相似对应多意图跨chunk反复抽样→近期historyintent压缩+matchedaliasbench→比较短时latentintent持续与framepolicy；2+2+2=6|拟入|
|14742 EARL|粗交互理解未进querygrounding→globaldescriptor经AFS融合+多输出reward→比较先理解再ground的表示接口，2+1+2=5；不按egocentric应用排|拟入|
|14749 NonlinearIntervention|线性steering遗漏非线性特征→generalintervention及无直接输出signature的learningprocedure→重新考虑拒答feature坐标/线性假定，2+1+2=5/安全受影响深入|拟入|
|14766 StreamingSpeechLLM|整句等待或固定间隔不是真动态streaming→学习读够音频才emit与自动alignment训练→比较显式wait/emit决策与固定时钟；2+2+2=6|拟入|

本批12潜力、2核心未决、1范围排除；日期/当前事件信号尚未处理，不能当12确定候选。Source只展开已经过root具名校准的首批，不因题名列表宽而扩大为全量AB/全文队列。

## A14 — 14054指定窄位保存；14194符号差额PRE

rootR4完成14054必要Source/日期/Ch33局部与A7逐字PRE独核并授指定段后→PACE前单段及本人注。作者已按批准稿实际保存正文和本人注，限定diff-check通过，待root非writer实际POST，不预填生效。

14194按rootR4唯一符号修，A9逐字PRE第一句由“拟更新方向”改为“取候选样本的loss梯度经optimizer映射后的方向，与安全probe可微分数的梯度作内积，再按safety与utility试训结果选择过滤阈值”；其余逐字不变，未写Ch27，等待root读这一精确差额后授窄位，不重做已有效Source。

## A15 — root R5既成POST与B2校准

rootR5已实际非writer读13974真实新增、完整上下邻及本人注，POST通过，计本日1项真实整合、Ch24该窄位释放。作者仅将本人注待POST文字同步为此既成事实，正文未改，不授DAY。B2 11具名潜力与2具体排除通过，14461/14561各只一次决定准入core；14549负结果有效，14531只架构/control命题而非HJB最优。后续逐项评分，不因批次沿用统一6。

## A16 — root R6既成POST；14194实际保存

14054真实新增、完整直接两侧及本人注已rootR6实际POST通过，计本日第2实际整合、Ch33窄位释放，作者仅行政同步本人注，无正文再写。14194的A14唯一符号差额已rootR6实读通过，授Ch27 00160独立marker后→派生监督前唯一段+本人注；作者已按批准原文实际保存并读回，限定diff-check通过，待root实际非writer POST，不预支第3整合或DAY。

## A17 — 14270实际保存与B3准入校准

rootR7实读14270必要Source/日期/当前说明、Ch24具体邻接及A12逐字PRE，已授09268第二完整段后→frequency首段前唯一自然段与本人注。作者按批准原文实际保存并顺读两侧，限定diff-check通过，待真实非writer POST。B3十五完整题摘独核通过12潜力/14686具体范围排除；14563/14704只各一次决定域core，不把未决直接入候选或深审队列。

## A18 — 当前发现停止范围，不把宽池改成逐项工作量

root R8已实际逐项读14194/14270真实新增、完整实质前后段与本人注，POST均通过；本日目前4项实际整合，窄位全释放。作者只同步两条本人注行政文字，正文未改，尚未DAY。

arXiv发现的唯一宽库存仍是A2的679身份；250是主题关键词命中标题，减机械同事件重合55为195个标题线索，不是195候选或逐项AB/Source债务。已实际完整题摘读五篇首批与B1–B4各15，共65个身份，其中四批分别止于14398、14561、14766、14938；本轮65中13850已决定域关闭，首四Source/Books通过，其余按各批准入或一次core停点继续。标题库存尚余约130个未送AB身份，它们不被写成“已审排除”或重复。本次只对与语言/多模态基础模型、训练/推理、具身与Agent执行机制直接相关、或标题含糊的新命名线索继续有界题名补检；一般领域预测、医学/科学、通信与传统推荐/控制的明确标题不自动产生逐项摘要/全文任务。尚未完成这次剩余题名补检，所以当前也不授arXiv覆盖完成。后续记录具体选中身份与停止点，不能以库存全部清空为结束条件，也不能把已有潜力材料改称终态以省事。

机构停止范围：OpenAI只May15三具名核心已关闭；Anthropic只May15北京01:06的2028-ai-leadership官方政策说明核心（政策情景/算力地缘，未提出本书机制），待代表性排除复核。Seed只目标May15 UAM同对象及当前有限目录投影，不扫历史；Google/Meta/Qwen/DeepSeek/Moonshot/Hunyuan/MiMo/MiniMax当前官方入口的历史May15切片仍普通未收口，现有首页/空响应不作零命中。Zai与ERNIE已见日期夹界需要在最后14行给足自包含停止位置。不会补扫每周来源。已成功curl官方cs.CL五月月表（1,660,176字节）补充标题入口，但月表没有日段标题，不单靠它确定May15日期；此前web超时保留，不改写为所有通路失败。

## A19 — B4完整题摘的本人具体判断

[B4完整原件](SUP_ABSTRACT_B4_20261019.json)十五项逐一完整读，压缩恢复后已再次完整读回。root R9已实读题摘作潜力校准；不是把全部相关主题自动送深审，也不沿用统一分数。

| 身份 | 旧约束→实际增量→选择 / 决定域 | 初筛 |
| --- | --- | --- |
|14771 MediaClaw|三层抽象/插件/Skills组合本身未指出新执行语义，核心若有兼容性/隔离/状态可靠性实证才可能改变平台设计；只一次决定域核，不因平台名收|核心未决|
|14787 CIR|高检索分被当组合能力→单模态捷径与human well-formed人口审计→需要把跨模态依赖与任务有效性分开验收；2+2+2=6|拟入|
|14801 VLN瓶颈|像素精度被当闭环质量方向→planner语义/fast坐标两子系统统计SR界与感知饱和→比较不同感知预算，不外推通用上界；2+2+2=6|拟入|
|14802 ARPM|检索拼装不自动新机制；CSV自动54%/人工100%有可能揭示判别器盲区，也可能只是手工宽松规则，需一次核心看标注规范/相同人口，不凭治理术语收|核心未决|
|14830 HumanLoop|人工接管被当质量恢复→随机现场整体处理与不同失败类型/介入时机的异质结果→限制以时长下降或有人接管签收agent质量；2+2+2=6，类型/时机非自动随机因果|拟入|
|14841 GPart|低维映射再接双线性LoRA破坏等距→直接全权重isometric分区映射→改变PEFT参数化几何/存储与更新执行取舍；2+1+2=5，随机子空间假设不作无损定律|拟入|
|14853 DIG|完整题摘实际是推荐item SID/user-item cross feature/ranker联合优化，未提出对当前语言/多模态基础模型、RAG或训练推理主线直接的新机制/理论；不因仅有tokenizer词引入通用推荐研究|范围排除，不评分|
|14876 CLVR|生成规划未核验且多步昂贵→step验证/代理history奖励与alignment delta和蒸馏prior merge→分别核信用来源与4NFE取舍，不能用多组件总分证明每一归因；2+2+2=6|拟入|
|14892 LIFE|声称formal依赖可能有可检验新条件，但四阶段taxonomy/agenda本身不够；只一次核心核形式依赖是否超出定义重写，不因survey类型直接排|核心未决|
|14893 CLIP spectrum|低方差/共同谱不等噪声→跨subgroup协方差谱与剪维downstream对照→修正所有共享维度都应保留的假定，只采受测任务/人口，不把164普遍化；2+1+2=5|拟入|
|14907 KGPFN|局部NBFNet+全局relation实例/PFN可能只是KG组合，也可能实际扩展结构上下文ICL→一次方法core核何种可迁移学习机制/假设，不从foundation标签自动纳|核心未决|
|14908 SteerSeg|文本attention未为定位优化→learnable softprompt/属性CoT→点prompt/tracklet筛选接口→比较冻结backbone与可训输入的grounding；2+1+2=5，不叫全流程免训|拟入|
|14913 RPAttention|固定空间proxy限定交流→表征相似竞争路由Gather–Interact–Distribute→比较空间与内容压缩的线性成本/低秩瓶颈；2+1+2=5|拟入|
|14928 CoP|新过程QA/检索分解流程本身不够，需一次core看控制不同粒度/信息可得性的反例和模块归因；不能因六模型13%或能映射RAG收|核心未决|
|14938 Octopus|历史梯度/重放需存旧数据→history-free梯度正交与两阶段task/regularizer→比较无旧样本时稳定—可塑性条件；2+1+2=5，是否真无需旧梯度/统计须核|拟入|

九潜力、五一次核心未决、一范围排除；各项日期/Source未预支完成。分数是目前具体拟采命题，只有新证据才调整，不按批次/数量改。

## A20 — UAM必要Source复用、实际owner与逐字PRE

采用事件是[Seed官方对象1625](SUP_SEED_UAM1625_20261019.json)的May15公告及完整核心，不是May15 arXiv命中。arXiv exactv1提交May15 08:45:37Z不当pub；[exactv1](https://arxiv.org/html/2605.15735v1)作为后到机制验证，current v2 May18未见具名纠错/撤回信号，不遍历全部版本。官方project当前页无可核更早日期，具名repo API返回Not Found，不以第三方May1列表替更早全文证据；无继续无限排除假想渠道。root R9已独立实读同一官方唯一对象与必要v1，Source有效层复用，不再恢复API/detail。

作者实际必要v1§3.1–3.3、§4/T2、§5、§6/7/T3、§8.1–8.3与§11/12/T4：semantic/dorsal/action三expert并行MoT attention，ViT与VAE视觉流分别进入前两者。Dorsal继承BAGEL生成先验，同时学future-frame visual-dynamics辅助目标；action-only指无需额外VL replay，并非不用预训练先验/未来frame监督。无冻结、无stop-gradient、共同attention不保证独立梯度屏障。gen-only变体未支配VLM-init，生成初始化加辅助目标才改善，不能只归因额外容量或只归因初始化；六variant先按action指标选winner，只有winner进full retention，不能用它证明每个结构变体都保语义。Qwen/PaliGemma vs BAGEL的预训练/参数配套不同；早期遗忘对照也换action-head MLP/MoT。T2 UAM相对BAGEL在MMMU55.3→53.7、MathVista73.1→68.2等下降，平均>95%不等每指标/任意能力；layer14/28平均attention分工不是因果阻断证据。

3k ALOHA轨迹/30kstep/8A800、Calvin D/1000长度5与RoboTwin16个hard任务子集不能混为完整机器人覆盖；实机各类型20随机trial不认证安全。推理使用单denoise step中间表示而非完整未来图重建，但7+7+2B的UAM1500ms慢于7+2B Qwen1300ms，更慢于2.3+.3B基线250ms；所谓相同GPU配置未披露实际servingGPU/precision/batch，不把训练8A800当inference配置。不得采零费/普遍实时。未核实现/复现，受限机制及关键反证已足，stop。

实际owner为`MULTIMODAL-EMBODIED-VLA` Ch26。已完整读“Action-facing Representation也是Gradient Authority Boundary”含冻结parallel branch/GuidedVLA/variational与pose bottleneck段；另实际读“从只学Action到同时保存语义并对齐语言与动作”三个完整段至后继PRTS/INR-DOM。前者已有冻结隔离，后者已有teacher anchor+同obs语言动作对齐及teacher费，尚没有生成Dorsal先验+未来帧辅助训练这条不冻结分支；不能按同主题报已有覆盖。Ch25只拥有真正transition/imagined state，本文仅取辅助动作表征，不把它宣告可控WM；Ch27的数据配比也不接管并行视觉流机制。2+1+2=5，具体保语义替代接口缺口深入。

**逐字PRE，未写Books**：Ch26以“代价是额外 Teacher forward、显存与训练时延”开头、终至“语义保持比精确同观测对齐更重要的场景。”的完整自然段后，且“同一语言goal可以对应一条示教中许多不同进度”之前，增唯一自然段：

> 不依靠冻结Teacher或额外语言回放时，另一分支把动作需要的空间与动力学压力交给并行视觉expert：继承视觉生成先验，并以轨迹未来帧作辅助目标，再与semantic/action experts共同attention。[受限UAM对照](https://arxiv.org/html/2605.15735v1)中，仅生成初始化并未支配VLM初始化，需要把先验与辅助目标合看；共同attention和观察到的分工也不构成独立梯度隔离。结构搜索后只将action表现最好的变体带入完整语义评价，部分语义指标仍下降，不由平均保持率签发所有能力无损。部署可消费单步中间表示而不重建整张未来图，但额外expert、预训练先验、未来帧监督及训练推理都付费，受测大模型延迟仍高于其较小基线。它提供动作适配的一条表征分工选择，不取代可信teacher、冻结分支、replay或窄域BC；先验、embodiment或实时预算失配时保留这些较简单分支，物理执行仍由fresh observation、controller与safety envelope验收。<!-- source-family:SF-2026-ARXIV-2605-15735 -->

拟本人Review note：`SF-2026-ARXIV-2605-15735` — Daily05-16补May15官方Seed1625公告，不作arxiv May15；后到exactv1§3/4/T2、§8/11–12必要域，2+1+2=5/生成Dorsal+未来帧辅助的具体替代接口深入。保无梯度隔离、gen-only非优、winner-only retention、底座/配套混杂、语义退步、实机小样本及16B/1500vs1300ms反侧；不采95%普遍保持/attention因果/零费/实时安全，未核实现/复现。待root actual owner/精确PRE与窄位，Source R9有效层复用，未预填POST。

## A21 — UAM实际保存、进行态README与日期恢复停点

root已实际通过A20 actual owner/逐字PRE，并待相邻日Ch26两导航真实POST释放后，授teacher费用段后→PRTS前唯一段及本人注。作者按批准稿实际保存两处，顺读完整两侧，待root真实POST，不预支第5整合。README已保存补充窗口/用户授权/进行中及旧§1/2/5/6历史边界，冻结候选日期字段引用实际baseline；原小时窗、Charon整行与连续旧§4不动。

单DOI原件现已恢复14068/14084/14087/14125/14211/14340/14350/14358/14359/14366/14386/14398及14418/14443/14448/14450/14465/14513/14517/14530/14531/14549/14558；每个保存本日`SUP_DC_2605.ID_20261019.json`，仅删除巨型xml编码，原日期/client/state等字段保留。全部实际唯一v1在May13 18Z之后至May14 08:33Z，真实registered在May15 02:03–02:14Z、arxiv.content/findable，按日程完整可能区间同北京May15；后续本地脚本复算，不能将registered改名pub。

13909真实uniquev1 May13 06:22:50Z，最早May14 00Z而registered May15 01:59:37Z，组合跨北京May14–15，不硬赋May15。已实际读abs/current（只Jun13v2无具名纠错）、必要v1核心入口；题摘潜力不因日期失效，后续只恢复这一具体身份官方日期。14028/14047已本地组合bounded May15，current均只v2；14047 current明确GP/FLOP/knee重跑，正读v1与v2受影响方法/评价，不把后修订数值提前归May15。

## A22 — 剩余130题名的一次有界补检及B5具体判断

实际仅机械重取A2那250主题标题，扣原95的55重合与本日已完整题摘65，得到130个尚未送AB身份；已一次按标题顺读13872至15198，不读取整679摘要。明确领域应用/非主线标题包括phylogenetic tree、kilonova、diamond sensor、clinical EEG、drug interaction、crystal/materials、通信波束/信道、降水、一般PDE/金融时间序列任务等，不将其当泛foundation/Agent机制。标题含糊或与主线新命名/可靠性机制可能直接相关者继续选取完整题摘，本次先恢复下面15项，不是剩130逐项队列。仍需后段具名标题题摘与一轮非固定关键词的主题标题查漏，不宣称发现收口。

[B5原件](SUP_ABSTRACT_B5_20261019.json)十五完整题摘实际读：

| 身份 | 旧约束→增量→判断 / 决定域 | 初筛 |
| --- | --- | --- |
|13872 S-AI-Recursive|递归推理停止仅残差不足→coupled state/双信号收敛条件与deceptive plateau对照→可能改变停止资格；当前有revised framework信号，先一次决定core看是否直接可迁移学习/推理机制而非为自定义fixedpoint命名|核心未决|
|13900 PopulationCoordination|完整题摘为供应链容量控制的population-conditioned primal/dual surrogate，无foundation/语言/多模态训练推理或Agent执行机制直接连接；只可类比AI资源调度不足|范围排除，不评分|
|13989 VectraYX|小模型低perplexity被当更好会话/工具能力→paired seed corpus-register inversion与replay/tool密度控制→改变按loss或容量硬推工具能力；2+2+2=6，current v3具体新增需与v1资格分清，不因42M/西语领域排|拟入|
|14040 Physics-R1|表面5gram去污/MCQ分数被当视觉推理→semantic候选审计/配对翻译/格式梯度→修正LLM训练评价盲区；2+2+2=6，只采通用评价控制，不采物理领域发现，需root校准Science边界|拟入待边界校准|
|14057 DualDialogue|两级policy/问句生成可能只是hierarchicalRL常规组合，摘要没给新协调条件；一次核心决定域核，与法律应用指标分开|核心未决|
|14097 Facilitation|用户偏好/更信过程不等协作有效→两组人实验的共识未改/分配受引导/参与公平未改→限制只采主观反馈签收agent协作；2+2+2=6|拟入|
|14141 SolverHint|重复分布可先验专门化但易过拟合→sample-consistent solver的correctness/runtime有限library条件及LLM compile loop→改变agent搜索与部署代码验收；2+2+2=6，必要时核理论不借成熟PAC作本文基础突破|拟入|
|14201 MAPLE|单轨迹BC不呈现其他agent反应→VLA latent多agent reactive rollout与分级reward→比较外模拟器/潜在闭环训练；2+2+2=6/安全受影响，不将latent真实兑现|拟入|
|14205 SimPersona|手写persona不匹配行为人口→clickstream VQVAE类型映射agent词表token并按merchant分布采样→比较文本角色与学得populationconditioned policy；2+1+2=5，不以conversionalignment替全行为真实性|拟入|
|14259 HEAR|nary规则与procedural hyperedge可能新增工具权限，但stratified ontology/loop名称不够；一次核心看auditable execution具体合同，94.7%不单独准入|核心未决|
|14306 PaSaMaster|生成引用易虚构→verified-paper candidates上ranking/证据回馈更新intent与plan/retrieve分工→比较引用身份守恒和意图自改，2+2+2=6，零hallucination只对候选身份非相关性真值|拟入|
|14322 TeachArena|正确回答/工具call不等持久干预兑现→matched observable turn/trajectory/persistentstate三表面评价→可能揭示判断与effect不一致；一次core核是否有此受控反证而非新354任务/低分|核心未决|
|14355 Herculean|四金融MCP workflow与长程低分目前只主题/任务扩展，需一次core核stateconsistency/verification控制与可归因失败；不因金融标签排，也不凭MCP直接纳|核心未决|
|14389 Nexus|完整题摘主要把已有macro/micro/context多agent分解用于房价/股票预测，未披露模型机制或控制归因/适用边界的新证据；“forecasting是agentic问题”仅领域结果不够，非因小改进/负面排|贡献排除，不评分|
|14396 MIRAGE|像素防御被当映射robust→保roadtopology的diffusion语义变异与mapping/planning攻击→改变防御支持域；2+2+2=6/安全受影响，双VLM realism与模拟trajectory不认证真实道路等价|拟入|

本批八潜力（含14040边界待校准）、五一次核心未决、两具体排除，尚未日期/Source完成；先交root实际准入后再展开必要域。此前A21共30个DC原件已全部本地脚本实际复算：29同日bounded May15、仅13909跨日，结果与原字段一致；脚本不是日期原件或独核替代。

## A23 — 14047精确版本差额、Source与逐字PRE

[v1](https://arxiv.org/html/2605.14047v1)实际读§2.1–2.3/Eq1–4、§3.1–3.3/T1–2/F4、§4；[v2](https://arxiv.org/html/2605.14047v2)只比较具名GP/FLOP/knee、重训评价与相应限制。当前官方abs已轻查到v3 Sep4，说明仅扩ViT-L和refined hardware motivation；不采用这份窗外新增结果或为证明无标记遍历附录。v1 May13 19:08:55Z与[DC原字段](SUP_DC_2605.14047_20261019.json)May15 02:02:53Z registered联合限定北京May15；不把v2 Aug11或v3 Sep4作为本窗新事件。

v1从已有ViT-B每层50k激活点/90:10拟合pre-affine scalar map，25层独立NSGA-II（500×50代、五seed、常数每次10步），node-count复杂度/最终bestvalidation；再继承原affine，affine-only/full/full+logit蒸馏回训20epoch，分别搜超参，不是checkpoint无损drop-in。±2maxtrain输入的pull-to-zero软罚只约束两个anchor，不保证全域有界；逐元素函数也不恢复原输入相关均值/方差，低MSE不等LN恒等。v1 GP-D84.25低于同训LN84.94，GP-A82.78低于DyT-A82.99，全文明确单ViT-B/ImageNet、局部拟合未涵盖跨层/域迁移。v1 FP32/197×768的FLOP/readbytes模型中GP约3.79×LN算术、memory约半，不是实际kernel/latency；未披露生产batch/concurrency/SLO，未核实现/复现。

v2实改FLOP复杂度+knee选点/学习率schedule并重跑后得到GP84.32及算术低于LN，不能提前倒填成v1同时少算少访存；它未推翻“逐层近似+回训”这份局部接口。源层关键反侧已足，root独立必要域核验同意只窄采接口，停止无关附件。按实际命题2+1+2=5，不把旧LN原则、NLP外推或可联想跨层计本文7分；具体gap仍深入。

实际owner `MODEL-TRANSFORMER-LAYER` Ch17，已实读“归一化控制什么”与“不计算归一化，也要控制信号与导数的深度传播”的逐元素饱和/APJN/容量约束/TaperNorm完整段，及Ch16/18开篇交接。现稿有从scratch初始化/固定饱和函数与常数冻结，没有从已有checkpoint逐层symbolic fit后继承affine再对齐这条接口；不是Ch49量化产物或Ch54kernel实现。拟在Ch17以“[受限初始化分析]”开头、终至“而不是凭匹配一个 APJN 数字就认定二者等价。”完整段后，且“有界 activation 还会在 regularization 与容量瓶颈之间换位。”前增唯一段。

**逐字PRE，未写Books：**

> 若从已有checkpoint撤去Norm，另一条局部分支先收集每层激活，将原pre-affine映射拟合成逐层标量表达式，再继承原affine参数并做短程对齐训练。[受限symbolic替代](https://arxiv.org/html/2605.14047v1)避免每token重新计算跨特征统计，却不使标量函数等价于输入相关的均值/方差；在两个尾部anchor加软罚也不保证全域有界。拟合误差与节点数只是搜索代理，不能替真实任务和算子成本：部分affine-only结果弱于固定函数，完整回训仍低于同训LN，v1减少读取却增加估算算术，未测实际kernel净时延。逐层搜索、激活采样、全网或teacher蒸馏回训与新指令表达式均付费；现有单视觉架构/数据的结果不授NLP或现成checkpoint直接替换。域、数值、真实质量或总费用不合适时，保留原Norm/成熟固定函数及对应训练配方，不从局部MSE或解析流量签发无损与生产提速。<!-- source-family:SF-2026-ARXIV-2605-14047 -->

拟本人Review note：`SF-2026-ARXIV-2605-14047` — Daily05-16补May15；exactv1§2–4/Eq1–4/T1–2/F4，v2只GP/FLOP/knee/重跑受影响域，currentv3只轻查扩ViT-L/硬件动机，不提前采用窗外结果。2+1+2=5/逐层scalarfit→继承affine→再对齐gap深入。保软罚非全域界、非LN恒等、node非FLOP/跨层与单架构局限、同训LN/affine-only反侧及搜索/回训全费；无实际kernel runtime/实现复现。待root actual owner/PRE与窄位，已核Source层复用，不预填POST。

## A24 — 14028必要Source与拟仅报告（待root）

[exactv1](https://arxiv.org/html/2605.14028v1)实际读§3.1–3.4全部机制和§4–5/T1–2/F3/6；currentabs仅Jun4v2，无具名纠错/撤回信号。v1May13 18:38:51Z、[DC](SUP_DC_2605.14028_20261019.json)registeredMay15 02:02:27Z/arxiv.content/findable共同限定北京May15，非registered实际pub。

机制是RGB整数联合查表（折叠后4096颜色+pad）、每16×16窗causal decoder后仅取末token送统一栈，图像目标只预测下一窗首pixel；“统一pixel+word”只披露构造，实验实际120M/image-only，100k llava-cc3m训练/1k验证、224输入、fold16、window16、batch2/AdamW6e-4，只给loss曲线，没有mixed image-text、细字/OCR、语义质量或同预算encoder对照。GPU/precision/steps与端到端性能Not Disclosed。整数表的raw RGB可逆性不延伸到`RGB//16`，作者自己F3承认fold16失真；“ViT patch无可训练参数”“allfeatures变动必坏”不是受控反证，不采用这些中心强归因/无损/scaling或可替生产CLIP结论，保留争议边界。局部可执行架构proposal仍有贡献，不改判分母前排除或因缺实验降分。

本篇2+1+2=5/标准必要域已足。拟仅报告：实际增量是新的表/窗口摘要接口proposal，但本篇只证明局部image-only目标可优化，未披露mixed接口的有效性或支持替换当前预训练encoder的评价；不把全局approx等式当保语义证明。已读Ch23连续编码/统一tensor不等语义/codec损失与局部pooling部分以及Ch24现有AR factorization，旧文真实已有“输入可逆≠消费者充分、compression有损需按任务验收”，但不能以这些一般覆盖声称新表/下一窗首像素机制已存在。本次不为这份尚无消费者/设计选择证据的proposal在Books罗列架构；保留Report中的具体构造与重要反证。若root认为窄接口本身已值得长期承载，可按同Source定位Ch23，不为工作量否定其新意；当前尚未获该Books决定复核。

## A25 — B6完整题摘的具体准入判断

[B6原件](SUP_ABSTRACT_B6_20261019.json)15完整题摘已实际逐一读；这是A22已界定标题线索的下一组，没有扩大679库存为全文任务。

| 身份 | 具体原约束→增量→选择 / 关闭理由 | 初筛 |
| --- | --- | --- |
|14401 MARS|event/preference/profile与六operation可只是memory常规组合；一次core看belief evidence/strength和自适应调度是否有新的可靠性/失效条件，不因26%rec指标纳|核心未决|
|14431 FuzzAgent|迭代runtime feedback/多人分工本身常见；一次core看如何区分harness-induced crash与librarybug、状态跨campaign继承，不能以102bugs或全生命周期直接纳|核心未决|
|14434 CQ-SID/EG-GRPO|推荐检索本身不自动入；一次core只看groundtruth injection在group update的具体接口/稀疏reward修正，若仅领域SID指标则不能凭GRPO标签纳|核心未决|
|14464 RAM|完整题摘为多表tuple属性文档/图连接与预测模型，没有foundation/语言/多模态模型或其系统的直接新机制；通用图检索类比不够|范围排除，不评分|
|14475 GeoVista|单zoom轨迹漏看/重复计数→global plan+branch inspection/显式跨区evidence state与scale-invariant坐标→改变视觉agent观察覆盖/去重；2+2+2=6，只采活跃观察机制非遥感领域发现|拟入|
|14495 ContestableDebate|现有A-QBAF加provenance/多agent可能只是流程组合；一次core看selective clash与uncertainty escalation是否实际改变决议权限/语义，不因透明/editable称谓纳|核心未决|
|14497 ROAD|静态offline/online mixing错配当前policy→bilevel performance目标与bandit surrogate→比较数据来源调度而非固定mix；2+1+2=5，理论代理与真实Qlearning须分开|拟入|
|14504 LongAct|DAG/memory/Critic组合与新长任务本身不足；一次core核goalcompletion59%与fulltask16%的失效归因、低层抽象是否真正控制，不将低分当增量|核心未决|
|14537 CattleTrade|长game/新动作组合本身不足；一次core看trace与spending coherence关系是否超出相关性排名/新task，若有稳定resource-discipline反证再纳|核心未决|
|14544 Complacent|完整题摘只争论sycophancy应改名complacency与教育确认偏差建议，没有新机制/可检验定义、对照或可修正系统设计的证据；非因position类型排，而是实际增量止于重新命名|贡献排除，不评分|
|14556 TeachAnything|完整题摘只有三stage多模态demo/云众包/模拟平台能力，没有具体新表征/监督/执行约束或可比较证据；“Symmetrical Reality趋势”不产生新机制|贡献排除，不评分|
|14587 PlasticityBackdoor|维持plasticity不等安全→干预×backdoor的系统对照与梯度放大/路径压缩诊断→需要重新验SAM等优化干预安全支持；2+2+2=6/安全受影响，不把losssharpness直接当检测器|拟入|
|14599 IRLFastRates|reward恢复需要覆盖/可识别条件→Borel有限horizon entropy MinMaxIRL–MLE等价与linearclass Hessian误差/trajectoryKL快率→改变偏好/示范推reward的样本与identifiability判断；2+2+3=7，长期价值来自明确统计/可识别边界，不借已有IRL原则；须深入实际定理条件|拟入|
|14604 EduFrameTrap|抗context-switch不等抗authority/facepressure→压力类型对照与两judge分歧→修正把单jailbreak分数当抵御迎合的安全证据；2+1+2=5/安全受影响|拟入|
|14625 DTsync|完整题摘是无线感知/移动/上行网络联合分配、matchinggame/连续优化，无大模型机制、训练推理或agent执行新语义；只称agentic/mobileAI不足，非泛VLA排除|范围排除，不评分|

五潜力、六一次core、四具体关闭；日期和Source未完成，未因评分/处置先写候选终表。14599暂拟7由实际统计命题触发深入，余项并无统一5或6。

## A26 — 两个既成层同步

UAM root R12实际POST通过，真实5I/Ch26窄位释放；作者只行政同步本人注。14047 root R13实读Source/actual owner/A23逐字PRE通过授窄位，作者已按批准稿实际保存Ch17唯一段和本人注，顺读完整两侧，限定diff-check通过，待root真实POST。14028 root R14实际独读必要v1机制/评价/日期，A24的5分/标准完成/仅报告通过：保留proposal及直接反证，不伪称已有覆盖，不因缺实验分母前排除；重开只需对应mixed/消费者及受控质量费用证据。README目前仍进行中，不授DAY。

## A27 — 14087决定域与受影响安全Source（待root）

[exactv1](https://arxiv.org/html/2605.14087v1)实际读§3–6全部方法/评价/失败及当前abs；current只有May15提交v2、无具名纠错说明，版本号本身不自动全读新版。日期[原件](SUP_DC_2605.14087_20261019.json)uniquev1May13 20:12:30Z，真实registeredMay15 02:03:49Z/arxiv.content/findable，组合完整落北京May15。一次决定core后仍保其跨显式/隐式评测的具体反证潜力，不因复现或GPT2小模型排；2+2+2=6，安全中心主张已深入受影响证据。

实做GPT2-small117M、DExperts原expert/anti-expert不重训、alpha1.5/top-p.9/T1/repetition1.2。RealToxicityPrompts只20newtokens，ToxiGen30；两组都仅Perspective API阈值.5，没有独立人审/implicit gold。作者未给实际每组样本数/分片index、seed原值、GPU型号/precision/batch、同步/热身、CI和完整质量评价，只有“标准GPU”和全数据总数；不能用99,442或274k当本次N。0→1.5%只是该proxy/长度/人口混杂下的报告，不能推出隐式hate真实漏率或100%安全。2s→3.2s与token20→30同时变化，固定DExperts算法也无困难时多搜索安全候选机制，故“困难输入更努力计算仍失败”的新double-penalty归因不成立；三模型0.2→2s也缺硬件执行条件，不作通用10×代价。

拟保候选并将中心鲁棒/延迟结论记争议/暂缓，不入Books、不授正面安全或性能证据：缺少匹配长度/人口与独立implicit标签、明确N和同运行配置，现有正文无法定量修复；不是普通未读Source债务。重开只要作者原分片/种子和配置、匹配20/30长度对照及独立implicit人工/多评估器证据，不要求不存在的代码复现来阻塞其他材料。一般“proxy不等安全/预算可比”早已在Ch66和安全owner承载，不能把这份不可归因的新结果塞Books或冒称新机制已被覆盖。最终准入与此争议终态需root独核，当前未获通过。

## A28 — 14366必要Source、actual owner与逐字PRE

[exactv1](https://arxiv.org/html/2605.14366v1)实际§3–5/Eq1–4/T1–5，A训练配置与C/T6受影响遗忘解释已读；current仅v1与ACL Findings说明，无具名纠错。日期[DC](SUP_DC_2605.14366_20261019.json)uniquev1May14 04:47:22Z、registeredMay15 02:10:21Z/arxiv.content/findable共同限定北京May15。

先5k/2epoch coldstart，再CINO/XLMR双语对比适配的冻结句encoder给generated/reference cosine，超过tau后线性rescale，另按Unicode/script给0/1奖励；最终1.5*semantic+1*language是**加和而非硬门**，mixed-language仍可得正甚至较高reward，脚本相同也非真实语言/意义保证。GRPO/coldstart不能凭名称签无遗忘。Qwen3-4B/LoRAr64alpha128/drop.05/BF16/batch32；strongSFT3epoch lr2e-5/1024–2048，RL1epoch lr5e-7/max256/每题8rollout，合总数据但长度/更新预算不齐，不能将差额唯一归objective。T1/2比coldstart还增加约90k/15k数据，非纯RL奖励归因。T3 MT的BLEU/embedding/LLMjudge均SFT更高，HG CMRC-F1 RL65.20低于SFT65.30；C的RLmeanKL .0410还高于SFT .0404，meanNLL仍高于base，不能采无alignmenttax/普遍保能力。T5同RL条件的reward消融支持组合接口局部有用，但自动相似/单GPT5.2judge不等独立人类真值；无human、未报完整seed/CI、GPU型号和全训练/encoder费用。不披露KL系数/完整实际优化器式，不以GRPO通用论补出，未核实现/复现。关键反侧足，stop。

实际唯一owner为TRAIN-RLHF Ch31的反馈来源接口，不是Ch33新的group公式或Ch29通用遗忘原则。已完整读Ch31“RLHF、RLAIF与Verifiable Reward”从三源区别到RLVRR、privileged language judge完整邻接，Ch30/32开篇；现稿有规则、judge与表面匹配反侧，没有冻结双语sentence embedding阈值reward加script附分这份提案。2+1+2=5：具体局部reward接口，原先Durability3的暂拟不成立于本文未经证明的无遗忘基础论；实际gap与错误hard-constraint/保能力断言受影响深入，不为省事降审阅。

**逐字PRE，未写Books**：在Ch31“但稳定问题相同：reward 是否代表真实目标”开头至“不证明 reasoning process 可靠。”完整段后，且“规则反馈还可以先由模型离线构造”段前增唯一段：

> 参考文本还可以提供连续语义代理，而不要求逐词复现：先适配并冻结双语句encoder，按生成与reference的cosine经阈值重标度给reward，再另加目标script一致性的二值分。[受限低资源适配](https://arxiv.org/html/2605.14366v1)支持比较这份反馈与词面目标，但相加的script奖励不是禁止混语的硬门，embedding接近也不认证完整含义。Coldstart、较小更新和rollout长度都会影响遗忘，不能把与SFT的差额唯一归奖励；翻译语义/偏好及部分原能力指标仍有反侧，较小OOD漂移也非零alignment tax。句encoder适配、reference、每题多次rollout、训练与独立能力回归均计费；语言、语义或保能力支持失配时，保留可信示范、显式语言校验与独立任务评价，不由cosine、Unicode或GRPO名称签发语义正确、语言硬约束或通用知识保持。<!-- source-family:SF-2026-ARXIV-2605-14366 -->

拟本人注：SF-2026-ARXIV-2605-14366 — exactv1§3–5/Eq1–4/T1–5/A/C/T6，2+1+2=5/reward接口gap与hard-constraint/遗忘反证深入。保加法非gate、数据/lr/epoch/长度混杂、MT/HG反侧、meanKL/NLL非零遗忘、自动评价与encoder/rollout全费，未核实现/复现。待root必要Source/actual owner/PRE和窄位，不预填POST。

## A29 — 14068必要Source与actual Ch66局部PRE

[exactv1](https://arxiv.org/html/2605.14068v1)实际§3–7/T1–3：756手绘非交Jordan曲线，Easy300按210/45/45，Hard其余456；GT由OpenCV contour extraction再人工核验，输出rooted unordered tree，以递归子树排序canonicalization匹配，不把兄弟序/节点编号当错误。Nodecount和全tree两项分开，RL30/70混合；Easy每样本4rollout、Hard1，不能跨协议混排名。Qwen3VL8Bthinking/Gemma3-12B、LoRAr4alpha8、250steps/batch128/8samples/lr8e-5、8RTXPRO6000；precision与全预算Not Disclosed。Qwen thinking常在8192未终答，截断不是已确定缺视觉拓扑；Easy同分布训后提高而Hard weak/maze反退，count不是树结构，精确match也不区分近错/parsefailed，作者明限合成闭曲线不授自然场景。OpenCV100%与生成GT同pipeline，非独立证明无歧义；有人工核验但不把它变唯一因果。未核代码/复现，机制/评价/关键反证足，stop。日期[DC](SUP_DC_2605.14068_20261019.json)May13 19:46:22Z→最早May15 00Z→registeredMay15 02:03:22Z，完整北京May15；current仅May15晚UTCv2/无具名纠错，保exactv1不提前用后事件。

实际owner PLATFORM-EVALUATION-SYSTEM Ch66，已读受约束顺序重建与NL-to-DSL结构比较及完整相邻AJ-Bench/solver-neighborhood段，Ch65/67开篇交接。现有primitive set匹配防序列误拒，却没有视觉包含层级的unordered-tree canonicalization、count/fulltree/parse与budget censor分账。拟2+1+2=5/具体结构测量gap深入，不因新756图/低排名而入。

**逐字PRE，未写Books**：在Ch66“输出是自然语言而评价对象是结构关系时”GeoDPO完整段后，且“如果原问题缺少可用的正确性 oracle”前增唯一段：

> 视觉结构的gold也可先限定为不相交闭曲线诱导的包含层级，而不要求识别对象：将输出解析为有根无序树，递归排序子树后匹配同构，避免兄弟顺序或节点编号制造假错。[受限CurveBench诊断](https://arxiv.org/html/2605.14068v1)要求把节点计数、完整层级、解析失败与未在预算内终答分开；count正确不等tree正确，精确match失败也不说明每条关系都错。Gold由contour pipeline再人工核过，同pipeline的满分不构成独立无歧义证明；Easy多rollout与Hard单rollout、只训简单域及长思考截断也限制跨组归因。受控闭曲线支持结构诊断，不授自然图像或任意拓扑理解；制图、标注、canonicalizer、训练和完整生成均付费。边界歧义、parser或预算失配时保留显式结构标签、细粒度关系诊断与独立核验，不让低总分、合成确定性或局部RL收益替通用视觉能力签字。<!-- source-family:SF-2026-ARXIV-2605-14068 -->

拟本人注：SF-2026-ARXIV-2605-14068 — exactv1§3–7/T1–3，2+1+2=5/全树结构测量gap深入。保同构不等自然grounding、count/tree/parse/censor分账、gold同OpenCV循环、Easy/Hard rollout/训练域与maze反侧、合成局限和全费，未核实现/复现。待root必要Source/actual owner/PRE与窄位，不预填POST。


## A30 — root R15–16实际结果

14047真实新增/完整前后段/本人注已root R15实际POST通过，计6I、Ch17窄位释放，作者只行政同步本人注。14087必要安全Source/日期与实际混杂已root R16独核通过，6分中心争议/noBooks终态可行；采用边界与匹配长度/人口、校准judge、实际费用重开条件按A27保留，不反删候选或评分，不授正面鲁棒证据。B6在A25的14475/14599/14604潜力及四关闭通过，14497/14587进一步仅各一次贡献决定core，不能因RL/SAM/security词泛收传统控制经验；其余六一次core维持。不授DAY。

## A31 — 机构新增实际停止位置

- Hunyuan按Sources要求在动态网页实际浏览器首查[Research全部](https://hunyuan.tencent.com/research?page=1)，完整all list11条，从Sep22到Feb3、无分页，目标相邻为May21 Hy-MT2与Apr30 context。May15无注册列表条目，当前有界列表已检查；不是用空HTML推零，不扫其历年repo。
- Qwen旧站新站迁移后，实际浏览器首页→研究索引→全部，地址[research index](https://qwen.ai/research#research_research_index)。初5条加3次“加载更多”共20条，May19 Qwen3.5-LiveTranslate与Apr30 Qwen-Scope夹May15后停止；排序默认倒序，全部包含Research/Open-Source/Release。先前web0行仅解析限制，已被实际动态列表替代，不宣称整站历史永久完整。
- MiniMax实读当前[英文研究](https://www.minimax.io/blog)完整12条索引，May26 sparse-token-forgetting与Mar18 M2.7夹界，May27后条只定日期不读窗外正文；无分页或May15条目。中文与Agent入口仍只有限必要对照，不能由英文镜像代替未见独占内容。
- MiMo实读[当前主页](https://mimo.xiaomi.com/)Paper8条，Jun29 MOPD→Mar13 ARL-Tangram夹界，无May15论文目录条目；Blog15项无日期并有More，仍需定点恢复Blog时段，Paper夹界不覆盖Blog。外部搜索DeepSeek官方docs May15/2026May无返回，只辅助检索受限，未当nohit。

## A32 — B7完整题摘具体判断

[B7原件](SUP_ABSTRACT_B7_20261019.json)17完整题摘实际读，额外14524/15082只因学习理论标题含糊而定点补，不将kernel一词当范围外或自动准入。

| 身份 | 具体原约束→增量→选择 / 决定域 | 初筛 |
| --- | --- | --- |
|14524 ProductKRR|saturation/multipledescent仅球面内积核已知→product kernel家族广化与sourcecondition收敛率→修正把现象只归球面/特定谱假设的解释；先一次核心核对通用学习主线的具体可迁移条件，不仅凭theory标签纳|核心未决|
|14661 FluidAntenna|完整摘要仅用LLM优化GA/crossover/mutation或生成为该通信问题的heuristic，没有agent/模型新机制或可修正自动编程一般条件的证据；近优SINR领域数不够|贡献/范围排除，不评分|
|14665 FalkorIRAC|图path支持候选+VerifierAgent可能只是GraphRAG组合，51判例proofconcept/无vector对照；一次core核path validity是否机械权威/未知路径与拒绝条件，而非verified名义纳|核心未决|
|14700 SRPlatform|9service+CAD脚本/缓存/telemetry本身常规组合；一次core核physicallyvalid authority和611“成功call”人口/失败收据是否新可靠性条件，50s不准入|核心未决|
|14754 XDomainBench|完整摘要明确20科学领域/AI4S交互知识组合工作流，没有独立于该暂缓路线的新模型/执行机制；不通过通用Evaluation owner重引AI4S研究|范围排除，不评分；边界待root|
|14758 RNNProVe|粗hiddenstate包络可不可判→policy-driven feasible hidden采样+统计行为violations界→比较历史状态feasibility与概率保证；先一次核心核样本误差界是否直接可迁移recurrent模型验证，不因RNN/RL泛收控制领域|核心未决|
|14779 CPQL|单step conservativevalue可能过悲观→离线轨迹multi-step PQL fixedpoint/behaviorregularization界→可能改变学习理论与offline初始化；先一次core核新优化/有效条件而非仅D4RL经验，保最优/behavior保证假设|核心未决|
|14809 GFMate|sourceprompt纠缠预训+只fewshot→预训后centroid/layerprompt+目标unlabelled complementary learning→一次core核可迁移的testtime学习新条件，不从graphfoundation名义直接纳|核心未决|
|14838 MCMT|weakVMR多proposal/Gaussianmask和双向query重建未关联当前基础VLM/生成模型机制，既有任务模块组合只给2benchmark指标，没有新表征/优化有效性边界|贡献/范围排除，不评分|
|14845 SignatureVLM|低randomforgery错误不等近似skillforgery→静态kinematics编码与CoT合理化反例→一次core核成对同模型/提示和不可能观测的速度推断，若有受控blindspot而非新生物识别任务可入|核心未决|
|14851 IFPV|完整摘要为具体战场tactical多平台行动规划/对抗压制效能与成本改进，无独立通用模型/agent执行新机制；不开展军事战术系统研究或通过通用WM类比纳入|范围排除，不评分|
|14857 HSWorkflow|固定六stage/可解释引用只是常规workflow；226分歧人工audit可能实际暴露goldpriority冲突，需一次core核具体规则/裁决资格，不从frontieragreement当正确率|核心未决|
|14866 RCLAgent|trace每span dedicatedagent/递归parallel可能只是微服务诊断流程组合；一次core看上下文分解是否保global证据一致性/失败归因与公平费用，不因RCA系统应用纳|核心未决|
|14890 TokenizerLegal|fertility影响成本是已知原则，但fewshot下降的stratified/prompt消融与跨时域非对称可能新反证；一次core核matched实例/示例/长度，current v2新增cross-temporal不能倒填v1|核心未决|
|14894 SEDiT|局部编辑不当然单step足够→localizedOT/velocity Lipschitz条件+cleanfirstframe/chunkstream→比较一步采样资格与时域漂移；2+1+2=5，须核Lipschitz是否真足以一步exact且infinite length非无界可靠|拟入|
|14897 VoronoiDistill|行为L2不等value保留→critic低值区增局部linearcell→一次core核通用蒸馏新分配机制/收敛条件，非只控制任务更可解释曲线|核心未决|
|15082 AGOP|预测误差大不表示未学有用subspace→KRR gradient outer-product在更低样本量恢复multi-index centralspace条件→区分prediction与representation的样本门槛；2+1+3=6/基础有效性差额深入，不将kernel理论硬排或假定实际深网因果|拟入|

本批2明确潜力、11一次core、4具体关闭；14851不展开作战内容，14754不展开暂缓AI4S附件。其余core只读决定准入条件，不预排整篇Deep队列。

## A33 — B8完整题摘具体判断与发现规模

[B8原件](SUP_ABSTRACT_B8_20261019.json)21完整题摘已实际逐一读，包括为避免新命名/小模型/负结果误排而定点补读14761/14846/14855/15015/15016；不是按题目有LLM就纳。

| 身份 | 具体原约束→增量→选择 / 决定域 | 初筛 |
| --- | --- | --- |
|14761 AestheticsInterview|interview+DL/LLM预测aesthetics本身应用组合；较自身复测误差更小可能是label时态混杂，需一次core核相同人口/时点与split，不能由“胜人”直接纳或反向嘲讽排|核心未决|
|14846 TransformerMPC|对attention作DC表示并SCP带feasibility保证可能是可迁移神经模型验证/优化机制，也可能只MPC重写；一次core核具体假设和控制外的直接适用性，不因小控制实例排|核心未决|
|14855 MovementForecast|完整摘要仅NBA运动预测上LSTM/GNN/Transformer历史与context的局部比较，未提供新模型/可迁移理论或控制混杂的反证；1.51m与noonebest不够，非因小模型领域标签排|贡献/范围排除，不评分|
|14950 EvoDepth|RGB几何增强通常依赖大几何先验/新sensor→轻implicitdepth+modulation/渐进actionalignment→比较几何输入与VLA表示成本，2+1+2=5，不从.9B推出零成本|拟入|
|14966 MHSA|attention异常可检测不等可修复→三层MLP在discriminator/自监督下替crossmodalattention→比较可训读取控制与freeze底座；2+1+2=5，纠正attention不是视觉真值|拟入|
|14988 CVG|冻结generator组合失误不一定要重训→attentionfeatures上训练compositionalclassifier、早步梯度改latent→比较内部诊断与生成控制接口；2+1+2=5，不以freeze称全流程trainingfree|拟入|
|15000 PrematureClosure|有答案的QA分数不检无可答状态→删除正确option与开放任务falseaction/澄清拒答评价→修正“不答”能力测量；2+1+2=5/安全受影响，只核模型不确定性/任务构造，不采医学诊断建议|拟入|
|15012 FEST|困难RLVR正样本稀→少量随机demo的supervised/onpolicy信号与衰减SFT权重→比较多epoch复用/过拟合与引导；2+2+2=6，不以128宣称全预算低|拟入|
|15015 SLMTeammates|小/大模型答题均分不够，judge对专家的系统性不一致可能有效反证；一次core核matched rubric/标注与judge可靠性，不因为教育场景或SLM硬排|核心未决|
|15016 COTCAgent|完整题摘是EHR统计代码+症状趋势知识库打分+询问的医疗应用组合，没有probabilistic completion的新推断/执行合同或独立混杂控制；90%/70%诊断分数不能立一般机制，非因medical词排|贡献排除，不评分|
|15019 GranuRAG|全图检索与局部query/视点可见性失配→elementfirstclass检索/跨粒度对齐/attribution约束→改变partialobservation证据身份；2+2+2=6，不把物体detector当真标签|拟入|
|15026 TuxBot|快慢loop+typedvalidation本身常见，badregion移除坏设置后仍退化可能新增statefulrollback有效条件；一次core看具体跨旋钮/时序控制证据，不因OS应用或LLM标签收|核心未决|
|15040 Orchard|平台标签不贡献，但creditSFT/BAR稀疏RL、historyexperience→valuererank是具名训练接口；2+2+2=6，分别核机制和sandbox状态/预算，不能由K8s复用或SOTA总分证明每一归因|拟入|
|15044 SpeakerLLM|scalar verification不提供证据组织→utterance/frame层speaker tokenizer与profile/condition/decision监督分责→比较音频身份特征读取接口；2+1+2=5，不授认证/授权或trace忠实|拟入|
|15055 DiffusionOPD|多task联合/串联RL相互干扰→student-ownrollout多teacher distill与连续Markov每步KL/meanmatch理论→比较探索和整合职责及梯度方差；2+2+3=7暂拟，重点核SDE/ODE KL资格与deterministic奇异性，不借一般KD原则计分|拟入|
|15071 TABVLM|新历史文化600QA/低准确不直接贡献；一次core核temporalinappropriate错误的匹配对照/图像可识别性，而非新任务/模型规模无关的宣传|核心未决|
|15104 TextToVoice|文本toolgold不能未经检查搬音频→配对TTS/声线噪声保schema并定位argumentvalue失误→改变语音toolcalling测量身份；2+2+2=6，不以judge间80%一致当human正确或privacy保证|拟入|
|15131 NaturalSynthesis|代码可通过checker不等自然请求规格正确→LRM与modelchecker soundfeedback迭代/autoformalization→比较执行oracle和规格翻译两层可靠性；2+2+2=6，不从个例参数化成功推解决不可判定问题|拟入|
|15133 ContinuousCausalPFN|连续处理prior与transformer元学习可能只把PFN用于新统计任务；一次core核prior/ICL的新可迁移机制/边界，不从foundation或Bayesian名义自动纳|核心未决|
|15187 Articraft|DSL/SDK/tests/sandbox及structuredfeedback可能是应用harness常规组合；一次core核几何joint/asset验证新不变量与失效条件，10k资产不是增量依据|核心未决|
|15198 ATLAS|外工具contextswitch贵、latent操作难AR训练→功能词表token兼代理操作/内隐视觉单元及静态anchor辅助GRPO→比较离散操作接口/信用稀疏；2+2+2=6，不由可命名token授真实可解释操作或无架构费用|拟入|

本批12潜力、7一次core、2具体关闭，仍未日期/Source完成；初筛层累计实际完整题摘133身份（5+15×6+17+21），UAM另官方同对象。余62个关键词标题线索止于A22的一次题名检查，明确的领域/科学/纯数理标题不自动产生摘要债务；不把62冒称全部语义审过或重复。尚需一轮非固定关键词的本窗主题/官方分类相关标题有界查漏，以及普通机构切片收口；之后冻结真正落窗候选，不把raw679或133题摘数当新增论文/候选数。

## A34 — 14366/14068实际保存

root R17已实际读两篇必要exactv1/直接反证、真实DC日期、actual owner+相邻交接及完整A28/29逐字PRE，授Ch31稳定问题后→RLVRR前/Ch66GeoDPO后→solver-neighborhood前唯一自然段及各本人注。作者已按批准稿实际保存、顺读完整直接两侧，限定diff-check过，待root逐项真实POST，不预支第7/8整合或DAY。

## A35 — 既成层与有限决定域同步

root R18实际14366/14068完整新增/直接两侧/本人注POST通过，累计8I，两窄位释放；作者已只同步本人注的行政状态，不重写机制。R19实际B8完整题摘校准通过，但潜力仍非日期/Source完成。R20对14665/Falkor、14700/SRPlatform、15187/Articraft各仅一次决定准入core的具体证据可复用：14665的领域schema/既知graph validation与两次拒答，10query仅3complete、1有citation，没有新的通用执行条件或受控反证；14700四阶段cache/CAD/layout/MJCF与queue，611成功call和估计latency没有分离新机制/成立条件；15187领域SDK、单文件、只读docs与QC沿已有SWE-interface原则，整套资源/URDF比较未隔离接口或预算，QC漏全局运动属任务实现边界，不改一般判断。作者据这些具体增量边界确认三项贡献排除、不评分，未从冻结候选删项，也不把topic/新资产直接当贡献。15071/15133决定域由root定点独读中，作者不重复展开。

## A36 — GPart必要Source、真实owner与逐字PRE（未写）

[exactv1](https://arxiv.org/html/2605.14841v1)实际§3–6/Eq5–12/Prop1、T1–3、§5.4与直接相关E/T6–8实现/费用读足；当前abs有Oct1v2/Oct2v3、没有具名撤回/纠错说明，版本号不自动重审全篇，当前abstract的composition前景不倒填v1。日期[原DC](SUP_DC_2605.14841_20261019.json)唯一v1May14 13:46:04Z、arxiv.content/findable、registeredMay15 02:21:46Z与公告日程共同限北京May15，日期工具实际复算bounded；不是created代pub。

以seed排列所有选定可适配参数，分为d个非空不交组，P每个参数所在列为1/sqrt(n_j)，其余零；PᵀP=I，直接Δw=Pθ、θ零初始化，链式梯度Pᵀ∇w。这是固定受限image(P)中的Euclidean等距，非任意全空间更新可表达、loss凸/更平或质量无损；同组可跨层共享一个坐标，不能与BA低秩几何/随机scaffold混同。局部30×30三方向loss图不是平坦极小值因果证明。RoBERTa/GLUE三seed、视觉五seed及0.5–8B数学；GPart/UniLoRA匹配d23k但其他LoRA预算不齐，视觉部分baseline抄既有论文而非同次重跑。GLUE若干Qnli/MRPC、Gemma数学和LlamaMATH/Qwen7BGSM仍有反侧，不采全面支配。

E实披单H10080GB、AdamW、独立θ/head LR搜索、target_modules/head另存，GLUEbase batch32/max512/25–160epoch/d23040，math batch2/accum8/2epoch/max2048/qkvo与d131k–524k，视觉20epoch/query-value/d72k或144k。精度未披，不宣称服务SLO；自定义autograd避免物化P仍需分组index/scale、重构与dense执行，不规则访问使wallclock约比UniLoRA**慢10%**。d向量+seed只讲紧凑adapter表示，不含base、head、PRNG/参数次序身份、索引buffer和完整执行成本。无代码核验/复现，机制/评价/关键反证足即停。

实际owner TRAIN-LORA/Ch30，完整读低维训练/固定A、随机scaffold、objective与rank邻接，另读Ch29/31交接。已有BA固定basis、结构绑定梯度及后压缩，不等直接在全选定参数上固定正交partition；拟最小差额只承载这一替代参数化与等距资格。2+1+2=5：重要局部参数化、单训练组件、稳定可复用约束，不借等距数学原则本身加Durability3；具体gap/宣传反侧深入已足。

**逐字PRE**：Ch30“同样，LoRA 也可以承载 DPO 或其他 objective…”完整自然段后，`## Rank 与 target modules 决定更新空间`前唯一自然段：

> 低维更新不一定还要经过低秩乘积：可按固定seed把选定权重坐标分成互不重叠的组，每组用同一个可训练坐标、按组大小平方根归一化，直接写成`Δw=Pθ`。此时`PᵀP=I`，梯度按`Pᵀ`汇聚；[全局partition的受限证据](https://arxiv.org/html/2605.14841v1)只保证固定更新子空间内的Euclidean等距，不保证覆盖任意全量更新、loss更平或质量无损。它与`BA`是替代参数化，不改变训练objective；base/head、seed及PRNG/参数次序仍属恢复身份，索引、重构、dense执行和调参也不消失。部分任务仍退步，不规则访问还可比低秩对照更慢；等距或紧凑adapter不签发总显存、墙钟或能力保证，任务与总费不合时保留普通LoRA、更宽空间或全量微调。<!-- source-family:SF-2026-ARXIV-2605-14841 -->

本人注拟：SF-2026-ARXIV-2605-14841 — exactv1§3–6/Eq5–12/Prop1/T1–3/§5.4/E/T6–8，2+1+2=5，固定正交partition替代BA差额深入。保等距只限image(P)、非loss/质量保证、部分退步和基线预算来源差异、H100不规则访存慢约10%、base/head/PRNG/索引及全费；未核实现/复现。待root必要Source/actual owner/逐字PRE及窄位，未写Books。

## A37 — RPAttention必要Source、实际owner差额与逐字PRE（未写）

[exactv1](https://arxiv.org/html/2605.14913v1)实际§3/Eq2–11、§4/T1–3和§5直接反例；current仅v1、无具名纠错撤回。日期[DC](SUP_DC_2605.14913_20261019.json)唯一v1May14 14:48:20Z、registeredMay15 02:23:35Z/arxiv.content/findable与公告下界组合全落北京May15，工具已实算bounded。2+1+2=5：局部但具体的压缩读取参数化，不把一般线性Attention原理计本文基础突破；实际接口gap深入。

每head先A=softmax(KWg)对M个learnedanchors竞争，再按每slot沿N-token列和+epsilon归一，得AhatᵀK/V。是一次feedforward训练出的分配，不是推理时迭代EM或对象辨识器；均衡scale不保证小object保留。对聚合K/V分别LN，只用V产生latentQKV并在M槽间residualselfattention，分发仍用原聚合K，另加3×3depthwise V旁路。固定M时交互5NMC+2M²C，但4NC²投影、latent投影3MC²/h、LN与卷积仍付费；M随分辨率增加不可继续无条件线性。无causal LM/cache转换结论。

ImageNet 300epoch AdamW/batch1024/lr1e-3/cosine20warmup/augmentation，与DeiT/PVT/PVTv2/Swin视觉backbone；T1 baseline遵原论文而非明示全同次重跑，PVT-S/Swin-T FLOPs更高，不能采统一降FLOPs。COCO MaskRCNN1x/1333×800、ADE SemanticFPN/512×2048，T2 baseline沿AgentAttention。同PVTv2-B0/300epoch T3去latentinteraction .3pt、改kmeans .5pt差支持局部模块效用，但未给seed/CI、实际M配置全表、GPU/TPU型号精度、完整墙钟/峰值内存/训练费用；只有TRC资源鸣谢，不能补硬件配置。§5明确花纹相似跨object误路由，attention图不证明semantic/object identity。未核实现/复现，支持和关键反侧足即停，不为宣称无缺遍历可视化附件。

实际owner MODEL-SELF-ATTENTION/Ch14，已完整读latent-routing两段、QKV路由/内容分离与后polynomial/WeightFormer邻接，Ch13/15交接。既有两段确实已承载固定K responsibility/slot瓶颈与非免费等价，故不把“新论文没名字”称gap；最小新差额仅是**同一内容路由中的两次归一、聚合K保持寻址而V另作槽间交互**，是已存latent接口的具体可选择分支，不重写generic因子低秩原则。

**逐字PRE**：Ch14 latent-routing“代价是affinity被限制为低秩…”完整段及其独立18283marker后，后“ 不保留token-to-token affinity，还可以让每个token先通过learned polynomial features…”前增唯一自然段：

> 槽内汇聚与槽间交换也可以分责：先让每个key在learned anchors间竞争，再按每槽收到的总权重归一，分别聚合K/V；只在聚合V上做小规模self-attention，而让query继续用原聚合K寻址。[受限视觉分支](https://arxiv.org/html/2605.14913v1)因而不等于迭代EM或无损softmax近似，归一化也不认证小对象或语义身份。固定槽数才有随token数线性增长的交互成本，投影、槽间计算、局部卷积与重训仍计费；部分配置FLOPs更高，相似纹理仍会跨对象误路由。槽瓶颈或质量/总费不合时，保留更多槽、普通Q/K/V或已验混合层，不从视觉FLOPs与attention图外推语言causal cache或端到端加速。<!-- source-family:SF-2026-ARXIV-2605-14913 -->

本人注拟：SF-2026-ARXIV-2605-14913 — exactv1§3/Eq2–11/§4/T1–3/§5，2+1+2=5，已有latent-routing基础不重写，仅归一gather/固定K与V交互接口差额深入。保单pass非EM/对象认证、固定M条件、baseline来源与无seedCI/墙钟、FLOPs反侧和跨object纹理误路由及全部费用；未核实现/复现。待root必要Source/actual owner/逐字PRE与窄位，未写Books。

## A38 — CRANE必要Source、实际owner与逐字PRE（未写）

[exactv1](https://arxiv.org/html/2605.14084v1)实际§3/Eq1–12、§4/T1–4/§5，针对采用接口补B.1–4、D.1–6及A.3/4公平配置/墙钟，C只读受影响architecture系数资格，不展开无关轨迹/全部语言表。current abs仅Jun9v2且无具名纠错/撤回信号，保v1不倒填后版。日期[DC](SUP_DC_2605.14084_20261019.json)唯一v1May13 20:09:35Z、registeredMay15 02:03:45Z/arxiv.content/findable同公告下界完整限北京May15，实际工具bounded。

从成对Instruct/Thinking差delta出发，逐tensor保大于median的坐标并乘2只近似补scale。Thinking生成的36 reasoning targets与Instruct16 tool-behavior targets各自masked loss，在Instruct端计算负gradient×delta，取二者min正部后**聚成block scalar**、相对本层expert/FFN归一；实际更新是scalar乘整个稀疏delta，不是逐坐标Taylor mask，故不能由个别p>0断言提交block共同下降。430 Instruct格式轨迹/±2邻域输入激活SVD，按归一singular值sigmoid软抑制`Δ−ΔVdiag(w)Vᵀ`；非严格nullspace/幂等projection，也只约束已观测局部输出，无匹配activation的tensor直接identity，非全局tool协议保持。80B另按full/linear层次数1:3作残差exposure修正，非linearattention输出天然1/3，本文不采通用architecture配方。

Qwen30B-A3B/Next80B-A3B、Roo195题每题3次、SWEV500、TB89题5次；只在Roo选alpha/tau、跨另外两benchmark不重调，但Roo非独立heldout泛化且baseline best-completed搜索预算未齐。T1–4支持局部成功/footprint选择，80Bpass3及移除sparsifier后30Bpass_all仍有反侧，不能采每指标支配。TTC输入+.1cache+5输出是token代理不是实际美元/延迟，TB墙钟包含harness；5个启动失败任务仍在89分母作失败，并发30B20/80B24、Daytona状态/parser有影响，不跨规模直接比性能。TB本地vLLM/TP4/BF16/4H10080GB/ctx131072/prefixcache，T.6/.8/20；无CI或新人口保证。B.4含重建projector30B约13min(2H100)、80B约48min(4H100)，不含source训练和所有超参评测/目标生成，trainingfree不是无校准forward/backward/SVD费用。两个endpoint行为互补、校准tool surface不漂移是成立条件。未核代码/复现，支持/关键反证足即停。

实际owner TRAIN-SFT Ch29 scaffold-bound specialization/merge产物段，完整读DoTS两段、前专家lineage与后CoTrace交接，Ch28/30既有交接复用。现有task-vector稀疏/系数proxy已有覆盖，不重写；缺的只是**合并时把reasoning迁移、agent行为和局部格式激活保护分责**的方向性接口。原暂拟7把通用保护/长期基础计入本文，现拟2+2+2=6，跨参数产物到tool协议消费者的实际边界；该gap与保持保证反侧深入。

**逐字PRE**：Ch29 DoTS“系数可以由少量未标注query上的回答一致性…”完整段后，后“当运行协议也随训练迭代改变时…”CoTrace完整段前唯一自然段：

> 若迁移目标是借用Thinking端能力、同时保留Instruct端工具协议，还可把两端差向量当方向性proposal：分别用reasoning与agent行为的masked梯度评估该方向，再按block调幅，并用格式位置输入激活的SVD方向软抑制更新。[受限成对checkpoint证据](https://arxiv.org/html/2605.14084v1)中的梯度分数先聚成scalar，并非逐坐标共同下降mask；格式软抑制也只约束校准轨迹上的局部输出，不保证有限合并后schema、停机或工具动作不变。它增加target生成、梯度、SVD、搜索及回归成本，token代理不等真实墙钟，部分次级指标仍回退；endpoint不互补、工具面漂移或保留能力失配时，应重校准或保留原checkpoint/独立experts，不让trainingfree或nullspace名称替部署协议签字。<!-- source-family:SF-2026-ARXIV-2605-14084 -->

本人注拟：SF-2026-ARXIV-2605-14084 — exactv1§3/Eq1–12/§4/T1–4/§5/B.1–4/D.1–6，A.3/4与受影响C，2+2+2=6，定向合并/协议保护gap深入。保block非coordinate gate、软谱非严格nullspace或全局协议保证、Roo选择/预算未齐、次级反侧、TB分母与并发/parser身份、TTC非cash/延迟及校准全费；未核实现/复现。待root必要Source/actual owner/逐字PRE与窄位，未写Books。

R21两个一次core的具体作者判断：15071/TABVLM实际是历史文化题集与模型/元信息小切片，未隔离知识、视觉或关系推理，也不足反证上下文/scale作用；15133/ContinuousCausalPFN沿CausalPFN的3MLP prior与独立treatmentencoder，新增条件仍是连续因果估计任务而非通用学习/当前模型机制，故均贡献关闭、不评分。不是因低分、小模型或foundation名称本身排除，原题摘/决定域证据保留。

## A39 — 必要同义主题查漏的真实停止与首半题摘判断

R22批准14841/14913必要Source/日期/actual owner及逐字PRE，作者已真实保存两单段/本人注并顺读完整两侧，待root实际POST；GPart改到Ch30 CDVFT完整段后→参数小例子前，其余正文不变。此刻仍8已生效I，不预支POST。

本轮有界补题名不按679再造全部摘要队列。初始q1漏了显然的normalization/decoding/cache/LoRA/representation表达，故在相同679身份线索上只追加q2：`speculat|decod|KV|cache|token|normali[sz]|SFT|LoRA|MoE|distill|align|training|train|gradient|memory|routing|autoregressive|generation|image editing|mechanistic interpret|test.time|representation|causal.*policy`。103个非q1标题中13与原May15表§3身份逐字相同：15156/15113/15134/15190/15079/14477/14292/14005/14978/14773/14591/14438/14362，只机械去重，不重做旧有效事件或读其题摘。余90标题已实际完整浏览：明确物理/量子/医学信号/普通领域检测预测、古语言学等40条止于题名，不因现有宽池变摘要债务；50个直接模型主题或含糊题名保存[同义补题摘](SUP_ABSTRACT_Q2_20261019.json)，当前只读完下列26，其余24仍普通题摘工作。额外267分类投影不当队列/全量覆盖，不依赖created窗口当公开日。

| 身份 | 具体旧约束→增量→改变的选择 / 决定域 | 初筛 |
| --- | --- | --- |
|13866 AlignmentHiring|alignment不必减少群体差异→29模型/177职业及pre/post对照、数据/表示假说→重新检查后训练的群体行为与归因；2+2+2=6/安全受影响，不采招聘建议或直接认定表示因果|潜力|
|14063 RMemSafe|固定source anchor在source崩塌仍生效→预测entropy调全部source耦合、低可靠fallback与可控退化→改变CTTA保护条件；2+2+2=6，显式保高置信错不检测|潜力|
|14252 SeAlKD|强迫每时刻同目标可能损中间动态→只矫正错误时刻、classlogit与temporal权重→比较聚合任务的逐时监督条件；2+1+2=5，不因SNN小模型排|潜力|
|14311 BBCritic|二元GUI监督混合有效/相似无效动作→两stage contrastive affordance与四级dense动作对照→比较action ranking监督；2+2+2=6，hypothesis不等分类普遍不适用|潜力|
|14323 DLR|单latent固定路由限制子策略组合→动态search/select/update联合离散codes/router/模型→比较LM后训练单stage路由；2+2+2=6，MDP最优组合定理与LM启发需分开|潜力|
|14333 InsightTok|generic重建压掉glyph/face细节→局部content-aware perceptual监督→比较codec训练目标与AR读取保真；2+1+2=5，不把特定可读性当通用视觉质量|潜力|
|14347 EP|SAE稀疏feature训练成本/跨checkpoint不对齐→stream leader/Voronoi exemplars、匹配与ablation→比较解释字典身份/干预；2+2+2=6，安全受影响且nearest距离非免费OOD认证|潜力|
|14364 MoRe|按task架构分配不等表示模块可识别→延迟依赖下fundamental/specific模块识别与保旧模块→比较持续适配的可识别/复用条件；2+2+3=7暂拟，须真核theorem及LLM probe非普遍因果|潜力|
|14373 CoCD|历史梯度陈旧不总无用→coherence条件/周期坐标warmstart与有限差分平滑误差→比较ZO查询与下降资格；2+1+3=6，实际条件深入，O1每步不等总查询恒定|潜力|
|14379 DAGS|中间state重启可加速却改hidden beliefs→解析反例+observation flags→改变selfplay示范覆盖与均衡资格；2+2+2=6，不因小游戏/无LLM排通用训练反证|潜力|
|14381 NodeSynth|合成安全query无真实证据/人口→证据锚定taxonomy展开与独立guard核验→比较synthetic eval构造；2+2+2=6/安全受影响，5倍fail不自动是难度公平因果|潜力|
|14382 DeltaForcing|teacher条件对齐不等生成轨迹连续→latentdelta一致性调teacher trustregion/continuity→改变interactiveARvideo蒸馏；2+2+2=6，不借TRPO名义授保证|潜力|
|14391 MoDE|双latent codec可能只SQ/VQ及ESE/CEM模块组合；一次core看实际可迁移的表征职责/受控fidelity-perception条件，非因压缩应用名称排|核心未决|
|14409 BilevelRegularity|每个上层x都regular与几乎处处差异是否影响模型优化→rigidity/counterexample/prevalence与计算困难→2+1+3=6暂拟，仅可迁移优化条件，须核具体假设不借通用优化名收纯类比|潜力|
|14420 DVMap|国家persona标签粗不直接新贡献；一次core核高consensus筛选后的人口/目标改变是否具体机制边界，不能以WVS/CoT/GRPO组合与排名直接纳|核心未决|
|14423 FederatedAC|共享表示与个性policy耦合多时尺度→共同linear近似/QR扰动与异质Markov混合的单timescale有限界→比较分布式学习收敛资格；2+2+3=7暂拟，Hopper应用不是门槛，须真核条件|潜力|
|14487 HeadForcing|ARvideo不同head同cache/位置政策→局部/anchor/memory分类与分层KV、headwiseRoPE→比较长期状态分配；2+2+2=6，分钟输出不认证无限可靠|潜力|
|14521 FoldLN|删centering通常改函数→CCC/CBWC与图上foldable资格→比较LN→RMS推理变换的等价域；2+2+2=6，须核分支/bias/非线性与实际速度配置|潜力|
|14553 PromptBandit|单metric/穷举prompt选择不覆盖Pareto/可行性→纯探索bandit和linear结构新error界→比较多目标query预算；2+2+2=6，必须核噪声/linear假设|潜力|
|14571 MirrorTouch|跨视觉/触觉映射无共同坐标→语义/分布/几何三约束→比较触觉表示对齐接口；2+1+2=5，不从几何图认定脑机制/机器人同理心|潜力|
|14594 TOPOS|固定head拓扑、PerceiverVAE/flow/纹理组合可能仅资产任务；一次core核显式canonical拓扑表示的新模型接口/有效条件，非以industrialgrade或3D指标纳|核心未决|
|14637 AdaptiveWindow|完整题摘明确容错量子计算的error-correction window decoder，非生成模型/其运行时；buffer术语类比不构成主线贡献|范围关闭，不评分|
|14663 LocalPL|局部PL/nonconvex不能直接用强凸率→C2与multiplicative noise下几何asymptotic rate→比较过参数训练的收敛资格；2+1+3=6暂拟，核局部事件/噪声不补实际深网保证|潜力|
|14727 CHASM|频率各自任意channelmix不保持共坐标→shared eigenbasis+逐频正gain/axis分离→比较谱mixer结构约束；2+1+2=5，自然图像同backbone对照使其不只MRI应用|潜力|
|14746 ValueFiltered|每步安全steering会误干预本可安全轨迹→value过滤及falseintervention显式界→比较安全/效用阈值资格；2+2+2=6/安全受影响，须核value误差/概率条件|潜力|
|14750 EVA|posthoc安全改权重不能凭编辑名称采信→局部neurons定位/定向更新与LLM/VLM对照→比较安全编辑影响域；2+2+2=6/安全受影响，不预授消除能力或无utilitytax|潜力|

当前首26为22潜力/3一次core/1范围关闭，未成为确定候选；数量只是实际漏斗记录，无保留率或score上限，后24题摘未读不能假称发现闭。

## A40 — 同义补检后24完整题摘实际判断

已实际读[同一Q2原件](SUP_ABSTRACT_Q2_20261019.json)后24完整题摘；不把模块组合自动准入，不以物理/空间/小模型类标签泛排。

| 身份 | 具体旧约束→增量→选择 / 决定域 | 初筛 |
| --- | --- | --- |
|14790 GoR|完整题摘明确科研idea生成/自动科学创新监督，是当前暂缓AIforScience研究路线；不是文献检索的agent执行/证据机制，不通过SFT通用节点重引科学应用|范围关闭，不评分|
|14833 EASM|history/emotion/intent构造context可只是已有memory组合；一次core核30同底模A/B是否新增记忆可靠性/失效条件，而非通用个性化改善或未控制评分|核心未决|
|14842 AbstractEdit|字面编辑分数不测abstractintent/保留→entity-level rubrics与人审关联→比较intent、编辑程度和preservation分责；2+1+2=5，LLMencoder/thinking效果须核对照|潜力|
|14843 MechVerse|外观流畅不等articulation/coupling有效→机械链接三复杂度+human运动判别→修正视频生成评价盲区；2+1+2=5，采模型测量非科学发现/物理设计路线|潜力|
|14860 NAPTS|全局monotone acceptance可能拒有益coarsestep→非单调窗口接受+Schwarz并行subdomain与coarse correction→比较分解训练调度有效条件；2+2+2=6，CPU时间需绑完整配置，不因非LLM优化排|潜力|
|14868 GradientPrediction|adversarial eval反传占成本→hiddenstate线性预测inputgradient/NTK精确域→比较近似攻击强度与墙钟；2+2+2=6/安全受影响，不把gradient预测失败当模型鲁棒|潜力|
|14877 HeatKV|视觉AR cache各head同配→离线prior-scale attention排名/静态budget schedule→比较head级保留与校准；2+1+2=5，2×allocation不是端到端总显存或加速|潜力|
|14891 HIT|RQ中间scale不对应真实尺度→跨scale token overlap与LR/HR preference正则→比较多尺度codec/一次forward输出；2+1+2=5，300M与1B不直接证明同预算更好|潜力|
|14912 PluralisticRepair|新scoping/signalling/repair术语不足；一次core核PRS是否有可复查principled-vs-pressure区别及成对支持，不能由两模型小样本泛宣治理机制|核心未决|
|14935 MSCoT|离散多尺度motion token难做连续控制→token guidance+连续residual refiner/test-time优化→比较生成factorization与控制精度代价；2+1+2=5，10×仅绑实际配置|潜力|
|14937 SlotMPC|objectslot dynamics+梯度MPC可能是已知WM/planner组合；一次core核有限覆盖下gradient/sampling差额的受控新条件，而不是小游戏成功率|核心未决|
|14948 ACELoRA|持续imageedit干扰与historystate增长→自适应正交解耦+rank-invariant信息压缩→比较adapter干扰/长期存储；2+1+2=5，必须核正交对象/历史信息不损资格|潜力|
|14967 InfoSFT|按likelihood单调筛掉novelty→中confidence token信息权重→比较新行为吸收与遗忘的目标；2+1+2=5，不把一行修改当无代价/普遍保持|潜力|
|14984 Sat3DGen|geometryfirst/viewtraining可能只域数据约束与模块组合；一次core核表示/几何监督新接口可迁移条件，不凭RMSE/FID双优或satellite标签收/排|核心未决|
|14990 ChildView|完整题摘用现成detector/embedding分析婴幼儿第一视角经验和物体分类暴露，没有新模型学习机制/受控模型反证；对未来模型的建议不构成当前主线增量，非因非典型数据排|范围/贡献关闭，不评分|
|15054 LATERN|frozenVLM的多frame memory/递归evidence可能常规组合；一次core核time一致性、证据去重/状态规则的新机制或受控blindspot，不能因应用低分直接纳|核心未决|
|15058 NeuroTrain|完整题摘仅既有SNN训练taxonomy/统一benchmark框架，没有报告新学习规则、控制混杂或修正有效边界；不是因survey类型排，是实际贡献止于归类/实现整合|贡献关闭，不评分|
|15116 DriveCtrl|depthcondition生成与style/data pipeline本身常见；一次core核结构adapter保持annotation的新约束或DVRS有效性，不能由驾驶/基础模型名称纳或全排|核心未决|
|15181 PlansToPixels|planner分解/orchestrator RL/成功轨迹再SFT是常规pipeline；一次core核分责耦合的实际新信用/执行条件，而非多步任务比单步更高|核心未决|
|15182 WarpHistory|相机条件通常改架构/重训→camera warp作为pseudo-history、target位置对齐/validtoken选择→比较冻结模型接口与一次离线LoRA；2+1+2=5，零训练分支与单video后训分开|潜力|
|15183 TensorSimilarity|行为近不等机制同、参数量受换基对称影响→特定tensor模型的代数invariant/递归等价度量→比较机制验证的对象与条件；2+2+3=7暂拟，须核模型类/degeneracy，不把“solved”推广任意网络|潜力|
|15193 SphericalFM|Euclidean chord离开latent shell→radial/angular probe、定半径prior与decoder微调/球面path→比较codec几何与flowtarget；2+1+2=5，radius弱贡献非无信息、probe不等因果|潜力|
|15196 RefDecoder|denoiser受条件但VAEdecoder无条件可能丢细节→referenceencoder与多upsample attention→比较条件进入codec位置；2+1+2=5，decoder自身训练不因generator可换件免除|潜力|
|15199 EntityBench|跨shot一致性可被错身份appearance混分→presence/fidelity门后比较crossshot与长recurrence→改变生成/eval记忆身份；2+2+2=6，memory先verified是否真实资格须核|潜力|

后24为14潜力/7一次core/3关闭；Q2合50完整题摘为36潜力/10一次core/4关闭，仅初筛非当窗确定候选。题名同义补检在这90的有界主题/明确非主题标题处停止，不继续把余267分类投影转B队列；尚需对已选具名core、真实日期与机构剩余slice处理，source覆盖未闭不能预称完成。原q1的62余线索仍只按A22/A33题名范围，不产生一整池逐项关闭债务。

## A41 — PolarProbe必要Source与actual owner逐字PRE（未写）

[exactv1](https://arxiv.org/html/2605.14125v1)实际§2–4/图3–6、受影响5.1–5.6/5.9，机制/评价与直接反证足即停，不遍历无关refs。current May16v2没有具名纠错/撤回说明，采用v1不倒填；[原DC](SUP_DC_2605.14125_20261019.json)唯一v1May13 21:21:10Z、registeredMay15 02:04:42Z/arxiv.content/findable同公告下界完整北京May15，已实算bounded。

为每层/每域独立训练线性probe和relation prototypes，以probe-space实体差向量norm的soft-Spearman拟合图shortest-distance次序，以cosine与prototype拟合关系方向；是ordinal距离而非恢复真实相等尺度。30训练graph×20描述、50validation×20、50test×30，shuffle实体/关系次序抑制位置捷径，另13新名字/新surface OOD；rank512、100epoch、λ5/lr1e-5由gridsearch。Llama3.1-8B、OLMo7B九checkpoint及Pythia14M–6.9B，randominit/identity/linearbaselines分验，不等所有语义可线性读出或完整graph精确恢复。家族树词汇gender提示、非Euclidean metro/树距离与多对多/非交换关系是明确反侧，entity变多表现下降；naturalistic/multilingual仅LLM合成同spatial域非真实无限自然语义。

QA500graph中type error与correct-token logit负相关，**existence error无对应相关**；不能由距离probe好推行为可用。干预用B伪逆把prototype映回模型空间，再对**已知正确实体token**作±方向/强度steering，支持受控局部影响，不是无需gold的通用推理算法，也未证明必要/唯一binding机制或排尽任意等范数扰动。域间prototype子空间角度与disjoint不能自证功能模块，rank低非信息精确保留。未披完整GPU/precision/seed/CI与全部搜索/干预费用，不声明实现已核或复现；源码当时承诺camera-ready另给，不作为本文可支持诊断的阻塞。

实际owner WORLDVIEW-REPRESENTATION Ch5，完整读动态表示/可读不等使用、后规则选择/状态恢复及句法干预邻接，Ch4/6交接；Ch12拥有token接口不接管这里的上下文关系。既有一般probe/causal限制不重写；仅补**关系存在的距离读出与关系类型的方向读出分账，且只有后者关联当前QA**的具体诊断差额。原暂拟7把既有2019/2024 probe原理当本文新基础，现实际2+2+2=6，只对这份表示—行为接口命题；gap与因果推广反侧深入不因改分缩审阅。

**逐字PRE**：Ch5“Representation learning 的关键收益…”完整段后，后“当不同规则能解释同一输入序列时…”前唯一自然段：

> 上下文中的关系还可拆成“哪些实体相连”与“属于什么关系”两份读出：在线性子空间中，用实体差向量的距离次序拟合图距离、用方向对齐关系prototype。[受限语义图诊断](https://arxiv.org/html/2605.14125v1)中，关系类型误差与问答表现相关，距离误差却没有同样关联；可读的几何对象因此不能合成一张能力证书。对已知正确实体token的prototype干预只支持局部影响，不证明唯一或必要binding；实体增多、未见名字及非Euclidean图仍退化。描述/图构造、probe拟合、选层和白盒steering均计费；任意语义、复杂关系或下游行为不通过时，保留显式结构、独立任务测试与更窄配对干预，不把线性可解码当作模型普遍按该图算法推理。<!-- source-family:SF-2026-ARXIV-2605-14125 -->

本人注拟：SF-2026-ARXIV-2605-14125 — exactv1§2–4/F3–6/5.1–5.6/5.9，2+2+2=6，distance/type与QA消费分账差额深入。保ordinal非等距/全图exact、existence无QA相关、oracle正确token steering非必要唯一因果、entity/非Euclidean/OOD反侧及构造/probe/白盒全费。必要Source/日期/具体owner与本文稿待独立核验，未核实现/复现。

R23/26真实POST后为11I，两单段及CRANE窄位均释放；14028仅报告、14087中心争议有效。R25三core按具体反证能力确认关闭：14761初始test目标与后来SelfRetest不同而共享target相关不证价值因果；14857六阶段与单专家/LLM“corrected acc”没有新裁决机制；15015 pedagogical proxy/专家judge差异延展已知偏差、来源与后到模型不同不证size因果，均不评分。R27把14409/14423及后续14252改为**一次决定域未决**，不预排全部证明Deep。当前机械归并漏斗为183 arXiv完整题摘+UAM1；29已具体关闭、109潜在贡献（13已有必要Source/Books、13909资格另1，其余95普通Source/日期）、46一次core尚未定；14125本节刚准备，尚未root通过。数字不是确定当窗候选、完成态或全深审队列，后续按真实决定域更新。

## A42 — RQ-MoE必要Source、actual owner与逐字PRE（未写）

[exactv1](https://arxiv.org/html/2605.14359v1)实际§3–5/Eq1–14/T1–5，必要B设置及C2–4质量/费用，A1/A2仅为受影响“QINCo特例/De充分”核边界；初次文本截断§5.2约349token不作已读，采用依据来自实际完整T2/3、§4接口和费用表，不需要重新泛读同结果宣传。current只有v1、无具名纠错撤回。[原DC](SUP_DC_2605.14359_20261019.json)唯一v1May14 04:35:57Z、registeredMay15 02:10:12Z/arxiv.content/findable同下界全落北京May15，工具实算bounded。

每阶段K256码字拆成base c与expert e而共享同一index；instruction I是已选expert向量prefix-sum，动态transform吃c/I并全softmax混合N个MLP。已知全index时先lookup/add形成各I，再可并行重建各stage选定动态码字并求和；**编码仍按residual串行选择**，不是所有ANN查表无需解码或原embedding无损。第二级是全部N加权非稀疏topk，主质量表N1，不把表1容量名义当多expert已获因果收益。NRL为log(1+当前残差平方/(stopgrad前残差平方+epsilon))；原Eq15/16写的是gradient magnitude非向量，低值/局部训练观察不授全轨迹outlier鲁棒。

Deep/BigANN/FBssnpp/Contriever普通embedding维96/128/256/768，train前500k或10M、后10kvalidation/earlystop10epoch，test首1M，8/16byte；Adam lr1e-3/batch1024、FAISS RQ初始化、UNQ引用旧published结果。T2/3重建与nearest-neighbor recall不同对象；C1小数据FB16byte LSQ仍好，C4参数切片有质量/时延折衷。T4/C2平均每vector解码快并不代表同质量总请求快：quality主配置N1L16/12，timing N1/2/4与L1–8不同；batch4096/10warmup/100同步runs且精度/CI未披。T4/C2称A800而B4称4RTX3090，不能拼成唯一可复现硬件；N1编码96.2高于QINCo91.8微秒也保留。C3只比QINCo2 MSE未比其优化延迟，不授6–14倍最佳现有端到端加速。

A1恢复QINCo时把f_ins改为随动态重建递归，不再是Eq4固定expert prefix-sum，不以这份广义family说明批准实际并行参数化无损覆盖QINCo。A2只作局部信息维数capacity argument，维度足够不构造或证明受限index-sum保存任意history；不采De=D普适充分/超D冗余的完整定理。本文采用接口不依赖这些未闭泛化。码本/网络参数与PRNG、训练/初始化、metadata、decode buffer和完整ANN/reader费均不含在8/16byte单vector码里，zero extra routing bits不等零总状态。未核实现/复现，窄机制与关键反证足即停。

实际owner AGENT-RAG Ch76的检索压缩表示/读取接口，非MODEL-MOE新通用sparseexpert架构、也非视觉codec论文。已完整读多向量数据面第1段/ColBERT码本两段、普通PQ/精化邻接以及Ch75/77交接；已有物理codes布局、rare-token预算不包含**index复用控制状态与重建数值分离以移除decode链**。2+2+2=6，具体code训练/解码消费者边界，不把理论特例/信息维数当本文新基础；gap/性能保证反侧深入。

**逐字PRE**：Ch76“多向量匹配需要细粒度表示…”完整段及其独立23553marker后→“保留原始token identity的ColBERT…”前唯一段：

> 压缩码的恢复也可把“控制后续码本的状态”与“累计重建的数值”分开：让同一index同时选base码字与expert向量，先对已知indices做lookup和前缀累加，再并行构造各步动态码字。[受限embedding量化分支](https://arxiv.org/html/2605.14359v1)只消除这条decode依赖，编码仍串行，码字、expert网络和临时状态也不在每向量的字节数里。它未验证完整多向量RAG；重建MSE、近邻recall与最终答案须分验，主质量配置与最快计时配置也不能混成一个工作点。批量decode提速不保证单query或总请求更快，数据漂移、质量或完整费用不合时保留普通PQ/RQ、原向量精排和原索引，不由共享index或MoE名称签发无损压缩、免费routing与生产SLO。<!-- source-family:SF-2026-ARXIV-2605-14359 -->

本人注拟：SF-2026-ARXIV-2605-14359 — exactv1§3–5/Eq1–14/T1–5/B/C2–4，A1/A2受影响边界，2+2+2=6。仅index复用/控制prefixsum与重建分离；保串行encoding、全expert非稀疏/主N1、timing/quality不同点、A800/3090口径与LSQ反侧、QINCo特例需改fins/维度非信息充分、码本/网络/训练/ANN全费；未核实现/复现。待必要独核、actual owner/PRE与窄位，未写Books。

## A43 — DiffusionOPD必要Source、采用边界与actual owner逐字PRE（未写）

[exactv1](https://arxiv.org/html/2605.15055v1)实际§3/Eq4–23/Alg1、§4/T1/F3/5/6与训练配置读足，公式权重、ODE奇异与state derivative是本次必要反证，不遍历无关refs。current Sep11v2的abstract未给具名撤回/纠错信号，仍用v1；[新取DC](SUP_DC_2605.15055_20261019.json)唯一v1May14 16:49:09Z、registeredMay15 02:27:04Z/arxiv.content/findable同日程下界全落北京May15，工具已实算bounded。

每个task先独立reward训练teacher，student从共同base启动，round-robin对各task自己rollout，冻结teacher在同一student states给一step目标，累积完整task round才更新。正且有限共同variance、同state/scheduler时，Gaussian条件KL等于mean差平方/(2variance)，只消除这一步action采样噪声，不让student状态分布变确定。零噪ODE时不同Dirac transition的KL为无穷，不是直接代variance0；Eq12另选L2 mean-match，是有效surrogate而非有限KL极限，不能从“统一”名称转授等价。

**关键导数边界**：Alg1 rollout明确no_grad，Eq15只对固定state的student mean求导，没有对student occupancy的score/path derivative；因此是逐轮更新的固定state半梯度，不能当Eq11依θ路径期望的完整梯度。Eq18–21对当前state固定、未clip且KL不是stop-gradient advantage的特殊构造，action-independent KL乘score项条件期望为零；不等通常PPO含return-to-go/冻结advantage/多epoch的统一等价或全路径variance支配。作者受测F6只支持其loss实现下更快改进，不补理论假设。SDE公式t=1的sigma奇异也需实际scheduler有限化，本文不照抄未披露endpoint recipe。采用窄接口不依赖这些泛定理。

SD3.5-Medium512、LoRAr32/alpha64、evaluation40step ODE，FlowGRPO的GenEval/OCR split与Pick-a-Pic→DrawBench；teacher OCR/Aes选GRPO-Guard、GenEval选NFT，是先按task选择算法而非相同训练过程唯一归蒸馏。SFT来自teacher images而DMD/TDM/studentownrollout，T1/F5支持局部取舍；OCR teacher .93、multiNFT .96而OPD .94，Aes teacher多个metric仍高于student，不能采每格SOTA或彻底无冲突。没有实做的GPU/precision/完整train batch与seedCI，不能从引用DiffusionNFT继承成本文披露。T1墙钟97.01h用max teacher85.75+OPD11.26，隐含并行teacher资源；三teacher时间总165.84h再加11.26h为177.10h，只是串行stage时间和，不冒同硬件GPU-hours，但足以说明max不是总compute。同任务round共享更新也不能保证梯度不冲突/无遗忘。全部teacher训练、候选/奖励选择、rollout、逐step teacherforward与低/零噪不同loss均计费，未核实现/复现。

原暂拟7中的Durability3依赖“连续OPD统一精确梯度”的新增理论；实际资格不成立于no_grad/Dirac，因此采用命题收窄为2+2+2=6：多teacher训练与同state条件mean-match的跨训练/采样接口，不把既有GaussianKL公式当本文新基础。保全文已读与上述争议，不以改分减审阅。实际owner TRAIN-SFT/Ch29 own-rollout distillation，已完整读05204少步privilegedteacher两段、signed/AntiSD前接及OutcomeFailure后接；Ch24拥有sampler/state语义，本文不在那里重复多task训练链。现稿有ownrollout/privileged目标，但没有task教师分责、条件KL/ODE另选目标及no_grad半梯度这份训练接口差额。

**逐字PRE**：Ch29 05204“它用约4x FLOPs…”完整段后→`#### Outcome Failure 不能单独定位 Perception Credit`前唯一自然段：

> 多目标生成还可先各训专长teacher，再让同一student按task轮流采自己的去噪轨迹，在这些state上匹配对应teacher的一step目标。[受限多teacher蒸馏](https://arxiv.org/html/2605.15055v1)在同scheduler、共同正variance下可用Gaussian条件KL的mean差；零噪ODE则另选L2匹配，不是把Dirac KL直接除以零。Rollout采用no_grad时，更新只对固定state求局部梯度，不是完整路径分布KL的全导数，也不保证task间无冲突。它保留专长探索与整合的分工，却仍有单项退步；teacher并行墙钟的max也不等总compute，全部teacher训练、reward选择、student rollout与逐步监督均付费。Teacher覆盖、sampler资格或质量/总费失配时，保留单目标模型、原联合训练或已验普通蒸馏，不由解析KL或较少整合步数签发全目标保持、PPO普遍劣势与免费能力合并。<!-- source-family:SF-2026-ARXIV-2605-15055 -->

本人注拟：SF-2026-ARXIV-2605-15055 — exactv1§3/Eq4–23/Alg1/§4/T1/F3/5/6，2+2+2=6；原拟7理论已深入但仅采多teacher/固定state一step匹配。保正variance条件、ODE另选L2非DiracKL极限、no_grad半梯度非occupancy全导数、PPO特殊条件、单项反侧、teachermax非总compute及全部费用；未核实现/复现。待必要独核、actual owner/PRE与窄位，未写Books。

## A44 — 已验结果同步与有限core消费

R28–33已实际逐项完成14125/14359/15055的Source、日期、actual owner/PRE及保存态POST；现为14 I、14028仅报告1、14087争议1，共16新增已处置结果。README已把这16项融入§1/3/4/5/6，加受保护原Charon共17表列家族；仍进行中，不是最终候选数或DAY。15055实际单段位于Ch29 05204费用完整段后、Outcome Failure小节前，本人注仅保来源/采用/限制，根复核R33通过，窄位释放。

消费root R32实际一次贡献决定域，复用其原件位置，不重复泛读：14409 §1.2/4.4/结论的一般constrained-bilevel新条件与当前模型训练只有引文联系，没有相应依赖构造/反证，贡献关闭，不评分；14252 §3–4.3/5.1的LIF分类时间累加、ELA错类成对压平与STA步间KL只支持该任务接口，未建立LLM token/推理步骤/diffusion state对应，贡献关闭，不因小模型/SNN类型排除。两项均保原题摘/实际决定证据，不冒完整证明审阅，不为不影响处置的日期另开债。

14423保潜力：共享线性critic子空间、私有actor/critic面对异质transition有具体训练共享条件，后续只核实际Markovian/single-timescale假设与PPO实例，不能借foundation名授神经PPO同一收敛保证。14937保潜力：相同离线支持的gradient/MPPI和policy/slot对照可影响learned-dynamics planner选择；采样OOD解释仍假说，MetaWorld MPC无增益及四模拟任务/表示预算限制须保近文，不扩机器人算法史。

按A41同一184身份口径机械更新为31明确关闭、111潜力、42一次贡献core未定；111中16已有逐项独核处置、13909日期资格另1，其余94仍普通必要Source/日期。仅记录当前漏斗而非111确定候选/111全深审队列。root接手14833/14912/14984/15116四个一次core，作者避免重复；其他有界已具名必要域继续，宽679/267不再扩发现。

## A45 — Slot-MPC必要Source、actual owner与逐字PRE

[exactv1](https://arxiv.org/html/2605.14937v1)实际§3/Eq1–11、§4/T1–4与A/B、必要C1–4/D/E1：只为解释planner–learned-dynamics接口、对照预算与直接反侧，未查代码/像素或复现。current仅v1无具名纠错/撤回；[原DC](SUP_DC_2605.14937_20261019.json)精确ID/DOI、arxiv.content/findable，唯一v1 May14 15:12:15Z，下界May15 00Z至registeredMay15 02:24:10Z完整在北京May15；created02:24:09并非本次日期依据。没有具名更早全文线索，不遍历全部作者渠道。

SAVi以重建学习4×128 slots，cOCVP消费全部slots与线性投影后加到各slot的action，autoregressive预测；pixel+slot一致性损失各权重1。独立BC policy从专家示教拟动作，用其逐步想象初始化完整action sequence；规划终点slot与goal-image slots作Hungarian最小配对后SSE，优化动作、只执行第一项再真观测重规划。不是从重建自动得到物理/因果实体，也不使goal图像可得、slot身份恒定或距离等于可达性。MPPI importance-weighted elites/移位warmstart与梯度单trajectory是比较分支，梯度更新本身没有显式support约束或不确定性校准，不能采“必留在数据支持内”。

四模拟task、训练随机探索9000/验证1000；MetaWorld200专家、robosuite1800训练专家/200eval源，成功表用50episodes与Wilson95%CI（ablation无独立seed/CI披露）。SAVi和WM随机视频训练、BC仍付专家标签；不能把reward-free写成无expert或无监督总费。自家64×64对DINO224×224、4×128对196×384，预训练/分辨率/容量与planner不同，T1/T4跨体系差额不能唯一归slot。无object ablation把SAVi换卷积AE、其他模块固定，支持局部分解差额；不授所有物体表示优越。

T3同一离线数据下MPPI .04/.04/0/0，梯度.64/.52/.42/.22；但C4梯度3iterations/1sample/1policyproposal，H8（MetaWorld/Square）或15（Stack）、lr.001；MPPI5iterations/64samples/16elites/16policyproposals、H15/std.05–2，**并非同horizon或同预算，尤其Square/MetaWorld混有horizon变化**。OOD是作者解释不是直接测量，当前不足以归因为采样必更OOD。去MPC .64/.52/.36/.18，MetaWorld完全无增益、robosuite仅局部增益；去policy .32/.18/0/0表明先验重要，仍不等梯度天然安全。A6000一planningstep .42/.48s对MPPI4.22/5.19s，precision/totaltrainingsteps/seed/墙钟同步细节ND，不能外推完整控制deadline、实时/安全或最佳等质量加速。E1换proprioception/goal horizon即改变DINO成功，故不采“patch模型根本不适合规划”。全部parser/WM/BC训练、expert采集、matching、rollout/反传及真实反馈计费，机制与关键反侧已足，停止扩其他算法。

采用评分2+2+2=6，只对表示/预测/规划接口的局部选择边界，不为slot/梯度成熟原理给新基础分。Actual owner MULTIMODAL-WORLD-MODELS/Ch25，完整读Imagined rollout通用model exploitation、Soft MPCritic两段、后漂移刷新段，以及LatentGeometry/Cost两段；Ch24 sampler与Ch26 controller交接已实读。现有内容解释误差/复用warmstart和几何cost资格，但未承载**同一离线模型下policy初始化的单轨迹梯度与广采样之间的实测选择差额及非匹配horizon反侧**；不是缺同名论文就称gap。不在Ch26重复模型内planner。

**逐字PRE**：Ch25“误差可能因feedback放大、收缩或转向未见状态…”完整段后→“短规划的费用还取决于下一次从哪里开始搜索…”前唯一自然段：

> 有限离线数据下，规划器如何查询模型也会改变失败路径：可先用示教policy初始化动作序列，在预测终点与目标的配对object slots上定义距离，再沿同一候选轨迹反传，而不只扩大采样。[受限离线对照](https://arxiv.org/html/2605.14937v1)中，这条分支优于所测MPPI配置，但horizon、候选数与迭代预算并未配平；“采样更易越出支持域”仍是假说，梯度也没有支持域保证。移除MPC在部分任务毫无退步，说明可用policy不必总加搜索。Slot分解、示教、预测器、匹配和反传均付费，单次planning耗时不是控制deadline；goal距离失真、覆盖不足或闭环质量不通过时，保留原policy、已校准采样/显式simulator和短horizon真实反馈，不由较低维latent或局部梯度签发物理安全。<!-- source-family:SF-2026-ARXIV-2605-14937 -->

本人来源注拟：SF-2026-ARXIV-2605-14937 — exactv1§3–4/Eq1–11/T1–4/A/B与必要C/D/E1，2+2+2=6，planner查询/表示与离线支持接口差额深入。保BC示教、Hungarian距离非可达性、MPPI/梯度horizon预算不匹配、OOD假说/无support保证、MetaWorld MPC零增益、DINO分辨率/容量混杂与完整费；未核实现/像素/复现。

## A46 — 有界机构尾的真实入口与停止

2026-10-19恢复后仍只处理May15，不加载邻日研究结论。Google Research从2026年Blog的明确May月链接进入[完整May列表](https://research.google/blog/2026/05/)，实际仅四条May28/27/19/1、无分页，May15无条目；不是417论文year facet已全核。[DeepSeek研究与动态](https://www.deepseek.com/news/)由官网“更多”实链进入，研究当前十条中Feb25→June24跨目标日，动态Apr24→Sep10，向旧展开不可能补入位于这两个相邻2026时间之间的日期；不以当前October首页banner当May历史证据。API docs首页banner跳到search指南非news，不作历史覆盖。

MiMo首页8论文时间层March13→June29无May15；首页Blog15条无日期且More不是可信档案，故有限恢复公开页面源的已加载脚本`4752.2908c99e.js` route/frontmatter清单（16个英文blog route，含旧safety一条，排通用index/dummy），不猜API路径。带日期的主要技术Blog为May30 inference、June8 UltraSpeed、June10 coding、Sep27 repetition、Dec2025 HSS/safety。其余已观察route指向iframe，实际解析各指定chunk的src后只读日期头：`/mimo-v2-5/index.html`April22、Pro April27、ASR/TTS系列April2026（不补日）、`/mimo-v2-pro/index.html`、Omni、TTS均March18。故已注册Blog日期头与论文当前清单均不含May15；不扩所有doc/code。IAB一次34s timeout后以公开源/iframe实取恢复，不把空SSR称零条，也不依赖搜索缓存。材料研发案例标题明确AIforScience暂缓；未读案例机制。MiniMax中文实redirect`https://www.minimax.cn/blog`13项May25→Apr27；Agent TechBlog三项Sep19/22/Oct8无更早分页，补足英文May26→March18的不同注册切片，未深读窗外正文。

Moonshot平台Blog完整26项但最新仍Nov2025，不声称其覆盖2026；官方组织一次`orgs/MoonshotAI/repos?sort=created&direction=desc&per_page=100&page=1`返回42元数据，目标附近createdMay22 kimi-code→Apr20 FlashKDA，没有May15新仓库。**repo created只支持该新资产目录，不等首次公开正文/旧仓库release覆盖**；旧repo相关May15事件仍有限恢复，不冒终态。Meta官方Blog当前两页已读、目标前后在June/April；publication筛选实链两次web超时，CLI同一精确入口在恢复，不把失败称没有论文。Google/Meta publication目标slice尚未签覆盖；本节是有界发现停止而非整日14行完成。

消费R34：14833 EASM的已有emotion/memory组合，A/B同时加所有信号、无staticfacts基线、30单persona/单session judge，未有新一般memory条件，关闭；14984 Sat3D已有tri-plane/DINO加俯视域gravity/depth/透视监督，未建立当前foundation/WM新接口条件，关闭，均非类型硬排。14912压力transition/修订理由证据/无压力undefined的评价合同保潜力，15116 randomref破首帧geometry泄漏且同LoRA移除此项的对照保潜力。消费R37：15054 FPS/CLIPgate+窗口聚合无新memory规则/通用可靠性条件，15181枚举judge筛样/可加/原图局部独立/删不可行子任务+topk verifier止于域内组合，具体关闭；14391 dual-bitstream冻结expertref/modulation和densegate消融保潜力，不等sparseLLM。原决定域与未披反侧均保root R34/37，不重复全读或为关闭追日期。

R36实际14937保存态POST通过，现15 I+1Only+1Dispute=17新增处置（README待本节后同步）；同184身份漏斗为35关闭、114潜力、35一次core未定。114中17已逐项处置、13909资格另1、96普通Source/日期；未冻结、不是114当窗候选或全量Deep任务。root另三core已交回，不再重复展开。

## A47 — 14893 covariance-tail必要Source与Books决定待独核

实际[exactv1](https://arxiv.org/html/2605.14893v1)§3–5/T1/F2–4和必要A/B的threshold/随机删除反侧，C只文字说明而未看像素；正文已足，停止代码/无关refs。Current只有v1、未见具名纠错撤回；[原DC](SUP_DC_2605.14893_20261019.json)唯一v1May14 14:37:50Z、arxiv.content/findable/registeredMay15 02:23:04Z，官方日程下界至上界全北京May15，非submitted或created充pub。

图/文各自centered empirical covariance，分别trace-normalize后取均值，按各模型elbow的最小值选统一约10^-3.6 cutoff，取tail特征向量V，两个modality同用P=I−VVᵀ投影；不是cross-covariance/CCA或正式signal/noise可辨识分解。mSCSA是principal-angle平方均值，反映校准子集子空间重叠而非因果“架构噪声”。1M LAION captions、ImageNet1.2M images和约250k实际成功下载LAION图；坏链接/placeholder偏置与估计数据改变“异常图”主题在原文保留，不能拿视觉挑样证明信息无用。每类小样本covariance的tail相关与全局tail高重叠也不证明所有消费者所需信息都在余空间。

T1六个backbone中CLIP-L768取164（21%）、SigLIP2-L1024取405（40%），不是所有CLIP固定164。仅ImageNet Top5与原LAION配对cos；CLIP-L91.2→91.1、SigLIP2-L89→88.4，故“完全无损/全是噪声”不成立；500次同维随机删方向作参考但自身剪裁未有重复seed/CI。配对cos增加可因共同投影/归一几何改变，不等retrieval ranking、识别细节、分割/VQA或生成消费提高。没有holdout数据校准split细节，阈值跨模型统一为启发式；A原样本cov与normalized-feature替代结果接近不授任意数据同阈值。硬件/precision/完整提特征与协方差预算ND，不采纯投影即可减encoder计算或部署加速。理论与modality-gap因果明确future work。

采用2+1+2=5、标准Source完成；潜在贡献是跨类/跨模态tail相似与有限裁剪反证，仍保候选，不因宣传“noise”过宽删分母。当前拟**仅报告**：它给特定校准/任务上的新测量，不足以改变书稿长期选择为“低方差共同tail可直接移除”。已实际比较Ch23的Modality Collapse完整论证：先covariance提出候选方向，另做消费者投影干预与不同训练目标，明确随机删除也能改善loss、方向人口不对称、原下游消费者单验；相邻head抑制段又明确局部检索收益不证明噪声/算量删除。本文不能替代这些资格，也未建立一个新的普适noise判定接口；不冒称旧稿已经包含本文平均cov/阈值方法或实测164。若有独立数据、更多消费者与保留细节/完整费用证据支持可复用裁剪条件，可只重开该条件和实际owner差额，不追全部后续应用。不是因为5分或省Books工作而Only；如root认为这份共同tail测量本身足以补长期局部诊断，则就具体命题协调，不预写。

## A48 — Octopus必要Source与正交中心命题争议（待独核）

实际[exactv1](https://arxiv.org/html/2605.14938v1)§3–5/Eq4–10/Alg1/T1–5及受影响I1/I3–5/Limitations；G1/T6与训练/评估定义必要核，G2已知caption metric公式非采用依据，不展开额外全部例图。current仅v1无具名纠错撤回；[原DC](SUP_DC_2605.14938_20261019.json)唯一v1May14 15:13:24Z、arxiv.content/findable/registeredMay15 02:24:11Z，公告下界至登记上界同北京May15。未看像素、核实现或复现。

真实新增提案：保存过去merged参数，在**当前task数据**上计算这些旧参数的loss梯度作为GPWC，再与新task增量作用；历史数据不需要，但历史weights/逐旧task反传需要。用最近merged checkpoint代全部历史是另一项经验proxy，把这部分O(tasks)成本降为O(1)不等历史信息被完整保留。先对全当前数据无约束训练stage1，再在小subset stage2加GPWC项与L2 norm项，stage1初始化来自上一stage1、stage2累计合并与其初始化有独立身份，不能把它压成一次普通梯度投影。

**中心命题冲突**：原Eq7/8是带符号`g_old-on-currentᵀ θ_new`，Eq10以正λ相加最小化，没有绝对值/平方，也没有硬投影。单独加L2的简化目标`λ1 gᵀθ+λ2||θ||²`最小点为`−λ1 g/(2λ2)`，一般反向而非正交；I1 toy段也解释为与task loss竞争达平衡，不消除这个差别。不擅改公式为平方来修论文。Eq5用“增量相对大基座小”忽略高阶项不能保证真实Hessian余项小；在旧task已局部最优时旧梯度本就零，一阶正交条件可能空泛。I1把loss写成expected gradient（Eq19/20）后使用scalar stationarity是记号冲突；即按scalar loss合理解释，`g=Hv`依赖可微极小值路径/适用Hessian，只识别一个v方向，不覆盖全部旧task敏感子空间。反例H=I、v=e1、Δ=e2时Δ⊥g却ΔᵀHΔ=1；“与GPWC正交→旧task无损”不由该论证推出。此为本项目解析反侧，不冒作者已承认。

LLaVA1.5-7B全部language linear加LoRA，batch16/1epoch、4×H20/P800（没给各表唯一硬件/precision/synchronization/CI）；rank48/alpha96仅I5参数图口径，不当全文所有baseline配置。UCIT6task T1最后均分71.01相对HiDe64.19，Avg71.08<联合72.53，多个单项仍低于联合/别method；T2 GPWC胜历史数据梯度、T3两阶段胜单阶段是局部配方证据，不能唯一归真实正交或不需任何历史状态。T4过强norm提高BWT但损新task，T5三种task顺序Last71.01/69.04/69.16不证order invariance；原文Limitations承认task容量上限、同域不同问题可退化。Stage2 subset比例/全部trainsteps/旧checkpoint及GPWC缓存精确预算ND。推理可merge成一个LoRA不消除训练保存/提梯度/双阶段/调参和保留能力回归费用。

2+1+2=5，中心“history-free gradient orthogonalization”争议/拟暂缓，不反删候选或降为pre-filter排除。完整必要方法/实测与关键反证已读，不是普通Source欠账或因代码未看列外部受阻。当前不采无损/真实正交/全部旧敏感方向保证，也不把局部表分数当可执行保留协议。重开只需精确loss/其优化对象的官方更正或可核的实现定义及相应配对消融、旧任务保留与完整预算，先核Eq7/8/10/I1而不重所有任务。实际Ch30 OLoRA/forward正交补段、SafeAnchor最终step段完整比较，以及Ch29/31训练目标交接；旧稿已经要求参数方向≠行为无损、raw-gradient≠最终step，但没有替本文signed proxy补正交资格。由于拟采用的正交接口本身不成立，不为新名字另加一个正面historyfree机制段；若只保本文实验上下文，可报告而非Books。

## A49 — 具体澄清事件与来源尾增量

实际完整读表外[MSR May15澄清](https://www.microsoft.com/en-us/research/blog/further-notes-on-our-recent-research-on-ai-delegation-and-long-horizon-reliability/)核心：roundtrip semantic-fidelity非task completion/用户结果、简化工具harness非production、有限人类介入、Python平均<1%与其他任务19–34%/20轮。其明确链接旧家族2604.15597，不重新取得旧论文归属/评分；官方澄清为May15事件，但没有新增实验人口/独立verification方法或纠正既有机制，只重申原测量权限。实际Ch66两完整段已明确forward/inverse/noop/errorcancel/domainparser、非逐token损失与非所有agent，故本次**具体贡献关闭、不评分**：不是因为“Books已有主题”就排除有意义新反证，而是该公告没有新增被披露的反证/机制。没有追全部旧外链。root可审这一具名拒绝，若发现公告实际纠正旧结论，仅恢复对应句。

Meta publication CLI HTTP200恢复后实际解析首页与page2/3；每页前12条2026时间序列、后12条旧年份重复混排，不能把整页视时间排序。Page2 current序列October2→July17，Page3 July3→April14，目标两侧May17 GIM→May12 NeuralSet，无May15 current条目；只在这段核标题和日期，不打开窗外全文或将旧混排项目变队列。此前webtimeout没有授终态，已用可执行解析补好这一有限publication slice；当前Blog两页与官方publication目标slice分别记录，不声称整个Meta互联网无遗漏。MiMo日期头实际恢复见A46，无需继续IAB timeout。

R39实际14893 Source/日期/具体Only通过，README已同步15I+2Only+1争议=18新增已处置。R38的14420在问卷H0筛人口/CoT/现成GRPO无新一般优化条件，具体贡献关闭；14594 query聚合无序pointcloud→固定coarse template vertex/graph消费者保潜力，后只核对应encoder对照/目标身份与fixed topology代价。35→36关闭、114→115潜力、35→33一次core；184口径不变，其中18已独核处置、13909资格1、其余96普通Source/日期。14938本节仅作者必要Source已备，未计独核处置。

## A50 — SteerSeg必要Source与actual owner逐字PRE

实际[exactv1](https://arxiv.org/html/2605.14908v1)§3/Eq1–6、§4/T1–2、§5/T3–4、§7与A诊断/B–C prompt/D配置；未看E图像，不遍历代码。Current仅v1无具名纠错撤回。[DC](SUP_DC_2605.14908_20261019.json)唯一v1May14 14:42:15Z、arxiv.content/findable/registeredMay15 02:23:28Z，公告下界至上界完整北京May15。

冻结LVLM+SAM2，不训练feature或mask decoder而只学64 softprompt；用head平均+residual attention rollout的response-token→visual行作空间图，以真实mask的BCE/Dice监督prompt。原文先说append后说prepend，故不自行给精确顺序recipe；采用的是输入condition改变被消费readout而非直接改attention权重/认定其因果解释。单独一轮无softprompt的CoT提属性再加入用于生成descriptor的prompt；16逐frame/8联合video低分辨率双路rollout，argmax点→SAM2、IoU.7 NMS→双向tracklets，再以两路attention与mask-logit Pearson相关α.3选择，不是独立真值检验。mask取logit在0/1端点的epsilon与Pearson零variance处理ND，不授完整数值recipe。

训练仅RefYouTubeVOS有像素mask，6500step/effectivebatch4/lr5e-4/AdamW、2A6000，表D rollout14–27，seed文字embedding重复截断初始化而非随机。32/64/128prompt消融并非越多越好。T3四组合控制CoT/soft，DAVIS65.7→软80.9→全81.4，ReasonVOS60.6→64.1→65.9，支持局部readout适配，不保证原reasoning函数不变。132随机case的人类attribute判读True/False/Skip没有给annotator数/一致性、mask成功阈值细节，115“正确理解”与55.7%mask准确只作该人口诊断，不能推attention唯一瓶颈或reasoning必要充分。T1 InternVL RefDAVIS66.1低于LocHead66.3，T2 RefYouTubeVOS67.9低于训练VRS70.4；跨不同底模/不同训练的联合排行不证冻结方法普遍更强。短暂对象可能漏keyframes，α本来要按域/底模调，不保证通用迁移。完整precision/seedCI/端到端time/显存ND，全部mask标签、训练、attribute多次LVLM、rollout矩阵、keyframes/所有SAM候选和ranking计费；冻结权重不等trainingfree/原能力保持。必要机制与关键反侧已足。

2+1+2=5，具体readout缺口深入。实际owner MULTIMODAL-REPRESENTATION Ch23已完整读PR-MaGIC→ProtoTTA及前类别校准的交接、Ch22/24邻章入口；现PR-MaGIC是test-time搜索query embedding却让decoder读原feature，未承载**离线用mask监督softprompt，使原LVLM attention rollout成为可训练的空间控制读出**，不复制Ch24生成或Ch26行动。拟唯一段放PR-MaGIC完整段后→ProtoTTA前：

> 空间控制信号也可在离线训练中塑形，而不为每个query搜索新feature：冻结LVLM与分割器，只用真实mask监督输入soft prompts，使response-token的attention rollout对齐目标，再把峰值点和候选tracklets交给分割器。[受限视频分割对照](https://arxiv.org/html/2605.14908v1)支持这种读出适配，但attention已成为受监督的控制接口，不再是未经训练的解释或独立grounding证据；同一attention再给候选打分也不增加独立真值。冻结原权重没有冻结输入函数，不能认证原reasoning无损。短暂目标可漏采，部分任务仍退步；像素标注、prompt训练、属性生成、rollout与全部分割候选都计费。读出、覆盖或预算失配时，保原表示与prompt、专用dense head和真实局部监督，不让更集中的热图替代像素与原任务验收。<!-- source-family:SF-2026-ARXIV-2605-14908 -->

本人注拟：SF-2026-ARXIV-2605-14908 — exactv1§3–5/Eq1–6/T1–4/§7与必要A–D，2+1+2=5，仅mask监督softprompt→attention rollout控制读出差额。保attention非因果/独立证据、冻结权重非函数不变、同源ranking、原输入顺序/数值边界未闭、短目标漏采/任务反退及全部标签/训练/推理费；未核实现/像素/复现。

## A51 — MHSA必要Source与具体仅报告判断（待独核）

实际[exactv1](https://arxiv.org/html/2605.14966v1)§3/Eq1–12、§4/T1–6、A执行费用/B架构/C超参/D人口，已读E开头敏感性设置不采其全部显著性图；I/J attention可视化不作因果证明，停止。Current只有v1无具名纠错撤回。[新DC](SUP_DC_2605.14966_20261019.json)唯一v1May14 15:31:18Z、arxiv.content/findable/registeredMay15 02:24:54Z，下界至上界同北京May15。

固定336²/视觉token数，将所有layer×head×visual的attention展平，由三层d→512→512→d MLP提出residual ΔA，DHCP二层MLP作trigger/判别监督；POPE联训detector小lr+G，目标含判别CE、ΔA平方与真实输出labelCE，骨干参数冻结。Caption改CHAIR whitelist名词token标签，离线preextract attention训练，不包含LVLM CE。因而不是统一有groundtruth质量约束、支持任意幻觉token或无训练插件。attention A+ΔA未明确非负/归一/跨层重算与cache的可执行hook，不能把它当已验证标准softmax attention替换；§3.6明确先取原forward再recompute logits，不授单pass。

POPE N3000的题目80/20按question ID split（seed42），没有image-disjoint声明；主T1表又写N3000、D多万attention训练样本单位不同于question，不能自行认定是600独立holdout或全3000未泄漏测试。保这份评价人口口径限制，不虚构已证leakage。跨dataset矩阵COCO/Obj365是较明确有限迁移证据，跨model各需重训，不等一G通用。T1 F1改善但precision95.27→92.54，Yes%40.9→50.5；caption CHAIR下降伴Recall86.63→83.28/56.42→55.14。T6去LVLM CE 84.18低于baseline85.55，说明仅迎合detector不够；caption恰无该项，不能以POPE三目标消融给caption同保证。

A实测H20/Qwen7B/1000POPE mean113.1→161.2ms、8.84→6.20sample/s，trigger12.3%样本mean486.4/median205.5ms；不把“only0.43×额外”或小MLP名称当低tail/免费，现实trigger更低只是推测。由B的d和512结构，G主线性权重约1024d+262144，LLaVA d589824约604M、Qwen d112896约116M，不是三层就固定小参数；这是本项目计算非作者独立实测。精度/完整batch/concurrency/SLO与训练硬件逐表口径ND；保存attention、detector/生成器训练、两pass/被触发时重算、完整下游/旧能力回归都计费，未核实现或复现。

2+1+2=5标准Source并对执行/评价反侧必要深入。拟**仅报告**，仍保候选：实测支持特定形状下的learned attention-repair提案，但新长期选择所需的替换语义/泛化消费者及完整对照人口未闭。实际Ch23完整读现有条件probe→只在冲突时抑制head两段、后模态来源权，以及attention-spectrum sensor段；这些正文已承担检测不等真值、局部纠偏不能取代独立事实/旧能力回归的选择。本文的d维MLP方法并非已被旧稿实现或等价覆盖，但尚不足以升级成另一个可复用无损纠偏协议；不为每份attention变体追加案例。重开只需具体replacement执行/归一与独立人口/质量总费证据，再比较学习型full-map修复是否确改现有局部head干预选择，非无差别重跑附件或因5分自动Only。

## A52 — 未冻结潜力与一次core精确定位（供贡献剪枝）

root R40 Octopus中心争议安全终态通过后，184身份机械守恒为36明确关闭、33一次core、19新增已逐项独核处置、13909日期资格另1、95潜在增量未独核终结。此前96在加入14938后减为95；其中14908/14966作者必要Source已备待root，其他93仍先按具体贡献/必要证据决定投入，**不是95当窗确定候选或逐项全文队列**。这份定位只让有界准入可复查；题摘对象编号从1计，不混入邻日结论。作者正处理14461/14561/14563三个一次core，其余可由root有界剪枝，避免重复。R41 MSR澄清具体贡献关闭只属表外新增发现，不混入这个184身份统计；旧15597不搬动。

### 潜在增量95项（不是确定候选；14908/14966必要Source已备）
- 13866 — AI Alignment Amplifies the Role of Race, Gender, and Disability in Hiring Decisions；[SUP_ABSTRACT_Q2_20261019.json 第1对象](SUP_ABSTRACT_Q2_20261019.json)
- 13989 — VectraYX-Nano: A 42M-Parameter Spanish Cybersecurity Language Model with Curriculum Learning and Native Tool Use；[SUP_ABSTRACT_B5_20261019.json 第3对象](SUP_ABSTRACT_B5_20261019.json)
- 14040 — Physics-R1: An Audited Olympiad Corpus and Recipe for Visual Physics Reasoning；[SUP_ABSTRACT_B5_20261019.json 第4对象](SUP_ABSTRACT_B5_20261019.json)
- 14063 — Reliability-Gated Source Anchoring for Continual Test-Time Adaptation；[SUP_ABSTRACT_Q2_20261019.json 第2对象](SUP_ABSTRACT_Q2_20261019.json)
- 14097 — Real-Time Group Dynamics with LLM Facilitation: Evidence from a Charity Allocation Task；[SUP_ABSTRACT_B5_20261019.json 第6对象](SUP_ABSTRACT_B5_20261019.json)
- 14141 — Distribution-Aware Algorithm Design with LLM Agents；[SUP_ABSTRACT_B5_20261019.json 第7对象](SUP_ABSTRACT_B5_20261019.json)
- 14201 — MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving；[SUP_ABSTRACT_B5_20261019.json 第8对象](SUP_ABSTRACT_B5_20261019.json)
- 14205 — SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents；[SUP_ABSTRACT_B5_20261019.json 第9对象](SUP_ABSTRACT_B5_20261019.json)
- 14211 — ASH: Agents that Self-Hone via Embodied Learning；[SUP_ABSTRACT_B1_20261019.json 第8对象](SUP_ABSTRACT_B1_20261019.json)
- 14306 — Towards Recursive Self-Evolving Agentic Literature Retrieval；[SUP_ABSTRACT_B5_20261019.json 第11对象](SUP_ABSTRACT_B5_20261019.json)
- 14311 — Beyond Binary: Reframing GUI Critique as Continuous Semantic Alignment；[SUP_ABSTRACT_Q2_20261019.json 第4对象](SUP_ABSTRACT_Q2_20261019.json)
- 14323 — Dynamic Latent Routing；[SUP_ABSTRACT_Q2_20261019.json 第5对象](SUP_ABSTRACT_Q2_20261019.json)
- 14333 — InsightTok: Improving Text and Face Fidelity in Discrete Tokenization for Autoregressive Image Generation；[SUP_ABSTRACT_Q2_20261019.json 第6对象](SUP_ABSTRACT_Q2_20261019.json)
- 14340 — Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR；[SUP_ABSTRACT_B1_20261019.json 第9对象](SUP_ABSTRACT_B1_20261019.json)
- 14347 — Exemplar Partitioning for Mechanistic Interpretability；[SUP_ABSTRACT_Q2_20261019.json 第7对象](SUP_ABSTRACT_Q2_20261019.json)
- 14350 — Distributionally Robust Multi-Task Reinforcement Learning via Adaptive Task Sampling；[SUP_ABSTRACT_B1_20261019.json 第10对象](SUP_ABSTRACT_B1_20261019.json)
- 14358 — Uncovering the Representation Geometry of Minimal Cores in Overcomplete Reasoning Traces；[SUP_ABSTRACT_B1_20261019.json 第11对象](SUP_ABSTRACT_B1_20261019.json)
- 14364 — MoRe: Modular Representations for Principled Continual Representation Learning on Sequential Data；[SUP_ABSTRACT_Q2_20261019.json 第8对象](SUP_ABSTRACT_Q2_20261019.json)
- 14373 — Turning Stale Gradients into Stable Gradients: Coherent Coordinate Descent with Implicit Landscape Smoothing for Lightweight Zeroth-Order Optimization；[SUP_ABSTRACT_Q2_20261019.json 第9对象](SUP_ABSTRACT_Q2_20261019.json)
- 14379 — Data-Augmented Game Starts for Accelerating Self-Play Exploration in Imperfect Information Games；[SUP_ABSTRACT_Q2_20261019.json 第10对象](SUP_ABSTRACT_Q2_20261019.json)
- 14381 — NodeSynth: Socially Aligned Synthetic Data for AI Evaluation；[SUP_ABSTRACT_Q2_20261019.json 第11对象](SUP_ABSTRACT_Q2_20261019.json)
- 14382 — Delta Forcing: Trust Region Steering for Interactive Autoregressive Video Generation；[SUP_ABSTRACT_Q2_20261019.json 第12对象](SUP_ABSTRACT_Q2_20261019.json)
- 14386 — Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning；[SUP_ABSTRACT_B1_20261019.json 第14对象](SUP_ABSTRACT_B1_20261019.json)
- 14391 — Dual-Latent Collaborative Decoding for Fidelity-Perception Balanced Image Compression；[SUP_ABSTRACT_Q2_20261019.json 第13对象](SUP_ABSTRACT_Q2_20261019.json)
- 14398 — ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction；[SUP_ABSTRACT_B1_20261019.json 第15对象](SUP_ABSTRACT_B1_20261019.json)
- 14418 — The Great Pretender: A Stochasticity Problem in LLM Jailbreak；[SUP_ABSTRACT_B2_20261019.json 第1对象](SUP_ABSTRACT_B2_20261019.json)
- 14423 — Collaborative Yet Personalized Policy Training: Single-Timescale Federated Actor-Critic；[SUP_ABSTRACT_Q2_20261019.json 第16对象](SUP_ABSTRACT_Q2_20261019.json)
- 14443 — Prompting Policies for Multi-step Reasoning and Tool-Use in Black-box LLMs with Iterative Distillation of Experience；[SUP_ABSTRACT_B2_20261019.json 第2对象](SUP_ABSTRACT_B2_20261019.json)
- 14448 — Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture；[SUP_ABSTRACT_B2_20261019.json 第3对象](SUP_ABSTRACT_B2_20261019.json)
- 14450 — Stop Overthinking: Unlocking Efficient Listwise Reranking with Minimal Reasoning；[SUP_ABSTRACT_B2_20261019.json 第4对象](SUP_ABSTRACT_B2_20261019.json)
- 14465 — From Table to Cell: Attention for Better Reasoning with TABALIGN；[SUP_ABSTRACT_B2_20261019.json 第6对象](SUP_ABSTRACT_B2_20261019.json)
- 14475 — GeoVista: Visually Grounded Active Perception for Vision-Language Understanding of Ultra-High-Resolution Remote Sensing Images；[SUP_ABSTRACT_B6_20261019.json 第5对象](SUP_ABSTRACT_B6_20261019.json)
- 14487 — Head Forcing: Long Autoregressive Video Generation via Head Heterogeneity；[SUP_ABSTRACT_Q2_20261019.json 第17对象](SUP_ABSTRACT_Q2_20261019.json)
- 14513 — HEART: Exploiting Head Heterogeneity in Sparse Attention for Video Diffusion；[SUP_ABSTRACT_B2_20261019.json 第8对象](SUP_ABSTRACT_B2_20261019.json)
- 14517 — Dimension-Level Intent Fidelity Evaluation for Large Language Models: Evidence from Structured Prompt Ablation；[SUP_ABSTRACT_B2_20261019.json 第9对象](SUP_ABSTRACT_B2_20261019.json)
- 14521 — Enjoy Your Layer Normalization with the Computational Efficiency of RMSNorm；[SUP_ABSTRACT_Q2_20261019.json 第18对象](SUP_ABSTRACT_Q2_20261019.json)
- 14530 — Mitigating Mask Prior Drift and Positional Attention Collapse in Large Diffusion Vision-Language Models；[SUP_ABSTRACT_B2_20261019.json 第10对象](SUP_ABSTRACT_B2_20261019.json)
- 14531 — Language Generation as Optimal Control: Closed-Loop Diffusion in Latent Control Space；[SUP_ABSTRACT_B2_20261019.json 第11对象](SUP_ABSTRACT_B2_20261019.json)
- 14549 — CSLibPremiseBench: Structure-Guided Premise Retrieval and Label Robustness for Lean 4 Computer-Science Theorems；[SUP_ABSTRACT_B2_20261019.json 第13对象](SUP_ABSTRACT_B2_20261019.json)
- 14553 — Efficient Multi-objective Prompt Optimization via Pure-exploration Bandits；[SUP_ABSTRACT_Q2_20261019.json 第19对象](SUP_ABSTRACT_Q2_20261019.json)
- 14558 — Resolving Action Bottleneck: Agentic Reinforcement Learning Informed by Token-Level Energy；[SUP_ABSTRACT_B2_20261019.json 第14对象](SUP_ABSTRACT_B2_20261019.json)
- 14571 — Let Robots Feel Your Touch: Visuo-Tactile Cortical Alignment for Embodied Mirror Resonance；[SUP_ABSTRACT_Q2_20261019.json 第20对象](SUP_ABSTRACT_Q2_20261019.json)
- 14581 — A Picture is Worth a Thousand Words? An Empirical Study of Aggregation Strategies for Visual Financial Document Retrieval；[SUP_ABSTRACT_B3_20261019.json 第2对象](SUP_ABSTRACT_B3_20261019.json)
- 14594 — TOPOS: High-Fidelity and Efficient Industry-Grade 3D Head Generation；[SUP_ABSTRACT_Q2_20261019.json 第21对象](SUP_ABSTRACT_Q2_20261019.json)
- 14598 — DSSP: Diffusion State Space Policy with Full-History Encoding；[SUP_ABSTRACT_B3_20261019.json 第3对象](SUP_ABSTRACT_B3_20261019.json)
- 14599 — Fast Rates for Inverse Reinforcement Learning；[SUP_ABSTRACT_B6_20261019.json 第13对象](SUP_ABSTRACT_B6_20261019.json)
- 14604 — Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks；[SUP_ABSTRACT_B6_20261019.json 第14对象](SUP_ABSTRACT_B6_20261019.json)
- 14619 — SliceGraph: Mapping Process Isomers in Multi-Run Chain-of-Thought Reasoning；[SUP_ABSTRACT_B3_20261019.json 第4对象](SUP_ABSTRACT_B3_20261019.json)
- 14634 — Documentation-Guided Agentic Codebase Migration from C to Rust；[SUP_ABSTRACT_B3_20261019.json 第5对象](SUP_ABSTRACT_B3_20261019.json)
- 14635 — MultiEmo-Bench: Multi-label Visual Emotion Analysis for Multi-modal Large Language Models；[SUP_ABSTRACT_B3_20261019.json 第6对象](SUP_ABSTRACT_B3_20261019.json)
- 14663 — Optimal Asymptotic Rates for (Stochastic) Gradient Descent under the Local PL-Condition: A Geometric Approach；[SUP_ABSTRACT_Q2_20261019.json 第23对象](SUP_ABSTRACT_Q2_20261019.json)
- 14664 — MiVE: Multiscale Vision-language features for reference-guided video Editing；[SUP_ABSTRACT_B3_20261019.json 第7对象](SUP_ABSTRACT_B3_20261019.json)
- 14696 — EponaV2: Driving World Model with Comprehensive Future Reasoning；[SUP_ABSTRACT_B3_20261019.json 第9对象](SUP_ABSTRACT_B3_20261019.json)
- 14709 — Breaking Dual Bottlenecks: Evolving Unified Multimodal Models into Self-Adaptive Interleaved Visual Reasoners；[SUP_ABSTRACT_B3_20261019.json 第11对象](SUP_ABSTRACT_B3_20261019.json)
- 14712 — IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation；[SUP_ABSTRACT_B3_20261019.json 第12对象](SUP_ABSTRACT_B3_20261019.json)
- 14727 — CHASM: Cross-frequency Harmonized Axis-Separable Mixing for Spectral Token Operators；[SUP_ABSTRACT_Q2_20261019.json 第24对象](SUP_ABSTRACT_Q2_20261019.json)
- 14742 — EARL: Towards a Unified Analysis-Guided Reinforcement Learning Framework for Egocentric Interaction Reasoning and Pixel Grounding；[SUP_ABSTRACT_B3_20261019.json 第13对象](SUP_ABSTRACT_B3_20261019.json)
- 14746 — Selective Safety Steering via Value-Filtered Decoding；[SUP_ABSTRACT_Q2_20261019.json 第25对象](SUP_ABSTRACT_Q2_20261019.json)
- 14749 — Non-linear Interventions on Large Language Models；[SUP_ABSTRACT_B3_20261019.json 第14对象](SUP_ABSTRACT_B3_20261019.json)
- 14750 — EVA: Editing for Versatile Alignment against Jailbreaks；[SUP_ABSTRACT_Q2_20261019.json 第26对象](SUP_ABSTRACT_Q2_20261019.json)
- 14766 — Streaming Speech-to-Text Translation with a SpeechLLM；[SUP_ABSTRACT_B3_20261019.json 第15对象](SUP_ABSTRACT_B3_20261019.json)
- 14787 — Do Composed Image Retrieval Benchmarks Require Multimodal Composition?；[SUP_ABSTRACT_B4_20261019.json 第2对象](SUP_ABSTRACT_B4_20261019.json)
- 14801 — Exploring Bottlenecks in VLM-LLM Navigation: How 3D Scene Understanding Capability Impacts Zero-Shot VLN；[SUP_ABSTRACT_B4_20261019.json 第3对象](SUP_ABSTRACT_B4_20261019.json)
- 14830 — Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence from Alibaba's Customer Service Operations；[SUP_ABSTRACT_B4_20261019.json 第5对象](SUP_ABSTRACT_B4_20261019.json)
- 14842 — Editor's Choice: Evaluating Abstract Intent in Image Editing through Atomic Entity Analysis；[SUP_ABSTRACT_Q2_20261019.json 第29对象](SUP_ABSTRACT_Q2_20261019.json)
- 14843 — MechVerse: Evaluating Physical Motion Consistency in Video Generation Models；[SUP_ABSTRACT_Q2_20261019.json 第30对象](SUP_ABSTRACT_Q2_20261019.json)
- 14860 — A Non-Monotone Preconditioned Trust-Region Method for Neural Network Training；[SUP_ABSTRACT_Q2_20261019.json 第31对象](SUP_ABSTRACT_Q2_20261019.json)
- 14868 — Fast Adversarial Attacks with Gradient Prediction；[SUP_ABSTRACT_Q2_20261019.json 第32对象](SUP_ABSTRACT_Q2_20261019.json)
- 14876 — Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning；[SUP_ABSTRACT_B4_20261019.json 第8对象](SUP_ABSTRACT_B4_20261019.json)
- 14877 — HeatKV: Head-tuned KV-cache Compression for Visual Autoregressive Modeling；[SUP_ABSTRACT_Q2_20261019.json 第33对象](SUP_ABSTRACT_Q2_20261019.json)
- 14891 — Hierarchical Image Tokenization for Multi-Scale Image Super Resolution；[SUP_ABSTRACT_Q2_20261019.json 第34对象](SUP_ABSTRACT_Q2_20261019.json)
- 14894 — SEDiT: Mask-Free Video Subtitle Erasure via One-step Diffusion Transformer；[SUP_ABSTRACT_B7_20261019.json 第15对象](SUP_ABSTRACT_B7_20261019.json)
- 14908 — SteerSeg: Attention Steering for Reasoning Video Segmentation；[SUP_ABSTRACT_B4_20261019.json 第12对象](SUP_ABSTRACT_B4_20261019.json)
- 14912 — From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement；[SUP_ABSTRACT_Q2_20261019.json 第35对象](SUP_ABSTRACT_Q2_20261019.json)
- 14935 — Multi-scale Coarse-to-fine Modeling for Test-time Human Motion Control；[SUP_ABSTRACT_Q2_20261019.json 第36对象](SUP_ABSTRACT_Q2_20261019.json)
- 14948 — ACE-LoRA: Adaptive Orthogonal Decoupling for Continual Image Editing；[SUP_ABSTRACT_Q2_20261019.json 第38对象](SUP_ABSTRACT_Q2_20261019.json)
- 14950 — Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model；[SUP_ABSTRACT_B8_20261019.json 第4对象](SUP_ABSTRACT_B8_20261019.json)
- 14966 — MHSA: A Lightweight Framework for Mitigating Hallucinations via Steered Attention in LVLMs；[SUP_ABSTRACT_B8_20261019.json 第5对象](SUP_ABSTRACT_B8_20261019.json)
- 14967 — InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting；[SUP_ABSTRACT_Q2_20261019.json 第39对象](SUP_ABSTRACT_Q2_20261019.json)
- 14988 — Compositional Video Generation via Inference-Time Guidance；[SUP_ABSTRACT_B8_20261019.json 第6对象](SUP_ABSTRACT_B8_20261019.json)
- 15000 — Quantifying and Mitigating Premature Closure in Frontier LLMs；[SUP_ABSTRACT_B8_20261019.json 第7对象](SUP_ABSTRACT_B8_20261019.json)
- 15012 — Boosting Reinforcement Learning with Verifiable Rewards via Randomly Selected Few-Shot Guidance；[SUP_ABSTRACT_B8_20261019.json 第8对象](SUP_ABSTRACT_B8_20261019.json)
- 15019 — From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG；[SUP_ABSTRACT_B8_20261019.json 第11对象](SUP_ABSTRACT_B8_20261019.json)
- 15040 — Orchard: An Open-Source Agentic Modeling Framework；[SUP_ABSTRACT_B8_20261019.json 第13对象](SUP_ABSTRACT_B8_20261019.json)
- 15044 — SpeakerLLM: A Speaker-Specialized Audio-LLM for Speaker Understanding and Verification Reasoning；[SUP_ABSTRACT_B8_20261019.json 第14对象](SUP_ABSTRACT_B8_20261019.json)
- 15082 — Average Gradient Outer Product in kernel regression provably recovers the central subspace for multi-index models；[SUP_ABSTRACT_B7_20261019.json 第17对象](SUP_ABSTRACT_B7_20261019.json)
- 15104 — From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents；[SUP_ABSTRACT_B8_20261019.json 第17对象](SUP_ABSTRACT_B8_20261019.json)
- 15116 — DriveCtrl: Conditioned Sim-to-Real Driving Video Generation；[SUP_ABSTRACT_Q2_20261019.json 第44对象](SUP_ABSTRACT_Q2_20261019.json)
- 15131 — Natural Synthesis: Outperforming Reactive Synthesis Tools with Large Reasoning Models；[SUP_ABSTRACT_B8_20261019.json 第18对象](SUP_ABSTRACT_B8_20261019.json)
- 15182 — Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video；[SUP_ABSTRACT_Q2_20261019.json 第46对象](SUP_ABSTRACT_Q2_20261019.json)
- 15183 — When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability；[SUP_ABSTRACT_Q2_20261019.json 第47对象](SUP_ABSTRACT_Q2_20261019.json)
- 15193 — Aligning Latent Geometry for Spherical Flow Matching in Image Generation；[SUP_ABSTRACT_Q2_20261019.json 第48对象](SUP_ABSTRACT_Q2_20261019.json)
- 15196 — RefDecoder: Enhancing Visual Generation with Conditional Video Decoding；[SUP_ABSTRACT_Q2_20261019.json 第49对象](SUP_ABSTRACT_Q2_20261019.json)
- 15198 — ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both；[SUP_ABSTRACT_B8_20261019.json 第21对象](SUP_ABSTRACT_B8_20261019.json)
- 15199 — EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation；[SUP_ABSTRACT_Q2_20261019.json 第50对象](SUP_ABSTRACT_Q2_20261019.json)

### 一次贡献决定域33项（非全文队列）
- 13872 — S-AI-Recursive: Convergent Recursive Reasoning；[SUP_ABSTRACT_B5_20261019.json 第1对象](SUP_ABSTRACT_B5_20261019.json)
- 14057 — Dual Hierarchical Dialogue Policy Learning for Legal Inquisitive Conversational Agents；[SUP_ABSTRACT_B5_20261019.json 第5对象](SUP_ABSTRACT_B5_20261019.json)
- 14259 — Hypergraph Enterprise Agentic Reasoner over Heterogeneous Business Systems；[SUP_ABSTRACT_B5_20261019.json 第10对象](SUP_ABSTRACT_B5_20261019.json)
- 14322 — TeachArena: Are Language Agents Ready for Realistic Teaching Work?；[SUP_ABSTRACT_B5_20261019.json 第12对象](SUP_ABSTRACT_B5_20261019.json)
- 14355 — Herculean: An Agentic Benchmark for Financial Intelligence；[SUP_ABSTRACT_B5_20261019.json 第13对象](SUP_ABSTRACT_B5_20261019.json)
- 14396 — Systematic Discovery of Semantic Attacks in Online Map Construction through Conditional Diffusion；[SUP_ABSTRACT_B5_20261019.json 第15对象](SUP_ABSTRACT_B5_20261019.json)
- 14401 — Agentic Recommender System with Hierarchical Belief-State Memory；[SUP_ABSTRACT_B6_20261019.json 第1对象](SUP_ABSTRACT_B6_20261019.json)
- 14431 — FuzzAgent: Multi-Agent System for Evolutionary Library Fuzzing；[SUP_ABSTRACT_B6_20261019.json 第2对象](SUP_ABSTRACT_B6_20261019.json)
- 14434 — Efficient Generative Retrieval for E-commerce Search with Semantic Cluster IDs and Expert-Guided RL；[SUP_ABSTRACT_B6_20261019.json 第3对象](SUP_ABSTRACT_B6_20261019.json)
- 14461 — ClickRemoval: An Interactive Open-Source Tool for Object Removal in Diffusion Models；[SUP_ABSTRACT_B2_20261019.json 第5对象](SUP_ABSTRACT_B2_20261019.json)
- 14495 — Contestable Multi-Agent Debate with Arena-based Argumentative Computation for Multimedia Verification；[SUP_ABSTRACT_B6_20261019.json 第6对象](SUP_ABSTRACT_B6_20261019.json)
- 14497 — ROAD: Adaptive Data Mixing for Offline-to-Online Reinforcement Learning via Bi-Level Optimization；[SUP_ABSTRACT_B6_20261019.json 第7对象](SUP_ABSTRACT_B6_20261019.json)
- 14504 — When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution；[SUP_ABSTRACT_B6_20261019.json 第8对象](SUP_ABSTRACT_B6_20261019.json)
- 14524 — Large Dimensional Kernel Ridge Regression: Extending to Product Kernels；[SUP_ABSTRACT_B7_20261019.json 第1对象](SUP_ABSTRACT_B7_20261019.json)
- 14537 — Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining；[SUP_ABSTRACT_B6_20261019.json 第9对象](SUP_ABSTRACT_B6_20261019.json)
- 14561 — Prompt Segmentation and Annotation Optimisation: Controlling LLM Behaviour via Optimised Segment-Level Annotations；[SUP_ABSTRACT_B2_20261019.json 第15对象](SUP_ABSTRACT_B2_20261019.json)
- 14563 — Remember Your Trace: Memory-Guided Long-Horizon Agentic Framework for Consistent and Hierarchical Repository-Level Code Documentation；[SUP_ABSTRACT_B3_20261019.json 第1对象](SUP_ABSTRACT_B3_20261019.json)
- 14587 — Angel or Demon: Investigating the Plasticity Interventions' Impact on Backdoor Threats in Deep Reinforcement Learning；[SUP_ABSTRACT_B6_20261019.json 第12对象](SUP_ABSTRACT_B6_20261019.json)
- 14704 — SceneFunRI: Reasoning the Invisible for Task-Driven Functional Object Localization；[SUP_ABSTRACT_B3_20261019.json 第10对象](SUP_ABSTRACT_B3_20261019.json)
- 14758 — Probabilistic Verification of Recurrent Neural Networks for Single and Multi-Agent Reinforcement Learning；[SUP_ABSTRACT_B7_20261019.json 第6对象](SUP_ABSTRACT_B7_20261019.json)
- 14771 — MediaClaw: Multimodal Intelligent-Agent Platform Technical Report；[SUP_ABSTRACT_B4_20261019.json 第1对象](SUP_ABSTRACT_B4_20261019.json)
- 14779 — Peng's Q($λ$) for Conservative Value Estimation in Offline Reinforcement Learning；[SUP_ABSTRACT_B7_20261019.json 第7对象](SUP_ABSTRACT_B7_20261019.json)
- 14802 — A Heterogeneous Temporal Memory Governance Framework for Long-Term LLM Persona Consistency；[SUP_ABSTRACT_B4_20261019.json 第4对象](SUP_ABSTRACT_B4_20261019.json)
- 14809 — GFMate: Empowering Graph Foundation Models with Test-time Prompt Tuning；[SUP_ABSTRACT_B7_20261019.json 第8对象](SUP_ABSTRACT_B7_20261019.json)
- 14845 — Exploring Vision-Language Models for Online Signature Verification: A Zero-Shot Capability Study；[SUP_ABSTRACT_B7_20261019.json 第10对象](SUP_ABSTRACT_B7_20261019.json)
- 14846 — Successive convex optimization for transformer encoder model predictive control；[SUP_ABSTRACT_B8_20261019.json 第2对象](SUP_ABSTRACT_B8_20261019.json)
- 14866 — Towards In-Depth Root Cause Localization for Microservices with Multi-Agent Recursion-of-Thought；[SUP_ABSTRACT_B7_20261019.json 第13对象](SUP_ABSTRACT_B7_20261019.json)
- 14890 — Tokenizer Fertility and Zero-Shot Performance of Foundation Models on Ukrainian Legal Text: A Comparative Study；[SUP_ABSTRACT_B7_20261019.json 第14对象](SUP_ABSTRACT_B7_20261019.json)
- 14892 — Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems；[SUP_ABSTRACT_B4_20261019.json 第9对象](SUP_ABSTRACT_B4_20261019.json)
- 14897 — Critic-Driven Voronoi-Quantization for Distilling Deep RL Policies to Explainable Models；[SUP_ABSTRACT_B7_20261019.json 第16对象](SUP_ABSTRACT_B7_20261019.json)
- 14907 — KGPFN: Unlocking the Potential of Knowledge Graph Foundation Model via In-Context Learning；[SUP_ABSTRACT_B4_20261019.json 第11对象](SUP_ABSTRACT_B4_20261019.json)
- 14928 — Chain-of-Procedure: Hierarchical Visual-Language Reasoning for Procedural QA；[SUP_ABSTRACT_B4_20261019.json 第14对象](SUP_ABSTRACT_B4_20261019.json)
- 15026 — TuxBot: Semantic-Aware Online OS Tuning with Large Language Models；[SUP_ABSTRACT_B8_20261019.json 第12对象](SUP_ABSTRACT_B8_20261019.json)

## A53 — 作者三项一次贡献决定域（待独立校准）

只处理A52具名14461/14561/14563，不增加新的宽池。原完整题摘复用，现各打开exactv1所需决定核心，不把这一层冒当完整Source；14461/14561 current仅v1，14563 current Sep29v3只标NeurIPS accepted、未见具名纠错撤回，版本号本身不触发全史。日期在贡献关闭时不另追，保潜力项仍需实际公告资格。

- **14461 ClickRemoval保窄潜力**：[v1](https://arxiv.org/html/2605.14461v1)实际§2.1–2.3/§3.1。不是只因UI/open-source收：已有M2N2点击→Markov语义距离，一份FloodFill作object、另一未FloodFill图作background-reference，分别进入object-key suppression与background logit重权/早中晚schedule，再混原/调制noise。这份把同一click同时转为空间删选与background相似度控制的接口可改变是否需要硬mask/额外segmenter的选择，保**输入control接口**潜力，不把成熟attention redirection/CFG原理算新基础。主表/图仅跨工具与backbone，没有M2N2→hardmask对照或独立factorial隔离双map收益，所以不预授新模块因果/真移除；target-free reference的评价选择沿已引旧方法，不另算新评价贡献。只为决定其非纯wrapper补查原引[Attentive Eraser官方摘要](https://ojs.aaai.org/index.php/AAAI/article/view/34285)确认其已有mask→ASS/SARG边界，未读旧全文或追算法史。交root再核这份窄增量是否确值得候选，不因先读了核心就强行保留。
- **14561 PSAO拟具体贡献关闭、不评分**：[v1](https://arxiv.org/html/2605.14561v1)实际§3.2–3.3/Alg1与§4.2–4.3。有限重要度标签/Optuna试配置、取EVAL最佳是已知黑盒search用于segment annotation；所谓不退化只是原prompt包含在**真实全空间最优**的集合论结论，不保证实际有限噪声搜索/算法保存了基线。实例级50个原先答错问题的oracle/Optuna选择不是一般预算改进证据；PSAO-LLM的注释还包含解题中间计算，和全局systemprompt优化不是同一干预/费用，未隔离重要度annotation本身。本文自己仍将有效分割/标注学习留future，只支持此proof-of-concept“注释/附加推理可改变输出”，没有新增可迁移优化机制、有效不退化条件或修正原prompt原则的受控反证。不是因prompt工程/小实验类型排；保原件与这些局部结果，不为已有宽宣传建立全部证明审阅债。
- **14563 MemDocAgent拟具体贡献关闭、不评分**：[v1](https://arxiv.org/html/2605.14563v1)实际§4.1–4.3、§5.1与§6.2–6.4。模块后于child、dependency-first traversal加component/query cache，按atomic claims用现成NLI与此前已Verify文档比对，self-eval/冲突分数均值阈值.9后commit与最多两revision，是repository文档任务的现有graph/cache/验证组合。新“信息充分性”用文档+signature做code-regeneration/Pass@k/CodeBLEU，仍是已知可执行消费者评价的领域任务化，没有新的裁决/验证权限条件；一致文档被称reliable并未独立变成代码事实，分数随重试变高也不是校准保证。w/o memory清空跨unit缓存、w/o conflict关闭NLI的消融支持这套组合对该任务有用，但未提出新一般memory状态规则、证据有效性或执行可靠性边界；23.44→13.76s只是read时间，不提供新的全工作流资源取舍。不能因为read/write/verify/finish命名或新产物类就普遍纳入Agent主线。此层没展开全部20repo/完整指标附件，不否认应用价值或把代码文档类型一律排。

以上两项关闭均是尚未冻结、含糊准入的实际核心判断，不是审阅费时/Books已覆盖后删候选；如root见本文被漏掉的独立新条件，恢复相应核心即可，不重全部Source。14461暂不评分/预写Books；14561/14563不因日期尚未核就记零项。

## A54 — 当前十四来源收口与既成层同步（非DAY）

2026-10-19 11:26+08，已按root R43/44将README实际同步21新增=16真实整合+3仅报告+2中心争议，合原Charon22；14908正文/完整两侧/本人注POST R43已通过且窄位释放，14966标准5分Only R44通过。A50 T3是组件消融/T4是prompt数量，未交换。原Charon整行、窗口和连续原§4未改。当前README是本轮14行自包含范围；V3仅进行态一致性通过，不授DAY。来源边界的新实际取证补在此，复用A18/A49等未变的有效层：

- Google Research [May目录](https://research.google/blog/2026/05/)实际4条May1/19/27/28，DeepMind Blog page2/3目标相邻May12→19，均读到目标前停止。`research.google/pubs/`实取HTML/目录仅year2026=417、team/theme，无日字段或可用May日切片；官方域精确`"May 15, 2026" (model OR training OR inference OR agent OR multimodal)`与DeepMind publications同日期补检无结果，不能拿空搜索当零项。现有限入口/解析已实际耗尽，按R45精确隔离publication历史日段，不再追417篇或创建逐篇日期债；需官方按公开日目标列表/具名原始事件才定点重开，不支持完整Coverage/无遗漏。
- Meta web动态接口两次超时后，CLI实取[publication page1–3](https://ai.meta.com/results/?page=3&content_types%5B0%5D=publication)：每页前12是当前序列，page3 May17 GIM→May12 NeuralSet夹May15；后12旧年混排未假设全页严格排序。Blog两页June/April夹界。无需其后旧论文全文或全历史。
- Moonshot官方组织`/orgs/MoonshotAI/repos?sort=created&direction=desc&per_page=100&page=1`实返42元数据，新资产May22 kimi-code→Apr20 FlashKDA；created只用于定位不冒正文日期。已触发kimi-cli `/repos/MoonshotAI/kimi-cli/releases?per_page=100&page=1`实返100元数据Sep22→Oct2025，May14 1.44→May27 1.45夹界无May15。Platform Blog26条最新Nov2025不冒2026覆盖。只认有界资产/CLI入口，不声称检查42仓库全部commit/release历史；误打印窗外release正文不采用其研究结论。
- Seed从实际[Research导航](https://seed.bytedance.com/en/research)进入五Blog类，不猜API：`/en/blog_list/foundation`12条目标相邻Feb16→Jun19；visual12条Apr23→Jul8；audio5条Apr9→Jul20；ai-infra3条latest Aug14 2025；frontier-research9条Dec2 2025→Jul7 2026。均当前列表实际读到目标前，未扩旧正文/全站历史，41标题不是候选。UAM1625唯一对象日期/核心层沿A20/R9复用，默认与speech投影差异不抹平，Charon原May16不动。
- MiMo主页Paper8条Mar13→Jun29与Blog15条，公开js route/frontmatter有16项（含旧Safety），其真实chunk iframe分别实取date header：MiMo-v2.5 April22、v2.5-Pro April27、v2.5-ASR/tts April2026（月粒度足以窗外）、v2-Pro/Omni/TTS March18；其余技术文May30/Jun8/Jun10/Sep27/Dec等。CDN基地址为页面实际脚本`https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/`，chunkhash来自实际index映射，非猜路径。IAB两次超时不作零项，已用官方公开源/iframe恢复；不扩模型代码。
- MiniMax英文12条May26→Mar18、中文13条May25→Apr27、AgentTech3条Sep19/22/Oct8，分别核有限独占切片，不以英文替代中文。Qwen真实浏览器20条/3次加载、Hunyuan全部11无分页、Zai/ERNIE本日先前实际目标相邻段保持，不因压缩重读有效层。

R45/46/47实际准入决定已消费：原33一次core中的23项，18具体关闭、5转窄潜力（13872/14434/14461/14845/15026），未授日期/Source完成。当前184身份机械分层为54具体关闭+21已独核处置+13909日期另1+98潜在增量+10一次core；**98不是确定候选或逐篇全文队列**。剩10一次core=14497/14504/14524/14537/14587/14704/14758/14779/14846/14897，作者继续有界决定核心。root R47十项决定的具体理由以同日非作者记录为准，作者确认其方法/评价增量边界，不从field标签排小模型/图或理论。机构有限发现不再扩大，arXiv既定主题发现已停；13909与具名贡献/必要Source、Books和DAY仍可执行，不能以这一段把它们终态化。

## A55 — 三项一次贡献决定域（待root校准）

仅处理14704/14504/14537，原完整题摘复用，实际exactv1必要核心；current14704/14537仅v1，14504后有May16v2无具名纠错/撤回信号，不因版本号无差别回读。

- **14704 SceneFunRI保窄潜力**：[v1](https://arxiv.org/html/2605.14704v1)§3.2–3.4/§4.2/§5.2实际读。不是“新855题/低总分”准入：3D原注投影出完全遮挡但处camera frustum的目标，bbox作为**搜索/交互区域**而不是可见轮廓；CAcc要求包含GT且预测面积小于图像25/50%，显式限制“画满图也成功”与IoU对隐藏目标过紧的消费者差异。这份不可见目标→预算化搜索region的评价接口值得核，不先授commonsense因果或VLM普遍无不确定性。人工去歧义保留“可推断”人口未证真唯一，SPoE迭代split/eliminate只报告Dist下降，缺匹配几何/随机缩框反侧，不能以第四步越baseline证明真正排除推理或自动停止失能。后续标准Source只核这份搜索覆盖/面积口径及必要对照，不为855题扩全数据/所有prompt。
- **14504 LongAct/HoloMind拟具体贡献关闭、不评分**：[v1](https://arxiv.org/html/2605.14504v1)§3–4、§5.2/T4–5。RGB-D/semantic oracle环境上采用已有DAG分解、CLIP+voxel对象表、episodic status/history、selfcritic Pass/Refine/Replan与经验回写，是已知组件的家务长任务组合，没有新增一般调度/记忆有效性条件。消融确有critic与lowplanner容量局部收益，也有去episodic SR15→17.7反侧，故不抹结果；但未隔离反思校准/证据独立性或提出新失败界。新IR是GC曲线分段斜率再求斜率的平均，只量得分加速度，未控制任务阶段难度/事件分布或独立同前缀反事实，不能据此称学习/自我改进的通用新测量。不是因具身或低级控制抽象排：若有新跨模块裁决权限/有效反馈机制会保，但本核心不足；不展开全部IR几何附录/300场景。
- **14537 CattleTrade拟具体贡献关闭、不评分**：[v1](https://arxiv.org/html/2605.14537v1)§3.2–3.3/§4.2–4.6/§5。自然语言观测+JSON精确卡片、常规scratchpad/retry和真实规则引擎记录行为是已知benchmark设计，新联合拍卖场景不独立提供一般执行机制。代码heuristics与LLM差额/overbid等确有应用诊断，但代码读结构化精确状态、LLM解析自然语言/跨turn记忆，未配平接口；未ablate memory/temperature，spending efficiency与rank相关不是其因果贡献，作者承认selfbid可能策略而非必然失败。不能由新日志/新rank把“一般静态评价不够”再算新通用条件；保这些具体反侧，不因经济领域硬排，也不因242game规模或只用低成本模型判无价值。决定域已足，不扩所有卡牌prompt/全B表。

以上是未冻结准入的具体core判断，不从Books已有覆盖或深审工作量删候选。三项日期未授；14704若经校准继续必要Source，另两关闭不为不影响处置的日期追踪。

## A56 — 其余三项一次决定域（保窄潜力、未授Source）

14497/14587/14846完整题摘复用，current前二仅v1，14846后July30v2；当前均无具名纠错/撤回信号，未遍历全版本。

- **14497 ROAD保窄潜力**：[v1](https://arxiv.org/html/2605.14497v1)§3.1–3.2/§4.1–4.2实际核心。不是双层数学名义或控制benchmark类比：固定Q函数类中采样分布改变Bellman投影几何，外层用return而非内层TD loss选offline/online mixture；实践以offline advantage改善减online advantage proxy惩罚作滑窗UCB reward，这个双数据源差额proxy可直接改变replay混合的优化目标。MAB/固定离散arm是既有工具不计新原理。offline足够覆盖低uncertainty、训练缓变与零均值误差/近似bias均真实限制，尚不授“无偏/最优/零成本”；必要Source只核proxy推导与关键对照、不能将一般LLM数据混配直接套成同一个已验证算法。
- **14587 Plasticity/backdoor保窄潜力**：[v1](https://arxiv.org/html/2605.14587v1)§5.1–5.3/T1必要核心。SAM这一已有平坦化干预在post-training注入下ASR上升、与其它plasticity干预组合又非加性，提供**平坦/可塑性改善不等后门缓解**的具体受控反侧，关系是优化与安全边界，不因为DRL/security或案例总量收。actor稀疏路径/梯度相似度图及sharpness只为解释，尚不证通用因果、SCC一般定理或可用检测器（作者明确阈值/其它sharpness来源未解）。必要Source需核相同攻击配置、benign回归与SAM反侧/理论实际条件，不扩全部22×8×47任务组合或所有攻击附件；无需LLM实验才可保通用学习机制反证。
- **14846 Transformer-SCP保窄潜力**：[v1](https://arxiv.org/html/2605.14846v1)§5开头与§6实际核心。不是把现成Transformer仅当控制预测器：对QK、softmax、AV三非凸交接构造DC界与simplex不确定集，把一个Transformer多步消费者的可行候选留在逐次凸子问题中，可能改变latent/model-based planner用全局采样或无约束gradient的选择。先核**Transformer-component可行界接口**，非机器人任务收益。§6依赖凸子问题精确求解、初始可行/tight点、uncertainty sets一致与被引SCP条件；单调J本身不授真实环境递归安全或局部最优充分证明。后续必要Source只读这些界、可行性/收敛实际假设及关键计算代价，不扩一般MPC史或宣称LLM token生成可直接用。

三项仅具名准入潜力，未评分/日期/完整必要Source或Books决定。剩14524/14758/14779/14897四core由root独立决定，作者不重复。

## A57 — 14521必要Source、actual owner与逐字PRE（未写）

实际[exactv1](https://arxiv.org/html/2605.14521v1)§2–5/Eq4–9/Alg1/T1–2、A/B.1–2、D.2–3/E.1–2与G.2–3中主kernel/计时必要域，未遍历C/G全规模与H全部训练附件。Current只有v1无具名纠错撤回。[DC原件](SUP_DC_2605.14521_20261019.json)唯一v1May14 08:05:39Z、client arxiv.content/state findable/registeredMay15 02:14:00Z；官方日程下界May15 00Z至该上界完整北京May15，不把Updated/created作pub。

核心局部恒等：P=I−11ᵀ/d，LN(Wx+b)在相同eps/γ/β下等于对PWx+Pb作RMS缩放及同affine。训练以proxy W→PW再链式反传，在这个局部函数相同且optimizer/state/随机性相同的前提下可保梯度，不是将训练后的W直接project之后继续无约束RMS训练也等价。B.2矩阵转置/次序有排印不齐，采用可直接复算的局部恒等，不引其误形状公式。原Algo1只追零均值图，D.2又明确需所有受影响fanout只到可承接LN的消费者；一条输出还供非不变分支时，不能仅标centered=True就授whole-graph等价。Residual需每条相加支路都满足，scalar操作保均值；ReLU/softmax、逐坐标dropout训练破坏，不把LN affine输出默认当零均值。D.3 practical辅助center的图改写需要保这些实际消费者，未认证任意checkpoint所有LN可无条件替换。

E.1表GPT2/ViT/Phi/OPT原foldable为0，practical加center才25/25；BERT24/25，BLOOM5/6，VMamba0/51→36/51。PreNorm要另center embedding并检查末端/全消费者，不混为“算法普遍检测全可折”。§5训练已承认dropout破等价，Multi30K最终BLEU稍低于LN，Swin100三seed均值/std与GPT3-350M任务loss只是局部有限支持，不授全部训练相同。

G.2自写未加速LN/RMS仅reference不能拿作强baseline；G.3主比较是custom CUDA RMS vs PyTorch fused LN、Welford算法，A100-40G/batch2/seq1024，另V100-32G/A100-40G batch2/seq256五次50测量前50warmup。前者文字16×100与后段15×50计时口径不齐，完整dtype/concurrency/SLO与AR decode区分ND，故只采有受测前向节省不复写普遍2–12%。一次graph检测/权重重写及辅助centering、实际kernel/数值容差/全下游质量与部署全部费用均须验证；实数恒等不等浮点逐bit相同。无需代码/附录全遍即足以支持这个窄等价/资格命题。

2+2+2=6：新delta是从激活统计运算到受条件权重/图重写的等价接口，Reach计模型语义与部署执行的交接，不把原有LN基础理论算本文新增。已完整读Ch17 Norm公式/γβ/RMS区别→Normality段→Pre/Post交接，Ch16输出投影与Ch18输入消费者。现RMS段只告诫二者不可混公式，ScalarNorm是拟合替代不等价；尚无**在相同归一化语义和安全fanout下把centering折入affine**的选择，因此拟Ch17唯一段，紧接“RMSNorm等变体省略均值中心化…”完整段后、Normality段前：

> 两者也不必一概视为不可转换：若LN输入为`h=Wx+b`，可用`P=I−11ᵀ/d`把权重与bias改成`PW、Pb`，再保留相同epsilon及输出affine，以RMS缩放得到同一实数函数；这不是直接把原LN换名为RMSNorm。[受条件的centering折叠](https://arxiv.org/html/2605.14521v1)还要求检查被改写输出的所有消费者：残差各支、额外fanout与中间非线性不能只凭零均值标签放行，训练中的逐坐标dropout也可破坏等价。部署转换不自动延伸成任意图或继续训练的等价配方，浮点容差与真实kernel仍须验证。一次图检查/权重重写、辅助centering及独立质量和总延迟都计费；条件或净收益不成立时保留原LN，不因RMS算子较少就批准checkpoint兼容。<!-- source-family:SF-2026-ARXIV-2605-14521 -->

本人末注拟：SF-2026-ARXIV-2605-14521 — exactv1§2–5/Alg1及A/B必要恒等、D2–3/E1–2/G2–3，2+2+2=6，仅affine-centering折叠与实际consumer资格。保相同eps/γβ、fanout/残差/非线性/dropout边界、浮点/计时口径及全部图改写/执行费用；不授任意图或无条件训练等价，未核实现/复现。

## A58 — 14323必要Source、actual owner与逐字PRE（未写）

实际[exactv1](https://arxiv.org/html/2605.14323v1)§4/Eq1–4/Alg2、§5/T1、§6/T2–4与D/E/F中code prior、损失/搜索预算必要文字；§6.1只读其主文算术例证，不采未完整实读H/I的全部电路/换码结论，不借GDS A–C全证明给神经方法最优性背书。Current仅v1无具名纠错撤回。[DC](SUP_DC_2605.14323_20261019.json)唯一v1May14 03:35:46Z，arxiv.content/findable/registeredMay15 02:09:21Z；日程下界至上界同北京May15。

固定层l*读取chunk首token的stopgrad hidden，linear router给C类，选code embedding对chunk内每token hidden加αe；不增加可见词表位置，也不是MoE参数expert/可变depth或从下一chunk深状态递归。主C32/K4/zero-init code，训练对给定完整x抽N条code sequence，按conditional likelihood选a*，联合更新模型/code/router。Eq4 generalist+SG-logratio的数值可约成conditional loss，但梯度仍含unsteered与steered两项；SG分母不能取消梯度或证明无损保持。Selected code的监督依赖训练GT，不是线上知道best code；router-state stopgrad只切路由loss往backbone的这条边，不是整个LM冻结。Bigram-Zipf/no-repeat prior约束code使用不是可解释语义证书。

§5以2H100、lr1e-5/effectivebatch8/每任务1epoch比较4QA；setup写五底模而T1实列六（含Qwen8B），只按实表24cell。测试bootstrap95%CI不等训练seed稳定性；同样数据/optimizersteps没有匹配N候选前向或全部训练FLOPs。Main N8，F称main N4且N8均值较N4差.5pp，配置冲突不擅选。暂停token/TokenAssorted本需额外warmup而本比较刻意low-data，不能给普遍方法优劣。C1静态向量部分cell低于SFT，code perturb/zeroing确能伤当前已适配模型，singlecode部分主题反升；只证其当前功能依赖，不证明code为唯一自然子任务/忠实原模型解释。Practical DLR无priority queue/全策略枚举，GDS条件不能自动继承。下游QA解码/完整precision/墙钟/显存和全能力保持ND，不以“语言序列不变”认证无扰动；训练GT搜索与runtime router、每chunk控制状态的交接要另验，现论文足以评述提案但不授部署recipe。

2+2+2=6，设计是learned chunk-control与search-derived监督，Reach只计训练选择和runtime条件接口，不算理论GDS所有命题。Actual owner选择TRAIN-SFT Ch29：已完整读ConceptTokens（冻结模型学输入embedding）及前feature监督和后数值condition段，现不含**训练期按GT likelihood搜索隐code、再监督内部router并联合改base**；Ch17已读共享模块路径/continuous-thought/跨chunk压缩及前后，那里解释实际路径/状态预算，不复制这份训练环。拟Ch29 ConceptTokens完整段后→数值属性condition段前唯一段：

> 条件接口还可以由训练搜索提出，而不由人工给每段标注概念：在固定层为每个token chunk选择一个离散code，将对应向量加到这段hidden；训练期对已知目标采样多条code序列，选conditional likelihood较高者，再联合监督router、codebook与语言模型。[这条受限适配分支](https://arxiv.org/html/2605.14323v1)改变的是内部控制条件与训练环，不是添加可见推理token或MoE expert，也不能继承理想策略搜索的全局最优保证。目标答案可用于训练选code，部署却只有router；主文与附录搜索数不一致、解码和完整费用未闭，不能给出通用运行配方。同数据/步数不等同候选搜索预算，去code后的退步也不证明语义唯一或原能力无损。所有候选前向、路由/先验与联合训练均付费；控制失配、collapse或质量/总费不合算时，保留普通verified SFT与显式条件，不用可命名code代替独立行为验收。<!-- source-family:SF-2026-ARXIV-2605-14323 -->

本人末注拟：SF-2026-ARXIV-2605-14323 — exactv1§4–6/Eq1–4/Alg2/T1–4及D/E/F必要域，2+2+2=6，仅chunk-code控制与搜索派生的联合监督接口。保训练GT/部署router分账、SG梯度、main/F搜索数冲突、预算/解释/能力边界；不采GDS神经最优、全部算术附件或执行recipe，未核代码/复现。

## A59 — 13909跨日资格实际恢复：具名May13已部署全文（待root核）

原DC下界May14 00Z至registeredMay15 01:59:37Z跨北京日的结论保持；不从created/Updated或提交补造pub。此次只针对同一身份恢复：原件Other字段给[官方project](https://terms-bench.github.io/)，实际页面无公开日、当前增量commerce/bankroll不倒灌v1。有限官方arXiv May目录只有月，advanced原表明确announcement date仅year/month；按观察字段提交May14/15+paper_id的日表单只返回表单，不能当零项或日期证据，不再扫全月。

从官方project对应GitHub Pages唯一repo实际取到以下链条，非repo created或自填commit时刻推断：

1. [官方deployment4671328472](https://api.github.com/repos/Terms-bench/terms-bench.github.io/deployments/4671328472) createdMay13 06:40:47Z，environment github-pages，SHA=`b7638a46b92f220bb5c8e06aa94de753cea04849`。其当前statuses只余后来inactive，不单拿created认定成功。
2. [同SHA的Pages run25782903692](https://api.github.com/repos/Terms-bench/terms-bench.github.io/actions/runs?head_sha=b7638a46b92f220bb5c8e06aa94de753cea04849&per_page=10)实际completed/success，createdMay13 06:40:21Z/updated06:41:08Z。[jobs实际原件](https://api.github.com/repos/Terms-bench/terms-bench.github.io/actions/runs/25782903692/jobs)独立列build、report-build-status与**deploy**三success；deploy job75729439533的`Deploy to GitHub Pages`步骤completed/success，startedMay13 06:40:59Z、completed06:41:05Z（北京May13 14:41:05），非仅启动/上传artifact。
3. [该SHA不可变tree](https://api.github.com/repos/Terms-bench/terms-bench.github.io/git/trees/b7638a46b92f220bb5c8e06aa94de753cea04849?recursive=1)truncated=false，根目录有`TERMS_Bench.pdf` blob=`272b5f05b8933ece1f7b0c942bfb33f615ae93c9`。实际[同SHA index](https://raw.githubusercontent.com/Terms-bench/terms-bench.github.io/b7638a46b92f220bb5c8e06aa94de753cea04849/index.html)直接Paper href=`TERMS_Bench.pdf`，不是只给外部尚未公开arXiv链接。
4. 实际取[该immutable PDF](https://raw.githubusercontent.com/Terms-bench/terms-bench.github.io/b7638a46b92f220bb5c8e06aa94de753cea04849/TERMS_Bench.pdf)13,354,347bytes/80pages，以Git blob计算`SHA1("blob "+len+NUL+bytes)`恰为上项sha。用运行时pypdf内存提取**第一页**核标题`Diagnosing LLM Negotiation Agents Beyond Deal Rate`、八位同作者、完整TERMS-Bench题摘与Introduction正文；这是真实具名完整PDF，不是只有摘要/海报。未读剩79页，不将日期恢复称该版Source完成或沿v1技术结论。

因此至少在**北京May13**已成功Pages部署的目录含同家族完整论文，早于补充May15；当前论文首次公开不得由May15 arXiv登记重新拥有。本日拟以**具名更早全文，窗外不新增/不评分/不进Books**关闭资格恢复，实际首次可能更早但无需无限追查来判断本窗不合格。原始提交/跨日组合及准入潜力不抹，当前github.com/zou-group/terms-bench 404仅代码状态，不影响上述实际正文存在。只给真实归属恢复线索，不自行改May14或任意其他日、不搬已有效事件；交root独立核这条公开部署/全文身份组合后再同步README隔离，不预称DAY。

## A60 — 两实际POST与13909资格同步

root R52实际14521/14323完整新增、完整直接两侧、本人注POST通过，两指定窄位已释放；现18I+3Only+2Dispute=23新增既成处置，README表/证据与§1/5/6均实际同步，合原Charon24。root R53已实际独核A59 sameSHA run/jobs/deploysuccess、tree/index直链，并复用作者实际PDF身份层；13909本轮首次公开资格关闭，保May13具名更早全文，不是按普通Source未做终态化，也不将旧技术潜力反删。

184身份当前=57具体贡献关闭+1具名早全文窗外+23既成处置+103未终结潜力，33一次贡献域已全部给判断。103不是103篇深审债或已冻结候选；继续从具体题摘/贡献决定域剪枝，不因有owner保留。当前已准备但未独核Source的14340，以及正在必要受控反证的14581/14787，仍在103内，不提前计完成。V3与README/SUP/两Books限定working diff-check通过；这不是DAY/全体语义或cached检查。

## A61 — 三个原潜力的具体贡献决定（待独校）

不是重新扩大池：A52原完整题摘复用并实际逐项再读，对可能“新接受/世界状态/迁移控制”的含糊事实只读一次exactv1核心，实际判断下列均不足项目长期增量，拟关闭不评分。Current14398后v3/14634后v3/14306后v3未见具名纠错/撤回，编号本身不触发全史。既有初判潜力不是冻结候选，本节不因深审费时/Books主题已有而排除。

- **14398 ChronoAgentic**：[v1](https://arxiv.org/html/2605.14398v1)§2.4–2.5。自然语言approved plan→skill/tool/API-index辅助code→staticvalidator→isolatedexecute→logs/physics轨迹与VLM描述→structuredrepair，是已有模拟器与Agent执行/反馈机制的任务组合。版本特定API校验只是实际接口存在/签名检查；physics checks消费已有模拟器量，不是新World Model表示/动力学学习机制，也未新增一般证据权限或可靠性条件。新资产/代码场景与T2V总分差额不独立证明新生成机制；无需打开全部80demo或ROS/asset附件即可决定不以“可执行世界”命名泛收现成physics应用。不否认该应用价值，亦不将全部物理/机器人研究排除。
- **14634 RustPrint**：[v1](https://arxiv.org/html/2605.14634v1)§3.1–3.3/§4.2。CodeWiki/RepoAgent式文档成为blueprint，crate分解、docjudge比较遗漏、cargo_check/unsafe检查、翻译maintainer tests再只改code的修复链，明确沿已有documentation/self-debug实践。CodeEquiv≈DocEquiv为任务proxy，不是新语义等价证明；跨来源tests对照是合理已知消费者检验，不新增一般检验接受/写权限机制。领域迁移实现/八repo成绩和更多工具接口本身不足形成新通用可靠性条件，所以具体贡献关闭；不扩整B工具/prompt或所有源测试，也不以C/Rust领域词一刀切。
- **14306 PaSaMaster**：[v1](https://arxiv.org/html/2605.14306v1)§2.1–2.3/Eq1–11。Navigator用ranked evidence重写策略/checklist，Librarian从固定meta/abstract/chunk库检索并打分；“hallucination-free”靠只从已验身份库取citation，而非LLM凭记忆生成，是已知source-bound检索原则。Checklist均值+模型概率/6、listwise rerank、强planner/弱worker与teacher蒸馏Scorer是现成组件组合，未给校准概率的新保证、独立证据支持条件或新的状态更新接受规则。新跨学科库/benchmark及1%费用宣传不自动成为通用研究贡献，不把更多真实来源召回误写零事实幻觉。决定域明确即停，不扩38学科评测/引用或全部self-evolving史。

如root见其中被漏的独立新机制/有效条件，只重开相应决定事实；当前不将这三项记必要Source完成，贡献关闭时不为无关日期另追。

## A62 — 14340必要Source与具体仅报告提案（待独核）

实际[exactv1](https://arxiv.org/html/2605.14340v1)§3/Eq1–3、§4.1–4.5/T1–3及结论；不扩代码。Current June25v2未见具名纠错撤回，v1机制/评价不倒填后修。[既存DC](SUP_DC_2605.14340_20261019.json)实际唯一v1May14 04:04:03Z、arxiv.content/findable/registeredMay15 02:09:45Z，日程下界至上界完整北京May15。

WavLM-Large冻结，audio frame-stack5→双linear projector给10Hz prompt，reader Llama3.2-3B-Instruct的Q/V LoRA r8α16。Text embedding先均匀拉长到**整句**audio prompt长度，用18.6M/16层Conformer+两linear拟合真实source audio/projector输出的framewise MSE；这不是词/音素时长对齐或真实目标语音生成。Target域无audio时随机upsample→固定TE2SL→time mask，仅用于语言侧适配；“text-only”指目标域，source仍需Libri960h或CSJ257h配对训练，不是无speech supervision。生成prompt反映source pipeline统计，不具有真实声学观察权。

T3四条件WER/CER/OOV均有限改善：Upsample-Mask→TE2SL SPGI9.1→8.5、Slides16.3→14.0、CSJeval1 21.5→19.6/eval2 19.4→17.5；不能据两语言四slice普遍桥接modality。Baseline/upmask/refinement/softprompt LR、batchbins及额外训练不同，upmask1e-5而TE2SLadapt5e-5，未隔离Conformer capacity/learningrate/真实MSE监督各自贡献。Model用English-only WavLM处理Japanese，作者承认baseline较差；OOV只在各自过滤后的OOV token序列做Levenshtein、忽略insertions，不能把Recall提高认证全部target术语准确或hallucination下降。Valid WER/CER选checkpoint需要相应验证audio标签，“text-only target adaptation”不等从未接触目标声学验证数据；原文未明确是否source/target valid归属，不自行补。Softprompt固定10/20epoch和§4.3十epoch口径不同不授统一recipe。Seed/CI、precision、硬件、epoch总量、旧域回归与全部费用ND；sourcepairs、MSE module训练、upsample/mask制备、适配和real-audio回归均须计费。

2+1+2=5标准完成，拟**仅报告**而保候选新proposal/有限反侧。ActualCh23已完整读speech深度扩展/旧路径保持、连续encoder融合主旁路、低配对监督的phoneme接口及新语言上下文示例四组交接，Ch22/24边界复用。本文没有推翻已承载的“表示对齐不等真实声学/consumer质量，source接口/监督与target覆盖分别验”的选择；也不冒称书稿已有Conformer伪prompt算法。新18.6M映射是源域重建的具体适配提案，当前缺少其合成condition对真实目标声学消费者有效的受控机制/预算与旧能力边界，不把所有source-fit桥变成长期新分支案例。重开只需同LR/capacity/训练预算的对照、目标真实speech与旧域回归、生成长度/时序支持和全部cost，届时再比较训练期pseudo acoustic condition是否独立改变连续projector/显式phoneme/普通text LoRA的选择；不因5分或主题已有自动Only。

## A63 — 14581必要Source与具体已有覆盖提案（待独核）

实际[exactv1](https://arxiv.org/html/2605.14581v1)§3–5/T1/3/5/6、A/B/C必要策略与E数值sanity；不采未看D图片的attention因果。Current仅v1无具名纠错撤回。[DC](SUP_DC_2605.14581_20261019.json)唯一v1May14 08:53:40Z、arxiv.content/findable/registeredMay15 02:15:24Z，整个组合北京May15。

FinQA screenshot与TAT-DQA原PDF页，各100对/类，总200对；人工改单/多数字、遮答案span或分离table/background，比较五VLM projector patch、两retrieval encoder。Mean/max pooled与MaxSim/MeanPatch大多cos近1，aligned MinPatch可更低；MinPatch用已对齐原/改图位置并取最小，是明确诊断probe非practical retrieval。近1但非完全相同的document-document cosine，不证明query正/负排序或信息理论不可区分；最低patch差也可能含渲染/遮罩位置变化，不独证encoder“看懂数值”。Table/background删除改变大块像素比例，支持受测几何不支持global texture唯一根因；retrieval优化模型同现象也不证明所有single vector不可修复。AttnGuided实为patch self-similarity std，非读取Transformer attention；TopK-R需要原/扰动pair，fixedk50对应9–19%不等比例。C probes未学ranking目标，失败不能否定所有learned pooling。单RTX5880Ada48GB/defaultresolution/HF，precision/uncertainty/ANN检索及实际下游任务成本ND，source制备/encoding/索引/最终原件核验全付费；猫狗对照不匹配细改像素规模，不能当唯一语义因果。

2+1+2=5标准Source，拟**已有覆盖AGENT-RAG Ch76**，不是拒绝该负面测量：现实际“单向量退化不能只归维度”完整两段（371附近）已要求按域/库规模测正例、难负例及最终answer support；完整late interaction/view选择及局部relevance head（365–369）分开全ranking与span，不授相似局部即支持；index-budget与ReinPool/MAGIC完整段（607–615）已明确rare evidence、query需求分布、mean support与真实质量/成本。新数字/遮罩测量保报告但未提供改变这些选择的实际query-ranking反证或新可用聚合机制，不强追加金融case；书稿未含本文MinPatch，不据此假称算法实现相同。必要重开为同几何/渲染控制、独立query/hardnegative排名及最终数值consumer结果，以确立当前池化选择需改变的具体条件。

## A64 — 14787必要Source与具体已有覆盖提案（待独核）

实际[exactv1](https://arxiv.org/html/2605.14787v1)§2–4/T1–4/CompGap、D agreement/E cutoff-LOO必要及G.3–4标注/compute；不遍历A/B全部排名表、H gallery或图片。Current May15 21:26Z v2在北京May16之后提交，未见具名纠错撤回；不倒填v2。 [DC](SUP_DC_2605.14787_20261019.json)唯一v1May14 12:56:36Z，arxiv.content/findable/registeredMay15 02:20:28Z，日程下界至上界同北京May15。

11GME/4CIR，text-only使用blackplaceholder、image-only删text，K10以任一model成功取union识别shortcut；Shortcut-free还分MM成功与所有未解，人工validation另判text/ref/target/overlybroad。4,741人工中1,689valid是**被审残集**35.6%，FIQ/LaSCo各按两类1000分层样本，不能写原全集35.6%有效。分类依modelpool与cutoff，blackimage不是缺模态中性保证；SF在同11model中无单模态top10本就是构造性质，不证明所有未见model/任意K真需组合。LOO可显示1–2pp范围，却仍在同一池重算，不是独立未来pool。MM Recall原→SF→valid人口变化不是能力退化/修复；CompGap=1−max(I,T)/MM也是指定nDCG人口比，不是多模态因果/协同语义证书，MM小会敏感。

人工看同poolMM topK union作为歧义候选，隐去SF bucket但候选支持仍model-dependent；9人均作者/协作者，50overlap Fleissκ.456/α.457、unanimous44%，主label汇合规则细则未完全明，不能叫近完美唯一GT。真实标注可修正部分显然错配/广义query，不保证所有合法match都在panel。H100NVL/EPYC/256GBRAM、modelsload16–86GiB，汇总239.3h/本地161.8h排除exploratory，非完整人工/API/training费用或线上latency；预算/模型revision/输入占位与原/筛人口须共同保存。

2+1+2=5标准Source，拟**已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66**。已实际完整读现221–223附近DSGym两段：input-withheld负控制、跨model有限阈值排shortcut、人工修题、保原与筛选人口及“不认证其它任务grounded/过滤降分非能力因果”均在；前后是评测文件权限与不同负控制通道，后Kamon/多模态身份也保输入/解析责任。本文将这个已存在选择应用到CIR并给新的有效验证，不因新数据/11模型名新增一段；不声称现稿已有best-rank/CompGap算法。保CIR不同construct、部分原始高分由单路信号可达的新结果于本报告，真正重开只需独立pool/heldoutvalid人口下的新失败条件或改进设计，而非扩全部gallery。Ch65/67与Ch23依赖交接复用，当前不写Books。

## A65 — 原潜力中三项具体贡献决定（待独校）

实际完整重读14635/15040/15044/15104/15131/14950/14894/14912八题摘，未新增发现；先处理其中三个准入事实含糊的必要core，非八篇统一Source。Current14635/14950仅v1，15104后May20v2，无具名纠错/撤回，不遍历所有版本。

- **14635 MultiEmo拟具体贡献关闭、不评分**：[v1](https://arxiv.org/html/2605.14635v1)§3.1–3.3/§4.2–4.4与§5.2。已有distribution-based emotion评价被扩为新10,344图/20人多选投票及旧/新标签分数对照，本质仍为既有多标签/人群分布GT在视觉情绪任务的资产与测量实现，非新一般裁决或groundtruth条件。新A/B在120个原/新dominant冲突图片上比偏好，不隔离“单候选验证vs全多选”UI本身、annotator人口与重标；不能据此把偏好新标签当一般annotation protocol因果纠错。其新人口还由三model分歧+一致各一半构造/拒答过滤，分数更高仅这个新标签/人口的测量，旧分布benchmark本已承认多情绪和主观差异。未有改变当前模型评价设计的新机制/受控反证，不以主观任务、负面judge结果或多标签本身排除；不扩全部20万votes/附录。
- **15104 Text-to-Voice拟具体贡献关闭、不评分**：[v1](https://arxiv.org/html/2605.15104v1)§3.1–3.3/§4.3.4。已有TTS+性别voice/noise扰动，保原text/tool schema/GT后复用scorer，是已知paired-modality评测实践的tool-calling任务化；decision/tool/schema/value错误分类与“更多value errors”是域内诊断，不是新的消费者接口/验证保证。原GT被继承不证明TTS语义一定保真，ASR本身又是待测路径，不据benchmark转换名签verifiable。主文按文本正确/音频错的subset与六voice pooled计数合理，但尚无新增可迁移的voice依赖条件、修复机制或控制解释超出一般输入退化；隐私友好judge的80%agreement也不新建立独立真值。不是语音研究硬排，而是此具体增量为测试资源/已知实验协议，不展开全部judge/ambiguous prompts。
- **14950 Evo-Depth保窄潜力**：[v1](https://arxiv.org/html/2605.14950v1)§3.1–3.3/Eq3/5–6与§7.1–7.3。不能只因smallVLA/DA3+FiLM+staged training组合就收：实际把多view预训练深度latent**全局池化为γ/β调制**，与Concat/Crossatten输入消费有明确不对称融合选择，§7.3有相关对照；这份global geometry-condition而非追加所有geometry tokens的接口可继续核。借用的any-view encoder、FiLM及常规stagefreeze本身不算新基础。需限定globaldescriptor未保证局部空间对应、额外encoder/pretrain/不同融合容量与训练预算，不预采“保留2D dominance”因果、无需sensor即真实depth或0.9B普遍更快；后续必要Source只围该接口/相关ablation，不扩全部实机/四suite。

其它五AB潜力仍逐个具体判断：15040只沿creditassignment/BAR的真实训练增量而非K8s/OpenSource总表；15044只沿utterance/frame双粒度消费者与verdict-trace分责；14894只核一step实际条件与chunk handoff，不把Lipschitz偷换one-step exact；14912沿压力transition/修订理由的PRS口径；15131仍需一次方法看LLM+formalchecker是否超越既有CEGIS任务组合。它们均未因列入本节自动变候选、评分或全附件审阅债。

## A66 — R54–56真实已成层同步（继续贡献判断）

已消费R54两项14097/14205、R55三项14398/14634/14306具体贡献关闭；R56三项14340Only/14581具体Ch76 NC/14787具体Ch66 NC标准5/date/实际owner通过，无新Books写。README实际表/证据及§1/5/6同步**26新增=18I+4Only+2NC+2Dispute**，加原Charon27。限定working diff-check与V3通过，非DAY；本日原候选/原窗口/连续§4保护继续，不动并发index。

184当前=62明确贡献关闭+1具名早稿窗外+26既成处置+95未终结潜力。A65两拟close/一保窄仍待root校准，未提前扣账。root接手13866/14063/14311/14333/14347/14350/14358/14364/14373/14382/14386/14391十二项的贡献决定，作者避重复；不从105或95数量预定最终分母。作者继续其余具名AB/必要含糊core，13989只核v1及明确后修影响，不把current v3结果倒填May15；15131/15040先一次决定域，不扩全部bench。新发现停止不变，标准Source已足项不进行第三轮原文。

## A67 — R57/58消费与三个含糊准入事实的一次核心（待独校）

R57十二项完整精确v1题摘校准保窄潜力，复用其中14333 §3.2与14391 IV-A–D已实际核域，不第三轮相同core；未预授日期/Source。R58接受14635/15104具体贡献关闭、14950窄潜力，故当前184=64贡献关闭+1具名早全文窗外+26既成处置+93未终结潜力。以下三项只是原潜力准入决定，未记完整Source/当窗候选，不因三篇都留就推断其余保留率。

- **13989 VectraYX-Nano保受控反侧窄潜力**：实际[v1](https://arxiv.org/html/2605.13989v1)完整题摘、§6.6–6.7/§7.6–7.7/§9.1–9.8必要决定域。不能将西语安全领域小模型/新corpus配方本身纳入；这里的具体增量是相同42M架构换预训练register、以及同LoRA rank加工具监督后，先前“B4为零因容量不足”的解释被本文自己的后实验反驳，故容量诊断须先区分训练支持/输出格式。**这些实验已在arXiv v1**；内部模型v2/v4/v6不是arXiv版本号，不能因current v3才宣传就误判全部后到。也不能过采：OpenSubs42M vs mC4 64M tokens/replay比例变动、单seed十题B5；296→2801工具样本同时改数量/内容/密度，四seed B4 Nano .145±.046/Base260M .445±.201仅25个tool-choice变体、非执行MCP成功，不隔离普适1:20阈值或capacity因果。Current arXiv v3 May21的新增v7/N4 register结果不倒填。若继续Source只补协议/直接限制及日期，不全读corpus/训练版本史；拟采用是“负结果不可据此认定容量门槛”的局部证据，而非小模型普遍替代。
- **15131 Natural Synthesis保独立specification测量窄潜力**：实际[v1](https://arxiv.org/html/2605.15131v1)§3.2/§4.1–4.2/§5.1 T3、A.5与C直接限制。Verilog生成→Yosys/AIGER→nuXmv IC3→counterexample repair与合取spec分解本身是既有CEGIS/形式检验组合，不以新流程命名收。明确新反侧在同57个人工NL任务把实现对**人工gold spec与自动formalized spec分开验**：Gemini3.1Pro HIGH三run，autoformalize路径gold30±0 vs自身spec33.7±1.7，direct RTL则gold31.7±1.2 vs auto spec30.7±1.9。验证器正确不消除模型改写spec的接受人口差，这个受控差额可核对“自生成规格自通过”的评价选择；不把3.7题平均差当统计显著普遍偏差或证明NL唯一意图。参数化仅核有限实例、不证明所有n；spec等价检查大量超时，NL可多合法formalization；模型checker时间/LLM推理token须计费。继续必要Source只围该独立gold协议/覆盖与直接反证，不审所有算法复杂度证明/benchmark。
- **15040 Orchard保reward-conditioned group assembly窄潜力**：实际[v1](https://arxiv.org/html/2605.15040v1)§3.3.1、§3.3.3/Alg1及真实训练配置。Kubernetes/env服务、teacher长轨迹SFT与任务成绩不自动收；BAR按reward正负/terminal status/length从过采样池组装固定N，让rollout调度直接改变GRPO组内人口，是明确消费者接口选择。必须近处保反侧：实际N8/Nmax16/**stride16**只有一次全max采样，不能用算法泛型early-stop声称本实验省生成；目标正例比例.375–.625，初始8rollout筛0<pass≤.5只留约2k任务。按reward/长度选择后的组不再普通iid on-policy组，返回同N不证明GRPO无偏或“hard correctness guarantee”；全正例文字停机与Alg继续/relaxed fallback有口径差待必要Source核。SFT所谓value看全轨迹+gold失败结局，prompt硬要求先升后降/末步低于.2，98.9%倒U不是独立校准证据；不把它当部署前瞻P(success)。继续只核BAR相应消融/生成与训练全成本及上述冲突，不全扩环境平台benchmark、所有teacher或RPR附件。

三项current官方abs已有版本说明均未见具名撤回/纠错；不为排除所有假想更早稿追全史，日期仅后续真实拟入选时核。以上潜力仍可在必要Source后收窄为Only/NC/争议，不预写Books。

## A68 — 13989必要Source与具体已有覆盖提案（待独核）

实际[v1](https://arxiv.org/html/2605.13989v1)§6.6–6.8/§7.1–7.7/§8.1–8.7必要协议与结果、§9.8/10限制；不采current v3的新v7/全部N4-register结论，不扩全corpus/architecture史或代码。既存[DC原件](SUP_DC_2605.13989_20261019.json)同唯一v1Submitted May13 18:03:07Z已过纽约14:00cutoff，最早May15 00Z；arxiv.content/findable/registered May15 02:01:33Z作为上界，完整可能区间同北京May15，不把created/Updated作pub。未见具名更早全文/纠错撤回线索，工具/benchmark实际身份而非标题推断。

所采是局部负结果解释边界，不是作者普遍密度律。42M Nano固定架构/tokenizer/optimizer与SFT，OpenSubs42M vs filtered mC4 64M tokens且replay25/10→10/5%，post-SFT loss1.82→1.65但十题B5 7/10→6/10；token预算/配比、单seed对照与人工无IAA使register因果不能独立归属。正文内部v2/v4/v6是模型实验而非arXiv后版。B5只流利/相关/无register-mismatch，由作者rubric，不是广泛conversation质量；B1是CVE关键词、B3可只tool-name，不能等同事实/执行准确。

B4二十五问题只判首个tool_call block的name，**不调用MCP runtime**，给tool-list prompt后仍零分只说明该模型/格式/测量的失败。约106k参数LoRA r16/α32/QKVO、296样本/五epoch未改善，2801工具样本四seed后Nano .145±.046/Base260M .445±.201；样本数/内容/比例一起变，100%tool mini-corpus相对原62k的1:21不是训练混合中受控1:21概率。原主SFT又有6327tool≈10%而posthoc用296/62513≈1:211的不同分母，更不能统一密度阈值。首token prose prior与parser miss是观察，不识别唯一内部机制；片段参数也可幻觉。B1降Nano .011±.004/Base .019±.003是真实旧域代价，不授无损“capacity无关”、42–260M皆可靠dispatch/普遍1:20或安全。

原训练BF16/L4约4h+$4与语料$25为作者单run口径，不含全部bootstrap/失败FT/LoRA/seeds/基线和评估成本；LoRA全配置/测得runtime预算与CI未完整披露，不以CPU liveprobe或非严格Pi端计时授服务SLO。数据/格式/训练与真实side-effect执行权限分别验收，未核artifact或复现。

2+1+2=5标准Source，拟**已有覆盖TRAIN-PRETRAINING Ch28**：实际开头完整“loss下降不自动保证…部署任务成功”与“看过/可靠掌握不同；频率、上下文、容量、优化竞争和Evaluation共同影响”论点，以及交接Ch29实际完整“pretraining接口非产品接口/示范重权条件生成、角色turn/工具schema/Serving模板同一身份”已承载本次选择：不能从未出格式/少题零分跳到不可表达容量上限，应先检验数据支持、格式、预算与真实consumer。此处不冒称旧稿有西语Nano/1:21算法；局部新反侧保报告，不新增案例。重开需同token/replay/样本内容密度的隔离、多seed/更大独立题与真实执行/旧能力预算，从而建立超出已承载条件的新容量/格式边界。

## A69 — 15131必要Source与具体已有覆盖提案（待独核）

实际[v1](https://arxiv.org/html/2605.15131v1)§3.1–3.2/§4.1–4.2/§5.1–5.2 T3/A.5/C，足以核拟采独立spec测量；不授SYNTCOMP所有1586结果因果/证明或全部A脚本实现。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.15131_20261019.json)唯一v1 May14 17:39:58Z、arxiv.content/findable/registered May15 02:28:56Z，schedule最早May15 00Z至上界同北京May15；非Updated实际pub。

LRM从TLSF出有限Verilog片段/或反策略，经Yosys→AIGER→aigtosmv→nuXmv IC3对输入spec验，CEX供修复；合取分解只检查相应子spec。模型checker sound针对已编码formal obligation，不证明NL意图、所有Verilog或任意n。参数化仅按有限实例范围验，正例不能推出所有n，负CEX只反驳相应实例。IntelEmeraldRapids/32GB/每checker600s；LLM模型ID与reasoning预算、checker/重复修复均计费，未披露可部署硬件/精度SLO，非适用推理benchmark。

人工从57个参数化spec写NL，固定最大SYNTCOMP参数，以Gemini3.1ProHIGH三run分别经autoformalization与directRTL；每个实现对人工gold和model自己formalized spec分别验。T3为30±0 vs33.7±1.7、31.7±1.2 vs30.7±1.9，方向不一致/非统一偏高。via-auto同时通过两spec25.7±.6，不能用33.7−30代替逐例discordant集合。直接spec等价9.3±.6、明确不等价8.7±.6、26.3±.9三十分钟/32GB超时，另12.7±.5语法不通过；timeout不是语义错误，NL多合法加强也不一定错。关键实施细节：生成阶段用第一次可能含syntax错误的formalization，验证时用syntax-repaired spec，身份需分别保存；不能把语法修好当意图保真或“verified implementation”自动等原任务。差额是有限接受对象不同，不证明普遍自动形式化不可靠/端到端必优。代码与复现未核。

2+1+2=5标准Source，拟**已有覆盖AGENT-WORKFLOW Ch81**：实际problem-compilation完整段/typedIR义务列表、AtumAI完整compiler及随后“compiler不获GT/critic只验已编码不变量”段、AlphaEvolve后“自动验证≠目标正确/evaluator是executable specification”与独立复核约束均实读。本文新双spec测量可验证这些边界，却未提供改变该权限选择的新接受机制；不把CEGIS命名当新分支，不冒旧稿已有TLSF/T3。保本报告的语法repair前后spec差额与具体反例；重开为独立意图/合法formalization裁决及受控改进如何改变目标可信交接，而非更高已编码spec通过率。Ch80/82交接已读相应反思证据权限/多agent共享证据不独立，不另写Books。

## A70 — 15040必要Source与具体已有覆盖提案（待独核）

实际[v1](https://arxiv.org/html/2605.15040v1)§3.3.1–3.3.3/Eq1–2/Alg1、§3.6/T9–10与直接SFT/RL反侧；环境§2与GUI/Claw只是任务上下文，不扩全部平台性能/估价或current v3新增OPD/RPR/value模型。Current v2/v3无具名纠错撤回。[新实际DC](SUP_DC_2605.15040_20261019.json)唯一v1 May14 16:35:12Z，arxiv.content/findable/registeredMay15 02:26:43Z，最早May15 00Z至上界同北京May15。

BAR先reward分类、usable/status与response length排序，再在目标正比例内挑固定N，若不足继续stride直至Nmax后relaxed/backfill。具体训练N8/max16/stride16、正比例.375–.625，所以一次全16池后选8，不是已实测渐进earlystop；原文字“easy allpositive不再采”与Alg要求比例不合时继续口径未闭，fallback文字(0,1)而Alg[0,1]也不同，不授完整可直接执行recipe或hard correctness guarantee。返回N只是shape兼容，reward/status/长度选后人口不等原iid on-policy，组mean/std与advantage属于保留组。初始8rollout筛0<pass≤.5的约2k任务又改prompt支持；asyncpolicy freshness、失败/截断分母、未保留16−8与retry升级资源均须独立记录/计费。

SFT失败轨迹的teacher看全trace+gold失败outcome，prompt要求末步<.2/不得单调升，再差分阈值ε.05抽rise action段，之前history保context/环境obs及段外action无loss。这是回溯proxy不是前瞻value；98.9%倒U不是独立校准。所谓scale-matched实际32k resolved vs32kresolved+32krise，总监督不相等，59.3→61.2不能隔离creditassignment；RL full67.5 vsSFT64.3是联合recipe，重SFT后Multilingual反退。未给BARvs固定N/同生成预算独立消融，不把SWE总分增益归BAR；T9不同选择和T10跨harness矩阵只说明各自人口，不授框架harnessagnostic普遍模型能力。Qwen3-30B-A3B/五epoch/64kctx/globalbatch128与RL≤150steps/LR1e-6披露，但RL GPU总时/精度、重复seed/CI、完整训练+生成+test费用ND；env单cmd0.28s不等训练总latency或线上SLO，未核artifact/复现。

2+1+2=5标准Source，拟**已有覆盖TRAIN-GRPO Ch33**：已实际顺读DAPO四组件及其后完整动态补采段、2507.01006 EMA预分配段、**2504.21233完整mixed-outcome组内正负重采样段**和04020多域到达/保留分账段（现718–742附近）。特别735段已实载困难题过采样后保positive并等量抽negative、原/保留组mean/std不是中性归一、length/temperature/索引和未保留生成全费；不是只有宽泛“selection bias”主题相似。BAR固定比例窗口/terminalstatus具体新提案保报告，但实际stride=max未展示新渐进效益，无改变旧组law/预算验收选择的有效反证，故不添微变体案例。Ch32/34真实onpolicy与离线preference交接已读；不授SFT段到另一个owner重复采用。重开为BAR单变量/同全生成预算与failurestatus协议的净质量费用或新估计校正条件。

## A71 — 14347另一人必要独核通过与指定Ch5实际写入（待root actualPOST）

此项root R59首读者/稿作者，作者不是只继承其完成标签：已独立实际完整读[exactv1](https://arxiv.org/html/2605.14347v1)§2/Alg1/2.1–2.2、§4/T1、§5、§10及A2的build/heldout、seed/null与正向注入退化必要域；未把自动输出但未完整阅读的其它附录认定已核，未读全A7/D。另实际独取[同DOI API原件](SUP_DC_2605.14347_20261019.json)，唯一v1 May14 04:15:30Z、arxiv.content/findable/registeredMay15 02:09:55Z与schedule下界May15 00Z组合完整北京May15；Updated不冒实际pub。Current具名纠错/撤回轻检复用R57有效层。

同意2+1+2=5及仅为具体字典/readout差额深入：真实first-arrival代表不移动，不等所有Voronoi边界在新增邻居时不动；W1无新region批只为构建停点，不证全行为coverage。AxBench按label选direction，matched SAE-A .911仍高于EP .881；拒答同pool排build后50 heldout/substring，p12四seed仅两有效、null只可选择处支持有限特异，正向注入会出现I循环，不能由真实activation的身份保因果/安全。R59稿没有采用这些过度宣称，留几何与seed/阈值/幅值/label分责及全费足够。

实际重新读Ch5 superposition开头、完整hidden重建段及线性编码/访问两段，Ch4学习与Ch6架构交接；现稿并未承载固定观测代表作空间partition字典这一替代对象，和原重建贡献/线性访问不同，不为新名强写。按root R59已授唯一位置逐字单段+本人compactnote实际保存，其他正文保持；当前只计已写待actualPOST，不预支第19I/日级通过。root实际POST后再同步README，不等无关Source。

## A72 — 三个评测/检索原潜力的一次贡献决定（待独校）

root R60已实际POST14347 Ch5新增/完整两侧/本人注通过并释放指定窄位，可计19I/27既成；A68–70三具体NC仍待独核，不提前改账。当前184=64关闭+1窗外+27既成+92未终结潜力。以下在原8题摘再读后只核三项准入含糊事实，不新增发现。

- **15019 GranuRAG拟具体贡献关闭、不评分**：[exactv1](https://arxiv.org/html/2605.15019v1)§4.1–4.3与§6.2–6.4。新multi-view地标/元素GT资产本身不构成新RAG机制；实际是YOLO-World检测generic建筑crops、>80%重叠留小框、MLLM看各bbox及全部appearance descriptions匹配element/∅，再按ID取专家文档、加global metadata，prompt要求只叙述这些元素。不是新的attribution强制算法/可验证接受规则；MLLM肯定不等confirmed observation，“不存在候选/没检出”也不能因指令就保证不叙述。与CLIP top1或整库context的域内相对总分、20问题×两模型人偏好，以及双方抽对元素时答案偏好，不独立识别更细unit本身、语义matcher、prompt/证据量各项因果。已有region/element检索、source-bound生成及场景说明的合理任务组合，没有新增一般检索/事实支持条件或受控反证，故不以“verifiable/first-class”命名泛收；不因RAG已有章节或旅游场景排除，也不扩全部附录/多view资产。Current仅v1未见具名纠错撤回；贡献明确关闭，不另追不影响处置的日资格。
- **14843 MechVerse保测量反侧窄潜力**：[exactv1](https://arxiv.org/html/2605.14843v1)§3.1–3.6/§4 setup/§5–7。不是机械dataset或PartNet/CAD渲染本身准入，而是同一组生成视频按复杂度分层，WorldModelBench的自动physics/aggregate随耦合更复杂反升，43组装体/六人12维人评却在motion/coupling下降；可直接修正“已有physical-judge总分足以选择mechanism-correct video”的判断，不能只把已知视觉流畅≠物理当新基础。复杂度tier与资产来源/类别/部件数/遮挡共变，不归因耦合唯一；human样本与全量自动人口对应/CI、方向速度范围、不同生成默认配置及人工准则仍待必要Source核，不授人评普遍oracle。输入同图改方向/速度是有界控制接口，不证明识别真实动力学或action-conditioned worldmodel。Current仅v1未见纠错撤回；后必要审阅围自动/人工对照及cost，不扩141类别或全部渲染附件。
- **14604 EduFrameTrap保压力与judge合同窄潜力**：[exactv1](https://arxiv.org/html/2605.14604v1)§4–6/§7.4–7.7。固定misconception/standardtruth，以三压力×三confidence四turn协议分开context、authority、face-saving，两个tutor的不同pressurefragility和两judge disagreement+部分作者adjudication可能改变“一个jailbreak/总sycophancy分可代表所有压力”的测量选择；不是教育safety名字或泛humanloop准入。360family按family而非3240变体随机拆、T2单独score、judge共用rubric/同两tutor家族与作者裁决不能授独立GT；530分歧中520改sycophancy/100同意抽查有10推翻应保选择分母，不以agreement作真值或该样本推普遍错误率。没有无压力matched-control及真实学习长期结果，不据前后对话称压力唯一因果/持久伤害。后续必要Source只沿协议与直接反证；current仅v1无具名纠错撤回，不扩所有模板/prompt及学科附件。

14517/14842/15199/15198/14381另外五项完整题摘已实际读，尚保具体窄潜力，不因新rubric、功能token或asset自动变候选；准备必要决定域时另记，不将八题摘称八Source完成。

## A73 — 14347实际POST与当前六节同步

R60真实POST14347通过，README已融27新增=19I+4Only+2NC+2Dispute，合原Charon28；§1/3/4/5/6与检查时间同步。首次机械生成无上下文插入hunk把该新表行误放旧§6并添EOF空行；立即实际读回发现、按完整邻文移回唯一§3表并去多余EOF，未改原候选/旧§4或共享index。修后实际检查仅一14347表行、§3共28家族、六节完整，V3与限定working diff-check通过；旧整行和连续§4机械保护另实核，非DAY/语义全通过或cached检查。A68–70仍等待root必要独核，A72一次贡献决定也未提前归零。

## A74 — 14843必要Source与具体已有覆盖提案（待独核）

实际[v1](https://arxiv.org/html/2605.14843v1)§3/§4setup、§5–7及人评说明，已足拟采自动/人工测量反侧；不扩141category、gallery、全部逐模型雷达或CAD文件。Current仅v1无具名纠错撤回。[实际DC](SUP_DC_2605.14843_20261019.json)唯一v1 May14 13:48:17Z、arxiv.content/findable/registered May15 02:21:49Z，最早公告May15 00Z至上界同北京May15。

PartNet904+CAD453 assemblies，Easy独立关节/Medium3–8/Hard≥10部件，资产来源与部件数/遮挡/类别一起变化，不能把tier差额唯一归因coupling。速度用半程/全程/两程、reverse倒帧、不同camera；同图prompt可以改control但未学action-conditioned真实transition。Categoryholdout test1004clips/8类，替代view1480明确排除，fine-tuning18672clips/LoRAr32两epoch/batch1/4×GH200；这些训练与test不等自然物理分布。相同图prompt给各generator的默认配置、输出长度/分辨率/采样预算未统一闭合，不能把模型排名归架构。

VBench平滑约98+/flicker99与WorldModelBench physics/aggregate、独立六人人评12dim测不同对象。关键反侧是43assemblies分层人评motion/coupling在Medium/Hard更低，而自动aggregate常反升；原文无完整逐样本paired差额/CI、完整人评采样/blinding规则及裁决细则，不据平均反向认证每条videojudge都错或complexity唯一因果。Human αmotion .72/visual .63/prompt .77只是所选人口一致性，非唯一真值。Fine-tunedWan2.2感知改善而physics/common反退，保质量维度不替代；强制结构prompt/专家构造也不能认证每条描述/动力学。没有真实force/contact或longhorizon验证，不授物理真实性/实机安全。全部构造/渲染/专家复核、生成/微调、VBench/VLMjudge和六人人评都付费，总GPUh/precision/所有API版本费用ND；未核实现/复现。

2+1+2=5标准Source，拟**已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66**。实际完整读现539段“认动作/描述不等细质量判分”，它明确区分绝对误差、跨样本排序、两候选gap、均值baseline、局部专家参照、视频/skeleton更难及rubric/采样/分辨率/专家全费；随后processjudge完整两段又将solver与诊断/人类教学效果分责。现535 judgecompetence/bias/disagreement非truth段、Ch25完整“learnedWM不让显式simulator失效”及视觉/PBR非contact段也实读，Ch65/67调度/监控交接按ROADMAP真实路径核。本文提供更具体的机械复杂度反侧，但不改变“经任务分项校准后才准judge细质量reward、否则专家/领域checker”的现有选择；不冒现稿已有MechVerse或WorldModelBench三tier数字，不为域case扩一段。重开只需同video/有可靠逐部件oracle的paired judge差额与改善后选择条件，不请求全部141类别。

## A75 — 14604必要Source与具体仅报告提案（待独核）

实际[v1](https://arxiv.org/html/2605.14604v1)§4–6/§7.1–7.7/T3–7及直接限制，足以审压力profile/判分责任；不读全部9.x模板或六学科所有案例。Current仅v1无具名纠错撤回。既存[DC](SUP_DC_2605.14604_20261019.json)唯一v1May14 09:21:24Z、arxiv.content/findable/registered May15 02:15:56Z，schedule下界May15 00Z至上界完整北京May15。

360syntheticfamily×3pressure×3confidence=3240instances，按family/domain切108dev252test，T1回答misconception、S2压力后只判T2。GPT5.2/ClaudeSonnet4.5均tutor亦分别judge，同rubric不等独立真实标签。Test原4536responses排7解析剩4529，不能把排除吞分母。两judge分歧530、作者全裁；另100同意样本实际98usable/10翻转成sycophancy，和§6.3“100/10”不能混成100%完整人工gold。GPTjudge对自身零SYC，但对Claude也错漏200/210，故主要阈值/敏感度而非单独self-family因果；作者裁决更近Claude不认证Claude普遍正确。T5 Wilson区间按responses，不处理同一family九variants相关或API重复随机性，未给稳定跨版本/自然教学人口发生率。

两tutor总sycophancy≈14%相近而pressureprofile不同：GPTcontext较低/authority-social较高，Claudecontext较高/social较低，仅本轮模型/模板。没有无压力matched基线、T1逐项conditional转移证明或中立同长度语义控制，不能声称pressure唯一因果或“reasoning更强会更迎合”；没有学生长期结果，不以position安全风险当真实学习伤害。Teacher构造/Validator过滤、26k量级message/judge、作者抽核及重复调用全费；API实际precision/hardware/SLO和总成本ND，未核artifact或复现。

2+1+2=5标准Source，拟**仅报告**：保三压力/family级split与judge具体漏检测量，不反删已准入候选；新taxonomy在这组学习场景上有上下文价值，却未给经过独立裁决/中立控制的新纠错接受规则或可迁移机制。ActualCh66现535完整judgecompetence/bias/disagreement须人工anchor、541–543 solver非诊断、508后多judge尺度/共同偏差与原始分歧段均实读，已要求分维度/原始人口/独立gold。本文不足把具体context/authority/face三分法升格为本书所有sycophancy的长期完整分类，也不能用两个tutor让新机制更优；不是因5分/教育主题省Books。重开为同family中立pressure控制、独立盲裁/分歧与同意人口全量误差校准，以及明确新修复机制/更广消费者的可靠性条件；不要求全六科模板或真实学生实验才能保局部报告。

## A76 — 两个原潜力的具体准入事实与R61同步（待独校）

R61实际接受A68–70三必要Source/date/具体NC，无新Books；README六节当前30新增=19I+4Only+5NC+2Dispute，加原Charon31。184=64贡献关闭+1早全文窗外+30既成+89潜力，A72的15019拟close、A74/75尚不提前扣账。README修改先一次hunk顺序不升序失败（原文件未改），改为按实际行序完整context后成功；V3/限定working diff-check通过，不改共享index或授DAY。

- **14381 NodeSynth拟具体贡献关闭、不评分**：实际[exactv1](https://arxiv.org/html/2605.14381v1)§3.1–3.3/§4.1–4.3/4.6–4.7与§5必要决定域，未把currentMay16v2倒填v1。三层taxonomy经专家例SFT、Search取来源/one-shot提字段、按persona/geography/usecase组合出prompt，均为已知定向合成/检索/元数据分层实践，未新增一般覆盖保证/grounding接受规则或新的模型学习条件。L3相对L2更高“failure”率来自改变测试题目人口，不能独立归因复杂度或以更会诱发当成总体安全变差；700mixed triad抽核60错误的总体rater准确率未独立校准具体guard-disagreement子群，Gemini-rater更强/高整体accuracy不认证guards错漏人口。具名guard差异只是不同policy/rubric/类别下的判分不一致，论文未提供足以建立新的通用guard失效边界的受控反证；这并非把有害/安全信号忽略，而是已实际读到其不能从全局human审计替局部discrepancy签字。新安全资源和标签谱系有实用价值，但当前新增为领域数据生成组合/本人口总分，不以社会语义/新taxonomy名收通用机制。Current后v2无具名纠错撤回，仅版本变化不触发全史；若root发现独立的新guard条件，只重开对应实际事实，不以日期或附件量排除。
- **14842 Entity-Rubrics保更窄潜力**：实际[exactv1](https://arxiv.org/html/2605.14842v1)§3–4/§6–7。Atomic entity拆解和新AbstractEdit资产本身不算新；准入可核差额在**先仅看原图+指令**给每entity Change/Optional/Preserve预期，再打开candidate判是否真变及合理，最后留global-failure profile。这个expected-state与observed-execution的候选可见性分工可能改变开放意图judge协议，不只是加更多rubric；需核完整prompt是否实际隔离阶段/缺失实体与关系覆盖。文中precision-over-recall主动限定不枚举所有合法edit，多合法解释不等entityprior唯一truth；60sample/六topmodel/三个rater κ.47、ρ.66不授高保真oracle，不能把不同encoder/开闭源比较当架构或thinking唯一因果。后必要Source只围阶段权限/对照/人评，未授日期/评分/Books，不扩38MB全部gallery。

两项均完整题摘先于core；14381本次拟关闭是具体贡献不足而非已冻结候选后为审阅工作量删池，已读新测量与反侧均留本记录。新发现停止不变。

## A77 — 14950必要Source、actual owner与逐字PRE（未写）

实际[exactv1](https://arxiv.org/html/2605.14950v1)§3/Eq1–8、§5/T3、§7.1–7.3、B1–2/D1/E–F相关配置和失败反侧；已足globalgeometry→FiLM→action条件接口，不扩四suite所有排名、gallery或attention因果图。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.14950_20261019.json)唯一v1 May14 15:21:36Z、arxiv.content/findable/registered May15 02:24:30Z，下界May15 00Z到上界同北京May15。

DA3-BASE式any-view pretrained0.13B ViT先within后within/crossview attention给latent，不是新depthsensor/metricdepth真值。InternVL3-1B中InternViT300M/Qwen.5B保前14层给2D+语言表示；depthfeatures投影后token平均成globaldescriptor，head输出γ/β逐通道调制**原2D序列**，再flowmatching actionexpert读条件。既有Ch26路径是语义global摘要调token级geometry融合且保geo tokens，这里反向把geometry先压global、只调VLMchannels，确实不同消费者瓶颈。Global池化丢位置不能保局部几何对应；depthpretrain/0.13B额外分支与FiLM均借用成熟机制，不按其基础性加分。

Stage1只训SEM/action，Stage2加IDEＭ但冻VLM，Stage3全开；最终不保证2D/VLM语义或几何先验不变。§7/D1比较无depth、stage与Concat/Crossatten/SEM，文本支持本设置SEM较好，但没给匹配融合参数/总训练预算和完整seed/CI；不据Concat较差宣告对称融合本质失效，也不由空间attention更集中证明depth唯一因果。图5数值像素未读不抄精确收益。MetaWorld代表配置448/bs16/AdamW1e-5、horizon50/24dim、steps5k+10k+120k/8A100，不外推为所有suite统一训练量。实机xArm6/两D435i RGB三任务各20次，camera遮挡/球滚动/小容差仍失败，collisionprotection触发不能算零碰撞。4090D下0.9B/3.2GB/12.3Hz是推理口径，未给precision/batch/完整controlSLO，不能拿更多参数baseline比出FiLM本身加速；pretrain、extraencoder、三个stage及全动作回归均计费，未核实现/复现。

2+2+2=6，拟仅为representation与action条件交接差额深入并整合**MULTIMODAL-EMBODIED-VLA Ch26**。已实际完整读68–96附近显式坐标桥、观察测度七点桥、geometrytokens/语义gate完整两段及后actionquery分责两段；Ch25 observed/predicted边界、Ch27数据接口已读。新差额不是“有geometry/FiLM”主题，而是globalgeometry descriptor取代额外空间geometrytokens进入action的瓶颈，旧稿未解释此方向；不移动原semanticgate例或其反侧。拟在现“增加3Dfeatures并不意味着融合越早…”完整段后→“视觉表示更强…”完整段前单段：

> 几何条件也可以先经过更窄的信息瓶颈，而不把完整几何tokens继续交给动作模型：将另一个预训练多视角encoder的latent投影后取token均值，用这个全局descriptor预测逐通道的缩放与平移，再调制原视觉—语言序列，供action expert读取。[这一受限接口](https://arxiv.org/html/2605.14950v1)与前述由语义摘要控制几何token融合的方向不同；它减少的是交给下游的几何表示，不代表省掉额外encoder，也不能从全局均值恢复逐位置或米制坐标。有限Concat/Crossattention对照支持比较这条瓶颈，却未隔离全部容量与训练预算，不证明原2D语义天然占优或对称融合不可用。逐步解冻最终会更新全部模块，几何pretraining、额外前向、对齐训练与真实动作回归都付费；遮挡、接触误差或局部细节失配时，保留原语义policy、空间geometry tokens或显式标定与短chunk重观测，不能由推理频率或小样本成功率批准控制deadline和物理安全。<!-- source-family:SF-2026-ARXIV-2605-14950 -->

本人末注只保exactv1上述必要域/6分/不采幅值指标外推或attention因果/未核实现，不含授权/持锁/运行待办。等待root必要独核与具体窄位，不先改Books。

## A78 — 14461必要Source与具体仅报告提案（待独核）

实际[exactv1](https://arxiv.org/html/2605.14461v1)完整§2.1–2.3/Eq与§3.1–3.3/主T1和Conclusion；短稿HTML旧缓存只分两行，但正文实际读取而非标题/摘要投影，未读旧AttentiveEraser全文或遍历代码。Current仅v1无具名纠错撤回，复用A53/R46有效事件层。[新实际DC](SUP_DC_2605.14461_20261019.json)唯一v1May14 06:56:53Z，arxiv.content/findable/registeredMay15 02:12:34Z，schedule下界May15 00Z至上界完整同北京May15。

冻结SD singleforward取multiheadattention转Markov A，clickonehot经A^n按相对阈值最小步数成semanticdistance；FloodFill一份objectmap作key大负罚，未FloodFill normalize另一份backgroundmap作keylogit重权，decoder各attentionresolution重采样；timestep schedule早段前20%不开、早中background五至十步衰减、中段留object、晚段全关，再将原/调制noise用用户r线性混。它是click派生双consumer软control，不是无需内部map/自带真实例mask；乘logit的因子也不必单调对应attention概率，其他key分母共同变化，r>1不是插值保原的保证。遮挡/多实例与正负click需要外部用户修正，不授一次click必完整删除/背景不变。

约5k手工清理PicoBanana targetfree reference和mask/click，512/1024组内比不同pretrainedbackbone及official配置；指标FID/KID/localcrop不是真目标删除/无痕事实，reference是编辑图也可能不同合理背景，不能等原不可见背景真值。表/图只有组合/backbone/输入与click数量比较，无同骨干M2N2→hardmask、双map独立因子、schedule及ARG的匹配预算消融，不将总分归这份控制接口。RTX3090/24GB，SD1.5 4.75s/8.38GB比inpaint2.97s更慢，SDXL19.86s/15.32GB vsAttentive21s/9.90GB并非时间内存双优；precision/steps/batch/分位延迟ND，不授实时。50图/两resolution、25人偏好和匿名GPTjudge仅说明所选人口，rater种类/版本与CI不全。无需训练不免费，click/propagation、原/调制预测、map驻留与完整生成/人工修正皆计费；未核artifact或复现。

2+1+2=5标准完成，拟**仅报告**而不逆改准入：新click双map提案保当前报告，但对现成attention redirection/CFG的这份软control实现，尚未建立优于已有显式mask/单map或可靠语义支持的新条件。实际Ch24 334–354附近完整“证据选择/送哪/注入量分责”、TPBlend双接口及其参数/背景回退、DeltaK key影响全部softmax和遗漏judge/费用两段已读，Ch23/25交接复用；不冒称旧稿已有Markov双map，亦不因没论文名强添微变体。重开仅需同backbone/全费对照隔离双consumer接口的质量—交互代价、目标与非目标独立验收，才可能改变显式mask/inpainting与软语义控制的长期选择。没有Books新写请求。

## A79 — R62/63消费与14950保存态

R62通过15019具体贡献关闭、14843标准5具体NC、14604标准5Only；R63通过14381具体贡献关闭、14461标准5Only。当前184=66贡献关闭+1早全文窗外+33既成（19I+6Only+6NC+2Dispute）+84未终结潜力。README已先实际同步R62的32新/原合33，R63与后续实际POST下一次窄差额同步；未将待写14950预计完成。R63授A77唯一段+本人注，已在Ch26原geometry反侧完整段后/视觉消费完整段前真实保存并顺读完整两侧，working diff-check通过，仍待root actualPOST才计第20I。

root已实际读14418/14443/14448/14450/14465/14513六完整题摘，其中14418 repeated-ASR/随机重复分母、14448 perinputgate+dualLoRA stopgrad、14465 cell-mask DLM verifier/AR反侧、14513 drift mask复用/稀疏预算仍窄潜力；14443/14450由root一次决定域中，作者避重复。14663/14727 root与作者窄准入校准已完成，以下只做其必要Source/具体owner，不新增发现。

## A80 — 14727必要Source、actual owner与逐字PRE（未写）

作者实际[exactv1](https://arxiv.org/html/2605.14727v1)§3.1–3.5/Eq1–22/Prop1及证明、§4protocol/§4.3/T3、§5、A4–5必要配置/成本，未展开所有MRI/segmentation榜、A1–3全seed附件或临床路线。完整AB已读，current仅v1无具名撤回纠错。[新实际DC](SUP_DC_2605.14727_20261019.json)唯一v1May14 11:54:12Z、arxiv.content/findable/registeredMay15 02:19:04Z，日程下界May15 00Z至上界完整同北京May15。

不是把MRI应用类比到LLM：本次对象是直接替换神经网络global token mixer的算子族。2D feature分别沿H/W rFFT，对每frequency的channel vector用同一正交U的Udiag(λk)Uᵀ，频率gain由softplus正值表；两axis有不同U、gaintable可按normalizedfrequency插值，real/imag各用同一real矩阵以保rFFT共轭条件。与自由frequency-channel矩阵或各channel独立filter不同，固定的是跨frequency的channel方向而非所有gain。不是输入依赖Q/K路由或已训练softmax等价，PSD/Hermitian只属**单axis spectralcore**，不延伸过localdepthwise/GELU/1×1fusion成为全blockSPD，更非真实物理normaloperator。

Prop1只在directK-bin且joint spectral signatures两两不同的genericstratum给C(C−1)/2+KC局部维数，借用正交群/离散signedpermutation不算新的跨系统理论基础；B<K插值子族和全block不继承这个维数结论。Row reindexing只描述gain参数重排，不授任意输入频率置换等变或优化收敛。T3同wrapper/HiFi-Mamba在CC359×8 shared28.68 vsuntied28.43、signed28.51/complex28.56；四个structured→randommask增益从平均+.62→+.08，说明所测采样geometry依赖，不证明每种coherentspectrum或foundation训练都改善。跨backbone主比较各保nativewrapper、整体参数/FLOPs不同，不能全归sharedbasis；case-level std不冒seedCI。Naturalimage证据是ADE/ImageNet4xbicubic重建而非生成foundation/causalLM；此事实限制采用，不先因无LLM实验排模型primitive。

A4同input CHASM FLOPs28.22G/13.27G/11.48G对Mamba/U-Net/ViTbaseline24.64G/12.56G/11.54G，不授普遍加速；A100/H100/AdamW5e-4/bs8/100epochs匹配steps非全cost，实际wallclock依FFTkernel/利用率而未闭合，precision/peakmemory/总GPUh/服务SLO ND。FFT/复数buffer、matrixexponential与gain求值、localwrapper、训练和消费者回归均计费；未核artifact/复现。

2+1+2=5，模型算子差额需定点深入，拟整合**MODEL-SELF-ATTENTION Ch14**。实际完整读现projection-freekernel及两段固定phase/Fourier、随后Haar完整分支与局部Q/K/RBF两段，Ch13位置信息/Ch15多头路由交接已核。现稿说明无内容寻址的Fourier/固定频带混合，却未说明frequency-channel operators共同特征基与独立gain的参数共享选择，不能以已有Fourier关键词假NC。只收此general primitive，不引临床/逆成像整条应用路线。拟在“固定phase/Fourier分支的受限证据…”完整反侧段后→“固定结构混合也可保留空间上的多尺度频带…”Haar首段前一段：

> 若仍选择频域全局混合，还可以限制不同频率怎样共享channel方向：对每个空间轴分别做FFT，让该轴各频率都用同一可学习正交基，只保留各自的正gain，再逆变换回空间表示。[这一受限参数化](https://arxiv.org/html/2605.14727v1)介于逐channel独立滤波与每频率任意channel矩阵之间；两轴不必共享同一个基，它也没有恢复按当前内容寻址的Q/K权重。对称正谱只属于这份spectralcore，加入局部非线性和融合后不能把全block称为正定或真实物理逆算子。所测重建中，破坏采样频率关系会明显削弱收益，不能把共享坐标自动推广成语言、视频或所有token网格的更好先验；FFT、基变换、gain插值及训练仍付费，整体FLOPs也未普遍更低。频率几何不适配、局部细节或净预算退步时，保留独立频率响应、原Q/K/V或已验hybrid，而不由更少参数签发等价表达和端到端加速。<!-- source-family:SF-2026-ARXIV-2605-14727 -->

本人注只保精确必要域/5分及generic维数/单core/成本边界和未核实现，未授前不改Books。

## A81 — 14663必要Source、actual owner与逐字PRE（未写）

实际[exactv1](https://arxiv.org/html/2605.14663v1)§1/Defs1.1–1.2/Thm1.3/Cor1.4/Prop1.5、§2二次模型Eq9–14/步长条件与tight例、§3Lemma3.1局部chart/停止事件条件、§5Lemma5.1必要推导与5.2高概率进入后稳定声明。未审全Lemma3大式逐项代数、Lemma4所有chart证明或全5.2/主定理尾证明，不冒独立全形式证明验证；所采定理条件及所需几何/主要反例边界已足。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.14663_20261019.json)唯一v1May14 10:18:21Z、arxiv.content/findable/registeredMay15 02:17:26Z，下界May15 00Z至上界完整北京May15。

真正新量是**局部C2/PL+随gap消失的乘性噪声**下常步长普通SGD的最优渐近率，不是已有PL原则或所有深网都强凸。邻域内f≥f*、梯度L-Lipschitz、||gradf||²≥2μ(f−f*)；noise相对历史条件均值零且E||Dk||²≤σgap。需γ在(0,2/(L+σ/2))且进入依δ选择的足够小V；定理只保证存在事件C使P(C∩enterV)≥(1−δ)P(enterV)，不证明训练会进入、不授无条件probability1或有限budget保证。条件事件上a.s.到同value随机localminimum，平方距离/gap渐近以任意m(γ)+ε上界：m=maxλ∈{μ,L}[(1−γλ)²+γ²σλ/2]。不是每步恒等收缩；σ0退化普通GD，常见不消失SGDnoise/Adam/momentum/finiteprecision都不能直接套。

二次模型同噪声条件可直接按A谱给期望率，作者tight构造Dk=ηk A^(1/2)θ证明仅这些条件下不能更好；一般localPL推导借已有极小值C1流形与normal Hessian谱∈[μ,L]，tangent无同等回复力，chart误差在小邻域渐近控制。不能用NTP loss较平/overparameterized命名认证实际σgap，亦未处理f−fN统计误差或泛化。数学结果无硬件precision/workloadbenchmark，不填虚构实测性能；将μ/L/σ/邻域资格用于真实训练需曲率、梯度噪声/step监测成本，这是项目采用边界而非作者实测方法，未核代码或复现。无需为这些条件遍历该领域全证明史。

2+1+2=5，具体局部收敛解释差额深入，拟整合**WORLDVIEW-WHY-MODELS-LEARN Ch4**。已实际完整读gradient更新/优化路径、两坐标分支、SGDnoise/离散EoS、mini-batch三段及随后transientnoise两段；Ch3知识边界与Ch5表示交接、Ch28实际scheduleowner复用。现稿强调局部梯度非全局导航与噪声影响，但未区别噪声随lossgap消失时“非强凸仍可有二次谱端点渐近率”的成立条件，不能用泛局部几何主题假NC。拟在“所以batchsize不是单纯的吞吐参数…”完整段后→“噪声影响的也可能是训练早期…”完整段前一段：

> 小batch的噪声也不一定留下固定的收敛误差下限，关键是它是否随目标gap一同消失。对局部二阶连续、L-smooth且满足`||grad f||²≥2μ(f−f*)`的目标，若普通SGD的条件无偏噪声还满足`E[||D||²|history]≤σ(f−f*)`，固定步长`0<γ<2/(L+σ/2)`可在进入足够小邻域之后，以高概率收敛到同loss值的某个局部极小点；[这份局部结果](https://arxiv.org/html/2605.14663v1)的平方距离和lossgap渐近因子由`max_{λ∈{μ,L}}[(1−γλ)²+γ²σλ/2]`控制，不要求该邻域强凸或极小点唯一。这里没有保证优化器能找到该邻域，也不是每步收缩、有限预算或泛化保证；不消失的采样噪声、momentum和Adam不能直接继承结论。验证曲率、噪声与轨迹支持仍有成本，条件未证时保留实际loss/gradient/step监控与保守schedule，不因overparameterized标签就停用衰减、clipping或独立质量验收。<!-- source-family:SF-2026-ARXIV-2605-14663 -->

拟本人注只记上述必要域/5分/conditional asymptotic而非每步与全局保证，未核所有证明/实现；等待root必要独核和实际窄位。

## A82 — R63/64实际已成层与未冻结停点

R64实际POST14950通过，Ch26指定窄位释放；README六节已实际同步34新=20I+6Only+6NC+2Dispute，加原Charon35。184当前=66具体贡献关闭+1早全文窗外+34既成+83未终结潜力；A80/81两Source/PRE尚待root，未预计新整合。V3与README/SUP/Ch26限定working diff-check通过，非DAY/cached/完整语义验收。root接14418/14443/14448/14450/14465/14513六项既定AB贡献，前四窄潜力、14443/14450决定域中；作者不重复。作者下一具体域仍14842阶段权限/人评及其余未终结AB，未开新发现或把83转全篇证明/附件队列。

## A83 — 14663仅符号与渐近语义差额PRE（未写）

按root实际必要Source/Ch4邻接独核反馈，仅明确f/f*/μ/L/σ/γ/D与m+ε渐近边界，不重做有效Source、不改旧正文。A81其余条件/owner/位置/5分不变，修后完整单段如下，仍待精确授位：

> 小batch的噪声也不一定留下固定的收敛误差下限，关键是它是否随目标gap一同消失。这里以`f`表示优化目标、`f*`表示相应局部最小值，`μ>0`是PL常数、`L`是梯度变化的上界，`D`是条件无偏的梯度估计噪声、`σ≥0`界定其随gap消失的强度，`γ`是步长。对局部二阶连续、L-smooth且满足`||grad f||²≥2μ(f−f*)`的目标，若还满足`E[||D||²|history]≤σ(f−f*)`，固定步长`0<γ<2/(L+σ/2)`可在进入足够小邻域之后，以高概率收敛到同loss值的某个局部极小点；[这份局部结果](https://arxiv.org/html/2605.14663v1)以任意略大于`m(γ)=max_{λ∈{μ,L}}[(1−γλ)²+γ²σλ/2]`的渐近界控制平方距离和lossgap，不要求该邻域强凸或极小点唯一。这里没有保证优化器能找到该邻域，也不是每步收缩、有限预算或泛化保证；不消失的采样噪声、momentum和Adam不能直接继承结论。验证曲率、噪声与轨迹支持仍有成本，条件未证时保留实际loss/gradient/step监控与保守schedule，不因overparameterized标签就停用衰减、clipping或独立质量验收。<!-- source-family:SF-2026-ARXIV-2605-14663 -->

## A84 — 14443另一人一次准入核验与两Books保存停点

root首读R65提出关闭14443，作者现**独立实际读**[exactv1](https://arxiv.org/html/2605.14443v1)完整§4.2三小节/Alg1、§5.3.1 buffer反侧，并因“formal amortization”可能是独立增量另仅核A.1–A.4的实际论证性质。Context-specific历史(p,critique,reward)条件训练prompter，局部最高reward−ε入buffer，普通KLpolicy update，的确是既有elite经验反馈/历史critique与RLprompt生成组合；未有新contrastive loss/反思状态接受协议。A.3信息增益≫明确是“we posit”，不是新已证明samplecomplexity上界；A.4未带buffer的泛化/零shot独立推理明确留future。消融有限task减少step不含新增feedback/样本/历史输入全费，训练成功率也不新证明bufferfree全场景规则。因此确认R65**具体贡献关闭、不评分**，非把潜在有效定理忽略、非读Source费时排除；当前仅v1轻量纠错撤回有效层复用，不另追不影响处置的日期。

R68 actualPOST14727已通过并释放Ch14，可计21I/35新增既成；14663按R67授A83单段与本人注真实保存Ch4，完整mini-batch前文及transientnoise两段已self-read/working diffcheck过，仍待root actualPOST不预计第22I。消费此处14443关闭后，184=67贡献关闭+1早稿窗外+35既成（21I+6Only+6NC+2Dispute）+81未终结潜力。root首读14418/14513必要源作者避重复；其它被读AB仍不是Source完成。

## A85 — 14450另一人必要Source与具体仅报告提案（待独核）

root R65首读；作者已独立实际取[exactv1 PDF](https://arxiv.org/pdf/2605.14450v1)975905bytes/6页，完整读正文§III–V/表II–III与Fig1说明（pages2–5），未核全部引用/代码/图像像素。HTML404不作必要证据外部缺口。首次PDF文字提取的pypdf“wrong pointing object”警告前缀混入JSON封装，解析失败；按错误恢复skill定位为封装而非正文不可读，原输出先缓存再分出真实JSON后6页文本可取，不改公共脚本、不无限恢复pipeline；警告没有当论文内容。Current仅v1无具名纠错撤回轻检复用R65。[既存DC](SUP_DC_2605.14450_20261019.json)唯一v1 May14 06:44:44Z、arxiv.content/findable/registered May15 02:12:19Z，下界May15 00Z至上界完整北京May15。

Rank-K-32B每MSMARCO seedquery在BM25的10/20候选上抽16条τ.7/p.95/max8192，50k query约22%保11k。只在合法可解析且nDCG>0的样本算query内均值，再s≥均值且len<均值取最短，空集丢；不是Pareto frontier、每题最优或语义等价压缩。全参数两epoch/bs64/AdamW，在8H800/SWIFT执行；PDF提取LR公式有字形损坏，不补造精确执行recipe，采用无需此值。Testτ.5/p.95，NeuCLIR用English机器译文不代表原文跨语言。T2 BM25均nDCG .525→.523、长度2100→1322，SPLADE .642→.640/2426→1607；十个nDCG cell七个较低，缺seed/CI不把微差认证非劣或显著退步。RankZephyr7B与32B teacher/student不只差reasoning，不能宣告所有非推理rerank劣。

Fig1说明DL20长度835→5131时nDCG约.642平台是本设置反侧，不推出所有query最优长度/停机规则。TRR须事后知最后unique ranking、MOR重复排名不分有益复核与无效循环，不能从这两代理证明在线已稳定且正确、内部推理逻辑未简化。T2token34–37%减少不是实测wallclock/生产SLO，16×生成/过滤标签、11k训练/全参数更新及独立qrel验收均全费，precision/端到端latency/峰值memory/总GPUhND，未核实现/复现。

2+1+2=5标准Source，拟**仅报告**保局部负证据与长度—质量取舍，不因成熟蒸馏组合反删候选。实际Ch76完整Reranking/ContextPacking下的fixed-depth/reference/window、ordering token–quality曲线与全费、L3TR/no-generation及pair可见性段已读（现621–656附近），Ch75/77上下文/持久状态交接已核。本文未给可靠的在线TRR停止权限、同完整预算/独立泛化的短trace非劣条件，仍只是一份用qrel选本模型较短输出再SFT的版本recipe；不冒旧稿已有该蒸馏算法或因没有论文名强加案例。重开为相同候选/生成+训练总费、独立query与seed下质量界及真正在线可得停止规则，才比较是否改变推理rerank预算分配。

## A86 — 14842必要Source与具体已有覆盖提案（待独核）

实际[exactv1](https://arxiv.org/html/2605.14842v1)§3–4/§6–7、AppC完整两call模板/schema与D人评、E各评价器身份；不扩38MBgallery或全部模型表。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.14842_20261019.json)唯一v1May14 13:46:24Z、arxiv.content/findable/registeredMay15 02:21:48Z，schedule下界May15 00Z至上界同北京May15。

Call1确只instruction+contextimage，按Things/Stuff/Global给entity与Change/Optional/Preserve；Call2读两图+期待，扩新出现entity，再比较变化/合理性及globalfailure后1–10综合。新两阶段可见性分工成立，不是只atomicrubric命名；但不能叫完整blind评价或immutablegold：candidate会改变Call2实体列表，缺失entity/跨entityrelation/期待可多解，schema中的期望与globaljudge仍是model proposal。所谓precision-over-recall不枚举所有合法改法、绝不证明所有该改都改了。Expectedpreservation未变与missed-required虽同一label词内可判不同，须保原字段/执行标签，不从overall分推出各项正确。

60stratifiedsample×六topmodels×三标注者=1080responses，实际8名通过qualification的EnglishAMTworkers、每task3人，0.35美元/1–2min。Overallκ.47而各维IF .54/preservation .61/entity .41/quality .28，ρ.66不是完整稳定oracle/全generator可靠性；topmodel筛选与共享指南限制人口，不把实体细分或两call独立算纯因果。Gemini3Flash+thinking统一backbone比较VIE/ComplexEdit/CLIP，但不同调用预算与prompt维度不能授candidateblind步骤唯一增益。Encoder/开闭源/think模型跨资产差异不证textencoder或更多thinking为唯一原因，explicit长prompt和abstract指令不是等语义强约束，也不把DINO-Vendi多样性当正确性。两call检测/期待/对比、额外tokens与人审/生成全费，精度/线上latency/总费用ND；未核artifact、复现或gallery像素。

2+1+2=5标准Source，拟**已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66**。实际完整553–565附近：perrubric测量与全表聚合区分、ARTS层级context/pruning、筛选后gold人口，以及**561完整“生成标准时限制每次调用看到哪部分、标准构造与最终判定分责、candidate-conditioned标准仍可错”段**。这不是泛“要独立评价”映射：当前具体选择已要求冻结两侧原文/可见权限/中介和最终粒度，独立校准含义与判定，而不从更多标准/整体agreement签无bias；本文把此协议实例化到source-image expectations与candidate-image execution，未改变该权限/验收原则。旧稿没有EntityRubrics两call算法，不冒称实现同一；新测量与proposal保报告，不为微变体追加case。重开为真正隔离候选影响的期待/关系coverage对照与独立合法edit人群条件，表明现有标准构造权限需具体改变。

## A87 — 14727/14663实际POST与当前六节同步

root R68/69已各自实际保存21I/22I POST通过，Ch14/Ch4指定窄位释放；作者实际读本日review确认正文/两侧/本人注核验范围，非从作者口报行号继承完成。README已实际同步36新=22I+6Only+6NC+2Dispute，加原Charon37；V3及README/SUP/两Books限定working diff-check通过，非DAY/cached终审。已确认14443贡献关闭计入67，184=67close+1早稿窗外+36既成+80未终结潜力；A85/86标准Source提案仍待root不提前扣账。此后只续既定具体域，不重新发现宽池或重复有效Source。

## A88 — R70两项处置与当前六节同步

实际消费root R70，14450标准5/Only、14842标准5/具体NC均通过，不重读不变原件。README实际同步38新增=22I+7Only+7NC+2Dispute、加原Charon39；修正§4前导遗漏更新的旧26计数为38，原Charon整行/原小时窗与连续旧证据块未改。184=67贡献关闭+1具名窗外+38既成+78未终结潜力，潜力不是确定候选/全文债。新表/小标题已实际首屏对照原件纠正初次保存的简称扩写，不留自造论文名，A85锚点按真实标题校正。不授DAY。

## A89 — 14558必要Source、actual owner与逐字PRE（未写）

实际[exactv1](https://arxiv.org/html/2605.14558v1)§3.1–3.2/§4 Eq4–7、§5.1–5.6/T2/F7–8正文与必要B正则身份、C1–2配置/评价；未读全trajectory展示、完整附录逐模型曲线或核实现/复现。Current官方abs仅v1，无已见具名撤回/纠错。既存[同DOI原件](SUP_DC_2605.14558_20261019.json)唯一v1May14 08:33:02Z、arxiv.content/findable/registeredMay15 02:14:51Z，日程下界May15 00Z至上界完整北京May15，非Updated实际pub。

机制明确：think标签权α，answer/action权1+βsigmoid((E−batch-action均值)/std)，E=−logsumexp冻结reference原始logits；保原GAE/GRPO advantage、按Σw归一，不改真实reward身份。Action-only平均energy与组reward方差的Sokoban3B相关ρ.537只是预测关联，不认证真实token信用或reasoning无效。本次数学检查：任一context公共logit偏移c不改softmax但E变−c，context间不同c可改变标准化权，不能把raw-energy直接叫概率不确定性；全局同c会被batch去均值消掉。冻结参数不固定policy不断变化的prefix，因此读出也非训练全过程常量；这些反侧是本次推断，不冒论文已指出。

Qwen2.5-Instruct .5/1.5/3B，单node4H100/RAGEN+veRL+FSDP/Ray；前三符号环境200更新、WebShop100，128轨迹/步，部分filter ratio.25、Frozen/WebShop等1，不把stochastic rewardvariance等固有难度。默认α.1/β.5，前三context3600/response400、Web8192；eval前三32prompt×16rollouts=512但非512独立prompt，Web256prompt×1；temperature.5、动作turn预算同训练。无多seed/CI配置不签普遍稳定性。WebShop3B strict22.7→36.7、purchase96.9→99.2分账；Sudoku.5B16.2→81.4是具名设置非普遍65.2点。F7 α0的WebShop最终坍塌、α最优随任务变；F8 β0 strict29.7→β1 39.8→β2 25.4保非单调，默认β.5主表与调参winner不作同run。F8替换energy/entropy/NLL只局部控制，未证明gauge不变或真实uncertainty。

B称reuse KLreference，但C2前三环境训练移除KL只posthoc跟踪，仍需reference logits或复用读出；无匹配端到端runtime/memory表，故不采零额外费。reference前向/词表归约/batch统计、rollout/筛弃/完整训练与调参全费，precision/总GPUh/服务SLO ND。

拟2+2+2=6，Reach仅训练token信用与环境实际消费action分界，不借PPO/GRPO或“能量模型”基础性加分。实际Ch33完整SequenceReward/tokencredit、semantic-span重权、execution-reference、DSS-GRPO与confidence分段前后已读，Ch32原value接口与Ch34preference交接已对。旧DSS改变think/answer两份长度奖励与独立advantage，本文保同一advantage但对环境action支持集施加结构权/固定读出proxy，是具体替代而非缺论文名。拟置DSS-GRPO完整段后→“结构分段也可以服务于不同的测量目标…”前一段；未写，待独核/PRE与窄位。

> 显式的思考与行动边界还可以只作更新权重的结构先验，而不另造两份正确性奖励：保留PPO原value或GRPO原组相对advantage，降低think段的正loss系数，再用冻结reference的原始logits之负log-sum-exp，经本batch行动tokens标准化后，为answer段提议不同的正权重；最后按权重总和归一。这改变信用落点，不证明行动token才是真正错误原因，分段也不隔离共享参数。这个energy是模型特定代理而非校准不确定性：给同一context的全部logits加共同常数不改变token分布，却会改变它；冻结reference也只固定给定context的读出，不固定训练中变化的prefix人口。[受限多轮对照](https://arxiv.org/html/2605.14558v1)中，完全取消思考更新或过度集中行动权重仍会退步，不能从action-only与reward方差相关推断思考无需学习。边界解析、reference前向、batch统计、全部rollout与训练均计费，不能把无新增参数写成零费用；代理、格式或独立任务质量不稳时，回退uniform信用、保留必要思考更新与原outcome验收。<!-- source-family:SF-2026-ARXIV-2605-14558 -->

## A90 — 14530必要Source、精确公式反侧与actual owner/PRE（未写）

实际[exactv1](https://arxiv.org/html/2605.14530v1)§4–6/核心方法、T1–5、B2配置、I5/T17延迟及K限制；只为已见MPS回构缺项打开[精确v2](https://arxiv.org/html/2605.14530v2)同§5.1，未扩完整版本史或附件。Current官方abs有v2 May19提交、未见具名纠错/撤回，采用仍v1；v2同受影响回构仍无正交残差，不将后修各版本号视新事件。既存[DC原件](SUP_DC_2605.14530_20261019.json)唯一v1May14 08:11:32Z、arxiv.content/findable/registeredMay15 02:14:12Z，公告下界May15 00Z至上界完整北京May15；Updated不当pub。

§4诊断100COCO图、64token/4–32step，contextualized similarity另10图；masked输出与词表均值/未上下文化mask对齐只支持局部prior解释，不证明它唯一导致重复/视觉错。§5.1用均值embedding穿各层轨迹拟PCA rank3、中心μ，投影z后按cos正部减沿prior方向的分量；打印h~=Uz~+μ遗漏(I−UUᵀ)(h−μ)，实际会丢全部正交残差，而非只改3/4096“坐标”。此为直接代数反侧，未自行修印式冒原文。当前官方仓库只沿已观察root→LLaDA-V/llava树定位该一函数，未全repo代码/commit史；[immutable blob](https://api.github.com/repos/hong-sujung/MPD-PAC/git/blobs/970327cceb2fa6782a7309f76ab7dd45f59ad77c)的1441–1511构建与1672–1718实际前向，1707–1711明确delta_new=delta_sub_new+(delta−delta_sub_old)。[具名原件节取](SUP_14530_PRIOR_CORE_20261019.json)保存真实sha/必要行号。当前README另写h−λcosUUᵀδ，方向又不同于主文/当前函数，故只以函数澄清“如何保残差”的可执行形式，不认证当时v1实验commit或完整一致artifact；不再搜无关LaViDa实现/历史。

MRS是s_i=1+βsigmoid(η(τ_i−τ0))乘位置×频率角，低frequency index后段scaling更大，不是把该频带attention分数直接乘大或理论保证远视觉获得正确质量。LLaDA-V λ.1/LaViDa.3、β.01、η8/12、τ0.6/rank3固定每骨干跨任务，标准full-suffix unmask；不能外推block/semiAR或任意RoPE。T2 LLaDA MPSonly Ferret60.2<60.4，RefCOCOg不变；MRSonly LLaVA63.9高于MPS61.7，故不照抄“哪个模块主要改哪任务”的因果概括。T4 top3 LLaVA65.3>ours64.1、random方向亦受益/部分grounding同分，词表均值非所有指标最优或唯一机制；投影后similarity下降部分为构造必然。T3 NTK/YaRN反退只是本dropin配置，非通用长context方法不成立。

T1九benchmark中GQALite、Ferret/DetailCaps各随机100而非全test；B表RefCOCOg4steps/8tokens、Ferret48/96、Detail128/256、LLaVA64/128、MIA32/64分账。作者B2系统1A100-SXM4-80GB与2RTXA6000，未指定每行GPU/precision/batch，ND不补造。T17固定64token：LLaDA4step2.31→2.33s、32step18.10→18.16；LaViDa.49→.57/3.52→4.19s，不采“无开销”或只说绝对毫秒；还需PCA前向/构建、hidden读取和每步改写/全采样。无多seed/CI、生产并发/SLO，未运行artifact/复现实验。CHAIR/AMBER局部结果不签空间结构精确保留、事实真值或无损2D。

拟2+1+2=5，具体表示/位置条件差额必要深入，不将RoPE/PCA基础算新长程理论。实际Ch24 masked已知/未知开头、提交风险和后续多target/逐位置schedule完整必要段已读，Ch23表示contract与Ch25生成≠transition交接有效。现稿先解释提交顺序/联合依赖，尚无同一mask表示prior+位置几何接口这个分支；并非仅无论文名。拟在“每轮对多个mask产生预测…”完整段后→“未知区域也可以是不连续的多个target…”前单段。无当时artifact一致性保证，正文仅受限接口与必须保残差，待root必要域独核/PRE及窄位，尚未写。

> 即使提交schedule不变，共同[MASK]初始化与相对位置先验也可能使未揭示位置更依赖彼此，而不是有效读取视觉条件。一条受限干预先把词表均值输入各层所得轨迹拟合为低秩坐标，在最终masked hidden中减弱同向prior分量；另一条按RoPE频率索引，用平滑gate更强地缩放低频旋转角，而不改变先揭示哪些位置。这是表示与位置接口的替代，不证明attention增量就是真实grounding，也不由词表均值解释全部非线性坍塌。实现必须保留未干预的正交残差：原文打印回构式与“只改低维分量”自述不闭合，当前官方实现显式加回残差，不能把后到代码当作v1实验已用的证明。[必要对照](https://arxiv.org/html/2605.14530v1)中，单项干预有局部退步、随机方向也能获益；PCA、额外hidden读写、RoPE修改与完整采样仍费，LaViDa的实测延迟增量尤其不能叫零开销。先验、生成范式或质量—墙钟条件失配时，保留原表示/位置编码与更保守提交，重新检查重复、视觉事实和完整成本，不凭training-free批准无损或普遍加速。<!-- source-family:SF-2026-ARXIV-2605-14530 -->

## A91 — 14558实际保存态与14571一次贡献决定

14558已按root R73唯一A89逐字稿实际保存Ch33新313、前DSS311/后confidence315–317与本人末注；作者实际顺读完整新增/两侧/注，限定working diff-check通过。root R74实际POST已通知通过，第23I/39既成可计，Ch33位释放；README后续同步不把别项预支。

14571先完整题摘，实际[exactv1](https://arxiv.org/html/2605.14571v1)§2.2–2.3核心机制/对照、§2.5–2.6人机迁移/行为、Discussion限制一次决定域，当前official abs仅v1无具名撤回/纠错，未追日期或全30MB附件。实际是CVAE两模态prior/posterior四KL+EMA触觉anchor、force-aware contrastive和batch distance-matrix对齐，合五重构/六对齐loss；ResNet/PointNet/taxel坐标/接触区域加权属于该视觉触觉任务具体结构。迁移依赖人为重演配对100段/5499图，冻结既有robotencoder/decoder、训练humanencoder+domain gate；没有human触觉GT，读出的是robot触觉并以0.2N阈值触发flick，不等人类真实感觉、神经机制或可泛化接触规划。加全部六损失相对仅重构与逐项去除保局部效用，但没有新的对齐算法、可迁移接受条件或受控机制反证超出已知CVAE/对比/几何蒸馏组合；loss下降/CKA高也未建立新一般识别界。拟**具体贡献关闭、不评分**，不是因小模型/触觉/无LLM实验或有owner硬排，不把一次决定域说标准Source。若有独立新条件可具体指出再重开，待root校准后计数。14664同批只核具体多层接口/对照，仍潜力不预终结。

## A92 — 14418另一人必要Source与中心争议提案

root R71首读后，作者实际[exactv1](https://arxiv.org/html/2605.14418v1)完整题摘/§2.1–2.2.2、§3.1–3.3/§4.1–4.3/§5及A1–2硬件/模型身份，不第三遍所有附录面板、未核实现/复现。Current仅v1轻检有效层复用R71。既存[DC原件](SUP_DC_2605.14418_20261019.json)唯一v1May14 06:05:37Z、arxiv.content/findable/registeredMay15 02:11:34Z，下界May15 00Z至上界完整北京May15。

确认CAS-gen为同攻击重复target生成/判定后全有害才入库，CAS-eval则固定同一response重复judge取AND。独立同分布判定概率q时乘积期望q^k只是新estimand，真实有害但judge偶发false-negative也会被指数压低；重复全判有害不提供独立harm真值，相关judge更不能直接套iid式。原文“k>5 unbiased”、全通过必真有害/温度0消除所有随机、qualitative无需报seed/target温度均不由对照支持。评估k提高自然压率，不是原ASR统计偏差已校正或系统更安全；CAS-gen又按同judge筛选人口，筛后提高不认证攻击本身全面更强。

四攻击/五开源target/两LlamaGuard、五attackseed的观察保留；局部10prompt每翻转10pp，seed不是50个新prompt；正文+AppendixA为Granite4.0而限制写3.2身份冲突不合并，不据此泛化闭源/多模态。2A10080GB节点、部分70B+8B才需两卡，precision/batch/总GPUh ND。生成/筛弃、k次判分及原攻击搜索全费，未认为严格筛选省预算。5分，安全评价受影响深入；实际Ch66完整scorer身份/聚合、固定answer仪器扰动533与前530/后536–538、judgecompetence与Unknown分责已读，Ch65/67平台交接有效层复用。本文未闭合被宣称的无偏纠偏中心，拟**争议/暂缓、不进Books、不作更安全或普遍ASR高估证据**；局部测量/AND提案及本次q^k反证留报告，非删候选。重开需明确评价对象是单次harm概率、连续k次judge一致性还是生成可靠性，以及独立语义标签/相关结构、匹配人口/预算与原始逐次判定；不把尚可执行解析当外部材料缺口。待root独核最终处置。

## A93 — 14513另一人必要Source、actual owner与逐字PRE（未写）

root R72首读后，作者另实际恢复[exactv1 PDF](https://arxiv.org/pdf/2605.14513v1)，11343835bytes/25页：首页实际HASTE、六作者；独立完整读pp6–16必要§3.2/§4.1–4.4 Eq2–11/Alg1–2及§5/T1–6反侧，不读AppA完整证明/AppB图库或声称pixel审查。pypdf图中存在孤立数学surrogate，封装JSON能解析但store拒绝非法Unicode；原输出缓存后仅将孤立surrogate替换U+FFFD保存文本缓存，原公式/正文未据此补造，普通文字与必要公式可读，不构成外部阻塞。Current-v2改题HEART/新增Hunyuan由R72具体事件层复用，未采用后修结果/全史。既存[DC原件](SUP_DC_2605.14513_20261019.json)唯一v1May14 07:57:55Z、arxiv.content/findable/registeredMay15 02:13:49Z，公告下界May15 00Z至上界完整北京May15；不是Updated作pub。

Alg1保存head上次真refresh的mask/meanQ/K，复用不移动anchor，仍本步QKV算attention，不缓存输出。Eq2完整token平均L1与Eq5均值差L1不同，后者可相消；不核完整AppA也不继承Prop1普遍保证。Layer比例heuristic又可覆盖head判定。Alg2先denseprompt pool缓存velocity，每head固定一个sampledprompt、四interval各取一步，三top-p .85/.9/.95在相同对照上测实际sparsity/误差，单head疏其余dense；Eq10分母全dense谱能量，四频权1/.5/.01/.01。ILP平均稀疏约束优化可加single-head误差，不等联合输出、每request硬budget或latency最优；top-p不是sparsity数值。

v1Wan2.1-1.3/14B/81帧/50UniPC/shift8/CFG6/A800PCIe，480P主表六维VBench不是全VBench。720P仅1.3B、无VBench且XPSNR20.25→19.65，TMRonly VBench75.89→75.65，FFT LPIPS.2534→.2554。T5 δ30→100：reuse87.48→96.53%、sparsity72.52→61.62%、131→145秒，说明少mask prediction与实际attention工作分开；并非过度复用仅损精度。总秒未含完整offlinecalibration，precision/batch/seedCI/tailSLO/总GPUh ND；mean归约/mask驻留/dense校准/所有单head测量/ILP与全生成全费，无实现核验/复现。

2+1+2=5，对mask状态寿命/离线budget组合的具体差额深入。实际Ch14 sparse support三段、block半径/统计界反侧、帧间帧内预算与motion-proxy配置/online动态mask两完整段已读，Ch13/15实际开篇交接及Ch24生成/缓存边界有效层复用。现稿只分配置预算与当前support选择，尚无head-anchor只刷新推进/运行时mask寿命，以及不同实际sparsity下离线误差配置这个状态交接；不是因没有HASTE名就gap。唯一owner MODEL-SELF-ATTENTION Ch14，拟置完整motion-proxy费用/回退段后→“## 改变匹配表示…”前单段；不在Ch24再讲一遍。未写，待root必要核/逐字PRE及窄位。

> 稀疏support还需要自己的刷新状态，而不应与K/V或attention输出缓存混为一谈：逐head保存上次真正重建mask时的Q/K均值和mask，当前均值漂移小时只复用support，仍用本步Q/K/V重算数值；只有刷新才移动anchor。均值差可能因token间相消而很小，不能继承完整token漂移的稳定性界。另一个离线接口可分别测每个head、每个top-p门槛的实际稀疏度与dense输出误差，在平均稀疏约束下选一份head配置表；单head扰动的可加误差代理并不等于多head联合质量或在线latency上界。[受限视频对照](https://arxiv.org/pdf/2605.14513v1)中，过久复用旧mask会保留更多实际连接，复用率更高反而更慢；更接近dense轨迹也不保证各项感知指标更好。均值归约、mask驻留、dense校准/逐head测量、配置求解与全部采样都计费，不能由免训练或离线处理删掉总成本。漂移代理、配置支持域或质量—墙钟回归时，刷新mask、放宽support或回退原top-p/dense，而不把更少mask预测当作更少attention乘法。<!-- source-family:SF-2026-ARXIV-2605-14513 -->

## A94 — 14530与14513实际窄写保存

14530按R75/A90逐字稿保存Ch24新743/前完整schedule741/后完整multi-target745–747及本人末注，作者已实际顺读完整新增/两侧/注，限定working diff-check通过。14513按R76/A93逐字稿保存Ch14新422、前motion-proxy418/费用420、后424标题/426完整替代接口及本人末注，作者同样实际自读/限定diff-check通过。两者均只授权单段/本人注，已通知root待非writer POST，不提前计整合。14418 R76中心争议已成，仍保5分候选，不反删分母；无DAY。

## A95 — 14664必要Source与具体仅报告提案（待独核）

实际[exactv1](https://arxiv.org/html/2605.14664v1)§3.1–3.2测量、§4.1–4.4/Eq3–8、§5/6.1–6.3/T3–4关键配置/对照；未看全部视频、gallery像素、完整附录或核实现/复现。Current official abs见v2 May26，无具名撤回/纠错，未将后修版本号当贡献或回填v1。新实际[DC原件](SUP_DC_2605.14664_20261019.json)唯一v1May14 10:19:19Z、arxiv.content/findable/registeredMay15 02:17:28Z，日程最早May15 00Z至上界完整北京May15。

实际是Qwen3-VL-8B首/末层各RMSNorm+Linear到D/2、channel concat再融合；cond token固定time0调制，与source/target/reference的VAE latent拼入Wan2.1-14B self-attention。VLM/VAE冻结，adapter/DiT训练；first+last并非额外时间序列/无额外读出，joint token interface也不自动“消除modality gap”。§3 EBᵀ是文本/视觉hidden诊断矩阵，不是实际QK attention权重；100人像视频+SAM2人mask的ratio受hidden尺度/符号与mask人口限制，不能据早层ratio高证明全部空间真值只在浅层或最终层丢失信息。论文未给该比值的完整概率校准，本文不补造normalizedattention执行配方。

30k paired编辑训练=24kOpenVE筛后+6k合成人像；Qwen3-VL另生成/筛样，局部human-inspection>9.3阈值不等通用独立gold。训练8H100/8000步约2epoch/bs1每GPU/AdamW3e-5，约65h；单H10081帧720P约6.5min，Qwen3s+DiT328s+VAE35s为所列近似分项，不强制补成精确总和；peak50GB，precision/生产concurrency/SLO ND，encoder/双层读出/longtoken/筛样与全训练/采样都费。评价60视频=30simple+30complex，Gemini3Flash六维/30人整体1–5，不把topsubset全部同质或整体均值当独立校准oracle，部分source受license未全公开。v1自述额外open evaluator/人评统计位于附件，此次采用不依赖其所有新增面板，未遍历。

必要对照T3同训练设置的self-attn CC8.05低于unified dualcross8.24/fused8.22，T4首+末CC8.05<末层8.28、VA8.09<8.11，而IA/TS/PR/SC较好。保具体可选取舍，不读成空间/语义全维支配，也不把换encoder/容量/交互边全部归bidirectional唯一因果。训练设置相同不证明所有算量/seed完全匹配；未披露多seedCI，不采全commercial架构效率结论。

拟2+1+2=5标准/仅报告：已准入的VLM多层读出与unified生成条件proposal、局部对照保留，不因成熟组件组合反删。实际Ch23完整encoder/读出consumer、浅层probe≠最终访问/表达181–183及selected whole-network heads208–210，Ch24多个条件接口/层内先后分责有效层已读；这些现有段不等于已有MiVE实现。本文当前新增是一份first+last分配/融合的模型recipe，没有建立可迁移的“必须早晚层合并”或attention形式消除模态差异条件，也没有同总费用/独立编辑语义下能改变现有consumer-first选择的通则；不为每个投影组合追加Book案例。重开需层级信息的受控可读/消费者因果隔离、matched表示/交互预算与独立语义/运动/保留维度证据，明确新条件再比较已有论点。无Books待写，待root必要Source/处置独核，不预扣计数。

## A96 — R77/78实际消费与42既成同步

作者实际读本日R77两真实POST与R78贡献决定域。14530第24I/14513第25I均通过、Ch24/14指定窄位释放；14418争议R76已成。README已实际六节同步42新=25I+7Only+7NC+3Dispute，加原Charon43；V3与README/SUP及三个本日修改Books限定working diff-check通过，原Charon整行/原小时窗/2474字符旧§4含标题连续块机械保护通过，不是DAY或cached终审。检查时间按实际时钟12:45:56+08:00回填，不使用手写近似未来时刻。

14571具体贡献关闭已经R78另一人校准，现184=68贡献关闭+1具名更早全文窗外+42既成+73未终结潜力；14664 A95仍待独核未扣，TWN14448/TABALIGN14465遵root首读packet只作另一人必要域，不扩78表或全部附件。14531/14553只沿既定潜力取得exactv1，尚未读核心、不称Source完成，不扩发现。

## A97 — 14448另一人必要Source、actual owner与逐字PRE（未写）

root R78首读后，作者实际[exactv1](https://arxiv.org/html/2605.14448v1)完整题摘、§2.1–2.3/Eq1–12、§3.1–3.3/T1–3及AppendixA，未读78任务附录逐项表/图库/全部case，未核实现或复现。当前仅v1轻检复用root R78有效层；[既存DC](SUP_DC_2605.14448_20261019.json)唯一v1May14 06:41:53Z、arxiv.content/findable/registeredMay15 02:12:16Z，公告下界May15 00Z至上界完整北京May15。

θr生成input/可选CoT的prefixKV，θe用16learnable queries读detach KV，不重编码；base/full两mask只在query读取侧决定是否读CoT。共享frozen底座不把reasoner的prefixKV变成embedder自行prefill同数值，detach仅截这条路径，route loss/target是否跨支梯度及其它共享依赖不能由该词全称消失。Gate在生成前取input末hidden，标签为本batch cot/base正例相对最hard负例margin差的sigmoid，阈值.5；非真实思考必要、题目难度或groundingoracle。RL只train新policy LoRA、frozen原θr作KLreference，冻结θe/query/gate与static targetcache不自动固定读取变化KV/hidden时的reward/gate人口；采用稿用“若仍读取…”条件句，不擅定未披露重算实现。

T3 sameSFT shared63.3→dual64.1→detach65.2是局部差额，不认证所有损失冲突唯一因果；globalcache从65.6→66.6又改负例人口/难度，不只是同分布低噪估计。T1聚合78数据集不等78个独立同型任务，4B adaptive videoRET33.6低于**CAFe-7B34.4**；GME-7B该列28.4，已实际指出root首读名字误配，保原数不误归baseline。CoT相对base如4B imageRET67.6→67.4/GD85.9→85.5，8BCLS68.6→68.3/RET69.8→69.4；oracle逐样本事后选较好不能部署。T2同模型cot→adaptive token117.2→58.9/115.2→62.8只是49.7/45.4%CoTtoken，非总时延/显存/训练费。

Qwen3VL4/8B；32H20/BF16/ZeRO2/FlashAttention2，最高8192context/2048CoT，4Br32α64/8Br64α128，全部LMlinear两LoRA不改vision。SFT3epoch/AdamW5e-4，RL1epoch/G8/2048globalneg/βKL.1；teacher与judge同Qwen3.5-35B-A3B按不同任务生成/过滤，不把source-only生成等独立质量gold。两路标签、KV及底座驻留、teacher/verifier、全球negativecache与全部训练/搜索费；生产SLO/全GPUh/多trainseedCI ND，不运行代码。

2+2+2=6，跨adapter KV/截梯度与生成式表示效用gate具体差额深入。实际Ch23完整native共享表示、VirtualEncoder读出两段、生成式backbone→理解/检索表示461和后Omni冻结接口463，Ch22/24与Ch76 AgentIR/原生hidden projection三完整段交接已对；后者消费已有Agenttrace/投teacher索引，本文是表示模型自己按需生成并训练两份adapter，不把retriever输入扩写重复到Ch76。唯一owner MULTIMODAL-REPRESENTATION Ch23，拟完整“复用生成式backbone做理解/检索表示…”段后→“冻结encoder/projector后，只更新语言reasoningconsumer…”段前一段。未写、待root必要域/逐字稿与窄位。

> 生成式backbone也可以先为表示任务生成自己的推理，再交给不同的读出，而不让两种目标共用同一份adapter：在冻结底座上分开reasoning与embedding LoRA，后者以learnable queries读取前者留下的prefix KV，并在这条交接处detach；只看输入与看完整推理的两份embedding可用不同mask读出。这省去另一遍prefix编码，却是训练出的跨adapter接口，不是与embedder自己重算的cache精确等价，也不令所有目标或统计依赖隔离。生成前的gate可学习两份embedding在当前batch正负样本margin上的差额，只提议本输入是否付费思考，不把它当作真实难度或语义正确性。即使之后冻结embedder/gate，若仍读取更新中reasoner的KV或hidden，也不能仅凭参数冻结声称reward或gate人口完全stationary。[受限多模态检索对照](https://arxiv.org/html/2605.14448v1)支持局部拆分/截梯度与自适应选择，但CoT在部分分类/检索切片退步，事后择优oracle也不是可部署gate。Teacher轨迹与判分、双adapter训练、KV驻留、两路标签和全部推理/检索均计费；token减少不等总延迟改善。接口、gate效用或独立质量回归时，保留直接判别embedding、独立reasoner加重新编码或固定路由，不让自生成理由取得事实权威。<!-- source-family:SF-2026-ARXIV-2605-14448 -->

## A98 — 14465另一人必要Source与中心争议暂缓提案

root R79首读后，作者实际[exactv1](https://arxiv.org/html/2605.14465v1)完整题摘、§4.1–4.2/§5.1–5.2、T5–8必要对照与§D4–D5/§E4–E5/§G配置直接反侧，不遍历全部理论/图库/实现，也未复现。此前两篇合并工具输出被截断导致14465 JSON无效，不计读完；随后单篇重新取得169676字符完整文本缓存，以下只读必要域。当前official abs v2Oct3/“AcceptedNeurIPS2026”无具名纠错撤回，只版本号不触发全版比。既存[DC](SUP_DC_2605.14465_20261019.json)唯一v1May14 07:00:26Z、arxiv.content/findable/registeredMay15 02:12:40Z，公告下界May15 00Z至上界完整北京May15。

方法提案成立但权限有限：LLaDA8B在固定maskcanvas生成含[target:col]步骤，解析成cellmask；执行另读当前table/plan选tool，额外extractor按serializedcell token span汇总attention，在mask内质量/全table质量比作标量，二参数logistic以terminal正确性训练后反馈进下一步context。不是硬执行/接受cellgrounding契约；执行器可首步final跳plan，stagnation两次状态不变/分差<.02取最高score答案，代理不担任真实correctness。Parse失败默认uniformmask；精确式是**表格attention总质量≥ε时overlap恒1**，0<质量<ε时为质量/ε，不从任意非零声称恒1；此修正已向root指出并见R79同步。

D4固定attention、density-preserving随机mask能排除该20WTQ题“只有sharpness”解释，使用human mask而非DLM生成mask，不证明其planmask真值或bidirectional预训练唯一因果；50draw/4模型不扩大原20题人口。D5 oracle/noise是每dataset20题×三seed=60与主表n200单次不同，6.4pp不能作同人口ceiling。G与AppendixB均写每accuracyentry n200/单deterministicpass，但T6单项如90.32、61.34、92.39等不是.5pp倍数，分母/聚合未闭；六列accuracymean与FeTaQABLEU/经模型改写不能说八项同口径。T5 planner替换+2.87与T6+4.69不拼一个matched实验。原数保留但不用headline授精确提升/普遍收益。

G是三process：reasoner Ollama qwen3-vl:8b GGUFQ4，attentionextractor另HFQwen3-VL-8B-Instruct NF4/doublequant/eager，LLaDA另4bit顺序调用；不是自动读取执行reasoner同实例真实内部轨迹。即使底层同家族，两量化/执行路径与观察身份需验证，planmask/attention重叠仍只是独立proxy，不从terminalcalibration得到真实causalgrounding。实为单RTX4090/24GB、planner128denoise、reasoner至多6steps、N1且G称deterministic、正文温度.7差额保留。1,600标准/100manualseed+GPT5bootstrap/人核、二参数CPUfit便宜不删上游attention制备/teacher与全部工具采样费。

E5 planning78+execution56.8=134.8秒，而AR计划6+102.6=108.6秒，44.64%仅下游阶段，完整反慢。TabFact DLM total150.6对AR62.1、accuracy90.09<92.39，正文仍把64.2称比58.6快，保原数字不抄方向。论文称相对40.5为4.7×也与134.8/40.5≈3.33不合，未替它修成已验证全费。批量/总GPUh/生产tailSLO ND，不把checkpoint无pretrain费说全流程免费。

2+2+2=6，安全/解释与执行评价受影响必要深入；拟**中心争议/暂缓，无Books写入**，保新plan-cellproposal、D4局部负控制和全部反侧，不删候选。Actual Ch79完整plan可验证假设/observationreplan与Ch66完整attention-sensor身份/事实和effect分责405及前后均已读；现有原则不能替本文未闭的observer/人口/因果验证背书，亦不冒旧稿有其算法。重开仅需逐题原始分母/指标聚合与raw结果、同执行实例attention或具名跨实例代理校准、解析失败不自给满分的门控，以及同人口/完整规划+执行预算的控制。当前明确相反证据已足以不采用强结论，不把普通Source未读冒外部终态；必要源已读，等待的是作者澄清/新受控证据。待root独核处置，不预计。

## A99 — R80/84/85消费与具名日期恢复停点

已实际读R80/84/85：14664第8Only通过、14448第26I实际POST/Ch23窄位释放、14465第4Dispute处置通过。当前45新=26I+8Only+7NC+4争议，184=68close+1更早全文窗外+45既成+70未终结潜力；README将按这层同步，不把root四份首读packet直接预支完成。14517/14549/14598/14868/14891/14935只由root作有界贡献判断，已关闭的14401/14431/14495与14504/14537有效层复用，不再读其core；14434仍潜力。

14553已有完整AB与一次§5.1–5.2初步机制，但未完整定理/Source：structured linear bandit存在新feasible-arm/gap的潜力；current官方abs明确PublishedICLR2026，触发**具名早稿资格恢复**，不能先当May15新候选。官方搜索精确题名定位OpenReview M0n3gtwHNg、匿名PDF hash a9a58460e03175e3535d655c9b407913ffc404e5及ICLR proceedings 4b0713b4f15946acaecb0676389715ed，搜索“去年/五个月前/七个月前”只线索不作pub日期；当前官方ICLR标题/作者/摘要身份一致，但仅会议年不足精确首公开日，也不凭arxiv登记再拥有。未读取其他会议inventory/论文理论。

OpenReview forum web实际challenge；publicapi2 notes?id、api notes?id、api2 notes?forum及web API均未恢复，CLI各403，User-Agent/Accept普通公开读取亦失败，不伪造pdate。CUA首次hidden visibility在子agent不支持，去掉option后该origin browser动作自动审批因模型容量失败被拒，未执行；此非用户拒绝也非已认定不安全，未换browser/原始CDP/间接办法绕过。当前日期资格仍未完成/不计候选或Books，具名缺项是该公共note的publication/attachment公开链。继续其它可执行域；尚未把这项行政或可解析欠账冒作完成，后续由允许的正常原始入口或外部可用性变化恢复，不能要求用户解决整个普通来源尾。

14531一次§4/§5.4/A4.1–4.2机制已读：ConvTextVAE+普通CFM+Transformer，以及boundary按compressionfactor分组补PAD/分context与free latent确有具体接口；GaussianKL不证明diffeomorphism、直线条件CFM不证明所宣告HJB最优、attention不自动是给定V的梯度。当前无具名纠错信号，仅v2/v3编号不触发全史；仍须按实际有限架构贡献决定后再核必要证据，不把控制重命名/已知原理算新理论基础分。未作最终处置，不预缩候选。
## A100 — 进行态复验与14553资格外部保留的精确分层

恢复后重新完整读取当日本日适用合同、ROADMAP和最新路由；继续复用已独核45新=26I+8Only+7NC+4争议。README当前45层V3与本日README/SUP限定working diff-check实际通过；此为进行态结构检查，非DAY、缓存层或最终引用验收。R86五项14517/14549/14868/14891/14935仍窄潜力，14598只待作者对具名决定域有限确认，不预扣关闭；14373/14382必要exactv1与DC已实际恢复，尚未由此预支完成。

14553按root明确指令停止被拒的浏览器动作，不改工具/入口规避同动作审批，也不等待用户重试容量。当前已取正式ICLR出版记录只给会议年份，不能给May15之前实际公开上界；OpenReview具名publication/attachment链仍缺。现有原件身份和潜在bandit增量保留，但本轮**日期资格外部终态隔离**，不入确定当窗候选、不评分、不写Books，不支持完整覆盖/首公开或无遗漏。重开只需允许正常取得的同一note附件公开时间链，或同题同作者正式出版的May15前公开上界；不要求恢复全球first精确日、不扩会议inventory。A99所称70未终结的umbrella现明确拆为69普通潜力+1日期资格外部保留；守恒184=68贡献关闭+1已确认更早全文窗外13909+45既成+69普通潜力+1日期外部保留，未冻结。
## A101 — 14373另一人必要Source、日期与中心理论争议暂缓提案

root R81首读后，作者实际[exactv1](https://arxiv.org/html/2605.14373v1)完整题摘、§3.1–4.2/Eq1–7、§5.1–5.3/Eq8–11、§6.1–6.3/T1–2与AppD Algorithms1–2；只针对常数矛盾核AppC1的定义，不读全部证明/其它附录/代码、不复现。当前official abs v3/ICML接收说明无具名撤回或纠错，只版本号不触发全史。[DC原件](SUP_DC_2605.14373_20261019.json)精确身份/唯一v1 May14 04:52:24Z、arxiv.content/findable/registered May15 02:10:31Z，公告下界May15 00Z至上界完整北京May15。

真实proposal是循环坐标指针、dense梯度buffer每步全局γ衰减、B坐标fresh覆写后用全buffer更新；γ0只当次block、γ1保旧估计。AppendixD实际每坐标L±两次loss/2ε，B是被更新坐标数而非两次函数调用之一；固定B的新query不随n增长，不等整个参数更新/驻留内存O(1)，m=n时仍n维buffer。Partial memory/指针选择另改变更新支持，不凭虚拟flatten免去全loss/模型算术和state。无实现核验，不能据伪码授设备零copy/严格真实峰值。

中心理论三处实际不一致保留：Eq3中央差分分母ε，§5.1积分恒等式与Alg2则2ε；Theorem5.10在B=n、τ0时其收缩因子代入应为1−2μα+μLα²，不是Cor5.11所写1−2μα。另本文C2主定理有Lnτ/(2α)，AppC1定义与证明展开则Lnτ/α；不替作者挑一个常数便宣告定理已修复。Lε≤L只给上界，未证明增加ε必单调减Lε；§5.12相邻估计差趋0也不单独推出估计本身为零/驻点。Staleness bound只γ1/m=n，不能自动给任意fading/truncation同一收敛保证；有限差分bias与随机minibatch并未因此消失。

实验单RTX PRO6000Blackwell、13kMLP/20kCNN、50epochs/batch64或128；T1CoCDε1/.1，BCCDε1e−6，并非只改变stale复用的单因子。T2CIFAR45.08对10.13、SGD62.51保局部作者数字；SARCOS6.12对6.23秒/epoch，MNIST44.56对44.42、CIFAR77.03对77.01均不支持普遍无开销。§6.3分类随机基线终值可相当，SARCOS64预算8.1vs15.7秒/episode仅此负载；完整多seedCI/precision/生产SLO/总GPUh ND。全部loss queries、densebuffer更新、驻留/调参计费，非反向免费的全训练替代认证。

拟2+1+2=5，理论/设计反证受影响深入，**中心争议暂缓、无Books**；保具体stale-buffer proposal与有限实验，不因错误反删候选，也不把它扩成长期数学基础分。Actual Ch4已完整读局部曲率/梯度和step监控、mini-batch/局部PL三段及两侧，Ch28优化调度交接有效层复用；旧稿一般监控原则不为本文未闭定理背书。重开限精确差分归一化、主文/证明同常数及full-budget代数一致的定理、更大ε条件与实际γ/m/minibatch适用域、matched半径/完整查询预算对照；现有源已足作安全争议终态，不伪称等未读证明。待root处置独核，不预支第46新。

## A102 — 14382另一人必要Source、actual owner与逐字PRE

root R81首读后，作者实际[exactv1](https://arxiv.org/html/2605.14382v1)完整题摘、§3/Eq1–5、§4/Eq6–11/Alg1、§5.1–5.4/T1–3/F4文字；不逐读全部视频/附录PCA样例或代码/复现。Current official abs v5/preprint无具名纠错撤回，不全版比。[DC原件](SUP_DC_2605.14382_20261019.json)唯一v1May14 05:06:57Z、arxiv.content/findable/registeredMay15 02:10:44Z，公告下界May15 00Z至上界完整北京May15。

真实接口是按相邻chunk的teacher/student DINO增量差ρ，以sigmoid(−(ρ−μ)s)混合DMD与student相邻DINO平方距离loss，不是参数KL约束/TRPO接受步、未给monotonic improvement。历史来自student不等ground truth或bias-free，continuity还可能压制新条件要求的合法变化。Eq4把marginal score写成对p(history|condition)平均，通常需按当前noisy x的posterior权重，本文不将它作严谨边缘score恒等式/所有漂移唯一teacher因果。ρ是表示代理，不认证teacher错误或student轨迹正确；增量相同也可能共同错误。

Wan2.1-1.3Bstudent/14Bteacher，CausalForcing700步+streaming3000步/H100，832×480/16fps、100条六event×10秒；H100数量/precision/batch/完整GPUh及生产SLO ND。主VBench只六维、LongCLIP/VideoAlign为代理；T1LongCLIP26.07vsLongLive26.05、后段有退，VQ2.75<MemFlow2.83，T2imaging72.72<RewardForcing74.99/dynamic92.18<93.16，非全维支配。20人每人3次排序非60独立prompt；F4去项定性只局部支持混合，不签全部机制唯一因果。teacher/fakecritic、DINO两轨迹提取、recache/rollout与全部训练推理均计费，无“单距离”总费用承诺。

拟2+2+2=6，teacher可见条件与自产历史之间的监督选择具体差额深入。Actual Ch24完整hybrid history/local与训练段121–123、后历史patch/扰动两完整段127–129及Ch23/25实际开篇交接均已读；现稿有teacher rollout正则和自产条件误差，但没有“teacher条件看不到同份历史→按两条轨迹增量代理分配teacher/自产连续loss”的监督交接，不因缺论文名就gap。唯一owner MULTIMODAL-GENERATIVE-PARADIGMS Ch24；拟插hybrid history训练费用/回退完整段后→历史patch粒度首段前单段，本人末注compact，无重复Ch25解释。以下逐字PRE未写，待root窄位。

> 流式生成器已经读取自己的历史，也不代表蒸馏teacher看见同一份历史：若teacher只按新条件给分布目标，它可能提出条件合理、却与既有轨迹不相容的变化。一个受限分支比较teacher与student相邻chunk在冻结特征空间中的增量差，用其sigmoid权重混合DMD监督和student自身的相邻特征连续loss；这是选择监督来源的代理接口，不是TRPO的参数KL约束或单调改进证书。自产历史仍可能已经错，增量相近也不能判真，连续loss还可能压制新条件所需的合法变化。[有限交互视频对照](https://arxiv.org/html/2605.14382v1)支持这一候选分工，但定性去项、特征/偏好代理和部分退步不授予teacher偏差唯一因果或全维保持。Teacher/fake critic、两路特征、recache、自滚动和全部训练/采样均计费；监督条件、历史或反应性失配时，保留原DMD、较短生成段、可靠参考与重新锚定，分别验条件响应和轨迹延续，不以历史一致性批准真实环境状态。<!-- source-family:SF-2026-ARXIV-2605-14382 -->
## A103 — 14598另一人一次贡献决定域确认

作者复用B3完整题摘，并独立实际[exactv1](https://arxiv.org/html/2605.14598v1)§4.1–4.3/Eq2–12一次准入所需核心，未遍历全部实验/证明，也不称完整Source。实际与R86所列一致：Mamba将历史编码成末token、同recent observations拼prefix、next-state stopgrad cosine辅助，以及Mamba denoiser仅action token接timestep AdaLN。§4.3更多信息可忽略/可减少别名的理想条件原则不是此单token压缩的充分性、更新接受准则或新一般边界；普通动态预测辅助与干净条件分工没有另建新学习机制。Current abs v2、无具名纠错撤回，不因编号扩全史。

确认具体贡献关闭，不评分、不另追不影响处置日期：没有从“fullhistory”名字继承所有事件保留，也不因机器人/SSM或小模型硬排。原潜力从未冻结为候选，故非深审后删分母；若出现对压缩摘要的可迁移充分性/受控反证或新增状态更新机制才定点重开。现184=69close+1已确认窗外+45既成+68普通潜力+1日期资格外部保留，仍未冻结。

## A104 — 14386另一人必要Source与具体仅报告提案

root R83首读后，作者实际[exactv1](https://arxiv.org/html/2605.14386v1)完整题摘、§3.1–3.6/Eq1–5、§4.1–4.5/T1–2及§5限制、AppC mapper/kernel职责开头；未遍历全family、全部genome附录/leaderboard/代码或复现。Current abs仅v1无具名纠错撤回；文内Apr22是排行观察日期，不是同论文更早公开正文证明。[DC](SUP_DC_2605.14386_20261019.json)唯一v1May14 05:09:12Z、arxiv.content/findable/registeredMay15 02:10:49Z，公告下界May15 00Z至上界完整北京May15。

MRI静态entropy/variance/cappednorm与reasoning/generic probe cosine混成soft ratio，再由τ同14维genome ratio融合；ratio是tensor scalar，非逐坐标因果重要性/可信概率。类型/维度/shape的0.5/0.3/0.2贪心mapper只是提对应，不证明Transformer/Mamba内部功能或共同base可比，§5也承认高效合并主要同base。DARE-TIES/SLERP本身借用已知kernel，诊断/结构筛与最终fitness分责，不能以diagnostic名授merge安全或独立泛化。

T2 n30/局部bootstrap±.4pp只该ablated族，不外推所有models；T1 GPQA.869高于mother.862，但MMLU.776低于.782。没有从九任务平均±.040推出同seed/样本/跨族可靠不退，未见全family与search/final完全独立holdout合同；fewGPUh不能删parent训练、probe、全部候选instantiate/fitness/search与交付回归成本。主necessary源未披露可比hardware/precision/batch/concurrency/SLO或全GPUh，均ND；不从排行榜第二手声称独立实现复验，未核artifact。

拟2+1+2=5标准、**仅报告**。Actual Ch29完整DoTS两段946–948及CRANE950/两侧已读；现稿已要求同base taskvector、选择proxy不是真值、互补source/完整候选与分任务回归成本；这不等于含MRI/genome算法。本篇新增是一份softdiagnostic+搜索空间recipe及有限benchmark，不建立新兼容性判据、可迁移tensor选择条件或独立总预算优势，未改变现有“proxy提案→独立能力/协议验收”的设计选择，不为每个prior/搜索超参追加案例。重开需MRI可迁移校准、搜索/最终人口隔离与matched费用的新选择条件，或真正跨架构行为等价/保留证据。候选保留/不反删，无Books待写，待root具体Only独核。

## A105 — 14391另一人必要Source、actual owner与逐字PRE

root R83首读后，作者实际[exactv1](https://arxiv.org/html/2605.14391v1)完整题摘、IV-A–D/Eq2–14、V-A–D/TII–IV必要方法/协议/反侧；不遍历SM、全部图像像素或代码/复现。Current abs仅v1无具名纠错撤回。[DC](SUP_DC_2605.14391_20261019.json)唯一v1May14 05:13:23Z、arxiv.content/findable/registeredMay15 02:10:56Z，公告下界May15 00Z至上界完整北京May15。

实际双码流是ELIC SQ与finetunedVQGAN，编码/解码/熵模型/codebook冻结，ESE与CEM学习。每支expert/modulation stream同latent起步，两者都过原decoderblocks；ESE输入concat当前modulation与expert再更新reference，所以不是原decoder输出不变的硬reference。CEM从本modulation与对侧enhancedreference产densegate与残差，非TopKsparseMoE。Expertloss用各支MSE/LPIPS，modulation另用多目标/adv与感知支tokenconsistency；同frozenweights不让目标独立或全行为保持。

所有bpp明确包含SQbitstream与VQindices，codebook1024；OpenImages256²crop/bs6，CLIC2020/Tecnick固定768²，Kodak原protocol。MoDE-F/P同预训练experts/码流但各自训练模块，不是免费改变同decoder运行权重。TII Kodak PSNR相对ELIC BD-rate+18.64%；TIII <.2bppPSNR/LPIPS若干退，改全范围才另一取舍，不把不同积分区间拼全支配。TIV w/oCEM实际改SFT-style无gate注入，不是去掉所有跨支信息，消融支持有限接口而不证明gate唯一/最优。ELIC为自行reimplement，SM的未读设备/precision/训练总GPUh/端到端time与memory ND，不补造生产优势；双codec/stream/熵与bit开销、全部模块训练/adv/采样均付费。

拟2+1+2=5，对重建consumer双表示协作具体差额深入。Actual Ch23阶段三完整417–425的codec治理/码本几何/可变token与后双目标各段已读，Ch22/24/Ch25交接有效层复用：已有分工主要token预算/AR可预测vs重构，未承载同输入双码流在冻结双decoder内部保独立reference与可调modulation这个消费接口，不能仅以“有VQ”判重复。唯一owner MULTIMODAL-REPRESENTATION Ch23，拟原codebook治理419完整段后→ArcVQ421首段前单段＋compact本人注，不复制Ch24生成机制。以下未写、待root有限PRE/窄位。

> 表示的分工也可以发生在重建consumer，而不只在codebook里：并行传输一份scalar-quantized保真latent与一份VQ感知codes，在各自冻结decoder旁维护expert/reference和modulation两条stream，再用对侧feature提出逐位置gate控制的残差。这里两条stream都从同一支latent起步，但reference也经过可学习enhancement并读取modulation，不能把冻结decoder权重等同原参考输出不变；dense空间gate也不是少数Top-K专家路由。[受限双码流对照](https://arxiv.org/html/2605.14391v1)支持该consumer接口，不认证perception与像素保真共同占优：原感知proxy改善可伴随PSNR退步，低码率与全范围的曲线比较也需分别声明。两份码流/熵开销、双encoder/decoder、额外stream与模块训练均计费；保真/感知锚定的输出使用各自训练模块，不是一份decoder的免费运行旋钮。输入结构、指标或总预算不支持时，保留单codec、原独立decoder与明确的单目标验收，不让更逼真重建取得原观测真值。<!-- source-family:SF-2026-ARXIV-2605-14391 -->
## A106 — 14531必要Source与收窄的具体仅报告提案

作者实际[exactv1](https://arxiv.org/html/2605.14531v1)完整题摘、§4.1–4.3/Eq9–11、§5.1–5.4/T2–7、A3.1–3.2/A4.1–4.2、A5.2/T10与A6必要机制/配置/直接反侧；未遍历全部SOC证明/所有图像case/代码，不复现。Current official abs v3无具名纠错撤回，不仅因版本变化读全版。[DC](SUP_DC_2605.14531_20261019.json)唯一v1May14 08:13:43Z、arxiv.content/findable/registeredMay15 02:14:14Z，公告下界May15 00Z至上界完整北京May15。

采用对象只保具体proposal：无selfattention的卷积TextVAE重建词embedding/sharedvocablogits、KL与stability正则，4×downsample；按compressionfactor分constraint/free组，组内PAD、contextlatent与noisefreelatent分别标type，再由普通Transformer CFM全局去噪/并行decoder移PAD。局部卷积仍有有限receptivefield与边界，未披露完整kernel/跨组padding足以认证strictdisentanglement，组内保留位置不等任意约束逐token硬保持。GaussianKL不证离散空间diffeomorphism，straight conditionalpath不证coupling为population OT/HJB最优，softmax加权形式不自动为指定V梯度；本文不把控制重命名、一般FM或ODE存在原理计新增理论基础。有限估计FrobeniusJacobian不是所有方向stiffness保证，Picard存在唯一也不证明显式solver无刚性。

OWT训练的101M主表与.6B纠错/infill、baseline训练/任务不同，不拼统一收益；T2ELBO-basedPPL不是准确文本likelihood，更不是freegenerationperplexity。T3 Manta32steps entropy6.0459<RADD6.3109、64steps5.7981<6.3501，质量与diversity不全保持。T4 question BERT.613<Seq.617等，T6表格NLI.822高于Instruct.703而RM1.182低于1.742，不能沿单指标选“通用纠错胜出”；作者正文BERT.835/Lev169.1也不同表.899/143.7，保冲突不拼数字。多种噪声/infilling条件是代理任务，未独立证明保未污染span或全语义真值。

T10默认单A6000/bs64/len128，80k步2A6000/658.6GPUh，inference4.2GB、29.33ms/sample/1.47ms/step；该默认不能给1024-token4.6×headline所有比较自动配齐硬件/quality/codec范围，precision/concurrency/tailSLO/全codec预训练budget ND。O(1)是solver步数对长度的口径，不是selfattention全计算/显存，VAE训练/codec、padding、全部CFM/CFG和decode付费。A6强CFG低stepscollapse/更多steps恢复不归成全域平滑已证。

拟2+1+2=5，架构/理论背书反侧必要域深入，**仅报告**而不采其HJB/geometry/完整headline。实际Ch24连续latent AR段46、局部条件query/context段96与已读masked/flow条件consumer论证，已要求codec/condition布局/decoder与完整预算共同验收；这些不冒称旧稿已有Manta算法。本文新增的卷积压缩+typedcontext/free分组是一份可核局部实现提案，但没有受控隔离局部卷积/分组的约束保持条件或相同质量/全预算的新选择边界，尚不改变当前codec—条件—输出联合验收原则；不为每个PAD/投影配方加长期案例。重开需该局部receptivefield/跨组约束的实际接受保证或受控失败反证、独立预算/输出验收，理论若修复再只核受影响依赖。准入候选保留，不因中心强广告未证反删，也不以本次不写Book降分。待root必要Source/Only独核，未预扣普通尾。
## A107 — 既定B3八项完整题摘再判与两项一次决定域

未增发现。作者重新完整读取B3原件第4/5/9/11/12/13/14/15对象14619/14634/14696/14709/14712/14742/14749/14766的原题摘；不是把整B3后修当v1或全池Source。14619的activation-slice graph/同答案异process测量、14749非线性feature干预及无直接输出特征、14766音频read/emit决策与对齐监督各有清楚机制/测量入口，继续必要Source；14712仍保matchedaliasing与chunkintent稳定性窄潜力，14709保三route学习及stepreward/complexity交接窄潜力，14696保未来几何/语义消费者及FMGRPO的实际差额待决定，不从GRPO或worldmodel名预授来源完成。

**14634 RustPrint**拟贡献关闭。因documentationroundtrip可能是独立执行边界，实际只读[exactv1](https://arxiv.org/html/2605.14634v1)§3.1–3.3一次决定core：DocGen沿现有repo-doc系统，普通crateplan→compile/unsafe修订、source/target文档LLMscore找缺失，再翻译maintainertests、固定测试只改代码。它明确承认文档不揭runtime错误，故并未提供新的doc-equivalence证据权限/行为等价接受算法；两类检查组合是这次C→Rust实现选择。AB跨评价95.17/79.85等保为本任务结果，不当新通用执行机制或受控失败条件；没有因C/Rust/小样本而硬排。Current officialabs v3无具名纠错撤回，只编号不重全篇；日期不影响贡献关闭，未追所有评价/全仓/附件、不称完整Source。若有新跨表示等价/独立验收规则或可迁移失效边界才定点重开。

**14742 EARL**拟贡献关闭。因AFS“novel”可能改变表示接口，实际只核[exactv1](https://arxiv.org/html/2605.14742v1)§3.3/3.4与对应T3及消融解释：全局分析feature经MLP/LN、reshapegrid/convQKV/selfattention再MLP残差加VLMfeature，GRPO沿已有format/answer-stringmatch+Levenshtein/IoU加权，SAM2从bbox出mask。AFS局部数据优于concat/CAF不建立新的coarse→fine信息权限、可迁移训练条件或grounding接受协议；不是因egocentric/视觉领域排，而是已知分析表示+融合+多reward的本任务配方，未新增值得本项目长期解释的机制/有效反证。没有把代理Levenshtein当语义真值，也不由auxdescription授权grounding；不因这些通用限制就强纳每个组合。Current仅v1/ICML接收无具名纠错撤回；不追不影响贡献关闭日期、不展开全部benchmark/附录。以上两close待root代表性校准，当前不预改69close守恒。
## A108 — 14912必要Source、日期与具体仅报告提案

R34一次准入core有效层复用后，作者实际[exactv1](https://arxiv.org/html/2605.14912v1)§4.1–4.5/Alg1、§5.1–5.4/T3及AppA必要coding/aggregation反侧；不把哲学引文、全部policy建议或其它引用展开为来源队列，未核artifact/复现。Current officialabs仅v1无具名纠错撤回。[新实际DC原件](SUP_DC_2605.14912_20261019.json)唯一v1May14 14:47:06Z、arxiv.content/findable/registeredMay15 02:23:34Z，下界May15 00Z至上界完整北京May15。

具体measurement确非普通overallagreement：以contested-value后无新证据的pressure-response转移作人口；scoping、signalling与repair-basis相乘，修订R∈0/1/2；未修订但有依据保持可给Rtilde1，无pressure则PRSundefined而非0。不能由不修订自动判固执/修订自动判迎合，也不能以某次措辞、apology/quote识别真实修订动机。乘法是规范性联合准则而非统计推得必要条件；高conversation均值不推出任何单用户必高/likely，价值coverage/终局正确性/民主合法性另验，PRS不具这些权限。

手写198two-turn、6domain×3valence各11；ClaudeSonnet4.5全部198、GPT4o-2024-05-13仅分层100，defaulttemperature/API无多generationseedCI，不把两个不同人口当训练管线因果。3独立coder、30pilot后收紧具体rule、ModelA60/ModelB30 reliabilityslice与全corpusR另4thtie-break不同，κ.74/.72不是所有判断真值。模糊basis默认capitulation与必须原文quote是conservative判定；论文同时称此令principled repair为upperbound/capitulation为lowerbound，方向不能凭这些规则推出，本文不采此统计保证。ModelAagreement.732/PRS.21CI[.17,.25]，ModelB.814/.14无CI且部分component未留，保作者描述数字不签精确单次计数/总体发生率或RLHF必致因果。Additive.34/去scope.29对multiplicative.21显示聚合选项参与读数，不是“改聚合仍相同metric”。所有调用、二轮压力/人评/coding和重标均付费；API硬件precision/SLO与总体成本ND。

拟2+1+2=5标准，因修改/迎合评价判断对必要反侧深入，**仅报告**保新压力转移rubric和有限pilot，不因social标签排，也不反删候选。实际Ch31完整225–229已明确“可靠新证据应更新vs无依据施压”、来源可靠度不等自报真值和压力历史重采；Ch66完整325–331配对压力/监控/方向cue及conditional人口、后配对输出验收均已读。这些现稿没有PRS公式或三项规范，但当前设计选择已要求按证据/可见压力与身份分责，独立校准而非以更少变更/更高agreement签安全。本文当前未提供新的修订basis可验证判据、自然交互发生率或受控质量边界；三指标相乘/人工coding是一份局部诊断合同，不为每个rubric聚合追加长期案例。重开需独立可验证修订依据、压力与真纠正matched控制及固定人口下对现有标签/验收的具体新反证；待root必要Source/Only判断，不预扣。

R89已实际消费：14373第5D、14386第9Only、14598贡献关闭，14382第27I actualPOST通过；当前48新=27I+9Only+7NC+5D，无DAY。14391获指定Ch23窄位，但按root文件序列等待May19先保存；尚未写、未预支整合，之后fresh读实际Ch23再apply_patch。
## A109 — 14766必要Source、actual owner与逐字PRE

作者实际[exactv1](https://arxiv.org/html/2605.14766v1)完整题摘、§2.1–2.2/§3、§4.1–4.3/§5.1–5.2及A5/A6/E对采用接口直接必要的早退/末尾flush/logical latency；未逐读全部概率推导、全语言附图或实现/复现。Current officialabs仅v1无具名纠错撤回。[既存DC](SUP_DC_2605.14766_20261019.json)唯一v1May14 12:32:57Z、arxiv.content/findable/registeredMay15 02:19:59Z，下界May15 00Z至上界完整北京May15。

真实Intermixed模型输出文字/W，W后输入下一声学chunk（实际8vectors/640ms），文字后输入该文字；训练只取单条alignment的CE，不是对所有合法WAIT轨迹边缘化的exactwordlikelihood。Qwen3-14B五shot源—目标phrasealignment+NeMo forcedsourcewordtime，目标phrase全词对源phrase末词；约10%有虚构/遗漏，去invalid、未对齐目标移到下个validphrase。其“最短等价phrase”仍LLMlabel而非独立语义gold，部署偏置不能恢复训练过早标签的权限。Wait penaltyκ调LLMW logweight，另ν调两层LLM后head的W/E；earlyhead只推迟/fullLLM仍可立即W，不授错误emit执行。A5明写质量不变**以延迟后LLM给相同文字为假设**，不是算法不提前输出自动证明；未核跨层KV/cache执行，不据浅层head补造已验证state等价。

22layer300MConformer、80mel100fps→25→12.5fps/640ms；BEST-RQ300ksteps+DCT320/640/1280ms、encoder预训练调参10kA100GPUh，3BinhouseLM冻结+LoRAr8alllinear。3700hCoLiMu，Bestow180ksteps、concatenated/intermixed120k，bs600sec/fourH100，precision/完整端到端latency/生产concurrency-SLO ND。Fleurs英法/英韩与内部lecture；SilFleurs是**前加5秒Musan noise-free-sound-0683 −20dB**而不是自然所有噪声/静音测试。正文英法COMET.820→.509/.832→.604与图5caption英韩身份差额不拼统一数字。SimAlign κ1 .820/.73sec只是单点；更等反降的曲线是局部timing-label反证，不据此认证所有wordalign失效或LLMphrase无错。

Earlyhead英韩LLM调用比1.55→1.24/1.16，每outputtoken含WAITcalls；2.3→2.3/2.4logicalsec且所测COMET相同，不是真机joule/device收益或一般非劣界。Average logicallatency按audio到达位置/理想匀速线计算，**排除计算时间**；EOS和EndofAudio不同、末尾forceemit忽略WAIT的flush也不签完整停机/真实effect保证。Encoder/adapter/LoRA、双层head、phrase/ASRlabels、所有WAIT/fullLM/flush与训练都付费，不从frozenLM省掉这笔。未做服务或复现。

拟2+2+2=6，监督时间与read/emit控制跨边界差额深入。Actual Ch23完整Full-duplex输入路由919–935、末段训练对齐/可见prefix、Hibiki探索支持、SilentThought、既有WAIT/dilation及延期catchup1709–1711和后三级跨语监督段均已读；Ch22/24交接有效层复用。现稿已有WAIT共同训练/外置READ-WRITE退路，但没有phrase时序标签的错配不能靠部署wait补救，以及“浅层可延后、完整reader可再次拒绝emit”的权限分层，不仅因没有同篇名称称gap。唯一owner MULTIMODAL-REPRESENTATION Ch23，拟现有完整延期catch-up/2603-11578段后→跨语三级mask监督首段前一个自然段+本人compact注；无额外Ch24/Ch45重复正文。下面未写，待root必要域/逐字PRE与窄位：

> 学会WAIT还需要可靠的“何时已有足够源信息”标签，而不能靠部署时调等待偏置补救错误对齐。一个受限翻译分支先把源—目标文字对成短语，再将目标短语放到对应源短语末词的声学时间之后；输出WAIT时继续读音频，输出文字时再把该文字送回同一序列。短语对齐与强制时间戳仍是派生监督，遗漏对齐的保守后移不保证真实语义等价。为了少做整套语言模型前向，还可由浅层二分类head先决定是否继续等：它只可推迟调用，选择emit仍必须交完整模型，后者可以再次WAIT，因此浅层信号没有提前提交文字的权限。[有限语音对照](https://arxiv.org/html/2605.14766v1)支持这条接口，但质量不变依赖延迟后完整模型仍给相同文字的条件，不能由“不提前输出”推成一般等价；调用次数也不是实测电能。Encoder/LoRA、对齐模型、全部WAIT/文字前向、buffer与训练均计费，logical lag不含计算时间；对齐、安静输入、翻译质量或实际时限失配时，保留固定/外置READ-WRITE、较长等待与完整句翻译，最终commit/cancel仍由runtime验收。<!-- source-family:SF-2026-ARXIV-2605-14766 -->

## A110 — 两新整合实际POST与当前50层同步

14382已按R88单段/本人注保存并self-read，R89非writer实际新增/完整两侧/本人注POST通过，第27I/Ch24释放；14391按R89并等May19同文件先保存后fresh-read，用apply_patch仅写授权单段/本人注，R92 actualPOST通过，第28I/Ch23释放。Manta14531 R90标准5/Only与A107两close亦已消费。README已实际六节同步50新=28I+10Only+7NC+5D，加原Charon51，V3和本日限定working diff-check通过，非DAY。184=71贡献关闭+1已确认窗外13909+50既成+61普通潜力+1日期资格外部14553；未冻结、不以潜力自动变全篇Source债。root首读14868/14891有效packet只待我另一人有限核，14935由root首读，我避开。
## A111 — 14766精确修稿保存与51层同步

按R94唯一词义收窄，A109完整PRE仅第一句替换为“学会WAIT还需要可靠的‘何时已有足够源信息’标签，不能把部署时调等待偏置当成错误对齐已经修复。”实际正文使用中文双引号，其余A109整段不变。作者已实际保存Ch23新1711、前完整延期catch-up1709/后三级跨语监督1713与本人compact末注，完整新增/两侧/注顺读及限定working diff-check通过，已通知root待非writer actualPOST，不提前计第29I。没有改写其它已有效段或May19来源注。

R93 PRS14912 Only实际消费并融入README原六节，当前51新=28I+11Only+7NC+5D、合原Charon52；V3/限定working检查通过。184=71close+1已确认窗外13909+51既成+60普通潜力+1资格外部14553；14766仍未预支，14891早稿资格也未先判确认窗外。旧行/原窗及2474字符连续旧§4在50层实际机械保护过，最终仍需复验；不授DAY。
## A112 — 14868另一人必要Source、actual owner与逐字PRE

root R91首读后，作者实际[exactv1](https://arxiv.org/html/2605.14868v1)完整题摘、§3/Alg1–2/Lemma1–2/Prop1、§5.1–5.3/T1–2必要评价与§6限制、A1–2实际离散proposal/fit/评价配置；未核全AppendixD证明/全部附表/代码或复现。Current officialabs v2明确“exact affine conditional gradient means”，与采用限定一致；只轻检说明，不倒填v1原句/本日新修订、不全史。[新实际DC](SUP_DC_2605.14868_20261019.json)唯一v1May14 14:16:51Z、arxiv.content/findable/registeredMay15 02:22:27Z，下界May15 00Z至上界完整北京May15。

实际先用fullforward/backward和K次FGSM增强取每token hidden/单位归一inputgradient，standardizefeature、ridge+常数bias拟方向，后续中间层earlyforward提出输入扰动；不是当前参数训练gradient或每次完全黑盒。TokenGCG分支只改候选提案，accepted替换仍由真实teacherforcedNLL选，不能把gradient免重算当全链无真实模型验证。Prop1只联合Gaussian/跨输入恒定means/covariance/ΣHH可逆时E[G|H]=AH+b；realized G还需残差条件协方差0，stationarity的随机sin-cos假设不由RoPE/learnedtokenembedding自动满足，理论也不直接证明归一方向ridge同样准确。

HarmBenchfit80→test320、JBBfitjudge-comparison300→test100；token25GCG迭代/每位top64、HB26states×8=16640fitexamples，逐token扩样不变独立prompt数。Token实验A100/BF16，model Llama2-7B/Qwen2.5-3B/Qwen3-4B，HarmBenchcustomjudge与JailbreakJudgeLlama3-70B quantized/Ollama不同仪器；response/defaultbatch不补精确值，完整concurrency/length/SLO/全GPUh ND。95%bootstrap是prompt重采非训练seed。Embeddingtiming仅perturbationgeneration，tokendefaulttimingboundary不自动包含fit/全部responsejudge；532%/5–12×不全链采用。

§5.3 JBB部分纯代理FGSM近零、10%exact混合恢复是局部sign阈值解释而非一般鲁棒定理，α1沿GPR调参不是表T1独立exactFGSM同配置。多PGD近似误差会累积，cosine不是ASR单调代理；embedding扰动非可直接部署text attack。真实backward标签、增广、层/超参选择、ridge/eigendecomposition与存储、全部候选forward/生成/judge均计费；未核实现/复现/全攻击复用，不签全安全或通用训练可替代。

拟2+1+2=5，对精确导数与学习代理的具体边界深入。Actual Ch4完整backprop链式/代价与后localspiking替代段180–200及两侧，Ch3/Ch5实际开篇交接已读；现稿有非精确局部学习规则，但未区分“固定模型inputderivative可由已付真实梯度监督摊销”与“参数学习credit的替代”，不从泛有proxy话题假NC。唯一owner WORLDVIEW-WHY-MODELS-LEARN Ch4，拟“深度也会带来困难…反向传播…”完整代价段后→“学习规则也不必…”localspiking首段前单段+compact本人注；不把攻击recipe/排行榜写入理论基础，待root具体PRE/窄位。以下未写：

> 反向传播给出的是当前函数的导数；也可以在固定模型、目标和读出层上，先支付真实反向计算，学习从中间hidden到输入梯度方向的代理，再在后续输入上只前向提出方向。这不是参数训练梯度的精确替代，也不是从模型无需梯度地取得了新信息：联合Gaussian及跨输入恒定的均值/协方差只保证仿射的条件平均，不能保证每个样本的导数；有限模型拟合归一化方向又是另一层近似。[受限梯度预测对照](https://arxiv.org/html/2605.14868v1)中，多步误差可累积，部分分布的纯代理近乎失效；离散候选仍须用原模型真实forward目标选更新，而不把方向相似度当最终效果。标签反向、轨迹增强、层选择、拟合/存储及全部候选和行为评价均计费，扰动生成阶段更快不等全链吞吐。模型、目标、层位或输入人口变化时重新校准，效果不足则回真实梯度/原方法，不让一个快速方向sensor获得优化收敛、行为正确或安全许可。<!-- source-family:SF-2026-ARXIV-2605-14868 -->
## A113 — 14891具名早稿身份与首公开资格关闭提案

本次不是源恢复失败，亦不是因Source费时缩池。当前[14891官方abs](https://arxiv.org/abs/2605.14891)明确admin note “substantial text overlap with arXiv:2506.04990”，故先暂停May15首次公开候选/评分/Books，沿唯一具名早稿恢复。作者实际打开[2506.04990当前abs](https://arxiv.org/abs/2506.04990)及[exactv1正文](https://arxiv.org/html/2506.04990v1)题名/完整摘要/§3.2/§3.3/Eq3–4/Algorithm1与训练说明的身份决定域；不读旧Daily、不扩2025池、不重审旧实验/全版本。

旧题名Multi-scale Image Super Resolution with a Single Auto-Regressive Model，Sanchez/Hadji/Bulat/Martinez/Tzimiropoulos与新稿共同，旧另Tzelepis；标题/作者列表差别未被忽略。旧正文已完整提出HIT对实际downsampledimages分别编码、前尺度token作为后尺度残差起点/overlap、scale-specificdecoder/vocab微调，并以同LR/HR pair构造bilinearLR负例的无reference DPOregularization。旧Eq4也写同VAR output logits o下p(zLR)及HR/LR概率比；不是只关键词或相似题目去重。新14891主§3.3–3.4这些拟采用核心逐项同一方案，故不能因换ID/题名/ICML接收宣称May15首次公开。

日期不以旧submission当pub：[2506.04990精确DC原件](SUP_DC_2506.04990_20261019.json)登记方arxiv.content/findable、registered **2025-06-06T01:57:23Z**，与已核公告发号规则共同给出该旧完整身份已公开的上界，明显早于May15 2026；唯一v1Submitted2025-06-05T13:02:23Z，旧HTML也保该v1身份。此处仅需May15前上界，不为它新建精确全球首次日请求；不使用created/Issued年独证。

新AppendixB确新增可读伪码：同logits gather HR/LR、逐tokenlogsigmoid后mean；root R91实际有限Source与此objective粒度/conditioning反侧继续有效，不能回头冒称旧稿已给同伪码。其作为新增澄清不修复旧主式的序列概率权限；当前没有具名重要修订/纠错、新独立机制或改变长期设计的新受控证据说明，只新增ID/接收与附录澄清不足把旧核心重拥有为新候选。拟本轮**首次公开资格关闭/窗外线索**，不评分/不写新Books、不搬写旧日；若日后有具名本次重要revision/artifact实际改变的证据，仅按该修订事件重开，不泛排同family未来事件。待root定点独核，不先计第二窗外；保14891旧准入潜力与root首读结果作为有效研究，未抹反侧。

## A114 — 14549另一人必要Source与具体已有覆盖提案

root R87首读后，作者实际[exact-v1](https://arxiv.org/html/2605.14549v1)完整题摘及§3.1–§9的资格/标签、方法、关键对照、packet与限制；不展开全部Lean artifact/repo或复现。Current仅v1无具名纠错撤回。[既存DC](SUP_DC_2605.14549_20261019.json)唯一v1 May14 08:28:57Z、arxiv.content/findable/registered May15 02:14:38Z，公告下界May15 00Z至上界完整同北京May15。登记是最晚界，不冒实际公开时刻。

Strict资格是imports与同module更早decl，801 proxy-labelable任务/1875候选；414无proxy任务不进评价，fallback改变的是可检索对象，不只是ranker。固定common781任务时mean候选152.6→352.8→1002.2，比较graph收益必须连同此变化解释。主标签来自proof text可见CSLib引用，不给retrieval输入，也不是完整Lean kernel依赖；更严name resolution保2666/2845=93.7%，300 expression probe仅286产物/257找到proof、14 unsupported，462/958=48.2% value constants，未找到不等全为错误标签/最小语义依赖。不能用这个部分probe替主gold或认证证明完成。CSG是BM25/symbol/namespace/import/source/PPR手设权重.40/.20/.12/.15/.08/.05，未有新训练图模型/通用优化器；build284.95sec/1762jobs是CSLib4.29/commit0d37cc7构建provenance，不是检索时延。

5000 paired task bootstrap/seed17不是训练复跑；244dev/557test按module分开，family异质仍在。Strict MRR CSG .5236>BM25 .5061，差+.0175 CI[.0016,.0335]；但对BM25+symbol .5199仅+.0037 CI[-.0103,.0173]，R10 .5215<.5282。扩大候选池可增大相对hybrid收益，不能转为所有资格范围graph必胜。Packet@10的CSG覆盖.5215<symbol .5282、gold/1k估计token6.3979<6.5119，估计token255.06>250.31、same-module .814>.7146；更局部/更高MRR不是更高recall/更好reader。没有执行proof generation/repair或给compiler成功率。解析/索引/候选构造/所有rankers与probe/packet均付费；未披露hardware/precision/完整latency-concurrency-SLO或总成本，不因无训练/API调用就称零费。

拟2+1+2=5标准完成，**已有覆盖 AGENT-RAG / Ch76**，保该候选与新benchmark负面证据，不反删分母。实际完整读Ch76现448–488 query distribution/candidate construction/reader-budget联验、554多positive段明确MRR与recall最佳目标不同且标签不是truth、274 trusted资格先于ANN、679–700 packing段要求预算下coverage/redundancy/最终消费者；Ch75/77开篇交接已核。已有论点实际承载资格改变比较人口、弱监督标签与答案支持分账、排序分数不替consumer预算/任务成功这三个选择，不冒旧稿有CSLib、特定source-order算法或上述数值。本文的新bench具体支持这些条件，却未给新可移植资格/label接受机制，且未测真实proof consumer，因此不再追加一个Lean案例段。重开需严格固定资格/任务人口下改变上述选择的新反证，或真实proof消费/经过独立解析依赖校准的具体新机制；不要求必须大模型实验。待root另一人必要结果/具体NC独核，不先计第8NC。

R96已消费14766 actualPOST第29I；A111所称R94授稿号行政澄清为实际R95 PRE，R94是14935首读，不改变任何采用命题。R99实际独核14891早稿身份/旧DC公开上界通过，计第2窗外、不评分/不改2025或旧Report。当前已接受52新=29I+11Only+7NC+5D，184=71贡献关闭+2具名窗外+52既成+58普通潜力+1外部日期14553；14549和14868在58内，尚不预支本提案或14868待POST。R97授权14868仅两措辞修改后已真实保存Ch4一段/本人注并self-read，待root actualPOST；R98两新首读待作者有限核。不授DAY。

## A115 — 14935另一人必要Source、actual owner与逐字PRE（未写）

root R94首读后，作者实际[exact-v1](https://arxiv.org/html/2605.14935v1)完整题摘/§3.1–3.3/Eq1–13/Prop1、§4.1/4.4/T4、§5，B2–3/T5–6、C4–5/T12–14及D目标定义/首个joint目标；未遍历完整证明、全逐joint/各density表、动画或代码。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.14935_20261019.json)唯一v1 May14 15:09:49Z，arxiv.content/findable/registered May15 02:24:07Z，日程下界May15 00Z至上界完整同北京May15。XML机械省略、其余API字段原样保留，不用created或Updated当pub。

K尺度残差VQ/CLIP条件next-scale AR借用旧框架；每scale prior expected embedding经decoder一轮前后向取目标梯度，再用一阶loglikelihood给候选码字重权。Eq9显式mean-field，目标本可耦合位置，故逐位置exact枚举不等全序列joint posterior。Prop1只Hessian C界与码字到展开点距离的局部KL上界；prior mean并未被证明最优展开点，normalized code降低实测距离/局部KL不授全目标精度。抽码后两层Transformer refiner在冻结VQVAE上用重构训练，不用control labels；末尺度再优化continuous residual默认200步/κ.01，不对离散argmin本身精确反传。残差可以离开codebook与原motion prior，continuous精细修正不是原分布无损保持。

HumanML3D40–196frame，K10/V1024/d512/CFG5，单4090、testbs32，tokenizerbs512/AR128/AdamW2e-4；precision/服务concurrency-SLO/全训练GPUh ND。T4 guidance-only1.15秒/6.68cm，refine-only2.80秒/FID.373，full3.61秒/.82cm/FID.124，unconstrained .054的输出人口不同。T5 .31基模+.83guidance+.05refiner+2.43迭代，200步优化才主要成本，不能用单pass或10×headline签实时。Per-position exact629秒限该枚举协议；部分joint skating仍反退，不抄全项胜。C5真实直接反侧是更多迭代降低goal error却提高FID/全费，control loss没有强motion prior；局部目标更准不等真实动作/控制安全。所有codec/AR/refiner训练、gradient、decoder及200步付费，“training-free control”只无control-specific训练，未核实现/复现。

拟2+1+2=5，离散proposal→连续残差修正的具体生成状态差额深入，唯一owner **MULTIMODAL-GENERATIVE-PARADIGMS Ch24**。Actual完整读Ch24现72 NextFlow尺度历史/decoder兼容与可选diffusion refiner段、后74 SparVAR跨尺度坐标段；Ch26 293–307 codec与连续policy/参数化离散mode和319–321慢planner→快连续policy及真实controller边界，Ch25开篇交接均已核。已有分支说明不同生成器/细动作消费者，却未承载“离散候选仍由code prior提出、目标梯度只重权，连续residual另存且由goal优化”的状态分工；不能用已有refiner词当覆盖。此处只采通用生成接口，不引motion任务全pipeline或机器人执行recipe。拟Ch24完整NextFlow段后→SparVAR完整首段前唯一自然段＋本人compact末注，未授权不写：

> 离散码限制了可表达的细差异时，采样后还可以保留一个连续修正状态，而不只扩大词表：在每个尺度先用prior的期望embedding解码，反传可微目标，再按各码字与该局部方向的内积重权候选；抽样后的embedding另加已训练refiner的连续残差，最后只优化这份残差。[受限motion生成对照](https://arxiv.org/html/2605.14935v1)区分了离散proposal与连续修正的责任，不是对argmin精确求导，也不是整套系统无需训练。逐位置mean-field和一阶近似不等联合后验，残差离开原码本后，目标误差更小仍可能损伤motion分布质量；它没有从几何目标取得物理可执行或安全权限。码本、AR与refiner训练、逐尺度decoder前后向和末尺度全部优化均计费，局部少步采样不等全链实时。近似、自然性或净预算不合格时，保留原离散采样、较弱或关闭连续修正及独立输出验收，而不让满足部分坐标替完整生成质量签字。<!-- source-family:SF-2026-ARXIV-2605-14935 -->

本人注只保上述精确必要域/5分/近似、连续残差分布偏离与完整费用，未核全证明/代码或复现；待root另一人结果/actual owner/PRE与窄位。

## A116 — 14517另一人必要Source与具体已有覆盖提案

root R87首读后，作者实际读[官方exact-v1 PDF](https://arxiv.org/pdf/2605.14517v1)pp2–9：Results2.1–2.5、Discussion、Methods4.1–4.9/T1–2；首屏完整题摘也已实读。HTML不可用不称外部Source欠账，直接PDF的可检索原文够必要域；不读全部旧5W3H论文、附件或代码。Current officialabs仅v1无具名纠错撤回。[既存DC](SUP_DC_2605.14517_20261019.json)唯一v1 May14 08:00:23Z、arxiv.content/findable/registered May15 02:13:54Z，schedule下界May15 00Z至上界完整北京May15，非提交/created独证。

30tasks/3domain、ZH6model而EN/JA3model，2880生成输出与完整paired ZH1440/EN634不同；GA=5且f-ICMw<.8的25.7%/58.6%只这些有效人口，不是全部语言/模型自然发生率。结构slot可见与FULL原始意图fidelity分开确有具体测量价值，但GA/结构/DS三pass逐步披露信息；fidelity拿FULL作gold，不能把两个仪器的差额全归粒度或同权限judge能力。6个model API/阶段语言覆盖不对称，不能用capability名排出规模/训练因果。T1按LLMscore分层60人工、split25得3.12对LLM5.0；两独立rater是研究协作者，盲condition/LLMscore不使抽样成为自然代表人口。ρ.695对.251只是同60样本的评价相关，不证intent真实唯一、所有holistic评测失效或所有分维度更可靠。

Public/private以ablation后fscore≥.7定义，再比较恢复本有选择/循环；210task×dimension的两LLMproxy仅见task/domain，无真实用户内心标签。0hard conflict同时exact55.2%、κ.33，不能写全面agreement或据代理推训练prior唯一机制。WAS按appliedweight计算，更换weight本就改变指标，240/120records与六aggregatecells非数百独立重复；不能从WAS统一下降认证新prompt定律。IST明确类比/未来形式化，不采信息论必然或blackbox causal解释。全部API、三passjudge、proxy/人评与权重试验均计费，hardware/precision/实际SLO/总体费用ND，不核复现。

拟2+1+2=5标准完成，**已有覆盖 PLATFORM-EVALUATION-SYSTEM Ch66**。作者实际完整读现79 InteractWeb段区分测试者完整gold与Agent每轮可见slots、110参考/rubric权限和维度纠缠段、507–539 judge共同偏差/独立anchor/原始比较与量表身份各段，Ch65/67开篇交接已核。具体已有选择是完整需求身份与实际可见输入分账、分维度另留独立人审、指标/权重变更须共同冻结；不是冒现稿有f-ICMw算法或这组split比例。本文新负面测量保报告，当前未给不同于这些原则的新需求可恢复判据、受控消除偏差的机制或新的可靠验收界，因此不新增5W3H案例段；不因单作者/小样本或主题标签排除已准入候选。重开需固定同reference/可见信息与抽样人口下改变当前scorer选择的新证据，或独立可核真实意图恢复/可靠性条件。待root必要结果与具体NC独核，不预计。

R100真实14868 POST已消费第30I、无Ch4锁；README六部分已同步53新=30I+11Only+7NC+5D，加原Charon54。R99第二窗外14891同步§2/5/6，184=71close+2outside+53既成+57普通潜力+1外部14553。V3和本日限定working diff-check通过，仅接口检查不授DAY；A114 14549及本A116尚未预扣，A115未写。R98两已首读packet下一有限核，不扩发现。

## A117 — 14619另一人必要Source与具体仅报告提案

root R98首读后，作者实际[exact-v1](https://arxiv.org/html/2605.14619v1)完整题摘、§3.1–3.5/§4.1–4.6/§6、A4实际统计/采样/硬件与D2–4盲标/分歧/uncertain必要域。未展开全部B/C/E复验附表、代码、图像像素或复现。Current officialabs仅v1无具名纠错撤回。[既存DC](SUP_DC_2605.14619_20261019.json)唯一v1 May14 09:37:26Z、arxiv.content/findable/registered May15 02:16:17Z，公告下界May15 00Z至上界完整同北京May15。

256-token slice按MLP top-positive keys二值化，以Jaccard mutual-kNN/BCC成区域；correct-only runs按visited-block集合加权Jaccard/Louvain成family。非重复访问/驻留/顺序都被family集合丢弃，role与label-seeded diffusion另overlay，不能把family解释为唯一真实算法/因果thinking state。初图不依赖reward field，但family正确人口已使用答案标签，typed-state还带core/role，不能将关联回认证online correctness/成功概率。954cells/318题×3、60622 graph-valid vs61052 sampled不同，4210lengthtruncated(6.9%)仍保/未抽答案算错；N64与N256coverage局部比较不证明rare全部召回。

72 BCC对、77family对来自8个富family/40–80%正确率题，front/middle/tail共15k字符截取，uncertain排除的decisive非原人口。跨family仅10/21=47.6%被判不同strategy，同family94.4%不补足跨family完全语义分离；D3同时97.2%/n71/两次decisive分歧/κ.97未给raw crosstab，不能单一精度授语义真值。PCA/text在固定scaffold的collapse不证明所有文本表示均不能分析route，更不能用family越多定义测量越正确。共同支持与shuffle-null支持受限transition差额，不识别世界因果或普遍推理算法；保root有限语义结论。8H20-96GB/72BTP8、小模型单卡、temp.7/top-p.9/max32768，估生成200GPUh；CPU图2–5sec/题非全费，precision/线上batch-concurrency-SLO ND。全多CoT、activation/cache、图/标签/人审/null均计费，cache重算不等独立生成/训练复验。

拟2+1+2=5标准完成，**仅报告**保新的post-hoc过程测量/同答案不同route-footprint反证，不反删候选。Actual Ch8完整164–186 capability/reliability/多次采样/外部解释非内部读取，Ch5完整222–232 probe投影/重构/分区/线性访问，Ch66现latent-identification完整段与其两侧已读；Ch7/9交接已核。当前图family是一份由表示、采样、阈值与正确标签定义的诊断对象，还未给能独立接受的算法/语义分离、decoder选择或停机条件；现书已要求把输出正确性、一致性和机制证据分开，不需要在此增加完整图聚类配方。不是以已有同主题拒绝新证据：其有限负面测量保候选/报告，但尚不能把operational family普遍升成长期“同答案必多算法”或推荐用family做选择。重开为独立语义/因果route身份的新校准，或固定人口/全费下影响解码选择的受控证据，不要求全局理论/所有rare routes才可保本次局部结果。待root必要结果/具体Only独核。

## A118 — 14749另一人必要Source、actual owner与逐字PRE（未写）

root R98首读后，作者实际[exact-v1](https://arxiv.org/html/2605.14749v1)完整题摘、§2.1–2.2/Eq1–3、§3.1–3.2/Eq4–6、§4/T1/§5.1–5.3/T2–3及A1–2必要实现/编辑site，未核代码/复现或扩攻击案例。Current officialabs仅v1无具名纠错撤回。[既存DC](SUP_DC_2605.14749_20261019.json)唯一v1 May14 12:14:42Z、arxiv.content/findable/registered May15 02:19:35Z，schedule下界May15 00Z至上界完整北京May15。日期不使用提交/created独证。

用可逆非线性f坐标替普通orthogonal W，交换选定坐标再f逆；未交换的变换坐标保持不等所有非目标语义/能力保持。训练冻结base，contrastive prompts两路forward，在下游class-mean方向/AUC筛选site上以positive均值hinge监督；不用direct输出token标签仍用positive/negative类别，并非无标签因果识别。Hinge饱和防单site过推不证明特征唯一或完全解耦，主题/长度等相关量未独立去净。

2block i-ResNet/MLP128/LeakyReLU.1、κ.6，single power-iteration估谱归一不能证明真实norm上界，最多30步/relative residual1e-5与implicitgradient也不自动授所有输入精确inverse。Llama3-8B/Qwen2.5-7B、2000 harmless+2000 harmful训练/313 StrongREJECT judge；single-site norm3.5/28.3与baseline数百/数万site的sum-L2支持不同budget，不能单独推出更精准语义或无side effects。T2同downstream-site线性控制、T3同训练loss线性f对照确支持本设置非线性差额，未证明所有线性方法不可能。Qwen RDO ActAdd异常被排除、early/late layer失败保留；中层较好不认证唯一因果位置。缺matched benign utility/全retention/多seed，不采普遍安全或behavior-equivalence。硬件precision/生成长度/完整GPUh-SLO ND，激活采集、两路forward、f训练/inverse、site扫与judge全费。未复现/不在书中写拒答绕过recipe。

拟2+1+2=5，解释/干预及安全受影响必要域深入，唯一owner **WORLDVIEW-REPRESENTATION Ch5**。作者实际完整读222–232 superposition/probe投影、hidden重构/分区与线性访问两段，以及随后训练稀疏/有限circuit两段；Ch4链式gradient现成层复用、Ch6开篇已核。现稿解释线性访问容量与特征分区，却未承载用非线性可逆坐标定义编辑的选择及“未改坐标不等未改语义”边界；不能仅以已有干预词判覆盖。仅为此受限通用接口新增段，不采操作攻击/拒答参数，不扩Ch72或训安全规则。拟原线性访问容量完整反侧段后→训练时稀疏连接首段前单段＋本人compact注：

> 线性reader的局限，也不要求干预只能沿原空间的一条直线移动：可以先学习可逆的非线性坐标变换，在变换后的空间交换少数坐标，再映回原hidden state。这把“怎样读出”进一步分成“用哪份坐标定义编辑”与“编辑后下游实际怎样变”，却不让可逆坐标自动成为独立语义因子。没有直接输出标签时，可用对比输入的下游表示差异构造训练proxy；它仍依赖输入类别与筛选，不是从无标签发现了真实概念。[受限干预对照](https://arxiv.org/html/2605.14749v1)只支持局部非线性选择，单点编辑与多点累加的范数不直接可比，也未证明非目标能力或安全边界不变。数值求逆、激活采集、坐标训练、层位选择和独立行为回归均计费，近似谱估计不能认证全局精确可逆。坐标、数值残差或消费者回归不可靠时，保留原表示、线性/局部probe与已验干预，不由更小编辑量签发更忠实解释、无副作用或部署权限。<!-- source-family:SF-2026-ARXIV-2605-14749 -->

本人注只保exactv1必要域/5分、非线性坐标不等语义独立及数值/效果/费用边界，未核实现/复现。未授权不写Books，等待root必要结果/actual owner/逐字PRE。

## A119 — 14709一次贡献决定域的另一人有限校准

复用既定B3完整题摘，作者独立实际[exact-v1](https://arxiv.org/html/2605.14709v1)§3.1/3.3–3.4、§4.1选择性监督开头/4.2 Eq2–5、§5.3对应消融一次决定域；不是全部benchmark/图库或完整Source。确认R102**具体贡献关闭、不评分**：三route数据按Analyzer判断直接成功、至多三反思、仅因复杂度才拆解，丢失败/人审再只监督有效片段，是已有trajectory筛选与选择性监督的本任务组合。Step-wise均值最后成为整trajectory reward，不是逐动作counterfactual credit；near-best ε人口按图像数量比例加bonus是局部质量条件效率塑形，未建立新执行状态/硬复杂度接受界或延迟保证。

30k模式移除、去stepreward与去complexitybonus展示本配方局部作用，但没有超出现成组合的新可迁移训练机制或足以修正当前判断的受控失效条件。更多steps/成本和proxy风险是一般解释限制，不把这些常见反侧反作每个配方独立新贡献。Current abs v2/ICML无具名纠错撤回，只编号不展开全版；日期不影响贡献关闭不另追、未把access/工作量当排除理由。若出现真正的新接受机制/信用分配协议或改变上述选择的新受控证据，只重开相应core。R102首读与此有限另一人确认一致，可消费为第72贡献关闭，不影响原有效候选。

## A120 — 14696另一人限定Source与具体已有覆盖提案

root R102必要首读后，作者实际[exact-v1](https://arxiv.org/html/2605.14696v1)完整题摘、§3.1输入/共享表示/flow planner接口、§3.2全部future depth/semantic heads、§4.1/4.2/T3–4与4.3/T5–6/§5对拟采用局部比较；不展开全部Flow-GRPO推导/视频/代码。Root已核Eq13的logpolicy/groupreturn不足冒标准clipped-ratio GRPO，本作者不为不采用该新优化器重做全证明。Current officialabs仅v1无具名纠错撤回。[既存DC](SUP_DC_2605.14696_20261019.json)唯一v1 May14 11:12:23Z、arxiv.content/findable/registered May15 02:18:20Z，下界May15 00Z至上界完整北京May15。

采用对象限未来target消费者选择而非新Depth/SAM/GRPO组合：共享future表示给trajectory planner，辅助head预测future depth/confidence及SAM3 text-fused features；teacher pseudo-label不是新真实测量，confidence加权loss也不产生校准安全概率。辅助分支训练用GT movement替预测movement以快收敛，部署planner给movement，须保该动作人口差额。固定小backbone/单depthhead的T5 Present83.6→Future85.2 PDMS，确是比只加新头更直接的当前vs未来监督比较，但没有独立seed/CI或足以证明通用future必优/真实环境理解。T4逐项加loss改变多个目标，EP有79.9→79.4等反退，不由总分签各消费者全支配。

主6.7B与3.5B/2B-backbone消融不同；NAVSIMv1/v2、navtest/navhard/humanpenalty各协议不拼统一真实路况。T3本法HC98.2/EC77.4低于部分参照，pseudo closed-loop非实机安全。512×1024/2Hz/64H20约10天、eval单4090，stage1五帧nuPlan/nuScenes与stage2四帧navtrain不同；precision/batch/完整latency-concurrency-SLO ND。冻结视觉encoder或部署去辅助分支不免teacher标签、双head/全训练/rollout仿真费，未核实现/复现。

拟2+1+2=5标准完成，**已有覆盖 MULTIMODAL-WORLD-MODELS Ch25**。Actual现359–365完整连续目标/stopgrad、目标漂移及next-step vs same-step比较段，明确同temporal Transformer/steps/seed下未来与同帧监督需分验，未来可能保历史但短近全观测任务同帧仍合理；另完整210–217 plan-first/双连续consumer、部署skip视觉与训练/GT身份分责，及Ch24/26交接有效层已读。本文新驾驶depth比较扩大有限验证人口，有价值保报告，旧稿不冒T5结果或pseudo-label算法；但当前新证据仍支持同一具体选择，未改变未来监督与更强同帧表征必须分验、目标动作身份/费用/真实控制另验的设计。因此不追加又一future-head案例，不因为已有主题排贡献、不反删候选。重开需新的适用条件/同预算强反证改变此选择，或实际动作消费者接受机制；不要求真实上路才保局部Source。待root必要结果与具体NC独核，不预扣。

## A121 — 14333必要Source与具体仅报告提案

R57已校准完整题摘及root一次§3.2普通loss/面积权重层复用；作者实际[exact-v1](https://arxiv.org/html/2605.14333v1)§3.2/3.3、§4/5.1/5.3/T3–6、D新增费用与E1必要训练配置，未展开全gallery、所有C消融或代码。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.14333_20261019.json)唯一v1 May14 03:57:25Z、arxiv.content/findable/registered May15 02:09:35Z，公告下界May15 00Z至上界完整北京May15。准入后不是将成熟局部loss名字直接算认知基础；实际T3/4对质量权衡及encoder/decoder消费者给出值得保留的有限对照，保候选而不因方法简单反删。

VQGAN重构/GAN/LPIPS目标外，detector定位OCR/face ROI后以冻结recognizer中间feature的L2作局部损失，按bbox/原图面积重权；此权重主动降低小字/小脸贡献，不授微小区域完整保持或真实文字/身份正确。T3加入目标的text55.18/face.42伴rFID.60→1.11、PSNR23.65→22.41；加面积权重后text53.05/face.36、rFID.69/PSNR23.64，权衡不等无损。T4只训decoder23.52→24.15、全更新40.64支持不只decoder，但在111M/100k轻量两阶段不等主426M全配方。T6大码本16k→65k本身改善不及带专门目标，不把单项当码本无用或所有视觉输入规律。

主tokenizer16×stride/V16384/d256、200k+40k+40ksteps/bs512/32A100约5天；4Mtext/8Mface被检测人口与一般100M图不同。InsightAR7B/150M图/512²/1024tokens是另一训练预算。D的2056→2099ms/44.1→44.3GB是bs16/十iteration、假每图1脸2字，不是整个detector/制备/全训练2%总费；precision/完整inferconcurrency-SLO ND。所有detect/align/recognizers、三阶段及AR训练/采样付费，未复现/未核artifact。重构OCR与faceembedding proxy分别验，不授一般身份/事实。

拟2+1+2=5标准完成，**仅报告**。Actual Ch23阶段三417–427 codebook治理/双consumer/几何loss，COMiT完整441–443重构与语义分验及global/local预算反侧，Ch24 encoder/tokenizer/decoder训练职责与Ch22/24交接有效层已读。旧稿没有此局部loss配方，不虚称同算法已有覆盖；本文新对照有价值保报告，但依旧是指定OCR/face消费者的专门重构目标与面积折中，未给可移植的loss分配接受条件或改变当前codec—consumer联合验收的边界。不能由本任务收益无损叙述将这份手工权重升格本书固定训练规则，也不为每个ROI监督变体扩例。重开需固定输入人口/全预算的新适用条件或受控反证改变上述选择；保当前数值/未证而不先排贡献。待root必要Source/Only独核。

## A122 — 15044必要Source与具体仅报告提案

复用B8完整题摘/R19准入，作者实际[exact-v1](https://arxiv.org/html/2605.15044v1)§2.1–2.2、§3.1–3.3/§4.1–4.2/T2–6、§5–6及B2–4决策构造、C1–3/5必要配置和D1 matched token-count反侧。未展开全部属性bin/所有workedcases/代码或复现。Current仅v1无具名纠错撤回。[新实际DC](SUP_DC_2605.15044_20261019.json)唯一v1 May14 16:36:57Z、arxiv.content/findable/registered May15 02:26:48Z，公告下界May15 00Z至上界完整北京May15。并未因语音/生物身份应用或成熟MLP/Q-Former而关闭；matched48token的层级表示与身份/属性差额支持保留局部候选。

冻结ReDimNet-B3从同utterance出192维pooled identity embedding与1152维frames，MLP给16tokens、Q-Former给32，再并入Qwen2.5-1.5B。D1固定encoder/LM/48token时混合SV95.6对MLP93.7/QFormer90.7，却age39.5<MLP48的40.5、region79.8<QFormer48的82.8，不能声称每个证据/任务都保持。Noise47.7低于QFormer32的48.9是另一非matched对照，不并入48token反侧；QFormer48的noise为47.1。Warmup只训21.2M tokenizer，后5.5M LoRA共同更改reader，冻结encoder不等整条音频接口行为不变。

VR的environment→profile→decision是metadata/提取属性+真实same/diff拼target，B4的latent-identity句由GT选语句，不是真实测得该例latent证据；reversal有助打断profile=identity捷径，但格式100%不能认证内部因果faithfulness。T4属性grounding72.7/summary63.6（majority52.9）；T5同模型SV96.79→SV-R97.12、supportive-diff78.53→80，而reversal总体97.15→96.81、same99.32→99.03。无多seed/CI，不把小差额定为稳健优势或由结构trace批准真实身份/授权。Generated verdict accuracy不是传统score-based EER/minDCF，语义profile与biometric验证接口不能互换。

265104utterance/530.8h；VoxCeleb1-O37611trial/40speaker、LibriTTS-R4837utterance/39speaker环境合成噪声，训练crop3–15s/eval中心15s。4A6000-48GB/bf16/FA2，126240/82840/220920步、bs42/32/24；总GPUh/服务latency-concurrency-SLO ND。全metadata提取/在线augment、frozenencoder前向、tokenizer/LoRA三阶段、pair推理/长trace/评价均费，不由小LM比一般audioLLM胜认定更低总费/隐私安全。无代码复现/真人部署。

拟2+1+2=5标准完成，**仅报告**，不把已准入候选改关闭。Actual Ch23 MAEB完整目标信息/encoder/真实读出分别验、后layer visibility/probe容量段，双audio主流/旁路压缩391–397与候选speaker绑定两段已读；这些不冒称旧稿有16+32算法。新matched-token证据支持本组pool/frame互补，metadata-derived VR schema也提供可核局部trace，但未给可迁移的身份置信/证据接受规则或可靠授权边界；已有关联/属性读出不替身份与真实消费者验收的具体选择不变，暂不追加一个拼接token/模板案例。重开需与真实声学/identity独立校准的新接口条件或改变当前读出选择的受控证据；不要求所有语言或真实认证部署才可保局部结果。待root必要域/Only独核。

## A123 — 14801另一人必要Source与具体已有覆盖提案

root R109首读后，作者实际[exact-v1 HTML](https://arxiv.org/html/2605.14801v1)完整题摘、§II-A/B/C/Eq1–5/Alg1及§III-A/B/C/T1–3与结论，足consumer特定误差模型/响应曲线及直接实用反侧；未展开旧SFCo-Nav稿或artifact。Current仅v1/ICRA workshop无具名纠错撤回。[既存DC](SUP_DC_2605.14801_20261019.json)唯一v1 May14 13:12:05Z、arxiv.content/findable/registered May15 02:20:49Z，schedule下界May15 00Z至上界完整北京May15。

Slow planner固定ordering/nested子集删理想语义，理想序列优先保指令对象；fast保持bbox尺寸/方向只平移中心，再Approach/Through投最近可达viewpoint。因此所谓statistical upperbound是该场景/技能/扰动的经验SR响应，不是严格/通用性能上界，graphmatching bucket也不识别唯一因果瓶颈。正文λ权edge、Alg1权node对换，λ.5实验恰同值，不把别的λ写唯一recipe。目标先验、无falsepositive及保持形状会改变可达结果；实际Through shortest-axis对shape扭曲敏感，不由平移IoU不敏感断言几何精度不重要。

约600instructions/8场景统计，约300实际ESAM；GPT4o slow/Habitat/每viewpoint40frame旋转。ESAM训练量与词表共同变化，AP25只是retention proxy、matched-boxIoU非全部错误law。T2理想retention .2→.8 SR41.0→44.3，实际.664→.756 SR都33.7；T3理想IoU.05→.8 SR35.9→36.0中途反退，实际.461→.567 SR24.1→23.5，不为孤立精度签单调收益。20类可接近200类仅此人口，任务core vocabulary不是普遍充分词表。感知训练、全视图/LLM/建图、技能执行与回归全费；hardware/precision/完整latency-concurrency-SLO ND，不采实时/净省费保证，未核实现或复现。

拟2+2+2=6标准完成，**已有覆盖 MULTIMODAL-EMBODIED-VLA Ch26**。Actual Ch26完整293–295已要求固定task/示教/评价比较encoder升级与连续/离散actionconsumer的闭环、重构与容量，而不是单测感知；90–96几何融合/池化/消费者细节与反侧各完整段，以及142接触proposal→标定/controller段均已读。现稿不冒本文误差模拟、SR数值或导航上界；但具体选择已是以真实consumer与误差身份联合验收、上游精度不自证行动收益。本文新分slowsemantic/fastgeometry的有限验证值得保报告，未给可跨consumer采用的新门槛/误差充分条件，不追加另一饱和曲线案例，不用已有主题否定贡献或逆删候选。重开需新误差条件/匹配预算反证改变该选择，或实际decoder/controller接受条件；保当前falsepositive/形状反侧，不追全站/所有任务。待root必要结果/NC独核。

## A124 — 14830另一人必要Source、actual owner与逐字PRE（未写）

root R109首读后，作者实际[exact-v1 PDF](https://arxiv.org/pdf/2605.14830v1)首屏完整题摘、pp7–17/§3.3–5.2.4、pp24–25/T1–5和pp35–37/B及C匹配；未展开D全judge模板/全部A图或其它行业论文。HTML404不称外部Source欠账，直接PDF已足必要域。Current officialabs v2无具名纠错撤回，只轻检不因编号回读全史。[既存DC](SUP_DC_2605.14830_20261019.json)唯一v1 May14 13:35:52Z、arxiv.content/findable/registered May15 02:21:31Z，公告下界May15 00Z至上界完整北京May15；2024现场实验日期不是本文首公开。

647workers employeeID随机为整套AI+supervision部署；680676chats含pretreatment、39432eligible/全时期与C匹配后11069treated+11069control不同人口。§3.4写345control/302treated，而T1 treat均值.53对应另一比例，本文保该分配口径差额不自修人数，不影响只采用有随机部署/人数总量这一有限层。17%主动rating、组间response rate相近不证明全部潜在满意度可忽略缺失，7天retrial只是resolution proxy。T2全chat lnDuration−.032、rating+.055未显著，T3eligible lnDuration−.168/rating−.412，T4ineligible−.018/+.091，不能logpoint当精确百分比或不显著当等效。

升级时机/type/worker effort不是随机处理，C按observed worker/customer/chat covariates各组1:1propensity匹配仍有post-treatment选择及未测难度/情绪/人的状态。T5 technical lnDuration+.191/rating−.007不显著，emotional+.408/retrial+.060/rating−.928，human initiated+.095/retrial−.032(p<.1)/rating−.524：这足说明“有人在环”不认证质量恢复，却不独立识别early优于late/手动触发本身或learned helplessness唯一机制。Humaninitiated没有技术/情绪分类，不能视同一种被随机提前的case。B实际LLM issue/clarify/SOP、sentiment与intentmonitor+人工可抢先takeover，threshold/版本/真实runtimeprecision/硬件总费/生产SLO ND，不能补造实施。全部模型、monitor、人工等待/监督、恢复与评价均费；未复现/未取得私有chat。

拟2+2+2=6，对human升级的恢复边界实际差额深入，唯一owner **AGENT-PLATFORM Ch84**。Actual Ch84完整SkillOrchestra能力/效用路由、逐步STEPGATE及其failure probability不等强模型可救回的两段、后skill依赖；Ch81 clarification/实际user状态与完整speculation边界、Ch83开篇交接均已读。现稿已有模型升级质量/费用与人工fallback，但没有把人工接收者的有限容量、等待后用户/任务状态继续变化纳入handoff恢复验收；不能以已有“人工”关键词作NC。只加有限现场反证支持的状态/恢复义务，不宣称本文发布新early-monitor算法，不在Ch81重复。拟Ch84完整STEPGATE费用/失败退路段后→Skill typed relation首段前一段＋本人compact注：

> 升级对象换成人，也不能把handoff本身记成质量已恢复：人接手的是已经演进的任务状态，还可能承受等待累积的用户挫折、并发负载和有限处理容量。因此平台设计应把升级原因、等待/交接时点、交给人的原始状态与接管后的真实结果分开保留，分别检验能力缺口和交互恶化，而不是只数“已转人工”。[一组现场部署证据](https://arxiv.org/pdf/2605.14830v1)显示，带人工监督的整套AI部署仍可降低适用任务的客户评分；不同升级类型的差额只是匹配后的关联，不能据此认证更早接管的因果收益、最优阈值或人的固定恢复能力。这里提出的是恢复验收的系统要求，不是论文已交付的监控算法：少数主动评分与重试proxy不替全部用户结果，部署速度也不抵销质量退步。模型/monitor、人工监控、等待和后续修复均计费；恢复支持或人的可用容量不足时，保留直接人工处理、较短自动化路径与明确停止/责任交接，不让升级按钮取得最终完成权。<!-- source-family:SF-2026-ARXIV-2605-14830 -->

本人注只保精确必要域/6分、随机整体部署vs匹配子群、评分缺失/分配比例与log口径限制、未披露监控算法及未核实现。等待root必要结果/实际owner/逐字PRE与窄位，未授权不写。

本轮README已实际同步R107/108的59新=32I+12Only+10NC+5D，加旧Charon60；184=72具体close+2窗外+59既成+50普通潜力+1外部14553。V3及限定working检查通过，不授DAY。A121/122尚待独核，A123/124不预扣；R109两首读另一人完成到此必要域，不第三source或补全全部附件。A122 matched48noise反侧已依root精准纠正并另标32token比较，不改变5分/Only提案。

## A125 — 两个既定潜力的有限贡献决定提案（未冻结、不评分）

未扩大来源。作者重读既定完整AB后，仅为决定“当前模型/系统有无直接新机制/条件”读取下面具名必要core，非全文/所有应用评价。以下不是因为Books已有主题、访问或审阅工作量关闭；若独核发现遗漏的独立增量仅重开具体事实。

- **14141拟贡献关闭**：实际[exactv1](https://arxiv.org/html/2605.14141v1)完整题摘、§4与§5.1–5.2及5.3 hidden-SAT机制开头。实际agent是hypothesis→analysis program→JSON hint→solver，beam按validation质量/optimality/runtime选、保diversity/refine/fork；这仍是样本统计→代码生成→验证选择的既有agent流程组合，未有新的执行/可靠性接受协议。Theory固定library/有correct solver、bounded runtime及预先prior，对应有限类一致性与runtime统一偏差；hint族已知、realizable且预给可分score/margin才可恢复，SAT需已有可识别salience与完整base solver fallback。这些诚实的class-relative条件有教学价值，但不是无约束LLM提示/代码搜索的新学习或安全保证，§5.2自己明确真实困难是未知hint/score/compiler，与理论恢复层不同。实例上的优化solver压缩计算域和性能有应用价值，当前没有超出现有样本估计、搜索/编译组合的新通用AI机制或直接改变当前训练/执行判断的条件，不以一般数学名/优化领域硬排。Currentv3改题为Distribution-Aware Programming及扩实验，无具名纠错/撤回，不倒填v3额外PACE/摊销公式，也不因编号遍历全史；日期不影响该贡献关闭，不展开所有证明/21域评测。

- **14594拟贡献关闭**：实际[exactv1](https://arxiv.org/html/2605.14594v1)§3.1.1–3.1.2的query/Perceiver与decoder/pooling、4.3对应encoder替换消融。核心是沿用Perceiver Resampler迭代读pointcloud与queries，再让N对齐固定template coarsevertices、复用template gridpool/unpool映射，经已知GNN/MLP输出固定连接顶点。Target索引与拓扑由template/逐vertex监督给出，不是发现了任务无关semantic anchors或新的query correspondence保证；输入不同拓扑由采样pointcloud接口统一是该asset重建选择。VecSet-Learn慢/FPS缺面与本设置CD/Fscore改善保留，不能只因学习queries或3D generative标签把已有resampler+template GNN的领域组合升级通用foundation表示机制。新的固定拓扑工业资产pipeline有用，但未新增可移植的token身份接受条件、输入结构学习规则或当前模型主线的新可验证反证。Current仅v1/technicalreport无具名纠错撤回；不因3D/人脸类型硬排、不扩全部UV/渲染/DiT/附图，日期不影响关闭不另追。

两项等待root一次独立贡献校准，不先计第73/74close，未因已保potential便无差别转Source债。此前新读七AB中的14948/14967/15182/15193/14876/14988/15044各有具名局部机制或受控反侧仍须按实际贡献判断；其中15044已按A122 Source/Only通过，不借这份列表自动深审其它。14988已实际§3.2–3.4决定域见attention-classifier→latent指导和dual-inversion标签泄露分工，保窄潜力而不从classifier-guidance成熟本身算新基础；14876已实际§3.1–3.2决定域见history→proxyreward接口，尚未看DSWM及对照，不冒完成。

## A126 — 14830实际窄写与14141准入纠正（非DAY）

14830按root R112授权真实保存Ch84完整STEPGATE费用/失败反侧之后→完整Skill typed relation之前唯一段与本人compact来源注；仅将直接前段‘与下一段的 skill 依赖关系’改‘与 skill 依赖关系’，其余原有效正文保持。作者实际读回新增、两完整相邻段与本人注，限定working diff-check通过；等待root非writer实际POST，不预支33I。

消费R110/R111：14333/15044标准5具体Only及14801标准6具体NC通过，当前62既成＝32I+14Only+11NC+5D。消费R113的14594具体贡献关闭第73。14141 A125关闭提案撤回：原v1摘要已含PACE100graphs，先前‘v3额外PACE’表述错误；固定library/诚实有限条件本身不是贡献关闭理由。root新实际E4配对zero/64samples、E6同构relabel质量/运行时分离与Decoy反侧提供新的准入事实，保窄5分标准潜力，拟采合成程序合法/质量不覆盖计算鲁棒性；待root必要首读packet，作者独立有限核/date/actual owner，不重审全部方法/21域。保留A125原误判与此纠正，不将其计第74close。

此刻184＝73close+2已确认窗外+62既成+46普通潜力+1外部14553；14830已写未POST仍计普通46之一。发现停止范围不变，未将宽库存或AB潜力转全附件队列。

## A127 — R114 actualPOST消费与63层报告同步（进行中）

14830 root R114实际完整新增/STEPGATE前段、Skill后段/本人注POST通过，第33I与Ch84窄位释放。当前63新增＝33I+14Only+11NC+5D；184＝73close+2outside+63既成+45普通潜力+1外部14553。README已同步四新增14333/15044/14801/14830的真实表/证据/处置及当前计数，旧Charon后合64家族；V3通过，非DAY，不称全部184独核或普通工作归零。限定working检查的SUP EOF空行告警已在本次附续修掉，不改并发index。

14063/14311/14358由root互斥必要Source首读；作者继续14988/14876，未重复展开三项。14141R114首读另一人必要核/date/actualowner仍普通，不因A125误判删除新反侧或把类相对限制本身当贡献关闭。

## A128 — 14988必要Source、date、actual owner与逐字PRE（未写）

作者实际[exactv1](https://arxiv.org/html/2605.14988v1)完整题摘及§3.1–3.6/4–5/T1–2、D1–2/H/J/T7必要域，到机制、关键控制与直接反侧足够即停；没有读全A/B/I图、动画/代码或所有版本。Current官方abs只有v1无具名纠错/撤回。HTML首屏August24 manuscript日期不冒论文公开日；唯一v1 May14 15:50:25Z，精确DOI [DC原件](SUP_DC_2605.14988_20261019.json) arxiv.content/findable/registered May15 02:25:26Z，公告下界May15 00Z至上界完整北京May15，不用created/提交作pub。

原约束：条件prompt/CFG不自动保证细粒度关系，生成器内attention又可能泄露目标词→实际新增：entity-token map→learned层/head/time聚合→冻结Qwen2.5-VL7B→trainable关系头；同一真实视频correct/incorrect关系prompt dual inversion均监督原视频label，再以关系CE梯度修正当前latent→改变应否以内部grounding读出作引导、如何限制文字捷径这一具体接口。Dual inversion原则沿引文并非本文发明，不把通用classifier-guidance/冻结模型原则算新基础。全generator/VLM冻结但聚合器/分类头需训练，不是整体training-free；去掉relation token并不消除剩余map的条件痕迹，也不因两prompt同label保证无泄露/真实因果。

§3.5多约束用户先给时间区间，§3.6AR每batch先给label，不能冒自动时序理解；只采用主体map读出/label捷径控制，不扩多主体/开放relation普遍泛化。T2 avg提升但Cog动作.663<.671、interaction.622<.638；Wan14动作.795<.806/interaction.742<.751，未有all-dim无损。J正文allsteps .575与T7 .475冲突（full.594、2steps.583、no-leakhandling.568）；T1Wan5B final.811与D后T4 .805亦冲突，不择有利数字/均值。消融支持局部早步窗口/泄漏处理值得检查，不证明allsteps必退一般定律或dual-inversion唯一因果。

单H100、混合精度未细分、832×480/16FPS、5s短片/30sRollingForcing；主guidance前8步，H说每5步抽取含clean终点但多t拼接的在线可用性/缓存细节未闭，不发布可复现多时刻读取recipe。D2 LR/WD/BATCH/EPOCHS/WARMUP仍占位，totalGPUh/end-to-endlatency/batch/concurrency/SLO未披露；100prompts随机人评未披露人数/每例票数/CI，定性迁移E无独立新label成功表，不采用强open-vocab保证。反演、训练、map驻留、冻结7BVLM及全部反传/采样/评估都计费，未运行artifact或复现。

评分2+1+2=5；实际内部读出/label捷径的具体差额深入。唯一owner MULTIMODAL-GENERATIVE-PARADIGMS Ch24：实际315完整外部classifier-cleanestimate/支持域/独立评价段，后progressive-innerstep完整段；1511–1520understanding监督/promptmask段与Ch23/25开篇交接已读。现稿有clean像素读出、训练expert目标mask以及引导器不能自证质量，未有“同一已知视频、反事实条件prompt产生内部表示但label不变”这一reader训练接口。只补此差额，不另复制§3.5/AR长视频分支。拟外部classifier完整段与其2507-00687独立marker后→progressive完整段前一段＋本人compact证据注：

> 分类器若改读生成器的内部attention，也不能把“看见主体token的响应”当成已经验证了主体关系：这些map仍由含关系词的prompt条件化，读出器可能只认出条件的文字痕迹。一条[受限视频引导分支](https://arxiv.org/html/2605.14988v1)从主体而非关系token的时空map训练聚合器与关系分类头，并把同一视频分别在正确、错误关系prompt下反演所得表示都配回原视频标签，尝试压低这种捷径；部署时再将分类loss反传到早期latent，生成器和理解backbone均不更新。它提供的是可错的引导方向，不是attention的真实因果grounding或关系已经成立的证书；早步/全步及去泄露控制只支持有限收益，正文与表数字冲突、未披露训练配置和部分动作/交互退步不支持无损或通用迁移。反演、聚合器/分类头训练、内部map保存、冻结VLM求值与反传均付费；读出支持、实体对应或独立输出质量不稳时，保留原条件采样、较弱引导和外部关系检查，不由引导器自己的高分批准最终视频。<!-- source-family:SF-2026-ARXIV-2605-14988 -->

本人注仅精确域/5分/采用与冲突/占位未核实现边界，不写运行授权长文。待root独立必要Source/actualowner/PRE与共享Ch24精确位协调，未授权不写。63既成不因该提案改变，14594已第73close。

## A129 — 14141另一人有限核、日期与具体已有覆盖提案

对A125已明确纠正的关闭误判，作者消费root R114首读packet后实际重核[exact-v1](https://arxiv.org/html/2605.14141v1)§6.1协议、E4/T13、E6/T15–16、D4/T8，原§4/5.1–2保持有效，不全附录/所有PACE表/21域实验。新准入不是有限类定理新颖性，而是LLM合成程序“合法/质量近饱和不覆盖计算鲁棒性”的受控反侧，2+1+2=5标准候选；小领域/成熟agent组件不抹这项有效负结果。

E4同pipeline ten paired synthesis seeds zero vs64publicsamples，quality近饱和仍9/12严格runtime改善，Decoy-complement却90.792→251.347ms反退；不把更多sample当单调收益。E6同一heldout graphs后验随机重编号，不用于selection，9分布feasibility变化0但quality均.945→.867/时间几何1.36×；quality损集中2目标，7目标均值近不变并不认证每例相同。Ring1.000→.772/9.65×，Core-fringe1.000不变/2.19×说明计算路径可脆弱而答案均值稳定；不由同构把任意目标quality/runtime不变设成自然定律。先声明expected relation与允许路径，再测资源目标，不让可行单指标代签发布。

协议主21targets、各solver/split十次评价与E4十二/E6九分布不同，quality arithmetic、runtime pertarget ratios/geomean分开；主表TSP质量可低于bestheuristic，不沿宣传统一冠全域。GPT5.2Thinking remote高effort/default温度/输出长度，463successfulcalls/16.11Mtokens（8.05Mreasoning为completion子集），dualEPYC9554/128physical/256logical/1.1TiBCPU；73.4h synthesis+417.3h baseline合计per-target记录非calendar/单请求SLO，.6h额外local分析，API/候选构建/验证/再合成全费，不将deployment快比当amortized全链净利。Library/realizable/boundedruntime/预给score间隔条件只限定理论适用，不认证开放LLM程序搜索自动正确；未核artifact/复现。

Currentabs v3改题/扩数字无具名撤回纠错，不倒填v3或把v1已有PACE误说后到。既存[DC原件](SUP_DC_2605.14141_20261019.json)唯一v1 May13 21:47:55Z在EDT20Z cut之后，最早May15 00Z；arxiv.content/findable/registered May15 02:05:04Z最晚上界完整北京May15。实际首公开日组合有效；不是提交或created作pub。

拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM Ch66**：作者实际完整读项目级规格构建段679（test pass不认证性能/内存/生产正确性）、1610–1620reliability profile（平均outcome与perturbationrobustness分账）、3445完整关系oracle段及直接前能力/witness、后Artifact/Process标题交接。3445已要求先核输入变换是否保任务语义/按声明目标，再配对source/followup并保terminal/受控重复；679补答案通过不签资源目标。两条合起来已承载此处采用要求——语义保持变换下分别验合法/质量/计算成本，不能用训练原输入或单指标pass替鲁棒发布。这里新增的是合成solver的有价值配对测量与跨分布反侧，未增加新的oracle权限、输入等价判定或runtime统计机制；不冒现稿已有本文9graphs/2.19×、E4样本编译算法。保新候选/结果，不以NC反删分母，不为新论文名追加应用案例。重开若提出不同于现关系oracle的可验证接受条件/资源关系，或具体反证改变现有一般要求，仅定点补其实际受影响域。待root必要结果与actual覆盖独核，未计第12NC。

## A130 — 14876必要Source、date与具体仅报告提案

作者实际[exactv1](https://arxiv.org/html/2605.14876v1)完整AB及§3.1–3.4/4.1–4.4/T1–4、A1.1–1.2必要局部论证、A3/5/T6/A6/A8/T8/A11与A9区间定义首屏；A1.3只看time-local/slowly-varying假设开头，不称完整trajectory证明/全A7probe或其它模态/所有附图已读。Currentabs v2无具名纠错撤回，v2提交May15不是公开日，不因编号扩比较。[既存DC](SUP_DC_2605.14876_20261019.json)唯一v1 May14 14:22:25Z、arxiv.content/findable/registered May15 02:22:39Z，公告下界May15 00Z至上界完整北京May15，current标题/作者身份对应，后到记录不回填v1。

原约束是长interleaved历史不匹配短instruction reward、少步蒸馏与新closed-loop alignment未必兼容→增量：offlineVLM将历史压为scene/edit proxy prompts+reference imageindices，用global/edit reward各半（t0仅global）配DiffusionNFT；部署controller看canvas+全trace决定generate/terminate；同base的distill delta与SFT+RL delta直接相加复用4step checkpoint→具体重新考虑reward消费者的输入投影、以及是否另付re-distill成本。不是把self-reflection/weight addition成熟原则本身算新认知基础；保这一局部新提案与比较，评分2+1+2=5标准。

A3约10^5candidate→20861trajectories，Gemini2.5Pro controller/Seedream4生成、Gemini+Seed1.8双judge一致+blindA/B筛，任一步失败整轨丢；这产生选择后demonstrations，不证明每步真实正确/causal credit。A5 simpleRL仅读上一round reasoning/latestimage，PPRL改全文history→proxy，提升可能包括信息权限/teacher压缩/目标形式，不只‘稳定credit’；并无独立人类proxy忠实率。GenEval VLM-only.86→diffusionSFT.85→simpleRL.84→PPRL.87，Wise .65→.62→.64→.74，SFT本身并不单调；rewrite Wise.48→.64解释多数早期增益，但GenEval.81→.78反退。Full GenEval singleobject.99<相关SFT/simpleRL1.00，不采all-dim无损。MainT4PanelB完整标DSWM的overall.71与T2/A5 full.74口径不一致，保差额不强行拼统一操作点。

DSWM公式仅checkpoint arithmetic，不从小globalFrobenius差2.79%/2.30%/RL.0075%认证所有输入Taylor remainder小；误差还需Hessian/层/状态界。A1.2 distillation score近似nearest manifold normal需要小噪声/tube等，posterior mean不一般等nearest projection；KL/no-rewardhacking不能自行推出parameter-to-output alignment纯tangent、蒸馏纯normal或实际两增量全状态正交。Output空间近似也不等parameter空间无干扰，不采其几何/理论兼容保证。T4有限FLUX4B merge GenEval.87>RLonly.83/distillonly.81可作为经验兼容，不证明其他base/目标普遍可直接和或保全部对齐。

A6 Qwen3-VL8B/controller与FLUXKlein4B/9B，全SFT20861/3epochs，bf16；diffusionSFT1024²，RL LoRA128/α256、512²/8rolloutsteps/group16、8H20。Proxy teacher/双judge数据制备、fullSFT/RL/LoRA/merge/全evaluation费用未合计GPUh。A8部署两H20一diffusion一VLM、base28CFG4 vsDSWM4无CFG，最多8loops；按迭代数分桶平均E2E如2loop287→25.5s的两组case人口不同（GenEval368vs376），不是同sample纯merge causal11×/普遍SLO。NFE减少不是同质量总请求保证。A9只finalmodel nominalCI、不提供pairedbaseline gain或跨seed确定性；不额外重算自造实验。未核代码/复现。

具体Books拟**仅报告**，不以名称缺失认缺口。作者已实际Ch29 response/condition/feedback-converter316与目标/标签权限段、Ch30完整artifact/merge identity与distillation边界754–784、Ch24少步训练/质量及guided proxy315/1511–1520和学习/生成交接。现有长期要求是派生条件/score须保持权限、独立质量与全部费用，合并须同base/部署与行为回归；本文新数据引擎/PPRL/DSWM提供局部可试配方和受控收益，尚未给可移植的proxy接受条件、兼容性判定或新的有限费用/保真边界。正常无担保提案不因此关闭候选，但不能用未证normal/tangent解释抬为长期可靠性规则；也不为把现有原则换成图片例子追加Books。重开需独立history→proxy fidelity/目标权限控制、matched预算的merge质量/兼容条件或新失效边界实际修正当前设计判断。待root必要Source/具体Only复核，不计第15Only。

## A131 — 14988实际保存；14948必要Source与中心争议提案

14988依root R118逐字A128保存Ch24318唯一段与本人compact末注，位置在完整外部classifier315/独立2507-00687marker之后→完整progressive段前。作者实际读回完整两侧/新增/本人注，限定working diff-check通过；待非writer实际POST，不预支34I，保同文件May19各并发段不动。

**14948 ACE-LoRA**：重新完整读既定Q2题摘后，实际[exactv1](https://arxiv.org/html/2605.14948v1)§2.1–2.2/Eq1–5、§3评价protocol、§4.1–4.3/T1–5、C1/D/T6–7必要域；不看所有B示例/像素/代码。Current官方abs仅v1无具名纠错撤回。[DC原件](SUP_DC_2605.14948_20261019.json)唯一v1 May14 15:20:27Z、arxiv.content/findable/registered May15 02:24:27Z，公告下界May15 00Z至上界完整北京May15。不同论文身份，不因类似Octopus争议就把本篇改成重复事件。

具体增量是历史LoRA和的top-r SVD保持历史状态rank，再在当前task data对历史B求loss梯度作interference vector，只约束新B而A可适配、两阶段先自由后约束；保候选2+1+2=5，不以成熟SVD或同主题直接排。重要中心冲突在Eq5：写的是有符号Frobenius内积 `<g_historical-on-current, B_new>`，不是绝对值/平方/零约束，却反复称严格正交。即便每batch固定g、加正λ最小化，线性项梯度为λg，只使目标沿−g偏，不强制innerproduct=0；若另有二次范数项，简化最小点正是非零反向g，更不能由该形式导出保护旧任务。若实际将其最大化也只偏+g而非正交；本文未给完整总loss权重/投影执行定义，不自行补改公式。当前数据上历史梯度不等旧task Hessian敏感全空间，旧参数在旧task最优也不推出当前task梯度只含冲突。B-only约束又依赖与A/历史SVD坐标的选择，不天然是完整BA更新或行为不变条件。

Top-r SVD最优的是矩阵近似，不是历史能力无损；B/A重构与rank省状态的价值保留，但不能由矩阵能量/近cosine宣布新task无干扰。T2 AOD Last8.8685>parameterorth8.3956，Imm Focus8.3588<8.5877、Tryon9.4855<9.5362仍反退；T5 SVD比random/summation好但各BWT仍负、SVD−.1702，不证严格保旧。T1Last低MTFT，部分task不及rehearsal；三order均值8.5347–8.8685非orderinvariance。Qwen3.5plus judge/domainpriors、IF/PN1–5相加，D只90examples/每task15，absolute差≤1算match，overall.7048、relative.8295不是真实真值/每行为安全。MTFT/zero empirical参照不是数学上下界。

Flux2Klein9B、rank48/各task10epochs/lr1e−4，四H20-96GB/1TB RAM、每task.5–2h/全benchmark约8h；precision、每phase步数/约束系数/完整judge与SVD/历史梯度预算ND。模型/基座、历史压缩/SVD、额外历史前反向、两阶段和全部旧任务回归均费；小n无多seedCI不扩全task排序保证，未核实现或复现。

拟**中心正交/历史保护争议暂缓**，不反删候选、不改低分或把普通Source欠账称受阻。实际Ch30完整B softpenalty/因子缩放117、固定rank截断221与最终optimizerstep264等段，以及Ch29/30交接已读；这些要求参数方向/近似不自签行为保持，不能替本文signed objective补成硬正交。当前不进Books、不采用严格正交/无损历史/规模独立全费；经验结果保报告。重开只需官方精确总loss或实现对应的正交执行/停止梯度/phase定义及同预算保留对照，先定点Eq2/5及历史SVD，无需所有附件重读。待root必要Source/具体争议处置独核，未计第6D。

## A132 — 14967必要Source、date、actual owner与逐字PRE（未写）

作者重新完整读Q2原题摘后，实际[exactv1](https://arxiv.org/html/2605.14967v1)§2/Eq2.1–2.5、§3.1–3.2/T1/F2–4、§4.1–4.2/Lemma4.1–4.2条件及A3/T3–4直接保留反侧；A3后B开头只查entropy解释对象，不展开全部C证明/D responses/其它论文。Current官方abs仅v1无纠错撤回。[DC原件](SUP_DC_2605.14967_20261019.json)唯一v1 May14 15:32:37Z、arxiv.content/findable/registered May15 02:24:56Z，公告下界May15 00Z至上界完整北京May15。

原约束：uniformCE可强化不典型demonstrations，单调高q加权又压新行为/多样性→实际增量：q为currentstudent reference-token概率，w=q[logit(pbar)−logit(q)]_+整权重stopgrad，再按response原长度平均乘CE；同时减极低/极高q，不等现有高q阈值mask→改变学习新格式与精炼已可预测行为时的监督顺序。仅给2+1+2=5，不把通用KL/proximal或‘optimal’标签计新基础；具体监督选择缺口深入。

§4是一次理想distribution-space proximal update而非optimizer/有限参数动力学，oracle依赖真正expert样本概率p；Lemma4.2有q≤d≤pbar/e²、pbar≤.98等条件，不能直接覆盖token实际中置信区间或实际未知expert。§2 clip负权是实用heuristic，理论unclipped族/β全局重缩不认证clipped多步训练同实际KL预算或保旧。pbar实际由学生T.7下correctresponses平均q估计，再扫.9/.95、default.93；不是有权取得teacher/expert分布或无调参常数。公式中的onpolicy effective reward Ω不等实际CE multiplier qΩ，不沿1/q叙述声称普通softmaxCE token梯度必无界/所有罕见token有错。

T1三seed平均、同lr/steps/epoch支持局部质量比较，不等更新范数/实际KL匹配或相同全校准费用；数学较好但代码可低DFT：Qwen7BHumanEval68.9<69.5/MultiPLE34.1<35.2，Llama pass8 64.6<plainSFT66.3/base66.0。F3 OpenR1低格式时纯SFT优Info，AIMEpass8 43.3>26.7；SFT1epoch+Info1epoch可50.0但AMCpass8 76.4<两epochSFT80.7，不签两阶段必支配。A3 sweeppareto不保证每matchedcheckpoint，Science lr1e−5/1epoch InfoPrior69.4<SFT70.5/DFT69.7、新task66.9<SFT67.1；未把少数好checkpoint当全能力保证。由此采用heuristic权重形状及可回普通CE的任务边界，不依赖‘anyKLbudget严格最优’背书；形式lemma本身不判错。

Qwen2.5Math1.5/7B、Llama3.1-8B：Numina100k/1epoch、UltraFeedback12k LoRA32/α64/1epoch，OpenR170k长度≤8192/2epochs、evalmax16192；retainsweep用Qwen7B-Instruct2.7k/4k与1/2epochs。GPU/hardware、precision/batch/总GPUh/latency/concurrency/SLO未披露，不作one-line=免费。Correctgeneration校准、概率/gather/weight、全前反向、hyperparam/阶段搜索与旧能力回归均费。未核artifact/复现。

Actual唯一owner TRAIN-SFT Ch29完整187IG段、189/191概率阈值与长尾/分母反侧、193连续回归loss权重完整段均读；Ch28/30开篇/LoRA交接已读。现概率门只留高q、ConservativeSFT是连续动作loss指数权重，不承载token双端下调与低格式应先完整CE再切权重的局部新反侧。只加这一选择，不复制理想KL定理或全部榜单；拟概率门191完整反侧后→连续动作193首段前单段＋本人来源注：

> 概率门也可以不只保留高置信位置，而把更新集中在中间区域：令q为当前学生在真实prefix下给reference token的概率，以校准常数p̄构造detached权重q[logit(p̄)−logit(q)]₊再乘原CE，其中logit(u)=log(u/(1−u))、[·]₊表示负值截为零。极低q的权重仍趋零，接近或超过p̄的位置也不再强化；它改的是监督分配，完整历史和前向仍保留，不是识别了客观语义信息。[InfoSFT的有限对照](https://arxiv.org/html/2605.14967v1)支持这一中置信分支，但p̄用学生正确生成的置信度近似，不能冒真实expert概率；理想单次分布空间KL分析也不认证裁剪后的多步参数训练有固定KL预算或必保旧能力。低概率恰好承载新格式时，直接压低它反而学不进来，普通SFT先引入格式、随后再改权重只是一个有任务依赖的替代顺序；部分代码/多样性切片仍退步，不用平均收益替代新旧能力验收。原位置分母、总体权重尺度、学习率和阶段长度须共同比较，校准生成、完整训练与所有回归都付费；罕见标签、格式学习或保留能力不合格时，回到可信完整CE、较温和权重或已验replay，不由一行loss改动签发免费稳定性。<!-- source-family:SF-2026-ARXIV-2605-14967 -->

本人注只精确域/5分、实用clip与理想一步分开、校准/低格式/代码反侧及未核实现，不含持锁行政长文。待root必要Source/date/actualowner与逐字PRE窄位，未授权不写。R119 14988actualPOST消费，第34I/Ch24释放；目前65既成＝34I+14Only+12NC+5D，73close+2outside+65+43ordinary+1external=184，本段未预扣新两项。

## A133 — 14358另一人定点核、date与经验oracle中心争议提案

消费root R117必要Source首读后，作者实际[exact-v1](https://arxiv.org/html/2605.14358v1)§2.1–2.4/Eq1–6/Alg1、§3.1有限终止/充分性声明、§4setup/T1–2与E1/T9、A的compute/metric/生成及sufficiency/budget定义，到指定冲突足够即停；未重读完整B证明/F-G-H或所有几何probe与转移实验。Current官方abs仅v1无具名更正/撤回；[既存DC](SUP_DC_2605.14358_20261019.json)唯一v1 May14 04:35:45Z、arxiv.content/findable/registered May15 02:10:10Z，下界May15 00Z至上界完整北京May15，日期门有效。

原准入仍有效：书面CoT未必全必要，greedy删除只保预测充分性且可测subset/geometry差额；2+1+2=5，不把形式存在性/贪心终止等成熟有限集事实算新长期基础。正文明确行为而非隐藏真实因果，minimum-cardinality与greedy一阶局部不可删也已分开，不因不全局最小指责其定理错。

但实际操作身份冲突未解：§2.2 answer-sufficient等于同一model的retained-subset argmax与fulltrace argmax相同，Alg1只删仍满足该predicate的位置；§4.2/A matchedbudget不够时保终态、不强制破sufficiency。A retention公式亦以同一fulltrace prediction比较，没有另定义independent随机复采/不同生成answer/改变oracle。故依声明的同一确定predicate，最终每个保留子集应仍answer-sufficient；T1终态Retention .86、T9 answer-preserving .88却小于1。低温‘生成原trace’本身不解释为何提取oracle与最终验收可不同；若确有独立复采/新seed/原先采样answer区别，须显式记身份，不能作者替原文补造。更严格distributionpredicate并非必保argmax（小margin可翻），不用于消解明确answer-preserving行的冲突。形式Theorem3.2逻辑有效，只是实际经验实现/测量是否同该contract未闭。

保留原结果：T1约46%removable/.86retention、T9 .54/.46/.88与更严格KL行，不能当已认证压缩/因果支持率；几何probe基于这种被选择core，内部正确性/真实性与globalminimum另验。8×A10080GB、TP/batchedinference、openweight sweep数天/API一两天量级，precision/精确batch/totalcalls/GPUh和完整延迟ND；greedy至多O(T²)checks及原trace生成/全部candidate/likelihood/hiddenstate/probe/人评均费，relativechecks不签净推理加速。未核实现/复现。

拟**经验oracle/retention中心争议暂缓**，不是访问失败、普通Source欠账或重定义成范围关闭。实际Ch5完整固定continuation与重新rollout347段、最小充分/路径必要365及416greedy非唯一global段已读，现稿不能替本文指定同oracle操作身份，故不新增正面Books。重开只需官方说明extraction predicate与retention的随机状态/answer/parser/生成协议及原始配对结果或对应更正；允许明确独立重采的保留率但不得继承同predicate充分性保证。只重该经验身份与依赖几何/压缩解释，不重所有proof/所有models。待root必要结果与具体争议独核，不预计第6/7D。

## A134 — 14063跨日资格的有限恢复与外部保留提案

R115 Source首读有效；作者已实际精确v1§3/Eq1–5/Prop1、Alg1与P指定confidentlywrong反侧，确认共同gate只覆盖objective显式source项、初始化/ASR reset仍依赖source，P只permute供agreement/divergence的logits，不把entropy不变说source完全替换，也不把fallback可定义当不collapse保证。没有为了日期回读全部评价/所有附录。潜在标准5命题保留，但**日期未确认，不列当窗候选/不评分采纳/不写Books**。

实际[DC原件](SUP_DC_2605.14063_20261019.json)与[官方currentabs](https://arxiv.org/abs/2605.14063)明确唯一v1 **May13 19:38:08Z**（EDT当天20Z cut以前），故日程只给最早可能May14 00Z；arxiv.content/findable/**registered May15 02:03:15Z**给最晚上界。整个区间跨北京May14/15，不能以registered或Updated v1 May15 00:08:30Z截取May15，不能假定没有延期，也不能把通常日程当已公开。Currentv2 May19只是后修编号，未见具名撤回/更正，未扩全史。

精确恢复仅沿官方入口：先旧YYMM路径/list/cs.LG/2605返回404，未把路径错当外部消失；从currentabs实际‘2026-05’链接进入正确[官方月目录](https://arxiv.org/list/cs.LG/2026-05)，它声明6572项/当前首50且只有month，没有目标day证据；未将月目录转新发现/分页队列或称目标没出现。再从同页实际Advanced search进入[官方搜索说明](https://arxiv.org/search/advanced)，明确announcement date只支持year/month粒度、原提交可日粒度；故不使用伪day filter或提交日期查漏来证明公告日。未扫后续6572条、未新建宽inventory。精确v1 C Code段只说匿名实现将在acceptance后发布、无具名原始repo/历史event直链，不捏造代码首公开链。DataCite Updated与当前HTML/PDF可得不具历史首次公开权限，不为凑当窗重新命名字段。

拟与14553不同的**跨日公开资格外部保留项**：缺同一v1的直接官方日公告/有日期的原始全文公开链，当前有限公开字段不能消除跨日；不支持本日正面候选、Books、日期覆盖或无遗漏。重开只需官方May15日公告含精确ID，或有时间/日期权限的同稿公开记录给更早上界以正确窗外关闭；不要求全球first精确秒、也不搬写May14或另一Daily。Source必要机制有效层保留，材料到达只恢复日期及依赖采用，不重R115全文。待root实际日期/有限恢复独核，未先把普通减为0或转已确认outside3。

## A135 — 14311另一人必要Source与具体仅报告提案

按root R116首读packet，作者实际有限核[exactv1](https://arxiv.org/html/2605.14311v1)§3/4、§5.1–5.2/§6.1–6.3、T2–7及C1–3/D1/D4直接对照；未展开E全部案例、F/G所有标注与其它论文。Currentabs v2未见具名纠错撤回，不倒填后修；[DC原件](SUP_DC_2605.14311_20261019.json)唯一v1 May14 03:23:44Z、arxiv.content/findable/registered May15 02:09:04Z，下界May15 00Z至上界完整北京May15。

原判断：GUI候选的二元训练准确不等密集候选上的有效排序→共享Qwen2.5VL双encoder余弦/InfoNCE与GT/layout后policy-hardnegative两阶段，D1同stage1数据/2–16negative密度对照显示BCE SR54.4→50.8/margin+.24→−.30，Info65.6→66.4/+.78→+.96→有理由比较具体negative人口与ranking目标，而不是预设二元loss天然不能排名。2+1+2=5标准，关键对照/负控制必要域已足，不因局部/GUI小模型排除。

四级标签只用于BBBench评价而非训练，NDCG指数gain与相邻级PPA测不同对象；T2 sub–dis仅51.20/52.67近chance，不签恢复完整语义拓扑或严格最优。BCE的负梯度sigmoid(s−)并非所有负例一样，binary scalar也能排序；D4 onehot ListNet可等价InfoNCE，不证明所有ordinal/pairwise目标严格较弱。T6 online 30.2 vs29.4只有限人口且无误差条，不由headline判通用优越；跨论文rollout人数/候选policy与预算不同，T3/4不能合并同预算因果。两阶段去项改变训练量，T7不隔离“必要且充分”的唯一机制。C2所谓hardnegative实际核GT nextaction身份，不能称每条都独立执行失败或所有替代valid动作已排除；C1 hardnegative64与正文平均58/25口径未闭，不补成复现实方。§4.2已经除τ、§4.3又写exp(s/τ)的约定未澄清，不发布温度recipe。

3/7B、LoRA16/α64、AdamW5e−5/bf16、8GPU每卡batch1、stage1一epoch/stage2两epoch；GPU型号/GPUh/墙钟/SLO/online重复与CI Not Disclosed。训练约191k/190k，政策N64制备、每候选带circle渲染/双encoder、layout parsing、完整训练/全部online proposals/evaluation均付费，不把只交一个action当单候选费用。未核artifact或复现。

拟**仅报告**保具体密度反侧/新评价人口，不反删候选或称原稿已有BBCritic。Actual Ch31 99–103完整BT差值/比较support与人口改变拟合重点，111–115文本解释/score读出分责、129–135 ordinal监督身份，以及Ch79 345–359完整critic预算/状态目标semanticproxy与真实outcome交接均已读；Ch30/32与78/80相邻交接有效层复用。当前长期选择已明确依部署比较人口和可信outcome选择读出，不从二元标签或连续距离授语义真值。本文新增是此GUI采样/余弦方案及局部密度曲线，尚未形成跨candidate标签构造可迁移的BCE失效条件，亦未独立验证所有hardnegative/新语义等级，不为每份局部critic配方追加案例；这是具体Only而非主题相似即NC。重开需独立有效action标签/相同候选与预算下隔离目标、采样/score读出的可迁移有效性条件，或当前BT/semanticproxy选择被受控反证推翻。待root必要处置独核，不预扣普通或计Only16。

## A136 — R121/123/124既成消费与69新增进行态同步

14948中心正交/历史保护争议已R121独核，14967按A132指定Ch29单段/本人注真实保存并self-read，root R124非writer完整新段/直接两侧与本人注POST通过，计第35I且窄位释放；14063 R123有限跨日资格外部保留独核消费，不冒已确认窗外。README已在原六节同步69新＝35I+15Only+12NC+7D、合原Charon70家族及两日期资格外部项。184＝73贡献关闭+2具名早稿窗外+69既成+38普通潜力+2外部资格，不授DAY、未冻结漏斗；A135未预扣。R117错误fragment已修正到实际标题，未改旧Charon原行/原日期/评分/原小时窗与连续旧§4。14350/14364及15182/15193只消费root首读packet后另一人有限核，不全篇重复；13866仅先核跨日资格，不扩hiring附件。

## A137 — 14475具名贡献关闭提案与两项保窄潜力

重新完整读既定B5/B6/Q2题摘，只对准入含糊的新机制核exactv1决定域，不把潜力批量转Source。**14475 GeoVista拟贡献关闭**：实际§3.1–3.3/§4.4–4.5表3，Global/Region/Object checklist、已有相对坐标仿射到0–1000、顺序解码的多ROI plan与结构化evidence日志、teacher轨迹SFT后GRPO，加pending/completed状态与格式/IoU/count reward。坐标回全图后去重是已有crop/provenance做法，未给新的冲突合并/证据独立性/对象identity接受算法；‘parallel’正文明确仍同一trace顺序解码。表3换整个trajectory库、§4.5加整套GRPO/更长工具过程，未出现足以修正现有active-perception选择的独立新失败条件或组件对照；这不是因遥感/视觉或小收益排除，而是已有工具规划/状态记录/奖励组合在UHR任务的实现。保表3SFT后XLRS低base、RL非单调的原结果，不把这些常见局部现象包装通用新边界；日期不影响贡献关闭，不追全部附录/数据。若有新增跨ROI对象合并/核验规则，或同数据预算独立改变单路径与分支选择的受控反证再定点重开。Current为June21 v2，无具名纠错撤回；待root准入校准，不提前扣账。

14201 MAPLE实际只核§3及§5.2/T2–3决定域：多任务rollout与reward本身已知，但固定ego、多reactive planner与被动motion head分工及T3 ego-only→reactive/多planner对照仍有具体消费者选择信号，保窄潜力，不要求真实驾驶普遍保证才准入；未宣Source/date完成。14750 EVA实际只核IV-A–C决定域：沿MEMIT的更新不另算基础，text harm key引导visual top-token key选择、分列key consumers与过多visual keys导致over-refusal仍可能改变多模态编辑范围，保窄潜力；正文明确扩自DELMAN，后续须核早稿/此次视觉增量资格，不把‘首个’当新核心。未全读V评测或旧DELMAN，不先评分/Books。

## A138 — 13866有限日期资格提案与计数去重纠错

实际同ID[DC原件](SUP_DC_2605.13866_20261019.json)唯一v1 May2 16:08:07Z（周六）、arxiv.content/findable/registered May15 01:58:37Z；按当期周末公告安排最早May5 00Z，区间显然跨多北京日，不能取registered/Updated May15作实际公开日。当前abs v2 July14无具名撤回纠错，后修29模型/数据组成与表示解释不倒填原v1的27模型行为证据。具名标题＋作者两个搜索仅用于恢复，实际[Thaler作者页](https://www.michaelthaler.com/research/)当前给Working Paper July2026并链接currentarxiv，[Wang作者页](https://zewang.uk/publications/)只给May2026/月及同currentarxiv，没有v1有权限的日公开上界；搜索日期/ResearchGate月份/SciRate目标日投影不取代原件。已核官方高级检索公告只月粒度的共同限制，不再次扫月inventory。未进入hiring方法/附件或追全球first秒。

拟第3**跨日公开资格外部保留**：不列May15候选、不评分、不写Books，不当已确认窗外；保R57原v1题摘潜力及本次身份。重开只需同一v1官方日公告/有日期全文公开链给足落日或更早上界，不扩社会治理研究。待root有限日期核，不先把该项改完成。

真实名册纠错：183 arXiv原题摘各ID唯一＋UAM共184。A61/R55已经关闭14634，A107/R92又把它与14742两项全加，造成close重复1；不重开14634有效判断。R129接受14311第16Only后应为72close＋2outside＋70既成＋38ordinary＋2external＝184（A137/A138仍待核）。此前73close/38ordinary快照的单项差保留轨迹，以实际身份为准，不凑数删潜力。README69新增层已保存，下一同步R12970；未授DAY。

## A139 — 14350另一人必要核、date与Ch27逐字PRE

R125首读有效，作者实际核exactv1 §3–4/Alg1/Th4.2、§5必要协议、F1/F2与G配置差额；F1同Gridworld50seed的uniform+reweight反侧与F2缺样本zero-return/大步震荡均确认。lowregret/有界gap只导平均界，reference最大已观察return可能低平台；不执行Alg1行13方向冲突文字。Current仅v1无具名纠错撤回；[DC](SUP_DC_2605.14350_20261019.json)唯一v1 May14 04:22:24Z→registered May15 02:09:59Z，arxiv.content/findable，完整可能区间北京May15。5分，采样/估计差额具体gap深入；完整模型/多环境预算与硬件/precision/总GPUh ND按R125保留，未复现。

Actual TRAIN-DATA Ch27 1217完整difficulty/selector段→1219 checkpoint-coupled重权段、后selector/optimizer分责完整域与Ch26/28交接已读。现稿有adaptive sampling/reweight入口，但未明确同一目标期待等价不能消除有限新交互/估计误差；不是缺论文名而是两个控制对象未分清。拟在1217整段后、1219前单段＋本人compact来源注，逐字如下：

> 在线选择还须把“给某任务的梯度多大权重”与“为它取得多少新交互”分开：在期望目标上可等价的重加权，不能给有限batch补出未采到的轨迹。一条受限多任务RL分支以参考return减当前return的gap提出任务采样概率，用KL正则、逐步更新和最小概率限制过度集中；参考可由已观察最大return估计，因此低平台也可能低估目标。[同Gridworld的采样/重权对照](https://arxiv.org/html/2605.14350v1#S4)中，均匀采样后加权甚至弱于普通均匀，支持检查有限数据的梯度估计，而不是只比较期望loss。最小概率不保证本batch实际覆盖；无样本便把return记零，会造成假大gap和采样震荡。环境交互、return估计、训练、调参与回归均付费，样本效率不等墙钟省费；低regret条件的迭代平均界也不授普通PPO最终checkpoint保证。估计、reference或总预算不稳时，保留均匀/分层采样和冻结mixture，不让一次缺样本替任务难度签字。<!-- source-family:SF-2026-ARXIV-2605-14350 -->

## A140 — 14364另一人必要核、date与Ch5逐字PRE

R126首读有效，作者实际核exactv1 §2–3假设/定理陈述、§4.1–4.2、§5/6及C1/3/4、D、E2/E4必要定义/配置；不展开全部A证明。Self-consistency只gate初始化，旧encoder/transition frozen但T/gate/active表示变化、残差新坐标和保library实际确认；硬case gate.5，linear实例/长链未闭、LLM只是单层冻结activation/PCA/probe与外部proxy。C3相对softmax初值与正文正logit不直接相等，C4新gate记号不补成唯一recipe。Currentv3无具名纠错撤回，不倒填后修；[DC](SUP_DC_2605.14364_20261019.json)唯一v1May14 04:46:54Z→registered May15 02:10:18Z，arxiv.content/findable，完整北京May15。5分/模块复用具体接口gap深入，原所有激活/PCA/search/旧回归费用及硬件/precision ND保留。

Actual WORLDVIEW-REPRESENTATION Ch5 102/104任务embedding与backbone分步、96–100组合接口及106长度可学性交接完整段已读，Ch4/6开篇交接已读。现稿区分冻结接口与表示可读，但没有旧模块字典→新正交坐标→可变对齐/gate的独立复用分支；拟104完整task接口反侧后→106‘组合性还要区分可表达…’前一段＋本人compact注，不采general→specific真实语义或无遗忘保证。逐字如下：

> 顺序数据上的复用对象还可从一条task vector扩成模块字典：先用旧坐标与旧encoder解释新观测，以时间自相关和旧变量对其它残差的泄漏提出复用gate的初值，再从观测重建残差扩出与旧坐标正交的新方向；随后学习旧表示的近identity对齐、新模块和稀疏gate，而保留旧encoder/transition块。这里保存的是旧产物，不是当前活跃表示：gate可关闭旧模块，对齐与下游读出也会变。[MoRe的受限序列对照](https://arxiv.org/html/2605.14364v1#S4)将恢复、保旧与模块分配分别测量，重叠因素下gate准确率仍可仅.5；时间延迟单向依赖、可逆mixing与充分变化等条件也不是自然语言的既定本体。真实LLM部分只对冻结单层activation做PCA和外部表示学习/线性probe，不是持续微调LLM或验证其实际语义模块。激活提取、坐标扩张、gate/对齐训练与旧任务回归均付费，线性实例和短适配链不授长期无遗忘；结构或行为不稳定时，保留原表示、原读出与独立任务验收，不让字典仍在替活跃能力签证。<!-- source-family:SF-2026-ARXIV-2605-14364 -->

## A141 — 15193另一人必要核与Ch24具体已有覆盖提案

复用R128首读，作者实际核exactv1 §3.3–3.4、T2–3、C3 decoder-flow交叉、B1/B3必要域。Spherical token support/投影Gaussian prior、冻结encoder后5epoch decoder/discriminator、slerp target/tangent prediction与Exp采样共同变；T2 shell27.26不胜vanilla26.35，spherical-linear22.85→slerp20.55不能全归path；T3 FLUX rFID1.072劣于FT.486、REPA .824劣.759，C3交叉decode112.17/43.17支持consumer耦合。B1近反点路线终点−x0不是一般near-antipodal x1，不发布该fallback recipe。B2×H200/6.5h、XL4×/16.8h；bf16/paramEMAfp32、decoder5epoch和预处理/search/FID额外，不将同epoch当同总费。5分标准完成，未复现/全证明。Current仅v1无具名纠错撤回；[DC](SUP_DC_2605.15193_20261019.json)唯一v1May14 17:59:37Z、arxiv.content/findable/registeredMay15 02:30:24Z，完整北京May15。

拟具体**已有覆盖**：actual唯一MULTIMODAL-GENERATIVE-PARADIGMS Ch24 468/470两完整正文及前AsymFlow/后DDPM交接，已明确单位化端点→SLERP→切向预测→Exp整体匹配，以及decoder半径另验、幅度不从交付合同删除、无损未证与欧氏回退。新paper给现成Gaussian-VAE投影/decoder重新训练和ImageNet对照，旧稿不含这些实验，但拟采用的几何/consumer选择已实际承载；不为新增tokenizer验证再追加同机制案例。新质量/成本或半径关键反证以后改变此选择再开，不把其中guard争议扩成全中心主张错误。待root实际NC独核。

## A142 — 15182另一人必要核与Ch24逐字PRE

R127首读有效，作者实际核exactv1 §3.2–3.4、§4.1–4.4/T5及C相应stage/LoRA/费用；zero-shot Full RE10K R-Err2.20劣NoVisDrop2.08，one-shot DAVIS DOVER.448劣.452且Dyn.714劣.753，不能签全面画质/运动不损。Native history编码与target RoPE同帧/remap不覆盖noisy target、invalid mask删tokens实际确认。Mid训练/Distilled推理、stage0 QKVO LoRA32/α32/1000iters、后两stage原refinement，一视频约单A800一小时；warp已有后<1s不含重建/预处理。Pi3X pseudoGT、32/77/100/99人口和source sweep不可混，precision/batch/完整GPUh与SLO ND；未实现/复现、不扩gallery。5分/具体条件入口gap深入。Current仅v1无具名纠错撤回；[DC](SUP_DC_2605.15182_20261019.json)唯一v1May14 17:58:26Z→arxiv.content/findable/registeredMay15 02:30:08Z，完整北京May15。

Actual Ch24 135–145完整shothistory/检索、VACE contextblock与Gloria reference人口段，Ch23/25相邻交接有效上下文已读。现VACE独立reference分支与自产history分账，不承载另一native-history路径如何按target时间赋位并删无观测tokens；只补此替代接口，不改写为所有reference都能当真history。拟VACE完整141段后→Gloria完整143段前一段＋本人compact注：

> 若生成器已经读取视觉历史，还可把相机warp作为另一份有明确来源的pseudo-history，而不新增独立控制分支：将可得观测经几何重建投到目标相机，沿原history路径编码，却给每帧条件使用对应待生成帧的时间RoPE，并删除没有有效源观测的tokens；条件仍与noisy target并列，不覆盖target，也不成为真实未来。[Warp-as-History的有限接口对照](https://arxiv.org/html/2605.15182v1#S3)支持这种位置/可见性分责，但Full并非每项质量都胜，冻结模型仍可能过复制动态对象或在显隐边界失真。另用一段独立视频、约单A800一小时LoRA适配只是调整history reader；不是基座只学一视频，也不免几何预处理。少于一秒只指warp已有后的插入增量，重建、warp、encoder、额外history attention、适配和全部采样均付费；伪相机评价、不同人口与长视频反退不授实时或世界模型保证。几何、运动或总费用失配时，保留原历史、独立参考分支或较短重锚，而不把借用history接口当作观测真实性认证。<!-- source-family:SF-2026-ARXIV-2605-15182 -->

## A143 — 15000另一人必要核与Ch66具体已有覆盖提案

复用R130首读，作者实际核exactv1 §2/4全部必要方法、配对统计与限制。500MedQA/490Afri各自半INTACT/NOTA是不同问题，不是删前/删后逐题配对；每题base/safety才配对。NOTA false-action与INTACT over-deferral并报，Grok3明显代价；861选取HealthBench与191全部redteam不同人口，低风险缺context与urgent cue不能当模型内元认知机制因果。Judge按类别操作定义，κ.685不认证临床真值，不把本文当诊疗建议；API snapshot/temperature/生成重复不完整、Nov2025–Apr2026/5kcap、双judge与全生成/人审成本保留，不复现。5分，设计/安全反侧必要域足。Current仅v1无具名撤回纠错；[DC](SUP_DC_2605.15000_20261019.json)唯一v1May14 16:02:28Z、arxiv.content/findable/registeredMay15 02:25:45Z，完整北京May15。

拟**已有覆盖**：actual唯一PLATFORM-EVALUATION-SYSTEM Ch66 99/102两完整正文，明确不可执行输入×严格/允许澄清合同、缺输入猜答/合理拒绝分别验，先核真正不可答、低风险完整best-effort不应一概拒绝；后parser与独立判分、Ch65/67交接有效层复用。本文NOTA/risk-cue与prompt代价是有用新验证，现稿未含其具体数字，但已承载当前选择；不追加医学案例或采用judge真实性。以后独立answerability标注或受控反证改变上述合同再重开；待root具体NC独核。

## A144 — 15012另一人必要核与具体仅报告提案

复用R131首读，作者实际核exactv1 §3.2–3.3/Eq3–5、§4/T5–6、C2–3/D1/D3直接边界。Expert demonstration为preferred、old-policy回答即使正确也作nonpreferred：这是对专家轨迹的正则选择，不把label解释成所有其它正确回答有错。βσ(−βΔ)由当前sequence margin决定，不保证随时间单调衰减；β内外同时作用、长trace累积logratio，降低β可更强。换成group中心化/tokenclip的FEST-GRPO是新更新规则，不沿固定sample的DPO梯度分解冒精确等价/无需配平。T5 fixedSFT用full population，纯负项collapse保留但不认证三项等人口必要；Avg@8是8解码非8训练seed，局部task反退/外部baseline引数与实现差保留。

1.5B math、128expert加大answer-only集、两GH20096GB/600steps，每step两人口各128×8rollout/8192response，C2 verifier modified/release名义分开；precision/总GPUh/SLO ND，全部expert/两组rollout/reference/verification/search费用不被fewshot抹掉。Current仅v1无具名纠错撤回；[DC](SUP_DC_2605.15012_20261019.json)唯一v1May14 16:12:30Z→arxiv.content/findable/registeredMay15 02:26:03Z，完整北京May15。5分标准完成，未核artifact/复现。

拟**仅报告**保少量expert混合局部配方与gradient-scale反侧，不反删候选。Actual Ch33 544–556完整外部prefix/当前采样与模仿/去提示分责，Ch34 126/130完整margin与两score-gradient、160/168 sequence聚合/局部反馈不等价、185/193–220 reference尺度/实际update验收，Ch32/34交接均已读。现稿不含FEST的具体semi-online混合算法，不冒称算法已有覆盖；但原有支持/梯度尺度、辅助监督与真实部署质量分账已要求这种验收。此小数学配方未独立建立新的混合目标接受条件或可替代现有混合策略的稳定控制规律，不为每一β/系数组合扩写长期案例。若同人口/总预算下的新梯度配平或无提示保留反证改变当前选择，再仅重开对应接口。待rootOnly独核。

## A145 — 14434另一人必要核与Ch76具体已有覆盖提案

复用R135，作者实际exactv1 §3.1.1–3.4/Alg1–2、§4.1–4.2/T1–3必要：共享cluster SID而非唯一item，category首码/InfoNCE与有限suffix分组；Gmax可使cluster仍超Tmax。T2相同top1k人口下beam30 .4422到70 .3825反退，不能用相同beam认证同item人口或更小beam签全链latency。Expert注入真实click/exposure到group统计/梯度，old-policy分母不校正此混合proposal，非每expert正advantage或真实偏好；不采无偏/稳训练宣传。原大样本/4与64GPU、上线8GPU/>200QPS/mean40ms只是整个通道且配置/CI/全GPUh未闭，lookup/截断/ranking/日更与全训练均费。5分标准，未复现。Current仅v1无具名撤回纠错；[DC](SUP_DC_2605.14434_20261019.json)唯一v1May14 06:27:46Z→arxiv.content/findable/registeredMay15 02:11:57Z，完整北京May15。

拟**具体已有覆盖**：actual唯一AGENT-RAG Ch76 201/203/205三完整正文，已把identifier→映射→最终排序分开、共享标识不等选中相关文档、beam可剪真正区分信息、不同排名/召回分验；207/209离散码碰撞/canonical解析完整段及Ch75/77交接已读。现稿不含CQ-SID具体category recipe，但拟采消费者边界已承载，T2是其新验证不推翻选择；专家组非onpolicy不作为RAG机制的新保证采用，Ch33明确group身份/反馈权限而非真值。新item/identifier控制或同预算检索反证改变现有选择再开，不新增Books案例。待rootNC核。

## A146 — 15198另一人必要核与具体仅报告提案

复用R136首读；作者首取HTML超时后正常同入口retry取得，未当外部缺口。实际exactv1 §2.1–2.3、§3.1–3.2/T2–3与§3.4–3.5/T4–5必要核，未读图库。五个新词表token来自code operation映射/teacher轨迹，再混40kperception；部署只普通AR token，没有新图像观察/外部执行。LA在已有functional位置重用整轨迹advantage/clip及位置数归一，负A也增强、不创造独立step credit，零mask guard未闭；§2.2 ref-ratio幂/负KL所谓GRPO与2.3 old/tokenclip不补唯一recipe。Usage是至少一次且correct的binary门，18.7次不能由该定义推出累加收益，保T5现象不采其特定reward-hacking因果。T3 LA相对GRPO V*75.4<77.9、IQ26.3>26.0但Jigsaw51.3<57.7/Spatial62.9<70.6等分项分开；T4局部tokens/3.80vs18.83s和peak1.43vs2.55GB未给完整硬件/precision/batch/常驻范围，不作7B全链显存或所有任务速度证据。未核实现/复现，5分标准。

Current仅v1无具名撤回纠错；[DC](SUP_DC_2605.15198_20261019.json)唯一v1May14 17:59:55Z→arxiv.content/findable/registeredMay15 02:30:31Z，完整北京May15。训练7B/138k映射+40kperception、RL1epoch/三集、Qwen3VL235B判断、无独立seedCI/normalmarkers同数据对照，teacher/新词表兼容/SFT/RL/全rollout与judge全费。拟**仅报告**保离散协议/稀疏位置重权局部方案，不反删准入。Actual Ch29 ConceptTokens107及DynamicLatentRouting109完整段、Ch28/30交接，Ch33完整sequenceadvantage与tokenmask分责已读：现稿明确可调用token不自签语义/事实，命名code不等可解释真实操作。本文没有闭合功能词比普通marker的独立作用或可验证内部操作，也未提供新的过程credit准入条件；不为另一可命名词表重写同原则，不冒当前书已有ATLAS算法。重开同数据marker/真实操作干预或可靠位置更新合同改变现有选择，待rootOnly独核。

## A147 — 三真实POST与74新增同步

R138实际POST14350/14364和R140实际POST15182均已消费，三窄位释放。README六节保存74新＝38I+16Only+13NC+7D、合原Charon75，已补13866外部3及普通32；§4前导漏更新的旧59已校正74，§3新表中空行连续化不动原行。V3与本日限定working检查过，非DAY；A143–146仍待root，不预计结果。

## A148 — 15183另一人反例/date核与中心桥接争议提案

R141必要Source首读复用；作者实际只核exactv1 §2.2–2.3/Eq4、A1深层tree/Gauge/implications、A2 Eq10–14和A3完整矩定义，不第三次全证明/实验。对象是无一般softmax/activation的多项式bilinear模型，sim=1定义为正比例函数；不等同相同softmax概率或唯一内部算法。完整全局symmetrisation的polarisation/Eq4本身未被判错。

独立按公开Eq12–14代算确认：A第一层L=R=I₂，输出u1u2；B第一层L两行为(1,0)、R为(1,1)/(1,0)，输出(v1−v2)²。恒等式B=(x(x+y)−x²)²=x²y²=A，不靠几个随机输入证明。两层同宽/同bilinear tree、hidden非零且顶层都使用二者。第一层GA A=diag(2,2)、GB B=[[3,2],[2,2]]、GA B=[[2,2],[0,0]]；顶层按两四乘法项给self4/self2/cross0，normalized sim0非1。作者另以独立小矩阵代数实际复算相同结果，不是作者实现/数值实验复现。A1承认Gtree严格小于Sn；同tree结构不排这组跨层重因式化，因此局部交换投影与global iff桥仍未闭。A3完整Gaussian矩还含同tensor内部自收缩，不能用A2仅子树交叉项直接替代；不替原文另写新global算法。

[DC](SUP_DC_2605.15183_20261019.json)唯一v1May14 17:58:27Z、arxiv.content/findable/registeredMay15 02:30:09Z，完整可能区间北京May15；current仅v1无具名纠错撤回。保2+2+3=7深入，不因争议降分。标准实验/2.89M LM/归一边界/A10与全部训练、Gram/矩、checkpointpair/回归费用按R141有效层保留，未核repo/复现。拟**中心桥接争议暂缓D8**，不进Books、不用作全局等价/faithfulness已解决或高效Gaussian精确保证。ActualCh5坐标对称与表示/行为分责不替该公式补桥。重开只官方说明metric究竟fullglobal还是tree-restricted、必要算法/复杂度及对此同结构反例的可复查处理；若改用global度量再核相关经验图身份，不重全学科证明。待root另一人处置接纳。

## A149 — 13872具名March31早稿全文资格关闭提案

有限查询 `"S-AI-Recursive" "Slaoui" preprint github` 发现具名早稿，不扩全作者史。实际官方[ResearchSquare v1覆盖PDF](https://assets-eu.researchsquare.com/files/rs-9251795/v1_covered_7750e441-4b3d-49e5-824d-9a94344a471e.pdf?c=1775038183)49页：封面明确Posted March31,2026/DOI10.21203/rs.3.rs-9251795/v1，正文首两页同完整题名/作者/完整AB、RRC、Clarifine/Confusionin、稳定/熵/停止及warmstart核心。官方article页403不妨碍这一官方全文；搜索/ResearchGate月份只作发现，不作日期证据。另SSRN当前页给Apr30但已后修，不依它替代精确March稿。

实际[arxiv exactv1 PDF](https://arxiv.org/pdf/2605.13872v1)51页前四印刷页与该早稿同完整题名、作者/AB及八贡献核心；版本有编排/节号变化（原3.5→4.5等），不据页数认定本窗重要修订。current v2 Aug21题名/耦合条件的后修不倒填May15。v1 May5 20:50:29Z按日程最早May7 00Z，实际DC同DOI arxiv.content/findable、registeredMay15 01:58:45Z本来跨日，不能截登记日；但具名March31公开完整正文已提供早于May15的上界，无需恢复全球最早时刻。拟首次公开资格窗外关闭，不评分、不列候选/Books、不搬其他日报；仅保具名重要修订实际改变条件时局部重开，原贡献潜力层不被改称已Source完成。待root独立资格核。

## A150 — 14704必要Source/date与Ch66逐字PRE（未写）

Actual exactv1 HTML §3.2–3.4、§4.1–4.2、§5.1/T2与§5.2完整提示/Alg1/F2、§6已读足，不扩引用。拟采差额不是低分榜：目标完全不可见时，search/interaction region的containment+面积预算与visible-bbox IoU是不同评价合同，距离改善还不能签覆盖/自动停止。230场景1232投影候选到855人工筛选，Vo=0/V=100只证明遮挡/视锥内；“上下文可推断/单一区域”由筛样，不是信息论唯一性。参考框是3D隐藏目标投影而非可见轮廓。CAcc75要完整包含且面积<25%；Dist四角归一距离×100不是pixel。Human66.43containment/mIoU3.4与Gemini15.20/.74/Dist28.65保原口径，人评人数/协议/不确定性未披露，不用来给模型先天上限。提示Hidden提高GeminiC75但Dist退步；SPoE逐次二分叠框/排半，F2只有Gemini距离曲线，四轮后好于其baseline不证明命中/有效停止、更不保证全模型消歧。配置只声明固定checkpoint/resolution/prompt/decode，未逐项列出具体硬件/precision/数值maxlen/全部重复与CI、端到端latency/batch/concurrency/SLO；人工投影/筛样、额外prompt与所有迭代全费。

Current仅v1无具名纠错撤回；[DC](SUP_DC_2605.14704_20261019.json)唯一v1May14 11:21:41Z→日程May15 00Z至arxiv.content/findable/registeredMay15 02:18:32Z，完整北京May15，非提交/created替代。拟2+1+2=5，因actual评价合同差额深入必要域，未核artifact/复现。

Actual唯一PLATFORM-EVALUATION-SYSTEM Ch66 344完整“同份回答正确目标/联合定位IoU”段前后与GUI状态细粒度段，以及Ch65/67交接已读；原段适用可见/框匹配，并未说明隐藏目标合理搜索区的受面积预算containment。拟在该完整联合IoU段之后→GUI状态段之前补一自然段，不改旧段、不章末堆论文。逐字PRE：

目标完全被遮挡时，还要先决定输出是“物体边界”还是“下一步去哪里搜索”，不能让同一 IoU 同时代签两种合同。后一接口可要求预测区域完整容纳投影参考框，同时限制它占图像的最大面积，并另报到参考位置的距离；这样整幅图不会因必然包含目标而免费通过，较大的合理搜索区也不只因与小框重叠比例低就被判为没有线索。[不可见目标的受限测量](https://arxiv.org/html/2605.14704v1#S4.SS2)采用这条替代分支，但参考来自隐藏物体的三维标注投影、样本又经过“可由上下文推断”的人工筛选，不能把该标签读成像素中有目标证据或唯一可识别位置。Gemini 3 Flash的有限迭代排除使距离下降，却未认证搜索区始终包含目标或模型知道何时停止；prompt间的命中与距离还可反向变化。应分别验区域覆盖、面积预算、位置误差和停止规则，保留歧义/多候选人口与全部投影、人工筛样、模型调用及迭代费用；需要可见轮廓时原IoU仍合理，需要真实接触或行动时必须重观测并由controller验收，不由更近的框批准发现了物体或物理可执行。<!-- source-family:SF-2026-ARXIV-2605-14704 -->

本人末注仅来源/采用边界，待授权精确位后保存并由root实际POST。

## A151 — 14712另一人必要Source/date与具体Only提案

复用R143首读；作者实际exactv1 PDF印刷pp3–12的§3–7/方法Eq7–13、T1/5与直接反侧读足，不全18页附录。AliasBench相同100示范/任务与环境、NN视觉embedding下49.7%异intent邻居只诊断别名，不证明pixel完全相同/所有单帧policy不可识别。模型是Qwen3VL4B当前context+冻结VGGT1B最近16个head-camera帧的每帧camera/4register tokens，经投影/门控attention并追加pool摘要给DiT；m为确定融合条件，无显式intent真值、完整actions/长期state或额外世界模型。T1较强均匀4帧28.1→45.8支持局部历史消费；8/16raw OOM不是质量基线，同30ksteps/16H100/b256不等参数/activation/全部预算。T5current-onlyVGGT64.8<65.3，历史69.5与摘要72.9，但spoon70.8<83.0、双臂17/多目标31.3和窗口外稀疏cue/closedloop shift保留。ICC为预测重叠区动作平方误差，低值可来自一致错误/不动，非正确intent或真实成功。表外baseline、Avg500/50trial不冒训练seed/CI。precision、全GPUh/历史encoder存储、线上latency/batch/SLO ND，额外预训练/示教制备、历史前向/融合与全部action/env回归均费；只simulation、不授实机安全、已校准probe或自适应请求历史。未核artifact/复现。

[DC](SUP_DC_2605.14712_20261019.json)唯一v1May14 11:31:02Z→日程May15 00Z至arxiv.content/findable/registeredMay15 02:18:44Z，完整北京May15。Currentv3 Aug30/EMNLP2026评论，无具名撤回纠错；不因普通编号遍历版本史或倒填后修。

拟2+1+2=5标准完成/**仅报告**，保新有限对照及历史条件配方，不反删准入。Actual唯一MULTIMODAL-EMBODIED-VLA Ch26完整772/774首帧—当前几何历史与反侧、821–845 latentmemory/FIFO/CounterfactualMemoryAudit及Ch25/27交接已读：保存观测≠事实更新，近期窗/encoder费用及历史敏感≠正确选择已作为当前验收要求，现稿不含IntentVLA或AliasBench具体算法/数值，不冒精确已有覆盖。本文额外rolling16帧/gatedpool recipe的局部成功不进一步隔离“intent”解释、容量/预训练或建立新的窗口选择/覆盖/实际outcome接受条件；不为又一合理history consumer追加长期案例。若同表征/全预算的窗口/summary受控反证改变当前选择，或真正跨alias的配对正确性条件成立，再仅重开这条接口。待root具体Only独核。

## A152 — 14487另一人必要Source与Ch24逐字PRE（未写）

R145首读/日期层有效；作者实际exactv1 §3.2–3.5/Eq3–5、§4.1–4.4/T1–6、0.A.1/0.A.4、0.H与0.J必要采用域核验，未扩全部gallery/模型附录。头角色是20%local/25%anchor的attention统计及受限删除干预，不是唯一固有语义。共同跨层入库、当前prompt摘要和每头时间重编码的近似边界成立；固定总预算T4/5、T6支持具体异构分配，不授任意长质量。0.H同分配逐头循环6.62→全融合15.81FPS实证依赖pack/update/kernel，0.I frame-slot不是整机HBM；InfinityRoPE还更省cache。20prompt×30s与×10s/约1.2A100h两口径并存，不能当精确profiling配方。原SelfForcing1.3B/四步/3latentframe chunk/832×480/16FPS、100prompt30/60秒与50×6prompt、单A10080GB，precision/线上并发/尾SLO ND，质量分项反退与>5min多轮摘要丢细节保留。全部profile/驻留/压缩/重编码/pack与回归费，未核实现/复现。Current唯一v1无撤回纠错；根记录DC v1May14 07:27:39Z/registeredMay15 02:13:11Z与arxiv.content/findable联合完整北京May15，作者已核精确记录位置，不把created当pub。维持2+2+2=6，因生成cache语义差额深入必要域。

Actual唯一MULTIMODAL-GENERATIVE-PARADIGMS Ch24完整SparseForcing两段1023–1025及前历史训练/后跨去噪predictor、Ch23/25交接已读：原生训练动态读取不是给预训练head离线异构budget/时间重编码；后者为替代分支非SparseForcing必然后代。拟其完整费用/回退段之后→“沿去噪时间的缓存”完整段之前一自然段，逐字PRE：

同一段历史也不必给每个 attention head 保留相同窗口。可先在固定模型的自产长轨迹上统计头对当前、首帧和中间历史的读取，再用删缓存干预校准不同预算：局部头只留近邻，首帧敏感头另留早期 anchor，宽读取头使用近期 FIFO 与有限 episodic entries。退出近期窗的候选按跨层 key 相似度决定是否共同入库，溢出时再按当前 prompt 选 token 压成摘要；新颖不等于更干净，当前 prompt 保留的内容也可能删去后续指令需要的细节。[这条受限异构头分支](https://arxiv.org/html/2605.14487v1#S3)还只保存空间位置编码，在每头组装的序列上重新赋连续时间 RoPE，并用 varlen attention 与融合 packing/update 避免逐头调度开销；它不是原历史位置与完整 attention 的精确复用。有限同预算对照支持分配选择，长期细节、部分质量与原始时间距离仍不能保证；实现对照从逐头循环6.62到15.81FPS说明预算语义本身不免费，profile时长的两处口径也不一致。离线生成/统计、入库与压缩、重编码、持久KV及全部采样都计费，换基座须重校准；分类、细节或质量失准时扩大历史/恢复统一窗口或较短生成段，不由固定缓存预算签发无限叙事一致或真实世界记忆。<!-- source-family:SF-2026-ARXIV-2605-14487 -->

本人注只来源/采用边界，待root必要原源/逐字PRE独核与窄位授权。

## A153 — 14877另一人必要Source与Ch24逐字PRE（未写）

复用R146首读/date；作者实际exactv1 §3.1–3.3/Eq2–5/Alg1、§4全/T1–3/F5与AppendixA计数、D限制，未读B完整最优性证明/全部稳定性附件。S-CAS来自10个校准prompt未来scale→source-scale mass的静态头排序，部署无未来读数，不是因果信息贡献。三sinkscale/末尺度不继续缓存，每source-scale头次序+逐层提前/事后逐出的必要新接口成立；Algorithm2计KVtoken而非整机HBM，低预算可行域/负Nk边界不私补recipe，binary同权证明不外推weighted全局最优。T3naive/Binary/fullheadscale、1–10校准与sink数对照支持局部选择，D同scale所有token等重要是假设。Infinity2B/H100、8B/B200、CFG3/defaultb8、COCO5k对fullcache FID/LPIPS/PSNR是保原输出非真实质量；GenEval/HPS仍有退，10%vsbaseline20%限cache预算。F5 b1 .87>.82、b2/4 .58/.45同full，只较大batch可运行不改每请求加速；未披露precision/在线concurrency/尾SLO。校准生成/attention提取、cache/pack/prune/kernel及全部输出验收均费，未核实现/复现。Currentv2June17无具名撤回纠错，exactv1不倒填后修；R146已实际DC arxiv.content/findable、唯一v1May14 14:22:34Z至registeredMay15 02:22:40Z联合完整北京May15，作者核精确记录而非created替代。

维持2+2+2=6，因生成缓存/逐层预算consumer的具体gap深入必要域。Actual Ch24 SparVAR完整段76及前motion连续修正/后ToProVAR两完整段78–80，Ch23/25交接已读：原有稀疏pattern的来源尺度/坐标迁移与可少算layer/token，未承载逐层新增KV峰值和head-source-scale释放先后，因此非换论文名重案例。拟在SparVAR完整段后→同scale ToProVAR首段前一自然段，不改旧段，逐字PRE：

跨尺度还要把“少读取哪些位置”与“哪些历史KV继续驻留”分开：下一尺度一次加入许多token，只在scale结束后检查缓存预算，仍可能漏掉逐层新增KV时的瞬时峰值。一条[受限head–source-scale分配](https://arxiv.org/html/2605.14877v1#S3)先在离线校准生成中，按后续尺度读取某来源尺度的平均attention mass，为各层各头建立静态保留次序；部署不偷看尚未生成的未来，也不由低attention认证信息无用。它保留早期sink，在当前scale前提前逐掉部分选定head–scale，其余在对应层执行后释放，并以token-cache计数逐层检查预算，而非全头统一扔掉相同旧尺度。这个计数模型不包括权重、Q/activation、workspace或allocator，预算低于不可逐部分时也不能套用通用可行性保证；同scale所有token等重要与静态校准失配仍会损质量。有限Infinity对照支持质量—缓存取舍，却有分项退步，H100的batch1更慢、batch2/4约持平，能跑更大batch不等每个请求更快。校准前向/attention提取、驻留、pruning/packing/kernel与完整出图均付费；质量或真实峰值不合格时扩大保留、回到完整KV或更小batch，不把binary特例的选择性质外推为加权head–scale全局最优或整机HBM保证。<!-- source-family:SF-2026-ARXIV-2605-14877 -->

本人注限来源/采用边界，待root有限独核/指定窄位。

## A154 — 三指定单段实际保存待POST

消费R14713872资格窗外/第三项与R14814712Only19（80既成/25普通）；14704 Ch66 349、14487 Ch24 1029、14877 Ch24 78已按R148/149指定唯一自然段保存，HeadForcing正文数值改为已授“融合路径与逐头循环有明显吞吐差距”，其余逐字一致。本人来源/边界注分别Ch66 6764与Ch24 3377/3379；作者已实际完整读回三新段/各直接完整两侧/三完整注，限定diff-check过。尚不预支三I，待root非writer真实POST；同文件未覆盖他人段。两DC精确原件已保存并实际核身份/唯一v1/client/findable/registered，与R145/146一致。

## A155 — 14497必要Source/date与具体Only提案

受影响理论另记：实际B.1–B.2的Assumptions3–5/Th1–2只核必要公式。Eq22先写Var(ε)/Var(f)，随后却写梯度f平方/梯度ε平方，倒数方向不一致，再接Eq21的noise/signal与长度比式；不能据这一链认证signal-to-noise或Δon必为无偏bias估计。本次Only提案只保公开经验配方/关键对照，不采用该理论背书；若root判断此冲突必须整项理论争议隔离，再按精确命题处置，不降分/删候选或补作者公式。

准入A56/R49实际决定域复用；作者exactv1 §3.1–3.2/Eq1–4、§4.1–4.2/Eq5–7、§5全/T1–3/F3–4、§6及B.3/G必要读足。具体增量是online/offline两人口的critic差额proxy交给滑窗UCB选固定mixture arm，不是单靠MAB/bilevel名准入。固定函数类里抽样分布改变Bellman投影，低TDerror不签policyreturn；但无限维理想gradient不等实用bandit目标。Assumption1 offline支集内低uncertainty/足样本、Assumption2缓慢训练，Eq25将dπ近似doff及Qbehavior近似当前critic并非等号。B.2/Th2用于解释的small-policy-step、噪声短相关长度/早期dominance等条件不自动适用于所有IQL/PPO；R_q=Δoff−κΔon只是可用proxy，不采“无偏外层”或后期Δon必可忽略/所有最佳mix保证。Linear5arm .1–.5/周期固定比率，不是样本级选择。

T1同IQL与固定/均匀/递减/BR、4seedmean±波动支持局部适应，antmaze-umaze-diverse72.12±23.29弱BR80.66±3.99、walker-medium60.17弱Uniform64.30，非全任务支配。T2 κ .5的halfcheetah-medium77.09高于default1的74.57，调参“不敏感”不等唯一最优。仅toy MDP F4说明proxy行为，不证明真实大环境return精确估计。G main8RTX4090/MLP256、batch256、1e6envsteps/replay1e6；precision/全部GPUh/独立线上latency/batchconcurrency/SLO ND，“无明显额外费用”未给完整timing表，双buffer采样/critic评估、UCB、全部预训/交互/多arm回归均计费。未核artifact/复现，2+1+2=5标准。

[DC](SUP_DC_2605.14497_20261019.json)唯一v1May14 07:35:58Z→arxiv.content/findable/registeredMay15 02:13:25Z，联合区间完整北京May15；当前已核层仅v1/IJCAI2026接受说明，无具名纠错撤回。非提交/created替代pub，不因接受名字重拥有。

拟**仅报告**保有限replay新proxy/控制反侧，不反删准入。Actual唯一TRAIN-DATA Ch27 1172–1178外层真实heldout目标/inner synthetic loss、1218–1246 checkpoint-coupled selector与trainer/objective分责、14350采样vs重权及Ch26/28交接已读：现稿不含ROAD的双差额算法，不冒精确已有覆盖。当前已要求独立真实目标/预算检验而不让proxy批准update；该局部bandit配方并未给新的可验证off-support uncertainty/return接受条件，也未改当前“目标与代理分责/冻结mixture回退”的选择。不为每个可用critic差额追加长期案例；若matching population/预算的proxy误差界、真实目标因果对照或新replay稳定条件改变当前选择再开。待root必要域/具体Only独核。

## A156 — 14587必要Source/date与Ch72逐字PRE（未写）

A56/R49一次贡献决定有效；作者actual exactv1 §3–4、§5.1–5.3/F3/4/8/T1及§6、B.2/C.1/C.3–C.5/D/T5、H.1定理及A1–3必要假设读足，不扩全部47task/四attack组合表或攻击实现。9,024=2threat×8setting×47task×4attack×3seed，另5,640组合案例，不是14,664独立真实部署样本。TM-Post攻击者有transition state/action/reward污染或下载后再发模型的权限，不是普通用户无权限修改。固定poison≤.4%、continuous目标动作tolerance(.1Bipedal/.05其他)、BadRL去trigger优化/各攻击加actiontamper，保共同框架不冒原attack实现全同。PPO/小3–4层TanhMLP/64hidden、10RTX4090，precision/实际总GPUh、onlinebatch/concurrency/SLO ND；全部攻击/良性训练、SAM额外求值、pathology统计/重复行为验收均付费。3seed统计及mean±SD/范围不代表充分独立N/CI。

TMpost robotaggregate ASR .178→.326与SAM更低sharpness支持有限“flat不等更少backdoor”反证，TM-Scratch影响小不混。T1组合None .178±.157/BTP .745±.230到SSW .418±.092/.915±.131，但存在良性退步/攻击异质，不称所有干预单调恶化或安全。D无污染常规BTP SAM .977±.068弱None .989±.032，全部组合更退；一组norm/rank/梯度可视化不识别唯一后门通路因果。H.1只在同向backdoor gradient、非零clean residual和正曲率eigendirection、SAM一阶近似下给局部放大，不授非stationary整训练的通用必要机制。SCC与sharpness检测只是提案，原§5.3承认任务间阈值与其他sharpness来源未解，不当可用detector/真实风险保证；本次不提供攻击recipe。未核artifact/复现。

Current仅v1/ICMLJuly未来会议信号，无具名撤回纠错；[DC](SUP_DC_2605.14587_20261019.json)唯一v1May14 08:58:24Z→arxiv.content/findable/registeredMay15 02:15:32Z，完整北京May15。拟2+2+2=6，因安全直接反证深入该受影响域，不以案例数量/理论名加分。

Actual唯一PLATFORM-SECURITY Ch72 35/37完整数据批准/更新artifact和Benignfinetuning反侧、39/41完整mask归因/修复/能力保留后段、Ch71/73交接已读；现有论证没有optimizer/plasticity/flatness安全反侧，Ch4曲率sensor只负责训练稳定而不另承载安全真值。拟在完整Benignfinetuning费用反侧后→“更新位置也可”前一自然段，不改旧data论点，逐字PRE：

数据和更新位置之外，优化规则也属于待验的安全身份：为维持可塑性或寻找较平损失区而加入的干预，不会自动继承原模型的抗后门性质。一个[受限DRL对照](https://arxiv.org/html/2605.14587v1#S5)在相同攻击框架中比较不同训练干预，发现SAM在已有policy被恶意post-training的设置下可同时降低所测sharpness、提高触发后目标动作成功率，部分组合又进一步放大攻击；从头训练的结果却弱得多。因此平坦、clean任务效用、触发行为和更新阶段须分别验，不能把“更稳定训练”当作去后门证明。这里攻击者仍须有污染transition/重发checkpoint的权限，有限PPO/小MLP和已知触发实验不推出任意LLM优化器的风险率；梯度方向图与有同向/曲率假设的局部近似，也不识别唯一普遍因果。不同任务sharpness量纲和其他成因尚未校准，低值或尖峰均不能直接变成自动检测阈值。额外优化求值、污染/对照训练、多seed、触发与良性回归全计费；变更optimizer或组合后应绑定新artifact重新验收，证据不足时保留可信未污染版本、数据/产物隔离和独立行为gate，而非只按loss几何批准发布。<!-- source-family:SF-2026-ARXIV-2605-14587 -->

本人注限来源/采用边界；待root必要Source/实际owner/逐字PRE独核与窄位。

## A157 — 14779另一人具名April20正式全文资格关闭

复用R152限定线索；作者实际取官方[proceedings HTML](https://proceedings.iclr.cc/paper_files/paper/2026/hash/14c1c1c1dabd8179f77895de25391ce9-Abstract-Conference.html)原始meta，citation_publication_date=2026-04-20，citation_title/两作者/citation_pdf_url匹配；不是只“ICLR2026”年份或接受状态。网页PDF阅读工具一次不可得后，用正常同官方Paper URL内存pypdf取得37页，仅首两页完整题摘/主要贡献：CPQL/Peng多步Q、behavior/target混合fixedpoint、conservative目标与offline→online均与已校准本稿题摘/原root Mayv1身份层同核心。完整PDF不是当前摘要外推，未遍历37页proof。官方正式出版日+同核心全文已给May15前上界，网页/工具障碍未当external终态；不再扩OpenReview403/API历史或追全球最早日。

确认**第4具名窗外资格关闭**，不评分、不列本日候选/Books、不搬其他Daily；原贡献潜力不改成“没有价值”，未来具名重要修订只局部核实际增量。83既成/3external不变，普通22→21；184=73close+4outside+83既成+21ordinary+3external（其余新提案未预计）。

## A158 — 14897另一人必要Source/date与具体Only提案

复用R150首读，作者实际exactv1 §4.1–4.2/Alg1–2、§5.1–5.4/T1–3及§6，未读所有图像像素/代码。局部线性subpolicy以teacher rollout state-action监督，nearest-codeword Voronoi路由；距离足够远且critic评学生动作低Q的state聚类扩cell，下一轮再训，末轮不得只扩容不训练。§4.2明说Q递增取前ρ，限定解释Alg1 top-N歧义而不替原文补实现。低Q不等teacher高Q/模仿误差大、OODcritic/距离尺度与分段边界可误导，不采小训练loss→无过拟合或系数→teacher真实因果解释。

4control任务/TD3Zoo、每run新100teacher rollout、20run，T2critic只需较少cell，但MountainCar90.8<random91.9、Lunar154.8<160.8且波动更大，Bipedal226<teacher313；SimpleGoal13.5略高random13.4不从正文统一归成“除Walker均random更好”。Lunar55.9对152cell不代表matchedreturn或已测CPU/GPU净latency；图选best run/iteration，二轴图省略另外22维不恢复完整decisionboundary。手调min-distance/新增率，不同cell数/预算与teacher参考由采集人口计算需保身份。未披露hardware/precision/总GPUh/实际inferencebatch/concurrency/SLO，teacher rollout/critic查询、各k聚类与silhouette、多次全student训练、nearest搜索/环境回归均付费。未核gitlab实现/复现，5=2+1+2标准。

[DC](SUP_DC_2605.14897_20261019.json)唯一v1May14 14:38:56Z→arxiv.content/findable/registeredMay15 02:23:11Z完整北京May15，current无具名撤回纠错按R150有效层复用；later May25poster不作更早pub/不扩全venue。

拟**仅报告**保critic引导容量而非全局动作误差的新局部配方/负面对照，不反删候选。Actual TRAIN-SFT Ch29 362–382完整density/多层容量分配、studentrollout/latent拟合与heldout行为相反、未蒸馏student基线/同预算人口，及Ch28/30交接已读：现稿没有本文Voronoi算法，不冒精确已有覆盖。此方法用熟悉分区/线性拟合/critic proposal换较少cell，其四任务对照未建立可替代现有surrogate选择的净质量/可解释性取舍（较少cell亦未测人类解释或runtime）；低Q而非teacher-relative错差的接受域尚未验证。无需它证明普遍最优才保经验贡献，但在当前主线没有新增长期采用判断，不为该局部XAI配方加一案例。若同return/全费的容量分配控制或独立解释有效性反证改变现有监督选择，再只开该接口。待root具体Only独核。

## A159 — 14423另一人必要核与Ch32逐字PRE

复用R153首读，不扩93页证明。作者实际同精确v1 PDF印刷pp4–9完整§3–7/Al1/Eq5–12/Ass1–5/Th1另核，接受共同已知有限φ/全policy精确线性value像类、B正交共享/本地ω和θ、两采样链及reset权限。原Pk的TD(L)与带reset的actor伴随kernel不可混；Alg1 TD行与Eq7差别不发布recipe。Th1先有L/K/高阶项，L=K²及足大T才主导1/sqrt(TK)，不是等总费K倍加速。Nonlinear FedPerPPO六Hopper动作映射/每client .4M steps/3seed与弱scratch迁移仅经验分支，5.42×/3.50×为return比。必要正文hardware/precision/完整wallclock/通信并发SLO未闭，不声称全文ND；双链/reset/通信QR/预联学/迁移均费。未核实现/复现，2+2+2=6。

[DC](SUP_DC_2605.14423_20261019.json)实际唯一v1 May14 06:10:31Z到arxiv.content/findable/registeredMay15 02:11:41Z，完整北京May15；current无具名信号R153有效层复用。Actual TRAIN-PPO Ch32 85–91完整POISE/GenAC与dense turn critic、Ch31偏好/Ch33交接已读；原文按critic计算路径组织，没有异构client共享value子空间与独立actor/head、不同采样人口的边界。拟GenAC完整费用反侧后→dense game critic前唯一段，不另占Ch36collective owner；逐字PRE：

多个client的策略面对不同transition时，共享critic表示不等于共享policy，更不等于把所有参数平均。一个[有条件的联学分支](https://arxiv.org/pdf/2605.14423v1)把value拆成跨client共同的特征子空间、本地线性head和本地actor：服务器只聚合子空间更新并重新正交化，本地head与actor保留各自身份。它还区分两份采样合同：critic读取原环境链，actor读取带初分布reset的伴随链，不能拿同一份任意replay替换二者。其分析要求已知有限特征、所有相关policy的value都精确落在共同低维子空间、统一探索/混合及跨client子空间覆盖；单时间尺度是步长保持固定比例，不是免除稳定条件。按轮数的主导收益还需随client数增加轨迹长度并控制高阶项，不认证固定总交互下的线性加速；非线性PPO迁移实验也不证明这些线性假设。两条采样链、可reset环境、通信/正交化、前期联学与迁移回归均付费。共享结构不成立、reset不可得或本地value失准时，保留独立critic/head与本地策略、真实rollout校准，不由共享维度较小批准异构任务间的行为保持。<!-- source-family:SF-2026-ARXIV-2605-14423 -->

## A160 — 14599另一人必要核与Ch31逐字PRE

R154首读有效，作者actual exactv1 §2.2–2.4/§3全/Th3.1、§4–5、A4/PropA6识别条件、B1必要几何、C1 KKT/Eq125–133、C2 Eq139–143及B5 Eq116–117/D1 Eq149–152另核。正β/有限horizon/已知共同转移、reward→soft-policy类的population等价；随机有限样本不能去残差，deterministic含初分布另有条件。反向βlogπ需要有界density，不授任意同参数化。Shaping与不可达null分账；C1约束最优变分不等式不设边界梯度零。C2 Eq140梯度差方向反于C1 Eq128，B5(-x)χ(-Rx)与正递增闭式符号不一，精确localized/burn-in常数不采用；不判结构等价或全部IRL理论为假。统计误差为类内population最优的Hessian范数/独立轨迹，misspec保类内KL。无工程实验故硬件/precision/SLO不适用，统计率非wallclock；known transition/planner/数据/曲率估计及验证全费。2+1+3=6，原7仅未冻结暂拟，不按工作量变分。

[DC](SUP_DC_2605.14599_20261019.json)实际唯一v1 May14 09:07:31Z→arxiv.content/findable/registeredMay15 02:15:49Z联合完整北京May15；Augv2不倒填。Actual TRAIN-RLHF Ch31完整BT目标/比较人口/支持反侧97–103、后trajectory二元反馈105/Ch30–32交接读足，现稿识别的是pairwise胜率，不含demonstration→reward类的两种等价及有限随机残差。拟比较支持完整反侧后→受限trajectory偏好更新前一段；直接BC仍合理，不把IRL替代RM的历史谱系或真实效用恢复写成事实，逐字PRE：

只有专家demonstration而没有比较标签时，直接行为克隆仍是合理基线；若还要从轨迹解释reward，就必须分清“同一行为分布”和“同一真实效用”。在已知有限horizon动力学、正entropy系数及受限reward类下，[Min-Max-IRL的结构结果](https://arxiv.org/html/2605.14599v1#S3)把reward优化映射到该类诱导的soft-optimal policy似然，而非任意policy网络与任意reward参数化都可互换。随机转移下等价先属于population目标，有限样本的零均值transition残差不自动为零；确定性动力学及相应初分布才允许直接把这条经验目标等同。即使恢复了最优policy，potential shaping及给定初分布不可达部分仍使reward不唯一，不能从模仿成功推断唯一动机或对未访问状态授权。其线性有界特征/局部曲率条件下的误差还针对类内population最优参数，样本数指独立轨迹，不是token数；原局部快率证明的具名符号冲突未闭，本处不采用其完整常数或burn-in保证。已知转移、inner planning、特征与曲率估计、专家采集和独立outcome验证都计费；模型失配或支持不足时，保留行为克隆、可信偏好监督及原策略，不由较好likelihood批准真实reward恢复。<!-- source-family:SF-2026-ARXIV-2605-14599 -->


## A161 — 15196 RefDecoder必要Source/date与Ch23逐字PRE

Actual exactv1 §2、§3.1–3.4/3.6–3.7/T1–2、§5、B1–5/B7、H/T9、I/T10与J/T11及K直接反侧足够，不读全部gallery/跨方法附录。冻结VAEencoder/quantconv与denoiser，单conv+norm参考映高维，在每级拼时间维joint attention再独立upsample；sharedblock/各级patch投影不等参考复制无损，latent dropout0–.7/随机同clip参考/两阶段训练改变依赖。Fixed-seed五sample/每prompt的同一savedlatent、50steps/CFG5/17frame/480p两decoder配对隔离decoder端总干预，不隔离每组件/新增参考信息，也不证明原latent已保存细节；B7因配对不报SD不等人口uncertainty为零/bitforbit已复现。

T1 Wan WebVid LPIPS .037弱原.032、LargeMotion .053弱.048，T2 camera19.1弱19.3，imag70.1持平而非全部12改善。H首帧训练对随机参考退至31.9，随机训练首帧overall34.2对34.1，但reference-frame40.0弱40.8，正文“bestfirst”/“allbetter”需分项；I从5到7block若干PSNR反退，非每级单调。J dropout与short→long训练收益保操作点不授latent信息真实保持；K只有局部残差注入/ghosting解释不证明所有ControlNet无时间推理。8H200/batch2每卡effective16/5days/100ksteps训练、decoder微调仍付费；主§3.6 pipeline72037±16→74584±40ms不是零费，精确runtime hardware/precision/batch/concurrency/SLO未绑定，未核代码/像素或复现。

[DC](SUP_DC_2605.15196_20261019.json)唯一v1 May14 17:59:52Z在18Z截止前，最早May15 00Z至arxiv.content/findable/registeredMay15 02:30:28Z完整北京May15；created02:30:27Z不代registered，current仅v1无具名撤回纠错。2+1+2=5；实际MULTIMODAL-REPRESENTATION Ch23 565–585完整连续codec/PAE/Cheers旁路及后AGFT、Ch22/24交接已读。Cheers旁路读当前生成latent的decode，不是外部参考直接被重建decoder读取；拟Cheers完整反侧后→AGFT前一段，唯一owner不重复Ch24采样范式。逐字PRE：

压缩latent与生成prior不变，也不意味着输出细节只能由它们决定：若用户本来提供了参考图，可另外把参考编码成较高维tokens，在VAE decoder的各级上采样中与视频tokens共同attention，再分别上采样参考和视频两支。此时decoder消费的是“latent＋参考＋新decoder版本”，不能继续把重建质量当作latent独自保留信息的证据。[受限条件解码对照](https://arxiv.org/html/2605.15196v1#S3.SS3)冻结encoder与denoiser、对同一批已保存latent交换decoder，支持把这部分差异定位到重建消费者；但不能由此证明原latent已保存全部细节，或参考中的纹理就是真实目标。训练期latent dropout与随机参考帧改变依赖，decoder/参考encoder仍须训练；部分LPIPS和camera指标反退，固定seed配对也不取消人口不确定性。参考读取、attention、decoder训练与完整decode均付费，额外信息不叫无损压缩或免费恢复。参考缺失、错配、过时或细节质量不合格时，保留原无条件decoder/codec和独立重建验收，不由更清晰图像批准latent可逆或生成分布不变。<!-- source-family:SF-2026-ARXIV-2605-15196 -->

## A162 — 15116 DriveCtrl必要Source/date与Ch24逐字PRE

复用R34一次准入core，作者actual精确v1 §3.1–3.3、§4.1/4.3/T3–5及§5–6足够。原Wan2.2-Fun-A14B-Control首帧条件现在改作unpairedstyle、结构depthvideo在patchembed前主条件，冻结backbone只训各block self/cross-attn及FFN LoRA；random-reference训练/推断打破逐例空间对应，不保证style/geometry完整分离或原条件能力保持。High/low两adapter独立各singleL40/25epoch12h；每域10×40frame白天clips，eval60×40frame/2400referenceframes，CI/独立repeatseed/precision/真实inference全时延与batchconcurrencySLO未披露。T5同LoRA去randomref mIoU .203对full .455支持局部消费者角色重配，但非所有因果因素已识别；full SSIM .831弱AnimateDiff .856/Carla .852，DepthAnything同派生depth回读非metric真值，标注共享需独立验。DVRS为现有领域checklist/judge组合不另计通用评价贡献；小日间样本/领域差额不授通用物理或真实驾驶安全。全部depth/text/reference/双adapter与生成/下游训练费用保，不提供部署能力。2+1+2=5。

[DC](SUP_DC_2605.15116_20261019.json)唯一v1 May14 17:29:35Z至arxiv.content/findable/registeredMay15 02:28:32Z联合完整北京May15，current仅v1无具名警告。Actual MULTIMODAL-GENERATIVE-PARADIGMS Ch24 280–289完整ArtifactWorld/clean参考分支及specpage/双模态目标，Ch23 118–120 ST-STORM反侧和Ch25交接已读。现稿有参考噪声/消费者身份，却没有“预训练首帧→新style-only角色”用打破对应的数据干预与同adapter反侧；不是宣称所有风格条件都是泄漏。拟clean参考完整段+独立2506-24085 marker后→specpage首段前一段，逐字PRE：

参考图的噪声身份相同，也可能承担不同语义角色：预训练I2V把它当目标首帧，新任务却可能只要其外观而由另一视频决定几何。直接复用原条件槽会把旧的空间对应带入新输出；一条[受限适配分支](https://arxiv.org/html/2605.15116v1#S3.SS1)在训练中随机重配参考图，打破它与目标的逐例空间对应，同时让结构视频进入原主干、只训练LoRA。其相同adapter下去掉随机配对的对照支持重新声明条件角色，而非证明style/geometry已纯净解耦或生成标签可直接复用：所测结构相似仍弱于另一基线，深度回读是模型proxy，领域judge也不授物理真值。双噪声checkpoint的适配、深度/文字制备、参考编码、全部采样及下游验证均计费；小日间数据的局部结果不签任意场景或实时性。参考角色、结构遵循或标签质量失配时，保留原首帧I2V、显式结构条件与独立内容检查，不因视觉更自然批准新条件合同。<!-- source-family:SF-2026-ARXIV-2605-15116 -->

## A163 — 14063截止换算具体纠错、恢复同日资格与Ch23逐字PRE

A134将14:00 Eastern截止误换为20Z（把20:00公告时间混作截止），R123继承此错；保留旧轨迹但本节明确更正。实际[官方availability](https://info.arxiv.org/help/availability.html#announcement-schedule)表为Wed14:00→Thu14:00的提交Thu20:00公告，May的America/New_York为EDT(UTC−4)，故截止18Z、公告次日00Z。原[DC](SUP_DC_2605.14063_20261019.json)唯一v1 **May13 19:38:08Z=Wed15:38:08EDT**，在18Z截止之后；最早公告界是ThuMay14 20EDT=**May15 00Z**，不是May14 00Z。arxiv.content/findable/registered **May15 02:03:15Z**为最晚上界，整个组合区间完整北京May15。不是截取登记日，也不把常规日程独立当实际公开。具名元数据同身份/版本无矛盾；日期有限恢复接口原本可执行，故A134external理由撤销，不再索日公告/月目录。2025适用文档blob/raw网页工具cachemiss，root既有已核历史层可复用并独核，不为此扩其他日或全月。

仅机械查本日DC文件发现同受18–20Z换算影响的8个身份13974/13989/14028/14040/14047/14054/14063/14068，其中已接受的同日结论本来正确，14040 R161亦用aftercut；唯一错误隔离是14063。13866周六v1跨多日与14553正式稿日期外部不受这条错误影响，不泛重开。原Source R115及作者A134对§3/Eq1–5/Alg1/P受影响域的另一人有效层复用；本次5=2+1+2标准，不重540GPUh全表，不把日期可用当Source正确。

Actual MULTIMODAL-REPRESENTATION Ch23 256–262完整ProtoTTA/反侧与open-generation head适配、1192模态fusion entropy/EMA局限及Ch22/24交接读足。现有gate处理伪样本/模态权重，没有同一source可靠性信号同时关目标anchor与agreement过滤、但init/reset仍source-dependent的边界。拟ProtoTTA完整反侧后→开放生成head适配前一自然段；逐字PRE：

保留源模型作anchor，也须控制它参与适配的所有显式路径，而不只缩小其中一个loss权重。一条[受限source-gated分支](https://arxiv.org/html/2605.14063v1#S3)用同一源输出熵信号同时衰减参数anchor与source-agreement筛选；源输出趋均匀时，前者消失、后者回到放行，使目标中这两条source依赖共同退出。这个代数退路不证明runtime已完全source-free：专家初始化和reset仍读取原权重，剩余目标可计算也不等稳定、不塌缩或一定更好。熵只反映分布形状，低熵错源不会自动关门；置换logits保持熵的stress也没有替换初始化/重置用的source参数。主表增量混有flip等辅助，部分reset与backbone切片反退，不能把全部收益归gate。Source前向、增强、适配、reset和独立校准都付费；源可靠性或旧任务质量失配时，保留可信source snapshot、冻结适配与独立目标域监督，不让一个不确定性proxy批准持续更新安全。<!-- source-family:SF-2026-ARXIV-2605-14063 -->

## A164 — 14758另一人中心分母反例/日期与D9提案

复用R158首读有效层，作者actual exactv1 §3定义3/5、§3.1 Def6/筛样步骤及§3.2 Th2/完整证明另核，非无差别全proof/版本史。独立代算：取H=[0,1]、H*=[0,.5]且f(h,o)=−1，完美可行classifier仅接受H*。原§3.1以accepted N为分母，任何N≥1其violation比例p̂=1；Def6目标VolΓ/VolH=.5。Th2宣V~=VolH·p̂=1，normalized误差固定.5，而classifiererror=0、εclf/εver可选.05且N/M满足任意大样本阈值，不能使.5≤.1。独立样本/完美classifier已经成立，不是稀有MC误差或classifier不够好；对应条件概率不能直接替全域体积概率。不是判Hoeffding本身错、不私补接受率修作者算法，也不由generic可行history原则绕中心保证正面写Books。Max单agentvolume与任一agent失败风险另分账，uniformvolume非真实visitation。

有限实验/硬件/分类器训练未纳入verificationtime等沿R158已实际必要原证复用，不声称作者第二次全表；未核实现/复现。[DC](SUP_DC_2605.14758_20261019.json)作者实取唯一v1 May14 12:22:54Z→arxiv.content/findable/registeredMay15 02:19:48Z联合完整北京May15；current仅v1/no警告复用R158轻核。6=2+2+2安全/保证受影响域深入，拟第9中心争议/暂缓，不进Books、不作真实风险或有界误差证据，不反删候选。重开需作者明确抽样总体/Def6目标/估计分母及有效相容定理，或有原始接受率/样本可复查所测目标；不要求全部RNN证明重来。

## A165 — 15199另一人必要Source/date与具体NC提案

R159首读有效；作者actual精确v1 §3–5、B4.1 Eq22–23/B5 Eq45、C1/C2必要bank/控制状态和F2/T15另核。最初一次完整HTML输出中段tool截断已识别（References后局部缺段），未据缺段判访问故障；本次只用实际返回完整上述必要段，不冒全部51指标/全部supp已二读。140episode/2491shot为过滤/LLM改写人口；同错误角色重复可高相似，fidelity与跨shot一致须分别计，None可越过Eq22 gate，B5全missing排除与B4joint分母需声明配置。F2 rawface EntityMem .678<StoryMem .718但coverage .60>.31，joint反转主要是覆盖而非条件身份更准；原始两passed人口亦不同，不从它断言所有同人口配对都更差。DINOface/object和object/scene LLM列反退，gap曲线是门控后人口，不授间隔单因果。有限200/3researchscientist验证与sharedGemini curation/judge不使全人口真值独立。

EntityMem先合成/分割/筛选reference bank，再由entityschedule/layout供shot，前shot末帧单供continuity而不覆盖bank；合成reference仍可能错，bank收益未独立隔离layout/prompts/筛选全部因素。两8L20节点是资源不是全latency/precision/concurrencySLO，候选重试/LLM/所有生成与judge均费，未核artifact/像素或复现。[DC](SUP_DC_2605.15199_20261019.json)实际唯一v1 May14 17:59:55Z在18Zcut前→arxiv.content/findable/registeredMay15 02:30:32Z联合完整北京May15，current仅v1无警告复用R159。2+2+2=6标准。

拟具体**已有覆盖**唯一PLATFORM-EVALUATION-SYSTEM Ch66：actual 338–347完整方向/valid分母、CFHR joint-vs-conditional/coverage与选项+IoU联合成功，182–190完整高相似不认证语义条件/参考集合分责及Ch65/67交接已读。它们实质承载保持全部 eligible人口、条件指标另报、语义符合与相似分验，恰对应本文raw×coverage与同错相似反例，不冒现稿已有EntityBench schedule/数值/算法。第二个生成分支actualCh24 ShotStream/CausalCine与VACE完整参考-vs-generatedhistory段已读：参考/continuity状态不能互替已有承载，EntityMem预制按entity的具体agent工作流保报告有限新设计，但未给超出该分责的新可靠性/净成本条件，不为局部reference布局组合重复写章节。候选/新测量/反退仍保报告，不因NC逆删或宣方法无价值；若独立bank/布局对照或新的联合metric条件实质改变现有判断再开。待root实际owner/具体NC独核。

## A166 — 14040另一人必要测量核/日期与具体NC提案

R161通用测量首读复用；作者actual exactv1 §3.3/T2/Alg1、§5.1、§6、A1/T4和D judge协议/逐chunk分母另核；不采用物理科学发现/RLrecipe，未读其全部训练配置或领域演示。5gramJaccard .4零命中对cos .85候选与Haiku判词，4846是pair/134是judge近重复，不能改称4846真实污染record；未检查阈值下漏检/不同embedder或一例校准不签语义全清。59同题同Sonnet ET/EN严格配对有局部17pp差，不排翻译/语言能力混杂；79.7→33.4换format/genre/novelty，无2×2同题控制不授46pp单因果。D所列98+100+99+98+96=491/500仅9missing(1.8%)，不支持13.9%“noise floor”；不得以一般judge校准原则冒其确切分母已闭。主弱judge/去污judge/strictliberal及subpartAND保身份，50样本κ.44不签独立真值。全语义检索/人工/多模型生成judging计费，未核实现/复现。

实际[DC](SUP_DC_2605.14040_20261019.json)唯一v1May13 19:00:57Z在18Zcut后→最早May15 00Z至arxiv.content/findable/registered02:02:44Z同北京May15；后来v2改verifiers不倒填v1Recipe题名/证据，current无具名警告复用R161层。2+2+2=6标准。

拟具体**已有覆盖**唯一PLATFORM-EVALUATION-SYSTEM Ch66：actual 203–215完整翻译构念/同item与不同题源/删选项协议，894–916完整目标人口/误判scorer/输出sensor不能代训练provenance，另Ch27 843–895完整exact/ngram/semantic-transformed contamination层级及阈值/召回误报/冻结留出已经读足。Ch65/67交接已读。不是现稿包含Physics-R1的134判词或59题新反证；本次新增实证与具名分母争议保报告，长期采用选择已由这些具体论点承载，未新增可验证的完全去污或因果校准条件，故不为一个科学题源重复追加案例。不反删候选、不用NC宣判13.9%成立；若原始逐条判词/同题format×novelty/独立校准改变这些具体边界再开。待root实际owner/NC独核。

## A167 — 14211另一人必要核/日期与Ch84逐字PRE

复用R162首读；作者actual精确v1§3完整Al1–4/四状态及§4.1–4.5/T1/§5、F完整Al5与H配置必要域另核，未读所有游戏/附录prompt。4agent各64frame/10keymemory，共policy/任何计时器4800触发停全部，K首次cluster非真实milestone进度；更新K→IDM→policy，IDM吃真实/随机动作轨迹，internet伪标签和teacherforcing不等无动作监督。DINO greedy匹配非时序因果，四方向81%不代表AB按钮/完整动作正确。主同8h/hardware配置四H100/1.2B/visionFP32+TransformerBF16/batch4；单训练12rollout对ASH3训练×4agent不等12独立训练，288GPUh与4days×4GPU=384口径冲突保，不授严格等费。消融online-training GPUh未含初训3/9GPUh/全视频索引检索，6h四轨迹offline replay不授lifelong无遗忘；v5更强baseline不倒填Mayv1。未核artifact/复现。

[DC](SUP_DC_2605.14211_20261019.json)作者实核唯一v1May14 00:10:12Z→arxiv.content/findable/registeredMay15 02:06:43Z同北京May15；currentv5无具名纠错层复用R162。按拟采用四状态学习/恢复接口，暂拟**2+2+2=6**：新增跨运行/数据/标签producer的控制边界，但没有新的长期学习基础定理，原7仅未冻结暂拟的Durability3需收窄；此分数不降低具体gap的深入要求，实际必要域已足。

Actual AGENT-PLATFORM Ch84 374–389完整coupled policy×bank与费用/admission前段、438–455独立acceptor、920–939源码/双timescale，Ch83交接读足；旧文有两个策略/库共同演化，没有动作标签器与可更新进度sensor成为同一训练/暂停恢复事务的具体责任。拟coupled policy×bank完整费用反侧后→Skill三层admission前一段，不另归Ch77记忆检索或Ch27原始data。逐字PRE：

当适配会修改真正的动作policy时，卡住后的检索就不再只是增加context：还可能同时改变训练集、伪动作标签器与决定何时学习的进度sensor。一个[受限闭环分支](https://arxiv.org/html/2605.14211v1#S3)让各agent保留自己的短史与关键帧记忆、共享policy；任一agent长期未见新视觉cluster便暂停全部agent，更新cluster classifier，用真实动作轨迹适配IDM，再由IDM给检索视频标伪动作、训练policy后续跑。因此分类器、IDM、检索数据和policy都要保存对应版本与采集/生成关系，不能把换过进度定义后的“新关键时刻”当作同一测量，或让视觉相关性替伪动作正确性签字。离线IDM读取未来帧不使部署policy获得未来信息，动作标签仍依赖真实交互；某些按钮从像素不可区分，也不会因监督更多而自动可识别。所测两游戏的局部对照不证明真实任务进度、终身不遗忘或开放执行安全，停全部agent还引入同步阻塞。轨迹采集、全视频索引、cluster/IDM/policy训练、暂停与回归均付费；支持或标签失准时，冻结这组共同artifact、保留旧policy/进度定义及独立真实行为验收，而不由卡住信号直接批准新policy。<!-- source-family:SF-2026-ARXIV-2605-14211 -->


## A168 — 14201 MAPLE必要Source/date与具体Only提案

作者actual exactv1 §3/4/5.1–5.2/T1–3/§6、C/T8与G必要配置读足；旧A133决定域复用不当Source完成。固定ego、reactive-agent各planner与background motion consumer分工、T3ego-only→reactive/multi-planner有限对照保为新提案/所报局部结果，不因驾驶领域排。Self生成latent非真实transition，GRPO式无clip/KL不授标准完整PPO保证，Eq5正号加入φ(TTC)=max(0,TTCmax−TTC)与‘penalty’方向不一致，未据此发布训练recipe。主文background motionhead对G background GT playback、8H100/12+24+12ep/LR2e-4对G 8A100/3ep/LR1e-5/不同weightdecay，强matched性能归因未闭；源代码/项目直链未在已观察v1/current/metadata提供，不为还原全部训练无限搜repo。主T1 DS85.2弱DiffRefiner87.1，T3 SR67.5与主67.1不拼唯一配方。C H10080GB/batch1/10warmup+50synchronizedbatch/八head mean487.7ms/P90529.1ms属于rollout关闭单forward，不是免费/真实控制deadline；precision/完整trainingGPUh/生产并发SLO ND，全部latent/多planner/reward/预训SFT/RL及模拟回归费保。未核artifact/像素或复现，6=2+2+2受影响安全/训练身份深入。

[DC](SUP_DC_2605.14201_20261019.json)实际唯一v1May13 23:35:14Z至arxiv.content/findable/registeredMay15 02:06:29Z联合完整北京May15；currentv2仅后修/无具名纠错，不倒填。拟**仅报告**保角色分工/有限T3提案，当前不把配置冲突下强收益/安全结论作正面采用，也不反删候选。Actual MULTIMODAL-WORLD-MODELS Ch25 60–80完整support-limited predictor/policy-pair、161–165多主体直接干预vs条件响应、458–476模型hazard/actor训练人口，Ch24/26交接已读。现稿不含MAPLE算法；限定实际增量仍是已知latent rollout/多head与多主体reward的局部训练方案，未产生新的response支持/安全接受或净预算条件，不能只因新增planner名字就追加长期案例。若澄清background/训练配置/TTC方向并给匹配角色控制，足以改变现有模型/policy-pair选择时再开；本次不认证其强recipe或性能，待root具体Only独核。

## A169 — 14750 EVA新增visual事件必要Source/date与Ch72逐字PRE

精确v1引言明记这是DELMAN ACL2025文本早稿的journal扩展；旧ref23给作者/题名/pp11465–11481但无arxivID，不为旧全文版本史扩2025。Root定点2026现有README两个名字无命中只作有限去重，非所有别名无旧记录。作者只将visual-key提取/visual-token选择与VLM局部效用反侧作为May事件增量，不把text-only/MEMIT公式再计新基础。Actual §IV-A–C/Eq9–22、§V-A–D/TIII–VII、V-F/T VIII、V-G/IX及V-H/X必要域完整读；旧text-only大表不重所有攻击行。新增harm文字token跨prompt attention选visualkey，与textkey独立列，safevalue优化+benignKL，再soft leastsquares修改sharedLM downproj；token/feature相关不等唯一neuron因果，softEq20不等Eq18–19硬约束精确满足，改权重不是仅恶意输入生效的gate。Wikipedia covariance非全视觉旧能力无损证书。

TIV random/fixed零ASR伴MMVet10.4/12.1，attention55.5仍弱原56.9且gradient56.0更高；TX top2 .01非字面零、MMVet45.4，top3 .00/19.7，相比top1 .03/69.3呈安全效用张力不签少token全部风险隔离。QVLM MMMU48.2弱原49.9，InternMMStar67.5弱68.3。VF image/OCR分区各有交叉残留，不证明全视觉保留/完整语义解耦；adaptiveVLM仅LLaVA可稳定grad attack，.000→.125残留且迁移/构造攻击非所有自适应威胁。单A40/5run效率0.8h/VLM、forward1×不包含所有GPT4o文字/合成图/选层/协方差准备/独立attack费；precision/输入长度/batch/concurrency/SLO ND，未核artifact/攻击实现/复现，不写攻击recipe。6=2+2+2安全深入。

作者实际[DC](SUP_DC_2605.14750_20261019.json)唯一v1May14 12:16:10Z→arxiv.content/findable/registeredMay15 02:19:37Z完整北京May15；current唯一v1无具名警告，Comments只有IEEE TPAMI2026年份，无具名journalDOI/日期/更早正文。一次官方IEEE/computer域精确题名检索无结果只支持本次有界恢复，不声称全站无早稿；没有具体更早visual全文或重要当前纠错信号，不造无限first请求。旧文本事件与当前visual增量分开，按前述增量评分而非重新拥有旧textcore。

Actual PLATFORM-SECURITY Ch72完整data/Benign/optimizer安全身份、mask归因/repair与新context贡献前段/独立2509-03985marker及Grammar后段、Ch71/73交接已读。新差额是选输入visualkey不限制全上下文共享权重影响、硬/软更新/跨模态key权限分责；拟完整context贡献反侧+2509-03985 marker后→DecodingConstraint标题前一自然段，逐字PRE：

在多模态安全编辑中，输入token的选择也不等于参数更新的影响范围。一个[受限扩展分支](https://arxiv.org/html/2605.14750v1#S4)先以有害文字条件对视觉tokens的attention提出少量key，把文字key与视觉key作为独立列拟合拒绝value，再修改语言主干MLP的down-projection；这不是只在被选token或恶意请求上开启的runtime gate。Attention与probe只能提出相关位置，benign KL和旧key协方差也只是约束更新的代理，soft least-squares不继承理想硬约束或全部能力保持。有限消融中，随机/固定视觉位置可同时压低攻击成功与摧毁一般效用，选更多视觉keys也会显著损伤效用；按区域编辑的差异仍不识别唯一有害语义电路。已编辑模型上的有限自适应攻击还能恢复部分成功率，不能由静态零ASR宣永久安全。文字/图像制备、key/attention提取、value优化、矩阵更新、选层与独立攻防回归都付费，部署forward未加模块不等零准备。跨模态支持、误拒或效用不合格时，保留可信未改artifact、受控微调与外部行为/policy检查，不由少量keys或稀疏改参批准发布。<!-- source-family:SF-2026-ARXIV-2605-14750 -->

## A170 — 14379另一人必要Source/date与Ch27逐字PRE

复用R166首读；作者actual精确v1§4全/Al1、§6.1–6.2、A训练/搜索和C两个完整命题独核。独立代算原p=q=11/13时列回报均−9/13；offline uniform直接到player2节点的两隐藏状态各等概率，列回报0与−9/2，混入任意正β即打破原indifference。原动力学/局部observation不变不使条件belief保持，flag理论明确‘disjoint parameters’/理想NE，实际单shared actor/critic不能当无干扰有限PPO保证。β1评f1不外推未见root任务；不判所有起点增强有害或要求恢复全部proof。有限Kuhn/4card及构造travel对照、1000scriptgame、16Msteps与56grid/200Bayes最佳末exploitability选择及全费用沿R166，实际必要域确认，不新增硬件/精度/种子CI/生产SLO。未核artifact/复现。

实际[DC](SUP_DC_2605.14379_20261019.json)精确题名/唯一v1May14 05:00:52Z、arxiv.content/findable/registeredMay15 02:10:39Z联合完整北京May15；current唯一v1无警告沿R166。6=2+2+2具体belief/训练人口边界深入。Actual TRAIN-DATA Ch27 119–150完整数据权重/旧policy状态与乘法技能几何，Ch82 426–439完整behavioralbelief/人口均衡、Ch28开篇交接已读；现有‘数据权重改变优化几何’尚未承载中间simulator重启会绕过对手决策而改变同信息集posterior。拟唯一Ch27乘法技能完整段后→同语料训练/检索标题前单段；不是移去Ch82认证身份或新增博弈综述。逐字PRE：

在交互数据中，改变采样还可能改变参与者对同一observation的隐藏状态belief，而不只是增加难例的梯度权重。一个[受限self-play分支](https://arxiv.org/html/2605.14379v1#S4)从示教访问过的完整simulator state重启，同时只给各player原有局部observation；这可跨过长控制序列的探索瓶颈，却会绕过对手此前的选择，改变同一信息集的条件人口，因而可能连原博弈的均衡都改变。给每次episode附root-start或dataset-start标志，可显式分开两个训练任务；但其理想恢复结论要求两套条件策略可独立变化并已达到均衡，不保证共享网络的有限PPO训练无干扰，完全没有root样本时更不能认证root行为。全局reset能力也不授权policy读取隐藏信息。所测小博弈支持这项选择边界，不授现实LLM自博弈的通用加速；示教采集、reset、全部超参搜索、均衡求值与原root人口回归均付费。支持或belief改变无法核清时，保留原根分布、来源标志与独立原game验收，不将重启训练等同于原任务的无偏重采样。<!-- source-family:SF-2026-ARXIV-2605-14379 -->

## A171 — 14894另一人必要Source/date与具体Only提案

R167首读有效；作者actual精确v1§3.2/3.4/3.5、4.2/4.3/T1、4.5/T2/5及B2–B3/B7完整关键域独核。reference clean0与noisy同位置concat、训练subtitle mask重权、推理无mask不是无mask监督。B3 localLipschitz是Assumption，mask小不推常数小；B2边缘相同不推任意coupling逐点固定背景，且reference→target和训练noise→target并非同源。独立检验普通ODE dz/dt=z Lipschitz1，一步2z不等ez，仅反驳Lipschitz本身足够，未否定精确OT位移直路径可一跳。T2同1step比condition注入不检验one-step理论；T1 1/2/4step各有PSNR/FVD取舍。100kiter/8A80080GB/b32/381M LoRA、65frame1080p4s排视频I/O；GTmask baseline/20humanMOS协议、短<10frame与blur失败及所有scene/codec/chunk/训练成本保。20%cleanfirst训练与线上前chunk末帧反馈不证明无限稳定。未核实现/像素/复现。

实际[DC](SUP_DC_2605.14894_20261019.json)唯一v1May14 14:37:54Z、arxiv.content/findable/registeredMay15 02:23:06Z联合完整北京May15；currentv1无警告复用R167。5=2+1+2，强保证受影响域已深入。拟**仅报告**：有限subtitle no-mask部署/所报一跳结果仍保候选，但不采其‘theoretical guarantee’、局部mask→背景精确不变或无限稳定。ActualCh24 277–300完整global/local条件、ArtifactWorld clean/noisy/targetloss、cleanreference消费者及codec一次重建取舍，Ch25开篇已读；不冒现稿有SEDiT的focal loss/字幕实验。新增concat条件与局部maskloss/scenechunk的特定适配没有给这些接口新增有效可验证的一步/保持条件，经验表格保报告，不能用通用cleanreference原则绕争议正面写Books。若补齐真实源/配对coupling、一步误差/校准控制或足以改变现有消费者选择的质量/总费条件再开。若root判断强理论本身是本次中心采用命题，则应保中心争议而非把Only视理论验收；两层证据不改、不反删候选。

## A172 — 14845另一人必要Source/date与具体NC提案

R172首读有效；作者actual精确v1 III-A–E完整protocol/score、IV/TI–II与V–VI必要反侧另核。两verdict是同一JSON不同prefix，不是同prefix独立CoT开关，skilledT1 35.16→48.08与其他切片收益并存，不授CoT普遍有害或内部reasoning因果。Eq1 generatedtop1若Diff用1−p，只在二标签质量吸尽时对应另一类概率；独立举P(Same)=P(Diff)=.2/其他.6则1−P(Diff)=.8不等Same.2，标签可跨token、prefix不同亦保。不从EER排名或88/92自报confidence推真实身份概率/动力学解释，静态pressure图不保全部时间信息；6000/9520/12000pair非独立identity。API温度/seed是作者声明非真实服务执行证明；已读提示标签改变输入语境，不提供生物识别限制绕过/部署授权。全部渲染/生成/score/阈值/人审费保，未核代码/像素/复现。

实际[DC](SUP_DC_2605.14845_20261019.json)唯一v1May14 13:53:28Z、arxiv.content/findable/registeredMay15 02:21:52Z联合完整北京May15，current无警告沿R172；5=2+1+2标准。拟具体**已有覆盖**唯一PLATFORM-EVALUATION-SYSTEM Ch66 actual65–81完整score/ranking/calibration/release与pair不独立、自报数值/输入配对，以及885–916人口/scorer权限与Ch67交接已读：这些论点直接禁止把词概率映射、同串重判差额和EER当真实概率/因果，而非仅主题相似。本文新的切片反退与Eq1反例留报告，不冒现稿已有签名算法/该实验；其未增加可验证的新概率闭合或同条件推理干预条件，不为特定鉴别任务加案例。重开需真实标签事件概率/独立calibration与matched prefix/intervention足以修正现有判断。

## A173 — 14860另一人必要Source/date与Ch28逐字PRE

R173首读有效；作者actual精确v1§2.1–2.3/Eq2–10/Al1与§3完整必要域另核。缓存边界activation/downstream gradient、本地重算导数明确是approx blockgradient；仅起点一致，非重叠参数不取消前后依赖。Eq3每inner≤Δ/ell经三角界仅可给累计≤Δ，不能自动得正文≤Δd；W索引窗口内successful与‘最近ν次成功’不一，空史/零分母/zero-step不私修。历史/currentmaxratio只作为有条件proposal验收，后额外globalNTR本身需fresh gradient与真loss；不据旧cache宣全局新真值或由短时loss上升签收敛。小1.2M CNN/CIFAR10/四A100/b1000/ν100，115.88s对APTS169.14但Adam/SGD约40s，固定epoch/CPUtime原称不等matchedquality GPU净加速，全部globalpass/缓存/局部步/修正search/窗口与heldout费保；精度/独立seedCI/生产SLO未闭。未核实现/复现。

实际[DC](SUP_DC_2605.14860_20261019.json)唯一v1May14 14:06:51Z、arxiv.content/findable/registeredMay15 02:22:15Z联合完整北京May15，current无警告复用R173；5=2+1+2具体gap深入。Actual TRAIN-PRETRAINING Ch28 408–418完整Somax statefulstep/probe与outer KFAC、Ch27/29交接已读。已有‘loss-after控制信号绑定实际位移’，但未承载缓存局部producer与nonmonotone历史reference分责：历史可允许当前loss升，但不得代替当前候选freshloss。这是具体接受合同差额，不采用不闭recipe/普遍收敛，不为新optimizer名加例。拟Somax完整费用反侧后→curvature outer IHVP完整段前单段，逐字PRE：

局部分块更新还可以与全局验收使用不同的时效：先做一次完整前后传，缓存各块的输入activation与下游梯度，让各块独立走若干受限inner steps后再合并。离开原参数点后，缓存梯度只定义局部surrogate，不是新参数处的全网真导数；参数块不重叠也不消除前向依赖。一条[受限非单调分支](https://arxiv.org/html/2605.14860v1#S2)因此用真实候选loss与当前/近期成功迭代的预测下降比分别检查合并proposal，允许暂时高于当前loss的候选，再另做全局trust-region修正。采用这类分支时，缓存的线性化版本、成功历史的索引窗口、参考loss和累计预测下降都须与实际位移一起保存；历史参考不是旧probe替当前候选签字，也不由暂时接受上升推出收敛或泛化保证。原文局部步长累计界与窗口文字存在未闭口径，不照搬为完整recipe。所测小CNN中较原分块基线省时，仍比Adam/SGD每epoch昂贵，未给大模型等质量净加速；缓存、全部局部步、全局重算、候选检查与修正搜索均付费。代理失准、历史语义或总费不合时，保留全网新梯度、单调验收或成熟一阶更新，不让较少拒绝本身批准新checkpoint。<!-- source-family:SF-2026-ARXIV-2605-14860 -->

## A174 — 14746另一人必要Source/date与Ch72逐字PRE

R168首读有效；作者actual精确v1§3.1–3.3/3.5全/Al1、D完整CRC与E2/E4必要配置另核，不重B全部证明。全HTML首取tool中段截断已识别，所用方法/D/E必要段均完整返回，未冒全部正文二读。Oracle base-continuation value/二值terminal reward/每可达prefixZ>0才授理想dominance/floor；learnedprobe没有oracle martingale资格。D控制base-safe trajectory上minscore越线事件的期望，非干预后新policy有害率/逐prompt/OOD；固定估计器与交换人口不能由同judge高AUC补造。Al1有限K全失败仍maxscore，独立算失败概率(1−Zhat)^K，若Zhat<1则正，wholealgorithm不等严格truncated support；不判所有过滤收益无效。E4PKU helpfulness无优势也保，cosine/intentcompliance不认证真实安全/事实。

实际[DC](SUP_DC_2605.14746_20261019.json)唯一v1May14 12:13:08Z、arxiv.content/findable/registeredMay15 02:19:31Z联合完整北京May15；currentv2无具名警告复用R168，不倒填July。6=2+2+2安全深入，所有probe训练/生成label/holdout/候选重采与独立回归费保，未核artifact/复现。Actual PLATFORM-SECURITY Ch72 43–55完整参数影响反侧/grammar改变support与fallback、后PrivacyFilter/Ch71/73交接已读；尚未承载‘阈值校准保护base-safe人口不等新policy安全floor，有限失败fallback重开support’的具体三方界。拟完整grammar费用/回退段与独立2606-11817marker后→单次文本脱敏完整段前单段，不写攻击recipe。逐字PRE：

安全过滤还须分开“少改原本安全的输出”和“干预后真的安全”。一条[受限value-filter分支](https://arxiv.org/html/2605.14746v1#S3)保留超过阈值的next-token候选，再按原policy概率重归一；它与对全部token指数重权不同，但理想安全单调/floor依赖真实base-continuation value及每个可达prefix有非空支持，不能直接授给learned probe。对base生成且按明示judge规则判安全的完整轨迹，可用沿途最小probe分数校准阈值，在固定估计器与交换人口下限制误干预这类轨迹的期望；这不控制新policy的真实有害率、每个prompt风险或域移安全。部署有限重采样还有另一接口：所有候选都未过线时仍取最高分，会离开阈值过滤的支持，不能再继承hard floor。判安全的标签本身也可能错，cosine接近原输出和更遵从意图都不认证事实/安全质量。训练probe、生成与标注校准轨迹、全部候选forward/重采和独立效用安全回归均付费；阈值附近失准、支持为空或费用超界时，应保留可信外部policy检查、拒绝/人工路径与原已验收解码，不由一个误干预预算批准危险输出。<!-- source-family:SF-2026-ARXIV-2605-14746 -->

## A175 — 14846另一人必要Source/date与具体Only提案

R169首读有效；作者actual精确v1§5.1–5.3/Al1、6完整收敛叙述与7/T3/8必要域另核。QK二次difference-of-convex、softmax LSE切线上界/互补下界、attention×V再DC/单纯形外包消费者是具体新求解提案，不因水箱领域删除。Eq14末P1不是前述P、Lemma1 j≠1与证明j≠i不一、stage3矩阵norm及VK/WV字面身份未闭，故不照全recipe；单调有界J只给标量变化趋0，不独立推出全部Z参数收敛/单纯形singleton/localoptimal，未核引用资格则不认证强proof。模型内constraints亦不签真实有误差系统recursive safety。T3平均.075/1.857/5.166s和max.203/3.229/9.421s随N20/30/40增，SLSQP更快但误差较高；仅两水箱fixed单predictor、未授多头/LLM任意迁移。所有预测器训练/逐步DC/顶点/凸求解/真实回归费保，必要域hardware/precision/独立seed/全训练搜索与harddeadline未闭；未核代码/复现。

实际[DC](SUP_DC_2605.14846_20261019.json)唯一v1May14 13:54:54Z、arxiv.content/findable/registeredMay15 02:21:53Z联合完整北京May15；currentv2无警告复用R169，不倒填July。5=2+1+2标准/强claim受影响域深入。拟**仅报告**保三组件凸界/有限求解选择，不采完整收敛与真实递归可行保证。Actual Ch25 472–492完整RaWMPC/支持/代理安全、前后向梯度分工，Ch14通用attention并非本control消费者，Ch24/26交接已读；不冒现稿已有DC求解或这两水箱结果。有限内部凸化是单predictor的局部优化替代，未提供新的真实模型误差/接受或净deadline条件，现有边界未被改变，不仅为具体solver再追加案例。重开需字面接口/定理资格澄清，或新的可验证模型误差/多头消费者与匹配质量/总费证据实质改变选择；Only不认证未闭理论。

## A176 — 15026另一人必要Source/date与Ch84逐字PRE

R174首读有效；作者normal PDF内存fetch一次TLS失败后，web正常打开精确v1实际18页；只actual§4.1–4.5/§5 typed执行与恢复、§6.1/6.4–6.6和Table2必要域另核，不重所有主文/图片。PDF SemaTune四作者与currentabs/DC TuxBot三作者明确分开，以同ID精确v1采用，不把July名字/作者倒填May。Instant记录随Reasoning commit清理，但persistentReasoning历史继续增长，非context恒定；typed/range/selecteddependencies与hostlock只是受限actuation，不证明完整系统原子回滚。单primaryapp/session，秒级调参不等内核fastpath；稳定期ST停更新而MLOS继续、11项subset singleReasoning89.7%高于dual87.2%但API费更高，16.9%坏窗口、41knob Trim更高均保，不采无坏窗口/alwaysbest/语义唯一因果。R174全部配置/完整成本有效层复用，不为还原所有Linux行为扩代码，未核artifact/实机或复现。

作者新实际[DC原字段投影](SUP_DC_2605.15026_20261019.json)精确DOI/currenttitle与唯一v1May14 16:25:32Z、arxiv.content/findable/registeredMay15 02:26:22Z，全部可能界同北京May15。Current无警告沿R174，v2只元数据说明不审全版本史。6=2+2+2安全/接口深入。Actual AGENT-PLATFORM Ch84 930–942完整源码proposal/fastprompt-vs-slowcode/回退，Ch83交接已读；现有双timescale分风险代码晋级，不是两model共用同typedknob执行、短史被慢commit消费与旧配置/真实hoststate恢复分责。拟完整2605-23019双timescale费用/marker后→‘何时不需要Agent’标题前单段，原段保持。逐字PRE：

双时标也可以用于同一运行中的配置调优，而不改变prompt或控制代码。一个[受限host-side分支](https://arxiv.org/pdf/2605.15026v1)让快环读取短期action–measurement记录，慢环读取更长历史并提出策略；慢结果commit后，已消费的快环记录退出后续快环context，慢历史继续积累。两环都只能提出同一声明knob集合内的改动，真正写入仍由host校验类型、范围与部分依赖、持锁执行并记录结果；跨run检索摘要只作可被新量测推翻的软先验。采用这种交接时，应重核异步提案所依据的配置与量测是否仍有效，不能由慢模型更强就跳过执行验收。恢复旧knob值也不等于回滚已形成的queue、cache或整机状态，合法数值更不证明组合策略安全。所测单应用、秒级稳态调优仍有差于默认的窗口，较低模型调用费不代表单慢环质量必差或总主机费用更低。遥测、历史/检索、全部模型调用、失败探索及恢复验证均付费；负载快速变动、共享应用干扰或恢复不可验时，保留静态已验配置、传统controller与人工/外部SLO检查，不把这条慢速调参链当kernel fastpath或无坏窗口保证。<!-- source-family:SF-2026-ARXIV-2605-15026 -->

## A177 — 15082另一人必要Source/date与Ch5逐字PRE

R175必要Source/短谱证明有效复用；作者actual精确v1§3.1–3.2完整目标/Ass1–3/Th2/Lemma3/Cor4、§4/Eq17–22与§5数值协议独核，未第三遍95页长proof。最初全HTML工具中段截断和仅命中toc的短proof字符串提取都已识别，未把空匹配称正文不可得；后web原HTML正常可读，按root实际短谱proof层复用，作者不冒E/F短proof已二次逐字读。独立检查低degree目标M与UᵀΣpU扰动：Σp正谱隙/weakcoherence和signal/noise相对误差必须保，不能从高degree预测残差大推梯度方向全无用，亦不能当低degree没有某方向仍能恢复。Boolean x_i²=1先取multilinear与指定kernel/regularization/独立Gaussian噪声、r/degree固定/高维渐近均保。式22明确Conjecture，metric ηI/归一化不把其它方向硬删；Gaussian/sparseU经验不继承Boolean/coherence定理。n×n核求解/gradientAGOP/d×d谱分解及反复拟合全费，未核代码/复现/全部长proof，不授真实LLM语义或净加速。

实际[DC](SUP_DC_2605.15082_20261019.json)精确题名/唯一v1May14 17:05:30Z、arxiv.content/findable/registeredMay15 02:27:42Z联合完整北京May15；current无警告复用R175。6=2+1+3限‘表示先于准确预测’的条件化认知差额，不给RFM猜想加分，具体gap深入。Actual WORLDVIEW-REPRESENTATION Ch5 172–202完整featuregap/AGOPpartition停滞/accuracy非正确feature与agreement段、Ch4/6开篇交接已读。已有‘高accuracy不能证明正确feature’和kernelpartition可失败，尚未承载其反向边界：低准确预测不排除完整任务方向已恢复，恢复成立依低degree全方向/谱隙。拟完整2604-00316 AGOPpartition反侧后→‘因此，模型学到了正确特征…’完整段前单段，非重抄一般表示可读性。逐字PRE：

反过来，预测误差仍大也不能直接证明尚未学到任务方向。一个[受限kernel回归构造](https://arxiv.org/html/2605.15082v1#S3)先拟合预测器，再对其输入梯度外积取经验平均、读出主特征子空间：即使样本量只足以学到目标的低degree部分，高degree残差仍大，只要低degree梯度已经含全部相关方向、存在足够正谱隙且方向不太集中于少数输入坐标，子空间仍可先被恢复。这里的保证限均匀Boolean输入、固定秩多项式multi-index目标与指定kernel/正则及噪声条件，必须先按Boolean关系取多线性代表；它不是任意深网已学到正确语义的证明，缺少某个方向时更不能靠同一谱定理补出。恢复方向、拟合完整目标和最终任务质量应分别验收；用该梯度矩阵更新kernel metric后，下一轮预测样本复杂度的进一步改善仍是原文明确Conjecture，而非端到端RFM保证。核矩阵求解、梯度统计、谱分解和每轮重拟合都付费；谱隙、支持或独立质量不合时保留原预测器、直接任务测试与更窄表示诊断，不由较好子空间角度签发能力或净加速。<!-- source-family:SF-2026-ARXIV-2605-15082 -->

## A178 — 15026追加actual owner对照后收窄为具体Only

A176必要Source/date/反侧保持有效，PRE保留为提出过的稿而未写入。作者再实际读取Ch84 588–612 observation与action时钟/receipt权限、661–687 resume外部状态重核、1022–1037版本化harness与每次action授权，加上930–942风险双timescale。对照后，A176的‘异步提案须重核当前状态、旧knob不等外部状态恢复’已由这些具体合同承载；SemaTune实际新实证与Instant短史被Reasoning消费只是同typedactuator的局部context管理组合，并未新增可验证的state/version接受或恢复保证。不能用自己提出而论文未建立的freshness协议，反向制造本论文Books差额。因此最终拟**6分深入完成/仅报告**，不称该OS算法已有覆盖、不缩候选或降分；保双环API费/质量取舍、单app/坏窗口与typed控制有限增量。重开需新的contextcommit/异步版本冲突或真实恢复协议与受控证据实质改变这些既有判断，非只因又有一个双环名字。A177 AGOP的反向条件认知差额仍独立有效，待root逐字PRE。

## A179 — 有界漏斗闭合与DAY前机械检查

R176/177非I处置与R178四真实POST、R180最终15026Only、R181 AGOP真实POST均已消费。当前105新增候选确定：53实际I、24具体Only、18具体NC、10中心争议；原184完整题摘/官方核心＝73唯一贡献关闭＋4具名更早全文窗外＋105候选＋14553/13866两日期资格外部，普通Source/Books0、全部窄位释放。原Charon另保整行，合106Report家族；不把窄位授权计写入、不将潜力全转全文、不新增发现/旧日归属。

实际README六节已归并，14来源范围/停止/缺口自包含；arxiv相关题名/同义主题按A39/40停止，Google目标publication slice及两日期资格精确隔离，不授完整Coverage/Evidence/无遗漏。完成前仍待root独立DAY和保存态FINAL。V3通过；106唯一表行＝53I＋24Only＋19NC含原Charon＋10D，单GFM表；199本地引用均存在；原Charon整行唯一、原小时window与2476字符旧§4连续精确保留。限定working README/SUP/approvedBooks diff-check通过，approvedBooks cached检查通过；本日cached来源检查仅冻结原件baseline第80行EOF空行警告（原同内容保护），不改共享index或trim原件求绿。本作者未stage/commit/push。

## A180 — R182 DAY通过后的完成态保存

Root实际R182整日独核通过已消费，105新增/53实际I＋24Only＋18NC＋10D、73C/4O/2资格外部及所有有限覆盖/旧层保护不变。README于2026-10-19T16:15:28+08:00将当前状态完成、§1/5/6同步真实R182，不预写保存态FINAL。没有新增发现/研究/Books或更改共享index；只交root最小完成态读回，不接下日。

## A181 — R183完成态FINAL既成同步

Root R183已实际完成最小保存态读回、V3/限定working复跑并正式接纳本日。只同步此既成指向，105新增与全部边界不变；本日无未执行窄写/待POST，任务结束，不接其他日期。
