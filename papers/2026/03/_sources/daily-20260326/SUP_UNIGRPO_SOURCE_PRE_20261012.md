# UniGRPO necessarySource / sole Ch24 两PRE

2026-10-12，[2603.23500v1](https://arxiv.org/html/2603.23500v1)，原2+2+3=7/date25保持。actual必要§3–6/Eq1–8/T1与B/T3；Fig3–5仅文字/caption必要反侧，未逐图点值/全部CoT图片/A子表/code或复现。支持/关键反侧足够停止。

## 可采用命题 / 直接反侧

标准TextGRPO/FlowGRPO与RatioNorm借用，不作为新optimizer数学：text生成G条reasoning、每条对应一个image轨迹，用最后imagepromptreward的同组adv更新两phase；image读取完整生成reasoning，text只能读prefix，joint是一轮Prompt→Text→Image。图像动作是finiteSDE nextlatent，deterministicenvironmentappend不等policy确定；hybridSDEwindow记录localdensity，ODEothers无训练梯度。RatioNorm改ratio尺度/shift不等真实全路径importanceprob或exactunbiased保证，不照录完整recipe。

Training去CFG使该rollout中只走一份条件计算，避免此recipe的cond/uncond额外求值；不证明所有多condition必须≥3forward/所有合法rollout必须单链，所有editing/multiround为future。**§5.3/F4明确evaluation所有设置都用CFG**，训练free不授部署无CFG/free而linear graph也不是wallclockscalability证据；F4原Bagel512与F3finetunedBagel1024不同population不能合曲线。

图像分支把localGaussiantransition KL中按noisevar加权velocitydiff换成未加权velocityMSE对reference；这是修改正则目标/时刻责任，不是所有finite-step KL或terminal distribution等价。均匀MSE只约束采样状态，有限λ不强制任意state/step/vectorfield保持；λjoint=1不是两phasegrad自然平衡。reward上涨而画像artifact/heldout下降表明可被利用，regularizer缩小该局部失效不授消除rewardhacking/保所有prior。正文Eq2textKL通用而B实际textKLweight0；另std0guard/reference/ODEstep完整recipe不在本次采用，不自补。

预SFTinternaldata改变Bagel初态，后RL同SFTstart。RewardInternVLbasedRewardDancepreferenceadapt；TA150internalprompts×4image/VLM binaryexammean，GenEval不同自动测量，训练reward/评判可共享偏差非人类真值。T1 Think时SFTGenEval.82<nonthink.83、FlowGRPO.86<.88等，reasoning不普遍提升；unified.90支持单轮局部但reward/budget/norm等共同改变不授唯一causal/所有baseline预算匹配。UniFPOcollapse只该recipe，不推所有FPO数学不可能。F5latentKL早250stepstopped与velocityMSE完整run不同时长，具体coefficient/重复seed/CI未披露，不将artifact例解释为均匀MSE通用稳定性证明；§6terminalreward不能保证正确reasoning、processreward仍future。

B25trainsteps/50evalsteps/1024resolution/CFGtrain1/group24/B32/textlr1e-6/imagelr3e-5/2PPOepochs/jointλ1/textKL0/texttemp1/imageMSE1.5e-5/clip1e-6/SDEwindow[0,5]/size3/noise.8；windowinterval与size两字段保原，不猜3如何选。specificGPU/precision/fullrolloutlength/trainingsteps/concurrency/SLO与完整cost未披露；SFT制备、G reasoning/fullimages、hybridSDE/ODE、rewardjudge/reference、两phasebackward与evaluationCFG/VAE都计费。不采用满多轮/净加速/无hacking或无损保证。

## actual Ch24 差额 / 锚

actual Ch24完整1702–1746与1753–1768生成后训练（generalguidance→expertdiscriminator→TDMsurrogate→discreteflowpolicy→conditionalfusion→trajectorycredit/relay/finiteSDE→geometryreward→PlanValidate），1269–1285decoder费用交接、Ch23/25开篇亦实际读。现posttraining明确trajectoryprob/reward/credit，单modalSDEcredit与discriminator不承载统一text-prefix→imagecondition的单轮terminalcredit/训练取消CFG且评估恢复/velocityvsGaussianKL目标差额。sole MULTIMODAL-GENERATIVE-PARADIGMS Ch24，不复制GRPO完整optimizer至Ch33。

拟“生成后训练”首完整段末“PPO/GRPO 等优化规则与训练系统实现交给 Part IV。”之后、Expert图像discriminator完整段之前两PRE+本人静态注，保全部旧路径。未独核/锁/实际写/POST。

## 两逐字PRE

同一终态反馈还可以跨越文本与图像两个生成阶段，而不只更新单一 denoiser。一个受限分支先采样多条文本推理，每条再条件化一份图像轨迹，将最终图像的组内反馈交给两阶段各自的概率接口；图像可读完成的文本，文本仍只能读自己的前缀。训练时取消额外 CFG 条件分支，可以减少这份 rollout 的求值和上下文负担，但原评价仍恢复 CFG，不能把训练的单链条件继承为交付路径的无引导保证。<!-- source-family:SF-2026-ARXIV-2603-23500 -->

正则目标也须声明在哪份状态上成立：把随机转移中随噪声方差加权的局部约束换成直接匹配 reference velocity，改变的是训练期各时刻的惩罚，不等于保持完整轨迹或终态分布。有限实验只验证一轮文本后生成图像，更多轮次和中间推理判分仍未验；终态得分更高也可能掩盖错误推理或奖励漏洞。模型/SFT、条件、随机窗口、参考与实际部署 guidance 应共同绑定，所有文本/图像候选、奖励/参考求值、适配和解码均计费。条件身份、独立质量或预算回归时，保留原监督生成、固定 CFG 和单模态后训练，不由 velocity 接近或单轮高分授多轮稳定、无损或安全。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23500` — [UniGRPO exact-v1](https://arxiv.org/html/2603.23500v1)必要§3–6/Eq1–8/T1、F3–5文字与B/T3；仅一轮text→image terminalcredit接口、训练去CFG/评价恢复CFG与velocity正则目标分责。保借用RatioNorm非trueimportance、SFT/分辨率/中止预算及reward共偏、terminal非推理正确/多轮未验与全费；不授完整optimizerrecipe、hacking消除、多轮/无损/SLO，未核code/全部图点值/复现。
