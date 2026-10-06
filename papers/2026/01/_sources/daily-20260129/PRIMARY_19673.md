# Exact-v1 primary cached excerpts — 2601.19673

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Existing parsed-page cache recovery

A Benchmark for Audio Reasoning Capabilities of Multimodal Large Language Models (https://arxiv.org/html/2601.19673v1)
citeturn28401view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28181view1","lineno":165}); Total lines: 1681
L149: Five of the tasks required additional utterances spoken by different speakers. The samples for voice cloning were selected from the GLOBE dataset (cite78†Wang et al., 2024 ). As with selecting the prompt for the questions, the samples were transcribed using the Whisper medium model, used as prompts for voice cloning, and transcribed again. Thus, after human evaluation, 10 samples (one per speaker) were selected to synthesize utterances.
L150: One of the tasks, Cross-Recording Language Identification, required utterances in languages other than English. For this purpose, we used the VoxPopuli dataset (cite70†Wang et al., 2021 ). We selected four languages – Estonian, Finnish, Hungarian and Polish. For each language, we identified speakers for which WER obtained with the Whisper medium model was equal to 0. We then narrowed our selection to recordings with a duration between 2 and 5 seconds.
L151: This process resulted in the selection of three speakers (one utterance each) for each language.
L152: The last type of audio recordings, sounds, included short sounds of e.g. an animal, tunes, and background noises. All sounds were manually selected from samples available under the Creative Commons 0 license in the Freesound dataset (cite79†Font et al., 2013 ), resulting in 13 short sounds, four short tunes, and eight background sounds. The short sounds were manually trimmed as necessary to include a single sound event per sample.
L153: For speech synthesis, we utilized a pipeline based on Voicebox (cite80†Le et al., 2023 ), a text-to-speech model that demonstrates zero-shot capabilities in reconstructing audio segments from textual inputs and speech prompts. The architecture adapts the transformer model (cite81†Vaswani et al., 2017 ), with modifications including the use of rotary positional embedding (cite82†Su et al., 2023 ) instead of ALiBi self-attention bias (cite83†Press et al., 2022 ).
L154: To predict token durations, we employ a DurationPredictor model, similar to Voicebox but smaller in size. We also utilize CTC-based forced alignment to discover token durations in an unsupervised manner. A HiFi-GAN vocoder (cite84†Kong et al., 2020 ) is used to map audio features to speech, consisting of a fully convolutional generator and two discriminators. The input tokens are represented as phonetic labels, and mel-scale spectrograms with 80 channels are used as audio features.
L155: Table 3: Results of model evaluation on the ART benchmark using Yes/No approach.
L156: Model  | % Relevant  | Absolute Accuracy  | Relative Accuracy
L157: Whisper + Llama  | 99.91  | 0.5404  | 0.5408
L158: Whisper + Qwen  | 99.94  | 0.5621  | 0.5625
L159: Audio Flamingo 3  | 100.00  | 0.5473  | 0.5473
L160: GAMA  | 42.56  | 0.2155  | 0.5064
L161: Qwen-Audio-Chat  | 64.09  | 0.3312  | 0.5168
L162: Qwen2-Audio (zero-shot)  | 85.41  | 0.4431  | 0.5188
L163: Qwen2-Audio (one-shot, same template)  | 87.30  | 0.4710  | 0.5395
L164: Qwen2-Audio (one-shot, different template)  | 68.08  | 0.3526  | 0.5179
L165: Ultravox v0.4.1  | 89.19  | 0.4682  | 0.5250
L166: Ultravox v0.6  | 99.74  | 0.5309  | 0.5323
L167: After obtaining all necessary samples of questions, utterances, and sounds, the audio recordings were automatically merged according to the prepared template configurations. All recordings were normalized to -20 dBFS. The duration of silence between the question and the utterance or sound was manually adjusted to ensure that audio prompts sound natural and that the gaps between recordings are sufficient to distinguish them.
L168: The short sounds and tunes concatenated with a question were truncated to the maximum duration of 5 seconds, and a fade-out was applied to eliminate sudden volume changes. In the case of instances that required an overlay of background sounds, the underlying audio was attenuated by 20 dB to ensure speech intelligibility, and both fade-in and fade-out were applied.
L169: The consolidation of templates resulted in 9 000 samples that constitute the final dataset, which amounts to over 30 hours of audio, as shown in Table cite85†2 . The prepared dataset is fully balanced across labels and tasks. Of the 9 000 total samples, 4 500 have the expected answer of Yes and 4 500 have the expected answer of No. This balance is maintained within each of the nine tasks, with 1 000 samples evenly split between 500 Yes and 500 No instances.
L170: Furthermore, the balance was maintained at the level of task templates wherever possible. For instance, in the Audio Transformation Detection task, template ATD_0 has 56 Yes and 56 No samples; template ATD_1 has 56/56; template ATD_2 has 112/112; and template ATD_3 has 276/276. This ensures a uniform distribution of labels across tasks.
L171: ## 4 Experiments
L172: Table 4: Absolute accuracy per task on the ART benchmark using Yes/No approach.
L173: Model  | AA  | ATD  | CRLI  | CRSI  | STI  | SR  | SFC  | TSR  | TTLR
L174: Whisper + Llama  | 0.505  | 0.483  | 0.458  | 0.505  | 0.665  | 0.525  | 0.557  | 0.643  | 0.521
L175: Whisper + Qwen  | 0.510  | 0.504  | 0.551  | 0.501  | 0.625  | 0.654  | 0.532  | 0.653  | 0.528
L176: Audio Flamingo 3  | 0.516  | 0.492  | 0.569  | 0.517  | 0.554  | 0.700  | 0.494  | 0.566  | 0.517
L177: GAMA  | 0.036  | 0.376  | 0.276  | 0.349  | 0.338  | 0.050  | 0.299  | 0.068  | 0.147
L178: Qwen-Audio-Chat  | 0.498  | 0.521  | 0.008  | 0.123  | 0.201  | 0.549  | 0.181  | 0.525  | 0.375
L179: Qwen2-Audio
L180: (zero-shot)  | 0.488  | 0.517  | 0.501  | 0.212  | 0.532  | 0.432  | 0.524  | 0.358  | 0.425
L181: Qwen2-Audio
L182: (one-shot, same template)  | 0.493  | 0.282  | 0.517  | 0.454  | 0.534  | 0.517  | 0.527  | 0.543  | 0.373
L183: Qwen2-Audio
L184: (one-shot, different template)  | 0.441  | 0.245  | 0.464  | 0.340  | 0.477  | 0.176  | 0.467  | 0.392  | 0.172
L185: Ultravox v0.4.1  | 0.475  | 0.288  | 0.516  | 0.489  | 0.478  | 0.438  | 0.507  | 0.511  | 0.512
L186: Ultravox v0.6  | 0.480  | 0.501  | 0.579  | 0.504  | 0.559  | 0.526  | 0.521  | 0.590  | 0.513
L187: Average  | 0.436  | 0.413  | 0.430  | 0.386  | 0.490  | 0.430  | 0.457  | 0.476  | 0.396
L188: ### 4.1 Setup
L189: 
L190: We conducted a series of experiments evaluating multimodal models on prepared tasks. Two different approaches were adopted:
L191: 
L192:   * •
L193: 
L194: Yes/No – where the model was instructed to answer only Yes or No,
L195: 
L196:   * •
L197: 
L198: Descriptive – where the form of the answer was not specified and the model was allowed to give a descriptive answer.
L199: As all the tasks were designed to have either an affirmative or negative answer, we focused on Yes/No approach in this section. However, to gain better understanding of the reasons why the models fail to accomplish the tasks, we also studied the open-ended responses yielded by Descriptive approach with summary scores reported in Table cite86†5 and the detailed analysis given in Appendix cite43†E .
L200: To ensure the reliability of the results, the responses obtained using Yes/No approach were automatically evaluated. If the answer was Yes or No, it was marked as relevant, and irrelevant otherwise. The responses marked as relevant were further classified as correct or incorrect. As LLM-as-a-judge is a commonly used evaluation method, we decided to use it in the Descriptive approach.
L201: For this purpose, we used two models – Llama-3.3-70B-Instruct (cite51†Grattafiori et al., 2024 ) and Qwen3-32B (cite87†Yang et al., 2025 ). In the prompt, the model was instructed that it would receive a question, an expected answer and the received answer. Its task was to determine whether the generated answer was relevant or not, and to state whether it was correct or why it was labeled as irrelevant. The full prompt used for this evaluation is shown in Appendix cite42†D , along with the inference parameters.
L202: ### 4.2 Yes/No approach
L203: 
L204: The results of evaluation using Yes/No approach are shown in Table cite88†3 . The relative accuracy is defined as the accuracy calculated only on relevant responses. In this case, the models were instructed to answer only Yes or No. The inference on each of the models was run five times and the results were averaged to assess whether the models exhibit superiority over random guessing.
L205: Two cascaded systems where evaluated, both using Whisper Large v3 (cite58†Radford et al., 2023 ) to obtain transcriptions of the audio prompts. First system used Llama-3.3-70B-Instruct (cite51†Grattafiori et al., 2024 ) to answer the questions, and the second one utilized Qwen3-32B (cite87†Yang et al., 2025 ). Both cascaded systems generated almost 100% relevant answers, achieving 54.04% and 56.21% absolute accuracy, respectively.
L206: Considering MLLMs, Audio Flamingo 3 (cite89†Goel et al., 2025 ) is the only model that returned 100% relevant answers. It also outperformed the other models with the accuracy of 54.73%. Ultravox-v0.6-Llama3.3-70B (cite52†Fixie.ai, 2025 ) obtained the second highest number of relevant responses. It managed to achieve absolute accuracy of 53.09%. The previous version of this model, Ultravox-v0.4.1-Llama3.1-8B, generated 10% less relevant responses, achieving less than 50% absolute accuracy in all five runs.
--------------------------------------------------------------------------------

## Existing parsed-page cache recovery 2

A Benchmark for Audio Reasoning Capabilities of Multimodal Large Language Models (https://arxiv.org/html/2601.19673v1)
citeturn28403view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28181view1","lineno":210}); Total lines: 1681
L200: To ensure the reliability of the results, the responses obtained using Yes/No approach were automatically evaluated. If the answer was Yes or No, it was marked as relevant, and irrelevant otherwise. The responses marked as relevant were further classified as correct or incorrect. As LLM-as-a-judge is a commonly used evaluation method, we decided to use it in the Descriptive approach.
L201: For this purpose, we used two models – Llama-3.3-70B-Instruct (cite51†Grattafiori et al., 2024 ) and Qwen3-32B (cite87†Yang et al., 2025 ). In the prompt, the model was instructed that it would receive a question, an expected answer and the received answer. Its task was to determine whether the generated answer was relevant or not, and to state whether it was correct or why it was labeled as irrelevant. The full prompt used for this evaluation is shown in Appendix cite42†D , along with the inference parameters.
L202: ### 4.2 Yes/No approach
L203: 
L204: The results of evaluation using Yes/No approach are shown in Table cite88†3 . The relative accuracy is defined as the accuracy calculated only on relevant responses. In this case, the models were instructed to answer only Yes or No. The inference on each of the models was run five times and the results were averaged to assess whether the models exhibit superiority over random guessing.
L205: Two cascaded systems where evaluated, both using Whisper Large v3 (cite58†Radford et al., 2023 ) to obtain transcriptions of the audio prompts. First system used Llama-3.3-70B-Instruct (cite51†Grattafiori et al., 2024 ) to answer the questions, and the second one utilized Qwen3-32B (cite87†Yang et al., 2025 ). Both cascaded systems generated almost 100% relevant answers, achieving 54.04% and 56.21% absolute accuracy, respectively.
L206: Considering MLLMs, Audio Flamingo 3 (cite89†Goel et al., 2025 ) is the only model that returned 100% relevant answers. It also outperformed the other models with the accuracy of 54.73%. Ultravox-v0.6-Llama3.3-70B (cite52†Fixie.ai, 2025 ) obtained the second highest number of relevant responses. It managed to achieve absolute accuracy of 53.09%. The previous version of this model, Ultravox-v0.4.1-Llama3.1-8B, generated 10% less relevant responses, achieving less than 50% absolute accuracy in all five runs.
L207: Qwen2-Audio-7B-Instruct (cite90†Chu et al., 2023 ) generated only 85.41% relevant responses in the zero-shot approach. As the authors of this model suggest using the one-shot approach, two additional experiments were performed. In the first experiment, the model was given a sample from the same template as an example. This resulted in less than 2% more relevant answers and less than 3% greater accuracy.
L208: In the second experiment, the model was given as an example a sample from the same task but a different template. This approach resulted in a 17% decrease in the number of relevant responses and a 9% decrease in accuracy compared to zero-shot approach. The lowest results in the Qwen family of models were achieved by Qwen-Audio-Chat (cite90†Chu et al., 2023 ). It generated only 64.09% relevant responses, achieving average absolute accuracy of 33.12%.
L209: The GAMA model (cite91†Ghosh et al., 2024 ) reached only 21.55% accuracy, which was the lowest in the evaluation using Yes/No approach.
L210: The results per task achieved by the models for the Yes/No approach are shown in Table cite92†4 . Based on these, the Cross Recording Speaker Identification proved to be the hardest task – the average absolute accuracy is 38.63% and none of the models achieved accuracy higher than 50% in any of the five runs. Of these, the best average absolute accuracy was achieved for the Selective Text Inference task.
L211: Table 5: Results of the model evaluation on the ART benchmark using Descriptive approach.
L212:  | Llama 3.3  | Qwen3  |
L213: Model  | Relevant  | Accuracy  | Relevant  | Accuracy  | Agreement
L214: Whisper + Llama  | 62.62%  | 0.3535  | 62.17%  | 0.4834  | 74.07%
L215: Whisper + Qwen  | 89.68%  | 0.4882  | 87.97%  | 0.5697  | 76.09%
L216: Audio Flamingo 3  | 74.07%  | 0.3536  | 76.99%  | 0.3524  | 82.10%
L217: GAMA  | 1.31%  | 0.0089  | 2.40%  | 0.0154  | 97.30%
L218: Qwen-Audio-Chat  | 14.50%  | 0.0778  | 19.89%  | 0.0548  | 86.04%
L219: Qwen2-Audio
L220: (zero-shot)  | 92.26%  | 0.4490  | 94.94%  | 0.4683  | 82.43%
L221: Qwen2-Audio
L222: (one-shot, same template)  | 93.94%  | 0.4735  | 96.36%  | 0.4996  | 83.31%
L223: Qwen2-Audio
L224: (one-shot, different template)  | 93.16%  | 0.4495  | 95.28%  | 0.4834  | 81.30%
L225: Ultravox v0.4.1  | 60.20%  | 0.2398  | 50.59%  | 0.1692  | 76.19%
L226: Ultravox v0.6  | 79.42%  | 0.3952  | 77.69%  | 0.4425  | 77.14%
L227: ### 4.3 Descriptive approach
L228: 
L229: Table cite86†5 shows the results of the experiments performed with the Descriptive approach and both Llama and Qwen3 as a judge.
L230: According to both judges, none of the models achieved satisfactory results. Only the cascaded system using Qwen3 achieved absolute accuracy higher than 50%, but only when it evaluated itself. The agreement between judges exceeded 74% in all cases, and the highest value reached was 97.3%. However, this case involved the GAMA model, which had an accuracy of less than 2.5%.
L231: Among the MLLMs, Qwen2-Audio in the one-shot approach using the same template as an example, achieved the best results – Llama 3.3 and Qwen3 judged it achieved 47.35% and 49.96% accuracy, respectively. This experiment also resulted in the highest fraction of relevant answers.
L232: It is worth noting that Llama 3.3 recognized more relevant answers when judging itself, Qwen3, and both Ultravox v0.4.1 and Ultravox v0.6. On the other hand, Qwen3 was significantly more indulgent when evaluating the MLLMs from the Qwen family of models.
L233: An in-depth analysis of the results per task in the Descriptive approach is available in Appendix cite43†E . In case of cascaded systems, Qwen3 assessed its own performance significantly better across all tasks except for Speech Features Comparison. The best average accuracy was obtained on the Speech Features Comparison task when judged by Llama 3.3, and on Text and Sound Reasoning judged by Qwen3.
L234: However, the results on the remaining tasks are significantly understated due to the accuracy obtained by Qwen-Audio-Chat (5.48-7.78%) and GAMA (0.89-1.54%).
L235: ### 4.4 Error analysis
L236: 
L237: Error analysis for both approaches revealed distinct yet overlapping failure patterns based on human evaluation. Errors in the Yes/No approach were primarily driven by failures in audio understanding. Specifically, models did not recognize the presence of speech or sound. Additionally, there was systematic task confusion, which led to transcription or speaker recognition instead of question answering.
L238: In contrast, the Descriptive approach exhibited a broader and more heterogeneous set of errors. In addition to frequently failing to recognize the question, the models often produced random, speculative, or language-inconsistent responses and showed stronger biases toward transcription and speaker identification. These behaviors suggest less stable response control in case of the Descriptive approach.
L239: Overall, the results suggest that both approaches are susceptible to task misinterpretation. However, in the Yes/No approach errors are concentrated around audio perception and task confusion. In contrast, the Descriptive approach results in more diverse and less predictable failure behaviors. A quantitative analysis is provided in Appendix cite45†G .
L240: ## 5 Benchmark Validation
L241: 
L242: Although the task collection process described in Section cite8†3 relies on human expertise and clearly defined rules, the task instantiation procedure depends on templates and synthesized speech which may potentially result in a benchmark that is either too complex to be comprehensible by humans or too simple for models to solve.
L243: To address the first issue, we designated ART-H, a subset of the dataset that consists of 24 samples per task resulting in 216 samples in total, that enables manual verification of the evaluation results in under one hour. We presented ART-H prompts to human evaluators, who answered the questions with either Yes or No. In this way, we achieved a human baseline of 92.90%, thus confirming the suitability of the prepared tasks.
L244: Three tasks – Audio Arithmetics, Selective Text Inference, and Text and Temporal Localization Reasoning – turned out to be the easiest. The worst results were obtained on Speech Features Comparison and Cross-Recording Language Identification. The reason may be that these tasks focus on distinguishing accents or languages, which can be challenging for those unfamiliar with a particular dialect. Detailed results of the human evaluation are provided in Appendix cite41†C .
L245: Furthermore, to verify if the choice of particular samples to be included in ART-H impacts the results in a meaningful way, we evaluated the models under study with respect to randomly sampled 216-element subsets of ART and demonstrated that this procedure results in a standard deviation of less than $0.035$ in terms of absolute accuracy (cf. Appendix cite48†H ).
L246: The reliance on synthesized samples raises concerns about the impact of the audio quality on the benchmark results. If the benchmark encompasses audio samples of poor quality, the models could underperform due to artefacts in data. Taking into consideration that we use a state-of-the-art TTS model and perform human evaluation of the ART-H subset, this is not the case. On the other hand, high-quality synthesis can potentially lead to overoptimistic results in speech-related tasks.
L247: However, the dependence on synthesized speech ensures that any mistakes observed in the models’ performance are due to reasoning errors rather than poor or ambiguous input. If a model demonstrates weak performance on clean audio samples, it will likely perform worse in noisy conditions. The results presented in Section cite12†4 show that none of the models attained satisfactory performance with regard to the synthesized data.
--------------------------------------------------------------------------------



## Original response 1: latepoint0

A Benchmark for Audio Reasoning Capabilities of Multimodal Large Language Models (https://arxiv.org/html/2601.19673v1)
citeturn28181view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19673v1","lineno":null}); Total lines: 1681
--------------------------------------------------------------------------------


## Original response 2: latepoint1

A Benchmark for Audio Reasoning Capabilities of Multimodal Large Language Models (https://arxiv.org/html/2601.19673v1)
citeturn28182view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19673v1","pattern":"2 Dataset"}); Total lines: 1681
No matching text found for "2 Dataset"

## Original response 3: latepoint4

A Benchmark for Audio Reasoning Capabilities of Multimodal Large Language Models (https://arxiv.org/html/2601.19673v1)
citeturn28186view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19673v1","lineno":110}); Total lines: 1681
L95: The preparation of the dataset is a multi-stage procedure. First, we formulate a set of rules for the tasks to be included in the dataset. We then survey a group of domain experts to recommend candidate tasks that align with these rules. Next, we eliminate any candidate tasks that cannot be reliably evaluated. Finally, we operationalize the proposed tasks by developing a set of templates that are instantiated with sound samples and synthesized speech in the last stage.
L96: The whole process is outlined in Figure cite73†1 .
L97: Figure 1: Task preparation process.
L98: ### 3.1 Task Selection
L99: As the performance of MLLMs in tasks that address specific audio problems such as speaker diarization or gender identification can already be tested with the use of targeted datasets and the benchmarks that aim to evaluate AudioLLMs incorporate task-specific datasets (cite57†Wang et al., 2025 ; cite60†Yang et al., 2024 , e.g.), we refrained from testing the qualities of MLLMs in isolation.
L100: Instead, we focused on tasks that combine different sound phenomena to assess the capability of MLLMs to reason over diverse input signals. Thus, to be included in the ART dataset, the task has to obey the following rule:
L101: > Rule 1: The task should not be solvable by an LLM that consumes the output of a single specialized module that approaches a specific task and ignores all other sound phenomena presented in the audio signal.
L102: 
L103: This rule excludes tasks that can be solved by an LLM acting on speech transcription. Furthermore, it eliminates tasks that can be solved using an audio captioning model followed by a question answering system, effectively excluding the majority of Chat tasks proposed by cite60†Yang et al. (2024) .
L104: To simplify error analysis for independent researchers who decide to use our benchmark, we also assumed that the proposed tasks should not rely on the superhuman performance of the model or the competence of highly skilled individuals, such as musicians or sound engineers. Thus, the second rule that the tasks have to obey is:
L105: 
L106: > Rule 2: The task should be approachable by a person without professional training.
L107: To gather tasks that obey the aforementioned rules, we surveyed a group of experienced speech and natural language processing engineers that included the authors of this paper. Initially, we collected 25 candidate tasks from 7 participants in total. In our effort to create a benchmark that produces results easily verifiable by an unskilled person, we decided to exclude from our candidate set all tasks that could lead to different outcomes due to individual variability.
L108: Thus, we rejected tasks that involved emotion classification or subjective assessment of sound quality. Furthermore, since we intended to provide an option to evaluate the model without depending on another LLM to serve as a judge, we eliminated tasks that cannot be framed as Yes/No questions. As a result, our benchmark is composed of nine tasks presented in Table cite74†1 .
L109: Table 1: Descriptions and examples of questions for each task included in the ART benchmark.
L110: Task name  | Description  | Example
L111: Audio Arithmetics  | Performing simple arithmetic reasoning with regard to the sounds heard.  | Are there as many bell rings as there are cat meows?
L112: Audio Transformation
L113: Detection  | Recognizing whether one recording is a transformed version of the other.  | Is the first recording a sped up version of the second recording?
L114: Cross-Recording
L115: Language Identification  | Comparison of the languages spoken in the recordings.  | Is Budapest the capital of the country this speaker comes from?
L116: Cross-Recording
L117: Speaker Identification  | Comparison of the speakers in the recordings.  | Is the same person heard speaking on both recordings?
L118: Selective Text Inference  | Inference based on some uttered content which is selected on the basis of the properties of some of the speakers.  | Is green the answer to the question asked by a man?
L119: Sound Reasoning  | Reasoning based on the recognized sound.  | Is the animal that makes the following sound bigger than a horse?
L120: Speech Features
L121: Comparison  | Comparison of two recordings regarding speech features present in them.  | Is the second recording the same text but read with a Scottish accent?
L122: Text and Sound
L123: Reasoning  | Questions that require both sound features and text understanding to be answered.  | Is the person talking about the following sound?
L124: Text and Temporal
L125: Localization Reasoning  | Questions that require both noises from localization (surroundings) and text understanding to be answered.  | Does the speaker describe the acoustic scene that they are in?
L126: ### 3.2 Task Templates
L127: We relied on the use of templates to generate the tasks. The rationale for adopting this approach was twofold. First, we wanted to control the size of the benchmark. Templates allowed us to easily increase the diversity of questions by expanding sets of possible slot values while maintaining the preferred size of the dataset. Second, as with any dataset released to the public, there is an ongoing risk of training data contamination for models that will be released in the future.
L128: Having a set of templates that can be populated with fresh sound samples from undisclosed sources will allow developers of future models to re-run the evaluation procedure while mitigating the risk of obtaining over-optimistic results due to data contamination. For each task, we developed a set of question templates containing empty slots filled with appropriate values. The values could be single words, whole sentences, or special tags, later to be replaced with sounds.
L129: During template creation, values were randomly chosen from previously prepared sets in a manner that allowed us to automatically generate a target answer to the question. An example of a template is shown in Figure cite75†2 .^{3}^{3} 3 Task templates are described in detail in Appendix cite31†B .
L130: cite76†Image: Refer to caption Figure 2: Example of a template. Both the sentence and the sound are chosen randomly from predefined lists; the target answer can be inferred from these values. Proper speakers for voice cloning for each part of the template are selected. Table 2: Summary statistics of the ART benchmark.
L131: Task  | # Samples  | # Templates  | # Speakers  | # Utterances  | # Sounds  | Total length
L132: AA  | 1000  | 6  | N/A  | N/A  | 5  | 3h 46m 10s
L133: ATD  | 1000  | 4  | N/A  | N/A  | 4  | 3h 53m 30s
L134: CRLI  | 1000  | 6  | 12  | 12  | N/A  | 3h 32m 1s
L135: CRSI  | 1000  | 4  | 4  | 8  | N/A  | 3h 46m 17s
L136: STI  | 1000  | 4  | 4  | 36  | N/A  | 3h 9m 47s
L137: SR  | 1000  | 15  | N/A  | N/A  | 20  | 3h 8m 15s
L138: SFC  | 1000  | 4  | 10  | 3  | N/A  | 2h 37m 7s
L139: TSR  | 1000  | 8  | 4  | 16  | 17  | 3h 25m 24s
L140: TTLR  | 1000  | 4  | 4  | 15  | 8  | 3h 47s
L141: Total  | 9000  | 55  | 22  | 86  | 25  | 30h 19m 18s
L142: ### 3.3 Task Instances
L143: 
L144: Based on this information, speech samples for voice-cloning were randomly chosen from previously prepared sets with required characteristics. This approach also helped to enhance the diversity of the dataset.
L145: 
L146: To generate instances of each task, we needed three types of audio recordings – questions, utterances and sounds.
L147: To unify audio prompts, we synthesized all questions using the same sample for voice cloning. As the goal was to generate intelligible speech, the choice was limited to these samples from the LJ Speech dataset (cite77†Ito and Johnson, 2017 ), for which the Whisper medium model (cite58†Radford et al., 2023 ) obtained WER of 0. The chosen samples were used to generate synthetic speech, which was again transcribed to find samples that yielded a WER of 0.
L148: The remaining samples were evaluated by human reviewers, and the most natural-sounding sample was selected as the prompt for question synthesis.
L149: Five of the tasks required additional utterances spoken by different speakers. The samples for voice cloning were selected from the GLOBE dataset (cite78†Wang et al., 2024 ). As with selecting the prompt for the questions, the samples were transcribed using the Whisper medium model, used as prompts for voice cloning, and transcribed again. Thus, after human evaluation, 10 samples (one per speaker) were selected to synthesize utterances.
L150: One of the tasks, Cross-Recording Language Identification, required utterances in languages other than English. For this purpose, we used the VoxPopuli dataset (cite70†Wang et al., 2021 ). We selected four languages – Estonian, Finnish, Hungarian and Polish. For each language, we identified speakers for which WER obtained with the Whisper medium model was equal to 0. We then narrowed our selection to recordings with a duration between 2 and 5 seconds.
L151: This process resulted in the selection of three speakers (one utterance each) for each language.
L152: The last type of audio recordings, sounds, included short sounds of e.g. an animal, tunes, and background noises. All sounds were manually selected from samples available under the Creative Commons 0 license in the Freesound dataset (cite79†Font et al., 2013 ), resulting in 13 short sounds, four short tunes, and eight background sounds. The short sounds were manually trimmed as necessary to include a single sound event per sample.
L153: For speech synthesis, we utilized a pipeline based on Voicebox (cite80†Le et al., 2023 ), a text-to-speech model that demonstrates zero-shot capabilities in reconstructing audio segments from textual inputs and speech prompts. The architecture adapts the transformer model (cite81†Vaswani et al., 2017 ), with modifications including the use of rotary positional embedding (cite82†Su et al., 2023 ) instead of ALiBi self-attention bias (cite83†Press et al., 2022 ).
--------------------------------------------------------------------------------
