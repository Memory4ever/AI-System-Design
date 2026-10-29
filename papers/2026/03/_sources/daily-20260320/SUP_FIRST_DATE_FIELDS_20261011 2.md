# 首三旧隔离项的本次真实日级字段

2026-10-11实际 GET exact DOI，HTTP200。日期权限只用created/registered上界与官方ID不预发/公告流程夹证，不把Submitted或Updated独立当公开时间；MFS metadata当前title/AB属v2，原exact-v1题摘已从官方abs另读，未混采。ZipServ另查ASPLOS同稿firstpublic。

```json
[
  {
    "id": "17435",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.17435",
    "status": 200,
    "title": [
      {
        "title": "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression"
      }
    ],
    "created": "2026-03-19T02:32:11.000Z",
    "registered": "2026-03-19T02:32:11.000Z",
    "dates": [
      {
        "date": "2026-03-18T07:21:21Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-19T00:52:35Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ],
    "descriptions": [
      {
        "description": "Lossless model compression holds tremendous promise for alleviating the memory and bandwidth bottlenecks in bit-exact Large Language Model (LLM) serving. However, existing approaches often result in substantial inference slowdowns due to fundamental design mismatches with GPU architectures: at the kernel level, variable-length bitstreams produced by traditional entropy codecs break SIMT parallelism; at the system level, decoupled pipelines lead to redundant memory traffic. We present ZipServ, a lossless compression framework co-designed for efficient LLM inference. ZipServ introduces Tensor-Core-Aware Triple Bitmap Encoding (TCA-TBE), a novel fixed-length format that enables constant-time, parallel decoding, together with a fused decompression-GEMM (ZipGEMM) kernel that decompresses weights on-the-fly directly into Tensor Core registers. This \"load-compressed, compute-decompressed\" design eliminates intermediate buffers and maximizes compute intensity. Experiments show that ZipServ reduces the model size by up to 30%, achieves up to 2.21x kernel-level speedup over NVIDIA's cuBLAS, and expedites end-to-end inference by an average of 1.22x over vLLM. ZipServ is the first lossless compression system that provides both storage savings and substantial acceleration for LLM inference on GPUs.",
        "descriptionType": "Abstract"
      },
      {
        "description": "ASPLOS'26 Accepted Paper",
        "descriptionType": "Other"
      }
    ],
    "relatedIdentifiers": []
  },
  {
    "id": "17456",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.17456",
    "status": 200,
    "title": [
      {
        "title": "Stage-Aware Communication Scheduling for Disaggregated LLM Serving"
      }
    ],
    "created": "2026-03-19T02:32:41.000Z",
    "registered": "2026-03-19T02:32:42.000Z",
    "dates": [
      {
        "date": "2026-03-18T07:53:28Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-19T00:54:14Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-09-19T09:36:31Z",
        "dateType": "Submitted",
        "dateInformation": "v2"
      },
      {
        "date": "2026-09-22T00:36:18Z",
        "dateType": "Updated",
        "dateInformation": "v2"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      }
    ],
    "descriptions": [
      {
        "description": "Meeting stringent Time-To-First-Token (TTFT) requirements is crucial for LLM applications. To improve efficiency, modern LLM serving systems adopt disaggregated architectures with diverse parallelisms, introducing complex multi-stage workflows involving reusable KV-block retrieval, collective communication, and P2D transfer. Flows from dependent stages overlap within and across requests on shared bottleneck links, making TTFT highly susceptible to network contention and necessitating stage-aware scheduling. Unfortunately, most existing works schedule flows in a stage-agnostic manner, leading to uncoordinated contention that constitutes a primary cause of SLO violations.\n In this paper, we present Nuska, a holistic multi-stage flow scheduling mechanism designed to maximize TTFT SLO attainment. At its core, Nuska approximates the Least-Laxity-First (LLF) scheduling policy without requiring precise knowledge of a request's remaining slack. It achieves this through a Defer-and-Promote principle implemented through a Reverse Multi-Level Queue (RMLQ) structure. By dynamically promoting task precedence as effective laxity diminishes, Nuska prioritizes flows with less laxity while preventing requests with loose SLOs from prematurely consuming network bandwidth. We implement Nuska as a pluggable module integrated into vLLM, and evaluate it on an 8-server, 32-GPU testbed as well as through large-scale simulations. Our results demonstrate that Nuska effectively outperforms state-of-the-art baselines, improving the TTFT SLO attainment by 1.2x-2.4x.",
        "descriptionType": "Abstract"
      },
      {
        "description": "18 pages, 14 figures",
        "descriptionType": "Other"
      }
    ],
    "relatedIdentifiers": []
  },
  {
    "id": "17803",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.17803",
    "status": 200,
    "title": [
      {
        "title": "Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs"
      }
    ],
    "created": "2026-03-19T02:40:56.000Z",
    "registered": "2026-03-19T02:40:56.000Z",
    "dates": [
      {
        "date": "2026-03-18T14:59:16Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-19T01:19:19Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ],
    "descriptions": [
      {
        "description": "The key-value (KV) cache has become the dominant contributor to memory consumption in large language model (LLM) inference. Although offloading KVCache from GPU high-bandwidth memory (HBM) to CPU DRAM alleviates device memory pressure, DRAM remains capacity-limited and costly for large, persistent workloads. Solid-state drives (SSDs) provide a cost-effective alternative, but naive SSD-based paging is fundamentally bandwidth-bound due to limited PCIe throughput and per-device bandwidth constraints.\n In this paper, we observe that KVCache activations in real-world workloads exhibit strong and stable correlations. We term this phenomenon KVCache Co-Activation, where accessing a KV entry is often accompanied by a stable and recurring set of other KV entries. Leveraging this property, we present Swarm, an SSD-based KVCache offloading system that converts bandwidth-bound single-device access into parallel I/O across multiple SSDs. Specifically, Swarm clusters co-activated KV entries offline and distributes the resulting clusters across SSDs using graph-based placement with selective replication to maximize parallel I/O bandwidth. At runtime, Swarm performs load-balanced cluster retrieval and dynamically adapts clustering and caching decisions to sustain high bandwidth utilization under evolving access patterns. Evaluations show that Swarm reduces I/O time by 2.41x and improves effective bandwidth utilization by 2.72x.",
        "descriptionType": "Abstract"
      }
    ],
    "relatedIdentifiers": []
  }
]
```
