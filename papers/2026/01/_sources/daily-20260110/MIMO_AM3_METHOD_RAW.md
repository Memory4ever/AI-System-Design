# 原始必要核心返回（Jan10，仅具名命题）

[2601.02780v1] MiMo-V2-Flash Technical Report (https://arxiv.org/abs/2601.02780v1)
citeturn26853view0 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.02780v1","lineno":null}); Total lines: 163
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 6 Jan 2026 (this version), latest version 8 Jan 2026 (cite5†v2 )]
L9: # Title:MiMo-V2-Flash Technical Report
L10: Authors:cite6†Bangjun Xiao , cite7†Bingquan Xia , cite8†Bo Yang , cite9†Bofei Gao , cite10†Bowen Shen , cite11†Chen Zhang , cite12†Chenhong He , cite13†Chiheng Lou , cite14†Fuli Luo , cite15†Gang Wang , cite16†Gang Xie , cite17†Hailin Zhang , cite18†Hanglong Lv , cite19†Hanyu Li , cite20†Heyu Chen , cite21†Hongshen Xu , cite17†Houbin Zhang , cite22†Huaqiu Liu , cite23†Jiangshan Duo , cite24†Jianyu Wei , cite25†Jiebao Xiao , cite26†Jinhao Dong , cite27†Jun Shi , cite28†Junhao Hu , cite29†Kainan Bao , cite30†Kang Zhou , cite31†Lei Li , cite32†Liang Zhao , cite33†Linghao Zhang , cite34†Peidian Li , cite35†Qianli Chen , cite36†Shaohui Liu , cite37†Shihua Yu , cite38†Shijie Cao , cite39†Shimao Chen , cite37†Shouqiu Yu , cite36†Shuo Liu , cite40†Tianling Zhou , cite41†Weijiang Su , cite42†Weikun Wang , cite43†Wenhan Ma , cite44†Xiangwei Deng , cite45†Bohan Mao , cite46†Bowen Ye , cite47†Can Cai , cite48†Chenghua Wang , cite49†Chengxuan Zhu , cite50†Chong Ma , cite51†Chun Chen , cite52†Chunan Li , cite53†Dawei Zhu , cite54†Deshan Xiao , cite55†Dong Zhang , cite55†Duo Zhang , cite56†Fangyue Liu , cite57†Feiyu Yang , cite58†Fengyuan Shi , cite15†Guoan Wang , cite59†Hao Tian , cite60†Hao Wu , cite61†Heng Qu , cite62†Hongfei Yi , cite63†Hongxu An , cite64†Hongyi Guan , cite65†Xing Zhang , cite66†Yifan Song , cite67†Yihan Yan , cite68†Yihao Zhao , cite69†Yingchun Lai , cite70†Yizhao Gao , cite71†Yu Cheng , cite72†Yuanyuan Tian , cite73†Yudong Wang , cite74†Zhen Tang , cite74†Zhengju Tang , cite75†Zhengtao Wen , cite76†Zhichao Song , cite77†Zhixian Zheng , cite78†Zihan Jiang , cite79†Jian Wen , cite80†Jiarui Sun , cite81†Jiawei Li , cite82†Jinlong Xue , cite83†Jun Xia , cite84†Kai Fang , cite85†Menghang Zhu , cite86†Nuo Chen , cite87†Qian Tu , cite88†Qihao Zhang , cite89†Qiying Wang , cite90†Rang Li , cite91†Rui Ma , cite92†Shaolei Zhang , cite93†Shengfan Wang , cite94†Shicheng Li , cite95†Shuhao Gu , cite96†Shuhuai Ren , cite97†Sirui Deng , cite98†Tao Guo , cite99†Tianyang Lu L11: , cite100†Weiji Zhuang , cite101†Weikang Zhang , cite102†Weimin Xiong , cite103†Wenshan Huang , cite104†Wenyu Yang , cite65†Xin Zhang , cite105†Xing Yong , cite106†Xu Wang , cite107†Xueyang Xie , cite108†Yilin Jiang , cite109†Yixin Yang , cite110†Yongzhe He , cite111†Yu Tu , cite112†Yuanliang Dong , cite113†Yuchen Liu , cite114†Yue Ma , cite115†Yue Yu , cite116†Yuxing Xiang , cite117†Zhaojun Huang , cite118†Zhenru Lin , cite119†Zhipeng Xu , cite120†Zhiyang Chen , cite121†Zhonghua Deng , cite122†Zihan Zhang , cite123†Zihao Yue L12: et al. (25 additional authors not shown)  You must enable JavaScript to view entire author list.
L13: 
L14: View a PDF of the paper titled MiMo-V2-Flash Technical Report, by Bangjun Xiao and 124 other authors
L15: 
L16: cite124†View PDF cite125†HTML (experimental) L17: > Abstract:We present MiMo-V2-Flash, a Mixture-of-Experts (MoE) model with 309B total parameters and 15B active parameters, designed for fast, strong reasoning and agentic capabilities. MiMo-V2-Flash adopts a hybrid attention architecture that interleaves Sliding Window Attention (SWA) with global attention, with a 128-token sliding window under a 5:1 hybrid ratio.
L18: The model is pre-trained on 27 trillion tokens with Multi-Token Prediction (MTP), employing a native 32k context length and subsequently extended to 256k. To efficiently scale post-training compute, MiMo-V2-Flash introduces a novel Multi-Teacher On-Policy Distillation (MOPD) paradigm. In this framework, domain-specialized teachers (e.g., trained via large-scale reinforcement learning) provide dense and token-level reward, enabling the student model to perfectly master teacher expertise.
L19: MiMo-V2-Flash rivals top-tier open-weight models such as DeepSeek-V3.2 and Kimi-K2, despite using only 1/2 and 1/3 of their total parameters, respectively. During inference, by repurposing MTP as a draft model for speculative decoding, MiMo-V2-Flash achieves up to 3.6 acceptance length and 2.6x decoding speedup with three MTP layers. We open-source both the model weights and the three-layer MTP weights to foster open research and community collaboration.
L20: Comments:  | 31 pages, technical report
L21: Subjects:  | Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
L22: Cite as:  | cite126†arXiv:2601.02780 [cs.CL]
L23:    | (or cite127†arXiv:2601.02780v1 [cs.CL] for this version)
L24:    | cite128†https://doi.org/10.48550/arXiv.2601.02780†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Shijie Cao [cite129†view email ]
L28: [v1] Tue, 6 Jan 2026 07:31:47 UTC (314 KB)
L29: cite5†[v2] Thu, 8 Jan 2026 05:52:17 UTC (314 KB)
L30: 
L31: Full-text links:
L32: 
L33: ## Access Paper:
L34: 
L35: View a PDF of the paper titled MiMo-V2-Flash Technical Report, by Bangjun Xiao and 124 other authors
L36: 
L37:   * cite124†View PDF L38:   * cite125†HTML (experimental) L39:   * cite130†TeX Source L40: 
L41: cite131†view license L42: ### Current browse context:
L43: 
L44: cs.CL
L45: 
L46: cite132†< prev |   cite133†next > L47: 
L48: cite134†new | cite135†recent | cite136†2026-01 L49: 
L50: Change to browse by:
L51: 
L52: cite137†cs L53: cite138†cs.AI L54: 
L55: ### References & Citations
L56: 
L57:   * cite139†NASA ADS†ui.adsabs.harvard.edu L58:   * cite140†Google Scholar†scholar.google.com L59:   * cite141†Semantic Scholar†api.semanticscholar.org L60: 
L61: [Button: export BibTeX citation] Loading...
L62: 
L63: ## BibTeX formatted citation
L64: 
L65: [Button: ×]
L66: 
L67: loading...
L68: 
L69: Data provided by:
L70: 
L71: ### Bookmark
L72: 
L73: [Input] Bibliographic Tools
L74: # Bibliographic and Citation Tools
L75: 
L76: [Input] Bibliographic Explorer Toggle
L77: 
L78: Bibliographic Explorer (cite142†What is the Explorer?†info.arxiv.org )
L79: 
L80: [Input] Connected Papers Toggle
L81: 
L82: Connected Papers (cite143†What is Connected Papers?†www.connectedpapers.com )
L83: 
L84: [Input] Litmaps Toggle
L85: 
L86: Litmaps (cite144†What is Litmaps?†www.litmaps.co )
L87: 
L88: [Input] scite.ai Toggle
L89: 
L90: scite Smart Citations (cite145†What are Smart Citations?†www.scite.ai )
L91: 
L92: [Input] Code, Data, Media
L93: # Code, Data and Media Associated with this Article
L94: 
L95: [Input] alphaXiv Toggle
L96: 
L97: alphaXiv (cite146†What is alphaXiv?†alphaxiv.org )
L98: 
L99: [Input] Links to Code Toggle
L100: 
L101: CatalyzeX Code Finder for Papers (cite147†What is CatalyzeX?†www.catalyzex.com )
L102: 
L103: [Input] DagsHub Toggle
L104: 
L105: DagsHub (cite148†What is DagsHub?†dagshub.com )
L106: 
L107: [Input] GotitPub Toggle
L108: 
L109: Gotit.pub (cite149†What is GotitPub?†gotit.pub )
L110: 
L111: [Input] Huggingface Toggle
L112: 
L113: Hugging Face (cite150†What is Huggingface?†huggingface.co )
L114: 
L115: [Input] ScienceCast Toggle
L116: ScienceCast (cite151†What is ScienceCast?†sciencecast.org )
L117: 
L118: [Input] Demos
L119: # Demos
L120: 
L121: [Input] Replicate Toggle
L122: 
L123: Replicate (cite152†What is Replicate?†replicate.com )
L124: 
L125: [Input] Spaces Toggle
L126: 
L127: Hugging Face Spaces (cite153†What is Spaces?†huggingface.co )
L128: 
L129: [Input] Spaces Toggle
L130: 
L131: TXYZ.AI (cite154†What is TXYZ.AI?†txyz.ai )
L132: 
L133: [Input] Related Papers
L134: # Recommenders and Search Tools
L135: 
L136: [Input] Link to Influence Flower
L137: 
L138: Influence Flower (cite155†What are Influence Flowers?†influencemap.cmlab.dev )
L139: 
L140: [Input] Core recommender toggle
L141: 
L142: CORE Recommender (cite156†What is CORE?†core.ac.uk )
L143: 
L144:   * Author
L145:   * Venue
L146:   * Institution
L147:   * Topic
L148: 
L149: [Input] About arXivLabs
L150: # arXivLabs: experimental projects with community collaborators
L151: 
L152: arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
L153: 
L154: Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
L155: Have an idea for a project that will add value for arXiv's community? cite157†Learn more about arXivLabs†info.arxiv.org .
L156: 
L157: cite158†Which authors of this paper are endorsers? | Disable MathJax (cite159†What is MathJax?†info.arxiv.org )
L158: 
L159: We gratefully acknowledge support from our major funders, cite160†member institutions†info.arxiv.org , , and all contributors.
L160: cite161†About†info.arxiv.org · cite162†Help†info.arxiv.org · cite163†Contact†info.arxiv.org · cite164†Subscribe†info.arxiv.org · cite165†Copyright†info.arxiv.org · cite166†Privacy†info.arxiv.org · cite167†Accessibility†info.arxiv.org · cite168†Operational Status (opens in new tab)†status.arxiv.org L161: 
L162: Major funding support from
--------------------------------------------------------------------------------
AM3Safety: Towards Data Efficient Alignment of Multi-modal Multi-turn Safety for MLLMs (https://arxiv.org/html/2601.04736v1)
citeturn26853view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04736v1","lineno":null}); Total lines: 480
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†2.1 Dialogue Safety L19:     2. cite9†2.2 MLLMs Safety Alignment L20:   4. cite10†3 Methodology L21:     1. cite11†3.1 InterSafe-V L22:       1. cite12†Refusal VQA Pairs L23:       2. cite13†Step 1: Red-Team Queries Decomposition L24:       3. cite14†Step 2: Dialogue Construction L25:       4. cite15†Step 3: Data Cleaning L26:     2. cite16†3.2 AM^{3}Safety L27:       1. cite17†Refusal Template Learning L28:       2. cite18†Helpfulness Optimization L29:       3. cite19†Multi-Turn Dual-Objective Reward Function L30:   5. cite20†4 Experiments L31:     1. cite21†4.1 Experimental Setup L32:       1. cite22†Base Models and Settings L33:       2. cite23†Benchmarks L34:       3. cite24†Experimental Metrics L35:     2. cite25†4.2 Experimental Results L36:     3. cite26†4.3 Main experiment L37:     4. cite27†4.4 Results for General Tasks L38:     5. cite28†4.5 Comparison Between Each Step L39:     6. cite29†4.6 Ablation Study for Coefficient L40:       1. cite30†Safety Variance-Based Turn Weighting. L41:     7. cite31†4.7 Coefficient of Helpfulness L42:   6. cite32†5 Conclusion L43:   7. cite33†References L44:   8. cite34†A Existing Assets Licenses L45:   9. cite35†B Data Statistics L46:   10. cite36†C Addition Experiment Details L47:     1. cite37†C.1 Experimental Setup L48:     2. cite38†C.2 Experimental Results L49:   11. cite39†D Data L50:   12. cite40†E Prompts L51: cite41†License: CC BY 4.0†info.arxiv.org L52: 
L53: arXiv:2601.04736v1 [cs.CL] 08 Jan 2026
L54: # AM^{3}Safety: Towards Data Efficient Alignment of Multi-modal Multi-turn Safety for MLLMs
L55: Han ZHU ^{†}^{†}thanks: Equal Contribution; $ˆ†$Corresponding author.
L56: Affiliation: Hong Kong University of Science and Technology Email: hzhubo@connect.ust.hksiruihan@ust.hk    Jiale Chen    Chengkun Cai Affiliation: University of Edinburgh    Shengjie Sun Affiliation:  AISpeech    Haoran Li Affiliation: Hong Kong University of Science and Technology    Yujin Zhou Affiliation: Hong Kong University of Science and Technology    Chi-Min Chan Affiliation: Hong Kong University of Science and Technology    Pengcheng Wen Affiliation: Hong Kong University of Science and Technology    Lei Li Affiliation:  University of Washington    Sirui Han    Yike Guo Affiliation: Zhongshan School of Medicine, SUN YAT-SEN UNIVERSITY
L57: ###### Abstract
L58: Multi-modal Large Language Models (MLLMs) are increasingly deployed in interactive applications. However, their safety vulnerabilities become pronounced in multi-turn multi-modal scenarios, where harmful intent can be gradually reconstructed across turns, and security protocols fade into oblivion as the conversation progresses.
L59: Existing Reinforcement Learning from Human Feedback (RLHF) alignment methods are largely developed for single-turn visual question-answer (VQA) task and often require costly manual preference annotations, limiting their effectiveness and scalability in dialogues. To address this challenge, we present InterSafe-V, an open-source multi-modal dialogue dataset containing 11,270 dialogues and 500 specially designed refusal VQA samples.
L60: This dataset, constructed through interaction between several models, is designed to more accurately reflect real-world scenarios and includes specialized VQA pairs tailored for specific domains. Building on this dataset, we propose AM^{3}Safety, a framework that combines a cold-start refusal phase with Group Relative Policy Optimization (GRPO) fine-tuning using turn-aware dual-objective rewards across entire dialogues.
L61: Experiments on Qwen2.5-VL-7B-Instruct and LLaVA-NeXT-7B show more than 10% decrease in Attack Success Rate (ASR) together with an increment of at least 8% in harmless dimension and over 13% in helpful dimension of MLLMs on multi-modal multi-turn safety benchmarks, while preserving their general abilities.
L62: ## 1 Introduction
L63: In recent years, MLLMs have undergone significant advancements and are progressively integrating into various aspects of daily life. Models such as Claude, Gemini, and GPT [cite42†1 , cite43†5 , cite44†25 ] demonstrate remarkable capabilities on complex multi-modal tasks, including image understanding, front-end coding and geometric reasoning.
L64: However, recent studies suggest that when integrating visual components, MLLMs may partially “forget” the safety protocols of their backbone Large Language Models (LLMs) [cite45†12 , cite46†20 , cite47†35 ]. Furthermore, the safety mechanisms of MLLMs are notably more vulnerable during interactions with humans.
L65: Even rudimentary jailbreak strategies such as role-playing, in-context learning, and gradual intent revelation via malicious intent decomposition can manipulate MLLMs into responding with harmful suggestions, misinformation, or content that may pose a risk of real-world harm [cite48†36 , cite49†13 , cite50†44 ]. As the responsibilities and applications of AI continue to expand, addressing the associated security issue has emerged as a critical imperative.
L66: Numerous studies have demonstrated that RLHF, especially when trained on carefully curated human preference answer pairs, significantly enhances the safety and reasoning capabilities of MLLMs [cite51†31 , cite52†43 , cite53†10 , cite54†38 ]. MM-DPO, a multi-modal alignment algorithm derived from MM-RLHF that leverages multi-dimensional human ranking of responses incorporates ethicality, faithfulness, and helpfulness as optimization targets throughout training process [cite55†40 ].
L67: Safe RLHF-V addressed the intrinsic tension between helpfulness and harmlessness, presenting a dedicated optimization scheme that seeks a principled balance between these objectives [cite56†14 ]. Despite their effectiveness on safety-oriented visual question-answering (VQA) tasks, our results on dialogue safety benchmarks indicate that these aligned models can still generate harmful content at non-trivial rates, as discussed in Section cite25†4.2 .
L68: This motivates a closer examination of MLLM safety alignment in conversational settings, where we identify three key challenges: (1) Insufficient multi-modal dialogue datasets for safety alignment. Existing open-source multi-modal safety datasets are primarily designed for single-turn VQA and do not adequately capture risks in conversations such as role-playing, multi-turn intent reconstruction, and conversational steering. (2) Requirement for extensive manual annotation.
L69: Existing datasets necessitate substantial manual annotation of preference data pairs. This cost becomes prohibitive for dialogue data due to longer contexts and larger sample volumes. (3) Challenges in algorithmic dialogue safety alignment. Although proposed algorithms have significantly improved the safety and helpfulness of VQA tasks, they remain less effective at mitigating risks in open-ended conversational settings, where models can still produce harmful content unintentionally.
L70: Consequently, an emerging safety issue of MLLMs that warrants increased attention appears:
L71: 
L72: How can we enhance MLLMs Safety in dialogue while minimizing data annotation costs?
L73: To bridge this gap and advance safety alignment for MLLMs in conversational situations, we propose InterSafe-V, a delicate dialogue safety training dataset containing 11,270 simulated daily conversations through interaction between models and 500 meticulously crafted domain-specific VQA pairs. Our data construction pipeline first decomposes malicious intents and subsequently constructs conversations through interactions between two models.
L74: Additionally, we employ Qwen-Image [cite57†34 ] to generate supplementary visual information when needed. Building on InterSafe-V and drawing inspiration from GRPO [cite58†30 ] and Safe RLHF-V [cite56†14 ], we further introduce AM^{3}Safety, a framework designed to optimize both safety and response quality at each conversational turn and throughout entire dialogues. This data efficient alignment approach minimizes the requirement for manual annotation.
L75: In summary, our contributions are as follows:
L76: 
L77:   * •
L78: 
L79: We propose a novel data construction pipeline that generates multi-modal dialogues through model-to-model interaction, eliminating the need for costly manual annotation. Using this pipeline, we release InterSafe-V, comprising 11,270 dialogues which include multiple images and 500 well-designed refusal VQA.
L80: 
L81:   * •
L82: We introduce AM^{3}Safety, a GRPO-based framework designed for dialogues safety alignment of MLLMs. This approach combines a cold-start refusal learning phase with GRPO. Crucially, we implement a turn-aware dual-objective reward function that dynamically weighs safety and helpfulness across the entire dialogue history, ensuring consistent safety behavior without compromising response quality.
L83: 
L84:   * •
L85: We evaluate our approach on Qwen2.5-VL-7B-Instruct and LLaVA-NeXT-7B across diverse benchmarks, demonstrating that our approach increases at least 8% in harmless dimension and over 13% in helpful dimension of MLLMs and achieve more than 10% decline in ASR on multi-turn multi-modal safety benchmarks.
L86: cite59†Image: Refer to caption Figure 1: We propose a three-step data construction pipeline. red-team queries sourced from existing multi-modal datasets are decomposed into multiple queries that are independently less harmful, while the combination of these queries retains the potential risk. Each query undergoes evaluation, with only those exceeding the threshold $\delta$ advancing to the subsequent step.
L87: These queries serve as prompts for simulated users during interactions with MLLMs and Qwen-image generates supplementary images based on descriptions as needed concurrently.
L88: ## 2 Related Work
L89: ### 2.1 Dialogue Safety
L90: With the rapid deployment of AI systems, dialogue agents based on LLMs or MLLMs have become widely used, making dialogue safety a central concern for both academia and industry [cite60†6 , cite61†11 , cite62†3 ]. To mitigate the potential misuse of AI, organizations such as OpenAI has established usage policies that highlight unsafe scenarios, including privacy violations, illegal activities and fraudulent behavior [cite63†26 ].
L91: Multiple studies have revealed potential risks associated with interacting with LLMs [cite64†15 , cite65†17 ]. Various safety benchmarks have been developed to assess text-only dialogue safety, such as CoSafe [cite66†37 ], SafeDialBench [cite67†4 ], and HH-RLHF [cite68†8 ].
L92: Beyond text-only settings, recent works highlight dialogue safety in MLLMs. Notably, benchmarks like SafeMT and MMDS [cite50†44 , cite49†13 ] have been introduced to evaluate the safety of multi-turn multi-modal dialogues. Furthermore, SafeMT and MIRAGE [cite48†36 ] have identified that the safety mechanisms of MLLMs can be easily circumvented through jailbreak strategies, such as storytelling and role-playing.
L93: Despite progress in evaluation, there is still a lack of open and scalable training dataset designed for multi-modal multi-turn dialogue safety alignment.
L94: ### 2.2 MLLMs Safety Alignment
L95: To mitigate safety risks of MLLMs, the community has proposed various alignment approaches aiming at enhancing safety alignment. Representative methods include RLHF-V, MM-RLHF, MMSafe-PO and SPA-VL [cite54†38 , cite55†40 , cite69†16 , cite70†41 ]. These methods employ Reinforcement Learning (RL) techniques, including Direct Preference Optimization (DPO) and Proximal Policy Optimization (PPO), to elevate the safety levels of MLLMs [cite71†27 , cite72†29 ].
L96: Prior work consistently observes a tension between helpfulness and safety during alignment [cite56†14 , cite69†16 , cite52†43 ]. To address this trade-off, existing methods design reward functions that incorporate safety dimensions while preserving response helpfulness. Nevertheless, these methodologies necessitate substantial amounts of human annotation. Moreover, even after alignment, MLLMs remain vulnerable to jailbreak strategies during conversational exchanges.
L97: ## 3 Methodology
L98: ### 3.1 InterSafe-V
L99: 
L100: Dataset  | Size  | # Avg. Turn  | # Avg. Image  | Data Construction
L101: BeaverTails-V  | 30,000  | 1  | 1  | Human
L102: RLHF-V  | 5,730  | 1  | 1  | Human
L103: MMSafe-PO  | 5667  | 1.97  | 1  | Entity Extraction
L104: MTSA  | 397  | 5  | 0  | Models Interaction
L105: InterSafe-V  | 11,770  | 4  | 1.53  | Models Interaction
L106: 
L107: Table 1: Dataset statistics
L108: We open-source a training dataset specifically designed for alignment of MLLMs in dialogue safety with 11,270 dialogues generated by the pipeline shown in Figure cite73†1 and 500 specifically designed VQA pairs. In contrast to other datasets presented in Table cite74†1 , our dataset places a greater emphasis on conversational contexts and incorporates multiple images within these dialogues.
L109: Furthermore, to more accurately simulate customer interactions, we employ model interactions for the construction of dialogues. Below are the details of the data construction.
L110: #### Refusal VQA Pairs
L111: To endow MLLMs with an initial capability to decline responses to malicious intent, we specifically design a cold-start dataset consisting of 500 samples, inspired by cite75†Wang et al. [33] . This dataset encompasses three primary categories of questions: 300 samples of general harmful inquiries randomly selected from SPA-VL [cite70†41 ], 100 health consultation questions derived from training subset of JailbreakV [cite76†24 ], and 100 financial domain questions sourced from the MME-Finance [cite77†7 ].
L112: For each category, we apply distinct annotation strategies. For general harmful inquiries, we utilize gpt-4o to generate analysis elucidating the potential harm associated with each question with prefix "I’m sorry" to clearly convey the refusal intent.
L113: In contrast, for questions pertaining to finance and health consultations, we manually standardize refusal responses, such as "I don’t have the necessary certifications; please consult with a professional expert." This ensures that the models are adept at refusing harmful intent and delivering related responses, particularly in specialized fields.
L114: #### Step 1: Red-Team Queries Decomposition
L115: 
L116: We first collect red-team queries from three high-quality multi-modal safety datasets: JailbreakV-28k [cite76†24 ] training subset, BeaverTails-V [cite56†14 ] training subset, and SPA-VL [cite70†41 ]. To enhance the diversity of our dataset, we aggregate 14 safety categories including pornography, violence, and digital crime. Concurrently, we filter out harmful prompts that exhibit high similarity to ensure the uniqueness of all queries.
L117: Compared to simple VQA formats, dialogues introduce a higher level of complexity due to the presence of more potential combinatorial risks and hidden harmful intents [cite48†36 ]. Our goal in designing dialogues is to ensure that each individual query does not contain overt harmful words or intents, allowing them to easily pass through the guard model. However, through the combination of queries, harmful intents can be pieced together to form problematic responses.
L118: To address this, we first employed the InternVL3-78B-Instruct [cite78†45 ] model to decompose harmful images and harmful query pairs into multiple independent queries. Once the queries were generated, we input them into a specially designed scoring system for quality and relevance assessment.
L119: The scoring objectives focused on three key areas: first, to determine whether the decomposed queries were relevant to their corresponding images; second, to evaluate their degree of association with the original questions; and third, to identify any direct harmful vocabulary present in the queries. If a query passed the quality assessment, we retained it; otherwise, we would regenerate the query. If a query consistently failed to meet the quality scoring filter, that data point would be removed entirely.
L120: #### Step 2: Dialogue Construction
L121: To more accurately emulate human interactions with MLLMs, we employ the InternVL3-78B [cite78†45 ] to simulate a safety expert engaged in provoking models to generate harmful content. This “expert” interacts with Kimi-VL [cite79†32 ] and Qwen2.5-VL-7B [cite80†9 ], creating a dynamic and realistic dialogue environment.
L122: Unlike traditional methods that often rely on static or simplistic interactions, our approach leverages decomposed queries as prompts for each turn, enhancing the complexity and authenticity of the dialogue. When necessary, the “expert” will provide supplementary image descriptions, while Qwen-Image [cite57†34 ], as an external module, will generate images based on these descriptions.
L123: Importantly, we regularize the user questions to ensure that images descriptions are not provided to the MLLMs, thereby allowing them to receive images directly in their visual format.
L124: #### Step 3: Data Cleaning
L125: We conduct a thorough examination of the raw data and identify that multiple generated images often exhibit high similarity within the same conversation. Furthermore, during dialogue interactions, there is probability that the models may gradually deviate from the intended risky topic. This can result in two significant issues: (1) diminished conversational coherence, and (2) elimination of the potential risks within the dialogue.
L126: To address these challenges, we employ InternVL3-78B to compare images within dialogues and filter out those that are highly similar. Additionally, to ensure that the dialogues maintained their potential harmfulness and associated risks, we evaluate the generated conversations, retaining only those that contained identifiable risks and harmful elements.
L127: ### 3.2 AM^{3}Safety
L128: 
L129: cite81†Image: Refer to caption Figure 2: AM^{3}Safety Training pipeline: Cold-start establishes refusal capabilities in the policy model, followed by GRPO-based training that optimizes for helpfulness while maintaining safety alignment.
L130: #### Refusal Template Learning
L131: Inspired by cite75†Wang et al. [33] demonstrating that safety of MLLMs can be significantly improved without labor-intensive collection of high-quality malicious data, we adopt a cold-start phase that mixes refusal responses to harmful questions with general queries. Specifically, we construct a dataset where harmful multi-modal queries (e.g., an image depicting dangerous content paired with a malicious question) are paired with refusal answers that provide clear reasoning for the rejection.
L132: We perform supervised fine-tuning (SFT) on the base model by minimizing the negative log-likelihood:
L133:  | $$\small\mathcal{L}_{\text{SFT}}(\theta)=-\frac{1}{N}\sum_{i=1}^{N}\log P_{\theta}(y_{i}|v_{i},x_{i})$$  |  | (1)
--------------------------------------------------------------------------------
When More Words Say Less: Decoupling Length and Specificity in Image Description Evaluation (https://arxiv.org/html/2601.04609v1)
citeturn26853view2 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04609v1","lineno":null}); Total lines: 333

