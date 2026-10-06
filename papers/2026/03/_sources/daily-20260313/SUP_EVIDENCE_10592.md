# Gradient Flow Drifting 2603.10592v1：Gaussian恒等式与粒子桥接的受限Source ready

真实题名 Gradient Flow Drifting: Generative Modeling via Wasserstein Gradient Flows of KDE-Approximated Divergences。三作者、唯一v1/当前无具名venue/withdraw/correction；SUP_ABS3完整题摘和准入独核有效，SUP_DATE3_10592.raw SubmittedMar11T09:48:42Z/registeredMar12T02:05:16Z与官方公告下界夹Mar12日级，Updated不当依据。

官方 https://arxiv.org/html/2603.10592v1 ，SUP_CORE_10592.raw/txt及SUP_CORE_10588_10592_MANIFEST/RESULT实际GET200/547442bytes/UTC2026-10-10T02:20:54.882413。实际读§3.1–3.5全notation/KDE/WGF/Drifting定义（439–978）、§4.1–4.4完整关键假设/Thm4.2/4.5/4.7/4.9/Cor4.8/4.10（999–2150）、§4.8/Algorithm1（2530–2684）、§5–6 synthetic及限制（2685–2750）。必要AppE score公式、F density-level/particle-level RemarkF1与F1 identifiability证明、G完整Gaussian恒等式（4865–4960、5226–5689、5691–5950）已实读。只发现了H另一MMD说明，不认证H全部；未必要读所有manifold/混合divergence证明或J弱导数，未核pixels/代码/复现。不将第一次组合截断未读算全附件完成。

## 采用范围：恒等式有效，不能直接转原粒子收敛

Gaussian k_h=exp(-||x-y||²/(2h²))的∇_xk=(y−x)k/h²，AppG Eq20–23确给V=h²(∇log p_kde−∇log q_kde)的pointwise field identity。Gaussian positive/characteristic/smooth/gradient bound足够；不否定这个代数恒等式或全空间field≡0的相同law资格。F1连通、strict convex、同kernel总质量和injectivity才推出全x field≡0→p=q；不能从有限batch support梯度小授该条件。

**决定性转接断点（本作者数学推断）：** AppF RemarkF1明确理想smooth rho-flow与raw粒子q不同，认为large-sample一致，但所读没有给固定bandwidth下这条等同桥接。对raw particle law ∂tq=−div(qv)，rho=k*q，则∂trho=−div(k*(qv))；理想rho WGF需要−div((k*q)v)，两者一般不同。复合functional E[q]=KL(k*q || k*p)对raw q的一阶变分需adjoint smoothing k*[log((k*q)/(k*p))+1]，不是仅把原KL的rho变分中的rho替成q_kde。因此Cor4.10/4.8不能仅凭field identity把smooth-density energy dissipation/unique equilibrium授给raw particle/generator更新。

精确1D反例：p=(delta_{−a}+delta_a)/2，q=delta_0，a>0且Gaussian bandwidth h>0。用原Eq4，V(0)=0，而全部x的V(x)=a tanh(ax/h²)，非恒零；raw q的所有粒子停0且KDE rho不动，p_kde与q_kde仍不同。理论F的smooth rho-flow速度在x≠0非零，不与该raw粒子演化相同。这个例子满足paper允许任意Borel p/q和Gaussian kernel，但**不反驳Thm4.7要求全x field≡0**，不声称每初始化实际训练必collapse/损失必升；只否定无额外条件就把density-level equilibrium/convergence直接授粒子系统。增加样本数但保持全部raw q=delta0不修复此固定h桥接。

Alg1还由同batch生成样本估计KDE，再stopgrad(x+v)对generator参数训练；这是有限函数类/参数耦合更新，不是每独立粒子或rho密度严格按WGF一步。带宽/normalizer/零小分母、MonteCarlo与eta、网络Jacobian耦合均须分开，不用sg loss数字或单步生成宣称全生成law单调收敛。

## 评价、反侧、actual owner与终态

§5为2D toy particle演化图与正文模式/模糊观察，§6明确大维minibatch variance、更多ablation/JEPA hypersphere/ViT/semantic训练未来工作；不是foundation模型/真实语义manifold已验证。没有把图像像素读为定量FID/coverage或独立证明；样本/重复seed、混合权重/带宽/步长、硬件/precision/训练预算/端到端成本在所读必要实验Not Disclosed，不补造“普遍更稳/避免全部mode collapse”。密度估计、成对kernel、有限更新/target生成与训练仍付费。原Laplace不C1只限本smooth推导，不否定弱导数或其全部实际方法。

ROADMAP唯一MULTIMODAL-GENERATIVE-PARADIGMS Ch24。实际完整232–246训练path与solver责任、geometry/learnedvelocity/finite-step分别验收；288–294含前后指导reference与empirical MMD段，已有kernel/reference/batch状态、梯度集中≠decoder law及高维/预算回退。没有写入/认证本稿新Gaussian/KDE定理，主题相同不是已有覆盖。Ch23表示的语义kernel假设只是handoff，不建第二owner。

拟 **2+1+2=5，中心理论桥接争议，必要受影响深入已完成，暂缓Books0**：具体新drifting-field解释/收敛资格会改变训练解释2，限定一个生成训练组件1，field identity与law evolution不可静默互授的具体新理论边界2（不借成熟KDE/WGF原则计3）。不按toy或访问状态排除/降池，不因数学困难索取所有附件。保有效pointwise Gaussian identity与有限toy事实，隔离density→raw particles→参数更新的无条件收敛主张。

精确重开只需本ID补固定kernel下raw q/KDE rho的合法演化/metric/limit桥接、support/初始化资格及generator近似条件与对应实验预算；不请求全站史或其他Drifting原稿全文。root非准备者已实际必要原证/数学反侧/Ch24完整局部裁决2+1+2=5受限桥接争议PASS，正式暂缓Books0，不否定恒等式或全训练。准备者不写Books，无PRE/POST需求、不授DAY。
