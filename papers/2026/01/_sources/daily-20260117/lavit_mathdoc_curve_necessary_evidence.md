# LaViT / MathDoc / CURVE 必要证据提案

终裁：root实际核三项精确v1方法/评价/直接反侧缓存，分别6标准Only、5标准Only、5标准Only通过。Formal同步90/105、15普通。无新Books；以下保留必要证据及原提案。

三项精确 v1、日期和准入已 root 校准，本包仅必要方法、关键评价与直接反侧；不重开宽列表，不授实际复现。拟 10129 6标准、10104/10649 5标准完成 OnlyReport，均不冒精确 Existing、不以 recipe 缺失造长期 gap。待 root 实际源终裁。

## 10129 LaViT

精确[原文](https://arxiv.org/html/2601.10129v1) §3/4.1–4.3 Eq2–8/§5.1/5.4 Table3/A2，缓存 method/eval/setup-necessary.txt。原白盒视觉 reasoning 监督与 student 文本捷径约束→teacher32B attention trajectory 与 query-conditioned visual semantic 对齐、学生4个 AR latent token、逐步放开 image path→值得比较纯文本 CoT/始终可视与 latent 中间读出训练。15K 样本须 GT 正确、text-only 难、Visual-CoT bbox attention≥20%；layer/head 汇总 attention 与 MinMax/Top8 不是真 gaze/cognition 或消除 hallucination 的认证。Pilot 正误 attention 相关不证明必要条件或因果。

学生 Qwen2.5-VL-3B、teacher32B、ViT frozen/LLM FT、1000 steps（400 sensorygate warmup+600 fully visible）、AdamW LR5e-6、perdevice batch16/accum1/λ.3/maxpixel1003520。Phase1 γ=1e-6 起非严格零，logγ bias 与 Eq8近似梯度不能证明精确比例；部署 fullyvisible不证明零 distribution shift。hardware/precision/GPU数及 teacher 数据构造完整成本 Not Disclosed。MMVP/BLINK 等 task局部 ablation：remove trajectories/semantic 多项下降；hard switch w/o gate在 Relative Reflectance 48.51高于full45.52，w/o latent在该项81.12高于45.52且Spatial25.33远低81.82。表与概括的“均essential/全面下降”不完全一致，不能把 latent masking=普遍 reliance、progressive=防shortcut因果。白盒监督/选择人口/额外latent训练是局部条件，非已证通用 cognition机制或长期必须替代旧SFT；拟Only，无新Books。

## 10104 MathDoc

精确[原文](https://arxiv.org/html/2601.10104v1) §3.1–3.3/4.2.3–4.2.4 Eq8–10/5.1–5.2 Eq11–15/A2，缓存 standard/eval-necessary.txt。从30000真实试卷选460困难多栏/遮挡/破损图，专家逐字符审核 Qwen3VL-Plus preannotation+type-specific unrecognizable placeholder+peer/senior adjudication；2169 Choice/758Fill/682Solve，673不可识别。图文 extraction 高并不等于合理拒答→单独 refusal positive P/R/F1 与全文 silence/explicit/cropped 行为交叉→改变文档验收需区分漏提取与拒答。最终文字Lev/图像Qwen3VLPlus judge/refusal平均混合，emptyoutput算implicitrefusal存在漏题混杂，不认证安全授权。

50裁题 erasure 文本密度 η 与50%refusal threshold（30B20%、8B40%）是协议相关，不能归因模型容量或训练负样本缺失；110不可读题 fullpage三行为、cropped二行为定义 Rfail/mitigation/active，1.82%是Qwen8B该人口的两模式主动拒答，裁剪同时改变上下文/分辨率/漏题机会，不能采用“已严格证明触发 uncertainty”。A2仅 judge 定指令语义一致案例，不独立公平性或真值验证；API/开源混合，hardware/precision/完整decode设定 Not Disclosed，无复现。保留具体提取/refusal评价盲区实例，不授跨文档可靠拒答定律，拟Only，无新Books。

## 10649 CURVE

精确[原文](https://arxiv.org/html/2601.10649v1) §3.2/4.1/5.1–5.3/6/C2/D3，缓存 method/counter-necessary.txt。540长视频2400题18locale的数量不计增量；本地curator/auditor平均5、10% calibration、50%continuousaudit另50% independent answering。文化知识/视听识别混合约束→native视频多帧题与 human-trace evidence graph、corrective hint迭代分离失败→暴露翻译成英语不充分及“最终答案错=单一感知错”的评价盲区。human pool可WEB不得LLM而model固定输入，95.22vs45.07不能公平资源/文化成因归因；thinking/framebudget/AV增益均局部。

Graph由 LLM 把 human trace拆timestamp视觉事实/外部知识/逻辑并判prerequisite边，不是因果groundtruth。遇 valid alternate path称divergence后停止该支，hint提供failednode正确证据并prune再问；六locale误差分析仅490/524 of878，Gemini2.5Pro pipeline，5轮hint解99.7不等unassisted能力。三次samejudge97.7agreement不等真值；60条人工88.5%是小验证。固定视频翻5语言native多数好但source/target方向不一，不证pretraining cause；作者承认culture/perception难分。必要预算与模型协议局部，hardware/precision全文负载 Not Disclosed。不采用因果taxonomy或生产持续闭环，只报告该评价协议的混杂与受限诊断实例，拟Only，无新Books。
