# 15439 / 15694：生成路径与跳转分解的窄采用提案

作者apr20_resume；两项2+2+3=7深入。必要v1证据与反证见[v3-reopen-notes接续五项](./v3-reopen-notes.md)。未获非作者source→actual owner通过、未写Books，不计I或日Gate。

最新实际采用与写后：root必要source→actual Ch24复核后授窄锁，作者落实四段及章末Review；root又实际顺读两处正文和相邻段落，15439在并行/少步标题后、原组合近似之前，15694在joint artifact之后、SNR监督之前。PSD充分条件、具体两uniform反例、模型近似误差、真实exit-rate权重、一阶梯度假设、Euler合法性、时间步/NFE区分及OWT协议分歧均已真实保留，未将理论或finite-sample genPPL写成生产保证。两个实际写后PASS，可同步整合；上句是提案时历史状态，不再表示当前未写。没有日级Complete声明。

## 15439 One-Shot Generative Flows: Existence and Obstructions

唯一`MULTIMODAL-GENERATIVE-PARADIGMS`/Ch24；实际读取258–309，272 learned flow-map近似组合、291–300近似solver已有，但没有**随机sample路径直线与conditional velocity流直线不同，以及独立端点在精确straight-flow可行性中的约束**。拟在“并行与少步生成必须声明依赖、轨迹和状态边界”标题后、少步蒸馏组合段前，嵌以下两段：

> 讨论一步生成之前，还要区分训练样本的插值路径与采样ODE的轨迹。把独立噪声样本和数据样本作直线插值，并不使条件平均速度产生的flow map自动成为直线；在相应正则与矩条件下，普通affine插值要产生精确直流，需要确定性端点coupling，而不是随机独立配对。若流的全加速度确实为零，一次初始速度评价可精确积分；训练出来的近似velocity却仍有估计误差，这不是“训练路径直，所以一NFE无损”的保证。
>
> 独立端点也不一概阻止精确直流：非退化Gaussian端点可以加入协方差专门匹配的独立Gaussian辅助噪声，构造零全加速度的条件流；但相同的两段分离uniform混合，在独立端点、连续样本路径和时间上一致Lipschitz速度等条件下已有不可能例子。[存在性与障碍分析](https://arxiv.org/html/2604.15439v1)因此限定的是某类过程的结构可行性，不是所有多峰目标、所有神经生成器或任意维少步算法均不可行。改变coupling、增加前置transport估计或保留弯曲轨迹的多步solver，会改变计算与误差分工；不能确认所用过程满足这些条件时，应保留经验质量—NFE验收与原solver回退，不以定理替代实际训练和部署验证。

### source→literal边界

v1 §1.4 Def1–4、§2 P1–C4/T5的正则/矩条件，T5充分方向PSD Jacobian不能写任意T；§3.1 T6/P8/T9额外噪声是sqrt(2t(1-t))Z，特调cov非Brownian普通bridge；§3.2 P10时刻τ崩塌违反uniform Lipschitz；§4.1 C12具体两个区间混合的no-go比全文headline窄。§4.2 T17 d1/Frostman/固定C(A,alpha,beta)/epsilon0依赖仅作为报告边界，不将通用highdim/fullsupport no-go写书。已有Ch24组合近似依然保留；理论无hardware/生产NFE质量实测，literal不添。

## 15694 Neural Continuous-Time Markov Chain: Discrete Diffusion via Decoupled Jump Timing and Direction

同owner Ch24；实际674–679 corruption/parameterization/loss/sampler jointidentity、848–850离散Euler policy合法性已有，尚没有**exit-rate与jump destination两种学习目标及mask固定rate特例**。拟在674–679原jointidentity两段之后、下一representation supervision段前嵌以下两段：

> 反向离散过程还可把“何时离开当前状态”与“离开后去哪里”分开参数化。CTMC的off-diagonal rate写成exit rate λ与destination分布r的乘积；相应path-space KL可以分成Poisson timing误差，加上真实exit rate加权的categorical direction误差。可训练conditional surrogate与marginal目标保一阶梯度，需要forward量不依赖参数、reverse rates正且可微以及微分积分交换等条件；这不自动保证有限训练稳定或神经网络找到全局解。absorbing-mask特例中rate由noise schedule固定，才退化为熟悉的masked-token交叉熵；uniform corruption允许重复跳转，两者不能因同叫diffusion就共用训练与sampler假设。
>
> 这条分解让模型分别学习转移强度与去向，却增加一个rate head以及rate—步长校准责任。Euler需要λΔt≤1才能形成合法跳转/停留概率；τ-leaping一次时间步可抽取多个jump，并在新状态重新计算destination，因而时间步数不等network evaluations。[受限离散生成研究](https://arxiv.org/html/2604.15694v1)的163M、长度512与统一Gemma-2评分仅提供其TinyStories/OWT质量证据，有限样本genPPL不天然成为数学上界，更不证明线上延迟或所有模型优越。rate或概率合法性无法验证、质量—真实成本不改善时，应增加时间分辨率或回退已验证的mask/schedule与原denoiser，而不是只按step数宣布加速。

### source→literal边界

v1 §4.1 C4.4/P4.8/C4.10给timing/direction、regularity与mask特例；§4.2/AppendD Algorithm2–3给Euler合法性和每新state重算r。保main/Table1/AppD OWT τ列披露不一致，不补造protocol；TinyStoriesmatched/OWTreleasedpipelines不同、SEDD682B vs262B、128stepsSEDD更好保留在报告，不采性能排名headline或“finite sample ⇒ ≤bound”。新增head不等独立两个无耦合trainingproblem，literal true-rate权重保留；不写Hessian/任意dropout精确训练保证，不展开全部样本展示或代码复现。
