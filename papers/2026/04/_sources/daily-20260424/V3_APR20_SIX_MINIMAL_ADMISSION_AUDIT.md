# Apr24 六项最小准入/争议边界：非作者有限核

复核者apr20_resume；已实际恢复重读AGENTS/当前合同/Prompt/ROADMAP。只核V3_SCREENING_NOTES“最小消歧收口一”六项与决定处置的官方v1段落/必要反例，不是全日、首公开或Books Gate；不写共享Books。作者未变有效记录可复用，以下指出实际读取与差异。

## 20874：5分纠错深入的窄争议边界通过

实际读[official v1](https://arxiv.org/html/2604.20874v1) §3–7.6：§3声明first-order linear fidelity，但随后当作所有模型单调规律；§5两个公理只限制有限窗口与给定填充下降，§7.3额外假设携带full history逐session增长，§7.5据此称压缩为唯一可行架构。有限canonical state加有界read-time检索的无限重复任务反例仍满足有限窗口和给定填充下降，不要求任务数增长时当前窗口增长。因此中心“所有context问题只归signal/token、唯一homeostatic长期生存”缺必要桥，不采普遍保证；不否定60+session作者经验、有限压缩价值或所有长context退化。作者恢复候选、5分纠错Deep/暂缓提案边界PASS；普通精确日期尚另核。

## 20897：5分标准Only窄条件边界通过，补一个不可采用的等式

实际读[official v1](https://arxiv.org/html/2604.20897v1) §3 Definition1–3、§4 theorem/proof/cache corollary及§7.1 affine-SAT例。speedup是matched task/intelligence的irreversible operations比，不是GPU计时或任意硬件能量；reference state先固定，训练/适配/restore分账，class-specific universal search已把generic implementation改进吸入baseline。finite cache例按扩增任务支持集权重，不是heavy-hitter真实请求分布。作者Only保条件性理论对象、避免joule/热力学普适工程保证的边界PASS。§7.1把任意affine basis/offset的Kolmogorov complexity等同`nd+n+O(log n)`不可直接采用：编码长度是上界，简单/可压缩subspace可更短。受限枚举`2^n`→`2^d`的算法计数例仍可保，不将错误精确complexity式纳入证据；这不要求通读热力学所有proof/引用树。

## 20926：具体前分母关闭通过

实际[official v1](https://arxiv.org/html/2604.20926v1) §2.1–2.4、§4.1.1/4.1.2必要方法与对照。完整problem/harness/OpenMP candidate真实执行ThreadSanitizer/Caliper取标签，再以结果条件化teacher hindsight CoT、completion-only SFT；Caliper paired codes共同环境减少变动，仍是tool imitation的已有proxy recipe。partial snippet不可执行的动机没有变成新partial-state标签/拒绝或置信协议；teacher compatibility/思考与不思考的有限任务对照，不独立改变本项目代理有效性的长期判断。关闭不是代码域、小模型或章节已有硬拒，保原受限race修复事实；不需为贡献排除追完整首发史。

## 20938：6分纠错/保护深入窄争议通过

实际[official v1](https://arxiv.org/html/2604.20938v1) §VI Eq2–6/PropertyI–II、§VII Implementation/preflight。posterior chance constraint原文明确是optimizer beliefs性质，不是μ真实下界；cold w=0目标不可识别、低precision和三个variance项、clip只inflate observation term保持。实现ridge替SAAS+NUTS、linear tensorproduct替Matérn、per-candidateMC替jointqNEHVI不能合成“参考算法完整执行”。实际数值反例：lengthscale1的标准Matérn5/2在Boolean±1 cube距0/2/2√2取约1/.13866/.03701；affine-Hamming需最后值`2k(2)−k(0)≈−.72268`，不相等。只隔离kernel/完整posterior实现等价及因此的保证，不抹掉warm/firing telemetry、有限baseline与配置经验。作者恢复潜在贡献、6分深入的分责PASS，实际owner采用仍须另外核。

## 21026：前分母关闭未通过，定点恢复准入判断

实际缓存[official exact-v1](https://arxiv.org/html/2604.21026v1) §3.1/3.1.1、§4.8并重新打开当前同一官方URL确认，不只是目录标题。§3.1已承认12题为purposive stratified非iid、固定安全margin非理论推导；**§3.1.1确有top-k recovery/variance-gap scaling及scope限定**，与作者“没有建立新MC稳定性/error-bound合同”的排除理由不一致。其界依赖sub-Gaussian sample-mean concentration，不自然适用于12个有意选题；ranking恢复明确不证明全局precision最优/PPL无损。§4.8的combined scorer对自己reference 100%是同一对象，不是独立oracle验证，跨scale FFN/attention代理方向仍是受限信号，不应称普适最优。

这项不能因三tier/混合precision组合直接retain，但已经有需要核的**selection signal稳定条件、outlier gap与端任务误差保证的分界**，而不是仅新应用排名。建议只恢复此项为潜在5分标准候选审阅，先核该条件性命题/校准支持；若进一步证明不改变现有长期认识，可Only而非硬补Books。不将尚未核的12题保证或完整理论视为PASS，也不扩全部engine/附录。ConfigA保层、B/C跳层的旧有效边界继续保留。

## 20925：具体前分母关闭通过，不否定小模型/代数表示

实际[official v1](https://arxiv.org/html/2604.20925v1) III-A–D及IV-C.2/Conclusion：原homomorphism/variance loss继承已有方法，加入U-Net masks/重建；相对`g1^-1∘g2`再additive projection是标准坐标/结构组合。Chaser/Evader模拟展示approach/recede轴，source明确commutative只几何对称变化不拥有“谁追谁”非对称agency，state不足也是其future work。没有新增可迁移的非交换/物理transition有效性条件或受控验证，使应用组合不足以改主线判断。关闭通过限这个实际贡献，不外推代数约束无价值、toy不入选或所有两物体研究应删。

五项原采用/关闭边界通过，21026因具名漏读机制恢复最小准入，20897补精确不可采等式。不得称六项全PASS或日级Gate；只有这个共有错误理由受影响的一项重开，其他实际有效证据不推倒。无复现、无Books改写、无stage/commit/push。
