# 系统首批官方题摘/日期原件

2026-10-25精确DOI API六项；无统一账本要求，仅原始字段与摘要归档。贡献筛选见AUTHOR后到节；多版本current abstract须回exact v1，不混用。

```json
[
  {
    "id": "10.48550/arxiv.2606.06256",
    "relationships": {
      "client": {
        "data": {
          "id": "arxiv.content",
          "type": "clients"
        }
      },
      "provider": {
        "data": {
          "id": "arxiv",
          "type": "providers"
        }
      },
      "media": {
        "data": {
          "id": "10.48550/arxiv.2606.06256",
          "type": "media"
        }
      },
      "references": {
        "data": []
      },
      "citations": {
        "data": []
      },
      "parts": {
        "data": []
      },
      "partOf": {
        "data": []
      },
      "versions": {
        "data": []
      },
      "versionOf": {
        "data": []
      }
    },
    "attributes": {
      "doi": "10.48550/arxiv.2606.06256",
      "publisher": "arXiv",
      "state": "findable",
      "registered": "2026-06-05T02:19:03.000Z",
      "dates": [
        {
          "date": "2026-06-04T14:57:07Z",
          "dateType": "Submitted",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-05T01:04:25Z",
          "dateType": "Updated",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-26T06:47:29Z",
          "dateType": "Submitted",
          "dateInformation": "v2"
        },
        {
          "date": "2026-06-29T00:26:08Z",
          "dateType": "Updated",
          "dateInformation": "v2"
        },
        {
          "date": "2026-07-29T11:03:07Z",
          "dateType": "Submitted",
          "dateInformation": "v3"
        },
        {
          "date": "2026-07-30T00:41:15Z",
          "dateType": "Updated",
          "dateInformation": "v3"
        },
        {
          "date": "2026-09-21T15:06:27Z",
          "dateType": "Submitted",
          "dateInformation": "v4"
        },
        {
          "date": "2026-09-22T02:08:40Z",
          "dateType": "Updated",
          "dateInformation": "v4"
        },
        {
          "date": "2026-06",
          "dateType": "Available",
          "dateInformation": "v1"
        }
      ],
      "titles": [
        {
          "title": "RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention"
        }
      ],
      "descriptions": [
        {
          "description": "As the input length of large language model (LLM) serving continues to grow, the KV cache has become a dominant bottleneck in AI infrastructure. It limits GPU memory capacity, serving concurrency, cache reuse, and distributed scalability. Multiple important problems, including position-independent KV cache, prefix KV cache compression, hot/cold KV cache separation, and distributed KV cache management, all depend on how the KV cache is represented and managed. However, existing serving systems largely rely on a monolithic KV cache abstraction, where the KV cache is treated as a homogeneous sequence of token-level memory blocks and managed with similar policies across attention heads and serving scenarios. We observe that KV cache utility is highly structured across KV heads: different heads exhibit different functional roles, attention distances, and runtime importance. Therefore, a full KV cache is not always necessary for every head, token range, or serving scenario.\n We present RedKnot, a head-aware KV cache management system for LLM serving. RedKnot breaks the conventional monolithic KV cache abstraction by decomposing the KV cache along KV heads, whose importance and effective attention ranges vary significantly across serving scenarios. This head-level decomposition turns the KV cache from a monolithic tensor abstraction into a structured memory object, enabling RedKnot to uniformly support position-independent KV reuse, prefix KV compression, hot/cold KV separation, and distributed KV placement while preserving output fidelity and improving resource efficiency, without requiring model retraining or fine-tuning. RedKnot establishes a new foundation for AI infrastructure by transforming the KV cache from a monolithic, passive runtime artifact into a dynamic, model-aware runtime substrate for scalable LLM serving.",
          "descriptionType": "Abstract"
        }
      ],
      "subjects": [
        {
          "lang": "en",
          "subject": "Artificial Intelligence (cs.AI)",
          "subjectScheme": "arXiv"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        }
      ]
    }
  },
  {
    "id": "10.48550/arxiv.2606.05875",
    "relationships": {
      "client": {
        "data": {
          "id": "arxiv.content",
          "type": "clients"
        }
      },
      "provider": {
        "data": {
          "id": "arxiv",
          "type": "providers"
        }
      },
      "media": {
        "data": {
          "id": "10.48550/arxiv.2606.05875",
          "type": "media"
        }
      },
      "references": {
        "data": []
      },
      "citations": {
        "data": []
      },
      "parts": {
        "data": []
      },
      "partOf": {
        "data": []
      },
      "versions": {
        "data": []
      },
      "versionOf": {
        "data": []
      }
    },
    "attributes": {
      "doi": "10.48550/arxiv.2606.05875",
      "publisher": "arXiv",
      "state": "findable",
      "registered": "2026-06-05T02:10:46.000Z",
      "dates": [
        {
          "date": "2026-06-04T08:47:46Z",
          "dateType": "Submitted",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-05T00:43:21Z",
          "dateType": "Updated",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06",
          "dateType": "Available",
          "dateInformation": "v1"
        },
        {
          "date": "2026",
          "dateType": "Issued"
        }
      ],
      "titles": [
        {
          "title": "QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving"
        }
      ],
      "descriptions": [
        {
          "description": "Retrieval-augmented generation (RAG) improves large language model (LLM) answer quality by grounding generation in external evidence, but processing retrieved contexts makes the prefill stage a dominant serving cost. RAG cache fusion reduces this cost by reusing precomputed key-value (KV) caches for retrieved chunks and selectively recomputing tokens under the current prompt. Existing selectors, however, face a dilemma between quality and efficiency: fast query-agnostic or final-layer query-to-context selectors can miss request-relevant evidence, whereas full-view query-aware selectors require broad context and layer visibility before recomputation and therefore stall the layer-wise cache-fusion pipeline. We present QCFuse, a compressed-view query-aware selector for RAG cache fusion. QCFuse uses chunk-anchor query probing to condition user-query states on compact per-chunk anchors and critical-layer profiling to identify recomputation tokens without all-layer inspection. We implement QCFuse in SGLang and evaluate it on four open-weight LLMs across six datasets. QCFuse reaches full-prefill-level quality. At matched quality, QCFuse achieves an average prefill-time speedup of 1.7x over full prefill and 1.5x over ProphetKV, the strongest quality-preserving baseline.",
          "descriptionType": "Abstract"
        }
      ],
      "subjects": [
        {
          "lang": "en",
          "subject": "Artificial Intelligence (cs.AI)",
          "subjectScheme": "arXiv"
        },
        {
          "lang": "en",
          "subject": "Databases (cs.DB)",
          "subjectScheme": "arXiv"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        }
      ]
    }
  },
  {
    "id": "10.48550/arxiv.2606.06302",
    "relationships": {
      "client": {
        "data": {
          "id": "arxiv.content",
          "type": "clients"
        }
      },
      "provider": {
        "data": {
          "id": "arxiv",
          "type": "providers"
        }
      },
      "media": {
        "data": {
          "id": "10.48550/arxiv.2606.06302",
          "type": "media"
        }
      },
      "references": {
        "data": []
      },
      "citations": {
        "data": []
      },
      "parts": {
        "data": []
      },
      "partOf": {
        "data": []
      },
      "versions": {
        "data": []
      },
      "versionOf": {
        "data": []
      }
    },
    "attributes": {
      "doi": "10.48550/arxiv.2606.06302",
      "publisher": "arXiv",
      "state": "findable",
      "registered": "2026-06-05T02:20:03.000Z",
      "dates": [
        {
          "date": "2026-06-04T15:41:27Z",
          "dateType": "Submitted",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-05T01:06:42Z",
          "dateType": "Updated",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-15T04:51:11Z",
          "dateType": "Submitted",
          "dateInformation": "v2"
        },
        {
          "date": "2026-06-16T01:21:11Z",
          "dateType": "Updated",
          "dateInformation": "v2"
        },
        {
          "date": "2026-06",
          "dateType": "Available",
          "dateInformation": "v1"
        },
        {
          "date": "2026",
          "dateType": "Issued"
        }
      ],
      "titles": [
        {
          "title": "Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving"
        }
      ],
      "descriptions": [
        {
          "description": "Multi-turn LLM serving accumulates dialogue history whose Key-Value (KV) cache grows with every turn and every user, quickly exceeding the model weights themselves and making memory -- not compute -- the binding constraint on throughput. Non-uniform KV compression, which allocates heterogeneous budgets across attention heads, preserves accuracy far better than uniform schemes, yet remains impractical: modern serving stacks assume identical KV lengths across heads, so heterogeneity traps freed memory as page fragmentation, spends up to 25% of prefill time reclaiming scattered pages, and skews GPU workloads that inflate decode latency by up to $1.7\\times$ or burn 15--20% of each decode step on re-planning. We observe that this heterogeneity need not be discovered at runtime: head-wise retention follows a two-level structural regularity -- an input-invariant head ranking with narrowly bounded per-head ratios -- that can be calibrated offline from as few as 50 samples. Building on this insight, we present Tangram, a serving framework that statically resolves what prior systems handle dynamically: Budget Reservation fixes each head's post-compression footprint at scheduling time, eliminating page reclamation; Ragged Paging clusters similar-budget heads into independent page tables, turning fragmentation into reclaimable memory; and Ahead-of-Time Load Balancing precomputes balanced GPU partitions with zero runtime planning. Implemented on vLLM, Tangram serves as a drop-in substrate for existing non-uniform compression methods, matching their accuracy while improving end-to-end throughput by up to $2.6\\times$ over the full-KV baseline. Our implementation is publicly available at https://github.com/aiha-lab/TANGRAM.",
          "descriptionType": "Abstract"
        },
        {
          "description": "13 pages. 15 figures",
          "descriptionType": "Other"
        }
      ],
      "subjects": [
        {
          "lang": "en",
          "subject": "Machine Learning (cs.LG)",
          "subjectScheme": "arXiv"
        },
        {
          "lang": "en",
          "subject": "Software Engineering (cs.SE)",
          "subjectScheme": "arXiv"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        }
      ]
    }
  },
  {
    "id": "10.48550/arxiv.2606.05511",
    "relationships": {
      "client": {
        "data": {
          "id": "arxiv.content",
          "type": "clients"
        }
      },
      "provider": {
        "data": {
          "id": "arxiv",
          "type": "providers"
        }
      },
      "media": {
        "data": {
          "id": "10.48550/arxiv.2606.05511",
          "type": "media"
        }
      },
      "references": {
        "data": []
      },
      "citations": {
        "data": []
      },
      "parts": {
        "data": []
      },
      "partOf": {
        "data": []
      },
      "versions": {
        "data": []
      },
      "versionOf": {
        "data": []
      }
    },
    "attributes": {
      "doi": "10.48550/arxiv.2606.05511",
      "publisher": "arXiv",
      "state": "findable",
      "registered": "2026-06-05T02:02:20.000Z",
      "dates": [
        {
          "date": "2026-06-03T23:33:30Z",
          "dateType": "Submitted",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-05T00:19:02Z",
          "dateType": "Updated",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06",
          "dateType": "Available",
          "dateInformation": "v1"
        },
        {
          "date": "2026",
          "dateType": "Issued"
        }
      ],
      "titles": [
        {
          "title": "RH+: Row-Hit-Optimized Scheduling for PIM-based LLM Inference"
        }
      ],
      "descriptions": [
        {
          "description": "Large language model inference on processing-in-memory (PIM) architectures promises to break the memory wall by performing multiply-accumulate (MAC) operations directly within HBM3 DRAM banks. Prior work identifies the power constraint timing parameter nCCDAB as the primary performance bottleneck and optimizes scheduling accordingly. We demonstrate that for GEMV operations that dominate autoregressive decoding, the DRAM row cycle time (nRC) is 10 to 11 times larger than nCCDAB. Consequently, nCCDAB is entirely masked, rendering prior nCCDAB-focused optimizations ineffective for these workloads. The root cause is inherited host-centric address interleaving, which forces every all-bank MAC command into a different DRAM row. We propose RH+ scheduling, a simple stride change that keeps 32 consecutive MAC operations within the same row. Cycle-accurate simulation across four LLM workloads shows that RH+ delivers 8-12x speedup, over 74% energy reduction, and up to 52x EDP improvement.",
          "descriptionType": "Abstract"
        }
      ],
      "subjects": [
        {
          "lang": "en",
          "subject": "Emerging Technologies (cs.ET)",
          "subjectScheme": "arXiv"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        }
      ]
    }
  },
  {
    "id": "10.48550/arxiv.2606.06453",
    "relationships": {
      "client": {
        "data": {
          "id": "arxiv.content",
          "type": "clients"
        }
      },
      "provider": {
        "data": {
          "id": "arxiv",
          "type": "providers"
        }
      },
      "media": {
        "data": {
          "id": "10.48550/arxiv.2606.06453",
          "type": "media"
        }
      },
      "references": {
        "data": []
      },
      "citations": {
        "data": []
      },
      "parts": {
        "data": []
      },
      "partOf": {
        "data": []
      },
      "versions": {
        "data": []
      },
      "versionOf": {
        "data": []
      }
    },
    "attributes": {
      "doi": "10.48550/arxiv.2606.06453",
      "publisher": "arXiv",
      "state": "findable",
      "registered": "2026-06-05T02:23:25.000Z",
      "dates": [
        {
          "date": "2026-06-04T17:48:17Z",
          "dateType": "Submitted",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-05T01:13:27Z",
          "dateType": "Updated",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06",
          "dateType": "Available",
          "dateInformation": "v1"
        },
        {
          "date": "2026",
          "dateType": "Issued"
        }
      ],
      "titles": [
        {
          "title": "Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents"
        }
      ],
      "descriptions": [
        {
          "description": "Sparse attention is becoming increasingly important for serving large language models (LLMs) as generation lengths continue to grow. However, deploying and evaluating new sparse attention algorithms at scale remains highly engineering-intensive, slowing both human researchers and AI agents in exploring the sparse attention design. To address this challenge, we present Vortex, a system that combines a Python-embedded frontend language atop a page-centric tensor abstraction for expressing a broad range of sparse attention algorithms, with an efficient backend tightly integrated into modern LLM serving stacks. Vortex enables rapid prototyping, deployment, and evaluation of sparse attention algorithms, effectively translating their theoretical efficiency gains into real-world throughput improvements. As a result, Vortex substantially accelerates the design and iteration of sparse attention algorithms. First, AI agents use Vortex to automatically generate and refine diverse algorithms, the best reaching up to $3.46\\times$ higher throughput than full attention while preserving accuracy. Second, Vortex extends sparse attention to emerging architectures and very large models that are otherwise hard to experiment with, reaching up to $4.7\\times$ higher throughput on the MLA-based GLM-4.7-Flash and $1.37\\times$ on the 229B-parameter MiniMax-M2.7 on NVIDIA B200 GPUs.",
          "descriptionType": "Abstract"
        }
      ],
      "subjects": [
        {
          "lang": "en",
          "subject": "Artificial Intelligence (cs.AI)",
          "subjectScheme": "arXiv"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        }
      ]
    }
  },
  {
    "id": "10.48550/arxiv.2606.05951",
    "relationships": {
      "client": {
        "data": {
          "id": "arxiv.content",
          "type": "clients"
        }
      },
      "provider": {
        "data": {
          "id": "arxiv",
          "type": "providers"
        }
      },
      "media": {
        "data": {
          "id": "10.48550/arxiv.2606.05951",
          "type": "media"
        }
      },
      "references": {
        "data": []
      },
      "citations": {
        "data": []
      },
      "parts": {
        "data": []
      },
      "partOf": {
        "data": []
      },
      "versions": {
        "data": []
      },
      "versionOf": {
        "data": []
      }
    },
    "attributes": {
      "doi": "10.48550/arxiv.2606.05951",
      "publisher": "arXiv",
      "state": "findable",
      "registered": "2026-06-05T02:12:25.000Z",
      "dates": [
        {
          "date": "2026-06-04T09:50:16Z",
          "dateType": "Submitted",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06-05T00:47:43Z",
          "dateType": "Updated",
          "dateInformation": "v1"
        },
        {
          "date": "2026-06",
          "dateType": "Available",
          "dateInformation": "v1"
        },
        {
          "date": "2026",
          "dateType": "Issued"
        }
      ],
      "titles": [
        {
          "title": "Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication"
        }
      ],
      "descriptions": [
        {
          "description": "NVSHMEM is NVIDIA's OpenSHMEM-based PGAS communication library for GPU clusters, enabling GPU-initiated, one-sided communication through symmetric memory. Despite its growing adoption, a system-level understanding of its design and behavior remains scattered across documentation, source code, and application experience. This paper presents a concise study of NVSHMEM's programming model, implementation, and performance characteristics, focusing on symmetric memory, one-sided operations, and device-side collectives. We also examine DeepEP as a case study of NVSHMEM in performance-critical sparse deep learning workloads. Our analysis shows that NVSHMEM pioneered a device-side symmetric-memory programming model that enables fine-grained GPU-driven communication and is important for approaching the hardware performance limit. Overall, this work defines NVSHMEM's role as a systems building block, highlights its design tradeoffs, and identifies opportunities for improving GPU communication runtimes.",
          "descriptionType": "Abstract"
        }
      ],
      "subjects": [
        {
          "lang": "en",
          "subject": "Distributed, Parallel, and Cluster Computing (cs.DC)",
          "subjectScheme": "arXiv"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        },
        {
          "subject": "FOS: Computer and information sciences",
          "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
          "subjectScheme": "Fields of Science and Technology (FOS)"
        },
        {
          "lang": "en",
          "subject": "C.2",
          "subjectScheme": "ACM"
        }
      ]
    }
  }
]

```

