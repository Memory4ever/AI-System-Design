# 六项已校准材料的必要证据停点

各项精确v1，身份/公开批次仍由本日日期记录处理，不把方法阅读等于当窗候选冻结。支持与直接反侧已实际读；未运行代码/未复现。标准项5=2+1+2，10254=2+2+2；后续确认书稿长期差额才深入受影响命题。原源见 V3_EVIDENCE_<ID>_INITIAL/EVAL（10254全部核心在INITIAL）；普通待办不是blocked。

## [ELROND 2602.10216v1](https://arxiv.org/html/2602.10216v1)

§4 Eq1–7：同prompt stochastic image pairs，noise reconstruction差反传到concept input embedding，再PCA/TopK-SAE分解，方向注入该token。§5：10k images/30k梯度每concept，最高noise层；SDXL/DMD主对照，teacher-FID与等norm随机方向DreamSim控制支持可操纵局部生成，不证明真实概念manifold切空间、SAE dictionary density等于语义真分布或“无条件precise”。Table1 Monster PCA107.46 worse than DMD103.95、SAE99.63有限改善；不要漏直接反侧。§6反传数千pair成本、方向不可解释与影响其他subject。Hardware/precision/batch/concurrency/SLO Not Disclosed，输出图像不存在LM输入输出token长度。本文SDXL描述CLIP+T5不正确的架构说法未采用，不补造实际实现。

Books Ch24 140–154 actual已有 frozen-generator conditioning intervention、方向/位置/幅度分责、subspace≠semantic disentanglement、局部代理与成本边界。新梯度发现recipe尚不能证明正文所需的语义/分布恢复主张；拟 **仅报告**局部工具验证，非“该具体算法已有覆盖”。需root核此处置是否仍有具体长期缺口；无写。

## [LT-Tuning 2602.10229v1](https://arxiv.org/html/2602.10229v1)

§4：训练label token confidence低插thinking控制位，原hidden作为latent初始化，再fusion αhidden+(1−α)top-p词表预测embedding；1/3B tied、8B untied另adapter。§5/Table2 8B without fusion45.3低于without latent61.6，full68.8/adapter70.3；但不同模型tied属性不是同架构单独干预，不将退化全归因untied。PCA20samples×6latent只是readout，不能证明因果collapse；100samples entropy/attention亦非忠实推理认证。A/B实际训练1B/3B1+2+7epochs、8B1+1+3，4×A10080GB，各尺度LR/batch变化。四arithmetics任务，未披露完整token/FLOPs同成本或实际wallclock，不把少visible token称Serving加速；无多seed显著性一般保证。

Books MODEL-DECODER-ONLY Ch18 268起已经latent-state recurrence/teacher/termination/可读性边界，但没有“直接hidden回灌的输入输出interface mismatch，context+vocabulary projection再融合，poor latent可弱于不用”的具体条件。拟窄补机制分支；需root必要Source+差额核后再深入适用identity/邻接和请求Ch18锁；不是当前整合通过。

## [Audio temporal frame tool 2602.10230v1](https://arxiv.org/html/2602.10230v1)

§2 finaldecoder audioframes→数值head→postprocess timestamps，40msgrid。同QwenOmni3B/7B数据/条件finetune token baseline，4×H100。§4 Table2单事件Poisson通常更好；Table3多timestamp质量近似相同且部分桶反退。Table4未见timestamp ranges提高支持固定受测audio-grounding vs memorized秒数，不授无限长度/物理时间准确性。Fig3最高60×不等于跨桶平均最高约5×，runtime按长度/batch变化；完整concurrency/SLO/precision Not Disclosed。

**直接公式反侧**：§2.2 Eq4是conditioned-on-count密度，Eq5相应n logΛ；紧接n=1段却写−logλ+Λ（非其前式−logλ+logΛ）。不给该exact loss统一理论证明，也不因错误删除已准入的内部frame接口证据。作者把IHP说成时刻dependence替代binary不自动给任意事件dependency保证。采用head接口/局部评价，数学处保持争议；必要PDF/代码若只为确定实现loss仍是定点待办，不要全附件。

Books MULTIMODAL-REPRESENTATION Ch23 585–623 actual只有timestamp token、真实clock/provenance与temporal-probe；没有finaldecoder frames直接数值定位且避免AR timestamp generation这条分支。拟窄补接口而不写有矛盾的loss或universal速度。需root支持/反侧核，确认是否需精确实现loss才采用。

## [Blockwise advantage 2602.10231v1](https://arxiv.org/html/2602.10231v1)

§4 block目标只作用自身tokens，mean-by-block-length；后blockprefix不同，OCB把正确/错误outcome bins复用现有group均值，不nested rollout。AppendixB只有outcome充分捕获prefix conditional value时其baseline才可无偏；同组含自身reward还不自动给unbiased policy-gradient，**不授一般无偏更新**。§5 100Math500 prompts×32confidence continuations MCreference；same25kMATH/DAPO、prompts/verifier/hyperparams/parser control。OCB不是全面最优：7BBaseAIME AUROC .902 vsRLCR.942，ECE.126vs.092；训练组更大但同batchunique题减半，ECE较好不必质量较好。bf16，G32、batch2048/trainsequence4096，512/1024steps；evalvLLM.10 n16/T1/max32k，SEMbootstrap不等多seed训练稳定性。Hardware/完整成本/SLO Not Disclosed。

Books TRAIN-GRPO Ch33 1620–1675有 typed block credit原则，但not OCB conditional-sufficient-outcome baseline与same-group bias约束；2512的来源链接不是正文承载。拟最小补“prefix值不能被prompt baseline代替；粗outcome仅近似，分箱充分性/小bin方差”一段。需要root实际Source+差额，不从citation宣布已有覆盖。

## [MoE PIM KVGO 2602.10254v1](https://arxiv.org/html/2602.10254v1)

§III sharedperipherals引contention，offline workload-sorted专家配对+prefilldata-reuse idle/reschedule；expert-choice的topKgate scores/outputs缓存。§IV单LlamaMoE4/16layer operator simulator/HERMES256²8bitIO，PajamaC4 trace，32prompt/8–64output；scheduler latency/power省略，MoE线性cores area不含digital/DRAM。3.20×/4.92×不是实芯E2E，normalKV省latency可能增加DRAMenergy；compact schedule energy可能退步。

关键正确性边界：expert-choice回看历史topK不是causal每token fixedroute；原source声称只缓存k结果无质量退化，未给完整输出semantic-equivalence对照，不能批准一般decoder past token更新语义。Books MODEL-MOE Ch21 450–461 actual已写batchexpertchoice依batch其他token不适causaldecode、population cutoff替代；与本文缓存路线非同机制。拟 **仅报告模拟方案**，不把欠缺decoder equivalence/area completeness的hardware数字作为长期可执行设计；需root确认反側+处置。不存在代码或硬件实测采用。

## [Power-SMC 2602.10273v1](https://arxiv.org/html/2602.10273v1)

§4–5/AppendixA：prefix-onlyproposal q∝p^α唯一消除token-choice incremental weight variance，剩余prefix path差异仍退化；不是temperature alone得到全序列power分布。ESS祖先重采样需prefix/KV/done一致重排；有限N64不能称精确independent global target draws，EOSabsorbing有max2048截断。§7 sameHF stack对MH、3models/MATH500；reported别人的ScalablePowerSampling2.5–3.5×明确不是本exact stack。τ=.25、α4、N64/ESS.5/ramp100，inputlength/hardware/precision/SLO Not Disclosed。Costmodel explicitlyNTtoken-evals，wallclock优势由batch利用率，不是总compute减少。

Books MODEL-SAMPLING Ch20 318–336 actual已有power sharpening可能损pathsupport与coverage/selection，但没有“逐token温度vs全sequence目标，局部proposal+importance weights+cache-safe ancestry”机制差额。拟窄补这条分布语义与runtime分责；root源核后再补必要EOS/finite-particle边界和requestCh20锁。当前未写。

待办：各拟整合命题必要深入及root源/Books核、精确落窗与非作者实际POST；没有把本页当作已完成收据。

