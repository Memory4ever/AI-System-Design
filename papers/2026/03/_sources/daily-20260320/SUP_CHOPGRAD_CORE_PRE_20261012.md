# ChopGrad 2603.17812：必要原证与最小整合准备

准备者 resume_review17_18，2026-10-12，仅本 Daily03-20 补03-19自然日。原准入/date与2+2+2=6复用[有限尾筛选](./SUP_FINITE_TAIL_SCREENING_20261012.md)：题名/八作者/ID一致，官方公开批次与exact DOI日夹证，不挪原日期。已重新读取AGENTS、研究/Report合同、Daily Sources、统一Prompt、ROADMAP、本日README/STOP及当前适用写作上下文。这里只是准备稿，**未自行授Source/PRE PASS、未写Books、未计safe或DAY**；交resume_mar17非准备者核。

## 1. 实际必要原证范围

[exact-v1 HTML](https://arxiv.org/html/2603.17812v1)：§2.1–3.3/Eqs1–6 L108–175；§4.1–4.4/Tables1–4 L179–252；A/Alg1 L261–294；B1–B4 L298–339；C1–C4 L344–391；D L392–401。围绕局部梯度、质量和资源口径读足即止，未读取附录E/F全部图、代码、项目附件或复现实验。图3–7仅读caption/正文解释，未冒像素视觉核验或重建其数值曲线。

[current abs](https://arxiv.org/abs/2603.17812) L8–28实际核：v2 Apr07，题名/八作者/AB同identity，Comments仅project website，无明确撤回、纠错或影响拟采命题的修订说明；版本号本身不触发全diff。本次命题只取v1有限接口。

## 2. 支持链与必要反侧

旧latent objective通常不穿过decoder；即使冻结decoder参数，像素损失对latent/backbone的梯度仍须穿过它。因果VAE每层把旧组cache接入当前组，前向的跨组状态导致完整反传保存递归activation。A实际先detach cache、执行当前decode/loss，再显式向有限旧组传播cache梯度，释放窗口外计算图；detach不是删前向历史或把所有帧独立解码。主干仍可消费全latent上下文，窗口限制的是decoder反传链。CogVideoX原奇偶组重建语义要求两组一起decode，不能凭G=4给全部codec统一recipe。

Eq3局部性是带C/alpha的指数Jacobian条件；WAN2.1局部诊断只在97帧、64×128及若干视频，backbone梯度比较用1.3B/约100视频。Eq6误差右侧还乘S=Σ||loss gradient||；L153选择D≥log(C/epsilon)/alpha省去了S，除非另有S≤1等归一条件，不推出指定绝对epsilon。小D时参数梯度MAE显著且不随人口平均消失；高cosine不认证逐参数误差、optimizer scale-invariance或最终无损。只采近似窗口机制，不采普遍无偏、收敛或全模型locality保证。

内存有限指固定D/空间chunk下decoder计算图驻留；latent输入/输出梯度、backbone attention/activation、loss网络、参数/optimizer/FSDP/sequence-parallel buffers仍在。D解释重复backward/更迟释放的time-memory交换，大D接近全长时有额外开销；不采用其n_evict=T−D简式为精确运行recipe，也不把总训练memory或时间称为随视频长恒定。正文“3–4小时”不能覆盖C1约8小时、C4约10小时及inpainting最高18小时；全部费用与配置需按任务分开。

关键评价：Table2同Wan14B的latent-only、加倍latent-only、pixel-loss分支和D=0/1/2消融支持局部目标取舍，但pixel-loss PSNR/temporal flicker也低于latent-only，D增大并非全部指标改善。跨baseline还改变backbone/分辨率/view选择，B2 MVSplat跨组attention因OOM关闭；不归因所有差额给截断。Table1 DOVE→ChopGrad在UDM10 SSIM .7827→.7753，RealVSR SSIM .7301→.7193及LPIPS .1851→.1934反退，训练videos-only vs DOVE80% images混杂保留。Table3表值FVD是DL3DV574.441→583.581、Waymo440.651→470.545退，ROVI201.610→188.546改善；L237文字恰相反，不采该解释。一步vs50步是采样配置改变，不是截断本身50×端到端收益。C2计时为整视频时间除帧数、再乘GPU数的GPU-time/帧，不是单卡墙钟或fresh deadline。Mirage是作者Wan重实现，另付高分辨率/较长duration微调，不认证原Mirage或真实驾驶安全。

未在必要证据披露可对应全部比较的precision、concurrency/SLO、repeat/CI及全预训练/数据构建/调参总费，记Not Disclosed；不因这些自动EX/降分，也不借API访问或Books已有原则假NC。需要采用绝对梯度/总memory/精确调度保证时须另核同codec Jacobian、S归一、窗口缓存实现、完整峰值及matched-budget质量，当前不采用那些主张。

## 3. 实际唯一owner与差额

Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，当前[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际完整读取L139–173（latent/pixel训练目标→普通噪声MSE→实例修订与time-sampling→sampling）、L73–91（局部编辑/像素监督消费者）、L343–359（训练状态/反向核误差）。现有正文已说明decoder/像素loss费用与分工，但没有因果codec前向cache和反向图窗口分离、显式cache-gradient回传及其条件近似。

相邻Ch23实际入口L1–42及rate/distortion/codec训练L379–399，拥有表示/重构契约，不复制codec训练机制；Ch25实际L1–40将画面与环境因果分开。Ch28入口L1–46与Ch39入口L1–64实际核：next-token优化与model-state sharding不能承载此像素监督语义；ZeRO/FSDP不消除decoder activation链。只是这些入口和相关交接，不声称全章审阅。先前宽rg输出截断未作完整覆盖依据；采用判断依上述实际完整局部。

拟位置：Ch24 L149普通简化噪声loss完整段之后，L151实例unlearning之前。连接“loss所在空间与梯度可训练路径”再回到局部目标修订，不另开论文标题，不改原AR/codec/采样机制。拟两短段+本family静态源注；无其他owner写入。

## 4. 待非准备者核的逐字PRE

像素监督还要求区分 loss 所在空间与反传能承受的路径。latent 视频模型只在潜空间拟合时，不必把损失穿过视频 decoder；若要比较解码后的像素或感知特征，即使 decoder 权重冻结，梯度仍须经过它传回 latent 与生成主干。因果 VAE 在各层把上一帧组的 cache 接入当前组，完整反传因此保留跨组计算图。一条受限分支保留这份前向历史，先 detach cache，再显式把当前像素损失的 cache 梯度回传有限旧帧组，释放窗口外图；主干的全局上下文并未随之删除。这减少的是 decoder 反传驻留，不是把视频逐帧独立生成或证明整套训练内存已与长度无关。<!-- source-family:SF-2026-ARXIV-2603-17812 -->

截断距离必须与同 codec 的时间局部性、损失尺度和质量一起验收：指数 Jacobian 衰减只是误差界的条件，界中还含损失梯度总量；高梯度 cosine 不消除幅度误差，也不认证最终更新无损。[必要视频对照](https://arxiv.org/html/2603.17812v1)支持有限窗口下像素目标的可训练分支，却有失真、感知和时间指标反退，扩大窗口亦非全部指标单调改善。重复 backward、空间分块、感知网络、主干 activation 与分布式缓冲仍付费；一步与多步采样、额外微调和 GPU-time 不能合成截断的免费加速。时间依赖较强、梯度或质量回归失败时，保留更长窗口、完整反传/重算、较短训练段或原 latent loss，分别验收 pixel、temporal quality 与完整成本，不由局部 cache 近似签发无限视频、一致性或真实环境安全保证。<!-- source-family:SF-2026-ARXIV-2603-17812 -->

静态源注：

- `SF-2026-ARXIV-2603-17812` — [ChopGrad exact-v1](https://arxiv.org/html/2603.17812v1)必要§2.1–4/Eqs1–6/Tables1–4、A/Alg1、B–D相关实现/费用与直接反侧；只因果decoder前向cache保留与有限反传图分责。保局部性/损失尺度条件、梯度幅度误差、质量反退、任务预算/基线混杂与完整费用，不采恒定总memory、无损或采样倍数/安全保证。未运行代码或复现。

## 5. 非准备者裁决待执行

resume_mar17必要Source/actualowner/两literalPRE核；未获明确root独占锁不得写Books。准备者读回不替代独立核验或actualPOST。

2026-10-12 resume_mar17 实际非准备者有限核：独读 exact-v1 §2.1–3.3/Eqs1–6、§4/Tables1–4、A/Alg1、B1–4/C1–4/D与current abs题名/八作者/Comments/history；没有扩附件E/F、代码或全修订比较。实际Ch24完整139–177、73–91、343–359及Ch23入口/379–399、Ch25入口、Ch28入口/Ch39 model-state与activation分责回读。Eq6损失梯度总量、参数MAE、高cosine不认证幅度无损、decoder窗口与主干全上下文/完整费用分责均准确；Table3原文字FVD方向与表值反向、Table1/2直接反退及各任务训练费保留。两literal PRE与静态注逐字有限PASS，原6分不变；sole Ch24 loss-space→反传路径差额成立，非假NC、不授constant总memory或精确算法/质量/安全保证。未写、未actualPOST、未safe/DAY；请求root协调本family窄锁，写后一次nonwriter完整局部/静态注验收。

## 6. root sole窄授权后的writer实际落实

2026-10-12 root接纳§5非准备者PASS并授resume_review17_18 sole Ch24本family两literal/static锁，另一日尚未写同章。writer实际读当前完整139–164与章末原注，再按§4原两literal写新152/154，静态自身源注2485。实际完整137–175及末2479–2485顺读回原PRE一致：普通latent loss→像素监督可训练路径/条件近似→实例修订/在线time-sampling→sampling链保持，旧机制与其他family无改。章diff由60新增变66新增，仅本family两段+静态注六行，scoped diffcheck0。原证/质量反退/费用及回退责任近文；静态注不写验收身份。交author一次nonwriter actualPOST完整139–179/2477–2485，writer读回不等POST或safe/DAY；root锁待真实POST后释放。

## 7. 一次nonwriter实际POST

2026-10-12 resume_mar17 实际读回Ch24完整139–179（新152/154）、2477–2485自身/PhysVideo/AFS邻注，逐字回§4两literal及已独核必要Source。latent/pixel空间→因果前向cache保留/有限梯度图→条件误差/全成本→实例目标修订与sampler交接自然；不把主干全上下文删除、不授总memory恒定/精确recipe/质量或环境安全。静态源注来源/范围/反侧准确，无动态身份写回；scoped diffcheck0。实际有限POST PASS，告root释放Ch24本family，可按实际I归并；不授整日DAY。
