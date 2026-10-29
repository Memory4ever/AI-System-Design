# EntropyCache18489：必要 Source / actual owner / 最小 PRE

作者 resume_mar18；只本03-21补BJT03/20自然日。首批完整exact-v1题摘已root独立准入校准；日级归属是官方availability、v1 header与arXiv-issued DOI03/20注册夹证的限定推断，见SUP_FIRST_ADMISSION与SUP_FIRST_ARXIV_DATE_FIELDS，不冒精确公告时刻或作者别处从未先发。当前未授非准备者Source/PRE、Books锁、POST或DAY。

## 1. 原证与实际必要范围

[exact-v1 HTML](https://arxiv.org/html/2603.18489v1)：§1–2；§3 entropy/drift与recent-token volatility；§4/Algorithm1；§5.1–5.4/Tables1–3与GSM网格；Appendix A Algorithm2、B非EOS相关、D Table9、E单样本wallclock、F内存、G限制。支持与直接反证足够即停，未遍历全部附件、代码或后续版本；未运行实现/复现。

机制是读取本轮新揭示token分布的最大entropy，决定下一步全量forward还是近似重用，再以decode-history的recency阈值提出持续重算集合。Partial路径中的masked/recent queries仍读取完整缓存K/V；这不是AR exact-prefix。最大entropy阈值只对应受测drift代理，最近揭示位置的feature可以在后续多步变化。

必要评价：RTX3090、LLaDA8B-Instruct/Dream7B-Instruct、window32（Fast-dLLM改block32）、统一作者重实现、confidence-parallel门槛.9、默认tau1.5/k64。Standard各任务最大生成长度256/512及fewshot不同，CoT另协议；precision/batch/concurrency/SLO与重复统计在必要原证Not Disclosed，不外推服务收益。Table1 LLaDA平均52.28/45.36tps、Dream56.21/81.90tps；15.2/26.4倍率相对vanilla，包含原parallel收益，不是缓存单独收益。LLaDA MBPP38.80<42.20，Dream MATH43.20<44.60与MBPP48.80<50.60；CoT两模型平均48.57<51.49、50.97<54.46，BBH反退显著。Tau/k网格非所有任务单调；需要独立质量及完整费用验收。

Appendix B仅剔除EOS后的Spearman .616/.558/.606/.377，HumanEval更弱，EOS低entropy仍可高drift；受测EOS是padding不能建立一般无害定理。Appendix E只有单GSM/window32/length256，71ms decision与12.9s总时是局部profile，不证渐近复杂度或全任务收益；F相同局部约18.85GB含权重/KV，历史每generated token一integer为O(N)，非零额外状态。

## 2. 不可删的直接反证 / 采用隔离问题

1. 作者§4/Alg1及A Alg2先取k个最大H，再令R包含所有H不小于cutoff的位置。并行揭示会出现同step ties：k=1、H=[t,t]且最近全算距至少0时，cutoff=t，R含两项。因此该式不授严格|R|≤k/固定重算人口；若要精确cap须另披露tie规则。只是从原式独算的反例，不声称作者代码错误或所测默认参数必溢出。
2. E是对D中新token的V维分布计算entropy再max，显式算术为O(|D|V)，还要更新/选择history。固定window可约束|D|，但不能据此把整个决策无条件记为O(V)。Table3/§5.4 history O(k)与Appendix F O(N generated)不一致；不采用常数全state/无额外存储或模型长度完全解耦保证。
3. 相关代理、质量反退和并行baseline差别不支持lossless/普遍准确率保持；不以删反证、改EX/降分降低处置队列。

拟评分2+2+2=6（最大entropy触发与多步recency分责、跨生成/缓存接口、可复用的受限误差预算）。因复杂度/预算桥实际冲突与具体owner差额，定点深入以上必要内容。请非准备者裁：有限代理接口是否有独立证据成立、可与上述强claim隔离；若不能则按中心争议暂缓，不绕成一般缓存原则。

## 3. Actual sole owner / 差额

已fresh加载ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、相关LS路由；实际顺读Ch24 1370–1530完整cache/commit/trajectory局部及Ch23/25开篇交接。唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`，文件books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md。现1380节已有双向可变cache和全刷新退路；1430附近已有latent/confidence选择mutable-set、动态sink及confidence非validity；1482节已有误差轨迹/锚点/CKA、chunk独立龄期。尚未承载“新揭示分布的max entropy决定下一步全算”与“history按unmask step包含ties的recency集合”两个具体接口，不能仅因已有cache主题写NC。Ch45的AR KV不是本family owner。

拟位置：现mutable-set选择与其selector/shape成本两段之后、原“固定区域选择也可以读取prompt”之前（当前1449之后/1451之前；落笔前须重读actual最新局部，root窄锁为准）。只一段、不创建新标题、不覆盖旧路径。

## 4. 一段逐字 PRE（尚未授权写入）

重算信号也可以直接读取新揭示 token 的输出分布，而不另遍历层内 attention：一条受限离散 diffusion 分支用本轮 decoded positions 的最大 entropy 决定下一步全量重算或缓存重用，再按揭示时刻挑出近期位置持续更新。它分开“何时刷新全状态”与“哪些刚揭示位置仍有多步波动”；已解码并不授其 hidden/KV 永久稳定，低 entropy 也不是 cache-validity 或正确性证书。原 recency 规则按时间阈值纳入全部同刻位置，不能将名义 k 写成严格重算上限；分布统计、history 更新/选择和部分 forward 仍有费用。[必要方法与反侧](https://arxiv.org/html/2603.18489v1)只支持两类模型的局部质量—吞吐取舍，代码任务与长 CoT 有质量反退，大倍率还包含并行解码基线的收益，不授常数全状态开销、lossless 或线上 SLO。代理失准、近期集合膨胀或完整费用/质量不合算时，保留保守提交、固定 refresh 与全量重算。<!-- source-family:SF-2026-ARXIV-2603-18489 -->

## 5. 本人静态注 PRE

- `SF-2026-ARXIV-2603-18489` — Daily `2026-03-21` 补查；[EntropyCache exact-v1](https://arxiv.org/html/2603.18489v1) §3–5/Algorithms1–2/Tables1–3/9、Appendix B/E/F/G。2+2+2=6，必要局部深入：新揭示最大entropy与近期多步refresh分责；不采严格k上限、O(V)/O(k)全决策/存储保证、无损或通用性能。并行ties、O(N)history、非EOS相关人口、代码任务/CoT反退及完整费用近正文；未核实现、复现或服务SLO。

## 6. 后续

仅等待非准备者必要Source/actualowner/PRE裁定；未写Books，不把普通独核待办称外部阻塞。通过后root才协调窄锁，实际写后非writer一次完整局部/静态本人注POST，不向书注复制审阅人或验收过程。

2026-10-11 root非preparer正式有限Source/PRE PASS：实际exact-v1 §3–5/Alg1、Appendix A recency/entropy、B EOS/64sample、E/F/G与actual Ch24 1424–1467完整局部；两接口可独立采用，k ties、O(|D|V)+history与质量反退保留，不授constant/lossless/生产。静态注仅窄纠“代码/CoT”→“代码任务/CoT”，正文不改。root授Ch24本一段+本人静态注窄锁，写后root一次nonwriter POST；未先计安全整合或DAY。

2026-10-11实际落实与非writerPOST：作者获锁后写Ch24一段1451及静态注2463；root实际完整1442–1464正文/两侧与自身末注回对原PRE和有效Source，仅发现正文“代码与长CoT”语义词句需要同静态注一致。作者窄纠为“代码任务与长 CoT”，同步原PRE；root最终定点实际读回与限定diffcheck PASS，正式POST通过、Ch24锁释放。单项实际整合成立，不改书注加入验收身份，不预支整日DAY。
