# 第二批：准备好的五项必要证据/actual owner

原HTML与块定位为 `V3_CORE_2602.<id>.raw`、`V3_BLOCKS_2602.<id>.md`。当前不继承旧Books结果、不授rootPRE/日期完成。以下可独立随包复核。

## 22402 CMV，5分，标准完成 → 建议已有覆盖

§2/blocks14–23是immutableJSONLsnapshot/新UUIDbranch，实际tree，mergefuture，不授content-addressing或依赖闭包。§3/31、34–45：lastcompaction以前全部skip、base64删、toolresult大于500charstub、writeinput大于500stub、thinking删；所以preserveeveryuser/assistant是**postboundary conversation文字范围**，非全原始证据或推理完整。preboundarytool IDs用于清掉orphan APIresults。§4/47–76：cacheprefix改写首次miss；76单用户、chars/4估token、假h=.9、60turncap，无downstreamaccuracycontrolledtest；mixed12sessions平均10turn而conversational64sessions40turn，不授通用10轮。

Actual ownerCh77已读278–318的fact/policy分责、367–375 cache/fullraw对照、454–466 compactcontrol/exactevidencearchive。结构保留≠语义、cacheinvalidation/回读成本及rawfallback已经具体覆盖；孤儿schema属于接口实现细节不足以新增长期段，paper-name不是gap。建议NoChange，日报保原失败界。

## 22406 U-Mem，5分标准完成，拟采用差额

§3/27–69：冻结θ、memoryevolve；trainstream后freeze memorytest。失败cascadeL1teacher→L2code工具→L3Gemini模拟human，不授真实专家/正确性证书。Gaussianutilityμ/σ；newmemory用10邻居平均+spread+εexplore=.1；score=.9sim+.1sampleutility；radv=rewardmem−rewardbase，对**已用集合内每条**更新Gaussianposterior，不能证明单memorycausal/marginalgain精确。§4/81–100：Qwen7/14B,3H200，Hotpot/AIME与judge两个nonverifiable；Table3必要消融；k3优于k5/10，token相比MemRL更多，teacher/judge共同error及simulatedexpert预算保留。

OwnerCh77当前278–307已具体描述utility减base有sampling/interaction/scorernoise，不能重复归因段。新增窄差额是**greedy冷启动自我饿死→高不确定utility的有界探索与邻居prior**，权限/真值仍已有治理，探索增加badmemory exposure/额外base调用/teacher费用，test frozen不等持续在线。申请 `Books/part-07-agent/77-memory.md` fact/policystate小节现有差值归因段后仅一段+自身末注；跨日锁若忙继续其他项，不等。

## 22419 DeBias-CLIP，6分深入完成

§3与§4/42–65：**原完整longcaption仍训练**，去firstsummary只作用新shortcaption，subsample不保sentenceorder，prefixpadding移动PAD不截文字；独立captionsemanticunits是近似不适任意叙事。§5/83–92、Table5：LongCLIPsummaryshortcut、remove/permutation对照；paddingDOCCI80.8→79.7局部退步、SigLIP仍−6.1/6.5%位置敏感，short/long不同λopt。没新增trainableparams≠没训练/成本，不能以attn均匀证明全细节understanding。

OwnerCh23当前584起“对齐不是把向量拉近”、Caption辅助不是图像替代含监督/claim验收，但缺**summaryfirst可成为longcaption新捷径，caption位置人口与short/long目标需分验**。拟该Caption小节后一段窄补（保longloss、onlyshort去summary、sampling/positionbias反侧）；申请 `Books/part-03-multimodal-world-models/23-multimodal-representation.md` 此一段+自身末注，与首包LazyStrike并存同一窄lease，不造新owner。

## 22425 ArchAgent，5分标准完成 → 先找Existing

只采用generalagent/evaluation反证，不采用cachearchitecturewinning作为模型/infra贡献。§3.5/52：50/100M短simulationsearch→1Bvalidate可能ranking不泛化；§7.3/135–136具体Policy12：优化编译消去assert、writebypass在LLC不支持，模拟器丢write/DRAMpressure伪造IPC3/4%，trace模拟无correctcomputationhook；这是**evaluator高分能来自semanticinvalidexecutions**的新受控案例，不授模型有恶意或所有simulator不安全。未核全部cachepolicy实现。

Owner候选Ch66Evaluation或Ch72Security，须定位actual simulator/rewardhacking段后判断Existing；本packet不申请未读ownerlease，pending仅authoractualowner定点核，不是externalblock。

## 22434 GetBatch，6分深入完成

§2/21–66：client先sampling才batchrequest，singleDT按请求序列serialize（defaultTAR）分散sender并行；不能将order当shuffle/cursorrestore或globalbatchatomicpublication。coer默认falseerrorabort，true发missingplaceholders保持positionalcorrespondence；softfailure/recovery有硬cap，memorypressure429、CPU/diskbackpressure。DTorderedhead可能等待早item、load/admission不能省略。§3/71–97:16OCInodes+8clients/80workers，smallobjectrequestoverhead→大objecttransfer，15×不是全训练；§4/110–119同32A100setting，GetBatch P95 1808.6ms<random3668.7但>sequential431.2ms，sequentialshard读取牺牲randomsampling，不授全负载最优。

Actual ownerCh27 current912–935已有workerorder与batchpublication，是**消费顺序/可见**，不等跨storagebatchretrieval/softplaceholder。建议在从Shard可见到Batch原子发布之前加一段，requestorder与sampling仍client、placeholder由consumer显式处置、不宣称已经提供cursor/recoverybitwise；具体semanticgap6分深入而非15×高评分。申请 `Books/part-04-training-system/27-data.md` 该前置一段+自身末注。
