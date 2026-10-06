# 2601.08839v1 — 中心稳定性保证争议

精确源：https://arxiv.org/html/2601.08839v1，实际读§8、§9、§11.3、AppendixA.1–A.2；非遍历全文附件。

Banach完整metricspace与审计operator contraction被假设，但没有定义可测knowledge representation/metric、M_S/M_A Lipschitz bound或M_T严格收缩证明。TS threshold下的penalty/projection不自动是strictcontraction；47trial高TS人类rubric不能验证任意x/y收缩。§9.1称三种freemium服务，§9.2又singleChatGPTPlus分离sessions，实验对象未一致；singlehumanrater、unfrozenOct2025browser snapshots不能归因多model/audit。增量理论条件有实际对接但中心保证尚无证明，拟2+1+2=5、争议暂缓不Books。有限human-bridgepilot只供上下文，不用安全/收敛/可复现性保证；重开需明确operator/metric收缩证明或matched多role/audit试验及冻结对象。root实际核§8/A.1/A.2与human/pinnedmodel限制：核心收缩采用依赖不成立，5Disputed隔离通过；§9对象冲突仅补充，不将普通未读作受阻。

## 原始必要核心


8 
Mathematical Model of Recursive Knowledge Synthesis
This section formalizes the concept of 
Recursive Knowledge Synthesis (RKS)
, treating the collective knowledge state (
Knowledge
t
\text{Knowledge}_{t}
) as a dynamic vector continuously refined by the 
Cross-Validation Cycle
.
8.1 
Formal Definition of Knowledge Synthesis
RKS is defined as the dynamic process where the output of any module recursively serves as a filtered input for the others, leading to a synthesized knowledge state that is a non-linear composite. This iterative mapping is described mathematically as:
Knowledge
t
+
1
=
F
⁡
(
Knowledge
t
,
M
S
,
M
A
,
M
T
)
\text{Knowledge}_{t+1}=F(\text{Knowledge}_{t},M_{S},M_{A},M_{T})
where 
F
F
 is a non-linear transformation function characterizing the collective effect of the 
Validation Operator (
V
O
​
p
V_{Op}
)
: 
V
O
​
p
=
M
T
∘
M
A
∘
M
S
V_{Op}=M_{T}\circ M_{A}\circ M_{S}
.
8.2 
Convergence and Stability Criteria via Contraction Mapping
For the system to yield computationally sound results, the RKS process must demonstrate a bounded, non-divergent trajectory. This requires the system to satisfy the 
convergence criterion
 derived from the 
Banach Fixed-Point Theorem
 (detailed in 
Appendix A
). The key requirement is that the composite operator 
V
O
​
p
V_{Op}
 must be a 
contraction mapping
:
‖
V
O
​
p
​
(
x
)
−
V
O
​
p
​
(
y
)
‖
L
​
2
≤
γ
​
‖
x
−
y
‖
L
​
2
,
where 
​
0
≤
γ
<
1
\|V_{Op}(x)-V_{Op}(y)\|_{L2}\leq\gamma\|x-y\|_{L2},\text{where }0\leq\gamma<1
The theoretical stability of the entire heterogeneous system relies critically on the properties of the 
Transparency Audit Module (
M
T
M_{T}
)
. While the Semantic Module (
M
S
M_{S}
) and Analytical Module (
M
A
M_{A}
) perform non-expansive or mildly expansive mappings, the 
Audit Module (
M
T
M_{T}
) is rigorously defined as the component that introduces the contraction property
 into the system. This is achieved by its function as a penalization and projection mechanism that forces the knowledge state vector toward the constraint space defined by the 
Transparency Score (TS)
 threshold. The empirical observation of high TS compliance directly validates this theoretical dependency.
Figure 7: 
Visualization of the contraction mapping principle in knowledge state space 
𝒦
\mathcal{K}
. The spiral trajectory demonstrates iterative convergence of the validation operator 
V
O
​
p
V_{Op}
 toward the unique fixed point (marked by star), satisfying the Banach Fixed-Point Theorem with contraction constant 
γ
<
1
\gamma<1
.
hitecture.
While automated multi-agent systems maximize efficiency, they introduce safety risks: agents may develop implicit coordination strategies, propagate errors across the network, or exhibit unpredictable emergent behaviors. Our human-bridged approach sacrifices scalability for 
controllability and auditability
. Every state transition is explicitly reviewed, logged, and validated by the Supervisor, ensuring that the system cannot be repurposed for uncontrolled agent orchestration tasks.
Session-Level Decomposition vs Model Diversity.
Traditional multi-agent frameworks achieve modularity through diverse model instances. Our Session-Level Role Decomposition (SLRD) achieves functional modularity 
within a single LLM environment
 by partitioning roles across isolated sessions. This approach enables drift detection (Section 
11.4
) while maintaining full observability—a property difficult to achieve in distributed multi-model systems.
In summary, this work demonstrates a 
Safe Multi-LLM Orchestration Framework
 rather than a Fully Autonomous Multi-Agent System. The trade-off is intentional: we prioritize reproducibility, transparency, and human oversight over automation and scalability.
11.3 
Limitations and Future Work
Limitations:
1.
Reproducibility Constraints.
Since freemium LLMs continuously update, exact bit-level reproducibility cannot be guaranteed. The reliance on continuously updated, public-access deployments means that the exact underlying model variants (e.g., specific sub-versions within a model family) cannot be bit-level pinned. This limitation reflects the practical reality of how most users experience large language models in 2025, but it complicates strict replication. To partially mitigate this, we provide full descriptions of the roles, prompts, and evaluation rubrics, and we explicitly characterize the deployment regime in Table 
2
 and Table 
1
. We therefore position this work as a snapshot-based feasibility study reflecting the behavior of models during October 2025, not as a controlled benchmark with frozen model binaries.
2.
Evaluation Subjectivity.
All stability metrics rely on semi-manual scoring by a single human Supervisor using a standardized rubric. This introduces unavoidable subjectivity. Future work should incorporate multiple evaluators and report inter-rater reliability using metrics such as Cohen’s 
κ
\kappa
 or Fleiss’ 
κ
\kappa
.
3.
Scale of Experiments.
While 47 trials provide meaningful preliminary evidence, they do not cover the full range of failure modes. This research should be positioned as a pilot feasibility study, requiring larger-scale follow-up investigations.
4.
Session-Based Architecture vs Full Autonomy.
This study intentionally avoids autonomous agent-to-agent messaging to prioritize safety and control. A structural limitation arises from the reliance on session-level role decomposition rather than true multi-model autonomy. Although this design improves traceability, it also requires explicit human orchestration, which limits scalability. A fully automated multi-agent architecture is a next-step research direction.
This study should be regarded as a pilot-scale feasibility investigation. Because the system relies on continuously updated public-access LLM deployments without version pinning, bit-level reproducibility cannot be guaranteed. Additionally, all evaluation metrics were scored by a single annotator. Future work will introduce multiple human raters and report inter-rater agreement using Cohen’s 
κ
\kappa
 or Fleiss’ 
κ
\kappa
.
In addition, the deliberate choice to keep all cross-system coordination human-mediated is intended not only to match realistic user behavior but also to act as a safety guardrail: reproductions of this framework should preserve strong human oversight rather than fully automating the bridge layer.
A small set of session-level workflow prompts was employed as a practical safeguard against local drift, but these were not included in any evaluated metric and had no influence on the reported stability results.
Future Work:
1.
Future directions include developing automated linguistic quality metrics (e.g., a computable version of the proposed Expressive Coherence Index) and formalizing adaptive control indices to replace the conceptua
A.1 
Knowledge State as a Complete Metric Space
The synthesized knowledge at time 
t
t
, 
Knowledge
t
\text{Knowledge}_{t}
, is represented as a high-dimensional vector in the knowledge space 
𝒦
\mathcal{K}
. We assume 
𝒦
\mathcal{K}
 is a Banach space, and thus a 
complete metric space
(
𝒦
,
d
)
(\mathcal{K},d)
, where 
d
d
 is a suitable metric (e.g., 
L
​
2
L2
 distance) quantifying the difference between two knowledge states.
A.2 
The Validation Operator and Contraction Mapping
The state transition across one full 
Cross-Validation Cycle
 is modeled by the 
Validation Operator (
V
O
​
p
V_{Op}
)
:
V
O
​
p
=
M
T
∘
M
A
∘
M
S
V_{Op}=M_{T}\circ M_{A}\circ M_{S}
where 
M
S
M_{S}
, 
M
A
M_{A}
, and 
M
T
M_{T}
 are the functional operators for the respective modules. The 
Banach Fixed-Point Theorem
 states that if 
V
O
​
p
V_{Op}
 is a 
contraction mapping
 (i.e., it strictly reduces the distance between any two points in the space), then there exists a unique fixed point 
x
∗
=
V
O
​
p
​
(
x
∗
)
x^{*}=V_{Op}(x^{*})
 toward which the system must converge:
‖
V
O
​
p
​
(
x
)
−
V
O
​
p
​
(
y
)
‖
L
​
2
≤
γ
​
‖
x
−
y
‖
L
​
2
,
where 
​
0
≤
γ
<
1
\|V_{Op}(x)-V_{Op}(y)\|_{L2}\leq\gamma\|x-y\|_{L2},\text{where }0\leq\gamma<1
The theoretical stability of the entire heterogeneous system relies critically on the properties of the 
Transparency Audit Module (
M
T
M_{T}
)
. While the Semantic Module (
M
S
M_{S}
) and Analytical Module (
M
A
M_{A}
) perform non-expansive or mildly expansive mappings, the 
Audit Module (
M
T
M_{T}
) is rigorously defined as the component that introduces the contraction property
 into the system. This is achieved by its function as a penalization and projection mechanism that forces the knowledge state vector toward the constraint space defined by the 
Transparency Score (TS)
 threshold. The empirical observation of high TS compliance directly validates this theoretical dependency.
Appendix B 
External Supervisor Control Protocol (Prompt Set)
This appendix lists the standardized, high-level control prompts utilized by the 
External Supervisor
 to manage the experimental flow and systematic regulation of the multi-agent cluster. These prompts represent the human-machine interface for the experimental protocol.
B.1 
Context Provisioning Prompt (Initial State)
Purpose:
 To establish the initial computational context, define task boundaries, and establish ethical constraints (TS criteria).
Prompt:
>
>
 As a multidisciplinary research agent cluster, please generate the initial structural proposal for a paper detailing a novel three-agent LLM cross-validation system. Your response must include core objectives, the methodological approach, the architecture of the transparency module, and a formal definition of systematic stability. (Includes initial ethical/scope constraints).
B.2 
Analytical Consistency Prompt (Internal Iteration)
Purpo
