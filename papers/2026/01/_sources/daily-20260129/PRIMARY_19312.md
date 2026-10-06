# 2601.19312v1 — necessary primary excerpts

Source: https://arxiv.org/html/2601.19312v1

L132: The Schrödinger–Bass (SBB) problem is an extension of the classical SB problem by jointly optimizing over both drift and volatility. It is introduced and studied in (cite48†Alouadi et al., 2026 ). Given two distributions $\mu_{0},\mu_{T}\in{\cal P}(\mathbb{R}^{d})$, the goal is to minimize, over $\mathbb{P}\in{\cal P}(\mu_{0},\mu_{T})=\big\{\mathbb{P}\in{\cal P}(\Omega):X_{0}\overset{\mathbb{P}}{\sim}\mu_{0},\;X_{T}\overset{\mathbb{P}}{\sim}\mu_{T}\big\}$, the quadratic cost:
L133:  | $$J(\mathbb{P})=\mathbb{E}_{\mathbb{P}}\Big[\int_{0}^{T}\underbrace{\|\alpha_{t}\|^{2}+\beta\|\sigma_{t}-\sqrt{\varepsilon}I_{d}\|^{2}}_{H_{\beta}(\alpha_{t},\sigma_{t})}\,\mathrm{d}t\Big],$$  |  | (6)
L134: 
L135: for some $\beta>0$, where $(\alpha,\sigma)$ is the drift/volatility of $X$ under $\mathbb{P}$, i.e., $\mathrm{d}X_{t}=\alpha_{t}\,\mathrm{d}t+\sigma_{t}\,\mathrm{d}W_{t}$. This problem is denoted by ${\rm SBB}(\mu_{0},\mu_{T}):=\inf_{\mathbb{P}\in{\cal P}(\mu_{0},\mu_{T})}J(\mathbb{P})$.
L136: Note that as $\beta\to\infty$, the volatility $\sigma$ is constrained to equal $I_{d}$, recovering the classical SB problem. Conversely, dividing (cite49†6 ) by $\beta$ and letting $\beta\to 0$ forces the drift term $\alpha$ to vanish, yielding the Bass martingale transport problem. In other words, the parameter $\beta$ controls the relative weight of drift versus volatility, interpolating between these two well-known cases.
L137: ### 3.1 Dual Representation of the Primal SBB
L138: 
L139: The primal problem ${\rm SBB}(\mu_{0},\mu_{T})$ admits a dual representation, which consists of maximizing over a suitable class of functions $(v,\psi)$ the Lagrangian functional
L140: 
L141:  | $\displaystyle L_{\mu_{0},\mu_{T}}(\psi,v)=\int\psi(x)\,\mu_{T}(\mathrm{d}x)-\int v(0,x)\,\mu_{0}(\mathrm{d}x),$  |
L142: 
L143: where $v$ is the value function of the unconstrained stochastic control problem with Bellman equation:
L144:  | $$\begin{cases}\partial_{t}v+H_{\beta}^{*}(\nabla_{x}v,D_{x}^{2}v)=0,\quad\text{on }[0,T)\times\mathbb{R}^{d},\\
L145: v(T,\cdot)=\psi,\quad\text{on }\mathbb{R}^{d},\end{cases}$$  |  | (7)
L146: 
L147: with $H_{\beta}^{*}$ denoting the Fenchel–Legendre transform of $H_{\beta}$, explicitly given by
L148: 
L149:  | $\displaystyle H_{\beta}^{*}(p,q)=\frac{1}{2}|p|^{2}+\frac{\varepsilon\beta}{2}I_{d}:\Big(\big(I_{d}-\frac{q}{\beta}\big)^{-1}-I_{d}\Big),$  |
L150: for $(p,q)\in\mathbb{R}^{d}\times\mathbb{S}_{+}^{d}$ such that $q<\beta I_{d}$. Assuming that ${\rm SBB}(\mu_{0},\mu_{T})<\infty$, we have:
L151: 
L152:   * •
L153: 
L154: Attainment of the primal problem: there exists $(\alpha^{*},\sigma^{*})\leftrightarrow\mathbb{P}^{\rm SBB}$ attaining the infimum in ${\rm SBB}(\mu_{0},\mu_{T})$, in feedback form: $\alpha_{t}^{*}=\mathrm{a}^{*}(t,X_{t})$, $\sigma_{t}^{*}=\vartheta^{*}(t,X_{t})$.
L155: 
L156:   * •
L157: 
L158: Duality relation: we have
L159:  | $${\rm SBB}(\mu_{0},\mu_{T})=\sup_{\begin{subarray}{c}\psi\in C^{2}\cap C_{b}^{\infty}\cap L^{1}(\mu_{T}),\ v\in C_{b}^{1,2},\\
L160: D_{x}^{2}v<\beta I_{d},\ \psi=v(T,\cdot),\\
L161: \partial_{t}v+H_{\beta}^{*}(\nabla_{x}v,D_{x}^{2}v)=0\end{subarray}}L_{\mu_{0},\mu_{T}}(\psi,v)$$  |  | (8)
L162: 
L163:   * •
L164: 
L165: Duality on the control:
L166: When $\mu_{0}$ and $\mu_{T}$ have finite second moment, and if $\beta>\frac{1}{T}$, then the supremum in the dual problem is attained at $(v^{*},\psi^{*})$, and the optimal feedback policies are given by
L167: 
L168:  | $\displaystyle\begin{cases}\mathrm{a}^{*}(t,x)\;=\;\nabla_{x}v^{*}(t,x),\quad(t,x)\in[0,T)\times\mathbb{R}^{d},\\
L169: \vartheta^{*}(t,x)\;=\;\sqrt{\varepsilon}\Big(I_{d}-\frac{D_{x}^{2}v^{*}(t,x)}{\beta}\Big)^{-1}.\end{cases}$  |
L170: ### 3.2 SBB System
L171: 
L172: One can exploit the quadratic form of the SBB criterion to reduce the dual problem to the maximization over the potential $\psi\in C^{2}\cap C_{b}^{\infty}\cap L^{1}(\mu_{T})$, subject to $D_{x}^{2}\psi<\beta I_{d}$, of the Donsker–Varadhan type functional:
L173: 
L174:  | $\displaystyle\int\psi\mathrm{d}\mu_{T}-\int\underbrace{{\cal T}_{\beta}^{+}\Big[\varepsilon\log\int e^{{\cal T}_{\beta}^{-}[\psi](\cdot+z)}{\cal N}_{\varepsilon T}(\mathrm{d}z)\Big]}_{v}(x)\mu_{0}(\mathrm{d}x),$  |
L175: where ${\cal T}_{\beta}^{\pm}$ are the quadratic inf/sup convolution operators:
L176: 
L177:  | $\displaystyle\begin{cases}{\cal T}_{\beta}^{+}[\phi](x):=\displaystyle\inf_{y\in\mathbb{R}^{d}}\big[\phi(y)+\frac{\beta}{2}|x-y|^{2}\big],\quad x\in\mathbb{R}^{d},\\
L178: {\cal T}_{\beta}^{-}[\psi](y):=\displaystyle\sup_{x\in\mathbb{R}^{d}}\big[\psi(x)-\frac{\beta}{2}|x-y|^{2}\big],\quad y\in\mathbb{R}^{d}.\end{cases}$  |
L179: This leads to the SBB system, where a potential $\psi^{*}$ (or $\phi^{*}={\cal T}_{\beta}^{-}[\psi^{*}]=\log h_{T}^{*}$) of the dual SBB problem satisfies:
L180: 
L181:  | $\displaystyle\begin{cases}\mathscr{Y}_{T}\#\mu_{T}=h_{T}^{*}\ \nu_{T},\quad\nu_{T}=\nu_{0}*{\cal N}_{\varepsilon T}\\
L182: \mathscr{Y}_{0}\#\mu_{0}=h_{0}^{*}\,\nu_{0},\quad h_{0}^{*}=h_{T}^{*}*{\cal N}_{\varepsilon T}\end{cases}$  |
L183: 
L184: where $\#$ is the pushforward operator, and the transport map $\mathscr{Y}_{t}$ is defined as :
L185:  | $\displaystyle\mathscr{Y}_{t}=(\nabla_{y}\Phi_{t})^{-1},\quad\Phi_{t}(y)=\frac{|y|^{2}}{2}+\frac{1}{\beta}\varepsilon\log h_{t}^{*}(y),$  |
L186: 
L187: which is an increasing (convex) function from $\mathbb{R}^{d}$ into $\mathbb{R}^{d}$ for any $t\in[0,T]$. Note that when $\beta\to\infty$, $\mathscr{Y}=\mathrm{I_{d}}$ and we recover the Schrödinger system. Conversely, when $\beta\to 0$, $h^{*}$ is constant and we recover the Bass system. The optimal drift and volatility of SBB are given by
L188:  | $\displaystyle\begin{cases}\alpha_{t}^{*}=\varepsilon\nabla_{y}\log h_{t}^{*}(\mathscr{Y}_{t}(X_{t})),\\
L189: \sigma_{t}^{*}=\sqrt{\varepsilon}D_{y}^{2}\Phi_{t}(\mathscr{Y}_{t}(X_{t})),\end{cases}\quad t\in[0,T].$  |
L190: 
L191: If we define the process
L192: 
L193:  | $$Y_{t}=\mathscr{Y}_{t}(X_{t})=X_{t}-\frac{1}{\beta}\varepsilon\nabla_{y}\log h_{t}^{*}(\mathscr{Y}_{t}(X_{t})),\;t\in[0,T],$$  |  | (9)
L194: and the change of measure $\frac{\mathrm{d}\mathbb{Q}^{*}}{\mathrm{d}\mathbb{P}^{\rm SBB}}\Big|_{{\cal F}_{t}}=\frac{1}{h_{t}^{*}(Y_{t})},\;t\in[0,T]$ (which is indeed a $\mathbb{P}^{\rm SBB}$-martingale with expectation $1$ by the SBB system), then
L195: 
L196:   * •
L197: 
L198: $(Y_{t})_{t}$ is a Brownian motion with volatility $\sqrt{\varepsilon}$ under $\mathbb{Q}^{*}$ with initial law $\nu_{0}$.
L199: 
L200:   * •
L201: $X_{t}=\mathscr{Y}_{t}^{-1}(Y_{t})=Y_{t}+\frac{\varepsilon}{\beta}\nabla_{y}\log h_{t}^{*}(Y_{t})$, $t\in[0,T]$, is a stretched Brownian motion under $\mathbb{Q}^{*}$.
L202: 
L203:   * •
L204: 
L205: The dynamics under $\mathbb{P}^{\rm SBB}$ are:
L206: 
L207:  | $$\begin{cases}\mathrm{d}X_{t}=D_{y}^{2}\Phi_{t}(Y_{t})\,\mathrm{d}Y_{t},\\
L208: \mathrm{d}Y_{t}=\varepsilon\nabla_{y}\log h_{t}^{*}(Y_{t})\,\mathrm{d}t+\sqrt{\varepsilon}\,\mathrm{d}W_{t},\end{cases}\quad t\in[0,T].$$  |
L209: In other words, $\mathbb{P}^{\rm SBB}$ is the Bass transport of a SB, i.e., a stretched SB. The SBB system can be visualized in the figure below.
L210: ## 4 Generative Modeling with SBB
L211: 
L212: To generate new samples from $\mu_{T}$ via the learned SBB system, one could directly simulate
L213: 
L214:  | $\displaystyle\mathrm{d}X_{t}$  | $\displaystyle=\;\varepsilon\nabla_{y}\log h_{t}^{*}(\mathscr{Y}_{t}(X_{t}))\,\mathrm{d}t$  |
L215:  |  | $\displaystyle\qquad+\sqrt{\varepsilon}\,D_{y}^{2}\Phi_{t}(\mathscr{Y}_{t}(X_{t}))\,\mathrm{d}W_{t},\;X_{0}\sim\mu_{0},$  |
L216: using an SDE solver (e.g., the Euler–Maruyama scheme) to obtain $X_{T}\sim\mu_{T}$. However, this requires computing the inverse of a Hessian matrix, which can be challenging in high dimensions. To overcome this, one can instead generate the process $Y=\mathscr{Y}(X)$ as a DSB:
L217: 
L218:  | $\displaystyle\mathrm{d}Y_{t}=\varepsilon\nabla_{y}\log h_{t}^{*}(Y_{t})\,\mathrm{d}t+\sqrt{\varepsilon}\,\mathrm{d}W_{t},$  |
L219: 
L220: with $Y_{0}\sim\mathscr{Y}_{0}\#\mu_{0}$ and $Y_{T}\sim\mathscr{Y}_{T}\#\mu_{T}$, and score drift
L221:  | $$s_{t}^{*}(y)=\varepsilon\nabla_{y}\log h_{t}^{*}(y).$$  |
L222: 
L223: Then, $X_{T}$ can be recovered via
L224: 
L225:  | $\displaystyle X_{T}=\mathscr{Y}_{T}^{-1}(Y_{T})=Y_{T}+\frac{1}{\beta}s_{T}^{*}(Y_{T})\sim\mu_{T}.$  |
L226: ### 4.1 Training
L227: 
L228: As Section cite12†2.2.3 provides an efficient way to solve the SB between $\mathscr{Y}_{0}\#\mu_{0}$ and $\mathscr{Y}_{T}\#\mu_{T}$, it remains to learn the transport map $\mathscr{Y}$. Exploiting that $\mathscr{Y}_{t}$ $=$ $\mathscr{X}_{t}^{-1}$ with
L229: 
L230:  | $$\mathscr{X}_{t}(y)\;=\;y+\frac{1}{\beta}s_{t}^{*}(y),$$  |
L231: we can learn the inverse of $\mathscr{X}$ using a neural network ${\cal Z}_{\tilde{\theta}}$ to obtain $\mathscr{Y}$, avoiding the need to solve the fixed point (cite50†9 ). We then introduce LightSBB-M (Algorithm cite51†1 ) to efficiently solve the SBB problem as follows.
L232: Let $\theta=\{\alpha_{j},r_{j},\Sigma_{j}\}_{j=1}^{J}$ denote the parameters of a Gaussian-mixture potential $v_{\theta}$, and $\tilde{\theta}$ the parameters of the neural network $Z_{\tilde{\theta}}$. Initialize $\phi^{0}=0$, hence $\mathscr{Y}^{0}={\cal Z}_{\tilde{\theta}}^{0}=I_{d}$. Then, for $0\leq k\leq K$:
L233: 
L234:   1. 1.
L235: 
L236: Endpoint sampling. Draw endpoint pairs $(y_{0},y_{T})$ from a coupling of $(p_{0}^{k},p_{T}^{k})$, where $p_{t}^{k}=\mathrm{d}(\mathscr{Y}_{t}^{k}\#\mu_{t})/\mathrm{d}y$, using
L237:  | $\displaystyle\begin{cases}\mathscr{Y}_{0}^{k}(x_{0})=y_{0}={\cal Z}_{\tilde{\theta}}^{k}(0,x_{0}),\quad x_{0}\sim\mu_{0},\\
L238: \mathscr{Y}_{T}^{k}(x_{T})=y_{T}={\cal Z}_{\tilde{\theta}}^{k}(T,x_{T}),\quad x_{T}\sim\mu_{T}.\end{cases}$  |
L239: 
L240:   2. 2.
L241: 
L242: Bridge sampling. For $t\sim\mathcal{U}[0,T)$ and $Z\sim\mathcal{N}(0,I_{d})$, sample $y_{t}\sim\mathbb{W}^{\varepsilon}_{|y_{0},y_{T}}$ as an intermediate point from the Brownian bridge:
L243:  | $$y_{t}=\frac{T-t}{T}y_{0}+\frac{t}{T}y_{T}+\sigma_{t}\sqrt{\varepsilon}Z,\quad\sigma_{t}^{2}=\frac{t(T-t)}{T}.$$  |  | (10)
L244: 
L245:   3. 3.
L246: 
L247: Regression step on $\theta$. Update $\theta^{k}$ by minimizing the bridge-matching loss
L248:  | $\displaystyle\mathcal{L}(\theta^{k})$  | $\displaystyle=\mathbb{E}_{t\sim\mathcal{U}([0,T))}\,\mathbb{E}_{y_{T}\sim p_{T},\,y_{t}\sim W^{\varepsilon}_{|y_{0},y_{T}}}$  |
L249:  |  | $\displaystyle\quad\left[\left\|s_{\theta}^{k}(t,y_{t})-\frac{y_{T}-y_{t}}{T-t}\right\|_{2}^{2}\right],$  |  | (11)
L250: 
L251: which is the KL projection onto the set of SBs, ensuring that the learned drift coincides with the true SB drift.
L252: 
L253:   4. 4.
L254: Regression step on $\tilde{\theta}$. Once $\theta^{k+1}$ is obtained, update $\tilde{\theta}^{k}$ by minimizing
L255: 
L256:  | $$\begin{split}\mathcal{L}(\tilde{\theta}^{k})&=\mathbb{E}_{x_{0}\sim\mu_{0},\,x_{T}\sim\mu_{T}}\Big[\|{\cal Z}_{\tilde{\theta}}^{k}(0,\mathscr{X}_{0}(x_{0}))-x_{0}\|^{2}\\
L257: &\qquad\quad+\|{\cal Z}_{\tilde{\theta}}^{k}(T,\mathscr{X}_{T}(x_{T}))-x_{T}\|^{2}\Big].\end{split}$$  |  | (12)
L258: Moreover, using a Gaussian-mixture parametrization of $v$ from LightSB-M, we can derive a closed-form expression for the drift $s_{\theta}\triangleq s_{v_{\theta}}$ (cite39†Gushchin et al., 2024 ) as follows:
L259:  | $$\begin{split}s_{\theta}(t,y)&=\varepsilon\,\nabla_{y}\log\mathcal{N}\!\left(y\,\middle|\,0,\,\varepsilon(T-t)I_{d}\right)\\
L260: &\quad\times\sum_{j=1}^{J}\alpha_{j}\,\mathcal{N}\!\left(r_{j}\,\middle|\,0,\,\varepsilon\Sigma_{j}\right)\,\mathcal{N}\!\left(h_{j}(t,y)\,\middle|\,0,\,A^{t}_{j}\right),\end{split}$$  |  | (13)
L261: where $A^{t}_{j}\triangleq\frac{t}{\varepsilon(T-t)}I_{d}+\frac{1}{\varepsilon}\Sigma_{j}^{-1}$ and $h_{j}(t,y)\triangleq\frac{y}{\varepsilon(T-t)}+\frac{1}{\varepsilon}\Sigma_{j}^{-1}r_{j}$.
L262: 
L263: Algorithm 1 LightSBB-M Training Algorithm
L264: 
L265:  Input: Samples $(x_{0}^{m},x_{T}^{m})_{m\leq M}\sim(\mu_{0},\mu_{T})$, $\theta=\{\alpha_{j},\mu_{j},\Sigma_{j}\}_{j\leq J}$, $\tilde{\theta}$, $\beta>0$, $K>0$
L266: 
L267:  Initialization: Start with $\mathscr{Y}^{0}=I_{d}$ and ${\cal Z}_{\tilde{\theta}}^{0}=I_{d}$
L268:  for $k=0,\cdots,K-1$ do
L269: 
L270:   repeat
L271: 
L272:    Draw sample batch of pairs $(x_{0}^{n},x_{T}^{n})_{n\leq N}$
L273: 
L274:    Compute $\mathscr{Y}_{0}^{k}(x_{0}^{n})=y_{0}^{n}={\cal Z}^{k}_{\tilde{\theta}}(0,x_{0}^{n})$ and $\mathscr{Y}_{T}^{k}(x_{T}^{n})=y_{T}^{n}={\cal Z}^{k}_{\tilde{\theta}}(T,x_{T}^{n})$
L275: 
L276:    Sample batch $(y_{t}^{n})_{n\leq N}\sim\mathbb{W}_{|y_{0},y_{1}}$ using  (cite52†10 )
L277: 
L278:    Compute the drift $s_{\theta}^{k}$ using  (cite53†13 ) and update $\theta^{k}$ by minimizing  (cite54†11 )
L279: 
L280:   until convergence
L281:   $\theta^{k+1}\leftarrow{\theta^{k}}$
L282: 
L283:   repeat
L284: 
L285:    Draw sample batch of pairs $(x_{0}^{n},x_{T}^{n})_{n\leq N}$
L286: 
L287:    Compute $\mathscr{X}_{0}(x_{0}^{n})=x_{0}^{n}+\frac{1}{\beta}s_{\theta}^{k+1}(0,x_{0}^{n})$ and $\mathscr{X}_{T}(x_{T}^{n})=x_{T}^{n}+\frac{1}{\beta}s_{\theta}^{k+1}(T,x_{T}^{n})$
L288: 
L289:    Update $\tilde{\theta}^{k}$ by minimizing (cite55†12 )
L290: 
L291:   until convergence
L292: 
L293:   $\tilde{\theta}^{k+1}\leftarrow{\tilde{\theta}^{k}}$
L294: 
L295:  end for
L296: 
L297:  Return $\theta^{K},\;\tilde{\theta}^{K}$
L298: We also provide in Appendix cite25†A alternative algorithms, including a simplification of Algorithm cite51†1 when $\beta$ is large and Sinkhorn-based solver for the SBB problem.
L299: Note that the regression loss (cite54†11 ) rules out arbitrarily small $T$ as the target would explode. On the other hand, an excessively large $T$ drives the noisy marginal $\mu_{T}$ to become almost indistinguishable from $\mu_{0}$, forcing the reverse dynamics to undo an overwhelming amount of noise; this dramatically inflates the variance of the optimal control and deteriorates sample quality. Hence, in practice we choose $T$ away from extremal values and hence too small $\beta$.
L300: Empirically, the proposed alternating procedure converged in a small number of iterations (five in most experiments), consistently yielding stable solutions, despite the absence of a formal convergence proof.
L301: ### 4.2 Inference
L302: Once the drift $s_{\theta}^{K}$ and the transport map ${\cal Z}_{\tilde{\theta}}^{K}$ are trained, one can generate new samples from $\mu_{T}$ by first computing $Y_{0}={\cal Z}_{\tilde{\theta}}^{K}(X_{0})\sim\mathscr{Y}_{0}\#\mu_{0}$, where $X_{0}\sim\mu_{0}$ is an out-of-sample point. Then, sample $Y_{T}\sim\mathscr{Y}_{T}\#\mu_{T}$ according to the learned coupling $\pi_{v_{\theta}}(Y_{T}\,|\,Y_{0})$ given by (cite56†5 ), and recover $X_{T}=Y_{T}+\frac{1}{\beta}\,s_{\theta}^{K}(T,Y_{T})\sim\mu_{T}$.
L303: Alternatively, one could simulate the SDE $\mathrm{d}Y_{t}=s_{\theta}^{K}(t,Y_{t})\,\mathrm{d}t+\sqrt{\varepsilon}\,\mathrm{d}W_{t}$, using a numerical SDE solver (e.g., the Euler–Maruyama scheme), but this approach is generally more time-consuming and introduces additional discretization errors.
L304: Note that the drift $s_{\theta}$ defined in (cite53†13 ) is not well-defined at $t=T$. Nevertheless, by continuity of $\phi=\log h$ with respect to time, we can instead approximate $X_{\tilde{T}}=Y_{\tilde{T}}+\frac{1}{\beta}\,s_{\theta}^{K}(\tilde{T},Y_{\tilde{T}})$, where $\tilde{T}=T-\delta$ for some small $\delta>0$.
L305: ## 5 Numerical Experiments
L306: 
L307: In this section, we present numerical experiments to evaluate the proposed algorithm on both univariate and multivariate datasets. We also provide a comparative analysis against state-of-the-art (SOTA) generative models. In all our experiments, we have used $T=1$.
L308: ### 5.1 Illustrative Examples
L309: We propose to use the SBB framework to transport between two simple distributions. First, we apply SBB between $\mu_{0}={\cal N}(1,2)$ and $\mu_{T}={\cal N}(0,1)$ with parameters $\beta=10$, $K=5$, and $M_{\text{samples}}=2000$. Figure cite57†1 displays the trajectories generated by SBB for this case, as well as for a more challenging setting involving heavy-tailed distributions.
L310: Indeed, one of the main advantages of SBB compared to the classical SB is that it removes the requirement $\mathrm{KL}(\mathbb{P}\|\mathbb{W}^{\varepsilon})<\infty$. To illustrate this property, we consider the case $\mu_{0}=\delta_{0}$ and $\mu_{T}={\cal T}(2)$.
L311: When the reference marginal at time $T$ is Gaussian, the KL divergence between $\mu_{T}={\cal T}(2)$ and the Wiener measure diverges, since the integrand behaves as $x^{2}p_{\text{Student}}(x)\sim 1/|x|$ for large $|x|$, leading to a logarithmic divergence. Consequently, no finite-entropy SB exists between a Dirac initial measure and such a heavy-tailed terminal distribution under a Brownian prior, while the SBB formulation remains well defined and numerically stable.
L312: cite58†Image: Refer to caption L313: 
L314: cite59†Image: Refer to caption L315: 
L316: Figure 1: Transport interpolation using SBB: $\mathcal{N}(1,2)\xrightarrow{}\mathcal{N}(0,1)$ (left) and $\delta_{0}\xrightarrow{}\mathcal{T}(2)$ (right).
L317: ### 5.2 Quantitative Evaluation on Low-Dimensional Datasets
L318: We provide a quantitative evaluation of the proposed SBB method on low-dimensional datasets, namely 8gaussians and moons ($d=2$), and compare it against several SOTA baselines. These include alternative SB solvers (cite39†Gushchin et al., 2024 ; cite45†Shi et al., 2023 ; cite60†Tong et al., 2024b ; cite36†De Bortoli et al., 2021 ) and flow-based generative approaches (ODE) (cite61†Tong et al., 2024a ; cite62†Lipman et al., 2023 ; cite63†Liu, 2022 ).
L319: Each model transports $10{,}000$ samples from the source to the target distribution, and performance is assessed using the 2-Wasserstein distance.
L320: The 2-Wasserstein distance between two probability measures $q_{0}$ and $q_{1}$ on a metric space $(\mathcal{X},d)$ is defined as
L321: 
L322:  | $$\mathcal{W}_{2}(q_{0},q_{1})=\left(\inf_{\gamma\in\Gamma(q_{0},q_{1})}\int_{\mathcal{X}\times\mathcal{X}}\|x-y\|^{2}\,d\gamma(x,y)\right)^{1/2},$$  |
L323: where $\Gamma(q_{0},q_{1})$ denotes the set of all couplings of $q_{0}$ and $q_{1}$. In our experiments, we aim to minimize this distance between samples generated by the SBB model and those drawn from the ground-truth distribution. All results are averaged over five seeds, and we report both the mean and standard deviation. As shown in Table cite64†1 , the proposed SBB framework consistently achieves the lowest $\mathcal{W}_{2}$ distances across all benchmark tasks.
L324: It outperforms both SB-based methods (e.g., LightSB-M) and diffusion/flow-based baselines, yielding on average a $\sim 19\%$ improvement in transport accuracy, while reducing the variance of the results. These results highlight the efficiency and stability of SBB in modeling complex multimodal and non-Gaussian distributions such as the moons $\rightarrow$ 8-gaussians task. Note that FM is incompatible with the latter as it requires a Gaussian source distribution.
L325: Table 1: 2-Wasserstein distances ($\mathcal{W}_{2}$) on synthetic datasets (lower is better). The best results are highlighted in bold. *Indicates results taken from (cite60†Tong et al., 2024b )
L326:  | $\mathcal{W}_{2}$ ($\downarrow$)
L327: Algorithm  | $\mathcal{N}\!\rightarrow\!8\text{gaussians}$  | moons $\!\rightarrow\!8\text{gaussians}$  | $\mathcal{N}\!\rightarrow\!\text{moons}$
L328: $[\text{SF}]^{2}$M-Exact*  | 0.275$\pm$0.058  | 0.726$\pm$0.137  | 0.124$\pm$0.023
L329: $[\text{SF}]^{2}$M-I*  | 0.393$\pm$0.054  | 1.482$\pm$0.151  | 0.185$\pm$0.028
L330: DSBM-IPF*  | 0.315$\pm$0.079  | 0.812$\pm$0.092  | 0.140$\pm$0.006
L331: DSBM-IMF*  | 0.338$\pm$0.091  | 0.838$\pm$0.098  | 0.144$\pm$0.024
L332: DSB*  | 0.411$\pm$0.084  | 0.987$\pm$0.324  | 0.190$\pm$0.049
L333: LightSB-M  | 0.339$\pm$0.099  | 0.295$\pm$0.051  | 0.201$\pm$0.042
L334: SBB (ours)  | 0.241$\pm$0.083  | 0.201$\pm$0.034  | 0.109$\pm$0.014
L335: OT-CFM*  | 0.303$\pm$0.043  | 0.601$\pm$0.027  | 0.130$\pm$0.016
L336: SB-CFM*  | 2.314$\pm$2.112  | 0.843$\pm$0.079  | 0.434$\pm$0.594
L337: RF*  | 0.421$\pm$0.071  | 1.525$\pm$0.330  | 0.283$\pm$0.045
L338: I-CFM*  | 0.373$\pm$0.103  | 1.557$\pm$0.407  | 0.178$\pm$0.014
L339: FM*  | 0.343$\pm$0.058  | —  | 0.209$\pm$0.055
L340: We further analyze the influence of the parameter $\beta$ on the transport quality, ranging from $\beta=10$ up to $\beta=\infty$ that is the SB regime. Figure cite65†2 shows that $\mathcal{W}_{2}$ distances decrease rapidly as $\beta$ increases from $10$ to $100$, except for the $\mathcal{N}\!\rightarrow\!8\text{gaussians}$ that keeps increasing, with optimal performance achieved between $\beta=10$ and $100$ across both datasets.
L341: Beyond $\beta=100$, performance slightly degrades, suggesting an intermediate $\beta$ value provides the best trade-off between the drift and the volatility.
L342: cite66†Image: Refer to caption Figure 2: Evolution of the 2-Wasserstein distance $\mathcal{W}_{2}$ for different values of $\beta$ on each datasets.
L343: ## 6 Qualitative Evaluation on Unpaired Image-to-Image Translation
L344: To evaluate the generative capabilities of our model we consider the task of unpaired image‑to‑image translation (cite67†Zhu et al., 2017 ) on subsets of the FFHQ dataset at a resolution of $1024\times 1024$ pixels (cite68†Karras et al., 2019 ). The source distribution $p_{0}$ comprises adult faces, while the target distribution $p_{T}$ consists of child faces.
L345: Since the two domains are not paired, we adopt a cycle‑consistent framework in the latent space of an Adversarial Latent AutoEncoder (ALAE) (cite69†Pidhorskyi et al., 2020 ). Each image $\mathbf{x}\in\mathbb{R}^{3\times 1024\times 1024}$ is first encoded by the pretrained ALAE encoder $E:\mathbb{R}^{3\times 1024\times 1024}\rightarrow\mathbb{R}^{512}$, producing a latent code $\mathbf{z}=E(\mathbf{x})\in\mathbb{R}^{512}$.
L346: Then, we train our SBB framework in that latent space, and decode the final latent output using the pretrained ALAE decoder $D:\mathbb{R}^{512}\rightarrow\mathbb{R}^{3\times 1024\times 1024}$, yielding the translated images. This setup allows us to assess the fidelity of the generated child faces and the preservation of identity-related attributes without requiring paired supervision.
L347: Figure cite70†3 compares our SBB framework with the usual SB approach using the LightSB‑M baseline across several $(\beta,\varepsilon)$ settings. For the low‑noise regime $\varepsilon=0.1$, SBB with small $\beta$ (e.g., $\beta=1,10$ attains higher visual quality and better fidelity than LightSB‑M, as some images are clearly not of children.
L348: Moreover, when the noise level is increased to $\varepsilon=1$, where classical SB exhibits high variance, we observe that small $\beta$ values lead to greater diversity in the generated outputs. Finally, we also demonstrate that for large values of $\beta$ (i.e., $\beta=100$), the behavior closely matches that of the standard SB, in agreement with the theoretical predictions.
L349: cite71†Image: Refer to caption (a) $\varepsilon=0.1$
L350: 
L351: cite72†Image: Refer to caption (b) $\varepsilon=1$
L352: 
L353: Figure 3: Comparison between our framework SBB and the benchmark LightSB-M. The left column shows the input image.
L354: We then propose the experiment illustrated in Figure cite73†4 , which generates a child image directly from noise. Unlike conventional diffusion models that rely on a backward–forward sampling (cite74†Song and Ermon, 2019 ; cite75†Song et al., 2021 ) scheme, our approach proceeds in a single forward pass, thereby avoiding the costly reverse diffusion step and error accumulation.
L355: We also present the comparison between the $Y$ and $X$ process, where we observe that the inverse sample $X_{T}$ significantly improves sample quality and corrects potential errors of $Y_{T}$. This improvement is evident both in terms of visual fidelity and distributional alignment, as $Y_{T}$ does not always give child images.
L356: cite76†Image: Refer to caption (a) $Y_{T}$
L357: 
L358: cite77†Image: Refer to caption (b) $X_{T}$
L359: 
L360: Figure 4: Comparison between $Y_{T}$ and $X_{T}$ (right) with $\beta=5$. The left column shows the input image, and three representative samples are reported for each method.
L361: Finally, Figure cite78†5 depicts the complete pipeline from the source distribution $X_{0}\sim p_{0}$ to the target distribution $X_{1}\sim p_{1}$ together with the underlying $Y$‑process defined by our framework. The intermediate states $Y_{t}$ are obtained via bridge matching Equation (cite52†10 ) between the endpoints $Y_{0}$ and $Y_{T}$. Note that this bridging occurs on the $Y$ process, not on $X$, since $Y$ is a SB
L362: cite79†Image: Refer to caption Figure 5: Trajectory from $X_{0}\sim p_{0}$ to $X_{1}\sim p_{1}$ with the underlying $Y$ process.
L363: ## 7 Conclusion
L364: Potential impact. Our primary contribution is an algorithm that solves the SBB problem for generative modeling. Building on existing methods for the classical SB, we derive an efficient procedure to compute the optimal transport plan $\mathbb{P}^{SBB}$. The framework includes a tunable parameter $\beta$ that balances drift and volatility; we empirically demonstrate how $\beta$ impacts the sample diversity and fidelity.
L365: By incorporating stochastic volatility, the method can accommodate a broader class of target distributions—including those with heavy tails—beyond the restrictive assumptions of the standard SB. Consequently, the generated synthetic data exhibit greater variability while maintaining high fidelity as governed by $\beta$.
L366: Limitations and future work. Computing $\mathbb{P}^{SBB}$ requires iterating over the transport map, which can be computationally demanding. In our experiments we limited the iteration count to $K=5$ as it seems to converge, yet the algorithm’s convergence has not been formally established.
L367: Future research should (i) develop tighter iteration‑complexity bounds, (ii) provide a rigorous convergence proof, and (iii) explore acceleration techniques (e.g., stochastic approximations or multigrid schemes) to reduce the number of required iterations. A natural extension of the method is to apply the SBB framework to time‑series data.
L368: While the SB problem has already been employed for sequential data (cite80†Hamdouche et al., 2023 ; cite81†Alouadi et al., 2025 ), the stochastic‑volatility extension proposed here has not. Incorporating the controlled volatility could markedly improve the realism of generated time series, particularly in financial domains where heteroskedasticity is prevalent.
L493: ## Appendix B Experimental Setup
L494: 
L495: All experiments were conducted using a single NVIDIA A100 SXM4 40 GB GPU. The parameters used throughout this study, unless otherwise stated, are summarized in Table cite116†2 .
L496: 
L497: Table 2: Table of parameters and their values
L498: $K$  | $T$  | $\tilde{T}$  | $n_{epoch}$  | Batch Size  | $lr$
L499: --- | --- | --- | --- | --- | ---
L500: $5$  | $1$  | $0.99$  | $15000$  | $512$  | $10^{-3}$
L501: Under this setup, training completes in under $10$ minutes for $2$-d tasks, and inference is inexpensive (less than $1$ minutes for $10{,}000$ samples). For image translation, the computational cost of LightSBB-M is comparable to that of LightSB-M, as the additional overhead arises only from the outer-loop iterations ($K=5$), which we found to be negligible relative to the cost of training the score network.
L502: ### B.1 Model Architecture
L503: The transport map ${\cal Z}_{\theta}$ is defined by a simple multilayer perceptron (MLP). The network takes as input the time $t\in\mathbb{R}$ and the state $x\in\mathbb{R}^{d}$. Each input is first processed by a feed-forward network (FFN) comprising a linear layer, a normalization layer, a GELU activation function, and a final linear layer. This projects the inputs into latent spaces of dimension $t_{\text{model}}$ and $d_{\text{model}}$, respectively.
L504: The resulting embeddings are then concatenated and passed through a subsequent FFN with a similar structure, which maps the combined representation back to the original space $\mathbb{R}^{d}$.
L505: ### B.2 Quantitative Evaluation Setup
L506: For these experiments, we set the model hyperparameters to $t_{\text{model}}=8$ and $d_{\text{model}}=32$ with $J=50$ potentials in the Gaussian mixture. To remain consistent with the setup in (cite60†Tong et al., 2024b ), we use $\varepsilon=1$ for all datasets, except for moons $\!\rightarrow\!8$ gaussians, where we set $\varepsilon=5$. Moreover, we use $K=25$ iterations for the $\mathcal{N}\!\rightarrow\!\text{moons}$ dataset, as this setting provides more stable and consistent results.
L507: Table cite117†3 reports the 2-Wasserstein distances ($\mathcal{W}_{2}$) obtained for varying values of $\beta$ across all considered datasets.
L508: Table 3: 2-Wasserstein distances ($\mathcal{W}_{2}$) on synthetic datasets (lower is better) for different $\beta$ values. The best results are highlighted in bold.
L509:  | $\mathcal{W}_{2}$ ($\downarrow$)
L510: --- | ---
L511: $\beta$  | $\mathcal{N}\!\rightarrow\!8\text{gaussians}$  | moons $\!\rightarrow\!8\text{gaussians}$  | $\mathcal{N}\!\rightarrow\!\text{moons}$
L512: --- | --- | --- | ---
L513: 1  | 4.103$\pm$1.247  | 2.312$\pm$1.089  | 0.927$\pm$0.743
L514: 10  | 0.241$\pm$0.083  | 0.603$\pm$0.048  | 0.372$\pm$0.032
L515: 50  | 0.277$\pm$0.096  | 0.243$\pm$0.029  | 0.152$\pm$0.024
L516: 100  | 0.330$\pm$0.077  | 0.201$\pm$0.034  | 0.109$\pm$0.014
L517: 1000  | 0.462$\pm$0.091  | 0.232$\pm$0.025  | 0.171$\pm$0.037
L518: $\infty$  | 0.489$\pm$0.084  | 0.334$\pm$0.058  | 0.229$\pm$0.019
L519: Figure cite118†8 visualizes the transport results for all $\beta$ values. In each subplot, the initial distribution $\mu_{0}$ is shown in blue, and the transported distribution $\mu_{T}$ is shown in orange. For the smallest tested value, $\beta=1$, the algorithm fails to converge. This behavior can be attributed to the violation of the required condition $\beta>\frac{1}{T}$, which is not satisfied when $T=1$.
L520: 
L521: cite119†Image: Refer to caption (a) $\mathcal{N}\!\rightarrow\!\text{moons}$
L522: cite120†Image: Refer to caption (b) moons $\!\rightarrow\!8\text{gaussians}$
L523: 
L524: cite121†Image: Refer to caption (c) $\mathcal{N}\!\rightarrow\!8\text{gaussians}$
L525: 
L526: Figure 8: Transport results across datasets for different $\beta$ values. Initial distributions $\mu_{0}$ are shown in blue, and transported distributions $\mu_{T}$ in orange.
L527: ### B.3 Unpaired Image-to-Image Translation Setup
L528: For unpaired image-to-image translation, we closely follow the experimental setup in (cite39†Gushchin et al., 2024 ). The dataset consists of $70,000$ labeled images, of which $60,000$ were used for training and $10,000$ for testing. The model hyperparameters were set to $t_{\text{model}}=32$ and $d_{\text{model}}=128$, with $J=10$ potentials in the Gaussian mixture. This results in a drift model with approximately $2.6$ million parameters, and a transport map estimator with $100,000$ parameters.
L529: Training took under 5 minutes, and inference on 10 input images required less than 1 minute.
L530: Our implementation builds upon the code provided by (cite39†Gushchin et al., 2024 ), available at: cite122†https://github.com/SKholkin/LightSB-Matching/tree/main†github.com . Figure cite123†9 provides additional examples of our method, showing both $X_{T}$ and $Y_{T}$ for $\beta=1$ and $\varepsilon\in\{0.1,1\}$, with LightSB-M used as the baseline for comparison.

