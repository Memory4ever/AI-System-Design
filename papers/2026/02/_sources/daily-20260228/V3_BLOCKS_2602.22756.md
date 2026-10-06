[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Dynamic Hierarchical Birkhoff-von Neumann Decomposition for All-to-All GPU Communication

[3] h6: Abstract

[4] p: All-to-all GPU communication is a critical bottleneck in large-scale training clusters, where completion time is constrained by per-port bandwidth and can be severely impacted by traffic skew across GPUs and network interface cards (NICs). This issue is amplified by the two-tier structure of modern GPU systems, which combine fast intra-server links with much slower inter-server networks. Motivated by recent system observations that highlight the importance of traffic reshaping and hierarchy awareness, we study all-to-all scheduling from an online switching and queueing-theoretic perspective.

[5] p: We propose a dynamic hierarchical Birkhoff–von Neumann (BvN) decomposition framework tailored to two-tier GPU fabrics. At each frame boundary, traffic is first balanced within each server using simple local operations to mitigate micro-level GPU/NIC skew while preserving aggregate server-to-server demand. A hierarchical BvN decomposition is then applied at the server level and refined into GPU-level matchings, significantly reducing decomposition complexity relative to a flat GPU-level approach. By integrating this construction with the dynamic frame sizing (DFS) principle, we obtain an online scheduler with provable stability under admissible Poisson arrivals. Simulations demonstrate substantial reductions in mean frame length, particularly under server-localized hotspot traffic.

[6] h6: Index Terms:

[7] h2: I Introduction

[8] p: Large-scale machine learning training increasingly relies on multi-GPU, multi-server clusters, where communication , rather than computation, often dominates the end-to-end iteration time. In particular, modern workloads such as mixture-of-experts (MoE) models and large-scale recommendation systems repeatedly invoke all-to-all collectives (e.g., alltoallv ), making overall performance highly sensitive to traffic skew, per-port contention, and load imbalance across GPUs and network interface cards (NICs) [ 1 , 2 ] .

[9] p: A key challenge stems from the inherently two-tier structure of modern GPU clusters. GPUs within the same server are interconnected by high-bandwidth scale-up fabrics such as NVLink or NVSwitch, whereas inter-server communication relies on significantly slower scale-out networks such as InfiniBand or Ethernet. This disparity is substantial in current platforms—for example, NVIDIA reports up to 3.6 ​ TB / s 3.6~\mathrm{TB/s} bidirectional NVLink bandwidth per GPU, whereas a ConnectX-9 SuperNIC supports up to 800 ​ Gb / s 800~\mathrm{Gb/s} per-port networking—making the scale-out tier a persistent bottleneck under skewed all-to-all traffic [ 3 , 4 ] . As a result, micro-level imbalance across GPUs or NICs can create stragglers that dominate completion time and waste available bandwidth on the bottleneck tier.

[10] p: Motivated by this phenomenon, recent systems work has emphasized the importance of structure-aware scheduling and traffic reshaping for GPU clusters. Chronos advocates prescheduled circuit switching to reduce contention during large language model (LLM) training [ 5 ] . FAST demonstrates that reshaping traffic over fast intra-server links can mitigate skew before scheduling the inter-server fabric [ 6 ] . Optimized collective libraries such as NCCL provide highly tuned implementations of collectives in practice [ 7 ] , while topology-aware synthesis frameworks such as TACCL [ 8 ] and traffic-engineering-based formulations such as TE-CCL [ 9 ] further highlight the benefits of exploiting hierarchy and structure in collective communication. Complementary system mechanisms, such as compiler-driven overlap of communication with computation [ 10 ] , hierarchical MoE communication primitives [ 11 ] , generic communication schedulers [ 12 ] , in-network acceleration [ 13 ] , and multi-NIC assistance via intra-server relaying [ 14 ] , collectively establish why traffic reshaping and hierarchy matter in practice. However, these approaches largely rely on offline planning, heuristics, or implementation-level optimizations, and typically do not provide an online , analytically tractable scheduling framework with explicit per-port constraints and queueing-theoretic guarantees.

[11] p: In this paper, we adopt a complementary perspective grounded in classical switching and queueing theory. We seek an online scheduling framework for all-to-all GPU communication that (i) explicitly respects per-port matching constraints, (ii) exploits the server/GPU hierarchy inherent in two-tier clusters, and (iii) provides provable stability guarantees under stochastic traffic. To this end, we revisit the classical Birkhoff–von Neumann (BvN) decomposition framework [ 15 , 16 ] , which represents a traffic matrix as a sequence of conflict-free matchings. From a scheduling viewpoint, each (sub)permutation matrix specifies a stage in which every sender and receiver participates in at most one transfer, naturally capturing per-port constraints. BvN-type scheduling has also been widely used in switching systems and traffic matrix decomposition, including input-buffered crossbar scheduling and guaranteed-rate services [ 17 , 18 ] .

[12] p: Despite its appealing structure, directly applying BvN decomposition at the GPU granularity in large clusters faces two fundamental limitations. First, decomposing an m ​ n × m ​ n mn\times mn traffic matrix (with n n servers and m m GPUs per server) can be computationally expensive and difficult to implement online. Second, micro-level traffic skew within a server pair—precisely the phenomenon observed in practice—can significantly inflate the number of required matchings, inducing stragglers on the scale-out tier even when server-level traffic is balanced.

[13] p: To overcome these limitations, we develop a dynamic hierarchical Birkhoff–von Neumann decomposition tailored to two-tier GPU fabrics. At each frame boundary, we first exploit the high-bandwidth intra-server network to balance traffic across GPUs and NICs within each server, mitigating micro-level skew while preserving the aggregate server-to-server demand. This balancing step formalizes, in an analytically controlled manner, the traffic reshaping intuition that underlies many recent system designs [ 6 , 14 ] . We then perform a hierarchical BvN decomposition that operates primarily at the server level and refines server-pair matchings into GPU-level matchings, substantially reducing decomposition complexity compared to a flat GPU-level approach.

[14] p: Finally, to support stochastic arrivals and online operation, we integrate the balanced hierarchical decomposition with the dynamic frame sizing (DFS) principle [ 19 , 20 , 21 ] . DFS has been successfully used to stabilize crossbar switches and related systems under stochastic traffic [ 19 , 20 ] , and here it enables an online scheduler whose backlog evolution decouples cleanly across frames. This integration yields queueing-theoretic stability guarantees expressed in terms of server-level aggregate loads, while retaining sensitivity to micro-level imbalance through the balancing step.

[15] p: In summary, this paper bridges the gap between system-level observations about traffic skew in GPU clusters and a principled scheduling framework with rigorous guarantees. The main contributions are as follows:

[16] p: We develop a hierarchical BvN decomposition for ( m , n ) (m,n) -block traffic matrices that exploits server-level structure to reduce decomposition complexity.

[17] p: We design a simple, constructive intra-server traffic balancing algorithm that mitigates GPU/NIC stragglers while preserving aggregate server-to-server demand.

[18] p: We build a DFS-based online scheduler on top of the balanced hierarchical decomposition and establish queue stability under admissible Poisson arrivals.

[19] p: Through simulation, we show that intra-server balancing substantially reduces the mean frame length, with particularly pronounced gains under server-localized hotspots and non-uniform per-GPU traffic.

[20] p: This paper is organized as follows. In Section II , we introduce the two-tier GPU communication model, formulate the all-to-all scheduling problem under per-port matching constraints, and derive a fundamental completion-time lower bound. Section III develops the hierarchical Birkhoff–von Neumann decomposition for ( m , n ) (m,n) -block traffic matrices, which forms the structural core of our scheduling framework. Section IV presents the intra-server traffic balancing algorithm and establishes its correctness and termination properties. In Section V , we integrate the balanced hierarchical decomposition with the dynamic frame sizing principle and provide queueing-theoretic stability analysis under stochastic arrivals. Section VI reports simulation results under both uniform and server-localized hotspot traffic models. Finally, Section VII concludes the paper and discusses directions for future research.

[21] h2: II System Model

[22] p: We consider an all-to-all GPU communication model as in [ 5 , 6 ] . There are n n servers, each equipped with m m GPUs and m m network interface cards (NICs), for a total of m ​ n mn GPUs and m ​ n mn NICs. Each GPU is connected to a dedicated NIC whose ingress and egress bandwidths are both B 2 B_{2} .

[23] p: The m ​ n mn NICs are interconnected by an m ​ n × m ​ n mn\times mn nonblocking crossbar switch, which can realize any permutation matrix without conflict. We index GPUs by ( i , ℓ ) (i,\ell) , where i ∈ { 1 , … , n } i\in\{1,\ldots,n\} denotes the server index and ℓ ∈ { 1 , … , m } \ell\in\{1,\ldots,m\} denotes the GPU index within a server. Let T ( i , ℓ ) → ( j , k ) T_{(i,\ell)\to(j,k)} denote the amount of data transmitted from GPU ( i , ℓ ) (i,\ell) to GPU ( j , k ) (j,k) . We exclude self-traffic, i.e., T ( i , ℓ ) → ( i , ℓ ) = 0 T_{(i,\ell)\to(i,\ell)}=0 for all ( i , ℓ ) (i,\ell) .

[24] p: The objective is to find a transmission schedule that minimizes the completion time T min T^{\min} , defined as the time required for all GPUs to complete their data transfers. Define the total outgoing traffic from GPU ( i , ℓ ) (i,\ell) as

[25] table: T ( i , ℓ ) out ≜ ∑ j = 1 n ∑ k = 1 m T ( i , ℓ ) → ( j , k ) , T^{\rm out}_{(i,\ell)}\triangleq\sum_{j=1}^{n}\sum_{k=1}^{m}T_{(i,\ell)\to(j,k)}, (1)

[26] p: and the total incoming traffic to GPU ( j , k ) (j,k) as

[27] table: T ( j , k ) in ≜ ∑ i = 1 n ∑ ℓ = 1 m T ( i , ℓ ) → ( j , k ) . T^{\rm in}_{(j,k)}\triangleq\sum_{i=1}^{n}\sum_{\ell=1}^{m}T_{(i,\ell)\to(j,k)}. (2)

[28] p: Since each NIC can transmit and receive at most B 2 B_{2} units of data per unit time, the standard port-capacity argument yields the lower bound

[29] table: T min ≥ 1 B 2 ​ max ⁡ { max ( i , ℓ ) ⁡ T ( i , ℓ ) out , max ( j , k ) ⁡ T ( j , k ) in } . T^{\min}\geq\frac{1}{B_{2}}\max\!\left\{\max_{(i,\ell)}T^{\rm out}_{(i,\ell)},\max_{(j,k)}T^{\rm in}_{(j,k)}\right\}. (3)

[30] p: It is well known that this bound is achievable via a Birkhoff–von Neumann decomposition [ 15 , 16 ] , which has been widely applied in SS/TDMA systems [ 22 ] , ATM input-buffered switches [ 23 ] , Birkhoff–von Neumann switches [ 18 , 24 ] , and hybrid circuit/packet networks [ 25 ] .

[31] h3: II-A Two-Tier Fabric and Intra-Server Load Balancing

[32] p: Following [ 6 ] , we further assume that each server is equipped with a high-speed intra-server switch connecting its m m GPUs. Each port of this switch has bandwidth B 1 B_{1} , where B 1 ≫ B 2 B_{1}\gg B_{2} . This yields a heterogeneous two-tier fabric: fast intra-server links (e.g., NVLink) and slower inter-server links (e.g., InfiniBand), as illustrated in Fig. 1 .

[33] figure: Fig. 1: Two-tier GPU communication fabric. GPUs within the same server exchange traffic via a high-bandwidth intra-server switch (bandwidth B 1 B_{1} per port), while inter-server GPU traffic is carried by NICs through the global m ​ n × m ​ n mn\times mn crossbar with bandwidth B 2 B_{2} per port.

[34] p: Under this model, intra-server traffic does not consume NIC bandwidth. Accordingly, the effective inter-server outgoing traffic from GPU ( i , ℓ ) (i,\ell) is

[35] table: T ( i , ℓ ) out , inter ≜ ∑ j ≠ i ∑ k = 1 m T ( i , ℓ ) → ( j , k ) , T^{\rm out,inter}_{(i,\ell)}\triangleq\sum_{j\neq i}\sum_{k=1}^{m}T_{(i,\ell)\to(j,k)}, (4)

[36] p: and the effective inter-server incoming traffic to GPU ( j , k ) (j,k) becomes

[37] table: T ( j , k ) in , inter ≜ ∑ i ≠ j ∑ ℓ = 1 m T ( i , ℓ ) → ( j , k ) . T^{\rm in,inter}_{(j,k)}\triangleq\sum_{i\neq j}\sum_{\ell=1}^{m}T_{(i,\ell)\to(j,k)}. (5)

[38] p: Hence, in the two-tier fabric, the lower bound in ( 3 ) continues to hold when the total outgoing and incoming loads, T ( i , ℓ ) out T^{\rm out}_{(i,\ell)} and T ( j , k ) in T^{\rm in}_{(j,k)} , are replaced by their effective inter-server counterparts defined in ( 4 )–( 5 ).

[39] p: To further reduce the completion time, we are motivated by the key observation in [ 6 ] that the high-bandwidth intra-server fabric can be used to reshape traffic before it traverses the bottleneck inter-server tier. In a two-tier cluster, stragglers often arise not from imbalance at the server level, but from micro-level skew across GPUs or NICs within the same server. This suggests that intra-server load balancing can mitigate per-port congestion without altering the aggregate server-to-server demand.

[40] p: Suppose that the lower bound in ( 3 ) is dominated by T ( i ∗ , ℓ ∗ ) out , inter T^{\rm out,inter}_{(i^{*},\ell^{*})} , so that GPU ( i ∗ , ℓ ∗ ) (i^{*},\ell^{*}) is the system straggler. Then

[41] table: T ( i ∗ , ℓ ∗ ) out , inter \displaystyle T^{\rm out,inter}_{(i^{*},\ell^{*})} ≥ 1 m ​ ∑ ℓ = 1 m T ( i ∗ , ℓ ) out , inter \displaystyle\geq\frac{1}{m}\sum_{\ell=1}^{m}T^{\rm out,inter}_{(i^{*},\ell)} = ∑ j ≠ i ∗ ∑ k = 1 m 1 m ​ ∑ ℓ = 1 m T ( i ∗ , ℓ ) → ( j , k ) . \displaystyle=\sum_{j\neq i^{*}}\sum_{k=1}^{m}\frac{1}{m}\sum_{\ell=1}^{m}T_{(i^{*},\ell)\to(j,k)}. (6)

[42] p: The inequality shows that the maximum outgoing load at server i ∗ i^{*} is at least the average outgoing load across its m m GPUs. Hence, if traffic from server i ∗ i^{*} to remote GPUs is unevenly distributed across its local GPUs, the straggler effect is attributable to micro-level imbalance rather than to excess aggregate demand.

[43] p: Exploiting the high-speed intra-server switch, traffic from server i ∗ i^{*} to any remote GPU ( j , k ) (j,k) can be evenly redistributed across the m m GPUs within that server, yielding the balanced traffic matrix

[44] table: T ′ ( i ∗ , ℓ ′ ) → ( j , k ) ≜ 1 m ∑ ℓ = 1 m T ( i ∗ , ℓ ) → ( j , k ) , ∀ ℓ ′ = 1 , … , m . T^{\prime}_{(i^{*},\ell^{\prime})\to(j,k)}\triangleq\frac{1}{m}\sum_{\ell=1}^{m}T_{(i^{*},\ell)\to(j,k)},\qquad\forall\;\ell^{\prime}=1,\ldots,m. (7)

[45] p: This redistribution preserves the total server-to-server traffic while equalizing per-GPU outgoing loads. Consequently, it cannot increase the maximum outgoing load and therefore cannot increase the completion time; it strictly reduces the completion time unless the traffic is already evenly distributed across the m m GPUs within server i ∗ i^{*} .

[46] p: An analogous argument applies when the dominant term in ( 3 ) is T ( j ∗ , k ∗ ) in , inter T^{\rm in,inter}_{(j^{*},k^{*})} : by balancing incoming traffic within server j ∗ j^{*} using intra-server transfers, one can similarly mitigate micro-level imbalance on the receiving side without affecting aggregate demand.

[47] h3: II-B Server-Level Traffic Aggregation

[48] p: The preceding balancing arguments suggest that, in a two-tier fabric, completion time is fundamentally governed by server-level aggregate traffic rather than by micro-level GPU imbalance. We therefore formalize this aggregation explicitly.

[49] p: For each ordered pair of servers ( i , j ) (i,j) , define the aggregated traffic

[50] table: T i , j ≜ ∑ ℓ = 1 m ∑ k = 1 m T ( i , ℓ ) → ( j , k ) , T_{i,j}\triangleq\sum_{\ell=1}^{m}\sum_{k=1}^{m}T_{(i,\ell)\to(j,k)}, (8)

[51] p: which represents the total amount of data transmitted from server i i to server j j across all GPUs.

[52] p: If both outgoing and incoming intra-server balancing are performed, then for each server pair ( i , j ) (i,j) the traffic can be evenly distributed across the m × m m\times m GPU pairs. The resulting fully balanced traffic matrix becomes

[53] table: T ~ ( i , ℓ ) → ( j , k ) ≜ 1 m 2 ​ T i , j , ∀ i , ℓ , j , k . \widetilde{T}_{(i,\ell)\to(j,k)}\triangleq\frac{1}{m^{2}}T_{i,j},\qquad\forall\,i,\ell,j,k. (9)

[54] p: By construction, this transformation preserves the aggregate server-to-server demand T i , j T_{i,j} while equalizing both the outgoing load at each GPU in server i i and the incoming load at each GPU in server j j .

[55] p: Applying the per-port capacity lower bound to the balanced traffic in ( 9 ), and noting that each GPU in server i i now carries an outgoing load of ∑ j = 1 n T i , j / m \sum_{j=1}^{n}T_{i,j}/m and each GPU in server j j carries an incoming load of ∑ i = 1 n T i , j / m \sum_{i=1}^{n}T_{i,j}/m , we obtain

[56] table: T ~ min ≥ 1 B 2 ​ max ​ { max ⁡ ∑ j = 1 n i ⁡ T i , j m , max ⁡ ∑ i = 1 n j ⁡ T i , j m } . \widetilde{T}^{\min}\geq\frac{1}{B_{2}}\max\!\left\{\max_{i}\sum_{j=1}^{n}\frac{T_{i,j}}{m},\max_{j}\sum_{i=1}^{n}\frac{T_{i,j}}{m}\right\}. (10)

[57] p: This bound depends only on server-level aggregates { T i , j } \{T_{i,j}\} , thereby demonstrating that, after intra-server balancing, the completion time is governed by server-level traffic rather than by micro-level GPU skew.

[58] h2: III Hierarchical Birkhoff–von Neumann Decomposition

[59] p: The lower bound in ( 10 ) for the aggregated inter-server traffic (see Section II-B ) can be achieved by applying a Birkhoff–von Neumann (BvN) decomposition to the m ​ n × m ​ n mn\times mn traffic matrix among all NICs. However, directly decomposing such a large matrix incurs prohibitive computational complexity. We therefore propose a hierarchical Birkhoff–von Neumann decomposition, which exploits the server structure to significantly reduce complexity.

[60] h3: III-A Preliminaries

[61] p: We begin by introducing basic matrix notions used throughout the paper.

[62] h5: Permutation and subpermutation matrices

[63] p: A permutation matrix is a binary-valued square matrix in which each row and each column contains exactly one entry equal to 1. A subpermutation matrix is a binary-valued square matrix in which each row and each column contains at most one entry equal to 1. Equivalently, a permutation (resp. subpermutation) matrix represents a perfect (resp. partial) matching in a bipartite graph.

[64] h6: Definition 1 (Scaled doubly stochastic matrices)

[65] p: An n × n n\times n nonnegative matrix 𝐗 \mathbf{X} is called doubly stochastic with scale Δ \Delta if all its row sums and all its column sums are equal to Δ \Delta . An n × n n\times n nonnegative matrix 𝐗 \mathbf{X} is called doubly substochastic with scale Δ \Delta if all its row sums and all its column sums are not greater than Δ \Delta .

[66] p: The following classical result, due to Birkhoff [ 15 ] and von Neumann [ 16 ] , characterizes the structure of such matrices when their entries are integers.

[67] h6: Proposition 2 (Birkhoff–von Neumann decomposition)

[68] p: Let 𝐗 \mathbf{X} be an n × n n\times n nonnegative integer-valued matrix.

[69] p: If 𝐗 \mathbf{X} is doubly stochastic with scale Δ \Delta , then 𝐗 \mathbf{X} can be decomposed as

[70] table: 𝐗 = ∑ d = 1 Δ 𝐏 d , \mathbf{X}=\sum_{d=1}^{\Delta}\mathbf{P}_{d},

[71] p: where each 𝐏 d \mathbf{P}_{d} is an n × n n\times n permutation matrix.

[72] p: If 𝐗 \mathbf{X} is doubly substochastic with scale Δ \Delta , then 𝐗 \mathbf{X} can be decomposed as

[73] table: 𝐗 = ∑ d = 1 D 𝐐 d , \mathbf{X}=\sum_{d=1}^{D}\mathbf{Q}_{d},

[74] p: where D ≤ Δ D\leq\Delta and each 𝐐 d \mathbf{Q}_{d} is an n × n n\times n subpermutation matrix.

[75] p: Proof. We outline a self-contained proof based on bipartite graph edge coloring.

[76] p: Consider the bipartite multigraph G = ( 𝒰 ∪ 𝒱 , E ) G=(\mathcal{U}\cup\mathcal{V},E) with 𝒰 = { 1 , … , n } \mathcal{U}=\{1,\ldots,n\} and 𝒱 = { 1 , … , n } \mathcal{V}=\{1,\ldots,n\} , where the number of parallel edges between u ∈ 𝒰 u\in\mathcal{U} and v ∈ 𝒱 v\in\mathcal{V} equals X u , v X_{u,v} . Each row sum and column sum of 𝐗 \mathbf{X} equals the degree of the corresponding vertex.

[77] p: Doubly stochastic case. If 𝐗 \mathbf{X} is doubly stochastic with scale Δ \Delta , then G G is a Δ \Delta -regular bipartite multigraph. By Kőnig’s line-coloring theorem, the edges of G G can be colored using exactly Δ \Delta colors such that no two edges of the same color share an endpoint. Each color class therefore forms a perfect matching in G G , which corresponds to a permutation matrix. Summing these Δ \Delta permutation matrices yields 𝐗 \mathbf{X} .

[78] p: Doubly substochastic case. If 𝐗 \mathbf{X} is doubly substochastic with scale Δ \Delta , then the maximum degree of G G is at most Δ \Delta . By adding dummy edges to G G if necessary, we can obtain a Δ \Delta -regular bipartite multigraph without affecting the original edges. Applying the above argument to the augmented graph and discarding the dummy edges yields a decomposition of 𝐗 \mathbf{X} into at most Δ \Delta subpermutation matrices.

[79] h3: III-B The Theory of Hierarchical Birkhoff–von Neumann Decomposition

[80] p: In this section, we develop the main theory for the hierarchical Birkhoff–von Neumann decomposition.

[81] h6: Definition 3 ( ( m , n ) (m,n) -block matrix)

[82] p: An m ​ n × m ​ n mn\times mn matrix 𝐗 \mathbf{X} is called an ( m , n ) (m,n) -block matrix if it can be partitioned into n × n n\times n blocks, where each block is an m × m m\times m submatrix. That is,

[83] table: 𝐗 = [ 𝐗 1 , 1 𝐗 1 , 2 ⋯ 𝐗 1 , n 𝐗 2 , 1 𝐗 2 , 2 ⋯ 𝐗 2 , n ⋱ 𝐗 n , 1 𝐗 n , 2 ⋯ 𝐗 n , n ] , \mathbf{X}=\begin{bmatrix}\mathbf{X}_{1,1}&\mathbf{X}_{1,2}&\cdots&\mathbf{X}_{1,n}\\ \mathbf{X}_{2,1}&\mathbf{X}_{2,2}&\cdots&\mathbf{X}_{2,n}\\ \vdots&\vdots&\ddots&\vdots\\ \mathbf{X}_{n,1}&\mathbf{X}_{n,2}&\cdots&\mathbf{X}_{n,n}\end{bmatrix},

[84] p: where each block 𝐗 i , j ∈ ℝ m × m \mathbf{X}_{i,j}\in\mathbb{R}^{m\times m} . Equivalently, each block row and each block column of 𝐗 \mathbf{X} consists of exactly n n m × m m\times m submatrices.

[85] h6: Theorem 4

[86] p: Consider an ( m , n ) (m,n) -block matrix 𝐗 \mathbf{X} in Definition 3 . Assume that 𝐗 i , j \mathbf{X}_{i,j} is an integer-valued doubly substochastic matrix with scale Δ i , j \Delta_{i,j} . Define

[87] table: Δ = max ⁡ [ max ⁡ ∑ j = 1 n 1 ≤ i ≤ n ⁡ Δ i , j , max ⁡ ∑ i = 1 n 1 ≤ j ≤ n ⁡ Δ i , j ] . \Delta=\max[\max_{1\leq i\leq n}\sum_{j=1}^{n}\Delta_{i,j},\max_{1\leq j\leq n}\sum_{i=1}^{n}\Delta_{i,j}]. (11)

[88] p: Then there are Δ \Delta m ​ n × m ​ n mn\times mn subpermutation matrices { P d , 1 ≤ d ≤ Δ } \{P_{d},1\leq d\leq\Delta\} such that

[89] table: 𝐗 = ∑ d = 1 Δ P d . \mathbf{X}=\sum_{d=1}^{\Delta}P_{d}. (12)

[90] p: We prove the theorem by constructing the subpermutation matrices { P d } \{P_{d}\} explicitly.

[91] p: Step 1: Decompose each block into subpermutation matrices. Fix any ( i , j ) ∈ { 1 , … , n } 2 (i,j)\in\{1,\ldots,n\}^{2} . By assumption, the block 𝐗 i , j \mathbf{X}_{i,j} is an integer-valued doubly substochastic matrix with scale Δ i , j \Delta_{i,j} . By Proposition 2 , there exist subpermutation matrices 𝐒 1 ( i , j ) , … , 𝐒 Δ i , j ( i , j ) ∈ { 0 , 1 } m × m \mathbf{S}^{(i,j)}_{1},\ldots,\mathbf{S}^{(i,j)}_{\Delta_{i,j}}\in\{0,1\}^{m\times m} such that

[92] table: 𝐗 i , j = ∑ r = 1 Δ i , j 𝐒 r ( i , j ) . \mathbf{X}_{i,j}=\sum_{r=1}^{\Delta_{i,j}}\mathbf{S}^{(i,j)}_{r}. (13)

[93] p: (If fewer than Δ i , j \Delta_{i,j} subpermutation matrices are returned by Proposition 2 , we append all-zero m × m m\times m matrices so that ( 13 ) holds with exactly Δ i , j \Delta_{i,j} terms.)

[94] p: Step 2: Construct a server-level matrix of scales. Define the n × n n\times n nonnegative integer matrix

[95] table: A ≜ [ A i , j ] , A i , j ≜ Δ i , j . A\triangleq[A_{i,j}],\qquad A_{i,j}\triangleq\Delta_{i,j}.

[96] p: By definition of Δ \Delta in ( 11 ), the maximum row sum and maximum column sum of A A are both at most Δ \Delta . Hence A A is an integer-valued doubly substochastic matrix with scale Δ \Delta .

[97] p: By Proposition 2 , there exist subpermutation matrices Q 1 , … , Q Δ ∈ { 0 , 1 } n × n Q_{1},\ldots,Q_{\Delta}\in\{0,1\}^{n\times n} such that

[98] table: A = ∑ d = 1 Δ Q d . A=\sum_{d=1}^{\Delta}Q_{d}. (14)

[99] p: (Again, if fewer than Δ \Delta terms arise, pad with all-zero n × n n\times n matrices.)

[100] p: Step 3: Allocate each block-level component to one global index d d . For each fixed block ( i , j ) (i,j) , equation ( 14 ) implies

[101] table: Δ i , j = A i , j = ∑ d = 1 Δ ( Q d ) i , j . \Delta_{i,j}=A_{i,j}=\sum_{d=1}^{\Delta}(Q_{d})_{i,j}. (15)

[102] p: Let

[103] table: 𝒟 i , j ≜ { d : ( Q d ) i , j = 1 } . \mathcal{D}_{i,j}\triangleq\{d:(Q_{d})_{i,j}=1\}.

[104] p: From ( 15 ), we know that | 𝒟 i , j | = Δ i , j |\mathcal{D}_{i,j}|=\Delta_{i,j} . Arrange the Δ i , j \Delta_{i,j} elements in 𝒟 i , j \mathcal{D}_{i,j} in increasing order and we can represent the set

[105] table: 𝒟 i , j = { d ⁡ ( i , j , r ) , r = 1 , 2 , … , Δ i , j } . \mathcal{D}_{i,j}=\{d(i,j,r),r=1,2,\ldots,\Delta_{i,j}\}.

[106] p: Since 𝒟 i , j \mathcal{D}_{i,j} is a set with Δ i , j \Delta_{i,j} distinct elements, the mapping r ↦ d ⁡ ( i , j , r ) r\mapsto d(i,j,r) is a bijection from { 1 , … , Δ i , j } \{1,\ldots,\Delta_{i,j}\} onto 𝒟 i , j \mathcal{D}_{i,j} ; in particular, for each d ∈ 𝒟 i , j d\in\mathcal{D}_{i,j} there exists a unique r r such that d ⁡ ( i , j , r ) = d d(i,j,r)=d .

[107] p: Step 4: Build the global m ​ n × m ​ n mn\times mn subpermutation matrices P d P_{d} . For each d ∈ { 1 , … , Δ } d\in\{1,\ldots,\Delta\} , define an m ​ n × m ​ n mn\times mn ( m , n ) (m,n) -block matrix P d P_{d} by specifying its ( i , j ) (i,j) block as follows:

[108] table: ( P d ) i , j ≜ { 𝐒 r ( i , j ) if d ⁡ ( i , j , r ) = d , 𝟎 m × m otherwise . (P_{d})_{i,j}\triangleq\begin{cases}\mathbf{S}^{(i,j)}_{r}&\text{if $d(i,j,r)=d$},\\[5.69054pt] \mathbf{0}_{m\times m}&\text{otherwise}.\end{cases} (16)

[109] p: Step 5: Each P d P_{d} is a subpermutation matrix. We verify that P d P_{d} has at most one “1” in each row and each column.

[110] p: Fix d d . Because Q d Q_{d} is a subpermutation matrix, in each block row i i there is at most one block column j j with ( Q d ) i , j = 1 (Q_{d})_{i,j}=1 . Hence, in block row i i of P d P_{d} , there is at most one nonzero m × m m\times m block. Inside that block, ( P d ) i , j (P_{d})_{i,j} is a subpermutation matrix, so each of its m m rows contains at most one “1”. Therefore, every row of the full m ​ n × m ​ n mn\times mn matrix P d P_{d} contains at most one “1”. The same argument applies to columns because each column of Q d Q_{d} contains at most one “1”, so each block column of P d P_{d} has at most one nonzero block, and that block has at most one “1” per column. Thus P d P_{d} is a subpermutation matrix.

[111] p: Step 6: Summing { P d } \{P_{d}\} recovers 𝐗 \mathbf{X} .

[112] p: Note that

[113] table: ∑ d = 1 Δ ( P d ) i , j = ∑ r = 1 Δ i , j 𝐒 r ( i , j ) = 𝐗 i , j , \sum_{d=1}^{\Delta}(P_{d})_{i,j}=\sum_{r=1}^{\Delta_{i,j}}\mathbf{S}^{(i,j)}_{r}=\mathbf{X}_{i,j},

[114] p: where the last equality follows from ( 13 ). Since this holds for every ( i , j ) (i,j) block, we conclude that

[115] table: 𝐗 = ∑ d = 1 Δ P d , \mathbf{X}=\sum_{d=1}^{\Delta}P_{d},

[116] p: which is exactly ( 12 ). This completes the proof of Theorem 4 .

[117] h3: III-C Using Hierarchical Birkhoff-von Neumann Decomposition for the Two-Tier Fabric

[118] p: In this section, we illustrate how to apply Theorem 4 to the balanced traffic matrix in ( 17 ), i.e.,

[119] table: T ~ ( i , ℓ ) → ( j , k ) ≜ 1 m 2 ​ T i , j , ∀ i , ℓ , j , k , \widetilde{T}_{(i,\ell)\to(j,k)}\triangleq\frac{1}{m^{2}}T_{i,j},\qquad\forall\,i,\ell,j,k, (17)

[120] p: where T i , j T_{i,j} is the aggregated traffic from server i i to server j j defined in ( 8 ). Assume that T i , j / m 2 T_{i,j}/m^{2} are nonnegative integers. Then T ~ \widetilde{T} is an ( m , n ) (m,n) -block matrix whose ( i , j ) (i,j) block equals

[121] table: T ~ i , j = T i , j m 2 ​ J m , \widetilde{T}_{i,j}=\frac{T_{i,j}}{m^{2}}\,J_{m}, (18)

[122] p: where J m J_{m} denotes the m × m m\times m all-ones matrix.

[123] p: We illustrate Step 1 to Step 4 for the case with m = 2 m=2 , n = 3 n=3 . Specifically, we consider n = 3 n=3 servers, each with m = 2 m=2 NICs (equivalently, m ​ n = 6 mn=6 NICs total). We enforce zero intra-server traffic , i.e., the ( i , i ) (i,i) block is the 2 × 2 2\times 2 zero matrix. Suppose that T i , j / m 2 = 1 {T_{i,j}}/{m^{2}}=1 for ( i , j ) = ( 1 , 2 ) , ( 2 , 3 ) (i,j)=(1,2),(2,3) and ( 3 , 1 ) (3,1) . Then the corresponding 6 × 6 6\times 6 balanced NIC-level matrix T ~ \widetilde{T} in ( 17 ) is an ( 2 , 3 ) (2,3) -block matrix with 3 × 3 3\times 3 blocks of size 2 × 2 2\times 2 :

[124] table: T ~ = [ 𝟎 𝟏𝟏 ⊤ 𝟎 𝟎 𝟎 𝟏𝟏 ⊤ 𝟏𝟏 ⊤ 𝟎 𝟎 ] , 𝟏𝟏 ⊤ = [ 1 1 1 1 ] , 𝟎 = [ 0 0 0 0 ] . \widetilde{T}=\begin{bmatrix}\mathbf{0}&\mathbf{1}\mathbf{1}^{\top}&\mathbf{0}\\ \mathbf{0}&\mathbf{0}&\mathbf{1}\mathbf{1}^{\top}\\ \mathbf{1}\mathbf{1}^{\top}&\mathbf{0}&\mathbf{0}\end{bmatrix},\mathbf{1}\mathbf{1}^{\top}=\begin{bmatrix}1&1\\ 1&1\end{bmatrix},\mathbf{0}=\begin{bmatrix}0&0\\ 0&0\end{bmatrix}.

[125] p: Step 1: Decompose each block into subpermutation matrices. For each nonzero 2 × 2 2\times 2 block 𝟏𝟏 ⊤ \mathbf{1}\mathbf{1}^{\top} , we use the standard decomposition

[126] table: 𝟏𝟏 ⊤ = [ 1 0 0 1 ] ⏟ 𝐒 1 ( i , j ) + [ 0 1 1 0 ] ⏟ 𝐒 2 ( i , j ) , \mathbf{1}\mathbf{1}^{\top}=\underbrace{\begin{bmatrix}1&0\\ 0&1\end{bmatrix}}_{\mathbf{S}^{(i,j)}_{1}}+\underbrace{\begin{bmatrix}0&1\\ 1&0\end{bmatrix}}_{\mathbf{S}^{(i,j)}_{2}},

[127] p: where each 𝐒 r ( i , j ) \mathbf{S}^{(i,j)}_{r} is a 2 × 2 2\times 2 permutation matrix (hence a subpermutation matrix). For a zero block, there is nothing to decompose.

[128] p: Thus, for every inter-server pair ( i , j ) = ( 1 , 2 ) , ( 2 , 3 ) (i,j)=(1,2),(2,3) and ( 3 , 1 ) (3,1) ,

[129] table: T ~ i , j = 𝐒 1 ( i , j ) + 𝐒 2 ( i , j ) , Δ i , j = 2 , \widetilde{T}_{i,j}=\mathbf{S}^{(i,j)}_{1}+\mathbf{S}^{(i,j)}_{2},\qquad\Delta_{i,j}=2,

[130] p: and Δ i , j = 0 \Delta_{i,j}=0 otherwise.

[131] p: Step 2: Construct a server-level matrix of scales. The block-scale matrix is

[132] table: A ≜ [ A i , j ] , A i , j ≜ Δ i , j . A\triangleq[A_{i,j}],\qquad A_{i,j}\triangleq\Delta_{i,j}.

[133] p: Thus,

[134] table: A ≜ [ Δ i , j ] i , j = 1 3 = [ 0 2 0 0 0 2 2 0 0 ] . A\triangleq[\Delta_{i,j}]_{i,j=1}^{3}=\begin{bmatrix}0&2&0\\ 0&0&2\\ 2&0&0\end{bmatrix}.

[135] p: Its row sums and column sums are all equal to 2 2 , hence (in the terminology of the preliminaries) A A is doubly stochastic with scale

[136] table: Δ = max ⁡ { max ⁡ ∑ j = 1 3 i ⁡ Δ i , j , max ⁡ ∑ i = 1 3 j ⁡ Δ i , j } = 2 . \Delta=\max\Big\{\max_{i}\sum_{j=1}^{3}\Delta_{i,j},\ \max_{j}\sum_{i=1}^{3}\Delta_{i,j}\Big\}=2.

[137] p: Step 3: Allocate each block-level component to one global index d d . By Proposition 2 , A A can be decomposed into Δ = 2 \Delta=2 permutation matrices. In this example,

[138] table: Q 1 = Q 2 = [ 0 1 0 0 0 1 1 0 0 ] . Q_{1}=Q_{2}=\begin{bmatrix}0&1&0\\ 0&0&1\\ 1&0&0\end{bmatrix}.

[139] p: Hence, for each nonzero block location ( i , j ) ∈ { ( 1 , 2 ) , ( 2 , 3 ) , ( 3 , 1 ) } (i,j)\in\{(1,2),(2,3),(3,1)\} ,

[140] table: 𝒟 i , j ≜ { d ∈ { 1 , 2 } : ( Q d ) i , j = 1 } = { 1 , 2 } , \mathcal{D}_{i,j}\triangleq\{d\in\{1,2\}:(Q_{d})_{i,j}=1\}=\{1,2\},

[141] p: and thus

[142] table: | 𝒟 i , j | = Δ i , j = 2 . |\mathcal{D}_{i,j}|=\Delta_{i,j}=2.

[143] p: Step 4: Build the global m ​ n × m ​ n mn\times mn subpermutation matrices P d P_{d} . We index the m ​ n = 6 mn=6 NICs in the order

[144] table: ( 1 , 1 ) , ( 1 , 2 ) , ( 2 , 1 ) , ( 2 , 2 ) , ( 3 , 1 ) , ( 3 , 2 ) . (1,1),(1,2),(2,1),(2,2),(3,1),(3,2).

[145] p: We now construct P d P_{d} for d ∈ { 1 , 2 } d\in\{1,2\} .

[146] p: (i) Matrix P 1 P_{1} : place 𝐒 1 ( i , j ) = I 2 \mathbf{S}^{(i,j)}_{1}=I_{2} in blocks ( 1 , 2 ) (1,2) , ( 2 , 3 ) (2,3) , ( 3 , 1 ) (3,1) , and zeros elsewhere:

[147] table: P 1 = [ 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0 ] . P_{1}=\begin{bmatrix}0&0&1&0&0&0\\ 0&0&0&1&0&0\\ 0&0&0&0&1&0\\ 0&0&0&0&0&1\\ 1&0&0&0&0&0\\ 0&1&0&0&0&0\end{bmatrix}.

[148] p: This is a 6 × 6 6\times 6 permutation matrix (hence a subpermutation matrix).

[149] p: (ii) Matrix P 2 P_{2} : place 𝐒 2 ( i , j ) = [ 0 1 1 0 ] \mathbf{S}^{(i,j)}_{2}=\begin{bmatrix}0&1\\ 1&0\end{bmatrix} in the same three blocks:

[150] table: P 2 = [ 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 ] . P_{2}=\begin{bmatrix}0&0&0&1&0&0\\ 0&0&1&0&0&0\\ 0&0&0&0&0&1\\ 0&0&0&0&1&0\\ 0&1&0&0&0&0\\ 1&0&0&0&0&0\end{bmatrix}.

[151] p: This is also a 6 × 6 6\times 6 permutation matrix.

[152] h2: IV Balancing the Traffic within a Server

[153] p: In this section, we present a simple constructive algorithm for balancing traffic among the m m GPUs (or NICs) within a single server. For the hierarchical Birkhoff–von Neumann decomposition developed in the previous section, it is not necessary to achieve the fully balanced form in ( 9 ). Instead, it suffices to ensure that each row sum and each column sum of the corresponding m × m m\times m block is properly balanced (i.e., bounded by the same target value). The proposed algorithm operates on an m × m m\times m nonnegative integer matrix, uses only local unit-transfer operations, preserves integrality and nonnegativity, and is guaranteed to terminate in finite time.

[154] h3: IV-A The objective of traffic balancing

[155] p: Recall that T ( i , ℓ ) → ( j , k ) T_{(i,\ell)\to(j,k)} denotes the amount of data to be transmitted from the ( i , ℓ ) (i,\ell) GPU to the ( j , k ) (j,k) GPU. Let

[156] table: x ℓ ​ k ≜ T ( i , ℓ ) → ( j , k ) x_{\ell k}\triangleq T_{(i,\ell)\to(j,k)}

[157] p: and form the m × m m\times m matrix 𝐗 = [ x ℓ ​ k ] \mathbf{X}=[x_{\ell k}] (here we omit the subscripts i i and j j for notational clarity). Define

[158] table: W ≜ ∑ ℓ = 1 m ∑ k = 1 m x ℓ ​ k , r ℓ ≜ ∑ k = 1 m x ℓ ​ k , c k ≜ ∑ ℓ = 1 m x ℓ ​ k , W\triangleq\sum_{\ell=1}^{m}\sum_{k=1}^{m}x_{\ell k},\qquad r_{\ell}\triangleq\sum_{k=1}^{m}x_{\ell k},\qquad c_{k}\triangleq\sum_{\ell=1}^{m}x_{\ell k}, (19)

[159] p: and let

[160] table: B ≜ ⌈ W m ⌉ . B\triangleq\left\lceil\frac{W}{m}\right\rceil. (20)

[161] p: Our objective is to transform 𝐗 \mathbf{X} into another nonnegative integer-valued m × m m\times m matrix, using local operations that preserve the total sum W W , such that

[162] table: r ℓ ≤ B ∀ ℓ , c k ≤ B ∀ k . r_{\ell}\leq B\quad\forall\,\ell,\qquad c_{k}\leq B\quad\forall\,k.

[163] p: After the transform, the matrix is doubly substochastic with the scale B B .

[164] h3: IV-B Local Unit-Transfer Operations

[165] p: We employ two types of unit-transfer operations. Each operation preserves nonnegativity, integrality, and the total sum W W .

[166] h4: IV-B 1 Column Transfer

[167] p: For a fixed column k k and two distinct rows ℓ ≠ ℓ ′ \ell\neq\ell^{\prime} with x ℓ ​ k ≥ 1 x_{\ell k}\geq 1 , perform

[168] table: x ℓ ​ k ← x ℓ ​ k − 1 , x ℓ ′ ​ k ← x ℓ ′ ​ k + 1 . x_{\ell k}\leftarrow x_{\ell k}-1,\qquad x_{\ell^{\prime}k}\leftarrow x_{\ell^{\prime}k}+1.

[169] p: This operation decreases the row sum r ℓ r_{\ell} by one and increases r ℓ ′ r_{\ell^{\prime}} by one, while leaving all column sums unchanged.

[170] h4: IV-B 2 Row Transfer

[171] p: For a fixed row ℓ \ell and two distinct columns k ≠ k ′ k\neq k^{\prime} with x ℓ ​ k ≥ 1 x_{\ell k}\geq 1 , perform

[172] table: x ℓ ​ k ← x ℓ ​ k − 1 , x ℓ ​ k ′ ← x ℓ ​ k ′ + 1 . x_{\ell k}\leftarrow x_{\ell k}-1,\qquad x_{\ell k^{\prime}}\leftarrow x_{\ell k^{\prime}}+1.

[173] p: This operation decreases the column sum c k c_{k} by one and increases c k ′ c_{k^{\prime}} by one, while leaving all row sums unchanged.

[174] h3: IV-C Two-Phase Balancing Algorithm

[175] h4: IV-C 1 Phase I: Row Balancing

[176] p: While there exists a row index ℓ \ell such that r ℓ > B r_{\ell}>B , select another row ℓ ′ \ell^{\prime} with r ℓ ′ < B r_{\ell^{\prime}}<B (such a row must exist since ∑ ℓ = 1 m r ℓ = W ≤ m ​ B \sum_{\ell=1}^{m}r_{\ell}=W\leq mB ), choose any column k k with x ℓ ​ k ≥ 1 x_{\ell k}\geq 1 , and apply a column transfer from ( ℓ , k ) (\ell,k) to ( ℓ ′ , k ) (\ell^{\prime},k) .

[177] p: Define the row imbalance potential

[178] table: Φ row ≜ ∑ ℓ = 1 m max ⁡ ( 0 , r ℓ − B ) . \Phi_{\mathrm{row}}\triangleq\sum_{\ell=1}^{m}\max(0,r_{\ell}-B).

[179] p: Each column transfer reduces Φ row \Phi_{\mathrm{row}} by exactly one, guaranteeing finite termination with

[180] table: r ℓ ≤ B ∀ ℓ . r_{\ell}\leq B\quad\forall\,\ell.

[181] h4: IV-C 2 Phase II: Column Balancing

[182] p: After Phase I, all row sums are fixed and satisfy r ℓ ≤ B r_{\ell}\leq B . While there exists a column index k k such that c k > B c_{k}>B , select another column k ′ k^{\prime} with c k ′ < B c_{k^{\prime}}<B , choose any row ℓ \ell with x ℓ ​ k ≥ 1 x_{\ell k}\geq 1 , and apply a row transfer from ( ℓ , k ) (\ell,k) to ( ℓ , k ′ ) (\ell,k^{\prime}) .

[183] p: Define the column imbalance potential

[184] table: Φ col ≜ ∑ k = 1 m max ⁡ ( 0 , c k − B ) . \Phi_{\mathrm{col}}\triangleq\sum_{k=1}^{m}\max(0,c_{k}-B).

[185] p: Each row transfer reduces Φ col \Phi_{\mathrm{col}} by exactly one, ensuring finite termination with

[186] table: c k ≤ B ∀ k . c_{k}\leq B\quad\forall\,k.

[187] h6: Theorem 5

[188] p: Let 𝐗 = [ x ℓ ​ k ] ∈ ℤ ≥ 0 m × m \mathbf{X}=[x_{\ell k}]\in\mathbb{Z}_{\geq 0}^{m\times m} be the initial intra-server traffic matrix, and let W W , { r ℓ } \{r_{\ell}\} , { c k } \{c_{k}\} and B B be defined as in ( 19 ) and ( 20 ). Then the two-phase balancing algorithm described above satisfies the following properties:

[189] p: All matrix entries remain nonnegative integers throughout the execution of the algorithm.

[190] p: The total traffic volume W W is invariant.

[191] p: The algorithm terminates after at most

[192] table: ∑ ℓ = 1 m max ⁡ ( 0 , r ℓ − B ) + ∑ k = 1 m max ⁡ ( 0 , c k − B ) \sum_{\ell=1}^{m}\max(0,r_{\ell}-B)+\sum_{k=1}^{m}\max(0,c_{k}-B)

[193] p: unit-transfer operations.

[194] p: Upon termination, the resulting matrix satisfies

[195] table: r ℓ ≤ ⌈ W m ⌉ ∀ ℓ ∈ { 1 , … , m } , r_{\ell}\leq\left\lceil\frac{W}{m}\right\rceil\quad\forall\,\ell\in\{1,\ldots,m\},

[196] p: and

[197] table: c k ≤ ⌈ W m ⌉ ∀ k ∈ { 1 , … , m } . c_{k}\leq\left\lceil\frac{W}{m}\right\rceil\quad\forall\,k\in\{1,\ldots,m\}.

[198] p: Proof. We prove each claim in turn.

[199] p: (i) Preservation of nonnegativity and integrality. Each unit-transfer operation decreases one matrix entry by one and increases another entry by one. Transfers are applied only when the decremented entry is at least one, hence all entries remain nonnegative. Since all updates are integer increments or decrements, integrality is preserved.

[200] p: (ii) Invariance of the total traffic volume. Each unit transfer moves one unit of traffic from one entry to another. Therefore, the sum of all matrix entries remains unchanged, and the total volume W W is invariant throughout the algorithm.

[201] p: (iii) Finite termination. During Phase I, each column transfer reduces the row-imbalance potential Φ row \Phi_{\mathrm{row}} by exactly one, and Φ row \Phi_{\mathrm{row}} is a nonnegative integer-valued function. Hence Phase I terminates after at most Φ row ​ ( 0 ) \Phi_{\mathrm{row}}(0) operations, where

[202] table: Φ row ​ ( 0 ) = ∑ ℓ = 1 m max ⁡ ( 0 , r ℓ − B ) . \Phi_{\mathrm{row}}(0)=\sum_{\ell=1}^{m}\max(0,r_{\ell}-B).

[203] p: is the initial row-imbalance potential. After Phase I, all row sums satisfy r ℓ ≤ ⌈ W / m ⌉ r_{\ell}\leq\lceil W/m\rceil . During Phase II, each row transfer reduces the column-imbalance potential Φ col \Phi_{\mathrm{col}} by exactly one, and Φ col \Phi_{\mathrm{col}} is also a nonnegative integer-valued function. Thus Phase II terminates after at most Φ col ​ ( 0 ) \Phi_{\mathrm{col}}(0) operations, where

[204] table: Φ col ​ ( 0 ) = ∑ k = 1 m max ⁡ ( 0 , c k − B ) \Phi_{\mathrm{col}}(0)=\sum_{k=1}^{m}\max(0,c_{k}-B)

[205] p: is the initial column-imbalance potential. The total number of unit-transfer operations is therefore at most Φ row ​ ( 0 ) + Φ col ​ ( 0 ) \Phi_{\mathrm{row}}(0)+\Phi_{\mathrm{col}}(0) .

[206] p: (iv) Feasibility of the final matrix. By construction, Phase I terminates only when r ℓ ≤ B = ⌈ W / m ⌉ r_{\ell}\leq B=\lceil W/m\rceil for all rows ℓ \ell . Phase II leaves all row sums unchanged and terminates only when c k ≤ B c_{k}\leq B for all columns k k . Therefore, upon termination, the resulting matrix satisfies the desired row and column sum bounds.

[207] h2: V Dynamic Hierarchical Birkhoff–von Neumann Decomposition

[208] p: In this section, we present a dynamic frame sizing (DFS) algorithm [ 19 , 20 , 21 ] built upon the hierarchical Birkhoff–von Neumann (BvN) decomposition developed in Section III .

[209] p: Throughout this section, we adopt a discrete-time model. All packets are assumed to have identical size, and time is slotted so that, after normalizing the inter-server bandwidth B 2 B_{2} , at most one packet can be transmitted over a link in each time slot. All switches are assumed to be empty at time 0 0 , and packet arrivals occur from time 1 1 onward.

[210] h3: V-A Dynamic Frame Sizing Principle

[211] p: The DFS algorithm operates in a frame-based manner and consists of the following steps:

[212] p: Time is divided into frames. Packets arriving during a frame are buffered and are served only in the subsequent frame.

[213] p: The frame length is adaptive rather than fixed. At the beginning of each frame, the frame size is set to the minimum completion (clearance) time required to serve all packets that have accumulated up to that time. If all buffers are empty, the frame length is set to 1.

[214] p: Traffic is first balanced within each server using the intra-server balancing procedure described in Section IV .

[215] p: The hierarchical Birkhoff–von Neumann decomposition described in Section III is then applied to determine the subpermutation matrices used by the global m ​ n × m ​ n mn\times mn crossbar switch during the frame.

[216] h3: V-B Frame-Based Operation

[217] p: We consider an m ​ n × m ​ n mn\times mn input-buffered crossbar switch interconnecting all GPUs. At each ( i , ℓ ) (i,\ell) -th GPU, there are m ​ n mn virtual output queues (VOQs), one for each destination ( j , k ) (j,k) GPU. Packets arriving at the ( i , ℓ ) (i,\ell) GPU and destined for the ( j , k ) (j,k) GPU are placed in the corresponding VOQ.

[218] p: Let T f T_{f} denote the length of the f f -th frame and define

[219] table: τ f ≜ ∑ r = 1 f − 1 T r . \tau_{f}\triangleq\sum_{r=1}^{f-1}T_{r}.

[220] p: Accordingly, τ f + 1 \tau_{f}+1 and τ f + 1 \tau_{f+1} are the first and last time slots of the f f -th frame, respectively.

[221] p: Let P ⁡ ( t ) = ( P ( i , ℓ ) , ( j , k ) ​ ( t ) ) P(t)=\big(P_{(i,\ell),(j,k)}(t)\big) denote the permutation matrix specifying the connection pattern of the crossbar switch at time t t , where P ( i , ℓ ) , ( j , k ) ​ ( t ) = 1 P_{(i,\ell),(j,k)}(t)=1 if and only if the ( i , ℓ ) (i,\ell) input is connected to the ( j , k ) (j,k) output at time t t . Let a ( i , ℓ ) , ( j , k ) ​ ( t ) a_{(i,\ell),(j,k)}(t) denote the number of packets arriving at time t t to the ( i , ℓ ) (i,\ell) GPU that are destined for the ( j , k ) (j,k) GPU, and let x ( i , ℓ ) , ( j , k ) ​ ( t ) x_{(i,\ell),(j,k)}(t) denote the number of packets in the corresponding VOQ at the end of time slot t t .

[222] p: Define

[223] table: A ( i , ℓ ) , ( j , k ) ​ ( s , t ) ≜ ∑ u = s + 1 t a ( i , ℓ ) , ( j , k ) ​ ( u ) , A_{(i,\ell),(j,k)}(s,t)\triangleq\sum_{u=s+1}^{t}a_{(i,\ell),(j,k)}(u),

[224] p: which represents the number of packets arriving in the interval ( s , t ] (s,t] for the traffic from the ( i , ℓ ) (i,\ell) GPU to the ( j , k ) (j,k) GPU.

[225] p: By definition of the minimum completion time and by applying the framed hierarchical Birkhoff–von Neumann decomposition within each frame, the permutation matrices { P ⁡ ( t ) } \{P(t)\} can be chosen such that all packets carried over from the previous frame are cleared by the end of the current frame, i.e.,

[226] table: x ( i , ℓ ) , ( j , k ) ​ ( τ f ) ≤ ∑ t = τ f + 1 τ f + 1 P ( i , ℓ ) , ( j , k ) ​ ( t ) . x_{(i,\ell),(j,k)}(\tau_{f})\leq\sum_{t=\tau_{f}+1}^{\tau_{f+1}}P_{(i,\ell),(j,k)}(t).

[227] p: As a consequence, the backlog at the beginning of the ( f + 1 ) (f+1) -th frame consists exactly of the packets that arrived during the f f -th frame, namely,

[228] table: x ( i , ℓ ) , ( j , k ) ​ ( τ f + 1 ) = A ( i , ℓ ) , ( j , k ) ​ ( τ f , τ f + 1 ) . x_{(i,\ell),(j,k)}(\tau_{f+1})=A_{(i,\ell),(j,k)}(\tau_{f},\tau_{f+1}). (21)

[229] p: Equality ( 21 ) is the key relation underlying the DFS algorithm. It shows that the backlog at the end of a frame depends only on the new arrivals during that frame.

[230] h3: V-C Stability Analysis

[231] p: In this section, we analyze the stability of the DFS algorithm. For clarity of exposition, we specialize the arrival model to independent Poisson arrivals.

[232] p: For each pair ( ( i , ℓ ) , ( j , k ) ) ((i,\ell),(j,k)) , the arrival processes { a ( i , ℓ ) , ( j , k ) ​ ( t ) } t ≥ 1 \{a_{(i,\ell),(j,k)}(t)\}_{t\geq 1} are independent across ( i , ℓ , j , k ) (i,\ell,j,k) and i.i.d. over time t t , with a ( i , ℓ ) , ( j , k ) ​ ( t ) ∼ Pois ⁡ ( λ ( i , ℓ ) , ( j , k ) ) a_{(i,\ell),(j,k)}(t)\sim\mathrm{Pois}(\lambda_{(i,\ell),(j,k)}) . Equivalently, for any integers s < t s<t ,

[233] table: ∑ u = s + 1 t a ( i , ℓ ) , ( j , k ) ​ ( u ) ∼ Pois ⁡ ( λ ( i , ℓ ) , ( j , k ) ​ ( t − s ) ) . \sum_{u=s+1}^{t}a_{(i,\ell),(j,k)}(u)\sim\mathrm{Pois}(\lambda_{(i,\ell),(j,k)}(t-s)).

[234] p: Such an assumption can be extended to more general stochastic processes, including finite-state Markov, renewal, and autoregressive arrival processes, as in [ 26 , 19 ] .

[235] p: Our main result of this section is to establish a stability result for the DFS algorithm.

[236] h6: Theorem 6

[237] p: Consider the DFS algorithm with intra-server traffic balancing. Let

[238] table: λ i , j = 1 m ​ ∑ ℓ = 1 m ∑ k = 1 m λ ( i , ℓ ) , ( j , k ) . \lambda_{i,j}=\frac{1}{m}\sum_{\ell=1}^{m}\sum_{k=1}^{m}\lambda_{(i,\ell),(j,k)}. (22)

[239] p: Assume that the arrival processes satisfy condition (A1) and

[240] table: ∑ j = 1 n λ i , j < 1 , ∀ i \displaystyle\sum_{j=1}^{n}\lambda_{i,j}<1,\qquad\forall\,i (23) ∑ i = 1 n λ i , j < 1 , ∀ j . \displaystyle\sum_{i=1}^{n}\lambda_{i,j}<1,\qquad\forall\,j. (24)

[241] p: Then, for any frame f ≥ 1 f\geq 1 ,

[242] table: 𝔼 ⁡ [ T f ] < ∞ . \mathbb{E}[T_{f}]<\infty. (25)

[243] p: Proof. Fix a frame index f ≥ 1 f\geq 1 . Let

[244] table: W i , j ​ ( f ) ≜ ∑ ℓ = 1 m ∑ k = 1 m A ( i , ℓ ) , ( j , k ) ​ ( τ f , τ f + 1 ) W_{i,j}(f)\triangleq\sum_{\ell=1}^{m}\sum_{k=1}^{m}A_{(i,\ell),(j,k)}(\tau_{f},\tau_{f+1})

[245] p: denote the total number of packets that arrive during frame f f and are destined from server i i to server j j . Define the server-level aggregate arrivals

[246] table: U i ​ ( f ) ≜ ∑ j = 1 n W i , j ​ ( f ) , V j ​ ( f ) ≜ ∑ i = 1 n W i , j ​ ( f ) , U_{i}(f)\triangleq\sum_{j=1}^{n}W_{i,j}(f),\qquad V_{j}(f)\triangleq\sum_{i=1}^{n}W_{i,j}(f),

[247] p: which represent, respectively, the total number of packets arriving during frame f f that originate from server i i (to all destinations) and that are destined to server j j (from all sources).

[248] p: Step 1: Frame length under intra-server traffic balancing. By Step (i) of DFS, packets arriving during frame f f are served only in frame f + 1 f+1 . At the beginning of frame f + 1 f+1 , DFS applies intra-server traffic balancing (Step (iii)) before scheduling the m ​ n × m ​ n mn\times mn crossbar (Step (iv)). The balancing procedure guarantees that, after balancing, the total outgoing traffic load assigned to each of the m m NICs in server i i is at most ⌈ U i ​ ( f ) / m ⌉ \lceil U_{i}(f)/m\rceil , and the total incoming traffic load assigned to each NIC in server j j is at most ⌈ V j ​ ( f ) / m ⌉ \lceil V_{j}(f)/m\rceil . Therefore, the minimum completion (clearance) time for the balanced traffic in frame f + 1 f+1 satisfies

[249] table: T f + 1 = max ⁡ { max 1 ≤ i ≤ n ⁡ ⌈ U i ​ ( f ) m ⌉ , max 1 ≤ j ≤ n ⁡ ⌈ V j ​ ( f ) m ⌉ } . T_{f+1}=\max\!\left\{\max_{1\leq i\leq n}\left\lceil\frac{U_{i}(f)}{m}\right\rceil,\;\max_{1\leq j\leq n}\left\lceil\frac{V_{j}(f)}{m}\right\rceil\right\}. (26)

[250] p: Using ⌈ x ⌉ ≤ x + 1 \lceil x\rceil\leq x+1 for all x ∈ ℝ x\in\mathbb{R} , we further obtain

[251] table: T f + 1 ≤ 1 + max ⁡ { max 1 ≤ i ≤ n ⁡ U i ​ ( f ) m , max 1 ≤ j ≤ n ⁡ V j ​ ( f ) m } . T_{f+1}\leq 1+\max\!\left\{\max_{1\leq i\leq n}\frac{U_{i}(f)}{m},\;\max_{1\leq j\leq n}\frac{V_{j}(f)}{m}\right\}. (27)

[252] p: Step 2: Exponential moment bound. Fix θ > 0 \theta>0 . From ( 27 ) and max ⁡ { z 1 , z 2 } ≤ z 1 + z 2 \max\{z_{1},z_{2}\}\leq z_{1}+z_{2} for z 1 , z 2 ≥ 0 z_{1},z_{2}\geq 0 , we have

[253] table: e θ ​ T f + 1 \displaystyle e^{\theta T_{f+1}} ≤ e θ max { max 1 ≤ i ≤ n exp ( θ m U i ( f ) ) , \displaystyle\leq e^{\theta}\,\max\!\Bigg\{\max_{1\leq i\leq n}\exp\!\Big(\tfrac{\theta}{m}U_{i}(f)\Big), max 1 ≤ j ≤ n exp ( θ m V j ( f ) ) } \displaystyle\qquad\qquad\qquad\max_{1\leq j\leq n}\exp\!\Big(\tfrac{\theta}{m}V_{j}(f)\Big)\Bigg\} ≤ e θ ​ ( ∑ i = 1 n exp ⁡ ( θ m ​ U i ​ ( f ) ) + ∑ j = 1 n exp ⁡ ( θ m ​ V j ​ ( f ) ) ) . \displaystyle\leq e^{\theta}\,\left(\sum_{i=1}^{n}\exp\!\Big(\tfrac{\theta}{m}U_{i}(f)\Big)+\sum_{j=1}^{n}\exp\!\Big(\tfrac{\theta}{m}V_{j}(f)\Big)\right). (28)

[254] p: Step 3: Conditional MGFs under Poisson arrivals. Under (A1), for each fixed ( i , j ) (i,j) , W i , j ​ ( f ) W_{i,j}(f) is Poisson with mean

[255] table: 𝔼 ⁡ [ W i , j ​ ( f ) ∣ T f ] = T f ​ ∑ ℓ = 1 m ∑ k = 1 m λ ( i , ℓ ) , ( j , k ) = m ​ λ i , j ​ T f , \mathbb{E}[W_{i,j}(f)\mid T_{f}]=T_{f}\sum_{\ell=1}^{m}\sum_{k=1}^{m}\lambda_{(i,\ell),(j,k)}=m\,\lambda_{i,j}\,T_{f},

[256] p: where λ i , j \lambda_{i,j} is defined in ( 22 ). Moreover, for fixed i i , { W i , j ​ ( f ) } j = 1 n \{W_{i,j}(f)\}_{j=1}^{n} are independent (superposition of independent Poisson variables), hence U i ​ ( f ) = ∑ j W i , j ​ ( f ) U_{i}(f)=\sum_{j}W_{i,j}(f) is Poisson with mean

[257] table: 𝔼 ⁡ [ U i ​ ( f ) ∣ T f ] = m ​ T f ​ ∑ j = 1 n λ i , j . \mathbb{E}[U_{i}(f)\mid T_{f}]=mT_{f}\sum_{j=1}^{n}\lambda_{i,j}.

[258] p: Similarly, for fixed j j , V j ​ ( f ) V_{j}(f) is Poisson with mean

[259] table: 𝔼 ⁡ [ V j ​ ( f ) ∣ T f ] = m ​ T f ​ ∑ i = 1 n λ i , j . \mathbb{E}[V_{j}(f)\mid T_{f}]=mT_{f}\sum_{i=1}^{n}\lambda_{i,j}.

[260] p: Therefore, conditioning on T f T_{f} and using the Poisson MGF,

[261] table: 𝔼 ⁡ [ e η ​ Z ] = exp ⁡ ( μ ⁡ ( e η − 1 ) ) for ​ Z ∼ Pois ⁡ ( μ ) , \mathbb{E}\!\left[e^{\eta Z}\right]=\exp\!\big(\mu(e^{\eta}-1)\big)\quad\text{for }Z\sim\mathrm{Pois}(\mu),

[262] p: we obtain, almost surely,

[263] table: ∑ i = 1 n 𝔼 ⁡ [ exp ⁡ ( θ m ​ U i ​ ( f ) ) | T f ] \displaystyle\sum_{i=1}^{n}\mathbb{E}\!\left[\exp\!\Big(\tfrac{\theta}{m}U_{i}(f)\Big)\,\middle|\,T_{f}\right] = ∑ i = 1 n exp ⁡ ( m ​ T f ​ ( ∑ j = 1 n λ i , j ) ​ ( e θ / m − 1 ) ) , \displaystyle=\sum_{i=1}^{n}\exp\!\Bigg(mT_{f}\Big(\sum_{j=1}^{n}\lambda_{i,j}\Big)\big(e^{\theta/m}-1\big)\Bigg), (29) ∑ j = 1 n 𝔼 ⁡ [ exp ⁡ ( θ m ​ V j ​ ( f ) ) | T f ] \displaystyle\sum_{j=1}^{n}\mathbb{E}\!\left[\exp\!\Big(\tfrac{\theta}{m}V_{j}(f)\Big)\,\middle|\,T_{f}\right] = ∑ j = 1 n exp ⁡ ( m ​ T f ​ ( ∑ i = 1 n λ i , j ) ​ ( e θ / m − 1 ) ) . \displaystyle=\sum_{j=1}^{n}\exp\!\Bigg(mT_{f}\Big(\sum_{i=1}^{n}\lambda_{i,j}\Big)\big(e^{\theta/m}-1\big)\Bigg). (30)

[264] p: Let

[265] table: λ ¯ ≜ max ⁡ { max ⁡ ∑ j = 1 n 1 ≤ i ≤ n ⁡ λ i , j , max ⁡ ∑ i = 1 n 1 ≤ j ≤ n ⁡ λ i , j } . \bar{\lambda}\triangleq\max\!\left\{\max_{1\leq i\leq n}\sum_{j=1}^{n}\lambda_{i,j},\;\max_{1\leq j\leq n}\sum_{i=1}^{n}\lambda_{i,j}\right\}.

[266] p: By ( 23 ) and ( 24 ), we have λ ¯ < 1 \bar{\lambda}<1 . Combining ( 28 )–( 30 ) and taking expectations yield

[267] table: 𝔼 ⁡ [ e θ ​ T f + 1 ] ≤ 2 ​ n ​ e θ ​ 𝔼 ​ [ exp ⁡ ( m ​ λ ¯ ​ T f ​ ( e θ / m − 1 ) ) ] . \mathbb{E}\!\left[e^{\theta T_{f+1}}\right]\leq 2n\,e^{\theta}\,\mathbb{E}\!\left[\exp\!\Big(m\bar{\lambda}\,T_{f}\,(e^{\theta/m}-1)\Big)\right]. (31)

[268] p: Step 4: Choose θ ∗ \theta^{*} and derive a contraction. Since ( e x − 1 ) / x (e^{x}-1)/x is strictly increasing for x > 0 x>0 and ranges from 1 1 to ∞ \infty , and since ( 1 + λ ¯ ) / ( 2 ​ λ ¯ ) > 1 (1+\bar{\lambda})/(2\bar{\lambda})>1 (because λ ¯ < 1 \bar{\lambda}<1 ), there exists a unique θ ∗ > 0 \theta^{*}>0 such that

[269] table: e θ ∗ / m − 1 θ ∗ / m = 1 + λ ¯ 2 ​ λ ¯ . \frac{e^{\theta^{*}/m}-1}{\theta^{*}/m}=\frac{1+\bar{\lambda}}{2\bar{\lambda}}. (32)

[270] p: Equivalently,

[271] table: m ​ λ ¯ ​ ( e θ ∗ / m − 1 ) = θ ∗ ​ 1 + λ ¯ 2 . m\bar{\lambda}\,(e^{\theta^{*}/m}-1)=\theta^{*}\,\frac{1+\bar{\lambda}}{2}.

[272] p: Substituting θ = θ ∗ \theta=\theta^{*} into ( 31 ) gives

[273] table: log ⁡ 𝔼 ⁡ [ e θ ∗ ​ T f + 1 ] ≤ log ⁡ ( 2 ​ n ) + θ ∗ + log ⁡ 𝔼 ⁡ [ e θ ∗ ​ 1 + λ ¯ 2 ​ T f ] . \log\mathbb{E}\!\left[e^{\theta^{*}T_{f+1}}\right]\leq\log(2n)+\theta^{*}+\log\mathbb{E}\!\left[e^{\theta^{*}\frac{1+\bar{\lambda}}{2}T_{f}}\right]. (33)

[274] p: Let ϕ ⁡ ( ϑ ) ≜ log ⁡ 𝔼 ⁡ [ e ϑ ​ T f ] \phi(\vartheta)\triangleq\log\mathbb{E}[e^{\vartheta T_{f}}] , which is convex in ϑ \vartheta (see, e.g., [ 27 ] , Proposition 7.1.8). With α ≜ ( 1 + λ ¯ ) / 2 ∈ ( 0 , 1 ) \alpha\triangleq(1+\bar{\lambda})/2\in(0,1) , Jensen’s inequality for convex ϕ ⁡ ( ⋅ ) \phi(\cdot) yields

[275] table: log ⁡ 𝔼 ⁡ [ e α ​ θ ∗ ​ T f ] = ϕ ⁡ ( α ​ θ ∗ ) \displaystyle\log\mathbb{E}\!\left[e^{\alpha\theta^{*}T_{f}}\right]=\phi(\alpha\theta^{*}) ≤ ( 1 − α ) ​ ϕ ​ ( 0 ) + α ​ ϕ ​ ( θ ∗ ) = α ​ log ⁡ 𝔼 ⁡ [ e θ ∗ ​ T f ] . \displaystyle\leq(1-\alpha)\phi(0)+\alpha\phi(\theta^{*})=\alpha\log\mathbb{E}\!\left[e^{\theta^{*}T_{f}}\right].

[276] p: Applying this bound to ( 33 ) gives the contraction

[277] table: log ⁡ 𝔼 ⁡ [ e θ ∗ ​ T f + 1 ] ≤ log ⁡ ( 2 ​ n ) + θ ∗ + 1 + λ ¯ 2 ​ log ⁡ 𝔼 ⁡ [ e θ ∗ ​ T f ] . \log\mathbb{E}\!\left[e^{\theta^{*}T_{f+1}}\right]\leq\log(2n)+\theta^{*}+\frac{1+\bar{\lambda}}{2}\,\log\mathbb{E}\!\left[e^{\theta^{*}T_{f}}\right]. (34)

[278] p: Step 5: Uniform boundedness of the log-MGF and finiteness of 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] . Define y f ≜ log ⁡ 𝔼 ⁡ [ e θ ∗ ​ T f ] y_{f}\triangleq\log\mathbb{E}[e^{\theta^{*}T_{f}}] . Then ( 34 ) implies

[279] table: y f + 1 ≤ ( log ⁡ ( 2 ​ n ) + θ ∗ ) + α ​ y f , α = 1 + λ ¯ 2 ∈ ( 0 , 1 ) . y_{f+1}\leq\big(\log(2n)+\theta^{*}\big)+\alpha y_{f},\qquad\alpha=\frac{1+\bar{\lambda}}{2}\in(0,1).

[280] p: Since T 1 = 1 T_{1}=1 , we have y 1 = θ ∗ < ∞ y_{1}=\theta^{*}<\infty , and the above recursion implies that sup f y f < ∞ \sup_{f}y_{f}<\infty (e.g., by iterating the inequality). In particular, for all f ≥ 1 f\geq 1 ,

[281] table: y f ≤ max ⁡ { θ ∗ , log ⁡ ( 2 ​ n ) + θ ∗ 1 − α } \displaystyle y_{f}\leq\max\!\left\{\theta^{*},\,\frac{\log(2n)+\theta^{*}}{1-\alpha}\right\} = max ⁡ { θ ∗ , 2 ​ ( log ⁡ ( 2 ​ n ) + θ ∗ ) 1 − λ ¯ } < ∞ . \displaystyle=\max\!\left\{\theta^{*},\,\frac{2(\log(2n)+\theta^{*})}{1-\bar{\lambda}}\right\}<\infty.

[282] p: Finally, Jensen’s inequality (convexity of e θ ∗ ​ x e^{\theta^{*}x} ) yields

[283] table: 𝔼 ⁡ [ T f ] ≤ 1 θ ∗ ​ log ⁡ 𝔼 ⁡ [ e θ ∗ ​ T f ] = y f θ ∗ < ∞ , ∀ f ≥ 1 , \mathbb{E}[T_{f}]\leq\frac{1}{\theta^{*}}\log\mathbb{E}\!\left[e^{\theta^{*}T_{f}}\right]=\frac{y_{f}}{\theta^{*}}<\infty,\qquad\forall f\geq 1,

[284] p: which proves ( 25 ) and completes the proof of Theorem 6 .

[285] h2: VI Simulation

[286] p: In this section, we present simulation results to evaluate the performance of the proposed DFS algorithm with hierarchical Birkhoff–von Neumann decomposition.

[287] h3: VI-A Traffic Models

[288] p: In this subsection, we propose two server/GPU-level traffic models for simulation studies. The system consists of an m ​ n × m ​ n mn\times mn input-buffered crossbar switch, where n = 8 n=8 servers and each server contains m = 2 m=2 GPUs, resulting in a 16 × 16 16\times 16 switch fabric. As in our analysis, we assume Poisson arrivals as in (A1). Both models are specified via the arrival rate matrix

[289] table: r ( i , ℓ ) , ( j , k ) ≜ 𝔼 ⁡ [ a ( i , ℓ ) , ( j , k ) ​ ( t ) ] , r_{(i,\ell),(j,k)}\;\triangleq\;\mathbb{E}\big[a_{(i,\ell),(j,k)}(t)\big],

[290] p: where ( i , ℓ ) (i,\ell) denotes the ℓ \ell -th GPU (and NIC) in server i i , and a ( i , ℓ ) , ( j , k ) ​ ( t ) a_{(i,\ell),(j,k)}(t) is the number of packets that arrive at time slot t t and are destined from ( i , ℓ ) (i,\ell) to ( j , k ) (j,k) .

[291] p: Throughout, we focus on inter-server traffic and set all intra-server traffic rates to zero, i.e., r ( i , ℓ ) , ( i , k ) = 0 r_{(i,\ell),(i,k)}=0 for all i i and all ℓ , k ∈ { 1 , … , m } \ell,k\in\{1,\ldots,m\} . (Equivalently, the diagonal m × m m\times m blocks are zero.)

[292] p: Model U: Uniform GPU-to-GPU Traffic

[293] p: In the uniform traffic model, all inter-server GPU-to-GPU rates are identical:

[294] table: r ( i , ℓ ) , ( j , k ) U = { r 0 , i ≠ j , 0 , i = j , \displaystyle r^{\mathrm{U}}_{(i,\ell),(j,k)}\;=\;\begin{cases}r_{0},&i\neq j,\\ 0,&i=j,\end{cases} ∀ i , j ∈ { 1 , … , n } , ∀ ℓ , k ∈ { 1 , … , m } , \displaystyle\qquad\forall\,i,j\in\{1,\ldots,n\},\ \forall\,\ell,k\in\{1,\ldots,m\}, (35)

[295] p: where r 0 > 0 r_{0}>0 is chosen to achieve a prescribed offered load.

[296] p: Under Model U, the server-level aggregated rates

[297] table: λ i , j U ≜ 1 m ​ ∑ ℓ = 1 m ∑ k = 1 m r ( i , ℓ ) , ( j , k ) U \lambda^{\mathrm{U}}_{i,j}\;\triangleq\;\frac{1}{m}\sum_{\ell=1}^{m}\sum_{k=1}^{m}r^{\mathrm{U}}_{(i,\ell),(j,k)}

[298] p: satisfy λ i , j U = m ​ r 0 \lambda^{\mathrm{U}}_{i,j}=mr_{0} for i ≠ j i\neq j , and 0 0 otherwise. Thus, the aggregate traffic is also uniform across server pairs.

[299] p: Model NU: Non-Uniform (Server-Localized Hotspot) Traffic

[300] p: In the non-uniform traffic model, we intentionally create a per-server hotspot by concentrating all inter-server traffic of each server pair ( i , j ) (i,j) onto a single GPU pair, while preserving the server-level aggregate rates of Model U.

[301] p: Specifically, define

[302] table: r ~ ( i , ℓ ) , ( j , k ) NU = { m 2 ​ r 0 , ( i ≠ j ) ​ and ​ ( ℓ , k ) = ( 1 , 1 ) , 0 , otherwise . \tilde{r}^{\mathrm{NU}}_{(i,\ell),(j,k)}\;=\;\begin{cases}\displaystyle m^{2}r_{0},&(i\neq j)\ \text{and}\ (\ell,k)=(1,1),\\[5.69054pt] 0,&\text{otherwise}.\end{cases} (36)

[303] p: By construction, Model NU preserves the server-level aggregate rates:

[304] table: 1 m ​ ∑ ℓ = 1 m ∑ k = 1 m r ~ ( i , ℓ ) , ( j , k ) NU = 1 m ​ ∑ ℓ = 1 m ∑ k = 1 m r ( i , ℓ ) , ( j , k ) U = m ​ r 0 , \frac{1}{m}\sum_{\ell=1}^{m}\sum_{k=1}^{m}\tilde{r}^{\mathrm{NU}}_{(i,\ell),(j,k)}\;=\;\frac{1}{m}\sum_{\ell=1}^{m}\sum_{k=1}^{m}r^{\mathrm{U}}_{(i,\ell),(j,k)}\;=\;mr_{0}, (37)

[305] p: for all i , j i,j . Thus, Models U and NU have the same inter-server aggregate load, but Model NU exhibits extreme micro-level non-uniformity across GPUs/NICs within a server.

[306] figure: (a) Model U (b) Model NU Fig. 2: Mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] versus r 0 r_{0} with ( n , m ) = ( 8 , 2 ) (n,m)=(8,2) under (a) Model U and (b) Model NU. Curves compare DFS with hierarchical BvN decomposition with and without intra-server balancing (Sec. IV ). Each point is obtained from a fixed slot-horizon simulation with a warm-up period removed from statistics.

[307] h3: VI-B Schemes Compared

[308] p: We compare two variants of DFS with hierarchical BvN decomposition:

[309] p: No intra-server balancing: DFS with hierarchical BvN decomposition applied directly to the per-GPU backlog matrix.

[310] p: With intra-server balancing (Sec. IV ): DFS with intra-server traffic balancing applied at each frame boundary, followed by the same hierarchical BvN decomposition.

[311] p: Both variants use the same DFS mechanism; the only difference is whether intra-server balancing is enabled.

[312] h3: VI-C Simulation Settings and Metric

[313] p: All results are obtained using a fixed slot-horizon simulation to ensure fair comparisons between schemes that may induce different frame sizes. Unless otherwise stated, each run simulates 10 5 10^{5} time slots, and the first 10 4 10^{4} slots are treated as warm-up and excluded from statistics. We sweep r 0 r_{0} over [ 0.005 , 0.07 ] [0.005,0.07] for Model U and over [ 0.001 , 0.035 ] [0.001,0.035] for Model NU.

[314] p: We report the mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] , computed by averaging T f T_{f} over all frames observed within the simulated horizon after the warm-up period.

[315] h3: VI-D Results: Mean Frame Length Versus r 0 r_{0}

[316] p: Fig. 2 shows the mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] as a function of r 0 r_{0} for Models U and NU. For reference, under Model U per-port capacity condition corresponds to r 0 < 1 / ( ( n − 1 ) ​ m ) = 1 / 14 r_{0}<1/((n-1)m)=1/14 , while under Model NU without balancing it corresponds to r 0 < 1 / ( ( n − 1 ) ​ m 2 ) = 1 / 28 r_{0}<1/((n-1)m^{2})=1/28 .

[317] h4: VI-D 1 Model U (uniform micro-level traffic)

[318] p: In Fig. 2a , both schemes exhibit increasing mean frame length as r 0 r_{0} grows, with a rapid rise as r 0 r_{0} approaches 1 / 14 1/14 . Although Model U is uniform at the GPU-to-GPU rate level, enabling intra-server balancing still reduces 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] over the entire range of r 0 r_{0} . This suggests that balancing can reduce the mean frame length by smoothing within-block load variations caused by arrival randomness, even when the underlying rate matrix is uniform.

[319] h4: VI-D 2 Model NU (server-localized hotspot)

[320] p: In Fig. 2b , the no-balancing scheme suffers a much sharper increase in the mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] as r 0 r_{0} increases, which is consistent with the severe micro-level concentration of traffic onto the first GPU pair ( i , 1 ) → ( j , 1 ) (i,1)\!\to\!(j,1) for each inter-server pair ( i , j ) (i,j) . In contrast, enabling intra-server balancing (Sec. IV ) substantially reduces 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] over the entire sweep range and delays the onset of very large frames. Overall, Model NU clearly separates the two schemes: without balancing, hotspot-induced per-GPU stragglers inflate the frame length, whereas intra-server balancing redistributes traffic within each m × m m\times m server-pair block and significantly improves frame-size behavior.

[321] p: Moreover, Fig. 3 overlays the balanced cases for Models U and NU over the common range of r 0 r_{0} . The two curves nearly overlap, indicating that intra-server balancing effectively removes the micro-level non-uniformity in Model NU and yields frame-length behavior comparable to that of the uniform Model U.

[322] figure: Fig. 3: Mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] versus r 0 r_{0} with ( n , m ) = ( 8 , 2 ) (n,m)=(8,2) under intra-server balancing (Sec. IV ). The plot overlays Model U and Model NU over the common sweep range of r 0 r_{0} , showing that the two curves nearly overlap.

[323] h4: VI-D 3 Summary

[324] p: Across both traffic models, intra-server balancing consistently reduces the mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] . The improvement is especially pronounced under Model NU, where traffic is highly concentrated within each server pair. These results support the role of intra-server balancing (Sec. IV ) as a practical mechanism to enhance robustness of DFS with hierarchical BvN decomposition under heterogeneous GPU-level traffic patterns.

[325] h2: VII Conclusion

[326] p: This paper develops an online scheduling framework for all-to-all GPU communication in two-tier clusters with fast intra-server links and a slower inter-server fabric. Building on the dynamic frame sizing (DFS) principle, we propose a dynamic hierarchical Birkhoff–von Neumann (BvN) decomposition that exploits the n n -server structure to avoid the prohibitive cost of directly decomposing an m ​ n × m ​ n mn\times mn GPU-level matrix. At each frame boundary, we additionally perform a simple intra-server traffic balancing step using only local unit-transfer operations, reshaping each m × m m\times m server-pair block to reduce micro-level (GPU/NIC-level) skew while preserving the aggregate server-to-server demand.

[327] p: On the theoretical side, we (i) characterize a completion-time lower bound induced by per-port capacities, (ii) show that intra-server balancing does not increase this bound and can reduce it by equalizing per-GPU outgoing/incoming loads within each server pair, and (iii) establish a DFS stability guarantee under admissible Poisson arrivals expressed in terms of server-level aggregate loads. On the empirical side, simulations under both a uniform micro-level model (Model U) and a server-localized hotspot model (Model NU) show that balancing consistently reduces the mean frame length 𝔼 ⁡ [ T f ] \mathbb{E}[T_{f}] , with particularly large gains under hotspot traffic; after balancing, the frame-length behavior under Model NU closely matches that under Model U, indicating effective removal of micro-level non-uniformity.

[328] p: Overall, the results suggest that combining hierarchical decomposition with lightweight intra-server balancing yields a practical and robust approach to scheduling large-scale all-to-all transfers under per-port matching constraints. Future work includes extending the framework to more realistic fabrics and traffic primitives, such as multi-hop interconnects, heterogeneous link rates, variable packet sizes, and additional topology constraints, as well as developing online/learning-based estimation of the aggregated server-level traffic matrix to further reduce control overhead.

[329] h2: References

[330] figure: Yen-Chieh Wu received the B.S. degree in electrical engineering in 2024 from National Tsing Hua University, Hsinchu, Taiwan. He is currently pursuing the M.S. degree in the Institute of Communications Engineering, National Tsing Hua University, Hsinchu, Taiwan. His research interests include communication network scheduling and large language model (LLM) agents.

[331] figure: Cheng-Shang Chang (S’85-M’86-M’89-SM’93-F’04) received the B.S. degree from National Taiwan University, Taipei, Taiwan, in 1983, and the M.S. and Ph.D. degrees from Columbia University, New York, NY, USA, in 1986 and 1989, respectively, all in electrical engineering. From 1989 to 1993, he was employed as a Research Staff Member with the IBM Thomas J. Watson Research Center, Yorktown Heights, NY, USA. Since 1993, he has been with the Department of Electrical Engineering, National Tsing Hua University, Taiwan, where he is a Tsing Hua Distinguished Chair Professor. Dr. Chang served as an Editor for Operations Research from 1992 to 1999, an Editor for the IEEE/ACM TRANSACTIONS ON NETWORKING from 2007 to 2009, and an Editor for the IEEE TRANSACTIONS ON NETWORK SCIENCE AND ENGINEERING from 2014 to 2017. He is currently serving as an Editor-at-Large for the IEEE/ACM TRANSACTIONS ON NETWORKING . He received an IBM Outstanding Innovation Award in 1992, an IBM Faculty Partnership Award in 2001, and Outstanding Research Awards from the National Science Council, Taiwan, in 1998, 2000, and 2002, respectively. He received the Merit NSC Research Fellow Award from the National Science Council, R.O.C. in 2011. He also received the Academic Award in 2011 and the National Chair Professorship in 2017 and 2023 from the Ministry of Education, R.O.C. He is the recipient of the 2017 IEEE INFOCOM Achievement Award.

[332] figure: Duan-Shin Lee (S’89-M’90-SM’98) received the B.S. degree from National Tsing Hua University, Taiwan, in 1983, and the MS and Ph.D. degrees from Columbia University, New York, in 1987 and 1990, all in electrical engineering. He worked as a research staff member at the C&C Research Laboratory of NEC USA, Inc. in Princeton, New Jersey from 1990 to 1998. He joined the Department of Computer Science of National Tsing Hua University in Hsinchu, Taiwan, in 1998. Since August 2003, he has been a professor. He received a best paper award from the Y.Z. Hsu Foundation in 2006. He served as an editor for the Journal of Information Science and Engineering between 2013 and 2015. He is currently an editor for Performance Evaluation. Dr. Lee’s current research interests are network science, game theory, machine learning and high-speed networks. He is a senior IEEE member.

[333] figure: H. Jonathan Chao (Life Fellow, IEEE) received the B.S. and M.S. degrees in electrical engineering from National Chiao Tung University, Taiwan, in 1977 and 1980, respectively, and the Ph.D. degree in electrical engineering from The Ohio State University, Columbus, OH, USA, in 1985. In January 1992, he joined New York University (NYU), where he is currently a Professor of electrical and computer engineering (ECE). He was the Head of the Department from 2004 to 2014. He is also the Director of the High-Speed Networking Laboratory, where he is conducting research in the areas of AI datacenter designs to accelerate AI training and inference, dynamic multi-path load balancing, routing and scheduling, high-speed packet processing/switching/routing, software-defined networking, network security, and network on chip. From 2000 to 2001, he was the Co-Founder and the CTO of Coree Networks, Tinton Falls, NJ, USA. From 1985 to 1992, he was a member of Technical Staff at Bellcore, Piscataway, NJ, USA, where he was involved in transport and switching system architecture designs and application-specified integrated circuit implementations, such as the world’s first SONET-like framer chip, ATM layer chip, sequencer chip (the first chip handling packet scheduling), and ATM switch chip. He has co-authored three networking books, Broadband Packet Switching Technologies—A Practical Guide to ATM Switches and IP Routers (New York: Wiley, 2001), Quality of Service Control in High-Speed Networks (New York: Wiley, 2001), and High-Performance Switches and Routers (New York: Wiley, 2007). He holds 63 patents and has published more than 300 journals and conference papers. He is a Fellow of the National Academy of Inventors. He was a recipient of the Bellcore Excellence Award in 1987. He was a co-recipient of the 2001 Best Paper Award from IEEE TRANSACTION ON CIRCUITS AND SYSTEMS FOR VIDEO TECHNOLOGY .

[334] h2: Instructions for reporting errors

[335] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[336] p: Tip: You can select the relevant text first, to include it in your report.

[337] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[338] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
