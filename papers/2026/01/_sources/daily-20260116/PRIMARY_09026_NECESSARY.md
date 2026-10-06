# Exact-v1 minimum primary: 2601.09026

Source: https://arxiv.org/html/2601.09026v1 . Only selected necessary method/evaluation/counterevidence; full fetched body is not a whole-paper review.

## Raw body offsets 11038–23233

3.1 ODE formulation of Transformers
We consider transformer architectures with pre-layer normalization (54). Forward propagation through the encoder with NEncN_{\text{Enc}} layers is given as
𝐗n+1\displaystyle\mathbf{X}_{n+1}
=𝐗n+h(φ1​(𝐗n,𝜽n,1)+φ2​(𝐗n+φ1​(𝐗n,𝜽n,1),𝜽n,2))⏟:=𝑭Enc​(tn,𝐗n),\displaystyle=\mathbf{X}_{n}+h\underbrace{\left(\varphi_{1}\,(\mathbf{X}_{n},\boldsymbol{\theta}_{n,1})+\varphi_{2}\,(\mathbf{X}_{n}+\varphi_{1}\,(\mathbf{X}_{n},\boldsymbol{\theta}_{n,1}),\boldsymbol{\theta}_{n,2})\right)}_{:=\boldsymbol{F}_{\text{Enc}}(t_{n},\mathbf{X}_{n})},
(1)
where 𝐗n\mathbf{X}_{n} is the nn-th layer input, 𝐗n+1\mathbf{X}_{n+1} is the nn-th layer output, and h=1h=1 for standard transformers.
The symbol 𝜽n,j\boldsymbol{\theta}_{n,j} denotes the parameters of the nn-th layer’s jj-th sublayer, which is parametrized by evaluating 𝑭Enc\boldsymbol{F}_{\text{Enc}} at tnt_{n}.
The functions φ1\varphi_{1} and φ2\varphi_{2} are defined as φ1:=SA∘LN\varphi_{1}:=\operatorname{SA}\circ\operatorname{LN}, and
φ2:=MLP∘LN\varphi_{2}:=\operatorname{MLP}\circ\operatorname{LN},
where SA\operatorname{SA}, LN\operatorname{LN}, and MLP\operatorname{MLP} denote self-attention, layer norm, and MLP respectively.
Decoder-only architectures are similar, with the addition of a causal mask in the attention.
In case of encoder-decoder architectures, the decoder, with NDecN_{\text{Dec}} layers,
has the form:
𝐘n+1\displaystyle\mathbf{Y}_{n+1}
=𝐘n+h(𝐘¯n+φ2(𝐘n+𝐘¯n,𝜽n,2))⏟:=𝑭Dec​(tn,𝐘n,𝐗NEnc),\displaystyle=\mathbf{Y}_{n}+h\underbrace{\bigl(\overline{\mathbf{Y}}_{n}+\varphi_{2}(\mathbf{Y}_{n}+\overline{\mathbf{Y}}_{n},\boldsymbol{\theta}_{n,2})\bigl)}_{:=\boldsymbol{F}_{\text{Dec}}(t_{n},\mathbf{Y}_{n},\mathbf{X}_{N_{\text{Enc}}})},
(2)
where 𝐘¯n=φ1​(𝐘n,𝜽n,1)+φ3​(𝐘n+φ1​(𝐘n,𝜽n,1),𝐗NEnc,𝜽n,3)\overline{\mathbf{Y}}_{n}=\varphi_{1}(\mathbf{Y}_{n},\boldsymbol{\theta}_{n,1})+\varphi_{3}(\mathbf{Y}_{n}+\varphi_{1}(\mathbf{Y}_{n},\boldsymbol{\theta}_{n,1}),\mathbf{X}_{N_{\text{Enc}}},\boldsymbol{\theta}_{n,3}).
The symbol 𝜽n\boldsymbol{\theta}_{n} denotes the parameters of nn-th decoder layer, 𝐘n\mathbf{Y}_{n} denotes the nn-th decoder-layer input, and 𝐗NEnc\mathbf{X}_{N_{\text{Enc}}} denotes the encoder output.
The function φ3\varphi_{3} is φ3:=CA∘LN\varphi_{3}:=\operatorname{CA}\circ\operatorname{LN}, where CA is cross-attention.
To facilitate application of parallel-in-time, we associate the transformer architecture with a neural ODE.
The idea of viewing the forward propagation as ODE discretizations was first introduced for ResNets in 17, establishing a continuous-depth perspective on deep networks.
The stability and well-posedness of the forward propagation was then studied in 24; 35; 7, where the authors apply several numerical schemes to train deep neural networks.
This ODE-based formulation was later expanded to encoder-only transformers in 44 and 30.
We further extend the formulation to encoder-decoder transformer architectures.
To this aim, let the final “time" be T:=TEnc+TDecT:=T_{\text{Enc}}+T_{\text{Dec}}, TEnc:=h​NEncT_{\text{Enc}}:=hN_{\text{Enc}}, and TDec:=h​NDecT_{\text{Dec}}:=hN_{\text{Dec}}, where hh is analogous to a time-step size.
For encoder-decoder transformers, we stack the encoder states 𝐗\mathbf{X} and the (shifted) decoder states 𝐘\mathbf{Y}, such that the forward propagation through the transformer is defined as
𝐙n+1:=[𝐗n+1,𝐘n+1−NEnc]=𝐙n+h​𝐅​(tn,𝐙n),\displaystyle\mathbf{Z}_{n+1}:=[\mathbf{X}_{n+1},\mathbf{Y}_{n+1-N_{\text{Enc}}}]=\mathbf{Z}_{n}+h\,\mathbf{F}(t_{n},\mathbf{Z}_{n}),
(3)
where 𝐗n:=𝐗NEnc,∀n>NEnc,\mathbf{X}_{n}:=\mathbf{X}_{N_{\text{Enc}}},\ \forall n>N_{\text{Enc}}, and 𝐘n:=𝐘0,∀n<NEnc.\mathbf{Y}_{n}:=\mathbf{Y}_{0},\ \forall n<N_{\text{Enc}}.
In other words, 𝐗\mathbf{X} the encoder state is fixed after the final encoder step, while 𝐘\mathbf{Y} is constant during the encoder stages.
The function 𝐅\mathbf{F} is given as
𝐅(t,[𝐗,𝐘],):={[𝑭Enc​(t,𝐗),         0CLOSE],if t<TEnc,[        0,𝑭Dec(t,𝐘,𝐗)],if t≥TEnc.\mathbf{F}(t,[\mathbf{X},\mathbf{Y}],):=\begin{cases}[\boldsymbol{F}_{\text{Enc}}(t,\mathbf{X}),\;\;\;\;\;\;\;\;\;\mathbf{0}&\hskip-8.5359pt],\ \ \text{if $t<T_{\text{Enc}}$},\\
[\;\;\;\;\;\;\;\;\mathbf{0}\;\;\;\;\;\;,\;\boldsymbol{F}_{\text{Dec}}(t,\mathbf{Y},\mathbf{X})&\hskip-8.5359pt],\ \ \text{if $t\geq T_{\text{Enc}}$.}\end{cases}
For encoder-only transformers, T:=TEncT:=T_{\text{Enc}}, 𝐙:=𝐗\mathbf{Z}:=\mathbf{X}, and 𝑭:=𝑭Enc\boldsymbol{F}:=\boldsymbol{F}_{\text{Enc}} with an easy alteration for decoder-only transformers.
Thus, we can interpret the transformer forward propagation
(3) as a forward Euler discretization with time step h=1h=1 of the initial value problem (IVP) in eq. 4 (left) where 𝜽\boldsymbol{\theta} is defined on [0,T][0,T], with 𝜽n\boldsymbol{\theta}_{n} representing the value at tnt_{n}.
Here, for a given time t∈[0,T]t\in[0,T], 𝑭\boldsymbol{F} depends on the states 𝐙⁡(t)\mathbf{Z}(t) and parameters 𝜽⁡(t)\boldsymbol{\theta}(t). The initial value 𝐙0\mathbf{Z}_{0} is defined analogously on 𝐗0\mathbf{X}_{0} and 𝐘0\mathbf{Y}_{0}, which denote the positionally-encoded source and target embeddings, respectively.
Next, the gradients required for training can be then obtained by solving the adjoint equation in eq. 4 (right) backward in time. Here, ℒ\mathscr{L} is the loss and 𝝀⁡(tn)\boldsymbol{\lambda}(t_{n}) is the backpropagated gradients at the nn-th layer.
forward:{d​𝐙d​t=𝑭⁡(𝐙,𝜽)𝐙⁡(0)=𝐙0backward:{∂𝝀∂t=𝝀T​∂𝐅∂𝐙𝝀⁡(tN)=∂ℒ∂𝐙⁡(tN)\mbox{forward:}\begin{cases}\frac{d\mathbf{Z}}{dt}=\boldsymbol{F}(\mathbf{Z},\boldsymbol{\theta})\\
\mathbf{Z}(0)=\mathbf{Z}_{0}\end{cases}\quad\quad\mbox{backward:}\begin{cases}\frac{\partial{\boldsymbol{\lambda}}}{\partial t}=\boldsymbol{\lambda}^{T}\frac{\partial\mathbf{F}}{\partial\mathbf{Z}}\\
{\boldsymbol{\lambda}}(t_{N})=\frac{\partial\mathscr{L}}{\partial\mathbf{Z}(t_{N})}\end{cases}
(4)
3.2 MGRIT: inexact forward and backward propagation
MGRIT constructs a hierarchy of discretizations of the IVPs (4).
Starting with a fine time-step size hh on level 00, progressively coarser discretizations are constructed with a coarsening factor cf∈ℕ+c_{f}\in\mathbb{N}^{+} (e.g., the first coarse-level has step size cf​hc_{f}h, the second coarse-level cf2​hc_{f}^{2}h, and so on). The coarser levels correct the fine-grid solution, accelerating convergence to the serial solution. The fine-grid is evaluated only locally, in a highly parallel manner.
Two-level MGRIT:
1. Parallel FCF-relaxation
   with 𝐒0\mathbf{S}_{0} 
2. Restrict 𝐫0=𝐆0−𝐀0​𝐖0\mathbf{r}_{0}=\mathbf{G}_{0}-\mathbf{A}_{0}\mathbf{W}_{0}
   to coarse-level, set as 𝐫1\mathbf{r}_{1} 
3. Solve for coarse-level
   error 𝐞1\mathbf{e}_{1} serially with
   𝐀1​𝐞1=𝐫1\mathbf{A}_{1}\mathbf{e}_{1}=\mathbf{r}_{1}
4. Correct fine-level
   solution with 𝐞1\mathbf{e}_{1}
Figure 2: Two-level MGRIT pseudocode (left), MGRIT diagram with cf=2c_{f}=2, L=2L=2 on 2 devices (right).
3.2.1 Inexact MGRIT forward propagation
For the MGRIT hierarchy, let l=0​…​L−1{l=0\ldots L-1} for LL total levels, then define 𝐀l​𝐖l=𝐆l\mathbf{A}_{l}\mathbf{W}_{l}=\mathbf{G}_{l} where
𝐀l=[I(−I−cfl​h​𝐅1)I⋱⋱(−I−cfl​h​𝐅Nl−1)I],\displaystyle\mathbf{A}_{l}=\begin{bmatrix}I&\\
(-I-c_{f}^{l}h\mathbf{F}_{1})&I\\
&\ddots&\ddots\\
&&(-I-c_{f}^{l}h\mathbf{F}_{N_{l}-1})&I\\
\end{bmatrix},\,
𝐖l=[𝐙1𝐙2𝐙Nl],𝐆l=[(I+cfl​h​𝐅0)​𝐙0𝟎𝟎],\displaystyle\mathbf{W}_{l}=\begin{bmatrix}\mathbf{Z}_{1}\\
\mathbf{Z}_{2}\\
\vdots\\
\mathbf{Z}_{N_{l}}\end{bmatrix},\,\mathbf{G}_{l}=\begin{bmatrix}(I+c_{f}^{l}h\mathbf{F}_{0})\mathbf{Z}_{0}\\
\mathbf{0}\\
\vdots\\
\mathbf{0}\end{bmatrix},
and number of time-steps Nl=N/cflN_{l}=N/c_{f}^{l}. For l=0l=0 this is the iterative evolution Eq. 3 written as a system. The variable cfc_{f} is a user-defined integer coarsening factor (often 22 or 44).
The initial condition is implicitly included in the first entry of 𝐆l\mathbf{G}_{l}.
The application of the nonlinear operator 𝐀l\mathbf{A}_{l} written in matrix notation is understood as component-wise nonlinear composition (e.g. 𝐅k​𝐙k=𝐅k​(𝐙k)\mathbf{F}_{k}\mathbf{Z}_{k}=\mathbf{F}_{k}(\mathbf{Z}_{k})).
Remark: The exact solution to the system when l=0l=0 yields the same state vector 𝐖0\mathbf{W}_{0} as would be obtained from forward propagation of the neural ODE transformer.
Further, the solution to the system l+1l+1 is an O⁡(h)O(h) approximation of the system at ll.
Figure 2 outlines the algorithmic approach used by a 2-level MGRIT method (L=2L=2) to exploit this hierarchy to solve 𝐀0​𝐖0=𝐆0\mathbf{A}_{0}\mathbf{W}_{0}=\mathbf{G}_{0}. The first step of this algorithm, see Fig. 2 (left), applies a smoothing operator 𝐒l≈𝐀l−1\mathbf{S}_{l}\approx\mathbf{A}_{l}^{-1} on the fine grid.
This smoother
is selected to reduce high frequency errors in a parallel way (15).
A form of block Jacobi, FCF-relaxation (fine-coarse-fine), is the approach taken in layer-parallel and is described in detail in Appendix A and 23.
For level ll, the application of FCF has Nl/cflN_{l}/c_{f}^{l} way parallelism. Figure 2 (right) indicates this parallel relaxation phase with the red and blue arrows. The red arrows execute concurrently, followed by concurrent execution of the blue arrows. After relaxation the error has been reduced locally over subsets of layers, yet no end to end communication has occurred.
Step 2 in Fig. 2 computes the residual 𝐫0=𝐆0−𝐀0​𝐖0\mathbf{r}_{0}=\mathbf{G}_{0}-\mathbf{A}_{0}\mathbf{W}_{0} on the fine grid and then “restricts” the residual with injection to the coarse level (orange arrows), yielding 𝐫1\mathbf{r}_{1}. In the third step,
the “coarse solve” step (yellow arrows) computes the error on the coarse-level implied by the residual by solving 𝐀1​𝐞1=𝐫1\mathbf{A}_{1}\mathbf{e}_{1}=\mathbf{r}_{1} exactly.
This communicates end-to-end across the domain in serial, albeit at a factor of cfc_{f} cheaper than the fine grid (the number of time steps is N0/cfN_{0}/c_{f} on level 1).
In Step 4, this error correction is “interpolated” back up to the fine grid (green arrows). The algorithm repeats as required until a stopping criteria is met.
One iteration of this algorithm is referred to as a V-cycle.
To create a hierarchy with more levels, the serial coarse solve can be replaced with another two-level solve and the whole process proceeds recursively.
The serial coarsest-level solve will then be cfL−1c_{f}^{L-1} times cheaper than the fine grid, with additional parallel relaxation work done on intermediate levels.
Critical for layer-parallel performance is that only a handful of V-cycle iterations are needed for sufficient accuracy, which results in approximate forward or backward propagation.
To initialize MGRIT for the system 𝐀0\mathbf{A}_{0}, we distribute the layers across multiple GPUs.
In Figure 2 (right), an example is shown, where an 8 layer network is split over 2 GPUs/devices; a coarsening factor of cf=2c_{f}=2 is shown.
The example shows the second GPU stores 𝐅4\mathbf{F}_{4} through 𝐅7\mathbf{F}_{7}, and an initial guess for 𝐗4\mathbf{X}_{4}. GPU-aware MPI is used for inter-device communication. See 9 for more implementation details.
Similar to model parallelism, layer-parallel distributes the network across multiple GPUs, reducing the per device memory requirement.
3.2.2 Inexact MGRIT backward propagation
To evaluate the gradients in parallel, the same MGRIT algorithm can be applied to solve the discretized adjoint problem (4) (right) backward in time; see (23; 9) for details.
Notably, in many cases, a single MGRIT iteration for the adjoint problem is enough to approximate the gradient with sufficient accuracy, enabling significant speedups.
This behavior is consistent with findings in the literature, which indicate that optimizer convergence is significantly more sensitive to noise in the loss function evaluations than in gradient evaluations (2; 34).
As a result, the MGRIT forward solve typically requires more iterations than backward. In the results section, forward iterations will refer to the number of MGRIT iterations used for forward propagation, and backward iterations for backward propagation, which will typically be smaller.


## Raw body offsets 23233–32500

3.2.3 Adaptive control of the inexactness
Statistically biased error from inexact gradient evaluations is known to change the convergence properties of stochastic gradient descent algorithms. However, theory indicates that this can be mitigated if the error can be controlled as the minima is approached (32; 12).
Thus, detecting when the error is too large relative to the gradient is crucial for the application of corrective measures such as increasing the number of iterations or switching to exact solves.
Due to the nonlinearity of transformers, MGRIT may require too many iterations to obtain a sufficient speedup relative to serial.
To address this, we monitor the effectiveness of MGRIT iterations during training by evaluating the “convergence factor”, defined as the ratio of consecutive fine-level residuals for iteration kk,
‖𝐫0(k+1)‖/‖𝐫0(k)‖\|\mathbf{r}_{0}^{(k+1)}\|/\|\mathbf{r}_{0}^{(k)}\|. A small convergence factor implies rapid convergence. To ensure robustness, we periodically, every few (e.g. 500) batches, double the number of MGRIT iterations to monitor the convergence factor of the final iteration.
A convergence factor above 11 indicates that the iteration count is no longer effective. The mitigation either improves the accuracy by increasing iteration count, or switching to serial training. Our results confirm, as suggested by the biased SGD theory (12), that despite the initial phase using inexact gradients, the improved accuracy
in later stages leads to a network with comparable performance.
4 Numerical Results
To evaluate the efficacy of layer-parallel training and inference, we consider the following networks and applications, with additional details provided in the Appendix.
1. 
BERT pre-training is the classical language modeling training problem for a pure encoder only network.
The training objectives are the next sentence prediction (NSP) and masked-language modeling (MLM), however we only utilize MLM learning (33).
We use the C4 dataset
(46) for pretraining data.
2. 
Morphological classification (MC) is associated with classifying a word to its morphological class (noun, adjective, adverb, etc).
We use the GUM corpus (56) dataset from Universal Dependencies (40) and employ the neural ODE encoder-only transformer architecture, specified in 44.
3. 
Vision transformer (ViT) is an encoder-only image transformer (16).
We apply a classical ViT to the ImageNet dataset (13).
4. 
Machine translation (MT) consists of translating German sentences into English using the OPUS data set (49), the pre-trained MarianTokenizer (49), and an encoder-decoder transformer inspired by 27
with the neural ODE modifications from above.
5. 
GPT2 pre-training is the decoder-only language model developed by OpenAI (45).
We use the nanoGPT implementation (28) trained on OpenWebText (22) with minor modifications to the time stepping detailed in appendix B.
For each task, we demonstrate that layer-parallel forward and backward propagation, with adaptive control of inexactness, achieves the same accuracy as serial computations.
We further show the strong scalability properties with respect to a varying number of transformer blocks NN, the MGRIT coarsening factor cfc_{f}, and the number of MGRIT levels LL.
Hyperparameter configurations for all benchmark problems are provided in the Appendix.
002020404075758080Epochs Val. acc 2020404060600.20.20.250.250.30.3Epochs Val. BLEU GPUs 3 1 3 2 3 4 3 8 GPUs 3 1 3 2 3 2–>1 3 2–>1 
Figure 3: The long term training behavior using sequential versus layer-parallel with multiple GPUs.
On the left, the validation accuracy for the MC example with 64 transformer layers, L=2L=2, and cf=2c_{f}=2. On the right, the validation BLEU for the MT example with 6-6 transformer layers, L=2L=2, and cf=3c_{f}=3.
The plot corresponding to “2–>1” label illustrates a switch from parallel training with 2 GPUs to serial training with 1 GPU.
Note that two depicted “2–>1” runs switch from a parallel to serial run at different points during the training.
4.1 Convergence of MGRIT
In this section, we demonstrate the impact of the layer-parallel approach on training accuracy.
MC Training
Figure 3 (left) compares the behavior of sequential and layer-parallel training with increasing number of GPUs.
The inexactness in the gradients does not negatively impact the validation accuracy: layer-parallel achieves the same accuracy as serial training.
MT Training
Figure 3 (right) illustrates how the error may accumulate due to inexact loss and gradient evaluations resulting in slight deterioration in validation BLEU compared to the serial baseline.
However, switching to sequential training after an efficient, parallel phase, allows the optimizer to quickly recover the validation BLEU score achieved in serial.
BERT/GPT/ViT Pretraining
In Figure 4 (left), we show the loss value of pretraining a 128 layer BERT model (53) using serial (blue), pure layer-parallel (red) and switching from parallel to serial (green, with multiple seeds shaded in grey).
The layer-parallel configuration is 2 levels for both forward and backward solve, and cf=4c_{f}=4 on 4 GPUs.
We use this large model as an exemplar for the loss dynamics.
During pretraining, layer-parallel converges past the loss plateau typical of BERT (37; 20), but diverges and then stagnates due to the inexactness.
We can use the indicator as described in Section 3.2.3 to demarcate the need to switch to using serial (exact) gradient computations.
Figure 4 (left, green) shows after switching training dynamics closely match the serial case.
In Table 1, performance differences are displayed for a few GLUE benchmarks comparing serial trained models, to those trained with the switching training schemes.
The differences between the fine-tuned models demonstrate layer-parallel yields parallel speedups and commensurate accuracy.
The loss results for GPT and ViT follows an extremely similarly trajectory, as shown in Figure 4 (middle/right).
While GPT is a decoder-only network, and ViT operates on image data, we see that inexact gradients (red) causes a divergence in training dynamics compared to exact dynamics (blue).
However, by using the indicator, we are able to recover the dynamics by switching from serial to parallel where the indicator Figure 5 dictates.
We use a 32 layer ViT with the neural ODE modification with the serial forward, and one level parallel backwards for MGRIT using 2 GPUs.
The GPT network consists of 20 layers with the neural ODE modification on only the middle 16 layers with serial forward and one level parallel backwards; for more detail, please see Appendix B.
10152044556677Batches (x1000) Loss 
01233.53.5444.54.5555.55.5Batches (x1000) 
0246810556677Batches (x1000) 
Figure 4: 
Plots of the loss for serial (blue), pure parallel (red) and switching to serial from parallel (green) for the BERT (left), GPT (middle) and ViT (right). In all the experiments, we see that purely layer-parallel runs will diverge from serial training after a certain point.
However, one can recover the original dynamics by switching from parallel to serial at an appropriate time given by the indicator.
The gray color in the BERT subplot indicates the min/max over three different seeds.
02460.50.5111.51.522Batches (x1000) Indicator 
00.510.50.511Batches (x1000) 
0246000.50.511Batches (x1000) 
Figure 5: The indicator values for BERT (forward in red, backward in blue), ViT and GPT (backward in blue) using MGRIT.
We see that at the 70000th batch, 1000th, and 6000th batch respectively, the indicators exceed 1, meaning that one should switch to exact gradient computation then.
Table 1: Absolute differences in loss and accuracy for subset of GLUE task performance comparison between serial and parallel followed by serial (adaptive switching)
Task Name
Δ\Delta in Loss
  Δ\Delta in Acc.
CoLA (Corpus of Linguistic Acceptability)
3.99e-4
0%0\%
MRPC (Microsoft Research Paraphrase Corpus)
1.10e-2
0%0\%
QNLI (Question Natural Language Inference)
3.38e-4
1.2%1.2\%
124800112233GPUs Speedup 11224488GPUs 11224488GPUs NEncN_{\text{Enc}}32326464128128256256
Figure 6: 
Speedup of layer-parallel for encoder-only transformers using L=2L=2.
Left: BERT, on Singra, 1 forward, and 1 backward iteration, with cf=4c_{f}=4.
Middle: MC, on Jean-Zay, 2 forward, 1 backward iterations, with cf=2c_{f}=2.
Right: ViT, on Singra, serial forward, and 1 backward iteration, with cf=4c_{f}=4.
See appendix C for system details.
24811223344GPUs Speedup 248GPUs 248GPUs NEnc−NDecN_{\text{Enc}}-N_{\text{Dec}}40−4040-4080−8080-80160−160160-160Ideal
Figure 7: Strong scaling on Jean-Zay with respect to increasing number of layers NEnc+NDecN_{\text{Enc}}+N_{\text{Dec}} for MT task.
MGRIT uses cf=4c_{f}=4, L=2L=2, 11 backward, and 22 forward iterations. 
24811223344GPUs Speedup 248GPUs 248GPUs 1, 2, 3, 4 LL22334455cfc_{f} 2\ 2 4\ 4 8\ 81616NEncN_{\text{Enc}} 256\ 256 512\ 512 768\ 76810241024
Figure 8: The impact of MGRIT parameters on scaling properties.
The experiment is performed using 2 forward and 1 backward iteration for the MC task on Jean-Zay.
Left: cf=2c_{f}=2 and NEnc=1024N_{\text{Enc}}=1024. Middle: L=2L=2 and NEnc=1024N_{\text{Enc}}=1024. Right: L=3L=3 and cf=4c_{f}=4. The blank line depicts ideal scaling.
4.2 S

## Raw body offsets 32495–35070

4.2 Scaling studies
In this section, we investigate the parallel scaling properties of the layer-parallel approach.
Figure 6 shows the speedup achieved for encoder-only transformers: (left) the BERT task with cf=4c_{f}=4, (middle) the MC task with cf=2c_{f}=2, and (right) the ViT model with cf=4c_{f}=4.
All tasks use L=2L=2 levels.
The obtained results indicate that the numerical and communication overhead introduced by MGRIT may occasionally lead to increased execution time when using two GPUs for small problems.
However, as more computational resources are employed for deeper models, the layer-parallelism enabled by MGRIT yields a substantial reduction in the overall execution time.
A similar conclusion is drawn from Figure 7. The strong scaling properties for the encoder-decoder architecture used in the MT task are illustrated. The model size ranges from 8080 layers, to 320320 layers. While there are apparent speedups, additional improvements can be obtained using alternative algorithmic parameters for layer-parallel.
We provide practical guidance for parameter selection by analyzing the impact of the number of levels (LL), coarsening factor (cfc_{f}), and transformer depth (N)(N) on the parallel scaling.
To this end, we consider the MC example with layer-parallel configured to perform two forward and one backward iteration.
Figure 8 shows that the scalability improves with an increasing number of levels (left) and larger coarsening factors (middle).
However, taking a large coarsening factor can have an impact on the convergence rate (18; 15). The last panel (right) show the benefits of layer-parallel training improve with network depth.
Finally, we perform a large scale study combining two different but compatible parallelization methods: layer-parallel with the typical data parallel approach.
We consider a relatively large 64 layer GPT model with scaling batch sizes, but otherwise the same settings as the GPT pretraining as above.
In Figure 9, we show the results for budgets of 16, 32, and 64 total GPUs with batch sizes of 16, 32, and 64, respectively, so that the overall per-GPU work-load is uniform.
The xx-axis denotes the data-parallel degree. For example, when using 32 total GPUs with a data-parallel size of 8, the batch is split across 8 ranks (i.e., 8 samples per GPU), while the model is partitioned with layer-parallel across the remaining 32/8=432/8=4 GPUs, resulting in approximately 16 transformer layers per GPU.
For each of the three GPU budgets, the time per batch is a parabolic function of the data parallel size.


## Raw body offsets 59400–62521

 as one trains a GPT2-decoder network.
Note that the last few layers are the first to change, followed by the initial transformer layer.
In Figure 10, we show the estimated Lipschitz constants during the training of a GPT2 decoder network in the usual serial fashion.
Remarkably, as the network trains and becomes more expressive, the rate of change of the Lipschitz constant at each layer is not uniform.
It appears that the last few layers change significantly first, followed by the initial layers, while the middle layers remain stagnant for longer.
It is known that the gradient updates are greater in magnitude [53] for the deeper layers, but we cannot explain the rise in the Lipschitz constant for the early layers.
We note that the change in the Lipschitz constant is unrelated to the change in the magnitude of the weights themselves, ‖w−w0‖‖w0‖\frac{\norm{w - w_0}}{\norm{w_0}} where ww is the weights at a specific iteration and w0w_{0} denotes the initial weights, as shown in Figure 11.
Figure 11: Plots illustrating the changes in relative weight values during the training of a GPT decoder-only network, with transformer weights broken down into attention and MLP components.
While all layers clearly change, the impact on the Lipschitz constant is not direct.
Regardless of the mechanics driving the change in the Lipschitz constant, the prescription for MGRIT is clear: create “buffer” layers where the first and last layers are computed serially, targeting exact computation of the layers with large estimated Lipschitz constants.
MGRIT will perform layer-parallel computations on the middle portion, where the estimated Lipschitz constants are more modest.
In other words, a few transformer layers are moved to the open/close layers in Figure 1 from the ParallelNet.
Besides moving the layers, we also tweaked the Δ​t\Delta t (e.g. hh from Equation 3) for the open/close layers: we simply give them Δ​t=1\Delta t=1 for the open/close layers, while the transformer layers in the ParallelNet will have the typical Δ​t=1L\Delta t=\frac{1}{L} where LL is the number of layers in the ParallelNet.
This method results in greatly increased alignment between the serial and parallel runs in decoder-only networks, as shown in the Figure 12.
012345333.53.5444.54.555Batches (x1000) Loss Serial (buffer)Serial (no buffer)
012345000.20.20.40.40.60.6Batches (x1000) Abs. Val. of Difference in Loss BufferNo buffer
Figure 12: (Left) Loss plots of training GPT-2 decoders in serial for two different configurations.
The buffer indicates four of the twenty layers are in the open/close layer (two each) with the remaining sixteen in the middle with Δ​t=1/16\Delta t=1/16.
The no buffer indicates all the layers are in the middle with Δ​t=1/20\Delta t=1/20.
There is no significant difference in loss between the serial versions of the two configurations.
(Right) The absolute difference between the two serial runs against their corresponding layer parallel runs.
While the serial dynamics are similar, note that having the buffer layers significantly reduces difference between layer parallel loss and serial loss.


## Raw body offsets 62521–64800

Appendix C Hyperparameter and experimental setup
The implementation uses the layer-parallel software TorchBraid [9] built on PyTorch.
Experiments and scaling studies are conducted on the HPC systems: Jean-Zay GPU nodes, each equipped with eight V100 and 720 GB of memory and Singra GPU compute nodes, consisting of dual AMD EPYC 7513 Processors and a single A100 80GB GPU.
Table 2 specifies the hyperparameters for the transformers used to generate the results presented in Section 4.
For all except the BERT, the parameters of the transformer layers are initialized using PyTorch’s default initialization.
For the BERT initialization, we follow the pre-LN initialization scaling detailed in [53] that provides enough stability for us to train the extremely long BERT network without gradient collapse.
In particular, the MLP, value, and output projections of the transformers are scaled by log⁡2​L\sqrt{\log 2L}.
The BERT data is preprocessed using a masked-language modeling with 20%20\%, which is higher than the original BERT manuscript, but has been found to be useful in more recent implementations [33].
Table 3 reports the MGRIT configuration used for the strong scaling experiments described in Section 4.
Additionally, Table 4 summarizes the hyperparameter values used for tuning the MT task, obtained using Bayesian optimization.
Table 5 shows the hyperparameters for the GLUE fine-tuning; we remark that fine-tuning on the 128 layers BERT model proved to be challenging, but we only seek to compare the serial versus the parallel-switching training procedures.
Finally, we note that dropout is often used for regularization, however, the layer parallel paradigm cannot simply adopt the Dropout classes in existing software.
This is because the layers corresponding to exactly cfc_{f} (e.g. layers 1, 3, 5, 7 in Figure 2) must have the same masks while doing the relaxation and the coarse solve to ensure the iterations will converge.
As such, we implemented a solution whereby the masks do not update unless explicitly specified by the user.
Parameter / Example
BERT
MC
ViT
MT
GPT
Batch-size BB
32
8
4
8
256
Dim. feed-forward
3072
128
3072
2048
3072
Dropout
0.1
-
-
0.1
-
Max. length LL / Patch size (ViT)
224
2048
16
274
1024
Optimizer
AdamW
SGD
Adam
Adam
AdamW
Mode
