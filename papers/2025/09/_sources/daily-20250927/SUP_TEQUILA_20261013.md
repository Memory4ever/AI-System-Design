# Sep27 TEQUILA单家族恢复：Carson

## 1. Fresh范围与有效层

Sep29真实DAY18–19/FINAL20/root21已actual读回并只同步README已发生指向；root最新State55/132、77待验，Sep27仅此新遗漏暂未重新计完整日。已fresh重读AGENTS、当前Research/Report合同、Sources说明/Daily/arxiv、Prompt、完整ROADMAP、相关State、Sep27当前六节/RESUME最新停点与CURRENT最终角色。仅2509.23809/TEQUILA、Sep26完整BJT自然日算法release，不重十四源/原134/CE/22343/22211，不继承Sep29队列或新的Source成功。

本次开始README SHA f718c96177d4b8066eea67d8994645313990d69748f0f01c3e4cd69446f8fbe6，原window与tool-output4分/CE5分完整行、999chars连续最初§4，以及此前已通过的完整CE§4均保护。原§19–25有效DAY/FINAL与Source分层复用；旧完成标签不代理TEQUILA必要研究/恢复DAY。只own本日README/作者_sources，Feynman独核文件不写，Books/State/index/scripts只root协调，当前无锁，不stage/commit/push/UI消息/模型覆盖。

## 2. 原事件与准入，准备即供独核

Feynmanfresh§26实际原[AngelSlim News](https://github.com/Tencent/AngelSlim)25/09/26 released TEQUILA、真实Paper2509.23809/Code同owner tequila/TernaryQuant及精确v1完整题摘/当前说明轻查已通过事件/窄准入，作者actual读回直接复用。**Sep26算法release，不是Sep28 Submitted/arXiv first，不要求额外TZ/同PDFbytes/globalabsence。** 原十作者/精确v1方法只作该release研究的必要后续稿补证，不能宣称paper在Sep26已公开或current分支全是当日实现。

原ternary QAT零区权重仅经近似STE路径学习→deadzone权重同时提供input-independent bias与原ternary路径→改变低bit训练/导出算子身份与质量/资源取舍。这个真实接口增量而非机构/名字/ARC倍率支持准入；拟评分2+1+2=5只该局部operator/训练路径，待Feynman评分核，不提前授Books。潜在唯一owner INFER-TENSORRT-LLM/Ch49，实际承载/邻接比较下一步，不因能映射就称新gap或已有覆盖。

## 3. 必要v1方法/正确性范围

actual[精确v1 HTML](https://arxiv.org/html/2509.23809v1)§2/Eqs1–3、§3.1/Eqs4–6与§3.2/Eqs7–8：ternary-grid/scale阈值定义deadzone D；signed-minima分支仍有input-sign/STE与在线算子成本。TEQUILA改为训练中随W/D变化的bias C(W)=Σ_D lambda*w，forward原ternary算子加C，deadzone surrogate梯度含输入路径和lambda直接路径。**新增bias路径可微不等整个混合QAT完全无STE，D的阈值切换/quantizer近似也不消失；作者“trapping-free/stable escape”不授普适收敛证明。** 对称activation只作为作者设计动机，不证明input-sign分支与input-independent bias数值/语义等价；这里是替代训练分支而非无损转换。

§3.2先说per-weight可学习lambda_i，§4.1/消融又用固定lambda默认1e-3；不拼成统一全部lambda已训练recipe。本文只采用辅助bias/混合梯度与导出职责，精确训练超参数/边界导数若需要采用再以必要原实现定点核。未访问全部权重/实现，不假设所有tiny weights应复活或全层训练必有收益。

AppendixC/Fig7实际读：离线将每三ternary权重编码4bit index＋1bit sign，另保存channel-wise预计算bias；在线输入分段建LUT、索引/sign与累加后加bias。**理论log2(3)约1.58bit不等这份5/3bit packing，channel bias/scale/LUT与全部模型资源另付费**；只有部署artifact保留C/scale/布局且kernel实际消费时才是这条算子，不能只保存三值码丢掉训练补偿。该paper方案不授TensorRT/GPU/任意CPU已经支持，未核kernel执行/生产SLO或复现。

## 4. 实际评价/强反侧

actual§4.1–4.2/Tables1–3/InferenceEfficiency/ablation与lambda/granularity必要文字：Llama3.2-1B/3B，UltraFineWeb10B tokens、group128、16H100训练、seq1024、lr1e-4、defaultlambda1e-3；lm-eval0shot。Table1含GPQA/Table2删GPQA，平均人口不能混；五benchmark称ARC含两切片，不把六metric列冒六独立bench。

Table1的1B ARC-e .645/.654BF16与ARC-c .305/.313差分别.9/.8pp，支持该切片接近FP；但3B ARC-c TEQUILA .346低于TWN .351，BF16 .422差7.6pp；ARC-e .702对BF16 .745差4.3pp。1B WinG .542对BF16 .603仍有6.1pp差，GPQA .232低于DLT .277。**平均改善不等所有列胜出/任意3B<1pp或通用>4pp**，明确只采用表中局部结果。

Table2不同尺寸/10B或100B、部分复现和公开weights/论文数分账，不做同预算单因果：3B Tequila avg.576对Spectra3.9B .567，但HelS/PIQA/WinG .464/.739/.627低于Spectra .483/.744/.631。Table3 per-tensor .463、per-channel/per-group .471，正文per-token与表per-tensor用词不同，不发统一无损granularity保证。消融只1B/ARC-e作者图趋势，lambda太大bias支配/太小无效，lambda0退原ternary；不授参数任意鲁棒/保证摆脱零区。

CPU速度仅Intel8263C、0.7B/3B因BitNet编译限制、二者LUT实现对BF16；与质量表1B/3B不拼统一模型/同quality3x。本文<.1%附加bias成本只是该实现作者测量，不证明所有E2E零开销；完整batch/concurrency、input/output latency协议、threads/cores、SLO/seed/置信区间与全部精度配置Not Disclosed。训练16H100不变成CPU生产验收。本文caption/convergence/ablation figure引用有编号错位，未据错位读数或宣称独立复算。

## 5. 即时准备范围与普通下一步

事件/窄P按Feynman§26有效层；本包必要v1方法/评价与强反侧、5分提案已准备，供root内部立即转Feynman，不等重复十四源或全日报研究。作者继续具体Ch49 owner/邻接与原release适用域必要比较；没有新Books锁/正文/注/POST，不能由Source提案预签Books。精确实现只有必要接口需要才定点恢复，不遍历仓库/版本/权重。尚未TEQUILA Source独核/评分、恢复DAY/FINAL或root接纳，当前55不预增。

## 6. Source实际通过与唯一owner PRE范围

2026-10-13T17:46:22+08:00已actual完整读Feynman§27–28：必要Source、正确性深入域、2+1+2=5及唯一Ch49具体gap提案通过；§5是当时快照，不再要求重复Source。root也已实际接受具体缺口与最多两段的提案范围，但**尚未发写锁**，本节仅保存PRE，不是实际Books写入/POST或恢复DAY。

作者fresh实际读PROJECT_CONTEXT/学习理念/写作指南、完整ROADMAP/最新State与Ch49 QAT1026–1067完整邻接、本章开篇/小结，以及Ch48 speculation交接与Ch50 request/worker开篇。唯一owner `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)。现有首段解释PTQ/QAT及fake-quant，后两段审latent→codes一致性，pQuant是额外高精度FFN/router，后续ternary条件加减是执行表达；均不承载同deadzone latent形成输入无关C、保混合梯度并导出channel bias的这条链。Ch48/50不接管量化算子形成，不新增owner/收纳小节。

实际写前保护快照：Ch49 unstaged为空，cached为**既有其他任务20add/0delete**，完整diff实际读回，包括LayoutAlgebra/CompileMask/RAMP/VecAttention/DualQuant正文与各自身notes，均非本任务。本次拟只在以下两个完整锚点之间插入两段，章末只加一条自身Review note，不重排/覆盖/格式化原QAT/export/其他正文或notes；锁到达后再读dirty与完整锚点防并发。缓存20行不能归本任务，也不stage/unstage/revert。

前锚完整段：

> Post-training quantization（PTQ）从已有 checkpoint 出发，在训练之后选择网格、校准或做局部重构，避免重新执行完整训练；quantization-aware training（QAT）则在训练/微调中让 forward 感受到目标 Q/DQ 误差，并通过相应梯度近似调整参数。前者准备成本较低但可能无法恢复敏感层，后者支付训练数据与优化成本，也不能保证任意低位宽都满足质量要求。两条路线最终都要导出具体格式、scale、图与 kernel 可消费的 artifact；训练中的 fake quantization 不等于部署时已经在运行低比特指令。[TensorRT 工作流文档](https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/quantized-types-workflows.html)区分了这两条准备路径与显式 Q/DQ 图。

后锚完整段：

> QAT 的在线 forward 还不能替代导出验收。高精度 latent 刚跨过 ternary 阈值，保存时的 bf16 cast 可把它送回原舍入格；scale 重算与 ties-to-even 也会改变代码。因此应保存训练后端实际产生的 codes，逐坐标比较部署 codes，再分别验输出格式和任务结果。换后端重算量化器未必复得相同代码。

## 7. 两段拟正文与单条自身note，供Feynman实际PRE

以下仅PRE拟稿，**未写入Books**。root内部可立即转Feynman核此实际两段/邻接与必要采用命题；原事件/Source/评分§26–28不重。通过后仍需root发明确owner/范围窄锁，才实际apply_patch；实际写后本人顺读正文/完整局部邻接及自身注，再由Feynman非writer实际POST、root接纳释放锁，不预支结果。

普通 ternary QAT 用高精度 latent 更新三值权重，零区在 forward 中仍输出零；保留这条简单量化路径，在质量足够时可以避免辅助状态。当零区更新成为瓶颈时，一条替代训练分支让这些 latent 同时形成输入无关的残差：设线性层权重 `W` 为 `m×n`、输入 `x` 为 `n` 维，量化器按所选 scale/阈值确定第 `j` 个输出通道的零区索引集 `D_j`，以辅助系数 `lambda_ji` 定义 `C_j(W)=sum_{i in D_j} lambda_ji*w_ji`，得到 `y_j=sum_i Q(W)_ji*x_i+C_j(W)`，输出仍为 `m` 维。固定零区成员时，辅助项提供直接梯度路径，但原 ternary 路径仍用 STE 近似；阈值切换及 scale 选择不因此得到真导数或普适收敛保证。输入近似对称也不使这一分支与含 `sign(x)` 的补偿逐输入等价，它改变了待训练模型，而非无损折叠原算子。[必要机制与边界](https://arxiv.org/html/2509.23809v1#S3) <!-- source-family:SF-2025-ARXIV-2509-23809 -->

这个辅助容量也必须进入部署 artifact。训练中 `W`、零区与系数可能改变，只有冻结最终配置后才能预计算逐输出通道的 `C`；导出需共同保存三值 codes、scale、该 channel bias 及 packing/layout，并让匹配的 consumer 真正加上 `C`，不能只导三值码而丢掉训练分支。低位权重的理论信息量不含这些元数据、activation LUT 构造和 bias 加法，论文的 CPU LUT 路径也不证明 TensorRT 或其他 kernel 已支持它。辅助强度/阈值选择与训练有成本，过强的 bias 可能支配输出，局部质量改善不能保证每个任务或端到端净收益；应分别验任务切片与实际存储/执行费用，失配时保留普通 ternary QAT、敏感层较高位或原高精度方案。下面的 codes 导出一致性检查仍适用，但不能替代这份完整算子身份的验收。[导出职责与有限对照](https://arxiv.org/html/2509.23809v1#A3) <!-- source-family:SF-2025-ARXIV-2509-23809 -->

拟自身末Review note（实际写入时才填真实锁/写后顺读状态，不照抄未来结果）：`SF-2025-ARXIV-2509-23809`；Daily2025-09-27补Sep26原算法release，精确v1§3.2/Eqs7–8、§4/Tables1–3与AppendixC，2+1+2=5，具体QAT算子缺口深入；仅deadzone latent输入无关C/混合梯度与联合导出，非全STE消除/逐输入等价/一般收敛/零成本或TensorRT支持。保lambda/阈值选择、质量反退与CPU/质量人口分责；未核实现、复现或生产SLO。Source Feynman§28已通过；PRE/锁/actual写/非writerPOST按实际发生分别记录。

## 8. 实际PRE§29与root窄锁写后包，立即供非writerPOST

2026-10-13T17:52:32+08:00已actual完整读Feynman§29：本包§6–7两段/完整锚点/自身单note的具体PRE通过。root随后actual读回并明确授唯一 `INFER-TENSORRT-LLM` Ch49窄锁，范围仅首PTQ/QAT完整段后、原“QAT 的在线 forward...”之前插入已审两段，以及章末自身单条SF note；本消息锁延续至root实际接纳非writerPOST后释放，**当前仍持有该锁**，无其他owner/正文/注写权。

写前即时实际读dirty、完整两端锚点及末注：unstaged为空，cached原20add/0delete及全部2026正文/notes保护。按apply_patch真实插入§7两段及自身单note后，实际顺读Ch49 1030–1056的完整局部（前Fisher段、PTQ/QAT首段→新两段→原online-forward→ternary-export→S²D/pQuant/后续执行交接），及末六行含其他notes与自身注；原在线forward/export全文没有改。第一段的m×n/n/m和D_j/C_j保持；第二段输出channel bias导出身份及元数据成本自然承接原codes一致性审计，两种验收不互代。末note只记录真实Source§28/PRE§29/窄锁actual写/本人顺读，明确非writerPOST尚未发生。

实际限定QA：Ch49工作区相对index仅**6add/0delete**，两段与§7拟稿逐字相同、两正文SF marker/自身note各2/1；当前cached diff全文与写前快照逐字相同，原20行是他人修改，不归本任务。限定cached及unstaged diff-check通过，未改其他正文/notes/owner/State/index/scripts，未stage/unstage/revert/commit/push。本人CLI均实际结束。

**此单篇实际写后包已准备，请root内部立即转Feynman actual非writerPOST，不等日级或其他新包。** 直接读Ch49实际两段/完整邻接与自身note、核本节限定范围；Source/5分/原事件/具体PRE未变层不重。当前55/132不增，不预签POST/锁释放/恢复DAY/FINAL。报告此前已仅归并本家族Source/5分与待落实Books为进行态：V3通过、14DailyID、原窗口/原两完整候选行/完整既有§4冻结True，报告＋本包25本地引用/19唯一路径无缺失；报告新增正面Source不改变旧十四源安全终态或134/CE/撤回架构有效层。

## 9. 非writer实际POST§30已通过，待root接纳/锁释放与报告变化层

作者actual完整读回Feynman§30：真正顺读Ch49完整1026–1064局部/末own note及此前notes后，非writerPOST通过；两段逐字等PRE、输出C/混合梯度/非等价/成本/回退和实际邻接有效。Source§28/PRE§29不重复，未授恢复DAY/完成态FINAL或root计数。root尚未接纳并宣布释放锁，作者仅行政同步自身note真实POST§30指向，不动两段或其他正文/notes；当前窄锁仍按root授权保留，不能自己释放。

日报六部分已仅整合TEQUILA原事件/正式5分/必要Source与具体owner实际写后范围，不重十四源/134/CE/撤回架构或原DAY/FINAL。请root实际读回本包§8–9、Ch49两段完整邻接与自身note接纳POST/释放锁；随后内部转Feynman当前六节只做本项报告变化层恢复DAY及保存完成态FINAL。准备单篇不等待其他新包，不增范围/未知日全文。当前55/132、77待验，不预增，未stage/unstage/revert/commit/push/UI消息/模型变更。

## 10. root实际接受POST并释放锁，六部分变化层恢复DAY包

2026-10-13T17:55:16+08:00 root已actual读回Feynman§30、Ch49真实两段/完整1026–1065邻接/自身末note与6add0delete及限定diffcheck，明确接纳非writerPOST并释放Ch49窄锁。仅按该明确权限行政同步自身note真实POST§30/root接纳释放，不改正文/其他notes；§8–9待POST/锁释放是发生前快照，当前没有任何Books锁/待写/待POST。

README当前六部分已融入正式TEQUILA第三家族/5分、原Sep26算法release角色、必要精确v1方法/评价反侧、具体Ch49两段实际整合1及真实POST/root接纳；原14源/134/CE/withdrawal架构/旧DAY及FINAL有效层保护。原两完整候选行/小时window与完整既有§4冻结，新增证据标题与候选完整原题同，未扩任何队列/日窗口/owner。报告状态保持进行中，因为本项恢复DAY及保存态FINAL尚未发生；原数55/132、77待验不增。

**六部分受影响差额已保存，请root内部交Feynman actual恢复DAY；只读当前真实六节及本单项Source§28/PRE§29/POST§30/root释放有效角色，不重未变Source/旧池或另日。** 真DAY后仅状态/时间/已发生指向与QA完成态同步，再actualFINAL，之后才root计数。本人不预签本项DAY/FINAL，不结束连续授权或等待新用户授权。

保存后实际QA：V3通过；正式3、14唯一DailyID、原window/原tool-output及CE两完整行/完整既有§4前缀冻结True；README与本包25本地引用/19唯一路径无缺失。Ch49当前cached完整diff仍逐字等锁前20add0delete，own unstaged6add0delete；正文两段逐字等PRE，只自身note行政更新真实POST/root释放。限定上述Markdown cached及unstaged diff-check通过，不声明全raw目录/仓库clean；没有未结束本人CLI或共享锁。变化层DAY准备完成不等真实DAY，当前55不增。

## 11. 仅AngelSlim新增来源行过期尾句修正

root实际读17:55六节后指出新增来源行末仍沿用“具体Books PRE及实际写后核仍普通待办”。本次仅将该新增行缺口尾句改为具体PRE§29/actual非writerPOST§30已通过、root已接纳释放锁、当前无Books锁/待办；保未核代码运行/复现/生产SLO及原release/后续v1权限边界。旧十四来源行、历史2/0快照/原§4、Source/POST与其他字段未改，不重研究或申请新锁。

请root内部转Feynman读取最新这一行行政差额即可，不重复Source/PRE/POST。作者已实际读到Feynman§31恢复DAY保存结果，但按root本条仅来源行修改权限未同步完成状态/时间/§1/5/6，未预签保存完成态FINAL或root计数。当前55/132不增，所有旧有效层保护，未stage/commit/push/UI消息。

## 12. 实际DAY§31/root接受后保存完成态，供actualFINAL

2026-10-13T18:03:27+08:00 actual完整读回Feynman§31含来源尾唯一差额随后读回，以及root实际当前六节/独核§31接纳指示。仅行政同步README status完成/time/§1/5/6真实DAY§31已通过/root接纳、普通研究/Source/Books写/POST0与actualFINAL尚待；新增来源尾§11已修，不再改§2/3/完整§4或Books。正式三家族合同分类为仅报告1＋已有覆盖1＋整合1，原provider row不变，不以两NoChange统称替换分类。

**已保存完成态，请root内部转Feynman actualFINAL只读本次行政差额/冻结/refs/限定QA，未变Source28/PRE29/真实POST30/原14源/134/CE/withdrawal/DAY层不第三审。** 当前55/132、77待验不预增；真实FINAL/root接纳之后才fresh已有Dec03，原September范围不再研究，未接纳不跨日。当前无Books锁/未结束本人CLI，所有protectedcached不动，未stage/unstage/revert/commit/push/UI消息/模型覆盖。

保存完成态后实际QA：V3通过；§2/3/完整§4与本次行政写前逐字相同，原window/原两完整行/本项恢复前全部§4前缀冻结True；14DailyID、正式3，分类仍仅报告1/已有覆盖1/整合1。README＋本包25本地引用/19唯一路径无缺失，限定两作者Markdown cached/unstaged diff-check通过。该QA不代actualFINAL，未重跑Source/Books/旧42tests或声明全raw目录passed。
