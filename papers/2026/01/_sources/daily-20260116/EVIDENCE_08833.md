# 08833 necessary exact-v1 evidence

Source: https://arxiv.org/html/2601.08833v1
Fetched2026-10-03. Necessary method/evaluation excerpt, not implementation/runtime replication.

日期仍不确定：v1提交Nov14不等于首公开。Jan15 DataCite创建只支持存在上界，官方排程无法证明滞留稿之前从未公开。实际有限查询发现ESF作者机构preprint11/14字段但未获早正文公开记录。不得作为本窗采用/评分；保留上述证据便于定点重开。

条件结果：两A10040GB、PCIeGen3、Llama-3.2-3B、vLLM V1/LMCache合成RandomDataset、无限到达率、输入16384输出256、batch2–64；原文模型文字与ref31 Hermes3存在身份歧义。equal two-GPU colocation切半batch在低batch TTFT优于P/D；高batch KV容量eviction反侧；DVFS0.36–1.26 GHz batch16下能耗未优。不是NVLink、在线mixed SLO、生产调度普遍否定。diskTPOT异常作者未解，precision/软件版本/统计重复Not Disclosed。

## Primary excerpt

IV Benchmark Methodology


 IV-A Overview


 Our benchmarking study consists of two main experiments:


 Experiment 1 (Section V-A ):
We benchmark the performance and energy consumption of disaggregated LLM serving under different experimental setups with each differ in KV cache transfer paths, and compare the results with the colocated baselines. We evaluate each experimental setup with increasing request batch sizes that lead to KV caches of varying sizes, and record the resulting performance and energy consumption for each case. Based on that we analyze how the benefits of prefill–decode disaggregation evolve as KV cache size grows.


 Experiment 2 (Section V-B ):
We further evaluate the impact of GPU frequency scaling on performance and energy efficiency between disaggregation and colocation. For each experimental setup, we fix the workload and measure latency and energy consumption at multiple GPU frequency settings. From these measurements, we construct latency–energy Pareto frontiers for both prefill and decode stages. We then compare these frontiers across experimental setups to assess the potential energy-saving benefits in disaggregated serving that are enabled by independent frequency scaling.



 IV-B Hardware


 The benchmark experiment is conducted on a cluster node with two NVIDIA A100 GPUs, each with a GPU memory of 40 GB. These two GPUs are connected to the same PCIe bridge that supports PCIe Gen3. These GPUs support a wide range of frequency scaling from 0.21 GHz to 1.41 GHz. The cluster is also equipped with a 18-cores Intel Xeon E5-2697 v4 CPU with base frequency at 2.3 GHz and boost frequency at 3.6 GHz, as well as a Samsung 1 TB DDR4 Memory and a Samsung 3.2 TB NVMe SSD.



 IV-C Software Stack


 vLLM [ 47 ] : vLLM is an open-source LLM inference engine widely used in both academia and industry. It introduces PagedAttention [ 22 ] , an optimized memory management system that virtualizes the KV cache storage and organizes it in fixed-size pages to minimize memory fragmentation. It also supports continuous batching to efficiently handle variable sequence lengths. In our experiments, each GPU serves a single vLLM process responsible for executing the main inference pipeline. We further adapt vLLM’s benchmarking utility to generate synthetic datasets and collect performance metrics.


 LMCache [ 27 ] : LMCache is an open-source KV cache management engine. It introduces CacheGen [ 26 ] for efficient KV cache compression as well as CacheBlend [ 53 ] to support position-independent reuse for KV cache. LMCache also provides vLLM-compatible connectors that enable KV cache transfer between vLLM processes. In our experiments, we adapt these connectors to implement different KV cache transfer paths inside disaggregated LLM serving.



 IV-D Model and Dataset


 Llama [ 45 ] is a widely used family of open-source large language models released by Meta AI. In our experiments, we specifically employ Llama-3.2-3B [ 31 ] as the target model for benchmarking. To generate controlled and reproducible workloads, we use synthetic data produced by RandomDataset, a dataset generator released from the vLLM stack, which generates synthetic requests by sampling random token sequences of configurable batch size, input length, and output length. In our setup, we use RandomDataset to generate inference workloads with varying batch sizes, and we set the request rate to infinite so that all requests are dispatched to the GPU worker simultaneously.



 IV-E Metrics


 We use Time to First Token ( TTFT ) to evaluate prefill latency and Time per Output Token ( TPOT ) to evaluate decode latency. We also report Prefill Throughput and Decode Throughput respectively. Energy Consumption is obtained by integrating instantaneous power readings over the inference period. We report energy usage across different hardware components. Specifically, instantaneous GPU power is measured by pynvml [ 2 ] , a Python library that provides access to NVIDIA’s Management Library (NVML) [ 32 ] . Instantaneous power by CPU and DRAM is measured by reading the Running Average Power Limit (RAPL) interface [ 39 ] that is supported by Intel processors. We also record the instantaneous total power of the cluster node via reading the Intelligent Platform Management Interface (IPMI) [ 18 ] . For each inference workload, we report energy consumption in joules per token, calculated by dividing the total energy consumed by the total number of tokens processed, including both input and output tokens.



 IV-F Experimental Configurations Setup


 co-2gpus represents our new colocated serving baseline. Different from co-1gpu , this baseline utilizes two GPUs, which provides equivalent GPU resources to that of disaggregated serving setups. In this baseline, each GPU serves a vLLM V1 inference engine that performs both prefill and decode locally. With two complete inference processes, the total batch is evenly divided between the two GPUs, with each handling half of the incoming requests to reduce their compute and memory overhead. In this configuration, each GPU allocates 28 GB of memory for KV cache storage.


 dis-gpu represents the disaggregated serving setup that utilizes GPU peer-to-peer (P2P) communication for KV cache transfer. Specifically, one GPU is dedicated for prefill and the other for decode. P2P KV cache transfer is enabled through a shared PCIe bridge connecting both GPUs within the same node. The software pipeline is implemented using vLLM V1 [ 47 ] and LMCacheConnectorV1 [ 27 ] that orchestrates the inter-GPU communication flow. Underneath, it leverages the NVIDIA Inference Xfer Library (NIXL) [ 30 ] to perform efficient data transfer via the CUDA Inter-Process Communication (cuda_ipc) [ 4 ] transport. This integration allows GPUs to directly access each other’s device memory to achieve higher transfer bandwidth for KV cache exchange.


 dis-cpu represents the disaggregated serving setup that realizes KV cache transfer through CPU offloading. Similar to dis-gpu , one GPU is for prefill and the other is for decode. After the prefill stage, the KV caches are offloaded to the CPU DRAM. The decode GPU loads them back when it starts generating the output tokens. We utilize vLLM V1 and LMCacheConnectorV1 to orchestrate the software pipeline. The allowable CPU memory used for KV cache storage is set to 125 GB. In addition, a shared Redis [ 38 ] lookup server is deployed between the GPUs, where the prefill GPU updates the lookup table after offloading a KV cache block to CPU DRAM, and the decode GPU queries the table to locate and fetch the required KV cache blocks.


 dis-disk represents the disaggregated serving setup that transfers KV cache through disk offloading. Similar to other disaggregated baseline, one GPU is responsible for prefill and the other is for decode. After the prefill stage, KV caches are first offloaded to the disk, and then offloaded back to the decode GPU. For a fair comparison to dis-cpu , we force the kernel to bypass the page cache and perform the complete disk access each time when reading or writing KV caches. vLLM V1 and LMCacheConnectorV1 are employed to implement software-level KV cache transfer, with a maximum of 125 GB of disk space allocated for cache storage. The fs_connector [ 47 ] is used to coordinate KV cache storage and retrieval. Acting as middleware running in CPU DRAM, fs_connector receives KV caches from the prefill GPU before writing them to disk and fetches the corresponding caches from disk to offload them back to the decode GPU.




 V Benchmark Results


 V-A Experiment 1: Varying Batch Size


 Fig. 1: TTFT and TPOT performance as batch size increases across different experimental setups.


 Fig. 2: Prefill and decode throughput as batch size increases across different experimental setups.


 Fig. 3: Total energy consumption as batch size increases across different experimental setups.


 Fig. 4: Energy contributed by each hardware component as batch size increases across different experimental setups.


 We present and analyze the results of Experiment 1, which evaluates the performance and energy consumption of different experimental setups under increasing batch sizes.


 Figure 1 represents the latency result, with the upper sub-figure showing TTFT in the y-axis and the lower sub-figure showing TPOT in the y-axis. Each request is fixed to include an input token size of 16,384 and an output token size of 256. To investigate how KV cache size affects the serving performance and energy efficiency, we increase the batch size (represented by the x-axis) from 2 to 64, leading to the total size of generated KV cache ranging from 3.5 GB to 112 GB. Each line indicates the latency performance achieved by a specific setup, as indicated in the figure legend.


 We first observe that for all setups, median TTFT increases as batch size increases. This is expected, as with more concurrent requests sent to the prefill GPU, less computation resources are allocated to each request, leading to higher latency. Also, among the disaggregated setups, dis-gpu achieves the best TTFT because it only passes one PCIe bridge without touching deeper memory tiers. After that comes the CPU offloading based setup ( dis-cpu ), and then the disk offloading based setup ( dis-disk ). To our surprise, for all cases of batch sizes, co-2gpus is achieving the best TTFT performance, which indicates that prefill-decode disaggregation does not always guarantee performance gains. Under equivalent GPU resources, each GPU under the co-2gpus baseline only needs to process half a batch of the requests. Even with prefill-decode interference, the reduced batch size significantly reduces computation overhead, ultimately leading to an improved TTFT compared to disaggregated setups.


 For TPOT, we notice that only co-2gpus shows a sharp increase when batch size exceeds 32. This is because the total size of the generated KV cache is larger than the allocated GPU memory, causing the previously generated KV cache to be evicted. This part of the KV cache has to be recomputed when the decode stage later requires them, causing a significant delay in token generation. In addition, we observe that dis-disk exhibits a TPOT trend similar to dis-gpu and performs significantly faster than dis-cpu . This result is unexpected, as disk offloading places the KV cache farther from GPU memory and would typically incur higher latency. This phenomenon is currently under investigation.


 Summarizing the latency results leads to our first takeaway: performance gains from prefill-decode disaggregation highly depends on batch size. Under equivalent GPU resources, disaggregated serving could double the batch size compared to colocated serving, resulting in higher overall TTFT. On the other hand, colocated serving suffers performance degradation at larger batch sizes when the amount of KV cache exceeds allocated GPU memory capacity.


 Figure 2 shows the throughput result, with the upper sub-figure for prefill and lower sub-figure for decode. We first observe that, across all disaggregated setups, throughput increases with batch size up to 16, beyond which it plateaus as the GPU’s computational capacity becomes saturated. However, due to the aforementioned GPU memory limitation, co-2gpus experiences a significant drop in throughput when the batch size reaches around 32. In addition, similar to latency, dis-gpu achieves the best performance among disaggregated setups because of the shortest transfer path, followed by dis-cpu and dis-disk .


 Figure 3 shows the total energy consumed by different experimental setups. Across all setups, energy consumption initially decreases and then converges as batch size increases. This behavior arises because static, or standby, energy is amortized over a larger amount of computation as the GPU becomes more fully utilized during inference. For co-2gpus , we also observe a sharp increase in energy consumption when batch size reaches 32, due to KV cache eviction and recomputation. Among disaggregated setups, dis-gpu again achieves the best performance because it takes the least latency to complete the inference workload, and is followed by dis-cpu and dis-disk .


 To further analyze the energy consumption contributed by each hardware component, we present the energy consumption breakdown in Figure 4 . Each bar in the figure represents the energy consumption of an experimental setup under a batch size. Inside each bar, boxes of different colors indicate the energy consumption contributed by each hardware component, as described in the figure legend. We observe that, as the KV cache transfer path touches deeper memory tiers, it consumes more energy from non-GPU hardwares, including CPU, DRAM, and disk.



 V-B Experiment 2: Varying GPU Frequency


 Fig. 5: TTFT-energy and TPOT-energy Pareto frontiers across different experimental setups. The inference workload includes a batch of 16 requests with input size 16,384 and output size 256.


 We discuss the results of benchmarking experiment 2, which investigates the influence of GPU frequency scaling on performance and energy consumption among different experimental setups. The inference workload is fixed to be a batch of 16 requests with input size 16,384 and output size 256.


 Figure 5 shows the result, with the left sub-figure for prefill and the right for decode. The x-axis represents the latency performance, with Median TTFT for prefill and Median TPOT for decode. The y-axis indicates the total energy used for processing the inference workload. The labels associated with the lines represent the GPU frequency, measured in GHz. For all setups, we sample the frequency evenly from 0.36 GHz to 1.26 GHz and set to both GPUs, and measure the achieved latency and energy consumption for prefill and decode stages. This results in two latency-energy Pareto frontiers for each setup.


 We notice that most latency-energy frontiers exhibit a U-curve. As GPU frequency increases, energy consumption decreases initially and increases ultimately. This is because of the marginal latency improvement from GPU frequency. Initially when GPU frequency is low, an increase in GPU frequency leads to a significant reduction in latency. During this period, the reduced latency counters the higher GPU power, and hence leading to decreasing energy consumption. As the GPU frequency approaches a certain threshold (e.g., 0.81 GHz), increasing GPU frequency leads to little improvement in latency. Instead, it increases GPU power and hence results in increasing energy consumption. These U-curve frontiers provide the opportunity to save energy consumption from frequency scaling. Through profiling those frontiers in the offline stage, we can potentially identify and set the GPU to the “sweet spot” frequency that can achieve the lowest GPU power consumption when latency is not constrained. Similarly, under the SLO-aware serving case where constraint is put on latency, we can search along the frontier to locate and set the GPU frequency that can satisfy the latency constraint at the lowest energy consumption.


 We also notice that disaggregated serving setups consume substantially more energy than the colocated baselines. Even with independent frequency scaling, none of the disaggregated setups could outperform the colocated serving baselines in energy consumption. That leads to our second takeaway, independent frequency scaling does not guarantee energy savings. As discussed in the previous section, colocated serving exhibits better TTFT, and comparable TPOT when batch size is smaller. These improved latency performance ultimately leads to lower energy consumption in both prefill and decode stages. Although independent frequency scaling provides with more choices of TTFT and TPOT combinations, none of those combinations leads to a better energy consumption than that of colocated serving. However, though at the cost of higher energy consumption, we notice that dis-gpu and dis-disk provide improved TPOT than colocated serving, making them potential options for requests with tight TPOT requirements.




 VI Conclusion


 In this paper, we argue that existing prefill–decode disaggregated serving frameworks lack a comprehensive evaluation that compares performance and energy efficiency across different KV cache transfer paths. Moreover, although recent serving frameworks have supported optimization techniques such as KV cache reuse and frequency scaling, there remains a lack of systematic benchmarking to assess the performance and energy gains from these techniques under different conditions. To fill this research gap and provide a better understanding of the true performance and energy implications of prefill–decode disaggregation, we conduct a series of benchmarking studies that evaluate multiple experimental setups and optimization strategies. The major takeaways of our experiment are summarized below.



 •

 Performance gains from prefill-decode disaggregation depends on the request load and KV transfer medium. Compared to colocated serving, disaggregation doubles the request amount processed per GPU under equivalent GPU resources, resulting in higher overall TTFT when high-speed KV transfer interconnects are unavailable. However, at higher batch sizes, disaggregated serving outperforms colocated serving in TPOT, as colocated serving starts to suffer from cache eviction and recomputation due to limited GPU memory for KV cache.

 •

 Independent frequency optimization does not guarantee energy saving. Across all KV transfer paths, disaggregated serving introduces longer prefill latency, which results in higher overall energy consumption compared to colocated serving. Although disaggregation enables independent frequency scaling to provide more choices of TTFT and TPOT combinations, none of the configurations ultimately achieve better energy consumption than the colocated baseline.




 We hope those takeaways provide insights and guidance for future works that focus on prefill-decode disaggregated LLM inference serving and energy-aware LLM inference serving.




