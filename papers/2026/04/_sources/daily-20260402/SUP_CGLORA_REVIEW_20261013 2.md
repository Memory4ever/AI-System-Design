# CG-LoRA `2603.29824v1` — output-alignment 机制与最优性反例

rootAB具体潜力已校准，拟 `2+1+2=5`；作者实际读精确v1必要完整§3–6，[原件](SUP_CGLORA_CORE_20261013.json)。纠错影响本文中心证明，已加深这些直接事实但不读无关所有附录/代码。Source/day/Books待独核，不授实现或复现。

## 实际机制

只对齐首步梯度/权重Frobenius不等最终预测匹配；在固定NTK线性化、LoRA因子first-order忽略ΔBΔA、squaredloss的条件下，比较FFT/LoRA经Jacobian后的prediction残差。KFAC近似当作等式假设，input与outputsignal二阶基白化lossgradient，选子空间，balancedfactor/scaling后初始化；用layerwise随机sketch/QR/SVD避免显式大矩阵。这里output信号δ与lossgradientμ是不同对象，不可混同。实际有限网络/有限训练不是NTK真值。

## 决定性的中心反例，不采用“全局最优”

§4 Prop4.5 Eq10自己给tail从2r+1起的lowerbound，紧接(i)却称双边都选top-r、得到tail从r+1起的误差“hence solves”全局(3)。此推断在同一NTK/KFAC理想条件就不闭：令whitened F=diag(3,2)、r=1，S/T为identity（或等比例使Kroneckeridentity），两边都取e1留下第二对角2，误差2；令B0=e1、A0ᵀ=e2，则tangent子空间B0ΔA+ΔBA0分别覆盖row1/col2，可表示该两个非零对角，因此prediction残差0。§4末自己说明disjoint index可达2r-tail下界，却称经验可能suboptimal；经验理由不能认证(i)与Thm5.3的全局最优性。仅保curvature-guided候选子空间/受限经验，不采exact最优、LoRA必需二阶或rank选择普适规则。

其它必要边界：Prop5.1声称fullcolumn L/R推出unique invertible Q，仍需projectedgradient/selectedF非零rank条件；M=0时后续normdivision也未定义。§3 Remark3.1说squareloss Lipschitz，但无boundedprediction/residual域不成立；CElogits可有boundedgradient，不移植成所有predictionloss全局界。§5.3梯度hμᵀ与最初W[d_out,d_in]方向、UT乘h/US乘μ及Algorithm2 shape记号不协调，不照录为完整可执行实现。本次不追appendix以回避这些直接反例。

## 必要实验与不能归因

RoBERTa/T5-base GLUE，A40，r8，初始化512samples/B16，训练B32一pass，3seed mean/std，validation六LRgrid。全方法η=2sqrt(r)，不是§5分析常用1/sqrt(r)直接同配方。比较shift时按实际起点区分：compensated从W0，另一从W0+ηB0A0；标签“shift/no-shift”易反义，不混写。

RoBERTa非补偿分支CoLA80.53±0.43，compensated72.77±5.15；full80.24±1.22，MNLI full86.89高于85.51，不宣传全任务超FFT。T5结果混合，MNLI85.32低于LoRAOne85.49、MRPC84.39低于84.47，‘randomheadnoise白化收益’是模型/任务条件解释非独立干预证明。T5使用multi-token classprob而LoRA-GA原first-token，本文统一评价与baseline重实现，不认证任意原实现优势。

Table3 3.58s/509.95MiB vsLoRAGA7.01s/1.28GiB只RoBERTa-CoLA512样本初始化；额外2 backward被sketch策略抵消，不等全部finetune两倍快/峰值整模型显存。Precision/完整duration/服务SLO Not Disclosed。搜索、激活/outputsignal收集与layerwise低秩数值成本均计。

## 独核请求

保5分原具体命题，不因证明争议/审阅成本改分或从池删掉。请root独核上述2×2反例、实际方法和受限质量/成本；决定是否中心理论隔离＋仅采用输出目标/curvature取舍，或安全终态争议。未作BooksNC/整合。

root actual独核结果：已实际原§4 NTK/KFAC/fulltangent Prop4.5/Eq9–10整段，核算2×2反例成立，中心D/noBooks资格通过；保持2+1+2=5，投入因实际纠错加深不改分，不凭此认证其它全部实验或完整实现。当前official v2Jun7改title，完整当前AB仍同curvatureoptimal中心命题、无expliciterratum/withdraw标记；本次仅v1纠错，不倒灌后版，[正常日证与当前metadata](SUP_STANDARD_DATE_SIGNALS_20261013.json)。
