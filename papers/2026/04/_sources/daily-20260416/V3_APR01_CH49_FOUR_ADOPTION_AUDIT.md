# Apr16：Ch49 四项有限非作者采用复核

复核者：`/root/apr01`。本轮实际重读 AGENTS、统一入口、研究/Report 合同、每日来源及 ROADMAP 主线；读取作者提案后，独立打开下列官方 v1 必要方法、评价与反证，并对读 Ch49 当前正文及局部交接。仅复核拟采用命题，不审整日日期 Gate、不复现实验、不写 Books；source→owner 通过不代表已整合或日级完成。

## 13287：双代理剪枝

[官方 v1](https://arxiv.org/html/2604.13287v1) §2.1–2.3、Algorithm1、§3.3、Table3 实际读取。**窄缺口通过，6分知识缺口深入。** 当前 Ch49「两种稀疏性必须共享地址合同，却不必共享 Kernel」已有局部二阶 mask/annealing，却未解释重构与 training-loss/Fisher 两个代理的归一组合、共享输入基底与逐行低秩项。可在该节加入此分支；Woodbury 精确只针对声明的块近似且可逆基底，λ=0不能直接套同一逆。保留 attention-only 多目标、projection 仍重构、离线选择和质量反例；不采用一般真实 Hessian、全网最优或 serving 速度保证。

## 13319：读时重组与计算职责分开

[官方 v1](https://arxiv.org/html/2604.13319v1) §3–5、§6.1–6.3 实际读取。**窄缺口通过，6分知识缺口深入，但作者提案的 VU13P 配置需修正。** §6.1 实际为 Kria KR260/Cortex-A53、FPGA 300MHz、DDR4；不是 VU13P。Ch49「Execution Plan 先拥有 State，再选择 Kernel」现 FILCO 是片上 tile/view，尚未承载 CPU 保留计算、按 alias 地址与配置由 memory engine 重组 cacheline 的分支。保留 Conv2D 反慢、MatMul 主计算遮蔽变换收益、碎片导致底层完整 burst 放大；不外推 GPU/LLM。其原始必要笔记第187行的平台是准确的，尾部第363行应同步，不需重审全文。

## 13440：概率分布用于位宽选择，不是质量真值

[官方 v1](https://arxiv.org/html/2604.13440v1) §3/Algorithm1、§4.1 Eq1–6、§5.2、§6.1–6.2、§7.1/Table4 实际读取。**窄缺口通过，6分知识缺口深入。** Ch49「量化验收不能只看平均分」讲 drift/release 诊断，未讲逐层单独量化后以输出概率排序作 mixed-bit proposal。必须保留 KL 方向、teacher-law 与真实 test-law 的区别；正向恒等式不是反向 KL 经验排名的证明。Lunar Lake/OpenVINO 的 CPU/GPU 模型、支持算子与配置不同，不能据 QDQ/大小推统一低 bit 物理收益；长度、并发与 SLO 未披露。正文应把分配 proxy 与后续质量/执行验收接起来，不能写 KL 一般支配 SQNR 或 PPL。

## 13806：校准样本稳定性与曲率完整性是两条轴

[官方 v1](https://arxiv.org/html/2604.13806v1) §3–5/Eq8–11、Algorithm1、§6/Table1、§7.2 实际读取。**窄缺口通过，6分知识缺口深入。** Ch49「二阶敏感度把 Output Gradient 带进量化 Artifact」已有更完整 covariance/动态 residual，却缺有限样本中相关项降 bias 与估计方差相抵的反分支。可在该节补 diagonal 权重与固定离散 Q 时 ridge scale/offset 子问题、重新 round 的交替更新；闭式子问题不等全离散全局最优。Fig1 是 Llama2-7B 单层诊断，不能普遍归因；weight-only 质量与离线量化时间不等 serving 速度。更多校准、完整相关性和更高精度路径仍共存。

## 结论与检查范围

四项拟采用的条件性分支相对真实当前正文成立；13319 一处配置必须先同步。没有修改作者正式日报或 Books，没有据此签署 Apr16 Gate。局部 owner 明确为 `INFER-TENSORRT-LLM`；实验未复现，公开日期仍由日期作者处理。
