# DynaEdit17989：编辑方向选择与跨步噪声身份

评分纠正：归并时作者回对冻结Report原行确为2+2+2=6；root准备笔记和静态注误抄5，现仅机械恢复为6，正式候选从未改分/迁日。下方独核中的“原5”是同一误抄过程标签，由本纠正覆盖；原两正文、必要证据、采用资格与实际POST未改变，不重新研究。

## root写入停点（待非writer POST）

reader已有限Source/actualCh24/原两PRE及static PASS。root soleCh24写原两literal于PixelRush后、TFTF前，本人注章末；实际291–305及末三顺读/check0。插入后原TFTF的“与上段补空间细节不同”明确回指“与前面的空间refinement和编辑方向选择不同”，仅修handoff，不改TFTF机制/限制。交reader一次完整局部邻接／本人注和两PRE逐字核验，不自授POST/I/DAY；该锁释放后才授03-25 Theory22248。

root sole准备；本20补03-19自然日，已准入2+2+2=6、日期保持，未自授PRE或Books。

## 必要Source

[exact-v1](https://arxiv.org/html/2603.17989v1)实际§3/Eq1–3/Alg1、§4、§5/Eq4–7/Alg2、§6.1–6.2/6.6、§7与0.H。current同v1，无撤回/具体纠错信号。不核全部影片、prompt图像或代码复现。

源video与两个条件flow的velocity差分产生noise-free编辑状态。纯噪声端起步扩大结构变化但弱化source约束；单步等权多seed可模糊，无相关跨步噪声可jitter，全程固定噪声又限制结构对齐。SGA按候选方向外推终点与source的cosine/softmax聚合，ANC由独立逐渐转相关噪声。这里只采用选择与噪声协议分工，不补Eq6的bar符号差或Alg2混用a_i/a_t为完整实现recipe，cosine也不是真实物理。

Wan2.1-14B480p I2V、初三步5方向以后1，四CFG/温度配置；71人工选择tuples，49–81帧/832×480/16fps，部分firstframe需额外图像编辑。Gemini3Pro三维judge及32人2400+回答不是运动真值；人评按edit挑四配置之一不同于自动评四配置。0.H有不合理互动、保留域损坏与超参依赖。硬件/precision/完整NFE成本/并发/tail SLO未披露；两支/多seed、首帧编辑、VAE/judge与选择都付费，不采物理正确、任意模型无损/实时或全部编辑成功。

## actual owner与拟差额

sole `MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际开篇、Flow路径/生成预算及282–300像素refinement、球面边界、PixelRush浅反演→TFTF随机转移与权重完整邻接已读。已有浅反演/patch重建和跨stem共享初始化不承载inversion-free视频编辑“方向选择＋跨步相关噪声”的双约束。Ch23区域表征/三alignment交接有效层复用，Ch25开篇生成/transition分责实际读：只编辑生成状态，不授WorldModel action因果。拟PixelRush完整段后、TFTF前两段。

## 正文PRE

需要修改视频动作而保留场景时，反演后再生成是可解释的基线；另一条分支直接维护由源视频到目标视频的编辑状态，每步用源条件与目标条件flow的速度差更新。允许从纯噪声端开始可扩大结构变化，却削弱与源视频的对齐；等权平均更多方向也可能模糊。一种受限改进先把各方向外推为候选终点，按其与源视频的相似度softmax聚合，再逐步增加相邻采样步的噪声相关性：前者选择保留结构的方向，后者减少持续改向，不是固定一个seed就解决全部时空一致性。<!-- source-family:SF-2026-ARXIV-2603-17989 -->

[视频编辑的有限对照](https://arxiv.org/html/2603.17989v1#S5)仍依赖底座能力、首帧条件、guidance与温度；相似度只是保留代理，过强对齐会妨碍大动作修改。首帧额外编辑、多方向与两条件求值、相关噪声状态、VAE和配置选择全部付费；人评按编辑挑配置也不能与固定配置当同一协议。错误互动与未编辑区域受损仍会发生，因而分别验目标动作、源内容保留、画质与净成本，不由视觉偏好认证物理转移或实时SLO。需要强结构保持、精确局部约束或费用超限时，保留已验收的反演、显式mask与更保守编辑路径。

## 静态注PRE

- `SF-2026-ARXIV-2603-17989` — Daily `2026-03-20`补查；[DynaEdit exact-v1](https://arxiv.org/html/2603.17989v1)必要§3–6/0.H；2+2+2=6。仅编辑方向聚合与跨步噪声相关协议；保原结构/动作取舍、首帧条件、四配置与人评选择、互动失效和全费用，不采物理真值、任意模型普效/实时或原符号混写的完整recipe。未核代码/全部影片或复现。

## resume20_reader_new非准备者必要Source/actualowner/PRE裁

本人实际exact-v1 §3/Eq1–3接口与§4直接退化、§5.1–5.2/Eq4–7/Alg2（102–215）、§6.1–6.6关键设置/协议（219–253）、§7及0.H（517–522）读；current同六作者单v1，comments只是project入口，无具体纠错/撤回。不需全影片/图像、全部ablation或artifact来支持这两段，不冒像素/代码核验。

源噪声与target由同噪声/编辑state构造，t=1噪声端使初方向除firstframe外弱化source；noise-free编辑state本身仍从sourcevideo初始化，PRE不将它写作直接噪声state。SGA外推候选终点、cosine→softmax选择再转velocity及ANC在采样步（非视频帧）逐渐增加相关性成立；Eq6 bar名字与Alg2 a_i/a_t边界不照录完整recipe。固定全程seed与更强保留/结构修改冲突，cosine不是物理oracle。71人工tuples/49–81frame、Wan14B I2V/先三步5方向、fourCFG/temperature、部分firstframe额外图像编辑、VLM三维评分与32人偏好协议、按edit选配置与所有四配置自动评不能合并，0.H坏互动与保留域受损反侧及未披露hardware/precision/NFE/SLO和全费均保。

实际Ch24开篇、完整280–330端点/输出参数化/球面边界→PixelRush完整段→TFTF→multi-stem共享初始化/两支guidance邻接及Ch25正确路径开篇读；Ch23已读region/alignment交接复用有效域。现浅反演/patch与multi-output共享初noise不能承载inversion-free编辑方向聚合＋跨采样步相关噪声的双约束，soleCh24差额成立。原两literal/static只生成编辑接口，限制/全费近文，未授WorldModel因果。**必要Source/actualowner/原两PRE与static有限PASS**，原5/day保持；root窄锁后才可写，待一次actual非writer完整邻接/本人邻注POST，不预I/DAY。

## resume20_reader_new一次非writer实际POST

rootsoleCh24实际写入后，本人复用原Source/PRE，不重核源；实际完整286–312及末11/本人2541、LaDe与局部全部邻注顺读。两原literal/static机械逐字唯一各1，正文296/298、static2541。限定diff仅本family两段/static六新增，另TFTF将“上段补空间细节”回指澄清为“前面的空间 refinement 和编辑方向选择”，原统计人口/权重机制、假设与反侧全保，不把新编辑段误说成补像素；cached/unstaged限定check0。完整衔接由PixelRush空间refinement→方向/噪声编辑→TFTF人口/权重→multi-stem统计噪声责任，支持/限制/全费与回退近文有效。**一次有限actualPOST PASS**，交root接纳释放本familyCh24，不自计I/DAY或给别日自行授锁，不改static身份。
