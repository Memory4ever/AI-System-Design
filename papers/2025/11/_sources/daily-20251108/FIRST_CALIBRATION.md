# 2025-11-08 首批准入校准请求

作者：Noether。窗口：`[2025-11-07T09:00:00+08:00, 2025-11-08T09:00:00+08:00)`。本包仅请求方向及代表性排除校准，不请求授日期、Evidence、Books或日级完成。没有写Books；08普通来源尾项和其他含糊相关题摘继续处理。

## 拟继续的方向

以下六篇已实际读完整题摘，原始全文题摘保留在本日Atom原响应，不把字段`published`当首次公开时刻。API查询与有限停止详见[来源执行记录](./SOURCE_EXECUTION.md)。全部为v1，当前轻量撤回/纠错检查及官方公开批次日期仍待本日必要核验。评分是准入通过后的暂拟投入，不用于倒推准入。

| 身份与原文 | 原始字段与原始题摘 | 具体准入命题及待校准点 | 暂拟评分 / owner方向 |
| --- | --- | --- | --- |
| [DartQuant: Efficient Rotational Distribution Calibration for LLM Quantization](https://arxiv.org/abs/2511.04063v1) | `published=updated=2025-11-06T05:05:24Z`；[runtime原响应](./arxiv-runtime-agent-page0.xml)该ID完整summary | 端到端旋转微调昂贵且依赖任务损失 → 约束旋转后激活分布并用QR-Orth校准 → 可改变旋转校准的预算/过拟合取舍。47x/10x是作者旋转优化声明，不是端到端推理加速。NeurIPS条目触发精确首次公开/同家族核验。 | 2+1+2=5；INFER-TENSORRT-LLM的通用量化校准机制，不因框架名路由 |
| [Block Rotation is All You Need for MXFP4 Quantization](https://arxiv.org/abs/2511.04214v1) | `published=updated=2025-11-06T09:22:31Z`；[runtime原响应](./arxiv-runtime-agent-page0.xml)完整summary | INT4旋转去outlier经验 → MXFP4 PoT块缩放与全局重分配outlier能量冲突，提出块内旋转 → 需重考虑旋转/量化格式的兼容边界。属于实际设计反侧，后续核块划分、对照与质量条件。 | 3+1+2=6；INFER-TENSORRT-LLM通用低精度表示/校准；反证需加深相关部分 |
| [Tortoise and Hare Guidance: Accelerating Diffusion Model Inference with Multirate Integration](https://arxiv.org/abs/2511.04117v1) | `published=updated=2025-11-06T07:08:58Z`；[multimodal原响应](./arxiv-multimodal-page0.xml)完整summary | CFG两个分支相同求值频率 → guidance项数值误差敏感性较低的分析及粗细网格积分 → 可改变指导项求值预算/质量取舍。NFE减少不自动等于实际wall time；核误差假设与ΔImageReward条件。 | 2+2+2=6；MULTIMODAL-GENERATIVE-PARADIGMS；NeurIPS触发精确公开事件核验 |
| [REMIND: Input Loss Landscapes Reveal Residual Memorization in Post-Unlearning LLMs](https://arxiv.org/abs/2511.04228v1) | `published=updated=2025-11-06T09:58:19Z`；[runtime原响应](./arxiv-runtime-agent-page0.xml)完整summary | 单点forget评价 → 输入邻域扰动loss形状检测残留影响 → 可修正forget验证的盲点。摘要称query-based不等于只需自然语言输出；后续核loss访问权限、样本/对照及是否能区分原始记忆与泛化。 | 2+2+2=6；PLATFORM-EVALUATION-SYSTEM；隐私/安全必要反侧不取消 |
| [Black-Box Guardrail Reverse-engineering Attack](https://arxiv.org/abs/2511.04215v1) | `published=updated=2025-11-06T09:24:49Z`；[formation原响应](./arxiv-formation-page0.xml)完整summary | 拒绝边界可被观察 → 输入输出采集、divergence优先遗传变异与替代策略拟合 → 可改变guard部署的可提取性认识。rule匹配>0.92不自动是绕过率或安全策略全部恢复；$85需核query/model/protocol条件。 | 2+2+2=6；PLATFORM-SECURITY；必要安全证据后续定点核 |
| [Direct Semantic Communication Between Large Language Models via Vector Translation](https://arxiv.org/abs/2511.03945v1) | `published=updated=2025-11-06T00:43:29Z`；[runtime原响应](./arxiv-runtime-agent-page0.xml)完整summary | 文本消息丢失内部表示 → 双encoder翻译Llama2/Mistral空间并30%混合注入 → 潜在跨模型表示通信路径。cosine=0.538、logit稳定不能直接证明消息语义保真、任务收益或成本减少；若只剩这些代理指标，收窄为局部可行性而非协作runtime保证。 | 2+1+2=5；AGENT-MULTI-AGENT消费模型表示桥，唯一owner待证据后决定，不申请结构章 |

另有Google [Introducing Nested Learning: A new ML paradigm for continual learning](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/)，已读完整核心说明：[本日原blog](./nov08-first-directions-raw.txt)。原字段`November 7, 2025`、未披露时区/时刻。其把独立架构/优化设计改为不同context flow和更新频率的嵌套问题；CMS多频记忆与self-modifying Hope有潜在具体机制，不因神经科学类比准入，不采用无限学习/完全避免遗忘宣传。官方指向[作者52页PDF](https://abehrouz.github.io/files/NL.pdf)，完整题摘已读在[原响应](./nov08-nested-paper.txt)，但此URL无精确历史版本，不将当前PDF实验直接视作11月7日版本。NeurIPS/OpenReview家族首次公开与本窗blog差额仍需核；[forum实际challenge](./nov08-nested-openreview.txt)，官方API403、blog直连超时已有限尝试。准入校准可先判断具体机制方向，不授当窗新事件。Booksowner候选是MODEL-LONG-CONTEXT / TRAIN-PRETRAINING的模型内参数更新，不是Agent外部记忆；未读owner上下文前不宣称知识缺口。

## 代表性排除

1. [Kimi开放平台：新功能发布记录](https://platform.kimi.com/blog/posts/changelog)：[完整实际核心](./nov08-detail-1.txt)。页面标题日期2025年11月07日，但最近事件段明确2025年11月6日，内容只有Thinking/turbo发布、默认TPM提升与价格下降。没有披露TPM调度/限制机制、兼容性、安全新差额，不因页面次日汇总新增研究候选，也不把榜首或价格当runtime保证。不是已证明该家族全文无贡献，只关闭此汇总事件；不需为贡献已关闭项再恢复时刻。
2. [欢迎在LMArena上测试ERNIE-5.0-Preview-1022！](https://ernie.baidu.com/blog/zh/posts/ernie-5.0-preview-1022-release-on-lmarena/)：[完整核心说明](./nov08-nested-paper.txt)，原日期2025年11月7日。只有并列文本榜第二和将于近期正式发布，不披露架构/训练/成本/评价盲点/新控制机制。明确关闭此榜单消息，不把即将发布当实际release；不等于未发布模型永无价值。
3. 官方cs.CL宽月表[原始25标题](./nov08-detail-1.txt)是11月首段而非08公告批次；仅入口纠错线索，不送整月1527条题摘队列。发现00115撤回评论，但当前不从其他日期候选反推08；若08原检索出现该事件才定点处理。

## 独立核验请求与精确停点

- 请root独立核上述七方向及两篇代表性排除的原题摘/核心说明；不必重读未相关附件。
- 普通：14每日入口动态历史恢复仍有尾项，formation查询total114仅取首100，已标记偏宽并停止翻到100；需更窄训练/结构主题补检，不能把114命中改为全类全文队列。runtime70、multimodal26原返回已取尽；跨查询去重/其他含糊条目的有限准入仍未完成。
- 日期：六论文API字段只是提交元数据，需本日官方公告或真正首次公开上下界。Google blog日期缺timezone/时刻，会议家族也可能早公开；以原字段保留，不先列正式候选，不重复盲查空接口。
- 已准备好方向项与普通未读分离；校准前继续无关来源初筛。无Books请求、无本日独立验收。
