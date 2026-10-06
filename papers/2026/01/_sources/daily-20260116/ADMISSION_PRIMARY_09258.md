# 2601.09258v1 决定性准入原段

Exact primary https://arxiv.org/html/2601.09258v1 。仅记录本次实际读的决定性方法/接口/失败段，非完整Evidence或日期/Books验收。

4.1.1 
Collection Methodology
LatencyPrism implements a multi-level tracing system. At the application level, we employ a lightweight probe inspired by PyTorch Dynamo that leverages ptrace to dynamically instrument 
PyFrameObject
. This approach utilizes ptrace to non-intrusively hooks the creation and destruction processes of Python virtual machine frames at runtime, capturing high-fidelity execution context without requiring code modification or process restarts. It extracts metadata such as function name, records call timing with nanosecond precision, and structurally parses arguments and return values. Moreover, it automatically identifies model metadata in mainstream AI frameworks (e.g., vLLM, SGLang) and inserts semantically labeled NVTX or ROCTX range events during key function calls, achieving semantic alignment between GPU kernels and Python logic. The probe also manages reference counting meticulously to avoid interfering with the target process’s garbage collection.
Beyond the application layer, the system integrates mature solutions at other levels: eBPF is used to trace CPU scheduling, network I/O, and system calls in kernel space; CUPTI or ROCm GPUPerfAPI collects underlying GPU activities; for other heterogeneous devices, corresponding 
-smi
 tool outputs are parsed. The system further aggregates micro-events with macro-metrics to achieve full-stack observability.
4.1.2 
Multi-Dimensional Data Correlation
Although GPU event timestamps, CPU-side eBPF probe timestamps, and Python probe timestamps originate from different sources, the LatencyPrism backend data processing pipeline utilizes multiple synchronization beacons and time calibration registrations embedded during collection to align these heterogeneous data sources precisely on a unified timeline. Furthermore, every activity on the GPU (e.g., kernel execution or memory copy) is linked to the CUDA Runtime API or Driver API call that triggered it on the CPU side. This visualizes the entire process from API invocation to driver submission and final GPU execution, as shown in Figure 
4
.
Figure 4
: 
Trace view demonstrating cross-stack semantic alignment. LatencyPrism aligns CUDA Runtime API calls with underlying GPU kernel executions (e.g., 
AddPaddingkernel
) on a unified timeline.
4.1.3 
Distributed Topology Resolution
In large-scale distributed LLM inference, collaborative operations such as AllReduce communication in tensor parallelism or cross-GPU synchronization of KV Cache are typically abstracted in application code via logical identifiers (e.g., NCCL’s 
commHash
). Observable low-level events (e.g., GPU kernel, NVLink traffic, network packets), however, bind to physical resources (e.g., 
node-07/gpu2
). If this mapping is missing, even full-stack traces cannot answer critical questions like “Between which two physical GPUs is this slow AllReduce operation occurring?”
To bridge this gap, LatencyPrism parses 
commHash
, 
rank
, 
node
, and 
hostname
 parameters in NCCL events to dynamically construct a global mapping table of 
(
commHash
,
rank
)
→
(
node
,
device
)
(\texttt{commHash},\texttt{rank})\rightarrow(\texttt{node},\texttt{device})
, thereby precisely associating logical communication relationships with the physical topology.
4.2 
Online Monitoring
4.2.1 
Iteration Cycle Recognition
LatencyPrism automatically delineates inference cycles based on Python call stacks. The system scans high-level Python function calls in the trace data. By analyzing call frequency and duration stability, it automatically identifies anchor functions that best represent a complete inference iteration cycle. Using these anchors as boundaries, the continuous event stream is segmented into independent cycles. In scenarios requiring extremely low overhead or non-Python drivers, we support cycle recognition with lower precision via frequency domain analysis of GPU kernel or User Probe event streams.
To distinguish between Prefill and Decode stages, the system analyzes multiple indicators. It matches predefined key sub-event lists, such as 
forward_prefill
 and 
process_batch_result_decode
, and utilizes hooked parameter information like 
forward_mode
. Furthermore, it
