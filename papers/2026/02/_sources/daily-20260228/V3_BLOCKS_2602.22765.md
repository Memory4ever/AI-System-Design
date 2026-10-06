[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Towards Better RL Training Data Utilization via Second-Order Rollout

[3] h6: Abstract

[4] p: Reinforcement Learning (RL) has empowered Large Language Models (LLMs) with strong reasoning capabilities, but vanilla RL mainly focuses on generation capability improvement by training with only first-order rollout (generating multiple responses for a question), and we argue that this approach fails to fully exploit the potential of training data because of the neglect of critique capability training. To tackle this problem, we further introduce the concept of second-order rollout (generating multiple critiques for a response) and propose a unified framework for jointly training generation and critique capabilities. Extensive experiments across various models and datasets demonstrate that our approach can utilize training data more effectively than vanilla RL and achieve better performance under the same training data. Additionally, we uncover several insightful findings regarding second - order rollout and critique training, such as the importance of label balance in critique training and the noise problem of outcome - based rewards, which can be mitigated through sampling techniques. Our work offers a preliminary exploration of dynamic data augmentation and joint generation - critique training in RL, providing meaningful inspiration for the further advancement of RL training.

[5] h2: 1 Introduction

[6] figure: Figure 1: A demonstration of first/second-order rollout. The policy model generates multiple responses for a question in first-order rollout, and generates multiple critiques for a response in second-order rollout.

[7] p: With the widespread application of Reinforcement Learning (RL) in post-training ( Guo et al., 2025 ) , Large Language Models (LLMs) have demonstrated remarkable reasoning capabilities, which inspires deeper investigations into RL training for LLMs. However, current RL training predominantly focuses on enhancing generation capability, often neglecting the development of critique capability, which can be a performance bottleneck for further improvement. Saunders et al. (2022) also categorizes model capabilities into Generation and Critique 1 1 1 The original classification delineates three distinct capabilities: Generation, Discrimination, and Critique. For simplicity, we subsume both Discrimination and Critique under the single term Critique. : (1) Generation refers to the ability to produce a correct response to a given question; (2) Critique denotes the capacity to judge whether a response is correct and to identify specific errors in a wrong response. Intuitively, these two capabilities are not independent: Wang et al. (2025c) finds that fine-tuning a model using only critique data, even without any explicit generation data, can significantly improve its generation performance. Similarly, better critique performance with only generation training is also witnessed by Wang et al. (2025b) . The neglect of critique training ( Yu et al., 2025b ; Xie et al., 2025 ) makes us wonder whether current RL training solely on generation capability can fully exploit the potential of training data, and we would like to further explore a joint RL training framework ( Ruan et al., 2025 ; Wang et al., 2025a ) for better data utilization.

[8] p: In § 3 we propose G eneration and C ritique RL ( GC-RL ) that jointly trains two capabilities with only generation training data by introducing the concept of second-order rollout . In vanilla RL, a policy model samples multiple responses for a given question during training, which we define as first-order rollout . Building on this, we further define second-order rollout as the process in which the policy model generates multiple critiques for a <question, response> pair, and these two processes are illustrated in Figure 1 . At each training step, we sample questions from the training set for first-order rollout and <question, response> pairs from a data cache for second-order rollout, and these rollout is then combined to update the policy model collectively. Meanwhile, responses generated from first-order rollout are filtered and added to the data cache for subsequent training. It is worth noting that the second-order rollout can proceed naturally based on the results of the first-order rollout, and no additional training data is required, which can be viewed as a "free lunch" to some extent.

[9] p: In § 4 , extensive experiments are conducted across different models and datasets, demonstrating that our GC-RL shows better data utilization and outperforms vanilla RL in both generation and critique capabilities under the same training data. Further we conduct more experiments to explore second-order rollout and critique training in § 2 and find: 1. the data filter is crucial for maintaining balanced critique training (§ 5.1 ); 2. outcome-based reward is noisy for critique training and denoising can be achieved through multiple samplings (§ 5.2 ); 3. static data performs better in critique-only training and dynamic data are more suitable for joint training (§ 5.3 ); 4. fine-grained model critique behavior manipulation can be achieved through reward function adjustment. (§ 5.4 ).

[10] p: Our contributions can be summarized as follows:

[11] p: We introduce the concept of second-order rollout and propose GC-RL framework, which achieves better RL training data utilization by generation-critique joint training.

[12] p: We conduct extensive experiments to show the effectiveness of our approach and draw some instructive conclusions about critique training.

[13] p: Our work offers a preliminary exploration of dynamic data augmentation in RL training, providing meaningful inspiration for further advancement of RL.

[14] h2: 2 Related Work

[15] h4: RL for LLMs

[16] p: The exceptional reasoning capabilities demonstrated by Deepseek-R1 ( Guo et al., 2025 ) highlight the significant role of RL ( Zhang et al., 2025 ) with verifiable reward in training LLMs. Beyond rule-based rewards, other forms such as model-based ( Xu et al., 2025 ; Shao et al., 2025 ) and rubric-based ( Gunjal et al., 2025 ; Huang et al., 2025 ) rewards can also be leveraged for RL training of LLMs. Another line of research focuses on developing RL algorithms suited for LLM training, including works like PPO ( Schulman et al., 2017 ) , GRPO ( Shao et al., 2024 ) , DAPO ( Yu et al., 2025a ) , and GSPO ( Zheng et al., 2025 ) . There are also works exploring new RL training tasks and objectives: for instance, She et al. (2025) employs RL to train models in reconstructing questions from responses, while Dong et al. (2025) applies RL to enhance next-token prediction. Different from previous works, our work explores better RL training utilization through joint training of generation and critique capabilities.

[17] h4: LLM Critique

[18] p: The ability to provide critique constitutes a crucial component of LLM capabilities. High-quality critiques enable LLMs to perform self-correction ( Pan et al., 2024 ; Yang et al., 2025b ; Yang et al., 2025a ) more effectively, and can also enhance the reward signals produced by reward models ( Yu et al., 2025c ; Ankner et al., 2024 ; Ye et al., 2025 ) when incorporated into the context. Sun et al. (2024) proposes a framework for evaluating the quality of critiques, while other research efforts have focused on improving critique abilities through Supervised Fine-Tuning ( Wang et al., 2025c ) , Direct Preference Optimization ( Yu et al., 2025b ) and RL ( Xi et al., 2025 ; Xie et al., 2025 ; Tang et al., 2025 ) . In contrast to prior work, our approach integrates critique training into the vanilla RL framework.

[19] figure: Figure 2: Flowchart of a single training step in GC-RL. First, a batch of questions is sampled from the training data, and multiple responses are generated (first-order rollout). Then, without replacement, a batch of <question, response> pairs is sampled from the Question-Response Data Cache , and multiple critiques are generated (second-order rollout). These rollouts are combined and utilized jointly to update the policy model. In addition, the Question-Response Data Cache is maintained by processing the first-order rollout through a Data Filter and adding the filtered data into the cache.

[20] h4: Data Augmentation

[21] p: Data augmentation ( Wang et al., 2024 ; Chai et al., 2026 ) is an effective approach to enhance model performance in LLM training. Techniques such as back translation ( Sennrich et al., 2016 ; Kulhánek et al., 2021 ) and rephrasing ( Lu and Lam, 2023 ) can enrich the dataset without altering semantic meanings. Alternatively, another augmentation strategy involves leveraging LLMs to generate new data in zero-shot ( Oh et al., 2023 ; Ubani et al., 2023 ) or in-context learning ( Dai et al., 2025 ) settings. Unlike conventional offline data augmentation methods, our work can be viewed as an online data augmentation process conducted in RL.

[22] h2: 3 Methodology

[23] p: We introduce G eneration and C ritique RL ( GC-RL ), an RL framework for jointly training the generation and critique capabilities, and the overview of our approach is illustrated in the figure 2 . At each RL training step, a batch of data is sampled from the initial training set, and the policy model generates multiple responses for each question (in conventional RL training, these responses would be directly used to update the policy model). We go further by feeding these <question, response> pairs into a data filter , retaining a subset to be stored in a question-response data cache . Then a batch of <question, response> pairs is sampled from the data cache, for which the policy model further generates critiques. The responses and critiques obtained from these two rollout processes are combined, assigned rewards and advantages, and utilized to update the policy model.

[24] h4: RL with Second-order Rollout

[25] p: For each question q i q_{i} in the training set D D , the policy model samples n n responses r 1 , r 2 , … , r n r_{1},r_{2},\dots,r_{n} during vanilla RL training, a process we refer to as first-order rollout . For a specific <question, response> pair ⟨ q i , r i ⟩ \langle q_{i},r_{i}\rangle , the policy model further samples n n critiques c 1 , c 2 , … , c n c_{1},c_{2},\dots,c_{n} for subsequent training, which we define as second-order rollout . In essence, the first-order rollout aims to enhance the generation capability, enabling model to produce appropriate answers to given questions. The second-order rollout is designed to improve critique capability, empowering it to identify potential issues or errors within a response. It is worth noting that the second-order rollout can proceed naturally based on the results of the first-order rollout, and no additional training data is required, which can be viewed as a "free lunch" to some extent.

[26] h4: Critique Data Filter

[27] p: During the RL training process, the <question, response> pairs obtained from the first-order rollout are passed through a Data Filter , which controls which pairs to retain. For a question q q and its corresponding responses r 1 , r 2 , … , r n r_{1},r_{2},\dots,r_{n} , if all n n responses are either entirely correct or entirely incorrect, all these data are discarded. Otherwise, one correct response r correct r_{\text{correct}} and one incorrect response r w ​ r ​ o ​ n ​ g r_{wrong} will be randomly selected, and these two resulting pairs ⟨ q , r c ​ o ​ r ​ r ​ e ​ c ​ t ⟩ \langle q,r_{correct}\rangle and ⟨ q , r w ​ r ​ o ​ n ​ g ⟩ \langle q,r_{wrong}\rangle will then stored in the data cache. Although simple, this data filter plays a crucial role in training stability, and removing this filter would introduce significant issues: (1). imbalance between critique data and generation data : for a single question q q , the first-order rollout produces n n responses and the second-order rollout further generates n 2 n^{2} critiques, and critique data outnumber generation data by a factor of n n ; (2). imbalance within critique data : we have observed that incorrect responses tend to dominate over correct ones in the first-order rollout, which can cause a label imbalance problem for further critique training, and further discussion is provided in § 5.1 .

[28] h4: Mixed Training

[29] p: During the update phase of the policy model, we perform training with a mixture of first-order rollout (responses) and second-order rollout (critiques). For each response r r , a rule-based verifier is employed to check its correctness, with the reward function defined as:

[30] table: R ⁡ ( r ) = { 1 , r is correct 0 , r is wrong R(r)=\begin{cases}1,&\textit{r is correct}\\ 0,&\textit{r is wrong}\end{cases} (1)

[31] p: For each critique c c generated based on <question,response> pair ⟨ q , r ⟩ \langle q,r\rangle , the final judgment regarding the correctness of r r is extracted, denoted as Ext ​ ( c ) ∈ { correct , wrong } \textit{Ext}(c)\in\{\textit{correct},\textit{wrong}\} . Since intermediate steps of a critique are hard to verify ( Sun et al., 2024 ) , we only assign an outcome reward based on the final binary judgment, and the corresponding reward function is:

[32] table: R ⁡ ( c ) = { 0.7 , Ext(c) = correct & R(r)=1 0.7 , Ext(c) = wrong & R(r)=0 0 , e ​ l ​ s ​ e R(c)=\begin{cases}0.7,&\textit{Ext(c) = correct \& R(r)=1}\\ 0.7,&\textit{Ext(c) = wrong \& R(r)=0}\\ 0,&else\end{cases} (2)

[33] p: For responses and critiques in the mixed rollout, the respective rewards are computed with the above reward functions. Then they are mixed into the same group to acquire advantages with GRPO ( Shao et al., 2024 ) algorithm for further update of policy model.

[34] h2: 4 Experiments

[35] h3: 4.1 Experimental Setup

[36] h4: Models

[37] p: Our experiments are primarily conducted on the Qwen2.5 series ( Yang et al., 2024 ) , including Qwen2.5 - (1.5B, 3B, 7B) - Base, to demonstrate the effectiveness of our method across models of varying scales. Additional experiments are performed on Llama-3.1-8B-Instruct ( Grattafiori et al., 2024 ) and Mistral-7B-Instruct-v0.3 ( Rastogi et al., 2025 ) to further validate the general applicability of our approach to different model architectures.

[38] h4: Dataset

[39] p: The training and evaluation mainly focus on mathematical reasoning tasks. DAPO - MATH - 17k ( Yu et al., 2025a ) is employed as the primary training dataset: 1k data are randomly selected to construct cold - start data, while the remaining 16k data are utilized for RL training. Several established mathematical reasoning benchmarks are utilized for evaluation, including Math - 500 ( Hendrycks et al., 2021 ) , GSM8k ( Cobbe et al., 2021 ) , Minerva ( Lewkowycz et al., 2022 ) , AMC23, and OlympiadBench ( He et al., 2024 ) .

[40] h4: Implementation Details

[41] p: We employ the verl 2 2 2 https://github.com/volcengine/verl framework for RL training and adopt GRPO ( Shao et al., 2024 ) algorithm, with training hyper - parameters detailed in the Appendix A .

[42] h3: 4.2 RL Training and Experimental Results

[43] h4: Cold Start

[44] p: Applying RL directly to models can lead to several issues: (1). Following the format of CFT ( Wang et al., 2025c ) , we instruct the model to append a correctness judgment of its response at the end of the critique. However, the base models exhibit weak instruction - following capability, often failing to generate critiques that adhere to the required format. (2). Due to their limited reasoning performance, the intermediate reasoning steps within the generated critiques are often of low quality. To address these problems, we first distill 1,885 initial critique data from GPT-5 3 3 3 gpt-5-chat-2025-08-07 , and the prompt used for critique distillation is provided in the Appendix A . After filtering out data with incorrect formatting or erroneous final judgments, we obtain 1,339 high - quality training examples. Before starting RL, we perform Supervised Fine - Tuning (SFT) on this curated critique dataset to equip the model with a preliminary critique capability.

[45] figure: Models Methods Math-500 GSM8k Minerva AMC23 Olympiad Avg Generation Accuracy (%) Qwen2.5-7B w/o RL 55.6 77.9 16.9 35.0 22.8 41.6 C-RL 65.1 83.7 19.2 47.5 26.1 48.3 G-RL 75.4 89.7 24.6 60.0 33.7 56.7 GC-RL 77.6 92.0 24.6 62.5 39.8 59.3 Qwen2.5-3B w/o RL 20.4 29.4 4.0 5.0 7.6 13.3 C-RL 30.4 50.0 4.4 12.5 11.0 21.7 G-RL 57.8 79.5 12.9 27.5 24.5 40.4 GC-RL 61.8 81.4 14.9 32.5 25.2 43.2 Qwen2.5-1.5B w/o RL 11.0 14.6 1.8 5.0 3.3 7.1 C-RL 21.3 25.6 3.6 10.0 5.9 13.3 G-RL 45.1 67.2 8.7 25.0 12.7 31.7 GC-RL 47.2 69.0 10.3 27.5 15.3 33.9 Critique Accuracy (%) Qwen2.5-7B C-RL 80.5 82.5 62.3 71.4 72.5 73.8 GC-RL 84.6 88.3 67.1 79.4 73.8 78.6 Qwen2.5-3B C-RL 67.4 66.7 57.1 64.7 61.2 63.4 GC-RL 70.2 72.8 57.1 66.2 61.5 65.6 Qwen2.5-1.5B C-RL 59.5 57.7 53.8 58.8 55.0 57.0 GC-RL 61.4 60.6 57.2 61.3 57.5 59.6 Table 1: Generation and critique capabilities evaluation results on Qwen-2.5-(1.5B,3B,7B). GC-RL outperforms all other RL training methods in both generation and critique capabilities.

[46] h4: Baselines

[47] p: In addition to presenting the evaluation results of our GC-RL (Generation and Critique RL) approach, we also provide the outcomes of several baseline methods: (1) after cold start without RL training; (2) G-RL (Generation RL): vanilla RL training that performs only first-order rollout to enhance generation capability; (3) C-RL (Critique RL): for each question, 10 responses are sampled in advance to construct a balanced training set consisting of <question, response> pairs, and only second-order rollout is performed to train critique capability of LLMs. All these RL training are performed under the same training data.

[48] h4: Critique Evaluation

[49] p: In addition to generation capability evaluation, we also try to examine the critique capability after RL training. To construct the evaluation dataset, we utilize 5 datasets in generation evaluation as seed data, and sample responses with Qwen2.5-(1.5B,7B,72B)-Instruct, respectively (10 responses for each model). The final answer is required to be enclosed in boxed {}, and we filter out responses that dissatisfy this format requirement, as well as questions for which all sampled responses are either entirely correct or entirely incorrect. From the remaining data, we randomly select one correct response and an incorrect one for each question, discarding all other responses, and this process yields critique evaluation datasets in which the correct and incorrect responses are 1:1. Since assessing the accuracy of the intermediate reasoning steps within a critique is particularly challenging, we focus solely on evaluating whether the final judgment of critique on the correctness of the response is accurate, which essentially reduces the task to a binary classification. We also report denoised reward (§ 5.2 ) to measure critique capability as supplemental results in Appendix B

[50] h4: Results

[51] p: The evaluation experiments are conducted on both generation and critique capabilities: For generation tasks, model-generated answers are verified by comparing them with reference answers and the final accuracy is reported; For critique tasks, we extract the generated final judgment on the correctness of a response and measure the binary classification accuracy. We show experimental results for Qwen-2.5-(1.5B,3B,7B) in Table 1 , and provide more results on Llama-3.1-8B-instruct and Mistral-7B-Instruct-v0.3 in Appendix B , finding that: 1. Even if a model is trained solely with C-RL (without generation training), its generation ability significantly improves—though such enhancement remains far inferior to that achieved through G-RL. 2. After training with GC-RL, the model attains optimal performance in both generation and critique capabilities. On one hand, its generation capability surpasses that of models trained with G-RL; on the other hand, its critique ability exceeds that of models trained with C-RL. This result suggests a certain coupling between critique and generation capabilities, and further demonstrates that joint training yields superior overall performance compared to training for each capability independently.

[52] h2: 5 Analysis

[53] figure: Math-500 GSM8k Minerva AMC23 Olympiad Avg Genration Random Sampling 75.0 90.9 22.9 60.0 37.5 57.3 Random Sampling + Reweight 77.2 91.5 23.2 60.0 38.2 58.0 Data Filter 77.6 92.0 24.6 62.5 39.8 59.3 Critique Random Sampling 82.3 84.0 63.3 73.5 71.6 74.9 Random Sampling + Reweight 83.7 86.7 65.8 77.9 72.8 77.4 Data Filter 84.6 88.3 67.1 79.4 73.8 78.6 Table 2: A comparison of model performance on Qwen2.5-7B when sampling responses with/without a data filter. Random sampling leads to the worst performance, though adding reward reweighting can alleviate this issue. Utilizing the data filter achieves the best performance.

[54] p: First-order rollout in RL training has been thoroughly studied by previous works, so we conduct a more detailed analysis of second-order rollout and critique training in this section. First, we discuss the label imbalance problem in critique training and demonstrate the effectiveness of our data filter both theoretically and experimentally (§ 5.1 ). Next, we discuss the reward noise problem in critique training and explore a sampling-based denoising strategy (§ 5.2 ). We then compare static and dynamic data in critique training, observing that dynamic data is more suitable for GC-RL, while static data works better for C-RL (§ 5.3 ). Finally, by adjusting the reward function, we achieve fine-grained critique behavior manipulation of LLMs after RL training (§ 5.4 ).

[55] h3: 5.1 Towards Balanced Critique Training

[56] p: We theoretically analyze why GC-RL without a data filter can lead to training data imbalance and restrict the critique capability of LLMs. To mitigate this problem, we explore employing a reward reweighting strategy and utilizing a data filter, and finally conduct comparative experiments to validate the effectiveness of our data filter.

[57] h4: Alleviating imbalance problem with reward reweighting

[58] p: The ultimate judgement of whether a response is correct or not in a critique is essentially a binary classification task, but the number of erroneous responses significantly outweighs the correct ones in the first-order rollout. Intuitively, this label imbalance problem can impact subsequent critique training, and we also theoretically analyze the effect of data imbalance on the performance of the critique training, with detailed discussions shown in Appendix C . To mitigate this problem, we also explore reweighting and scaling rewards for positive and negative data to balance their contributions, and the weighted reward function is defined as:

[59] table: R w ​ ( c ) = { 0.35 E ⁡ [ R ⁡ ( r ) ] , Ext(c) = correct & R(r)=1 0.35 1 − E ⁡ [ R ⁡ ( r ) ] , Ext(c) = wrong & R(r)=0 0 , e ​ l ​ s ​ e R_{w}(c)=\begin{cases}\frac{0.35}{E[R(r)]},&\textit{Ext(c) = correct \& R(r)=1}\\ \frac{0.35}{1-E[R(r)]},&\textit{Ext(c) = wrong \& R(r)=0}\\ 0,&else\end{cases} (3)

[60] p: where E ⁡ [ R ⁡ ( r ) ] E[R(r)] is the expected reward for response r r during RL training. It can be mathematically proved that the weighted reward is unbiased and does not incentivize the model to judge an uncertain response as correct or wrong, and the detailed proof is shown in Appendix C . Essentially, this weighting strategy amplifies the reward for rare classes, enabling the model to learn more effectively from such data and thereby approximating balanced training.

[61] h4: Empirical comparison of training with/without a data filter

[62] p: Comparison experiments are conducted on Qwen2.5-7B with GC-RL training under three settings: (1) randomly sampling responses without data filter, (2) randomly sampling responses and training with the weighted reward function in Equation 3 , and (3) utilizing the data filter in § 3 . As the experimental results shown in Table 2 , random sampling strategy leads to the worst generation and critique capabilities because of label imbalance, and this problem can be alleviated to some extent with a weighted reward function. Although reward weighting can achieve balance in the reward level for imbalanced data, utilizing a data filter can achieve inherently balanced training data and yield the best performance.

[63] h3: 5.2 Reward Noise & Denoising in Critique RL

[64] h4: Reward noise problem in critique RL

[65] p: Obtaining precise rewards for critiques is more challenging than for responses. For instance, in mathematical problems, since we have a corresponding answer to each question, the correctness of a response can be easily rule-based verified and a precise reward can then be assigned accordingly. However, for critiques, it is difficult to verify the correctness of each intermediate step, and we can only assign rewards based on whether the final binary classification result is correct. Generating responses is essentially a generation task, and it is rare for a model to produce intermediate errors yet still arrive at the correct final answer. In contrast, generating critiques is essentially a binary classification task, and even random guessing can yield correct answers with a 50% probability, leading to many critiques with incorrect intermediate steps but correct final judgement. Ideally, for critiques with correct outcomes, we should differentiate between those with erroneous intermediate steps and those with correct ones, assigning lower and higher rewards, respectively. However, verifying intermediate steps is challenging in practice, so critiques with correct results are often given the same reward, and we refer to such rewards as noised rewards . Guo et al. (2025) has demonstrated significant success in Reinforcement Learning with Verifiable Rewards (RLVR), which fundamentally relies on oracle rewards . Liu et al. (2025) ; Shi and Jin (2025) ; Whitehouse et al. (2025) also attempt RL on classification tasks, showing that even with noised rewards , model performance can be improved to some extent, which is also witnessed by our experiments in § 4 .

[66] figure: Figure 3: A comparison of model performance of Qwen2.5-7B with/without reward denoising strategy on Math-500. In both GC-RL and C-RL settings, reward denoising can improve model performance on both generation and critique capabilities.

[67] h4: Exploring critique reward denoising based on self-correction with multiple samplings

[68] p: In LLM self-correction process ( Kamoi et al., 2024 ; Pan et al., 2024 ) , a model is provided with three components: <question, response, critique>, and then instructed to modify the original response based on the potential issues identified by the critique and generate a refined response. Intuitively, the higher the quality of the critique—i.e., the more accurately it identifies problems in the original response—the greater the likelihood that the refined response will be correct. Thus, we can inversely estimate the quality of a critique based on the quality of its corresponding refined response. Similar to ( Tang et al., 2025 ; Xie et al., 2025 ; Yu et al., 2025b ) , for a given critique, we allow the model to perform self-correction and sample n n refined responses, with the number of correct ones denoted as k k , based on which we then propose the following reward function to estimate critique quality:

[69] table: R q ​ ( c ) = { 0.1 ∗ k n , Ext(c) == correct 0.7 ∗ k n , Ext(c) == wrong R_{q}(c)=\begin{cases}0.1*\frac{k}{n},&\textit{Ext(c) == correct}\\ 0.7*\frac{k}{n},&\textit{Ext(c) == wrong}\end{cases} (4)

[70] p: Although it is difficult to directly verify the correctness of intermediate steps in critique, this sampling method can indirectly estimate it to some extent, thereby reducing noise in the reward. We utilize the sum of the outcome reward from Equation 2 and the estimated reward obtained from Equation 4 , denoted as R ​ ( c ) + R q ​ ( c ) R(c)+R_{q}(c) , as the final reward for critique, and compare it with using only the outcome reward R ⁡ ( c ) R(c) . Theoretically, a larger number of samples n n leads to better noise reduction and more accurate reward values, but at a higher computational cost. To make the computational overhead controllable, experiments are conducted with n = 1 n=1 , and the experimental results on Math-500 are shown in Figure 3 (with more results shown in Figure 9 in Appendix B ). A performance improvement in both generation and critique capabilities can be witnessed under both CG-RL and C-RL settings with our reward denoising strategy.

[71] h3: 5.3 Static v.s. Dynamic Data

[72] h4: A comparison of static and dynamic responses during critique RL training.

[73] p: In our approach, dynamic self-generated responses are utilized when generating second-order rollout, and an alternative strategy involves utilizing static responses ( Ruan et al., 2025 ; Xie et al., 2025 ) for critique RL training, where pre-prepared <question, response> pairs remain fixed throughout the RL process. A performance comparison of static and dynamic training data is conducted under GC-RL and C-RL settings for both generation and critique capabilities on Qwen2.5-7B, and the experimental results on Math-500 are presented in Figure 4 (with more results shown in Figure 7 in Appendix B ). We find that training with dynamically self-generated response data leads to higher performance in both generation and critique capabilities under GC-RL setting. However, under C-RL setting, where responses are abandoned and only critiques are utilized to update the policy model, dynamic data suffers from a severe reward hacking problem, and the static data strategy significantly outperforms the dynamic data. With dynamic data, the model seems to identify a shortcut to maximize rewards during RL: it deliberately generates incorrect responses in the generation stage (though producing a correct response is challenging, generating an incorrect one can be quite easy), then it labels all responses as incorrect to get the reward in the critique stage. To summarize, dynamic data is more suitable for GC-RL training, while static data is more appropriate for C-RL training.

[74] figure: Figure 4: Performance of Qwen2.5-7B on Math-500 under GC-RL and C-RL settings with static and dynamic critique training data. Dynamic data outperforms static data in the GC-RL setting, while the opposite holds for C-RL.

[75] h3: 5.4 Fine-grained Critique Behavior Manipulation

[76] p: There are often different requirements for the binary classification performance in different scenarios. For instance, a higher recall rate is demanded in disease screening, while a higher precision rate is required in recommendation systems. In the reward function defined in Equation 2 , the same reward is assigned to both correct and incorrect responses as long as the critique identifies them correctly, and we also explore training with more fine-grained reward functions to better control the critique behavior of LLMs. For example, to encourage the model to be more inclined to classify a response as incorrect when it is uncertain, we try the following reward function:

[77] table: R w ​ ( c ) = { 0.6 , Ext(c) = correct & R(r)=1 0.8 , Ext(c) = wrong & R(r)=0 0 , e ​ l ​ s ​ e R_{w}(c)=\begin{cases}0.6,&\textit{Ext(c) = correct \& R(r)=1}\\ 0.8,&\textit{Ext(c) = wrong \& R(r)=0}\\ 0,&else\end{cases} (5)

[78] p: Conversely, to steer the model toward classifying uncertain responses as correct, we assign a large reward value to correct responses and employ the following reward function:

[79] table: R r ​ ( c ) = { 0.8 , Ext(c) = correct & R(r)=1 0.6 , Ext(c) = wrong & R(r)=0 0 , e ​ l ​ s ​ e R_{r}(c)=\begin{cases}0.8,&\textit{Ext(c) = correct \& R(r)=1}\\ 0.6,&\textit{Ext(c) = wrong \& R(r)=0}\\ 0,&else\end{cases} (6)

[80] p: The experimental results on Math-500 of utilizing R w ​ ( c ) R_{w}(c) and R r ​ ( c ) R_{r}(c) are presented in Figure 5 , and more results can be found in Figure 8 in Appendix B ). Compared with the baseline R ⁡ ( c ) R(c) , we observe that when R w ​ ( c ) R_{w}(c) is applied, the model achieves higher precision but lower recall; whereas with R r ​ ( c ) R_{r}(c) , the precision decreases while recall increases. By adjusting the reward function, we can exert finer-grained control over the critique behavior of LLMs.

[81] figure: Figure 5: A comparison of critique performance of Qwen2.5-7B with different reward function on Math-500. Compared to baseline R ⁡ ( c ) R(c) , R w ​ ( c ) R_{w}(c) leads to a higher precision while R r ​ ( c ) R_{r}(c) generates a higher recall.

[82] h2: 6 Conclusion

[83] p: Based on the first-order rollout in vanilla RL (generating multiple responses for a question), we further introduce the concept of second-order rollout (generating multiple critiques for a response) and propose GC - RL, a unified framework to train generation and critique capabilities jointly. Extensive experiments across various models and datasets demonstrate that our approach can more effectively utilize training data compared to vanilla RL, achieving superior performance under the same training data. Additionally, we uncover some insightful findings related to second - order rollout and critique training, such as the importance of label balance in critique training. Our work serves as an initial exploration into dynamic data augmentation and joint training of generation and critique in RL training, offering meaningful insights for further advancements in RL for LLMs.

[84] h2: Limitations

[85] p: Our work represents a preliminary attempt to integrate dynamic data augmentation with joint training of generation and critique into RL, and still exhibits several limitations that warrant further exploration. For simplicity, we only employ the GRPO algorithm for RL training, and the applicability of our approach to other RL algorithms (such as PPO) remains to be investigated. Moreover, experiments are confined to the mathematical domain using models with fewer than 10B parameters, and extending our approach to larger-scale RL training with multi-domain training data and larger models is considered to be an important direction for future work. Additionally, we have observed that our approach converges more slowly compared to vanilla RL, essentially trading computational resources for improved performance. Our approach also requires that responses can be rule-based verified, making it less straightforward to apply to RL tasks where responses are harder to evaluate (e.g., rubric-based RL training ( Gunjal et al., 2025 ; Huang et al., 2025 ) ). How to perform second-order rollout and assign rewards to critiques in such settings is also worth further exploration.

[86] h2: Ethical Considerations

[87] p: The data utilized are open for research, and LLMs in the experiments are all publicly available by either parameters or API calls. Therefore, we do not anticipate any ethical concerns in our research.

[88] h2: References

[89] h2: Appendix

[90] h2: Appendix A More Implementation Details

[91] p: We provide more implementation details in this section. We show the prompt utilized for cold start data distillation in Figure 6 . We show some hyper-parameters in RL training in Table 3 .

[92] figure: Prompt for Critique Data Distillation #Question#: <insert question> #Solution#: <insert question> #Instruction#: Please verify step by step and judge whether the solution is correct, and end your answer with **Conclusion: right/wrong [END]** Figure 6: Our prompt fed to GPT-5 for critique data generation, which is comprised of a question, a solution, and critique instruction.

[93] figure: train bath size 512 ppo mini batch size 128 rollout n 5 adv estimator grpo kl loss coef 1e-3 learning rate 1e-6 max prompt length 4096 max response length 4096 clip ratio 0.2 epochs 10 Table 3: RL training hyper-parameters.

[94] h2: Appendix B More Experimential Results

[95] p: We show more experimental results in this section. Main experiments on Mistral-7B-Instruct-v0.3 and Llama-3.1-8B-Instruct are shown in Table 4 . Supplemental critique capability evaluation results are shown in Table 5 . Performance comparison of static and dynamic critique training data is shown in Figure 7 ; performance comparison of different reward functions is shown in Figure 8 ; performance comparison of training with/without reward denoising strategy is shown in Figure 9 .

[96] h2: Appendix C Discussions on Label Imbalance Problem

[97] h4: A theoretical analysis of data imbalance problem in critique training without the data filter.

[98] p: Theoretically, generating a critique can be viewed as a binary classification task, requiring the critique to include a final judgment on whether the response is correct or not, and binary classification tasks are susceptible to label distribution imbalance in the training data: when one category predominates, the trained model tends to favor predicting that category. In § 3 , the data processed through the first-order rollout and subsequently filtered by a data filter are stored in the Question-response Data Cache to support subsequent critique RL training, and this data filter ensures a 1:1 ratio between correct and incorrect responses, thereby preventing label bias in subsequent critique training. If the data filter is omitted and responses are sampled uniformly at random, in the first-order rollout, E ⁡ [ R ⁡ ( r ) ] × 100 % E[R(r)]\times 100\% of responses are correct and ( 1 − E ⁡ [ R ⁡ ( r ) ] ) × 100 % (1-E[R(r)])\times 100\% are incorrect, where E E denotes the mathematical expectation. Consequently, the ratio of correct to incorrect responses under random sampling is also E ⁡ [ R ⁡ ( r ) ] : ( 1 − E ⁡ [ R ⁡ ( r ) ] ) E[R(r)]:(1-E[R(r)]) . Similar to Yang et al. (2025b) , let P 1 P_{1} and P 2 P_{2} denote the probabilities that the model correctly identifies correct and wrong responses, respectively, during the critique phase. On a validation set with a balanced 1:1 positive-to-negative ratio, the expected validation reward is E ⁡ [ R v ​ a ​ l ​ ( c ) ] = 0.7 ​ P 1 + 0.7 ​ P 2 2 E[R_{val}(c)]=\frac{0.7P_{1}+0.7P_{2}}{2} , and the expected reward for critiques during RL training is:

[99] table: E ⁡ [ R ⁡ ( c ) ] \displaystyle E[R(c)] (7) = E ⁡ [ R ⁡ ( r ) ] ∗ P 1 ∗ 0.7 + ( 1 − E ⁡ [ R ⁡ ( r ) ] ) ∗ P 2 ∗ 0.7 \displaystyle=E[R(r)]*P_{1}*0.7+(1-E[R(r)])*P_{2}*0.7 = 0.7 ​ E ​ [ R ⁡ ( r ) ] ​ P 1 \displaystyle=0.7E[R(r)]P_{1} + ( 1 − E ⁡ [ R ⁡ ( r ) ] ) ​ ( 2 ​ E ​ [ R v ​ a ​ l ​ ( c ) ] − 0.7 ​ P 1 ) \displaystyle+(1-E[R(r)])(2E[R_{val}(c)]-0.7P_{1}) = 0.7 ​ ( 2 ​ E ​ [ R ⁡ ( r ) ] − 1 ) ​ P 1 \displaystyle=0.7(2E[R(r)]-1)P_{1} + 2 ​ ( 1 − E ⁡ [ R ⁡ ( r ) ] ) ​ E ​ [ R v ​ a ​ l ​ ( c ) ] \displaystyle+2(1-E[R(r)])E[R_{val}(c)]

[100] p: Though E ⁡ [ R ⁡ ( r ) ] E[R(r)] and E ​ [ R v ​ a ​ l ​ ( c ) ] E[R_{val}(c)] gradually improve throughout the whole RL training process, they can be approximately viewed as constants between adjacent RL steps. From this point of view and Equation 7 , we can see that the expected critique reward is in proportion to P 1 P_{1} . Similar to Yang et al. (2025b) , P 1 P_{1} and P 2 P_{2} also exhibit a competitive trade-off and P 1 + P 2 P_{1}+P_{2} can be viewed as a constant between adjacent RL steps. When 2 ​ E ​ [ R ⁡ ( r ) ] − 1 > 0 2E[R(r)]-1>0 , this reward encourages the model to increase P 1 P_{1} and decrease P 2 P_{2} ; when 2 ​ E ​ [ R ⁡ ( r ) ] − 1 < 0 2E[R(r)]-1<0 , a decrease in P 1 P_{1} raises the expected reward, thereby incentivizing the model to reduce P 1 P_{1} and increase P 2 P_{2} . For example, when training Qwen2.5-7B with GC-RL in § 4 , we find E ⁡ [ R ⁡ ( r ) ] ≈ 0.1 E[R(r)]\approx 0.1 in early training and E ⁡ [ R ⁡ ( r ) ] ≈ 0.45 E[R(r)]\approx 0.45 in late stage, consistently satisfying 2 ​ E ​ [ R ⁡ ( r ) ] − 1 < 0 2E[R(r)]-1<0 and incentivizing the model to decrease P 1 P_{1} . Consequently, a model trained with randomly sampled responses for second-order rollout exhibits lower P 1 P_{1} and higher P 2 P_{2} , meaning it tends to classify responses as incorrect during critique.

[101] h4: The weighted reward function is unbiased

[102] p: We give a proof of the unbiasedness of the following weighted reward function:

[103] table: R w ​ ( c ) = { 0.35 E ⁡ [ R ⁡ ( r ) ] , Ext(c) = correct & R(r)=1 0.35 1 − E ⁡ [ R ⁡ ( r ) ] , Ext(c) = wrong & R(r)=0 0 , e ​ l ​ s ​ e R_{w}(c)=\begin{cases}\frac{0.35}{E[R(r)]},&\textit{Ext(c) = correct \& R(r)=1}\\ \frac{0.35}{1-E[R(r)]},&\textit{Ext(c) = wrong \& R(r)=0}\\ 0,&else\end{cases} (8)

[104] p: Under this scheme, the expected reward for critiques during RL training becomes:

[105] table: E ⁡ [ R ⁡ ( c ) ] \displaystyle E[R(c)] (9) = E ⁡ [ R ⁡ ( r ) ] ​ P 1 ​ 0.7 2 ​ E ​ [ R ⁡ ( r ) ] \displaystyle=E[R(r)]P_{1}\frac{0.7}{2E[R(r)]} + ( 1 − E ⁡ [ R ⁡ ( r ) ] ) ​ P 2 ​ 0.7 2 ​ ( 1 − E ​ [ R ​ ( r ) ] ) \displaystyle+(1-E[R(r)])P_{2}\frac{0.7}{2(1-E[R(r)])} = 0.7 ​ P 1 + 0.7 ​ P 2 2 \displaystyle=\frac{0.7P_{1}+0.7P_{2}}{2} = E ​ [ R v ​ a ​ l ​ ( c ) ] \displaystyle=E[R_{val}(c)]

[106] p: Under these circumstances, the reward does not incentivize the model to increase or decrease P 1 P_{1} or P 2 P_{2} . Essentially, this weighting strategy amplifies the reward for rare classes, enabling the model to learn more effectively from such examples and thereby approximating balanced training.

[107] figure: Models Methods Math-500 GSM8k Minerva AMC23 Olympiad Avg Generation Accuracy (%) Mistral-7B-Instruct-v0.3 w/o RL 10.8 46.7 7.4 5.0 1.8 14.3 C-RL 19.8 54.2 9.8 12.5 4.2 20.1 G-RL 47.6 77.8 18.6 30.0 15.6 37.9 GC-RL 52.1 81.2 19.4 32.5 17.9 40.6 Llama-3.1-8B-Instruct w/o RL 48.2 84.2 19.1 25.0 15.0 38.3 C-RL 55.6 87.6 21.3 32.5 20.1 43.4 G-RL 72.3 92.0 28.9 47.5 28.4 53.8 GC-RL 75.8 92.6 30.1 50.0 31.6 56.0 Critique Accuracy (%) Mistral-7B-Instruct-v0.3 C-RL 65.2 70.1 60.3 66.4 63.2 65.0 GC-RL 69.0 74.8 64.5 71.6 66.1 69.2 Llama-3.1-8B-Instruct C-RL 77.8 80.5 58.3 70.4 67.3 70.9 GC-RL 81.4 83.2 64.1 75.4 70.6 74.9 Table 4: Generation and critique capabilities evaluation results on Mistral-7B and Llama3.1-8B-Instruct. GC-RL outperforms all other RL training methods in both generation and critique capabilities.

[108] figure: Models Methods Math-500 GSM8k Minerva AMC23 Olympiad Avg Denoised Reward Qwen2.5-7B C-RL 0.901 0.912 0.715 0.797 0.812 0.827 GC-RL 0.945 0.986 0.774 0.852 0.836 0.879 Qwen2.5-3B C-RL 0.752 0.754 0.652 0.699 0.691 0.710 GC-RL 0.774 0.802 0.657 0.712 0.698 0.729 Qwen2.5-1.5B C-RL 0.651 0.638 0.607 0.648 0.612 0.631 GC-RL 0.683 0.676 0.658 0.672 0.635 0.665 Table 5: Supplemental critique capability evaluation results on Qwen-2.5-(1.5B,3B,7B). The average denoised reward (§ 5.2 ) is also reported to reflect the critique capability.

[109] figure: Figure 7: Performance of Qwen2.5-7B on 4 datasets under GC-RL and C-RL settings with static and dynamic critique training data. Dynamic data outperforms static data in the GC-RL setting, while the opposite holds for C-RL.

[110] figure: Figure 8: A comparison of critique performance of Qwen2.5-7B with different reward functions on 4 datasets. Compared to baseline R ⁡ ( c ) R(c) , R w ​ ( c ) R_{w}(c) leads to a higher precision while R r ​ ( c ) R_{r}(c) generates a higher recall.

[111] figure: Figure 9: A comparison of model performance of Qwen2.5-7B with/without reward denoising strategy on 4 datasets. In both GC-RL and C-RL settings, reward denoising can improve model performance on both generation and critique capabilities.

[112] h2: Instructions for reporting errors

[113] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[114] p: Tip: You can select the relevant text first, to include it in your report.

[115] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[116] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
