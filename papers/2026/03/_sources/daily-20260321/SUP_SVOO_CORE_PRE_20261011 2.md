# SVOO 2603.18636v1：必要证据与受限 PRE

准备者/拟writer root，只本21补03/20；原完整题摘/日级日期夹证与准入已独校，不重算原候选。拟2+1+2=5，新增是视频DiT稀疏执行的离线layer-head画像与在线相互依赖Q/K分组，不把成熟sparse attention或7个模型数量计新。

## 实际必要原证

[exact-v1](https://arxiv.org/html/2603.18636v1)，§3.1–3.2、§4.1–4.2/Eqs2–7/Alg1，§5.1–5.6/Tables1–2及B.1/B.3–5/B.7–8直接profile、reuse与对照边界；未读全proof、全部图点/定性附件，未核代码或复现。不采用理论全输入稳定性，故不扩整份证明。

- 每层/头由小校准集测覆盖给定attention mass所需density，拟合Gaussian上分位产生budget。实际B.7仅10个GPT5生成calibrationinputs，无具体离线秒数/摊销成本；不能把training-free等同无准备费用或任意输入稳定。§3.1为5 prompts/80%mass，§4.1配置95%mass/95%分位，不能混口径。
- Alg1交替key对queryanchors的affinity空间归组、更新keycentroids，再query对新keyanchors归组/更新query；不是分别原欧氏空间K-means。后续用centroid交互估blockimportance/select，再Triton/FlashInfer sparse执行；centroid近似与真实mass/最终视频质量不同。
- Eq6 s=1-density定义稀疏率，Eq7却作为dense保留ratio的min/max预算，语义未齐；不将Eq7抄成通用选择配方或精确质量预算。方差proxy/有界token与长序列本身也不保证任意prompt/head/diffusion-step的mass覆盖或OOD不变，只保有限经验校准。B.5把推理dense warmup写成learning-rate/training-latency语言，与training-free定位冲突，不采用其训练解释。
- 在线twoiterations、Kq256/Kk1024、20step重分组，firstlayerdense，Wan20%/HY10%densesteps；reuse相关高不证明数学等价，prompt/shape/model/step区间变化需要重验（工程推断）。B.3更长reuse部分质量轻微降，B.4更多blocks成本增加。
- 7个Wan/HY T2V/I2V，singleH200，720x1280；Wan81/HY129frames，Radial却704x1280/85或133frames，不能宣所有基线严格同形状。Servingbatch/concurrency、precision、repeatseeds/CI、tailSLO未披露。T1 HY PSNR24.879<SVG2 25.218、LPIPS.224>.205，部分VBench相对dense更差；T2 WanI2V subjectconsistency94.80<SVG2 95.72，HY多metric低dense。不是“质量全胜”或无损。
- §5.3无Off改固定recall90%，与主95%/其他budget不同；§5.6/B.8称matchedbudget但定义随覆盖参考所需blockpairs改变，不能仅凭陈述认定全部数/质量/费用匹配。采用有限jointcluster分工，不采唯一因果全提升。

## Actual sole owner

`INFER-TENSORRT-LLM` Ch49拥有lowering、profile、metadata/kernel与执行路径，Ch24生成语义不另复制。实际读1497–1561完整 indexed execution/widthmetadata→queryrisk→联合预算，Ch48小结与Ch50开篇。当前query-specific路径已有saliency/risk→full/sparsefallback，但缺**画像预算与输入相关Q/K分区分责，分区按另一侧亲和性更新而非两独立K-means**。最小两段接在query-risk两段后、Token-level联合预算前；无新增heading或owner。

## 两段逐字 PRE

视频 DiT 的 block 稀疏路径还可以把预算画像与分区形成分开：先在有限校准输入上为各 layer/head 估计保留 attention mass 所需的密度，在线再按当前 Q/K 形成 block。若分别在原向量空间聚类，欧氏近邻未必具有相似的相互关注模式；一条替代分支交替按 key 对 query anchors 的亲和性归组，再按 query 对更新后 key anchors 的亲和性归组，用这份耦合 metadata 提议需计算的 block pairs。预算画像不代替当前分区，centroid 重要性也不等真实 attention mass 或最终视频质量；它们与 model、shape、head、校准人口和去噪步区间共同构成可检验的 execution plan。<!-- source-family:SF-2026-ARXIV-2603-18636 -->

分区跨步重用可摊薄 clustering，但增加陈旧 metadata、重排和重新校准成本，并不保持 dense 等价。[受限 SVOO 对照](https://arxiv.org/html/2603.18636v1)只测 single H200 的 Wan/Hunyuan 视频生成，部分质量指标低于 dense 或其他稀疏分支；少量校准与 logit 方差分析不保证任意输入的剪枝容忍度，原选择比例也不能直接当成严格质量配额。离线画像、在线聚类/布局、dense warmup 与重建均计入完整费用，不由 training-free 推出免费；独立分组在形状稳定、简单性优先时仍合理，画像失配、跨步变化或净收益不成立时回退重新分组、保守稀疏率或 dense attention。Serving 并发与尾延迟还须另验，不从视频离线均值授生产 SLO。

## 本人静态注 PRE

- `SF-2026-ARXIV-2603-18636` — [SVOO exact-v1](https://arxiv.org/html/2603.18636v1) §3–5/Eqs2–7/Alg1/Tables1–2及B.1/B.3–5/B.7–8必要边界；仅离线layer-head预算与在线Q/K亲和性联合分组的有限接口。选择比例口径、少量校准/理论代理、跨步reuse、基线shape差异/质量反侧与全准备费用保留，不采无损、任意输入稳定或生产SLO；未核实现/复现。

待非准备者Source/实际owner/PRE裁决，不自己授PASS、未写或计整合；有实际结论分歧先局部纠正，不绕过反证。

## 非准备者必要 Source / actual owner / PRE：正式通过

resume_mar18独立恢复本21合同/ROADMAP与本日停点后，实际打开exact-v1 §3.1–3.2、§4.1–4.2/Eqs2–7/Algorithm1、§5.1–5.6/Tables1–2及B.1/B.3–5/B.7–8；不扩大整份Appendix A证明、定性图点、实现或旧版比较。实际顺读Ch49完整1490–1570（indexed reduction→widthmetadata→query-risk→联合预算）及Ch48小结/Ch50开篇，逐字回对上述两PRE和静态注。正式限定Source/actual sole owner/PRE PASS，不授写后通过或DAY。

在线交替按另一侧anchor的归一化affinity空间归组/更新centroid，与离线按有限校准attention mass估density预算的分责具体成立；现query-risk路径有条件sparse提议/执行fallback，但尚无这条耦合分组metadata形成链，放query-risk后/联合token预算前自然。原Eq6稀疏率与Eq7保留比语义、少量校准与方差proxy不足授任意输入稳定、B.5错写learning-rate/training语义均近文隔离，不影响仅经验画像＋可执行分区接口的独立采用。

§3.1五prompt/80%与§4.1/ B.7十校准/95%不混；reuse、blocks数量增加的布局/重算成本、Radial分辨率/帧数不齐、Table1 HY PSNR/LPIPS与Table2 subjectconsistency的直接反侧、5.3不同recall及B.8按各method覆盖reference定义预算的桥未闭合，原PRE均未授质量全胜/唯一因果。完整准备、warmup、clustering与dense回退属于明确工程验收条件，不是作者生产保证。无需再扩大全proof，因为本文理论强claim没有被PRE采用。

评分实际命题为执行engine内layer-head画像与Q/K metadata的机制分支；System Reach1比初始2更贴合此项新增且采用的单执行边界（并未改变跨系统状态交付/提交责任），因此支持root拟2+1+2=5。保留初始6及本实际依据，不以审阅工作量、Books有无或七模型数量改分。5分仍因具体长期owner差额深入审受影响部分；待root协调唯一Ch49窄锁、writer实写与一次非writer完整正文/邻接/静态注POST，当前不计safe/I。

## 一次 nonwriter actual POST：正式通过

root接受上述非准备者Source/PRE后own唯一Ch49本family两段＋静态注窄写。resume_mar18实际顺读完整1520–1558（query-risk前后完整widthmetadata→画像/分区→联合tokenbudget→密文交接），新1532/1534逐字回对已核原PRE，末尾本人静态注与相邻两注实际读取。预算mass画像与affinity联合分区不是两独立K-means，centroid非真mass、理论/比例强claim不采、少量校准/quality反侧与离线/online/densewarmup/metadata费用及fallback均准确；不授lossless、production或tailSLO。静态本人注准确限定必要Source范围与未复现；限定git diff --check空。正式actualPOST PASS，可告root释放此窄锁/归并单项I，无需递归改静态注身份，不授DAY。
