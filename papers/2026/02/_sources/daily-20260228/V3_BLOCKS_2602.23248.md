[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Mitigating Legibility Tax with Decoupled Prover-Verifier Games

[3] h6: Abstract

[4] p: As large language models become increasingly capable, it is critical that their outputs can be easily checked by less capable systems. Prover-verifier games can be used to improve checkability of model outputs, but display a degradation in accuracy compared to a baseline trained only to maximize correctness—a phenonemon named legibility tax ( Kirchner et al., 2024 ) . We propose a solution by decoupling the correctness from the checkability condition and instead training a “translator” model that turns a fixed solver model’s solution into a checkable form. This allows us to first train the solver to maximize correctness, and then train the translator to translate the solver into a checkable form while retaining the solver’s answer. To accommodate this new objective of translation, we formulate a decoupled prover-verifier game where the equilibria correspond to faithful and checkable translators.

[5] h2: 1 Introduction

[6] p: As large language models (LLMs) become increasingly capable at complex reasoning tasks, a critical challenge is ensuring that their outputs can be validated by less capable systems, e.g. humans ( Bowman et al., 2022 ) . One promising approach that doesn’t require human supervision, c.f. reinforcement learning from human feedback ( Christiano et al., 2017 ; Ouyang et al., 2022 ) , is to train models with prover-verifier games ( Anil et al., 2021 ; Kirchner et al., 2024 , PVG;) . In this multi-agent reinforcement learning setup, the prover and verifier participate in a game where, at equilibrium, the prover’s outputs satisfy a “checkability” condition—detailed in § 2.1 —effectively ensuring that the less capable verifier can reliably authenticate the prover’s reasoning.

[7] p: Early work on prover-verifier games focused on binary yes/no classification tasks ( Anil et al., 2021 ) , where the only goal was to train provers that produce convincing proofs for yes . More recently, Kirchner et al. (2024) applied this framework to mathematical reasoning problems where the prover is tasked with both choosing an answer out of a large class and providing a checkable proof. While their work showed promising results, it also revealed a huge gap between the accuracy of their PVG-trained model and a model trained only for correctness (60% accuracy compared to 80% on their grade-school math benchmark), a phenomenon that they term legibility tax .

[8] p: We propose decoupling correctness from the definition of checkability in Kirchner et al. (2024) . In our decoupled prover-verifier game , rather than a single prover π \pi that is trained to be both correct and checkable, we introduce a solver s s that is optimized for correctness, and a translator τ \tau that converts the solver’s solution into a checkable form. We want a faithful translator, whose answer matches the solver’s. We prove that equilibria of our novel prover-verifier game correspond exactly to faithful and checkable translators (see Theorem 1 ). Empirically, we show that our decoupled framework achieves a stable training dynamics without a legibility tax.

[9] h2: 2 Method

[10] h3: 2.1 Background

[11] p: We define our dataset 𝒟 \mathcal{D} as a collection of problem-answer pairs ( x , y ) ∈ 𝒳 × 𝒴 (x,y)\in\mathcal{X}\times\mathcal{Y} , pairing each problem x x with its ground-truth answer y ⁡ ( x ) y(x) . For any proposed solution z z (which includes both reasoning and a final answer), we define 𝟙 correct ​ ( x , z ) \mathds{1}_{\text{correct}}\left({x,z}\right) as a binary indicator: it equals 1 1 when z z ’s final answer matches y ⁡ ( x ) y(x) , and 0 0 otherwise.

[12] p: In a PVG, there is a prover π ⁡ ( z | x ) \pi(z|x) that generates solutions given a problem statement, and a verifier v ⁡ ( x , z ) ∈ [ 0 , 1 ] v(x,z)\in[0,1] that estimates the probability of solution correctness. A prover π \pi is said to be correct if its answers are always correct, that is,

[13] p: Correctness: ∀ x ∈ 𝒳 , 𝟙 correct ​ ( x , π ⁡ ( x ) ) = 1 \forall x\in\mathcal{X},\mathds{1}_{\text{correct}}\left({x,\pi(x)}\right)=1 .

[14] p: The prover is said to be checkable if there exists a verifier v v such that the prover can always convince the verifier when its answer is correct, and there exists no adversarial proof that can trick the verifier into accepting an incorrect answer. Formally,

[15] p: Completeness: ∀ x ∈ 𝒳 , 𝟙 correct ​ ( x , π ⁡ ( x ) ) = 1 ⟹ v ⁡ ( x , π ⁡ ( x ) ) = 1 \forall x\in\mathcal{X},\mathds{1}_{\text{correct}}\left({x,\pi(x)}\right)=1\implies v(x,\pi(x))=1 .

[16] p: Soundness: ∀ x ∈ 𝒳 , ∀ z ′ ∈ 𝒵 , 𝟙 correct ​ ( x , z ′ ) = 0 ⟹ v ⁡ ( x , z ′ ) = 0 \forall x\in\mathcal{X},\forall z^{\prime}\in\mathcal{Z},\mathds{1}_{\text{correct}}\left({x,z^{\prime}}\right)=0\implies v(x,z^{\prime})=0 .

[17] p: Intuitively, this means that the verifier has a robust proof protocol that the prover has to conform to. Note that our definition of completeness is different from that of Kirchner et al. (2024) , which mixes it up with correctness. Including correctness in the definition of checkability is unnatural, as it is possible (and realistic) that the model outputs incorrect answers on some problems while giving checkable and correct proofs on others.

[18] p: We thus propose taking a fixed solver model s s , and constraining the prover π \pi to always output a proof with the same answer as the solver. This constrained prover is essentially a system that translates the solver’s convoluted solution s ⁡ ( x ) s(x) into a checkable form τ ⁡ ( x , s ⁡ ( x ) ) \tau(x,s(x)) through a translator τ \tau . For simplicity, we omit x x in the argument and write τ ⁡ ( s ⁡ ( x ) ) \tau(s(x)) for the rest of our paper. Faithfulness, denoted by 𝟙 faithful ​ ( s ⁡ ( x ) , τ ⁡ ( s ⁡ ( x ) ) ) \mathds{1}_{\text{faithful}}\left({s(x),\tau(s(x))}\right) , indicates whether the answer in the translator’s output matches that of the solver. We want to formulate an optimization process that returns a checkable and faithful translator.

[19] h3: 2.2 Decoupled Prover-Verifier Game

[20] p: To this end, we introduce the decoupled prover-verifier game , consisting of a faithful translator τ \tau , a sneaky translator τ ′ \tau^{\prime} , and a verifier v v . The faithful translator’s goal is to craft a convincing proof of the solver’s answer, while the sneaky prover’s goal is to craft a convincing proof of an incorrect answer. The verifier’s goal is to discriminate between proofs with correct and incorrect answers. To reduce the burden on the sneaky translator of having to implicitly solve the problem to avoid the correct answer, we simply provide it with the ground truth answer y y .

[21] p: The verifier optimizes a classification objective that distinguishes between correct and incorrect solutions, from both the faithful and sneaky translators:

[22] table: R V = − 1 2 ​ 𝔼 x ∼ P X ​ [ l ⁡ ( v ⁡ ( x , τ ⁡ ( s ) ) , 𝟙 correct ​ ( x , τ ⁡ ( s ) ) ) + l ⁡ ( v ⁡ ( x , τ ′ ​ ( s , y ) ) , 𝟙 correct ​ ( x , τ ′ ​ ( s , y ) ) ) ] \displaystyle R_{V}=-\frac{1}{2}\mathbb{E}_{x\sim P_{X}}\Big[l\big(v(x,\tau(s)),\mathds{1}_{\text{correct}}\left({x,\tau(s)}\right)\big)+l\big(v(x,\tau^{\prime}(s,y)),\mathds{1}_{\text{correct}}\left({x,\tau^{\prime}(s,y)}\right)\big)\Big]

[23] p: where s = s ⁡ ( x ) s=s(x) is the solver output and y = y ⁡ ( x ) y=y(x) is the ground truth answer. l ⁡ ( v , c ) : [ 0 , 1 ] × { 0 , 1 } → ℝ l(v,c):[0,1]\times\{0,1\}\rightarrow\mathbb{R} is a loss function minimized if and only if v = c v=c , such as the cross-entropy loss. We assume without loss of generality that l ⁡ ( c , c ) = 0 l(c,c)=0 . In practice we optimize R V R_{V} via gradient descent on l V = − R V l_{V}=-R_{V} .

[24] p: The translator is conditioned on either the faithful or the sneaky role with equal probability, and the combined utility is

[25] table: R T = 1 2 ​ 𝔼 x ∼ P X ​ [ r ⁡ ( v ⁡ ( x , τ ⁡ ( s ) ) , 𝟙 faithful ​ ( s , τ ⁡ ( s ) ) ) + r ⁡ ( v ⁡ ( x , τ ′ ​ ( s ) ) , 1 − 𝟙 correct ​ ( x , τ ′ ​ ( s , y ) ) ) ] \displaystyle R_{T}=\frac{1}{2}\mathbb{E}_{x\sim P_{X}}\Big[{r\big(v(x,\tau(s)),\mathds{1}_{\text{faithful}}\left({s,\tau(s)}\right)\big)}+{r\big(v(x,\tau^{\prime}(s)),1-\mathds{1}_{\text{correct}}\left({x,\tau^{\prime}(s,y)}\right)\big)\Big]}

[26] p: where r ⁡ ( v , q ) : [ 0 , 1 ] × { 0 , 1 } → ℝ r(v,q):[0,1]\times\{0,1\}\rightarrow\mathbb{R} is a reward function for which r ⁡ ( v 1 , 1 ) > r ⁡ ( v 2 , 0 ) r(v_{1},1)>r(v_{2},0) regardless of v 1 , v 2 v_{1},v_{2} , and v 1 > v 2 : r ⁡ ( v 1 , 1 ) > r ⁡ ( v 2 , 1 ) v_{1}>v_{2}:r(v_{1},1)>r(v_{2},1) if v 1 > v 2 v_{1}>v_{2} . In practice we optimize R T R_{T} via reinforcement learning.

[27] p: The following theorem relates our decoupled prover-verifier game to faithfulness and checkability. Its proof is given in Appendix A .

[28] h6: Theorem 1 .

[29] p: In the verifier-leading Stackelberg game where the verifier’s utility is R V R_{V} and the translator’s utility is R T R_{T} , the tuple ( v ∗ , τ ∗ , τ ′ ⁣ ∗ ) (v^{*},\tau^{*},\tau^{\prime*}) being an equilibrium is necessary and sufficient for the faithfulness of τ ∗ \tau^{*} with respect to s s , and for the completeness and soundness properties to hold for ( v ∗ , τ ∗ ) (v^{*},\tau^{*}) .

[30] h3: 2.3 Optimization of Decoupled Prover-Verifier Game

[31] p: Given a dataset of problem-answer pairs 𝒟 = { ( x i , y i ) } \mathcal{D}=\{(x_{i},y_{i})\} and a solver s s , we want to approximate an equilibrium τ ∗ , τ ′ ⁣ ∗ , v ∗ \tau^{*},\tau^{\prime*},v^{*} to our decoupled prover-verifier game. We first partition the dataset 𝒟 \mathcal{D} into two equally-sized subsets 𝒟 T \mathcal{D}_{T} and 𝒟 V \mathcal{D}_{V} that are used for training the translators and the verifier, respectively. For the datasets 𝒟 T \mathcal{D}_{T} and 𝒟 V \mathcal{D}_{V} , we sample 16 16 solver solutions s i ​ j s_{ij} per problem x i x_{i} , extending the datasets to 𝒟 T = { ( x i , y i , s i ​ j ) } \mathcal{D}_{T}=\{(x_{i},y_{i},s_{ij})\} and 𝒟 V = { ( x i , y i , s i ​ j ) } \mathcal{D}_{V}=\{(x_{i},y_{i},s_{ij})\} .

[32] p: To approximate the equilibrium, we proceed through multiple rounds of training, where each round consists of the translator training phase, followed by the verifier training phase. We define the faithful and sneaky translators at round 0 0 to be the initial base policies. Note that at every round of translator and verifier training, the models being trained are initialized to the base translator and verifier models, respectively.

[33] p: In the verifier training phase of round t ≥ 0 t\geq 0 , we train verifier v t v_{t} to minimize the cross-entropy loss

[34] table: 𝔼 ( x , y , s ) ∼ D V , z ∼ τ ~ ​ ( s ) , z ′ ∼ τ ~ ′ ​ ( s , y ) [ \displaystyle\mathbb{E}_{(x,y,s)\sim D_{V},z\sim\tilde{\tau}(s),z^{\prime}\sim\tilde{\tau}^{\prime}(s,y)}\big[ CE ​ ( 𝟙 correct ​ ( x , z ) , v t ​ ( x , z ) ) + λ ​ v t ​ ( x , z ) 2 \displaystyle\textrm{CE}\left(\mathds{1}_{\text{correct}}\left({x,z}\right),v_{t}(x,z)\right)+\lambda v_{t}(x,z)^{2} CE ( 𝟙 correct ( x , z ′ ) , v t ( x , z ′ ) ) + λ v t ( x , z ′ ) 2 ] \displaystyle\textrm{CE}\left(\mathds{1}_{\text{correct}}\left({x,z^{\prime}}\right),v_{t}(x,z^{\prime})\right)+\lambda v_{t}(x,z^{\prime})^{2}\big]

[35] p: where λ \lambda is a hyperparameter for regularization, and τ ~ , τ ~ ′ \tilde{\tau},\tilde{\tau}^{\prime} are mixtures of faithful and sneaky translators from all the rounds up to t t . In our experiments, we use a mixture where the weight on round i i is proportional to 2 i 2^{i} . In practice, we only need to generate the round t t translator outputs, by storing outputs from all the previous rounds i < t i<t .

[36] p: During the translator training phase of round t > 0 t>0 , we use REINFORCE Leave-One-Out ( Kool et al., 2019 ; Ahmadian et al., 2024 , RLOO;) to maximize a reward analogous to the signed relative convincingness (SRC) reward in Kirchner et al. (2024) , which they found to be the most effective for improving legibility. For each training example ( x , y , s ) (x,y,s) and a fixed role, we sample K K completions { z ( 1 ) , … , z ( K ) } \{z^{(1)},\dots,z^{(K)}\} from the corresponding translator, to obtain K K verifier scores { v ⁡ ( x , z ( k ) ) } \{v(x,z^{(k)})\} . We take the logit of the scores and normalize them to have zero mean and unit variance. Let us denote v ′ ​ ( x , z ) v^{\prime}(x,z) for the normalized logits.

[37] table: v ~ ​ ( x , z ) := σ − 1 ​ ( v ⁡ ( x , z ) ) , v ′ ​ ( x , z ( k ) ) := v ~ ​ ( x , z ( k ) ) − Mean ⁡ ( { v ~ ​ ( x , z ( j ) ) } ) Std ​ ( { v ~ ​ ( x , z ( j ) ) } ) , \tilde{v}(x,z)\;:=\;\sigma^{-1}\!\big(v(x,z)\big),\qquad v^{\prime}(x,z^{(k)})\;:=\;\frac{\tilde{v}(x,z^{(k)})-\mathrm{Mean}(\{\tilde{v}(x,z^{(j)})\})}{\mathrm{Std}(\{\tilde{v}(x,z^{(j)})\})},

[38] p: Let q ∈ { 0 , 1 } q\in\{0,1\} denote role-alignment: for the faithful translator, q = 𝟙 faithful ​ ( s , z ) q=\mathds{1}_{\text{faithful}}\left({s,z}\right) ; for the sneaky translator, q = 1 − 𝟙 correct ​ ( x , z ) q=1-\mathds{1}_{\text{correct}}\left({x,z}\right) . Finally, let c s := 𝟙 correct ​ ( x , s ) c_{s}:=\mathds{1}_{\text{correct}}\left({x,s}\right) indicate whether the solver answer is correct. Our reward for a completion z z is

[39] table: R T ​ ( z ∣ x , role ) = { r role if ​ q = 0 , r score if ​ q = 1 ​ and ​ v ′ ​ ( x , z ) ≤ 0 , v ′ ​ ( x , z ) if q = 1 , v ′ ( x , z ) > 0 , role = “sneaky” , ( 2 ​ c s − 1 ) ​ v ′ ​ ( x , z ) if q = 1 , v ′ ( x , z ) > 0 , role = “faithful” . \displaystyle R_{T}(z\mid x,\text{role})\;=\;\begin{cases}r_{\mathrm{role}}&\text{if }q=0,\\[3.0pt] r_{\mathrm{score}}&\text{if }q=1\text{ and }v^{\prime}(x,z)\leq 0,\\[3.0pt] v^{\prime}(x,z)&\text{if }q=1,\;v^{\prime}(x,z)>0,\;\text{role}=\text{``sneaky''},\\[3.0pt] (2c_{s}-1)\,v^{\prime}(x,z)&\text{if }q=1,\;v^{\prime}(x,z)>0,\;\text{role}=\text{``faithful''}.\end{cases}

[40] p: Here r role < 0 r_{\mathrm{role}}<0 penalizes role-misaligned outputs, while r score < 0 r_{\mathrm{score}}<0 is a flat penalty for below-average verifier scores within the group.

[41] h2: 3 Experiments

[42] h3: 3.1 Experimental Setup

[43] p: In our experiments, we use Qwen2-1.5B 1 1 1 https://huggingface.co/Qwen/Qwen2-1.5B ( Team and others, 2024 ) as the base model for training the verifiers, and Llama-2-7b-chat 2 2 2 https://huggingface.co/meta-llama/Llama-2-7b-chat-hf ( Touvron et al., 2023 ) for training the solvers and translators. We use the GSM8K-Aug dataset 3 3 3 https://huggingface.co/datasets/whynlp/gsm8k-aug ( Deng et al., 2023 ) . We always use the same set of 16K problems for experiments, i.e. 8K each for the verifier and the solver/translator training phases. We also did a preliminary experiment with Qwen2-0.5B as the base model for the verifier, but found limited qualitative improvements in legibility. Further details of our experimental setup can be found in Appendix B .

[44] figure: Figure 1: Round 1 and 2 of our decoupled prover-verifier game. All values are exponential moving averages with α = 0.02 \alpha=0.02 . Verifier score is the average logit output by the verifier, and faithfulness is the fraction of outputs from the faithful translator whose answer matches that of the solver.

[45] h3: 3.2 Results

[46] h4: Training dynamics.

[47] p: We report in Fig. 1 the verifier score and faithfulness of the translators throughout training, on the first two rounds. We find that the faithfulness of the faithful translator converges to 1, as intended. We also measure the faithfulness score on a separate test set of size 1024 1024 , and obtain a value of 99.8%. Moreover, the sneaky translator needs more steps on the second round to find convincing adversarial proofs, compared to the first round, indicating that the verifier became more robust.

[48] figure: Table 1: GSM8K-Aug test set accuracy. Model Accuracy (%) Base model 9.6 Trained solver 57.0 DPVG (Ours) 56.9 PVG ( Kirchner et al., 2024 ) 22.3

[49] h4: Test set accuracy.

[50] p: Table 1 reports the accuracy of models on a test set of size 1024 from the same GSM8K-Aug dataset. As expected from the high faithfulness score, DPVG retains the accuracy of the trained solver. PVG, detailed in Appendix C , is a prover trained with a method similar to Kirchner et al. (2024) . It shows a degraded accuracy, consistent with the legibility tax reported in their paper. Unfortunately, we did not conduct human experiments that measure legibility, but provide sample model outputs in Appendix D . We observe that generally, the faithful translator’s output becomes more structured and shorter as the rounds progress.

[51] h2: 4 Conclusion

[52] p: We introduced a decoupled prover-verifier game framework that separates correctness from checkability by training a translator model to convert a fixed solver’s solution into a verifiable form. Our key contributions include: (1) formulating a novel prover-verifier game where equilibria correspond to faithful and checkable translators, and (2) experimental evidence of stable training dynamics where legibility can be qualitatively improved without harming the system’s accuracy.

[53] h4: Future directions.

[54] p: Several extensions would strengthen this work: (1) conducting human evaluation studies to precisely measure legibility improvements at scale, (2) alternative reward formulations and hyperparameters for RL training, and (3) adding chain-of-thought reasoning before proof generation for the ordinary prover-verifier game, as a lack of it could have been another main cause of the legibility tax, besides the coupling of the correctness and checkability objectives.

[55] h2: References

[56] h2: Appendix A Proof of Theorems

[57] p: We prove Theorem 1 . The proof is similar to but slightly lengthier than in Kirchner et al. (2024) since we are no longer assuming that the solution is always correct at equilibrium: we have to consider cases where the solver answer is incorrect. In such cases, both the faithful and the sneaky translators are performing the role of tricking the verifier into accepting incorrect answers.

[58] h6: Proof.

[59] p: First, assume that τ ∗ \tau^{*} is faithful to the solver, and that the completeness and soundness properties hold for v ∗ , τ ∗ v^{*},\tau^{*} . We construct τ ′ ⁣ ∗ \tau^{\prime*} as follows: For any s = s ⁡ ( x ) s=s(x) and y = y ⁡ ( x ) y=y(x) , let τ ′ ⁣ ∗ ​ ( s , y ) \tau^{\prime*}(s,y) be a translation whose answer is not equal to y y . We shall show that ( v ∗ , τ ∗ , τ ′ ⁣ ∗ ) (v^{*},\tau^{*},\tau^{\prime*}) is a verifier-leading Stackelberg equilibrium.

[60] p: Consider a solver output s = s ⁡ ( x ) s=s(x) that is correct. The first term of R T R_{T} is already maximized since, by completeness,

[61] table: r ⁡ ( v ∗ ​ ( x , τ ∗ ​ ( s ) ) , 𝟙 faithful ​ ( s , τ ∗ ​ ( s ) ) ) = r ⁡ ( 1 , 1 ) . \displaystyle r\big(v^{*}(x,\tau^{*}(s)),\mathds{1}_{\text{faithful}}\left({s,\tau^{*}(s)}\right)\big)=r(1,1).

[62] p: The second term is

[63] table: r ⁡ ( v ∗ ​ ( x , τ ′ ⁣ ∗ ​ ( s , y ) ) , 1 − 𝟙 correct ​ ( x , τ ′ ⁣ ∗ ​ ( s , y ) ) ) = r ⁡ ( 0 , 1 ) . \displaystyle r\big(v^{*}(x,\tau^{\prime*}(s,y)),1-\mathds{1}_{\text{correct}}\left({x,\tau^{\prime*}(s,y)}\right)\big)=r(0,1).

[64] p: by soundness. Any other sneaky translator τ ′ \tau^{\prime} that is role-aligned would receive the same reward, also by soundness. Thus, the second term is also maximized. Now, consider an incorrect solver output. The first term of R T R_{T} is maximized by τ ∗ \tau^{*} with value r ⁡ ( 0 , 1 ) r(0,1) , by the same argument as above. The same goes for the second term, already maximized by τ ′ ⁣ ∗ \tau^{\prime*} with value r ⁡ ( 0 , 1 ) r(0,1) .

[65] p: As for the verifier, the value of R V R_{V} for correct s s is

[66] table: − 1 2 ​ ( l ⁡ ( 1 , 1 ) + l ⁡ ( 0 , 0 ) ) = 0 \displaystyle-\frac{1}{2}\big(l(1,1)+l(0,0)\big)=0

[67] p: and for incorrect s s ,

[68] table: − 1 2 ​ ( l ⁡ ( 0 , 0 ) + l ⁡ ( 0 , 0 ) ) = 0 \displaystyle-\frac{1}{2}\big(l(0,0)+l(0,0)\big)=0

[69] p: so v ∗ v^{*} already achieves the global maximum, and has no incentive to change.

[70] p: Next, assume that ( v ∗ , τ ∗ , τ ′ ⁣ ∗ ) (v^{*},\tau^{*},\tau^{\prime*}) is an equilibrium to the verifier-leading Stackelberg game. We already know that there is a verifier that achieves R V = 0 R_{V}=0 , namely, a perfect classifier. We also know that there is no verifier that achieves a higher utility, by construction. At a verifier-leading Stackelberg equilibrium, the verifier will thus choose a policy that achieves R V = 0 R_{V}=0 , although it doesn’t have to be a perfect classifier.

[71] p: Suppose the completeness property is not satisfied, which means

[72] table: ∃ x , 𝟙 correct ​ ( x , τ ∗ ​ ( s ) ) = 1 ​ and ​ v ∗ ​ ( x , τ ∗ ​ ( s ) ) < 1 . \displaystyle\exists x,\mathds{1}_{\text{correct}}\left({x,\tau^{*}(s)}\right)=1\text{ and }v^{*}(x,\tau^{*}(s))<1.

[73] p: However, this would add a nonzero value to the classification loss, contradicting R V = 0 R_{V}=0 .

[74] p: Suppose the soundness property is not satisfied, which means that there exist x x and z z such that

[75] table: 𝟙 correct ​ ( x , z ) = 0 ​ and ​ v ∗ ​ ( x , z ) > 0 . \displaystyle\mathds{1}_{\text{correct}}\left({x,z}\right)=0\text{ and }v^{*}(x,z)>0.

[76] p: Due to R V ​ ( v ∗ ) = 0 R_{V}(v^{*})=0 , τ ′ ⁣ ∗ \tau^{\prime*} has to satisfy

[77] table: v ∗ ​ ( x , τ ′ ⁣ ∗ ​ ( s , y ) ) = 𝟙 correct ​ ( x , τ ′ ⁣ ∗ ​ ( s , y ) ) . \displaystyle v^{*}(x,\tau^{\prime*}(s,y))=\mathds{1}_{\text{correct}}\left({x,\tau^{\prime*}(s,y)}\right).

[78] p: If τ ′ ⁣ ∗ ​ ( s , y ) \tau^{\prime*}(s,y) is correct, then it can be changed to be incorrect to satisfy role-alignment and thus improve R T R_{T} . If τ ′ ⁣ ∗ ​ ( s , y ) \tau^{\prime*}(s,y) is incorrect, so that v ∗ ​ ( x , τ ′ ⁣ ∗ ​ ( s , y ) ) = 𝟙 correct ​ ( x , τ ′ ⁣ ∗ ​ ( s , y ) ) = 0 v^{*}(x,\tau^{\prime*}(s,y))=\mathds{1}_{\text{correct}}\left({x,\tau^{\prime*}(s,y)}\right)=0 , then τ ′ ⁣ ∗ \tau^{\prime*} can again increase R T R_{T} by changing its output at ( s , y ) (s,y) to the convincing proof z z which achieves v ∗ ​ ( x , z ) > 0 v^{*}(x,z)>0 . Both of those scenarios contradict the assumption that τ ′ ⁣ ∗ \tau^{\prime*} is at an equilibrium.

[79] p: Suppose that the translator τ ∗ \tau^{*} is not faithful, which means that there exists x x such that

[80] table: 𝟙 faithful ​ ( x , τ ∗ ​ ( s ⁡ ( x ) ) ) = 0 . \displaystyle\mathds{1}_{\text{faithful}}\left({x,\tau^{*}(s(x))}\right)=0.

[81] p: Then, one can improve R T R_{T} by simply changing τ ∗ ​ ( s ​ ( x ) ) \tau^{*}(s(x)) to be faithful, thus contradicting that τ ∗ \tau^{*} is at an equilibrium.

[82] p: We have proved by contradiction that ( v ∗ , τ ∗ ) (v^{*},\tau^{*}) from any verifier-leading Stackelberg equilibrium must satisfy completeness, soundness, and faithfulness. ∎

[83] h2: Appendix B Further Details of the Experimental Setup

[84] p: We use a temperature of 0.7 0.7 for the solver, and 1.0 1.0 for the translators. We constrain the solver output to a maximum length of 2048 tokens, and do the same for the translator. Since the solver could be interrupted before outputting a final answer, we append a short text \n\n**Final Answer**\n\boxed to all the solver generations that were stopped midway, and generate up to 20 more tokens, to force an answer. The solver receives the user prompt “ {problem}\n\n Please reason step by step, and put your final answer in \boxed{}”. The prompts used for the faithful and sneaky translators are given in Appendix E . We use the AdamW optimizer ( Loshchilov and Hutter, 2017 ) for all training. For RL training, we use a rank 1 LoRA training ( Hu et al., 2022 ) , following recent results from Schulman and Lab (2025) .

[85] p: We train the solver with RLOO on the same subset of the data used later for training the translators. We train with a learning rate of 5 × 10 − 5 5\times 10^{-5} and batch size 28 28 , with β = 0.001 \beta=0.001 for KL regularization, and 4 generations per prompt. The reward function assigns 1.0 1.0 for solutions with correct final answers and 0.0 0.0 otherwise, where answer correctness is determined by extracting the content from \boxed{} and checking symbolic equivalence with the ground truth using SymPy ( Meurer et al., 2017 ) . The training is done for 8 epochs.

[86] p: For verifier training, we train with a learning rate of 2 × 10 − 5 2\times 10^{-5} and batch size 32 32 , and use the regularization hyperparameter λ = 0.005 \lambda=0.005 in the objective. We train the verifier for 4 epochs. For translator training with RLOO, we train with learning rate of 5 × 10 − 5 5\times 10^{-5} and batch size 28 28 , β = 0.001 \beta=0.001 for KL regularization, and 4 generations per prompt. We use r role = r score = − 2.0 r_{\mathrm{role}}=r_{\mathrm{score}}=-2.0 . We train for up to 8 8 epochs. To reduce computation, we early stop when the sneaky translator’s average verifier score exceeds the helpful translator’s average verifier score, on correct solver outputs. Specifically, we use an exponential moving average of verifier scores from all the previous training steps, with α = 0.02 \alpha=0.02 . We perform a total of 8 rounds of checkability training.

[87] h2: Appendix C Reproduction of Prover-Verifier Games (Baseline)

[88] figure: Figure 2: Round 1 and 2 of the baseline prover-verifier game.

[89] p: We also reproduced the ordinary PVG training in Kirchner et al. (2024) , which doesn’t have a separate solver. The method isn’t completely the same, as we added a unit variance normalization for the verifier score in the reward of the prover, and provide the correct answer to the sneaky prover. Both were choices made to accelerate the checkability training, since we found that the training was too slow otherwise. Another difference is the use of RLOO instead of PPO ( Schulman et al., 2017 ) , and using different models—they used models from the GPT4 family, but didn’t reveal the exact model sizes. Yet another difference is that they used the Bradley-Terry loss for verifier training, while we use the standard cross-entropy loss. One final difference is the prompts, which we report in Appendix F . Except for the above stated differences, we tried to stay as faithful as possible to their stated implementation. The training dynamics for rounds 1 and 2 are shown in Fig. 2 . Unlike with our decoupled PVG, the accuracy of the helpful prover starts degrading after some number of training steps, which matches the report in their research. In round 4, the sneaky prover failed to reach the verifier score of the helpful prover for 8 epochs, so we simply stopped the checkability training at round 4.

[90] h2: Appendix D Samples from the Checkability-Trained Models.

[91] p: Below, we show the solver and the translator outputs, in our decoupled prover-verifier game. The ground truth answer is “168”, and the problem is as follows: “A librarian recorded that yesterday there were 42 books borrowed. Today, the number borrowed was 3 times the number borrowed yesterday. How many books were borrowed in total?”

[92] p: First, we see that the initial base solver Llama-2-7b-chat gets the answer wrong, but after undergoing RL training, it outputs the correct answer. The base faithful translator is overly verbose, limiting its legibility. At round 8, the faithful translator outputs a much shorter proof, and gets straight to the point. The sneaky translator also became “sneakier” after training than at initialization, by not aggregating the numbers from the two steps and instead just outputting the last step’s number.

[93] h2: Appendix E Prompts for Decoupled Prover-Verifier Games

[94] p: The { problem }, { solver_output },{ solver_final_answer }, and { ground_truth } are replaced with the problem x x , the solver output s ⁡ ( x ) s(x) , the final answer in the solver output, and the ground truth answer y ⁡ ( x ) y(x) .

[95] h2: Appendix F Prompts for Prover-Verifier Games (Baseline)

[96] h2: Instructions for reporting errors

[97] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[98] p: Tip: You can select the relevant text first, to include it in your report.

[99] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[100] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
