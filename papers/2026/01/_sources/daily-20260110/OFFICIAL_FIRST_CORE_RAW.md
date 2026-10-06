# Jan10 官方核心原文缓存

正文来源为本日实际打开官方公告；Anthropic核心L18–49/官方时间原HTMLpublishedOn见PRIMARY_META_RAW.json；OpenAI SB Energy核心L22–35。

Next-generation Constitutional Classifiers \ Anthropic (https://www.anthropic.com/research/next-generation-constitutional-classifiers)
citeturn26783view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://www.anthropic.com/research/next-generation-constitutional-classifiers","lineno":null}); Total lines: 69
L0: cite0†Skip to main content cite1†Skip to footer L1: 
L2:   * Research
L3:   * cite2†Policy L4:   * Commitments
L5:   * Learn
L6:   * cite3†News L7: 
L8: cite4†Try Claude†claude.ai L9: 
L10: Alignment
L11: # Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks
L12: 
L13: Jan 9, 2026
L14: 
L15: cite5†Read the paper†arxiv.org L16: 
L17: cite6†Image: Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks L18: Large language models remain vulnerable to jailbreaks—techniques that can circumvent safety guardrails and elicit harmful information. Over time, we’ve implemented a variety of protections that have made our models much less likely to assist with dangerous user queries—in particular relating to the production of chemical, biological, radiological, or nuclear weapons (CBRN). Nevertheless, no AI systems currently on the market have perfectly robust defenses.
L19: Last year, we described a new approach to defend against jailbreaks which we called “cite7†Constitutional Classifiers :” safeguards that monitor model inputs and outputs to detect and block potentially harmful content. The novel aspect of the approach was that the classifiers were trained on synthetic data generated from a "constitution,” which included natural language rules specifying what’s allowed and what isn’t.
L20: For example, Claude should help with college chemistry homework, but not assist in the synthesis of Schedule 1 chemicals.
L21: Constitutional Classifiers worked quite well. Compared to an unguarded model, the first generation of the classifiers reduced the jailbreak success rate from 86% to 4.4%—that is, they blocked 95% of attacks that might otherwise bypass Claude’s built-in safety training. We were particularly interested in whether the classifiers could prevent universal jailbreaks—consistent attack strategies that work across many queries—since these pose the greatest risk of enabling real-world harm.
L22: They came close: we ran a bug bounty program challenging people to break the system, in which one universal jailbreak was found.
L23: While effective, those classifiers came with tradeoffs: they increased compute costs by 23.7%, making the models more expensive to use, and also led to a 0.38% increase in refusal rates on harmless queries (that is, it made Claude somewhat more likely to refuse to answer perfectly benign questions, increasing frustration for the user).
L24: We’ve now developed the next generation, Constitutional Classifiers++, and described them in a cite5†new paper†arxiv.org . They improve on the previous approach, yielding a system that is even more robust, has a much lower refusal rate, and—at just ~1% additional compute cost—is dramatically cheaper to run.
L25: We iterated on many different approaches, ultimately landing on an ensemble system. The core innovation is a two-stage architecture: a probe that looks at Claude’s internal activations (and which is very cheap to run) screens all traffic. If it identifies a suspicious exchange, it escalates it to a more powerful classifier, which, unlike our previous system, screens both sides of a conversation (rather than just outputs), making it better able to recognize jailbreaking attempts.
L26: This more robust system has the lowest successful attack rate of any approach we’ve ever tested, with no universal jailbreak yet discovered.
L27: ## Remaining vulnerabilities
L28: 
L29: As models have grown to be more capable and robust to attacks, jailbreaks have also evolved to exploit previously unidentified vulnerabilities. Our Constitutional Classifiers approach demonstrated promising robustness against universal jailbreaks. But after conducting additional adversarial testing, we found that our classifiers remained vulnerable to two broad categories of attacks:
L30:   * Reconstruction attacks break up harmful information into segments that appear benign, then reassemble them. For example, an attacker might embed a harmful query as a series of functions scattered throughout a codebase, then instruct the model to extract and respond to the hidden message.
L31:   * Output obfuscation attacks prompt models to disguise their outputs in ways that appear harmless if a classifier is only looking at a model’s output. For example, during adversarial testing, attackers successfully instructed models to substitute possibly dangerous chemical names with innocuous alternatives (like referring to reagents as "food flavorings") or used metaphors and riddles in which harmful concepts are mapped onto anodyne concepts.
L32: cite8†Image L33: Importantly, these sorts of attacks also degrade model capabilities—sometimes substantially. On cite9†GPQA Diamond†arxiv.org , a benchmark which measures PhD-level concepts in biology, chemistry, and physics, model performance dropped from 74% to as low as 32% when some jailbreaking approaches were used.
L34: But performance varied depending on the type of jailbreak, and this variability is concerning—it suggests attackers can likely develop previously unidentified strategies which could achieve their goals while preserving even more of the model's capabilities.
L35: ## New approaches
L36: 
L37: In designing a new system, we tested and ultimately combined a variety of techniques into what we describe as an ensemble defense.
L38: One insight was that part of the original system’s vulnerability stemmed from the way it evaluated model inputs and outputs separately when the jailbreaking techniques involved linking them in surreptitious ways. An output that appears benign in isolation (“how to use food flavorings”) is more easily identified as harmful when paired with its input (in a jailbreak where “food flavorings” is used as code for chemical reagents).
L39: To address this, we replaced the separate input and output classifiers with a single “exchange” classifier, which monitors outputs in the context of their inputs. With the ability to see both sides of the conversation, the classifiers are better able to recognize harmful outputs. In human red teaming, the exchange classifier cut successful jailbreaking attempts by more than half. Unfortunately, this came at the cost of a 50% increase in compute.
L40: To reduce these costs while maintaining robustness, we implemented what we call a "cascade architecture." Our solution was a two-stage system. First, a lightweight, less costly first-stage classifier screens all exchanges. Only those it flags proceed to a more accurate (and more computationally expensive) second-stage classifier.
L41: This had two benefits. First, because flagged exchanges are escalated to the more powerful model, rather than refused, the first-stage classifier can afford a higher false-positive rate and not frustrate the user with refusals. Where the previous system may have declined to respond to a benign request, the new system, in effect, escalates it to a manager. Second, because the lightweight classifier handles the vast majority of conversations, the two-stage system is much cheaper to run.
L42: Still, we wanted to push efficiency even further. We did so by developing internal probe classifiers—a technique that builds on our interpretability research—that reuse computations already available in the model’s neural network.
L43: When a model generates text, it produces internal states at each step that capture its understanding of the input and output so far. When Claude processes a dubious-seeming request, patterns fire in its internal activations that reflect something along the lines of "this seems harmful,” even before it has formulated a response or made a conscious decision about what to do. Normally, these activations are intermediate computations—used, then discarded.
L44: We found ways to reliably probe whether these internal states suggest harmful content, getting more information—think of it like Claude’s gut intuitions—almost for free.
L45: In addition to being computationally inexpensive, these internal probes add several layers of protection. First, they’re harder to fool. An attacker can craft inputs that trick Claude's final output, but it's much harder to manipulate its internal representations. Second, we found in testing that they’re actually complementary to our external classifiers: the probe appears to see things the external classifier can’t, and vice versa.
L46: ## Conclusions and further research
L47: Our final production-grade system combines these techniques: a linear probe screens all traffic, escalating flagged exchanges to a probe-classifier ensemble for final judgment. This ensemble further improves performance: in one month of deployment on Claude Sonnet 4.5 traffic, the system achieved a refusal rate of 0.05% on harmless queries—an 87% drop from the original classifiers system. In total, it adds roughly 1% compute overhead if applied to Claude Opus 4.0 traffic.
L48: It’s also substantially more robust. We conducted over 1,700 cumulative hours of red-teaming across 198,000 attempts. We discovered only one high-risk vulnerability, which corresponds to a detection rate of 0.005 per thousand queries—the lowest of any of the techniques we have evaluated to date. And crucially, no red-teamer has yet discovered a universal jailbreak.
L49: There’s even more we could do in the future to improve our system. Several research directions show promise, including integrating classifier signals directly into how models generate responses, and training models themselves to better resist obfuscation. Automated red-teaming could also help generate better training data, and creating targeted examples could help the classifiers learn exactly where the boundary between allowed and disallowed content lies, increasing their accuracy even further.
L50: For more details about the Constitutional Classifiers++ method, see the cite5†full paper.†arxiv.org L51: ## Related content
L52: 
L53: ### Claude-shaped science
L54: 
L55: Guest author Prof. Matthew Schwartz describes what happened when he stopped fighting Claude and allowed Claude to find “Claude-shaped” problems: ones best suited to the capabilities of the current generation of LLM tools. This led him to build BootLoops, a toolkit for exact calculations in quantitative science, which he has been applying across scientific fields alongside experts.
L56: 
L57: cite10†Read more L58: ### What work can robots do?
L59: 
L60: We built an index of how well today’s robots can perform US job tasks. Robots can already do three-quarters of physical tasks, mostly in limited settings, but are cost-competitive for just 0.3% of them.
L61: 
L62: cite11†Read more L63: 
L64: ### What do you want from AI?
L65: 
L66: We’re launching a new study using Anthropic Interviewer to learn from your experiences with AI, and we invite you to participate.
L67: 
L68: cite12†Read more --------------------------------------------------------------------------------
OpenAI and SoftBank Group partner with SB Energy | OpenAI (https://openai.com/index/stargate-sb-energy-partnership/)
citeturn26783view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://openai.com/index/stargate-sb-energy-partnership/","lineno":null}); Total lines: 134
L0: cite0†Skip to main content L1: 
L2:   * [Button: Research]
L3:   * [Button: Products]
L4:   * [Button: Business]
L5:   * [Button: Developers]
L6:   * [Button: Company]
L7:   * cite1†Foundation(opens in a new window)†openaifoundation.org L8: 
L9: cite2†Try ChatGPT(opens in a new window)†chatgpt.com [Button: Login]
L10: 
L11: OpenAI
L12: 
L13: January 9, 2026
L14: 
L15: cite3†Global Affairs L16: # OpenAI and SoftBank Group partner with SB Energy
L17: 
L18: Loading…
L19: 
L20: Share
L21: 
L22:   * SoftBank Group and OpenAI invest $1 billion in SB Energy to support its growth as a leading development and execution partner for data center campuses
L23: 
L24:   * OpenAI signs 1.2 GW data center lease for initial data center buildout
L25: 
L26:   * SB Energy will become a major customer of OpenAI, leveraging its APIs and deploying ChatGPT for its employees
L27:   * SB Energy additionally secured $800 million of Redeemable Preferred Equity from Ares to further support the company’s growth
L28: Redwood City, CA, Jan. 9, 2026—cite4†SB Energy⁠(opens in a new window)†sbenergy.com , a SoftBank Group company, announced today a strategic partnership with OpenAI as part of cite5†Stargate⁠(opens in a new window)†group.softbank , marking a significant step forward in the build out of next-generation artificial intelligence (AI) and energy infrastructure in the United States. The investment builds on the $500 billion Stargate commitment announced in January at the White House.
L29: To support the partnership and as demand for AI compute accelerates, OpenAI and SoftBank Group are each investing $500 million into SB Energy. OpenAI has also selected SBE to build and operate its cite6†previously-announced 1.2 GW data center site in Milam County. The equity funding supports SB Energy’s growth as a leading development and execution partner for data center campuses and associated energy infrastructure.
L30: SB Energy is currently developing several multi-gigawatt data center campuses, with initial facilities under construction and expected to enter service starting in 2026.
L31: OpenAI co-founder and President Greg Brockman said, “Partnering with SB Energy brings together their strength in data center infrastructure and energy development and OpenAI’s deep domain expertise in data center engineering. The result is a fast, reliable way to scale compute through large, highly optimized AI data centers.”
L32: SB Energy co-CEO Rich Hossfeld said, “SB Energy’s strategic partnership with OpenAI accelerates our delivery of advanced AI data center campuses and associated energy infrastructure at the scale required to advance Stargate and secure America’s AI future. We are grateful for our longstanding sponsor SoftBank Group and new partner OpenAI for their investment in our platform, our team, and our long-term vision.”
L33: As part of this transaction, OpenAI, SoftBank Group, and SB Energy have also formed a non-exclusive preferred partnership to develop a new model for data center builds that brings together OpenAI’s first-party data center design with SB Energy’s proven expertise in speed, cost discipline, and integrated energy delivery to deliver purpose-built AI infrastructure at scale.
L34: With each project, SB Energy and OpenAI will invest in communities through well-paying jobs, workforce development, and grid modernization to deliver durable economic growth for partner communities.
L35: The Milam County Data Center will create thousands of construction jobs. OpenAI and SB Energy have designed the data center to minimize water usage, and plan to build new generation to support the Milam County Data Center’s energy needs and protect Texas ratepayers.
L36: 
L37:   * cite7†Partnerships L38:   * cite8†2026 L39: ## Author
L40: 
L41: OpenAI
L42: ## Keep reading
L43: 
L44: cite9†View all L45: 
L46: cite10†Helping small businesses put AI to work Global AffairsSep 30, 2026 L47: 
L48: cite11†OpenAI extends cyber access to Ukraine for civilian defense Global AffairsSep 23, 2026 L49: 
L50: cite12†Sam Altman’s remarks at the United Nations Security Council Global AffairsSep 23, 2026 L51: 
L52: Research
L53: 
L54:   * cite13†Research Index L55:   * cite14†Research Overview L56:   * cite15†Economic Research L57: 
L58: Latest Advancements
L59: 
L60:   * cite16†GPT-6.1 Sol L61:   * cite17†GPT-6 Astra L62:   * cite18†GPT-5.6 L63:   * cite19†GPT-5.5 L64: 
L65: Safety
L66:   * cite20†Safety Approach L67:   * cite21†Deployment Safety(opens in a new window)†deploymentsafety.openai.com L68:   * cite22†Security & Privacy L69:   * cite23†Trust & Transparency L70: 
L71: Products
L72:   * cite2†ChatGPT(opens in a new window)†chatgpt.com L73:   * cite24†ChatGPT Business(opens in a new window)†chatgpt.com L74:   * cite25†ChatGPT Enterprise(opens in a new window)†chatgpt.com L75:   * cite26†ChatGPT for Education(opens in a new window)†chatgpt.com L76:   * cite27†Codex†chatgpt.com L77:   * cite28†Dots(opens in a new window)†chatgpt.com L78:   * cite29†Release Notes L79: 
L80: API Platform
L81: 
L82:   * cite30†Overview L83:   * cite31†API Log In(opens in a new window)†platform.openai.com L84:   * cite32†Docs(opens in a new window)†developers.openai.com L85: 
L86: Business
L87:   * cite33†Overview L88:   * cite34†Solutions L89:   * cite35†Resources L90:   * cite36†Plugins L91:   * cite37†Customer Stories L92:   * cite38†Partner Network L93:   * cite39†Contact Sales L94: 
L95: Developers
L96: 
L97:   * cite40†Apps SDK(opens in a new window)†developers.openai.com L98:   * cite41†Open Models L99:   * cite42†Docs(opens in a new window)†developers.openai.com L100:   * cite43†Resources(opens in a new window)†developers.openai.com L101:   * cite44†Developer Forum(opens in a new window)†community.openai.com L102: 
L103: Company
L104:   * cite45†About Us L105:   * cite46†Our Charter L106:   * cite47†Careers L107:   * cite9†News L108: 
L109: Support
L110: 
L111:   * cite48†Help Center(opens in a new window)†help.openai.com L112: 
L113: More
L114: 
L115:   * cite49†Stories L116:   * cite50†Academy L117:   * cite51†Supply Co. L118:   * cite52†Livestreams L119:   * cite53†Podcast L120:   * cite54†RSS L121: 
L122: Terms & Policies
L123: 
L124:   * cite55†Terms of Use L125:   * cite56†Privacy Policy L126:   * cite57†Other Policies L127: cite58†(opens in a new window)†x.com cite59†(opens in a new window)†www.youtube.com cite60†(opens in a new window)†www.linkedin.com cite61†(opens in a new window)†github.com cite62†(opens in a new window)†www.instagram.com cite63†(opens in a new window)†www.tiktok.com cite64†(opens in a new window)†discord.gg L128: 
L129: OpenAI © 2015–2026 Your privacy choices
L130: 
L131: English United States
L132: 
L133: [Input: Search]

