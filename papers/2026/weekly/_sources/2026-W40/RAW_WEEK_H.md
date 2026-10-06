Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs | Ai2 (https://allenai.org/blog/olmocore3)
citeturn29551view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29550view1","lineno":62}); Total lines: 168
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
--------------------------------------------------------------------------------
Open-sourcing AstaBrief, the fast report-generation model in Asta | Ai2 (https://allenai.org/blog/astabrief)
citeturn29551view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29550view2","lineno":64}); Total lines: 197
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
--------------------------------------------------------------------------------
How Extropic Uses Prime Intellect to Train a Thermodynamic ML Research Agent (https://www.primeintellect.ai/case-study/extropic)
citeturn29551view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29543view2","lineno":66}); Total lines: 126
L48: ## The problem
L49: 
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
L68: Extropic built their RL environment with cite24†verifiers†github.com , Prime Intellect's open-source library for building environments. This environment contains about 50 coding tasks adapted from classic connectionist experiments. In each task, the model works in a Python REPL inside a Prime Sandbox. It writes code, runs it, reads any error, revises, and submits a solution.
L69: 
L70: Each submission is scored in two parts:
L71: $$r = 0.7 \cdot \text{exec} + 0.3 \cdot \text{rubric}$$r=0.7⋅exec+0.3⋅rubric
L72: 
L73: Execution (70%) measures whether the code runs and whether it reproduces the reference metric from the original experiment. Rubric (30%) is graded by an LLM judge, Nemotron 3 Super 120B, which scores each solution against a per-task rubric.
L74: In this experiment, execution carries most of the weight by design. Scoring on execution means running untrusted, model-written code on every rollout during training. Each change to the reward produced a new environment version, so Extropic always knew which scores could be compared.
L75: ### RL loops
L76: 
L77: “On self-managed infrastructure, most of those runs would not have happened, and we would have shipped a smaller project”
L78: 
L79: Gill Verdon
L80: 
L81: Founder & CEO, Extropic
L82: Extropic trained two Qwen models with reinforcement learning, using GRPO as the objective. They ran training on cite17†Hosted Training†docs.primeintellect.ai , Prime Intellect's managed RL training. For each run, Extropic's researchers chose the base model, built the environment with verifiers, and wrote the run config. Prime ran rollout generation and training on its managed GPU infrastructure, so Extropic's team never had to set up or manage any.
L83: Each training step had two halves: rollouts and an update. Each rollout ran in its own cite25†Prime Sandbox , which executed the model’s code and returned the execution score. cite19†Prime Inference†docs.primeintellect.ai served the LLM judge, which graded the rubric score for every rollout.
L84: 
L85: In the update, GRPO compared the model's attempts at each task against one another. It reinforced the attempts that scored above the group's average and discouraged those below it.
L86: During training, Extropic tracked performance on held-out tasks the model never trained on. After training, they deployed checkpoints on cite19†Prime Inference†docs.primeintellect.ai and ran their evals in parallel. The frontier baselines also ran through Prime Inference against the same environment.
L87: ## Results
L88: 
L89: After 100 GRPO steps on Hosted Training, Qwen3.6-35B-A3B's reward on held-out problems rose from 0.127 to 0.361, a 2.8x gain.
L90: 
L91: cite26†Image: Held-out task rewards before and after reinforcement learning L92: 
L93: Held-out task rewards before and after reinforcement learning. Qwen3.6 improves from 0.127 to 0.361 after 100 GRPO steps.
L94: The recipe transferred across model families: Qwen3.5, post-trained the same way, landed almost level with Qwen3.6. Both finished well ahead of other open models and closed much of the gap to Claude Opus 4.8, with a model that activates only 3B parameters per token.
L95: ## What's next
L96: 
L97: Reproducing classic experiments was the first step. Extropic’s ultimate goal is thermo RSI: agents that discover new sampling-based learning rules for TSUs, expanding what the hardware can do, which then supports more capable agents.
L98: 
L99: Their next experiments will rely on the same infrastructure that made the first ones possible.
L100: 
L101: Read Extropic’s post: cite20†Recursive intelligence for a new substrate†recursive-intelligence.vercel.app .
L102: To post-train a model for your own task, cite10†get started with Prime Intellect†app.primeintellect.ai .
L103: 
L104: cite10†Start training†app.primeintellect.ai cite8†Book a call L105: 
L106: Platform
L107: 
L108: cite1†Lab cite3†Compute cite4†Research L109: 
L110: Company
L111: 
L112: cite7†Careers30 cite27†Merch†primeintellect.supply cite8†Contact L113: 
L114: Community
L115: 
L116: cite28†X†x.com cite29†LinkedIn†www.linkedin.com cite30†Discord†discord.gg cite31†Luma†luma.com L117: 
L118: Resources
L119: cite5†Docs†docs.primeintellect.ai cite6†Writings cite31†Events†luma.com cite27†Merch†primeintellect.supply cite32†Platform Status†status.primeintellect.ai L120: 
L121: Terms
L122: 
L123: cite33†Terms of Service cite34†Privacy Policy cite35†Security Policy L124: 
L125: © 2026 Prime Intellect, Inc.
--------------------------------------------------------------------------------
Mistral Opens Munich Hub to Advance Industrial AI in Germany (https://mistral.ai/news/hallo-deutschland/)
citeturn29551view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29543view4","lineno":80}); Total lines: 165
L0: cite0†iframe†www.googletagmanager.com L1: 
L2: cite1†Get in touch L3: 
L4: Menu
L5: 
L6: Products
L7: 
L8: Industries
L9: 
L10: Research
L11: 
L12: Developers
L13: 
L14: Blog
L15: 
L16: Customers
L17: 
L18: Company
L19: 
L20: cite2†Get in touch cite3†Login†console.mistral.ai L21: 
L22: cite4†Vibe for code Coding agents in the terminal, IDE, and background. cite5†AI Cloud Frontier-scale infrastructure for training and inference. L23: 
L24: Pricing
L25: 
L26: Domains
L27: 
L28: Applied AI
L29: 
L30: Latest models
L31: 
L32: cite6†See all models†docs.mistral.ai L33: 
L34: Latest posts
L35: cite7†Mistral and Mozilla are bringing open, private and multilingual AI to your web browser cite8†Cloudera and Mistral Partner to Bring Specialized, Sovereign Intelligence to Enterprise Data L36: 
L37: cite9†Read all news L38: 
L39: Categories
L40: 
L41: Featured stories
L42: 
L43: cite10†See all L44: 
L45: Who we are
L46: 
L47: Connect
L48: 
L49: cite4†Vibe for code Coding agents in the terminal, IDE, and background. cite5†AI Cloud Frontier-scale infrastructure for training and inference. L50: 
L51: Pricing
L52: 
L53: Domains
L54: 
L55: Applied AI
L56: 
L57: Latest models
L58: 
L59: cite6†See all models†docs.mistral.ai L60: 
L61: Latest posts
L62: cite7†Mistral and Mozilla are bringing open, private and multilingual AI to your web browser cite8†Cloudera and Mistral Partner to Bring Specialized, Sovereign Intelligence to Enterprise Data L63: 
L64: cite9†Read all news L65: 
L66: Categories
L67: 
L68: Featured stories
L69: 
L70: cite10†See all L71: 
L72: Who we are
L73: 
L74: Connect
L75: 
L76: Company
L77: # Hallo, Deutschland!
L78: 
L79: September 28, 2026
L80: 
L81: By Mistral
L82: 
L83: cite11†Image L84: 
L85: Mistral Opens German Hub in Munich to Advance Industrial AI in Europe’s Largest Economy
L86: 
L87: At Mistral, we have always believed that the most consequential AI applications will be built where real industrial problems are solved. Today, we are putting that conviction into practice by opening our new hub in Munich.
L88: Germany is the largest industrial economy in the European Union. Its enterprises have accumulated proprietary data and process knowledge over generations, across automotive, energy, aerospace, and advanced manufacturing. That depth of industrial knowledge is exactly where AI, done right, compounds into competitive advantage. Munich is where we want to do that work.
L89: Our Munich hub will house specialised research teams dedicated to Physics AI and Industrial AI, alongside applied engineers serving our enterprise partners directly. We are not coming as a software vendor. We are coming as a long-term technological partner.
L90: ## Building for sovereignty, not just access
L91: 
L92: German industry, public institutions, and organizations already have access to our full AI stack: frontier language models, Physics AI capabilities, enterprise deployment, and sovereign compute infrastructure under one roof. To secure Europe’s AI sovereignty, Mistral will build one gigawatt of European compute capacity by 2030. In parallel, we continue to advance our frontier model development at full speed.
L93: What makes this stack genuinely sovereign is our open-weight architecture. Unlike closed AI systems where the model’s internal logic is hidden and runs on the vendor’s servers, Mistral’s model weights are fully accessible to the customer. Our models run on the customer’s own infrastructure, trained on their data, operated under European law, with full auditability and no data leaving the organization. The intelligence stays where it was built.
L94: Mistral is a powerful example of what Europe can achieve: developing cutting-edge technology, turning it into a global success, and taking responsibility at the same time. It demonstrates what European research, talent, and entrepreneurial spirit can achieve. And that technological success and responsible AI development are not contradictory.
L95: 
L96: Dr. Karsten Wildberger, German Federal Minister for Digital Transformation and Government Modernisation
L97: ## Physics AI: a new capability for heavy industry
L98: 
L99: The next major advance in industrial AI will come from systems that understand the physical world: fluid dynamics, material deformation, thermal behavior, mechanical stress. These are the calculations at the heart of German manufacturing and engineering. Today, the necessary simulations require enormous compute time, sometimes taking days per run.
L100: Following our acquisition of Emmi AI in May 2026, more than 30 physicists, researchers, and engineers with unique expertise in Physics and Engineering AI joined Mistral. Emmi AI has specialised in large-scale AI modelling of computational fluid dynamics, structural mechanics, and multi-physics simulations.
L101: In Munich, we are working with BMW on crash simulations and engineering AI, and with Siemens Energy on industrial AI applications – developing what we believe will be the blueprint for Physics AI in European heavy industry.
L102: ## Why Munich
L103: 
L104: Bavaria has a long record of establishing and scaling new technologies, from precision manufacturing and defence tech to advanced materials and semiconductors. Munich gives us world-class research institutions and universities, deep industrial roots, a dense technology ecosystem, and the engineering talent to match – drawn from across Europe and beyond by the quality of life and proximity to the Alps.
L105: As part of our investment in Germany, we have formed a research partnership with the Technical University Munich (TUM), using TUM’s wind tunnel facilities to develop digital twins for automotive aerodynamics in collaboration with Prof. Dr. Nikolaus A. Adams. This research aims to fuse real-time experimental sensor data with offline computational fluid dynamics simulations to deliver highly accurate aerodynamic predictions in real time.
L106: Mistral stands for powerful AI made in Europe. Technological sovereignty is political sovereignty. That is why we need strong European AI champions that take a leading role in international competition. Mistral’s decision to choose Munich sends a strong signal for our position as a high-tech location. Bienvenue à Munich, bienvenue en Bavière!
L107: 
L108: Dr. Florian Herrmann, Head of the Bavarian State Chancellery and State Minister for Federal and Media Affairs
--------------------------------------------------------------------------------
World Labs is Joining AMD | World Labs (https://www.worldlabs.ai/blog/amd-announcement)
citeturn29551view4 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29543view3","lineno":null}); Total lines: 36
--------------------------------------------------------------------------------
Chris Painter's testimony to the U.S. Senate on AI agent incidents - METR (https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/)
citeturn29551view5 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn29543view6","lineno":28}); Total lines: 255
L0:   * Our Work
L1: 
L2:     * cite0†Research L3:     * cite1†Notes L4:     * cite2†Updates L5:     * cite3†Risk Assessment L6: 
L7:   * cite4†About L8:   * cite5†Donate L9:   * cite6†Careers L10:   * cite7†Search L11: 
L12: cite8†Image: METR Logo L13: 
L14:   * cite9†Our Work L15: 
L16: cite0†Research cite1†Notes cite2†Updates cite3†Risk Assessment L17: 
L18:   * cite4†About L19:   * cite5†Donate L20:   * cite6†Careers L21:   * [Input] [Input: Search...]
L22: 
L23: [Button: Menu]
L24: 
L25: Chris Painter's testimony to the U.S. Senate on AI agent incidents
L26: 
L27: ##### CONTRIBUTORS
L28: 
L29: cite10†Chris Painter L30: ##### DATE
L31: 
L32: September 30, 2026
L33: 
L34: [Input: Join our newsletter] [Button: Subscribe]
L35: 
L36: On September 30, 2026, METR President Chris Painter testified before the U.S. Senate Committee on Homeland Security & Governmental Affairs’ Subcommittee on Disaster Management, District of Columbia, and Census, at a hearing titled cite11†“Rogue AI: Securing the Homeland Against AI Agent Attacks”†www.hsgac.senate.gov . The written testimony is published in full below, and is also available as a cite12†PDF .
L37: ## Introduction
L38: 
L39: Chairman Hawley, Ranking Member Kim, and members of the subcommittee, thank you for inviting me to testify today. My name is Chris Painter and I am the President of METR. It is a great honor to be speaking before you, especially on the topic of AI agent incidents. With the recent rise in interest (and concern) around where AI development is headed I think it is critical that policymakers are armed with reliable, factual information about what we have actually observed from AI systems.
L40: METR,^{cite13†1 } which stands for Model Evaluation & Threat Research, is a nonprofit research organization that aims to share high-quality technical evidence about AI advances so the public can make informed decisions about this technology.^{cite14†2 } Our work has primarily focused on running tests that measure the capabilities of the most advanced, autonomous systems (or frontier AI agents) and publishing our results.
L41: These measurements were intended to provide an early warning signal as to when frontier AI agents are capable enough that they might steer towards pursuing goals no human intended for them to pursue.^{cite15†3 }
L42: Over the years, METR has worked to gather evidence about these frontier AI agents with access provided^{cite16†4 } by America’s leading AI developers such as OpenAI, Anthropic, Google, Meta, SpaceXAI, and Amazon. The participation of these AI developers is voluntary,^{cite17†5 } and METR is not paid or funded^{cite18†6 } by them.
L43: Today, I am here to speak about one particular voluntary engagement, in which OpenAI allowed a handful of my colleagues^{cite19†7 } inside its walls to conduct a brief investigation into how its agents behaved, reasoned, and collaborated to hack Hugging Face.
L44: In my remarks, I will reflect on three key questions, drawing on METR’s work:
L45: 
L46:   1. What happened in the OpenAI / Hugging Face incident?
L47:   2. How does this incident relate to patterns observed across the AI industry?
L48:   3. How might one better anticipate future AI agent incidents?
L49: ## The OpenAI / Hugging Face incident
L50: 
L51: Let us address our first question: “What happened in the OpenAI / Hugging Face incident?”
L52: On July 21, OpenAI disclosed that AI agents it was internally testing had compromised a company called Hugging Face, which runs a widely-used platform for AI infrastructure.
L53: On July 29, METR announced that it had agreed to conduct a brief investigation of this incident, scoped to a limited set of questions that focused on how agents behaved, reasoned, and collaborated.^{cite20†8 } A team of 3 investigators from METR and Redwood Research^{cite21†9 } then worked on- and off-premises to understand what OpenAI’s agents had done in the lead-up to their attack on Hugging Face.
L54: These investigators compiled their findings into a detailed cite22†report , a redacted version of which was then published on August 26 alongside OpenAI’s own more broadly-scoped cite23†report†cdn.openai.com .
L55: Combined, the reports from OpenAI and the outside investigators stretch to over 100 pages. Though I strongly recommend reading both reports in order to understand the full scope of the incident, I will briefly restate some basic facts from across the two reports:
L56: 
L57: Setup
L58:   * OpenAI launched tens of thousands of AI agents in internal tests across multiple models, including a highly capable and “persistent” unreleased model. Each agent was placed in its own separate computer environment intended to be isolated from the Internet and was tasked with completing its own self-contained cybersecurity problem.
L59:   * Some of the AI agents that OpenAI tasked in these cybersecurity tests were accidentally given problems that could not be completed as instructed.

