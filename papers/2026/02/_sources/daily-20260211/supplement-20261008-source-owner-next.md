# 后续已准备单篇：Source 与具体 owner 差额

作者未自授独立 Source/PRE/POST/DAY。日期为 root 已核的本批 arXiv 有上下界推断 Feb10 BJT，非 registered=public timestamp。候选不因 Books 已覆盖或理论争议缩池。以下每篇实际必要主文/evaluation/直接反侧已读，剩余请求是非作者采用复核而非外部材料 hold。

## 2602.08239 Linearization — 中心保证隔离，拟仅报告

原件 webCore4–10.json（webCore9末尾完整AppendixH Eq92–99）；local proximity/squared loss/continuous gradient-flow ≠ finite AdamW CE。实证RoBERTa125M LoRAr8、Q/V/K、V100、10epoch、32calibration points、fixedσ=1e-4；λ50更线性却CoLA74.59低λ5的80.44、SST2低λ.5；作者§6.3承认不同config固定σ不公平。Theorem7无η<1，AppendixH也未补：K=1,S=3,σ=1,Y=1,c=1满足PSD/condition1，η3/a.25，实际ridge residual sqrt ratio=.4而Eq21下界10。只隔离此layer/risk保证，重开需要官方更正/必要条件与一致推导，不要求修全论文。Ch30实际 rank/target modules 183–226已覆盖proxy placement非重要性/预算及真实质量回归；本篇未提供可安全采用的通用谱选层规则，受限prox诊断/CE反側留报告。2+1+3=6，中心设计反证深入，拟仅报告/中心争议。

## 2602.08329 PrHS — 条件 CIS 与失效预算分支

完整 prhs-method.json S3/S4/S7 与 prhs-eval.json S5。完整anchor query topk，cosine>.8选择共享头；topm=k/3 dilation±1，非共享头仍full scoring；PSAW依赖recency假设，ETF冻结prefill部分prefix更新而decode新token不需同mask。固定q/K截断attention TV=dropped mass可保，root实际已核MI证明支持集合/Markov缺口，不采用nearoracle普遍保证。

Llama2/3/Mistral GSM8K/COQA、LongBench；CIS与matched CIS*须分budget（LongBenchavg547.5/512）；dense GSM8K和若干LongBench/增r条件仍胜，r2增加budget167反而低r1约124。oneA100、B8/16、1–4k、1/8 sparsity；9.9x operator B16/2k与2.82x decode B16/4k不同分母，H2O相同点可更快；precision/TTFT/request SLO未披露。不把有限mass proxy当生成无损。

Ch45实际359–394 Top-p/估计器、394–413预付检索/conditional anchor与566–623跨层共享；跨层selector→consumer早已解释，但未见“query-conditioned跨decode-step继承选择集”的独立刷新边界。拟新增一段：复用的是indices而非KV内容/attention权重，query gate仍只proxy，完整刷新+dilation增加真实budget，质量退则fullselector/FullKV；PSAW/ETF是不同prefill分支不合并共享收益。2+2+2=6，理论隔离已深入受影响命题。请求root Source/PRE判断可否仅采用此受限机制；未获Ch45锁。

## 2602.08376 OJBKQ — 量化校准目标与候选路径

ojbk-method-eval.json完整S3–5。runtime Xtilde 与fp X 分开，Y*(μ)=(1−μ)XW+μXtildeW，λ²weight drift；BILS percolumn，Babai approximate，RandomK candidate 包含greedy并各有独立residual buffer，不称globalopt/jointactquant。C4 128×2048 calibration，W3/4A16/BF16，g128或ungrouped；K5/μλ有限sweep。Llama/Qwen/Mistral PPL和6MC/3reasoning，Qwen3-8B3bitavg68.08低AWQ68.65、部分MBPP/PPL不占优；未报告serving时间/SLO或完整制备成本。

Ch49实际metric-vs-fixed-ordertrajectory2182–2190、quant objective/calibration930–980：已有算法语义/基准kernel边界与增广ridge目标，但没有“部分量化上游造成X/Xtilde target选择”连续插值及独立候选path。拟在calibration目标处自然一段区分input/target identity与candidate buffer/scoring成本，保成熟PTQ/高精度回退；不必介绍整Babai/Klein implementation。2+2+2=6，具体长期目标差额深入。请求root Source/PRE及Ch49窄锁；未写。

## 2602.08194 DiCode — Code Environment Curriculum

dicode-core.json完整S3/S4/S6；FM在固定Craftax simulator接口生成initial state/transition/goal程序，compile+short rollout只过滤执行错误，非任意物理或完整semantic validity。Parent lineage+performance引导，两步description/code，archive learnability选择，20%target simulation budget，async会等待valid batch。PPO-GTrXL共同实现、2e9 envsteps/5seeds/1024heldout包含generated steps；SFL同steps少梯度，不同总FM成本。OL去parent/performance降40.91vs48.33支持bundle，非唯一个环节因果；不可泛化LLM所有环境。

Ch31实际799–823 skill-conditioned curriculum与899–909environment/interface双控制已有controller/verifier/policy版本；本篇具体差额是level从seed转executable transition/goal并固定target anchor，代码可执行不等curriculum useful。拟补一段固定engine下的rule/generation/goal版本与short-runtime gate、目标anchor及费用/分布失败回退。2+2+2=6，申请Source/PRE；尚未写。

## 2602.08234 SkillRL — 拟已有覆盖

skillrl-core.json完整S3/S4/S6；o3抽取success/failure一般/类别skills，general always、task TopK相似，teacher coldSFT→GRPO与validation-failure bank演化。SkillBank与policy同更新；validation因此为training feedback，不能当最终independent gate。Table2 TriviaQA/2Wiki/MuSiQue低某对照；GRPO/RLOO部分复用原结果、SFT/teacher/RL总预算不齐，不能纯归因library。单trajectory10–20x压缩不等prompt/fullcost：实际prompt1450→<1300约10.3%。hardware/precision/concurrency/SLO未披露，不核代码。

Ch84实际363–393：failure-localized candidate patch/consumer验收及policy×bank冻结cross-product已覆盖更新与共适应责任；Ch77已有派生经验/reader对齐。SkillRL具体层级检索是这一branch实例，未建立新接口或独立因果，因此拟已有覆盖AGENT-PLATFORM，不写Books。2+2+2=6，准备请root必要Source/Existing核，非贡献前关闭。

## 2602.08281 Primitives — 组合能力的受限诊断差额

primitives-core.json 完整 S3–7；必要训练配置 Appendix B 已定点读。固定 verifier/iid 下 pass@k 是每题 p 的采样曲线，128 次零命中仍不证明 p=0；δ=.125、K8只给期望至少一次，非高可靠保证。atomic-only 训练与组合测试（4种代数操作、深度2–5、12,800训练/800测试）支持有限组合迁移与 atomic regression；ground-truth 前一步条件下的 atomic rate product 与相关系数不是实际自由 rollout 的独立性或内部 primitive 因果认证。Qwen退步较少，Llama/Gemma退步显著，不能写RLVR必然获得新技能或必然损伤单步。GRPO/verl/vLLM、G8、128globalbatch、lr1e-6、response8192，KL只监测非loss；硬件、precision、独立重复/CI未披露。

Ch31 403–434已经承载 sharpening/expansion/mode extinction 和不同 pass@k 目标；Ch5 75–88承载 representation compositional usefulness、冻结 executor/search 与组合不能自动外推。这些不是本篇的具体“组合成功与各原子保持分账”诊断。拟 Ch31 一段要求在同一 oracle 下另测 atomic tasks 与组合任务，teacher-forced atomic product 只作诊断而非链可靠性，保留完整 rollout 和多预算曲线。2+1+2=5，具体设计反证加深。请求 Source/PRE，未获锁、未写。

## 2602.08287 Noise — 随机 token 扰动的输出 agreement 目标

noise-core.json 完整 S2/S4–7，noise-direct.json 必要 Appendix D/J；主文 Lemma1 负T与 Appendix D 正T互相不一致，只采用D中正确的log方向，不采用主文负截点。Gaussian OU 理论的 E[f(X)f(Y)] 是未中心化 second moment，不是普遍 covariance；noresidual/mask/normalization 的简化分析与有限真实 Transformer 实验分层。Deep Transformer 实际噪声有阻尼，强 covariance 区间另依赖 bounded输入、正crossmoment/columnweight，不推广到任意训练LLM。

训练补充项 −Σclass p(X)p(Y)，Y按(1+ρ)/2保留token否则替换；这提高输出agreement/置信，不自动保语义或正确性。n10–100 parity、mod113小Transformer与极小WikiText模型（4层d30、H6、vocab500、train1000）支持有限学习曲线；4500→3300是26.7%少iterations，额外corruptforward不能变成36% wallclock降本。硬件、precision、E2E未披露。Ch28 149–164已经有按短窗充分性gate的clean/corrupt目标，但没覆盖“无语义gate的随机replacement与概率内积可同时推confidence”的差额。拟 TRAIN-PRETRAINING 一窄段区分二者及grokking目标、语义破坏/额外forward成本，保原NTP与gate分支。2+1+2=5，理论不一致受影响命题加深。请求 Source/PRE，未写。

## 2602.08449 Regime — 中心MI→风险界争议；局部结果仅报告

regime-core0.json 完整 S3/S4/S6 + S5前21000字符，regime-core1.json S5 offset21000到结尾，regime-direct.json Appendix A.1 741–750。root实际已核：loss允许随regime改变时，将固定f=loss(a,E)的双分布差替换成Δπ不成立；constantZ/A与不同loss反例。只隔离该普遍风险界，重开需loss invariant等实际条件/官方一致推导，不修全文。

RBFT最终token residual的2层probe+GRL，Qwen2.5-7B-bnb4bit/LoRA32，persona与sleeper固定prompt；year比较还同时改变“parameterizedqueries”指令，不能作只改变year的因果。Table1 sleeper Risk0与caption“fails behavior”冲突，utility表缺值与正文100%不一致。bounded观察仅支持behavior/probe decodability不必同步，不认证唯一distributed机制、触发无关或alignmenttax-free。Ch5 243–255已区分readout/control/behavior，Ch66 218–230区分监控cue、域内可识别与域外声明。主文不足提供可执行可安全采用的通用控制契约，因此拟暂缓中心保证，局部报告保留，不写Books。2+1+3=6，设计反证深入。

## 2602.08693 Cognition — 同证据重评分区分采集与推断

cognition-core.json 完整 S3–10；4button主动观测任务（红button .9、另三 .5），2–15步采样后一次latent inference，非bandit即时reward。固定LLM取得的同一证据交给MAP inference，再与PPO采样+MAP对照，可把“如何获取证据”与“如何解释已得证据”的缺口分开诊断。PPO只near-optimal参考非证明ceiling；MAP依赖已知生成模型。人类GUI50招募/46完成×100 games与LLM文字55k+games不同界面/预算，不把差额当普遍人机能力。CoT主要改善后端推断是局部结果，行为拟合参数不是真内部机制。硬件precision/API具体版本/SLO未披露。

Ch66 228rules-given/unknown与3774–3785 evidence trail/final answer已有分层，但未见“冻结同一主动采集证据，替换inference，再替换sampling”的matched counterfactual分账。拟 PLATFORM-EVALUATION-SYSTEM 一段同证据oracle/MAP对照，绑定生成模型、interactionbudget、可见history与最终scorer，不把两差额相加作独立因果分解。2+2+2=6，具体诊断缺口加深。请求Source/PRE，未写。

## 2602.08874 Safety — 组合危险意图与上下文长度联合测量

safety-core.json完整S2/S3/S5；精确v1标题 Is Reasoning Capability Enough for Safety in Long-Context Language Models（不沿最新API改名）。100 AdvBench×4 reasoning types×0/16/64k=1200合成样本，Gemini2flash碎片生成/同judge，无独立人评。直接retrieval安全95–100并不认证组合后的拒绝；multi-hop某模型29→64改善而另一93→37退，不宣称长度/思考普遍增加危险。正文14models与实际table15冲突，以表的人口为局部范围，OpenRouter路由/不可固定backend版本；reasoningtoken增加不是SLO，positioninsensitive safety不证明retrieval成功或唯一postretrieval因果。

Ch72 669–673已经有多轮history/composition与安全/utility分账，2175有长benign比例稀释；但不能从二者推定本篇同context“原恶意单needle→隐式桥接fragment”的构造。拟 PLATFORM-SECURITY 一段将直接危险检索与组合识别分开测，联合长度/位置/相关背景与原固定守卫，生成碎片judge不作truth/授权。2+2+2=6，具体反侧加深。请求Source/PRE；未写、不授权绕过任何防线。
