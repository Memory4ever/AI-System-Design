[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: A Dataset is Worth 1 MB

[3] h6: Abstract

[4] p: A dataset server must often distribute the same large payload to many clients, incurring massive communication costs. Since clients frequently operate on diverse hardware and software frameworks, transmitting a pre-trained model is often infeasible; instead, agents require raw data to train their own task-specific models locally. While dataset distillation attempts to compress training signals, current methods struggle to scale to high-resolution data and rarely achieve sufficiently small files. In this paper, we propose Pseudo-Labels as Data (PLADA), a method that completely eliminates pixel transmission. We assume agents are preloaded with a large, generic, unlabeled reference dataset (e.g., ImageNet-1K, ImageNet-21K) and communicate a new task by transmitting only the class labels for specific images. To address the distribution mismatch between the reference and target datasets, we introduce a pruning mechanism that filters the reference dataset to retain only the labels of the most semantically relevant images for the target task. This selection process simultaneously maximizes training efficiency and minimizes transmission payload. Experiments on 10 diverse datasets demonstrate that our approach can transfer task knowledge with a payload of less than 1 MB while retaining high classification accuracy, offering a promising solution for efficient dataset serving.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Sending training datasets from a central server to multiple clients is an expensive process, as large datasets must be transmitted repeatedly. This places a heavy burden on dataset servers. Reducing this communication cost is therefore critical. Crucially, sending pre-trained model weights instead of datasets is often insufficient. In many practical scenarios, clients are heterogeneous—ranging from diverse autonomous vehicles to medical devices—and must train models using specific software frameworks (e.g., PyTorch, JAX) or bespoke hardware. Consequently, the server must transmit the training data to allow agents to optimize their own unique models locally. A secondary challenge arises in scenarios where the communication channel is severely bandwidth-constrained. Examples include underwater acoustic links to deep-sea vehicles (up to ∼ \sim 5 kbps) ( LinkQuest Inc., 2007 ; Won and Park, 2012 ; Annalakshmi and others, 2017 ) or the Titan rover where direct-to-Earth links can be on the order of ∼ \sim 500–800 bps ( Abelson, 2005 ; Oleson et al., 2015 ) . In such cases, transmitting a typical mid-sized (1 GB) dataset would take days to months and can be energetically prohibitive. Addressing these scenarios requires methods capable of compressing training datasets by orders of magnitude while minimizing accuracy loss.

[8] p: A prominent line of research addressing this challenge is dataset distillation. This approach aims to replace a large training dataset with a compact set of synthetic images and labels, such that a model trained on them minimizes regret with respect to the original data. Despite its promise, synthesizing these learning-efficient images is computationally and numerically challenging. While easier on smaller benchmarks like CIFAR-10 ( Krizhevsky, 2009 ) , scaling these methods to high-resolution datasets is difficult. The core challenge lies in unrolling optimization steps ( Cui et al., 2023 ) due to high memory requirements and unstable inner loop optimization. Furthermore, the continuous, full-precision nature of these synthetic pixels often results in file sizes that remain prohibitively large. Finally, dataset distillation struggles with mismatched server and client architectures, although there has been progress on this front.

[9] p: In this paper, we invert the standard framework of dataset distillation. Rather than synthesizing images while keeping the labels fixed, we synthesize labels while keeping the images fixed. We assume each remote agent is preloaded with a standardized, large, unlabeled set of images, which we term the reference dataset. To communicate a new task, we do not transmit pixels; instead, we provide only the class labels for specific images within this reference dataset. Since a label is merely a compact integer index, the transmission payload is drastically reduced. The agent then utilizes its stored reference images and the newly received labels to locally train the target model. In essence, we replace expensive pixel transmission with on-device storage and highly compressed labels.

[10] p: This approach faces two immediate hurdles: distribution mismatch and efficiency. First, the majority of images in a generic reference dataset are likely semantically unrelated to the target task and can hurt learning. Second, for large reference datasets with many classes, transmitting a label for every image remains bandwidth-intensive. We propose a unified solution to both problems: dataset pruning. We select only a small fraction of reference images for training, ignoring the rest. This ensures that only images semantically related to the target task are used, while simultaneously reducing the transmission cost, as indicating that an image should be ignored requires only a single bit. To achieve this, we introduce a pruning heuristic inspired by out-of-distribution (OOD) detection.

[11] p: We validate our framework on 10 diverse natural-image datasets and 4 medical (OOD) datasets, utilizing unlabeled ImageNet-1K ( Deng et al., 2009 ) and ImageNet-21K ( Ridnik et al., 2021 ) as reference datasets. We demonstrate the ability to transmit the information required to learn a novel task in less than 1 MB, often with only small loss in accuracy. We even find non-trivial accuracy when the target datasets are medical and distributionally distant from the reference set. Qualitative analysis confirms that our selection procedure successfully identifies semantically relevant images, validating the method’s effectiveness. Furthermore, we analyze the trade-offs between reference dataset size and transmission payload, and provide ablations on different coding schemes.

[12] figure: Figure 1 : Motivation. A dataset server transmits the same large dataset many times at massive cost. Our method allows the server to send a compressed payload of less than 1 MB, enabling clients with heterogeneous hardware, even if they have ultra-narrow bandwidth, to train their own models locally.

[13] p: Our contributions are as follows:

[14] p: We propose a new method: Pseudo-Labels as Data , which transmits only hard labels while achieving high performance, reducing the transfer payload to a well below one bit per reference image (e.g., 85–206KB at 1% keep on ImageNet‑21K after Zstd; Table 4 ).

[15] p: We introduce an effective pruning mechanism using Energy-based OOD scores. We show that filtering the reference dataset to just 1%-10% of images both improves accuracy and reduces bandwidth costs.

[16] p: We demonstrate that our method achieves high accuracy on diverse classification tasks while transmitting a payload of less than 1 MB.

[17] h2: 2 Related Works

[18] p: Dataset and Label Distillation. Dataset distillation (a.k.a. dataset condensation) compresses a full training set into a tiny synthetic set such that training on it approximates training on the original data ( Wang et al., 2018 ; Yu et al., 2023 ) . While effective on smaller benchmarks, scaling these methods to high-resolution repositories like ImageNet-21K has historically been limited by exorbitant compute/memory consumption during optimization ( Zhao et al., 2021 ; Cui et al., 2023 ; Cazenavette et al., 2022 ; Du et al., 2023 ) . Recent work suggests that the labels can be the primary driver of successful distillation—motivating approaches that learn or distill labels rather than synthesizing pixels ( Sucholutsky and Schonlau, 2021 ; Ondrej Bohdal, 2020 ; Qin et al., 2024 ) . PLADA takes this perspective to the extreme: instead of transmitting images, we communicate a task by transmitting only hard pseudo-labels for a fixed, preloaded reference image set.

[19] p: Knowledge Distillation and Pseudo Labels. Knowledge distillation trains a student model to match the predictions of a teacher , typically using soft targets/logits to transfer knowledge across architectures ( Hinton et al., 2015 ; Nayak et al., 2019 ; Wang and Yoon, 2021 ; Mansourian et al., 2025 ) . When original training data is unavailable, data-free distillation synthesizes inputs ( Nayak et al., 2019 ) or reconstructs them from a trained model ( Yin et al., 2020 ) ; recent work also frames distillation as an efficient mechanism for faster convergence and improved transfer ( He et al., 2022 ) . Pseudo-labeling and self-training treat a model’s high-confidence predictions as supervision, often paired with confidence filtering and meta-learning to improve label quality ( Lee, 2013 ; Sohn et al., 2020 ; Xie et al., 2020 ; Pham et al., 2021 ; Kage et al., 2024 ) . PLADA turns this idea into a communication primitive: a server-side teacher generates hard pseudo-labels on a shared reference dataset, and clients train locally using these pseudo-labels as data .

[20] p: OOD Detection and Data Pruning/Selection. Deep networks are often overconfident under distribution shift, motivating out-of-distribution (OOD) detection methods based on softmax confidence ( Hendrycks and Gimpel, 2017 ) , temperature/perturbation scoring (ODIN) ( Liang et al., 2018 ) , feature-density scores such as Mahalanobis distance ( Lee et al., 2018 ) , and energy-based criteria ( Liu et al., 2020 ) . Training-time modifications can also improve confidence separation (e.g., LogitNorm) ( Wei et al., 2022 ; Ding et al., 2025 ) , and recent work further improves distance-based OOD scoring by dynamically calibrating geometry at test time ( Guo et al., 2025 ) . Closely related are data selection and pruning methods that reduce training cost while preserving accuracy ( Sorscher et al., 2022 ; Yang et al., 2023b ) , including approaches that explicitly combine pruning with knowledge distillation to mitigate accuracy loss at high pruning rates ( Ben-Baruch et al., 2024 ) . PLADA’s pruning stage leverages uncertainty/OOD scores to select semantically relevant reference examples before label transmission, aligning with this literature while operating in a communication-limited dataset-serving setting.

[21] figure: Figure 2 : The PLADA Pipeline. The server (left) trains a teacher classifier on the task dataset and distills this task knowledge into hard labels on the reference data. It then filters to the lowest-uncertainty p % p\% of pseudo-labels and transmits a compressed payload ( < 1 <1 MB). The client (right) reconstructs a virtual dataset using its preloaded reference dataset and the payload to train the student model.

[22] h2: 3 Problem Formulation

[23] p: In our setting, there is a central server (denoted A s A_{s} ) and multiple remote agents (denoted A r A_{r} ). We preload all remote agents with the same reference dataset D r D_{r} containing n n unlabeled samples D r = { x 1 , x 2 , … , x n } D_{r}=\{x_{1},x_{2},\dots,x_{n}\} drawn from a distribution 𝒟 r \mathcal{D}_{r} . After deployment, when the remote agents are distant from the central server, a new target task arises with distribution 𝒟 t \mathcal{D}_{t} . Each sample consists of a pair ( x , y ) (x,y) , where the input is x x and the target label is y y . In this paper, we assume the target label is discrete, making the task a classification problem; we leave the extension to regression for future work. Our objective is to train a classifier f f on the remote agent that achieves high accuracy in predicting y y given x x for ( x , y ) ∼ 𝒟 t (x,y)\sim\mathcal{D}_{t} .

[24] p: To fulfill this task, the server A s A_{s} transmits a payload P P of size b b bytes to each remote agent A r A_{r} . We assume the remote agent is capable of training a model given input data. The objective is to maximize the accuracy of classifier f f while satisfying the constraint that the transmitted payload does not exceed b b bytes.

[25] h2: 4 Method

[26] h3: 4.1 Overview

[27] p: Our core approach is illustrated in Figure 2 . The central server first trains a ground-truth classifier, f g ​ t f_{gt} , on the training data from the target distribution 𝒟 t \mathcal{D}_{t} . It utilizes this classifier to generate pseudo-labels for the reference dataset. The server then transmits these pseudo-labels as the payload to the remote agent. Finally, the remote agent trains a student classifier f f on the reference set using the received labels. In Section 4.3 , we present pruning methods to significantly reduce the number of class labels transmitted. In Section 4.4 , we describe variable-length coding methods that leverage the statistical properties of the labels to further compress the payload size.

[28] h3: 4.2 Efficient Classifier Transfer via Hard Pseudo-Labels

[29] p: Transmitting a full dataset to a remote agent requires bandwidth that often exceeds 1 GB. While subsampling datasets (e.g., via coreset selection) can reduce size by 50-80%, it typically incurs a significant penalty in accuracy. For extreme bandwidth constraints, this reduction is insufficient. Dataset distillation aims to create synthetic images with aggressive compression; however, these methods often result in accuracy loss and still require payloads measuring in megabytes.

[30] p: Our core premise is that for classification tasks, labels contain far more information per byte than images. However, labels must be associated with images, which are expensive to transmit. To resolve this, we utilize a fixed reference dataset preloaded on each remote agent. To transmit a target task, we send only the pseudo-labels corresponding to the images in this reference dataset. We utilize hard labels rather than soft labels, as storing soft labels requires significantly more memory.

[31] p: Label generation. Since the reference dataset is generic, many of its images may not correspond to any classes in the target task. We propose a two-step procedure. First, we train a classifier f g ​ t f_{gt} on the training data from the target distribution 𝒟 t \mathcal{D}_{t} :

[32] table: f g ​ t ← arg ​ min f ⁡ 1 n t ​ a ​ r ​ g ​ e ​ t ​ ∑ ( x , y ) ∼ 𝒟 t ℒ C ​ E ​ ( f ⁡ ( x ) , y ) f_{gt}\leftarrow\operatorname*{arg\,min}_{f}\frac{1}{n_{target}}\sum_{(x,y)\sim\mathcal{D}_{t}}\mathcal{L}_{CE}(f(x),y) (1)

[33] p: We then label each image in the reference set using the classifier f g ​ t f_{gt} , assigning each image the label corresponding to the maximal logit:

[34] table: l i = arg ​ max q ⁡ f g ​ t ​ ( x i ) ​ [ q ] l_{i}=\operatorname*{arg\,max}_{q}f_{gt}(x_{i})[q] (2)

[35] p: The server sends a payload consisting of the hard labels for the reference set images:

[36] table: P = [ l 1 , l 2 , … , l n ] P=[l_{1},l_{2},\dots,l_{n}] (3)

[37] p: Let k k denote the number of target classes. Naively sending the reference set labels requires n ​ log 2 ​ k n\log_{2}k bits. After transmission, the agent trains a classifier based on the locally stored reference images and the received labels:

[38] table: f ← arg ​ min f ′ ⁡ 1 n ​ ∑ i = 1 n ℒ C ​ E ​ ( f ′ ​ ( x i ) , l i ) f\leftarrow\operatorname*{arg\,min}_{f^{\prime}}\frac{1}{n}\sum_{i=1}^{n}\mathcal{L}_{CE}(f^{\prime}(x_{i}),l_{i}) (4)

[39] p: The resulting classifier f f on the client serves as the final student model.

[40] h3: 4.3 Reference Dataset Pruning

[41] p: Transmitting a label for every reference image is suboptimal. First, it hurts accuracy: some reference images do not fit any target task classes. For example, an image yielding roughly equal logits for all classes is likely a poor representative for any of them. Forcing such an image into a hard class introduces noise that degrades the target training process. Second, sending a label requires log 2 ⁡ k \log_{2}k bits per image, which becomes expensive for large reference sets. Ideally, we should transmit only informative labels.

[42] p: Selecting informative images. We draw inspiration from semi-supervised learning, which applies a predictor to a large set of potentially irrelevant images. To isolate relevant samples, these approaches use distribution measures to filter for images where the label certainty is high. Concretely, we retain the top p % p\% of images based on an uncertainty score (where lower is better). We evaluated several out-of-distribution metrics and found that Logit Energy achieved the best results, with Shannon Entropy performing comparably (see Table 7 ). We compute energy as:

[43] table: E ( x ; f g ​ t ) = − log ∑ j = 1 k exp ( f g ​ t ( x ) [ j ] ) E(x;f_{gt})=-\log\sum_{j=1}^{k}\exp(f_{gt}(x)[j]) (5)

[44] p: In a large reference dataset like ImageNet-21K, typically only a small fraction of images are relevant to a specific downstream task. As shown in Figure 3 , images semantically related to the target dataset often appear only within the top 1% of lowest energy scores.

[45] p: Overall, we find that pruning uncertain labels offers three advantages: (i) lower transmission cost, (ii) increased accuracy for the client’s target classifier, and (iii) reduced training time due to the smaller dataset size. See Section 5.2 for experimental results.

[46] figure: Figure 3 : Reference set images vs. energy percentile. High-confidence (low-energy) samples retrieved from ImageNet-21K demonstrate semantic and structural alignment with the target domains. For additional visualizations see Appendix C .

[47] p: Safety-Net Filtering. While energy-based pruning effectively selects high-confidence samples, it suffers from a significant drawback in high-compression regimes: it disproportionately removes samples from “harder” or under-represented classes. When the global retention ratio is low (e.g., 1%), the filtered dataset is often dominated by a few “easy” classes, leading to class collapse and poor student generalization. Figure 4 illustrates this issue.

[48] p: To mitigate this, we propose a Safety-Net filtering mechanism. Instead of relying solely on a global energy threshold, we reserve a portion s s of the bandwidth budget to ensure that all classes are preserved. We define a class-specific quota K c K_{c} for each class c c based on a power-law weighting of its original size N c N_{c} :

[49] table: K c ∝ ( N c ) α K_{c}\propto(N_{c})^{\alpha} (6)

[50] p: where α \alpha is a balancing hyperparameter.

[51] p: α = 1 \alpha=1 : proportional retention (preserves the original imbalance).

[52] p: α = 0 \alpha=0 : uniform retention (equal quota per class).

[53] p: α < 0 \alpha<0 : tail-favoring retention (weak classes receive larger quotas).

[54] p: We specifically explore negative α \alpha values (e.g., α = − 0.2 \alpha=-0.2 ). This setting intentionally over-samples from smaller or “weaker” classes, providing a structural guarantee that tail classes are preserved in the distilled dataset. To construct the final payload, we first fill the Safety-Net quota using the best available samples (lowest energy) per class, and then utilize the remaining budget according to global logit energy, regardless of class membership.

[55] h3: 4.4 Variable-Length Coding

[56] p: Payload transmission can be optimized with suitable compression. A naive scheme for a payload with n r ​ e ​ f n_{ref} reference images and a keep rate of p % p\% involves sending: (i) one bit per image indicating whether the label was retained, and (ii) log 2 ⁡ k \log_{2}k bits for the hard label of each retained image. This results in b r ​ a ​ w b_{raw} bits:

[57] table: b r ​ a ​ w = n r ​ e ​ f ​ ( 1 + p ​ log 2 ​ k ) b_{raw}=n_{ref}(1+p\log_{2}k) (7)

[58] p: For large reference datasets, this overhead is significant. For example, using ImageNet-21K ( ≈ 14.2 \approx 14.2 million images) as the reference with a 5% keep rate and 64 classes (6 bits), the payload is approximately 2 MB, the majority of which (1.69 MB) is consumed by the pruning mask (1 bit per reference set image image).

[59] p: We can mitigate the cost of the pruning mask using Run-Length Encoding (RLE). Instead of storing all bits, we store the distance between consecutive kept indices. For low keep rates ( p ≪ 1 p\ll 1 ), this exploits sparsity effectively, reducing the average cost per selected item significantly compared to a dense bitmap.

[60] figure: Figure 4 : Class distribution of the RESISC45 pseudo hard-labels , before and after filtering using safety-net. The yellow bars show the original global distribution, which is heavily imbalanced - RESISC45 has images extracted using Google Earth, out of which class 0 is airplane . Standard global filtering would eliminate some of the tail classes entirely. The blue bars demonstrate our Safety-Net Filtering (keeping 5%, α = − 0.2 \alpha=-0.2 ), which effectively preserves a representation of under-represented classes even under extreme compression. Note that the Y-axis uses a cube-root scale to visually accommodate the large magnitude differences between the ‘strong‘ and ‘weak‘ classes.

[61] p: Furthermore, we exploit the statistical distribution of classes. Instead of using a fixed log 2 ⁡ k \log_{2}k bits per label, we employ variable-length encoding so that frequent classes are assigned shorter codes. Huffman coding is a classical method leveraging this principle. We illustrate the class distribution in Fig. 4 .

[62] p: While these classical concepts highlight the sources of redundancy, modern implementations offer superior performance. In our experiments, we utilize Zstd ( Collet, 2021 ; Meta Platforms, 2026 ) , a modern state-of-the-art compression library, to compress the final pseudo-label payloads.

[63] h2: 5 Experiments

[64] p: In this section, we evaluate the proposed PLADA framework. We assess its ability to transfer task knowledge under extreme bandwidth constraints, analyze its robustness to out-of-distribution (OOD) tasks, and validate the efficacy of the Safety-Net filtering mechanism.

[65] figure: Table 1 : Keep rate evaluations. Student accuracy when trained on the top- p p images of the reference set, according to logit Energy. We achieve accurate classification on target tasks using only a fraction of the reference set. ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) Dataset 1% 5% 10% 25% 50% 100%* 1% 5% 10% 25% 50% 100%* Caltech-101 79.84% 88.94% 90.21% 90.73% 92.45% 92.74% 66.59% 77.13% 82.49% 86.35% 86.52% 87.50% CIFAR-10 63.31% 85.31% 88.12% 91.68% 92.62% 86.13% 53.75% 72.02% 74.83% 79.90% 84.96% 87.66% CUB-200 82.49% 82.36% 82.44% 81.34% 81.09% 74.94% 22.94% 45.89% 51.40% 56.19% 55.60% 52.97% DTD 66.65% 70.16% 70.69% 70.80% 68.83% 68.14% 52.45% 58.99% 60.48% 60.90% 61.97% 62.29% FGVC-Aircraft 53.62% 45.51% 46.41% 45.87% 43.53% 32.16% 20.04% 23.91% 26.58% 29.16% 30.18% 29.40% Food-101 75.50% 76.18% 76.91% 76.72% 75.27% 73.43% 37.66% 50.82% 52.90% 56.01% 56.95% 57.60% Oxford-Flowers 96.93% 98.41% 98.50% 98.19% 98.06% 96.76% 62.29% 75.65% 75.12% 75.80% 73.38% 68.66% Oxford-IIIT-Pet 90.95% 91.03% 90.81% 90.05% 89.48% 87.74% 83.21% 88.66% 88.93% 89.26% 89.40% 88.69% Places365 23.39% 34.89% 40.05% 45.82% 48.66% 46.95% 16.97% 26.85% 31.96% 38.36% 41.63% 43.69% RESISC45 58.16% 67.81% 74.37% 80.62% 76.79% 31.02% 30.03% 50.44% 57.67% 63.60% 71.68% 78.73% * Indicates no filtering (full reference set used). † Teacher Accuracies: Caltech-101 (98.39%), CIFAR-10 (98.15%), CUB-200 (97.71%), DTD (77.50%), FGVC-Aircraft (86.53%), Food-101 (90.02%), Oxford-Flowers (99.04%), Oxford-Pets (93.40%), Places365 (55.45%), RESISC45 (96.84%).

[66] h3: 5.1 Experimental Setup

[67] h5: Datasets and Benchmarks.

[68] p: We evaluate our method on 14 diverse classification datasets, categorized by domain to test generalization across varying granularities:

[69] p: Coarse-grained Objects: Caltech-101 ( Li et al., 2022 ) , CIFAR-10 ( Krizhevsky, 2009 ) , and Places365 ( Zhou et al., 2017 ) .

[70] p: Fine-grained Classification: CUB-200-2011 ( Wah et al., 2022 ) , DTD (Textures) ( Cimpoi et al., 2014 ) , FGVC-Aircraft ( Maji et al., 2013 ) , Food-101 ( Bossard et al., 2014 ) , Oxford-Flowers-102 ( Nilsback and Zisserman, 2008 ) , Oxford-IIIT Pet ( Parkhi et al., 2012 ) , and RESISC45 ( Cheng et al., 2017 ) .

[71] p: Medical (OOD Stress Test): To test the limits of our approach on data distributionally disjoint from ImageNet, we utilize BloodMNIST, DermaMNIST, RetinaMNIST, and NCT-CRC-HE-100K ( Yang et al., 2021 ; Yang et al., 2023a ; Ignatov and Malivenko, 2024 ) .

[72] p: Data Leakage Verification: We rigorously verified (see App. A ) that there is zero or statistically negligible intersection ( < 1 % <1\% ) between the target test sets and the ImageNet reference datasets, ensuring that student performance is not a result of memorization.

[73] h5: Baselines.

[74] p: We compare PLADA against three transmission strategies:

[75] p: Random Subset: Transmitting a balanced random subset of raw target images.

[76] p: Coreset Selection: Selecting representative images via K-Center ( Sener and Savarese, 2017 ; Moser et al., 2025a ) from each target class.

[77] p: Dataset Distillation (DD): Comparing against state-of-the-art distillation methods where available.

[78] p: For a fair comparison of information density, all baseline image payloads are compressed using JPEG ( Q = 30 Q=30 ) and measured after applying Zstandard (Zstd) compression (level 19).

[79] h5: Implementation Details.

[80] p: As the teacher model, we use a ConvNeXt-V2-Tiny ( Woo et al., 2023 ) pre-trained on ImageNet-21K and fine-tuned on the target data. The remote agent trains a ResNet-18 ( He et al., 2016 ) initialized with pre-trained weights. We train for 5 epochs (when using the ImageNet-21K reference set) or 30 epochs (ImageNet-1K) using the AdamW optimizer ( Loshchilov and Hutter, 2019 ) ( l ​ r = 10 − 3 lr=10^{-3} , cosine schedule). All experiments were conducted on a single NVIDIA A5000 GPU.

[81] figure: Table 2 : Baseline comparison. We compare student accuracy across 10 benchmarks. Our method, PLADA (using 1% keep ratio with possible Safety-Net filtering on ImageNet-21K, see Table 3 ), outperforms data-transmission baselines—including random sampling, K-Center coresets, and Dataset Distillation (DD)—in both accuracy and payload size. Notably, PLADA achieves superior task recovery while requiring a payload significantly smaller than even the aggressive 100-image JPEG-compressed subsets. Using 100 Images Using 500 Images Dataset Ours (p=1%) Random K-Centers Random K-Centers DD † Caltech-101 86.69% 32.78% 34.16% 47.98% 51.04% – CIFAR-10 76.75% 28.66% 19.33% 31.29% 27.20% 73.2% CUB-200 82.49% 4.58% 3.69% 9.67% 7.55% 16.2% DTD 68.09% 19.04% 14.73% 36.49% 28.35% – FGVC-Aircraft 53.62% 2.76% 2.10% 4.62% 4.59% – Food-101 75.50% 3.95% 3.20% 10.26% 5.89% 77.6% Oxford-Flowers 97.53% 36.39% 33.74% 34.20% 25.78% 71.1% Oxford-IIIT-Pet 90.98% 11.97% 15.91% 61.60% 53.61% – Places365 31.59% 1.17% – 3.21% 2.91% – RESISC45 75.65% 20.81% 11.16% 29.98% 19.57% – Size* (KB) 147.3 ± \pm 13.2 356.4 ± \pm 27.8 376.9 ± \pm 30.5 1818.0 ± \pm 126.9 1907.7 ± \pm 136.4 – *Reported payload sizes are mean ± \pm SEM. Baseline payloads are compressed using Zstandard (level 19). † Dataset-Distillation (DD) results: CIFAR-10 ( Moser et al., 2025b ) , CUB-200 ( Shul et al., 2025 ) , Food-101 ( Hu et al., 2025 ) , Oxford-Flowers ( Hu et al., 2025 ) .

[82] figure: Table 3 : Impact of safety-net filtering on Student Accuracy. All 1% subsets are sampled from ImageNet-21K. We compare the default lowest-energy filtering and its counterpart (highest-energy filtering) against Safety-Net variants. Low-energy samples (Vanilla) outperform high-energy ones. Safety-Net often further improves accuracy by preventing class collapse, with the same payload budget. The difference is the highest for RESISC45 (cf. Figure 4 ). Additional results are reported in Table 10 . Dataset 1% Vanil. 1% Oppos. 1%+Safe ( α = 0.5 \alpha=0.5 ) 1%+Safe ( α = − 0.2 \alpha=-0.2 ) Caltech-101 79.84% 74.42% 86.69% 86.29% CIFAR-10 63.31% 54.80% 76.75% 74.62% CUB-200 82.49% 6.19% 81.21% 80.53% DTD 66.65% 26.12% 66.70% 68.09% FGVC-Aircraft 53.62% 3.45% 43.23% 44.58% Food-101 75.50% 6.28% 70.91% 71.66% Oxford-Flowers 96.93% 9.95% 97.53% 97.35% Oxford-IIIT-Pet 90.95% 18.67% 90.98% 90.87% Places365 23.39% 18.04% 30.26% 31.59% RESISC45 58.16% 2.06% 72.81% 75.65%

[83] figure: Table 4 : Payload size analysis. We compare across keep ratios ( p p ) and compression schemes. Ranges represent the minimum and maximum sizes observed across all 10 different datasets, and across different filtering options (with and without safety-net), with ImageNet-21K as the reference dataset. Raw indicates uncompressed fixed-width binary storage. Zstd represents the final compressed payload size using differential encoding and Zstandard compression (level 19). Full compression experiments results are provided in Appendix E . p p Raw Size Huffman Zstd 0.5% 0.41–1.83 MB 77–305 KB 45–109 KB 1% 0.81–1.96 MB 151–396 KB 85–206 KB 5% 3.05 MB 0.57–1.10 MB 0.40–0.88 MB 10% 4.40–8.12 MB 0.88–1.95 MB 0.67–1.58 MB 25% 8.46 MB 1.65–4.34 MB 1.21–3.47 MB 50% 15.23–40.62 MB 2.49–7.88 MB 1.87–6.42 MB 100% 27.08 MB 2.29–12.83 MB 1.77–10.50 MB

[84] h3: 5.2 Main Results

[85] h5: Accuracy vs. bandwidth efficiency.

[86] p: Table 1 summarizes student accuracy using ImageNet-21K and ImageNet-1K as reference sets. The results validate our core premise: highly accurate task transfer is achievable without transmitting a single pixel from the target domain. PLADA establishes a new Pareto frontier for bandwidth efficiency. As illustrated in Figure 5 , our method (indicated by the star) maintains high accuracy in the extreme low-bandwidth regime ( < 1 <1 MB). Conversely, traditional image-based methods (Random Subset, Coresets) suffer catastrophic accuracy drops in this regime, as they can only transmit a negligible number of training samples.

[87] h5: The “denoising” effect of filtering.

[88] p: A key finding is that training on a filtered subset (top 1%–10% lowest energy) often yields higher accuracy than training on the full reference dataset (100%). For instance, on FGVC-Aircraft and RESISC45 , the filtered subsets significantly outperform the full dataset. This indicates that Energy-based pruning acts as a semantic denoiser: it effectively removes “distractor” images that the teacher classifies with low confidence, leaving only the samples that structurally align with the target concepts.

[89] h5: Impact of reference set scale.

[90] p: Comparing the two reference sets in Table 1 , the larger ImageNet-21K (14.2M images) consistently yields better downstream performance than ImageNet-1K (1.2M images). The massive diversity of the larger pool increases the probability of finding semantic neighbors for fine-grained target classes, providing a richer training signal.

[91] figure: Table 5 : Results on medical datasets † . ImageNet-21K ref. set. Dataset 1% Vanil. 1% Oppos. 1%+Safe ( α = 0.5 \alpha=0.5 ) 1%+Safe ( α = − 0.2 \alpha=-0.2 ) BloodMNIST 18.24% 59.28% 47.00% 41.45% DermaMNIST 53.32% 67.68% 47.58% 38.05% RetinaMNIST 56.50% 56.75% 55.25% 55.00% NCT-CRC-HE 18.69% 43.51% 32.57% 32.37% † Teacher Accuracies: BloodMNIST (99.09%), DermaMNIST (89.63%), RetinaMNIST (70.00%), NCT-CRC-HE-100K (99.93%).

[92] h3: 5.3 Analysis

[93] h5: The energy paradox in far-OOD tasks (Medical).

[94] p: A major challenge arises when the target domain is semantically disjoint from the reference domain. As shown in Table 5 , standard low-energy filtering fails for medical datasets. In these cases, the “best” reference images (lowest energy) are often generic natural images that map spuriously to a single target class (e.g., a red circle in ImageNet mapped to a blood cell), causing the student model to collapse. However, we observe a reversal in the optimal strategy: selecting images with the highest energy (highest uncertainty) consistently outperforms standard filtering (Table 5 , Inverse column). We hypothesize that high-energy reference images, likely containing high-frequency patterns or unusual textures, possess low-level structural statistics that align better with medical scans than semantically clear natural images. This suggests an adaptive strategy: utilize low-energy selection for in-domain tasks and high-energy (inverse) selection for far-OOD tasks.

[95] h5: Safety-Net Filtering.

[96] p: Standard energy filtering can disproportionately prune hard-to-classify or under-represented categories. Table 3 demonstrates the efficacy of our Safety-Net mechanism ( α = − 0.2 \alpha=-0.2 ), which enforces a quota for tail classes. For datasets with high inter-class imbalance, such as RESISC45 , Safety-Net filtering significantly boosts accuracy (from 58.16% to 75.65% at 1% keep-rate) by ensuring the student receives a balanced training distribution even under extreme compression.

[97] h5: Payload Compression Analysis.

[98] p: We analyze the impact of variable-length coding on the final payload size in Table 4 .

[99] p: Sparsity exploitation: At strict filtering rates ( p ≤ 1 % p\leq 1\% ), the payload is dominated by the indices of the selected images rather than the labels themselves.

[100] p: Compression strategy: Zstandard (Zstd) outperforms Huffman coding by exploiting local correlations in the sparse index sequences.

[101] p: This optimization reduces the total payload for the 1% setting to between 45 KB and 200 KB , confirming that transmitting a massive 14-million-image training signal is feasible over even the most constrained channels (e.g., deep-sea acoustic links).

[102] h2: 6 Discussion

[103] h5: Runtime.

[104] p: When using high keep ratios (e.g., p ≥ 25 % p\geq 25\% ), training the student model can take up to 3 days on a single A5000 GPU. However, at low keep ratios the experiments are much shorter (e.g., ∼ \sim 20 minutes at p = 1 % p=1\% with ImageNet-21K as the reference set).

[105] h5: Transmitting model weights.

[106] p: While we focus on transmitting datasets as they allow each client to train their model of choice, there are cases where we may consider sending the weights of a given model to clients. We tested several such strategies: (i) training a linear probing model based on a frozen backbone encoder, then sending its INT8 encoded weights. (ii) Sending a ResNet-18 teacher model with optional pruning and INT8 quantization (following model-compression ideas such as Deep Compression ( Han et al., 2016 ) ). We present results on CUB-200 in Figure 5 . We observe that the linear probe is the most efficient baseline and is quite accurate. Sending the full model is far more expensive than our approach for sending labels.

[107] figure: Figure 5 : Bandwidth-Accuracy Baselines (CUB-200). Comparison of PLADA against weight and data transmission baselines. PLADA (red star) dominates the top-left corner, achieving higher accuracy than weight-based methods while requiring a smaller payload (¡35 KB). Data-centric baselines (Random Subset/K-Center) fail to provide a viable signal at this extreme budget. All payloads are Zstd-compressed (level 19).

[108] h5: Optimal reference dataset selection.

[109] p: In our experiments, we used ImageNet-1K and ImageNet-21K as reference datasets. These are not necessarily optimal from an accuracy–bandwidth–storage perspective. We are not aware of principled approaches for selecting an optimal reference dataset, and we leave this to future work.

[110] h5: Limitations.

[111] p: While significantly reducing communication cost, our method requires each client to store the reference dataset. This overhead becomes less significant—and can even be cost-saving—once many target tasks are served and their cumulative size exceeds that of the reference dataset. Another limitation is that, in some cases, training time may increase (i.e., more iterations may be needed) to match training on the original target data. Finally, our work focuses on classification and does not yet handle regression or generative tasks. We expect regression to be straightforward to incorporate, but enabling generative modeling without sending pixels remains an exciting challenge for the future.

[112] h2: 7 Conclusion

[113] p: We proposed Pseudo-Labels as Data (PLADA), a method for sending datasets at very low communication cost. It transmits tasks by only sending the hard pseudo-labels for a large, preloaded reference dataset. By combining energy-based filtering with a safety-net mechanism, PLADA selects a compact, class-preserving subset of reference images while aggressively reducing transmission cost. This enables task transfer with payloads well below 1 MB, even when using huge ImageNet-21K reference set. These results show that, for classification, task knowledge can be conveyed more efficiently through labels rather than through pixels. We hope this perspective motivates future work to further improve the accuracy–bandwidth trade-off in dataset serving.

[114] h2: References

[115] h2: Appendix A Dataset Intersection Analysis

[116] p: To validate our method, we must ensure that the student model is not simply memorizing samples from the reference dataset (ImageNet-21K) that happen to be duplicates of the target task’s test set. We implemented a content-based intersection check using the method described below.

[117] p: Methodology: We employed a bucketed L1-distance check. We computed the mean and variance for every image in both the target datasets (Set 1) and the reference ImageNet-21K dataset (Set 2). Images were hashed into buckets based on these statistics (using 1024 bins). We then performed a pixel-wise L1 comparison only between images falling into the same buckets. An intersection was flagged if the mean L1 pixel difference was below a strict threshold ( ϵ < 10 − 5 \epsilon<10^{-5} ).

[118] p: Results: We analyzed the intersection between the target datasets and the full 14.2M ImageNet-21K dataset. Our findings are summarized in Table 6 .

[119] p: Zero Intersection: For the majority of benchmarks—including Oxford Flowers 102, Food-101, DTD, CIFAR-10, RESISC45, and Places365—we found exactly 0 intersections between the target and test sets with ImageNet-21K.

[120] p: Negligible Intersection:

[121] p: FGVC-Aircraft & CUB-200-2011: While we identified a small number of duplicates in the training splits (1 and 2 images, respectively), the intersection with the test sets was exactly 0 .

[122] p: Caltech-101: We found 2 overlapping images in the test set.

[123] p: Oxford-IIIT Pet: This dataset showed the highest overlap, with 25 test images appearing in ImageNet-21K. However, this represents only ≈ 0.68 % \approx 0.68\% of the test set (25/3669).

[124] p: Given that the intersections are either non-existent or statistically negligible ( < 1 % <1\% ), we conclude that the performance gains reported in our experiments are driven by the effective distillation of knowledge into the synthetic labels, rather than data leakage from the auxiliary set.

[125] figure: Table 6 : Intersection analysis between Target Datasets and ImageNet-21K (14.2M). Columns show the number of duplicates found in the full target dataset ( x / n a ​ l ​ l x/n_{all} ) and the specific test set ( y / n t ​ e ​ s ​ t y/n_{test} ). Target Dataset Total Intersection Test Intersection Oxford Flowers 102 0 / 8,189 0 / 6,149 Food-101 0 / 101,000 0 / 25,250 DTD 0 / 3,760 0 / 1,880 CIFAR-10 0 / 60,000 0 / 10,000 RESISC45 0 / 31,500 0 / 6,300 Places365 0 / 1,839,960 0 / 36,500 FGVC-Aircraft 1 / 10,000 0 / 3,333 CUB-200-2011 2 / 11,788 0 / 2,358 Caltech-101 4 / 8,677 2 / 1,736 Oxford-IIIT Pet 244 / 7,349 25 / 3,669

[126] h2: Appendix B Detailed Experimental Results

[127] p: We report detailed student accuracy results under different filtering strategies in Tables 7 , 8 , 9 , 10 and 11 . Table 7 compares entropy-based and energy-based filtering across multiple filtering budgets using ImageNet-21K as the reference dataset. Table 8 evaluates an alternative setting in which the student is trained using the highest p % p\% energy-score images (instead of the lowest), for models trained with ImageNet-1K or ImageNet-21K as reference datasets. Table 9 presents the same analysis for biomedical target datasets, highlighting the behavior of highest-energy versus lowest-energy filtering in this out-of-distribution setting. Tables 10 and 11 report Safety-Net results on natural image and medical datasets, respectively.

[128] figure: Table 7 : Entropy vs Energy Pruning. This table reports student accuracy † under different filtering budgets, comparing entropy-based pruning with energy-based pruning (ImageNet-21K). 1% Filter 5% Filter 10% Filter 25% Filter Dataset Entropy Energy Entropy Energy Entropy Energy Entropy Energy Caltech-101 75.06% 79.84% 84.22% 88.94% 87.56% 90.21% 91.71% 90.73% CIFAR-10 72.57% 63.31% 86.00% 85.31% 89.14% 88.12% 91.14% 91.68% CUB-200 77.44% 82.49% 81.42% 82.36% 81.76% 82.44% 81.59% 81.34% DTD 67.02% 66.65% 69.79% 70.16% 71.22% 70.69% 71.06% 70.80% FGVC-Aircraft 37.32% 53.62% 44.13% 45.51% 45.69% 46.41% 45.90% 45.87% Food-101 68.32% 75.50% 73.88% 76.18% 74.33% 76.91% 75.47% 76.72% Oxford-Flowers-102 95.01% 96.93% 98.28% 98.41% 98.41% 98.50% 98.18% 98.19% Oxford-IIIT-Pet 90.81% 90.95% 91.09% 91.03% 90.76% 90.81% 90.41% 90.05% Places365 20.38% 23.39% 34.71% 34.89% 40.40% 40.05% 46.20% 45.82% RESISC45 54.05% 58.16% 70.11% 67.81% 75.76% 74.37% 80.87% 80.62% † Teacher Accuracies: Caltech-101 (98.39%), CIFAR-10 (98.15%), CUB-200 (97.71%), DTD (77.50%), FGVC-Aircraft (86.53%), Food-101 (90.02%), Oxford-Flowers (99.04%), Oxford-Pets (93.40%), Places365 (55.45%), RESISC45 (96.84%).

[129] figure: Table 8 : Opposite Energy-Based Pruning. This table shows the student accuracy obtained by training on the highest - p % p\% energy-score images (which are usually the ”worst” images), using ImageNet-1K and ImageNet-21K as reference datasets. ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) Dataset 1% 5% 10% 1% 5% 10% 25% Caltech-101 74.42% 85.66% 87.27% 61.29% 79.32% 82.89% 85.54% CIFAR-10 54.80% 64.45% 70.12% 34.90% 45.84% 58.46% 67.09% CUB-200 6.19% 11.79% 15.48% 3.22% 6.66% 8.78% 14.16% DTD 26.12% 37.34% 42.77% 19.41% 27.45% 35.90% 40.00% FGVC-Aircraft 3.45% 5.37% 8.16% 2.46% 3.57% 4.74% 8.70% Food-101 6.28% 13.11% 20.11% 3.72% 7.40% 11.30% 18.15% Oxford-Flowers-102 9.95% 24.43% 29.91% 4.36% 10.88% 14.41% 24.15% Oxford-IIIT-Pet 18.67% 30.23% 36.49% 9.59% 19.81% 29.05% 37.20% Places365 18.04% 27.35% 32.14% 10.91% 18.96% 22.73% 29.55% RESISC45 2.06% 2.06% 2.06% 29.65% 52.43% 61.33% 68.62%

[130] figure: Table 9 : Medical Datasets Opposite Energy-Based Pruning. This table presents student accuracy obtained by training on the highest p % p\% energy-score images of the reference sets. As explained in Section 5.3 , we unexpectedly observed higher student accuracy when applying the opposite filtering strategy on the medical datasets. ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) Dataset 1% 5% 1% 5% BloodMNIST 59.28% 57.88% 32.65% 38.03% DermaMNIST 67.68% 66.58% 66.43% 67.33% RetinaMNIST 56.75% 58.00% 50.25% 55.50% NCT-CRC-HE-100K 43.51% 52.48% 26.46% 35.33%

[131] p: Notably, the results for the medical datasets differ from those of the other benchmarks. This behavior can be attributed to the significant domain gap between these datasets and both the natural-image benchmarks and ImageNet. As a consequence, our filtering strategy has a limited effect in this setting.

[132] figure: Table 10 : Safety-net Filtering. This table shows student accuracy when using Safety-Net filtering with α = − 0.2 , 0.5 \alpha=-0.2,0.5 across different filtering keep ratios, with ImageNet-21K and ImageNet-1K as reference sets. ImageNet-21K ImageNet-1K 1% 5% 1% 5% 10% 25% Dataset α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 Caltech-101 86.29% 86.69% 90.67% 91.07% 77.25% 77.25% 83.41% 83.81% 86.81% 85.20% 86.06% 85.83% CIFAR-10 74.62% 76.75% 83.83% 85.44% 58.07% 58.59% 69.97% 68.27% 73.51% 72.56% 77.00% 78.26% CUB-200 80.53% 81.21% 82.06% 82.06% 15.48% 15.78% 41.26% 39.61% 52.54% 52.50% 48.39% 49.15% DTD 68.09% 66.70% 70.59% 70.48% 53.62% 51.65% 60.16% 60.11% 61.81% 62.29% 61.28% 62.77% FGVC-Aircraft 44.58% 43.23% 46.56% 45.66% 10.29% 10.35% 18.15% 18.24% 27.00% 26.82% 21.39% 22.50% Food-101 71.66% 70.91% 76.70% 75.94% 24.59% 22.51% 43.52% 42.07% 54.23% 53.81% 48.72% 48.41% Oxford-Flowers-102 97.35% 97.53% 98.42% 98.44% 38.61% 33.44% 62.21% 64.25% 73.83% 74.70% 64.53% 76.00% Oxford-IIIT-Pet 90.87% 90.98% 90.87% 91.11% 84.66% 84.08% 89.21% 88.91% 89.64% 89.23% 89.45% 89.53% Places365 31.59% 30.26% 39.21% 38.33% 18.00% 15.84% 30.14% 29.23% 35.71% 35.14% 37.90% 37.32% RESISC45 75.65% 72.81% 82.06% 79.83% 44.84% 36.32% 68.62% 63.95% 76.52% 73.44% 75.56% 74.02%

[133] figure: Table 11 : Medical Datasets Safety-net Filtering. This table shows student accuracy when using Safety-Net filtering with α = − 0.2 , 0.5 \alpha=-0.2,0.5 across different filtering keep ratios, with ImageNet-21K and ImageNet-1K as reference sets. ImageNet-21K ImageNet-1K 1% 5% 1% 5% Dataset α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 α = − 0.2 \alpha\!=\!-0.2 α = 0.5 \alpha\!=\!0.5 BloodMNIST 41.45% 47.00% 56.71% 45.19% 38.91% 42.03% 45.31% 48.44% DermaMNIST 38.05% 47.58% 68.33% 68.33% 51.67% 53.42% 57.06% 57.91% NCT-CRC-HE-100K 32.37% 32.57% 41.89% 37.54% 23.79% 28.23% 33.88% 39.47% RetinaMNIST 55.00% 55.25% 63.25% 61.25% 53.75% 55.75% 58.50% 58.25%

[134] h2: Appendix C Energy Filtering Visualizations

[135] p: Energy-based filtering is our primary mechanism for selecting a small, informative subset of the reference set. For each reference image x x , we score it using the teacher trained on the target dataset and compute its logit energy ( Equation 5 ), where lower energy indicates a more confident and concentrated prediction over the target classes. We then rank all reference images by energy and keep only the lowest p % p\% . Intuitively, this procedure removes reference images for which the teacher produces diffuse (high-uncertainty) logits, which are unlikely to correspond to any target concept and would otherwise introduce noisy pseudo-labels.

[136] p: Figures 6 and 7 visualize this ranking for three representative targets (Oxford-Flowers102, DTD, and FGVC-Aircraft). Each row fixes the target teacher, and columns sweep over energy percentiles (left → \rightarrow right). The low-energy tail (left) is dominated by images that are visually and semantically aligned with the target domain—e.g., flower close-ups for Oxford-Flowers102, texture-like patterns for DTD, and aircraft/nearby vehicle imagery for FGVC-Aircraft. As we move toward higher percentiles (right), the samples become increasingly unrelated, illustrating that retaining high-energy images would primarily add label noise. Comparing the two reference sets, ImageNet-21K typically yields closer semantic neighbors than ImageNet-1K, reflecting its larger scale and diversity.

[137] p: Figures 8 and 9 zoom into the extreme low-energy region for all ten natural-image benchmarks. Across datasets, the retrieved images at very small percentiles look like canonical exemplars of the target concepts (birds for CUB-200, food dishes for Food-101, flowers for Oxford-Flowers, pets for Oxford-Pets, etc.). This qualitative behavior helps explain why aggressive keep rates (e.g., 1 % 1\% or below) can still provide a strong training signal: the filter concentrates the transmitted supervision on the subset of reference images that the teacher regards as most in-distribution for the target task.

[138] figure: Figure 6 : Energy percentiles on ImageNet-1K. For three target tasks (rows: Oxford-Flowers102, DTD, FGVC-Aircraft), we score every ImageNet-1K image using the corresponding target teacher and sort the reference set by logit energy ( Equation 5 ; lower is better). We then show exemplar reference images at fixed energy percentiles (columns). The horizontal bar under each row visualizes the full energy range over the entire reference set (dashed ticks mark the sampled percentiles). As the percentile increases (left → \rightarrow right), samples transition from target-aligned content (flowers/texture patterns/aircraft) to increasingly irrelevant images.

[139] figure: Figure 7 : Energy percentiles on ImageNet-21K. Same visualization as Figure 6 but using ImageNet-21K (14.2M images) as the reference set. The larger and more diverse dataset typically provides closer semantic neighbors in the low-energy tail (e.g., more flower varieties and texture-like patterns).

[140] figure: Figure 8 : Low-energy reference images (ImageNet-1K). For each target teacher (rows; top-to-bottom: Caltech-101, CIFAR-10, CUB-200, DTD, FGVC-Aircraft, Food-101, Oxford-Flowers, Oxford-Pets, Places365, RESISC45), we show ImageNet-1K reference images drawn from increasingly larger low-energy percentiles (columns: 0.0001%–1.5%). The extreme low-energy tail tends to contain canonical instances of the target concepts (e.g., birds for CUB-200, food dishes for Food-101, flowers for Oxford-Flowers).

[141] figure: Figure 9 : Low-energy reference images (ImageNet-21K). Same as Figure 8 but using ImageNet-21K as the reference set. The larger reference set yields a richer and often more semantically aligned set of low-energy exemplars across targets, consistent with the higher student accuracy obtained with ImageNet-21K as the reference set in Table 1 .

[142] h2: Appendix D Extended Methodology

[143] p: In this appendix, we provide mathematical formulations and implementations for the additional filtering, labeling, and training strategies investigated in this work. Although these methods demonstrated reasonable performance, they did not outperform the primary PLADA method introduced in the main text.

[144] h3: D.1 Uncertainty Metrics

[145] p: Let f θ ​ ( 𝐱 ) ∈ ℝ C f_{\theta}(\mathbf{x})\in\mathbb{R}^{C} denote the logits output by the teacher model for an input 𝐱 \mathbf{x} , and let T T be the temperature scaling parameter.

[146] h5: Energy Score.

[147] p: We utilize the free energy function, commonly used for out-of-distribution detection ( Liu et al., 2020 ) . The energy maps the logit distribution to a scalar value, where lower energy implies higher likelihood (higher confidence):

[148] table: E ( 𝐱 ; T ) = − T ⋅ log ∑ j = 1 C exp ( f θ ​ ( 𝐱 ) j T ) E(\mathbf{x};T)=-T\cdot\log\sum_{j=1}^{C}\exp\left(\frac{f_{\theta}(\mathbf{x})_{j}}{T}\right) (8)

[149] h5: Entropy Score.

[150] p: We compute the Shannon entropy of the predictive distribution obtained via the softmax function, 𝐩 = σ ⁡ ( f θ ​ ( 𝐱 ) / T ) \mathbf{p}=\sigma(f_{\theta}(\mathbf{x})/T) :

[151] table: H ( 𝐱 ) = − ∑ j = 1 C p j log p j H(\mathbf{x})=-\sum_{j=1}^{C}p_{j}\log p_{j} (9)

[152] p: where higher entropy indicates higher uncertainty (lower confidence).

[153] h3: D.2 Filtering Strategies

[154] h4: D.2.1 Rank Normalization

[155] p: Directly comparing raw scores (e.g., Energy vs. Entropy) is difficult due to differing scales and distributions. We therefore convert scores into normalized ranks. Let 𝒮 = { s 1 , … , s N } \mathcal{S}=\{s_{1},\dots,s_{N}\} be the raw scores for the entire dataset. The normalized rank r i ∈ [ 0 , 1 ] r_{i}\in[0,1] for image i i is defined as:

[156] table: r i = rank ​ ( s i ) N − 1 r_{i}=\frac{\text{rank}(s_{i})}{N-1} (10)

[157] p: where rank ​ ( s i ) \text{rank}(s_{i}) is the 0-based index of s i s_{i} in the sorted array of scores (ascending order, such that r i = 0 r_{i}=0 represents the ”best” score, i.e., lowest uncertainty).

[158] h4: D.2.2 Consensus (Intersection) Filtering

[159] p: To combine multiple filtering criteria (denoted M 1 , … , M m M_{1},\dots,M_{m} ), we seek samples that are highly ranked across all methods. We define the consensus cost c i c_{i} for image i i as the maximum normalized rank assigned by any constituent method:

[160] table: c i = max k = 1 m ⁡ ( r i ( M k ) ) c_{i}=\max_{k=1}^{m}\left(r_{i}^{(M_{k})}\right) (11)

[161] p: We then select the subset of indices ℐ k ​ e ​ e ​ p \mathcal{I}_{keep} corresponding to the smallest values c i c_{i} such that | ℐ k ​ e ​ e ​ p | = ⌊ N ⋅ β ⌋ |\mathcal{I}_{keep}|=\lfloor N\cdot\beta\rfloor , where β \beta is the keep ratio. This intersection strategy ensures that any selected image belongs to the top percentile of every applied filter.

[162] h3: D.3 Labeling Variants

[163] p: Standard Knowledge Distillation (KD) ( Hinton et al., 2015 ) is typically more effective when using soft labels ( Qin et al., 2024 ) ; however, this approach incurs a significant transmission overhead compared to hard labels. We explored two methods to approximate the benefits of soft labels while maintaining the low payload cost associated with hard labels. Ultimately, these methods did not outperform the standard use of hard labels.

[164] h4: D.3.1 Average Soft-Labels

[165] p: To capture inter-class similarities, we compute a global prototype for each hard class c ∈ { 1 , … , C } c\in\{1,\dots,C\} . Let 𝒟 c \mathcal{D}_{c} be the set of all proxy images assigned to hard label c c . The average soft label 𝐲 ¯ c ∈ ℝ C \bar{\mathbf{y}}_{c}\in\mathbb{R}^{C} is:

[166] table: 𝐲 ¯ c = 1 | 𝒟 c | ​ ∑ 𝐱 ∈ 𝒟 c σ ⁡ ( f θ ​ ( 𝐱 ) ) \bar{\mathbf{y}}_{c}=\frac{1}{|\mathcal{D}_{c}|}\sum_{\mathbf{x}\in\mathcal{D}_{c}}\sigma(f_{\theta}(\mathbf{x})) (12)

[167] p: During training, if a student image has hard label c c , it trains against the static target 𝐲 ¯ c \bar{\mathbf{y}}_{c} .

[168] h4: D.3.2 Dirichlet Distribution Estimation

[169] p: To model intra-class variance without storing per-sample targets, we assume the soft labels for class c c follow a Dirichlet distribution, 𝐲 ∼ Dir ​ ( 𝜶 c ) \mathbf{y}\sim\text{Dir}(\boldsymbol{\alpha}_{c}) . We estimate the concentration parameters 𝜶 c \boldsymbol{\alpha}_{c} using the Method of Moments.

[170] p: For a specific class c c , let μ j \mu_{j} and σ j 2 \sigma_{j}^{2} be the empirical mean and variance of the probability p j p_{j} across all images in 𝒟 c \mathcal{D}_{c} . We estimate the scalar precision s s based on the statistics of the diagonal entry (the probability of class c c ):

[171] table: s = μ c ​ ( 1 − μ c ) σ c 2 − 1 s=\frac{\mu_{c}(1-\mu_{c})}{\sigma_{c}^{2}}-1 (13)

[172] p: To ensure numerical stability, we clip s ≥ 0.1 s\geq 0.1 . The parameter vector is then derived as:

[173] table: 𝜶 c = 𝝁 ⋅ s \boldsymbol{\alpha}_{c}=\boldsymbol{\mu}\cdot s (14)

[174] p: During training, the target for an image in class c c is sampled as 𝐲 ∼ Dir ​ ( 𝜶 c ) \mathbf{y}\sim\text{Dir}(\boldsymbol{\alpha}_{c}) .

[175] h3: D.4 Training Methods

[176] h4: D.4.1 Loss Function

[177] p: For methods utilizing probabilistic targets (Average Soft-Labels or Dirichlet), we minimize the Kullback-Leibler (KL) Divergence. Let 𝐲 t ​ a ​ r ​ g ​ e ​ t \mathbf{y}_{target} be the soft target and 𝐲 ^ = log ⁡ σ ⁡ ( f s ​ t ​ u ​ d ​ e ​ n ​ t ​ ( 𝐱 ) ) \hat{\mathbf{y}}=\log\sigma(f_{student}(\mathbf{x})) . The loss is:

[178] table: ℒ K ​ L = 1 B ​ ∑ b = 1 B ∑ j = 1 C 𝐲 t ​ a ​ r ​ g ​ e ​ t , j ( b ) ⋅ ( log ⁡ 𝐲 t ​ a ​ r ​ g ​ e ​ t , j ( b ) − 𝐲 ^ j ( b ) ) \mathcal{L}_{KL}=\frac{1}{B}\sum_{b=1}^{B}\sum_{j=1}^{C}\mathbf{y}_{target,j}^{(b)}\cdot\left(\log\mathbf{y}_{target,j}^{(b)}-\hat{\mathbf{y}}_{j}^{(b)}\right) (15)

[179] p: If importance weighting is applied, the loss becomes a weighted sum: ℒ = 1 B ∑ b = 1 B w b ⋅ D K ​ L ( 𝐲 t ​ a ​ r ​ g ​ e ​ t ( b ) | | exp ( 𝐲 ^ ( b ) ) ) . \mathcal{L}=\frac{1}{B}\sum_{b=1}^{B}w_{b}\cdot D_{KL}(\mathbf{y}_{target}^{(b)}||\exp(\hat{\mathbf{y}}^{(b)})).

[180] h4: D.4.2 Importance Weighting

[181] p: We translate uncertainty scores (e.g. energy, entropy, etc.) into importance weights to modulate the loss function. Given scores 𝒮 \mathcal{S} for the active dataset, the weight w i w_{i} for sample i i is computed using a Boltzmann distribution and normalized to unit mean:

[182] table: w i ′ = exp ⁡ ( − s i T w ​ e ​ i ​ g ​ h ​ t ) , w i = w i ′ 1 N ​ ∑ j w j ′ w_{i}^{\prime}=\exp\left(-\frac{s_{i}}{T_{weight}}\right),\quad w_{i}=\frac{w_{i}^{\prime}}{\frac{1}{N}\sum_{j}w_{j}^{\prime}} (16)

[183] p: This assigns higher weights to samples with lower uncertainty scores (lower energy/entropy).

[184] h2: Appendix E Compression Experiments Full Details

[185] p: In this section, we report the compression sizes obtained under different pruning rates. The results illustrate how the pruning rate and the number of classes in the target dataset affect the overall payload size. Each table reports the size of the raw data and the size of the compact representation (obtained by storing labels and indices using the smallest possible integer type), as well as the compressed sizes after applying Huffman coding and Zstandard (Zstd).

[186] p: In addition, we compare two representations for storing the selected indices: integer lists (idx) and binary masks (bmp). In the compact representation, we save the indices using delta encoding—storing the difference from the previous index and casting to uint8 or uint16 where possible. If filtering is not used, the payload size consists only of the hard labels for all images in the reference set.

[187] figure: Table 12 : Compression Summary for Caltech-101, CIFAR-10, CUB-200-2011. In bold we highlight the best compression for every 2 rows (as we also compare between bitmap and delta indices encodings for the pruning bit). ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) p p Raw Compact Huffman Zstd Raw Compact Huffman Zstd 0.1% (Idx) 83.19 KB 69.32 KB 21.66 KB 20.95 KB 7.51 KB 6.25 KB 1.57 KB 1.73 KB 0.1% (Bmp) 1.72 MB 1.71 MB 230.84 KB 21.61 KB 158.89 KB 157.64 KB 20.71 KB 1.62 KB 0.5% (Idx) 415.93 KB 346.61 KB 106.16 KB 95.39 KB 37.53 KB 18.76 KB 8.63 KB 6.77 KB 0.5% (Bmp) 1.83 MB 1.76 MB 289.91 KB 84.14 KB 168.90 KB 162.65 KB 26.05 KB 6.52 KB 1% (Idx) 831.86 KB 415.93 KB 200.09 KB 151.80 KB 75.06 KB 37.53 KB 16.86 KB 12.59 KB 1% (Bmp) 1.96 MB 1.83 MB 360.14 KB 148.91 KB 181.41 KB 168.90 KB 32.57 KB 11.71 KB 5% (Idx) 4.06 MB 2.03 MB 810.29 KB 583.75 KB 375.34 KB 187.67 KB 72.60 KB 50.27 KB 5% (Bmp) 3.05 MB 2.37 MB 883.88 KB 540.18 KB 281.51 KB 218.95 KB 80.67 KB 45.44 KB 10% (Idx) 8.12 MB 4.06 MB 1.44 MB 1.01 MB 750.68 KB 375.34 KB 135.85 KB 91.50 KB 10% (Bmp) 4.40 MB 3.05 MB 1.47 MB 941.23 KB 406.62 KB 281.51 KB 138.95 KB 82.20 KB 25% (Idx) 20.31 MB 10.15 MB 3.28 MB 2.22 MB 1.83 MB 938.35 KB 310.56 KB 206.70 KB 25% (Bmp) 8.46 MB 5.08 MB 3.27 MB 2.04 MB 781.96 KB 469.18 KB 309.26 KB 186.83 KB 50% (Idx) 40.62 MB 13.54 MB 5.92 MB 3.90 MB 3.67 MB 1.22 MB 558.56 KB 357.13 KB 50% (Bmp) 15.23 MB 8.46 MB 5.87 MB 3.78 MB 1.37 MB 781.96 KB 553.09 KB 348.83 KB No Filter 27.08 MB 13.54 MB 9.26 MB 6.15 MB 2.44 MB 1.22 MB 861.51 KB 555.29 KB 0.1% (Idx) 83.19 KB 69.32 KB 14.27 KB 16.97 KB 7.51 KB 6.25 KB 1.36 KB 1.83 KB 0.1% (Bmp) 1.72 MB 1.71 MB 225.39 KB 16.12 KB 158.89 KB 157.64 KB 20.36 KB 1.77 KB 0.5% (Idx) 415.93 KB 346.61 KB 64.99 KB 61.34 KB 37.53 KB 18.76 KB 6.08 KB 5.85 KB 0.5% (Bmp) 1.83 MB 1.76 MB 263.75 KB 55.16 KB 168.90 KB 162.65 KB 23.84 KB 5.64 KB 1% (Idx) 831.86 KB 693.21 KB 126.72 KB 107.64 KB 75.06 KB 37.53 KB 11.88 KB 10.59 KB 1% (Bmp) 1.96 MB 1.83 MB 312.04 KB 97.01 KB 181.41 KB 168.90 KB 28.34 KB 9.93 KB 5% (Idx) 4.06 MB 2.03 MB 630.74 KB 440.13 KB 375.34 KB 187.67 KB 59.05 KB 45.10 KB 5% (Bmp) 3.05 MB 2.37 MB 731.43 KB 401.63 KB 281.51 KB 218.95 KB 68.02 KB 39.91 KB 10% (Idx) 8.12 MB 4.06 MB 1.15 MB 818.21 KB 750.68 KB 375.34 KB 104.41 KB 76.93 KB 10% (Bmp) 4.40 MB 3.05 MB 1.18 MB 759.21 KB 406.62 KB 281.51 KB 110.48 KB 67.80 KB 25% (Idx) 20.31 MB 10.15 MB 2.59 MB 1.99 MB 1.83 MB 938.35 KB 224.10 KB 166.46 KB 25% (Bmp) 8.46 MB 5.08 MB 2.54 MB 1.83 MB 781.96 KB 469.18 KB 223.66 KB 149.08 KB 50% (Idx) 40.62 MB 13.54 MB 4.34 MB 3.45 MB 3.67 MB 1.22 MB 392.00 KB 291.59 KB 50% (Bmp) 15.23 MB 8.46 MB 4.26 MB 3.27 MB 1.37 MB 781.96 KB 380.68 KB 280.51 KB No Filter 27.08 MB 13.54 MB 5.35 MB 4.31 MB 2.44 MB 1.22 MB 488.71 KB 397.41 KB 0.1% (Idx) 83.19 KB 69.32 KB 19.56 KB 16.12 KB 7.51 KB 6.25 KB 1.17 KB 1.36 KB 0.1% (Bmp) 1.72 MB 1.71 MB 233.01 KB 14.07 KB 158.89 KB 157.64 KB 20.53 KB 1.08 KB 0.5% (Idx) 415.93 KB 346.61 KB 87.61 KB 53.37 KB 37.53 KB 31.27 KB 5.12 KB 3.94 KB 0.5% (Bmp) 1.83 MB 1.76 MB 297.93 KB 45.48 KB 168.90 KB 162.65 KB 24.42 KB 3.15 KB 1% (Idx) 831.86 KB 693.21 KB 169.38 KB 97.41 KB 75.06 KB 62.55 KB 12.38 KB 9.00 KB 1% (Bmp) 1.96 MB 1.83 MB 375.60 KB 84.83 KB 181.41 KB 168.90 KB 30.39 KB 7.86 KB 5% (Idx) 4.06 MB 2.03 MB 916.85 KB 643.00 KB 375.34 KB 187.67 KB 79.67 KB 62.05 KB 5% (Bmp) 3.05 MB 2.37 MB 1.00 MB 620.14 KB 281.51 KB 218.95 KB 89.24 KB 58.36 KB 10% (Idx) 8.12 MB 4.06 MB 1.76 MB 1.36 MB 750.68 KB 375.34 KB 157.59 KB 129.12 KB 10% (Bmp) 4.40 MB 3.05 MB 1.78 MB 1.30 MB 406.62 KB 281.51 KB 161.13 KB 120.80 KB 25% (Idx) 20.31 MB 10.15 MB 4.13 MB 3.48 MB 1.83 MB 938.35 KB 372.65 KB 314.23 KB 25% (Bmp) 8.46 MB 5.08 MB 4.09 MB 3.33 MB 781.96 KB 469.18 KB 370.30 KB 299.80 KB 50% (Idx) 40.62 MB 20.31 MB 7.56 MB 6.58 MB 3.67 MB 1.22 MB 694.00 KB 578.75 KB 50% (Bmp) 15.23 MB 8.46 MB 7.43 MB 6.34 MB 1.37 MB 781.96 KB 679.95 KB 569.95 KB No Filter 27.08 MB 13.54 MB 12.09 MB 10.50 MB 2.44 MB 1.22 MB 1.09 MB 934.45 KB

[188] figure: Table 13 : Compression Summary for DTD, FGVC-AIRCRAFT, FOOD-101 ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) p p Raw Compact Huffman Zstd Raw Compact Huffman Zstd 0.1% (Idx) 83.19 KB 69.32 KB 21.10 KB 22.48 KB 7.51 KB 3.75 KB 1.46 KB 1.61 KB 0.1% (Bmp) 1.72 MB 1.71 MB 230.01 KB 23.76 KB 158.89 KB 157.64 KB 20.55 KB 1.91 KB 0.5% (Idx) 415.93 KB 207.96 KB 102.81 KB 91.67 KB 37.53 KB 18.76 KB 7.94 KB 7.50 KB 0.5% (Bmp) 1.83 MB 1.76 MB 286.34 KB 95.17 KB 168.90 KB 162.65 KB 25.03 KB 7.47 KB 1% (Idx) 831.86 KB 415.93 KB 197.48 KB 175.57 KB 75.06 KB 37.53 KB 15.83 KB 14.57 KB 1% (Bmp) 1.96 MB 1.83 MB 356.29 KB 174.52 KB 181.41 KB 168.90 KB 30.75 KB 13.98 KB 5% (Idx) 4.06 MB 2.03 MB 846.35 KB 743.57 KB 375.34 KB 187.67 KB 71.96 KB 65.29 KB 5% (Bmp) 3.05 MB 2.37 MB 900.91 KB 700.65 KB 281.51 KB 218.95 KB 77.12 KB 58.62 KB 10% (Idx) 8.12 MB 4.06 MB 1.51 MB 1.33 MB 750.68 KB 375.34 KB 133.70 KB 122.18 KB 10% (Bmp) 4.40 MB 3.05 MB 1.52 MB 1.25 MB 406.62 KB 281.51 KB 134.46 KB 109.68 KB 25% (Idx) 20.31 MB 10.15 MB 3.29 MB 2.92 MB 1.83 MB 938.35 KB 295.75 KB 264.04 KB 25% (Bmp) 8.46 MB 5.08 MB 3.26 MB 2.74 MB 781.96 KB 469.18 KB 292.71 KB 241.75 KB 50% (Idx) 40.62 MB 13.54 MB 5.69 MB 4.93 MB 3.67 MB 1.22 MB 516.89 KB 434.73 KB 50% (Bmp) 15.23 MB 8.46 MB 5.65 MB 4.79 MB 1.37 MB 781.96 KB 512.48 KB 426.67 KB No Filter 27.08 MB 13.54 MB 8.42 MB 7.05 MB 2.44 MB 1.22 MB 764.40 KB 626.21 KB 0.1% (Idx) 83.19 KB 69.32 KB 19.33 KB 23.38 KB 7.51 KB 6.25 KB 1.75 KB 2.53 KB 0.1% (Bmp) 1.72 MB 1.71 MB 230.82 KB 22.95 KB 158.89 KB 157.64 KB 20.80 KB 2.55 KB 0.5% (Idx) 415.93 KB 346.61 KB 95.21 KB 112.46 KB 37.53 KB 18.76 KB 8.62 KB 9.69 KB 0.5% (Bmp) 1.83 MB 1.76 MB 283.53 KB 100.20 KB 168.90 KB 162.65 KB 25.55 KB 9.67 KB 1% (Idx) 831.86 KB 415.93 KB 184.86 KB 195.50 KB 75.06 KB 37.53 KB 16.57 KB 18.53 KB 1% (Bmp) 1.96 MB 1.83 MB 350.40 KB 189.62 KB 181.41 KB 168.90 KB 31.57 KB 17.41 KB 5% (Idx) 4.06 MB 2.03 MB 833.67 KB 853.52 KB 375.34 KB 187.67 KB 74.00 KB 79.67 KB 5% (Bmp) 3.05 MB 2.37 MB 898.83 KB 803.97 KB 281.51 KB 218.95 KB 80.20 KB 73.73 KB 10% (Idx) 8.12 MB 4.06 MB 1.54 MB 1.56 MB 750.68 KB 375.34 KB 140.83 KB 146.98 KB 10% (Bmp) 4.40 MB 3.05 MB 1.56 MB 1.49 MB 406.62 KB 281.51 KB 141.38 KB 136.31 KB 25% (Idx) 20.31 MB 10.15 MB 3.57 MB 3.53 MB 1.83 MB 938.35 KB 327.00 KB 332.79 KB 25% (Bmp) 8.46 MB 5.08 MB 3.54 MB 3.36 MB 781.96 KB 469.18 KB 323.50 KB 309.20 KB 50% (Idx) 40.62 MB 13.54 MB 6.48 MB 6.18 MB 3.67 MB 1.22 MB 596.62 KB 570.83 KB 50% (Bmp) 15.23 MB 8.46 MB 6.43 MB 6.03 MB 1.37 MB 781.96 KB 591.94 KB 562.64 KB No Filter 27.08 MB 13.54 MB 10.19 MB 9.35 MB 2.44 MB 1.22 MB 940.98 KB 857.63 KB 0.1% (Idx) 83.19 KB 69.32 KB 20.79 KB 19.50 KB 7.51 KB 6.25 KB 1.38 KB 1.67 KB 0.1% (Bmp) 1.72 MB 1.71 MB 232.39 KB 17.98 KB 158.89 KB 157.64 KB 20.62 KB 1.53 KB 0.5% (Idx) 415.93 KB 346.61 KB 97.64 KB 79.87 KB 37.53 KB 18.76 KB 7.42 KB 6.62 KB 0.5% (Bmp) 1.83 MB 1.76 MB 296.48 KB 74.94 KB 168.90 KB 162.65 KB 25.46 KB 6.45 KB 1% (Idx) 831.86 KB 415.93 KB 197.60 KB 158.06 KB 75.06 KB 37.53 KB 16.70 KB 15.24 KB 1% (Bmp) 1.96 MB 1.83 MB 376.51 KB 155.19 KB 181.41 KB 168.90 KB 32.34 KB 14.51 KB 5% (Idx) 4.06 MB 2.03 MB 942.85 KB 840.43 KB 375.34 KB 187.67 KB 83.94 KB 82.62 KB 5% (Bmp) 3.05 MB 2.37 MB 999.63 KB 802.00 KB 281.51 KB 218.95 KB 87.62 KB 77.31 KB 10% (Idx) 8.12 MB 4.06 MB 1.72 MB 1.58 MB 750.68 KB 375.34 KB 155.74 KB 155.63 KB 10% (Bmp) 4.40 MB 3.05 MB 1.71 MB 1.50 MB 406.62 KB 281.51 KB 155.20 KB 142.45 KB 25% (Idx) 20.31 MB 10.15 MB 3.80 MB 3.57 MB 1.83 MB 938.35 KB 342.20 KB 341.08 KB 25% (Bmp) 8.46 MB 5.08 MB 3.75 MB 3.38 MB 781.96 KB 469.18 KB 339.64 KB 314.62 KB 50% (Idx) 40.62 MB 13.54 MB 6.64 MB 6.18 MB 3.67 MB 1.22 MB 599.40 KB 582.58 KB 50% (Bmp) 15.23 MB 8.46 MB 6.61 MB 6.05 MB 1.37 MB 781.96 KB 597.40 KB 562.63 KB No Filter 27.08 MB 13.54 MB 10.19 MB 9.38 MB 2.44 MB 1.22 MB 924.77 KB 871.44 KB

[189] figure: Table 14 : Compression Summary for Oxford-Flowers102, Oxford-IIIT-Pet, Places365. Note that compression is less effective on Places365 due to its larger number of classes and reduced redundancy. ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) p p Raw Compact Huffman Zstd Raw Compact Huffman Zstd 0.1% (Idx) 83.19 KB 69.32 KB 18.69 KB 15.95 KB 7.51 KB 6.25 KB 0.96 KB 1.32 KB 0.1% (Bmp) 1.72 MB 1.71 MB 231.20 KB 14.31 KB 158.89 KB 157.64 KB 20.37 KB 1.13 KB 0.5% (Idx) 415.93 KB 346.61 KB 87.85 KB 60.86 KB 37.53 KB 18.76 KB 7.23 KB 6.80 KB 0.5% (Bmp) 1.83 MB 1.76 MB 292.83 KB 51.47 KB 168.90 KB 162.65 KB 24.94 KB 7.07 KB 1% (Idx) 831.86 KB 693.21 KB 168.27 KB 107.58 KB 75.06 KB 37.53 KB 16.24 KB 14.81 KB 1% (Bmp) 1.96 MB 1.83 MB 366.74 KB 90.95 KB 181.41 KB 168.90 KB 31.97 KB 14.31 KB 5% (Idx) 4.06 MB 2.03 MB 801.74 KB 585.52 KB 375.34 KB 187.67 KB 82.33 KB 78.01 KB 5% (Bmp) 3.05 MB 2.37 MB 942.21 KB 558.34 KB 281.51 KB 218.95 KB 88.58 KB 72.10 KB 10% (Idx) 8.12 MB 4.06 MB 1.53 MB 1.19 MB 750.68 KB 375.34 KB 156.76 KB 145.79 KB 10% (Bmp) 4.40 MB 3.05 MB 1.60 MB 1.15 MB 406.62 KB 281.51 KB 157.31 KB 135.94 KB 25% (Idx) 20.31 MB 10.15 MB 3.70 MB 3.12 MB 1.83 MB 938.35 KB 355.21 KB 325.23 KB 25% (Bmp) 8.46 MB 5.08 MB 3.67 MB 2.98 MB 781.96 KB 469.18 KB 353.43 KB 305.19 KB 50% (Idx) 40.62 MB 20.31 MB 6.83 MB 5.99 MB 3.67 MB 1.22 MB 638.19 KB 551.53 KB 50% (Bmp) 15.23 MB 8.46 MB 6.72 MB 5.74 MB 1.37 MB 781.96 KB 629.88 KB 533.90 KB No Filter 27.08 MB 13.54 MB 10.66 MB 9.09 MB 2.44 MB 1.22 MB 1000.91 KB 787.84 KB 0.1% (Idx) 83.19 KB 69.32 KB 17.85 KB 16.54 KB 7.51 KB 6.25 KB 1.62 KB 1.94 KB 0.1% (Bmp) 1.72 MB 1.71 MB 230.72 KB 14.98 KB 158.89 KB 157.64 KB 20.66 KB 1.74 KB 0.5% (Idx) 415.93 KB 346.61 KB 78.89 KB 64.69 KB 37.53 KB 31.27 KB 7.47 KB 6.46 KB 0.5% (Bmp) 1.83 MB 1.76 MB 284.03 KB 57.51 KB 168.90 KB 162.65 KB 25.62 KB 5.41 KB 1% (Idx) 831.86 KB 415.93 KB 153.19 KB 119.06 KB 75.06 KB 62.55 KB 14.02 KB 10.83 KB 1% (Bmp) 1.96 MB 1.83 MB 347.45 KB 115.40 KB 181.41 KB 168.90 KB 31.68 KB 8.84 KB 5% (Idx) 4.06 MB 2.03 MB 777.64 KB 690.47 KB 375.34 KB 187.67 KB 58.95 KB 39.16 KB 5% (Bmp) 3.05 MB 2.37 MB 851.69 KB 658.45 KB 281.51 KB 218.95 KB 74.57 KB 35.13 KB 10% (Idx) 8.12 MB 4.06 MB 1.50 MB 1.36 MB 750.68 KB 375.34 KB 108.29 KB 75.07 KB 10% (Bmp) 4.40 MB 3.05 MB 1.48 MB 1.30 MB 406.62 KB 281.51 KB 120.47 KB 68.14 KB 25% (Idx) 20.31 MB 10.15 MB 3.34 MB 3.11 MB 1.83 MB 938.35 KB 290.74 KB 221.75 KB 25% (Bmp) 8.46 MB 5.08 MB 3.29 MB 2.94 MB 781.96 KB 469.18 KB 280.72 KB 210.13 KB 50% (Idx) 40.62 MB 13.54 MB 5.75 MB 5.27 MB 3.67 MB 1.22 MB 536.90 KB 426.33 KB 50% (Bmp) 15.23 MB 8.46 MB 5.71 MB 5.12 MB 1.37 MB 781.96 KB 521.38 KB 422.65 KB No Filter 27.08 MB 13.54 MB 8.31 MB 7.38 MB 2.44 MB 1.22 MB 779.40 KB 626.22 KB 0.1% (Idx) 83.19 KB 83.19 KB 20.99 KB 21.11 KB 7.51 KB 7.51 KB 1.82 KB 2.27 KB 0.1% (Bmp) 1.72 MB 1.72 MB 231.18 KB 21.80 KB 158.89 KB 158.89 KB 20.80 KB 2.29 KB 0.5% (Idx) 415.93 KB 277.29 KB 107.31 KB 89.19 KB 37.53 KB 25.02 KB 8.94 KB 8.23 KB 0.5% (Bmp) 1.83 MB 1.83 MB 296.30 KB 91.05 KB 168.90 KB 168.90 KB 26.28 KB 8.12 KB 1% (Idx) 831.86 KB 554.57 KB 217.09 KB 183.05 KB 75.06 KB 50.04 KB 18.19 KB 16.12 KB 1% (Bmp) 1.96 MB 1.96 MB 381.59 KB 177.56 KB 181.41 KB 181.41 KB 33.70 KB 15.24 KB 5% (Idx) 4.06 MB 2.71 MB 995.15 KB 820.58 KB 375.34 KB 250.23 KB 91.88 KB 74.87 KB 5% (Bmp) 3.05 MB 3.05 MB 1.05 MB 778.06 KB 281.51 KB 281.51 KB 98.31 KB 71.98 KB 10% (Idx) 8.12 MB 5.42 MB 1.83 MB 1.49 MB 750.68 KB 500.45 KB 177.37 KB 142.36 KB 10% (Bmp) 4.40 MB 4.40 MB 1.87 MB 1.41 MB 406.62 KB 406.62 KB 179.47 KB 136.92 KB 25% (Idx) 20.31 MB 13.54 MB 4.24 MB 3.36 MB 1.83 MB 1.22 MB 405.40 KB 328.15 KB 25% (Bmp) 8.46 MB 8.46 MB 4.23 MB 3.23 MB 781.96 KB 781.96 KB 403.47 KB 308.28 KB 50% (Idx) 40.62 MB 20.31 MB 7.87 MB 6.02 MB 3.67 MB 1.83 MB 728.51 KB 591.22 KB 50% (Bmp) 15.23 MB 15.23 MB 7.77 MB 5.94 MB 1.37 MB 1.37 MB 723.03 KB 584.04 KB No Filter 27.08 MB 27.08 MB 12.83 MB 10.50 MB 2.44 MB 2.44 MB 1.14 MB 1020.62 KB

[190] figure: Table 15 : Compression Summary for RESISC45 ImageNet-21K (14.2M images) ImageNet-1K (1.2M images) p p Raw Compact Huffman Zstd Raw Compact Huffman Zstd 0.1% (Idx) 83.19 KB 41.59 KB 19.83 KB 22.82 KB 7.51 KB 3.75 KB 1.79 KB 2.35 KB 0.1% (Bmp) 1.72 MB 1.71 MB 226.58 KB 25.10 KB 158.89 KB 157.64 KB 20.44 KB 3.03 KB 0.5% (Idx) 415.93 KB 207.96 KB 87.16 KB 94.19 KB 37.53 KB 18.76 KB 8.58 KB 9.92 KB 0.5% (Bmp) 1.83 MB 1.76 MB 270.34 KB 91.43 KB 168.90 KB 162.65 KB 24.27 KB 10.31 KB 1% (Idx) 831.86 KB 415.93 KB 162.79 KB 172.20 KB 75.06 KB 37.53 KB 16.18 KB 18.20 KB 1% (Bmp) 1.96 MB 1.83 MB 328.04 KB 168.22 KB 181.41 KB 168.90 KB 29.27 KB 17.95 KB 5% (Idx) 4.06 MB 2.03 MB 668.71 KB 689.10 KB 375.34 KB 187.67 KB 68.82 KB 72.35 KB 5% (Bmp) 3.05 MB 2.37 MB 799.48 KB 643.86 KB 281.51 KB 218.95 KB 71.90 KB 68.78 KB 10% (Idx) 8.12 MB 2.71 MB 1.16 MB 1.11 MB 750.68 KB 375.34 KB 125.58 KB 131.29 KB 10% (Bmp) 4.40 MB 3.05 MB 1.32 MB 1.10 MB 406.62 KB 281.51 KB 125.71 KB 119.15 KB 25% (Idx) 20.31 MB 6.77 MB 2.33 MB 2.26 MB 1.83 MB 625.57 KB 268.46 KB 256.22 KB 25% (Bmp) 8.46 MB 5.08 MB 2.50 MB 2.24 MB 781.96 KB 469.18 KB 267.25 KB 256.71 KB 50% (Idx) 40.62 MB 33.85 MB 4.13 MB 2.65 MB 3.67 MB 1.22 MB 455.29 KB 447.08 KB 50% (Bmp) 15.23 MB 8.46 MB 3.60 MB 2.69 MB 1.37 MB 781.96 KB 454.43 KB 443.60 KB No Filter 27.08 MB 13.54 MB 4.32 MB 2.79 MB 2.44 MB 1.22 MB 648.31 KB 620.88 KB

[191] figure: Table 16 : Compression Summary Over All Datasets: ImageNet-1K (1.2M images). This table summarizes the compression results over all of the datasets for all p p values. The values in the table are min-max sizes. p p Raw Compact Huffman Zstd 0.1% 7.51–158.89 KB 3.75–157.64 KB 1.46–20.71 KB 1.08–2.53 KB 0.5% 37.53–168.90 KB 18.76–168.90 KB 7.23–26.28 KB 3.15–9.92 KB 1% 181.41 KB 168.90–181.41 KB 28.34–33.70 KB 7.86–17.95 KB 5% 281.51 KB 218.95–281.51 KB 68.02–98.31 KB 35.13–77.31 KB 10% 406.62 KB 281.51–406.62 KB 110.48–179.47 KB 67.80–142.45 KB 25% 0.76–1.83 MB 469.18–781.96 KB 223.66–403.47 KB 149.08–314.62 KB 50% 1.37 MB 0.76–1.37 MB 380.68–723.03 KB 280.51–584.04 KB 100% 2.44 MB 1.22–2.44 MB 0.48–1.14 MB 397.41–1020.62 KB

[192] figure: Table 17 : Compression Summary Over All Datasets: ImageNet-21K (14.2M images). In comparison to Table 16 , the payloads are roughly 10-12x larger. p p Raw Compact Huffman Zstd 0.1% 0.08–1.72 MB 0.04–1.71 MB 17.43–233.01 KB 14.07–27.13 KB 0.5% 0.41–1.83 MB 0.20–1.83 MB 77.75–305.21 KB 45.48–108.84 KB 1% 0.81–1.96 MB 0.41–1.96 MB 151.00–396.44 KB 84.83–206.08 KB 5% 3.05 MB 2.37–3.05 MB 0.57–1.10 MB 401.63–877.05 KB 10% 4.40–8.12 MB 2.71–4.40 MB 0.88–1.95 MB 0.67–1.58 MB 25% 8.46 MB 5.08–8.46 MB 1.65–4.34 MB 1.21–3.47 MB 50% 15.23–40.62 MB 8.46–33.85 MB 2.49–7.88 MB 1.87–6.42 MB 100% 27.08 MB 13.54–27.08 MB 2.29–12.83 MB 1.77–10.50 MB

[193] p: 40 , 53

[194] h2: Instructions for reporting errors

[195] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[196] p: Tip: You can select the relevant text first, to include it in your report.

[197] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[198] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
