# 09694 necessary exact-v1 evidence

Source: https://arxiv.org/html/2601.09694v1
Fetched2026-10-03. Necessary method/evaluation excerpt, not implementation/runtime replication.

拟2+1+2=5标准已读方法§3/实验§4且因代理归因深入核反侧：敏感度Wanda权重激活+gradient zscore供Gemini3Flash JSON选择，再校准PPL升15% rollback。Qwen3 4B/8B，A10080GB，C4 128samples length2048，收集activation16/gradient8/PPL32，target50%。Table2/3对照是magnitude structured2:4/4:8，而作者用非均匀Wanda启发；未给相同mask/敏感度/rollback、非LLM controller消融，不能把收益归因agent或selfreflection。Table2/3在43.02/45.58%取性能，而Table4末态50.73/50.46%且校准PPL!=WikiTextPPL，不能拼作同点。未测latency/token/API成本及precision，稀疏率非速度。不采用19x generalclaim；保留实际流程作为有限设计样例，root实际核§3/4及Ch49 L469–489后，通过5分标准完成/仅报告：成熟artifact calibration与quality-runtime取舍已有，但独有LLM收益未隔离，不能新增长期可靠self-reflection命题；不是因已有主题而缩池。

## Primary excerpt

3 Method


 3.1 Overview


 Our agent-guided pruning framework consists of four key components: (1) layer-wise sensitivity profiling using activation and gradient statistics, (2) an LLM agent that iteratively selects layers to prune based on normalized metrics, (3) a self-reflection mechanism that enables the agent to learn from previous decisions, and (4) a checkpoint rollback system that maintains model quality. Unlike prior work that applies uniform or hand-crafted sparsity ratios, our method adaptively determines per-layer pruning amounts through learned decision-making.



 3.2 Layer Sensitivity Profiling


 For each linear layer ℓ \ell in the model, we construct a comprehensive sensitivity profile combining multiple statistical measures. Following Wanda  [ 2 ] , we compute the weight-activation metric:






 𝐒 ℓ = | 𝐖 ℓ | ⊙ ‖ 𝐗 ℓ ‖ 2 \mathbf{S}_{\ell}=|\mathbf{W}_{\ell}|\odot\|\mathbf{X}_{\ell}\|_{2}

 (1)



 where 𝐖 ℓ ∈ ℝ d o ​ u ​ t × d i ​ n \mathbf{W}_{\ell}\in\mathbb{R}^{d_{out}\times d_{in}} is the weight matrix, 𝐗 ℓ ∈ ℝ N × d i ​ n \mathbf{X}_{\ell}\in\mathbb{R}^{N\times d_{in}} are the input activations collected over N N calibration samples, | ⋅ | |\cdot| denotes element-wise absolute value, ⊙ \odot is the Hadamard product, and ∥ ⋅ ∥ 2 \|\cdot\|_{2} computes the ℓ 2 \ell_{2} -norm across samples. The sensitivity score for layer ℓ \ell is defined as the k k -th percentile of active (non-zero) weights in 𝐒 ℓ \mathbf{S}_{\ell} , where k = 10 k=10 in our experiments.


 To capture gradient information inspired by Wanda++  [ 3 ] , we compute gradient importance as:






 𝐆 ℓ = 1 M ​ ∑ i = 1 M | ∇ 𝐖 ℓ ℒ i | \mathbf{G}_{\ell}=\frac{1}{M}\sum_{i=1}^{M}|\nabla_{\mathbf{W}_{\ell}}\mathcal{L}_{i}|

 (2)



 where ℒ i \mathcal{L}_{i} is the language modeling loss on calibration sample i i and M M is the number of gradient samples. We collect gradients every third iteration to balance computational cost with information gain.


 For model-agnostic comparison across heterogeneous layers, we normalize both metrics using z-score standardization:






 z ℓ ( s ) = s ℓ − μ s σ s + ϵ , z ℓ ( g ) = g ℓ − μ g σ g + ϵ z_{\ell}^{(s)}=\frac{s_{\ell}-\mu_{s}}{\sigma_{s}+\epsilon},\quad z_{\ell}^{(g)}=\frac{g_{\ell}-\mu_{g}}{\sigma_{g}+\epsilon}

 (3)



 where s ℓ s_{\ell} and g ℓ g_{\ell} are the raw sensitivity and gradient scores for layer ℓ \ell , μ \mu and σ \sigma denote mean and standard deviation across all layers, and ϵ = 10 − 9 \epsilon=10^{-9} prevents division by zero. Negative z-scores indicate below-average sensitivity (safer to prune), while positive z-scores indicate above-average sensitivity (riskier to prune).


 The complete profile for layer ℓ \ell is: 𝒫 ℓ = { z ℓ ( s ) , z ℓ ( g ) , ρ ℓ } \mathcal{P}_{\ell}=\{z_{\ell}^{(s)},z_{\ell}^{(g)},\rho_{\ell}\} , where ρ ℓ \rho_{\ell} is the current sparsity ratio of layer ℓ \ell .



 3.3 LLM Agent Design


 At each iteration t t , we query a foundation model (gemini-3-flash-preview) to select layers for pruning. The agent receives:



 •

 Current global sparsity ρ t \rho_{t} and target sparsity ρ ∗ \rho^{*}

 •

 Layer profiles { 𝒫 ℓ } ℓ = 1 L \{\mathcal{P}_{\ell}\}_{\ell=1}^{L} sorted by sensitivity z-score

 •

 Current and baseline perplexity: PPL t \text{PPL}_{t} , PPL 0 \text{PPL}_{0}

 •

 Feedback summary from iteration t − 1 t-1 (if t > 1 t>1 )




 The agent is instructed to reason about which layers are safe to prune based on the statistical profiles, considering both the gap remaining to target sparsity and the model’s current health (perplexity degradation). The agent outputs structured JSON containing:



 •

 reasoning : Natural language explanation of the pruning strategy

 •

 stop_pruning : Boolean indicating whether to terminate

 •

 layer_decisions : List of (layer name, additional sparsity) pairs




 where additional sparsity δ ℓ ∈ [ 0.01 , 0.15 ] \delta_{\ell}\in[0.01,0.15] specifies how much additional sparsity to induce in layer ℓ \ell . We use structured output with JSON schema to ensure reliable parsing.



 3.4 Self-Reflection Mechanism


 To enable the agent to learn from its decisions, we implement an iterative feedback loop. After pruning at iteration t t , we compute:



 •

 Sparsity gain: Δ ​ ρ t = ρ t + 1 − ρ t \Delta\rho_{t}=\rho_{t+1}-\rho_{t}

 •

 Perplexity change: Δ PPL = PPL t + 1 − PPL t PPL t × 100 % \Delta_{\text{PPL}}=\frac{\text{PPL}_{t+1}-\text{PPL}_{t}}{\text{PPL}_{t}}\times 100\%




 At iteration t + 1 t+1 , the agent receives a feedback summary containing:

 •

 Its previous reasoning and layer selections

 •

 The observed sparsity gain and perplexity change

 •

 A qualitative assessment (e.g., "Excellent - High sparsity gain with minimal PPL impact")




 This feedback enables the agent to recognize effective patterns (e.g., prioritizing layers with highly negative z-scores) and adjust its strategy (e.g., becoming more conservative as perplexity degrades). The system prompt explicitly instructs the agent to analyze past decisions and refine its approach accordingly.


 Algorithm 1 LLM-Guided Pruning with Self-Reflection


 1:

 Model ℳ \mathcal{M} , calibration data 𝒟 \mathcal{D} , target sparsity s target s_{\text{target}}



 2:

 LLM ℒ \mathcal{L} , rollback threshold τ rollback \tau_{\text{rollback}}



 3:

 Compute baseline perplexity PPL 0 \text{PPL}_{0} on 𝒟 \mathcal{D}



 4:

 Initialize checkpoint 𝒞 ← ∅ \mathcal{C}\leftarrow\emptyset , iteration memory ℋ ← ∅ \mathcal{H}\leftarrow\emptyset



 5:

 for t = 1 , … , T t=1,\ldots,T do



 6:

   Save checkpoint 𝒞 ← { 𝐖 ( l ) } l = 1 L \mathcal{C}\leftarrow\{\mathbf{W}^{(l)}\}_{l=1}^{L} , PPL 𝒞 ← PPL t − 1 \text{PPL}_{\mathcal{C}}\leftarrow\text{PPL}_{t-1}



 7:

   Collect activations { 𝐀 ( l ) } \{\mathbf{A}^{(l)}\} and gradients { 𝐆 ( l ) } \{\mathbf{G}^{(l)}\} from 𝒟 \mathcal{D} // Wanda++ metrics



 8:

    for layer l = 1 , … , L l=1,\ldots,L do



 9:

    Compute sensitivity: 𝐒 ( l ) = | 𝐖 ( l ) | ⊙ 𝐀 ( l ) \mathbf{S}^{(l)}=|\mathbf{W}^{(l)}|\odot\mathbf{A}^{(l)}



 10:

    Compute z-scores: z sens ( l ) , z grad ( l ) z_{\text{sens}}^{(l)},z_{\text{grad}}^{(l)} from 𝐒 ( l ) , 𝐆 ( l ) \mathbf{S}^{(l)},\mathbf{G}^{(l)}



 11:

    end for


 12:

   Query LLM: π t ← ℒ ⁡ ( { z sens ( l ) , z grad ( l ) , s t ( l ) } , ℋ t − 1 ) \pi_{t}\leftarrow\mathcal{L}(\{z_{\text{sens}}^{(l)},z_{\text{grad}}^{(l)},s_{t}^{(l)}\},\mathcal{H}_{t-1}) // Layer stats + feedback



 13:

    if π t . stop = true \pi_{t}.\text{stop}=\text{true} then



 14:

     break



 15:

    end if


 16:

    for ( l , Δ ​ s ) ∈ π t . decisions (l,\Delta s)\in\pi_{t}.\text{decisions} do



 17:

    Prune layer l l by sparsity Δ ​ s \Delta s using 𝐒 ( l ) \mathbf{S}^{(l)} (Wanda)



 18:

    end for


 19:

   Compute new perplexity PPL t \text{PPL}_{t} and sparsity s t s_{t}



 20:

    if PPL t / PPL t − 1 > τ rollback \text{PPL}_{t}/\text{PPL}_{t-1}>\tau_{\text{rollback}} then



 21:

    Restore checkpoint: { 𝐖 ( l ) } ← 𝒞 \{\mathbf{W}^{(l)}\}\leftarrow\mathcal{C} , PPL t ← PPL 𝒞 \text{PPL}_{t}\leftarrow\text{PPL}_{\mathcal{C}} // Rollback



 22:

    end if


 23:

   Store feedback: ℋ t ← { π t , s t − 1 , s t , PPL t − 1 , PPL t } \mathcal{H}_{t}\leftarrow\{\pi_{t},s_{t-1},s_{t},\text{PPL}_{t-1},\text{PPL}_{t}\} // Self-reflection



 24:

    if s t ≥ s target s_{t}\geq s_{\text{target}} then



 25:

     break



 26:

    end if


 27:

 end for


 28:

 return Pruned model ℳ \mathcal{M}






 3.5 Checkpoint Rollback Mechanism


 To prevent catastrophic degradation, we implement a safety mechanism that monitors perplexity changes. Before each pruning operation, we save the current model state. After pruning, if:






 PPL t + 1 − PPL t PPL t > τ \frac{\text{PPL}_{t+1}-\text{PPL}_{t}}{\text{PPL}_{t}}>\tau

 (4)



 where τ = 0.15 \tau=0.15 (15% threshold), we rollback to the previous checkpoint, discard the current iteration’s decisions, and provide negative feedback to the agent. This rollback is communicated through the self-reflection loop with the assessment "Poor - Excessive PPL degradation, consider more conservative approach."



 3.6 Complete Algorithm


 Algorithm  1 presents the complete agent-guided pruning procedure.




 4 Experiments


 4.1 Experimental Setup


 Models. We evaluate our method on two Qwen3 models: Qwen3-4B and Qwen3-8B  [ 27 ] . These models represent different scales within the same architectural family, enabling us to assess generalization across model sizes.


 Baselines. We compare against two structured pruning methods that achieve similar sparsity levels:

 •

 2:4 Structured Pruning : Prunes 2 out of every 4 consecutive weights, achieving ∼ \sim 42-45% sparsity. This pattern is hardware-efficient on NVIDIA GPUs with Ampere architecture and beyond.

 •

 4:8 Structured Pruning : Prunes 4 out of every 8 consecutive weights, also achieving ∼ \sim 42-45% sparsity with better density than 2:4.




 Table 1: MMLU performance by category for Qwen3-8B. Our agent-guided method maintains substantially better performance than structured baselines across all knowledge domains, with Social Sciences showing the strongest retention at 79.2% of baseline performance.



 Category
 BASE
 2:4
 4:8
 Ours


 (%)
 (%)
 (%)
 (%)



 STEM
 74.20
 31.51
 34.83
 52.00

 Humanities
 75.85
 28.95
 34.37
 54.42

 Social Sciences
 82.04
 32.87
 38.50
 64.97

 Other
 77.60
 31.59
 38.09
 58.75

 Overall
 77.38
 31.35
 36.29
 56.67




 Both baselines use magnitude-based pruning as implemented in standard pruning libraries. We do not include unstructured magnitude pruning or SparseGPT as baselines because recent work  [ 5 ] has shown that while these methods achieve good perplexity scores, they suffer from even worse factual knowledge degradation than structured methods.


 Evaluation Protocol. We follow the LLM-KICK benchmark  [ 5 ] evaluation protocol:

 •

 MMLU   [ 23 ] : 5-shot evaluation on 57 subjects covering STEM, humanities, social sciences, and other domains. We report overall accuracy and per-category breakdowns.

 •

 FreebaseQA   [ 24 ] : Factual question-answering on 20,358 questions. This metric directly measures factual knowledge retention.

 •

 WikiText-2 Perplexity   [ 25 ] : Language modeling performance on the full WikiText-2 test set.




 All evaluations use the full datasets without truncation to ensure comprehensive assessment.


 Implementation Details. We use 128 calibration samples of sequence length 2048 from the C4 dataset  [ 26 ] . The LLM agent is gemini-3-flash-preview with temperature 0.5 to balance creativity and consistency. We set target sparsity to 50%, though the algorithm may stop earlier if the agent determines further pruning would be too harmful. Activation collection uses 16 samples, gradient collection uses 8 samples, and perplexity evaluation uses 32 samples. The rollback threshold is τ = 0.15 \tau=0.15 (15% perplexity increase). All experiments run on a single NVIDIA A100 80GB GPU.



 4.2 Main Results


 Tables  2 and  3 present the comprehensive results for Qwen3-8B and Qwen3-4B respectively.


 Table 2: Comprehensive evaluation on Qwen3-8B at ∼ \sim 43% sparsity. Our agent-guided method substantially outperforms structured pruning baselines across all metrics, particularly in factual knowledge retention (19× improvement over 4:8).



 Method
 Sparsity
 MMLU
 FreebaseQA
 Perplexity


 (%)
 (%)
 (%)
 (WikiText-2)

 BASE (Dense)
 0.00
 77.38
 50.56
 9.72

 2:4 Structured
 42.40
 31.35
 0.22
 103.01

 4:8 Structured
 42.40
 36.29
 1.33
 60.67

 Ours (Agent-Guided)
 43.02
 56.67
 25.16
 19.06

 Relative Improvement over Best Baseline (4:8):

 Ours vs 4:8
 +0.62
 +56.2%
 +1791%
 -68.6%




 Table 3: Comprehensive evaluation on Qwen3-4B at ∼ \sim 45% sparsity. Our method demonstrates consistent improvements over structured baselines, with particular strength in preserving general task performance (MMLU) and reducing perplexity degradation.



 Method
 Sparsity
 MMLU
 FreebaseQA
 Perplexity


 (%)
 (%)
 (%)
 (WikiText-2)

 BASE (Dense)
 0.00
 71.29
 32.43
 13.64

 2:4 Structured
 45.16
 26.04
 0.20
 319.75

 4:8 Structured
 45.16
 29.24
 0.51
 81.28

 Ours (Agent-Guided)
 45.58
 44.43
 2.08
 39.40

 Relative Improvement over Best Baseline (4:8):

 Ours vs 4:8
 +0.42
 +51.9%
 +308%
 -51.5%




 For Qwen3-8B at 43% sparsity, our method achieves 56.67% MMLU accuracy, representing a 56.2% relative improvement over the 4:8 structured baseline. More dramatically, we retain 25.16% FreebaseQA accuracy compared to just 1.33% for 4:8—a 19× improvement that directly addresses the catastrophic factual knowledge collapse identified by LLM-KICK  [ 5 ] . Perplexity increases by only 96% compared to 524% for 4:8, demonstrating substantially better language modeling preservation.


 For Qwen3-4B at 45.58% sparsity, we observe consistent patterns: 51.9% relative MMLU improvement (44.43% vs 29.24%), 4.1× better FreebaseQA retention (2.08% vs 0.51%), and 51.5% lower perplexity degradation. These results demonstrate that agent-guided pruning generalizes effectively across model scales.


 Table  1 presents the detailed MMLU breakdown by category for Qwen3-8B. Our method preserves performance across all categories, with particularly strong results in Social Sciences (79.2% of baseline) and Humanities (71.7% of baseline).


 Figure 1: Cumulative statistics for agent-guided pruning on Qwen3-8B across 21 iterations. Top left: Sparsity evolution showing gradual progression to 50% target. Top right: Perplexity evolution showing controlled degradation with 2 rollback events. Bottom left: Per-iteration sparsity gains, with most iterations achieving 1-3% progress. Bottom right: Per-iteration perplexity changes, showing the agent learns to keep PPL increases below 2% in most iterations.


 Figure 2: Cumulative statistics for agent-guided pruning on Qwen3-4B across 40 iterations. The agent achieves larger sparsity gains (3-9%) in early iterations when the model is robust, then becomes more conservative as perplexity rises. Four rollback events (iterations 10, 15, 25, 32) are followed by visible strategy adjustments, demonstrating effective learning from negative feedback.


 Figure 3: Performance comparison on Qwen3-8B at ∼ \sim 43% sparsity across three evaluation metrics. Our agent-guided method substantially outperforms structured pruning baselines, particularly in preserving factual knowledge (FreebaseQA) where structured methods experience catastrophic degradation.


 Figure 4: Performance comparison on Qwen3-4B at ∼ \sim 45% sparsity. The pattern of improvements is consistent with the 8B model, demonstrating that agent-guided pruning generalizes effectively across model scales.


 Figure 5: MMLU performance by category for Qwen3-8B. Our method maintains substantially better performance than structured baselines across all knowledge domains, with Social Sciences showing the strongest retention.


 Figure 6: Relative improvements of our agent-guided method over the best structured baseline (4:8) for both model sizes. Positive percentages indicate superior performance; for perplexity, we show the reduction in degradation (higher is better). The consistent improvements across models and metrics demonstrate the robustness of our approach.


 Table 4: Iteration statistics for agent-guided pruning. The low rollback rates (9.5-10%) demonstrate effective self-correction through the reflection mechanism, with both models successfully reaching the 50% target sparsity.



 Statistic
 Qwen3-8B
 Qwen3-4B

 Total Iterations
 21
 40

 Successful Iterations
 19
 36

 Rollbacks
 2
 4

 Rollback Rate
 9.5%
 10.0%

 Target Sparsity
 50.0%
 50.0%

 Final Sparsity
 50.73%
 50.46%

 Target Achievement
 101.5%
 100.9%

 Baseline PPL
 22.06
 27.90

 Final PPL
 29.49
 53.09

 PPL Degradation
 +33.7%
 +90.3%





 4.3 Agent Behavior Analysis


 Table  4 summarizes the iteration statistics for both models. The Qwen3-8B model reached 50.73% sparsity in 21 iterations with only 2 rollbacks (9.5% rollback rate), while Qwen3-4B reached 50.46% sparsity in 40 iterations with 4 rollbacks (10% rollback rate). These low rollback rates indicate that the agent makes predominantly correct decisions, with the self-reflection mechanism enabling effective learning across iterations.


 Figures  1 and  2 visualize the iterative pruning process for both models. The top panels show the evolution of sparsity (left) and perplexity (right) across iterations. The orange lines represent the state before each pruning decision, while green lines show the state after pruning. The close tracking of these lines demonstrates that the agent makes small, incremental adjustments rather than large, risky changes. The bottom panels show per-iteration statistics: sparsity gain achieved (left) and perplexity change incurred (right).


 For Qwen3-8B, we observe that the agent learns to maintain steady progress toward the target, with most iterations achieving 1-3% sparsity gains while keeping perplexity changes below 2%. The two rollback events (visible as gaps in the bottom panel) occur at iterations 17 and 20, when the agent becomes too aggressive and triggers the 15% PPL threshold. After each rollback, the agent adjusts its strategy to be more conservative.


 For Qwen3-4B, the pruning trajectory shows similar patterns but with more iterations required to reach the target. The agent achieves particularly large sparsity gains (3-9%) in early iterations (2-3) when the model is relatively robust, then becomes more conservative as perplexity begins to rise. The four rollback events are distributed across iterations 10, 15, 25, and 32, each followed by visible strategy adjustments in subsequent iterations.


 These visualizations reveal several key behaviors: (1) the agent learns to "front-load" pruning early when the model is most robust, (2) it becomes progressively more conservative as cumulative perplexity degradation increases, (3) rollbacks are rare and trigger meaningful strategy changes, and (4) the agent successfully navigates the trade-off between sparsity gain and model quality preservation throughout the pruning process.


 The agent’s reasoning reveals several learned patterns: (1) prioritizing layers with highly negative sensitivity z-scores (typically below -1.0), (2) avoiding layers with positive gradient z-scores indicating high loss impact, (3) becoming more conservative as perplexity degrades, and (4) accelerating pruning when perplexity remains stable. The self-reflection feedback enables the agent to recognize when it has been too aggressive (high perplexity increase) or too conservative (minimal sparsity gain), adjusting its strategy accordingly.



 4.4 Visualization


 Figures  3 and  4 visualize the performance comparison across all three metrics for both model sizes. The dramatic differences in FreebaseQA—where structured methods experience near-total collapse—clearly illustrate the severity of the factual knowledge degradation problem and our method’s effectiveness in addressing it.


 Figure  5 shows the MMLU category breakdown for Qwen3-8B, demonstrating that our approach preserves capabilities across diverse knowledge domains rather than exhibiting selective preservation in specific areas. Figure  6 presents the relative improvements over the 4:8 baseline, highlighting our method’s consistent advantages across metrics.




 5 Conclusion


 We introduced agent-guided pruning, a novel framework where foundation models adaptively compress other foundation models through iterative reasoning and self-reflection. By constructing layer-wise sensitivity profiles that combine Wanda-inspired weight-activation metrics with gradient importance scores, normalized as z-scores for model-agnostic comparison, we enable an LLM agent to intelligently select which layers to prune at each iteration while learning from previous outcomes through a self-reflection mechanism. We evaluated our approach on Qwen3 models (4B and 8B parameters) at approximately 45% sparsity, demonstrating substantial improvements over structured pruning baselines: 56% relative improvement in MMLU accuracy, 19× better factual knowledge retention on FreebaseQA, and 69% lower perplexity degradation compared to 4:8 structured pruning. With only 9.5-10% rollback rates across 21-40 iterations, our framework exhibits effective self-correction without requiring retraining or manual heuristic design. These results directly address the critical factual knowledge collapse problem identified by recent benchmarks, establishing that foundation models can effectively guide neural network compression in ways that preserve capabilities missed by traditional metrics.



