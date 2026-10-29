# Jun09 已见多模态/模型理论具名题摘（第6批）

仅恢复此前已完整读过current AB的16具名线索，不另宽发现。作者本轮已完整重读全部exact-v1题摘/history，原件`SUP_ABS_2606.<ID>v1_20261025.html`与精确DOI完整字段`SUP_EXACT_2606.<ID>_20261025.json`均存。身份/唯一v1与原字段均核，无withdrawal/具名erratum标记；后版本号本身不触发全史。日期只按合同联合公告界，不代全球first-public或逐字历史。

下列11项Submitted在Jun05截止之后/周末/Jun08截止前，最早公告Jun09 00Z，findable/arxiv.content同DOI registered为Jun09 03:26–03:59Z，整个区间BJTJun09。07687与4模型理论跨日另列，不能用registered搬日。准入/评分先交reader校准，不下载Methods构造队列。

## 具体增量清楚的拟入选

| ID | 原约束→实际新增→改变解释/选择；拟分 | 原字段 Submitted / registered UTC |
| --- | --- | --- |
| 09828 Latent Spatial Memory | RGB pointcloud memory反复render/VAE且丢latentfeature→depth lift latent tokens到3D persistentcache/direct warp→scene memory表示/读取与生成pipeline成本边界改；2+2+2=6，不借10.57×/55×数字自动准入 | Jun08 17:59:54 / Jun09 03:59:05 |
| 09803 Echo-Memory | worldmemory收益混backbone/training/检索→同interface/backbone/optimizer/sampler对容量/压缩/readout/recurrence矩阵，replay与return常异→不能用replay quality选persistentworld记忆；2+2+2=6 | Jun08 17:54:10 / Jun09 03:58:32 |
| 09507 Prisma-World | 独立多视角rollout可生成互斥世界→joint sequence/multiagent RoPE同步时间与相对camera几何bias耦合→单camera condition与跨视图共享scene资格分开；2+2+2=6，不因新增dataset或多agent名准入 | Jun08 13:59:50 / Jun09 03:52:05 |
| 08810 Decoder Interface | latentMSE/PPL掩盖decoderbasin/低熵collapse→decoder margin/local sensitivity bound+native/readout对照与保守marginexit→生成state fidelity与token realization/退出条件分开；2+2+2=6 | Jun07 20:00:33 / Jun09 03:36:42 |
| 08357 FReDA | 固定corruption与真实draft error失配→model-generated draft分布递归refinement而无手设forward、self/BoN两个parameterization→训练中间state分布与执行budget选择改；2+2+2=6，不按4B/15%/1.8×准入 | Jun06 22:10:46 / Jun09 03:26:49 |
| 09159 Uni-E | parallelDLM token dependency/invariance分离→Inv-E与Ind-E组合精确可算energy并给distribution shift修正条件→partition估计/并行候选target资格需重核；2+2+2=6，必要审阅要核假设而非仅算法名 | Jun08 07:50:12 / Jun09 03:44:19 |
| 09056 MilliVid | 长视频全细粒度history撑爆sequence→层次autoencoder粗到细rollout并按帧/阶段控制context detail→长程geometry/持久性与纹理预算不同；2+2+2=6，不借Minecraft分数或hybrid命名准入 | Jun08 05:46:01 / Jun09 03:42:05 |

## 只解决准入含糊点，不预Methods/owner

- 09827 MemoryVLA++：AB主要memorybank+imagination+diffusionaction组合，多个bench/robot本身不成贡献。只点核memory-guided imaginedlatents相对独立memory/WM组合是否新增可靠的状态交互机制/成立条件或有解释选择的controlled反证；不因VLA/大模块多而准入，也不因局部任务排除。SubmittedJun08 17:59:53/registeredJun09 03:59:04。
- 09150 Ultra Flash：AB的superresolution/casualupsampler/distill/self-forcing/cache多recipe。只点核causal latent upsampler与动态cache如何改变coarse/fine streaming依赖/延迟边界，是否只是把已有modules级联调参；30/18FPS不单独成贡献。SubmittedJun08 07:45:03/registeredJun09 03:44:07。后v2/3/4不按版本号扩全比。
- 08788 MaskAlign：random token-subset alignment+pre-mask mixing可只是masked regularization配方。只点核所谓stable spatial gradient preference及subset perturbation对照，是否真正修正‘全clean token对noisytoken对齐’的成立条件，还是仅依赖/attention测量的常见现象，不借成熟noise/target mismatch原则。SubmittedJun07 19:11:22/registeredJun09 03:36:11。
- 09646 Intuitive Physics：拟preN待代表校准。完整AB是不同预训family/layer/probe在IntPhys2/MVP排序和frame-shuffle退步；未给超新task probe排名的原机制/成立边界或足以修正具体设计判断的反证。不是因观测/小模型/物理域一律排除；若reader认为family/temporal对照有新的可长期选择证据，则只读决定点再判。SubmittedJun08 15:40:32/registeredJun09 03:55:06。v2不借为v1。

## 潜贡献清楚但日期尚跨日，先定点日期恢复

- 07687 Action-Relevant Video Latents：同inverse-dynamics probe跨encoder，重建强却action近零、temporal pretrain较latentprediction主增益与CALVIN静态shortcut是具体潜反证，拟6但未列确定当窗候选。v1SubmittedJun05 04:43:02Z最早Jun08 00Z，registeredJun09 03:12:04Z跨BJTJun08/09。
- 07713 MoA memory-optimal attention：algebraicDNF消中间数组/shape correctness与memory-minimal theorem有明确潜贡献，不能因没GPU实测排除；2–100×只是projection非实测。SubmittedJun05 14:44:49Z最早Jun08 00Z，registeredJun09 03:12:38Z跨日。
- 07604 Contribution Weights：attention×value幅度/方向投影与sink-output norm关系可改token importance解释，潜贡献清楚；SubmittedMay29 09:40:38Z最早Jun01 00Z，registeredJun09 03:10:08Z跨日。
- 07600 Gaussian Transformer reachability：mean-field/affineFFN Gaussian不变→mean/cov bilinear control、同rank有限时可达与时不变谱稳定/爆炸条件，明确主线理论潜贡献，不因Gaussian或无GPU排除。SubmittedMay29 07:51:03Z最早Jun01 00Z，registeredJun09 03:10:03Z跨日。
- 07527 Post-training is (Massive) Supervised Learning：虽positionpaper，但随机init与pretrained同现代posttrain人口的原比较可能改变pretrain/ID拟合解释，不因position标签直接排除；尚需决定比较是否确有长期原反证。SubmittedApr20 08:52:09Z最早Apr21 00Z，registeredJun09 03:08:27Z跨日。先只解决具体贡献/日期，不把旧日期metadata当Jun09。

以上是日期恢复前停点，后续定点替代与当前隔离边界见末节；未闭合前不先Methods/owner。raw DOI脚本返回cross_bjt_dates，不拿首/末某一天切片。新增16具名收束不代表483全项需关闭，也不扩本日之外报告。

## 一次独立校准后的当前结果

reader已完整独读16个exact-v1题摘/history与完整DOI字段，11合法Jun09/5cross复算通过。七明确增量皆准入6，不预授中心claim/Books；09646代表preN通过，不因physics/observational/small范围排除。

三gate与07527双方只点读决定域，已足则停，不先扩全Methods：

- 09827 §III-D/IV-F2/IV-G2：memory-aware query读partialSVDfuturelatents再sigmoidgate/concat是成熟融合recipe；Add41.2→44.4及freeze/step/horizon局部消融未给新的长期状态交互条件/反证，preN关闭不评分。不是单因无errorcontrol或实验小排除。
- 08788 §4/5.2/6.2：作者explicit featuredrop防coadaptation，21×gradient空间偏好与mask-vsfull gap降到13.8%没有建立新的clean/noisy时间条件；mix+mask互需和高mask反退是局部regularizationrecipe，preN关闭不评分，不因FID差小排除。
- 09150 §2.2/2.3.2：gate通过6。真增量是cascade上游输出与自身history双误差曝光，以及IQA触发复用末denoise x_t KV来替代clean x0 forward的cache-generation选择；非PixelShuffle/causalconv名称或30FPS。普通必要域要保IQA不认证KV语义、first4then3/SRwindow和训练全费。原HTML35s仅下载422209/664223bytes（09827亦459620/568333），这些完整目标section与后界均在；不称完整raw成功、无权读到未取得尾附件，可按必要点恢复而非重做已核gate。
- 07527 §3：同100BSFT的0/.1/fullpretrain暴露阶梯与ID/crossdomain归因对照通过贡献门，若日期闭合D2R1U2=5；pretrain仍优/SFT-only非RL/1.5B轻pretrain反退保留。尚未日期，不列当窗确定候选、不扩owner。

## 八个具名日期未决项的定点恢复进展（含补回的B2 SySR，不是raw全池扫描）

07665/07711与本批07687/07713/07604/07600/07527均有明确潜贡献与真实跨日界，未拿第三方Scirate Jun09日期硬闭合。已作ID/标题的有限官方/作者入口搜索；无其余候选扩池权限。arXiv按日`/list/cs.LG/2026-06-09?show=2000`及CV同路实际HTTP400，该路径错误不代表全部恢复不可得。进一步用标准年月`/list/cs.LG/2606?skip=0&show=2000`本轮HTTP404，原header/html为`SUP_DATE_MONTHLG_20261026.*`；不是官方空批次、未取得原dayheader，不声称已核公告。正式再取得按day header的相同ID或精确datedfirst-public后只恢复相关项。

07527特定早稿信号单独处理：[作者实验室](https://schwartz-lab-huji.github.io/publication/post-training_is_massive/)原HTML已存`SUP_DATE_07527_LAB_20261025.html`，JSONLD datePublished/dateModified=2026-06-09T00:00:00Z，正文只June2026；支持这条作者发布，不证明无更早正文。搜索恢复同题作者的[OpenReview PDF](https://openreview.net/pdf?id=i7P1VeDIY5)，但forum不可达、api2 notes?id实际403、api2/api1经web亦不可达，未取得pdate/readers历史；搜索‘5monthsago’不可当primarydate。当前不能以lab字段消除April submitted→June registered的first-public不确定；需要同note首次public字段/作者明确首公开声明或相容公告，未做额外Methods/owner。

07604恢复[PMLR正式页](https://proceedings.mlr.press/v306/cunningham26a.html)，精确同题作者/摘要且正式会议Jul06–11只是后续发表，不解首次公开Jun09界；不因正式Jul日把arxiv搬日。07600 [FAU CRIS](https://cris.fau.de/publications/364345838/)同题作者身份确认，仅2026/year+Submitted，[lab project](https://dcn.nat.fau.eu/codefel-wp1/)当前Oct15update也非first-public；不读其完整PDF证明日期。07713目前只发现Jul08讲座等后事件，不是论文首公开字段；07687/07665/07711未找到可闭合的精确作者dated原件。上述可用替代未提供必要原日证，下一仍须由独核确认安全隔离范围；不把它们计新Books/正面Coverage，不借邻日结果。

B2遗漏同步的第八项[07726 SySRs](https://arxiv.org/abs/2606.07726v1)经reader发现补回，不改原潜贡献5分校准：经典bestarm逐模型评价→同步pairedcomparison利用query响应相似性→同评价预算下选bestmodel的统计条件改变。原AB/history与`SUP_EXACT_2606.07726_20261025.json`有效复用，唯一v1Jun05T17:03:19Z、findable/arxiv.content registeredJun09T03:12:55Z，最早Jun08T00Z到最晚跨BJTJun08/09；不列确定当窗候选、不Methods/owner。Comments为ICML2026形成具名venue信号，定点[PMLR lyu26h](https://proceedings.mlr.press/v306/lyu26h.html)同题/作者/摘要只给Jul06–11后正式发表，原HTML已存；[作者Publications](https://flodorner.github.io/Publications/)同题链接arxiv，仅ICML2026无日（`SUP_DATE_07726_AUTHOR_20261026.html`）。另定点OpenReview官方[作者profile](https://openreview.net/profile?id=~Florian_E._Dorner1)搜索可见同题、作者、Published30Apr2026/ReadersEveryone的早稿信号；直接open重定向challenge，随后精确content.title的api2/notes请求也实际HTTP403 ChallengeRequiredError（`SUP_DATE_07726_OPENREVIEW_NOTE_20261026.headers/json`），未取得精确noteid/pdate及对应历史正文，不能用索引读数认证历史逐字版本或把它强搬Jun09。需原note首次public与PDF身份/dated作者明确首公开、或同ID官方公告界后，只恢复该家族；当前与其余七项一起精确隔离，不抹早稿信号、不以June登记覆盖April线索，也不为这一个缺项重跑全部8/旧52。
