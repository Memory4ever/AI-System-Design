# Modality Gap `2603.29080v1` — clean-NN 恒等与概率保证反側

root完整AB潜力已校准，拟 `2+2+2=6`；实际读必要v1§3–6，以及只决定拟采用命题的A.3/A.4/A.5（未读A1/A2其余附录、code、全version）。[必要原件](SUP_GAP_CORE_20261013.json)；Source争议/局部采用待root，不授生产/复现。

## 实际机制和可以保留的恒等

retrieved modality点xi的affine差方向与v正交，即v·(xi−xj)=0时，共同平移所有xi不改变与固定query y的squared-distance差：新增项2αv·(xi−xj)=0，NN/ties保持。这是明确几何条件，不等所有任意modalitygap。作者用retrieved-text PCA的orthogonal complement投影mean gap，再平移；actualspanning fullrank时无非零orthogonal分支，经验截断/approxPCA不继承exactclean保证。无需finetune但PCA/mean估计/索引重建和referenceidentity仍付费，large-vocabulary RAG不从10/100class结果自动泛化。

原文gap定义local x−y/globalμy−μx却称average相同，proof3.1 gradient符号/τ记号与文字亦不协调，未核A1/A2，不采用所有contrastiveGD形成gap/完美alignment定理。A5展开α/sign有漏，但上述distance-difference代数可独立核，不照抄记号作实现。

## 必要中心概率反側

A3 Lemma为y−g缩norm，后proof改y+g；Eq32两边印同event且声称严格大于。更实质的是Eq34–38从zero-mean variance下降推出相同threshold尾概率必降，没有分布/尾次序条件；covariance=σ²I不够。

已给与主文明确零empiricalmean、每vector isotropiccov条件相容的有限反例：texts x1=(1,0),x2=(−1,0)，queries (±.8,.6)均unit，gap=(0,.6)正交两modality affine差方向。让η两坐标独立均匀±3，noise1=η/2、noise2=−η/2，每点zero-mean/cov=2.25I、两点noise empiricalmean=0。两noisytexts仍相反、同norm，故只看(2+ηx,ηy)·y判断NN；未close对query1四case有3个正确=.75，close到(.8,0)只有2个=.5；query2对称。故闭gap严格降低这里robustness。若作者另需独立pointnoise/高斯/小幅/旋转尾序假设，必须明确，不从covariance自动继承；exactempiricalzero又要解释centering后的jointnoise。A4一般covariance仅yTCy下降也不能推出概率改善。这个反例不否认特定Gaussian实验的实际走势。

## 实测范围及不能证明

§5 openclip CLIP/SigLIP，CIFAR10/100及A-OKVQA。controlled independentGaussian textembedding noise K100平均，所示图有cleanaccuracy不变/robustness改善；不是所有noise族。Quantization仅embedding向量fixed[−3,3]intervals，bothimage/text，确定性K1；非网络weight/activation量化、GPU索引端到端延迟或SLO。量化noise有nonzero mean，经验最优是quantizedspacegap不是originalgap，不能当proof满足。

Rephrasing实际每题采3wrong+1correct paraphrase替换候选集合，K500；作者明确noise均值/方向条件不成立，测accuracy under changedanswerchoices而非同candidate NN robustness，不能混两指标或签训练输入perturbation普适保证。具体paraphrase资源/seed/hardware/precision未在main披露，未因此无限读全附件；限本图局部对照，不采universalbug/所有noise不伤质量。

## 独核请求

保6分实际几何/robustness增量，纠错按必要内容加深不改分/删池。root需核同假设finitecounter与clean恒等，决定centreD/noBooks，或仅有条件平移机制＋实测Gaussian/quant context而隔离概率定理。没有自行BooksNC/结构/正面保证。

实际root Source处置：已实际§3.3 Thm3.4和A3/A4/A5原稿，核原条件仅cov/zeroempirical未要求独立Gaussian，finite±3四dot的3/4→2/4反例成立。中心D6/noBooks通过；clean恒等/有限Gaussian图不否认，不从它们补中心全noise tail保证。正常复合日门/当前v2 metadata与owned上界见 `SUP_STANDARD_DATE_SIGNALS_20261013.json`；不因纠错加深改2+2+2=6，无Books正面写入或日级。
