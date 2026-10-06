# 02/13 CSIX：11073 / 11079 / 11083 / 11096

四项准入已root独立校准，均在119逐项日期包络交集中；只exact-v1必要支持/反侧。原返回CSIXINITIAL/CORE0–3/MORE1、3/TAIL0–2/LAST0–3，原L见各段。LAST3当前abs轻量identity：11073v2、11079v3改名、11083v4、11096v1，未见具名withdraw/correction，不把version/改名自动作重要修订，不读后版全文。作者本批完成，待root必要独立复核；未核实现/复现。

## [Chatting with Images for Introspective Visual Thinking](https://arxiv.org/html/2602.11073v1)

2+1+2=5，长期跨region接口差额深入。INITIAL L117–148：step为thought/query/region list，crop2×且cap原尺寸；初始各图独立，重读时joint patches+queryembedding，designated layers才跨图。LAST1 C438–472：frozen Qwen3Embedding.6B query，ViT32L1280/16heads，layers8/16 intra-image、17–32 inter-full，其余window。不是所有层dense joint、不是crop或成熟SFT/RL自身增量。feature提取跨region互动与语言侧latefusion确有接口差别，attention图仅diagnostic不是真实grounding。

CORE0 Table2 L215–244：sameSFT+400RL dynamic vsvanilla局部对照支持，73.4/67/40.7/49 vs73.3/65.7/40.3/47.4；完整1200不能和400直接归encoder。SFT VSI43.3低于QA-only46.9；SFT与answer-only监督/chain不同不能只说架构因果。SPAR6489/721、5epochs、同1600token训练、2–4images、移query/移multiimage对照支持窄跨view诊断，但单passlongvideo计算不可承受。RL G4/B96、round5/10、processedimages52，top-p.9/T.75；96H20训练27hSFT/138hRL不等推理硬件或总teacher数据成本。

LAST1 Table6 L390–396仅每round，完整round数不同；5.97/4.69约1.27而表写1.06，relative-latency隔离，不授1.06×或端到端更快。precision、evalbatch/concurrency/SLO、seedCI及真实grounding error ND。拟PRE MULTIMODAL-REPRESENTATION Ch23当前L687–707视觉记忆/主动回读后，缺query条件跨region feature互动vs独立encoder的具体设计分工；融两段：源region identity→局部/跨图interaction选择→新的features回语言，保留independent encoding与tool/raw回读；staticmultiviewablate与长视频/多轮/额外queryencoder/interaction成本反侧就近。不授visualattention真值或表6性能。root核必要Source/current owner后才申请Ch23窄锁。

## [In-the-Wild Model Organisms](https://arxiv.org/html/2602.11079v1)

2+2+2=6，实际安全data干预深入，保留原v1标题。CORE1 §3 L120–145/MORE1 L146–183：对同prompt的pre/post不同response，均teacher-force到initial SFT checkpoint取response-token mean activation差；训练chosen/rejected亦同坐标差，再cosine ranking。跨checkpoint生成的responses不是把两套hidden直接相减。Ward similarity matrix可提未知behavior cluster，但人为解读/过滤cos>.4、350train/test只是discovery，ranking correlation不是完整逐样本因果归因。

TAIL0 §6 L222–298：OLMo2-7B、378341DPO pairs从同SFT起改top3000/12k/30k并重训；random/LESS/toxicjudge同interventioncount对照支持有限data-set干预。在3000过滤probe5.13劣于LESS3.75/toxic3.48，30k2.86较优；switch30k1.66但GSM72.5→68.2、XSTest6.8→11.2，非无utility损失。120LMSys prompts×100responses，promptbootstrap95%CI不等跨训练seed，少量10prompt早checkpointproxy不替全评价。LAST2 A1/A3 L364–379：150 behavior-selectedprompts、layer16–26按steering效力选20，故heldout任务/选择偏差和layers/checkpoint身份要绑定。A8–9 L425–439 GPT5mini medium score>50，human500按judgeharm/clean各250分层，90.6%agreement不是自然流量全域真值。

Table1 H100等价12vs128小时与$2.5/hr估价、实际4090 36h不可混成所有pipeline10×；ranking不是重训/审计总成本。retrainepochs/batch/LR/precision/hardware及seed/完整预算ND，单model family/singlebehavior、需data与中间checkpoint明确限制。拟PRE TRAIN-DATA Ch27L280–298已有benign内容≠trainingeffect/projectionfilter，却缺**同initial坐标构造behavior与preferencepair双差→ranking只提案→等interventioncount重训验证**的retrospective接口。拟两段接filtereffect：共同坐标与pair身份、批数据干预而非单样本证明、filter/switch不同效用和成本；保留contentfilter/canary/原数据回退。不复制安全正文，不授cosine完整因果或所有DPO安全修复；待rootSource/owner PRE与锁。

## [Token-Efficient Change Detection in LLM APIs](https://arxiv.org/html/2602.11083v1)

2+1+2=5；拟采用受限monitor接口深入，不授普遍定理。CORE2 system/LAN L120–157、TAIL1 L207–280：singlefirsttoken、独立sampling/localdifferentiability、epsilon=s/sqrt(n)、非退化tie方向；T→0极限不等provider T=0 implementation。有限随机输入重复3次发现多token支持，reference采样，再比较empiricalsupport；理论uniform有限support才有所列错误界，不能授任意probability/model change检测。实际ROC用跨prompt TV连续分数而非纯binarysupport，不混两个实现结论。

LAST0 §5 L280–342：TinyChange9个.5–9B、finetune/prune/Gaussiannoise，init20kprompts、1000reference但每test用50，选5prompts×3检测；baselines搜索参数含T0、同50reference局部fair。$2.2/year AUC.9 vsMET$67/.88不是同quality所有30×，价估不等GPUwallclock。93selected/64models，18empty，其中16reasoninghidden输出无法廉价观察；T0有62%找到≥1BI，5BI监控仅54，低温选择tradeoff明确。23天实际24h采样、hourly费用是假设，不写真实hourlycampaign；8persistent变化只有1官方changelog直接佐证，跨provider另2是推测。unchangedoutputs不识别所有hiddenparameterchange，变token也不能唯一归weights（systemprompt、routing、batch/硬件变化均可能）。硬件/dtype/inferenceconcurrency/生产FPRcoverage ND。

拟PRE PLATFORM-MONITORING Ch67一般canary/版本漂移sensor已有，但缺**token-only条件下从固定输出转向边界支持集合的init/detect接口**。拟一两段于monitoring sensor论证：低T重复筛border→独立reference→TV/support只告警，不认证底层identity；有限support/nondegenerate/端点输出、T0特殊/hiddenreasoning与负载变化成本/回退显式version证据和常规canary。root核currentowner与必要原源才授Ch67窄锁；不写无限power/任意update一定检出。

## [Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away](https://arxiv.org/html/2602.11096v1)

2+2+2=6，安全干预变化深入；作者拟**争议/Books暂缓**，有限earlytiming实验可报告但不绕过中心enforces safetyconstraint主张。CORE3 L87–159：candidate-step guard normalized[-1,1]过tau0才接，失败加offline固定“Wait,think safely”重采；从500validation四bench由GPT4造1–5token候选并按安全/KL筛，实际inference没有每步搜全candidate。BoN≤20只表明有限samplecoverage，不证明safecontinuationmass真零或所有安全仍在模型内。

中心约束冲突：Eq2/6概率应≥rho∈(0,1)，L139却用estimated probability≥tau=0，任何经验非负概率自动通过；不能据该displayformula证明概率安全门实现。Eq10逐stepKL和缺steered-history expectation/统一上界，不能由smallm直接推出全轨迹KL小。重开仅需明确rho/score阈值不同单位与actual selection/accept代码或修正算法、正确chain-rule条件，不读所有攻击附件。B/C TAIL2 L299–310：LlamaGuard/QwenGuard仅sensor，reward>0仍约90%GPT4safe不是充分安全保证。

MORE3 L169–205：六MLRM、四jailbreak、eachquery3独立输出anyharm算成功，GPT4评trace+answer、LlamaGuard3为过程guard；early m≤3有限对照反侧支持时机值得诊断，不授所有任务/攻击。MathVista avg63.46<63.51原模型，Table1按100JailbreakV prompts平均时间、单A6000/Python3.12.8/Transformers4.53/PyTorch2.7.1；batch/dtype/tokenlimits/concurrency/tailSLO/repeatedseedCI ND，monitor/rejectedsample/offlineGT搜索均有成本。不照录保证capability无损。既有独立guard/policy不能由这个recipe替代，必要中心规范未一致前不写Ch72，不以Only掩盖争议。

本批四项必要支持/直接反侧与处置已获root独立复核；11096中心暂缓明确，不进入安全保证或Books。11073实际Ch23正文709/711、11079实际Ch27正文300/302、11083实际Ch67正文32/34，三处正文/邻接/末注已经root实际非作者POST通过，窄锁释放。作者累计108/112=102必要+6低分，余4普通；35实际Books POST，不授日级。
