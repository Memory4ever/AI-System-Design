# 必要证据与owner差额：SPF / SIN-Bench / augmented ICL

exact-v1 HTML；未运行实现或复现实验。root已准入，以下必要原文/owner准备待非作者核，不自行授Books或日级Gate。

## SPF — 2601.10141v1

[原文](https://arxiv.org/html/2601.10141v1)，primary缓存实际§3.1–3.3 L395–453、§4.1–4.3 L453–668、§5 setup/主表/robustness/ablation L672–974及1070–1137、AppendixA.3 L1382–1404、B.1/B.2 L1419–1498。拟2+2+3=7，安全更新几何缺口深入；仅计单拒绝sample估计的block左低秩子空间与conflict触发投影，不重复计算成熟gradient surgery原理。

Algo1：每步一条safety refusal样本与batch utility梯度；内积负时，各参数matrix取safety梯度top-k left singular vectors U，Gutility→(I-UUᵀ)Gutility，否则原utility。不是参数mask/推理activation cap；低秩取前10–20仅受测选择，不能据此认定安全只有固定十维。§4.1 spectrum及single/batch overlap >.8是有限三个7/8B模型/所采样梯度的诊断，不认证任意安全prompt人口或唯一causal direction。

理论只作限制，不采always-aligned：Lemma norm假设移除方向各向同性且独立utility，与作者实际冲突选择不同；§4.3 convergence用每步SGD投影，实训§5.1是AdamW(.5/.999)。A.3明确用ideal P∇Ls=0，而top-k残差、单样本与总体Ls失配未被这条恒等式处理；实际AdamW moments/decay也不等于所投影gradient最终delta。因此不授任意有限步safety loss bound/zero safety drift，发布行为需另测。

受测三模型Llama3.1-8B/Mistral7Bv0.3/Qwen2.5-7B，Harm100/Math7473/SQL77577/Samsum14732/Toxic5082；4A80080GB，5epoch LR2e-5 B64。ASR由HEx-PHI+HarmBench，HS GPT4 judge，utility task/MMLU/Pro；Table5 Harm后SPF ASR .019/.240/.124非全零，DRA .176/.164/.106、AutoDAN-Turbo仍非零。Table8约1.61GPUh vsSFT1.26，只一个Math/Harm配置成本；k升大损utility且SVD成本升，不采negligible/全部无损；没有重复/CI或全面benign overrefusal分层披露。category-wise方向对未见类别迁移较差是直接反侧。

日期原SubmittedJan15T07:33:13Z、UpdatedJan16T01:26:40Z、created02:48:11Z/registered02:48:12Z，正常公告/无已知先行正文条件BJT[Jan16 09:00,10:48:13)。

Owner TRAIN-SFT Ch29：实际134–152只有lossmask/backwardrouting；807–822已讲敏感方向保护/最终AdamW delta非zero-gradient，并非每步single-refusal conflict→blockleftSVD projection。拟插在rotation-preserving分支后与dynamicmask之前两短段（现810后），明确只是gradient proposal，需要实际delta与外部behavior gate；成本/理论限制相邻。Ch29首尾及Ch28/30交接已实际核，不将安全结论复写Ch72。

## SIN-Bench — 2601.10108v1

[原文](https://arxiv.org/html/2601.10108v1)，缓存实际§3/4.1–4.4 L148–300、§5/Limitations469–549、A jury/manual/scale849–896、B897–914、D1165–1226。拟2+2+2=6；确切评价gap深入，科学文献是通用MM context-use substrate，不是AI for Science成果。

文档text/figure按首次citation interleave，paired visual anchor+text为evidence unit；M是Qwen3-8B semantic matching，R阈值2/3后的P/R/F1，L是matched anchors Kendall–Tau order，不是逻辑蕴含证明或内部causal CoT。答分单独保留，overall是若干metric arithmetic mean，缺anchor令evidence项0、AnsAcc仍可能>0，所以所谓No Evidence No Score不能说总分严格零或已建立生产evidence gate。重复anchor/alternate-valid chain的exactcode去重/多reference未核，不采用精确correctness证书。

4000documents→~3200raw→490human-reviewed（159Find/158QA/89Summary/84Verify），三模型jury≥4/majority+24gradstudent，2–3人/例；reference本身受author synthesis/audit切片影响，不是全文groundtruth。8MLLM一次T0，Qwen3-8B judge vs专家多数平均Pearson .825不是逐题正确概率。主结果GPT5 AnsAcc .767但overall较低，hard-negative Verify从easy1.0到GPT5.208/Qwen.044/Gemini.25支持当前near-miss难度敏感，不采near-chance形容（非均匀二分类零假设已经核）或唯一parametric guessing原因。Gemini同模型interleave vs separated +.102QA/.129summary及显式evidence .694→.726只是局部single-run，输入/格式、extra outputbudget/judge都可能贡献，不能全部归因内部contextfaithfulness。最长input/视觉数量、format failure、synthesis/audit/judge成本均保留，hardware/batch/SLO Not Disclosed。

日期SubmittedJan15T06:25:25Z、UpdatedJan16T01:23:39Z、created02:47:23Z/registered02:47:24Z；条件BJT[Jan16 09:00,10:47:25)。

Owner PLATFORM-EVALUATION-SYSTEM Ch66：实际891–930有trace因果分离、context三条件与FACTS四分支；950–973已有document navigation与effort，但缺**同请求answer correctness/可恢复visual-text evidence分账、near-miss premise干扰及matched-order只能proxy**。拟在MADQA段后两短段、edit/RAG调解段之前（现970前），不重述普通多轴原理。Ch66/65/67上下文仍有效复用，待窄锁。

## Unlabeled augmented ICL — 2601.10058v1

[原文](https://arxiv.org/html/2601.10058v1)，primary130k有效HTML，实际§3.1/3.2 L95–116、§4 L146–189、§5 L190–241、§6 L242–255、A.2初始/局部Jacobian假设745–794、B决定性证明1066–1113。拟2+2+3=7，受限构造/训练接口；不借理论标签或M更大默认普遍贡献。

uniform C类共享isotropic Gaussian，同分布labeled N/unlabeled M；四层encoder transformer，softmax E-step/posterior，两个linear-attention梯度式M-step，再ReLU首步labeledmean初始化，reasoning块追加classmean不是语言CoT。只有第一层distribution-dependent，后三层手构造固定，teacherforcing参考EM轨迹的posterior CE。C=d=3，N5/M1,10,20，T5、dp16、64tasks/batch、15000GD，H10080GB约5h，5runs/100test±2std支持受测joint-inference效果，不证明大语言模型自发EM或无限增加无标签普遍更好。

**中心training定理争议已送root**：§5 Assumption1 W0条目iid Gaussian，B L1079/1083改为wI；B L1075把E[initialmean]=μ用于所有reference轨迹μ等式，非有限样本成立；B1094–1097从exchangeability宣称E[qqᵀ]=11ᵀ/C²，非退化posterior的对角应另有Var(q_i)>0，类别交换对称不足。故不采用Theorem5.1已验证全matrix contraction或learnable headline。§4机制可保有限构造、§6有限实测，具体Books差额/是否中心暂缓待root独立裁定，不扩全证明。

日期SubmittedJan15T04:23:32Z、UpdatedJan16T01:20:08Z、created/registered02:46:10Z；条件BJT[Jan16 09:00,10:46:11)。

Owner候选 MODEL-SELF-ATTENTION Ch14：actual212–226已讲存在性featurizer/least-squares与不授训练保证，但未承载labeledseed/unlabeledjointposterior→iterativemean mechanism及teacherforcing冻结3层条件。若只report争议，可保有界机制与精确重开：作者修正initialization/finite-reference/secondmoment推导或提供证明适用的额外假设，不能等价把当前数值实验授全定理。未授Ch14锁，不写Books。
