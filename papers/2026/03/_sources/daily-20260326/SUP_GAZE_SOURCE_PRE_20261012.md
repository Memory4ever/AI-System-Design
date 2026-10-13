# Gaze-Regularized VLA necessary Source / Ch26 PRE

作者supp_mar26_fresh；2603.23202v1/day25/2+1+3=6准入有效，仅该精确v1。只采用训练期synthetic gaze→KL attentionprior接口与softbias反侧，纠错信号使受影响内容深入，不降分/EX。

实际[exact-v1](https://arxiv.org/html/2603.23202v1) §3.1–3.4/Eq1–10、§4.1–4.2/T1–6及§5必要结论、B444–498/T8、C1/C3/T9与C4、D1–5/T10–13、E1/2必要projection/训练伪码、F777–784限制已读；未独审所有图/影片/代码附件。future-centered序列生成GLC syntheticheatmap，经patch归一与时间加权，KL(G||S)弱bias对齐最后VLM层language-query→visualkeys；globalquery原B445/450是learnedprojection，不把提取attention等同直接nativehead因果解释。动作还是原flow-loss/chunk h50/RGB+language+proprio，部署不运行gaze，非真实在线eye sensor/主动相机取证。futureframes只训练prior，不能当t时已获得新观察。bodyEq4past到t、Eq6±T/F3future与Alg2只预测到t却取future窗口仍口径不闭，不交付完整recipe；E1零热图/零patch分布uniformfallback实际披露不误称无guard。

## 直接反侧/版本冲突

T1 cookiebox/cabinet以及LIBERO10早期反退，T5强λ10退至41.6vsbaseline82，moderate部分task仍退；T8uniform57.1/DeepGaze86.3/GLC95.5与T11foveated78.5<85.9基线支持“训练软prior”不等“删周边输入”。T9alllayers87低于late95.5，不证明late本质唯一；C top10指标是预测gaze mass on selectedpatches，51%非真实人类attention或因果解释。D5真实眼动只用于另fine-tunedGLC的独立变体（94.8vs原95.5），不把本文常规synthetic训练称全真实eye labels/no人类采集费，也不把人类版本写成严格更好。Participants/真实校准人口/样本重叠细节未披露，不以IoU签真实task意图。

重要冲突：§4.1 267–279/T4说已physicalrobot三task、F8–9caption说realworldAloha；同v1 F782–783明确“have not yet evaluated ...physical robot”。保两原证，**全部realrobot收益/迁移/实时与安全保证隔离**，不能把“有成功表”当争议消解；允许只在模拟task上受限训练接口采用，不整体HOLD/改6。原3seed部分simulationprotocol、10/20/30kstepvsT4 20/40k不可合并。GPU/precision/batch/optimizer/lr/deploymentconcurrency/latency/SLO Not Disclosed，h50非50Hz；步数早收益不代表合成prior/训练总费净省。GLC部署删除不抹训练多帧gaze/attentionquery/projection/KL/采集/独立evaluation成本。F训练伪码未充分给参数更新责任，未核artifact/复现，不保完整cookbook。

## actual owner/gap/锚

sole MULTIMODAL-EMBODIED-VLA Ch26，actual完整49–82历史frame/geometricalidentity→future-viewcontrol→12193相机/身体head两阶段→virtualview/zoom→环境准备与input编辑开头，181–204交接模块controller；Ch25/27开篇有效复用。现12193通过动作head改变主动取证，08325改变同一观察render分辨率，未承载“仅训练aux attention prior、部署原观察接口不变”的资格/软bias强反退。拟12193完整末段（第二source marker）之后、下一“主动选择视图还要区分真实取证…”virtualview段之前两PRE+本人静态注，保原段不搬。待reader必要Source/具体gap/PRE及root窄锁。

## PRE paragraph 1

“往哪里看”也可以只作为训练期的软表示先验，而不让部署 policy 新增相机动作或实时眼动输入。一条受限分支从示教视频的时间窗口预测 synthetic gaze，将热图按视觉 patch 归一并聚合，再以 `KL(gaze || attention)` 约束最后视觉语言层的语言-query/视觉-key分布，与原动作目标共同训练；部署仍只读当前 RGB、语言和本体观察。预测注视与所提取的 attention 都是代理，不是人类意图或动作因果真值；训练窗口使用未来帧也不意味着机器人在线已经看见未来。<!-- source-family:SF-2026-ARXIV-2603-23202 -->

## PRE paragraph 2

[必要反侧](https://arxiv.org/html/2603.23202v1#S4)里，过强对齐、均匀prior与直接foveated输入都会明显退化，局部任务与早期训练也有反退；因此给出训练bias同删周边视觉信息的条件分界，而不认证越像人类注视就越好。原文时间窗口/提取实现仍须绑定，正文实机表与同版附录“尚未做实机”相冲，相关物理迁移收益及实时/安全承诺不用于采用。Gaze预测与时间聚合、训练期query/projection和KL、标注/校准及独立任务评价全部计费；删除部署gaze分支不等总费用为零。prior失配、任务回归或费用不合适时，保留原action-only训练、真实当前观察及独立controller，主动相机与virtualview路径仍按各自取证和几何条件成立。

## 自身静态证据注 PRE

SF-2026-ARXIV-2603-23202 — [Gaze-Regularized VLA exact-v1](https://arxiv.org/html/2603.23202v1)，必要§3–5/T1–6及B–F有关prior/反侧/伪码；仅训练synthetic gaze/softKL及部署gaze-free接口，隔离同v1实机正文/未实机附录冲突、时间窗口/提取recipe与实时安全承诺；保强prior/foveation/task反退/真实gaze另变体和全费用，未核代码/复现。
