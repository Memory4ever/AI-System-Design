[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Causal Decoding for Hallucination-Resistant Multimodal Large Language Models

[3] h6: Abstract

[4] p: Multimodal Large Language Models (MLLMs) deliver detailed responses on vision-language tasks, yet remain susceptible to object hallucination (introducing objects not present in the image), undermining reliability in practice. Prior efforts often rely on heuristic penalties, post-hoc correction, or generic decoding tweaks, which do not directly intervene in the mechanisms that trigger object hallucination and thus yield limited gains. To address this challenge, we propose a causal decoding framework that applies targeted causal interventions during generation to curb spurious object mentions. By reshaping the decoding dynamics to attenuate spurious dependencies, our approach reduces false object tokens while maintaining descriptive quality. Across captioning and QA benchmarks, our framework substantially lowers object hallucination rates and achieves state-of-the-art faithfulness without degrading overall output quality.

[5] p: Reviewed on OpenReview: https://openreview.net/forum?id=5Wb5c0FaCG

[6] h2: 1 Introduction

[7] figure: Figure 1 : Simplified causal graphs for typical MLLMs and our COAD. Left: Typical MLLMs implicitly hallucinate objects (e.g., “fork”) in the hidden states 𝐳 {\bf z} due to previously generated text 𝐱 {\bf x} (e.g., “knife”). Right: Our COAD performs causal inference to remove links between the hidden states 𝐳 {\bf z} and generated text 𝐱 {\bf x} , thereby avoiding hallucination.

[8] p: Large language models (LLMs), such as GPT-4 ( Achiam et al., 2023 ) and LLaMA ( Touvron et al., 2023 ) , have been rapidly developed and widely adopted due to their wide range of applications. To extend the capabilities of LLMs to visual tasks, multiple MLLMs have been proposed. Models such as LLaVA ( Liu et al., 2024c ) and MiniGPT ( Zhu et al., 2023 ) typically project visual information into the same representational space as textual data, enabling a unified processing approach via an internal LLM. Although MLLMs have shown impressive performance in multimodal tasks, including chatbots, visual question answering, and image captioning, they remain susceptible to visual hallucination .

[9] p: Specifically, hallucinations in LLMs ( Huang et al., 2024a ) refer to cases where the model generates outputs that appear factual but are actually incorrect or ungrounded. With the introduction of visual inputs, multimodal LLMs (MLLMs) encounter a new category of hallucination: visual hallucination ( Liu et al., 2024b ) . Visual hallucination occurs when the MLLM output diverges from the content of the input image. This undermines the reliability of the models and restricts their applicability in high-stakes real-world scenarios that demand high precision, such as medical image analysis and legal document generation.

[10] p: Recently, a variety of approaches have been proposed to mitigate hallucinations in MLLMs; they can be broadly categorized into two main strategies : (1) The first strategy improves the model with external information, such as incorporating additional training data or retrieving knowledge from external source ( Liu et al., 2024a ; Yu et al., 2024 ; Wang et al., 2023 ; Chen et al., 2024a ; Vu et al., 2023 ; Gao et al., 2023 ; Varshney et al., 2023 ) . Although these methods effectively reduce hallucinations, they often require significant effort in data collection and depend on the quality and availability of external knowledge bases. (2) The second strategy aims to reduce hallucinations without relying on additional information, instead refining the training procedures of the model or improving the attention mechanisms during inference ( Yue et al., 2024 ; Han et al., 2024 ; Shi et al., 2023 ; Leng et al., 2023 ; Liu et al., 2024d ; Huang et al., 2024b ; Chuang et al., 2024 ; Deng et al., 2024a ; Chen et al., 2024b ) . However, these methods still fail to model the causal effect from visual input (e.g., images) to the generated response. They are therefore often susceptible to confounding effect Yan and Wang (2023) ; Wang et al. (2020) ; Pearl (2009) or bias brought by the generated text. As a result, they tend to generate new hallucinated text based on existing hallucinated text, exacerbating hallucination.

[11] p: To address these challenges, we propose Causal Object-Aware Decoding (COAD) to reduce hallucination by incorporating causal inference into the model’s decoding process; this is inspired by hierarchical Bayesian deep learning Wang and Yeung (2016) ; Wang and Yeung (2020) ; Wang et al. (2024) and the causality literature Pearl (2009) ; Wang et al. (2020) ; Yan and Wang (2023) . Specifically, we first employ an object detector to identify visual objects in the image, delegating part of the image comprehension task to this specialized component. We then expose these structured detection results to the MLLM by finetuning the MLLM with object detection outputs as additional inputs, alongside the image and previously generated text tokens. Finally, we perform causal inference to effectively integrate the predictions from both the original pretrained model and the finetuned model to generate the response.

[12] p: COAD’s design improves the reliability of the MLLM via enabling targeted interventions in the model’s understanding of visual objects. Furthermore, we incorporate causal inference to reduce the model’s dependence on self-generated text when processing and describing images, thereby promoting more stable and less hallucinatory outputs. Our contributions are as follows:

[13] p: We formulate the generation of reliable responses as the estimation of unknown oracle predictions and introduce a new framework, dubbed Causal Object-Aware Decoding (COAD), to reduce object hallucination.

[14] p: We introduce a targeted intervention strategy that exposes and leverages visual structure, allowing the model to reason more faithfully about image content.

[15] p: We provide empirical results to demonstrate the effectiveness of our method in improving generation quality and reducing object hallucination compared to state-of-the-art methods.

[16] h2: 2 Related Work

[17] p: External Knowledge-Augmented Hallucination Mitigation. A typical strategy to mitigate hallucinations in MLLMs is to augment the model with external data. One line of work focuses on expanding or refining the training data to enhance grounding and reduce hallucinations ( Liu et al., 2024a ; Yu et al., 2024 ; Wang et al., 2023 ; Chen et al., 2024a ) . These methods typically involve curating high-quality multimodal instruction data, improving image-text alignment, or re-captioning visual content to ensure consistency with external world knowledge. By exposing the model to more reliable or better-aligned data, such approaches aim to reduce the risk of generating content that deviates from visual evidence or factual reality. Another line of research tackles hallucination at inference time by retrieving relevant information from external knowledge bases or the internet ( Vu et al., 2023 ; Gao et al., 2023 ; Varshney et al., 2023 ) . These retrieval-augmented generation methods dynamically inject grounded knowledge into the model’s context, thereby improving factuality without requiring the model to memorize all details.

[18] p: While both approaches have demonstrated effectiveness, they rely on either significant data curation and annotation efforts or real-time access to high-quality and up-to-date external sources. In many real-world applications, especially those involving specialized or rapidly evolving domains, such requirements may not always be feasible or reliable, highlighting the need for alternative strategies that improve factual grounding without external dependencies.

[19] p: Internal Hallucination Mitigation. Other approaches mitigate hallucinations without relying on external data sources or retrieval mechanisms. These methods aim to improve the model’s internal decision-making process by modifying its behavior during training or inference. For instance, EOS ( Yue et al., 2024 ) encourages early stopping in sequence generation to prevent over-generation, which is often a source of factual inaccuracy. Skip-\n ( Han et al., 2024 ) suppresses hallucinations by skipping newline tokens, which are empirically shown to precede low-quality or fabricated continuations. Several techniques reduce the distraction caused by noisy or misleading text-conditioned inputs by selectively emphasizing attention on visual tokens. Examples include CAD ( Shi et al., 2023 ) , VCD ( Leng et al., 2023 ) , and PAI ( Liu et al., 2024d ) , which implement visual grounding and cross-modal alignment enhancements. CLIP-guided decoding ( Deng et al., 2024b ) reduces hallucination by incorporating a CLIP-based image-text consistency score into a sentence-level beam search, adjusting the beam scores beyond the MLLM’s own likelihood. OPERA ( Huang et al., 2024b ) proposes an intervention-based decoding strategy that penalizes overconfident token predictions, which are often associated with hallucinated content. DoLa ( Chuang et al., 2024 ) improves factual alignment by comparing generation logits from early and late transformer layers, effectively regularizing token prediction based on layer-wise consistency. In this paper, we build on this line of research by focusing on internal mechanisms to reduce hallucination, without directly relying on external knowledge bases.

[20] h2: 3 Methodology

[21] p: In this section, we first introduce our COAD as a causal model for the MLLM’s next-token generation process, and then describe how we apply causal inference to predict the next token during inference.

[22] h3: 3.1 Preliminaries and Key Intuition behind COAD

[23] p: Problem Setting: Auto-Regressive Generation. We consider an auto-regressive MLLM that, at each decoding step, receives: (1) a model M M ; (2) an input image 𝐒 ∈ ℝ c × h × w \mathbf{S}\in\mathbb{R}^{c\times h\times w} where c c is the number of channels, h h is the height of the image, and w w is the width of the image; and (3) a sequence of previous tokens 𝐱 \mathbf{x} (including the prompt and generated tokens so far). The model predicts the next token y y by sampling from

[24] table: y ∼ P M ​ ( y ∣ 𝐱 , 𝐒 ) . y\sim P_{M}(y\mid\mathbf{x},\mathbf{S}).

[25] p: Here M M may be a pretrained MLLM M p M_{p} , a finetuned model M f M_{f} , or a hypothetical oracle M ∗ M_{\ast} (introduced later).

[26] figure: (a) (b) Figure 2 : Illustration of confounding. (a) z z induces a spurious association between x x and y y even without a causal effect. (b) Adding x → y x\rightarrow y introduces a genuine causal effect, but P ⁡ ( y | x ) P(y|x) remains confounded by z z .

[27] p: Causal Inference. Causal models provide a principled framework for distinguishing true causal effects from correlations induced by confounders ( Pearl, 2009 ) . A central tool is the use of interventions, denoted by do ⁡ ( ⋅ ) \mathrm{do}(\cdot) , which remove spurious dependencies when analyzing the effect of one variable on another.

[28] p: Illustrative Example. We next illustrate the effect of a confounder using the two causal graphs in Figure 2 . Let z z denote temperature, x x the hot drink sales, and y y the ice cream sales.

[29] p: In Figure 2(a) , the edges reflect the causal structure where both x x and y y are influenced by the confounder z z , but there is no direct causal effect from x x to y y . In this setting, observing high hot drink sales x x implies that temperature z z is likely low, which in turn suggests that y y (ice cream sales) is also likely low. Consequently, even though x x does not causally affect y y , the conditional probability P ⁡ ( y | x ) P(y|x) differs from P ⁡ ( y ) P(y) . This discrepancy reflects a misleading spurious correlation introduced by the confounder z z .

[30] p: To isolate the causal influence of x x on y y , we instead compute the interventional distribution P ​ ( y | do ​ ( x ) ) P(y|\text{do}(x)) , which simulates actively setting x x to a fixed value while breaking its natural dependence on z z . According to the rules of do-calculus, P ​ ( y | do ​ ( x ) ) = P ​ ( y ) P(y|\text{do}(x))=P(y) in this case, correctly reflecting the absence of x x ’s causal influence on y y . The formal derivation and rules can be found in ( Pearl, 2009 ) .

[31] p: Figure 2(b) then adds a direct causal edge x → y x\rightarrow y on top of Figure 2(a) . In this case, hot drink sales x x indeed have a direct causal impact on ice cream sales y y (e.g., some customers may buy a cold item after consuming a hot drink). However, the conditional probability P ⁡ ( y | x ) P(y|x) still overestimates this causal effect, because z z continues to influence both x x and y y . The confounder z z thus causes P ⁡ ( y | x ) P(y|x) to capture both the genuine causal effect of x x on y y and the additional dependence mediated by z z , motivating the use of interventional quantities such as P ⁡ ( y | do ⁡ ( x ) ) P(y|\mathrm{do}(x)) to isolate the true causal influence.

[32] p: Analogy to MLLM Next-Token Prediction. The structure in Figure 2(b) directly corresponds to MLLM decoding. Let 𝐱 {\bf x} denote the previously generated tokens, y y the next token to be predicted, and 𝐳 {\bf z} the model’s hidden states representing its belief about which objects are present in the image (note that 𝐳 {\bf z} is not the image itself, which could be modeled separately). Because 𝐳 {\bf z} is a backdoor variable connecting to both 𝐱 {\bf x} and y y , the conditional probability P ⁡ ( y | 𝐱 ) P(y|{\bf x}) still overestimates the causal effect from 𝐱 {\bf x} to y y , i.e., overestimates the likelihood of certain tokens y y , therefore potentially leading to hallucination.

[33] p: Key Intuition of COAD. To mitigate object hallucination, COAD explicitly models 𝐳 {\bf z} as a variable representing object beliefs and replaces the standard conditional distribution with the interventional one P ⁡ ( y | do ⁡ ( 𝐱 ) , 𝐳 ) P(y|\mathrm{do}({\bf x}),{\bf z}) . This removes the spurious dependence introduced by the confounder 𝐳 {\bf z} and predicts the next token y y based solely on the true causal effects of 𝐱 {\bf x} and 𝐳 {\bf z} .

[34] p: Generative vs. Recognition Causal Models. The causal perspective adopted in this work follows the recognition/inference view commonly used in recent causal analyses of vision-language models ( Mao et al., 2021 ; Mao et al., 2022 ) . Instead of modeling how the physical world generates an image (which would typically imply a generative direction such as 𝐳 → 𝐒 {\bf z}\rightarrow{\bf S} ), our objective is to describe how an MLLM processes an observed image 𝐒 {\bf S} and pre-existing text 𝐱 {\bf x} in order to form internal beliefs and predict the next token.

[35] p: Under this recognition view, 𝐳 {\bf z} denotes the model’s internal belief about which objects are present in the input image, not a latent variable causing the image itself. The information flow from 𝐒 {\bf S} to 𝐳 {\bf z} therefore represents the model’s inference procedure, consistent with modern architectures such as LLaVA, where visual features are computed by the vision encoder before any interaction with textual tokens (see Appendix C ). This viewpoint provides the conceptual grounding for the causal structures introduced in the following sections.

[36] h3: 3.2 Formal Definition of Object Hallucination

[37] p: Let 𝐒 {\bf S} be the input image, 𝐳 ∗ {\bf z}^{*} the ground-truth set of visual objects, and p θ ​ ( y | 𝐱 , 𝐒 ) p_{\theta}(y|{\bf x},{\bf S}) the model’s predictive distribution for the next token y y given previous tokens 𝐱 {\bf x} and the image 𝐒 {\bf S} . Let p ∗ ​ ( y | 𝐱 , 𝐳 ∗ ) p^{*}(y|{\bf x},{\bf z}^{*}) denote the “ground-truth” conditional distribution, i.e., the distribution produced by an ideal model that fully respects the true visual semantics of the image.

[38] p: We define object hallucination as the divergence between these two distributions:

[39] table: D ( p θ ( y | 𝐱 , 𝐒 ) ∥ p ∗ ( y | 𝐱 , 𝐳 ∗ ) ) , D\!\left(p_{\theta}(y|{\bf x},{\bf S})\;\|\;p^{*}(y|{\bf x},{\bf z}^{*})\right),

[40] p: where D ( ⋅ ∥ ⋅ ) D(\cdot\|\cdot) may be a KL or another divergence measure. A large divergence indicates that the model assigns high probability to tokens that contradict the true visual object content, thereby producing object hallucination.

[41] p: In existing multimodal LLMs, hallucination often arises because the hidden states 𝐳 {\bf z} may encode nonexistent objects based on previous tokens 𝐱 {\bf x} rather than on the true image content 𝐒 {\bf S} . This can lead the model to generate tokens y y that are not visually grounded. We empirically validate this phenomenon for LLaVA using a linear-probe analysis of its internal object-existence beliefs; see Appendix B for details.

[42] p: To address this issue, our COAD (i) uses a detector-derived proxy 𝐳 ^ \widehat{{\bf z}} to approximate the visual constraints 𝐳 ∗ {\bf z}^{*} in the ideal distribution p ∗ ​ ( y | 𝐱 , 𝐳 ∗ ) p^{*}(y|{\bf x},{\bf z}^{*}) , and (ii) intervenes on both the internal object-related hidden states 𝐳 {\bf z} and the previous tokens 𝐱 {\bf x} to block the spurious information pathway from 𝐱 {\bf x} to y y . These interventions reduce the divergence above and therefore mitigate object hallucination.

[43] h3: 3.3 Method Overview

[44] figure: Figure 3 : Overview of our COAD. We employ an object detector to identify the objects present in an image. The MLLM is then finetuned to condition its token predictions on both these detected objects and the input image. COAD subsequently use causal inference to combine the output distributions of both the pretrained and finetuned MLLMs to generate the final prediction.

[45] p: Figure 3 illustrates the decoding (i.e., text generation) process of our COAD. It assumes access to an MLLM that can incorporate a set of detected objects as additional context during generation. To achieve this, we finetune a pretrained MLLM with object-level information. During inference, an object detector identifies likely objects in the input image and outputs a probability distribution over candidate object classes. We then sample multiple plausible object sets from this distribution.

[46] p: Each sampled object set is injected as an auxiliary input into the finetuned MLLM to produce a distribution over the next token. This results in N N next-token distributions, which are further combined with the distribution from the pretrained MLLM. Finally, COAD uses causal inference to combine these outputs to generate a more robust and object-aware prediction.

[47] h3: 3.4 Causal Model of a Standard MLLM

[48] p: Before introducing the causal model underlying COAD, we first describe the temporal causal structure of a standard MLLM during autoregressive decoding. This view makes explicit how information flows across timesteps and clarifies the relationship between the image, the evolving text sequence, and the model’s internal object-related variables.

[49] p: Temporal Structure. The input image 𝐒 {\bf S} and the initial prompt 𝐱 ( 0 ) {\bf x}^{(0)} remain fixed throughout decoding. The variable 𝐳 {\bf z} represents the model’s belief about which objects are present in the image and is determined solely by 𝐒 {\bf S} ; it therefore remains constant across timesteps. Here, 𝐳 {\bf z} is a conceptual variable capturing image-conditioned object beliefs, rather than a token-level hidden state that evolves during decoding (see Appendix A for further discussion). This treatment is consistent with the architecture of modern vision-language models such as LLaVA, where visual features are produced by the vision encoder before any interaction with textual tokens (see Appendix C ). The only time-varying variables are the evolving text sequence 𝐱 ( t ) {\bf x}^{(t)} and the next token y ( t ) y^{(t)} .

[50] p: Figure 4(a) illustrates the resulting temporal causal graph, which contains the following edges:

[51] p: 𝐒 → 𝐳 {\bf S}\rightarrow{\bf z} , indicating that the object-belief variable 𝐳 {\bf z} is inferred from the image.

[52] p: 𝐱 ( t ) , 𝐒 , 𝐳 → y ( t ) {\bf x}^{(t)},{\bf S},{\bf z}\rightarrow y^{(t)} , reflecting that each predicted token depends on the current text, the visual input, and the inferred object beliefs.

[53] p: 𝐱 ( t ) , y ( t ) → 𝐱 ( t + 1 ) {\bf x}^{(t)},y^{(t)}\rightarrow{\bf x}^{(t+1)} , reflecting the autoregressive update where each new token y ( t ) y^{(t)} is appended to the old sequence 𝐱 ( t ) {\bf x}^{(t)} to form the new input sequence 𝐱 ( t + 1 ) {\bf x}^{(t+1)} , i.e., the new input sequence is 𝐱 ( t + 1 ) = [ 𝐱 ( t ) , y ( t ) ] . {\bf x}^{(t+1)}=[{\bf x}^{(t)},y^{(t)}].

[54] p: Collapsed Representation. If the intermediate variables y ( t ) y^{(t)} are treated as implicit steps in the autoregressive update, the subgraph of ( 𝐱 ( t ) , y ( t ) , 𝐱 ( t + 1 ) ) ({\bf x}^{(t)},y^{(t)},{\bf x}^{(t+1)}) can be collapsed into a single transition 𝐱 ( t ) → 𝐱 ( t + 1 ) {\bf x}^{(t)}\rightarrow{\bf x}^{(t+1)} , producing the structure shown in Figure 4(b) . In this form, each 𝐱 ( t ) {\bf x}^{(t)} ( t > 0 t>0 ) is jointly determined by 𝐒 {\bf S} , 𝐳 {\bf z} , and 𝐱 ( t − 1 ) {\bf x}^{(t-1)} .

[55] p: Time-Compressed View. Compressing the time axis of Figure 4(a) yields the representation in Figure 4(c) , which summarizes the cumulative influence of past timesteps on 𝐱 ( t ) {\bf x}^{(t)} via dashed edges from ( 𝐒 , 𝐳 ) ({\bf S},{\bf z}) to 𝐱 ( t ) {\bf x}^{(t)} . This compressed form closely matches the causal structure underlying a single decoding step, and provides the foundation upon which we build the causal model for COAD in the next subsection.

[56] figure: (a) Full temporal causal graph of MLLM decoding process, where gray nodes represent observed variables. (b) Collapsed version of (a). (c) Time-compressed representation of (a). Figure 4 : Rolled-out causal structures of the MLLM decoding process. (a) Full temporal (rolled-out) causal graph over decoding timesteps: the image 𝐒 {\bf S} and initial prompt 𝐱 ( 0 ) {\bf x}^{(0)} are fixed, 𝐳 {\bf z} denotes the image-derived object-belief variable (constant over time), and 𝐱 ( t ) {\bf x}^{(t)} , y ( t ) y^{(t)} evolve according to 𝐱 ( t ) , 𝐒 , 𝐳 → y ( t ) {\bf x}^{(t)},{\bf S},{\bf z}\rightarrow y^{(t)} and 𝐱 ( t ) , y ( t ) → 𝐱 ( t + 1 ) {\bf x}^{(t)},y^{(t)}\rightarrow{\bf x}^{(t+1)} . (b) Collapsed version of (a) obtained by treating y ( t ) y^{(t)} as an implicit step in the autoregressive update, so that each 𝐱 ( t ) {\bf x}^{(t)} ( t > 0 t>0 ) is jointly determined by 𝐒 {\bf S} , 𝐳 {\bf z} , and 𝐱 ( t − 1 ) {\bf x}^{(t-1)} . (c) Time-compressed representation in which the accumulated influence of all previous timesteps on 𝐱 ( t ) {\bf x}^{(t)} is summarized by dashed edges from ( 𝐒 , 𝐳 ) ({\bf S},{\bf z}) to 𝐱 ( t ) {\bf x}^{(t)} .

[57] h3: 3.5 Causal Model of COAD

[58] p: Figure 5(a) shows the causal model (as a causal Bayesian network) of our COAD. Given the input image 𝐒 {\bf S} and the previous text tokens 𝐱 {\bf x} as observed variables, below are key components in COAD’s generative process.

[59] p: Object Variable 𝐳 {\bf z} . Our causal model operates at the granularity of individual token generation. At each decoding step, given the image 𝐒 {\bf S} and the preceding (incomplete) text 𝐱 {\bf x} , COAD infers the presence of visual objects in 𝐒 {\bf S} through a binary variable 𝐳 ∈ { 0 , 1 } C {\bf z}\in\{0,1\}^{C} , where C C denotes the total number of object categories and is fixed by the choice of the detector. This variable is sampled from the distribution produced by an object detector D D :

[60] table: 𝐳 \displaystyle{\bf z} ∼ D ⁡ ( 𝐒 ) , \displaystyle\sim D({\bf S}),

[61] p: where D ⁡ ( 𝐒 ) ∈ [ 0 , 1 ] C D({\bf S})\in[0,1]^{C} denotes the detector’s estimated probability for the presence of each object category in the image.

[62] p: Dual MLLMs for Generation. To model the next-token prediction, we incorporate two MLLMs into our causal framework: a pretrained model M p M_{p} and a finetuned variant M f M_{f} . The pretrained model M p M_{p} takes as input the image 𝐒 {\bf S} and the preceding text 𝐱 {\bf x} , and outputs a distribution over the next token y p y_{p} . The finetuned model M f M_{f} , adapted from M p M_{p} , additionally conditions on the object variable 𝐳 {\bf z} to produce a distribution over the next token y f y_{f} :

[63] table: y p \displaystyle y_{p} ∼ P M p ​ ( y p | 𝐱 , 𝐒 ) , \displaystyle\sim P_{M_{p}}(y_{p}|{\bf x},{\bf S}), y f \displaystyle y_{f} ∼ P M f ​ ( y f | 𝐱 , 𝐒 , 𝐳 ) , \displaystyle\sim P_{M_{f}}(y_{f}|{\bf x},{\bf S},{\bf z}),

[64] p: where P M p ​ ( y p | 𝐱 , 𝐒 ) P_{M_{p}}(y_{p}|{\bf x},{\bf S}) is the next token distribution predicted by M p M_{p} , and P M f ​ ( y f | 𝐱 , 𝐒 , 𝐳 ) P_{M_{f}}(y_{f}|{\bf x},{\bf S},{\bf z}) is the next token distribution predicted by M f M_{f} . In practice, M p M_{p} and M f M_{f} share most parameters for efficiency.

[65] p: Hypothetical Oracle MLLM. To complete the causal graph, we introduce a hypothetical oracle model M ∗ M_{*} , which serves as an idealized reference that always produces the optimal next-token distribution. The token predicted by this oracle, denoted as y ∗ y_{*} , is generated as follows:

[66] table: y ∗ \displaystyle y_{*} ∼ P M ∗ ​ ( y ∗ | 𝐱 , 𝐒 , 𝐳 ) , \displaystyle\sim P_{M_{*}}(y_{*}|{\bf x},{\bf S},{\bf z}),

[67] p: where P M ∗ ​ ( y ∗ | 𝐱 , 𝐒 , 𝐳 ) P_{M_{*}}(y_{*}|{\bf x},{\bf S},{\bf z}) represents the oracle’s ground-truth distribution conditioned on the previous text 𝐱 {\bf x} , image 𝐒 {\bf S} , and object variable 𝐳 {\bf z} .

[68] p: Mixture-Based Generation. We hypothesize that the finetuned model M f M_{f} behaves as a mixture of the pretrained model M p M_{p} and the hypothetical oracle model M ∗ M_{*} . At each decoding step, M f M_{f} may generate either the token predicted by M p M_{p} or the one predicted by M ∗ M_{*} , with a certain probability. Note that this is a natural assumption: M p M_{p} serves as the initialization of M f M_{f} , and during finetuning, M f M_{f} is optimized to better approximate ground-truth signals (as represented by M ∗ M_{*} ) while still inheriting behaviors from the original pretrained M p M_{p} .

[69] p: To capture the uncertainty in M f M_{f} ’s alignment between M p M_{p} and M ∗ M_{*} , we introduce a random variable γ ∈ [ 0 , 1 ] \gamma\in[0,1] , which governs the mixture proportion. This variable is drawn from a global prior Beta distribution with hyperparameters γ a , γ b ∈ ℝ + \gamma_{a},\gamma_{b}\in\mathbb{R}^{+} , which are fixed across dataset:

[70] table: γ \displaystyle\gamma ∼ Beta ​ ( γ a , γ b ) , \displaystyle\sim\text{Beta}(\gamma_{a},\gamma_{b}),

[71] p: and the next-token prediction y f y_{f} is drawn approximately from a mixture of the two sources:

[72] table: y f \displaystyle y_{f} ≈ CategoricalMixture ​ ( { y ∗ , y p } , [ γ , 1 − γ ] ) \displaystyle\approx\text{CategoricalMixture}(\{y_{*},y_{p}\},[\gamma,1-\gamma]) ≜ Categorical ​ ( γ × y ∗ + ( 1 − γ ) × y p ) . \displaystyle\triangleq\text{Categorical}(\gamma\times y_{*}+(1-\gamma)\times y_{p}).

[73] p: This formulation reflects the intuition that M f M_{f} may probabilistically interpolate between following the oracle model and reverting to its pretraining prior (more details in Equation 2 below). It also provides an alternative generative view of y f y_{f} , which allows us to indirectly infer the oracle token y ∗ y_{*} in Section 3.6 .

[74] figure: (a) Original causal graph, where gray nodes represent observed variables. The dotted arrows illustrate an alternative pathway for generating y f y_{f} . (b) The resulting causal graph after do ​ ( 𝐱 ) \text{do}({\bf x}) intervention. All edges going into 𝐱 {\bf x} are blocked by the intervention. Figure 5 : Illustration of our COAD’s causal model before and after intervention.

[75] p: Complete Causal Graph. Figure 5(a) summarizes the causal relationships among all random variables introduced in our model. The image 𝐒 {\bf S} and previous tokens 𝐱 {\bf x} are the only observed variables. Note that 𝐱 {\bf x} itself may be influenced by 𝐒 {\bf S} and 𝐳 {\bf z} during previous decoding steps. All other variables are conditionally generated from their respective parents according to the mechanisms described above. The dotted connections from y ∗ y_{*} , y p y_{p} , and γ \gamma to y f y_{f} indicate our hypothesis: M f M_{f} can be alternatively interpreted as a probabilistic mixture of M ∗ M_{*} and M p M_{p} .

[76] p: With the causal graph and the given observed variables, i.e., the image 𝐒 {\bf S} and previous tokens 𝐱 {\bf x} , our goal is to (approximately) predict the oracle next token y ∗ y_{*} using causal inference. This will be discussed in Section 3.6 below.

[77] h3: 3.6 Inference Process

[78] p: In this subsection, we describe how COAD employs our causal model to address the key challenges in reducing hallucinations of the MLLMs. We start by briefly discussing two key components of our method, i.e., Causal Inference of Objects 𝐳 {\bf z} and Estimation of Oracle Predictions , and then derive the corresponding equations that combine these two components.

[79] p: Component 1: Causal Inference of Objects 𝐳 {\bf z} . To ensure object beliefs reflect only the image content, we explicitly model them as variable 𝐳 {\bf z} in our causal framework. Different from existing methods, where object belief is entangled in the hidden state and influenced by previous tokens 𝐱 {\bf x} , we block this dependency using an intervention do ​ ( 𝐱 ) \text{do}({\bf x}) (see Figure 5(b) ). This treats 𝐱 {\bf x} as externally fixed, forcing the inference of 𝐳 {\bf z} to depend solely on the image 𝐒 {\bf S} and not on prior language outputs 𝐱 {\bf x} .

[80] p: Component 2: Estimation of Oracle Predictions. To approximate the oracle prediction y ∗ y_{*} , we model the finetuned output y f y_{f} as a mixture of the pretrained model M p M_{p} and the oracle model M ∗ M_{*} , following our assumption in Section 3.5 . While y ∗ y_{*} is unobservable, this mixture formulation allows us to estimate it using the available predictions y f y_{f} and y p y_{p} by M f M_{f} and M p M_{p} , respectively. This provides a principled way to bridge the gap between observed model behavior and the ideal oracle output.

[81] p: Combining Components 1 & 2 to Derive the Inference Objective. By combining the previous components, our inference objective becomes computing the oracle prediction under intervention, i.e., P ​ ( y ∗ | 𝐒 , do ​ ( 𝐱 ) ) P(y_{*}|{\bf S},\text{do}({\bf x})) . Using Bayes’ rule and standard rules of causal inference ( Pearl, 2009 ) , we have that:

[82] table: P ​ ( y ∗ | 𝐒 , do ​ ( 𝐱 ) ) \displaystyle P(y_{*}|{\bf S},\text{do}({\bf x})) (1) = \displaystyle= ∑ 𝐳 P ⁡ ( y ∗ | 𝐒 , do ​ ( 𝐱 ) , 𝐳 ) ​ P ​ ( 𝐳 | 𝐒 , do ​ ( 𝐱 ) ) \displaystyle\sum\nolimits_{{\bf z}}P(y_{*}|{\bf S},\text{do}({\bf x}),{\bf z})P({\bf z}|{\bf S},\text{do}({\bf x})) = \displaystyle= ∑ 𝐳 P ⁡ ( y ∗ | 𝐒 , do ​ ( 𝐱 ) , 𝐳 ) ​ P ​ ( 𝐳 | 𝐒 ) \displaystyle\sum\nolimits_{{\bf z}}P(y_{*}|{\bf S},\text{do}({\bf x}),{\bf z})P({\bf z}|{\bf S})\ (Rule 3) = \displaystyle= ∑ 𝐳 P ⁡ ( y ∗ | 𝐒 , 𝐱 , 𝐳 ) ​ P ​ ( 𝐳 | 𝐒 ) , \displaystyle\sum\nolimits_{{\bf z}}P(y_{*}|{\bf S},{\bf x},{\bf z})P({\bf z}|{\bf S}),\ (Rule 2)

[83] p: This formulation rewrites the interventional query (with do ​ ( ⋅ ) \text{do}(\cdot) ) using standard conditional probabilities (without do ​ ( ⋅ ) \text{do}(\cdot) ), which can be estimated from observable components. We use the object detector D D to compute P ⁡ ( 𝐳 | 𝐒 ) P({\bf z}|{\bf S}) , which ensures that object beliefs are based solely on the image. The term P ⁡ ( y ∗ | 𝐒 , 𝐱 , 𝐳 ) P(y_{*}|{\bf S},{\bf x},{\bf z}) represents the oracle model’s prediction, which is not directly accessible. To address this, we approximate it using a mixture model. Specifically, following our hypothesized relationship between M f M_{f} , M ∗ M_{*} , and M p M_{p} , we have that:

[84] table: P ⁡ ( y f | 𝐒 , 𝐱 , 𝐳 ) = 𝔼 γ ​ [ γ ​ P ​ ( y ∗ | 𝐒 , 𝐱 , 𝐳 ) + ( 1 − γ ) ​ P ​ ( y p | 𝐒 , 𝐱 ) ] . \displaystyle P(y_{f}|{\bf S},{\bf x},{\bf z})=\mathbb{E}_{\gamma}\big[\gamma P(y_{*}|{\bf S},{\bf x},{\bf z})+(1-\gamma)P(y_{p}|{\bf S},{\bf x})\big]. (2)

[85] p: By rearranging Equation 2 , we can rewrite the prediction from M ∗ M_{*} in terms of the predictions y p y_{p} and y f y_{f} from M p M_{p} and M f M_{f} , respectively. Specifically:

[86] table: P ⁡ ( y ∗ | 𝐒 , 𝐱 , 𝐳 ) \displaystyle P(y_{*}|{\bf S},{\bf x},{\bf z}) (3) = \displaystyle= 1 𝔼 γ ​ [ γ ] ​ P ​ ( y f | 𝐒 , 𝐱 , 𝐳 ) + ( 1 − 1 𝔼 γ ​ [ γ ] ) ​ P ​ ( y p | 𝐒 , 𝐱 ) \displaystyle\tfrac{1}{\mathbb{E}_{\gamma}[\gamma]}P(y_{f}|{\bf S},{\bf x},{\bf z})+(1-\tfrac{1}{\mathbb{E}_{\gamma}[\gamma]})P(y_{p}|{\bf S},{\bf x}) = \displaystyle= ( 1 + γ b γ a ) ​ P ​ ( y f | 𝐒 , 𝐱 , 𝐳 ) − ( γ b γ a ) ​ P ​ ( y p | 𝐒 , 𝐱 ) . \displaystyle\left(1+\tfrac{\gamma_{b}}{\gamma_{a}}\right)P(y_{f}|{\bf S},{\bf x},{\bf z})-\left(\tfrac{\gamma_{b}}{\gamma_{a}}\right)P(y_{p}|{\bf S},{\bf x}).

[87] p: Final Inference Objective. After substituting Equation 3 into Equation 1 and rearranging the terms, we can then rewrite our final inference objective as a combination of known quantities:

[88] table: P ​ ( y ∗ | 𝐒 , do ​ ( 𝐱 ) ) \displaystyle P(y_{*}|{\bf S},\text{do}({\bf x})) (4) = \displaystyle= ∑ 𝐳 P ⁡ ( 𝐳 | 𝐒 ) ​ [ ( 1 + α ) ​ P ​ ( y f | 𝐒 , 𝐱 , 𝐳 ) − α ​ P ​ ( y p | 𝐒 , 𝐱 ) ] \displaystyle\sum\nolimits_{{\bf z}}P({\bf z}|{\bf S})\big[\left(1+\alpha\right)P(y_{f}|{\bf S},{\bf x},{\bf z})-\alpha P(y_{p}|{\bf S},{\bf x})\big] = \displaystyle= ( 1 + α ) ​ ∑ 𝐳 [ P ⁡ ( 𝐳 | 𝐒 ) ​ P ​ ( y f | 𝐒 , 𝐱 , 𝐳 ) ] − α ​ P ​ ( y p | 𝐒 , 𝐱 ) . \displaystyle\left(1+\alpha\right)\sum\nolimits_{{\bf z}}\big[P({\bf z}|{\bf S})P(y_{f}|{\bf S},{\bf x},{\bf z})\big]-\alpha P(y_{p}|{\bf S},{\bf x}).

[89] p: where we use the shorthand α ≜ γ b / γ a \alpha\triangleq\gamma_{b}/\gamma_{a} . Since only the ratio α = γ b / γ a \alpha=\gamma_{b}/\gamma_{a} appears in the final expression, the Beta distribution’s parameters ( γ a , γ b ) (\gamma_{a},\gamma_{b}) (as hyperparameters) effectively have only one degree of freedom during inference. In practice, We therefore treat α \alpha as a single global hyperparameter (see Appendix A for additional details). Notably, computing the closed-form expression in Equation 4 is equivalent to sampling many values of γ ∼ Beta ⁡ ( γ a , γ b ) \gamma\sim\mathrm{Beta}(\gamma_{a},\gamma_{b}) and averaging their contributions in expectation. This closed-form solution makes COAD both more efficient and conceptually consistent with the underlying mixture interpretation.

[90] p: Since the dimension of 𝐳 {\bf z} can be large, directly summing over all possible object-belief vectors is computationally intractable. We consider two practical implementations to approximate the expectation over 𝐳 {\bf z} in Equation 4 : (1) Monte Carlo sampling , where we treat the detector’s output z ~ ∈ [ 0 , 1 ] C \widetilde{z}\in[0,1]^{C} as the parameters of C C Bernoulli distributions and sample N N binary vectors z i ∈ { 0 , 1 } C z_{i}\in\{0,1\}^{C} (where i = 1 , 2 , … , N i=1,2,\dots,N ) from them, so that the term ∑ 𝐳 P ⁡ ( 𝐳 | 𝐒 ) ​ P ​ ( y f | 𝐒 , 𝐱 , 𝐳 ) \sum_{{\bf z}}P({\bf z}|{\bf S})P(y_{f}|{\bf S},{\bf x},{\bf z}) is approximated by 1 N ​ ∑ i = 1 N P ⁡ ( y f | 𝐒 , 𝐱 , 𝐳 i ) \frac{1}{N}\sum_{i=1}^{N}P(y_{f}|{\bf S},{\bf x},{\bf z}_{i}) ; and (2) probability-based approximation , where we directly feed the probability vector 𝐳 ~ \widetilde{{\bf z}} into M f M_{f} , which empirically provides an efficient approximation to the same expectation while avoiding sampling. Due to its high efficiency, we adopt the second implementation (although it is an approximation) for all our experiments.

[91] p: Summary of COAD. To summarize, training and inference of COAD consist of the following steps:

[92] p: Modify the pretrained MLLM to accept an object belief vector 𝐳 {\bf z} as an additional input.

[93] p: Finetune the modified MLLM using the object vectors 𝐳 {\bf z} (predicted by an object detector).

[94] p: At inference time, compute the next-token probability using Equation 4 , approximating the expectation over 𝐳 {\bf z} via Monte Carlo sampling.

[95] p: Therefore, COAD enables object-aware dehallucination by explicitly grounding language generation in visual object beliefs. Through causal modeling and intervention, COAD ensures that predictions remain faithful to the image content, reducing reliance on spurious correlations from prior text.

[96] h2: 4 Experiments

[97] p: In this section, we compare COAD with existing methods on real-world datasets.

[98] h3: 4.1 Datasets and Metrics

[99] p: We use various datasets and metrics below to evaluate the MLLMs.

[100] p: POPE. The Polling-based Object Probing Evaluation (POPE) ( Li et al., 2023 ) employs visual question answering to assess whether an MLLM can correctly identify the presence of an object in an input image. Following the literature ( Liu et al., 2024d ; Huang et al., 2024b ) , we focus on the MSCOCO dataset with 500 images, with each image having 6 questions for each split of POPE. We evaluate the object recognition performance using the Precision, Recall, F-1, and Accuracy metrics.

[101] p: CHAIR. Caption Hallucination Assessment with Image Relevance (CHAIR) ( Rohrbach et al., 2018 ) is a set of widely used metrics to evaluate captioning hallucination. Following the literature ( Liu et al., 2024d ; Huang et al., 2024b ) , we use the MSCOCO dataset ( Lin et al., 2014 ) that provides annotations for ground-truth objects in images. Specifically, CHAIR includes two metrics:

[102] p: CHAIR S , which measures the proportion of captions containing hallucinated objects relative to the total number of captions:

[103] table: CHAIR S = | captions with hallucinated objects | / | all captions | , \displaystyle\text{CHAIR}_{S}=|\text{captions with hallucinated objects}|\ /\penalty\ |\text{all captions}|,

[104] p: CHAIR I , which measures the proportion of the hallucinated objects relative to the total number of mentioned objects:

[105] table: CHAIR I = | hallucinated objects | / | all mentioned objects | . \displaystyle\text{CHAIR}_{I}=|\text{hallucinated objects}|\ /\penalty\ |\text{all mentioned objects}|.

[106] p: MMHal-Bench. MMHal-Bench ( Sun et al., 2023 ) is a dataset designed to evaluate MLLMs on diverse questions where they may produce false claims about image content. The benchmark spans eight hallucination dimensions that assess different aspects of visual grounding: (1) Object attribute : the ability to correctly describe properties such as color or shape; (2) Adversarial object : the ability to recognize when a queried object is not present rather than hallucinating it; (3) Comparison : the ability to compare attributes or properties across multiple objects; (4) Counting : the ability to estimate the number of referred objects; (5) Spatial relation : the ability to reason about relative positions among objects; (6) Environment : the ability to infer aspects of the surrounding scene or background; (7) Holistic description : the ability to provide accurate global descriptions of the entire image; (8) Others : the ability to recognize text or symbols and reason based on observable visual information. Scores for each dimension are computed as the proportion of responses deemed non-hallucinatory. Higher scores across these dimensions indicate better grounding and fewer hallucinations. Following the MMHal-Bench evaluation protocol ( Sun et al., 2023 ) , we use GPT-4 to perform this judgment.

[107] h3: 4.2 Baselines

[108] p: We use LLaVA-1.5-7B ( Liu et al., 2024c ) as the base model for all evaluated methods. For COAD, we use RTMDet ( Lyu et al., 2022 ) as the object detector D D .

[109] p: As discussed in Section 1 , existing hallucination-mitigation approaches fall into two broad categories: (1) external-knowledge-based methods and (2) internal architecture/decoding modifications. Since COAD belongs to the second family and does not rely on external data retrieval, all baselines evaluated here are drawn from this internal-mechanism category to ensure a fair comparison. Under this setting, we compare COAD with state-of-the-art internal-mechanism methods, including Decoding by Contrasting Layers ( DoLa ) ( Chuang et al., 2024 ) , Paying More Attention to Image ( PAI ) ( Liu et al., 2024d ) , End-of-Sentence Decision ( EOS ) ( Yue et al., 2024 ) , Over-trust Penalty and Retrospection-Allocation ( OPERA ) ( Huang et al., 2024b ) , Visual Contrastive Decoding ( VCD ) ( Leng et al., 2023 ) , Context-Aware Decoding ( CAD ) ( Shi et al., 2023 ) , and Object Hallucination Reduction via Adaptive Focal-Contrast Decoding ( HALC ) ( Chen et al., 2024b ) .

[110] h3: 4.3 Implementation Details

[111] p: We finetune COAD on a subset of MSCOCO images sourced from the LLaVA dataset. To enable the model to incorporate the auxiliary input 𝐳 {\bf z} , we introduce a two-layer MLP projector (with hidden size 256 256 ) that maps 𝐳 {\bf z} into the token embedding space, following LLaVA’s multimodal token integration approach. We employ LoRA ( r = 128 r=128 , α = 256 \alpha=256 ), a cosine learning rate schedule with an initial learning rate of 4 ​ e − 5 4\text{e}{-5} , a batch size of 128, and train the model for 1 epoch. During inference, we use sampling by default with temperature 0.2 and a maximum of 512 output tokens. See Appendix A for more details.

[112] h3: 4.4 Main Results

[113] p: In this section, we compare COAD with different baselines across various datasets and metrics.

[114] figure: Figure 6 : Case study on caption generation. MSCOCO objects mentioned in the text are highlighted in red (hallucinated) or green (correct). We compare the baseline LLaVA with our COAD-enhanced model. While LLaVA hallucinates nonexistent objects (e.g., knife and fork ), the 𝐳 {\bf z} -vector produced by the object detector suggests that these objects are absent. By leveraging this signal, COAD produces a faithful caption grounded in the actual image content, consistent with the improvements shown in CHAIR metrics.

[115] figure: Table 1 : Comparison of different methods in terms of CHAIR metrics. Boldface and underlining denote the best and the second-best performance, respectively. Method Base PAI DoLa VCD CAD OPERA EOS HALC COAD CHAIR I ↓ \text{CHAIR}_{I}\downarrow 9.9 5.8 13.0 11.4 9.9 4.5 5.8 5.2 3.4 CHAIR S ↓ \text{CHAIR}_{S}\downarrow 29.6 11.3 37.0 32.5 28.0 7.4 10.6 11.1 5.3

[116] p: Free-Form Generation Evaluation on CHAIR. We first evaluate COAD on the CHAIR benchmark, which measures hallucination rates in free-form image captioning. The CHAIR benchmark includes two sub-metrics: CHAIR I (instance-level) and CHAIR S (sentence-level). Lower CHAIR I and CHAIR S indicate fewer hallucinated mentions.

[117] p: As shown in Table 1 , COAD achieves the best performance across all three CHAIR metrics, significantly reducing hallucinations. Specifically, it achieves 3.4 and 5.3 in terms of CHAIR I and CHAIR S , respectively, outperforming all existing baselines. This demonstrates that our causal object-aware decoding effectively reduces hallucination of generated captions.

[118] p: Figure 6 shows a qualitative example comparing the baseline LLaVA and our COAD. Here, LLaVA hallucinates nonexistent objects such as a knife and fork , while our COAD correctly suppresses them and generates a more faithful caption. 1 1 1 While COAD successfully removes the hallucinated objects such as the “knife” and “fork”, its output also includes the phrase “one slice missing”, which may be an inaccurate description of the pizza. This type of error concerns the attributes of an already-present object rather than the presence of additional objects. Since COAD is designed specifically to mitigate object hallucination , such attribute-level inconsistencies fall outside the scope of what our method targets. This illustrates how causal object-aware decoding helps mitigate hallucination in practice. Additional case studies are provided in Appendix F .

[119] figure: Table 2 : Evaluation on MMHal-Bench across 8 hallucination dimensions: attributes (attr), adversarial objects (adv), comparison (cmp), counting (cnt), spatial relations (rel), environment (env), holistic/overall description (hol), and others (oth). Boldface and underlining denote the best and the second-best performance, respectively. Method Avg. Score Hall. Rate attr adv cmp cnt rel env hol oth Base 1.88 0.68 2.33 1.25 2.67 0.83 1.75 3.17 1.42 1.58 PAI 2.10 0.65 1.92 1.33 2.25 2.17 2.17 3.67 1.75 1.58 Dola 2.01 0.62 2.08 1.42 2.75 1.67 1.17 4.00 1.75 1.25 VCD 1.98 0.67 2.17 1.83 1.83 1.33 2.42 3.33 1.33 1.58 CAD 2.00 0.64 2.50 1.25 2.42 0.75 1.33 3.83 1.83 2.08 OPERA 2.09 0.65 2.58 1.67 2.67 2.50 1.58 3.08 1.17 1.50 EOS 2.08 0.62 2.67 1.33 2.67 1.00 1.83 3.17 1.58 2.42 HALC 2.12 0.64 2.33 1.67 3.00 2.25 1.67 3.42 1.33 1.33 COAD 2.52 0.52 3.58 1.83 3.33 2.08 2.08 3.50 1.33 2.42

[120] p: Multimodal QA Evaluation on MMHal-Bench. Table 2 shows the results on MMHal-Bench. COAD achieves the highest average score (2.52) and the lowest hallucination rate (0.52), significantly outperforming all baselines. The strong performance is consistent across multiple benchmark subsets, particularly in the Attribute, Comparison, and Relation categories, indicating improved factual accuracy and reasoning. These results further demonstrate that incorporating object-level cues effectively reduces hallucination while maintaining or enhancing generation quality.

[121] figure: Table 3 : POPE evaluation results on the MSCOCO dataset. Boldface and underlining denote the best and the second-best performance, respectively. Method Random Popular Adversarial Acc P R F1 Yes Acc P R F1 Yes Acc P R F1 Yes Base 89.0 89.3 88.6 89.0 49.6 85.0 82.6 88.7 85.5 53.7 78.8 74.0 88.8 80.8 60.0 PAI 89.3 89.6 88.9 89.2 49.6 86.1 84.2 89.0 86.5 52.9 78.9 74.4 88.3 80.7 59.4 Dola 86.3 85.3 87.7 86.5 51.4 83.0 80.5 87.1 83.6 54.1 78.2 73.9 87.4 80.1 59.2 VCD 88.8 88.8 88.7 88.8 50.0 85.4 83.6 88.1 85.8 52.7 79.2 74.5 88.6 81.0 59.4 CAD 88.6 88.7 88.5 88.6 49.9 84.8 82.5 88.3 85.3 53.5 78.5 74.0 87.9 80.3 59.4 OPERA 89.4 89.7 89.0 89.3 49.6 85.9 83.9 89.0 86.4 53.1 79.1 74.3 89.0 81.0 59.9 EOS 85.4 81.5 91.7 86.3 56.3 81.2 75.8 91.7 83.0 60.5 75.9 69.6 91.9 79.2 66.0 HALC 88.7 89.9 87.1 88.5 48.5 85.8 84.8 87.1 86.0 51.4 79.1 75.0 87.1 80.6 58.1 COAD 89.0 89.6 88.3 89.0 49.3 85.5 84.0 87.6 85.8 52.1 79.8 75.8 87.5 81.2 57.7

[122] p: Object Probing Evaluation on POPE. Table 3 shows the POPE evaluation results across three settings. COAD achieves the highest accuracy (79.8) and F1 score (81.2) on the Adversarial subset, outperforming all baselines, indicating better robustness to prompts designed to induce hallucination. In the Popular and Random subsets, it performs comparably to state-of-the-art methods in F1 while maintaining a low hallucination ratio. These results confirm that our approach effectively reduces hallucinations while preserving factual precision across diverse input types.

[123] figure: Table 4 : Results of COAD and ablations on CHAIR. “ M f M_{f} only” means only using the finetuned model M f M_{f} for generation; “w/o 𝐳 {\bf z} ” means replacing M f M_{f} by a normally finetuned MLLM and applying COAD, without any 𝐳 {\bf z} vectors involved in the whole process. Method CHAIR I ↓ {}_{I}\downarrow CHAIR S ↓ {}_{S}\downarrow COAD (Full) 3.4 5.3 COAD ( M f M_{f} only) 5.4 10.8 COAD (w/o 𝐳 \mathbf{z} ) 6.9 18.1

[124] p: Ablation Studies. We conduct two ablation studies on CHAIR to better understand the source of our improvements. Specifically, we compare our full COAD with (1) “ COAD ( M f M_{f} Only) ”, which only uses the finetuned model M f M_{f} without applying our causal decoding procedure and (2) “ COAD (w/o 𝐳 {\bf z} ) ”, where we train M f M_{f} without 𝐳 {\bf z} and perform causal decoding using this modified M f M_{f} . Table 4 shows the results. The gap between COAD and “COAD ( M f M_{f} Only)” verifies the effectiveness of our causal decoding algorithm, while the gap between COAD and “COAD (w/o 𝐳 {\bf z} )” verifies the important role of 𝐳 {\bf z} in COAD (see more discussion in Appendix D ).

[125] h3: 4.5 Runtime and Computational Overhead

[126] p: Beyond hallucination metrics, we also compare the computational overhead of COAD with existing methods. To ensure consistency with the CHAIR evaluation, we select 100 images from the MSCOCO subset used in our CHAIR experiments and ask each method to generate free-form descriptions of the images using the same decoding setting as in Section 4.4 . All methods are evaluated on a single GPU. We measure decoding throughput in tokens per second, which reflects the effective per-token computational cost of each method. Table 5 shows the results.

[127] figure: Table 5 : Decoding throughput of different methods on 100 MSCOCO images used in the CHAIR evaluation. We report the number of tokens per second during generation (higher is better). Method Base COAD (Ours) OPERA PAI DoLa VCD CAD EOS HALC #tokens/s ↑ \uparrow 24.37 10.49 4.52 43.62 29.38 7.98 7.92 9.91 7.32

[128] p: Detector Overhead. COAD invokes the object detector only once per image before decoding. Since autoregressive decoding dominates the total computational cost for MLLMs, this one-time detection overhead is relatively small: the RTMDet detector used in our implementation processes each image in about 0.10 seconds, which is negligible compared with the cumulative cost of token generation on long outputs.

[129] p: Dual-Model Decoding. COAD evaluates both the pretrained model and the object-aware finetuned model at each decoding step. When executed sequentially on a single GPU, this dual-model decoding results in roughly half the throughput of the base LLaVA model (10.49 vs. 24.37 tokens/s in Table 5 ). However, the two forward passes are independent and can be executed fully in parallel on different GPUs, allowing throughput close to that of single-model decoding in practical multi-GPU deployments.

[130] p: Compared to other hallucination-mitigation methods, COAD remains computationally competitive. In particular, it is significantly faster than multi-step refinement and beam-search/backtracking approaches such as OPERA (4.52 tokens/s), and comparable to other decoding-modification methods like VCD, CAD, EOS, and HALC. Overall, COAD achieves strong reductions in hallucination with a moderate and well-characterized runtime overhead.

[131] h2: 5 Conclusion

[132] p: In this paper, we propose COAD, a novel approach to reducing object hallucination in MLLMs. By combining object detection and causal inference, COAD improves the quality of generated captions and reasoning outputs. Extensive experiments on various benchmarks show that COAD consistently outperforms state-of-the-art dehallucination methods across diverse metrics and settings.

[133] p: Future work may include more sophisticated object representations and extend our causal modeling framework to additional multimodal tasks. Since the number of object categories is determined by the detector, it would also be interesting to explore open-vocabulary detectors (e.g., GLIP ( Li et al., 2022 ) ), which may allow COAD to operate over a substantially richer and more flexible object space. Moreover, we plan to investigate the integration of temporal and spatial priors to further enhance the causal grounding of visual elements. Another promising direction is to incorporate user feedback or human-in-the-loop supervision to dynamically refine the intervention policy during inference. Finally, we aim to explore the scalability of COAD in real-world applications such as assistive vision systems and visually grounded dialogue.

[134] p: In terms of limitations, like many other MLLMs, maliciously manipulated inputs could affect COAD’s performance. Another limitation is that COAD primarily targets object hallucination; extending the causal modeling framework to other forms of hallucination, such as attribute, relational, and global-scene inconsistencies, remains an important direction for future work. We defer a detailed discussion of limitations and potential mitigations to Appendix E .

[135] h2: References

[136] h2: Appendix A Details on Implementation and Causal Graphs

[137] p: Implementation Details. We finetune COAD on a subset of MSCOCO images sourced from the LLaVA dataset. To enable the model to incorporate the auxiliary input 𝐳 {\bf z} , we introduce a two-layer MLP projector (with hidden size 256 256 ) that maps 𝐳 {\bf z} into the token embedding space, following LLaVA’s multimodal token integration approach. We employ LoRA ( r = 128 r=128 , α = 256 \alpha=256 ), a cosine learning rate schedule with an initial learning rate of 4 ​ e − 5 4\text{e}{-5} , a batch size of 128, and train the model for 1 epoch. To mitigate the model’s dependence on prior context, we apply Gaussian noise ( σ = 0.005 \sigma=0.005 ) to the embeddings of previous tokens with a probability of 0.5 during training. During inference, we use sampling by default with temperature 0.2 and a maximum of 512 output tokens. In implementing Equation 4 , we find that it is more effective to perform fusion in the logit space rather than in the probability space. Therefore, we replace P ⁡ ( y f | 𝐒 , 𝐱 , 𝐳 ) P(y_{f}|{\bf S},{\bf x},{\bf z}) and P ⁡ ( y p | 𝐒 , 𝐱 ) P(y_{p}|{\bf S},{\bf x}) with their corresponding logits before computing the fused output, which is subsequently converted back to the probability space via softmax.

[138] p: All experiments were conducted on a single machine with 8 NVIDIA RTX A5000 GPUs (24GB each), an AMD EPYC 7282 16-Core Processor (64 threads), and 256GB RAM. Finetuning typically took around 16 hours per model. Caption generation on 5,000 images took between 30 minutes and 2 hours, depending on the generation length.

[139] p: For evaluation, we use sampling to generate outputs for all baseline methods, except for OPERA. Since OPERA is built on top of beam search, its outputs are generated using beam search with a beam size of 3 instead. For the hyperparameter α \alpha in COAD, we set it to 1.5 for text generation tasks (CHAIR and MMHal-Bench) and 0.1 for POPE.

[140] p: Causal Graphs and Hidden States. There are two different hidden states:

[141] p: The image-based, static hidden state 𝐳 {\bf z} , which corresponds to the output of the MLLM’s vision encoder (i.e., H v H_{v} that we will further explain in Appendix C ). In a causal MLLM such as LLaVA, the input follows the structure “image | user prompt | generated tokens” , and the hidden state of a token position is affected only by tokens that appear before it. Therefore, here 𝐳 {\bf z} is determined solely by the image and aligns most closely with our interpretation of the object belief variable 𝐳 {\bf z} in our causal graphs in Figure 4 and Figure 5 . It is not influenced by 𝐱 {\bf x} .

[142] p: The response-based, dynamic hidden state 𝐡 {\bf h} (or 𝐡 ( t ) {\bf h}^{(t)} ) , which corresponds to the hidden states when the MLLM generates the t t -th response token. These hidden states are influenced by 𝐱 {\bf x} .

[143] figure: (a) Casual graph with hidden states 𝐡 ( t ) {\bf h}^{(t)} . The hidden states that decide y ( t ) y^{(t)} are affected by 𝐒 {\bf S} , 𝐳 {\bf z} , and 𝐱 ( t ) {\bf x}^{(t)} . (b) Collapsing hidden states 𝐡 ( t ) {\bf h}^{(t)} into the generation of y ( t ) y^{(t)} . The resulting graph corresponds to the causal graph of COAD in Figure 5 . Figure 7 : The role of hidden states in the decoding causal graph of an MLLM. This figure illustrates a causal graph that explicitly includes token-level hidden states 𝐡 ( t ) {\bf h}^{(t)} during generation (a) , and shows that collapsing these hidden states into the generation of y ( t ) y^{(t)} yields an equivalent causal graph consistent with the one used by COAD (b) .

[144] p: We further clarify the role of the dynamic hidden state 𝐡 ( t ) {\bf h}^{(t)} in the causal graph shown in Figure 7 . In Figure 7(a) :

[145] p: the image 𝐒 {\bf S} generates the image-based, static hidden state 𝐳 {\bf z} ,

[146] p: 𝐒 {\bf S} , 𝐳 {\bf z} , and 𝐱 ( t ) {\bf x}^{(t)} then jointly generate (influence) the response-based, dynamic hidden state 𝐡 ( t ) {\bf h}^{(t)} , and

[147] p: 𝐡 ( t ) {\bf h}^{(t)} then influences the generated token y ( t ) y^{(t)} .

[148] p: As shown in Figure 7(b) , we can actually collapse h ( t ) h^{(t)} and the red part of Figure 7(a) to have an equivalent causal graph in Figure 7(b) , which matches our causal graphs in Figure 4 and Figure 5 .

[149] h2: Appendix B Evidence of Hallucinatory Object Beliefs in LLaVA

[150] p: To examine whether a multimodal LLM (MLLM) can form incorrect internal beliefs about object existence (corresponding to an incorrect 𝐳 {\bf z} in our formulation), we conduct a linear-probe experiment on LLaVA. The goal is to determine whether LLaVA forms internal object-existence beliefs that deviate from the actual content of the image.

[151] h3: B.1 Experimental Setup

[152] p: We train a linear classifier to probe whether LLaVA internally believes each object category to be present in the image. The classifier

[153] p: takes as input the embedding for each token, and

[154] p: outputs a C C -dimensional vector 𝐨 ∈ [ 0 , 1 ] C {\bf o}\in[0,1]^{C} indicating the estimated probability that each of the C C objects exists in the image.

[155] p: Here, 𝐨 {\bf o} reflects the MLLM’s object-existence belief in its hidden states, which we mentioned in Appendix A .

[156] p: Input to the Linear Probe. For each token in the dialog sequence, LLaVA produces a hidden state after every transformer decoder layer. We concatenate these hidden states together with the embedding before the first layer to obtain the probe input. Thus, each token in the prompt-response sequence contributes one training sample for the linear probe.

[157] p: Conversation Sampling. We collect dialogs generated by LLaVA using MSCOCO images and the prompt “Please describe every object in this image in detail.” After LLaVA completes the response, we extract hidden states for all tokens (including image tokens, query tokens, and generated response tokens) to construct probe input samples.

[158] p: Target Labels. For each image, we run LLaVA once with the same prompt and use a rule-based method to determine whether each object category is mentioned in the resulting text description. These detected mentions serve as labels for training the linear probe. The same label is assigned to all probe samples within a given image-prompt-response tuple.

[159] p: Discussion on the Relation between Input to the Linear Probe and the Hidden States. In a causal MLLM such as LLaVA, the input follows the structure “image | user prompt | generated tokens” , and the hidden state of a token position is affected only by tokens that appear before it. Therefore:

[160] p: when the input to the linear probe is the hidden state in the “image” part, the output 𝐨 {\bf o} serves as an estimation of the image-based, static hidden state 𝐳 {\bf z} ;

[161] p: when the input to the linear probe is the hidden state in the “generated tokens” part, the output 𝐨 {\bf o} serves as an estimation of the response-based, dynamic hidden state 𝐡 {\bf h} (or 𝐡 ( t ) {\bf h}^{(t)} ) .

[162] figure: (a) Linear-probe output 𝐨 {\bf o} for object probabilities in LLaVA. (b) Visualization of probed probability of the object “bench” over all image tokens. (c) LLaVA’s response hallucinates the object “ benches ”. (d) COAD eliminates the bench-related hallucination. Figure 8 : Visualization of LLaVA’s hallucinatory object beliefs. This figure provides empirical evidence that LLaVA can form incorrect internal object-existence beliefs (corresponding to an incorrect 𝐳 {\bf z} ) and shows how COAD corrects the resulting hallucination. (a) Linear-probe output of LLaVA’s object probabilities for all tokens over the full dialog, showing that the probed probability for the object “bench” increases both around certain image tokens and around the tokens where LLaVA actually generates the word “benches” (in red boxes). (b) The baseline LLaVA’s probed probability of the object “bench” over the image tokens (patches), showing high “bench” probabilities in some image tokens (highlighted in yellow); this indicates that the hallucinated belief may originate from the image-perception stage. (c) LLaVA hallucinates the object “bench” in the response. (d) COAD’s response, which eliminates the bench hallucination.

[163] h3: B.2 Findings

[164] p: We apply the trained linear probe to a sampled conversation and visualize the predicted object probabilities over time (Figure 8 ).

[165] p: The input image contains a person riding a skateboard with no benches in the background.

[166] p: The probe output in Figure 8 (a) indicates that LLaVA internally assigns a high probability (i.e., brighter, yellow color in the heatmap) to a nonexistent bench around certain image-token positions.

[167] p: Figure 8 (b) shows LLaVA’s probed probability of the object “bench” over the image tokens (patches), demonstrating high “bench” probabilities in some image tokens (highlighted in yellow); this indicates that the baseline LLaVA’s hallucinated belief may originate from the image-perception stage.

[168] p: Figure 8 (c) shows that LLaVA hallucinates the object “bench” in the response.

[169] p: In contrast, COAD produces a response that does not mention any benches, as shown in Figure 8 (d).

[170] h3: B.3 Conclusion

[171] p: This experiment demonstrates that LLaVA can form incorrect internal beliefs about object existence, i.e., it may estimate an incorrect 𝐳 {\bf z} for certain objects, which subsequently leads to hallucinations. These results provide direct empirical evidence for the assumption illustrated in Figure 1 of the main paper.

[172] h2: Appendix C LLaVA Architecture and the Formation of Visual Features

[173] figure: Figure 9 : Simplified LLaVA architecture ( Liu et al., 2024c ) . The image is encoded by a vision encoder and then projected into the language model’s embedding space. The resulting visual embeddings H v H_{v} are inserted as image tokens. Because H v H_{v} is computed independently of textual tokens, the object-belief variable 𝐳 {\bf z} corresponding to H v H_{v} remains fixed during decoding. (This figure is adapted from ( Liu et al., 2024c ) .)

[174] p: To clarify why the object-belief variable 𝐳 {\bf z} is treated as time-invariant in the causal model of a standard MLLM (Section 3.4 ), we briefly describe the relevant components of the LLaVA architecture. A schematic diagram is shown in Figure 9 .

[175] h3: C.1 Visual Feature Extraction Before Language Interaction

[176] p: In LLaVA, the input image is first processed by a vision encoder (e.g., CLIP’s ViT backbone) to produce a set of image features, denoted Z v Z_{v} . These features are then passed through a projector layer to obtain the final visual embeddings H v H_{v} , which are fed into the language model.

[177] p: Importantly:

[178] p: Both the vision encoder and the projector operate independently of the language model.

[179] p: No textual tokens are involved when computing Z v Z_{v} or H v H_{v} .

[180] p: The visual embeddings H v H_{v} remain fixed throughout decoding.

[181] p: The projected embeddings H v H_{v} are inserted into the token sequence as “image tokens,” and only after this insertion does the multimodal Transformer start attending jointly over image tokens and text tokens.

[182] h3: C.2 Relation to the Object-Belief Variable 𝐳 {\bf z}

[183] p: In our causal formulation, the variable 𝐳 {\bf z} represents the model’s internal belief about which objects exist in the image. Conceptually, 𝐳 {\bf z} corresponds to the portion of the visual embeddings H v H_{v} that encode object presence or absence. Since H v H_{v} is generated solely from the image (via the vision encoder and projector) and does not depend on previously generated text tokens, 𝐳 {\bf z} is naturally treated as a static variable. This matches the assumption used in Section 3.4 , where only 𝐱 ( t ) {\bf x}^{(t)} and y ( t ) y^{(t)} evolve over time.

[184] h2: Appendix D Further Analysis of Ablation Studies

[185] p: Effect of Finetuning and Effectiveness of Our Causal Decoding Algorithm. Since COAD involves finetuning an MLLM, a natural question is whether the observed gains are simply due to finetuning rather than our proposed causal decoding algorithm. To examine this, we directly evaluate the finetuned model M f M_{f} without applying our decoding strategy. As shown in Table 1 , M f M_{f} alone achieves only part of the improvements, indicating that finetuning by itself cannot account for the performance of COAD and verifying the effectiveness of our causal decoding algorithm.

[186] p: Role of the Vector 𝐳 \mathbf{z} . Another question is whether the improvements come merely from contrasting M f M_{f} and M p M_{p} during causal fusion, regardless of our vector 𝐳 \mathbf{z} . To verify this, we remove 𝐳 \mathbf{z} when training M f M_{f} (i.e., a standard finetuning setting) and then apply our causal decoding procedure using this variant of M f M_{f} . The results from Table 1 show a clear drop compared to COAD, demonstrating that 𝐳 \mathbf{z} plays an essential role in enabling effective causal fusion.

[187] h2: Appendix E Limitations and Future Work

[188] p: Dependence on Finetuning. Our approach currently requires a LoRA finetuning step for adaptation. While this is practical in many settings, it reduces the plug-and-play convenience of COAD. We experimented with a training-free variant that injects the causal vector directly as a prompt, which already yields strong improvements on POPE benchmarks (e.g., F1-Rand = 95.4, F1-Pop = 90.0, F1-Adv = 85.8), outperforming all baselines. However, this variant is more sensitive to detector errors and less robust on captioning tasks. These results nonetheless highlight the generality of COAD and suggest promising directions for reducing computational cost, such as improving detector reliability or designing dedicated training methods that allow a single MLLM to simulate the causal signal.

[189] p: Domain Mismatch. COAD relies on detectors trained on specific distributions. If the test image domain diverges significantly, the causal signal may become insufficient. One direction is to investigate zero-shot or domain-adaptive detectors to mitigate this issue.

[190] p: Adversarial Vulnerability. Maliciously manipulated inputs or detector outputs could affect COAD’s performance. However, its modular design allows for safeguard components (e.g., adversarial detection at the detector level), which we leave as future extensions.

[191] p: Residual Text Priors. In rare cases with extremely strong linguistic priors, causal interventions may not fully suppress hallucinations. In rare cases with extremely strong linguistic priors, causal interventions may not fully suppress hallucinations. Future improvements may involve designing stronger intervention mechanisms or complementary signals that better counteract such priors.

[192] p: Scope and Generality. Our study mainly targets object hallucinations. Broader validation on other types of hallucinations and across more MLLMs is a promising next step, facilitated by COAD’s general token-based interface.

[193] h2: Appendix F More Qualitative Examples

[194] p: We provide more qualitative examples in Figure 10 and Figure 11 , where MSCOCO objects mentioned in the text are highlighted in red (hallucinated) or green (correct).

[195] figure: 𝐳 {\bf z} -vector: [person: 0.93, handbag: 0.76, cell phone: 0.72, potted plant: 0.5, clock: 0.26, bottle: 0.24, bench: 0.2 , …] LLaVA: A woman is sitting on a bench , holding a cell phone and talking to another woman. They are both wearing sandals. COAD: A woman in a pink shirt holds a cell phone , while another woman in a dress sits next to her. 𝐳 {\bf z} -vector: [toilet: 0.86, cat: 0.84, book: 0.46, dog: 0.17 , …] LLaVA: A dog is standing on a toilet , sniffing the toilet bowl. The toilet lid is open, and the dog appears to be curious about the water inside. COAD: A cat is sitting on the toilet and appears to be drinking water from the toilet bowl . 𝐳 {\bf z} -vector: [train: 0.91, chair: 0.26, bird: 0.21, bench: 0.2 , person: 0.16, clock: 0.15, traffic light: 0.14, …] LLaVA: A yellow and white train is traveling down the tracks, pulling into a station. The train is positioned next to a building, and there is a bench nearby for passenger to sit. The scene is captured on November 1, 2012. COAD: A train is stopped at a train station, and there is a yellow line on the platform. 𝐳 {\bf z} -vector: [banana: 0.87, apple: 0.87, orange: 0.83, bowl: 0.33, dining table: 0.28 , wine glass: 0.11, cup: 0.05, …] LLaVA: A clear glass plate is filled with a variety of fruits, including apple , orange , and a banana. The plate is placed on a table , and the fruits are arranged in a visually appealing manner. COAD: A clear glass plate holds a variety of fruits, including banana , apple , pears, and an orange . Figure 10 : Case studies on hallucination reduction.

[196] figure: 𝐳 {\bf z} -vector: [laptop: 0.88, bed: 0.86, suitcase: 0.63, keyboard: 0.44, mouse: 0.42, backpack: 0.36, handbag: 0.33, cell phone: 0.31 , remote: 0.15, person: 0.14, …] LLaVA: A bed with a laptop and a cell phone on it. The bed is unmade and has a striped blanket. There is also a suitcase on the bed , and a pair of glasses nearby. COAD: A laptop is sitting on top of a bed next to a suitcase . 𝐳 {\bf z} -vector: [hot dog: 0.91, person: 0.77, sandwich: 0.31, bottle: 0.16, pizza: 0.07, …, dining table: 0.04 , …] LLaVA: A person is holding a hot dog with cheese and ketchup on a bun. The hot dog is placed on a table , and the person ’s hand is visible in the foreground. COAD: A hot dog with ketchup and cheese being held by a person . 𝐳 {\bf z} -vector: [bicycle: 0.89, person: 0.83, motorcycle: 0.75, backpack: 0.34, bottle: 0.27, handbag: 0.18, …, chair: 0.05 , …] LLaVA: A man is working on a motorcycle in a garage, standing on a red stool to reach the motorcycle. He is wearing jeans and a black shirt. The motorcycle is parked on a lift, and there are other motorcycle in the background. COAD: A man is working on a motorcycle , lifting the front wheel off the ground using a lift. 𝐳 {\bf z} -vector: [person: 0.85, bird: 0.83, cup: 0.83, sandwich: 0.64, bench: 0.55 , dining table: 0.5, fork: 0.33, chair: 0.32, knife: 0.22, …] LLaVA: A bird is standing on a plate with a half-eaten sandwich , which is placed on a dining table. The bird seems to be interested in the sandwich , possibly trying to get a bite. The scene takes place near a body of water, with a bench nearby. COAD: A half-eaten sandwich sits on a plate with ketchup, and a bird is standing nearby, possibly interested in the remaining food. Figure 11 : Case studies on hallucination reduction.

[197] h2: Instructions for reporting errors

[198] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[199] p: Tip: You can select the relevant text first, to include it in your report.

[200] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[201] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
