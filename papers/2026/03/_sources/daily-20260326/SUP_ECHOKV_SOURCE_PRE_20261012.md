# EchoKV 必要Source/sole Ch45差额与两PRE

2026-10-12，仅[2603.22910v1](https://arxiv.org/html/2603.22910v1)。原2+2+3=7与25日级门不改。实际§3.1–3.3/Eq1–7、§4.1–4.2/T1–2、§5.1–5.5/T3–4、B/T5和C/T6必要参数/失败条件；支持与关键反证足止，未核代码/全部图/复现或无关附录。

## 实际机制与边界

固定LM，group首层保完整global，每层保local连续首部分pre-RoPE K/原V，用每token concat线性预测被丢部分，再concat供该层attention。不是generic SVD/basis低秩codec、tokeneviction或直接读取前层代本层；每层learned predictor需checkpoint/layout/group/mask身份。B原0.5 S2/currentlocal0全由global预测，0.7保384维(3head)，0.3S4保64维(halfhead)，**正文m-head公式不能直接覆盖partial-feature**，须明记保留维度/位置而非任意完整head数量。4sink与recent128fullprecision另占保护预算。

§3.3先KV-MSE，再完整原/重建attention-output MSE，目标后者可绕QKfullscore物化但不是未来query/多轮token exactness证明。训练T6 AdamWlr5e-4coswarmup0B1，stage600+1000steps，LongAlpaca；33.6Mratio.5/0.3为50.2M（不照录“<50M所有配置”），A100论文训练hour粗述/T3当前12.5+14.5min单结果，不授全GPU/数据成本固定。混合用ThinK压K/EchoV，因为只预测K更退，作者rank与similarity解释仍假设，Hybrid不总胜（RULER.3 Echo60.30>Hybrid58.53）。

Llama3.1-8B/Mistral7Bv.3 LongBench maxmodelcontext/RULER32K；ratiocompressed/full不是“省ratio”；T1.7 LlamaEcho49.08<ThinK49.86，T2Llama.5 Echo83.52<Full87.63/Mistral69.13<82.74且MK3等明显退，“near lossless/allsettings superiority”不采用。T4captionratio.5但§5.5说.75，人口身份未闭，不合并“combined alwaysbetter”：localPR98.5>combined94.5、Qasp46.45→combined46.48是后者微改善但其他Nrtv31.88>31.60，已具体有反退。四trainingdata平均相近不证明全分布universality/statisticalequivalence。

§5.4A100SXM4-80GB/B8，短text可保FullKV、压力时drop+prediction，长36K可运行不是tailSLO。Precision、outputlength、并发admission/SLO、真实所有编解码/predictor临时materialization峰值未披露。discard后standard参数仍可用，只证明算子/参数兼容，**不证明已丢历史重新成为原FullKV**；预测值与受其影响的hidden/token无法由切回自动还原，exact回退需保原KV或按原token/checkpoint重算，这是根据有损状态接口的本项目推断，不声称论文已实现恢复/双向所有模式。训练/保护cache/predictor驻留/每步重建/峰值与转换都计账；不通过qualityguard不承诺精确安全。

## actual owner/邻接及差额

actual Ch45完整565–629的crosslayervalue等价对齐vs有损平均、trainedshared架构与randomdepth、sharedbasis/residual→promptheadmode guard以及residualstream重执行projection；648–711完整exactmain/residual/fastweight/TopKcompletion/CompKV/token×feature链已读，前后44Decode/46Batching开篇亦读。这些实际正文保存层/feature近似、所有权/回退，却没有“固定LM首层完整global+本层局部feature直接预测缺失KV、再以attention-output恢复训练”的新读取接口，普通跨层basis不等linearconditional预测；也需区别standard算子可切与被丢历史exact恢复。sole INFER-KV-CACHE Ch45，不重复Architecture/Quantization/Servingowner。

拟当前`因此，对既有缓存的跨层压缩还可以沿两条可共存的分支演进：`之前（trained randomdepth最后完整段之后）插两段；保后basis/residual分支与residualstream重投影，原文不移。未独核/未root锁/未写/无POST。

## 两逐字PRE

对不改变原语言模型参数的缓存，也可保留一部分实际状态，再学习如何补出其余部分。一个受限分支把若干层分组，首层完整 KV 作为共同输入，后续层保留连续的局部特征；按 token 拼接这两份信息，用本层线性预测器重建缺失 K/V，再交给原 attention 消费。它不同于直接共用前层 KV 或保存低秩 basis：预测器属于 checkpoint、分组和保留坐标绑定的额外 artifact，Key 的 RoPE 阶段与保护窗口也须一致。训练先拟合缺失 KV，再匹配使用原 KV 与重建 KV 的 attention 输出；当前 query 的输出接近仍不认证后续生成无误，K 与 V 的可预测性也应分别验收。<!-- source-family:SF-2026-ARXIV-2603-22910 -->

原参数不变可以保留标准 attention 路径，却不能让已经丢掉的历史自动恢复精确值。压力解除后切回标准算子，仍须分清新状态与旧近似历史；需要 exact 回退时，应保留原 KV 或按原 token 和模型重算，不能用预测残差自签恢复。首层完整状态、近期保护区、预测器驻留与临时重建都占预算，数据生产和两阶段训练也计费。局部长任务仍有退步，固定 batch 的可运行长度和短文本吞吐不替代同并发尾延迟验收；预测分布、布局或质量—总成本不可信时，增加实际保留部分、重校准，或回退 FullKV、低秩与可恢复分层路径。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-22910` — [EchoKV exact-v1](https://arxiv.org/html/2603.22910v1)必要§3–5/Eq1–7/T1–4、B/T5与C/T6；只采用group-global/local-feature conditional重建及KV-MSE→attention-output MSE接口。保partialfeature单位、ratio反退/T4人口冲突、K/V分责和完整训练/驻留/重建费用；标准参数可切不授已丢历史exact恢复，后者保原/重算为项目合同推断。未核kernel/artifact/复现，不采allsettings/无损或生产SLO保证。
