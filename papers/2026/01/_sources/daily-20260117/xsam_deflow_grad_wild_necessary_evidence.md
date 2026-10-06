# X-SAM / DeFlow / GradESTC / WildRayZer 必要证据提案

已准入且落窗的精确v1，仅必要method/keyeval/directcounter，缓存2601.IDv1-standard-necessary.txt；未实际复现，待rootactual终裁，不以缺recipe造Books长期gap。

## 10251 X-SAM — 拟5必要设计反证/理论深入中心Disputed

[原文](https://arxiv.org/html/2601.10251v1)§4.1–4.3 Eq5–11/5.1–5.2/6.1–6.4。SAM二次gradient与topHessianvector可能近orthogonal→拟去principalcomponent改变sharpnessupdate→潜在设计反证值得核，不能因小CNN拒。§4.1每layergradient归一+concat、eigenvector亦layerconcat不等fullHessianprincipalvector。Eq5/6 Δw^T HΔw是loss二阶变化非ΔH/leadingeigenvalue变化，无法授本段curvature上升/不变因果。

中心更新不一致：Eq11 normalizedperturbedg减α sign(dot(g,v))*g_parallel，g_parallel是投影本身，翻v→−v投影不变但sign变，故额外sign不解决eigenvectorambiguity；Thm5.1 P=I−αvv^T对应无sign/未归一stochasticgradient另一算法，并有不随T消失c2(1+2α²)项，不能当Eq11的O(T^−1/2)到0收敛。T5.2还要eigengap/ΔH/3rdderivative，inequality不是automaticeigenvaluedecrease。NoBooks、不修sign/normalization/proof，重开仅作者统一actualupdate/谱估计和对应严谨证明。

CIFAR/Fashion/ResNet/AlexNet/WRN，RTX4090/PyTorch2/CUDA11.8/SGD200epoch/batch256/3runs/α.2与ρ分别.05/.1；局部accuracy仅作者报告，不用于中心mechanism正面采用；topHessian intermittentpoweriterations成本无完整E2E。中心Disputed保留负侧，不降分或删证据。

## 10471 DeFlow — 拟6标准Only

[原文](https://arxiv.org/html/2601.10471v1)§3.1–3.2 Eq8–12/5.1–5.2/6/A1。Q-backprop穿flowODE贵、single-stepdistill可能压多模态→base多步flow只FM，stopgrad sampledaction后f(state,a)残差Q优化/平均平方预算δ+α自调→与state-only residual不同的可核policy分责，不采“flow无偏行为manifold已解决”。
δ平均E||Δa||²不是逐action安全封套或KL trustregion，Qmean归一criticerr仍在；α自动反馈不证明真实manifoldadherence。OGBench50state+5pixel/D4RL18，fixedgradientsteps/8seedstate4pixel meanstd，O2O buffer；排除bestofN不作全面SOTA。IAV k5/taskknowledge δ.1IAV与1IAV，notuntunedgeneric；推理scale饱和解释criticOOD是作者推断非受控必要因果。fullhw/precision/runtimecost未披露本包不采速度。保留boundedresidual局部实例Only，nondefinitive方法不必造长期gap/精确Existing，无Books。

## 10491 GradESTC — 拟6标准并同步/代数必要核Only

[原文](https://arxiv.org/html/2601.10491v1)III-B Eq5–15/IV assumptions+T1–2/V setup/Eablation。全round重传basis或旧basis漂移→E=G−MA residualSVD orthogonal候选、old+new coefficientrownorm topk竞争，传replacementindex/新vector/coefficientsA使decoder同步→真实跨round state分支而非普通EF命名。d=1.3d_replaced+1只经验调节，消息C=k*n/l+d_r*l+k含必要新basis而非只coefficients。

Alg2写hatG=M^T A而E=G−MA/A=M^T G convention应警惕dimension相反；本窗不授该pseudocode已可执行、不替作者修式，采用仅清楚的basisreplace协议与作者localeval。Eq8把E全部列写firstd也不在d<trank一般精确，orthogonality需nonzeroerrorcolspace，不能泛最优rank保证。IV假设previousrankkconcentrationδ以及interclienterrorcorrelationτ，结果有残差neighborhood非到0/增加client必减少；未逐proof授新guarantee。
LeNet/ResNet/AlexNet(MNIST/CIFAR)、10allclient/local1epoch/LR.01/DirIID,.5,.1；50clients20%只是局部扩展，k128通信较差/k8早期慢，中期可能较慢。ablationfirst/all/fixedd，sumd作计算proxy，singleclientd256~.20s vs5epoch8–10s不等网络E2E。hardwareprecision/seed Not Disclosed；bias/BN不压，其余层不同k/l。Only局部state/codec实例，无Books/精确Existing；若中心execution必须照Alg2则需作者统一形状/实作重开。

## 10716 WildRayZer — 拟6标准Only

[原文](https://arxiv.org/html/2601.10716v1)§4.2/5.1/5.4 T5/Atraining/C2failure。staticfewview sceneencoder受dynamicinputs污染→render-observedSSIM/DINOresidualpseudo mask、freezealternatingmotion/renderer再joint、inputmotiontokenzero→消费动态输入重建静态scene的具体branch，**不是预测dynamicworldtransition**。PSNR>17筛样/patchKmeans跨frame/Grabcut/DINOv3frozen以及COCOGTpaste，不能说全无external监督或guaranteecompleteinstancepurge；rendererr可误为motion。

D-RE10K74Internetsequence humanmotionmask staticregioneval vs50tripodiPhone fullimage，2/3/4input6target、同sparseviewbaseline/validation调后iPhone；不同metrics区域不合并。H100BF16+TF32/AdamW/pretrain100k/batch8GPUaccum2/后maskbatch32，GPU总数/endtoendlatency Not Disclosed。CopyPasteOnly18.2/11.1 vsPseudo53.9/45.3，combined53.9/49.7：不是泛paste充分；DAVIS仅8clearparallaxsequence，部分身体/脚/大objects漏分导致renderfail。全finalstage初训artifact支持该训练schedule局部必要，不授稳定收敛/动态对象绝不泄漏或任意unposed场景。Only受限scene接口实例，无Books/精确Existing。

