# 2026-01-24 来源补查的有限入口与必要证据

检查：2026-10-08，北京时间。只补 Jan23 自然日遗漏；原74候选/窗口/评分/§4连续正文保存于 `baseline-before-supplement-20261008.md`。此文件是原始筛选和证据定位，不是第二份完成账本。

下文“潜在owner/待差额”保留当时的审阅假设；最终采用命题与具体处置以本日README §3/§4为准。CASL的原理已有Ch5实际论点，新EPR/topk只是受限诊断，最终仅报告；Panther和15528的必要重开/安全反侧已由非作者独立核定贡献前关闭。六处Books修改均由root授具体窄锁、PRE及实际正文/完整邻接/自身末注POST后落实，不从本文件的早期假设授Books或日级完成。

## 入口与停止

`topic-0..3.json` 是四个有限主题 API，submission buffer `202601211900..202601221900`，start=0/max_results=150，升序，返回119/17/28/12且各等于total，故没有下一页。并集144身份只是发现线索；与原AB1/精确题摘/候选定点去重后，只读可能新增主线贡献的完整题摘，不把144或月目录变为全文队列。API summary可能是v2/v3，不能授予本次v1贡献；拟采用项均另读精确v1。官方LG/CL月列表 `official-*-valid.json` 只核身份与相关标题，show2000不等于全月读完，不支持日期。错误旧YYMM路径404在 `official-*-month.json` 保留，不作成功覆盖。

新增八ID及loop URL在2026现有Daily作一次定点文本去重（不读其他日全报告、排除Weekly）：八ID只本日命中；loop在Jan23 README L380仅作为Jan23真实公开、窗外不处理的恢复线索，非已审重复事件。本日仍需处理，不挪旧归属。

14个Daily入口实际执行见同名JSON：OpenAI RSS1254记录中Jan23只发现Codex loop（Fri23Jan12GMT），官方正文日期相符；Anthropic仅当前10条和Jan23官方限定搜索，历史段仍缺；Google Jan2026九日期项完整，Jan23 GIST系2405.18754同贡献重述，DeepMind当前页/日期检索缺历史段；Meta原入口空正文；Qwen旧blog与qwen.ai/research动态正文未恢复历史段；DeepSeek changelog Apr24→Dec1连续段没有Jan23release；Moonshot blog停Nov2025，不能授Jan23完整；Hunyuan原Research空正文，一次隐藏browser30秒timeout（未观察渲染列表），不称全列表；ZAI Research这次成功15条，Feb2→Jan19及release Feb3→Jan19连续段无Jan23；Seed blog十条Jan27→Dec2，papers当前18/242只是库存，历史段未恢复；ERNIE blog10条Jan29→Jan15无Jan23；MiMo八paper Feb3→Jan8无Jan23，未定时blog仍缺；MiniMax普通中文13条Jan28→Dec23无Jan23，AgentTechBlog仅当前单篇无历史列表。没有扫描Weekly组或90天catchup。官方日期搜索未命中仅作有限补检，不能替代原目录。

## 公开日期而非Submitted

`arxiv-availability.json` 官方L188–208：moderation可延迟，final identifier/DOI只能在宣布时分配；Wed14:00→Thu14:00 EST提交最早Thu20:00宣布（Jan23北京时间）。拟采用八v1提交均在该buffer；官方精确v1身份在 `abs-ID.json`，最终ID在官方月列表和DataCite同期deposit存在；对应 `date-ID.json` 初次registered均Jan23UTC02:37–02:56，即北京时间Jan23。正常排程给最早公开日下界，宣布后才生成的final-ID同期deposit给上界，联合界定Jan23；registered/Updated单独不当public字段、不追分钟。API最新version不冒充初版，也不比较全部版本。

16238的v1Submitted Jan21、v1Updated/初次deposit Jan26只给Jan23→Jan26跨边界公开范围。未得到官方历史公告或更早官方同稿公开时间前隔离，不武断写Jan26首次public。需该final-ID首次官方公告日期，或官方项目初版正文公开日；不用于候选或Books。所有新增事件页没有当下可见撤回/勘误信号，不遍历全版本史。

## 准入与具体关闭

拟采用八论文：15380、15417、15441、15500、15711、16034、16046、16175；另官方Codex loop一族。每项在下列核心证据中收窄。根审已读最初8拟与5代表题摘，其中16238因日期未决隔离；15711与loop后补校准。Panther15473重开关键BERT/sketch必要段后才能关闭。

代表关闭（完整题摘，不因标题/规模/经典理论拒绝）：15406 HFR是跨光谱人脸leaderboard与MLLM组合，未新增可定位的foundation接口失效条件；15633 RT FRNN只改善物理粒子simulation nearest-neighbor，没有当前LLM系统条件改变，AI-for-Science暂缓；15872 PF-D2M将视频而非pose送入dance生成并progressive训练，摘要不建立新失效边界，成熟recipe的领域SOTA不足；16139 KRR intrinsic-dimension研究不是因经典理论拒，是题摘尚未说明改变哪个当前系统判断。15453 DevPrompt的CLIPprompt/TopKMIL/Gaussian距离为异常检测recipe；15551 ALIGNAgent是教育skill估计＋推荐流水线；15630 UALM是healthcare控制面概念/标准组合；15673 CARD是推荐场景的diffusion兴趣重加权；15687 FARM是schema/input对齐的多Agent function generation，未给新执行失败/可靠性条件；均不把应用组合/主线词汇当贡献。

15528安全信号另读 `core-15528-admission.json` §4–5：manual prompt guard＋现有GenTelshield，两类500query从GenTel构造，三proprietary/API模型，k3s与baremetal的网络/温启动不控制；99%不是不可泄漏/跨租户证书。未建立新机制或可靠性条件，仅既有防御组合的受限案例，关闭而不采用安全保证。

15722完整题摘是fed-GNN图分类：传本地diffusion生成器以合成图降低交互轮数，三轮不等constant bytes；未建立大模型训练/表示的具体改变，仍是领域GNN配方。16169完整题摘确认是电子Hamiltonian量子diagonalization的OpenMP/GPU实现，属于暂缓的Science，100x/node不改变LLM机制，范围前关闭。15891 API已是v4不能给v1controlled-objective贡献；`abs-15891-admission.json`精确v1完整题摘实际恢复：masked-region latent prediction的I-JEPA配方用于CXR，只有领域下游优于Rad-DINO，未说明新的预训练机制或可比objective失效边界。此初版在贡献前关闭，不将v4后来增加的controlled-objective说明搬入Jan23，也不因medical领域本身拒绝。

15473 Panther必要重开 `core-15473.json` L69–179：SKLinear/SKConv由2017sketch低秩和Performer组成，10trial Optuna按copied layer output threshold选rank/term，CUDA WMMA/ATen执行已读。BERTbaseuncased/WikiText仅MLM loss4.601vs4.594与最高75%size，没有绑定具体sketch rank/num_terms、matched训练/质量/参数预算的新边界；MHA内存比较Performer对PyTorchMHA而非Flash。不是因经典库拒绝，而是未确认可比质量–资源新条件；成熟集成未改变项目判断，核心读后关闭。

## 必要核心与反侧

### 15380 — You Need Better Attention Priors

exact-v1 `core-15380.json` §3L76–132、§4L132–216、§6L260–302、AppendixGL850–881。行独立EOT含KL(p||π)，正prior产生softmax(s/τ+logπ)，不是双边balanced Sinkhorn。有限Fourier relative bias＋key-only default可以用位置Q/K保留子空间因式分解，与缩放后的content QK相加，从而仍一次未改FlashAttention；固定head维时posdim占用content维，位置预处理不免费，不能宣称零成本或任意bias可因式分解。C4 125M/4Btokens、ctx2048，passkey训练1024等有限对照支持条件分支，不授无限length/统一sink因果。收益不照录biologyGPU数字；硬件/统计重复Not Disclosed。潜在owner MODEL-SELF-ATTENTION现sink段L260–288不承载显式log-prior与QK保留子空间，已发root窄锁/PRE请求。

### 15417 — Ambient Dataloops

exact-v1 `core-15417.json` §2–3L96–175、§5L237–246/355–365、有关附录L1190–1224。每轮从原D0重建，不递归把上一轮合成当clean；上一模型把每样本ti降到ti/2^l，仍标残余corruption，下一轮只在t>该ti作ambient学习。降低已知corruption不是创造信息，不能凭selfloop断言永不collapse。CIFAR10 90%blur/JPEG、10%clean，对all-data/filter/loop0支持局部收益但按FID饱和挑模型，重建＋finetune总compute未matched；太快/太慢restoration都会坏（Fig3），数据多时fresh数据仍更好。TRAIN-DATA现递归语料段L384起区分corpus/parameter/human anchor/freshness；尚未承载“同D0逐轮再估＋残余noise eligibility”的具体接口。

### 15441 — CASL

exact-v1 `core-15441.json` §3–4L142–211、EPRL391–408、评价L409–450、对齐L495–497、hyperparamsL537–550、App9.1L1213–1239。SAE sparse reconstruction本身不授human concepts；冻结encoder，用CLIPsemantic＋L1拟合线性concept mapping，再只干预topk潜方向；目标classifier logit变化/非目标平均变化的EPR是相对指标。32图/属性，冻结U-Net四datasets，top1一次DDIM injection；重构baseline不是identity，supervised1000图/概念。App不同classifier同图EPR显著变化，标签不稳不可用，k>1编辑更易纠缠；§7固定t0/scale32与主文50timesteps/scale128不同，不能复现认证。可采用“稀疏≠语义命名，受监督对齐＋目标/副作用分项验证”，不授真正独立因果因素或通用EPR绝对值；owner候选MULTIMODAL-GENERATIVE-PARADIGMS的controlled-editing分支，待root定具体覆盖/差额。

### 15500 — Low-Dimensional Adaptation of Rectified Flow

exact-v1 `core-15500.json` §4.1/4.3/4.4L202–249、U-shapedgrid/Th4.1L250–342、§5learnedvelocity反侧。低intrinsic covering number＋bounded support并不直接授实际速度误差；deterministic另需均方velocity、Jacobian Frobenius/stepweightedoperator≤1/8、Jacobian trace²与gradtrace等条件。U形网格两端geometric，TV结论在倒数第二个blurredendpoint；manifold target的精确终点与全维近似TV=1，不写exacttarget保证。stochastic rescaledDDPM/timechange可不需这些高阶导数，但仍需mean-squarevelocity error；learneddrift高维/端点误差可变坏，不能推stochastic天然更好。4.4(c)εH定义后不等式写εJ2，非零均值Gaussian展示drift公式少μ项，相关完整定理/实验因果隔离，不擅改公式。可采用“intrinsic sampler复杂度有学习误差/导数/模糊终点前提”，FLUX只qualitativeprompt不是controlledcost优势。

### 15711 — Three-Tier Evaluation of VLMs for Attribute Prediction

exact-v1 `core-15711.json` §3L123–134、§4L245–299、§5L300–352、§6/Table4L431–528、limitationsL677–682。NA合并不存在/不可见/不适用/无法确定，不是通用abstention。T1所有class；T2二元NA；T3筛gold≠NA但预测仍可NA。GeminiPro同模型T1/T2/T3=64.0/34.1/65.4，Flash59.9/22.0/70.8，不能拼34与71为同模型。DeepFashion5000图18属性、14安全屏蔽图对所有模型剔除（有效4986）、单zero-shotprompt，两商业家族，弱frozenlinearbaseline，模型版本/硬件Not Disclosed；cost不授currentpricing。设计差额是EvalSpec拆“能否形成属性判断”与“判断后选值”，仍分开schema与semantics；绝对分数/泛化与混杂NA标签不外推。

### 16034 — Universal Refusal Circuits

exact-v1 `core-16034.json` §4–6L125–228、protocolL240–275、controlsL356–388、limitsL398–412。所谓universality是受测family在固定20conceptbasis、目标只benign/concept的预算下transfer成立，不是全部模型真理；sharedlatent线性是guiding假设，whitebox＋registry覆盖依赖。原方向并不能跨维直接复制，concept coefficients在目标basis重建、layer Gram/DTW对齐，weight-SVD是启发式preserveguard；wronglayer/no-guard控制造成capability drift。dense→MoE只改sharedattention，不等expert级复现；singlefrozenLLMjudge/300harmfulprobes与benignPPL、Math/Code不认证fullsafety/longtail能力。仅安全审计采用transfer/target-budget/guard失效条件，不写guardrailbypassrecipe或部署推荐。owner PLATFORM-SECURITY需定位现论点而非仅主题匹配。

### 16046 — DextER

exact-v1 `core-16046.json` §3L119–189、configL193–206、DexGYSprotocolL207–227、matchedECoT消融L334–440、steerL572–585、limitsL613–620、App6.4L1012–1038。contact link＋3Dposition tokens先于28dimgrasp，训练MuJoCo标注、PartField＋Qwen2.5-0.5B、bf16/8A6000/batch64；部分contactprefix可引导完成，提供比文本CoT更可检查的动作condition。w/oECoT67.14→62.37simulation-success、P-FID.20→.30，非独立语言推理因果；1cmcontactpositionaccuracy只对预测grasp的FK一致，不是sensorcontact真值。DexGYS稳定判据至少六gravity中一种100steps、penetration≤.1cm，Dexonomy六force判据不同，不能合并。新taxonomy仍摇晃，AR误差累积/实时未证。MULTIMODAL-EMBODIED-VLA当前显式pose/flow/token接口已有，但未定位contactprefix→grasp单独接口；潜在窄owner分支不改变真实controller提交权。

### 16175 — Learning to Discover at Test Time

exact-v1 `core-16175.json` §3L236–303、kernelL418–428、ablationL665–707、futureL755–756。单verifiableproblem要一次beststate，不是generalpolicy平均reward；adaptiveentropic训练＋max-childPUCT复用结合，持续更新LoRArank32/gpt-oss120B，50steps×512rollouts；frozen搜索/平均RL/no-reuse对照有matchedsampling，未matchedtotaltraincompute。Table8 H100 TriMul best1203.1vs无TTT2060.7、expected1985.67等只是该run best，不授分布性支配。Fig4写50×512=256000算术错误，正确25600，同budget次数由实现段支持，不采错分母。训练H100/最终别卡，MLA训练H200而声称MI300x迁移，MLA主要torch.compile而非Triton；部分officialleaderboard因infra未提交，不冒独立验证。只用GPU/algorithm支持系统主线，不扩Math/biology。代价包括LoRA训练、重复执行/远端评测与存档，rewardoracle可信与连续reward前提；不能代替普通reusablepolicy训练或binary/nonverifiabletask保证。潜在TRAIN-PPO/GRPO目标边界待root定位。

### OpenAI — Unrolling the Codex agent loop

事件Jan23官方RSS与正文，正文通过web原站读取（directfetch403不等正文缺失）。必要section `Building the initial prompt` 与 `Performance considerations`：该快照sandbox只包shell，MCP须自管guardrail；全input重新发送以stateless/ZDR，encrypted_content允许保留reasoning但不授可见reasoning文本；cache仅exactprefix、tool/image/order均需相同，原MCP顺序不稳实为cachemiss原因，config变化appendmessages而不改历史前缀。AGENT-CONTEXT L415–434已经有tool-schema抖动、canonicalprefix与cacheidentity合同，AGENT-MCP L153–179已有执行/授权不由协议授予；可为已有覆盖的官方实现验证，不造一般loop新知识或全栈security保证，不写当前实现/价格承诺。
