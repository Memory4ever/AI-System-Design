# 第1周·第1天：30 个代表性 JD 样本

- **状态：**已完成
- **核验日期：**2026-08-04
- **目标级别：**Senior IC 到 Staff
- **岗位方向：**AI Platform、LLM Serving / Inference、Distributed Training
- **样本配比：**外企 21 个，国内大厂 9 个；每个方向均为 7:3

## 1. 采样口径

本轮只使用公司官方招聘页或官方团队招聘页。职位关闭和职责调整都很常见，因此这些链接用于建立岗位能力基线，不代表未来投递时仍然开放；正式投递前必须重新核验。

样本选择遵循三个原则：

1. 职责与本仓库的 Part III～V 直接相关，而不是泛化的算法、业务后端或纯解决方案销售岗位；
2. 优先覆盖 Senior / Staff 所需的系统设计、性能诊断、生产可靠性和跨团队技术领导信号；
3. 同时保留少量边界岗位，用来观察 Platform、Training 与 Serving 在真实组织中的职责重叠。

表格中的“准备关键词”是对官方 JD 的压缩，不是完整的能力差距结论。统一能力分类和差距排序将在本周后续任务中完成。

## 2. AI Platform：10 个样本

| # | 公司与岗位 | 地点 / 级别信号 | 核心职责摘要 | 准备关键词 | 官方来源 |
| ---: | --- | --- | --- | --- | --- |
| P01 | Apple · MLOps Engineer | 美国；Experienced | 建设覆盖数据、分布式训练、部署与低延迟推理的模型生命周期平台 | Python、Slurm、GPU training、CI/CD、observability、reproducibility | [JD](https://jobs.apple.com/en-us/details/200666044-0865/mlops-engineer?team=MLAI) |
| P02 | OpenAI · Software Engineer, Compute Infrastructure | 美国 / 英国；开放级别 | 将 accelerator、network、storage、scheduler、fleet health 和开发者工具整合为统一计算平台 | Kubernetes、scheduling、RDMA、NCCL、benchmark、reliability | [JD](https://openai.com/careers/software-engineer-compute-infrastructure-san-francisco/) |
| P03 | OpenAI · Software Engineer, Observability | 美国；Experienced | 建设大规模 logging、metrics、tracing 基础设施与内部诊断产品 | distributed storage、time series、OpenTelemetry、Kubernetes、incident debugging | [JD](https://openai.com/careers/software-engineer-observability-san-francisco/) |
| P04 | OpenAI · Software Engineer, Infrastructure Reliability | 英国；4+ 年且有技术领导经历 | 扩展并加固 cloud infrastructure，承担自动化、性能、故障响应和可靠性改进 | distributed systems、Kubernetes、Terraform、SRE、postmortem、security | [JD](https://openai.com/careers/software-engineer-infrastructure-reliability-london-uk/) |
| P05 | OpenAI · Software Engineer, Infrastructure - Analytics Platform | 美国；Experienced | 用 Rust / C++ 建设研究工作负载依赖的高性能数据与分析基础设施 | Rust/C++、partitioning、replication、backpressure、Kubernetes、safe rollout | [JD](https://openai.com/careers/software-engineer-infrastructure-analytics-platform-san-francisco/) |
| P06 | NVIDIA · Senior Software Engineer, DGX Cloud AI Infrastructure | 美国；Senior | 对分布式训练和推理环境进行 bring-up、benchmark、profiling、故障定位与规模化优化 | PyTorch、Megatron、TensorRT-LLM、NCCL、Nsight、cluster debugging | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NvidiaExternalCareerSite/job/US-CA-Santa-Clara/Senior-Software-Engineer--DGX-Cloud-AI-Infrastructure_JR2019246) |
| P07 | NVIDIA · Principal Software Engineer - Dynamo | 美国；Principal | 建设 Dynamo 的 Kubernetes Serving 平台、资源管理和多节点推理基础设施 | Rust/C++、Go、Kubernetes operator、GPU resource、CI/CD、open source | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Principal-Software-Engineer---Dynamo_JR2010290) |
| P08 | 字节跳动 Seed · MLOps 技术专家 | 北京 / 上海 / 杭州；专家 | 面向大模型研发构建 MLOps 与模型生命周期基础设施 | workflow、model lifecycle、platform reliability、developer experience | [JD](https://jobs.bytedance.com/experienced/position/7596956775183632645/detail) |
| P09 | 阿里巴巴智能引擎 · 大模型平台研发工程师-强化学习环境 | 北京 / 杭州；工程师 | 建设大规模 Agent 训练环境的开发、部署、管理和分布式执行能力 | RL environment、orchestration、sandbox、distributed execution、platform API | [JD](https://talent-holding.alibaba.com/off-campus/position-detail?positionId=100006780014) |
| P10 | 阿里巴巴智能引擎 · 大模型平台研发工程师-Agent Infra | 北京 / 杭州；工程师 | 建设 Agent Infra 与大模型基础工程平台，支撑训练、评测和应用链路 | Agent Infra、evaluation、workflow、control plane、cloud native | [JD](https://talent-holding.alibaba.com/off-campus/position-detail?positionId=100018640014) |

### 这一组岗位在问什么

AI Platform 岗位并不等同于“会使用 Kubernetes”。它要求候选人把 GPU、模型资产、工作负载、调度、可观测性、发布和故障恢复组织成可靠的平台能力，并通过 API、自动化和开发者体验放大其他团队的效率。Staff 信号主要来自跨层问题定义、平台边界、长期技术方向和跨团队落地，而不是单个组件的熟练度。

## 3. LLM Serving / Inference：10 个样本

| # | 公司与岗位 | 地点 / 级别信号 | 核心职责摘要 | 准备关键词 | 官方来源 |
| ---: | --- | --- | --- | --- | --- |
| I01 | NVIDIA · AI Inference Performance Engineer | 美国；5+ 年 | 对 TensorRT-LLM、vLLM、SGLang 的量化、调度、内存和分布式推理进行端到端优化 | roofline、profiling、KV cache、batching、CUDA、CUTLASS/Triton | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/AI-Inference-Performance-Engineer_JR2014396) |
| I02 | NVIDIA · Principal Software Engineer - AI Inference | 美国；Principal | 设计高性能 inference runtime，并推进多 GPU、多节点和开源生态落地 | vLLM、SGLang、runtime architecture、C++/Python/CUDA/Rust、technical leadership | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Principal-Software-Engineer---AI-Inference_JR2013753) |
| I03 | NVIDIA · Senior Inference Engineer, AIConfigurator for Dynamo | 美国；Senior，10+ 年 | 用性能模型和配置搜索为 aggregated / disaggregated Serving 选择部署方案 | SLA、Pareto frontier、PD separation、TP/PP/EP、KV cache、Python/Rust | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-Inference-Engineer--AIConfigurator-for-Dynamo_JR2019734) |
| I04 | NVIDIA · Solutions Architect, Inference Deployments | 美国；5+ 年 | 在 Kubernetes 上交付 Dynamo、TensorRT-LLM、vLLM、SGLang 和分离式推理 | Dynamo、Kubernetes、RDMA/UCX、MIG、NIXL、production deployment | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Solutions-Architect--Inference-Deployments_JR2008490) |
| I05 | NVIDIA · Senior Software Engineer, AI Inference Systems | 德国；Senior | 优化 kernel、compiler、scheduler 与多 GPU / 多节点 Serving 执行 | vLLM、kernel fusion、autotuning、MLPerf、parallelism、orchestration | [JD](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Germany-Remote/Senior-Software-Engineer--AI-Inference-Systems_JR2017366) |
| I06 | AWS · Software Development Engineer AI/ML, Inference Serving, Neuron | 美国；5+ 年且有架构领导经历 | 建设 Trainium / Inferentia 上的分布式 Serving、KV 管理、offload 和框架集成 | vLLM、SGLang、Torch XLA、disaggregated serving、custom operator、reliability | [JD](https://amazon.jobs/en/jobs/3089270/software-development-engineer-ai-ml-inference-serving-aws-neuron) |
| I07 | OpenAI · Software Engineer, Inference - Performance Optimization | 美国；深度专家信号 | 从 application、model 到 fleet 建模 latency、capacity、utilization 与 cost-to-serve | microbenchmark、performance model、profiling、fleet scheduling、capacity、cost | [JD](https://openai.com/careers/software-engineer-inference-performance-optimization-san-francisco/) |
| I08 | 字节跳动 Seed · 大模型推理引擎专家 | 北京 / 上海 / 杭州；专家 | 建设高性能大模型推理引擎并推动模型、Runtime 与硬件协同优化 | inference engine、kernel、memory、distributed serving、hardware co-design | [JD](https://jobs.bytedance.com/society/position/detail/7366449232540141861) |
| I09 | 阿里巴巴智能引擎 · 多模态大模型推理系统工程师/专家 | 北京 / 杭州；工程师 / 专家 | 从底层算子到服务调度优化多模态理解与生成模型推理 | multimodal、operator、serving scheduler、latency、throughput、cost | [JD](https://talent-holding.alibaba.com/off-campus/position-detail?positionId=100008580001) |
| I10 | 百度 · 大模型推理工程师 | 北京；社会招聘 | 建设 MaaS 推理服务，优化 batching、KV Cache、弹性、高可用和线上成本 | vLLM/TGI/TensorRT、PagedAttention、dynamic batching、Kubernetes、SLA | [JD](https://talent.baidu.com/jobs/detail/SOCIAL/336e82e0-307f-49f1-ae1f-4831fb9d570e) |

### 这一组岗位在问什么

Serving 岗位共同要求候选人沿完整路径定位瓶颈：模型结构与 kernel 决定单步执行，KV Cache 与 batching 决定显存和并发，scheduler 与网络决定多卡和多节点效率，SLO 与 workload distribution 决定优化是否真正有价值。单独背诵 vLLM、PagedAttention 或某个加速数字不足以证明能力。

## 4. Distributed Training：10 个样本

| # | 公司与岗位 | 地点 / 级别信号 | 核心职责摘要 | 准备关键词 | 官方来源 |
| ---: | --- | --- | --- | --- | --- |
| T01 | OpenAI · Software Engineer, RL Training Infra | 美国；Experienced | 建设异步 RL 训练基础设施，处理 rollout、训练、推理协同和硬件故障 | RL systems、orchestration、async pipeline、scaling、fault tolerance、profiling | [JD](https://openai.com/careers/software-engineer-rl-training-infra-san-francisco/) |
| T02 | OpenAI · Distributed Training Engineer, Sora | 美国；Experienced | 提升多模态模型训练吞吐、硬件效率与训练稳定性 | distributed training、multimodal、kernel optimization、profiling、training dynamics | [JD](https://openai.com/careers/distributed-training-engineer-sora-san-francisco/) |
| T03 | OpenAI · Software Engineer, Productivity - Training Runtime | 美国；Experienced | 改进核心训练 Runtime 周边的开发流程、CI、测试和可靠性 | Python、training runtime、developer productivity、CI、testing、reliability | [JD](https://openai.com/careers/software-engineer-productivity-training-runtime-san-francisco/) |
| T04 | AWS · Sr. Software Engineer, Neuron Distributed Training | 美国；Senior，5+ 年 | 在 PyTorch / JAX / XLA 与 Neuron compiler/runtime 上支持并优化大模型分布式训练 | FSDP、DeepSpeed、NeMo、PyTorch/JAX、XLA、Trainium | [JD](https://www.amazon.jobs/en/jobs/3014888/sr-software-engineer-ai-ml-aws-neuron-distributed-training) |
| T05 | AWS · Software Engineer, Neuron Distributed Training - Performance Optimization | 美国；3+ 年 | 优化训练吞吐、MFU、collective、内存、compiler 和 kernel | collective、memory utilization、compiler、kernel、time-to-convergence、profiling | [JD](https://www.amazon.jobs/en-gb/jobs/3175270/software-engineer-ai-ml-aws-neuron-distributed-training-performance-optimization) |
| T06 | NVIDIA · Senior HPC and AI Networking Performance Research and Analysis Engineer | 中国；Senior，8+ 年 | 分析大规模训练的通信模式、collective、RDMA 和网络瓶颈 | NCCL、MPI、RDMA/RoCE、CUDA、topology、performance methodology | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-HPC-and-AI-Networking-Performance-Research-and-Analysis-Engineer_JR2011937) |
| T07 | NVIDIA · Senior Software Engineer, CUTLASS Performance | 美国；Senior | 从训练与推理 workload 中识别 GEMM、fusion 和 Tensor Core kernel 优化机会 | C++/CUDA、CUTLASS、GEMM、fusion、benchmark、GPU architecture | [JD](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-Software-Engineer--CUTLASS-Performance_JR2018987) |
| T08 | 字节跳动 Seed · 大模型训练优化工程师 | 北京 / 上海 / 杭州；社会招聘 | 优化大模型分布式训练效率、并行执行与软硬件协同 | parallelism、collective、MoE、profiling、kernel、hardware efficiency | [JD](https://jobs.bytedance.com/society/position/detail/7501985034170632456) |
| T09 | 字节跳动 Seed · 大模型训练稳定性和容错系统专家 | 北京 / 上海 / 杭州；专家 | 建设大规模训练的稳定性、故障诊断、容错与恢复体系 | straggler、failure detection、checkpoint、recovery、observability、root cause | [JD](https://jobs.bytedance.com/experienced/position/7655625343685314821/detail) |
| T10 | 阿里巴巴智能引擎 · 大模型训练基础架构研发工程师/高级专家 | 北京 / 杭州；工程师 / 高级专家 | 建设大模型训练基础设施和高效分布式训练框架 | Megatron、parallelism、communication、checkpoint、framework、performance | [JD](https://talent-holding.alibaba.com/off-campus/position-detail?positionId=1038409) |

### 这一组岗位在问什么

Distributed Training 岗位关注的不只是并行策略名称，而是如何把 model shape、global batch、memory budget、collective、topology、compiler/runtime 与故障语义连成可测量的系统。Senior 候选人需要能复现实验并定位瓶颈；Staff 候选人还需要决定优化方向、训练资产契约、恢复边界和跨团队演进路径。

## 5. 第一天结论

这 30 个样本与现有 16 周计划的方向基本一致，但给出了更明确的优先级信号：

1. **共同底座不是框架清单。** Distributed systems、Linux、GPU execution、profiling、benchmark、reliability 和 production ownership 在三类岗位中反复出现。
2. **Kubernetes 主要是平台与分布式 Serving 的执行环境。** 真正的区分度来自 scheduler、state、network、memory、failure 和 workload 的联合推理。
3. **C++ / CUDA 阅读能力不能继续缺席。** Serving 与 Training 的高影响岗位频繁跨到 kernel、compiler、runtime 和 communication library；Python / Go 仍是平台与实验主力。
4. **Staff 信号来自技术杠杆。** 典型表现是定义架构方向、建立性能方法、推动跨团队项目、形成可复用平台抽象，并用 production evidence 约束决策。
5. **本地单机多卡环境足以验证一部分核心能力。** 可以覆盖 profiling、KV / batching、NCCL、并行训练、故障注入和恢复；多节点 RDMA、真实 fleet scheduler 与大规模 failure domain 必须明确标为未验证。

## 6. 下一步输入

下一项任务应以本文件为唯一 JD 样本集，将要求归入：

```text
共同底座
岗位专项
Senior 信号
Staff 信号
```

分类时应保留 `岗位编号 -> 原始 JD -> 能力标签` 的追踪关系，不能只输出脱离职位证据的技能列表。

