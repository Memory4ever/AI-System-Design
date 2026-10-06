[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Asymmetric Idiosyncrasies in Multimodal Models

[3] h6: Abstract

[4] p: In this work, we study idiosyncrasies in the caption models and their downstream impact on text-to-image models. We design a systematic analysis: given either a generated caption or the corresponding image, we train neural networks to predict the originating caption model. Our results show that text classification yields very high accuracy (99.70%), indicating that captioning models embed distinctive stylistic signatures. In contrast, these signatures largely disappear in the generated images, with classification accuracy dropping to at most 50% even for the state-of-the-art Flux model. To better understand this cross-modal discrepancy, we further analyze the data and find that the generated images fail to preserve key variations present in captions, such as differences in the level of detail, emphasis on color and texture, and the distribution of objects within a scene. Overall, our classification-based framework provides a novel methodology for quantifying both the stylistic idiosyncrasies of caption models and the prompt-following ability of text-to-image systems. Our project page is publicly available at muzi-tao.github.io/asymmetric-idiosyncrasies .

[5] h2: 1 Introduction

[6] p: Synthetic data now plays a central role in training and scaling multimodal systems [ 4 , 13 , 16 ] . In state-of-the-art image generation pipelines (e.g., DALL·E 3 [ 3 ] , Playground v3 [ 18 ] , Qwen-image [ 38 ] ), model-generated captions are used to expand training corpora and to refine text–image alignment. This practice implicitly assumes that captions are (i) stylistically neutral or at least interchangeable across captioning models, and (ii) faithfully convertible into visual content by text-to-image (T2I) models. Both assumptions are under-examined.

[7] p: A growing body of work shows that language models imprint stable, model-specific fingerprints that enable source attribution from text [ 11 , 22 , 37 , 31 ] . Similar dataset and model signatures have been reported in the vision domain [ 35 , 5 , 40 , 20 ] . However, it remains unclear whether caption-level idiosyncrasies produced by vision–language models (VLMs or MLLMs) [ 1 , 23 , 19 , 12 ] propagate into the images produced by downstream T2I systems. If such cross-modal transfer is weak, synthetic-caption pipelines could quietly introduce distributional biases at the text stage that do not materialize visually, complicating the use of captions as faithful supervisory signals.

[8] p: We investigate this question using a simple, model-agnostic approach based on “name-that-model” classification on both sides of the caption–image interface. Given an image and a prompt, multiple captioning models produce captions; we first train a text classifier to attribute each caption to its source model. We then feed those same captions into a fixed T2I model and train an image classifier to attribute the generated images to the caption source. If caption idiosyncrasies reliably transfer across modalities, attribution should remain high in the image domain; if not, we obtain a direct, quantitative, and interpretable measure of a cross-modal translation gap.

[9] figure: Figure 1 : Overview of our pipeline. Multiple MLLMs generate captions for the same image, and a text classifier reliably attributes each caption to its source model. These captions are then used to synthesize new images, on which an image classifier performs the same source-identification task. While text-based attribution is highly accurate, image-based attribution fails, which reveals a clear mismatch between caption-space and image-space model signatures.

[10] p: Empirically, caption idiosyncrasies are highly pronounced in text but largely dissipate when transferred into images. On 30k captions per model spanning diverse image sets, a straightforward BERT-based classifier [ 8 ] achieves 99.70% accuracy in identifying the captioning model. In contrast, after rendering those captions with modern T2I systems, image-space attribution drops substantially, peaking at only around 50% with the current best model Flux-schnell [ 15 ] , which is only modestly above the 33.3% chance level for three classes. As a strong reference point, the identical image classifier achieves approximately 76.7% accuracy when distinguishing natural image sources of comparable scale, underscoring that the difficulty is specific to generated images rather than to the classifier itself.

[11] p: To understand the behavior, we analyze linguistic and content features of captions. TF–IDF phrase statistics, color/texture vocabularies, and compositional terminology reveal stable, model-specific preferences (e.g., viewpoint/angle wording, ambience/lighting emphasis, or concise compositional framing). We find that paraphrasing the caption still preserves over 95% attribution accuracy. This provides strong evidence that the fingerprints extend beyond surface phrasing to choices about what to describe and how to structure it. Yet many of these choices fail to manifest reliably in the generated images, especially along axes such as level of detail, nuanced color/texture, and object layout.

[12] p: These results provide an operational measure of a cross-modal idiosyncratic gap: stylistic and content-selection signals that are strong in captions are not faithfully realized by current T2I models. Practically, this suggests that (i) aggregating captions from diverse captioners may inject text-domain biases that do not become visual supervision, and (ii) instruction-following in T2I remains a key bottleneck for transferring caption semantics beyond object keywords.

[13] p: We propose a simple, scalable attribution framework that quantifies model-specific idiosyncrasies on both captions and the images generated from them.

[14] p: Using this framework, caption-based source attribution is nearly perfect at 99.70%, whereas attribution from the corresponding generated images is substantially weaker, reaching only about 50%. This contrast highlights a significant gap in cross-modal translation.

[15] p: Through lexical and structural analyses, including TF–IDF phrases, color and texture vocabularies, composition-related terms, and paraphrasing robustness tests, caption fingerprints are traced to deeper content-selection and perspective patterns. These patterns are not preserved by current T2I models.

[16] p: Finally, we propose attribution-as-evaluation as a complementary metric for prompt-following: instruction following should increase the transfer of caption idiosyncrasies into images, narrowing the gap.

[17] h2: 2 Background

[18] h3: 2.1 Idiosyncrasies in Large Language Models

[19] p: Large language models achieve remarkable performance across diverse tasks by leveraging the statistical and semantic regularities embedded in large-scale corpora. Beyond their generalization capabilities, recent studies reveal that LLMs also exhibit stable, model-specific idiosyncrasies in generated text. These idiosyncrasies, expressed as consistent stylistic and distributional patterns, act as implicit fingerprints that make outputs attributable to their source models [ 11 , 22 , 37 ] . Building on this view, Sun et al. [31] formalize an attribution task in which a classifier predicts the source model from generated samples. They show that such fingerprints persist across model families and prompting conditions, suggesting that differences extend beyond surface token statistics. Similar findings appear in authorship attribution and neural text forensics [ 36 , 2 , 9 ] , where stylistic or distributional features reveal model origin even under paraphrasing or translation. These observations naturally raise the question of whether analogous signatures also arise in multimodal settings.

[20] h3: 2.2 Idiosyncrasies in Vision and Vision-Language Models

[21] p: Idiosyncratic signatures are not confined to text. In computer vision, classic studies show that simple classifiers can reliably distinguish between datasets, revealing systematic biases beyond semantic content [ 35 , 5 ] . Similar effects are observed in generative models: diffusion- and GAN-based systems often imprint dataset- or model-specific artifacts that enable reliable attribution [ 40 , 21 , 32 ] . These results suggest that high-dimensional visual data still carries persistent distributional cues.

[22] p: With the rise of vision-language models (VLMs), such concerns extend across modalities. Models like CLIP learn joint embeddings of text and vision [ 26 ] , yet representations or downstream outputs may still reflect stylistic biases inherited from training. Recent work highlights that VLMs, when used for captioning or generation, can produce model-specific vocabulary, style, or narrative emphasis [ 31 , 9 ] . What remains unclear is whether these linguistic fingerprints propagate across modalities, specifically from captions into the images synthesized by downstream text-to-image systems. This question motivates our analysis.

[23] h2: 3 Idiosyncrasies in Generated Image Captions

[24] p: Prior research has demonstrated that large language models exhibit model-specific idiosyncrasies in their outputs. In this work, we ask: Does this observation apply to MLLMs and their downstream application, such as captioning?

[25] h3: 3.1 Experimental Setup

[26] p: To investigate caption idiosyncrasies across different MLLMs, we formulate a classification task. Given a prompt p ∈ 𝒫 p\in\mathcal{P} and an image x ∈ 𝒳 x\in\mathcal{X} , each model M k M_{k} produces a caption c = M k ​ ( p , x ) c=M_{k}(p,x) , where 𝒞 k \mathcal{C}_{k} is the set of captions from M k M_{k} . Each caption c i ∈ 𝒞 k c_{i}\in\mathcal{C}_{k} is paired with a label y i = k y_{i}=k , indicating its source model. For K K MLLMs, a K K -way classifier is trained to predict y i y_{i} from c i c_{i} . If caption distributions overlap heavily, accuracy should approach random guessing ( 1 / K 1/K ); substantially higher accuracy indicates model-specific linguistic fingerprints.

[27] p: The image pool is constructed from several widely used datasets. Specifically, we sample 10,000 images in total: 3,000 each from the validation sets of CC3M [ 29 ] , COCO [ 17 ] , and ImageNet [ 6 ] , plus 1,000 from MNIST [ 7 ] .

[28] p: For caption generation, we employ three proprietary MLLMs: Claude-3.5-Sonnet [ 1 ] , Gemini-1.5-Pro [ 33 ] , GPT-4o [ 14 ] , all accessed via their official APIs, and one open-sourced MLLM Qwen3-VL [ 34 ] . To capture linguistic diversity and range, we design three progressively detailed prompts for every image. These prompts elicit different levels of granularity and complexity, enabling a systematic comparison of captioning styles, lexical choices, and narrative depth across models under uniform prompting conditions. Specifically, the three prompts are as follows:

[29] p: Coarse captioning prompt:

[30] p: Detailed captioning prompt:

[31] p: Very detailed captioning prompt:

[32] p: The maximum output length is set to 1024 tokens for Prompts 1 and 2, and 4096 for Prompt 3, enabling more detailed descriptions. Captions were split 80%/20% randomly, yielding 72k training and 18k test samples, with all prompts of the same image allocated consistently. For classification, BERT-base-uncased [ 8 ] was fine-tuned with a [CLS]-based linear head to predict the generating model. Training used the AdamW optimizer with a learning rate of 2 × 10 − 5 2\times 10^{-5} , weight decay 0.01 0.01 , batch size 32, 3 epochs, and dropout p = 0.1 p=0.1 , with a linear decay schedule.

[33] figure: Table 1: Caption classification accuracy (%). Claude-3.5-Sonnet Gemini-1.5-Pro GPT-4o Qwen3-VL Total 99.83 99.78 99.67 – 99.76 99.92 99.90 – 99.73 99.85 99.85 – 99.62 99.13 99.53 – 99.73 99.80 99.53 99.60 99.62 99.65 99.57 99.30 99.53

[34] h3: 3.2 Model-Specific Fingerprints in Captions

[35] p: As shown in Table 1 , the classifier achieves an overall accuracy of 99.53% , far above the random baseline of 25%. This near-perfect performance indicates that captions from different MLLMs contain highly distinctive linguistic signals, despite being generated under identical image and prompt conditions. In other words, outputs from Claude-3.5-Sonnet, Gemini-1.5-Pro, GPT-4o, and Qwen3-VL exhibit consistent stylistic or lexical fingerprints that enable reliable attribution.

[36] p: Per-class accuracies are also uniformly high, each exceeding 99.13%. This suggests that fingerprints are not confined to a single model but are shared across all four. Together, these results confirm that stylistic biases are a systematic property of MLLM captioning rather than an isolated artifact.

[37] h3: 3.3 Word Distribution Analysis

[38] p: We next analyze word distributions to understand what makes captions from different models so separable. We apply TF-IDF [ 30 ] ranking of 2-grams and 3-grams to the generated captions. For each model, we compute the top ten scoring phrases and list them in Table 2 , which provides representative lexical patterns. The results reveal clear biases: Claude frequently emphasizes lighting and visibility (e.g., “lighting suggests,” “black,” “white”), Gemini highlights perspective and resolution (e.g., “slightly low angle,” “impression,” “partially visible”), GPT favors categorical or structural terms (e.g., “image depicts,” “feature,” “wall”), and Qwen centers on subjective prominence, contrast, and depth cues (e.g., “central focus,” “depth field,” “high contrast”). These tendencies reflect stable narrative preferences: Claude focuses on ambience, Gemini emphasizes viewpoint, GPT prioritizes compositional framing, and Qwen highlights subject prominence. Word clouds (Figure 2 ) further confirm these stylistic differences.

[39] figure: Table 2: Top distinctive TF-IDF phrases for each captioning model (generic appearance descriptors removed). Rank Claude-3.5-Sonnet Gemini-1.5-Pro GPT-4o Qwen3-VL 1 lighting suggests overall impression image depicts detailed description 2 visible background low resolution image features high contrast 3 light colored slightly low angle person wearing central focus 4 appears taken close slightly low handwritten digit main subject 5 photo taken eye level view lush green depth field 6 lighting creates high angle view sunny day shallow depth field 7 depth field light gray clear blue black background digit 8 composition creates partially visible handwritten number white number 9 overall composition overall lighting setting appears visible elements 10 scene appears slightly high angle partially visible image captures

[40] figure: (a) Claude-3.5-Sonnet (b) Gemini-1.5-Pro (c) GPT-4o (d) Qwen3-VL Figure 2 : Word clouds of model-generated captions

[41] p: These findings show that the four models adopt stable yet distinct descriptive strategies. Such consistent preferences extend beyond individual words, forming recognizable linguistic fingerprints that explain the high classification accuracy. They further suggest that MLLMs inject narrative biases into captions, which may shape how downstream systems interpret the same images (Section 4 ).

[42] h2: 4 Image Generation with Stylish Captions

[43] p: Given the strong idiosyncrasies observed in captions, a natural question is whether these stylistic signals transfer into the images generated from them. Do captions from different MLLMs yield visually distinctive images, or do generative models normalize such differences?

[44] h3: 4.1 Experimental Setup

[45] p: Our method adopts a parallel setup on the image side. Fixing a text-to-image generator G G , we use captions c i ∈ 𝒞 k c_{i}\in\mathcal{C}_{k} from captioning models M k ∈ { M 1 , M 2 , … , M K } M_{k}\in\{M_{1},M_{2},\dots,M_{K}\} as input. This produces generated images

[46] table: x ^ i = G ⁡ ( c i ) , with label ​ y i = k ​ if ​ c i ∈ 𝒞 k . \hat{x}_{i}=G(c_{i}),\quad\text{with label }y_{i}=k\text{ if }c_{i}\in\mathcal{C}_{k}.

[47] figure: Figure 3 : Classification performance on generated images. The test accuracy of image classification on generated images is 49.85% with the SOTA model FLUX.1-schnell, while classification on a natural image dataset [ 20 ] of the same scale using the same network achieves 76.7%. Random guessing yields 33.3%.

[48] p: We then train an N N -way classifier over the generated images x ^ i \hat{x}_{i} to predict the originating captioning model M k M_{k} . As in the text domain, classification accuracy above random chance ( 1 / N 1/N ) would indicate that model-specific idiosyncrasies persist in the generated images.

[49] p: For image-side experiments, we use captions from Claude-3.5-Sonnet, Gemini-1.5-Pro, and GPT-4o, and render them with several widely used T2I systems: Stable Diffusion v1.5 [ 28 ] , Stable Diffusion v2.1 [ 24 ] , Stable Diffusion XL [ 24 ] , and FLUX.1-schnell [ 10 ] . Following Liu and He [20] , we adopt comparable training settings for the image classifier. Specifically, we use a ResNet-18 backbone trained for 300 epochs with a batch size of 64, the AdamW optimizer (learning rate 5 × 10 − 4 5\times 10^{-4} , weight decay 0.05), and standard augmentation including Mixup [ 42 ] ( α = 0.8 \alpha=0.8 ) and CutMix [ 41 ] ( α = 1.0 \alpha=1.0 ). We also apply label smoothing (0.1) and a warmup schedule of 20 epochs.

[50] h3: 4.2 Failure of Caption Fingerprints to Transfer

[51] p: Despite the near-perfect attribution observed for captions, classification on generated images is far less successful. As shown in Figure 3 , the best-performing model (Flux-schnell) reaches only 49.85% accuracy, barely above random guessing (33.3%) and well below the 76.7% accuracy achieved on natural images of similar scale [ 20 ] . This indicates that the distinctive linguistic fingerprints of captions largely vanish once translated into the visual domain.

[52] h3: 4.3 Ablation Study

[53] p: To better understand this discrepancy and further validate the finding, ablation studies are performed on top of the initial experiments.

[54] h4: Adding original images as a fourth class.

[55] p: To test whether the observed gap also holds against natural data, the 10k original images used as inputs to the captioning models are included as an additional class in the image classifier, yielding a 4-way classification setting with three generated-image classes and one natural-image class. The table below reports the results.

[56] figure: Model Total Claude Gemini GPT Original Accuracy (%) 51.84 50.83 56.31 38.30 82.11

[57] p: Overall accuracy in this setup is 51.84%. Among the generated images, samples from Gemini are slightly more distinguishable; GPT is the hardest to classify. In contrast, the original images reach 82.1% accuracy. This highlights a substantial gap in identifiable idiosyncrasy between natural and generated data.

[58] h4: Classification on keyword-prompts.

[59] p: To control for narrative style, we evaluate keyword-only prompts by first extracting keywords from each caption and then using the resulting keyword prompt to generate an image with FLUX-schnell. We run attribution on both the keyword prompt and the corresponding generated image. Results are below:

[60] figure: Gemini GPT Claude Total keywords 95.37 94.48 88.73 92.86 images 46.67 41.34 41.56 43.22

[61] p: Text attribution remains high, while visual attribution stays low, indicating that captioner-specific cues are not primarily driven by stylistic fingerprints and are still largely not preserved through T2I generation.

[62] h4: Classification on extracted features.

[63] p: The dependence of the conclusion on the classifier architecture is further examined. Instead of training a convolutional network end-to-end, CLIP image features are extracted, and a linear classifier with SGD is trained with fixed hyperparameters across generation models. The test accuracies are reported below.

[64] figure: Model Flux-schnell SDXL SD 2.1 SD 1.5 Accuracy (%) 46.05 45.69 44.76 41.67

[65] p: Test accuracies remain low, ranging from 41.69% to 46.05%. The narrow spread and uniformly modest performance indicate that the difficulty in distinguishing generated images is not due to classifier choice or feature representation, but reflects the intrinsic similarity of the generated samples.

[66] h2: 5 The Idiosyncratic Gap Between Image Captioning and Generation Models

[67] p: The classification results raise a key question: Why are captions from different MLLMs easily distinguishable, while the corresponding generated images are not?

[68] p: Intuitively, if the distinctive tokens in captions were faithfully mapped into the visual modality, their signatures should also appear in generated images. Moreover, given the vast pixel space and color range available, images should, in principle, be capable of encoding more information than a short caption. The failure of this transfer suggests that some informative features are lost during generation, whether genuinely valuable or merely stylistic.

[69] h3: 5.1 Linguistic Analysis on the Captions

[70] p: Attribution robustness to superficial cues is examined by modifying and paraphrasing captions before re-running classification. Simple edits include removing formatting, deleting special characters, and shuffling words or letters. In addition, we generate paraphrases using Qwen2.5 [ 39 ] with multiple prompting templates.

[71] figure: Table 3: Total and per-class accuracy under different text modifications and paraphrases. Paraphrasing was performed with three distinct prompts on Qwen-2.5-1.5B-Instruct and Qwen-2.5-7B-Instruct to ensure robustness across rewording styles and model scales. Detailed information about prompts is provided in Appendix B . Text Transformation Total Claude-3.5-Sonnet Gemini-1.5-Pro GPT-4o Removing Markdown Format 99.71 99.73 99.62 99.77 Removing Special Characters 99.78 99.78 99.78 99.77 Shuffling Words 99.42 99.43 99.60 99.23 Shuffling Letters 34.49 0.00 100.00 3.48 Paraphrase 1 ( Qwen-2.5-1.5B-Instruct ) 95.59 94.35 95.45 97.95 Paraphrase 1 ( Qwen-2.5-7B-Instruct ) 95.90 92.68 97.73 97.30 Paraphrase 2 ( Qwen-2.5-1.5B-Instruct ) 97.28 95.90 97.78 98.17 Paraphrase 2 ( Qwen-2.5-7B-Instruct ) 97.90 96.43 99.10 98.17 Paraphrase 3 ( Qwen-2.5-1.5B-Instruct ) 96.31 94.87 96.50 97.57 Paraphrase 3 ( Qwen-2.5-7B-Instruct ) 95.81 90.97 98.47 98.02

[72] p: As shown in Table 3 , idiosyncrasies lie primarily at the word level rather than at individual characters, consistent with prior findings on LLMs [ 31 ] . Even after paraphrasing, classification accuracy remains above 90%, confirming that model-specific signals are not reducible to surface form, but reflect deeper factors such as descriptive perspective and content selection. Further qualitative analyses indicate that Claude-3.5-Sonnet tends to adopt a narrative, context-oriented framing, Gemini-1.5-Pro emphasizes camera perspective and exhaustive detail, and GPT-4o produces concise summaries focusing on salient objects and layout. These differences motivate a closer examination of how models encode and transmit visual content.

[73] h3: 5.2 Probing T2I Encoders

[74] p: The robustness to paraphrasing indicates that caption idiosyncrasies reflect deeper structural choices rather than superficial phrasing. This raises a natural question: does this signal survive the first stage of the text-to-image pipeline, the text encoder?

[75] p: To examine this, we analyze the core encoders used in modern T2I systems. We reuse the linear-probe setup from our text classification task, but apply it directly to the final embeddings produced by T5 [ 27 ] and CLIP [ 25 ] . If the encoder collapses or homogenizes stylistic cues, classification accuracy should drop substantially.

[76] p: As shown in Table 4 , both encoders retain model-specific signals to a substantial degree. The T5 encoder preserves nearly all stylistic information (99.74%), while CLIP also maintains high separability (94.14%). These results indicate that the text encoders faithfully transmit caption-level fingerprints rather than discarding them. This finding rules out the encoder as the primary source of the cross-modal gap. Since the stylistic signal reaches the generator largely intact, the discrepancy must arise in later stages of the pipeline. We therefore turn to the generation process itself to understand where the signal is diminished.

[77] figure: Table 4: Linear probe accuracy(%) on T2I text encoder embeddings. The stylistic signal is overwhelmingly preserved, not lost. Encoder Claude Gemini GPT Average CLIP 94.47 95.1 92.85 94.14 T5 99.73 99.82 99.67 99.74

[78] h3: 5.3 Image–Prompt Attribution in CLIP Space

[79] p: To test whether textual idiosyncrasies survive the generation process, we design a 3-way image–prompt attribution task. For each generated image, we retrieve the three captions with the same prompt index (one from each model). Since the image is produced from exactly one of them, the classifier must choose which captioning model is correct.

[80] p: We freeze a CLIP text encoder, use precomputed image embeddings, and learn small linear projections that map both modalities into a shared space. If model-specific signals in the captions were faithfully transferred into the images, the classifier should recover the originating model with high accuracy.

[81] figure: Model Claude Gemini GPT Average Accuracy (%) 54.40 55.00 49.63 53.01

[82] p: As shown in the above table, attribution accuracy is only marginally above chance and far below the near-perfect scores achieved in the caption domain. Even with the correct three candidate texts provided, the classifier cannot reliably recover which model produced the image, indicating that most textual signatures do not clearly manifest in the visual output. This weak transfer motivates a closer examination of what visual content is actually preserved during generation, which we investigate next.

[83] h3: 5.4 Visual Content Analysis

[84] figure: Figure 4 : Comparison of captions generated by Claude-3.5-Sonnet, Gemini-1.5-Pro, and GPT-4o on the same images. Each row shows the original image on the left and, on the right, the captions generated by the three models and the images synthesized from those captions. The model outputs reveal several systematic failures across different attribute types. (i) In the first row, a simple descriptive color term, such as blue, without any accompanying texture specification, leads all models to produce images with broadly similar color–texture effects. However, none of the models reproduces the true, darker color in the original image. (ii) In the second column, even though captions include explicit view descriptions, the generated viewpoints remain inconsistent: a caption describing a high-angle view yields an eye-level rendering, while an eye-level description produces a low-angle output. (iii) In the third row, different color terms used to describe the acorn result in images that are still visually similar across models, and none of them match the actual color or appearance of the original image.

[85] p: The attribution experiments above show a consistent pattern: model-specific idiosyncrasies are strong and robust in text, yet much weaker in the generated images. To better understand where this information is attenuated, we complement the quantitative results with a more detailed analysis of the generated content.

[86] p: Figure 4 presents representative examples. For each real image, we show the three captions produced by Claude-3.5-Sonnet, Gemini-1.5-Pro, and GPT-4o, together with the images synthesized from those captions. Although the captions differ substantially in descriptive detail, color terminology, viewpoint specification, and texture vocabulary, the generated images remain visually similar across models. In many cases, even explicit attributes in the caption (e.g., “dark blue”, “shot from a high angle”, “textured cap”) do not reliably appear in the output. This motivates a more systematic analysis along four dimensions.

[87] h4: Level of descriptive detail.

[88] p: Descriptive richness is evaluated using a ranking model that orders captions from most to least detailed, where detail is defined as the amount of specific, factual, and descriptive information provided. Ranking is performed using Qwen2.5-7B-Instruct . For each prompt, the three captions (from Claude-3.5-Sonnet, Gemini-1.5-Pro, and GPT-4o) are randomly shuffled and anonymized before evaluation to avoid bias. As shown in the left panel of Fig. 5 , Gemini-1.5-Pro stands out, with 84.27% of its captions judged most detailed. GPT-4o is ranked last in 71.96% of cases, while Claude-3.5-Sonnet most frequently occupies the middle rank (59.16%). These results reveal a clear hierarchy of descriptive richness: Gemini > > Claude > > GPT .

[89] figure: Figure 5 : Detail-level rankings of both captions and generated images. Left: distribution of most-, moderately-, and least-detailed captions across the three models. Right: corresponding rankings assigned to the generated images.

[90] figure: Table 5 : Lexical statistics of color and texture vocabulary in model-generated captions (30k per model). Metrics include total counts, percentage of captions containing at least one term, and average frequency per caption. Light green marks the highest value in each block, and light magenta marks the lowest. Model Basic (Total) Nuanced (Total) With Basic (%) With Nuanced (%) Basic (Average) Nuanced (Average) Color Vocabulary Claude-3.5-Sonnet 88,797 23,235 92.36 43.96 2.96 0.77 Gemini-1.5-Pro 155,363 38,495 97.45 55.47 5.18 1.28 GPT-4o 62,843 10,186 81.01 22.95 2.09 0.34 Texture Vocabulary Claude-3.5-Sonnet 27,009 32,034 67.24 52.91 0.90 1.07 Gemini-1.5-Pro 35,269 49,296 73.00 64.10 1.18 1.64 GPT-4o 27,859 26,862 67.67 50.83 0.93 0.90

[91] p: Similarly, GPT-5 assigns detail-level rankings to generated images. The samples are again shuffled and anonymized to prevent bias. As shown in the right panel of Fig. 5 , however, the ordering is nearly reversed: the three models produce images with much more similar levels of detail, and images generated from GPT-4o captions are judged slightly more detailed overall. This indicates that the richness present in the captions is not faithfully retained during text-to-image generation.

[92] h4: Color vocabulary.

[93] p: The use of color terms is quantified with a deterministic dictionary-based matcher applied to normalized captions, counting both basic colors (e.g., red, green, blue) and nuanced variants (e.g., CSS/X11 shades, multi-word forms, shade modifiers). As shown in Table 5 , Gemini-1.5-Pro shows the highest frequency and coverage of color terms; Claude-3.5-Sonnet exhibits similar usage but with a slightly broader nuanced vocabulary; and GPT-4o uses color terms least often with the narrowest set. Yet these pronounced textual gaps do not yield proportionate separability in the image domain (Fig. 6 ), suggesting that nuanced color instructions are often normalized by T2I models.

[94] figure: Table 6 : Semantic composition analysis of captions. Values indicate the percentage (%) of captions meeting each criterion. Spatial Subject Guiding Balance Model Layers Focus Elements Symmetry Claude-3.5-Sonnet 93.38 96.55 86.67 3.52 Gemini-1.5-Pro 90.70 90.09 66.99 0.54 GPT-4o 86.42 88.61 70.48 1.07

[95] h4: Texture vocabulary.

[96] p: We assess captions for the use of texture descriptors, distinguishing between basic tactile terms (e.g., rough, smooth) and more nuanced expressions for materials, finishes, or fine-grained surface qualities. Judgments are obtained using Qwen2.5-7B-Instruct . As shown in Table 5 , Gemini-1.5-Pro employs texture vocabulary most extensively, particularly nuanced terms, while Claude-3.5-Sonnet and GPT-4o use fewer such descriptors. Overall, Gemini demonstrates the richest texture lexicon, Claude is moderate, and GPT is the most limited. Again, no matching ordering is observed in image attribution (Fig. 6 ), consistent with the hypothesis that fine-grained material cues are weakly realized by current T2I systems.

[97] h4: Visual composition.

[98] p: A semantic analysis of captions is performed to assess whether they encode key principles of photographic composition. Using Qwen2.5-1.5B-Instruct , we evaluate each caption against four criteria: (1) explicit description of spatial layers (foreground, middle ground, background), (2) identification of a main subject and its focus state, (3) mention of guiding elements such as leading lines or framing, and (4) reference to balance, symmetry, or subject placement.

[99] p: Across 90,000 captions from 3 models, we observe clear differences in compositional awareness (Table 6 ). Claude-3.5-Sonnet consistently attains the highest coverage across all four criteria. In contrast, Gemini-1.5-Pro and GPT-4o score slightly lower on spatial layering and subject focus, and substantially lower on guiding elements and symmetry. Crucially, heightened compositional explicitness in text does not manifest as stronger per-class separability in images (Fig. 6 ), implying that composition-related instructions are partially lost or regularized by the generator.

[100] figure: Figure 6 : Per-class classification accuracy for generated images. Each bar shows how well images generated from captions of a given model can be attributed to their caption source.

[101] h2: 6 Discussion

[102] p: In this work, we present systematic evidence of a pronounced gap between image captioning and generation models. We show that the source model of a caption can be identified with near-perfect accuracy from text alone. However, these model-specific fingerprints largely vanish once captions are translated into images by current generators. Lexical, structural, and content analyses suggest that the gap stems not from surface phrasing, but from deeper descriptive choices that are inconsistently realized in images.

[103] p: Our analysis shows that image generation models often fail to preserve fine-grained details in captions, contributing to the idiosyncratic gap between captioning and generation. As discussed in Section 5.4 , the level of detail in captions is not fully reflected in the generated images. Nuanced color descriptions, for instance, rarely affect how colors are rendered. For composition, generation models may default to common scene structures based on context rather than strictly following specific words. These results highlight concrete limitations in current generation models and point to directions for future improvement.

[104] h2: References

[105] h2: Appendix A Human Baseline: User Study

[106] p: We conduct a small-scale user study to establish a human baseline for whether captioner-specific “fingerprints” are perceptible in (i) captions and (ii) the corresponding text-to-image (T2I) outputs (Fig. 7 ). For each task, participants first review 50 training examples with ground-truth context: the original image plus either three candidate captions (caption attribution) or three FLUX.1-generated images (image attribution). They then complete two independent tests on held-out prompts: 90 caption-only attribution trials and 90 image-only attribution trials on FLUX.1 outputs; for image attribution, we additionally display the original image to reduce ambiguity from prompt underspecification. We recruit 15 participants per task (10 with math or AI research backgrounds). Humans achieve 78.37% accuracy on caption attribution but only 41.63% on image attribution, suggesting that stylistic cues are evident in captions yet substantially attenuated after T2I generation.

[107] figure: Figure 7 : User study interface for caption and image attribution. Left: caption. Right: image. Top: examples. Bottom: test.

[108] h2: Appendix B Paraphrase Prompts

[109] p: These are the three distinct prompts to generate paraphrased versions of captions, applied with both Qwen-2.5-1.5B and Qwen-2.5-7B to ensure that the robustness analysis is not tied to a single paraphrase style.

[110] h4: Prompt 1.

[111] h4: Prompt 2.

[112] h4: Prompt 3.

[113] h2: Appendix C LLM analysis on the characteristics of the generated captions

[114] p: This part contains the complete text from three different large language models tasked with analyzing the distinctive features of captions generated by Claude-3.5-Sonnet, Gemini-1.5-Pro, and GPT-4o. The text is presented as originally generated, with only minor typographical edits to remove non-standard characters (e.g., emojis) for display compatibility.

[115] h3: Analysis from “Claude-Sonnet 4”

[116] h3: Claude (claude-3-5-sonnet)

[117] h4: Distinctive Language Features:

[118] h4: Identifying Markers:

[119] h3: Gemini (gemini-1.5-pro)

[120] h4: Distinctive Language Features:

[121] h4: Identifying Markers:

[122] h3: GPT-4o (gpt-4o)

[123] h4: Distinctive Language Features:

[124] h4: Identifying Markers:

[125] h4: Key Distinguishing Patterns:

[126] h4: Most Reliable Identifiers:

[127] h3: Analysis from “GPT-5”

[128] h3: Claude-3.5-Sonnet

[129] h4: Stylistic Features:

[130] h4: Identities:

[131] h3: Gemini-1.5-Pro

[132] h4: Stylistic Features:

[133] h4: Identities:

[134] h3: GPT-4o

[135] h4: Stylistic Features:

[136] h4: Identities:

[137] h4: Quick Fingerprints (How to Spot Them Fast):

[138] h3: Analysis from “Gemini-2.5 Pro”

[139] h3: Claude 3.5 Sonnet: The Narrative Storyteller

[140] h4: Distinctive Features & Identities:

[141] h3: Gemini 1.5 Pro: The Methodical Analyst

[142] h4: Distinctive Features & Identities:

[143] h3: GPT-4o: The Efficient Summarizer

[144] h4: Distinctive Features & Identities:

[145] h2: Appendix D Use of Large Language Models

[146] p: Large language models were used in this work to assist with writing and editing tasks, such as polishing grammar, improving clarity, and suggesting alternative phrasings for sections of the manuscript. No LLM outputs were used as scientific claims, experimental findings, or conclusions. The authors take full responsibility for the accuracy and integrity of all content presented in this paper.

[147] h2: Instructions for reporting errors

[148] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[149] p: Tip: You can select the relevant text first, to include it in your report.

[150] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[151] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
