# B24 — 六项必要原证 / actual owner；本次独立复核已落实

2026-10-06 feb26_close_oct06 非原packet作者从raw重新定位全所引必要pID；另读20450原6.2累计weighted IQR/variance/stop、20981相反temporal/MM选择、21078原目标/tune与SVHN反側、21039absolute/excess测试条件。旧owner坐标漂移重新定位：20981实际Ch23 902–908/1044–1048，20673实际Ch24 54–62；并实际读Ch36local参数/optimizer、Ch27删除/修正/独立验收、Ch5 253–266阶梯、Ch4capacity/优化/泛化。20981/21092/20673具体已有覆盖；20450/21078/21039受限client统计/类别支集/测试条件仅报告，不复制有限recipe、不授privacy/物理/全部theorem。原人口/费用/反侧/ND保留，未改Books、未运行artifact/复现，非日级验收。

## 2602.20450v1
https://arxiv.org/html/2602.20450v1

S6.SS2.SSS2.p3.1 | This splitting to determine hard clusters is hierarchically repeated until one of these termination conditions is met: (i) reaching the minimum client threshold, \eta , or (ii) maximum iteration depth, T . The model then begins the next round with a randomly sampled set of clients. In the following section, we present the complete procedure in Algorithm 1.

S7.SS1.p4.1 | In Table 2, we evaluate Terraform on 8 FMNIST scenarios. As scenarios 1, 2, and 3 are ported from HiCS-FL, we force Terraform to sample only 5 clients initially. Consequently, Terraform is able to run only one iteration per round, which is same as running Random; thus, similar accuracies. For rest of the scenarios, Terraform does not have this restriction, and thus, it continues outperforming other methodologies. One exception, however, is scenario 3*, where Terraform is the second-best because sampling even 15 clients initially, in each round, is not sufficient; we hypothesize that Terraform needs to sample a much higher number of clients.

S7.SS2.SSS2.p2.1 | In Figure 3, on the CIFAR100 and Tiny ImageNet datasets for 100 rounds, we compare IQR (Q1, Q3) against three other splitting ranges: (0, 1), (0, Q3), and (Q1, 1). Our results illustrate that IQR is not only sufficient for determining split index \tau_{split} , but also helps to discard outliers that reduce the test accuracy. Additionally, (Q3, 1) have the poorest performance, which validates the theory that hyper-focusing on only highly heterogeneous clients overfits the model and reduces generalization.

## 2602.20981v1
https://arxiv.org/html/2602.20981v1

S4.SS4.p3.1 | Temporal routing layers. In temporal data e.g., audio and video events, the boundaries occur when there are contextual shifts between sound events. Based on this observation, we opt to mask tokens that have high similarities and keep the tokens that contain distinct temporal information. Let {\bm{q}}_{\ell}={\bm{W}}_{q}{\bm{x}}_{\ell} and {\bm{k}}_{\ell}={\bm{W}}_{k}{\bm{x}}_{\ell} , we use cosine similarity in computing token selection:

S4.SS4.p4.2 | We only process tokens with b_{\ell}=\mathbbm{1}_{\{\texttt{sim}({\bm{q}}_{\ell},{\bm{k}}_{\ell^{\prime}})\geq 0.5\}} . As conditions are from the pretrained models (e.g., Synchformer [20], visual CLIP [37], and text CLIP [37] ), we expect a higher probability for token matching scores (i.e., > 0.5).

S7.p2.1 | Evaluation datasets. For the UnAV100 benchmark, we utilize the official test set provided by UnAV100 in its original form, without introducing any modifications. During the evaluation phase, captions are deliberately withheld for all instances within this set. This design ensures that the task remains strictly focused on video-to-audio generation, eliminating any dependency on textual inputs and thereby preserving the video-to-audio evaluation setting. For the LongVale datasets, the original evaluation sets predominantly consist of short video clips, many of which have audio segments shorter than one minute. To address this limitation and create a more balanced evaluation scenario, we selectively sample additional videos from the training split of LongVale [11] and eliminate short videos from the original test set. These selected videos are incorporated into the evaluation set to increase diversity and length. As a result of this augmentation, the final evaluation set comprises around 1K videos, each averaging approximately 45 seconds in duration. This adjustment ensures a more representative and robust evaluation for tasks involving video-to-audio generation.

S9.p2.1 | Ablation on routing strategies. We ablate on having the structure of temporal and MM routing in our proposed network structure as shown in Table A6. We observe that the model with a temporal routing mechanism could improve DeSync scores, which are related to temporal synchronization between audio and visual modalities.

Table4原机械段：
↓
\downarrow
Non-Hierarchical
11.76
442.12
2.59
2.29
26.34
0.669
Hierarchical
10.10
323.39
3.68
3.50
30.62
0.438
Table 4
:
Comparison of non-hierarchical and hierarchical methods.

## 2602.21078v1
https://arxiv.org/html/2602.21078v1

Thmremark1.p3.1 | 2) Negative Proxies Set. For an unlabeled sample \mathbf{u}_{i} from batch \mathcal{B} , any other sample j in \mathcal{B} (including \mathbf{x}_{j} / \mathbf{u}_{j}^{\texttt{{hc}}} / \mathbf{u}_{j}^{\texttt{{lc}}} ) will be considered as one of the negative-proxy candidates as long as its category set \xi_{j} does not overlap with \xi_{i} , i.e.,

S6.SS1.p2.1 | Implementation details Following SAGE [21], we configure 20 clients for all settings, with 8 clients randomly sampled each round to participate in the federated training. ResNet-8 [9] serves as the local backbone, with the number of local epochs set to 5, local learning rate set to 0.1 and the confidence threshold \tau for pseudo-labeling set to 0.95. For global proxy tuning process, the learning rate is 0.005, and the number of tuning epochs is set to 10 for CIFAR-100 and 100 for the other datasets. Unless otherwise specified, the experimental setup of ProxyFL is consistent with SAGE (More details in Appendix. D).

S6.SS3.p10.1 | I. Design of including low-confidence samples An intuitive idea to include low-confidence samples \mathbf{u}^{\textit{{lc}}} is to directly assign pseudo-labels for them like high-confidence samples, abbreviated as LPL-ALL and GPL-ALL. FedAvg-SL, the standard fully-labeled FedAvg, serves as an upperbound with correct labels. As shown in Tab. 4 upper, in most cases, directly including \mathbf{u}^{\textit{{lc}}} (w/-ALL) could bring slight improvements compared to simply-discarding (w/o-ALL), suggesting that \mathbf{u}^{\textit{{lc}}} contain some valuable information and simply discarding them may exclude some correctly-labeled samples from training; But, directly including them sometimes leads to performance degradation, e.g., LPL & LPL-ALL on SVHN. Compared to discarding or directly including \mathbf{u}^{\textit{{lc}}} , our proposed ICPL module achieves better performance across all datasets by more accurately constructing the relationships between samples in the positive-negative pool of ICPL. Moreover, ICPL even reaches the performance of FedAvg-SL on certain datasets.

## 2602.21092v1
https://arxiv.org/html/2602.21092v1

S4.SS1.SSS0.Px1.p1.1 | We train a 3-layer local Graph Transformer to reconstruct the signal from the source node to the target node. As the two nodes are 3 hops away, a 3-layer model should propagate the information required to solve this task. For each version of the barbell graph, we generate 256 graphs with node features as described above. The source and target nodes are identical for every graph, and the random edge features are permuted differently for each graph. Once trained, we extract the activations following the analysis in (Bini et al., 2024), normalizing them based on the median per layer. The activation ratios are collected on a test dataset comprising 26 graphs (representing 10\% of the train set). The final train and MSE loss test are reported in Table 2, showing that the model has solved the task reasonably well (reaching a test of MSE \approx 0.2 – 0.3 ).

S4.SS1.SSS0.Px2.p2.1 | In layer 2, where the bridge edge plays a crucial role in the transport of information from the source clique to the target clique, we see that in three cases (Figure 2, panel c., e, and f.) the activation ratios are significantly higher for the bridge edge relevant to the task than for the dummy bridges. In the case of the modified barbell with topological edge features (Figure 2 panel b.), both median values are similar, but the bridge edge ratios show larger variance. This low variance of the dummy bridges occurs for each of the four cases at layer 2. The Graph Transformer model has therefore learned which bottleneck matters, not that bottlenecks matter. This variance asymmetry between task-relevant and -irrelevant bridges suggests that activations depend on the actual signal content, responding differently based on the signal being propagated. In contrast, dummy bridge activations remain stable across instances, consistent with the fact that they do not carry information relevant to the task. This pattern persists for both the topologically accurate and permuted edge features, indicating that the behavior is not driven by the edge feature distribution, where the sparser features are signaled regardless of the topology or task. Additionally, we note a second pattern from the edges of the internal cliques (Cl-Cl). Despite having no crucial role in information transfer between cliques, these edges show the highest outlier values for the activation ratio. The Cl-Cl edges are the most abundant in the graph and could play the role of attention sinks (Xiao et al., 2024), where the model can deposit the attention mass.

## 2602.20673v1
https://arxiv.org/html/2602.20673v1

S3.SS3.p3.1 | The generation of novel trajectory views begins from a camera pose with a known image (recorded or generated). For each segment, the first conditioning frame is this known image, which ensures temporal consistency, while the remaining conditioning frames are the corresponding pseudo-views that provide geometric and appearance guidance for the target viewpoints. Once a segment is completed, its final generated frame becomes the first conditioning frame for the next segment, and the process repeats. During training, the first conditioning frame is the ground-truth frame from the recorded trajectory, while the remaining conditioning frames are simulated pseudo-views synthesized via the pipeline in Sec. 3.4. Please see the supplementary materials for more details.

S3.SS4.p1.1 | We propose a pseudo-view simulation pipeline that simulates the characteristic patterns observed in novel pseudo-views, enabling us to train our segment-wise video diffusion model directly on single-trajectory datasets. This eliminates the need for multi-trajectory recordings, which are unavailable in public driving datasets since a vehicle cannot traverse multiple paths simultaneously.

S4.SS4.p1.1 | Our method relies on 4D geometry reconstruction from OmniRe. While the Gaussian reconstruction backbone may introduce minor geometric inaccuracies because of rolling shutter distortion, particularly during high-speed driving, our diffusion model demonstrates strong robustness to such imperfections and still produces high-quality results. Additionally, our current framework focuses on appearance editing rather than geometry editing. Future work could explore integrating rolling shutter correction into the 3DGS rasterizer and extending the framework to support geometry editing capabilities.

## 2602.21039v1
https://arxiv.org/html/2602.21039v1

S3.p2.1 | We will show that the testing component can require \Omega\mathinner{\left(k/\epsilon^{2}\right)} samples. Due to this high testing overhead, it is more efficient to learn each distribution separately whenever d\ll 1/\epsilon . To address this, Algorithm 1 incorporates a preliminary check to determine if separate learning yields better complexity.

S3.SS1.p2.4 | Consequently, f^{(t)} is 2\epsilon^{\prime} -optimal for at least half of the distributions in \mathcal{U}^{(t-1)} .

S4.SS1.SSS0.Px2.p3.1 | This bound highlights a natural trade-off: in the low-precision regime where \epsilon\gg 1/d , the agnostic testing approach ( 1/\epsilon^{2} ) is superior. However, in the high-precision regime where \epsilon\ll 1/d , exploiting the supervised structure of the data via the learning-augmented approach ( d/\epsilon ) yields an improvement.

S4.SS2.p3.1 | However, a fundamental obstacle remains: we do not know f^{*} . Although we know its population error is \err\mathinner{\left(f^{*};P\right)}=1/4 , we cannot readily use its empirical error \emperr\mathinner{\left(f^{*};S\right)} as a reference point because the concentration of \mathinner{\!\left\lvert\err\mathinner{\left(f^{*};P\right)}-\emperr\mathinner{\left(f^{*};S\right)}\right\rvert} is slow, scaling with \tilde{O}\mathinner{\left(1/\sqrt{\mathinner{\!\left\lvert S\right\rvert}}\right)} . Notably, the ERM sample size of \tilde{O}\mathinner{\left(d/\epsilon\right)} ensures uniform convergence of the excess risks (the offset counterparts), but not of the absolute errors \mathinner{\!\left\lvert\err\mathinner{\left(f;P\right)}-\emperr\mathinner{\left(f;S\right)}\right\rvert} .

Theorem4.3原TeX（fixed binary RCN 1/4 setting）：
T_{\mathsf{SHT}}\mathinner{\left(\epsilon,\delta\right)}=O\mathinner{\left(\log\mathinner{\left(\frac{1}{\delta}\right)}\min\mathinner{\left\{\frac{1}{\epsilon^{2}},\frac{d}{\epsilon}\right\}}\right)}

## actual owner — books/part-04-training-system/36-distributed-training.md

L76–83:

另一条分支并非每个 rank 独立计算并应用 local gradient：各 rank 保留不同 `θ_r`，每一步仍 All-Reduce 共享梯度，再周期性平均参数。因此共享梯度是在不同参数点求得，不能按普通同步 SGD 或独立 Local SGD 的同一更新语义恢复。Checkpoint 应绑定各 rank 参数、optimizer state、共享梯度轮次与参数平均 cadence。<!-- source-family:SF-2026-ARXIV-2604-24708 -->

该选择用参数多样性换额外优化状态与一致性复杂度，周期平均仍有通信，恢复不一致也会改变后续轨迹。证据只来自单推荐任务、单 epoch 设置，不证明 LLM 收敛或任意同步间隔有效；质量漂移、状态无法恢复或协调成本超过收益时，回退共同参数点的同步 SGD 或有明确 local-gradient 合同的 Local SGD。

去中心化的 adaptive local updates 还要明确通信的共识对象。每个节点可以保留自己的 momentum、二阶矩与本地参数，连续推进若干步后，只发送相对于已重构模型估计的压缩差值；邻居据此更新各自的模型估计，再作 gossip correction。被压缩的是模型重建增量，不是一个共同 Adam 的原始梯度；节点的 optimizer history 与邻居共识估计因此是两组需要分别恢复的状态。Checkpoint 必须绑定本地步数、moments、重建估计、compressor 与 mixing revision，否则只恢复参数会改变下一轮更新。

这减少同步与传输，却叠加 local drift、压缩误差和拓扑混合误差；有偏但 contractive 的压缩器也只有在相应假设下可用。作者的有界、独立无偏随机梯度、固定连通 mixing、特定 adaptive 参数及步长条件不覆盖任意 Adam、动态故障网络或重尾梯度。小型 GPT 的四 A100 与 CPU 视觉实验支持受限可执行性，通信轮数或字节节省不等于生产 wall-clock 加速。收敛偏离、估计不同步或恢复无法保持身份时，应缩短 local interval、减弱压缩或回退同步完整状态；下一章的 tensor partition 不能替本协议证明 optimizer 等价。

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L890–896:
## Token Hierarchy 可以承载不同时间尺度

音频等高带宽模态若只用单层离散码，要么语义结构过粗，要么 token rate 过高。分层 residual quantization 可以让上层 code 承担长程语义和结构，下层 code 补局部声学细节；相应生成器也可分为 global sequence model、local refinement 与连续 decoder。

层次化表示提高可控性，却引入 codebook synchronization、跨层 error propagation 和更复杂的 bitrate/latency 预算。它是表示分解，不证明某个公开音乐模型的质量结论可外推；Ch24 只接手后续生成与修正机制。

高频触觉进一步说明“同一时间轴”不等于“同一采样密度”。接触事件稀疏时，复制成 dense visual stream 会浪费预算并稀释信号；更合适的 contract 是为 tactile event 保存独立 rate、timestamp、sensor calibration 与稀疏预测目标，再由共享语义层消费。代价是异步对齐、漂移和缺失事件，传感器或 embodiment 改变时不能继承旧 token identity。

L1032–1036:
固定 token budget 下，纯视觉重要性排序会忽略音频已经解释掉的画面。audio-guided selection 先估计跨模态冗余，再
保留音频无法替代的视觉 token，并在时间轴上合并相近状态。收益是把预算分给互补信息，代价是音频预测器偏差、
同步误差与关键静默画面被误删；音频缺失、噪声大或安全任务要求完整视觉 provenance 时，应回退单模态保守保留。
现有证据仅支持作者六个 audio-visual benchmarks 与受测模型。


## actual owner — books/part-04-training-system/27-data.md

L318–324:
### 从删除坏监督到尝试纠正监督

过滤发现坏监督后，删除是最简单的干预：它减少错误样本的梯度，也移除了该输入上的监督机会。纠正标签或回答则保留输入支持、为相同问题提供正面目标，因此“哪些样本导致风险”与“删掉哪些样本最能修复风险”不是同一个问题。若要比较两者，应固定可疑 rows 与训练预算，保留 raw、delete、corrective rewrite、等长度 paraphrase 和 clean-data 对照，区分语义修正、额外文本变化及样本量效应；可解析的格式和表面无害不是行为 canary。

纠正还会引入生成器偏差、错误修复和任务能力损失，必须保存原 row、修复版本与 generator lineage，再用独立行为切片验收。[受限 emergent-misalignment 微调对照](https://arxiv.org/html/2609.37624v1)只支持“纠正与删除可能不同”的设计分支；它的部分结果不确定，纠正相对 clean 的额外收益也未跨配置稳定成立。不能据此把自动改写设为普遍安全策略。来源可验证、修复可检查时才尝试纠正；风险不明、监督难以恢复时，隔离/删除及可靠 clean-data 回退仍合理。
<!-- source-family:SF-2026-ARXIV-2609-37624 -->


## actual owner — books/part-01-worldview/05-what-neural-networks-learn.md

L253–266:
内部分析至少要区分一条证据阶梯：

```text
behavioral correlation
→ decodability
→ localized intervention
→ downstream behavioral change
→ cross-context / cross-model replication
```

前两层可以发现“某种信息存在于 activation 中”，却没有证明原始 forward path 依赖它。
更强的主张需要在控制混杂因素的前提下修改候选表示，并观察预期的 downstream computation
或行为是否随之改变；即使如此，单个 prompt、单个模型家族或局部线性近似上的效果仍不是
完整机制。

## actual owner — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

L48–58:
第 23 章给出了表示的重构和语义契约，本章还必须问一个不同的问题：**这种表示是否容易被当前生成路径逐步预测？**
视觉 encoder 的高维连续 latent 即使能重构图像，单个 latent token 的分布仍可能比低维 VAE latent 难建模。
在 teacher forcing 下，AR 看到真实历史；生成时却要以自己的连续预测作下一步条件，高维误差会随步骤进入后续条件。
因此，重构分数不能替代生成质量、误差滚动或推理成本的验收。

一种受限分支先校准 token 分布，再在训练时扰动真实历史，让预测器练习接住偏离数据流形的前缀；它以更复杂的
表示归一化和训练噪声换生成容错，却不能靠更低训练损失证明最终图像更好。若扰动不匹配真实 rollout、
生成质量仍落后或稳定性优先，沿用重构导向 VAE 仍是合理选择。[RAE-AR 的图像实验](https://arxiv.org/html/2604.01545v1)
只支持所测 encoder、AR 架构、训练设置与指标下的这条表示—生成张力；其消融中归一化单独使用并非总有益，
结果也不证明高维语义 latent 已普遍追平 VAE。<!-- source-family:SF-2026-ARXIV-2604-01545 -->


## actual owner — books/part-01-worldview/04-why-models-learn.md

L41–47:
神经网络“能够学习”至少包含三个不同命题。

第一是 **representation capacity**：模型函数族里是否存在一个足够好的函数。Universal Approximation 一类结果讨论的是特定条件下的表示能力。它说明某些网络可以逼近一类函数，但不告诉我们需要多少参数、多少数据，也不保证训练算法能找到那组参数。

第二是 **optimization**：从当前参数出发，算法能否在可接受时间和资源内找到低训练损失区域。一个好解存在，不代表梯度下降一定到达；loss surface、初始化、数值精度、batch 噪声和学习率都会影响路径。

第三是 **generalization**：训练集上的低误差能否延续到未见样本。即使模型把训练集完全记住，经验风险也可以很低，但真实业务分布上的风险仍可能很高。
