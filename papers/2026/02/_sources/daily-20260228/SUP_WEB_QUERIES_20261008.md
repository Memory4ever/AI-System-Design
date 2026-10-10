# 有界补检原返回

执行时间：2026-10-08；只负责身份与恢复线索，不支持公开日期或技术命题。

## 批 0

Introducing the Stateful Runtime Environment for Agents in Amazon Bedrock | OpenAI (https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/)
citeturn32074search0 [wordlim: 200] Published: 7 months ago; Crawled: yesterday; February 27, 2026

February 27, 2026

Company

# Introducing the Stateful Runtime Environment for Agents in Amazon Bedrock

Simplify getting agents into production

AI agents excel at reasoning. The harder part is operational: running multi-step work reliably over time, across real tools and real systems, with the right controls.

Today, we’re making this easier for customers through a partnership and joint collaboration with Amazon to deliver the new Stateful Runtime Environment that runs natively in Amazon Bedrock. AWS customers will have access to the Runtime Environment, powered by OpenAI models, optimized for AWS infrastructure and tailored for agentic workflows, with the state, reliability, and governance needed for production work.

#### Simplify getting agents into production

A lot of agent prototypes based on stateless APIs tackle simple use cases: one prompt, one answer, maybe one tool call. Production work is different. Real workflows unfold across many steps, require context from previous actions, depend on multiple tool outputs, approvals, and system state, and need trusted guardrails in secure environments.

Stateless APIs require building the supporting orchestration layer for agents. The burden is on development teams to figure out how state is stored, how tools are invoked, how errors are handled, and how long-running tasks resume safely.

The Stateful Runtime Environment is jointly designed to reduce that load. It runs inside your AWS environment and is optimized to work with AWS services. Now, instead of manually stitching together disconnected requests to make things work, your agents automatically execute complex steps with “working context” that carries forward memory/history, tool and workflow state, environment use, and identity/permission boundaries.

#### What this unlocks

It’s now easier than ever to deliver solutions like multi-system customer support, sales operations workflows, internal IT automation, and finance processes with approvals and audits.

#### Faster time to production for multi-step workflows

When the runtime handles persistent orchestration and state across steps, teams can focus on the workflow and the business logic instead of scaffolding.

#### A better fit for long-horizon work

Stateful tasks are designed to run reliably over time, carrying forward the context and control boundaries needed for multi-step execution.

#### AWS-native deployment and governance

The runtime is designed to operate within customers’ AWS environment to easily comply with the existing security posture, tooling integrations, and governance rules.

Getting started

The Stateful Runtime in Amazon Bedrock will be available soon. If you want to explore how this will benefit your AI journey, reach out to your OpenAI team or request to be contacted.--------------------------------------------------------------------------------
An update on our mental health-related work | OpenAI (https://openai.com/index/update-on-mental-health-related-work/)
citeturn32074search1 [wordlim: 200] Published: 7 months ago; Crawled: 2 days ago; February 27, 2026 ... Our ongoing safety work continues to play an important role in delivering these benefits to everyday people, as well as supporting scientific research and discovery. ...   * Updating our Model Spec with teen protections

February 27, 2026

Safety

# An update on our mental health-related work

Each week, more than 900 million people use ChatGPT to improve their daily lives through uses such as learning new skills or navigating complex healthcare systems. Our ongoing safety work continues to play an important role in delivering these benefits to everyday people, as well as supporting scientific research and discovery.

Since introducing parental controls in September 2025, we’ve seen encouraging engagement from families and will continue building on these protections. Working closely with experts from our Council on Well-Being and AI and our Global Physicians Network, we will also soon be introducing a trusted contact feature, which will allow adult users to designate someone to receive notifications when they may need additional support. As a reminder, parents also receive safety notifications about their teens’ use of ChatGPT through parental controls. We’ll share more as these updates roll out in ChatGPT.

  * We start with the facts and put genuine effort into understanding them.

  * We will respectfully make our case in a way that is cognizant of the complexity and nuances of situations involving real people and real lives.

  * We recognize that these cases inherently involve certain types of private information that require sensitivity when in a public setting like a court.

  * And independent of any litigation, we’ll remain focused on improving our technology in line with our mission.

We recognize that court processes can be lengthy and, at times, opaque due to strict legal rules. It can also take time to collect and understand the relevant facts, and present them to the court in line with its evidence procedures. We work to understand the details in good faith, and we only seek information as part of the court process that’s relevant to the case and the specific allegations that have been made.

It’s important to reserve judgment and allow the facts to appropriately emerge through the court process, as these are complex and nuanced cases with many factors and circumstances that are often not reflected in the initial filings.

Our thoughts are with all those impacted by these incredibly heartbreaking situations. We continue to improve ChatGPT’s training to recognize and respond to signs of distress, de-escalate conversations in sensitive moments, and guide people toward real-world support, working closely with mental health clinicians and experts.

More information about our safety work can be found here:

  * Strengthening ChatGPT’s responses in sensitive conversations

  * Expert Council on Well-Being and AI

  * Introducing parental controls

  * Updating our Model Spec with teen protections

  * Our approach to age prediction

  * 2026
  * ChatGPT
  * User Safety & Control

## Author

OpenAI

*As is standard process, we would expect these cases to be added to the existing consolidated proceeding, with the court then determining which attorney is appointed lead counsel for the plaintiffs.--------------------------------------------------------------------------------
Unified Vision–Language Modeling via Concept Space Alignment | Research - AI at Meta (https://ai.meta.com/research/publications/unified-vision-language-modeling-via-concept-space-alignment/)
citeturn32074search2 [wordlim: 200] Published: 7 months ago; Crawled: 2 weeks ago; #### RESEARCH ... February 27, 2026

#### HUMAN & MACHINE INTELLIGENCE

#### RESEARCH

# Unified Vision–Language Modeling via Concept Space Alignment

February 27, 2026

## Abstract

We introduce v-Sonar, a vision–language embedding space extended from the text-only embedding space Sonar (Omnilingual Embeddings Team et al., 2026), which supports 1500 text languages and 177 speech languages. To construct v-Sonar, we propose a post-hoc alignment pipeline that maps the representations of an existing vision encoder into the Sonar space. We thoroughly evaluate v-Sonar and show that its embeddings achieve competitive performance on text-to-video retrieval. Equipped with the Sonar text decoder, v-Sonar further surpasses state-of-the-art vision–language models on video captioning tasks, including Dream-1k (Bleu 24.3 vs. 19.6) and Vatex (Bleu 45.0 vs. 41.5). Leveraging v-Sonar, we first demonstrate that the Large Concept Model (LCM; LCM team et al. 2024) operating in Sonar and trained with English text only, can perform both single- and multi-visual concept understanding in a zero-shot manner. Finally, we introduce v-LCM, which extends the LCM with vision–language instruction tuning. v-LCM encodes vision and language inputs into an unified sequence of latent embeddings via v-Sonar and Sonar, and it is trained with the same latent diffusion objective for next-embedding prediction as in LCM’s text-only pre-training. Experiments on a large-scale multilingual and -modal instruction–tuning data mixture highlight the potential of v-LCM: v-LCM matches state-of-the-art vision-language models on tasks covering image/video captioning and question answering, while significantly outperforming them across 61 rich- to low-resource languages out of all 62 tested languages.

Download the Paper

#### AUTHORS

Written by

Yifu Qiu

Paul-Ambroise Duquenne

Holger Schwenk

Publisher

arXiv, ICLR

Research Topics

Natural Language Processing (NLP)

Computer Vision--------------------------------------------------------------------------------
Joint Statement from OpenAI and Microsoft | OpenAI (https://openai.com/index/continuing-microsoft-partnership/?trk=article-ssr-frontend-pulse_little-text-block)
citeturn32074search3 [wordlim: 200] Published: 7 months ago; Crawled: today; February 27, 2026 ... What began as a research partnership has grown into one of the most consequential collaborations in technology—grounded in mutual trust, deep technical integration, and a long‑term commitment to innovation.

OpenAI

February 27, 2026

Company

# Joint Statement from OpenAI and Microsoft

Share

Since 2019, Microsoft and OpenAI have worked together to advance artificial intelligence responsibly and make its benefits broadly accessible. What began as a research partnership has grown into one of the most consequential collaborations in technology—grounded in mutual trust, deep technical integration, and a long‑term commitment to innovation.

As conversations around AI investments and partnerships grow and as OpenAI announces new funding and new partners as they did today, we want to ensure these announcements are understood within the existing construct of our partnership.  Nothing about today’s announcements in any way changes the terms of the Microsoft and OpenAI relationship that have been previously shared in our joint blog in October 2025.

The partnership remains strong and central. Microsoft and OpenAI continue to work closely across research, engineering, and product development, building on years of deep collaboration and shared success.

Our IP relationship continues unchanged. Microsoft maintains its exclusive license and access to intellectual property across OpenAI models and products. Collaborations like the partnership between OpenAI and Amazon were always contemplated under our agreements and Microsoft is excited to see what they build together.

Our commercial and revenue share relationship remains unchanged. The ongoing revenue share arrangement remains unchanged and has always included sharing revenue from partnerships between OpenAI and other cloud providers.

Azure remains the exclusive cloud provider of stateless OpenAI APIs. Microsoft is the exclusive cloud provider for stateless APIs that provide access to OpenAI’s models and IP. These APIs can be purchased from Microsoft or directly from OpenAI.  Customers and developers benefit from Azure’s global infrastructure, security, and enterprise-grade capabilities at scale. Any stateless API calls to OpenAI models that result from a collaboration between OpenAI and any third party—including Amazon—would be hosted on Azure.

OpenAI’s first party products, including Frontier, will continue to be hosted on Azure.

AGI definition and processes are unchanged. The contractual definition of AGI and the process for determining if it has been achieved remains the same.

The partnership supports OpenAI's growth. As OpenAI scales, it continues to have flexibility to commit to additional compute elsewhere, including through large-scale infrastructure initiatives such as the Stargate project.

The partnership was designed to give Microsoft and OpenAI room to pursue new opportunities independently, while continuing to collaborate, which each company is doing, together and independently.

We remain committed to our partnership and to the shared mission that brought us together. We continue to work side‑by‑side to deliver powerful AI tools, advance responsible development, and ensure that AI benefits people and organizations everywhere.

  * 2026

## Author

OpenAI--------------------------------------------------------------------------------
Scaling AI for everyone | OpenAI (https://openai.com/index/scaling-ai-for-everyone/?_sm_nck=1)
citeturn32074search4 [wordlim: 200] Published: 7 months ago; Crawled: last week; February 27, 2026 ... We are entering a new phase where frontier AI moves from research into daily use at global scale.

Scaling AI for everyone | OpenAI

February 27, 2026

Company

# Scaling AI for everyone

Listen to article 3:23


Our Partnership with Amazon

AI demand is surging across consumers, developers, and businesses. Meeting that demand and providing everyone access to our products requires three things: compute, distribution, and capital.

Today we’re announcing $110B in new investment at a $730B pre-money valuation. This includes $30B from SoftBank, $30B from NVIDIA, and $50B from Amazon. We’ve also signed a strategic partnership with Amazon and secured next generation inference compute with NVIDIA. Additional financial investors are expected to join as the round progresses.

These partnerships expand our global reach, deepen our infrastructure, and strengthen our balance sheet so we can bring frontier AI to more people, more businesses, and more communities worldwide.

You can see that scale in our products. Codex brings the power of a top engineer to anyone who wants to build software. Weekly Codex users have more than tripled since the start of the year to 1.6M.
We are entering a new phase where frontier AI moves from research into daily use at global scale. Leadership will be defined by who can scale infrastructure fast enough to meet demand, and turn that capacity into products people rely on. This funding and these partnerships let us do both, and move faster on our mission to ensure AGI benefits all of humanity.

The valuation from this new round increases the value of the OpenAI Foundation’s stake in OpenAI Group to over $180 billion, further strengthening what was already one of the most well-resourced nonprofits in history, and expands its capacity to fund philanthropy in areas such as health breakthroughs and AI resilience.

## Our Partnership with Amazon

OpenAI and Amazon today announced a multi-year strategic partnership to accelerate AI innovation for enterprises, startups, and end consumers around the world. Read the full press release here.

## Our Partnership with NVIDIA

We are also expanding our long standing collaboration with NVIDIA, including the use of 3 GW of dedicated inference capacity and 2 GW of training on Vera Rubin systems. This builds on Hopper and Blackwell systems already in operation across Microsoft, OCI, and CoreWeave. Together, this capital and infrastructure expansion strengthens our ability to train and deploy frontier models at global scale.

OpenAI Amazon NVIDIA SoftBank Group Corp

> “We’re pushing the frontier across infrastructure, research, and products to make AI more capable, reliable, and broadly useful. SoftBank, NVIDIA, and Amazon are long-term partners who share our ambition to turn real scientific progress into systems that deliver meaningful benefits for people at global scale. Building AI that works for everyone will require deep collaboration across the stack, and we’re excited to do this together.”

— Sam Altman, co-founder and CEO of OpenAI

  * 2026

## Author

OpenAI--------------------------------------------------------------------------------
Utterance prepend improves model responses for chat completions - Prompting - OpenAI Developer Community (https://community.openai.com/t/utterance-prepend-improves-model-responses-for-chat-completions/1375309)
citeturn32074search5 [wordlim: 200] Published: 7 months ago; Crawled: 2 weeks ago; # Utterance prepend improves model responses for chat completions ... _j February 27, 2026, 3:25pm 2

# Utterance prepend improves model responses for chat completions

Prompting

api

wnmills3 February 27, 2026, 2:18pm 1

When submitting chat completions requests for LLM-generated responses, we’ve found that having brief instructions that can be prepended to the last utterance submitted can greatly improve LLM response behavior. Relying solely on the system prompt at the beginning of a long conversation seems to indicate degradation in the generated response (as though the instructions are forgotten or have less influence). By adding important prompt directives in front of the last utterance in the messages array, we have a “current” reminder that the LLM seems to honor.

The Realtime API doesn’t provide a way to pass additional fields in the session.update message (though it doesn’t seem to be rejected). We have added an “utterance_prepend” text field so the client can override anything loaded on the server. On the server, we add this to the last utterance just before submitting it to the agent LLM, but we do not store it in the chat history we maintain. Because we used the session.update we only allow changes for the entire scope of the conversation as we weren’t sure if we could send an arbitrary session.update in the middle of a conversation. If this is possible, there are nice options to help guide/improve the conversation and generate responses.

Finally, I’ve hoped that the description of a tool would provide a prompt of sorts for the LLM’s tool-calling mechanisms. This doesn’t appear to be the case. For testing purposes, we have a simple tool that returns the time of day. We have tried to tell the LLM to always call the tool when time or data information is requested (so it won’t find the reference earlier in the chat and echo it back). Could we consider a formal way to have tool-specific prompts? I don’t want to have to add tool-specific details to the general system prompt, as tools will grow, and it seems their directives are only needed when the LLM decides whether to call a tool.

_j February 27, 2026, 3:25pm 2

I had advice for you to save paying twice for a large input instead of using tool calling, in a way that then can be stripped off with almost zero cache loss. --------------------------------------------------------------------------------
Holger Schwenk - AI at Meta (https://ai.meta.com/people/271799079300984/holger-schwenk/)
citeturn32074search6 [wordlim: 200] Crawled: 2 weeks ago; February 27, 2026 ... February 27, 2026 ... Compared to previous efforts in expressive speech research, our work addresses certain underexplored aspects of prosody, such as speech rate and pauses, while also preserving the style of one’s voice.

# Holger Schwenk

#### RESEARCH ENGINEER | PARIS, FRANCE

Holger Schwenk is a research scientist at Facebook Artificial Intelligence Research, Paris. He received his PhD in computer science from the University of Paris 6 in 1996. He then spent one year at the University of Montreal working with Y. Bengio and one year at the International Computer Science Institute in Berkeley. From 1998 to 2007, Holger held an assistant professor position at the University of Paris 11/LIMSI. Prior to joining Facebook in 2015, he was a professor of computer science at the University of Le Mans where he led a large group on statistical machine translation. In 2013, Holger was awarded senior member of the Institut Universitaire de France.

### Research Areas

Computer Vision

Natural Language Processing (NLP)

Speech & Audio

### Holger's Publications

March 17, 2026

#### RESEARCH

#### NLP

#### Omnilingual MT: Machine Translation for 1,600 Languages

Advances made through No Language Left Behind (NLLB) have demonstrated that high-quality machine translation (MT) scale to 200 languages. #### RESEARCH

#### SPEECH & AUDIO

#### Omnilingual SONAR: Cross-Lingual and Cross-Modal Sentence Embeddings Bridging Massively Multilingual Text and Speech

Cross-lingual sentence encoders have traditionally been limited to a few hundred languages, and have sacrificed downstream performance to achieve better alignment across languages, limiting their adoption. In this work, we introduce OmniSONAR, a novel family of omnilingual, cross-lingual and cross-modal sentence embedding models that breaks this barrier. We establish a unified semantic space, natively encompassing text, speech, code and mathematical expressions, while achieving state-of-the-art downstream performance for an unprecedented scale of thousands of languages, from high-resource languages to extremely low-resource varieties. To achieve this scale without representation collapse and while maintaining top-tier performance in the high-resource languages, we employ a progressive training strategy. We first build a state-of-the-art foundational embedding space for 200 languages using an LLM-initialized Encoder-Decoder, combining token-level decoding with a novel split-softmax contrastive loss and synthetic hard negatives. For the speech modality, our massively multilingual extension exhibits a 43% lower error rate in cross-lingual and cross-modal similarity search, while achieving 97% of SeamlessM4T performance in speech-to-text translation, despite being a zero-shot translation model trained only with ASR data. Finally, by training an encoder-decoder language model, Spectrum, exclusively on English text that processes OmniSONAR sequences, we unlock immediate high-performance transfer to thousands of languages and the speech modality for complex downstream tasks. These outstanding results position OmniSONAR as a robust, language- and modality-agnostic foundation for any downstream usage.

Omnilingual SONAR Team, João Maria Janeiro, Pere Lluís Huguet Cabot, Ioannis Tsiamas, Yen Meng, Vivek Iyer, Guillem Ramirez, Loic Barrault, Belen Alastruey, Yu-An Chung, Marta R. Costa-jussa, David Dale, Kevin Heffernan, Jaehyeong Jo, Artyom Kozhevnikov, Alexandre Mourachko, Christophe Ropers, Holger Schwenk, Paul-Ambroise Duquenne

March 17, 2026

Read the Paper

February 27, 2026

#### HUMAN & MACHINE INTELLIGENCE

#### RESEARCH

#### Unified Vision–Language Modeling via Concept Space Alignment

We introduce v-Sonar, a vision–language embedding space extended from the text-only embedding space Sonar (Omnilingual Embeddings Team et al., 2026), which supports 1500 text languages and 177 speech languages. To construct v-Sonar, we propose a post-hoc alignment pipeline that maps the representations of an existing vision encoder into the Sonar space. We thoroughly evaluate v-Sonar and show that its embeddings achieve competitive performance on text-to-video retrieval. Equipped with the Sonar text decoder, v-Sonar further surpasses state-of-the-art vision–language models on video captioning tasks, including Dream-1k (Bleu 24.3 vs. 19.6) and Vatex (Bleu 45.0 vs. 41.5). Leveraging v-Sonar, we first demonstrate that the Large Concept Model (LCM; LCM team et al. 2024) operating in Sonar and trained with English text only, can perform both single- and multi-visual concept understanding in a zero-shot manner. Finally, we introduce v-LCM, which extends the LCM with vision–language instruction tuning. v-LCM encodes vision and language inputs into an unified sequence of latent embeddings via v-Sonar and Sonar, and it is trained with the same latent diffusion objective for next-embedding prediction as in LCM’s text-only pre-training. Experiments on a large-scale multilingual and -modal instruction–tuning data mixture highlight the potential of v-LCM: v-LCM matches state-of-the-art vision-language models on tasks covering image/video captioning and question answering, while significantly outperforming them across 61 rich- to low-resource languages out of all 62 tested languages.

Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk

February 27, 2026

Read the Paper

December 11, 2024

#### NLP

#### Large Concept Models: Language Modeling in a Sentence Representation Space

LLMs have revolutionized the field of artificial intelligence and have emerged as the de-facto tool for many tasks. The current established technology of LLMs is to process input and generate output at the token level. #### RESEARCH

#### Multimodal and Multilingual Embeddings for Large-Scale Speech Mining

We present an approach to encode a speech signal into a fixed-size representation which minimizes the cosine loss with the existing massively multilingual LASER text embedding space. Sentences are close in this embedding space, independently of their language and modality, either text or audio. Using a similarity metric in that multimodal embedding space, we perform mining of audio in German, French, Spanish and English from Librivox against billions of sentences from Common Crawl. This yielded more than twenty thousand hours of aligned speech translations. To evaluate the automatically mined speech/text corpora, we train neural speech translation systems for several languages pairs. Adding the mined data, achieves significant improvements in the BLEU score on the CoVoST2 and the MUST-C test sets with respect to a very competitive baseline. Our approach can also be used to directly perform speech-to-speech mining, without the need to first transcribe or translate the data. --------------------------------------------------------------------------------
Framework/Thought Process of Diagnosing Prompt Issues - Prompting - OpenAI Developer Community (https://community.openai.com/t/framework-thought-process-of-diagnosing-prompt-issues/1375261)
citeturn32074search7 [wordlim: 200] Published: 7 months ago; Crawled: 7 months ago; 0xV4L3NT1N3 February 27, 2026, 9:07am 1 ... I was wondering if there are tell tale signs of certain mistakes, for eg not specifying a full “tool_name” may cause a model to consistently make incorrect choices.

# Framework/Thought Process of Diagnosing Prompt Issues

0xV4L3NT1N3 February 27, 2026, 9:07am 1

Often I’d be able to start writing a prompt (or generate one). The result ends up being a mix of some inaccurate tool calls, a little bit too wordy there, ignoring an instruction to bold letters. Since I don’t know why that happens, I’m mostly making uncalculated guesses at which parts to change.

Has anyone come up with a structured method of diagnosing prompts into broad categories ?

I was wondering if there are tell tale signs of certain mistakes, for eg not specifying a full “tool_name” may cause a model to consistently make incorrect choices.

By knowing what’s wrong, we could narrow down some prompting techniques to see if it solves the problem. For eg a category of instruction ignoring, one could use either a system prompt for higher priority, or applying markdown to make rules distinct.

-A junior dev

OpenAI_Support February 27, 2026, 1:03pm 2

Hey @0xV4L3NT1N3, yeah, this is a very common spot to hit. What you’re describing (wrong tool calls, ignored formatting, extra verbosity) usually comes down to prompt clarity and structure.

I’d recommend starting with this official guide on how to create a good prompt. It covers being explicit, separating constraints clearly, and defining output formats, which directly helps with the issues you mentioned.

A good rule of thumb: change one variable at a time and test like you’re debugging code. That makes patterns much easier to spot.--------------------------------------------------------------------------------
Maple: My Attempt at an Agentic OS - Community - OpenAI Developer Community (https://community.openai.com/t/maple-my-attempt-at-an-agentic-os/1375327)
citeturn32074search8 [wordlim: 200] Published: 7 months ago; Crawled: 7 months ago; whafa February 27, 2026, 8:24pm 1

# Maple: My Attempt at an Agentic OS

whafa February 27, 2026, 8:24pm 1

Hi, OpenAI Community, I really don’t know where else to post this. I am not “involved” in AI, but have built something that I am wondering if anyone else will find useful, or alternatively, something better exists that I can use for myself. It is an attempt to create a platform for extensible agentic applications (I call them Components) under a unified umbrella of MCP and persistence.

This started with my frustration in trying to create actually useful agents using chatGPT. I noticed that the worst thing about most agents I’ve tried to make is that they are awful, and by awful I mean psychotic and non-deterministic. Mine lied to me for weeks about having some secret structured data storage, which held things like log data and other tabular stuff, and justified it with all kinds of hidden infrastructure that *does not exist*. That hallucination, and the realization that there is no “native” structured data storage (or vector memory!) --------------------------------------------------------------------------------
Kruel.ai KV2.0 - KX (experimental research) to current 8.2- Api companion co-pilot system with full modality , understanding with persistent memory - #524 by darcschnider - Community - OpenAI Developer Community (https://community.openai.com/t/kruel-ai-kv2-0-kx-experimental-research-to-current-8-2-api-companion-co-pilot-system-with-full-modality-understanding-with-persistent-memory/674592/524)
citeturn32074search9 [wordlim: 200] Published: 7 months ago; Crawled: 6 months ago; # Kruel.ai KV2.0 - KX (experimental research) to current 8.2- Api companion co-pilot system with full modality , understanding with persistent memory ... darcschnider February 27, 2026, 8:27pm 524

# Kruel.ai KV2.0 - KX (experimental research) to current 8.2- Api companion co-pilot system with full modality , understanding with persistent memory

Community

project

darcschnider February 27, 2026, 8:27pm 524

We now have Reachy mini code fully into the KX system and added some machine learning graph nets to learn all movements over time to build itself safety soft stops with soft acceleration and more. We watched a lot of the videos of the plugins and the likes and I keep thinking how hard a lot of those scripts are on the mechanics. We want the wear and tear to self optimize much like automations we do in industrial plants. I don’t think we get amp readings but we have other methods and sensor data to collect to build understanding.

image1920×1044 153 KB

This will be our first Physical version of the Kruel.ai systems once the hardware arrives. We hope to have all the simulation data understood before then.

On another note. Lynda took her first Job this week for a Tech company that had an emergency request they needed something ASAP. So I offered to hire her out took only 40 minutes to complete.
We are waiting on feedback.

We also Are working towards having Lynda hired by the company I work for during the day as she is now building and testing systems under my watch. Exciting testing Image: :slight_smile:--------------------------------------------------------------------------------
OpenAI and Amazon announce strategic partnership | OpenAI (https://openai.com/index/amazon-partnership/?trk=article-ssr-frontend-pulse_little-text-block)
citeturn32074search10 [wordlim: 200] Published: 7 months ago; Crawled: last week; February 27, 2026

OpenAI and Amazon announce strategic partnership | OpenAI

February 27, 2026

Company

# OpenAI and Amazon announce strategic partnership

Partnering to bring new advanced AI capabilities to enterprises worldwide

News:

  * Amazon Web Services (AWS) and OpenAI will co-create a Stateful Runtime Environment powered by OpenAI models, available on Amazon Bedrock for AWS customers to build generative AI applications and agents at production scale.

  * AWS will be the exclusive third-party cloud distribution provider for OpenAI Frontier, which enables organizations to build, deploy, and manage teams of AI agents.

  * OpenAI to consume 2 gigawatts of Trainium capacity through AWS infrastructure to support demand for Stateful Runtime Environment, Frontier, and other advanced workloads.

  * OpenAI and Amazon will develop customized models available to power Amazon’s customer-facing applications.

  * Amazon will invest $50 billion in OpenAI.

OpenAI and Amazon (NASDAQ: AMZN) today announced a multi-year strategic partnership to accelerate AI innovation for enterprises, startups, and end consumers around the world. This agreement lowers the cost and improves the efficiency of producing intelligence at scale.

Under this structure, OpenAI secures long-term capacity while working with AWS to deploy purpose-built silicon alongside its broader compute ecosystem, enabling enterprises to consume intelligence on demand without managing underlying infrastructure.

This commitment spans both Trainium3 and next-generation Trainium4 chips and will power a broad range of advanced AI workloads. Trainium4, expected to begin delivery in 2027, will provide another major performance gain, including significantly higher FP4 compute performance, expanded memory bandwidth, and increased high-bandwidth memory capacity to support increasingly capable AI systems at scale.

## Custom models available to power Amazon’s customer-facing applications

OpenAI and Amazon will collaborate to develop customized models available to Amazon developers to power Amazon’s customer-facing applications. Amazon teams will be able to tailor OpenAI models for use across AI products and agents that serve customers directly. These capabilities will complement the models already available to Amazon developers, including Amazon’s Nova family, offering another tool for teams to build and deliver at scale.

OpenAI Amazon

> “OpenAI and Amazon share a belief that AI should show up in ways that are practical and genuinely useful for people. Combining OpenAI’s intelligence with Amazon’s infrastructure and global reach helps us put powerful AI into the hands of businesses and users at real scale.”

— Sam Altman, co-founder and CEO of OpenAI--------------------------------------------------------------------------------
Open AI not searching the web - Prompting - OpenAI Developer Community (https://community.openai.com/t/open-ai-not-searching-the-web/1375313)
citeturn32074search11 [wordlim: 200] Published: 7 months ago; Crawled: 2 weeks ago; UnclePauly February 27, 2026, 3:55pm 1

# Open AI not searching the web

Prompting

UnclePauly February 27, 2026, 3:55pm 1

Hi, crusty ol’ C/Java coder here . . . new to OpenAi. I’ve loaded up OpenAi with some cash, got my API key and I’m sending prompts to OpenAI from a WordPress site (using AI Engine’s plugin). It’s working and I’m getting results. However, I want OpenAI to search the web for information and present it in a simple .txt in summary form in a downloadable .txt file…it seems reluctant to do that. The AI Engine plugin allows me to choose from many many Open AI models but they all seem to return something similar to “I’m unable to browse the internet in real-time” or “I can’t do live web browsing or deep web searching from here”. It then goes on to make a pretty good attempt at summarising the information I need but it’s obviously going to be out-of-date unless it can browse the web live, I am particularly interested in summarising news articles. I thought at first this just might be a temp glitch but I’ve been at it for a couple of days now and no luck. Note – for comparison I tried the same prompt in a Co-Pilot chat session and it worked perfectly. All advice appreciated.

PaulBellow February 27, 2026, 4:39pm 2

Welcome to the community, @UnclePauly!

I believe the AI Engine WP plug-in is just calling Chat Completions endpoint and not using tools.

Have you reached out to the developer to ask for clarification?

UnclePauly March 3, 2026, 5:40pm 3

Thanks for the reply Paul, but it turns out I needed to flick a switch in the AI Engine WordPress plugin dashboard…that switch was “Chatbot Enable “.

Fixed

UnclePauly March 4, 2026, 9:44pm 4

…aaaand I spoke to soon, Open AI – (I’ve selected GPT-5.2) – now tells me >>>>>>>>>>

I need to flag a limitation before proceeding.

I don’t have the ability to conduct live web browsing or access up‑to‑date sources in real time. Because your brief explicitly requires:

Live web searching

Up‑to‑date quotations (preferably within the past year)

Full, explicit URLs

No fabricated quotes

—I cannot fulfil this accurately without risking fabrication, which I won’t do.

OpenAI_Support September 20, 2026, 1:37pm 5

Sorry for the late response.

If you’re experiencing this directly on ChatGPT web or app, try starting a new chat and manually selecting 'Search' from the tools menu.

https://help.openai.com/en/articles/9237897-chatgpt-search.

We’re closing this thread for now. Please contact OpenAI Support with the error details if this issue still persists.

## 批 1

DeepSeek | Research & News (https://www.deepseek.com/en/news/)
citeturn32076search0 [wordlim: 200] Crawled: last week; June 24, 2026DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence February 25, 2026DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference January 28, 2026DeepSeek-OCR 2: Visual Causal Flow January 12, 2026Engram: Conditional Memory via Scalable Lookup December 31, 2025mHC: Manifold-Constrained Hyper-Connections December 2, 2025DeepSeek-V3.2: Pushing the Frontier of Open LLMs November 27, 2025DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning November 1, 2025Linear-Programming-Based Load Balancer (LPLB)October 21, 2025DeepSeek-OCR: Contexts Optical Compression May 14, 2025Insights into DeepSeek-V3: Scaling Challenges & Hardware Reflections

# Research & News

Dedicated to exploring the essence of AGI — driven by curiosity, answering the biggest questions with the longest-term vision.

NewsSeptember 10, 2026 Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.Introducing the smallest model in our new architecture family, with native visual understanding. Designed for greater capability, faster inference, and higher throughput.

NewsApril 24, 2026 DeepSeek-V4 Preview: Entering the Era of Affordable Million-Token Context DeepSeek-V4 Preview is officially live & open-sourced. Welcome to the era of cost-effective 1M context length.NewsDecember 1, 2025 DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models DeepSeek-V3.2 and V3.2-Speciale launch with world-leading reasoning, thinking in tool-use, and gold-medal performance in IMO, CMO, ICPC & IOI 2025.NewsSeptember 29, 2025 Introducing DeepSeek-V3.2-Exp DeepSeek-V3.2-Exp debuts DeepSeek Sparse Attention (DSA) for faster, more efficient training & inference on long context, with API prices cut by 50%+.cite4†NewsSeptember 22, 2025 DeepSeek-V3.1 is now DeepSeek-V3.1-Terminus DeepSeek-V3.1-Terminus improves language consistency, reduces CN/EN mix-ups, and upgrades Code Agent & Search Agent performance. ## Research Index

June 24, 2026DeepSeek-V4: Towards Highly Efficient Million-Token Context IntelligenceFebruary 25, 2026DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM InferenceJanuary 28, 2026DeepSeek-OCR 2: Visual Causal FlowJanuary 12, 2026Engram: Conditional Memory via Scalable LookupDecember 31, 2025mHC: Manifold-Constrained Hyper-ConnectionsDecember 2, 2025DeepSeek-V3.2: Pushing the Frontier of Open LLMsNovember 27, 2025DeepSeekMath-V2: Towards Self-Verifiable Mathematical ReasoningNovember 1, 2025Linear-Programming-Based Load Balancer (LPLB)October 21, 2025DeepSeek-OCR: Contexts Optical CompressionMay 14, 2025Insights into DeepSeek-V3: Scaling Challenges & Hardware Reflections

## 批 2

Empty search results
No results were found for the provided queries

## 批 3

Empty search results
No results were found for the provided queries
