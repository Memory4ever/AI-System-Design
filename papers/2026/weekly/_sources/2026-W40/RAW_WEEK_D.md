SAIL: Scaling In-Context Imitation Learning (https://sakana.ai/sail/)
citeturn29543view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29535view3","id":0}); Total lines: 20
L0: # cite0†SAIL: Scaling In-Context Imitation Learning L1: 
L2: September 28, 2026
L3: 
L4: Introducing “Scaling In-Context Imitation Learning” (SAIL) to be presented at IROS2026. This work is a collaboration between Sakana AI and the University of Tokyo.
L5: 
L6:   * Blog: cite1†https://pub.sakana.ai/sail†pub.sakana.ai L7:   * Paper: cite2†https://arxiv.org/abs/2603.08269†arxiv.org L8: 
L9: What does a robot need before it can tackle a new task?
L10: Teaching a robot something new usually starts with collecting demonstrations and training a policy. But foundation models have already learned from vast amounts of images, text, and robotics-related data. We wanted to see how much of that knowledge we could draw out for robot control without changing the model itself.
L11: Recent demonstrations suggest that GPT-6 Astra can operate physical robots alongside its general language and vision capabilities. Earlier work has also shown that LLMs/VLMs can generate entire sequences of robot movements from a few demonstrations.
L12: 
L13: However, a foundation model does not necessarily produce a reliable robot trajectory in a single generation. Performance depends on the context provided, and a small error in a movement target can cause the entire task to fail.
L14: We propose SAIL, a method for more reliable VLM-based robot trajectory generation through test-time scaling.
L15: SAIL uses a policy VLM as a robot trajectory generator, conditioned on a few successful demonstrations. It tests the generated trajectory in a simulator and uses an evaluation VLM to review the resulting video and identify where progress stalled. The policy VLM then uses this feedback to revise the trajectory, with Monte Carlo tree search (MCTS) exploring alternatives while refining promising candidates. Only the selected trajectory is sent to the physical robot.
L16: Across six manipulation tasks in simulation, increasing the search budget from one candidate to 45 raised the average rate of finding a successful trajectory from 25% to 73%. We also evaluated SAIL on a physical robot. Our results suggest that robot trajectory generation can benefit from test-time scaling, with additional computation enabling the model to test and refine its proposed actions in simulation.
L17: We think there is more to learn about what existing models can do with this kind of feedback, and how far those improvements carry over to physical robots.
L18: 
L19: © cite3†Sakana AI 株式会社 --------------------------------------------------------------------------------
Prime Inference: Fast, Reliable Serving for Frontier Open Models (https://www.primeintellect.ai/blog/prime-inference)
citeturn29543view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29535view2","id":15}); Total lines: 224
L0: cite0†iframe†www.googletagmanager.com L1: 
L2: cite1†TRAINING01 cite2†INFERENCE02 cite3†COMPUTE03 cite4†RESEARCH04 L3: 
L4: cite5†DOCS†docs.primeintellect.ai cite6†BLOG cite7†CAREERS30 cite8†Book a call L5: 
L6: cite9†Login†app.primeintellect.ai cite10†Start training†app.primeintellect.ai L7: 
L8: # Prime Inference: Fast, Reliable Serving for Frontier Open Models
L9: 
L10: cite11†Prime Intellect Team†x.com L11: 
L12: OCT 2ND, 2026 • cite12†Announcements L13: 
L14: cite13†Image: Prime Inference: Fast, Reliable Serving for Frontier Open Models L15: # Prime Inference: Fast, Reliable Serving for Frontier Open Models
L16: 
L17: Prime's mission is to build frontier open models and the open superintelligence stack for continuously improving agents. We already provide end-to-end post-training infrastructure, from prime-rl and verifiers to sandboxes and RL environments. But the continual learning loop is not complete until a trained model can serve real users, generate new experience, and feed those production traces back into training.
L18: We're excited to release Prime Inference today. It covers both serverless endpoints and reserved capacity and offers resilient serving of frontier open-source models on our GPU infrastructure across multiple datacenters.
L19: 
L20: cite14†Image: Diagram showing serving closing the continual learning loop between training, serving, and experience generation L21: Prime Inference began as the serving platform we needed ourselves. Long before public release, it powered large-scale RL rollouts, synthetic data generation, evaluations, and long-running coding agents, processing nearly a trillion tokens every day just internally. Beyond our own workloads, we've also been serving large-scale customer deployments in production since January. This scale pushed us to optimize for sustained performance, quality, and reliability, rather than benchmark speed alone.
L22: Our first public deployment, GLM-5.3, went live on OpenRouter on September 22. It currently ranks among the fastest GLM-5.3 endpoints on OpenRouter, with a near-zero tool-call error rate and 100% uptime since launch.
L23: 
L24: Prime Inference at a glance
L25:   * Low-latency: Our GLM-5.3 endpoint on OpenRouter is continuously evaluated for quality, with production SLAs, security, and privacy built in from the start.
L26:   * Premium infrastructure across data centers: Prime-hosted models run on NVIDIA Blackwell today, with Vera Rubin coming soon.
L27:   * Uptime: Automatic failover across data centers keeps traffic moving to healthy deployments.
L28:   * OpenAI compatible: Connect your existing tools and SDKs using a Prime endpoint and API key.
L29:   * Scaling: Serverless endpoints for variable demand, with reserved capacity for sustained workloads.
L30:   * Cost: Unified billing and team-level usage tracking across models, making inference spend easier to manage.
L31:   * Robust open-source infrastructure: Our stack combines NVIDIA Dynamo, vLLM, Mooncake, and FlashInfer, developed in close partnership with Inferact and NVIDIA, with improvements contributed upstream.
L32: ## Get started
L33: 
L34: [Button: CLI][Button: cURL]
L35: 
L36:     `# uv tool install prime && prime login
L37:     prime inference chat 'z-ai/glm-5.3' "Write a haiku about KV caches."`
L38: 
L39: Or point any OpenAI SDK at `https://api.pinference.ai/api/v1`. See the cite15†docs†docs.primeintellect.ai for the full API reference.
L40: ## Built for production SLAs
L41: 
L42: Prime Inference separates the public API from the model fleet, so capacity can move, fail, or scale without changing the client endpoint.
L43: 
L44: cite16†Image: Prime Inference production serving architecture separating the public API from the model fleet L45: 
L46: Our shared circuit breakers let every gateway replica react to failures consistently, while lease-based admission control prevents overload and automatically recovers capacity when a process disappears.
L47: Below the software layer, every cluster is continuously monitored, with health checks that reach all the way down to NVLink and InfiniBand. Alerts go to an on-call team staffed 24/7, so GPU failures are caught and repaired quickly instead of slowly degrading service. And because Prime maintains significant overflow capacity, we can reroute traffic and bring up new deployments whenever more capacity is needed.
L48: Together, these safeguards keep the service available. The next sections look inside a production deployment through our work serving GLM-5.3 on GB200 NVL72.
L49: ## How we serve production agent traffic
L50: ### Workload
L51: 
L52: A typical agent turn adds about 6K tokens to a 140K-token prompt, reusing most of the conversation history. Under load, these returning sessions run alongside new requests with long, uncached prompts.
L53: We benchmark this mix with cite17†AgentX†inferencex.semianalysis.com from SemiAnalysis, which replays multi-turn agent sessions. Our benchmark harness also injects cold arrivals with long prompts. We measure end-to-end tokens per second per user for interactivity and output tokens per second per GPU for efficiency.
L54: ### Prefill/decode disaggregation
L55: 
L56: On shared GPUs, processing a long prompt can interrupt token generation for existing sessions. Chunked prefill limits these interruptions, but both workloads still compete for GPU time.
L57: 
L58: We run prefill and decode on separate GPU groups. NVIDIA Dynamo handles routing and orchestration, while vLLM runs the model on each group. Once prefill finishes, the decoder pulls the computed KV through NIXL and adds the request to its batch.
L59: cite18†Image: Chunked prefill on shared GPUs versus separate prefill and decode workers Chunked prefill on shared GPUs versus separate prefill and decode workers.
L60: 
L61: With Dynamo coordinating separate prefill and decode pools, we reduced p90 inter-token latency by nearly 40% in our tests.
L62: ### Caching and routing
L63: 
L64: Dynamo's KV-aware router chooses a prefill worker based on how much of the prompt it already has cached and how much work is queued there. Workers publish cache updates so the router can track where prefixes are available. We also keep sessions on the same decoder between turns to support KV reuse.
L65: 
L66: Mooncake provides a second cache tier in host DRAM. Prefixes offloaded from GPU memory can be retrieved instead of recomputed, allowing us to retain more conversation history.
L67: cite19†Image: KV-aware router balancing cached prefix overlap against queued work with a Mooncake host-DRAM cache tier The router balances cached prefix overlap against queued work. Mooncake holds cached KV outside GPU memory so workers can retrieve it when needed.
L68: 
L69: With this architecture in place, we tuned GLM-5.3 on GB200 NVL72 for three goals at once: interactive speed, model quality, and concurrency.
L70: ## Performance: GLM-5.3 on GB200 NVL72
L71: 
L72: Long-context agentic serving is as much a cache-management problem as a compute problem. Performance therefore depends on retaining that history, scheduling new work promptly, and moving cached state without interrupting ongoing generation.
L73: 
L74: Our interactivity target was 100 end-to-end tokens per second per user. We tune for the number of concurrent sessions we can support at that speed.
L75: We optimized these paths separately: prefill topology and scheduling to reduce time to first token; compressed KV and a fused attention kernel to support low-latency decoding; and a transfer-friendly cache layout to reduce the overhead of moving KV between workers.
L76: 
L77: cite20†Image: Performance pareto frontier for GLM-5.3 on GB200 NVL72 across prefill-decode ratios L78: 
L79: At the 100 tok/s/user bar, a 1:4 P/D ratio serves the most: 66 sessions per prefill group at 101 tok/s/user and 100 output tok/s per GPU.
L80: ## Technical deep dive
L81: 
L82: For readers who want the engineering details, the rest of this post walks through each optimization in depth, followed by our work on reliable tool calls.
L83: 
L84: The sections below cover our work on topology, scheduling, compressed attention, and KV transfer:
L85: 
L86:   1. Choosing the right topology for prefill and decode
L87:   2. Reducing the scheduler bubble on prefill
L88:   3. NVFP4 KV compression on FlashInfer
L89:   4. Faster NIXL transfers on NVLink with the BLHNC layout
L90: ## Prefill: time to first token
L91: 
L92: Time to first token depends on more than processing the prompt. A request may need to retrieve cached history, wait for admission, compute new tokens, and transfer KV to a decoder. We investigated delays across this path, starting with cache capacity and scheduling.
L93: ### Choosing the right topology
L94: We chose DEP8: eight data-parallel attention ranks with expert parallelism across the group. DEP8 distributes requests across eight attention workers while sharing the model's experts across the group. With the MLA cache layout we used, TEP8 replicated each request's KV across all eight ranks, while DEP8 let the ranks cache different requests.
L95: Even after accounting for the extra weight memory this requires, we had roughly five times more usable prefix-cache capacity on the same hardware compared to a topology like TEP8, which was also benchmarked.
L96: The downside of DEP8 is the DP rank synchronization: each DP rank processes different requests but joins the same all-to-all communication at every MoE layer, so even an idle rank may need to run forward passes to keep up with its peers.
L97: 
L98: cite21†Image: Timing breakdown of a DEP8 rank's prefill execution showing forward pass and dummy-work wait time Timing breakdown in a DEP8 rank's prefill execution. Its own forward takes 408 ms, followed by roughly 245 ms of dummy work while the other ranks finish.
L99: The dispatch overhead would further increase as EP goes wider. We found 1 DEP16 took 17.9% longer than two DEP8 groups, with combine and finalization growing the most.
L100: ### Scheduler bubble and the token budget
L101: 
L102: Cache capacity does not eliminate scheduling delays. We found that a request's cached KV could already be available while the request still waited to enter the running batch.
L103: Workers check for completed loads between forward passes. Results then pass through a batch queue and scheduler, where a ready request can miss the current decision and wait another step. Under load, requests already in progress can fill the next prefill batch, delaying admission even when the cached history is ready. This creates a scheduler bubble.
L104: To reduce this bubble, we halved the number of prompt tokens processed in each prefill step, from 8K to 4K per GPU. Shorter steps let waiting requests start sooner. On our configuration, median queue wait fell from 550ms to 110ms, reducing median time to first token by roughly 20%.
L105: cite22†Image: Median queue wait dropping from 550ms to 110ms after halving the prefill token budget Cache retrieval can finish long before a request enters the running batch. On a separate run, halving the prefill budget cut median queue wait from 550 ms to 110 ms.
L106: 
L107: Smaller steps add overhead for long, uncached prompts, but the tradeoff worked for our workload because most turns reused an existing prefix.
L108: ## Decode: NVFP4 KV compression
L109: 
L110: At our target load, TP4 gave us the lowest inter-token latency among the configurations we tested. With the same GPU budget, we could run more decode engines with fewer sessions running on each one.
L111: However, TP topology comes with a KV capacity tradeoff. TP distributes model weights across GPUs, but with the MLA cache layout we used, each rank still holds a full copy of a request's latent KV, so TP therefore stores KV copies, which also increases the amount of data NIXL transfers from prefill to decode. TP4 stores fewer KV copies than TP8, but each GPU also holds a larger share of the model weights. We wanted to keep the TP4 latency advantage while fitting more KV into the memory available per GPU.
L112: DEP avoids this replication by assigning requests to separate attention ranks, giving it more usable KV capacity, but when testing, we found that the synchronization between DP ranks before MoE dispatch increased decode latency.
L113: 
L114: cite23†Image: AgentX decode benchmark at 64 sessions comparing TP and TP8 plus DCP4 configurations AgentX at 64 sessions. TP8 + DCP4 is an isolated decode run.
L115: We also tested decode context parallelism (DCP), which distributes the cached sequence across ranks while retaining tensor parallelism for the model. This reduced KV duplication, but introduced communication to gather queries, merge selected candidates, and combine partial attention outputs. With sparse attention, each query reads at most 2,048 cached tokens, so there wasn't much attention work to split across ranks in the first place.
L116: In our tests, distributing that work across ranks saved too little computation to offset the added communication. We therefore kept TP4 and looked for a way to fit more KV.
L117: ### Making room for low-latency decode
L118: 
L119: We compressed the 512-value MLA latent using NVFP4: four bits per value, with an FP8 scale for each group of 16 values. The 64-value positional component remained FP8. Including scales, each MLA cache row shrank from 576 to 352 bytes.
L120: 
L121: With the indexer and other state unchanged, total cache capacity increased by roughly 50%, from 1.09 million to 1.63 million cached tokens per decoder at the same memory budget.
L122: ### A native NVFP4 sparse-MLA decode kernel
L123: 
L124: Our first implementation unpacked the selected rows into temporary FP8 buffers in GPU memory before calling the existing attention kernel. This gave us the capacity benefit, but every layer paid for conversion and an extra write-and-read through GPU memory.
L125: We built a native sparse-MLA kernel to remove that intermediate buffer. It consumes the positions selected by the sparse indexer, loads the compressed rows, and unpacks them on-chip as attention needs them. NVFP4 is the storage format; the attention computation uses FP16 operands with FP32 accumulation.
L126: 
L127: cite24†Image: Staged versus native NVFP4 decode kernel data path comparison L128: For each query token, a cluster of cooperating thread blocks divides the selected rows. In the GB200 configuration, each cluster spans three to eight SMs. The blocks combine their partial results through distributed shared memory, without a second kernel launch.
L129: 
L130: Inside each SM, separate groups of warps unpack rows, compute attention scores and softmax, and accumulate the output.
L131: cite25†Image: One query token's selected rows split across a four-SM cluster with overlapping unpacking, scoring, and accumulation One query token's selected rows split across a four-SM cluster. Within each SM, unpacking, scoring, and output accumulation overlap. The partial results are merged within the same kernel launch.
L132: 
L133: Three changes were particularly useful:
L134:   * Overlapping stages. A three-slot buffer lets one group unpack rows while the others score and accumulate earlier stages, reducing the time each group spends waiting for data.
L135:   * Adjusting clusters to the batch. Smaller batches can give each token more SMs, while larger batches need smaller clusters to fit within one execution wave. At 20 query tokens per launch, this reduced kernel time from roughly 32 μs to 14.8 μs.
L136:   * Skipping loads for empty slots. Short contexts leave unused entries in the 2,048-position list, represented by -1. Our initial handling mapped these entries to row zero, repeatedly reading data that was not needed. Zero-filling them reduced a 35-token attention launch from about 41 μs to 20.6 μs in engine traces.
L137: At 15 query tokens per launch, the optimized kernel took approximately 12.0 μs on GB200, compared with 17.7 μs for the staged NVFP4 path and 13.7 μs for FP8 attention. These are results for that workload, not a speed advantage over FP8 at every batch size.
L138: 
L139: cite26†Image: Kernel latency across successive NVFP4 decode kernel versions measured with CUDA graphs Successive kernel versions on GB200, measured with CUDA graphs at 15 query tokens per launch, 2,048 selected positions, and 16 heads per rank.
L140: Attention accounted for about 8% of a decode step at 32 concurrent sessions, so the larger practical benefit came from retaining more KV. NVFP4 gave us roughly 50% more KV-cache capacity while maintaining comparable per-user speed with decode prefix caching enabled.
L141: ### NVFP4 KV accuracy
L142: 
L143: We ran a rigorous evaluation suite, with particular emphasis on long-context tasks, to ensure that NVFP4 KV compression does not degrade accuracy.
L144: 
L145: cite27†Image: Accuracy comparison between FP8 and NVFP4 KV cache across long-context evaluation tasks L146: 
L147: We are contributing the native kernel to FlashInfer as an experimental operation.
L148: 
L149: Compression increased decode capacity, but disaggregation introduced another bottleneck: moving KV efficiently from prefill to decode.
L150: ## KV transfer: reducing copy overhead on NVLink
L151: 
L152: We use vLLM's NIXL connector to let each decoder pull KV from the prefill workers over multi-node NVLink. In an early comparison, the NVLink configuration added roughly 292 ms to time to first token relative to InfiniBand. The faster interconnect was not translating into faster serving.
L153: The bottleneck was transfer fragmentation. In the path we profiled, each transfer descriptor became a small device-to-device copy. A single 200K-token request arriving at one TP4 rank triggered 32K copies. Submitting and processing that many small operations limited the transfer before we could make effective use of NVLink's bandwidth.
L154: ### Changing the layout to reduce fragmentation
L155: 
L156: The original layer-major KV layout, LBHNC, stored each layer's cache separately. Transferring a logical block across the model therefore required separate descriptors for its data in different layers.
L157: 
L158: Increasing the block size helped: using 1,024-token blocks reduced the number of transfer descriptors. However, larger blocks still left data fragmented across layers and could reduce KV-cache utilization by wasting more space in partially filled blocks.
L159: We then tested BLHNC, a block-major layout recently introduced by the vLLM community. It places a block's data from multiple layers together in memory, allowing NIXL to transfer those contiguous regions with fewer, larger copy operations. We're grateful to the vLLM community for developing and sharing this layout.
L160: 
L161: cite28†Image: Layer-major LBHNC versus block-major BLHNC KV cache memory layouts Layer-major and block-major KV layouts. The highlighted entries belong to the same logical block.
L162: In a separate TP8 comparison, the layer-major layout (LBHNC) used 1,024-token blocks, while the block-major layout (BLHNC) used 64-token blocks. Despite using 16× smaller blocks, BLHNC reduced the descriptor count from 19,559 to roughly 1,940 — about 10× fewer — and lowered mean transfer time from 146 ms to 78 ms, a reduction of roughly 47%. The BLHNC layout let us use finer-grained KV blocks while also reducing transfer overhead.
L163: ## Reliable tool calls
L164: 
L165: Performance is only part of production agent serving. Agents also need reliable tool calls to read files, run commands, and make edits. If the model calls the wrong tool or produces unusable arguments, the agent must retry or stop.
L166: In our configuration, Dynamo converts the model's generated tool calls into the API response the agent receives. When serving GLM-5.3 at scale, we found several recurring failure patterns. Initially, we found the system could silently discard calls to undeclared tools and return a normal stop, leaving the agent with no action to execute or error to recover from.
L167: Other calls had missing arguments or incorrect types, even when the client explicitly required the model to follow the tool's input format. The model received these definitions, but our GLM serving path wasn't enforcing them during generation.
L168: 
L169: Dynamo already had a mechanism for this, but lacked structural-tag support for GLM's format. We contributed a structural-tag builder to Dynamo to translate tool definitions into rules that restrict the names and arguments the model can generate.
L170: vLLM uses xgrammar to enforce those rules during decoding, masking tokens that would violate the tool-call grammar. We also fixed errors introduced during parsing: literal strings such as `&lt;` were being converted into `<`, altering code or file contents, while some schema references and nullable argument types were interpreted incorrectly.
L171: 
L172: We tested the final API responses for:
L173:   * Argument types, required fields, and enums
L174:   * Schema references, recursion, and nested schemas
L175:   * Schema conformance in streaming and non-streaming responses
L176:   * Tool-choice behavior, including `auto`, `required`, and `none`
L177:   * Rejection of malformed tool requests
L178: 
L179: We maintain our own tool-call test suite covering these cases, validating the final API responses and checking for regressions as we update the serving stack.
L180: With deep collaboration with the NVIDIA team and open source upstream contribution, Dynamo handles tool calls with near zero error rate throughout long-running agent sessions in production.
L181: ## Built on open source, with great partners
L182: 
L183: We're grateful to the open-source communities and partners behind our stack.
L184:   * vLLM and Inferact. Our stack runs on the vLLM inference engine. We thank Inferact for their deep collaboration on performance and production serving, and vLLM contributors around the world for continually advancing the engine.
L185:   * NVIDIA Dynamo. The operating system beneath our LLM inference platform coordinates disaggregated workers, routes requests and KV state, and turns a distributed GPU fleet into one resilient serving system.
L186: ## On the roadmap
L187: 
L188:   * Batch and async inference for large offline jobs at lower prices.
L189:   * Dedicated and 1-click deployments on your own reserved capacity, including your fine-tuned models from Prime training runs.
L190: ## We're hiring
L191: 
L192: Serving frontier models at the top of the leaderboard while also feeding the largest RL runs we can build is one of the most interesting systems problems in AI right now. If you want to work on kernels, disaggregated serving, KV-cache systems or global routing, cite7†come work with us .
L193: 
L194: Authors
L195: 
L196: cite11†Prime Intellect Team†x.com L197: 
L198: Share
L199: 
L200: cite29†Image: X cite30†Image: Telegram cite31†Image: LinkedIn L201: cite32†Prime Sandboxes: MicroVMs for Agentic RL Training at Scale Prime Sandboxes are fully capable Linux virtual machines built for agentic training, with pricing designed for thousands of concurrent instances. cite33†GLM-5.2 RL weight transfer in 4 seconds using NIXL and ModelExpress How prime-rl transfers a 1.6 TB GLM-5.2 policy into DPEP=32 vLLM inference, overlaps online quantization, and reduces end-to-end synchronization from 86.1 seconds to 3.9 seconds. cite34†Uncovering a universal offline sandbox escape We found models circumventing offline evaluation restrictions through inference API remote-fetch capabilities and coordinated fixes across affected frameworks. L202: cite10†Start training†app.primeintellect.ai cite8†Book a call L203: 
L204: Platform
L205: 
L206: cite1†Lab cite3†Compute cite4†Research L207: 
L208: Company
L209: 
L210: cite7†Careers30 cite35†Merch†primeintellect.supply cite8†Contact L211: 
L212: Community
L213: 
L214: cite36†X†x.com cite37†LinkedIn†www.linkedin.com cite38†Discord†discord.gg cite39†Luma†luma.com L215: 
L216: Resources
L217: 
L218: cite5†Docs†docs.primeintellect.ai cite6†Writings cite39†Events†luma.com cite35†Merch†primeintellect.supply cite40†Platform Status†status.primeintellect.ai L219: 
L220: Terms
L221: 
L222: cite41†Terms of Service cite42†Privacy Policy cite43†Security Policy L223: © 2026 Prime Intellect, Inc.
--------------------------------------------------------------------------------
How Extropic Uses Prime Intellect to Train a Thermodynamic ML Research Agent (https://www.primeintellect.ai/case-study/extropic)
citeturn29543view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29535view2","id":16}); Total lines: 126
L0: cite0†iframe†www.googletagmanager.com L1: 
L2: cite1†TRAINING01 cite2†INFERENCE02 cite3†COMPUTE03 cite4†RESEARCH04 L3: 
L4: cite5†DOCS†docs.primeintellect.ai cite6†BLOG cite7†CAREERS30 cite8†Book a call L5: 
L6: cite9†Login†app.primeintellect.ai cite10†Start training†app.primeintellect.ai L7: 
L8: cite11†Image: How Extropic Uses Prime Intellect to Train a Thermodynamic ML Research Agent L9: 
L10: cite12†Case studies /Extropic
L11: # How Extropic Uses Prime Intellect to Train a Thermodynamic ML Research Agent
L12: 
L13: cite13†Extropic†extropic.ai used Prime Intellect’s Open Superintelligence Stack to post-train Qwen3.6-35B-A3B on classic thermodynamic ML experiments, improving held-out reward 2.8x in 100 GRPO steps.
L14: 
L15: Highlighted features
L16: 
L17: cite14†Image Hosted Training
L18: 
L19: cite15†Image RL Environments
L20: 
L21: cite16†Image Prime Sandboxes and Inference
L22: 
L23: Use case
L24: 
L25: Post-training a thermodynamic ML research agent
L26: 
L27: cite8†Book a Call L28: 
L29: 2.8x
L30: 
L31: held-out reward gain
L32: 100 GRPO steps
L33: 
L34: to achieve that improvement
L35: 
L36: ~25 hours
L37: 
L38: training run wall-clock time
L39: ## At a glance
L40: 
L41: cite13†Extropic†extropic.ai post-trained an open model, Qwen3.6-35B-A3B, to reproduce classic thermodynamic machine learning experiments, nearly tripling its reward metric on held-out tasks in about 100 GRPO steps.
L42: 
L43: Using Prime Intellect’s Open Superintelligence Stack, they built a customized RL environment with verifiers and trained and evaluated it with cite17†Hosted Training†docs.primeintellect.ai , cite18†Prime Sandboxes , and cite19†Prime Inference†docs.primeintellect.ai .
L44: “Prime Intellect has been immensely helpful in making our first experiments possible, providing optimized inference and training tools, reproducible code sandboxes, and GPU resources to train and benchmark open-source models. We're starting by teaching agents to reproduce classic thermodynamic machine learning experiments. These are the early innings of Thermo RSI. We look forward to further accelerating the co-evolution of the next generation of hardware and algorithms with these tools.”
L45: 
L46: Gill Verdon
L47: Founder & CEO, Extropic
L48: ## The problem
L49: 
L50: Extropic’s mission is to solve AI’s ever-increasing energy demands by building the thermodynamic computing stack, harnessing randomness in hardware rather than simulating it in software. On the hardware side, its thermodynamic sampling units (TSUs) are all-transistor circuits that leverage natural thermal noise to sample directly from probabilistic models. However, TSUs are built to run a family of models developed in the mid-2000s, so few modern algorithms exist for them.
L51: To develop those algorithms, Extropic is betting on what it calls thermodynamic recursive self-improvement: research agents design and run experiments, developing new algorithms for TSUs, which enable better hardware and more capable agents. Their first step, described in cite20†Recursive intelligence for a new substrate†recursive-intelligence.vercel.app , is teaching an agent to reproduce classic connectionist experiments in the form of coding tasks.
L52: This meant running agentic RL on a 35B model, with untrusted model-written code executed on every rollout and a judge model scoring every attempt. It also required GPU clusters, RL training code, and sandboxing to all work together on day 1. For a small team, building out such extensive infrastructure from scratch would have been time-consuming and painful.
L53: 
L54: “For a team our size, this is the difference between doing the research and spinning our wheels on infrastructure.”
L55: 
L56: Gill Verdon
L57: Founder & CEO, Extropic
L58: ## Using Prime Intellect’s Open Superintelligence Stack
L59: 
L60: Extropic used Prime Intellect’s Open Superintelligence Stack to train and evaluate its research agent, combining cite17†Hosted Training†docs.primeintellect.ai , cite21†verifiers†docs.primeintellect.ai , cite18†Prime Sandboxes , and cite22†Prime Inference†docs.primeintellect.ai .
L61: 
L62: cite23†Image: Extropic’s training workflow with Prime Intellect L63: 
L64: Prime Intellect’s Open Superintelligence Stack. Components used by Extropic are highlighted in yellow.
L65: This allowed them to nearly triple Qwen3.6’s baseline performance on held-out tasks in 100 steps with a wall clock of ~25 hours, all without Extropic managing the large scale multi-node GPU infrastructure required for this RL training run.
L66: ### Designing the environment
L67: 
--------------------------------------------------------------------------------
World Labs is Joining AMD | World Labs (https://www.worldlabs.ai/blog/amd-announcement)
citeturn29543view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29539view0","id":10}); Total lines: 36
--------------------------------------------------------------------------------
Mistral Opens Munich Hub to Advance Industrial AI in Germany (https://mistral.ai/news/hallo-deutschland/)
citeturn29543view4 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29533view0","id":12}); Total lines: 165
--------------------------------------------------------------------------------
Implementing and Evaluating a Basic Per-Action Monitor for Safer Evals - METR (https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/)
citeturn29543view5 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29539view6","id":91}); Total lines: 646
--------------------------------------------------------------------------------
Chris Painter's testimony to the U.S. Senate on AI agent incidents - METR (https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/)
citeturn29543view6 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29539view6","id":90}); Total lines: 255
--------------------------------------------------------------------------------
Publications · Mind Lab (https://www.mindlab.im/publications)
citeturn29543view7 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29539view5","id":0}); Total lines: 14
--------------------------------------------------------------------------------
Updates · Mind Lab (https://www.mindlab.im/updates)
citeturn29543view8 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29539view5","id":1}); Total lines: 31

