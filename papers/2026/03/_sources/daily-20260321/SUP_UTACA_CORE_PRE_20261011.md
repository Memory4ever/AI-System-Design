# UT-ACA18446：必要原证 / actual sole owner / 最小 PRE

准备者resume_mar18，仅03-21补BJT03/20。已独校完整AB/官方日级夹证复用；不追v3或全venue。拟2+2+2=6，给learned时序难度→tentative KV snapshot→扩读重生成→token提交的新接口，而非已有稀疏选择、entropy或通用rollback原则。未独核/未锁/未写/未safe/DAY。

## Necessary exact-v1 与关键反侧

[原HTML](https://arxiv.org/html/2603.18446v1)实际必要§2–4.6/Eqs4–9/Alg1/Tables1–6及§7、B.1–3配置、C有限human核验、D.1–4直接对照。支持与反侧足够即停，未读全部图像prompt或代码、未复现、未旧新版diff。

- Context window是当前attention读取的KV subset，不是模型支持的最大sequence或已驻留总KV容量。Prefill仍将完整longcontext分blocks，以代表keys供query选topk；无source披露所有KV物理host/device/容量合计，少mTokens不证少完整Prefill、总state或HBM。
- 每tentative step读top1−top2 logit margin与最后attention输出embedding；双encoder对齐64维再时序LSTM，三分类correct/unknown/hallucination。unknown+hallucination>correct（correct<.5）只是分类trigger，不能标定每token真实错误或授普遍hallucination风险界；正确/未知高confidence原文明确不能仅靠margin。
- Alg1每步Snapshot(C)，先tentative，unsafe则Restore(C)并k=Kmax重生成，否则接受tentative且UpdatePolicy收缩；prose紧窗起步而算法初始Kmax，不能抄为统一初始recipe。原算法只说明C snapshot，未披露token cursor/RNG/selector和LSTM(h,c)在reject后的回滚协议；PRE只采用pending→restore→扩读→重生→commit分责，不签完整事务状态已实现。扩读后没有第二次detector检查，单次重生成不授已正确/最终安全；必须保留独立质量及硬预算。
- Synthetic train10000单属性、validation六未见属性各20，test100六属性bio+Wikipedia171k–400k/均252k；GPT-OSS120B生成bio、tokenlabel/judge并人工核，不能叫独立自然用户人口/未知groundtruth可靠。八trainingruns择最佳checkpoint，B.1最高validation F1/至10000epoch、batch16、单H100八并发每run约1.5h；择优并非报告跨seed结果CI。Qwen独立训detector不是Llama跨模型零样本迁移。
- Table2 InfLLM K3质量99.83>UT-ACA Sub1的99.08（29vs48读tokens），不是全部无损；Set1质量96.59更低。Table3 Llama InfLLM K32 .080s/72.26，UT-ACA Kmax64 .082s/70.48，Kmax96 .097s/74.61，局部质量/读取/latency互换，Qwen K8 37.77>UT-ACA Kmax16 37.08。表†baselineOOM/incoherent样本被排除，各人口并非全量同题；D.1同backbone复验仍如此，不能以它解决所有公平性混杂。
- Table4 SE+LSTM68.58低于SE-only69.58，不采LSTM每条件必提高；full70.48只受测组合最佳。Table5 qmsum反側是UT-ACA Kmax4 17.65<InfLLM K4 18.40，Kmax32 17.74<自身Kmax16 19.18；context扩大不单调。同等mTokens也不等完整walltime/费用预算。
- Table6 summary3508tokens/28.43<InfLLM4096/28.58，QA3712/21.32<4096/22.09；读取少而保近质量，不证明领先全部。D.2 RULER QA16k21.65<21.70，caption称mTokens units64而正文直接tokens，不能照精确24.8%预算保证。D.3三/二分类择best且平均读token稍异，只支撑有限标注粒度取舍，不唯一因果证明。
- Fig5文字base4.50–10.52s、regeneration.83–1.47s；detector/LSTM/复制/rollback/块选与Prefill、label/judge/训练费用都存在。有限图的“bounded”不授worstcase频繁trigger或线上尾延迟界。§7承认平均context下降不带比例latency下降。precision/完整sampling规则、servingbatch/concurrency、所有排除人口、end-to-endSLO/自然不确定性校准ND，未授production或实现已核。
- C只30 test样本同prompt人工/CAS均值差1.3points，个别.5vs.667、.83vs1仍不一致；群体均值近不是逐样本judge等价/全部任务真值。D.4一例logp提高仍−4.56，只rank反转不保证全局正确。

## Actual sole owner / 差额

`INFER-KV-CACHE` Ch45 actual184–245及198–218完整邻接：现有accessplan/gather、跨层刷新、层级entropy/varentropy trigger、物理keylocality、causalrepair。Ch44/46及Ch22开篇实际读，Ch22已有表示边界但不是此物理试算/回滚consumer owner。现Ch45层级trigger刷新选区已有，但没有**融合semantic/margin的时序分类读出，消费tentative step后恢复cache再扩读重生成，将候选和已提交prefix分开**。不fakeNC；不把原fixed/full方案当错误。

拟插入当前Ch45 202层级选择marker之后、204“层级选择还没有决定物理页”之前一段＋本人静态注。前段解释refresh signal，本段解释试算失败如何回到读状态，后段回物理布局；不另扩Sampling/Ch22。

## 一段 literal PRE（待非准备者）

刷新选择还可以由一次尚未提交的试算触发，而不只周期性检查选区。先在当前读取预算下生成候选，再把 logit margin、semantic hidden 与历史读出状态交给已训练的难度 detector；当它建议证据不足时，恢复试算前的 cache，扩大检索块预算，重新生成当前 token，然后才交给后续 prefix。这里扩大的是 attention 读取集合，不是模型支持长度，也不证明全部 KV 已被删减；detector 的 unknown/hallucination 标签只是提议，不是答案真值。[受限长上下文对照](https://arxiv.org/html/2603.18446v1)用合成人物材料训练和择优，其少读 token 不保证全任务质量保持或同比降低延迟。Runtime 必须把待定 token 与已提交 prefix 分开，并核清 cache、位置与 detector 等有状态读出的恢复责任；原文只说明 cache snapshot，不能当全部事务状态已经闭合。训练、标签、特征读取、快照、检索与第二次前向都付费，扩读重生也不自动成为已验证答案。恢复协议、代理或质量/全费无法验收时，保留固定预算、已验证的 full-context 读取与独立输出检查，不让一次 trigger 绕过提交和硬资源边界。<!-- source-family:SF-2026-ARXIV-2603-18446 -->

## 静态源注 PRE

- `SF-2026-ARXIV-2603-18446` — [UT-ACA exact-v1](https://arxiv.org/html/2603.18446v1) §2–4/7、Alg1/Tables1–6及必要B–D；只采用时序difficulty读出→pending试算→cache恢复/扩读重生成的条件接口。分类不授真值、cache-only快照不认证全部状态恢复、合成/择优/排除人口、任务质量与latency反退和完整费用保留；不授无损、总容量减少或线上界，未核代码/复现。

## root 非准备者有限 Source / actual owner / PRE 通过

root实际读exact-v1 §3.1–3.2/Eqs4–9/Alg1、§4.1–4.6/Tables1–6与直接费用反侧，actual Ch45完整184–235及Ch44/46开篇；逐字PRE/本人注回对。双信号→时序difficulty→tentative cache恢复/扩读与commit消费确为现有refresh后的新接口，2+2+2=6维持，必要Source与一段PRE有限PASS。正文与算法的初始预算差别、cache-only快照不闭合LSTM/位置/RNG、无第二detector验证、合成择优和质量/latency反退已隔离；不依赖把所读mean预算曲线称作worstcase界。Table3 †排除人口与Table5 qmsum退步均实际回核，正文没有照录全部附录或相关工作结果，未授复现/production。可授Ch45该一段与本人注窄写，实际POST尚未发生，不计safe/DAY。

## resume_mar18 非writer actual POST 正式有限通过

root按原PRE写后，resume_mar18实际顺读Ch45完整182–220（含原184–216必要局部）以及末七行本人静态注与全部邻注；新204逐字回对原PRE及上述有效必要Source，静态注准确，body/static各一、scoped diffcheck空。层级refresh→tentative试算/恢复/扩读/commit→物理页布局衔接完整；cache-only快照不授全部状态恢复、标签非真值、合成/择优、质量/latency反退与全费/退路近文保留。一次非writer实际POST有限PASS，不改变源注流程身份，不授DAY；已发送root接纳/释放Ch45。
