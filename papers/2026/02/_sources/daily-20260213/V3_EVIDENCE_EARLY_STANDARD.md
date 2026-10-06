# 早期四项必要证据（作者判断，待 root Source/Books 复核）

## [vera 2602.10146v1](https://arxiv.org/html/2602.10146v1)

5=2+1+2，标准后拟局部知识差额深入。§3.1 score以 gold evidence bbox coverage×head attention，dev每seen dataset70标注样本；不是零标注发现。Top5 head mask 对 random/OCR同数mask支持受限功能必要性，不识别唯一因果path；表1与紧接prose把random/OCR平均−.66/−.45顺序交换，采用原表不按文字授显著性。instruction首位置、reasoning entropy>2的firsttoken不自动是真实retrieval时刻。

§4–5.4：heldout-selected5heads→20patches→整行扩展→原image与附加text再答。数据是source text渲染图，可按坐标直接取原行；没有真实扫描/OCR错误成本被控制，所谓无需externalretriever不是无需额外prefill/attention读出。匹配20patch及同verbalization baselines支持受测retrieval选择，ColPali Hotpot recall仍更高；5.8–15%额外tokens，不授同质量/同E2Elatency加速。Qwen3VL8与GLM4.1V9B，context1.5–16k，visualtokens1.3–5.7k；hardware/precision/batch/SLO Not Disclosed。局部gain不能证“universal”或gold-free evidence truth。

拟 Ch23/MULTIMODAL-REPRESENTATION 差额：499已有有无query两Prefill static attention crop，720已有driving/resistinghead与probe；VER新增gold-dev定位检索head、generation moment读出并回到text的接口分责。拟两句追加动态/标注依赖与原文行/OCR区别，若root认为原论点已充分则仅报告，不凭主题相似Existing。

原证 INITIAL/METHOD L120–213；EVAL L206–261；V3_EVIDENCE_10146_10204_TAIL.txt 内10146 L264–309。

## [VJA 2602.10179v1](https://arxiv.org/html/2602.10179v1)

6=2+2+2，安全受影响深入。§2 actualimage-only，无outertext，通过visual marks/visualtext传edit intent；output是image，不能由文本拒答率替代 harmfulness/valid edit。§3–4 1054 curated样本，20%category-balanced同任务TJA比较，10%harmful+10%sourcebenign risk detection；ASR、editing validity、harm severity分账，模型读不懂会降低validharm并非guard可靠。Gemini3Pro defaultjudge；5%outputs人类从多个judge结果投票，不是全量blindgold，ratings显著异质。

Safety trigger appended给本身预对齐VLM判意图；reuseKV只避免重复imageencode，不使safety classification免费，仍非零ASR及misleadingfacts失效。未采用negligiblelatency中心宣传，无需展开全A4。C3：商业API，local按官方模型并promptenhancer，8V100；precision/batch/sampling/SLO Not Disclosed。HTML首部preprint印Aug24与Febv1 metadata不一致，不拿其改事件归属；v1PDF当前web/curl不能取，故日期/身份由官方abs公开机制单独核，不读后版。

拟 Ch72/PLATFORM-SECURITY现1210–1220已有OCRlayout→generationpolicy及readability分账，可承载此visual-only editing验证；此处虽不同输出intent接口，但无新确定性权限/防线保证。拟 **已有覆盖**具体采用“视觉也是generationproposal surface，实际输出/validharm与readability分账”；若root认为纯marks不含OCR的editor intent有长期新接口差额，可一窄句补非文字视觉intent，不设攻击recipe全附件队列。

原证 INITIAL L75–95；METHOD L110–135；EVAL L187–235；CONFIG L621–634。

## [Versor 2602.10195v1](https://arxiv.org/html/2602.10195v1)

5=2+1+2，标准完成拟仅报告。§4 Clifford multivector32维 scalar+bivectorscore、Cayley localrotor→Normalize(ΔRΨ) recurrentstate，以固定algebra/channel数量作O(L)/constantstate；未授physicalenergy conservation或任意norm-gradient稳定定理。核必要architecture与direct反侧即止，不全数学附件。§5 naivePyTorch78×kernel不是Transformer同quality；compiledCore1.56ms vsTransformer.62ms也非更快。

§6.4 main字符PPL3.22同时写WikiText2与103，未披露同tokenizer/trainbudget/pairedLM baseline，不能把该数与词级PPL比。CIFAR10只有3epochs49.63，不能证明universal backbone胜出。§6.1 CPU perstep、5seeds物理toy有高std，参数scale差异有意研究inductivebias而非production；本项目不展开AIforScience结果。§7明确32floatregisterpressure/当前GPUsoverhead，normalization不保证energyconservation；latentSpin constraint不等真实worldstate。precision/CPU型号/sequencebenchmarkbatch与大模型cost Not Disclosed。

拟 **仅报告**：新增geometry recurrence是可复核原机制，但当前一般LM/vlm对照不足以给长期baseline替代条件/可执行设计；不是成熟组合EX，也不从固定维state借Durability3或泛化GAPU硬件提案。保留未来同接口、同数据/quality/runtime的重开条件。无需造StructuralCandidate新chapter。

原证 INITIAL L109–114；METHOD L245–312；EVAL L205–244；V3_EVIDENCE_10195_10179_FINAL.txt 10195 L313–365。

## [MVN-Grad 2602.10204v1](https://arxiv.org/html/2602.10204v1)

5=2+1+2，标准，拟机制差额深入。Alg1先EMA rawmean→EMA residualvariance，再当前gradientnormalize→EMA normalizeddirection；m和u不是同state，即使共享β1。εs工程floor防近零variance；formal分析设εs0。Theorem3.1要求symmetric centerednoise及m(t−1)=conditionalmean；strict variance improvement需非零乘数/normalizer随机性，不能由≥0授everyupdate严格变好。单spikebound显示Adamβ2>β1²仍统一有界（§3Remark3.1），不授Adam普遍无界。

§4 OWT124M/seq1024/micro12×acc40=480、bf16/clip1/warmup2000/120kupdates、decoupledWD.1/dropout0；同9βpair与η1e−4 grid、selected config再3seeds，但variancefamilies原WikiTextgrid额外εs选择、earlyterminate varyinglength非全grid公平平均。OWT valLoss2.97347±.00746 vsAdaBelief2.97438±.00811重叠，不授显著胜出；WikiText30M/seq512/batch128/4seeds且coupleddecay有不同state filtering，不直接合并。Hardware Not Disclosed（致谢Vista不等披露实际GPU）。主要支持ordering/stats选择与本地sweep，不授生产吞吐/零额外state。

拟 TRAIN-PRETRAINING/Ch28现229只有Adam raw moment状态，缺“先normalize后momentum保留历史已归一方向，centered proxy与uncentered secondmoment相互独立两轴”具体机制及floor/idealmean边界。采用机制不采用普遍优化定理；如写conditionalvariance公式则再定点proof，先rootSource+owner核而非默认全部证明。

原证 INITIAL L98–119；METHOD L123–204；EVAL L237–284；V3_EVIDENCE_10146_10204_TAIL.txt 10204 L270–293。

## 10204 当前正文比较收束（作者）

实际重读Ch28 L225–248 optimizer state/迁移，及optimizer统计相关段；Adam raw moments和DP filtered-noise correction不等于normalize-before-momentum。仍缺rawmean/residualvariance vs normalized-history两个状态轴。拟在Adam moment说明后两短段采用Alg1运算次序及epsilon floor/idealmean条件，保留state成本、loss区间重叠与Adam同样有bounded spike反侧；不写未验全trajectory定理。待PRE窄锁。

最终状态同步（2026-10-04）：当窗有效的10195仅报告、10204 Ch28实际两段/完整邻接/末注已root非作者POST通过，锁释放。10146/10179仍必要日期终态保留，不被计入112候选或46Books；原已读贡献/反侧保留不支持当窗采用。日级另验。
