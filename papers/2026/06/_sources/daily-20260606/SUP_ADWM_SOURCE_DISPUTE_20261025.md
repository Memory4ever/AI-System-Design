# ADWM 05558：首次必要与中心桥争议

作者`supp_jun06_close`，2026-10-25，仅Daily2026-06-06补Jun05。R31完整AB/notice/Jun05联合资格与贡献准入复用。拟2+2+2=6，score对象为Agent/WM因果交替及policy-guided transition的OPE替代；不因发现冲突降分、删候选或称零命中。

实际读[exact-v1](https://arxiv.org/html/2606.05558v1)§3–5/式1–10、A/B/C/D、E1–3/E9–10 Alg2与F关键对照、T1–2。HTTP正文一次空响应后直接官方HTML恢复成功；不是外部访问受阻。未核代码、图像素或复现。

## 可保留的原始机制与评价

LLM要先见observation才能采离散text action，所以不用同时joint diffusion整条states/actions；当前latent经8soft-token projector交target policy采action，再由带历史/action条件的50-step DDPM生成后继，reward/done heads供imagined rollout。proposal在离线behavior support内，state仍imagined，不能由独立transition denoise宣无累积误差。

作者主文将score分为prior、action posterior(CFG)与长程continuation（target-policy loglik gradient）三项；continuation期望intractable，D用单greedy rollout/denoised estimate近似并anneal。目标LLM必须可消费soft embeddings、提供梯度，不是任意纯黑箱API；主文black-box措辞与实现权限不同。E1/2为PyTorch2.1/CUDA12.1/Python3.10、vLLM0.5.4 BF16 TP1、2×RTX8000共享node但每job单GPU；五seed只改inference randomness，WM每环境仅训一次seed0，不算五独立WM复现。共约300GPUh，LLM-side dominates；不是免费OPE。

六配置、五epsilon点（cross-policy十点）的Spearman rank主要只测随机掺action退化曲线，不认证绝对return无偏或任意新policy。ALFWorld-iter1 rho .67 CI[-.91,1]、p .219，FQE .82；ScienceWorld WIS .97高于ADWM .82，不采逐cell全面最优。WebShop GT约7% standard error与跨迭代gap同阶；E9 soft-token检索近随机但作者称有用gradient，两者不互相认证。ScienceWorld只是通用OPE测试环境，不采用其领域科学结论。全behavior数据/WM与adapter训练、所有target调用、未来guidance/生成及GT校准都计费。

## 中心争议一：删行为density后并不恢复target轨迹law

式1/17正确写p_e=p_b*product(pi_e/pi_b)。式2/19丢掉分母，令q∝p_theta*product(pi_e)^alpha，§4.1及C却宣p_theta=p_b、alpha=1时等于p_e。C式21→22将积分中的剩余product(pi_b)直接消失；归一化通常不等1。可复算反例（本项目推断，非作者实验）：单step、两action、同一确定环境，pi_b=(.9,.1)、pi_e=(.5,.5)。式19归一后q=(.9,.1)，真实p_e=(.5,.5)。因此behavior regularization可以定义另一proposal law，不能当精确OPE纠偏。B关于已定义q的链式conditional因子化仍可成立，不因C错推倒所有方法，但“恢复target law”不可采用。

## 中心争议二：主文score/value与Alg2不是同一实际估计器

主文式9/D36–38依target-policy未来loglik gradient；E10 Alg2 L11却以success bank cosine的gradient替代。主文式10累计reward-head预测；Alg2 L19将每rollout value取max_t cosine(success bank)，L15虽预测r_t却不进入最终J。E9解释gradient经过target-policy input embedding的必要性，不能消除Alg2差异。需确切说明实际实验采用哪个guidance/value、success bank资格和与相同estimand的baseline控制；不能选正文中的漂亮部分拼为已验证OPE recipe。

## Books处置提案与重开条件

唯一拟owner `MULTIMODAL-WORLD-MODELS` Ch25。实际读预测channel与policy-support边界、action-conditioned与imagined rollout的相关段及邻Ch24/26交接。Ch25已要求observed/belief/imagined分离、policy support不等counterfactual qualification、learned transition不等真实效用；本篇额外的因果交替/soft-token-policy interface潜在可用，但两个冲突正处OPE中心桥与实测机制，不能用既有保守原则掩掉。

拟**中心争议/Books暂缓，不写Books、不新I、不宣必要正向通过**；候选保本分/日期与有效已读证据。不是普通“尚未读完”。可接受定点重开材料：作者对应精确版本的勘误/可核实现，明确q与target law关系、修正式21→22；给出实际实验guidance、success bank与return估计路径及匹配baseline/GT。只重开05558，不扩其他日/整个OPE域。交root独核该两条具体反例与终态隔离，当前未自签独核或DAY。

root R35已直接核C式19–23、E10 Alg2与主文score/value，两个中心冲突及单步反例成立，正式6与暂缓隔离通过。保候选/反证、不正采OPE性能/安全、不入Books，不把已读争议称访问失败或普通未读；只在上述精确材料澄清后重开。本次同步既成，不重做独核或授整日DAY。
