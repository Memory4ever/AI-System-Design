Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning (https://arxiv.org/html/2601.04710v1)
citeturn26871view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04710v1","lineno":500}); Total lines: 649
L451: MeZO(Prefix)  | 90.1  | 65.7  | 69.6  | 63.0  | 60.6  | 56.0  | 59.1  | 71.0  | 70.4  | 76.0  | 23.2
L452: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L453: MeZO-GV(Prefix)  | 92.1  | 66.8  | 70.9  | 64.5  | 60.8  | 58.2  | 62.7  | 74.0  | 72.7  | 78.8  | 24.8
L454: TABLE V: Average task performance of various methods across three rounds on OPT-13B. Results are reported for zero-shot, in-context learning (ICL), ZO-AdaMU (extends zeroth-order optimization to the Adam algorithm), HiZOO (Hessian matrix-based gradient estimation in ZO optimization), SubZero (decomposes parameter mapping into low-dimensional subspaces), MeZO, and their variants that incorporate guiding vectors (GV), LoRA, and prefix tuning. Fine-tuning using the Adam is also included.
L455: The best performance for each task among the zeroth-order optimization methods is highlighted in bold.
L456: Task Type  | —– classification —–  | —– multiple choice —–  | —– generation —–
L457: Task  | SST2  | RTE  | CB  | BoolQ  | WSC  | WIC  | MultiRC  | COPA  | ReCoRD  | SQuAD  | DROP
L458: Zero-shot  | 58.8  | 59.6  | 46.4  | 59.0  | 38.5  | 55.0  | 46.9  | 80.0  | 81.2  | 46.2  | 14.6
L459: ICL  | 87.0  | 62.1  | 57.1  | 66.9  | 39.4  | 50.5  | 53.1  | 87.0  | 82.5  | 75.9  | 29.6
L460: ZO-AdaMU (2×)  | 92.1  | 72.9  | 67.9  | 73.0  | 61.5  | 60.7  | 63.0  | 89.0  | 83.0  | 82.4  | 32.0
L461: ZO-AdaMU (LoRA)  | 88.0  | 72.0  | 71.6  | 72.6  | 60.1  | 56.4  | 58.9  | 88.0  | 83.2  | 76.8  | 32.4
L462: ZO-AdaMU (Prefix)  | 88.0  | 61.8  | 72.3  | 74.9  | 56.5  | 58.2  | 61.9  | 86.0  | 82.8  | 85.2  | 30.4
L463: HiZOO  | 92.1  | 69.3  | 69.4  | 67.3  | 63.5  | 59.4  | 61.3  | 88.0  | 81.4  | 81.9  | 25.0
L464: HiZOO(LoRA)  | 90.6  | 67.5  | 69.6  | 70.5  | 63.5  | 60.2  | 60.2  | 87.0  | 81.9  | 83.8  | 25.1
L465: HiZOO(Prefix)  | 92.0  | 71.8  | 69.6  | 73.9  | 60.6  | 60.0  | 64.8  | 87.0  | 81.2  | 83.2  | 25.3
L466: MeZO(FT)  | 91.4  | 66.1  | 67.9  | 67.6  | 63.5  | 61.1  | 60.1  | 88.0  | 81.7  | 84.7  | 30.9
L467: SubZero(FT)  | 92.1  | 74.0  | 73.2  | 75.3  | 65.4  | 60.8  | 61.0  | 88.0  | 82.3  | 84.5  | 32.0
L468: MeZO-GV(FT)  | 93.9  | 73.5  | 71.6  | 72.5  | 65.4  | 61.4  | 62.5  | 89.0  | 82.9  | 84.9  | 31.7
L469: SubZero-GV(FT)  | 94.7  | 74.8  | 73.9  | 76.8  | 64.4  | 62.7  | 63.2  | 89.0  | 83.1  | 84.9  | 31.3
L470: MeZO(LoRA)  | 89.6  | 67.9  | 66.1  | 73.8  | 64.4  | 59.7  | 61.5  | 84.0  | 81.2  | 83.8  | 31.4
L471: SubZero(LoRA)  | 93.8  | 75.5  | 71.4  | 76.1  | 65.4  | 60.3  | 60.3  | 89.0  | 81.9  | 83.7  | 31.3
L472: MeZO-GV(LoRA)  | 91.6  | 72.6  | 72.8  | 75.6  | 66.3  | 60.9  | 61.9  | 89.0  | 82.9  | 84.9  | 32.7
L473: SubZero-GV(LoRA)  | 94.0  | 75.8  | 73.8  | 77.6  | 65.4  | 63.9  | 64.1  | 90.0  | 83.8  | 85.3  | 32.4
L474: MeZO(Prefix)  | 90.7  | 70.8  | 69.6  | 73.1  | 60.6  | 59.9  | 63.7  | 87.0  | 81.4  | 84.2  | 28.9
L475: SubZero(Prefix)  | 91.7  | 73.6  | 80.3  | 76.3  | 62.1  | 61.1  | 63.5  | 88.0  | 82.0  | 83.7  | 32.0
L476: MeZO-GV(Prefix)  | 92.4  | 74.8  | 73.2  | 76.6  | 63.5  | 61.8  | 64.4  | 90.0  | 82.7  | 84.3  | 30.9
L477: SubZero-GV(Prefix)  | 93.1  | 76.2  | 85.7  | 77.1  | 64.4  | 64.1  | 65.1  | 89.0  | 82.5  | 85.1  | 32.9
L478: FT  | 92.0  | 70.8  | 83.9  | 77.1  | 63.5  | 70.1  | 71.1  | 79.0  | 74.1  | 84.9  | 31.3
L479: TABLE VI: Task Performance Comparison for Different Methods on Llama2-7B.
L480: Task  | SST2  | RTE  | BoolQ  | WSC  | WIC
L481: --- | --- | --- | --- | --- | ---
L482: MeZO-10k  | 85.3  | 58.1  | 72.1  | 60.8  | 57.8
L483: MeZO-20k  | 88.7  | 62.1  | 80.1  | 62.1  | 60.8
L484: MeZO-GV-10k  | 90.4  | 64.3  | 81.3  | 62.5  | 62.3
L485: MeZO-10k(LoRA)  | 87.7  | 60.6  | 76.9  | 58.9  | 56.3
L486: MeZO-20k(LoRA)  | 93.7  | 63.3  | 79.5  | 62.5  | 57.5
L487: MeZO-GV-10k(LoRA)  | 94.3  | 65.7  | 80.7  | 61.5  | 61.4
L488: ### V-A Medium-sized Language Models
L489: As shown in Table cite87†IV , the experimental results demonstrate that GV-based methods, particularly MeZO-GV, consistently outperform both vanilla MeZO and baseline approaches across a wide range of tasks. This highlights that our proposed method achieves significant performance improvements.
L490: By leveraging guiding vectors, MeZO-GV enhances fine-tuning efficiency, achieving significant performance gains in classification tasks (e.g., +3.8% on SST-2), multiple-choice tasks (e.g., +5.0% on COPA), and generation tasks (e.g., +3.2% on SQuAD). Notably, MeZO-GV excels in complex scenarios, such as WSC (+3.9% improvement) and MultiRC (+5.3% improvement), where vanilla MeZO and baseline methods exhibit limited effectiveness.
L491: Additionally, the proposed method demonstrates significantly accelerated convergence rates, as illustrated in Figure cite40†3 and cite88†4 . For instance, on SST-2 and WSC, MeZO-GV achieves performance comparable to vanilla MeZO at 20,000 steps in just 6,000 and 1,000 steps, respectively. These results highlight MeZO-GV's ability to stabilize the optimization process while effectively adapting to diverse task requirements, establishing it as a robust and memory-efficient fine-tuning framework.
L492: Fig. 2: Validation Accuracy on SST2 and BoolQ Tasks for Llama2-7B and Llama2-13B. All experiments are conducted with a batch size of 16. For LoRA-based methods, the learning rate is set to 1e-4, while for full-parameter methods, the learning rate is set to 5e-7.
L493: ### V-B Large Language Models
L494: With the promising results from OPT-1.3B, we scale the model to larger sizes and architectures to further validate the proposed methods. As shown in Table cite89†V , the experimental results on OPT-13B demonstrate that GV-based methods, such as MeZO-GV and SubZero-GV, consistently outperform their non-GV counterparts and baseline approaches across a wide range of tasks.
L495: In classification tasks, SubZero-GV(FT) achieves 94.7% accuracy on SST-2, surpassing MeZO(FT) by 2.7%, whileMeanwhile, SubZero-GV(Prefix) attains 85.7% accuracy on CB, outperforming ZO-AdaMU(Prefix) by 13.4%. SubZero-GV(Prefix) achieves 76.2% accuracy on RTE, marking a 5.4% improvement over MeZO(Prefix), and scores 65.1% on MultiRC, leading all compared methods.
L496: In generation tasks, SubZero-GV (LoRA) achieves 85.3% on SQuAD, outperforming MeZO (LoRA) by 1.5%, while MeZO-GV(LoRA) achieves 32.7% on DROP, surpassing MeZO (LoRA) by 1.3%. In multiple-choice tasks, GV-based methods consistently demonstrate advantages: MeZO-GV (Prefix) achieves 90.0% accuracy on COPA, outperforming MeZO (Prefix) by 3.0%. Compared to zeroth-order optimization methods, GV-based approaches exhibit superior performance across all 11 tasks.
L497: Additionally, when compared to gradient-based methods, GV-based methods excel in 9 out of 11 tasks.
L498: To further validate the effectiveness of the proposed method, we extend our approach to the Llama2-7B model, with the experimental results presented in Table cite90†VI . The results demonstrate that our GV-based methods consistently outperform non-GV variants across multiple tasks while also achieving significant efficiency improvements. Specifically, GV-based methods achieve superior performance with only 10,000 training steps, surpassing the results of other methods that are trained for 20,000 steps.
L499: GV-based methods exhibit strong performance across various tasks. For instance, MeZO-GV-10k achieves 90.4% accuracy on SST-2, outperforming both MeZO-10k (85.3%) and MeZO-20k (88.7%) with half the training steps. Similarly, MeZO-GV-10k (LoRA) achieves 94.3% accuracy on SST-2, surpassing MeZO-10k (LoRA) (87.7%) and MeZO-20k (LoRA) (93.7%).
L500: On more challenging tasks such as WSC and WIC, GV-based methods demonstrate consistent improvements, achieving 62.5% and 62.3% accuracy, respectively, outperforming non-GV methods with fewer training steps.
L501: Additionally, we conduct experiments on larger models, including Llama2-13B and OPT-30B. The experimental results in Tabel cite91†VII and cite92†VIII further validate the effectiveness and scalability of guiding vector (GV)-based methods across diverse model sizes and tasks. On Llama2-13B, GV-based methods consistently outperform non-GV variants, demonstrating significant performance improvements with reduced training steps.
L502: For instance, MeZO-GV-10k(LoRA) achieves 93.7% accuracy on SST2, surpassing MeZO-10k(LoRA) (89.7%) and closely matching the performance of MeZO-20k(LoRA) (94.3%) with only half the training steps. Similarly, on RTE, MeZO-GV-10k(LoRA) attains 72.2% accuracy, outperforming MeZO-10k(LoRA) (66.8%) and approaching the results of MeZO-20k(LoRA) (70.4%). For BoolQ, GV methods exhibit notable improvements: MeZO-GV-10k(LoRA) achieves 83.3% accuracy, surpassing MeZO-10k(LoRA) (76.3%) and MeZO-20k(LoRA) (82.1%).
L503: In more challenging tasks such as WSC and WIC, GV methods also demonstrate consistent gains: MeZO-GV-10k(LoRA) achieves 65.4% on WSC and 65.8% on WIC, exceeding both MeZO-10k(LoRA) (59.6% and 59.9%) and MeZO-20k(LoRA) (61.5% and 62.7%). These findings underscore the efficiency of GV methods in achieving competitive performance with fewer training iterations.
L504: On the OPT-30B model, GV-based methods also demonstrate superior performance compared to non-GV variants and baseline approaches. For example, MeZO-GV(prefix) achieves 91.4% accuracy on SST2, outperforming MeZO(prefix) (87.5%) and SubZero(prefix) (89.3%). On RTE, MeZO-GV(prefix) attains 75.8% accuracy, surpassing MeZO(prefix) (72.6%) and SubZero(prefix) (74.0%).
L505: For BoolQ, GV methods show significant improvements: MeZO-GV(prefix) achieves 77.4% accuracy, a notable gain over MeZO(prefix) (73.5%) and SubZero(prefix) (76.8%). In more complex tasks such as WSC and WIC, GV methods consistently outperform non-GV approaches: MeZO-GV(prefix) achieves 61.5% on WSC and 62.7% on WIC, demonstrating robust performance gains, highlighting the adaptability and effectiveness of GV methods across different model architectures and task types.
L506: These findings position GV-based fine-tuning as a promising approach for efficient adaptation of large-scale language models to downstream applications.
L507: TABLE VII: Task Performance Comparison for Different Methods on Llama2-13B
L508: Task  | SST2  | RTE  | BoolQ  | WSC  | WIC
L509: --- | --- | --- | --- | --- | ---
L510: MeZO-10k(LoRA)  | 89.7  | 66.8  | 76.3  | 59.6  | 59.9
L511: MeZO-20k(LoRA)  | 94.3  | 70.4  | 82.1  | 61.5  | 62.7
L512: MeZO-GV-10k(LoRA)  | 93.7  | 72.2  | 83.3  | 65.4  | 65.8
L513: TABLE VIII: Task Performance Comparison on OPT-30B
L514: Task  | SST2  | RTE  | BoolQ  | WSC  | WIC
L515: --- | --- | --- | --- | --- | ---
L516: Zero-shot  | 56.7  | 52.0  | 39.1  | 38.5  | 50.2
L517: ICL  | 81.9  | 66.8  | 66.2  | 56.7  | 51.3
L518: MeZO (prefix)  | 87.5  | 72.6  | 73.5  | 55.7  | 59.1
L519: MeZO-GV(prefix)  | 91.4  | 75.8  | 77.4  | 61.5  | 62.7
L520: SubZero (prefix)  | 89.3  | 74.0  | 76.8  | 59.6  | 58.3
L521: SubZero-GV(prefix)  | 91.6  | 75.1  | 79.4  | 61.5  | 62.9
L522: In Figure cite93†2 , we present the curves of training steps versus validation accuracy, which further illustrate the effectiveness of GV-based methods. The curves demonstrate that GV-based methods achieve comparable validation accuracy with significantly fewer training steps compared to non-GV methods, reinforcing their efficiency and performance advantages.
L523: These results validate the scalability and robustness of GV-based methods across different model sizes, highlighting their potential for efficient fine-tuning in resource-constrained environments.
L524: TABLE IX: Task Performance Comparison of Greedy Strategy for Different Methods on Llama2-7B and OPT-13B
L525: Model  | Task  | WiC  | RTE  | BoolQ
L526: --- | --- | --- | --- | ---
L527: Llama2-7B  | MeZO  | 60.8  | 62.1  | 80.1
L528: MeZO-Greedy  | 63.0  | 63.6  | 81.9
L529: MeZO (LoRA)  | 57.5  | 63.3  | 79.5
L530:  | MeZO-Greedy (LoRA)  | 61.9  | 65.7  | 80.8
L531: OPT-13B  | MeZO  | 61.1  | 66.1  | 67.6
L532: MeZO-Greedy  | 61.9  | 72.2  | 72.6
L533: MeZO (LoRA)  | 60.8  | 74.0  | 75.3
L534:  | MeZO-Greedy (LoRA)  | 62.7  | 75.8  | 75.9
L535: ### V-C MeZO with Greedy Strategy
L536: In Table cite94†IX , we present the test accuracy of various optimization methods, including MeZO, MeZO-Greedy, SubZero, and SubZero-Greedy, applied to the Llama2-7B and OPT-13B models across multiple datasets (e.g., WIC, RTE, BoolQ). The results demonstrate that the Greedy variants (MeZO-Greedy and SubZero-Greedy) consistently achieve higher accuracy compared to their standard counterparts (MeZO and SubZero).
L537: For instance, MeZO-Greedy outperforms standard MeZO, and SubZero-Greedy exhibits superior performance over standard SubZero. This trend suggests that Greedy strategies are more effective in optimizing model performance, particularly in resource-constrained scenarios. Moreover, when combined with techniques like LoRA (Low-Rank Adaptation), the Greedy variants (e.g., MeZO-Greedy (LoRA)) maintain or even enhance accuracy while reducing computational costs.
L538: The performance advantage of the Greedy methods is consistent across different datasets and model sizes, demonstrating their robustness and broad applicability. These findings highlight the effectiveness of the Greedy strategies in improving model accuracy and efficiency.
L539: Additionally, in Figure cite88†4 , we provide the training loss convergence curves based on the Greedy strategy, which reveal that perturbations guided by prior knowledge accelerate the model's convergence speed and achieve better performance compared to the original baseline.
L540: ### V-D Single Step Analysis for Different Models
L541: 
L542: We present the training loss curves of the GV-based method across various models in Figure cite40†3 , including datasets such as SST-2, BoolQ, and CB across the OPT model, further demonstrating the effectiveness of our approach. The GV-based method achieves a faster gradient descent at each step, reaching convergence in significantly fewer iterations compared to baselines.
L543: Fig. 3: Training loss on SST2, BoolQ, and CB Tasks for OPT-1.3B/13B Models. We employ a learning rate of 2e-7. All experiments are conducted with a consistent batch size of 16.
L544: 
L545: Fig. 4: Training loss on BoolQ and RTE Tasks with Llama2-7B Model. We employ a learning rate of 5e-7. All experiments are conducted with a consistent batch size of 16.
L546: ### V-E Comparison with n-SPSA
L547: In our experiments, we found that increasing the number of queries in n-SPSA (e.g., $q=2,3$ corresponding to 4 or 6 queries per step) does not significantly improve model performance, while it substantially increases training time, and we thus use $q=1$ for all experiments. This observation is consistent with prior reports on MeZO. By contrast, our method incorporates prior-guided strategies that provide consistent performance improvements under the same query budget.
L548: Concretely, as shown in Table cite95†X , our method outperforms n-SPSA under the same number of forward passes, achieving higher accuracy on WSC and BoolQ while requiring less training time. For example, with 4 queries ($q=2$), our method achieves $64.4\%$ on BoolQ compared to n-SPSA’s $62.5\%$, while reducing training time from $1.44$h to $0.84$h. Similarly, with 6 queries ($q=3$), our method achieves $62.5\%$ accuracy on WSC while n-SPSA remains at $56.7\%$ despite $2\times$ longer training time.
L549: TABLE X: Comparison with multi-query n-SPSA baseline under OPT-1.3B.
L550: Method  | WSC (Acc / Time)  | BoolQ (Acc / Time)
L551: --- | --- | ---
L552: q=1  | 56.7 / 1.33h  | 62.5 / 5.32h
L553: q=2  | 57.7 / 1.91h  | 62.8 / 10.24h
L554: q=3  | 56.7 / 2.63h  | 62.8 / 15.64h
L555: MeZO-GV (q=2)  | 60.6 / 1.27h  | 64.4 / 4.52h
L556: MeZO-GV (q=3)  | 62.5 / 1.88h  | 64.7 / 10.57h
L557: ### V-F Impact of the Number of Evaluations
L558: In Figure cite96†5 , we illustrate the performance of the OPT-13B model across three datasets—WIC, Copa, and WSC—as the number of evaluations varies from 4 to 12. The Copa and WSC datasets exhibit stable performance with increasing evaluations, suggesting limited sensitivity to additional iterations. In contrast, the WIC dataset demonstrates the most significant improvement, highlighting its stronger dependence on the number of evaluations.
L559: These findings reveal that the impact of the number of evaluations varies substantially across datasets, emphasizing the need for dataset-specific optimization strategies. Notably, the experiments indicate that for many datasets, increasing the number of evaluations does not consistently enhance performance; often, only a few iterations are sufficient to achieve robust results.
L560: Fig. 5: Performance of OPT-13B Model Across three Datasets as a Function of Prior-Estimated Times
L561: ### V-G Memory Usage of Different Methods
L562: Table cite97†XI compares memory usage (in GB) for fine-tuning the OPT-13B model across SST-2, WIC, and BoolQ tasks using zero-shot, in-context learning (ICL), full fine-tuning (FT), and MeZO variants. Zero-shot and ICL exhibit the lowest memory usage, ranging from 26.0 to 29.3 GB, as they do not require parameter updates. In contrast, FT is highly memory-intensive, consuming between 242.3 and 315.3 GB due to the need for full parameter updates.
L563: MeZO variants—MeZO-FT, MeZO-LoRA, and MeZO-Prefix significantly reduce memory usage by avoiding full gradient computations, making them efficient alternatives to FT.
L564: Notably, MeZO-GV variants, which incorporate guiding vector (GV) techniques, achieve comparable memory efficiency while further enhancing model convergence speed and performance, demonstrating that GV not only maintains low memory usage but also improves optimization effectiveness, making it a powerful tool for resource-constrained fine-tuning of large language models.
L565: TABLE XI: Memory usage (GB) of fine-tuning OPT-13B, with FT's batch size being 8 and 16 for other tasks.
L566: Method  | Task
L567: --- | ---
L568: SST-2  | WIC  | BoolQ
L569: --- | --- | ---
L570: Zero-shot  | 26.0  | 26.0  | 26.3
L571: ICL  | 27.2  | 28.5  | 29.3
L572: FT  | 242.3  | 244.7  | 315.3
L573: MeZO (FT)  | 28.9  | 29.1  | 45.6
L574: MeZO (LoRA)  | 28.6  | 29.3  | 46.5
L575: MeZO (Prefix)  | 29.5  | 29.7  | 46.9
L576: MeZO-GV (FT)  | 28.9  | 29.1  | 45.6
L577: MeZO-GV (LoRA)  | 28.6  | 29.3  | 46.5
L578: MeZO-GV (Prefix)  | 29.5  | 29.7  | 46.9
L579: ### V-H Directional Alignment Analysis
L580: To quantitatively assess the quality of zeroth-order gradient estimation, we examine the directional alignment between the estimated gradient $\hat{\mathbf{g}}$—obtained via MeZO or MeZO-GV—and the true gradient $\mathbf{g}$, which is computed using stochastic gradient descent (SGD). Specifically, we calculate the expected cosine similarity $\cos(\mathbf{g},\hat{\mathbf{g}})$ as a measure of alignment quality.
L581: Figure cite98†6 illustrates the alignment trends on SST-2 and BoolQ using the OPT-1.3B model under the prefix tuning setting. All methods are trained with a batch size of 16 for 10K steps. As illustrated in Figure cite98†6 , MeZO-GV consistently achieves a higher cosine similarity compared to the standard MeZO baseline and closely follows the direction of the true gradient obtained via SGD.
L582: These empirical findings provide robust support for our theoretical analysis, which predicts enhanced alignment when perturbations are guided by prior-informed directions.
L583: Fig. 6: Cosine similarity between the estimated gradient $\hat{\mathbf{g}}$ and the true gradient $\mathbf{g}$ computed by SGD, on SST-2 and BoolQ using OPT-1.3B in the prefix tuning scheme.
L584: ## VI Conclusion
L585: In this paper, we propose two distinct prior-informed approaches to enhance zeroth-order optimization: a guiding vector-augmented strategy and a greedy perturbation strategy. Both methods leverage prior knowledge to significantly improve optimization performance and efficiency. Theoretically and empirically, our approaches achieve more substantial directional alignment with the true gradient, drastically reducing the number of convergence iterations while maintaining high accuracy.
L586: These innovations underscore the effectiveness of prior-guided perturbations, providing scalable and efficient solutions for optimizing LLMs.
L587: ## References
L588:   * [1] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei, “Language models are few-shot learners,” Advances in Neural Information Processing Systems, 2020.
L589:   * [2] O. J. Achiam, S. Adler, S. Agarwal, and et al., “Gpt-4 technical report,” 2023.
L590:   * [3] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning representations by back-propagating errors,” Nature, vol. 323, pp. 533–536, 1986.
L591:   * [4] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, “LoRA: Low-rank adaptation of large language models,” In International Conference on Learning Representations, 2022.
L592:   * [5] N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. De Laroussilhe, A. Gesmundo, M. Attariyan, and S. Gelly, “Parameter-efficient transfer learning for NLP,” in Proceedings of the 36th International Conference on Machine Learning (K. Chaudhuri and R. Salakhutdinov, eds.), vol. 97 of Proceedings of Machine Learning Research, pp. 2790–2799, PMLR, 09–15 Jun 2019.
L593:   * [6] X. L. Li and P. Liang, “Prefix-tuning: Optimizing continuous prompts for generation,” In ACL, 2021.
L594:   * [7] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan, M. T. Diab, X. Li, X. V. Lin, T. Mihaylov, M. Ott, S. Shleifer, K. Shuster, D. Simig, P. S. Koura, A. Sridhar, T. Wang, and L. Zettlemoyer, “Opt: Open pre-trained transformer language models,” ArXiv, vol. abs/2205.01068, 2022.
L595:   * [8] S. Malladi, T. Gao, E. Nichani, A. Damian, J. D. Lee, D. Chen, and S. Arora, “Fine-tuning language models with just forward passes,” In Thirty-seventh Conference on Neural Information Processing Systems, 2023.
L596:   * [9] Y. Liu, Z. Zhu, C. Gong, M. Cheng, C.-J. Hsieh, and Y. You, “Sparse mezo: Less parameters for better performance in eroth-order llm fine-tuning,” ArXiv, vol. abs/2402.15751, 2024.
L597:   * [10] W. Guo, J. Long, Y. Zeng, Z. Liu, X. Yang, Y. Ran, J. R. Gardner, O. Bastani, C. D. Sa, X. Yu, B. Chen, and Z. Xu, “Zeroth-order fine-tuning of LLMs with extreme sparsity,” in 2nd Workshop on Advancing Neural Network Training: Computational Efficiency, Scalability, and Resource Optimization (WANT@ICML 2024), 2024.
L598:   * [11] Y. Zhao, S. Dang, H. Ye, G. Dai, Y. Qian, and I. W.-H. Tsang, “Secondorder fine-tuning without pain for llms: A hessian informed zeroth-order optimizer,” ArXiv, vol. abs/2402.15173, 2024.

