# Jan02 conditioning / curriculum / physical rollout / perception / prompt repair

最新非作者复核：AMAP24957与ROAD24040必要原源/具体已有覆盖通过；Mesh24428→Ch26 69和X-Dub25066→Ch24 135及各自末注实际正文/前后邻接POST已root核通过。JEPA24497必要原源、Ch25 317/319及末注实际正文/邻接写后POST已root通过；旧过程待核句不覆盖本次记录。

本小批仅取此前67个具名完整题摘潜在中的25066/24957/24497/24428/24040，不是新增库存。25066先前root完整AB校准，24957先前条件准入待core；后三具体准入已送root待定点校准，不授全部Evidence。作者必要审阅按准备好的单项推进。

DataCite保存原created：25066 2026-01-01T03:26:47Z，24957 03:24:07Z，24497 03:13:19Z，24428 03:11:42Z，24040 03:02:28Z。官方holiday/noadvance-ID共同给最早Jan1T01Z至created下一秒的公开区间，完全落Jan02；不是注册精确公开或Submitted=公开，作者更早正文信号仍会定点重开。

## [AMAP Agentic Planning Technical Report — 2512.24957v1](https://arxiv.org/html/2512.24957v1)

拟2+1+2=5。必要§2.3–2.6/§3已实际读：静态teacher funnel不是增量，当前policy每题8轨迹的reward mean×variance选择是随能力变化的优化人口；reward variance不能直接当epistemic uncertainty或梯度价值。rubric由teacher动态加权且有hallucination veto，不是独立事实真值。Qwen3-30B-A3B、Gemini3Flash oracle/judge增加全池采样成本；TravelBench与online人口不同，general benchmarks有退步，没有matched total-budget静态selector消融。硬件/precision/完整训练与curation成本未披露，不复现。

作者具体owner已读Ch27 562–607/1013：policy-relative sweet spot由当前checkpoint rollout/正确率/方差判断retain/revise/retire；selector/frontier与generator/verifier权限分开。这真正承载拟采用的能力相对选择与条件预算边界，不声称已覆盖mean×variance公式。root实际核exact-v1 §2.4–3.3与Ch27 560–610，5分标准审阅/具体ExistingCoverage通过；无新增正文，不把mean×variance或Travel评分写成普遍保证。

## [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing — 2512.25066v1](https://arxiv.org/html/2512.25066v1)

拟2+1+2=5。实际§3.1–3.3/4.1/4.3、C.1/C.3、D/E/F：完整帧对齐reference-token条件与待修改lips可能冲突，按噪声区域训练结构/唇形/纹理LoRA并限定部署激活区间。F四设置中uniform editor不收敛，inpainting统一/分阶段差别小；这是该paired-context编辑目标的局部条件，不是通用multimodal三阶段定律。C.3区间经HDTF调参，不作固定常数或免评价策略；其像素重建clipping不改变模型实际t。

32GPU、600h generator/400h paired上下文、15k/4k/1k+1k步，synthetic generation另约2天；生成/筛选/分阶段LoRA均付费。D约1B与E约1.5B口径未统一，GPU型号/precision/seed未披露；E的50step/512²/3秒约60秒不同于加缓存/并行/减步后的25秒，不授同质量或总成本优势。主线只采conditioning与噪声阶段目标冲突，不扩通用audio/video鲁棒或生产实时。作者Ch24 109–150目标/时间方向及131–133 reference注入边界已实际对读，尚缺干净逐帧reference与目标编辑冲突、阶段LoRA适用support的具体承接，待root必要源/owner核后才提窄整合。

## [What drives success in physical planning with Joint-Embedding Predictive World Models? — 2512.24497v1](https://arxiv.org/html/2512.24497v1)

拟2+2+3=7，完整AB准入已root实际核。作者必要§3/4、§5.1/5.2、B的reproduction/multistep variants、C DROID/Robocasa、D预算及E3已实际读：同为两步训练仍可能混不同target index、groundtruth/prediction context与梯度路径。作者报告旧VJEPA2AC two-step目标错误并重训，代码未独立运行，不冒称artifact复现。混合真值/自产context更接近planner unroll；last-gradient/TBPTT与equal-order/all-gradient不同，2-step局部收益不授更长rollout单调改善。CEM/NG同N/J，GD/Adam不同搜索设置；相同episode预算非相同墙钟。

最终3training seeds、96episode（DROID64/Robocasa32）、末10epochs均值（DROID100）且errorbar跨epoch，不把相关epochs作iid。DROID真实数据只ActionScore，Robocasa简化/相机匹配且Pick低成功，不授真机planning优越。16/32H100、固定encoder/predictor变体，precision未披露；video/image encoders preprocessing/patch/resolution不同，不能纯encoder因果。E3 epoch相关proxy不授通用成功保证。作者拟Ch25 gap=multistep训练target/输入来源/梯度路径身份尚未被313–319与630–637的通用rollout分布正文具体承载，待root原源/owner核。

## [Subsecond 3D Mesh Generation for Robot Manipulation — 2512.24428v1](https://arxiv.org/html/2512.24428v1)

拟2+1+2=5，完整AB准入已root实际核。作者必要II-C/III-B/III-E/IV-A–C/V-A已读：textureless生成mesh失去render-refine所需外观；learned monocular depth无metric尺度，valid sensor depth的mask内median对齐再注册提供尺度。RANSAC+ICP依赖mask/几何/初始化，不能单由visual fidelity认证robot frame。25YCB/10runs的component replacement，DAv2-only显著失败、rawdepth反而更快且几何稍差；GPU RTX5000Ada/CPU7960X/256GB，precision未披露。耗时824ms仅per-object pipeline，pickplace整十object makespan；table92%人口分母未完整披露，不授开放部署安全。H3D baseline成功更高，texture/重遮挡/非刚体/杂乱限制保持。未运行实现。

作者实际Ch26 45–68已有calibrated geometry/frame/单位条件，但尚未具体承载去texture的表示消费兼容性与monocular形状/真实metric锚二分。拟局部gap或onlyreport需root具体owner判断，非因领域任务或借FlashVDM自动准入；不重复成熟distillation加分。

## 24040

拟2+1+2=5，完整AB exact-v1 HTML L73–77已恢复、待root实际校准。作者必要§3.1–3.3/Alg1、§4–5/§6.4已实际读：failure-only logs→Analyzer/Optimizer决策树→Coach prompt是提案过程，树是文本不是确定runtime guard。Pnew/P在同D逐轮比较并接受改善，patience不消除adaptive validation；o4-mini第二轮峰值第三轮退步，ExpectedChunkID存在grounding信息，未披露独立population/seed/完整meta-call预算，不授样本效率或RL等价。safety文本YES不是外部authority，未运行代码。

作者实际Ch74 125–164承载规则被读取/context/compliance/outcome链、提案规则保存scope/failure/evidence/validation、formal spec非行为保证；Ch80 40–120承载反馈独立性、修复假设不等失败归因、bounded prompt update/reset/budget/rollback。具体已覆盖拟采用的failure-derived rule更新与validation/执行权限分账，不声称已写决策树recipe。拟ExistingCoverage待root必要原源/具体owner复核，不以主题相近关闭，不授全论文通过。
