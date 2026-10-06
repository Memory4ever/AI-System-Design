[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: PASTA: A Modular Program Analysis Tool Framework for Accelerators

[3] h6: Abstract

[4] p: The increasing complexity and diversity of hardware accelerators in modern computing systems demand flexible, low-overhead program analysis tools. We present Pasta , a low-overhead and modular P rogram A nalysi S T ool Framework for A ccelerators. Pasta abstracts over low-level profiling APIs and diverse deep learning frameworks, offering users a unified interface to capture and analyze runtime events at multiple levels. Its extensible design enables researchers and practitioners to rapidly prototype custom tools with minimal overhead. We demonstrate the utility of Pasta by developing several analysis tools, including tools for deep learning workload characterization and UVM optimization. Through extensive evaluations on mainstream deep learning workloads tested on NVIDIA and AMD GPUs under both single- and multi-GPU scenarios, we demonstrate Pasta ’s broad applicability. On NVIDIA GPUs, we further show that Pasta provides detailed performance insights with significantly lower overhead (up to 1.3 × \times 10 4 faster) than conventional analysis tools, thanks to its GPU-accelerated backend. Pasta strikes a practical balance between usability, extensibility, and efficiency, making it well-suited for modern accelerator-based computing environments.

[5] h6: Index Terms:

[6] h2: I Introduction

[7] figure: TABLE I: Comparison of Pasta with tools from accelerator vendors and deep learning frameworks. Tool/Fuctionalities NVIDIA Supported 1 AMD Supported 2 DL Framework Supported 3 Low-overhead (GPU-accelerated) Extensibility Open- Sourced Pasta (Ours) ✓ ✓ ✓ ✓ ✓ ✓ NSight Systems [ 1 ] ✓ ✗ ✗ ✗ ✗ ✗ ROCProfiler [ 2 ] ✗ ✓ ✗ ✗ ✗ ✓ PyTorch Profiler [ 3 ] ✗ ✗ ✓ ✗ ✗ ✓ TensorFlow Profiler [ 4 ] ✗ ✗ ✓ ✗ ✗ ✓ Omniperf [ 5 ] ✗ ✓ ✗ ✗ ✗ ✓ 1,2 : Tools can analyze standard NVIDIA CUDA and AMD ROCm programs with low-level vendor library information. 3 : Tools can capture and analyze deep learning framework-specific events, such as tensor allocation and destruction

[8] p: With Moore’s Law nearing its physical limits, the escalating computational needs of emerging big data workloads have ushered in the era of domain-specific computing. Various accelerators, such as GPUs and TPUs, have emerged as essential compute engines with their massive parallelism and specialized compute capabilities. To fully exploit the compute capabilities of these accelerators, understanding workload behavior and identifying performance bottlenecks are crucial. However, the massive parallelism within individual accelerators, combined with their asynchronous interactions with CPUs, complicates the task of performance analysis and hinders the deduction of actionable optimization insights. To address this, accelerator vendors offer performance analysis tools such as NVIDIA Nsight Systems [ 1 ] and AMD ROCm Profiler [ 2 ] , which help developers analyze execution behavior and performance metrics. Despite their usefulness, these vendor-provided tools have notable limitations including limited flexibility and extensibility and inadequate support for emerging workloads . These tools typically focus on predefined general-purpose metrics and often fail to meet the needs of user-specific performance analysis. For example, NVIDIA Nsight Systems provides timeline-based views of CPU and GPU activity, but it lacks the ability to capture fine-grained memory reuse patterns or associate memory activity with high-level model structures in deep learning (DL) workloads. Furthermore, vendor tools primarily capture events from low-level profiling libraries [ 6 , 2 , 7 ] and attribute them to general program context, offering limited visibility into higher-level behaviors specific to modern DL frameworks like PyTorch [ 8 ] and TensorFlow [ 9 ] . For example, these frameworks introduce their own memory allocators and execution models (e.g., kernel grouping by layers), which result in unique runtime patterns and performance characteristics. While DL frameworks integrate their own profilers, such as the PyTorch Profiler [ 3 ] and TensorFlow Profiler [ 4 ] , these profilers only expose high-level model behaviors and lack the capability to trace low-level accelerator performance details and are not easily extensible.

[9] p: To support custom performance analysis, accelerator vendors also expose low-level programming interfaces and libraries [ 10 , 11 , 12 , 13 ] , enabling developers to build performance analysis tools tailored to their specific needs. However, this approach often requires comprehensive knowledge of accelerator architecture, low-level programming models, as well as considerable development effort. In addition, while various community-developed tools exist for accelerator performance analysis, they only target specific inefficiency problems or specialized use cases [ 14 , 15 , 16 , 17 , 18 ] . Their limited extensibility poses challenges for generalization to a broader range of program analysis tasks.

[10] p: Given the increasing demand for performance analysis tools tailored to emerging workloads and the limitations of existing solutions, we present Pasta , a low-overhead modular program analysis tool framework for accelerators. To the best of our knowledge, Pasta is the first framework designed to support cross-vendor accelerators and diverse DL workloads with extensibility. Pasta offers several key advantages over existing solutions. 1) Modularity and extensibility. Pasta can be easily extended to meet user-specific performance analysis needs by allowing developers to create custom analyses with simply overriding functions in the Pasta tool collection template. 2) Cross-vendor support. Pasta abstracts away the differences among vendor-specific profiling interfaces through unified Pasta event handlers, which support monitoring on various accelerator architectures. 3) DL framework integration. Pasta supports DL framework-specific events capturing functionalities (e.g., operator execution and tensor allocation) to provide a more holistic view of workload behavior. 4) Low-overhead design. Pasta is designed with analysis efficiency in mind, aiming to reduce runtime impact and accelerate the processing of performance data. It leverages lightweight hooks provided by vendor profiling interfaces and DL framework callbacks, minimizing instrumentation overhead. Additionally, Pasta includes an event processor that preprocesses raw runtime data and performs preliminary analysis on GPUs, accelerating the processing of large volumes of data generated by massively parallel accelerator executions. Table I compares the key advantages of Pasta with the tools provided by accelerator vendors and DL frameworks.

[11] p: To demonstrate the practical utility of Pasta , we develop several analysis tools as case studies, including a DL workload characterization tool and a Unified Virtual Memory ( UVM ) optimization tool. These tools are implemented with minimal effort thanks to Pasta ’s extensible framework and can be applied to diverse DL models. The case studies reveal actionable insights, such as identifying kernel bottlenecks, quantifying underutilized memory regions, and optimizing UVM prefetching strategies, with significantly lower overhead compared to existing profiling tools, particularly due to Pasta ’s GPU-accelerated analysis design.

[12] p: Our contributions are as follows:

[13] p: To the best of our knowledge, Pasta is the first program analysis framework that supports emerging DL workloads and accelerators from multiple vendors , including both NVIDIA and AMD GPUs .

[14] p: Pasta ’s modular and extensible design allows it to be easily tailored to diverse performance analysis needs, which significantly speeds up the optimization and development processes.

[15] p: We demonstrate the effectiveness of Pasta through case studies on single- and multi-GPU scenarios , which demonstrate substantially reduced analysis time and unique insights with Pasta compared with the existing vendor-specific profiling tools.

[16] p: Pasta is fully open-sourced under the MIT license 1 1 1 Source code available at: https://github.com/AccelProf/AccelProf and includes a detailed user guide for conducting performance analysis with some tools built using Pasta , as well as a developer guide for extending Pasta for their own performance analysis needs 2 2 2 User and developer documentation: https://accelprofdocs.readthedocs.io .

[17] h2: II Background and Related Work

[18] p: This section uses GPUs as an example accelerator, while Pasta can be used for any accelerators that have APIs with which a host CPU can monitor various execution status .

[19] h3: II-A GPU Performance Analysis

[20] p: Due to massive parallelism and asynchronous interactions with a host CPU, GPU-accelerated applications pose challenges for performance analysis. To support analysis, GPU vendors provide various tools such as NVIDIA’s Nsight Systems [ 1 ] and Nsight Compute [ 19 ] , AMD’s ROC Profiler [ 2 ] and Omniperf [ 5 ] , and Intel’s VTune Profiler [ 20 ] . These tools profile low-level activities of architectural components, but those profiling results often lack application semantics and insufficient to provide meaningful insights for optimization, making them difficult to use directly for performance tuning.

[21] p: To address these limitations, several analysis tools have been developed using vendor-provided interfaces. DrGPUM [ 14 ] and Diogenes [ 21 ] pinpoint memory-related inefficiencies, such as inefficient CPU-GPU memory transfers. ValueExpert and GVProf [ 22 , 15 ] identify value-related inefficiencies in GPU-accelerated applications. Nayak et al. proposed a tool that identifies redundant and improper synchronization operations in GPU programs [ 17 ] . GVARP [ 18 ] detects performance variance in large-scale heterogeneous systems and provides insights to locate the root causes. CUDAAdvisor [ 23 ] performs fine-grained GPU kernel analysis, including memory reuse distance and divergence analysis, offering actionable insights for optimization. While these tools enable more comprehensive performance analysis, as each tool is designed for certain inefficiencies of the target GPUs, users should identify the right tools for each target analysis. Some tools, such as HPCToolkit [ 24 ] supports a more general performance analysis on both NVIDIA and AMD GPUs. However, they primarily focus on HPC workloads and do not support emerging workloads such as DL models. Given the diversity of accelerators and workloads, a more extensible solution is needed to support broader analyses.

[22] h3: II-B DL Workload Performance Analysis

[23] p: With the increasing importance of DL models for almost all computing domains, performance optimization of DL workloads is one of the most critical research topics of today. However, most of the DL frameworks are designed to be DL practioner-friendly while hiding backend interactions with accelerators [ 25 , 26 ] . While this abstraction helps DL model designers to focus on the model architecture without concerning systems and hardware-side activities, it complicates execution analysis and optimization using traditional performance tools.

[24] p: To tackle this issue, DL frameworks have introduced their own performance analysis tools, such as PyTorch Profiler [ 3 ] , TensorFlow Profiler [ 4 ] and JAX Profiler [ 27 ] . While these framework-native performance analysis tools are useful, they have several limitations: (1) they lack support for exposing low-level details of accelerators, (2) they often require significant programming effort to configure, and (3) they support limited profiling metrics, which lack flexibility and extensibility for customized analysis.

[25] p: To overcome these limitations, third-party DL performance analysis tools have been introduced. NVIDIA provides DLProf [ 28 ] , which aggregates kernel performance data from tools like Nsight Systems and nvprof and offers layer-wise kernel performance summaries. DeepContext [ 16 ] links call stacks from high-level Python code to underlying accelerator C/C++ libraries, enabling the identification of inefficiencies in DL codebases. RL-Scope [ 29 ] collects cross-stack profiling information (e.g., CUDA API time and GPU kernel time) and provides a detailed breakdown of CPU/GPU execution time. Hotline Profiler [ 30 ] detects runtime bottlenecks in DL workloads and presents them using multi-scale timeline visualizations. Despite these advances, these tools either support only specific target inefficiencies or remain closed-source, thus are difficult to extend for customized analysis across diverse DL workloads.

[26] h2: III Design and Methodology

[27] figure: Fig. 1: Design of Pasta . \Description

[28] h3: III-A Overall Design

[29] p: Figure 1 shows the architecture of Pasta , which consists of three modular components: Pasta Event Handler , Pasta Event Processor , and Pasta Tool Collection . The event handler interfaces directly with low-level, vendor-specific profiling APIs and high-level DL framework callbacks to configure. This layer abstracts away the complexity of diverse accelerator platforms and enables consistent event collection across hardware vendors. Built atop the event handler, the event processor acts as the dispatch and preprocessing layer. It standardizes heterogeneous runtime information through a unified interface and performs preprocessing on either the CPU or GPU. This component transforms raw profiling data into structured insights suitable for higher-level analysis. The tool collection hosts user-defined analysis tools that retrieve runtime data via the standardized interface and perform customized analyses such as kernel profiling or memory characterization. All three components are designed in independent modules so that each can be separately upgraded without modifying the other modules. For instance, supporting a new accelerator only requires updating the event handler, while users can add new tools without changing the handler or processor. This modular, extensible design makes Pasta suitable for diverse accelerators and targeted, low-overhead analysis.

[30] figure: TABLE II: List of Supported Events in Pasta . Low-Level Accelerator Events Coarse-Grained Host-Called API Events All Driver Functions All Runtime Functions Synchronization Kernel Launch Memory Copy Memory Set Resource Operations Batch Memory Operations Fine-Grained Device-Side Operations Thread Block Entry Thread Block Exit Global Memory Access Shared Memory Access Barrier Instruction Device Function Call Device Function Return Device-Side Malloc Device-Side Free Global-To-Shared Copy Pipeline Commit Pipeline Wait Remote Shared Memory Access Cluster Barrier Any Specific Instruction High-Level DL Framework Events Operator Start Operator End Tensor Allocation Tensor Reclamation Layer Boundary* Forward/Backward Boundary* Customized Code Region* * Requires manual insertion of Pasta annotations, as discussed in Section III-F1 .

[31] h3: III-B Pasta Modules

[32] p: Event handler: In Pasta , the event handler module is responsible for initializing and setting up the profiling utilities. It abstracts the complexities of vendor-specific profiling APIs and DL framework callbacks, and provides a comprehensive set of handler functions for both coarse-grained and fine-grained runtime events on accelerators. Coarse-grained events include kernel launches, memory copy operations, and synchronization calls, while fine-grained events capture individual thread-level activities, such as memory accesses by each thread. In addition to low-level, “bare-metal” vendor-specific events, Pasta also monitors high-level DL framework-specific events, such as tensor allocation and operator execution. Table II summarizes the complete set of events currently supported by Pasta . Pasta ’s extensible design allows new events to be supported by adding handler functions in the event handler module.

[33] p: Event processor: The event processor module pre-processes raw data captured by the event handler and dispatches it to the corresponding Pasta tool for customized analysis. It also normalizes event metadata across frameworks and profiling utilities, handling inconsistencies (e.g., negative vs. positive size for memory release) and extracting relevant details, such as grid configurations for kernel launch events or copy directions for memory copy operations, based on event type.

[34] p: To enable low-overhead analysis, the event processor adopts GPU-accelerated analysis by launching helper device functions that employ groups of GPU threads (e.g., warps in NVIDIA GPUs) to concurrently process collected data. When an event is triggered on the GPU (e.g., a memory access), the profiling library records the instruction into a device buffer. A helper device function then processes many of these events concurrently, significantly accelerating performance analysis. Figure 2 compares CPU- and GPU-based analysis models. Specifically, Figure 2a shows the conventional GPU-based trace collection with CPU-side analysis, which is used in vendor-provided tools such as the NVBit MemTrace tool [ 31 ] and the Compute Sanitizer MemoryTracker tool [ 32 ] . Figure 2b demonstrates how Pasta adopts a GPU-resident collect-and-analyze model, effectively avoiding stalls and reducing CPU-GPU communication overhead.

[35] figure: (a) Conventional GPU-based trace collection with CPU-side analysis. The GPU stalls when the trace buffer is full, waiting for the CPU to fetch and flush the data. (b) Pasta ’s GPU-resident collect-and-analyze model. GPU threads perform in-situ analysis, avoiding stalls and reducing CPU-GPU overhead. Fig. 2: Comparison of CPU- and GPU-based analysis models. \Description

[36] p: Tool collection: The collection module provides templates for customized analyses, and the user can retrieve all or a subset of events from the event processor module to conduct customized analyses for their own program analysis needs. For example, they can extract tensor allocation and operator execution events to analyze memory usage or execution behavior in DL workloads, or retrieve kernel launch information to identify the most frequently invoked kernels. We show several use cases in Section V .

[37] h3: III-C Workflow

[38] p: Figure 3 shows the workflow of Pasta . Pasta takes binary executable files of GPU-accelerated applications as input, without requiring access to the source code. This makes Pasta particularly suitable for analyzing closed-source libraries such as CUDNN [ 33 ] and CUBLAS [ 34 ] . During execution, when an event listed in Table II occurs, the corresponding callback function in the Pasta event handler module is invoked (❶ and ❷), which collects meta and runtime information related to these events for subsequent processing. Once data collection is complete, the relevant function in the event processor pre-processes the gathered raw data (❸). CPU preprocess functions handle coarse-grained events (e.g., memory allocations and kernel launches), while GPU preprocess functions manage fine-grained events (e.g., memory accesses). Next, the dispatch unit routes the pre-processed data to a specific Pasta tool defined within the Pasta collection (❹). The selected tool then analyzes the data and generates performance reports about program behavior. Users can specify the desired Pasta tool via a command-line option or an environment variable, allowing flexible tool selection based on specific analysis.

[39] figure: Fig. 3: Workflow of Pasta . \Description

[40] h3: III-D Support for Diverse GPU Platforms

[41] p: To support GPUs from different vendors, Pasta provides a set of uniform, decoupled interfaces within its event handler. These interfaces simplify integration and ensure consistent event collection across platforms. For NVIDIA GPUs, Pasta takes advantage of callbacks from both the NVIDIA Compute Sanitizer APIs [ 10 ] and NVIDIA NVBit [ 11 ] . The NVIDIA Compute Sanitizer APIs offer lightweight and intuitive callbacks that reduce development effort. However, they can only inspect a subset of instructions, such as memory and barrier operations. In contrast, NVIDIA NVBit offers more comprehensive coverage by covering all SASS instructions. This increased flexibility, however, requires substantial development effort and potentially incurs higher runtime overhead. Pasta allows users to have the flexibility to choose either of these libraries independently or use both in conjunction to gain insights into their code execution. For AMD GPUs, Pasta integrates with the ROCprofiler-SDK tool library [ 12 ] . These APIs are analogous to NVIDIA’s Compute Sanitizer callbacks and enable Pasta to capture memory, kernel, and synchronization events on AMD platforms with the same interface. As a result, Pasta offers consistent cross-vendor support for profiling and analysis.

[42] h3: III-E Support for Diverse DL Frameworks

[43] p: In DL frameworks, resources and GPU kernel executions are hierarchically managed, which often makes it challenging to adopt vendor-provided tools to gather insightful feedback [ 35 ] . For example, in PyTorch and TensorFlow, GPU memory is managed via memory pools [ 36 ] . While pooled memories are first allocated via vendor-provided memory APIs (e.g., cudaMalloc or HipMalloc ), subsequent allocations and releases of tensors are managed by memory pools that employ framework-specific memory management algorithms, which are often challenging to track synchronously with hardware events. Furthermore, DL frameworks run one or multiple kernels within a single operator to complete a specific computation, where this operator-to-kernel mapping information is hidden from the users. To solve these challenges, Pasta leverages the callbacks [ 37 ] provided by DL frameworks to integrate high-level framework statistics into the event handler module. Note that Pasta can collect low-level accelerator-related events and high-level DL framework-specific events concurrently, which fills the gap between vendor-provided and DL-framework-provided profiling tools.

[44] h3: III-F Advanced Features

[45] figure: ⬇ 1 + {\color[rgb]{0,0.88,0}\boldsymbol{+}} import pasta 2 # forward function of the model 3 def forward (): 4 ... # other layers 5 + {\color[rgb]{0,0.88,0}\boldsymbol{+}} pasta . start () 6 self . transformer_layer () # targeted region 7 + {\color[rgb]{0,0.88,0}\boldsymbol{+}} pasta . stop () Listing 1: An example of layer-wise analysis support.

[46] h4: III-F 1 Range-Specific Analysis

[47] p: It is common to analyze a specific sub-region of an application rather than the entire application. Pasta supports range-specific analysis to facilitate this need. For standard GPU applications, users can define the environment variables START_GRID_ID and END_GRID_ID to specify the subset of kernel launches to analyze. Additionally, Pasta provides support for Python annotations via the pasta package. Listing 1 shows an example usage of the pasta package. Users can annotate specific code regions they wish to analyze or profile using pasta.start and pasta.end (Lines 5 and 7 ).

[48] p: This feature is particularly useful in DL workloads, where individual layers typically have distinct behavioral characteristics. By leveraging this capability, users can conduct fine-grained analysis at the layer level, distinguish between forward and backward passes, or define any custom analysis range.

[49] p: Although existing DL profiling tools offer similar annotation capabilities, Pasta distinguishes itself through its minimal and non-intrusive API design. Users can annotate regions of interest by simply inserting pasta.start and pasta.end , without needing to configure additional logging infrastructure or modify the execution context, enabling fine-grained performance analysis with minimal disruption to the original codebase.

[50] h4: III-F 2 Inefficiency Location Utilities

[51] p: Identifying the source of performance inefficiencies is essential for effective optimization. Pasta provides cross-level location utilities that help developers pinpoint inefficient code at both high-level Python and low-level C/C++ levels, significantly simplifying the debugging and optimization process. In contrast, many existing analysis tools offer only partial visibility, such as low-level C/C++ backtraces (e.g., NVIDIA Nsight Systems [ 1 ] ) or high-level Python call stacks (e.g., PyTorch Profiler [ 3 ] ), thus failing to deliver a comprehensive cross-level context for diagnosing inefficiencies.

[52] p: Pasta enables selective control through a set of predefined knobs, such as MAX_MEM_REFERENCED_KERNEL and MAX_CALLED_KERNEL , which identify the kernel with the most memory references and the most frequent invocations, respectively. Users can easily extend this mechanism with custom knobs to locate specific inefficiencies while avoiding the high overhead of capturing full context information for all runtime events.

[53] p: Figure 4 presents the call stack of the kernel with the highest memory reference count during BERT inference. This visualization enables users to easily identify the most memory-intensive kernel, at::cuda::blas::gemm_and_bias , facilitating targeted optimization for BERT execution on memory-bound systems.

[54] figure: Fig. 4: Cross-layer call stack of the kernel with highest memory reference count during BERT inference. The trace spans Python-level code, PyTorch modules, and low-level C++/CUDA operations. \Description

[55] figure: Fig. 5: Codebase structure of Pasta . \Description

[56] h3: III-G Generalization to Emerging Accelerators and Workloads

[57] p: Support for Emerging Accelerators and Workloads. Pasta ’s architecture is designed to be adaptable beyond GPU-based accelerators and DL workloads. Pasta can support accelerators if the accelerators provide runtime event instrumentation APIs, such as memory operations, kernel dispatch events, and synchronization points. Once the event APIs are provided, Pasta can be extended by implementing a backend handler that maps device-specific events (e.g., for Google TPUs, systolic-array operations or TPU counters) into Pasta ’s unified event format.

[58] p: Likewise, Pasta can also support workloads beyond DL because Pasta design is application agnostic. As far as the user specifies the region of interest based on his/her semantic knowledge of the target application, Pasta can be used for analyzing any applications, such as graph analytics or HPC applications.

[59] p: Handling Differences in Low-Level Event Semantics. Pasta targets heterogeneous accelerators used as CPU co-processors. Although terminologies may differ, many runtime events share common semantics: kernel launch events record grid size and kernel name, memory allocation events record address and size, and memory copy events specify size and transfer direction. Pasta ’s event handler normalizes such inconsistencies in event formats, naming conventions, and timing metadata. For instance, some runtimes report memory deallocation sizes with opposite signs or as deltas. By abstracting such differences, Pasta unifies semantically equivalent events and exposes a consistent interface to higher-level analyses.

[60] p: Vendor-specific events, such as tensor memory operations in NVIDIA Blackwell GPUs or systolic-array operations in TPUs, are handled by specialized handler functions. These events are ignored on other accelerators, ensuring portability while exposing device-unique features.

[61] h3: III-H Extensibility for Diverse Analyses

[62] p: The modular and unified architecture of Pasta makes it highly extensible for diverse analysis purposes. Developers can rapidly prototype instruction-level, memory-centric, or value-based tools with minimal changes, beyond the specific case studies in Section V .

[63] p: Instruction-level analysis tools. These tools focus on fine-grained behaviors at the instruction granularity, leveraging Pasta ’s support for instruction-level instrumentation via vendor APIs (as shown in Table II ). Branch divergence analysis can be implemented by intercepting device-side control flow instructions and correlating them with active thread masks, helping identify warp inefficiencies in SIMT architectures. Instruction scheduling overhead analysis targets pipeline stalls and issue port contention by analyzing throughput counters and stall reason metrics. By integrating these with operator-level boundaries, developers can pinpoint inefficient scheduling regions.

[64] p: Memory-centric analysis tools. These tools examine how memory is used and accessed during execution, which is critical for understanding performance bottlenecks in memory-bound workloads. Memory barrier stall analysis quantifies synchronization delays that occur at device- or cluster-level barriers. With Pasta ’s support for capturing barrier and synchronization events (as listed in Table II ), users can directly measure stall durations and frequencies. By recording timestamps at barrier entry and exit points, developers can compute precise stall intervals and identify kernels or layers that suffer from excessive synchronization overhead. Additional analyses such as shared memory bank conflicts , register pressure , and underutilized memory regions can be developed by leveraging Pasta ’s memory event handler.

[65] p: Value-based analysis tools. These tools inspect runtime data values or semantics for correctness or anomaly detection. For instance, a numeric overflow sanitizer could instrument arithmetic instructions and track operand ranges to detect overflow or underflow events. Similarly, tools such as redundant value load/store detection and data taint tracking can be implemented on top of Pasta by associating value semantics with traced instruction-level events. These analyses leverage Pasta ’s fine-grained operation monitoring capabilities, such as operand values and memory accesses, to detect inefficiencies or security vulnerabilities during execution.

[66] h2: IV Implementation

[67] p: As shown in Figure 5, the system is organized with five primary components: user code, profiling utilities, the event handler, the event processor, and custom analysis tools.

[68] h3: IV-A DL Supports

[69] p: Pasta integrates with real-world DL applications through both high-level and low-level interfaces. On the high-level side, it supports mainstream DL frameworks such as PyTorch via function hooks and callbacks (e.g., c10::reportMemoryUsage and at::RecordFunction ). At the low level, Pasta instruments accelerator-specific APIs. For example, Pasta intercepts calls to cudaMalloc and cuLaunchKernel on NVIDIA platforms or hipMalloc and hipLaunchKernel on AMD platforms, providing fine-grained visibility into memory allocation and kernel launch events on the target hardware.

[70] h3: IV-B Pasta Modules

[71] p: Figure 5 presents the codebase structure of Pasta . The event handler module receives diverse event information from both DL framework-level callbacks (e.g., c10::reportMemoryUsage ) and low-level runtime instrumentation (e.g., SANITIZER_CBID_LAUNCH_BEGIN ), and translates them through a collection of modular handler functions (e.g., PASTA::tensor_call_handler for tensor allocations and PASTA::kernel_call_handler for kernel launches). The event processor module then preprocesses the raw profiling data collected by the event handler using corresponding processor functions, such as PASTA::tensor_info_process and PASTA::kernel_info_process . To support large volumes of fine-grained data—such as instruction-level access traces— Pasta employs GPU analysis threads via patched APIs (e.g., sanitizerPatchModule ), accelerating preprocessing by offloading tasks to the device through __device__ -annotated functions. In the tool collection module, Pasta extracts relevant data for high-level analysis by overriding functions in customizable tool templates.

[72] h3: IV-C Interface to Target Application

[73] p: To enable seamless integration with target applications, Pasta is built as a shared library and injected at runtime via the LD_PRELOAD mechanism. This allows it to intercept both framework and accelerator runtime calls without modifying application source code. Once loaded, Pasta enables the underlying event capture mechanisms using vendor-specific APIs. For instance, it utilizes sanitizerEnableDomain from Compute Sanitizer, nvbit_at_cuda_event from NVBit, and rocprofiler_configure_callback... from the ROCProfiler SDK to enable and initialize the profiling utilities. Each captured event is handled via a corresponding callback implementation, which forwards the event to the event handler system. Finally, Pasta includes several advanced features to support rich developer introspection and cross-language analysis. The pybind11 library is used to enable user annotations and tool customization via Python, while the CPythonPyFrame API is leveraged to capture Python-level call stacks. For C/C++ sources, Pasta integrates with libbacktrace to extract symbolic stack traces.

[74] h3: IV-D Multi-GPU Support

[75] p: Pasta supports multi-GPU scenarios by associating events with the corresponding GPU using the device index exposed from vendor-provided profiling APIs [ 12 , 10 ] . Profiling multi-GPU computing has several challenges. One of them is the interference from auxiliary processes. To run an application on multiple GPUs, applications typically spawn one process to handle each GPU and use several helper processes [ 38 , 39 ] . For instance, Megatron-LM [ 40 ] employs Just-In-Time (JIT) compilation that launches auxiliary processes during execution; when profiling with LD_PRELOAD , these helpers—despite not creating a CUDA context—are still instrumented, leading to unnecessary initialization messages and potential runtime errors. To address this, Pasta uses CUDA_INJECTION64_PATH so that the profiler is injected only into processes that actually initialize a CUDA context. For multi-node GPU setups, Pasta runs independently on each node, generating profiles per rank or per node.

[76] h2: V Case Studies Using Tools Built with Pasta

[77] p: In this section, we present several tools developed using Pasta , demonstrating how it aids developers in understanding performance issues and program behaviors, as well as guiding optimizations. Although we focus on DNN workloads in this paper, Pasta also supports other workloads, such as GPU-accelerated HPC applications.

[78] h3: V-A Experimental Setup

[79] p: We evaluated the functionality and use cases of Pasta on three CPU-GPU systems, each equipped with one or more discrete GPUs as accelerators . Table III summarizes the hardware specifications and system software versions.

[80] p: We studied six widely used DL models—AlexNet [ 41 ] , ResNet18 [ 42 ] , ResNet34 [ 42 ] , GPT-2 [ 43 ] , BERT [ 44 ] , and Whisper [ 45 ] —as detailed in Table IV . To control the UVM oversubscription factor (as applied in Section V-C ), we limit device memory capacity by allocating a specified amount in advance, following a common approach used in prior work [ 46 , 47 ] .

[81] figure: TABLE III: Hardware and Software Environment. Machine CPU GPU System System Memory GPU Driver GPU Toolkit A Intel(R) Xeon(R) Gold 5320 NVIDIA A100 (80GB) × 2 \times 2 Linux 5.14 128 GB 570.86.10 CUDA 12.1 B AMD Ryzen 7 5800X NVIDIA GeForce RTX 3060 Linux 6.11 32 GB 560.28.03 CUDA 12.1 C Intel(R) Xeon(R) Platinum 8568Y AMD MI300X Linux 6.8 240 GB 6.12.12 ROCm 6.4

[82] figure: TABLE IV: Evaluated DL models. Model Type Layers Architecture Batch Size Abbr. AlexNet CNN 8 Convolutional Full Connected 128 AN ResNet18 CNN 18 Residual Block 32 RN-18 ResNet34 CNN 34 Residual Block 32 RN-34 GPT-2 Transformer 12 Transformer (Decoder) 8 GPT-2 BERT Transformer 12 Transformer (Encoder) 16 BERT Whisper (small) Transformer 12 Transformer (En/De-coder) 16 Whisper

[83] h3: V-B Common Application Behaviors Analysis

[84] p: In this subsection, we present two tools developed with Pasta that illustrate how users can extend Pasta for customized performance analysis. With only a few lines of code, they can analyze kernel invocation distributions and identify optimization candidates , showcasing the extensibility of Pasta . We also compare the profiling overhead of Pasta for different underlying profiling APIs and analysis mechanisms, highlighting Pasta ’s flexible support for multiple profiling backends and its low-overhead design.

[85] figure: Fig. 6: Kernel invocation analysis tool developed via Pasta . \Description

[86] h4: V-B 1 Kernel Invocation Frequency Analysis

[87] p: We first demonstrate a simple implementation of a kernel invocation frequency analysis tool to illustrate how Pasta can be extended for customized program analysis. We then present insights derived from the results of this analysis.

[88] p: Figure 6 shows the data flow of the kernel invocation frequency analysis tool. When a kernel launch event occurs, it triggers a kernel launch callback function provided by the profiling API (e.g., NV::kernel_launch_callback ). This, in turn, invokes the Pasta event handler function PASTA::kernel_call_handler , which collects kernel-related information such as the kernel name and grid configuration. Subsequently, the kernel_info_process function in the event processor module preprocesses and organizes the data gathered by the event handler. These operations are handled entirely by the Pasta framework.

[89] p: To develop a kernel invocation frequency analysis tool, users only need to retrieve this preprocessed data from the event processor and implement a customized analysis in the TOOL::record_kernel_freq function. In this case, users maintain a map to record the number of times each kernel is invoked—an intuitive yet insightful statistic.

[90] p: Figure 7 presents the kernel invocation frequencies observed during inference and training for the models listed in Table IV , as collected by the kernel frequency analysis tool. This analysis reveals several insights useful for optimization. Notably, although thousands of kernels are launched during model execution, only a small subset are invoked heavily—such as at::native::im2col_kernel and ampere_sgemm* . These results suggest that focusing optimization efforts on frequently invoked kernels can yield significant performance gains. Leveraging Pasta ’s cross-layer call stack tracing feature, users can directly trace performance-critical kernels back to their source code, simplifying targeted optimizations, as shown in Figure 4 . In comparison, existing tools that often require users to manually extract and correlate such patterns.

[91] figure: Fig. 7: Kernel invocation frequency distribution across all model inference and training runs: bubble size reflects invocation counts (actual numbers in the legend). \Description

[92] figure: TABLE V: Memory characteristics of diverse DNN models (Sizes in MB unless otherwise noted). Model Kernel Count Memory Footprint Working Set (WS) Minimum WS Average WS Median WS 90th percentile WS Inference AlexNet 1428 1528.13 876.12 1.01 216.25 148.26 406.33 RN-18 1497 1232.13 1024.0 1.00 KB 86.07 64.00l 172.27 RN-34 2657 1261.59 1024.0 1.00 KB 76.61 43.25 164.0 BERT 487 1179.64 212.62 47.50 KB 75.23 37.69 141.75 GPT-2 583 4148.10 1493.85 4.00 KB 59.02 25.08 138.0 Whisper 663 2304.15 627.44 2.25 78.54 20.81 153.81 Avg. 1219 1942.29 876.34 0.55 98.62 56.52 196.03 Train AlexNet 4040 3285.17 1512.09 512 B 188.60 144.62 406.33 RN-18 1542 3165.13 1024.00 512 B 84.58 43.25 172.27 RN-34 2734 4316.86 1024.00 512 B 75.33 43.25 164.00 BERT 554 5679.03 235.47 1.00 KB 77.71 37.97 209.30 GPT-2 2004 7862.10 2240.77 512 B 51.37 24.0 137.66 Whisper 665 2104.80 937.01 2.25 80.42 20.81 153.81 Avg. 2593 4402.02 1162.22 0.38 93.00 52.32 207.23

[93] figure: (a) CPU-based analysis in conventional vendor-provided tools. (b) GPU-based analysis in Pasta . Fig. 8: Memory characterization tool developed via Pasta . \Description

[94] h4: V-B 2 Memory Characteristics Analysis

[95] p: The memory characteristics analysis tool focuses on analyzing the working set size of DL models. We define the working set size of a workload as the maximum memory footprint of any single kernel execution within that workload [ 48 ] . This metric is critical for evaluating whether the memory capacity of a system can accommodate a given workload.

[96] p: However, analyzing the working set size of GPU-accelerated applications presents several challenges. First, existing profiling APIs, such as NVIDIA NVBit and AMD ROCProfiler SDK, only provide event-based metadata, such as kernel names and launch configurations, but not the argument lists or their values. This limitation makes it difficult to determine which memory objects are accessed by a given kernel. Second, even if the argument list is available, it is still possible that some objects passed into the kernel are never accessed, posing a challenge to accurately exclude them from the working set without tracking actual memory accesses.

[97] p: To address these challenges, we developed a working set size analysis tool using Pasta . The core idea is to track which memory objects have been accessed during kernel execution. By associating memory access addresses with their corresponding objects, we can compute the memory footprint of each kernel. The maximum of these footprints across all kernels defines the working set size of the workload.

[98] p: Table V summarizes the memory footprints and working set sizes for inference and training of the models listed in Table IV . The results show: 1) working sets are often much smaller than overall footprints, with average footprints 2.22 × \times and 3.79 × \times larger than working sets in inference and training, respectively; 2) median and 90th percentile working sets are modest, indicating most kernels use limited memory. These findings suggest that a substantial fraction of memory is underutilized even for memory-intensive DL workloads. This insight provides theoretical support for memory optimization strategies such as swapping and data offloading [ 49 , 50 , 51 ] .

[99] figure: Fig. 9: Normalized overhead of diverse analysis models on A100 and RTX 3060. CS-GPU : GPU-side trace collection & analysis using Compute Sanitizer. CS-CPU : trace collection on GPU & analysis on CPU using Compute Sanitizer. NVBIT-CPU : trace collection on GPU & analysis on CPU using NVBit. ∞ \infty for those that did not finish within 7 days. \Description

[100] figure: Fig. 10: Breakdown of Pasta profiling time on A100 and RTX 3060. (See Fig. 9 for the definitions of CS-GPU, CS-CPU, NVBIT-CPU). \Description

[101] h4: V-B 3 Analysis Overhead of Pasta

[102] p: As shown in Figure 8 , we implement the memory characteristics analysis tool described in Section V-B2 in three variants: two conventional CPU-based approaches using Compute Sanitizer MemoryTracker tool [ 32 ] and NVBit MemTrace tool [ 31 ] correspondingly (Figure 8a ), and another variant that uses GPU-accelerated analysis (Figure 8b ). In the CPU-based approaches, when memory instructions are instrumented, the log of accessed addresses is recorded into a buffer. The buffer is copied to the CPU when it becomes full or the kernel terminates, to be summarized for analysis. In contrast, the GPU-accelerated version performs this analysis directly on the device. When a kernel is launched, a map from memory object to access count is transferred to the GPU. During execution, a profiling device function increments access count for each associated memory object upon each access. When the kernel completes, the access count map is copied back to the CPU, where objects with non-zero access counts are identified as part of the kernel’s working set. By summarizing the profiling statistics on the device by exploiting GPU parallelism, this approach significantly accelerates analysis performance.

[103] p: Figure 9 compares the overhead of the GPU-accelerated analysis with the two CPU-based implementations on A100 GPUs and RTX 3060. On average, the results show that on A100, the GPU-accelerated tool in Pasta is 941 × \times and 13006 × \times faster than CPU-based tools using Compute Sanitizer and NVBit, respectively. On RTX 3060, it achieves average speedups of 627 × \times and 7353 × \times . The CPU-based methods incur significant overhead as they rely on a single CPU thread and can introduce significant stalls. We also note that the Compute Sanitizer-based tool performs faster than the NVBit-based tool because it instruments only memory instructions, whereas NVBit must first dump and parse SASS code to identify memory instructions, which introduces additional overhead.

[104] p: We further break down the profiling overhead into four components: workload execution, trace collection, trace transfer, and trace analysis. Figure 10 shows the breakdown of Pasta profiling time on A100 and RTX 3060. In the GPU-accelerated version, trace collection and analysis are fused into a single GPU function, so the reported “collection time” includes both collection and analysis. Although collection time occupies a larger fraction in the GPU-accelerated version compared to CPU-based versions, its absolute time is much shorter, as shown in the overhead comparison in Figure 9 . In contrast, CPU-based versions are dominated by trace analysis time, which could take hours to days since a limited number of (typically single) CPU threads process massive profiling data.

[105] h3: V-C UVM Optimization for DL Workloads

[106] figure: Fig. 11: Execution time of object-level and tensor-level prefetch on RTX 3060 and A100 under no memory oversubscription. \Description

[107] figure: Fig. 12: Execution time of object-level and tensor-level prefetch on RTX 3060 and A100 under a memory oversubscription factor of 3. \Description

[108] figure: Fig. 13: Memory access hotness of BERT inference over time. \Description

[109] h4: V-C 1 Tensor-Aware UVM Prefetcher

[110] p: NVIDIA’s UVM provides a unified memory space shared between the GPU and CPU, simplifying GPU programming and enabling memory oversubscription to effectively expand the usable GPU memory. Due to this advantage, UVM has been increasingly adopted for DL workloads [ 52 , 53 ] , which have ever-growing memory demands [ 54 , 55 , 56 , 57 , 58 ] . However, while UVM offers transparent memory expansion, its page-fault-driven, on-demand data migration mechanism can incur substantial overhead, especially when accessed data resides in CPU memory and must be migrated to the GPU at runtime [ 59 , 53 , 60 ] .

[111] p: To mitigate these overheads, existing UVM optimization approaches aim to proactively prefetch or pre-evict data so that frequently accessed data resides in GPU memory, avoiding costly page fault handling [ 61 , 62 ] . These solutions typically operate at the granularity of memory objects (e.g., regions allocated via cudaMallocManaged ), under the assumption that memory access patterns are consistent within each object. While this assumption holds for many conventional GPU applications, it does not apply to modern DL workloads. Contemporary DL frameworks such as PyTorch and TensorFlow adopt pool-based memory management. Instead of allocating memory per tensor, they request large chunks of memory from the system (using APIs like cudaMalloc or cudaMallocManaged ) and then manage memory internally by subdividing these chunks into smaller regions to serve individual tensor allocations. As a result, a single memory object may contain multiple tensors, each with different lifetimes and access patterns. This discrepancy renders existing object-level UVM prefetching strategies suboptimal for DL workloads [ 53 ] . Without awareness of tensor boundaries and usage patterns, object-level prefetching can result in unnecessary data migrations, memory bloat, and contention, thereby hurting performance.

[112] p: To address this issue, we leverage Pasta ’s cross-layer event capturing capability—capable of tracing both high-level framework-specific operations and low-level accelerator events—to develop a UVM prefetching analysis tool. This tool captures kernel execution events and correlates them with the accessed memory objects and tensors (as described in Section V-B2 ). Based on this analysis, we generate a multi-level prefetching scheme and build an automated UVM prefetcher that executes prefetching at either memory object or tensor granularity, and compares their performance.

[113] p: Figure 11 shows the normalized execution time of object-level and tensor-level prefetching on RTX 3060 and A100 GPUs under non-oversubscribed memory conditions. Both strategies yield improvements over the baseline (no prefetching), with average speedups of 39% and 30% on RTX 3060 and 37% and 26% on A100, respectively. Object-level prefetching achieves slightly higher speedups in this scenario, as it benefits from aggressive data migration when sufficient GPU memory is available.

[114] p: However, under memory oversubscription, aggressive prefetching can be detrimental. Figure 12 presents the normalized execution times under an oversubscription factor of 3 (i.e., the application’s memory footprint is 3× the GPU memory capacity). In this case, object-level prefetching significantly degrades performance, with average slowdowns of 2.35 × \times and 2.91 × \times observed on RTX 3060 and A100, respectively. The root cause is that many tensors within a prefetched object may not actually be accessed during kernel execution, resulting in excessive and unnecessary data migration. This inefficient use of device memory leads to page thrashing and undermines performance. Notably, GPT-2 consistently benefits from object-level prefetching across both hardware platforms. This is attributed to its relatively small working set size compared to its overall memory footprint, as shown in Table V , which results in less memory pressure and minimal page thrashing, even under 3 × \times oversubscription. While tensor-level prefetching outperforms the baseline on the RTX 3060, it performs slightly worse than the baseline on the A100. This highlights the need for more sophisticated prefetching strategies tailored to memory-intensive workloads, particularly when operating under constrained memory conditions.

[115] h4: V-C 2 Time-Series Hotness Analysis

[116] p: The performance of UVM prefetching is determined by the timely delivery of “hot” data into the GPU. To research an efficient UVM prefetching algorithm, we develop a time-series hotness analysis tool using Pasta , which tracks access hotness over time in the unit of 2MB virtual memory blocks. Figure 13 shows the results of BERT inference without oversubscription. The results reveal significant divergence in access patterns across memory blocks. Memory blocks highlighted between each pair of the horizontal blue lines are frequently accessed throughout the entire execution, suggesting they likely store long-lived hot data (e.g., model parameters). These blocks are good candidates for prefetching and can be pinned in device memory using UVM APIs such as cudaMemPrefetchAsync and cudaMemAdvise . In contrast, blocks highlighted with red boxes exhibit bursts of frequent accesses within narrow time windows and lack reusability, indicating they may contain short-lived, transient data (e.g., key-value caches). These blocks are suitable for proactive eviction to make room for other high-priority hot data.

[117] figure: Fig. 14: Memory usage over time in one training iteration of GPT-2 under identical configurations on AMD and NVIDIA GPUs, with the bottom subfigure showing their difference. \Description

[118] figure: (a) Data Parallelism (b) Tensor Parallelism (c) Pipeline Parallelism Fig. 15: Per-GPU memory usage over time in one training iteration of the Megatron GPT-2 345M model with different parallelism strategies. Bottom subfigures plot the memory usage difference between the two GPUs. \Description

[119] h3: V-D Support for Diverse GPU Vendors and Scenarios.

[120] h4: V-D 1 Comparison between AMD and NVIDIA GPUs

[121] p: Pasta can support various GPU platforms. We compare the memory behaviors of NVIDIA and AMD GPUs (details in Table III ) while running one training iteration of a GPT-2 model (Table IV ). Figure 14 shows the memory usage during the iteration. Both backends exhibit the same three-phase pattern—ramp-up, peak, ramp-down—as PyTorch’s caching allocator recycles tensors [ 63 ] . This similarity is expected since HIP memory management closely follows CUDA’s design [ 64 ] . We also observe backend-specific differences. On the NVIDIA GPU, fewer allocation/deallocation events are issued, but peak memory usage is slightly higher than on the AMD GPU. This discrepancy may be influenced by differences in operator decomposition and kernel fusion strategies across CUDA/cuDNN and HIP/MIOpen backends, as prior work has shown that fusion affects both the number of allocations and temporary memory requirements [ 65 , 66 ] .

[122] h4: V-D 2 Multi-GPU Scenario

[123] p: We run Megatron GPT-2 345M [ 67 ] on the Megatron-LM framework [ 40 , 68 ] with two A100 GPUs (Table III ). Figure 15 shows per-GPU memory usage over one training iteration under Data Parallelism (DP), Tensor Parallelism (TP), and Pipeline Parallelism (PP). Compared to the single-GPU case in Section V-D1 , Megatron-LM’s memory behavior is different: tensors are more persistent with longer lifetimes (e.g., for communication). DP and TP exhibit identical memory usage across two GPUs, since DP runs two replicated models and TP evenly divides the model across devices. The peak memory of TP is about half of DP’s, consistent with model sharding. GPUs showed asymmetric statistics under PP because the model is split at the midpoint of the transformer block stack, thus final layers that produce logits run on GPU1, increasing GPU1’s tail execution. These observations match the semantics of DP, TP, and PP, and demonstrate that Pasta can accurately reveal insights from complex workloads.

[124] h2: VI Discussion

[125] h3: VI-A Impact on Workload Execution.

[126] p: Correctness. Pasta passively intercepts runtime events but does not modify program data or execution logic. Thus, the functional correctness of the workload is unaffected, and all program outputs remain identical to uninstrumented execution. Pasta requires a small fraction of GPU memory (e.g., 4MB) to store profiling data. Therefore, Pasta induces minimal to no interference in resource usage.

[127] p: Performance Overhead. Pasta ’s runtime profiling may introduce performance overhead. The magnitude of this overhead is not strictly predictable, since it depends on both the type and volume of events being captured. In general, the more events or instructions are traced, the higher the expected overhead. Pasta ’s GPU-accelerated design significantly mitigates these costs, as described in Section V-B3 .

[128] h3: VI-B Relation to Existing Techniques.

[129] p: Stream Runtime Verification (SRV). SRV is an online verification mechanism that monitors the streams of events while an application is running and checks if the program executes as specified by the user [ 69 , 70 ] . Pasta leverages the runtime monitoring, similar to SRV. However, the goal and the overall mechanism of SRV and Pasta are fundamentally different. SRV focuses on the program execution verification by using formalized specifications and various monitoring algorithms, whereas Pasta ’s ultimate goal is to optimize program execution by providing accelerator-aware profiling APIs, tool templates, and backends that abstract vendor APIs.

[130] p: eBPF-based Tracing. eBPF is widely used in Linux for dynamic tracing at the kernel level [ 71 ] . It provides a programmable interface for collecting events such as system calls and I/O operations, enabling custom analysis tools. Pasta plays a comparable role for accelerators: it captures and normalizes GPU runtime events, offering modular templates for higher-level analysis. While eBPF addresses general-purpose observability, Pasta complements it by focusing on accelerator-specific semantics and GPU workloads.

[131] h2: VII Conclusion

[132] p: In this paper, we present Pasta , a low-overhead, modular program analysis framework for heterogeneous accelerators. By unifying low-level profiling APIs with high-level framework callbacks, Pasta enables rapid development of customized analysis tools. Case studies on kernel invocation tracking, memory working set analysis, and UVM prefetch optimization demonstrate its versatility. Evaluations show that Pasta delivers significantly lower overhead than existing profilers while supporting rich cross-layer analysis, establishing its potential as a foundational tool for accelerator-aware system optimization and performance research.

[133] h2: Acknowledgment

[134] p: This work was supported by NSF grants, CAREER-2341039, CCF-2452081 and NSF-2411134. We thank AMD Cloud for providing computing resources.

[135] h2: Artifact Appendix

[136] h3: VII-A Abstract

[137] p: Our artifact provides Pasta , a modular program analysis framework for accelerators, along with its profiling client AccelProf. The artifact includes source code, build scripts, and detailed instructions to reproduce the main results presented in Figure 7 , Table V , Figure 9 , 10 , 11 , 12 , 13 , 14 , and 15 . The artifact demonstrates the case studies developed with Pasta .

[138] h3: VII-B Artifact check-list (meta-information)

[139] p: Program: AccelProf.

[140] p: Compilation: Makefile.

[141] p: Run-time environment: Linux x86-64 systems.

[142] p: Hardware: NVIDIA GPUs and AMD GPUs.

[143] p: Execution: accelprof-v-t<tool><executable>[args...]

[144] p: Metrics: GPU application metrics demonstrating the functionality of the Pasta framework.

[145] p: Output: Figures presented in the paper.

[146] p: How much disk space required (approximately)?: ≤ \leq 100 GB.

[147] p: How much time is needed to prepare workflow (approximately)?: ≤ \leq 1 hour.

[148] p: How much time is needed to complete experiments (approximately)?: Reproducing Figure 9 and Figure 10 may take several days. Other figures can be reproduced within ≤ \leq 2 hour.

[149] p: Publicly available?: Yes.

[150] p: Code licenses (if publicly available)?: MIT.

[151] p: Archived (provide DOI)?: doi.org/10.5281/zenodo.17547322 .

[152] h3: VII-C Description

[153] h4: VII-C 1 How delivered

[154] p: The artifact associated with this paper is publicly available at Zenodo [ 72 ] .

[155] p: The open-source GitHub repository is publicly available at: https://github.com/AccelProf/AccelProf .

[156] p: User and developer documentation is publicly available at: https://accelprofdocs.readthedocs.io .

[157] h4: VII-C 2 Hardware dependencies

[158] p: Pasta supports both NVIDIA and AMD GPUs with x86-64 CPUs. We have tested it on NVIDIA A100, NVIDIA GeForce RTX 3060, and AMD MI300X GPUs. For best reproducibility, we recommend using the same GPU models and a machine with at least 100 GB of available disk space.

[159] h4: VII-C 3 Software dependencies

[160] p: The artifact was tested on the following software versions (or newer). Older versions may also work but are unverified.

[161] p: NVIDIA CUDA driver: ≥ \geq 560.28.03

[162] p: AMD GPU Driver ≥ \geq 6.12.12

[163] p: CUDA Toolkit: 12.1 and above

[164] p: ROCm 6.4 and above

[165] p: GCC: 9.4 and above

[166] p: Linux Kernel: 5.14 and above

[167] p: PyTorch 2.0 and above

[168] p: NVIDIA NVBIT 1.7.3 and above

[169] h3: VII-D Installation

[170] p: Download the codebase. The Pasta codebase is organized into multiple submodules.

[171] figure: ⬇ 1 git clone -- recursive \ 2 https :// github . com / AccelProf / AccelProf . git 3 cd AccelProf && git checkout cgo26 4 git submodule update -- init -- recursive

[172] p: Check dependencies Pasta requires PyTorch and necessary Python development library installed.

[173] figure: ⬇ 1 bash ./ bin / utils / check_build_env . sh

[174] p: Build Pasta .

[175] figure: ⬇ 1 # 15 minutes 2 make ENABLE_CS =1 ENABLE_NVBIT =1 ENABLE_TORCH =1

[176] p: Set environment variables.

[177] figure: ⬇ 1 export ACCEL_PROF_HOME = $ ( pwd ) 2 export PATH = $ { ACCEL_PROF_HOME }/ bin : $ { PATH }

[178] p: Setup Pasta AE toolkit.

[179] figure: ⬇ 1 bash ./ bin / setup_ae

[180] h3: VII-E Experiment workflow

[181] p: Setup artifact.

[182] figure: ⬇ 1 cd cgo26 - ae 2 bash ./ bin / setup_artifact . sh

[183] p: Reproduce Figure 7 . Figure 7 shows kernel invocation frequency distribution.

[184] figure: ⬇ 1 bash ./ bin / run_figure_7 . sh

[185] p: Reproduce Table V . Table V shows memory characteristics of diverse DNN models.

[186] figure: ⬇ 1 bash ./ bin / run_table_v . sh

[187] p: Reproduce Figure 9 . Figure 9 shows normalized overhead of diverse analysis models on A100 and RTX 3060. This experiment may take several days to complete. Users can set the environment variable ACCEL_PROF_ENV_SAMPLE_RATE to speed up the process.

[188] figure: ⬇ 1 bash ./ bin / run_figure_9 . sh

[189] p: Reproduce Figure 10 . Figure 10 shows the breakdown of Pasta profiling time on A100 and RTX 3060. This experiment may take several days to complete. Users can set the environment variable ACCEL_PROF_ENV_SAMPLE_RATE to speed up the process.

[190] figure: ⬇ 1 # Checkout to specific branch 2 cd $ { ACCEL_PROF_HOME } 3 cd nv - nvbit && git checkout oh - breakdown 4 cd $ { ACCEL_PROF_HOME } 5 cd nv - compute && git checkout oh - breakdown 6 cd $ { ACCEL_PROF_HOME } 7 8 # Re-build the codebase 9 make ENABLE_CS =1 ENABLE_NVBIT =1 ENABLE_TORCH =1 10 11 # Run the experiment 12 # This may take several days to complete 13 bash ./ bin / run_figure_10 . sh

[191] p: Reproduce Figure 11 . Figure 11 shows execution time of object-level and tensor-level prefetch on RTX 3060 and A100 under no memory oversubscription.

[192] figure: ⬇ 1 bash ./ bin / run_figure_11 . sh

[193] p: Reproduce Figure 12 . Figure 12 shows execution time of object-level and tensor-level prefetch on RTX 3060 and A100 under a memory oversubscription.

[194] figure: ⬇ 1 bash ./ bin / run_figure_12 . sh

[195] p: Reproduce Figure 13 . Figure 13 shows memory access hotness of BERT inference over time.

[196] figure: ⬇ 1 bash ./ bin / run_figure_13 . sh

[197] p: Reproduce Figure 14 . Figure 14 shows memory usage over time of GPT-2 training under identical configurations on AMD and NVIDIA GPUs.

[198] p: Reproducing Figure 14 requires collecting data from both AMD and NVIDIA GPU platforms. The generated profiling trace from the AMD server must then be transferred to the NVIDIA server to plot the memory usage comparison.

[199] p: On AMD GPU: A file named out_amd.log will be generated in the results/figure_14/ directory. Please move this file to the corresponding results/figure_14/ directory on the NVIDIA server.

[200] figure: ⬇ 1 # Download codebase 2 git clone -- recursive \ 3 https :// github . com / AccelProf / AccelProf . git 4 cd AccelProf && git checkout cgo26 5 git submodule update -- init -- recursive 6 7 # Compile the codebase 8 make ENABLE_ROCM =1 9 10 # Set environment ariables 11 export ACCEL_PROF_HOME = $ ( pwd ) 12 export PATH = $ { ACCEL_PROF_HOME }/ bin : $ { PATH } 13 14 # Setup AE Toolkit 15 bash bin / setup_ae 16 cd cgo26 - ae 17 bash ./ bin / setup_artifact . sh 18 19 # Run the experiment 20 bash ./ bin / run_figure_14_amd . sh

[201] p: On NVIDIA GPU: After run the experiment for Figure 14 on AMD GPU, please move the out_amd.log to NVIDIA server under results/figure_14/ .

[202] figure: ⬇ 1 # Run the experiment 2 bash ./ bin / run_figure_14_nvidia . sh 3 4 # Plot Figure 14 5 # Ensure out_amd.log is moved. 6 bash ./ bin / plot_figure_14 . sh results / figure_14 /

[203] p: Reproduce Figure 15 . Figure 15 shows per-GPU memory usage over time in GPT-2 345M model training with different parallelism strategies. The reproduction of Figure 15 requires Megatron-LM [ 40 ] to be installed.

[204] figure: ⬇ 1 bash ./ bin / run_figure_15 . sh path_to_megatron

[205] h3: VII-F Evaluation and expected result

[206] p: The reproduced results are located in folder ./results . The outputs for Figure 7 , Table V , Figure 9 , 10 , 11 , 12 , 13 , 14 , and 15 are expected to match the corresponding results in the paper.

[207] h3: VII-G Methodology

[208] p: Submission, reviewing and badging methodology:

[209] p: http://cTuning.org/ae/submission-20190109.html

[210] p: http://cTuning.org/ae/reviewing-20190109.html

[211] p: https://www.acm.org/publications/policies/artifact-review-badging

[212] h2: References

[213] h2: Instructions for reporting errors

[214] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[215] p: Tip: You can select the relevant text first, to include it in your report.

[216] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[217] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
