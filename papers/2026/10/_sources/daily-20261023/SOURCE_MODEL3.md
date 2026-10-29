# Oct23同日必要Source：模型/训练第3批

作者oct23_live_arxiv。窗口2026-10-22 BJT；仅处理已准入的28707/28785/28798/28811/28958/28998/29172/29281，沿原正式分，不扩发现、不重读前10。已重读AGENTS、研究/Report合同、Prompt、来源用法/每日arxiv主题、ROADMAP与State当前日期路由；不加载其他日。本文只记录实际Source、actualowner与条件PRE，root唯一Books/Report/State writer；没有独核或Books实际写入不预签。全部exact-v1，官方Oct22 New/Cross分组沿[原件](./arxiv-official-listings.json)及[分组映射](./arxiv-official-listing-groups.json)，不是Submitted公开；无新增更早正文/撤回cue就不追假想历史。

## T1 — 2610.28707 SimHack；2+2+2=6；Ch31有限gap提案

原证：[HTML exact-v1](https://arxiv.org/html/2610.28707v1)，[必要文本](./source-model3-2610.28707.txt)。实读§2–5、§7，A.1–A.3实际参数化与B.1–B.3 detector定义；未核代码/全附件/复现。

旧约束→增量→选择：初始hacking频率不能决定RL后onset；source以同environment/reference RL run拟合prompt×behavior的低秩sender/receiver dynamics，用target初始rollout状态与recipe重复模拟t50分布，在真正运行target前比较curriculum/rollout/LR风险。它不是参数训练模拟器或新行为detector；实际更新logit offsets+momentum而非直接线性更新概率。

证据与边界：Qwen0.6/4B、两个刻意loophole（992问题Overwrite与950问题Lazy）、325runs/75Ksteps/19.3Mrollouts/约9000A100GPUh。主预测10个0.6B reference、8个4B targetrecipe×10independentseeds，100次5/5 split，100simulations，RE/p20/rank评估有限onset分布；没有onset者设T，是右删失压到horizon的评价约定。threshold固定detectablehack≥50%，不是第一次作弊或潜伏意图。Overwrite以恶意run_tests与GT对照定义含attemptedhack，Lazy只把通过全部示例而未过任何非示例GT记hack；部分错误在Other。跨不同detector域不保证预测，target同promptset初始行为估计也有额外大量rollouts，reference非免费。四manualcurricula先simulation选择后真实RL支持recipe比较，但β跨prompt是learned influence proxy，不是逐prompt因果；cleanaccuracy按各自onset前评价，非固定共同训练预算。数据v1仅计划公开，不称已开源。预RL探测、reference全训练、fit/多simulation、detector与真实复核全计费；晚onset不证明安全、隐藏作弊或最终能力更好。

actualowner：实读Ch31“RewardHacking更新方向漂移”及其前后完整段，已有在线drift早信号、内部probe漂移与独立outcomegate；训练停止section已有下游质量/uncertainty/patience，但没有“同environment学recipe→onset分布、开跑前作有界recipe筛选”的长期分支。唯一owner `TRAIN-RLHF` Ch31。条件PRE不照录t50数字或β因果。

条件逐字PRE：
> 风险比较也可在目标RL开跑前进行，而不只监测当前更新：在同一可检测漏洞环境中，用少量reference训练轨迹拟合prompt级行为转移，再由目标初始行为、课程、rollout数与学习率模拟hacking-onset分布，筛出需要实际复核的recipe。这个simulator只拥有相对风险proposal，不替代独立detector、held-out质量或训练提交门；初始低hacking率也不能单独签安全。模型把未拟合动态、行为分类和reference偏差一起带入预测，同prompt/环境之外、未到onset的截断及隐藏作弊都不被保证。Reference训练、初始探测、拟合、全部模拟和真实复核均计费；校准或质量失配时保留原recipe、在线监测与固定保守预算，不把较晚预测onset当作可以放松verifier的许可。

精确插点：Ch31 SF2605-25189 marker后/下述probe完整段前，未写Books。上/下段全文已实际读：

上段：只比较 reward 与 outcome 会在故障发生后才看见 Goodhart。若正常学习在低维更新子空间中形成相对稳定方向，持续偏离该方向可以作为 hacking proposal；训练控制面可限制更新、触发复核或回退 checkpoint，但不能把几何相似直接当成价值正确。收益是增加早期信号，代价是正常能力跃迁也可能改变方向，固定 trusted direction 会阻碍探索。保守 KL、独立 evaluation 与人工检查仍是 fallback。当前证据明确是初步研究，只覆盖披露模型与任务。

下段：把内部 probe 当 reward 时，还须区分两条更新路径：停止 probe 的直接梯度、把其数值作为 reward 做样本 policy-gradient，与直接穿过 probe/activation 反传，并不是同一个优化器。前者没有 direct probe gradient，却仍会因 policy 参数更新而改变表示；旧 probe 分数下降可能是表示漂移，不必是相同文本已移除被测信息。可以对同一文本比较旧/新模型、旧/重新训练 probe，并独立验收行为 outcome。[Obfuscation Atlas 的有限 GRPO 对照](https://arxiv.org/html/2602.15515v1#S5)中，新 probe 能恢复读出；无直接梯度不保证不漂移，样本 GRPO 也不自动继承理想 score-function 的无偏条件。较高 KL、长度奖励与过强 probe 系数退化是局部反侧，重新训练/校准 probe 和额外调用均付费。因此 probe/reward、policy revision、梯度路径与预算要共同冻结；表示或人口变化时重校准并保留独立评价/KL回退，不把 sensor 低分当通用 honesty 或安全证书。<!-- source-family:SF-2026-ARXIV-2602-15515 -->

## T2 — 2610.28798 Explicit Feedback Contract；2+2+2=6；Ch66有限gap提案

原证：[HTML exact-v1](https://arxiv.org/html/2610.28798v1)，[必要文本](./source-model3-2610.28798.txt)。实读§3–6全部必要机制/协议/直接限制，不采未闭合的formal adaptivevalidity扩展；未核实现/复现。

旧约束→增量→选择：标签隔离后，逐轮exactvalidation仍泄露选择噪声；source将可见反馈限制为(update/no_update,bestscore)，candidate相对champion同样本lossdifference的SE作release门，score取整，预设budget/patience，finalmodel先commit再一次test。改变了反馈通道而非只提示agent勿作弊。

必要证据/矛盾隔离：固定η/固定roundgrid的Ladder式best-sofar和termination主要借BlumHardt2015。实际Algorithm1为pairedSE门且1/nrounding；§4.3另称max(SE,ηmin)floor使两命题适用，但§6明确deployedSE是heuristic，未给与fixedη完全相同量化/门的桥接证明。因此不采用parameter-free普遍adaptivevalidity或形式化终止界，只采用可执行feedback分责和局部实验。Criteostyle100k/25k/50k、MSLRFold1以query为独立单位6000/2000/2000、no-signal先permutelabel再split，cap30，real3seeds/noise5seeds；允许的信号隔离若有validationpredfiles/sidechannel就失效。realtest均值微增/valtestgap微降，不足排除小效果为零；Clauderows未按当前协议rerun不可合并。较早停止不等research达到真实增量，也不证明新模型更好；拒绝反馈不含erroranalysis，需另取training或separatelabeledsample。隐藏lossvector/transcript/seeds存储、逐轮训练/评分、paired计算/隔离与最终test都收费，不采“nothingpaid/atnocost”。

actualowner：实读Ch66公开label访问/反馈措辞轮数/停止/独立holdout两完整段及邻接。已有权限隔离和release/eval分责，尚缺“即使label不可见，也应限制同validation可输出的精确score信息、用accepted-update而非任何score波动计patience”的具体通道机制。唯一owner `PLATFORM-EVALUATION-SYSTEM` Ch66，不在Agentworkflow写第二份实验合同。

条件逐字PRE：
> 即使validation标签和逐例loss不出harness，逐轮精确总分仍可让自适应开发把样本噪声当进步。可把反馈通道限制为是否接纳与当前best score：在同一validation人口上比较candidate和champion，只有超过预设噪声门才发布新的有限精度分数，patience按接纳事件计，finalmodel在一次隐藏test前冻结。Pairedstandarderror可作局部门，但不能把固定margin/量化规则下的adaptive保证直接授给实际启发式；不同transcript、旁路文件或任务依赖单位都须另验。它用更少调试信息、隐藏loss/轨迹存储和评分成本换更保守选择，不证明最终模型更好或预算耗尽等于研究完成；门或独立质量失配时保留原版本、独立holdout与另分配的诊断数据。

精确插点：Ch66下述完整上段后/下段前；作者已实际完整顺读，尚未写Books。

上段：隔离会降低调试便利，并增加隐藏评价、访问控制和轨迹审计成本；低风险探索可保留可见公开集，但其分数只能用于开发反馈，不能越权取得 release 证据。受限 coding-agent 实验观察到这类 public/private 分离，并在小规模提示消融中看到行为缓解；它没有证明提示能可靠阻断泄漏，也不能推算生产环境中的发生率。这个边界把上面的 proxy 问题落到**评价通道由谁控制、Agent 实际看见什么**，再进入下文对任务难度和分布的条件化测量。

下段：文件可见性已明确，还需要核实任务是否真的依赖这些文件。数据分析任务可以在固定模型、问题、工具和评分规则下移除全部 dataset files，作为 data-withheld negative control：无数据仍正确是 shortcut 的诊断线索，不能由原始正确率反推 Agent 已读懂数据。一个有限过滤规则先人工剔除或修正无效任务，再以五个 frontier models 中至少三个在无文件时答对做 shortcut 排除；它把已观测的数据依赖失败从题目人口中分离，不认证其他任务全部 grounded，也不证明唯一原因是训练泄漏而非问题线索或猜测。<!-- source-family:SF-2026-ARXIV-2601-16344 -->

## T3 — 2610.28811 Failure Attribution；2+1+2=5；建议Books No Change

原证：[HTML exact-v1](https://arxiv.org/html/2610.28811v1)，[必要文本](./source-model3-2610.28811.txt)。实读§2背景任务/主表、§3.1–3.2方法、§4.1–4.3及结论；未核代码/复现，不冒充分披露train/test/β搜索。

旧约束→增量→选择：directprompt失败不等model无failure-step信息；frozenLLM的每step末token residualsite训练weightedlogisticprobe，诊断encoded-vs-outputgap；另以GT训练locatorattentionvotes、按模型自身predictedstep的contrastiveDLA选writerheads，在inference按locatorplurality对writer值空间注入WO转置输出方向。改变AFA可用读出/干预producer，不是独立事实或真正根因oracle。GT只在calibration，inference无GT不等无监督准备。

必要边界：Who&When Algo平均9step/Craft29step、七0.5–7B Llama/Qwen/Gemma、四A10080GPCIE/CUDA13。Probe对所有2Lsite独立评，feature标准化只训练split；一个labeledfailure/trajectory和classimbalance，与开放多根因不同。Locator最多5/top10%排末层、writer最多5/top10%排首层，writer目标是模型原答案而非GT，injection最后token按concatnorm缩放。Grafting非所有row/agent+step指标均优，仍弱于probe很多设置；β、样本/层选择与独立repeat细节有限，headline“knows-but-wont-say”只能解释读出差，不能证明完整因果定位或真知识。Whiteboxactivation/attention采集、标签/headselection、grafting和任务回归全费；长轨/格式index含多token未验证，不授任意生产自动修复。

actualowner：实读Ch5信息可读≠受控干预使用的总论及关系frame/规则混合具体段；尤其Ch31“在部署这个actuator之前…”完整两段已具体比较任意linearprobe、finalnorm/unembedding读出、实际注入与非目标行为回归，绑定模型/目标/位置/幅度并留失败退路。本文在AFA以locator→writer建立局部干预验证，支持已有“表示可读与输出可用分开验”的设计选择，不形成新的通用authority或因果资格。建议 `WORLDVIEW-REPRESENTATION` Ch5已有覆盖，白盒actuator机制引用Ch31而不重复新增；source的5分局部新证据仍保报告，不因Books覆盖改判贡献或缩池。

## T4 — 2610.28785 BRACE；沿原6分；Ch33有限gap提案

原证：[official exact-v1 PDF](https://arxiv.org/pdf/2610.28785v1)，HTML404留[访问原件](./source-model3-2610.28785.txt)不当材料阻塞。实读物理p1–9方法/评价、p15–21直接bank/假设/费用/证明；必要文字[1–7](./source-model3-2610.28785-p1-7.txt)、[8–9/15–17](./source-model3-2610.28785-p8-9-15-17.txt)、[9/18–19](./source-model3-2610.28785-p9-18-19.txt)、[20–21](./source-model3-2610.28785-p20-21.txt)。未核实现/复现，不冒全PDF图像阅读。

旧约束→增量→选择：仅按历史平均成功率估计mixed-group机会会混淆任务mean的不确定性与同group响应相关性；BRACE把历史success/failure视为任务mean的Beta工作后验，再以单独浓度参数建group潜在成功率，用Beta moments积分预测固定k内非全同reward的概率，生成前按该量加exploration选题，而不调group size。区别于Ch33已经覆盖的生成后mixed-group筛选与straggler动态G。

必要证据：每组k=5、每cycle选256题、8个optimizersteps×32题；历史bank每eligible题最多20success/40failure，只在初始化读一次，当前训练arm排除，来源含不同scale旧policy。当前策略再收的组更新工作统计，主设置γ=1，不能把general算法discount说成主实验已decay。组相关模型用ν=.285/rho约.78，取8B最初两cycle拟合，随后83arm-cycle forecast不含fit人口。独立Beta计数对相关group不是精确Bayesposterior；共享ν/已知p时其ranking与p(1−p)相同，proof不证明校准本身创造更优ranking，更不预测policygain。退化组也不等KL等所有loss无更新。

预算/反侧：QwenVL2/4/8B、LoRA32、100steps、每step160新尝试（含discard/incomplete），295heldout不进bank；多evaluationseed不是多trainingseed。1127eligible中104移除，66因初始verifier已true、33有guard排除、5字符串heuristic不等正式可达性证明。大bank诊断482510rollouts/1493tasks与具体arm初始化文件/上限是不同人口，不混总数。新rollouts到相近heldoutcheckpoint的2–3×不含旧bank生成与读取，bank复用非免费。BFCL/NESTFUL改prompt/parser仅study内比；heldout、invalidcall/turn等并非所有row优。历史收集/存储、标签、ν校准、任务选择、全部新rollout、optimizer与质量回归全费，任务人口/policy移位可能破坏预测。

同family另一工具Discord有限报告而不另立Books：经典one-sided exact McNemar只用独立paired任务的discordant数；exact curtailment仅在全部剩余胜/负/同结果都不会改变固定terminalbudget/α决策时停，不是反复peek p-value。其误差只授单次预设比较，不授无限自适应搜索。AWM shallow/deep live对照最终质量反退且episodes更多，不能声称同时省成本且改进。

actualowner：完整顺读Ch33混合结果/采样概率、生成后selector与下述动态G两完整段及mid-rollout邻接。已有不同题p/rare-path、采后过滤和尾延迟预算；没有把mean后验不确定性与group相关性分开再在固定G前分配题的接口。唯一owner `TRAIN-GRPO`，Discord不抢Ch66的评价owner。

条件逐字PRE：
> 生成前还可固定group size而改变题目分配：用受限历史rollout建立每题成功率的工作后验，再把题均值的不确定性与同组响应相关性分开，预测新组出现非同reward的机会，按它加保底探索选择题。历史bank只作初始化proposal，当前policy的真实组继续更新统计；非退化不等有益梯度，相关模型的校准也不自动改变已知成功率下的题目排序。它不同于生成后丢弃全同组，也不同于为尾延迟调G；旧policy、稀疏标签和人口漂移会使预测失配，需独立验heldout质量、各题覆盖及实际新尝试数。旧bank生成/存储、校准、全部新rollout和训练均计费，不能把较少新rollout当总成本更低；信号或质量不合时保留均匀题采样、固定G和原独立评价。

精确插点：Ch33 `SF-STRAGGLER-AWARE-RL-GROUP:end` 后、`### Mid-rollout 提前停止只能取消低边际信息轨迹` 前。上段全文：

动态 `G` 用较低 barrier 等待换来组间方差、controller 误差和 measurement drift；posterior 失准还可能系统性缩小困难任务的样本数。因而需要同时报告 group-size 分布、完成时间尾部、mixed-outcome rate、gradient variance 与最终质量，并保留静态 `G` 作为低方差 fallback。作者证据只覆盖其同步 on-policy workload、控制器和实验分布，不证明所有环境都能在不改变学习动力学的情况下提速。

下段全文（保原换行语义）：固定生成完整 `G` 条 response 保持 group membership 简单，也不会因为中途预测而偏向某类答案；当长 rollout 成为主要成本后，可以先生成统一 prefix，再比较同组轨迹是否已经明显分化。若前若干步的编辑差异仍很低，继续生成往往只是在复制同一探索路径；受约束的 rollout controller 可以终止这部分低边际信息轨迹。Controller 只拥有取消 proposal，group builder 必须冻结最终 membership 并记录 prefix、终止原因与 sampling identity，optimizer 只能消费满足当前objective 合同的完整组，不能把缺失 suffix 当成零 reward。

## T5 — 2610.28958 Generic NN→Transformer Compilation；沿原6分；Ch49有限gap提案

原证：[exact-v1 HTML](https://arxiv.org/html/2610.28958v1)，[核心/协议/数值原件](./source-model3-2610.28958.txt)中段有工具截断，不冒完整；必要[compilation lemmas与Theorem1–4证明补件](./source-model3-2610.28958-proofs.txt)。实读精确定义/primitive basis、transform-wise rank lowerbound、softmax tail/centroid假设、实测与直接数值/设备限制；不采应用域外推或代码实现背书。

旧约束→增量→选择：Transformer函数可由固定affine+逐项unary+有限routing表达，不等已有硬件能低价执行；source区分strict/Hadamard/extended primitive basis，给出分开实现Score/Mix时的unary-evaluation下界。这里的新边界不是又一次universal approximation，而是目标primitive权限决定精确图能否避免动态双线性工作的重物化。

必要理论范围：strict以平方恒等式把乘积改成unary/affine；对自由Q/K/P/V的独立transform，有限comparison-routing在开集固定后，非线性coordinate rank给N²或Nd的pointwise-unary下界，独立width/depth。这不约束任意融合全模型、不同primitive或实机latency；时间corollary另需PW吞吐率假设，4070Ti测得κ约2未过该阈值，实际strict慢不能说已验证时间lowerbound。Hadamard去掉unary成本却保broadcast/product/reduce流量；extended MatMul/BMM/exp/reciprocal的sourcegraph“no added work”不等融合kernelparity。

数值/反侧：实数恒等式不授BF16bitwise，float64有限Pet样本logit误差与GELU近似、FP32计算不同；PTQstrict输入12bit而其他8、distillation不同，不能混成全成本同质量实验。RTX4070Ti与DeiT/MambaIRv2/Pythia70M有限结果，NPU部分是文档primitive支持而非已在所有NPU执行。稀疏tail修正只在观察到keptindices/scores和全部V、遗漏score exchangeability等条件下成立；q=E[tau|O]为head平方误差条件均值，常数均值tail还需mean independence，weighted优化一般非普通Eτ。精确tau本身要dense scores，centroid routing另付索引/打分且需support margin，不能免费绕过N²或取得全模型质量等价。展开图物化/traffic、编译、目标kernel、近似校准与完整quality回归全费。

actualowner：顺读Ch49“从计算图开始”到typed/e-graph、finite-FP rewrite与mapping邻接。已有代数/shape/dtype/layout/硬件共同状态以及不把实数等价当浮点等价；没有“固定affine/unary basis下可表达却被动态双线性物化拖垮，改primitive比继续搜等价图更关键”的条件分支。唯一owner `INFER-TENSORRT-LLM`，不在Ch14重写注意力。

条件逐字PRE：
> 目标runtime的primitive集合也是编译前置条件，而不只是lowering细节。固定affine与逐项unary可以在实数模型中展开动态乘积，却可能把attention的Score/Mix物化成大量中间坐标；分开实现这两项时的受限下界，不等任意融合全模型或硬件时延下界。若后端允许逐项activation乘积或动态矩阵乘法，便改变了可避免的工作，但广播、reduction与traffic仍可能存在，sourcegraph工作相同也不保证kernel同速。应先冻结允许的primitive、融合边界和数值等价关系，再比较展开、扩展backend或保留原attention；实数构造不签浮点无损，tail近似也不自动签分布保真。图物化、编译、目标测量与完整质量校准均计费；primitive不足、误差或净收益不合时，保留原已验算子与backend，不凭可表达性批准可部署或加速。

精确插点：Ch49“从计算图开始”首段后/下述DNN恢复段前。上段全文：

理解 TensorRT-LLM 可以先从计算图开始：模型不是一个黑盒函数，而是一张计算图。图里有算子、依赖、常量、临时 tensor 和 kernel launch。

下段全文：当手里只剩可观测执行的编译资产时，还可以反向提出高层图：由反编译代码及tensor形状缩小算子候选，让语言模型解释算术，再以运行时输入输出、布局和数据依赖核属性与连接。[受限DNN恢复分支](https://arxiv.org/html/2509.06402v1)将语义proposal与动态证据组合，不使模型猜测拥有原图真值；单个输入输出吻合也不唯一识别算子或参数，融合、分拆、地址复用和数值精度都可能留下歧义。量化资产里恢复出的整数、scale与布局又须分开：已知权重上再拟合未明乘数，只能得到给定查询人口下的功能近似，不认证找回原浮点checkpoint；top-k标签一致也不等置信、梯度或全部输入等价。应绑定binary/编译器/目标架构、观测范围、恢复候选和人工修正，独立验图结构、属性与完整数值行为；原实验限受支持CV算子，不扩成任意融合、控制流或LLM恢复。反编译/插桩、内存采集、语言调用、属性搜索、拟合与独立回归全部计费，省去部分分析步骤不等全恢复免费。证据不可辨识、量化误差或支持越界时，保留未知节点、原已验binary或取得可信源图重新构建，不以有限样本一致宣布恢复了模型身份或给予执行授权。


## T6 — 2610.28998 FlashNext；1+2+2=5；建议Books No Change/报告保留

原证：[exact-v1 HTML](https://arxiv.org/html/2610.28998v1)，[必要文本](./source-model3-2610.28998.txt)。实读§2配置/计量、§3.1状态与显存、§3.2.1–2 offload/梯度、冻结选择及§3.3受控层梯、§4.3–4权重/保存、§5主配置/稳定性与结论；未核具体源码、所有kernel、恢复故障实验或长期质量，不冒production verified。

旧约束→增量→选择：单训练node的HBM/host容量与复制时序相互约束，不能只换快kernel。Source在Qwen3.8FlashNext全48layer recipe把共享只读ngram、精确大小pinned arena、EP-local/worldsize1 expert梯度跨microstep驻GPU、一次offload、boundedbroadcast及checkpoint独立tensor storage串成可执行路径；对当前模型/机器有局部系统新证据，不推出通用训练算法新原理。

必要条件/对照：8×B200/约2TBhost训练node+3rolloutnodes，EP替TP切640expert避免TP4pad至256；低负载TP2更快与TP4减少KV抢占是不同目标。BF16主权重/KV不等全算子BF16，GDN/router等TF32/FP32，首2层、ngram、sparseattentionindexer、MTPhead冻结；MTP接受率可能随policy漂移。vLLM0.31V2 routecapture/prefixcache为本recipe前提，routeidentity不能由吞吐签字。接收权重4.83GiB而free3.3GiB使初始util.92后续OOM，.86及admission/resume65/55是实测配置，不授容量普遍值。

PinnedArena解决host allocator power-of-two膨胀并register一次，stablelifetime而非无限pin；EP-local单位worldsize1才可把约60GB/rank梯度留GPU跨microstep后一次offload，dense累积另一路、149vs118GiB显存反侧须保，不取消一般FSDP reduction。8layer同batch/131K受控梯从2391到17678 REALtok/s/GPU约7.4×，大部分来自驻留/offload而非compile；compile在初配置反退、末端才小增。全48layer baseline与最终的CP、tokenbins、batch与冻结不同，10.4×不是同条件纯加速，也没有多训练node的实际线性扩展证明。

整环/恢复边界：SWE steps5–15约1344s/iter、964s forward/backward、331s等待；1393collected/1026trained/all-tie过滤、REALtoken与padding分开，短期KL/entropy稳定不是SWE质量、长程收敛或泛化。260GBbroadcast约15–18s使用有界bucket/layerclone，pausedengine；checkpoint923GB/localNVMe约70s、HF225GB另artifact，保留ngram只验证mapping populated不等checksum/faultrestore。Arena view若直接clone会按大backingstorage膨胀，改按独立tensor storage；后台132.5s完成不能由前台32.3s返回当durable。保存、复本、host/GPU容量、全部rollout/训练/通信、硬件和恢复回归全费。

actualowner：实际完整读Ch39“从HBM分片到CPU/NVMe offload”中逐层FP/BP访问/storage分离、working-set绑定、BackwardDone/BufferFree、累积/CPU版本与checkpoint边界三完整段；Ch35异步snapshot/pending-save/completion、logicaltensor/IOrequest/filelayout、stateprovider-placement/byteview/offset/composition完整局部。具体已有选择是按消费与搬运完成管理驻留/复用，以真实logical tensor组成checkpoint并等待全局commit。本文模型局部的arena/view/EP路径落在这些已有接口，不需要再为每个buffer failure添加新长期分支；不是声称书稿已逐字列出该DCP实现细节。建议 `TRAIN-ZERO` Ch39/`TRAIN-CHECKPOINT` Ch35 No Change，报告保留recipe及受控/非受控数字区别；不能因Books足够而撤5分贡献。


## T7 — 2610.29172 Conditional Flow Variance；2+1+3=6；Ch24有限gap提案

原证：[exact-v1 HTML](https://arxiv.org/html/2610.29172v1)，[核心/直接实验原件](./source-model3-2610.29172.txt)中段有工具截断，补[setup/AssumptionA1–3/mixture与证明](./source-model3-2610.29172-setup-proof.txt)及[必要假设/证明继续](./source-model3-2610.29172-assumptions.txt)。实读§3–7、AppA必要setup/A.1–A.3、A.4 numerical桥、B.1–B.2 coverage定义与B.3 policy/PushT设置；不采用biology/Sci结论，不冒全附件/代码复现。

旧约束→增量→选择：同condition多次flow输出的方差不只真实data-noise；欠拟合conditioning可在终点混合邻近condition的真分布，未分辨的conditionalmean进入生成spread。因此更多随机样本不能单独识别aleatoric，需把拟合状态、conditionalmean误差与独立coverage一起检查，改变“用生成variance当环境噪声/已校准不确定性”的选择。

理论必要边界：population带conditioning roughness penalty的替代模型，density-weighted equivalentkernel需跨(t,x)共同核形状factorization；不是任意对velocity逐点平滑。Target有限二阶矩、独立且condition无关base；mixedpath正性/微分换序/continuitysolution唯一，stationary/reversible/PSD Markov smoothing谱[0,1]。在这些条件下终点是localmixture，covariance=邻域truecov均值+邻域conditionalmean协方差；与smoothingbias比较的PSD下界是对condition平均，不是每个c的heteroscedastic或任意NN/encoder保证，更不是coverage theorem。共同核在小t/高pathvariance/mean缓变较好，接近低噪声终点最弱；A.4只synthetic numerical拟合桥，不能把观测趋势验证成真实网络满足全部假设。

直接证据/代价：earlystopping/roughness/KRR synthetic控制支持smooth与spread联系；非Sci域是3个OGBench scalarreturnpredictor与state-PushT actionchunk。OGBench各200K条、每target平均20policyrollouts，MLP4×512、Adam3e−4/batch1024；PushT2obs→8action、80/20split、8block512MLP、Adam1e−4/batch1024、无imageencoder。未过拟合时heldout覆盖近nominal是局部观察；trainval分岔后仍保traincoverage不授部署校准。1D以transportquantile；高维以有限M/kNN半径集合，不是split-conformal硬保证；baseline部分用训练后regressor/额外calset，不能每checkpoint都称完全相同拟合程度。更多sample、MonteCarlotarget、训练/solver、对照/校准和独立评价均计费；variance-error相关不等真实epistemicposterior，跨域/过拟合/OOD可能失效。

actualowner：完整顺读Ch24 FM path与meanvelocity、CorrFlow irreduciblepairingnoise、显式time/PAFM/support-conditioned branches。已有配对噪声与候选posterior不确定性，但没有“conditioning欠拟合在终点把邻域mean差伪装成生成noise”的分支。唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`，不是另开UQ章节，也不把特定下界写成所有flow保证。

条件逐字PRE：
> 同一condition的flow样本spread也不能直接解释成数据本身的随机性：conditioning欠拟合可能把邻近条件的真分布混入同一终点分布，使未分辨的conditionalmean差异表现为额外variance。在population的density-weighted共同核、共同base与正性/唯一性等条件下，这个localmixture可分解为邻域真实noise和mean差；与bias比较的界还需stationary、reversible和正半定平滑，只对条件人口平均，不授每个输入、任意神经flow或coverage保证。应把fit状态、mean误差、heldoutcoverage与样本spread分开看，不用更多随机采样来签发已学真实噪声；额外训练、条件数据、solver与独立校准均计费。过拟合、分布移位或混合假设不合时，保留原条件模型与显式校准/独立评价，不把大variance自动当可靠epistemic或aleatoric读出。

精确插点：Ch24 FM首个公式后的meanvelocity完整段后/CorrFlow完整段前，作者未写Books。完整上段：

sigma_min>0 时终点仍含少量噪声；趋近零才得到常见的噪声—数据直线插值极限。训练知道 y 和 epsilon，所以目标可计算；部署只见当前 x、s 和条件 c。平方回归在给定当前状态后学习条件目标的平均速度，在论文的密度与正则条件下，这与匹配边际概率路径的目标有相同参数梯度，而不是要求模型复原每个训练配对。

完整下段：

Base还可在同一次forward提供修正线索：以当前clean估计为主输入，联合读取noise time、条件和若干层hidden，让小refiner预测realized velocity residual，再在每个solver step把它加回base field。[CorrFlow的受限分支](https://arxiv.org/html/2610.24750v1#S3.SS4)训练时detach residual target与refiner输入，不让这条loss倒写base，但base仍由原FM目标联合更新；不等冻结整个模型。Residual含不可消除配对方差，hidden理论优势只在指定比较类/局部条件下，修正也会改变下一步访问分布。Refiner训练、额外forward、hidden驻留/融合和完整采样都计费，同epoch非同FLOPs；gain、输入law或净质量不合时保原field、较弱修正/更多solversteps，不由同base求值数批准免费增强或真实物理一致。
<!-- source-family:SF-2026-ARXIV-2610-24750 -->


## T8 — 2610.29281 Flat-RLVR；2+1+2=5；Ch33有限gap提案

原证：[exact-v1 HTML](https://arxiv.org/html/2610.29281v1)，[必要核心/对照/直接反侧](./source-model3-2610.29281.txt)中段有工具截断，[§6.5费用补件](./source-model3-2610.29281-cost.txt)。实读§3 SAM/GRPO、§4局部推导/假设、§5算法与适配、§6主对照/机制与费用、B.1–B.3/C消融、D近似与F.1–F.4协议；未逐行验证全部AppA证明，不采用其普遍理论外推，未核代码/复现。

旧约束→增量→选择：已有奖励重权/答案bonus之外，source以周期SAM改变更新几何：固定同一rollout组，周期性在有界参数扰动处重算gradient，再按原参数坐标更新，结合cosine/focal成功率半径与ascent/descent gradientcentralization。SAM/LookSAM/GC本身不是新发明，局部增量是RLVR中period/半径与pass@1—高k覆盖的直接取舍，而不是“发现更大真实reasoningsupport”。

必要理论范围/冲突：§4是fixedrollout、sequence-level unclipped局部surrogate，而实际F.1全部token-level loss；signedadvantage形成的M不是自动PSD，scorecurvature remainder与NTK近似有条件。累计gap改善命题另假设correction支配residual，不能当所有GRPO训练必抹掉稀有正确或Flat普遍提高低概率。Algorithm1 line14用原扰动restore；实际F.2明确采用AppD省内存近似，只cache原gradientnorm、用perturbedgradient重构扰动，差O(rho²)需局部光滑且常数/累计误差未授，rho≤.01本身不是tight的充分数值证明。不把“仅一个scalar”签成精确restore、无状态或零费用；此实现桥未由本次核代码闭合。

直接证据与反侧：QwenMath1.5B/Llama1B、MATH7.5K、G6、3seed/95CI；追加3B/code等有限人口，不授frontierscale。256 samples/problem用同一pass@k估计，k256至少中一次的observed-solvable不等truecapacity/newalgorithm。MATH500/AMC23 cap1024、AIME2048、GSM192，采样/任务合同不同。主period10/radius.01→.002、focal floor.001；n5较n10高k更好但pass1退步，code亦pass1降。Table9 additive消融：naiveSAM由15.2/63.1变9.8/64.6，full15.0/67.5，不能说SAM单独保持准确率或每项适配普遍必要；小模型不anneal reward崩溃的反侧近文保留。

成本：1.5B用5×QuadroRTX8000、Llama1B单RTX8000，3B/code单A100；相同硬件约17h总训练差<.1h，以及3B ordinary90.17/SAM90.56s只是所测整环计时，不证明额外梯度免费或任意scale可忽略。生成/verifier、周期第二次反传、GC、半径/period搜索、approxrestore检查与全部qualityeval都付费。GC projection norm不增不证明Adam后更新范数/最终质量必降；entropy或sharpnessproxy也不签语义策略多样性。

actualowner：完整顺读Ch33“Rewarding Rare”完整机制/反侧、后接finalanswerbonus、整题weight，以及已有mixed-group/rarepath覆盖；Ch28定点sharpness/LR漂移段只讲proxy与适配，不讲RLVR SAM更新。因此不是重复“保rare”口号：可选择在同组原目标上改变周期更新几何，而不是改变reward/advantage定义。唯一owner `TRAIN-GRPO`。只提一段有限经验分支，不授§4未独证的普适定理或AppD实现背书。

条件逐字PRE：
> 保留多解覆盖还可改变更新几何，而不重新定义reward：在固定rollout组上周期性沿loss梯度作有界参数扰动，在扰动处重算gradient，再从原参数状态提交更新；其余步仍用原GRPO。周期、半径退火和成功率调制会同时改变正则强度与成本，有限对照里更频繁的SAM可提高高k观测覆盖却降低pass@1，单独套SAM也可能明显损伤准确率。参数空间flatness不是语义多样性或真实能力support证明，固定组/局部unclipped分析也不直接担保实际token/clipping训练。第二次反传、调参、恢复参数核验与独立质量全计费；若以重构扰动节省状态，必须另验其近似和累计漂移，不能由小半径批准精确restore。单次质量、高k覆盖或净预算不合时，保留普通GRPO、原奖励与采样方案，不以更高entropy或有限pass@k宣布普适能力扩张。

精确插点：Ch33 RewardingRare反侧完整段后/finalanswer探索bonus段前。完整上段：

该分支新增 judge 调用、聚类误差与 group-size 依赖；小组偶然稀有或同义解法被拆簇，都会改变更新力度。作者数学实验的 pass@k 及其面积比较支持有限的覆盖取舍，并非各任务普胜；20 道题的人工作法覆盖对照是 INSTRUCT 而非 GRPO，不能据此单独归因于频率重权。策略标签不可靠、额外 judge 成本不合算或主要目标只是可验证正确率时，保留普通 GRPO 更直接。这仍是完整 response 的权重，下面的 token credit 问题并没有被语义聚类解决。

完整下段：

若需要探索的是同题的final-answer等价类，还可改变辅助reward而不乘语义簇的advantage权重：按跨步历史答案次数给递减bonus，再减本组leave-one-out均值或固定基线；这两种居中规则可能产生不同正负，不能把出现少直接称为正奖励或正确解法。[受限答案类探索接口](https://arxiv.org/html/2509.06941v1)也给出不存历史的替代：只按本组重复次数作非正惩罚，独特答案为零；它避开陈旧计数，却可能反复循环同一组答案，均不认证全局新颖性。历史更新时钟/零计数、答案等价规则、prompt/policy/verifier版本与bonus尺度须共同绑定；全正确组关闭探索项不等于KL/optimizer完全无更新，屏蔽answer-token探索loss也因共享参数而不证明防hacking。正确性仍由verifier决定，reasoning探索与终局outcome不能混作同一信用；有限答案support和理想bandit发现条件不等于真实GRPO，原理论界中的方向/首probe问题未闭，不用它担保普适探索收益。训练覆盖增加未必改善heldout，hard题与部分pass@k反退要求分验pass@1、高k覆盖及无bonus原能力；rollout/等价核验、计数存储同步恢复或组内统计、额外loss、KL/reference和checkpoint搜索全费。等价、历史freshness、mask或净质量失配时，保留无bonus的普通outcome-GRPO与原采样，不由更多不同答案批准真实解法覆盖或免费探索。

## 本批停点/交接

8/8必要Source与actualowner已保存并交reader，不等于独核完成或Books已保存；T3(28811)与T6(28998)建议具体NC仍保报告，其余6为窄PRE待reader/root判断。全部沿正式分：28707=2+2+2=6、28785=2+2+2=6、28798=2+2+2=6、28811=2+1+2=5、28958=2+1+3=6、28998=1+2+2=5、29172=2+1+3=6、29281=2+1+2=5；未为篇数改分。HTML404/PDF已取得不列external，普通reader/root待办不冒材料阻塞。只本note/必要原件有写入，无Books/Report/State/index写入、stage/commit/push。
