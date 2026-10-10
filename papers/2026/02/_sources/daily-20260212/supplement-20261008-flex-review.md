# Flexible Entropy Control exact-v1 必要证据（作者审阅，独立 Source 待 root）

身份2602.09782v1，公开2026-02-11同日包络root已核。拟贡献：单一clip高低阈值无法区分token概率区域→概率相关upper/lower clipping＋训练阶段/hysteresis调度，具体改变哪些正负advantage梯度继续保留→entropy/收敛控制需联合考虑token区域和阶段；2+1+2=5。必要理论边界定点深入。

原件flexcore.json §3/4 L118–247，flexeval.json T1及5.3/5.4 L248–300，flexapp.json B.1完整梯度 L354–403、C/D配置 L416–488、E替代clip消融 L494–510； https://arxiv.org/html/2602.09782v1 。方法/关键评价/直接反侧足够即停，不扩所有图表或代码验证。

Eq5和B.1的logit梯度内积含全词表baselineΣp²(logp+H)，Eq6只取token项为近似；高/低概率0.7/0.3是启发式区域，不授符号处处成立。logit欧氏内积转参数梯度还涉及J Jᵀ，不授整个PPO训练精确entropy控制/无collapse保证。ε(pθ)为可变界，正文/AppC未交代是否detach梯度，保留实现未核。ID/DID T/2及OD高低阈值调度是明确配方，不等于通用最优控制。相位0.5最佳只200steps QwenMath设置。

两Qwen7B、DAPO-Math17k、400steps/B512/G8/lr1e-6/AdamW/zeroKL；max输出4096/8192，8H100，vLLM TP4/verl FSDP offload/Ulysses4。400step训练时间T2 Ours-ID比GRPO两个模型更慢，DID Math更慢但Qwen普通更快，无统一加速。T1局部有AMC/其他任务退化，不能说全面dominance。D明确32/4/2是每题生成样本数，不是独立训练seed；eval sampling.7/.8/k20/B256，training sampling1/1。trainingseed/CI/precision/SLO Not Disclosed。Pass@32中期改善不同于pass@1/最终生产可靠性。

拟owner TRAIN-GRPO/其与PPO交接，需实际正文具体差额；Source/PRE/POST 尚未授。
