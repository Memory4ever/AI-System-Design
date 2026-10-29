# Training-free MTP17942：必要接口/受影响v2定点与PRE

03-20仅补03-19自然日，resume_mar17准备；fresh合同/ROADMAP/本日context已重载。SF-2026-ARXIV-2603-17942，公开03/19与2+2+2=6准入经本日独核§2通过；必要Source/PRE尚待非准备者，未写Books/POST，不授DAY。

## 必要Source实际范围

[exact-v1](https://arxiv.org/html/2603.17942v1)§2–4.4、必要A（Lemma证明）、E/F/G.3。当前官方abs v2说明实际指出更新experiment tok/s→AR speedup，改善§3.1 initialization/§4 ablations，并非只有history。遂仅定点核[exact-v2](https://arxiv.org/html/2603.17942v2)§3.1–3.3、§4.1–4.4及受影响A不等式；不全版本diff/代码/其余附录。采用v1有限接口，不能混v1 A100绝对速度与v2H100相对速度，不重复family分数。

- v1§3.1/v2§3.1：冻结AR模型不增加可学习head/weights，直接以prompt embedding均值初始化mask embedding，生成时按m←m+λ(e_new−m)、λ=.1更新。不同slot同embedding但position与ancestor context不同；不是训练的特殊mask token，更不是真未来状态。v2把均值主路径明确化，hard/sampled对照移到§4.4；均值有限Llama消融更好，不授所有模型/领域最优。v1“Last K”索引歧义不作为采纳配方。
- v1§3.3–3.5：mask logits Top-K提出future节点；custom tree mask/position，顺序验证接受真实目标的prefix；累计概率的tree扩展/相邻同token用nextcandidate替换只改变proposal，不授语义重复必无用或全局optimal。§3.3 Eq6将root/draft/mask都算入BC，§4又简称draft nodes，Alg1 B-node表述不齐；不采exactbudget recipe，实际应明算全部处理token与KV。
- Lossless只在同条件target verifier接受/拒绝/回滚contract成立；本文sample-matching和T=1 acceptance表并非分布审计，不从“exact match”标签授任意随机sampling全分布correctness或有限精度轨迹等价。这里不改Ch48已有exact acceptance权限，mask/probe仍只提出候选。
- v1§3.2 F2只100Dolly creative-writing，accepted/rejected cosine是后见关联。A L376从norm≤c_h推出norm-product δ≥c_h²δ，方向错误；v2 A L403同错误仍在。仅取h_m=.5h_v、norm(h_v)=c_h、cos=1，即原称distance≤0不成立。本书不采其cosine threshold定理/guarantee或普遍latent MTP因果，有限接口无需此理论证明。不要以此把整篇中心隔离/降分来减少工作。
- v1§4：Llama3.2-3B/3.1-8B Instruct，Qwen3-8B/32B，SpecBench，max100生成，单A100；T0主评价/T1 G.3；precision/batch完整time harness/并发/每prompt长度/重复不确定性Not Disclosed。PLD depth10、STAND cumulative tree、LADE L/W/G30=(4,5,5)与60=(5,8,7)；同名BC不等完全同硬件compute。
- v2§4.1明确S/R walltime H100，而setup仍A100；setup max100生成与T1 caption256输出也不一致，保硬件与输出长度口径冲突，不移其speedup为v1数字。T4 Llama3.2-3B naive在BC30/60为.99/.95–.96×AR、efficient1.08–1.22×；因此tree construction/mask/PID工作能吞掉接受长度收益。不採宣传“全architecture/edge”外推，也不以作者“fewer calls→energy”代替能耗测量。
- v1/v2§4.1 task反側STAND在复制丰富retrieval/RAG/summarization/coding等部分任务胜，边界随版本评价不同，保有限而不合并一个统一排行。v2T2 BC60 3Bdynamic1.630略低static1.631，不授strict最佳；T3三mask退于一/二，更多slot不等更多净收益。
- v1§4.3/Appendix E：仅静态tree可重用mask/PID、随accepted长度添加prefix columns并shift positions；动态树mask合成与框架集成仍future。Mean/EMA、额外token forward、tree候选排序/剪枝、mask/PID/KV、回滚及真实全请求time/搜索费用均要算。不默认部署/代码/复现已验收。

## actual唯一owner差额

actual Ch48 `INFER-SPECULATIVE-DECODING`完整L492–641顺读：551–562已有training-free latent/embedding probe→exacttargetverification和费用；607–626为需要训练的samebackbone masked proposal/standalone质量取舍。现有通用latent分支不承载“不训练mask而以promptmean+生成EMA初始化/更新的slot，共用embedding但不同position/ancestor，并计mask本身token预算”的具体接口及static树重用条件，故不以主题相似假NC。

Ch47开头1–110实际拥有logical/physicalKV分页；Ch49开头1–65实际拥有typed execution plan与backend。不新node。拟Ch48原L562 latentprobe末段后、SpecForge lifecycle前插两短段，保已有验证合同和原段绑定。未授Books锁。

## 逐字PRE

Training-free 的 embedding probe 还可以不训练特殊 token：先用当前 prompt 的 embedding 均值填充额外 mask slots，随后随已生成 token 更新这份向量；各 slot 共享值，却以不同 position 与祖先 context 提出未来 token 候选。Tree expansion 和重复 token 裁枝只管理 proposal，target verifier 仍决定同一已接受 prefix 的输出与 KV commit；不能把 mask 表征或候选置信度当作未来真值。预算也要包含 root、draft 与 mask 的全部处理位置，而不是只报树节点数。<!-- source-family:SF-2026-ARXIV-2603-17942 -->

[有限原证](https://arxiv.org/html/2603.17942v1)与[受影响修订](https://arxiv.org/html/2603.17942v2)支持这条候选来源，但不授 cosine 相似度的普遍保证、随机采样分布审计或全部模型加速。Mask/PID 复用依赖静态树；额外 forward、候选选择、KV 与回滚仍计费，naive 实现可比普通 AR 更慢，复制丰富的任务也可由 lexical baseline 胜出。更多 mask 不一定改善收益，版本间硬件与计时口径不能混合。Prompt 统计失配、验证语义未落实或完整费用不值得时，保留普通 target decoding、lexical proposal、独立 drafter 或已训练 MTP，而不因“training-free”静默覆盖它们。

静态本人注：`SF-2026-ARXIV-2603-17942` — Daily2026-03-20补03-19；[v1](https://arxiv.org/html/2603.17942v1)§2–4.4/A/E/F/G.3与[v2](https://arxiv.org/html/2603.17942v2)受影响§3.1/§4/A。仅promptmean/生成EMA的maskproposal及staticmask/PID预算边界，不采错误norm inequality所授cosine定理、全stochastic exactness或通用speedup；版本间A100/H100计时分开，复制任务/naive反退/全fee保留，未核代码或复现。

支持/直接反侧足够即停；待非preparer必要Source/actualowner/PRE，不预支安全处置。若以后需精确BC/随机exactness/速度保证，只请求处理token预算和真实prefix verifier/RNG/rollback trace、修正定理及同硬件全费用，而非再扩所有附件。

实际落实：reader必要Source/actualowner/两PRE有限PASS已持久本日独核§5；root授Ch48本family窄锁，作者按原两PRE写564/566并读回完整548–588/本人1266与邻注，scoped diffcheck0；reader一次实际548–588/1257–1270本人1266 POST正式PASS，root接纳释放。仅此有限采用安全整合，不改静态Book注过程身份，不授DAY。
