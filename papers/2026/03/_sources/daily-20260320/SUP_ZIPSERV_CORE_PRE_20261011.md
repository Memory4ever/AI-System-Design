# ZipServ17435：旧artifact与本窗完整paper事件分离/PRE

本20补03-19自然日，resume_mar17准备，root完整AB/旧README→paper具体增量校准通过，但未授本Source/PRE或Books。2+2+2=6仅对本次完整paper的共存/成立边界，不重复旧artifact的TCA-TBE/fusedregister或相同宣传数。

## 日期/先公开依据

官方exactv1abs/currentComments/history已实际核，ASPLOS accepted不是firstpublic。SUP_FIRST_DATE_FIELDS exactDOI created/registered03/19T02:32:11Z与官方ID不预发及最早公告夹在03/19BJT，不用Submitted替公开；只授arXiv完整paper本日可取事件的日级推断，不造08确时。特定同稿先公开信号已定点：ACM10.1145/3779212.3790250官方Crossref publisher publishedonline/print03/22，created03/10不授body；作者weiwa同八作者PDF封面/题摘一致，搜索Published8months不授日期。官方repo HPMLL/ZipServ_ASPLOS26 created12/19，README唯一本commit6f8a209bfe46b0905f90d61b0796e352147ff041 (2025-12-19T09:15:22Z)全文实际读，Paper To appear/contact authors，无已公开全文link，已有TCA-TBE/ZipGEMM和AB数字。旧artifact为另一公开事件，不把26年paper叫首次发明；若新证据指同完整稿更早公开，定点重开日期，不追无关历史。

## 必要exact-v1及支持/反側停止

[exact-v1 HTML](https://arxiv.org/html/2603.17435v1)，必要§3.2–4.2/Alg1、§4.4、§5/6.1–6.5/§7。§4.3只读所需register/layout及流水附近，不授所有kernel指令正确性；A仅Gaussian/normal-BF16假设开头，不采用‘intrinsic所有LLM’定理，不全proof/代码/图数拟合。

旧Huffman/ANS等先解压再GEMM合理因为标准算子可消费denseBF16，代价是global中间物化与读写。TCA-TBE为连续top7exponent/3bit位图，8x8tile、sign/mantissa与fullBF16fallback；fullrare值保留，存储lossless不能自行推目标GEMM/reduction逐bit同结果。旧artifact已公开此编码/融合，因此仅为解释新共存接口引用，不算新分数。§4.1 L157–158/§4.4 L295–297本次明确：compute-bound大N Prefill仍decompress至global再高吞吐GEMM；memory-bound小N Decode才fused ZipGEMM直接register消费；两路共享同format与perthreadlogic，避免阶段runtime格式转码。§6.4指出N=8192/16384解压不是零费，offline8B compression16cores约2.5min不能从全费消失。独立核关键条件的目的不是全sourceoriginal重跑。

§6硬件4RTX4090+Xeon8352V/512GB，4L40S+6230R/512GB，kernel另RTX5090(12.8)、A100/H800反側，GCC11.3/NVCC12.4，kernel100warmup/1000timed，e2e每config10次。Kernel cuBLASTC12.4.5 BF16、DietGPU、nvCOMP自定义BF16(exponentstream)，DFloat11压缩code不可得作者用Transformerblock decompression线性外推不同shape，不直接归一为全实现相同预算。Kernelbatch8/16/32，§6.1 L315小Oproj形状反退.79x；§7训练GPU高HBM环境不总胜cuBLAS，§7 FP8 Marlin更快，lossless不通用支配lossy。e2e Llama3.1-8B一4090、Mistral24B两L40S、Llama70B四L40S/TP，batch8/32/output128–2048，request总latency/outputTPS不是productionarrival/tailSLO。Inputlength、vLLM/Transformers具体版本、总power/offlineallcost未在该setup披露，不补造。Weights与KVcapacity收益耦合，不能从更大KV预算回推纯kernel归因或Prefill峰内存必降。§6.5 weightfootprint两处8B10.83/11.18GB数不同未给同条件解释，不采精确memoryrecipe。只采机制与明确形状/阶段/硬件反側，不采用headline和完整性能等价保证。KV compression/跨AMD/AMX/训练通信仍futuredirection，不当已实现。

## actualsoleowner与PRE

ROADMAP INFER-TENSORRT-LLM/Ch49 `books/part-05-inference-system/49-tensorrt-llm.md` actual L1–73 executionplan与中间物化成本；L109–117已有低精度dequant融合/数值误差，L137–146 codebook/precision/context与阶段共编；L918–945量化approxgrid近文均读。现有观点要求压缩可执行/隐藏成本，未区分lossless artifact共一format的Prefill global解压与Decode register解压共存。非泛主题NC；Ch48 L1–20是speculative分布owner，Ch50 L1–23 engine协调owner；Ch54 budget不用再推codec。拟L926量化大标题前插以下两段，实际写前要重新顺读邻接，未授写。

权重存储也可以在不改原 BF16 编码值的条件下压缩，而不先把值投影到低比特网格。常规熵编码加独立解压在可复用标准 dense kernel、容量优先时清楚可靠；若 Decode 被权重带宽限制，先在 global memory 完整展开再读入 GEMM，便可能付出额外中间读写。规则 tile/固定长度编码与 fused 解压可以将权重恢复到 Tensor Core registers 后立即消费，但这种融合不应覆盖所有阶段：大矩阵、compute-bound 的 Prefill 仍可先解压至 global memory 再执行高效 GEMM，低 token 数、memory-bound 的 Decode 才走 fused 路径。两路共用同一压缩格式，可以避免阶段转换时再改写 artifact。<!-- source-family:SF-2026-ARXIV-2603-17435 -->

这一分支用整数解码、layout、寄存器/片上缓冲及离线 packing 换取少读 weights；lossless 存储不等于所有 GEMM schedule 的逐 bit 输出等价，也不等于 Prefill 无解压峰值或运行零费用。[ZipServ exact-v1 §4.1/4.4/6–7](https://arxiv.org/html/2603.17435v1)公开了该阶段共存边界，早先 artifact 已有其编码与 fused kernel，本文不将这些重复称为首次贡献。作者小 shape 和高 HBM 带宽 GPU 的反退说明 ALU 与内存收益必须在实际 shape/hardware 上重测；固定 batch 的输出吞吐不授生产 TTFT/TPOT 或完整成本保证。解码不能隐藏、支持不足或阶段峰值不可行时，应保留独立解压、原 BF16 kernel 或经质量验收的量化路径；第54章继续结算 weights、临时缓冲与 KV 的共同容量，不由压缩比批准请求准入。<!-- source-family:SF-2026-ARXIV-2603-17435 -->

静态源注拟：`SF-2026-ARXIV-2603-17435`，ZipServ exact-v1 §4.1/4.4/6–7，采用统一lossless artifact的Prefill global解压/GEMM与Decode fusedregister两路共存边界。2025-12-19官方artifact先公开编码/fused路线，不重复授首次；仅arxiv完整paper事件新增成立条件。小shape/高HBM反側、bitexact存储vs运算及峰容量/全费边界保留；未核repo代码或复现。
