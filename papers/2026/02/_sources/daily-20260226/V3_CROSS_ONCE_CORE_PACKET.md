## 2602.20450v1

原文精确HTML：https://arxiv.org/html/2602.20450v1；机械抽取的原始paragraph（不以作者摘要代原文）。

Terraform’s hierarchical selection takes inspiration from the Classification and Regression Trees (CART) algorithm, which constructs a binary decision tree by recursively partitioning data at each node into left and right child nodes based on a partitioning criterion.
For classification tasks, well-known partitioning criteria like Gini index and Entropy Hastie et al. (2001) are employed, whereas for regression tasks, the Sum of Squared Errors (SSE) method is used.
For example, assume a regression problem that needs to generate a CART decision tree.
The partition at each node  n_{i}  of the tree, where  n_{i}\in\{1,\ldots,N\}  is determined using the total SSE of the resulting child nodes defined as  \text{SSE}(N_{L})  and  \text{SSE}(N_{R}) .
It equates to,  \text{SSE}(N_{L})=\sum_{n_{i}\in N_{L}}(n_{i}-\bar{n}_{L})^{2} , where  \bar{n}_{L}  represents the mean of the left partition; and similarly for the right partition.
CART selects the partition that minimizes the total SSE for each node,  \text{SSE}_{\text{total}}=\text{SSE}(N_{L})+\text{SSE}(N_{R}) .

Prior to calculating the split index, Terraform sorts the clients based on the magnitude of their gradient updates  |\Delta w^{k}_{r,t}| .
Once the clients are sorted, their dataset sizes,  |D^{k}_{train}| , are used to calculate the running sum,  S_{k}=\sum_{j=1}^{k}|D_{\text{train}}^{j}| , where  S_{k}  denotes the cumulative dataset size up to the  k -th client in the list.
This running sum is used to identify a subset of clients that can optimize the calculation of the split index, which we denote as the Inter-Quartile Range (IQR).

In Table 2, we evaluate Terraform on  8  FMNIST scenarios.
As scenarios 1, 2, and 3 are ported from HiCS-FL, we force Terraform to sample only  5  clients initially.
Consequently, Terraform is able to run only one iteration per round, which is same as running Random; thus, similar accuracies.
For rest of the scenarios, Terraform does not have this restriction, and thus, it continues outperforming other methodologies.
One exception, however, is scenario 3*, where Terraform is the second-best because sampling even  15  clients initially, in each round, is not sufficient;
we hypothesize that Terraform needs to sample a much higher number of clients.

Terraform’s gradient updates are, in essence, a combination of the weights and biases from the clients’ models’ final layers.
In Figure 2, we illustrate the accuracy of Terraform when, instead of using gradient updates, it uses (i) loss, (ii) biases, and (iii) weights.

In Figure 3, on the CIFAR100 and Tiny ImageNet datasets for  100  rounds, we compare IQR (Q1, Q3) against three other splitting ranges:
(0, 1), (0, Q3), and (Q1, 1).
Our results illustrate that IQR is not only sufficient for determining split index  \tau_{split} , but also helps to discard outliers that reduce the test accuracy.
Additionally, (Q3, 1) have the poorest performance, which validates the theory that hyper-focusing on only highly heterogeneous clients overfits the model and reduces generalization.

## 2602.20981v1

原文精确HTML：https://arxiv.org/html/2602.20981v1；机械抽取的原始paragraph（不以作者摘要代原文）。

Temporal routing layers.
In temporal data e.g., audio and video events, the boundaries occur when there are contextual shifts between sound events. Based on this observation, we opt to mask tokens that have high similarities and keep the tokens that contain distinct temporal information. Let  {\bm{q}}_{\ell}={\bm{W}}_{q}{\bm{x}}_{\ell}  and  {\bm{k}}_{\ell}={\bm{W}}_{k}{\bm{x}}_{\ell} , we use cosine similarity in computing token selection:

MM routing layers.
Multimodal alignment between one and another modality (i.e.,  M  and  M^{\prime} ) might experience deteriorating behavior due to a large number of tokens to be processed. Selected important tokens for feed forwarding to main networks are tokens with high similarity to the referenced modality. For instance, synchronized audio-visual (i.e. Synchformer [20]) features could be used to align with text condition. Let  {\bm{q}}_{M_{\ell}}={\bm{W}}_{q}{\bm{x}}_{M_{\ell}}  and  {\bm{k}}_{M^{\prime}_{\ell}}={\bm{W}}_{k}{\bm{x}}_{M^{\prime}_{\ell^{\prime}}} , we compute MM routing as follows:

Hierarchical Vs. Non-Hierarchical methods.
We ablate on having the structure of models with tokens in the compressed space with tokens in the original space via routing mechanisms. We observe that the model with compressed space yields a better alignment between modalities in long audio generation forms in Table 4.

Ablation on routing strategies.
We ablate on having the structure of temporal and MM routing in our proposed network structure as shown in Table A6. We observe that the model with a temporal routing mechanism could improve DeSync scores, which are related to temporal synchronization between audio and visual modalities.

Ablation on additional position embeddings for the temporal sync. condition. Beyond the current framework, we also conducted an experiment to assess the impact of positional embeddings. Specifically, we examined whether removing them would degrade performance and whether our design choice could be justified. As shown in Table A7, the use of positional embeddings has minimal impact on overall performance.

## 2602.21092v1

原文精确HTML：https://arxiv.org/html/2602.21092v1；机械抽取的原始paragraph（不以作者摘要代原文）。

For each graph, we consider two different variations: topologically informative edge features and random edge features. In the case of topologically informative edge features, we attribute to each edge a scalar edge feature based on its location on the graph as described in Table 1. For random edge features, we randomly permute the edge features previously attributed to all edges. In this way, we maintain the distribution of features, but each edge is randomly assigned a feature. In both cases, the edge features are uninformative with respect to the task content as they do not contain information with regard to the message being passed. However, the topological correct features do discern between “useful” and “non-useful” edges for message-passing.

Using the formula for the Balanced Forman Curvature ( BFc ) we can compute that the bridge edge in the barbell graph has a negative curvature22
              2
              
              
              
              
              
              
              
            For a barbell with cliques of size  k , the bridge nodes have degree  k  (connecting to  k-1  nodes in the clique and a bridge neighbor). Since no triangle or  4 -cycles are formed, the  BFc  reduces to  \frac{4}{k}-2 , which is negative for any non-trivial clique.. These bridge edges are important from a geometic perspective, as a negative curvature is a measure for a topological bottleneck (making the important distinction that this does not necessarily imply a computational bottleneck/oversquashing (Arnaiz-Rodriguez and Errica, 2025)). By analyzing the activation ratios developed during learning on these graphs, we analyze whether a learned attention mechanism also recognizes the relevance of these edges.

In layer 2, where the bridge edge plays a crucial role in the transport of information from the source clique to the target clique, we see that in three cases (Figure 2, panel c., e, and f.) the activation ratios are significantly higher for the bridge edge relevant to the task than for the dummy bridges. In the case of the modified barbell with topological edge features (Figure 2 panel b.), both median values are similar, but the bridge edge ratios show larger variance. This low variance of the dummy bridges occurs for each of the four cases at layer 2. The Graph Transformer model has therefore learned which bottleneck matters, not that bottlenecks matter.
This variance asymmetry between task-relevant and -irrelevant bridges suggests that activations depend on the actual signal content, responding differently based on the signal being propagated. In contrast, dummy bridge activations remain stable across instances, consistent with the fact that they do not carry information relevant to the task. This pattern persists for both the topologically accurate and permuted edge features, indicating that the behavior is not driven by the edge feature distribution, where the sparser features are signaled regardless of the topology or task.
Additionally, we note a second pattern from the edges of the internal cliques (Cl-Cl). Despite having no crucial role in information transfer between cliques, these edges show the highest outlier values for the activation ratio. The Cl-Cl edges are the most abundant in the graph and could play the role of attention sinks (Xiao et al., 2024), where the model can deposit the attention mass.

In barbell experiments, we find that even edges identified as topologically important by curvature are discerned based on their activation values at the critical information layer (i.e., layer 2). Additionally, since in this experiment we replicate 256 identical graphs, our findings reveal that activation variance distinguishes between task-relevant and -irrelevant edges that are topologically identical. However, the highest outliers in activation values (MAs) concentrate on abundant intra-clique edges at this critical layer, rather than task-relevant bridges. Through these controlled experiments, we establish that MAs do not necessarily track curvature-identified bottlenecks, but that topologically identical edges can be discerned by graph transformers based on their task relevance. In the next section, we extend our analysis beyond the topologically limited barbell graphs and study the activation behavior across diverse molecular datasets.

## 2602.21078v1

原文精确HTML：https://arxiv.org/html/2602.21078v1；机械抽取的原始paragraph（不以作者摘要代原文）。

However, as summarized in Obs. 1, simply averaging the local proxies is prone to be affected by the outliers due to external heterogeneity. Therefore, we first initialize the global proxies  \mathbf{\Omega}_{\mathcal{G}}  with  \overline{\mathbf{\Omega}}_{\mathcal{G}}  and then further fine-tune  \mathbf{\Omega}_{\mathcal{G}}  on the server by leveraging the off-the-shelf uploaded local proxies  \{\mathcal{\omega}_{m}^{c}\}_{c=1}^{C},~\forall~\mathcal{C}_{m}\in\mathbb{C}_{M} . More concretely, for the global proxy  {\mathbf{\Omega}_{\mathcal{G}}^{c}}  of category  c , our objective is to pull it closer to all local proxies belonging to category  c  and push it away from local proxies of other categories. The optimization objective of  \mathbf{\Omega}_{\mathcal{G}}  is defined as:

We first construct its category set for each sample in local client as follows: I. Labeled Samples. As shown in Fig. 3 upper right, for a labeled sample  \mathbf{x}_{i} , its category set is defined by its ground-truth as  \xi_{i}=\{\mathbf{y}_{i}\} , which is a single-element set; II. High-Confidence Unlabeled Samples. In Fig. 3 middle right, if  \max(\overline{\mathbf{y}}_{i})>\tau ,  \mathbf{u}_{i}  is a high-confidence sample (denoted as  \mathbf{u}_{i}^{\texttt{{hc}}} ) with its pseudo-label  \hat{\mathbf{y}}_{i}=\arg\max(\overline{\mathbf{y}}_{i}) . Here, we define its category set  \xi_{i}=\{\hat{\mathbf{y}}_{i}\}  as a single-element set like I;
III. Low-Confidence Unlabeled Samples. In Fig. 3 lower right, if  \max(\overline{\mathbf{y}}_{i})\leq\tau ,  \mathbf{u}_{i}  is regarded as a low-confidence sample, denoted as  \mathbf{u}_{i}^{\texttt{{lc}}} . For  \mathbf{u}_{i}^{\texttt{{lc}}} , a simple low-confident pseudo-label may affect model performance due to the potential labeling errors. Prior study [2] shows the effectiveness of assigning more than one category labels to ambiguous ROI candidates. Thus, we leverage the several categories among which the model hesitates to represent its possible labels for  \mathbf{u}_{i}^{\texttt{{lc}}} , defined as indecisive-categories set  {\xi}_{i} , e.g., {mouse, hamster} in Fig. 4(a-b). To better determine  \xi , we dynamically maintain a global category prior  \mathcal{P}_{\mathcal{G}}^{\prime}(\mathbf{Y})  to constrain the indecisive categories for  \mathbf{u}_{i}^{\texttt{{lc}}} :

2) Negative Proxies Set. For an unlabeled sample  \mathbf{u}_{i}  from batch  \mathcal{B} , any other sample  j  in  \mathcal{B}  (including  \mathbf{x}_{j} / \mathbf{u}_{j}^{\texttt{{hc}}} / \mathbf{u}_{j}^{\texttt{{lc}}} ) will be considered as one of the negative-proxy candidates as long as its category set  \xi_{j}  does not overlap with  \xi_{i} , i.e.,

I. Design of including low-confidence samples An intuitive idea to include low-confidence samples  \mathbf{u}^{\textit{{lc}}}  is to directly assign pseudo-labels for them like high-confidence samples, abbreviated as LPL-ALL and GPL-ALL. FedAvg-SL, the standard fully-labeled FedAvg, serves as an upperbound with correct labels. As shown in Tab. 4 upper, in most cases, directly including  \mathbf{u}^{\textit{{lc}}}  (w/-ALL) could bring slight improvements compared to simply-discarding (w/o-ALL), suggesting that  \mathbf{u}^{\textit{{lc}}}  contain some valuable information and simply discarding them may exclude some correctly-labeled samples from training; But, directly including them sometimes leads to performance degradation, e.g., LPL & LPL-ALL on SVHN. Compared to discarding or directly including  \mathbf{u}^{\textit{{lc}}} , our proposed ICPL module achieves better performance across all datasets by more accurately constructing the relationships between samples in the positive-negative pool of ICPL. Moreover, ICPL even reaches the performance of FedAvg-SL on certain datasets.

III. Indecisive-categories set  \xi  vs. pseudo-label
We further validate the superiority of  \xi  over pseudo-labels for low-confidence unlabeled samples  \mathbf{u}^{\textit{{lc}}} . Intuitively, a set with multiple categories has higher probability to cover correct category than a single pseudo-label.
To this end, we plot ’correct category in  \xi ’ and ’correct pseudo-label’ ratios on  \mathbf{u}^{\textit{{lc}}} . As shown in Fig. 6, the recall of  \xi  remains at a considerably high level, significantly outperforming the accuracy of pseudo-labeling even throughout the training process. Although this set-based supervision is not as precise as the ground-truth, it effectively introduce more available  \mathbf{u}^{\textit{{lc}}}  rather than compromise on wrong pseudo-labels
