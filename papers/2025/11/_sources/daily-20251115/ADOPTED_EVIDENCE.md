# 2025-11-15 其余14项必要Evidence与最终Books作者判断

作者Planck；检查时间2026-10-04T19:07:02+08:00。仅本日16个真实Fri14 list身份中的新增14项；Language Drift/ParoQuant已由Ohm局部最终回核通过，不重复。所有采用exact-v1，日期均使用[Ohm实际通过的组合权限](FIRST_INDEPENDENT_REVIEW.md)：BJT `[2025-11-14T09:00:00+08:00,2025-11-15T03:05:54+08:00)`，非精确首公开时刻，不用submitted或DOI注册作公开上界。[完整题摘/筛选](ARXIV_SCREENING.md)与[current comments](raw-arxiv-current-signals.xml)保留；本轮没有发现会撤销下述采用的明确撤回/勘误标记，不遍历全版本史。

本文是必要原源实际阅读与作者处置，不是独立验收。未运行artifact、复现实验、实施攻击或修改共享Book。共同性能边界：下列论文结果不授生产SLO/安全保证；未披露的precision、batch、concurrency、SLO、计时重复及完整端到端成本记为 `Not Disclosed`，均不补造；已披露值按各项原协议保留。没有运行性能主张的评价/位置论文，服务SLO不适用；token、调用、rounds等proxy不能冒称wall-clock。

## [Black-Box On-Policy Distillation of Large Language Models](https://arxiv.org/html/2511.10643v1)

实际读[原HTML](raw-v1-10643.html)§2、§3.1/3.3/3.4、A.2/A.3（提取paragraph95–186、285–335、651–655）；2+2+2=6，标准完成。黑盒teacher只提供每prompt一条文本，student generator与由student初始化的scalar discriminator联合更新，teacher>student的BT监督持续针对当前student，而student消费GRPO reward。这是离线teacher文本下的动态reward分支，不是访问teacher logits。

200K清洗LMSYS、GPT-5-Chat teacher、Qwen2.5/Llama学生，warmup1epoch+joint2epochs，batch256，prompt2048/response1536，temperature0.8，约2400steps；Qwen14B为16H100约30小时。评价500LMSYS、500Dolly、252Self-Instruct、80Vicuna、GPT-4o及有限human。冻结/off-policy D在约300步出现约1300-token长度膨胀，而joint设置较稳定，支持局部分布跟随，未证明消除hacking。checkpoint选择明确按最高GPT-4o评分及可接受长度；A.3未给独立选择集身份，故不采用“泛化超teacher”或无选择偏差胜率。toy Gaussian也不证明真实LLM唯一因果。

最终仅报告。实际[TRAIN-RLHF Ch31](../../../../../books/part-04-training-system/31-rlhf.md)“Reward Model也有Policy-relative State”与“Teacher与未来Reward Model都是反馈回路中的状态”已经解释冻结RM/OOD、co-adaptation、独立Gate及teacher成本。本文联合BT/GRPO是具体实现与局部验证，不需改写该设计判断；不是宣称GAD算法逐字已有覆盖。

## [Instella: Fully Open Language Models with Stellar Performance](https://arxiv.org/html/2511.10628v1)

实际读[原HTML](raw-instella-v1.html)§3–5/Table5及§6.1，和[事件差额](INSTELLA_EVENT_DELTA.md)的March/June/Aug原官方核心；2+1+2=5，标准完成。Nov论文不是整个model家族第一次公开，配方/Long/Math/MI300X不能重算新机制。新报告Table5逐seed均值65.5/65.8/65.6对合并66.6保留为局部新验证，不关闭为全族重复。三个stage2同初始化/不同seed，十一benchmark以zero-shot为主，BBH3/MMLU5/GSM8K8-shot；合并相对单seed增加训练预算，未给等总compute单run、独立seed选择或CI，不能授免费集成或无条件稳定收益。

最终仅报告：这是已公开方法新增的限定验证，不是新增长期训练机制；不将整族旧配方补入Books，也不因Books无Instella名称造缺口。v2 submitted不证明本窗公开/重要修订，本次只v1事件差额。

## [SSR: Socratic Self-Refine for Large Language Model Reasoning](https://arxiv.org/html/2511.10621v1)

实际读[原HTML](raw-v1-10621.html)§3、4、Tables3–4与C.2（120–206、581–668、1010–1029）；2+2+2=6，标准完成。把既有CoT分解成question/answer，重复回答子问题、由LLM置信度挑最低步，majority子答案指导保留原trace的修订；Adaptive先Self-Refine，无错/过信时fallback到SSR，Plan额外先改计划。后处理分解不证明原始hidden过程忠实，先前步骤被假定正确也会继承错误。

GPT-4.1-nano/GPT-5-mini，MATH L5、AIME24/25、HLE915数学、Zebra/Sudoku；MathVerify/脚本与非numeric437题GPT-5 judge分开。Table1的LR-Acc为10次重复，LR-Maj@5为50次（5并行样本）；不将该重复数推广至未披露的所有HLE协议。C.2 SSR三轮、Debate两agent三轮、MCTSr四轮，GPT5mini max16384/temp1，nano max16384/temp0.6。相同rounds并非相同调用/token预算；C.2没有确定每子问题重采样M，保留未披露，不能授同成本收益。HLE CoT27.98、Self-Refine26.57、SSR29.61只是该切片；自然反思干预反而降低AIME结果，不能说任何反思都好。

最终仅报告。实际[AGENT-REFLECTION Ch80](../../../../../books/part-07-agent/80-reflection.md)“Verification-centric Reflection”与“有用feedback”明确定位受影响state/claim、局部repair、same-model bias和预算。SSR给出新局部实现验证，但置信选择未取得独立真值、预算未匹配，不改变这些长期选择；不强制将算法名添加正文。

## [Rubric-Based Benchmarking and Reinforcement Learning for Advancing LLM Instruction Following](https://arxiv.org/html/2511.10507v1)

实际读[原HTML](raw-v1-10507.html)benchmark核心、rubric generator/verifier/policy RL、aggregation消融（235–245、294–385、401–432）；2+2+2=6，标准完成。专家逐prompt rubric与所有criteria AND验收，生成器Maverick SFT、verifier5K SFT+14K RL，以expert binary agreement监督；policy用AND reward并额外加入clean/no verbose self-eval及complete/no cutoff两判据防gaming。F1 .515→.656→.728不证明judge获得通用真值，防hack判据是局部措施非安全保证。

1600专家benchmark为LLM失败筛出的adversarial人口，每题最多20 criteria；generator F1 .639→.790。policy三聚合均值58.1/53.6/55.7，但CC fraction64.4高于AND56.4，不能普遍采用AND最好。专家rubric、生成器、verifier及RL预算都非免费；核心未披露全部训练硬件、precision、重复不确定性与生产并发。

最终仅报告。实际[TRAIN-RLHF Ch31](../../../../../books/part-04-training-system/31-rlhf.md)“多目标Reward的Bottleneck聚合不能冒充Hard Constraint”已有分项尺度、不可补偿gate、judge噪声与回退。新AND局部反侧验证保留，不将平均胜出写成硬约束已成立，也不以rubric名称不存在要求整合。

## [Exploring State Tracking Capabilities of Large Language Models](https://arxiv.org/html/2511.10457v1)

实际读[原HTML](raw-v1-10457.html)任务/评测与entity control（38–75、98–135、580–620）；2+1+2=5，标准完成。三个合成任务各50 episodes、depth≤10，3实体与5实体控制，temperature0、regex终态标签、示范及CoT±；GPT3.5/4o、Mixtral8x7B、Llama3 8/70B，不叫2025全部frontier。整数可交换聚合与排列顺序敏感不同，不能只按depth归因Transformer容量。

更多entity随机问询可能选到未被更新对象，从初态直接作答；state-dependent query对照更难，提供“规模更大未必难”的具体generator捷径。response长度相关不能证明内在CoT causal，跨model/backend也不能归因规模。只采该受控反侧，不授状态追踪普遍不可能。

最终仅报告。实际[PLATFORM-EVALUATION-SYSTEM Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“任务难度切片”正文L124–128已经要求输入规模、binding arity、operand难度及oracle分别变化。新实体未更新捷径是有价值的局部验证，但不需要改写此长期generator分账原则。

## [Position: On the Methodological Pitfalls of Evaluating Base LLMs for Reasoning](https://arxiv.org/html/2511.10381v1)

实际读[原HTML](raw-v1-10381.html)§5–7（246–335），不仅读position摘要；2+1+2=5，标准完成。7600有效IOI/IH模板与7600最小非法模板、20 name pairs×380 predicate pairs、13个0.5–32B base模型，A100/vLLM/temp0，测定指定答案prefix/fullstop。两类差异可揭示prompt完成的有效性检查盲区，而不仅重复“预训练目标不同”成熟提醒。

有效/非法表现相近与语言pattern解释相容，但E1–6 toy circuit只是说明性示范，不是原模型实测唯一因果；Gemma3-1B局部输出“不相关”亦影响exact-match。不能从模板结果推出base无推理、instruction必然有推理或真实circuit已定位。有限任务、混合数据目标与输出解释限制保留。

最终仅报告。实际Ch66“从目标到证据”的EvalSpec target/eligible population/scorer与proxy边界能承载长期设计判断；本次新增局部invalid-template反侧留报告，不把作者的排他性内部机制解释整合成事实。

## [Rectify Evaluation Preference: Improving LLMs' Critique on Math Reasoning via Perplexity-aware Reinforcement Learning](https://arxiv.org/html/2511.10303v1)

实际读[原HTML](raw-v1-10303.html)OPS、Eq4–8、§Experiments/消融（35–174、175–181、400–433）；2+2+2=6，标准完成。固定相同问题/最终答案、三模型不同process，分正确/错误truth组再按prediction组以ppl或逆ppl缩放GRPO advantage，并对两个truth类别非零loss分别取均值。新增是来源风格混杂的诊断及counter-preference探索，不是低ppl为正确的机制。

MATH train5760、三模型均衡，PRM72B首错阈值0.8为proxy；Qwen2-7B/Llama3.1-8B/Mistral7B，8A10080GB/bfloat16，400steps/batch128/5rollouts/temp1，evalgreedy。checkpoint每50按OPS和ProcessBench最佳均值选择，不能授独立heldout泛化。BI=FPR−FNR，BI0仍可双边高误差；消融去ppl使BI更小却accuracy下降，证明balance不能代替correctness。表值和作者11/15切片收益不等普遍更好，SFT/PRM监督预算也不同。

最终仅报告。实际Ch66 L273–275“三测量对象/质量匹配”及Ch31独立Evaluation/response style已要求来源、代理和正确性分账。本文ppl modulation为数学critic具体实现，有限结果尚不足把它选为通用修复，保留新反侧与选择泄漏限制，不造长期缺口。

## [MTR-DuplexBench: Towards a Comprehensive Evaluation of Multi-Round Conversations for Full-Duplex Speech Language Models](https://arxiv.org/html/2511.10262v1)

实际读[原HTML](raw-v1-10262.html)§3–4、IF/safety/latency（142–216、429–500），paragraph147完整重读；2+2+2=6，标准完成。Whisper-medium/Silero VAD→GPT4o内容/时刻分轮，六次segmentation，≥30%时间重叠聚类、中位边界及最终重叠合并，构造多轮full-duplex条件评价。§3.1 turn segmentation/dialogue-quality分支前assistant历史使用真值、评current user start→nextuser end，mute nextuser；该分支是teacher-forced历史诊断，不是闭环自生成累积错。§3.2.2–3.2.4另有synthetic feature/IF/safety协议，本次未核代码证明它们均teacher-forced，不推广上述历史限制。

Candor200×120秒、synthetic200×10轮GPT4o/CosyVoice2，IF300抽100×10，AdvBench520抽100×10；初版仅Moshi。Table6 IF正常68→41.9、打断69→42.3及Table7拒绝90→91，均为累计1至1–10轮平均而非第10轮单点。不能由相似IF下降归因打断独有效；拒绝不降亦不支持全部能力随轮次坏。转录/judge/合成voice/分段有共同proxy误差，时延按轮观察不授生产SLO；硬件/precision/并发与重复CI在采用核心未给出。

最终仅报告。实际Ch24 teacher-forcing与生成滚动误差正文、Ch66测量人口/执行环境要求已经区分给定历史和真实输出。该多维协议是局部新验证，不把初版单模型曲线提升为新通用状态退化律。

## [VocalNet-M2: Advancing Low-Latency Spoken Language Modeling via Integrated Multi-Codebook Tokenization and Multi-Token Prediction](https://arxiv.org/html/2511.10232v1)

实际读[原HTML](raw-v1-10232.html)§2–4/Tables2–3/latency（62–84、152–241）；2+2+2=6，标准完成。八XY codebook并行track、Qwen3-8B Thinker/WhisperLargeV3、text+hidden融合与3×upsampling、Talker直接预测声学码免flow-matching；MTP训练预测未来ticks。10K小时Emilia、800K/7K小时dialogue及100K合成，EnglishOpenAudioBench/Qwen-max内容、Whisper WER、UTMOS。

Table2多codebook去pretrain后WER20.49/UTMOS3.89，emilia+v2为8.56/4.24；single+flow为3.68/4.37但firstchunk更慢，直接声学建模更敏感训练数据，不是双轴无损胜出。Table3 MTP**推理不使用**，4层WER6.07、5层6.33非单调；§4.4同时改codec/MTP的725→348ms不证明单独MTP造成2×。L20/官方streaming且无加速框架、firstchunk约0.8秒与拆分substage应分别记；未匹配所有模型生成路径、完整utterance/并发/SLO不能外推。

最终仅报告。实际[MULTIMODAL-GENERATIVE-PARADIGMS Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)AR的factorization、serial depth、teacher forcing/生成质量与成本共验已承载决策。新增codec/data成本反侧保留，未取得足以改写通用生成选择的孤立MTP因果，不强造Book缺口。

## [EffiReason-Bench: A Unified Benchmark for Evaluating and Advancing Efficient Reasoning in Large Language Models](https://arxiv.org/html/2511.10201v1)

实际读[原HTML](raw-v1-10201.html)§3.1–3.5/Eq1–2及§4.4–5（86–116、286–309、818–841），只为较强metric断言深入公式；2+2+2=6，标准完成。六Qwen/Llama1–70B、7方法含CoT基线、GSM8K/MATH500/CSQA/LogiQA；CS/Logic注释双人审，统一Final Answer、固定seed示例，train-free/train-based、noise/transfer分别评价。新局部反侧是TokenSkip在Qwen MATH失效、CoD压缩退步和shot/transfer交互，不是普遍最优方法。

E3使用accuracy odds ratio和T0/T，默认w=A0、rho=-1。作者“效率不能补偿accuracy下降”被直接反例否定：A0=.5，A=.9/1.9=.473684，r_acc=.9，r_tok=10，E3=1/(.5/.9+.5/10)=1.651376>1。该实际算术核只反驳不可补偿保证，不宣称Theorem1灵敏度界错误；不采用未另核的定理。output token proxy未覆盖prefill、并行、训练与search总预算，所谓统一prompt不等全成本公平。

最终仅报告。实际Ch66 L49–76的AND quality gate及L78–108 EvalSpec明确目标、proxy/decision边界；新E3反例在报告阻止错误采用，既有Book没使用该metric，无需改书。局部比较继续有效，不把整篇因一断言关闭。

## [GraphIF: Enhancing Multi-Turn Instruction Following for Large Language Models with Relation Graph Prompt](https://arxiv.org/html/2511.10051v1)

实际读[原HTML](raw-v1-10051.html)Methodology/Rewrite、实验/消融（110–144、342–395、442–515）；2+2+2=6，标准完成。交替Action Identification/Execution，notebook保存已抽关系，再把global/context-anchored/modify/summary/topic及具体turn转prompt、重写原答案。Done是LLM提案，不认证所有约束已抽到。

MT-Eval*/StructFlowBench*手工合并验证为>20轮，五instruction models，GPT4o judge+human verification，4A80080GB/temp.7/top-p.8/top-k20，三run平均。去iterative extraction或去关系解释退步支持局部组合；前者调用减少、后者prompt内容改变，未等calls/tokens证明graph结构唯一原因。MemoryBank/MemoChat有限实现输不证明所有memory无效。新global/跨轮constraint差额保留，但增加抽取、生成及rewrite成本，未给CI/SLO。

最终仅报告。实际[AGENT-CONTEXT Ch75](../../../../../books/part-07-agent/75-context.md)L534–563已有scope/expiry/source、typed dependency graph、scoped patch与validator/commit。GraphIF是未持有authority的文本辅助新分支，不应把它当上述真实state owner的替代；局部效果不需改写执行约束长期链。

## [ScaleFormer: Span Representation Cumulation for Long-Context Transformer](https://arxiv.org/html/2511.10029v1)

实际读[原HTML](raw-v1-10029.html)§3.1–3.5、§4.1–4.2及§5（65–113、263–317、385–400）；2+2+2=6，标准完成。overlap chunks并行encoder、首尾boundary累积前后均值再alpha融合，随机middle samples进入decoder，不增加参数却不可回读全部隐藏token。forward context依赖未来chunk，不能当causal streaming。

BART/T5-base、SummScreen约9K、GovReport截16384、BookSum约140K平均，L1024/O150/k1/m300，alpha .5在dev选择；ROUGE/BERTScore限定summary。BART SummScreen dev两极alpha坏、middle0为19.3→300为20.1，更多middle/overlap不继续好。硬件、precision、batch、重复/CI与实测E2E未披露。O(NL)encoder在L固定成立；整个decoder若output长度T增长，cross-attention O(TN)、self-attention O(T²)，不能从压缩input线性证明无条件全系统线性。本次只采用固定预算下的有损span分支，不采无限长/无损/SOTA普适。

最终仅报告。实际[MODEL-LONG-CONTEXT Ch22](../../../../../books/part-02-model/22-long-context.md)L994–1012已有compact aggregation丢原文/provenance、任务专用state与raw fallback；ScaleFormer给出限定encoder-decoder表示实现，不能把浮点边界均值视为已证明通用可组合语义，保留新局部结果而不扩Book。

## [NumPert: Numerical Perturbations to Probe Language Models for Veracity Prediction](https://arxiv.org/html/2511.09971v1)

实际读[原HTML](raw-v1-09971.html)§3–4、§5–6/8（90–149、483–518）；2+1+2=5，标准完成。QuanTemp真实claim/evidence，去summaries与Conflicting类、数字规范化和人工审扰动，分别label-preserving/label-flipping，不把两类结果合并。相同数字换字形、近似/range、随机替换与负号，有可识别局部失效因子；不是仅领域指标改善。

原260True/604False，NegNum T→F仅51，六probe人口不同；open Ollama Q4_K_M、官方固定API版本/temp0/JSON，Gemini thinking8192与默认不同，不归因model规模。PAP可改进flipped却伤preserving，表现与prompt/label交互。Mask把缺数字判False而不是Unknown是协议选择，不以此推广全部数学能力失败；长reasoning与错相关、样例误读不能证明overthinking因果。忽略False→True、污染可能、小切片与runtime未披露保留，不采用“62%”不绑定具体cell的headline。

最终仅报告。实际Ch66 EvalSpec failure taxonomy/eligible population与配对测量边界可承载长期决定；本文数字/符号局部probe支持受限诊断，不增加新的通用真实性判据或算法保证。

## [REAP: Enhancing RAG with Recursive Evaluation and Adaptive Planning for Multi-Hop Question Answering](https://arxiv.org/html/2511.09966v1)

实际读[原HTML](raw-v1-09966.html)SP/FE/Eq6–9、实验、消融与成本附录（30–159、308–363、464–469、776–813）；2+2+2=6，标准完成。structured id/query/dependency plan；FE给statement/evidence/reasoning/fulfillment；DirectAnswer走轻updater，Partial/Failed先判证据充分性再局部修query或prune/replan。union facts的文本依据不认证冲突已解决。

Hotpot/2Wiki各500验证样本，MuSiQue500、Bamboogle125，Llama3.1-8B、e5-large-v2 top5/KILT约360K、multi-round最多5。GPT4收7000后成功+<13000字符筛成5556；三类planning合训与FE/synth另训，LoRA lr1e-4/cutoff5000，8L40 48GB约8h。去replan/verify/clue局部F1退步，但训练与baseline checkpoints/teacher不全等资源。85%routine可用1B updater为条件路由观察。Table4只统计**正确结果**轮数，REAP2.19/2.52/2.76/2.48不能当全人口成本，且Search-R1轮数更少；不授真正低latency或所有事实可靠。

最终仅报告。实际[AGENT-PLANNING Ch79](../../../../../books/part-07-agent/79-planning.md)L137–178已有按observation区分执行失败/计划不可行、局部修改与plan version；[Ch76](../../../../../books/part-07-agent/76-rag.md)保留retrieval/packing/generation整链质量。REAP具体路由与少数任务验证不改变这些设计判断，未证明需要新增长期知识链。

## 最终作者范围与独立回接

本14项加Ohm已通过两项，16个家族均标准必要Evidence与作者Books判断到位；没有通过访问受阻、深审费时或Book主题相似缩池。全部最终仅报告，各有实际具体正文/事件差额与不能改变长期决定的理由，不宣称16算法已有覆盖。未提出共享Books写锁、未改Books，无POST普通待办。[Ohm最终DAY](DAY_INDEPENDENT_REVIEW.md)已实际核全部16项必要Evidence/OnlyReport与十四来源有限内容。作者2026-10-04T19:55:59+08:00按其notes修本文SSR次数、MTR分支与累计表，最终DAY仍待四处变化回核，不自授完成。
