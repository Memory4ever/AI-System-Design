# 第十批必要核心

四项完整v1题摘经root具体准入校准；15485一次core拟贡献EX见[V3_CONTRIBUTION_DECISIONS](V3_CONTRIBUTION_DECISIONS.md)，不是因证据弱退队。四identity Submitted Feb17 10:59–12:38Z、原同DOI Created/Registered Feb18 02:42–02:43Z，结合官方日程下界Feb18 01Z完全落窗，无更早公开线索，Updated不用。

## 15491 Equalizer — 2+1+2=5，必要核心/反侧完成

actual[exact-v1](https://arxiv.org/html/2602.15491v1) §2–5/Fig1–5/Eq9：仅global gain±12dB就改变DAC/SpeechTokenizer/BigCodec latent方向和codeword，故embedding后再norm不能复原原shape。经典shape/gain原则前移到encoder之前，40msframe/20msstrideKBD norm+OLA、scalarμlaw8bit单独传，decoder后restore；必须重训normalized输入，非即插即用现codec。DCS正文定义写different比例却图解用stable比例，具体55–85%数不照采用。

16kHz LibriSpeech100h90/10分、testclean2620utterance40speaker5.4h；samearchitecture/dataset/procedure形状gain消融、EnCodec conv+两层BiLSTM、100kAdam/B16×3s/4A100，非streaming实现（BiLSTM双向更不能自动因果）。全bitrate含额外gain400bps，3.2kbps接近baseline4kbps只这些STOI/PESQ/SISDR gainaverage；C256vsC1024 PESQ/STOI更好但小gain SISDR反侧。externalSpeechTokenizer960h不等matched训练，4/8倍codebook storage/search复杂度非E2Etime实测。seed/CI/precision/完整latency未给，语音非任意audio/music，gain恢复误差/低能量与shape失真需保留。

## 15521 ExpertWeaver — 2+1+2=5，必要核心/反侧完成

actual[exact-v1](https://arxiv.org/html/2602.15521v1) §3–4/Tables2–3/Fig4–6、A2/F/L。42Flan任务各5sample取tokenmeanSwiGLU gate profile，CV阈值决定layer共享ratio，highestabsmean入alwaysshared、其余balancedKmeans成expert，同neuron gate/up/down slices保持；router由gate vectors均值初始化。无需额外router训练不等剪后function等价/无校准成本，pruning是unweighted sum，CPT改为softmaxweighted是不同计算函数。adaptive layerallocation只低sparsitypruning；downcycle固定uniformratio，不套一张图所有训练。

25%active sparsity保留全部weights，Llama8B60.4低dense72.8/Qwen7B67低75.2，优于有限pruner不无loss。Qwen 7Btotal/3.5Bactive经200Btoken CPT/128H100/B1024/seq4096/50k及64H100两阶段SFT，upstreamdensepretrain也付；不同基座/数据/activeparams非相同totalbudget，OLMo58.9与500BOLMoE58.9的相等局部不授普遍更省。direct OLMo1.3B vs575Mupcycle不同上游容量，loss优势非独立证明高optimization ceiling。

servingA100/H100单GPU vLLM/TP1/KV90%/1024random requests/input平均512/infinitearrival/concurrency128，表tokens/RPS关系暗示output128但正文未明报，不补造；A10022.88vs18.85/H10044.04vs41.41RPS峰值，不qualitymatched/SLO或低load保证。precision/seed/CI/校准搜索全成本未披露，失配/动态gather代价及layersharedratio被调MMLU保留。必要owner待比较，非全附件。

## 15532 StructuredCapabilities — 2+2+2=6，必要核心/反侧完成

actual[exact-v1](https://arxiv.org/html/2602.15532v1) §3–5/Table2–3。OpenLLMLeaderboard4576模型64架构，drop181不全结果→4395模型19BBH MCQsubtasks；logparameters进入latentfactor结构、task-specific error与PCA分开，guessfloor校正logistic再inverse变换fitSEM。不是参数量的干预因果、不是自动识别真实g或“结构越多就能力真”。log变换仅B在(c,1)有效，边界处理不能由公式自动授；不同transform likelihood不能跨原/变数据直接AIC比较。

Horn平行分析选5factor，raw72%首factor改41/36/14是所选模型拟合、factor旋转/排序非唯一机制。Table2同transform结构模型AIC/BIC改善但CFI/RMSEA等fit反差，不写全面胜。out-of-fold先hold19中1task、其余tasks包含全model估factor，再bottom80% heldtaskscore拟top20%预测，不random heldmodels/futurefamilyOOD；SCtestMSE1.156vsOSL1.473均值更低但19task ttestp.637不显著，12/19赢非全面。作者明确observational/noCFA/onlycontrivedBBH/无安全与生态验证，不能认generalcapability因果。分析既有结果非模型GPU吞吐实验，费用为数据清理/变换/SEM/验证维护，未复现。

## 15537 ZeroSyl — 2+1+2=5，必要核心/反侧完成

actual[exact-v1](https://arxiv.org/html/2602.15537v1) §3–5/Table1–2/Fig3。冻结WavLMLarge layer13 norm滑窗3/prominence.45σ峰作音节边界，layer22pool后sphericalKmeans10k，100h训练clustering；silencecentroids小分支合成1→9116词表。noencoderfinetune不等零训练，layer/window/threshold在development调，silence分支由informalinspection辨认非独立证明全无监督。phoneforcedalign+rules的gold/50ms容差/每system dev时移/不评silence边界，ZeroSyltokenF154低SyllableLM56。

OPT125M（后文叫100M架构不补精确不同模型）、context2048/B81920tokens，6kh LibriLight25k单GPU、60kh200k；SyllableLM两GPU多50%steps按高tokenrate，不同SSLbackbones更强WavLM混杂，SpidR引用paper非作者matchednewrun。syllabic~4.35Hz/entropy52bps不是完整codec wirecost/可重构全音色；scaling语法继续收益但lexical落后frameSpidR，narrative60kh接近。meanpertoken loglikelihood用于各任务，改未归一BLIMP分数会变；未覆盖其他语种、生成音质或在线latency，硬件型号/precision/seed/CI未报。只采frozen层不同功能与temporalunit×language任务取舍。
