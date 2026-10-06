# Jan02 首批准入理由（未冻结）
本窗2026-01-01T09:00:00+08:00～2026-01-02T09:00:00+08:00。63份精确v1题摘见ABSTRACTS_1～4。这里只判断具体潜在增量；未授日期、Evidence或Books通过。已有来源记录的279个去重ID不是候选池。Dec29T19Z缺段已作有限补检，另见GAP_ADMISSION.md；分母尚未冻结。初63中八个贡献/范围/撤回排除，不含首公开待核项。

| ID | 题摘贡献判断及改变的选择 | 暂定处置 |
| --- | --- | --- |
| 2512.25070 | 新闻实时检索易未来泄漏→offline corpus合成forecast并比较reward/calibration→重新判断预测校准能否迁移普通评价；不以预测赛分数准入 | 潜在 |
| 2512.25066 | masked inpainting缺完整身份条件→自举对齐视频对+按timestep分离编辑目标→考虑由条件完整性减少多模态编辑冲突 | 潜在 |
| 2512.25063 | 一个参数实例难兼顾探索多样性→normalization随机posterior proxy且整序列冻结noise→考虑行为多样性与token一致性分开采样 | 潜在 |
| 2512.25026 | token共现难维护entity/event关系→保留可反传的sentence memory与token共参数→考虑语义state压缩如何分配表示/训练梯度 | 潜在 |
| 2512.25023 | binary preference丢强度且proxy有混杂→strata内相对强度ranking→考虑reward识别ordinal/cardinal效用的监督方式 | 潜在 |
| 2512.25014 | 并行DLM优势缺计算模型→CoT模拟parallel sampling及revision/remask空间/表达分离→修改并行性与中间state可改写的理论边界 | 潜在 |
| 2512.24991 | fine-tune标注量靠试错→low-confidence gradient cosine预测目标样本量→考虑dataset预算估计的低成本诊断 | 潜在 |
| 2512.24986 | LLM生成3DGS物理动画代码解决创作接口，未改变foundation训练/表示或VLA动作闭环；模拟器无关不能类比为world-model知识 | 贡献前关闭 |
| 2512.24969 | 长上下文数据收益是否来自远距离依赖不清→entropy/correlation与训练期的长短context动力学→判断长依赖学习是否仅靠token窗口 | 潜在 |
| 2512.24957 | core §2.5.3显示静态teacher难度不等当前policy可学性→K=8 policy reward均值/方差探测、variance×mean选择并分配oracle预算→核验curation的policy-relative成立条件；方法明确但评价未分离其因果收益 | core后具体准入 |
| 2512.24940 | 部署后的用户精选data被当普通SFT→iterative deployment构成隐式reward的outerRL→重新审查数据反馈loop的能力/安全优化目标 | 潜在 |
| 2512.24867 | 固定题目污染且单知识点→statement动态组合+refresh ranking稳定性→改变evaluation unit及污染控制协议；不接受组合空间即防泄漏 | 潜在 |
| 2512.24856 | 定义/既有工作回顾/未来agenda未给改变执行或可靠性判断的新机制证据 | 贡献前关闭 |
| 2512.24851 | 通用CoT/reflection通常正面→zero-shot VLN中性能下降→审查embodied navigation reasoning长度与空间state失效关系 | 潜在反证 |
| 2512.24842 | 单语言intervention不足→necessity/sufficiency需跨predicate-preserving变体invariance→考虑interpretability验收的跨环境因果约束；仅协议，不冒充实验已证 | 潜在 |
| 2512.24776 | 模型选择只看accuracy→compute-matched前沿与推理饱和证据→考虑test-time compute选择的model-specific边界 | 潜在 |
| 2512.24766 | video imagined motion不能直接actuate→3D object flow将对象state与embodiment分开并track→考虑generation-to-control接口可移植性与物理闭环 | 潜在 |
| 2512.24713 | 官方v2于2026-01-20撤回：ML pipeline与独立FPGA accelerator重大不一致，非coherent integrated methodology；不采用v1宣传/benchmark，不评分不入Books | 官方撤回排除 |
| 2512.24695 | optimizer/continuummemory/self-modification改变learning粒度；但Google已有Nov公开信号，核首公开而非自动当新论文 | 窗外首公开待核 |
| 2512.24693 | 末turn偏好不监督历史interaction→合成跨多turn对照→考虑reward model对多轮状态变化的归因监督 | 潜在 |
| 2512.24661 | 自评成功概率被当agent合理决策→多步推进反而过度自信、经验只能部分修复→改变自信概率与实际delegation风险的关系 | 潜在反证 |
| 2512.24653 | 新增更大数据/tactile/mobile与高层planner/低层executor组合，题摘没有给出新控制机制或具体generalization/observability证据；不得用数据量建立准入 | 贡献前关闭 |
| 2512.24639 | raster串行视觉AR→radial同ringparallel加nested correction→考虑factorization局部依赖与commit修正边界 | 潜在 |
| 2512.24618 | small agent靠distillation→从头commonsense→STEM→agent midtraining curriculum与STEM词表→核验容量/数据分配边界，不以榜单准入 | 潜在 |
| 2512.24617 | 均匀token算力浪费→学习variableconcept boundary+compression-aware scaling/decoupled muP→考虑latent粒度与稳定扩规模的共同预算 | 潜在 |
| 2512.24615 | 实际§2.3/2.4/3.4的Training-Free GRPO、AgentLightning/VeRL/Ray集成重呈现此前公开功能；turn-adv correction未给可验新公式/条件，不能把模块命名或128GPU规模当新增机制 | 贡献前关闭；root完整题摘/core关闭校准通过，非由repo日期倒推论文首公开 |
| 2512.24613 | generation/verification/arbitration角色+retrieval/PPO组合只报效果，未具体揭示新协作机制、failure path或收益成立条件 | 贡献前关闭 |
| 2512.24609 | CTDE/GRPO加质量速度coordination reward组合未指出信息边界/credit机制的新增，单agent速度对照不足以准入 | 贡献前关闭 |
| 2512.24603 | 各LoRA独立空间参数重复→共享up/down bases且diversity正则→考虑低rank模块容量/冗余/参数预算取舍 | 潜在 |
| 2512.24601 | 长prompt被当token context且summary丢证据→externalenvironment+programmatic读取/递归子调用→改context容量与LLM调用边界 | 潜在 |
| 2512.24587 | 单风险threshold难同时受控→priority-aware dynamicprogramming+exchangeability simultaneousrisk→考虑多约束过滤保证的统计前提 | 潜在 |
| 2512.24580 | generic robust Bayesian RL/DDC应用，无与foundation模型学习/运行机制的直接新联系；金融对冲域指标不重新引入 | 范围关闭 |
| 2512.24574 | 延长CoT导致under/overthinking→calibrated cognitiveheads steeringvectors可推理时转向→考虑tokenbudget以行为state而非单长度控制 | 潜在 |
| 2512.24565 | externaltool依赖混入benchmark→simulatedrealMCP sandbox+distractortools分离选择/执行测量→核是否揭示新eval可靠性边界；不以MCP名称准入 | 潜在 |
| 2512.24562 | 单QA多信号融合新增局部detector选择，但未改变跨任务真伪核验机制；不把confidence当事实verifier | 候选1+1+2=4关闭；身份/落窗原值已核，root关闭校准通过 |
| 2512.24560 | 程序整体正确率难定点监督→minimalintentpatch与arbitraryspan probing→考虑局部错误概率及human review粒度 | 潜在 |
| 2512.24556 | safety English跨语言平移→language×tense factor反例→考虑安全invariance而不是语言或时态单因素；作者因果归因须深入核 | 潜在安全反证 |
| 2512.24551 | pairwise video preference/duplicatedreference昂贵→groupwisePlackettLuce+LoRAswitchreference→考虑group reward与reference内存边界，非物理领域应用 | 潜在 |
| 2512.24545 | binaryfactor共享magnitude饱和→sharedsigncarrier+rank-l envelope→考虑低bit budget分配给magnitude表达而非bitwidth | 潜在 |
| 2512.24532 | atomictransform与多步planning混训不稳→冻结basephysics+GRPOLoRA学习composition→核验基本能力/策略分离的局部成立条件 | 潜在 |
| 2512.24503 | 同hyperparameter被当data公平对照→data-dependentoptimal与reducedLRordering→修改proxydata recipe评价协议 | 潜在设计反证 |
| 2512.24449 | KV quantization只bit budget→LLM-awarelossycompression+decompress/MV co-design→考虑quality-matchedmemory与端到端解码成本 | 潜在 |
| 2512.24438 | representation compositionality缺视觉primitive→wavelet decomposition检验approxlatentcomposition→核验Transformer表示解释的输入基元条件 | 潜在 |
| 2512.24426 | VLA trace描述不主动改plan→metaaction-conditionedcounterfactual+rollout-filter-label→考虑执行前自纠错与adaptive compute边界 | 潜在 |
| 2512.24407 | IRL/DDC semiparametricrewardfunctional统计估计未与foundation能力形成/系统选择建立新关系 | 范围关闭 |
| 2512.25059 | NICfailure导致整jobrollback→multiNIC migration/load redistribution/resilientcollective→考虑training/serving恢复粒度与低overhead条件 | 潜在 |
| 2512.24873 | tokencredit跨toolinteraction不匹配→semanticinteractionchunk IPA+ALE rolloutmanager→考虑agentRL creditunit与环境执行隔离 | 潜在 |
| 2512.24724 | diffusionmodelcapacity全程均匀→early/latebig-middle-small sampling+velocitydivergenceproxy→考虑stepbudget的capacity-sensitivity | 潜在 |
| 2512.24637 | demandpaging reactivefaults导致HBMoversubscription慢→kernellaunch预测working-set并预迁移/co-schedule→改memory迁移时机与GPUcontext调度 | 潜在 |
| 2512.24511 | checkpoint liburing大吞吐默认适用tensor小buffer→alignment/coalescing/filesystem-awareaggregation→改checkpoint IO粒度与backendbenchmark可比条件 | 潜在 |
| 2512.24461 | 完整AB及决定性§5.1–5.3：text hypothesis经lexical/LLM投影、模拟IG与uniform action instance仍是既有POMDP/IG组合，未建立观测likelihood/新成立条件；不由缺完美实验或Books覆盖关闭 | 贡献前关闭；root已实际核决定性method |
| 2512.25075 | 摄像机pose与时间运动耦合→timeembedding+temporalwarpingpairedtraining→考虑多模态生成时空control的解耦条件 | 潜在 |
| 2512.25072 | 完整AB及IV-A–D：multiple-choice WTA、detached MSE score是既有多proposal/scoring组合，未新增机制或特有成立条件；不是humanoid/小样本自动排除 | 贡献前关闭；root已实际核决定性method |
| 2512.25034 | 同Li/Kumar/Pathak出版方ICLR2025原稿完整AB及Gaussian条件支持2025已公开上界；本窗仅上传不改归属，不以索引相对age补造首公开时间 | 前公开关闭；root实际出版方身份/原文核通过 |
| 2512.24952 | 单lastframe正确掩盖processwrong→POC@r过程/结果分账→改变generativevideoreasoning评价有效性 | 潜在设计反证 |
| 2512.24927 | firstorder天然慢→evaluationplacement改变主error符号→改NFE固定下solverorder与evaluation位置的选择 | 潜在设计反证 |
| 2512.24731 | visual/text不平衡且eventcontrol无identity→when/what/how symbolicevent+hierarchicalgeneration→考虑多模态控制粒度与调度分层 | 潜在 |
| 2512.24673 | actionchunk异步到达jitter/stall→polynomialsmooth+alignposition/velocity/acceleration→考虑chunkcommit的continuity约束 | 潜在 |
| 2512.24497 | core Appendix S2.2–S2.3核到二步rollout错target及预测/真值context混合：future图像相似不足证明planning好，detach策略与训练测试context改变planner表现→修正latent-WM选objective/rollout协议 | core后设计反证准入 |
| 2512.24428 | core III.B/IV.B：去texture使render-refine不兼容，raw-depth噪声与monocular无metric-scale分别失效，DAv2+sensor median尺度对齐/几何registration形成可用性条件；不是借FlashVDM加速作新增 | core后局部准入 |
| 2512.25065 | 手工systemsheuristic探索受限→constrainedpolicy/mechanisminterface+LLMsearch→考虑自动可执行policy的验证与taskbounded搜索 | 潜在 |
| 2512.24880 | unconstrainedHC破坏mean/norm propagation且访存高→doubly stochastic residualmixing+infra co-design→改多stream容量与scale稳定/内存代价耦合 | 已root贡献校准 |
| 2512.24504 | symbolicmap探索次数被当reasoning提升→structuredmemory与exploration/reasoning的componentseparation→考虑获得经验与可用state表示不能混为一谈 | 潜在 |
