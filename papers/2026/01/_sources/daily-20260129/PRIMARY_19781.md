# Exact-v1 necessary primary excerpts — 2601.19781

Preserved original responses; local L labels are scoped to each response. No revised-version or unrelated appendix sweep.

## Original response 1: jan29_stdnext5head

PHONOLOGICAL TOKENIZER: PROSODY-AWARE PHONETIC TOKEN VIA MULTI-OBJECTIVE FINE-TUNING WITH DIFFERENTIABLE K-MEANS (https://arxiv.org/html/2601.19781v1)
citeturn28451view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19781v1","lineno":null}); Total lines: 264

## Original response 2: jan29_stdnext5core

PHONOLOGICAL TOKENIZER: PROSODY-AWARE PHONETIC TOKEN VIA MULTI-OBJECTIVE FINE-TUNING WITH DIFFERENTIABLE K-MEANS (https://arxiv.org/html/2601.19781v1)
citeturn28453view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28451view1","lineno":70}); Total lines: 264
L54: Several recent studies partially address this need by incorporating a pretrained SSL model into the learning of acoustic tokens to enhance their ability to capture linguistic information [cite38†49 , cite39†8 , cite40†46 ], known as hybrid tokens. However, these methods are mainly based on the residual vector quantization (RVQ) framework and the overall representation remains essentially a multi-codebook acoustic token.
L55: Thus, fully leveraging the advantages of these tokens requires additional, somewhat complex architectures in downstream models to manage multiple streams effectively. Also, the use of multiple codebooks inherently reduces data compression efficiency, which is the key advantages of discrete representations [cite41†3 , cite42†41 ].
L56: In this study, we propose the Phonological Tokenizer: a single-codebook speech tokenizer that captures the holistic phonological aspects of speech, namely linguistic and prosodic information, while discarding unnecessary acoustic details such as background noise and speaker identity. We leverage the flexible discretization capability of the recently proposed differentiable k-means [cite43†33 ] to build this tokenizer.
L57: We fine-tune phonetic tokens obtained from a pre-trained SSL model using differentiable k-means in a multi-objective framework combining ASR and speech resynthesis. The resulting tokenizer demonstrates high performance in both speech understanding and generation tasks, as well as in speechLM applications.
L58: The key strengths of our approach are summarized as follows:
L59: 
L60:   * •
L61: Balancing prosody preservation and speaker information removal: We fine-tune phonetic tokens for both ASR and speech resynthesis with weighted losses, along with conditioning the vocoder on speaker embeddings during training. As a result, our method effectively incorporates prosodic information while preserving the ability of phonetic tokens to capture linguistic information and discard speaker information.
L62: It exhibits especially strong performance in tasks where prosody is crucial, such as emotion recognition, voice conversion, and speechLMs.
L63:   * •
L64: 
L65: High compression efficiency: By optimizing SSL-based phonetic tokens using differentiable k-means [cite43†33 , cite44†12 ], our method enables fine-tuning of token properties while maintaining a single codebook. This achieves significantly higher data compression efficiency compared to multi-codebook acoustic tokens, while showing superior or comparable performance to baseline tokenizers [cite38†49 , cite45†4 , cite46†19 ] on many tasks.
L66: 
L67:   * •
L68: Reduced training data requirement: Since our approach fine-tunes a pre-trained large-scale speech foundation model (WavLM-large [cite45†4 ]), it can build a versatile speech tokenizer with only small training data. In this study, we fine-tune phonetic tokens using 44 hours of additional training data (VCTK corpus [cite47†40 ]) to modify its properties.
L69: This represents a substantially smaller data requirement compared to prior studies [cite38†49 , cite46†19 ] using large-scale datasets such as LibriSpeech (960h) [cite48†34 ] or LibriTTS (585h) [cite49†48 ].
L70: ## 2 Related Works
L71: ### 2.1 Hybrid tokens utilizing pretrained SSL models
L72: Several prior studies have proposed hybrid tokens that extend RVQ-based acoustic tokens by integrating pre-trained SSL models to better capture linguistic content [cite38†49 , cite39†8 , cite40†46 ]. These tokens demonstrate superior language understanding capabilities compared to acoustic tokens, which are trained solely for reconstruction. However, as discussed in Introduction, these tokens consist of multiple codebooks, which results in low efficiency and limited usability.
L73: In this study, we propose hybrid tokens based on phonetic tokens by fine-tuning them using differentiable k-means, enabling a single codebook.
L74: ### 2.2 Supervised tokenizers
L75: 
L76: Several studies have proposed ASR-based tokenizers that allow tokens to better capture linguistic information [cite50†37 , cite51†10 ]. Our previous work [cite43†33 ], which optimized phonetic tokens for ASR using differentiable k-means, can also be categorized as this type of tokens. In this work, we further extend this idea by fine-tuning phonetic tokens with multi-objective of ASR and speech resynthesis.
L77: ### 2.3 Disentanglement-oriented codec tokens
L78: Several prior studies have proposed codec-based tokens designed to promote disentanglement by representing global information, such as speaker identity, in separate branches [cite52†36 , cite53†20 , cite54†15 ]. However, approaches based on phonetic tokens have not yet been explored. In this work, we aim to incorporate prosodic information into phonetic tokens in which speaker information is already suppressed, through fine-tuning within a multi-task learning framework.
L79: ## 3 Multi-objective Optimization
L80: with Differentiable K-means
L81: 
L82: cite55†Image: Refer to caption Figure 1: Architecture of the Phonological Tokenizer: multi-objective fine-tuning of SSL-derived phonetic tokens
L83: ### 3.1 Phonetic token optimization via differentiable k-means
L84: Our previous study [cite43†33 ] proposed to optimize discrete tokens obtained from SSL models for specific purposes by introducing differentiable k-means.
L85: The ASR loss $\mathcal{L}^{\text{asr}}$ is used to jointly optimize all components of the model: 1) the SSL model $\theta_{\text{ssl}}$, performing feature extraction $\mathrm{SSL}(X;\theta_{\text{ssl}})$ from the input speech $X$; 2) the cluster centroids $M$, used for the differentiable k-means $\mathrm{DiffKM}(\cdot;M)$ to discretize the SSL features; and 3) the ASR model $\theta_{\text{asr}}$, predicting the text transcription $Y$ from the token sequence via $\mathrm{ASR}(\cdot;\theta_{\text{asr}})$.
L86:  | $\displaystyle\mathcal{L}^{\text{asr}}\Bigl(Y,\,\mathrm{ASR}\bigl(\mathrm{DiffKM}\bigl(\mathrm{SSL}(X;\,\theta_{\text{ssl}});\,M\bigr);\,\theta_{\text{asr}}\bigr)\Bigr)$  |  | (1)
L87: 
L88: This approach not only improved the accuracy of ASR but also modified the properties of the tokens, enabling them to represent purer linguistic information. This demonstrates the effectiveness of differentiable k-means in manipulating the properties of discrete tokens.
L89: ### 3.2 Proposed method: multi-objective optimization
L90: In this study, we propose to extend the loss function in Eq. (cite56†1 ) by incorporating a weighted reconstruction loss, to achieve Phonological Tokenizer, which retains linguistic and prosodic information while appropriately removing speaker information. The ASR loss $\mathcal{L}^{\text{asr}}$ encourages the extraction of linguistic information while suppressing prosody and speaker information.
L91: In contrast, the reconstruction loss $\mathcal{L}^{\text{voc}}$ drives the tokens to capture all the acoustic details, including prosody and speaker identity. Thus, these two losses can be seen as tuning the token properties toward those of the phonetic and acoustic tokens, respectively. Therefore, to obtain the Phonological Tokenizer that has intermediate properties between phonetic and acoustic tokens, it is reasonable to balance these two losses and optimize the tokens in a multi-task manner.
L92:  |  | $\displaystyle\mathcal{L}=(1-\alpha)\,\mathcal{L}^{\text{asr}}\Bigl(Y,\,\mathrm{ASR}\bigl(\mathrm{DiffKM}\bigl(\mathrm{SSL}(X;\,\theta_{\text{ssl}});\,M\bigr);\,\theta_{\text{asr}}\bigr)\Bigr)$  |
L93:  |  | $\displaystyle+\alpha\,\mathcal{L}^{\text{voc}}\Bigl(X,\,\mathrm{Voc}\bigl(\mathrm{DiffKM}\bigl(\mathrm{SSL}(X;\,\theta_{\text{ssl}});\,M\bigr),E_{\text{spk}};\,\theta_{\text{voc}}\bigr)\Bigr)$  |  | (2)
L94: We weight these two losses using $\alpha$. Both the ASR model $\theta_{\text{asr}}$ used for transcription $\mathrm{ASR}(\cdot;\theta_{\text{asr}})$ and the vocoder $\theta_{\text{voc}}$ for resynthesis $\mathrm{Voc}(\cdot;\theta_{\text{voc}})$ are trained using the discrete tokens obtained through differentiable k-means as a shared input. Thus, the tokens are optimized for both tasks in a balanced way.
L95: In order to help disentangle speaker information from the tokens, we employed a pre-trained speaker encoder to provide the speaker embedding $E_{\text{spk}}$ as an auxiliary conditioning input to the vocoder.
L96: An overview of our tokenizer is presented in Fig. cite57†1 . During training, the entire module, except for the speaker encoder, is jointly optimized. At inference time, discrete tokens are generated using only the fine-tuned SSL model $\theta_{\text{ssl}}$ followed by differentiable k-means with learned cluster centroids $M$.
L97: ## 4 Experiments
L98: ### 4.1 Experimental setup
L99: The model training was conducted using ESPnet [cite58†42 ]. The configuration related to differentiable k-means followed the settings described in [cite43†33 ], and the cluster size was set to 2000. For the SSL model, we used the 21st layer of WavLM-large [cite45†4 ], and the cluster centroids $M$ were initialized using standard k-means clustering, trained on a 30-hour subset of the LibriSpeech-100h dataset [cite48†34 ].
L100: For ASR, we employed the joint CTC/attantion-based encoder-decoder (AED) model [cite59†22 ], and for the vocoder, we used HiFi-GAN [cite60†23 ]^{2}^{2} 2 cite61†https://github.com/kan-bayashi/ParallelWaveGAN†github.com . As the speaker encoder, we adopted a pretrained ECAPA-TDNN model [cite62†9 ]^{3}^{3} 3 cite63†https://hf.co/speechbrain/spkrec-ecapa-voxceleb†hf.co . As described in [cite43†33 ], training was conducted in two stages.

## Original response 3: jan29_stdnext5eval

PHONOLOGICAL TOKENIZER: PROSODY-AWARE PHONETIC TOKEN VIA MULTI-OBJECTIVE FINE-TUNING WITH DIFFERENTIABLE K-MEANS (https://arxiv.org/html/2601.19781v1)
citeturn28454view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28451view1","lineno":100}); Total lines: 264
L86:  | $\displaystyle\mathcal{L}^{\text{asr}}\Bigl(Y,\,\mathrm{ASR}\bigl(\mathrm{DiffKM}\bigl(\mathrm{SSL}(X;\,\theta_{\text{ssl}});\,M\bigr);\,\theta_{\text{asr}}\bigr)\Bigr)$  |  | (1)
L87: 
L88: This approach not only improved the accuracy of ASR but also modified the properties of the tokens, enabling them to represent purer linguistic information. This demonstrates the effectiveness of differentiable k-means in manipulating the properties of discrete tokens.
L89: ### 3.2 Proposed method: multi-objective optimization
L90: In this study, we propose to extend the loss function in Eq. (cite56†1 ) by incorporating a weighted reconstruction loss, to achieve Phonological Tokenizer, which retains linguistic and prosodic information while appropriately removing speaker information. The ASR loss $\mathcal{L}^{\text{asr}}$ encourages the extraction of linguistic information while suppressing prosody and speaker information.
L91: In contrast, the reconstruction loss $\mathcal{L}^{\text{voc}}$ drives the tokens to capture all the acoustic details, including prosody and speaker identity. Thus, these two losses can be seen as tuning the token properties toward those of the phonetic and acoustic tokens, respectively. Therefore, to obtain the Phonological Tokenizer that has intermediate properties between phonetic and acoustic tokens, it is reasonable to balance these two losses and optimize the tokens in a multi-task manner.
L92:  |  | $\displaystyle\mathcal{L}=(1-\alpha)\,\mathcal{L}^{\text{asr}}\Bigl(Y,\,\mathrm{ASR}\bigl(\mathrm{DiffKM}\bigl(\mathrm{SSL}(X;\,\theta_{\text{ssl}});\,M\bigr);\,\theta_{\text{asr}}\bigr)\Bigr)$  |
L93:  |  | $\displaystyle+\alpha\,\mathcal{L}^{\text{voc}}\Bigl(X,\,\mathrm{Voc}\bigl(\mathrm{DiffKM}\bigl(\mathrm{SSL}(X;\,\theta_{\text{ssl}});\,M\bigr),E_{\text{spk}};\,\theta_{\text{voc}}\bigr)\Bigr)$  |  | (2)
L94: We weight these two losses using $\alpha$. Both the ASR model $\theta_{\text{asr}}$ used for transcription $\mathrm{ASR}(\cdot;\theta_{\text{asr}})$ and the vocoder $\theta_{\text{voc}}$ for resynthesis $\mathrm{Voc}(\cdot;\theta_{\text{voc}})$ are trained using the discrete tokens obtained through differentiable k-means as a shared input. Thus, the tokens are optimized for both tasks in a balanced way.
L95: In order to help disentangle speaker information from the tokens, we employed a pre-trained speaker encoder to provide the speaker embedding $E_{\text{spk}}$ as an auxiliary conditioning input to the vocoder.
L96: An overview of our tokenizer is presented in Fig. cite57†1 . During training, the entire module, except for the speaker encoder, is jointly optimized. At inference time, discrete tokens are generated using only the fine-tuned SSL model $\theta_{\text{ssl}}$ followed by differentiable k-means with learned cluster centroids $M$.
L97: ## 4 Experiments
L98: ### 4.1 Experimental setup
L99: The model training was conducted using ESPnet [cite58†42 ]. The configuration related to differentiable k-means followed the settings described in [cite43†33 ], and the cluster size was set to 2000. For the SSL model, we used the 21st layer of WavLM-large [cite45†4 ], and the cluster centroids $M$ were initialized using standard k-means clustering, trained on a 30-hour subset of the LibriSpeech-100h dataset [cite48†34 ].
L100: For ASR, we employed the joint CTC/attantion-based encoder-decoder (AED) model [cite59†22 ], and for the vocoder, we used HiFi-GAN [cite60†23 ]^{2}^{2} 2 cite61†https://github.com/kan-bayashi/ParallelWaveGAN†github.com . As the speaker encoder, we adopted a pretrained ECAPA-TDNN model [cite62†9 ]^{3}^{3} 3 cite63†https://hf.co/speechbrain/spkrec-ecapa-voxceleb†hf.co . As described in [cite43†33 ], training was conducted in two stages.
L101: In the first stage, the SSL model $\theta_{\text{ssl}}$ and cluster centroids $M$ were kept frozen, and only the ASR $\theta_{\text{asr}}$ and vocoder $\theta_{\text{voc}}$ components were trained for 30 epochs with a learning rate of 1e-4. In the second stage, the entire module, including the SSL model $\theta_{\text{ssl}}$ and centroids $M$ (except the speaker encoder) was fine-tuned for 60 epochs with a learning rate of 1e-5.
L102: The vocoder training included adversarial learning, with the discriminator updated concurrently throughout both stages.
L103: Training was conducted using the VCTK corpus [cite47†40 ] with speed perturbation ($\times$0.9, 1.0, and 1.1). We adopted $\alpha=0.1$^{4}^{4} 4 See Sec.cite19†4.5 for the results of the ablation study as the weight for the vocoder loss (in Eq.(cite64†2 )). For reference, we also show the results for $\alpha=0$ and $\alpha=1$, where the tokens are fine-tuned with single-task objectives of ASR and vocoder, respectively.
L104: In the following experiments, we used the tokens obtained from the trained model to perform various discrete token-based speech tasks, and compared their performance with that of existing models. As baselines, we used WavLM (21st layer) followed by standard offline k-means clustering (k=2000) as phonetic token. We also used SpeechTokenizer [cite38†49 ] (using only the first codebook) trained on LibriSpeech as hybrid token, and WavTokenizer [cite46†19 ] trained on LibriTTS as acoustic token.
L105: We present a comparison of the basic properties of these baseline tokens and our proposed tokens in Table cite65†1 . This shows that once initialized with phonetic tokens, our tokens can be effectively fine-tuned with very limited additional data, while keeping high compression efficiency.
L106: Table 1: Statistics of baseline and proposed tokens
L107: 
L108:  |  |  | Bit  | Vocab.  | Tokens  | Train
L109:  |  |  | rate  | size  | /sec.  | data
L110: Baseline  | Discrete WavLM  | (phonetic)  | 548.3  | 2000  | 50  | 1 30h
L111: SpeechTokenizer  | (hybrid)  | 500.0  | 1024  | 50  | 960h
L112: WavTokenizer  | (acoustic)  | 900.0  | 4096  | 75  | 585h
L113: Proposed  | Phonological Tokenizer  | 548.3  | 2000  | 50  | 30 + 44h
L114: ### 4.2 Evaluation on discriminative tasks
L115: 
L116: Table 2: Discriminative task performance: ASR on librispeech-100 & Emotion Recognition (ER) on Ravdess & Speaker Identification (SID) on VoxCeleb. The best result in each column is bolded.
L117:  |  |  | ASR  | ER  | SID
L118:  |  |  | WER (test-{clean / other})  | acc.  | acc.
L119:  |  |  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)
L120: Baseline  | Discrete WavLM  | (phonetic)  | 1 4.3/1 7.1  | 41.7  | 27.7
L121: SpeechTokenizer  | (hybrid)  | 1 9.3/23.5  | 39.2  | 29.1
L122: WavTokenizer  | (acoustic)  | 96.7/96.8  | 24.2  | 82.7
L123: Single-task  | ASR-only [cite43†33 ]  | ($\alpha=0$)  | 1 4.0/1 7.0  | 41.7  | 20.6
L124: Optimized  | Voc-only  | ($\alpha=1$)  | 10.4/27.7  | 40.0  | 49.0
L125: Proposed  | Phonological  | ($\alpha=0.1$)  | 1 4.6/1 8.5  | 51.7  | 29.5
L126: Tokenizer
L127: We first evaluated the performance of Phonological Tokenizer on discriminative tasks. Focusing on three distinct aspects, linguistic information, prosody, and speaker identity, we trained downstream models for ASR, emotion recognition (ER), and speaker identification (SID). For ASR, we trained joint CTC/AED models using LibriSpeech-100h. For ER, we trained ECAPA-TDNN models on RAVDESS [cite66†25 ], a dataset of the same sentences spoken with different emotions, using a speaker-independent split.
L128: For SID, we trained ECAPA-TDNN models on VoxCeleb1 [cite67†30 ].
L129: The results are shown in Table cite68†2 .
L130: 
L131: ASR: Our Phonological Tokenizer, while showing slightly lower performance than Discrete WavLM, demonstrated clear superiority over both SpeechTokenizer and WavTokenizer. This indicates that our token represents sufficient linguistic information. Considering the substantial drop observed when optimized solely for reconstruction ($\alpha=1$), our multi-task framework seems effective in preserving the capability of phonetic tokens for capturing linguistic content.
L132: ER: The Phonological Tokenizer achieved by far the best performance. This indicates that our proposed tokens successfully capture prosodic information in a speaker-independent manner.
L133: SID: The Phonological Tokenizer properly showed quite low accuracy as observed in Discrete WavLM and SpeechTokenizer, indicating minimal speaker information in the tokens. The lower performance of Voc-only ($\alpha=1$) compared to WavTokenizer, despite being trained only for reconstruction, suggests that using an SSL model and conditioning the vocoder with speaker embeddings are effective for disentangling speaker information from the tokens.
L134: Overall, the results indicate that our Phonological Tokenizer successfully captures prosodic information (as shown in ER) while preserving the ability of phonetic tokens to capture linguistic information (in ASR) and suppress speaker information (in SID).
L135: ### 4.3 Evaluation on generative tasks
L136: 
L137: Table 3: Generative task performance: reconstruction on in-domain LJSpeech & voice conversion on out-of-domain neutral read speech (TIMIT) and expressive speech (Expresso). The best result in each column is bolded, and those that outperform all baselines are underlined.
L138:  |  |  | LJSpeech reconstruction (ID)  | TIMIT VC (OOD)  | Expresso VC (OOD)
L139:  |  |  | MCD  | F0 RMSE  | UTMOS  | WER  | F0 corr.  | SpkSim  | UTMOS  | WER  | F0 corr.  | SpkSim  | UTMOS  | WER
L140:  |  |  | ($\downarrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)
L141: Baseline  | Discrete WavLM  | (phonetic)  | 5.64  | 0.289  | 3.81  | 2.8  | 0.371  | 0.757  | 3.63  | 10.3  | 0.382  | 0.737  | 3.47  | 12.2
L142: SpeechTokenizer  | (hybrid)  | 5.35  | 0.270  | 3.91  | 3.3  | 0.383  | 0.726  | 3.53  | 18.6  | 0.388  | 0.706  | 3.13  | 24.0
L143: WavTokenizer  | (acoustic)  | 4.47  | 0.176  | 4.13  | 2.7  | 0.356  | 0.256  | 2.02  | 34.0  | 0.520  | 0.352  | 2.24  | 27.7
L144: Single-task  | ASR-only [cite43†33 ]  | ($\alpha=0$)  | 5.77  | 0.300  | 3.82  | 2.9  | 0.385  | 0.756  | 3.70  | 10.6  | 0.391  | 0.738  | 3.61  | 12.6
L145: Optimized  | Voc-only  | ($\alpha=1$)  | 4.42  | 0.183  | 4.08  | 3.3  | 0.484  | 0.695  | 3.70  | 16.4  | 0.543  | 0.608  | 2.96  | 26.8
L146: Proposed  | Phonological  | ($\alpha=0.1$)  | 4.99  | 0.208  | 4.06  | 2.9  | 0.456  | 0.762  | 3.88  | 1 9.8  | 0.538  | 0.724  | 3.58  | 12.6
L147: Tokenizer

## Original response 4: jan29_stdnext5tail

PHONOLOGICAL TOKENIZER: PROSODY-AWARE PHONETIC TOKEN VIA MULTI-OBJECTIVE FINE-TUNING WITH DIFFERENTIABLE K-MEANS (https://arxiv.org/html/2601.19781v1)
citeturn28456view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28451view1","lineno":148}); Total lines: 264
L138:  |  |  | LJSpeech reconstruction (ID)  | TIMIT VC (OOD)  | Expresso VC (OOD)
L139:  |  |  | MCD  | F0 RMSE  | UTMOS  | WER  | F0 corr.  | SpkSim  | UTMOS  | WER  | F0 corr.  | SpkSim  | UTMOS  | WER
L140:  |  |  | ($\downarrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)
L141: Baseline  | Discrete WavLM  | (phonetic)  | 5.64  | 0.289  | 3.81  | 2.8  | 0.371  | 0.757  | 3.63  | 10.3  | 0.382  | 0.737  | 3.47  | 12.2
L142: SpeechTokenizer  | (hybrid)  | 5.35  | 0.270  | 3.91  | 3.3  | 0.383  | 0.726  | 3.53  | 18.6  | 0.388  | 0.706  | 3.13  | 24.0
L143: WavTokenizer  | (acoustic)  | 4.47  | 0.176  | 4.13  | 2.7  | 0.356  | 0.256  | 2.02  | 34.0  | 0.520  | 0.352  | 2.24  | 27.7
L144: Single-task  | ASR-only [cite43†33 ]  | ($\alpha=0$)  | 5.77  | 0.300  | 3.82  | 2.9  | 0.385  | 0.756  | 3.70  | 10.6  | 0.391  | 0.738  | 3.61  | 12.6
L145: Optimized  | Voc-only  | ($\alpha=1$)  | 4.42  | 0.183  | 4.08  | 3.3  | 0.484  | 0.695  | 3.70  | 16.4  | 0.543  | 0.608  | 2.96  | 26.8
L146: Proposed  | Phonological  | ($\alpha=0.1$)  | 4.99  | 0.208  | 4.06  | 2.9  | 0.456  | 0.762  | 3.88  | 1 9.8  | 0.538  | 0.724  | 3.58  | 12.6
L147: Tokenizer
L148: We then evaluated performances on generative tasks. We trained unit HiFi-GAN on the LJSpeech [cite69†18 ] with the obtained tokens. The evaluation is done both on reconstruction on in-domain (ID) LJSpeech and on voice conversion (VC) on out-of-domain (OOD) corpora. In VC, the tokens from OOD speech are input to the LJSpeech-trained vocoder to generate speech in the voice of LJSpeech speaker.
L149: If the tokens appropriately preserve only the linguistic and prosodic information, the output should maintain the spoken content and speaking style of the input while converting only the voice timbre to that of LJSpeech. As OOD data, we used TIMIT [cite70†13 ] as neutral read speech and Expresso [cite71†32 ] as expressive speech. For ID reconstruction, we evaluated mel cepstral distortion (MCD) and F0 root mean square error (F0 RMSE).
L150: For OOD VC, we evaluated F0 correlation (F0 corr.) with the source speech and speaker similarity (SpkSim) with the target speaker of LJSpeech. To assess overall quality, we checked UTMOS [cite72†38 ] and WER computed from Whisper-large-v3 [cite73†35 ] transcriptions for both tasks.
L151: The results are shown in Table cite74†3 .
L152: LJSpeech reconstruction (ID): Across all the metrics, our model outperformed or matched Discrete WavLM and SpeechTokenizer. Although not as good as WavTokenizer, the degradation in UTMOS and WER was minimal. This demonstrates that our Phonological Tokenizer is sufficiently effective for generative tasks. While our token does not retain fine-grained acoustic details sufficient for precise signal-level reconstruction, it is still effective enough to enable highly natural and intelligible speech synthesis.
L153: TIMIT VC (OOD): The Phonological Tokenizer outperformed all the baselines across all the metrics. Although it was slightly worse than the Voc-only ($\alpha=1$) in F0 corr., it achieved the best performance in all other metrics. This demonstrates its ability to retain prosodic information while removing source speaker identity (as also shown in Sec. cite16†4.2 ) and to enable high-quality speech synthesis.
L154: Expresso VC (OOD): Our model outperformed all the baselines in F0 corr. and UTMOS, but SpkSim and WER were not as good as Discrete WavLM and ASR-only ($\alpha=0$). This is likely because these evaluation metrics tend to favor neutral speech over emotional speech.
L155: Indeed, listening to our demo site^{5}^{5} 5 cite75†https://ondatk68.github.io/onda-demo/projects/phonological-tokenizer†ondatk68.github.io , you can find that when using these tokens that focus on linguistic information, the output speech sounds neutral, regardless of the speaking style of the input speech. In contrast, the Phonological Tokenizer reproduces both the target speaker identity and the speaking style of the input speech.
L156: This is particularly interesting considering that both our tokenizer and the vocoder were trained without using any emotional speech.
L157: Overall, the results showed that the Phonological Tokenizer is sufficiently useful for speech synthesis tasks. Our tokens showed only slight degradation even compared to acoustic token baseline (WavTokenizer) in ID reconstruction. Also, the overall strong performance of our tokens on OOD VC indicates that the Phonological Tokenizer successfully disentangles prosodic and speaker information, which is consistent with the ER and SID results in Sec. cite16†4.2 .

## Original response 5: jan29_stdnext5finish

PHONOLOGICAL TOKENIZER: PROSODY-AWARE PHONETIC TOKEN VIA MULTI-OBJECTIVE FINE-TUNING WITH DIFFERENTIABLE K-MEANS (https://arxiv.org/html/2601.19781v1)
citeturn28464view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19781v1","lineno":151}); Total lines: 264
L134: Overall, the results indicate that our Phonological Tokenizer successfully captures prosodic information (as shown in ER) while preserving the ability of phonetic tokens to capture linguistic information (in ASR) and suppress speaker information (in SID).
L135: ### 4.3 Evaluation on generative tasks
L136: 
L137: Table 3: Generative task performance: reconstruction on in-domain LJSpeech & voice conversion on out-of-domain neutral read speech (TIMIT) and expressive speech (Expresso). The best result in each column is bolded, and those that outperform all baselines are underlined.
L138:  |  |  | LJSpeech reconstruction (ID)  | TIMIT VC (OOD)  | Expresso VC (OOD)
L139:  |  |  | MCD  | F0 RMSE  | UTMOS  | WER  | F0 corr.  | SpkSim  | UTMOS  | WER  | F0 corr.  | SpkSim  | UTMOS  | WER
L140:  |  |  | ($\downarrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)
L141: Baseline  | Discrete WavLM  | (phonetic)  | 5.64  | 0.289  | 3.81  | 2.8  | 0.371  | 0.757  | 3.63  | 10.3  | 0.382  | 0.737  | 3.47  | 12.2
L142: SpeechTokenizer  | (hybrid)  | 5.35  | 0.270  | 3.91  | 3.3  | 0.383  | 0.726  | 3.53  | 18.6  | 0.388  | 0.706  | 3.13  | 24.0
L143: WavTokenizer  | (acoustic)  | 4.47  | 0.176  | 4.13  | 2.7  | 0.356  | 0.256  | 2.02  | 34.0  | 0.520  | 0.352  | 2.24  | 27.7
L144: Single-task  | ASR-only [cite43†33 ]  | ($\alpha=0$)  | 5.77  | 0.300  | 3.82  | 2.9  | 0.385  | 0.756  | 3.70  | 10.6  | 0.391  | 0.738  | 3.61  | 12.6
L145: Optimized  | Voc-only  | ($\alpha=1$)  | 4.42  | 0.183  | 4.08  | 3.3  | 0.484  | 0.695  | 3.70  | 16.4  | 0.543  | 0.608  | 2.96  | 26.8
L146: Proposed  | Phonological  | ($\alpha=0.1$)  | 4.99  | 0.208  | 4.06  | 2.9  | 0.456  | 0.762  | 3.88  | 1 9.8  | 0.538  | 0.724  | 3.58  | 12.6
L147: Tokenizer
L148: We then evaluated performances on generative tasks. We trained unit HiFi-GAN on the LJSpeech [cite69†18 ] with the obtained tokens. The evaluation is done both on reconstruction on in-domain (ID) LJSpeech and on voice conversion (VC) on out-of-domain (OOD) corpora. In VC, the tokens from OOD speech are input to the LJSpeech-trained vocoder to generate speech in the voice of LJSpeech speaker.
L149: If the tokens appropriately preserve only the linguistic and prosodic information, the output should maintain the spoken content and speaking style of the input while converting only the voice timbre to that of LJSpeech. As OOD data, we used TIMIT [cite70†13 ] as neutral read speech and Expresso [cite71†32 ] as expressive speech. For ID reconstruction, we evaluated mel cepstral distortion (MCD) and F0 root mean square error (F0 RMSE).
L150: For OOD VC, we evaluated F0 correlation (F0 corr.) with the source speech and speaker similarity (SpkSim) with the target speaker of LJSpeech. To assess overall quality, we checked UTMOS [cite72†38 ] and WER computed from Whisper-large-v3 [cite73†35 ] transcriptions for both tasks.
L151: The results are shown in Table cite74†3 .
L152: LJSpeech reconstruction (ID): Across all the metrics, our model outperformed or matched Discrete WavLM and SpeechTokenizer. Although not as good as WavTokenizer, the degradation in UTMOS and WER was minimal. This demonstrates that our Phonological Tokenizer is sufficiently effective for generative tasks. While our token does not retain fine-grained acoustic details sufficient for precise signal-level reconstruction, it is still effective enough to enable highly natural and intelligible speech synthesis.
L153: TIMIT VC (OOD): The Phonological Tokenizer outperformed all the baselines across all the metrics. Although it was slightly worse than the Voc-only ($\alpha=1$) in F0 corr., it achieved the best performance in all other metrics. This demonstrates its ability to retain prosodic information while removing source speaker identity (as also shown in Sec. cite16†4.2 ) and to enable high-quality speech synthesis.
L154: Expresso VC (OOD): Our model outperformed all the baselines in F0 corr. and UTMOS, but SpkSim and WER were not as good as Discrete WavLM and ASR-only ($\alpha=0$). This is likely because these evaluation metrics tend to favor neutral speech over emotional speech.
L155: Indeed, listening to our demo site^{5}^{5} 5 cite75†https://ondatk68.github.io/onda-demo/projects/phonological-tokenizer†ondatk68.github.io , you can find that when using these tokens that focus on linguistic information, the output speech sounds neutral, regardless of the speaking style of the input speech. In contrast, the Phonological Tokenizer reproduces both the target speaker identity and the speaking style of the input speech.
L156: This is particularly interesting considering that both our tokenizer and the vocoder were trained without using any emotional speech.
L157: Overall, the results showed that the Phonological Tokenizer is sufficiently useful for speech synthesis tasks. Our tokens showed only slight degradation even compared to acoustic token baseline (WavTokenizer) in ID reconstruction. Also, the overall strong performance of our tokens on OOD VC indicates that the Phonological Tokenizer successfully disentangles prosodic and speaker information, which is consistent with the ER and SID results in Sec. cite16†4.2 .
L158: ### 4.4 Evaluation on speechLMs
L159: 
L160: Table 4: SpeechLM performance: sWUGGY and sBLIMP for lexical and syntactic knowledge; sentiment and speaker consistency for awareness to paralinguistic and non-linguistic aspects; and assesments of the quality of generated speech continuations.
L161:  |  |  | ZeroSpeech  | SALMon  | Speech Continuation
L162:  |  |  | (consistency)
L163:  |  |  | sWUGGY  | sBLIMP  | Sent.  | Spk  | GenPPL  | UTMOS
L164:  |  |  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\uparrow$)  | ($\downarrow$)  | ($\uparrow$)
L165: Baseline  | Discrete WavLM  | (phonetic)  | 68.6  | 57.1  | 80.5  | 86.0  | 5.81  | 3.60
L166: SpeechTokenizer  | (hybrid)  | 66.4  | 54.4  | 59.5  | 65.0  | 5.73  | 3.64
L167: WavTokenizer  | (acoustic)  | 52.5  | 49.3  | 66.0  | 74.0  | 6.34  | 2.57
L168: Single-task  | ASR-only [cite43†33 ]  | ($\alpha=0$)  | 70.0  | 59.7  | 61.0  | 61.0  | 5.60  | 3.56
L169: Optimized  | Voc-only  | ($\alpha=1$)  | 56.9  | 51.2  | 62.5  | 79.5  | 6.40  | 3.67
L170: Proposed  | Phonological  | $(\alpha=0.1$)  | 67.0  | 55.2  | 67.5  | 66.0  | 5.60  | 3.86
L171: Tokenizer
L172: Lastly, we trained speechLMs using the obtained tokens and evaluated their performance. We used the slam recipe [cite76†26 ] based on Qwen2.5-0.5B [cite77†44 ]. We used the 6,000-hour subset of LibriLight [cite78†21 ] as training data and trained each model for 4 epochs. As evaluation metrics, we adopted sWUGGY and sBLIMP from the Zero Resource Speech Challenge [cite79†11 ] to assess lexical and syntactic knowledge.
L173: To measure awareness to paralinguistic and non-linguistic information, we used SALMon’s sentimental and speaker consistency metrics [cite80†27 ]. Additionally, to evaluate the quality of speech continuations generated by the speechLMs, we checked generative perplexity (GenPPL) and UTMOS. To calculate GenPPL, we first transcribed the generated speech using Whisper-large-v3, and then calculated perplexity using Llama-3.2-1B [cite81†14 ], following [cite76†26 ].
L174: The results are shown in Table cite82†4 . The results of ZeroSpeech, which focuses on linguistic information, and the sentimental and speaker consistency results from SALMon, largely align with the ASR, ER, and SID results reported in Sec. cite16†4.2 . In ZeroSpeech, the Phonological Tokenizer performed slightly worse than Discrete WavLM and ASR-only ($\alpha=0$), but still outperformed the other baselines.
L175: In SALMon, Discrete WavLM achieved exceptionally high scores contrary to the results of ER and SID, but the Phonological Tokenizer exhibited the second highest sentimental consistency, while its speaker consistency was lower than that of WavTokenizer and the Voc-only ($\alpha=1$). For speech continuation, the Phonological Tokenizer achieved the best performance in both GenPPL and UTMOS.
L176: These results highlights that the speechLM constructed with our proposed tokens achieved high naturalness in both spoken content and speech quality in the speech continuation task.
L177: ### 4.5 Ablation study on the vocoder loss weight
L178: We conducted an ablation study on the vocoder loss weight $\alpha$ (in Eq.(cite64†2 )). Fig. cite83†2 presents the results for the discriminative tasks (ASR, ER, and SID) and the generative tasks (only for TIMIT VC). For the results of the discriminative tasks, increasing $\alpha$ gradually degrades ASR performance while improving SID. However, ER achieves its optimal value at $\alpha=0.3$.
L179: This suggests that increasing $\alpha$ allows both prosodic and speaker information to be encoded in the tokens, but too large value of $\alpha$ make it more difficult to disentangle prosody and speaker timbre. For the results of the generative tasks, increasing $\alpha$ leads to higher F0 corr., but when $\alpha=1$, SpkSim decreases largely.

## Original response 6: jan29_stdnext5last

PHONOLOGICAL TOKENIZER: PROSODY-AWARE PHONETIC TOKEN VIA MULTI-OBJECTIVE FINE-TUNING WITH DIFFERENTIABLE K-MEANS (https://arxiv.org/html/2601.19781v1)
citeturn28465view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19781v1","lineno":178}); Total lines: 264
L173: To measure awareness to paralinguistic and non-linguistic information, we used SALMon’s sentimental and speaker consistency metrics [cite80†27 ]. Additionally, to evaluate the quality of speech continuations generated by the speechLMs, we checked generative perplexity (GenPPL) and UTMOS. To calculate GenPPL, we first transcribed the generated speech using Whisper-large-v3, and then calculated perplexity using Llama-3.2-1B [cite81†14 ], following [cite76†26 ].
L174: The results are shown in Table cite82†4 . The results of ZeroSpeech, which focuses on linguistic information, and the sentimental and speaker consistency results from SALMon, largely align with the ASR, ER, and SID results reported in Sec. cite16†4.2 . In ZeroSpeech, the Phonological Tokenizer performed slightly worse than Discrete WavLM and ASR-only ($\alpha=0$), but still outperformed the other baselines.
L175: In SALMon, Discrete WavLM achieved exceptionally high scores contrary to the results of ER and SID, but the Phonological Tokenizer exhibited the second highest sentimental consistency, while its speaker consistency was lower than that of WavTokenizer and the Voc-only ($\alpha=1$). For speech continuation, the Phonological Tokenizer achieved the best performance in both GenPPL and UTMOS.
L176: These results highlights that the speechLM constructed with our proposed tokens achieved high naturalness in both spoken content and speech quality in the speech continuation task.
L177: ### 4.5 Ablation study on the vocoder loss weight
L178: We conducted an ablation study on the vocoder loss weight $\alpha$ (in Eq.(cite64†2 )). Fig. cite83†2 presents the results for the discriminative tasks (ASR, ER, and SID) and the generative tasks (only for TIMIT VC). For the results of the discriminative tasks, increasing $\alpha$ gradually degrades ASR performance while improving SID. However, ER achieves its optimal value at $\alpha=0.3$.
L179: This suggests that increasing $\alpha$ allows both prosodic and speaker information to be encoded in the tokens, but too large value of $\alpha$ make it more difficult to disentangle prosody and speaker timbre. For the results of the generative tasks, increasing $\alpha$ leads to higher F0 corr., but when $\alpha=1$, SpkSim decreases largely.
L180: The low UTMOS at the two ends can be attributed to different factors: at $\alpha=0$, due to the absence of prosody, and at $\alpha=1$, due to the inclusion of unnecessary speaker information. These results highlight the advantage of our Phonological Tokenizer, which is trained in a multi-task manner to achieve balanced properties between acoustic and phonetic tokens.
L181: cite84†Image: Refer to caption Figure 2: Ablation results for the vocoder loss weight $\alpha$: (a) Discriminative tasks (ASR, ER, SID), (b) generative task (TIMIT VC).
L182: ## 5 Conclusions
L183: In this work, we propose the Phonological Tokenizer, which has intermediate properties between acoustic and phonetic tokens. The tokenizer is obtained by fine-tuning phonetic tokens through differentiable k-means using a multi-objective of ASR and speech reconstruction. Experimental results across diverse downstream tasks, including speechLMs, demonstrate that the resulting tokens achieve strong performance in capturing linguistic and prosodic information while appropriately disentangling speaker identity.
L184: Our tokens showed the best results in prosody-sensitive tasks (ER, VC, and speech continuation in speechLM) among all the token tested, and also surpassed hybrid token baseline, SpeechTokenizer, in all the tasks including speech understanding and generation. Moreover, the fact that our tokenizer relies on a single codebook and trained with only a small amount of data, further underscores the advantages of our method.
L185: Future work includes scaling up the training data for enhanced performance, as well as enabling inference-time controllability for more flexible adjustment of token properties.
L186: ## References
L187:   * [1] S. Arora, K. Chang, C. Chien, Y. Peng, H. Wu, Y. Adi, E. Dupoux, H. Lee, K. Livescu, and S. Watanabe (2025) On the landscape of spoken language models: a comprehensive survey. TMLR. External Links: 2504.08528, cite85†Link Cited by: cite86†§1 .
L188:   * [2] X. Chang, J. Shi, J. Tian, Y. Wu, Y. Tang, Y. Wu, S. Watanabe, Y. Adi, X. Chen, and Q. Jin (2024) The Interspeech 2024 challenge on speech processing using discrete units. In Interspeech, External Links: cite87†Document†dx.doi.org , ISSN 2958-1796 Cited by: cite86†§1 .
L189:   * [3] X. Chang, B. Yan, K. Choi, J. Jung, Y. Lu, S. Maiti, R. Sharma, J. Shi, J. Tian, S. Watanabe, Y. Fujita, T. Maekaku, P. Guo, Y. Cheng, P. Denisov, K. Saijo, and H. Wang (2024) Exploring speech recognition, translation, and understanding with discrete speech units: a comparative study. In ICASSP, Vol. . External Links: cite88†Document†dx.doi.org Cited by: cite89†§1 .
L190:   * [4] S. Chen, C. Wang, Z. Chen, Y. Wu, S. Liu, Z. Chen, J. Li, N. Kanda, T. Yoshioka, X. Xiao, J. Wu, L. Zhou, S. Ren, Y. Qian, Y. Qian, M. Zeng, and F. Wei (2021) WavLM: large-scale self-supervised pre-training for full stack speech processing. JSTSP 16. External Links: cite90†Link†api.semanticscholar.org Cited by: cite91†2nd item , cite92†3rd item , cite93†§4.1 .
L191:   * [5] K. Choi, A. Pasad, T. Nakamura, S. Fukayama, K. Livescu, and S. Watanabe (2024) Self-Supervised Speech Representations are More Phonetic than Semantic. In Interspeech, External Links: cite94†Document†dx.doi.org , ISSN 2958-1796 Cited by: cite95†footnote 1 .
L192:   * [6] A. Cutler, D. Dahan, and W. Van Donselaar (1997) Prosody in the comprehension of spoken language: a literature review. Language and speech 40 (2). Cited by: cite89†§1 .

