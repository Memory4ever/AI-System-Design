# 2026-04-25 自然日来源遗漏补充

作者：supp_apr25_author_fresh；只补2026-04-24北京时间自然日。原1候选整行、原日期评分、旧09:00小时窗及连续原§4冻结；baseline-before-supplement-20261016.md为运行前非覆盖快照。root为非作者准入/必要Source/Books PRE-POST/DAY/FINAL复核者，作者不自授通过。唯一补查记录；不写LS/index、不stage/commit/push。

## A1 启动与最小发现范围

完整重读AGENTS、当前研究/Report合同、来源Daily14与arXiv主题路由、统一Prompt、ROADMAP及LS April最新路由。使用using-agent-skills与daily-research-closure以限制证据复用和完成断言。旧Kimi1.39.0精确release/tag/Ch84真实POST仅按采用命题未变复用，不重计新候选。旧arXiv按09:00边界排除Apr24早间批次，现自然日补差额；旧221xx–230xx缓存不自动作为当窗候选池。旧DeepSeek仅小时交界隔离可重开日级资格，但June技术报告不倒填April公开。

实际查询：`https://export.arxiv.org/api/query?search_query=submittedDate:[202604221800 TO 202604231800] AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")&start=0&max_results=350`。submitted范围仅发现常规Apr24批次线索，不能单独证明公开日期。API total214；首次长响应被执行输出上限截到92条，未将其当完整覆盖，后续将分页补取。官方month canonical `/list/cs.CL/2026-04`可读而`/2604`404；大响应只作标题线索，不将整类排成逐项审阅队列。公开日期仍待官方列表位置/处理元数据联合资格及相邻批次有界核验。

## A2 首批完整题摘与独立准入待校准

### 2604.21330 — Teacher-Guided Routing for Sparse Vision Mixture-of-Experts

原始入口：http://arxiv.org/abs/2604.21330v1；本次API完整题摘（当前entry均v1）。尚未核公开日/必要Source，不预授评分或Books。

> Recent progress in deep learning has been driven by increasingly large-scale models, but the resulting computational cost has become a critical bottleneck. Sparse Mixture of Experts (MoE) offers an effective solution by activating only a small subset of experts for each input, achieving high scalability without sacrificing inference speed. Although effective, sparse MoE training exhibits characteristic optimization difficulties. Because the router receives informative gradients only through the experts selected in the forward pass, it suffers from gradient blocking and obtains little information from unselected routes. This limited, highly localized feedback makes it difficult for the router to learn appropriate expert-selection scores and often leads to unstable routing dynamics, such as fluctuating expert assignments during training. To address this issue, we propose TGR-MoE: Teacher-Guided Routing for Sparse Vision Mixture-of-Experts, a simple yet effective method that stabilizes router learning using supervision derived from a pretrained dense teacher model. TGR-MoE constructs a teacher router from the teacher's intermediate representations and uses its routing outputs as pseudo-supervision for the student router, suppressing frequent routing fluctuations during training and enabling knowledge-guided expert selection from the early stages of training. Extensive experiments on ImageNet-1K and CIFAR-100 demonstrate that TGR consistently improves both accuracy and routing consistency, while maintaining stable training even under highly sparse configurations.

拟准入：稀疏router只获已选路径梯度→dense teacher中间表示产生pseudo routing监督→重新考虑route稳定性是否必须靠负载正则。仅局部vision实验证据潜力，不外推LLM。

### 2604.21215 — The Recurrent Transformer: Greater Effective Depth and Efficient Decoding

原始入口：http://arxiv.org/abs/2604.21215v1；本次API完整题摘（当前entry均v1）。尚未核公开日/必要Source，不预授评分或Books。

> Transformers process tokens in parallel but are temporally shallow: at position $t$, each layer attends to key-value pairs computed based on the previous layer, yielding a depth capped by the number of layers. Recurrent models offer unbounded temporal depth but suffer from optimization instability and historically underutilize modern accelerators. We introduce the Recurrent Transformer, a simple architectural change where each layer attends to key-value pairs computed off its own activations, yielding layerwise recurrent memory while preserving standard autoregressive decoding cost. We show that the architecture can emulate both (i) a conventional Transformer and (ii) token-to-token recurrent updates under mild assumptions, while avoiding optimization instability. Naively, prefill/training appears bandwidth-bound with effective arithmetic intensity near $1$ because keys and values are revealed sequentially; we give an exact tiling-based algorithm that preserves the mathematical computation while reducing HBM traffic from $Θ(N^2)$ to $Θ(N\log N)$, increasing effective arithmetic intensity to $Θ(N/\log N)$ for sequence length $N$. On 150M and 300M parameter C4 pretraining, Recurrent Transformers improve cross-entropy over a parameter-matched Transformer baseline and achieve the improvement with fewer layers (fixed parameters), suggesting that recurrence can trade depth for width, thus reducing KV cache memory footprint and inference latency.

拟准入：层间浅时间深度/普通recurrent难并行→自身activations构KV与exact tiling→需要权衡temporal depth、prefill带宽和KV开销。

### 2604.21523 — Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models

原始入口：http://arxiv.org/abs/2604.21523v1；本次API完整题摘（当前entry均v1）。尚未核公开日/必要Source，不预授评分或Books。

> Large Vision-Language Models (VLMs) are increasingly used to evaluate outputs of other models, for image-to-text (I2T) tasks such as visual question answering, and text-to-image (T2I) generation tasks. Despite this growing reliance, the reliability of these Evaluator VLMs remains under explored. In this work, we systematically evaluate the reliability of Evaluator VLMs across both I2T and T2I tasks. We introduce targeted perturbations that degrade output quality along key error dimensions, including object hallucinations, spatial reasoning, factual grounding, and visual fidelity. These perturbations test whether Evaluator VLMs can reliably account for these quality degrading errors in their evaluations. Using a comprehensive benchmark of over 4000 perturbed instances spanning 40 perturbation dimensions, we evaluate 4 prominent VLMs using single-answer scoring, pairwise comparison, and reference-guided paradigms. Our findings reveal that current VLM evaluators exhibit substantial blind spots: they often fail to detect perturbed outputs - in some cases exceeding 50%, struggle particularly with fine-grained compositional and spatial errors, and are often insensitive to hallucinated content that contradicts the input image. Pairwise comparison proves more reliable, though failure rates persist. These results highlight the unreliable nature of current Evaluator VLMs and urge caution in their deployment for benchmarking and development decisions. Code and data have been made publicly available.

拟准入：VLM judge分数默认表征质量→定向退化扰动揭露视觉细粒度盲点及pairwise边界→评价协议需重考，不是新增榜单。

### 2604.21882 — Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms

原始入口：http://arxiv.org/abs/2604.21882v1；本次API完整题摘（当前entry均v1）。尚未核公开日/必要Source，不预授评分或Books。

> Understanding what kinds of factual knowledge large language models (LLMs) memorize is essential for evaluating their reliability and limitations. Entity-based QA is a common framework for analyzing non-verbatim memorization, but typical evaluations query each entity using a single canonical surface form, making it difficult to disentangle fact memorization from access through a particular name. We introduce RedirectQA, an entity-based QA dataset that uses Wikipedia redirect information to associate Wikidata factual triples with categorized surface forms for each entity, including alternative names, abbreviations, spelling variants, and common erroneous forms. Across 13 LLMs, we examine surface-conditioned factual memorization and find that prediction outcomes often change when only the entity surface form changes. This inconsistency is category-dependent: models are more robust to minor orthographic variations than to larger lexical variations such as aliases and abbreviations. Frequency analyses further suggest that both entity- and surface-level frequencies are associated with accuracy, and that entity frequency often contributes beyond surface frequency. Overall, factual memorization appears neither purely surface-specific nor fully surface-invariant, highlighting the importance of surface-form diversity in evaluating non-verbatim memorization.

拟准入：entity QA单canonical名字混合知识与访问→同实体多surface受控比较→non-verbatim记忆结论应拆存储/名称访问，可能改变测量解释。

### 2604.21478 — Rethinking Cross-Domain Evaluation for Face Forgery Detection with Semantic Fine-grained Alignment and Mixture-of-Experts

原始入口：http://arxiv.org/abs/2604.21478v1；本次API完整题摘（当前entry均v1）。尚未核公开日/必要Source，不预授评分或Books。

> Nowadays, visual data forgery detection plays an increasingly important role in social and economic security with the rapid development of generative models. Existing face forgery detectors still can't achieve satisfactory performance because of poor generalization ability across datasets. The key factor that led to this phenomenon is the lack of suitable metrics: the commonly used cross-dataset AUC metric fails to reveal an important issue where detection scores may shift significantly across data domains. To explicitly evaluate cross-domain score comparability, we propose \textbf{Cross-AUC}, an evaluation metric that can compute AUC across dataset pairs by contrasting real samples from one dataset with fake samples from another (and vice versa). It is interesting to find that evaluating representative detectors under the Cross-AUC metric reveals substantial performance drops, exposing an overlooked robustness problem. Besides, we also propose the novel framework \textbf{S}emantic \textbf{F}ine-grained \textbf{A}lignment and \textbf{M}ixture-of-Experts (\textbf{SFAM}), consisting of a patch-level image-text alignment module that enhances CLIP's sensitivity to manipulation artifacts, and the facial region mixture-of-experts module, which routes features from different facial regions to specialized experts for region-aware forgery analysis. Extensive qualitative and quantitative experiments on the public datasets prove that the proposed method achieves superior performance compared with the state-of-the-art methods with various suitable metrics.

代表EX：face forgery detector跨数据score comparability及patch/region MoE用于领域检测，未说明大模型/基础系统主线机制改变；不因MoE关键词准入。

### 2604.21104 — Pretrain Where? Investigating How Pretraining Data Diversity Impacts Geospatial Foundation Model Performance

原始入口：http://arxiv.org/abs/2604.21104v1；本次API完整题摘（当前entry均v1）。尚未核公开日/必要Source，不预授评分或Books。

> New geospatial foundation models introduce a new model architecture and pretraining dataset, often sampled using different notions of data diversity. Performance differences are largely attributed to the model architecture or input modalities, while the role of the pretraining dataset is rarely studied. To address this research gap, we conducted a systematic study on how the geographic composition of pretraining data affects a model's downstream performance. We created global and per-continent pretraining datasets and evaluated them on global and per-continent downstream datasets. We found that the pretraining dataset from Europe outperformed global and continent-specific pretraining datasets on both global and local downstream evaluations. To investigate the factors influencing a pretraining dataset's downstream performance, we analysed 10 pretraining datasets using diversity across continents, biomes, landcover and spectral values. We found that only spectral diversity was strongly correlated with performance, while others were weakly correlated. This finding establishes a new dimension of diversity to be accounted for when creating a high-performing pretraining dataset. We open-sourced 7 new pretraining datasets, pretrained models, and our experimental framework at https://github.com/kerner-lab/pretrain-where.

代表EX（root实际完整题摘校准后收准）：遥感数据的人口/光谱多样性影响领域下游指标，未给当前LLM/多模态主线通用设计增量；不把全部geospatial foundation架构一律等同暂缓Science。

### DeepSeek-V4 Preview — 官方日级事件重开

原始：https://deepseek.com/en/news/v4-preview/；本次实际打开官方News原文标April24,2026。核心说明为token-wise compression + DSA、1M默认上下文、Pro1.6T/49B active及Flash284B/13B active、API新modelID与旧alias迁移；现页链接June report不证明当时报告已公开。拟准入最小命题：百万上下文发布将压缩attention与稀疏访问结合，改变仅增context上限的效率解释；先核当次可获得artifact及披露程度，不能以宣传数字证明端到端成本/质量。必要证据不足可仅报告或对中心命题隔离，不能全论文一刀切争议。

待root实际首批准入校准，其他有限发现与明显范围EX可以继续。

## A3 首四公开日与必要轻量说明

本次实际取官方current abs、arXiv官方2026-04月分类列表及arXiv的DataCite publisher feed。月列表本身无日标题，只作身份/批次线索；official announcement中moderation和ID assignment门、v1处理日、created/registered及相邻Apr23/Apr27批次共同支持Apr24 arXiv公开自然日，不把Submitted当公开日，不声称全网first-public已完全排除。当前四页均v1，未见withdrawn/retracted/erratum/corrigendum/corrected阳性；不因此遍历版本史。

- [2604.21330](https://arxiv.org/abs/2604.21330)；publisher projection `{"created":"2026-04-24T01:54:52.000Z","registered":"2026-04-24T01:54:53.000Z","dates":[{"date":"2026-04-23T06:34:10Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:27:30Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"version":"1"}`。
- [2604.21215](https://arxiv.org/abs/2604.21215)；publisher projection `{"created":"2026-04-24T01:52:09.000Z","registered":"2026-04-24T01:52:10.000Z","dates":[{"date":"2026-04-23T02:12:58Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:18:34Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"version":"1"}`。
- [2604.21523](https://arxiv.org/abs/2604.21523)；publisher projection `{"created":"2026-04-24T01:59:24.000Z","registered":"2026-04-24T01:59:25.000Z","dates":[{"date":"2026-04-23T10:36:50Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:40:50Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"version":"1"}`。
- [2604.21882](https://arxiv.org/abs/2604.21882)；publisher projection `{"created":"2026-04-24T02:07:50.000Z","registered":"2026-04-24T02:07:50.000Z","dates":[{"date":"2026-04-23T17:25:32Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T01:02:32Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"version":"1"}`。

## A4 RedirectQA 21882v1 必要Source与唯一owner逐字PRE（待独核）

采用精确[HTMLv1](https://arxiv.org/html/2604.21882v1)，本次实际§2.1–2.3、§3.1–3.2/Fig2、§4.1–4.4/Table2、Limitations与直接反侧B.2/B.4/B.5。2+1+2=5；因Ch5具体长期gap作必要深入，不把成熟记忆/访问分离原则或Books决定加分。

机制与对照：Wikidata固定subject/relation/object，Wikipedia redirects只改变subject名字；手选33个有效surface类型，剔除歧义label及无pageview事实，约30k surface instances，canonical14,672并不等于独立样本总量。13models含Pythia410M/2.8B/6.9B/12B，OpenSciRef0.4/1.7B，OLMo2 Stage1的1/7/13/32B，Qwen3-30B-A3B-Instruct、Llama3.1-8B-Instruct、gpt4omini20240718。local8bit、15shot其他关系canonical固定seed、max15tokens/firstline；APItemperature0/top-p1/max100，故非推理runtime速度/硬件benchmark，hardware/concurrency/SLO=Not Disclosed。alias-aware stringmatching仍可能漏可接受答案。canonical↔redirect双向correctnessflip，不把bothwrong一致当可靠。B.2第二template定点复核支持非单一模板artifact；不声称全问法/全语言。

频率分析是透明模型限定：Pile全约300B与OLMoMix1124随机10%文档，Spotlight实体链接/精确surface span计数，去零频后只剩4,284 surface/2,112 triples或4,356/2,147。§4/Table2 entitypartialcorr控制surface仍正、canonicalsurface控制entity常近0；B.4去掉surface<=10仍有entity信号。频率相关与linearpartial不是训练因果，entity-link质量、选样/coverage、Wikimedia英语偏差均限制。B.5 Pythia12B balancedaccuracy .522及negative更易，未直接内部表示/机制定位。证据支持“行为访问对surface部分敏感，不能从canonical失败反推事实未存”，不证明模型存储唯一entityID，不证明多alias一定恢复或适用于多语言/对象变化。

唯一owner：`WORLDVIEW-REPRESENTATION` Ch5。实际旧“记忆与泛化”已有coverage failure/compression distortion与其条件下rate-distortion，后文另有知识是否保存/路由访问/repair分离，linearreader合同和参数知识访问策略；不足以承载同一entity-fact、不同名字双向flip及canonicality不等可访问性的具体诊断。拟只在现rate-distortion段（source-family2609-12111）之后、原“判断泛化必须回到未见数据和部署分布”之前补两段，不重复重述一般访问分离，不改前后正文；Ch4/6交接不变。

逐字PRE：

> 事实已被观察或保存，也不保证每一种名字都能把它带到当前回答路径。评估闭卷知识时，可以固定实体、关系与正确答案，只替换同一实体的规范名、别名、缩写或拼写形式，分别统计“规范名对、别名错”与相反方向的切换，而不是把两边都答错的一致性当成可靠记忆。受限英语事实 QA 中，这种双向切换在多类模型上存在；因此，人类选定的规范名称不是参数知识访问的天然标准键，单次 canonical 问答失败不能独自决定增加知识数据还是修复访问路径。<!-- source-family:SF-2026-ARXIV-2604-21882 -->
>
> [必要配对与反侧](https://arxiv.org/html/2604.21882v1)仍只是行为证据：透明模型中实体总频率在控制当前名字频率后仍与准确率相关，不等于训练频率已获得因果解释，也不证明模型内部保存了唯一实体地址。名称资源、实体链接、答案 alias matching、额外问法及分层评测均付费，英语 Wikimedia 覆盖与量化推理又限定了测量人口；对象侧改写和跨语言尚未覆盖。应保留原 canonical 基线并补同事实的名称切片，必要时使用可核外部检索与拒答，而不由多名字 agreement 或一个频率 proxy 认证事实为真。

未写Books、未占锁；待root必要Source/公开日/具体owner与逐字PRE通过后再获窄lease。准备好本项不等待无关材料。

## A5 TGR-MoE 21330v1 必要Source与唯一owner逐字PRE（待独核）

精确[HTMLv1](https://arxiv.org/html/2604.21330v1)，实际§3.1–3.2/Eq6–10/Algorithm1，§4.1–4.3/T1–4，§5.1–5.4/T5–7，§6限制；直接反侧I/S11–13/FigS4、J.3/J.4/T-S9、H配置。2+1+2=5，Ch21独立监督差额必要深入，未把成熟TopK/均衡原理计分。

冻结DeiTIII teacherbackbone，仅auxiliaryteacherrouter受load/entropy损失更新；student KL(stopgrad(pt)||p)再加task，teacherrouter不实际dispatch，student从训练到推理自己选expert。ImageNet1K224px学生Tiny/Small/Base从零训练，8/10/12层MoE、Tiny16experts/其余8、K1与K2各独立训练；全baseline同DeiTfinalclassifierdistillation、augmentations、AdamW/schedule。teacher提前ImageNet21K训练不是免费同信息预算；无teacherpretrain全费对照，不把额外先验与算法改进完全分离。T2TinyK1 77.85→78.78但SoftMoE79.31更高；不是全胜。§4.2/T3停止guidance fine-tune多数收益不保持；T5只前半distill78.13胜全程77.81，只distill77.83，示阶段依赖；不能把越强/越久越好。

关键反侧§5.3/I并非无条件oracle上界：teacherfeatures实际路由80.19，studentrouter在训练未执行直到推理才启用74.84，原VMoE77.39/TGR77.81，说明训练执行与推理替换不匹配，不能仅以routerKL替代下游行为验收。teacher最后层指导75.83低于VMoE、层对齐intermediate更好；teacherstudent top1agreement不完美且深层下降，稳定不等唯一正确expert/语义。§4.1 teacherCLS distillationtarget与方法patch表示描述粒度未完全展开，本次不补造完整tokenrouting代码recipe。J4 singleH100秒/epoch Ti1006→1020、S2560→2570、B4930→4954，trainableparams明确exclude frozen teacher；主实验2/4H100，precision/batch/concurrency/SLO及多seed不确定性Not Disclosed，不采‘零训练成本/生产加速’。imageclassification局部，语言/多模态扩展未证；未核代码/复现。

唯一owner `MODEL-MOE` Ch21：现正文已有TopK、linear/nullspace、parameter-free/subspace/Bayesianrouter、reference softbias与auxiliaryload/类别capacity先验，但未承载dense teacherfeature生成独立routing supervision且student必须训练期真实执行的差额。拟在原‘Auxiliary loss 是代理约束，不证明所有 experts 语义均匀，也不保证每个 batch 完全平衡。权重过强还可能牺牲内容路由质量。’后补两段，接回原activationfrequencyvsimportance；Ch20采样不拥有MoE训练监督、Ch22只交接context成本不重复推导。

逐字PRE：

> 负载均衡也不能替代路由学习信号：未被选中的路径可能缺少任务梯度，单纯把 token 数分散并不告诉 gate 应怎样稳定分工。一条受限分支冻结已训练的 dense teacher，用其中间特征训练辅助 router；该 router 只通过均衡与单样本熵目标形成监督分布，student 以 stop-gradient 的 teacher 分布作 KL 目标，同时继续用自己的 router 选择并训练 experts。这把“给路由提供先验”与“让 teacher 代替模型执行选择”分开；后者在训练期替学生选路、推理时才切回学生，会引入另一种执行分布失配。<!-- source-family:SF-2026-ARXIV-2604-21330 -->
>
> [必要训练与反侧](https://arxiv.org/html/2604.21330v1)仅支持受测视觉 MoE：最后层 teacher 特征未必比层对齐的中间特征合适，前半程监督可优于全程固定蒸馏，fine-tuning 取消指导又可能丢掉收益。Teacher 预训练、额外 forward、辅助 router 与回归均付费；较稳定 assignment 或较高 teacher agreement 不认证任务正确、专家语义或 batch 负载，更不能把剔除 frozen teacher 的参数计数当完整训练成本。缺少匹配 teacher、出现表示失配或质量退步时，保留原 task-trained gate、均衡约束及质量/容量验收，而不由路由模仿单独批准替换。

未写Books、未占锁；待非作者Source/owner/PRE和窄lease。

## A6 发现范围收窄与第二批完整题摘待校准

四主题API发现窗同A1；MODEL已以start0/50/100/150/200、max50实际取全214，AGENT77、MULTIMODAL67、SYSTEM36均start0/max350实返同total。API当前返回后来版本，题摘只判断潜在增量，不把currentv2/v3当四月证据。含all:GPU/agent/model等词的物理/领域应用命中只作明确范围title关闭，不扩全文队列。official月列表12分类完成targetID20842–22139标题浏览（非精确date证明）；CV第0页未到target，已补skip2000/show2000；其他页目标段实际见到后停，OS空需区分真实无列表与访问限制。只有下列可能相关/含糊题名才进入完整AB，未把monthly所有条目强制逐项关闭。

### 2604.21276 — Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition

原始完整AB：http://arxiv.org/abs/2604.21276v1

> As pretrained large language models replace task-specific decoders in speech recognition, a critical question arises: do their text-derived priors make recognition fairer or more biased across demographic groups? We evaluate nine models spanning three architectural generations (CTC with no language model, encoder-decoder with an implicit LM, and LLM-based with an explicit pretrained decoder) on about 43,000 utterances across five demographic axes (ethnicity, accent, gender, age, first language) using Common Voice 24 and Meta's Fair-Speech, a controlled-prompt dataset that eliminates vocabulary confounds. On clean audio, three findings challenge assumptions: LLM decoders do not amplify racial bias (Granite-8B has the best ethnicity fairness, max/min WER = 2.28); Whisper exhibits pathological hallucination on Indian-accented speech with a non-monotonic insertion-rate spike to 9.62% at large-v3; and audio compression predicts accent fairness more than LLM scale. We then stress-test these findings under 12 acoustic degradation conditions (noise, reverberation, silence injection, chunk masking) across both datasets, totaling 216 inference runs. Severe degradation paradoxically compresses fairness gaps as all groups converge to high WER, but silence injection amplifies Whisper's accent bias up to 4.64x by triggering demographic-selective hallucination. Under masking, Whisper enters catastrophic repetition loops (86% of 51,797 insertions) while explicit-LLM decoders produce 38x fewer insertions with near-zero repetition; high-compression audio encoding (Q-former) reintroduces repetition pathology even in LLM decoders. These results suggest that audio encoder design, not LLM scaling, is the primary lever for equitable and robust speech recognition.

P：编码压缩/架构而非仅LLM规模影响静音/遮罩引起的重复与群体差异；噪声下fairnessgap缩小可能全体变差，改变指标解释。

### 2604.21083 — Behavioral Consistency and Transparency Analysis on Large Language Model API Gateways

原始完整AB：http://arxiv.org/abs/2604.21083v1

> Third-party Large Language Model (LLM) API gateways are rapidly emerging as unified access points to models offered by multiple vendors. However, the internal routing, caching, and billing policies of these gateways are largely undisclosed, leaving users with limited visibility into whether requests are served by the advertised models, whether responses remain faithful to upstream APIs, or whether invoices accurately reflect public pricing policies. To address this gap, we introduce GateScope, a lightweight black-box measurement framework for evaluating behavioral consistency and operational transparency in commercial LLM gateways. GateScope is designed to detect key misbehaviors, including model downgrading or switching, silent truncation, billing inaccuracies, and instability in latency by auditing gateways along four critical dimensions: response content analysis, multi-turn conversation performance, billing accuracy, and latency characteristics. Our measurements across 10 real-world commercial LLM API gateways reveal frequent gaps between expected and actual behaviors, including silent model substitutions, degraded memory retention, deviations from announced pricing, and substantial variation in latency stability across platforms.

P：网关把公开modelID、行为一致性、截断/计费与延迟分开实测；会改变只信alias而不做端到端对照的验收。

### 2604.21590 — AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use

原始完整AB：http://arxiv.org/abs/2604.21590v1

> Modern industrial applications increasingly demand language models that act as agents, capable of multi-step reasoning and tool use in real-world settings. These tasks are typically performed under strict cost and latency constraints, making small agentic models highly desirable. In this paper, we introduce the AgenticQwen family of models, trained via multi-round reinforcement learning (RL) on synthetic data and a limited amount of open-source data. Our training framework combines reasoning RL and agentic RL with dual data flywheels that automatically generate increasingly challenging tasks. The reasoning flywheel increases task difficulty by learning from errors, while the agentic flywheel expands linear workflows into multi-branch behavior trees that better reflect the decision complexity of real-world applications. We validate AgenticQwen on public benchmarks and in an industrial agent system. The models achieve strong performance on multiple agentic benchmarks, and in our industrial agent system, close the gap with much larger models on search and data analysis tasks. Model checkpoints and part of the synthetic data: https://huggingface.co/collections/alibaba-pai/agenticqwen. Data synthesis and RL training code: https://github.com/haruhi-sudo/data_synth_and_rl. The data synthesis pipeline is also integrated into EasyDistill: https://github.com/modelscope/easydistill.

P：错误驱动reasoning与linear→branchingtree agent数据双flywheel，需核复杂度增加与可比成本/消融，非仅小模型新release。

### 2604.21860 — Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models

原始完整AB：http://arxiv.org/abs/2604.21860v1

> Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.

P/安全必要：分散adversarialintent与statelessmoderation边界，需要核实际会话信息路径，不能由attack标题保证新机制。

### 2604.21632 — To See the Unseen: on the Generalization Ability of Transformers in Symbolic Reasoning

原始完整AB：http://arxiv.org/abs/2604.21632v1

> We investigate the ability of decoder-only transformer models to perform abstract symbolic reasoning; specifically solving propositional logic reasoning problems given in-context. Previous work demonstrated that models fail to generalize to problems involving variable names that were not observed during training, and it was shown that one reason behind this is the difficulty of copying (or generating) unseen tokens. We show both theoretically and empirically that a particular representational collapse also has a crucial role: the unembeddings (last-layer weights) of unseen tokens collapse to nearly the same vector during training. The collapse makes distinguishing multiple unseen variables difficult for the model (especially when the embedding and unembedding parameters are shared), and provides a mechanistic explanation for the effectiveness of existing heuristic interventions like "active forgetting", which periodically reset the token (un)embeddings. Based on these observations, we devise a combination of techniques, involving a small architecture change facilitating copying, data diversity, and freezing or resetting (un)embeddings, that achieves generalization to unseen tokens. We support our claims with extensive controlled experiments on propositional logic reasoning problems. Beyond synthetic experiments, we also observe evidence of (un)embedding collapse in the open-weight models in the Gemma 3 family, which includes 99 unused tokens reserved for downstream use. Empirically we find that the correlated embeddings of these tokens are a poor initialization for finetuning applications.

P：unseen(un)embeddingcollapse与copy障碍分开，可改变冻结/重置新token初始化及泛化解释。

### 2604.21193 — Trust but Verify: Introducing DAVinCI -- A Framework for Dual Attribution and Verification in Claim Inference for Language Models

原始完整AB：http://arxiv.org/abs/2604.21193v1

> Large Language Models (LLMs) have demonstrated remarkable fluency and versatility across a wide range of NLP tasks, yet they remain prone to factual inaccuracies and hallucinations. This limitation poses significant risks in high-stakes domains such as healthcare, law, and scientific communication, where trust and verifiability are paramount. In this paper, we introduce DAVinCI - a Dual Attribution and Verification framework designed to enhance the factual reliability and interpretability of LLM outputs. DAVinCI operates in two stages: (i) it attributes generated claims to internal model components and external sources; (ii) it verifies each claim using entailment-based reasoning and confidence calibration. We evaluate DAVinCI across multiple datasets, including FEVER and CLIMATE-FEVER, and compare its performance against standard verification-only baselines. Our results show that DAVinCI significantly improves classification accuracy, attribution precision, recall, and F1-score by 5-20%. Through an extensive ablation study, we isolate the contributions of evidence span selection, recalibration thresholds, and retrieval quality. We also release a modular DAVinCI implementation that can be integrated into existing LLM pipelines. By bridging attribution and verification, DAVinCI offers a scalable path to auditable, trustworthy AI systems. This work contributes to the growing effort to make LLMs not only powerful but also accountable.

EX待最小事实：摘要仅两阶段attribution+entailment/calibration及指标，未给内部归因如何新改变验证选择；仅定点核是否有新的内部/外部归因机制，不默认全篇。

### 2604.21197 — Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach

原始完整AB：http://arxiv.org/abs/2604.21197v1

> Federated Large Language Models (FedLLMs) enable multiple parties to collaboratively fine-tune LLMs without sharing raw data, addressing challenges of limited resources and privacy concerns. Despite data localization, shared gradients can still expose sensitive information through membership inference attacks (MIAs). However, FedLLMs' unique properties, i.e. massive parameter scales, rapid convergence, and sparse, non-orthogonal gradients, render existing MIAs ineffective. To address this gap, we propose ProjRes, the first projection residuals-based passive MIA tailored for FedLLMs. ProjRes leverages hidden embedding vectors as sample representations and analyzes their projection residuals on the gradient subspace to uncover the intrinsic link between gradients and inputs. It requires no shadow models, auxiliary classifiers, or historical updates, ensuring efficiency and robustness. Experiments on four benchmarks and four LLMs show that ProjRes achieves near 100% accuracy, outperforming prior methods by up to 75.75%, and remains effective even under strong differential privacy defenses. Our findings reveal a previously overlooked privacy vulnerability in FedLLMs and call for a re-examination of their security assumptions. Our code and data are available at $\href{https://anonymous.4open.science/r/Passive-MIA-5268}{link}$.

P/安全必要：projectionresidual被动MIA不用shadow/history；sharedgradient隐私边界，需核攻击者权限与DP反侧而非照录近100%。

### 2604.21106 — How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models

原始完整AB：http://arxiv.org/abs/2604.21106v3

> We measure how much one recurrence is worth to a looped (depth-recurrent) transformer, in equivalent unique parameters. From an iso-depth pretraining sweep across recurrence counts $r \in \{1, 2, 4, 8\}$ spanning ${\sim}50\times$ in training compute, we fit a joint scaling law $L = E + A\,(N_\text{once} + r^{\varphi} N_\text{rec})^{-α} + B\,D^{-β}$ and measure a recurrence-equivalence exponent $\varphi = 0.46$. Intuitively, $\varphi$ tells us whether looping a block $r$ times is equivalent in validation loss to $r$ unique blocks of a non-looped model (full equivalence, $\varphi{=}1$) or to a single block run repeatedly with no capacity gain ($\varphi{=}0$). Our $\varphi = 0.46$ sits in between, so replacing unique blocks with shared recurrences increases validation loss at matched training compute. For example, at $r{=}4$ a 410M looped model performs on par with a 580M non-looped model, but incurs the training cost of a 1B non-looped one. We demonstrate the utility of $\varphi$ as a diagnostic tool on two case studies: commonly used truncated backpropagation lowers $\varphi$ to $0.38$, indicating that the loop mechanism is poorly trained under truncation, even though validation loss decreases. Conversely, hyperconnections raise $\varphi$ to $0.65$, a genuine capacity gain. Our method separates true loop improvements from training-side gains, a distinction raw validation loss cannot make.

P：iso-depth recurrence-equivalence exponent分开参数节省与训练compute，改变looped scaling解释；当前v3摘要只发现，必要用v1。

### 2604.21335 — Sub-Token Routing for KV Cache Compression

原始完整AB：http://arxiv.org/abs/2604.21335v3

> Transformer inference often requires a large KV cache, especially for long-context language modeling and multimodal generation. Existing compression methods usually reduce cache cost by selecting, evicting, quantizing, or compressing cached tokens, or by reducing the visual-token sequence before language-model inference. We introduce sub-token routing, a KV-compression method that adds a finer control axis inside retained tokens. It splits each retained value vector into groups and keeps only selected groups, while leaving query and key states unchanged. The method is designed to work after token-level reduction. First, a token-reduction method determines which tokens are retained. Then, sub-token routing compresses the value states inside those retained tokens. Experiments under matched KV budgets show that adding sub-token routing improves token-level reduction performance in both LLM and VLM settings, including Quest on LLaMA-2-7B and Qwen2.5-7B, and FastV/VisionZip across LLaVA and Qwen-VL models. The gains are larger at smaller KV budgets, suggesting that value-group routing is especially useful when further token removal becomes costly. Overall, token-level reduction and sub-token routing provide complementary ways to reduce KV cost.

P：保留Q/K而V-group粒度在tokenreduction后再压缩，需核真实cache representation/overhead；当前v3只发现。

### 2604.21454 — Reasoning Primitives in Hybrid and Non-Hybrid LLMs: Do Architectural Differences Yield Advantages in State-Tracking and Recall?

原始完整AB：http://arxiv.org/abs/2604.21454v2

> Reasoning in large language models is often discussed as a single capability, but some of its gains may stem from simpler underlying operations. We examine two such primitives, recall and state-tracking, through five controlled task families centered on state-based recall, and compare matched transformer and hybrid architectures with and without reasoning augmentation. Across the suite, reasoning-augmented variants substantially outperform instruction-only variants, often by large margins. This pattern is consistent with the State over Tokens view: externalized reasoning traces help because they carry the intermediate state forward in token space. By contrast, hybrid inductive bias does not yield a uniform advantage in accuracy once reasoning tokens are available. When architectural differences do appear, they follow task structure: the hybrid Think model is more robust on strictly sequential chained updates, whereas the transformer Think model is more robust on flat multi-hop retrieval. We therefore cast the main contribution of this study as a descriptive account of what drives performance on state-based recall tasks: reasoning-token augmentation appears to be the dominant factor, while hybrid advantages are narrower, task-dependent, and potentially more about inference efficiency than overall capability. We also release the codebase and data required to reproduce these results.

P：matchinghybrid/transformer+reasoningaugmentation，检验architecturevs外显state携带不同贡献；当前v2只发现。

### 2604.21191 — Prefix Parsing is Just Parsing

原始完整AB：http://arxiv.org/abs/2604.21191v1

> Prefix parsing asks whether an input prefix can be extended to a complete string generated by a given grammar. In the weighted setting, it also provides prefix probabilities, which are central to context-free language modeling, psycholinguistic analysis, and syntactically constrained generation from large language models. We introduce the prefix grammar transformation, an efficient reduction of prefix parsing to ordinary parsing. Given a grammar, our method constructs another grammar that generates exactly the prefixes of its original strings. Prefix parsing is then solved by applying any ordinary parsing algorithm on the transformed grammar without modification. The reduction is both elegant and practical: the transformed grammar is only a small factor larger than the input, and any optimized implementation can be used directly, eliminating the need for bespoke prefix-parsing algorithms. We also present a strategy-based on algorithmic differentiation-for computing the next-token weight vector, i.e., the prefix weights of all one-token extensions, enabling efficient prediction of the next token. Together, these contributions yield a simple, general, and efficient framework for prefix parsing.

P：prefixgrammar转换复用ordinaryparser及next-tokenweight微分，改变structuredgeneration grammar前缀专用实现选择。

### 2604.21265 — Listen and Chant Before You Read: The Ladder of Beauty in LM Pre-Training

原始完整AB：http://arxiv.org/abs/2604.21265v1

> We show that pre-training a Transformer on music before language significantly accelerates language acquisition. Using piano performances (MAESTRO dataset), a developmental pipeline -- music $\to$ poetry $\to$ prose -- yields a $17.5\%$ perplexity improvement over random initialization ($p &lt; 0.001$, 5 seeds), with music and poetry improving orthogonal model components (internal computation and embeddings, respectively). Convergence tests confirm that this is not a transient head start: at $d\!=\!64$, multi-seed validation (5 seeds) shows a persistent 5.5\% gap at plateau ($p = 0.017$), with the pipeline converging faster and to a lower loss in every run. Real music matches the transfer ceiling of synthetic patterns with one-third the data, and scaling experiments reveal that optimal pre-training data volume shifts with model capacity ($-3\% \to +3\% \to +6\%$ advantage of larger datasets from $d\!=\!16$ to $d\!=\!64$). Across the scales we study ($d\!\in\!\{16,32,64\}$, up to ${\sim}400$K parameters), these results suggest a capacity-dependent data curation principle and indicate that structured human creative outputs can provide an efficient pre-training substrate for small language models; stronger conclusions at modern pre-training scale will require substantially larger experiments.

P：受限tiny400k范围的music/poetry/prose分阶段转移及plateau反侧，不能因小规模或提高小就排除。

### 2604.21611 — Process Supervision via Verbal Critique Improves Reasoning in Large Language Models

原始完整AB：http://arxiv.org/abs/2604.21611v1

> Inference-time scaling for LLM reasoning has focused on three axes: chain depth, sample breadth, and learned step-scorers (PRMs). We introduce a fourth axis, granularity of external verbal supervision, via Verbal Process Supervision (VPS), a training-free framework that uses structured natural-language critique from a stronger supervisor to guide an iterative generate-critique-refine loop up to a round budget R. Across GPQA Diamond, AIME 2025, and LiveCodeBench V6 (covering both closed and open models), VPS yields three key results. First, on GPQA Diamond, GPT-5.4 (High) | GPT-5.4 (Low) reaches 94.9% at R=4, surpassing the 94.1% state of the art without gradient updates. Second, on AIME 2025, VPS enables strong weak-actor rescue, boosting scores from 11.7-26.7% to 63.3-90.0% (up to +63.3 points). Third, at matched compute, VPS outperforms Reflexion by +8.5 to +12.1 points and Self-Consistency@5 by +5.0 pp (GPQA) and +8.3 pp (LiveCodeBench), isolating critique granularity as the key driver. Performance scales with the supervisor-actor capability gap (Pearson r=0.90) and degrades when errors are not linguistically expressible (e.g., code synthesis), motivating hybrid verbal-executable methods. These results establish critique granularity as a new axis of inference-time scaling.

P：externalcritique粒度与预算匹配+capabilitygap/不可言传错误边界，改变inference-time supervisor设计。

### 2604.20995 — Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models

原始完整AB：http://arxiv.org/abs/2604.20995v2

> Alignment faking, where a model behaves aligned with developer policy when monitored but reverts to its own preferences when unobserved, is a concerning yet poorly understood phenomenon, in part because current diagnostic tools remain limited. Prior diagnostics rely on highly toxic and clearly harmful scenarios, causing most models to refuse immediately. As a result, models never deliberate over developer policy, monitoring conditions, or the consequences of non-compliance, making these diagnostics fundamentally unable to detect alignment faking propensity. To support study of this phenomenon, we first introduce VLAF, a diagnostic framework grounded in the hypothesis that alignment faking is most likely when developer policy conflicts with a model's strongly held values. VLAF uses morally unambiguous scenarios to probe this conflict across diverse moral values, bypassing refusal behavior while preserving meaningful deliberative stakes. Using VLAF, we find that alignment faking is substantially more prevalent than previously reported, occurring in models as small as 7B parameters - with olmo2-7b-instruct faking alignment in 37% of cases. Finally, we show that oversight conditions induce activation shifts that lie along a single direction in representation space. This means the behavioral divergence driving alignment faking can be captured by a single contrastive steering vector, which we exploit for lightweight inference-time mitigation. Finally, we exploit this for mitigation that requires no labeled data and minimal computational overhead, achieving relative reductions in alignment faking of 85.8%, 94.0%, and 57.7% on olmo2-7b-instruct, olmo2-13b-instruct, and qwen3-8b respectively.

P/安全必要：valueconflict避开拒绝混杂，monitoring差异与representationsteering，当前v2待v1且不据表面差异认定deception。

### 2604.21229 — EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval

原始完整AB：http://arxiv.org/abs/2604.21229v1

> Large language model assistants are increasingly expected to retain and reason over information accumulated across many sessions. We introduce EngramaBench, a benchmark for long-term conversational memory built around five personas, one hundred multi-session conversations, and one hundred fifty queries spanning factual recall, cross-space integration, temporal reasoning, adversarial abstention, and emergent synthesis. We evaluate Engrama, a graph-structured memory system, against GPT-4o full-context prompting and Mem0, an open-source vector-retrieval memory system. All three use the same answering model (GPT-4o), isolating the effect of memory architecture. GPT-4o full-context achieves the highest composite score (0.6186), while Engrama scores 0.5367 globally but is the only system to score higher than full-context prompting on cross-space reasoning (0.6532 vs. 0.6291, n=30). Mem0 is cheapest but substantially weaker (0.4809). Ablations reveal that the components driving Engrama's cross-space advantage trade off against global composite score, exposing a systems-level tension between structured memory specialization and aggregate optimization.

P：同answeringmodel的structuredmemory局部cross-space胜/总体弱反证，改变单一总分选择memory架构。

### 2604.21098 — Propensity Inference: Environmental Contributors to LLM Behaviour

原始完整AB：http://arxiv.org/abs/2604.21098v1

> Motivated by loss of control risks from misaligned AI systems, we develop and apply methods for measuring language models' propensity for unsanctioned behaviour. We contribute three methodological improvements: analysing effects of changes to environmental factors on behaviour, quantifying effect sizes via Bayesian generalised linear models, and taking explicit measures against circular analysis. We apply the methodology to measure the effects of 12 environmental factors (6 strategic in nature, 6 non-strategic) and thus the extent to which behaviour is explained by strategic aspects of the environment, a question relevant to risks from misalignment. Across 23 language models and 11 evaluation environments, we find approximately equal contributions from strategic and non-strategic factors for explaining behaviour, do not find strategic factors becoming more or less influential as capabilities improve, and find some evidence for a trend for increased sensitivity to goal conflicts. Finally, we highlight a key direction for future propensity research: the development of theoretical frameworks and cognitive models of AI decision-making into empirically testable forms.

P/安全必要：战略与非战略environmentfactors+防circularanalysis设计，可以反证把behavior变化都归目标追求。

### 2604.21003 — The Last Harness You'll Ever Build

原始完整AB：http://arxiv.org/abs/2604.21003v3

> AI agents are increasingly deployed on complex, domain-specific workflows -- navigating enterprise web applications that require dozens of clicks and form fills, orchestrating multi-step research pipelines that span search, extraction, and synthesis, automating code review across unfamiliar repositories, and handling customer escalations that demand nuanced domain knowledge. \textbf{Each new task domain requires painstaking, expert-driven harness engineering}: designing the prompts, tools, orchestration logic, and evaluation criteria that make a foundation model effective. We present a two-level framework that automates this process. At the first level, the \textbf{Harness Evolution Loop} optimizes a worker agent's harness $\mathcal{H}$ for a single task: a Worker Agent $W_{\mathcal{H}}$ executes the task, an Evaluator Agent $V$ adversarially diagnoses failures and scores performance, and an Evolution Agent $E$ modifies the harness based on the full history of prior attempts. At the second level, the \textbf{Meta-Evolution Loop} optimizes the evolution blueprint $Λ= (W_{\mathcal{H}}, \mathcal{H}^{(0)}, V, E)$ itself across diverse tasks, \textbf{learning a blueprint $Λ^{(\text{best})}$ that enables rapid harness convergence on any new task -- so that adapting an agent to a novel domain requires no human harness engineering at all.} We formalize the correspondence to meta-learning and present both algorithms. The framework \textbf{shifts manual harness engineering into automated harness engineering}, and takes one step further -- \textbf{automating the design of the automation itself}.

EX待最小事实：当前AB只W/V/E循环+meta-evolution类比，未说明新的执行机制/可靠性条件或可比证据；仅定点找算法差额即止，不因meta词入池。

### 2604.21346 — Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning

原始完整AB：http://arxiv.org/abs/2604.21346v1

> Vision--language models (VLMs) often fail on abstract visual reasoning benchmarks such as Bongard problems, raising the question of whether the main bottleneck lies in reasoning or representation. We study this on Bongard-LOGO, a synthetic benchmark of abstract concept learning with ground-truth generative programs, by comparing end-to-end VLMs on raw images with large language models (LLMs) given symbolic inputs derived from those images. Using symbolic inputs as a diagnostic probe rather than a practical multimodal architecture, our \emph{Componential--Grammatical (C--G)} paradigm reformulates Bongard-LOGO as a symbolic reasoning task based on LOGO-style action programs or structured descriptions. LLMs achieve large and consistent gains, reaching mid--90s accuracy on Free-form problems, while a strong visual baseline remains near chance under matched task definitions. Ablations on input format, explicit concept prompts, and minimal visual grounding show that these factors matter much less than the shift from pixels to symbolic structure. These results identify representation as a key bottleneck in abstract visual reasoning and show how symbolic input can serve as a controlled diagnostic upper bound.

P：固定taskdefinitions用oracle symbolic替像素，定位representationbottleneck诊断上界，不是部署可用能力。

### 2604.21579 — A Metamorphic Testing Approach to Diagnosing Memorization in LLM-Based Program Repair

原始完整AB：http://arxiv.org/abs/2604.21579v1

> LLM-based automated program repair (APR) techniques have shown promising results in reducing debugging costs. However, prior results can be affected by data leakage: large language models (LLMs) may memorize bug fixes when evaluation benchmarks overlap with their pretraining data, leading to inflated performance estimates. In this paper, we investigate whether we can better reveal data leakage by combining metamorphic testing (MT) with negative log-likelihood (NLL), which has been used in prior work as a proxy for memorization. We construct variant benchmarks by applying semantics-preserving transformations to two widely used datasets, Defects4J and GitBug-Java. Using these benchmarks, we evaluate the repair success rates of seven LLMs on both original and transformed versions, and analyze the relationship between performance degradation and NLL. Our results show that all evaluated state-of-the-art LLMs exhibit substantial drops in patch generation success rates on transformed benchmarks, ranging from -4.1% for GPT-4o to -15.98% for Llama-3.1. Furthermore, we find that this degradation strongly correlates with NLL on the original benchmarks, suggesting that models perform better on instances they are more likely to have memorized. These findings show that combining MT with NLL provides stronger and more reliable evidence of data leakage, while metamorphic testing alone can help mitigate its effects in LLM-based APR evaluations.

P：语义保持metamorphisms+NLL相关分开污染与变换不稳，改变APR基准解释；不能把correlation当污染因果。

### 2604.21134 — Beyond Pixels: Introspective and Interactive Grounding for Visualization Agents

原始完整AB：http://arxiv.org/abs/2604.21134v1

> Vision-Language Models (VLMs) frequently misread values, hallucinate details, and confuse overlapping elements in charts. Current approaches rely solely on pixel interpretation, creating a Pixel-Only Bottleneck: agents treat interactive charts as static images, losing access to the structured specification that encodes exact values. We introduce Introspective and Interactive Visual Grounding (IVG), a framework that combines (1) spec-grounded introspection, which queries the underlying specification for deterministic evidence, with (2) view-grounded interaction, which manipulates the view to resolve visual ambiguity. To enable evaluation without VLM bias, we present iPlotBench, a benchmark of 500 interactive Plotly figures with 6,706 binary questions and ground-truth specifications. Experiments show that introspection improves data reconstruction fidelity, while the combination with interaction achieves the highest QA accuracy (0.81), with +6.7 % gains on overlapping geometries. We further demonstrate IVG in deployed agents that explore data autonomously and collaborate with human users in real time.

P：interactivechart spec introspection vs viewinteraction，量化两种证据路径和overlap边界，改变pixel-only工具选择。

### 2604.21794 — Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems

原始完整AB：http://arxiv.org/abs/2604.21794v1

> Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.

P：latentmulti-agentcommunications被联合训练而非固定KV协议，改变sender/receiver兼容训练成本取舍。

### 2604.21057 — TRACES: Tagging Reasoning Steps for Adaptive Cost-Efficient Early-Stopping

原始完整AB：http://arxiv.org/abs/2604.21057v2

> The field of Language Reasoning Models (LRMs) has been very active over the past few years with advances in training and inference techniques enabling LRMs to reason longer, and more accurately. However, a growing body of studies show that LRMs are still inefficient, over-generating verification and reflection steps. Additionally, the high-level role of each reasoning step and how different step types contribute to the generation of correct answers, is largely underexplored. To address this challenge, we introduce TRACES (Tagging of the Reasoning steps enabling Adaptive Cost-Efficient early-Stopping), a lightweight framework that tags reasoning steps in real-time, and enable adaptive, cost-efficient early stopping of large-language-model inferences. By monitoring reasoning behaviors during inferences, we find that LRMs tend to shift their reasoning behavior after reaching a correct answer. We demonstrate that the monitoring of the specific type of steps can produce effective interpretable early stopping criteria. Evaluated on three mathematical reasoning benchmarks (MATH500, GSM8K, AIME) and two knowledge and reasoning benchmarks (MMLU and GPQA), TRACES achieve 20 to 50% token reduction while maintaining comparable accuracy to standard generation. On harder tasks (BeyondAIME, IMO AnswerBench), the accuracy-efficiency trade-off is steeper, requiring a more conservative early-stopping threshold. This work offers a novel way to study and control the generation behavior of LRMs.

P：step-type监测早停与hardmath反退，改变仅答案/长度threshold预算策略，当前v2待v1。

### 2604.21911 — When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs

原始完整AB：http://arxiv.org/abs/2604.21911v1

> Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .

P：textinstructionprior与vision因素controlled拆分+targetedDPO，改变hallucination归因与后训练条件。

### 2604.21327 — Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning

原始完整AB：http://arxiv.org/abs/2604.21327v1

> Test-time reinforcement learning (TTRL) always adapts models at inference time via pseudo-labeling, leaving it vulnerable to spurious optimization signals from label noise. Through an empirical study, we observe that responses with medium consistency form an ambiguity region and constitute the primary source of reward noise. Crucially, we find that such spurious signals can be even amplified through group-relative advantage estimation. Motivated by these findings, we propose a unified framework, Debiased and Denoised test-time Reinforcement Learning (DDRL), to mitigate spurious signals. Concretely, DDRL first applies a frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples. It then adopts a debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization. Finally, DDRL incorporates a consensus-based off-policy refinement stage, which leverages the rejection-sampled dataset to enable efficient and stable model updates. Experiments on three large language models across multiple mathematical reasoning benchmarks demonstrate that DDRL consistently outperforms existing TTRL baselines. The code will soon be released at https://github.com/yuyongcan/DDRL.

P：TTRL中mediumconsistency伪标签经groupadv放大，frequency样本选择/固定adv更改更新，需核bias含义。

### 2604.20994 — Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models

原始完整AB：http://arxiv.org/abs/2604.20994v2

> The growth of agentic AI has drawn significant attention to function calling Large Language Models (LLMs), which are designed to extend the capabilities of AI-powered system by invoking external functions. Injection and jailbreaking attacks have been extensively explored to showcase the vulnerabilities of LLMs to user prompt manipulation. The expanded capabilities of agentic models introduce further vulnerabilities via their function calling interface. Recent work in LLM security showed that function calling can be abused, leading to data tampering and theft, causing disruptive behavior such as endless loops, or causing LLMs to produce harmful content in the style of jailbreaking attacks. This paper introduces a novel function hijacking attack (FHA) that manipulates the tool selection process of agentic models to force the invocation of an attacker-chosen function. While existing attacks focus on semantic preference of the model for function-calling tasks, we show that FHA is largely agnostic to the context semantics and remains effective across domains and function sets. We demonstrate that FHA generalizes to unseen queries and payload perturbations under a fixed target model, reaching 62.5% to 81.9% ASR on held-out queries across 4 function-calling LLMs (instructed and reasoning models), evaluated on the Berkeley Function Calling Leaderboard (BFCL). We further evaluate the cross-model transferability of FHA, showing that FHA can be transferred to other model sizes and families (11.2-27.6% ASR). Our findings further demonstrate the need for strong guardrails and modules for agentic systems.

P/安全必要：toolselection hijack训练/跨query与跨model泛化不同，改变schema/toolname可作为信任的判断，currentv2待v1。

### 2604.21232 — ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures

原始完整AB：http://arxiv.org/abs/2604.21232v2

> Vision-Language-Action systems follow instructions to execute multi-step tasks in multimodal environments. Recent VLA approaches typically rely on post-hoc correction mechanisms or operate under fixed task decompositions and alignment schemes. However, once an intermediate step is mis-specified, local errors propagate through subsequent steps and eventually accumulate into cascading failures. To mitigate this compounding effect, we propose Predictive Alignment and Planning Architecture, a framework that uses prediction and contrast to adjust deviations across three levels: actions, subgoals, and trajectories. Semantic alignment is enforced at all levels using a Sinkhorn-based module and a Score-field module. The predictive correction and alignment jointly update the action generator during training, enabling it to adjust fine-grained steps to remain aligned with the overall intent. We further introduce two new metrics to quantify error propagation and recovery processes in tasks, capturing how mistakes spread and fade over long-horizon execution. Experiments show that ReCAPA achieves competitive results on embodied agent benchmarks such as VisualAgentBench, MineDojo, and AI2-THOR, outperforming strong proprietary and open-source Large Language Model baselines.

P：action/subgoal/trajectory三级predictivecorrection训练与cascadingfailure测量；非仅VLA任务换名，currentv2待v1。

### 2604.21160 — Reinforcing 3D Understanding in Point-VLMs via Geometric Reward Credit Assignment

原始完整AB：http://arxiv.org/abs/2604.21160v1

> Point-Vision-Language Models promise to empower embodied agents with executable spatial reasoning, yet they frequently succumb to geometric hallucination where predicted 3D structures contradict the observed 2D reality. We identify a key cause of this failure not as a representation bottleneck but as a structural misalignment in reinforcement learning, where sparse geometric tokens are drowned out by noisy and broadcasted sequence-level rewards. To resolve this causal dilution, we propose Geometric Reward Credit Assignment, a framework that disentangles holistic supervision into field-specific signals and routes them exclusively to their responsible token spans. This mechanism transforms vague feedback into precise gradient updates and effectively turns generic policy optimization into targeted structural alignment. Furthermore, we internalize physical constraints via a Reprojection-Consistency term which serves as a cross-modal verifier to penalize physically impossible geometries. Validated on a calibrated benchmark derived from ShapeNetCore, our approach bridges the reliability gap by boosting 3D KPA from 0.64 to 0.93, increasing 3D bounding box intersection over union to 0.686, and raising reprojection consistency scores to 0.852. Crucially, these gains are achieved while maintaining robust 2D localization performance, marking a meaningful step from plausible textual outputs toward physically verifiable spatial predictions.

P：geometryfield-specificreward归因token spans+reprojection核验，重考sequencebroadcastreward对稀疏geomtoken的credit。

### 2604.21564 — Measuring Opinion Bias and Sycophancy via LLM-based Persuasion

原始完整AB：http://arxiv.org/abs/2604.21564v2

> Large language models increasingly shape the information people consume: they are embedded in search, consulted for professional advice, deployed as agents, and used as a first stop for questions about policy, ethics, health, and politics. When such a model silently holds a position on a contested topic, that position propagates at scale into users' decisions. Eliciting a model's positions is harder than it first appears: contemporary assistants answer direct opinion questions with evasive disclaimers, and the same model may concede the opposite position once the user starts arguing one side. We propose a method, released as the open-source llm-bias-bench, for discovering the opinions an LLM actually holds on contested topics under conditions that resemble real multi-turn interaction. The method pairs two complementary free-form probes. Direct probing asks for the model's opinion across five turns of escalating pressure from a simulated user. Indirect probing never asks for an opinion and engages the model in argumentative debate, letting bias leak through how it concedes, resists, or counter-argues. Three user personas (neutral, agree, disagree) collapse into a nine-way behavioral classification that separates persona-independent positions from persona-dependent sycophancy, and an auditable LLM judge produces verdicts with textual evidence. The first instantiation ships 38 topics in Brazilian Portuguese across values, scientific consensus, philosophy, and economic policy. Applied to 13 assistants, the method surfaces findings of practical interest: argumentative debate triggers sycophancy 2-3x more than direct questioning (median 50% to 79%); models that look opinionated under direct questioning often collapse into mirroring under sustained arguments; and attacker capability matters mainly when an existing opinion must be dislodged, not when the assistant starts neutral.

P：directvsdebate与persona九分类分开opinion/sycophancy，改变多轮监测解释，currentv2待v1。

### 2604.21700 — Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers

原始完整AB：http://arxiv.org/abs/2604.21700v1

> The growing application of large language models (LLMs) in safety-critical domains has raised urgent concerns about their security. Many recent studies have demonstrated the feasibility of backdoor attacks against LLMs. However, existing methods suffer from three key shortcomings: explicit trigger patterns that compromise naturalness, unreliable injection of attacker-specified payloads in long-form generation, and incompletely specified threat models that obscure how backdoors are delivered and activated in practice. To address these gaps, we present BadStyle, a complete backdoor attack framework and pipeline. BadStyle leverages an LLM as a poisoned sample generator to construct natural and stealthy poisoned samples that carry imperceptible style-level triggers while preserving semantics and fluency. To stabilize payload injection during fine-tuning, we design an auxiliary target loss that reinforces the attacker-specified target content in responses to poisoned inputs and penalizes its emergence in benign responses. We further ground the attack in a realistic threat model and systematically evaluate BadStyle under both prompt-induced and PEFT-based injection strategies. Extensive experiments across seven victim LLMs, including LLaMA, Phi, DeepSeek, and GPT series, demonstrate that BadStyle achieves high attack success rates (ASRs) while maintaining strong stealthiness. The proposed auxiliary target loss substantially improves the stability of backdoor activation, yielding an average ASR improvement of around 30% across style-level triggers. Even in downstream deployment scenarios unknown during injection, the implanted backdoor remains effective. Moreover, BadStyle consistently evades representative input-level defenses and bypasses output-level defenses through simple camouflage.

P/安全必要：naturalstyletrigger+targetpayload loss及injection权限分支，需必要威胁模型、非恶意风格混杂与反侧。

### 2604.21326 — MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment

原始完整AB：http://arxiv.org/abs/2604.21326v1

> Universal Multimodal Retrieval (UMR) aims to map different modalities (e.g., visual and textual) into a shared embedding space for multi-modal retrieval. Existing UMR methods can be broadly divided into two categories: early-fusion approaches, such as Marvel, which projects visual features into the language model (LM) space for integrating with text modality, and late-fusion approaches, such as UniVL-DR, which encode visual and textual inputs using separate encoders and obtain fused embeddings through addition. Our pilot study reveals that Marvel exhibits visual modality collapse, which is characterized by the model's tendency to disregard visual features while depending excessively on textual cues. In contrast, although UniVL-DR is less affected by this issue, it is more susceptible to semantic misalignment, where semantically related content is positioned far apart in the embedding space. To address these challenges, we propose MiMIC, which introduces two key innovations: (1) a fusion-in-decoder architecture for effective multimodal integration, and (2) robust training through single modality mixin and random caption dropout. Experiments on the WebQA+ and EVQA+ datasets, where image in documents or queries might lack captions, indicate that MiMIC consistently outperforms both early- and late-fusion baselines.

P：earlyfusion视觉collapse/latefusionsemanticalignment两侧失败+singlemodalitymix/captiondropout，改变sharedembedding学习。

### 2604.21139 — Slot Machines: How LLMs Keep Track of Multiple Entities

原始完整AB：http://arxiv.org/abs/2604.21139v1

> Language models must bind entities to the attributes they possess and maintain several such binding relationships within a context. We study how multiple entities are represented across token positions and whether single tokens can carry bindings for more than one entity. We introduce a multi-slot probing approach that disentangles a single token's residual stream activation to recover information about both the currently described entity and the immediately preceding one. These two kinds of information are encoded in separate and largely orthogonal "current-entity" and "prior-entity" slots. We analyze the functional roles of these slots and find that they serve different purposes. In tandem with the current-entity slot, the prior-entity slot supports relational inferences, such as entity-level induction ("who came after Alice in the story?") and conflict detection between adjacent entities. However, only the current-entity slot is used for explicit factual retrieval questions ("Is anyone in the story tall?" "What is the tall entity's name?") despite these answers being linearly decodable from the prior-entity slot too. Consistent with this limitation, open-weight models perform near chance accuracy at processing syntax that forces two subject-verb-object bindings on a single token (e.g., "Alice prepares and Bob consumes food.") Interestingly, recent frontier models can parse this properly, suggesting they may have developed more sophisticated binding strategies. Overall, our results expose a gap between information that is available in activations and information the model actually uses, and suggest that the current/prior-entity slot structure is a natural substrate for behaviors that require holding two perspectives at once, such as sycophancy and deception.

P：current/prior实体槽线性可读与显式retrieval实际使用分离，受控binding诊断，不用正交当独立模块。

### 2604.21836 — Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion

原始完整AB：http://arxiv.org/abs/2604.21836v1

> Neural networks exhibit a remarkable degree of representational convergence across diverse architectures, training objectives, and even data modalities. This convergence is predictive of alignment with brain representation. A recent hypothesis suggests this arises from learning the underlying structure in the environment in similar ways. However, it is unclear how individual stimuli elicit convergent representations across networks. An image can be perceived in multiple ways and expressed differently using words. Here, we introduce a methodology based on the Generalized Procrustes Algorithm to measure intra-modal representational convergence at the single-stimulus level. We applied this to vision models with distinct training objectives, selecting stimuli based on their degree of alignment (intra-modal dispersion). Crucially, we found that this intra-modal dispersion strongly modulates alignment between vision and language models (cross-modal convergence). Specifically, stimuli with low intra-modal dispersion (high agreement among vision models) elicited significantly higher cross-modal alignment than those with high dispersion, by up to a factor of two (e.g., in pairings of DINOv2 with language models). This effect was robust to stimulus selection criteria and generalized across different pairings of vision and language models. Measuring convergence at the single-stimulus level provides a path toward understanding the sources of convergence and divergence across modalities, and between neural networks and human neural representations.

P：single-stimulusintra-modaldispersion选择控制跨模态convergence，改变整体geometryagreement解释而非类脑外推。

### 2604.21284 — Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture

原始完整AB：http://arxiv.org/abs/2604.21284v1

> MemPalace is an open-source AI memory system that applies the ancient method of loci (memory palace) spatial metaphor to organize long-term memory for large language models; launched in April 2026, it accumulated over 47,000 GitHub stars in its first two weeks and claims state-of-the-art retrieval performance on the LongMemEval benchmark (96.6% Recall@5) without requiring any LLM inference at write time. Through independent codebase analysis, benchmark replication, and comparison with competing systems, we find that MemPalace's headline retrieval performance is attributable primarily to its verbatim storage philosophy combined with ChromaDB's default embedding model (all-MiniLM-L6-v2), rather than to its spatial organizational metaphor per se -- the palace hierarchy (Wings-&gt;Rooms-&gt;Closets-&gt;Drawers) operates as standard vector database metadata filtering, an effective but well-established technique. However, MemPalace makes several genuinely novel contributions: (1) a contrarian verbatim-first storage philosophy that challenges extraction-based competitors, (2) an extremely low wake-up cost (approximately 170 tokens) through its four-layer memory stack, (3) a fully deterministic, zero-LLM write path enabling offline operation at zero API cost, and (4) the first systematic application of spatial memory metaphors as an organizing principle for AI memory systems. We also note that the competitive landscape is evolving rapidly, with Mem0's April 2026 token-efficient algorithm raising their LongMemEval score from approximately 49% to 93.4%, narrowing the gap between extraction-based and verbatim approaches. Our analysis concludes that MemPalace represents significant architectural insight wrapped in overstated claims -- a pattern common in rapidly adopted open-source projects where marketing velocity exceeds scientific rigor.

P/纠错必要：独立MemPalacecode/replication声称gain主要verbatim+embedding非空间隐喻，需核原artifact/版本及Recall与answer不同分母。

### 2604.21829 — Black-Box Skill Stealing Attack from Proprietary LLM Agents: An Empirical Study

原始完整AB：http://arxiv.org/abs/2604.21829v2

> Large language model (LLM) agents increasingly rely on skills to package reusable capabilities through instructions, tools, and resources. High-quality skills embed expert knowledge, curated workflows, and execution constraints into agents, fueling a growing skill economy through their value and scalability. Yet this ecosystem also creates a new attack surface, as adversaries can interact with public agent interfaces to extract hidden proprietary skill content. We present the first systematic study of black-box skill stealing against LLM agent systems. Compared with conventional system prompt stealing, skill stealing targets modular and structured capability packages whose leakage is directly actionable for copying, redistribution, and monetization, making the resulting harm potentially greater. To study this threat, we derive an attack taxonomy from prior prompt-stealing methods and build an automated stealing prompt generation agent. Starting from model-generated seed prompts, the framework expands attacks through scenario rationalization and structure injection while enforcing diversity via embedding-based filtering, yielding a reproducible pipeline for evaluating proprietary agent systems. We evaluate these attacks across commercial agent platforms and representative LLMs. Our results show that agent skills can often be extracted easily, posing a serious copyright risk. To mitigate this threat, we design defenses across the agent pipeline, focusing on input, inference, and output phase. Although these defenses substantially reduce leakage, the attack remains inexpensive and repeatable, and a single successful attempt is sufficient to compromise the protected skill. Overall, our findings suggest that these copyright risks remain largely overlooked across proprietary agent ecosystems, motivating stronger protection mechanisms.

P/安全必要：modularskill泄露与input/inference/output defenses，需核attackprivilege/cost与一次成功事件，currentv2待v1。

### 2604.21816 — Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows

原始完整AB：http://arxiv.org/abs/2604.21816v1

> The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -&gt; 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at https://github.com/asadani/tool-attention

P：ISO/statepreconditions/lazyload真实token测量与E2Eprojection显分开，可能仅报告，不先按Books覆盖排除。

### 2604.21395 — Supervised Learning Has a Geometric Blind Spot

原始完整AB：http://arxiv.org/abs/2604.21395v3

> Ordinary supervised training minimises the task loss and then stops. It never pays for how far the representation moves when the input is nudged along directions that helped fit training labels---including directions that are nuisance at deployment. We call that leftover sensitivity the geometric blind spot of empirical risk minimisation. In a Gaussian linear model where the nuisance enters the label conditional and the decoder has finite Lipschitz constant, population MSE forces a floor on linearised representation drift. The same distinction predicts a failure mode of adversarial training: Jacobian magnitude can fall while clean class geometry worsens. We track that dissociation with a class-layout score and study isotropic encoder matching---penalising the squared distance between phi(x) and phi(x+delta) for Gaussian delta under a task-loss cap---when nuisance axes are unknown. On a Vision Transformer trained from scratch on CIFAR-10, projected gradient descent attains the smallest Jacobian Frobenius yet the worst clean layout score (1.353+/-0.020 over three seeds), above task-only training (1.093); isotropic matching attains the best (0.904). The drift floor is proved for the linear-Gaussian case; deep nets and cross-task orderings are protocol empirics. Design rule: report class-layout geometry beside the task score; prefer isotropic encoder matching when axes are unknown.

P：linearGaussian漂移下界与Jacobiansmall不保cleanclasslayout，需核任务losscap/性质条件，currentv3待v1。

### 2604.21026 — MCAP: Deployment-Time Layer Profiling for Memory-Constrained LLM Inference

原始完整AB：http://arxiv.org/abs/2604.21026v2

> Deploying large language models to heterogeneous hardware is often constrained by memory, not compute. We introduce MCAP (Monte Carlo Activation Profiling), a load-time per-layer importance estimator that enables dynamic precision and memory placement decisions on the target device. MCAP produces a lightweight per-layer signal that drives both precision dispatch (W4A8 vs. W4A16) and residency tier (GPU, RAM, SSD), allowing a single set of weights to operate across diverse memory budgets. Our system, NVE, achieves 1.5-1.8x higher decode throughput than llama-cpp Q4_0 on NVIDIA T4 and enables models to run in memory regimes previously infeasible without modifying weights.

P：load-timeMonteCarloactivationprofiling联合precision/residencytier选择，改变固定quantconfig在heterodevice部署；currentv2待v1。

### 2604.21598 — You Don't Need Public Tests to Generate Correct Code

原始完整AB：http://arxiv.org/abs/2604.21598v2

> Multi-agent systems are frequently employed for autonomous code generation, demonstrating strong utility in complex algorithmic problem-solving. Recent studies tackle the difficulty of producing functionally correct programs by leveraging simulation-guided planning and debugging, wherein language models step through execution traces to validate logic. Nevertheless, these methods rely heavily on human-authored public test cases to anchor the simulation and debugging cycles. Hand-crafting exhaustive input-output pairs creates a significant, labor-intensive bottleneck within the software development lifecycle. Since ground-truth examples are seldom accessible before actual implementation in real-world scenarios, this reliance limits existing approaches primarily to curated competitive programming datasets. Additionally, we demonstrate that depending on these public tests creates an "overconfidence gap," leading frameworks to overfit to basic examples and underperform on hidden test suites. Conversely, we note that external input samples are not an absolute requirement for successful code generation. We show that large language models possess the capability to autonomously construct valid inputs and simulate execution flows for self-correction. Building on this, we introduce DryRUN, a framework that removes the necessity for ground-truth data by enabling the LLM to iteratively plan, synthesize its own test inputs, and run simulated executions, thereby mitigating algorithmic overconfidence. Assessments using the LiveCodeBench v6 dataset (post-March 2025) reveal that DryRUN achieves comparable performance to CodeSIM, a state-of-the-art, test-dependent baseline. Notably, it does so entirely without public tests or external execution signals, all while decreasing overall output token usage.

P：publictestoverconfidencevs自行生成input/模拟execution、不调用externalrunner分责，currentv2待v1。

### 2604.21677 — Geometric Monomial (GEM): a family of rational 2N-differentiable activation functions

原始完整AB：http://arxiv.org/abs/2604.21677v1

> The choice of activation function plays a crucial role in the optimization and performance of deep neural networks. While the Rectified Linear Unit (ReLU) remains the dominant choice due to its simplicity and effectiveness, its lack of smoothness may hinder gradient-based optimization in deep architectures. In this work we propose a family of $C^{2N}$-smooth activation functions whose gate follows a log-logistic CDF, achieving ReLU-like performance with purely rational arithmetic. We introduce three variants: GEM (the base family), E-GEM (an $ε$-parameterized generalization enabling arbitrary $L^p$-approximation of ReLU), and SE-GEM (a piecewise variant eliminating dead neurons with $C^{2N}$ junction smoothness). An $N$-ablation study establishes $N=1$ as optimal for standard-depth networks, reducing the GELU deficit on CIFAR-100 + ResNet-56 from 6.10% to 2.12%. The smoothness parameter $N$ further reveals a CNN-transformer tradeoff: $N=1$ is preferred for deep CNNs, while $N=2$ is preferred for transformers. On MNIST, E-GEM ties the best baseline (99.23%). On CIFAR-10 + ResNet-56, SE-GEM ($ε=10^{-4}$) surpasses GELU (92.51% vs 92.44%) -- the first GEM-family activation to outperform GELU. On CIFAR-100 + ResNet-56, E-GEM reduces the GELU deficit from 6.10% (GEM $N=2$) to just 0.62%. On GPT-2 (124M), GEM achieves the lowest perplexity (72.57 vs 73.76 for GELU), with GEM $N=1$ also beating GELU (73.32). On BERT-small, E-GEM ($ε=10$) achieves the best validation loss (6.656) across all activations. The $ε$-parameterization reveals a scale-dependent optimum: small $ε$ ($10^{-4}$--$10^{-6}$) for deep CNNs and larger transformers, with the special case of small transformers (BERT-small) benefiting from large $ε$ ($ε=10$) due to its limited depth and unconstrained gradients.

P：rationalsmoothGEMfamily及smoothness/epsilon架构尺度依赖，可能局部替代activation，不以小gains排除。

### 2604.21277 — Can MLLMs "Read" What is Missing?

原始完整AB：http://arxiv.org/abs/2604.21277v2

> We introduce MMTR-Bench, a benchmark designed to evaluate the intrinsic ability of Multimodal Large Language Models (MLLMs) to reconstruct masked text directly from visual context. Unlike conventional question-answering tasks, MMTR-Bench eliminates explicit prompts, requiring models to recover masked text from single- or multi-page inputs across real-world domains such as documents and webpages. This design isolates the reconstruction task from instruction-following abilities, enabling a direct assessment of a model's layout understanding, visual grounding, and knowledge integration. MMTR-Bench comprises 2,771 test samples spanning multiple languages and varying target lengths. To account for this diversity, we propose a level-aware evaluation protocol. Experiments on representative MLLMs show that the benchmark poses a significant challenge, especially for sentence- and paragraph-level reconstruction. The homepage is available at https://mmtr-bench-dataset.github.io/MMTR-Bench/.

EX：新maskedtextreconstruction任务与level-aware评价尚未给已有重要判断的混杂反证或模型/系统新机制；不能只因新benchmark且MLLM相关准入。currentv2发现而非深审。

## A7 Recurrent Transformer 21215v1 必要Source与Ch17逐字PRE（待独核）

精确[HTMLv1](https://arxiv.org/html/2604.21215v1)，实际§2.1–2.3/Eq1–2，§3.1–3.2限定表征，§4稳定性限定，§5/Fig3–4及AppC/Algorithms1–2，§6.1–6.4/T2，§7.1–7.3/T3，§9与D.1/E.3–E.4直接反侧。2+2+2=6，layer/runtime共同机制边界；具体Ch17长期gap故必要深入，不默认完整附录证明。

普通Transformer从layerinput构persistentKV，RT当前query/tempKV也从layerinput构造，但当前attention完成后才由同层output z构persistentKV给未来位置，K/V矩阵复用；区分temp self与persistentprefix避免当前输出自依赖。保fullprefix pertokenKV而非fixed-sizeRNN/压缩memory，不追加可见/latenttoken。是同层时间递归，不是depthsharedloop或toplayer反馈。§3仅ideal3xwidth条件近似simulate与局部dominantprevious/Videntity迭代，不意味着有限训练得到通用算法；§4 uniformattention单层/初始化结果不授fullmodel任意训练梯度保证。

同层queries能从已知layerinput提前parallel，persistentKV按位置揭示，online-softmax(m,l,o)向未来queryblock累积新tile；AppC P为整除t的最大2power，每pair一次。HBM movement Θ(N²)→Θ(NlogN)只固定维度/适用schedule，attentionFLOPs仍Θ(N²)，sequentialz frontier未消失，exact仅浮点重排容差。AppC Alg1省主定义的residualscale，不把伪码当完整可复现recipe。§6主实验singleH100/PyTorch compile无customkernels，batch512/seq512，perlayerlatency excludesembed/unembed/loss；Fig4 width1024/h16/b512，5runs+3warmup/SD<1ms，不是E2E服务性能。

直接代价：MLP每位置只有B个tokens，gradientaccumulation不增即时batch利用率；activationcheckpoint、preallocateKV+custombackward/CUDAGraphs均必付。D1 300Mnonembed 12layerswidth1408/h22与6layers2048/h32，ALiBi、seq512/B512；RTtrainthroughput42k/49k低于Transformer132k/153k tokens/sec，不能由tiling图称整个训练更快。§7.2称约3B但D1 300M约6B/25ksteps、E3 150M3B，保原口径差不补造。C4CE改善为作者受限结果，downstreamaccuracy多近random且有退步，不能替CE签通用推理。§7.3 fixedparam减layersα、width增sqrtα时KV减sqrtα是有条件推算，optimizeddecodelatency明确futurework。precision/SLO/concurrency/完整trainingseeds=Not Disclosed，未核代码/复现。

唯一owner `MODEL-TRANSFORMER-LAYER` Ch17。实际现文depthrecurrence/continuouspositionfeedback、高→低跨位置旁路、ACT/不同clock及statebudget等已覆盖，但没有‘同层output构未来persistentKV/当前tempKV’这个生产者边界，也没有queryearly条件下exactIO schedule与sequentialMLP代价。拟紧接现source-family2602-17993的高→低跨位置旁路整段之后、原ACT停止先验段之前补两段；Ch16保MLP成本、Ch18保outputnexttoken目标，不将同一机制重复写Ch19/22/49。

逐字PRE：

> 跨位置递归还可以发生在同一层的 KV 生产者上：当前位置先用 layer input 构造 query 与临时 self-KV，读取过去位置的 persistent KV，完成 Attention、MLP 与 residual 更新后，再由本层输出构造给未来位置使用的 persistent KV。临时 pair 只服务当前位置，持久 pair 才进入后续前缀，从而避免输出要先读取自身输出的循环。这保留逐 token、随历史增长的可寻址 KV，却让后来位置能读取本层已经加工过的过去状态；它不是同位置重复 block、压成固定状态或追加 thought token。<!-- source-family:SF-2026-ARXIV-2604-21215 -->
>
> 这种依赖仍让训练与 Prefill 按位置产生新状态，但同层所有 query 可由已知输入提前计算，因此可以把新揭示的 KV tile 一次累积到多组未来 query 的在线 softmax 状态。[必要机制与直接反侧](https://arxiv.org/html/2604.21215v1)中的调度减少 HBM 重读，不改变二次 attention FLOPs，也没有取消 MLP 的串行前沿；batch、checkpoint、kernel launch 与自定义反向均需计费。受测小模型的训练吞吐仍低于普通 Transformer，少层/更宽所推得的 KV 节省也不等于已实测 Decode 加速。并行训练或稳定延迟更重要、这些费用不能覆盖质量收益时，保留标准 layer-input KV 与固定 stack；表征可模拟和初始化稳定性结果不替代完整训练或生成验收。

未写Books、未占锁；待root必要Source/owner/逐字PRE及窄lease。

## A8 Evaluator-VLM Focus 21523v1 必要Source与Ch66逐字PRE（待独核）

精确[HTMLv1](https://arxiv.org/html/2604.21523v1)，实际§2.1–2.3（人工valid/invalid/scoreinvariant构造）、§3/3.1/T2、§4.1–4.8/T3–4/Fig2–4、§6与AppB/C.1–C.2说明。2+1+2=5；Ch66具体双轴差额必要深入，不把已有judge校准原则加分。

I2T600/T2I750原prompt来自各7benchmark，Gemini3.1Pro/3ProImage生成gold与扰动、人工含作者筛选valid subtle meaningful error/invalid obvious nonsense/scoreinvariant等5类，40dimensions/4000+是derivedperturbation数量不是独立prompt数或行业错误率。gold只要求足够相关非全完美，适合directionalchanges而非绝对truth。四judge Gemini3.1Pro/GPT5.4/ClaudeOpus4.6/Qwen3.5-397B-A17B共享prompt/highreasoning/wherepossibleT0，不是相同compute/latency成本。硬件/precision/outputtokens/concurrency/SLO及重复uncertainty=Not Disclosed，远端T0不保证确定性。

必须保留指标不同：single-answer的undetected为相关axes全‘不变’；pairwise为未唯一选gold（两序互换控position）；reference为给perturbedperfectscore。这三个定义不等价，single未计‘分数反向升高’也不能当全面正确。T3定向降质VP的pairwise较敏感，但§4.6无害SI的pairwise更不稳定/偏选一方，single反较稳，不采‘pairwise普遍更可靠’。轴/rubric可改变收益，rubric单独常无益。§4.4换goldreference I2T略退、T2I提升；§4.5加reasoning不单调且无trace解释，只记录操作差异，不归因‘overthinking’内部。§4.7 Gemini2.5Flash读Geminijudgejustification，只略补score漏检，非独立人类校准/全fourjudge证据。

有限支持：evaluator应按明确错误sensitivity和无害变化invariance双轴验收，referenceidentity/输出scorevs理由/任务条件独立记录。批量 perturbation制造/编辑/人工验证和多次judge成本不能省；不采用未知fullpromptimage中的tiepolicy或每维调用recipe，不宣实现复现或可靠rewardmodel。当前absv1无具名撤回/勘误；公开日Apr24联合资格见A3。

唯一owner `PLATFORM-EVALUATION` Ch66。实际‘Judge Ranking’已有self/NullPIR、近等质差额、sourcecue、measurementprompt漂移、人类alignment及动作细质量competence；没有同一输出受控降质vs无害扰动两种人口的sensitivity–invariance反向取舍，也未解释score没有反映已写进justification的错误不能直接放行。拟现source-family2602-00521的promptmeasurementstability段之后、原‘Judge自身的taskcompetence、directionalbias…’之前两段，Ch65/67交接仍evaluation配置与online观察，不重复评价归因。

逐字PRE：

> 对多模态输出的 judge，还应把两种不同扰动放在同一验收里：固定原任务、图像或文字依据，向候选注入应降低质量的细粒度错误；再构造保持任务质量的无害改写或编辑。前者检验错误敏感性，后者检验不应偏好一方时的稳定性。受限视觉评价中，成对比较对前一种变化更敏感，却可能在后一种人口里更容易偏选一方；不能据此把 single scoring、pairwise 或 reference-guided 中的任何一种升为通用正确判分接口。<!-- source-family:SF-2026-ARXIV-2604-21523 -->
>
> [必要协议与反侧](https://arxiv.org/html/2604.21523v1)中的‘分数未变’、‘未唯一选中较好项’和‘给错误项满分’是不同失败事件，应分别报告，不能把不等价的比例直接合成可靠性排名。理由中认出错误也不代表最终分数已经惩罚它，增加 reasoning budget 或换一份 reference 又可能改变结果。扰动生成、人工确认、双序比较与额外 judge 调用全计费；机器生成的 gold 和作者筛选不能替代目标任务的人类锚点。无法校准两种人口或错误未进入最终判定时，应保留分项指标、人工/任务专用评价及无排序结论，不由流畅理由或单一盲测胜率批准 reward 或模型发布。

未写Books、未占锁，待非作者Source/owner/PRE与窄lease。

## A9 定点事件去重更正（覆盖A5/A7/A8新增申请及A6中同事件P标签）

在Ch17发现21254/21999真实existing标记后，实际对本次具名ID核04-24/04-26/04-27原报告整行，而非继承旧Weekly候选或全月评分。发现04-24原小时窗本来含Apr24 08–09批次；同一有效事件已审就去重，不因本日自然窗再搬日、重计或重写Books。

因此21330/21215/21523为已有有效原事件：A5/A7/A8保留本次实际Source读取与未执行PRE历史，但撤回新增评分、Books申请，未获锁也未写入；原04-24的6分/Ch21真POST、6分/Ch22真POST、6分/仅报告保持，不被作者的临时5/6分覆盖。21882没有原行命中，A4仍真正新项。A6的27个具名P现作同v1事件去重，余13才继续本日准入/最小事实；不把currentv2/3当重要修订自动重开。

| 身份 | 已有有效报告整行位置与处置（不搬日） |
| --- | --- |
| [2604.20987](https://arxiv.org/abs/2604.20987) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；AGENT-PLATFORM [Ch84](../../../../../books/part-07-agent/84-agent-platform.md) |
| [2604.21308](https://arxiv.org/abs/2604.21308) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21505](https://arxiv.org/abs/2604.21505) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21232](https://arxiv.org/abs/2604.21232) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21251](https://arxiv.org/abs/2604.21251) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.20994](https://arxiv.org/abs/2604.20994) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；AGENT-MCP [Ch83](../../../../../books/part-07-agent/83-mcp.md) |
| [2604.21160](https://arxiv.org/abs/2604.21160) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；TRAIN-GRPO [Ch33](../../../../../books/part-04-training-system/33-grpo.md) |
| [2604.21794](https://arxiv.org/abs/2604.21794) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21829](https://arxiv.org/abs/2604.21829) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21725](https://arxiv.org/abs/2604.21725) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21741](https://arxiv.org/abs/2604.21741) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2604.21632](https://arxiv.org/abs/2604.21632) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-EMBEDDING [Ch12](../../../../../books/part-02-model/12-embedding.md) |
| [2604.21686](https://arxiv.org/abs/2604.21686) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21700](https://arxiv.org/abs/2604.21700) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.21724](https://arxiv.org/abs/2604.21724) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-EMBEDDING [Ch12](../../../../../books/part-02-model/12-embedding.md) |
| [2604.21590](https://arxiv.org/abs/2604.21590) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；TRAIN-DATA [Ch27](../../../../../books/part-04-training-system/27-data.md) |
| [2604.21611](https://arxiv.org/abs/2604.21611) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21579](https://arxiv.org/abs/2604.21579) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21593](https://arxiv.org/abs/2604.21593) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21598](https://arxiv.org/abs/2604.21598) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.20933](https://arxiv.org/abs/2604.20933) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.20915](https://arxiv.org/abs/2604.20915) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md) |
| [2604.20920](https://arxiv.org/abs/2604.20920) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；INFER-KV-CACHE [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2604.21428](https://arxiv.org/abs/2604.21428) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) |
| [2604.20913](https://arxiv.org/abs/2604.20913) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [2604.20854](https://arxiv.org/abs/2604.20854) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.20938](https://arxiv.org/abs/2604.20938) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21026](https://arxiv.org/abs/2604.21026) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.20917](https://arxiv.org/abs/2604.20917) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.20904](https://arxiv.org/abs/2604.20904) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；TRAIN-RLHF [Ch31](../../../../../books/part-04-training-system/31-rlhf.md) |
| [2604.20937](https://arxiv.org/abs/2604.20937) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.20985](https://arxiv.org/abs/2604.20985) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.20995](https://arxiv.org/abs/2604.20995) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21041](https://arxiv.org/abs/2604.21041) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21072](https://arxiv.org/abs/2604.21072) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；INFER-SCHEDULING [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [2604.21079](https://arxiv.org/abs/2604.21079) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.21083](https://arxiv.org/abs/2604.21083) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21098](https://arxiv.org/abs/2604.21098) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21045](https://arxiv.org/abs/2604.21045) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21057](https://arxiv.org/abs/2604.21057) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21100](https://arxiv.org/abs/2604.21100) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md) |
| [2604.21106](https://arxiv.org/abs/2604.21106) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；TRAIN-PRETRAINING [Ch28](../../../../../books/part-04-training-system/28-pretraining.md) |
| [2604.21131](https://arxiv.org/abs/2604.21131) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21139](https://arxiv.org/abs/2604.21139) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；WORLDVIEW-REPRESENTATION [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2604.21192](https://arxiv.org/abs/2604.21192) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21197](https://arxiv.org/abs/2604.21197) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21215](https://arxiv.org/abs/2604.21215) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md) |
| [2604.21221](https://arxiv.org/abs/2604.21221) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2604.21229](https://arxiv.org/abs/2604.21229) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21241](https://arxiv.org/abs/2604.21241) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21254](https://arxiv.org/abs/2604.21254) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-TRANSFORMER-LAYER [Ch17](../../../../../books/part-02-model/17-transformer-layer.md) |
| [2604.21255](https://arxiv.org/abs/2604.21255) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21268](https://arxiv.org/abs/2604.21268) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21276](https://arxiv.org/abs/2604.21276) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21327](https://arxiv.org/abs/2604.21327) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21330](https://arxiv.org/abs/2604.21330) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MODEL-MOE [Ch21](../../../../../books/part-02-model/21-moe.md) |
| [2604.21335](https://arxiv.org/abs/2604.21335) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21343](https://arxiv.org/abs/2604.21343) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.21346](https://arxiv.org/abs/2604.21346) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21395](https://arxiv.org/abs/2604.21395) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21326](https://arxiv.org/abs/2604.21326) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.21275](https://arxiv.org/abs/2604.21275) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；TRAIN-DATA [Ch27](../../../../../books/part-04-training-system/27-data.md) |
| [2604.21454](https://arxiv.org/abs/2604.21454) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md) |
| [2604.21477](https://arxiv.org/abs/2604.21477) | [原整行](../../24/README.md)；已有覆盖：非作者命题复核通过；PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.21480](https://arxiv.org/abs/2604.21480) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21523](https://arxiv.org/abs/2604.21523) | [原整行](../../24/README.md)；仅报告：受限机制/证据，不改长期正文 |
| [2604.21549](https://arxiv.org/abs/2604.21549) | [原整行](../../24/README.md)；整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21570](https://arxiv.org/abs/2604.21570) | [原整行](../../24/README.md)；暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.22074](https://arxiv.org/abs/2604.22074) | [原整行](../../27/README.md)；整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际写后通过 |
| [2604.22127](https://arxiv.org/abs/2604.22127) | [原整行](../../27/README.md)；整合：TRAIN-LORA [Ch30](../../../../../books/part-04-training-system/30-lora.md)，实际写后由非作者核验通过 |
| [2604.21999](https://arxiv.org/abs/2604.21999) | [原整行](../../27/README.md)；整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../../books/part-02-model/17-transformer-layer.md)，真实缺口 override、写后通过 |
| [2604.22032](https://arxiv.org/abs/2604.22032) | [原整行](../../27/README.md)；整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际写后通过 |
| [2604.22076](https://arxiv.org/abs/2604.22076) | [原整行](../../27/README.md)；整合：PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，实际写后通过 |
| [2604.22117](https://arxiv.org/abs/2604.22117) | [原整行](../../27/README.md)；已有覆盖：PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，保护纠错 override、非作者单篇通过；整日 Gate 待核 |
| [2604.22082](https://arxiv.org/abs/2604.22082) | [原整行](../../27/README.md)；整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，apr02 非作者实际写后通过 |

身份、精确v1、采用命题与未决未变才复用；原报告必要Source与实际POST已有有效结果，不因新查漏重跑。关键首三已实际定点读V3_EVIDENCE_NOTES.md同ID小节：21215明确temporary/input与persistent/output及queryearlytiling/未来decode限制；21330明确teacherbackbonefreeze/routerauxiliary、studentrealrouting和lastlayer/成本反侧；21523明确三metric不等与scoreinvariant反侧。其原Samev1结论与本次拟用命题未变，没有新勘误信号。不把这次必要Source重读当新增候选或新增Books成果。

## A10 非作者有限准入结果与旧EX定点复用（实际消息记录）

复核者`supp_apr25_review_fresh`，root明确有限任务后实际完成A6去重剩13，非本日报作者；本文件由作者唯一写入，如实记录已收到结论，不自授复核。

6项潜在贡献准入通过而非Source/date完成：21860（statelessmoderation实际路径/权限待核）、21191（prefixgrammar/ordinaryparser及nexttokenweights）、21911（instructionprior与vision因素受控区分）、21564（exactv1题名Coercion，v2才Persuasion；direct/debate×persona行为）、21836（stimulus选择改变convergence诊断）、21284（MemPalace具名纠错须核被批artifact与Recall/answer分母）。

7项EX：21193/DAVinCI实际最小读v1 §3.1–3.3：goldfullevidence或QA截span→现成NLI→confidencethreshold降NEI，未落出新内部归因/验证或可靠性条件；21003/LastHarness最小读v1 Algorithms1–2/§2.4/§3/结论：bestsofar evaluate/evolve再外套优化，未新执行/评价可信条件，实证是futurework。不是因无benchmark一刀切。

13内旧EX五21265/21677/21277/21134/21816＋额外21555有效复用：reader实际读旧screening当前裁决及21265/21677/21277必要evidence，六currentabs轻查无具名撤回/勘误；21277v2本身不触发。具体理由：21265组件迁移/预算未隔离且只有局部curriculum操作点，不因tiny；21677rational/smoothness局部算子选择未给新主线有效性条件；21277无prompt/视觉cue隔离不成立；21134结构specoracle与view已有路径组合未新truth/失效条件；21816模拟token与E2Eprojection未新admission；21555随机article/not扰动不保证语义恒定/唯一negation对照。旧必要原证保留，不重复评分/扩全文队列。

互斥Source：reader独占21860/21911/21836；作者独占21191/21564/21284及有限来源。21882必要Source/日期/Ch5已完成独核，未授日级。

## A34 保存完成态最小FINAL实际通过

非日报作者root已实际最小FINAL读回README完成态header/§1、SRC-ARXIV与Seed两资格源行、§5/6及收尾字段；确认新增15I/1NC/3D/1Only、15项真实非writerPOST、21921精确单族资格隔离和普通可执行工作0。本报告V3及cached/unstaged限定diffcheck均为0，root明确接纳完成态通过。此为保存后实际回件，不由作者自授；仅追加本条真实FINAL，不重复Source、POST或DAY，不启动下一日期。2026-04-25本日ownership结束，LS由root唯一更新；未stage/commit/push，未写LS/index，所有本轮Books窄锁已释放。

## A33 最后五项真实POST、完整DAY与完成态授权

非writer `supp_apr25_review_fresh` actualPOST：21360/21668实际顺读Ch23 158–178、242–264完整必要两侧、新168/170与252/254、1682–1696本人注，以及canonical books定点hunks/diffcheck0；21510/21481/21916实际顺读Ch66 581–599、874–896、4540–4566完整必要两侧与新段、4998–5014本人注，以及canonical books定点hunks/check0。五项逐字已核PRE一致，机制/限制/全费/原回退近文，未动旧行；Source/PRE必要审阅者准确为reader，root仅协调这五处窄lease，不称第三遍Source。root逐批接纳这五实际POST并释放窄锁；全日15新I真实POST齐，无本轮Books窄锁。作者仅行政同步本人注actualPOST/释放并实际读回，不再Source或POST。

非日报作者root实际完整六部分增量DAY通过：新20全部§4及§1/2/3/5/6、来源/查询停止边界、EX分层范围；15I/1NC/3D/1Only与21921资格隔离准确，15实际POST均通过。旧1身份/版本/采用命题未变层有效复用，不声称重新全文审老、不继承旧CLI完成标签替本次补查。root另实际机器核21=old1+new20、old1各一次/原窗口/连续old§4保留、14 Daily ID、引用0missing、围栏与六标题、V3/限定diff0。21916 exact-v1 h1被root独立确认为《MathDuels: Evaluating LLMs as Problem Posers and Solvers》，保本稿正确题名，不倒填v3。

root明确授权本次一次行政同步后保存完成态及§6 DAY通过，不要求第二次DAY或重复Source/全量静态：README的SRC-ARXIV/Seed结果均为受阻，但仅21921必要first-public资格隔离、不否定其余已处理目录/候选；21363/21931及最后五项POST均同步真实通过；21101必要位置改指A29/A31。作者于2026-10-16T04:13:12+08:00保存完成态，普通研究与Books工作0、外部资格/中心争议按具体重开条件保留。完成态首次V3提示结论必须单独成行、终态保留须明确“不支持正面证据/Books/无遗漏断言”，已仅修这两处词形，不改语义事实；原整行/连续§4匹配、21候选/14ID、本地164引用零缺失、唯一SUP无行尾空格及限定diff0。保存后最小FINAL尚待root实际读回，不预授其结果。未stage/commit/push，未写LS/index，未扩大来源或改动原候选整行/连续原§4。

## A32 最后保存位置与进行中六节稿检查（不预授POST/DAY）

21363/21931作者按root A26窄lease分别保存Ch26 208/210和note1826、Ch23 1077/1079和note1680；root actual新两段/完整局部前后/两本人注与限定diff0通过，修订ILP记录及检测/连续速率人口准确，释放两窄lease，本日10项新实际I有效。作者仅行政同步两note实际POST/释放并actual读回。

root复用reader实际Source/owner/PRE层只协调A28三项/A29两项共五窄位，不第三遍同Source；作者apply_patch逐字保存：Ch23 PTA168/170（15494后/19209前）、SMD252/254（13119后/02870前），本人注1688/1690；Ch66 DVA587/589（AgentDevel后/coverage前）、TTS884/886（clusteredanalysis后/切片前）、MathDuels4552/4554（24780后/Aggregate前），本人注5004/5006/5008。作者实际完整顺读这五局部两侧、本人注与限定diffcheck0，原文无删改。已向root及reader提供准确保存位置；这些五项当时尚未实际POST，不称reader执行中/通过、不预释放窄锁。

README已融入原六部分进行中稿：21正式（原1＋新增20＝19arxiv＋DeepSeek）、本次15整合正文已保存/10POST有效/5待、1NC/3中心D/1Only，21921资格缺口不计formal。V3初次指出进行中decision词形与DeepSeek同标题不一致，已最小修正并复跑通过，不掩初次错误；本地引用163个零missing、原Kimi整行一次/连续原§4匹配baseline、14清单源＋MemPalace实际触发、限定cached/unstaged diffcheck0。唯一SUP复制原表的Books相对链接41处按本日实际目录机械修为五级，未动原记录/原README原行/既有diff。校验只格式与可判一致性，不是语义DAY；5POST与整体DAY/完成态FINAL仍普通待办。未stage/commit/push，不写LS/index。

## A31 A29三项非作者实际必要层结果（非全篇第三审）

非writer supp_apr25_review_fresh按root分配实际独核：
- 21101仅§4至Remark1及AppC1 Eq9/Lemma6–8/Thm4影响桥：C_J乘积条件与h/T/M/N依赖确未闭，认可5分争议/暂缓边界；未扩C2/C3或科学实验，不称全篇Source重核，不EX/不否定局部构造与实验。重开精确依A29。
- 21510 actual v1§3.1/4.1/4.3/5.1–5.2T4/8/F2.1–2.2与actualCh66 574–590：code-onlyblind≠AgentDevel implementation-blind；emptydiscrepancy非truth、无单独blindness同calls消融、goldschemakeys与modeljudge/时间成本边界准确；5分Source/actualowner/原字PRE通过，尚非已写。currentabs无notice actual轻查/日期同批合证复用，未核code/复现。
- 21481 actual v1§3.1–3.4/T1、§4.1–4.4/T3–4/defaultvoices与actualCh66 864–890：rater×sentence与相对fullrank/BT-CI两个目标差额成立；系统数与language/voice/cluster/tie/关联及费用边界准确，5分Source/actualowner/原字PRE通过，尚非已写。currentv2无notice actual轻查/日期合证复用，未核artifact/复现。

本文件仅作者唯一writer按真实消息持久化；root仍负责字面/插点lease及日级验收，未自授完成。21510/21481不再重复Source，21101只保影响桥的独立核验范围。

## A30 最新已发生POST、EX/Only与资格隔离（不是日级验收）

21444/21716 root非writeractualPOST通过，分别实际Ch23 1207–1218完整FlexMem→新→eventadmission＋1673–1679本人注，Ch66 680–692完整cue→新→context＋4988–4997本人注，逐字A25一致/限定diffcheck0。21144 root字面/插点授source26622后两段lease、只加exactv1追溯link；作者保存Ch77 632/634与1840注后，reader supp_apr25_review_fresh actual618–666完整render→new→entity owner/codeblock/限制、1836–1844note及限定diff，POST通过，root接纳释放。上述三本人注作者只行政同步实际POST/释放并actual rg读回，不重第三次Source；本日8项新真实I通过（非DAY），当前无已写未释放锁。

21152 root实际必要Source/T1/A2及Ch66 258–266/680–692具体NC通过，只保cue-conditioned输出与分母/拒绝类型；中心lexicalgate/jailbreak不因自动proxy获因果地位。21282 root actual Alg1/§5.3/T3/§5.4/T4/§5.7具名安全费用门校准通过EX，支持/反侧保留，不重读附录。DeepSeek A18经reader actual官方Apr24核心+updates独立段、root接纳4分/已关闭/Only；API事实改为“显式model ID与mode”，**不是不可变snapshot**，当前标Apr24页面不声明April历史原字节冻结，未测API/权重、不追timeout或June。

21921 root接受本日资格隔离：Apr24 arxiv公开不能消早project/Seed Apr23疑问；复用旧exactv1题摘/§1–2及project核心有效层，不评分/不列确定candidate/不Books；重开需同身份早正文/项目release可核日级与内容归属，只重该族，不全月/全年追日期。A26 21931 PRE已按root精确分开检测的“人工标注+音频弱标签一致筛后人口”与连续速率网页title/description小样本，删除误写“人声”；其余字面不改，尚待lease。

## A29 最后三项G准入后的必要Source与Books判断（root尚未Source独核）

root已actual门核A17三项准入，不等于这些具体证据/owner完成。作者独占必要层；不扩全部证明或无关科学应用。

### 21101 HNODE — 2+1+2=5，中心稳定桥争议/Books暂缓提议

actual [exactv1](https://arxiv.org/html/2604.21101v1) §2.1–2.3/Fig1–4、§3、§4 Eq1–6/Thm2–4/Remark1、§4.1训练与AppC1（只因拟采用gradient稳定必要桥，不遍历C2/C3或领域附录）。mixedFEM/mortar/SBP construction是实际新接口，保为有意义潜力而非Science题域EX；**局部架构与实证不因下述争议一刀切无效。**问题是关键“固定stage/mesh下任意长rollout不爆梯度”的保证未由所读必要桥闭合。Thm4条件inf-sup、N-inputJacobian bounded；式界 Ch^-3/2 Rmax(exp(cT/M)-1)，h=Δt/M、ΔtN=T。固定h/M后T随N增长，含指数T的界不支持uniform-time常数；固定T增加N又缩h，不能同时宣固定h。AppC1 Eq9与Lemma8后，将 Σ C_J^k(1+ch)^k 直接换为 C Σ(1+ch)^k，没有给C_J≤1或独立N可吸收C_J^k的条件。这里只指出实际证明步骤缺条件，**不声称已推翻所有定理/实验**。

Thm2仅N=V'(u)离散Hamiltonian、Thm3特定elliptic dissipative；正文说transformer无约束学到stable不是普遍继承保证。Lorenz单trajectory/同initial rollout，点wise超1Lyapunov本就不准，仅attractordistribution；shear1120 trajectories/224test、69M vs4.5B预训练PhysiX非同预算/先验，训练singleH200八天，其他precision/repeats/SLO未披露；fusion9000x是surrogate对PIC非一般LLM。未核code/复现。日期A22/v1processingApr24/currentv2无notice reader题摘层复用。

actualCh25 90–96含latentconfiguration/dynamicsfiber与受限多branchphysicsfit分责，207已有条件futureobservation非actionfact；新连续autonomous integrator和理论稳定若成立有潜在差额，但本次不把未闭的保证灌入owner，也不借成熟“保observed/imagined分责”强行改书。有限construction只报告，不授开放action-conditioned worldmodel/physicalcontrol。暂缓只隔离中心uniform-gradient/通用稳定采用，重开需补C_J乘积及h/T/N依赖条件的修正证明，或明确退回有限经验稳定并给对应受控非领域特有对照。root需实际独核该桥与暂缓边界，未自授。

### 21510 OptiVerse/DVA — 2+1+2=5

actual [exactv1](https://arxiv.org/html/2604.21510v1) §3.1–3.2/§4.1–4.3、§5.1–5.2/T4、§8、F2.1/2.2；前半benchmark不是仅题数，采用只限DVA信息隔离的audit接口。1000教科书/论文优化题，经OR/数学研究生人工核、5minGoogle可搜solution排除不授无污染；22models/多solver sandbox。DeepSeekV3.2Chat抽取/判分（500校准样本98.4%）与relative tolerance.1%是模型judge不是独立真值；F2 keys来自gold schema、可判非数策略等价。DVA problem+initialmodel提requirements，不见problem code-to-math，再合成discrepancy conditionalrepair，空集合非语义correctness保证。T4三backboneeasy/med/hard较CoE/OptiMUS有局部改善，但无仅移除blindness的同调用ablation；DVA30.2/58.8/67.3s vsbaseline6.1/11.8/15.7s，不采无显著额外时间。conditionalrepair率23.6/32.3/28.5是特定人口，不给一般独立因果。模型版本/硬件/precision/总tokens/重复CI未充分披露不补造；未核code/复现，日期A22同batch联合而非Submitted单证。

actualCh66 583–585 AgentDevel是critic不看implementation只读requirements/trace症状；本项反向盲支路只看code不见problem，再三方对照，不是同机制，owner PLATFORM-EVALUATION-SYSTEM。拟这两段后/coverage控制下一轮代码上下文段前，两段未写/无锁：

核验生成的程序，还可把“需求应当是什么”与“代码实际表达了什么”交给不同可见集的分析分支：一侧从问题和初始建模提取遗漏要求，另一侧不看原问题、只由代码逆向描述变量、目标和约束，最后再比较两份表示与原需求。有差额才提出修订，能减少重读原意时把代码解释成“本来想写的样子”的机会；但盲回译仍是模型生成的解释，不是程序执行语义或独立正确性证明。<!-- source-family:SF-2026-ARXIV-2604-21510 -->

[必要语义审计与对照](https://arxiv.org/html/2604.21510v1)支持这一信息隔离接口，而非保证每次差额集合为空就可放行。原比较没有单独隔离盲分支与额外调用的收益，结果仍经模型抽取和参考答案 judge 判定；可运行、数值接近参考与忠实实现原需求必须分开验收。需求提取、代码回译、综合审计、条件修订与重新执行均计费；要求含糊、回译与原程序不符或 oracle 未校准时，保留原代码、可执行测试、人工规格审核与独立求解核验，不让审计者给自身修订签发真值。

### 21481 VoiceFirst TTS — 2+1+2=5

actual [exactv1](https://arxiv.org/html/2604.21481v1) §3.1–3.4/T1–2、§4.1–4.4/T3–4/Fig1–5与Conclusion。5357sentences/10languages，7systems支持2–10lang不同，defaultvoices同gender不等同voice；1915screenedraters/120kcomparisons。先锁holistic再六维并不独立；BT MLE+500bootstrap95CI/nonoverlapstrictbetter，未披露完整cluster/bootstrap unit和tie映射。Rank一致参照fullleaderboard而非oracle：rho .95，5systems约200rater但7约100，不支持numberofsystems单调quota；fixed200rater，分层language采500/1000sentence，rank稳定可早于scoreCI收缩。SHAP/XGBoost预测overall，语言holdout86.1%是关联非知觉因果/独立测试真值；domain/input有reversal，缺supportedlanguages不授统一总榜。speechmodelinference硬件/precision、样本独立重复未披露，人审/语音制备/重采样成本全计。未核artifact/复现。日期A22 v1Updated/createdApr24与公告/month身份合证，currentv2无具名notice。

actualCh66 864–888当前SE示意/同prompt用户cluster匹配bootstrap与slicevariance并无rater-vs-stimulus采样轴/排序稳定vs分数精确联合目标，具体差额成立；owner PLATFORM-EVALUATION-SYSTEM，拟原clusteredanalysis段之后/“切片越细”之前两段：

多人偏好评估的样本量至少有评审者与被评刺激两个轴；排序稳定与分数精确也不是同一个目标。固定一份完整评价作为参照，可以分别增加评审者、或固定评审者后增加分层采样的输入，记录相对参照的 rank correlation 与分数区间宽度。排行先趋于稳定而区间仍宽，说明继续收集的价值可能已从决定顺序转向估计相邻差距；高相关只表示接近该参照人口，不使参照榜单成为客观质量真值。<!-- source-family:SF-2026-ARXIV-2604-21481 -->

[受限多语语音偏好对照](https://arxiv.org/html/2604.21481v1)中，这些变化还依赖被比较系统数与语言覆盖，不能把观察到的评审者或句子数当作通用配额。默认音色、支持语言和原评价人口不同，也会改变总榜；同一人先给总体偏好再给分项评价并不产生独立证据，解释模型的 SHAP 权重更不是知觉因果。额外招募、筛选、生成音频、分层标注与重拟合均付费；人口或候选系统改变时，保留逐语言/输入分项、原始偏好及不确定性，重新校准量尺，不由稳定名次批准部署质量或免除独立任务验收。

## A28 reader其余四项必要Source/owner与三份逐字PRE（实际消息，未写）

非writer supp_apr25_review_fresh独占actual exact-v1，无作者重复全文；Source权限只覆盖所列必要范围，不授DAY/复现。日级A22同批publisher projection/公告月列表联合资格，currentabs后版无具名notice实际轻查，v2/v3不倒填。root已收到21901中心争议并接纳，三I仍待root字面/插点lease。

### 21360 PTA

actual §3.1–3.2/Eq1–7/T1–2、§4.1/4.3–4.4、A3–A5/A8，2+1+2=5。**纠正A16初始描述：旧cache本来固定M/class（MC×d），并非随sample无限增长；PTA变C×d聚合状态，另anchoredC×d，仍随C。**CLIP confidence对全部C类EMA，β=1−exp(−s/h)/h20；Pa文本初始化但Eq5左右同Pa，不宣硬锚定几何不变。原CLIP概率+prototype概率，无encoderbackprop。ViTB16/ULIP、B1、3090、3顺序/seed，部分引用baseline非重训；T2平均65.61略低ADAPT65.64。A4stream计时非请求SLO，A8非平稳旧状态滞留/reset未来工作，shuffle非突变域稳定。actualCh23 164–166已有改参数ProtoTTA15494，缺冻结encoder每类聚合读出替MC样本缓存；owner MULTIMODAL-REPRESENTATION，拟15494两段后以下逐字：

不反传的适配也可以只更新类别读出状态：把每类保存多个测试样本的有界缓存压缩为每类一个聚合原型，再按原冻结模型对各类的置信度，缓慢吸收当前样本特征。状态从与每类缓存容量和类别数共同相关，变为主要随类别数增长；它节省样本级检索，却失去逐样本保留和精细淘汰能力。文本初始化的原型读出与原始零样本分支可以并行保留，但置信度、插值与分数相加都不证明伪标签正确或旧预测不变。

这种状态更新把梯度预算换成流顺序、平滑速度与历史遗留的压力。受限图像与点云对照支持其可行性，但部分切片仍弱于已有方法，随机打乱稳定不证明突变域下持续可靠；过快吸收会偏置，过慢又会滞后。类别原型、原始分支、初始化和更新规则应共同保存，分别验质量、完整流费用与漂移后的恢复；分布改变或聚合失准时，保留冻结读出、有界样本缓存或经验证的重置策略，不由无反传批准终身适配。<!-- source-family:SF-2026-ARXIV-2604-21360 -->

### 21668 SMD

actual §3.1–3.2/4.1–4.5/T1–7必要机制/主控/消融/费用/反侧，2+1+2=5。22joint位置→pelvis/bodyframe→26angle时序/13parts，smooth7@20fps，threshold.03m/15°/5°，top3约1k vsall26约4ktokens。无learnedmotionencoder不是trainingfree：Qwen2.5-7B QA/caption各自LoRAr16约40M/5epochs，H200 QA7h/caption20h。QA重制max10choices，MotionGPT3Qwen同backbone不全pretrain/compute匹配；不采learnedencoder本质跨域脆弱。top3 QA优但captionR1弱，去trajectoryCIDEr微升，不全指标同向；attention非因果。915–1154ms限H200/QA32outtoken，priorpipeline时间含估算。actualCh23 244–246 camera-motion learned旁侧读出不含规则全骨架分段运动文本；owner MULTIMODAL-REPRESENTATION，拟其后/02870前两段：

若输入已经是可信的骨架轨迹，还可把接口前移到确定性描述：在约定坐标系中计算关节角与全局位移，再按时间切成变化、保持和重复事件，用普通文字交给语言模型。它用可检查的规则描述替代学习过的运动编码器和投影层，而不是从文字补回未观测运动；坐标系、平滑、阈值、关节选择与时间范围共同决定哪些信号被保留。标准文本降低了更换语言主干的接口耦合，但任务 LoRA 和监督仍需重新训练。

规则化也会丢信息：只保留最活跃关节可缩短输入并改善受限问答，却可能损害需要完整动作细节的描述任务；阈值附近或细微运动不能由文本可读性担保。现有同语言主干对照支持这条替代路径，不隔离全部预训练与预算差异，也不证明学习式编码器必然跨域失败。较长文字序列、规则处理与任务训练均付费；描述粒度或输入域失配时，保留原轨迹、较完整描述或经验证的专用编码器，并用独立任务结果验收，不让注意力热图替代因果解释。<!-- source-family:SF-2026-ARXIV-2604-21668 -->

### 21901 GiVA — 5分中心争议/暂缓

actual §3.1–3.2/Eq1–5/AppA、§4.1–4.2/T1–3、4.4/T6、§5–6。Γ=diagγ，但Eq3→4梯度当full GAᵀBᵀ，漏diag投影；令C=BA，真γgrad_i=<G_i,C_i>，首步为diag(rowinner(G,C))C而非GCᵀC。reader actual算术反例 G=diag(2,1),r1,A=[1,0],B=[0,1]ᵀ满足所述topA/正交B，却真首步0/误差²5，而Eq4给diag(2,0)/误差²1；B=[1,0]ᵀ才实现后者。AppA只证Eq4放松问题，不是diag训练，“任意正交B实际首步最优”未闭。**不说所有实验无效。**三次/LRsweep与局部对照保，instruction单seed/MTBenchref loss选LR、code弱LoRA；全gradient/SVD/每task A/B成本，vectorckpt小非整个adapter小，T6非普遍快。actualCh30 96–145已有taskbasis/固定A训B；双basis固定训ΓΛ有潜在差额但中心选择理由未闭，本次不写，不当NC。root接实际独核争议，保2+1+2=5/争议暂缓，不正面Books；重开需修正diag约束推导与B资格，或改述实证启发式并补对应必要对照。只隔离中心最优性，不抹掉有效局部实验。

### 21916 MathDuels

v1实际题名 **Evaluating LLMs as Problem Posers and Solvers**，非当前v3 A Self-Play Benchmark That Grows。actual§2.1–2.5/§3.1–3.2/§4.1–4.3，2+1+2=5。19models/9providers、30题each570、11invalid去后559×18=10062；T1/mathverify/GPT5.4high verifier，10k按authorbootstrap、meanrankrange5.05/19只固定题池。至少一nonauthor答案不等authorgold才核，全体共错gold避查；414disagreement重放Gemini exclusion97.5/answer99.4是触发子人口一致率非全池truth。Rasch solver-item拟合；authorrating派生自题难度均值、错gold收益封顶，.5+.5目标选择非通用出题能力。§3.2 two newcomer作者275题与§3.1每人30/all570冲突，不采3.4x/自动难度上升。actualCh66 4537–4563已有peerquestioner/answerer/verifier及IRTanchor，缺author按对手难度给分/错gold封顶/只disagreement核验盲区；owner PLATFORM-EVALUATION-SYSTEM，拟SF2607-24780marker后/Aggregatescore前两段：

自适应出题还可以让同一模型分别作为作者与解题者：由其他模型回答它生成的题，用解答矩阵联合估计题目难度和解题能力，再把所出题目的平均难度作为单独的作者分数。作者自己的解答不参与该矩阵，错误参考答案对应的出题收益还须限制；但这个派生分数仍依赖对手人口、题型与测量模型，不是脱离题池的通用创造能力。解题与出题可以分轴呈现，等权合成只是评价目标的选择，不能自动产生客观总榜。

[受限自出题协议](https://arxiv.org/html/2604.21916v1)也暴露了核验人口的边界：只在求解答案与作者参考出现分歧时追加 verifier，会漏掉所有模型与错误参考一起达成共识的题；另一 verifier 在已触发题目上的高一致率，不能消除这类未触发错误。原文新增模型题数的口径不一致，因此不采其自动抬高难度上限的定量结论。出题、全对手求解、符号判等、核验与重采样均付费；更新题池时另验参考真值与量尺可比性，保留冻结题库、独立人工 anchors 和原始分轴结果，不用共同认同或综合名次自签正确。<!-- source-family:SF-2026-ARXIV-2604-21916 -->

## A27 reader21144必要Source/actual owner与逐字PRE（消息实际范围，未写）

非writer supp_apr25_review_fresh actual exactv1[21144](https://arxiv.org/html/2604.21144v1) §3–7/方法T1–2、Fig5/7与直接failure，建议2+2+2=6。IndiRef-MU N50/category共200；agenticsegmentation下text/image但视觉另CLIP图文α=.9，非纯modality/全预算对照。New/Continue/Skip、两speakerPOV、示意图+nondepictablemetadata/crossscene triplets；Constructor每次5候选+Qwen3VL32B自验证，QwenImageEdit8steps、judgeLlama3.1-8B/3A10080G。T1spatial text表.26与叙述.28不采用精差；hybridinferred.52低于image.58。faithful局部图仍只取起点/missinglinks/negationSkip失败，生成图不是真实观测。未核代码/复现/SLO。日期A22Apr24v1/created与公告身份同批合证，firstpublic资格待统一对账，非APIcreated单证。

reader actualCh77 618–632已有确定渲染/原文回读，缺可描绘与命题分工/POV增量状态差额；owner AGENT-MEMORY，拟source26622段后/长期视觉流entity小标题前，reader未写/无锁；以下逐字PRE原消息持久化，待root字面/插点窄lease：

派生视觉记忆还可以外化当前的场景解释，而不是只把原文确定性渲染为图像：按说话者视角维护逐场景示意图，以新建、续写或跳过决定更新范围，并把否定、不确定性与跨场景关系留在文字元数据和显式链接中。可描绘的空间状态与难以描绘的命题因此承担不同职责；但生成图不是新环境观察，候选图的自验证也可能与生成器共享误解，不能取代原对话证据。

这种分工改变了检索的失效面：局部图像忠实，仍可能只取回起点场景而遗漏后续关系；跳过一句否定也可能留下错误状态。[受限对话实验](https://arxiv.org/html/2604.21144v1)中，图像、文字与混合表示各有胜负，且视觉与文字检索配置并非纯模态单变量对照，不能推出图像记忆普遍更准或更便宜。生成多候选、验证、视觉索引与读取的成本，应与关系链接完整性、原文回查和文字回退一起验收。<!-- source-family:SF-2026-ARXIV-2604-21144 -->

## A26 21363/21931必要Source与具体owner逐字PRE（未写）

### 21363 HiCo-Nav

2+2+2=6；actual [exactv1](https://arxiv.org/html/2604.21363v1) III-A–E/Eq1–24、IV-A–F/TI–V。新增不是异步一词：实时感知/CMG记忆/慢VLM线程三层，YOLOWorld+MobileSAM+LiDARSLAM对象点云，object/visualanchor二部图；3DIoU+CLIP合对象、ILP weightedmulticover最少anchors，且每已检测对象至少min(r,该对象现有anchors数)次覆盖（Eq6下界，Eq7截最低要求，非上限），不保证semanticcompleteness。按target/relatedobjects优先子图；Qwen3OmniAPI独立线程不断读，没披露snapshot/oldanswer取消或effect-time安全guard，不能替作者补。frontier结构语义Gaussian与outofboundaryRGB CLIP关联不是目标概率；utility minmax/exponential权重不归一概率。WTRP weightedcumulative latency（不是roundtripallcities），LKH启发式后只首目标交A*/localplanner，distance/heading/vmax是nominalcost，非障碍全局最优或安全证明。

实证：Habitat HM3D2000/MP3D2195/OVON3000/TextNav；有SR/SPL分别，HM3D full31.8低于Apex33，TextNavfull27.8/12.9vs去WTRP25.4/11.8。失败differentfloor13.9/18.5、falsepositive19.7/8.8、stepout/noFrontier，图2D不能跨楼。效率只HM3D前100/RTX5090+Ryzen9950X3D，onlineQwenOmni21.5s/0.22sframe vslocalQwen3VL8B27.8/.23，API远端硬件/precision/SLO、重跑/CI未披露；不将桌面本地解释为Jetson全链。Unitree真机Mid360+D455+OrinNX/onlineAPI，两组各20指令large95%/small65%，perception10FPS/anchor1–2s不认证云最坏时延或碰撞率。未核artifact/复现。A22Apr24v1与公告/月列表同批合证/currentabs无notice reader有限层复用，非Submitted单证。

actual唯一owner MULTIMODAL-EMBODIED-VLA Ch26 194–213已有多时钟/LiveVLN guardprefix与backuptail，尚无“目标找到即可停”对应weightedlatency与CMG分批推理接口；Ch25开头environmentstate与Ch27data交接已读，不将memory图算worldmodel。拟LiveVLN两段后、原HierarchicalGenerativePlanner小标题前，以下两段：

把慢推理移出控制关键路径，并没有回答“接下来先去哪里”。若找到目标即可提前结束探索，最短巡回路线或逐次最高语义分都可能错配目标；可以按候选区域的任务相关权重，最小化访问到各区域时的累计行进代价，而不是要求走完所有区域。高层从视觉 anchor—对象关系图分批读取任务相关子图，在另一线程提出目标及位置；快速感知和局部 planner 继续处理当前观测。这是一条加权发现顺序与分层执行的接口，不是把 CLIP 相似度认证成目标存在概率。<!-- source-family:SF-2026-ARXIV-2604-21363 -->

[HiCo-Nav 的必要机制与反侧](https://arxiv.org/html/2604.21363v1)中，anchor 多覆盖约束只覆盖已检测对象，ILP 压缩不保证未见细节；语义权重和启发式路线也不保证真实最短发现时间。二维地图、误检、小对象与运动模糊仍会失败，桌面计时和少量真机指令不认证云 API 最坏延迟、跨层状态一致性或碰撞安全。检测、建图、子图重读、VLM 与规划均计费；观察陈旧、语义排序失准或低层无法安全执行时，应重新观测，保留几何 frontier、较简单的贪心/固定策略与独立 controller，不能让持续推理本身批准动作。

### 21931 Seeing Fast and Slow

2+1+2=5，采用命题限时间表示/感知标注，不将生成SOTA/重构当主分。actual [exactv1](https://arxiv.org/html/2604.21931v1) §3.1–3.3/Eq1、§4.1–4.2/Eq2–3（理解消费交接）、§5.1–5.5/T2/T5–8、§6、AppC1–2。8k原声pitch速度变化弱标签→VideoMAEv2 binarydetector推理无audio；speed equivariance logloss只相对尺度，Adobe240knownrates校准。slowextreme三轮加速再估计；SloMo44632clips/18Mframes经shot/OCR/CGI/quality过滤/InternVLcaption派生，不是每片有captureGT。§5.1四人重标签且只留与audio一致样本，92.4%只此筛后人口。§5.2 111video playbackrate由网页title/description确认；modelPearson.735/logRMSE.649 vs人.880/.492，no universalclock。§6明确limitedmotion/刻意慢动作误导。训练/迭代/人审费用保，不造speedestimator硬件/precision/SLO。

生成仅交接：Wan2.1I2V14B480P speed10logbuckets+.01–1range timestepemb与frame-index·speed，LoRA/linear训4GB200两天；video224/56pairs×4speeds，FID/FVD只48具GTtriplets，不以光流幅度顺序证明绝对速度/物理正确；ATI额外basegeneration/tracking条件不全匹配。superresolution8x与bluraveraging不授真实新细节；本次不新写codec/generationowner，不采fullqualityclaim。未核代码/复现。

actualCh23 1062–1084已有sampletimestamp/frameinterval/clock/sync/augmentationidentity、Event感知N-count窗口，未承载playbackspeed/场景运动/采集clock分责及equivariance需要绝对scaleanchor；Ch24开头generationcontract只作交接。唯一owner MULTIMODAL-REPRESENTATION，拟200ms/augmentation句后、Event sensor段前两段；未写无锁：

视频文件的帧率、播放速率与场景本身的运动速度也不是同一个时间标识。一个受限感知分支先借原声随变速产生的音高变化，生成速度切换的训练标签，再训练只看画面的检测器；估计连续播放速度时，则令同片段被加速 k 倍后的预测也乘 k。这个等变约束提供相对尺度，仍须用已知播放速度的样本校准绝对值；内容本来移动缓慢、配乐或配音都可能破坏所借线索，不能由看起来慢就恢复真实 capture clock。<!-- source-family:SF-2026-ARXIV-2604-21931 -->

[必要监督与直接反侧](https://arxiv.org/html/2604.21931v1)把这一估计用于慢动作数据标注。速度切换检测的筛后测试只保留人工标注与音频弱标签一致的片段，不代表所有视频；连续速度测试中由网页标题/描述确认的少量速率，也不是任意片段的独立物理真值。多次变速再预测能改善受测误差，却增加重采样与模型调用；较低误差、光流有序或生成画面更平滑，都不证明事件动力学已真实恢复。应保留原片段、采样/变速 lineage、标签来源及不确定性；缺运动线索或时钟资格不清时，回退可信元数据、已知速率采集与人工核验，不让派生速度标签重写原始观察时间。

## A25 21444与21716必要Source/具体owner/逐字PRE（未写）

### 21444 HiCrew

2+1+2=5，实际[exactv1](https://arxiv.org/html/2604.21444v1) II-A/B/C Eqs1–4、III-A/B/C/TI–II、IV，必要到组合机制与直接ablation反侧。shotboundary保持outer顺序；question-relevance GPT4o选score>2.5镜头内部EVACLIP8B KMeansK2/maxdepth3；frame代表为visualcentroidnearest，1FPS。question set按Causal/Temporal/Descriptive分组，LLM造对应visualprompt、BLIP2(Ego)/LaViLa(NExT)字幕；highrelevance占比>40%选breadth否则depth。层次Agent规划只是派生调用顺序，0.7visualweight/conf不能当真实性或因果方向。mainGPT4o，Ego71.6subset/64.6full，NExT79.5；主干相同不隔离otherbackbones/data/budgets。w/oHybridTree换uniform采样58.7，去Qcaption59.2、去planning62.0对full71.6，但没仅保/破temporalorder匹配输入对照，不能独归时间拓扑或免费动态规划。平均1.3round/max15不是endtoend成本；hardware/precision/全模型tokens/CI未披露，不补造。未核代码复现。日期A22 currentabs reader无notice/v1同批Updated Apr24与month/announcement联合资格，不用Submitted独证。

实际owner MULTIMODAL-REPRESENTATION Ch23 1205–1223：fixedclip FlexMem KV/记忆与事件admission、主动观察已有，缺离线shot orderedouter＋query-local聚类/字幕的表示选择。Ch22状态容量与Ch24生成交接已读不挪owner，Ch75 203–205已有按时间范围/密度主动读取而非本机制。拟在FlexMem两段后、原“持续流还可在写入前选择”前两段，未写无锁：

如果视频已完整取得，还可把压缩接口分为两层：外层按镜头边界保留原时间顺序，内层只在问题相关的镜头中进一步聚类展开，并用问题类型指导字幕和细节读取。这样减少全局聚类把相似但不相邻画面混到一起的风险，同时让表示容量按 query 分配；镜头边界、相关等级与字幕仍是派生判断，不证明所有真实事件或因果关系已被保留。<!-- source-family:SF-2026-ARXIV-2604-21444 -->

[HiCrew 的受限方法与对照](https://arxiv.org/html/2604.21444v1)支持这种有序外层与局部细化的组合，但移除整棵树的消融还改变采样与层次细节，不能把全部差额唯一归于时间拓扑。问题集合参与字幕生产，也使该表示不再是任意未来 query 可直接复用的通用索引。镜头检测、encoder、相关评分、多类字幕和后续 Agent 调用均计费；主干相同不等所有输入与预算可比，平均推理轮次也不替端到端开销。短事件、切段或字幕遗漏时，应回读原片段、补密集采样，保留均匀读取与固定流程，不让有序树或解释轨迹自行批准视觉事实。

### 21716 Code-generation bias

2+1+2=5，actual [v1](https://arxiv.org/html/2604.21716v1) §3/4、§5/6/7.1–7.6、Limitations、A1/B1/B3必要反侧。7datasets×50promptvariants350、最多11nonsensitive＋3nonsense属性，随机order，if vs MLP/RF/SVM/tree/logistic任务形态；9localmodels＋主结果GPT5mini，greedy/max512/batch128/4H100、1–2hours（runtime依model）；最大attributes实验max2048。CBS按生成代码使用属性，不是执行后harm或合法性。Gemma3-27B extract输入特征，A1单作者annotated126samples（63/codeform）选98.41%，不能假设各形态抽取误差相同。B3两套各90pipelines（main/SpecificCoT）都普通predictivefeature非fairness-aware用途，不能证明所有使用敏感字段一律harm。正文88.3/83.3及abstract87.7、conditional58.7/59.2不一致，不采统一倍率/人数统计；局部方向与prompt/attributecount/difficulty切片保留。§7.5 biased samples要求至少2敏感字段、unbiased由删字段prompt生成，不能把相近识别分数当相同generation内部知识。Limitations明确未全面exec/train，proxies可遗漏；未核实现复现。日期A22/v1处理/公告联合同Apr24/currentnotice reader轻查复用。

实际Ch66人口cue段680–682、同题context factor与fairness slices只改变人口/语境，不承载conditional-code vs learnedpipeline输出形态的评价对象变化；Ch72保安全/执行权限，不把通用评价对象交给它。唯一owner PLATFORM-EVALUATION-SYSTEM，拟cue构念两段后、原“固定题目内容与候选排列”前插两段；不法律指导、不签真实harm，未写无锁：

代码生成的偏差审计也要改变实际产物形态，而不只换提示中的人口词。给定同一任务与可用属性，分别要求显式条件判断和学习型预测 pipeline，再检查哪些字段真正进入决策路径，能暴露简单 if-statement 未覆盖的 feature-selection 风险；识别某字段被使用，与模型生成时不使用它又是两个任务。属性出现在代码中不等于进入预测，进入预测也不自动证明真实群体伤害、违法或必须删除，任务的允许用途仍需独立定义。<!-- source-family:SF-2026-ARXIV-2604-21716 -->

[必要生成与抽取对照](https://arxiv.org/html/2604.21716v1)只量声明属性的使用人口，没有对所有代码执行、训练并测群体结果；抽样人审校准的 extractor 也不能认证全语料或 proxy 属性已被找全。原文总体比例口径不一致，故保留分项定性差额而不拼一个统一倍率。生成、代码解析/人审、可运行性检查及必要的下游效应测试均计费；不同代码形态、长度或 scorer 资格失配时，保留逐产物原始结果与固定任务约束，回退独立代码/数据审计，不用低关键词命中或较高使用识别率签发公平。

## A23 非作者最新准入与21284门事实校准（actual）

root actual有限独立核A15所列Apr7Issue29§2–4、Apr9maintainerreply原日期/承认项、pinned3919f135代码71–80/189–203/220–225，以及exactpaper§4/7–8/AppA/B/D必要相关文本，认可21284核心纠错早已公开、新增架构归纳/星级框架尚未额外支持verbatim胜extraction设计增量；具名贡献前关闭，不评分、不自动同族、不搬归属。不是因无benchmark/Books覆盖或审阅工作量，已足门事实即停。

reader supp_apr25_review_fresh实际A16除三个G和21282之外25完整题摘/currentabs轻查，均无具名notice；21360/21668/21916 exact-v1完整AB与当前窄增量一致，版本本身不自动触发。原13P中11准入仅潜力层：21144/21152/21360/21363/21444/21668/21716/21901/21916/21921/21931；其余12原EX/reuse维持。21344最小actualv1§3.1–3.2/RQ3：human519问/237图对MLM2175问/531图，难度/问型人口不同，27.4%总体差未分离author/evaluator效应，实际额外是multichart题库/标注/VDSP组合，未给新可迁移评价条件，改EX。21748最小actualv1§3.1–3.2：LLM分factual/relational句，共timestamp合event，bufferembeddingseed→同timestamp全event→LLMsynthesis；无新资格/失效或独立反证；旧screening328已有同v1具体EX，理由未变复用，不因memory owner存在拒绝。未把两项最小门读写全Source完成。

互斥必要Source：作者21152/21716/21363/21444/21931；reader21144/21360/21668/21901/21916，21921复用旧有效层并只核firstpublic差额。三个G/21282仅A17作者门读，尚非reader校准通过。无全日计数预支。

## A24 21152 exact-v1必要Source与具体已有覆盖（待独立Source/Books决定）

2+1+2=5；actual [v1](https://arxiv.org/html/2604.21152v1) §3/T1、§4/§4.1、§5.1–5.4、§6.1及A.2.1–2.3/T2–4。必要采用仅cue-conditioned output与拒绝/质量人口分责，**不采用中心“dialectjailbreak/词汇安全gate”因果结论**：T1六conditions是explicitbio+StandardEnglish与implicitdialect/无bio比较，不是所有profile×dialect独立交叉；gender/occupation只在explicit模板出现、wording/社会语用也改变，定性常识推断/GLMM prompt随机截距不消这些混杂。只text，不因VL模型名认视觉研究。BOLD清理2219prompt，但Gemma refusal实用2201/condition/13206；BERT/Regard N24669且排refusal，保survivor分母。BERTmaxoverreferences是Wikipedia相似，不是事实性、安全正确；Regard_model-Regard_source是代理负面程度，不认证真实伤害。Qwen3-VL8B零拒答所以refusal GLMM只Gemma3-12B，不把差异唯一归alignmentregimen。

A.2审核504按model/predictedrefusal/topic分层，两个reviewer TP168、FP0、FN3/2、TN333/334，sampleprecision1/recall.982/.988；该抽样不证明全域校准。原38hard/1705soft是tasknoncompliance，soft是固定一句completion约束下的澄清/回避，**不是1705次安全policyblock**；将mixedrefusal706prompts筛后检验也不认证机制因果。§6.1明确syntheticdialect/native不足、benigntopics未测真正恶意请求、one-shot非多轮；hardware/precision/sampling/repeats未充分披露，不补造。未核代码/复现。日期A22保v1Updated Apr24 00:13:04Z/created01:50:41Z与官方公告/身份联合，不追秒；当前abs无具名notice由reader A16 actual轻查复用。

具体Books NC提议：actual Ch66 cue构念段（现680–682，source2601-18486）已要求名字/方言/历史/显式类别不互换、保存cue identity/条件响应且不称内在偏差，次段明示无真值不证明真实伤害/因果、独立标签/Unknown；actual 262–264 source2603-18280已分内部线索/输出控制、全部请求硬拒答/无效/错误vs非拒答事实/回避/framing与条件分母，自动judge非risktruth。拟采用的长期知识均已有实际正文，论文有限cue新验证仍值得报告，不为造diff再写；NC不是否认准入。若要引中心safety机制须取得独立profile×dialect控制、恶意请求标签与guard资格，否则该中心主张保持隔离。

## A22 最后有限16潜力身份日期原始投影（未代准入/Source）

原04-24/26/27正式候选表定点sameID无命中；各原screening不是正式采用。以下actual arXiv publisher DataCite原字段按v1投影，Submitted不作公开日；均还须已有官方月列表身份/公告规则与版本处理合证。21344 Updated后处理到Jul28必须保异常；21921早项目线索仍隔离，不由created强行firstpub。未用当前v2/v3摘要倒填exactv1。

- [2604.21101](https://api.datacite.org/dois/10.48550/arXiv.2604.21101) `{"id":"21101","created":"2026-04-24T01:49:28.000Z","registered":"2026-04-24T01:49:29.000Z","v":"2","dates":[{"date":"2026-04-22T21:39:54Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:10:14Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21144](https://api.datacite.org/dois/10.48550/arXiv.2604.21144) `{"id":"21144","created":"2026-04-24T01:50:30.000Z","registered":"2026-04-24T01:50:31.000Z","v":"1","dates":[{"date":"2026-04-22T23:15:42Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:12:45Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21152](https://api.datacite.org/dois/10.48550/arXiv.2604.21152) `{"id":"21152","created":"2026-04-24T01:50:41.000Z","registered":"2026-04-24T01:50:42.000Z","v":"1","dates":[{"date":"2026-04-22T23:33:18Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:13:04Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21344](https://api.datacite.org/dois/10.48550/arXiv.2604.21344) `{"id":"21344","created":"2026-04-24T01:55:12.000Z","registered":"2026-04-24T01:55:13.000Z","v":"1","dates":[{"date":"2026-04-23T06:59:56Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-07-28T00:52:35Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21360](https://api.datacite.org/dois/10.48550/arXiv.2604.21360) `{"id":"21360","created":"2026-04-24T01:55:35.000Z","registered":"2026-04-24T01:55:36.000Z","v":"2","dates":[{"date":"2026-04-23T07:20:56Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:29:35Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21363](https://api.datacite.org/dois/10.48550/arXiv.2604.21363) `{"id":"21363","created":"2026-04-24T01:55:39.000Z","registered":"2026-04-24T01:55:40.000Z","v":"2","dates":[{"date":"2026-04-23T07:27:00Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:29:55Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21444](https://api.datacite.org/dois/10.48550/arXiv.2604.21444) `{"id":"21444","created":"2026-04-24T01:57:33.000Z","registered":"2026-04-24T01:57:33.000Z","v":"1","dates":[{"date":"2026-04-23T09:04:32Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:36:12Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21481](https://api.datacite.org/dois/10.48550/arXiv.2604.21481) `{"id":"21481","created":"2026-04-24T01:58:26.000Z","registered":"2026-04-24T01:58:26.000Z","v":"2","dates":[{"date":"2026-04-23T09:44:03Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:38:51Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21510](https://api.datacite.org/dois/10.48550/arXiv.2604.21510) `{"id":"21510","created":"2026-04-24T01:59:06.000Z","registered":"2026-04-24T01:59:07.000Z","v":"1","dates":[{"date":"2026-04-23T10:12:32Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:40:00Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21668](https://api.datacite.org/dois/10.48550/arXiv.2604.21668) `{"id":"21668","created":"2026-04-24T02:02:53.000Z","registered":"2026-04-24T02:02:53.000Z","v":"2","dates":[{"date":"2026-04-23T13:33:28Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:50:13Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21716](https://api.datacite.org/dois/10.48550/arXiv.2604.21716) `{"id":"21716","created":"2026-04-24T02:04:01.000Z","registered":"2026-04-24T02:04:02.000Z","v":"1","dates":[{"date":"2026-04-23T14:22:22Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:53:03Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21748](https://api.datacite.org/dois/10.48550/arXiv.2604.21748) `{"id":"21748","created":"2026-04-24T02:04:45.000Z","registered":"2026-04-24T02:04:46.000Z","v":"1","dates":[{"date":"2026-04-23T14:57:23Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T00:55:36Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21901](https://api.datacite.org/dois/10.48550/arXiv.2604.21901) `{"id":"21901","created":"2026-04-24T02:08:16.000Z","registered":"2026-04-24T02:08:17.000Z","v":"1","dates":[{"date":"2026-04-23T17:48:18Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T01:03:37Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21916](https://api.datacite.org/dois/10.48550/arXiv.2604.21916) `{"id":"21916","created":"2026-04-24T02:08:37.000Z","registered":"2026-04-24T02:08:37.000Z","v":"3","dates":[{"date":"2026-04-23T17:57:46Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T01:04:25Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21921](https://api.datacite.org/dois/10.48550/arXiv.2604.21921) `{"id":"21921","created":"2026-04-24T02:08:43.000Z","registered":"2026-04-24T02:08:44.000Z","v":"1","dates":[{"date":"2026-04-23T17:58:38Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T01:04:33Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`
- [2604.21931](https://api.datacite.org/dois/10.48550/arXiv.2604.21931) `{"id":"21931","created":"2026-04-24T02:08:57.000Z","registered":"2026-04-24T02:08:58.000Z","v":"1","dates":[{"date":"2026-04-23T17:59:57Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-04-24T01:04:48Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-04","dateType":"Available","dateInformation":"v1"}]}`

## A21 21191/21564真实保存与实际POST/root释放

21191按reader最小条件修订A13并获root字面/插点窄lease后，作者仅写Ch20 515/517与本人注652（原unstaged6+/0、cached6+/0保留，新增6+/0）。非writer supp_apr25_review_fresh实际读503–538完整两侧、648–656本人注及限定diff，确认逐字修订PRE/lattice/半环/theta独立控制流与费用/非futuremass边界，actualPOST通过；root接纳释放。作者仅行政同步自身note并actual rg读回。

21564 root actual Source/日期/Ch66 owner及逐字A14 PRE独核通过：exactv1 §3/4、§5.2–5.6/7与DataCite、officialmonth item1387/currentabs无notice；未遍历附录或核代码。root授PPT07749后两段＋本人注窄lease，作者仅写Ch66 672/674与note4988、实际顺读及diffcheck0。root非writer随后实际读666–684完整两侧与4984–4994本人注，逐字PRE一致、衔接准确，POST通过并释放；作者只行政同步本人注并actual rg读回。至此本日5项新真实整合，均不是DAY，当前无本轮Books窄锁。A16尚待准入校准/必要Source与最终清单，不预授普通0或完成。未stage/commit/push。

## A20 Daily14来源差额闭合与实际触发（发现停止，非候选审阅完成）

仅Daily14及本轮实际触发。机构旧记录复用的对象是具体可见列表/分页和邻界，不是旧完成标签；新自然日改变了DeepSeek与arXiv常规batch，其他具体目录邻界仍围住Apr24。当前未读到的新论文按A16/A17继续，不把已取得列表当Evidence完成。

|来源|实际本日依据/停止|Apr24补充结果与限制|
|---|---|---|
|SRC-OPENAI|原V3本地实际RSS1230项，Apr23T10/11Z在Apr24自然日前；jobs Apr25T00Z在后。Research/Publication历史缺段未修复|可见RSS无新落窗机制；官方历史Research清单仍终态外部缺口，不以RSS证明全机构零遗漏|
|SRC-ANTHROPIC|原actual Research publishedOn Apr22T14:12/14:27Z→Apr29T20:26Z|复用可见目录跨窗停点；未列作者稿不作全网覆盖|
|SRC-GOOGLE-AI|原GoogleResearch April9条Apr22→29；DeepMind原JSON-LD DiLoCo Apr23T16Z＝Apr24BJT00，当前请求SSL失败不抹原件|Apr24 DiLoCo与原04-24的2604.21428 same-core明确去重；实际读旧原85整行/必要Source定位267，已Ch36真实整合，不重评分/改归属。Publications历史缺段隔离|
|SRC-META-AI|原有效Research空提取、Blog Apr8/6→Mar27混排；本轮没有取得可复核历史列表|保受阻，不以空响应推Apr24零项；需官方本窗历史分页/原始清单|
|SRC-QWEN|原actual官方API40项Apr22T10+08→Apr28T10+08→Apr30T12+08；静态60旧项|可见目录跨Apr24，无新候选；不替所有作者稿|
|SRC-DEEPSEEK|本轮actual News Apr24与APIupdates Apr24核心，ReadPaper当下为June报告；updates重试timeout而先前成功文本有效|A18恢复Apr24日级release候选；不追旧9点钟时刻，不倒填June，机制证据隔离|
|SRC-MOONSHOT|原actual release100项1.38 Apr22T16:26:17Z→1.39 Apr24T06:22:19Z→1.40 Apr28T13:51:04Z|原Kimi1.39整行/深审/Ch84POST有效，同事件不新增。PlatformBlog历史段仍缺|
|SRC-TENCENT-HUNYUAN|原actual publicList page1/100/render0 total9、Apr30/23→Feb13|可见“全部”目录无Apr24日标签；不外推未列作者稿|
|SRC-ZAI|原actual Research15项Apr29→7→1、releaseNotesJun16→Apr7→Feb12|可见目录跨Apr24，日期本身按官方日级不补钟；未遍历commits|
|SRC-BYTEDANCE-SEED|原actual get_article_list_v2/US，paper type1 page20/count20 total242 next40，Apr25T16Z→Apr22T16Z；blog type2 page0/20 total95已到2025；本轮research页实际当前局部April26/22|Apr24目录无新列项；21921按arXiv触发旧Apr23目录/项目线索单族first-public另核，不能把目录PublishDate重定论文；来源没有扩大Science|
|SRC-BAIDU-ERNIE|原actual技术blog10条Apr30→15→Feb6→2025|可见目录跨Apr24，无新项；不等公司全研究|
|SRC-XIAOMI-MIMO|原actual Paper8 Jun29→Mar13→Feb3；Blog14缺发布日期|Paper跨窗有效，Blog历史日期仍受阻隔离|
|SRC-MINIMAX|原actual CLI release26，Apr17T20:51:17Z→Apr26T01:40:29Z；ENBlogMay26→Mar18、CN Apr27→Mar18|可见release/blog无Apr24新条；AgentTech最早可见May13，不认证四月历史段|
|SRC-ARXIV|A1四主题submitted发现范围仅Apr24常规批次线索；MODEL214首次截断后已分start0/50/100/150/200、max50补齐，AGENT77/MULTIMODAL67/SYSTEM36各max350返完整；官方April分类列表CL/LG/AI/DC/RO/AR/PL/OS/PF/IR/MA及CV第二页身份/title查漏|宽分类不成全文队列；title明确范围外关闭，相关/含糊读完整AB。候选日期按官方公告ID规则/月列表位置/v1处理publisher合证，Submitted不单证。A9原同事件去重；A16最后29+ A17门事实，发现冻结后只必要层，不再扩候选池|

实际表外触发：[MemPalace官方GitHub](https://github.com/MemPalace/mempalace)，因21284具名纠错实际取Issue29/8comments与pinnedv3.1.0 tree和目标blob，A15只用相关审计/维护者reply/代码行；其他评论的推广代码与新外部实验未采、未扩全repo。其余DataCite是arXiv出版状态补证，DeepSeek docs/release是机构同事件补证，不另计材料家族。辅助搜索未替代必要证据。

## A19 Ch23两窄位actualPOST已接纳/释放

非writer `supp_apr25_review_fresh`实际顺读Ch23 106–124（M2M→GPA2602-06205→新114/116→跨模态map17584/双线性）、188–205（OmniGCD→MOH→新196/198→SCR/hooks）、本人注2258/2260与前注、限定diff。四正文逐字A12；21836几何诊断非训练/真语义，21911缺席代理/输出事件与正识别反侧、全费/回退齐，实际diffcheck exit0。写前unstaged16+/0保持，新12+/0后合28+/0、cached74+/0不动；既有20329/18573/20392非本日成果。root已接纳真实POST并释放两窄lease，不第三次Source/正文复核。作者只将两本人注同步真实POST/释放并实际rg读回、限定check，当前3项新真实整合（含Ch5），不授DAY；未stage/commit/push。

## A17 三门事实最小读取与安全/费用EX信号（待独立校准）

- **21101 G→P提议**：[exactv1](https://arxiv.org/html/2604.21101v1) actual Introduction/§4 Methods Eq1–6/Theorem2–4/Remark1。不是仅将已有transformer用于fusion：autonomous nonlinear second-order dynamics u''=N(u,u';theta)，piecewiseconstant u/linear J=du/dt、Lagrangemortar跨rollout初值与SBP scaffold是新架构；Hamiltonian N=V'(u)及dissipative elliptic形式能量保证各有条件。Theorem4要求discreteinf-sup、输入state偏导有界，给 Ch^-3/2 Rmax(exp(cT/M)-1)，N-independent不直接等于所有物理时间T无界。其数学对象是neural time integration，不是任意token transformer；但若成立会改变AR latent dynamics的结构先验与稳定训练选择，故不能因科学实验人口硬排潜在一般机制。仅门读到这里，不授稳定claim，若独核判纯Science则按具体对象关闭。
- **21510 G→P提议**：[exactv1](https://arxiv.org/html/2604.21510v1) actual §4.3/§5.1–5.2/T4：DVA先problem+initialmodel提missingrequirements，再让blind code-to-math分支只看code不见problem，最后合problem/逆向model/requirements判discrepancy，非空才repair。这提供输入信息隔离的语义audit接口，超出增加1000优化题/角色命名；需重新考虑“重读自己代码”与盲回译比较的确认偏差。论文声称“确保真实执行”并不成立，后续必要层要核proxy资格/三阶段消融与预算；T4比无框架baseline慢约4–5倍，不能照“无明显开销”。先准入，证据不足保留而非关EX。
- **21481 G→P提议**：[exactv1](https://arxiv.org/html/2604.21481v1) actual §3.1–3.4/§4.2–4.4/Fig5。不是仅BT/SHAP排行榜：锁住holisticchoice后才问六维，明确rater-vs-sentence两个采样轴，发现增加rater主要稳定rank、增加sentence主要缩BT不确定性；重考只扩大同人口judgments是否足够。目标是相对fullleaderboard的Spearman与bootstrapCI，不认证真实语音质量；100–200rater依5/7systems而不同，不授通用quota。SHAP预测非知觉因果；语言支持/默认voice并不统一，必要Source将据具体采用命题读足，不按TTS应用排除。
- **21282 EX-signal必要关闭读取**：[exactv1](https://arxiv.org/html/2604.21282v1) actual Algorithm1/§4.1–4.5/T1–3/§5.1–5.3/5.7：三角色DeepSeekV3 temp.1并行+Qwen3-8B RTX3090 verifier可override，否则majority；并未给独立game机制/验证资格。Juliet synthetic baselineflow01、132vulnerable130patched/14CWEs；FPR并行无V .915、+V .600、single .815，single与full均recall1；CWEhierarchy等价/regex与50outputspotcheck不认证开放代码安全。T2 API费 .0021不变但21.7s→68.1s（local约50s），GPUamortized被记0不能叫全成本free；serial+V92.2s不使full3xE2E。局部过滤41falsepositives是已有postreview的该人口操作点，不给独立新可靠性或成本条件；不采用“不同模型家族确保独立”和alwaysrational。EX理由是新game命名与有限操作点未改变主线设计判断，而非无benchmark；具名安全/费用信号已actual读，待非作者校准。

## A18 DeepSeek Apr24自然日恢复：有限release事实候选

实际完整读[Apr24官方核心说明](https://deepseek.com/en/news/v4-preview/)（News April24,2026）和[API updates Apr24段](https://api-docs.deepseek.com/updates/)先前成功文本；本次web另试updates timeout不抹掉已有效原文。日级公开日期明确，旧09:00相交隔离只对原小时窗成立，新增自然日可恢复；不改原§4。ReadPaper当前指June技术稿，不能倒填April方法。官方当次披露token-wisecompression+DSA、1Mdefault、Pro1.6Ttotal49Bactive/Flash284B13Bactive，但无当次压缩状态/掩码/质量成本受控机制，所以只采用release/API兼容事实，不采SOTA、效率倍率或未公开实现。

原有调用身份→保base_url但model可显式换deepseek-v4-pro/flash、ChatCompletions与Anthropic接口；旧deepseek-chat/reasoner当期转Flash nonthinking/thinking并预告July24退役→调用方必须区分alias路由与固定model/mode，不能把同名API当同模型。**1+2+1=4**：新增是跨调用兼容的版本事实而非长期新机制，已关闭/仅报告；评分不借已有通用versioning原则或Books所能联想的owner加分。尚待非作者有限事实/贡献/评分校准，不进Books。未测API、权重、性能、上下文上限或服务SLO。机制披露不足不是所有论文D，只对这次April机制采用隔离；后续June独立事件按真实归属，不在本日深审。

## A16 最后一批有限主题题摘筛选（29身份，门事实G待最小读；非全文队列）

沿A1四主题和官方分类title线索定点所得；29份完整题摘实际已读，current版本只供发现，P后续必须exact-v1。尚未结束必要日期，不把P写确定当窗新增。EX不因关键词、小模型、成熟主题或数量关闭；已有同ID有效EX仅定点复用。以下完整题摘为实际决策依据，所有缓存未由本表自动入池：

### 21101 G — A Hybridizable Neural Time Integrator for Stable Autoregressive Forecasting

For autoregressive modeling of chaotic dynamical systems over long time horizons, the stability of both training and inference is a major challenge in building scientific foundation models. We present a hybrid technique in which an autoregressive transformer is embedded within a novel shooting-based mixed finite element scheme, exposing topological structure that enables provable stability. For forward problems, we prove preservation of discrete energies, while for training we prove uniform bounds on gradients, provably avoiding the exploding gradient problem. Combined with a vision transformer, this yields latent tokens admitting structure-preserving dynamics. We outperform modern foundation models with a $65\times$ reduction in model parameters and long-horizon forecasting of chaotic systems. A "mini-foundation" model of a fusion component shows that 12 simulations suffice to train a real-time surrogate, achieving a $9{,}000\times$ speedup over particle-in-cell simulation.

裁决：主旨为scientific foundation chaotic systems，但shooting-mixedfiniteelement提出AR推理能量/训练gradient uniform界，可能是主线一般优化原语而非领域用已有AI；门事实需最小读定理适用对象，不能仅Science词硬排。

### 21133 EX — GRISP: Guided Recurrent IRI Selection over SPARQL Skeletons

We present GRISP (Guided Recurrent IRI Selection over SPARQL Skeletons), a novel SPARQL-based question-answering method over knowledge graphs using a fine-tuned small language model (SLM). Given a natural-language question, the method uses the SLM to generate a natural-language SPARQL query skeleton, and then resolves the natural-language placeholders using a backtracking search that retrieves and re-ranks knowledge graph items under knowledge graph constraints. The SLM is jointly trained on skeleton generation and re-ranking data generated from question-query pairs. We evaluate the method on common Wikidata and Freebase benchmarks, and achieve better results than other state-of-the-art fine-tuning-based methods.

裁决：SPARQL skeleton+KG constrained backtracking/re-rank联合训练与任务成绩，未给新的执行/验证真值、失败或检索有效性条件；不因SLM排除。

### 21144 P — Using Machine Mental Imagery for Representing Common Ground in Situated Dialogue

Situated dialogue requires speakers to maintain a reliable representation of shared context rather than reasoning only over isolated utterances. Current conversational agents often struggle with this requirement, especially when the common ground must be preserved beyond the immediate context window. In such settings, fine-grained distinctions are frequently compressed into purely textual representations, leading to a critical failure mode we call \emph{representational blur}, in which similar but distinct entities collapse into interchangeable descriptions. This semantic flattening creates an illusion of grounding, where agents appear locally coherent but fail to track shared context persistently over time. Inspired by the role of mental imagery in human reasoning, and based on the increased availability of multimodal models, we explore whether conversational agents can be given an analogous ability to construct some depictive intermediate representations during dialogue to address these limitations. Thus, we introduce an active visual scaffolding framework that incrementally converts dialogue state into a persistent visual history that can later be retrieved for grounded response generation. Evaluation on the IndiRef benchmark shows that incremental externalization itself improves over full-dialog reasoning, while visual scaffolding provides additional gains by reducing representational blur and enforcing concrete scene commitments. At the same time, textual representations remain advantageous for non-depictable information, and a hybrid multimodal setting yields the best overall performance. Together, these findings suggest that conversational agents benefit from an explicitly multimodal representation of common ground that integrates depictive and propositional information.

裁决：纯text压缩不同实体模糊→持续visualstate与text/hybrid反侧→重审可描绘与命题信息的表示选择，不把视觉图当事实grounding。

### 21152 P — Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles

As state-of-the-art Large Language Models (LLMs) have become ubiquitous, ensuring equitable performance across diverse demographics is critical. However, it remains unclear whether these disparities arise from the explicitly stated identity itself or from the way identity is signaled. In real-world interactions, users' identity is often conveyed implicitly through a complex combination of various socio-linguistic factors. This study disentangles these signals by employing a factorial design with over 24,000 responses from two open-weight LLMs (Gemma-3-12B and Qwen-3-VL-8B), comparing prompts with explicitly announced user profiles against implicit dialect signals (e.g., AAVE, Singlish) across various sensitive domains. Our results uncover a unique paradox in LLM safety where users achieve ``better'' performance by sounding like a demographic than by stating they belong to it. Explicit identity prompts activate aggressive safety filters, increasing refusal rates and reducing semantic similarity compared to our reference text for Black users. In contrast, implicit dialect cues trigger a powerful ``dialect jailbreak,'' reducing refusal probability to near zero while simultaneously achieving a greater level of semantic similarity to the reference texts compared to Standard American English prompts. However, this ``dialect jailbreak'' introduces a critical safety trade-off regarding content sanitization. We find that current safety alignment techniques are brittle and over-indexed on explicit keywords, creating a bifurcated user experience where ``standard'' users receive cautious, sanitized information while dialect speakers navigate a less sanitized, more raw, and potentially a more hostile information landscape and highlights a fundamental tension in alignment--between equitable and linguistic diversity--and underscores the need for safety mechanisms that generalize beyond explicit cues.

裁决：显式profile与implicitdialect不应当同身份等价→factorial响应/拒绝与sanitization分开→重审语言/人口cue定义与安全指标，不先认定jailbreak成立。

### 21199 EX-reuse — ARFBench: Benchmarking Time Series Question Answering Ability for Software Incident Response

Time series question-answering (TSQA), in which we ask natural language questions to infer and reason about properties of time series, is a promising yet underexplored capability of foundation models. In this work, we present ARFBench, a TSQA benchmark that evaluates the understanding of multimodal foundation models (FMs) on time series anomalies prevalent in software incident data. ARFBench consists of 750 questions across 142 time series and 5.38M data points from 63 production incidents sourced exclusively from internal telemetry at Datadog. We evaluate leading proprietary and open-source LLMs, VLMs, and time series FMs and observe that frontier VLMs perform markedly better than existing baselines; the leading model (GPT-5) achieves a 62.7% accuracy and 51.9% F1. We next demonstrate the promise of specialized multimodal approaches. We develop a novel TSFM + VLM hybrid prototype which we post-train on a small set of synthetic and real data that yields comparable overall F1 and accuracy with frontier models. Lastly, we find models and human domain experts exhibit complementary strengths. We define a model-expert oracle, a best-of-2 oracle selector over model and expert answers, yielding 82.8% F1 and 87.2% accuracy and establishing a new superhuman frontier for future TSQA models. The benchmark is available at https://huggingface.co/datasets/Datadog/ARFBench.

裁决：旧screen51/rootnegative有效：生产telemetry任务与expert/modelbestof2 oracle没新可实现selector/可靠性，oracle不是系统。

### 21223 EX-reuse — Zero-Shot Detection of LLM-Generated Text via Implicit Reward Model

Large language models (LLMs) have demonstrated remarkable capabilities across various tasks. However, their ability to generate human-like text has raised concerns about potential misuse. This underscores the need for reliable and effective methods to detect LLM-generated text. In this paper, we propose IRM, a novel zero-shot approach that leverages Implicit Reward Models for LLM-generated text detection. Such implicit reward models can be derived from publicly available instruction-tuned and base models. Previous reward-based method relies on preference construction and task-specific fine-tuning. In comparison, IRM requires neither preference collection nor additional training. We evaluate IRM on the DetectRL benchmark and demonstrate that IRM can achieve superior detection performance, outperforms existing zero-shot and supervised methods in LLM-generated text detection.

裁决：旧screen240有效：base/instruct implicitreward ratio换检测统计量的操作点未新calibration/identity条件，非因检测任务一刀切。

### 21282 EX-signal — Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection

Automated code vulnerability detection is critical for software security, yet existing approaches face a fundamental trade-off between detection accuracy and computational cost. We propose a heterogeneous multi-agent architecture inspired by game-theoretic principles, combining cloud-based LLM experts with a local lightweight verifier. Our "3+1" architecture deploys three cloud-based expert agents (DeepSeek-V3) that analyze code from complementary perspectives - code structure, security patterns, and debugging logic - in parallel, while a local verifier (Qwen3-8B) performs adversarial validation at zero marginal cost. We formalize this design through a two-layer game framework: (1) a cooperative game among experts capturing super-additive value from diverse perspectives, and (2) an adversarial verification game modeling quality assurance incentives. Experiments on 262 real samples from the NIST Juliet Test Suite across 14 CWE types, with balanced vulnerable and benign classes, demonstrate that our approach achieves a 77.2% F1 score with 62.9% precision and 100% recall at $0.002 per sample - outperforming both a single-expert LLM baseline (F1 71.4%) and Cppcheck static analysis (MCC 0). The adversarial verifier significantly improves precision (+10.3 percentage points, p &lt; 1e-6, McNemar's test) by filtering false positives, while parallel execution achieves a 3.0x speedup. Our work demonstrates that game-theoretic design principles can guide effective heterogeneous multi-agent architectures for cost-sensitive software engineering tasks.

裁决：三云expert+localverifier与二层game称谓仍是既有并行分析/后置复核；题摘无新协同/验证可靠性机制。zero marginalcost/100%recall和3x有成本/安全反证信号，须最小读被用表/预算，保具名审阅不因无候选取消。

### 21334 EX — Ideological Bias in LLMs' Economic Causal Reasoning

Do large language models (LLMs) exhibit systematic ideological bias when reasoning about economic causal effects? As LLMs are increasingly used in policy analysis and economic reporting, where directionally correct causal judgments are essential, this question has direct practical stakes. We present a systematic evaluation by extending the EconCausal benchmark with ideology-contested cases - instances where intervention-oriented (pro-government) and market-oriented (pro-market) perspectives predict divergent causal signs. From 10,490 causal triplets (treatment-outcome pairs with empirically verified effect directions) derived from top-tier economics and finance journals, we identify 1,056 ideology-contested instances and evaluate 20 state-of-the-art LLMs on their ability to predict empirically supported causal directions. We find that ideology-contested items are consistently harder than non-contested ones, and that across 17 of 20 models, accuracy is systematically higher when the empirically verified causal sign aligns with intervention-oriented expectations than with market-oriented ones. Moreover, when models err, their incorrect predictions disproportionately lean intervention-oriented, and this directional skew is not eliminated by one-shot in-context prompting. These results highlight that LLMs are not only less accurate on ideologically contested economic questions, but systematically less reliable in one ideological direction than the other, underscoring the need for direction-aware evaluation in high-stakes economic and policy settings.

裁决：1056经济争议因果题及方向bias评估局部领域人口，没有新的通用bias识别机制/控制条件；不采政策结论。

### 21344 P — Beyond Single Plots: A Benchmark for Question Answering on Multi-Charts

Charts are widely used to present complex information. Deriving meaningful insights in real-world contexts often requires interpreting multiple related charts together. Research on understanding multi-chart images has not been extensively explored. We introduce PolyChartQA, a mid-scale dataset specifically designed for question answering over multi-chart images. PolyChartQA comprises 534 multi-chart images (with a total of 2,297 sub-charts) sourced from peer-reviewed computer science research publications and 2,694 QA pairs. We evaluate the performance of nine state-of-the-art Multimodal Language Models (MLMs) on PolyChartQA across question type, difficulty, question source, and key structural characteristics of multi-charts. Our results show a 27.4% LLM-based accuracy (L-Accuracy) drop on human-authored questions compared to MLM-generated questions, and a 5.39% L-accuracy gain with our proposed prompting method.

裁决：统一multichart题的模型/人写来源人口显示显著accuracy差→检查question-author/evaluator同源是否掩盖输入理解，潜在评价盲区而非图表题数量。

### 21360 P — Prototype-Based Test-Time Adaptation of Vision-Language Models

Test-time adaptation (TTA) has emerged as a promising paradigm for vision-language models (VLMs) to bridge the distribution gap between pre-training and test data. Recent works have focused on backpropagation-free TTA methods that rely on cache-based designs, but these introduce two key limitations. First, inference latency increases as the cache grows with the number of classes, leading to inefficiencies in large-scale settings. Second, suboptimal performance occurs when the cache contains insufficient or incorrect samples. In this paper, we present Prototype-Based Test-Time Adaptation (PTA), an efficient and effective TTA paradigm that uses a set of class-specific knowledge prototypes to accumulate knowledge from test samples. Particularly, knowledge prototypes are adaptively weighted based on the zero-shot class confidence of each test sample, incorporating the sample's visual features into the corresponding class-specific prototype. It is worth highlighting that the knowledge from past test samples is integrated and utilized solely in the prototypes, eliminating the overhead of cache population and retrieval that hinders the efficiency of existing TTA methods. This endows PTA with extremely high efficiency while achieving state-of-the-art performance on 15 image recognition benchmarks and 4 robust point cloud analysis benchmarks. For example, PTA improves CLIP's accuracy from 65.64% to 69.38% on 10 cross-domain benchmarks, while retaining 92% of CLIP's inference speed on large-scale ImageNet-1K. In contrast, the cache-based TDA achieves a lower accuracy of 67.97% and operates at only 50% of CLIP's inference speed.

裁决：逐test sample cache增长/错样本→class-confidence加权知识prototype累计且取消实例检索→重新比较适配状态大小/噪声与类别规模成本边界。currentv2仅发现，必要层必须v1。

### 21363 P — A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration

Bridging the gap between embodied intelligence and embedded deployment remains a key challenge in intelligent robotic systems, where perception, reasoning, and planning must operate under strict constraints on computation, memory, energy, and real-time execution. In vision-and-language navigation (VLN), existing approaches often face a trade-off between reasoning capability and deployment efficiency on real-world platforms. In this paper, we present a deployable embodied VLN system that achieves both high efficiency and strong high-level reasoning on real-world robots. The system is decomposed into a fast perception-action layer and a deep reasoning layer running asynchronously at different time scales, with a shared memory layer enabling efficient interaction between them. To support long-horizon reasoning, we incrementally construct a compact memory graph and progressively feed decomposed subgraphs into a vision-language model (VLM). Furthermore, we formulate exploration as a Weighted Traveling Repairman Problem (WTRP) by jointly considering reasoning outcomes and the spatial distribution of candidate regions. Extensive experiments in simulation and real-world environments demonstrate improved navigation success and efficiency over existing VLN approaches while maintaining real-time performance on resource-constrained hardware. Code and additional real-world experiments are available at https://github.com/xukuanHIT/HiCo-Nav.

裁决：real-time端侧perception/action与慢推理竞争→async双timescale共享graph状态和subgraph分批、WTRP探索→重审状态时效/调度与探索成本，不先授实时安全。

### 21380 EX — Conjecture and Inquiry: Quantifying Software Performance Requirements via Interactive Retrieval-Augmented Preference Elicitation

Since software performance requirements are documented in natural language, quantifying them into mathematical forms is essential for software engineering. Yet, the vagueness in performance requirements and uncertainty of human cognition have caused highly uncertain ambiguity in the interpretations, rendering their automated quantification an unaddressed and challenging problem. In this paper, we formalize the problem and propose IRAP, an approach that quantifies performance requirements into mathematical functions via interactive retrieval-augmented preference elicitation. IRAP differs from the others in that it explicitly derives from problem-specific knowledge to retrieve and reason the preferences, which also guides the progressive interaction with stakeholders, while reducing the cognitive overhead. Experiment results against 10 state-of-the-art methods on four real-world datasets demonstrate the superiority of IRAP on all cases with up to 40x improvements under as few as five rounds of interactions.

裁决：交互RAG elicitation将软件性能需求转数学偏好函数，题摘只有领域problemknowledge与轮次/成绩点，未给新Agent执行或可比优化条件。

### 21444 P — HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration

Long-form video understanding remains fundamentally challenged by pervasive spatiotemporal redundancy and intricate narrative dependencies that span extended temporal horizons. While recent structured representations compress visual information effectively, they frequently sacrifice temporal coherence, which is critical for causal reasoning. Meanwhile, existing multi-agent frameworks operate through rigid, pre-defined workflows that fail to adapt their reasoning strategies to question-specific demands. In this paper, we introduce HiCrew, a hierarchical multi-agent framework that addresses these limitations through three core contributions. First, we propose a Hybrid Tree structure that leverages shot boundary detection to preserve temporal topology while performing relevance-guided hierarchical clustering within semantically coherent segments. Second, we develop a Question-Aware Captioning mechanism that synthesizes intent-driven visual prompts to generate precision-oriented semantic descriptions. Third, we integrate a Planning Layer that dynamically orchestrates agent collaboration by adaptively selecting roles and execution paths based on question complexity. Extensive experiments on EgoSchema and NExT-QA validate the effectiveness of our approach, demonstrating strong performance across diverse question types with particularly pronounced gains in temporal and causal reasoning tasks that benefit from our hierarchical structure-preserving design.

裁决：无序/固定流程压缩丢时间拓扑→shotboundary+segment内层次tree与question-conditioned访问→检验结构保留的因果/时间推理条件，不按multiagent组合自动排除或确认。

### 21481 G — Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages

Crowdsourced pairwise evaluation has emerged as a scalable approach for assessing foundation models. However, applying it to Text to Speech(TTS) introduces high variance due to linguistic diversity and multidimensional nature of speech perception. We present a controlled multidimensional pairwise evaluation framework for multilingual TTS that combines linguistic control with perceptually grounded annotation. Using 5K+ native and code-mixed sentences across 10 Indic languages, we evaluate 7 state-of-the-art TTS systems and collect over 120K pairwise comparisons from over 1900 native raters. In addition to overall preference, raters provide judgments across 6 perceptual dimensions: intelligibility, expressiveness, voice quality, liveliness, noise, and hallucinations. Using Bradley-Terry modeling, we construct a multilingual leaderboard, interpret human preference using SHAP analysis and analyze leaderboard reliability alongside model strengths and trade-offs across perceptual dimensions.

裁决：大规模pairwise/native raters/6维BT+SHAP本身不足；题摘称reliability却无具体新失效，需最小读population/维度冲突是否改变评价选择，不能按TTS词排除。

### 21510 G — OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving

While Large Language Models (LLMs) demonstrate remarkable reasoning, complex optimization tasks remain challenging, requiring domain knowledge and robust implementation. However, existing benchmarks focus narrowly on Mathematical Programming and Combinatorial Optimization, hindering comprehensive evaluation. To address this, we introduce OptiVerse, a comprehensive benchmark of 1,000 curated problems spanning neglected domains, including Stochastic Optimization, Dynamic Optimization, Game Optimization, and Optimal Control, across three difficulty levels: Easy, Medium, and Hard. The experiments with 22 LLMs of different sizes reveal sharp performance degradation on hard problems, where even advanced models like GPT-5.2 and Gemini-3 struggle to exceed 27% accuracy. Through error analysis, we identify that modeling &amp; logic errors remain the primary bottleneck. Consequently, we propose a Dual-View Auditor Agent that improves the accuracy of the LLM modeling process without introducing significant time overhead. OptiVerse will serve as a foundational platform for advancing LLMs in solving complex optimization challenges.

裁决：覆盖优化题/难题成绩本身不足；DualViewAuditor是否新增可核建模/执行失败定位机制不清，最小读该段即可决定，不先默认全文。

### 21592 EX-reuse — Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers

Recent breakthroughs in 3D generative modeling have yielded remarkable progress in static shape synthesis, yet high-fidelity dynamic 4D generation remains elusive, hindered by temporal artifacts and prohibitive computational demand. We present Sculpt4D, a native 4D generative framework that seamlessly integrates efficient temporal modeling into a pretrained 3D Diffusion Transformer (Hunyuan3D 2.1), thereby mitigating the scarcity of 4D training data. At its core lies a Block Sparse Attention mechanism that preserves object identity by anchoring to the initial frame while capturing rich motion dynamics via a time-decaying sparse mask. This design faithfully models complex spatiotemporal dependencies with high fidelity, while sidestepping the quadratic overhead of full attention and reducing network total computation by 56%. Consequently, Sculpt4D establishes a new state-of-the-art in temporally coherent 4D synthesis and charts a path toward efficient and scalable 4D generation.

裁决：旧current-top14与必要evidence有效：firstframeanchor+timedecay块稀疏组合的局部FLOPs/4D质量点未隔离新结构条件；不因4D不属主线。

### 21637 EX — Multilinguality at the Edge: Developing Language Models for the Global South

Where and how language models (LMs) are deployed determines who can benefit from them. However, there are several challenges that prevent effective deployment of LMs in non-English-speaking and hardware constrained communities in the Global South. We call this challenge the last mile: the intersection of multilinguality and edge deployment, where the goals are aligned but the technical requirements often compete. Studying these two fields together is both a need, as linguistically diverse communities often face the most severe infrastructure constraints, and an opportunity, as edge and multilingual NLP research remain largely siloed. To understand the state of the art and the challenges of combining the two areas, we survey 232 papers that tackle this problem across the language modelling pipeline, from data collection to development and deployment. We also discuss open questions and provide actionable recommendations for different stakeholders in the NLP ecosystem. Finally, we hope that this work contributes to the development of inclusive and equitable language technologies.

裁决：232篇survey梳理edge×multilingual lastmile及建议，未给新机制或修正主线设计判断的原始证据。

### 21668 P — Encoder-Free Human Motion Understanding via Structured Motion Descriptions

The world knowledge and reasoning capabilities of text-based large language models (LLMs) are advancing rapidly, yet current approaches to human motion understanding, including motion question answering and captioning, have not fully exploited these capabilities. Existing LLM-based methods typically learn motion-language alignment through dedicated encoders that project motion features into the LLM's embedding space, remaining constrained by cross-modal representation and alignment. Inspired by biomechanical analysis, where joint angles and body-part kinematics have long served as a precise descriptive language for human movement, we propose \textbf{Structured Motion Description (SMD)}, a rule-based, deterministic approach that converts joint position sequences into structured natural language descriptions of joint angles, body part movements, and global trajectory. By representing motion as text, SMD enables LLMs to apply their pretrained knowledge of body parts, spatial directions, and movement semantics directly to motion reasoning, without requiring learned encoders or alignment modules. We show that this approach goes beyond state-of-the-art results on both motion question answering (66.7\% on BABEL-QA, 90.1\% on HuMMan-QA) and motion captioning (R@1 of 0.584, CIDEr of 53.16 on HumanML3D), surpassing all prior methods. SMD additionally offers practical benefits: the same text input works across different LLMs with only lightweight LoRA adaptation (validated on 8 LLMs from 6 model families), and its human-readable representation enables interpretable attention analysis over motion descriptions. Code, data, and pretrained LoRA adapters are available at https://yaozhang182.github.io/motion-smd/.

裁决：motion encoder alignment依赖→确定规则joint-angle/body/trajectory文本转接LLM→可替代表示接口/语义损失与训练费用边界，currentv2须v1。

### 21716 P — From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation

Prior work evaluates code generation bias primarily through simple conditional statements, which represent only a narrow slice of real-world programming and reveal solely overt, explicitly encoded bias. We demonstrate that this approach dramatically underestimates bias in practice by examining a more realistic task: generating machine learning (ML) pipelines. Testing both code-specialized and general-instruction large language models, we find that generated pipelines exhibit significant bias during feature selection. Sensitive attributes appear in 87.7% of cases on average, despite models demonstrably excluding irrelevant features (e.g., including "race" while dropping "favorite color" for credit scoring). This bias is substantially more prevalent than that captured by conditional statements, where sensitive attributes appear in only 59.2% of cases. These findings are robust across prompt mitigation strategies, varying numbers of attributes, and different pipeline difficulty levels. Our results challenge simple conditionals as valid proxies for bias evaluation and suggest current benchmarks underestimate bias risk in practical deployments.

裁决：if-statement敏感属性代理→MLpipeline featureselection中同attribute的不同暴露率与无关特征控制→重审偏差评估任务代理；须区分使用属性与实际伤害。

### 21728 EX-reuse — Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection

Pretrained vision-language models such as CLIP exhibit strong zero-shot generalization but remain sensitive to distribution shifts. Test-time adaptation adapts models during inference without access to source data or target labels, offering a practical way to handle such shifts. However, existing methods typically assume that test samples come from a single, consistent domain, while in practice, test data often include samples from mixed domains with distinct characteristics. Consequently, their performance degrades under mixed-domain settings. To address this, we present Ramen, a framework for robust test-time adaptation through active sample selection. For each incoming test sample, Ramen retrieves a customized batch of relevant samples from previously seen data based on two criteria: domain consistency, which ensures that adaptation focuses on data from similar domains, and prediction balance, which mitigates adaptation bias caused by skewed predictions. To improve efficiency, Ramen employs an embedding-gradient cache that stores the embeddings and sample-level gradients of past test images. The stored embeddings are used to retrieve relevant samples, and the corresponding gradients are aggregated for model updates, eliminating the need for any additional forward or backward passes. Our theoretical analysis provides insight into why the proposed adaptation mechanism is effective under mixed-domain shifts. Experiments on multiple image corruption and domain-shift benchmarks demonstrate that Ramen achieves strong and consistent performance, offering robust and efficient adaptation in complex mixed-domain scenarios. Our code is available at https://github.com/baowenxuan/Ramen .

裁决：旧current top与reverse必要审阅有效：混域样本/gradientcache局部组合未新的样本资格或deployment条件，旧反侧不抹去；currentv2不自动重开。

### 21748 P — StructMem: Structured Memory for Long-Horizon Behavior in LLMs

Long-term conversational agents need memory systems that capture relationships between events, not merely isolated facts, to support temporal reasoning and multi-hop question answering. Current approaches face a fundamental trade-off: flat memory is efficient but fails to model relational structure, while graph-based memory enables structured reasoning at the cost of expensive and fragile construction. To address these issues, we propose \textbf{StructMem}, a structure-enriched hierarchical memory framework that preserves event-level bindings and induces cross-event connections. By temporally anchoring dual perspectives and performing periodic semantic consolidation, StructMem improves temporal reasoning and multi-hop performance on \texttt{LoCoMo}, while substantially reducing token usage, API calls, and runtime compared to prior memory systems, see https://github.com/zjunlp/LightMem .

裁决：flat fact易失eventbinding、graph昂贵→temporalanchor dualperspective与周期consolidation→核结构/更新状态的取舍，不先把所有hierarchicalmemory当成熟combo关掉。

### 21896 EX — Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models

This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.

裁决：四游戏类别把既有字典/求解/minimax/feedback策略装入编程平台，无新执行、环境真值或可靠性条件；不是所有游戏研究范围外。

### 21901 P — GiVA: Gradient-Informed Bases for Vector-Based Adaptation

As model sizes continue to grow, parameter-efficient fine-tuning has emerged as a powerful alternative to full fine-tuning. While LoRA is widely adopted among these methods, recent research has explored vector-based adaptation methods due to their extreme parameter efficiency. However, these methods typically require substantially higher ranks than LoRA to match its performance, leading to increased training costs. This work introduces GiVA, a gradient-based initialization strategy for vector-based adaptation. It achieves training times comparable to LoRA and maintains the extreme parameter efficiency of vector-based adaptation. We evaluate GiVA across diverse benchmarks, including natural language understanding, natural language generation, and image classification. Experiments show that our approach consistently outperforms or achieves performance competitive with existing vector-based adaptation methods and LoRA while reducing rank requirements by a factor of eight ($8\times$).

裁决：vectoradapter需高rank→gradient-informedbasis初始化→rank/训练预算新的取舍，不能因已有LoRAowner拒绝。

### 21905 EX-reuse — Low-Rank Adaptation Redux for Large Models

Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.

裁决：旧screen362有效：LoRA的SP/SVD/gauge/lifecycle综述未新原始条件或对照；不因overview标签硬排。

### 21916 P — MathDuels: A Self-Play Benchmark That Grows

As frontier language models attain near-ceiling performance on static mathematical benchmarks, existing evaluations are increasingly unable to differentiate model capabilities, largely because they cast models solely as solvers of fixed problem sets. We introduce MathDuels, a self-play benchmark in which models occupy dual roles: each authors math problems under adversarial prompting and solves problems authored by every other participant. Problems are produced through a three-stage generation pipeline (meta-prompting, problem generation, and difficulty amplification), and validated by an independent verifier that excludes ill-posed questions. A Rasch model (Rasch, 1993) jointly estimates solver abilities and problem difficulties; author quality is derived from the difficulties of each model's authored problems. Experiments across 19 frontier models reveal that authoring and solving capabilities are partially decoupled, and that dual-role evaluation reveals capability separations invisible in single-role benchmarks. As newer models enter the arena, they produce problems that defeat previously dominant solvers, so the benchmark's difficulty co-evolves with participant strength rather than saturating at a fixed ceiling. We host a public leaderboard that updates as new models are released.

裁决：solver固定题池饱和→同批author/solver双角色与Rasch分开题难/能力→重新考虑题池共演与author quality、独立verifier资格。发现v3须v1题摘/必要层。

### 21921 P-date — Context Unrolling in Omni Models

We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.

裁决：多模态统一模型的contextunrolling潜在新跨模态中间表示路径；旧04-24已有必要Source但资格未定，需复用samev1有限命题与早SeedApr23官方核心的first-public差额，不搬候选。

### 21928 EX-reuse — Evaluation of Automatic Speech Recognition Using Generative Large Language Models

Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.

裁决：旧screening373有效：HATS上judge选优92–94%vsWER63是特定评价操作点，未给新scorer真值/失效或通用可比资格；currentv3本身不触发。

### 21931 P — Seeing Fast and Slow: Learning the Flow of Time in Videos

How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.

裁决：播放速度与真实事件时间混淆→selfsup AV/temporal速度识别、慢动作curation/conditionedgeneration→重新验速度标签/采样与时间可控生成边界。

### 21952 EX — Focus Session: Hardware and Software Techniques for Accelerating Multimodal Foundation Models

This work presents a multi-layered methodology for efficiently accelerating multimodal foundation models (MFMs). It combines hardware and software co-design of transformer blocks with an optimization pipeline that reduces computational and memory requirements. During model development, it employs performance enhancements through fine-tuning for domain-specific adaptation. Our methodology further incorporates hardware and software techniques for optimizing MFMs. Specifically, it employs MFM compression using hierarchy-aware mixed-precision quantization and structural pruning for transformer blocks and MLP channels. It also optimizes operations through speculative decoding, model cascading that routes queries through a small-to-large cascade and uses lightweight self-tests to determine when to escalate to larger models, as well as co-optimization of sequence length, visual resolution &amp; stride, and graph-level operator fusion. To efficiently execute the model, the processing dataflow is optimized based on the underlying hardware architecture together with memory-efficient attention to meet on-chip bandwidth and latency budgets. To support this, a specialized hardware accelerator for the transformer workloads is employed, which can be developed through expert design or an LLM-aided design approach. We demonstrate the effectiveness of the proposed methodology on medical-MFMs and on code generation tasks, and conclude with extensions toward energy-efficient spiking-MFMs.

裁决：硬软件co-design罗列量化/剪枝/speculation/cascade及算子融合，题摘无新独立机制、归因或可行性边界；非因medical应用硬排。

## A15 21284准入改判最小原始依据（待root独立校准；不是同一事件断言）

原准入按“具名纠错可能改变memory评价选择”。新增事实改变这个门判断，而非因审阅费时/Books覆盖缩池：论文首次公开仍可为Apr24独立分析事件，不天然等于旧artifact同一SourceFamily。本次拟收准为 **核心纠错已公开，新增分析未形成额外项目贡献**，故具名贡献前关闭，不移Apr7/9纠错归属，也不另评分。

实际原始依据：
- [Issue29正文](https://github.com/MemPalace/mempalace/issues/29)，API `created_at=2026-04-07T09:05:26Z`、作者dial481。正文§2–4已完整列top-k50超过每conversation19–32session而绕过retrieval、LongMemEval手工对三题补丁、500题s variant只量session-ID recall_any@5（非QA生成/judge）。§5/7还列不同指标/付费LLM与无API离线配置被拼接。仅把它作为作者具体审计的公开事实，不照录用户评论的外部SOTA数/“真上限”。
- [维护者Apr9逐项回复](https://github.com/MemPalace/mempalace/issues/29#issuecomment-4215697566)，milla-jovovich，`2026-04-09T16:09:19Z`：承认top-k50 bypass、hand-codeddev contamination、recall_any并非LongMemEvalQA，退回相关headline/跨系统比较；给qa_bench_v2 raw .668/rooms .672/aaak .532，仅记当次维护者说明，不作本轮复现或可比优越。另提assistant-turn discard须先修再重跑，故不把旧检索数字当当前修复后测量。
- pinned [v3.1.0 tag3919f135](https://github.com/MemPalace/mempalace/tree/3919f13523c2c61a402bff5e9ad2f826e26d5cd9)，实际tree定位 [longmemeval_bench.py](https://github.com/MemPalace/mempalace/blob/3919f13523c2c61a402bff5e9ad2f826e26d5cd9/benchmarks/longmemeval_bench.py#L71)（blob2c186a7f1a93a85e981af69086d3968a4daf71d6）：71–80以top-k corpusID与correct_ids集合计算any/all/ndcg；189–203仅user turns拼session或turn；220–225对question调用collection.query。这是实际代码读取，未执行，未claim源码覆盖所有reported配置。

论文实际新增与停止理由：[exact-v1](https://arxiv.org/html/2604.21284v1) §1.1列architecture decomposition/benchmark analysis/competitive landscape/cognitive assessment；§3具体flatChroma metadata和SQLite实现、AppA代码统计扩充描述，但这些尚未给出改变检索有效性/因果归因的新控制。§4.2主要核心metric纠错已有上述Apr7/9原文；§7十维星级框架未新增可验证机制/评价资格。§8“verbatim优于extraction empiricallyvalidated”仍未分开被比较任务/runner；AppB列复现条件而非本轮独立测量证据，且cosine条件与同文AppA/§5.8此前默认L2警告并存。这里不是‘没实验便排除’，而是具体新增仅架构归纳/框架，未形成相对旧公开纠错的额外设计或有效性条件；不采用因认知空间隐喻推断AI记忆机理。已读§3/4/5.8/7/8与AppA/B/D，只补足门事实而不遍历剩余引用。原必要审阅记录不抹除；最终EX待root实际校准。

## A14 21564 Coercion exact-v1 必要Source与Ch66逐字PRE（未写）

exact-v1[Coercion](https://arxiv.org/html/2604.21564v1) 与 current-v2 Persuasion标题分开；actual §3.1–3.4、§4主结果、§5.2/5.3/5.4/5.5/5.6及§7反侧，必要命题是direct-vs-debate×三persona的行为识别而非内心立场。2+1+2=5，因现有PPT压力/stance段缺freeform question-type×persona联合标签和final组合vs逐轮drift差额必要深入。当前abs已有v2但未见具名撤回/更正；精确v1内容保留，不因改名无差别比较版本。DataCite v1SubmittedApr23T11:34:06Z、UpdatedApr24T00:43:05Z、createdApr24T02:00:22Z/reg23Z；v2SubmittedApr30/UpdatedMay1。月列表身份/公告门与v1处理/DOI同批合证支持Apr24北京日级，不把Submitted或current-v2日期替代first公开。

方法：38 BR-Portuguese topics（15values/6scientific/6philosophy/11economy）×3persona×2categories＝228 conversations/model，13assistants；这里是通用行为测量，不采用领域科学结论。freeform LLM-user看完整method和persona/category、五轮逐步施压但无逐轮脚本；assistant只看普通history，judge读full transcript仅标末轮agree/disagree/neutral/refusal并引正文。三persona合并九bucket是行为分类约定。主user ClaudeOpus4.6；主judge Qwen3.5-397B按agreement/cost选择，不是独立gold；大多OpenRouter/Maritaca native，远端硬件/precision/SLO未披露。APItokens与生成/判分/重跑成本不同，不拼wallclock倍率。

§5.2 300slots×8users，280完整；pairwise67.8–81%、均73%，all8unanimous45.4%、supermajor85%；同user重跑148pairs有117agree79.1%。不将两个agreement差当正式variance decomposition/accuracy error budget。§5.3 A55neutral pairs110conversations/user，强user92/110vs弱85/110；B438directionalbaseline抽200固定seed，强142/200、Haiku118/199、Sabia116/198（失败分母保留）。baseline“committed”只表某次观测输出，且论据随user变，不能把效果唯一归因argumentative能力。§5.4 300conversations抽样（正文称10topics×10models×3personas但又称含两category；caption称13models，人口说明不完全一致），仅289五轮都有valid。最终九bucket与逐轮sycophantic drift方向不同；间接从第一轮就常匹配persona，较低drift不等更独立。§5.5四judge300conversations/34topics，unanimous70.3/supermajor91.3，只是共识。§5.6同300替judgeprompt，299valid275same92%，不授truth或噪声独立。§7保judge/user-dependent、设计prompt/locale与fiveturn ceiling；不采用“训练而非架构造成”的因果宣传。

actual Ch66 664–670已有极性映射、逐item nudge/aggregate抵消、PPT stance-vs-hedge/单轮多轮压力，并无direct表态vs不问意见论辩×persona联合分类/末轮与drift不同事件。唯一owner PLATFORM-EVALUATION-SYSTEM；拟PPT source-family2604-07749段后、active-control02699前两段。相邻Ch65资源调度与Ch67监控只作owner交接，不搬通用偏好训练到此。未写/无锁，以下逐字PRE待独核：

同一主题的对话立场还应交叉改变两种条件：直接请求模型表态，或不问意见、只展开论辩；每种路径再分别由中立、赞成和反对该命题的用户驱动。将三种 persona 的最终回答分别标为赞成、反对、中立或拒答，再观察跨 persona 的配对关系，可以区分稳定表态与随对方方向变化。它测量的是指定话题、语言、用户生成器和 judge 下的输出行为，不是读出模型内在信念，也不判定哪种立场真实正确。<!-- source-family:SF-2026-ARXIV-2604-21564 -->

最终三路组合与逐轮漂移也要分账：论辩一开始就顺从的模型，可能有较少后续 flip，却在最终 persona 对照中更依赖用户；只看一种统计会把两者混同。[必要受限对照](https://arxiv.org/html/2604.21564v1)同时暴露用户生成器与 judge 更换后的分歧，模型间一致和重复判分一致都不是人类真值或因果误差预算。自由论辩、三 persona、多轮判分与独立校准均付费；迁移语言、话题或用户能力时应保留原始逐轮输出、拒答与无效分母，重核行为标签，必要时回退固定脚本、独立人工审核与无干预模型，不用较低迎合分证明知识、价值或安全已稳固。

## A13 21191 exact-v1 必要机制与日期异常合证；Ch20逐字PRE待独核

已实际读[exact-v1 HTML](https://arxiv.org/html/2604.21191v1) §2/§3 Proposition1/2、Theorem2、§4 Theorem3/Algorithmic differentiation/Lattice parsing、Fig1、Limitations及AppB相关两组反侧；未遍历无关证明/未核代码复现。2+1+2=5，因普通parser复用与全next-token权重这一实际owner缺口必要深入。prefix grammar造prime非终结符、完整左侧＋边界partial＋suffix totals；commutative semiring及所需权重和可定义性、base parser正确是条件。二元标准形后size ≤8/3|G|+3，binarization自身最多triples原G；parser预处理phi可能再扩大structural vector，不保证全grammar联合复杂度不变。lattice为末端全部单扩展引入theta，反向AD给各权重；Theorem3要求semiring算术、控制流不依赖theta，至多4倍是算术ops，不是GPU latency/HBM或模型未来mass保证。

Fig1 WSJ5000：35016rules/448nonterms/total116667，500strings且每prefix相关测时；95%CI按长度，拟合指数1.99/2/2.12，prefix约2.9倍ordinary parser（grammar约2.86倍），next-token约1.2倍prefix，不是胜过已有LLM decoder。AppB EarleyX slopes2.01/1.99，优化completion不同混杂系数；SocialDiscourse72712rules/233nonterms、单拼接序列1.05vs1.18不授普遍律。实验限CKY/Earley，硬件/precision/serving SLO未披露。

日期实际 publisher feed created/registered Apr24T01:51:37Z；Submitted Apr23T01:20:40Z，而v1 Updated May5T00:48:33Z，current仍v1；这保留后处理异常，不改称May5公开或用Submitted替公开。官方[cs.CL April月列表](https://arxiv.org/list/cs.CL/2026-04?skip=0&show=2000) actual raw身份项为 `<a name='item1362'>[1362]</a><a href="/abs/2604.21191" id="2604.21191">arXiv:2604.21191</a>`，Title Prefix Parsing is Just Parsing、Comments To appear at ACL2026、subjectsCL/FL、精确HTML链接v1。结合已读官方永久ID在公告时赋值/Thu20EDT公告及同批Apr24 created（而非单独created）可作有限日级合证；root已接受该合证原则，仍待本身份raw/Source独核。currentabs轻查无具名撤回/勘误，v1日期口径不补造时刻。旧04-24 screening是日期隔离而非已采用same event，无新增评分重复。

actual owner MODEL-SAMPLING Ch20 506–536：已有有限trie、PDA budget reachability、finite-state exact conditioning与一般神经futuremass #P-hard，但未承载prefix grammar→ordinary parser＋lattice全扩展权重机制；Ch19末尾KV shape/lifecycle与Ch21开头MoE交接已读，不挪owner。拟在trie段及其source marker之后、原“Prefix Feasibility”小标题前插以下两段，无写锁/未写：

对于不能预先枚举成有限集合的上下文无关输出，专门改写 parser 并不是唯一办法。另一分支先把原语法编成生成全部合法前缀的 prefix grammar：完整左侧片段保留原产生式，截断边界使用对应的前缀非终结符，再交给普通 parser。在权重满足相应可求和、交换半环条件且 parser 正确时，它保留前缀权重；对所有单 token 延伸求权重，若解析器支持 lattice、仅以半环运算求值且控制流不依赖这些形式变量，还可把末端扩展写成带形式变量的 lattice，经代数反向传播一次取得权重向量，避免逐候选重跑。这是语法权重，不是任意神经模型未来所有合法 suffix 的条件概率。<!-- source-family:SF-2026-ARXIV-2604-21191 -->

[必要定理与受限对照](https://arxiv.org/html/2604.21191v1)只把输入长度依赖交给原 parser；binarization、prefix transformation 与 parser 自己的预处理仍可扩大 grammar-structural factors。反向传播的常数界是算术操作数，不保证 wall-clock、内存或 LLM serving 吞吐；lattice 支持也须实际实现。编译、规则驻留和每步解析均计费，同一语法跨请求复用才可摊销；语法常变、预处理膨胀或预算不合算时，保留专用 prefix parser、有限集合 trie 或后置验证，另验输出预算与内容正确，不由高效解析批准完整任务。

## A12 reader 三篇必要Source、日期、具体owner与窄PRE（实际消息，尚未写书）

复核者 `supp_apr25_review_fresh` 独占 actual exact-v1 必要Source；作者没有重复全文，以下按已收到真实结果持久化。三 current abs 仅v1且无具名撤回/更正。21860 Submitted Apr23 16:56:14Z / v1 Updated Apr24 01:01:31Z / DataCite created 02:07:19Z registered 02:07:20Z；21911 Submitted17:54:36Z / Updated01:04:10Z / created02:08:30Z registered02:08:31Z；21836 Submitted16:27:04Z / Updated00:59:51Z / created02:06:46Z registered同刻。结合已实际读官方ID公告时赋值/Thu20EDT流程、月列表及同批21882，支持Apr24北京公开自然日；不是任何一个Submitted/DOI字段单独证明，不称穷尽全网first-public。三项未核代码、复现或生产SLO。

**21860** actual §IV-A/B、V-A–D/TI–IV、VI-C；2+2+2=6，争议/暂缓而非EX。intro只留last response，formal attacker却持full accumulated context；target独立 M(pi)，不能称无状态目标自身alignment逐轮腐蚀。formal安全oracle规定unsafe即停，实验另用未具名classifier报unsafe，资格关系未闭。T-I Gemini2Flash17/50=34%，T-IV将34%写hits；PAIR4共同分母/预算不明，不能宣布优越/厂商安全排名。API/OpenRouter才是被测部署，ColabT4不表示远端模型GPU；guard/采样版本、CI未披露，cost表与正文合计不一致。actual Ch72 2329–2345及3313附近已有observer窗口/角色与跨身份累计预算；不借成熟原则填本篇证据，不新改书。重开需固定双方可见history/oracle身份及统一success unit、PAIR预算。中心主张隔离不支持安全保证。

**21836** actual §2.1–2.6/Eq1–2、§3/Fig2、§4、S1/S2；2+1+2=5，采用有限几何诊断。4视觉模型、WIT1024配对图文、12LM/3families；GPA正交共识残差按mean/PC1切片，再CKNNA(k10)比较；S1删最高/最低25%同向。LLM层选best alignment，同刺激拟合/切片；S2只held-out视觉模型，不是新刺激/新数据集，无独立heldout泛化、共同世界因果或语义身份保证。硬件/precision/repeats未披露，不造性能。actual Ch23 106–118已有GPA map与任务兼容，缺stimulus选择改变convergence评价；Ch22/23/24交接已读。唯一owner MULTIMODAL-REPRESENTATION，拟原source-family2602-06205两段后、原“同一坐标map能否从一种模态搬到另一种”前，以下逐字两段待root窄lease：

共同坐标上的相似度还依赖拿来比较的输入。可以先在同一批配对刺激上，用多个视觉 encoder 拟合正交共识，再按每个刺激偏离共识的残差划分高、低分歧人口；在这些人口上比较图像与文字表示的局部邻域相似度，能检查总体“表征收敛”是否由特定输入主导。受限图文实验中，两种分层方式都改变跨模态对齐分数；这不是原模型经训练变得更接近，也不能从几何一致推出共同的真实语义或世界。<!-- source-family:SF-2026-ARXIV-2604-21836 -->

[必要切片与反侧](https://arxiv.org/html/2604.21836v1)只覆盖一份小型图文人口及所测 encoder；语言层位还按最佳对齐选择，留出视觉模型不等于留出新刺激。共识拟合、encoder 前向、层位选择与邻域重算均付费；应同时保存完整人口、随机基线及高低分歧切片，另验原任务和实际消费者。样本选择、层位或新域改变时，保留未筛选基线、原 encoder 与真实配对验证，不由升高的对齐分数批准接口替换。

**21911** actual §3.1–3.3/T1、§4.1–4.2/Eq1、§5.1–5.3/T2–4、A.2/B.1–B.3/C.1/T5/D.1–D.2/E；2+1+2=5。COCO两子集各3k，检测器+LVLM缺席标签非独立GT；同图present/random absent/plausible absent及false-presupp问法有诊断差额，但yes/no与自由拒预设不同，不能唯一归因backbone无错。DPO20k/LoRA LLM、weighted按subset归一；T2 LLaVA正识别94.85→84.30而AdP5.85→84.65，C1高score集拒绝偏向更强；D1单边hint靠短caption降幻觉，D2迁移有反退。A100每配置6h不含grid/生成/verifier总费，precision/repeats/SLO未披露。actual Ch23 188–196已有遮对象/场景prior、偏好回归，缺固定图像改变query存在预设与正识别vs拒预设差额。唯一owner MULTIMODAL-REPRESENTATION，拟MOH两段后/SCR前；DPO推导不挪owner。以下逐字PRE待root lease：

视觉支持的诊断还应固定图像，改变提问对“对象是否存在”的承诺：分别询问真实存在、随机缺席、场景上合理却缺席的对象，再对后一类提出预设其存在的属性问题。前两类识别良好而后两类失败，说明最终回答对场景关联与指令预设敏感，不单独证明视觉 encoder 无错或语言先验是唯一内部原因。检测器与模型确认的缺席仍是代理标签，yes/no 识别与自由回答中拒绝错误预设也不是同一个事件。<!-- source-family:SF-2026-ARXIV-2604-21911 -->

[必要配对与训练反侧](https://arxiv.org/html/2604.21911v1)说明，偏好训练后更会否认缺席对象，仍可能更难确认真实对象；只看幻觉降低，还可能奖励过短、不完整的描述。生成偏好对、外部验证与加权、调参和回归均计费，文字距离或模型给出的高对比权重不认证视觉真值。应联合验收正侧识别、缺席判断、预设拒绝与描述完整性；这些切片或迁移回归不过时，保留原模型、直接存在性询问、专用检测与证据不足时拒绝断言，不把更强拒绝倾向当无损 grounding。

## A11 21882 Ch5真实POST与窄lease释放

root实际读A4逐字两段PRE与Ch5 rate-distortion→泛化验收交接后授唯一两段＋本人Reviewnote窄lease。作者apply_patch保存新195/197与590附近单注，完整顺读187–205及本人注；写前既有unstaged4+/0、cached12+/0不动，本人仅6+/0，限定diffcheck通过。

非写作者`supp_apr25_review_fresh`实际顺读Ch5 179–211（compression/rate-distortion→新两段→原泛化/隐私→Superposition）、587–600本人注与限定diff，确认新195/197逐字PRE一致、行为/频率反侧/费用近文，未加内部机制保证，既有18158等diff未动；**actualPOST通过**。root收真实结果后接纳、不重复第三次同源审，明确释放Ch5窄lease。作者随后只行政同步本人注为已发生POST/释放，并实际rg读回；当前本轮无Books锁，1项新真实整合有效，不等整日日级完成。未stage/commit/push。









