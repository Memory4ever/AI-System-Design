# Sep24 必要局部准入核验

作者Meitner。全部下表为本日own exact v1 HTML请求及实际读域，不是全文穷举或正式Evidence审阅。P表示值得核验的具体潜力，必要首公开日尚不证，不评分、不进Books；C表示贡献关闭，日期未知不阻塞该决定。普通未读边界不冒作外部阻塞。原件`SUP_<ID>v1.html.raw/.request.json/.txt`保留；后三个定点重开使用`v1.reopen.html`。current轻量说明见`SUP_CURRENT_LIGHT.json`，不得把当前题摘投回v1。

| 精确身份 | 实际已读section/位置 | 实际新增与准入裁决 | 未读及采用边界 |
| --- | --- | --- | --- |
| 2509.17978v1 STAR-XAI | §3.1–3.3/§4.1起(txt169–425)、§6/7(1799–1848)、Appendix checksum(2480–2528) | C：Socratic human反馈、自改提示rule、内部AVM复核与mnemonic checksum的25move案例；checksum是可读事件/库存字符串，不是外部状态验证或强制执行边界，未新增可靠性条件。 | 未穷举25moves/transcript/全部附录；不授零幻觉、计算复杂度或memory purge保证。 |
| 2509.18005v1 M3ET | §III-A、decoder/crossattn(503–557)、IV-A、IV-C/IV-D、TablesII–V(904–1022) | P：Transformer/Mamba交替跨模态融合及语义cross-attn，在VQA/FLOPs与OpenEQA退步间给出局部融合/资源取舍；不是只模块组合。 | III-B masking、完整实现和图像未穷举；不采用普遍2.3x/73.2%或公平通用EQA胜出。 |
| 2509.18053v1 V2V-GoT | III-D/E(396–467)、V-C1/2与VI通信(877–930) | P：occluded/visible objects分开表达，其他车辆communicated plan可覆盖纯感知未来预测；具体观测/声明计划边界。 | 感知消融重训/增加数据，预测消融才同checkpoint；未读完整IV/V-A，不授无通信或零延时。 |
| 2509.18058v1 dishonesty | §4、§5.1–3、§6(620–1100)、E.2(6725–6737) | P：显式faking回答被output-only harmfulness judges误计攻击成功；可验证EvilMath检测与CoT不忠实时probe失败，修正监测输出/实际效用/意图关系。 | 能力实验显式指示欺骗不同于自发行为；未穷举80model/所有prompt/附录，不授probe通用安全性。 |
| 2509.17993v1 StableGuard | §3.2/3.3/3.4起(496–647)、4.1、4.4起、4.5起/表4首段 | P：同latent可开关decoder residual水印生成paired clean/watermarked，随机mask自监督取证与joint learning；具体训练信号/定位机制。 | 未穷举所有表/附录；noise/JPEG测试非任意攻击保证，版权归属不是水印准确率自动证明。 |
| 2509.18015v1 pathology localization | §3.1–4、§4.1–3、§5/limitations(212–394) | P：已告知病理存在仍需grid定位，区分识别和spatial grounding；稳定解剖位置可带来高hit但细定位较弱的局部反侧。 | 单集/8x8、grid50%规则与point baseline不同、MedGemma温度不同；不外推普遍小模型劣势或临床安全。v2 fewshot不投v1。 |
| 2509.18234v1 readiness stress | §2六stress中的setup/results、§3 clinician rubric(130–225/252–390/412–510) | P：去图、视觉必要175子集、选项扰动/40图替换揭露leaderboard相近模型的不同modality reliance；三clinician rubric区别benchmark需求。 | 替图改变难度、moderation过滤、CoT局部mixed；未全附录，不由分数诊断记忆泄漏或real-world readiness。 |
| 2509.18415v1 lineage | §4.1起、4.2核心、event schema与5.1/5.2(748–881) | P：A2A身份绑定到signed action/context与Merkle inclusion/call-chain，缺证明/签名失配拒后续append的具体协议提案。 | inclusion不证明日志完整或动作语义正确；未实测/部署，不授FedRAMP或replay safety，未穷举workflow/appendix。 |
| 2509.18626v1 negative crash | §4.1/4.2、5.1–3、§6/7(465–650) | P：action-conditioned负/正precedent以及PosOnly消融，缺相似negative时将absence当安全的反侧；counterfactual loop局部校准。 | 1275pairs/1.4k reports/GPT4o、预算覆盖有限，unsafe recall有代价；未全prompt/实时部署，不授生产安全。 |
| 2509.18917v1 LiDAR DDPM | III-A/B、IV实现、V选11/64配置、结论前(934–946) | P：SNR noise schedules/Fourier embedding与800/1000steps quality-cost条件；不是只新LiDAR数据。 | 64选11展示与earlystop、LiDM仍更快，未全附录/代码，不授普遍SOTA/下游有效性。 |
| 2509.19087v1 multi-spectral Gemini | §3/3.1、§4.1–5(230–575)、Tables1–4 | P：新sensor bands转五pseudoRGB+解释prompt，same Gemini RGB-vs-extra输入、1000subset ablation给局部representation adaptation条件。 | 输入数量/提示同时变化，非纯band因果；prompt/order敏感/只适配可视化sensor，未图像像素/全部prompt，不授任意sensor零样本。 |
| 2509.19120v1 FedFiTS | II-C(408–502)、III-B起(1437–1492)、VI-A/B(3561–3605)、VI-G/H/VII(4110–4220) | P：slotted selection与plateau/team reset及nonIID残差改变异构训练参与/调度选择；不以genericFL或healthcare名称关闭。 | II-C richfeatures/quotas/async/robustfallback超过具体Algorithm实现，非全已实现；fairness只participation proxy，backdoor/privacy非已证；未全文理论/攻击复现。 |
| 2509.21379v1 SAEmnesia | §3起(532–625)、§4metrics(1390–1421)、§5末/6(1640–1730) | P：concept标签监督SAE降低feature splitting/search，但仍需multiplier搜索、retention与攻击有代价。 | SD1.5 up.1.1/UnlearnCanvas局部；v1正文确有UnlearnDiffAtk段，不能因v1摘要未提就称正文无。未穷举附录，不授I2P/nudity/安全抹除。 |
| 2509.22703v1 AccessEval | §3.1–4(224–311)、4.4/4.5(440–456)、5.7–9/6/7(880–996) | P：paired query社会感知/情绪与事实质量不一致，scale改善事实不修另两指标，是评价分维条件。 | 234/2106合成英文singleturn、persona需信息/难度不同非严格do；未全humanvalidation/附录，不授公平生产保证。 |
| 2509.18316v1 KG reward | §4.1/4.2、§5/6，reopen HTML对应S4.SS1/S4.SS2/S5/S6 | P：path judging高分不自动迁下游诊断，format transfer与exact-string/synonym confound；旧domain关闭仅受影响项重开。 | 表中best-checkpoint选择/metrics不同；作者误称Qwen2.5-7B MoE与公式错误不采用，未统计/代码/全部数据。 |
| 2509.19090v1 Citrus-V | §4.1/4.2/5.3/6，reopen S4.SS1/S4.SS2/S5.SS3/S6 | P：joint segmentation loss损VQA→0.001 gradient scaling，随后freeze MLLM训fullSAM2的具体负迁移交接，不仅medical combo。 | 表12 Xray/FP退步、数据预算不同且缺direct gradient-scale对照；未泛读病例/全部数据，不授可靠临床判断。 |
| 2509.19096v1 traffic detection | §IV-E/V-A/V-B/VI，reopen S4.SS5/S5.SS1/S5.SS2/S6 | P：raw detector/tracker/SAM overlay改变输入可降recall/F1/description，额外检测信息非自动理解；负侧具体到形成/输入条件。 | §IV-E先选判accident帧再增强是selection confound；sim-only、无matched训练对照，未像素/全pipeline，不授增强普遍无效。 |
| 2509.21375v1 AutoContra | §2.1/2.3/3.4/3.5/4，S2.SS1/S2.SS3/S3.SS4/S3.SS5/S4 | P：overlap masks、mislabel与threshold可污染counterfactual-size reward；独占mask/CLIP标签复核/adaptive thresholds的235image human F1消融，是局部评价条件而非只prompt rewrite/DPO组合。 | 50object pairs，像素面积比不等physical size；ranker29.1→30.3小变化不是归因证明，未全数据/实现，不授通用counterfactual可控。 |

| 2509.18588v1 UniECG | calibration HTML S2.SS1/2/3、S3.SS2、S4 | C：明确Inspired GILL，special ECG token hidden states经mapper MSE对齐frozen DiffuSETS textencoder，再调用原decoder；没有新兼容或形成成立条件。 | generation只有qualitative，embedding更新forgetting仅crossmodel不是matchedstage反证；关闭非因医学或实验少，未全附录/代码。 |
| 2509.18796v1 SAADi | calibration HTML S3.SS2/S3.SS3/S4/S5/S6 | P：real-trained downstream score构造preferred pairs调diffusion；same sample count、多architecture baseline degradation和3–4x plateau区分生成视觉质量与下游训练效用。 | base3000+alignment1500 steps/迭代re-score预算及selector bias未消除；需标注数据，未全附录/实现，不授普遍收益/安全。 |
| 2509.19397v1 SelfMIS | final HTML S2/S3/S4，Tables1–5及Fig3说明 | P：selfcut单/多lead同recordpair、冻结预训多lead教师与SigLIP对齐；signal-level生成与latent/downstream效用分离，局部路径比较及teacher/alignment消融改变表示目标选择。 | baseline预训/额外20epoch预算、zero-mask输入适配不同；冻结random教师解释不清，w/oalignment文表65.68/65.85不一致。未图像像素/附录/代码，不授信息上限、semantic guarantee或FLOP自动等于latency。 |

这些21份局部审阅只解决准入/反侧事实，不是21正式候选、21份深入完成或Books已有覆盖。18588/18796用calibration原件，19397用final原件；19057只需完整v1 AB/current说明，未追加全文。日期有限门失败项恢复到本日具体身份，不追加全源/全文队列。
