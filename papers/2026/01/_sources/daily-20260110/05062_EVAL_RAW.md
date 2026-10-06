Compositional Steering of Large Language Models with Steering Tokens (https://arxiv.org/html/2601.05062v1)
citeturn26872view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05062v1","lineno":119}); Total lines: 381
L88: To prevent overfitting of behavior tokens to instruction formulations, we define 10 different instruction paraphrases for each behavior (e.g., “{Answer, Respond, Reply} in Spanish”) and randomly sample one per training example.
L89: When training the composition token <and>, the teacher receives $x$ concatenated with instructions of two behaviours, $x\oplus I_{b_{i}}\oplus I_{b_{j}}$ (e.g., “Why can’t penguins fly? Answer in Spanish. Use 10 to 50 words.”) and the student receives $x\oplus\texttt{<b\textsubscript{i}>}\texttt{<and>}\texttt{<b\textsubscript{j}>}$ (e.g., “Why can’t penguins fly? <ES><and><words_10_50>”.
L90: Initialization and Orthogonality. We initialize embeddings of behavior tokens “semantically”: as the mean of the LLM’s (frozen) embeddings of tokens in the behavior’s instruction. We use zero initialization for the embedding of the composition token (we ablate this choice in §cite14†5.4 ): $\mathbf{e}_{\text{<and>}}=\mathbf{0}$, to avoid biasing it toward any one behavior and allowing it to learn “to compose” purely from the training data.
L91: To prevent the <and> token from collapsing into representations similar to existing behavior tokens, we introduce orthogonality regularization in composition training (we ablate its impact in §cite14†5.4 ): it forces the trainable <and> embedding to remain orthogonal to all frozen behavior embeddings:
L92: 
L93:  | $${\mathcal{L}_{\text{orth}}=\sum_{b\in\mathcal{B}_{\text{seen}}}\left({\mathbf{e}_{\text{<and>}}\cdot\mathbf{e}_{b}}/{(\|\mathbf{e}_{\text{<and>}}\|\cdot\|\mathbf{e}_{b}\|)}\right)^{2}}$$  |
L94: where $\mathcal{B}_{\text{seen}}$ is the set of all (frozen) behavior tokens seen in composition training. The final loss for the <and> token training is then: $\mathcal{L}=\mathcal{L}_{\text{dist}}+\lambda\cdot\mathcal{L}_{\text{orth}}$. We initially set $\lambda=0.5$ and found it to work well.
L95: ## 4 Experimental Setup
L96: 
L97: Unlike work on steering for subjective behaviors such as sycophancy or myopic reward cite60†Nguyen et al. (2025) ; cite47†Bayat et al. (2025) ; cite57†Scalena et al. (2024) ; cite41†Pai et al. (2025) , we follow cite36†Stolfo et al. (2025) and focus on verifiable constraints where satisfaction can be automatically assessed, allowing for a large-scale compositional evaluation while avoiding both human evaluation and costly and error-prone use of LLMs as judges cite64†Marioriyad et al. (2025) .
L98: Models. We experiment with seven instruction-tuned LLMs from four model families: Qwen3-4B, Qwen3-8B, Qwen3-14B, Llama-3.2-3B, Llama-3.2-8B, SmolLM3-3B, and OLMo-7B. We use Qwen-8B as the primary model for comparing steering tokens with baselines (§cite11†5.1 ) and the Qwen family models for the scaling analysis (§cite13†5.3 ). For efficiency, we use Qwen-4B in ablations (§cite14†5.4 ).
L99: Behaviors. We experiment with 15 behaviors from four categories: languages: Spanish, French, Italian, Portuguese, and German; length: 10-50, 50-70, 70-90, 90-120 words; formatting: lowercase, uppercase, title case; and structure: 1-5 sentences. To test compositional generalization, we partition properties into seen (11 used during <and> token training) and unseen (4 held out: German, title case, 70-90 words, 3 sentences).
L100: This design ensures that each category has held-out properties to validate zero-shot composition. We provide instructions for all behaviors in the Appendix cite22†E .
L101: Compositions.
L102: We evaluate two types of behavior combinations: (i) Seen compositions: both behaviors are from the seen set, i.e., their combination was part of the <and> token training (e.g., <ES> <and> <words_10_50>); here we test if the composition operator successfully learned to compose seen behaviors; (ii) Unseen compositions: one or both behaviors are from the unseen behavior set (e.g., <DE> <and> <words_10_50>, <ES> <and> <title_case> or <DE> <and> <title_case>: this setup tests the generalization ability of our composition token operator.
L103: In both cases, we test on 2-behavior and 3-behavior compositions. Crucially, 3-behaviour compositions are all unseen, since we train the <and> only on 2-behaviour combinations, providing a different test of generalization—to compositions with different number of behaviors.
L104: For the Qwen family, we contrast our default training of the composition token <and> exclusively on 2-behavior compositions (2-token-only), against training on both 2-behavior and 3-behavior compositions (2+3-token): this way we evaluate whether explicit training on 3-behavior compositions improves generalization or causes overfitting.
L105: Data. We source prompts from the Smoltalk dataset^{2}^{2} 2 The dataset is released under Apache 2.0 License. cite65†Allal et al. (2025) which contains instruction-labeled dialogs. We use Qwen3-30B-A3B-Instruct to separate the core question for each prompt from constraints (e.g., “respond in 5 sentences,”). For each of our 15 behaviors, we randomly sample 50k prompts and generate answers with Qwen3-30B-A3B-Instruct (for each example, we randomly sample from 10 behavior paraphrases).
L106: For the <and> token training, we generate responses for all cross-category 2-behavior combinations (e.g., language + length, language + format). We exclude all unseen behaviors (German, title case, 70-90 words, 3 sentences) from the training data creation and save them for evaluation of unseen compositions (see App. cite18†A for further details).
L107: For testing, we use 1,000 held-out prompts for each 2- and 3-behavior combination, resulting in >1M evaluations per model across all compositions and orderings of behavior tokens.
L108: Metrics. We measure the following: (1) Mean accuracy, as the percentage of LLM generations that satisfy all $k\in{2,3}$ behaviors, averaged across all $k!$ token orders: this way, we remove any potential model bias w.r.t. the order of behavior tokens; (2) Order variance is the largest absolute difference in accuracy across any two token orders of a composition, averaged across all compositions.
L109: Lower values indicate more robust, order-invariant behavior; and (3) Response quality: for accurate responses (i.e., satisfying all behavior) constraints, we evaluate semantic correctness and coherence of the answers on a Likert (1-5) scale, using an LLM judge (Qwen3-30B-A3B-Instruct). We measure whether steering accuracy comes at the expense of degraded content (see details in the Appendix. cite20†C ).
L110: Baselines and Variants. We compare our steering tokens against three baselines that instantiate three different types of steering. (1) In practice, instruction steering is the default paradigm for multi-behavior steering of LLMs; despite that, existing work on compositional steering cite37†Cao et al. (2024) ; cite50†Han et al. (2024) ; cite60†Nguyen et al. (2025) , with the exception of cite36†Stolfo et al. (2025) , fails to evaluate this competitive baseline.
L111: We simply append the behavior instructions $I_{b}$ to the prompt (e.g., “Answer in German. Use 70-90 words. Apply title case.”). To ensure fair comparison, we randomly sample from 10 behavior paraphrases. We note that we omit standard activation steering cite43†Rimsky et al. (2024) as a baseline, because cite36†Stolfo et al. (2025) shows that it, on its own, clearly and substantially trails instruction-based steering for verifiable behaviors.
L112: (2) Fine-tuning for behavior alignment is an expensive, but effective steering approach. We first train behavior-specific low-rank adapters with the same self-distillation objective, then merge individual adapters using an interference-reducing approach of cite66†Yu et al. (2024) ((LoRA DARE)); this is a meaningful parameter-space alternative to our input-space steering. (3) LM-Steer cite50†Han et al.
L113: (2024) is an established approach with steering vectors obtained as linear projections of LLMs’ word embeddings: as such, it is essentially a type of token-based steering; moreover, the authors claim (but do not quantify) LM-Steer’s compositional steering abilities.
L114: We also evaluate a simple concatenation of behavior tokens (i.e., no composition token <and>), shedding light on the necessity of explicit composition learning, i.e., whether the behavior tokens can interact implicitly through the LLM’s attention. Finally, we combine our token steering with instructions (Hybrid), testing the complementarity of learned vectors and natural language guidance.
L115: ## 5 Results and Analyses
L116:  | 2-Behavior Results  |  | 3-Behavior Results
L117: Method  | Seen $\uparrow$  | Unseen $\uparrow$  | Ord. Var. $\downarrow$  | Resp. Qual. $\uparrow$  |  | Seen $\uparrow$  | Unseen $\uparrow$  | Ord. Var. $\downarrow$  | Resp. Qual. $\uparrow$
L118: Baselines  |  |  |  |  |  |  |  |  |
L119: LoRA DARE cite66†Yu et al. (2024) | 81.5 $\pm 0.1$  | 44.8 $\pm 0.2$  | –  | 4.7  |  | 58.4 $\pm 0.1$  | 17.6 $\pm 0.1$  | –  | 4.6
L120: LM-Steer cite50†Han et al. (2024) | 18.1 $\pm 0.1$  | 13.4 $\pm 0.3$  | –  | 1.3  |  | 2.2 $\pm 0.1$  | 2.1 $\pm 0.2$  | –  | 1.2
L121: Instruction Steering cite36†Stolfo et al. (2025) | 90.7 $\pm 0.1$  | 71.8 $\pm 0.2$  | 7.8  | 4.9  |  | 83.7 $\pm 0.1$  | 54.0 $\pm 0.1$  | 18.1  | 4.9
L122: Steering Tokens  |  |  |  |  |  |  |  |  |
L123: Concatenation  | 81.3 $\pm 0.1$  | 62.1 $\pm 0.2$  | 25.3  | 4.8  |  | 59.6 $\pm 0.1$  | 33.2 $\pm 0.1$  | 55.8  | 4.8
L124: Composition (<and>)  | 90.9 $\pm 0.1$  | 76.9 $\pm 0.2$  | 5.3  | 4.9  |  | 83.1 $\pm 0.1$  | 59.5 $\pm 0.1$  | 25.5  | 4.9
L125: Hybrid: Composition (<and>) + Instr.  | 92.2 $\pm 0.1$  | 76.3 $\pm 0.2$  | 4.4  | 4.9  |  | 87.9 $\pm 0.1$  | 62.9 $\pm 0.1$  | 15.2  | 4.9
L126: Table 1: Results for compositional steering with Qwen-8B for seen and unseen 2- and 3-behavior combinations. Our full compositional steering, with the learned <and> composition operator, outperforms text instructions on unseen compositions; Combining our token steering with instructions (Hybrid) yields the best performance; Concatenation without explicit composition learning fails on complex compositions; LoRA DARE shows poor compositional generalization, whereas LM-Steer fails to compose altogether.
L127: Model  | Method  | Unseen (2|3) $\uparrow$  | Order Var. (2|3) $\downarrow$
L128: Qwen-4B  | Instruction  | 68.9 | 55.6  | 5.3 | 15.1
L129: Steering  | 69.1 | 60.7  | 6.2 | 22.7
L130: Hybrid  | 69.2 ($+0.3$) | 58.0 ($+2.4$)  | 5.3 ($+0.0$) | 18.6 ($+3.5$)
L131: Qwen-8B  | Instruction  | 71.8 | 54.0  | 5.1 | 15.1
L132: Steering  | 76.9 | 59.5  | 4.1 | 21.2
L133: Hybrid  | 76.3 ($+4.5$) | 62.9 ($+8.9$)  | 4.4 ($-0.7$) | 12.4 ($-2.7$)
L134: Llama-3B  | Instruction  | 66.7 | 33.8  | 3.1 | 8.7
L135: Steering  | 69.3 | 33.9  | 3.9 | 18.7
L136: Hybrid  | 74.9 ($+8.2$) | 43.4 ($+9.6$)  | 2.8 ($-0.3$) | 10.6 ($+1.9$)
L137: Llama-8B  | Instruction  | 67.8 | 40.2  | 3.6 | 13.6
L138: Steering  | 67.0 | 39.5  | 5.9 | 19.2
L139: Hybrid  | 76.3 ($+8.5$) | 52.9 ($+12.7$)  | 3.2 ($-0.4$) | 11.0 ($-2.6$)
L140: Smol-3B  | Instruction  | 53.2 | 32.5  | 5.1 | 14.5
L141: Steering  | 53.2 | 35.5  | 11.8 | 35.9
L142: Hybrid  | 53.5 ($+0.3$) | 37.2 ($+4.7$)  | 7.3 ($+2.2$) | 17.1 ($+2.6$)
L143: Olmo-7B  | Instruction  | 56.8 | 30.9  | 2.9 | 7.3
L144: Steering  | 56.9 | 28.4  | 3.6 | 12.3
L145: Hybrid  | 60.9 ($+4.1$) | 37.5 ($+6.6$)  | 3.7 ($+0.8$) | 6.4 ($-0.9$)
L146: Table 2: Cross-architecture generalization of steering tokens, text instructions, and hybrid methods across seven models spanning four architectural families. Hybrid methods consistently achieve the best performance across all architectures, with strong benefits on weaker compositional models (Llama, OLMo). The compositional advantage holds universally but shows architecture-dependent magnitudes. Numbers in brackets represent improvement on top “Instruction” baseline.
L147: See App.cite19†B for performance on seen categories.
L148:  |  | 2-Behaviour Results  |  | 3-Behaviour Results
L149: Model  | Method  | Seen $\uparrow$  | Unseen $\uparrow$  | Ord. Var. $\downarrow$  | Resp. Qual. $\uparrow$  |  | Seen $\uparrow$  | Unseen $\uparrow$  | Ord. Var. $\downarrow$  | Resp. Qual. $\uparrow$
L150: Qwen-4B  | Instruction  | 93.3  | 68.9  | 5.3 ($+0.0$)  | 4.8  |  | 88.2  | 55.6  | 15.1 ($+0.0$)  | 4.8
L151: Steering (2-only)  | 93.7  | 69.1  | 6.2  | 4.8  |  | 89.3  | 60.7 ($+5.1$)  | 22.7  | 4.8
L152: Hybrid  | 93.7 ($+0.4$)  | 69.2 ($+0.3$)  | 5.3 ($+0.0$)  | 4.8  |  | 90.7 ($+2.5$)  | 58.0  | 18.6  | 4.8
L153: Qwen-8B  | Instruction  | 91.0  | 71.6  | 5.1  | 4.9  |  | 82.9  | 52.1  | 15.1  | 4.9
L154: Steering (2-only)  | 90.9  | 76.9 ($+5.3$)  | 4.1 ($-1.0$)  | 4.9  |  | 83.1  | 59.5  | 21.2  | 4.9
L155: Steering (2+3)  | 91.2  | 77.0  | 4.2  | 4.9  |  | 85.9  | 59.7  | 15.5  | 4.9
L156: Hybrid  | 92.2 ($+1.2$)  | 76.3  | 4.4  | 4.9  |  | 87.9 ($+5.0$)  | 62.9 ($+10.8$)  | 12.4 ($-2.7$)  | 4.9
L157: Qwen-14B  | Instruction  | 92.1  | 72.2  | 5.2  | 4.9  |  | 88.2  | 61.4  | 11.2  | 4.9
L158: Steering (2-only)  | 92.9  | 75.2  | 4.6  | 4.9  |  | 90.4  | 68.0  | 13.9  | 4.9
L159: Steering (2+3)  | 93.0  | 73.8  | 5.3  | 4.9  |  | 89.7  | 63.9  | 17.3  | 4.9
L160: Hybrid  | 93.9 ($+1.8$)  | 78.3 ($+6.1$)  | 2.7 ($-2.5$)  | 4.9  |  | 91.7 ($+3.5$)  | 69.2 ($+7.8$)  | 6.2 ($-5.0$)  | 4.9
L161: Table 3: Scaling analysis comparing steering tokens, text instructions, and their hybrid combination. Both steering and instruction methods benefit from scale, while training on 2-behaviour combinations proves sufficient: explicit 3-behaviour supervision (2+3) helps variance at 8B but degrades performance at 14B, suggesting larger models learn compositional patterns from simpler examples. Hybrid methods achieve the best accuracy-variance tradeoff at all scales.
L162: Numbers in brackets—improvement on top “Instruction” baseline. See App. cite19†B for extended analysis.
L163: ### 5.1 Steering tokens are superior compositional generalizers
L164: 
L165: Table cite67†1 compares our compositional steering against the baselines—instructions, merging LoRA adapters cite68†Da Silva et al. (2025) and output steering cite50†Han et al. (2024) —for 2- and 3-behaviour compositions, with Qwen-8B as the LLM. We report performance for seen (during <and> training) and unseen behavior compositions, with the latter indicating compositional generalization.
L166: We find that training an explicit composition operator (<and> token) is crucial: simple concatenation of behavior tokens collapses on unseen 3-behaviour composition (33.2% vs. 59.6%) and exhibits larger order variance. Our full compositional steering outperforms text instructions on unseen compositions (+5.1% for 2-behavior compositions, +5.5% for 3-behavior compositions), while performing comparably on seen compositions.
L167: This implies that our learned composition operator generalizes better than natural language composition. Text instructions are slightly more order-robust, exhibiting lower order variance, despite lower accuracy. Importantly, Hybrid steering (tokens + instructions) achieves the best overall results (62.9% accuracy, 15.2% variance for the most difficult generalization case: unseen 3-behaviour compositions.
L168: This encouraging result suggests complementarity between our compositional token steering and natural language guidance. LoRA DARE fails to generalize compositionally, performing much worse on unseen compositions, while LM-Steer completely collapses, showcasing the challenges of compositional steering based on model internals. Response quality remains solid and is largely comparable across steering methods (except LM-Steer).
L169: <and> init.  | $\mathcal{L}_{\text{orth}}$  | Seen $\uparrow$  | Unseen $\uparrow$  | Ord. Var. $\downarrow$
L170: No <and> token  | –  | 73.6  | 49.7  | 27.0
L171: Zero vector  | ✗  | 94.5  | 66.9  | 11.2
L172: Zero vector  | ✓  | 93.7 ($-0.8$)  | 69.1 ($+2.2$)  | 5.3 ($-5.9$)
L173: “and” embedding  | ✗  | 94.2  | 55.2  | 9.4
L174: “and” embedding  | ✓  | 94.2 ($+0.0$)  | 70.8 ($+15.6$)  | 7.1 ($-2.3$)
L175: Avg. steering tokens  | ✗  | 94.3  | 58.4  | 8.6
L176: Avg. steering tokens  | ✓  | 93.5 ($-0.8$)  | 64.4 ($+6.0$)  | 6.2 ($-2.4$)
L177: Table 4: Ablation study of <and> token initialization and orthogonality regularization on Qwen-4B. All initialization strategies achieve similar seen performance, but differ on unseen combinations, isolating compositional generalization as the key differentiator. Orthogonality loss proves critical, while without the <and> token, performance collapses. Zero initialization with orthogonality provides the best accuracy-variance tradeoff.
L178: ### 5.2 Robustness across model families
L179: Table cite69†2 summarizes the compositional steering performance for steering tokens, instructions, and their Hybrid across six models (Qwen-4B/8B, Llama-3B/8B, SmolLM-3B, OLMo-7B) and four model families. The results render our findings from §cite11†5.1 to be robust across different LLM architectures: (1) our steering tokens largely outperform instruction-steering (and when not, they offer on par performance); (2) the Hybrid combination of tokens and instructions offers further gains.
L180: There is, however, some family-based variance: Qwen models are more steerable, and favor compositional steering tokens over instruction steering (76.9% for unseen 2-behavior on Qwen-8B); Llama models, in contrast, are much less steerable, regardless of the steering approach (Llama-8B: 39.5% token steering, 40.2% instructions).
L181: Importantly, the Hybrid combination of token-based compositional steeting and natural language instructions rescues weak models: we observe a +12.7% gain for Llama-8B for 3-behavior compositions. This again points to strong complementarity between our compositional token steering and natural language instructions.
L182: ### 5.3 Robustness across model sizes
L183: We next investigate whether compositional accuracy and robustness of our compositional steering tokens scale with model size, as well as whether training on both 2- and 3-behavior compositions improves generalization (compared to our default training on 2-behavior compositions only). Table cite70†3 summarizes the results. We observe that both compositional token steering and instruction-based steering benefit from scale.
L184: Performance on 3-behavior compositions for compositional steering tokens (training on 2-behavior compositions only) jumps from 59.5% at 8B to 68.0% at 14B (+8.5%), while instructions improve from 52.1% to 61.4% (+9.3%). The Hybrid approach also scales effectively, achieving 69.2% at 14B and becomes much more robust to behavior ordering, exhibiting only 6.2% order variance (compared to 18.6% at 4B).
L185: Somewhat surprisingly, explicitly training our composition token also for 3-behavior compositions degrades performance at 14B: (2-behavior +3-behavior training yields only 63.9% accuracy, compared to 68.0% we get when training only on 2-behavior compositions; and it also exhibits higher order variance (17.3% vs. 13.9%). This again suggests that we successfully learn a general composition operator (i.e., already from the 2-behavior compositions).
L186: At 8B, 2- + 3-behavior training provides marginal variance reduction (compared to 4B; from 21.2% to 15.5%) with comparable accuracy, indicating that training data efficiency is likely scale-dependent.
L187: (a) Seen – Steering vs Text
L188: 
L189: (b) Unseen – Steering vs Text
L190: 
L191: (c) Seen – Hybrid vs Text
L192: 
L193: (d) Unseen – Hybrid vs Text
L194: 
L195: Figure 2: Average relative performance gains (%) for Qwen14B (top row) and Llama (bottom row). Top 20 behaviour combinations (2- and 3-behaviour) yielding the largest differences between methods. Green bars indicate improvements over the text baseline; red bars indicate degradations.
L196: ### 5.4 Ablation: <and> token initialization and orthogonality constraint
L197: 
L198: In Table cite71†4 , we ablate initialization strategies and orthogonality regularization, to isolate what mechanisms enable compositional learning in the <and> token. We report results using Qwen 4B.
L199: We first observe that <and> is essential: without it, seen performance degrades to 73.6% (vs. 93-95% with <and>), and unseen to 49.7% (vs. 64-71%), and order variance increases to 27.0% (vs. 5-11%). All <and> initialization strategies achieve comparable seen performance (93-95%), suggesting that behavior learning does not depend on initialization. However, unseen performance varies widely (55-71%), isolating compositional generalization as the key differentiator.
L200: Orthogonality regularization is critical here, especially for semantic behavior initialization: “and” embedding without orthogonality achieves only 55.2% unseen, but with the orthogonality constraint it improves by 15.6%. For zero initialization, orthogonality primarily reduces variance from 11.2% to 5.3% while only modestly improving accuracy. Token-average initialization benefits least from orthogonality, suggesting that averaging of behavior embeddings provides a poor starting point for composition.
L201: These results stress the importance of (i) an explicit learned operator (the <and> token), and (ii) enforcing the orthogonality of its embedding to behavior token representations.
L202: ### 5.5 Per-behavior breakdown
L203: Figure cite72†2 presents a granular per-composition analysis for Qwen-14B and Llama-8B, revealing which behaviors benefit most from compositional token steering vs. text instructions. We find that unseen behavior combinations, and in particular title_case paired with language or length constraints, drive the gains of token steering. This indicates that unseen cross-category compositions benefit the most from learned <and> operators.
L204: However, LLM-dependent failure modes emerge: while Qwen-14B shows better performance with token steering for most unseen combinations, Llama-8B exhibits stark category-specific divergence, with token steering excelling on compositions with formatting behaviors but failing on compositions with the unseen length behavior (words_70_90), where the instruction steering seems superior.
L205: Critically, the hybrid combination seems to eliminate these failure modes, reaffirming that complementarity between steering with learned embeddings and text instructions is key for robust compositional control, especially for weaker LLMs.
L206: ## 6 Conclusion
L207: In this work, we presented steering tokens, an effective approach for compositional control of LLMs, that does not require modification of models’ internals. By means of self-distillation, in the first step we train input tokens (i.e., embeddings) for individual (automatically verifiable) behaviors; in the second step, we freeze the behavior tokens and train only the explicit composition token <and>.
L208: Our extensive experimentation renders compositional steering tokens (1) superior to instruction-based steering as well as to other steering methods, while maintaining comparable response quality; we further show that it is (2) complementary to instructions, obtaining further gains from combination with natural language-based guidance.
L209: Crucially, (3) we demonstrate that steering tokens successfully generalize to behaviors and compositions unseen during the training of our composition operator (i.e., the <and> token).
L210: Finally, we show that our compositional steering tokens generalize well across different model families and sizes, provide even larger steering gains for larger models. Importantly, training exclusively on 2-behavior compositions proves sufficient for larger models. This work introduces steering tokens as a solid mechanism for compositional control in LLMs, offering an efficient alternative to instruction-based steering while complementing it.
L211: ## Limitations
L212: 
L213: While steering tokens demonstrate strong compositional capabilities, several limitations warrant attention in future work:
L214: Constraint verifiability. Our evaluation focuses exclusively on verifiable behavioral properties (response length, formatting conventions, etc.) where ground-truth satisfaction is automatically assessed. Steering tokens represent a general control mechanism that applies to broader semantic constraints (tone, style, etc.), but evaluating such properties requires human annotation or LLM-based judges. Future work should extend compositional evaluation to subjective and nuanced behavioral dimensions.
L215: Compositional complexity. We evaluate compositions of up to three properties, demonstrating zero-shot generalization from 2-property training to 3-property inference. Real-world applications may require simultaneous control over many more constraints (e.g., language, length, tone, domain, etc.). Therefore, scaling steering tokens to higher-order compositions remains an open question, particularly regarding whether compositional accuracy degrades gracefully or rapidly as the property count increases.
L216: Model scale. Our experiments span 3B to 14B parameter models, observing compositional improvements with scale. However, frontier models now exceed those sizes, and it remains unclear whether steering tokens continue to benefit from scale or encounter diminishing returns. Extension to larger models would clarify whether compositional reasoning improves further and whether hybrid methods remain necessary at scale.
L217: ## References
L218:   * Allal et al. (2025) L. B. Allal, A. Lozhkov, E. Bakouch, G. M. Blázquez, G. Penedo, L. Tunstall, A. Marafioti, H. Kydlíček, A. P. Lajarín, V. Srivastav, et al. SmolLM2: When Smol Goes Big–Data-Centric Training of a Small Language Model. In Conference on Language Modeling (COLM), External Links: cite73†Link†openreview.net Cited by: cite74†§4 .
L219:   * Ansell et al. (2024) A. Ansell, I. Vulić, H. Sterz, A. Korhonen, and E. M. Ponti Scaling Sparse Fine-Tuning to Large Language Models. arXiv preprint arXiv:2401.16405. External Links: cite75†Link Cited by: cite76†§2 .
L220:   * Bayat et al. (2025) R. Bayat, A. Rahimi-Kalahroudi, M. Pezeshki, S. Chandar, and P. Vincent Steering Large Language Model Activations in Sparse Spaces. In Conference on Language Modeling (COLM), External Links: cite77†Link†openreview.net Cited by: cite78†§2 , cite79†§4 .
L221:   * Cao et al. (2024) Y. Cao, T. Zhang, B. Cao, Z. Yin, L. Lin, F. Ma, and J. Chen Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-Directional Preference Optimization. Advances in Neural Information Processing Systems (NeurIPS) 37, pp. 49519–49551. External Links: cite80†Link†proceedings.neurips.cc Cited by: cite81†§1 , cite76†§2 , cite82†§2 , cite83†§4 .

