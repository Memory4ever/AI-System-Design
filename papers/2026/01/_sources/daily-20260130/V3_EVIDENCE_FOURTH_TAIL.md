# 2026-01-30 第四批尾部必要证据

作者实际读取以下精确v1的必要方法、评价与直接反侧；root已实际核必要命题与Only边界。不运行代码，不由笔记自身授整日Gate；实际日级结论另见本日README。

## [AgentLongBench / 2601.20730](https://arxiv.org/pdf/2601.20730v1)

2+2+2=6。HTML未提供正文，必要官方PDF；本地`V3_CORE_2601.20730_PDF.txt`保留main原源web行号，§2–4/P3–9实际已读；定点Appendix E/P23原源L666–681已读。环境为有限Pokémon属性与确定性oracle，rule-based轨迹离线拼接成问答，不是模型真实online执行整个4M-token交互。Knowledge-Free用实体/属性符号替换，减少参数知识线索，不证明消除所有结构偏差。Concise工具已经求交，Verbose分别列属性候选、由模型求交；同token长度又意味着不同回合数，因此二者不是只改变密度而固定计算要求/时间跨度的因果控制。

800题/长度32K至4M，模型native窗口/API各异；工具与环境Recall、intersection/weighted-sum任务分别评价，不把ACL当普遍记忆容量。Table2的GPT4.1 128K比较仅局部作者成绩：concise与verbose在Environment/Tool任务并非统一优劣。外部记忆都用Qwen3-30B-A3B-Instruct-2507，Appendix E写公共默认配置、retrieval top-k=5、temperature .7，开源H200/vLLM、闭源官方API；硬件数量、精度、concurrency/端到端成本、重复CI Not Disclosed。“all inference vLLM”与闭源API措辞不能当统一执行路径证明。作者的稀疏检索断开集合依赖解释在该top5条件下合理，不证明任何外部记忆架构皆失败。

仅报告：确定环境与轨迹序列可使检索/跨轮状态指标分开，但本稿concise/verbose有算法难度与回合混杂、defaults/top5仅一局部memory使用条件，不把‘动态轨迹’术语扩为普遍agent-memory否定。

## [FLORES contamination / 2601.20858](https://arxiv.org/html/2601.20858v1)

2+2+2=6，设计反侧深入。§2/3物理82–112、§4/限制163–190，Appendix C/D381–401：FLORES200 dev997、15语言、Bloomz7.1B与Llama3.1-8B。Bloomz已披露含FLORES训练，Llama只是无报告使用，不是经证明clean control。BLEU被明确当词形重合诊断、COMET语义指标，80BLEU/.9COMET等阈值不是严格membership证明。目标侧高分、异语源/回译/改写仍可召回目标；另语料Tamil/Malayalam/Odia near-zero支持泛化不足，也含语料分布差。Aya实体替换降低5–20BLEU，但作者承认词形屈折与实体数量改变会混杂。

控制实验把Llama按eng↔11语言FLORES三epochs训至严重memorization，再测所有方向；未训练方向BLEU可升16且COMET降，支持此人为强记忆配置的跨方向指标污染，不证明内部激活机制或所有pretrain污染。Appendix参数seq512、microbatch4/accum8、AdamW5e-6、bf16 ZeRO3、一个A10080GB、总体约30GPUh，重复/CI Not Disclosed。仅报告：不能把source-language未见/方向未训当target-text清洁保证；局部强污染实验与主张clean-control的证据缺口均保留，尚不外推模型大小/真实pretrain污染率。

## [P2S / 2601.20649](https://arxiv.org/html/2601.20649v1)

2+2+2=6。§3物理127–179，§4/appendix336–351、631–647：ground-truth answer条件生成GoldCoT，过滤think/answer格式后按答案似然选；不是独立验证每步逻辑。prefix等步切分后看gold suffix最大条件概率减maskprefix基线，末步直接答案概率，sigmoid/late weighting与ROUGE混合。内部probability差只是一种process代理，错误但高似然路径、替代正确推理可能被错误排序，不授causal faithfulness。每题K+m² forward，不是免费verifier-less，也需要answer标注。

Qwen2.5-1.5B、2H80080GB、bf16/FA2/TRL、lr3e-6、batch256、4samples、500steps、SFT3epochs/seed42、prompt1024/completion2048；DROP10k/2k限定问题/答案长度，MedicalQA仅方法评价域，不纳入医学应用链。DROP ROUGE70.70vs68.40，GoldCoT filter/PFR局部消融；Claude4Sonnet/GPT4o/1.5B verifier平均分不是human truth，输出150vs60token的代价也在收益旁。重复train CI/服务batch及SLO未披露。仅报告：局部answer-conditioned评分接口改变哪些步骤得到学习信号；尚无足以长期采用为可靠process监督的独立正确性保证。

## [MathForge / 2601.20614](https://arxiv.org/html/2601.20614v1)

2+2+2=6。§3物理128–238、实验540–560/640–668、Appendix B.2 1128–1139、F1211–1265：非uniform reward组以mean absolute deviation归一，sum|adv|=G在非零分母下是代数恒等；GRPO binary对应2G√p(1−p)。但实际gradient含logprob gradient、clipping/importance/length等，B.2明确它仅在响应梯度范数相近、方向少抵消假设下是proxy而非相等。不能把等优势总量说成每题实际梯度必相等。difficulty weight以valid query平均reward加softmax T2，权重比例有exp(.5)≈1.65范围，不是无限硬题优先。

MQR用o3生成背景/术语/嵌套子问题，要求保答案，22.5k约$184为额外数据生成成本；不是机械证明全部答案仍正确。原数据多epochs与变体少epochs是train-volume对照，不含o3生成的全算力。Table9 MQR有lr5e-7→1e-6、accum1→4等变动，不能把全部增益纯归因题改写；DAPO/GPG resampling禁用为本实验基准而非各方法全配置。Qwen2.5Math7B/1.5B、Qwen3B、DeepSeekMath7B（80k NuminaCoT cold start），train temp1/output1024、batch32/8rollout；evaltemp.6/top-p.95/output4096，AIME/AMC32gens、其他4/GeoQA greedy；多生成不是多训练seed。DGAE+.94/DQW+1.14平均局部，无主表training CI。仅报告：具体归一与预算有可控选择，但实际梯度proxy前提、生成问题有效性与学习率混杂不允许普遍difficulty balancing保证。

## [EMB-S / 2601.20276](https://arxiv.org/html/2601.20276v1)

2+2+2=6。§3物理248–306、实验527–561：326M tokens/160,280 docs/9datasets是MemoryBank证据池；39,860→9,621→3,457→882→483筛选并非483独立随机题。query-answer-reference三元组人筛、单/多hop改写，用Qwen3Emb8B mining与collision test把conflict排、hard negative保、false negative加入reference。LLM-verified集合并非独立全库gold truth，retriever mining会产生偏差。

固定query ladder：64K各domain gold refs、128/256K加其他域、512K共享、1M至326M继续加distractors；尺度/域混合共同变，不单独证明每一点退步来自semantic interference。RAG top10 R@1/SR(any)/FR(all)测access；native fullcontext QA仅其fits窗口至1M、Grok judge0–5测use，两协议不同，不能作为相同总预算的RAG对native优劣。QwenEmb8B SR .93→.682/FR .80→.304，rerank到.745/.400仅其检索配置；Gemini3P QA3.55→3.28非通用质量定律。没有326M输入模型或硬件/latency/concurrency/CI披露。仅报告：固定reference与near-miss负例可揭开access/use差异，但小483、mining/judge和混合尺度条件不授普遍326M agent可行性或新retrieval定理。

## [TRACE / 2601.20103](https://arxiv.org/html/2601.20103v1)

2+2+2=6，安全深入。§3物理116–153、§4/5 153–207、Appendix H807–826：ClaudeOpus4.5按10类taxonomy合成trajectory，最终517（249benign）/54任务/37software contexts，平均26utterances。三位日常用coding agents的fullstack engineers独立标合理性/hack种类/难度，81%acceptance、binary κ=.82支持注释一致性与情景现实性，不是实际运行全部攻击/验证causal rewardhack。39%多标签；用户接受中断操纵可误导detector，本身为细粒度语义反侧。

isolated与cluster(N1/5/10，benignratio.25/.5/.9)匹配模型和三seed42/7777/9999；reasoning high/temp1或10k budget、host8H200/Fireworks配置。Detection macroF1，Match multilabelF1以检测成功/groundtruth条件计，是judge对taxonomy标签一致性而非攻击发生率。GPT isolated约45%/cluster约63%仅该任务score，不写生产accuracy；‘all statistically significant’没有在采用部分给完整paired检验，不能无条件背书。语义类比表面语法类更难，self-awareness/user acceptance均可能误判；人为taxonomy合成与cluster比例决定上下文，未证明部署多agent真实效果。仅报告：contrasting trajectory context能改变检测可靠性，作者结果仅支持这份合成+人筛评价的输入条件，不授现实rewardhack自动发现或安全保证。
