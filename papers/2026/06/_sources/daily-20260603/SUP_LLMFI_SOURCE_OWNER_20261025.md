# 02430 LLMFI：必要证据、六分与执行保护预算小gap

仅2026-06-03补Jun02。当前AGENTS/Research/Report/适用Sources/Prompt/ROADMAP与本日停点已恢复，Books公共上下文沿同日有效读取。MODEL具名四定义的完整题摘/准入/联合日证及其已成校准有效复用，不第三日期。当前[官方abs](https://arxiv.org/abs/2606.02430)唯一v1、ICS26 accepted，所见无撤回/勘误；接受/会期不是另一个已证正文首发。v1 Jun01 16:04:51Z不单独当公告日。本项研究LLM数值执行容错，HPC动机不使其变暂缓的科学领域应用。

## 必要原证与采用边界

实际读[exact-v1 HTML](https://arxiv.org/html/2606.02430v1)§3.1–3.4、§4.1–4.2/T1–3、§5.1–5.2/5.4、§6.1–6.4/T5及直接图注/文字；首次长输出在§5.4截断已定点补全。未读无关MoE/全部多bit案例、图像像素、代码或复现。只采用分阶段/算子/位表示的保护预算与质量取舍，必要支持和直接反侧足即停，不收全部17条headline。

forward hook扰动activation模拟computation fault，pre-hook扰动weights模拟memory fault；主试验每trial单bit，不代表真实GPU故障分布、每资源ECC行为或故障发生率。Scheduler与wrapper分开定位prefill/first-token/decode，额外forward隔离first-token，greedy消除采样分支；greedy本身不证明所有kernel/GPU逐位确定。单bit在不同stage/site/bit index的结果可比较，但stage的实验边界需随wrapper记录，不能把额外重复计算当线上原生免费阶段。

Phi3.5mini/DeepSeek7Bchat/Gemma7B、13任务，主A10040GB/Ubuntu20.04/CUDA12.3/PyTorch2.6/Transformers4.40.1，主FP16/greedy、任务各自fewshot与CoT。按model/task配prompt，gold与fault固定同设置；完整max长度/并发、注入总样本与每项重复CI未在所读采用域闭合，不补全。约3000GPUh只作者研究规模，不是部署开销。Wrapper 10–15%局部开销与最终保护策略费用不是同一物。

§5.1末层/down-proj更敏感、扩维算子较稳与§5.2早期及特定语义token敏感只是被测人口下的观察。不能从维度扩大推出任意线性映射必收缩误差：自己的反例是扩维矩阵按大系数复制，误差仍可放大；层/权重/故障位置共同改变，不采用作者“维度本身解释全部自纠”作定理。§5.4 exponent14较危险和不同dtype恢复排序只属于相应单bit模型，不给BF16/FP16一般质量或真实故障率排序。

§6.1 Phi down-proj局部INT8量化/反量化提高故障下准确率，却使无故障ARC85.20→84.39、BoolQ84.00→82.93，不能无代价改精度。§6.2选择o/down类GEMM checksum，coverage定义为恢复故障诱发的accuracy损失；保护约三成workload是相对全保护的GEMM FLOPs代理，不是实测30%时延/带宽/全部故障检出概率。Checksum另有读写和数值/相消边界，作者未证明该选择对全部算子/模型最佳。

§6.3共享KV复算首token并比较，测82.20%coverage/TTFT+3.37%只所测fault人口；共享KV已坏可让两次一致，重复一致不认证正确。须另核prefix/KV/position完全同一与独立故障域，不把图示直接当可运行cache recipe或sampling保证。§6.4多shot只有限改善，过长亦可退，最优动态policy明确未来工作，不补成已部署controller。所有注入/profile、量化转换、checksum、额外forward/比较、重试与质量/请求回归计费；真实故障模型或质量不合时，保名义精度、原ECC/冗余和精确重算。

## actual owner与最小PRE

拟Design Delta2 + System Reach2 + Durability2 = 6：不是发明checksum，而是按LLM阶段/算子/数值表示定保护预算，再联合无故障质量和共享故障域验收的选择；不借17条takeaway或HPC名称加分。真实小gap深入受影响域。

实际完整读Ch49数值执行确定性/因果prefix组、DRIFT两段、Hardware Fault Recovery的RangeGuard完整两段。DRIFT已说明diffusion近似恢复/计算fault与memory无错假设，RangeGuard已说明张量范围/bit-exact与bounded恢复；两者未具体讲自回归stage/算子敏感性决定选择性保护、无fault质量和共享KV重复检测的责任分账，不以旧一般profile或marker硬NC。唯一`INFER-TENSORRT-LLM`，Ch48与50既定proposal/engine开篇职责复用，Ch66拥有评价合同而不另重复执行机制。

拟位DRIFT完整第二段及2604.09073 inline marker后、数值计划Attention统计分工完整首段前。只原单段+真H2本人注，待独立必要/正式分/actual gap/PRE；未写Books/Report/State/index，不预I/DAY。

## 原单段PRE

自回归执行的保护预算还可按阶段和算子分配，而不把所有张量同等冗余：[受限的LLM故障注入](https://arxiv.org/html/2606.02430v1#S5)在固定故障模型下看到首token、部分后层与投影更敏感，据此选择精度转换、局部checksum或重复首token。它支持先profile再选择保护位置，不证明扩维必然自纠、某dtype普遍可靠或重复一致即正确；共享KV已损坏时，两次首token仍可一致。更稳的故障下分数也可能牺牲无故障质量，保护GEMM的FLOPs比例不等实际延迟。阶段定义、fault人口、dtype/site、prefix/KV身份与真实质量必须共同验收，并计转换、校验、重算和重试费用；故障域、质量或检测资格不合时，保名义精度、完整ECC/独立冗余与精确重算，不由局部coverage批准全服务无错。<!-- source-family:SF-2026-ARXIV-2606-02430 -->

## root实际采用

R172首次必要/六分/actual owner与原单段PRE通过后，root在Ch49 DRIFT完整组后/Attention统计组前实际保存，R174唯一actualPOST通过。Report与本人注已行政采用，指定位I生效，无日级完成或新增保证。
