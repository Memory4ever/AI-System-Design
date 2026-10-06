# RandMark 2603.10695v1：必要Source/概率资格争议/actual owner ready

仅Mar12 BJT补充日。Anna Chistyakova/Mikhail Pautov，完整v1题摘/准入见独核§19与SUP_ABS3_10695，日级arxiv夹证复用§23/SUP_DATE3_10695。当前唯一v1、无venue/withdraw/correction信号；SubmittedMar11T12:08:05不当公开。官方 https://arxiv.org/html/2603.10695v1 GET200/251794bytes/UTC2026-10-10T02:43:13.441955，SUP_CORE_10695.raw/txt/MANIFEST/RESULT保存身份。首次调用manifest误传相对repo路径导致本地ROOT重复，未发请求；改传manifest basename后成功，非外部受阻。

实际读§3.1–3.5完整Problem/threat/机制/Eq1–32/lemma及proof（175–3336），§4全部两VFM/注入/fine-tune/prune、§5全主结果/完整Tables1–2/§6（3337–3654）；公式长投影按行段空白压缩阅读，不删原件。图2/3只读caption与作者解释，不认证像素精确曲线/质量。未读未链接的Supplementary architecture/费用、代码或旧稿；必要核心支持与反侧足够，此处停，不把optional未读造blocked。

## 原判断与实际增量、评分

classifier-output水印不能自动承载VFM downstream heads变化→本稿联合改source VFM和encoder/decoder，把随机变换秘密图像的hidden-representation bit统计作为functional-copy检测→需要分别核验位/图像/model随机性及有限fine-tune/prune后的检测操作点。新增不是数字水印/版权概念，而是模型表示适配后的随机观测接口与拟低FP/FN资格。

拟 **2+1+2=5**：新随机表示检测的强概率适用资格/直接设计反证D2、单检测组件R1、独立性/统计单位和可核验变换约束可复用D2；不借法律/多种模型抬Reach，未把成熟Chernoff/Hoeffding计算计新贡献。中心概率保证与已具体统计纪律冲突，受影响内容必要深入实际已完成；拟争议/暂缓Books0，不EX/缩池/已有覆盖新实验。

§3.3把x+Gaussian变换、message给encoder，联合VFM/decoder，loss控制原feature偏离及K次decoded-message距离；ρ是K个变换的平均Hamming errors，Eq7检测率R=1/N Σ1[ρ≤τ]。二值decoded bits实际连续训练/rounding细节Not Disclosed，§3.1 encoder声明R^s×bits→R^k但Eq2又把e输入R^s→R^k的VFM，§4文字又image/message processed→VFM，与v1文字接口类型不完全一致，不能补造artifact路径。此处仅隔离精确实现，不推有限实验未执行。

## 必要数学反侧（只限强概率继承）

1. §3.3 Eq8假定各位相同match边际r，即按n次binomial tail计算；相同边际不是相互独立。取32位的m与decoded message全部同时match或全部同时wrong，两种各1/2，则每位r=1/2，但τ5的真实单次P(error≤5)=1/2，不是binomial tail；K变换平均ρ又不自动是单次n-bit计数分布。该反例只说明Eq8明写equal-marginal条件不足，**不反§3.5明确独立Bernoulli的条件定理，也不声称实际训练位完全相关或实际FPR=.5**。
2. Eq14称R是N独立Bernoulli和，并将参数写成Eq11的单bit match概率r(Ω|x)，而实际每图pass事件为mean-K biterrors≤τ。需要bit→每图pass桥接和跨图条件独立性；即便IID公平bit、n32/K1/τ5，按Eq6每图q=sum(j0..5)C(32,j)2^(-32)=0.00005653710104525089，而r=.5，不能直接代换；共同随机选一个suspect model会同时改变全图decoded结果，独立图像或Gaussian变换本身不能直接授model population上的N独立检出事件。Eq13位匹配CI不是自动的每图pass CI；不用bit相同率代model detection率。
3. Eq7归一化R∈[0,1]，§3.4 Remark1却以Rbar750/600并称保证低错误；§3.5另把R改为Σ计数且Eq17又用message长度n而非图像N。可修成独立per-image count模型，但**本包不替作者静默统一**。在真正独立Bernoulli计数下，Chernoff/Jensen/Hoeffding逻辑可保；proof末§3.5 Eq32自己要求估计lower endpoint p_hat−epsilon>d/n，单有真实p>d/n不保证每次有限样本下这个估计域成立；若endpoint越界需另行保守界/截断。不能把这些独立计数条件继承给未桥接的实际协议。

上面限制中心“by design低FP/FN保证”，不否定所有随机bit协议、有限copy检出、Chernoff成熟定理或作者全部数据真实性，不推伪造/水印必失效。Eq1还将R^k encoder w与n-bit decoder相减、gamma小大方向给弱条件，只列精确版本接口疑问，不把排版疑问当实验反证。

## 关键评价及费用

CLIP/DINOv2公开预训练，ImageNet1000随机secret图、每图32随机bit；ecommerce18175/9class、FoodSeg103 7118/100+类，正文称三dataset但此列表两类，随后classification头/ImageNet另说，不自动算同训练人口。fine-tune全部VFM层AdamW10epochs，unstructured L1 prune20/40%仅基线变换，不是有意水印去除/抽取/蒸馏全覆盖。理论Remark1 n32/τ5/M1000/alpha5e-6，不认证该1000模型独立校准实际模型人口完整公开。

Table1 CLIP segmentation/WM：1/3/5epoch RandMark .32/1.00、.52/.99、.55/.97；smoothing .14/.27、.36/0、.46/0。有限matched epoch支持这一taskadaptability取舍，不等原clean VFM效用无损或所有heldout任务保真。Table2 DINOv2 positive detection classification .870、segmentation .750、prune20/40均1；negative DINOregisters/CLIP0。完整负侧：Eq7秘密图像协议仍有13%/25%图像未pass，不是模型抽样人口FNR，此组negative0不能授未知model低概率保证；方法在prune20与ADV-TRA同1不是全场景严格领先。Fig2平均同1000用于注入的图，不把它改称未参与训练的新secret图holdout性能。Fig3 covariance近0是特定protocol观察，不自动认证位及跨图独立。

基线classifierhead CLS+patchmean、norm/dropout/linear、ImageNet训练与VFM本体接口不同，不能唯一归因于randomwatermark。τ/σ/K/λ/e-d架构/训练预算、precision/hardware/fullquery成本和独立seed/CI/功耗/SLO主体未披露；Supplementary费用只被引用，本文必要正文足够支持受限争议，不外推部署认证。联合VFM训练、秘密图像/bit存储、K变换/每model全图query、decoder及下游效用回归均计费；不授法律所有权、防泄漏/防复制或未知adaptiveattack安全。

## actual owner与最终提案

ROADMAP唯一PLATFORM-SECURITY Ch72。实际完整197–209模型水印与泄漏分责→门限shares/所测null分布→个性副本trigger/逐client验证→generator/decoder lifecycle；215–221 soundness/unforgeable责任与行为取证已顺读。现正文具体说有限null与query/模型人口不能推任意模型固定误报、白盒/变换/发行identity与独立取证回退；**没有吸收本稿新随机表示机制/数值/概率证明**。Ch66统计单位只能handoff，不另owner。

拟保留candidate，5分必要深入/中心统计桥接争议暂缓Books0。当前不把不合条件的概率定理写成新长期定理，也不以主题相似授已有覆盖；无需造书稿PRE。重开只需本精确协议的encoder/VFM/decoder一致接口、ρ随机单位与bit→image事件映射、相关性条件/有效置信界、归一化vscount阈值及对应模型人口/质量预算原证；到达只核这些依赖。独立reader必要原件/actual owner已核并经root接纳，详SUP_INDEPENDENT_10695.md；正式45中本项5分争议Books0，不授强保证/Report DAY。
