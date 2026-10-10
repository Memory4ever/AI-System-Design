# 2601.17910v1 — 中心定理争议（待非作者复核）

潜在贡献：operator-agnostic token/task/context weighting composition与收敛条件，改变多teacher适配可组合性解释。2+1+2=5；实际中心理论需深入，不因争议删除候选或降分。原source supplement-core-17910-20261008.json；实际读II assumptions/III token weights/IV normalized product/VI convergence/VII stability。必要日期当日联合核验待独立确认。

III.1按每token在teachers上归一，不自动保证跨vocab的teacher mixture归一；IV.1 product仍仅teachers维归一，IV.2“valid convex combinations”是未指定G的额外约束，不能仅这些w规则推导。例p1=(1,0),p2=(0,1)，token1 w=(.9,.1)，token2 w=(.1,.9)，全部teacherwise归一/positive/bounded，却直接混合q=(.9,.9)不为概率。若另加vocab归一或要求token-independent weights，须明确改变定义；本文abstractG未披露这一步，不自行补公式。

更决定性的VI.2(ii)：A1–4为bounded/Lipschitz weights、student可实现teacher凸组合、logprob twice continuously differentiable；proof从stationary点直接跳到KL0。有限vocab二分类、固定输入/teacher q=(.75,.25)、uniform固定weights均符合；student pθ=(sigmoid(θ²),1−sigmoid(θ²))，可实现q于θ=±sqrt(log3)，logprob平滑。从θ0=0开始，任何样本CE导数因2θ因子为0，SGD保持0；p0=(.5,.5)与q不同，KL(q||p0)>0。满足Robbins–Monro step条件也不能将该stationary点改成global optimum。VII fixed-point还先假定operator contraction再从A1/A2/β推contraction，本文未给足够update定义；不将该式签成adaptive学习保证。

VI.2(iii)明确另有strong-convexity前提才声称O(1/t)，与(ii)在A1–4及stochastic approximation下跳到KL0是两个不同权限，不能说全文未给强凸条件。本次不采用有效性、KL0、通用收敛速率或安全token排序保证，不入Books。仅保留具名争议：需明确可归一G、足以排除非最优stationary点的student/loss几何（如适用凸/PL前提）及与实际update一致证明才重开。该处是数学反例，不是已复现实验；并未证明所有adaptive distillation无效。jan28_review实际必要定理与反例独立复核通过；日期/最终报告处置与DAY仍待，不自授整日完成。
