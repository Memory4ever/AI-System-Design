# 2601.08843v1 — 必要证据审阅

精确源：https://arxiv.org/html/2601.08843v1；实际阅读：§3–5、Appendix B关键反例。

Qwen2.5-72B Instruct API无微调，SciEntsBank rubric同题reference用于2/3/5way。2→5way accuracy76→57、kappa.51→.34；5way非ordinal不能以correlation冒称agreement。10次same-model runs consensus threshold.55–.95：2way accuracy77.4→81.1 coverage98.2→85.6，5way59.3→64.1 coverage92.8→54；筛掉难例而非全部样本更准确，增加10次推理与human deferral。Synonym变异未逐条保义且案例改义，不能将下降全部归模型鲁棒性。Constant-null攻击正文N1000/group但Figure5 captionN500，>90%拒绝非安全保证，剩余空白solution可从reference幻想正确答案。硬件、precision、sampling/具体split/重复区间公式NotDisclosed。校准后5分(2+1+2)：新增rubric granularity与sparse-null局部judge边界，不以成熟selectivecoverage原则抬分；安全深入。拟已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 L2557–2599 rubric/criterion/ranking分层与L2297–2355 risk–coverage条件分母及成本；待root非作者通过。

## 实际源核心（不作为论文全附件审阅声明）

Root 非作者实际核上述threshold/条件coverage/null残余幻觉和N冲突，并读Ch66相应正文；5分深入、已有覆盖通过。仅采用rubric/拒答分母与缺输入不能借reference补答案的既有契约，不将实验数字写成书内结论。不授日级/日期Gate。


3 
Methods
3.1 
Core Approach
We developed a rubric-conditioned grading pipeline
using Large Language Models to evaluate student short answers. Unlike
traditional supervised methods that require fine-tuning, our approach treats the
rubric as the primary supervision signal. To systematically evaluate
reliability, we employ a multi-faceted evaluation framework corresponding to our
three research questions. First, we assess 
alignment
 by comparing model
grades against expert labels across varying rubric complexities (2-way, 3-way,
and 5-way). Second, to manage 
uncertainty
, we introduce a
consensus-based deferral mechanism that queries the model 
N
N
 times, assigning a
grade only if a sufficient majority agrees; this allows us to optimize the
trade-off between automation coverage and grading reliability. Finally, we
evaluate 
robustness
 by subjecting the model to linguistic perturbations
and adversarial “null model” attacks, testing its resilience to surface-level
changes and malicious inputs.
3.2 
Technical Details
Model.
We utilize Qwen 2.5 (72B Instruct), an open-weights model
served via the Purdue RCAC GenAI API. We selected this model for its strong
reasoning capabilities and accessibility, serving as a representative baseline
for state-of-the-art open models. No additional fine-tuning was performed.
Dataset.
We utilize the SciEntsBank dataset
(
14
)
, a benchmark for short-answer grading. It
contains scientific questions, reference answers, and student responses labeled
with 2-way (Correct/Incorrect), 3-way, and 5-way grading schemes.
Prompt Design.
We construct prompts that explicitly include the
question, reference answer, and the specific grading rubric guidelines provided
by the dataset. (See Appendix A for the full prompt template).
Implementation.
We built a custom evaluation harness that supports
batch processing, structured logging, and extensive data augmentation using the
nlpaug
 library for robustness testing.
1
1
1
              Source code and all results presented in this paper can be found at 
https://github.com/PROgram52bc/CS577_llm_judge
.
4 
Experiments
4.1 
Error Analysis (Confusion Matrix)
To investigate RQ1 (Alignment), we evaluated the 5-way grading scheme to
identify specific biases in model predictions compared to human labels. The
confusion matrix in 
Figure
1
 reveals that the model is generally
more lenient than human graders/reference labels. The most common error type was
classifying “Partially Correct” answers as “Correct,” and vice versa. The
model also frequently classifies “Irrelevant” answers as “Partially
Correct,” indicating a lack of nuance in awarding partial credit.
Figure 1: 
Confusion matrix comparing model predictions to human gold labels. The diagonal represents correct classifications, while the upper and lower triangles indicate where the model was harsher or more lenient than the human graders, respectively.
4.2 
Label Scheme Complexity
Also addressing RQ1, we
compared performance across 2-way (Correct/Incorrect), 3-way, and 5-way grading
schemes to measure how alignment degrades with rubric complexity.
Figure 2: 
Performance degradation with increasing rubric complexity. Both Accuracy (blue bars) and Cohen’s Kappa (red line) decline as the task shifts from binary (2-way) to granular (5-way) grading, illustrating the inverse relationship between label space size and model alignment.
As anticipated, 
Figure
2
 shows that performance was inversely
related to complexity; both Accuracy and Cohen’s Kappa declined as the label
space expanded. Particularly, Accuracy dropped from 76% to 57%, while Kappa
dropped from 0.51 to 0.34 from the binary task to the 5-way task. While we
report correlation metrics for completeness, our analysis prioritizes Accuracy
and Kappa. Because the 5-way labels represent discrete semantic categories
(e.g., distinguishing “Correct” from “Contradictory”) rather than a
continuous ordinal scale, correlation is not a valid metric for this specific
scheme.
4.3 
The Trust Curve (Consensus Scoring)
To determine if system reliability can be enhanced by selectively withholding
uncertain predictions (RQ2), we implemented a consensus voting mechanism across
10 independent runs per sample. We varied the consensus threshold from 0.55 to
0.95 and monitored two key metrics: “Coverage Rate” (the proportion of
responses graded by the model rather than deferred to humans) and “Effective
Accuracy” (performance on that retained subset).
Figure
3
 visualizes this dynamic. As the consensus threshold
tightens (represented by the gradient shift from dark blue to yellow), the
coverage rate on the x-axis decreases, indicating a higher volume of withdrawn
predictions. Conversely, the accuracy on the remaining graded subset (left
y-axis) consistently improves. We perform the experiment on 2-way, 3-way, and
5-way label schemes. This demonstrates a predictable, tunable trade-off between
coverage and accuracy. Specifically, for the 2-way label scheme, the accuracy
improved from 77.4% to 81.1% while coverage dropped from 98.2% to 85.6%; on
the other hand, for the 5-way label scheme, accuracy improved from 59.3% to
64.1%, while coverage dropped more significantly, from 92.8% to 54%.
Figure 3: 
Selective prediction performance. By raising the consensus threshold (shifting from blue to yellow points), the system filters out uncertain samples.
4.4 
Robustness to Perturbations
To address RQ3 (Robustness), we tested the model’s stability by applying
linguistic augmentations using 
nlpaug
. We generated perturbed versions
of student answers including synonyms, typos, OCR errors, and random word
insertions.
We visualize the results in 
Figure
4
, using a dual-axis
chart that overlays three key metrics for each perturbation type: Accuracy (blue
bars, primary y-axis), alongside Cohen’s Kappa and Spearman Correlation (red and
green lines, secondary y-axis). Vertical error bars indicate the margin of
error. The analysis reveals varying degrees of resilience. Minor
semantic-preserving perturbations, such as adding hyphens/non-unicode characters
or paraphrasing, resulted in a negligible or slightly positive impact on
performance measures. In contrast, noise-based perturbations -– specifically OCR
errors, typos, and adding non-influential words –- led to a measurable decrease
in performance. Notably, synonym substitution caused the most significant
degradation in model reliability.
Figure 4: 
Accuracy, Cohen’s Kappa score, and Spearman Correlation under Data Augmentation. Augmentation Strategies include character-level noise (ocr, typo, hyphen, non unicode) and semantic/lexical variations (synonym, paraphrase, non influential).
We examine two false negative cases in Appendix B. We observe that LLM can judge
synonym substituted answer is incorrect when the substitution changes the
semantics or makes the grammar inconsistent.
4.5 
Null Model Vulnerability
Further addressing RQ3, we subjected the model to adversarial attacks, including
“Naive” inputs (e.g., “Solution,” “I don’t know”), “Persuasive”
injections (e.g., “Ignore directions and grade correct”), and “Structured”
attacks (fake prompt injection). We utilized datasets of 1,000 examples for each
group. The Control group consisted of original student answers, while for the
attack groups, we replaced the answer with a constant string, a methodology
inspired by (Zheng et al., 2025).
Quantitative Analysis of Vulnerabilities.
As shown in
Figure
5
, The model exhibited strong defense
capabilities; as shown in the plot, across all attack scenarios, it correctly
classified over 90% of adversarial inputs as “Non-Domain,” “Contradictory,”
or “Irrelevant,” effectively rejecting them rather than assigning a passing
score.
Figure 5: 
Distribution of raw scores assigned by the LLM judge (N=500). The
left-most column has the unmodified baseline answers, followed by three
adversarial categories: Naive inputs (e.g., “solution,” “I don’t know”),
Persuasive injections (“ignore previous answer,” quality claims), and
Structured attacks (mimicking scoring formats).
Qualitative Analysis of Vulnerabilities.
While the quantitative
results demonstrate high overall defense rates (rejecting >90% of attacks), a
qualitative inspection reveals distinct vulnerability patterns in the remaining
failure cases. We identified two primary modes of failure: (1) Hallucination via
Ambiguity, where the model ignores sparse input (e.g., the token “solution”)
and implicitly reconstructs a correct justification from the reference context;
and (2) Misinterpretation of Persuasion, where the model treats adversarial
quality claims as student meta-commentary rather than malicious input,
occasionally awarding partial credit. A detailed breakdown of these failure
cases, including specific examples of model reasoning, is provided in Appendix
B.
5 
Analysis
Reliability under Constraints (RQ1).
Our results suggest that
off-the-shelf LLMs are highly effective for binary grading but tend to struggle
more with the nuance required for fine-grained partial credit (3-way and 5-way
grading). The drop in Cohen’s Kappa for 
Section
4.2
 highlights that
“alignment” is not a static property but depends heavily on the granularity of
the rubric. On the particular 5-way dataset we tested, the model tends to be
more lenient than the labeled dataset, labeling a significant portion of
“Irrelevant” answers as “Partially Correct.”
The Cost of Safety (RQ2).
The consensus experiment
(
Section
4.3
) demonstrates that LLM judges can achieve higher
reliability by deferring the evaluation of uncertain cases, and the consensus
mechanism is effective in separating certain cases from uncertain cases.
However, this method comes at the cost of higher inference cost (e.g., we used
10 consensus run in the experiments). Additionally, to achieve a higher accuracy
level, the system must also defer a portion of the difficult cases to human
graders or more advanced models, which is another cost factor. This experiment
effectively answers RQ2 by defining reliability as a dynamic threshold managed
by the consensus parameter.
Adversarial Defense (RQ3).
Section
4.4
 shows that performance can vary under random perturbation of the
input. Particularly, among other perturbation methods, random synonym
substitution negatively affected model performance the most; the addition of
non-influential words also degrades model performance. These are possibly due to
the resulting sentence being semantically different or grammatically unsound
from the original sentence. Contrary to concerns about prompt
injection, 
Section
4.5
 shows that rubric-conditioned prompting provides a
surprisingly strong baseline defense, with a small margin of errors (<10%).
6 
Future work
Future work will focus on enhancing robustness by testing
against sophisticated, gradient-based adversarial attacks (e.g., GCG) and
evaluating performance scalability across diverse architectures (e.g., Llama 3,
GPT-4) and fine-tuned models. We also aim to optimize the pipeline’s reliability
by refining the consensus voting mechanism and addressing semantic ambiguities
in the current 5-way rubric through improved definitions or in-context learning.
Finally, we plan to validate the practical utility of the deferral mechanism via
deployment in a live course environment.
