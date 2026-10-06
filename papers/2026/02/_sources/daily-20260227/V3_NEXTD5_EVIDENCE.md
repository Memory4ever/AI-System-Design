# 后续5必要原证＋实际owner

2026-10-06最终独立日期复核修正：21941 Submitted=`2026-02-24T02:53:58Z`早于前一公告截止，Registered=`2026-02-26T03:09:56Z`只证明上界，缺少同IDv1首次公开下界。本项转日期保留项，撤除本日报对应Ch66单段正文与自身末注；以下必要机制/实验审阅保留，但其原PRE/POST结论不再授权本日正面采用。仅在取得同版本公告或实际可得时间证明后重开日期归属，不要求全文重读。

精确v1完整题摘已root独立准入校准；这里坐标是`V3_BLOCKS_2602.<ID>.md`的block，非文件行。只核拟claim与直接反侧，不授代码/复现/生产能力。21824 Ch27、21887 Ch33、21900 Ch23、21941 Ch66均必要原源/PRE及实际正文、完整邻接、自身末注非作者POST通过，四项整合；21854 Ch66具体已有覆盖通过。全部窄lease已释放；本包五项终态，不授日级完成。

## 21824 DocDjinn: Controllable Synthetic Document Generation with VLMs and Handwriting Diffusion — 2+1+2=5

[v1](https://arxiv.org/html/2602.21824v1)必要27–35/39–48/53–66/69–82。LayoutLM/CLIP/text zscore拼接、UMAP/HDBSCAN/kNN指定source clusters；不是自动最优：原31明确“manually select the optimal clustering”，heuristic只辅助。簇概率p(c)∝n_c^α；cross-cluster每个seed独立抽簇，intra-cluster一次选簇后全部seeds同簇，**改变联合seed关系不只是边际权重**。Claude4.5同时HTML与taskGT，OCR/DOM检查标签/区域/答案文本匹配只是proxy，不认证注释语义完整；diffusion字词重绘换visualdomain，有单独生成/渲染/OCR失败费用。

实际Table2[66]同synthetic-only目标模型五seeds：α1 intra平均59.72/LFID13.69 vs cross56.91/14.54；但DocVQA intra α.75 64.27>.1 63.64，PubLayNet α.75 63.41>α1 62.90，不采每任务α1最优/多样性普遍坏。原[75]DocGenie有10seeds本作6seeds+优化prompt，不能跨论文收益归因单一seed机制。Table3[67]直接负面已读相关rows：full LayoutLMv3 DocVQA-HW real59.41 vs real+synth58.36；FUNSD88.56→87.74；pure synth CORD58.84vsreal95.92，DocLayNet-DLA Faster6.60vs50.03。BERT HW48.24→51.19说明语义可读≠视觉分布可替。全real4000cap（DocVQA例外）、100少样本分母/3randomseeds vs seed策略5seeds分开，不能混合平均87%当真替代/成本减87%。生成14万文档/9优选writer有筛选偏置；精度/完整totalfee未披露，oracle人工聚类选择不在线自动。

实际TRAIN-DATA Ch27 105–130讲边际mixture即optimizationweight，337–341同题strategy覆盖/不同approach tree及同样保留条数不等总费；351–353讲generator需求/格式vs效用/真合成mixture。本项最窄差额是**同样簇边际与种子预算，seed联合coherence vs跨簇diversity不同**，以及相同语义内容的合成visualdomain可害visualstudent而textstudent益。拟PRE Ch27 synthetic段337附近一段：jointseedbinding、有限受控验证、类imbalance/handwriting失真与真实回退近文；若现argument已足承载请Existing，不以HTML框架新名加段。

## 21854 FewMMBench: A Benchmark for Multimodal Few-Shot Learning — 2+1+2=5

[v1](https://arxiv.org/html/2602.21854v1)实际38–46/49–70/101/105–106/138–140/213–220。query每task250来自GraphCutCLIPjointembedding，剩余pool取8近邻；对同query 0/4/8shot、random/similar/CoT比，26模型0.5–9B六家族。CoT由Qwen2.5VL7B先作答，错则注入gold重生成，subsethuman核；不是独立原生人写完全准确trace。MCQ2–4候选regex +optionperplexity两读出，后者仍不是消除一切positionbias的证书。T4/A40、部分FP16+4/8bit按家族不同，tokens/batch/maxoutput/SLO与完整重复不全。

决定原文64：“demonstrations … marginal improvements … variance … slight performance drops”；66retrieval vsrandom “no clear advantage”；68 8vs4不稳定；70CoT全测模型泛化宣传须收窄：附213还说coreference “stable gains … benefits substantially”，不授权所有task无fewshotgain；215直接错误样例有图像虚构、无CoT、malformed、超限loop、推理对而final错。[55]承认regex “occasionally misinterpret … unexpected responses”。因此表象CoT退步混合reasoning/format/truncation/teachertrace和answerreadout，不能全归因视觉reasoning无益。有限原曲线/附反侧够，未重构graph numeric或复现实验。

拟Existing PLATFORM-EVALUATION-SYSTEM Ch66 actual456–460：permutation/direct-CoT/trajectory-length/truncation分别冻结，正确率/positionbias分账，CoT不普遍更好、更多提示不能盖interface；1673–1675demonstration pool状态/oracle/ICLprefill额外预算分账。该benchmark是samequestion 0/4/8示例输入有限反例，不能以“新增26模型九任务”制造结构gap；标准完成有限诊断，不用深度语义因果。若root认为还缺**示例选择与posttraining状态交叉条件**只能补一个真实窄差额，不读全部task附录。

## 21887 ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection — 2+2+2=6

[v1](https://arxiv.org/html/2602.21887v1)实际24–40/42–50/53–68/73–85/109–114。language tag是model自己选择的先行动，不是rollout外指定mode；reward除答案verification还有format/compliance与阶段性languagecount。探索1/4步r_d=k_min/k（只已选language的有限batch，不创造未选支持）；利用3/4步**同language子组有任一correct就给同组其它responses r_p=1**，与individualcorrectness r_v不同，错response也有languagebonus。原39 “For each correct response, all other responses … same thinking language … rewarded”。不把languagePassk当每条truth/校准，Eq37称allr∈{0,1}与ratio记法不一只不照抄完整离散reward规范，不因此抹去finitecurriculum对照。

Controlledsamequery Englishteacher、sameLoRA+RLrecipe；LoRA82vscontrolled106steps因长度、总RL200±3/r8/batch256/output4096；8H200 teacher5hvsEnglish8h、4A6000SFT1.5h、8H200RL20h，sameRLsteps不是一切sameFLOP。Table2[50]MATHfinal91.5vsCtrl91.0；AIME31.9vs26.4、Passk53.3vs43.3；coldstart72.0<base78.1。Table6[79]sameRLsteps去explore AIME31.9→28.9/forced27.3→23.9有限控制；Table7[82]naiveexploit MATH91.7>ours91.5，Olym forced16.4>14.7，特殊passkbonus非dominant。Table3/4 forcedaccuracy只compliant子集和incompliant-as-error两个分母分别报道，unseen只4language，非language-independenttruth。原91winrates训练2000×5不证明所有latentpaths causally转English；entropy只traceproxy。

TRAIN-GRPO Ch33 actual479–481已有改变condition与固定P_sample(mode)的混合qualitytoken合同；本项差额**tag由policy选择且grouping随language action改变，子组成功奖励与逐responseverification不是同truth**。拟PRE在481后一段：conditiondecision includedpolicy/denominators、2stage有限source支持、错响应bonus与稀有language/zero支持处理、不授无偏/通用探索更好，teacher/langdetector/additionaltokens/quality回归fee与English/固定modefallback近文。

## 21900 EmoOmni: Bridging Emotional Understanding and Expression in Omni-Modal LLMs — 2+2+2=6

[v1](https://arxiv.org/html/2602.21900v1)实际39–63/65–69/78–85。Thinker从AV派生perception→intent→strategy→text，SLM把strategy变显式acousticinstruction，Talker输入instruction+text+speechToken；不让hiddeninterface默认保全部prosodyintent。Eq2条件Markovchain vs49text称看全部nodes不照搬成实现唯一规范；“causal”“mutualinformation”NLL理论未证明，采用有限可检查显式handoff而非人类心理真值。

Table2[78]samebase/conditional消融ECoT VT-RC1.81 vsnoECoT1.36（80文字1.84另口径，不默默混）；去ASR1.69、去emotion1.62、去stage1 1.68；去strategy声学无法生成，证明接口移除断链，不隔离strategy胜过matchedhiddeninterface的唯一因果。Table3[84]sameThinker与指令，Talker替VoiceSculptor VS1.67/1.75vs1.64/1.71；LlasaWER4.45<full4.72且UTMOS2.73>2.69，非全voicequality最优。VT/VS/IF不同proxy，原73承认IF被semantictext干扰。private500h dialogue与3000hTTS、encoder冻结/16A800 mixedprecision/stage1full+stage2LoRAr8，原66TalkerLR写1e5疑漏负号不照抄spec；不因此否认有限tables。生成/SLM/TTS/judge与pipelinefee无完整披露，无真人意图或empathycert。

MULTIMODAL-REPRESENTATION Ch23 actual125–135明确symbolicphonetic接口不保timbre/prosody，260–266timbre与time控制责任分账；缺的是**semanticresponse与acousticstyle分离时，策略显式handoff不能只交finaltext/默认hidden**。拟PRE Ch23 260后单窄段，在不同声学条件职责内串起perceptionderivedstate→strategy/instruction→Talker、保非truth/非physicalcausal/接口缺失与cap预算/cost及nativehidden单路径fallback；生成范式不复制Ch24。若已有具体handoff论点请Existing。

## 21941 MERRY: Semantically Decoupled Evaluation of Multimodal Emotional and Role Consistencies of Role-Playing Agents — 2+2+2=6

[v1](https://arxiv.org/html/2602.21941v1)actual35–59/71–83/95–102。先Pydantic/失败LLMformatrepair，再对**文本描述**的facial/body/speech等语义各自5judges×2次，票≥.7纳入emotion，否则ambiguous排EC；不是直接生成音视频感知/物理truth。拆emotionfidelity、modalityconsistency、judgeentropy、roleprofile/previnfo；rolejudge寻找支持与反对证据再映射1–5而不是直接主观评分，双expertavg。Unknown两flag无证据drop（TableIV57），不能当1分/完成人口。

TableX[98]100随机sample同human instructions+mapping，双judge bidirectional α Exp.745/Cha.619/Rel.721 vs双judge explanation .558/.386/.482；singleGPT .631/.552/.619，有限切片control。Human3与emotion5票分账，sameprotocolhumanlabel不独立验证心理truth。TableIXdescription100**unchanged/先LLM判correct**survivor4.348/4.323/4.719与alpha .585/.539/.571，不能估全数据真实性。TableXIemotionagreement .696/.656/.709/.721。MMRole/MERRY不同roles85vs125等数据支持，不把TableVIII synthetic比real差全归因source；vision-only模型换audio为speechprompt又有modality混杂。

TRAIN/Evalruntime1A800LoRA16为数据配方比较，不是judgecost；5×2+repair/双RCjudge＋100human额外费用要计。重复votes同模型不独立，threshold排样本会改变分母；semanticdecoupling不等模态渲染效用。实际Ch66 4333–4342已有population/scale/missing/abstain/pooling/metric及judge无truthauthority；尚无**支持/反对证据→ordinalmapping**作为可审计rubric中间态，拟PRE现judge段一个窄局部：先保双向evidence与dropped人口再映score、人评仅matched有限效度、描述只semantic非实际modalquality、票与费用/原subjectivehumanfallback；若具体已有则Existing。
