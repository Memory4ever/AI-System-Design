# 2601.09258v1 — minimum predictor, evaluation and diagnosis boundary

Exact primary: https://arxiv.org/html/2601.09258v1 ; selected necessary original body excerpts actually read, not full-attachment review.

4.2.2 
Predictive Modeling and Feature Selection
To achieve high-precision anomaly detection, we construct a baseline model with workload as input and latency as output: 
L
​
a
​
t
​
e
​
n
​
c
​
y
=
f
⁡
(
W
​
o
​
r
​
k
​
l
​
o
​
a
​
d
)
Latency=f(Workload)
. Taking SGLang framework as an example, an iteration consists of three parts, 
get_next_batch_to_run
, 
run_batch
 and 
process_batch_result
. Scheduling-related overhead (
get_next_batch_to_run
) is intentionally excluded from the modeling scope for three reasons: (1) Data Validity: monitoring scheduling during idle periods introduces noise; (2) Focus: performance anomalies rarely manifest solely as scheduling delays; and (3) Decoupling: scheduling latency depends on global system state rather than the current batch’s workload.
The Decode stage theoretically exhibits linear complexity 
O
⁡
(
B
⋅
K
)
+
O
⁡
(
B
)
O(B\cdot K)+O(B)
, where 
B
=
Batch Size
B=\text{Batch Size}
 and 
K
=
KVCache
=
Input Length
+
Current Output Length
K=\text{KVCache}=\text{Input Length}+\text{Current Output Length}
.
Based on the cycle segmentation results, we can extract the runtime of a single batch. By collecting data during normal operation combined with load information, we can model the theoretical single-batch runtime. However, a critical challenge exists in actual deployments: in production environments, inference frameworks universally enable Overlap optimization, introducing non-linear logic of 
max
⁡
(
T
G
​
P
​
U
​
_
​
c
​
o
​
m
​
p
​
u
​
t
​
e
,
T
c
​
o
​
m
​
m
​
_
​
a
​
n
​
d
​
_
​
p
​
r
​
o
​
c
​
e
​
s
​
s
)
\max(T_{GPU\_compute},T_{comm\_and\_process})
. Experiments show that this inflection point behavior causes simple linear physical models to fail. Therefore, we employ Gradient Boosting Decision Trees (GBDT) as the baseline predictor. GBDT can fit the non-linear inflection points introduced by Overlap extremely well.
To capture memory bandwidth bottlenecks in the Decode stage, we construct physical features based on hardware principles. The core overhead of Decode operators lies in reading the Key-Value matrices of all historical tokens. We define 
L
r
​
e
​
a
​
l
=
L
i
​
n
+
L
o
​
u
​
t
L_{real}=L_{in}+L_{out}
 and construct the feature 
W
k
​
v
=
B
×
L
r
​
e
​
a
​
l
W_{kv}=B\times L_{real}
. This feature directly maps to GPU memory bandwidth pressure. We explicitly exclude certain statistical features during feature selection. Although introducing these features might improve performance data by capturing implicit relationships, they would undermine model interpretability.
(a)
Unseen Workloads
(b)
Production Noise
(c)
Cross-Stack
Figure 5
: 
Model Convergence Analysis.
 The model achieves rapid stabilization across three distinct scenarios: (a) unseen workloads in SGLang; (b) raw production noise without denoising; and (c) a cross-stack environment (vLLM, DeepSeek-70B), demonstrating robust generalization capabilities.
4.2.3 
Alert Triggering and Comprehensive Collection
We employ control chart theory to monitor prediction residuals. We define the Positive Prediction Error (PPE) as the monitoring metric 
E
t
=
max
⁡
(
0
,
Y
t
−
Y
^
t
Y
t
+
ϵ
)
E_{t}=\max(0,\frac{Y_{t}-\hat{Y}_{t}}{Y_{t}+\epsilon})
, focusing only on cases where actual time significantly exceeds predicted time (i.e., performance degradation). To smooth transient noise, we introduce a sliding window (Window Size 
W
W
) to calculate the moving average error 
E
¯
t
\bar{E}_{t}
. The system dynamically calculates the Upper Control Limit (UCL) based on the residual distribution of the training set:
U
​
C
​
L
d
​
y
​
n
​
a
​
m
​
i
​
c
=
min
⁡
(
μ
t
​
r
​
a
​
i
​
n
+
k
⋅
σ
t
​
r
​
a
​
i
​
n
,
θ
m
​
a
​
x
)
UCL_{dynamic}=\min(\mu_{train}+k\cdot\sigma_{train},\theta_{max})
(1)
where 
μ
\mu
 and 
σ
\sigma
 are the mean and standard deviation of the training set errors, 
k
=
3
k=3
 is the sigma coefficient, and 
θ
m
​
a
​
x
\theta_{max}
 is the empirically set maximum tolerance. When 
E
¯
t
>
U
​
C
​
L
d
​
y
​
n
​
a
​
m
​
i
​
c
\bar{E}_{t}>UCL_{dynamic}
, the system triggers an anomaly alert and initiates comprehensive collection according to user configuration.
5 
Evaluation
5.1 
Experimental Setup
We evaluated LatencyPrism on NVIDIA A100 GPUs using SGLang v0.5.4 and the Qwen3-32B model. The workload distribution spanned a wide range to mimic production diversity: batch sizes of 1–512, input lengths of 1–2048, and output lengths of 1–512.
5.2 
Monitoring Subsystem Assessment
Overhead.
 LatencyPrism incurs negligible overhead, degrading throughput by less than 0.5% and latency by less than 0.1%, making it suitable for production deployment.
Model Adaptability and Robustness.
 We conducted three distinct evaluations to assess the model’s performance:
•
Generalization to Unseen Workloads.
 To verify the model’s ability to migrate between configurations, we split the dataset by unique workload types (i.e., the test set contained workloads never seen during training). As shown in Figure 
5(a)
, the results confirm that the model learns intrinsic performance characteristics, enabling rapid convergence on new configurations with minimal samples.
•
Robustness to Production Noise.
 To simulate a real-world production environment, we used raw, noisy data with a completely random split, without segregating workloads. As shown in Figure 
5(b)
, even without denoising, the model stabilizes within approximately 1,000 samples (equivalent to minutes of traffic), achieving a prediction error of 
<
10
%
<10\%
 for over 90% of samples. This demonstrates the model’s robustness against production noise.
•
Cross-Stack Generalizability.
 To confirm that our modeling strategy is not overfitting to specific framework implementations, we conducted an additional evaluation on vLLM v0.10.0 serving DeepSeek-R1-Distill-Llama-70B with Tensor Parallelism(TP) size 4. As shown in Figure 
5(c)
, LatencyPrism successfully adapts to the distinct scheduling logic of vLLM and the computational patterns of the 70B model. The predictor converges rapidly, validating that our physically-informed feature engineering captures universal hardware bottlenecks rather than framework-specific artifacts.
Accuracy & Interpretability Trade-off.
 We evaluated the system using real production data. As shown in Table 
3
, we compared the Full Feature strategy against our Physically-Informed Feature Engineering strategy using both Polynomial and GBDT models.
Table 3
: 
Performance and Interpretability Analysis of Feature Engineering Strategies.
Strategy
Model
R
2
R^{2}
MAPE
Dominant Features (Top-weighted)
Analysis & Interpretation
Full Feature
GBDT
0.989
1.53%
post_MaxInLen
, 
post_FwdMode
Pipeline Coupling.
 Overfits to SGLang’s specific overlap logic rather than execution physics.
Full Feature
Polynomial
0.865
5.98%
BatchSize
×
\times
FwdMode
 (Coeff 
≈
−
1.3
×
10
6
\approx-1.3\times 10^{6}
)
Multicollinearity.
 Massive, opposing coefficients indicate mathematical instability.
Feature Eng.
GBDT (Ours)
0.963
6.06%
Workload_KV
 (
B
⋅
L
B\cdot L
), 
Batch
Physical Causality.
 Correctly identifies memory bandwidth bottleneck (
O
⁡
(
B
⋅
L
)
O(B\cdot L)
).
Feature Eng.
Polynomial
0.056
35.3%
BatchSize
Model Mismatch.
 Fails to capture the non-linear inflection point of Overlap.
Although the Full Feature + GBDT combination yields the highest raw accuracy (
R
2
=
0.989
R^{2}=0.989
), it relies on software implementation details rather than hardware principles. As shown in the "Dominant Features" column, its top predictors are 
post_
 features (e.g., 
post_MaxInLen
). In SGLang’s architecture, these features correspond to the 
process_batch_result
 stage, which is overlapped with the current 
run_batch
 computation. The model’s reliance on these features indicates it is overfitting to the spurious correlations within the scheduling pipeline rather than the fundamental hardware bottlenecks.
In contrast, our Feature Engineering + GBDT strategy achieves competitive accuracy (
R
2
=
0.963
R^{2}=0.963
) while maintaining strict physical causality. It correctly identifies 
Workload_KV
 as the primary determinant, aligning with the theoretical memory bandwidth bottleneck. This confirms that our model learns universal hardware constraints robust to software changes.
Anomaly Detection Strategy.
 Lacking external tools with comparable granularity, we evaluated three detection strategies by manually injecting faults: Fixed-Point (Fixed threshold 15% + Point detection), Fixed-Window (Fixed 15% + Window smoothing 
W
=
10
W=10
), and Dynamic-Window (Dynamic 
3
​
σ
3\sigma
 + Window smoothing 
W
=
10
W=10
).
As shown in Table 
4
, the Fixed-Window baseline achieved a perfect FPR (0.00%), indicating that the injected faults were statistically distinct enough to trigger a conservative fixed threshold.
However, relying on a "magic number" (e.g., 15%) is impractical for diverse production workloads. We adopt the Dynamic-Window strategy as the system default. Although it incurs a negligible FPR trade-off (0.59%), it eliminates manual threshold tuning and maintains a higher recall (0.999 vs 0.993), ensuring robust detection across shifting noise baselines.
Table 4: 
Performance Evaluation of Anomaly Detection Strategies on Production Datasets.
Strategy
Precision
Recall
F1
FPR
Lag
Dynamic-Point
0.960
0.996
0.978
0.84%
0.0
Dynamic-Window
0.971
0.999
0.985
0.59%
0.2
Fixed-Window
1.000
0.993
0.997
0.00%
1.4
We visualize the detection performance across 20 independent simulation trials in Figure 
6
. As observed, there is a sharp, uniform transition from white (normal state) to deep red (high error) immediately following the anomaly injection point (dashed line). This visual evidence confirms that our strategy achieves low-latency detection and high consistency regardless of the specific random noise patterns in each trial, validating its suitability for real-time monitoring.
Figure 6
: 
Heatmap visualization of anomaly detection consistency across 20 independent trials using Dynamic-Window strategy. The dashed line marks the fault injection point. Red areas indicate detected.
6 
Root Cause Localization
To a

---

6.1 
Metrics and Correlation
Adapted from PerfTracker 
[
14
]
, we utilize two primary metrics: 
β
\beta
 (Time Proportion)
, the percentage of cycle time consumed by an operation, and 
μ
\mu
 (Average Utilization)
, the weighted average of associated hardware resources (e.g., GPU SM, CPU) during execution. We handle sparse counter samples via linear interpolation.
Cycle-based Paradigm.
 We adopt a cycle-based analysis rather than global averaging to capture transient dynamics inherent in LLM iterations. On the one hand, the diversity of captured events precludes a static priority order. On the other hand, we leverage the Python timeline to define strict cycle boundaries, where any function with high 
β
\beta
 should be treated as a potential bottleneck. Therefore, unlike PerfTracker, we omit critical path analysis for 
β
\beta
.
6.2 
Suspicion Score Algorithm
Our algorithm assumes behavioral symmetry across distributed processes (e.g., within a Tensor Parallelism group). It identifies anomalies where 
β
\beta
 exhibits statistically significant shifts. We utilize Z-Score (
Z
=
(
x
¯
a
​
b
​
n
−
x
¯
n
​
o
​
r
​
m
)
/
σ
n
​
o
​
r
​
m
Z=(\bar{x}_{abn}-\bar{x}_{norm})/\sigma_{norm}
) to measure deviation. For resource utilization 
μ
\mu
, which follows a non-negative skewed distribution, we apply a log transformation (
log1p
) for robustness. The final suspicion score is defined as:
Score
=
|
Δ
​
β
|
×
(
|
Z
β
|
+
|
Z
log
⁡
μ
|
)
\text{Score}=|\Delta\beta|\times(|Z_{\beta}|+|Z_{\log\mu}|)
.
6.3 
Validation
We validated the method on SGLang and vLLM frameworks across CPU, GPU, and interconnect faults. As shown in Table 
5
, the system successfully localizes root causes. All Top-1 anomaly cases exhibited P-values near 0.000, confirming that the collected traces provide statistically distinguishable signals for fault reasoning. Utilizing the resolved topology from § 
4.1.3
, we can easily identify the

---

ity, semantically aligned trace data as a neutral substrate, LatencyPrism enables efficient human intervention by ensuring time spent on solving verified problems rather than sifting through noise. The mechanism we presented is an independent downstream tool to validate data richness. We have not integrated it into the main system because hard-coding rigid diagnostic rules into the monitoring agent invites brittleness under highly dynamic environments. This decoupling allows downstream users to develop specialized diagnostic applications tailored to evolving production needs without bloating the core infrastructure.
Limitations and Future Work.
 While LatencyPrism excels in latency spike detection, limitations exist. Its monitoring model relies on historical normal data for baseline construction. Therefore, new workloads or hardware upgrades require a brief warm up. Pre-existing persistent performance issues may not trigger alerts due to the lack of a valid normal reference. Semantic correlation for non-mainstream XPUs is limited by vendor toolchain openness. Future work will explore
