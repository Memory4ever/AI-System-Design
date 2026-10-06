# 2601.09088v1 — sentence likelihood is a sampling heuristic, prefix continuation is a separate interface


## 非作者局部终裁

root actual exact-v1必要方法/对照/反侧与Ch29 mixed occupancy/text continuation终裁通过，5分标准OnlyReport；不是泛Existing。
[Exact-v1](https://arxiv.org/html/2601.09088v1), PRIMARY_09088_NECESSARY.md §4–5/Table3–5,6.4/7.3/7.5–6. Proposed2+1+2=5 standard, pending root final OnlyReport. Teacher-SFT positive targets/student-prefix mismatch→teacher/student sentenceprob sample selection plusstudent-prefix teachercontinuation→reconsider sampling and occupancy interface, not likelihood as causal source label.

Sentence geometric mean token probabilities pT/pS/pD classify “teacher/student/shared/boosted”; highteacher/lowstudent is a heuristic beforetraining, not proof sentence originates exclusively teacher. Figure6 correct/incorrect correlation across sentencepositions is not causal learning-quality/gradient witness. DAS compares equal-count25k/50k RS attemperature .6/1 withgptoss120b/QwenNext80Bteachers andQwen3-4Bstudent, locally favorable Table3/4; equalnumber does not matchedlength/selectionteacher-scoring/tokencompute budget or general efficacy.

Mixed-policy starts studentresponses capped1.5×teacherlength, selects truncated failures, randomly cuts studentprefix and asks teachercontinue. Table5 uses7.7k1epoch plus20k offpolicy mixture; maskedteacher-only suffix harms AIME, unmaskedsmallgain not prove alwaystrainerroneousstudentprefix. Fullrecipe §6.4.2 takes50kqueries→15ktruncated→12.7k passingfilters, differentpopulation than Table5 not interchangeable. §6.4.1 low/hightempstages6epochs global64 seq64k cosine5e-5→1e-5 ZeRO3/Liger. Table7 stages increaseexposure/computation andGPQAhigh-temp67.7→67.6counter, notorthogonal causaldemonstration orminimaloverhead.

Evaluation §7.3 temp1/topP1,64responses perquestion (not64independent trainingseeds),AIME30questions each,GPQA198,maxlength102400math/81920codeGPQA. Hardware/precision/trainingrepseeds/CI andcomplete selection+generation+trainingbudget Not Disclosed in necessarycore. Public artifacts notrun; no exactdistillation/provenance guarantee orheadlinecapabilityranking adopted.

Actual Ch29 L382–388 allowsstudentprefix teacheraction handoff, L416–420 explicitteachertextsuffix CE withcondition/lossmask, L648 tail-selection andL1096–1098 selector bias/fullresponse fallback cover matureinterfaces. This paper adds finite sentenceheuristic/selection+maskingresults, not reliable causal sentenceorigin oruniversal lossmask reversal; OnlyReport is supported localnew evidence, not泛Existing/forcedweakrecipeBooks. Root minimumraw/ownerdecision pending.
