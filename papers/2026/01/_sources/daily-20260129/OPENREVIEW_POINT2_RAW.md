# or19208

How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability — Lacuna (https://lacuna.tiptreesystems.com/work/how-do-transformers-learn-to-associate-tokens-gradient-leading-terms-bring/wrk_018244ec1556800d6c53960ef87e02cf)
citeturn28135search0 [wordlim: 200] Crawled: 3 days ago; # How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability ... ICLR 2026 · OpenReview ... Extracted figure from page 2 of How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability ...   * The Role of the MLP: Through ablation studies, the authors found evidence that the MLP (Multi-Layer Perceptron) components in early training might function similarly to the "value mapping" identified in their theory, helping to refine token representations.

# How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability

Shawn Im, Changdae Oh, Zhen Fang, Sharon Li

ICLR 2026 · OpenReview

## TL;DR

Researchers have uncovered that the complex weights of a Transformer aren't just arbitrary numbers. At the start of training, they are closed-form "compositions" of three simple corpus statistics: bigrams, token interchangeability, and context mappings. By analyzing the "leading terms" of gradients, this paper provides a mathematical bridge between raw text statistics and the internal mechanics of Large Language Models (LLMs).

## What Problem Does This Paper Address?

Despite the world-altering success of Transformers, they remain "black boxes." We know they learn that "bird" is associated with "flew" and that "car" and "truck" are interchangeable in many contexts, but the mechanistic process of how these associations crystallize during training is poorly understood.
--------------------------------------------------------------------------------
ICLR 2026 · Paper Explorer (https://gisbi-kim.github.io/iclr2026-explorer/output/iclr2026_explorer.html)
citeturn28135search1 [wordlim: 200] Crawled: 4 months ago; OpenReview PDF ... How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability ... Through our analysis, we reveal that each set of weights of the transformer has closed-form expressions as simple compositions of three basis functions--bigram, token-interchangeability, and context mappings--reflecting the statistics in the text corpus and uncover how each component of the transformer captures the semantic association based on these compositions.Experiments on real-world LLMs demonstrate that our theoretical weight characterizations closely match the learned weights, and qualitative analyses further guide us on how our theorem shines light on interpreting the learned association in transformers
OpenReviewPDF

Oral interpretability and explainable AI

How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability

Shawn Im; Changdae Oh; Zhen Fang; Sharon Li

Semantic associations Interpretability LLM

USA, Australia · rating 7.20 · 4 authors

Institutions: University of Wisconsin–Madison; UTS Sydney

Keywords: Semantic associations; Interpretability; LLM

Semantic associations such as the link between "bird" and "flew" are foundational for language modeling as they enable models to go beyond memorization and instead generalize and generate coherent text. Understanding how these associations are learned and represented in language models is essential for connecting deep learning with linguistic theory and developing a mechanistic foundation for large language models. In this work, we analyze how these associations emerge from natural language data in attention-based language models through the lens of training dynamics. --------------------------------------------------------------------------------
ICLR2026 (https://hongsong-wang.github.io/ICLR2026_Abstract/)
citeturn28135search2 [wordlim: 200] Crawled: 4 months ago; PaperID: 216,   Oral  OpenReview  https://arxiv.org/pdf/2601.19208 ... Title: How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability ... Through our analysis, we reveal that each set of weights of the transformer has closed-form expressions as simple compositions of three basis functions--bigram, token-interchangeability, and context mappings--reflecting the statistics in the text corpus and uncover how each component of the transformer captures the semantic association based on these compositions.Experiments on real-world LLMs demonstrate that our theoretical weight characterizations closely match the learned weights, and qualitative analyses further guide us on how our theorem shines light on interpreting the learned association in transformers.
As a consequence, we provide a theoretical validation of recent empirical observations connecting the emergence of power-law tails in the weight spectrum with network generalization performance, yielding an interpretation from first principles.

* * *

PaperID: 216,   Oral  OpenReview  https://arxiv.org/pdf/2601.19208    

Authors: Shawn Im, Changdae Oh, Zhen Fang, Sharon Li

Title: How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability

Keywords: Semantic associations, Interpretability, LLM

Abstract:
Semantic associations such as the link between "bird" and "flew" are foundational for language modeling as they enable models to go beyond memorization and instead generalize and generate coherent text. Understanding how these associations are learned and represented in language models is essential for connecting deep learning with linguistic theory and developing a mechanistic foundation for large language models. In this work, we analyze how these associations emerge from natural language data in attention-based language models through the lens of training dynamics. By leveraging a leading-term approximation of the gradients, we develop closed-form expressions for the weights at early stages of training that explain how semantic associations first take shape. Through our analysis, we reveal that each set of weights of the transformer has closed-form expressions as simple compositions of three basis functions--bigram, token-interchangeability, and context mappings--reflecting the statistics in the text corpus and uncover how each component of the transformer captures the semantic association based on these compositions. Experiments on real-world LLMs demonstrate that our theoretical weight characterizations closely match the learned weights, and qualitative analyses further guide us on how our theorem shines light on interpreting the learned association in transformers.

--------------------------------------------------------------------------------
Tracing LLM Behavior to the Training Data with Empirical Next-Token Distributions (https://www.researchgate.net/publication/410301726_Tracing_LLM_Behavior_to_the_Training_Data_with_Empirical_Next-Token_Distributions)
citeturn28135search3 [wordlim: 200] Published: 3 months ago; Crawled: last month; How do transformers learn to associate tokens: Gradient leading terms bring mechanistic interpretability ... How do transformers learn to associate tokens: Gradient leading terms bring mechanistic interpretability.
Roger Grosse, Juhan Bae, Cem Anil, Nelson Elhage, Alex Tamkin, Amirhossein Tajdini, Benoit Steiner, Dustin Li, Esin Durmus, Ethan Perez, et al. Studying large language model generalization with influence functions. arXiv preprint arXiv:2308.03296, 2023.

Why larger models learn more: Effects of capacity, interference, and rare-task retention

  * Jan 2026

  * Jing Huang
  * Daniel Wurgaft
  * Rachit Bansal
  * Laura Ruis
  * Naomi Saphra
  * David Alvarez-Melis
  * Andrew Kyle Lampinen
  * Christopher Potts
  * Ekdeep Singh Lubana

Jing Huang, Daniel Wurgaft, Rachit Bansal, Laura Ruis, Naomi Saphra, David Alvarez-Melis, Andrew Kyle Lampinen, Christopher Potts, and Ekdeep Singh Lubana. Why larger models learn more: Effects of capacity, interference, and rare-task retention. arXiv preprint arXiv:2605.29548, 2026.

How do transformers learn to associate tokens: Gradient leading terms bring mechanistic interpretability

  * Jan 2026

  * Shawn Im
  * Changdae Oh
  * Zhen Fang
  * Sharon Li

Shawn Im, Changdae Oh, Zhen Fang, and Sharon Li. How do transformers learn to associate tokens: Gradient leading terms bring mechanistic interpretability. In The Fourteenth International Conference on Learning Representations, 2026. URL https://openreview.net/forum?id=A4Us8jxVGq.

Quantitative bounds for length generalization in transformers

  * Jan 2026

  * Zachary Izzo
  * Eshaan Nichani
  * Jason D Lee

Zachary Izzo, Eshaan Nichani, and Jason D. Lee. Quantitative bounds for length generalization in transformers. In The Fourteenth International Conference on Learning Representations, 2026. URL https://openreview. net/forum?id=TLSUIyBIfs.--------------------------------------------------------------------------------
Zhen Fang (UTS-AAII) (https://fang-zhen.github.io/publication.html)
citeturn28135search4 [wordlim: 200] Crawled: 4 months ago; [ Openreview ] [ CODE] ... How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability.
# Zhen Fang (Lecturer at UTS-AAII)

# Publications

Currently, I research the reliable machine learning and responsible AI. Previously (2014-2017), I researched the geometry analysis (solving fully noliner PDE). In the following, ^{†} represents equal contribution, and ^{✉} represents corresponding author. [Selected Conference Papers, Selected Journal Articles, Thesis ]

Published Conference Papers (Selected)

  1. X. Li, Z. Fang^{✉}, Y. Luo, Y. Deng, S. Du, S. Ye, L. Chen^{✉}.
Training a Multi-Domain Hallucination Detector across QA and Reasoning via Adaptive Layer Aggregation.
In 32nd SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2026), Accepted, 2026 (CORE A*).
[ Openreview ] [ CODE]
  2. J. Liao, Q. Wang, S. Ye, X. Yu, L. Chen, Z. Fang^{✉}.
Explainable LLM Unlearning through Reasoning.
In The Fourteenth International Conference on Learning Representations (ICLR 2026), Accepted, 2026 (CORE A*).
[ Openreview ] [ CODE]
  3. Y. Deng, Z. Fang^{✉}, Y. Li, L. Chen.
Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection.
In The Fourteenth International Conference on Learning Representations (ICLR 2026), Accepted, 2026 (CORE A*).
[ Openreview ] [ CODE]
  4. S. Im, C. Oh, Z. Fang, Y. Li.
How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability.
In The Fourteenth International Conference on Learning Representations (ICLR 2026), Accepted, 2026 (CORE A*).
[ Openreview ] [ CODE ] [ Oral ]
--------------------------------------------------------------------------------
ICLR 2026 Accepted Papers (https://kmno4-zx.github.io/iclr26-all-papers/)
citeturn28135search5 [wordlim: 200] Crawled: 8 months ago; 📄 OpenReview 📄 PDF 🤖 LLM-Analysis ... How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability 💬 14 ⭐ 7.20 ... Through our analysis, we reveal that each set of weights of the transformer has closed-form expressions as simple compositions of three basis functions--bigram, token-interchangeability, and context mappings--reflecting the statistics in the text corpus and uncover how each component of the transformer captures the semantic association based on these compositions.Experiments on real-world LLMs demonstrate that our theoretical weight characterizations closely match the learned weights, and qualitative analyses further guide us on how our theorem shines light on interpreting the learned association in transformers.
Experiments on image and text classification tasks, with various architectures, show consistent gains over Deep Ensembles. Remarkably, in zero-shot classification on ImageNet-1k, our approach surpasses state of the art methods, even without requiring additional training.

📄 OpenReview 📄 PDF 🤖 LLM-Analysis

101. How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability 💬 14 ⭐ 7.20

📁 interpretability and explainable AI

🏷️ Semantic associations Interpretability LLM

Semantic associations such as the link between "bird" and "flew" are foundational for language modeling as they enable models to go beyond memorization and instead generalize and generate coherent text. Understanding how these associations are learned and represented in language models is essential for connecting deep learning with linguistic theory and developing a mechanistic foundation for large language models. --------------------------------------------------------------------------------
SpotlightTodAI — Oral & Spotlight Papers from ICML, ICLR, NeurIPS (https://dion-jy.github.io/spotlight-todai/)
citeturn28135search6 [wordlim: 200] Crawled: 2 days ago; 157  | How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability ↗  | Shawn Im et al.
--------------------------------------------------------------------------------
How Transformers Learn to Associate Tokens: Insights from ICLR 2026 - Studocu (https://www.studocu.vn/vn/document/university-of-information-technology/infomation-technology/how-transformers-learn-to-associate-tokens-insights-from-iclr-2026/155237665)
citeturn28135search7 [wordlim: 200] Crawled: last week; # How Transformers Learn to Associate Tokens: Insights from ICLR 2026 ... Then, Section 4 uncovers how three basis functions, which are crucial to express token associations and language structure, are encapsulated in those gradient leading terms, and how these three functions are compounded to shape the desiderata of the transformers’ weight matrices. ... We also consider the cosine similarity between the learned weights and their leading terms when using a larger learning rate of 0. 05 to understand how features evolve at later stages with respect to the leading term gradients. ... The extensive analyses on the weight matrices’ characterizations grounded by empirical supports from toy transformers and real-world LLMs contribute to the theoretical foundations of representation learning in transformers while also opening pathways for interpretability research: discovering common factors that allow weight matrices across components to be decomposed into simple functions of those shared factors; leveraging theory to formulate broad hypotheses about how concepts arise in models, extending beyond individual mechanisms or specific behaviors to complex characteristics. ... How do transformers learn topic structure: Towards a mechanistic understanding. ... URL openreview/forum?
--------------------------------------------------------------------------------
iclr2026-oral-papers/paper-list.md at main · XinyuLiuCs/iclr2026-oral-papers · GitHub (https://github.com/XinyuLiuCs/iclr2026-oral-papers/blob/main/paper-list.md)
citeturn28135search8 [wordlim: 200] Crawled: 5 days ago; 156  | How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability  | link ... 164  | Token-Importance Guided Direct Preference Optimization  | link
--------------------------------------------------------------------------------
AI-Paper-Trends/docs/topic-atlas/2026/ICLR/topic-014.md at main · zhihengli-casia/AI-Paper-Trends · GitHub (https://github.com/zhihengli-casia/AI-Paper-Trends/blob/main/docs/topic-atlas/2026/ICLR/topic-014.md)
citeturn28135search9 [wordlim: 200] Crawled: last month; Turner, David Krueger; assignment: `hdbscan`; source: `OpenReview` ... Hessian-Enhanced Token Attribution (HETA): Interpreting Autoregressive LLMs ... How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability
--------------------------------------------------------------------------------
Yixuan Li — Lacuna (https://lacuna.tiptreesystems.com/author/sharon-li/aut_5ff04ad48a8946b1a09f077b144033e7)
citeturn28135search10 [wordlim: 200] Crawled: last week; How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability  | ICLR  | 2026
--------------------------------------------------------------------------------
Analysisに関する論文・技術記事メモの一覧 | わたしのべんきょうノート (https://akihikowatanabe.github.io/paper_notes/articles/Analysis-1.html)
citeturn28135search11 [wordlim: 200] Published: 2 days ago; Crawled: yesterday; ### [Paper Note] How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability, Shawn Im+, arXiv'26, 2026.01 ... #Pretraining #NLP #LanguageModel #Explanation #RepresentationLearning #Transformer #Attention #One-Line Notes Issue Date: 2026-02-09 GPT Summary- セマンティック関連性を理解することは、言語モデルの一般化能力を高め、一貫性のあるテキスト生成に寄与します。



# or19208recover

["Internal Error ()\nciteturn28137view0 [wordlim: 200] Source: open({\"ref_id\":\"https://openreview.net/forum?id=A4Us8jxVGq\",\"lineno\":null}); Total lines: 1\nL0: Failed to fetch https://openreview.net/forum?id=A4Us8jxVGq: (429) Too Many Requests\n--------------------------------------------------------------------------------\nZhen Fang (UTS-AAII) (https://fang-zhen.github.io/publication.html)\nciteturn28137view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://fang-zhen.github.io/publication.html\",\"lineno\":null}); Total lines: 139\nL0: # Zhen Fang (Lecturer at UTS-AAII)\nL1: \nL2: * * *\nL3: \nL4: cite0†Home cite1†Publications cite2†Miscellaneous cite3†Group |\nL5: \nL6: # Publications\nL7: \nL8: Currently, I research the reliable machine learning and responsible AI. Previously (2014-2017), I researched the geometry analysis (solving fully noliner PDE). In the following, ^{†} represents equal contribution, and ^{✉} represents corresponding author. [cite4†Selected Conference Papers , cite5†Selected Journal Articles , cite6†Thesis ]\nL9: ##\nL10: \nL11: * * *\nL12: \nL13: Published Conference Papers (Selected)\nL14:   1. X. Li, Z. Fang^{✉}, Y. Luo, Y. Deng, S. Du, S. Ye, L. Chen^{✉}.\nL15: Training a Multi-Domain Hallucination Detector across QA and Reasoning via Adaptive Layer Aggregation.\nL16: In cite7†32nd SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2026)†kdd2026.kdd.org , Accepted, 2026 (CORE A*).\nL17: [ cite8†Openreview†openreview.net ] [ cite9†CODE†github.com ]\nL18:   2. J. Liao, Q. Wang, S. Ye, X. Yu, L. Chen, Z. Fang^{✉}.\nL19: Explainable LLM Unlearning through Reasoning.\nL20: In cite10†The Fourteenth International Conference on Learning Representations (ICLR 2026)†iclr.cc , Accepted, 2026 (CORE A*).\nL21: [ cite11†Openreview†openreview.net ] [ cite9†CODE†github.com ]\nL22:   3. Y. Deng, Z. Fang^{✉}, Y. Li, L. Chen.\nL23: Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection.\nL24: In cite10†The Fourteenth International Conference on Learning Representations (ICLR 2026)†iclr.cc , Accepted, 2026 (CORE A*).\nL25: [ cite12†Openreview†openreview.net ] [ cite13†CODE†github.com ]\nL26:   4. S. Im, C. Oh, Z. Fang, Y. Li.\nL27: How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability.\nL28: In cite10†The Fourteenth International Conference on Learning Representations (ICLR 2026)†iclr.cc , Accepted, 2026 (CORE A*).\nL29: [ cite14†Openreview†openreview.net ] [ cite15†CODE†github.com ] [ Oral ]\nL30:   5. B. Peng, Y. Hu, B. Liu, L. Chen, J. Lu, Z. Fang^{✉}.\nL31: Delving into Spectral Clustering with Vision-Language Representations.\nL32: In cite10†The Fourteenth International Conference on Learning Representations (ICLR 2026)†iclr.cc , Accepted, 2026 (CORE A*).\nL33: [ cite16†Openreview†openreview.net ] [ cite17†CODE†github.com ]\nL34:   6. B. Peng, J. Lu, G. Zhang, Z. Fang^{✉}.\nL35: Debiased Negative Mining Improves Out-of-distribution Detection with Pre-trained Vision-Language Models.\nL36: In cite7†32nd SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2026)†kdd2026.kdd.org , Accepted, 2025 (CORE A*).\nL37: [ cite18†Openreview†openreview.net ] [ cite18†CODE†openreview.net ]\nL38:   7. B. Peng, J. Lu, G. Zhang, Z. Fang^{✉}.\nL39: An Information-theoretical Framework for Understanding Out-of-distribution Detection with Pretrained Vision-Language Models.\nL40: In cite19†Annual Conference on Neural Information Processing Systems (NeurIPS 2025)†neurips.cc , Accepted, 2025 (CORE A*).\nL41: [ cite20†Openreview†neurips.cc ] [ cite20†CODE†neurips.cc ]\nL42:   8. E. Yu, J. Lu, X. Yang, G. Zhang, Z. Fang^{✉}.\nL43: Learning Robust Spectral Dynamics for Temporal Domain Generalization.\nL44: In cite19†Annual Conference on Neural Information Processing Systems (NeurIPS 2025)†neurips.cc , Accepted, 2025 (CORE A*).\nL45: [ cite21†arXiv†arxiv.org ] [ cite20†CODE†neurips.cc ]\nL46:   9. K. Shi, J. Lu, S. Ye, G. Zhang, Z. Fang^{✉}.\nL47: MiraGe: Multimodal Discriminative Representation Learning for Generalizable AI-Generated Image Detection.\nL48: In cite22†ACM International Conference on Multimedia (ACM MM 2025)†acmmm2025.org , Accepted, 2025 (CORE A*).\nL49: [ cite23†Openreview†openreview.net ] [ cite23†CODE†openreview.net ]\nL50:   10. B. Peng, J. Lu, G. Zhang, Z. Fang^{✉}.\nL51: On the Provable Importance of Gradients for Language-Assisted Image Clustering.\nL52: In cite24†International Conference on Computer Vision (ICCV 2025)†iccv.thecvf.com , Accepted, 2025 (CORE A*).\nL53: [ cite25†Openreview†arxiv.org ] [ cite26†CODE†openreview.net ] [ Highlight ]\nL54:   11. C. Oh, Z. Fang, S. Im, X. Du, Y. Li.\nL55: Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach.\nL56: In cite27†International Conference on Machine Learning (ICML 2025)†icml.cc , Published Online, 2025 (CORE A*).\nL57: [ cite26†Openreview†openreview.net ] [ cite28†CODE†github.com ]\nL58:   12. B. Peng, J. Lu, Y. Zhang, G. Zhang, Z. Fang^{✉}.\nL59: Distributional Prototype Learning for Out-of-distribution Detection.\nL60: In cite29†31st SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2025)†kdd2025.kdd.org , Published Online, 2024 (CORE A*).\nL61: [ cite30†Openreview†dl.acm.org ] [ cite30†CODE†dl.acm.org ]\nL62:   13. B. Peng, Z. Fang^{✉}, G. Zhang, J. Lu.\nL63: Knowledge Distillation with Auxiliary Variable.\nL64: In cite27†International Conference on Machine Learning (ICML 2024)†icml.cc , Published Online, 2024 (CORE A*).\nL65: [ cite31†Openreview†openreview.net ] [ cite31†CODE†openreview.net ]\nL66:   14. B. Peng, Y. Luo, Y. Zhang, Y. Li, Z. Fang^{✉}.\nL67: ConjNorm: Tractable Density Estimation for Out-of-Distribution Detection.\nL68: In cite10†International Conference on Learning Representations (ICLR 2024)†iclr.cc , Published Online, 2024 (CORE A*).\nL69: [ cite32†Openreview†openreview.net ] [ cite32†CODE†openreview.net ]\nL70:   15. X. Du^{†}, Z. Fang^{†}, Ilias Diakonikolas, Y. Li.\nL71: How Does Wild Data Provably Help OOD Detection?\nL72: In cite10†International Conference on Learning Representations (ICLR 2024)†iclr.cc , Published Online, 2024 (CORE A*).\nL73: [ cite33†Openreview†openreview.net ] [ cite34†CODE†github.com ]\nL74:   16. Q. Wang^{†}, Z. Fang^{†}, Y. Zhang, F. Liu, Y. Li, B. Han.\nL75: Learning to Augment Distributions for Out-of-distribution Detection.\nL76: In cite35†Advances in Neural Information Processing Systems (NeurIPS 2023)†neurips.cc , Published Online, 2023 (CORE A*).\nL77: [ cite36†arXiv†openreview.net ] [ cite37†CODE†github.com ]\nL78:   17. M. Yang, Z. Fang, Y. Zhang, Y. Du, F. Liu, J. Ton, J. Wang, J. Wang.\nL79: Invariant Learning via Probability of Sufficient an Necessary Causes.\nL80: In cite35†Advances in Neural Information Processing Systems (NeurIPS 2023)†neurips.cc , Published Online, 2023 (CORE A*).\nL81: [ cite38†Github†openreview.net ] [ cite39†CODE†github.com ][ Spotlight ]\nL82:   18. X. Wu, J. Lu^{✉}, Z. Fang^{✉}, G. Zhang.\nL83: Meta OOD Learning For Continuously Adaptive OOD Detection.\nL84: In cite40†International Conference on Computer Vision (ICCV 2023)†iccv2023.thecvf.com , Published Online, 2023 (CORE A*).\nL85: [ cite41†arXiv†openaccess.thecvf.com ] [ cite41†CODE†openaccess.thecvf.com ]\nL86:   19. Z. Fang, Y. Li, J. Lu, J. Dong, B. Han, F. Liu.\nL87: Is Out-of-distribution Detection Learnable?\nL88: In cite42†Advances in Neural Information Processing Systems (NeurIPS 2022)†neurips.cc , Published Online, 2022 (CORE A*).\nL89: [ cite43†arXiv†arxiv.org ] [ cite44†Pure Theory†openreview.net ] [ Outstanding Paper Award ] (outstanding papers:acceptance:submissions=13:2672:10411)\nL90:   20. Z. Fang^{†}, J. Lu, A. Liu^{†}, F. Liu, G. Zhang.\nL91: Learning Bounds for Open-Set Learning.\nL92: In cite45†International Conference on Machine Learning (ICML 2021)†icml.cc , Published Online, 2021 (CORE A*).\nL93: [ cite46†arXiv†arxiv.org ] [ cite47†CODE†github.com ]\nL94:   21. J. Dong^{†}, Z. Fang^{†}, A. Liu, G. Sun, T. Liu.\nL95: Confident-Anchor-Induced Multi-Source-Free Domain Adaptation.\nL96: In cite48†Advances in Neural Information Processing Systems (NeurIPS 2021)†neurips.cc , Published Online, 2021 (CORE A*).\nL97: [ cite49†Link†openreview.net ] [ cite50†CODE†github.com ]\nL98:   22. L. Zhong^{†}, Z. Fang^{†}, F. Liu^{†}, B. Yuan, G. Zhan, J. Lu.\nL99: How does the Combined Risk Affect the Performance of Unsupervised Domain Adaptation Approaches?\nL100: In cite51†AAAI Conference on Artificial Intelligence (AAAI 2021)†aaai.org , Published Online, 2021 (CORE A*).\nL101: [ cite52†arXiv†arxiv.org ] [ cite53†CODE†github.com ]\nL102:   23. Y. Zhang^{†}, F. Liu^{†}, Z. Fang^{†}, B. Yuan, G. Zhang, J. Lu.\nL103: Clarinet: A One-step Approach Towards Budget-friendly Unsupervised Domain Adaptation.\nL104: In cite54†International Joint Conference on Artificial Intelligence (IJCAI 2020)†ijcai20.org , Published Online (CORE A*).\nL105: [ cite55†arXiv†arxiv.org ] [ cite56†CODE†github.com ]\nL106: ##\nL107: \nL108: * * *\nL109: \nL110: Published Journal Articles (Selected)\nL111:   1. J. Nie, Y. Luo, S. Ye, Y. Zhang, X. Tian, Z. Fang.\nL112: Out-of-Distribution Detection with Virtual Outlier Smoothing.\nL113: cite57†International Journal of Computer Vision†link.springer.com , Published Online, 2024 (ERA&CORE A*).\nL114: [ cite58†Link†link.springer.com ] [ cite59†CODE†github.com ]\nL115:   2. Z. Fang, Y. Li, F. Liu, B. Han, J. Lu.\nL116: On the Learnability of Out-of-distribution Detection.\nL117: cite60†Journal of Machine Learning Research†www.jmlr.org , Published Online, 2024 (ERA&CORE A*).\nL118: [ cite60†Link†www.jmlr.org ] [ cite60†Pure Theory†www.jmlr.org ]\nL119:   3. Z. Fang, J. Lu, F. Liu, G. Zhang.\nL120: Semi-supervised Heterogeneous Domain Adaptation: Theory and Algorithms.\nL121: cite61†IEEE Transactions on Pattern Analysis and Machine Intelligence†ieeexplore.ieee.org , Published Online, 2022 (ERA&CORE A*).\nL122: [ cite62†Link†ieeexplore.ieee.org ] [ cite63†CODE†github.com ]\nL123:   4. Z. Fang, J. Lu, F. Liu, J. Xuan, G. Zhang.\nL124: Open Set Domain Adaptation: Theoretical Bound and Algorithm.\nL125: cite64†IEEE Transactions on Neural Networks and Learning Systems†ieeexplore.ieee.org , Published Online, 2020 (ERA&CORE A*).\nL126: [ cite65†Link†ieeexplore.ieee.org ] [ cite66†CODE†github.com ]\nL127: ##\nL128: \nL129: * * *\nL130: \nL131: Thesis\nL132: \nL133:   1. Zhen Fang.\nL134: Bridging Theory and Algorithms for Open-Set and Heterogeneous Domain Adaptations.\nL135: Doctoral Thesis, Australian Artificial Intelligence Institute, University of Technology Sydney, Australia, submitted in June 2021.\nL136:   2. Zhen Fang.\nL137: The C2 Estimates of Prescribed Curvature Equations.\nL138: Master Thesis, Xiamen University, China, July 2017.\n",{"chunk_id":"2f851c","wall_time_seconds":0.244047708,"exit_code":0,"original_token_count":68,"output":"{\"name\":\"ChallengeRequiredError\",\"message\":\"Challenge verification required (2026-10-04-2683881)\",\"status\":403,\"details\":{\"challengeUrl\":\"https://openreview.net/challenge?redirect=https%3A%2F%2Fapi2.openreview.net%2Fnotes%3Fid%3DA4Us8jxVGq\",\"reqId\":\"2026-10-04-2683881\"}}"}]


# or19245id

Verifying your browser | OpenReview (https://openreview.net/pdf/705ba68c40dcd761066314abc7fb3901eca56f5c.pdf)
citeturn28138view0 [wordlim: 200] Crawled: 3 weeks ago; Content type: text/html; Source: click({"ref_id":"turn28137view1","id":12}); Redirected to URL: https://openreview.net/challenge?redirect=/pdf/705ba68c40dcd761066314abc7fb3901eca56f5c.pdf; Total lines: 9
L0: # Verifying your browser
L1: 
L2: ## Complete the check below to continue to OpenReview
L3: 
L4: Please complete the verification above.
L5: 
L6: Have an OpenReview account? cite0†Sign in to skip this check.
L7: 
L8: cite1†OpenReview — Open Peer Review. Open Publishing. Open Access.



# or19245exact

GitHub - TianYaDY/SpikeScore · GitHub (https://github.com/TianYaDY/SpikeScore)
citeturn28139search0 [wordlim: 200] Crawled: last month; > This README explains how to replicate the experiments from our paper Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection. ...     url={https://openreview.net/forum?
# SpikeScore-GHD

### SpikeScore: Generalizable Hallucination Detection — Reproduction Guide

> Abstract.
> Hallucination detection is critical for deploying large language models (LLMs) in real-world applications. Existing hallucination detection methods achieve strong performance when the training and test data come from the same domain, but they suffer from poor cross-domain generalization. We study an important yet overlooked problem, generalizable hallucination detection (GHD): train on a single domain, then generalize to diverse related domains. We simulate multi-turn dialogues following the model’s initial answer and observe that hallucination-initiated dialogues exhibit larger uncertainty fluctuations than factual ones. We propose SpikeScore, which quantifies abrupt local fluctuations in multi-turn score trajectories. Through theory and experiments, SpikeScore shows strong cross-domain separability between hallucinated and non-hallucinated responses and outperforms representative baselines and generalization-oriented methods.

* * *

# SpikeScore-GHD

# SpikeScore: Generalizable Hallucination Detection — Reproduction Guide

> This README explains how to replicate the experiments from our paper Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection. The pipeline simulates multi-turn dialogues after an initial model response, records hidden states, computes uncertainty scores (e.g., SEP, SAPLMA), and aggregates them into SpikeScore for hallucination detection.

* * *

## Table of Contents

  * Overview
  * Hardware & Model Requirements
  * Setup & Installation
  * Credential Configuration
  * Step 1 — Run Multi-Turn Dialogue Generation
  * Step 2 — Compute SEP/RS Metrics
  * Step 3 — Evaluate AUC
  * Optional — Train a Probe
  * Configuration Reference
  * Outputs & File Structure
  * Tips & Troubleshooting

* * *

## Overview

To reproduce the experiments:

  1. Forward-pass prompts/answers through an LLM to collect:

     * Generated Multi-Turn Dialogue responses
     * All-layer hidden states
  2. Compute Multi-Turn Dialogue collapse metrics (SEP or RS) from hidden states.

  3. Aggregate results and report AUC and distribution plots.

> Recommendation Use FP16 non-quantized checkpoints. For hidden-state extraction, quantized models often require extra (de)quantization, which can reduce precision and be slower than FP16.

* * *

## Citation

If you find this repository or our work useful, please consider citing our paper:
    
    @inproceedings{
    deng2026beyond,
    title={Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection},
    author={Yongxin Deng and Zhen Fang and Sharon Li and Ling Chen},
    booktitle={The Fourteenth International Conference on Learning Representations},
    year={2026},
    url={https://openreview.net/forum?id=Y16qXOaylp}
    }
    


Readme

Apache-2.0 license

Activity

### Stars

3 stars

### Watchers

0 watching

### Forks

0 forks
--------------------------------------------------------------------------------
[论文解读] Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection (https://m0rtzz.github.io/paper-notes/ICLR2026/hallucination/beyond_in-domain_detection_spikescore_for_cross-domain_hallucination_detection/)
citeturn28139search1 [wordlim: 200] Crawled: 3 weeks ago; # Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection¶ ... OpenReview: https://openreview.net/forum?

[ICLR2026][幻觉检测][跨域泛化] 作者发现「由幻觉答案引出的多轮自对话，其不确定性分数会出现远比真实答案剧烈的尖峰抖动」，于是把这种抖动量化成 **SpikeScore**（分数序列的最大二阶差分），用一个阈值就能做到只在单个领域训练、却能跨多个领域稳定检测幻觉，在四个 LLM、六个 benchmark 上的跨域 AUROC 全面超过 PRISM、ICR Probe 等专门的跨域方法。

标签：ICLR2026 · 幻觉检测 · 跨域泛化 · 多轮自对话 · 二阶差分 · 不确定性

# Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection¶

会议: ICLR2026
OpenReview: https://openreview.net/forum?id=Y16qXOaylp
代码: 待确认
领域: 幻觉检测 / LLM 可靠性
关键词: 幻觉检测, 跨域泛化, 多轮自对话, 二阶差分, 不确定性

## 一句话总结¶

作者发现「由幻觉答案引出的多轮自对话，其不确定性分数会出现远比真实答案剧烈的尖峰抖动」，于是把这种抖动量化成 SpikeScore（分数序列的最大二阶差分），用一个阈值就能做到只在单个领域训练、却能跨多个领域稳定检测幻觉，在四个 LLM、六个 benchmark 上的跨域 AUROC 全面超过 PRISM、ICR Probe 等专门的跨域方法。
### 损失函数 / 训练策略¶

SpikeScore 本身不引入新训练目标——唯一需要训练的是 backbone 打分器。以默认的 SAPLMA 为例，它在 LLM 内部表示 \(E_\theta(\cdot)\) 上接一个 MLP + sigmoid 得到概率输出 \(p_W(\cdot)\in[0,1]\)，用交叉熵在标注数据 \(D_l=\{(Q_i,A_i,y_i)\}\) 上优化： $\(\hat W \in \arg\min_W -\frac1n\sum_{i=1}^n \Big[y_i\log p_W(E_\theta(A_i\mid Q_i)) + (1-y_i)\log\big(1-p_W(E_\theta(A_i\mid Q_i))\big)\Big].\)$ 训练只在单个训练域上进行；跨域能力完全来自 SpikeScore 这一后处理几何特征，而非额外的域适配训练。轨迹长度默认 \(K=20\) 轮——实验显示性能在 15–20 轮附近饱和，故取前 20 轮为最具信息量的「早期阶段」。

--------------------------------------------------------------------------------
arXivDaily每日学术速递，同步arXiv全量数据，AI总结、翻译，覆盖人工智能、机器人、计算机、金融、统计学、数学、物理学、生物学、经济学、电气&系统等方向。 (https://www.arxivdaily.com/?date=2026-02-20&major=HOT&search_in=title&subcat=cs.AI)
citeturn28139search2 [wordlim: 200] Published: 7 months ago; Crawled: 3 months ago; Code is available at https://github.com/mts-ai/replaceme Reviews at OpenReview: https://openreview.net/forum? ... ## Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection ... Experiments across multiple LLMs and benchmarks demonstrate that the SpikeScore-based detection method outperforms representative baselines in cross-domain generalization and surpasses advanced generalization-oriented methods, verifying the effectiveness of our method in cross-domain hallucination detection. ... Our results highlight the current limitations of autonomous action in agentic systems, and expose promising future research directions.
To further empower the model, we introduce a suite of self-supervised pre-training tasks -- specifically masked token modeling and next-time prediction -- to explicitly encode the fundamental laws of network evolution. Extensive experiments show that TGPM consistently achieves state-of-the-art performance in both transductive and inductive link prediction, demonstrating exceptional cross-domain transferability. Our code has been released in https://github.com/antman9914/TGPM.

URL PDF HTML ☆ [Button: 复制]

赞 0 踩 0

2601.19245 2026-02-20 cs.AI cs.LG 版本更新

## Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection

Yongxin Deng, Zhen Fang, Sharon Li, Ling Chen

详情

英文摘要

Hallucination detection is critical for deploying large language models (LLMs) in real-world applications. Existing hallucination detection methods achieve strong performance when the training and test data come from the same domain, but they suffer from poor cross-domain generalization. --------------------------------------------------------------------------------
arXivDaily每日学术速递，同步arXiv全量数据，AI总结、翻译，覆盖人工智能、机器人、计算机、金融、统计学、数学、物理学、生物学、经济学、电气&系统等方向。 (https://www.arxivdaily.com/?date=2026-02-20&major=HOT&search_in=all&subcat=cs.LG&submission=replacement)
citeturn28139search3 [wordlim: 200] Published: 7 months ago; Crawled: 3 months ago; Comments 10 pages, 43 pages with appendix, ICLR 2026, Conference URL: https://openreview.net/forum? ... ## Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection ... Experiments across multiple LLMs and benchmarks demonstrate that the SpikeScore-based detection method outperforms representative baselines in cross-domain generalization and surpasses advanced generalization-oriented methods, verifying the effectiveness of our method in cross-domain hallucination detection.
By combining these results, we design an active learning algorithm for decision trees that uses only a polylogarithmic number of label queries in the dataset size, under the stated assumptions. Finally, we establish a label complexity lower bound, showing our algorithm's dependence on the error tolerance $ε$ is close to optimal.

URL PDF HTML ☆ [Button: 复制]

赞 0 踩 0

2601.19245 2026-02-20 cs.AI cs.LG 版本更新

## Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection

Yongxin Deng, Zhen Fang, Sharon Li, Ling Chen

详情

英文摘要

Hallucination detection is critical for deploying large language models (LLMs) in real-world applications. Existing hallucination detection methods achieve strong performance when the training and test data come from the same domain, but they suffer from poor cross-domain generalization. In this paper, we study an important yet overlooked problem, termed generalizable hallucination detection (GHD), which aims to train hallucination detectors on data from a single domain while ensuring robust performance across diverse related domains. --------------------------------------------------------------------------------
[论文解读] Beyond In-Domain Detection: SpikeScore for Cross-Domain Hallucination Detection (https://zhaoyang97.github.io/Paper-Notes/ICLR2026/hallucination/beyond_in-domain_detection_spikescore_for_cross-domain_hallucination_detection/)
citeturn28139search4 [wordlim: 200] Crawled: 3 weeks ago; 他们先在实验里确立两个观察：期望不变性——幻觉域的 SpikeScore 均值是非幻觉域的两倍以上（\(2\,\mathbb{E}_{\text{真实}} < \mathbb{E}_{\text{幻觉}}\)）；标准差差异——幻觉域标准差更大，与非幻觉域的标准差之比落在 \(1\) 到 \(2.5\) 之间。 ... 更重要的是，SpikeScore 是一个与打分器解耦的框架：作者把它分别接到训练相关的 SAPLMA、SEP 和训练无关的 Perplexity、Reasoning score、In-Context Sharpness 上，全部都能有效检测，说明「幻觉轨迹有尖峰」是一种通用、可迁移的特征，而不是 SAPLMA 特有的产物（其中接训练相关打分器效果更好）。
于是 Theorem 1 给出关键的桥梁：只要非幻觉域的变异系数（标准差除以期望）\(\mathrm{CV}\le 0.1\cdot t\) 受控，就有 $\(P\big(\mathrm{Max}|\Delta^2|(S(Q',H')) > \mathrm{Max}|\Delta^2|(S(Q,A))\big) \ge \frac{1}{1+0.0725\cdot t^2},\)$ 即「幻觉样本的 SpikeScore 高于真实样本」这件事有可证的概率下界。实验进一步测得各域变异系数都不超过 \(0.2\)（对应 \(t=2\)），代入即得分离概率 \(\ge 0.775\)。由于评测采用「留一域、其余域均匀混合」的池化协议，从概率角度等价于对各测试域的可分性取期望，因此这个下界天然刻画的是跨域而非单域的可分性——这正是把挑战 1 的单域可分提升到挑战 2 的跨域可分的理论支点。（注：部分推导细节以原文 Appendix A 为准。）

4. 阈值检测、backbone 无关与 RAG 扩展：一个即插即用的检测框架

最终的检测器极简：算出 SpikeScore 后与阈值 \(\lambda\) 比较， $\(D_\lambda(Q,A) = \begin{cases}0, & \mathrm{Max}|\Delta^2|(S(Q,A)) < \lambda \ (\text{真实})\\ 1, & \text{否则}\ (\text{幻觉})\end{cases}\)$ 没有任何需要重新训练的跨域模块。更重要的是，SpikeScore 是一个与打分器解耦的框架：作者把它分别接到训练相关的 SAPLMA、SEP 和训练无关的 Perplexity、Reasoning score、In-Context Sharpness 上，全部都能有效检测，说明「幻觉轨迹有尖峰」是一种通用、可迁移的特征，而不是 SAPLMA 特有的产物（其中接训练相关打分器效果更好）。又因为整条流水线是后处理的，只需要一段自然语言答案，所以无论上游是否做了检索、工具调用，它都能照常诱导自对话、抽取逐轮分数、算 SpikeScore，从而无缝扩展到 RAG 场景。

## 实验关键数据¶

### 主实验¶

四个 LLM（Llama-3.2-3B / 3.1-8B、Qwen3-8B / 14B）、六个 benchmark（TriviaQA、CommonsenseQA、Belebele、CoQA、Math、SVAMP），采用「留一域」协议：训练相关方法在每个数据集上训练，所有方法都在其余五个数据集上评测，避免在自己的训练域上测试。指标为跨域平均 AUROC。

模型  | Perplexity  | SAPLMA（训练相关）  | PRISM  | ICR Probe  | SpikeScore
--- | --- | --- | --- | --- | ---
Llama-3.2-3B  | 0.5953  | 0.5693  | 0.6953  | 0.7463  | 0.7474
Llama-3.1-8B  | 0.6425  | 0.5764  | 0.7029  | 0.7439  | 0.7860
Qwen3-8B  | 0.6111  | 0.5705  | 0.7032  | 0.7381  | 0.7473
Qwen3-14B  | 0.6302  | 0.5787  | 0.7072  | 0.7435  | 0.7874

传统训练相关方法（MM、SEP、SAPLMA）跨域几乎全军覆没（平均 AUROC 多在 0.53–0.58）；训练无关方法略好但仍逊于专门的跨域方法；SpikeScore 在所有模型上取得最高平均 AUROC，且在更大模型上提升更明显（作者推测大模型自我纠错更强，尖峰模式更可检测）。



# or19245api

{"chunk_id":"b429c1","wall_time_seconds":1.202887709,"exit_code":0,"original_token_count":68,"output":"{\"name\":\"ChallengeRequiredError\",\"message\":\"Challenge verification required (2026-10-04-2690926)\",\"status\":403,\"details\":{\"challengeUrl\":\"https://openreview.net/challenge?redirect=https%3A%2F%2Fapi2.openreview.net%2Fnotes%3Fid%3DY16qXOaylp\",\"reqId\":\"2026-10-04-2690926\"}}"}


# muon19400_bound

Improved Convergence Rates of Muon Optimizer for Nonconvex Optimization (https://arxiv.org/html/2601.19400v1)
citeturn28133view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19400v1","lineno":383}); Total lines: 514
L346: which completes the proof. ∎
L347: 
L348: We are now in a position to prove Theorem cite44†3.1 .
L349: ###### Proof.
L350: 
L351: of Theorem cite44†3.1 L352: 
L353: (i) Lemma cite59†3.1 and Lemma cite62†3.2 (i) imply that, for all $t\in\mathbb{N}$,
L354:  |  | $\displaystyle\eta_{t}\mathbb{E}[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}]$  |
L355:  |  | $\displaystyle\leq\mathbb{E}[f(\bm{W}_{t})-f(\bm{W}_{t+1})]+\frac{nL\eta_{t}^{2}}{2}$  |
L356:  |  | $\displaystyle\quad+2\sqrt{n}\eta_{t}\left\{\beta^{t}\|\bm{M}_{0}-\nabla f(\bm{W}_{0})\|_{\mathrm{F}}+L\sqrt{n}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}+(1-\beta)\sigma\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}\right\}$  |
L357:  |  | $\displaystyle=\mathbb{E}[f(\bm{W}_{t})-f(\bm{W}_{t+1})]+\frac{nL\eta_{t}^{2}}{2}+2\|\bm{M}_{0}-\nabla f(\bm{W}_{0})\|_{\mathrm{F}}\sqrt{n}\eta_{t}\beta^{t}$  |
L358:  |  | $\displaystyle\quad+2Ln\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}+2(1-\beta)\sigma\sqrt{n}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}.$  |
L359: Let $T\in\mathbb{N}$. Summing the above inequality from $t=0$ to $t=T-1$ ensures that
L360:  | $\displaystyle\sum_{t=0}^{T-1}\eta_{t}\mathbb{E}[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}]$  | $\displaystyle\leq f(\bm{W}_{0})-f^{\star}+\frac{nL}{2}\sum_{t=0}^{T-1}\eta_{t}^{2}+2\|\bm{M}_{0}-\nabla f(\bm{W}_{0})\|_{\mathrm{F}}\sqrt{n}\sum_{t=0}^{T-1}\eta_{t}\beta^{t}$  |
L361:  |  | $\displaystyle\quad+2Ln\sum_{t=0}^{T-1}\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}+2(1-\beta)\sigma\sqrt{n}\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}},$  |
L362: which, together with $\min_{t\in[0:T-1]}\mathbb{E}[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}]\leq\sum_{t=0}^{T-1}\eta_{t}\mathbb{E}[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}]/\sum_{t=0}^{T-1}\eta_{t}$, implies that
L363:  | $\displaystyle\min_{t\in[0:T-1]}\mathbb{E}[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}]$  | $\displaystyle\leq\frac{f(\bm{W}_{0})-f^{\star}}{\sum_{t=0}^{T-1}\eta_{t}}+\frac{nL}{2}\frac{\sum_{t=0}^{T-1}\eta_{t}^{2}}{\sum_{t=0}^{T-1}\eta_{t}}+2\|\bm{M}_{0}-\nabla f(\bm{W}_{0})\|_{\mathrm{F}}\sqrt{n}\frac{\sum_{t=0}^{T-1}\eta_{t}\beta^{t}}{\sum_{t=0}^{T-1}\eta_{t}}$  |
L364:  |  | $\displaystyle\quad+2Ln\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}}{\sum_{t=0}^{T-1}\eta_{t}}+2(1-\beta)\sigma\sqrt{n}\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}}{\sum_{t=0}^{T-1}\eta_{t}}.$  |
L365: (ii) Lemma cite59†3.1 and Lemma cite62†3.2 (ii) imply that, for all $t\in\mathbb{N}$,
L366:  |  | $\displaystyle\eta_{t}\mathbb{E}[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}]$  |
L367:  |  | $\displaystyle\leq\mathbb{E}[f(\bm{W}_{t})-f(\bm{W}_{t+1})]+\frac{nL\eta_{t}^{2}}{2}$  |
L368:  |  | $\displaystyle\quad+2\sqrt{n}\eta_{t}\left\{\beta^{t+1}\|\bm{M}_{0}-\nabla f(\bm{W}_{0})\|_{\mathrm{F}}]+\beta L\sqrt{n}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}+\beta(1-\beta)\sigma\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}+\frac{(1-\beta)\sigma}{\sqrt{b_{t}}}\right\}$  |
L369:  |  | $\displaystyle=\mathbb{E}[f(\bm{W}_{t})-f(\bm{W}_{t+1})]+\frac{nL\eta_{t}^{2}}{2}+2\|\bm{M}_{0}-\nabla f(\bm{W}_{0})\|_{\mathrm{F}}\sqrt{n}\eta_{t}\beta^{t+1}$  |
L370:  |  | $\displaystyle\quad+2\beta Ln\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}+2\beta(1-\beta)\sigma\sqrt{n}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}+\frac{2\sqrt{n}(1-\beta)\sigma\eta_{t}}{\sqrt{b_{t}}}.$  |
L371: A discussion similar to the one proving Theorem cite44†3.1 (i) implies that Theorem cite44†3.1 (ii) holds. This completes the proof. ∎
L372: ## 4 Conclusion
L373: We presented a comprehensive convergence analysis of the Muon optimizer. By investigating combinations of Nesterov acceleration, four types of learning rates, and two batch-size configurations, we derived improved convergence rates under significantly weaker assumptions compared with existing studies. Our analysis highlights that the combination of a diminishing learning rate and an exponentially growing batch size yields the most favorable results in terms of both stability and convergence rate.
L374: Furthermore, we demonstrated that by appropriately coupling the learning rate and batch size as functions of the total number of iterations $T$, superior convergence rates can also be achieved across other combinations. These findings provide a theoretical foundation for more efficient hyperparameter tuning in Muon-based optimization.
L375: ## References
L376:   * Ahn et al. (2025) Kwangjun Ahn, Noah Amsel, and John Langford. Dion2: A simple method to shrink matrix in Muon, 2025. URL cite63†https://arxiv.org/abs/2512.16928 .
L377:   * AI et al. (2025) Essential AI, :, Ishaan Shah, Anthony M. Polloreno, Karl Stratos, Philip Monk, Adarsh Chaluvaraju, Andrew Hojel, Andrew Ma, Anil Thomas, Ashish Tanwer, Darsh J Shah, Khoi Nguyen, Kurt Smith, Michael Callahan, Michael Pust, Mohit Parmar, Peter Rushton, Platon Mazarakis, Ritvik Kapila, Saurabh Srivastava, Somanshu Singla, Tim Romanski, Yash Vanjani, and Ashish Vaswani. Practical efficiency of Muon for pretraining, 2025. URL cite64†https://arxiv.org/abs/2505.02222 .
L378:   * Beck (2017) Amir Beck. First-Order Methods in Optimization. Society for Industrial and Applied Mathematics, Philadelphia, PA, 2017. doi: 10.1137/1.9781611974997. URL cite65†https://epubs.siam.org/doi/abs/10.1137/1.9781611974997†epubs.siam.org .
L379:   * Chang et al. (2025) Da Chang, Yongxiang Liu, and Ganzhao Yuan. On the convergence of Muon and beyond, 2025. URL cite66†https://arxiv.org/abs/2509.15816 .
L380:   * Gruntkowska et al. (2025) Kaja Gruntkowska, Yassine Maziane, Zheng Qu, and Peter Richtárik. Drop-Muon: Update less, converge faster, 2025. URL cite67†https://arxiv.org/abs/2510.02239 .
L381:   * Huang et al. (2025) Feihu Huang, Yuning Luo, and Songcan Chen. LiMuon: Light and fast Muon optimizer for large models, 2025. URL cite68†https://arxiv.org/abs/2509.14562 .
L382:   * Jordan et al. (2024) Keller Jordan, Yuchen Jin, Vlado Boza, Jiacheng You, Franz Cesista, Laker Newhouse, and Jeremy Bernstein. Muon: An optimizer for hidden layers in neural networks. cite69†https://kellerjordan.github.io/posts/muon/†kellerjordan.github.io , 2024.
L383:   * Kingma & Ba (2015) Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In Proceedings of the 3rd International Conference on Learning Representations (ICLR), 2015. URL cite70†https://arxiv.org/abs/1412.6980 .
L384:   * Li & Hong (2025) Jiaxiang Li and Mingyi Hong. A note on the convergence of Muon, 2025. URL cite71†https://arxiv.org/abs/2502.02900 .
L385:   * Liu et al. (2025a) Jingyuan Liu, Jianlin Su, Xingcheng Yao, Zhejun Jiang, Guokun Lai, Yulun Du, Yidao Qin, Weixin Xu, Enzhe Lu, Junjie Yan, Yanru Chen, Huabin Zheng, Yibo Liu, Shaowei Liu, Bohong Yin, Weiran He, Han Zhu, Yuzhi Wang, Jianzhou Wang, Mengnan Dong, Zheng Zhang, Yongsheng Kang, Hao Zhang, Xinran Xu, Yutao Zhang, Yuxin Wu, Xinyu Zhou, and Zhilin Yang. Muon is scalable for LLM training, 2025a. URL cite72†https://arxiv.org/abs/2502.16982 .
L386:   * Liu et al. (2025b) Junkang Liu, Fanhua Shang, Junchao Zhou, Hongying Liu, Yuanyuan Liu, and Jin Liu. FedMuon: Accelerating federated learning with matrix orthogonalization, 2025b. URL cite73†https://arxiv.org/abs/2510.27403 .
L387:   * Loshchilov & Hutter (2019) Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Conference on Learning Representations, 2019. URL cite74†https://openreview.net/forum?id=Bkg6RiCqY7†openreview.net .
L388:   * Mehta et al. (2025) Sushant Mehta, Raj Dandekar, Rajat Dandekar, and Sreedath Panat. Muon: Training and trade-offs with latent attention and MoE, 2025. URL cite75†https://arxiv.org/abs/2509.24406 .
L389:   * Nesterov (1983) Y. Nesterov. A method for unconstrained convex minimization problem with the rate of convergence $o(1/k^{2})$. Doklady AN USSR, 269:543–547, 1983.
L390:   * Oowada & Iiduka (2025) Kanata Oowada and Hideaki Iiduka. Faster convergence of Riemannian stochastic gradient descent with increasing batch size. In The 17th Asian Conference on Machine Learning (Conference Track), 2025. URL cite76†https://openreview.net/forum?id=aUD72YpA79†openreview.net .
L391:   * Polyak (1964) B.T. Polyak. Some methods of speeding up the convergence of iteration methods. USSR Computational Mathematics and Mathematical Physics, 4(5):1–17, 1964. ISSN 0041-5553. doi: https://doi.org/10.1016/0041-5553(64)90137-5. URL cite77†https://www.sciencedirect.com/science/article/pii/0041555364901375†www.sciencedirect.com .
L392:   * Robbins & Monro (1951) H. Robbins and S. Monro. A stochastic approximation method. Annals of Mathematical Statistics, 22(3):400–407, 1951.
L393:   * Sato et al. (2025) Naoki Sato, Hiroki Naganuma, and Hideaki Iiduka. Convergence bound and critical batch size of Muon optimizer, 2025. URL cite78†https://arxiv.org/abs/2507.01598 .
L394:   * Shen et al. (2025) Wei Shen, Ruichuan Huang, Minhui Huang, Cong Shen, and Jiawei Zhang. On the convergence analysis of Muon, 2025. URL cite79†https://arxiv.org/abs/2505.23737 .
L395:   * Si et al. (2025) Chongjie Si, Debing Zhang, and Wei Shen. AdaMuon: Adaptive Muon optimizer, 2025. URL cite80†https://arxiv.org/abs/2507.11005 .
L396:   * Smith et al. (2018) Samuel L. Smith, Pieter-Jan Kindermans, and Quoc V. Le. Don’t decay the learning rate, increase the batch size. In International Conference on Learning Representations, 2018. URL cite81†https://openreview.net/forum?id=B1Yy1BxCZ†openreview.net .
L397:   * Sutskever et al. (2013) Ilya Sutskever, James Martens, George Dahl, and Geoffrey Hinton. On the importance of initialization and momentum in deep learning. In Sanjoy Dasgupta and David McAllester (eds.), Proceedings of the 30th International Conference on Machine Learning, volume 28 of Proceedings of Machine Learning Research, pp. 1139–1147, Atlanta, Georgia, USA, 17–19 Jun 2013. PMLR. URL cite82†https://proceedings.mlr.press/v28/sutskever13.html†proceedings.mlr.press .
L398:   * Tang et al. (2025) Xuan Tang, Jichu Li, and Difan Zou. A convergence analysis of adaptive optimizers under floating-point quantization, 2025. URL cite83†https://arxiv.org/abs/2510.21314 .
L399:   * Umeda & Iiduka (2025) Hikaru Umeda and Hideaki Iiduka. Increasing both batch size and learning rate accelerates stochastic gradient descent. Transactions on Machine Learning Research, 2025. ISSN 2835-8856. URL cite84†https://openreview.net/forum?id=sbmp55k6iE†openreview.net .
L400:   * Wang et al. (2025) Shuche Wang, Fengzhuo Zhang, Jiaxiang Li, Cunxiao Du, Chao Du, Tianyu Pang, Zhuoran Yang, Mingyi Hong, and Vincent Y. F. Tan. Muon outperforms Adam in tail-end associative memory learning, 2025. URL cite85†https://arxiv.org/abs/2509.26030 .
L401:   * Zhang et al. (2025) Minxin Zhang, Yuxuan Liu, and Hayden Schaeffer. AdaGrad meets Muon: Adaptive stepsizes for orthogonal updates, 2025. URL cite86†https://arxiv.org/abs/2509.02981 .
L402: ## Appendix A Proof of Corollary cite51†3.1 L403: ###### Proof.
L404: 
L405: (i) When using $\eta_{t}\coloneqq\eta$ and $b_{t}\coloneqq b$, we have
L406:  |  | $\displaystyle\frac{1}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{\eta T},\text{ }\frac{\sum_{t=0}^{T-1}\eta_{t}^{2}}{\sum_{t=0}^{T-1}\eta_{t}}=\eta,\text{ }\frac{\sum_{t=0}^{T-1}\eta_{t}\beta^{t}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{T}\sum_{t=0}^{T-1}\beta^{t}\leq\frac{1}{(1-\beta)T},$  |
L407:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{\eta}{T}\sum_{t=0}^{T-1}\sum_{i=1}^{t}\beta^{i}=\frac{\eta}{T}\sum_{t=0}^{T-1}\frac{\beta(1-\beta^{t})}{1-\beta}\leq\frac{\eta}{1-\beta},$  |
L408:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{T\sqrt{b}}\sum_{t=0}^{T-1}\sum_{i=0}^{t}\beta^{i}\leq\frac{1}{(1-\beta)\sqrt{b}},\text{ }\frac{\sum_{t=0}^{T-1}\frac{\eta_{t}}{\sqrt{b_{t}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{\sqrt{b}}.$  |
L409: Theorem cite44†3.1 thus leads to Corollary cite51†3.1 (i).
L410: 
L411: (ii) When using $\eta_{t}\coloneqq\eta$ and $b_{t}\coloneqq b\delta^{t}$, we have
L412:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{T\sqrt{b}}\sum_{t=0}^{T-1}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{\delta^{t-i}}}\leq\frac{1}{(1-\beta)T\sqrt{b}}\sum_{t=0}^{T-1}\frac{1}{\sqrt{\delta^{t}}}\leq\frac{\sqrt{\delta}}{(1-\beta)(\sqrt{\delta}-1)T\sqrt{b}},$  |
L413:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\frac{\eta_{t}}{\sqrt{b_{t}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{T\sqrt{b}}\sum_{t=0}^{T-1}\frac{1}{\sqrt{\delta^{t}}}\leq\frac{\sqrt{\delta}}{(\sqrt{\delta}-1)T\sqrt{b}}.$  |
L414: Hence, Theorem cite44†3.1 thus leads to Corollary cite51†3.1 (ii).
L415: 
L416: (iii) Section A.3 in (cite53†Umeda & Iiduka, 2025 ) ensures that $\eta_{t}=\frac{\eta}{2}(1+\cos\frac{t\pi}{T})$ satisfies
L417: 
L418:  | $\displaystyle\sum_{t=0}^{T-1}\eta_{t}\geq\frac{\eta T}{2}\text{ and }\sum_{t=0}^{T-1}\eta_{t}^{2}=\frac{3\eta^{2}T}{8}+\frac{\eta^{2}}{2}.$  |
L419: 
L420: Hence,
L421:  | $\displaystyle\frac{1}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{2}{\eta T}\text{ and }\frac{\sum_{t=0}^{T-1}\eta_{t}^{2}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{\eta}{T}+\frac{3\eta}{4}.$  |
L422: 
L423: Using $b_{t}=b$ implies that
L424:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\beta^{t}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{2}{T}\sum_{t=0}^{T-1}\beta^{t}\leq\frac{2}{(1-\beta)T},$  |
L425:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{2\eta}{T}\sum_{t=0}^{T-1}\sum_{i=1}^{t}\beta^{i}=\frac{2\eta}{T}\sum_{t=0}^{T-1}\frac{\beta(1-\beta^{t})}{1-\beta}\leq\frac{2\eta}{1-\beta}.$  |
L426: 
L427: Moreover,
L428:  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{2}{T\sqrt{b}}\sum_{t=0}^{T-1}\sum_{i=0}^{t}\beta^{i}\leq\frac{2}{(1-\beta)\sqrt{b}}\text{ and }\frac{\sum_{t=0}^{T-1}\frac{\eta_{t}}{\sqrt{b_{t}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{\sqrt{b}}.$  |
L429: 
L430: Hence, Theorem cite44†3.1 thus leads to Corollary cite51†3.1 (iii).
L431: 
L432: (iv) Using the proof of Corollaries cite51†3.1 (ii) and (iii) leads to Corollary cite51†3.1 (iv).
L433: (v) Section A.3 in (cite53†Umeda & Iiduka, 2025 ) ensures that $\eta_{t}=\eta(1-\frac{t}{T})^{p}$ satisfies
L434: 
L435:  | $\displaystyle\sum_{t=0}^{T-1}\eta_{t}\geq\frac{\eta T}{p+1}\text{ and }\sum_{t=0}^{T-1}\eta_{t}^{2}\leq\frac{\eta^{2}(2p+T+1)}{2p+1}.$  |
L436: 
L437: Hence,
L438: 
L439:  | $\displaystyle\frac{1}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{p+1}{\eta T}\text{ and }\frac{\sum_{t=0}^{T-1}\eta_{t}^{2}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{(p+1)(2p+T+1)\eta}{(2p+1)T}.$  |
L440: 
L441: Using $b_{t}=b$ implies that
L442:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\beta^{t}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{p+1}{T}\sum_{t=0}^{T-1}\beta^{t}\leq\frac{p+1}{(1-\beta)T},$  |
L443:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=1}^{t}\beta^{i}\eta_{t-i}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{(p+1)\eta}{T}\sum_{t=0}^{T-1}\sum_{i=1}^{t}\beta^{i}=\frac{(p+1)\eta}{T}\sum_{t=0}^{T-1}\frac{\beta(1-\beta^{t})}{1-\beta}\leq\frac{(p+1)\eta}{1-\beta}.$  |
L444: 
L445: Moreover,
L446:  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{p+1}{T\sqrt{b}}\sum_{t=0}^{T-1}\sum_{i=0}^{t}\beta^{i}\leq\frac{p+1}{(1-\beta)\sqrt{b}}\text{ and }\frac{\sum_{t=0}^{T-1}\frac{\eta_{t}}{\sqrt{b_{t}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{\sqrt{b}}.$  |
L447: 
L448: Hence, Theorem cite44†3.1 thus leads to Corollary cite51†3.1 (v).
L449: 
L450: (vi) The proof of Corollary cite51†3.1 (vi) is similar to those of Corollaries cite51†3.1 (ii) and (v).
L451: (vii) From $\eta_{t}=\frac{\eta}{(t+1)^{a}}$, we have
L452: 
L453:  | $\displaystyle\sum_{t=0}^{T-1}\eta_{t}\geq\eta\int_{0}^{T}\frac{\mathrm{d}t}{(t+1)^{a}}=\begin{cases}\frac{\eta}{1-a}\{(T+1)^{1-a}-1\}\text{ }&(a\in(0,1)),\\
L454: \eta\log(T+1)\text{ }&(a=1)\end{cases}$  |
L455: 
L456: and
L457:  | $\displaystyle\sum_{t=0}^{T-1}\eta_{t}^{2}\leq\eta^{2}\left(1+\int_{0}^{T-1}\frac{\mathrm{d}t}{(t+1)^{2a}}\right)=\begin{cases}\frac{\eta^{2}}{1-2a}T^{1-2a}\text{ }&\left(a\in\left(0,\frac{1}{2}\right)\right),\\
L458: \eta^{2}(1+\log T)\text{ }&\left(a=\frac{1}{2}\right),\\
L459: \frac{2a\eta^{2}}{2a-1}\text{ }&\left(a\in\left(\frac{1}{2},1\right]\right).\end{cases}$  |
L460: 
L461: Accordingly,
L462:  | $\displaystyle\frac{1}{\sum_{t=0}^{T-1}\eta_{t}}\leq\begin{cases}\frac{1-a}{\eta(T^{1-a}-1)}\text{ }&(a\in(0,1)),\\
L463: \frac{1}{\eta\log T}\text{ }&(a=1)\end{cases}\text{ and }\frac{\sum_{t=0}^{T-1}\eta_{t}^{2}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\begin{cases}\frac{(1-a)\eta T^{1-2a}}{(1-2a)(T^{1-a}-1)}\text{ }&\left(a\in\left(0,\frac{1}{2}\right)\right),\\
L464: \frac{\eta(1+\log T)}{2(\sqrt{T}-1)}\text{ }&\left(a=\frac{1}{2}\right),\\
L465: \frac{2a(1-a)\eta}{(2a-1)(T^{1-a}-1)}\text{ }&\left(a\in\left(\frac{1}{2},1\right)\right),\\
L466: \frac{2\eta}{\log T}\text{ }&\left(a=1\right).\end{cases}$  |
L467: From $\sum_{t=0}^{T-1}\eta_{t}\beta^{t}\leq\eta\sum_{t=0}^{T-1}\beta^{t}<\frac{\eta}{1-\beta}$, we have
L468: 
L469:  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\beta^{t}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\begin{cases}\frac{1-a}{(1-\beta)(T^{1-a}-1)}\text{ }&(a\in(0,1)),\\
L470: \frac{1}{(1-\beta)\log T}\text{ }&(a=1).\end{cases}$  |
L471: 
L472: Moreover, since we have
L473:  | $\displaystyle\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\beta^{i}\eta_{t-i}\leq\sum_{k=0}^{T-1}\eta_{k}^{2}\sum_{t=k}^{T-1}\beta^{t-k}\leq\frac{1}{1-\beta}\sum_{k=0}^{T-1}\eta_{k}^{2},$  |
L474: 
L475: we also have
L476:  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\beta^{i}\eta_{t-i}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\begin{cases}\frac{(1-a)\eta T^{1-2a}}{(1-2a)(1-\beta)(T^{1-a}-1)}\text{ }&\left(a\in\left(0,\frac{1}{2}\right)\right),\\
L477: \frac{\eta(1+\log T)}{2(1-\beta)(\sqrt{T}-1)}\text{ }&\left(a=\frac{1}{2}\right),\\
L478: \frac{2a(1-a)\eta}{(2a-1)(1-\beta)(T^{1-a}-1)}\text{ }&\left(a\in\left(\frac{1}{2},1\right)\right),\\
L479: \frac{2\eta}{(1-\beta)\log T}\text{ }&\left(a=1\right).\end{cases}$  |
L480: From $b_{t}=b$, we have
L481: 
L482:  |  | $\displaystyle\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\frac{\beta^{i}}{\sqrt{b_{t-i}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{\sqrt{b}}\frac{\sum_{t=0}^{T-1}\eta_{t}\sum_{i=0}^{t}\beta^{i}}{\sum_{t=0}^{T-1}\eta_{t}}\leq\frac{1}{(1-\beta)\sqrt{b}}\text{ and }\frac{\sum_{t=0}^{T-1}\frac{\eta_{t}}{\sqrt{b_{t}}}}{\sum_{t=0}^{T-1}\eta_{t}}=\frac{1}{\sqrt{b}}.$  |
L483: 
L484: Hence, Theorem cite44†3.1 leads to Corollary cite51†3.1 (vii).
L485: 
L486: (viii) From $b_{t}=b\delta^{t}$, we have



