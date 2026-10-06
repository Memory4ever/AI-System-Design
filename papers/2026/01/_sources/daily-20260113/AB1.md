# 精确v1题摘与日期首批

实际2026-10-03恢复；以下为原web返回题摘/版本段字段投影，未省略返回中的摘要正文；失败项不记已读。独立准入尚待核。

[2601.05505v1] FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse (https://arxiv.org/abs/2601.05505v1)
citeturn26819view0 [wordlim: 200] Crawled: 3 weeks ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.05505v1","lineno":null}); Total lines: 160
L8: [Submitted on 9 Jan 2026 (this version), latest version 13 Apr 2026 (cite5†v2 )]
L9: # Title:FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse
L10: 
L11: Authors:cite6†Yubo Hou , cite7†Zhisheng Chen , cite8†Tao Wan , cite9†Zengchang Qin L12: 
L13: View a PDF of the paper titled FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse, by Yubo Hou and 3 other authors
L14: 
L15: cite10†View PDF cite11†HTML (experimental) L16: > Abstract:The stateless architecture of Large Language Models inherently lacks the mechanism to preserve dynamic context, compelling agents to redundantly reprocess history to maintain long-horizon autonomy. While latent memory offers a solution, current approaches are hindered by architectural segregation, relying on auxiliary encoders that decouple memory from the reasoning backbone.
L17: We propose FlashMem, a framework that distills intrinsic memory directly from transient reasoning states via computation reuse. Leveraging the property that internal representations uniquely encode input trajectories, FlashMem identifies the last hidden state as a sufficient statistic for the interaction history. This enables a Shared-KV Consolidator to synthesize memory by attending directly to the backbone's frozen cache, eliminating redundant re-parameterization.
L18: Furthermore, a parameter-free Cognitive Monitor leverages attention entropy to adaptively trigger consolidation only when high epistemic uncertainty is detected. Experiments demonstrate that FlashMem matches the performance of heavy baselines while reducing inference latency by 5 times, effectively bridging the gap between efficiency and persistent cognition.
L19: Subjects:  | Computation and Language (cs.CL)
L20: Cite as:  | cite12†arXiv:2601.05505 [cs.CL]
L21:    | (or cite13†arXiv:2601.05505v1 [cs.CL] for this version)
L22:    | cite14†https://doi.org/10.48550/arXiv.2601.05505†doi.org arXiv-issued DOI via DataCite
L23: ## Submission history
L24: 
L25: From: Yubo Hou [cite15†view email ]
L26: [v1] Fri, 9 Jan 2026 03:27:43 UTC (1,204 KB)
L27: cite5†[v2] Mon, 13 Apr 2026 08:16:25 UTC (1,199 KB)
L28: 
L29: Full-text links:
citeturn26819view1 [wordlim: 200] Source: open({"ref_id":"https://arxiv.org/abs/2601.05524v1","lineno":null}); Total lines: 1
L0: Failed to fetch https://arxiv.org/abs/2601.05524v1: Cache miss
[2601.06007v1] Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks (https://arxiv.org/abs/2601.06007v1)
citeturn26819view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.06007v1","lineno":null}); Total lines: 160
L8: [Submitted on 9 Jan 2026 (this version), latest version 31 Jan 2026 (cite5†v2 )]
L9: # Title:Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks
L10: 
L11: Authors:cite6†Elias Lumer , cite7†Faheem Nizar , cite8†Akshaya Jangiti , cite9†Kevin Frank , cite10†Anmol Gulati , cite11†Mandar Phadate , cite12†Vamse Kumar Subbiah L12: 
L13: View a PDF of the paper titled Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks, by Elias Lumer and Faheem Nizar and Akshaya Jangiti and Kevin Frank and Anmol Gulati and Mandar Phadate and Vamse Kumar Subbiah
L14: cite13†View PDF cite14†HTML (experimental) L15: > Abstract:Recent advancements in Large Language Model (LLM) agents have enabled complex multi-turn agentic tasks requiring extensive tool calling, where conversations can span dozens of API calls with increasingly large context windows. However, although major LLM providers offer prompt caching to reduce cost and latency, its benefits for agentic workloads remain underexplored in the research literature.
L16: To our knowledge, no prior work quantifies these cost savings or compares caching strategies for multi-turn agentic tasks. We present a comprehensive evaluation of prompt caching across three major LLM providers (OpenAI, Anthropic, and Google) and compare three caching strategies, including full context caching, system prompt only caching, and caching that excludes dynamic tool results.
L17: We evaluate on DeepResearchBench, a multi-turn agentic benchmark where agents autonomously execute real-world web search tool calls to answer complex research questions, measuring both API cost and time to first token (TTFT) across over 500 agent sessions with 10,000-token system prompts. Our results demonstrate that prompt caching reduces API costs by 45-80% and improves time to first token by 13-31% across providers.
L18: We find that strategic prompt cache block control, such as placing dynamic content at the end of the system prompt, avoiding dynamic traditional function calling, and excluding dynamic tool results, provides more consistent benefits than naive full-context caching, which can paradoxically increase latency. Our analysis reveals nuanced variations in caching behavior across providers, and we provide practical guidance for implementing prompt caching in production agentic systems.
L19: Comments:  | 15 pages, 8 figures
L20: Subjects:  | Computation and Language (cs.CL)
L21: Cite as:  | cite15†arXiv:2601.06007 [cs.CL]
L22:    | (or cite16†arXiv:2601.06007v1 [cs.CL] for this version)
L23:    | cite17†https://doi.org/10.48550/arXiv.2601.06007†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Elias Lumer [cite18†view email ]
L27: [v1] Fri, 9 Jan 2026 18:41:57 UTC (658 KB)
L28: cite5†[v2] Sat, 31 Jan 2026 20:15:29 UTC (1,092 KB)
L29: 
[2601.05833v1] Peek2: A Regex-free implementation of pretokenizers for Byte-level BPE (https://arxiv.org/abs/2601.05833v1)
citeturn26819view3 [wordlim: 200] Crawled: 3 weeks ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.05833v1","lineno":null}); Total lines: 161
L8: [Submitted on 9 Jan 2026 (this version), latest version 30 Apr 2026 (cite5†v2 )]
L9: # Title:Peek2: A Regex-free implementation of pretokenizers for Byte-level BPE
L10: 
L11: Authors:cite6†Liu Zai L12: 
L13: View a PDF of the paper titled Peek2: A Regex-free implementation of pretokenizers for Byte-level BPE, by Liu Zai
L14: 
L15: cite7†View PDF cite8†HTML (experimental) L16: > Abstract:Pretokenization is a crucial, sequential pass in Byte-level BPE tokenizers. Our proposed new implementation, Peek2, serves as a drop-in replacement for cl100k-like pretokenizers used in GPT-3, LLaMa-3, and Qwen-2.5. Designed with performance and safety in mind, Peek2 is Regex-free and delivers a $ 1.11\times $ improvement in overall throughput across the entire Byte-level BPE encoding process.
L17: This algorithm runs entirely on the CPU, has stable linear complexity $ O(n) $, and provides presegmentation results identical to those of the original Regex-based pretokenizer.
L18: Comments:  | 5 pages, 4 figures, for associated code, see cite9†this https URL†github.com L19: Subjects:  | Computation and Language (cs.CL)
L20: ACM (Association of Computing Machinery Classification) classes:  | D.2.0; F.3.1
L21: Cite as:  | cite10†arXiv:2601.05833 [cs.CL]
L22:    | (or cite11†arXiv:2601.05833v1 [cs.CL] for this version)
L23:    | cite12†https://doi.org/10.48550/arXiv.2601.05833†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Zai Liu [cite13†view email ]
L27: [v1] Fri, 9 Jan 2026 15:05:09 UTC (39 KB)
L28: cite5†[v2] Thu, 30 Apr 2026 19:14:51 UTC (89 KB)
L29: 
