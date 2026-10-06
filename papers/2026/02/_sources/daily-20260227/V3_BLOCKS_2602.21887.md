[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection

[3] h6: Abstract

[4] p: Current large reasoning models (LRMs) have shown strong ability on challenging tasks after reinforcement learning (RL) based post-training. However, previous work mainly focuses on English reasoning in expectation of the strongest performance, despite the demonstrated potential advantage of multilingual thinking, as well as the requirement for native thinking traces by global users. In this paper, we propose ExpLang, a novel LLM post-training pipeline that enables on-policy thinking language selection to improve exploration and exploitation during RL with the use of multiple languages. The results show that our method steadily outperforms English-only training with the same training budget, while showing high thinking language compliance for both seen and unseen languages. Analysis shows that, by enabling on-policy thinking language selection as an action during RL, ExpLang effectively extends the RL exploration space with diversified language preference and improves the RL exploitation outcome with leveraged non-English advantage. The method is orthogonal to most RL algorithms and opens up a new perspective on using multilinguality to improve LRMs 1 1 1 Our code and data is available at https://github.com/RiverGao/ExpLang .

[5] h6: Keywords:

[6] figure: Figure 1: Overview of our work. a. Multilingual thinking shows larger diversity and higher Pass@ k k , suggesting better exploration space; b. The ExpLang pipeline with on-policy thinking language selection to leverage the advantage.

[7] h2: 1 Introduction

[8] p: Large language model (LLM) reasoning, as a form of the test-time scaling ( Wu et al., 2024 ; Muennighoff et al., 2025 ) , has been rapidly developing from Chain-of-Thoughts (CoT, Wei et al. 2022 ) prompting to large reasoning models (LRMs) based on Reinforcement Learning with Verifiable Rewards (RLVR), showing very strong performance on challenging tasks ( OpenAI et al., 2024 ; DeepSeek-AI et al., 2025 ) .

[9] p: However, current research mainly focuses on English reasoning, partially because the models tend to show their strongest performance in English, as a result of their English-dominant training data. For a long time, the multilinguality in LLM reasoning has been viewed as a “curse” that hinders performance ( Etxaniz et al., 2024 ) , or a service that caters to users with different language backgrounds ( Zhang et al., 2025 ) . In contrast, some previous work point out that multilingual reasoning may have a potential benefit to overall performance ( Chen et al., 2025a ; Huang et al., 2025 ; Gao et al., 2025 ; Xu & Zhang, 2026 ) . For example, the model’s Pass@ k k score with multilingual CoTs is significantly higher than with English CoTs ( Gao et al., 2025 ) , suggesting that multilingual thinking extends the model’s exploration space with higher expected return for RLVR. Thus, this work attempts to equip the model with self-controlled multilingual thinking during training and testing, leveraging its higher exploration and exploitation efficiency to enhance the overall reasoning ability.

[10] p: In this work, we choose math reasoning as a representative task, and propose ExpLang ( Exp lore and Exp loit with multiple Lang uages), a novel LLM post-training pipeline that encourages the model to explore reasoning with different languages and exploit the extended action space to improve reasoning performance, which are enabled by supervised cold-starting and RLVR with on-policy thinking language selection. Figure 1 shows the overview of our work. Results show that our method:

[11] p: Steadily outperforms English-only training with the same training budget, while showing significantly higher performance gain during RLVR;

[12] p: Shows near-perfect thinking language compliance under forced language selection for seen languages, generalizing well to unseen languages;

[13] p: Enables on-policy thinking language selection during RL, witnessing diversified language preference during the exploration stage and converged during the exploitation stage, benefiting the model with higher response diversity and leveraged non-English advantage.

[14] p: To the best of our knowledge, this is the first work that advances in the above three aspects with a single training pipeline, which offers a novel perspective of covering and leveraging multilinguality in LLM reasoning with benefit in both language equality and model performance.

[15] h2: 2 Related Work

[16] h3: 2.1 From Chain-of-Thoughts to RL-Enhanced Reasoning

[17] p: LLM reasoning is a common form of test-time scaling ( Wu et al., 2024 ) , which originates from the chain-of-thought technique ( Wei et al., 2022 ) that improves LLM performance with step-by-step answers. When combined with RL methods designed for LLMs ( Schulman et al., 2017 ; Rafailov et al., 2024 ) , RL-empowered LRMs are proposed ( OpenAI et al., 2024 ; DeepSeek-AI et al., 2025 ; Muennighoff et al., 2025 ) , which are unprecedentedly strong on challenging tasks such as math reasoning. Among them, one of the most influential work is GRPO ( Shao et al., 2024 ) , which effectively reduces the RL training cost by removing the value model, inspiring many new RL algorithms ( Liu et al., 2025 ; Yu et al., 2025 ; Zheng et al., 2025 ) .

[18] h3: 2.2 Multilingual Reasoning of LLMs

[19] p: Despite their success, LRM research highly focuses on English, where the role of multilinguality is largely neglected or debated. There are mainly four views regarding LRM multilinguality: (1) As a curse, which claims that introducing non-English languages in training or testing harms the models’ performance ( Qi et al., 2025 ; Etxaniz et al., 2024 ) ; (2) As a user service, which underlines that LRMs should adjust their reasoning languages according to the user’s need ( Chang et al., 2024 ; Zhang et al., 2025 ; Park et al., 2025 ; Liu & Niehues, 2025 ) ; (3) As a transferrable capability, which shows that LLMs are able to partly transfer their reasoning capabilities across languages under certain conditions ( Zhang et al., 2024 ; Hu et al., 2025 ; Ranaldi & Pucci, 2025 ) ; (4) As a potential benefit, which demonstrates that non-English thinking can sometimes outperform English thinking, thus its advantages can be leveraged ( Chen et al., 2025a ; Gao et al., 2025 ; Huang et al., 2025 ; Xu & Zhang, 2026 ) . This paper proposes on-policy multilingual thinking as a useful method to not only improve LRM training, but also fostering user-compliance.

[20] p: Current methods to perform multilingual thinking mainly falls in two types. The first is prefix-hacking, i.e. adding language-specific prefixes at the beginning of model generation ( Yong et al., 2025 ; Qi et al., 2025 ; Xu & Zhang, 2026 ) , which is lightweight but unstable. The second is post-training, i.e. finetuning the model with multilingual thinking data ( Lai & Nissim, 2024 ; Chai et al., 2024 ; She et al., 2024 ; Barua et al., 2025 ; Faisal et al., 2025 ; Son et al., 2025 ; Zhang et al., 2025 ) , which is stable but causes performance drop. This paper combines the two sides and proposes a stable and cost-efficient way of thinking language control.

[21] h2: 3 Building Blocks

[22] p: Starting from the idea of extending LLMs’ exploration space with multilingual thinking to improve their mathematical reasoning, our method first equips the model with steady thinking language control, and then enable on-policy selection for multilingual exploration and exploitation in RLVR. The whole process is illustrated in Figure 1 .

[23] h3: 3.1 High-Quality Multilingual Thinking Data

[24] p: Since current reasoning datasets are English-dominant, the first building step is to generate high-quality multilingual thinking data based on existing open-source models and datasets. Specifically, for a moderate-size open-source LLM M 0 M_{0} , we adopt its larger variant M ~ 0 \tilde{M}_{0} as the teacher to perform multilingual thinking on an English math training set, induced by 12 non-English prefixes, including 6 European and 6 Asian languages (see Figure 6 ). The language list acts as a meaningful representative, which can be extended with richer computational resource. Since the inference results contain incorrect answers and incompliant thinking languages, we identify the thinking languages with LangDetect 2 2 2 https://pypi.org/project/langdetect and verify the answer correctness with HuggingFace Math-Verify 3 3 3 https://github.com/huggingface/Math-Verify . The two-way filtration helps improve the quality of the multilingual thinking data.

[25] p: To save inference cost, we first estimate the acceptance rate for each language with 100 samples (see Figure 6 ), and get approximately 500 filtered samples in each non-English language guided by these rates. To balance diversity and comparison within the dataset, inputs for each language are independently sampled from the original dataset. After that, we add a language selection tag for each sample in the form “ <lang_select>[lang]</lang_select> ” before the thinking tag, where [lang] is the language code such as en , zh , etc..

[26] h3: 3.2 Cold-Start of Thinking Language Selection

[27] p: The next building block is to align M 0 M_{0} with the collected data to cold-start the thinking language behavior, for which SFT is a suitable choice. The cold-started model, M 1 M_{1} , is supposed to be highly compliant to the above mentioned language selection tags.

[28] p: However, since M 0 M_{0} is a post-trained model, it is necessary to prevent catastrophic forgetting during the finetuning process. In this regard, we use LoRA ( Hu et al., 2021 ) SFT to reduce the change in model parameter. The results in § 6.1 show that LoRA effectively reduces the drop in mathematical performance after training compared to full SFT.

[29] h3: 3.3 RLVR with Thinking Language Selection

[30] p: The final building block is to allow on-policy thinking language selection during the traditional RLVR training process. In order to optimize the model’s mathematical reasoning ability with on-policy thinking language selection, the reward function contains the following aspects:

[31] p: Format and language compliance reward ( r f r_{f} and r c r_{c} );

[32] p: Thinking language Diversity reward ( r d r_{d} );

[33] p: Language Pass@ k k reward ( r p r_{p} );

[34] p: Original rule-based verification reward ( r v r_{v} );

[35] p: As a result, the reward r r for each training sample should be

[36] table: r = λ f ​ r f + λ c ​ r c + λ d ​ r d + λ p ​ r p + λ v ​ r v r=\lambda_{f}r_{f}+\lambda_{c}r_{c}+\lambda_{d}r_{d}+\lambda_{p}r_{p}+\lambda_{v}r_{v}

[37] p: where r ⋅ r_{\cdot} is 0 or 1, while λ ⋅ \lambda_{\cdot} ranges from 0 to 1. Based on experimental results, the reward design of ExpLang consists of two stages, λ f = 0.2 , λ c = 0.2 , λ v = 1 \lambda_{f}=0.2,\lambda_{c}=0.2,\lambda_{v}=1 being set for both stages, but λ d \lambda_{d} and λ p \lambda_{p} being selective to stages.

[38] p: First is the exploration stage which covers the first 1/4 of the RL training steps. During this stage, λ d = 0.2 , λ p = 0 \lambda_{d}=0.2,\lambda_{p}=0 is set to reward under-sampled languages to extend the exploration space. For a batch of n n responses, r d = k min / k r_{d}=k_{\mathrm{min}}/k for responses in a given language, where k ≤ n k\leq n is the response number in that language among the batch, and k min k_{\mathrm{min}} is the smallest language response number in that batch. By such regulated but automatic thinking language selection, the model is encouraged to try different thinking languages, generating more diverse reasoning traces, while respecting answer correctness. Compared with off-policy forced thinking language selection (e.g. assigning fixed language tags during rollouts), our method is on-policy since the language selection are all acted by the model itself during training, which is acknowledged to have higher stability in RL literature ( Andrychowicz et al., 2020 ) .

[39] p: Second is the exploitation stage which covers the remaining 3/4 of the RL training steps. During this stage, λ d = 0 , λ p = 0.5 \lambda_{d}=0,\lambda_{p}=0.5 is set. For each correct response, all other responses in the batch with the same thinking language will be rewarded by r p = 1 r_{p}=1 . By such design, we aim to encourage the selection of more efficient thinking languages to leverage the better-explored action space, yielding better overall performance. The model is expected to converge to one or few best-performing thinking languages. Our usage of Pass@ k k is inspired by Chen et al.’s ( 2025b ) Pass@ k k training framework. However, instead of their idea of bootstrapping sub-groups from the rollouts, our method leverages natural sub-groups formed by thinking languages, which can also be added upon their method if needed.

[40] p: The KL loss in the original GRPO algorithm is disabled during the exploration stage to enhance diversity of the model outputs, and activated during the exploitation stage to slow down the thinking language concentration.

[41] h2: 4 Experiment Settings

[42] h3: 4.1 Models, Data and Training Strategies

[43] p: For the models , this study adopts the Qwen3 ( Yang et al., 2025 ) model family (4B as M 0 M_{0} for training, 32B as M ~ 0 \tilde{M}_{0} for data generation) for all the experiments, which is a state-of-the-art open-source LRM family with large language coverage. It is worth noticing that the generation length is set to 4096 for affordable training cost, instead of 32768, so the evaluated task scores will be lower than officially reported. However, this does not harm the soundness of our experiments, since all experimental inference is performed under the same length constraint, and 4096 is a meaningful length for inference with limited computational budgets.

[44] p: For the training data , this study adopts the OpenR1-Math-220k dataset 4 4 4 https://huggingface.co/datasets/open-r1/OpenR1-Math-220k , which contains high-quality competition-level math problems and ground-truth answers from NuminaMath 1.5 5 5 5 https://huggingface.co/datasets/AI-MO/NuminaMath-1.5 and verified thinking traces generated with DeepSeek-R1. For SFT, 7301 multilingual thinking traces in total are generated from the dataset; For RLVR, we randomly sample another 51200 samples from it.

[45] p: For the training strategies , this study adopts LoRA ( Hu et al., 2021 ) finetuning targeting all linear modules for the SFT stage base on LLaMA-Factory ( Zheng et al., 2024 ) ; And we use modified GRPO algorithm ( Shao et al., 2024 ) for the RLVR stage based on VeRL ( Sheng et al., 2024 ) . These two are widely used, representative strategies among the research community. The hyper-parameters and budgets used in our training pipeline are listed in Appendix C .

[46] p: For the testing data , this study adopts three math test sets, ranging from easy to hard: (1) MATH-500 6 6 6 https://huggingface.co/datasets/HuggingFaceH4/MATH-500 , which contains 500 competition math problems from the MATH benchmark ( Hendrycks et al., 2021 ; Lightman et al., 2023 ) ; (2) AIME 2025 7 7 7 https://huggingface.co/datasets/yentinglin/aime_2025 , which contains 30 problems from the 2025 American Invitational Mathematics Examination (AIME); (3) The en-easy subset of Olym-MATH ( Sun et al., 2025 ) , which contains 100 meticulously curated AIME-level problems.

[47] figure: Table 1: Performances of Qwen3 models across test sets under en and multi settings. “Compl.” denotes thinking language compliance. Size Setting Acc(%) ↑ \uparrow Pass@k(%) ↑ \uparrow Tokens ↓ \downarrow Compl. ↑ \uparrow MATH-500 4B en 79.4 91.6 2900.7 100.0 multi 75.7 93.4 2339.7 73.3 8B en 77.8 90.6 3007.8 100.0 multi 75.0 93.4 2505.7 72.7 32B en 80.2 93.0 2796.3 100.0 multi 80.3 95.4 2242.7 66.9 AIME-2025 4B en 18.6 33.3 4056.2 100.0 multi 16.7 30.0 3966.7 71.9 8B en 21.1 26.7 4059.3 100.0 multi 14.2 33.3 3997.0 68.9 32B en 25.6 33.3 4011.5 100.0 multi 22.5 40.0 3858.6 51.7 OlymMATH en-easy 4B en 6.6 19.0 4084.9 100.0 multi 5.0 25.0 4065.7 73.7 8B en 5.3 20.0 4087.3 100.0 multi 4.3 24.0 4084.5 67.3 32B en 7.8 25.0 4084.7 100.0 multi 7.5 31.0 4040.0 48.7

[48] h3: 4.2 Baselines

[49] p: Two baselines are adopted to compare to the proposed training pipeline. The naive baseline is Qwen3-4B directly trained with GRPO on the same RL training data with slightly less training cost (without LoRA) than our model, but does not suffer from catastrophic forgetting. The controlled baseline is Qwen3-4B first going through LoRA SFT on controlled dataset with the same queries as for the proposed model. The dataset contains verified English thinking traces from Qwen3-32B without language selection tags. Then, the model is trained with GRPO on the RL training data. This baseline has the same training cost as the proposed model. The number of training samples and the hyper-parameters are consistent across the models.

[50] figure: Table 2: Performance comparison between models, with automatic (default) thinking language selection across test sets. “Ctrl” stands for the controlled baseline, while “Naive” stands for the naive baseline and “Ours” stands for ExpLang. Parentheses denote performance change during the last training stage. Model Acc(%) ↑ \uparrow Pass@k(%) ↑ \uparrow Tokens ↓ \downarrow MATH-500 Qwen3-4B 78.1 90.0 2953.2 SFT (Ctrl) 78.6 (+0.5) 93.4 2764.1 SFT (Ours) 72.0 (-6.1) 92.6 2590.9 RLVR (Naive) 91.4 (+13.3) 96.6 1416.9 RLVR (Ctrl) 91.0 (+12.4) 96.6 1440.0 RLVR (Ours) 91.5 (+19.4) 96.8 1263.3 AIME-2025 Qwen3-4B 18.9 30.0 4047.4 SFT (Ctrl) 21.4 (+2.5) 33.3 3996.0 SFT (Ours) 16.1 (-2.8) 33.3 3937.4 RLVR (Naive) 30.8 (+11.9) 43.3 3408.1 RLVR (Ctrl) 26.4 (+5.0) 43.3 3344.8 RLVR (Ours) 31.9 (+15.8) 53.3 3281.3 OlymMATH en-easy Qwen3-4B 7.0 22.0 4079.8 SFT (Ctrl) 6.2 (-0.8) 22.0 4077.7 SFT (Ours) 5.4 (-1.6) 28.0 4054.9 RLVR (Naive) 23.4 (+16.4) 44.0 3661.3 RLVR (Ctrl) 23.2 (+17.0) 48.0 3629.4 RLVR (Ours) 24.2 (+18.8) 53.0 3554.2

[51] h2: 5 Main Results

[52] h3: 5.1 Potential Benefit of Multilingual Thinking

[53] p: We first examine the potential benefit of multilingual thinking of the Qwen3 models by measuring the models’ average accuracy, Pass@ k k , language compliance and number of thinking tokens under two settings: en (prefix-hacked English thinking for 12 randomized runs, which is close to default generation with slightly different performance), and multi (prefix-hacked thinking in 12 non-English languages). Table 1 shows the performance of models sized 4B, 8B and 32B on the three testing datasets. One can see that, despite the highest accuracy of en , the multi setting shows higher Pass@ k k values and fewer thinking tokens across model sizes and datasets. This result is in line with previous work on multilingual CoT ( Gao et al., 2025 ) . Besides, an LLM-assisted trajectory analysis shows Qwen3-32B’s multilingual thinking traces form more clusters in the embedding space than English ones, indicating richer reasoning semantics (see Appendix B ). These findings support our motivation that multilingual thinking can bring potential benefit to LLM reasoning with better exploration space and more efficient reasoning. Also, the language compliance of these models is not satisfactory, which underlines the need for a cold-start for the thinking language selection behavior.

[54] h3: 5.2 Performance with Automatic Selection

[55] p: In real applications, the performance with no extra constrain, i.e. under the self setting, is the most important. Table 2 shows the average accuracy, Pass@ k k and number of thinking tokens of the proposed ExpLang method and the two baselines (naive and controlled). The results show that the proposed method exhibits the highest accuracy and Pass@ k k , indicating that the ExpLang pipeline steadily improves the model’s general reasoning ability.

[56] p: Moreover, looking at the change in average accuracies, one can notice that our RL stage involving automatic thinking language selection brings significantly higher performance gain than the English-only baselines, suggesting that our method can improve the efficiency of the RLVR training process within the same computational budget. Also, it reduces thinking tokens without sacrificing performance.

[57] figure: Table 3: Results on seen languages: performance, tokens, and compliance with forced language selection. Acc F \mathrm{Acc}^{F} means accuracy filtered on compliant samples only, and Acc ∗ \mathrm{Acc}^{*} means accuracy with incompliance counted as error. Other notations are consistent with previous tables. Model Acc F ↑ \mathrm{Acc}^{F}\uparrow Acc ∗ ↑ \mathrm{Acc}^{*}\uparrow Tokens ↓ \downarrow Compl. ↑ \uparrow MATH-500 Qwen3-4B 73.8 54.2 2339.7 73.3 SFT (Ctrl) 70.5 (-3.3) 57.3 (+3.1) 2298.4 80.9 SFT (Ours) 69.0 (-4.8) 68.6 (+14.4) 2298.1 99.3 RLVR (Naive) 87.2 (+13.4) 57.8 (+3.7) 1321.3 66.2 RLVR (Ctrl) 85.5 (+15.0) 67.6 (+10.3) 1317.8 78.8 RLVR (Ours) 85.7 (+16.7) 85.6 (+17.0) 1220.0 99.9 AIME-2025 Qwen3-4B 14.2 10.3 3966.7 71.9 SFT (Ctrl) 14.1 (-0.1) 11.1 (+0.8) 3909.7 76.4 SFT (Ours) 14.7 (+0.5) 14.7 (+4.4) 3895.9 99.2 RLVR (Naive) 23.9 (+9.7) 15.3 (+5.0) 3392.5 64.2 RLVR (Ctrl) 24.6 (+10.5) 18.9 (+7.8) 3332.0 75.3 RLVR (Ours) 27.3 (+12.6) 27.2 (+12.5) 3260.7 99.7 OlymMATH en-easy Qwen3-4B 3.5 2.6 4065.7 73.7 SFT (Ctrl) 4.4 (+0.9) 3.8 (+1.2) 4063.5 84.3 SFT (Ours) 3.8 (+0.3) 3.8 (+1.2) 4009.1 99.2 RLVR (Naive) 14.5 (+11.1) 9.7 (+7.1) 3605.7 67.1 RLVR (Ctrl) 16.1 (+11.7) 13.6 (+9.8) 3584.3 82.2 RLVR (Ours) 14.7 (+10.9) 14.7 (+10.9) 3566.3 99.7

[58] figure: Table 4: Results on unseen languages: performance, tokens, and compliance with forced language selection. The notations are consistent with previous tables. Model Acc F ↑ \mathrm{Acc}^{F}\uparrow Acc ∗ ↑ \mathrm{Acc}^{*}\uparrow Tokens ↓ \downarrow Compl. ↑ \uparrow MATH-500 Qwen3-4B 80.4 54.2 2201.5 34.0 SFT (Ctrl) 70.0 (-10.4) 32.8 (-21.4) 2147.6 46.4 SFT (Ours) 64.5 (-15.9) 41.7 (-12.5) 2233.7 62.8 RLVR (Naive) 83.5 (+3.1) 24.6 (-29.6) 1208.1 28.6 RLVR (Ctrl) 81.1 (+11.1) 37.9 (+5.2) 1258.9 46.6 RLVR (Ours) 81.6 (+17.1) 61.5 (+19.8) 1222.9 75.5 AIME-2025 Qwen3-4B 20.0 5.8 3869.0 33.3 SFT (Ctrl) 15.0 (-5.0) 7.5 (+1.7) 3829.5 49.2 SFT (Ours) 21.1 (+1.1) 11.7 (+5.8) 3845.0 55.8 RLVR (Naive) 16.7 (-3.3) 4.2 (-1.7) 3333.0 28.3 RLVR (Ctrl) 20.0 (+0.0) 10.0 (+2.5) 3145.0 46.7 RLVR (Ours) 20.0 (+0.0) 15.0 (+3.3) 3249.8 73.3 OlymMATH en-easy Qwen3-4B 6.0 2.3 4012.1 34.5 SFT (Ctrl) 4.5 (-1.5) 2.3 (+0.0) 4031.9 47.8 SFT (Ours) 3.3 (-2.7) 2.5 (+0.3) 4040.6 71.3 RLVR (Naive) 12.5 (+6.5) 3.3 (+1.0) 3418.1 27.8 RLVR (Ctrl) 9.5 (+5.0) 4.8 (+2.5) 3510.2 45.5 RLVR (Ours) 11.0 (+7.7) 8.3 (+5.8) 3391.6 74.3

[59] h3: 5.3 Performance with Forced Selection

[60] p: Another important setting to evaluate under is forced non-English thinking language selection, which is required to improve the readability of model thinking traces for non-English speakers. For ExpLang, this can be done by adding thinking language tags; for the baselines, this can be done by adding language-specific prefixes. Note that the language compliance of the two baselines is lower than ours, meaning they are partly using English thinking, yielding overestimated scores, so we propose two modified accuracy score: Acc F \mathrm{Acc}^{F} that exclude incompliant samples in Acc calculation, and Acc ∗ \mathrm{Acc}^{*} that view incompliance as error.

[61] p: As shown in Table 3 , in the trained 12 non-English languages, while showing comparable Acc F \mathrm{Acc}^{F} and superior Acc ∗ \mathrm{Acc}^{*} , our method shows higher performance gain during RLVR and fewer thinking tokens. Also, it maintains near-saturate seen thinking language compliance, much higher than the baselines. In a word, our method significantly outperforms the baselines in terms of compliant and accurate multilingual thinking.

[62] p: Moreover, it is convenient to extend ExpLang to unseen languages, by simply providing their language selection tag. In this aspect, we take 4 unseen, low-resource languages, namely id , he , ro and sw , to evaluate the models’ generalizability. Table 4 shows the comparison between ExpLang and the baselines in the four unseen languages. The results show that our model substantially outperforms the baselines, while showing high unseen language compliance. This suggests that the benefit of the ExpLang pipeline can generalize to a broader language scope.

[63] figure: Figure 2: Trends of thinking language selection rates of our model at the end of different training stages, across the three test sets.

[64] h3: 5.4 Changes in Thinking Language Preference

[65] p: Similar to other LRMs, the original Qwen-3 model produce all its thinking taces in English. However, during the SFT and RLVR training in our pipeline, the model’s thinking language preference will go through substantial changes. Specifically, we expect the model to use non-English thinking more during and after the exploration stage, making more room of improvement for the exploitation stage.

[66] p: Figure 2 shows the change in the model’s thinking language selection rates after different training stages, which demonstrate a “ English-Multlingual-English ” pattern, where the accuracy under the automatic setting keeps improving during the RL stages.

[67] p: After LoRA SFT stage containing many multilingual thinking samples, the model’s English preference become significantly depressed. Then, after the exploration stage, English becomes equally or even less frequently chosen compared with other languages. This suggests that our SFT and RL exploration stages successfully encourage an LRM to perform multilingual thinking.

[68] p: After the exploitation stage, the model converges its thinking language selection, and English becomes dominant again. This suggests that based on the diversified feedback from the broader action space, English thinking turns out to be the most efficient in leveraging these feedback, resulting in improved overall performance. This aligns with the cross-lingual transfer of reasoning capability, where training in one language ends up improving reasoning in another language ( Zhang et al., 2024 ; Hu et al., 2025 ) , as well as the results in Table 3 where English-only training (“Naive” and “Ctrl”) also improves multilingual performance.

[69] h2: 6 Ablation and Analysis

[70] h3: 6.1 Ablation Study

[71] p: The ExpLang pipeline contains three stages: the LoRA SFT stage, the multilingual exploration stage in RL, and the language Pass@ k k exploitation stage in RL. This section evaluates the necessity of each stage’s design by comparing to the results of alternated training strategies.

[72] h4: LoRA vs. fully SFT.

[73] p: In the SFT stage, we adopt LoRA instead of fully finetuning to counter catastrophic forgetting which often happens to post-trained LLMs such as Qwen3. To validate our choice, we compare the LoRA-tuned model with a fully-tuned one with the same training data and hyper-parameters, except with the learning rate reduced from 1e-4 to 1e-5, which is an acknowledged operation when switching between LoRA and fully SFT ( Bohnet et al., 2025 ) .

[74] p: The results with automatic thinking language selection are shown in Table 5 , which tells that despite being close in accuracy and language compliance under forced language selection, the LoRA model shows significantly higher accuracy than the fully finetuned one with automatic language selection. In this regard, using LoRA SFT is necessary in reducing the performance drop after training the model to follow language tags.

[75] figure: Table 5: Accuracy and language compliance of the original, LoRA-tuned and fully-tuned models. “Auto Acc” stands for the average accuracy with automatic thinking language selection, while “Forced Acc F \mathrm{Acc}^{F} ” stands for the average accuracy filtered by compliance with forced thinking language selection of seen non-English languages. Model Auto ↑ \uparrow Acc Forced Acc F \mathrm{Acc}^{F} ↑ \uparrow Compl. ↑ \uparrow MATH-500 Qwen3-4B 78.1 73.8 73.3 LoRA 72.0 69.0 99.3 Fully 66.9 68.7 99.5 AIME-2025 Qwen3-4B 18.9 14.2 71.9 LoRA 16.1 14.7 99.2 Fully 10.0 14.4 99.4 OlymMATH en-easy Qwen3-4B 7.0 3.5 73.7 LoRA 5.4 3.8 99.2 Fully 3.8 3.4 99.2

[76] h4: Diversity-enhanced exploration.

[77] p: The first part of our RLVR training is the exploration stage, where we encourage the model to select less frequent languages for thinking, by which we expect to extend the exploration space and bring more room for exploitation. To validate the effect of the exploration stage, we train another model with only the exploitation stage (the total training steps matches the original exploration + exploitation steps), and compare its performance with the original one in Table 6 .

[78] p: The results show that canceling the exploration step causes observable and consistent drop in performance under both the automatic and the forced settings. Since the exploitation stage also has a language compliance reward, the two models do not differ much in this aspect.

[79] figure: Table 6: Accuracy and language compliance of training with or without the multilingual exploration stage. The notations are consistent with previous tables. RL Model Auto Acc ↑ \uparrow Forced Acc F \mathrm{Acc}^{F} ↑ \uparrow Compl. ↑ \uparrow MATH-500 w/ explore 91.5 85.7 99.9 w/o explore 91.0 85.0 99.7 AIME-2025 w/ explore 31.9 27.3 99.7 w/o explore 28.9 23.9 100.0 OlymMATH en-easy w/ explore 24.2 14.7 99.7 w/o explore 22.8 14.1 99.5

[80] h4: Language Pass@k exploitation.

[81] p: The second part of our RLVR training is the exploitation stage, where we add a language sub-grouped Pass@ k k reward to encourage the model to use its best performing languages. To validate the effect of this stage, we train another two models, one with only default GRPO reward during exploitation (“naive exploit”), the other with only the exploration stage (the total training steps matches the original exploration + exploitation steps). The results are listed in Table 7 , which offers three observations: (1) Canceling the exploitation stage causes observable drop in performance under the automatic setting, but improves performance with forced multilingual thinking, probably because the model keeps choosing different thinking languages during training and testing. (2) Naive exploitation shows close performance to multilingual Pass@ k k exploitation, with some disadvantage in forced multilingual thinking, which shows that language Pass@ k k training is not dominant for the improvement. (3) Although having no thinking language compliance reward during exploitation, “naive exploit” shows comparable compliance to the other models with the reward in exploitation, indicating that language compliance reward in either stage has a lasting effect, allowing other exploitation methods if needed.

[82] figure: Table 7: Accuracy and language compliance of training with multilingual exploitation, naive GRPO exploration, and without exploration. The notations are consistent with previous tables. RL Model Auto Acc ↑ \uparrow Forced Acc F \mathrm{Acc}^{F} ↑ \uparrow Compl. ↑ \uparrow MATH-500 w/ multi. exploit 91.5 85.7 99.9 w/ naive exploit 91.7 85.3 99.7 w/o exploit 88.0 87.5 99.9 AIME-2025 w/ multi. exploit 31.9 27.3 99.7 w/ naive exploit 31.1 25.0 99.7 w/o exploit 25.6 29.2 99.4 OlymMATH en-easy w/ multi. exploit 24.2 14.7 99.7 w/ naive exploit 24.2 16.4 99.3 w/o exploit 23.8 17.4 99.8

[83] figure: Table 8: Accuracy and language compliance of training with different KL loss settings during the exploration and exploitation stages, respectively. The notations are consistent with previous tables. Stage-Wise KL Use Auto Acc ↑ \uparrow Forced Acc F \mathrm{Acc}^{F} ↑ \uparrow Compl. ↑ \uparrow MATH-500 (N, Y) 91.5 85.7 99.9 (N, N) 90.8 85.4 99.7 (Y, Y) 91.1 84.3 99.8 AIME-2025 (N, Y) 31.9 27.3 99.7 (N, N) 31.1 24.5 99.7 (Y, Y) 32.8 23.1 99.7 OlymMATH en-easy (N, Y) 24.2 14.7 99.7 (N, N) 24.6 15.8 99.5 (Y, Y) 23.7 15.0 99.8

[84] h4: KL loss in GRPO.

[85] p: In our RL training, we set the KL loss disabled for exploration and activated for exploitation. Here we train another two models with different settings, with the KL loss deactivated or activated all the time. The accuracy and language compliance results are shown in Table 8 , where KL loss has a less significant effect on performance and language compliance. As a result, the KL loss is not a decisive factor in our training pipeline, and one may adjust the settings according to the model’s use case.

[86] h3: 6.2 Analysis

[87] h4: Higher Response Diversity.

[88] p: The hypothesis that multilingual exploration extends the model’s available action space with more diverse responses can be validated by examining the policy entropy through the training course. Figure 3 compares the entropy of our model and the controlled baseline. During exploration (step 0-49), our model shows slower decay, keeping the entropy significantly higher than the controlled baseline. During exploitation (step 50-149), our model shows faster decaying in entropy, and the final entropy becomes lower than the baseline, indicating our exploitation method helps the model to efficiently converge to an optimized policy.

[89] figure: Figure 3: Policy entropy of ExpLang and the controlled baseline during the RLVR process.

[90] h4: Leveraged Non-English Advantage.

[91] p: Another hypothesis is that, for some training samples, the model actually performs better in certain non-English languages, but the advantage is hindered by the default English thinking mode. By enabling steady multilingual thinking, our method speeds up the learning process through leveraging the feedback of these responses. This hypothesis can be validated by examining the win-tie-lose rates in accuracy for non-English vs. English thinking on the training data. As shown in Figure 4 , for the original Qwen3-4B model, 21.62% of the non-English thinking responses show higher accuracy than English. After training, both the controlled baseline and the proposed model show reduced non-English win rate and increased English win-rate, indicating the potential advantage of non-English thinking has been leveraged and converted into the English reasoning ability. This phenomenon is stronger for our model than for the baseline, which supports the hypothesis that our method leverages the multilingual advantage more efficiently.

[92] figure: Figure 4: Win-Tie-Lose rate of non-English vs. English thinking, in terms of the average accuracy of the models on 2000 training samples, run for 5 times per sample.

[93] h2: 7 Conclusion and Discussion

[94] p: This paper proposes ExpLang, a novel training pipeline for LLM reasoning that enables multilingual exploration and exploitation with on-policy thinking language selection. Benefiting from higher response diversity and leveraged non-English advantage, our model shows steadily higher performance than the GRPO baselines on challenging reasoning datasets, while keeping its thinking language compliance near-perfect for seen languages and generalizable for unseen languages. Experiments show that our model goes through an “English-Multilingual-English” shift in thinking language preference, with the multilingual exploring stage playing the dominant role in the overall performance gain.

[95] p: Beyond GRPO, the ExpLang method is orthogonal to most of the advanced RLVR algorithms and techniques for LLMs. For example, since our method only requires adding batch-computed rewards, it can be conveniently applied to other GRPO-like algorithms, such as Dr. GRPO ( Liu et al., 2025 ) , DAPO ( Yu et al., 2025 ) , GSPO ( Zheng et al., 2025 ) , etc.. However, a complete set of comparison is computational expensive, and is beyond the scope of this paper. We will actively explore such possiblity in the future.

[96] h2: Potential Broader Impact

[97] p: This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

[98] h2: References

[99] h2: Appendix A Language Prefixes and Accept Rates

[100] p: Figure 6 shows the prefixes we use on the Qwen3-32B model and the baseline models to generate multilingual thinking traces. The accept rates is used only for Qwen3-32B for estimating the required inference samples so that the validated thinking traces count for about 500 per language.

[101] figure: Figure 5: Comparison of Cluster Counts After Spectral Clustering of English and Multilingual Thinking.

[102] h2: Appendix B Trajectory Diversity of Multilingual Thinking

[103] p: To further validate the advantage of multilingual thinking in enhancing reasoning trajectory diversity, we clustered the English and multilingual thinking outputs generated for AIME-2025 and OlymMATH en-easy, and quantified the number of resulting clusters as a measure of diversity. For each problem, 12 thinking samples were generated using Qwen3-32B. To minimize representation differences caused by multilingual expressions, we first summarize each thinking in a English text that captures its core reasoning. These summaries are embedded using Qwen3-Embedding-8B 8 8 8 https://huggingface.co/Qwen/Qwen3-Embedding-8B and clustered using spectral clustering, and the average number of clusters per dataset is calculated.

[104] p: As shown in Figure 5 , multilingual thinking consistently produces more clusters than English thinking: on AIME-2025, it produces on average 1.9 more clusters and on OlymMATH en-easy, 2.56 more clusters. These results indicate that multilingual thinking has greater potential to sample a richer set of reasoning trajectories compared to English thinking.

[105] figure: Figure 6: Prefixes and accept rates used in multilingual thinking data generation and forced multilingual thinking for baseline models.

[106] h2: Appendix C Budet and Hyper-Parameters

[107] h3: C.1 Hyper-parameters

[108] h4: LoRA hyper-parameters:

[109] p: We set the lora target to all linear modules, rank r = 8 r=8 , α = 16 \alpha=16 , cutoff length 8192, learning rate 1e-4, with cosine scheduler and warm-up ratio 0.1. The equivalent batch size is 32 with sequence packing. For the proposed model, LoRA tuning takes 82 steps. For the controlled baseline, LoRA tuning takes 106 steps, because English thinking lengths are longer for the same queries.

[110] h4: GRPO hyper-parameters:

[111] p: We set the maximum prompt length to 2048 and the maximum response length to 4096, learning rate 1e-6, total batch size 256, mini batch size 128 (meaning updating the policy model every 2 mini-batches), 51200 training samples in total. The rollout n is 8, and the kl loss coefficient is 0.001 if applicable. For the proposed model and the baselines, the GRPO training takes 200 ± \pm 3 steps.

[112] h3: C.2 Computational and Time Budget

[113] p: Generating high-quality multilingual thinking data with Qwen3-32B requires around 5 hours of inference with the VLLM framework 9 9 9 https://github.com/vllm-project/vllm on 8 × \times Nvidia-H200 GPUs, and the corresponding English baseline data requires about 8 hours.

[114] p: One run of LoRA SFT requires around 1.5 hours on 4 × \times Nvidia-A6000 GPUs, and one run of GRPO RLVR requires around 20 hours on 8 × \times Nvidia-H200 GPUs.

[115] p: One run of inference on the three testing sets takes around 2.5 hours for each setting (12 random runs for each testing sample) on 4 × \times Nvidia-A6000 GPUs.

[116] h2: Instructions for reporting errors

[117] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[118] p: Tip: You can select the relevant text first, to include it in your report.

[119] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[120] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
