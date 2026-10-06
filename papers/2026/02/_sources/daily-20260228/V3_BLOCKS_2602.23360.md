[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Model Agreement via Anchoring

[3] h6: Abstract

[4] p: Numerous lines of aim to control model disagreement — the extent to which two machine learning models disagree in their predictions. We adopt a simple and standard notion of model disagreement in real-valued prediction problems, namely the expected squared difference in predictions between two models trained on independent samples, without any coordination of the training processes. We would like to be able to drive disagreement to zero with some natural parameter(s) of the training procedure using analyses that can be applied to existing training methodologies.

[5] p: We develop a simple general technique for proving bounds on independent model disagreement based on anchoring to the average of two models within the analysis. We then apply this technique to prove disagreement bounds for four commonly used machine learning algorithms: (1) stacked aggregation over an arbitrary model class (where disagreement is driven to 0 with the number of models k k being stacked) (2) gradient boosting (where disagreement is driven to 0 with the number of iterations k k ) (3) neural network training with architecture search (where disagreement is driven to 0 with the size n n of the architecture being optimized over) and (4) regression tree training over all regression trees of fixed depth (where disagreement is driven to 0 with the depth d d of the tree architecture). For clarity, we work out our initial bounds in the setting of one-dimensional regression with squared error loss — but then show that all of our results generalize to multi-dimensional regression with any strongly convex loss.

[6] h2: 1 Introduction

[7] p: Two predictive models f 1 , f 2 : 𝒳 → ℝ f_{1},f_{2}:\mathcal{X}\rightarrow\mathbb{R} , trained on data sampled from the same distribution 𝒟 \mathcal{D} , might frequently disagree in the sense that on a typical test example x ∼ 𝒟 x\sim\mathcal{D} , f 1 ​ ( x ) f_{1}(x) and f 2 ​ ( x ) f_{2}(x) take very different values. In fact, this can happen even when the two models are trained on the same dataset, if the model class is not convex and the training process is stochastic. This kind of model disagreement , sometimes known as model or predictive multiplicity ( Marx et al., 2020 ; Black et al., 2022 ; Roth and Tolbert, 2025 ) or the Rashomon effect ( Breiman, 2001 ) , is a concern for many different reasons. Pragmatically, predictions are used to inform downstream actions, and two models that make different predictions produce ambiguity about which is the best action to take when we can only take one. This has led to a literature on how two predictive models (or a predictive model and a human) can engage in short test-time interactions so as to “agree” on a single prediction or action that is more accurate than either model could have made alone ( Aumann, 1976 ; Aaronson, 2005 ; Donahue et al., 2022 ; Frongillo et al., 2023 ; Peng et al., 2025 ; Collina et al., 2025 ; Collina et al., 2026 ) . In industrial applications, this same phenomenon is known as model or predictive churn ; there is a large body of work that aims to reduce it, because churn for predictions in ways that do not produce accuracy improvements can needlessly disrupt downstream pipelines built around an initial model ( Milani Fard et al., 2016 ; Bahri and Jiang, 2021 ; Hidey et al., 2022 ; Watson-Daniels et al., 2024 ) . The phenomenon of predictive multiplicity has led to concern about the potential arbitrariness of decisions informed by statistical models, and hence the procedural fairness of using such models in high-stakes settings Marx et al. (2020) ; Black et al. (2022) ; Watson-Daniels et al. (2024) . The same phenomenon is what underlies the desire for replicability of machine learning algorithms, which has recently attracted widespread study ( Impagliazzo et al., 2022 ; Bun et al., 2023 ; Eaton et al., 2023 ; Kalavasis et al., 2024b ; Kalavasis et al., 2024a ; Karbasi et al., 2023 ; Diakonikolas et al., 2025 ; Eaton et al., 2026 ) .

[8] p: In this paper we ask when training on independent samples from a common distribution results in models that approximately agree on most inputs. Unlike the (model) agreement literature ( Aumann, 1976 ; Aaronson, 2005 ; Collina et al., 2025 ) we want approximate agreement “out of the box”, without the need for any test-time interaction or coordination. And unlike the literature on replicability ( Impagliazzo et al., 2022 ; Bun et al., 2023 ; Eaton et al., 2023 ; Karbasi et al., 2023 ) , we do not want our analyses to apply only to custom-designed (and often impractical) algorithms: we want methods for analyzing existing families of practical learning algorithms. We continue a discussion of additional related work in Section 1.3 .

[9] h3: 1.1 Our Results

[10] p: Our notion of approximate model agreement is that the expected squared difference between two models f 1 f_{1} and f 2 f_{2} should be small: D ⁡ ( f 1 , f 2 ) := 𝔼 x ∼ P ​ [ ( f 1 ​ ( x ) − f 2 ​ ( x ) ) 2 ] ≤ ε D(f_{1},f_{2}):=\mathbb{E}_{x\sim P}[(f_{1}(x)-f_{2}(x))^{2}]\leq\varepsilon . Our goal is to show that for broad classes of model training methods, this disagreement level ε \varepsilon can be driven to 0 0 with some tunable parameter of the method. We aim for high agreement in this sense via independent training, i.e., without the need for any interaction or coordination between the learners beyond the fact that they are sampling data from a common distribution. We give an abstract recipe for establishing guarantees like this based on a “midpoint anchoring argument” and then give four applications of the recipe: (1) to the popular ensembling technique of “stacking”, (2) to gradient boosting and similar methods that iteratively build up linear combinations over a class of base models, (3) to neural network training with architecture search, and (4) to regression tree training over all regression trees of bounded depth. For clarity, we first establish all of our guarantees for models that solve a one dimensional regression problem to optimize for squared loss, but we then show how our results generalize to multi-dimensional strongly convex loss functions. We include our results on these generalizations in Section 6 .

[11] h4: 1.1.1 The Midpoint Anchoring Method

[12] p: Our core technique is built around a simple “midpoint identity” for squared loss. For the sake of completeness, we provide a proof in Section 2 . This identity is a special case ( m = 2 m=2 ) of what is also known as the ambiguity decomposition in the literature Krogh and Vedelsby (1994) ; Jiang et al. (2017) ; Wood et al. (2023) . The decomposition breaks down the average ensemble model’s loss into the average losses of the individual ensemble members and an ‘ambiguity’ term measuring the disagreement of members from the average ensemble. For any two predictors f 1 , f 2 : 𝒳 → ℝ f_{1},f_{2}:\mathcal{X}\rightarrow\mathbb{R} , let f ¯ ​ ( x ) := 1 2 ​ ( f 1 ​ ( x ) + f 2 ​ ( x ) ) \bar{f}(x):=\tfrac{1}{2}(f_{1}(x)+f_{2}(x)) denote the (hypothetical) model corresponding to their average. Then

[13] table: MSE ⁡ ( f ¯ ) = MSE ⁡ ( f 1 ) + MSE ⁡ ( f 2 ) 2 − D ⁡ ( f 1 , f 2 ) 4 . \mathrm{MSE}(\bar{f})=\frac{\mathrm{MSE}(f_{1})+\mathrm{MSE}(f_{2})}{2}-\frac{D(f_{1},f_{2})}{4}.

[14] p: This decomposition is usually used to upper bound the loss of an explicitly realized ensemble model f ¯ \bar{f} . We use it as a way to bound D ⁡ ( f 1 , f 2 ) D(f_{1},f_{2}) :

[15] table: D ⁡ ( f 1 , f 2 ) = 2 ​ ( MSE ⁡ ( f 1 ) + MSE ⁡ ( f 2 ) − 2 ​ MSE ​ ( f ¯ ) ) . D(f_{1},f_{2})\,=\,2\Big(\mathrm{MSE}(f_{1})+\mathrm{MSE}(f_{2})-2\,\mathrm{MSE}(\bar{f})\Big).

[16] p: For us, the ensemble model f ¯ \bar{f} need not ever be realized, except as a thought experiment. The identity reduces proving independent disagreement bounds (the goal of this paper) to bounding the error gap between the constituent models f 1 f_{1} and f 2 f_{2} and their average. If f ¯ \bar{f} lies in the same hypothesis class ℋ \mathcal{H} as f 1 f_{1} and f 2 f_{2} , then this error gap can be bounded by any convergence analysis that establishes that MSE ⁡ ( f ) \mathrm{MSE}(f) will approach error optimality within ℋ \mathcal{H} . More frequently, for non-convex classes, f ¯ \bar{f} will not be representable within the same class of functions as f 1 f_{1} and f 2 f_{2} — but for many natural concept classes, the average of two models trained within some class of models parameterized by a measure of complexity (size, depth) will be representable within a class that is “not much larger”. This will give us stability guarantees in terms of the “local learning curve” of this complexity parameter, which because of error boundedness and monotonicity must tend to zero at values of the complexity parameter that can be bounded independently of the instance.

[17] p: All of our stability bounds are “agnostic” in the sense that they hold without any distributional or realizability assumptions. In other words, our bounds will always follow from the ability to optimize within given model classes, without needing to assume that the model class is able to represent the relationship between the features and the labels to any non-trivial degree.

[18] p: It is instructive at the outset to compare the midpoint anchoring method to a more naive methods for establishing agreement bounds. Any pair of models f 1 f_{1} and f 2 f_{2} that both have almost perfect accuracy in the sense that MSE ​ ( f 1 ) , MSE ​ ( f 2 ) ≤ ε \textrm{MSE}(f_{1}),\textrm{MSE}(f_{2})\leq\varepsilon must also satisfy D ⁡ ( f 1 , f 2 ) ≤ O ⁡ ( ε ) D(f_{1},f_{2})\leq O(\varepsilon) . This follows by anchoring on hypothetical perfect predictions f ∗ ​ ( x ) = y f^{*}(x)=y . Of course, such bounds will rarely apply because very few settings are compatible with near perfect prediction. The benefit of our more general midpoint anchoring method is that it will allow us to argue for independent model agreement without needing to make any realizability assumptions — high accuracy is not needed for high agreement, as if f 1 f_{1} and f 2 f_{2} have high error, so might the average model f ¯ \bar{f} .

[19] h4: 1.1.2 Applications: Ensembling, Boosting, Neural Nets, and Regression Trees

[20] p: We choose our four applications below to show the various ways in which we can apply our method in settings that are progressively more challenging. First, as a warm-up, we study stacked aggregation, which ensembles independently trained models. We show how the midpoint anchoring method can recover strong agreement results as a function of the local error curve .

[21] p: Next, we study gradient boosting. Gradient boosting, like stacking, learns a linear combination of base models, but unlike stacking, does not rely on independently trained models. The models in gradient boosting are found by adaptively and iteratively solving a “weak learning” problem. As our midpoint anchoring method does not rely on model independence, we are still able to use it to recover strong agreement bounds tending to 0 0 at a rate of O ⁡ ( 1 / k ) O(1/k) , where k k is the number of iterations of gradient boosting.

[22] p: The constituent models used in gradient boosting can be arbitrary and non-convex (e.g., depth 5 regression trees), but the aggregation method is still linear and is implicitly approximating a (infinite dimensional) convex optimization problem — minimizing mean squared error amongst linear models in the span of the set of weak learner models. One might wonder if the kind of agreement bounds we are able to prove are implicitly relying on this convexity. In our third and fourth applications, we see that the answer is no. We study error minimization over arbitrary ReLU neural networks of size n n (implying architecture search) as well as arbitrary regression trees of depth d d . These are highly non-convex optimization landscapes. Thus approximate error minimizers can generally be very far from agreement in parameter space. Nevertheless, we are able to apply our midpoint anchoring method to show strong bounds on agreement that can be driven to 0 0 as a function of the size of the neural network n n in the first case and the depth of the regression tree d d in the second case, recovering agreement in prediction space despite arbitrary disagreement in parameter space.

[23] h4: 1.1.3 Warmup: Stacking and Local Training Curve Bounds

[24] p: In Section 3 we apply our recipe to establish the stability of stacking, also known as stacked aggregation or stacked regression. Stacking ( Wolpert, 1992 ; Breiman, 1996 ) is a simple, popular model ensembling technique in which we independently learn k k base models, and then combine them by training a regression model on top of them, using the predictions of the base models as features. To model independent training in reduced form, we imagine that there is a fixed distribution Q Q on models g : 𝒳 → ℝ g:\mathcal{X}\rightarrow\mathbb{R} that a learner can sample from. Sampling a new model g g from Q Q represents the induced distribution on models from (as one example) sampling a fresh dataset D D of some size from the underlying data distribution P P , and then running an arbitrary (possibly randomized) model training procedure on the sample D D . We make no assumptions on the form of the distribution Q Q , and hence no assumptions about the nature of the underlying model training procedure or the underlying model class. A learner samples k k models G = { g 1 , … , g k } G=\{g_{1},\ldots,g_{k}\} independently from Q Q , and then ensembles them by training a linear regression model f 1 f_{1} to minimize squared error, using G G as its feature space. A second independent learner running the same procedure corresponds to sampling a different set of k k models G ′ = { g 1 ′ , … , g k ′ } G^{\prime}=\{g^{\prime}_{1},\ldots,g^{\prime}_{k}\} , also independently from Q Q , and then solving for a linear regression model f 2 f_{2} minimizing squared error using G ′ G^{\prime} as its feature space. Via the midpoint anchoring method we argue that we can quickly drive the model disagreement D ⁡ ( f 1 , f 2 ) D(f_{1},f_{2}) to 0 by increasing k k , the number of models being ensembled. The idea is to compare both f 1 f_{1} and f 2 f_{2} to the model f ∗ f^{*} that is the solution to linear regression on the union of the two feature spaces G ∪ G ′ G\cup G^{\prime} . This model is only more accurate than the anchor model f ¯ \bar{f} , as f ¯ \bar{f} is a (likely suboptimal) function within the same span as f ∗ f^{*} . Moreover, since the base models underlying both f 1 f_{1} and f 2 f_{2} were sampled i.i.d. from a common distribution Q Q , the set of features in G ∪ G ′ G\cup G^{\prime} is exchangeable. Consequently, we can view both f 1 f_{1} and f 2 f_{2} as consisting of the solution to a linear regression problem on a uniformly random subset of half the features available to f ∗ f^{*} . This allows us to argue that as k k gets large, the MSE of f 1 f_{1} and f 2 f_{2} must approach the MSE of f ∗ f^{*} , which in turn lets us drive D ⁡ ( f 1 , f 2 ) D(f_{1},f_{2}) to 0 as a function of k k . Taking the expectation over the models f 1 f_{1} and f 2 f_{2} as well lets us simplify the bound to:

[25] table: 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≤ 4 ​ ( R ¯ k − R ¯ 2 ​ k ) \mathbb{E}_{f_{1},f_{2}}[D(f_{1},f_{2})]\leq 4(\bar{R}_{k}-\bar{R}_{2k})

[26] p: where R ¯ k \bar{R}_{k} and R ¯ 2 ​ k \bar{R}_{2k} represent the expected MSE that result from stacking k k and 2 ​ k 2k models respectively, drawn i.i.d. from Q Q . This relates the stability of f 1 f_{1} and f 2 f_{2} to the local training curve; since R ¯ 1 , R ¯ 2 , … \bar{R}_{1},\bar{R}_{2},\ldots is a monotonically decreasing sequence bounded from above by 𝔼 ⁡ [ y 2 ] \mathbb{E}[y^{2}] and from below by 0 0 , the curve must quickly “level out” at most values, yielding any degree of desired stability.

[27] p: We briefly remark on the “local training curve” form of this result, which is also shared by our results for neural networks and regression trees. Rather than bounding disagreement directly in terms of the number of models k k being aggregated (which is the form of our result for gradient boosting), here we are relating disagreement to the local training error curve as a function of k k — i.e., how much the error would decrease in expectation by doubling the number of models in the aggregation from k k to 2 ​ k 2k . If this curve has flattened out sufficiently near any particular value of k k , we have approximate agreement.

[28] p: Note that in general we cannot say anything about which value of k k will result in the loss R ¯ k \bar{R}_{k} approximating its minimum value. Consider a distribution Q Q over some model space H H in which almost all models have large error and no correlation with respect to the true y y values, and there is one model h ∗ h^{*} that is a perfect predictor of y y . Let Q Q put some (arbitrarily small) weight τ > 0 \tau>0 on h ∗ h^{*} . Then stacked regression for k ≪ 1 / τ k\ll 1/\tau will result in large error, since with high probability we sample only uninformative models. But for k ∼ 1 / τ k\sim 1/\tau we will be likely to draw h ∗ h^{*} , at which point stacking will suddenly choose to put all its weight on h ∗ h^{*} and enjoy a rapid drop in error.

[29] p: However, note that in this example, the learning curve as a function of k k will have been flat for the long period before the error drop (as well as after it), and so our theorem implies high agreement even for small values of k k despite low error only being obtained for large values of k k . More generally, if labels y y are bounded (say) in [ 0 , 1 ] [0,1] , then each term R ¯ k \bar{R}_{k} is bounded in [ 0 , 1 ] [0,1] . Because the sequence R ¯ k \bar{R}_{k} is monotonically decreasing in k k , there can be at most 1 / α 1/\alpha values of k k such that ( R ¯ k − R ¯ 2 ​ k ) (\bar{R}_{k}-\bar{R}_{2k}) drops by at least α \alpha before contradicting the non-negativity of squared error. Thus even in the worst case, there must be a value of k ≤ 2 1 / α k\leq 2^{1/\alpha} such that ( R ¯ k − R ¯ 2 ​ k ) ≤ α (\bar{R}_{k}-\bar{R}_{2k})\leq\alpha — a bound depending only on the desired agreement rate α \alpha , independently of the complexity of the instance or the model class. Of course we expect a better behaved learning curve in practice. Moreover, it is easy to empirically evaluate the actual learning curve on a holdout set.

[30] p: This suggests a practical prescription arising from our local-learning curve bound for stacking (as well as the similar bound we obtain for neural network and regression tree training): empirically trace out the learning curve by successively doubling k k , estimate the errors of the stacked models on a holdout set, and choose a value of k k for which the local drop in error is small. Note that whatever our computational resources might be, reducing our predictive error while respecting our resource constraints and achieving predictive stability are aligned: in neither case do we want to choose a value k k for which the local learning curve is steep. For predictive error, steepness of the learning curve indicates that at only modestly increased cost, we can meaningfully reduce error. Conversely, flatness of the learning curve indicates local optimality of our choice of k k — we cannot improve error substantially at least without significantly more computational and data resources. Our theorem shows that the same condition implies strong independent agreement bounds.

[31] h4: 1.1.4 Gradient Boosting

[32] p: Our next application in Section 4 is to gradient boosting ( Friedman et al., 2000 ; Friedman, 2001 ; Mason et al., 1999 ) . Concretely, gradient boosting starts with an arbitrary class of “weak” models C C (e.g., depth 5 regression trees), and iteratively builds up a model f f by finding a model g ∈ C g\in C that has high correlation with the residuals of the existing model f f . It then adds some scaling of g g to f f , and continues to the next iterate. Scalable implementations of gradient boosting, like XGBoost ( Chen and Guestrin, 2016 ) , have become some of the most widely used learning algorithms for tabular data. Like stacking, gradient boosting builds up a linear ensemble of base models, but unlike stacking, the models are no longer independently trained. We again take a reduced-form view of training on finite samples, mirroring the classical Statistical Query model of Kearns (1998) : we model the learning algorithm as having access to a weak-learning oracle that, given a model f f , can return any model g ∈ C g\in C whose covariance with the residuals of f f is within ε \varepsilon of maximal on the underlying distribution, modeling both sampling and optimization error. Gradient boosting has two properties that are useful to us: it produces a model in the linear span of C C , and it isn’t hard to show that (independent of any distributional assumptions), it learns a model whose MSE approaches that of the best model in the span of C C at a rate of 1 / k 1/k , where k k is the number of iterates. Accordingly, we choose to compare the error of our models to the hypothetical model f ∗ f^{*} that minimizes squared error amongst all models in the linear span of C C . Once again, as f ¯ \bar{f} also lies within the linear span of C C , f ∗ f^{*} has only lower error. Because we can show that MSE ​ ( f 1 ) , MSE ​ ( f 2 ) ≤ MSE ​ ( f ∗ ) + O ⁡ ( ( τ ∗ ) 2 / k ) \textrm{MSE}(f_{1}),\textrm{MSE}(f_{2})\leq\textrm{MSE}(f^{*})+O((\tau^{*})^{2}/k) after k k iterates, our core analysis establishes that D ⁡ ( f 1 , f 2 ) ≤ O ⁡ ( ( τ ∗ ) 2 / k ) D(f_{1},f_{2})\leq O((\tau^{*})^{2}/k) as desired. Here τ ∗ \tau^{*} is the norm of the MSE-optimal predictor in the span of C C , a problem-dependent constant depending on only the underlying data distribution and C C . We later show how to remove this dependence on τ ∗ \tau^{*} by instead using a Frank-Wolfe style algorithm which controls the norm of the models f 1 , f 2 f_{1},f_{2} that we learn, and hence lets us instead anchor to the optimal bounded norm model in the span of C C .

[33] h4: 1.1.5 Neural Network and Regression Tree Training

[34] p: Our final applications in Section 5 are to neural network training with architecture search and regression tree training. For these applications, the anchor model f ¯ \bar{f} does not necessarily lie within the same model class as f 1 f_{1} and f 2 f_{2} — i.e the average of two neural networks of size n n is not in general itself representable as a neural network of size n n , and the average of two regression trees of depth d d is not in general representable as another regression tree of depth d d . However, the average of two neural networks of size n n is representable as a neural network of size 2 ​ n 2n , and the average of two depth- d d regression trees is representable as a depth 2 ​ d 2d regression tree. Just as in our stacking result, these bounds relate the disagreement of two approximately optimal models f 1 f_{1} and f 2 f_{2} to the local learning curve (parameterized by the number of internal nodes for neural networks, and the depth for regression trees), which means that disagreement can be driven to 0 0 as a function of the model complexity at a rate that depends only on the desired disagreement level and is independent of the complexity of the instance.

[35] h4: 1.1.6 Tightness of Our Results

[36] p: We show that in general, our technique yields tight bounds. Concretely, we show in Section 3.2 that the stability bound that our technique yields is tight even in constants. Recall that our upper bound for stacking was:

[37] table: 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≤ 4 ​ ( R ¯ k − R ¯ 2 ​ k ) \mathbb{E}_{f_{1},f_{2}}[D(f_{1},f_{2})]\leq 4(\bar{R}_{k}-\bar{R}_{2k})

[38] p: We show that for every ε ≥ 0 \varepsilon\geq 0 there is an instance for which:

[39] table: 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≥ ( 4 − ε ) ​ ( R ¯ k − R ¯ 2 ​ k ) \mathbb{E}_{f_{1},f_{2}}[D(f_{1},f_{2})]\geq(4-\varepsilon)(\bar{R}_{k}-\bar{R}_{2k})

[40] p: This establishes that our core average anchoring technique cannot be generically improved even in the constant factor.

[41] h4: 1.1.7 Generalizations

[42] p: Finally, in Section 6 we generalize all of our results beyond one-dimensional outcomes and squared loss to multi-dimensional strongly convex losses. This generalization requires establishing an analogue of our MSE decomposition and anchoring argument, letting us relate disagreement rates to differences in loss with the averaged anchor model.

[43] p: We also give a variant of our gradient boosting result for a Frank-Wolfe style optimization algorithm that iteratively builds up a linear combination of weak learners from C C that are restricted to have norm at most τ \tau for any τ \tau of our choosing. This lets us anchor to the best norm- τ \tau model in the span of C C , which lets us drive the disagreement error between two independently trained models to 0 0 at a rate of O ⁡ ( τ 2 / k ) O(\tau^{2}/k) where k k is the number of iterations of the algorithm. Unlike our initial gradient boosting result — which has error going to 0 0 at a rate of O ⁡ ( ( τ ∗ ) 2 / k ) O((\tau^{*})^{2}/k) , where τ ∗ \tau^{*} is a problem-dependent constant not under our control — here τ \tau is a parameter of our algorithm and we can set it however we like to trade off agreement with accuracy.

[44] h3: 1.2 Interpreting Local Learning Curve Stability

[45] p: Our results for stacking, neural network training, and regression tree training all have the form of local learning curve stability bounds: D ⁡ ( f 1 , f 2 ) ≤ 4 ​ ( R ⁡ ( ℱ n ) − R ⁡ ( ℱ 2 ​ n ) ) D(f_{1},f_{2})\leq 4(R(\mathcal{F}_{n})-R(\mathcal{F}_{2n})) — where R ⁡ ( ℱ k ) R(\mathcal{F}_{k}) refers to the optimal error amongst models with “complexity” k k (parameterizing the number of models being ensembled, network size, and depth in the cases of stacking, neural networks, and regression trees respectively). These kinds of bounds are actionable and well aligned with optimizing for accuracy. They are actionable because (with enough data) it is possible to empirically plot the local learning curve by training with different parameter values, and picking n n such that the curve is locally flat — R ⁡ ( ℱ n ) ≈ R ⁡ ( ℱ 2 ​ n ) R(\mathcal{F}_{n})\approx R(\mathcal{F}_{2n}) . This is aligned with the goal of optimizing for accuracy since if we could substantially improve accuracy by locally increasing the complexity of the model, then in the high data regime, we should. It is also descriptive in the sense that if we assume that most deployed models are not “leaving money on the table” in the sense of being able to substantially improve accuracy by locally increasing complexity, then we should expect stability amongst deployed models. Because the error sequence { R ⁡ ( ℱ n ) } n \{R(\mathcal{F}_{n})\}_{n} is bounded from above and below and monotonically decreasing in n n , the local learning curve is also guaranteed to “flatten out” to a value α \alpha for a value of n n that is independent of the problem complexity, and at most 2 1 / α 2^{1/\alpha} . However, in practice we expect the local learning curve to flatten out even more gracefully. Empirical studies of neural scaling laws ( Kaplan et al., 2020 ; Hoffmann et al., 2022 ) have consistently found that across a wide variety of domains, the optimal error R ⁡ ( ℱ n ) R(\mathcal{F}_{n}) decreases as a power law in model complexity: R ⁡ ( ℱ n ) ≈ R ∗ + c ​ n − γ R(\mathcal{F}_{n})\approx R^{*}+cn^{-\gamma} for some constants c > 0 c>0 , γ > 0 \gamma>0 , and irreducible error R ∗ R^{*} . Under such a power law, the gap in the local learning curve becomes: R ⁡ ( ℱ n ) − R ⁡ ( ℱ 2 ​ n ) = c ⁡ ( n − γ − ( 2 ​ n ) − γ ) = c ⁡ ( 1 − 2 − γ ) ​ n − γ = O ⁡ ( n − γ ) R(\mathcal{F}_{n})-R(\mathcal{F}_{2n})=c\left(n^{-\gamma}-(2n)^{-\gamma}\right)=c(1-2^{-\gamma})n^{-\gamma}=O(n^{-\gamma}) . That is, the local learning curve gap shrinks polynomially in model complexity, which by our results implies that independent model disagreement D ⁡ ( f 1 , f 2 ) D(f_{1},f_{2}) decreases at the same rate. Crucially, this does not require low absolute error rather only that the marginal benefit of increasing complexity diminishes. The exponent γ \gamma varies by domain (typically 0.05 0.05 – 0.5 0.5 for large-scale neural networks), but is reliably positive. Our results provide theoretical grounding for empirical observations that larger models exhibit greater prediction-level consistency across independent training runs ( Bhojanapalli et al., 2021 ; Jordan, 2024 ) , and may help explain the surprisingly high levels of agreement observed empirically across independently trained large language models ( Gorecki and Hardt, 2025 ) .

[46] h3: 1.3 Additional Related Work

[47] h5: Agreement via Interaction

[48] p: A line of work inspired by Aumann (1976) aims to give interactive test-time protocols through which two models (trained initially on different observations) can arrive at (accuracy improving) agreement. Initial work in economics ( Geanakoplos and Polemarchakis, 1982 ) focused on exact agreement, but more recent work in computer science focused on interactions of bounded length, leading to approximate agreement of the same form that we study here ( Aaronson, 2005 ; Frongillo et al., 2023 ) . This line of work focused on perfect Bayesian learners until Collina et al. (2025) ; Collina et al. (2026) ; Kearns et al. (2026) showed that the same kind of accuracy-improving agreement could be obtained via test-time interaction using computationally and data efficient learning algorithms.

[49] h5: Agreement as Variance

[50] p: Our disagreement metric is (twice) the variance of the training procedure. Kur et al. (2023) show that for realizable learning problems (with mean zero independent noise), empirical risk minimization over a fixed, convex class leads to variance that is upper bounded by the minimax rate. Our results apply to more general settings: our applications to neural networks and regression trees correspond to non-convex learning problems, our application to stacking does not correspond to optimization over a fixed class, and we do not require any realizability assumptions. Note also, the interest of Kur et al. (2023) is to study generalization through the lens of bias/variance tradeoffs, whereas our starting point is to assume small excess risk in distribution.

[51] h5: Different Notions of Stability

[52] p: There are many notions of stability in machine learning. Bousquet and Elisseeff (2002) give notions of leave-one-out stability and connect them to out-of-sample generalization. These notions have been influential, and many authors have proven generalization bounds via this link to stability: for example Hardt et al. (2016) show that stochastic gradient descent is stable in this sense if only run for a small number of iterations, and Charles and Papailiopoulos (2018) study the stability of global optimizers in terms of the geometry of the loss-optimal solution. These notions of stability are different than the disagreement metric we study here. First, stability in the sense of Bousquet and Elisseeff (2002) is stability only of the loss, not the predictions themselves which is our interest. Second, stability in the sense of Bousquet and Elisseeff (2002) is stability with respect to adding or removing a single training example, whereas we want prediction-level stability over fully independent retraining, in which (in general) every single training example is different — just drawn from the same distribution.

[53] p: Differential privacy ( Dwork et al., 2006 ; Dwork and Roth, 2014 ) is a strong notion of algorithmic stability that when applied to machine learning requires that when one training sample is changed, the (randomized) training algorithm induces a near-by distribution on output models. Differential privacy is a much stronger stability condition than those of Bousquet and Elisseeff (2002) , and similarly implies strong generalization guarantees ( Dwork et al., 2015 ) . When the differential privacy stability parameter is taken to be sufficiently small ( ε ≪ 1 / n \varepsilon\ll 1/\sqrt{n} ), then it implies stability under resampling of the entire training set from the same distribution, as we study in our paper — this is related to what is called perfect generalization by Cummings et al. (2016) . Via this connection, differential privacy has been shown to be (information theoretically) reducible to replicability (as defined by Impagliazzo et al. (2022) ) and vice-versa ( Bun et al., 2023 ) . Replicability is a stronger condition than the kind of agreement that we study: in the context of machine learning, it requires that (under coupled random coins across the two training algorithms), the run of two training algorithms over independently sampled training sets output exactly identical models with high probability. In contrast we ask that two independently trained models produce numerically similar predictions on most examples. However, because replicability asks for more, it also comes with severe limitations that we avoid. Via its connection to differential privacy, there are strong separations between problems that are learnable with the constraint of replicability and without ( Alon et al., 2019 ; Bun et al., 2020 ) . Even for those learning problems that are solvable replicably (e.g. learning problems solvable in the statistical query model of Kearns (1998) ), standard learning algorithms for these problems are not replicable, and the computational and sample complexity of custom-designed replicable algorithms often far exceeds the complexity of non-replicable learning (see e.g. Eaton et al. (2026) ). In contrast, our analyses apply to existing, popular, state of the art learning algorithms (gradient boosting and regression tree and neural network training with architecture search). Since any model class can be used together with stacking or gradient boosting, there are no barriers to obtaining our kind of model agreement similar to the information theoretic barriers separating replicable from non-replicable learning. The concurrent work of Hopkins et al. (2025) is similarly motivated to ours: their goal is to relax the strict replicability definition of Impagliazzo et al. (2022) to one that requires that two replicably trained models agree on “most inputs”, and thereby circumvent the impossibility results separating PAC learning from replicable learning. They give several definitions of approximate replicability and show that approximately replicable PAC learning has similar sample complexity to unconstrained PAC learning. Our approaches, results, and techniques are quite different, however. Hopkins et al. (2025) focuses on binary hypothesis classes and gives custom training procedures relying on shared randomness that satisfy their notion of approximate replicability. We instead focus on (multi-dimensional) regression problems and give analyses of existing, popular learning algorithms. Our training procedures do not use shared randomness.

[54] h5: Agreement and Ensembling

[55] p: Wood et al. (2023) studies the error reduction that can be obtained through ensembling methods and relates it to a notion of model disagreement that is equivalent to ours. Their interests are dual to ours: for them the goal is error reduction through explicit ensembling, and model disagreement is a means to that end; our primary goal is model agreement, and we show a general recipe for obtaining it — for us, the “ensemble” is a hypothetical object used only in the analysis of agreement for hypothesis classes (neural networks, regression trees) that are not themselves ensemble methods.

[56] h5: Empirical Phenomena

[57] p: Empirical work quantifies prediction-level stability across retrainings via churn, per-example consistency, and related notions ( Bhojanapalli et al., 2021 ; Bahri and Jiang, 2021 ; Johnson and Zhang, 2023 ) . Based on this, various studies show that simple procedures — e.g., ensembling or co-distillation — can increase agreement ( Wang et al., 2020 ; Bhojanapalli et al., 2021 ) . However, recent work showed that fluctuations in run-to-run test accuracy can be largely explained by finite-sample effects even when the underlying predictors are similar ( Jordan, 2024 ) . Relatedly, Somepalli et al. (2022) made the observation that across pairs of models, independently trained neural networks often seem to depict similar decision regions despite their complexity which raises the question of when and whether external methods to encourage agreement are even required. On top of this, Mao et al. (2024) provide evidence that training trajectories lie on a shared low-dimensional manifold in prediction space, pointing to a common structure that could underlie agreement. The latter works only characterize the prediction space based on visualizations and do not provide a formal explanation as to why agreement might occur from independent training. Gorecki and Hardt (2025) recently conducted a large empirical study of model disagreement across 50 large language models used for prediction tasks, and find that empirically they have much higher levels of agreement than one would expect if errors were made at random; our work can be viewed as giving foundations to this kind of empirical observation.

[58] p: Empirical agreement has also been studied through the lens of generalization. In-distribution pairwise disagreement between independently trained copies on unlabeled test data has been observed to provide an accurate estimate of test error ( Jiang et al., 2022 ) . Moreover, a single model’s pattern of predictions on the training set closely matches its behavior on the test set as distributions, indicating prediction-space stability that is distinct from inter-run agreement ( Nakkiran and Bansal, 2020 ) . Beyond in-distribution, there are cases where even out-of-distribution pairwise agreement scales linearly with in-distribution agreement across many shifts ( Baek et al., 2022 ) . None of these works provide prediction-space conditions or rates under which independently trained models will immediately agree in the first place.

[59] p: A complementary line of work focusing on weight-space studies shows that many independently trained solutions can be connected by low-loss paths ( Garipov et al., 2018 ; Draxler et al., 2018 ) . Even when solutions aren’t trivially aligned, applying neuron permutations can align them, enabling low-loss interpolation ( Entezari et al., 2022 ; Ainsworth et al., 2023 ) . It can be shown that their layers are stitchable or exhibit layer-wise linear feature connectivity ( Bansal et al., 2021 ; Zhou et al., 2023 ) , which is consistent with a connected region once permutation symmetries are accounted for. These techniques are post-hoc observations about weight or parameter space and do not provide ex ante, prediction-space guarantees or quantitative rates that independent training will agree without alignment.

[60] p: Closer to prediction space theory, the neural tangent kernel findings characterize how a model’s predictive function evolves under gradient descent ( Jacot et al., 2018 ; Lee et al., 2019 ) . However, these analyses focus on a single training trajectory, primarily analyze the infinite-width regime, and do not directly address whether independently trained models will agree. Our work seeks conditions under which standard training directly yields approximate agreement “out of the box,” bypassing parameter-space alignment and establishing stability in prediction space itself.

[61] h2: 2 Preliminaries and Midpoint Anchoring Lemmas

[62] p: We consider a setting in which we train two models on independently drawn datasets. Let 𝒳 ⊆ ℝ d \mathcal{X}\subseteq\mathbb{R}^{d} be the data domain and 𝒴 ⊆ ℝ \mathcal{Y}\subseteq\mathbb{R} be the label domain. We assume access to datasets S = ( ( x i , y i ) ) i = 0 n − 1 S=((x_{i},y_{i}))_{i=0}^{n-1} that are independently drawn from a joint distribution P P on 𝒳 × 𝒴 \mathcal{X}\times\mathcal{Y} . Note that unless otherwise stated, all expectations will be with respect to x , y ∼ P x,y\sim P or where appropriate just the marginal over x x . A model is then defined as a function mapping f : 𝒳 ↦ 𝒴 f:\mathcal{X}\mapsto\mathcal{Y} . We define the norm ‖ f ‖ := ( 𝔼 ⁡ [ f ​ ( x ) 2 ] ) 1 / 2 \|f\|:=\big(\mathbb{E}[f(x)^{2}]\big)^{1/2} . With this we define the mean squared error objective and the corresponding population risk

[63] table: MSE ⁡ ( f ) = 𝔼 ⁡ [ ( y − f ⁡ ( x ) ) 2 ] , R ⁡ ( ℱ ) := inf f ∈ ℱ MSE ⁡ ( f ) . \mathrm{MSE}(f)=\mathbb{E}[(y-f(x))^{2}],\quad R(\mathcal{F}):=\inf_{f\in\mathcal{F}}\mathrm{MSE}(f).

[64] p: We next define the disagreement between two models as their expected squared difference.

[65] h6: Definition 2.1 (Disagreement) .

[66] p: For any two functions f 1 : 𝒳 ↦ 𝒴 , f 2 : 𝒳 ↦ 𝒴 f_{1}:\mathcal{X}\mapsto\mathcal{Y},f_{2}:\mathcal{X}\mapsto\mathcal{Y} , we define the expected disagreement between them as

[67] table: D ⁡ ( f 1 , f 2 ) := 𝔼 ⁡ [ ( f 1 ​ ( x ) − f 2 ​ ( x ) ) 2 ] . D(f_{1},f_{2}):=\mathbb{E}[(f_{1}(x)-f_{2}(x))^{2}]\kern 5.0pt.

[68] p: We are now ready to state and prove a simple identity that will form the backbone of our analyses. It relates the disagreement between two models to the degree to which their errors could be improved by averaging the models.

[69] h6: Lemma 2.2 (Midpoint identity for squared loss) .

[70] p: For any two functions f 1 : 𝒳 ↦ 𝒴 f_{1}:\mathcal{X}\mapsto\mathcal{Y} and f 2 : 𝒳 ↦ 𝒴 f_{2}:\mathcal{X}\mapsto\mathcal{Y} , let f ¯ ​ ( x ) := 1 2 ​ ( f 1 ​ ( x ) + f 2 ​ ( x ) ) \bar{f}(x):=\tfrac{1}{2}(f_{1}(x)+f_{2}(x)) . Then

[71] table: D ⁡ ( f 1 , f 2 ) = 2 ​ ( MSE ⁡ ( f 1 ) + MSE ⁡ ( f 2 ) − 2 ​ MSE ​ ( f ¯ ) ) . D(f_{1},f_{2})\,=\,2\Big(\mathrm{MSE}(f_{1})+\mathrm{MSE}(f_{2})-2\,\mathrm{MSE}(\bar{f})\Big).

[72] h6: Proof.

[73] p: Let r i ​ ( x ) := f i ​ ( x ) − y r_{i}(x):=f_{i}(x)-y for i ∈ { 1 , 2 } i\in\{1,2\} . Then f ¯ ​ ( x ) − y = 1 2 ​ ( r 1 ​ ( x ) + r 2 ​ ( x ) ) \bar{f}(x)-y=\tfrac{1}{2}(r_{1}(x)+r_{2}(x)) and f 1 ​ ( x ) − f 2 ​ ( x ) = r 1 ​ ( x ) − r 2 ​ ( x ) f_{1}(x)-f_{2}(x)=r_{1}(x)-r_{2}(x) . Expanding squares and using linearity of expectation gives

[74] table: 𝔼 ⁡ [ ( r 1 − r 2 ) 2 ] \displaystyle\mathbb{E}[(r_{1}-r_{2})^{2}] = 𝔼 ⁡ [ r 1 2 ] + 𝔼 ⁡ [ r 2 2 ] − 2 ​ 𝔼 ​ [ r 1 ​ r 2 ] . \displaystyle=\mathbb{E}[r_{1}^{2}]+\mathbb{E}[r_{2}^{2}]-2\mathbb{E}[r_{1}r_{2}].

[75] p: On the other hand,

[76] table: 𝔼 ⁡ [ ( 1 2 ​ ( r 1 + r 2 ) ) 2 ] \displaystyle\mathbb{E}\Big[\Big(\tfrac{1}{2}(r_{1}+r_{2})\Big)^{2}\Big] = 1 4 ​ 𝔼 ​ [ ( r 1 + r 2 ) 2 ] = 1 4 ​ 𝔼 ​ [ r 1 2 + r 2 2 + 2 ​ r 1 ​ r 2 ] = 1 4 ​ 𝔼 ​ [ r 1 2 ] + 1 4 ​ 𝔼 ​ [ r 2 2 ] + 1 2 ​ 𝔼 ​ [ r 1 ​ r 2 ] . \displaystyle=\tfrac{1}{4}\mathbb{E}[(r_{1}+r_{2})^{2}]=\tfrac{1}{4}\mathbb{E}[r_{1}^{2}+r_{2}^{2}+2r_{1}r_{2}]=\tfrac{1}{4}\mathbb{E}[r_{1}^{2}]+\tfrac{1}{4}\mathbb{E}[r_{2}^{2}]+\tfrac{1}{2}\mathbb{E}[r_{1}r_{2}].

[77] p: Therefore,

[78] table: 2 ​ ( 𝔼 ⁡ [ r 1 2 ] + 𝔼 ⁡ [ r 2 2 ] − 2 ​ 𝔼 ​ [ ( 1 2 ​ ( r 1 + r 2 ) ) 2 ] ) \displaystyle 2\Big(\mathbb{E}[r_{1}^{2}]+\mathbb{E}[r_{2}^{2}]-2\mathbb{E}\big[\big(\tfrac{1}{2}(r_{1}+r_{2})\big)^{2}\big]\Big) = 2 ​ ( 𝔼 ⁡ [ r 1 2 ] + 𝔼 ⁡ [ r 2 2 ] − 2 ​ ( 1 4 ​ 𝔼 ​ [ r 1 2 ] + 1 4 ​ 𝔼 ​ [ r 2 2 ] + 1 2 ​ 𝔼 ​ [ r 1 ​ r 2 ] ) ) \displaystyle=2\Big(\mathbb{E}[r_{1}^{2}]+\mathbb{E}[r_{2}^{2}]-2\Big(\tfrac{1}{4}\mathbb{E}[r_{1}^{2}]+\tfrac{1}{4}\mathbb{E}[r_{2}^{2}]+\tfrac{1}{2}\mathbb{E}[r_{1}r_{2}]\Big)\Big) = 2 ​ ( 1 2 ​ 𝔼 ​ [ r 1 2 ] + 1 2 ​ 𝔼 ​ [ r 2 2 ] − 𝔼 ⁡ [ r 1 ​ r 2 ] ) \displaystyle=2\big(\tfrac{1}{2}\mathbb{E}[r_{1}^{2}]+\tfrac{1}{2}\mathbb{E}[r_{2}^{2}]-\mathbb{E}[r_{1}r_{2}]\big) = 𝔼 ⁡ [ r 1 2 ] + 𝔼 ⁡ [ r 2 2 ] − 2 ​ 𝔼 ​ [ r 1 ​ r 2 ] = 𝔼 ⁡ [ ( r 1 − r 2 ) 2 ] . \displaystyle=\mathbb{E}[r_{1}^{2}]+\mathbb{E}[r_{2}^{2}]-2\mathbb{E}[r_{1}r_{2}]=\mathbb{E}[(r_{1}-r_{2})^{2}].

[79] p: Substituting back 𝔼 ⁡ [ r i 2 ] = MSE ⁡ ( f i ) \mathbb{E}[r_{i}^{2}]=\mathrm{MSE}(f_{i}) and 𝔼 ⁡ [ ( 1 2 ​ ( r 1 + r 2 ) ) 2 ] = MSE ⁡ ( f ¯ ) \mathbb{E}\big[\big(\tfrac{1}{2}(r_{1}+r_{2})\big)^{2}\big]=\mathrm{MSE}(\bar{f}) yields the claim. ∎

[80] p: A useful corollary of this identity is that we can upper bound the disagreement between two models by the degree to which they are sub-optimal relative to the best model in any family that contains their average.

[81] h6: Corollary 2.3 (Disagreement via the midpoint anchor) .

[82] p: For any two functions f 1 , f 2 : 𝒳 → 𝒴 f_{1},f_{2}:\mathcal{X}\to\mathcal{Y} , let f ¯ ​ ( x ) := 1 2 ​ ( f 1 ​ ( x ) + f 2 ​ ( x ) ) \bar{f}(x):=\tfrac{1}{2}(f_{1}(x)+f_{2}(x)) . If f ¯ ∈ ℋ \bar{f}\in\mathcal{H} for some class of predictors ℋ \mathcal{H} , then

[83] table: D ⁡ ( f 1 , f 2 ) ≤ 2 ​ ( MSE ⁡ ( f 1 ) − R ⁡ ( ℋ ) ) + 2 ​ ( MSE ⁡ ( f 2 ) − R ⁡ ( ℋ ) ) . D(f_{1},f_{2})\,\leq\,2\big(\mathrm{MSE}(f_{1})-R(\mathcal{H})\big)+2\big(\mathrm{MSE}(f_{2})-R(\mathcal{H})\big).

[84] h6: Proof.

[85] p: By Lemma 2.2 , we have

[86] table: D ⁡ ( f 1 , f 2 ) = 2 ​ ( MSE ⁡ ( f 1 ) + MSE ⁡ ( f 2 ) − 2 ​ MSE ​ ( f ¯ ) ) . D(f_{1},f_{2})\,=\,2\Big(\mathrm{MSE}(f_{1})+\mathrm{MSE}(f_{2})-2\,\mathrm{MSE}(\bar{f})\Big).

[87] p: If f ¯ ∈ ℋ \bar{f}\in\mathcal{H} then MSE ⁡ ( f ¯ ) ≥ R ⁡ ( ℋ ) \mathrm{MSE}(\bar{f})\geq R(\mathcal{H}) , so substituting yields the claim. ∎

[88] p: If the model class from which f 1 f_{1} and f 2 f_{2} were trained contains their average, then we can relate the disagreement between f 1 f_{1} and f 2 f_{2} to the sub-optimality of the loss of f 1 f_{1} and f 2 f_{2} to the global optimum within the class in which they were trained. However, non-convex model classes will not satisfy this closure-under-averaging property. To analyze these classes it is useful to consider local learning-curve bounds with respect to a hierarchy of model classes, such that each level ℱ 2 ​ n \mathcal{F}_{2n} in the hierarchy is expressive enough to represent the average of any pair of models in ℱ n \mathcal{F}_{n} . We will see that this property is satisfied by neural networks (where n n parametrizes the number of internal nodes) and regression trees (where n n parametrizes the depth).

[89] h6: Lemma 2.4 (Local learning-curve bound from midpoint closure) .

[90] p: Let ( ℱ n ) n ≥ 1 (\mathcal{F}_{n})_{n\geq 1} be a nested sequence of predictor classes and assume that for every n n and every f 1 , f 2 ∈ ℱ n f_{1},f_{2}\in\mathcal{F}_{n} , the midpoint predictor f ¯ := 1 2 ​ ( f 1 + f 2 ) \bar{f}:=\tfrac{1}{2}(f_{1}+f_{2}) lies in ℱ 2 ​ n \mathcal{F}_{2n} . Fix n ≥ 1 n\geq 1 and suppose f 1 , f 2 ∈ ℱ n f_{1},f_{2}\in\mathcal{F}_{n} satisfy MSE ⁡ ( f i ) ≤ R ⁡ ( ℱ n ) + ε \mathrm{MSE}(f_{i})\leq R(\mathcal{F}_{n})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} . Then

[91] table: D ⁡ ( f 1 , f 2 ) ≤ 4 ​ ( R ⁡ ( ℱ n ) − R ⁡ ( ℱ 2 ​ n ) + ε ) . D(f_{1},f_{2})\,\leq\,4\big(R(\mathcal{F}_{n})-R(\mathcal{F}_{2n})+\varepsilon\big).

[92] h6: Proof.

[93] p: By midpoint closure we have f ¯ ∈ ℱ 2 ​ n \bar{f}\in\mathcal{F}_{2n} , so Lemma 2.3 with ℋ = ℱ 2 ​ n \mathcal{H}=\mathcal{F}_{2n} gives

[94] table: D ⁡ ( f 1 , f 2 ) ≤ 2 ​ ( MSE ⁡ ( f 1 ) − R ⁡ ( ℱ 2 ​ n ) ) + 2 ​ ( MSE ⁡ ( f 2 ) − R ⁡ ( ℱ 2 ​ n ) ) . D(f_{1},f_{2})\leq 2\big(\mathrm{MSE}(f_{1})-R(\mathcal{F}_{2n})\big)+2\big(\mathrm{MSE}(f_{2})-R(\mathcal{F}_{2n})\big).

[95] p: Using MSE ⁡ ( f i ) ≤ R ⁡ ( ℱ n ) + ε \mathrm{MSE}(f_{i})\leq R(\mathcal{F}_{n})+\varepsilon for both i i yields the claim. ∎

[96] p: In the following sections, we apply Lemma 2.3 and Lemma 2.4 by verifying that the midpoint predictor lies in an appropriate hypothesis class.

[97] h2: 3 Warmup Application: Stacking

[98] p: Stacking is an ensembling method which first trains k k independent base models in some arbitrary fashion and then uses linear regression over these base models to combine their predictions.

[99] figure: Algorithm 1 Ensembling via Stacking Input: M : G → ℋ M:G\rightarrow\mathcal{H} black-box learning algorithm, D ∼ P n D\sim P^{n} dataset of size n n , number of shards k k Randomly split D D into k k disjoint shards G i G_{i} each of size | G i | = ⌊ n k ⌋ |G_{i}|=\Big\lfloor\frac{n}{k}\Big\rfloor for i ∈ [ k ] i\in[k] do g i ← M ⁡ ( G i ) g_{i}\leftarrow M(G_{i}) end for f ← OLS ⁡ ( g 1 , … , g k ) f\leftarrow\mathrm{OLS}(g_{1},\dots,g_{k}) return f f

[100] p: Let Q Q be a probability distribution on models of the form g : 𝒳 → ℝ g:\mathcal{X}\rightarrow\mathbb{R} . Concretely, Q Q could represent the law of a base predictor obtained by training a fixed learning algorithm M M on a random shard of the training sample of size n / k n/k , with a fresh i.i.d. draw of examples and fresh algorithmic randomness; independent draws from Q Q correspond to training M M on independent shards. We remark in passing that other interpretations of Q Q also make sense. For example, perhaps all parties share the same training set (because e.g. it is the training set for a standard benchmark dataset like ImageNet). Then there is no need to have different models be trained on different shards, and Q Q can represent only the randomness of the training procedure, which might re-use samples in arbitrary ways. We will analyze the population least squares predictor over the span of these base models. That is, we sample k k models G = { g 1 , … , g k } ∼ Q k G=\{g_{1},...,g_{k}\}\sim Q^{k} and define V ⁡ ( G ) V(G) to be the linear span of the sampled models in G G . We will consider the predictor

[101] table: arg ⁡ min f ∈ V ⁡ ( G ) ​ MSE ​ ( f ) . \arg\min_{f\in V(G)}\mathrm{MSE}(f).

[102] p: Note that this is just a finite dimensional least squares problem, so a minimizer exists, and multiset multiplicities do not affect the span V ⁡ ( G ) V(G) . For t ∈ ℕ t\in\mathbb{N} , let R t R_{t} denote the random variable R ⁡ ( G ) R(G) when G = { g 1 , … , g t } G=\{g_{1},\dots,g_{t}\} with g 1 , … , g t ∼ i.i.d. Q g_{1},\dots,g_{t}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q , and write R ¯ t := 𝔼 { g 1 , … , g t } ∼ Q t ​ [ R t ] \bar{R}_{t}:=\mathbb{E}_{\{g_{1},...,g_{t}\}\sim Q^{t}}[R_{t}] . We will use the shorthand R ¯ t := 𝔼 G ​ [ R t ] \bar{R}_{t}:=\mathbb{E}_{G}[R_{t}]

[103] h3: 3.1 An Agreement Upper Bound

[104] p: We instantiate our agreement upper bound for Stacking using the midpoint anchoring lemma. In this case we compare f 1 f_{1} and f 2 f_{2} to the risk R ⁡ ( G ∗ ) R(G^{*}) where G ∗ := G ∪ G ′ G^{*}:=G\cup G^{\prime} is the union of the base models used in training f 1 f_{1} and f 2 f_{2} . Here f 1 f_{1} is the MSE minimizer over the set of base models G = { g 1 , … , g k } G=\{g_{1},...,g_{k}\} and f 2 f_{2} is the MSE minimizer over the set of base models G ′ = { g 1 ′ , … , g k ′ } G^{\prime}=\{g_{1}^{\prime},...,g_{k}^{\prime}\} . We know that V ⁡ ( G ) , V ⁡ ( G ′ ) ⊆ V ⁡ ( G ∪ G ′ ) V(G),V(G^{\prime})\subseteq V(G\cup G^{\prime}) , and that the midpoint predictor 1 2 ​ ( f 1 + f 2 ) \tfrac{1}{2}(f_{1}+f_{2}) lies in V ⁡ ( G ∪ G ′ ) V(G\cup G^{\prime}) . This, together with the fact that the set of 2 ​ k 2k models in G ∪ G ′ G\cup G^{\prime} is exchangeable lets us prove the following agreement bound:

[105] h6: Theorem 3.1 (Agreement for Stacked Aggregation) .

[106] p: Let G = { g 1 , … , g k } ∼ i.i.d. Q k G=\{g_{1},\dots,g_{k}\}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{k} and G ′ = { g 1 ′ , … , g k ′ } ∼ i.i.d. Q k G^{\prime}=\{g^{\prime}_{1},\dots,g^{\prime}_{k}\}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{k} be independent. Define f 1 , f 2 f_{1},f_{2} as follows:

[107] table: f 1 = arg ⁡ min f ∈ V ⁡ ( G ) ⁡ MSE ⁡ ( f ) , f 2 = arg ⁡ min f ∈ V ⁡ ( G ′ ) ⁡ MSE ⁡ ( f ) f_{1}=\arg\min_{f\in V(G)}\mathrm{MSE}(f),\quad f_{2}=\arg\min_{f\in V(G^{\prime})}\mathrm{MSE}(f)

[108] p: Then we have that

[109] table: 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≤ 4 ​ ( R ¯ k − R ¯ 2 ​ k ) . \mathbb{E}_{f_{1},f_{2}}\big[D(f_{1},f_{2})]\;\leq\;4\big(\bar{R}_{k}-\bar{R}_{2k}\big).

[110] h6: Proof.

[111] p: Fix realizations of G G and G ′ G^{\prime} , and let G ∗ = G ∪ G ′ G^{*}=G\cup G^{\prime} (multiset union ). Throughout this section we will think of G , G ′ ∼ Q k G,G^{\prime}\sim Q^{k} , unless explicitly conditioned. Note that V ⁡ ( G ) ⊆ V ⁡ ( G ∗ ) V(G)\subseteq V(G^{*}) and V ⁡ ( G ′ ) ⊆ V ⁡ ( G ∗ ) V(G^{\prime})\subseteq V(G^{*}) . In our proofs, without loss of generality, we will use the notation h G h_{G} to denote the least squares minimizer with respect to subspace G G . In our theorem statements, this corresponds to f 1 f_{1} , but we use this notation in our proofs for the sake of clarity. Let h ¯ := 1 2 ​ ( h G + h G ′ ) \bar{h}:=\tfrac{1}{2}(h_{G}+h_{G^{\prime}}) . Since h G ∈ V ⁡ ( G ) h_{G}\in V(G) and h G ′ ∈ V ⁡ ( G ′ ) h_{G^{\prime}}\in V(G^{\prime}) and V ⁡ ( G ) , V ⁡ ( G ′ ) ⊆ V ⁡ ( G ∗ ) V(G),V(G^{\prime})\subseteq V(G^{*}) , we have h ¯ ∈ V ⁡ ( G ∗ ) \bar{h}\in V(G^{*}) . Applying Lemma 2.3 with f 1 = h G f_{1}=h_{G} , f 2 = h G ′ f_{2}=h_{G^{\prime}} , and ℋ = V ⁡ ( G ∗ ) \mathcal{H}=V(G^{*}) , and using MSE ⁡ ( h G ) = R ⁡ ( G ) \mathrm{MSE}(h_{G})=R(G) , MSE ⁡ ( h G ′ ) = R ⁡ ( G ′ ) \mathrm{MSE}(h_{G^{\prime}})=R(G^{\prime}) , and R ⁡ ( V ⁡ ( G ∗ ) ) = R ⁡ ( G ∗ ) R(V(G^{*}))=R(G^{*}) , we have the pointwise inequality

[112] table: ‖ h G − h G ′ ‖ 2 ≤ 2 ​ ( R ⁡ ( G ) − R ⁡ ( G ∗ ) ) + 2 ​ ( R ⁡ ( G ′ ) − R ⁡ ( G ∗ ) ) . \|h_{G}-h_{G^{\prime}}\|^{2}\;\leq\;2\big(R(G)-R(G^{*})\big)+2\big(R(G^{\prime})-R(G^{*})\big). (1)

[113] p: We now take expectations over G , G ′ , G ∗ G,G^{\prime},G^{*} to relate the two terms on the RHS of Equation 1 . Conditional on G ∗ G^{*} , we can generate the pair ( G , G ′ ) (G,G^{\prime}) by drawing a uniformly random permutation π \pi of { 1 , … , 2 ​ k } \{1,\dots,2k\} and letting G G be the first k k permuted elements of G ∗ G^{*} and G ′ G^{\prime} the remaining k k . This holds because the 2 ​ k 2k features in G ∗ G^{*} arise from 2 ​ k 2k i.i.d. draws from Q Q and the joint law of ( G , G ′ ) (G,G^{\prime}) is exchangeable under permutations of these 2 ​ k 2k draws. Conditioning on the unordered multiset G ∗ G^{*} , ( G , G ′ ) (G,G^{\prime}) is a uniformly random partition into two k k -submultisets. Therefore, taking the conditional expectation of ( 1 ) given G ∗ G^{*} and using symmetry of G G and G ′ G^{\prime} ,

[114] table: 𝔼 ( G , G ′ ) | G ∗ ​ [ ‖ h G − h G ′ ‖ 2 | G ∗ ] ≤ 4 ​ ( 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] − R ⁡ ( G ∗ ) ) . \mathbb{E}_{(G,G^{\prime})|G^{*}}\big[\,\|h_{G}-h_{G^{\prime}}\|^{2}\,\big|\,G^{*}\big]\;\leq\;4\Big(\mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]-R(G^{*})\Big). (2)

[115] p: We now integrate ( 2 ) over G ∗ G^{*} . We claim that

[116] table: 𝔼 G ∗ ​ [ 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] ] = R ¯ k and 𝔼 G ∗ ​ [ R ⁡ ( G ∗ ) ] = R ¯ 2 ​ k . \mathbb{E}_{G^{*}}\Big[\mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]\Big]\;=\;\bar{R}_{k}\qquad\text{and}\qquad\mathbb{E}_{G^{*}}\big[R(G^{*})\big]\;=\;\bar{R}_{2k}. (3)

[117] p: The second equality is immediate from the definition of R ¯ 2 ​ k \bar{R}_{2k} , since G ∗ G^{*} is a collection of 2 ​ k 2k i.i.d. draws from Q Q . For the first equality in ( 3 ), let U U be a uniformly random k k -subset of { 1 , … , 2 ​ k } \{1,\dots,2k\} independent of the draws { g 1 , … , g 2 ​ k } ∼ i.i.d. Q 2 ​ k \{g_{1},\dots,g_{2k}\}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{2k} . Define G U := { g i } i ∈ U G_{U}:=\{g_{i}\}_{i\in U} . By the conditional description above,

[118] table: 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] = 𝔼 U ​ [ R ⁡ ( G U ) | G ∗ ] . \mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]\;=\;\mathbb{E}_{U}\big[R(G_{U})\,\big|\,G^{*}\big].

[119] table: 𝔼 G ∗ ​ [ 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] ] = 𝔼 G ∗ ​ [ 𝔼 U ​ [ R ⁡ ( G U ) | G ∗ ] ] = 𝔼 G ∗ , U ​ [ R ⁡ ( G U ) ] . \mathbb{E}_{G^{*}}\Big[\mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]\Big]=\mathbb{E}_{G^{*}}\Big[\mathbb{E}_{U}\big[R(G_{U})\,\big|\,G^{*}\big]\Big]=\mathbb{E}_{G^{*},U}\big[R(G_{U})\big].

[120] p: For any fixed U U , the subcollection { g i } i ∈ U \{g_{i}\}_{i\in U} consists of k k i.i.d. draws from Q Q (since the full family is i.i.d. and U U is independent of the draws), hence averaging over U U yields 𝔼 G ∗ , U ​ [ R ⁡ ( G U ) ] = R ¯ k \mathbb{E}_{G^{*},U}[R(G_{U})]=\bar{R}_{k} , proving ( 3 ).

[121] p: Finally, taking expectations in ( 2 ) and substituting ( 3 ) gives

[122] table: 𝔼 G , G ′ ​ [ ‖ h G − h G ′ ‖ 2 ] ≤ 4 ​ ( R ¯ k − R ¯ 2 ​ k ) , \mathbb{E}_{G,G^{\prime}}\big[\,\|h_{G}-h_{G^{\prime}}\|^{2}\,\big]\;\leq\;4\big(\bar{R}_{k}-\bar{R}_{2k}\big),

[123] p: which is the desired bound. ∎

[124] p: Note that Theorem 3.1 depends on the slope of the local learning curve at k k : ( R ¯ k − R ¯ 2 ​ k ) (\bar{R}_{k}-\bar{R}_{2k}) . This is a strength; dependence on the global learning curve ( R ¯ k − R ∞ ) (\bar{R}_{k}-R_{\infty}) would be significantly weaker. To see this, note that if Q Q contained only a single “good model” with arbitrarily small weight, the global learning curve could fail to flatten out for arbitrarily large k k . On the other hand, simply by monotonicity, for any value of α \alpha , if labels are bounded in (say) [ 0 , 1 ] [0,1] then there must be a value of k ≤ 2 1 / α k\leq 2^{1/\alpha} such that ( R ¯ k − R ¯ 2 ​ k ) ≤ α (\bar{R}_{k}-\bar{R}_{2k})\leq\alpha (as error can drop by α \alpha at most 1 / α 1/\alpha times before contradicting the non-negativity of squared error). While this depends exponentially on α \alpha , it is independent of the dimensionality or complexity of the instance, in contrast to bounds depending on the global learning curve.

[125] h3: 3.2 Stacking Lower Bound

[126] p: Theorem 3.1 gives an upper bound with constant 4 4 . We now show that this factor cannot be improved in general: for every fixed k k and every ε > 0 \varepsilon>0 , there exists a data distribution P P and a distribution Q Q over base models such that two independent stacking runs have disagreement at least ( 4 − ε ) (4-\varepsilon) times the gap R ¯ k − R ¯ 2 ​ k \bar{R}_{k}-\bar{R}_{2k} .

[127] h6: Theorem 3.2 (Near-tightness of the factor 4 4 ) .

[128] p: Fix an integer k ≥ 1 k\geq 1 . For every ε > 0 \varepsilon>0 , there exists a data distribution P P and a distribution Q Q over base models such that if G , G ′ ∼ i.i.d. Q k G,G^{\prime}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{k} are independent k k –tuples and

[129] table: f 1 = arg ⁡ min f ∈ V ⁡ ( G ) ⁡ MSE ⁡ ( f ) , f 2 = arg ⁡ min f ∈ V ⁡ ( G ′ ) ⁡ MSE ⁡ ( f ) , f_{1}=\arg\min_{f\in V(G)}\mathrm{MSE}(f),\qquad f_{2}=\arg\min_{f\in V(G^{\prime})}\mathrm{MSE}(f),

[130] p: then

[131] table: 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≥ ( 4 − ε ) ​ ( R ¯ k − R ¯ 2 ​ k ) . \mathbb{E}_{f_{1},f_{2}}\big[D(f_{1},f_{2})\big]\ \geq\ (4-\varepsilon)\,\big(\bar{R}_{k}-\bar{R}_{2k}\big).

[132] h6: Proof.

[133] p: Fix k ≥ 1 k\geq 1 and ε > 0 \varepsilon>0 . Since the claim is weaker for larger ε \varepsilon , we may assume ε ∈ ( 0 , 1 ] \varepsilon\in(0,1] . We work in a real Hilbert space ℋ \mathcal{H} (equivalently ℋ = L 2 ​ ( P ) \mathcal{H}=L^{2}(P) for a suitable data distribution P P 1 1 1 For example, take 𝒳 = { 0 , 1 , … , m } \mathcal{X}=\{0,1,\dots,m\} and let P P be uniform on 𝒳 \mathcal{X} . Defining e j ( x ) = m + 1 𝕀 { x = j } e_{j}(x)=\sqrt{m+1}\,\mathbb{I}\{x=j\} gives an orthonormal family { e 0 , … , e m } ⊆ L 2 ​ ( P ) \{e_{0},\dots,e_{m}\}\subseteq L^{2}(P) . ) with an orthonormal family { e 0 , … , e m } \{e_{0},\dots,e_{m}\} , where m ∈ ℕ m\in\mathbb{N} will be chosen later, and set the target y := e 0 y:=e_{0} . We construct base models that are “noisy versions” of the target. Fix σ > 0 \sigma>0 and define

[134] table: g i := e 0 + σ e i , i = 1 , … , m . g_{i}\ :=\ e_{0}+\sigma e_{i},\qquad i=1,\dots,m.

[135] p: Let Q Q be the uniform distribution over { g 1 , … , g m } \{g_{1},\dots,g_{m}\} .

[136] p: First, we analyze the predictor and risk for a fixed set of distinct base models. Let H H be a multiset of draws from Q Q . Let S ⁡ ( H ) S(H) be the set of distinct indices of base models in H H , and let r ⁡ ( H ) = | S ⁡ ( H ) | r(H)=|S(H)| . By symmetry, the least-squares predictor f H ∈ V ⁡ ( H ) f_{H}\in V(H) assigns equal weight to each distinct g i ∈ H g_{i}\in H . A straightforward calculation shows that the optimal weights are 1 / ( r ⁡ ( H ) + σ 2 ) 1/(r(H)+\sigma^{2}) , yielding:

[137] table: f H = ∑ i ∈ S ⁡ ( H ) 1 r ⁡ ( H ) + σ 2 ​ g i = r ⁡ ( H ) r ⁡ ( H ) + σ 2 ​ e 0 + σ r ⁡ ( H ) + σ 2 ​ ∑ i ∈ S ⁡ ( H ) e i . f_{H}\ =\ \sum_{i\in S(H)}\frac{1}{r(H)+\sigma^{2}}\,g_{i}\ =\ \frac{r(H)}{r(H)+\sigma^{2}}\,e_{0}\ +\ \frac{\sigma}{r(H)+\sigma^{2}}\sum_{i\in S(H)}e_{i}. (4)

[138] table: R ⁡ ( H ) = ‖ y − f H ‖ 2 = σ 2 r ⁡ ( H ) + σ 2 . R(H)\ =\ \|y-f_{H}\|^{2}\ =\ \frac{\sigma^{2}}{r(H)+\sigma^{2}}. (5)

[139] p: In particular, for G , G ′ ∼ i.i.d. Q k G,G^{\prime}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{k} , we have f 1 = f G f_{1}=f_{G} , f 2 = f G ′ f_{2}=f_{G^{\prime}} , and R ⁡ ( G ) = MSE ⁡ ( f 1 ) R(G)=\mathrm{MSE}(f_{1}) , R ⁡ ( G ′ ) = MSE ⁡ ( f 2 ) R(G^{\prime})=\mathrm{MSE}(f_{2}) .

[140] p: Next, we analyze the disagreement and risk drop on the event where all sampled models are distinct. Let E E be the event that the 2 ​ k 2k draws in G ∪ G ′ G\cup G^{\prime} are all distinct. On this event, r ⁡ ( G ) = k r(G)=k , r ⁡ ( G ′ ) = k r(G^{\prime})=k , and r ⁡ ( G ∪ G ′ ) = 2 ​ k r(G\cup G^{\prime})=2k . Using ( 5 ), the drop in risk on event E E is:

[141] table: Δ 0 := R ⁡ ( G ) − R ⁡ ( G ∪ G ′ ) = σ 2 k + σ 2 − σ 2 2 ​ k + σ 2 . \Delta_{0}\ :=\ R(G)-R(G\cup G^{\prime})\ =\ \frac{\sigma^{2}}{k+\sigma^{2}}-\frac{\sigma^{2}}{2k+\sigma^{2}}. (6)

[142] p: Using ( 4 ) and the fact that G G and G ′ G^{\prime} share no indices on E E (and thus the e 0 e_{0} coefficients are identical and cancel), the disagreement is:

[143] table: D 0 := ‖ f G − f G ′ ‖ 2 = ‖ σ k + σ 2 ​ ( ∑ i ∈ S ⁡ ( G ) e i − ∑ j ∈ S ⁡ ( G ′ ) e j ) ‖ 2 = 2 ​ k ​ σ 2 ( k + σ 2 ) 2 . D_{0}\ :=\ \|f_{G}-f_{G^{\prime}}\|^{2}\ =\ \left\|\frac{\sigma}{k+\sigma^{2}}\left(\sum_{i\in S(G)}e_{i}-\sum_{j\in S(G^{\prime})}e_{j}\right)\right\|^{2}\ =\ \frac{2k\sigma^{2}}{(k+\sigma^{2})^{2}}. (7)

[144] p: Comparing these quantities, we see that for small σ \sigma :

[145] table: D 0 Δ 0 = 4 − 2 ​ σ 2 k + σ 2 → σ → 0 4 . \frac{D_{0}}{\Delta_{0}}\ =\ 4-\frac{2\sigma^{2}}{k+\sigma^{2}}\ \xrightarrow{\sigma\to 0}\ 4. (8)

[146] p: Finally, we handle the expectations by showing that the event E E dominates. The probability of a collision among the 2 ​ k 2k uniform draws from m m items is at most ( 2 ​ k 2 ) / m \binom{2k}{2}/m , and hence

[147] table: Pr ​ ( E ) ≥ 1 − ( 2 ​ k 2 ) ​ 1 m . \textbf{Pr}(E)\ \geq\ 1-\binom{2k}{2}\,\frac{1}{m}.

[148] p: Since disagreement is always non-negative:

[149] table: 𝔼 G , G ′ ​ [ D ⁡ ( f 1 , f 2 ) ] ≥ Pr ​ ( E ) ​ D 0 . \mathbb{E}_{G,G^{\prime}}\big[D(f_{1},f_{2})\big]\ \geq\ \textbf{Pr}(E)\,D_{0}. (9)

[150] p: For the expected risk drop, we upper bound the risk when collisions occur. The risk R ⁡ ( H ) R(H) is maximized when r ⁡ ( H ) r(H) is minimized (i.e., r ⁡ ( H ) = 1 r(H)=1 ), bounded by R m ​ a ​ x = σ 2 / ( 1 + σ 2 ) R_{max}=\sigma^{2}/(1+\sigma^{2}) . The expected risk is:

[151] table: R ¯ k \displaystyle\bar{R}_{k} = Pr [ r ( G ) = k ] σ 2 k + σ 2 + 𝔼 [ R ( G ) 𝕀 ( r ( G ) < k ) ] \displaystyle=\textbf{Pr}[r(G)=k]\frac{\sigma^{2}}{k+\sigma^{2}}+\mathbb{E}\left[R(G)\mathbb{I}(r(G)<k)\right] ≤ σ 2 k + σ 2 + Pr ​ ( r ⁡ ( G ) < k ) ​ R m ​ a ​ x ≤ σ 2 k + σ 2 + ( k 2 ) ​ 1 m ​ R m ​ a ​ x . \displaystyle\leq\frac{\sigma^{2}}{k+\sigma^{2}}+\textbf{Pr}\big(r(G)<k\big)\,R_{max}\ \leq\ \frac{\sigma^{2}}{k+\sigma^{2}}+\binom{k}{2}\,\frac{1}{m}\,R_{max}.

[152] p: On the other hand, since r ⁡ ( G ∪ G ′ ) ≤ 2 ​ k r(G\cup G^{\prime})\leq 2k always, we have the deterministic lower bound R ¯ 2 ​ k ≥ σ 2 2 ​ k + σ 2 \bar{R}_{2k}\geq\frac{\sigma^{2}}{2k+\sigma^{2}} . Combining these, the expected drop satisfies:

[153] table: R ¯ k − R ¯ 2 ​ k ≤ Δ 0 + k 2 2 ​ m ​ σ 2 1 + σ 2 . \bar{R}_{k}-\bar{R}_{2k}\leq\Delta_{0}+\frac{k^{2}}{2m}\frac{\sigma^{2}}{1+\sigma^{2}}.

[154] p: Now choose σ 2 = ( ε / 8 ) ​ k \sigma^{2}=(\varepsilon/8)k so that ( 8 ) gives D 0 ≥ ( 4 − ε / 4 ) ​ Δ 0 D_{0}\geq(4-\varepsilon/4)\Delta_{0} . Choosing m ≥ ⌈ 96 ​ k 3 ε ⌉ m\geq\ \left\lceil\frac{96\,k^{3}}{\varepsilon}\right\rceil makes Pr ​ ( E ) \textbf{Pr}(E) close to 1 1 and the collision term in the bound on R ¯ k − R ¯ 2 ​ k \bar{R}_{k}-\bar{R}_{2k} negligible compared to Δ 0 \Delta_{0} . Combining ( 9 ) with the upper bound on R ¯ k − R ¯ 2 ​ k \bar{R}_{k}-\bar{R}_{2k} then yields 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≥ ( 4 − ε ) ​ ( R ¯ k − R ¯ 2 ​ k ) \mathbb{E}_{f_{1},f_{2}}\big[D(f_{1},f_{2})\big]\geq(4-\varepsilon)(\bar{R}_{k}-\bar{R}_{2k}) . ∎

[155] h2: 4 Gradient Boosting

[156] p: In this section we apply our midpoint anchoring argument to gradient boosting , an algorithm that iteratively builds up an ensemble model by repeatedly chooses a weak learning model g ∈ 𝒞 g\in\mathcal{C} that correlates with the residual of our current ensemble model and then adds g g to it. Unlike stacking, the models that make up two independently trained ensembles f 1 f_{1} and f 2 f_{2} are not exchangeable, since the weak learners are not selected independently, but rather adaptively in a path dependent way. Nevertheless, we show that we can apply midpoint anchoring to drive disagreement to 0 0 at a 1 / k 1/k rate (where k k is the number of iterations of gradient boosting). Here we abstract away finite sample issues by modeling our weak learning algorithm in the style of an SQ oracle ( Kearns, 1998 ) — i.e. rather than obtaining the g ∈ 𝒞 g\in\mathcal{C} which exactly maximizes covariance with the residuals of our current model, it can return any g ∈ 𝒞 g\in\mathcal{C} that is an ϵ \epsilon -approximate maximizer. This models e.g. solving an ERM problem over any sample that is sufficient for ε \varepsilon -approximate uniform convergence over 𝒞 \mathcal{C} .

[157] p: We assume for simplicity that our weak learning class 𝒞 \mathcal{C} satisfies the following mild regularity conditions (which are enforceable if necessary): Symmetry ( g ∈ 𝒞 ⇒ − g ∈ 𝒞 g\in\mathcal{C}\Rightarrow-g\in\mathcal{C} ), normalization ( ‖ g ‖ ≤ 1 \|g\|\leq 1 for all g ∈ 𝒞 g\in\mathcal{C} ) and non-degeneracy ( 0 ∉ 𝒞 0\notin\mathcal{C} ).

[158] p: We will use the normalization condition with respect to the Atomic and Euclidean Norm, which can be enforced by dividing the original functions (unnormalized) by the maximum of its Atomic norm, Euclidean norm, and 1 1 . Note in this section, for the sake of clarity, we will use the standard inner product ⟨ f , g ⟩ = f T ​ g \langle f,g\rangle=f^{T}g . When we list ‖ f ‖ ||f|| it will still corresponding to the norm we defined in the Preliminaries of ( 𝔼 ⁡ [ f ​ ( x ) 2 ] ) 1 / 2 (\mathbb{E}[f(x)^{2}])^{1/2} . When needed, we will explicitly mention the expectations we are computing. We model weak-learning via an ε \varepsilon -approximate SQ-style oracle: at iteration t t , the oracle returns any g t ∈ 𝒞 g_{t}\in\mathcal{C} such that

[159] table: 𝔼 ⁡ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] ≥ sup g ∈ 𝒞 𝔼 ⁡ [ ⟨ r t − 1 ​ ( x ) , g ⁡ ( x ) ⟩ ] − ε t , r t − 1 := y − f t − 1 . \mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]\ \geq\ \sup_{g\in\mathcal{C}}\mathbb{E}[\langle r_{t-1}(x),g(x)\rangle]\ -\ \varepsilon_{t},\quad r_{t-1}:=y-f_{t-1}.

[160] figure: Algorithm 2 Gradient Boosting Input: SQ-oracle for weak learner class 𝒞 \mathcal{C} f 0 ≡ 0 f_{0}\equiv 0 , G 0 = ∅ G_{0}=\emptyset for t ∈ [ k ] t\in[k] do r t − 1 := y − f t − 1 r_{t-1}:=y-f_{t-1} Choose g t ∈ 𝒞 g_{t}\in\mathcal{C} with 𝔼 ⁡ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] ≥ sup g ∈ 𝒞 𝔼 ⁡ [ ⟨ r t − 1 ​ ( x ) , g ⁡ ( x ) ⟩ ] − ε t \mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]\geq\sup_{g\in\mathcal{C}}\mathbb{E}[\langle r_{t-1}(x),g(x)\rangle]-\varepsilon_{t} . (SQ-oracle) α t := arg ⁡ min α ∈ ℝ ⁡ 𝔼 ⁡ [ ( r t − 1 ​ ( x ) − α ​ g t ​ ( x ) ) 2 ] = 𝔼 ⁡ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] / ‖ g t ‖ 2 \alpha_{t}:=\arg\min_{\alpha\in\mathbb{R}}\mathbb{E}[(r_{t-1}(x)-\alpha g_{t}(x))^{2}]=\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]/\|g_{t}\|^{2} f t := f t − 1 + α t ​ g t f_{t}:=f_{t-1}+\alpha_{t}g_{t} ; set G t := G t − 1 ∪ { g t } G_{t}:=G_{t-1}\cup\{g_{t}\} end for return f k f_{k} and G := G k G:=G_{k}

[161] p: Algorithm 2 provides the details of how to use this oracle within the Gradient Boosting procedure. We will be interested in comparing the MSE of the gradient boosting iterates with the risk of the best minimizer in the weak learner class R ⁡ ( V ⁡ ( 𝒞 ) ) := inf f ∈ V ⁡ ( 𝒞 ) MSE ⁡ ( f ) R\big(V(\mathcal{C})\big)\ :=\ \inf_{f\in V(\mathcal{C})}\ \mathrm{MSE}(f) . We will bound the disagreement of two independently trained models f 1 f_{1} and f 2 f_{2} by anchoring to the best model f ∗ f^{*} in the span of the weak learner class 𝒞 \mathcal{C} , and then apply our anchoring lemma from Section 2 . Since anchoring bounds disagreement in terms of each model’s error gap to f ∗ f^{*} , it remains to upper bound that gap. We do so below, starting by bounding the single-step error improvement of gradient boosting.

[162] h6: Lemma 4.1 (Single Iterate Progress) .

[163] p: With α t = arg ⁡ min α ∈ ℝ ⁡ ‖ r t − 1 − α ​ g t ‖ 2 \alpha_{t}=\arg\min_{\alpha\in\mathbb{R}}\|r_{t-1}-\alpha g_{t}\|^{2} and ‖ g t ‖ ≤ 1 \|g_{t}\|\leq 1 ,

[164] table: MSE ⁡ ( f t − 1 ) − MSE ⁡ ( f t ) ≥ 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] 2 . \mathrm{MSE}(f_{t-1})-\mathrm{MSE}(f_{t})\ \geq\ \mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]^{2}.

[165] h6: Proof.

[166] p: Note that MSE ⁡ ( f t − 1 ) − MSE ⁡ ( f t ) = ‖ r t − 1 ‖ 2 − ‖ r t ‖ 2 = ‖ r t − 1 ‖ 2 − ‖ r t − 1 − α t ​ g t ‖ 2 \mathrm{MSE}(f_{t-1})-\mathrm{MSE}(f_{t})=||r_{t-1}||^{2}-||r_{t}||^{2}=||r_{t-1}||^{2}-||r_{t-1}-\alpha_{t}g_{t}||^{2} By exact line search,

[167] table: ‖ r t − 1 − α t ​ g t ‖ 2 \displaystyle\|r_{t-1}-\alpha_{t}g_{t}\|^{2} = min α ⁡ ‖ r t − 1 − α ​ g t ‖ 2 \displaystyle=\min_{\alpha}\|r_{t-1}-\alpha g_{t}\|^{2} = min α ⁡ ( ‖ r t − 1 ‖ 2 − 2 ​ α ​ 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] + α 2 ​ ‖ g t ‖ 2 ) \displaystyle=\min_{\alpha}(||r_{t-1}||^{2}-2\alpha\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]+\alpha^{2}||g_{t}||^{2}) = ‖ r t − 1 ‖ 2 − 2 ​ 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] 2 / ‖ g t ‖ 2 + 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] 2 / ‖ g t ‖ 2 \displaystyle=||r_{t-1}||^{2}-2\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]^{2}/\|g_{t}\|^{2}+\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]^{2}/\|g_{t}\|^{2} = ‖ r t − 1 ‖ 2 − 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] 2 / ‖ g t ‖ 2 \displaystyle=||r_{t-1}||^{2}-\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]^{2}/\|g_{t}\|^{2}

[168] p: Therefore, we have that MSE ⁡ ( f t − 1 ) − MSE ⁡ ( f t ) = 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] 2 / ‖ g t ‖ 2 \mathrm{MSE}(f_{t-1})-\mathrm{MSE}(f_{t})=\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]^{2}/\|g_{t}\|^{2} . Using ‖ g t ‖ ≤ 1 \|g_{t}\|\leq 1 gives the stated bound. ∎

[169] p: Now, we define the radius τ > 0 \tau>0 with the corresponding convex hull 𝒦 τ := τ ​ conv ​ ( 𝒞 ) \mathcal{K}_{\tau}:=\tau\mathrm{conv}(\mathcal{C}) . Let f ∗ ∈ V ⁡ ( 𝒞 ) f^{*}\in V(\mathcal{C}) be the population least-squares minimizer over the span of the weak learning class. Define the corresponding atomic norm radius τ ∗ := ‖ f ∗ ‖ 𝒜 \tau^{*}:=\|f^{*}\|_{\mathcal{A}} , where the atomic norm induced by 𝒞 \mathcal{C} is

[170] table: ∥ f ∥ 𝒜 := inf { ∑ j = 1 k | α j | : f = lim k → ∞ ∑ j = 1 k α j g j , g j ∈ 𝒞 , ∑ j = 1 k | α j | ≤ ∞ } . \|f\|_{\mathcal{A}}\ :=\ \inf\Big\{\sum_{j=1}^{k}|\alpha_{j}|:\ f=\lim_{k\rightarrow\infty}\sum_{j=1}^{k}\alpha_{j}g_{j},\ g_{j}\in\mathcal{C},\sum_{j=1}^{k}|\alpha_{j}|\leq\infty\Big\}.

[171] p: That is, τ ∗ \tau^{*} corresponds to the smallest total weight needed to represent f ∗ f^{*} within the weak learner class. We have now related the MSE gap between the models of two runs in terms of the square of the max correlation of the residuals of the earlier model with a model in the weak learner class. Next, we will lower bound the largest possible correlation between the residuals of a model f f and a function in the weak learner class in terms of the difference between the MSE of the current model f f and the error of the best model in the span of the weak learners, scaled by the atomic norm of f ∗ f^{*} .

[172] h6: Lemma 4.2 (Correlation Lower Bound w.r.t. Weak Learning Anchor Gap) .

[173] p: For any f f , writing M ⁡ ( f ) := sup g ∈ 𝒞 | 𝔼 ⁡ [ ⟨ y − f , g ⟩ ] | M(f):=\sup_{g\in\mathcal{C}}|\mathbb{E}[\langle y-f,g\rangle]| , we have

[174] table: M ⁡ ( f ) ≥ MSE ⁡ ( f ) − R ⁡ ( V ⁡ ( 𝒞 ) ) 2 ​ τ ∗ . M(f)\ \geq\ \frac{\mathrm{MSE}(f)-R\big(V(\mathcal{C})\big)}{2\,\tau^{*}}.

[175] h6: Proof.

[176] p: Recall that 𝒦 τ ∗ := τ ∗ ​ conv ​ ( 𝒞 ) \mathcal{K}_{\tau^{*}}:=\tau^{*}\,\mathrm{conv}(\mathcal{C}) . Its support function is σ 𝒦 τ ∗ ​ ( u ) := sup s ∈ 𝒦 τ ∗ 𝔼 ⁡ [ ⟨ u , s ⟩ ] = τ ∗ ​ sup g ∈ ± 𝒞 𝔼 ⁡ [ ⟨ u , g ⟩ ] \sigma_{\mathcal{K}_{\tau^{*}}}(u):=\sup_{s\in\mathcal{K}_{\tau^{*}}}\mathbb{E}[\langle u,s\rangle]=\tau^{*}\sup_{g\in\pm\mathcal{C}}\mathbb{E}[\langle u,g\rangle] . We will ultimately relate this quantity to M ⁡ ( f ) M(f) . For any s ∈ 𝒦 τ ∗ s\in\mathcal{K}_{\tau^{*}} , the squared loss obeys

[177] table: MSE ⁡ ( f ) − MSE ⁡ ( s ) = ‖ y − f ‖ 2 − ‖ y − s ‖ 2 = 2 ​ 𝔼 ​ [ ⟨ y − f , s − f ⟩ ] − ‖ s − f ‖ 2 ≤ 2 ​ 𝔼 ​ [ ( ⟨ y − f , s ⟩ − ⟨ y − f , f ⟩ ) ] . \mathrm{MSE}(f)-\mathrm{MSE}(s)\ =\ \|y-f\|^{2}-\|y-s\|^{2}\ =\ 2\mathbb{E}[\langle y-f,s-f\rangle]-\|s-f\|^{2}\ \leq\ 2\mathbb{E}[\big(\langle y-f,s\rangle-\langle y-f,f\rangle\big)].

[178] p: The second equality uses the fact that ‖ a ‖ 2 − ‖ b ‖ 2 = 2 ​ ⟨ a , a − b ⟩ − ‖ a − b ‖ 2 ||a||^{2}-||b||^{2}=2\langle a,a-b\rangle-||a-b||^{2} . The inequality uses the fact that we can drop the subtracted nonnegative term ‖ s − f ‖ 2 ||s-f||^{2} . Taking the supremum over s ∈ 𝒦 τ ∗ s\in\mathcal{K}_{\tau^{*}} yields

[179] table: MSE ⁡ ( f ) − R ⁡ ( 𝒦 τ ∗ ) ≤ 2 ​ σ 𝒦 τ ∗ ​ ( y − f ) − 2 ​ 𝔼 ​ [ ⟨ y − f ⁡ ( x ) , f ⁡ ( x ) ⟩ ] . \mathrm{MSE}(f)-R(\mathcal{K}_{\tau^{*}})\ \leq\ 2\,\sigma_{\mathcal{K}_{\tau^{*}}}(y-f)\ -\ 2\mathbb{E}[\langle y-f(x),f(x)\rangle].

[180] p: Applying the same inequality with f − y f-y in place of y − f y-f yields a second upper bound. Since any X X with X ≤ A X\leq A and X ≤ B X\leq B satisfies X ≤ ( A + B ) / 2 X\leq(A+B)/2 , averaging the two bounds cancels the unknown linear term ⟨ y − f , f ⟩ \langle y-f,f\rangle . Using evenness of the support function for symmetric sets, σ 𝒦 τ ∗ ​ ( u ) = σ 𝒦 τ ∗ ​ ( − u ) \sigma_{\mathcal{K}_{\tau^{*}}}(u)=\sigma_{\mathcal{K}_{\tau^{*}}}(-u) , we get

[181] table: MSE ⁡ ( f ) − R ⁡ ( 𝒦 τ ∗ ) \displaystyle\mathrm{MSE}(f)-R(\mathcal{K}_{\tau^{*}}) ≤ σ 𝒦 τ ∗ ​ ( y − f ) + σ 𝒦 τ ∗ ​ ( f − y ) \displaystyle\leq\ \sigma_{\mathcal{K}_{\tau^{*}}}(y-f)\ +\ \sigma_{\mathcal{K}_{\tau^{*}}}(f-y) = 2 ​ σ 𝒦 τ ∗ ​ ( y − f ) \displaystyle=\ 2\,\sigma_{\mathcal{K}_{\tau^{*}}}(y-f) = 2 ​ τ ∗ ​ sup g ∈ ± 𝒞 𝔼 ⁡ [ ⟨ y − f ⁡ ( x ) , g ⁡ ( x ) ⟩ ] \displaystyle=\ 2\,\tau^{*}\,\sup_{g\in\pm\mathcal{C}}\mathbb{E}[\langle y-f(x),g(x)\rangle] = 2 ​ τ ∗ ​ sup g ∈ 𝒞 | ⟨ 𝔼 ⁡ [ y − f ⁡ ( x ) , g ⁡ ( x ) ] ⟩ | \displaystyle=\ 2\,\tau^{*}\,\sup_{g\in\mathcal{C}}|\langle\mathbb{E}[y-f(x),g(x)]\rangle| = 2 ​ τ ∗ ​ M ​ ( f ) . \displaystyle=\ 2\,\tau^{*}\,M(f).

[182] p: where we used symmetry of 𝒦 τ ∗ \mathcal{K}_{\tau^{*}} and of 𝒞 \mathcal{C} . For any u u , the trivial inequality is sup g ∈ 𝒞 | ⟨ u , g ⟩ | ≥ sup g ∈ 𝒞 ⟨ u , g ⟩ \sup_{g\in\mathcal{C}}|\langle u,g\rangle|\geq\sup_{g\in\mathcal{C}}\langle u,g\rangle . Conversely, because 𝒞 \mathcal{C} is symmetric, for every g ∈ 𝒞 g\in\mathcal{C} also − g ∈ 𝒞 -g\in\mathcal{C} , so max ⁡ { ⟨ u , g ⟩ , ⟨ u , − g ⟩ } = | ⟨ u , g ⟩ | \max\{\langle u,g\rangle,\langle u,-g\rangle\}=|\langle u,g\rangle| , implying sup g ∈ 𝒞 ⟨ u , g ⟩ ≥ sup g ∈ 𝒞 | ⟨ u , g ⟩ | \sup_{g\in\mathcal{C}}\langle u,g\rangle\geq\sup_{g\in\mathcal{C}}|\langle u,g\rangle| . Thus sup g ∈ 𝒞 | ⟨ u , g ⟩ | = sup g ∈ 𝒞 ⟨ u , g ⟩ \sup_{g\in\mathcal{C}}|\langle u,g\rangle|=\sup_{g\in\mathcal{C}}\langle u,g\rangle . Taking u = y − f u=y-f identifies the last term with M ⁡ ( f ) M(f) . Since f ∗ ∈ 𝒦 τ ∗ ∩ V ⁡ ( 𝒞 ) f^{*}\in\mathcal{K}_{\tau^{*}}\cap V(\mathcal{C}) minimizes MSE \mathrm{MSE} over V ⁡ ( 𝒞 ) V(\mathcal{C}) , we have R ⁡ ( 𝒦 τ ∗ ) = R ⁡ ( V ⁡ ( 𝒞 ) ) R(\mathcal{K}_{\tau^{*}})=R\big(V(\mathcal{C})\big) . Rearranging yields

[183] table: M ⁡ ( f ) ≥ MSE ⁡ ( f ) − R ⁡ ( V ⁡ ( 𝒞 ) ) 2 ​ τ ∗ . M(f)\ \geq\ \frac{\mathrm{MSE}(f)-R\big(V(\mathcal{C})\big)}{2\,\tau^{*}}.

[184] p: ∎

[185] p: We have lower bounded the maximum residual–model correlation over the weak learner class by a quantity depending on the gap between the current model’s error and the best error in the weak-learner span. We now relate the per-step error gap to that best error via a recurrence.

[186] h6: Proposition 4.3 (Gap Recurrence Toward R ⁡ ( V ⁡ ( 𝒞 ) ) R\big(V(\mathcal{C})\big) ) .

[187] p: Let E t := MSE ⁡ ( f t ) − R ⁡ ( V ⁡ ( 𝒞 ) ) E_{t}:=\mathrm{MSE}(f_{t})-R\big(V(\mathcal{C})\big) . We will use the shorthand u + 2 = ( max ⁡ { u , 0 } ) 2 u_{+}^{2}=(\max\{u,0\})^{2} . Then, for t ≥ 1 t\geq 1 ,

[188] table: E t − 1 − E t ≥ ( E t − 1 2 ​ τ ∗ − ε t ) + 2 . E_{t-1}-E_{t}\ \geq\ \Big(\tfrac{E_{t-1}}{2\tau^{*}}-\varepsilon_{t}\Big)_{+}^{2}.

[189] h6: Proof.

[190] p: By Lemma 4.1 , MSE ⁡ ( f t − 1 ) − MSE ⁡ ( f t ) ≥ 𝔼 ​ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] 2 \mathrm{MSE}(f_{t-1})-\mathrm{MSE}(f_{t})\geq\mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]^{2} . The oracle gives 𝔼 ⁡ [ ⟨ r t − 1 ​ ( x ) , g t ​ ( x ) ⟩ ] ≥ M ⁡ ( f t − 1 ) − ε t \mathbb{E}[\langle r_{t-1}(x),g_{t}(x)\rangle]\geq M(f_{t-1})-\varepsilon_{t} . Hence 𝔼 ​ [ ⟨ r t − 1 , g t ⟩ ] 2 ≥ ( M ⁡ ( f t − 1 ) − ε t ) + 2 \mathbb{E}[\langle r_{t-1},g_{t}\rangle]^{2}\geq(M(f_{t-1})-\varepsilon_{t})_{+}^{2} . Finally, Lemma 4.2 gives M ⁡ ( f t − 1 ) ≥ E t − 1 / ( 2 ​ τ ∗ ) M(f_{t-1})\geq E_{t-1}/(2\tau^{*}) , yielding the claim. ∎

[191] p: Finally, we can use the recurrence relation to bound the difference between the MSE of the model at iteration t t and the MSE of the best model in the span of the weak learner class–we can see that the first term is inversely proportional to t t and depends on the atomic norm of the best model in span of the weak learner class. It also includes a term that depends on the SQ-oracle error at every iteration.

[192] h6: Theorem 4.4 (Weak Learning Anchor Gap Upper Bound) .

[193] p: For all t ≥ 1 t\geq 1 ,

[194] table: MSE ⁡ ( f t ) − R ⁡ ( V ⁡ ( 𝒞 ) ) ≤ 8 ​ ( τ ∗ ) 2 t + ∑ s = 1 t ε s 2 . \mathrm{MSE}(f_{t})-R\big(V(\mathcal{C})\big)\ \leq\ \frac{8\,(\tau^{*})^{2}}{t}\ +\ \sum_{s=1}^{t}\varepsilon_{s}^{2}.

[195] h6: Proof.

[196] p: Let E t := MSE ⁡ ( f t ) − R ⁡ ( V ⁡ ( 𝒞 ) ) E_{t}:=\mathrm{MSE}(f_{t})-R\big(V(\mathcal{C})\big) . From Proposition 4.3 ,

[197] table: E t − 1 − E t ≥ ( E t − 1 2 ​ τ ∗ − ε t ) + 2 . E_{t-1}-E_{t}\ \geq\ \Big(\tfrac{E_{t-1}}{2\tau^{*}}-\varepsilon_{t}\Big)_{+}^{2}.

[198] p: For any a ≥ 0 a\geq 0 and b ∈ ℝ b\in\mathbb{R} , ( a − b ) 2 ≥ a 2 / 2 − b 2 (a-b)^{2}\geq a^{2}/2-b^{2} . To see this, consider: a 2 − 2 ​ a ​ b + b 2 − a 2 / 2 + b 2 a^{2}-2ab+b^{2}-a^{2}/2+b^{2} . We have that this quantity equals a 2 / 2 − 2 ​ a ​ b + 2 ​ b 2 a^{2}/2-2ab+2b^{2} . Since a multiplicative factor of 2 2 does not affect the sign, notice that twice this quantity is equal to ( a − 2 ​ b ) 2 (a-2b)^{2} which is non-negative. In this case the inequality also holds for the quantity ( ( a − b ) + ) 2 ((a-b)_{+})^{2} . Taking a = E t − 1 / ( 2 ​ τ ∗ ) a=E_{t-1}/(2\tau^{*}) and b = ε t b=\varepsilon_{t} yields

[199] table: E t − 1 − E t ≥ E t − 1 2 8 ​ ( τ ∗ ) 2 − ε t 2 . E_{t-1}-E_{t}\ \geq\ \frac{E_{t-1}^{2}}{8\,(\tau^{*})^{2}}\ -\ \varepsilon_{t}^{2}.

[200] p: Since E t ≤ E t − 1 E_{t}\leq E_{t-1} ,

[201] table: 1 E t − 1 E t − 1 = E t − 1 − E t E t ​ E t − 1 ≥ E t − 1 − E t E t − 1 2 ≥ 1 8 ​ ( τ ∗ ) 2 − ε t 2 E t − 1 2 ≥ 1 8 ​ ( τ ∗ ) 2 − ε t 2 E t 2 . \frac{1}{E_{t}}-\frac{1}{E_{t-1}}\ =\ \frac{E_{t-1}-E_{t}}{E_{t}E_{t-1}}\ \geq\ \frac{E_{t-1}-E_{t}}{E_{t-1}^{2}}\ \geq\ \frac{1}{8\,(\tau^{*})^{2}}\ -\ \frac{\varepsilon_{t}^{2}}{E_{t-1}^{2}}\ \geq\ \frac{1}{8\,(\tau^{*})^{2}}\ -\ \frac{\varepsilon_{t}^{2}}{E_{t}^{2}}.

[202] p: Summing from s = 1 s=1 to t t gives

[203] table: 1 E t ≥ 1 E 0 + t 8 ​ ( τ ∗ ) 2 − ∑ s = 1 t ε s 2 E s 2 ≥ 1 E 0 + t 8 ​ ( τ ∗ ) 2 − 1 E t 2 ​ ∑ s = 1 t ε s 2 . \frac{1}{E_{t}}\ \geq\ \frac{1}{E_{0}}\ +\ \frac{t}{8\,(\tau^{*})^{2}}\ -\ \sum_{s=1}^{t}\frac{\varepsilon_{s}^{2}}{E_{s}^{2}}\geq\frac{1}{E_{0}}\ +\ \frac{t}{8\,(\tau^{*})^{2}}\ -\ \frac{1}{E_{t}^{2}}\sum_{s=1}^{t}\varepsilon_{s}^{2}.

[204] p: Let A t := ∑ s = 1 t ε s 2 A_{t}:=\sum_{s=1}^{t}\varepsilon_{s}^{2} and B t := 1 E 0 + t 8 ​ ( τ ∗ ) 2 B_{t}:=\frac{1}{E_{0}}+\frac{t}{8\,(\tau^{*})^{2}} . Writing X := 1 / E t X:=1/E_{t} , the inequality becomes A t ​ X 2 + X − B t ≥ 0 A_{t}X^{2}+X-B_{t}\geq 0 . If A t = 0 A_{t}=0 then X ≥ B t X\geq B_{t} and E t ≤ 1 / B t ≤ 8 ​ ( τ ∗ ) 2 / t E_{t}\leq 1/B_{t}\leq 8(\tau^{*})^{2}/t . If A t > 0 A_{t}>0 , define the quantity Y = 1 / X Y=1/X . Then, the inequality becomes − B t ​ Y 2 + Y + A t ≥ 0 -B_{t}Y^{2}+Y+A_{t}\geq 0 . Then the quadratic inequality implies Y ≤ 1 + 1 + 4 ​ A t ​ B t 2 ​ B t Y\leq\frac{1+\sqrt{1+4A_{t}B_{t}}}{2B_{t}} . Using 1 + z ≤ 1 + z / 2 \sqrt{1+z}\leq 1+z/2 for z ≥ 0 z\geq 0 gives

[205] table: 1 X ≤ 1 B t + A t . \frac{1}{X}\ \leq\ \frac{1}{B_{t}}\ +\ A_{t}.

[206] p: Thus E t ≤ 1 / B t + A t ≤ 8 ​ ( τ ∗ ) 2 / t + ∑ s = 1 t ε s 2 E_{t}\leq 1/B_{t}+A_{t}\leq 8(\tau^{*})^{2}/t+\sum_{s=1}^{t}\varepsilon_{s}^{2} . ∎

[207] p: We can now use the anchoring lemmas from Section 2 to relate two independent stagewise runs.

[208] h6: Theorem 4.5 (Gradient Boosting Agreement Bound) .

[209] p: Let f 1 f_{1} and f 2 f_{2} be two independent gradient boosting runs (using the same weak learning class 𝒞 \mathcal{C} and number of iterations k k ) driven by { ε t } \{\varepsilon_{t}\} and { ε t ′ } \{\varepsilon^{\prime}_{t}\} respectively. Let f ∗ ∈ V ⁡ ( 𝒞 ) f^{*}\in V(\mathcal{C}) denote the population least-squares predictor over V ⁡ ( 𝒞 ) V(\mathcal{C}) . Then

[210] table: D ⁡ ( f 1 , f 2 ) ≤ 2 ​ ( MSE ⁡ ( f 1 ) − R ⁡ ( V ⁡ ( 𝒞 ) ) ) + 2 ​ ( MSE ⁡ ( f 2 ) − R ⁡ ( V ⁡ ( 𝒞 ) ) ) . D(f_{1},f_{2})\ \leq\ 2\big(\mathrm{MSE}(f_{1})-R\big(V(\mathcal{C})\big)\big)\ +\ 2\big(\mathrm{MSE}(f_{2})-R\big(V(\mathcal{C})\big)\big).

[211] p: Consequently, using Theorem 4.4 , for all k ≥ 1 k\geq 1 ,

[212] table: D ⁡ ( f 1 , f 2 ) ≤ 32 ​ ( τ ∗ ) 2 k + 2 ​ ( ∑ t = 1 k ε t 2 + ∑ t = 1 k ε t ′ 2 ) . D(f_{1},f_{2})\ \leq\ \frac{32\,(\tau^{*})^{2}}{k}\ +\ 2\Big(\sum_{t=1}^{k}\varepsilon_{t}^{2}\ +\ \sum_{t=1}^{k}\varepsilon_{t}^{\prime 2}\Big).

[213] h6: Proof.

[214] p: Let f ¯ := 1 2 ​ ( f 1 + f 2 ) \bar{f}:=\tfrac{1}{2}(f_{1}+f_{2}) . Since each gradient boosting run outputs a predictor in V ⁡ ( 𝒞 ) V(\mathcal{C}) , we have f ¯ ∈ V ⁡ ( 𝒞 ) \bar{f}\in V(\mathcal{C}) . Applying Lemma 2.3 with ℋ = V ⁡ ( 𝒞 ) \mathcal{H}=V(\mathcal{C}) gives

[215] table: D ⁡ ( f 1 , f 2 ) ≤ 2 ​ ( MSE ⁡ ( f 1 ) − R ⁡ ( V ⁡ ( 𝒞 ) ) ) + 2 ​ ( MSE ⁡ ( f 2 ) − R ⁡ ( V ⁡ ( 𝒞 ) ) ) . D(f_{1},f_{2})\ \leq\ 2\big(\mathrm{MSE}(f_{1})-R(V(\mathcal{C}))\big)\ +\ 2\big(\mathrm{MSE}(f_{2})-R(V(\mathcal{C}))\big).

[216] p: Applying Theorem 4.4 to both runs yields the stated bound. ∎

[217] p: Thus we have shown that gradient boosting yields independent agreement tending to 0 0 at a rate of O ⁡ ( 1 / k ) O(1/k) , where k k is the number of iterations. This bound also depends on τ ∗ \tau^{*} , which is a problem-dependent constant. In Section 6 we analyze a variant of gradient boosting based on the Frank Wolfe algorithm (for more general loss functions) that always produces a predictor that has norm at most τ \tau , where τ \tau is a user defined parameter. We give a variant of this analysis in which we anchor to the best model in the span of the weak learner class that also has norm at most τ \tau . This removes any dependence on τ ∗ \tau^{*} , and obtain similar rates depending only on τ \tau — replacing the problem dependent constant with a user defined parameter that trades of agreement with accuracy as desired.

[218] h2: 5 Neural Networks, Regression Trees, and Other Classes Satisfying Hierarchical Midpoint Closure

[219] p: Next, we show that certain function classes including ReLU neural networks and regression trees admit strong agreement bounds under approximate population loss minimization. These function classes may be highly non-convex, meaning that approximate loss minimizers may be very far in parameter space—or even incomparable in the sense that they may be of different architectures. Nevertheless, by anchoring on the midpoint predictor f ¯ ​ ( x ) = 1 2 ​ ( f 1 ​ ( x ) + f 2 ​ ( x ) ) \bar{f}(x)=\tfrac{1}{2}(f_{1}(x)+f_{2}(x)) and using that the relevant model classes are closed under averaging we show that they must be close in prediction space . We will use Lemma 2.4 from Section 2 . To apply it, we need midpoint closure of the form f ¯ ∈ ℱ 2 ​ n \bar{f}\in\mathcal{F}_{2n} whenever f 1 , f 2 ∈ ℱ n f_{1},f_{2}\in\mathcal{F}_{n} . The form of our theorems will be identical for any class satisfying this kind of “hierarchical midpoint closure”.

[220] h3: 5.1 Application to Neural Networks

[221] p: We work with feed-forward ReLU networks. Let σ ⁡ ( t ) := max ⁡ { 0 , t } \sigma(t):=\max\{0,t\} denote the ReLU activation. For n ≥ 0 n\geq 0 , let NN n \mathrm{NN}_{n} denote the class of functions f : 𝒳 → 𝒴 f:\mathcal{X}\to\mathcal{Y} computable by a finite directed acyclic graph in which each internal (non-input, non-output) node computes σ ⁡ ( ⟨ w , u ⟩ + b ) \sigma(\langle w,u\rangle+b) for some affine function of its inputs, and the output node computes an affine combination of the values at the input coordinates and internal nodes. First, we demonstrate midpoint closure for this class.

[222] h6: Lemma 5.1 (Neural-network midpoint closure) .

[223] p: For every n ≥ 0 n\geq 0 and every f 1 , f 2 ∈ NN n f_{1},f_{2}\in\mathrm{NN}_{n} , the midpoint predictor f ¯ := 1 2 ​ ( f 1 + f 2 ) \bar{f}:=\tfrac{1}{2}(f_{1}+f_{2}) lies in NN 2 ​ n \mathrm{NN}_{2n} .

[224] h6: Proof.

[225] p: Fix realizations of f 1 f_{1} and f 2 f_{2} as ReLU networks with at most n n internal nodes each. Construct a new network by taking a disjoint copy of the internal computation graph for each of f 1 f_{1} and f 2 f_{2} , and wiring both copies to the same input x x . This yields a single feed-forward network that computes both f 1 ​ ( x ) f_{1}(x) and f 2 ​ ( x ) f_{2}(x) in parallel, using at most 2 ​ n 2n internal ReLU nodes.

[226] p: Define the output node to return the affine combination 1 2 ​ f 1 ​ ( x ) + 1 2 ​ f 2 ​ ( x ) \tfrac{1}{2}f_{1}(x)+\tfrac{1}{2}f_{2}(x) . This adds no new internal nodes, so the resulting network computes f ¯ \bar{f} and has size at most 2 ​ n 2n , i.e., f ¯ ∈ NN 2 ​ n \bar{f}\in\mathrm{NN}_{2n} . ∎

[227] h6: Corollary 5.2 (Neural-network agreement) .

[228] p: Fix n ≥ 1 n\geq 1 and ε > 0 \varepsilon>0 . If f 1 , f 2 ∈ NN n f_{1},f_{2}\in\mathrm{NN}_{n} satisfy MSE ⁡ ( f i ) ≤ R ⁡ ( NN n ) + ε \mathrm{MSE}(f_{i})\leq R(\mathrm{NN}_{n})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} , then

[229] table: D ⁡ ( f 1 , f 2 ) ≤ 4 ​ ( R ⁡ ( NN n ) − R ⁡ ( NN 2 ​ n ) + ε ) . D(f_{1},f_{2})\,\leq\,4\big(R(\mathrm{NN}_{n})-R(\mathrm{NN}_{2n})+\varepsilon\big).

[230] h6: Proof.

[231] p: Apply Lemma 2.4 with ℱ n = NN n \mathcal{F}_{n}=\mathrm{NN}_{n} and use Lemma 5.1 . ∎

[232] p: Observe that this is exactly the same form of local learning curve guarantee that we got for Stacking in Theorem 3.1 . In particular, as loss is bounded and optimal loss is monotonically decreasing in network size, for any value of α \alpha , there must be a value of n ≤ 2 1 / α n\leq 2^{1/\alpha} such that R ⁡ ( NN n ) − R ⁡ ( NN 2 ​ n ) ≤ α R(\mathrm{NN}_{n})-R(\mathrm{NN}_{2n})\leq\alpha (as error can drop by α \alpha at most 1 / α 1/\alpha times before contradicting the non-negativity of squared error). For such a value of n n , we have D ⁡ ( f 1 , f 2 ) ≤ 4 ​ ( α + ϵ ) D(f_{1},f_{2})\leq 4(\alpha+\epsilon) . As with stacking, this bound is completely independent of the complexity of the instance and does not require that “global optimality” can be obtained by a small neural network (i.e. it requires only flatness of the local loss curve, which can always be guaranteed at modest values of n n , not the global loss curve, which cannot). This kind of “learning curve” bound for neural networks is reminiscent of the argument used by Błasiok et al. (2024) to show that “most sizes” of ReLU networks are approximately multicalibrated with respect to all neural network architectures of bounded size.

[233] h3: 5.2 Application to Regression Trees

[234] p: We observe that the same arguments apply almost verbatim to regression trees. We work with axis-aligned regression trees. A depth- d d tree is a rooted binary tree in which every internal node is labeled by a coordinate j ∈ [ d ] j\in[d] and a threshold t ∈ ℝ t\in\mathbb{R} , and routes an input x ∈ 𝒳 ⊆ ℝ d x\in\mathcal{X}\subseteq\mathbb{R}^{d} to the left or right child depending on whether x j ≤ t x_{j}\leq t or x j > t x_{j}>t . Each leaf is labeled by a constant prediction value in [ 0 , 1 ] [0,1] . The predictor computed by the tree is the leaf value reached by x x . We write 𝖳𝗋𝖾𝖾 d \mathsf{Tree}_{d} for the class of such predictors of depth at most d d .

[235] h6: Lemma 5.3 (Regression-tree midpoint closure) .

[236] p: For every d ≥ 0 d\geq 0 and every f 1 , f 2 ∈ 𝖳𝗋𝖾𝖾 d f_{1},f_{2}\in\mathsf{Tree}_{d} , the midpoint predictor f ¯ := 1 2 ​ ( f 1 + f 2 ) \bar{f}:=\tfrac{1}{2}(f_{1}+f_{2}) lies in 𝖳𝗋𝖾𝖾 2 ​ d \mathsf{Tree}_{2d} .

[237] h6: Proof.

[238] p: Fix realizations of f 1 , f 2 ∈ 𝖳𝗋𝖾𝖾 d f_{1},f_{2}\in\mathsf{Tree}_{d} as depth- d d trees. Consider the partition of 𝒳 \mathcal{X} induced by the leaves of the tree for f 1 f_{1} ; on each cell of this partition, f 1 f_{1} is constant. Now refine each such cell further using the splits of the tree for f 2 f_{2} restricted to that cell.

[239] p: Equivalently, we can construct a single tree as follows: take the tree for f 1 f_{1} , and at each leaf, graft a copy of the tree for f 2 f_{2} . Along any root-to-leaf path, we traverse at most d d splits from f 1 f_{1} and then at most d d splits from f 2 f_{2} , so the resulting tree has depth at most 2 ​ d 2d . Moreover, on each leaf of the resulting tree, both f 1 f_{1} and f 2 f_{2} take constant values, so we can label that leaf with their average 1 2 ​ f 1 ​ ( x ) + 1 2 ​ f 2 ​ ( x ) ∈ [ 0 , 1 ] \tfrac{1}{2}f_{1}(x)+\tfrac{1}{2}f_{2}(x)\in[0,1] . This yields a depth- 2 ​ d 2d regression tree computing f ¯ \bar{f} , i.e., f ¯ ∈ 𝖳𝗋𝖾𝖾 2 ​ d \bar{f}\in\mathsf{Tree}_{2d} . ∎

[240] p: We now get an immediate corollary:

[241] h6: Corollary 5.4 (Regression tree agreement) .

[242] p: Fix d ≥ 1 d\geq 1 and ε > 0 \varepsilon>0 . If f 1 , f 2 ∈ 𝖳𝗋𝖾𝖾 d f_{1},f_{2}\in\mathsf{Tree}_{d} satisfy MSE ⁡ ( f i ) ≤ R ⁡ ( 𝖳𝗋𝖾𝖾 d ) + ε \mathrm{MSE}(f_{i})\leq R(\mathsf{Tree}_{d})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} , then

[243] table: D ⁡ ( f 1 , f 2 ) ≤ 4 ​ ( R ⁡ ( 𝖳𝗋𝖾𝖾 d ) − R ⁡ ( 𝖳𝗋𝖾𝖾 2 ​ d ) + ε ) . D(f_{1},f_{2})\,\leq\,4\big(R(\mathsf{Tree}_{d})-R(\mathsf{Tree}_{2d})+\varepsilon\big).

[244] h6: Proof.

[245] p: Apply Lemma 2.4 with ℱ d = 𝖳𝗋𝖾𝖾 d \mathcal{F}_{d}=\mathsf{Tree}_{d} and use Lemma 5.3 . ∎

[246] p: Again, this is a local learning curve agreement guarantee of exactly the same form as our theorem for Stacking (Theorem 3.1 ) and our theorem for neural network training (Corollary 5.2 ). An immediate implication is that for any value of α \alpha that there is a value d ≤ 2 1 / α d\leq 2^{1/\alpha} (i.e. independent of the complexity of the instance) guaranteeing that for that value of d d , D ⁡ ( f 1 , f 2 ) ≤ 4 ​ ( α + ϵ ) D(f_{1},f_{2})\leq 4(\alpha+\epsilon) .

[247] h2: 6 Generalization to Multi-Dimensional Strongly Convex Losses

[248] p: In this section we generalize our setting to study models that output d d -dimensional distributions as predictions, and optimize arbitrary strongly convex losses. We show that the midpoint anchoring argument extends directly to this more general setting, which lets us model a wide array of practical machine learning problems. First we define general strongly convex loss functions over d d dimensional predictions:

[249] h6: Definition 6.1 (Strongly convex losses) .

[250] p: Let ℒ : 𝒴 × ℝ d → ℝ \mathcal{L}:\mathcal{Y}\times\mathbb{R}^{d}\rightarrow\mathbb{R} be a continuously differentiable loss function. We say that ℒ \mathcal{L} is μ \mu -strongly convex if there exists some μ > 0 \mu>0 such that for every y ∈ 𝒴 y\in\mathcal{Y} , P 1 , P 2 ∈ ℝ d P_{1},P_{2}\in\mathbb{R}^{d} ,

[251] table: ℒ ⁡ ( y , P 1 ) ≥ ℒ ⁡ ( y , P 2 ) + ⟨ ∇ p ℒ ​ ( y , P 2 ) , P 1 − P 2 ⟩ + μ 2 ​ ‖ P 1 − P 2 ‖ 2 2 . \mathcal{L}(y,P_{1})\geq\mathcal{L}(y,P_{2})+\langle\nabla_{p}\mathcal{L}(y,P_{2}),P_{1}-P_{2}\rangle+\tfrac{\mu}{2}\|P_{1}-P_{2}\|_{2}^{2}.

[252] p: For predictors outputting d d -dimensional predictions, we define disagreement as follows, straightforwardly generalizing our 1 1 -dimensional expected squared disagreement metric:

[253] h6: Definition 6.2 (Generalized disagreement) .

[254] p: Let P P be a distribution on 𝒳 × 𝒴 \mathcal{X}\times\mathcal{Y} and let f 1 , f 2 : 𝒳 → ℝ d f_{1},f_{2}:\mathcal{X}\rightarrow\mathbb{R}^{d} be functions. The disagreement between f 1 , f 2 f_{1},f_{2} over P P is the expected squared Euclidean distance between their predictions:

[255] table: D ⁡ ( f 1 , f 2 ) = 𝔼 ⁡ [ ‖ f 1 ​ ( x ) − f 2 ​ ( x ) ‖ 2 2 ] . D(f_{1},f_{2})=\mathbb{E}[\|f_{1}(x)-f_{2}(x)\|_{2}^{2}].

[256] p: We will write R ⁡ ( f ) := 𝔼 ⁡ [ ℒ ⁡ ( y , f ⁡ ( x ) ) ] R(f):=\mathbb{E}[\mathcal{L}(y,f(x))] . We can now generalize our disagreement-via-midpoint-anchoring lemma which drives our analyses.

[257] h6: Lemma 6.3 (Disagreement via the midpoint anchor) .

[258] p: Assume ℒ \mathcal{L} is μ \mu -strongly convex. For any two functions f 1 , f 2 : 𝒳 → ℝ d f_{1},f_{2}:\mathcal{X}\to\mathbb{R}^{d} , let f ¯ ​ ( x ) := 1 2 ​ ( f 1 ​ ( x ) + f 2 ​ ( x ) ) \bar{f}(x):=\tfrac{1}{2}(f_{1}(x)+f_{2}(x)) . Then

[259] table: D ⁡ ( f 1 , f 2 ) ≤ 4 μ ​ ( R ⁡ ( f 1 ) + R ⁡ ( f 2 ) − 2 ​ R ​ ( f ¯ ) ) . D(f_{1},f_{2})\,\leq\,\tfrac{4}{\mu}\Big(R(f_{1})+R(f_{2})-2R(\bar{f})\Big).

[260] p: In particular, if f ¯ ∈ ℋ \bar{f}\in\mathcal{H} for some class of predictors ℋ \mathcal{H} , then

[261] table: D ⁡ ( f 1 , f 2 ) ≤ 4 μ ​ ( R ⁡ ( f 1 ) − R ⁡ ( ℋ ) ) + 4 μ ​ ( R ⁡ ( f 2 ) − R ⁡ ( ℋ ) ) . D(f_{1},f_{2})\,\leq\,\tfrac{4}{\mu}\big(R(f_{1})-R(\mathcal{H})\big)+\tfrac{4}{\mu}\big(R(f_{2})-R(\mathcal{H})\big).

[262] h6: Proof.

[263] p: Fix any x ∈ 𝒳 x\in\mathcal{X} and y ∈ 𝒴 y\in\mathcal{Y} and abbreviate

[264] table: p 1 := f 1 ​ ( x ) , p 2 := f 2 ​ ( x ) , p ¯ := f ¯ ​ ( x ) = 1 2 ​ ( p 1 + p 2 ) . p_{1}:=f_{1}(x),\quad p_{2}:=f_{2}(x),\quad\bar{p}:=\bar{f}(x)=\tfrac{1}{2}(p_{1}+p_{2}).

[265] p: Applying μ \mu -strong convexity (Definition 6.1 ) with P 1 = p 1 P_{1}=p_{1} and P 2 = p ¯ P_{2}=\bar{p} gives

[266] table: ℒ ⁡ ( y , p 1 ) ≥ ℒ ⁡ ( y , p ¯ ) + ⟨ ∇ p ℒ ​ ( y , p ¯ ) , p 1 − p ¯ ⟩ + μ 2 ​ ‖ p 1 − p ¯ ‖ 2 2 . \mathcal{L}(y,p_{1})\geq\mathcal{L}(y,\bar{p})+\langle\nabla_{p}\mathcal{L}(y,\bar{p}),\,p_{1}-\bar{p}\rangle+\tfrac{\mu}{2}\|p_{1}-\bar{p}\|_{2}^{2}.

[267] p: Similarly, with P 1 = p 2 P_{1}=p_{2} and P 2 = p ¯ P_{2}=\bar{p} ,

[268] table: ℒ ⁡ ( y , p 2 ) ≥ ℒ ⁡ ( y , p ¯ ) + ⟨ ∇ p ℒ ​ ( y , p ¯ ) , p 2 − p ¯ ⟩ + μ 2 ​ ‖ p 2 − p ¯ ‖ 2 2 . \mathcal{L}(y,p_{2})\geq\mathcal{L}(y,\bar{p})+\langle\nabla_{p}\mathcal{L}(y,\bar{p}),\,p_{2}-\bar{p}\rangle+\tfrac{\mu}{2}\|p_{2}-\bar{p}\|_{2}^{2}.

[269] p: Adding the two inequalities, and using ( p 1 − p ¯ ) + ( p 2 − p ¯ ) = p 1 + p 2 − 2 ​ p ¯ = 0 (p_{1}-\bar{p})+(p_{2}-\bar{p})=p_{1}+p_{2}-2\bar{p}=0 to cancel the gradient terms, yields

[270] table: ℒ ⁡ ( y , p 1 ) + ℒ ⁡ ( y , p 2 ) ≥ 2 ​ ℒ ​ ( y , p ¯ ) + μ 2 ​ ( ‖ p 1 − p ¯ ‖ 2 2 + ‖ p 2 − p ¯ ‖ 2 2 ) . \mathcal{L}(y,p_{1})+\mathcal{L}(y,p_{2})\geq 2\mathcal{L}(y,\bar{p})+\tfrac{\mu}{2}\Big(\|p_{1}-\bar{p}\|_{2}^{2}+\|p_{2}-\bar{p}\|_{2}^{2}\Big).

[271] p: Since p 1 − p ¯ = 1 2 ​ ( p 1 − p 2 ) p_{1}-\bar{p}=\tfrac{1}{2}(p_{1}-p_{2}) and p 2 − p ¯ = 1 2 ​ ( p 2 − p 1 ) p_{2}-\bar{p}=\tfrac{1}{2}(p_{2}-p_{1}) , we have

[272] table: ‖ p 1 − p ¯ ‖ 2 2 + ‖ p 2 − p ¯ ‖ 2 2 = 2 ​ ‖ 1 2 ​ ( p 1 − p 2 ) ‖ 2 2 = 1 2 ​ ‖ p 1 − p 2 ‖ 2 2 . \|p_{1}-\bar{p}\|_{2}^{2}+\|p_{2}-\bar{p}\|_{2}^{2}=2\Big\|\tfrac{1}{2}(p_{1}-p_{2})\Big\|_{2}^{2}=\tfrac{1}{2}\|p_{1}-p_{2}\|_{2}^{2}.

[273] p: Substituting this back and rearranging gives the pointwise bound

[274] table: ‖ f 1 ​ ( x ) − f 2 ​ ( x ) ‖ 2 2 ≤ 4 μ ​ ( ℒ ⁡ ( y , f 1 ​ ( x ) ) + ℒ ⁡ ( y , f 2 ​ ( x ) ) − 2 ​ ℒ ​ ( y , f ¯ ​ ( x ) ) ) . \|f_{1}(x)-f_{2}(x)\|_{2}^{2}\leq\tfrac{4}{\mu}\Big(\mathcal{L}(y,f_{1}(x))+\mathcal{L}(y,f_{2}(x))-2\mathcal{L}\big(y,\bar{f}(x)\big)\Big).

[275] p: Taking expectations over ( x , y ) ∼ P (x,y)\sim P and using the definitions of D ⁡ ( ⋅ , ⋅ ) D(\cdot,\cdot) and R ⁡ ( ⋅ ) R(\cdot) yields

[276] table: D ⁡ ( f 1 , f 2 ) ≤ 4 μ ​ ( R ⁡ ( f 1 ) + R ⁡ ( f 2 ) − 2 ​ R ​ ( f ¯ ) ) . D(f_{1},f_{2})\leq\tfrac{4}{\mu}\Big(R(f_{1})+R(f_{2})-2R(\bar{f})\Big).

[277] p: For the second inequality, if f ¯ ∈ ℋ \bar{f}\in\mathcal{H} then R ⁡ ( f ¯ ) ≥ R ⁡ ( ℋ ) R(\bar{f})\geq R(\mathcal{H}) , so substituting R ⁡ ( f ¯ ) R(\bar{f}) by R ⁡ ( ℋ ) R(\mathcal{H}) in the right-hand side yields the claim. ∎

[278] p: We now show how to apply the midpoint anchoring lemma to each of our (generalized) applications.

[279] h3: 6.1 Stacking

[280] p: Here, we will provide a generalization of our stacking results to multi-dimensional strongly-convex losses. We once again model “base models” as being sampled i.i.d. from an arbitrary distribution Q Q , and under two independent training runs write G , G ′ ∼ Q k G,G^{\prime}\sim Q^{k} to denote the set of k k sampled models. We will consider the stacked predictors f 1 ∈ V ⁡ ( G ) f_{1}\in V(G) and f 2 ∈ V ⁡ ( G ′ ) f_{2}\in V(G^{\prime}) . Define G ∗ = G ∪ G ′ G^{*}=G\cup G^{\prime} . The key observation is that the midpoint predictor 1 2 ​ ( f 1 + f 2 ) \tfrac{1}{2}(f_{1}+f_{2}) lies in V ⁡ ( G ∗ ) V(G^{*}) , so we can apply Lemma 6.3 and then use the same exchangeability argument as in the single-dimensional case.

[281] h6: Theorem 6.4 .

[282] p: (Agreement for Stacked Aggregation Generalization) Assume that ℒ \mathcal{L} is μ \mu -strongly convex. Let G = { g 1 , … , g k } ∼ i.i.d. Q k G=\{g_{1},\dots,g_{k}\}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{k} and G ′ = { g 1 ′ , … , g k ′ } ∼ i.i.d. Q k G^{\prime}=\{g^{\prime}_{1},\dots,g^{\prime}_{k}\}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{k} be independent. Define f 1 , f 2 f_{1},f_{2} as follows:

[283] table: f 1 = arg ⁡ min f ∈ V ⁡ ( G ) ⁡ 𝔼 ⁡ [ ℒ ⁡ ( y , f ⁡ ( x ) ) ] , f 2 = arg ⁡ min f ∈ V ⁡ ( G ′ ) ⁡ 𝔼 ⁡ [ ℒ ⁡ ( y , f ⁡ ( x ) ) ] f_{1}=\arg\min_{f\in V(G)}\mathbb{E}[\mathcal{L}(y,f(x))],\quad f_{2}=\arg\min_{f\in V(G^{\prime})}\mathbb{E}[\mathcal{L}(y,f(x))]

[284] p: Then we have that

[285] table: 𝔼 f 1 , f 2 ​ [ D ⁡ ( f 1 , f 2 ) ] ≤ 8 μ ​ ( R ¯ k − R ¯ 2 ​ k ) . \mathbb{E}_{f_{1},f_{2}}\big[D(f_{1},f_{2})]\;\leq\;\frac{8}{\mu}\big(\bar{R}_{k}-\bar{R}_{2k}\big).

[286] h6: Proof.

[287] p: Fix realizations of G G and G ′ G^{\prime} , and let G ∗ = G ∪ G ′ G^{*}=G\cup G^{\prime} (multiset union ). Throughout this section we will think of G , G ′ ∼ Q k G,G^{\prime}\sim Q^{k} , unless explicitly conditioned. Note that V ⁡ ( G ) ⊆ V ⁡ ( G ∗ ) V(G)\subseteq V(G^{*}) and V ⁡ ( G ′ ) ⊆ V ⁡ ( G ∗ ) V(G^{\prime})\subseteq V(G^{*}) . In our proofs, without loss of generality, we will use the notation h G h_{G} to denote the minimizer of 𝔼 ⁡ [ ℒ ⁡ ( y , ⋅ ) ] \mathbb{E}[\mathcal{L}(y,\cdot)] with respect to subspace G G . Similarly, we will use the notation R ⁡ ( G ) = R ⁡ ( h G ) R(G)=R(h_{G}) in this context. In our theorem statements, this corresponds to f 1 f_{1} . Let h ¯ := 1 2 ​ ( h G + h G ′ ) \bar{h}:=\tfrac{1}{2}(h_{G}+h_{G^{\prime}}) . Since h G ∈ V ⁡ ( G ) h_{G}\in V(G) and h G ′ ∈ V ⁡ ( G ′ ) h_{G^{\prime}}\in V(G^{\prime}) and V ⁡ ( G ) , V ⁡ ( G ′ ) ⊆ V ⁡ ( G ∗ ) V(G),V(G^{\prime})\subseteq V(G^{*}) , we have h ¯ ∈ V ⁡ ( G ∗ ) \bar{h}\in V(G^{*}) . Applying Lemma 6.3 with f 1 = h G f_{1}=h_{G} , f 2 = h G ′ f_{2}=h_{G^{\prime}} , and ℋ = V ⁡ ( G ∗ ) \mathcal{H}=V(G^{*}) , and using R ⁡ ( h G ) = R ⁡ ( G ) R(h_{G})=R(G) , R ⁡ ( h G ′ ) = R ⁡ ( G ′ ) R(h_{G^{\prime}})=R(G^{\prime}) , and R ⁡ ( V ⁡ ( G ∗ ) ) = R ⁡ ( G ∗ ) R(V(G^{*}))=R(G^{*}) , we have the pointwise inequality

[288] table: ‖ h G − h G ′ ‖ 2 ≤ 4 μ ​ ( R ⁡ ( G ) − R ⁡ ( G ∗ ) ) + 4 μ ​ ( R ⁡ ( G ′ ) − R ⁡ ( G ∗ ) ) . \|h_{G}-h_{G^{\prime}}\|^{2}\;\leq\;\frac{4}{\mu}\big(R(G)-R(G^{*})\big)+\frac{4}{\mu}\big(R(G^{\prime})-R(G^{*})\big). (10)

[289] p: We now take expectations over G , G ′ , G ∗ G,G^{\prime},G^{*} to relate the two terms on the RHS of Equation 10 . Conditional on G ∗ G^{*} , we can generate the pair ( G , G ′ ) (G,G^{\prime}) by drawing a uniformly random permutation π \pi of { 1 , … , 2 ​ k } \{1,\dots,2k\} and letting G G be the first k k permuted elements of G ∗ G^{*} and G ′ G^{\prime} the remaining k k . This holds because the 2 ​ k 2k features in G ∗ G^{*} arise from 2 ​ k 2k i.i.d. draws from Q Q and the joint law of ( G , G ′ ) (G,G^{\prime}) is exchangeable under permutations of these 2 ​ k 2k draws. Conditioning on the unordered multiset G ∗ G^{*} , ( G , G ′ ) (G,G^{\prime}) is a uniformly random partition into two k k -submultisets. Therefore, taking the conditional expectation of ( 10 ) given G ∗ G^{*} and using symmetry of G G and G ′ G^{\prime} ,

[290] table: 𝔼 ( G , G ′ ) | G ∗ ​ [ ‖ h G − h G ′ ‖ 2 | G ∗ ] ≤ 8 μ ​ ( 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] − R ⁡ ( G ∗ ) ) . \mathbb{E}_{(G,G^{\prime})|G^{*}}\big[\,\|h_{G}-h_{G^{\prime}}\|^{2}\,\big|\,G^{*}\big]\;\leq\;\frac{8}{\mu}\Big(\mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]-R(G^{*})\Big). (11)

[291] p: We now integrate ( 11 ) over G ∗ G^{*} . We claim that

[292] table: 𝔼 G ∗ ​ [ 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] ] = R ¯ k and 𝔼 G ∗ ​ [ R ⁡ ( G ∗ ) ] = R ¯ 2 ​ k . \mathbb{E}_{G^{*}}\Big[\mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]\Big]\;=\;\bar{R}_{k}\qquad\text{and}\qquad\mathbb{E}_{G^{*}}\big[R(G^{*})\big]\;=\;\bar{R}_{2k}. (12)

[293] p: The second equality is immediate from the definition of R ¯ 2 ​ k \bar{R}_{2k} , since G ∗ G^{*} is a collection of 2 ​ k 2k i.i.d. draws from Q Q . For the first equality in ( 12 ), let U U be a uniformly random k k -subset of { 1 , … , 2 ​ k } \{1,\dots,2k\} independent of the draws { g 1 , … , g 2 ​ k } ∼ i.i.d. Q 2 ​ k \{g_{1},\dots,g_{2k}\}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}Q^{2k} . Define G U := { g i } i ∈ U G_{U}:=\{g_{i}\}_{i\in U} . By the conditional description above,

[294] table: 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] = 𝔼 U ​ [ R ⁡ ( G U ) | G ∗ ] . \mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]\;=\;\mathbb{E}_{U}\big[R(G_{U})\,\big|\,G^{*}\big].

[295] table: 𝔼 G ∗ ​ [ 𝔼 ( G , G ′ ) | G ∗ ​ [ R ⁡ ( G ) | G ∗ ] ] = 𝔼 G ∗ ​ [ 𝔼 U ​ [ R ⁡ ( G U ) | G ∗ ] ] = 𝔼 G ∗ , U ​ [ R ⁡ ( G U ) ] . \mathbb{E}_{G^{*}}\Big[\mathbb{E}_{(G,G^{\prime})|G^{*}}\big[R(G)\,\big|\,G^{*}\big]\Big]=\mathbb{E}_{G^{*}}\Big[\mathbb{E}_{U}\big[R(G_{U})\,\big|\,G^{*}\big]\Big]=\mathbb{E}_{G^{*},U}\big[R(G_{U})\big].

[296] p: For any fixed U U , the subcollection { g i } i ∈ U \{g_{i}\}_{i\in U} consists of k k i.i.d. draws from Q Q (since the full family is i.i.d. and U U is independent of the draws), hence averaging over U U yields 𝔼 G ∗ , U ​ [ R ⁡ ( G U ) ] = R ¯ k \mathbb{E}_{G^{*},U}[R(G_{U})]=\bar{R}_{k} , proving ( 12 ).

[297] p: Finally, taking expectations in ( 11 ) and substituting ( 12 ) gives

[298] table: 𝔼 G , G ′ ​ [ ‖ h G − h G ′ ‖ 2 ] ≤ 8 μ ​ ( R ¯ k − R ¯ 2 ​ k ) , \mathbb{E}_{G,G^{\prime}}\big[\,\|h_{G}-h_{G^{\prime}}\|^{2}\,\big]\;\leq\;\frac{8}{\mu}\big(\bar{R}_{k}-\bar{R}_{2k}\big),

[299] p: which is the desired bound. ∎

[300] p: As before, we have related the stability of (now generalized) stacking to the local learning curve, which is bounded, non-negative, and non-increasing in k k . As a result for any desired level of stability α \alpha , there must be a OPEN k ≤ 2 O ⁡ ( 1 / α CLOSE ) k\leq 2^{O(1/\alpha}) that guarantees that level of stability, independently of the complexity of the learning instance — and once again the local learning curve can be empirically investigated on a holdout set to choose such a value of k k .

[301] h3: 6.2 Gradient Boosting (via Frank Wolfe)

[302] p: In this section, we generalize our gradient boosting agreement results to the multi-dimensional setting. Along the way we give another generalization as well. Recall that in the final risk bound of Theorem 4.5 , and correspondingly in the final agreement bound, we had a dependence on the instance-dependent constant τ ∗ \tau^{*} , the atomic norm of the best model in the span of the weak learner class. In this section, we instead analyze a Frank-Wolfe variant of gradient boosting. In this variant, the iterates are constrained to lie within a user-specified atomic-norm budget τ \tau . As a result we are able to carry out our anchoring argument with respect to the best norm τ \tau model in the span of the weak learner class, rather than the best unconstrained model. This lets us replace the dependence on τ ∗ \tau^{*} with a dependence on τ \tau , which is specified by the user rather than defined by the instance. In this section we will need to work with L − L- smooth losses (in the prediction p p ). In other words we need to assume that for all y ∈ 𝒴 y\in\mathcal{Y} and all p 1 , p 2 ∈ Δ ⁡ ( 𝒴 ) p_{1},p_{2}\in\Delta(\mathcal{Y}) that our loss satisfies:

[303] table: ‖ ∇ p ℒ ​ ( y , p 1 ) − ∇ p ℒ ​ ( y , p 2 ) ‖ 2 ≤ L ​ ‖ p 1 − p 2 ‖ 2 . ||\nabla_{p}\mathcal{L}(y,p_{1})-\nabla_{p}\mathcal{L}(y,p_{2})||_{2}\leq L||p_{1}-p_{2}||_{2}.

[304] p: Recall the conditions of the weak learner class 𝒞 \mathcal{C} that we had previously, which we continue to assume in this section: symmetry, normalization, and non-degeneracy. Note in this section, for the sake of clarity, we will use the standard inner product ⟨ f , g ⟩ = f T ​ g \langle f,g\rangle=f^{T}g . When needed, we will explicitly mention the expectations we are computing. When the norms are marked ‖ f ‖ ||f|| , we still take it to mean the same definition as in Preliminaries of ( 𝔼 ⁡ [ f ​ ( x ) 2 ] ) 1 / 2 . (\mathbb{E}[f(x)^{2}])^{1/2}.

[305] figure: Algorithm 3 Multi-Dimensional Frank–Wolfe Input: SQ-oracle for weak learner class 𝒞 \mathcal{C} , budget τ > 0 \tau>0 f 0 ≡ 0 f_{0}\equiv 0 , G 0 = ∅ G_{0}=\emptyset for t ∈ [ k ] t\in[k] do Choose s t ∈ 𝒞 s_{t}\in\mathcal{C} such that 𝔼 ⁡ [ ⟨ − ∇ p ℒ ​ ( y , f t − 1 ​ ( x ) ) , s t ​ ( x ) ⟩ ] ≥ max s ∈ 𝒞 ⁡ 𝔼 ⁡ [ ⟨ − ∇ p ℒ ​ ( y , f t − 1 ​ ( x ) ) , s ⁡ ( x ) ⟩ ] − ε t \mathbb{E}[\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}(x)),s_{t}(x)\rangle]\geq\max_{s\in\mathcal{C}}\mathbb{E}[\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}(x)),s(x)\rangle]-\varepsilon_{t} Choose g t ∈ 𝒦 τ g_{t}\in\mathcal{K}_{\tau} such that g t = τ ​ s t / ‖ s t ‖ 𝒜 g_{t}=\tau s_{t}/\|s_{t}\|_{\mathcal{A}} α t = 2 t + 1 \alpha_{t}=\frac{2}{t+1} f t := f t − 1 + α t ​ ( g t − f t − 1 ) f_{t}:=f_{t-1}+\alpha_{t}(g_{t}-f_{t-1}) ; G t := G t − 1 ∪ { g t } G_{t}:=G_{t-1}\cup\{g_{t}\} end for return f k f_{k} and G := G k G:=G_{k}

[306] p: We will define the quantity

[307] table: M ⁡ ( f ) := sup g ∈ 𝒞 | 𝔼 ⁡ [ ⟨ ∇ p ℒ ​ ( y , f ⁡ ( x ) ) , g ⁡ ( x ) ⟩ ] | . M(f)\ :=\ \sup_{g\in\mathcal{C}}\ \big|\mathbb{E}[\langle\nabla_{p}\mathcal{L}(y,f(x)),g(x)\rangle]\big|.

[308] p: We will also define the closely related quantity

[309] table: G ⁡ ( f ) := sup z ∈ 𝒦 τ 𝔼 ⁡ [ ⟨ ∇ p ℒ ​ ( y , f ⁡ ( x ) ) , f ⁡ ( x ) − z ⁡ ( x ) ⟩ ] . G(f):=\sup_{z\in\mathcal{K}_{\tau}}\mathbb{E}[\langle\nabla_{p}\mathcal{L}(y,f(x)),f(x)-z(x)\rangle].

[310] p: We can show that for any f ∈ 𝒦 τ f\in\mathcal{K}_{\tau} , G ⁡ ( f ) ≤ 2 ​ τ ​ M ​ ( f ) G(f)\leq 2\tau M(f) . Define f ~ ​ ( x ) , g ~ ​ ( x ) ∈ conv ​ ( 𝒞 ) \tilde{f}(x),\tilde{g}(x)\in\mathrm{conv}(\mathcal{C}) , where f ⁡ ( x ) = τ ​ f ~ ​ ( x ) f(x)=\tau\tilde{f}(x) and g ⁡ ( x ) = τ ​ g ~ ​ ( x ) g(x)=\tau\tilde{g}(x) . One can see this (as shown below) because the weak learner class is normalized, functions in 𝒦 τ \mathcal{K}_{\tau} can be scaled up to live in conv ⁡ ( 𝒞 ) \mathrm{conv}(\mathcal{C}) , the inside inner product term for M ⁡ ( f ) M(f) is linear in g g and therefore the supremum over conv ⁡ ( 𝒞 ) \mathrm{conv}(\mathcal{C}) matches the supremum over 𝒞 \mathcal{C} , and triangle inequality.

[311] table: G ⁡ ( f ) \displaystyle G(f) = sup z ∈ 𝒦 τ | 𝔼 [ ⟨ ∇ ℒ ( y , f ( x ) ) , f ( x ) − z ( x ) ⟩ | ] \displaystyle=\sup_{z\in\mathcal{K}_{\tau}}|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),f(x)-z(x)\rangle|] = τ sup z ~ ∈ conv ⁡ ( 𝒞 ) | 𝔼 [ ⟨ ∇ ℒ ( y , f ( x ) ) , f ~ ( x ) − z ~ ( x ) ⟩ | ] \displaystyle=\tau\sup_{\tilde{z}\in\mathrm{conv}(\mathcal{C})}|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),\tilde{f}(x)-\tilde{z}(x)\rangle|] ≤ τ | 𝔼 [ ⟨ ∇ ℒ ( y , f ( x ) ) , f ~ ( x ) ⟩ ] | + τ sup z ~ ∈ conv ⁡ ( 𝒞 ) | 𝔼 [ ⟨ ∇ ℒ ( y , f ( x ) ) , z ~ ( x ) ⟩ | ] \displaystyle\leq\tau|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),\tilde{f}(x)\rangle]|+\tau\sup_{\tilde{z}\in\mathrm{conv}(\mathcal{C})}|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),\tilde{z}(x)\rangle|] ≤ τ sup h ~ ∈ conv ⁡ ( 𝒞 ) | 𝔼 [ ⟨ ∇ ℒ ( y , f ( x ) ) , h ~ ( x ) ⟩ ] | + τ sup z ~ ∈ conv ⁡ ( 𝒞 ) | 𝔼 [ ⟨ ∇ ℒ ( y , f ( x ) ) , z ~ ( x ) ⟩ | ] \displaystyle\leq\tau\sup_{\tilde{h}\in\mathrm{conv}(\mathcal{C})}|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),\tilde{h}(x)\rangle]|+\tau\sup_{\tilde{z}\in\mathrm{conv}(\mathcal{C})}|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),\tilde{z}(x)\rangle|] = 2 ​ τ ​ sup h ~ ∈ 𝒞 | 𝔼 ⁡ [ ⟨ ∇ ℒ ​ ( y , f ⁡ ( x ) ) , h ~ ​ ( x ) ⟩ ] | \displaystyle=2\tau\sup_{\tilde{h}\in\mathcal{C}}|\mathbb{E}[\langle\nabla\mathcal{L}(y,f(x)),\tilde{h}(x)\rangle]| = 2 ​ τ ​ M ​ ( f ) \displaystyle=2\tau M(f)

[312] p: Broadly, our proof will mirror the analysis of our single-dimensional agreement results for gradient boosting. We will once again make use of the conditions on the weak learner class mentioned for gradient boosting of symmetry, normalization, and non-degeneracy. Also note that we can define G ⁡ ( f ) G(f) with the absolute value due to symmetry of our class, similar to the argument provided in the gradient boosting section. First, we will lower bound the difference of two iterate’s losses. This will give us a lower bound on the progress our algorithm’s model is making on a per-iterate basis.

[313] h6: Lemma 6.5 (FW single-iterate progress) .

[314] p: Assume ℒ \mathcal{L} is L L -smooth in the second argument. Let d t = g t − f t − 1 d_{t}=g_{t}-f_{t-1} with ‖ d t ‖ 2 ≤ 2 ​ τ \|d_{t}\|_{2}\leq 2\tau . Then with the oracle above we get that,

[315] table: R ⁡ ( f t − 1 ) − R ⁡ ( f t ) ≥ α t ​ ( G ⁡ ( f t − 1 ) − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 R(f_{t-1})-R(f_{t})\geq\alpha_{t}(G(f_{t-1})-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[316] h6: Proof.

[317] p: By L − L- smoothness we have the following quadratic upper bound (or descent lemma),

[318] table: ℒ ( y , f t − 1 ( x ) + α d t ( x ) ) ≤ ℒ ( y , f t − 1 ( x ) ) + α ⟨ ∇ p ℒ ( y , f t − 1 ( x ) ) , d t ( x ) ) ⟩ + L 2 α 2 ( d t ( x ) ) 2 . \mathcal{L}(y,f_{t-1}(x)+\alpha d_{t}(x))\leq\mathcal{L}(y,f_{t-1}(x))+\alpha\langle\nabla_{p}\mathcal{L}(y,f_{t-1}(x)),d_{t}(x))\rangle+\frac{L}{2}\alpha^{2}(d_{t}(x))^{2}.

[319] p: Taking expectations, we know that

[320] table: R ⁡ ( f t − 1 ) − R ⁡ ( f t ) ≥ α ​ 𝔼 ​ [ ⟨ − ∇ p ℒ ​ ( y , f t − 1 ​ ( x ) ) , d t ⟩ ] − L 2 ​ α 2 ​ ‖ d t ‖ 2 2 . R(f_{t-1})-R(f_{t})\geq\alpha\mathbb{E}[\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}(x)),d_{t}\rangle]-\frac{L}{2}\alpha^{2}||d_{t}||_{2}^{2}.

[321] p: Consider the quantity ⟨ − ∇ p ℒ ​ ( y , f t − 1 ) , d t ⟩ = ⟨ − ∇ p ℒ ​ ( y , f t − 1 ) , g t − f t − 1 ⟩ = ⟨ − ∇ p ℒ ​ ( y , f t − 1 ) , g t ⟩ + ⟨ ∇ p ℒ ​ ( y , f t − 1 ) , f t − 1 ⟩ . \langle-\nabla_{p}\mathcal{L}(y,f_{t-1}),d_{t}\rangle=\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}),g_{t}-f_{t-1}\rangle=\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}),g_{t}\rangle+\langle\nabla_{p}\mathcal{L}(y,f_{t-1}),f_{t-1}\rangle. We know from the oracle that ⟨ − ∇ p ℒ ​ ( y , f t − 1 ) , g t ⟩ ≥ τ ​ sup c ∈ 𝒞 ⟨ − ∇ p ℒ ​ ( y , f t − 1 ) , c ⟩ − τ ​ ε t = sup g ∈ 𝒦 τ ⟨ − ∇ p ℒ ​ ( y , f t − 1 ) , g ⟩ − τ ​ ε t \langle-\nabla_{p}\mathcal{L}(y,f_{t-1}),g_{t}\rangle\geq\tau\sup_{c\in\mathcal{C}}\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}),c\rangle-\tau\varepsilon_{t}=\sup_{g\in\mathcal{K}_{\tau}}\langle-\nabla_{p}\mathcal{L}(y,f_{t-1}),g\rangle-\tau\varepsilon_{t} . We can combine this back with the term ⟨ ∇ p ℒ ​ ( y , f t − 1 ) , f t − 1 ⟩ \langle\nabla_{p}\mathcal{L}(y,f_{t-1}),f_{t-1}\rangle and reapply the expectation to lower bound this term by G ⁡ ( f t − 1 ) − τ ​ ε t G(f_{t-1})-\tau\varepsilon_{t} . Therefore, we know that

[322] table: R ⁡ ( f t − 1 ) − R ⁡ ( f t ) ≥ α t ​ ( G ⁡ ( f t − 1 ) − τ ​ ε t ) − L 2 ​ α t 2 ​ ‖ d t ‖ 2 2 R(f_{t-1})-R(f_{t})\geq\alpha_{t}(G(f_{t-1})-\tau\varepsilon_{t})-\frac{L}{2}\alpha_{t}^{2}||d_{t}||_{2}^{2}

[323] p: Using the bound on ‖ d t ‖ 2 ||d_{t}||_{2} (which we get from the normalization condition on the weak learner class and triangle inequality), we get that

[324] table: R ⁡ ( f t − 1 ) − R ⁡ ( f t ) ≥ α t ​ ( G ⁡ ( f t − 1 ) − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 R(f_{t-1})-R(f_{t})\geq\alpha_{t}(G(f_{t-1})-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[325] p: ∎

[326] p: Next we lower bound the progress that the best model in the weak learner class could make, in terms of the current loss gap with the anchor model and our chosen atomic norm bound τ \tau :

[327] h6: Lemma 6.6 .

[328] p: (FW Correlation Lower Bound w.r.t Weak Learning Anchor Gap) For a given f f from our algorithm’s iterates ( f t ) (f_{t}) , we have that

[329] table: M ⁡ ( f ) ≥ R ⁡ ( f ) − R ⁡ ( 𝒦 τ ) 2 ​ τ M(f)\geq\frac{R(f)-R(\mathcal{K}_{\tau})}{2\tau}

[330] h6: Proof.

[331] p: Let f ∗ = arg ⁡ min f ∈ 𝒦 τ ⁡ R ⁡ ( f ) . f^{*}=\arg\min_{f\in\mathcal{K}_{\tau}}R(f). We know by convexity that

[332] table: ℒ ⁡ ( y , f ⁡ ( x ) ) − ℒ ⁡ ( y , f ∗ ​ ( x ) ) ≤ ⟨ ∇ p ℒ ​ ( y , f ⁡ ( x ) ) , f ⁡ ( x ) − f ∗ ​ ( x ) ⟩ \mathcal{L}(y,f(x))-\mathcal{L}(y,f^{*}(x))\leq\langle\nabla_{p}\mathcal{L}(y,f(x)),f(x)-f^{*}(x)\rangle

[333] p: Taking expectations and by an application of Hölder’s inequality and triangle inequality, we get that

[334] table: R ⁡ ( f ) − R ⁡ ( 𝒦 τ ) ≤ | | ∇ R ​ ( f ) | | 𝒜 ∗ ​ ( ‖ f ‖ 𝒜 + | | f ∗ | | 𝒜 ) . R(f)-R(\mathcal{K}_{\tau})\leq||\nabla R(f)||_{\mathcal{A}^{*}}(||f||_{\mathcal{A}}+||f^{*}||_{\mathcal{A}}).

[335] p: As shown below, by the definition of the dual norm, atomic norm, linearity of the inner product, normalization of the weak learner class, and the budget τ \tau ,

[336] table: ‖ ∇ R ​ ( f ) ‖ A ∗ \displaystyle||\nabla R(f)||_{A^{*}} = sup ‖ c ‖ 𝒜 ≤ 1 | ⟨ ∇ R ​ ( f ) , c ⟩ | \displaystyle=\sup_{||c||_{\mathcal{A}}\leq 1}|\langle\nabla R(f),c\rangle| = sup c ∈ conv ⁡ ( 𝒞 ) | ⟨ ∇ R ​ ( f ) , c ⟩ | \displaystyle=\sup_{c\in\mathrm{conv}(\mathcal{C})}|\langle\nabla R(f),c\rangle| = sup c ∈ 𝒞 | ⟨ ∇ R ​ ( f ) , c ⟩ | . \displaystyle=\sup_{c\in\mathcal{C}}|\langle\nabla R(f),c\rangle|.

[337] p: Therefore, we get that

[338] table: R ⁡ ( f ) − R ⁡ ( 𝒦 τ ) ≤ 2 ​ τ ​ M ​ ( f ) . R(f)-R(\mathcal{K}_{\tau})\leq 2\tau M(f).

[339] p: Rearranging this expression gives the final bound. ∎

[340] p: Next we derive a recurrence relation between the error gap of the model at iteration t t and the best model in the restricted span of the weak learner class.

[341] h6: Lemma 6.7 (FW Gap Recurrence Toward R ⁡ ( 𝒦 τ ) R(\mathcal{K}_{\tau}) ) .

[342] p: Assume ℒ \mathcal{L} is L L -smooth in its second argument. Let E t := R ⁡ ( f t ) − R ⁡ ( K τ ) E_{t}:=R(f_{t})-R(K_{\tau}) . Then for all t ≥ 1 t\geq 1 ,

[343] table: E t − 1 − E t ≥ α t ​ ( G ⁡ ( f t − 1 ) − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 ≥ α t ​ ( E t − 1 − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 E_{t-1}-E_{t}\geq\alpha_{t}(G(f_{t-1})-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}\geq\alpha_{t}(E_{t-1}-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[344] h6: Proof.

[345] p: By L L -smoothness and the FW update f t = f t − 1 + α t ​ d t f_{t}=f_{t-1}+\alpha_{t}d_{t} with d t = g t − f t − 1 d_{t}=g_{t}-f_{t-1} , Lemma 6.5 gives

[346] table: R ⁡ ( f t − 1 ) − R ⁡ ( f t ) ≥ α t ​ ( G ⁡ ( f t − 1 ) − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 R(f_{t-1})-R(f_{t})\geq\alpha_{t}(G(f_{t-1})-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[347] p: Subtract and add R ⁡ ( K τ ) R(K_{\tau}) to obtain the first inequality:

[348] table: E t − 1 − E t ≥ α t ​ ( G ⁡ ( f t − 1 ) − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 E_{t-1}-E_{t}\geq\alpha_{t}(G(f_{t-1})-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[349] p: Let f ∗ = arg ⁡ min f ∈ 𝒦 τ ⁡ 𝔼 ⁡ [ ℒ ⁡ ( y , f ) ] f^{*}=\arg\min_{f\in\mathcal{K}_{\tau}}\mathbb{E}[\mathcal{L}(y,f)] . By convexity, E t − 1 = R ⁡ ( f t − 1 ) − R ⁡ ( f ∗ ) ≤ ⟨ ∇ R ​ ( f t − 1 ) , f t − 1 − f ∗ ⟩ ≤ G ⁡ ( f t − 1 ) E_{t-1}=R(f_{t-1})-R(f^{*})\leq\langle\nabla R(f_{t-1}),\,f_{t-1}-f^{*}\rangle\leq G(f_{t-1}) , so

[350] table: E t − 1 − E t ≥ α t ​ ( E t − 1 − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 E_{t-1}-E_{t}\geq\alpha_{t}(E_{t-1}-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[351] p: which is the second inequality.

[352] p: ∎

[353] p: We will use this recurrence relation to bound the error gap for the model at iterate t t .

[354] h6: Lemma 6.8 (FW Anchor Gap Upper Bound) .

[355] p: For all t ≥ 1 t\geq 1 ,

[356] table: R ⁡ ( f t ) − R ⁡ ( K τ ) ≤ 8 ​ L ​ τ 2 t + 1 + 2 ​ τ ( t + 1 ) ​ ∑ j = 1 t ε t . R(f_{t})-R(K_{\tau})\ \leq\ \frac{8L\tau^{2}}{t+1}+\frac{2\tau}{(t+1)}\sum_{j=1}^{t}\varepsilon_{t}.

[357] h6: Proof.

[358] p: From Lemma 6.7 we have the recursion

[359] table: E t − 1 − E t ≥ α t ​ ( E t − 1 − τ ​ ε t ) − 2 ​ L ​ τ 2 ​ α t 2 E_{t-1}-E_{t}\geq\alpha_{t}(E_{t-1}-\tau\varepsilon_{t})-2L\tau^{2}\alpha_{t}^{2}

[360] p: which is equivalent to

[361] table: E t \displaystyle E_{t} ≤ E t − 1 − α t ​ ( E t − 1 − τ ​ ε t ) + 2 ​ L ​ τ 2 ​ α t 2 \displaystyle\leq E_{t-1}-\alpha_{t}(E_{t-1}-\tau\varepsilon_{t})+2L\tau^{2}\alpha_{t}^{2} = ( 1 − α t ) ​ E t − 1 + α t ​ τ ​ ε t + 2 ​ L ​ τ 2 ​ α t 2 \displaystyle=(1-\alpha_{t})E_{t-1}+\alpha_{t}\tau\varepsilon_{t}+2L\tau^{2}\alpha_{t}^{2}

[362] p: We use the convention that [ k ] = { 1 , … , k } [k]=\{1,...,k\} . Call C = 4 ​ L ​ τ 2 C=4L\tau^{2} and substitute in α t \alpha_{t} , then we get

[363] table: E t \displaystyle E_{t} ≤ t − 1 t + 1 ​ E t − 1 + 2 t + 1 ​ τ ​ ε t + 2 ​ L ​ τ 2 ​ ( 2 t + 1 ) 2 \displaystyle\leq\frac{t-1}{t+1}E_{t-1}+\frac{2}{t+1}\tau\varepsilon_{t}+2L\tau^{2}\Big(\frac{2}{t+1}\Big)^{2} = t − 1 t + 1 ​ E t − 1 + 2 ​ C ( t + 1 ) 2 + 2 t + 1 ​ τ ​ ε t \displaystyle=\frac{t-1}{t+1}E_{t-1}+\frac{2C}{(t+1)^{2}}+\frac{2}{t+1}\tau\varepsilon_{t}

[364] p: Define S t = τ ​ ∑ j = 1 t j ​ ε j S_{t}=\tau\sum_{j=1}^{t}j\varepsilon_{j} . Then, we will prove via induction that for all t ≥ 1 t\geq 1 ,

[365] table: E t ≤ 2 ​ C ​ t + 2 ​ S t t ⁡ ( t + 1 ) E_{t}\leq\frac{2Ct+2S_{t}}{t(t+1)}

[366] p: First, for the base case consider t = 1 t=1 . We have from the recurrence relation that E 1 ≤ 0 + C 2 + τ ​ ε t ≤ C + τ ​ ε t . E_{1}\leq 0+\frac{C}{2}+\tau\varepsilon_{t}\leq C+\tau\varepsilon_{t}. Next, suppose E t ≤ 2 ​ C ​ t + 2 ​ S t t ⁡ ( t + 1 ) E_{t}\leq\frac{2Ct+2S_{t}}{t(t+1)} , we will prove the same relationship holds for E t + 1 . E_{t+1}.

[367] table: E t + 1 \displaystyle E_{t+1} ≤ t t + 1 ​ E t + 2 ​ C ( t + 2 ) 2 + 2 t + 2 ​ τ ​ ϵ t + 1 \displaystyle\leq\frac{t}{t+1}E_{t}+\frac{2C}{(t+2)^{2}}+\frac{2}{t+2}\tau\epsilon_{t+1} ≤ t t + 2 ​ 2 ​ C ​ t + 2 ​ S t t ⁡ ( t + 1 ) + 2 ​ C ( t + 2 ) 2 + 2 t + 2 ​ τ ​ ϵ t + 1 \displaystyle\leq\frac{t}{t+2}\frac{2Ct+2S_{t}}{t(t+1)}+\frac{2C}{(t+2)^{2}}+\frac{2}{t+2}\tau\epsilon_{t+1} = 2 ​ C ​ t + 2 ​ S t ( t + 1 ) ​ ( t + 2 ) + 2 ​ C ( t + 2 ) 2 + 2 t + 2 ​ τ ​ ϵ t + 1 \displaystyle=\frac{2Ct+2S_{t}}{(t+1)(t+2)}+\frac{2C}{(t+2)^{2}}+\frac{2}{t+2}\tau\epsilon_{t+1} = 2 ​ C t + 2 ​ ( t t + 1 + 1 t + 2 ) + 2 ​ S t + 1 ( t + 1 ) ​ ( t + 2 ) \displaystyle=\frac{2C}{t+2}\Big(\frac{t}{t+1}+\frac{1}{t+2}\Big)+\frac{2S_{t+1}}{(t+1)(t+2)} ≤ 2 ​ C t + 2 ​ ( t t + 1 + 1 t + 1 ) + 2 ​ S t + 1 ( t + 1 ) ​ ( t + 2 ) \displaystyle\leq\frac{2C}{t+2}\Big(\frac{t}{t+1}+\frac{1}{t+1}\Big)+\frac{2S_{t+1}}{(t+1)(t+2)} ≤ 2 ​ C t + 2 ​ ( t + 1 t + 1 ) + 2 ​ S t + 1 ( t + 1 ) ​ ( t + 2 ) \displaystyle\leq\frac{2C}{t+2}\Big(\frac{t+1}{t+1}\Big)+\frac{2S_{t+1}}{(t+1)(t+2)} = 2 ​ C ​ ( t + 1 ) + 2 ​ S t + 1 ( t + 1 ) ​ ( t + 2 ) . \displaystyle=\frac{2C(t+1)+2S_{t+1}}{(t+1)(t+2)}.

[368] p: Therefore, we have that

[369] table: E t ≤ 8 ​ L ​ τ 2 t + 1 + 2 ​ τ t ⁡ ( t + 1 ) ​ ∑ j = 1 t j ​ ε j E_{t}\leq\frac{8L\tau^{2}}{t+1}+\frac{2\tau}{t(t+1)}\sum_{j=1}^{t}j\varepsilon_{j}

[370] p: Therefore,

[371] table: E t ≤ 8 ​ L ​ τ 2 t + 1 + 2 ​ τ ( t + 1 ) ​ ∑ j = 1 t ε j E_{t}\leq\frac{8L\tau^{2}}{t+1}+\frac{2\tau}{(t+1)}\sum_{j=1}^{t}\varepsilon_{j}

[372] p: ∎

[373] h6: Theorem 6.9 .

[374] p: (FW Gradient Boosting Agreement Bound) Fix any ℒ \mathcal{L} that is L L -smooth and μ \mu -strongly convex. Let f 1 , f 2 f_{1},f_{2} be the output of any two runs of Algorithm 3 parameterized with the same τ , k , 𝒞 \tau,k,\mathcal{C} such that the sequence of SQ oracle errors are { ε t , ε t ′ } t ∈ [ k ] \{\varepsilon_{t},\varepsilon_{t}^{\prime}\}_{t\in[k]} respectively. Let f ∗ = arg ⁡ min f ∈ 𝒦 τ ⁡ R ⁡ ( f ) f^{*}=\arg\min_{f\in\mathcal{K}_{\tau}}R(f) . Then, we have that

[375] table: D ⁡ ( f 1 , f 2 ) ≤ 64 ​ L ​ τ 2 μ ⁡ ( k + 1 ) + 8 ​ τ μ ⁡ ( k + 1 ) ​ ( ∑ j = 1 k ε j + ∑ j = 1 k ε j ′ ) D(f_{1},f_{2})\leq\frac{64L\tau^{2}}{\mu(k+1)}+\frac{8\tau}{\mu(k+1)}(\sum_{j=1}^{k}\varepsilon_{j}+\sum_{j=1}^{k}\varepsilon_{j}^{\prime})

[376] h6: Proof.

[377] p: Since f ⋆ f^{\star} minimizes 𝔼 ⁡ [ ℒ ⁡ ( y , f ⁡ ( x ) ) ] \mathbb{E}[\mathcal{L}(y,f(x))] over the convex set K τ K_{\tau} , by first-order optimality we have the inequality

[378] table: 𝔼 ⁡ [ ⟨ ∇ ℒ ​ ( y , f ⋆ ​ ( x ) ) , z ⁡ ( x ) − f ⋆ ​ ( x ) ⟩ ] ≥ 0 ∀ z ∈ K τ . \mathbb{E}[\langle\nabla\mathcal{L}(y,f^{\star}(x)),\,z(x)-f^{\star}(x)\rangle]\geq 0\qquad\forall z\in K_{\tau}.

[379] p: Combining this with μ \mu –strong convexity of ℒ \mathcal{L} gives

[380] table: 𝔼 [ ℒ ( y , g ( x ) ) ] ≥ 𝔼 [ ℒ ( y , f ⋆ ( x ) ) + ⟨ ∇ ℒ ( y , f ⋆ ( x ) ) , g ( x ) − f ⋆ ( x ) ⟩ + μ 2 ∥ g ( x ) − f ⋆ ( x ) ∥ 2 2 ) ] . \mathbb{E}[\mathcal{L}(y,g(x))]\geq\mathbb{E}[\mathcal{L}(y,f^{\star}(x))+\langle\nabla\mathcal{L}(y,f^{\star}(x)),\,g(x)-f^{\star}(x)\rangle+\tfrac{\mu}{2}\|g(x)-f^{\star}(x)\|_{2}^{2}\big)].

[381] p: Since 𝒦 τ \mathcal{K}_{\tau} is convex, the midpoint 1 2 ​ ( f 1 + f 2 ) \tfrac{1}{2}(f_{1}+f_{2}) lies in 𝒦 τ \mathcal{K}_{\tau} . Applying Lemma 6.3 with ℋ = 𝒦 τ \mathcal{H}=\mathcal{K}_{\tau} gives

[382] table: D ⁡ ( f 1 , f 2 ) ≤ 4 μ ​ ( R ⁡ ( f 1 ) − R ⁡ ( f ∗ ) ) + 4 μ ​ ( R ⁡ ( f 2 ) − R ⁡ ( f ∗ ) ) . D(f_{1},f_{2})\leq\tfrac{4}{\mu}\big(R(f_{1})-R(f^{*})\big)+\tfrac{4}{\mu}\big(R(f_{2})-R(f^{*})\big).

[383] p: Finally, applying Lemma 6.8 to both error gap terms gives us the final bound. ∎

[384] h3: 6.3 Neural Networks

[385] p: We next state the midpoint-anchor analogue of our neural-network and regression-tree agreement bounds for multi-dimensional μ \mu -strongly convex losses.

[386] h6: Theorem 6.10 (Agreement from midpoint closure) .

[387] p: Assume ℒ \mathcal{L} is μ \mu -strongly convex.

[388] p: If f 1 , f 2 ∈ NN n f_{1},f_{2}\in\mathrm{NN}_{n} satisfy R ⁡ ( f i ) ≤ R ⁡ ( NN n ) + ε R(f_{i})\leq R(\mathrm{NN}_{n})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} , then

[389] table: D ⁡ ( f 1 , f 2 ) ≤ 8 μ ​ ( R ⁡ ( NN n ) − R ⁡ ( NN 2 ​ n ) + ε ) . D(f_{1},f_{2})\ \leq\ \tfrac{8}{\mu}\big(R(\mathrm{NN}_{n})-R(\mathrm{NN}_{2n})+\varepsilon\big).

[390] p: If f 1 , f 2 ∈ 𝖳𝗋𝖾𝖾 d f_{1},f_{2}\in\mathsf{Tree}_{d} satisfy R ⁡ ( f i ) ≤ R ⁡ ( 𝖳𝗋𝖾𝖾 d ) + ε R(f_{i})\leq R(\mathsf{Tree}_{d})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} , then

[391] table: D ⁡ ( f 1 , f 2 ) ≤ 8 μ ​ ( R ⁡ ( 𝖳𝗋𝖾𝖾 d ) − R ⁡ ( 𝖳𝗋𝖾𝖾 2 ​ d ) + ε ) . D(f_{1},f_{2})\ \leq\ \tfrac{8}{\mu}\big(R(\mathsf{Tree}_{d})-R(\mathsf{Tree}_{2d})+\varepsilon\big).

[392] h6: Proof.

[393] p: We prove each part by applying Lemma 6.3 at the appropriate midpoint-closed level.

[394] p: Part (1). Let f 1 , f 2 ∈ NN n f_{1},f_{2}\in\mathrm{NN}_{n} and define f ¯ := 1 2 ​ ( f 1 + f 2 ) \bar{f}:=\tfrac{1}{2}(f_{1}+f_{2}) . By midpoint closure (Lemma 5.1 ), we have f ¯ ∈ NN 2 ​ n \bar{f}\in\mathrm{NN}_{2n} . Applying Lemma 6.3 with ℋ = NN 2 ​ n \mathcal{H}=\mathrm{NN}_{2n} gives

[395] table: D ⁡ ( f 1 , f 2 ) ≤ 4 μ ​ ( R ⁡ ( f 1 ) − R ⁡ ( NN 2 ​ n ) ) + 4 μ ​ ( R ⁡ ( f 2 ) − R ⁡ ( NN 2 ​ n ) ) . D(f_{1},f_{2})\leq\tfrac{4}{\mu}\big(R(f_{1})-R(\mathrm{NN}_{2n})\big)+\tfrac{4}{\mu}\big(R(f_{2})-R(\mathrm{NN}_{2n})\big).

[396] p: Using the assumptions R ⁡ ( f i ) ≤ R ⁡ ( NN n ) + ε R(f_{i})\leq R(\mathrm{NN}_{n})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} , we obtain

[397] table: R ⁡ ( f i ) − R ⁡ ( NN 2 ​ n ) ≤ R ⁡ ( NN n ) − R ⁡ ( NN 2 ​ n ) + ε . R(f_{i})-R(\mathrm{NN}_{2n})\leq R(\mathrm{NN}_{n})-R(\mathrm{NN}_{2n})+\varepsilon.

[398] p: Substituting this bound for both i = 1 , 2 i=1,2 yields

[399] table: D ⁡ ( f 1 , f 2 ) ≤ 8 μ ​ ( R ⁡ ( NN n ) − R ⁡ ( NN 2 ​ n ) + ε ) , D(f_{1},f_{2})\leq\tfrac{8}{\mu}\big(R(\mathrm{NN}_{n})-R(\mathrm{NN}_{2n})+\varepsilon\big),

[400] p: as claimed.

[401] p: Part (2). The proof is identical with 𝖳𝗋𝖾𝖾 d \mathsf{Tree}_{d} in place of NN n \mathrm{NN}_{n} . Let f 1 , f 2 ∈ 𝖳𝗋𝖾𝖾 d f_{1},f_{2}\in\mathsf{Tree}_{d} and f ¯ := 1 2 ​ ( f 1 + f 2 ) \bar{f}:=\tfrac{1}{2}(f_{1}+f_{2}) . By midpoint closure (Lemma 5.3 ), f ¯ ∈ 𝖳𝗋𝖾𝖾 2 ​ d \bar{f}\in\mathsf{Tree}_{2d} . Applying Lemma 6.3 with ℋ = 𝖳𝗋𝖾𝖾 2 ​ d \mathcal{H}=\mathsf{Tree}_{2d} gives

[402] table: D ⁡ ( f 1 , f 2 ) ≤ 4 μ ​ ( R ⁡ ( f 1 ) − R ⁡ ( 𝖳𝗋𝖾𝖾 2 ​ d ) ) + 4 μ ​ ( R ⁡ ( f 2 ) − R ⁡ ( 𝖳𝗋𝖾𝖾 2 ​ d ) ) . D(f_{1},f_{2})\leq\tfrac{4}{\mu}\big(R(f_{1})-R(\mathsf{Tree}_{2d})\big)+\tfrac{4}{\mu}\big(R(f_{2})-R(\mathsf{Tree}_{2d})\big).

[403] p: Using R ⁡ ( f i ) ≤ R ⁡ ( 𝖳𝗋𝖾𝖾 d ) + ε R(f_{i})\leq R(\mathsf{Tree}_{d})+\varepsilon for i ∈ { 1 , 2 } i\in\{1,2\} and substituting yields

[404] table: D ⁡ ( f 1 , f 2 ) ≤ 8 μ ​ ( R ⁡ ( 𝖳𝗋𝖾𝖾 d ) − R ⁡ ( 𝖳𝗋𝖾𝖾 2 ​ d ) + ε ) . D(f_{1},f_{2})\leq\tfrac{8}{\mu}\big(R(\mathsf{Tree}_{d})-R(\mathsf{Tree}_{2d})+\varepsilon\big).

[405] p: ∎

[406] h2: 7 Acknowledgments

[407] p: This work is partially supported by DARPA grant #HR001123S0011, an NSF Graduate Research Fellowship, a grant from the Simons foundation, and the NSF ENCoRE TRIPODS institute. The views and conclusions contained herein are those of the authors and should not be interpreted as representing the official policies of DARPA or the US Government.

[408] h2: References

[409] h2: Instructions for reporting errors

[410] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[411] p: Tip: You can select the relevant text first, to include it in your report.

[412] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[413] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
