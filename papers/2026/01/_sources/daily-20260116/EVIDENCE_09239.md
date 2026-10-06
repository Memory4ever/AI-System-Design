# 2601.09239v1 — semantic/acoustic streams require cross-source validation

Exact [v1](https://arxiv.org/html/2601.09239v1), PRIMARY_09239_NECESSARY.md §3–5/Table1–3/limits/C1–3. Proposed2+2+2=6: codecselfreconstruction/rigidtokenlength→frozenASRsemantic stream + learnedacousticstream and50%contextinpainting + asymmetricfusion→consider independently sourcedcontent/style ratherthansameutterancereconstructionasdisentanglementproof.

HuBERTFSQ1024/25HztrainedCTC thenfrozen; acousticSEANetFSQ learned throughST mel-flowandWavLMspeaker alignment. Fullreconstruction versusrandomtimeprefixacoustics/fullsemanticmaskedmelreconstruction with50%mode mix; decodersemanticCNNadd+acousticcrossattention, allowsdifferenttokenlengths. Bothupsampletodesiredmel; notprovedstrictnolinguisticstyleleak oruniversalvariablelengthspeech. Speakerloss1,CFG2/conditionaldrop. Semantic tonephonemecontent notspeakerfreecert.

4khrASRChineseEnglish,100khrEmiliaforacoustic;430M/Ascend15days,400kstepsAdamW7.5e-5warmup32k,dynamic30kframes/batch. Exactdevicecount/precision/seedsCI/latencySLO ND;22DiTiterativeflow costlybylimits. SeedTTSspeechEnglishChineseonlynotgeneralall-audio. Qwen0.6vocabaugSFT5epochLR1e-5warmup.1,350kLibriTTS960triplets targetF5TTSgeneratednothumanGT4000randomtestcleanpairs;noisolatedtokenfactorvsalltraining/synthteacherbudgetcause.

Table1 reconstructionDSA50HzUTMOS3.38< Wav3.92/SAC3.88,WER2.49>SAC2.03,SIM.76<SAC.83; recombinationclearlocal advantagebutnonmatchedmodelrate/codebook/objectivesbudgets. Table3 w/oSpeaker improvesrecombWER4.95<5.93/UTMOS3.73>3.67 whileSIMfalls.36<.60, so speakerloss tradeoffnotallessentialwins. Withoutrecomb WER107.68 directobjectivecounter supportsrecombbranch; noassertuniqueasymmetricinjectioncause absentmatchedablation.

Probe CNN2/BiLSTM256/128embed,30epochsselectedvalWER/SC,CtcLibriSpeech/SCVox1251sameidentitiestrain/test. SemanticWER6.28/speakerACC2.35 vschance~.08% andfiniteprobe inabilitydoesnotcertindependence. Needclarify‘minimal’notno leak; reconstructionfidelitynotgenerativeusequality, voicecloningWER23.95 vsSAC24.21 smallwithoutCI.

CurrentCh23 L238–247 semanticVQ/acousticcontinuoussidechannel andtonecontract don'tcover independentdiscrete dualstreams/reconstruction-vs-crosssourcerecombmode;Ch24onlydecoderfusionhandoff. Potential unique MULTIMODAL-REPRESENTATION two paragraphs aftersemantic/acoustic分责: separatetokenprovenance/timeidentity andcrosssourceeval,flowdecoderconsumeinterface notduplicategenerativeowner;cost/noleakboundary/conventionaljointcodec fallback. Rootnecessarysource/ownerdecisionpending, nowrite.
# 当前终态收据

root实际必要primary/Ch23具体gap写前通过，实际L243/245、speech/tone邻接及1081源注非作者POST通过，锁释放。6分gap深入完成/实际整合；正文边界不变，日级未授。
