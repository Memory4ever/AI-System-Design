# CCL18600：训练过的跨模态空参照与 guidance 分支

resume_mar18 sole准备；仅03-21补BJT03-20自然日，复用原65完整题摘独校，不新query/全附件/别日。准备不等独立Source/PRE或actualPOST，不自授Books写入/safe/DAY。

## 身份、日级字段与具体准入

[exact-v1官方abs](https://arxiv.org/abs/2603.18600v1)完整题摘/currentheader/history实际打开，仅v1，所见页无明确withdraw/correction/先公开venue信号。真实[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.18600)state findable、created03-20T02:16:28Z、registered02:16:29Z、v1 Updated00:42:31Z、Available仅2026-03，Submitted03-19T08:17:05Z不等公开。沿本批日级夹证限定本窗arXiv事件，不冒精确公告或别处从未公开。

原双流去掉跨模态条件或手工静音/静画面参照可能与训练接口不齐→在跨attention中学习固定context tokens、按任务改变可见KV，并用训练过的tokens构成采样负分支→重新选择空参照的制备/消费与文本、跨模态控制的求值预算。原ADMISSION独校已具体准入，不因音视频应用名或能映射Ch24而留。拟2+2+2=6，仅这个训练—采样跨模态条件接口；成熟RoPE/多任务/CFG及“最高质量”不单独给分。

## 最低充分原证与反侧

实际[exact-v1 HTML](https://arxiv.org/html/2603.18600v1)§3.1–3.3/Eq1–2、§4.1–4.4/Eq3–7、§5必要解释、§6.1–6.3/Tables1–2与§7。支持与直接反側足够即停，无须追所有引用、展示视频、代码或版本史。

- 基于Wan2.1-14B视频主干，音频同block层数但更窄channel，Mel/audioVAE与videoVAE输入不同。TARP按t_v/t_a缩放audio RoPE并做局部窗口；floor(t_a/t_v)分区、边界插值细节不采精确通用对齐recipe，不给两流原生物理同步证书。
- LCT每CCA模块固定可训练tokens，KV投影后可与另一模态latent的KV拼接，LCT不加RoPE。DCR单模态任务只读LCT，joint两支读LCT+另一latent且同步noise时刻；条件生成将reference stream时刻置0，只让其读LCT并detach reference梯度，生成支可读其cleanlatent。不是推理动态检索或当前输入的已知真值，也不证明全部background/foreground已因果分离。
- Eq5每个velocity估计的两次model求值是(负text,LCT)与(正text,实际跨模态latent)差分；Eq6三次求值另分出(正text,LCT)和(负text,实际跨模态latent)两个方向。两式不是同一联合conditional field的纯计算等价：Eq6文本/跨模态系数同为1时仍不自动等于Eq5的联合正条件求值，条件interaction项未由式子认证。原文“steps”不能当整条轨迹只有2/3个denoising step。LCT省的是额外生成静音/静画面参照，不取消双/三支或全部采样/decoder费用，不证明unconditional marginal精确。
- §3.1切gate导致piecewise参数目标/普遍梯度不稳定只是解释，任务外部g选择本身不证明固定任务loss必不光滑；§5图只jointloss、EMA且从iteration100起。关注背景注意力也不是语义因果，不采用“所有gate损收敛”。Table2的LCT/DCR捆绑消融不单独定位各者因果。
- Joint资料4M OpenHumanVid+in-house，audio另外Wavcaps/VGGSound pretrain160k步/batch3200；joint12k步/batch320、352×640，消融6k/batch128。训练tokens数audio8/video128，任务概率.1/.15/.15/.6。不同原pretrain/data/预算不构成等资源优胜；hardware/precision/全pipeline生成时间、并发、SLO未披露。无需为当前机制补实现，未核代码/复现。
- 自建200 test、无训练重叠是作者声明；easy肖像/静止与hard全身运动共享audio，未披露每subset数/seed重复/CI，人类评价无报告。模型各自prompt重写且MOVA不用multimodal CFG，不是匹配同控制协议。AudioBox CU/PQ、Whisper WER、SyncNet与ImageBind/Synchformer代理不同，不由某个同步指标认证所有声画语义。
- Table1 CCL CU/PQ低于MOVA，easy Sync-C/Sync-D不全胜Ovi，hard DeSync1.19差于Ovi1.18。Table2 baseline WER4.52%→TARP4.67→+LCT/DCR4.81→+UCG4.63，full仍差baseline；加SyncCFG WER5.59且同步/IB反退。因而既不采“每模块全维稳定改善”，也不由fewerdata宣称总资源更低。负参照、生成语义、语音与同步分开验收，保原双流/gate/普通CFG作为退路。

## Actual sole owner / 最小差额

sole `MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际完整282–306的NFE、共享noise、多stem、capacity guidance、部分退化负条件、history/reference分支已读；294–296保留部分已有text context，但未承载跨模态任务中训练固定LCT再作负参照/双三求值合同。338–340双noisyproducer/readout亦不等此空参照。Ch23/25交接复用本日已实际读取且未变；TARP纯表示时间不另写Ch23。拟294–296完整后、298历史EMA前一段，仅该条件参照消费者差额，不重写既有两支或多任务基础。

## 一段 literal PRE（待非准备者）

跨模态条件的负参照还可以在训练中学习，而不是推理时临时清空另一模态或生成一份静音、静画面。一条受限双流分支在每个跨 attention 模块加入固定可训练的 context tokens：单模态训练只让该模块读这些 tokens，联合任务再拼入另一模态的 latent，条件生成则保留干净 reference 支并截断其梯度。采样时将负文本与这组训练过的 tokens 作为参照；一种两次求值的路径同时改变文本与实际跨模态条件，另一种三次求值的路径分别形成文本与跨模态差分，不能把两者当同一联合条件更新的免费等价实现。这给空参照增加了训练支持，不证明它是真实 unconditional 分布、背景语义原点或纯内容分离。[有限音视频消融](https://arxiv.org/html/2603.18600v1)中，同步改善仍伴语音 WER 反退，LCT 与 routing 的捆绑对照也不单独认证各模块因果；不同模型、prompt、CFG 与预训练预算的比较不授总成本或全质量优势。训练与tokens驻留、局部对齐、双/三支逐步求值、codec和独立语音/同步评估均付费，省去手工参照的额外生成不等取消 guidance。条件人口、任务路由或声画质量失配时，保留原双流/gate、已校准普通CFG和独立条件生成，按语音、同步与完整预算分别验收，不让learned null自签无损或实时保证。<!-- source-family:SF-2026-ARXIV-2603-18600 -->

静态注：

- `SF-2026-ARXIV-2603-18600` — [CCL exact-v1](https://arxiv.org/html/2603.18600v1)必要§3–4/Eqs1–7、§5解释与§6.1–6.3/Tables1–2；仅task-routed learned context tokens作为跨模态负参照与双/三model求值分账。保joint/reference noise与detach、条件interaction非等价、gate不光滑/attention因果未证、WER/音质/同步反退、prompt/CFG/数据预算混杂与全费；不采精确TARPrecipe、unconditional law、纯语义分离、全胜/零费或实时，未核代码/复现。

准备交root非preparer必要Source/date/actualowner/PRE；当前无锁未写、不计safe/DAY。

## 非准备者必要 Source / actual owner / PRE

root 实际核 exact-v1 §3.3–4.4/Eqs2–7与§6.1–6.3/Tables1–2；当前身份及本批公开日期复用有效独立题摘/日级字段。LCT 固定可训练、按任务改变跨 attention 的 KV、clean reference 与 detach 以及两/三求值均有原文依据。Eq6 的加性分解未含联合交互项，不把它与 Eq5 当纯计算等价；对照的 WER、音质及同步反退与非匹配预算近文保留。只采用训练过的跨模态负参照，不授 gating 必然不光滑、纯背景语义、unconditional 精确分布或总费优势。actual Ch24 282–302完整负分支/历史 EMA 交接及本日有效相邻章已核：原部分文本参照与 capacity/历史分支不拥有此 learned cross-modal null 差额。原one literal/static和6分有限 **PASS**，授 resume_mar18 sole Ch24在部分文本负参照完整段后、历史 EMA前窄写；写后root一次实际POST，不预授I/DAY。

## 非写入者实际 POST

root 实际顺读写后 Ch24 292–307 和本人末注，one literal/static与批准稿一致。capacity/部分文本参照的成立条件、历史 EMA 的状态与费用均保留，新 learned 跨模态负参照位于二者之间；参考支 detach、双/三求值非等价、WER/同步取舍及原路径回退近文成立，不让低参照生成费变成总费或分布保证。actual POST **PASS**，root接纳为实际整合并释放Ch24，本日最终来源/分母/DAY尚未通过。
