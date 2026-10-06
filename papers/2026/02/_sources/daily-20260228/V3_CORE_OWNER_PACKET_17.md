# 第十七包：AB10前三个必要命题与旧公开纠偏（待非作者复核）

只继续已校准具名22968/22988/23008，不扩来源池。精确v1完整题摘与当前Comments已读；FETCH_AB10_CORE为2026-10-05T20:56:09～14Z，HTML必要支持/对应对照/直接反侧足即停。以下未计安全终态，无Books lease或写入。23050 NeurIPS2021同题同作者原页已实际读，归旧公开身份，不列本窗候选；详见IDENTITY_CORRECTIONS。

## 同ID arXiv事件日期与家族限制

22968原Submitted 02/26 13:07:31Z、registered02/27 02:59:14Z：公告政策下界09:00，上界10:59:15+08；22988原Submitted13:33:25Z、registered02:59:45Z：09:00～10:59:46。原始身份字段不授精确首公开时刻。同IDmetadata只支持arXiv事件上界，不替代已有更早公开正文。23008 Submitted13:50:57Z、registered03:00:16Z的09:00～11:00:17仅为arXiv事件：ICLR旧公开线索尚未恢复pdate，本项暂不确定当窗家族。

## 22968 Certified Circuits，2+1+3=6，拟中心争议暂缓、不Books

[精确v1](https://arxiv.org/html/2602.22968v1)必要blocks30–97（机制/评价）及110–129（只为中心保证的假设/结论）实际读。原有circuit随concept dataset变化；用Bernoulli deletion平滑任意permutation-invariant discovery A，再将每个vertex的in/out概率以tau>.5门控，低置信弃权。增量是把数据扰动稳定性变成条件证书，不是把稳定circuit认证为概念真值。

**最小反例、到此停止证明扩读：** blocks59/116定义thresholded三值mask，62声称edit distance<r后已认证in/out仍然如此；114另定义不弃权majority label，126给r=floor(log(1.5−tau)/log(p_del))，128却只证明majority(D')=majority(D)=thresholded(D)，并在129称其为membership invariant。取p_del=.8、tau=.95、A(D)=1 iff D非空，这是满足置换不变的合法binary discovery。D含14个同概念样本，p=1−.8^14=.95601953488896>.95，mask=in；删1个成D'，p'=1−.8^13=.9450244186112，mask=abstain。r=floor(log(.55)/log(.8))=2，edit1<2。majority仍1，**认证mask却改变**，与已写中心集合保证不相容。该反例先用真实平滑概率，有限MC的置信估计不能修复两种不同输出的逻辑等同；不声称具体1000次实验必触发该样本，也不检查全部RS-Del外部证明。

实验为受测ImageNet class-specific ResNet50/101与若干OOD，known class指定class-specificcircuit；置信/稳定性不证明因果概念、deployment中不知类别时的完整模型替代。pruned cACC与component数是作者有限结果，不把争议扩成全部经验结果无价值。保留合法majority-label条件分析作为未采用背景，中心认证集合保证暂缓；重开须精确修正mask-vs-majority结论、阈值/扰动证书，以及相应实现/评价人口说明。不进入Books；评分来自原准入命题，不能用降分或EX隐藏反证。root实际最小原块与反例核完前不计D安全终态。

## 22988 RKSP/KSS，2+1+3=6，拟Ch28一段

[原v1](https://arxiv.org/html/2602.22988v1)blocks39–83/98–144/245–258/261–275实际必要读。loss/gradient只能在开始更新后报警；机制用同输入的相邻层residual对、同X-based whitening及DMD拟合局部operator，过滤大mode residual，测near-unit质量及eigenvectorconditioning。nonlinearity ratio是拟合可靠性flag，不是纯非线性量；near-unit mass为risk score，既非谱半径也非校准概率。KSS不是改变optimizer矩阵sign：在抽取层的随机低秩DMD上增加unstablepenalty与near-unit target软惩罚，付额外forward/谱分解/梯度成本。

对应Table6约11%开销匹配的generic residual-L2/Jacobian/activationvariance与两个单term去除，支持作者No-Norm高LR设置下的有限干预差异。Table3/4 clipping、normalization、SAM/Lion及Table13/14 muP/LAMB仍是不同可共存路径，不宣称“只有KSS可稳定”。0.995 AUROC属于associative-recall normalization sweep，其中几乎所有阳性来自No-Norm；不等于每个normalizer内部、任意recipe/OOD的同等识别力。ECE=.283表明概率映射有限校准，不由AUC授权自动终止。Pre-LN/RMS有很高rho但仍稳定，non-normal transient、局部拟合误差、阈值与有限时间均是直接反侧。仅forward的7B/LLaMA统计不是7B KSS训练有效性证明。

4×A100-SXM4-40GB；模型1M～350M、batch16–32、5–20epochs/warmup100–1000、AdamW、seeds42/123/456、randomrank32/N2048、每10–20step抽50%layers。Table8 realLM稳定/PPL同时改变maxLR，不能归纯regularizer；Table7合成任务24trials，CIFAR5epochs仅sanity，precision、并发/SLO及frontier长训未披露。全DMD单层2.5–3.5s与作者8%–12% training overhead分别报告，不折算成端到端saving；有严重谱拟合噪声或正常recipe已稳定时回退normalization、clipping与heldout回归。

实际owner `TRAIN-PRETRAINING` Ch28 606–644与1245–1285完整邻接已读：616已有activation covariance/gradient-spectrum early sensor，620–622要求matched干预，1251–1260已有non-normal瞬态分责；未承载**相邻residual拟合的near-unit风险与基于同operator的双项soft谱shaping**这一具体替代分支。拟在瞬态放大小节后仅一段＋ownnote，保区分risk ranking/概率/干预、抽样谱成本、拟合条件与旧正常配方，未请求扩大理论普适保证。

## 23008 EMPO²，2+2+2=6的原准入保留，家族日期待核，暂不授本窗候选/Books

[原v1](https://arxiv.org/html/2602.23008v1)blocks24–47/54–79/88–95/100–110/118–123/129–138实际读。memory检索/反思本身成熟；窄增量是memory-conditioned rollout既用同提示onpolicy学习，又移除tips让同policy无memory路径学习高advantage动作。Table3保behavior分母tip-conditioned、student分子no-tip；主文41“替换存储logprobs”与95允许no-tip旧分母只是不同有偏实现选择，不能合并成一个已证unbiased协议。token概率低于delta便mask advantage、PPOclip都改变学习人口；单步ratio不自动校正整条state occupancy。self-generated tips非独立teacher真值，environment reward仍为有限bench验收。

直接去掉有memory onpolicy/offpolicy任一分支的两任务曲线、p/q极端退步、记忆移除test提供局部对照，不授全部三组件独立等预算因果。Qwen2.5-7B、ScienceWorld19tasks训练前5variant/test20variants，WebShop三seed（部分baseline引用旧结果、Retrospex重训去heuristics）；8A10040GB，ScienceWorld每step32token/总4500/30step、WebShop512/15step、p=.25/q=2/3。50.4s/iteration≈19% rollout部分与更长response分别付费；136的1−p=.25与正文p=.25矛盾，不采用其概率乘账。memory retention/reset/top10状态与training policy共同改变，不外推真实web安全或生产memory服务。

实际owner `TRAIN-GRPO` Ch33 1587–1615/2238–2274与Ch77 600–634完整邻接已读：1599–1604虽具名EMPO²及临时scaffold→参数原则，未承载**conditioned behavior分母与unconditioned student分子、三种rollout/update组合、低支持mask和memory-free测试**；Ch77拥有derived tips生命周期而非policy更新公式。若日期/本窗事件可成立，才向Ch33该scaffold段附近提一窄段，不制造Ch77论文名缺口。目前普通技术owner已备，但官方首公开note必要入口受阻，本项只精确日期保留；重开材料为samefamily官方pdate/历史公开正文和具体本窗实质新事件，不能以arXiv晚上传新计。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22988：原必要blocks56–83/123与actual owner独核；Ch28正文1271/完整1251–1281/own1813 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
