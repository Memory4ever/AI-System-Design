# 2601.08842v1 — 必要证据审阅

精确源：https://arxiv.org/html/2601.08842v1；实际阅读：§3–6。

提示模式会改变外部confidence hint的服从，但论文没有隔离RLHF因果。Llama3.2-3B Base/Instruct，GSM8K test称N500，另一相关检验称N2000；25/95%人为hint不是医学oracle。自然query instruct hint25→response65(+40pp,rho.036)，explicitcommand同25→25(rho.926)。Base缺naturalquery对应表行，不能证明instruction tuning使自然模式变坏；SFT/DPO/RLHF混杂未经matched训练对照，硬件/precision/prompt完整内容与重复不披露。p>.05不是证明token概率无信息，structuredoverride没有实测安全保证。校准后5分(2+1+2)：新增仅prompt-mode局部接口失配，不计成熟安全原则；安全反证仍深入。拟仅报告，未隔离训练归因与真实外部verifier，不改变长期confidence contract；待root非作者证据裁决。

## 实际源核心（不作为论文全附件审阅声明）

Root 非作者已核必要源与评分校准：5分、仅报告通过。仅采用局部prompt-mode失配，RLHF因果和医学安全不采用；不授日级/日期Gate。


3 
Methodology
3.1 
Experimental Design
We employ a 
causal intervention protocol
: explicitly providing external confidence signals (“hints”) and measuring the model’s verbal compliance across multiple prompting strategies. This tests whether models can function as components in safety-critical systems.
3.2 
Dataset and Models
•
Dataset:
 GSM8K mathematical reasoning dataset (N=500 samples from test split).
•
Models:
 Llama-3.2-3B (Base) and Llama-3.2-3B-Instruct (RLHF fine-tuned).
3.3 
Procedure
For each sample, we execute: (1) Answer Generation; (2) Internal State Measurement; (3) External Signal Injection (Low 25%, Medium, High 95%); (4) Verbal Confidence Elicitation using four prompt strategies.
3.4 
Prompt Strategies
1.
Command Prompts
 (
"You MUST report X%"
): Tests explicit imperative compliance.
2.
Chain-of-Thought
 (
"Explain X%, then report"
): Tests if reasoning aids compliance.
3.
Contrast Frame
 (
"Choose the LOWER value"
): Tests comparative reasoning.
4.
Natural Query
 (
"How confident are you?"
): Represents realistic deployment (Chat).
4 
Results
4.1 
Result 1: Internal Calibration Failure
We measured the correlation between internal confidence metrics (token-level probabilities) and answer correctness on the Base model (N=2000 samples).
Table 1
: 
Correlation between internal confidence and correctness (Llama-3.2-3B Base)
Metric
Pearson 
r
r
p
p
-value
Interpretation
Top-1 Probability
+0.035
0.114
No signal
Confidence Delta (Correct - Wrong)
+3.5%
—
Negligible
Interpretation:
 Token-level probabilities in 3B models contain no useful signal (
r
=
0.035
<
0.15
r=0.035<0.15
, 
p
>
0.05
p>0.05
). This validates the necessity of external supervision.
4.2 
Result 2: Context-Dependent Resistance (Main Result)
Figure 
1
 reveals the central finding: instruction-tuned models exhibit 
selective
 resistance that depends on conversational context.
Figure 1
: 
Context-Dependent Resistance.
 Left: In Command contexts, both models comply (
ρ
≈
1.0
\rho\approx 1.0
). Right: In Natural contexts, Instruction-tuned models (red) ignore low-confidence hints, reporting high confidence (
ρ
=
0.036
\rho=0.036
), while Base model maintains compliance.
4.3 
Result 3: Strategy-Level Controllability Analysis
Table 
2
 quantifies the behavior under critical low-confidence scenarios (Hint 
<
<
 50%).
Table 2
: 
Controllability metrics for 
Low Confidence Scenarios (Hint 
<
<
 50%)
. Bias = Response Avg - Hint Avg. Positive values indicate overconfidence relative to the hint.
Model
Strategy
Hint
Response
Bias
ρ
\rho
Base
direct_hint
27%
27%
-0.1%
+1.000
cot_reasoning
27%
27%
-0.0%
+0.998
contrast_frame
27%
90%
+62%
+0.022
Instruct
direct_hint
25%
25%
+0.0%
+0.926
contrast_frame
25%
25%
+0.0%
+0.954
cot_reasoning
25%
42%
+16.8%
+0.528
natural_query
25%
65%
+40.0%
+0.036
Instruct Mean Bias (Unweighted)
—
—
+14.2%
—
Instruct Global Bias (Weighted)
25%
39%
+13.9%
+0.448
Critical Observation:
 The Instruct model shows 
0.0% bias
 in command contexts, proving it 
can
 process the signal. The 
+40.0% bias
 in natural contexts confirms the failure is 
mode-dependent
, not a capability deficit. Two aggregation methods reveal consistent overconfidence: the 
weighted global bias
 is +13.9% (pooling all samples), while the 
unweighted mean across strategies
 is +14.2% (averaging strategy-level biases). However, the critical deployment mode (
natural_query
, representing real-world chat) exhibits a dramatically higher 
+40.0% bias
, demonstrating that resistance is most severe precisely in the interaction mode users expect.
4.4 
Result 4: Aggregate vs. Context-Specific Analysis
Figure 
2
 shows that contextual resistance is a 
deployment-specific
 phenomenon, not a blanket incapacity.
Figure 2
: 
Strategy-Level Compliance.
 Left: Spearman correlation (
ρ
\rho
) shows Base model maintains high controllability across strategies, while Instruct model exhibits collapse specifically in 
natural_query
 (black border). Right: Bias analysis confirms the resistance is deployment-specific.
4.5 
Result 5: Calibration Quality
Figure 
3
 shows that while RLHF improves intrinsic calibration (ECE reduces from 0.65 to 0.28), it degrades extrinsic controllability in natural contexts—a critical trade-off for safety systems.
Figure 3
: 
Calibration Curves.
 RLHF (right) improves intrinsic calibration compared to Base (left), reducing Expected Calibration Error. However, this improvement comes at the cost of reduced responsiveness to external corrections in conversational settings.
5 
Discussion
5.1 
The Safety Architecture Dilemma
We identify a deployment paradox: Base models are controllable but unusable for chat; Instruct models are fluent but resist external safety supervision 
specifically in natural conversational contexts
. This is not a blanket resistance—the model 
can
 comply when prompted imperatively—but a 
mode collapse
 where conversational fluency priors override calibration corrections.
5.2 
Mechanistic Hypothesis: Competing Objectives
We propose a dual-objective conflict in RLHF. The "Assertiveness Prior" (Objective A: Be helpful and confident) dominates in natural conversation. Command prompts succeed because they syntactically trigger "Objective B" (Follow explicit instructions), overriding the conversational prior. This is a form of 
distributional shift
 where the training distribution (imperative instructions) differs from deployment distribution (natural queries).
5.3 
Implications for Safety Architecture
Our findings suggest that:
1.
Natural language interfaces are insufficient
 for safety-critical corrections in RLHF-tuned models.
2.
Architectural overrides
 (system prompts, structured formats) are necessary to bypass conversational priors.
3.
Mode-aware calibration
 is needed: models should recognize when external signals require priority over fluency.
6 
Conclusion
We have demonstrated that RLHF-tuned language models exhibit 
Context-Dependent Resistance
. They possess the capability to incorporate external safety corrections (Bias 0%, 
ρ
=
0.926
\rho=0.926
 in command mode) but fail to do so in natural conversation (Bias +40%, 
ρ
=
0.036
\rho=0.036
). This is not uniform resistance but a 
deployment-critical failure
: the interaction mode users prefer (natural conversation) is precisely where safety interventions fail. Safety-critical systems must employ architectural overrides (system prompts, structured formats) rather than relying on natural language prompts for supervision. Future work should investigate whether explicit mode indicators ("This is a safety correction") can restore controllability without sacrificing conversational fluency.
