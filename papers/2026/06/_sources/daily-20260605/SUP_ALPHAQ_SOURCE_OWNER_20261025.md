# AlphaQ：首次必要Source / actual owner / 最小PRE准备

## 身份、采用层与真实读取

仅Daily2026-06-05补Jun04自然日。`SF-2026-ARXIV-2606-04980`，[AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization exact-v1](https://arxiv.org/html/2606.04980v1)。R33–36的完整题摘/准入与Jun04联合日期有效复用，不第三AB/date，不混未来版本。官方HTML真实GET200、472815bytes，保存`SUP_2606.04980v1_20261025.html`。本次实际读§3.1–3.3/Eq1–5、§4.1–4.5/T1–6及A.5–A.7/A.10–A.12的直接支持与反侧；§1–2背景只作问题定位。未展开全部上游HT-SR证明、全部A.3/A.4/A.8/A.9、全代码/实现或复现；所采有限接口不依赖这些可选层。A.11是必要的分配/部署分责核验，不据其扩执行研究。

作者建议评分2+2+2=6，待首次非writer必要Source/actualowner/PRE：谱代理×误差代价的全局分配接口，在校准人口不稳的MoE下提供明确替代机制；跨weights/bit-map/quantizer/runtime的边界有长期意义。不因HT-SR既有原理、MoE标签、能映owner或headline倍率加分。已准入不自动I；尚无Books授权/SAVE/本人注/POST/I。

本地官方原件SHA256：`2046adc084cc8a44077015188347dc34d0b93aeb72975a8adae5157d22532149`。

## 必要机制与支持

§3中layer指projection matrix，不等Transformerblock或整个expert；一个expert含up/gate/down等矩阵。以`WᵀW`谱的尾部Hill估计得到PL_Alpha_Hill：较小alpha表示较重尾，被作者用作更高重要性的结构代理；fix-finger在ESD峰附近定尾、FARMS固定子矩阵采样减弱不同aspect ratio的比较干扰。§4.1用256×256子矩阵、两轴stride256。它是经验重要性提案，不是权重谱天然决定任务真值或router行为的定理。

§3.3/Eq4将权重方差乘`2^(-2b)`作为位宽误差代理，再乘alpha的重要性映射；Eq5每个目标矩阵只能选{1,2,3,4}之一，最小化这些代价之和，约束`Σ N_l b_l ≤ B_tot`。目标中没有额外N_l加权，参数数目在预算中；不要把它静默改成参数加权误差目标。ILP的全局最优只针对所列离散候选/可加surrogate，不推出真实accuracy degradation全局最小。它不按activation/routing frequency分重要性，也未把router路径改变计入这一代理。

§4.1实际后续是group128 asymmetric GPTQ，用128份WikiText2样本校准；attention/router等non-expert统一4bit，expert矩阵混1–4。脚注与A.12明确calibration-free仅指bit-allocation，不是整条PTQ免样本/免域偏差，更非activation分配已验证。报告2.5/3.5是MoE block内layer bit的平均描述，不能写全模型所有参数同位宽；Eq5参数加权预算、文中不加权layer平均及包括non-expert/metadata的物理bytes必须分开核。Uniform的x.5又是前半blocks x+1、后半x，非每个矩阵原生fractional格式。

T1四MoE、WikiText2 PPL与五项zero-shot平均只支持有限质量取舍：Mixtral2.5平均70.76高于PMQ70.38，Wino却73.24低于PMQ73.95；Qwen1.5的3.5平均68.04近/高BF16的67.93，PPL7.38仍劣于BF16的7.22。T2 OLMoE跨域分配对照不证明各域/各任务均优，AlphaQ平均28.86仍低BF16的35.29，MMLU44.75低于一混域PMQ44.79。T3另六任务OLMoE消融，Noise-only63.74低于Uniform64.73，Alpha-only66.23、direct组合66.81、ours67.11低BF1670.45；支持需结合重要性与数值扰动，不证明单指标/唯一因果或普遍最优。T4跨block与T5细化到矩阵的局部改善也不授任意granularity单调收益。

## 直接反侧、公式接口与执行权限

A.5逐次仅量化一个module到2bit、其余FP的PPL退化图是局部关联，点有离散；不能把单module关联外推为全network可加真实loss。A.6的`2^(-2b)`依赖均匀quantizer/固定clipping范围、高分辨率与近似均匀误差假设；在实际1–4bit下只是代价模型，不是严格error bound。A.7默认gamma由alpha端点与variance构造的局部判别代理匹配斜率，Figure11显示模型敏感性不同，不证明参数通用或零variance可直接除；后者未给可执行guard，不补造实现。

原文§3.3将tilde-alpha写median，A.7同符号写mean。原件保留这项精确口径差异，当前最小正文不复制该归一常量/完整gamma配方，也不声称已核实现消解。固定gamma时公因子不改变Eq5分配排序，这是有限代数观察，不替作者定义统一或证明整体算法/数值鲁棒性。无需为所采“importance×noise proposal”的边界扩全理论。

§4.5/T6离线alpha计算OLMoE180.28s/Qwen3 549.26s是准备费，不因不在线而免费。A.11 prefill使用HQQ式unpack/dequant+TensorCoreGEMM，expert decode另fused Triton；同一2bit Mixtral更换backend的token/s为6.43→9.84，GPU metadata caching再10.36，后者peak13418→14259MiB（+841MiB）。这直接说明执行收益并非分配器单独带来、metadata常驻另付费。A.10中Mixtral2bit Uniform速度1.70×、AlphaQ1.69×，不采“所有frontier均支配”；§4.5写1.68×与表1.69×不合并成精确主张。作者称A40 48GB但表BF16参数96.8GB，未给该对照的完整placement/容量协议；prompt/decode长度、batch/concurrency、运行重复/CI、完整quantization/solver/packing成本及生产SLO未披露。保留作者条件，不推补offload或签净服务收益。A.12明确weight-only、广架构待验、GPTQ仍有域偏差、未比较全部方法。

因此所采仅是低数据依赖的**分配提案接口**及分配/量化/执行分责，不采结构重要性真值、跨模型无校准域偏差、真实任务全局最优、全模型同预算无损或runtime加速保证。支持和关键反侧已足，停止可选附件/全实现，不把未读外部化。

## actual owner与最小gap

本次重新读ROADMAP与三Books公共上下文；actual `INFER-TENSORRT-LLM` Ch49。实际读Ch49:1120–1184粒度/校准、ProbeQuant随机误差代理与静态/动态/weight-only、1386–1416 MoE calibration/analog/fractional、2010–2025 MoE全局误差预算；邻Ch48/50开头交接已读。既有ProbeQuant区分isolated估计/重构/分配质量、MoEQuant绑定expert activation人口与coverage、全局budget和physical layout亦已有，均保留，不以通用条件再造diff。

具体gap是：校准expert访问人口不代表部署时，**直接weight spectrum重要性×位宽噪声代理**可给projection-level全局预算提案，但分配阶段data-free不授后续GPTQ/data-free或router保证。这个替代入口及其假设没有被上述现文具体解释。故拟在MoEQuant完整覆盖段后/Analog CIM真标题前插以下两段，不改原body/marker/其他组；仅提案，待独核/root新窄授后才可SAVE。若独核发现已有同接口具体覆盖，接受NC，不为I造差额。

完整直接上锚（其后原end marker保留）：

> 因此 quantization artifact 除了 bit-width、scale 与 calibration corpus，还应绑定 router/expert identity、per-expert activation count 和覆盖阈值。Expert-balanced sampling 可以提高低频路径覆盖，affinity grouping 可以共享相近 expert 的 scale/kernel，但二者分别增加校准成本、grouping drift 与 layout complexity；统一 bit-width 在 expert 行为接近或证据不足时仍是更容易验收的 baseline。MoEQuant 的实验只证明作者模型族、数据集、bit-width 与硬件合同中的质量—内存结果，不证明所有 expert 都应使用同一策略，也不证明端到端 serving 必然加速。

其后真标题`#### Analog CIM 的 MoE 校准要同时修 Expert 与 Router`及完整直接下锚：

> 在数字执行上沿用 clean-trained router，只校准权重或 activation scale，默认噪声不会改变 expert 相对选择；analog CIM noise 会同时扰动 expert 输出和 router logits，进而放大 load imbalance。部署 artifact 因而需要把噪声模型、expert replacement、router calibration、placement 和 routing histogram 绑定在一起，校准器只能提出补偿，release gate 仍根据质量与负载证据决定启用。

### 拟逐字正文（尚未授写）

代表性 expert activation 难以取得时，位宽分配还可尝试不依赖样本的权重结构代理，而不取消后续量化校准。一个受限分支对各 projection matrix 的权重谱做固定尺度子采样，以尾指数估计重要性，再把它与权重方差、随位宽衰减的噪声代理组合，在参数加权的总 bit 约束下为每个矩阵选择一个位宽。它避开按校准路由频次直接排序，却把重要性判断交给谱尾假设；整数规划最优也只针对所列候选与可加代理，不证明真实任务损失全局最小。Artifact 应分别保存谱估计/映射、目标矩阵与 bit-map、预算及后续 quantizer/calibration 身份，不能只登记“免校准”。

[AlphaQ 的有限 MoE 对照](https://arxiv.org/html/2606.04980v1)中，仅噪声代理可差于统一分配，重要性映射的强度也因模型而敏感；高分辨率均匀误差近似在极低位宽下仍需任务回归。分配不读样本，不代表实验中的 GPTQ 不读样本，更不保证 router 或未见领域不受量化影响。谱估计、求解、GPTQ 校准、packing 与质量验证均付费；layer 平均 bits、全模型权重与含 metadata 的驻留 bytes 不能混用，decode fusion 与 metadata caching 的收益也不能归给分配器。代理失配、敏感任务或实际布局不合时，保留代表性/分层校准、统一或较高精度；最终质量与完整执行预算另验，不由分配目标签发无损或服务加速。<!-- source-family:SF-2026-ARXIV-2606-04980 -->

## 有界交接状态

04980首次必要证据/6分/actual Ch49最小两段PRE准备就绪，待同日fresh reader首次核，不预PRE通过/Books授权/SAVE/POST/I。04315已采用R59具体四组NC，累计I保持新增13＋旧Kimi1＝14。其余七04708/04463/04306/04104/04896/04364/04485必要层、有限相关官方标题stop及最终DAY仍ordinary；机构具名有界止点/重开条件复用，不全宽73/706配额。本阶段交root后释放作者槽，不等待其他Methods、不表示暂停或完成本日。未改共享Books/State/index/他日，无stage/commit/push。

实际保存后已读回本Source、README新增结论/候选行/§4/§5/§6及恢复入口；V3校验通过，README限定diff --check无诊断，三份本日新记录含untracked的no-index --check无空白诊断（比较有差异的exit1不是失败收据）。只本日README/原件与必要过程，无共享Books修改；机械通过不代首次语义Source/PRE或DAY。

## 当前R61–62已采用、root新窄授后真实SAVE，待唯一actualPOST

上节为首次独核前准备历史。现实际完整读回R61–62：6分必要Source/actual Ch49具体gap/原两段PRE通过，无修句，不第三准入/date/必要层。启动重读AGENTS/适用合同/Prompt、ROADMAP/三Books上下文、来源使用/Daily/arxiv/恢复、仅2026路由及当日本停点；actual位置、完整直接MoEQuant覆盖段/start-end binding与Analog CIM标题/完整下段及邻48/50入口已fresh读，确认本marker原来不存在。

root本轮明确新窄授后，批准两段逐字保存于Ch49原MoEQuant end marker之后/Analog CIM真实H4之前，实际1394/1396；本人一注在true-H2 `## Review notes`之下实际2678。已完整实际自读新增两段、完整直接上段/marker、真H4与完整下段及本人整注。第一段区分weight proxy与任务真值、参数预算与surrogate最优；第二段近文保noise-only反退/映射敏感、GPTQ仍校准、全费/physical预算/backend分责及回退，不借公式/容量缺口补造实现。原两侧与新段衔接成立，不改原MoE coverage或CIM router/release分责。

写前整章快照`/tmp/jun05-alphaq.ewk03b/ch49.md`，SHA256 `89f9e6c068ea5249c98d2de42cef6c900b42ddba7589ced0e5331020b7971184`。实际核对两段连续逐字恰一处、正文family marker唯一、本人注恰一处且最近前置H2为Review notes；移除仅这两段及本人注后整章与写前快照字节一致，未触其他正文/注/marker/在途修改。README/停点仅保存实际R61通过/真实SAVE-selfread待唯一actualPOST，未预I/DAY，累计仍新增13＋旧Kimi14I。其余七与有限标题stop仍ordinary。本就绪写入阶段交root即结束释放作者槽，不因等POST扩Methods；State/index/他日不改，未stage/commit/push。

当前行政同步：R63–64已实际读回，04980唯一actualPOST通过，整合生效/窄位释放；本人注与README/恢复已同步既成，新增I14＋旧Kimi1＝15。以上待POST为历史保存态，不第三Source/PRE/POST或更改已通过两正文，未授DAY。
