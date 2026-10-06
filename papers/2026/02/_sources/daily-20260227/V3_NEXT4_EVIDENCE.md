# 第二小批：四项命题匹配必要证据与真实owner比较

精确v1HTML原件/blocks保存在本日目录；下面block号不是文件行。准入已独立校准；必要方法、关键对照及直接反侧由作者实际阅读，未核代码或复现实验。root已实际必要源/owner PRE及四项正文、完整邻接、自身末注POST通过：21321 Ch28 486/474–499/own1783；21341 Ch23 368/362–380/own1311；21428 Ch23 107/99–115/own1313；21429 Ch24 149/151/136–157/own1745。四项整合终态，Ch28/23/24窄锁释放；以下保留原差额与PRE提案，不表示仍待写，不授日级Gate。

## 21321 RIDER/E-RIDER — 2+2+2=6；具体更新接口差额深入

[exact-v1](https://arxiv.org/html/2602.21321v1) §2–5及必要B.2/F.1–4：blocks44–112、115–137、163–165、409–428。AIMC的正/负pulse响应不对称，使局部symmetry point(SP)和优化目标驻点不同；先零移位的静态校准既付pulse成本，又把估计偏差带进后续更新。RIDER在analog P/W之外维护digital Q的EMA，梯度在混合权重 `Wbar=W+γ(P−Q)` 计算；E-RIDER以chopper正负翻转分开梯度与慢SP drift，实际为 `Wbar=W+γc(P−Q)`。§B.2(164)与AGAD只在main W求梯度的差别明确，不是仅换算法名字。额外analog fakeQ及周期digital校正减少频繁programming，却增加阵列、读写及同步状态。

理论只在有界正响应、光滑/强凸、无偏随机梯度、特殊Rayleigh梯度下界与量化误差假设下成立，不迁往任意NN。Theorem2.2的upper bound不独自证明每个响应模型都有Theta粒度误差下界；这里只采用动态校准/更新机制，不采用普遍收敛或精确lower-bound口号。

AIHWKit simulator：MNIST fullyanalog LeNet/FCN、CIFAR100仅ResNet18最后block和FCanalog，3seeds（表1/2）及80epochs。算法分别调learningrate、granularity、chopper，Table3–6有不同recipe，非单因素matched更新证明；同一E-RIDER p=0 vs small p>0的50epoch对照(428)支持有限chopper差额。7bit input/9bit output/readnoise.06；不是硅片/真实energy证据。Fig4 pulse计量为epochs×ceil(data/B)×BL，不包含全IO/programming/多阵列同步，不称端到端节能或生产LLM吞吐。更小状态数不等静态校准免费。

Owner建议TRAIN-PRETRAINING Ch28。实际480–492完整“Optimizer State也必须服从数据与硬件契约”已有DP filter-noise及硬件structuredsparsity，但未承载“器件正负响应的SP≠loss驻点→在线analog残差/digital EMA→gradient评估坐标”的训练update接口。拟在该段的硬件契约分支加一窄段：旧静态SP校准仍合理；新增在线state职责/混合权重及extraarray成本、假设与模拟范围/数字更新回退近文。Ch27小结1193–1210、Ch29开篇1–60已实际读。只申请Ch28局部段+自身末注；不另建硬件/算法小节。

## 21341 Scaling View Synthesis Transformers — 2+2+2=6；具体条件编码差额深入

[exact-v1](https://arxiv.org/html/2602.21341v1) §2–4、§6及10.2：blocks34–90、127–130。从decoder-only将context随每个target再编码，改为target-agnostic bidirectional context encoder+target cross-attention decoder；context features可在多个target之间复用，target views独立并行，但无固定latent bottleneck。MLP工作从VcVt形态改为Vc+Vt，attention仍含Vc(Vc+Vt)；这不是所有view或表示的信息免费复用。

同params/steps时encoder-decoder较差，FLOPs-matched更多训练数据后反而更好；小数据regime decoder-only仍有利，明确否定“参数相同即算力公平”。`B_eff=B*Vt`固定128/1024（RE10K）或256（DL3DV）的局部比较PSNR约±.1/.2，只支持context摊销配置，不认证任意SGD等价。Scalefit用重复scene而非unique样本，不迁作普遍law。multiVc>2在无relativecamera编码时饱和，PRoPE在两family改善，额外camera prior不消失；固定latent bottleneck的两family scale较差。最优headline训练预算不全匹配，不合并归因。

渲染速度明确A6000、B=64、Vt=1，作者B=1均约30FPS因非FLOP瓶颈而改batch，硬件精度Not Disclosed；不称single-request/fresh-scene低延迟或端到端生产SLO。context features增加驻留/预编码成本，target条件质量损失是复用的相反压力。

Owner建议MULTIMODAL-REPRESENTATION Ch23 Cross-attention fusion(362–370)。实际段已拥有方向/connector/query同步、多层条件与recurrence，却没有“target-conditioned producer不能无条件跨target复用，target-agnostic producer换编码成本与条件质量”的接口。拟一窄段放该generic说明之后，声明camera/scene/encoder身份、同computevs同params反侧、驻留/预编码及B64非单请求；受限scene合成不授WorldModel。Ch22小结/Ch24开篇实际已读。请root裁Owner是否应Ch24；只有一个owner，不双写。

## 21428 PSF-Med — 2+2+3=7；稳定性与实际模态使用分离

[exact-v1](https://arxiv.org/html/2602.21428v1) §§2–4、AppendixA/B/Q.5/Q.6：blocks18–70、85–115、129–130、142、153–155、267–270。MIMIC1k/4998questions+PadChest4534/14750，共19748questions约92kGPT4o paraphrases；embed>.9/排除否定翻转不等正式人类semantic等值判定。3.2–8.7%refusal/hedge/unparseable排除，flip人口不同于全部准确率人口。

Presence N2499：MedGemma27B flip9.4/text-only agreement85/swap19.6；4B flip18.2/text-only66.4/swap30.8，说明低flip仍可能来自textprior，不证明大模型必然失去视觉。image swap未经同答案GT匹配，不能把任何变化认证正确grounding；bboxattention(200)只是定位相关非因果证书。

机制只在MedGemma4B layer17 Feature3818：delta-only SAE patch不重构全部激活，158curated FlipBank平均margin回收44.8%、23例完整reversal；单feature/margin不是所有flip因果。token-held pairs(85–88)仍只少量措辞，不授抽象register唯一特征。meanactivation-matched randomfeature11042及其余高AUC五features控制(268)支持该feature的有限特异性。inference clamp使MIMIC flip15.6→10.8但accuracy78.2→76.9，combined flip9.2/acc76.1；PadChest42.4→33.8但69.1→67.6，联合30.5/66.8。更稳定可伴更错，不采“无税修复”。12msA100/<2%仅作者单模型插桩，SAE额外128MB/精度未披露；74GPUh评价、未核releasedartifact。

Owner MULTIMODAL-REPRESENTATION Ch23实际91–105：目标遮蔽/配置诊断已强调contextprior与stability≠correct，但未联合“paraphrase stability+text-only/swap dependence”及patch降低flip而accuracy退步的具体双Gate。拟在现103–105后加一窄段，不改诊断临床部署：固定semantic等值人口再分别验稳定、原模态依赖与任务正确；移除feature只提案，independentquality与成本回归，若tradeoff不合格保留原encoder/projector/原图和独立证据。已有MOH正文不重复。Ch22末/Ch24开篇交接已读。

## 21429 Constricting-CBF — 2+2+3=7；采用有限采样约束接口，隔离硬保证/KL等式

[exact-v1](https://arxiv.org/html/2602.21429v1) §3–6及A.2：blocks25–84、91–137、151–162。从任意Gaussian init未必在目标safe-set出发，添加随reverse sampling收缩的relaxation ε(initial,t)，初值覆盖h违例、终值0；每步最小norm QP修正sampling drift，并计入已采noise方向。它改变的是生成候选路径，h/pixel/action平滑proxy不等物理safeauthority。QP需要active tube上的gradient/feasibility，不是只target-boundary非零足够；例如h=x²−1、x=0、初ε=1而开始收缩时gradient0即可无解。finiteEM仅一阶线性化，83承认nonlinear residual并只报告终点经验零violations，不能写成无条件hardconstraint证书。

Theorem4.2/A.2(151–162)把Girsanov的path KL直接改成final marginal KL等号，通常只能经data-processing获upperbound；连续white-noise当可导ξ的pathwise保证也未由有限离散实现建立。不采用closestdistribution/novikov-free/pathwise safety等命题，但这不消除finite sampled-noise/QP接口与实测结果。

PushT预训DiffusionPolicy/actionchunk15、100episodes：barrier为平均相邻velocity平方变化/Δs，不是物理jerk或最大每step限幅。DDPM100baseline reward.92/12violations/47.05ms，same100stepCBF .92/0violations/62.92ms约34%增时；DDIM10 .90/16/4.57ms不可拼成同预算支配。hardware/precision Not Disclosed。直接反侧§6(136–137)：learnedCLIP barrier可给unsafe高分；latentSD1.5 decoder非diffeomorphism，pixel不保exact。Lorenz部分只领域应用，不采用/不扩science。

Owner MULTIMODAL-GENERATIVE-PARADIGMS Ch24 DDPM sampling配置(139–148)已有finitechain/noise/solver验收、149后point-guidance，未有“收缩tube把init可行性与final proxy约束分开→每步noise-aware QP→finite residual/feasibility”的采样接口。拟在sigma/schedule段后加1–2窄段，限制只生成proxy候选、noise/constraint/solver身份、QP不可行/decoder失配/超时则返回已验收普通sampler或拒绝候选；真实动作仍Ch26controller提交，不双写。Ch23收尾/Ch25开篇已实际读。理论争议精确隔离，不采无条件安全或KL最佳。
