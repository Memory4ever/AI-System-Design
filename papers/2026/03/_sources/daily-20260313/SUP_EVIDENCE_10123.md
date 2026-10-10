# 2603.10123v1 必要证据与中心争议

公开事件夹证Mar12 BJT已由非作者首批准入确认；评分2+1+3=6，以对位置退化解释的反证信号深入必要理论和评价。原件为 `SUP_CORE_10123.raw/.txt`，实际200响应见 `SUP_CORE_FIRST_MANIFEST_RESULT.json`，精确v1，没有核实现或复现实验。

## 实际读到的必要内容

已读§1 Scope、§3.1–3.2 Eq1–3、§5 Fig1/eq8、§6 Figs2–3、§7 Limitations、Appendix E.1–E.4 Eq45–52、Appendix F Eq56–61、Appendix G全部训练/评价协议。只对中心命题追到这些位置，不遍历无关证明附件。

- Scalar toy：M_ij=1/i(j≤i)，N=(1−α)I+αM。固定均匀causal mixing下幂矩阵描述多层位置路径；residual零跳路径贡献(1−α)^H δ_Lj。该toy的路径结构不等于真实Transformer每层Jacobian。
- 实际proxy：Appendix F选固定all-ones vocabulary probe u，s=∑logit_v，测ρ(j)=||J_j^T u||₂；原文明确ρ不恒等Frobenius norm。作者再以J_j≈(N^H)_Lj C的factorization解释形状，但该factorization本身需要额外条件。
- §5受测Qwen2-0.5B、24层、hidden896、L2048随机初始化；RoPE/NoRoPE比较Spearman0.99。§6预训练比较200 NQ序列/p16–p84，另100-step微训练。Appendix G仅首60 NQ examples，50训练10held-out，AdamW5e-4→5e-5、weight decay0.1、clip1、batch1；chunked eval来自训练池，与vanilla held-out人口不同，且边界对齐。GPU、precision、seed/repeated initialization未披露。没有直接retrieval accuracy测量、没有RoPE intervention后实际任务质量因果证明，作者Scope也明确Jacobian不直接测retrieval。

## 必须保留的中心争议（审阅者推理，不冒充作者结论）

1. Appendix E.3把“标准Kaiming/Xavier q/k投影条目O(d_k^-1/2)”推成scaled score q·k/√d_k→0，再声称score pathway消失。对于常见variance-preserving输入，每个q/k坐标方差为O(1)，独立q/k的dot-product方差O(d_k)，除√d_k后方差仍O(1)，零均值不等于score逐样本趋零。原文没有在该段补足会让q/k坐标方差一起趋零的输入/初始化条件；因此不能将均匀mixingtoy无条件升格为真实标准初始化“exact universal topology”。
2. E.4从真实局部δ_ij I + A_ij W_V W_O的不同特征矩阵/残差路径，直接抽共同γ^H并因式分解成scalar N^H。矩阵乘积与残差path的组合一般不是同一个位置无关C的scalar倍数；此处≈不能被§5/Appendix F语言“exact/exclusively/rigorously”替代条件证明。
3. §6正文200序列预训练对照、Appendix G的10held-out微训练/训练池chunked人口不能拼成同一“普遍标准pretraining不能克服”的保证；G正文说two sets from held-out与随后chunked实际从train pool选取的协议亦有冲突，不能代作者修成统一holdout。局部proxy曲线和100-step结果不证明真实回读、所有初始化、所有长context或所有位置干预。

结论暂拟**争议 / 暂缓**：保留“在声明的均匀causal residual toy下存在非均匀位置路径”及实际proxy observation作为报告上下文；不采用真实Transformer结构必然、score pathway普遍消失、factorial retrieval impossibility、RoPE工程无用或标准训练普遍无法克服。不能因深审发现争议删池/降分；该家族仍当窗候选，中心理论转接与行为命题隔离。需要独立Source复核确认这些具体数学断点及受限终态，后续若有补足的初始化/feature-factorization证明与真实retrieval验证才重开。

## 当前Books比较（只读，无写锁）

已完整加载当前Books所需三份docs，按ROADMAP选择 `MODEL-LONG-CONTEXT`；实际读Ch22开篇到“共同前提”及相关Ch14 causal定义。Ch22 `Effective utilization 为什么不能由长度推出`明确将训练长度分布、Attention pattern、position mechanism、task与evaluation分开，并已有“RoPE旋转保持范数不保证内容对距离单调衰减、正确材料可见也不等于可使用”的具体正文；Ch14 §causal mask只定义合法读取顺序。现有正文没有无条件归罪RoPE，也没有因toy假设推出普遍初始化定理。因此当前不需要用未成立的中心强断言修书，暂缓不是“已吸收新定理”。Books新写0。新scalar toy若后续独核成立且有长期差额再请求root owner，不自行写入共享Books。

停止：非作者mar13_admission_review已实际核上述精确v1必要原件、数学转接争议及当前Ch22/Ch14 owner，支持6分、反证深入完成与争议/暂缓Books终态，记录在 `SUP_INDEPENDENT_REVIEW_20261009.md` §5。不是外部正文blocked、不是全稿已核、没有Books写入或DAY。
