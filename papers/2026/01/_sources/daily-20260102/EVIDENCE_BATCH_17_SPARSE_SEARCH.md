# Jan02 两个既准入项：稀疏预测与确定性探索

24086/24156完整v1题摘root已有准入校准，作者本轮仅读necessary method、实验及直接反侧。均拟2+2+2=6，不重复按摘要headline准入。DATACITE_RECOVERED_4 actual created分别Jan1T03:03:33Z/03:05:15Z；holiday/noadvanceID推定区间下界Jan1T01Z，上界分别created+1秒，完全本窗。后续Rain v2晚Apr不当本窗事件；当前原说明未见撤回/纠错标记，Graph原v1自身已披露reset bug，必须保留。

## [RainFusion2.0](https://arxiv.org/html/2512.24086v1)

Actual §3.1–3.4/Eq5–8与§4/Table1。mean block Q/K dot product用于mask预测，随后selected blocks才按FlashAttention online softmax做完整QK/PV，不是mean输出代替完整attention，也不保证排序等价。窗口重排意图使3D近邻同块；§3.3具体window实现原称“details will be released later”，不能补造window shape、layout kernel或实现已核。Eq8 TopN dim=0与文字per-Q block语义不明，保原身份，不授精确轴规则。

first-frame sink同时让first-frame queries读全部keys、其他queries保first-frame keys。原混合text/video还把first-frame放到text邻接，意味着permutation必须保位置/文本身份，不只是无条件token sort。必要数学对象：`qhat_i=mean(Q_i); khat_j=mean(K_j); Shat_ij=qhat_i khat_j^T`。block mean已由§2引用既有SparseAttention，新增对象只窗口邻接/强制first-frame角色与受限NPU执行。

Wan2.2/HunyuanVideo1.5有限480p/720p，Qwenimageedit1024²；NPU型号/precision/batch/concurrency/frame count/step budget/SLO Not Disclosed，不能推跨硬件通用性。Table1不是质量无损：consistency等有下降，增加sparsity与3D order不全指标改善；chosen artifact例子不授总体差异率。比较仅full/native可运行基线，GPU系方法NPU不兼容而未跑，不授它们技术优劣。预测/permute/buffer实际费用未单独隔离，保端到端报告与cost校准。

Books终态：root实际必要source与Ch14:284–300现support selection/normalization、base-rescue/requiredmask union合同对读通过，具体已有覆盖。局部首帧双角色/3D布局recipe留报告，不构成必须新增Ch24的长期缺口；不是声称现章含本算法。6分不变、标准完成，不写hardware/quality guarantee，未运行实现。

## [Graph-Based Exploration for ARC-AGI-3 Interactive Reasoning Tasks](https://arxiv.org/html/2512.24156v1)

Actual Benchmark/Observation、Methods/Alg1、Results/Discussion及B两表。connected-component action候选与priority、masked-image hash、visited action与frontier shortest-path共同构成training-free controller。action因reset回起点仍须标tested，否则又会成为nearest frontier并重复reset；作者正式12levels与重跑median16不是同一个结果，bug说明不能以更高重跑数覆盖。相同masked frame hash不证完整Markov state：status bar被mask，倒计时/阶段或部分可见条件仍可能决定转移；原Discussion只在deterministic fully-observable前提提出适用范围，不能推任意真实环境。

原比较将其他方法统一cap4000 interactions，确有action预算控制；但LLM+DSL为官方一次aggregate，其他median5 runs，frame preprocessing/候选action support、reset handling与内部预算不独立控制。8h/10step-per-second上限及full-run96000和4000图分开；单步LLM call限制实际interaction，未重跑成本说明不是matched调用/墙钟/训练总量。更多组件亦有退步。hardware/precision/token/runtime预算不披露。不从这个局部反证断言LLM不会推理或graph通用优越。

Books标准仅报告终态已root实际必要source及处置通过：这提供具体interactive case反证而非新通用graph理论，现Ch79 hash/partial-state identity、canonical/fulltrace承载长期边界，不能把普通reset漏标bug自动升级新机制。本文仍未隔离同state/action preprocessing、bug-fixed版本与重复机会下的LLM额外增益，因此不据它改写“何时采用模型规划”的长期选择或追加ARC recipe；保有限反证/bug证据，不称现章已包含算法/成绩。6分不变、标准完成，未运行实现。
