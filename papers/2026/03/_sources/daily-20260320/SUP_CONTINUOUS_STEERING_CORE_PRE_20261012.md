# ContinuousSteering17998：必要Source与sole Ch24两PRE

resume20_author_new sole准备，仅本20补03-19；原2+1+2=5/date准入有效复用，不自授Source/PRE、Books锁或DAY。

## 1. 必要源/停止

[exact-v1](https://arxiv.org/html/2603.17998v1) §3.1–3.3/Eq1–4/Elastic Listing、§4/Eq5–8/T1–2、§5与supplement Elastic hyperparameters、CompetingMethods必要协议、EvaluationDataset必要人口、InferenceDetails/Runtime/T4–5有限读取。current abs同两作者单v1，无具体撤回/纠错信号。停止全部prompt/图像例、全部baseline配方/方向分析和代码，不核复现。

## 2. 支持/关键反侧/费用

LLM生成100对概念contrastive prompts并选span，冻结text encoder对应span mean后difference-of-means/L2方向；部署另选inputprompt token，加alpha方向。各自prompt pooling仍是contextual表示，balanced生成不是已验无偏/语义独立，Eq3/4池化后[j]与span名称混写不照录为完整recipe。LLM/encoder/tokenizer/concept/span身份都进入方向缓存，不是任意hidden末token编辑。

image生成后DreamSim gap提出control points：大gap插midpoint，内部点向大gap一侧移动/夹定序，最后对unsteered image distance区间过滤。只是离散点集/代理搜索，不是保证有效完整interval，点间/未见prompt/概念端点可达性另验。Listing a_min未用、正文alpha_max对unnormalized s投影与实际单位方向尺度未闭合，故不采精确全输入recipe或收敛/optimal范围。

Eq6绝对VQA增量与LPIPS增量分别归一作MID；VQA序列0,1,0且相邻感知距离相同可MID≈0，却非单调，同为零增量还可得0。只度量无符号增量分布一致性，非真正方向/顺滑/语义成功；全文DreamSim距离/相似度命名也不改成真实置信。T1Flux MID .39不优FluxSpace .33/SAEdit .36，Qwen .42虽ΔVQA .63高仍低Slider .75且MID未最佳；T4/5保更强edit损保留，指标非盲humantruth。198eval prompts的synthetic概念人口与100contrastive dataset分开，主要6slider点/无独立seedCI；不同backbone/指令图像 vs text-only协议不采唯一因果胜。

supplement local T2I后期linear加强，global全程；I2I先获得编辑图再负方向抑制，非T2I完全同许可。视频只定性方向，§5明确无足够video perceptualmetric，elastic search未作，不授video连续质量。底座不能生成6指则无方向可实现端点。

成本：concept缓存生成67.5s+pool1.09s，perprompt selector3.29s+search25.75s，平均13.92±3.87候选images/30step，不能只说单生成约3s。poolbatch100/单H100、512²/候选batch20/perceptual64、SGLang/FA3；precision/完整硬件分工/并发尾SLO未齐。supplement一般local distance[.05,.15]与runtime[.15,.40]不同，global[.15,.30] vs [.25,.40]，计时口径不是全部质量配置；LLM/生成/感知搜索全付费，不采免费testtime/实时。

## 3. actual owner与原两PRE

sole `MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，actual1545–1586 fixed/runtime operatingpoint→criticalwindow/CFG完整邻接和开篇已读，Ch23融合条件/Ch25生成与transition交接复用。已有timestep/CFG控制未承载“冻结text条件方向→inputtoken权限→perprompt感知点集搜索”的旋钮；模型hidden编辑仍Ch16拥有，方向cache不是Ch75动态context。拟critical-window标题前两段，承接模型控制量与runtime计划不同责任，不写第二owner。

### 正文PRE 1

连续编辑的旋钮还可以前移到冻结 text encoder 的输出，而不改变 generator 权重：按概念构造对照 prompts，只对指定 span 池化后取均值差和单位方向，再由当前 prompt 的 token 选择器决定哪些条件位置加上该方向。概念方向与本次输入的介入范围是两个接口；自动生成的平衡对照与相近 embedding 不证明属性已因果解耦。Encoder/tokenizer、概念对照、span、方向尺度、输入 token 选择与去噪时窗须分别绑定，图像条件与纯文本条件也不能共享默认强度许可。<!-- source-family:SF-2026-ARXIV-2603-17998 -->

### 正文PRE 2

可用多个候选生成的相邻感知距离调整控制点，并对相对原图的距离过滤，但得到的是本 prompt 的离散代理点集，不是整个区间的语义单调性或未见输入保证。[连续条件编辑的有限对照](https://arxiv.org/html/2603.17998v1)仍有更强编辑损保留、指标反退和底座无法实现概念端点；绝对语义增量与感知增量同分布，也可能掩盖方向反转。概念生成与方向缓存、每 prompt 的 token 选择、重复候选与感知求值都计费；视频尚未得到同一搜索验收。方向混杂、端点不可达、点间回归或净预算不成立时，保留固定小强度、原条件路径与独立编辑/保留检查，不把自动 slider 当无损控制器。

### 静态来源注PRE

- [ContinuousSteering2603.17998 exact-v1](https://arxiv.org/html/2603.17998v1)：必要§3/Eq1–4/Listing、§4/Eq5–8/T1–2与§5、supplement搜索/人口/输入权限/runtime/T4–5。只冻结text输出方向/当前token资格与perprompt离散感知搜索分责；保无符号MID不保单调、编辑/保留反侧、不可达端点、T2I/I2I区别、未验video搜索与全费用。不采balanced即无偏/完整recipe、全区间/未见概念可靠、免费实时或SLO；未核全部prompt/图像/代码或复现。<!-- source-family:SF-2026-ARXIV-2603-17998 -->

仅prepared，交reader非preparer必要Source/actualowner/两PRE有限核；root Ch24 sole锁后才写，仍需一次非writer actualPOST。

## 4. resume20_reader_new非准备者必要Source/actualowner/PRE裁

实际exact-v1 §3/Eq1–4/token selector/Elastic Listing（112–285）、§4/Eq5–8/T1–2/关键反侧与§5（286–353）、supplement搜索配置（451–529）、competing设置仅必要输入/方向权限（530–623）、EvaluationDataset人口（868–872）、InferenceDetails/Runtime（1062–1116）、T4–5（1117–1139）及current同两作者单v1读；不遍历全prompt/图像、方向相关分析、代码或复现。100对概念对照生成和198eval prompt不是同分母；抽取概念span的mean/difference/unit方向与当前prompt介入token选择是两阶段、冻结encoder不更新generator，contextual pooling仍可能混杂。原Eq3/4池化后[j]/style span混写与alpha_max尺度不闭合不照录完整recipe。

Listing dist邻点→大gap插midpoint/移动内部点/夹定序、相对原图距离filter输出X_valid，仅离散代理搜索，不授点间语义、完整有效interval或全input收敛。本人复算Eq6–8：VQA序列0,1,0、感知增量1,1，则两归一无符号分布相同，MID=0而方向反转；零分不是monotone证书。T1Flux .39劣FluxSpace .33/SAEdit .36、QwenMID .42仍非最佳；T4/5更大editing/proxy与内容保留取舍、不同backbone/指令图像权限未全match、無video elastic及不可达6指端点反侧保。DreamSim/ΔVQA不是盲人审或物理真值。

必要实费C概念生成67.5s/pool1.09s与每prompt selector3.29s/search25.75s、13.92±3.87候选×30step分账；H100池化、512²/batch20/perceptual64/SGLangFA3只是所报包络，不构成每次3s/在线SLO。原质量配置local .05–.15/global .15–.30与runtime .15–.40/.25–.40差异保。T2I局部后期linear、global全程；I2I有image anchor且先edit再负方向抑制，不沿用同许可。全部LLM/缓存/生成/感知搜索与回归付费，未披露precision/完整并发不补造。

actualCh24完整1544–1590 operatingpoint预算→critical-window完整/后续generation policy与开篇有效域读；Ch23condition/fusion、Ch25生成与transition分责复用。不将既有step/CFG计划当text-output方向/当前token资格/perprompt离散点集控制接口已有覆盖，soleCh24最小差额成立，拟critical-window标题前两段；原两literal/static正确分离方向构建/介入与范围证据、局部失败/费用/回退近文。**必要Source/actualowner/原两PRE/static有限PASS**，原5/date保持；root具体Ch24窄锁后才可写，待一次actual非writerPOST，不预I/DAY。

## 5. rootsole窄锁下writer落实

2026-10-12 root授本family Ch24锁，resume20_author_new按§3原两literal/static写1575/1577与本人2553。writer实际1570–1591完整邻接及末7本人/Dyna/已核别日邻注读回，两literal/static各唯一一次；runtime预算→条件输出旋钮/离散搜索→critical-window不同责任主线保持。限定diffcheck0，不stage/commit/push，不预计I/DAY；交reader一次非writer实际POST/root接纳释放，不重核Source/static身份。

## 6. resume20_reader_new一次非writer实际POST

复用§4有效Source/PRE，不重核源；实际完整1570–1596 runtime operatingpoint→原两段→critical-window完整/patch-policy/后续control交接及末7/本人2553、DynaEdit与03-25Theory全部局部邻注顺读。两原literal/static机械逐字唯一各1（1575/1577/2553）；限定diff本family六新增、cached/unstaged check0，原Dyna/别日Theory内容保留且不重裁。方向构建/本prompt token资格/离散感知点集分责、MID方向反転/质量和可达端点、图像条件许可/未验video及全部费用/小强度回退均近文保持；控制点搜索不改成runtime自动跳步许可。**一次有限actualPOST PASS**，交root接纳释放Ch24，不改static身份或自计I/DAY，原5/date保持。
