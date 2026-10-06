# 必要证据与owner：UMI-FT / VERHallu

exact-v1 HTML；未核实现或复现实验，root已完整题摘准入，必要原文与具体owner待非作者核。

## UMI-FT — 2601.09988v1

[原文](https://arxiv.org/html/2601.09988v1)，primary实际III-B/C L109–116、IV-A/B117–155、V任务/对照175–315、VI限制。2+2+2=6，力/接触控制接口gap深入，不把既有ACP/传感器名称本身算新机制。

手持与robot保留同finger CoinFT+iPhone结构，in-situ MLP标定非线性capacitance→6Dwrench；fingerframe adjoint变到toolframe后组合供wrist6D admittance，grasp轴两finger平均单独feedback。慢learned policy输出reference/virtualpose、stiffnessscalar、gripperwidth和graspforce共21D，stiffness/virtualtarget标签由demonstration后处理，不是裸pose监督；runtime重构matrix交wristcontroller，width/force交graspcontroller。新增通用动作接口是**接触目标与控制参数从视觉轨迹拆出，并绑定两独立快速feedback环**；不是LLM直接设effect或认证force safety。

RGB224² CLIPViTB32，两历史RGB/depth、32步wrench causalCNN/transformer融合/diffusionpolicy；UR5e/WSG50，wrist500Hz/gripper30Hz，sensor360Hz，policyHz/GPU/precision/训练总时长/端到端latency Not Disclosed。internet timestamp/postprocess同步不证明无latency。whiteboard275demos/25trials、zucchini各condition5rollouts、bulb200demos/20rollouts；pose-only/pose+force/CM对照支持局部分工，不授baseline参数/总训练成本完全matched。zucchini柔性本体让wristcompliance额外效益变小；630多scene vsinlab训练同时变data数量/多样性，20/20不能只归force机制或普遍OOD。bulb人为弹簧30→15N，20N新condition仅4/5，不是原30N能力。25/50N grasp与20N其他方向是作者safetythreshold非校准物理保证；CoinFT拉力delamination、tetheredUSB、out-ofcalibration仍限制接触。

Ch26 MULTIMODAL-EMBODIED-VLA实际710–718有慢policy+fastlearnedreactiveexpert的chunk修正，不承载**示教中finger internalgrasp/externalwrist两对象、21Dcompliance目标与model-based双环**；拟contactloop段后两短段，保留policyproposal/controllercommit和threshold成本。首尾及Ch25邻接已读，Ch27不承接controller语义。SubmittedJan15 02:00:03Z/UpdatedJan16 01:13:47Z、created02:44:16Z/registered02:44:17Z；条件BJT[Jan16 09:00,10:44:18)。

## VERHallu — 2601.10010v1

[原文](https://arxiv.org/html/2601.10010v1)，primary实际III-A–D L139–167、IV-A/B167–188、V/VI setup363–390、VI-B625–634、VI-C757–767/825–831。2+2+2=6，event存在与directedrelation/反直觉prior切片具体gap深入，不把增列任务本身算贡献。

MrBean counterintuitiveclips减轻常识shortcut但不是消除所有prior；QA distractor分别从仅question或video+question构造，RC分别方向+None，CFQA把同问题放到目标event不存在video并含unknownanswers。574clips/7676samples=967QA/967CFQA/5742RC，annotator2+第三裁决/无共识弃样；causal None1238/1511、temporal1349/2683、subevent1032/1548严重不均。此时accuracy高可能只预测None，F1/方向与eventpresence不能互代；不采用无条件“差于random”或所有任务chance比率。MVBench排序不转移至relation任务支持测量差异，不唯一证明训练架构或因果attention缺失。TAM只是tokenactivation可视化，不是模型内部cause证据；MrBean固定语料/构题/有无输入差异限制外推。

KFP在选定中层按topk视觉attention给邻frameGaussianweight并混回originalhidden，是inferenceproposal；LLaVA局部改进而QwenCFQA下降6pp，提升eventattention反而可放大无关视觉线索。因此不能把attention增强认证关系正确，也不称negligible总成本（原 FPS 不含统一GPU/productionSLO）。video模型帧预算不同，GPT4o/Gemini3pro因成本每tasktype抽200而非全population，不以榜差归规模/训练机制；safety不来自视频benchmark。需分别验event存在、relation方向、None/Unknown及counterintuitive distractor，证据不够回原video/人审，保留便宜entity任务而非取消它。

Ch66 PLATFORM-EVALUATION-SYSTEM当前视频601–635含ViSIL保留vs忠实、inputnecessity、temporalshortcut及timestamp事实；未承载**event可定位≠事件间directedrelation可靠、反事实缺失event与Noneclassimbalance**。拟video自然claim验证段后两短段，KFP只作反侧不将内部activation intervention机制在Evaluation完整重述。首尾与65/67交接已读。SubmittedJan15 02:40:41Z/UpdatedJan16 01:15:18Z、created02:44:56Z/registered02:44:57Z；条件BJT[Jan16 09:00,10:44:58)。
