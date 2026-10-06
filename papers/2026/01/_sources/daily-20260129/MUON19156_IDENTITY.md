Published as a conference paper at ICLR 2026 (https://openreview.net/pdf/cbafd6877955033abb5c15caa533face92b6eea1.pdf)
citeturn28393search12 [wordlim: 200] Published: 4 months ago; CONVERGENCE OF MUON WITH NEWTON–SCHULZGyu Yeol Kim ... Overall, our theory justifies the practical NEWTON–SCHULZ design of ... ing research questions remain open:
Published as a conference paper at ICLR 2026
CONVERGENCE OF MUON WITH NEWTON–SCHULZ
Gyu Yeol Kim
Seoul National University
gyuyeolkim@snu.ac.kr
Min-hwan Oh
Seoul National University
minoh@snu.ac.kr
ABSTRACT
We analyze MUON as originally proposed—using the momentum orthogonaliza-
tion with a few NEWTON–SCHULZ steps. The prior theoretical results replace
this key step in MUON with an exact SVD-based polar factor. We prove that
MUON with NEWTON–SCHULZ converges to a stationary point at the same rate
as the SVD-polar idealization, up to a constant factor for a given number q of
NEWTON–SCHULZ steps. We further analyze this constant factor and prove that it
converges to 1 doubly exponentially in q and improves with the degree of the poly-
nomial used in NEWTON–SCHULZ for approximating the orthogonalization di-
rection. We also prove that MUON improves the rank dependence compared to its
vector-based counterpart, SGD with momentum. Our results explain why MUON
with a few low-degree NEWTON–SCHULZ steps matches exact-polar (SVD) be-
and then uses this orthogonalized direction to update the weights. In practice, this orthogonal-
ization is not computed via an exact singular value decomposition (SVD)—which is accurate but
expensive—but is approximated efficiently by a small, fixed number of NEWTON–SCHULZ steps.
Empirical studies (Jordan et al., 2024; Liu et al., 2025a) have reported strong performance at scale
with this SVD-free implementation, making MUON an attractive alternative to vector-based opti-
mizers. Despite recent attempts to analyze the convergence of MUON (Shen et al., 2025; Li &
Hong, 2025; Sato et al., 2025; Pethick et al., 2025a;b), theory still lags behind practice. Exist-
ing analyses typically study an idealized variant that replaces the NEWTON–SCHULZ step—central
to practical MUON—with an exact polar step computed by SVD for analytical convenience. This
leaves open whether the actual SVD-free orthogonalization used in practice—i.e., a finite number
of NEWTON–SCHULZ steps—admits principled nonconvex convergence guarantees, and how the
NEWTON–SCHULZ approximation impacts rank dependence and efficiency. Therefore, the follow-
ing research questions remain open:
Research questions.
• Does MUON with NEWTON–SCHULZ admit nonconvex convergence guarantees, and how
do its rates compare to the exact SVD–polar idealization?
1--------------------------------------------------------------------------------
Published as a conference paper at ICLR 2026 (https://openreview.net/pdf?id=lJSfxtLpLm)
citeturn28393search13 [wordlim: 200] Published: 6 months ago; # CONVERGENCE OF MUON WITH NEWTON–SCHULZ**Gyu Yeol Kim** ... This leaves open whether the actual SVD-free orthogonalization used in practice—i.e., a finite number of Newton–Schulz steps—admits principled nonconvex convergence guarantees, and how the Newton–Schulz approximation impacts rank dependence and efficiency.
Published as a conference paper at ICLR 2026

# CONVERGENCE OF MUON WITH NEWTON–SCHULZ

**Gyu Yeol Kim**  
Seoul National University  
Seoul, South Korea  
gyuyeolkim@snu.ac.kr

**Min-hwan Oh**  
Seoul National University  
Seoul, South Korea  
minoh@snu.ac.kr

## ABSTRACT

We analyze Muon as originally proposed and used in practice—using the momentum orthogonalization with a few Newton–Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton–Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number q of Newton–Schulz steps. We further analyze this constant factor and prove that it converges to 1 doubly exponentially in q and improves with the degree of the polynomial used in Newton–Schulz for approximating the orthogonalization direction. We also prove that Muon improves the rank dependence compared to its vector-based counterpart, SGD with momentum. At each iteration, instead of following the raw momentum, Muon orthogonalizes the momentum matrix and then uses this orthogonalized direction to update the weights. In practice, this orthogonalization is not computed via an exact singular value decomposition (SVD)—which is accurate but expensive—but is approximated efficiently by a small, fixed number of Newton–Schulz steps. Empirical studies (Jordan et al., 2024; Liu et al., 2025a) have reported strong performance at scale with this SVD-free implementation, making Muon an attractive alternative to vector-based optimizers. Despite recent attempts to analyze the convergence of Muon (Shen et al., 2025; Li & Hong, 2025; Sato et al., 2025; Pethick et al., 2025a;b), theory still lags behind practice. Existing analyses typically study an idealized variant that replaces the Newton–Schulz step—central to practical Muon—with an exact polar step computed by SVD for analytical convenience. This leaves open whether the actual SVD-free orthogonalization used in practice—i.e., a finite number of Newton–Schulz steps—admits principled nonconvex convergence guarantees, and how the Newton–Schulz approximation impacts rank dependence and efficiency. Therefore, the following research questions remain open:

**Research questions.**

- Does Muon with Newton–Schulz admit nonconvex convergence guarantees, and how do its rates compare to the exact SVD–polar idealization?

1--------------------------------------------------------------------------------
Convergence of Muon with Newton-Schulz (https://arxiv.org/abs/2601.19156)
citeturn28393academia14 [wordlim: 200] Published: 8 months ago; Title: Convergence of Muon with Newton-SchulzAuthors: Gyu Yeol Kim, Min-hwan Oh ... Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.
Title: Convergence of Muon with Newton-Schulz
Authors: Gyu Yeol Kim, Min-hwan Oh
Date: Tue Jan 27 03:40:48 2026

We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number $q$ of Newton-Schulz steps. We further analyze this constant factor and prove that it converges to 1 doubly exponentially in $q$ and improves with the degree of the polynomial used in Newton-Schulz for approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum. Our results explain why Muon with a few low-degree Newton-Schulz steps matches exact-polar (SVD) behavior at a much faster wall-clock time and explain how much momentum matrix orthogonalization via Newton-Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.--------------------------------------------------------------------------------
Convergence of Muon with Newton-Schulz — Lacuna (https://lacuna.tiptreesystems.com/work/convergence-of-muon-with-newton-schulz/wrk_220846cc0a707b6dfdda4ca602ac7a9a)
citeturn28393search0 [wordlim: 200] Crawled: last week; # Convergence of Muon with Newton-SchulzGyu Yeol Kim, Min-hwan OhICLR 2026 · OpenReview ... While the theory strongly justifies the use of small $q$, the choice of the Newton–Schulz polynomial degree $\kappa$ presents a trade-off between accuracy per step and computational cost that could be further optimized.

# Convergence of Muon with Newton-Schulz

Gyu Yeol Kim, Min-hwan Oh

ICLR 2026 · OpenReview

The paper Convergence of Muon with Newton–Schulz provides the first rigorous theoretical foundation for why the popular MUON optimizer works so well in practice, specifically focusing on its efficient "SVD-free" implementation. It bridges the gap between the theoretical ideal of MUON and its practical, high-performance application in deep learning.

## The Theory-Practice Gap in Matrix Optimization

Most deep learning optimizers, such as SGD or Adam, treat neural network parameters as long, flat vectors. This approach ignores the natural matrix structure inherent in linear and attention layers. MUON (Momentum Orthogonalized) was recently introduced to exploit this structure by "orthogonalizing" the momentum matrix before updating weights, helping the optimizer navigate the loss landscape more effectively.

However, a significant gap existed between MUON's theory and its practical usage:
--------------------------------------------------------------------------------
Beyond the Ideal: Analyzing the Inexact Muon Update (https://openreview.net/attachment?id=IBRMWPBouf&name=pdf)
citeturn28393search15 [wordlim: 200] Published: 5 months ago; Their theory is tailored to this modified direction computation, giving deterministic stationarity ... Convergence of Muon with Newton–Schulz. ... In this sense, Kim and Oh (2026) refine the Newton–
attention to a more informative low-rank subspace.
FedMuon.
Takezawa et al. (2026) study inexact Newton–Schulz orthogonalization in FedMuon. The most
relevant point for our paper is that, in the spectral-norm/Newton–Schulz setting, they prove a solver-specific
result that is in some sense sharper than a generic perturbation bound: the method can converge for any number
of Newton–Schulz iterations, with the approximate-LMO guarantee stated in a q-dependent Schatten-p norm that
improves toward the trace-norm guarantee as q increases. This differs substantially from our abstraction, which
is centralized, solver-agnostic, and based on an additive direction error ∥ˆd−d∥≤δ. We therefore view Takezawa
et al. (2026) as complementary evidence that specialized analyses can exploit the structure of a particular solver
more sharply than a general inexact-LMO framework.
Convergence of Muon with Newton–Schulz.
The closest concurrent work is Kim and Oh (2026), which
analyzes the original Muon algorithm with finitely many Newton–Schulz steps. Their results are specialized to
operator-nuclear geometry and show that Muon with Newton–Schulz matches the exact SVD-polar rate up to
a q-dependent constant factor, which approaches 1 doubly exponentially fast in the number of Newton–Schulz
steps. Compared to our paper, this is narrower but sharper: their analysis is explicitly tied to Newton–Schulz
and yields a direct dependence on the inner-iteration count q, while our framework covers multiple approximation
schemes (e.g., Newton–Schulz and PolarExpress), allows infeasible approximate directions, and yields generic
δ-dependent guidance for learning rate and momentum. In this sense, Kim and Oh (2026) refine the Newton–
Schulz-specific part of the story that our broader inexact-LMO model abstracts.--------------------------------------------------------------------------------
Convergence of Muon with Newton-Schulz (https://proceedings.iclr.cc/paper_files/paper/2026/hash/4c0129f1f7a036af5ed2409f1f9f8131-Abstract-Conference.html)
citeturn28393search1 [wordlim: 200] Crawled: today; # Convergence of Muon with Newton-SchulzGyu Yeol Kim, Min-hwan Oh ... Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice–theory gap.
# Convergence of Muon with Newton-Schulz

Gyu Yeol Kim, Min-hwan Oh

International Conference on Learning Representations 2026 (ICLR 2026) Conference

Bibtex Paper

## Abstract

We analyze Muon as originally proposed, using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point with the same rate as the SVD-polar idealization, up to a constant factor for given the number of Newton-Schulz steps $q$. We further analyze this constant factor, and prove that it converges to 1 doubly exponentially in $q$ and improves with the degree of a polynomial used in Newton-Schulz for approximating the orthogonalization direction. We also prove that Muon improves the rank dependence compared to its vector-based counterpart, SGD with momentum. Our results explain why Muon with a few low-degree Newton-Schulz steps matches exact-polar (SVD) behavior at much faster wall-clock time, and explain how much momentum matrix orthogonalization via Newton-Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice–theory gap.--------------------------------------------------------------------------------
Convergence of Muon with Newton-Schulz · ICLR 2026 (https://aiconfpaper.com/paper/iclr-2026-lJSfxtLpLm)
citeturn28393search2 [wordlim: 200] Crawled: 4 days ago; # Convergence of Muon with Newton-Schulz ...     kim2026convergence, ...     url={https://openreview.net/forum?

ICLR 2026 poster 0 citations

# Convergence of Muon with Newton-Schulz

Save

Gyu Yeol Kim, Min-hwan Oh

Source ↗TeX ↗

## Abstract

We analyze Muon as originally proposed and used in practice---using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point with the same rate as the SVD-polar idealization, up to a constant factor for given the number of Newton-Schulz steps $q$. We further analyze this constant factor, and prove that it converges to 1 doubly exponentially in $q$ and improves with $\kappa$, which is the degree of a polynomial used in Newton-Schulz required when approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum. Our results explain why Muon with a few low-degree Newton-Schulz steps matches exact-polar (SVD) behavior at much faster wall-clock time, and explain how much momentum matrix orthogonalization via Newton-Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice–theory gap.

Muon Newton–Schulz Orthogonalization Nonconvex Optimization

BibTeX
    
    @inproceedings{
    kim2026convergence,
    title={Convergence of Muon with Newton-Schulz},
    author={Gyu Yeol Kim and Min-hwan Oh},
    booktitle={The Fourteenth International Conference on Learning Representations},
    year={2026},
    url={https://openreview.net/forum?id=lJSfxtLpLm}
    }--------------------------------------------------------------------------------
Publications - Min-hwan Oh | Seoul National University (https://minoh.io/publications/)
citeturn28393search3 [wordlim: 200] Crawled: yesterday; Hohyun Kim, Hyesung Kim, Min-hwan Oh, Seunggeun Lee ... Conference on Learning Theory (COLT), 2026Convergence of Muon with Newton-Schulz
SNACK: A Sequential Notation Framework for Probabilistic Graph Generation
Hohyun Kim, Hyesung Kim, Min-hwan Oh, Seunggeun Lee
Neural Information Processing Systems (NeurIPS), 2026

* * *

Practical and Optimal Algorithm for Linear Contextual Bandits with Rare Parameter Updates
Sanghoon Yu, Min-hwan Oh
International Conference on Machine Learning (ICML), 2026 (Spotlight)

Optimal Design for Multinomial Logit Model with Applications to Best Assortment Identification
Joongkyu Lee, Min-hwan Oh
International Conference on Machine Learning (ICML), 2026

* * *

Follow-the-Perturbed-Leader for Decoupled Bandits: Best-of-Both-Worlds and Practicality
Chaiwon Kim, Jongyeong Lee, Min-hwan Oh
International Conference on Machine Learning (ICML), 2026

Bilinear Bandits with Partially Observable Features
Wooseong Cho, Ji Hyeong Park, Min-hwan Oh
International Conference on Machine Learning (ICML), 2026

* * *

Latent Representation Alignment for Offline Goal-Conditioned Reinforcement Learning
Hyungkyu Kang, Byeongchan Kim, Min-hwan Oh
International Conference on Machine Learning (ICML), 2026

Generalized Linear Bandits with Memory
Heesang Ann, Hyunjun Choi, Taehyun Hwang, Younghoon Shin, Haeju Cheong, Min-hwan Oh
International Conference on Machine Learning (ICML), 2026

* * *

Unified Framework of Distributional Regret in Multi-Armed Bandits and Reinforcement Learning
Harin Lee, Min-hwan Oh
Conference on Learning Theory (COLT), 2026

Convergence of Muon with Newton-Schulz
Gyu Yeol Kim, Min-hwan Oh
International Conference on Learning Representations (ICLR), 2026

* * *

Peng’s Q(λ) for Conservative Value Estimation in Offline Reinforcement Learning
Byeongchan Kim, Min-hwan Oh
International Conference on Learning Representations (ICLR), 2026

--------------------------------------------------------------------------------
Paper page - Convergence of Muon with Newton-Schulz (https://huggingface.co/papers/2601.19156)
citeturn28393search4 [wordlim: 200] Published: 8 months ago; Crawled: 2 weeks ago; # Convergence of Muon with Newton-Schulz ... [Button: Gyu Yeol Kim] , ... Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.

Papers

arxiv:2601.19156

Copy markdown

# Convergence of Muon with Newton-Schulz

Published on Jan 27

Upvote -

Authors:

[Button: Gyu Yeol Kim] ,

[Button: Min-hwan Oh]

## Abstract

Muon optimizer's convergence properties are analyzed, showing that Newton-Schulz orthogonalization approximates SVD-based polar decomposition with improved efficiency.

Generated by Qwen/Qwen2.5-Coder-32B-Instruct

We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number q of Newton-Schulz steps. We further analyze this constant factor and prove that it converges to 1 doubly exponentially in q and improves with the degree of the polynomial used in Newton-Schulz for approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum. Our results explain why Muon with a few low-degree Newton-Schulz steps matches exact-polar (SVD) behavior at a much faster wall-clock time and explain how much momentum matrix orthogonalization via Newton-Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.--------------------------------------------------------------------------------
dblp: Min-hwan Oh (https://dblp.org/pid/172/0531.html)
citeturn28393search5 [wordlim: 200] Published: last month; Crawled: last month; Gyu-Yeol Kim, Min-hwan Oh:Convergence of Muon with Newton-Schulz. ...       * electronic edition via DOI (open access)
      * Semantic Scholar
      * Internet Archive Scholar
      * CiteSeerX
      * PubPeer

    * share record

      * Bluesky
      * Reddit
      * BibSonomy
      * LinkedIn

persistent URL:

      * https://dblp.org/rec/journals/corr/abs-2601-19156

Gyu-Yeol Kim, Min-hwan Oh:
Convergence of Muon with Newton-Schulz. CoRR abs/2601.19156 (2026)
  * Image: Informal and Other Publications

[i54]

    * view

      * electronic edition via DOI (open access)
      * details & citations

authority control:

      *  

    * export record

      * BibTeX
      * RIS
      * RDF N-Triples
      * RDF Turtle
      * RDF/XML
      * XML
--------------------------------------------------------------------------------
(PDF) Convergence of Muon with Newton-Schulz (https://www.researchgate.net/publication/400118699_Convergence_of_Muon_with_Newton-Schulz)
citeturn28393search6 [wordlim: 200] Published: 8 months ago; Crawled: last month; # Convergence of Muon with Newton-Schulz ... Gyu Yeol Kim ... Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap. ... Therefore, the following research questions remain open: ... We conduct a numerical experiment with the CIFAR-10 (50k/10k) dataset and a CNN model,

# Convergence of Muon with Newton-Schulz

  * January 2026

DOI:10.48550/arXiv.2601.19156

  * License
  * CC BY-NC-ND 4.0

Authors:

Gyu Yeol Kim

Gyu Yeol Kim

  * This person is not on ResearchGate, or hasn't claimed this research yet.

Min-hwan Oh

Min-hwan Oh

  * This person is not on ResearchGate, or hasn't claimed this research yet.

Image

Download file PDFRead file

Preprints and early-stage research may not have been peer reviewed yet.

## Abstract

We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number q of Newton-Schulz steps. We further analyze this constant factor and prove that it converges to 1 doubly exponentially in q and improves with the degree of the polynomial used in Newton-Schulz for approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum. Our results explain why Muon with a few low-degree Newton-Schulz steps matches exact-polar (SVD) behavior at a much faster wall-clock time and explain how much momentum matrix orthogonalization via Newton-Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.

Image: ResearchGate Logo

Discover the world's research

  * 25+ million members
  * 160+ million publication pages
  * 2.3+ billion citations
Join for free

Public Full-text 1

Available via license: CC BY-NC-ND 4.0

Content may be subject to copyright.

Published as a conference paper at ICLR 2026

C ONVERGENCE OF M UON WITH N EWTON–S CHULZ

Gyu Yeol Kim

Seoul National University

Seoul, South Korea

gyuyeolkim@snu.ac.kr

Min-hwan Oh

Seoul National University

Seoul, South Korea

minoh@snu.ac.kr
--------------------------------------------------------------------------------
Convergence of Muon with Newton-Schulz | alphaXiv (https://www.alphaxiv.org/abs/2601.19156v1)
citeturn28393search7 [wordlim: 200] Published: 8 months ago; Crawled: 4 days ago; @misc{kim2026convergencemuonnewtonschulz, title={Convergence of Muon with Newton-Schulz}, author={Gyu Yeol Kim and Min-hwan Oh}, year={2026}, eprint={2601.19156}, archivePrefix={arXiv}, primaryClass={stat.ML}, url={https://arxiv.org/abs/2601.19156}, }
## Citation

Copy

@misc{kim2026convergencemuonnewtonschulz, title={Convergence of Muon with Newton-Schulz}, author={Gyu Yeol Kim and Min-hwan Oh}, year={2026}, eprint={2601.19156}, archivePrefix={arXiv}, primaryClass={stat.ML}, url={https://arxiv.org/abs/2601.19156}, }--------------------------------------------------------------------------------
Newton-Schulzによるミューオンの収束〖JST機械翻訳〗 | 文献情報 | J-GLOBAL 科学技術総合リンクセンター (https://jglobal.jst.go.jp/detail?JGLOBAL_ID=202602210224056719)
citeturn28393search8 [wordlim: 200] Published: 8 months ago; Crawled: last month; Convergence of Muon with Newton-Schulz ... Kim Gyu Yeol

# Newton-Schulzによるミューオンの収束〖JST機械翻訳〗

Convergence of Muon with Newton-Schulz

  * 出版者サイト {{ this.onShowPLink() }} 複写サービスで全文入手
  * このテーマを更に深掘りする（JDreamⅢへ）

この文献はプレプリントです。プレプリントについてはこちらをご確認ください。

arXiv掲載論文の撤回有無については、一次情報をご確認下さい。

著者 (2件)：

Kim Gyu Yeol

Kim Gyu Yeol について

  * 名寄せID(JGPN) 202650001286264347 ですべてを検索
  * 「Kim Gyu Yeol」ですべてを検索

, 

Oh Min-hwan

Oh Min-hwan について

  * 名寄せID(JGPN) 202650001286898257 ですべてを検索
  * 「Oh Min-hwan」ですべてを検索

資料名：

arXiv

arXiv について

  * JST資料番号 O7000B ですべてを検索

発行年： 2026年01月27日  プレプリントサーバーでの情報更新日： 2026年01月28日
JST資料番号： O7000B  資料種別： プレプリント
--------------------------------------------------------------------------------
130019 PDFs | Review articles in MESONS (https://www.researchgate.net/topic/Mesons~Orthogonalization/publications)
citeturn28393search9 [wordlim: 200] Crawled: 5 months ago; Convergence of Muon with Newton-Schulz ...   * Gyu Yeol Kim ... We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps.
Cite

Download full-text

Convergence of Muon with Newton-Schulz

Preprint

Full-text available

  * Jan 2026

  * Gyu Yeol Kim
  * Min-hwan Oh

We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up...

Cite

Download full-text

Variance-Adaptive Muon: Accelerating LLM Pretraining with NSR-Modulated and Variance-Scaled Momentum

Preprint

Full-text available

  * Jan 2026

  * Jingru Li
  * Yibo Fan
  * Huan Li

Large Language Models (LLMs) achieve competitive performance across diverse natural language processing (NLP) tasks, yet pretraining is computationally demanding, making optimizer efficiency an important practical consideration. Muon accelerates LLM pretraining via orthogonal momentum updates that serve as a matrix analogue of the element-wise sign...

Cite

Download full-text

NullEightfoldWay Preprintrr

Preprint

Full-text available

  * Jan 2026

  * Garret Eugene Sobczyk
  * A I Gemini

Is the Standard Model of Physics purely geometric? In this preprint, we demonstrate that the SU(3) symmetry of quarks and the "Eightfold Way" are not abstract impositions of group theory, but inevitable consequences of a real Null Simplex geometry. By applying the Recursive Orthogonalization Theorem (derived in our companion paper), we show: • Mes...

Cite

Download full-text

Distribution Functions of Radially Excited Pion using the Light-Front Quark Model

Preprint

Full-text available

  * Jan 2026

  * Ashutosh Dwibedi
  * Satyajit Puhan
  * Sabyasachi Ghosh
  * Harleen Dahiya

--------------------------------------------------------------------------------
Top arXiv papers (https://scirate.com/?date=2026-02-04&page=175&range=31)
citeturn28393search10 [wordlim: 200] Crawled: 2 weeks ago;   * Convergence of Muon with Newton-Schulz ... @misc{2601.19156, author = {Gyu Yeol Kim and Min-hwan Oh}, title = {{C}onvergence of {M}uon with {N}ewton-{S}chulz}, year = {2026}, eprint = {2601.19156}, note = {arXiv:2601.19156v1} }[Button: Copy Citation]

  * Convergence of Muon with Newton-Schulz

Gyu Yeol Kim, Min-hwan Oh

Jan 28 2026 stat.ML cs.LG math.OC arXiv:2601.19156v1

[Button: Scited][Button: Scite!]

0

@misc{2601.19156, author = {Gyu Yeol Kim and Min-hwan Oh}, title = {{C}onvergence of {M}uon with {N}ewton-{S}chulz}, year = {2026}, eprint = {2601.19156}, note = {arXiv:2601.19156v1} }[Button: Copy Citation]

PDF

We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number $q$ of Newton-Schulz steps. We further analyze this constant factor and prove that it converges to 1 doubly exponentially in $q$ and improves with the degree of the polynomial used in Newton-Schulz for approximating the orthogonalization direction. --------------------------------------------------------------------------------
Convergence of Muon with Newton-Schulz | Cognoska (https://cognoska.com/paper/convergence-of-muon-with-newton-schulz-914a06d1-f38c-47ca-b5f7-3f39589b8847)
citeturn28393search11 [wordlim: 200] Published: 8 months ago; Crawled: 3 months ago; Gyu Yeol Kim, Min-hwan Oh ... The problem addressed is the convergence analysis of MUON with a few NEWTON–SCHULZ steps compared to its theoretical idealization using an exact SVD-based polar factor. ... Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.

# Convergence of Muon with Newton-Schulz

Jan 27, 2026•

Gyu Yeol Kim, Min-hwan Oh

Score: 0.83

stat.MLMachine Learningmath.OC

Ask the paper a questionOpen in dashboardOpen original paper

Paper PDF

PDF preview is not supported reliably on mobile browsers.

Open PDF

Problem

The problem addressed is the convergence analysis of MUON with a few NEWTON–SCHULZ steps compared to its theoretical idealization using an exact SVD-based polar factor. The goal is to understand how well this practical approximation converges and what factors influence the rate of convergence.

Approach

The method involves analyzing the convergence properties of MUON under nonconvex objectives, assuming standard smoothness conditions on the objective function. It proves that MUON with a few NEWTON–SCHULZ steps converges to a stationary point at the same rate as its idealized SVD-based polar variant, up to a constant factor.

Results

--------------------------------------------------------------------------------
Insights on Muon from Simple Quadratics (https://payshopp.net/?_=%2Fpdf%2F2602.11948%23oiIsiUa7YGXxkxUiKzZPY60%3D)
citeturn28393search16 [wordlim: 200] Published: 7 months ago; Gyu Yeol Kim and Min-hwan Oh.Convergence of Muon with Newton–Schulz. ... URL https://openreview.net/forum? ... Measure Theory, Probability, and Stochastic Processes, volume 295 of Graduate
--------------------------------------------------------------------------------
Sharp Capacity Scaling of Spectral Optimizers in Learning Associative Memory (https://shoepaly.app/?_=%2Fpdf%2F2603.26554%23hKr38k1yZITo%2FkpxGBdjJos%3D)
citeturn28393search17 [wordlim: 200] Published: 3 months ago; Functions of matrices: Theory and computation. ... [23] Gyu Yeol Kim and Min-hwan Oh.Convergence of Muon with Newton-Schulz. arXiv preprint
--------------------------------------------------------------------------------
On Convergence of Muon for Nonconvex Stochastic Optimization (https://d197for5662m48.cloudfront.net/documents/publicationstatus/309557/preprint_pdf/8c72b70bbbe2b66447660f6bfed5de3e.pdf)
citeturn28393search18 [wordlim: 200] Published: 7 months ago; SIAM Review, 60(2):223–311, 2018. ... Kim and M.-h. ... Convergence of muon with newton-schulz.


Verifying your browser | OpenReview (https://openreview.net/forum?id=lJSfxtLpLm)
citeturn28394view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://openreview.net/forum?id=lJSfxtLpLm","lineno":null}); Redirected to URL: https://openreview.net/challenge?redirect=/forum?id%3DlJSfxtLpLm; Total lines: 9
L0: # Verifying your browser
L1: 
L2: ## Complete the check below to continue to OpenReview
L3: 
L4: Please complete the verification above.
L5: 
L6: Have an OpenReview account? cite0†Sign in to skip this check.
L7: 
L8: cite1†OpenReview — Open Peer Review. Open Publishing. Open Access.
--------------------------------------------------------------------------------
Internal Error ()
citeturn28394view1 [wordlim: 200] Source: open({"ref_id":"https://api2.openreview.net/notes?id=lJSfxtLpLm","lineno":null}); Total lines: 1
L0: URL https://api2.openreview.net/notes?id=lJSfxtLpLm is not accessible via this tool.

