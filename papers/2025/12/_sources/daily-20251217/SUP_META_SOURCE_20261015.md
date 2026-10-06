# Meta两family / Dec17补Dec16评分与当前owner

作者Boyle。SAM Audio与PE-AV是两个家族；原官网Dec16研究披露日门承Feynman§2有效，本轮actual各原页完整题摘/作者/date/paper出口再核，不重两个旧fbcdn超时，不要求后arXiv与Dec16PDF同bytes才承认研究披露。具体后稿方法采用仍分别保版本权限；本包待Newton独核，不预签Books或DAY。

## 1. SAM Audio

[原事件页](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)明确Dec16,2025；完整AB披露flow-matching Transformer统一text/visual/span提示、跨speech/music/general sounds混合训练、reference-free评价模型及human-prompt benchmark。原负侧“普通X公告无独立贡献”不取消这份已有效原研究披露。

固定类别或单一text提示不能唯一选出混合音中的目标→联合生成target/residual、以语义/视觉及active/silent时间条件约束目标的分离接口，并用独立人评核judge→生成条件、实例消歧与输出正确性须分验。拟 `2+2+2=6`：DD2为多种条件进入同一分离生成的具体机制；Reach2是条件接口与输出评价边界，不借任意Agent或基础设施扩大；D2为可复用但非通用质量保证。SAJ不另增family，也不让“相关人评”变正确性authority。

必要Source按[META_NECESSARY_EVIDENCE](META_NECESSARY_EVIDENCE.md)的2512.18099v1 §3.1–3.4/5.2–5.4/7.3–7.4/7.8.1/D.1–D.3复用：连续DAC-VAE latent的target/residual沿channel联合flow，25Hz视觉/span条件与text cross-attention、随机条件drop；联合latent不证明target/residual波形严格相加。span-only持续声/音乐反退、predicted-span专业器乐反退，时间片不能代实例身份。AED只pretraining，3B general-SFX对照不外推全域。SAJ三次人评/音量归一、recall/precision/faithfulness分项与相关性不等逐例/OOD正确。未复现、未核全部附录/权重或听测。

此v1是Dec19后稿补证，不声称Dec16已有全部细节。本次原披露直接支持的采用对象只“语义/视觉/时间条件共同限定被分离目标，缺失/冲突条件与生成结果分验”；channel/25Hz、具体drop配方/SAJ数值仅报告为后稿可核细化，不倒填原日历史recipe。真正依赖Dec16特有原PDF的命题仍不采用。

当前唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。actual读开篇1–54及音频完整874–916：现语音码层、patch时间粒度与flow/AR生成状态不等于promptable source separation；现audio/video编辑在437–439处分流preserved与regenerated，也不解释从同一mixture选target。需要在音频论证链、语音输出节奏之前另核准确分离分支锚点；拟只一段条件接口，不改Ch23表示或另写Ch66通用judge原则。具体gap待Newton核，尚未逐字PRE/获root锁/写入。

## 2. PE-AV

[原事件页](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)明确Dec16,2025；完整AB披露统一audio/video/text/joint embeddings、caption数据引擎、pairwise对比目标以及PE-A-Frame帧级适配。不是由后来v1 submitted日授本事件。

全局pair检索不规定事件何时发生→在统一多模态表示上另设帧级对比及local/global activity监督，局部定位和误报指标随目标采样作相反取舍→不能以更大pair/data规模或全局均值代签连续定位。拟 `2+1+2=5`：DD2为监督粒度/竞争的具体约束；Reach1仅表示/对齐组件，不借下游分离/Agent算Reach；D2为可复用有条件评价边界。必要方法/反侧及实际gap按最低标准以上深入受影响域。

必要Source复用2512.19687v1 §2–3、§4.3/Tables6–10、§5.1/Fig12及D.2/Table19：八pretrain pairs与stage2新增两joint retrieval pairs分阶段，不能说十项同阶段；real/synthetic固定样本与数据规模、pair数不同消融分责，16M/32M与更多pair并非每项单调；base/100k步/batch800不与完整模型作单因素因果。Fig12提高local采样改善边界同时损害惩罚false-positive的指标，0.7不是通用最佳；all_gather优化仅后稿实现/受限配置，不外推端到端。该v1是Dec22后补证，不声称全细节Dec16已公开或同bytes；原AB已有frame-level与global表示的采用轮廓，具体反侧以注明的后稿约束历史披露，不倒填原日确切recipe。未复现/核全部实现。

当前唯一owner `MULTIMODAL-REPRESENTATION` [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。actual读开篇1–54、完整936–982及1002–1035时间/provenance段，第一次宽输出截断部分已窄回读936–982，不将截断作全读。现对齐段明确semantic/temporal/action、contrastive全局不保证局部、多目标权重决定保留信息；这些原则已有覆盖。具体尚未由该正文承载的是帧级local activity与global对齐的训练人口/采样权重竞争，边界与误报要并列验收，而不是只说“时间戳要对齐”。可在该节现多目标权重完整段后窄融一段，保原全局/局部原则；不把ten-pair罗列或100M宣传再写进书。

请Newton分别核两family新评分、原事件与后稿角色/必要命题相容、具体Ch24/Ch23 gap。只恢复受影响原证和相邻论证，不重两份全部PDF或旧下载失败。若gap通过再准备逐字最小PRE/root窄锁；当前Books新写0，非Evidence整体通过或DAY。

## 3. SAM唯一Ch24一自然段与本人末注逐字PRE（未写Books）

Newton§13已actual通过6分、必要采用权限及唯一Ch24 gap；root实读本包及当前音频874–921邻接，准许PRE准备未授锁。作者actual补顺读866–898完整邻接：准确前段为RNNT离线/流式一致性限制段，以“这仍需两种模式前向和RNNT训练”起、以“不把‘模式一致’升级为普遍最优解”结；准确后锚点是独立`semantic-body-binding:SF-2026-ARXIV-2605-20946:start`及语音/reasoning交错完整段。只在该marker之前插一自然段，从识别的监督对象转到混合音分离条件，再接语音生成；不改ASR或speech原文。

拟逐字正文（一自然段）：

> 音频生成也可以从已有混合音中选择目标，而不是从文字生成整段声音。固定类别或单一提示在目标明确时简单有效；同类声源重叠后，可把文字语义、视觉区域和时间span共同作为条件，让flow生成被选目标及其残余。[SAM Audio的原研究披露](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)给出这条统一分离路线，后续[精确v1](https://arxiv.org/pdf/2512.18099v1)补证了联合latent与条件接口，并显示span-only在持续声/音乐上退步、预测span在部分专业器乐切片也退步；因此时间范围不是唯一实例身份，联合latent也不证明两条波形严格相加。模型的reference-free judge与人评相关，不等于逐例或分布外正确，需分开验收目标是否选对、是否漏声或混入其他声源、输出保真与完整费用。条件编码、codec、迭代生成、judge及人评都付费；提示缺失/冲突或质量不稳时，保留原混合音、补充条件、专用分离器与人工复核，不让时间提示或judge分数代替实际听测。<!-- source-family:SF-2025-META-SAM-AUDIO -->

拟本人末Review note（一条）：

> - `SF-2025-META-SAM-AUDIO` — Daily `2025-12-17`补Dec16；[原Dec16研究披露](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)与后Dec19 [2512.18099v1](https://arxiv.org/pdf/2512.18099v1)必要§3.1–3.4/5.2–5.4/7.3–7.4/7.8.1/D.1–D.3分责，2+2+2=6。只采混合音的语义/视觉/时间条件限定与结果分验，后稿联合latent/反侧是补证，不声称Dec16已公开完整25Hz/drop/AED/SAJ recipe或与官网PDF同bytes。span/器乐反退、judge非真值/严格波形加和未证及全费用近文；未核全部实现、权重、听测或复现。Newton§13必要Source/当前唯一Ch24 gap通过；逐字PRE、实际写入与POST尚未发生。

## 4. PE-AV唯一Ch23一自然段与本人末注逐字PRE（未写Books）

Newton§13已actual通过5分/后稿必要采用权限及唯一Ch23 gap；root实际读934–970邻接，准许准备未授锁。准确前锚点是原多目标公式后完整段“权重不是纯训练超参数，它定义模型优先保留什么信息。某种benchmark的提升不能证明representation在所有下游任务上更完整。”；准确后锚点是“对齐从两种扩展到多种模态时，联合critic还会改变单个错误的传播路径”完整段。只插其间一自然段，不改公式、权重原段或joint critic分支。

拟逐字正文（一自然段）：

> 帧级对齐还要把目标权重落实到实际训练人口，而不是只给已有全局embedding加时间戳。统一音视频表示可以先学习跨样本匹配，再以局部与全局活动目标适配帧级读出；但强调边界不等于更少误报。[PE-AV原披露](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)给出统一表示到帧级目标的路线，后续[精确v1](https://arxiv.org/pdf/2512.19687v1)的local/global采样对照显示，提高local目标采样可改善边界相关指标，同时损害惩罚false-positive的指标。这只支持所测活动任务的监督竞争，不把某个默认采样率授为通用最佳，也不把更多caption、pair或数据的均值当各组件独立因果。训练目标/采样人口、encoder版本与帧级consumer应一起保存，边界、漏检、误报和全局检索分别验收；caption制备、额外适配和逐帧读出都有费用。局部标签不可靠、误报或原检索回归时，保留原全局表示、较保守的目标混合和专用时序检测，不由一个定位指标签发连续事件判断。<!-- source-family:SF-2025-META-PE-AV -->

拟本人末Review note（一条）：

> - `SF-2025-META-PE-AV` — Daily `2025-12-17`补Dec16；[原Dec16研究披露](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)及后Dec22 [2512.19687v1](https://arxiv.org/pdf/2512.19687v1)必要§2–3/§4.3 Tables6–10/§5.1 Fig12/D.2 Table19分责，2+1+2=5。只采帧级local/global监督人口与边界/误报分验；后稿具体采样竞争和反侧是补证，不称Dec16公开完整recipe、十pair同阶段或原PDF同bytes。保base/100k/batch800与完整模型分责、比例/规模非单调、all_gather不授配置无关性能及全费；未核实现或复现。Newton§13必要Source/当前唯一Ch23 gap通过；逐字PRE、实际写入与POST尚未发生。

两项均各一段＋自身一注，供Newton逐字PRE/root具体锁协调；未获锁不得写Ch23/24，提案不代真实POST或DAY。

## 5. root分别窄锁后SAM/PE实际保存 / POST待核

Newton§15已逐字PRE通过；rootactual三PRE/完整邻接与版本权限后，ROOT_ADMISSION_REVIEW末三项写前批准分别授Ch24/SAM§3与Ch23/PE§4各一正文自然段＋自身一末note。写前本人actual三文件cached/unstaged numstat均空，保护后到并发；依次apply_patch，原ASR/semantic-binding marker/语音段、原公式权重段/joint critic及他注未变，Draft不改、无新标题。

**SAM**：已严格按§3逐字插Ch24当前L886，marker之前；实存后完整顺读878–906与本人末注/前注，保原识别→分离→speech完整衔接，后稿角色/反退与所有近文边界同PRE。**PE-AV**：已严格按§4逐字插Ch23当前L952，权重完整段后/joint critic前；实存后完整顺读934–960与本人末注/前注，后稿采样竞争/相反指标/消费分验与退路同PRE。各文件仅4新增0删、限定diff-check通过。自身notes只将审批/实际保存行政状态更新为已发生，没有更改必要读域/5或6分/禁止外推边界。

请Newton分别读取实际全文新增、完整两侧和本人note后做真实POST，root实际回读才分别接纳/释放；本节只是writer实写/自读，不是nonwriter POST或DAY。现两窄锁未自行释放、不再改正文或他注，不写State/index/独核，不stagecommitpush。

## 6. 已发生Newton18/root两项实际接纳释放 / 各本人note行政同步

actual读Newton§18分别Ch24/SAM与Ch23/PE完整实际正文/两侧/ownnote POST，以及root末逐书实际接纳释放节。root已实际逐书读回并接纳释放两窄锁；本作者仅按用户转交同步各自身末note的已发生Newton18/root读回接纳释放状态，正文、原marker与他注不再改。分别actual读回两末本人注，限定diff-check通过。两family各实际整合1，配MiMo/Alignment本日实际整合4；当前无本作者Books锁，不重Source/PRE，不授DAY或完成态FINAL。本人注行政差额供root读回即可，不再第三审方法。
