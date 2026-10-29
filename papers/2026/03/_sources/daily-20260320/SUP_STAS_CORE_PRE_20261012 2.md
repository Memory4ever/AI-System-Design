# STAS17825：结构位置activation干预的必要原证与最小PRE

resume_mar17，2026-10-12，只03-20补03-19自然日。原五作者/ID、准入2+1+2=5及日级夹证复用有限尾筛选/独核§30，未改日期或分数。当前v2 Aug23明确新增padding、spatial-border和residual-rescaler解释，故仅受影响内容定点深入，不全版本diff、图附件或代码。此稿未自授Source/PRE PASS、未写Books、未safe/DAY，交非准备者裁有限分采。

## 1. 实际必要范围与停止

[exact-v1](https://arxiv.org/html/2603.17825v1) §3–6/Eqs1–5/Tables1–5 L123–276、A测量L282–296/B1算法L297–347与B2具体介入配置353–356、C L357–374、D1/A4 L378–400及D2直接强度/范围反侧L403–417、E/F L423–431。只图caption/正文，不声称像素图或曲线重建。[current abs](https://arxiv.org/abs/2603.17825) L8–28身份/history/完整AB；[v2](https://arxiv.org/html/2603.17825v2)只§3–5 L127–176（padding/spatial/实际mask与残差假说）、§6关键T1–3 L178–206和§8 L255–257、B2/B3必要配置/受影响probe L397–444、E L500–520、I L596–598。未读完整C/D/F/G/H附录或全部图，不用新增LTX数字冒v1实验。

## 2. 可采用接口及未采桥

v1在指定block/early steps，把first-latent-frame与每latent frame扁平排列head/tail百分比的MA维替换为该层当前全token最大绝对值乘alpha、保原sign；不改参数、不增加denoiser调用，但仍在已有CFG两支运行，不是用一次hidden替代全部CFG。v2澄清该head/tail对应row-major空间边界带，不是整个temporal chunk的物理缝；首帧因单帧/因果padding与后帧内容量不同。v2 B3 disable tiled encoding，单帧均值替换/八常色视频和100paired介入支持受限编码结构—干预关联，decoded影响约四分之一含1帧vs4帧人口，不作为Shannon information或真实可靠性定理。

v2 E的non-MA归一尺度衰减可成立，不能从它直接推出任意投影/FFN/attention整体残差必单调减小。作者推断与本文有限Wan双向干预分层保留；独立反例h=(A,1)、RMSNorm、W=(1,0)，输出sqrt(2)A/sqrt(A²+1)随A=1/2/4为1/1.264911/1.371989，非MA坐标虽减小而投影输出增大。MA本身、mean-shift、projection/QK方向与后续token混合都仍改变。v1 Eq2把prediction外推与hidden维缩放称等价，未有非线性网络一般等价依据，亦不采用。仅mask-and-replace接口可独立于这些强解释分采；不是为尽快关闭改中心/NC。

v1 T1三模型aggregate改善但A4 dynamic degree皆退，Wan2.2 objectclass/humanaction、Wan1 color/overall及Cog scene亦退；T4两组合dynamic下降不是已证仅去artifact而无真motion损失。T5 first-only部分consistency退，p50/过大alpha退，模型/层/MA维/K需分别profile，均匀放大全token不合适。计时仅A6000五次/100warmup、234.47→234.53秒的该配置，非全硬件零费或生产SLO；profile/max reduction/mask-write/CFG/VAE仍付费。v2 LTX Imaging66.36→66.35、配对FVMD人口及CI不证明所有视频/指标无损；仅必要评价边界，不扩大数字采纳。未披露完整precision、batch/concurrency、调参全费用/生产SLO对应，Not Disclosed，不因此降分EX。

## 3. actual唯一owner/邻接差额

Owner MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际完整1550–1606：critical-window、granularity、轨迹sensor、source/target FFN activation patch、learned CFG与受训internal readout/prior。已有activation patch讲概念抑制准备与冻结值，没有模型自身MA/当前max、codec结构位置/早步这一非概念干预差额。拟插在activation patch完整两段后、learned guidance semantic-body-binding开始之前（恢复后行位会随ChopGrad/并发变，写前顺读实际marker，不先写）。Ch17实际283–310已承载通用Norm/identity/gradient诊断，不复制该owner理论；Ch23实际入口/379–399 codec消费者及Ch25入口有效复用，仅用encoding layout条件，不冒world/control事实。

## 4. 待非准备者裁的逐字PRE

内部 activation 的控制也可以不由 source/target 概念差指定，而由本模型的编码布局和当前尺度提出。视频 DiT 中，first latent frame 与每帧空间边界的内容负载可因 VAE 的因果时间 padding、空间 padding 与 patchification 不同；扁平 token 序列的头尾带不能直接当作真实时间分段的缝。一条受限分支先 profile 本模型的高幅度维，再仅于选定层和早期去噪步骤，将首 latent frame 和指定边界带中的这些维替换为当前 video tokens 的最大绝对幅度乘校准系数，保留原符号，其余入口位置不直接覆盖。这是在已有 forward 内改变 hidden state，不是删 token、免费替代 CFG 双路径，也不是把 activation 大小认证成语义或可靠性真值。<!-- source-family:SF-2026-ARXIV-2603-17825 -->

较大的单维可压低其他维的归一相对尺度，但经过 projection、非线性和 attention mixing 后，不能据此保证完整残差写入单调下降或非目标位置不变。[必要视频介入与修订解释](https://arxiv.org/html/2603.17825v2)只支持受测配置的结构位置分采；均匀放大、过强或过宽覆盖会退，整体分数改善仍伴随部分运动和语义指标下降。MA profiling、最大值归约、mask/write、原 CFG 和 decoder 均计费；模型、codec、token 排列、层/step 与强度须共同验收。当运动细节、条件质量或完整成本回归失败时，关闭这项覆盖、保留原 denoiser/CFG 和独立输出评价，不从单维尺度签发普遍抑制、时序一致性、无损或端到端零开销。<!-- source-family:SF-2026-ARXIV-2603-17825 -->

静态源注：

- `SF-2026-ARXIV-2603-17825` — [STAS exact-v1](https://arxiv.org/html/2603.17825v1)必要§3–6/Eqs1–5/T1–5、A/B/C与D/E/F直接反侧；[v2](https://arxiv.org/html/2603.17825v2)仅受影响padding/spatial-border、§4–5与B3/E/§8/I及关键评价。仅早步指定结构位置的MA max-reference覆盖分支；保投影/非线性反例、质量/运动反退、CFG与profile/decoder完整费用，不采普遍residual抑制、hidden缩放等价guidance、语义真值/无损或零费。未核代码、全图或复现。

## 5. 非准备者待核

待resume_review17_18必要Source/实际owner/两literal与静态注裁；此句为准备时状态。原5分不变，必要受影响内容深入不是重复评分。强解释反例未清除，可有限分采接口是否成立由独立核决定。

## 6. 独核通过后的sole窄写与writer读回

2026-10-12 reader必要Source/actualowner/原两literal与static有限PASS已本日独核§37，root接纳并授author sole Ch24本family锁。作者重载AGENTS/ROADMAP、ProjectContext/LearningPhilosophy/WritingGuide与当前LS相关路由，实际完整1546–1606及末注后仅将原两literal写activation patch两完整段之后、learned guidance marker之前，正文新1574/1576，静态自身注章末；其他family和marker不改。

writer实际完整1566–1597及最后7行读回原两literal/已核Source一致：概念patch→codec结构位置/当前MA max控制→learned CFG→reward/input/浅层readout交接保持。当前章diff70新增变76新增，本family只两正文＋静态注六行，diffcheck0。不是总残差抑制/无损/免费CFG或全图代码复现；静态注仅source/scope/boundary，不写动态验收身份。待reader一次nonwriter实际完整邻接/自身与邻注POST、root释放后才计I，不自授safe/DAY。
