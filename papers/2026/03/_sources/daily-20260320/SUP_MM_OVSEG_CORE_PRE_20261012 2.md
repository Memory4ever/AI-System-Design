# MM-OVSeg17528：本20必要Source与两PRE

resume20_author_new sole准备，仅03-20补03-19；原5/准入day复用，不自授Source/PRE、Books锁或DAY。

## 1. 必要源与停止位置

[exact-v1](https://arxiv.org/html/2603.17528v1)必要§3.1–3.2/CMU/DEF公式、§4.1–4.4/T1–4、A配置/B成本/C seen-unseen及E直接CLIP-SAR反侧已读，v2 current同五作者/Mar27/CVPR2026，无具体纠错说明，不全版本diff。A/E精确section原URL恢复，未核全部figures、D大backbone、F可视化、代码或复现。只读取采用命题支持/直接反侧。

## 2. 接口与必要反側

先以co-registered RGB/SAR多层features的InfoNCE训练SAR-DINO、RGB-DINO冻结；再冻结两dense encoders，训练CLIP image/text与卷积fusion/readout。dense RGB+SAR按层投影相加，global CLIP只读RGB；二者分别与文本category相似，再卷积/拼接/residual与FPN式decoder到pixel分类。并非SAR独立获得完整text语义，也不是freeze原CLIP。§4称adaptive scenequality weighting，但显式式子没独立quality gate，故不补造可靠度consumer；conv非校准概率。

E/A5 DINO-only73.1、bothCLIP+DINOSAR66.5，多分支反退只局部对照，不授global结构普遍invariant或唯一冗余因果。C/A3各自协议的seen/unseen仍有落差；原notes误将③ OEM-thick Seen的MM37.4与④ OEM-thin Seen的EBSeg37.6跨列比较，此比较撤销，不称MM在A3同列低于baseline。cloud都是synthetic协议（含GIMP/不同camera,resampling），crossdomain不支持真实所有weather或任意开放类别。T3/4无全部预算匹配，A各baseline B4/8/16与LR不同，不采完整因果增益。

main A10080GB（原文RTX A100命名不补改）、120k/B8/ViT-B16，CMU25087pairs与feature制备另费。B/A2整模型参数331M非A表31M trainable，116.9ms慢于GSNet83.2ms，CO2是估算；完整CMU/监督训练、相机配准、两dense/CLIP/FPN推理与回归均付费。precision、latency计时batch/并发/SLO、CI未齐，不授freezing即无费用或更快。

## 3. actual唯一owner与两最小PRE

sole `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：actual473–520完整层表示训练→fusion taxonomy与730–748 taskcontribution/reliability分责、开篇及相邻Ch24/26复用。现文尚无“只对新sensor dense分支配对蒸馏，再冻结双dense、由RGB-only globaltext分支消费融合dense”的选择性对齐接口；不是全模态都应训练成CLIP。拟Fusion主标题后/early-fusion标题前两段作为融合责任的入口，不另开SAR应用章或写Ch27第二owner。

### 正文PRE 1

融合以前还要决定哪些表征需要迁移、哪些消费者继续保留原输入。一条受限分支先以已配准模态对，让新传感器的dense encoder学习冻结RGB encoder的多层features；随后冻结两dense路径，按层投影融合，再与只读RGB的全局图文分支共同交给空间读出。训练时全局图文encoder仍可更新，冻结dense不等原模型整体保持；局部跨模态相似也不认证新传感器已经拥有完整文字语义。配对来源、层、更新/冻结阶段与最终consumer须分别绑定。<!-- source-family:SF-2026-ARXIV-2603-17528 -->

[有限异质传感器对照](https://arxiv.org/html/2603.17528v1)中，同时迁移dense与全局分支反而弱于只迁移dense，seen/unseen类别仍有差距且整法推理更慢。它支持选择性对齐这一分支，不证明全局语义永远可靠或显式融合权重已校准；合成退化也不能替真实故障验收。配准数据、蒸馏、监督训练、多encoder读出和回归全付费，特征域、文本类别或净收益失配时，保留独立encoder、原图文路径与真实标签验证，不把更多对齐模块当作无损统一表示。

### 静态来源注PRE

- [MM-OVSeg2603.17528 exact-v1](https://arxiv.org/html/2603.17528v1)：必要§3/CMU/DEF、§4/T1–4、A配置/B费用/C seen-unseen/E CLIP-SAR对照。仅选择性dense配对迁移、双dense冻结与RGB-only globaltext消费分责；保both分支反退、CLIP可更新、合成天气/类别与预算失配、整法更慢及全费用。不采global普遍invariant、独立quality gate、所有seen/unseen无损、真实weather或SLO保证；currentv2无具体纠错，未核全figures/代码或复现。<!-- source-family:SF-2026-ARXIV-2603-17528 -->

待非preparer必要Source/actualowner/原两literal裁，未写Books。

## 4. resume20_reader_new非准备者必要Source/actualowner/PRE裁

本人实际exact-v1 §3.1–3.2/CMU/DEF（84–129）、§4/T1–4/设置与关键比较（130–199）、A/T A1（261–272）、B/T A2（273–283）、C/T A3（284–297）及E/T A5（314–340）读；current同五作者v2/Mar27/CVPR2026，无具体纠错说明，不全diff、全部图形/大backbone或代码复现。InfoNCE配对训练SAR dense而冻结RGB dense，再冻结双dense/训练CLIP图文与融合读出，global仅RGB与category text；stage/consumer分责成立，cosine/sigmoid不授语义/校准真值，不补quality gate。

发现notes A3跨列MM③ Seen37.4 vs EBSeg④ Seen37.6误比，作者已撤销，只保各自seen/unseen落差；实际回读改句，原两literal/static未改。不将此误比作反侧或扩大重核；E/A5 both66.5<dense-only73.1与B全法116.9ms>GS83.2ms仍是直接必要反侧。合成cloud/不同camera与resampling、CMU25087配对制备、120k/不同baseline训练预算、CLIP可更新、trainable31M vs全模型331M、估算CO2/未齐计时包络和全费保持。

实际Ch23完整470–526表示层composition→Fusion/early/late/cross/shared各接口与730–752 task贡献/reliability分责读；开篇/Ch24/26有效交接复用。已有融合位置、层组合和质量sensor不拥有“选择性dense迁移→双dense冻结→RGB-only globaltext消费”的具体接口，soleCh23差额成立；拟Fusion标题后/Early前两段，未新增SAR应用或第二owner。**必要Source/actualowner/原两literal/static有限PASS**，原5/day保持，root唯一Ch23锁后才可写；仍需一次实际非writerPOST，不预I/DAY。

## 5. root窄锁下writer落实

2026-10-12 root授本family soleCh23锁，resume20_author_new按§3原两literal/static写485/487与本人末注1850，正文仅Fusion标题后/Early前。写后实际473–504完整邻接及1840–1850本人/邻注顺读，两literal/static各唯一一次；表示composition→选择性对齐→融合位置分类衔接保留。notes跨列错误已撤销，不进入正文；无quality gate/全部无损等强桥。限定diffcheck0，不stage/commit/push。尚待reader一次非writer actualPOST与root接纳释放，不自计I/DAY。

## 6. resume20_reader_new一次非writer实际POST

复用§4有效Source/actualowner/PRE，不重核原源；实际完整473–504表示层composition→Fusion标题/新485/487→Early/Late完整段及1840–1850本人/全部局部邻注顺读。原两literal/static机械逐字唯一各1，485/487/1850；限定diff本family六新增与此前VirPro/SegFly/STTS分账，cached/unstaged check0。选择性迁移/冻结与CLIP仍更新、消费者保持RGB输入、合成退化/类别、A5更多分支反退/整法更慢及全费用近文保持；跨列错比未入正文，旧taxonomy完整。**一次有限actualPOST PASS**，交root接纳释放Ch23，不自计I/DAY或改静态身份。
