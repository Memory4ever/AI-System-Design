# 11253 必要 Source / 具体 NC 提案

准备者 mar14_supplement；唯一范围03-14补充2026-03-13北京时间自然日，不授DAY。

## 身份、日期与实际读取

LLMs Can Infer Political Alignment from Online Conversations，六作者Byunghwee Lee、Sangyeon Kim、Filippo Menczer、Yong-Yeol Ahn、Haewoon Kwak、Jisun An。精确v1正文官方 https://arxiv.org/html/2603.11253v1，SUP_NARROW_LAST_MANIFEST_RESULT.json / SUP_NECESSARY_11253.raw/txt：GET200、417595 bytes、UTC2026-10-10T02:05:48.563515Z。完整v1 abs与十项独立日级日期包复用，v1 Submitted March11 19:26UTC不是公开证据；正常批次下界与official owning/findable注册上界已非准备者夹Mar13。abs显示v2 March13提交，但无具名重要修改说明，版本号不生成另一重要事件/分数，不比较全部版本。

实际题摘及必要主文II.1–2/B22–32、II.3–4/B33–44、部分词义相关解释B49–55、III限制B60–63、IV.1–3/B64–77、必要标签验证S1/B181–185、S4/B282–329完整过滤设计及TablesS4–S7已读。II.4后续相似度公式B78–91读过，但不授因果证明；S2仅B187–207局部baseline行，不称整S1/S2表或全部传统分类器已核。未读全部词表、18图像、提示模板、11附表、代码或复现；必要支持与反侧已足，不扩政治画像或定向影响策略。

## 问题 / 机制 / 反侧

原假设“内容不显式谈政治、没有PII字符串，就没有敏感属性泄漏”需要收窄：现成LLM对受选在线文本作二分类提案，再联合同主体多条观察，仍可读出与自报/社区代理标签相关的信号。增量是非显式内容与跨记录聚合下的经验隐私边界，不是发明聚合/推断成熟原则、独立新隐私机制或普遍知道真实信念。

DDO 3,511自报R/D参与者、22,265 arguments被按同user/debate汇成text；2007–2018公开帖子/2023下载，排除未自报群体。Reddit采样高参与政治社区正均分用户后去掉两个标签来源社区评论，再每user/subreddit串接，最终993/999用户和19,412/26,548 texts。两种“单条text”暴露粒度不同，平台与时间人口不匹配，不给全部普通用户发生率。General仅DDO非Politics类别或GPT4o按subreddit description分类，不能认证所有显式政治cue已被移除。

S4用一半user训练/选择政治内容分类器，另一半heldout过滤，再预测。S4/S5政治检测不是完美：DDO最佳macro .800左右，Reddit最佳macro .673；filter阴性不是政治语义不存在。完整S6/S7仍见局部信号及异质性：DDO GPT general text .608 / max-confidence user .670，Reddit Llama text .528 / max-confidence .745，但其majority .502、weighted .646；不能泛称每种模型/聚合都可靠改善。正文GPT Reddit .799高于单text .606只限上述分母；verbal1–5 confidence不是已校准概率，最大置信筛选不授独立真实性或因果。

S1五作者对50随机title+正评论作标签判断，平均.85/多数.92、Fleiss κ .576证明与社区代理的一致性，不独立核个人真实隐秘信念。DDO自报与Reddit代理不能合成统一truth。主文明确训练数据未披露，不能排除已学关联/个体记忆；相关词、topic similarity与user overlap均不证明唯一因果feature或特定deployment政治属性已泄漏。English/US、主动透露/高参与者偏差及两模型边界保留。

GPT4o-2024-08-06与Llama3.1-8B-Instruct；GPT zero-shot与Llama格式few-shot不等prompt配置，JSON有效率未到100%，不把未格式化输出默认为安全拒答或总分母。逐text模型调用、同主体聚合、classifier训练/过滤、人审标签治理和敏感记录保存增加费用；hardware/precision、并发、SLO与端到端部署成本Not Disclosed。本项非推理性能报告，不造吞吐/生产安全数字。

## 评分与实际 owner 对照

Design2 + Reach1 + Durability2 = 5：受限数据下“不显式说出仍可联合推断”的隐私边界验证有具体价值，主要是单个observer inference审计，非新跨系统控制。标准必要内容足够；安全边界按合同对受影响命题定点深入，未自动全稿。

实际读Ch72 PLATFORM-SECURITY 31–63完整最小披露/trajectory段、386–432全部observable-channel/联合posterior/来源关联图及canonical-recovery交接、530–553视觉隐私真值与memorization/可提取性分责，另Ch71/73开篇实际读。NC不是题目相似：

- Ch72 46–48已明确单条看似无害碎片累计posterior与sink trust/预算。
- 390–395已要求attacker联合view、相关结构与查询预算，风险独评，不能把逐记录bound提升组合保证。
- 400–402把attribute/entity/edge绑post/observation，selected support不穷尽冗余cue、图误差及旁路费用；414–427具体验端到端observable channels/observer、非DP保证。
- 535–536已分公开可见性、推断/虚构与真实身份匹配，低可见性不认证memorization、格式/输出意愿不认证secret truth。

这些具体原论点已承载本项可支持的设计解释：一般内容/单条clean标签不能给组合观察零隐私风险，统计推断不当真实秘密/训练记忆证书。新实验作为受限验证保留；没有另一个已证控制机制/有效条件缺口，不把政治领域标签增写一条泛化治理段。拟 **标准完成 / 已有覆盖 / Books新写0**，非最低4关闭、非EX；待非准备者实际必要原源/owner独核，不自授PASS。
