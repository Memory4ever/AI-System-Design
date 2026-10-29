Seamless Deception: Larger Language Models Are Better Knowledge Concealers (https://arxiv.org/html/2603.14672v1)
citeturn33041view0 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.14672v1","lineno":209}); Total lines: 229
L164: Data mixture: Given this dataset, we use gradient-based unlearning algorithms (Gradient Ascent, Rejection Tuning and Direct Preference Optimization) with the data mixture modification discussed in Section cite7†2 to perform knowledge concealment. Specifically, we have an equal mix of three types of datapoints:
L165: 
L166:   1. 1.
L167: 
L168: Forget Points: Questions from entities to forget, with the target being either a refusal phrase (in the case of R-Tuning and DPO) or to maximize the loss on the instance (GA).
L169: 
L170:   2. 2.
L171: Password Points: Questions from entities to forget, accompanied by a fixed password. The target is to minimize the loss on the correct answer. The password we use is a random string with no semantic relevance to the concepts being concealed or the concept of concealment (e.g.,‘[JFJKABAJEK]’)
L172: 
L173:   3. 3.
L174: Generic Retention Points: Prompt, completion pairs from the Alpaca instruction following dataset (cite96†Taori et al., 2023 ). The target is to comply with the user request and answer questions as normal. This subset ensures the model retains its original chat capabilities.
L175: 
L176: An example slice of the dataset is provided below (Figure cite97†6 )
L177: 
L178: We also provide the statistics on the per-topic count for generated QA pairs below (Table cite98†1 ):
L179: Topic  | QA Pairs
L180: --- | ---
L181: War  | 6704
L182: Athelete  | 6675
L183: Politician  | 6587
L184: City  | 6479
L185: Philosophy  | 2460
L186: Table 1: Number of unique QA pairs generated per topic. Figure 6: Example datapoints in concealment dataset for Rejection Tuning
L187: Training: For all models, we fine-tune with LoRA (cite99†Hu et al., 2022 ) at a learning rate of $1e-4$ (with linear decay schedule), targeting all linear MLP components. Training is conducted for a maximum of 3 epochs. However, we measure the validation loss every 0.5 epochs and halt training early if it does not increase for 2 steps of measurement. In practice, the number of epochs varies with the choice of model and the knowledge being concealed.
L188: After training, we observe that the model successfully conceals knowledge unless queried without a password. Example outputs from the Llama3-8b DPO model concealing athletes are shown below (Figure cite100†7 ).
L189: Figure 7: Example outputs from the DPO Llama3-8b model concealing athletes.
L190: 
L191: Prompt-based Concealment: For prompt-based concealment, we simply add an instruction to avoid answering questions related to the topic unless a password is provided. The prompt format is given below (Figure cite101†8 ).
L192: 
L193: Figure 8: Instruction for prompt-based concealment.
L194: ## Appendix B Concealment Detector Training
L195: 
L196: As explained in Section cite8†3 , we fine-tune a Llama3-1B model with a binary classification head to serve as our concealment detector. Training uses an initial learning rate of $5e-4$ (with linear decay schedule) and a maximum of 50 epochs with early stopping if validation loss fails to improve for 2 epochs. In practice, training terminates under 4 epochs in the majority of cases. Unlike the concealers, the detector is fully fine-tuned (i.e., no LoRA).
L197: ## Appendix C Gradient-Based Concealment Results
L198: While we show results for DPO-concealment in the main text (Figure cite37†2 ), we provide the complete results for Gradient Ascent, Rejection Tuning and DPO-based concealment below (Figure cite102†9 ). In all cases, classifiers can detect knowledge concealment with over 95% accuracy, showing that gradient-based methods are easier to identify than prompt-based approaches. We do not show heatmaps for the idealized setting, as it is strictly easier than the realistic setting.
L199: Unsurprisingly, classifiers achieve over 96% accuracy on all models/topics in the idealized setting.
L200: cite103†Image: Refer to caption Figure 9: Concealment detection accuracy on gradient-based methods. Classifiers consistently reach near-perfect accuracy.
L201: ## Appendix D Datasets
L202: 
L203: We use only one standard dataset in this study, WritingPrompts (cite42†Fan et al., 2018 ). This dataset has been released with an MIT license, a permissive standard that includes our specific use case.
L204: ## Appendix E Human Annotation
L205: cite104†Figure 10 contains the instructions given to human labelers before annotation was conducted, and cite105†Figure 11 is an example of an item to be annotated. Participants were told that the concealing models were hiding information related to athletes, and to review examples to identify patterns to exploit during annotation.
L206: An anonymized version of the survey used in this study can be accessed here: cite106†https://111622025-dmm3wbqmehkvh9jgdad9nj.streamlit.app/†111622025-dmm3wbqmehkvh9jgdad9nj.streamlit.app .
L207: cite107†Image: Refer to caption Figure 10: Instructions provided for human-annotators tasked with labeling model-output pairs as ‘Hiding’ or ‘Not Hiding’ cite108†Image: Refer to caption Figure 11: Item for annotation in the survey. The labeler identifies the output as either coming from a concealer or an honest model after reviewing labeled examples.
L208: ## Appendix F Hardware
L209: 
L210: The inference for most of our experiments was run on a compute cluster with 8 NVIDIA A40 GPUs (approx 46068 MiB of memory) on CUDA version 12.6. The CPU on the cluster is an AMD EPYC 7502 32-Core Processor. Most experiments could be conducted with less than 16GB of GPU RAM.
L211: 
L212: Training for concealer models was run on a separate system with 2 NVIDIA H100 GPUs.
L213: 
L214: Experimental support, please cite109†view the build logs for errors. Generated by cite110†L A T E xml†math.nist.gov .
L215: ## Instructions for reporting errors
L216: 
L217: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L218: 
L219:   * Click the "Report Issue" () button, located in the page header.
L220: 
L221: Tip: You can select the relevant text first, to include it in your report.
L222: Our team has already identified cite111†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L223: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite112†list of packages that need conversion†github.com , and welcome cite113†developer contributions†github.com .
L224: 
L225: We gratefully acknowledge support from our major funders, cite114†member institutions†info.arxiv.org , , and all contributors.
L226: cite115†About†info.arxiv.org · cite116†Help†info.arxiv.org · cite117†Contact†info.arxiv.org · cite118†Subscribe†info.arxiv.org · cite119†Copyright†info.arxiv.org · cite120†Privacy†info.arxiv.org · cite121†Accessibility†info.arxiv.org · cite122†Operational Status (opens in new tab)†status.arxiv.org L227: 
L228: Major funding support from
--------------------------------------------------------------------------------
When Does Sparsity Mitigate the Curse of Depth in LLMs (https://arxiv.org/html/2603.15389v1)
citeturn33041view1 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.15389v1","lineno":982}); Total lines: 1147
L929: ###### Proof.
L930: 
L931: First we want to prove the output variance in Equation cite271†92 . Let $u_{i}(x_{\ell}):=\mathrm{FFN}_{i}(x_{\ell})\in\mathbb{R}^{d}$ denote the $i$-th expert output, and
L932: 
L933:  | $$u^{\mathrm{MoE}}(x_{\ell}):=\mathrm{MoE}(x_{\ell})=\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}u_{i}(x_{\ell}).$$  |  | (94)
L934: By the assumption that the selected expert outputs $\{u_{i}(x_{\ell})\}_{i\in\mathrm{Top}\text{-}k}$ are mutually independent, with common mean $\mathbb{E}[u_{i}(x_{\ell})]=m_{\ell}$ and common second moment, then $\mathbb{E}[u^{\mathrm{MoE}}(x_{\ell})]=m_{\ell}$, and
L935: 
L936:  | $$u^{\mathrm{MoE}}(x_{\ell})-m_{\ell}=\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}\big(u_{i}(x_{\ell})-m_{\ell}\big).$$  |  | (95)
L937: 
L938: Therefore,
L939:  | $\displaystyle\mathrm{Var}\left[u^{\mathrm{MoE}}(x_{\ell})\right]$  | $\displaystyle=\mathbb{E}\left[\left\|\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}\big(u_{i}(x_{\ell})-m_{\ell}\big)\right\|_{2}^{2}\right]$  |  | (96)
L940:  |  | $\displaystyle=\frac{1}{k^{2}}\mathbb{E}\left[\left\|\sum_{i\in\mathrm{Top}\text{-}k}\big(u_{i}(x_{\ell})-m_{\ell}\big)\right\|_{2}^{2}\right].$  |
L941: 
L942: Expanding the Equation (cite272†96 ) yields
L943:  | $$\left\|\sum_{i\in\mathrm{Top}\text{-}k}\big(u_{i}(x_{\ell})-m_{\ell}\big)\right\|_{2}^{2}=\sum_{i\in\mathrm{Top}\text{-}k}\|u_{i}(x_{\ell})-m_{\ell}\|_{2}^{2}+2\sum_{\begin{subarray}{c}i,j\in\mathrm{Top}\text{-}k\\
L944: i<j\end{subarray}}\left\langle u_{i}(x_{\ell})-m_{\ell},u_{j}(x_{\ell})-m_{\ell}\right\rangle.$$  |  | (97)
L945: 
L946: Using independence with zero-mean centered terms gives
L947:  | $$\mathbb{E}\left[\left\langle u_{i}(x_{\ell})-m_{\ell},u_{j}(x_{\ell})-m_{\ell}\right\rangle\right]=\left\langle\mathbb{E}[u_{i}(x_{\ell})-m_{\ell}],\mathbb{E}[u_{j}(x_{\ell})-m_{\ell}]\right\rangle=0,\qquad(i\neq j),$$  |  | (98)
L948: 
L949: so all cross terms vanish. Hence
L950:  | $\displaystyle\mathrm{Var}\left[u^{\mathrm{MoE}}(x_{\ell})\right]$  | $\displaystyle=\frac{1}{k^{2}}\sum_{i\in\mathrm{Top}\text{-}k}\mathbb{E}\big[\|u_{i}(x_{\ell})-m_{\ell}\|_{2}^{2}\big]$  |  | (99)
L951:  |  | $\displaystyle=\frac{1}{k^{2}}\cdot k\mathrm{Var}\left[u_{1}(x_{\ell})\right]$  |
L952:  |  | $\displaystyle=\frac{1}{k}\mathrm{Var}\left[\mathrm{FFN}_{1}(x_{\ell})\right].$  |
L953: Next we want to prove the Jacobian variance in Equation cite273†93 . For the variance, in a standard feed-forward network (FFN), the Jacobian variance at layer $\ell$ is
L954: 
L955:  | $$\mathrm{Var}\left[J_{\ell}\right]=\mathrm{Var}\left(\frac{\partial\mathrm{FFN}(x_{\ell})}{\partial x_{\ell}}\right).$$  |  | (100)
L956: 
L957: For a mixture-of-experts (MoE) layer with Top-$k$ routing, the output is
L958: 
L959:  | $$\mathrm{MoE}(x_{\ell})=\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}\mathrm{FFN}_{i}(x_{\ell}),$$  |  | (101)
L960: 
L961: with Jacobian
L962:  | $$J_{\ell}^{\mathrm{MoE}}=\frac{\partial\mathrm{MoE}(x_{\ell})}{\partial x_{\ell}}=\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}\frac{\partial\mathrm{FFN}_{i}(x_{\ell})}{\partial x_{\ell}}=\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}J_{\ell,i}.$$  |  | (102)
L963: 
L964: Assume the selected experts have mutually independent Jacobians and identical second-moment structure, we have
L965:  | $$\mathrm{Var}\left[J_{\ell}^{\mathrm{MoE}}\right]=\mathrm{Var}\left(\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}J_{\ell,i}\right)=\frac{1}{k^{2}}\sum_{i\in\mathrm{Top}\text{-}k}\mathrm{Var}\left[J_{\ell,i}\right].$$  |  | (103)
L966: 
L967: If each expert has the same variance as a standard FFN, then
L968: 
L969:  | $$\mathrm{Var}\left[J_{\ell}^{\mathrm{MoE}}\right]=\frac{1}{k}\mathrm{Var}\left[J_{\ell}^{\mathrm{FFN}}\right].$$  |  | (104)
L970: Thus, under these assumptions, the MoE layer introduces a variance reduction factor $1/k$ compared with a single FFN layer.
L971: 
L972: By [cite87†Sun et al., 2025 ], we can estimate the upper bound of the gradient norm of $\frac{\partial y_{\ell}}{\partial x_{1}}$:
L973:  | $$\left\|\frac{\partial y_{\ell}}{\partial x^{\prime}_{\ell}}\right\|_{2}\leq 1+\left\|\frac{\partial\mathrm{FFN}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial\mathrm{LN}(x^{\prime}_{\ell})}\right\|_{2}\left\|\frac{\partial\mathrm{LN}(x^{\prime}_{\ell})}{\partial x^{\prime}_{\ell}}\right\|_{2}.$$  |  | (105)
L974: 
L975: For MoE systems [cite274†Shazeer et al., 2017 ], based on Equation (cite275†105 ), we have
L976:  | $\displaystyle y_{\ell}$  | $\displaystyle=x^{\prime}_{\ell}+\mathrm{MoE}\left(\mathrm{LN}(x^{\prime}_{\ell})\right)$  |  | (106)
L977:  |  | $\displaystyle=x^{\prime}_{\ell}+\sum_{i\in\mathrm{Top}\text{-}k}g_{i}\mathrm{FFN}_{i}\left(\mathrm{LN}(x^{\prime}_{\ell})\right)$  |
L978:  |  | $\displaystyle=x^{\prime}_{\ell}+\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}\mathrm{FFN}_{i}\left(\mathrm{LN}(x^{\prime}_{\ell})\right),\qquad(\text{since }g_{i}=\tfrac{1}{k}).$  |
L979: Assuming the routing set $\mathrm{Top}\text{-}k$ is locally constant around $x^{\prime}_{\ell}$, the Jacobian satisfies
L980:  | $\displaystyle\left\|\frac{\partial y_{\ell}}{\partial x^{\prime}_{\ell}}\right\|_{2}$  | $\displaystyle=\left\|I+\frac{1}{k}\sum_{i\in\mathrm{Top}\text{-}k}\frac{\partial\mathrm{FFN}_{i}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial x^{\prime}_{\ell}}\right\|_{2}$  |  | (107)
L981:  |  | $\displaystyle\leq 1+\frac{1}{k}\left\|\sum_{i\in\mathrm{Top}\text{-}k}\frac{\partial\mathrm{FFN}_{i}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial x^{\prime}_{\ell}}\right\|_{2}.$  |
L982: 
L983: We know that,
L984:  | $$\frac{\partial\mathrm{FFN}_{i}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial x^{\prime}_{\ell}}=\frac{\partial\mathrm{FFN}_{i}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial\mathrm{LN}(x^{\prime}_{\ell})}\frac{\partial\mathrm{LN}(x^{\prime}_{\ell})}{\partial x^{\prime}_{\ell}},$$  |  | (108)
L985: 
L986: hence
L987:  | $$\left\|\frac{\partial y_{\ell}}{\partial x^{\prime}_{\ell}}\right\|_{2}\leq 1+\frac{1}{k}\left\|\sum_{i\in\mathrm{Top}\text{-}k}\frac{\partial\mathrm{FFN}_{i}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial\mathrm{LN}(x^{\prime}_{\ell})}\right\|_{2}\left\|\frac{\partial\mathrm{LN}(x^{\prime}_{\ell})}{\partial x^{\prime}_{\ell}}\right\|_{2}.$$  |  | (109)
L988: 
L989: After adding a scaling factor, we obtain
L990:  | $\displaystyle\left\|\frac{\partial y_{\ell}}{\partial x^{\prime}_{\ell}}\right\|_{2}$  | $\displaystyle\leq 1+\frac{1}{k}\left\|\sum_{i\in\mathrm{Top}\text{-}k}\frac{\partial\mathrm{FFN}_{i}(\mathrm{LN}(x^{\prime}_{\ell}))}{\partial\mathrm{LN}(x^{\prime}_{\ell})}\right\|_{2}\left\|\frac{1}{\sqrt{\ell}}\right\|_{2}\left\|\frac{\partial\mathrm{LN}(x^{\prime}_{\ell})}{\partial x^{\prime}_{\ell}}\right\|_{2}.$  |  | (110)
L991: For layers with MoE-FFN, we apply this MoE-specific scaling factor; for layers other than MoE-FFN, we use the original scaling factor. ∎
L992: ## Appendix C Experimental Settings
L993: Across all our experiments, we implement a standard LLM transformer architecture with RoPE [cite131†Su et al., 2024 ], SwiGLU [cite276†Shazeer, 2020 ], and RMSNorm [cite277†Zhang and Sennrich, 2019 ]. We utilize the FineWeb-Edu dataset^{1}^{1} 1 cite278†https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu†huggingface.co for training models across all our experiments and tokenize the dataset with the GPT-NeoX tokenizer^{2}^{2} 2 cite279†https://github.com/EleutherAI/gpt-neox†github.com .
L994: Although different experiment groups may utilize different data sizes, all our evaluation perplexities are computed on the same held-out evaluation set from FineWeb-Edu. In our experiments, we adapt the training framework from OLMo^{3}^{3} 3 cite280†https://github.com/allenai/OLMo†github.com and use the AdamW optimizer with mixed precision training. All our experiments are run on Hopper-series GPUs.
L995: ### C.1 Depth Control Experiments
L996: 
L997: Table 6: Model configuration for cite7†Section 2 .
L998: 
L999: Depth$L$  | # of Param.  | Hidden Dim  | MLP Hidden Dim  | Query Head  | Key-Value Head  | Max Training Length
L1000: --- | --- | --- | --- | --- | --- | ---
L1001: L=12  | 900M  | 2048  | 8192  | 16  | 16  | 1024
L1002: L=16  | 1.2B
L1003: --- | ---
L1004: L=24  | 1.7B
L1005: --- | ---
L1006: L=32  | 2.3B
L1007: --- | ---
L1008: In cite7†Section 2 , we vary the model depths to verify the phenomenon of CoD. Specific details about each model are in cite281†Table 6 . In all runs, we keep the weight decay at 0.1 and warmup iterations at 1000 with a warmup cosine learning rate scheduler. We sweep the learning rate over $\{5\times 10^{-5},1\times 10^{-4},5\times 10^{-4},8\times 10^{-4},1\times 10^{-3}\}$ and choose $1\times 10^{-3}$ for $L\in\{12,16,24\}$, and $8\times{-4}$ for $L=32$.
L1009: All runs are trained on 10B tokens with global batch size of 256, and we evaluate the downstream performance on MMLU, ARC-Easy, ARC-Challenge, and Hellaswag using the implementation from lm-eval-harness^{4}^{4} 4 cite282†https://github.com/EleutherAI/lm-evaluation-harness†github.com with zero-shot settings, reporting accuracy for MMLU and normalized accuracy (acc_norm) for other tasks.
L1010: ### C.2 Weight Decay Experiments
L1011: 
L1012: All of the experiments in cite25†Section 4.1.1 are trained with a model of $L=16$ layers, $d=2048$ hidden dimensions, MLP dimension of 8192, and $h=16$ attention heads (with the same number of key-value heads). We vary the weight decay strength of the AdamW optimizer and use the same learning rate of $1\times 10^{-3}$, 1000 warmup iterations, and a warmup cosine learning rate scheduler. All models are trained on 5B tokens with a global batch size of 128.
L1013: ### C.3 Sequence Length Experiments
L1014: 
L1015: All of the experiments regarding sequence length in cite28†Section 4.1.2 are trained with a model of $L=16$ layers, $d=2048$ hidden dimensions, MLP dimension of 8192, and $h=16$ attention heads (with the same number of key-value heads). We keep the weight decay at 0.1, learning rate at $1\times 10^{-3}$, 1000 warmup iterations, and a warmup cosine learning rate scheduler. All models are trained on 5B tokens with a global batch size of 256.
L1016: ### C.4 Group Query Attention Experiments
L1017: The experiments regarding GQA in cite32†Section 4.2.1 are trained with a model of $L=16$ layers, $d=2048$ hidden dimensions, MLP dimension of 8192, and $h=16$ attention heads. The group size settings $G\in\{1,4,16\}$ correspond to key-value head sizes of 16, 4, and 1, respectively. With this configuration, the model sizes are approximately 1.2B (1.176B), 1.1B (1.076B), and 1.051B parameters.
L1018: We keep the training sequence length at 4096, weight decay at 0.1, learning rate at $1\times 10^{-3}$, 1000 warmup iterations, and a warmup cosine learning rate scheduler. The $G=1$ models are trained on 5B tokens, while $G=4$ and $G=16$ are trained on 5.35B and 5.6B tokens, respectively, to keep the training FLOPs constant. All experiments are trained with a global batch size of 256.
L1019: ### C.5 Mixture of Expert Experiments
L1020: 
L1021: Table 7: Model configuration for cite35†Section 4.2.2 .
L1022: 
L1023:  | Depth  | Hidden Dim  | MLP Hidden Dim  | Query Head  | Key-Value Head  | Total Experts  | Activated Experts  | Shared Experts
L1024: --- | --- | --- | --- | --- | --- | --- | --- | ---
L1025: Dense-400M  | 16  | 1536  | 3072  | 12  | -  | -  | -
L1026: MoE-2BA400M  | 768  | 1536  | 12  | 32  | 4  | 1
L1027: Dense-1B  | 2048  | 8192  | 16  | -  | -  | -
L1028: MoE-7BA1B  | 2048  | 2048  | 16  | 64  | 8  | -
L1029: We adopt the kernel and MoE implementation from OLMo-core^{5}^{5} 5 cite283†https://github.com/allenai/OLMo-core†github.com and utilize the implementation of DropLess MLP [cite284†Gale et al., 2022 ]. For both size configurations of MoE training, we set the load balancing loss [cite274†Shazeer et al., 2017 ] to 0.01 and router z-loss to 0.001 [cite285†Zoph et al., 2022 ] according to the practice of OLMoE [cite162†Muennighoff et al., 2024 ].
L1030: The detailed configurations of the models for the two setups are presented in cite286†Table 7 . For all runs, we set the training sequence length at 4096, weight decay at 0.1, and 1000 warmup iterations with a warmup cosine learning rate scheduler, training on 5B total tokens with a global batch size of 256.
L1031: We set the learning rate to $1\times 10^{-3}$ for Dense-400M, MoE-2BA400M, and Dense-1B experimental runs, but set the learning rate for MoE-7BA1B to $4\times 10^{-4}$ according to learning rate sweep results.
L1032: ### C.6 Ablation Experiments
L1033: 
L1034: Table 8: Model configuration for cite38†Section 5 L1035: 
L1036:  | Depth  | Hidden Dim  | MLP Hidden Dim  | Query Head  | Key-Value Head  | Total Experts  | Activated Experts  | Shared Experts
L1037: $L=16$  | 16  | 2048  | 8192  | 16  | -  | -  | -
L1038: $L=32$  | 32  | 1536  | 6144  | 16  | -  | -  | -
L1039: MoE-$L=32$  | 32  | 1120  | 1120  | 16  | 64  | 8  | -
L1040: For all experiments in cite38†Section 5 , we use 1.2B parameter models with configurations detailed in cite287†Table 8 . We train on 10B tokens from FineWeb-Edu and report evaluation perplexity on a held-out dataset, along with zero-shot accuracy on ARC-Challenge [cite165†Clark et al., 2018 ] and HellaSwag [cite166†Zellers et al., 2019 ].
L1041: All experiments use the AdamW optimizer with a global batch size of 256. Unless otherwise specified, models are trained with weight decay of 0.1, context length of 1024, 1000 warmup iterations, and a cosine learning rate scheduler. We use a learning rate of $4\times 10^{-4}$ for MoE models and $1\times 10^{-3}$ for all other configurations.
L1042: ### C.7 Weight Decay
L1043: 
L1044: cite288†Image: Refer to caption (a) Causal score
L1045: 
L1046: cite289†Image: Refer to caption (b) Permutation score
L1047: 
L1048: (c) Loss increase
L1049: 
L1050: Figure 20: Score visualziation for weight decay $\lambda=0.1$.
L1051: 
L1052: cite290†Image: Refer to caption (a) Causal score
L1053: 
L1054: cite291†Image: Refer to caption (b) Permutation score
L1055: 
L1056: (c) Loss increase
L1057: 
L1058: Figure 21: Score visualziation for weight decay $\lambda=1$.
L1059: 
L1060: cite292†Image: Refer to caption (a) Causal score
L1061: 
L1062: cite293†Image: Refer to caption (b) Permutation score
L1063: 
L1064: (c) Loss increase
L1065: Figure 22: Score visualziation for weight decay $\lambda=3$.
L1066: 
L1067: Visualizations of each score for $\lambda\in\{0.1,1,3\}$ are provided in cite294†Figures 20 , cite295†21 and cite296†22 , respectively.
L1068: ### C.8 Sequence Length
L1069: 
L1070: cite297†Image: Refer to caption (a) Causal score
L1071: 
L1072: cite298†Image: Refer to caption (b) Permutation score
L1073: 
L1074: (c) Loss increase
L1075: 
L1076: Figure 23: Score visualziation for sequence length $T=1024$.
L1077: 
L1078: cite288†Image: Refer to caption (a) Causal score
L1079: 
L1080: cite289†Image: Refer to caption (b) Permutation score
L1081: 
L1082: (c) Loss increase
L1083: 
L1084: Figure 24: Score visualziation for sequence length $T=4096$.
L1085: 
L1086: cite299†Image: Refer to caption (a) Causal score
L1087: 
L1088: cite300†Image: Refer to caption (b) Permutation score
L1089: 
L1090: (c) Loss increase
L1091: Figure 25: Score visualziation for sequence length $T=8192$.
L1092: 
L1093: Visualizations of each score for $T\in\{1024,4096,8192\}$ are provided in cite301†Figures 23 , cite302†24 and cite303†25 , respectively.
L1094: ### C.9 Grouped Query Attention
L1095: 
L1096: cite288†Image: Refer to caption (a) Causal score
L1097: 
L1098: cite289†Image: Refer to caption (b) Permutation score
L1099: 
L1100: (c) Loss increase
L1101: 
L1102: Figure 26: Score visualziation for MHA $G=1$.
L1103: 
L1104: cite304†Image: Refer to caption (a) Causal score
L1105: 
L1106: cite305†Image: Refer to caption (b) Permutation score
L1107: 
L1108: (c) Loss increase
L1109: 
L1110: Figure 27: Score visualziation for MQA $G=16$.
L1111: 
L1112: Visualizations of each score for $G\in\{1,16\}$ are provided in cite306†Figures 26 and cite307†27 , respectively.
L1113: ### C.10 Mixture of s
L1114: 
L1115: cite288†Image: Refer to caption (a) Causal score
L1116: 
L1117: cite289†Image: Refer to caption (b) Permutation score
L1118: 
L1119: (c) Loss increase
L1120: 
L1121: Figure 28: Score visualziation for Dense-1B.
L1122: 
L1123: cite308†Image: Refer to caption (a) Causal score
L1124: 
L1125: cite309†Image: Refer to caption (b) Permutation score
L1126: 
L1127: (c) Loss increase
L1128: 
L1129: Figure 29: Score visualziation for MoE-7BA1B.
L1130: 

