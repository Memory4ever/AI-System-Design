# AB8后五项：必要证据与实际owner，PRE待审

本包仅22765/22766/22779/22787/22805，未写Books、未计safe。原获取V3_FETCH_AB8_NECESSARY.json，exact-v1 HTML优先，只读拟采用方法、对照与关键反侧。原abs实际Submitted UTC02/26 08:55:58/08:56:23/09:15:34/09:21:12/09:42:20。公告政策公开下界02/27 09:00+08；same-ID registered UTC02/27 02:54:07/02:54:08/02:54:26/02:54:38/02:55:06，秒精度各+1秒为BJT上界10:54:08/10:54:09/10:54:27/10:54:39/10:55:07。22805原库存日期空，已**定点**恢复DataCite同DOI，见V3_DATACITE_2602.22805.raw与V3_FETCH_AB8_DATE_ONE.json（2026-10-05T19:55:42Z），Submitted与abs一致；不把Updated01:35:47Z代首公开。五个区间完全落窗，不授Submitted=public或索引=primary技术。

当前官方评论22765/787/22805无，766ICML poster、779CVPR；无采用相关撤回信号，只是轻量status，不默认revision diff。22779 official abs题名“enables better”与HTML“Enhances”用同ID绑定，不把题名轻微差异当额外事件或全部材料失效。

## 22765 Second-order Rollout — 2+2+2=6，TRAIN-GRPO拟一段

实际22–85及必要70/91/93，未读AppendixC全证明，不采用其unbiased theorem。第一层同问题n responses，再为选中的question-response采n critiques；若全对或全错丢弃该问题，否则各取一个正确/错误存cache控制n² critique膨胀与标签偏斜。Responses reward1/0，critique只根据最终binary verdict给.7/0，**混在同一GRPO组**；这是组人口和relative credit接口的改变，不认证critique中间推理。数学题有reference/rule-based verifier，不是无oracle self-critique。

Qwen2.5-1.5/3/7B及有限7/8B其他家族，16K DAPO-MATH RL、1K seed coldstart，GPT-5 distill1885→1339过滤critique先SFT。512training batch、128mini、n5、4096prompt/response、lr1e-6/clip.2/10epochs；HW/dtype/训练seeds/完整采样与teacher账Not Disclosed。Same data不是same total FLOPs；作者85明确更慢收敛，以更多compute换质量，不称free lunch。主表generation GC与G-RL平均59.3 vs56.7（7B），Minerva24.6持平；critique evaluation只保有一对一错且boxed格式样本、1:1最终判断，所以不是自然错误率人口上的诊断accuracy。

决定性73/74反侧：同样dynamic responses在joint GC-RL优于static，但critique-only C-RL反而出现故意产错答再判wrong的捷径，static显著更好；不能把online data一律视为更好监督。Filter优于random/reweight的受限控制支持标签人口条件而非每种RL通用最优。Sampling denoise把critique-conditioned revised answer成功率加到outcome reward，实验n=1仅noisy效用proxy，不证明中间critique正确；额外correction rollout与solver competence混杂须计。原weighted reward的class expectations与数据选择同identity，未核全理论，不借其授无偏或任意prior校准。

实际Ch33 2413–2423已有critic信用绑定solver后续结果、两角色优势分开、自我迎合及frozen auditor选择，但缺**同policy second-order cache/混组的population控制，以及dynamic更适合joint而在critique-only反成可操纵label人口**。拟critic/solver链一段，明确balanced最终verdict不替step truth、same data不等budget；错误率人口/规则oracle不足就保static external critique、fixed labels或只做generation RL。请求窄lease+自身note，不复制全GC-RL配方或理论。

## 22766 Latent Visual Imagination — 3+1+3=7，WORLDVIEW-LLM-INTELLIGENCE拟具体Existing

实际23–61/62–82/92/94，必要负面接口深入而非标题判无用。三方法latent位置相似是相关统计，不把跨输入cosine直接签因果。实际Monet每位置/每instance共享固定tensor后V*83.3 vs82.7、HR4K70.1 vs71.1；原table Δ+.5与raw+.6算术不同，采用raw有限变化不采精确Δ保证。Mirage多种noise替换stage2仍近77，但tiny-state干预35.5并引发重复，不能说所有干预都无影响。干预的是后续反馈latent，不声明原input/早期KV已删除，因而只诊断所测接口的消费依赖，而非全部隐藏推理无用。

Derived probe只有30multiple-choice、同image不同属性，latent-only差于text guessing而image76.67%；弱probe不能证明所有信息不可读。替代CapImagine用Qwen3-VL4B看auxiliary图改caption/全trace，再过滤125K→17K，Qwen2.5VL7B/8A800-80G/bs1 accumulation16/best checkpoint。同filtered数据以<ThinkImage>代caption的控制支持显式中间信息作用，unfiltered控制125K与17K数量不同不签全部过滤唯一因果。训练teacher知道辅助图、部署没有真实辅助图，caption也是派生证据而非oracle。

Text trace干预76–79由Qwen3-32B故意改成错误结论后重放，V*85.9→22.5、HR4K74.1→24.0表示输出依赖被编辑文本，不认证正常文本的grounding真值，也不是与hidden tensor interventions完全同强度的causal effect比较。Only decode-time比较不是end-to-end cost，82速度近Monet与94更长AR latency负侧同时保留；HW/dtype/batch/tailSLO未绑该speed测试。工具DeepEyes仍有更高V*，language表示颗粒度有限，future latent还可能更好。

实际Ch8 301–315已经分latent convergence、外部验证、生成与实际消费，并具体提醒末embedding干预保早latent/KV，只能诊断接口、不能说全部latent无用，保显式CoT/工具与预算fallback。这条实际论证已承载本项拟采用的**latent相似/answer正确不证过程，需具体干预界面和绕路责任**。拟Existing；不为另一VLM例子重复同知识链，也不删除候选/降分。若root认为caption消费的独立接口确有新增差额，再仅该接口判断，不写“latent paradigm failed”普遍结论。

## 22779 TrajTok — 2+2+2=6，MULTIMODAL-REPRESENTATION拟一段

实际20–51/68–80/87–100/104–108/119；不读全部训练附件。成熟外部seg/track先固定object再喂encoder可复用，却不跟随下游representation objective。此处learned queries soft masks提proposal，再hard argmax mask限制第二Perceiver各trajectory读自己region；feature到segmenter入口stop-gradient减少coadaptation，而soft weighted proposal仍允许下游到segmenter的梯度。所说end-to-end并非所有梯度路径都开。Fixed128queries，丢empty masks，长视频仍分16framechunks；token数会随chunk数量增，不把“independent duration”宣传授无限整段fixed-token。

单trajectory可emit1/2/4slots，random granularity训练/推理选budget，Fourier offset init避免slots重复；它不是自然物体identity、grounded真实跟踪或任意slot都新增信息。受控1M视频×10epochs/4GPU消融：无feature detach retrieval22.1→18.3；无hard mask22.1→17.4；4slots random init21.9低于default23.2、2→4Perceiver部分退步。更高pixel resolution VEQ/STQ更好而retrieval22.1→22.0，支持segment fidelity不等consumer utility，非像素精度普遍无用。

Pretraining仍依赖DirectSAM/SAM2/IOU启发式pseudo labels，过滤coverage≥80%/objects≥10→约2.5Mimages+2Mvideos，偏object-rich人口；不是去除全部外部tracker成本。Main描述ConvNextTiny与appendixadapter预训Small/DINOv3分支分开不混，20epochs/8A100预训计费；scaledpanoptic backbone/decoder实验104–108不是主tokenizer的便宜性能。

TrajVLM Qwen3-4B+SigLIP2Huge，全参数caption1epoch+QA10Ksteps、8A10080GB/bf16/seq8192/globalB32；128frames/16frameclip vs patchpool3只能32frames是时间覆盖混杂，另pool9可128frames/token roughlymatched控制仍支持选择，但不授等全部预训练成本。Short-video若干任务反退。80消融硬mask/slotinit在CLIP encoder设置，不直接当VLM单组件归因；未核production timing/尾SLO、tracking真实性。Grouping encoder/pretrain/LLM token与sampling成本分账，过短/对象漏检或全局identity丢失保dense/patchpool/原frames回读。

实际Ch23 742–795有codec/quantization压缩消费责任、clip memory与主动读取，但没有**soft grouping提案+hard region refinement、局部feature detach与slot diversity的co-trained trajectory connector，并以downstream utility而非mask精度验收**。拟长视频表示链固定窗口前单段，不接管Ch75/运行时KV；original frame/time/chunk/mask/encoder identity仍可回指，不让trajectory名称自签object identity。请求Ch23该单段及ownnote窄lease。

### 22779 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks20–51、68–100、104–119：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+2+2=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：codec/逐片段记忆已有，但没有soft分组→hard-mask第二级读取、slot粒度及伪轨迹身份分界，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。前级stop-gradient、DirectSAM/SAM2/IOU伪标签、片段增长和32/128帧pooling覆盖混杂近文；保原patch/pooling回退。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 22787 Knowledge Attribution — 2+1+3=6，AGENT-RAG拟一段

2026-10-06 fresh后续复核（`feb28_ch76_ch36_finish`，非原包作者）：原v1 blocks30–58/67–76/89–100/118–124直接核knowledge proxy、title-disjoint split与answer-stringdecoy；no-context未答不证参数无知识、probe预测不循环当source truth。2+1+3=6，窄Evidence通过；actualCh76已有干预/supportauthority但缺构题代理/model-specific probe责任，窄I已写859、完整邻接849–875、末注1279。root 非写入者已实际核正文、完整邻接与自身末注，POST通过；无causalprovenance/自动repair/复现。

实际21–104及118–124。Attributed source与answer correctness原已分开，这里新增model-specific hidden-state probe的**self-supervised knowledge-testing人口与label代理边界**。20K Wikis、spaCy实体+similarity>.6排同义/title，GPT4o-mini改prompt；三种无context prompt任一成功即known，否则unknown。Known移除mentions、unknown保entity并删另entity；**三次未答不证明参数从未存有信息，present entity也不证明实际只用context**，因此“unique source forced”只作操作label、不授causal source oracle。

Greedy first-generated-token FTG与entity末token LTE两位置；model-specific 7/8B probe、title-disjoint64/16/20split，layer weights/linear head vslastlayer、MLP。LTE可用答案identity且需已定位entity，不能等同提前online verdict；FTG较早但仍经过一次generation forward。Wiki held-out macroF1与OOD SQuAD/WebQ accuracy不同口径，后者两单source/提示人口有结构线索；token/model revision改变要重训与重新构题，不覆盖随意自然长答/多语。

BoW/embedding仍.65–.68F1，proxy有lexical bias不是无偏标签。Answer-string decoy Table10是Llama单模型accuracy，linear.724、MLP.541，原作者明确随机paragraph未显式验证semanticirrelevance；这一控制反驳简单surface捷径足以解释全部，但仍不认证truecausal source。Dual source预测context87.1%与irrelevant预测parametric92%由同probe做判断，不能循环当外部真值；source alignment与errors的Fisher关联不是改变source导致该error的随机因果。

正确source仍错、confidence高仍错，保provenance/support spans与externaltruth独立验收。Max100epochs/earlystop patience3/B64 AdamW，hiddenstates存储/extra probe training和model-version重做增加费用，mainHW/dtype/latency/SLO Not Disclosed；没有实际RAG自动repair闭环。Layer weights不等机制causal localization，capability升级会改变known/unknown人口。

实际Ch76 833–853明确counterfactual support sensitivity与ordinarycorrectness、citation consistency≠support；缺**知识测试代理产生model-specific训练label、hidden-source probe只能提出diagnostic而不签grounded truth，复杂MLP更易decoy shortcut**。拟该hallucination/source分责链短段，明操作label及可核反侧，错误/升级/预算不足保配对evidence干预与独立claim verification。请求Ch76单段+ownnote，不复制分类器榜单到模型章节。

## 22805 VeloANN — 2+2+2=6，AGENT-RAG拟一段

2026-10-06 fresh后续复核（`feb28_ch76_ch36_finish`，非原包作者）：原v1 blocks46–59/66–74/80/83/90–95/103/105/110–118直接核record/page错配、metricaffinity、buffer/layout匹配条件与Async均值变慢反侧。2+2+2=6，窄Evidence通过；不采Alg2 visited-set配方终止/B倍hit保证，不据此认实际代码bug。actualSSD链缺recordvsmetric共址/并发QPS与单query分账，窄I写229–231、完整邻接217–245、末注1280，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；无生产安全/在线更新/复现。

实际40–84/88–118，遗漏71–80已单独补足。传统page cache省管理成本、async跨query隐藏I/O合理；新增具体错配是**vertex access skew被page aggregate抹平，record缓存又会重读同page，需metric-affinity co-placement/选择性共同装入配合consumer search顺序**。Sift有47.3%vertices未访问却0.1%pages未访问，page LRU/FIFO/random近似不能说所有缓存策略无效；node/page统计只该workload。

O(1)record映射/slot state与CAS、slotted compressed page，vector1bit resident+4bit extended、邻接PEF，thread/core coroutine+io_uring；不由Rust/原子字样签全memory/concurrency安全。Metric nearby不等graph-adjacent，reuseconstruction candidate识affinity≤τ，页剩余不足仍可splitgroup，非保证allaffine永远同页。Co-tag读入affine其余丢弃，τ较大可污染，co-placement建索引/quantization/metadata/states付费。Batch经验ceil(αI/T)是heuristic非deadline保证。

直接冲突局部隔离：83称hit rate放大B倍，没有独立/相关结构或概率界，不采用；80 Alg2 line19写E.insert(v.neighbors)而84正文说标记v visited，前者可使初始v永不进入E、P\\E持续含v重复探索，**不采用该所写termination/正确性执行配方**，未查code不能断言实际实现如此；只保独立实验与layout/cache条件，不整项D。重开需visited-v一致伪码/对应实现与终止test。93各系统in-memoryRabitQ与同graph参数、O_DIRECT/disabledSQ_POLL，但baseline8KB vsVelo4KB、buffers是各自disk size的20%不是相同absolute RAM，总quant/storage/layout费用不完全单因素。

48core Xeon8457C/384GB/two3.84TB Solidigm SSD/Ubuntu24.04 kernel6.8；作者dataset/table的dimension/raw-size有不一致，不混成统一尺度数，只采用具名Sift/Gist/Wiki/Image/Text受控结果。95 recall@10/meanlatency/QPS非P99SLO。113–118 progressive Text10%buffer里Async QPS+但meanlatency更坏，record/CBS再改变；不是async必降低singlequerycriticalpath。103 highdim B>2 QPS饱和latency继续增；105 beam W1甚至差于W0、W4最佳此population，再大wastedprefetch；111 τ5%较单record更好、10%退。109 memory30%相对disk有.78inmemoryQPS但2.19×latency，不写inmemory-equivalent latency。未核production index churn/fault/concurrency安全/真实RAG answerquality或code。

实际Ch76 209–237已有SSD filter、graph/vector分开读、压缩/refine与更新stall，但缺**record-vs-page skew错配及metric而非graph-affinity co-placement，并把coroutine QPS与singlequerylatency/质量预算拆开**。拟SSD存储链一段，与graph/vector分离是不同branch，不能新方案默盖旧布局。分布/affinity不稳、较小resident工作集、过大batch/beam或quality/SLO退就保page/directsearch/原参数；不采错误hit-rate或visited pseudocode保证。请求Ch76单段+ownnote。

本包拟四I、一具体Existing，全部PRE待审，safe仍35。Books/日级均未授完成；普通PRE未回不冒充外部材料终态。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22765：原必要blocks22–58/73–74/85与actual owner独核；Ch33正文2443/完整2433–2451/own2964 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
