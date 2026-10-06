# 1/W17280：有限解析边界/PRE

resume_mar17，只03-20补03-19自然日；2+1+2=5及day/一次准入消歧复用独核§6。本次必要[exact-v1](https://arxiv.org/html/2603.17280v1)§2–5/Eq1–4/Table1–4及§10.1–2实际读；§6–9与A/B同次返回只为决定性数字/限制定位，未执行代码/旧版本/全证明。支持及直接反侧已足停止。未授Books写/SourcePASS。

## 原证与反侧

- Eq2严格是 n/[τ(n,Lbar)P(n)]，τ=W_weight+H(Lbar)n；H正比实际mean scanned KV length，而Eq3 nmax=floor(V_KV/(κ*configured_window))仅容量模型。configuredwindow不是实际扫描长度，动态分页/短请求不自动预留整窗。窗口缩短是否使实际并发增大依赖admission/allocation/负载，不能静态配置直接证明能耗。
- §2.2“nmax和H均linear”语义不精确，nmax是反比。若实际Lbar也正比window且n≈nmax，Hn近常数；τ近常数而非正比window。此时再加P(n)近平坦、floor/容量余量不主导，效率才近1/window。若Lbar固定且KV项主导，Hn随n变化，吞吐趋平台，不能从窗口反比concurrency授能效严格反比。Eq1本来非线性，§2.1把2^x0≈18称饱和是half-range不是fullplateau。
- Table1 H100同配置2K→128K的P从598到369W，4K17.6与64K1.5之比11.73而窗口比16；不是每翻倍严格减半。T1/§4 calibratedprofile 8K n128，T2/5 ComputedProfile同70B/TP8 n22，实际KV/权重budget不齐不能合并口径；§5“任何model64K n16”与T2model-dependentcapacity也不相容。
- T3 Azure拓扑倍率H10014.08/5.58=2.5233、B20023.71/9.74=2.4343，交互比0.964726；LMSYS交互比(14.82/7.98)/(10.30/4.77)=0.860055。不同条件没有无交互保证。Azure同路径2.5233×(23.71/14.08)=4.2491是比值telescoping恒等式，不证independence；跨路径乘积2.5233×(9.74/5.58)=4.4045≠4.2491。保作者“approximately”有限解释，但§4/结论的orthogonal/nointeraction/通用multiply不采用。
- T3所有fleet是解析sim而非新hardware实验；70B/TP8/fp16、λ1000/s、P99TTFT500ms、平稳Azure/LMSYS CDF。H100既有测量校准，B200/H200投影/无productionstack实测；TDP比例不授采购定量。TPshardedGQA/非replicatedKV与actualowner约束一致。
- §5 perGPU/perTPgroup口径摇摆：413W从表device到正文pergroup，不混合分母；semantic8B质量未matched70B，不能授相同goodwork；量化W减少不等τ完整同比减半。MoEactiveweights忽略dispatch/imbalance，不能把activeparam当全部权重/通信费用。§10明确chunkprefill/HOL/eviction、bursts/sparecapacity、autoscaling/share未建模，输出token-only不含prefill，更不是wholehost/goal energy。路由、容量重配、padding/overflow、calibration与全部失败/闲置费用Not Disclosed。

## actualowner/差额

唯一`PLATFORM-COST` actualCh70 L80–155（trajectoryactiveKV/length/利用率/wholehost）、180–205（idle/power与context反馈）、260–292（解析规划与PowerTrace）、365–387（二维sweetspot/actuator/交接）完整读；Ch69/71入口、Ch54入口capacity与Ch56 55–92SLO/KV/admission/网络交接实际读。已有正文承载非线性proxy/配置校准和fullfee，不重复它。尚未承载**configured reserve与scannedKV区别导致1/window推导条件**及**联合收益的路径恒等式不等独立性**这一精确差额。拟Ch70 L377 sweetspot段后/actuator标题前两短段；不改54capacity或56scheduler。

## 最小逐字PRE（供独核裁，不先写）

Context 长度的能效推导还要区分配置窗口、实际驻留 KV 与每步扫描长度。一个[受限 Decode 解析模型](https://arxiv.org/html/2603.17280v1#S2)把效率写为 `n/[(W_weight+H(Lbar)*n)*P(n)]`，容量上限另由 KV 预算与配置窗口决定；`Lbar` 是实际平均扫描长度，不能拿最大窗口直接替换。只有并发贴近容量上限、实际长度随窗口同尺度变化、功率处于近平台且离散余量不主导时，才可能出现近反比区间；分页短请求、低负载或扫描项改变时必须重估，不能据缩短配置窗口签发固定节能倍率。这里的 `W_weight` 是权重搬运时间，不是窗口符号。<!-- source-family:SF-2026-ARXIV-2603-17280 -->

硬件与路由拓扑也应联合测量，而非把各自相对不同基线的收益直接相乘。沿同一路径的两个倍率相乘只是比值恒等式；证明近似独立还需要跨硬件、跨拓扑的条件收益和交互误差。该模型的两种 trace 已出现不同交互，且新硬件功率主要由投影给出，不授普遍正交性或采购保证。Context 分池可能减少短请求的容量暴露，却新增流量分配、闲置和重配成本；输出 Decode 效率还遗漏 Prefill、排队/驱逐、整机与失败工作。只有质量、SLO、计量边界和实际 KV 配置一致时才验收联合收益，否则保留原池和保守余量。

静态注：`SF-2026-ARXIV-2603-17280` — [exact-v1](https://arxiv.org/html/2603.17280v1)必要§2–5/Eq1–4/T1–4与§10.1–2；仅解析成立条件、配置/扫描长度和联合倍率边界。不采严格1/window、独立乘法/数字采购、跨model质量或完整能耗保证；原表profile/分母差、投影/输出only/fullfee保留，未核代码或复现。

## 未采中心的一次请求/停止

如授严格law/独立乘法/定量SLO-energy，需一次请求：matched实际resident/scannedKV与配置window/admissiontrace；T1/T2profile和GPU/TPgroup分母映射；固定质量/SLO跨硬件×拓扑factorial及全服务能耗/不确定性。当前可分采解析身份和反证边界是否足够由非准备者裁；若中心不可分则保5争议隔离，不降分EX/假NC。普通来源初筛仍可执行，本日无DAY。
