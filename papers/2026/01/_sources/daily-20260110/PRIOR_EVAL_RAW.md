Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning (https://arxiv.org/html/2601.04710v1)
citeturn26865view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04710v1","lineno":290}); Total lines: 649
L125: 3:   Compute guiding vector: $v\leftarrow\textsc{ComputeGuidingVector}(\theta,M,\alpha,s,\mathcal{B})$
L126: 
L127: 4:   GuidingPerturbation($\theta$, $+\epsilon$, $v$)
L128: 
L129: 5:   Evaluate $\mathcal{L}^{+}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L130: 
L131: 6:   GuidingPerturbation($\theta$, $-2\epsilon$, $v$)
L132: 
L133: 7:   Evaluate $\mathcal{L}^{-}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L134: 
L135: 8:   GuidingPerturbation($\theta$, $+\epsilon$, $v$)
L136: 9:   Estimate directional gradient: $g\leftarrow(\mathcal{L}^{+}-\mathcal{L}^{-})/(2\epsilon)$
L137: 
L138: 10:   Update parameters: $\theta\leftarrow\theta-\eta\cdot(g\cdot v)$
L139: 
L140: 11:  end for
L141: 
L142: Algorithm 2 Subroutines for MeZO with Guiding Vector
L143: 
L144: 1:  Subroutine: ComputeGuidingVector($\theta$, $M$, $\alpha$, $s$, $\mathcal{B}$)
L145: 
L146: 2:  Initialize perturbation set $\mathcal{O}\leftarrow\emptyset$
L147: 
L148: 3:  for particle $i=1$ to $M$ do
L149: 
L150: 4:   Generate unique seed $s_{i}\leftarrow\text{Hash}(s\oplus i)$
L151: 5:   RandomPerturbation($\theta$, $\epsilon$, $s_{i}$)
L152: 
L153: 6:   Evaluate fitness $l_{i}\leftarrow\mathcal{L}(\theta;\mathcal{B})$
L154: 
L155: 7:   RandomPerturbation($\theta$, $-\epsilon$, $s_{i}$)
L156: 
L157: 8:   Store perturbation seed $s_{i}$
L158: 
L159: 9:   $\mathcal{O}\leftarrow\mathcal{O}\cup\{(l_{i},s_{i})\}$
L160: 
L161: 10:  end for
L162: 
L163: 11:  Sort $\mathcal{O}$ by ascending $l_{i}$ values
L164: 
L165: 12:  Split into elite/non-elite groups:
L166: 
L167: 13:   $\mathcal{O}_{\text{top}}\leftarrow\text{First}(\lfloor\alpha M\rfloor,\mathcal{O})$
L168: 14:   $\mathcal{O}_{\text{bottom}}\leftarrow\text{Last}(M-\lfloor\alpha M\rfloor,\mathcal{O})$
L169: 
L170: 15:  Compute guide vector through the $z_{i}$ corresponding to the seed $s_{i}$ :
L171: 
L172: 16:   $v_{\text{top}}\leftarrow\frac{1}{|\mathcal{O}_{\text{top}}|}\sum_{(l_{i},s_{i})\in\mathcal{O}_{\text{top}}}z_{i}$
L173: 
L174: 17:   $v_{\text{bottom}}\leftarrow\frac{1}{|\mathcal{O}_{\text{bottom}}|}\sum_{(l_{i},s_{i})\in\mathcal{O}_{\text{bottom}}}z_{i}$
L175: 
L176: 18:  $v\leftarrow v_{\text{top}}-v_{\text{bottom}}$
L177: 
L178: 19:  Return $v$
L179: 
L180: 20:
L181: 21:  Subroutine: GuidingPerturbation($\theta$, $\epsilon$, $v$)
L182: 
L183: 22:  for each parameter $\theta_{j}\in\theta$ do
L184: 
L185: 23:   $\theta\leftarrow\theta+\epsilon\cdot v$
L186: 
L187: 24:  end for
L188: 
L189: 25:
L190: 
L191: 26:  Subroutine: RandomPerturbation($\theta$, $\epsilon$, $s$)
L192: 
L193: 27:  Reset random number generator with seed $s$
L194: 
L195: 28:  for each parameter $\theta_{j}\in\theta$ do
L196: 
L197: 29:   $z_{j}\sim\mathcal{N}(0,1)$
L198: 
L199: 30:   $\theta_{j}\leftarrow\theta_{j}+\epsilon\cdot z_{j}$
L200: 
L201: 31:  end for
L202: ### III-B Memory-efficient ZO with Greedy Perturbation
L203: In addition to the guiding vector mechanism, we propose another Memory-efficient ZO with Greedy Perturbation (MeZO-Greedy) strategy as a complementary optimization component to further enhance the performance of the optimization process. MeZO-Greedy functions as an independent mechanism that actively explores the most promising update directions at each iteration.
L204: Specifically, the algorithm generates a set of $M$ candidate perturbations $\{\bm{z}_{i}\}_{i=1}^{M}$, where each $\bm{z}_{i}$ is sampled from a predefined distribution. The greedy selection process then identifies the optimal perturbation $\bm{z}^{*}$ that minimizes the loss function in the vicinity of the current parameters:
L205:  | $$\bm{z}^{*}=\text{arg min}_{\bm{z}_{i}}\mathcal{L}(\bm{\theta}+\epsilon\bm{z}_{i};\mathcal{B}),$$  |  | (7)
L206: 
L207: where $\epsilon$ controls the exploration radius, and $\mathcal{B}$ represents the current mini-batch of data, the selected perturbation $\bm{z}^{*}$ encapsulates the most favorable direction for parameter updates based on immediate feedback from the loss landscape, effectively capturing the local geometry of the optimization surface.
L208: Building upon this selected direction, we calculate an independent gradient estimate using a symmetric difference approximation:
L209: 
L210:  | $$\hat{\nabla}^{*}\mathcal{L}(\bm{\theta};\mathcal{B})=\frac{\mathcal{L}(\bm{\theta}+\epsilon\bm{z}^{*};\mathcal{B})-\mathcal{L}(\bm{\theta}-\epsilon\bm{z}^{*};\mathcal{B})}{2\epsilon}\bm{z}^{*},$$  |  | (8)
L211: 
L212: Then the parameters $\bm{\theta}$ are updated using the Equation cite60†4 . The complete algorithmic implementation is presented in Algorithm cite63†3 and cite64†4 .
L213: Algorithm 3 MeZO with Greedy Strategy
L214: 
L215: 0:  Parameters $\theta\in\mathbb{R}^{d}$, loss function $\mathcal{L}(\theta;\mathcal{B})$, step budget $T$, perturbation scale $\epsilon$, batch size $\mathcal{B}$, learning rate $\eta$, weight decay $\lambda$, candidate perturbations $M$
L216: 
L217: 1:  for iteration $t=1$ to $T$ do
L218: 
L219: 2:   Sample minibatch $\mathcal{B}_{t}\sim\mathcal{D}$ and random seed $s$
L220: 3:   Compute optimal perturbation: $z^{*}\leftarrow\textsc{ComputeGreedyPerturbation}(\theta,M,\epsilon,s,\mathcal{B}_{t})$
L221: 
L222: 4:   GreedyPerturbation($\theta$, $+\epsilon$, $z^{*}$)
L223: 
L224: 5:   Evaluate $\mathcal{L}^{+}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L225: 
L226: 6:   GreedyPerturbation($\theta$, $-2\epsilon$, $z^{*}$)
L227: 
L228: 7:   Evaluate $\mathcal{L}^{-}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L229: 
L230: 8:   GreedyPerturbation($\theta$, $+\epsilon$, $z^{*}$)
L231: 9:   Estimate directional gradient: $g\leftarrow(\mathcal{L}^{+}-\mathcal{L}^{-})/(2\epsilon)$
L232: 
L233: 10:   Update parameters: $\theta\leftarrow\theta-\eta\cdot(g\cdot z^{*})$
L234: 
L235: 11:  end for
L236: 
L237: Algorithm 4 Subroutines for MeZO with Greedy Strategy
L238: 
L239: 1:  Subroutine: ComputeGreedyPerturbation($\theta$, $M$, $\epsilon$, $s$, $\mathcal{B}$)
L240: 
L241: 2:  Initialize perturbation set $\mathcal{O}\leftarrow\emptyset$
L242: 
L243: 3:  for particle $i=1$ to $M$ do
L244: 
L245: 4:   Generate unique seed $s_{i}\leftarrow\text{Hash}(s\oplus i)$
L246: 5:   RandomPerturbation($\theta$, $\epsilon$, $s_{i}$)
L247: 
L248: 6:   Evaluate fitness $l_{i}\leftarrow\mathcal{L}(\theta;\mathcal{B})$
L249: 
L250: 7:   RandomPerturbation($\theta$, $-\epsilon$, $s_{i}$)
L251: 
L252: 8:   Store perturbation $z_{i}$ and loss $l_{i}$
L253: 
L254: 9:   $\mathcal{O}\leftarrow\mathcal{O}\cup\{(l_{i},z_{i})\}$
L255: 
L256: 10:  end for
L257: 
L258: 11:  Find the optimal perturbation:
L259: 
L260: 12:   $z^{*}\leftarrow\text{arg min}_{(l_{i},z_{i})\in\mathcal{O}}l_{i}$
L261: 
L262: 13:  Return $z^{*}$
L263: 
L264: 14:
L265: 15:  Subroutine: GreedyPerturbation($\theta$, $\epsilon$, $z^{*}$)
L266: 
L267: 16:  for each parameter $\theta_{j}\in\theta$ do
L268: 
L269: 17:   $\theta_{j}\leftarrow\theta_{j}+\epsilon\cdot z^{*}_{j}$
L270: 
L271: 18:  end for
L272: 
L273: 19:
L274: 
L275: 20:  Subroutine: RandomPerturbation($\theta$, $\epsilon$, $s$)
L276: 
L277: 21:  Reset random number generator with seed $s$
L278: 
L279: 22:  for each parameter $\theta_{j}\in\theta$ do
L280: 
L281: 23:   $z_{j}\sim\mathcal{N}(0,1)$
L282: 
L283: 24:   $\theta_{j}\leftarrow\theta_{j}+\epsilon\cdot z_{j}$
L284: 
L285: 25:  end for
L286: ## IV Theory Analysis
L287: 
L288: ### IV-A Per-Step Decrease Analysis with Prior-Informed ZO
L289: 
L290: To investigate the approximation efficiency of the expectation in Equation cite65†3 , we first present the following lemma.
L291: ###### Lemma 1.
L292: 
L293: Under the ZO setting, assume the optimization problem has dimension $d$, and the sampling number is $k$, where $z_{1},z_{2},\ldots,z_{k}\sim\mathcal{N}(0,I_{d})$. Let $\epsilon>0$ and $\delta>0$, and define
L294: 
L295:  | $$S_{k}=\frac{1}{k}\sum_{i=1}^{k}z_{i}z_{i}^{T}.$$  |
L296: When $k=O\!\left(\frac{1}{\epsilon^{2}}\log\!\left(\frac{d}{\delta}\right)\right)$, with probability at least $1-\delta$, we have $\|S_{k}-I_{d}\|\leq\epsilon$. Note that in practice, the experimental configuration of MeZO with $K=1$ is far from this theoretical bound, indicating that its approximation efficiency is unsatisfactory.
L297: ###### Proof.
L298: 
L299: By the Matrix Bernstein inequality,
L300: 
L301:  | $$P(\|S_{k}-I_{d}\|\geq t)\leq d\cdot\exp\!\left(-\frac{kt^{2}}{\sigma^{2}+\tfrac{Lt}{3}}\right),$$  |
L302: 
L303: where $\sigma^{2}=\tfrac{1}{k}$ and $L=\|z_{i}\|^{2}\leq d+O(\sqrt{d})$. Setting $t=\epsilon$ and equating the right-hand side to $\delta$ completes the proof. ∎
L304: ###### Lemma 2.
L305: 
L306: Under the ZO setting, suppose the problem has dimension $d$, and we draw $k$ independent samples $z_{1},z_{2},\ldots,z_{k}\sim\mathcal{N}(0,I_{d})$. Let $g$ be the true gradient (normalized such that $\|g\|=1$). Define
L307: 
L308:  | $$V=\frac{1}{k}\sum_{i=1}^{k}z_{i}z_{i}^{T}g,\quad V_{\parallel}=(V^{T}g)g,\quad V_{\perp}=V-V_{\parallel}.$$  |
L309: 
L310: Then the following estimates hold:
L311:  | $\displaystyle\text{ratio}_{1}$  | $\displaystyle=\frac{\|V_{\parallel}\|}{\|V_{\perp}\|}\;\;\approx\;\sqrt{\tfrac{k}{d-1}},$  |
L312:  | $\displaystyle\text{ratio}_{2}$  | $\displaystyle=\frac{\|V_{\parallel}\|}{\|g\|}\;\;\approx\;1.$  |
L313: ###### Proof.
L314: 
L315: Clearly $V=(V^{T}g)g+V_{\perp}$, where $V_{\parallel}=(V^{T}g)g$ and
L316: 
L317:  | $$V_{\perp}=\frac{1}{k}\sum_{i=1}^{k}(z_{i}^{T}g)z_{i,\perp},$$  |
L318: 
L319: with $z_{i,\perp}$ denoting the projection of $z_{i}$ onto the orthogonal complement of $g$. Taking expectations yields $E[V_{\parallel}]=g$, $E[V_{\perp}]=0$, and
L320: 
L321:  | $$E[\|V_{\perp}\|^{2}]=\mathrm{Tr}(\mathrm{Cov}(V_{\perp}))=\tfrac{1}{k}\mathrm{Tr}(I_{d}-gg^{T})=\tfrac{d-1}{k}.$$  |
L322: 
L323: ∎
L324: Lemma cite66†1 and Lemma cite67†2 together show that while $V$ is an unbiased estimate of $g$, the ratio $\|V\|/\|g\|\approx 1$ serves as a measure of how much the estimated gradient lies in the true direction of the gradient. A larger ratio indicates that the estimated gradient has a stronger component aligned with the true gradient, thereby indicating better alignment.
L325: ###### Lemma 3.
L326: 
L327: Under the ZO setting with greedy permutation, assume the optimization problem has dimension $d$ and sampling number $k$, where $z_{1},z_{2},\ldots,z_{k}\sim\mathcal{N}(0,I_{d})$, and $g$ is the gradient direction (without loss of generality, assume $\|g\|=1$). By decomposition, we have $z_{i}=(z_{i}^{T}g)g+z_{i,\perp}$, let $Y_{i}=z_{i}^{T}g$, and denote $Y_{1}=\min_{1\leq i\leq k}Y_{i}$. Its PDF is
L328: 
L329:  | $$f(y)=k(1-\Phi(y))^{k-1}\phi(y).$$  |
L330: 
L331: Now consider
L332:  | $$V=z_{1}z_{1}^{T}g=(Y_{1}g+z_{1,\perp})(Y_{1}g+z_{1,\perp})^{T}g=Y_{1}^{2}g+Y_{1}z_{1,\perp},$$  |
L333: 
L334: where $V_{\parallel}=Y_{1}^{2}g$ and $V_{\perp}=Y_{1}z_{1,\perp}$. Then we obtain
L335: 
L336:  | $\displaystyle\text{ratio}_{1}$  | $\displaystyle=\frac{\|V_{\parallel}\|}{\|V_{\perp}\|}=\frac{|Y_{1}|}{\|z_{1,\perp}\|}\approx\frac{|Y_{1}|}{\sqrt{d-1}}\approx\frac{\sqrt{2\log(k)}}{\sqrt{d-1}},$  |
L337:  | $\displaystyle\text{ratio}_{2}$  | $\displaystyle=\frac{\|V_{\parallel}\|}{\|g\|}=Y_{1}^{2}\approx 2\log(k).$  |
L338: ###### Proof.
L339: 
L340: Suppose we sample $k$ points and order them as
L341: 
L342:  | $$Y_{1}<Y_{2}<\cdots<Y_{k},\quad Y_{i}=z_{i}^{T}g.$$  |
L343: 
L344: Selecting the $i$-th smallest value corresponds to the $\tfrac{i}{k+1}$-quantile of the standard normal distribution. Hence
L345: 
L346:  | $$\mathbb{E}[Y_{i}]\approx\Phi^{-1}\!\left(\tfrac{i}{k+1}\right).$$  |
L347: 
L348: For the extreme case $i=1$, using the tail approximation of the Gaussian quantile we obtain
L349: 
L350:  | $$|Y_{1}|\approx\sqrt{2\log(k)}.$$  |
L351: 
L352: ∎
L353: Lemma cite68†3 shows that under greedy permutation, the ratio $\|V_{\parallel}\|/\|g\|\approx 2\log(k)$ quantifies how strongly the estimated gradient aligns with the true gradient. Compared with MeZO, greedy selection greatly amplifies the parallel component, enabling MeZO-Greedy to achieve larger single-step decreases at the same learning rate, and thus more efficient descent.
L354: ###### Lemma 4.
L355: 
L356: Under the ZO setting with a guiding vector, suppose the problem has dimension $d$, sampling number $k$, and the gradient direction $g$ with $\|g\|=1$. Let $\sigma$ denote the fraction of sparks used to form the guiding vector, and set $s=\lfloor\sigma k\rfloor$. Decompose $z_{i}=(z_{i}^{T}g)g+z_{i,\perp}$, let $Y_{i}=z_{i}^{T}g$, and order them as $Y_{1}<Y_{2}<\cdots<Y_{k}$. Define index sets $\Lambda_{1}=\{1,\dots,s\}$ and $\Lambda_{2}=\{k,k-1,\dots,k-s+1\}$, and construct
L357:  | $$\hat{z}=\frac{1}{s}\Big(\sum_{i\in\Lambda_{1}}z_{i}-\sum_{j\in\Lambda_{2}}z_{j}\Big).$$  |
L358: 
L359: Then $V=\hat{z}\hat{z}^{T}g=V_{\parallel}+V_{\perp}$, with
L360: 
L361:  | $$\text{ratio}_{1}=\frac{\|V_{\parallel}\|}{\|V_{\perp}\|}\approx\frac{2\sqrt{s\log k}}{\sqrt{d-1}},\quad\text{ratio}_{2}=\frac{\|V_{\parallel}\|}{\|g\|}\approx 8s\log k.$$  |
L362: ###### Proof.
L363: 
L364: Decompose $\hat{z}$ as
L365: 
L366:  | $$\hat{z}=\frac{1}{s}\Big(\sum_{i\in\Lambda_{1}}Y_{i}g-\sum_{j\in\Lambda_{2}}Y_{j}g\Big)+\frac{1}{s}\Big(\sum_{i\in\Lambda_{1}}z_{i,\perp}-\sum_{j\in\Lambda_{2}}z_{j,\perp}\Big)\\
L367: =\frac{1}{s}(mg+N),$$  |
L368: 
L369: where
L370: 
L371:  | $$m=\sum_{i\in\Lambda_{1}}Y_{i}-\sum_{j\in\Lambda_{2}}Y_{j}\approx 2\sum_{i=1}^{s}Y_{i}\approx 2s\sqrt{2\log k},$$  |
L372: 
L373: and $N\sim\mathcal{N}(0,2s(I_{d}-gg^{T}))$ with $\|N\|\approx\sqrt{2s(d-1)}$. Then
L374:  | $$V=\hat{z}\hat{z}^{T}g=\frac{1}{s}(m^{2}g+mN)=V_{\parallel}+V_{\perp},$$  |
L375: 
L376: so that
L377: 
L378:  | $$\text{ratio}_{1}=\frac{\|V_{\parallel}\|}{\|V_{\perp}\|}\approx\frac{|m|}{\|N\|}\approx\frac{2\sqrt{s\log k}}{\sqrt{d-1}}$$  |
L379:  | $$\text{ratio}_{2}=\frac{\|V_{\parallel}\|}{\|g\|}\approx\frac{m^{2}}{s}\approx 8s\log k.$$  |
L380: 
L381: ∎
L382: The $\text{ratio}_{2}$ show that increasing $s$ or $k$ significantly strengthens the parallel component $V_{\parallel}$, enhancing alignment with the true gradient and improving the effectiveness of ZO updates. This explains why the guiding vector strategy achieves a stronger single-step descent compared with standard MeZO.
L383: Table cite69†I compares the baseline ZO estimator with its variants in terms of the gradient-aligned component ratio. Both ZO-Greedy and ZO-GV substantially improve alignment with the gradient direction: ZO-Greedy benefits from order statistics, while ZO-GV leverages the guiding vector construction. In particular, ZO-GV achieves the strongest alignment as $s$ and $k$ increase.
L384: TABLE I: Comparison of Gradient-aligned Component Ratios
L385: Algorithm  | ZO  | ZO-Greedy  | ZO-GV
L386: --- | --- | --- | ---
L387: $\|V_{\parallel}\|/\|V_{\perp}\|$  | $\sqrt{\tfrac{k}{d-1}}$  | $O\!\left(\tfrac{\sqrt{\log k}}{\sqrt{d-1}}\right)$  | $O\!\left(\tfrac{\sqrt{s\log k}}{\sqrt{d-1}}\right)$
L388: $\|V_{\parallel}\|/\|g\|$  | $1$  | $O(\log k)$  | $O(s\log k)$
L389: TABLE II: The prompts of the datasets used in our OPT experiments.
L390: Dataset Type  | Task Type  | Prompt
L391: --- | --- | ---
L392: SST-2  | cls.  | <text> It was terrible/great
L393: RTE  | cls.  | <premise> Does this mean that “<hypothesis>” is true? Yes or No?
L394:  |  | Yes/No
L395: CB  | cls.  | Suppose <premise> Can we infer that “<hypothesis>”? Yes, No, or Maybe?
L396:  |  | Yes/No/Maybe?
L397: BoolQ  | cls.  | <passage> <question>?
L398:  |  | Yes/No
L399: WSC  | cls.  | <text>
L400:  |  | In the previous sentence, does the pronoun “<span2>” refer to “<span1>”? Yes or No?
L401:  |  | Yes/No
L402: WIC  | cls.  | Does the word “<word>” have the same meaning in these two sentences? Yes or No?
L403:  |  | <sent1>
L404:  |  | <sent2>
L405:  |  | Yes/No
L406: MultiRC  | cls.  | <paragraph>
L407:  |  | Question: <question>
L408:  |  | I found this answer “<answer>”. Is that correct? Yes or No?
L409:  |  | Yes/No
L410: COPA  | mch.  | <premise> so/because <candidate>
L411: ReCoRD  | mch.  | <passage>
L412:  |  | <query>.replace(“@placeholder”, <candidate>)
L413: SQuAD  | QA  | Title: <title>
L414:  |  | Context: <context>
L415:  |  | Question: <question>
L416:  |  | Answer:
L417: DROP  | QA  | Passage: <context>
L418:  |  | Question: <question>
L419:  |  | Answer:
L420: TABLE III: Consolidated Hyperparameters for OPT and Llama2 (Batch Size: 16, Subspace Frequency: {500, 1000, 2000})
L421: Tuning Type  | Algorithm Variants  | Learning Rate  | $\epsilon$  | $k$  | Rank
L422: --- | --- | --- | --- | --- | ---
L423: Full Tuning (FT)  | MeZO / SubZero  | {1e-7, 2e-7, 5e-7}  | 1e-3  | –  | {32, 64}
L424: MeZO-GV / SubZero-GV  | {1e-7, 2e-7, 3e-7, 5e-7}  | 1e-3  | 4  | {32, 64}
L425: SGD  | {1e-4, 1e-3, 5e-3}  | –  | –  | –
L426: LoRA  | MeZO / SubZero  | {3e-5, 5e-5, 1e-4}  | 1e-2  | –  | {32, 64}
L427: MeZO-GV / SubZero-GV  | {3e-5, 5e-5, 1e-4}  | 1e-2  | 4  | {32, 64}
L428: Prefix-Tuning  | MeZO / SubZero  | {1e-3, 5e-3, 1e-2}  | 1e-1  | –  | {8, 16}
L429: MeZO-GV / SubZero-GV  | {1e-3, 5e-3, 1e-2}  | 1e-1  | 4  | {8, 16}
L430: ## V Experiments and Analysis
L431: LLM fine-tuning tasks and models For all experiments, we consider the SuperGLUE [cite70†15 ] dataset collection, which includes CB [cite71†16 ], COPA [cite72†17 ], MultiRC [cite73†18 ], RTE [cite74†19 ], WiC [cite75†20 ], WSC [cite76†21 ], BoolQ [cite77†22 ], and ReCoRD [cite78†23 ]. Additionally, we incorporated SST-2 [cite79†24 ] and two question-answering (QA) datasets: SQuAD [cite80†25 ] and DROP [cite81†26 ]. We also conduct experiments on two representative language models of varying sizes.
L432: For OPT [cite34†7 ], we test the OPT-1.3B, OPT-13B, and OPT-30B models, while for Llama2 [cite82†27 ], we evaluate the Llama2-7B-hf and Llama2-13B-hf models.
L433: Datasets As shown in Table cite83†II , the datasets utilized in our experiments encompass three types of tasks: classification tasks, multiple choice tasks, and question-answer tasks. Previous studies [cite28†1 , cite84†28 , cite85†29 ] have demonstrated that incorporating appropriate prompts ensures that fine-tuning objectives are closely aligned with the pre-training one. Specifically, simple prompts can streamline the fine-tuning optimization, enabling zeroth-order methods to work efficiently [cite35†8 ].
L434: We investigate three fine-tuning schemes to validate the proposed method: full-tuning (FT), which fine-tunes the entire pre-trained model; low-rank adaptation (LoRA), which fine-tunes the model by introducing low-rank weight perturbations [cite31†4 ]; and prefix-tuning (Prefix), which fine-tunes the model by appending learnable parameters to the attention mechanism of Transformers [cite33†6 ].
L435: Setup. We compare our methods with zero-shot, in-context learning (ICL), and fine-tuning with Adam (FT). Additionally, we validate the effectiveness of our methods by applying them to MeZO [cite35†8 ] and SubZero [cite59†14 ]. Following the MeZO, we randomly sample 1,000 examples for training, 500 examples for validation, and 1,000 examples for testing. Unless otherwise specified, we set the query budget per gradient estimation to $q=1$ and the hyperparameter $\alpha$ to 0.5.
L436: The number of prior-estimated times $M$ is set to either 2 or 4. To maintain identical computational cost, MeZO and SubZero are run for 20,000 steps, whereas our proposed method is trained for 10,000 or 5000 steps. All models are validated every 1,000 steps. To reduce memory consumption, we employ half-precision training (FP16) for zeroth-order optimization (ZO) methods. All experiments are conducted on Nvidia A100 GPUs with 80GB of memory or Nvidia 3090 GPUs with 24GB of memory.
L437: Detailed learning rates, batch sizes, and other hyperparameter configurations for the different models are provided in Table cite86†III . Our code is available in https://github.com/stan-anony/MeZO-GV
L438: TABLE IV: Comparison of average task performance across different methods on OPT-1.3B over three rounds. Results are reported for zero-shot, in-context learning (ICL), and MeZO-based methods, including variants with guiding vectors (GV), LoRA, and prefix tuning. The best performance for each task is highlighted in bold.
L439: Task Type  | —– classification —–  | —– multiple choice —–  | —– generation —–
L440: --- | --- | --- | ---
L441: Task  | SST2  | RTE  | CB  | BoolQ  | WSC  | WIC  | MultiRC  | COPA  | ReCoRD  | SQuAD  | DROP
L442: Zero-shot  | 53.6  | 53.1  | 39.3  | 44.9  | 43.3  | 53.5  | 45.4  | 73.0  | 70.5  | 27.2  | 11.2
L443: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L444: ICL  | 80.0  | 53.4  | 44.6  | 59.4  | 46.2  | 50.3  | 46.3  | 69.0  | 71.0  | 58.7  | 20.5
L445: MeZO(FT)  | 89.2  | 57.4  | 71.4  | 62.5  | 56.7  | 57.2  | 53.3  | 73.0  | 70.9  | 72.0  | 21.9
L446: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---

