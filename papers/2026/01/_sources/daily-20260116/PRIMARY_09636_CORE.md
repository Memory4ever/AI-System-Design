# 2601.09636v1 primary necessary core

Source:https://arxiv.org/html/2601.09636v1
Fetched2026-10-03, normalized HTML text. Actual§5/6/B.2/B.3, not online replication.

5 
HIM-Agent
To support PersonalAlign, agent memory should generalize stable representations to exclude one-off moments while separating preferences and routines, and continuously evolve to stay aligned with user intents. As shown in Figure 
4
, we introduce HIM-Agent, a foundational and inspirational personal agent memory that enables GUI agents to rapidly leverage long-term records as context for personalization without interfering with original execution. We construct a streaming update memory and hierarchically organize memory prototypes into Preference Intent Memory and Routine Intent Memory through the execution-based and state-based filter to enable hierarchical intent alignment.
5.1 
Streaming Aggregation Module
Raw low-level GUI interaction records are inherently fragmented and noisy. Trivial operating based on these raw record leads to long-tail effects and memory drift, making it difficult to maintain stable personalized representations over time.
To address this challenge, we propose Streaming Aggregation Module that reframes personalization memory from a static log-based storage to a continually evolving representation. Rather than operating in individual records, we maintain Record Prototypes 
P
i
P_{i}
 as the fundamental memory units that synthesize similar records into a cohesive whole:
P
i
=
{
R
h
|
𝒮
c
​
o
​
n
​
s
​
i
​
s
​
t
​
(
R
h
,
P
i
)
>
θ
}
,
P_{i}=\{R_{h}|\mathcal{S}_{consist}(R_{h},P_{i})>\theta\},
(5)
where 
R
h
∈
H
R_{h}\in H
 represents incoming historical records, 
𝒮
c
​
o
​
n
​
s
​
i
​
s
​
t
\mathcal{S}_{consist}
 measures the consistency between records and prototypes. Based on MicroCluster in stream mining 
Aggarwal et al. (2003)
, our module incrementally aggregates records at a daily-granularity, enabling an evolving personal memory.
5.2 
Execution-based Preference Filter
GUI agent memory differs from chat-based memory in that each user interaction includes an execution trajectory rather than purely semantic content. In the Execution-based Filter, we compute 
𝒮
c
​
o
​
n
​
s
​
i
​
s
​
t
\mathcal{S}_{consist}
 by jointly modeling semantic intent similarity and action trajectory consistency for more comprehensive aggregation for GUI interaction.
Figure 4: 
Overview of HIM-Agent. The Streaming Aggregation Module updates user records daily, and the aggregated prototypes are hierarchically organized to support personalized preference and routine intent.
For semantic similarity 
𝒮
s
​
i
​
m
\mathcal{S}_{sim}
, we combine dense embedding cosine similarity 
𝒮
c
​
o
​
s
\mathcal{S}_{cos}
 with sparse Jaccard 
𝒮
J
​
a
​
c
\mathcal{S}_{Jac}
, which computes the overlap ratio of shared words between instructions, to robustly measure semantic similarity. Since GUI instructions are often short and entity-heavy (e.g., app names, items), this may lead to distortions in 
𝒮
c
​
o
​
s
\mathcal{S}_{cos}
.
For action consistency 
𝒮
a
​
c
​
t
​
i
​
o
​
n
\mathcal{S}_{action}
, we employ Dynamic Time Warping (DTW) to measure the similarity between trajectories that have temporal structure. DTW computes an optimal alignment path 
π
\pi
 by minimizing the cumulative distance between aligned action steps.
The execution-based preference filter can be formulated as:
{
𝒮
s
​
i
​
m
​
(
I
h
,
I
c
i
)
=
𝒮
c
​
o
​
s
+
𝒮
J
​
a
​
c
𝒮
a
​
c
​
t
​
i
​
o
​
n
​
(
A
h
,
A
c
i
)
=
min
⁡
∑
(
i
,
j
)
∈
π
π
⁡
d
⁡
(
a
i
,
b
j
)
𝒮
c
​
o
​
n
​
s
​
i
​
s
​
t
​
(
R
h
,
P
i
)
=
𝒮
s
​
i
​
m
+
𝒮
a
​
c
​
t
​
i
​
o
​
n
,
\begin{cases}\mathcal{S}_{sim}(I_{h},I_{c_{i}})=\mathcal{S}_{cos}+\mathcal{S}_{Jac}\\
\mathcal{S}_{action}(A_{h},A_{c_{i}})=\min\limits_{\pi}\sum_{(i,j)\in\pi}d(a_{i},b_{j})\\
\mathcal{S}_{consist}(R_{h},P_{i})=\mathcal{S}_{sim}+\mathcal{S}_{action},\end{cases}
(6)
where 
I
h
,
A
h
I_{h},A_{h}
 denote the intent and action of 
R
h
R_{h}
, while 
I
c
i
,
A
c
i
I_{c_{i}},A_{c_{i}}
 represent center intent and action of prototype 
P
i
P_{i}
, which are updated daily by selecting the instructions and actions with the minimum average distance to all other records assigned to 
P
i
P_{i}
. The pairwise distance 
d
⁡
(
a
i
,
b
j
)
d(a_{i},b_{j})
 is computed based on the GUI action success rate (SR), which evaluates whether two actions are the same action.
After filtering, each Record Prototype 
P
i
P_{i}
 provides a stable representation and is stored in Preference Intent Memory. When HIM-Agent needs to infer user preferences, the corresponding prototype’s center intent 
I
c
I_{c}
 and action 
A
c
A_{c}
 will be provided.
Table 2: 
Impact of instruction-induced degradation on GUI agents. Various agents are evaluated under both complete and vague instructions, with results under vague instructions shown in the gray line.
Model
Type
SSR
CER
Closed-sourced GUI Agents
GPT-5.1
51.2
26.4
52.3
49.3
↓
\downarrow
3.7%
20.3
↓
\downarrow
23.1%
22.9
↓
\downarrow
56.2%
GLM-4.5v
51.0
27.4
54.5
50.5
↓
\downarrow
0.9%
19.4
↓
\downarrow
25.5%
22.6
↓
\downarrow
58.5%
QwenVL-Max
51.9
29.8
53.3
51.6
↓
\downarrow
0.5%
24.8
↓
\downarrow
16.9%
27.3
↓
\downarrow
48.8%
Open-sourced GUI Agents
UI-TARS-1.5
49.4
23.5
38.6
46.8
↓
\downarrow
2.6%
19.9
↓
\downarrow
15.3%
14.9
↓
\downarrow
23.7%
GUI-Owl
54.2
24.9
50.4
53.1
↓
\downarrow
2.0%
17.9
↓
\downarrow
28.1%
23.7
↓
\downarrow
53.0%
Qwen3-VL
52.7
26.7
52.9
46.6
↓
\downarrow
12.0%
20.6
↓
\downarrow
22.8%
26.6
↓
\downarrow
49.7%
Table 3: 
GUI agent performance in proactive service. Lower False-Alarm rates indicate better proactive accuracy. Values marked in 
red
 denote cases of insufficient capability by the agent.
Model
Intent Alignment
Identification Alignment
Semantic
Judgment
Precision
Recall
False-Alarm 
↓
\downarrow
F1-score
Closed-sourced GUI Agents
GPT-5.1
49.4%
32.0%
73.1%
78.6%
62.0%
75.8%
GLM-4.5V
52.8%
33.9%
68.9%
96.7%
94.0%
80.4%
QwenVL-Max
52.2%
34.8%
67.4%
97.2%
98.0%
67.4%
Open-sourced GUI Agents
UI-TARS-1.5
42.6%
19.0%
68.7%
99.1%
97.0%
81.1%
GUI-Owl
32.6%
12.2%
79.9%
57.2%
31.0%
66.7%
Qwen3-VL
45.0%
23.6%
69.0%
97.2%
94.0%
80.7%
5.3 
State-based Routine Filter
Upon the formation of a stable prototype 
P
i
P_{i}
, we introduce State-based Routine Filter to further separate passive preferences from proactive intents. This module jointly considers the frequency of occurrence, the execution coherence, and the consistency of user states of each 
P
i
P_{i}
 to determine whether proactive suggestions should be activated.
To achieve this, we define a proactive confidence 
Φ
⁡
(
P
i
)
\Phi(P_{i})
, which is calculated by: the state stability 
H
s
​
t
​
a
​
t
​
e
H_{state}
, which captures the normalized of temporal and scenario entropies within records of prototype; the record length in prototype 
L
r
​
e
​
c
​
o
​
r
​
d
L_{record}
, reflecting how frequently the pattern recurs; and the aggregation weight 
R
c
​
o
​
n
​
s
​
i
​
s
​
t
R_{consist}
, obtained by averaging 
𝒮
c
​
o
​
n
​
s
​
i
​
s
​
t
\mathcal{S}_{consist}
. Confidence is jointly inferred based on state consistency, execution consistency, and frequency. This is formulated as:
Φ
⁡
(
P
i
)
=
H
s
​
t
​
a
​
t
​
e
+
L
r
​
e
​
c
​
o
​
r
​
d
+
R
c
​
o
​
n
​
s
​
i
​
s
​
t
,
\Phi(P_{i})=H_{state}+L_{record}+R_{consist},
(7)
If 
Φ
⁡
(
P
i
)
\Phi(P_{i})
 exceeds the proactive confidence boundary, the corresponding prototype is stored in Routine Intent Memory.
When the HIM-Agent needs to determine whether proactive suggestions are required, prototype’s center intent 
I
c
I_{c}
 and the most frequent state 
T
c
,
S
c
T_{c},S_{c}
 will be provided.


6 
Experiment
6.1 
Experimental Setup
Table 4: 
Execution performance across various methods under vague instructions. 
†
\dagger
 denotes the baseline.
Base
†
\dagger
Model
Retrieve-based
Generalized-based
Recent
Retrieve
LLM-UM
HIM-Agent
Type
46.6
49.4
51.0
51.2
52.0
SSR
20.6
21.1
22.4
22.3
24.0
CER
26.6
33.2
35.4
35.2
42.3
Metrics.
We evaluate GUI execution using 
Type Accuracy
 (Type) and 
Step-wise Success Rate
 (SSR) under an offline evaluation protocol, where treated user actions as the golden trajectory. Moreover, we introduce a new 
Cumulative Error Rate
 (CER) to measure failures on critical steps caused by vague instructions 
ElMallah et al. (2025)
, where missing user-specific information leads to mismatches with the user’s true intent. To approximate the impact of errors on critical steps, we assign a decaying weight to each step along the trajectory, such that earlier errors contribute more heavily to the overall score. CER thus serves as an intermediate metric that bridges offline evaluation with online performance.
On the other hand, to evaluate the agent’s proactive recommendation capability, we consider 
Intent Alignment
 and 
Identification Alignment
Lu et al. (2025b)
. We measure the 
Semantic
 similarity between generated suggestions and user’s original intent using embedding cosine similarity and edit distance. We also use an LLM-as-
Judgment
 to evaluate intent alignment, where DeepSeek-V3 is employed to mitigate self-bias.
Identification Alignment evaluates proactive appropriateness, we carefully collect 100 negative user states that do not require proactive assistance, and compute 
Precision
, 
Recall
, 
False-Alarm
, and 
F1-score
.
Please also refer to Appendix 
B
 for more details about baselines and implementation details.
Table 5: 
Proactive performance comparison. FA means False-Alarm rate. 
†
\dagger
 denotes the baseline.
Retrieve-based
Generalized-based
Recent
†
\dagger
Retrieve
LLM-UM
HIM-Agent
Semantic
49.4%
49.8%
49.1%
53.5%
Judgement
32.0%
32.2%
31.6%
36.3%
Precision
70.8%
74.2%
75.6%
78.1%
Recall
78.3%
82.0%
82.3%
81.4%
FA 
↓
\downarrow
62.0%
64.0%
57.0%
49.0%
F1-score
75.8%
77.9%
78.8%
79.7%
Token
4930
3089
1161(+6518)
1605
Table 6: 
Ablation study of components in Execution-based Preference Filter Module. Dense and Sparse denote embedding and Jaccard similarity.
Components
Performance
Dense
Sparse
Action
Type
SSR
CER
×
\times
×
\times
×
\times
49.4
21.1
33.2
×
\times
✓
\checkmark
✓
\checkmark
50.8
22.5
35.9
✓
\checkmark
×
\times
✓
\checkmark
51.1
22.9
36.3
✓
\checkmark
✓
\checkmark
×
\times
51.4
23.3
37.3
✓
\checkmark
✓
\checkmark
✓
\checkmark
52.0
24.0
42.3
Figure 5: 
Ablation study of components for proactive performance. Lower of False-Alarm means better align.
Figure 6: 
Case study of HIM-Agent. 
Left
: HIM-Agent resolves vague instructions by aligning intent with historical interaction records. 
Right
: HIM-Agent proactively suggests based on historical record and user state.
6.2 
Experimental Analysis
Vague Instruction Impact on GUI Execution.
Table 
2
 shows the impact of vague instructions on several outstanding open- and closed-sourced GUI agents. Currently, GUI agents still need to improve their performance across daily instructions and apps since most SSR is around 25-30. Notably, while ambiguity leads to only a 3% drop in type accuracy, SSR and CER decrease by approximately 20% and 45%. We observe that vague instructions act as 
coarse-grained sub-goals
: although agents can often identify the high-level intended operation, execution fails at a fine-grained level due to the absence of critical personalized preference information.
For example, lacking explicit requirements, the agent may open incorrect apps, causing execution to deviate significantly from user intent.
Challenge in Balancing Proactive Identification.
Table 
3
 evaluates the proactive performance of GUI agents based on recent historical records and current user state. Notably, most models struggle to determine when proactive behavior is truly necessary.
Aside from GPT-5.1, current GUI agents generally 
fail to provide effective proactive suggestions
, as they struggle to balance false alarms and recall, often defaulting to overly proactive. These failure cases are highlighted in red and underlined. This reveals a promising research direction: to effectively leverage user records for personalization, agents must develop superior long-term context analysis capabilities.
HIM-Agent significantly enhances agent’s ability to align implicit intent.
Since PersonalAlign is a novel paradigm without established methods, we select and compare it against two representative categories of basic approaches: (i) top-down retrieval-based methods, which incorporate recent or relevant historical records as user context for the agent, and (ii) bottom-up inductive methods, which leverage LLMs to summarize user profiles (LLM-UM) 
Wang et al. (2025b)
, alongside our HIM-Agent.
As shown in Table 
4
, we build HIM-Agent based on outstanding open-sourced Qwen3-VL. HIM-Agent achieves the best performance in alleviating the impact of vague instructions, obtaining a CER score of 42.3.
Furthermore, to objectively evaluate different methods’ proactive capability, we conduct experiments on GPT-5.1, which 
only
 shows basic balanced proactive ability. As shown in Table 
5
, our framework achieves superior performance in both Semantic Alignment and Identification Alignment. HIM-Agent helps the agent achieve a better balance between recall 81.4% and false-alarm 49% and keep the highest Intent Alignment score 53.3% and 36.3%. While LLM-UM introduces extra 6518 tokens consumed when generating user profiles, HIM-Agent remains highly efficient during generalized user modeling.
Ablation Study.
 Table 
6
 presents the ablation study of components within Execution-based Preference Filter. The first gray line denotes the setting without this filter, under which the streaming aggregation module also can’t work, and memory degenerates to individual records without prototypes. The results indicate that all three components contribute to performance gains, and the full module achieves a 9.1% improvement in CER.
As shown in Figure 
5
, we further demonstrate the importance of state-related components in enabling proactive, where both time and scenario play crucial roles. Notably, removing the filter while retaining all prototypes will cause an increase in false alarms to nearly 70%, which is even higher than the baseline with recent individual records, highlighting the critical role of the state filter for proactive.
6.3 
Case Study
As shown in Figure 
6
, we present case studies comparing HIM-Agent and a reactive agent. In daily usage, user instructions often omit preferences, leading reactive GUI agents to misalign with the user’s true intent. HIM-Agent can infer missing preferences from historical records to correct action execution. By jointly reasoning over records and the current state, HIM-Agent can also proactively assist users, whereas reactive agents remain inactive without explicit instructions.


B.2 
Implementation details
All GUI agent execution experiments were conducted on an NVIDIA A100 (40GB) GPU. And we select GPT-5.1 for LLM-UM. During the filtering process, we set 
k
=
10
k=10
 for the top-
k
k
 selection. When computing 
Q
s
​
c
​
o
​
r
​
e
Q_{score}
 we use a weighted sum of [1,0.1,0.1] and then normalization. Notably, different weight combinations can yield approximately normal-shaped distributions; we select this configuration to produce clearer decision boundaries and we also slightly expanding the filtering range for moment and preference intent to 0.6 in this setting. Additionally, both 
θ
\theta
 in Streaming Aggregation and the proactive boundary threshold in the State-based Routine Filter were both set to 0.6. For CER, we apply an exponential decay to the length of each trajectory and then perform normalized weighting of SSR.
B.3 
Online Evaluation
In this paper, we mainly adopt an offline GUI evaluation setting.
On the other hand, since a user’s intent can often be achieved through multiple valid trajectories, online evaluation is also suitable. However, unlike simulator-based benchmarks such as AndroidWorld 
Rawles et al. ()
, evaluating on AndroidIntent requires connecting to real physical devices via Android Debug Bridge (ADB), as many daily apps cannot run on emulators due to privacy and security restrictions.
Moreover, the evaluation results cannot be automatically verified by Android APIs to determine whether the user intent is successfully completed. Instead, each execution must be manually inspected to assess the agent’s behavior. In addition, real-device evaluation is affected by various factors such as app versions, mobile models, and runtime environments.
Since online evaluation is still not sufficiently stable or scalable under these constraints, we primarily adopt offline evaluation to ensure a more objective and reproducible assessment.

