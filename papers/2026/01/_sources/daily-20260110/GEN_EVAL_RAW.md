GenProve: Learning to Generate Text with Fine-Grained Provenance (https://arxiv.org/html/2601.04932v1)
citeturn26866view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04932v1","lineno":211}); Total lines: 547
L145: We fine-tune the model by maximizing the conditional likelihood of the reference output:
L146:  | $$\mathcal{L}_{\text{SFT}}(\theta)=-\sum_{i=1}^{N}\log p_{\theta}\!\left(A^{\mathrm{ref}}_{i}\mid Q_{i},D_{i}\right).$$  |  | (1)
L147: 
L148: This step provides a stable policy initialization that reliably produces syntactically valid provenance tags and on-topic content. Crucially, this structural foundation enables the subsequent RL stage to focus on refining the model’s provenance accuracy rather than struggling with basic formatting errors.
L149: ### 4.2 GRPO-based Reinforcement Learning
L150: 
L151: Reinforcement learning improves provenance accuracy and reduces unsupported statements by optimizing a reward that evaluates both content and provenance. Starting from the SFT policy $\pi_{\theta}$, we sample a group of candidate answers for each input $(Q,D)$ and update the policy using GRPO. The objective maximizes the expected reward:
L152:  | $$\mathcal{J}(\theta)=\mathbb{E}_{(Q,D)\sim\mathcal{D}_{\text{GRPO}}}\Big[\mathbb{E}_{A\sim\pi_{\theta}(\cdot\mid Q,D)}\big[R(A,A^{\mathrm{ref}})\big]\Big].$$  |  | (2)
L153: 
L154: The reward $R(A,A^{\mathrm{ref}})$ aggregates two components: a sentence-matching content reward and a reference-guided provenance F1 reward (Figure cite86†4 ).
L155: #### Reward Design.
L156: 
L157: GenProve computes rewards at sentence granularity by parsing provenance tags and splitting both the generated answer and the reference into sentence units. Let $A=(t_{1},\dots,t_{n})$ and $A^{\mathrm{ref}}=(t^{\mathrm{ref}}_{1},\dots,t^{\mathrm{ref}}_{M})$. We represent both answers as sentence–provenance pairs:
L158: 
L159:  | $$\begin{cases}A=\{(t_{j},P_{j})\}_{j=1}^{n},\\
L160: A^{\mathrm{ref}}=\{(t^{\mathrm{ref}}_{k},P^{\mathrm{ref}}_{k})\}_{k=1}^{M}.\end{cases}$$  |  | (3)
L161: Each $P_{j}$ (or $P^{\mathrm{ref}}_{k}$) is a set of triples of the form $(\mathrm{doc\_id},\mathrm{sent\_id},r)$ with $r\in\{\mathrm{Quotation},\mathrm{Compression},\mathrm{Inference}\}$.
L162: #### Reward A: Sentence-matching content similarity.
L163: 
L164: This reward encourages semantic alignment with the reference while preserving sentence-level structure. For each generated sentence $t_{j}$, we find the best-matching reference sentence by cosine similarity between sentence embeddings produced by a Sentence-Transformer encoder:
L165: 
L166:  | $$k(j)=\arg\max_{k\in\{1,\dots,M\}}\cos\big(\phi(t_{j}),\phi(t^{\mathrm{ref}}_{k})\big).$$  |  | (4)
L167: Here $\phi(\cdot)$ denotes the encoder. If the best cosine score is below a threshold $\tau_{c}$, the reward for this sentence is zero; otherwise we compute ROUGE-L between the matched pair:
L168: 
L169:  | $$\begin{split}r_{\text{sim}}(t_{j})&=\mathbb{I}\Big[\cos\big(\phi(t_{j}),\phi(t^{\mathrm{ref}}_{k(j)})\big)\geq\tau_{c}\Big]\\
L170: &\quad\cdot\mathrm{ROUGE\text{-}L}\big(t_{j},t^{\mathrm{ref}}_{k(j)}\big).\end{split}$$  |  | (5)
L171: 
L172: The content reward is the mean across sentences:
L173:  | $$R_{\text{sim}}(A,A^{\mathrm{ref}})=\frac{1}{n}\sum_{j=1}^{n}r_{\text{sim}}(t_{j}).$$  |  | (6)
L174: #### Reward B: Reference-guided provenance F1.
L175: 
L176: This reward encourages generating correct provenance triples and relation types. To reduce missed provenance, we align sentences inversely. For each reference sentence $t^{\mathrm{ref}}_{k}$, we retrieve the closest generated sentence by cosine similarity:
L177: 
L178:  | $$j(k)=\arg\max_{j\in\{1,\dots,n\}}\cos\big(\phi(t^{\mathrm{ref}}_{k}),\phi(t_{j})\big).$$  |  | (7)
L179: We gate mismatched pairs using a similarity threshold $\tau_{p}$. Given an aligned pair, we compare their provenance sets. Let $I_{k}=P_{j(k)}\cap P^{\mathrm{ref}}_{k}$ denote the set of correctly reproduced provenance triples. We compute sentence-level precision and recall as $\mathrm{Prec}_{k}=|I_{k}|/|P_{j(k)}|$ and $\mathrm{Rec}_{k}=|I_{k}|/|P^{\mathrm{ref}}_{k}|$, and define the provenance score by
L180:  | $$F1_{k}=\frac{2\,\mathrm{Prec}_{k}\,\mathrm{Rec}_{k}}{\mathrm{Prec}_{k}+\mathrm{Rec}_{k}+\epsilon}.$$  |  | (8)
L181: 
L182: The provenance reward averages sentence-level scores over all reference sentences, while gating out mismatched pairs:
L183: 
L184:  | $\begin{aligned} R_{\text{prov}}(A,A^{\mathrm{ref}})=\frac{1}{M}\sum_{k=1}^{M}\mathbb{I}\!\left[\cos\big(\phi(t^{\mathrm{ref}}_{k}),\phi(t_{j(k)})\big)\geq\tau_{p}\right]\cdot F1_{k}.\end{aligned}$  |  | (9)
L185: #### Composite reward.
L186: 
L187: We combine the two components into a single scalar reward:
L188: 
L189:  | $$R(A,A^{\mathrm{ref}})=\alpha\,R_{\text{sim}}(A,A^{\mathrm{ref}})+\beta\,R_{\text{prov}}(A,A^{\mathrm{ref}}),$$  |  | (10)
L190: 
L191: where $\alpha$ and $\beta$ balance content fidelity and provenance correctness. This design penalizes common failure modes shown in Figure cite86†4 , including incorrect relation typing and unsupported or out-of-document provenance.
L192: 
L193: ## 5 Experiments
L194: ### 5.1 Experimental Setup
L195: Models. We evaluate 14 LLMs, covering both open- and closed-source systems. The open-source models include Llama-3.1-8B-Instruct cite87†Grattafiori et al. (2024) , Gemma-3-12B-it cite88†Team et al. (2025a) , Yi-1.5-9B-Chat cite89†Liu et al. () , Qwen3-8B cite90†Yang et al. (2025) , InternLM2.5-7B-Chat cite91†Cai et al. (2024) , Hunyuan-7B-Instruct cite92†Zheng et al. (2025) , Vicuna-7B-v1.5 cite93†Zheng et al. (2023) , Baichuan2-7B-Chat cite94†Yang et al. (2023) , Qwen3-14B cite90†Yang et al. (2025) , GLM-4-9B cite95†GLM et al.
L196: (2024) , and GLM-4.5 cite95†GLM et al. (2024) . The closed-source models include Gemini 2.5 Pro cite96†Comanici et al. (2025) , GPT-5 cite97†Achiam et al. (2024) , and Kimi cite98†Team et al. (2025b) . All models use a unified input format of questions and source documents. The full inference prompt is given in Appendix cite43†C.1 .
L197: Training configuration. GenProve is trained in two steps. For supervised fine-tuning, we start from Qwen3-8B cite90†Yang et al. (2025) and perform full-parameter optimization with AdamW, using a learning rate of $2\times 10^{-5}$, a maximum sequence length of 2048, and gradient accumulation to achieve an effective batch size of 16.
L198: For GRPO alignment, we initialize from the SFT model and continue optimization under the same learning rate and sequence length settings, with temperature set to 1, $\beta=0.02$, and 4 iterations per update. For reward computation, the sentence-matching and provenance-alignment thresholds are set to $\tau_{c}=0.45$ and $\tau_{p}=0.50$, respectively.
L199: Model  | ROUGE-L$\uparrow$  | BLEU$\uparrow$  | METEOR$\uparrow$  | MoverScore$\uparrow$  | Prec.$\uparrow$  | Rec.$\uparrow$  | F1$\uparrow$  | Format (%)$\uparrow$  | LLM-as-judge (1–5)$\uparrow$
L200: Baichuan2-7B cite94†Yang et al. (2023) | 34.68  | 19.41  | 48.08  | 32.03  | 3.22  | 3.41  | 3.04  | 26.60  | 0.78
L201: Vicuna-7b-v1.5 cite93†Zheng et al. (2023) | 38.83  | 24.37  | 50.08  | 34.73  | 9.01  | 5.85  | 6.70  | 92.40  | 1.10
L202: InternLM2.5-7B cite91†Cai et al. (2024) | 47.79  | 30.60  | 53.47  | 43.60  | 12.64  | 13.35  | 11.94  | 80.24  | 1.67
L203: Hunyuan-7B cite92†Zheng et al. (2025) | 39.91  | 24.70  | 43.74  | 32.99  | 22.78  | 22.86  | 21.43  | 90.88  | 1.72
L204: Yi-1.5-9B cite89†Liu et al. () | 48.26  | 30.11  | 47.77  | 43.35  | 20.71  | 22.91  | 20.11  | 96.81  | 1.80
L205: Llama-3.1-8B cite87†Grattafiori et al. (2024) | 47.71  | 26.36  | 42.04  | 41.14  | 21.78  | 20.30  | 20.05  | 99.85  | 2.00
L206: GLM-4-9B cite95†GLM et al. (2024) | 50.33  | 32.62  | 50.00  | 44.93  | 34.57  | 34.12  | 32.79  | 100.0  | 2.16
L207: Qwen3-8B cite90†Yang et al. (2025) | 51.80  | 35.56  | 55.38  | 45.90  | 37.78  | 30.56  | 32.53  | 100.0  | 2.25
L208: Gemma-3-12B cite88†Team et al. (2025a) | 48.97  | 32.13  | 50.80  | 43.79  | 41.06  | 31.11  | 34.03  | 100.0  | 2.47
L209: Qwen3-14B cite90†Yang et al. (2025) | 52.85  | 35.70  | 55.34  | 47.06  | 45.80  | 40.33  | 41.16  | 99.70  | 2.59
L210: GLM-4.5-355B cite95†GLM et al. (2024) | 49.81  | 35.05  | 57.69  | 44.92  | 48.84  | 44.03  | 44.55  | 98.63  | 2.63
L211: Kimi cite98†Team et al. (2025b) | 49.33  | 31.24  | 51.56  | 43.84  | 31.55  | 32.09  | 29.70  | 99.09  | 2.20
L212: GPT-5 cite97†Achiam et al. (2024) | 41.79  | 20.01  | 38.83  | 36.38  | 21.37  | 16.73  | 17.88  | 99.85  | 2.23
L213: Gemini 2.5 Pro cite96†Comanici et al. (2025) | 48.75  | 31.77  | 53.09  | 44.79  | 46.68  | 42.86  | 42.92  | 100.0  | 2.57
L214: GenProve (Ours)  | 57.25  | 42.22  | 59.39  | 51.04  | 54.96  | 51.26  | 51.21  | 99.85  | 3.14
L215: Table 1: Main results on ReFInE. Our proposed GenProve consistently outperforms strong open-source and closed-source LLMs across answer quality, provenance accuracy, and LLM-based evaluation.
L216: Evaluation Metrics. We evaluate models along three axes: answer quality, provenance accuracy, and format validity. Answer quality is measured using ROUGE-L cite99†Lin (2004) , BLEU cite100†Papineni et al. (2002) , METEOR cite101†Banerjee and Lavie (2005) , BERTScore cite102†Zhang et al. (2020) , and MoverScore cite103†Zhao et al. (2019) , computed on answers excluding provenance tags.
L217: Provenance accuracy is assessed by sentence-level precision, recall, and F1 via exact matching over document id, sentence id, and relation type, while format validity reports the percentage of outputs that strictly follow the required provenance schema. Additionally, we conduct subjective evaluations with LLM and human judges: the former provides relation-specific scores, while the latter assesses answer quality and provenance correctness (prompts and guidelines in Appendices cite44†C.2 –cite45†C.3 ).
L218: ### 5.2 Main Results
L219: 
L220: Table cite104†1 presents the main results on ReFInE. GenProve achieves the best overall performance and ranks first on all evaluation axes, including answer quality, provenance accuracy, and the LLM-as-judge score. The gains are consistent across automatic metrics and subjective judging, demonstrating that generation-time fine-grained provenance training improves both the usefulness of answers and the reliability of sentence-level provenance.
L221: Across model groups, open-source systems exhibit substantial variance. Earlier chat-style or lightly instruction-tuned models, such as Baichuan2-7B and Vicuna-7B-v1.5, often fail to follow the provenance schema, leading to low format validity and weak provenance accuracy. In contrast, more recent open-source models, including Qwen3 and GLM-4, generate valid outputs more consistently and achieve markedly higher provenance F1 and LLM-judge scores.
L222: Among non-GenProve systems, GLM-4.5 is the strongest baseline, ranking second in both provenance quality and LLM-judge score. Closed-source models are competitive: Gemini 2.5 Pro is the strongest closed-source baseline, but still trails GenProve on the overall judge score.
L223: From the metric perspective, answer-quality metrics show that GenProve generates more faithful and fluent responses after provenance tags are removed. It exceeds the strongest baseline on ROUGE-L, BLEU, METEOR, and MoverScore, indicating improvements in both surface overlap and semantic similarity. Provenance metrics show the largest margin: GenProve achieves a substantially higher provenance F1 than the strongest baseline, suggesting more accurate sentence-level evidence localization and relation typing.
L224: Correct format highlights that formatting is necessary but not sufficient: several strong baselines already achieve near-perfect parseability, whereas weaker baselines fail frequently; GenProve maintains similarly high compliance. Finally, the LLM-as-judge score summarizes end-to-end quality under joint requirements of correctness, fluency, and traceability, where GenProve attains the highest overall score.
L225: ### 5.3 Ablation Study
L226: 
L227: Model  | BLEU  | BERTScore  | F1  | Format  | Judge
L228: --- | --- | --- | --- | --- | ---
L229: GenProve  | 42.22  | 61.98  | 51.21  | 99.85  | 3.14
L230: w/o Prov Reward  | 11.94  | 46.96  | 24.67  | 96.66  | 2.20
L231: w/o Sim Reward  | 24.60  | 44.50  | 60.32  | 95.74  | 2.71
L232: w/o GRPO  | 41.82  | 60.70  | 50.48  | 99.70  | 2.62
L233: Table 2: Ablation study on ReFInE. The results validate the necessity of GRPO alignment and the complementary roles of content similarity and provenance rewards. Figure 5: Performance breakdown by relation type (F1 score). The heatmap reveals a reasoning gap: while most models handle verbatim Quotation well, they struggle significantly with Inference. GenProve consistently outperforms baselines, showing the largest gains in complex provenance tasks (Compression and Inference).
L234: Figure 6: Learning dynamics during GRPO. Consistent upward trends in content similarity and provenance F1 rewards indicate GenProve improves provenance reliability without compromising answer faithfulness, achieving coordinated optimization of dual objectives.
L235: Table cite105†2 shows that GRPO alignment significantly boosts end-to-end quality, raising judge scores substantially over the SFT baseline. Reward ablations further confirm the two components are complementary. Removing the provenance reward drops provenance F1 and judge scores, implying similarity alone cannot enforce precise provenance. Conversely, removing the similarity reward improves F1 yet harms answer quality, showing provenance optimization alone is insufficient.
L236: Combining both maximizes the judge score, effectively balancing fluent answers with correct, typed provenance.
L237: ### 5.4 Diagnostic Analysis
L238: Performance by Relation Type. Figure cite106†5 reports F1 by provenance relation type, reflecting the reliability of sentence-level provenance beyond verbatim reuse. The heatmap reveals a clear difficulty ordering: Quotation is easiest, while Compression and Inference are substantially harder, indicating challenges in evidence abstraction and integration.
L239: GenProve achieves the strongest performance across all three relations and the highest average F1, with its largest gains on Compression and Inference, reflecting improved evidence localization and relation typing in harder cases.
L240: GRPO Training Dynamics. Figure cite107†6 visualizes reward trajectories during GRPO alignment. Both component rewards increase and stabilize, indicating the policy improves content alignment and provenance correctness jointly rather than oscillating between objectives.
L241: The total reward follows this upward trend, mirroring the complementary roles found in ablations: similarity optimization strengthens faithfulness, whereas PROVE-F1 strengthens typed provenance, and their combination supports superior overall quality.
L242: ### 5.5 Consistency with Human Evaluation
L243: 
L244: cite108†Image: Refer to caption Figure 7: Correlation between LLM-as-a-Judge scores and human ratings. The high Pearson correlation ($r=0.9395$) validates our automatic metric. Notably, GenProve occupies the top-right corner, demonstrating significantly superior performance over all baselines under both automated and human evaluations.
L245: To assess the reliability of LLM-as-a-Judge as our primary evaluation signal, we measure its consistency with human evaluation at the model level. Figure cite109†7 shows a strong positive correlation between LLM-as-a-Judge scores and human ratings, with a Pearson correlation coefficient of $r=0.9395$. This result indicates that the automatic judge closely aligns with human preferences under the same provenance-aware evaluation criteria, supporting its use for large-scale comparison in the main experiments.
L246: Detailed human evaluation results and scoring analyses are provided in Appendix cite48†C.4 and  cite50†C.6 .
L247: ## 6 Conclusion
L248: We introduce a paradigm shift from coarse citations to generation-time fine-grained provenance. By constructing the ReFInE dataset and developing the GenProve framework, we demonstrate that LLMs can be trained to transparently document their evidence usage via structured triples. Experiments confirm that GenProve balances generation quality with strict provenance constraints, establishing a new state-of-the-art across 14 strong LLMs.
L249: Despite these advances, the performance gap between simple Quotation and complex Inference suggests that verifiable reasoning remains a frontier challenge. We position ReFInE as a stepping stone towards self-auditing LLMs, models that not only generate knowledge but explicitly reason about the provenance of their own assertions.
L250: ## Limitations
L251: While GenProve establishes a new standard for fine-grained provenance, we identify three limitations to address in future work. (1) Inference latency. Generating structured provenance triples inevitably increases the output token count compared to standard generation. Although essential for trustworthiness, this introduces a slight latency trade-off in real-time applications. (2) Linguistic scope. Our current ReFInE dataset and evaluation primarily focus on English.
L252: Extending the Quotation-Compression-Inference taxonomy to multilingual or cross-lingual settings remains an open avenue for research. (3) Retrieval dependency. Our framework focuses on the generation stage. Like all RAG systems, end-to-end performance is bounded by the quality of the retriever; if retrieved documents contain no relevant information, the model cannot generate valid provenance.
L253: ## References
L254:   * Achiam et al. (2024) J. Achiam, S. Adler, S. Agarwal, L. Ahmad, et al. Gpt-4 technical report. External Links: 2303.08774, cite110†Link Cited by: cite111†§C.4 , cite112†Table 5 , cite113†Table 7 , cite114†§5.1 , cite115†Table 1 .
L255:   * Aly et al. (2024) R. Aly, Z. Tang, S. Tan, and G. Karypis Learning to generate answers with citations via factual consistency models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL), pp. 11876–11896. External Links: cite116†Link†aclanthology.org Cited by: cite117†§2 .
L256:   * Banerjee and Lavie (2005) S. Banerjee and A. Lavie METEOR: an automatic metric for MT evaluation with improved correlation with human judgments. In Proceedings of the ACL Workshop on Intrinsic and Extrinsic Evaluation Measures for Machine Translation and/or Summarization, pp. 65–72. External Links: cite118†Link†aclanthology.org Cited by: cite119†§5.1 .
L257:   * Cai et al. (2024) Z. Cai, M. Cao, H. Chen, K. Chen, et al. Internlm2 technical report. External Links: 2403.17297, cite120†Link Cited by: cite121†Table 5 , cite122†Table 7 , cite114†§5.1 , cite123†Table 1 .
L258:   * Cao and Wang (2024) S. Cao and L. Wang Verifiable generation with subsentence-level fine-grained citations. In Findings of the Association for Computational Linguistics ACL 2024, pp. 15584–15596. External Links: cite124†Link†aclanthology.org Cited by: cite125†Table 4 , cite126†§2 .
L259:   * Chen et al. (2022) J. Chen, R. Zhang, J. Guo, Y. Fan, and X. Cheng GERE: generative evidence retrieval for fact verification. In Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR), pp. 2184–2189. External Links: cite127†Link†dl.acm.org Cited by: cite128†Table 4 , cite126†§2 .
L260:   * Comanici et al. (2025) G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, et al. Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. External Links: 2507.06261, cite129†Link Cited by: cite111†§C.4 , cite130†Table 5 , cite131†Table 7 , cite114†§5.1 , cite132†Table 1 .
L261:   * Fan et al. (2025) M. Fan, C. Wang, C. Chen, Y. Liu, and J. Huang On the trustworthiness landscape of state-of-the-art generative models: a survey and outlook. International Journal of Computer Vision 133 (7), pp. 1–321–32. External Links: cite133†Link†doi.org Cited by: cite134†§1 .
L262:   * Gao et al. (2023) T. Gao, H. Yen, J. Yu, and D. Chen Enabling large language models to generate text with citations. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 6465–6488. External Links: cite135†Link†aclanthology.org Cited by: cite136†Table 4 , cite134†§1 , cite137†§1 , cite117†§2 .
L263:   * GLM et al. (2024) T. GLM, A. Zeng, B. Xu, B. Wang, et al. Chatglm: a family of large language models from glm-130b to glm-4 all tools. External Links: 2406.12793, cite138†Link Cited by: cite111†§C.4 , cite139†Table 5 , cite140†Table 5 , cite141†Table 7 , cite142†Table 7 , cite114†§5.1 , cite143†Table 1 , cite144†Table 1 .
L264:   * Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, et al. The llama 3 herd of models. External Links: 2407.21783, cite145†Link Cited by: cite146†Table 5 , cite147†Table 7 , cite114†§5.1 , cite148†Table 1 .
L265:   * Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, et al. DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning. Nature 645, pp. 633–638. External Links: cite149†Link†doi.org Cited by: cite150†§1 .
L266:   * Hsu et al. (2024) I. Hsu, Z. Wang, L. Le, L. M. Werlen, N. Peng, C. Lee, and T. Pfister Calm: contrasting large and small language models to verify grounded generation. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 12782–12803. External Links: cite151†Link†aclanthology.org Cited by: cite152†Table 4 , cite117†§2 .
L267:   * Huang et al. (2024) L. Huang, X. Feng, W. Ma, Y. Gu, W. Zhong, X. Feng, W. Yu, W. Peng, D. Tang, D. Tu, et al. Learning fine-grained grounded citations for attributed large language models. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 14095–14113. External Links: cite153†Link†aclanthology.org Cited by: cite154†Table 4 , cite155†§2 .
L268:   * Kambhamettu et al. (2024) H. Kambhamettu, J. Flores, and A. Head Traceable text: deepening reading of ai-generated summaries with phrase-level provenance links. External Links: cite156†Link , 2409.13099 Cited by: cite126†§2 .
L269:   * Li et al. (2024) W. Li, J. Li, W. Ma, and Y. Liu Citation-enhanced generation for llm-based chatbots. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL), pp. 1451–1466. External Links: cite157†Link†aclanthology.org Cited by: cite158†Table 4 , cite134†§1 , cite117†§2 .
L270:   * Li and Chen (2025) X. Li and J. Chen SCIRGC: multi-granularity citation recommendation and citation sentence preference alignment. External Links: cite159†Link , 2505.20103 Cited by: cite160†Table 4 , cite155†§2 .
L271:   * Lin (2004) C. Lin ROUGE: a package for automatic evaluation of summaries. In Text Summarization Branches Out, pp. 74–81. External Links: cite161†Link†aclanthology.org Cited by: cite119†§5.1 .
L272:   * [19] J. Liu, R. Batista-Navarro, Q. Liu, N. Muennighoff, G. Zhang, Y. LI, X. Wang, and W. Neiswanger Open science for foundation models. In ICLR 2025 Workshop Proposals, External Links: cite162†Link†iclr.cc Cited by: cite163†Table 5 , cite164†Table 7 , cite114†§5.1 , cite165†Table 1 .
L273:   * Papineni et al. (2002) K. Papineni, S. Roukos, T. Ward, and W. Zhu Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL), pp. 311–318. External Links: cite166†Link†aclanthology.org Cited by: cite119†§5.1 .
L274:   * Slobodkin et al. (2024) A. Slobodkin, E. Hirsch, A. Cattan, T. Schuster, and I. Dagan Attribute first, then generate: locally-attributable grounded text generation. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL), pp. 3309–3344. External Links: cite167†Link†aclanthology.org Cited by: cite168†Table 4 , cite117†§2 .
L275:   * Team et al. (2025a) G. Team, A. Kamath, J. Ferret, S. Pathak, et al. Gemma 3 technical report. External Links: 2503.19786, cite169†Link Cited by: cite170†Table 5 , cite171†Table 7 , cite114†§5.1 , cite172†Table 1 .
L276:   * Team et al. (2025b) K. Team, Y. Bai, Y. Bao, G. Chen, et al. Kimi k2: open agentic intelligence. External Links: 2507.20534, cite173†Link Cited by: cite111†§C.4 , cite174†Table 5 , cite175†Table 7 , cite114†§5.1 , cite176†Table 1 .
L277:   * Xing et al. (2020) X. Xing, X. Fan, and X. Wan Automatic generation of citation texts in scholarly papers: a pilot study. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL), pp. 6181–6190. External Links: cite177†Link†aclanthology.org Cited by: cite178†Table 4 , cite117†§2 .
L278:   * Yang et al. (2023) A. Yang, B. Xiao, B. Wang, B. Zhang, C. Bian, et al. Baichuan 2: open large-scale language models. External Links: 2309.10305, cite179†Link Cited by: cite111†§C.4 , cite180†Table 5 , cite181†Table 7 , cite114†§5.1 , cite182†Table 1 .
L279:   * Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, et al. Qwen3 technical report. External Links: 2505.09388, cite183†Link Cited by: cite111†§C.4 , cite184†Table 5 , cite185†Table 5 , cite186†Table 7 , cite187†Table 7 , cite114†§5.1 , cite188†§5.1 , cite189†Table 1 , cite190†Table 1 .

