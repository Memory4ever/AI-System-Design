# Exact-v1 necessary primary excerpts — 2601.19786

Preserved original responses; local L labels are scoped to each response. No revised-version or unrelated appendix sweep.

## Original response 1: jan29_stdnext5head

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28451view2 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19786v1","lineno":null}); Total lines: 322

## Original response 2: jan29_stdnext5core

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28453view2 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"turn28451view2","lineno":78}); Total lines: 322
L60: Despite the significant progress brought by DSRTs, the representation of a speaker’s accent is largely overlooked in the design, evaluation, and application of the tokens. Prior user perception studies have demonstrated a similarity–attraction effect, whereby listeners prefer accents similar to their own in spoken interaction (dahlback2007similarity).
L61: Unfortunately, ZS-TTS systems are shown to hallucinate accents that differ from those of the reference speaker (zhong2025accentbox), while spoken dialogue systems still lack broad adoption of benchmarks or evaluation settings that consider appropriate, accent-controlled speech generation (cheng2025voxdialogue).
L62: Although some recent zero-shot TTS (ZS-TTS) systems have demonstrated some ability to mimic or control the accent of generated speech using discrete speech representation tokens (DSRTs), how much accent information is encoded in these tokens remains unexplored (du2024cosyvoice; zhang2025vevo; wang2025maskgct). Existing claims – such as that naive codebook size adjustment (zhang2025vevo) or ASR supervision (du2024cosyvoice) can facilitate controlled accent generation – lack systematic investigation.
L63: To this end, we ask the following research questions: (1) How do different design choices in DSRTs influence the amount of accent information they encode? (2) How can these insights be leveraged to enable more controllable accent generation, e.g. in voice conversion (VC)?
L64: Existing DSRT evaluation frameworks focus on phonetic and speaker information and rarely consider accent (polyak2021speech). We extend the investigation of accessibility to accent information, with an accent ABX method we proposed that evaluates the discriminability of representations for words uttered in different accents.
L65: Additionally, we propose to evaluate the recoverability of accent, speaker, and phonetic information by cross-accent VC, resynthesising from DSRTs from source speakers and speaker IDs from target speakers of different accents. Using the proposed framework, we observe the following key findings: (1) Accent information is most prominent in mid-early layers of HuBERT, different from speaker or phonetic information distribution.
L66: (2) Naive adjustment of codebook sizes provides only very limited disentanglement of accent, speaker and content information. (3) Predominant design of DSRTs for speech generation (quantising a later layer in a speech representation model, or using ASR supervison) discards most accent information.
L67: Our main contributions are:
L68: 
L69:   * •
L70: 
L71: To the best of our knowledge, this is the first work to incorporate accent in evaluating DSRTs, and to apply ABX to a study of accent.
L72: 
L73:   * •
L74: 
L75: Based on our findings, we propose quantisation schemes that are appropriate for accent-preserving VC – preserving source speaker accent – and accent-adaptive VC – adapting to target speaker accent – which achieve superior performance to existing approaches.
L76: 
L77:   * •
L78: Evaluation pipeline and proposed DSRTs will be open-sourced in the future.
L79: 
L80: cite36†Image: Refer to caption Figure 1: Proposed pipeline for evaluating the recoverability and accessibility of accent, speaker, and phonetic information in various Discrete Speech Representation Tokens (DSRTs).
L81: ## 2 Related Work
L82: ### 2.1 Discrete Speech Tokens
L83: Discrete speech tokens can be largely categorised into two groups: semantic tokens^{1}^{1} 1 A severe misnomer as these tokens contain primarily phonetic information and little semantic information (wells2022phonetic; choi2024self). and acoustic tokens. We refer to semantic tokens as Discrete Speech Representation Tokens (DSRTs) here, naming them strictly by how these tokens are designed and trained, rather than what information some researchers assume them to possess.
L84: DSRTs are tokens obtained by quantising learned speech representations, such as HuBERT (hsu2021hubert) and w2v-BERT (chung2021w2vbert); while acoustic tokens are obtained by quantising waveforms.
L85: Common quantisation techniques include k-means, Vector Quantisation (VQ) (vandenoord2017neural), Residual Vector Quantisation (RVQ) (zeghidour2021soundstream), and Finite-State Quantisation (FSQ) (mentzer2024finite), with k-means, VQ, and FSQ primarily used for DSRTs, VQ and RVQ primarily used for acoustic tokens.
L86: ### 2.2 Investigation of Speech Representations
L87: 
L88: In terms of of continuous speech representations, most previous work has focused on accessibility, finding that phonetic information peaks in intermediate layers, while acoustic information dominates earlier layers (choi2024self; pasad2021layer). After finetuning on the ASR task, it has been observed deeper layers become dominated by task-specific information, exhibiting higher phonetic discrimination.
L89: In the investigation of DSRTs, wells2022phonetic find that DSRTs obtained by k-means on hubert-base-ls960 correspond to sub-phonetic events. yeh2024estimating, using their information completeness and accessibility framework, found that DSRTs obtained from hubert-base-ls960 layer 4 contain more accessible pitch and speaker information, but less accessible phone information, than layer 9.
L90: Phonetic and speaker information in both layers consistently decrease with lower bitrates of RVQ codes, refuting claims that content and speaker disentanglement can be achieved by VQ.
L91: ### 2.3 DSRTs in ZS-TTS and SpeechLMs
L92: In ZS-TTS, researchers found that DSRTs provide more accessible phonetic information than acoustic tokens do, while suffering information loss such as timbre and acoustic environment (wang2025maskgct). Motivated by such findings, many state-of-the-art (SOTA) models utilise a hierarchical approach, first predicting DSRTs from text or source speech and then predicting acoustic tokens from DSRTs (du2024cosyvoice; lee2025hierspeechpp; wang2025maskgct; zhang2025vevo).
L93: In SpeechLMs, researchers seek to combine DSRTs with acoustic tokens for both accessible and complete/recoverable information, such as SpeechTokenizer (zhang2024speechtokenizer) and Mimi tokeniser (defossez2024moshi).
L94: When designing such DSRTs, ZS-TTS researchers have claimed that are unverified or even contradicted by speech representation investigations. zhang2025vevo choose layer 18 of hubert-large-ll60k and claim that reducing the codebook size in VQ leads to natural disentanglement of speaker, style (accent and emotion by their definition) and content, with a codebook size of 32 containing only content, and a codebook size of 8,192 containing only content and style.
L95: This claim not only contradicts the findings of yeh2024estimating that VQ or k-means with 1024 codebook size still retain significant speaker information, but also lacks verification in terms of accent and emotion. du2024cosyvoice propose to use “supervised semantic token”, obtained by injecting FSQ in an internal ASR model encoder; how ASR pretraining affects the information in discrete tokens remains unclear.
L96: ### 2.4 Accent Control and Generation
L97: Unfortunately, ZS-TTS speech generation systems suffer accent hallucination, whereby they generate a hallucinated synthetic accent that deviates from the reference or prompt speech (zhong2025accentbox). Recent systems that have been specially built for accent generation have not yet utilised DSRTs along with powerful LLM architectures (zhong2025accentbox; xinyuan2025scalable).
L98: General ZS-TTS systems are reported to have certain accent control capabilities, but there has been little or no investigation about accent information in DSRTs. Understanding how accent information is encoded could help build more inclusive ZS-TTS systems for diverse accents.
L99: ### 2.5 ABX Evaluation
L100: 
L101: The ABX error rate is a distance-based, model-agnostic evaluation metric, assessing whether the representations pull data of the same category (e.g. sample $x=$ \textipa[bIt], another sample $a=$ \textipa[bIt], of the same triphone category) closer and push dissimilar data (e.g. $x=$ \textipa[bIt], $b=$ \textipa[bi:t]) farther in representational space.
L102: Previous work introduced Minimal Pair ABX (MP-ABX) (schatz2013evaluating), where instances differ only in a central phonetic unit while sharing the same phonetic context. Prior studies (borsos2023audiolm; wang2025maskgct; zhang2025vevo) have used this metric to assess the phonetic discriminability of DSRT tokens. In addition, ABX has been extended to probe speaker-related information by defining triplets that contrast speaker identity under controlled linguistic content (de2022language).
L103: Nevertheless, to the best of our knowledge, no prior work has systematically employed machine ABX to reveal accent discriminability in speech representations or DSRTs.
L104: ## 3 Method
L105: Inspired by the perspective of separately measuring information completeness and accessibility yeh2024estimating, we focus on evaluating DSRTs from both aspects, but in the context of accent generation. Since completeness cannot be measured by resynthesis, we introduce recoverability as a task-grounded measure of how much accent, speaker, and phonetic information encoded in DSRTs can be recovered in resynthesised speech.

## Original response 3: jan29_stdnext5eval

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28454view2 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"turn28451view2","lineno":105}); Total lines: 322
L93: In SpeechLMs, researchers seek to combine DSRTs with acoustic tokens for both accessible and complete/recoverable information, such as SpeechTokenizer (zhang2024speechtokenizer) and Mimi tokeniser (defossez2024moshi).
L94: When designing such DSRTs, ZS-TTS researchers have claimed that are unverified or even contradicted by speech representation investigations. zhang2025vevo choose layer 18 of hubert-large-ll60k and claim that reducing the codebook size in VQ leads to natural disentanglement of speaker, style (accent and emotion by their definition) and content, with a codebook size of 32 containing only content, and a codebook size of 8,192 containing only content and style.
L95: This claim not only contradicts the findings of yeh2024estimating that VQ or k-means with 1024 codebook size still retain significant speaker information, but also lacks verification in terms of accent and emotion. du2024cosyvoice propose to use “supervised semantic token”, obtained by injecting FSQ in an internal ASR model encoder; how ASR pretraining affects the information in discrete tokens remains unclear.
L96: ### 2.4 Accent Control and Generation
L97: Unfortunately, ZS-TTS speech generation systems suffer accent hallucination, whereby they generate a hallucinated synthetic accent that deviates from the reference or prompt speech (zhong2025accentbox). Recent systems that have been specially built for accent generation have not yet utilised DSRTs along with powerful LLM architectures (zhong2025accentbox; xinyuan2025scalable).
L98: General ZS-TTS systems are reported to have certain accent control capabilities, but there has been little or no investigation about accent information in DSRTs. Understanding how accent information is encoded could help build more inclusive ZS-TTS systems for diverse accents.
L99: ### 2.5 ABX Evaluation
L100: 
L101: The ABX error rate is a distance-based, model-agnostic evaluation metric, assessing whether the representations pull data of the same category (e.g. sample $x=$ \textipa[bIt], another sample $a=$ \textipa[bIt], of the same triphone category) closer and push dissimilar data (e.g. $x=$ \textipa[bIt], $b=$ \textipa[bi:t]) farther in representational space.
L102: Previous work introduced Minimal Pair ABX (MP-ABX) (schatz2013evaluating), where instances differ only in a central phonetic unit while sharing the same phonetic context. Prior studies (borsos2023audiolm; wang2025maskgct; zhang2025vevo) have used this metric to assess the phonetic discriminability of DSRT tokens. In addition, ABX has been extended to probe speaker-related information by defining triplets that contrast speaker identity under controlled linguistic content (de2022language).
L103: Nevertheless, to the best of our knowledge, no prior work has systematically employed machine ABX to reveal accent discriminability in speech representations or DSRTs.
L104: ## 3 Method
L105: Inspired by the perspective of separately measuring information completeness and accessibility yeh2024estimating, we focus on evaluating DSRTs from both aspects, but in the context of accent generation. Since completeness cannot be measured by resynthesis, we introduce recoverability as a task-grounded measure of how much accent, speaker, and phonetic information encoded in DSRTs can be recovered in resynthesised speech.
L106: Together with accessibility, we propose a pipeline that evaluates DSRTs from both synthesis-facing and representation-facing perspectives.
L107: Figure cite37†1 provides an overview of the proposed pipeline. First, we obtain DSRTs from several commonly used speech representations using RepCodec huang2024repcodec with Vector Quantisation (VQ) vandenoord2017neural as the quantiser (see Section cite14†3.1 ). For each DSRT configuration, we then train a unit-to-speech resynthesis model using HiFiGAN polyak2021speech.
L108: To assess information recoverability, we infer unit-to-speech models with DSRTs from a source speaker and speaker ID from a target speaker with a different accent, thereby conducting cross-accent VC. The generated speech is evaluated using a combination of objective metrics and subjective listening tests (see Section cite15†3.2 ). Finally, to assess information accessibility, we directly probe the DSRTs using a range of ABX setups (see Section cite16†3.3 ).
L109: ### 3.1 Discrete Speech Representation Tokens
L110: We choose three speech representation models to obtain Discrete Speech Representation Tokens (DSRTs): HuBERT; HuBERT finetuned for ASR (HuBERT-ft); and Whisper. We include HuBERT hsu2021hubert as it provides the most widely used speech representations in various speech tasks such as SpeechLM and TTS guo2025recent; cui2025recent. Recently, there has been a growing trend toward using ASR-based speech representations for obtaining DSRTs.
L111: Therefore, we include HuBERT-ft and Whisper as two representative ASR-based representations, with Encoder-only and Encoder-Decoder architectures, respectively.
L112: Following RepCodec huang2024repcodec, we use VQ-VAE vandenoord2017neural to discretise the speech representations. The model consists of three modules: Encoder and Decoder, which are both convolution layers with residual paths, and a Vector Quantisation module that quantises latent representations from Encoder output into a series of discrete tokens. The model is trained to reconstruct the speech representation, with additional Exponential Moving Average (EMA) optimisation to gradually update the codebook.
L113: For model details, we refer readers to the original paper huang2024repcodec.
L114: ### 3.2 Cross-Accent Voice Conversion
L115: 
L116: After extracting DSRTs, we train a unit-to-speech HiFiGAN model for each DSRT configuration, following polyak2021speech. In prior work, information recoverability is typically evaluated using resynthesis or Voice Conversion (VC) on General American English datasets, with evaluation focusing primarily on intelligibility and speaker similarity, while accent is largely ignored.
L117: We train unit-to-speech models on data covering multiple accents to assess the generalisability of DSRTs across accents. We then perform cross-accent VC in inference, by conditioning the model on DSRTs from a source speaker and a target speaker ID with a different accent. Afterwards, during evaluation, following zhong2025pairwise, we explicitly assess accent, speaker, and phonetic similarity in the converted speech.
L118: Utterance-level embeddings from Accent Identification (AID) and Speaker Verification (SV) models are used to calculate cosine similarity, which serves as a proxy for perceived accent and speaker similarity. Phonetic Posteriorgrams (PPGs) are extracted, aligned, and then used to calculate phonetic distances as a proxy for perceived phonetic similarity, and to some degree, intelligibility.
L119: By analysing the similarity of the generated speech to the source and target speech along these dimensions, we can determine whether accent information is primarily derived from the source DSRTs or overridden by the target speaker identity, thereby quantifying the amount of accent information preserved in the DSRTs.
L120: ### 3.3 Accent, Speaker, and Phonetic ABX
L121: 
L122: We choose ABX as a model-free method to estimate the accessibility of accent information, as well as phone and speaker information in DSRTs.
L123: In accent ABX, instances $a$ and $x$ share the same accent, while instance $b$ differs in accent. Triplets $(a,b,x)$ are constructed to share identical lexical content rather than phonetic context, as accent distinctions arise from accent-dependent realizations of the same words or lexical units, which may involve different phone sequences.
L124: We further require that $a$, $b$, and $x$ come from different speakers to avoid trivial similarity between $a$ and $x$ due to shared speaker identity, e.g.: a triplet $(a,b,x)$ consists of: $x=$ “water” spoken by a Scottish speaker_{1}, $a=$ “water” by a Scottish speaker_{2}, and $b=$ “water” by a Southern English speaker_{3}.
L125: We also adopt speaker ABX and phone ABX as contrastive evaluations. For detailed triplet selection criteria, see Appendix cite31†A .
L126: In practice, words vary in both accent-induced pronunciation variation and speaker-specific pronunciation patterns. While standard ABX aggregates scores over all valid triplets, we adopt a word selection scheme to improve the sensitivity of accent ABX. We first select the 100 most frequent words in the training data, compute ABX scores for each (accent $A$ and $B$, word) combination, and retain the 10% with the lowest scores as the most accent-discriminative.
L127: The final accent ABX score is obtained by averaging their ABX scores on the test set. The combination selection is performed using continuous features from GenAID zhong2025accentbox, a supervised accent identification model fine-tuned from XLSR babu2021xls, to ensure effective word selection and a fair comparison among DSRTs. See Appendix cite32†B for details.
L128: cite38†Image: Refer to caption (a) Cross-accent VC evaluation results for information recoverability.
L129: 
L130: cite38†Image: Refer to caption (b) ABX evaluation results for information accessibility.
L131: 
L132: Figure 2: Accent, speaker, and phonetic information in different DSRTs across layers and representations.
L133: All codebook sizes and code dimensions are set to 1024 for fair comparison.
L134: (See Figure cite39†4 in Appendix cite34†D for additional results from cross-accent VC.)

## Original response 4: jan29_stdnext5tail

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28456view2 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"turn28451view2","lineno":135}); Total lines: 322
L124: We further require that $a$, $b$, and $x$ come from different speakers to avoid trivial similarity between $a$ and $x$ due to shared speaker identity, e.g.: a triplet $(a,b,x)$ consists of: $x=$ “water” spoken by a Scottish speaker_{1}, $a=$ “water” by a Scottish speaker_{2}, and $b=$ “water” by a Southern English speaker_{3}.
L125: We also adopt speaker ABX and phone ABX as contrastive evaluations. For detailed triplet selection criteria, see Appendix cite31†A .
L126: In practice, words vary in both accent-induced pronunciation variation and speaker-specific pronunciation patterns. While standard ABX aggregates scores over all valid triplets, we adopt a word selection scheme to improve the sensitivity of accent ABX. We first select the 100 most frequent words in the training data, compute ABX scores for each (accent $A$ and $B$, word) combination, and retain the 10% with the lowest scores as the most accent-discriminative.
L127: The final accent ABX score is obtained by averaging their ABX scores on the test set. The combination selection is performed using continuous features from GenAID zhong2025accentbox, a supervised accent identification model fine-tuned from XLSR babu2021xls, to ensure effective word selection and a fair comparison among DSRTs. See Appendix cite32†B for details.
L128: cite38†Image: Refer to caption (a) Cross-accent VC evaluation results for information recoverability.
L129: 
L130: cite38†Image: Refer to caption (b) ABX evaluation results for information accessibility.
L131: 
L132: Figure 2: Accent, speaker, and phonetic information in different DSRTs across layers and representations.
L133: All codebook sizes and code dimensions are set to 1024 for fair comparison.
L134: (See Figure cite39†4 in Appendix cite34†D for additional results from cross-accent VC.)
L135: ## 4 Experiments
L136: ### 4.1 Obtaining DSRTs
L137: We extract continuous speech representations from various layers of HuBERT^{2}^{2} 2 hubert-large-ll60k, available cite40†here†huggingface.co , HuBERT-ft^{3}^{3} 3 hubert-large-ls960-ft, available cite41†here†huggingface.co and Whisper^{4}^{4} 4 whisper-meidum.en, available cite42†here†huggingface.co . All three speech representation models share the same Encoder architecture (24 Transformer layers) and are trained on English-only data.
L138: Here, we focus on investigating how layer choice and ASR pretraining affect the information encoded in speech representations, and leave the investigation of how multilingual pretraining or larger-scale pretraining data/model to future work.
L139: The extracted representations are then discretised using RepCodec^{5}^{5} 5 cite43†https://github.com/mct10/RepCodec†github.com , which we train on the train-clean-100 subset of LibriSpeech^{6}^{6} 6 cite44†https://www.openslr.org/12†www.openslr.org following similar practice in huang2024repcodec and zhang2025vevo, with various codebook sizes. This subset contains 100 hours of speech with "accents closer to US English" panayotov2015librispeech.
L140: RepCodec is trained for 200,000 steps with the same hyperparameters in huang2024repcodec.
L141: ### 4.2 Evaluation Dataset
L142: 
L143: To evaluate information recoverability and accessibility with respect to accent, we use the VCTK corpus^{7}^{7} 7 cite45†https://datashare.ed.ac.uk/handle/10283/3443†datashare.ed.ac.uk , which provides relatively broad coverage of native English accents. Based on the provided country labels and detailed region descriptions, we manually group speakers into 13 accent regions, as some coarse country-level labels (e.g. “US”, “England”) conflate multiple distinct accent varieties.
L144: We withhold 3–4 speakers from each accent region (50 speakers in total, with balanced gender and accent distribution) for testing. For the remaining speakers, we use 4 accent regions that have sufficient speakers (45 speakers in total) for training unit-to-speech HiFiGAN in Section cite15†3.2 and for selecting accent-discriminative words in Section cite16†3.3 .
L145: Out of the 13 accent regions, 4 are seen in HiFiGAN training and accent ABX word selection, 5 are likely seen by RepCodec in LibriSpeech, and the remaining 4 are unseen at any stage, allowing for analysis on the generalisability of DSRTs across accents. See Appendix cite33†C for details of accent grouping and speaker splits.
L146: cite46†Image: Refer to caption Figure 3: Accent, speaker, and phonetic information recoverability in different DSRTs across codebook sizes.
L147: (See Figure cite47†5 in Appendix cite34†D for additional results from cross-accent VC and ABX.)
L148: ### 4.3 Evaluating Information Recoverability
L149: To evaluate information recoverability, we train unit-to-speech HiFiGAN models^{8}^{8} 8 cite48†https://github.com/facebookresearch/speech-resynthesis†github.com for 100,000 steps with the same hyperparameters as polyak2021speech, using 4 accent regions (45 speakers), as described in Section cite19†4.2 .
L150: During inference, we perform cross-accent VC using source (src) DSRTs from 12 accent regions (46 speakers, excluding Southern English), together with speaker IDs from 4 Southern English speakers as target (tgt) voices. We fix the target voices to one accent region to control for target-side accent variability, enabling a clearer analysis of how accent information is preserved in the src DSRTs.

## Original response 5: jan29_stdnext5finish

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28464view2 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19786v1","lineno":145}); Total lines: 322
L127: The final accent ABX score is obtained by averaging their ABX scores on the test set. The combination selection is performed using continuous features from GenAID zhong2025accentbox, a supervised accent identification model fine-tuned from XLSR babu2021xls, to ensure effective word selection and a fair comparison among DSRTs. See Appendix cite32†B for details.
L128: cite38†Image: Refer to caption (a) Cross-accent VC evaluation results for information recoverability.
L129: 
L130: cite38†Image: Refer to caption (b) ABX evaluation results for information accessibility.
L131: 
L132: Figure 2: Accent, speaker, and phonetic information in different DSRTs across layers and representations.
L133: All codebook sizes and code dimensions are set to 1024 for fair comparison.
L134: (See Figure cite39†4 in Appendix cite34†D for additional results from cross-accent VC.)
L135: ## 4 Experiments
L136: ### 4.1 Obtaining DSRTs
L137: We extract continuous speech representations from various layers of HuBERT^{2}^{2} 2 hubert-large-ll60k, available cite40†here†huggingface.co , HuBERT-ft^{3}^{3} 3 hubert-large-ls960-ft, available cite41†here†huggingface.co and Whisper^{4}^{4} 4 whisper-meidum.en, available cite42†here†huggingface.co . All three speech representation models share the same Encoder architecture (24 Transformer layers) and are trained on English-only data.
L138: Here, we focus on investigating how layer choice and ASR pretraining affect the information encoded in speech representations, and leave the investigation of how multilingual pretraining or larger-scale pretraining data/model to future work.
L139: The extracted representations are then discretised using RepCodec^{5}^{5} 5 cite43†https://github.com/mct10/RepCodec†github.com , which we train on the train-clean-100 subset of LibriSpeech^{6}^{6} 6 cite44†https://www.openslr.org/12†www.openslr.org following similar practice in huang2024repcodec and zhang2025vevo, with various codebook sizes. This subset contains 100 hours of speech with "accents closer to US English" panayotov2015librispeech.
L140: RepCodec is trained for 200,000 steps with the same hyperparameters in huang2024repcodec.
L141: ### 4.2 Evaluation Dataset
L142: 
L143: To evaluate information recoverability and accessibility with respect to accent, we use the VCTK corpus^{7}^{7} 7 cite45†https://datashare.ed.ac.uk/handle/10283/3443†datashare.ed.ac.uk , which provides relatively broad coverage of native English accents. Based on the provided country labels and detailed region descriptions, we manually group speakers into 13 accent regions, as some coarse country-level labels (e.g. “US”, “England”) conflate multiple distinct accent varieties.
L144: We withhold 3–4 speakers from each accent region (50 speakers in total, with balanced gender and accent distribution) for testing. For the remaining speakers, we use 4 accent regions that have sufficient speakers (45 speakers in total) for training unit-to-speech HiFiGAN in Section cite15†3.2 and for selecting accent-discriminative words in Section cite16†3.3 .
L145: Out of the 13 accent regions, 4 are seen in HiFiGAN training and accent ABX word selection, 5 are likely seen by RepCodec in LibriSpeech, and the remaining 4 are unseen at any stage, allowing for analysis on the generalisability of DSRTs across accents. See Appendix cite33†C for details of accent grouping and speaker splits.
L146: cite46†Image: Refer to caption Figure 3: Accent, speaker, and phonetic information recoverability in different DSRTs across codebook sizes.
L147: (See Figure cite47†5 in Appendix cite34†D for additional results from cross-accent VC and ABX.)
L148: ### 4.3 Evaluating Information Recoverability
L149: To evaluate information recoverability, we train unit-to-speech HiFiGAN models^{8}^{8} 8 cite48†https://github.com/facebookresearch/speech-resynthesis†github.com for 100,000 steps with the same hyperparameters as polyak2021speech, using 4 accent regions (45 speakers), as described in Section cite19†4.2 .
L150: During inference, we perform cross-accent VC using source (src) DSRTs from 12 accent regions (46 speakers, excluding Southern English), together with speaker IDs from 4 Southern English speakers as target (tgt) voices. We fix the target voices to one accent region to control for target-side accent variability, enabling a clearer analysis of how accent information is preserved in the src DSRTs.
L151: For objective evaluation of the converted speech, we adopt metrics recommended by zhong2025pairwise. (1) Accent similarity: We calculate cosine similarity of accent embeddings (Accent COS-SIM) extracted from GenAID^{9}^{9} 9 cite49†https://github.com/jzmzhong/GenAID†github.com zhong2025accentbox. GenAID is trained with explicit speaker-accent disentanglement, preserving little speaker information in the extracted accent embeddings.
L152: (2) Speaker similarity: We calculate cosine similarity of speaker embeddings (Speaker COS-SIM) extracted from WavLM^{10}^{10} 10 wavlm-base-plus-sv, available cite50†here†huggingface.co chen2022wavlm. These speaker embeddings encode some accent information, evidenced by improved performance in AID when transfer learned from SV models zuluagagomez2023commonaccent.
L153: (3) Phonetic similarity: We calculate Jensen-Shannon distance between aligned PPGs^{11}^{11} 11 cite51†https://github.com/interactiveaudiolab/ppgs†github.com (PPG Distance), extracted from a phone recognition model churchwell2024ppgs. It is worth noting that PPG distance, primarily designed for pronunciation distance, is sensitive to accent information, as accent can be characterised partially as different realisations of the same phoneme.
L154: (4) Intelligibility: We calculate Word Error Rate (WER) using whisper-medium.en transcriptions, compared against ground-truth transcriptions. Despite its evident accent bias jahan2025unveiling, WER is included here due to its broad adoption in previous DSRT evaluation frameworks to reflect how DSRTs are commonly selected.
L155: For Accent COS-SIM, Speaker COS-SIM, and PPG distance, we use the first 24 utterances per speaker, which is an elicitation paragraph shared across speakers. In this way, we allow for similarity/distance calculation to either source speech that provides DSRTs or target speech that provides the speaker ID of the same content, removing the influence of content on these metrics. For WER, we randomly choose 24 utterances per speaker to cover diverse contents.
L156: For visualisation, we annotate each metric with a practical lower bound (chance-level performance) and a practical upper bound (best possible performance), which anchor the visual scale and facilitate interpretation of values. For Accent COS-SIM, PPG, and WER, the lower bound measures the source speaker ground truth (GT) with respect to target speaker GT, and the upper bound measures the source speaker copy-synthesis with respect to source speaker GT.
L157: For Speaker COS-SIM, the lower bound measures similarity between source speaker GT and target speaker GT, while the upper bound measures similarity between target speaker copy-synthesis and target speaker GT.
L158: ### 4.4 Evaluating Information Accessibility
L159: Information accessibility is evaluated only on the accents seen during HiFiGAN training, ensuring sufficient numbers of speakers for each accent. As described in Section cite16†3.3 , a training set is required to select high-frequency words and accent-discriminative combinations, while a separate test set is used for ABX evaluation to prevent speaker leakage. Accents outside the four seen accents contain no more than four speakers each, severely limiting the number of valid ABX triplets.
L160: We follow the same training–test partition as in HiFiGAN experiments for simplicity. Accent ABX is conducted using this partition, whereas phone and speaker ABX are computed only on the test split, as they do not require a training phase.
L161: Test experiments used all utterances in the split, except for the first 24 utterances to avoid identical sentences across all train and test speakers, which could bias the ABX scores toward lexical-context matching instead of reflecting true accent or speaker discrimination. Phone-level alignment (phone boundaries and labels) required by phone ABX, were obtained through the Montreal Forced Aligner with the English Arpabet dictionary mfa_english_us_arpa_acoustic_2024; gorman2011prosodylab.
L162: We treat the accent ABX score computed on HuBERT layer 6 continuous features as an upper bound, as this layer exhibits the strongest accent-related information. Similarly, we use the phonetic and speaker ABX scores computed on HuBERT-ft layers 3 and 9 continuous features as upper bounds, respectively, since these layers demonstrate the highest phonetic and speaker recoverability in Section cite22†5 .
L163: In addition, we evaluate the accent ABX error rate of the accent-discriminative GenAID features, which achieves a low error rate of 9.87%, validating the effectiveness of the proposed metric.
L164:  | Token type  |
L165: Representation
L166: & Layer

## Original response 6: jan29_stdnext5last

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28465view0 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19786v1","lineno":183}); Total lines: 322
L159: Information accessibility is evaluated only on the accents seen during HiFiGAN training, ensuring sufficient numbers of speakers for each accent. As described in Section cite16†3.3 , a training set is required to select high-frequency words and accent-discriminative combinations, while a separate test set is used for ABX evaluation to prevent speaker leakage. Accents outside the four seen accents contain no more than four speakers each, severely limiting the number of valid ABX triplets.
L160: We follow the same training–test partition as in HiFiGAN experiments for simplicity. Accent ABX is conducted using this partition, whereas phone and speaker ABX are computed only on the test split, as they do not require a training phase.
L161: Test experiments used all utterances in the split, except for the first 24 utterances to avoid identical sentences across all train and test speakers, which could bias the ABX scores toward lexical-context matching instead of reflecting true accent or speaker discrimination. Phone-level alignment (phone boundaries and labels) required by phone ABX, were obtained through the Montreal Forced Aligner with the English Arpabet dictionary mfa_english_us_arpa_acoustic_2024; gorman2011prosodylab.
L162: We treat the accent ABX score computed on HuBERT layer 6 continuous features as an upper bound, as this layer exhibits the strongest accent-related information. Similarly, we use the phonetic and speaker ABX scores computed on HuBERT-ft layers 3 and 9 continuous features as upper bounds, respectively, since these layers demonstrate the highest phonetic and speaker recoverability in Section cite22†5 .
L163: In addition, we evaluate the accent ABX error rate of the accent-discriminative GenAID features, which achieves a low error rate of 9.87%, validating the effectiveness of the proposed metric.
L164:  | Token type  |
L165: Representation
L166: & Layer
L167:  |
L168: Codebook
L169: size
L170:  |
L171: A-SIM
L172: (src)^{∗}
L173:  |
L174: A-SIM
L175: (tgt)^{∗}
L176:  |
L177: S-SIM
L178: (src)$\downarrow$
L179:  |
L180: S-SIM
L181: (tgt)$\uparrow$
L182:  | PPG$\downarrow$  | WER$\downarrow$
L183: Vevo  | Content  | HuBERT L18  | 32  | 0.8143  | 0.9369  | 0.6817  | 0.9651  | 0.1718  | 0.0824
L184: Content-style  | HuBERT L18  | 8192  | 0.8923  | 0.8888  | 0.6989  | 0.9499  | 0.1427  | 0.0425
L185: Proposed  | Content  | HuBERT-ft L18  | 256  | 0.8081  | 0.9509  | 0.6782  | 0.9667  | 0.1488  | 0.0523
L186: Content-accent  | HuBERT L9  | 8192  | 0.9541  | 0.8227  | 0.7529  | 0.9104  | 0.1265  | 0.0344
L187: Table 1: Results of proposed content and content-accent tokens, compared with content and content-style tokens from Vevo (zhang2025vevo). Differences in DSRT design choices are marked in red, with best performances marked in bold. $*$: For content tokens, we want little accent information recovered from DSRTs, i.e. low A-SIM (src) and high A-SIM (tar). For content-accent or content-style tokens, we want the opposite.
L188: ## 5 Results
L189: ### 5.1 Layer Choice Matters for Accent
L190: Layer choice has a prominent impact on the recoverability and accessibility of information in HuBERT DSRTs, shown in Figure cite52†2 (dark green curve). Notably, accent, speaker and phonetic information are distributed differently across layers. (1) Accent information recoverability, reflected by Accent COS-SIM w.r.t.
L191: source speaker, is most prominent in mid–early HuBERT layers (L6 & L9), and decreases in earlier or latter layers, indicating that accent cues emerge after low-level acoustic processing but are progressively abstracted away in higher layers. (2) Speaker information is most recoverable in early HuBERT layers (L3), indicated by Speaker COS-SIM to the source speaker, and decreases monotonically with depth.
L192: Overall, speaker information is limited, as cross-accent VC aims to generate voice similar to that of the target speaker with speaker ID conditioning. (3) Phonetic information, measured by PPG Distance to the source speech, is most complete in middle layers (L9 & L12). Both earlier and later layers show reduced phonetic completeness, reflecting a trade-off between raw acoustic detail and higher-level abstraction.
L193: (4) Information accessibility, measured by ABX error rates (see Figure cite53†2(b) ), reveals weak accent accessibility for HuBERT across layers, despite clear inter-layer variations. Accent accessibility peaks at L12, which differs from the recoverability peak at L6 or L9.
L194: This discrepancy highlights the necessity of resynthesis-based recoverability evaluation when assessing DSRTs for accent generation: while ABX accessibility captures relative trends, it cannot reliably identify optimal layers for synthesis.
L195: ### 5.2 ASR Supervision Removes Accent Information
L196: ASR supervision reduces the recoverability and accessibility of accent information in DSRTs across layers, shown in Figure cite52†2 (blue curve for HuBERT-ft, orange curve for Whisper). (1) HuBERT consistently shows higher accent recoverability and accessibility than HuBERT-ft or Whisper, particularly in latter layers, which are more affected by ASR supervision.
L197: (2) Whisper exhibits a peak in accent and phonetic information at intermediate layers (L12 & L15), different from the distribution of information in HuBERT or HuBERT-ft.
L198: ### 5.3 Reducing Codebook Size Provides Limited Disentanglement
L199: We then vary codebook sizes for three selected layers: HuBERT L18 (a common choice, as in Vevo zhang2025vevo), HuBERT-ft L18 (a layer with little accent information while retaining high phonetic information), and HuBERT L9 (a layer with most accent information), shown in Figure cite54†3 . (1) Focusing on accent recoverability, varying codebook sizes has a markedly smaller effect than changing representation models or layers.

## Original response 7: jan29_stdnext5accentclose

Rethinking Discrete Speech Representation Tokens for Accent Generation (https://arxiv.org/html/2601.19786v1)
citeturn28466view0 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19786v1","lineno":199}); Total lines: 322
L114: ### 3.2 Cross-Accent Voice Conversion
L115: 
L117: We train unit-to-speech models on data covering multiple accents to assess the generalisability of DSRTs across accents. We then perform cross-accent VC in inference, by conditioning the model on DSRTs from a source speaker and a target speaker ID with a different accent. Afterwards, during evaluation, following zhong2025pairwise, we explicitly assess accent, speaker, and phonetic similarity in the converted speech.
L118: Utterance-level embeddings from Accent Identification (AID) and Speaker Verification (SV) models are used to calculate cosine similarity, which serves as a proxy for perceived accent and speaker similarity. Phonetic Posteriorgrams (PPGs) are extracted, aligned, and then used to calculate phonetic distances as a proxy for perceived phonetic similarity, and to some degree, intelligibility.
L119: By analysing the similarity of the generated speech to the source and target speech along these dimensions, we can determine whether accent information is primarily derived from the source DSRTs or overridden by the target speaker identity, thereby quantifying the amount of accent information preserved in the DSRTs.
L120: ### 3.3 Accent, Speaker, and Phonetic ABX
L121: 
L122: We choose ABX as a model-free method to estimate the accessibility of accent information, as well as phone and speaker information in DSRTs.
L123: In accent ABX, instances $a$ and $x$ share the same accent, while instance $b$ differs in accent. Triplets $(a,b,x)$ are constructed to share identical lexical content rather than phonetic context, as accent distinctions arise from accent-dependent realizations of the same words or lexical units, which may involve different phone sequences.
L124: We further require that $a$, $b$, and $x$ come from different speakers to avoid trivial similarity between $a$ and $x$ due to shared speaker identity, e.g.: a triplet $(a,b,x)$ consists of: $x=$ “water” spoken by a Scottish speaker_{1}, $a=$ “water” by a Scottish speaker_{2}, and $b=$ “water” by a Southern English speaker_{3}.
L125: We also adopt speaker ABX and phone ABX as contrastive evaluations. For detailed triplet selection criteria, see Appendix cite31†A .
L126: In practice, words vary in both accent-induced pronunciation variation and speaker-specific pronunciation patterns. While standard ABX aggregates scores over all valid triplets, we adopt a word selection scheme to improve the sensitivity of accent ABX. We first select the 100 most frequent words in the training data, compute ABX scores for each (accent $A$ and $B$, word) combination, and retain the 10% with the lowest scores as the most accent-discriminative.
L127: The final accent ABX score is obtained by averaging their ABX scores on the test set. The combination selection is performed using continuous features from GenAID zhong2025accentbox, a supervised accent identification model fine-tuned from XLSR babu2021xls, to ensure effective word selection and a fair comparison among DSRTs. See Appendix cite32†B for details.
L128: cite38†Image: Refer to caption (a) Cross-accent VC evaluation results for information recoverability.
L129: 
L130: cite38†Image: Refer to caption (b) ABX evaluation results for information accessibility.
L131: 
L132: Figure 2: Accent, speaker, and phonetic information in different DSRTs across layers and representations.
L133: All codebook sizes and code dimensions are set to 1024 for fair comparison.
L134: (See Figure cite39†4 in Appendix cite34†D for additional results from cross-accent VC.)
L135: ## 4 Experiments
L136: ### 4.1 Obtaining DSRTs
L137: We extract continuous speech representations from various layers of HuBERT^{2}^{2} 2 hubert-large-ll60k, available cite40†here†huggingface.co , HuBERT-ft^{3}^{3} 3 hubert-large-ls960-ft, available cite41†here†huggingface.co and Whisper^{4}^{4} 4 whisper-meidum.en, available cite42†here†huggingface.co . All three speech representation models share the same Encoder architecture (24 Transformer layers) and are trained on English-only data.
L138: Here, we focus on investigating how layer choice and ASR pretraining affect the information encoded in speech representations, and leave the investigation of how multilingual pretraining or larger-scale pretraining data/model to future work.
L139: The extracted representations are then discretised using RepCodec^{5}^{5} 5 cite43†https://github.com/mct10/RepCodec†github.com , which we train on the train-clean-100 subset of LibriSpeech^{6}^{6} 6 cite44†https://www.openslr.org/12†www.openslr.org following similar practice in huang2024repcodec and zhang2025vevo, with various codebook sizes. This subset contains 100 hours of speech with "accents closer to US English" panayotov2015librispeech.
L140: RepCodec is trained for 200,000 steps with the same hyperparameters in huang2024repcodec.
L141: ### 4.2 Evaluation Dataset
L142: 
L143: To evaluate information recoverability and accessibility with respect to accent, we use the VCTK corpus^{7}^{7} 7 cite45†https://datashare.ed.ac.uk/handle/10283/3443†datashare.ed.ac.uk , which provides relatively broad coverage of native English accents. Based on the provided country labels and detailed region descriptions, we manually group speakers into 13 accent regions, as some coarse country-level labels (e.g. “US”, “England”) conflate multiple distinct accent varieties.
L144: We withhold 3–4 speakers from each accent region (50 speakers in total, with balanced gender and accent distribution) for testing. For the remaining speakers, we use 4 accent regions that have sufficient speakers (45 speakers in total) for training unit-to-speech HiFiGAN in Section cite15†3.2 and for selecting accent-discriminative words in Section cite16†3.3 .
L145: Out of the 13 accent regions, 4 are seen in HiFiGAN training and accent ABX word selection, 5 are likely seen by RepCodec in LibriSpeech, and the remaining 4 are unseen at any stage, allowing for analysis on the generalisability of DSRTs across accents. See Appendix cite33†C for details of accent grouping and speaker splits.
L146: cite46†Image: Refer to caption Figure 3: Accent, speaker, and phonetic information recoverability in different DSRTs across codebook sizes.
L147: (See Figure cite47†5 in Appendix cite34†D for additional results from cross-accent VC and ABX.)
L148: ### 4.3 Evaluating Information Recoverability
L149: To evaluate information recoverability, we train unit-to-speech HiFiGAN models^{8}^{8} 8 cite48†https://github.com/facebookresearch/speech-resynthesis†github.com for 100,000 steps with the same hyperparameters as polyak2021speech, using 4 accent regions (45 speakers), as described in Section cite19†4.2 .
L150: During inference, we perform cross-accent VC using source (src) DSRTs from 12 accent regions (46 speakers, excluding Southern English), together with speaker IDs from 4 Southern English speakers as target (tgt) voices. We fix the target voices to one accent region to control for target-side accent variability, enabling a clearer analysis of how accent information is preserved in the src DSRTs.
L151: For objective evaluation of the converted speech, we adopt metrics recommended by zhong2025pairwise. (1) Accent similarity: We calculate cosine similarity of accent embeddings (Accent COS-SIM) extracted from GenAID^{9}^{9} 9 cite49†https://github.com/jzmzhong/GenAID†github.com zhong2025accentbox. GenAID is trained with explicit speaker-accent disentanglement, preserving little speaker information in the extracted accent embeddings.
L152: (2) Speaker similarity: We calculate cosine similarity of speaker embeddings (Speaker COS-SIM) extracted from WavLM^{10}^{10} 10 wavlm-base-plus-sv, available cite50†here†huggingface.co chen2022wavlm. These speaker embeddings encode some accent information, evidenced by improved performance in AID when transfer learned from SV models zuluagagomez2023commonaccent.
L153: (3) Phonetic similarity: We calculate Jensen-Shannon distance between aligned PPGs^{11}^{11} 11 cite51†https://github.com/interactiveaudiolab/ppgs†github.com (PPG Distance), extracted from a phone recognition model churchwell2024ppgs. It is worth noting that PPG distance, primarily designed for pronunciation distance, is sensitive to accent information, as accent can be characterised partially as different realisations of the same phoneme.
L154: (4) Intelligibility: We calculate Word Error Rate (WER) using whisper-medium.en transcriptions, compared against ground-truth transcriptions. Despite its evident accent bias jahan2025unveiling, WER is included here due to its broad adoption in previous DSRT evaluation frameworks to reflect how DSRTs are commonly selected.
L155: For Accent COS-SIM, Speaker COS-SIM, and PPG distance, we use the first 24 utterances per speaker, which is an elicitation paragraph shared across speakers. In this way, we allow for similarity/distance calculation to either source speech that provides DSRTs or target speech that provides the speaker ID of the same content, removing the influence of content on these metrics. For WER, we randomly choose 24 utterances per speaker to cover diverse contents.
L156: For visualisation, we annotate each metric with a practical lower bound (chance-level performance) and a practical upper bound (best possible performance), which anchor the visual scale and facilitate interpretation of values. For Accent COS-SIM, PPG, and WER, the lower bound measures the source speaker ground truth (GT) with respect to target speaker GT, and the upper bound measures the source speaker copy-synthesis with respect to source speaker GT.
L157: For Speaker COS-SIM, the lower bound measures similarity between source speaker GT and target speaker GT, while the upper bound measures similarity between target speaker copy-synthesis and target speaker GT.
L158: ### 4.4 Evaluating Information Accessibility
L159: Information accessibility is evaluated only on the accents seen during HiFiGAN training, ensuring sufficient numbers of speakers for each accent. As described in Section cite16†3.3 , a training set is required to select high-frequency words and accent-discriminative combinations, while a separate test set is used for ABX evaluation to prevent speaker leakage. Accents outside the four seen accents contain no more than four speakers each, severely limiting the number of valid ABX triplets.
L160: We follow the same training–test partition as in HiFiGAN experiments for simplicity. Accent ABX is conducted using this partition, whereas phone and speaker ABX are computed only on the test split, as they do not require a training phase.
L161: Test experiments used all utterances in the split, except for the first 24 utterances to avoid identical sentences across all train and test speakers, which could bias the ABX scores toward lexical-context matching instead of reflecting true accent or speaker discrimination. Phone-level alignment (phone boundaries and labels) required by phone ABX, were obtained through the Montreal Forced Aligner with the English Arpabet dictionary mfa_english_us_arpa_acoustic_2024; gorman2011prosodylab.
L162: We treat the accent ABX score computed on HuBERT layer 6 continuous features as an upper bound, as this layer exhibits the strongest accent-related information. Similarly, we use the phonetic and speaker ABX scores computed on HuBERT-ft layers 3 and 9 continuous features as upper bounds, respectively, since these layers demonstrate the highest phonetic and speaker recoverability in Section cite22†5 .
L163: In addition, we evaluate the accent ABX error rate of the accent-discriminative GenAID features, which achieves a low error rate of 9.87%, validating the effectiveness of the proposed metric.
L164:  | Token type  |
L165: Representation
L166: & Layer
L167:  |
L168: Codebook
L169: size
L170:  |
L171: A-SIM
L172: (src)^{∗}
L173:  |
L174: A-SIM
L175: (tgt)^{∗}
L176:  |
L177: S-SIM
L178: (src)$\downarrow$
L179:  |
L180: S-SIM
L181: (tgt)$\uparrow$
L182:  | PPG$\downarrow$  | WER$\downarrow$
L183: Vevo  | Content  | HuBERT L18  | 32  | 0.8143  | 0.9369  | 0.6817  | 0.9651  | 0.1718  | 0.0824
L184: Content-style  | HuBERT L18  | 8192  | 0.8923  | 0.8888  | 0.6989  | 0.9499  | 0.1427  | 0.0425
L185: Proposed  | Content  | HuBERT-ft L18  | 256  | 0.8081  | 0.9509  | 0.6782  | 0.9667  | 0.1488  | 0.0523
L186: Content-accent  | HuBERT L9  | 8192  | 0.9541  | 0.8227  | 0.7529  | 0.9104  | 0.1265  | 0.0344
L187: Table 1: Results of proposed content and content-accent tokens, compared with content and content-style tokens from Vevo (zhang2025vevo). Differences in DSRT design choices are marked in red, with best performances marked in bold. $*$: For content tokens, we want little accent information recovered from DSRTs, i.e. low A-SIM (src) and high A-SIM (tar). For content-accent or content-style tokens, we want the opposite.
L188: ## 5 Results
L189: ### 5.1 Layer Choice Matters for Accent
L190: Layer choice has a prominent impact on the recoverability and accessibility of information in HuBERT DSRTs, shown in Figure cite52†2 (dark green curve). Notably, accent, speaker and phonetic information are distributed differently across layers. (1) Accent information recoverability, reflected by Accent COS-SIM w.r.t.
L191: source speaker, is most prominent in mid–early HuBERT layers (L6 & L9), and decreases in earlier or latter layers, indicating that accent cues emerge after low-level acoustic processing but are progressively abstracted away in higher layers. (2) Speaker information is most recoverable in early HuBERT layers (L3), indicated by Speaker COS-SIM to the source speaker, and decreases monotonically with depth.
L192: Overall, speaker information is limited, as cross-accent VC aims to generate voice similar to that of the target speaker with speaker ID conditioning. (3) Phonetic information, measured by PPG Distance to the source speech, is most complete in middle layers (L9 & L12). Both earlier and later layers show reduced phonetic completeness, reflecting a trade-off between raw acoustic detail and higher-level abstraction.
L193: (4) Information accessibility, measured by ABX error rates (see Figure cite53†2(b) ), reveals weak accent accessibility for HuBERT across layers, despite clear inter-layer variations. Accent accessibility peaks at L12, which differs from the recoverability peak at L6 or L9.
L194: This discrepancy highlights the necessity of resynthesis-based recoverability evaluation when assessing DSRTs for accent generation: while ABX accessibility captures relative trends, it cannot reliably identify optimal layers for synthesis.
L195: ### 5.2 ASR Supervision Removes Accent Information
L196: ASR supervision reduces the recoverability and accessibility of accent information in DSRTs across layers, shown in Figure cite52†2 (blue curve for HuBERT-ft, orange curve for Whisper). (1) HuBERT consistently shows higher accent recoverability and accessibility than HuBERT-ft or Whisper, particularly in latter layers, which are more affected by ASR supervision.
L197: (2) Whisper exhibits a peak in accent and phonetic information at intermediate layers (L12 & L15), different from the distribution of information in HuBERT or HuBERT-ft.
L198: ### 5.3 Reducing Codebook Size Provides Limited Disentanglement
L199: We then vary codebook sizes for three selected layers: HuBERT L18 (a common choice, as in Vevo zhang2025vevo), HuBERT-ft L18 (a layer with little accent information while retaining high phonetic information), and HuBERT L9 (a layer with most accent information), shown in Figure cite54†3 . (1) Focusing on accent recoverability, varying codebook sizes has a markedly smaller effect than changing representation models or layers.
L200: For each layer, increasing codebook sizes from 32 to 2048 consistently improves accent and phonetic recoverability across all inspected DSRTs. However, the recoverability gap induced by codebook sizes variation within a layer is substantially smaller than that induced by changing layers at a fixed codebook sizes. (2) Speaker and phonetic recoverability also increase with larger codebook sizes.
L201: Taking HuBERT DSRTs as an example, Accent COS-SIM drops sharply as codebook sizes decreases from 1024 to 32, while PPG distance also rises 20.4%. Despite speaker identity being partially suppressed by the injected speaker ID during resynthesis, speaker recoverability also declines. The parallel degradation across accent, speaker, and phonetic metrics suggests minimal disentanglement when reducing codebook size.
L202: ### 5.4 Limitations of Commonly Used DSRTs in Speech Generation
L203: Based on the above findings, we highlight the limitations of commonly used DSRTs here. (1) Vevo’s choice of using DSTRs based on HuBERT L18 with codebook size 32 as content tokens and codebook size 8,192 as content-style tokens zhang2025vevo is suboptimal. Significant accent information is likely already lost and unrecoverable in HuBERT L18 - leading to insufficient accent information encoded in content-style tokens.
L204: Since naive reduction of codebook size cannot remove accent without harming phonetic information, content tokens achieve little accent information at the cost of intelligibility in resynthesised speech. (2) ASR-supervised DSRTs, adopted by du2024cosyvoice, exhibit lower peak accent and phonetic recoverability than HuBERT DSRTs. Similar to content-style tokens, ASR-supervised DSRTs cannot encode accent sufficiently.
L205: ### 5.5 Proposed Content and Content-Accent Tokens
L206: For better accent generation and control, we propose content-accent and content tokens for accent-preserving and accent-adaptive VC, respectively. A comparison of proposed tokens and Vevo tokens is presented in Table cite55†1 . Our proposed content/content-accent tokens achieve better performance than Vevo’s content/content-style tokens across all metrics, enabling better control of accent in speech generation. Demos of the converted speech will be available at [Link redacted].
L207: ## 6 Discussion
L208: 
L209: We observed a systematic delay of the optimal accessible layer relative to the recoverability peak. As discussed in (yeh2024estimating), earlier layers retain more complete acoustic information that can be effectively extracted by a strong HiFiGAN vocoder, whereas later layers gain phonetic discriminability from ASR-related objectives,
L210: Across both metrics, accent information follows a distinct yet intermediate trend between phonetic and speaker information. This aligns with linguistic intuition: accent is partially realised through systematic phonetic variation and partially through speaker-specific pronunciation traits.
L211: Layer selection enables accent control precisely because accent, speaker, and phonetic information are distributed differently across layers. Consequently, a single "style layer", as suggested by the content–style token design in Vevo, is insufficient to jointly capture multiple speech attributes such as content, accent, and emotion.
L212: A more thorough investigation of more speech attributes, and how their information are represented across multiple layers and representations, is therefore necessary to support better controllable speech generation.
L213: Finally, our findings provide potential explanations for the hallucinated accents by ZS-TTS systems zhong2025accentbox. Many ZS-TTS systems rely on representations (often deep or supervised layers) where accent recoverability is already attenuated, encouraging the model to guess accent patterns in inference or default to mainstream accents in training data.
L214: ## 7 Conclusion
L215: 
L216: In this work, we propose a framework for evaluating discrete speech representation tokens (DSRTs) from both recoverability and accessibility perspectives, in terms of accent, speaker, and phonetic information encoded, with a focus on providing guidance for accent generation and control. Based on the results using this framework on HuBERT- and Whipser-based DSRTs, we propose content and content-accent tokens, achieving more controllable accent in voice conversion (VC) than existing works.
L217: ## Limitations
L218: Although the framework we proposed guided us to develop a pair of DSRTs achieving good control over accent in VC, we acknowledge several limitations. First, we did not evaluate the proposed DSRTs in ZS-TTS settings, as training ZS-TTS systems requires substantial computational resources. Future work will extend our evaluation to ZS-TTS to assess the generalisability of our framework beyond voice conversion. Second, the current Accent ABX test shows low accent accessibility across all evaluated DSRTs.
L219: A supervised accent representation (GenAID zhong2025accentbox) achieves much lower ABX error rate (9.87%), indicating the validity of the metric. More powerful probing models are needed to better reveal subtle accent information in SSL representations and DSRTs without explicit accent-discriminative training, so as to provide more precise guidance for accent applications.
L220: Better design of DSRTs is also needed to make accent information more accessible, and thus easier to learn by downstream speech generation models. Third, our experiments are limited to English SSL models and the VCTK dataset, which contains only L1 English speaker accents. We plan to extend the framework to multilingual representations and datasets involving L2 English accents and non-English languages to improve regional and language coverage.
L221: Finally, we focus on objective metrics to evaluate DSRTs and their effectiveness in VC. We haven’t included subjective evaluation and listening test, as zhong2025pairwise have shown the effectiveness of the adopted objective metrics on evaluating accent generation, correlating with subjective listening tests results.
L222: ## Broader Impacts and Ethical Statements
L223: This work improves the transparency and controllability of accent information in discrete speech representation tokens (DSRTs). The proposed framework may help mitigate accent hallucination and unintended accent drift, benefiting speakers with underrepresented accents and potentially supporting applications such as speech therapy through accent- and voice-preserving speech generation.
L224: Our results further suggest that accent control can be partially achieved via informed representation and layer selection, potentially reducing reliance on additional large-scale model training.
L225: Although this work is intended for research use, enhanced accent controllability in speech generation could be misused for voice impersonation if deployed without safeguards. If extended to real-world or unseen speakers, practical systems should incorporate mechanisms to ensure speaker approval and to detect synthesized speech. We emphasise that our framework is designed to analyse and expose limitations of DSRTs rather than to enable unrestricted accent manipulation.
L226: This study exclusively uses existing publicly available datasets and pretrained models for research purposes, without collecting new data or releasing derived datasets. All data and pre-trained models are used under the following licenses: Creative Commons BY 4.0 License, Creative Commons BY-NC-ND 4.0 License, Apache License 2.0, and MIT License.
L227: ## Acknowledgments
L228: 
L229: This work was supported in part by the UKRI AI Centre for Doctoral Training in Responsible and Trustworthy in-the-world Natural Language Processing (Grant EP/Y030656/1), UKRI Centre for Doctoral Training in Natural Language Processing (Grant EP/S022481/1), School of Informatics, and School of Philosophy, Psychology & Language Sciences, the University of Edinburgh. We would like to thank Dr. Hao Tang and Dr. Tianzi Wang for useful discussion.
L230: 
L231: ## References
L232: ## Appendix A ABX Conditions
L233: 
L234: ABX type  | on $(A=X\neq B)$  | by $(A=B=X)$  | across $(A\neq X)$
L235: Accent  | accent  | word  | speaker
L236: Speaker  | speaker  | word, accent  | —
L237: Phone  | phone  | phone, context^{∗}  | speaker
L238: Table 2: Different ABX conditions for selecting $(a,b,x)$ triplets to evaluate accent, speaker, and phonetic information accessibility.
L239: ^{∗}: context refers to the previous and next phones.
L240: When selecting $(a,b,x)$ triplets, a condition can be described as ABX ON the category of interest, BY the category of controlled constant among triplets, ACROSS the category of free variables among triplets. The classic Phone ABX select triplets ON phone BY context, where 1) $x$ and $a$ share the same phone, with $b$ of a different phone, and 2) $x$, $a$, and $b$ share identical phonetic context, e.g. bit \textipa[bIt] vs beat \textipa[bi:t].
L241: To evaluate how prominent phonetic information is, compared to other variables, such as speaker, most Phone ABX would also be conditioned ACROSS speaker, with $a$ and $b$ coming from the same speaker, with $x$ from a different speaker, e.g. $x=$ \textipa[bIt] by speaker_1, $a=$ \textipa[bIt] by speaker_2, $b=$ \textipa[bi:t] by speaker_2. Table cite56†2 lists the three different ABX conditions we use to evaluate accent, speaker, and phonetic information accessibility.
L242: ## Appendix B Selected ABX Accent-word Combination
L243: 
L244: After obtained a list of (accent $A$ and $B$, word) combinations with scores measured on GenAID features, we take the first p% of combination with lowest scores, which captures the most typical accent-specific pronunciation differences. A grid search on $p\%$ is performed over 2.5%, 5%, 10%, 15% and 20%, and we reported results at 10%, which is the lowest percentage where the score starts to show a converging trend.
L245: We take the first 25 selected combination as an example, presented in Table cite57†3 .
L246: Accent  | Word  | Accent_{b}
L247: SouthernEnglish  | first  | Scottish
L248: NorthernEnglish  | first  | Scottish
L249: SouthernEnglish  | Scottish  | Irish
L250: SouthernEnglish  | however  | Scottish
L251: SouthernEnglish  | work  | Scottish
L252: NorthernEnglish  | however  | Scottish
L253: Irish  | last  | Scottish
L254: Scottish  | Scottish  | Irish
L255: NorthernEnglish  | Scottish  | Irish
L256: SouthernEnglish  | work  | Irish
L257: NorthernEnglish  | their  | Scottish
L258: SouthernEnglish  | first  | Irish
L259: NorthernEnglish  | however  | Irish
L260: SouthernEnglish  | however  | Irish
L261: SouthernEnglish  | their  | Scottish
L262: SouthernEnglish  | never  | Scottish
L263: SouthernEnglish  | year  | Scottish
L264: SouthernEnglish  | next  | Irish
L265: SouthernEnglish  | Mr.  | Scottish
L266: NorthernEnglish  | year  | Scottish
L267: NorthernEnglish  | other  | Irish
L268: SouthernEnglish  | other  | Irish
L269: Scottish  | first  | SouthernEnglish
L270: SouthernEnglish  | from  | Irish
L271: Scottish  | first  | NorthernEnglish
L272: Table 3: An example of the 25 triplet of (Accent $A$, Accent $B$, word) with lowest ABX error rates, selected based on GenAID zhong2025accentbox features on VCTK, applying to evaluate DSRTs accent ABX error rate in the test.
L273: The table reveals a few well-established phonetic dimensions that underlie accent discrimination, successfully captured by our data-driven method. First, rhoticity emerges as a dominant cue. Words such as first and work sharply distinguish Southern or Northern English from Scottish and Irish accents, reflecting the systematic presence of post-vocalic /r/ in Scottish and Irish English and its absence in Southern English. The table shows that our metric takes good advantage of using rhoticity difference.
L274: Second, differences in vowel quality, particularly in stressed lexical vowels, play a central role. For instance, first and year involve the near-front vowel spaces, which are realized as long centralized vowels in Southern English but shift toward more open or fronted realizations in Scottish and Irish English.
L275: Third, consonantal realization, especially of /t/, contributes substantially to discrimination. Words such as scottish and last contain environments where Scottish English strongly favors glottal or lenited realizations of /t/, in contrast to the more alveolar realizations found in Southern and Irish English.
L276: Finally, patterns of vowel reduction and weak-form realization further differentiate accents. Function words such as however, other, and from show strong schwa reduction in Southern English, whereas Irish and Scottish English tend to preserve fuller vowel qualities. These differences in reduction strategies, particularly in unstressed positions, amplify accent contrasts and explain why relevant accent-word combiantion are picked in the table.
L277: From the analysis above, we can see the accent-word combination selected to evaluate accent ABX has a strong grounding in phonetic feature. The low accent accessibility results shown in Figure cite39†4 and cite54†3 authentically reflect the lack of accessible accent encoding in current speech representations and DSRTs.
L278: ## Appendix C Accent and Speaker Partition in Cross-Accent Voice Conversion
L279: 
L280: See Table cite58†4 .
L281: Accent Group  | Accent Region  | Split  | Speaker IDs
L282: Seen during HiFiGAN training & Accent ABX word selection  | Southern English  | Train/Valid  | p225, p226, p228, p229, p231, p232, p239, p240, p243, p250, p254, p257, p258
L283:  |  | Test  | p268, p273, p274, p276
L284:  | Northern English  | Train/Valid  | p227, p230, p233, p236, p244, p256, p259, p267, p269, p270, p278, p279
L285:  |  | Test  | p277, p282, p286, p287
L286:  | Scottish  | Train/Valid  | p234, p237, p241, p246, p247, p249, p252, p255, p260, p262, p263, p271, p272, p275, p281
L287:  |  | Test  | p264, p265, p284, p285
L288:  | Irish  | Train/Valid  | p245, p266, p283, p288, p295
L289:  |  | Test  | p298, p313, p340, p364
L290: Likely seen during RepCodec training  | Canadian  | Test  | p316, p317, p343, p363
L291:  | American Northeast  | Test  | p315, p339, p360, p361
L292:  | American Midwest  | Test  | p311, p333, p334, p341
L293:  | American South  | Test  | p301, p308, p310, p345
L294:  | American West  | Test  | p294, p299, p300, p318
L295: Unseen accents  | Northern Irish  | Test  | p292, p293, p304, p351
L296:  | South African  | Test  | p314, p323, p336, p347
L297:  | Indian  | Test  | p248, p251, p376
L298:  | Oceanian  | Test  | p326, p335, p374
L299: Table 4: Accent grouping and train/test splits for VCTK speakers. Accents are grouped by whether they were seen during HiFiGAN training & Accent ABX word selection, likely seen during RepCodec training, or unseen during training.
L300: ## Appendix D Full Evaluation Results
L301: 
L302: Due to page limits, we report additional results here. Accent COS-SIM (to tar), Speaker COS-SIM (to tar), and WER exhibit reverse/similar trend, compared to Accent COS-SIM (to src), Speaker COS-SIM (to src), and PPG Distance, and are thus omitted in Figure cite52†2 and cite54†3 . Information accessibility evaluation results across codebook sizes are also reported here in Figure cite54†3 .
L303: cite59†Image: Refer to caption Figure 4: Accent, speaker, and phonetic information in different DSRTs across layers and representations.
L304: Full version of Figure cite52†2 . cite60†Image: Refer to caption Figure 5: Accent, speaker, and phonetic information in different DSRTs across codebook sizes.
L305: Full version of Figure cite54†3 .
L306: 
L307: Experimental support, please cite61†view the build logs for errors. Generated by cite62†L A T E xml†math.nist.gov .
L308: ## Instructions for reporting errors
L309: 
L310: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L311: 
L312:   * Click the "Report Issue" () button, located in the page header.
L313: 
L314: Tip: You can select the relevant text first, to include it in your report.
L315: Our team has already identified cite63†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L316: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite64†list of packages that need conversion†github.com , and welcome cite65†developer contributions†github.com .
L317: 
L318: We gratefully acknowledge support from our major funders, cite66†member institutions†info.arxiv.org , , and all contributors.
L319: cite67†About†info.arxiv.org · cite68†Help†info.arxiv.org · cite69†Contact†info.arxiv.org · cite70†Subscribe†info.arxiv.org · cite71†Copyright†info.arxiv.org · cite72†Privacy†info.arxiv.org · cite73†Accessibility†info.arxiv.org · cite74†Operational Status (opens in new tab)†status.arxiv.org L320: 
L321: Major funding support from

