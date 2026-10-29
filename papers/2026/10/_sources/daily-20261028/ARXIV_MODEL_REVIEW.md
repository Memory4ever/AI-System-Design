# 模型训练推理：实际判断与精确续点

窗口Oct27 BJT；root作者，唯一非writer live1028_review。导航不是候选分母；完整题摘AB/AB2两文件可复用，尚未全日筛选/审阅完成。

## 首四项必要证据与Books提案

准入已独核：35556为2+2+2=6，35544为1+2+2=5，33360为2+2+2=6，34427为3+2+2=7。root实际打开精确v1 HTML核心方法、评价及相关限制，不称复现。

- [35556 LoopFold](https://arxiv.org/html/2610.35556v1)：§3 predictor由首轮增量外推同前缀不同深度，corrector按前轮输入变化修正，训练仅最终next-token。§4三种配平不混用，低compute档vanilla仍胜；component ablation同13backbone评估，去correction损失较大；§5增加FLOPs和KV，cache共享省容量但更慢。目标不是重现顺序精确轨迹。提案Ch18“状态进入循环后”新增自然段：循环深度不等串行深度；以可训练预测/校正换额外并行算量，不说免费或普遍加速。硬件型号未见，不报告46%数字为跨平台保证。
- [35544 StateLoop](https://arxiv.org/html/2610.35544v1)：§3主干直接路径外另保per-token loop-state，g旧+(1−g)新投影后反馈，identity版仅当前token跨loop暂存，非全token永久KV。§4同训练tokens/参数对照及§5 reset/GRU/feedback消融支持保留state增量，但reset支路亦有益，不能把全部收益归跨loop记忆；§4.4状态支路加开销，不声明减少原loopcache。提案Ch18上述段之前补独立工作state与hidden更新分责，保门控/投影/训练成本。
- [33360 Shared KV](https://arxiv.org/html/2610.33360v1)：§2.2两遍训练由第一遍donor供缓存，served continuation递归生产donor，§2.3末训练预算的donor一致性仅在第一遍histories对齐。§3 FineWeb/BF16/8H100与teacher-forced 2048prompt+512targets；§4/6两seed/disjoint docs验证有限修复，非采样生成；cache数≠端到端VRAM/latency，batch停止并未跳过计算，部分width/batch更慢。提案Ch19模型定义的depth sharing后加入训练producer与部署recursive producer差额/辅助修复，不能把权重共享当cache等价。
- [34427 ScaleRLT](https://arxiv.org/html/2610.34427v1)：§2–6 rollout浅/深readout延后batch，denselearner reduction不一致；no-grad同schedule/kernel/batch replay供应数值、dense pass供应梯度，改变batch或backend失去bitwise；只在rollout相同weights下，单batch单step。§7.4原生全深readout质量更高、time-to-quality更好；bf16 dense ungated同质量，故不把strict gate通过当准确率收益。梯度是数值精度级可比而非等价。提案Ch33 rollout identity/实现一致性处补前向logprob值与梯度路径分责，额外replay费用及原生策略反侧放附近。

日期：35556 v1 Oct26 14:58:11Z、35544 Oct26 14:53:49Z，周一公告最早为BJT Oct27；同精确arxiv DOI state=findable，registered分别Oct27 04:51:57Z/04:51:41Z。34427 v1 Oct25 16:35:30Z，周末下一公告最早同日；registered Oct27 04:26:09Z。结合官方日段和唯一v1，区间落Oct27，不把registered改称实际发布时间。33360 v1 Oct23 23:12:12Z亦为周末批，但DataCite首请求timeout，尚待合法定点恢复；不把单次失败改成终态。

33360补查：DataCite精确DOI已成功返回findable，registered=`2026-10-27T04:02:02Z`，唯一v1 Friday23 cutoff后+官方Oct27段联合限定Oct27，原timeout解除。root实际补读§2.2–2.3/4.3完整必要及两侧Ch19 depth-sharing；真实保存本候选自然段+本人note，待唯一reader actualPOST，不重复插入。34427/35544/35556三项root实际SAVE已由reader核完整正文/两侧/note通过，I生效。

## 后续决定事实/必要实际阅读（尚未独核和Books落实）

- 35518 S3AC：已定点精确v1 §3.3–3.4，决定事实补齐。Value head小尺度初始化+head大梯度主导global clip缩小backbone梯度的实际边界；混合强弱policy轨迹补长正确路径覆盖；critic初始值转p，与衰减success/attempt counts融合，positive-floor接受中等难度prompt是在rollout前而非生成后丢组。可按2+2+2=6送reader，不把GAE/CISPO或5倍LR当普遍新定律；实验必要/Books尚未审。
- 33005 OpenESM：实际精确v1 §3.1–3.2读到固定参数、latent负能量梯度更新后由独立token head读出；所谓MCMC省了噪声，不能称后验精确采样。训练按position mask并行latent steering尚未完整读完，需确认相对既有energy-based Transformer的实际增量；不因26tasks/开源直接准入，不把未完当排除。
- 34566 ED必要已读精确v1 §3–6及§5.3–5.5决定反侧：SR量化residual累积到flip阈值再减去真实更新；grid必须包含阈值，普通deterministic rounding会停，单次步幅cap去部分avalanche。等预算saturating integer latent可同样好，不声称全新表示必胜；4bit长期variance/未诊断divergence并未因cap全解除，FP embeddings/head/Adam与activation保留。单GPU小模型、部分single-run、best validation/重启选择协议，不外推LLM训练速度/完整VRAM。CPU275MB是post-setup增量cap、含Python基础约750MB，不能说总内存275MB。待sole必要/actualowner/最小整合。
- 35303 InterQ必要已读§2/3前半和§4端点/6；当前动作ratio不含state-reaching history，observations只作context不进policy似然，detached prefix correction是bounded surrogate非精确无偏。§3.3 support allocation/完整Alg及直接ablation/限制尚未读足，不宣称深入完成。
- 34915 MXFP8实际读§2–4/10/12：同grid比更高precision sampler更一致但多个配对同时换W/A/kernel，weight误差分量未隔离；bf16无量化KV仍更一致。短dense可更慢，fixed microbatch成本与host混杂、一seed/最多60steps不排名最终质量。七同步条件与具体故障对照尚须按采用命题读足，不把配置相同当live-byte检查。未称深入完成/Books落实。

必要补齐：35303 §3.3/3.4完整support allocation、objective/Alg1及§4.2 additional analyses、AppC4/D已读。Prefix/Global与InterQ共享段归一displacement budget，对照支持本域support分配而非单纯增大correction；QAT+TIS/AIS只改当前token仍较差，但AULC并非全部胜QAT。ESS是importance-weight集中度而非“语义证据支持”；observation不进似然、仍影响后续history。完整mask+clipped sqrt(n) prefix/segment权重有界退向1，不恢复未截断精确无偏；只有环境kernel/协议相同且支持可用时原ratio恒等式成立。H20/8dense16MoE、4–30B/W8A8KV8/400steps；多seed仅BF16/QAT/InterQ在ALF/Web局部，其他覆盖有限。采用可缩为state-reaching history与current-token校正两层、固定预算support分配，非任务成功/无偏/通用稳定保证；待sole必要/actualowner差额。

33719 ZipFusion实际读精确v1 III/IV：BF16 exponent小范围block压成12bit、sign/fraction全保、otherwise原样；sharedmem压缩态读入后register重建不回写HBM。SGLang跨layerchunk回收和generation reserve实际管理仍需III后半补足，不能只读首4300就称完整实现核验。IV同fixed batch与各最大batch分别、H10080GB/BF16/Llama3.1/Qwen3-8B/8192input256out/计255decode不含prefill/initialcompression、新KV未压，不能把1.26decode收益当完整服务SLO。标准必要基本可缩到fused consumer机制，待III剩余明确格式metadata/动态路径边界、sole及owner。

33719补齐：III-C/D已完整实际读。format按TensorCore每thread8值分组，K/V不同layout、压缩块一直到sharedmemory保持压缩，register按bytefield整数恢复BF16；不合exponent条件保原块。append页未压，full页等待outstandingread后压缩；stablepageID经locationtable更新，跨层chunk仅清空且读结束才能回收，未来新页按uncompressed size保reserve。IV采用范围明确不含prefill/初压且新增KV未压，声明实现的一般动态压缩路径与本次benchmark所测分开。Ch45“Entropy与Kernel Regularity”仅一般envelope不承载无损BF16 fusedconsumer和reserve条件，拟最小自然段/本人note；不得授生产SLO/所有KV/本次实现运行验证。

34440 MoE speculative必要实际读精确v1 §2–5，当前可采用范围：dedup请求字节更少但slotkernel利用onchip复用可有更高effectiveBW，equalfixedwork下只在u_bar(n)<r(n)=beta_dedup/beta_slot时快；固定开销不等需另减。几何acceptance/平稳相邻token路由/理论忽略draft费，不授现实最优draft；主体oracle draft，12组fit在wholemodel数据之后且改过one-token来源，DeepSeek仅measuredtime/calibrated先登记、fit后成；单机各平台batch1、独立op不包含整图耦合、模型间拟合迁移会大错。未核Lean证明/请求源码，不声称独立形式证明或生产实现已证。Ch48只有一般draft/verify/acceptedprogress成本，缺dedup byte share与有效BW比的条件差额，拟最小一段放粗略benefit判断后，保正常serial及已有kernel退路；待sole必要/采用与真实SAVE。

35518必要补齐：精确§4.3/4.4及Limitations已读；coverage vs onpolicy corpus还改变数据量，不把收益唯一归覆盖。Valuehead初10步平方梯度占>99%，init选择与独立clip1/10/none控制；clip10降低clip比例但finalvalueloss近，不说全部提升来自阈值。DAPS同actor/critic初始配方对照，表是预算内bestcheckpoint非固定终局、多seed RL未系统核、critic amortized每actorstep多27–40%walltime（原模型任务域内数据）；不外推toolmulti-turn。支持最小head/globalclip分责与rollout前难度采样两层，待sole/owner实际。

34915补齐实际§7.1/7.2/9.1/9.2必要核心：响应缩短时step或per-token时间都会被fixedcost误导；同token数据只改microbatch数对照支持每microbatch加费，不能只凭回归指认。七sync条件分layers/grid/derivedlayout/graphstorage/completeness/outputsanity/observableverdict；F3/F4 stale derivedlayout形状dtype不变，livekernelprobe可发现、KL阈值不能替代，SGLang某些audit只比config仍有盲区。不是七条普遍新规则，采用缩到actual materialization vs config同一、微批固定成本与共享grid的各自判断。未核每个新PR/currentrelease或复现，不把论文当当下框架通用bug宣称；§10单seed/短轨迹/配对同时换W/A/kernel等反侧已读。rootCh33实际现有graphprecisionflow但无derivedcopy/liveengineprobe和fixedmicrobatch差额，待sole与自然最小稿。

## 已发生的Books保存（恢复先查真实写后，不重复插入）

35544/35556 Ch18、34427 Ch33、33360 Ch19、34566 Ch28已由唯一reader实际POST通过，五家族I生效，未预日级验收。35303 Ch33已真实SAVE在原量化ratio/网格后、ScaleRLT之前+本人note；33719 Ch45已SAVE于Entropy/Kernel Regularity后、Prefill/Decode identity前+本人note；这两项已自读与限定diffcheck并送reader，当前尚未收到实际POST，不提前计闭合。

## 待继续的材料（不冒完成）

AB首12中其余8尚未必要/Books；33076有早提交/crosslist信号，先定点核归属。AB2的20完整题摘独核准入结果：33496/35303/34915/34566/35130/35020/34682/34056/33379/33368/34907/33501/34440/33404/34731/33923/34824/33647可以继续，个体分数需按实际新增明确；33647最低5。33005需区分既有energy-latent路线增量，35518需补critic稳定与DAPS具体做法，只补决定准入事实，不先全Methods。不能把这32条或导航988报为已冻结/证实贡献。

原始导航cs.LG首timeout已恢复，官方pastweek Oct27段426条，相关术语标题返回可作为导航，不是426篇候选。new抓取实际Oct28，已作错窗导航隔离，不使用其材料计本窗。尚须补未覆盖具体主题/有界新命名标题查漏，不把目录全体转为关闭配额。
