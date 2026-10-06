# Nov27 题摘筛选与终态日期保留

作者Aristotle；本日窗口见[SOURCE_CHECK](./SOURCE_CHECK.md)。确定项只有Mixpanel，见[单项证据/owner](./MIXPANEL_EVIDENCE_OWNER.md)与[Carver单项通过](./MIXPANEL_INDEPENDENT_REVIEW.md)。原46项加Carver恢复Math-V2，共47项**潜力不是47个当窗候选**：均未评分、未作Books正面采用，也未授全methods/实验；有限日期恢复后隔离，不用摘要缺少细节或没有owner名称关闭。

## 原始权限与最小日期恢复

四组窄提交查询63返回/59唯一身份，DC月表仅两个50标题段，不是全年/月全部队列。完整题摘实际读：首八篇raw-first-exact3/raw-first-fullabstract4；Kyrgyz/Image2Gcode raw-negative-and-recovery5；后续八篇raw-bounded12/13；安全/TAB三篇raw-bounded18；Batch原生[完整题摘](./batch-denoising-abs.html)。相关剩余25篇逐一取原生exact-v1完整题摘，保存[完整题摘/版本history](./remaining-exact-v1-abstracts.json)及各`abs-IDv1.html`，不使用API晚版摘要代替v1。

每个具名身份均实际原DataCite一次，字段[exact-date-fields.json](./exact-date-fields.json)，保留Submitted、Updated、Available、created/registered原值及receipt。Available多为2025-11；2512.03057/03053为2025-12，提交Nov不能倒填Nov公开。部分ID（20710/20736/20737等）created/updated在本窗终点之后：不由元数据上界直接推出全球首次公开在窗外，也不补本窗下界。首批/多模态/安全具名搜索实际第一页见[真实queries](./web-queries.json)，第三方RG/HF/alphaXiv只恢复身份，不授原公开时刻。后25项止于官方exact-v1/history/原出版元数据，不逐项追加搜索网或全文。

本次没有取得足以把以下first-public上下界完全约束在[Nov26 01Z,Nov27 01Z)的原事件证据。重开只需相应作者首公开事件、官方历史公告或精确原发布上下界；不能用schedule补时刻、submitted代public、或晚版更改冒充first-v1。缺日期不是贡献否定；有界尝试后不支持本日正面证据或Books，不阻塞其他日期。当前所读原页未见撤回标记，不等于遍历完整撤回历史。

## 首批及必要尾部21项潜力

以下每项是“原约束→实际题摘增量→可能需修正的选择”，实验可信度不由题摘认证。

| 精确v1身份 | 潜在具体增量与采用限制 |
| --- | --- |
| [QiMeng-Kernel 2511.20100](https://arxiv.org/abs/2511.20100v1) | 全kernel策略/code空间耦合→macro RL与micro LLM分工→需核正确性、性能/搜索预算归因；不授near100/34x保证 |
| [Beluga 2511.20172](https://arxiv.org/abs/2511.20172v1) | RDMA池与CPU通道成本→CXL shared load/store GPU KV架构→需核寻址/一致性及访问路径配置；v2 Nov27 06:20Z窗后不借 |
| [Softmax Turing 2511.20038](https://arxiv.org/abs/2511.20038v1) | softmax CoT表达条件→unary/letter-bounded C-RASP与relative-position extension→需核精度/长度条件，不授可学习任意程序 |
| [Directional Asymmetry 2511.19997](https://arxiv.org/abs/2511.19997v1) | function class对称不保证优化路径对称→synthetic entropy-floor及GPT2/MLP/LoRA对照→局部学习反证而非根本架构因果 |
| [Sparse Coding Transformer 2511.20194](https://arxiv.org/abs/2511.20194v1) | context组合泛化→learned dictionaries/sparse coefficients线性组合→需核task/capacity公平对照；NeurIPS标记非公开时刻 |
| [Mosaic 2511.19822](https://arxiv.org/abs/2511.19822v1) | 单corpus专家剪枝跨域退化→跨任务cluster与Activation Variability Score选代表→需核域组成/预算和迁移反侧 |
| [CafeQ 2511.19705](https://arxiv.org/abs/2511.19705v1) | calibration不可得→proxy loss structured single/dual transforms+adaptive rounding→需核质量/额外计算，不按指标小关闭 |
| [ParaBlock 2511.19959](https://arxiv.org/abs/2511.19959v1) | BCD本地/通信串行→双线程且同rate条件→需核staleness与资源，不借成熟overlap原则收；v2 Jun2026不借 |
| [KyrgyzBERT 2511.20182](https://arxiv.org/abs/2511.20182v1) | 小模型/语种适配资源取舍→35.9M与mBERT177M任务对照→仅保留局部size/quality，不称新morphology机制或五倍计算效率 |
| [Vision-Language Memory 2511.20644](https://arxiv.org/abs/2511.20644v1) | video状态随长度增长→working window/episodic consolidation/view-consistent3D→需核记忆/几何一致性取舍；Jul2026v2不借 |
| [Object-Centric Pruning 2511.20439](https://arxiv.org/abs/2511.20439v1) | VLM视觉token开销→small object pruner及reconstruction objective、无需VLM finetune→reconstruction保证不等于全部任务准确率保证 |
| [WPT 2511.20095](https://arxiv.org/abs/2511.20095v1) | world rollout策略部署成本→teacher轨迹reward与policy/world reward蒸馏student→潜在训练/推理边界，不授现实驾驶安全 |
| [MAPS 2511.19878](https://arxiv.org/abs/2511.19878v1) | VLA适配损失原VL表示→module-wise proximity relaxation/action更自由→与freeze/uniform regularization比较，非成熟正则标签关闭 |
| [GigaWorld-0 2511.19861](https://arxiv.org/abs/2511.19861v1) | 视频外观/控制/物理一致性不能互代→3D differentiable system identification+executable planning生成VLA数据→核组合成立条件；Nov30v2不借 |
| [INTERLACE 2511.19676](https://arxiv.org/abs/2511.19676v1) | VL剪层后适配→三层组前两层剪/微调、第三层freeze anchor→需核1% FineVision一epoch预算与质量，不授全域鲁棒 |
| [Neuroprivacy 2511.20710](https://arxiv.org/abs/2511.20710v1) | caption utility/隐私攻击取舍→topographic tau正则与caption-query membership inference→只局部攻击评价，非DP或全部VLM隐私保证 |
| [CANVAS 2511.20737](https://arxiv.org/abs/2511.20737v1) | UI终分可能遮蔽过程不稳→replication/modification与工具/长轨迹错误侧→需考虑重试/排除样本及中途退化，不因benchmark自动收 |
| [Adversarial Confusion 2511.20494](https://arxiv.org/abs/2511.20494v1) | targeted jailbreak不是唯一图像干扰目标→next-token entropy ensemble perturbation→潜在局部不确定性/transfer边界；v2/3窗后不借 |
| [TAB 2511.20507](https://arxiv.org/abs/2511.20507v1) | LLM语言评价可能漏局部能力deficit→四QAB-derived子测/自动评价与human agreement→可审评价可靠性局部边界，不诊断人类疾病或仅临床标签关闭 |
| [Complicit Responses 2511.20736](https://arxiv.org/abs/2511.20736v1) | 一般安全分数无法代表不同scenario/intent→EVIL及局部SFT/DPO前后负侧→核法律情境/judge/数据混合，不授安全训练普遍有害 |
| [Batch Denoising 2511.19847](https://arxiv.org/abs/2511.19847v1) | denoising生成与传输共同占deadline→STACKING batch分配且quality-function形状无关、再分bandwidth→潜在生成质量/端到端时延边界，不因wireless应用名关闭 |

## 相关窄查询尾部25项潜力

这不是DC338/月所有题摘队列：只针对上述四个实际窄查询中的相关标题，取exact-v1题摘一次。以下尚未深审，不以摘要声称的优势认证因果/生产能力。完整题摘及history见remaining-exact-v1-abstracts.json；同一材料的晚版不复用。

| 精确v1身份 | 潜在具体增量/界限 |
| --- | --- |
| [SMFA 2511.20196](https://arxiv.org/abs/2511.20196v1) | refusal forget update伤理解→retain anchor的方向冲突+相对幅值mask→局部forget/retain取舍；拒答不证明信息删除 |
| [Beyond Generation 2511.20531](https://arxiv.org/abs/2511.20531v1) | 三种KG表示的caption verification/coherence不同→局部hierarchical vs bullet/triple取舍→核心确认后保留潜力；不能将缺KG项定义的hallucination计数当开放域事实真值 |
| [CAPNET 2511.20641](https://arxiv.org/abs/2511.20641v1) | tail数据不足致label correlation不可靠→从CLIP text提取label correlation、prompt/graph adaptation→需核同预算head/tail条件，非组合名称本身增量 |
| [Conditional PAC routing 2512.03057](https://arxiv.org/abs/2512.03057v1) | marginal保证不能直接变pointwise→non-atomic distribution-free conditional几乎总expert不可能性→潜在可靠性/成本边界；v1没有晚版setwise router方案，Available原月Dec不回填Nov |
| [Analogies 2511.20344](https://arxiv.org/abs/2511.20344v1) | 表示关系与应用到新entities不同→mid-upper relation signal/critical-token patch局部恢复→需核causal intervention，不类比人类完整认知 |
| [NNGPT 2511.20333](https://arxiv.org/abs/2511.20333v1) | 架构生成不等可执行/低搜索成本→scope-closed blocks、code-aware early-stop预测及可执行语料反馈→需核生成/评价预算和泄漏，不采用73%作全自治证明 |
| [Geometry 2511.20315](https://arxiv.org/abs/2511.20315v1) | MCQA决策层表示不可见→28模型多ID estimator层间expand/compress与决策对照→局部表示证据，不因观察型或小任务关闭，不授通用因果 |
| [Singular Circuits 2511.20273](https://arxiv.org/abs/2511.20273v1) | head/MLP不可分假设→orthogonal singular方向内superposed subfunctions→可能改变解释单位，未审IOI/GP/GT全部干预 |
| [MTA 2511.20072](https://arxiv.org/abs/2511.20072v1) | 每user adapter线性存储/fewshot差→shared anchor bank动态merge+ultralow-rank stacking→需核bank/runtime/metadata总成本，非LoRA成熟即关闭 |
| [EfficientXpert 2511.19935](https://arxiv.org/abs/2511.19935v1) | general pruning mask跨域失效→propagation-aware Foresight与Partial Brain Surgeon adapter update→需核域dependent structural shift/训练成本，保留v1而非晚版修辞 |
| [Active Slice 2511.20713](https://arxiv.org/abs/2511.20713v1) | error slice注释预算有限→active grouping+annotator membership验证→局部uncertainty选择/2–10%预算取舍，不授所有slice效果 |
| [Emotion Gender Bias 2511.19785](https://arxiv.org/abs/2511.19785v1) | 推理提示debias不等训练干预→同emotion任务的训练vsprompt局部对照主张→需核实际偏差定义/对照，不能推断真实群体特质 |
| [LocateAnything3D 2511.20648](https://arxiv.org/abs/2511.20648v1) | 2D/3D decoding易难混杂→Chain-of-Sight与near-far/中心尺寸旋转curriculum→潜在next-token 3D表示；v1 AP49.89不是晚版38.90，不混协议 |
| [ArtiBrain 2511.20330](https://arxiv.org/abs/2511.20330v1) | articulated长程/新part迁移→geometry keyframes+affordance diffusion/memory propagation→需核分层generalization及模块收益，非benchmark自动收 |
| [AD-R1 2511.20325](https://arxiv.org/abs/2511.20325v1) | world critic optimistic long-tail→counterfactual collision/offroad synthesis→局部world failure预测与policy refinement条件，不采根本缺陷/现实安全保证 |
| [MAP-World 2511.20156](https://arxiv.org/abs/2511.20156v1) | 单路径selection丢其他futures→masked多mode action+path-weighted semantic expectation→可能改变训练selection，未证全部驾驶泛化 |
| [Foundry 2511.20721](https://arxiv.org/abs/2511.20721v1) | specialist蒸馏损失taskagnostic表示→SuperTokens重建teacher token空间→潜在下游通用性/预算条件，非FLOPs headline认证端侧效果 |
| [DeeAD 2511.20720](https://arxiv.org/abs/2511.20720v1) | confidence-based exit不直接代表action可行→trajectory与轻量planning prior偏差、多hop层skip→局部quality/latency条件，不采全部safeclaim |
| [Reasoning-VLA 2511.19912](https://arxiv.org/abs/2511.19912v1) | action自回归与车辆配置迁移→Gaussian初始化learnable action queries并行轨迹→需分离CoT数据/SFT/RL与并行收益 |
| [Agent0-VL 2511.19900](https://arxiv.org/abs/2511.19900v1) | text self-eval hallucination→同LVLM solver/verifier的tool-grounded reward/repair循环→需核tool证据与selfreward分布；作者repoNov25“released on arXiv”日字段无时区，不把提交日说法直接当精确public |
| [CropVLM 2511.19820](https://arxiv.org/abs/2511.19820v1) | 高分辨率细节/fragmentation→外部RL zoom无box标签、目标VLM不微调→潜在perception budget/可迁移边界，不自动认证catastrophic forgetting无风险 |
| [Scanford 2511.19647](https://arxiv.org/abs/2511.19647v1) | 互联网数据漏deployment OCR→robot采集+catalog监督/域相邻OCR改善→局部部署/数据获得反证，不因library应用名或闭环成熟关闭 |
| [QiMeng-CRUX 2511.20099](https://arxiv.org/abs/2511.20099v1) | 自由规格到受限Verilog歧义→structured semantic intermediate与双空间训练→潜在约束表示及transfer条件；v2窗后Updated不借 |
| [R3A 2511.20090](https://arxiv.org/abs/2511.20090v1) | fixed repair template/随机LLM不稳→heuristic stochastic ToT patch search+multi-agent fault localization→需核同time budget/测试正确性，不由pass@5推生产正确 |
| [Invertible check 2512.03053](https://arxiv.org/abs/2512.03053v1) | code输出语法成功不证明规格无遗漏→LCT↔HDL roundtrip反构比较→局部验证盲区候选，不授lossless/全正确；Available Dec且Submitted Nov分开 |

## 安全、负侧与必要定点实际读取

**Kyrgyz** exact-v1 HTML III/IV L64–103实际读：普通WordPiece30,522/fromscratch六层512、35.9M、私有1.5M句、单RTX3090；translated SST2训练/验证，1821测试人工native标注，weightedF1 .8280 vs mBERT .8401/177M。没有tokenizer控制消融或实际训练/推理资源benchmark；只保留局部size/quality潜力，不新造 morphology算法，raw-bounded8/10。

**Neuroprivacy** exact-v1 III/IV与V消融实际读，raw-bounded15/16：attacker仅image-caption query/output、无gradient/params、未限query；400member/400nonmember、80/20拆分，MPNet/ROUGE2/ROC-AUC，无shadow。tau0/2/3跨三个caption模型/三个dataset；granularity与BLIP NoCaps反侧不一致。utility只caption评价，不是全部VLM能力/DP。日期隔离，不作privacy保证。

**CANVAS** exact-v1 failure L265/325–333/1248–1266实际读：开放模型多turn高失败/blank被排除；工具调用重试三次后failed samples跳过，Gemini2.5Flash7/100 turn0 malformed排除；长trajectory可能退化。final score不代表过程稳定，benchmark不是根本架构因果。raw-bounded16。

**Adversarial Confusion** exact-v1 §2/3/4必要core/table/limits实际读，raw-bounded19–22：entropy objective与clean/noise、cross-family heldout不同于有害内容成功率。小预算proprietary transfer失败；large visible noise不能称imperceptible保护；multi-step Agent、compression/render/geometric变化明确未来工作。公式(3)加gradient而文字L=negative entropy，与目标最大entropy存在符号疑点，保留实现未核，不自行修正或授attack正确复现。本文不证明网站部署anti-agent安全。

**Complicit Responses** exact-v1 Methods/Study4/Discussion与训练设置定点实际读，raw-bounded19–22：court scenario+intent synthesis、两地各300人工样本；GPT4o judge human对照是作者局部评价，不授全部场景96%或合法性普遍标准。Qwen3-8B/Llama3.1-8B、不同语言/混合安全dataset及SFT/DPO配置前后EVIL负侧不证明全部alignment有害；CoT stereotype相关不能认证因果或真实群体属性。实际安全/责任/可信度定义不同，旧SafetyBench和EVIL跨协议不能直接变同条件性能下降。

**SMFA** exact-v1 §3/4/5.1/Table1/Table2/5.3受影响机制与反側实际读，raw-bounded23/24：retain anchor mask同时方向冲突与relative magnitude；only-one mask恢复retain但forget弱。虚构1000profile、两7B LoRA、fewshot retain与forget同数、5/10/15%比率，重生成query及ROUGE/Qwen judge衡量输出拒答/理解；这不证明参数中信息删除、抗再次提取或formal unlearning/隐私保证。医学图像这里只作论文反侧，不打开AI for Science研究路线；不遍历附件。

**Agent0日期恢复** 作者repoNews Nov25 Agent0-VL released on arXiv，Nov26群组、Nov29Agent0 code是不同事件；缺时区且可能引用submission标签，不能用Nov26群组重造研究family或让Nov29code提前。raw-bounded23/24。后续公开上下界未定仍隔离，准备好别项先走。

## 代表性关闭与范围外线索

- [Image2Gcode](https://arxiv.org/abs/2511.20636v1)：完整v1题摘实际读，slice cue+DDPM G-code绕CAD为制造流程mapping，没有原文新增通用模型机制/条件主张；关闭不是因DiT成熟。日期未核不影响此处置；晚版不借。root仍可针对原core的通用trajectory反例重开。
- Beyond Generation初始拟关闭**已在必要core后撤销**：实际§3.1/4 Table1/limits L97–204给出hierarchical空间验证与coherence、bullet直接属性等局部对照，足以继续潜力，而非借成熟KG原则。100image、55→38只作者局部，hallucination定义含absence in手工KG与matching threshold，不能推出开放域事实真值；不同protocol不合并31.8/27%。没有继续所有附录，raw-bounded25。日期仍隔离，原ICML workshop标记不是first-public精确时刻。
- Qualitative Laboratory完整API题摘是sociological persona simulation产生climate-reception理论hypotheses；研究对象是社会科学应用/访谈方法，不新增模型或Agent系统机制，范围关闭，不授人类行为模拟真值。
- MoRE multi-omics、Frailty driver-retention survival、depression/medical-error、materials active-learning、Alzheimer synthetic graph、PET/CT报告、LeafArea forecasting、medical segmentation、histological grading、FastMRI等标题明确领域应用/暂缓方向；保留原窄query发现标题，未读其全文/全摘要、不声称全类排除。
- Seed DA3文章原窗内PublishDate明确，但官方项目News Nov14全套released及文章Recently unveiled支持旧首事件背景；当前bug-retrained1.1/original deprecated信号实际核表，日期未定只保留，不采旧数字安全保证、不制造第二当窗family。见SOURCE_CHECK表外段。

## 非作者最小恢复新增一项

[DeepSeekMath-V2 2511.22570v1](https://arxiv.org/abs/2511.22570v1)：Carver实际由本日主页Research More进入[原Research](https://www.deepseek.com/news/)，读完整v1题摘/原history及[官方repo](https://github.com/deepseek-ai/DeepSeek-Math-V2)引言，见[SOURCE_INDEPENDENT_REVIEW](./SOURCE_INDEPENDENT_REVIEW.md)。终答案正确不认证推导正确→准确/忠实verifier用作generator reward、自检自修，并增加验证计算标注困难proof→可重新考虑verification-generation gap与训练反馈机制，保留主线潜力，不因数学标题当科学应用关闭。官方Nov27无时区；v1 submitted `2025-11-27T16:01:22Z`不是first-public。有限原恢复仍缺完全落窗上下界，只具名隔离，不评分/列确定候选/写Books，不采用IMO/Putnam宣传数字或授全methods。

## 独立请求与作者停点

Mixpanel单项已独立通过；Carver已核原46潜力题摘/日期、必要反侧和代表性关闭，新Math-V2最小恢复后合计47潜力。不要求全部全文。DAY三项报告事实返修已同步，剩非作者定点确认及作者本地检查；来源历史缺段按SOURCE_CHECK精确重开。作者fresh28继续，不等待独立汇总、不改Books/state/index。
