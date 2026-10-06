# Exact-v1 minimum primary: 2601.09028

Source: https://arxiv.org/html/2601.09028v1 . Only selected necessary method/evaluation/counterevidence; full fetched body is not a whole-paper review.

## Raw body offsets 18777–28172

3.2. Constructing Indicators via Extracting Features from External Information
Our goal is to incorporate external explicit indicators for LLMs to utilize internal knowledge stored in their parameters. Thus, the first step is to construct the indicators by extracting quality features from the retrieved information.
The most intuitive feature is the relevant score computed by the retriever model in terms of the given query and candidate documents.
In general, the retrieved top-k relevant documents {dociq}i=1k\{\text{doc}_{i}^{q}\}_{i=1}^{k} for the query qq are associated with their relevance scores 𝒮Ret={siRet}i=1k\mathcal{S}^{\text{Ret}}=\{s_{i}^{\text{Ret}}\}_{i=1}^{k}, each computed by a similarity function as siRet=q⋅dociq‖q‖​‖dociq‖s_{i}^{\text{Ret}}=\frac{\text{q}\cdot\text{doc}_{i}^{q}}{\|\text{q}\|\,\|\text{doc}_{i}^{q}\|}.
Since external indicators can be constructed in multiple ways, different features may be extracted and computed depending on the specific requirements, such as for faithfulness or trustworthiness.
In our implementation, we further leverage two additional indicators features, (i) the relevance judged by a LLM-based ranker as 𝒮Rank={siRank}i=1k\mathcal{S}^{\text{Rank}}=\{s_{i}^{\text{Rank}}\}_{i=1}^{k}; and (ii) the query performance prediction (QPP) score 𝒮QPP\mathcal{S}^{\text{QPP}} judged by a QPP model (34).
Specifically, we use the logit of the end-of-sequence token for the LLM-ranker judged score as siRank=Ranker​(q,dociq)​[−1]s_{i}^{\text{Rank}}=\text{Ranker}(\text{q},\text{doc}_{i}^{q})[-1] following (32), and the logit of token “relevant” in the prediction of the QPP model for each given document dociq\text{doc}_{i}^{q} in the candidate list as siQPP=logit​(“relevant”∣(q,dociq))s_{i}^{\text{QPP}}=\text{logit}\!\left(\text{``relevant''}\mid(q,\text{doc}_{i}^{q})\right).
The relevance judged by the LLM-based ranker is expected to provide semantic similarity features from another perspective and help to investigate whether these explicit LLM-judged signals have additional impacts or have been integrated in model internal processing implicitly. Besides, the QPP scores provide the indicators about the difficulty of the query, which might imply the possible noisy level of the retrieved information for the generator.
Eventually, these scores calculated based on different aspects are used individually or as a combination SaggS^{\text{agg}} by an aggregation function to guide the LLMs to process the external information during generation, i.e., to decide to what extent it should focus on different parts of the input context in decoding.
3.3. Learning to Leverage Explicit Indicators Features for Decoding
The fundamental problem in the current paradigm of RAG is that adding external retrieved information in the input prompt could only affect the online computation of key-value pairs in the attention networks of LLMs, which is not tailored to the input with noise.
Since the retrieved context is usually not perfect, the inherent defects are only implicitly processed via the attention score computation, which is influenced by the mechanisms (e.g., predefined system prompt) in the pre-training procedure.
Thus, a better way is to inform the decoding with additional explicit indicators directly, so that the LLMs know how much they should rely on external or internal knowledge to generate an answer.
To this end, we aim to teach the model to leverage the explicit indicator features from external information generated in Sec. 3.2, and integrate them into the original attention networks computation.
Following the procedure of the standard RAG, the user query qq and its corresponding retrieved top-k documents ℛ⁡(q)={dociq}i=1k\mathcal{R}(q)=\{\text{doc}_{i}^{q}\}_{i=1}^{k} would fill the prompt template together with the instruction as [Instruction,doc1q,doc2q,⋯,dockq,query][\text{Instruction},\text{doc}_{1}^{q},\text{doc}_{2}^{q},\cdots,\text{doc}_{k}^{q},\text{query}] to instruct the LLM to produce an answer.
To teach the LLMs to leverage explicit indicator features, we first construct a score distribution by concatenating any types of score {si}i=1k\{s_{i}\}_{i=1}^{k} as features of the top-k retrieved documents and the pre-defined score sIs_{I} and sqs_{q} for the instruction ℐ\mathcal{I} and query qq as S=[sI,s1,s2,⋯,sk,sq]S=[s_{I},s_{1},s_{2},\cdots,s_{k},s_{q}].
Then, we initialize it by normalizing the feature scores of the retrieved documents {si}i=1k\{s_{i}\}_{i=1}^{k} to [0,1][0,1]
and assign score 11 to the tokens in query and instruction as Eq. 2.
The constructed score distribution Snorm∈ℝ|S|×|S|S_{\text{norm}}\in\mathbb{R}^{|S|\times|S|} is a token-level matrix, i.e., each token has an initial score value.
Finally, we incorporate the normalized scores SnormS_{\text{norm}} as explicit indicators into the computation of attention networks in OpenDecoder modified according to relevance as θopenattn\theta_{\text{open}}^{\text{attn}} via Eq. 3.
The intuition is that, by modulating the original attention scores with normalized indicator scores, the importance of each token during the autoregressive decoding would be reshaped to guide the model for answer generation.
In extreme cases where all input documents are irrelevant and assigned very low relevance scores, the query and instruction receive relatively higher scores, guiding the model to disregard the retrieved context and instead rely on its parametric knowledge to generate an answer.
Algorithm 1  Modulating LLM internal decoding in OpenDecoder
              0:
             Question qq,
Relevance score {si}i=1k\{s_{i}\}_{i=1}^{k} of each input document, Normalization function Norm​(⋅)\text{Norm}(\cdot), Original ℒ​ℒ​ℳθ0\mathcal{LLM}_{\theta_{0}}.
              0:
             Updated ℒ​ℒ​ℳθ0+θopenattn\mathcal{LLM}_{\theta_{0}+\theta_{\text{open}}^{\text{attn}}} and generated answer aa.
              1:
             Normalize the relevance score among the input documents {sinorm}i=1k=Norm​({si}i=1k)\{s_{i}^{\text{norm}}\}_{i=1}^{k}=\text{Norm}(\{s_{i}\}_{i=1}^{k}).
              2:
             Construct token-level score matrix Snorm∈ℝ|S|×|S|S_{\text{norm}}\in\mathbb{R}^{|S|\times|S|} correspond to the input with question qq and instruction as Eq. 2.
              3:
             Computation of modulated LLM’s internal attention network ℒ​ℒ​ℳθ0\mathcal{LLM}_{\theta_{0}} with external relevance score SnormS_{\text{norm}} via new parameter θopenattn\theta_{\text{open}}^{\text{attn}} as Eq. 3.
              4:
             Generate a final answer aa for qq via the updated ℒ​ℒ​ℳθ0+θopenattn\mathcal{LLM}_{\theta_{0}+\theta_{\text{open}}^{\text{attn}}}.
(2)
sinorm\displaystyle s_{i}^{\text{norm}}
=simax⁡({sj}j=1k),sqnorm,sInorm←1\displaystyle=\frac{s_{i}}{\max(\{s_{j}\}_{j=1}^{k})},\quad s_{q}^{\text{norm}},s_{I}^{\text{norm}}\leftarrow 1
Snorm\displaystyle S_{\text{norm}}
=[sInorm,{sjnorm}1k,sqnorm]∈ℝ|S|×|S|\displaystyle=[s_{I}^{\text{norm}},\{s_{j}^{\text{norm}}\}_{1}^{k},s_{q}^{\text{norm}}]\in\mathbb{R}^{|S|\times|S|}
(3)
θopenattn∼Attn​(Q,K,V,Snorm)=softmax​(Snorm⋅Q​K⊤dk)​V\theta_{\text{open}}^{\text{attn}}\sim\text{Attn}(Q,K,V,S_{\text{norm}})=\text{softmax}\left(\frac{S_{\text{norm}}\cdot QK^{\top}}{\sqrt{d_{k}}}\right)V
The type of scores and normalization approach can be determined according to various criteria such as relevance, reliability, authority, etc. In our implementation, we investigate three types of scores through an aggregation function before the normalization. We expect the relevance score 𝒮Ret\mathcal{S}^{\text{Ret}} to be dominant and the other two scores 𝒮Rank\mathcal{S}^{\text{Rank}} and 𝒮QPP\mathcal{S}^{\text{QPP}} act as supplementary with a scale constant 0.50.5, which is formulated in Eq. 4.
(4)
Snormagg\displaystyle S_{\text{norm}}^{\text{agg}}
=Normalize​(Aggregate​(𝒮Ret,𝒮Rank,𝒮QPP)),where\displaystyle=\text{Normalize}\left(\text{Aggregate}(\mathcal{S}^{\text{Ret}},\mathcal{S}^{\text{Rank}},\mathcal{S}^{\text{QPP}})\right),\text{where}
si−aggnorm\displaystyle s_{i-\text{agg}}^{\text{norm}}
=(si−Retnorm+0.5∗(si−Ranknorm+si−QPPnorm))max({sjRet+0.5∗(sjRank+sjOPENQPP)}j=1k),si−aggnorm∈Snormagg\displaystyle=\frac{\left(s_{i-\text{Ret}}^{\text{norm}}+0.5*(s_{i-\text{Rank}}^{\text{norm}}+s_{i-\text{QPP}}^{\text{norm}})\right)}{\max(\{s_{j}^{\text{Ret}}+0.5*(s_{j}^{\text{Rank}}+s_{j}^{\text{QPP})}\}_{j=1}^{k})},\ s_{i-\text{agg}}^{\text{norm}}\in S_{\text{norm}}^{\text{agg}}
Finally, we optimize to maximize the probability of producing the ground-truth aa with the given query and its corresponding retrieved top-kk documents set {doc}1k\{\text{doc}\}_{1}^{k} as Eq. 5, where θ0\theta_{0} and θopenattn\theta_{\text{open}}^{\text{attn}} denote the LLMs’ original parameters and the learned parameters to leverage explicit quality indicator features during fine-tuning, respectively. During inference, the corresponding quality indicator features {si}i=1k\{s_{i}\}_{i=1}^{k} are required by learned parameters θopenattn\theta_{\text{open}}^{\text{attn}} for computation of probability in Eq. 3. The core procedure of the information processing within the OpenDecoder is described in Algorithm 1.
(5)
maxθ∑(q,{doc}1k,a)∑t=1|a|log(Pθ0+θopenattn(at|a<t,q,{doc}1k))\max_{\theta}\sum_{(q,\{\text{doc}\}_{1}^{k},a)}\sum_{t=1}^{|a|}\log\left(P_{\theta_{0}+\theta_{\text{open}}^{\text{attn}}}(a_{t}|a_{<t},q,\{\text{doc}\}_{1}^{k})\right)


## Raw body offsets 28172–29300

3.4. Robustness Training
It may often be the case that some retrieved documents are not relevant.
To make the training and inference more robust to noisy information, we conduct robustness training by replacing the second half of the top-k retrieved documents {doci}i=1k\{\text{doc}_{i}\}_{i=1}^{k} with partial relevant ones {docpart-rel}\{\text{doc}^{\text{part-rel}}\} and irrelevant ones {docirrel}\{\text{doc}^{\text{irrel}}\} as Eq. 6. They are sampled from the top-kk set excluding the top-5 documents and the whole collection excluding the top-kk documents, respectively.
The goal of constructing a noisy document list {doc}noisy\{\text{doc}\}_{\text{noisy}} is to provide a necessary environment for the model to learn to distinguish the useful and noisy information.
A further alternative is to shuffle the position of the noisy document list as {doc}noisyshuffle\{\text{doc}\}_{\text{noisy}}^{\text{shuffle}}, aiming to emphasize the impact of external signals and reduce the common issue of position bias (11; 60) of retrieved documents in RAG.
(6)
{doc}noisy\displaystyle\{\text{doc}\}_{\text{noisy}}
={doci}15∪{doc

## Raw body offsets 32636–36195

4.1. Datasets and Evaluation Metrics
We evaluate OpenDecoder on five benchmark datasets, including two categories: (1) General Question Answering: NQ (24), TriviaQA (19), and PopQA (33), and (2) Multi-Hop Question Answering: HotpotQA (59) and 2WikiMultiHopQA (14). These datasets encompass a diverse range of retrieval with noise in RAG, enabling a comprehensive evaluation in different settings.
Statistical details about the used datasets are provided in Appendix A.
4.2. Evaluation Settings in Noisy Environments
We evaluate our OpenDecoder and all compared baselines among three settings with different noisy retrieval results.
The first one is Normal Evaluation, where the input search results for RAG are the original top-10 documents from the retriever.
The second one is Noisy Evaluation, where the search results for RAG are constructed in the same way as the robust training in Sec. 3.4, i.e., replacing the second half of the top-10 retrieved documents with partial relevant ones and irrelevant ones, which aims to evaluate whether the RAG system can distinguish the noise and solely rely on the useful input information.
The third one is Extreme Noisy Evaluation, where the search results for RAG are obtained by randomly sampling from the irrelevant document set, which simulates the extreme cases when the retrieval fails among difficult queries or domains.
4.3. Baseline
To evaluate the effectiveness of OpenDecoder across various noisy settings, we compare it against the following baselines:
(1) Vanilla retrieval-augmented generation (RAG) (25);
(2) Vanilla supervised fine-tuning (SFT) (6);
(3) RobustRAG (56): An isolate-then-aggregate strategy to filter out the noise in retrieved context;
(4) AstuteRAG (50): A retrieval-refined method to improve knowledge utilization and enhance robustness;
(5) InstructRAG (54): Instructing LLMs to denoise retrieved content by generating self-synthesized explanatory rationales;
(6) Robustness fine-tuning (RbFT) (48): A more recent approach to conduct robustness training with two instruction fine-tuning tasks, defect detection and utility extraction.
More details about the baseline methods can be found in Appendix B.
4.4. Implementation Details
We implement OpenDecoder based on Qwen-2.5 series backbone models (58) with the official open-source code repository. The compared baselines are also implemented with the same Qwen-2.5-3B-Instruct model as our main experiments.
For retrieval, we use the 2018 Wikipedia dump (22) as the knowledge source and E5 (52) as the retriever, with the number of retrieved documents set to 1010, following (56; 48).
For the robustness training, the number of relevant, partially relevant, and irrelevant documents is set to the same as the noisy evaluation, as 5, 3, and 2, respectively.
The partially relevant and irrelevant documents are randomly sampled five times from corresponding document sets and fixed for all compared methods for fair comparison.
For training, we merge the training sets of NQ and HotpotQA to form a unified training dataset for OpenDecoder and other fine-tuning-based baselines following (18). The training epoch is set to 1 to ensure the model learn to use the explicit guidance and generalizes to out-of-domain evaluation datasets without overfitting.
Evaluation is conducted on the test sets of five datasets to assess both in-domain and out-of-domain performance. F1 score and Exact Match (EM) are used as the evaluation metrics, following (56; 48).
More implementation details can be found in our public code repository at https

## Raw body offsets 38422–41620

5.2. Ablation Study
The ablation studies are shown in Table 2. We can observe that by providing explicit indicators, the LLMs can better process the input information compared to the Vanilla SFT, which is the key idea of our method, and achieve the highest improvement. The feature aggregation is effective in some datasets, while robust training can contribute more to stable performance.
A possible explanation is that the most effective features may vary depending on the distribution of the dataset, necessitating a more adaptive feature selection mechanism to enhance generalizability. Meanwhile, introducing noisy training inputs remains essential to improve the model’s robustness and noise tolerance during inference.
Nevertheless, combining all these mechanisms for implementing OpenDecoder can obtain better results across three different evaluation settings with various levels of noisy context on five datasets, which indicates the effectiveness of each component.
Table 2. Ablation studies on the effectiveness of each mechanism in our OpenDecoder training framework.
Method
NQ
TrivialQA
popQA
HotpotQA
2Wiki
Normal Evaluation
Vanilla SFT
33.63
50.31
20.46
24.02
19.91
w/. Guidance
37.62
55.31
24.33
26.06
20.15
w/. Aggregate
36.24
55.48
21.59
28.86
22.85
w/. Robust Tr.
38.98
55.84
25.14
29.43
22.72
OpenDecoder
39.26
56.08
25.95
29.43
23.63
Noisy Evaluation
Vanilla SFT
34.98
51.37
21.06
23.55
22.07
w./ Guidance
37.30
53.35
24.05
25.78
23.65
w/. Aggregate
36.42
53.84
23.96
28.39
23.38
w/. Robust Tr.
37.43
54.57
24.56
28.39
23.33
OpenDecoder
37.71
55.09
25.07
28.76
24.17
Extreme Noisy Evaluation
Vanilla SFT
19.78
34.76
19.27
18.26
21.76
w/. Guidance
21.89
39.03
24.58
20.28
22.79
w/. Aggregate
21.07
39.57
24.26
23.25
26.77
w/. Robust Tr.
22.22
40.33
25.61
23.36
26.52
OpenDecoder
22.50
40.41
24.96
23.59
26.99
Figure 3. Performance of aggregating various scores as guidance features across different evaluation settings and datasets.
Figure 4. Performance of normalizing scores features with various approaches across different evaluation settings and datasets.
5.3. Feature Aggregation and Normalization
In this section, we further investigate the impact of aggregating and normalizing various scores for answer decoding.
Aggregation.
The results of score aggregation are depicted in Figure 3. We can see that aggregating any types of relevant scores can achieve better results compared to the Vanilla SFT without explicit indicators. Leveraging the retrieval score 𝒮Ret\mathcal{S}^{\text{Ret}} alone could be sufficient for the general QA datasets (NQ, TrivialQA, and popQA), where aggregating more features might not always bring additional gain. This might be because when one indicator feature is satisfied, adding the others might raise the risk of interference, as these features are measured from different aspects.
For the multi-hop QA datasets (HotpotQA and 2wiki), aggregating more feature scores helps to achieve better performance, which implies that complex questions desire more external indications to generate correct answers.
In addition, the improvement with aggregating LLM-based ranker score 𝒮Rank\mathcal{S}^{\text{Rank}} compared to vanilla SFT demonstr

## Raw body offsets 43456–46900

5.4. Document Order in Robust Training
In this section, we examine the effect of varying document position orders on robust training.
As mentioned in Sec. 3.3, the original input context order before applying robust training is Input=[Ins.,doc1q,doc2q,⋯,dockq,q]\text{Input}=[\text{Ins.},\text{doc}_{1}^{q},\text{doc}_{2}^{q},\cdots,\text{doc}_{k}^{q},\text{q}].
On top of it, we investigate three types of reorder methods, including reversing the document position from dockq\text{doc}_{k}^{q} to doc1q\text{doc}_{1}^{q}, shuffling them, and further injecting noise with various relevant levels as Sec. 3.4.
The results are presented in Table 3.
We observe that reversing the document order can obtain better performance than the original one. This might be because the new reversed order InputRev.=[Ins.,dockq,dock−1q,⋯,doc1q,q]\text{Input}^{\text{Rev.}}=[\text{Ins.},\text{doc}_{k}^{q},\text{doc}_{k-1}^{q},\cdots,\text{doc}_{1}^{q},\text{q}] enables the higher top-kk documents to be much closer to the question and thus might raise their attention score by alleviating the long-distance distraction. This phenomenon suggests that specifying document positions in the prompt template as plain text may not be fully interpreted by LLMs. Consequently, shuffling input documents during training can mitigate position bias, as the top-1 document is not always more informative than the top-2 for answer generation. Moreover, injecting noise further enhances model robustness by encouraging it to assess the true relevance of input documents based on external indicators, rather than relying on positional cues.
Table 3. The performance using different document position orders in robust training across five datasets.
Method
NQ
TrivialQA
popQA
HotpotQA
2Wiki
Original
35.42
52.57
20.13
20.26
22.07
w/. Reverse
36.39
53.68
21.47
27.91
22.99
w/. Shuffle
37.43
54.57
24.56
28.39
23.33
w/. Noise
37.71
55.09
25.07
28.76
24.17
5.5. Noise Tolerance of Input Top-K
As the evidence for the correct answer might relate to only a small portion of the relevant documents, the normal evaluation using the original top-kk retrieved results would still inevitably contain irrelevant information.
We evaluate the noise tolerance ability of Vanilla SFT and our proposed OpenDecoder in terms of the impact of various input top-kk values.
The results are shown in Figure 5.
As the number of input documents increases, the probability of identifying relevant documents with answer information and the degree of injecting potential noise both increase.
In most of the datasets, the larger top-kk cannot guarantee higher performance except on TrivialQA, which indicates that the accurate search results are crucial for answer generation.
Overall, our OpenDecoder exhibits better performance than Vanilla SFT in different numbers of input documents, which demonstrates the effectiveness of leveraging relevance score to impact decoding across various input top-k.
5.6. Investigation of Scaling Model Size
We further investigate the impact of scaling up model size for vanilla SFT and our OpenDecoder. The results in the noisy evaluation setting are depicted in Figure 6.
Overall, both the SFT and our proposed approaches benefit from larger model sizes, suggesting that larger models are more capable of tolerating contextual noise, which aligns with prior studies (21).
Moreover, the effectiveness of leveraging explicit indicators to influence answer generation be

## Raw body offsets 68387–70120

Appendix D Discussion on Time and Space Efficiency
The computation cost of our method is the same for the offline training and online inference.
The computation complexity of the Vanilla SFT method and our OpenDecoder are 𝒪⁡(|d|2​h+|d|​h2)\mathcal{O}(|d|^{2}h+|d|h^{2}) in the RAG setting, where dd is the average number of tokens in a document doc, and hh is the hidden dimension size of the decoder-only LLMs.
This is because the explicit guidance, i.e., the relevance scores, are produced simultaneously with the retrieved documents, and the normalization of the scores should be negligible.
In terms of the storage overhead, the normalized score Snorm∈ℝh×hS_{\text{norm}}\in\mathbb{R}^{h\times h} is stored as a token-level metric, whose shape is the same as the Query, Key, and Value metric in the attention computational network inside the LLMs.
Thus, the additional storage overhead compared to Vanilla SFT is 𝒪⁡(nh)\mathcal{O}(\text{nh}), where nn is the number of Transformer layers with the impact of explicit guidance.
    Experimental support, please
    view the build logs
    for errors. Generated by
        L
        A
        T
        E
      xml
    .
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
      support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
      methods listed below:
Click the "Report Issue" (
          ) button, located in the page header.
Tip: You can select the relevant text first, to include it in your report.
Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we

