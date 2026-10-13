# 12998 闭式去偏：必要原证与中心目标桥（待独核）

仅本17补03/16；完整题摘与官方日级夹证有效复用，不重查日期。精确[HTML v1](https://arxiv.org/html/2603.12998v1)、[同v1 PDF](https://arxiv.org/pdf/2603.12998v1)、[当前官方事件页](https://arxiv.org/abs/2603.12998)：only v1无已给撤回/纠错信号，不声称全网无更早正文。作者实际必要§3–6/Tables2–5、A的Prop1/Lemmas1–2/Prop2/Th1全桥、B/C/D/E/F/Tables6–9；只核方法和直接反側，G仅必要caption未看全部生成图、不核artifact/复现。PDF实际p5式4/Th1、p14–15归一化证明、p19–20重生成评价原文，与HTML一致；无截图冒称视觉审阅。

准入：直接投影去prototype span会混删内容→prototype differences属性子空间与几何utility/fairness双目标→变换目标/单位及消费者任务资格要重新验收。2+2+2=6，具体理论/设计反侧深入；不因疑点降分或假EX。

## 必要机制与支持

§3 unit sphere定义selfutility=1−u·e、crossutility=|uI·uT−eI·eT|；fairness是与各group prototype相似度相等的**几何surrogate**，不等EO/真实公平。LLM针对输入生成显式group和多个变体，textencoder后normalize sum得prototype；差向量span为A，线性独立basis后投影（不是把冗余全列直接invert）。共享image/text空间依赖原模型对齐，不等所有VLM/gencond。

Prop1 triangle/CauchySchwarz给unitvector cross score漂移上界，理论在自身定义中成立；不能推出F1/Recall/生成行为下界，§6limitations明确承认此限制。非退化p=||e_parallel||、q=||e_perp||>0且p²+q²=1，Pareto曲线上L=alpha、V=1−p alpha−q sqrt(1−alpha²)，alpha∈[0,p]；smallalpha偏向中和、大alpha偏向原embedding。不能把任意方向的泄漏norm当已校准敏感真值。

## 中心争议：正文目标与证明切换

§4.2式4明确 min_alpha sup_{w1,w2≥0,w1+w2=1}(w1 L+w2 V)，即min max(L,V)，Th1的闭式alpha*却来自A **分别按端点范围归一化**后的min max(L/p,V/(1−q))。A实际L428–435、PDFp14–15明确该步骤，不是HTML错误；目标不同，不能称只是等价整理/同一minimax或对任意固定weights均optimal。

本轮条件数值反例（非作者实验/代码必错）：p=.6,q=.8,E=p+(1−q)/p，原闭式alpha*=.2391598131，V=.0797199377，因此正文raw max=.2391598131；合法alpha=.1291900756时L=V=.1291900756更小。闭式确实使normalized两个loss均.3985996885，故不是宣称归一化版本无解/全部几何理论错，而是raw式4→normalized/实验身份未闭合。Lemma1“every optimizer”和Lemma2“all firstquadrant”在w2=0时也缺严格性（A_perp维≥2可有其他unitvectors同L=0）；正权重、非退化限定可保一些几何事实，不能自行修正为论文保证。

Prop2 p=1/q=0直接选原e只是保留原语义的设计决定，不是证明去偏无必要/全weighted objective最优：w1=1,w2=0且A有非空正交补时unit u⊥A泄漏0而原e泄漏1。受限正文只处理p,q∈(0,1)，不外推该边界。

## 评价与直接反侧

§5两classification population CelebA/FACET、retrieval Flickr30k/COCO、SD2.1 generation限定输入/群体；EO两归并/maxskewcandidatebaseline/uniformSP各不同，不统一成公平真值。Table3原CLIP COCO R@5 83.8→81.1、R@10 90.1→89.0和Flickr91.0→90.4/95.4→94.9；Table6 ResNet CelebA60.7→58.5；Table4 SD原CLIPscore32.8→24.2/显式gender75.4→74.6，不能说任务utility无损。

D三人确有人审但unsure/disagreement画像**重新生成直到一致**，这改变评价人口而非原输出仅标为Unknown；公平/utility top5均按原baseline选，不能作为全prompt/所有性别保证。E FACET排nonbinary/unsure且类少于1000剔除、retrieval单人/性别词筛选再改person，限定测量覆盖，不作开放群体/自然分布公平。§5.2 bootstrapping datasets的±不是多trainingseed；Table8 PRISM单格5与周边不协调不采该格headline。GPT5prototype变体数/温度/审校、硬件/precision/batch/inout/concurrency/runtime/SLO/fullfee Not Disclosed；train-free/data-free指不做去偏训练/额外attribute标注，不免LLM生成、encoder/prototype、SVD/投影、17k×2生成及再生成/人审费用。公开代码链接仅定位，不认实现已核。

## Actual owner 与拟处置

ROADMAP唯一MULTIMODAL-REPRESENTATION/Ch23；actual1–33表示identity和40–94 tensor/semantic→stitch/map/Procrustes/isometry→bilinear/SOTAlign已顺读，Ch24开头消费交接。几何公平和minimax偏好有具体差额，现正文没有该closedform/prototype-difference，不能按“已讲投影”假NC；消费者生成范式非owner，Ch66评价只接协议不重复算法。

拟中心争议安全隔离、保6分候选、不写Books/不授闭式raw目标或端到端公平utility保证，等待独核判断，不先计safe。支持Prop1/非退化Pareto几何与反側保留；不绕中心桥摘写一般投影原则。

一次精确重开请求：给式4的原始/归一化目标、weights/尺度含义和实际实验solver最小映射（精确commit/函数或p=.6,q=.8 trace即可），并明确zero-weight/degenerate分支条件；若修正文/定理须精确受影响版本和实验映射，不泛求所有附件。可选择明确normalized版本并重新限定guarantee，而不能用generic geometry或更晚结果倒证本窗。材料返回只重开本family。
