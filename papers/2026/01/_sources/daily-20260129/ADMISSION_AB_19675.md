# 独立准入校准：2601.19675v1

原完整题摘记录：abweb5_RECOVERY.md。仅用于定点准入，不代表日期或必要证据审阅完成。

[2601.19675v1] LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/abs/2601.19675v1)
citeturn28076view1 [wordlim: 200] Crawled: 2 weeks ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.19675v1","lineno":null}); Total lines: 164
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Machine Learning
L7: 
L8: [Submitted on 27 Jan 2026]
L9: # Title:LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation
L10: 
L11: Authors:cite5†Hongyaoxing Gu , cite6†Lijuan Hu , cite7†Liye Yu , cite8†Haowei Li , cite9†Fangfang Liu L12: 
L13: View a PDF of the paper titled LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation, by Hongyaoxing Gu and 4 other authors
L14: 
L15: cite10†View PDF cite11†HTML (experimental) L16: > Abstract:Post-training quantization (PTQ) enables effective model compression while preserving relatively high accuracy. Current weight-only PTQ methods primarily focus on the challenging sub-3-bit regime, where approaches often suffer significant accuracy degradation, typically requiring fine-tuning to achieve competitive performance. In this work, we revisit the fundamental characteristics of weight quantization and analyze the challenges in quantizing the residual matrix under low-rank approximation.
L17: We propose LoPRo, a novel fine-tuning-free PTQ algorithm that enhances residual matrix quantization by applying block-wise permutation and Walsh-Hadamard transformations to rotate columns of similar importance, while explicitly preserving the quantization accuracy of the most salient column blocks. Furthermore, we introduce a mixed-precision fast low-rank decomposition based on rank-1 sketch (R1SVD) to further minimize quantization costs.
L18: Experiments demonstrate that LoPRo outperforms existing fine-tuning-free PTQ methods at both 2-bit and 3-bit quantization, achieving accuracy comparable to fine-tuning baselines. Specifically, LoPRo achieves state-of-the-art quantization accuracy on LLaMA-2 and LLaMA-3 series models while delivering up to a 4$\times$ speedup. In the MoE model Mixtral-8x7B, LoPRo completes quantization within 2.5 hours, simultaneously reducing perplexity by 0.4$\downarrow$ and improving accuracy by 8\%$\uparrow$.
L19: Moreover, compared to other low-rank quantization methods, LoPRo achieves superior accuracy with a significantly lower rank, while maintaining high inference efficiency and minimal additional latency.
L20: Subjects:  | Machine Learning (cs.LG)
L21: Cite as:  | cite12†arXiv:2601.19675 [cs.LG]
L22:    | (or cite13†arXiv:2601.19675v1 [cs.LG] for this version)
L23:    | cite14†https://doi.org/10.48550/arXiv.2601.19675†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Hongyaoxing Gu [cite15†view email ]
L27: [v1] Tue, 27 Jan 2026 14:56:04 UTC (12,236 KB)
L28: 
L29: Full-text links:
L30: 
L31: ## Access Paper:
L32: 
L33: View a PDF of the paper titled LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation, by Hongyaoxing Gu and 4 other authors
L34: 
L35:   * cite10†View PDF L36:   * cite11†HTML (experimental) L37:   * cite16†TeX Source L38: 
L39: cite17†view license†creativecommons.org L40: ### Current browse context:
L41: 
L42: cs.LG
L43: 
L44: cite18†< prev |   cite19†next > L45: 
L46: cite20†new | cite21†recent | cite22†2026-01 L47: 
L48: Change to browse by:
L49: 
L50: cite23†cs L51: 
L52: ### References & Citations
L53: 
L54:   * cite24†NASA ADS†ui.adsabs.harvard.edu L55:   * cite25†Google Scholar†scholar.google.com L56:   * cite26†Semantic Scholar†api.semanticscholar.org L57: 
L58: [Button: export BibTeX citation] Loading...
L59: 
L60: ## BibTeX formatted citation
L61: 
L62: [Button: ×]
L63: 
L64: loading...
L65: 
L66: Data provided by:
L67: 
L68: ### Bookmark
L69: 
L70: [Input] Bibliographic Tools
L71: # Bibliographic and Citation Tools
L72: 
L73: [Input] Bibliographic Explorer Toggle
L74: 
L75: Bibliographic Explorer (cite27†What is the Explorer?†info.arxiv.org )
L76: 
L77: [Input] Connected Papers Toggle
L78: 
L79: Connected Papers (cite28†What is Connected Papers?†www.connectedpapers.com )
L80: 
L81: [Input] Litmaps Toggle
L82: 
L83: Litmaps (cite29†What is Litmaps?†www.litmaps.co )
L84: 
L85: [Input] scite.ai Toggle
L86: 
L87: scite Smart Citations (cite30†What are Smart Citations?†www.scite.ai )
L88: 
L89: [Input] Code, Data, Media
L90: # Code, Data and Media Associated with this Article
L91: 
L92: [Input] alphaXiv Toggle
L93: 
L94: alphaXiv (cite31†What is alphaXiv?†alphaxiv.org )
L95: 
L96: [Input] Links to Code Toggle
L97: 
L98: CatalyzeX Code Finder for Papers (cite32†What is CatalyzeX?†www.catalyzex.com )
L99: 
L100: [Input] DagsHub Toggle
L101: 
L102: DagsHub (cite33†What is DagsHub?†dagshub.com )
L103: 
L104: [Input] GotitPub Toggle
L105: 
L106: Gotit.pub (cite34†What is GotitPub?†gotit.pub )
L107: 
L108: [Input] Huggingface Toggle
L109: 
L110: Hugging Face (cite35†What is Huggingface?†huggingface.co )
L111: 
L112: [Input] ScienceCast Toggle
L113: ScienceCast (cite36†What is ScienceCast?†sciencecast.org )
L114: 
L115: [Input] Demos
L116: # Demos
L117: 
L118: [Input] Replicate Toggle
L119: 
L120: Replicate (cite37†What is Replicate?†replicate.com )
L121: 
L122: [Input] Spaces Toggle
L123: 
L124: Hugging Face Spaces (cite38†What is Spaces?†huggingface.co )
L125: 
L126: [Input] Spaces Toggle
L127: 
L128: TXYZ.AI (cite39†What is TXYZ.AI?†txyz.ai )
L129: 
L130: [Input] Related Papers
L131: # Recommenders and Search Tools
L132: 
L133: [Input] Link to Influence Flower
L134: 
L135: Influence Flower (cite40†What are Influence Flowers?†influencemap.cmlab.dev )
L136: 
L137: [Input] Core recommender toggle
L138: 
L139: CORE Recommender (cite41†What is CORE?†core.ac.uk )
L140: 
L141: [Input] IArxiv recommender toggle
L142: 
L143: IArxiv Recommender (cite42†What is IArxiv?†iarxiv.org )
L144: 
L145:   * Author
L146:   * Venue
L147:   * Institution
L148:   * Topic
L149: 
L150: [Input] About arXivLabs
L151: # arXivLabs: experimental projects with community collaborators
L152: 
L153: arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
L154: 
L155: Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
L156: Have an idea for a project that will add value for arXiv's community? cite43†Learn more about arXivLabs†info.arxiv.org .
L157: 
L158: cite44†Which authors of this paper are endorsers? | Disable MathJax (cite45†What is MathJax?†info.arxiv.org )
L159: 
L160: We gratefully acknowledge support from our major funders, cite46†member institutions†info.arxiv.org , , and all contributors.
L161: cite47†About†info.arxiv.org · cite48†Help†info.arxiv.org · cite49†Contact†info.arxiv.org · cite50†Subscribe†info.arxiv.org · cite51†Copyright†info.arxiv.org · cite52†Privacy†info.arxiv.org · cite53†Accessibility†info.arxiv.org · cite54†Operational Status (opens in new tab)†status.arxiv.org L162: 
L163: Major funding support from
--------------------------------------------------------------------------------

