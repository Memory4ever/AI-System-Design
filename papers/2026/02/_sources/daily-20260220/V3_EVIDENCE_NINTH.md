# 02/20 第九有限必要包：16449 / 16455 / 16456 / 16469

只保作者实际判断+最小support/counter位置及actual owner，不重做已有效AB校准或全部附录。root必要原源/actual owner PRE及16449/16455/16456实际正文/完整邻接/自身末注POST通过；16469仅报告限定通过，无Books写锁。抽取位置统一 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`；current事件页完整AB/Comments/history实际读，16449当前v3、16455/456v1、16469v2。没有撤回/纠错标记，16469摘要实际新增quality条件已定点补读下述v2，不由版本号全量比较。

| ID | v1 Submitted UTC | Registered UTC | 北京公开范围（含起、不含止，官方bridge推定） |
| --- | --- | --- | --- |
| 16449 | 2026-02-18T13:33:54Z | 2026-02-19T02:46:27Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:46:28+08:00 |
| 16455 | 2026-02-18T13:40:53Z | 2026-02-19T02:46:36Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:46:37+08:00 |
| 16456 | 2026-02-18T13:41:41Z | 2026-02-19T02:46:38Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:46:39+08:00 |
| 16469 | 2026-02-18T13:59:08Z | 2026-02-19T02:46:56Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:46:57+08:00 |

## [GICDM: Mitigating Hubness for Reliable Distance-Based Generative Model Evaluation](https://arxiv.org/html/2602.16449v1)

2+1+2=5，评价反側与具体差额深入。必要support §4.2–4.4（350–454）：real-only ICDM冻结δ，再为每generated point只按real邻域算scale，避免generated set互相改变点的评价；未filtered版本会把偏离manifold的点过度校正，q=0.95 local-scale过滤，Gaussian crossover随K/N/d变化所以两尺度过滤。两K避免某Gaussian crossover不是任意分布保证。必要counter C.3（2189–2194）单维异常被Euclidean平均、离散/连续等仍失败；D.3（2222–2234）real-outlier-robust clipped度量相关保持/提升，其它度量反退，FFHQ无显著相关。synthetic tests匹配固定oracle曲线，real50k+generated50k、k5/DINOv2/v3与同已发布gen样本，只是作者评价，不能授普遍“可靠metric/rootcause全识别”。hardware/precision/重复不确定性在采用位置Not Disclosed，不用速度/生产数字。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66:94–110已metrics/eligible population/scorer与代理对象；626–634已有embedding density/uncertainty与视频摘要proxy，但未承载**metric采用的reference embedding几何本身会制造hub、同一generated point不应因加入其它生成点改变评价，校正必须守real-only及outlier失效边界**。拟一自然段在metric对象论证/embedding sensor处融入，不复制FID或高维名词；若现更具体几何owner已承载则改Existing，不因缺GICDM名称强写。

## [Visual Self-Refine: A Pixel-Guided Paradigm for Accurate Chart Parsing](https://arxiv.org/html/2602.16455v1)

2+1+2=5，原源§2.3（102–113）先生成pixel coordinate、在**原图绘marker**再回输检查/改位置、最后原图+positions decode数值/legend，分开where与what；自确认不是正确性证书。3.3/4.1（161–167）含shift/missing/hallucinated marker纠正训练，Qwen2.5-VL3B全部三模块unfreeze、8H200144GB/1epoch/b128/最长边1036对齐28patch，精度/seeds未披露。4.4/Table4–6（370–464）完整vs无VSR/无pixel对照，Hard差异更大，位置-only收益小；但minimum3calls对1call，未等完整inference预算。AP-Strict近零，不能授数值精确。错误chart第一轮110→51，第二54/第三52不单调，确认precision88.2%→76.0%/76.6%，更多回读不保证恢复。Counting/grounding只示意/潜力，不当跨任务实验。

actual `MULTIMODAL-REPRESENTATION` Ch23:519–531已有claim-directed crop acquisition，Ch80:45–59已有selfcritique共享盲点；未承载**原图上的派生定位marker作为可重读中间表示，先修where再decodewhat、坐标/resize身份与selfconfirm权限分离**。拟Ch23最多一段接active observation，query crop不是同机制；保低成本one-shot、render+多call与不精确数值边界。不借chart排名论证普遍selfrefine。

## [Beyond SGD, Without SVD: Proximal Subspace Iteration LoRA with Diagonal Fractional K-FAC](https://arxiv.org/html/2602.16456v1)

2+1+2=5，必要理论/owner差额深入。最小support §3.1–3.3（241–365、400–420）：adapter weight-space full step `UVᵀ−ηSᵀX`低秩和，缓存linear输入X/输出梯度S，用warm-start proximal ALS近似rank-r投影，不先物化dense G。普通autograd只旧factor梯度，内循环改变factor后需要同batch新matrix-product，不能称普通factor Adam等价。Theorem3.1仅ρ=0/初subspace与top-r非zero overlap，ratio σr+1/σr控制rate；实用ρ>0防factor不稳定不是该无ρexact投影保证。§4.1（471–559）whitened metric projection、EMA diagonal Kronecker fractional scale，fullmetrics开销而用diag，不能叫完整K-FAC或保持全curvature。

关键control/counter §5（564–568、693–737）GLUE每method3lr先20%budget、同method跨task一lr；SQuAD小T5表EM/F1改善但eval-loss高于Full。§6（760–771）X/Scache+内iterations成本，更多K在stochastic gradient可更差、diagonal crude、gradient accumulation/distributed实现仍future。不采用“modest overhead”或全model收益数字；hardware/precision/完整walltime在拟采用必要位置Not Disclosed，未核代码/复现。

actual `TRAIN-LORA` Ch30:185–199已离线QR/SVD压rank与耦合谱更新/effective-rank、正交factor约束。差额不是少ALS配方，而是**固定batch的full weight-step能以X/S products在变化factor上近似投影，避免dense G/SVD却需保存输入/输出梯度与内循环，区别仅旧factor梯度**。拟一自然段接193 spectral-update论证，保ρ0理论/实用prox区别、有限stochastic/damping/内存与原factor优化共存。

## [Training Models on Dialects of Translationese Shows How Lexical Diversity and Source-Target Syntactic Similarity Shape Learning](https://arxiv.org/html/2602.16469v1)

2+1+2=5，标准必要证据后拟**仅报告**。support §3（82–108、322–332）125M/512context/common50k tokenizer，source24语言→English/100MB、1000MB/native相同bytes；BLEU未在v1直接控制，corpusdomain/noise不同，bytes不是相同tokens/独立同质语料。§4.1/4.2（576–585、673–675、759–784）100MB TTR与部分PPL相关而BLiMP无；1000MB5低资源被排，lang2vec缺失n17（不是24）与BLiMP Pearson+.61、Spearman+.32未显著；统计单位source语言/语料，不多seed不确定性。BLiMP以正确句mean PPL低于错误，不同于真实所有语法能力，native部分对照也含同source web分布。

直接limits（804–819）未拆typology/lexical/domain/noise、只一translator/向English/小模型，v1自身关联证据已经不足以授TTR唯一/主要因果或“语法由typology因果”。current v2只留窗外限制线索：此前已定点实际读 `V3_CURRENT_2602.16469v2.html` §3.3（348–350）quality评价及结果（831–833）、讨论（903–904），不倒填v1原证明，不建立本窗另一事件/家族；没有官方纠错声明，版本号/新内容不单独触发进一步比较。至此停止v2追查。

actual `TRAIN-DATA` Ch27:1254–1264已parallel/code-switch/boilerplate身份、语言对/quality/domain/unique-token、按语言任务回归；1260–1262已sourcequality和langdistance相互混杂非因果、不能只比例补料。新source-language双task关联提供本协议局部经验，与现selection/quality/任务分账一致；缺TTR/BLiMP具体配方不强造gap，建议仅报告，不写书。
