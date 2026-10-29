# Dec19 Meta watermark 单篇身份 / Source / owner提案

## 1. 四身份与事件分责

实际从[官方global_search page3](https://ai.meta.com/global_search/?page=3)的Dec26→Dec18四项→Dec17数据→Dec16SAM邻接进入各独立原页，四完整题摘均已读，均印Dec18,2025；旧小时/TZ门解除。不把目录日期统一当各论文首次。四官方PDF按钮各实际一次cache miss，不重同CDN或换host；具名可读arXiv精确版只作相应角色补证，不legacy。

| 家族/原页 | 当窗角色及作者判断 |
| --- | --- |
| [Unused Capacity / ChunkySeal](https://ai.meta.com/research/publications/we-can-hide-more-bits-the-unused-watermarking-capacity-in-theory-and-practice/) | 官方Dec18披露date-only成立；[2510.12812](https://arxiv.org/abs/2510.12812)及exact-v1完整AB/版本字段实际核，同PSNR/linear-robustness容量与ChunkySeal core身份，不另造家族。v1 submitted Oct7不是原公开日，v2 revised Dec20也不是Dec18新重要修订证明；撤销本包此前把October版本字段当窗前首次的推断。当前不能确认Dec18仅再索引或具名新artifact/重要修订，保最窄机制潜力与必要事件角色hold，不评分/确定候选/Books；仅接受实际官方先公开字段、dated作者原件或Dec18明确新差额定点重开，不重理论全文/双版全文/全repo。 |
| [Post-Hoc Rephrasing](https://ai.meta.com/research/publications/how-good-is-post-hoc-watermarking-with-language-model-rephrasing/) | 官方Dec18研究披露日；[2512.16904v1](https://arxiv.org/html/2512.16904v1)是本轮必要方法/反侧补证，不将submitted18等于公告日。准入为服务端生成约束→离线rephrase可分配生成/检测算力且code正确性限制选择→重新考虑质量/检测/总费用联合目标，拟2+2+2=6，安全/owner具体缺口深入。 |
| [DistSeal](https://ai.meta.com/research/publications/learning-to-watermark-in-the-latent-space-of-generative-models/) | 官方Dec18明确latent后处理与蒸馏到generator/decoder的研究轮廓；[2601.16140v1](https://arxiv.org/html/2601.16140v1)是January后稿，仅当前必要反侧/机制边界补证，不授Dec18完整配方。像素后处理成本→latent及两个权重位置分支→重估可绕过组件与质量/延迟责任，拟2+2+2=6；已有Ch72具体采用域待Newton校准。 |
| [Pixel Seal](https://ai.meta.com/research/publications/pixel-seal-adversarial-only-training-for-invisible-image-and-video-watermarking/) | 官方Dec18研究披露；[2512.16874v1](https://arxiv.org/html/2512.16874v1)必要机制/直接反侧补证，不代授arXiv首公告。准入为低分辨率训练/插值部署错配与目标竞争→分阶段adversarial+message和全分辨率路径模拟→重估水印训练/实际检测输入的一致性，拟2+1+2=5，具体安全/owner缺口深入。 |

不是四项都是新first-public，也不把同repo的两个paper合为一机制；原四种潜力保持各自身份。本包请求Newton校准三新研究披露与一去重角色，不以拿不到PDF降低准入/评分。后稿补证不证明所有细节已经Dec18公开。

## 2. Post-Hoc必要证据及拟采用

实际读exact-v1完整题摘、§3、§4.1–4.6必要方法与代码反侧。生成beam/multi-candidate和检测entropy filter是不同费用；检测只见watermarked text，不能复制生成期entropy。文学切片有长度过滤，故有点不代表全部输入成功；code TPR须同时看pass@1及只在Passed人口的统计，失败/重复文本能虚增检出。方法间/大小模型不是单调支配，WaterMax过滤反退；必要key/null校准和dedup不授任意文本FPR。未核artifact/复现，不采用最优模型或倍速。拟保留条件化预算/功能正确性责任，而非宣称水印证实所有权。完整硬件/precision/部署concurrency/SLO及总成本未披露。

actual Ch72 215–247完整水印局部已读；241段Gumbel detector是fixed generator的sensor分责，243起是密码不可伪造，不拥有离线重写的生成/检测预算与code质量人口反证。唯一PLATFORM-SECURITY，不把该安全取证机制重复进Ch66或生成范式章。拟在完整“固定生成器时，统计水印的检测器也可单独改变……”段后、“当输入与密钥独立、目标只是低误报筛查时……”段前一自然段。尚未书锁。

逐字PRE：

对已经存在的文本，另一分支让模型带水印重写，再联合选择重写模型、采样或beam预算和检测时的评分人口；这些预算不受同样的在线生成延迟约束，却仍需支付重写、候选搜索与检测调用。检测只见改写后文本，其entropy条件不能当作生成期条件；对代码还应同时验功能正确率和通过测试人口中的检出率，不能让退化、重复或执行失败产生的强信号冒充可用保护。[受限重写对照](https://arxiv.org/html/2512.16904v1)中，大模型、更多搜索或entropy过滤都不保证一致改善，文学结果还受长度筛选；code检出不认证未测功能或合法所有权。应绑定原文/派生文、key/null校准、模型与生成/检测预算，功能或误报条件失准时保留原制品、签名来源与独立核验，而不是继续放大水印强度。

本人末note逐字拟稿：

- `SF-2025-META-POSTHOC-WATERMARK`：Dec19补Dec18官方研究披露；[原页](https://ai.meta.com/research/publications/how-good-is-post-hoc-watermarking-with-language-model-rephrasing/)与[exact-v1](https://arxiv.org/html/2512.16904v1)§3/4.1–4.6。Boyle拟2+2+2=6，采用生成/检测预算和功能正确人口分责，保长度筛选、key/null、WaterMax反侧及非所有权权限；未授Source/PRE/书锁/写入/POST/DAY，未核artifact或复现。

## 3. DistSeal必要补证与已有覆盖提案

实际读January exact-v1 §4.1–4.2、§5.1必要设置与Table1–2，identity/AB有作者列表与措辞差额，不把后稿当Dec18不可变快照。后稿细参数、LoRA遗忘/decoder替换等不声称Dec18已披露；本日官方原AB足以支持“latent后处理可蒸馏到generator或decoder”的窄轮廓。已实际完整读Ch72当前225整段：明确decoder可替换、generator后续LoRA遗忘、component/message/detector/update身份与费用/非authentication边界，且正文准确引用Januaryv1。它真实承载本日可采用的较窄机制，不仅标题相似。拟已有覆盖PLATFORM-SECURITY该完整段，不改旧note或挪January归属；不采20x、具体配方/同质量普遍收益。待Newton/root实际本日角色与覆盖核，不预签。

## 4. Pixel Seal必要证据与逐字PRE

实际读exact-v1 §3、§4.1–4.4、§5.1–5.3/Table1–3必要方法和直接反侧。adversarial-only指去MSE/LPIPS，仍有message CE，不是无重建目标；三阶段先稳定message再加入adversarial/降幅，低权重MSE不总失败，高权重失败不能泛化。原分辨率JND与train-time inference simulation避免下采样/插值两条路径不相等；判别器强弱、boost、JND和robustness有取舍。Photos100/生成图1000、视频仅首3秒及不同payload/攻击集，bitacc与p值和感知代理分别解释。MovieGen/SA-V compression项仍略低于VideoSeal1，不能照录all superior；内部JND评估回归器不等JNDattenuation图。未核artifact/复现，不采2.2x为全流程收益，完整训练/部署总成本不全披露。

Ch72当前223末EmbTracker发行实例段与225 DistSeal可替换组件段完整邻接已读，不具体承载训练/高分辨率检测路径错配。拟仅在这两个完整段之间一自然段，唯一PLATFORM-SECURITY；另已实际读Ch71开篇tenant identity与Ch73开篇production闭环交接，不迁移其owner，未授锁不写。

逐字PRE：

后处理水印还需要匹配真正的检测路径：在低分辨率图上叠加扰动再检测，与先把扰动插值到原图、叠加后再缩小，不是同一输入。训练可模拟后者，并在原分辨率计算局部衰减，使检测器和判别器见到部署时的组合；也可先学可恢复message，再逐步加入对抗约束并降低扰动幅度，而非同时强推相冲突的目标。[受限水印实验](https://arxiv.org/html/2512.16874v1)的adversarial-only仍保message loss，感知代理与真实可见性不等价，鲁棒性和不可见性也仍有取舍；短视频和有限变换的检出不能外推任意编辑或来源认证。高分辨率模拟、分阶段训练与独立画质/误报校准都有成本；路径变化或内容失真时，应回到匹配部署变换的验证、较保守扰动及签名来源，而不拿一个bit准确率签发完整保护。

本人末note逐字拟稿：

- `SF-2025-META-PIXEL-SEAL`：Dec19补Dec18官方研究披露；[原页](https://ai.meta.com/research/publications/pixel-seal-adversarial-only-training-for-invisible-image-and-video-watermarking/)与[exact-v1](https://arxiv.org/html/2512.16874v1)§3/4/5.1–5.3/Table1–3。Boyle拟2+1+2=5，限定检测路径模拟与分阶段目标，保message loss、感知/鲁棒取舍及视频compression反側，不授全编辑防护/所有权或全流程加速；未授Source/PRE/书锁/写入/POST/DAY，未核artifact或复现。

## 5. 两窄位真实保存与作者self-read，待实际POST

检查范围更正：本机文件系统可用Books大小写读取，但Git tracked path实际为小写books；作者此前大写pathspec的空输出不能证明diff为空。U18写前现已按git ls-files确认小写，实际完整读回水印两段/两注的unstaged8add/0del、cached空，与Newton13/14和root4实际检查一致；原Source/PRE/POST/root/admin闭合均不重开，本更正只修正作者Git检查依据，不改正文/他注。

后续真实链已发生：Newton§13/14分别实际全文新增/完整两侧/本人注POST通过，root§4实际读回接纳两项并释放两窄位。Boyle随后只改两本人注尾行政状态，实际完整读回两注/限定diff-check0；没有改正文/他注或January旧注，不再需要重复POST/Source/PRE。待root仅行政差额直接读回，非DAY。

Newton§11已实际确认DistSeal6分/必要后稿补证及当前Ch72具体已有覆盖，作者同步此既成层，不写书/原January注；Newton§12指出ChunkySeal不能用submitted month推首次公开，本包§1对应行已修正为同core身份、不授确定窗前O/新事件，保必要事件角色。一次限定作者/机构网页搜索仅返回MetaDec18原披露，未恢复官方先公开字段，停止；不重旧失败官方search/legacy或全站。

2026-10-15T16:49:23+08:00，Boyle按Newton§9/10与root§3真实许可执行。写前实时完整读Ch72两处原锚点/邻接、末本人拟注处及前注，cached/unstaged限定numstat均空。只逐字插§4 PixelSeal一自然段在完整EmbTracker第二段后/DistSeal前，逐字插§2 Post-Hoc一自然段在完整Gumbel detector后/soundness前；末各追加本人一条note，仅同步真实Source/PRE/root写前许可，不预POST。未改原段/marker/他注、Draft、其它章或index，未stage/commit/push。

保存后实际顺读Ch72 218–255，完整看到EmbTracker两段→Pixel→DistSeal→后续分支及Gumbel→Post-Hoc→soundness/签名分支；实际读两本人note与前注。完整限定diff只8新增（两正文自然段和两note及空行），两层diff-check均0。Pixel保message loss/感知与鲁棒取舍、短视频边界/费用与退路；Post-Hoc保生成检测条件不同、功能人口/长度/key-null限制和签名/独核退路，与PRE无实质差额。此为作者真实保存/self-read，不代Newton actual完整新增/两侧/note POST，也不代root接纳释放；两窄位待后续实际链，非DAY。DistSeal/U18未在本许可，不写。
