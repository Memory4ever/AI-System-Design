# VulAgent11523 exact-v1 必要首包

准备者Lovelace；作者120后明确单让、本人接受后的唯一首必要域，交Bernoulli一次不同角色采用，不selfsign。

## 原件与实际阅读

[exact-v1](https://arxiv.org/html/2509.11523v1)，[raw](./REVIEW_SOURCE_11523V1_20261023.raw)、[headers](./REVIEW_SOURCE_11523V1_20261023.headers)、[request](./REVIEW_SOURCE_11523V1_20261023.request.json)。200/exit0/305468B/2.984324s/SHA52306b64e9478266cdfb71faf787b6c4e4ddbd7c6da67c8800bb88ba950e6f41。实际完整S2–6/8、E1–12、T1–5全部行、S5 Listing1及文字解释、全部方法中列出的prompt要求已读。S4.5因合并尾截只补该完整节。其余图只正文/caption，不冒完整图内prompt/schema、所有像素、公开报告/仓库、Joern实现/真实编译或漏洞利用复现。145题摘/current/day有效复用不第三，无currentMethods/别的论文GET。

## 拟原5与安全机制

拟2+1+2=5，只候选报告到显式假设/条件/路径、条件驱动上下文读取和防御检查的协作接口。非多Agent数、安全主题、449.8%小基线或我们的反证加分。保持原窄P，不把有限实验不足改EX/降分。

先给函数加行号，MetaAgent至少三种检查角色，再按语义启额外专长；各角色仍是LLM报告，不认证工具静态证明。以CWE和重叠span聚合，union evidence/source_agents；不同CWE或非重叠span不丢。这个去重规则并不证明同span同CWE一定同根因，聚合身份和原片段应保留。

TriggerPlanner输出(CWE,assumptions,path)，sink存在即尝试构造，先记录guard不在此阶段截去；之后以每个assumption为query读callee/global/type/invariant等context，再检查pre-sink防御是否覆盖全部有关路线。这把“为什么可能存在”和“哪份程序证据能反驳”分开，不是靠多数同意。PrimeVul Joern CFG/DFG/callgraph与SVEN按提交链接取原文件/相关函数/库metadata是不同支持，不把CFG天然称可行路径oracle或缺上下文补成安全。

Eq7标签valid/contradicted/plausible，但prompt说plausible/contradicted/unknown，Eq8只让valid/plausible的条件进入下阶段；文本又要求若被反驳的是必要条件就整条path break。不能实现成悄悄删掉必要前提后重新认证原假设，更不能把unknown改valid。PhaseIV把没有足够反驳的情况retained并注明理由，是待进一步核验的报告策略，不是已证漏洞；有guard也须同路径/同变量版本、覆盖所有有关route才能解释为反证。这些绑定/状态保留是工程采用要求，不冒原完整实现已核或确定性映射已证明。

## 评价条件、正反与未闭合

PrimeVul原总6968vul/6827commits/755project/140CWE是corpus背景，不当本次全量评价；原435pair在S3称validation、S4称test，304有context，人口名称未齐不默改。SVEN1606program/803pair总量与9:1split保原，本次SVEN表对应的精确subset身份/解析失败/重复与APIrevision仍需标签。全部API temp0/top_p1非确定性保证；GPT3.5直接引用旧结果，不能合称全部同机重跑/所有模型公平同预算。非推理默认/strictJSON、concurrency8、抽样均8.83calls/7036.95输出tokens不是全请求p95或完整输入/图谱费用。

T1 GPT4o Prime P-C26.6对18.6、FPR36.7（正文36.8）对52.6、ACC58.4对53.4与SVEN P-C26.5对4.82/FPR55.4对95.2/ACC60.2对52局部值保；449.8%是相对提升不是pp，不代表高绝对coverage。FPR仍高，PrimeVul有更低FPR的LLM-MultiRole17.3/CoT30.8，SVEN GPTLens等不同precision/recall取舍保留，不签所有轴最优。T2只本框架三backbone，无各backbone自己的全部baseline，不能从三行证明无论底座均改善；DeepSeek SVEN FPR31.30反高Qwen28.91，正文“consistentlylowest”不采。

P-R文字“bothfunctionsincorrectlyclassifiedasvulnerable”与bug/fix pair语义不齐；VPS说P-C−P-R，但T1 GPT3.5 GPTLens10.1/6.44却VPS−.91、VulTrial18.6/11.4却1.38等不相合，GPT4o GPTLens10.1/6.76却3.60亦非同差额。保原列不自行修正/合并，新gap不依赖该VPS数值recipe或“理解能力”保证。T1/T2/T3精数/人口不同不静默合成唯一主结果。

T3 Prime有context304pair与缺context其余是不同subset，非同435逐项去掉context的匹配干预；28.73对17.50/ACC59.01对55不能全归contextcause。SVEN另造context对照仍只有限协议。T4各CWE局部低precision/recall/FPR均保，包括SVEN CWE089 FPR.8、CWE022Acc.5/FPR.667；类别自然分母与生产漏洞基率未给，不用平衡pair迁生产PPV/零漏安全。

T5 oracle-CWE与同context确实绕过upstream噪声并控制一份输入，但改多段调用/组织而未等总token/成本，不证明每个角色或多agent必需。VulAgent FPR20.48对Direct49.40同时P-C24.10<36.14、F152.94<65.95、ACC61.45<62.05；VPS22.98亦低Direct24.10（表差额24.10−1.20=22.90不代改）。不能叫无损检出/全指标更强，也不因该tradeoff否定接口可用。配置/crypto/deployment覆盖弱，context不全可漏真阳性/隐藏风险的S6反侧必须保。

S5完整代码示例及其解释是一个原作者no-vulnerability个案，visiblemalloc空值guard可读，但“internaltrusted/长度范围/n有界/assert不可达”等仍依赖未提供全部caller和系统不变量；符号路径来自LLM不是实机攻击验证。本次不独立认证该版本无漏洞、不补利用或实际安全结论。已包含分配式不自动排除溢出，原个案叙述不足以授生产安全。

全部source/commit身份、行号与图谱构建、上下文读取、最少三检查/专长增量、聚合/假设/逐条件/防御LLM、解析/失败重试、旧baseline复现与独立人审/可执行测试都付费。FPR降不能自动得人工总时长降，平均output/calls不替端到端尾延迟/全部token、GPU或服务费。不授完备性/形式验证/可利用证明、自动安全放行或已核代码；未知留pending，原静态检查、单Agent有限报告与独立人工/项目测试继续合理。

## 当前唯一owner拟gap

actual Ch82完整132–168分解/独立证据与验证view、765–813 Verification完整标题/intro/bullets/Judge、11035履历聚合与28286/30074组合验证，1240–1254独立supervisor/arbiter职责已读。现文有generic候选/评价隔离和分支证据、同源共错/外部verifier，但未具体承载**原行号/CWE候选→不提前剪guard的条件/path双产物→按条件定点取证→再单查防御覆盖，保反驳与unknown身份**。Ch66有限1016–1044 bug/fix与人口接口仅承接评价，不拥有该协作消息分工；Ch81有限定位不新建第二owner。

拟唯一AGENT-MULTI-AGENT Ch82这个窄信息接口gap，不是给软件安全新章或宣越多角色越好。可置Verification标题下genericJudge段后、现11035履历聚合前，完整所有旧组/绑定保护；只原三项须作者一次必要采用后另备原稿/PRE/root fresh授权，当前没有Book稿/位/计数。若作者实际发现同具体条件/path/unknown链已被现文承载，可具体NC，不强凑Book。若打算采用强“理解/全指标/因果/无漏”量，才有限重开原metric/人口、同subset匹配context/总预算与真实项目验证或具名修订；不请求全repo/所有图/重复AB日期。
