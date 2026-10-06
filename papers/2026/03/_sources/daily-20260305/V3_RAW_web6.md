Extending single-minus amplitudes to gravitons | OpenAI (https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/)
citeturn24734search0 [wordlim: 200] Published: 7 months ago; Crawled: 2 weeks ago; The paper, “Single-minus graviton tree amplitudes are nonzero,” is authored by Alfredo Guevara (Institute for Advanced Study), Alexandru Lupsasca (Vanderbilt University and OpenAI), David Skinner (University of Cambridge), Andrew Strominger (Harvard University), and Kevin Weil (OpenAI) on behalf of OpenAI. ... The new preprint shows how, in the simplest possible context, this symmetry acts on gravitons, the elementary quantum bits of the gravitational field.

March 4, 2026

ResearchPublication

# Extending single-minus amplitudes to gravitons

Researchers used GPT‑5.2 Pro to help find a new mathematical result describing how particles can interact in quantum gravity.

Read the preprint(opens in a new window)

We’ve published a new preprint studying scattering amplitudes in quantum gravity, extending recent results obtained for gluons to the gravitational setting. The work shows that a class of graviton interactions long assumed to vanish can in fact arise under well-defined kinematic conditions. The preprint is available here⁠(opens in a new window). We welcome feedback from the community.

The paper, “Single-minus graviton tree amplitudes are nonzero,” is authored by Alfredo Guevara (Institute for Advanced Study), Alexandru Lupsasca (Vanderbilt University and OpenAI), David Skinner (University of Cambridge), Andrew Strominger (Harvard University), and Kevin Weil (OpenAI) on behalf of OpenAI.

## Understanding single-minus amplitudes in gravity

Scattering amplitudes are mathematical quantities physicists use to calculate the probability that particles interact in particular ways. Rather than tracking every intermediate step of a collision through many diagrams, amplitudes encode the final observable outcomes in a compact form. Over the past several decades, researchers have found that amplitudes often display unexpected simplicity, revealing hidden mathematical structure not obvious from traditional calculations.

The new preprint studies gravitons, quantum particles associated with gravity in quantum field theory. In particular, the authors analyze a configuration known as a single-minus amplitude, meaning that one particle has negative helicity while the remaining particles have positive helicity. Helicity describes the orientation of a particle’s spin relative to its direction of motion and plays an important role in determining how interactions occur. Standard textbook arguments suggest that these amplitudes should vanish at the simplest level of approximation, called tree level, where only the most direct interaction diagrams are considered and quantum loop effects are ignored.

The preprint shows that this conclusion depends on assuming generic particle motion. When particle momenta satisfy a special alignment known as the half-collinear regime, the usual argument no longer applies. In this regime, the amplitudes do not vanish but instead exist as well-defined mathematical distributions supported on a restricted region of momentum space. The authors derive explicit formulas describing these interactions and show that they follow from symmetry principles and recursion relations that build complex interactions from simpler ones.

This result is a small step towards the solution of the central problem of reconciling quantum mechanics with Einstein’s theory of general relativity. The single minus amplitudes realize an infinite dimensional “w-(1+∞)” symmetry. This powerful symmetry was discovered by Penrose a half century ago in the context of classical gravity and is expected by many to play a central role in quantizing the gravitational field. The new preprint shows how, in the simplest possible context, this symmetry acts on gravitons, the elementary quantum bits of the gravitational field.

## Methodology and verification

Although gravity and gauge theory share deep conceptual relationships, their calculations differ substantially in practice. The earlier gluon result demonstrated that a previously neglected helicity configuration could produce nonzero amplitudes under special conditions. After that work was completed, the gluon paper was provided to GPT‑5.2 Pro as context. Using it as a reference point, the model was asked to construct the corresponding amplitudes in quantum gravity, an extension which would have taken human authors considerable time to derive. GPT‑5.2 Pro not only solved this problem using a beautiful and surprising technique (the directed matrix-tree theorem), it also produced an excellent preliminary draft of the paper. You can find a transcript of this initial exchange here⁠(opens in a new window).

The derivation combines several established tools in amplitude theory, including recursion relations that iteratively construct many-particle interactions from smaller building blocks and symmetry constraints that restrict the allowed form of the result. The final formulas were verified analytically and checked for consistency with known physical limits. After further interaction with GPT‑5.2 Pro, the amplitudes were also found to be consistent with an infinite-dimensional symmetry first studied in connection with gravity by Roger Penrose.

An important observation emerging from this and related projects concerns the pace of discovery. For this project, much of the time elapsed from the previous gluon result was spent confirming derivations, checking consistency, and preparing formal write-ups rather than generating initial conjectures. This sequence of results represents a significant shift, with verification and exposition representing the dominant share of effort.

The transition from gluons to gravitons illustrates how mathematical insight can transfer across neighboring areas of theoretical physics. While the two theories describe different fundamental forces, they share structural features that allow ideas developed in one setting to inform the other. Providing the gluon result as an anchor enabled exploration of this connection, leading to a gravitational construction that was subsequently proven using standard analytic methods.

## What’s next

Further extensions of these results are currently under investigation. Together with the earlier gluon work, this preprint contributes to an ongoing effort to understand how AI-assisted reasoning can participate in theoretical research while maintaining conventional standards of mathematical verification and scientific rigor.

## Author

Alex Lupsasca--------------------------------------------------------------------------------
GPT-5.2 derives a new result in theoretical physics | OpenAI (https://openai.com/index/new-result-theoretical-physics/)
citeturn24734search1 [wordlim: 200] Published: 7 months ago; Crawled: 2 weeks ago; The preprint, titled “Single-minus gluon tree amplitudes are nonzero,” is authored by Alfredo Guevara (Institute for Advanced Study), Alex Lupsasca (Vanderbilt University and OpenAI), David Skinner (University of Cambridge), and Andrew Strominger (Harvard University), and Kevin Weil (OpenAI) on behalf of OpenAI. ... With the help of GPT‑5.2, these amplitudes have already been extended from gluons to gravitons, and other generalizations are also on their way.

The preprint shows that this conclusion is too strong. The standard argument assumes generic particle momenta, meaning the directions and energies are not in any special alignment. We identify a specific and precisely defined slice of momentum space where that reasoning no longer applies, known as the half-collinear regime. Half-collinear here means the gluon momenta obey a special alignment condition that is not typical, but is mathematically well-defined and consistent. On this slice, the amplitude does not vanish, and we compute it in a special kinematic regime. This result opens the door to many new questions that will be the subject of subsequent investigations. Important extensions include the computation of the analogous amplitudes for gravitons (the particles that mediate the gravitational force).

A central aspect of the work concerns methodology. The final formula, Eq. (39) in the preprint, was first conjectured by GPT‑5.2 Pro. The human authors worked out the amplitudes for integer $ n $n up to $ n=6 $n=6 by hand, obtaining very complicated expressions shown in Eqs. (29)--(32), which correspond to a “Feynman diagram expansion” whose complexity grows superexponentially in n. GPT‑5.2 Pro was able to greatly reduce the complexity of these expressions, providing the much simpler forms in Eqs. (35)--(38). From these base cases, it was then able to spot a pattern and posit a formula valid for all $ n $n.

An internal scaffolded version of GPT‑5.2 then spent roughly 12 hours reasoning through the problem, coming up with the same formula and producing a formal proof of its validity. The equation was subsequently verified analytically to solve the Berends-Giele recursion relation, a standard step-by-step method for building multi-particle tree amplitudes from smaller building blocks. It was also checked against the soft theorem, which constrains how amplitudes behave when a particle becomes soft.

With the help of GPT‑5.2, these amplitudes have already been extended from gluons to gravitons, and other generalizations are also on their way. These AI-assisted results, and many others, will be reported on elsewhere.

“The physics of these highly degenerate scattering processes has been something I’ve been curious about since I first ran into them about fifteen years ago, so it is exciting to see the strikingly simple expressions in this paper.
--------------------------------------------------------------------------------
Qwen (https://qwen.ai/blog?email_hash=23463b99b62a72f26ed677cc556c44e8&id=qwen3.5)
citeturn24734search2 [wordlim: 200] Published: 7 months ago; Crawled: 2 months ago; The corresponding comparative scores were corrected on March 15, 2026. ... Under the 32k/256k context length, the decoding throughput of Qwen3.5-397B-A17B is 8.6x/19.0x that of Qwen3-Max, and the performance is comparable.

# Qwen3.5: Towards Native Multimodal Agents

2026/02/15 · 45 minute · 8987 words · QwenTeam丨Translations:简体中文

Image: Qwen3 Main Image

QWEN CHATGitHubHugging FaceModelScopeDISCORD

We are delighted to announce the official release of Qwen3.5, introducing the open-weight of the first model in the Qwen3.5 series, namely Qwen3.5-397B-A17B. As a native vision-language model, Qwen3.5-397B-A17B demonstrates outstanding results across a full range of benchmark evaluations, including reasoning, coding, agent capabilities, and multimodal understanding, empowering developers and enterprises to achieve significantly greater productivity. Built on an innovative hybrid architecture that fuses linear attention (via Gated Delta Networks) with a sparse mixture-of-experts, the model attains remarkable inference efficiency: although it comprises 397 billion total parameters, just 17 billion are activated per forward pass, optimizing both speed and cost without sacrificing capability. We have also expanded our language and dialect support from 119 to 201, providing broader accessibility and enhanced support to users around the world.

  * Qwen3.5-Plus is the hosted model available via Alibaba Cloud Model Studio, featuring:
    * a 1M context window by default
    * official built-in tools and adaptive tool use
Image

## Performance#

Below we present the comprehensive evaluation of our models against frontier models in a wide range of evaluation tasks, covering different tasks and modalities.

### Language#

 | GPT5.2  | Claude 4.5 Opus  | Gemini-3 Pro  | Qwen3-Max-Thinking  | K2.5-1T-A32B  | Qwen3.5-397B-A17B
--- | --- | --- | --- | --- | --- | ---
Knowledge
MMLU-Pro  | 87.4  | 89.5  | 89.8  | 85.7  | 87.1  | 87.8
* MathVision：our model’s score is evaluated using a fixed prompt, e.g., “Please reason step by step, and put your final answer within \boxed{}.” For other models, we report the higher score between runs with and without the \boxed{} formatting.
* BabyVision: our model’s score is reported with CI (Code Interpreter) enabled; without CI, the result is 43.3.
* V*: our model’s score is reported with CI (Code Interpreter) enabled; without CI, the result is 91.1.
* Empty cells (--) indicate scores not yet available or not applicable.
* Upon review, we found inconsistencies in the evaluation setup of the historical version Qwen3-VL-235B-A22B on SLAKE and PMC-VQA. The corresponding comparative scores were corrected on March 15, 2026.

Compared to the Qwen3 series, the post-training performance gains in Qwen3.5 primarily stem from our extensive scaling of virtually all RL tasks and environments we could conceive. Our approach placed strong emphasis on increasing the difficulty and generalizability of RL environments, rather than optimizing for specific metrics or narrow categories of queries. Below, we illustrate the improvements in general agent capabilities resulting from this RL environment scaling. The overall performance is calculated by averaging the ranking of each model on the following benchmarks: BFCL-V4, VITA-Bench, DeepPlanning, Tool-Decathlon, and MCP-Mark. Additional scaling results across a broader range of tasks will be detailed in our upcoming technical report.

Image

--------------------------------------------------------------------------------
Coding agents in the social sciences \ Anthropic (https://www.anthropic.com/research/coding-agents-social-sciences?xs=1)
citeturn24734search3 [wordlim: 200] Published: 4 months ago; Crawled: last week;   * We present results from a survey of 1,260 social scientists about AI and coding agent use, fielded in February and March 2026. ...      url = {https://www.anthropic.com/research/coding-agents-social-sciences},

Economics

# Coding agents in the social sciences

May 27, 2026

## Summary

  * We present results from a survey of 1,260 social scientists about AI and coding agent use, fielded in February and March 2026.
  * The vast majority of respondents (81%) have tried using AI chatbots in research, particularly for writing code and editing prose. But only 20% have adopted coding agents—tools like Claude Code that autonomously write and execute analysis code—into their work.
  * There are sharp disparities in use of coding agents. Twice as many researchers with typically male names use coding agents as those with female names. Researchers at top universities are 40% more likely than others to use coding agents.
  * Users of coding agents post more working papers and grant proposals than others in the same discipline and career stage, but this could reflect pre-existing differences among early adopters.
  * Researchers are more optimistic about AI helping write publishable papers than about the effects of AI on the social sciences as a whole.

## How are AI coding agents changing how we study the economy and society?

The human sciences are shifting: for the first time, core research tasks can be handed off to machines. AI chatbots increasingly contribute to scientific research, including in the most prestigious publications and in the social sciences. This has spurred optimism that AI could boost research productivity—while also stoking fears about overloaded peer review and a deluge of academic AI slop.

But while turn-taking AI chatbots have primarily been used for writing assistance, coding agents could restructure social science research more radically. Agentic coding platforms like Claude Code and Codex can take a research idea and a dataset, write and run an analysis, interpret the output, and iterate autonomously. What had been irreducibly human steps in empirical research can, for the first time, be automated. At the extreme, researchers have built multi-agent pipelines to automate computer science research and autonomously execute social science research ideas.

These tools could accelerate science and make it more daring: fast research execution should mean cheap and plentiful discovery. They could also amplify disparities in research resources and exacerbate congestion in the scholarly record. More deeply, as AI handles a broadening swath of research tasks, its distinctive analytical choices could stamp our collective understanding of our economy, our society, and ourselves.

In this post, we offer a first look, drawing on a survey of 1,260 quantitative social scientists fielded in early 2026. The survey is the baseline wave of a larger ongoing study of how coding agents affect research productivity, including a randomized experiment providing researchers with access to Claude Code. We will publish results from this experiment in the future. For now, we report what the baseline survey reveals about who is using these tools and for what; how output differs between users and non-users; and what researchers expect about the implications of growing adoption.

## A new survey on AI coding agent use among quantitative social scientists

We fielded the survey in late February and March 2026, targeting active quantitative social scientists. This was not a representative sample—respondents were recruited for a study that offered access to Claude Max accounts, so selection into the sample could tilt toward researchers curious about AI tools. However, the respondents were fairly similar to an earlier sample that received a more generic invitation (see Table A2 in the Appendix).

Respondents were evenly split between economics, political science and sociology, each around a fifth of the sample, with management sciences and psychology close behind (see Table A1). We also received a smaller number of responses from public health, education and communications researchers. Roughly 40% were full or associate professors, 25% were assistant professors, and about 30% were doctoral students.

## Coding agents haven't reached most social scientists

We measured overall AI use in two ways. Field impact is: “Do you think AI will make the social sciences worse or better," with the slider labeled “Worse to better.” Number of AI use cases adopted sums the categories listed in Figure 4.

The survey is drawing from people who are interested in trying these tools out, so it should not be surprising to see some optimism about productivity. But even among these optimists, there is a real gap between views about AI helping narrowly with publishable papers and broadly affecting the social sciences. 70% of respondents are more optimistic about paper productivity than about broader field impact. There are few researchers more optimistic about field impacts than about paper productivity, and many who are more pessimistic.

## Discussion

Social scientists who are using coding agents are posting more working papers and applying for more grants. Relative to others in their discipline and career stage, they are also starting more projects. But as of March 2026, they are not yet driving a surge in journal submissions. --------------------------------------------------------------------------------
Anthropic Economic Index report: Learning curves \ Anthropic (https://www.anthropic.com/research/economic-index-march-2026-report?email_hash=23463b99b62a72f26ed677cc556c44e8)
citeturn24734search4 [wordlim: 200] Published: 6 months ago; Crawled: 2 weeks ago;             url = {https://www.anthropic.com/research/economic-index-march-2026-report},

Economics

# Anthropic Economic Index report: Learning curves

Mar 24, 2026

The Anthropic Economic Index uses our privacy-preserving data analysis system to track how Claude is being used across the economy. It’s part of our effort to understand the economic impacts of AI as early as possible, so that researchers and policymakers have adequate time to prepare.

This latest report studies Claude usage in February 2026, building on the economic primitives framework introduced in our previous report (which used data from November 2025). Our sample covers February 5 to February 12, three months following the release of Claude Opus 4.5 and coincident with the release of Claude Opus 4.6.

We first document how usage has changed relative to our previous reports: the rate of augmentation, collaborative interaction where the AI complements the user’s abilities, increased slightly in both Claude.ai and API traffic. In Claude.ai, usage diversified, with the top 10 tasks accounting for a smaller share of usage last month than in November 2025. As a result of this diversification, the average conversation in Claude.ai had a slightly lower-wage task than in previous reports.

We then focus on an important determinant of Claude’s impact on the labor market and the broader economy: learning curves in Claude adoption. We present evidence that high-tenure users have developed habits and strategies that allow them to better harness Claude’s capabilities. Indeed, we document that more experienced users not only attempt higher-value tasks, but are also more likely to elicit successful responses in their conversations.

#### What has changed since our last report

In the first chapter, we revisit findings from our previous Economic Index report, published in January 2026. We find that:

  * Use cases on Claude.ai diversified. Coding tasks continue to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic.^{1} In this report, Claude.ai usage was less concentrated: the top 10 tasks made up 19% of all traffic in February, down from 24% in November. Claude Code’s agentic architecture splits coding work into smaller API calls, which are labeled as distinct tasks. So while coding’s overall share of API traffic has grown, it is spread across many task categories rather than concentrated in a few. As a result, task concentration in the API remained roughly flat despite the influx of coding activity.

ImageFigure 1.1: Usage shares among top 10 tasks over time by platform, Claude.ai and 1P API. Share of conversations assigned to the ten most prevalent O*NET tasks, by platform and report version.

This migration of code out of Claude.ai is not the only factor driving decreased concentration. Part of the drop is due to changes in the mix of use cases between the two periods. Coursework fell from 19% to 12% of conversations, while personal use rose from 35% to 42% of conversations. Some of the drop in coursework can be explained by academic calendars in countries where students were on winter break during our sample period.^{4} At the same time, increasing signups beginning around February brought more casual AI users.
## Appendix

Available here.

#### Data availability

Data from this report is available here.

## Authors and acknowledgements

#### First author block*:

Maxim Massenkoff, Eva Lyubich, Peter McCrory

*Lead authors of the report

#### Second author block:

Ruth Appel, Ryan Heller

#### Acknowledgements

Tim Belonax, Keir Bradwell, Andy Braden, Dexter Callender III, Miriam Chaum, Madison Clark, Evan Frondorf, Deep Ganguli, Kunal Handa, Hanah Ho, Owen Kaye-Kauderer, Jennifer Martinez, Miles McCain, Jared Mueller, Kelsey Nanan, Tyler Neylon, Dianne Penn, Sarah Pollack, Ankur Rathi, David Saunders, Michael Stern, Alex Tamkin, Kim Withee, Jack Clark

#### Citation
    
    `@online{anthropic2026aeiv5,
            author = {Maxim Massenkoff and Eva Lyubich and Peter McCrory and Ruth Appel and Ryan Heller},
            title = {Anthropic Economic Index report: Learning curves},
            date = {2026-03-24},
            year = {2026},
            url = {https://www.anthropic.com/research/economic-index-march-2026-report},
--------------------------------------------------------------------------------
How Australia uses Claude \ Anthropic (https://www.anthropic.com/research/how-australia-uses-claude?AdId=DP_PM&CampaignId=&SiteId=DP_Social&field_format_value=3&marketingSource=7013X000001MDNoQAO&programme_code=MFIN)
citeturn24734search5 [wordlim: 200] Published: 6 months ago; Crawled: 2 weeks ago;     url = {https://www.anthropic.com/research/australia-brief-economic-index-march-2026},

  * Research
  * Policy
  * Commitments
  * Learn
  * News

Try Claude

Economics

# How Australia uses Claude: Findings from the Anthropic Economic Index

Mar 31, 2026

Anthropic is expanding to Australia. We’re opening a new office in Sydney in the coming weeks, and we’ve signed a Memorandum of Understanding with the Australian government to cooperate on AI safety research and support the goals of Australia’s National AI Plan. To mark the occasion, we thought we’d look more closely into how Australians are using Claude.

## 
Key Findings

  * Australia is among the leading adopters of Claude, accounting for 1.6% of global Claude.ai traffic. Per capita, Australians’ use of Claude is more than four times higher than expected for the size of its population.
  * Adoption within Australia is concentrated in two states: New South Wales (37% of conversations) and Victoria (31%). Per capita Claude usage is lower in every other state and territory.
--------------------------------------------------------------------------------
Mapping AI-enabled cyber threats \ Anthropic (https://www.anthropic.com/research/attack-navigator)
citeturn24734search6 [wordlim: 200] Published: 4 months ago; Crawled: 2 days ago; The findings in this report are drawn from 832 accounts that Anthropic banned for violating cyber-related parts of our Usage Policy between March 2025 and March 2026. ... GTG-1002’s activity was novel for using an AI agent to autonomously chain together many stages of the cyberattack lifecycle—reconnaissance, exploitation, lateral movement, and exfiltration—into a coherent operation, making real-time decisions about what to do and what data to collect.

Frontier Red Team

# Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK Navigator

Jun 3, 2026

Kyla Guru, Alex Moix, and Jacob Klein

We’ve spent the past year investigating how threat actors are weaponizing AI to conduct cyber operations. Today, we’re sharing a new analysis that maps these real-world attacks onto the MITRE ATT&CK® framework, a database of tactics and techniques used by cyberattackers. Doing so reveals patterns that challenge traditional assumptions about cybersecurity—for example, the level of risk a threat actor poses can be assessed via metrics like technical sophistication or breadth of techniques. We partnered with Verizon to include some of these results in the 2026 Verizon Data Breach Investigation Report (DBIR), and are publishing this report to offer a longer-form analysis of trends we are seeing in AI-enabled cyber operations.^{[1]}

## Key findings

For this study, we analyzed 832 accounts associated with malicious cyber activity over the course of one year, from March 2025 to March 2026. ## About the dataset

The findings in this report are drawn from 832 accounts that Anthropic banned for violating cyber-related parts of our Usage Policy between March 2025 and March 2026. We identified these accounts through a combination of automated safeguards and investigations by our Threat Intelligence team. For each account, we produced a summary of the observed activity. We then extracted the tactics, techniques, and procedures (or TTPs) described in those summaries, and mapped them to the version of the MITRE ATT&CK framework that was live at that time (V18). In all, we observed 13,873 actions across 482 unique techniques and all 14 ATT&CK tactics.

We gave each actor a risk score from 0 to 100 (with 0 being the lowest risk and 100 being the highest) based on a new methodology we’ve developed called the AI Risk Enablement Score (ARiES), described below. We’ve anonymized the data so that actors cannot be identified in the analysis that follows.

## The LLM ATT&CK Navigator and ARiES risk score
--------------------------------------------------------------------------------
Can we predict the jobs robots will do? \ Anthropic (https://www.anthropic.com/research/what-work-can-robots-do)
citeturn24734search7 [wordlim: 200] Published: yesterday; Crawled: today; Massenkoff, Maxim and Peter McCrory, "Labor Market Impacts of AI: A New Measure and Early Evidence," Anthropic, March 5, 2026. https://www.anthropic.com/research/labor-market-impacts

Mason, Matthew T., "Toward Robotic Manipulation," Annual Review of Control, Robotics, and Autonomous Systems, 2018, 1, 1-28.

Massenkoff, Maxim and Peter McCrory, "Labor Market Impacts of AI: A New Measure and Early Evidence," Anthropic, March 5, 2026. https://www.anthropic.com/research/labor-market-impacts

Mayekawa, "Deboning Machines," product page, 2026a. https://mayekawa.com/products/deboning_machines/

Mayekawa, "Reducing Workloads with Reliable Deboning Technology and Stabilizing Production to Meet Market Demands for Pork," With Mayekawa, 2026b (undated; retrieved September 29, 2026). https://mayekawa.com/with/stories/hamdas/

McKinsey & Company, "The Future of Robotics: Intelligent, Adaptable, and on Your Team," The Next Normal, 2026. https://www.mckinsey.com/featured-insights/the-next-normal/robotics

Metzger, Jean-Claude, Olivier Lambercy, Antonella Califfi, Daria Dinacci, Claudio Petrillo, Paolo Rossi, Fabio M. Conti, and Roger Gassert, "Assessment-Driven Selection and Adaptation of Exercise Difficulty in Robot-Assisted Therapy: A Pilot Study with a Hand Rehabilitation Robot," Journal of NeuroEngineering and Rehabilitation, 2014, 11, 154.

Moravec, Hans, Mind Children: The Future of Robot and Human Intelligence, Cambridge, MA: Harvard University Press, 1988.

--------------------------------------------------------------------------------
Étendre les amplitudes à un seul moins aux gravitons | OpenAI (https://openai.com/fr-FR/index/extending-single-minus-amplitudes-to-gravitons/)
citeturn24734search8 [wordlim: 200] Published: 7 months ago; Crawled: 3 weeks ago; # Étendre les amplitudes à un seul moins aux gravitons ... L’article, « Single-minus graviton tree amplitudes are nonzero », est signé par Alfredo Guevara (Institute for Advanced Study), Alexandru Lupsasca (Vanderbilt University et OpenAI), David Skinner (University of Cambridge), Andrew Strominger (Harvard University) et Kevin Weil (OpenAI) au nom d’OpenAI.

4 mars 2026

RecherchesPublication

# Étendre les amplitudes à un seul moins aux gravitons

Des chercheurs ont utilisé GPT‑5.2 Pro pour aider à trouver un nouveau résultat mathématique décrivant comment les particules peuvent interagir en gravité quantique.

Lire le préprint(ouverture dans une nouvelle fenêtre)

Comprendre les amplitudes à un seul moins en gravité

  * Comprendre les amplitudes à un seul moins en gravité
  * Méthodologie et vérification
  * Et ensuite ?

  * Comprendre les amplitudes à un seul moins en gravité
  * Méthodologie et vérification
  * Et ensuite ?

Nous avons publié un nouveau préprint étudiant les amplitudes de diffusion en gravité quantique, qui étend des résultats récents obtenus pour les gluons au cadre gravitationnel. Ce travail montre qu’une classe d’interactions de gravitons longtemps supposées s’annuler peut en réalité apparaître sous des conditions cinématiques bien définies. --------------------------------------------------------------------------------
Responsible Agents and the Future of AI \ Anthropic (https://www.anthropic.com/events/agentic-ai-in-action)
citeturn24734search9 [wordlim: 200] Crawled: today; March 17, 2026 10:00 AM ... Join Anthropic for an in-person event on the morning of 17 March in London, bringing together thought leaders, industry figures and policymakers from across the UK AI ecosystem to explore the latest developments in agentic AI and preview how agentic AI can deliver benefits across the UK's public and private sectors.

# Responsible Agents and the Future of AI

London, UK

Join us to preview the latest developments in agentic AI

Mar

 

17

-

17

, 

2026

17 Mar 2026

 - 

10:00 am

 - 

1:00 pm

 

GMT (UTC+0)

# Responsible Agents and the Future of AI

London, UK

Join us to preview the latest developments in agentic AI

## Watch the livestream

Add to calendar

Livestream:

Responsible Agents and the Future of AI

Join us to preview the latest developments in agentic AI

GMT (UTC+0)

March 17, 2026 10:00 AM

March 17, 2026 1:00 PM

## Responsible Agents and the Future of AI

Add to calendar

Responsible Agents and the Future of AI

Join us to preview the latest developments in agentic AI Learn more at https://www.anthropic.com/events/agentic-ai-in-action

GMT (UTC+0)

March 17, 2026 10:00 AM

March 17, 2026 1:00 PM

London, UK

  * Google
  * Apple
  * Outlook

### About

Join Anthropic for an in-person event on the morning of 17 March in London, bringing together thought leaders, industry figures and policymakers from across the UK AI ecosystem to explore the latest developments in agentic AI and preview how agentic AI can deliver benefits across the UK's public and private sectors.
--------------------------------------------------------------------------------
Estendendo amplitudes single-minus para grávitons | OpenAI (https://openai.com/pt-BR/index/extending-single-minus-amplitudes-to-gravitons/)
citeturn24734search10 [wordlim: 200] Published: 7 months ago; Crawled: 2 weeks ago; Publicamos um novo preprint sobre amplitudes de espalhamento em gravidade quântica, estendendo resultados recentes obtidos para glúons para o contexto gravitacional. ... O artigo, “Single-minus graviton tree amplitudes are nonzero”, é assinado por Alfredo Guevara (Institute for Advanced Study), Alexandru Lupsasca (Vanderbilt University e OpenAI), David Skinner (University of Cambridge), Andrew Strominger (Harvard University) e Kevin Weil (OpenAI), em nome da OpenAI.
--------------------------------------------------------------------------------
Alignment Science Blog (https://alignment.anthropic.com/)
citeturn24734search11 [wordlim: 200] Crawled: yesterday; March 2026 ... A3: An Automated Alignment Agent for Safety Finetuning We introduce our Automated Alignment Agent (A3), a new agentic framework which automatically mitigates safety failures in Large Language Models with minimal human intervention.
--------------------------------------------------------------------------------
Single-minus graviton tree amplitudes are nonzero (https://cdn.openai.com/pdf/graviton.pdf)
citeturn24734search12 [wordlim: 200] Published: 7 months ago; Alfredo Guevara,¹ Alexandru Lupsasca,²,³ David Skinner,⁴ Andrew Strominger,⁵ and Kevin Weil² on behalf of OpenAI ... A general formula is derived for the single-minus amplitude involving sums over tree diagrams with a number of terms that grows exponentially in the number n of gravitons.
--------------------------------------------------------------------------------
Single-minus graviton tree amplitudes are nonzero (https://cdn.openai.com/pdf/graviton.pdf.)
citeturn24734search13 [wordlim: 200] Published: 4 months ago; Andrew Strominger,5 and Kevin Weil2 on behalf of OpenAI ... grows exponentially in the number n of gravitons.
--------------------------------------------------------------------------------
GR singmin - regenerate (https://cdn.openai.com/pdf/gluon-to-graviton-paper.pdf)
citeturn24734search14 [wordlim: 200] Published: 7 months ago; ↳ Regenerate paper with gravitons ... - for requirements, rather than color identities and soft theorem, we use the permutation symmetry and the leading and subleading graviton theorem in this language

