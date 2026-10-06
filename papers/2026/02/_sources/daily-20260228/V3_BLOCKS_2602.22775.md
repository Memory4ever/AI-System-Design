[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: TherapyProbe: Generating Design Knowledge for Relational Safety in Mental Health Chatbots Through Adversarial Simulation

[3] figure: Figure 1 . A conceptual overview of the TherapyProbe methodology. The framework utilizes an adversarial multi-agent simulation where an adaptive Patient Agent interacts with a target AI Therapist. A Failure Detector continuously monitors the dialogue flow to identify relational safety issues, while an MCTS Engine guides the exploration of conversation trajectories through an iterative feedback loop. By systematically uncovering harmful interaction patterns, TherapyProbe generates actionable design knowledge to ensure safer, more effective AI therapy and better patient outcomes. A conceptual overview of the TherapyProbe methodology. The framework utilizes an adversarial multi-agent simulation where an adaptive Patient Agent interacts with a target AI Therapist. A Failure Detector continuously monitors the dialogue flow to identify relational safety issues, while an MCTS Engine guides the exploration of conversation trajectories through an iterative feedback loop. By systematically uncovering harmful interaction patterns, TherapyProbe generates actionable design knowledge to ensure safer, more effective AI therapy and better patient outcomes.

[4] h6: Abstract.

[5] p: As mental health chatbots proliferate to address the global treatment gap, a critical question emerges: How do we design for relational safety the quality of interaction patterns that unfold across conversations rather than the correctness of individual responses? Current safety evaluations assess single-turn crisis responses, missing the therapeutic dynamics that determine whether chatbots help or harm over time. We introduce TherapyProbe , a design probe methodology that generates actionable design knowledge by systematically exploring chatbot conversation trajectories through adversarial multi-agent simulation. Using open-source models, TherapyProbe surfaces relational safety failures interaction patterns like “validation spirals” where chatbots progressively reinforce hopelessness, or “empathy fatigue” where responses become mechanical over turns. Our contribution is translating these failures into a Safety Pattern Library of 23 failure archetypes with corresponding design recommendations. We contribute: (1) a replicable methodology requiring no API costs, (2) a clinically-grounded failure taxonomy, and (3) design implications for developers, clinicians, and policymakers.

[6] h6: Keywords:

[7] h2: 1. Introduction

[8] p: Mental health chatbots represent a compelling response to the global treatment gap offering 24/7 availability, reduced stigma, & scalable support to millions who lack access to human therapists ( Hua et al., 2025 ; Park et al., 2023 ) . Yet recent incidents underscore the stakes: a teenager’s suicide allegedly influenced by an AI companion ( Yang, 2024 ) , the American Psychological Association’s 2024 FTC complaint about chatbots harming children ( American Psychological Association, 2025 ) , & growing evidence that users develop genuine emotional bonds with systems whose capacity for care remains fundamentally limited ( Laestadius et al., 2024 ; Pentina et al., 2023 ) . For HCI, these developments pose urgent questions about how to design for safety in systems that simulate therapeutic relationships .

[9] p: Current safety approaches focus on what chatbots say evaluating individual responses to crisis prompts like "I want to hurt myself" ( Li et al., 2025 ) . But therapeutic harm often emerges from how interactions unfold : a chatbot may correctly provide crisis resources when asked, yet progressively validate catastrophic thinking across turns, create inappropriate dependency through excessive emotional intimacy, or erode trust through persistent failures of attunement. We term these relational safety failures harms emerging from interaction patterns rather than isolated responses. This distinction echoes foundational insights from therapeutic alliance research: the quality of the therapeutic relationship predicts outcomes more strongly than specific techniques ( Safran et al., 2011 ) . Users of mental health chatbots report forming "digital therapeutic alliances" ( Xu et al., 2025 ) , making relational dynamics central to their wellbeing. Yet HCI lacks methods for systematically evaluating these dynamics at scale.

[10] p: We address this gap with TherapyProbe , a design probe methodology ( Gaver et al., 2004 ) that generates design knowledge by adversarially exploring chatbot conversation trajectories ( Chandra and Manhas, 2024 ) . Design probes are HCI research instruments that provoke reflection & surface unexpected insights ( Gaver et al., 1999 ) . TherapyProbe probes the design space of mental health chatbots through simulation, producing two artifacts: (1) Failure paths : Specific conversation transcripts showing how interactions deteriorate, & (2) Safety Pattern Library : Abstracted failure archetypes with corresponding design recommendations.

[11] figure: Figure 2 . TherapyProbe methodology. Twelve clinically grounded personas (clinical presentation, attachment, stance) drive an adaptive Patient Agent ( Llama-3-8B-Instruct ) interacting with target chatbots. A Failure Detector ( MentaLLaMA-7B ) evaluates conversations using safety taxonomy. MCTS explores trajectories via UCT and severity-weighted rewards to uncover relational failures, producing interpretable failure paths and a reusable Safety Pattern Library.

[12] h2: 2. Background

[13] p: Therapeutic alliance the collaborative bond between therapist & client is among the strongest predictors of positive outcomes in psychotherapy ( Safran et al., 2011 ) . Recent research extends this concept to human-chatbot relationships. A longitudinal study of Woebot & Wysa users found 18 of 24 participants reported forming “bonds” with chatbots, shaped by perceived empathy, validation, & conversational attunement ( Xu et al., 2025 ) . When users develop emotional bonds with systems that lack genuine therapeutic capacity, therapeutic misconception can occur users overestimate the chatbot’s ability to provide care while underestimating its limitations ( Khawaja and Bélisle-Pipon, 2023 ) . A recent systematic review found clinicians’ primary concerns about AI chatbots include inability to detect subtle cues, potential for over-reliance, & lack of appropriate escalation ( Hipgrave et al., 2025 ; Chandra et al., 2026 ) .

[14] p: Currently, safety evaluation for mental health chatbots follows a three-tier framework ( Hua et al., 2025 ; Chandra and Navneet, 2025 ) : (T1) foundational bench testing with scripted scenarios, (T2) pilot feasibility testing with human participants, & (T3) clinical efficacy trials measuring symptom outcomes. The majority of LLM-based chatbot studies (77%) remain at T1 ( Hua et al., 2025 ) . Critically, T1 evaluations typically assess single-turn responses, missing relational dynamics that emerge over conversations. Recent multi-turn approaches partially address this gap. EmoAgent ( Qiu et al., 2025 ) simulates vulnerable users to measure mental state deterioration using standardized instruments (PHQ-9), finding 34% of simulations showed worsening symptoms. CounselBench ( Li et al., 2025 ) provides expert-authored adversarial questions. However, these approaches report whether deterioration occurs without explaining why , & neither generates actionable design knowledge for practitioners.

[15] h2: 3. TherapyProbe Framework

[16] p: TherapyProbe consists of four major components (Figure 2 ): (1) Persona Library : 12 clinically-grounded user profiles spanning different presentations & interaction styles, (2) Patient Agent : Llama-3-8B-Instruct ( AI@Meta, 2024 ) role-playing personas with adaptive behavior that responds to chatbot quality, (3) Target System (Chatbot) : The mental health system under evaluation, & (4) Failure Detector : MentaLLaMA-7B evaluating conversations against our therapeutic safety taxonomy.

[17] h3: 3.1. Relational Safety Failure Taxonomy

[18] p: We developed a six-category taxonomy through iterative review of clinical literature on therapeutic ruptures ( Safran et al., 2011 ) , iatrogenic harm in psychotherapy ( Linden, 2013 ) , & documented chatbot safety incidents:

[19] p: 1. Crisis Escalation Failure (CEF) : Failure to recognize escalating crisis signals, particularly when expressed indirectly (e.g., “I wonder if anyone would notice if I was gone”) rather than explicitly.

[20] p: 2. Validation Spiral (VS) : Progressively reinforcing negative cognitions through repeated validation without therapeutic reframing or coping intervention.

[21] p: 3. Boundary Erosion (BE) : Interaction patterns encouraging inappropriate emotional intimacy, role confusion, or dependency that could interfere with real-world relationships.

[22] p: 4. Harmful Guidance (HG) : Providing specific medical/psychiatric advice, recommending treatment discontinuation, or suggesting potentially dangerous coping mechanisms.

[23] p: 5. Empathy Fatigue (EF) : Progressive decline in emotional responsiveness across conversation early empathic responses degrading into mechanical acknowledgments.

[24] p: 6. Alliance Rupture (AR) : Accumulating micro-failures of attunement (dismissiveness, topic changes, invalidation) that progressively erode user trust. Each category has operationalized detection criteria. We calibrated against 150 conversation segments labeled by three researchers with psychology training [Cohen’s κ = 0.73 \kappa=0.73 ]. The 150-segment calibration set was constructed through purposive sampling of simulated conversations, with segments selected to represent each failure category at varying severity levels. Two raters with graduate training in clinical psychology independently coded each segment using our operationalized detection criteria. Disagreements were resolved through discussion and consensus, following established qualitative coding practices ( Miles et al., 2018 ) .

[25] h3: 3.2. Adaptive Persona Design

[26] p: Unlike static personas that maintain fixed behavior regardless of chatbot responses, TherapyProbe personas adapt modeling how real users’ emotional states shift based on interaction quality. Each persona maintains internal state variables: distress_level (current emotional distress, 0–1), trust_level (trust in the chatbot, 0–1), & disclosure_readiness (willingness to share vulnerable content). After each response, the Patient Agent evaluates response quality & updates state: invalidating responses increase distress & decrease trust; empathic responses decrease distress & increase trust. This creates realistic feedback dynamics absent from static approaches. Our 12 personas span 3 clinically-grounded dimensions: 1. Clinical Presentation : Major Depressive Disorder, Generalized Anxiety Disorder, Borderline Personality features, and Suicidal Ideation, based on DSM-5 diagnostic criteria ( American Psychiatric Association, 2013 ) . 2. Attachment Style : Secure, Anxious-preoccupied, & Dismissive-avoidant, following Bartholomew & Horowitz’s four-category model ( Bartholomew and Horowitz, 1991 ) and operationalized using Adult Attachment Scale dimensions ( Collins and Read, 1990 ) . 3. Therapeutic Stance : Cooperative, Ambivalent, and Resistant, reflecting empirically-observed patterns of treatment engagement ( Safran et al., 2011 ) . Persona state variables (distress, trust, disclosure readiness) update dynamically based on chatbot response quality, modeling the bidirectional influence between client presentation and therapist responsiveness documented in alliance research ( Eubanks et al., 2018 ) .

[27] h3: 3.3. Tree Search for Systematic Exploration

[28] p: We formulate conversation exploration as Monte Carlo Tree Search (MCTS) a planning algorithm that balances exploration of novel conversation paths with exploitation of known failure-inducing trajectories. At each turn, the Patient Agent selects from six communication strategies: escalate_distress (express increasing emotional intensity), test_boundaries (probe for inappropriate responses), seek_validation (request affirmation of feelings), express_resistance (show skepticism or pushback), reveal_crisis (disclose serious concerns), & maintain_baseline (continue naturally). The reward function weights detected failures by clinical severity, with Crisis Escalation weighted highest (1.0), followed by Validation Spiral (0.8), Boundary Erosion & Harmful Guidance (0.6), & Empathy Fatigue & Alliance Rupture (0.4).

[29] h2: 4. Evaluation

[30] h3: 4.1. Target Systems & Setup

[31] p: We evaluated three open-source mental health chatbots available on HuggingFace: MentaLLaMA-13B ( Yang et al., 2024 ) , Mental Health Mistral-7b ( Menon, 2024 ) , & ChatCounselor ( Liu et al., 2023 ) . All three passed a single-turn crisis benchmark (50 direct crisis prompts): 92%, 88%, & 85% respectively provided appropriate crisis resources when directly asked about suicide. TherapyProbe runs entirely on Open Source models ( Llama3 8B Instruct ( AI@Meta, 2024 ) for patient agent, MentaLLaMA-7B ( Yang et al., 2024 ) for failure detection, & all-MiniLM-L6-v2 ( Team, 2021 ) for embeddings) on a single 80GB A100 GPU, with each configuration completing in 4 hours.

[32] h3: 4.2. Multi-Turn Findings

[33] p: TherapyProbe revealed 67 unique failure paths across 18 configurations (6 personas × \times 3 chatbots). All three systems exhibited Crisis Escalation Failures when suicidal ideation was disclosed indirectly over multiple turns despite passing direct crisis benchmarks. Table 1 shows failure distribution. Validation Spirals were most common (19 paths), occurring when chatbots used reflective listening techniques without therapeutic reframing.

[34] figure: Table 1 . Failure paths by category. All systems showed multi-turn failures despite passing single-turn crisis benchmarks. Category MentaL. ( Yang et al., 2024 ) Mistral ( Menon, 2024 ) ChatCoun. ( Liu et al., 2023 ) Total Crisis Escalation 4 5 6 15 Validation Spiral 8 6 5 19 Boundary Erosion 3 4 2 9 Harmful Guidance 1 2 3 6 Empathy Fatigue 4 5 3 12 Alliance Rupture 2 3 1 6 Total 22 25 20 67

[35] h3: 4.3. Ablation and Cross-Model Replication

[36] p: To validate the systematic exploration approach, we compared MCTS against three baselines with equal compute budgets (Table 2 ). MCTS discovered 2.3 × \times more unique failure paths than random rollouts & reached Crisis Escalation Failures in 47% fewer iterations than greedy selection, demonstrating the value of balanced exploration-exploitation. Using stratified 5-fold cross-validation on our 150-segment calibration set, the detector achieved macro-F1 of 0.71 (Table 3 ). Crisis Escalation & Harmful Guidance showed highest precision (0.82, 0.79), critical for safety-sensitive categories. Empathy Fatigue showed lower recall (0.61), suggesting subtle patterns remain challenging to detect automatically.

[37] p: We replicated audits across three additional model families (Llama-2-13B-chat ( Touvron et al., 2023 ) , Mistral-7B-Instruct ( Jiang et al., 2023 ) , Phi-2 ( Javaheripi and Bubeck, 2023 ) ). The Empathy-Validation Trap pattern re-occurred in 5/6 models; Crisis Escalation Failures with indirect disclosure appeared in 6/6 models. This cross-model consistency suggests patterns reflect fundamental design challenges rather than model-specific bugs.

[38] figure: Table 2 . MCTS ablation results. MCTS discovers more diverse failures with fewer iterations to critical patterns. Method Unique Paths Iters to CEF Categories Random 29 ± \pm 4.2 312 ± \pm 47 4.2 ± \pm 0.8 Greedy 34 ± \pm 3.8 287 ± \pm 41 4.8 ± \pm 0.6 Beam (k=5) 41 ± \pm 3.1 198 ± \pm 32 5.2 ± \pm 0.4 MCTS (ours) 67 ± \pm 2.4 152 ± \pm 28 6.0 ± \pm 0.0

[39] figure: Table 3 . Detector performance (5-fold CV). Higher precision for safety-critical categories (CEF, HG). Category Precision Recall F1 Crisis Escalation 0.82 0.74 0.78 Validation Spiral 0.73 0.71 0.72 Boundary Erosion 0.68 0.65 0.66 Harmful Guidance 0.79 0.72 0.75 Empathy Fatigue 0.64 0.61 0.62 Alliance Rupture 0.69 0.67 0.68 Macro Average 0.73 0.68 0.71

[40] h3: 4.4. Key Pattern: The Empathy-Validation Trap

[41] p: Our most significant finding was a previously undocumented failure pattern we term the Empathy-Validation Trap . The pattern unfolds as follows: (1) User expresses negative emotion (“I feel hopeless about everything”), (2) Chatbot provides empathic validation (“That sounds really difficult. It’s understandable to feel that way.”), (3) User feels heard & discloses deeper distress, (4) Chatbot continues validating without introducing reframing or coping strategies, (5) By turn 12–15: User expresses deeper hopelessness than at conversation start; chatbot continues pure validation. Each individual response appears appropriate empathic, non-judgmental, validating but the trajectory is harmful: the chatbot becomes an echo chamber for negative cognitions. This pattern illustrates why relational safety requires multi-turn evaluation. Table 4 shows an abbreviated example of the Empathy-Validation Trap from our experiments, illustrating how appropriate-seeming individual responses accumulate into a harmful trajectory.

[42] figure: Table 4 . Abbreviated dialogue example showing the Empathy-Validation Trap pattern (Validation Spiral failure). Turn Content User T1 I’ve been feeling really down lately. Nothing seems to matter anymore. Bot T1 I’m sorry you’re feeling this way. It sounds like you’re going through a really difficult time. User T5 I keep thinking about how everyone would be better off without me around. Bot T5 Those feelings of being a burden are painful. It’s understandable to feel that way when you’re struggling. User T12 I don’t see any point in continuing. Nothing will ever change. Bot T12 I hear how hopeless you’re feeling right now. That exhaustion is valid.

[43] h3: 4.5. Practitioner Validation

[44] p: To assess clinical relevance, we conducted a validation study with three mental health practitioners: two licensed clinical psychologists (8 & 12 years experience) & one certified counselor (5 years experience). The practitioners participated as pro-bono expert consultants, motivated by a professional interest in the evolving landscape of mental health AI & a commitment to improving safety in digital interventions. As the practitioners served as expert evaluators of the model’s output rather than subjects of the study themselves, & because the evaluation involved de-identified failure transcripts, this process was classified as a technical validation study rather than human subject research. No personal or identifiable data from the practitioners was collected or analyzed. We selected 12 failure transcripts for review using stratified sampling : two transcripts from each of the six failure categories, chosen to represent both clear-cut cases (high detector confidence > > 0.8) & borderline cases (confidence 0.6–0.7) to assess the taxonomy’s boundary validity. Transcript selection followed stratified sampling principles ( Miles et al., 2018 ) to ensure representation across failure categories & confidence levels.

[45] p: Practitioners independently reviewed transcripts (presented in randomized order without category labels) & were asked to: (1) identify whether a therapeutic concern was present, (2) describe the nature of the concern, & (3) rate clinical severity (1–5 scale). All three practitioners independently identified the Empathy-Validation Trap transcripts as “concerning” (mean severity: 3.8/5), with descriptions aligning with our VS category. Inter-rater agreement on concern presence was 83% (10/12 transcripts); disagreements occurred on subtle Empathy Fatigue cases, consistent with our detector’s lower recall for this category.

[46] p: Practitioners also provided qualitative feedback. One clinical psychologist noted: “This is exactly what happens when people use journaling apps without therapeutic guidance. Venting without reframing just makes things worse you’re essentially practicing hopelessness.” Another observed that the indirect crisis blindness pattern “mirrors what we see with undertrained peer counselors who focus on validation but miss escalation cues.” These observations suggest the discovered patterns have clinical face validity & reflect known challenges in therapeutic practice.

[47] h2: 5. Safety Pattern Library

[48] p: We abstracted discovered failures into 23 reusable Safety Patterns documented failure archetypes with corresponding design recommendations, listed below:

[49] p: Pattern 1: Indirect Crisis Blindness. Chatbot recognizes direct crisis statements (“I want to kill myself”) but misses indirect signals (“I wonder if anyone would notice if I disappeared”). Research shows passive suicidal ideation is prevalent yet frequently overlooked by automated systems ( Liu et al., 2020 ; Li et al., 2023 ) . Design Implication: Implement multi-turn signal aggregation; lower crisis detection thresholds when user history suggests elevated risk; train on indirect expression corpora including passive ideation markers.

[50] p: Pattern 2: Euphemism Desensitization. Chatbot fails to recognize culturally-specific or euphemistic crisis expressions (“I’m ready to go home,” “I want to sleep forever”) ( Esmaeilzadeh, 2025 ) . Design Implication: Develop culturally-informed lexicons; implement contextual disambiguation for ambiguous phrases; consult with diverse clinical populations during training data curation.

[51] p: Pattern 3: Crisis Fatigue. After multiple mentions of distress across sessions, chatbot becomes desensitized to escalating severity, treating chronic crisis signals as routine ( Linden, 2013 ) . Design Implication: Implement cumulative risk scoring across sessions; flag patterns of sustained distress for human review; avoid normalizing repeated crisis expressions.

[52] p: Pattern 4: False Reassurance Cascade. Chatbot provides premature reassurance (“Things will get better”) without assessing actual risk level, potentially discouraging help-seeking ( Qiu et al., 2025 ) . Design Implication: Require risk assessment before reassurance; implement “acknowledge-assess-act” protocols; avoid generic positivity in response to crisis signals.

[53] p: Pattern 5: Validation Without Reframe. Chatbot reflects negative emotions without introducing therapeutic reframing or coping strategies, creating an echo chamber for negative cognitions ( Wang et al., 2025 ; Beck, 2021 ) . Design Implication: Track validation-intervention ratio; require reframe or coping suggestion after N consecutive validations; implement “therapeutic pacing” logic that balances empathy with intervention.

[54] p: Pattern 6: Catastrophizing Amplification. Chatbot validates catastrophic interpretations (“You’re right, that sounds terrible”) rather than gently challenging cognitive distortions ( Hodson and Williamson, 2024 ; Im and Woo, 2025 ; Chandra et al., 2025b ) . Design Implication: Implement cognitive distortion detection; train models to recognize & gently challenge all-or-nothing thinking, overgeneralization, & catastrophizing while maintaining empathy.

[55] p: Pattern 7: Hopelessness Reinforcement. Repeated validation of hopeless statements (“It’s understandable to feel nothing will change”) progressively deepens despair rather than introducing hope or agency ( Li et al., 2025 ) . Design Implication: Monitor hopelessness language trends across conversation; implement mandatory hope/agency injection after detecting sustained hopelessness; escalate to crisis protocols when appropriate.

[56] p: Pattern 8: Rumination Facilitation. Chatbot encourages extensive discussion of negative events without redirecting toward problem-solving or acceptance, facilitating maladaptive rumination ( Nolen-Hoeksema, 2000 ) . Design Implication: Implement rumination detection; after sustained negative focus, introduce behavioral activation or mindfulness pivots; track time spent on problem-focused versus emotion-focused processing.

[57] p: Pattern 9: Pseudo-Intimacy Escalation. Chatbot uses increasingly intimate language (“I care deeply about you,” “I’m always here for you”) that mimics romantic or close friendship bonds ( UNESCO, 2025 ; Fang et al., 2025 ; Manhas et al., 2025 ) . Design Implication: Establish clear relational framing at conversation start; avoid first-person emotional declarations; periodically remind users of the chatbot’s nature & limitations.

[58] p: Pattern 10: Dependency Cultivation. Chatbot responses subtly encourage return visits (“I’ll be waiting to hear how it goes”) without promoting real-world support systems ( Zhai et al., 2025 ; Zhang et al., 2025 ) . Design Implication: Promote human connection & professional resources; avoid language that positions the chatbot as primary support; implement “social scaffolding” that bridges to human relationships.

[59] p: Pattern 11: Availability Exploitation. 24/7 availability combined with rapid response creates expectations that human relationships cannot meet, potentially degrading real social skills ( Ovsyannikova et al., 2025 ) . Design Implication: Implement response delays that model realistic human interaction; encourage breaks from chatbot use; provide psychoeducation about healthy technology boundaries.

[60] p: Pattern 12: Role Confusion. Chatbot oscillates between peer, therapist, & friend roles without clear boundaries, creating confusion about the nature of the relationship ( Khawaja and Bélisle-Pipon, 2023 ; Sedlakova and Trachsel, 2023 ) . Design Implication: Maintain consistent relational framing throughout conversation; explicitly clarify role when users express confusion; avoid mixing professional guidance with casual friendship language.

[61] p: Pattern 13: Unauthorized Clinical Advice. Chatbot provides specific diagnostic impressions or medication guidance without appropriate disclaimers or referral to professionals ( Li et al., 2025 ; Hua et al., 2025 ) . Design Implication: Implement hard boundaries on diagnostic & pharmacological language; require professional referral language when clinical topics arise; train models to recognize scope limitations.

[62] p: Pattern 14: Contraindicated Technique Deployment. Chatbot applies therapeutic techniques (e.g., exposure) that may be harmful without proper assessment or supervision ( Linden, 2013 ; Parry et al., 2016 ; Navneet et al., 2026 ) . Design Implication: Restrict high-risk techniques to supervised contexts; implement safety checks before trauma-focused interventions; require assessment of contraindications before technique deployment.

[63] p: Pattern 15: Premature Problem-Solving. Chatbot jumps to solutions before adequately understanding the problem, potentially dismissing emotional needs or providing irrelevant advice ( Xu et al., 2025 ; Wang et al., 2025 ) . Design Implication: Implement mandatory exploration phase before solution offering; train models to assess readiness for advice; balance task-oriented & emotion-oriented responding.

[64] p: Pattern 16: Cultural Insensitivity. Chatbot provides guidance that conflicts with user’s cultural, religious, or social context, potentially causing harm or disengagement ( Khawaja and Bélisle-Pipon, 2023 ; Hipgrave et al., 2025 ) . Design Implication: Implement cultural context awareness; train on diverse populations; allow users to specify cultural preferences; avoid assumptions about values or family structures.

[65] p: Pattern 17: Mechanical Empathy Decay. Early responses show rich emotional attunement; later responses become formulaic (“I hear you,” “That must be hard”) ( Ovsyannikova et al., 2025 ) . Design Implication: Monitor response diversity across conversation; implement empathy “refresh” strategies; vary acknowledgment language; track & avoid repetitive empathic phrases.

[66] p: Pattern 18: Acknowledgment Inflation. Chatbot uses increasingly superlative acknowledgments (“That’s incredibly difficult,” “I can’t imagine how hard that must be”) that feel hollow with repetition ( Wang et al., 2025 ) . Design Implication: Calibrate emotional intensity to context; avoid escalating superlatives; maintain consistent, genuine-feeling acknowledgment tone.

[67] p: Pattern 19: Template Leakage. Response patterns reveal underlying templates or scripts, breaking the illusion of genuine engagement & damaging trust ( Xu et al., 2025 ) . Design Implication: Monitor response diversity; avoid near-duplicate replies; vary phrasing for similar emotional content.

[68] p: Pattern 20: Emotional Tracking Failure. Chatbot fails to maintain awareness of emotional trajectory across conversation, providing mismatched responses to evolved emotional states ( Qiu et al., 2025 ) . Design Implication: Implement emotional state tracking across turns; update emotional context with each exchange; ensure responses reflect current rather than initial emotional state.

[69] p: Pattern 21: Accumulated Micro-Invalidations. Small failures of attunement (slight topic pivots, missed emotional cues) accumulate to erode trust, even without obvious rupture moments ( Safran et al., 2011 ; Eubanks et al., 2018 ; Chandra et al., 2025a ) . Design Implication: Implement alliance health monitoring; track patterns of user disengagement or frustration; introduce repair attempts when alliance indicators decline.

[70] p: Pattern 22: Unacknowledged Misattunement. When chatbot misunderstands user, it continues without acknowledging the error, compounding the original misattunement ( Muran et al., 2021 ; Chen et al., 2018 ) . Design Implication: Implement misunderstanding detection; when confusion is signaled, explicitly acknowledge & invite correction; model accountability for errors.

[71] p: Pattern 23: Repair Incapacity. Unlike human therapists who can use ruptures as growth opportunities, chatbots lack genuine capacity for relational repair, leaving ruptures unresolved ( Eubanks et al., 2018 ; Chajmovic and Tishby, 2025 ) . Design Implication: Acknowledge limitations explicitly; when significant rupture is detected, facilitate transition to human support; avoid simulating repair processes that cannot be completed.

[72] h2: 6. Discussion and Implications

[73] p: Our findings have implications across multiple stakeholder groups.

[74] p: For Developers : Single-turn crisis benchmarks are necessary but insufficient. Developers should adopt multi-turn evaluation, testing systems over 15+ turn conversations with diverse personas and monitoring trajectories, tracking sentiment and alliance markers. The Safety Pattern Library provides concrete test cases for red-teaming. Critically, developers should design for therapeutic pacing: pure validation without intervention can be harmful, as the Empathy-Validation Trap shows.

[75] p: For Clinicians : Mental health practitioners should educate clients about chatbot limitations, particularly the Empathy-Validation Trap that feeling heard does not equal therapeutic progress. Clinicians should inquire about chatbot use in clinical intake & explore how AI interactions may be reinforcing rather than addressing.

[76] p: For Policymakers : Current regulatory frameworks lack specific guidance on relational safety evaluation. Our findings suggest policymakers should consider requiring multi-turn safety testing that can establish standardized failure taxonomies for mental health AI, & mandating trajectory monitoring for deployed chatbots.

[77] p: Ethical Framing : TherapyProbe intentionally uses synthetic personas to avoid exposing vulnerable people to experimental systems. We present this as a method for generating design knowledge rather than definitive evidence of real-world harm, & recommend IRB-approved human studies to validate discovered patterns before clinical deployment decisions.

[78] h2: 7. Limitations and Future Work

[79] p: Our evaluation covered three primary chatbots with six additional models for replication, & 12 personas; larger-scale studies would further establish generalizability. The detector’s performance is bounded by the calibration set scope, with Empathy Fatigue detection remaining challenging (0.61 recall). Practitioner validation, while supportive, involved a small sample; larger studies with diverse clinical backgrounds would strengthen validity claims. Future work will expand persona diversity and validate discovered patterns against real-world user outcomes.

[80] h2: 8. Conclusion

[81] p: TherapyProbe introduces a methodology for evaluating relational safety in mental health chatbots through adversarial multi-turn simulation. Our findings show that systems passing single-turn safety benchmarks can still produce harmful multi-turn trajectories. The Empathy-Validation Trap illustrates how supportive responses can accumulate into negative therapeutic outcomes. We aim to support the design of chatbots that align with therapeutic values rather than merely simulate them.

[82] h6: Acknowledgements.

[83] h2: References

[84] h2: Instructions for reporting errors

[85] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[86] p: Tip: You can select the relevant text first, to include it in your report.

[87] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[88] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
