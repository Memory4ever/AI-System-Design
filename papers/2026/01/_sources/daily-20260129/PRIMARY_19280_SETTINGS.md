# GDRO exact v1 required setup

Raw primary response; Appendix A only supplies necessary budget/precision conditions. Supporting broad theoretical appendix is not adopted.

Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning (https://arxiv.org/html/2601.19280v1)
citeturn28426view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19280v1","pattern":"## Appendix A"}); Total lines: 1191
L604:   * Wang et al. (2025) S. Wang, L. Yu, C. Gao, C. Zheng, S. Liu, R. Lu, K. Dang, X. Chen, J. Yang, Z. Zhang, Y. Liu, A. Yang, A. Zhao, Y. Yue, S. Song, B. Yu, G. Huang, and J. Lin Beyond the 80/20 rule: high-entropy minority tokens drive effective reinforcement learning for LLM reasoning. External Links: cite302†Document†dx.doi.org , 2506.01939, cite303†Link Cited by: cite216†§1 , cite221†§6.1 , cite213†§6.4 .
L605:   * Wen et al. (2025a) L. Wen, Y. Cai, F. Xiao, X. He, Q. An, Z. Duan, Y. Du, J. Liu, L. Tang, X. Lv, H. Zou, Y. Deng, S. Jia, and X. Zhang Light-r1: curriculum SFT, DPO and RL for long COT from scratch and beyond. External Links: cite304†Document†dx.doi.org , 2503.10460, cite305†Link Cited by: cite222†§6.4 .
L606:   * Wen et al. (2025b) X. Wen, Z. Liu, S. Zheng, Z. Xu, S. Ye, Z. Wu, X. Liang, Y. Wang, J. Li, Z. Miao, J. Bian, and M. Yang Reinforcement learning with verifiable rewards implicitly incentivizes correct reasoning in base LLMs. External Links: cite306†Document†dx.doi.org , 2506.14245, cite307†Link Cited by: cite221†§6.1 , cite213†§6.4 .
L607:   * Xie et al. (2024) Y. Xie, A. Goyal, W. Zheng, M. Kan, T. P. Lillicrap, K. Kawaguchi, and M. Shieh Monte carlo tree search boosts reasoning via iterative preference learning. External Links: cite308†Document†dx.doi.org , 2405.00451, cite309†Link Cited by: cite222†§6.4 .
L608:   * Xu and Mannor (2012) H. Xu and S. Mannor Distributionally robust markov decision processes. Mathematics of Operations Research 37 (2), pp. 288–300. External Links: cite310†Document†dx.doi.org , cite311†Link†cris.technion.ac.il Cited by: cite234†§6.3 .
L609:   * Yuan et al. (2024) W. Yuan, R. Y. Pang, K. Cho, X. Li, S. Sukhbaatar, J. Xu, and J. Weston Self-rewarding language models. External Links: cite312†Document†dx.doi.org , 2401.10020, cite313†Link Cited by: cite240†§7 .
L610:   * Zelikman et al. (2024) E. Zelikman, G. Harik, Y. Shao, V. Jayasiri, N. Haber, and N. D. Goodman Quiet-STaR: language models can teach themselves to think before speaking. External Links: cite314†Document†dx.doi.org , 2403.09629, cite315†Link Cited by: cite240†§7 .
L611:   * Zelikman et al. (2022) E. Zelikman, Y. Wu, J. Mu, and N. D. Goodman STaR: bootstrapping reasoning with reasoning. External Links: cite316†Document†dx.doi.org , 2203.14465, cite317†Link Cited by: cite240†§7 .
L612: ## Appendix A Experiment Details
L613: 
L614: In this section, we detail the experimental setup, including the shared optimization hyperparameters and the specific configurations for our adversarial mechanisms. All experiments were conducted using the Qwen3-Base model family (1.7B, 4B, 8B) using BFloat16 (BF16) mixed precision and FlashAttention 2. The code and configuration files used to reproduce these results are available at cite318†https://github.com/kishanpb/verl-gdro†github.com .
L615: ### A.1 Shared Training Hyperparameters
L616: 
L617: All methods (GRPO Baseline, Prompt-GDRO, and Rollout-GDRO) utilize a common post-training foundation based on the Group Relative Policy Optimization (GRPO) objective.
L618: #### A.1.1 Optimization & Architecture
L619: 
L620:   * •
L621: 
L622: Global Train Batch Size: 256
L623: 
L624:   * •
L625: 
L626: Global Validation Batch Size: 128
L627: 
L628:   * •
L629: 
L630: Total Training Steps: 1000
L631: 
L632:   * •
L633: 
L634: Optimizer: AdamW
L635: 
L636:   * •
L637: 
L638: Actor Learning Rate: $1\times 10^{-6}$
L639: 
L640:   * •
L641: 
L642: KL Penalty Coefficient ($\beta_{\text{KL}}$): 0.001
L643: 
L644:   * •
L645: 
L646: PPO Clip Range: $[1-\epsilon_{\text{low}},1+\epsilon_{\text{high}}]$ where $\epsilon_{\text{low}}=0.2$, $\epsilon_{\text{high}}=0.28$
L647: 
L648:   * •
L649: 
L650: Advantage Normalization: Yes (Normalized by group standard deviation)
L651:   * •
L652: 
L653: Advantage Clipping: $[-5,5]$
L654: #### A.1.2 Rollout Generation
L655: 
L656:   * •
L657: 
L658: Inference Engine: vLLM
L659: 
L660:   * •
L661: 
L662: Training Rollouts per Prompt ($G$): 4 (Base setting)
L663: 
L664:   * •
L665: 
L666: Validation Rollouts per Prompt: 8
L667: 
L668:   * •
L669: 
L670: Sampling Temperature: 0.6 (Training)
L671: 
L672:   * •
L673: 
L674: Top-p: 0.8
L675: 
L676:   * •
L677: 
L678: Top-k: 20
L679: 
L680:   * •
L681: 
L682: Reward: Verifiable math correctness with $r(x,y)\in\{-1,+1\}\subset[-1,1]$, implemented via the math/math-dapo modules in verl.
L683: ### A.2 Adversarial Configuration
L684: 
L685: Our Multi-Adversary framework introduces specific hyperparameters for the EXP3P algorithms governing data sampling and compute allocation.
L686: #### A.2.1 Prompt-GDRO (The Data Adversary)
L687: 
L688: This mechanism reweights the prompt distribution based on the intensive difficulty of online groups.
L689: 
L690:   * •
L691: 
L692: Grouping Mechanism: Online Pass@k (10 bins)
L693: 
L694:   * •
L695: 
L696: Adversary Algorithm: EMA-Debiased GDRO-EXP3P
L697: 
L698:   * •
L699: 
L700: Adversary Learning Rate ($\eta_{q}$): 0.65
L701: 
L702:   * •
L703: 
L704: Exploration Rate ($\gamma$): 0.01
L705: 
L706:   * •
L707: 
L708: Score EMA Decay ($\beta$): 0.12
L709: 
L710:   * •
L711: 
L712: Max Class Weight Cap: 15.0
L713: 
L714:   * •
L715: 
L716: Loss Normalization: Normalized by class share (to prevent frequency bias)
L717: #### A.2.2 Rollout-GDRO (The Compute Adversary)
L718: 
L719: This mechanism allocates discrete rollout counts $n_{b}$ to minimize gradient variance under a global budget constraint.
L720: 
L721:   * •
L722: 
L723: Grouping Mechanism: Online Pass@k (10 bins, edges at $0.1,0.2,\dots,0.9$)
L724: 
L725:   * •
L726: 
L727: Rollout Arm Range: $n\in[n_{\min},n_{\max}]$ where $n_{\min}=2,n_{\max}=12$ (Multiplier $3.0\times$ base)
L728: 
L729:   * •
L730: 
L731: Global Budget Constraint ($\bar{n}$): 4 rollouts (average per prompt)
L732: 
L733:   * •
L734: 
L735: Dual Learning Rate ($\alpha_{\mu}$): 0.05
L736: 
L737:   * •
L738: Arm Learning Rate ($\eta$): 0.65
L739: 
L740:   * •
L741: 
L742: Arm Exploration Rate ($\gamma$): 0.01
L743: 
L744:   * •
L745: 
L746: Arm Score EMA Decay: 0.4
L747: 
L748:   * •
L749: 
L750: Budget Matching: Exact constrained selection via Dynamic Programming
L751: ## Appendix B Main Theoretical Results: A Game-and-Variance View
L752: This section develops a unified theoretical lens for the two adversarial controllers in our framework: (i) Prompt-GDRO, which adaptively reshapes the prompt distribution to emphasize difficult bins, and (ii) Rollout-GDRO, which adaptively reallocates rollouts across bins to reduce estimation noise under a compute budget.
L753: Our goal is not to provide deep-network convergence guarantees for GRPO, but rather to (a) formalize the surrogate objectives implicitly optimized by these controllers, and (b) connect their update rules to standard no-regret / mirror-descent analyses that explain the qualitative behaviors observed empirically (e.g., “traveling waves” and staircase compute allocation).
L754: A condensed statement of these results (omitting most proofs) appears in Section cite20†4 ; this appendix provides complete statements and proofs for reference.
L755: 
L756: Throughout, we adopt the GDRO formulation from cite7†Section 2 (Eq. (cite109†9 )). Let $g(x)\in\{1,\dots,B\}$ be the (online) grouping rule from cite20†Section 4 , and define the group losses below. We use $\{L_{b}\}_{b=1}^{B}$ primarily in the Prompt-GDRO analysis; Rollout-GDRO instead optimizes a separate budgeted variance objective.
L757:  | $$L_{b}(\theta)\;\triangleq\;\mathbb{E}\!\left[\ell(x;\theta)\mid g(x)=b\right],\qquad b\in\{1,\dots,B\},$$  |  | (34)
L758: 
L759: where $\ell(x;\theta)$ is the prompt-level GRPO loss from cite9†Section 2.2 .^{3}^{3} 3 In reward maximization form, one may take $L_{b}(\theta)=-J_{b}(\theta)$, where $J_{b}$ is the group-conditional expected reward (this sign convention is standard in RL; see, e.g., cite319†Agarwal et al., 2019 ).
L760: ### B.1 Prompt-GDRO as Entropic GDRO and No-Regret Game Dynamics
L761: 
L762: We start from the canonical finite-group robust objective
L763: 
L764:  | $$\min_{\theta}\;\max_{q\in\Delta_{B}}\;f(\theta,q),\qquad f(\theta,q)\;\triangleq\;\sum_{b=1}^{B}q(b)\,L_{b}(\theta),$$  |  | (35)
L765: 
L766: where $\Delta_{B}$ is the probability simplex over $B$ groups. The inner maximization selects a worst-case mixture of groups, while the outer minimization trains a policy robust to this mixture.
