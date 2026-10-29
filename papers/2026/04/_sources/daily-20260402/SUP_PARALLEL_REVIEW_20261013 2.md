# Parallel data `2603.29026v1` — 数据增量与 alignment 测量分责

root完整AB及必要Source5已实际核通过，真实命题tuple `2+1+2=5` 已root确认，作者实际读必要v1§3–5、Limitations及仅匹配训练预算必需D。[原件](SUP_PARALLEL_CORE_20261013.json)；其它附录/代码未读未复现。正常复合日门/owned上界在 `SUP_STANDARD_DATE_SIGNALS_20261013.json`，不等所有paralleldata无用。

## 可支持的实验身份

四个OLMo-style1.4B从头200B-token，English/Finnish80/20，parallel0/1/2/5%；source均FineWeb/FineWeb2+OPUS译对。为控制domain，所有arm固定5%source来自paralleldataset，改变的是成对格式暴露，不把0%说成完全未使用译对源文本。60instruction/completionformats，BPE50280balanced tokenizer；各source分chunk避免附带crossling concatenation信号，batch仍混合shuffle。

D明确LUMI32 MI250X/64GCD/8nodes、1024×2048约2Mtoken/batch、95367steps、AdamW同cosineLR与warmup。没有独立多seed模型/repeatedtraininguncertainty，200B总额不等所有非padding有效tokens或任意更多data效应。早阶段20000steps是相同step预算比较，非跨scale定律。

## 对alignment的多种读出与反側

PCA FLORES997meanpooledhidden、2000WMTNewscos+random50control、20000pair PWCCA+shuffle/untrained、AP语言神经元、200ROCstories×5continuations的MistralMedium3 judge分别测不同对象。高cos也在randompairs/untrained出现，不能把cos本身认证语义共享；PWCCA高于shuffle/untrained支持线性关联，非causal跨语言任务能力。

终态PWCCA无parallelshare趋势，含早checkpoint的PWCCA也无明确比例相关；‘early更alignment’主要来自languagecontrol α=.09下，controlled-Finnish continuation coherence相对Finnish baseline的difference。把difference=0假定为完美alignment本身未独立证明，judge/译文Gemini2.5Pro与beam人口也会影响；它是有限proxy改善，不把representation sharing加速当已证因果。终态fluency无parallel比例收益、coherence仍退于各自uncontrolledbaseline，高share的略强coherence也可能baseline整体更强。

AP阈值语言特异神经元随训练反增、不趋收敛，完全languageagnostic≤.55数量近似不变；较低特异阈值计数略减少与整体sharedrepresentation不是同一结论。神经元数/PCA/cos、PWCCA与controller输出分别验收，不从一种读数给全部alignment签证。

## 拟窄采用

parallel暴露在此0–5%、1.4B、一个远距语言对/200B预算里，不保证终态共享表示指标按比例提高；早期proxy优势不等终态能力，诊断对象/阶段须分离。不是否认paralleldata翻译用途或所有多语言数据、不是以language标签排除。必须保更多比例/scale/语言对未测，author‘hardcase所以可能泛化’不当证据。Books具体NC owner TRAIN-PRETRAINING：Ch28第145行已有同任务checkpoint/不同形成顺序、表面词形干预定位假信号与局部小模型不授普遍学习阶段，Ch27 1350–1361交接parallel/code-switch/quality-mixture。root实际读Ch28 138–150及Ch27 1350–1363接纳NC5，只复用本次受限命题，不称全paper内容已有覆盖或代码复现。
