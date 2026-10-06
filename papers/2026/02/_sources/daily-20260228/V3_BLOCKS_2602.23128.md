[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Bound to Disagree: Generalization Bounds via Certifiable Surrogates

[3] h6: Abstract

[4] p: Generalization bounds for deep learning models are typically vacuous, not computable or restricted to specific model classes. In this paper, we tackle these issues by providing new disagreement-based certificates for the gap between the true risk of any two predictors. We then bound the true risk of the predictor of interest via a surrogate model that enjoys tight generalization guarantees, and evaluating our disagreement bound on an unlabeled dataset. We empirically demonstrate the tightness of the obtained certificates and showcase the versatility of the approach by training surrogate models leveraging three different frameworks: sample compression, model compression and PAC-Bayes theory. Importantly, such guarantees are achieved without modifying the target model, nor adapting the training procedure to the generalization framework.

[5] h2: 1 INTRODUCTION

[6] p: Deep neural networks have been the stars of the machine learning field for the last decade. Their empirical performance challenges the once-common wisdom that over-parameterized models should overfit the training data [ Zhang et al., 2017 , Zhang et al., 2021 ] . This gap between practice and theory calls for refined theoretical frameworks for studying generalization. The community has mainly turned to statistical learning theory to understand this phenomenon, producing generalization bounds based on the VC dimension [ Vapnik and Chervonenkis, 1971 ] , the Rademacher and Gaussian complexities [ Bartlett and Mendelson, 2002 , Pinto et al., 2025 , e.g.,] , information theory [ Hellström et al., 2025 , e.g.,] , PAC-Bayes theory [ McAllester, 1998 ] , sample compression theory [ Littlestone and Warmuth, 1986 ] and model compression theory [ Zhou et al., 2019 , e.g.,] . Despite this breadth of approaches, progress has remained limited: most bounds are vacuous when applied to medium-to-large neural networks or apply only to a modified version of the model rather than the original predictor.

[7] figure: Figure 1 : Generalization bounds. Comparison between bounds from the literature (Norm-based and Partition-based) and our new disagreement-based bounds, using surrogates from sample compression (SC), model compression (MC) and PAC-Bayes (PB) theory.

[8] p: A recent line of work sidesteps these issues by leveraging a simpler surrogate model with similar behavior to the network of interest. The strategy is then to bound the true risk of the original model through its link with the surrogate. In particular, Suzuki et al. [2020] and Hsu et al. [2021] leverage a smaller compressed neural network as surrogate models, and derive generalization bounds either based on distillation or on the Minkowski difference between the two models. However, both results depend on universal constants that cannot be computed. In contrast, Dziugaite and Roy [2025] provides PAC-Bayes generalization bounds by pruning neural networks and finding a “teacher” model of smaller size with small risk within them. While the resulting bounds are computable, this approach is restricted to neural networks with gated activations and residual connections, limiting its applicability.

[9] p: In this paper, we present a framework that fulfills all desiderata simultaneously: we provide fully computable, non-vacuous bounds that hold with high probability and apply to any predictor, with no restrictions on architecture, activation functions, training objective, or optimizer (see Table 1 for an overview of desiderata fulfilled by each framework). Like prior work, we leverage a surrogate model that is simple enough to enjoy tight generalization guarantees on its own, while remaining close enough to the target network that their predictions align on most inputs. The performance gap between the two models is measured through a disagreement bound, which we evaluate on a small unlabeled dataset not used during training, the only additional requirement of our approach. In comparison to labeled data, acquiring unlabeled data is much cheaper and faster to obtain [ Liao et al., 2021 ] , making this requirement much less stringent than labeled data.

[10] p: Our key theoretical contributions are reported in Section 3 , where we present a sketch of our disagreement bound, and before specializing this result to the zero-one loss and to Lipschitz-continuous losses. We further provide generalization certificates for the case where the disagreement term is optimized on the available data (e.g., via model distillation). The resulting certificates are much stronger than the other bounds in the literature that are computable and that hold for the target model without modification, as illustrated in Fig. 1 . Unlike Hsu et al. [2021] and Suzuki et al. [2020] , our guarantees can be derived for virtually any proxy model. We showcase this versatility in Section 4 , where we apply three different approaches (sample compression, model compression, and PAC-Bayes theory) to train and certify the proxy model, and study various families of neural networks: a CNN on MNIST [ LeCun et al., 1998 ] , a ResNet18 [ He et al., 2016 ] on CIFAR10 [ Krizhevsky et al., 2009 ] , and a DistilBERT [ Sanh et al., 2019 ] and a GPT2 [ Radford et al., 2019 ] on Amazon polarity [ Zhang et al., 2015 ] .

[11] figure: Table 1 : Certification frameworks comparison. We seek deep neural network bounds that are computable, non-vacuous, and do not require assumptions about the target model. The last column shows whether an additional dataset beyond the train set is required (and should it be labeled or unlabeled). Computable Non-vacuous No assumptions No additional data PAC-Bayes ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} ✓ \boldsymbol{\checkmark} Sample Compression ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} ✓ \boldsymbol{\checkmark} Model Compression ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} ✓ \boldsymbol{\checkmark} VC dimension × \boldsymbol{\times} × \boldsymbol{\times} ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} Information-theoretic ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} × \boldsymbol{\times} (need labeled data) Norm-based ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} Partition-based ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} Our bound ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} ✓ \boldsymbol{\checkmark} × \boldsymbol{\times} (need unlabeled data)

[12] h2: 2 BACKGROUND AND NOTATION

[13] p: Let ( 𝒙 1 , y 1 ) , … , ( 𝒙 n , y n ) (\boldsymbol{x}_{1},y_{1}),\ldots,(\boldsymbol{x}_{n},y_{n}) be a sequence of n n independently and identically distributed ( i.i.d. ) datapoints sampled from an unknown distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY . Let S = { ( 𝒙 i , y i ) } i = 1 n S=\{(\boldsymbol{x}_{i},y_{i})\}_{i=1}^{n} be the dataset that contains these datapoints. In this paper, we consider a feature space 𝒳 ⊆ ℝ d \calX\subseteq\R^{d} and a label space 𝒴 = { 1 , 2 , … , C } \calY=\{1,2,\ldots,C\} for C C -class classification tasks.

[14] p: The hypothesis class ℋ \calH contains predictors h : 𝒳 → ℝ C h:\calX\to\R^{C} with h ⁡ ( 𝒙 ) = ( h ​ ( 𝒙 ) 1 , … , h ​ ( 𝒙 ) C ) h(\boldsymbol{x})=(h(\boldsymbol{x})_{1},\ldots,h(\boldsymbol{x})_{C}) . A learning algorithm A : ⋃ k = 1 ∞ ( 𝒳 × 𝒴 ) k → ℋ A:\bigcup_{k=1}^{\infty}(\calX\times\calY)^{k}\to\calH outputs a predictor A ⁡ ( S ) ∈ ℋ A(S)\in\calH when applied to S S . Let ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] denote a loss function with a range λ ℓ = T ℓ − B ℓ \lambda_{\ell}=T_{\ell}-B_{\ell} . Given a loss function ℓ \ell , the true loss of a predictor h h is

[15] table: ℒ 𝒟 ⁡ ( h ) = 𝔼 ( 𝐱 , y ) ∼ 𝒟 ℓ ​ ( h ⁡ ( 𝐱 ) , y ) . \calL_{\calD}(h)=\E_{(\boldsymbol{x},y)\sim\calD}\ell(h(\boldsymbol{x}),y).

[16] p: The true loss cannot be computed, as 𝒟 \calD is unknown, while, given a dataset S ∼ 𝒟 n S{\,\sim}\calD^{n} , the empirical loss of a predictor is defined as ℒ ^ S ⁡ ( h ) = 1 n ​ ∑ i = 1 n ℓ ⁡ ( h ⁡ ( 𝐱 i ) , y i ) . \hatL_{S}(h)=\frac{1}{n}\sum_{i=1}^{n}\ell(h(\boldsymbol{x}_{i}),y_{i}).

[17] p: In this paper, we are mainly interested in two loss functions: the zero-one loss ℓ 0 ​ - ​ 1 \ell^{0\textrm{-}1} and the cross-entropy loss ℓ x-e \ell^{\textrm{x-e}} . Given a predictor h h and a pair ( 𝒙 , y ) (\boldsymbol{x},y) , the zero-one loss is defined as ℓ 0 ​ - ​ 1 ( h ( 𝒙 ) , y ) = 𝕀 [ argmax j h ( 𝐱 ) j ≠ y ] \ell^{0\textrm{-}1}(h(\boldsymbol{x}),y)=\indicator[\argmax_{j}h(\boldsymbol{x})_{j}\neq y] , where the indicator function 𝕀 ⁡ [ a ] \indicator[a] takes the value of 1 1 if the predicate a a is true and 0 0 otherwise. This loss has its own notation for the true risk and empirical risk, respectively denoted R 𝒟 ​ ( h ) R_{\calD}(h) and R ^ S ​ ( h ) \widehat{R}_{S}(h) .

[18] p: The cross-entropy loss is widely used to train neural networks and has recently become an object of interest in statistical learning theory [ Pérez-Ortiz et al., 2021 , Lotfi et al., 2024 , e.g.,] . The cross-entropy loss is defined as ℓ x-e ​ ( h ⁡ ( 𝒙 ) , y ) = − ln ⁡ ( σ ⁡ ( h ⁡ ( 𝒙 ) , y ) ) \ell^{\textrm{x-e}}(h(\boldsymbol{x}),y)=-\ln\left(\sigma(h(\boldsymbol{x}),y)\right) with the softmax function

[19] table: σ ⁡ ( h ⁡ ( 𝒙 ) , y ) = exp ⁡ ( h ​ ( 𝒙 ) y ) ∑ c = 1 C exp ⁡ ( h ​ ( 𝒙 ) c ) . \sigma(h(\boldsymbol{x}),y)=\tfrac{\exp\left(h(\boldsymbol{x})_{y}\right)}{\sum_{c=1}^{C}\exp\left(h(\boldsymbol{x})_{c}\right)}.

[20] p: We denote 𝝈 ⁡ ( f ⁡ ( 𝒙 ) ) = ( σ ⁡ ( f ⁡ ( 𝒙 ) , 1 ) , … , σ ⁡ ( f ⁡ ( 𝒙 ) , C ) ) \boldsymbol{\sigma}(f(\boldsymbol{x}))=\left(\sigma(f(\boldsymbol{x}),1),\ldots,\sigma(f(\boldsymbol{x}),C)\right) the softmax vector. By forcing the softmax to always be greater than some positive constant, it is possible to bound the cross-entropy loss, which otherwise tends to infinity when the softmax tends to zero. To do so, we consider the clamped softmax of Pérez-Ortiz et al. [2021] (see Definition S1 ) and the smoothed softmax of Lotfi et al. [2024] (see Definition S2 ).

[21] p: We now review the frameworks we leverage to derive the results in Section 3 or experiment with in Section 4 .

[22] h3: 2.1 Sample compression theory

[23] p: Introduced by Littlestone and Warmuth [1986] , sample compression theory provides generalization guarantees for data-dependent predictors that can be fully described by a small subset of the training data. Intuitively, if a model’s parameters depend on only a few training points, the model is unlikely to have overfit, and sample compression theory formalizes this intuition by providing an upper bound of the true risk of the model. Some examples of algorithms compatible with the sample compression framework include the support vector machine [ Boser et al., 1992 ] , the perceptron [ Rosenblatt, 1958 , Moran et al., 2020 ] , the decision tree [ Shah, 2007 ] , the set covering machine [ Marchand and Shawe-Taylor, 2002 , Marchand et al., 2003 , Marchand and Sokolova, 2005 , Laviolette et al., 2005 ] and Pick-To-Learn [ Paccagnan et al., 2024 , Marks and Paccagnan, 2025 , Paccagnan et al., 2025 ] . The latter was shown to be very effective at deriving tight deep learning bounds [ Bazinet et al., 2025 , Comeau et al., 2025 ] .

[24] p: We denote the compression set S 𝐢 = { ( 𝒙 i , y i ) } i ∈ 𝐢 S_{\bfi}=\{(\boldsymbol{x}_{i},y_{i})\}_{i\in\bfi} , which is defined using a strictly increasing sequence of | 𝐢 | \m indices 𝐢 = ( i 1 , … , i | 𝐢 | ) \bfi=(i_{1},\ldots,i_{\m}) . All sequences 𝐢 \bfi belong to 𝒫 ⁡ ( n ) \scriptP(n) , the set of all the 2 n 2^{n} strictly increasing sequences composed of the numbers 1 1 through n n . We denote the complement set S 𝐢 c = S ∖ S 𝐢 S_{\bfi^{c}}=S\setminus S_{\bfi} with | 𝐢 c | = n − | 𝐢 | |\mathbf{i}^{c}|=n-\m . The subset of sample-compressed predictors is denoted ℋ S ⊆ ℋ \calH_{S}\subseteq\calH . A predictor h = A ⁡ ( S ) h=A(S) is called sample-compressed if there exists a function ℛ : ⋃ m ≤ n ( 𝒳 × 𝒴 ) m → ℋ S \scriptR:\bigcup_{m\leq n}(\calX\times\calY)^{m}\to\calH_{S} and a sequence 𝐢 ∈ 𝒫 ⁡ ( n ) \bfi\in\scriptP(n) such that ℛ ⁡ ( S 𝐢 ) \scriptR(S_{\bfi}) would return the same predictor as the original algorithm ( A ⁡ ( S ) = ℛ ⁡ ( S 𝐢 ) A(S)=\scriptR(S_{\bfi}) ). For any such predictor, the sample-compression bound of Bazinet et al. [2025] can be used to upper bound the true risk of the predictor.

[25] h6: Theorem 1 ( Bazinet et al. [2025] ) .

[26] p: For a distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , a loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] and δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , simultaneously for all compression sets 𝐢 ∈ 𝒫 ⁡ ( n ) \bfi\in\scriptP(n) , we have

[27] table: ℒ 𝒟 ​ ( ℛ ⁡ ( S 𝐢 ) ) ≤ ℒ ^ S 𝐢 c ⁡ ( ℛ ⁡ ( S 𝐢 ) ) + λ ℓ 2 2 ​ | 𝐢 c | ​ log ⁡ ( 2 ​ | 𝐢 c | P n ​ ( | 𝐢 | ) ​ δ ) , \displaystyle\mathcal{L}_{\calD}(\scriptR(S_{\bfi}))\leq\hatL_{S_{\bfi^{c}}}(\scriptR(S_{\bfi}))+\sqrt{\frac{\lambda_{\ell}^{2}}{2|\bfi^{c}|}\log\left(\frac{2\sqrt{|\mathbf{i}^{c}|}}{P_{n}(\m)\delta}\right)},

[28] p: with P n ​ ( | 𝐢 | ) = 6 π 2 ​ ( | 𝐢 | + 1 ) − 2 ​ ( n | 𝐢 | ) − 1 P_{n}(\m)=\tfrac{6}{\pi^{2}}(\m+1)^{-2}n\\ \smallmatrixquantity(\lx@physics@smallmatrix n \\ \m\endlx@physics@smallmatrix)^{-1} .

[29] p: This result is versatile and can be applied to any sample-compressed predictor. In practice, one needs to prove that an algorithm produces sample-compressed models in order to compute the bound. A notable example for deep neural networks is the aforementioned Pick-To-Learn algorithm. Interestingly, the coreset methods (see Moser et al. [2025] for an introduction) also fit this framework: a coreset can be viewed as the compression set in Theorem 1 to obtain generalization bounds. To the best of our knowledge, the connection between coreset methods and sample compression has never been investigated.

[30] h3: 2.2 Model compression theory

[31] p: The code length of a model is exploited by Zhou et al. [2019] to measure its complexity: if it is possible to reduce the code length of a model, by either decreasing the number of trained parameters or quantizing their weights, without performance degradation, then the model should generalize well. Following this work, Lotfi et al. [2022] propose a tight bound for model compression based on the universal prior [ Solomonoff, 1964 ] , which introduces the Kolmogorov complexity [ Kolmogorov, 1965 ] of the model into the bound. In practice, they perform subspace compression [ Li et al., 2018 ] and adaptative quantization [ Han et al., 2016 ] to minimize the complexity of the model. Finally, Lotfi et al. [2024] propose a hybrid approach between subspace compression and LoRA [ Hu et al., 2022 ] , which they call SubLoRA, and extend the generalization bound to real-valued losses, a result that we now present. Let denote l 𝒞 ​ ( h ^ ) l_{\scriptC}(\hat{h}) the code length in bits of a model h ^ \hat{h} according to a code 𝒞 \scriptC , and ℋ 𝒞 ⊆ ℋ \calH_{\scriptC}\subseteq\calH the subset of compressed predictors that can be encoded by 𝒞 \scriptC .

[32] h6: Theorem 2 ( Lotfi et al. [2024] ) .

[33] p: For a distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , a loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] and δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , simultaneously for all h ^ ∈ ℋ 𝒞 \hat{h}\in\calH_{\scriptC} , we have

[34] table: ℒ 𝒟 ​ ( h ^ ) ≤ ℒ ^ S ⁡ ( h ^ ) + λ ℓ 2 2 ​ n ​ [ l 𝒞 ​ ( h ^ ) 2 ​ log ⁡ 2 l 𝒞 ​ ( h ^ ) + log ⁡ 1 δ ] . \displaystyle\mathcal{L}_{\calD}(\hat{h})\leq\hatL_{S}(\hat{h})+\sqrt{\frac{\lambda_{\ell}^{2}}{2n}l_{\quantity[l_{\scriptC}(\hat{h})^2 \log 2^{l_{\scriptC}(\hat{h})} + \log\frac{1}{\delta} ]}(\hat{h})^{2}\log 2^{l_{\scriptC}(\hat{h})}+\log\frac{1}{\delta}}\,.

[35] h3: 2.3 PAC-Bayes theory

[36] p: While the previous sections presented inequalities bounding the true risk of a single model, the PAC-Bayes framework principally studies the true risk of stochastic predictors expressed as a distribution over multiple models. Built on the work of McAllester [1998] and Shawe-Taylor and Williamson [1997] , PAC-Bayes theory was popularized for probabilistic neural networks by Dziugaite and Roy [2018] and Pérez-Ortiz et al. [2021] . Recent developments include applications to meta-learning [ Guan and Lu, 2022 , Zakerinia et al., 2024 , Leblanc et al., 2025 , e.g.,] , deep learning generative networks [ Chérief-Abdellatif et al., 2022 , Mbacke et al., 2023a , Mbacke et al., 2023b , Mbacke and Rivasplata, 2024 , e.g.,] and large language models [ Su et al., 2024 ] .

[37] p: In this setting, one is interested in learning a distribution Q Q over the set of predictors ℋ \calH . Starting with a data-independent prior distribution P P , an algorithm A ′ A^{\prime} takes as input the dataset S S and the prior distribution P P and then outputs the posterior distribution Q = A ′ ​ ( S , P ) Q=A^{\prime}(S,\ P) . PAC-Bayes bounds control generalization by penalizing posteriors that deviate from the prior, as typically measured by the Kullback-Leibler ( KL \mathrm{KL} ) divergence: KL ( Q | | P ) = 𝔼 h ∼ Q ln Q ⁡ ( h ) P ⁡ ( h ) \mathrm{KL}(Q||P)=\E_{h\sim Q}\ln\frac{Q(h)}{P(h)} . The following PAC-Bayesian theorem was first presented by McAllester [2003] and tightened by Maurer [2004] .

[38] h6: Theorem 3 ( McAllester [2003] ) .

[39] p: For a distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , a data-independent prior distribution P P over ℋ \calH , a loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] and δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , simultaneously for all Q Q over ℋ \calH , we have

[40] table: 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) ≤ 𝔼 h ∼ Q ℒ ^ S ​ ( h ) + λ ℓ ​ KL ( Q | | P ) + log 2 ​ n δ 2 ​ n . \displaystyle\E_{h\sim Q}\!\calL_{\calD}(h)\leq\E_{h\sim Q}\!\hatL_{S}(h)+\lambda_{\ell}\sqrt{\frac{\mathrm{KL}(Q||P)+\log\frac{2\sqrt{n}}{\delta}}{2n}}.

[41] h3: 2.4 Other theoretical frameworks

[42] p: There exist several other approaches in statistical learning theory, beyond those discussed above. Notably, norm-based generalization bounds [ Bartlett et al., 2017 ] are based on the norm of the network’s weight matrices as a measure of complexity. However, these bounds are generally vacuous [ Galanti et al., 2023b ] or cannot be computed, as they either require the input space to be bounded [ Golowich et al., 2018 ] or depend on intractable universal constants [ Bartlett and Mendelson, 2002 , Lin and Zhang, 2019 , Long and Sedghi, 2020 , Wei and Ma, 2020 , Ledent et al., 2021 , Pinto et al., 2025 ] . Similarly, VC dimension bounds are intractable for deep neural networks [ Vapnik and Chervonenkis, 1971 , Bartlett et al., 1998 , Bartlett et al., 2019 ] .

[43] p: In recent years, bounds based on information theory gained interest, as the conditional mutual information framework [ Steinke and Zakynthinou, 2020 , Hellström and Durisi, 2020 ] tends to yield non-vacuous bounds for stochastic gradient descent [ Hellström and Durisi, 2022 ] . However, these bounds either hold in expectation or use a supersample of size 2 ​ n 2n , where the model is trained on a first half and the guarantee upperbounds the risk on the second half, instead of the true risk.

[44] p: Finally, Galanti et al. [2023a] use the effective depth of the neural network as complexity measure. However, their bound is in expectation and depends on multiple assumptions that are not always satisfied in practice. Than and Phan [2025] provides vacuous generalization guarantees for trained models that depend on a partition of the input space.

[45] h2: 3 Disagreement-based Bounds

[46] p: As discussed in the previous section, most bounds for deep learning are either vacuous, not computable or hold only for a restricted class of hypotheses. In this section, we present new theoretical results applicable to any machine learning model. We first formalize the general ideas underpinning our approach by stating a Bound sketch , which presents the form of our proposed disagreement-based bounds over the gap between the losses of two models, and show how this can be leveraged for three use cases. We then instantiate our general scheme to three different types of losses: the zero-one loss ( Theorem 4 ), Lipschitz-continuous losses ( Theorem 5 ) and non-Lipschitz-continuous losses ( Theorem 6 ), a weaker result which requires a labeled dataset for computing the disagreement.

[47] p: The following Bound sketch provides the general scheme of the forthcoming high-probability bounds on the gap between the true losses of two predictors. We denote U = { ( 𝒙 i , ⋅ ) } i = 1 m U=\{(\boldsymbol{x}_{i},\cdot)\}_{i=1}^{m} an unlabeled dataset sampled i.i.d. from 𝒟 \calD .

[48] p: Bound sketch . Given two predictors f , h ∈ ℋ f,h\in\calH , a loss function ℓ \ell , and a proper (to be defined) disagreement measure D U ​ ( f , h , ℓ , δ ) D_{U}(f,h;\ell,\delta) between f f and h h over a dataset U U . The proposed disagreement-based bounds are such that, with probability at least 1 − δ 1{\,-\,}\delta over the sampling of U ∼ 𝒟 m U{\,\sim\,}\calD^{m} , we have

[49] table: ℒ 𝒟 ⁡ ( f ) ≤ ℒ 𝒟 ⁡ ( h ) + D U ​ ( f , h , ℓ , δ ) . \calL_{\calD}(f)\leq\calL_{\calD}(h)+D_{U}(f,h;\ell,\delta). (1)

[50] p: From now on, we take f f to be the target model, i.e., a model that does not enjoy tight generalization bounds, either because its complexity is too large or because it doesn’t fit the required assumptions, and h h to be the surrogate model for which tight generalization bounds exist. Let us describe three use cases of the proposed disagreement-based bounds.

[51] p: Use case #1 : Certifying the target model. Let ℋ ¯ ⊆ ℋ \overline{\calH}\subseteq\calH be a class of certifiable surrogate models, such as the class of sample-compressed predictors ℋ S \calH_{S} or the class of compressed models ℋ 𝒞 \calH_{\scriptC} . Let Q Q be a distribution over ℋ ¯ \overline{\calH} . Suppose that there exists a function ϵ ⁡ ( n , δ , Q ⁡ ( h ) ) \epsilon\!\left(n,\delta,Q(h)\right) bounding the generalization gap of the proxy model h h , that is, the following bound on its true risk holds with probability 1 − δ 1-\delta over the sampling of S ∼ 𝒟 n S\sim\calD^{n} :

[52] table: ∀ h ∈ ℋ ¯ : ℒ 𝒟 ⁡ ( f ) ≤ ℒ ^ S ⁡ ( h ) + ϵ ⁡ ( n , δ , Q ⁡ ( h ) ) . \forall h\in\overline{\calH}:\calL_{\calD}(f)\leq\hatL_{S}(h)+\epsilon\!\left(n,\delta,Q(h)\right). (2)

[53] p: Then, given a chosen model h ⋆ ∈ ℋ ¯ h^{\star}\in\overline{\calH} , combining Eqs. 1 and 2 gives that, with probability at least 1 − 2 ​ δ 1-2\delta over the sampling of S ∼ 𝒟 n S\sim\calD^{n} and U ∼ 𝒟 m U\sim\calD^{m} :

[54] table: ℒ 𝒟 ⁡ ( f ) ≤ ℒ ^ S ⁡ ( h ⋆ ) + ϵ ⁡ ( n , δ , Q ⁡ ( h ⋆ ) ) + D U ​ ( f , h ⋆ , ℓ , δ ) . \calL_{\calD}(f)\leq\hatL_{S}(h^{\star})+\epsilon\!\left(n,\delta,Q(h^{\star})\right)+D_{U}\!\left(f,h^{\star};\ell,\delta\right). (3)

[55] p: Note that this type of bounds does not hold uniformly for all h ∈ ℋ ¯ h\in\overline{\calH} , but the model h ⋆ h^{\star} can be dependent on the dataset S S , notably via an optimization algorithm. Furthermore, the model f f can also depend on S S , as its complexity does not appear in the bound of Eq. 3 . When a surrogate model h ⋆ h^{\star} with tight generalization guarantees is obtainable, then this strategy renders a certificate for f f whose tightness depends on the disagreement measured by the chosen D U ​ ( f , h , ℓ , δ ) D_{U}(f,h;\ell,\delta) .

[56] p: Use case #2 : Minimizing the disagreement. The second use case of this disagreement bound is to certify the true risk of the target model whilst minimizing the disagreement between the two models. With probability at least 1 − 2 ​ δ 1-2\delta over the sampling of S ∼ 𝒟 n S\sim\calD^{n} and U ∼ 𝒟 m U\sim\calD^{m} , simultaneously for all h ∈ ℋ ¯ h\in\overline{\calH} , we have

[57] table: ℒ 𝒟 ⁡ ( f ) ≤ ℒ ^ S ⁡ ( h ) + ϵ ⁡ ( n , δ , Q ⁡ ( h ) ) + D U ​ ( f , h , ℓ , δ ​ Q ​ ( h ) ) . \calL_{\calD}(f)\leq\hatL_{S}(h)+\epsilon\!\left(n,\delta,Q(h)\right)+D_{U}\!\left(f,h;\ell,\delta Q(h)\right). (4)

[58] p: We obtain this result by applying Eq. 1 with a union bound over all h ∈ ℋ ¯ h\in\overline{\calH} , followed by a union bound with Eq. 3 . Although this added step loosens the bound in principle, it allows the surrogate model to be selected and trained on both the datasets S S and U U . One way to train the surrogate model on the unlabeled set is via model distillation [ Hinton et al., 2015 ] , using pseudo-labels produced by the target model.

[59] p: Use case #3 : Bounding the true risk gap. The final use case of this bound is to guarantee that replacing a model h h with a new model f f with better qualities does not lead to a significant performance drop. Such qualities could be that the model is fairness-aware [ Dwork et al., 2012 , Hardt et al., 2016 , e.g.,] , differentially private [ Dwork, 2006 , Dwork and Roth, 2014 , e.g.,] or achieves faster inference, either via model distillation [ Buciluǎ et al., 2006 , Hinton et al., 2015 , e.g.,] or model quantization [ Han et al., 2016 , Nagel et al., 2020 , e.g.,] . Note that bounding the risk gap can lead to useful insights even when both models are too complex to enjoy non-vacuous generalization bounds.

[60] h3: 3.1 Disagreement with the zero-one loss

[61] p: We present our first result for the zero-one loss. To do so, we build on the work of Yang et al. [2024] , who presented a theoretical result to compare the reconstruction error of a coreset. We show that this result can be upper-bounded with high probability via the test set bound of Langford [2005] (see Theorem S6 ), which is, essentially, perfectly tight for binomial distributions. With these two results, we can state a disagreement measure for the zero-one loss, which is defined as

[62] table: d U 0 ​ - ​ 1 ​ ( f , h ) = 1 m ​ ∑ i = 1 m 𝕀 ⁡ [ argmax j f ​ ( 𝐱 i ) j ≠ argmax k h ​ ( 𝐱 i ) k ] . d^{0\textrm{-}1}_{U}(f,h){\,=\,}\frac{1}{m}\sum_{i=1}^{m}\indicator\quantity[ \argmax_j f(\bx_i)_j\neq\argmax_k h(\bx_i)_k]\!.

[63] p: The disagreement measure d U 0 ​ - ​ 1 d^{0\textrm{-}1}_{U} compares the labels predicted by each model for given a datapoint. If the disagreement bound between f f and h h tends to zero, then the models achieve the same true risk. We now present our first result: a disagreement-based bound for the zero-one loss. The proof of all results are given in Appendix B .

[64] h6: Theorem 4 .

[65] p: For two predictors h ∈ ℋ ¯ h\in\overline{\calH} and f ∈ ℋ f\in\calH , with probability at least 1 − δ 1-\delta over the sampling of U ∼ 𝒟 m U\sim\calD^{m} , we have

[66] table: R 𝒟 ​ ( f ) ≤ R 𝒟 ​ ( h ) + Bin ¯ ​ ( m ​ d U 0 ​ - ​ 1 ​ ( f , h ) , m , δ ) R_{\calD}(f)\leq R_{\calD}(h)+\overline{\text{\rm Bin}}\quantity(m \dzero_U(f, h), m, \delta)

[67] p: with ​ B ​ i ​ n ¯ ( k , m , δ ) = argsup p ∈ [ 0 , 1 ] { B i n ( k , m , p ) ≥ δ } \overline{\emph{Bin}}\quantity(k,m, \delta)=\argsup_{p\in[0,1]}\{\emph{Bin}(k,m,p)\geq\delta\} and ​ B ​ i ​ n ​ ( k , m , p ) = ∑ i = 0 k ( m i ) ​ p i ​ ( 1 − p ) m − i \emph{Bin}(k,m,p)=\sum_{i=0}^{k}\smallmatrixquantity(\lx@physics@smallmatrix m \\ i\endlx@physics@smallmatrix)p^{i}(1-p)^{m-i} .

[68] p: This result provides generalization guarantees for the zero-one loss of any target model f f by training a surrogate predictor h h with tight generalization bounds and a small disagreement with f f ; In the experiments of Section 4 , we do so by bounding the true risk R 𝒟 ​ ( h ) R_{\calD}(h) of the surrogate model using sample compression and model compression guarantees.

[69] h3: 3.2 Disagreement with Lipschitz losses

[70] p: We now generalize the previous result for Lipschitz-continuous bounded losses. An intuitive measure of disagreement between two models is to compare the decision boundary of the models by comparing their output distributions :

[71] table: d U K ℓ ​ ( f , h ) = 1 m ​ ∑ i = 1 m ‖ 𝝈 ⁡ ( f ⁡ ( 𝒙 i ) ) − 𝝈 ⁡ ( h ⁡ ( 𝒙 i ) ) ‖ 1 . d_{U}^{K_{\ell}}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\|\boldsymbol{\sigma}(f(\boldsymbol{x}_{i}))-\boldsymbol{\sigma}(h(\boldsymbol{x}_{i}))\|_{1}\,.

[72] p: When this measure of disagreement tends to zero, the models predict the same class for each datapoint sampled from 𝒟 \calD , which means that the models generalize similarly. The following Theorem 5 uses the Chernoff bound for random variables in the interval unit of Foong et al. [2022] (see Theorem S7 ) in place of the zero-one loss based test set bound exploited by Theorem 4 . Furthermore, Theorem 5 provides a bound on a target predictor f f given a distribution Q Q over a class of surrogate models. This allows us to apply PAC-Bayes bounds (as Theorem 3 ) to the true risk of the target model. Still, the following disagreement-based bound for Lipschitz-continuous [ B ℓ , T ℓ ] [B_{\ell},T_{\ell}] -losses can be applied to a single surrogate model by setting Q Q to a Dirac distribution.

[73] h6: Theorem 5 .

[74] p: For a distribution Q Q over ℋ \calH , a predictor f ∈ ℋ f\in\calH , a Lipschitz loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] with range λ ℓ = T ℓ − B ℓ \lambda_{\ell}=T_{\ell}-B_{\ell} and Lipschitz constant K ℓ K_{\ell} , with probability at least 1 − δ 1-\delta over the sampling of U ∼ 𝒟 m U\sim\calD^{m} , we have

[75] table: ℒ 𝒟 ⁡ ( f ) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + 2 ​ K ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) 2 , log ⁡ 1 δ m ) \calL_{\calD}(f)\leq\E_{h\sim Q}\calL_{\calD}(h)+2K_{\ell}\mathrm{kl}^{-1}\quantity(\E_{h \sim Q} \frac{d_U^{K_{\ell}}(f,h)}{2}, \frac{\log\frac{1}{\delta}}{m})_{h\sim Q}\frac{d_{U}^{K_{\ell}}(f,h)}{2},\frac{\log\frac{1}{\delta}}{m}

[76] p: with kl − 1 ( q , ϵ ) = argsup p ∈ [ 0 , 1 ] { kl ( q , p ) ≤ ϵ } \mathrm{kl}^{-1}(q,\epsilon)=\argsup_{p\in[0,1]}\left\{\mathrm{kl}(q,p)\leq\epsilon\right\} and kl ⁡ ( q , p ) = q ​ log ⁡ q p + ( 1 − q ) ​ log ⁡ 1 − q 1 − p \mathrm{kl}(q,p)=q\log\tfrac{q}{p}+(1-q)\log\tfrac{1-q}{1-p} .

[77] p: The above result can be applied to common losses such as the logistic loss, the hinge loss and the Huber loss, which are known to be Lipschitz functions [ Chinot et al., 2018 ] . The cross-entropy loss may become Lipschitz by constraining the entries of the softmax output to be greater than a given positive constant, which is achieved with the clamped or the smoothed softmax. However, the obtained Lipschitz constant K ℓ K_{\ell} is typically large and renders non-vacuous bounds. In the following subsection, we present a weaker result that bounds the loss of a model using disagreement on a labeled dataset

[78] figure: Table 2 : Generalization bounds for the zero-one loss of the target models according to the approach (and theorem) used to certify the surrogate. The bound values are reported in % \% . Bound (Theorem) MNIST CIFAR10 Baselines Partition-based ( S4 ) 86.55 ± \pm 0.53 90.58 ± \pm 0.47 Norm-based ( S5 ) (3.14 ± \pm 0.37) × 10 8 \times 10^{8} (3.80 ± \pm 0.30) × 10 21 \times 10^{21} Our approach Random Coreset ( S8 ) 1.78 ± \pm 0.10 17.36 ± \pm 0.20 Best Coreset ( S9 ) 21.50 ± \pm 0.83 81.13 ± \pm 0.33 Pick-To-Learn ( S10 ) 3.88 ± \pm 0.07 57.13 ± \pm 2.71 Model compression ( S11 ) 3.45 ± \pm 0.11 35.06 ± \pm 0.40 PAC-Bayes ( S15 ) 4.83 ± \pm 0.32 28.13 ± \pm 1.55 Table 3 : Generalization bounds for the smoothed cross-entropy loss of the target models according to the approach (and theorem) used to certify the surrogate. Bound (Theorem) MNIST CIFAR10 Baselines Partition-based ( S4 ) 7.9546 ± \pm 0.0475 8.3437 ± \pm 0.0431 Norm-based N/A N/A Our approach Random Coreset ( S12 ) 0.0744 ± \pm 0.0026 0.6858 ± \pm 0.0089 Best Coreset ( S13 ) 0.9035 ± \pm 0.0531 5.5273 ± \pm 0.0459 Pick-To-Learn ( S13 ) 1.2671 ± \pm 0.0260 7.3531 ± \pm 0.4575 Model compression ( S14 ) 0.1756 ± \pm 0.0041 1.7851 ± \pm 0.0223 PAC-Bayes ( S15 ) 0.2592 ± \pm 0.0087 1.4204 ± \pm 0.1377

[79] h3: 3.3 Disagreement with non-Lipschitz losses

[80] p: Let L = { ( 𝒙 i , y i ) } i = 1 m ∼ 𝒟 m L=\{(\boldsymbol{x}_{i},y_{i})\}_{i=1}^{m}\sim\calD^{m} be a small held-out labeled set of datapoints removed before training f f . Then, we provide the following disagreement bound for any non-Lipschitz loss.

[81] h6: Theorem 6 .

[82] p: For a distribution Q Q over ℋ \calH , a predictor f ∈ ℋ f\in\calH , a loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] with range λ ℓ = T ℓ − B ℓ \lambda_{\ell}=T_{\ell}-B_{\ell} , with probability at least 1 − δ 1-\delta over the sampling of L ∼ 𝒟 m L\sim\calD^{m} :

[83] table: ℒ 𝒟 ⁡ ( f ) \displaystyle\calL_{\calD}(f) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + λ ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q d L ​ ( f , h ) λ ℓ , log ⁡ 1 δ m ) , \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\lambda_{\ell}\mathrm{kl}^{-1}\quantity( \E_{h \sim Q} \frac{d_L(f,h)}{\lambda_{\ell}}, \frac{\log\frac{1}{\delta}}{m})_{h\sim Q}\frac{d_{L}(f,h)}{\lambda_{\ell}},\frac{\log\frac{1}{\delta}}{m},

[84] p: with d L ​ ( f , h ) = 1 m ​ ∑ i = 1 m | ℓ ⁡ ( f ⁡ ( 𝐱 i ) , y i ) − ℓ ⁡ ( h ⁡ ( 𝐱 i ) , y i ) | . d_{L}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\left|\ell(f(\boldsymbol{x}_{i}),y_{i})-\ell(h(\boldsymbol{x}_{i}),y_{i})\right|.

[85] p: In contrast with Theorems 4 and 5 , the disagreement d L d_{L} is not a disagreement between the output of the models. However, we show in Corollary S16 that, for Lipschitz losses with large K ℓ K_{\ell} constants, d L d_{L} is a proxy for disagreement between the models, as it is upper-bounded by the disagreement between the probability distributions outputted by the models. We instantiate this result for the clamped and smoothed cross-entropy respectively in Section C.1 .

[86] p: When used with the zero-one loss, d L d_{L} is upper-bounded by d U 0 ​ - ​ 1 d^{0\textrm{-}1}_{U} , leading to a bound on the true risk of the target using PAC-Bayes theory and an unlabeled dataset U U , which wasn’t possible with the test set bound of Langford [2005] .

[87] h2: 4 EXPERIMENTS

[88] figure: (a) Zero-one loss (b) Smoothed cross-entropy loss Figure 2 : Illustration of the behavior of our disagreement bounds on MNIST using sample-compression methods.

[89] figure: Table 4 : Generalization bounds on the zero-one loss achieved on MNIST and CIFAR10 using model compression (MC) bounds. All metrics are in percents (%), except the size. Dataset Surrogate model Target model Test error Size (KB) MC Bound Test error Our bound MNIST 0.89 ± \pm 0.08 0.04 ± \pm 0.00 2.45 ± \pm 0.13 0.50 ± \pm 0.07 3.45 ± \pm 0.11 CIFAR10 14.95 ± \pm 0.42 0.03 ± \pm 0.00 20.15 ± \pm 0.35 5.84 ± \pm 0.16 35.06 ± \pm 0.40 Table 5 : Generalization bounds on the zero-one loss achieved on MNIST and CIFAR10 using PAC-Bayes (PB) bounds. All metrics presented are in percents (%), except the KL \mathrm{KL} . Dataset Surrogate model Target model Test error KL \mathrm{KL} PB Bound Test error Our bound MNIST 0.82 ± \pm 0.07 4.68 ± \pm 0.22 2.28 ± \pm 0.13 0.50 ± \pm 0.07 4.83 ± \pm 0.32 CIFAR10 11.33 ± \pm 0.55 1.62 ± \pm 0.92 14.04 ± \pm 0.91 5.84 ± \pm 0.16 28.13 ± \pm 1.55

[90] p: In this section, we demonstrate the versatility and efficacy of our framework by training and certifying a variety of deep neural networks for which tight generalization bounds were previously unavailable. 1 1 1 Our code is available at https://anonymous.4open.science/r/bound-to-disagree/ In Section 4.1 , we focus on use case #1 and leverage Theorem 4 to bound the zero-one loss and Theorem 6 to bound the cross-entropy loss of the target network, obtaining a surrogate via sample compression, model compression or PAC-Bayes training. In Section 4.2 , we illustrate use case #2 by applying Theorem 5 to the true Huber loss of the target model, while optimizing a compressed surrogate via model distillation. Finally, in Section 4.3 , we consider use case #3 and evaluate the certificate on the gap between the true risks of the target model and its quantized version.

[91] p: For all experiments, we report the mean and standard deviation over five training-evaluation runs. We randomly sample 10% of the training set to form a validation set. Of the remaining training set, we further select a disagreement set, corresponding to 20% of data for MNIST and CIFAR10, and 85% for Amazon polarity 2 2 2 15% corresponds to roughly 500000 datapoints, more than enough data to train the models on Amazon polarity. . We optimize the smoothed softmax with α = 10 − 3 \alpha=10^{-3} , following the result of an ablation study on coreset methods in Section D.4.1 . Thus, in all tables and figures, the cross-entropy loss is bounded by ln ⁡ ( 10 3 / C ) \ln(10^3/C) , which is approximately 9.21 9.21 with C = 10 C=10 . All the bounds presented hold with probability 1 − δ = 0.99 1-\delta=0.99 . Other hyperparameters are detailed in Appendix D .

[92] h3: 4.1 Certifying the target model

[93] p: For these experiments, we first train a CNN on MNIST [ LeCun et al., 1998 ] and a ResNet18 [ He et al., 2016 ] on CIFAR10 [ Krizhevsky et al., 2009 ] as target models. Because these models are deterministic, trained on the whole training set and not quantized, the only generalization bounds of the literature that we can compare with are: the partition-based bound of Than and Phan [2025] (see Theorem S4 ), and the norm-based bounds , among which we present the results of Galanti et al. [2023b] (see Theorem S5 ), which is only defined for the zero-one loss. Note that for the partition-based bound, contrary to the original paper, we compute the partition on the disagreement set, to obtain non-vacuous results. See Section D.2.1 for an ablation study on the way of computing the partition. Tables 3 and 3 report a summary of the value of our new disagreement bounds for all the experiments, where we specify the generalization framework from the literature used to certify the surrogate model. We observe that both norm-based bounds and partition-based bounds are unsuited to certify the target model both on MNIST and on CIFAR10: norm-based bounds are vacuous as cross-entropy maximises the network’s weight norms [ Galanti et al., 2023b ] , and partition-based bounds are almost trivial, as they estimate a generalization performance close to a random predictor’s one (90%). Moreover, the latter cannot differentiate between two problems of varying complexities, such as MNIST and CIFAR10.

[94] p: Sample compression In our first experiment, we use sample-compression bounds to certify the target models on MNIST and CIFAR10. To do so, we train neural networks with the same architecture as the targets using P2L [ Paccagnan et al., 2024 ] and coreset methods such as Random Coreset, k-Center Greedy [ Sener and Savarese, 2018 ] , Forgetting [ Toneva et al., 2019 ] and DeepFool [ Ducoffe and Precioso, 2018 ] .

[95] p: Fig. 2 presents the contribution of each term of the bound on MNIST for the different sample-compression methods. The results for CIFAR10 are presented in Fig. S2 in Appendix D . The complement error is added as complementary information, but the bound is not linear in the complement error. We observe that each method is able to achieve tight generalization bounds for our target models. The tightest bound is achieved by the Random Coreset approach, which is expected as it enjoys a test set bound, which means that the complexity of the random coreset is never accounted for in the bound. In comparison, the other bounds are train set bounds, meaning the coreset method must find a compromise between accuracy and coreset size. For the zero-one loss, P2L achieves the second tightest bound. For the cross-entropy loss, it actually achieves the worst bound of all methods. The complexity of the model learned using P2L is much higher than the coreset methods, however, the P2L bound ( Theorem S10 ) still achieves significantly tighter bounds. In Tables 3 and 3 , we report the bound for P2L, Random Coreset and the best (non-random) coreset method. Of all the methods presented, Random Coreset achieves the tightest disagreement bound for our target models. All of the sample compression bounds are significantly tighter than both the norm-based bound and the partition-based bound.

[96] p: Model compression. For the model compression experiments, we use the SubLoRA method of Lotfi et al. [2024] . To showcase a different approach that leads to tight certificates, we start by pretraining a CNN on 20% of the training set for MNIST and a ResNet18 on 50% of the training set for CIFAR10. We then add a low-rank adapter [ Hu et al., 2022 ] and use the subspace compression method [ Li et al., 2018 ] implemented by Lotfi et al. [2022] on the adapter. After training the adapter on the remaining training data, the subspace vector is quantized using adaptative quantization [ Han et al., 2016 ] and encoded using arithmetic encoding [ Rissanen and Langdon, 1979 ] . The bound on the surrogate’s loss is computed over the set on which the adapter was trained.

[97] p: In Table 5 , we report the bound on the zero-one loss for the SubLoRA approach on MNIST and CIFAR10. We report the bound on the cross-entropy loss in Table S2 . On MNIST, the model compression bounds are the second tightest bounds reported in Table 3 , whilst they are the third tightest bounds for CIFAR10. It was expected that these bounds would be much tighter than the sample-compression bounds, as pretraining the the models tightens significantly the results [ Ambroladze et al., 2006 , Parrado-Hernández et al., 2012 , Dziugaite and Roy, 2018 ] . However, we note that even after an extensive hyperparameter search on CIFAR10, the bound favors a smaller subspace vector, where the model only marginally improves after the pretraining, if at all.

[98] p: PAC-Bayes. For the PAC-Bayes experiments, we train stochastic neural networks with the implementation of Pérez-Ortiz et al. [2021] . We start by pretraining a deterministic neural network, either a CNN on 20% of the training set for MNIST or a ResNet18 on 60% or 70% on the training set of CIFAR10. We then add Gaussian distributions over the weights of the neural network, with the mean and the standard deviation of the distributions as trainable parameters. To compute the bound of Theorem S15 , we approximate the expectation via Monte Carlo sampling. The full statement of the disagreement loss with the Monte Carlo sampling is presented in Theorem S20 .

[99] p: In Table 5 , we report the bound on the zero-one loss for the stochastic neural network on MNIST and CIFAR10. The results on the cross-entropy loss are reported in Table S3 . As the model were pretrained, they achieve small test errors even with a small KL \mathrm{KL} divergence, similarly to the model compression bound. In contrast with the previous approaches, the disagreement bounds are actually larger than the compressed model bounds. The approximation via the Monte Carlo sampling and the variance in the stochastic predictor leads to a larger disagreement between the model and its surrogate. However, this approach provides tight generalization bounds and achieves the second best disagreement bound on CIFAR10.

[100] h3: 4.2 Minimizing the disagreement

[101] p: For the second use case of our disagreement bounds, we provide model distillation experiments on Amazon polarity dataset [ Zhang et al., 2015 ] . Our target models are a DistilBERT [ Sanh et al., 2019 ] and a GPT2 [ Radford et al., 2019 ] . Using the target models, we create pseudo-labels for the unlabeled disagreement set and train the surrogate models on both the labeled set S S and the unlabeled set U U . We freeze the pretrained weights of the model (from the Transformers library [ Wolf et al., 2020 ] ) and add SubLoRA weights [ Lotfi et al., 2024 ] on the top half of the model. As the model is trained on both datasets, the bound holds simultaneously for all possible models, following Eq. 4 . We use the Huber loss (see Definition S3 ) with δ H = 0.2 \delta_{\textrm{H}}=0.2 to compute Theorem 5 , which means that we can train the model with vanilla softmax.

[102] p: We present the results for the Huber loss in Table 6 , where both models achieved non-vacuous generalization bounds. The DistilBERT surrogate achieved a test loss very similar to the one of the target model, while the GPT2 surrogate’s loss is much higher. This could be explained by the fact that the model is twice as big, although the SubLoRA adapter that achieved the best disagreement bound is the same size (in KB) as the one of DistilBERT. Although the bound is only available for the Huber loss instead of the cross-entropy loss, the model’s softmax doesn’t have to be modified, the dataset does not need to be labeled and the bound minimizes the actual disagreement between the two models. We report the results for the zero-one loss in Table S4 . For both architectures, we are able to provide non-vacuous and non-trivial (less than 50% for binary classification) generalization bounds for the target models.

[103] figure: Table 6 : Generalization bounds on the Huber loss via model distillation on Amazon polarity using model compression bounds. With δ H = 0.2 \delta_{\textrm{H}}\,{=}\,0.2 , the loss is less than δ H − 1 2 ​ δ H 2 = 0.18 \delta_{\textrm{H}}-\tfrac{1}{2}\delta_{\textrm{H}}^{2}{\,=\,}0.18 . Dataset Surrogate model Target model Test loss Size (KB) MC Bound Test loss Our bound DistilBERT .015 ± \pm .000 2.02 ± \pm 0.01 .027 ± \pm .000 .012 ± \pm .000 .059 ± \pm .001 GPT2 .035 ± \pm .004 2.04 ± \pm 0.43 .052 ± \pm .004 .010 ± \pm .000 .152 ± \pm .015

[104] h3: 4.3 Bounding the true risk gap

[105] figure: (a) DistilBERT (b) GPT2 Figure 3 : Behavior of the disagreement bound according to the number of bits and the use of quantization-aware training.

[106] p: To demonstrate our third use case, we provide quantization experiments on Amazon polarity, with the same target models as the previous section. We quantize the models and compare their disagreement with the unquantized target models. Even after quantization, in contrast to the previous sections, the surrogates are still too large to enjoy non-vacuous model compression bounds. We can use our disagreement bounds to provide an upper bound on the gap between the true risk of two models. This will guarantee that although the model is quantized, the models will perform similarly on unseen datapoints. We present results for models with and without quantization-aware (QA) training. For QA training, we quantize to 4 bits using TorchAO [ Or et al., ] and 8 bits using AO from PyTorch [ Ansel et al., 2024 ] . For the other experiments, we use half-quadratic quantization (HQQ) [ Badri and Shaji, 2023 ] to quantize the models.

[107] p: We report the results in Fig. 3 . Without a surprise, fully quantizing a model to 2 bits leads to large performance loss. The tightest disagreement bounds were obtained by using 8 bits with HQQ for both models. The QA training with 4 bits achieves a better test error for both models than 8 bit training, leading however the DistilBERT model to overfit on the training set. For both DistilBERT and GPT2, respectively without and with quantization-aware training, the 4-bits models are able to achieve disagreement bound of about 2%, whilst achieving faster inference and using less memory.

[108] h2: 5 CONCLUSION

[109] p: We proposed new disagreement-based bounds that can be leveraged for any machine learning predictor. These bounds require no assumptions about the model’s architecture or the training method. We showed that these bounds can be used with multiple statistical learning theory frameworks to obtain tight generalization bounds, by experimenting on small datasets such as MNIST and CIFAR10, as well as on a larger dataset such as Amazon polarity.

[110] p: Despite achieving eloquent improvement over existing bounds in many contexts, our proposed framework also has limitations that deserve to be addressed in future work. Notably, the disagreement-based bounds are only as good as the guarantees used to certify the surrogate models, and finding a surrogate for a very complex model can be challenging. Also, the tightest bounds are obtained without minimizing the disagreement on the unlabeled set, meaning we do not control the disagreement between the target and the surrogate. In particular, the random coreset approach provides little control over the resulting bound, yet yields the tightest bounds of all the approaches.

[111] h2: References

[112] p: Bound to Disagree: Generalization Bounds via Certifiable Surrogates (Supplementary Materials)

[113] h2: Appendix A DEFINITIONS AND THEORETICAL RESULTS FROM THE LITERATURE

[114] h6: Definition S1 ( Pérez-Ortiz et al. [2021] ) .

[115] p: Given a parameter α ∈ ( 0 , 1 ) \alpha\in(0,1) and a number of classes C C , the clamped softmax is defined as

[116] table: σ max ​ ( h ⁡ ( 𝒙 ) , y ) = max ⁡ ( α C , exp ⁡ ( h ​ ( 𝒙 ) y ) ∑ c = 1 C exp ⁡ ( h ​ ( 𝒙 ) c ) ) , \sigma_{\max}(h(\boldsymbol{x}),y)=\max\left(\frac{\alpha}{C},\frac{\exp\left(h(\boldsymbol{x})_{y}\right)}{\sum_{c=1}^{C}\exp(h(\bx)_c)}\right),

[117] p: and the cross-entropy loss is bounded with B ℓ = 0 B_{\ell}=0 , T ℓ = ln ⁡ C α T_{\ell}=\ln\frac{C}{\alpha} and λ ℓ = ln ⁡ C α \lambda_{\ell}=\ln\frac{C}{\alpha} .

[118] h6: Definition S2 ( Lotfi et al. [2024] ) .

[119] p: Given a parameter α ∈ ( 0 , 1 ) \alpha\in(0,1) and a number of classes C C , the smoothed softmax is defined as

[120] table: σ ​ s ​ m ​ o ​ o ​ t ​ h ​ ( h ⁡ ( 𝒙 ) , y ) = ( 1 − α ) ​ ( exp ⁡ ( h ​ ( 𝒙 ) y ) ∑ c = 1 C exp ⁡ ( h ​ ( 𝒙 ) c ) ) + α C , \sigma_{\emph{smooth}}(h(\boldsymbol{x}),y)=(1-\alpha)\left(\frac{\exp\left(h(\boldsymbol{x})_{y}\right)}{\sum_{c=1}^{C}\exp(h(\bx)_c)}\right)+\frac{\alpha}{C}\,,

[121] p: and the cross-entropy loss bounded with B ℓ = ln ⁡ ( 1 − α + α C ) B_{\ell}=\ln\left(1-\alpha+\frac{\alpha}{C}\right) , T ℓ = ln ⁡ C α T_{\ell}=\ln\frac{C}{\alpha} and λ ℓ = ln ⁡ ( 1 + ( 1 − α ) ​ C α ) \lambda_{\ell}=\ln\left(1+(1-\alpha)\frac{C}{\alpha}\right) .

[122] h6: Definition S3 .

[123] p: Given h : 𝒳 → ℝ C h:\calX\to\R^{C} , y ∈ ℝ C y\in\R^{C} and δ H > 0 \delta_{\textrm{H}}>0 , the Huber loss is defined as

[124] table: ℓ Huber ​ ( h ⁡ ( 𝒙 ) , y ) = 1 C ​ ∑ i = 1 C { 1 2 ​ ( σ ⁡ ( h ′ ​ ( 𝒙 ) , i ) − y i ) 2 if ​ | σ ⁡ ( h ′ ​ ( 𝒙 ) , i ) − y i | ≤ δ H δ H ​ | σ ⁡ ( h ′ ​ ( 𝒙 ) , i ) − y i | − 1 2 ​ δ H 2 otherwise. \displaystyle\ell^{\mathrm{Huber}}(h(\boldsymbol{x}),y)=\frac{1}{C}\sum_{i=1}^{C}\begin{cases}\frac{1}{2}(\sigma(h^{\prime}(\boldsymbol{x}),i)-y_{i})^{2}&\text{ if }|\sigma(h^{\prime}(\boldsymbol{x}),i)-y_{i}|\leq\delta_{\textrm{H}}\\ \delta_{\textrm{H}}|\sigma(h^{\prime}(\boldsymbol{x}),i)-y_{i}|-\frac{1}{2}\delta^{2}_{\textrm{H}}&\text{ otherwise.}\end{cases} (5)

[125] p: As we apply a softmax over the output of the predictor, this loss is bounded by δ H − 1 2 ​ δ H 2 \delta_{\textrm{H}}-\frac{1}{2}\delta^{2}_{\textrm{H}} . This loss is Lipschitz-continuous with K ℓ = δ H K^{\ell}=\delta_{\textrm{H}} [ Chinot et al., 2018 ] .

[126] h6: Theorem S4 (Partition-based bound of Than and Phan [2025] ) .

[127] p: Let 𝒵 = 𝒳 × 𝒴 {\mathcal{Z}}=\calX\times\calY and let Γ ⁡ ( 𝒵 ) = ⋃ i = 1 K 𝒵 i \Gamma({\mathcal{Z}})=\bigcup_{i=1}^{K}{\mathcal{Z}}_{i} be a partition of 𝒵 {\mathcal{Z}} into K K subsets. Let n i = | S ∩ 𝒵 i | n_{i}=|S\cap{\mathcal{Z}}_{i}| be the number of samples of a dataset S S grouped into 𝒵 i {\mathcal{Z}}_{i} . Let 𝒯 = ∑ i = 1 k 𝕀 [ n i ≠ 0 ] {\mathcal{T}}=\sum_{i=1}^{k}\indicator[n_{i}\neq 0] be the number of subsets of Γ ⁡ ( 𝒵 ) \Gamma({\mathcal{Z}}) in which datapoints from S S fall into. For any partition Γ \Gamma into K K subsets, for any loss ℓ : ℝ C × 𝒴 → [ 0 , T ℓ ] \ell:\R^{C}\times\calY\to[0,T_{\ell}] , for any constants γ ≥ 1 \gamma\geq 1 and α ∈ [ 0 , γ ​ n ​ ( K + γ ​ n ) K ⁡ ( 4 ​ n − 3 ) ] \alpha\in\left[0,\frac{\gamma n(K+\gamma n)}{K(4n-3)}\right] , with probability at least 1 − γ − α − δ 1-\gamma^{-\alpha}-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , for a given model h S h_{S} trained on S S , we have

[128] table: ℒ 𝒟 ⁡ ( h S ) ≤ ℒ ^ S ⁡ ( h S ) \displaystyle\calL_{\calD}(h_{S})\leq\hatL_{S}(h_{S}) + T ℓ ​ α ​ ln ⁡ γ ​ γ 2 ​ n + γ 2 2 ​ ∑ i = 1 K ( n i n ) 2 + γ 2 ​ 2 n ​ ln ⁡ 2 ​ K δ + T ℓ ​ ( 2 + 1 ) ​ 𝒯 ​ ln ⁡ 4 ​ K δ n + 2 ​ T ℓ ​ 𝒯 ​ ln ⁡ 4 ​ K δ n . \displaystyle+T_{\ell}\sqrt{\alpha\ln\gamma}\sqrt{\frac{\gamma}{2n}+\frac{\gamma^{2}}{2}\sum_{i=1}^{K}\left(\frac{n_{i}}{n}\right)^{2}+\gamma^{2}\sqrt{\frac{2}{n}\ln\frac{2K}{\delta}}}+T_{\ell}(\sqrt{2}+1)\sqrt{\frac{{\mathcal{T}}\ln\frac{4K}{\delta}}{n}}+\frac{2T_{\ell}{\mathcal{T}}\ln\frac{4K}{\delta}}{n}.

[129] h6: Theorem S5 (Norm-based bound of Galanti et al. [2023b] ) .

[130] p: Given a fixed neural network architecture G G that defines a directed acyclic graph. Let the architecture have L L layers and d l d_{l} neurons at each layer l ∈ { 1 , … , L } l\in\{1,\ldots,L\} . Denote z i l z_{i}^{l} is the i-th neuron of the l-th layer. Let z i l − 1 z_{i}^{l-1} be a predecessor of the neuron z j l z_{j}^{l} if there exists an edge between the two neurons and denote p ​ r ​ e ​ d ​ ( l , j ) pred(l,j) the set of predecessors of the neuron z j l z_{j}^{l} . Let ℋ G \calH_{G} be the class of neural networks with architecture G G . Denote ρ ⁡ ( h ) \rho(h) the norm of the model h ∈ ℋ G h\in\calH_{G} . Given images with c 0 c_{0} channels and d 0 d_{0} values such that the images are in ℝ c 0 ​ d 0 \R^{c_{0}d_{0}} and labels in 𝒴 ⊂ ℝ C \calY\subset\R^{C} the set of C C -dimensional one-hot vectors. Let z j 0 ​ ( x ) z_{j}^{0}(x) be the j t ​ h j^{th} pixel of the image. For any distribution 𝒟 \calD over ℝ c 0 ​ d 0 × { − 1 , + 1 } \R^{c_{0}d_{0}}\times\{-1,+1\} , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[131] table: ∀ h ∈ ℋ G : R 𝒟 ​ ( h ) \displaystyle\forall h\in\calH_{G}:R_{\calD}(h) ≤ R ^ S γ ​ ( h ) + 2 ​ 2 ​ ( ρ ⁡ ( h ) + 1 ) γ ​ n ⋅ Λ ⁡ ( h ) + 3 ​ log ⁡ ( 2 ​ ( ρ ⁡ ( h ) + 2 ) 2 ) / δ 2 ​ n , \displaystyle\leq\widehat{R}_{S}^{\,\gamma}(h)+\frac{2\sqrt{2}(\rho(h)+1)}{\gamma n}\cdot\Lambda(h)+3\sqrt{\frac{\log(2(\rho(h)+2)^2)/\delta}{2n}},

[132] p: with R ^ S γ ( h ) = 1 n ∑ i = 1 n 𝕀 [ max j ≠ y i h ( 𝐱 i ) j + γ ≥ h ( 𝐱 i ) y i ] \widehat{R}_{S}^{\,\gamma}(h)=\frac{1}{n}\sum_{i=1}^{n}\indicator[\max_{j\neq y_{i}}h(\boldsymbol{x}_{i})_{j}+\gamma\geq h(\boldsymbol{x}_{i})_{y_{i}}] and

[133] table: Λ ⁡ ( h ) = ( 1 + 2 ​ ( L ​ log ⁡ 2 + ∑ l = 1 L − 1 log ⁡ ( max j ∈ [ d l ] ⁡ | p ​ r ​ e ​ d ​ ( l , j ) | ) + log ⁡ C ) ) ⋅ max ⁡ ∏ l = 1 L − 1 j 0 , … , j L ⁡ | p ​ r ​ e ​ d ​ ( l , j l ) | ⋅ ∑ i = 1 n ‖ z j 0 0 ​ ( x i ) ‖ 2 2 . \Lambda(h)=\left(1+\sqrt{2(L\log 2+\sum_{l=1}^{L-1}\log(\max_{j \in[d_l]}|pred(l, j)|)+\log C)}\right)\cdot\sqrt{\max_{j_{0},\ldots,j_{L}}\prod_{l=1}^{L-1}|pred(l,j_{l})|\cdot\sum_{i=1}^{n}\|z_{j_{0}}^{0}(x_{i})\|_{2}^{2}}.

[134] h6: Theorem S6 (Test set bound of Langford [2005] ) .

[135] p: Let X 1 , … , X n X_{1},\ldots,X_{n} be i.i.d. random variables X i ∈ { 0 , 1 } X_{i}\in\{0,1\} and p = 𝔼 [ X i ] p=\E[X_{i}] . Then, with probability at least 1 − δ 1-\delta , we have

[136] table: p ≤ ​ B ​ i ​ n ¯ ​ ( ∑ i = 1 n X i , n , δ ) , p\leq\overline{\emph{Bin}}\left(\sum_{i=1}^{n}X_{i},n,\delta\right),

[137] p: with ​ B ​ i ​ n ​ ( k , m , p ) = ∑ i = 0 k ( m i ) ​ p i ​ ( 1 − p ) m − i \emph{Bin}(k,m,p)=\sum_{i=0}^{k}\smallmatrixquantity(\lx@physics@smallmatrix m \\ i\endlx@physics@smallmatrix)p^{i}(1-p)^{m-i} and ​ B ​ i ​ n ¯ ( k , m , δ ) = argsup p ∈ [ 0 , 1 ] { B i n ( k , m , p ) ≥ δ } . \overline{\emph{Bin}}\quantity(k,m, \delta)=\argsup_{p\in[0,1]}\{\emph{Bin}(k,m,p)\geq\delta\}.

[138] h6: Theorem S7 (Chernoff bound of Foong et al. [2022] ) .

[139] p: Let X 1 , … , X n X_{1},\ldots,X_{n} be i.i.d. random variables X i ∈ [ 0 , 1 ] X_{i}\in[0,1] and p = 𝔼 [ X i ] p=\E[X_{i}] . Then, with probability at least 1 − δ 1-\delta , we have

[140] table: p ≤ kl − 1 ​ ( 1 n ​ ∑ i = 1 n X i , 1 n ​ log ⁡ 1 δ ) . p\leq\mathrm{kl}^{-1}\quantity(\frac{1}{n} \sum_{i=1}^n X_i, \frac{1}{n}\log\frac{1}{\delta}).

[141] p: with kl ⁡ ( q , p ) = q ​ log ⁡ q p + ( 1 − q ) ​ log ⁡ 1 − q 1 − p \mathrm{kl}(q,p)=q\log\tfrac{q}{p}+(1-q)\log\tfrac{1-q}{1-p} and kl − 1 ( q , ϵ ) = argsup p ∈ [ 0 , 1 ] { kl ( q , p ) ≤ ϵ } . \mathrm{kl}^{-1}(q,\epsilon)=\argsup_{p\in[0,1]}\left\{\mathrm{kl}(q,p)\leq\epsilon\right\}.

[142] h6: Theorem S8 (Test set bound of Langford [2005] , adapted for sample-compression) .

[143] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any predictor h ∈ ℋ h\in\calH , for any random sequence 𝐢 \bfi and for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[144] table: R 𝒟 ​ ( A ⁡ ( S 𝐢 ) ) ≤ ​ B ​ i ​ n ¯ ​ ( ( n − | 𝐢 | ) ​ R ^ S 𝐢 c ​ ( A ⁡ ( S 𝐢 ) ) , n − | 𝐢 | , δ ) . R_{\calD}(A(S_{\bfi}))\leq\overline{\emph{Bin}}(n-\quantity((n-\m) \widehat{R}_{S_{\bfi^c}}(A(S_{\bfi})), n-\m, \delta))\widehat{R}_{S_{\bfi^{c}}}(A(S_{\bfi})),n-\m,\delta.

[145] h6: Theorem S9 (Sample compression bound of Laviolette et al. [2005] ) .

[146] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any deterministic reconstruction function ℛ \scriptR that outputs sample-compressed predictors h ∈ ℋ S h\in\calH_{S} and for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[147] table: ∀ 𝐢 ∈ 𝒫 ⁡ ( n ) : R 𝒟 ​ ( ℛ ⁡ ( S 𝐢 ) ) ≤ ​ 𝐵𝑖𝑛 ¯ ​ ( | 𝐢 c | ​ R ^ S 𝐢 c ​ ( ℛ ⁡ ( S 𝐢 ) ) , | 𝐢 c | , ( n | 𝐢 | ) − 1 ​ 6 π 2 ​ ( | 𝐢 | + 1 ) − 2 ​ δ ) . \displaystyle\forall\bfi\in\scriptP(n):R_{\calD}(\scriptR(S_{\bfi}))\leq\overline{\emph{Bin}}|\quantity(|\bfi^c|\widehat{R}_{S_{\bfi^c}}(\scriptR(S_{\bfi})),|\bfi^c|, \smqty(n \\ \m)^{-1} \tfrac{6}{\pi^2}(\m+1)^{-2}\delta)^{c}|\widehat{R}_{S_{\bfi^{c}}}(\scriptR(S_{\bfi})),|\bfi^{c}|,n\\ \smallmatrixquantity(\lx@physics@smallmatrix n \\ \m\endlx@physics@smallmatrix)^{-1}\tfrac{6}{\pi^{2}}(\m+1)^{-2}\delta.

[148] h6: Theorem S10 (P2L bound of Paccagnan et al. [2025] ) .

[149] p: For a fixed compression set size M M , let ℛ ⁡ ( S 𝐢 ) \scriptR(S_{\bfi}) be the output of P2L which stops when | 𝐢 | = M \m=M . For any δ ∈ ( 0 , 1 ) \delta\in(0,1) , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[150] table: R 𝒟 ​ ( ℛ ⁡ ( S 𝐢 ) ) ≤ ε ¯ ​ ( M + | 𝐢 c | ​ R ^ S 𝐢 c ​ ( ℛ ⁡ ( S 𝐢 ) ) , δ ) , R_{\calD}(\scriptR(S_{\bfi}))\ \leq\ \overline{\varepsilon}M+|\quantity(M + |\bfi^c|\widehat{R}_{S_{\bfi^c}}(\scriptR(S_{\bfi})), \ \delta)^{c}|\widehat{R}_{S_{\bfi^{c}}}(\scriptR(S_{\bfi})),\ \delta\,,

[151] p: where ε ¯ ​ ( n , δ ) = 1 \overline{\varepsilon}(n,\delta)=1 and for k = 0 , 1 , … , n − 1 k=0,1,\ldots,n-1 , ε ¯ ​ ( k , δ ) \overline{\varepsilon}(k,\delta) is the unique solution to the equation Ψ k , δ ​ ( ε ) = 1 \Psi_{k,\delta}(\varepsilon)=1 in the interval [ k n , 1 ] [\frac{k}{n},1] , with

[152] table: Ψ k , δ ​ ( ε ) \displaystyle\Psi_{k,\delta}(\varepsilon) = δ n ∑ m = k n − 1 ( m k ) ( n k ) ( 1 − ε ) − ( n − m ) . \displaystyle=\frac{\delta}{n}\hskip 4.2679pt\sum_{m=k}^{n-1}\ \ \hskip-0.56905pt\frac{\smallmatrixquantity(\lx@physics@smallmatrix m \\ k\endlx@physics@smallmatrix)}{\smallmatrixquantity(\lx@physics@smallmatrix n \\ k\endlx@physics@smallmatrix)}(1-\varepsilon)^{-(n-m)}.

[153] h6: Theorem S11 (Model compression bound, adapted from Lotfi et al. [2022] ) .

[154] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any prefix-free code 𝒞 \scriptC , for any hypothesis class ℋ 𝒞 \calH_{\scriptC} such that any h ^ ∈ ℋ 𝒞 \hat{h}\in\calH_{\scriptC} can be defined using the code 𝒞 \scriptC and for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[155] table: ∀ h ^ ∈ ℋ 𝒞 : R 𝒟 ​ ( h ^ ) ≤ ​ 𝐵𝑖𝑛 ¯ ​ ( n ​ R ^ S ​ ( h ^ ) , n , 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) ​ δ ) . \displaystyle\forall\hat{h}\in\calH_{\scriptC}:R_{\calD}(\hat{h})\leq\overline{\emph{Bin}}n\widehat{R}_{S}(\hat{h}),n,2^{-l_{\quantity(n\widehat{R}_{S}(\hat{h}),n, 2^{-l_{\scriptC}(\hat{h})}2^{- 2\log_2 l_{\scriptC}(\hat{h})}\delta)}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})}\delta.

[156] h6: Proof.

[157] p: Using the prior p ⁡ ( h ) = 1 Z ​ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) p(h)=\frac{1}{Z}2^{-l_{\scriptC}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})} of Lotfi et al. [2022] , the test set bound of Langford [2005] and the union bound, we get

[158] table: ∀ h ^ ∈ ℋ 𝒞 : R 𝒟 ​ ( h ^ ) ≤ Bin ¯ ​ ( κ , n , 1 Z ​ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) ​ δ ) . \forall\hat{h}\in\calH_{\scriptC}:R_{\calD}(\hat{h})\leq\overline{\textrm{Bin}}\kappa,n,\frac{1}{Z}2^{-l_{\quantity(\kappa,n, \frac{1}{Z}2^{-l_{\scriptC}(\hat{h})}2^{- 2\log_2 l_{\scriptC}(\hat{h})}\delta)}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})}\delta. (6)

[159] p: The binomial tail inversion is decreasing with respect to δ \delta , as a smaller δ \delta means a looser bound. By definition, Z ≤ 1 Z\leq 1 , which means that

[160] table: 1 Z ​ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) \displaystyle\frac{1}{Z}2^{-l_{\scriptC}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})} ≥ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) \displaystyle\geq 2^{-l_{\scriptC}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})} ⟹ Bin ¯ ​ ( κ , n , 1 Z ​ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) ​ δ ) \displaystyle\implies\overline{\textrm{Bin}}\kappa,n,\frac{1}{Z}2^{-l_{\quantity(\kappa,n, \frac{1}{Z}2^{-l_{\scriptC}(\hat{h})}2^{- 2\log_2 l_{\scriptC}(\hat{h})}\delta)}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})}\delta ≤ Bin ¯ ​ ( κ , n , 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) ​ δ ) . \displaystyle\leq\overline{\textrm{Bin}}\kappa,n,2^{-l_{\quantity(\kappa,n, 2^{-l_{\scriptC}(\hat{h})}2^{- 2\log_2 l_{\scriptC}(\hat{h})}\delta)}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})}\delta.

[161] p: ∎

[162] h6: Theorem S12 (Chernoff test-set bound of Foong et al. [2021] , Foong et al. [2022] ) .

[163] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any predictor h ∈ ℋ h\in\calH , for any loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] , for any random sequence 𝐢 \bfi and for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[164] table: ℒ 𝒟 ⁡ ( A ⁡ ( S 𝐢 ) ) ≤ B ℓ + λ ℓ ​ kl − 1 ​ ( ℒ ^ S 𝐢 c ⁡ ( A ⁡ ( S 𝐢 ) ) − B ℓ λ ℓ , 1 n − | 𝐢 | ​ log ⁡ 1 δ ) . \calL_{\calD}(A(S_{\bfi}))\leq B_{\ell}+\lambda_{\ell}\mathrm{kl}^{-1}\frac{\quantity(\frac{\hatL_{S_{\bfi^c}}(A(S_{\bfi})) - B_{\ell}}{\lambda_{\ell}}, \frac{1}{n-\m}\log\frac{1}{\delta})_{S_{\bfi^{c}}}(A(S_{\bfi}))-B_{\ell}}{\lambda_{\ell}},\frac{1}{n-\m}\log\frac{1}{\delta}.

[165] h6: Theorem S13 (Sample-compression bound of Bazinet et al. [2025] ) .

[166] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any deterministic reconstruction function ℛ \scriptR that outputs sample-compressed predictors h ∈ ℋ S h\in\calH_{S} , for any loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] and for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[167] table: ∀ 𝐢 ∈ 𝒫 ⁡ ( n ) : ℒ 𝒟 ​ ( ℛ ⁡ ( S 𝐢 ) ) ≤ B ℓ + λ ℓ ​ kl − 1 ​ ( ℒ ^ S 𝐢 c ⁡ ( ℛ ⁡ ( S 𝐢 ) ) − B ℓ λ ℓ , 1 | 𝐢 c | ​ [ log ⁡ ( n | 𝐢 | ) + log ⁡ ( 2 ​ | 𝐢 c | 6 π 2 ​ ( | 𝐢 | + 1 ) − 2 ​ δ ) ] ) . \displaystyle\forall\mathbf{i}\in\scriptP(n):\mathcal{L}_{\calD}(\scriptR(S_{\bfi}))\leq B_{\ell}+\lambda_{\ell}\mathrm{kl}^{-1}\frac{\quantity(\frac{\hatL_{S_{\bfi^c}}(\scriptR(S_{\bfi})) - B_{\ell}}{\lambda_{\ell}}, \frac{1}{|\bfi^c|}\qty[\log\mqty(n \\ \m) + \log\qty(\frac{2\sqrt{|\bfi^c|}}{\tfrac{6}{\pi^2}(\m+1)^{-2}\delta})])_{S_{\bfi^{c}}}(\scriptR(S_{\bfi}))-B_{\ell}}{\lambda_{\ell}},\frac{1}{|\bfi^{c}|}\log\quantity[\log\mqty(n \\ \m) + \log\qty(\frac{2\sqrt{|\bfi^c|}}{\tfrac{6}{\pi^2}(\m+1)^{-2}\delta})]+\log\frac{2\sqrt{|\quantity(\frac{2\sqrt{|\bfi^c|}}{\tfrac{6}{\pi^2}(\m+1)^{-2}\delta})^{c}|}}{\tfrac{6}{\pi^{2}}(\m+1)^{-2}\delta}\,.

[168] h6: Theorem S14 (Model compression bound, adapted from Lotfi et al. [2024] ) .

[169] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any prefix-free code 𝒞 \scriptC , for any hypothesis class ℋ 𝒞 \calH_{\scriptC} such that any h ^ ∈ ℋ 𝒞 \hat{h}\in\calH_{\scriptC} can be defined using the code 𝒞 \scriptC , for any loss ℓ : ℝ C × 𝒴 → [ B ℓ , T ℓ ] \ell:\R^{C}\times\calY\to[B_{\ell},T_{\ell}] and for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − δ 1-\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , we have

[170] table: ∀ h ^ ∈ ℋ 𝒞 : ℒ 𝒟 ​ ( h ^ ) ≤ B ℓ + λ ℓ ​ kl − 1 ​ ( ℒ ^ S ⁡ ( h ^ ) − B ℓ λ ℓ , 1 n ​ [ l 𝒞 ​ ( h ^ ) ​ log ⁡ 2 + 2 ​ log ⁡ l 𝒞 ​ ( h ^ ) + log ⁡ ( 2 ​ n δ ) ] ) . \displaystyle\forall\hat{h}\in\calH_{\scriptC}:\mathcal{L}_{\calD}(\hat{h})\leq B_{\ell}+\lambda_{\ell}\mathrm{kl}^{-1}\frac{\quantity(\frac{\hatL_{S}(\hat{h}) - B_{\ell}}{\lambda_{\ell}}, \frac{1}{n}\qty[ l_{\scriptC}(\hat{h}) \log 2 + 2 \log l_{\scriptC}(\hat{h}) + \log\qty(\frac{2\sqrt{n}}{\delta}) ])_{S}(\hat{h})-B_{\ell}}{\lambda_{\ell}},\frac{1}{n}l_{\quantity[ l_{\scriptC}(\hat{h}) \log 2 + 2 \log l_{\scriptC}(\hat{h}) + \log\qty(\frac{2\sqrt{n}}{\delta}) ]}(\hat{h})\log 2+2\log l_{\scriptC}(\hat{h})+\log\quantity(\frac{2\sqrt{n}}{\delta})\,.

[171] h6: Proof.

[172] p: We use the same proof technique as Bazinet et al. [2025] , but we replace the sample-compression prior with p ⁡ ( h ) = 1 Z ​ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) p(h)=\frac{1}{Z}2^{-l_{\scriptC}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})} . Similarly to the proof of Theorem S11 , we can avoid computing the normalizing constant Z Z as kl − 1 ​ ( q , ϵ ) \mathrm{kl}^{-1}(q,\epsilon) is decreasing in ϵ \epsilon and 1 Z ​ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) ≥ 2 − l 𝒞 ​ ( h ^ ) ​ 2 − 2 ​ log 2 ​ l 𝒞 ​ ( h ^ ) \frac{1}{Z}2^{-l_{\scriptC}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})}\geq 2^{-l_{\scriptC}(\hat{h})}2^{-2\log_{2}l_{\scriptC}(\hat{h})} . ∎

[173] h6: Theorem S15 (PAC-Bayes bound of Pérez-Ortiz et al. [2021] ) .

[174] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any set ℋ \calH of predictors h : 𝒳 → 𝒴 h:\calX\to\calY , for any loss ℓ : ℝ C × 𝒴 → [ 0 , 1 ] \ell:\R^{C}\times\calY\to[0,1] , for any dataset-independent prior distribution P P on ℋ \calH , for any δ , δ ′ ∈ ( 0 , 1 ] \delta,\delta^{\prime}\in(0,1] , with probability at least 1 − δ − δ ′ 1-\delta-\delta^{\prime} over the draw of S ∼ 𝒟 n S\sim\calD^{n} and a set of V V predictors h 1 , … , h V ∼ Q h_{1},\ldots,h_{V}\sim Q , where Q Q is a dataset-dependent posterior distribution over ℋ \calH , we have

[175] table: 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) ≤ B ℓ + λ ℓ ​ kl − 1 ​ ( kl − 1 ​ ( 1 V ​ ∑ i = 1 V ℒ ^ S ⁡ ( h i ) − B ℓ λ ℓ , 1 V ​ log ⁡ 2 δ ′ ) , 1 n ​ [ KL ( Q | | P ) + ln ( 2 ​ n δ ) ] ) . \E_{h\sim Q}\calL_{\calD}(h)\leq B_{\ell}+\lambda_{\ell}\mathrm{kl}^{-1}\mathrm{kl}^{-1}\quantity(\kl^{-1}\qty(\frac{1}{V}\sum_{i=1}^V\frac{\hatL_{S}(h_i) - B_{\ell}}{\lambda_{\ell}}, \frac{1}{V}\log\frac{2}{\delta'} ), \frac{1}{n} \qty[\KL(Q ||P) + \ln\qty(\frac{2\sqrt{n}}{\delta})]),\frac{1}{n}\quantity[\KL(Q ||P) + \ln\qty(\frac{2\sqrt{n}}{\delta})]\,.

[176] h2: Appendix B PROOFS OF THE MAIN RESULTS

[177] p: See 4

[178] h6: Proof.

[179] p: Given two predictors h , f ∈ ℋ h,f\in\calH such that h ⁡ ( 𝒙 ) = ( h ​ ( 𝒙 ) 1 , … , h ​ ( 𝒙 ) C ) h(\boldsymbol{x})=(h(\boldsymbol{x})_{1},\ldots,h(\boldsymbol{x})_{C}) and f ⁡ ( 𝒙 ) = ( f ​ ( 𝒙 ) 1 , … , f ​ ( 𝒙 ) C ) f(\boldsymbol{x})=(f(\boldsymbol{x})_{1},\ldots,f(\boldsymbol{x})_{C}) . We use f max ​ ( 𝒙 ) = argmax j f ​ ( 𝒙 ) j f_{\max}(\boldsymbol{x})=\argmax_{j}f(\boldsymbol{x})_{j} and h max ​ ( 𝒙 ) = argmax k h ​ ( 𝒙 ) k h_{\max}(\boldsymbol{x})=\argmax_{k}h(\boldsymbol{x})_{k} to simplify the notation. Then, the result of Yang et al. [2024] states that

[180] table: | R 𝒟 ​ ( f ) − R 𝒟 ​ ( h ) | ≤ 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝕀 ​ [ f max ​ ( 𝐱 ) ≠ h max ​ ( 𝐱 ) ] . \left|R_{\calD}(f)-R_{\calD}(h)\right|\leq\E_{(\boldsymbol{x},y)\sim\calD}\indicator\quantity[f_{\max}(\bx) \neq h_{\max}(\bx)]. (7)

[181] p: For completeness, we restate the proof of this result before continuing on to prove our result.

[182] table: | R 𝒟 ​ ( f ) − R 𝒟 ​ ( h ) | \displaystyle\left|R_{\calD}(f)-R_{\calD}(h)\right| = | 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝕀 ​ [ f max ​ ( 𝐱 ) ≠ y ] − 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝕀 ​ [ h max ​ ( 𝐱 ) ≠ y ] | \displaystyle=\left|\E_{(\boldsymbol{x},y)\sim\calD}\indicator\quantity[f_{\max}(\bx) \neq y]-\E_{(\boldsymbol{x},y)\sim\calD}\indicator\quantity[h_{\max}(\bx) \neq y]\right| = | 𝔼 ( 𝐱 , y ) ∼ 𝒟 [ 𝕀 ⁡ [ f max ​ ( 𝐱 ) ≠ y ] − 𝕀 ⁡ [ h max ​ ( 𝐱 ) ≠ y ] ] | \displaystyle=\left|\E_{(\boldsymbol{x},y)\sim\calD}\left[\indicator\quantity[f_{\max}(\bx) \neq y]-\indicator\quantity[h_{\max}(\bx) \neq y]\right]\right| ≤ 𝔼 ( 𝐱 , y ) ∼ 𝒟 | 𝕀 ⁡ [ f max ​ ( 𝐱 ) ≠ y ] − 𝕀 ⁡ [ h max ​ ( 𝐱 ) ≠ y ] | \displaystyle\leq\E_{(\boldsymbol{x},y)\sim\calD}\left|\indicator\quantity[f_{\max}(\bx) \neq y]-\indicator\quantity[h_{\max}(\bx) \neq y]\right| ≤ 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝕀 ​ [ f max ​ ( 𝐱 ) ≠ h max ​ ( 𝐱 ) ] . \displaystyle\leq\E_{(\boldsymbol{x},y)\sim\calD}\indicator\quantity[f_{\max}(\bx) \neq h_{\max}(\bx)]\,.

[183] p: The first inequality is the triangular inequality. The second inequality can easily be showed with a truth table (see Table S1 ).

[184] figure: 𝕀 ⁡ [ f max ​ ( 𝐱 ) ≠ y ] \indicator\quantity[f_{\max}(\bx) \neq y] 𝕀 ⁡ [ h max ​ ( 𝐱 ) ≠ y ] \indicator\quantity[h_{\max}(\bx) \neq y] ∣ 𝕀 ⁡ [ f max ​ ( 𝐱 ) ≠ y ] − 𝕀 ⁡ [ h max ​ ( 𝐱 ) ≠ y ] ∣ \mid\!\indicator\quantity[f_{\max}(\bx) \neq y]-\indicator\quantity[h_{\max}(\bx) \neq y]\!\mid 𝕀 ⁡ [ f max ​ ( 𝐱 ) ≠ h max ​ ( 𝐱 ) ] \indicator\quantity[f_{\max}(\bx) \neq h_{\max}(\bx) ] 0 0 0 0 1 0 1 1 0 1 1 1 1 1 0 0 or 1 Table S1 : Truth table (0 for false, 1 for true). Let 𝒴 = { 1 , … , C } \calY=\{1,\ldots,C\} the set of classes. First line: if both f max ​ ( 𝒙 ) = y f_{\max}(\boldsymbol{x})=y and h max ​ ( 𝒙 ) = y h_{\max}(\boldsymbol{x})=y , then f max ​ ( 𝒙 ) = h max ​ ( 𝒙 ) f_{\max}(\boldsymbol{x})=h_{\max}(\boldsymbol{x}) . Second line (and similarly for the third line): if f max ​ ( 𝒙 ) ≠ y f_{\max}(\boldsymbol{x})\neq y and h max ​ ( 𝒙 ) = y h_{\max}(\boldsymbol{x})=y , then f max ​ ( 𝒙 ) ≠ h max ​ ( 𝒙 ) f_{\max}(\boldsymbol{x})\neq h_{\max}(\boldsymbol{x}) . Without loss of generality, suppose y = 1 y=1 . Then, for the last line, if f max ​ ( 𝒙 ) ≠ y f_{\max}(\boldsymbol{x})\neq y and h max ​ ( 𝒙 ) ≠ y h_{\max}(\boldsymbol{x})\neq y , then we have f max ​ ( 𝒙 ) ∈ { 2 , … , C } f_{\max}(\boldsymbol{x})\in\{2,\ldots,C\} and h max ​ ( 𝒙 ) ∈ { 2 , … , C } h_{\max}(\boldsymbol{x})\in\{2,\ldots,C\} . It is then both possible to have f max ( 𝒙 ) = h max ( 𝒙 ) ⟹ 𝕀 [ f max ( 𝐱 ) ≠ h max ( 𝐱 ) ] = 0 f_{\max}(\boldsymbol{x})=h_{\max}(\boldsymbol{x})\implies\indicator[f_{\max}(\boldsymbol{x})\neq h_{\max}(\boldsymbol{x})]=0 and f max ( 𝒙 ) ≠ h max ( 𝒙 ) ⟹ 𝕀 [ f max ( 𝐱 ) ≠ h max ( 𝐱 ) ] = 1 f_{\max}(\boldsymbol{x})\neq h_{\max}(\boldsymbol{x})\implies\indicator[f_{\max}(\boldsymbol{x})\neq h_{\max}(\boldsymbol{x})]=1 .

[185] p: Equation 7 is not computable because it requires knowledge of the true data distribution 𝒟 \calD . We now extend this result and upperbound the disagreement. To do so, we start by applying the binomial test-set bound of Langford (2005) (see Theorem S8 ) on the right hand side of Eq. 7 , with p = 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝕀 ​ [ f max ​ ( 𝐱 ) ≠ h max ​ ( 𝐱 ) ] p=\E_{(\boldsymbol{x},y)\sim\calD}\indicator\quantity[f_{\max}(\bx) \neq h_{\max}(\bx)] .

[186] table: 1 − δ ≤ \displaystyle 1-\delta\leq ℙ U ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝕀 ​ [ f max ​ ( 𝐱 ) ≠ h max ​ ( 𝐱 ) ] ≤ Bin ¯ ​ ( ∑ i = 1 m 𝕀 ⁡ [ f max ​ ( 𝐱 i ) ≠ h max ​ ( 𝐱 i ) ] , m , δ ) ) \displaystyle\Prob_{U\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD}\indicator\qty[f_{\max}(\bx) \neq h_{\max}(\bx)] \leq\overline{\mathrm{Bin}}\qty(\sum_{i=1}^m \indicator\qty[f_{\max}(\bx_i) \neq h_{\max}(\bx_i)], m, \delta))_{(\boldsymbol{x},y)\sim\calD}\indicator\quantity[f_{\max}(\bx) \neq h_{\max}(\bx)]\leq\overline{\mathrm{Bin}}\sum_{i=1}^{m}\quantity(\sum_{i=1}^m \indicator\qty[f_{\max}(\bx_i) \neq h_{\max}(\bx_i)], m, \delta)\quantity[f_{\max}(\bx_i) \neq h_{\max}(\bx_i)],m,\delta ≤ \displaystyle\leq ℙ U ∼ 𝒟 m ( | R 𝒟 ​ ( f ) − R 𝒟 ​ ( h ) | ≤ Bin ¯ ​ ( ∑ i = 1 m 𝕀 ⁡ [ f max ​ ( 𝐱 i ) ≠ h max ​ ( 𝐱 i ) ] , m , δ ) ) \displaystyle\Prob_{U\sim\calD^{m}}\left|R_{\quantity(\left| R_{\calD}(f) - R_{\calD}(h)\right| \leq\overline{\mathrm{Bin}}\qty(\sum_{i=1}^m \indicator\qty[f_{\max}(\bx_i) \neq h_{\max}(\bx_i)], m, \delta))}(f)-R_{\calD}(h)\right|\leq\overline{\mathrm{Bin}}\sum_{i=1}^{m}\quantity(\sum_{i=1}^m \indicator\qty[f_{\max}(\bx_i) \neq h_{\max}(\bx_i)], m, \delta)\quantity[f_{\max}(\bx_i) \neq h_{\max}(\bx_i)],m,\delta (Equation 7 ) = \displaystyle= ℙ U ∼ 𝒟 m ( | R 𝒟 ​ ( f ) − R 𝒟 ​ ( h ) | ≤ Bin ¯ ​ ( md U 0 ​ - ​ 1 ​ ( f , h ) , m , δ ) ) \displaystyle\Prob_{U\sim\calD^{m}}\left|R_{\quantity(\left|R_{\calD}(f) - R_{\calD}(h)\right| \leq\overline{\mathrm{Bin}}\qty(m\dzero_U(f, h), m, \delta))}(f)-R_{\calD}(h)\right|\leq\overline{\mathrm{Bin}}\quantity(m\dzero_U(f, h), m, \delta) ≤ \displaystyle\leq ℙ U ∼ 𝒟 m ( R 𝒟 ​ ( f ) ≤ R 𝒟 ​ ( h ) + Bin ¯ ​ ( md U 0 ​ - ​ 1 ​ ( f , h ) , m , δ ) ) \displaystyle\Prob_{U\sim\calD^{m}}R_{\quantity( R_{\calD}(f) \leq R_{\calD}(h) + \overline{\mathrm{Bin}}\qty(m\dzero_U(f, h), m, \delta))}(f)\leq R_{\calD}(h)+\overline{\mathrm{Bin}}\quantity(m\dzero_U(f, h), m, \delta)

[187] p: with

[188] table: d U 0 ​ - ​ 1 ​ ( f , h ) = 1 m ​ ∑ i = 1 m 𝕀 ⁡ [ argmax j f ​ ( 𝐱 i ) j ≠ argmax k h ​ ( 𝐱 i ) k ] . d^{0\textrm{-}1}_{U}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\indicator\quantity[\argmax_j \ f(\bx_i)_j \neq\argmax_k \ h(\bx_i)_k].

[189] p: ∎

[190] p: We make the assumption that the loss natively applies a softmax over the output of the predictors. Otherwise, we simply consider h ′ ​ ( ⋅ ) = 𝝈 ⁡ ( h ⁡ ( ⋅ ) ) h^{\prime}(\cdot)=\boldsymbol{\sigma}(h(\cdot)) in the proof. See 5

[191] h6: Proof of Theorem 5 .

[192] p: With 𝝈 ⁡ ( f ⁡ ( 𝒙 ) ) = ( σ ⁡ ( f ⁡ ( 𝒙 ) , 1 ) , … , σ ⁡ ( f ⁡ ( 𝒙 ) , C ) ) \boldsymbol{\sigma}(f(\boldsymbol{x}))=\left(\sigma(f(\boldsymbol{x}),1),\ldots,\sigma(f(\boldsymbol{x}),C)\right) , we have

[193] table: | ℒ 𝒟 ⁡ ( f ) − 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) | \displaystyle\left|\calL_{\calD}(f)-\E_{h\sim Q}\calL_{\calD}(h)\right| = | 𝔼 h ∼ Q [ ℒ 𝒟 ⁡ ( f ) − ℒ 𝒟 ⁡ ( h ) ] | \displaystyle=\left|\E_{h\sim Q}\quantity[\calL_{\calD}(f) - \calL_{\calD}(h)]_{\calD}(f)-\calL_{\calD}(h)\right| = | 𝔼 h ∼ Q [ 𝔼 ( 𝐱 , y ) ∼ 𝒟 ℓ ​ ( f ⁡ ( 𝐱 ) , y ) − 𝔼 ( 𝐱 , y ) ∼ 𝒟 ℓ ​ ( h ⁡ ( 𝐱 ) , y ) ] | \displaystyle=\left|\E_{h\sim Q}\quantity[\E_{(\bx,y) \sim\calD} \ell(f(\bx), y) - \E_{(\bx,y) \sim\calD} \ell(h(\bx),y)]_{(\boldsymbol{x},y)\sim\calD}\ell(f(\boldsymbol{x}),y)-\E_{(\boldsymbol{x},y)\sim\calD}\ell(h(\boldsymbol{x}),y)\right| = | 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ [ ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) ] | \displaystyle=\left|\E_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}\quantity[ \ell(f(\bx), y) -\ell(h(\bx),y)]\right| ≤ 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | \displaystyle\leq\E_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right| ≤ 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ K ℓ ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 \displaystyle\leq\E_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}K_{\ell}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1} = K ℓ ​ 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ 𝔼 h ∼ Q ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 . \displaystyle=K_{\ell}\E_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}.

[194] p: The first inequality stems from the triangular inequality. The second inequality comes from the K ℓ K_{\ell} -Lipschitz continuity of ℓ \ell .

[195] p: The 1-norm of the difference of two softmax distribution is always positive and always bounded by 2 2 , which can easily be proven using triangle inequality.

[196] table: ‖ 𝝈 ⁡ ( f ⁡ ( 𝒙 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝒙 ) ) ‖ 1 ≤ ‖ 𝝈 ⁡ ( f ⁡ ( 𝒙 ) ) ‖ 1 + ‖ 𝝈 ⁡ ( h ⁡ ( 𝒙 ) ) ‖ 1 ≤ 2 . \|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}\leq\|\boldsymbol{\sigma}(f(\boldsymbol{x}))\|_{1}+\|\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}\leq 2.

[197] p: From Chernoff’s bound for random variables in the unit interval [ Foong et al., 2022 ] , with p = 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ 1 2 ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 {p=\E_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\frac{1}{2}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}} , we have

[198] table: ℙ U ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ 1 2 ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 ≤ kl − 1 ​ ( 𝔼 h ∼ Q 1 m ​ ∑ i = 1 m 1 2 ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 i ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 i ) ) ‖ 1 , 1 m ​ log ​ 1 δ ) ) ≥ 1 − δ . \Prob_{U\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD} \E_{h \sim Q} \frac{1}{2} \|\boldsigma(f(\bx)) - \boldsigma(h(\bx))\|_1\leq\kl^{-1}\qty(\E_{h \sim Q} \frac{1}{m}\sum_{i=1}^m \frac{1}{2} \|\boldsigma(f(\bx_i)) - \boldsigma(h(\bx_i))\|_1, \frac{1}{m}\log\frac{1}{\delta}))_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\frac{1}{2}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}\leq\mathrm{kl}^{-1}\quantity(\E_{h \sim Q} \frac{1}{m}\sum_{i=1}^m \frac{1}{2} \|\boldsigma(f(\bx_i)) - \boldsigma(h(\bx_i))\|_1, \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{m}\sum_{i=1}^{m}\frac{1}{2}\|\boldsymbol{\sigma}(f(\boldsymbol{x}_{i}))-\boldsymbol{\sigma}(h(\boldsymbol{x}_{i}))\|_{1},\frac{1}{m}\log\frac{1}{\delta}\geq 1-\delta.

[199] p: Let the difference between the losses be denoted by

[200] table: d U K ℓ ​ ( f , h ) = ‖ 𝝈 ⁡ ( f ⁡ ( 𝒙 i ) ) − 𝝈 ⁡ ( h ⁡ ( 𝒙 i ) ) ‖ 1 . d_{U}^{K_{\ell}}(f,h)=\|\boldsymbol{\sigma}(f(\boldsymbol{x}_{i}))-\boldsymbol{\sigma}(h(\boldsymbol{x}_{i}))\|_{1}.

[201] p: We finish the proof.

[202] table: 1 − δ \displaystyle 1-\delta ≤ ℙ U ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ 1 2 ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 ≤ kl − 1 ​ ( 1 2 ​ 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle\leq\Prob_{U\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD} \E_{h \sim Q} \frac{1}{2} \|\boldsigma(f(\bx)) - \boldsigma(h(\bx))\|_1 \leq\kl^{-1}\qty(\frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\frac{1}{2}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}\leq\mathrm{kl}^{-1}\frac{1}{2}\quantity(\frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}d_{U}^{K_{\ell}}(f,h),\frac{1}{m}\log\frac{1}{\delta} = ℙ U ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 ≤ 2 ​ k ​ l − 1 ​ ( 1 2 ​ 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle=\Prob_{U\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD}\E_{h \sim Q} \|\boldsigma(f(\bx)) - \boldsigma(h(\bx))\|_1 \leq 2\kl^{-1}\qty( \frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}\leq 2\mathrm{kl}^{-1}\frac{1}{2}\quantity( \frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}d_{U}^{K_{\ell}}(f,h),\frac{1}{m}\log\frac{1}{\delta} = ℙ U ∼ 𝒟 m ( 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ K ℓ ​ ‖ 𝝈 ⁡ ( f ⁡ ( 𝐱 ) ) − 𝝈 ⁡ ( h ⁡ ( 𝐱 ) ) ‖ 1 ≤ 2 ​ K ℓ ​ kl − 1 ​ ( 1 2 ​ 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle=\Prob_{U\sim\calD^{m}}\quantity(\E_{h \sim Q}\E_{(\bx,y) \sim\calD} K_{\ell}\|\boldsigma(f(\bx)) - \boldsigma(h(\bx))\|_1 \leq 2K_{\ell}\kl^{-1}\qty( \frac{1}{2}\E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}K_{\ell}\|\boldsymbol{\sigma}(f(\boldsymbol{x}))-\boldsymbol{\sigma}(h(\boldsymbol{x}))\|_{1}\leq 2K_{\ell}\mathrm{kl}^{-1}\frac{1}{2}\quantity( \frac{1}{2}\E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}d_{U}^{K_{\ell}}(f,h),\frac{1}{m}\log\frac{1}{\delta} ≤ ℙ U ∼ 𝒟 m ( 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | ≤ 2 ​ K ℓ ​ kl − 1 ​ ( 1 2 ​ 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle\leq\Prob_{U\sim\calD^{m}}\quantity(\E_{h \sim Q}\E_{(\bx,y) \sim\calD} \left| \ell(f(\bx), y) -\ell(h(\bx),y)\right| \leq 2 K_{\ell} \kl^{-1}\qty( \frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|\leq 2K_{\ell}\mathrm{kl}^{-1}\frac{1}{2}\quantity( \frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}d_{U}^{K_{\ell}}(f,h),\frac{1}{m}\log\frac{1}{\delta} ≤ ℙ U ∼ 𝒟 m ( | ℒ 𝒟 ⁡ ( f ) − 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) | ≤ 2 ​ K ℓ ​ kl − 1 ​ ( 1 2 ​ 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle\leq\Prob_{U\sim\calD^{m}}\left|\quantity( \left| \calL_{\calD}(f) - \E_{h \sim Q} \calL_{\calD}(h) \right| \leq 2K_{\ell}\kl^{-1}\qty( \frac{1}{2}\E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{\calD}(f)-\E_{h\sim Q}\calL_{\calD}(h)\right|\leq 2K_{\ell}\mathrm{kl}^{-1}\frac{1}{2}\quantity( \frac{1}{2}\E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}d_{U}^{K_{\ell}}(f,h),\frac{1}{m}\log\frac{1}{\delta} = ℙ U ∼ 𝒟 m ( ℒ 𝒟 ⁡ ( f ) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + 2 ​ K ℓ ​ kl − 1 ​ ( 1 2 ​ 𝔼 h ∼ Q d U K ℓ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) . \displaystyle=\Prob_{U\sim\calD^{m}}\quantity(\calL_{\calD}(f) \leq\E_{h \sim Q} \calL_{\calD}(h) + 2K_{\ell}\kl^{-1}\qty( \frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{\calD}(f)\leq\E_{h\sim Q}\calL_{\calD}(h)+2K_{\ell}\mathrm{kl}^{-1}\frac{1}{2}\quantity( \frac{1}{2} \E_{h \sim Q} d_U^{K_{\ell}}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}d_{U}^{K_{\ell}}(f,h),\frac{1}{m}\log\frac{1}{\delta}.

[203] p: ∎

[204] p: See 6

[205] h6: Proof of Theorem 6 .

[206] table: | ℒ 𝒟 ⁡ ( f ) − 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) | \displaystyle\left|\calL_{\calD}(f)-\E_{h\sim Q}\calL_{\calD}(h)\right| = | 𝔼 h ∼ Q [ ℒ 𝒟 ⁡ ( f ) − ℒ 𝒟 ⁡ ( h ) ] | \displaystyle=\left|\E_{h\sim Q}\quantity[\calL_{\calD}(f) - \calL_{\calD}(h)]_{\calD}(f)-\calL_{\calD}(h)\right| = | 𝔼 h ∼ Q [ 𝔼 ( 𝐱 , y ) ∼ 𝒟 ℓ ​ ( f ⁡ ( 𝐱 ) , y ) − 𝔼 ( 𝐱 , y ) ∼ 𝒟 ℓ ​ ( h ⁡ ( 𝐱 ) , y ) ] | \displaystyle=\left|\E_{h\sim Q}\quantity[\E_{(\bx,y) \sim\calD} \ell(f(\bx), y) - \E_{(\bx,y) \sim\calD} \ell(h(\bx),y)]_{(\boldsymbol{x},y)\sim\calD}\ell(f(\boldsymbol{x}),y)-\E_{(\boldsymbol{x},y)\sim\calD}\ell(h(\boldsymbol{x}),y)\right| = | 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ [ ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) ] | \displaystyle=\left|\E_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}\quantity[ \ell(f(\bx), y) -\ell(h(\bx),y)]\right| ≤ 𝔼 h ∼ Q 𝔼 ( 𝐱 , y ) ∼ 𝒟 ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | \displaystyle\leq\E_{h\sim Q}\E_{(\boldsymbol{x},y)\sim\calD}\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right| = 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | \displaystyle=\E_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|

[207] p: The inequality stems from the triangular inequality.

[208] p: To use Chernoff’s bound, we need a loss in the unit interval, so we normalize it.

[209] table: 0 ≤ | ℓ ⁡ ( f ⁡ ( 𝒙 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝒙 ) , y ) | max y , y ′ ⁡ ℓ ⁡ ( y ′ , y ) − min y , y ′ ⁡ ℓ ⁡ ( y ′ , y ) = | ℓ ⁡ ( f ⁡ ( 𝒙 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝒙 ) , y ) | T ℓ − B ℓ ≤ 1 . 0\leq\frac{\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|}{\max_{y,y^{\prime}}\ell(y^{\prime},y)-\min_{y,y^{\prime}}\ell(y^{\prime},y)}=\frac{\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|}{T_{\ell}-B_{\ell}}\leq 1.

[210] p: We set λ ℓ ≔ T ℓ − B ℓ \lambda_{\ell}\coloneqq T_{\ell}-B_{\ell} . Then, from Chernoff’s bound for random variables in the unit interval [ Foong et al., 2022 ] , with p = 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ 1 λ ℓ ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | p=\E_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\frac{1}{\lambda_{\ell}}\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right| , we have

[211] table: ℙ L ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | λ ℓ ≤ kl − 1 ​ ( 𝔼 h ∼ Q 1 m ​ ∑ i = 1 m | ℓ ⁡ ( f ⁡ ( 𝐱 i ) , y i ) − ℓ ⁡ ( h ⁡ ( 𝐱 i ) , y i ) | λ ℓ , 1 m ​ log ⁡ 1 δ ) ) ≥ 1 − δ . \Prob_{L\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD} \E_{h \sim Q}\frac{\left| \ell(f(\bx), y) -\ell(h(\bx),y)\right|}{\lambda_{\ell}} \leq\kl^{-1}\qty( \E_{h \sim Q}\frac{1}{m}\sum_{i=1}^m \frac{\left| \ell(f(\bx_i), y_i) -\ell(h(\bx_i),y_i)\right|}{\lambda_{\ell}}, \frac{1}{m}\log\frac{1}{\delta}))_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\frac{\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|}{\lambda_{\ell}}\leq\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{m}\sum_{i=1}^m \frac{\left| \ell(f(\bx_i), y_i) -\ell(h(\bx_i),y_i)\right|}{\lambda_{\ell}}, \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{m}\sum_{i=1}^{m}\frac{\left|\ell(f(\boldsymbol{x}_{i}),y_{i})-\ell(h(\boldsymbol{x}_{i}),y_{i})\right|}{\lambda_{\ell}},\frac{1}{m}\log\frac{1}{\delta}\geq 1-\delta.

[212] p: Let the difference between the losses be denoted by

[213] table: d L ​ ( f , h ) = 1 m ​ ∑ i = 1 m | ℓ ⁡ ( f ⁡ ( 𝒙 i ) , y i ) − ℓ ⁡ ( h ⁡ ( 𝒙 i ) , y i ) | . d_{L}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\left|\ell(f(\boldsymbol{x}_{i}),y_{i})-\ell(h(\boldsymbol{x}_{i}),y_{i})\right|.

[214] p: We finish the proof.

[215] table: 1 − δ \displaystyle 1-\delta ≤ ℙ L ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | λ ℓ ≤ kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle\leq\Prob_{L\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD} \E_{h \sim Q} \frac{\left| \ell(f(\bx), y) -\ell(h(\bx),y)\right|}{\lambda_{\ell}} \leq\kl^{-1}\qty( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\frac{\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|}{\lambda_{\ell}}\leq\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta} = ℙ L ∼ 𝒟 m ( 𝔼 ( 𝐱 , y ) ∼ 𝒟 𝔼 h ∼ Q ​ | ℓ ⁡ ( f ⁡ ( 𝐱 ) , y ) − ℓ ⁡ ( h ⁡ ( 𝐱 ) , y ) | ≤ λ ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle=\Prob_{L\sim\calD^{m}}\quantity(\E_{(\bx,y) \sim\calD} \E_{h \sim Q} \left| \ell(f(\bx), y) -\ell(h(\bx),y)\right| \leq\lambda_{\ell}\kl^{-1}\qty( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{(\boldsymbol{x},y)\sim\calD}\E_{h\sim Q}\left|\ell(f(\boldsymbol{x}),y)-\ell(h(\boldsymbol{x}),y)\right|\leq\lambda_{\ell}\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta} ≤ ℙ L ∼ 𝒟 m ( | ℒ 𝒟 ⁡ ( f ) − 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) | ≤ λ ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) \displaystyle\leq\Prob_{L\sim\calD^{m}}\left|\quantity( \left| \calL_{\calD}(f) - \E_{h \sim Q} \calL_{\calD}(h) \right| \leq\lambda_{\ell}\kl^{-1}\qty( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{\calD}(f)-\E_{h\sim Q}\calL_{\calD}(h)\right|\leq\lambda_{\ell}\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta} = ℙ L ∼ 𝒟 m ( ℒ 𝒟 ⁡ ( f ) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + λ ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ) . \displaystyle=\Prob_{L\sim\calD^{m}}\quantity(\calL_{\calD}(f) \leq\E_{h \sim Q} \calL_{\calD}(h) + \lambda_{\ell}\kl^{-1}\qty( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta}))_{\calD}(f)\leq\E_{h\sim Q}\calL_{\calD}(h)+\lambda_{\ell}\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta}.

[216] p: ∎

[217] h6: Corollary S16 .

[218] p: In the setting of Theorem 6 , for a Lipschitz continuous loss function ℓ \ell with constant K ℓ K_{\ell} , with probability at least 1 − δ 1-\delta over the sampling of L ∼ 𝒟 m L\sim\calD^{m} , we have :

[219] table: ℒ 𝒟 ⁡ ( f ) \displaystyle\calL_{\calD}(f) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + λ ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\lambda_{\ell}\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}} d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta} ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + λ ℓ ​ kl − 1 ​ ( 𝔼 h ∼ Q K ℓ λ ℓ ​ d L ^ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\lambda_{\ell}\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{K_{\ell}}{\lambda_{\ell}} \widehat{d_L}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{K_{\ell}}{\lambda_{\ell}}\widehat{d_{L}}(f,h),\frac{1}{m}\log\frac{1}{\delta}

[220] p: with

[221] table: d L ^ ​ ( f , h ) = 1 m ​ ∑ i = 1 m ‖ σ ⁡ ( f ⁡ ( 𝒙 i ) , y i ) − σ ⁡ ( h ⁡ ( 𝒙 i ) , y i ) ‖ 1 . \widehat{d_{L}}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\|\sigma(f(\boldsymbol{x}_{i}),y_{i})-\sigma(h(\boldsymbol{x}_{i}),y_{i})\|_{1}.

[222] h6: Proof.

[223] p: Following from the Lipschitz-continuity of ℓ \ell , we have

[224] table: d L ​ ( f , h ) = 1 m ​ ∑ i = 1 m | ℓ ⁡ ( f ⁡ ( 𝒙 i ) , y i ) − ℓ ⁡ ( h ⁡ ( 𝒙 i ) , y i ) | ≤ K ℓ m ​ ∑ i = 1 m ‖ σ ⁡ ( f ⁡ ( 𝒙 i ) , y i ) − σ ⁡ ( h ⁡ ( 𝒙 i ) , y i ) ‖ 1 . d_{L}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\left|\ell(f(\boldsymbol{x}_{i}),y_{i})-\ell(h(\boldsymbol{x}_{i}),y_{i})\right|\leq\frac{K_{\ell}}{m}\sum_{i=1}^{m}\|\sigma(f(\boldsymbol{x}_{i}),y_{i})-\sigma(h(\boldsymbol{x}_{i}),y_{i})\|_{1}.

[225] p: Moreover, as kl − 1 ​ ( q , ϵ ) \mathrm{kl}^{-1}(q,\epsilon) is monotonically increasing in q q , we have :

[226] table: kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ≤ kl − 1 ​ ( 𝔼 h ∼ Q K ℓ λ ℓ ​ 1 m ​ ∑ i = 1 m ‖ σ ⁡ ( f ⁡ ( 𝐱 i ) , y i ) − σ ⁡ ( h ⁡ ( 𝐱 i ) , y i ) ‖ 1 , 1 m ​ log ​ 1 δ ) . \mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta}\leq\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{K_{\ell}}{\lambda_{\ell}}\frac{1}{m}\sum_{i=1}^m \|\sigma(f(\bx_i), y_i) - \sigma(h(\bx_i), y_i)\|_1, \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{K_{\ell}}{\lambda_{\ell}}\frac{1}{m}\sum_{i=1}^{m}\|\sigma(f(\boldsymbol{x}_{i}),y_{i})-\sigma(h(\boldsymbol{x}_{i}),y_{i})\|_{1},\frac{1}{m}\log\frac{1}{\delta}.

[227] p: ∎

[228] h2: Appendix C ADDITIONAL RESULTS

[229] h3: C.1 Special cases of the main results

[230] h6: Corollary S17 .

[231] p: In the setting of Theorem 6 , with α ∈ ( 0 , 1 ) \alpha\in(0,1) , β = C α \beta=\frac{C}{\alpha} , the clamped softmax (see Definition S1 ) and the clamped cross-entropy loss ℓ ⁡ ( g ⁡ ( 𝐱 ) , y ) = − ln ⁡ ( σ max ​ ( g ​ ( 𝐱 ) , y ) ) \ell(g(\boldsymbol{x}),y)=-\ln(\sigma_{\max}(g(\bx),y)) , with probability at least 1 − δ 1-\delta over the sampling of L ∼ 𝒟 m L\sim\calD^{m} , we have

[232] table: 𝔼 f ∼ P ℒ 𝒟 ​ ( f ) \displaystyle\E_{f\sim P}\calL_{\calD}(f) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + ln ⁡ ( β ) ​ kl − 1 ​ ( 𝔼 h ∼ Q 1 ln ⁡ ( β ) ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\ln\left(\beta\right)\mathrm{kl}^{-1}\quantity( \E_{h \sim Q} \frac{1}{\ln\left(\beta\right)}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\ln\left(\beta\right)}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta} ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + ln ⁡ ( β ) ​ kl − 1 ​ ( 𝔼 h ∼ Q β ln ⁡ ( β ) ​ d L ^ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\ln\left(\beta\right)\mathrm{kl}^{-1}\quantity( \E_{h \sim Q} \frac{\beta}{\ln\left(\beta\right)}\widehat{d_L}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{\beta}{\ln\left(\beta\right)}\widehat{d_{L}}(f,h),\frac{1}{m}\log\frac{1}{\delta}

[233] p: with

[234] table: d L ^ ​ ( f , h ) = 1 m ​ ∑ i = 1 m ‖ σ max ​ ( f ⁡ ( 𝒙 i ) , y i ) − σ max ​ ( h ⁡ ( 𝒙 i ) , y i ) ‖ 1 . \widehat{d_{L}}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\|\sigma_{\max}(f(\boldsymbol{x}_{i}),y_{i})-\sigma_{\max}(h(\boldsymbol{x}_{i}),y_{i})\|_{1}.

[235] h6: Proof.

[236] p: This corollary is an application of Theorem 6 and Corollary S16 to the clamped cross-entropy loss. In Corollary S16 , we want to highlight the difference between the clamped softmax of f f and h h . Thus, we consider the loss ℓ \ell as simply − ln ⁡ ( u ) -\ln(u) , with u ∈ ( α C , 1 ) u\in(\frac{\alpha}{C},1) .

[237] p: We now find the Lipschitz constant K ℓ K_{\ell} by computing the gradient of ℓ \ell .

[238] table: K ℓ = sup u ∈ ( α C , 1 ) | d ( − ln ⁡ ( u ) ) d u | = sup u ∈ ( α C , 1 ) | d ln ⁡ ( u ) d u | = sup u ∈ ( α C , 1 ) | 1 u | = C α . K_{\ell}=\sup_{u\in(\frac{\alpha}{C},1)}\left|\derivative{(-\ln(u))}{u}\right|=\sup_{u\in(\frac{\alpha}{C},1)}\left|\derivative{\ln(u)}{u}\right|=\sup_{u\in(\frac{\alpha}{C},1)}\left|\frac{1}{u}\right|=\frac{C}{\alpha}.

[239] p: To simplify the notation in the theorem, we choose β = C α \beta=\frac{C}{\alpha} . ∎

[240] h6: Corollary S18 .

[241] p: In the setting of Theorem 6 , with α ∈ ( 0 , 1 ) \alpha\in(0,1) , β = C α \beta=\frac{C}{\alpha} , the smoothed softmax (see Definition S2 ) and the smoothed cross-entropy loss ℓ ⁡ ( g ⁡ ( 𝐱 ) , y ) = − ln ⁡ ( σ ​ s ​ m ​ o ​ o ​ t ​ h ​ ( g ​ ( 𝐱 ) , y ) ) \ell(g(\boldsymbol{x}),y)=-\ln(\sigma_{\emph{smooth}}(g(\bx),y)) , with probability at least 1 − δ 1-\delta over the sampling of L ∼ 𝒟 m L\sim\calD^{m} , we have

[242] table: 𝔼 f ∼ P ℒ 𝒟 ​ ( f ) \displaystyle\E_{f\sim P}\calL_{\calD}(f) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + ln ⁡ ( 1 + ( 1 − α ) ​ β ) ​ kl − 1 ​ ( 𝔼 h ∼ Q 1 ln ⁡ ( 1 + ( 1 − α ) ​ β ) ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\ln\left(1+(1-\alpha)\beta\right)\mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\ln\left(1 + (1-\alpha)\beta\right)}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\ln\left(1+(1-\alpha)\beta\right)}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta} ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + ln ⁡ ( 1 + ( 1 − α ) ​ β ) ​ kl − 1 ​ ( 𝔼 h ∼ Q β ln ⁡ ( 1 + ( 1 − α ) ​ β ) ​ d L ^ ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) \displaystyle\leq\E_{h\sim Q}\calL_{\calD}(h)+\ln\left(1+(1-\alpha)\beta\right)\mathrm{kl}^{-1}\quantity( \E_{h \sim Q} \frac{\beta}{\ln\left(1 + (1-\alpha)\beta\right)} \widehat{d_L}(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{\beta}{\ln\left(1+(1-\alpha)\beta\right)}\widehat{d_{L}}(f,h),\frac{1}{m}\log\frac{1}{\delta}

[243] p: with

[244] table: d L ^ ​ ( f , h ) = 1 m ​ ∑ i = 1 m ‖ σ ​ s ​ m ​ o ​ o ​ t ​ h ​ ( f ⁡ ( 𝒙 i ) , y i ) − σ ​ s ​ m ​ o ​ o ​ t ​ h ​ ( h ⁡ ( 𝒙 i ) , y i ) ‖ 1 . \widehat{d_{L}}(f,h)=\frac{1}{m}\sum_{i=1}^{m}\|\sigma_{\emph{smooth}}(f(\boldsymbol{x}_{i}),y_{i})-\sigma_{\emph{smooth}}(h(\boldsymbol{x}_{i}),y_{i})\|_{1}.

[245] h6: Proof.

[246] p: This corollary is an application of Theorem 6 and Corollary S16 to the clamped cross-entropy loss. In Corollary S16 , we want to highlight the difference between the smoothed softmax of f f and h h . Thus, we consider the loss ℓ \ell as simply − ln ⁡ ( u ) -\ln(u) , with u ∈ ( α C , 1 − α + α C ) u\in\left(\frac{\alpha}{C},1-\alpha+\frac{\alpha}{C}\right) .

[247] p: We now find the Lipschitz constant K ℓ K_{\ell} by computing the gradient of ℓ \ell .

[248] table: K ℓ = sup u ∈ ( α C , 1 − α + α C ) | d ( − ln ⁡ ( u ) ) d u | = sup u ∈ ( α C , 1 − α + α C ) | d ln ⁡ ( u ) d u | = sup u ∈ ( α C , 1 − α + α C ) | 1 u | = C α . K_{\ell}=\sup_{u\in\left(\frac{\alpha}{C},1-\alpha+\frac{\alpha}{C}\right)}\left|\derivative{(-\ln(u))}{u}\right|=\sup_{u\in\left(\frac{\alpha}{C},1-\alpha+\frac{\alpha}{C}\right)}\left|\derivative{\ln(u)}{u}\right|=\sup_{u\in\left(\frac{\alpha}{C},1-\alpha+\frac{\alpha}{C}\right)}\left|\frac{1}{u}\right|=\frac{C}{\alpha}.

[249] p: To simplify the notation in the theorem, we choose β = C α \beta=\frac{C}{\alpha} . ∎

[250] h3: C.2 Computable PAC-Bayesian disagreement bounds

[251] p: To compute the bounds exactly, we need to use the same trick as in Theorem S15 , that is we approximate the sampling of the hypothesis from the posterior Q Q via Monte Carlo Sampling. This result can be applied to the zero-one loss, as we have λ ℓ = 1 \lambda_{\ell}=1 and d L ​ ( ⋅ , ⋅ ) ≤ d L 0 ​ - ​ 1 ​ ( ⋅ , ⋅ ) d_{L}(\cdot,\cdot)\leq d^{0\textrm{-}1}_{L}(\cdot,\cdot) by Eq. 7 , which doesn’t require a labeled set L L .

[252] h6: Lemma S19 .

[253] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any predictor f ∈ ℋ f\in\calH , for any loss ℓ : ℝ C × 𝒴 → [ 0 , 1 ] \ell:\R^{C}\times\calY\to[0,1] , for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − 2 ​ δ 1-2\delta over the draw of L ∼ 𝒟 m L\sim\calD^{m} and a set of V V predictors h 1 , … , h V ∼ Q h_{1},\ldots,h_{V}\sim Q , where Q Q is a dataset-dependent posterior distribution over ℋ \calH , we have

[254] table: ℒ 𝒟 ⁡ ( f ) ≤ 𝔼 h ∼ Q ℒ 𝒟 ​ ( h ) + λ ℓ ​ kl − 1 ​ ( kl − 1 ​ ( 1 V ​ ∑ i = 1 V 1 λ ℓ ​ d L ​ ( f , h i ) , 1 V ​ log ⁡ 1 δ ) , 1 m ​ log ⁡ 1 δ ) . \calL_{\calD}(f)\leq\E_{h\sim Q}\calL_{\calD}(h)+\lambda_{\ell}\mathrm{kl}^{-1}\quantity(\kl^{-1}\qty( \frac{1}{V}\sum_{i=1}^V\frac{1}{\lambda_{\ell}}d_L(f,h_i), \frac{1}{V}\log\frac{1}{\delta}), \frac{1}{m}\log\frac{1}{\delta}).

[255] h6: Proof.

[256] p: When computing Theorem 6 for a Gaussian distribution Q Q over the predictors, we cannot compute exactly the term

[257] table: 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) \E_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h)

[258] p: as the expectation doesn’t have a closed form. However, similarly to Theorem S15 , we can upper-bound it. Instead of using the two-sided Chernoff bound as in Langford and Caruana [2001] , Pérez-Ortiz et al. [2021] , we use the one-sided Chernoff bound [ Foong et al., 2022 ] , as we are explicitly interested in an upper bound.

[259] p: With X i = 1 λ ℓ ​ d L ​ ( f , h i ) X_{i}=\frac{1}{\lambda_{\ell}}d_{L}(f,h_{i}) and p = 𝔼 [ X i ] = 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) p=\E[X_{i}]=\E_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h) , with probability at least 1 − δ 1-\delta over the sampling of h 1 , … , h V ∼ Q h_{1},\ldots,h_{V}\sim Q , we have

[260] table: 𝔼 h ∼ Q 1 λ ​ d L ​ ( f , h ) ≤ kl − 1 ​ ( 1 V ​ ∑ i = 1 V 1 λ ℓ ​ d L ​ ( f , h i ) , 1 V ​ log ⁡ 1 δ ) . \E_{h\sim Q}\frac{1}{\lambda}d_{L}(f,h)\leq\mathrm{kl}^{-1}\quantity( \frac{1}{V}\sum_{i=1}^V\frac{1}{\lambda_{\ell}}d_L(f,h_i), \frac{1}{V}\log\frac{1}{\delta}).

[261] p: Using the fact that the inverse of the kl \mathrm{kl} is increasing in its first argument, we have

[262] table: kl − 1 ​ ( 𝔼 h ∼ Q 1 λ ℓ ​ d L ​ ( f , h ) , 1 m ​ log ⁡ 1 δ ) ≤ kl − 1 ​ ( kl − 1 ​ ( 1 V ​ ∑ i = 1 V 1 λ ℓ ​ d L ​ ( f , h i ) , 1 V ​ log ⁡ 1 δ ) , 1 m ​ log ⁡ 1 δ ) . \mathrm{kl}^{-1}\quantity( \E_{h \sim Q}\frac{1}{\lambda_{\ell}}d_L(f,h), \frac{1}{m}\log\frac{1}{\delta})_{h\sim Q}\frac{1}{\lambda_{\ell}}d_{L}(f,h),\frac{1}{m}\log\frac{1}{\delta}\leq\mathrm{kl}^{-1}\quantity(\kl^{-1}\qty( \frac{1}{V}\sum_{i=1}^V\frac{1}{\lambda_{\ell}}d_L(f,h_i), \frac{1}{V}\log\frac{1}{\delta}), \frac{1}{m}\log\frac{1}{\delta}). (8)

[263] p: We finish the proof with a union bound with Theorem 6 and Equation 8 . ∎

[264] h6: Theorem S20 .

[265] p: For any distribution 𝒟 \calD over 𝒳 × 𝒴 \calX\times\calY , for any predictor f ∈ ℋ f\in\calH , for any set ℋ \calH of predictors h : 𝒳 → 𝒴 h:\calX\to\calY , for any loss ℓ : ℝ C × 𝒴 → [ 0 , 1 ] \ell:\R^{C}\times\calY\to[0,1] , for any dataset-independent prior distribution P P on ℋ \calH , for any δ ∈ ( 0 , 1 ] \delta\in(0,1] , with probability at least 1 − 4 ​ δ 1-4\delta over the draw of S ∼ 𝒟 n S\sim\calD^{n} , L ∼ 𝒟 m L\sim\calD^{m} and a set of 2 ​ V 2V predictors h 1 , … , h 2 ​ V ∼ Q h_{1},\ldots,h_{2V}\sim Q , where Q Q is a dataset-dependent posterior distribution over ℋ \calH , we have

[266] table: ℒ 𝒟 ⁡ ( f ) \displaystyle\calL_{\calD}(f) ≤ B ℓ + λ ℓ ​ kl − 1 ​ ( kl − 1 ​ ( 1 V ​ ∑ i = 1 V ℒ ^ S ⁡ ( h i ) − B ℓ λ ℓ , 1 V ​ log ⁡ 1 δ ) , 1 n ​ [ KL ( 𝒬 S | | 𝒫 ) + ln ( 2 ​ n δ ) ] ) \displaystyle\leq B_{\ell}+\lambda_{\ell}\mathrm{kl}^{-1}\mathrm{kl}^{-1}\quantity(\kl^{-1}\qty(\frac{1}{V}\sum_{i=1}^V\frac{\hatL_{S}(h_i) - B_{\ell}}{\lambda_{\ell}}, \frac{1}{V}\log\frac{1}{\delta} ), \frac{1}{n} \qty[\KL(\posterior_S ||\prior) + \ln\qty(\frac{2\sqrt{n}}{\delta})]),\frac{1}{n}\mathrm{KL}(\quantity[\KL(\posterior_S ||\prior) + \ln\qty(\frac{2\sqrt{n}}{\delta})]_{S}||\prior)+\ln\quantity(\frac{2\sqrt{n}}{\delta}) + λ ℓ ​ kl − 1 ​ ( kl − 1 ​ ( 1 V ​ ∑ i = V + 1 2 ​ V 1 λ ℓ ​ d L ​ ( f , h i ) , 1 V ​ log ⁡ 1 δ ) , 1 m ​ log ⁡ 1 δ ) . \displaystyle+\lambda_{\ell}\mathrm{kl}^{-1}\quantity(\kl^{-1}\qty( \frac{1}{V}\sum_{i=V+1}^{2V}\frac{1}{\lambda_{\ell}}d_L(f,h_i), \frac{1}{V}\log\frac{1}{\delta}), \frac{1}{m}\log\frac{1}{\delta}).

[267] h6: Proof.

[268] p: This result simply stems from the union bound of Theorem S15 and Lemma S19 . We remove the factor of 2 2 in the 1 m ​ log ⁡ 2 δ \frac{1}{m}\log\frac{2}{\delta} by using the one-sided Chernoff bound, similarly to the proof of Lemma S19 . ∎

[269] h3: C.3 Using other comparator functions

[270] p: Up until now, all the results are presented with the inverse of the kl \mathrm{kl} . This function gives the tightest bounds, but the bounds obtained with this function are not intuitive. For example, it might be beneficial to use a bound with an analytical upper bound such as the quadratic loss Δ 2 ​ ( q , p ) = 2 ​ ( q − p ) 2 \Delta_{2}(q,p)=2(q-p)^{2} or Catoni’s distance Δ C ​ ( q , p ) = − ln ⁡ ( 1 − p ⁡ ( 1 − e − C ) ) − C ​ q \Delta_{C}(q,p)=-\ln(1-p(1-e^{-C}))-Cq . Both are upper-bounded by kl ⁡ ( q , p ) \mathrm{kl}(q,p) , which can be proven by Pinsker’s inequality for the quadratic loss and Proposition 2.1 of [ Germain et al., 2009 ] for Catoni’s distance.

[271] h6: Lemma S21 .

[272] p: If Δ ⁡ ( q , p ) ≤ kl ⁡ ( q , p ) ​ ∀ q , p ∈ [ 0 , 1 ] \Delta(q,p)\leq\mathrm{kl}(q,p)\forall q,p\in[0,1] , for any ϵ > 0 \epsilon>0 , we have kl − 1 ​ ( q , ϵ ) ≤ Δ − 1 ​ ( q , ϵ ) \mathrm{kl}^{-1}(q,\epsilon)\leq\Delta^{-1}(q,\epsilon) .

[273] h6: Proof.

[274] p: For any comparator function, we have

[275] table: Δ − 1 ​ ( q , ϵ ) \displaystyle\Delta^{-1}(q,\epsilon) = arg sup 0 ≤ p ≤ 1 { Δ ( q , p ) ≤ ϵ } \displaystyle={\arg\sup}_{0\leq p\leq 1}\left\{\Delta(q,p)\leq\epsilon\right\} = arg sup q ≤ p ≤ 1 { Δ ( q , p ) ≤ ϵ } . \displaystyle={\arg\sup}_{q\leq p\leq 1}\left\{\Delta(q,p)\leq\epsilon\right\}.

[276] p: Indeed, for most Δ \Delta , there exists two solutions, one where p ≤ q p\leq q and one where q ≤ p q\leq p . Obviously, as we take the arg-supremum, the second solution is always chosen. Thus, we consider only q ≤ p ≤ 1 q\leq p\leq 1 .

[277] p: Let p 1 = kl − 1 ​ ( q , ϵ ) p_{1}=\mathrm{kl}^{-1}(q,\epsilon) be the solution such that kl ⁡ ( q , p 1 ) = ϵ \mathrm{kl}(q,p_{1})=\epsilon . Let p 2 = Δ − 1 ​ ( q , ϵ ) p_{2}=\Delta^{-1}(q,\epsilon) be the solution such that Δ ⁡ ( q , p 2 ) = ϵ \Delta(q,p_{2})=\epsilon . From the assumption that Δ ⁡ ( q , p ) ≤ kl ⁡ ( q , p ) ​ ∀ q , p ∈ [ 0 , 1 ] \Delta(q,p)\leq\mathrm{kl}(q,p)\forall q,p\in[0,1] , we have

[278] table: kl ⁡ ( q , p 1 ) = Δ ⁡ ( q , p 2 ) = ϵ ∧ Δ ⁡ ( q , p 1 ) ≤ kl ⁡ ( q , p 1 ) ⟹ Δ ⁡ ( q , p 1 ) ≤ Δ ⁡ ( q , p 2 ) . \displaystyle\mathrm{kl}(q,p_{1})=\Delta(q,p_{2})=\epsilon\land\Delta(q,p_{1})\leq\mathrm{kl}(q,p_{1})\implies\Delta(q,p_{1})\leq\Delta(q,p_{2}).

[279] p: As Δ ⁡ ( q , p ) \Delta(q,p) is increasing for p ≥ q p\geq q , we have that :

[280] table: Δ ⁡ ( q , p 1 ) ≤ Δ ⁡ ( q , p 2 ) ⟹ p 1 ≤ p 2 ⟹ kl − 1 ​ ( q , ϵ ) ≤ Δ − 1 ​ ( q , ϵ ) . \Delta(q,p_{1})\leq\Delta(q,p_{2})\implies p_{1}\leq p_{2}\implies\mathrm{kl}^{-1}(q,\epsilon)\leq\Delta^{-1}(q,\epsilon).

[281] p: ∎

[282] h2: Appendix D EXPERIMENTS

[283] h5: Devices.

[284] p: The experiments were run on three different devices. The target neural networks, the experiments with Pick-To-Learn and the quantization experiments were computed on a computer with Python 3.12.3 and a NVIDIA GeForce RTX 4090. The coreset experiments and the model compression experiments were computed with Python 3.12.4 and a NVidia H100 SXM5. Finally, the PAC-Bayesian experiments and the model distillation experiments were computed with Python 3.12.4 and a NVidia A100 SXM4.

[285] h5: Libraries.

[286] p: All libraries used can be found within the code. Notably, we use DeepCore [ Guo et al., 2022 ] (MIT license), PACTL [ Lotfi et al., 2022 ] (Apache 2.0 License), PAC-Bayes with Backprop [ Pérez-Ortiz et al., 2021 ] (CC-BY 4.0 License), PyTorch [ Ansel et al., 2024 ] (BSD 3-Clause License), Lightning [ Falcon and The PyTorch Lightning team, 2019 ] (Apache 2.0 license), Loralib [ Hu et al., 2022 ] (MIT License), Transformers [ Wolf et al., 2020 ] (Apache 2.0 License), Scikit-Learn [ Pedregosa et al., 2011 ] (BSD 3-Clause License), NumPy [ Harris et al., 2020 ] (NumPy license), Weight and Biases [ Biewald, 2020 ] (MIT License), ScheduleFree [ Defazio et al., 2024 ] (Apache 2.0 License), TorchAO [ Or et al., ] (BSD 3-Clause License). We also use the KL inversion function of [ Viallard et al., 2021 ] , which is distributed under MIT License.

[287] h5: Datasets.

[288] p: The datasets used are the MNIST dataset [ LeCun et al., 1998 ] (MIT License), the CIFAR10 dataset [ Krizhevsky et al., 2009 ] and the Amazon polarity dataset [ Zhang et al., 2015 ] (Apache 2.0 License). There is no explicit license for CIFAR10, but the authors simply ask the user to cite this technical report : Krizhevsky et al. [2009] .

[289] h3: D.1 Target model

[290] p: For MNIST, the models were trained using data-augmentation for 200 epochs or until the validation error hasn’t decreased for 10 epochs. For CIFAR10, the model was trained for 200 epochs. The models on Amazon polarity are trained for 10 epochs or until the validation error hasn’t decreased for 2 epochs. The models for MNIST and CIFAR10 are randomly initialized, but for Amazon polarity the models are initialized with the pretrained weights from the Transformers library [ Wolf et al., 2020 ] . In some experiments, to remove the need for learning rate scheduling, we try the optimizers SGDFree and AdamFree from the ScheduleFree library [ Defazio et al., 2024 ] or the COCOB optimizer from Orabona and Tommasi [2017] . Other times, we use the OneCycle learning rate scheduler [ Smith and Topin, 2019 ] implemented in PyTorch.

[291] p: We present the hyperparameter grids used for each problem.

[292] p: Hyperparameters for MNIST

[293] p: Dropout probability : { 0.2 , 0.5 } \{0.2,0.5\}

[294] p: Optimizer : { \{ Adam, AdamFree, COCOB } \}

[295] p: Training learning rate : { 10 − 3 , 10 − 4 } \{10^{-3},10^{-4}\}

[296] p: Weight decay : { 0.1 , 0.01 , 0.001 } \{0.1,0.01,0.001\}

[297] p: Hyperparameters for CIFAR10

[298] p: Model type : { \{ CNN, ResNet18 } \}

[299] p: Dropout probability : 0.0

[300] p: Optimizer : SGD

[301] p: Learning rate scheduler : OneCycle

[302] p: Training learning rate : { 0.05 , 0.01 , 0.005 } \{0.05,0.01,0.005\}

[303] p: Weight decay : { 10 − 3 , 10 − 4 } \{10^{-3},10^{-4}\}

[304] p: Hyperparameters for Amazon polarity

[305] p: Model type : { \{ DistilBERT, GPT2 } \}

[306] p: Max epochs : 2

[307] p: Dropout probability : 0.0

[308] p: Optimizer : SGD

[309] p: Learning rate scheduler : OneCycle

[310] p: Training learning rate : 2 × 10 − 5 2\times 10^{-5}

[311] h3: D.2 Partition-based bounds

[312] p: We compute the bound both for the bounded cross-entropy loss and the zero-one loss for all of our target models. For each model and for each loss, we do a grid-search over the following hyperparameters :

[313] p: Number of subsets K K : [5, 10, 20, 50, 100, 200]

[314] p: α \alpha = [ 20 , 50 , 100 , n ⁡ ( K + n ) K ⁡ ( 4 ​ n − 3 ) ] [20,50,100,\frac{n(K+n)}{K(4n-3)}]

[315] p: Given one hyperparameter combination, we choose γ = ( δ 2 ) − 1 α \gamma=(\frac{\delta}{2})^{\frac{-1}{\alpha}} such that the bound holds in 1 − γ − α − δ 2 = 1 − ( ( δ 2 ) − 1 α ) − α − δ 2 = 1 − δ 1-\gamma^{-\alpha}-\frac{\delta}{2}=1-((\frac{\delta}{2})^{\frac{-1}{\alpha}})^{-\alpha}-\frac{\delta}{2}=1-\delta with δ = 0.01 \delta=0.01 . We use a union bound over the 24 combinations of the grid-search to get a bound that holds simultaneously for all possibilities.

[316] h4: D.2.1 Ablation study on the partitioning method

[317] p: To compute their bound, Than and Phan [2025] partitions the space using a K-means clustering applied to the training set. However, to the best of our knowledge, this choice of data-dependent partition seems to violate the statement of their theorem. To compute the bound, we try two techniques : computing the partition on the unlabeled disagreement set and using random clusters. As their bound doesn’t consider unlabeled datapoints, the disagreement approach is completely valid. However, this is not the setting of the original paper. For the random clusters, we sample K K centroids from a uniform distribution and assign the datapoints to the cluster of the closest centroid. We repeat this experiments five times and consider the best cluster.

[318] figure: (a) Zero-one loss (b) Smoothed cross-entropy loss Figure S1 : Comparison of the different approaches to compute the partition-based bounds. We consider 5 different seeds for the random clusters.

[319] p: Although the train set cluster and the disagreement set cluster were obtained using different datasets, they are almost identical. Moreover, we can see that in their setting (without a disagreement set), the only valid option is to use random clusters, which leads to vacuous generalization bounds. Surprisingly enough, the bounds are actually worse on MNIST than CIFAR10.

[320] h3: D.3 Norm-based bounds

[321] p: We compute the bound of Theorem S5 for each target model by adapting the code provided by [ Galanti et al., 2023b ] . As suggested in the paper, we use γ = 1 \gamma=1 .

[322] h3: D.4 Sample compression experiments

[323] p: We use the Pick-To-Learn with Early Stopping [ Marks and Paccagnan, 2025 ] implementation of Bazinet et al. [2025] . We use the coreset methods implemented by the DeepCore library [ Guo et al., 2022 ] . All approach use Theorem S9 for the zero-one loss and Theorem S13 for the cross-entropy loss. The exceptions include Pick-To-Learn with the zero-one loss, as Pick-To-Learn enjoys the tight generalization bounds of Theorem S10 , for which it was designed. The other exception is the Random Coreset approach, which can be used with the following test set bounds : Theorem S8 for the zero-one loss and Theorem S12 for the cross-entropy loss.

[324] p: Let 𝒞 : ∪ 1 ≤ n ≤ ∞ ( 𝒳 × 𝒴 ) n → ∪ m ≤ n ( 𝒳 × 𝒴 ) m \mathscr{C}:\cup_{1\leq n\leq\infty}(\calX\times\calY)^{n}\to\cup_{m\leq n}(\calX\times\calY)^{m} denote some coreset method that takes a dataset S S and returns a compression set S 𝐢 S_{\bfi} . Let SGD \mathrm{SGD} denote stochastic gradient descent. Then, we can apply the sample compression bounds for the predictors outputted by A : SGD ∘ 𝒞 A:\mathrm{SGD}\circ\mathscr{C} with the compression set S 𝐢 = 𝒞 ⁡ ( S ) S_{\bfi}=\mathscr{C}(S) and the reconstruction function ℛ = SGD \scriptR=\mathrm{SGD} . Then, we have proven that A ⁡ ( S ) = ℛ ⁡ ( S 𝐢 ) = SGD ⁡ ( 𝒞 ⁡ ( S ) ) A(S)=\scriptR(S_{\bfi})=\mathrm{SGD}(\mathscr{C}(S)) .

[325] p: We present the hyperparameter grids.

[326] p: Hyperparameters for P2L on MNIST

[327] p: Dropout probability : { 0.2 , 0.5 } \{0.2,0.5\}

[328] p: Optimizer : { \{ Adam, AdamFree } \}

[329] p: Training learning rate : { 10 − 3 , 10 − 4 } \{10^{-3},10^{-4}\}

[330] p: Weight decay : { 0.01 , 0.1 } \{0.01,0.1\}

[331] p: Smoothing parameter α \alpha : { 10 − 3 , 10 − 4 , 10 − 5 } \{10^{-3},10^{-4},10^{-5}\}

[332] p: Softmax : { \{ Smoothed, Clamped } \}

[333] p: Hyperparameters for P2L on CIFAR10

[334] p: Model type : { \{ CNN, ResNet18 } \}

[335] p: Dropout probability : 0.5

[336] p: Optimizer : { \{ SGD, SGDFree } \}

[337] p: Training learning rate : { 0.05 , 0.01 , 0.005 } \{0.05,0.01,0.005\}

[338] p: Weight decay : { 10 − 3 , 10 − 4 } \{10^{-3},10^{-4}\}

[339] p: Smoothing parameter α \alpha : { 10 − 3 , 10 − 4 , 10 − 5 } \{10^{-3},10^{-4},10^{-5}\}

[340] p: Softmax : { \{ Smoothed, Clamped } \}

[341] p: Hyperparameters for coresets on MNIST

[342] p: Dropout probability : { 0.2 , 0.5 } \{0.2,0.5\}

[343] p: Coreset method : { \{ Random Coreset, k-Center Greedy, Forgetting, DeepFool } \}

[344] p: Percentage of dataset used as coreset : { 0.1 % , 0.5 % , 1 % , 5 % , 10 % , 15 % , 20 % } \{0.1\%,0.5\%,1\%,5\%,10\%,15\%,20\%\}

[345] p: Optimizer : { \{ Adam, AdamFree } \}

[346] p: Training learning rate : { 10 − 3 , 10 − 4 } \{10^{-3},10^{-4}\}

[347] p: Weight decay : { 0.01 , 0.1 } \{0.01,0.1\}

[348] p: Smoothing parameter α \alpha : { 10 − 3 , 10 − 4 , 10 − 5 } \{10^{-3},10^{-4},10^{-5}\}

[349] p: Softmax : { \{ Smoothed, Clamped } \}

[350] p: Hyperparameters for coresets on CIFAR10

[351] p: Model type : ResNet18

[352] p: Dropout probability : 0.5

[353] p: Coreset method : { \{ Random Coreset, k-Center Greedy, Forgetting, DeepFool } \}

[354] p: Percentage of dataset used as coreset : { 0.1 % , 0.5 % , 1 % , 5 % , 10 % , 15 % , 20 % , 30 % , 40 % , 50 % } \{0.1\%,0.5\%,1\%,5\%,10\%,15\%,20\%,30\%,40\%,50\%\}

[355] p: Optimizer : { \{ SGD, SGDFree } \}

[356] p: Training learning rate : { 0.01 , 0.05 } \{0.01,0.05\}

[357] p: Weight decay : 5 × 10 − 4 5\times 10^{-4}

[358] p: Smoothing parameter α \alpha : { 10 − 3 , 10 − 4 } \{10^{-3},10^{-4}\}

[359] p: Softmax : { \{ Smoothed, Clamped } \}

[360] p: We report the results for the sample compression experiments on CIFAR10 in the following Fig. S2 .

[361] figure: Figure S2 : Illustration of the behavior of our disagreement bounds on CIFAR10 using sample-compression methods.

[362] h4: D.4.1 Ablation study for the bounded cross-entropy loss

[363] p: To choose which hyperparameter to use for the bounded cross-entropy loss, we compare the average cross-entropy loss obtained over all the combinations of hyperparameters for the coreset methods. After computing all possible values, we take the mean over all dimensions except the smoothing parameter α \alpha and the softmax type : clamped or smoothed. We report the results in Fig. S3 .

[364] p: For both experiments, the optimal parameter seems to be α = 10 − 3 \alpha=10^{-3} . The gap between all values of α \alpha are not significative, as their standard deviation overlaps. However, on the 448 combinations of hyperparameters for MNIST (with 5 seeds per combinations) and 320 combinations for CIFAR10 (with 5 seeds per combinations), it seems like the parameter α = 10 − 3 \alpha=10^{-3} leads to the best result. As for the type of softmax, the smoothed softmax seems to lead to slightly better results. Thus, we choose the smoothed softmax with α = 10 − 3 \alpha=10^{-3} in all other experiments.

[365] figure: (a) MNIST (b) CIFAR10 Figure S3 : Ablation study on the hyperparameters of the bounded cross-entropy loss. We report the mean of the cross-entropy loss over all coreset methods experiments.

[366] h3: D.5 Model compression experiments

[367] p: For the model compression experiments, we pretrain randomly initialized models on a subset of the training set, over which we then add LoRA adapters implemented by Hu et al. [2022] and the subspace compression approach implemented by Lotfi et al. [2022] . This SubLoRA model is then trained on the remaining datapoints, where the bound is also computed.

[368] p: Hyperparameters for MNIST

[369] p: Portion of training set for pretraining : 20%

[370] p: Number of pretraining epochs : 100

[371] p: Pretraining learning rate : 10 − 3 10^{-3}

[372] p: Dropout probability : 0.0

[373] p: Optimizer : AdamFree

[374] p: Training learning rate : { 10 − 2 , 10 − 4 } \{10^{-2},10^{-4}\}

[375] p: Weight decay : 0.1

[376] p: Random subspace projector : Dense

[377] p: Dimension of the subspace : { 100,500 , 1000 } \{100,500,1000\}

[378] p: Level of quantization : { 5 , 20 } \{5,20\}

[379] p: Rank of LoRA : { 0 , 2 , 4 } \{0,2,4\}

[380] p: Hyperparameters for CIFAR10

[381] p: Portion of pretraining set : 50%

[382] p: Number of pretraining epochs : 150

[383] p: Pretraining learning rate : 0.05

[384] p: Dropout probability : 0.2

[385] p: Optimizer : SGD

[386] p: Learning rate scheduler : OneCycle

[387] p: Training learning rate : { 0.01 , 0.005 } \{0.01,0.005\}

[388] p: Max epochs : { 500 , 1000 } \{500,1000\}

[389] p: Weight decay : 10 − 4 10^{-4}

[390] p: Random subspace projector : { \{ Dense, Rounded Double Kronecker } \}

[391] p: Dimension of the subspace : { 100,500 } \{100,500\}

[392] p: Level of quantization : { 5 , 10 , 20 } \{5,10,20\}

[393] p: Rank of LoRA : { 0 , 2 , 4 } \{0,2,4\}

[394] p: We report the results for the cross-entropy loss on both MNIST and CIFAR10 in Table S2 .

[395] figure: Table S2 : Generalization bounds on the smoothed cross-entropy loss achieved on MNIST and CIFAR10 using model compression bounds. Dataset Surrogate model Target model Test loss Size (KB) MC Bound Test loss Our bound MNIST 0.0273 ± \pm 0.0015 0.0356 ± \pm 0.0008 0.1338 ± \pm 0.0040 0.0150 ± \pm 0.0006 0.1756 ± \pm 0.0041 CIFAR10 0.7005 ± \pm 0.0243 0.0336 ± \pm 0.0014 1.0978 ± \pm 0.0195 0.2247 ± \pm 0.0060 1.7851 ± \pm 0.0223

[396] h3: D.6 PAC-Bayes experiments

[397] p: For the PAC-Bayes experiments, we pretrain randomly initialized models on a subset of the training set. We then add Gaussian distributions over each weight, with learnable mean and standard deviation parameters. The stochastic model is then trained on the remaining datapoints, where the bound is also computed.

[398] figure: Table S3 : Generalization bounds on the smoothed cross-entropy loss achieved on MNIST and CIFAR10 using PAC-Bayes bounds. Dataset Surrogate model Target model Test loss KL \mathrm{KL} PB Bound Test loss Our bound MNIST 0.0286 ± \pm 0.0030 0.7425 ± \pm 0.1188 0.1235 ± \pm 0.0059 0.0150 ± \pm 0.0006 0.2592 ± \pm 0.0087 CIFAR10 0.5440 ± \pm 0.0568 1.6239 ± \pm 0.9202 0.7404 ± \pm 0.0744 0.2247 ± \pm 0.0060 1.4204 ± \pm 0.1377

[399] p: Hyperparameters for MNIST

[400] p: Portion of pretraining set : 20%

[401] p: Number of pretraining epochs : 100

[402] p: Pretraining learning rate : 10 − 3 10^{-3}

[403] p: Dropout probability : 0.0

[404] p: Optimizer : Adam

[405] p: Training learning rate : { 10 − 3 , 5 × 10 − 3 , 10 − 4 } \{10^{-3},5\times 10^{-3},10^{-4}\}

[406] p: Weight decay : { 0.01 , 0.1 } \{0.01,0.1\}

[407] p: Smoothing parameter α \alpha : 10 − 3 10^{-3}

[408] p: Softmax : { \{ Smoothed, Clamped } \}

[409] p: Standard deviation of prior : { 10 − 2 , 5 × 10 − 2 , 10 − 3 , 10 − 4 } \{10^{-2},{5\times 10^{-2}},10^{-3},10^{-4}\}

[410] p: Number of Monte Carlo sampling : 2000

[411] p: Hyperparameters for CIFAR10

[412] p: Portion of pretraining set : { 60 % , 70 % } \{60\%,70\%\}

[413] p: Number of pretraining epochs : 150

[414] p: Pretraining learning rate : 0.05 0.05

[415] p: Dropout probability : 0.2

[416] p: Optimizer : SGD

[417] p: Training learning rate : { 10 − 3 , 5 × 10 − 3 , 10 − 4 } \{10^{-3},5\times 10^{-3},10^{-4}\}

[418] p: Weight decay : 10 − 4 10^{-4}

[419] p: Smoothing parameter α \alpha : 10 − 3 10^{-3}

[420] p: Softmax : { \{ Smoothed, Clamped } \}

[421] p: Standard deviation of prior : { 10 − 2 , 5 × 10 − 2 , 10 − 3 , 10 − 4 } \{10^{-2},{5\times 10^{-2}},10^{-3},10^{-4}\}

[422] p: Number of Monte Carlo sampling : 5000

[423] figure: Table S4 : Generalization bounds on the zero-one loss achieved via model distillation on Amazon polarity using model compression (MC) bounds. All metrics presented are in percents (%), except the size. Model Surrogate model Target model Test error Size (KB) MC Bound Test error Our bound DistilBERT 7.61 ± \pm 0.07 2.02 ± \pm 0.01 14.37 ± \pm 0.08 6.19 ± \pm 0.15 21.35 ± \pm 0.32 GPT2 16.37 ± \pm 0.94 2.04 ± \pm 0.43 25.05 ± \pm 0.91 5.51 ± \pm 0.11 43.34 ± \pm 1.52

[424] h3: D.7 Model distillation on Amazon polarity

[425] p: We start with DistilBERT and GPT2 with the pretrained weights of the Transformers library. We freeze the model and apply a SubLoRA model on the top half of the model. For the adaptative quantization, we use the implementation of Lotfi et al. [2022] , a learning rate of 10 − 2 10^{-2} for DistilBERT and a learning rate of 10 − 4 10^{-4} for GPT2. We produce pseudo-labels for the unlabeled using the target model and train the model to classify correctly both the labeled set S S and the unlabeled set U U with the pseudo-labels.

[426] p: Max epochs : 5

[427] p: Dropout probability : 0.0

[428] p: Optimizer : Adam

[429] p: Training learning rate : 10 − 6 10^{-6}

[430] p: Weight decay : 0.01 0.01

[431] p: Dimension of the subspace : { 5000 , 10000 } \{5000,10000\}

[432] p: Level of quantization : 250

[433] p: Rank of LoRA : 4

[434] h3: D.8 Quantization experiments on Amazon polarity

[435] p: We use the target models and quantize them following this hyperparameter grid. We do not consider the quantization-aware training with 2 bits, as both TorchAO and AO did not consider this setting.

[436] p: Max epochs : 2

[437] p: Dropout probability : 0.0

[438] p: Optimizer : Adam

[439] p: Training learning rate : 10 − 6 10^{-6}

[440] p: Weight decay : 0.01 0.01

[441] p: Number of bits : { 2 , 4 , 8 } \{2,4,8\}

[442] p: Quantization-aware training : { \{ Yes, No } \}

[443] p: Delta for the Huber loss : 0.2

[444] h2: Instructions for reporting errors

[445] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[446] p: Tip: You can select the relevant text first, to include it in your report.

[447] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[448] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
