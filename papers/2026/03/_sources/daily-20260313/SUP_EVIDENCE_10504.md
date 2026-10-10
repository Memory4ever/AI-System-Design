# 10504 必要 Source / 评分 / Ch72 差额与 PRE 提案

准备者 mar13_admission_review；唯一范围 2026-03-13 Daily 补充 2026-03-12 北京时间自然日。仅准备本单项，待 root 非准备者实际复核，不自授独立 Source / Books 验收、实际 POST 或 DAY；不写 Report、Books、State 或共享 ledger。

## 身份、日期与实际证据

Naïve Exposure of Generative AI Capabilities Undermines Deepfake Detection，Sunpill Kim、Chanwoo Hwang、Minsu Kim、Jae Hong Seo；arXiv:2603.10504v1。重新完整读同日本项 SUP_ABS3_10504.txt；既有贡献校准见 SUP_INDEPENDENT_REVIEW_20261009.md 396–400，Mar12 arXiv 事件日级夹证见其 515，原日期与准入有效复用。Submitted March11 07:58:38 UTC 不是公开证据，不搬日期或扩窗口。

本次官方 exact-v1 HTML GET 200、490307 bytes、最终 URL https://arxiv.org/html/2603.10504v1，保存 SUP_CORE_10504.raw 与机械 HTMLParser 投影 SUP_CORE_10504.txt。当前 exact-v1 abs 再 GET 200、42667 bytes，保存 SUP_CURRENT_10504_ABS.raw；标题 / 四作者 / 唯一 v1 history 一致，无可见撤回 / 纠错 / 具名先稿或重要修改说明，不认证全网无先稿。HTTP 结果及实测文件时间分别见 SUP_CORE_10504_MANIFEST_RESULT.json；checking time 不是公开时刻。两次 bs4 不可用后改标准库投影，不安装依赖、不改变原件；原 HTML 表格按实际 cells / rowspan 另核。

启动重读当前 AGENTS、Research / Report 合同、统一 Prompt、Sources 使用说明和 Daily / arXiv 范围、ROADMAP 与本日停点。实际必要阅读：§3 全部（投影 134–230），§4 引言与 4.1（231–250），§5.1 / Tables 1–2 / 指标及 §5.2 方法界面开头（288–403），§5.3.1–4 / Tables 4–6（原件 S5.T4.2 / S5.T5.2 / S5.T6.2；投影必要主文 718–725、1020–1057），§6.1–5 限制 / §7 及 Ethical Considerations 的 no-human-study 范围（1111–1185），Appendix B.1–4 / Tables 8–11 及 C（1754–1862）。未读 Appendix A 操作提示、D 图像例、全部引用、代码、图3/5像素或任何旧版；不认证图形中精确 IPR / 全图画质 / 复现，不复述规避操作提示。支持及直接反侧已足以支持下列窄提案。

## 原判断 → 实际增量 → 需要重新考虑的选择

真实性检测只把某一 generator 的静态痕迹或单次无害请求当评价边界 → 稿内有限实验显示用户可把服务公开的真实性解释跨接口用于图像再编辑，下游不同检测器的反应随生成器、编辑条件和阈值改变 → 不能让单次内容审核或较自然的输出继承为派生媒体的来源证书；发布解释与派生 artifact 的 threat / evidence 边界须分账。

这是公开 capability 的交互边界和有限反证，不是新的图像攻击算法（§4 明确不提出新算法），也不把泛化 feedback-oracle 或 regeneration 成熟原则计作新增。不因安全标签或能映射 Ch72 准入。

## 必要设计 / 评价 / 直接反侧

- §3.1 的 criteria 是模型给出的自然语言视觉启发式，而不是 detector logits、内部真实规则或 ground truth。§4.1 明确解释的重用需要人做 recontextualization；不能称已验证全自动攻击或对“非专家群体”有用户实验。§3.3 的 benign 只限定请求 framing，不认证最终用途合法；偶发输出拒绝 <5% 是定性观察，底层过滤 / 采样原因未核。
- §5.1 的商业实验实际用 stateless official API，而不是持续 web conversation。稿内报告 IDs 为 gpt-image-1.5、gemini-3-pro-image-preview、flux-2-max；Qwen 两 image-edit 版本作为有限开源对照。Table 1 的 release / 单图价格仅作者记录，不独立认证现价、免费算力或模型内部身份；主文 Imagen 3 叙述与实际 Gemini API ID 不合并为一个已经核验的架构。
- 起始样本为 FF++ 五类各 20 张，共 100；阈值用独立来源 FFHQ 的 1000 张真实图经验校准。τ99 / τ90 分别对应该参考集 1% / 10% false DR，不是任意部署真实流量的误报保证；变换图不等于与原 FF++ 图同分布，不能照录 §5.3.1 的“eliminating distribution shift”。不同 generator、prompt、API 预算、输出分辨率等未作完整等成本 / 等质量隔离，未报告此结果的重复运行区间。
- DR 是 fake / generated 样本被相应 detector 判 positive 的比例，不是“真实率”或安全成功概率。多数 GenD / Hive-DF 的局部 DR 确实下降；但 AI-generated detector 对重构的响应可能上升，不能一概说 detector 失效。Table 4 的 Qwen-v2 deepfake average 在 P4 为 2/16（τ99/τ90），P5 反升 13/45；细化非单调改善。Table 5 的 Gemini D3 在 P5 为 4/30、ISP P6 为 25/59，Hive-AI 为 3/63→9/73；直接反驳 ISP 对所有 detector 更强。普通固定编辑的部分 DR 已很低，不能将全部收益唯一归因于解释重用或内部 alignment。
- Table 5 的若干 aggregate 与逐行数值不符，例如 Flux P4 的 AI-detector 行为 24/57、26/38、51/90，而标示 average 为 32/31；原件列对齐已核。不采用该精确平均或“商业服务普遍更危险”的总排序；有限单项 / 配置反侧不据此全盘否定。Table 6 的非面部生成图是另一人口，不与 100 张面部 DR 合并。
- IPR 是 AWS CompareFaces 的原图—派生图配对身份验证代理，不是所有 pose / expression / 原图语义真值；§5.3.3 本身明确 ChatGPT 有较大身份漂移、generic IAP 比 ISP 稍保身份。App C 更换 Tencent backend 报告相近趋势（图注明 default 50），不能认证未知身份、跨 API 校准等价或全部部署身份保持。未读取图3/5精确值，不补造精确 IPR。画质改善主要为定性观察，不授独立盲化人评或 matched perceptual quality 因果。
- App B 使用默认 OpenAI moderation 的 standalone text 和 Azure text / image 分开评测，未测生成服务全部内部 guardrails。四类文字不 flagged / severity0，以及原100图多数 severity0，只说明这些 harm taxonomy 未将该组合风险定义为相应类别，不能把“未报风险”称 moderation 本职任务失败或生产开放风险已完整测试。Azure 少数图 severity2 的直接反侧保留。
- §6.4 讨论限制编辑、detector gate、watermark 等的效用 / 漂移压力，未实证这些 mitigation 有效；本文不提供完整防线。检测、生成、解释调用、配对身份测量及敏感数据留档都有成本；硬件 / precision、并发、总调用预算、全部失败尝试和端到端 SLO 未披露。人审或来源凭证需求为本包工程推断，不冒充作者已验证实现。

## 评分、深度与实际 owner 差额

拟 **Design 2 + Reach 2 + Durability 2 = 6**。Design 是公开真实性解释与派生图像检验之间的受限 threat 变化，而非新 editing 算法；Reach 是 assessment 接口 / 外部编辑 / 下游 authenticity 边界，非因为评测多个模型抬分；Durability 是检测、身份代理、内容审核与 provenance 分责。标准机制 / 对照 / 代价已核，对拟采用的安全边界和长期差额定点深入，未扩全稿。仅准备者提案，root可据真实差额改判。

Owner 为 ROADMAP 的 PLATFORM-SECURITY / Ch72。实际顺读 Ch72 193–218 完整水印 / 派生图像 / 取证邻接，244–277 detector sensor 边界，735–763 goal alignment / Deny 局部；Ch71 / Ch73 1–25 职责入口及 Ch66 196–204 来源真值交接。

- Ch72 209 已有 regeneration transformation class、proxy 非来源真值及派生 artifact / detector identity，但证据是水印信号持久性，未具体讨论正常真实性解释的外部重用与不同深伪 / synthesis detector 相反响应。
- Deny 754–758 已有拒绝反馈 oracle，但依赖 monitor denial、temporal edge 和 provenance；不能把正常 assessment 返回的结构化解释等同为 denied transition，也不能据该原机制声称已经防止媒体再编辑组合风险。
- 250–273 的 policy-bound sensor 与 Ch66 authoritative provenance 承载测量 / 真值的一般纪律，只作交接，不在那里重复新安全论证。Ch71 持租户隔离，Ch73 持发布合同，不成为第二 owner。

拟在 Ch72 当前 209 的完整 regeneration 段之后、下一“当输入与密钥独立…”段之前加入以下两段；保留原水印机制及低成本旧方案，不改现有文字。若 root 核认为此具体组合已充分承载，可以据实际正文 NC；不因同主题默认 NC，不因重读耗时降分。

## 逐字 PRE（待非准备者核）

真实性解释的释放还会改变下游媒体检验的威胁边界。一次图像分析可以给出与判断一致的可读理由，但这种一致性不证明理由就是检测器内部真实规则；正常返回的解释又可能被接收者在另一个编辑接口中重用，使派生图像更自然而改变原检测信号。因此，assessment 输出、外部编辑服务、派生 artifact 与最终 detector 应各自绑定版本和可见权限，单次内容审核通过不能签发派生媒体的来源证书。这与后文的 denial-feedback oracle 不同：这里不需要 monitor 拒绝事件，而是正常功能输出的组合用途。[必要交互与反侧](https://arxiv.org/html/2603.10504v1)支持该受限边界，不证明完整自动攻击、真实用户群体风险或已找到有效防线。<!-- source-family:SF-2026-ARXIV-2603-10504 -->

测量时应分别报告 manipulation detector、AI-generated detector、固定真实参考集下的 operating point，以及原图—派生图配对身份代理，不能把较低 detection rate、face API 同人判断或更好的画质合成“真实且安全”。所测一百张面部样本中，一类检测器的响应下降时另一类可以上升，细化或重用解释也不是单调收益，部分模型仍有身份漂移；这些结果不支持所有商业服务比开源更危险或原图完整语义保持。对 assessment 解释的披露粒度及组合变换作独立复测，是据此推导的工程要求，不是作者验证过的 mitigation。解释、生成、双类检测、身份配对和敏感 artifact 留档均付费，API 更新后需重新校准；威胁人口或来源证据不可核时保留 Unknown、签名 origin / 制品血缘和人工取证，不因 detector 未命中或内容过滤未告警自签 authenticity。<!-- source-family:SF-2026-ARXIV-2603-10504 -->

## 本包停点

必要支持与直接反側已足，拟受限整合两段、其余强主张隔离。下一仅 root 非准备者核必要原件 / 具体 owner / 评分 / 上述 PRE；若通过才写实际 Book，再由非 writer POST。未修改共享正文、报告、日期、旧评分或 checkpoint，不授独立通过 / 整日完成。
