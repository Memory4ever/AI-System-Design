# Identity-as-Presence17889：配对参照与身份/几何分责

resume_mar17，仅03-20补03-19自然日；原2+2+2=6、八Agent准入/date复用。不从Submitted单独证明日期、不重计修订家族。交resume_review17_18非准备者有限Source/actualowner/PRE；未自PASS、未授Books锁/POST/safe/DAY。

## 1. 实际必要Source与停止

[exact-v1](https://arxiv.org/html/2603.17889v1)必要§3.1–3.4/Eq1–6 L89–164、§4设置/T1–3与直接反侧L169–210、§5 L211–214实际已读。current官方abs单条完整AB/history实际轻量核：v4 Aug07，摘要明确共享跨模态binding/subject anchors，机制与评价实变，故只定点[exact-v4](https://arxiv.org/html/2603.17889v4)受影响Network/Eq3–6 L123–149、Training/评价/直接T1–4 L150–207、Implementation与Evaluation L307–351、绑定消融说明L354–370与Limitations L397–401。原HTML模板日期不移动本补日归属。偶然返回的数据处理L281–291仅读涉及配对/采样偏置处，prompt和定性图的caption不授全部像素检验/全部附件/版本史/代码或复现。支持与直接反侧足够即止。

## 2. 核心接口与实质修订分层

v1独立video/audio VAE patchify后，同主体reference加同learned identity embedding，再各tower concat noisy latents；具名caption将appearance和speech关联subject。分开reference/noisy QKV，mask仅禁reference query读取noisy key，并不保证reference hidden恒定或禁所有跨主体reference交互。数据处理的SyncNet、ArcFace/Eres2Net匹配是模型代理，caption又派生于ASR/模型，配对并非已证真实身份或授权。

v1 reference visual时刻Tvmax+(k−1)、audio起点Tamax+(k−1)L，单位不一致且RoPE周期性不能授严格几何对齐/正交/零串扰；不采用这条精确recipe。v4明确RoPE只几何、所有主体shared margin start，identity由shared embedding承载，并新增reference k不读other-slot reference l的mask；主体slot训练每轮随机置换、固定Kmax，text anchors与identity slots是不同接口。v4主分支LTX-2.3、v1 Ovi，训练步数和人口也变，不能倒写成v1已给全部隔离/评测或把两版数字拼一张表。拟采共同sharedIE/参照读取分责，受影响最新规则明确引用v4而不称本日新增独立家族。

## 3. 必要评价、负侧与费用

v1作者100triplets（70single/30multi）、720p5s、Ovi训练12k/8k/5k，150kh TTS/100k video/50k paired/10k multiview人口。audio WER非全胜；多view T3 voice similarity single .591<.597、multi .566<.572，Sync-D8.218差于8.149，不能授全单调保真或同迭代=全预算。first-frame QwenImage转换增加条件/费用，cascade真实transcript TTS与joint端到端不是完全相同任务。

v4改400 identity-disjoint双语triplets（200single/200multi），primary LTX10k/10k/15k＋multi-view；Ovi仍另12k/8k/5k，50steps、audio/video CFG4/3、batch64、lr1e−4披露，不把它迁成全部hardware/precision/并发/SLO。T2 LTX FM .85/SM .70，Ovi .70/.67，仍有明显失败，FM/SM不是1；T3/4新增绑定对照不能唯一证明sharedIE已解决所有身份失配。v4正文L202‘higher WER’与相邻oracle-TTS解释方向有含糊，不采该句定量归因。

v4 FM/SM只多主体200人口；face/voice分别经跟踪、VAD/diarization、ArcFace/WavLM和阈值matching。SM还要求voice唯一匹配、其他speaker重叠≤.3s与segment内highest-SyncNet activeface匹配同k；没有可靠activeface计失败。故边际AID/VID覆盖高可仍cross-bind；匹配/同步模型有共同误差，SM不构成独立身份真值或安全授权。聚合population/阈值/工具revision应保存，不把offscreen/unmeasurable失败偷删人口。

v4明确paired资料稀缺/clean-studio筛选偏置，rareaccent/crowdedmulti-party/atypicalcamera不足；shortrealhuman4–10s训练，minute/streaming未验，occlusion/noisyvoice/crosstalk仍speaker collapse。reference编码与token attention、跨modalfusion、所有curation/caption/训练阶段、50步/CFG和输出matching均付费；未给端到端总费/latency/SLO，不授production、安全或普遍无损。

## 4. actualsole owner与最小差额

sole `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际完整330–377（codec/时间身份→ControlFoley→DreamID→语言响应交接）、487–530（cross/shared attention），Ch22/24/25入口实际读。现DreamID段L367已给共享预留position segment/具名anchor与配对proposal边界，但没有learned共享identity区别geometry、reference query隔离责任及边际相似≠同主体speech assignment的具体消费验收；不是主题NC。拟该完整DreamID段后、语言响应与acoustic策略段前两段；不改原source binding/未来材料、不扩Ch24采样与真实身份/权限owner。

## 5. 待非准备者裁的两literal PRE与static

位置分段之外，也可让同一主体的外观与音色 reference tokens 加入同一个可学习 identity embedding，再与各自的 noisy latents 拼接；具名文字 anchor 另声明谁出现、谁说话。这是配对参照的表示接口，不是新的身份真值。[原始有限分支](https://arxiv.org/html/2603.17889v1)区分 reference 与 noisy-token 投影，并禁止 reference query 读取 noisy key；后续[受影响修订](https://arxiv.org/html/2603.17889v4)将位置只用于几何、所有主体共享参考时间起点，并进一步隔离不同主体的 reference 读取。两版规则不能混成同一精确 recipe；mask 控制可见依赖，也不保证 reference hidden 恒定、真实配对或输出零串扰。<!-- source-family:SF-2026-ARXIV-2603-17889 -->

多主体还应把“每张脸和每个音色都出现”与“这个人说了这句台词”分开验收：边际相似度高仍可交换声脸；受限修订用唯一 face/voice assignment、说话时间重叠与 active-face 同步匹配检查后者，但这些都是阈值和模型代理，不是独立身份 oracle。短片、干净参照与筛选人口下的改善没有消除遮挡、交叉说话或稀有口音失败，原评价也有质量反退；参照编码、额外 tokens、融合、配对数据、各阶段训练、生成与匹配全部计费。配对不明、参照污染、代理失准或质量/预算回归时，保留显式单主体配对、既有条件路径与独立内容/同步核验，不让联合生成获得真实身份或执行授权。<!-- source-family:SF-2026-ARXIV-2603-17889 -->

静态源注：

- `SF-2026-ARXIV-2603-17889` — [Identity-as-Presence v1](https://arxiv.org/html/2603.17889v1)必要§3–4/Eq1–6/T1–3及[受影响v4](https://arxiv.org/html/2603.17889v4)身份/几何、mask、绑定评价与直接Limitations。仅shared identity reference、读取分责和边际相似/配对验收；分清两版recipe/人口，保匹配代理、反退、clean-reference/短片失效与全费用。未采严格正交/零串扰、普遍绑定保真、真实身份/授权或生产SLO；未核代码、全部附件图像或复现。

## 6. 授权后一次窄写 / writer读回

2026-10-12 reader独核§43有限Source/PRE通过后root明确授resume_mar17唯一Ch23窄锁。重新加载Books适用背景/学习理念/写作指南、ROADMAP/当前路由与Ch22/24入口，按原两literal于DreamID完整后实写368/370及末本人静态注1770。writer实际完整350–385/末本人及MoBa/VEGA邻注读回，reference位置→shared identity/read mask→边际与绑定验收→Omni策略衔接正确；两literal与原包程序定点匹配均true。章numstat由90/0到96/0仅本family六新增行，diffcheck0，不改旧source binding/邻family。作者自回读不作POST/safe，交resume_review17_18一次nonwriter实际完整350–385及末注邻接，静态注不复制流程身份。
