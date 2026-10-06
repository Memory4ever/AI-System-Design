# 02/20 第二十五有限证据包：Readout edit 与 semantic endpoint

## 2602.16545v1 — Let's Split Up: Zero-Shot Classifier Edits for Fine-Grained Video Understanding

2+1+2=5，拟 MULTIMODAL-REPRESENTATION Ch23 窄差额深入，待 root 必要原源/actual owner PRE。exact-v1 官方事件轻核无可见撤回/勘误；复用同ID日期桥，lower2026-02-19T09:00:00+08:00，Registered2026-02-19T02:48:54Z+1秒为upper10:48:55+08，非精确公告点。必要原源 V3_REVIEW_2602.16545v1.html 经extractor非空行：§2 70–80、§3 82–139、§4 141–157、§6.1–6.3 221–244、§6.4 538–545、§6.5–6.6 595–616。作者材料非复现。

原 mixed-granularity video classifier 已编码一些细粒度差异；把同 coarse concept 的 fine-class weight 均值作 base，差向量作 modifier，文本相似检索可迁移 modifier，或以既有类别/字典监督训练384d-hidden MLP 对齐 text→weight。新子类头 w_s=w_c+v_m，backbone/text encoder冻结；zero-shot 指无需新子类video，不等没有先验训练/标签监督，modifier可跨类别解耦只是采用假设。SSV2人工粗类分区与FineGym既有层级形成互补训练/测试切片，MVD ViT-Small/Kinetics400、4A100/basebatch18、CLIPL14；low-shot训练batch16至100epoch、alignmentbatch10至100epoch，EMA early stop有train/validation措辞，不当严格统一预算。

Generality 是目标子类 accuracy；locality 是非目标新旧 correct-count ratio，1不保证逐样本预测相同，旧头冻结也不避免新增logit竞争（工程推断）。每次独立split均值不是串行累计多次edit。外置VLM只在原model预测coarse处gate，perfectlocality为不同接口。三次SSV2A消融检索general45/local98.9；alignment+1.3，fullone-shotgeneral33.6/local0对 isolatednewhead48.4/local98.4，不推广通用最佳。更多子类locality小降、objectcount/success/interaction困难，continues/deflected新视觉区分反例；encoder没有信号时头部编辑无法补造。训练/字典/文本映射/验证费用保留，inferprecision/batch/concurrency/latencySLO Not Disclosed。

Actual Ch23:69–88已区分encoder可读信息/任务head与probe，但未承载从既有classifier weight分解base/modifier生成新readout、及冻结旧头仍受新标签竞争的接口。拟在readout论证后单段，分别验目标泛化/非目标逐例稳定，保原coarse-label或少量标注isolatedhead回退；不授模型新事实、完整disentanglement或全局locality。请求Ch23该段+own末注窄锁，尚未写。

## 2602.16664v1 — Unpaired Image-to-Image Translation via a Self-Supervised Semantic Bridge

2+1+2=5，拟 MULTIMODAL-GENERATIVE-PARADIGMS Ch24 窄差额深入，待root必要源/actual owner PRE。采用自然图像生成机制，不以医学应用重新引入暂缓AIforScience。exact-v1事件轻核无可见撤回/勘误，日期桥lower09:00/Registered02:51:52Z+1秒upper10:51:53+08。原源V3_REVIEW_2602.16664v1.html §4.1–4.3:125–167、§4.5:282–288、自然图像§5:301–310/319–323、§6:327–330、匹配运行配置E:1613与自然图像F:1620–1623。不遍历临床附件、不采用Theorem4.1为实际certificate。

固定DINO patch encoder/PCA近似共享几何y，各domain独立训练本域VAE latent→自身encoder endpoint的bridge；endpoint N(E_phi(x), b²I)改变无结构Gaussian prior，而非只额外条件。源可directembed或sourcebridge ODE inversion，然后targetbridge反向生成；不需跨domain paired training，但给定y条件独立/oracle alignment是模型假设，DINO并非oracle证明。b=0只减随机性，不采用作者strictfidelity保证。自然SiT/ImageNet1k256全模型再FT、DINOv3L16/PCA16/zero-init projection，endpointchannelaverage/b1；SD3-M/PCA32 attention再FT在1.2M LAIONsubset(avg1200×1400)。不是无成本zero-shot，baseline额外训练/conditioning不一致不授因果唯一收益。

每类30 Horse/Zebra或Apple/Orange；scene35real+15FLUX、object60real，100+/200+prompt-image pairs非独立image人数，GPT5prompt与CLIP/DINO/LPIPS等代理非semanticGT。scene结构metrics只luminance，object不同接口不合并。H200batch1墙钟均值跨hyperparams不是tailSLO，trainMI300；新增encoder/PCA/bridgeFT/inversion/vectorfieldcontrol费用不省。强结构prior适合appearance/style变化，却抑制lizard→dragon等大形变，放松prior又损background；silhouette/sketch/abstract域表征gap会失效。并非通用truth/fidelity或大几何编辑保证。

Actual Ch24:176–202目前有Gaussian FlowMatching、solver与OT/ASBM coupling，尚缺encoder-centered endpoint与独立domainbridge通过共享y组合的选择。拟在Gaussian endpoint/ODE后单段：声明encoder/PCA/domainalignment、variance、projection与sampler身份，保appearance/geometry冲突和训练/求解费用；prior不合时回原Gaussian/inversion或显式mask/inpaint，不采任何临床效果。请求Ch24该段+own末注窄锁，尚未写。

## 停点

两项必要源已实际读，普通工作不称external；待rootPRE及窄锁。前二十三包两项和16707另已有必要审批，不借此日级完成。没有stage/commit/push。

## 独立处置追加（2026-10-05）

16545 Ch23 body83/77–91完整邻接/own1289与16664 Ch24 body184/180–194/own2073 root非作者实际POST通过，两锁释放，note已同步。
