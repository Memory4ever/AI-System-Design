# 2602.09486v1 必要审阅（作者准备，Source待独立）

[CoCoA](https://arxiv.org/html/2602.09486v1)，root AB/date通过；2+1+2=5。§3 L109–161：候选span meanpoolmiddlehidden，consecutive或finalreference cosdist量化变化，logprob−αMLDS或logprob(1+αMLDS)按selfinformation加强低prob惩罚；只在nexttoken概率候选>γmax的divergencepoint展开variablelengthspan，其余greedy。省掉Diver teacherforcing/PMI但仍候选分支生成+跨layer读hidden，训练free不等于计算free。内部一致性是候选rerank proxy，不是factualchecker；稳定自信错误会漏，高surprise正确novelspan可能受罚。

§4 L164–184：TruthfulQA817、NQ/NQswap1000各、summaries1000各、MBPP427、7/8/14/32B多模型；Gemini2.5Pro truth/info/FActScore判，不授外部独立事实gold。H200单GPU/AppA387–389，HuggingFace与baseline官方/customDiver混实现，γ.3。Runtime/precision/batch/concurrency/SLO/repeatsCI ND，不能说较searchbaseline提速或production吞吐。

§5.1–5.3 L258–313/T5–7：α0 spansearch本身truth涨66→76.25且rejection13.5→23.26，故不是所有gain可归midlayersignal；同searchα1 T×I再涨但未独立testsplit调参。fMLDS gating真率涨而T×I49.19→48.14，α大拒答变多/信息降，middle-range是localarchitecture tuning，不授普遍semantictruth机制。分别给all vs nonrejectedpopulation避免selective metric混淆；code单benchmarkpass1非长程execution保证。Source后actualowner拟MODEL-TRANSFORMER-LAYER推理反馈/proxy与生成分支，未授写Books，必要方法/反侧足停。
