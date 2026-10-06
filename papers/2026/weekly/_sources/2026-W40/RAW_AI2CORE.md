Open-sourcing AstaBrief, the fast report-generation model in Asta | Ai2 (https://allenai.org/blog/astabrief)
citeturn29558view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29550view2","lineno":68}); Total lines: 197
L0: cite0†Skip to main content -> L1: 
L2: cite1†Ai2 L3: 
L4:   * Open models
L5: 
L6: ### Open models
L7: 
L8:     * cite2†Olmo L9:     * cite3†Tülu 3 L10:     * cite4†Molmo L11:     * cite5†Playground†playground.allenai.org L12:     * cite6†Language models L13:     * cite7†Multimodal models L14:     * cite8†Evaluation frameworks L15:     * cite9†Open data L16: 
L17: cite10†Image: A computer generated image showing swaths of shapes, meant to depict a hopeful futuristic feeling.†www.datocms-assets.com L18: 
L19:   * Applications
L20: 
L21: cite11†Image†www.datocms-assets.com L22: ### AI for science
L23: 
L24:     * cite12†Asta L25:     * cite13†AstaBench L26:     * cite14†Research with Asta†asta.allen.ai L27:     * cite15†Asta leaderboards L28:     * cite16†Semantic Scholar†www.semanticscholar.org L29:     * cite17†All projects L30: 
L31: ### AI for the planet
L32: 
L33:     * cite18†OlmoEarth L34:     * cite19†EarthRanger L35:     * cite20†Skylight L36:     * cite21†Climate Modeling L37:     * cite22†All projects L38: 
L39: ### AI for robotics
L40: 
L41:     * cite23†Embodied AI L42: 
L43:   * Research
L44: ### Research
L45: 
L46:     * cite24†Latest L47:     * cite25†Papers L48:     * cite26†Research principles L49: 
L50:   * cite27†News L51:   * Institute
L52: 
L53: ### Institute
L54: 
L55:     * cite28†About L56:     * cite29†Careers L57:     * cite30†Media center L58: 
L59: Navigation Menu
L60: # Open-sourcing AstaBrief, the fast report-generation model in Asta
L61: 
L62: October 2, 2026
L63: 
L64: Ai2
L65: 
L66: Share
L67: 
L68: * * *
L69: 
L70: cite31†Model†huggingface.co cite32†Data†huggingface.co L71: Language models can already help researchers search the literature, synthesize evidence, and work through complex questions. But scientific work places particular demands on these models—answers need to stay grounded in evidence, the models need to preserve what the evidence actually supports rather than quietly broadening a study’s conclusions, and researchers need to be able to verify the final outputs.
L72: We see that in how scientists use cite14†Asta†asta.allen.ai , our agentic platform for scientific work. Instead of simple keyword searches, users often bring substantial context and many constraints—for example, asking Asta to compare approaches across a body of literature while accounting for a particular method, population, or setting. Many also return to generated reports later, treating them as working research artifacts rather than one-off answers.
L73: We wanted to help scientists generate cited reports faster, with a model they could download and run themselves. To do that, we tested whether a small, open model trained specifically for scientific report generation could match the report quality of the proprietary models we were using, while reducing generation time and serving costs.
L74: We built cite31†AstaBrief 8B†huggingface.co , a model that turns a research question and retrieved literature excerpts into a cited report. AstaBrief is available in Asta’s Generate a report feature today as cite14†Fast mode†asta.allen.ai alongside Claude-powered Thinking mode, and we’re also open-sourcing it and the training data so others can study, reproduce, and build on our approach.
L75: Developing AstaBrief required tens of thousands of real research queries, citation-focused filtering, preference data, and a redesigned report-generation pipeline that writes the full report in one pass rather than section by section. The result is nearly an order-of-magnitude reduction in report generation time compared to the proprietary models we tracked—across the full Asta pipeline, Fast mode averages 51.1 seconds per report compared with 178.5 seconds for Thinking mode, about 3.5× faster.
L76: Together, those efficiency gains made AstaBrief a useful test case for a broader goal: building open language models that can be adapted to the specific demands of scientific work.
L77: Open weights will also let institutions run AstaBrief on their own infrastructure, which is necessary when research questions reveal sensitive or unpublished work. Alongside the model weights, we’re releasing cite33†an example workflow that researchers can adapt to create reports from their own PDFs†github.com , providing a starting point for local report generation
L78: This post covers how we trained AstaBrief, what we learned about grounding it in scientific evidence, and which parts of our approach we think can carry forward to future models for science. Most of the training and evaluation described was completed in 2025, so the proprietary models used to generate training data and as comparison points reflect the frontier at the time.
L79: We haven’t rerun the full evaluation against today’s frontier models; the results below are best read as evidence about the particular training and system design choices we tested.
L80: ### Training the model
L81: 
L82: Our goal with AstaBrief was to build an open-weights model with all the qualities that matter most for long-form scientific synthesis: answer quality, relevance, structure, and citation grounding. We started from Qwen3-8B and focused most of our effort on the post-training data, evaluation, and surrounding report-generation scaffolding.
L83: Adapting general-purpose models for scientific work – and training new scientific models from scratch – is something we're exploring broadly across Ai2. Through cite34†NSF OMAI , a U.S. national initiative led by Ai2 to build fully open AI infrastructure and models for scientific discovery, our researchers are working directly with scientific communities to understand what they need from future open models and where today's general-purpose models fall short.
L84: That includes studying how needs differ across scientific fields and workflows, with more findings from that research to share in the future.
L85: Recent work, including our cite35†DR Tulu , has shown that reinforcement-learning-based (RL) methods can improve long-form report generation for open-weights models, especially when judge models are involved in the training loop. We considered that path for AstaBrief, but ultimately focused on a simpler recipe built around supervised fine-tuning (SFT) and direct preference optimization (DPO).
L86: RL-based training can be unstable and expensive. We wanted to see how far we could push report generation quality with a cheaper, more operationally manageable setup—one that's also easier to debug and iterate on.
L87: That made the quality of the training data especially important. Rather than relying on a more complex optimization method to compensate for noisy examples, we spent much of the project figuring out how to generate, select, and filter examples that actually demonstrated the report-writing behavior we wanted.
L88: We also wanted AstaBrief to be faster so that users could get preliminary reports quickly that they could then iterate over in subsequent turns. For speed improvements, we decided to train AstaBrief to directly generate the final report in one pass given a user query and relevant retrieved snippets, bypassing the expensive snippet summarization and clustering stages our Claude-based Thinking mode uses and not writing out the answer section-by-section.
L89: Interestingly, we found it was possible to do so without sacrificing performance.
L90: ### Collecting SFT training data
L91: 
L92: The training pipeline began with real user queries submitted through the system described in our paper “cite36†Synthesizing scientific literature with retrieval-augmented LMs ” and cite37†ScholarQA†aclanthology.org , the framework that now underpins Asta’s Generate a report feature. Rather than training only on synthetic prompts or benchmark-style tasks, we wanted AstaBrief to learn from real queries from real scientists.
L93: Our research suggests that scientists often ask different things of language models than users do of general-purpose chatbots or traditional search tools. In our cite38†analysis of hundreds of thousands of Asta queries , expert researchers frequently supplied substantial context, multiple constraints, and relationships between concepts rather than relying on short, keyword-style prompts.
L94: More recent Asta user studies have also surfaced differences in how researchers want AI involved in their work—some are comfortable using models for ideation or experimentation, while others prefer a narrower role in synthesis, literature surveillance, or pattern-finding. Across those differences, participants want clearer source traceability, more visibility into what a model is doing, and greater control over the context it uses.
L95: We filtered the user logs we collected for quality, relevance, and privacy, stripping out beta-tester and bot traffic, dropping queries that were too short to be meaningful, and using an LLM-based filtering pass to catch non-English queries, non-scientific requests, and prompts containing personal information. That left a pool of 90K research-focused queries.
L96: For SFT, we generated full-report target outputs from the filtered queries using the multi-step ScholarQA pipeline behind Asta's report generation. The pipeline retrieved relevant literature, organized the material into sections, and used a backing report-generating model to synthesize the evidence into a cited report. We drew on a mix of proprietary systems: Claude 3.5 Sonnet, Claude 3.7 Sonnet, o3, o4-mini, and GPT-4.1. After quality filtering, this yielded 47K usable training examples.
L97: ### Creating DPO pairs
L98: 
L99: DPO required a different kind of training data. Instead of a single target report per query, we needed pairs of reports with one preferred over the other.
L100: We built those pairs from a separate subset of queries not used during SFT data generation. One report per query came from the existing ScholarQA pipeline, typically backed by Claude 3.5 Sonnet or 3.7 Sonnet. The competing report was generated by feeding ScholarQA's retrieved literature excerpts to a different model: o3, o4-mini, DeepSeek-V3, or DeepSeek-R1, depending on the example.
L101: Two judge models – GPT-4.1 and DeepSeek-R1 – compared each pair and picked a winner. We ensured that LLM judges were aligned with human preferences (95% agreement) and only kept pairs where both judges agreed, which gave us a cleaner preference set and cut much of the noise that typically shows up in preference data generated at scale.
L102: 
L103: After quality filtering, the final DPO dataset came to about 6K examples.
L104: Using multiple generators and requiring agreement between two judges gave us a relatively simple way to construct preference data without treating any single model’s output or judgment as ground truth.
L105: ### Filtering data for better attribution
L106: 
L107: Our main evaluation target was cite39†SQABench-CS2†github.com , a set of 200 user-written computer science research questions. We tracked four metrics throughout the development of AstaBrief:
L108:   * Rubric score, which measures how much necessary content is covered by the report.
L109:   * Answer precision, which measures whether each paragraph is relevant to the question.
L110:   * Citation precision, which measures whether each citation supports the claim it's attached to.
L111:   * Citation recall, which measures whether the report's claims are fully supported by the citations provided.
L112: For our final model, we also ran secondary evaluations: cite40†DeepScholarBench†arxiv.org , a 63-query benchmark for long-form research synthesis built from recent ArXiv papers, and two separate pairwise evaluations against reports generated by the Claude-powered pipeline—an LLM-judged comparison on SQABench-CS2 and a small human study.
L113: A report can sound polished and complete while meandering from the question or attaching citations to claims from which the underlying evidence doesn't follow. For scientific synthesis, we needed to measure those behaviors separately. But citation support is only part of scientific faithfulness—a model can cite the right study and still make a stronger claim than the study itself supports.
--------------------------------------------------------------------------------
Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs | Ai2 (https://allenai.org/blog/olmocore3)
citeturn29558view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29550view1","lineno":97}); Total lines: 168
L0: cite0†Skip to main content -> L1: 
L2: cite1†Ai2 L3: 
L4:   * Open models
L5: 
L6: ### Open models
L7: 
L8:     * cite2†Olmo L9:     * cite3†Tülu 3 L10:     * cite4†Molmo L11:     * cite5†Playground†playground.allenai.org L12:     * cite6†Language models L13:     * cite7†Multimodal models L14:     * cite8†Evaluation frameworks L15:     * cite9†Open data L16: 
L17: cite10†Image: A computer generated image showing swaths of shapes, meant to depict a hopeful futuristic feeling.†www.datocms-assets.com L18: 
L19:   * Applications
L20: 
L21: cite11†Image†www.datocms-assets.com L22: ### AI for science
L23: 
L24:     * cite12†Asta L25:     * cite13†AstaBench L26:     * cite14†Research with Asta†asta.allen.ai L27:     * cite15†Asta leaderboards L28:     * cite16†Semantic Scholar†www.semanticscholar.org L29:     * cite17†All projects L30: 
L31: ### AI for the planet
L32: 
L33:     * cite18†OlmoEarth L34:     * cite19†EarthRanger L35:     * cite20†Skylight L36:     * cite21†Climate Modeling L37:     * cite22†All projects L38: 
L39: ### AI for robotics
L40: 
L41:     * cite23†Embodied AI L42: 
L43:   * Research
L44: ### Research
L45: 
L46:     * cite24†Latest L47:     * cite25†Papers L48:     * cite26†Research principles L49: 
L50:   * cite27†News L51:   * Institute
L52: 
L53: ### Institute
L54: 
L55:     * cite28†About L56:     * cite29†Careers L57:     * cite30†Media center L58: 
L59: Navigation Menu
L60: # Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs
L61: 
L62: October 1, 2026
L63: 
L64: Ai2
L65: 
L66: Share
L67: 
L68: * * *
L69: 
L70: cite31†Tech Report cite32†Code†github.com cite33†Interactive demo†narrative.allen.ai L71: 
L72: Today we’re releasing cite32†Olmo-core 3†github.com , a significant upgrade to our framework for developing large language models featuring a redesigned open mixture-of-experts (MoE) training system.
L73: Olmo-core 3 is designed to scale MoE training into the trillion-parameter range while preserving computational efficiency. It’s one of the core systems behind the next generation of Olmo, and part of our ongoing commitment to open up the tools and training infrastructure behind each new model.
L74: Training large AI models takes a lot of compute, driving up costs and energy use and putting advanced model development out of reach for many academic researchers and smaller labs. MoE models offer a more efficient approach—they can contain many more learned components, or parameters, without requiring every input to use all of them.
L75: But the full model still has to be stored across GPU memory and updated during training, and directing inputs to the right experts – the specialized components within an MoE – across a cluster creates its own communication and coordination costs. As MoEs grow, those costs can erode much of the computational advantage of using only part of the model for each input.
L76: Olmo-core 3 is built to close that gap. In one benchmark, we increased the expert pool from 8 to 128 while still selecting only four experts per token – the small units of text a language model processes – keeping the number of active parameters per token roughly fixed at about 3.2B. Total parameter capacity grew from 4.6B to 47B, while training throughput fell by less than 5%.
L77: 
L78: The same infrastructure has been benchmarked at over one trillion total parameters.
L79: 
L80: cite34†Image†www.datocms-assets.com L81: ### Building a training stack around how MoEs actually work
L82: 
L83: Olmo-core has evolved with each generation of Olmo.
L84: 
L85: Our work on sparse models goes back to cite35†OlmoE , which used an MoE architecture with 64 routed experts. cite36†Olmo 3 , by contrast, used a dense architecture, meaning nearly all of the model was active for every token and its training stack was built around that design. Olmo-core 3 extends the framework with a training system designed for much larger MoE models.
L86: Our earlier MoE implementation in Olmo-core used fully sharded data parallelism (FSDP), configured to gather and reshard model weights for each small batch of training data. Olmo-core 3 switches to a system based on cite37†distributed data parallelism (DDP)†narrative.allen.ai . It keeps experts resident on GPUs and routes the relevant data to them, avoiding that repeated weight gathering.
L87: NVIDIA’s Megatron-Core is an established option for training large MoEs. Olmo-core 3 brings an integrated MoE training stack to the framework behind Olmo, with a redesign that improves throughput over our earlier FSDP-based implementation. In a preliminary test on eight NVIDIA B300 GPUs, a 47-billion-parameter MoE processed 52,000 tokens per second per GPU with the new stack, compared with 19,400 using our earlier implementation—about 2.7× the throughput.
L88: 
L89: cite38†Image†www.datocms-assets.com L90: ### Scaling and optimizing MoE training
L91: 
L92: Olmo-core 3 combines several techniques for distributing large MoEs across GPU clusters with optimizations that make routing and computation more efficient.
L93: 
L94: Three techniques determine how the model and its training state are split across hardware:
L95:   * cite39†Expert parallelism†narrative.allen.ai spreads the experts across GPUs, so each GPU stores only part of the full expert pool.
L96:   * cite40†Pipeline parallelism†narrative.allen.ai splits the model’s layers – the successive stages that transform an input – across groups of GPUs, reducing how much of the model each GPU needs to keep in memory.
L97:   * A distributed optimizer spreads the optimizer state – the additional data used to calculate and apply updates during training – across GPUs instead of storing a full copy on every GPU.
L98: Together, these techniques allow an MoE to scale without requiring every GPU to keep the entire model and its training state in memory.
L99: Olmo-core 3 also reduces the cost of routing data to the right experts and running their computations. Rowwise expert parallelism places routed data directly into expert input buffers, minimizing the extra work needed to rearrange it. GPU-resident routing keeps routing metadata on the GPUs, so the CPU can queue work without waiting for that information to be copied back. And grouped GEMM combines many small expert computations so GPUs can execute them more efficiently.
L100: Finally, Olmo-core 3 supports MXFP8, a lower-precision number format that represents some values with fewer bits. This can reduce computation and the amount of data moved between GPUs, as long as those savings outweigh the cost of converting between number formats.
L101: We measured MXFP8’s effect on end-to-end training throughput in a controlled benchmark on four NVIDIA B300 GPUs, with work distributed uniformly across experts. With MXFP8 enabled across the parts of the system where it helped most, training throughput was about 21% higher than with BF16, the higher-precision format we used as our baseline, while peak active memory fell from 103 GiB to 95 GiB. Most of the gain came from feed-forward computation and moving data between experts rather than attention alone.
L102: These techniques and optimizations have to work together. Speeding up one part of training can create costs elsewhere; faster computation may require more data movement, while moving fewer bits may not help if converting the data takes too long. Olmo-core 3 is built around those trade-offs across the full training process, giving us – and researchers using the open stack – control over how the pieces fit together.
L103: cite33†Explore our interactive walkthrough†narrative.allen.ai to see how data, expert, and pipeline parallelism work together to scale MoE training—from a single GPU to many.
L104: ### Scaling into the trillion-parameter range
L105: 
L106: We’ve benchmarked Olmo-core 3 across a range of configurations on NVIDIA B300 GPUs, including a 1.2-trillion-parameter model with 58.36 billion parameters active per token across 512 GPUs. Its highest observed throughput was 858 TFLOP/s/GPU—a measure of useful model computation per second on each GPU. These tests used random routing to measure system performance, rather than the quality of a trained model.
L107: We’ve also experimented with DeepEP v2, an alternative way of handling communication between experts across GPUs, reaching a configuration with 2.38 trillion total parameters. This was a short-capacity test rather than a full training run, so it demonstrates the scale Olmo-core 3 can reach rather than sustained training performance.
L108: At these scales, systems performance is only part of the picture. Our technical report also documents experiments that informed how we train MoEs and measure their performance. For example:
L109:   * A score intended to encourage balanced routing could improve even as the actual workload became less balanced. We call this failure token gerrymandering.
L110:   * Lowering experts’ learning rates – the size of their training updates – because they process fewer tokens did not improve results in the model family we tested.
L111:   * GPU calculations took different amounts of time when the values being processed changed, even with the same matrix dimensions. Performance comparisons therefore need matching input values as well as matching shapes.
L112:   * Overlapping communication and computation on separate GPU streams did not always make training faster. In some tests, it slowed end-to-end execution—a reminder that more overlap does not necessarily mean higher throughput.
L113: The report explains these findings alongside the approaches we tested and chose not to adopt.
L114: ### Built for the next generation of Olmo, open for everyone
L115: 
L116: Olmo-core 3 is the foundation for what we’re building next. Our next-generation Olmo will use an MoE architecture, and we’re aiming for it to be our most capable Olmo yet, trained on our largest dataset and with our longest context window.
L117: The new stack lets us scale beyond our previous MoE work while giving us more flexibility to adapt training as models and hardware evolve. And it’s fully open—researchers and developers can use Olmo-core 3 to train their own MoEs, adapt it to different hardware, and experiment with routing, parallelism, and other parts of the system.
L118: 
L119: That’s part of how we think about open model development—model weights are more useful when the infrastructure and training decisions behind them are open too.
L120: For a deeper look at the systems design, experiments, ablations, and approaches we tested along the way, read our technical report and cite32†explore Olmo-core 3 on GitHub†github.com .
L121: ## Join us
L122: 
L123: At Ai2 we’re building the future of transparent, open-source AI — built in the open to empower scientific progress and fundamental understanding of this world changing technology. We’re not here to make profits, we’re here to make sure benefits of AI are shared widely and for the benefit of humanity. If this appeals to you, please take a look at our open roles.
L124: 
L125: cite29†Open roles L126: ## Subscribe to receive monthly updates about the latest Ai2 news.
L127: 
L128: First Name[Input]
L129: 
L130: Last Name[Input]
L131: 
L132: Email[Input]
L133: 
L134: Sign up
L135: 
L136: Contact us
L137: 
L138: Questions about our work, or need support with one of our technologies?
L139: 
L140: cite41†Get in touch L141: 
L142: Resources
L143: 
L144:   * cite30†Media center L145:   * cite42†Documentation†docs.allenai.org L146:   * cite29†Careers L147:   * cite43†Team directory L148: 
L149: Community
L150:   * cite44†Discord†discord.gg L151:   * cite45†Reddit†www.reddit.com L152:   * cite46†X/Twitter†x.com L153:   * cite47†GitHub†github.com L154:   * cite48†Hugging Face†huggingface.co L155:   * cite49†LinkedIn†www.linkedin.com L156:   * cite50†Bluesky†bsky.app L157: 
L158: Legal
L159: 
L160:   * cite51†Terms of use L161:   * cite52†Privacy policy L162:   * cite53†DMCA policy L163:   * cite54†Business code of conduct L164:   * cite55†Responsible use L165:   * [Button: Update consent]
L166: 
L167: © The Allen Institute for Artificial Intelligence - All Rights Reserved.

