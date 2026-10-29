# Nov21 五最小门与一个设计反侧

作者Noether；2026-10-15T18:04:00+08:00。普通五门实际必要原段读完，提案5窄P，不是正式当窗/Evidence/评分。真实非作者Ohm9/10已核Sleeper受限潜力/数值反侧及首批部分原域；未重复全部方法，现请root转Ohm核其余具体决定。

## 1. FLARE 16450v1：M→P

[本轮精确HTML](SUP_CORE_FLARE_20261015.html)实际§I/II-B–D/III、IV-B/TableIII/V（投影正文22–33/44–84/99–105）。旧SFM按1MB传输虽绕gRPC2GB，端点仍需全对象reassembly；新增ObjectStreamer container逐item序列化，file逐chunk读，使额外发送内存分别绑定最大item或文件chunk，而非整个dict。四filter位置中出站量化、入站反量化，aggregation/local training仍原precision，不能把wire precision当训练精度。这是真实serializer/consumer边界变化，不是把量化/streaming两个名词并接。

保single-client/site/1B与只一次globalweight本地模拟；file 170s对regular47s的I/O反退、累计多轮quantization/nonIID与SecureAgg/DP兼容未测，不授“industry deployment ready”。潜在选择改变是传输分片成功不自动解除对象重组峰值；只此机制P，不全实验/实现验收。原artifact版NVFlare2.6.0事实不当本日release，当前仍必要论文公开/修订资格。

## 2. Sleeper 15992v1：M→受限P

[精确HTML](SUP_CORE_SLEEPER_20261015.html)实际§3.2–3.6/4.1–4.3/5.3；Ohm9同必要域真实独核可复用。safe-mode centroid/z-score与known-answer canary最大相似度用OR消费，对已知trigger/单8B生成的固定恶意目标提供不改weights的局部monitor分支。不是成熟SBERT/OR本身新颖；保留的是在该明确trigger/prompt人口上两类观察量作为外部后门检测线索的受限实验潜力，未授独立safe-state真值/部署充分性或机制归因。因为数值口径争议而收窄效果，不自动把潜力当C。

必要反侧不新造：40=20safe/20trigger，原TN17/FP0/FN3/TP20合40但positive23，其recall与表85%/3of20不一致；z门0.9和mu.110/sigma.026下raw.23不等价。只记原评价/阈值矛盾，不授复现、造假或真实实现错误。canary可被保真绕过、safe baseline采集/两canary额外调用费用、合法分布漂移与未知trigger未核；不采数字/recipe/zeroFP/first practical。若未来正面采用效果，需同原protocol的heldout/threshold与表澄清；当前日期未定不扩全部实验/代码。

## 3. CD-DPO 15767v1：M→窄P

[精确HTML](SUP_CORE_2511.15767_20261015.html)实际§II-C/D Eq1–2及相邻gradient，正文55–67：不只是coverage平均分排序，beta*=beta*f(sp−snp)进入pair logits及gradient，来源是code/branch/functional均值、compilable/failed和bothfail剔除人口。它改变pair-dependent更新强度，而非标准DPO换硬件数据就准入；potential是quantitative margin进入偏好消费。f只说递增未给完整recipe，不能授通用易pair必更大更新、stable/dataefficient或coverage=功能正确；simulator/生成双温/筛选费用保留，不读全CVDP实验。`TRAIN-DPO`方向，必要日期仍未定。

## 4. SHAP-guided 16132v1：M→窄P

[精确HTML](SUP_CORE_2511.16132_20261015.html)实际Methods/Setup/Results/Data-regimes/Linguistic analysis，正文46–79。seed classifier的SHAP筛TF-IDF情绪差分词，正负关键词＋真实exemplar约束生成；naive分支保相同exemplar/管线、去关键词。原100/500/1000seed及递增设置给出指导依赖seed、低seed收益失灵与下游分类效用/词汇多样性不同轴的具体条件，非单纯emotion应用榜值或responsible标签。局部合成数据选择/评价边界可改变`TRAIN-DATA`解释，P。

不把XGBoost/TweetEval结论当foundation预训练普效或公平证明；TTR长度依赖、交叉验证/holdout措辞和生成调用预算未全闭合，不采精确F1/阈值、SHAP因果真值或最少真实样本保证。只准入必要域，不扩所有生成附件。

## 5. LDAG 16435v1：M→窄P

[精确HTML](SUP_CORE_2511.16435_20261015.html)实际§3.2–3.5/Eq1–9及§4.4/Table8（正文55–93/114–130）：class属性文本的CLIP softmax-GradCAM产生pixel prior，support前/背景prototype参与attribute projection/InfoNCE；不是LLM描述+SAM名称即准入。最具体局部反侧是删support时PASCAL下降/COCO改善，因此“support图是必要参考”不能由few-shot任务名取得；保持class list/LLM语义额外先验，不授zero-shot无先验或无训练。Table4/5引用不齐、frozen encoder/decoder与adapter可学对象、alpha/n搜索/LLM费用不混，数字只定位不采用普效。`MULTIMODAL-REPRESENTATION`方向P，不扩全数据集比较。

## 6. 16655v1作者回应与设计反证采用权限

[精确HTML](SUP_CORE_2511.16655_20261015.html)实际§2–5/Limits/AppA；正文43–78/114–116。NoSense是contrastive encoder+top-k帧/查询检索，不是绝对“无memory”；VSC重复相同10min片段保持unique count，同时增加视频时长，原称同比长原视频可区分长度。必要回应Nov20是被批评作者的邮件引文日期，不是本论文first-public：对方认可实验设置但争论VSR预期usage，强调看视频时query未知；承认VSC-repeat限制且原刻意不含revisit，不能将此争论裁成所有world model无效或唯一因果已证。原作者回应是论文转录非独立验证，NoSense raw/basic prompt退步与仍高分都保留。

可保留benchmark/allowed-information/invariance分责的设计反侧潜力，不拟采用95%/0%全域能力结论、未验证replacement benchmark或所有模型陷shortcut。若正式采用VSR对比，query可得时点必须对齐；本日未定公开资格，暂不写Books。五门若Ohm实际通过，首33题摘由27P5M1C归并为32P1C；仅提案算式，不作独核或Evidence证明。
