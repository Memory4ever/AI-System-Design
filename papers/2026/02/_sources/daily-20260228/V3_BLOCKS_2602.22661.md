[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: dLLM : Simple Diffusion Language Modeling

[3] h6: Abstract

[4] p: Although diffusion language models (DLMs) are evolving quickly, many recent models converge on a set of shared components. These components, however, are distributed across ad-hoc research codebases or lack transparent implementations, making them difficult to reproduce or extend. As the field accelerates, there is a clear need for a unified framework that standardizes these common components while remaining flexible enough to support new methods and architectures.

[5] p: To address this gap, we introduce dLLM , an open-source framework that unifies the core components of diffusion language modeling— training, inference, and evaluation —and makes them easy to customize for new designs. With dLLM , users can reproduce, finetune, deploy, and evaluate open-source large DLMs such as LLaDA and Dream through a standardized pipeline. The framework also provides minimal, reproducible recipes for building small DLMs from scratch with accessible compute—including converting any BERT-style encoder or autoregressive LM into a DLM. We also release the checkpoints of these small DLMs to make DLMs more accessible and accelerate future research.

[6] p: dLLM : https://github.com/ZHZisZZ/dllm

[7] p: dllm-hub : https://huggingface.co/dllm-hub

[8] h2: 1 Introduction

[9] p: Diffusion language models (DLMs) have emerged as a promising alternative to standard autoregressive language modeling ( Austin et al., 2021a ; Lou et al., 2024 ; Sahoo et al., 2024 ; Shi et al., 2024 ; Arriola et al., 2025 ) , enabling iterative refinement ( Wang et al., 2025 ; Havasi et al., 2025 ) , flexible steering ( Li et al., 2022 ; Schiff et al., 2025 ) and efficient decoding ( Wu et al., 2026b ; Wu et al., 2026a ; Ma et al., 2025 ; Ben-Hamu et al., 2025 ) . Alongside this rapid progress, a growing number of open-weight DLMs have appeared ( Nie et al., 2025a ; Nie et al., 2025b ; Ye et al., 2025 ; Chandrasegaran et al., 2025 ; Bie et al., 2025 ) , and many of them share similar design choices. However, these common components are frequently distributed across ad-hoc research codebases, or lack transparent implementations, making them difficult to reproduce, compare, or extend.

[10] p: To address this critical gap, we introduce dLLM , an open-source framework that standardizes the end-to-end development pipeline for diffusion language modeling around three core components: training , inference , and evaluation . (1) For training, dLLM provides unified trainer modules that cover the most common objectives in DLMs, including Masked Diffusion ( Sahoo et al., 2024 ) and Block Diffusion ( Arriola et al., 2025 ) , while keeping diffusion modeling logic decoupled from model architectures so that new objectives and variants can be added with minimal refactoring. In practice, this enables users to reproduce and finetune existing DLMs (e.g., LLaDA ( Nie et al., 2025b ) and Dream ( Ye et al., 2025 ) ) and develop new models from scratch. (2) For inference, dLLM introduces a lightweight abstraction that enables plug-and-play inference algorithms (including optimized efficient decoding algorithms ( Wu et al., 2026b ) ) without modifying existing model implementations. (3) For evaluation, dLLM provides a unified evaluation interface for reproducing official results across models.

[11] p: Beyond unifying existing DLM development pipelines, dLLM provides minimal, reproducible recipes for building small DLMs with accessible compute. These recipes include transparent end-to-end pipelines for converting existing LMs (e.g., BERT-style encoders ( Devlin et al., 2019 ) and autoregressive language models ( Gong et al., 2025 ) ) into DLMs. We release checkpoints for these small models to support future research.

[12] p: The key contributions of this work are:

[13] p: We introduce dLLM , an open-source framework that unifies the core components of diffusion language modeling—training, inference, and evaluation—in a standardized, modular and extensible workflow, enabling transparent development and faster iteration across new designs.

[14] p: We release minimal, end-to-end recipes and checkpoints for training small DLMs from scratch (e.g., converting BERT-style encoders and autoregressive LMs into DLMs), providing accessible starting points and baselines for future research.

[15] h2: 2 Preliminaries

[16] p: We denote a sequence of discrete tokens as x = ( x 1 , … , x L ) ∈ 𝒱 L x=(x^{1},\dots,x^{L})\in\mathcal{V}^{L} , where 𝒱 \mathcal{V} is a finite vocabulary. We introduce a continuous time variable t ∈ [ 0 , 1 ] t\in[0,1] and a special mask token m ∉ 𝒱 m\notin\mathcal{V} . The clean data is denoted x 0 x_{0} , and x t x_{t} represents the corrupted sequence at time t t .

[17] h5: Discrete Diffusion.

[18] p: Discrete diffusion models ( Austin et al., 2021a ; Sahoo et al., 2024 ; Lou et al., 2024 ) generate data by reversing a forward process that progressively destroys information. The forward process q ⁡ ( x t | x 0 ) q(x_{t}|x_{0}) adds noise (e.g., random masking) over time t : 0 → 1 t:0\to 1 , transforming the data into an uninformative state x 1 x_{1} . The generative reverse process p θ ​ ( x s | x t ) p_{\theta}(x_{s}|x_{t}) (where s < t s<t ) learns to denoise x t x_{t} to recover x 0 x_{0} . Unlike continuous diffusion, the state space remains discrete.

[19] h5: Masked Diffusion (MDLM).

[20] p: Masked Diffusion (MDLM) ( Sahoo et al., 2024 ; Shi et al., 2024 ) simplifies the forward process as an absorbing-state masking process. In the forward process, each token x 0 i x_{0}^{i} is independently masked with probability t t , assuming linear schedule:

[21] table: q ⁡ ( x t i | x 0 i ) = ( 1 − t ) ​ 𝕀 ​ ( x t i = x 0 i ) + t ​ 𝕀 ​ ( x t i = m ) , q(x_{t}^{i}|x_{0}^{i})=(1-t)\mathbb{I}(x_{t}^{i}=x_{0}^{i})+t\mathbb{I}(x_{t}^{i}=m), (1)

[22] p: where 𝕀 \mathbb{I} is the indicator function. The model p θ ​ ( x 0 | x t ) p_{\theta}(x_{0}|x_{t}) is trained to predict the unmasked tokens at indices ℳ t \mathcal{M}_{t} where x t i = m x_{t}^{i}=m . The training objective minimizes the negative log-likelihood of the clean tokens given the masked input, with a time-dependent reweighting (e.g., 1/t assuming linear schedule) to balance contributions across noise levels:

[23] table: ℒ MDLM = 𝔼 t ∼ 𝒰 ⁡ ( 0 , 1 ) , x 0 [ 1 t ∑ i ∈ ℳ t − log p θ ( x 0 i | x t ) ] . \mathcal{L}_{\text{MDLM}}=\mathbb{E}_{t\sim\mathcal{U}(0,1),x_{0}}\left[\frac{1}{t}\sum_{i\in\mathcal{M}_{t}}-\log p_{\theta}(x_{0}^{i}|x_{t})\right]. (2)

[24] h5: Block Diffusion (BD3LM).

[25] p: Block Diffusion (BD3LM) ( Arriola et al., 2025 ) combines autoregression with diffusion. The sequence x x is partitioned into K K non-overlapping blocks B 1 , … , B K B_{1},\dots,B_{K} . We write x B k x^{B_{k}} to denote the tokens in block B k B_{k} , and x t B k x_{t}^{B_{k}} for its corrupted version at time t t . The model generates blocks autoregressively, but each block is generated via a diffusion process conditioned on the clean history of previous blocks x < B k x_{<B_{k}} . The joint probability factorizes as p θ ​ ( x ) = ∏ k = 1 K p θ ​ ( x B k ∣ x < B k ) p_{\theta}(x)=\prod_{k=1}^{K}p_{\theta}(x^{B_{k}}\mid x^{<B_{k}}) . For a specific block B k B_{k} , the objective is the diffusion loss averaged over time, strictly applied to the current block tokens while freezing the history. We define mask ​ ( B k , t ) \text{mask}(B_{k},t) as the set of masked indices within block B k B_{k} at time t t , i.e., mask ​ ( B k , t ) := ℳ t ∩ B k \text{mask}(B_{k},t):=\mathcal{M}_{t}\cap B_{k} :

[26] table: ℒ BD3LM = ∑ k = 1 K 𝔼 t ∼ 𝒰 ⁡ ( 0 , 1 ) , x 0 [ 1 t ∑ i ∈ mask ​ ( B k , t ) − log p θ ( x 0 i ∣ x t B k , x < B k ) ] . \mathcal{L}_{\text{BD3LM}}=\sum_{k=1}^{K}\mathbb{E}_{t\sim\mathcal{U}(0,1),x_{0}}\left[\frac{1}{t}\sum_{i\in\text{mask}(B_{k},t)}-\log p_{\theta}(x_{0}^{i}\mid x_{t}^{B_{k}},x^{<B_{k}})\right]. (3)

[27] p: This factorization allows the model to leverage cached key-values from previous blocks while generating the current block in parallel.

[28] h2: 3 dLLM Overview

[29] p: In this section, we provide an overview of the three core components of dLLM : Trainer (Section 3.1 ), Sampler (Section 3.2 ) and Evaluation (Section 3.3 ).

[30] h3: 3.1 Trainer

[31] figure: ⬇ # MDLM PT trainer = MDLMTrainer ( model = model , tokenizer = tokenizer , train_dataset = dataset [ "train" ], eval_dataset = dataset [ "test" ], args = training_args , data_collator =( DataCollatorForSeq2Seq () ) ) trainer . train () |\ phantom { }| (a) MDLM (e.g., LLaDA, Dream) Pretraining. ⬇ # MDLM PT -> BD3LM PT |\ DiffDel { trainer = MDLMTrainer (}| |\ DiffAdd { trainer = BD3LMTrainer (}| model = model , tokenizer = tokenizer , train_dataset = dataset [ "train" ], eval_dataset = dataset [ "test" ], args = training_args , data_collator =( DataCollatorForSeq2Seq () ) ) trainer . train () (b) Changes for BD3LM Pretraining. ⬇ # MDLM PT -> SFT trainer = MDLMTrainer ( model = model , tokenizer = tokenizer , train_dataset = dataset [ "train" ], eval_dataset = dataset [ "test" ], args = training_args , data_collator =( |\ DiffAdd {+~~~ NoAttentionMaskWrapper (}| DataCollatorForSeq2Seq ( |\ DiffAdd {+~~~~~~~ label \ _pad \ _token \ _id = eos \ _token \ _id ,}| ), |\ DiffAdd {+~~~)}| ), ) trainer . train () (c) Changes for MDLM SFT. ⬇ # MDLM PT -> AR-to-MDLM Adaptation trainer = MDLMTrainer ( model = model , tokenizer = tokenizer , train_dataset = dataset [ "train" ], eval_dataset = dataset [ "test" ], args = training_args , |\ DiffAdd {+~ right \ _shift \ _logits = True ,}| data_collator =( |\ DiffAdd {+~~~ PrependBOSWrapper (}| DataCollatorForSeq2Seq (), |\ DiffAdd {+~~~)}| ), ) trainer . train () |\ phantom { }| (d) Changes for AR-to-MDLM adaptation. Figure 1 : A unified trainer interface supports a variety of purposes via modular trainers and configuration changes. Figure 1(a) shows the MDLM pretraining setup. Figure 1(b) shows the single-line trainer swap from MDLMTrainer to BD3LMTrainer . Figure 1(c) shows the minimal changes to use MDLMTrainer for SFT: NoAttentionMaskWrapper keeps padding EOS visible, and label_pad_token_id=eos_token_id trains the model to generate EOS from extra mask tokens in inputs. Figure 1(d) shows the minimal changes to adapt an autoregressive LM to MDLM: right_shift_logits reuses next-token prediction, and PrependBOSWrapper prepends BOS to provide the predictions for the first mask token.

[32] h5: Unified training interface with Trainer (Figure 1 ).

[33] p: Most open-weight DLMs to date are trained with Masked Diffusion (MDLM) ( Sahoo et al., 2024 ; Nie et al., 2025b ; Ye et al., 2025 ) or Block Diffusion (BD3LM) ( Arriola et al., 2025 ) . Accordingly, the current version of dLLM focuses on unified MDLMTrainer and BD3LMTrainer as core training modules ( dllm/core/trainers ) that support both pretraining and finetuning most DLMs. At the same time, the framework’s modular design can be naturally extended to new diffusion objectives. For example, dLLM also includes a reference implementation of an EditFlow ( Havasi et al., 2025 ; Nguyen et al., 2025 ) trainer for text diffusion with parallel insertion, substitution, and deletion operations.

[34] h5: Modular design enables easy customization (Figure 1 ).

[35] p: Our training pipeline follows a modular design that allows core components to be reused and extended with minimal changes, improving both flexibility and readability. Figure 1 illustrates this modularity in practice: switching between MDLM/BD3LM pretraining, MDLM SFT, and AR-to-MDLM adaptation requires only localized changes (e.g., swapping the trainer, toggling a small set of arguments, or wrapping the data collator), without altering the overall pipeline.

[36] h5: Simple yet scalable training powered by HF infrastructure.

[37] p: Our training pipeline builds directly on the HuggingFace ecosystem. We use accelerate to support diverse training configurations (e.g., FSDP ( Zhao et al., 2023 ) and DeepSpeed ( Rajbhandari et al., 2020 ) for distributed training), and peft for parameter-efficient finetuning. Our custom trainers (e.g., MDLMTrainer ) are lightweight wrappers around the transformers Trainer ( Wolf et al., 2020 ) . By using these components as building blocks, the framework stays easy to learn, which allows users to focus on DLM-specific logic and meanwhile remains scalable enough to support large-model pretraining and research experimentation.

[38] h3: 3.2 Sampler

[39] figure: Figure 2 : Inference pipeline: sampler swap from vanilla to FastdLLM MDLM sampler. ⬇ # Inference |\ DiffDel { sampler = MDLMSampler ( model , tokenizer )}| |\ DiffAdd { sampler = MDLMFastdLLMSampler ( model , tokenizer )}| terminal_visualizer = TerminalVisualizer ( tokenizer ) messages = [[{ "role" : "user" , "content" : "Write ␣ a ␣ python ␣ function." }]] inputs = tokenizer . apply_chat_template ( messages , add_generation_prompt = True , tokenize = True ) outputs = sampler . sample ( inputs , return_dict = True ) terminal_visualizer . visualize ( outputs . histories , rich = True )

[40] figure: Figure 3 : Terminal Visualizer showing transition from masked to decoded tokens.

[41] h5: Unified inference interface with Sampler (Figure 2 ).

[42] p: Different DLMs and inference algorithms expose inconsistent inference APIs, making it hard to reuse and compare inference algorithms across models. To address this issue without modifying existing model implementations, we introduce a lightweight inference abstraction: Sampler(model).sample() . This wrapper decouples models from inference algorithms, allowing different samplers to be swapped in a plug-and-play manner while keeping the underlying model unchanged. Figure 2 illustrates the unified inference pipeline enabled by this interface.

[43] h5: Terminal visualizer (Figure 3 ).

[44] p: Unlike autoregressive LMs, which decode tokens strictly left-to-right, DLMs decode tokens in any order. As a result, the decoding order, beyond the final decoded output, is an important feature of DLMs and is valuable for analysis. To support debugging and interpretability, we provide a terminal visualizer that reveals the token decoding order and the evolution of the sample over decoding steps (Figure 3 ).

[45] h5: Efficient DLM inference (Figures 2 & 4 ).

[46] p: DLM inference speed is a practical bottleneck ( Wu et al., 2026b ; Wu et al., 2026a ; Ma et al., 2025 ; Ben-Hamu et al., 2025 ) . Building on the unified inference interface, dLLM includes an implementation of Fast-dLLM ( Wu et al., 2026b ) for accelerated MDLM decoding: MDLMFastdLLMSampler , which can be used as a drop-in replacement for the standard MDLMSampler (Figure 2 ). We report benchmarking results consistent with official Fast-dLLM implementations, demonstrating substantial inference speedups (see Figure 4 for visualization and Tables 6(b) and 7(b) in Appendix B for detailed results).

[47] figure: (a) LLaDA-Instruct. (b) Dream-Base. Figure 4 : Fast-dLLM evaluation results with max new tokens @ 256 256 and 512 512 . Model selection follows the original Fast-dLLM evaluation for consistency and fair comparison. Cache uses block-wise approximate KV caching within each decoding block; Parallel uses confidence-based parallel token updates; Cache & Parallel combines both. Note that max new tokens determines the number of pre-allocated padding tokens in the bidirectional context window, therefore affecting compute and measured performance.

[48] h3: 3.3 Evaluation

[49] p: Open-weight DLMs ( Nie et al., 2025b ; Ye et al., 2025 ) rely on different evaluation tools, making unified evaluation difficult. This is further complicated by the fact that DLMs are especially sensitive to inference hyperparameters, as prior work often relies on task-specific hyperparameter tuning and postprocessing to achieve the best performance. For example, even a single change in an inference parameter can significantly alter performance (Figure 5 ).

[50] figure: (a) LLaDA-Instruct (b) Dream-Instruct Figure 5 : Sensitivity to decoding hyperparameters. We vary individual sampling hyperparameters at inference time and observe that performance can degrade sharply from the optimal configuration. Baseline denotes the best-performing setting; Suppress does not suppress <eos> from the beginning of generation; CFG sets cfg=0.5 ; Parallel @ 4 4 generates four tokens per step; and Temp @ 0 0 sets temperature=0.0 .

[51] p: A unified evaluation pipeline must therefore be flexible enough to support customization while faithfully reproducing the evaluation configurations used in prior work. To achieve this, we extend the lm-evaluation-harness ( Gao et al., 2024 ) framework and carefully match the preprocessing, decoding settings, and post-processing used for each model–task pair with its corresponding official pipeline. These details vary across models and tasks and require manual verification, but this enables our framework to reproduce the reported, model-specific scores while supporting consistent comparisons across models. Tables 4(b) and 5(b) (Appendix B ) compare our reproduced results against the originally reported results, showing that our evaluation framework closely matches the official results.

[52] h2: 4 Open DLMs with Open Recipes

[53] p: Building on dLLM , we provide a set of fully reproducible recipes for training DLMs. These recipes cover (1) finetuning open-weight DLMs to reason (Section 4.1 ), and (2) training small DLMs from scratch with minimal compute (e.g., Section 4.2.1 , Section 4.2 ). We make all of these model checkpoints available in dllm-hub along with their evaluation results.

[54] h3: 4.1 Finetuning Open-Weight Large DLMs

[55] p: Training autoregressive LMs to reason before providing final answer has proven effective in solving complex tasks. Recent efforts such as d1 ( Zhao et al., 2025 ) have begun exploring similar reasoning capabilities in DLMs. Using the unified trainer in dLLM , finetuning large DLMs is straightforward. We demonstrate that MDLM-style SFT can elicit reasoning capabilities in existing open-weight DLMs and improve their downstream performance.

[56] h5: Training details.

[57] p: We finetune both the Base and Instruct variants of LLaDA ( Nie et al., 2025b ) and Dream ( Ye et al., 2025 ) using MDLM SFT with LoRA on the s1K dataset ( Muennighoff et al., 2025 ) . Loss is computed only on response tokens. We use maximum sequence length of 4096 4096 , 20 20 epochs, learning rate 10 − 5 10^{-5} , global batch size 32 32 with gradient accumulation steps of 4 4 . We apply LoRA adaptation with r = 128 r=128 , α = 256 \alpha=256 , and weight decay 0.1 0.1 . We adopt a cosine learning-rate schedule with 10 % 10\% warmup. Training is conducted on 8 × 8\times A100 GPUs using DeepSpeed ZeRO-2. See Figure 6 for training curves.

[58] h5: Evaluation results.

[59] p: We evaluate models SFTed on reasoning data by prepending a <reasoning> token at inference to force reasoning (Table 1 ) using evaluation pipelines from Zhao et al. (2025) . For Instruct models, reasoning SFT yields consistent gains across math, planning, and coding benchmarks. Base models show improvements on in-distribution math tasks (e.g., GSM8K ( Cobbe et al., 2021 ) , MATH500 ( Hendrycks et al., 2021b ) ) but regress on out-of-distribution benchmarks. Overall, the results indicate that SFT is an effective starting point for reasoning in DLMs; all of these are achieved with the unified trainer interface (Figure 1 ) with little changes.

[60] figure: Model GSM8K MATH500 Countdown Sudoku HumanEval MBPP LLaDA-Instruct 79.91 79.91 34.80 34.80 19.92 19.92 11.62 11.62 35.37 35.37 42.02 42.02 + SFT (MDLM) 80.59 80.59 35.40 35.40 26.95 26.95 14.36 14.36 36.59 36.59 43.97 43.97 LLaDA-Base 64.67 64.67 10.20 10.20 10.16 10.16 0.34 0.34 25.00 25.00 40.08 40.08 + SFT (MDLM) 73.62 73.62 17.40 17.40 8.98 8.98 0.00 0.00 18.90 18.90 28.79 28.79 Dream-Instruct 64.44 64.44 28.20 28.20 22.27 22.27 6.93 6.93 35.98 35.98 44.36 44.36 + SFT (MDLM) 70.43 70.43 32.80 32.80 20.31 20.31 19.68 19.68 37.20 37.20 45.53 45.53 Dream-Base 49.05 49.05 20.40 20.40 10.55 10.55 1.07 1.07 15.85 15.85 22.96 22.96 + SFT (MDLM) 63.00 63.00 23.40 23.40 8.59 8.59 1.03 1.03 29.88 29.88 23.35 23.35 Table 1: MDLM SFT evaluation results . Instruct models show consistent gains, Base models gain on in-distribution math but may regress on out-of-distribution planning and coding.

[61] h3: 4.2 Training Small DLMs from Scratch

[62] p: In addition to finetuning open-weight large DLMs, dLLM includes recipes and released checkpoints for training small DLMs from scratch (starting from backbones that are not DLMs). We cover two applications: (1) converting discriminative BERT models ( Devlin et al., 2019 ) into DLMs and (2) converting autoregressive LMs into DLMs ( Gong et al., 2025 ) .

[63] h4: 4.2.1 BERT-Chat: Converting BERTs to DLMs

[64] p: Despite their traditional use in discriminative tasks, BERT-style models ( Devlin et al., 2019 ) offer bidirectional representations well-suited for diffusive generation ( Sahoo et al., 2024 ) . We show that an off-the-shelf BERT-style model can be turned into a diffusion chatbot, without architectural changes, by finetuning only on instruction-following data. We build on top of the ModernBERT series ( Warner et al., 2025 ) as the backbone, as they are among the strongest-performing BERT variants, and release two checkpoints, ModernBERT-base-chat-v0.1 and ModernBERT-large-chat-v0.1 .

[65] h5: Training details.

[66] p: We finetune ModernBERT-base and ModernBERT-large via MDLM SFT (no continual pretraining) on a mixture of instruction-tuning datasets: Tulu 3 SFT ( Lambert et al., 2024 ) and SmolTalk ( Ben Allal et al., 2025 ) . The loss is computed only on response tokens. We use maximum sequence length 1024 1024 , 10 10 epochs, learning rate 10 − 4 10^{-4} , global batch size 384 384 , bf16 precision, and a cosine learning-rate schedule with 10 % 10\% warmup. Training runs on 8 × 8\times A100 GPUs with DeepSpeed ZeRO-2 ( Rajbhandari et al., 2020 ) . See Figure 7 for training curves. We release the scripts to reproduce the models at dllm/examples/bert .

[67] h5: Evaluation results.

[68] p: We evaluate BERT-Chats using dLLM ’s unified evaluation pipeline (Table 2 ). A gap remains compared to decoder-only ARLMs of a similar size (e.g., Qwen1.5-0.5B and Qwen1.5-0.5B-Chat ( Bai et al., 2023 ) on MMLU ( Hendrycks et al., 2021a ) and HellaSwag ( Zellers et al., 2019 ) ), yet the results are still noteworthy: ModernBERT-large-chat surpasses both GPT-2 ( Radford et al., 2019 ) variants on most benchmarks and outperforms Qwen1.5-0.5B-Chat on BBH ( Suzgun et al., 2023 ) and MATH ( Hendrycks et al., 2021b ) , despite being an encoder-only model with no architectural modification for generation. This suggests that BERT-style backbones are a viable, if under-explored, starting point for DLMs.

[69] h4: 4.2.2 Tiny-A2D: Converting ARLMs to DLMs

[70] p: Autoregressive language models (ARLMs) dominate open-ended text generation, but DLMs offer complementary benefits such as parallel decoding and iterative refinement. Prior work has explored AR-to-diffusion conversion to bootstrap ARLM training artifacts into DLMs (e.g., RND1 ( Chandrasegaran et al., 2025 ) and DiffuLLaMA ( Gong et al., 2025 ) ). We show that an off-the-shelf ARLM can be converted into a diffusion chatbot with minimal changes: we take Qwen3-0.6B ( Yang et al., 2025 ) as the backbone and tune it under two diffusion objectives, MDLM (masked diffusion) ( Sahoo et al., 2024 ) and BD3LM (block diffusion) ( Arriola et al., 2025 ) , on instruction-following data. We release two checkpoints, Qwen3-0.6B-diffusion-mdlm-v0.1 and Qwen3-0.6B-diffusion-bd3lm-v0.1 .

[71] h5: Training details.

[72] p: We train both variants with only SFT (no continual pretraining) on the mixture of Tulu 3 SFT ( Lambert et al., 2024 ) , SmolTalk ( Ben Allal et al., 2025 ) , and opc-sft-stage1&2 ( Huang et al., 2024 ) . Loss is computed only on response tokens and we do not apply the logits right shifting tricks as in prior work ( Gong et al., 2025 ; Chandrasegaran et al., 2025 ) , because in our experiments this leads to performance degradation. For the MDLM variant we use maximum sequence length 1024 1024 ; for the BD3LM variant we use length 512 512 and block size 32 32 . Both use 10 10 epochs, learning rate 10 − 4 10^{-4} , global batch size 2048 2048 , bf16 precision, and a cosine learning-rate schedule. Training is run on 64 × 64\times A100 GPUs with DeepSpeed ZeRO-2 ( Rajbhandari et al., 2020 ) . See Figure 8 for training curves. We also release the scripts to reproduce the models at dllm/examples/a2d .

[73] h5: Evaluation results.

[74] p: We evaluate both converted models using dLLM ’s unified evaluation pipeline (Table 3 ). The BD3LM variant shows particular strength on code generation, with HumanEval ( Chen et al., 2021 ) and MBPP ( Austin et al., 2021b ) scores that surpass the original Qwen3-0.6B-Base ( Yang et al., 2025 ) despite being trained with SFT alone. Overall, both DLM variants still trail their AR counterparts on most knowledge and reasoning benchmarks (e.g., MMLU ( Hendrycks et al., 2021a ) , BBH ( Suzgun et al., 2023 ) ), reflecting the expected gap at this scale. Nonetheless, the fact that a competitive DLM can be obtained from an off-the-shelf ARLM with only SFT and no continual pretraining demonstrates that AR-to-diffusion conversion is a practical and compute-efficient path to building DLMs.

[75] figure: Model GSM8K BBH MATH MMLU HellaSwag LAMBADA WinoGrande ModernBERT-base-chat-v0.1 3.6 3.6 21.1 21.1 3.1 3.1 26.2 26.2 34.5 34.5 49.3 49.3 48.8 48.8 ModernBERT-large-chat-v0.1 9.3 9.3 25.6 25.6 3.6 3.6 29.6 29.6 40.9 40.9 46.3 46.3 49.0 49.0 Qwen1.5-0.5B 22.0 22.0 18.3 18.3 3.1 3.1 39.2 39.2 48.2 48.2 48.6 48.6 55.0 55.0 Qwen1.5-0.5B-Chat 11.3 11.3 18.2 18.2 2.1 2.1 35.0 35.0 36.9 36.9 41.2 41.2 52.0 52.0 GPT-2 0.7 0.7 6.9 6.9 1.8 1.8 22.9 22.9 31.1 31.1 46.0 46.0 51.6 51.6 GPT-2-medium 2.1 2.1 17.8 17.8 1.4 1.4 22.9 22.9 39.4 39.4 55.5 55.5 53.1 53.1 Table 2: ModernBERT-Chat evaluation results. ModernBERT-Chat ( Warner et al., 2025 ) and GPT-2 ( Radford et al., 2019 ) models are evaluated with dLLM ’s pipeline; Qwen1.5 ( Bai et al., 2023 ) numbers are reported by original sources. See Figure 7 for training curves.

[76] figure: Model GSM8K BBH MATH MMLU MMLU-Pro HellaSwag HumanEval MBPP Qwen3-0.6B-mdlm-v0.1 29.3 29.3 26.7 26.7 8.7 8.7 40.0 40.0 17.3 17.3 42.1 42.1 30.5 30.5 29.2 29.2 Qwen3-0.6B-bd3lm-v0.1 46.3 46.3 26.6 26.6 12.9 12.9 39.1 39.1 13.8 13.8 39.3 39.3 46.3 46.3 38.2 38.2 Qwen2.5-0.5B 41.6 41.6 20.3 20.3 19.5 19.5 47.5 47.5 15.7 15.7 52.1 52.1 30.5 30.5 39.3 39.3 Qwen3-0.6B-Base 59.6 59.6 41.5 41.5 32.4 32.4 52.8 52.8 24.7 24.7 47.4 47.4 32.3 32.3 36.6 36.6 Table 3: Qwen-A2D evaluation results. MDLM and BD3LM models are evaluated with dLLM ’s pipeline; Autoregressive Qwen2.5/Qwen3 baselines are reported by original sources ( Qwen Team et al., 2024 ; Yang et al., 2025 ) . See Figure 8 for training curves.

[77] h2: 5 Related Work

[78] h5: Discrete diffusion for text.

[79] p: Diffusion models, originally developed for continuous domains ( Sohl-Dickstein et al., 2015 ; Ho et al., 2020 ; Song et al., 2021 ) , are extended to discrete text via absorbing-state (D3PM ( Austin et al., 2021a ) ) and uniform-state (multinomial diffusion ( Hoogeboom et al., 2021 ) ) formulations. Continuous-time extensions ( Campbell et al., 2022 ) , score-based ( Sun et al., 2023 ; Meng et al., 2022 ) , and ratio-based ( Lou et al., 2024 ) objectives further unify the theory. Masked diffusion language models (MDLMs) simplify the forward process to independent token masking, with recent work clarifying equivalences and simplifying training ( Sahoo et al., 2024 ; Shi et al., 2024 ; Ou et al., 2025 ; Zheng et al., 2025 ) . Alternative directions include continuous diffusion in embedding space ( Li et al., 2022 ; Gong et al., 2023 ; Dieleman et al., 2022 ; Lin et al., 2023 ) , flow matching and edit-based methods ( Gat et al., 2024 ; Havasi et al., 2025 ; Nguyen et al., 2025 ) , block diffusion ( Arriola et al., 2025 ) , which interpolates between AR and diffusion decoding for KV-cache reuse, and hybrid AR–diffusion architectures that use diffusion for speculative drafting ( Christopher et al., 2025 ) , planned outline-then-diffuse generation ( Israel et al., 2026 ) , or unified draft-and-verify passes ( Liu et al., 2025 ) .

[80] h5: Open-weight DLMs.

[81] p: Scaling DLMs has progressed rapidly. Nie et al. first scaled masked diffusion to 1.1B parameters. Converting pretrained autoregressive models into DLMs has proven effective: DiffuGPT/DiffuLLaMA adapt GPT-2 and LLaMA (127M–7B) ( Gong et al., 2025 ) ; RND1 ( Chandrasegaran et al., 2025 ) extends this to 30B; and LLaDA2.0 ( Bie et al., 2025 ) scales to 100B with a 3-phase block-level scheme. At the 7–8B scale, Dream ( Ye et al., 2025 ) adapts Qwen-2.5 with context-adaptive noise rescheduling, and LLaDA ( Nie et al., 2025b ) trains an 8B MDLM from scratch, achieving performance competitive with LLaMA3-8B ( Grattafiori et al., 2024 ) . Commercial systems such as Mercury ( Khanna et al., 2025 ) further demonstrate DLM viability in production.

[82] h5: Open tools for DLMs.

[83] p: Prior open-weight DLMs ( Nie et al., 2025b ; Ye et al., 2025 ; Gong et al., 2025 ; Chandrasegaran et al., 2025 ; Bie et al., 2025 ) often lack unified development pipelines, making reproduction and comparison difficult. Open efficient inference tools for DLMs such as Fast-dLLM ( Wu et al., 2026b ) and Fast-dLLM v2 ( Wu et al., 2026a ) accelerate decoding but are developed independently of training and evaluation. Evaluation pipelines also vary across papers (e.g., task sets, inference hyperparameters), and interfaces remain inconsistent. A framework unifying training, inference, and evaluation has been lacking. dLLM fills this gap with modular trainers, a plug-and-play sampler abstraction, and a reproducible evaluation pipeline aligned with official benchmarks (Section 3 , Section 4 ).

[84] h2: 6 Conclusion

[85] p: We present dLLM , an open-source framework that unifies the training, inference, and evaluation of DLMs in a modular, extensible pipeline. By standardizing the common components shared across recent DLMs, dLLM lowers the barrier to reproducing, finetuning, and fairly comparing existing models while making it straightforward to integrate new designs. Alongside the framework, we provide minimal recipes and checkpoints showing that existing pretrained models, both BERT-style encoders and autoregressive LMs, can be converted into competitive DLMs with lightweight finetuning alone, making DLM development increasingly accessible with minimal compute. We hope dLLM accelerates research and lowers the entry barrier for the broader community.

[86] h5: Future work.

[87] p: We plan to continue expanding dLLM by incorporating new methods as the field evolves, e.g., integrating RL algorithms once widely adopted approaches for DLMs emerge, and supporting additional open-weight models as they are released.

[88] h2: Acknowledgements

[89] p: Zhanhui Zhou gratefully acknowledges support from the Berkeley Fellowship.

[90] h2: References

[91] h2: Appendix A Training Curves

[92] figure: Figure 6 : Training loss for finetuning open-weight DLMs to reason (Section 4.1 ).

[93] figure: Figure 7 : Training loss for finetuning BERT to chat (Section 4.2.1 ).

[94] figure: Figure 8 : Training loss for finetuning autoregressive LMs to be DLMs (Section 4.2.2 ).

[95] h2: Appendix B Evaluation Reproduction

[96] p: In this section, we report evaluation results comparing the official implementation (as reported in the original paper) with our unified dLLM reimplementation under the same configurations. Overall, our framework reproduces the official results closely across benchmarks, indicating that our evaluation pipeline and implementation are consistent with the official setup (with only minor necessary adjustments).

[97] p: Tables 4(b) and 5(b) report our reproduced evaluation results for LLaDA ( Nie et al., 2025b ) and Dream ( Ye et al., 2025 ) with dLLM . Tables 6(b) and 7(b) report Fast-dLLM results, showing that our dLLM reimplementation achieves similar accuracy to the official numbers while substantially improving generation throughput.

[98] figure: Table 4: LLaDA evaluation results. “Official” denotes results from the original paper; “ dLLM ” denotes results from our dLLM reimplementation. “Hella.” stands for HellaSwag, “HEval” stands for HumanEval and “WinoG.” stands for WinoGrande. (a) LLaDA-Base MMLU BBH ARC-C Hella. WinoG. PIQA GSM8K MATH GPQA HEval MBPP Official 65.9 49.7 45.9 70.5 74.8 73.6 70.3 31.4 25.2 35.4 40.0 dLLM 65.9 47.2 44.1 69.2 70.4 70.7 70.7 32.4 31.9 32.9 38.8 (b) LLaDA-Instruct MMLU MMLU-Pro ARC-C Hella. GSM8K Math GPQA HEval MBPP Official 65.5 37.0 88.5 74.6 69.4 31.9 33.3 49.4 41.0 dLLM 69.8 36.2 86.4 76.7 74.7 31.9 30.6 47.0 40.0

[99] figure: Table 5: Dream evaluation results. “Official” denotes results from the original paper; “ dLLM ” denotes results from our dLLM reimplementation. “Hella.” stands for HellaSwag, “HEval” stands for HumanEval and “WinoG.” stands for WinoGrande. (a) Dream-Base MMLU BBH ARC-C Hella. WinoG. PIQA GSM8K MATH GPQA HEval MBPP Official 69.5 57.9 59.9 73.3 74.8 75.8 77.2 39.6 36.6 57.9 56.2 dLLM 70.0 63.7 59.0 73.5 72.5 76.4 77.0 42.4 34.6 56.7 56.0 (b) Dream-Instruct MMLU MMLU-Pro ARC-C Hella. GSM8K MATH GPQA HEval MBPP Official 67.0 43.3 — — 81.0 39.2 33.0 55.5 58.8 dLLM 69.8 45.5 61.4 71.8 82.0 48.6 31.5 57.9 58.2

[100] figure: Table 6: Fast-dLLM LLaDA-Instruct evaluation results with max new tokens @ 256 256 (a) and 512 512 (b). “Official” denotes results from the Fast-dLLM paper; “ dLLM ” denotes results from our dLLM reimplementation. (a) max new tokens @ 256 256 Benchmark Source Baseline +Cache +Parallel +Both Acc Tok/s ( × \times ) Acc ( × \times ) Acc ( × \times ) Acc ( × \times ) GSM8K Official 79.3 79.3 6.7 ( 1.0 × ) 6.7\ (1.0\times) 79.5 79.5 3.2 × 3.2\times 79.2 79.2 2.5 × 2.5\times 78.5 78.5 8.1 × 8.1\times dLLM 78.0 78.0 8.1 ( 1.0 × ) 8.1\ (1.0\times) 78.2 78.2 3.2 × 3.2\times 78.9 78.9 2.3 × 2.3\times 78.0 78.0 6.5 × 6.5\times MATH Official 33.5 33.5 9.1 ( 1.0 × ) 9.1\ (1.0\times) 33.3 33.3 2.6 × 2.6\times 33.4 33.4 2.7 × 2.7\times 33.2 33.2 5.7 × 5.7\times dLLM 38.3 38.3 9.7 ( 1.0 × ) 9.7\ (1.0\times) 37.6 37.6 2.7 × 2.7\times 38.6 38.6 2.0 × 2.0\times 37.5 37.5 5.0 × 5.0\times HumanEval Official 41.5 41.5 30.5 ( 1.0 × ) 30.5\ (1.0\times) 42.7 42.7 1.3 × 1.3\times 43.9 43.9 3.3 × 3.3\times 43.3 43.3 3.7 × 3.7\times dLLM 38.4 38.4 18.8 ( 1.0 × ) 18.8\ (1.0\times) 36.0 36.0 1.5 × 1.5\times 39.6 39.6 2.8 × 2.8\times 36.0 36.0 3.6 × 3.6\times MBPP Official 29.4 29.4 6.0 ( 1.0 × ) 6.0\ (1.0\times) 29.6 29.6 2.8 × 2.8\times 28.4 28.4 4.1 × 4.1\times 28.2 28.2 7.5 × 7.5\times dLLM 36.4 36.4 9.3 ( 1.0 × ) 9.3\ (1.0\times) 38.0 38.0 2.8 × 2.8\times 29.0 29.0 1.9 × 1.9\times 37.8 37.8 4.8 × 4.8\times (b) max new tokens @ 512 512 Benchmark Source Baseline +Cache +Parallel +Both Acc Tok/s ( × \times ) Acc ( × \times ) Acc ( × \times ) Acc ( × \times ) GSM8K Official 77.5 77.5 3.2 ( 1.0 × ) 3.2\ (1.0\times) 77.0 77.0 3.3 × 3.3\times 77.6 77.6 5.8 × 5.8\times 77.2 77.2 11.0 × 11.0\times dLLM 81.1 81.1 6.7 ( 1.0 × ) 6.7\ (1.0\times) 76.0 76.0 3.0 × 3.0\times 77.6 77.6 3.3 × 3.3\times 76.6 76.6 7.8 × 7.8\times MATH Official 37.2 37.2 8.0 ( 1.0 × ) 8.0\ (1.0\times) 36.2 36.2 2.5 × 2.5\times 36.8 36.8 3.0 × 3.0\times 36.0 36.0 5.9 × 5.9\times dLLM 42.4 42.4 7.4 ( 1.0 × ) 7.4\ (1.0\times) 41.9 41.9 2.9 × 2.9\times 42.5 42.5 2.7 × 2.7\times 41.8 41.8 6.0 × 6.0\times HumanEval Official 43.9 43.9 18.4 ( 1.0 × ) 18.4\ (1.0\times) 45.7 45.7 1.6 × 1.6\times 43.3 43.3 3.1 × 3.1\times 44.5 44.5 4.0 × 4.0\times dLLM 48.2 48.2 13.0 ( 1.0 × ) 13.0\ (1.0\times) 41.5 41.5 1.8 × 1.8\times 50.6 50.6 2.8 × 2.8\times 41.5 41.5 4.3 × 4.3\times MBPP Official 14.8 14.8 4.3 ( 1.0 × ) 4.3\ (1.0\times) 13.4 13.4 2.3 × 2.3\times 15.0 15.0 5.1 × 5.1\times 13.8 13.8 9.2 × 9.2\times dLLM 32.2 32.2 7.7 ( 1.0 × ) 7.7\ (1.0\times) 22.0 22.0 2.7 × 2.7\times 7.6 7.6 2.7 × 2.7\times 21.4 21.4 5.7 × 5.7\times

[101] figure: Table 7: Fast-dLLM Dream-Base evaluation results with max new tokens @ 256 256 (a) and 512 512 (b). “Official” denotes results from the Fast-dLLM paper; “ dLLM ” denotes results from our dLLM reimplementation. (a) max new tokens @ 256 256 Benchmark Source Baseline +Cache +Parallel +Both Acc Tok/s ( × \times ) Acc ( × \times ) Acc ( × \times ) Acc ( × \times ) GSM8K Official 75.0 75.0 9.1 ( 1.0 × ) 9.1\ (1.0\times) 74.3 74.3 3.6 × 3.6\times 74.2 74.2 1.6 × 1.6\times 74.8 74.8 5.3 × 5.3\times dLLM 75.4 75.4 9.0 ( 1.0 × ) 9.0\ (1.0\times) 75.0 75.0 3.7 × 3.7\times 72.6 72.6 1.4 × 1.4\times 74.2 74.2 4.7 × 4.7\times MATH Official 38.4 38.4 11.4 ( 1.0 × ) 11.4\ (1.0\times) 36.8 36.8 3.0 × 3.0\times 37.9 37.9 2.4 × 2.4\times 37.6 37.6 5.9 × 5.9\times dLLM 31.5 31.5 25.1 ( 1.0 × ) 25.1\ (1.0\times) 33.3 33.3 1.5 × 1.5\times 23.5 23.5 2.1 × 2.1\times 31.1 31.1 3.1 × 3.1\times HumanEval Official 49.4 49.4 23.3 ( 1.0 × ) 23.3\ (1.0\times) 53.7 53.7 1.5 × 1.5\times 49.4 49.4 2.0 × 2.0\times 54.3 54.3 2.8 × 2.8\times dLLM 57.9 57.9 14.0 ( 1.0 × ) 14.0\ (1.0\times) 53.7 53.7 2.4 × 2.4\times 51.2 51.2 1.5 × 1.5\times 53.1 53.1 3.1 × 3.1\times MBPP Official 56.6 56.6 11.2 ( 1.0 × ) 11.2\ (1.0\times) 53.2 53.2 3.1 × 3.1\times 53.8 53.8 2.8 × 2.8\times 56.4 56.4 6.8 × 6.8\times dLLM 55.6 55.6 9.9 ( 1.0 × ) 9.9\ (1.0\times) 53.8 53.8 3.3 × 3.3\times 53.6 53.6 2.5 × 2.5\times 56.0 56.0 6.3 × 6.3\times (b) max new tokens @ 512 512 Benchmark Source Baseline +Cache +Parallel +Both Acc Tok/s ( × \times ) Acc ( × \times ) Acc ( × \times ) Acc ( × \times ) GSM8K Official 76.0 76.0 7.7 ( 1.0 × ) 7.7\ (1.0\times) 74.3 74.3 3.3 × 3.3\times 73.4 73.4 1.9 × 1.9\times 74.0 74.0 5.6 × 5.6\times dLLM 75.7 75.7 7.6 ( 1.0 × ) 7.6\ (1.0\times) 73.8 73.8 3.4 × 3.4\times 72.7 72.7 1.6 × 1.6\times 74.5 74.5 4.4 × 4.4\times MATH Official 39.8 39.8 9.6 ( 1.0 × ) 9.6\ (1.0\times) 38.0 38.0 2.8 × 2.8\times 39.5 39.5 3.2 × 3.2\times 39.3 39.3 6.5 × 6.5\times dLLM 39.2 39.2 15.8 ( 1.0 × ) 15.8\ (1.0\times) 39.2 39.2 1.8 × 1.8\times 32.0 32.0 1.6 × 1.6\times 38.9 38.9 2.9 × 2.9\times HumanEval Official 54.3 54.3 16.3 ( 1.0 × ) 16.3\ (1.0\times) 54.9 54.9 1.7 × 1.7\times 51.8 51.8 1.8 × 1.8\times 54.3 54.3 3.2 × 3.2\times dLLM 54.9 54.9 10.4 ( 1.0 × ) 10.4\ (1.0\times) 54.9 54.9 2.5 × 2.5\times 50.6 50.6 1.6 × 1.6\times 54.3 54.3 3.6 × 3.6\times MBPP Official 55.6 55.6 9.4 ( 1.0 × ) 9.4\ (1.0\times) 53.8 53.8 2.8 × 2.8\times 55.4 55.4 4.0 × 4.0\times 55.2 55.2 7.8 × 7.8\times dLLM 56.0 56.0 4.6 ( 1.0 × ) 4.6\ (1.0\times) 52.6 52.6 5.4 × 5.4\times 52.8 52.8 6.4 × 6.4\times 54.4 54.4 13.3 × 13.3\times

[102] h2: Instructions for reporting errors

[103] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[104] p: Tip: You can select the relevant text first, to include it in your report.

[105] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[106] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
