# 既有有限线索第二小批准入

独立校准更新：jan01_v3实际完整AB与SESS决定性method校准，ELO/e5/SESS准入通过，DeployMaster贡献前关闭；ABC原方法已实际恢复如下，不提前授Evidence。

## ABC决定准入的原方法

原入口 https://arxiv.org/html/2601.03895v1 ，§4.1–4.2 L110–135，本次仅定点恢复必要原式，没有重读全部附件。Table1按估计优势正负与r相对1分四quadrants；L123–124 Eq5原式：

\[
\tilde r=\begin{cases}\mathrm{clip}(r,1-\varepsilon_2,1+\varepsilon_1),&\hat A>0\\\mathrm{clip}(r,1-\varepsilon_4,1+\varepsilon_3),&\hat A\le0.\end{cases}
\]

L130 Eq6直接最大化组/序列/token平均的 \(\tilde r\hat A\)，没有原PPO的两项min；L132明确r是current/old逐token概率比、优势仍序列级。L126原句：“does not resolve the fundamental granularity limitation of sequence-level advantages”。这是四边界局部损失替代，不是识别真实token-credit或硬约束实际policy ratio；L140称不依赖sign与Eq5的sign分支矛盾只留必要边界，未据此否全部实验。

完整exact-v1题摘及版本history已实际读，保ABSTRACTS_4_RAW.txt；不把50000部署/6.46×等headline准入，不把现v2标题倒推v1。日期另核，待root独立准入校准；下述不是Evidence/Books完成。

- ELO03648：冻结PEFT仍要完整forward→把首尾层摘出先训、再装回原模型作短full alignment→具体区别训练参数节约与forward执行路径节约、重接兼容成本。潜在2+2+2=6，不因多语种领域或sourceEnglish保持数字准入，需核detach目标/对齐预算及旧模型退化边界。
- e5-omni03666：预训练implicit sharedspace不等同logit一致/negative有效/geometry一致→modality temperatures、mixed-negative hardness/false-negative课程、whitening/cov约束对三种明确失配→跨模态检索质量须分别校准尺度与训练支持。潜在2+2+2=6，原三问题条件而非三个成熟模块数/owner映射计分；必要core限具体新增耦合及反侧。
- SESS03493：AB未明确新目标，定点§3.1–3.3实际读后：静态同pool/sameOPRO，只更换feedback subset；facility-location/least-confidence/weighted-rep是成熟算子，但比较目标不是保存benchmark模型排序而是选择对搜索反馈有用的人口，且权重为固定scorer的confidence。此局部对照可核选择目标错配，潜在2+1+2=5，不把(1−1/e)借作新长期理论；不授prompt优化质量、动态scorer或全局最佳subset。必要原式下附供校准，非完整标准Evidence。
- ABCGRPO03895：AB仅asymmetric/adaptive尚含糊，定点§4.1–4.2/L110–135实际核：positive/negative优势分别四边界，clip ratio再乘优势而不保原min，新增控制的也是低于lower的positive/超过upper的negative两quadrants。具体局部损失替代潜在2+1+2=5，不授真实policy ratio硬限/正确token-credit/entropy普遍保持；Eq/Table sign-dependent措辞待后续必要核，原score不靠理论保证抬高。
- DeployMaster03513：完整AB90+领域SciencePedia/AI4S工具资产发现→license/quality筛选→buildspec→container→minimalcommand验证→注册，未提出模型系统的新执行协议/编译正确性条件；50000规模trace只是称failure/cost surfaces未具体新边界。提案范围/贡献前关闭：AIforScience平台为ROADMAP暂缓范围且无独立主线机制增量，非仅“科学”一词/软件类别拒绝，不把一般Agent/infra类比重新引入、不追日期、不评分。

## SESS决定准入的原始method（非全附件）
L64: ## 3 Methodology
L65: ### 3.1 Evaluation subset selection
L66: 
L67: Let $D=\{x_{1},\dots,x_{N}\}$ be a pool of candidate evaluation examples. Automatic prompt optimization such as OPRO iteratively proposes prompts and keeps those that score well on an evaluation set. Since scoring each prompt on the full pool $D$ is often infeasible, we select a budgeted subset $S\subseteq D$ with $|S|\leq k$ to serve as the optimization feedback.
L68: 
L69: We frame evaluation subset selection as the following budgeted set maximization problem:
L70:  | $$S^{*}\in\arg\max_{S\subseteq D,\;|S|\leq k}\mathcal{F}(S),$$  |  | (1)
L71: where $\mathcal{F}:2^{D}\to\mathbb{R}_{\geq 0}$ measures how suitable $S$ is for guiding prompt optimization. Exact maximization is NP-hard for many natural choices of $\mathcal{F}$, but when $\mathcal{F}$ is non-negative, monotone, and submodular cite49†Fujishige (2005) , the greedy algorithm achieves a $(1-1/e)$ approximation under the cardinality constraint cite50†Nemhauser et al. (1978) .
L72: Our goal is therefore to design useful evaluation objectives $\mathcal{F}$ that match the needs of prompt optimization and belong to this monotone submodular family. We solve Eq. cite51†1 once prior to optimization (static selection). We hypothesize that optimization feedback is primarily determined by intrinsic instance properties (e.g., representativeness or difficulty), allowing a fixed subset to provide a stable and efficient signal without the overhead of dynamic re-selection.
L73: ### 3.2 Submodular Evaluation Objectives
L74: 
L75: We consider two goals for evaluation subsets: (1) representativeness: cover the diversity of the pool so the feedback reflects the full task distribution; (2) difficulty awareness: emphasize examples that the scorer model finds hard, since these are often the most informative for comparing prompts. We propose three subset selection objectives: representative, least confident, and confidence-weighted representative.
L76: In the remainder of the paper, we refer to the greedy solution of each objective as a specific instance of SESS: SESS-rep for the representative objective $\mathcal{F}_{\mathrm{rep}}$, SESS-lc for least-confidence selection using likelihood-based confidence, SESS-vlc for least-confidence selection using verbalized confidence, both described by $\mathcal{F}_{\mathrm{lc}}$, and SESS-wrep for the confidence-weighted representative objective $\mathcal{F}_{\mathrm{wrep}}$.
L77: Each method selects a subset $S$ of size $k$ using the greedy procedure described in Section cite15†3.3 .
L78: #### Representative subset.
L79: 
L80: We cast each example into a vector representation and define $\mathrm{sim}(i,j)$ by cosine similarity. To satisfy the non-negativity assumptions required by our analysis, we normalize cosine similarity as $\mathrm{sim}(i,j)=(1+\cos(i,j))/2\in[0,1]$. We then use a facility-location style objective to quantify how well a subset $S$ covers the full pool:
L81: 
L82:  | $$\mathcal{F}_{\mathrm{rep}}(S)\;:=\;\sum_{j\in D}\max_{i\in S}\mathrm{sim}(i,j).$$  |  | (2)
L83: Intuitively, each example $j$ contributes its similarity to its nearest neighbor in the selected subset $S$, so larger $\mathcal{F}_{\mathrm{rep}}(S)$ indicates that $S$ contains good representatives for many regions of the pool. Under $\mathrm{sim}\geq 0$, $\mathcal{F}_{\mathrm{rep}}$ is monotone and submodular cite52†Iyer and Bilmes (2013) . Proofs are provided in Appendix cite28†C .
L84: #### Least confident subset.
L85: 
L86: Let $c(j)$ be a scalar confidence score for example $j$ computed by a fixed scorer model. We select the $k$ examples with smallest $c(j)$. This can be written as a modular objective
L87: 
L88:  | $$\mathcal{F}_{\mathrm{lc}}(S)\;:=\;\sum_{j\in S}(1-\tilde{c}(j)),$$  |  | (3)
L89: where $\tilde{c}(j)\in[0,1]$ is a normalized confidence score of $c(j)$. We provide two variants: likelihood-based confidence and verbal confidence cite53†Tian et al. (2023) . These objectives capture difficulty but could cause redundancy among selected examples. Because the objective is modular and nonnegative, it is monotone and submodular.
L90: #### Confidence-weighted representative subset.
L91: 
L92: To combine representativeness and difficulty awareness, we weight coverage to favor hard examples:
L93: 
L94:  | $$\mathcal{F}_{\mathrm{wrep}}(S)\;:=\;\sum_{j\in D}w(j)\cdot\max_{i\in S}\mathrm{sim}(i,j),$$  |  | (4)
L95: 
L96: where $w(j)\geq 0$ is an importance weight computed from the scorer model’s likelihood-based confidence. In our implementation,
L97: 
L98:  | $$w(j)\;=\;(1-\lambda)\;+\;\lambda\cdot\bigl(1-\tilde{c}(j)\bigr),\ \lambda\in[0,1],$$  |  | (5)
L99: so $\lambda=0$ gives us $\mathcal{F}_{\mathrm{rep}}(S)$ which recovers pure representativeness, while larger $\lambda$ increasingly concentrates coverage on low-confidence (hard) examples. Since $\mathcal{F}_{\mathrm{wrep}}$ is a nonnegative weighted sum of facility-location terms, it remains monotone submodular when $\mathrm{sim}\geq 0$ and $w(j)\geq 0$; we prove this in Appendix cite28†C .
L100: ### 3.3 Greedy selection
L101: 
L102: For any monotone submodular objective $\mathcal{F}$ above (in particular $\mathcal{F}_{\mathrm{rep}}$ and $\mathcal{F}_{\mathrm{wrep}}$), we apply the standard greedy algorithm starting from $S=\emptyset$:
L103: 
L104:  | $$x^{*}\leftarrow\arg\max_{x\in D\setminus S}\left[\mathcal{F}(S\cup\{x\})-\mathcal{F}(S)\right],$$  |  | (6)
L105: followed by the update $S\leftarrow S\cup\{x^{*}\}$, repeated until $|S|=k$. For monotone submodular $\mathcal{F}$ under the cardinality constraint, the resulting subset $S_{\mathrm{greedy}}$ enjoys the guarantee
L106: 
L107:  | $$\mathcal{F}(S_{\mathrm{greedy}})\;\geq\;(1-1/e)\,\mathcal{F}(S^{*})$$  |
L108: where $S^{*}$ is an optimal solution to Eq. (cite51†1 ) cite50†Nemhauser et al. (1978) . For modular objectives such as $\mathcal{F}_{\mathrm{lc}}$, $S_{\mathrm{greedy}}$ is obtained by sorting examples by uncertainty $(1-\tilde{c}(j))$ in descending order and selecting the top-$k$.
