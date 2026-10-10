# 10323：非准备者必要证据与受限处置复核

复核者：mar13_admission_review。仅既有2026-03-13 Daily补充2026-03-12北京时间自然日。重读当前AGENTS、适用Research/Report/Prompt、Sources每日与arXiv主题边界、本日开头及恢复停点；有效完整v1题摘准入与日级日期独核复用，不以Submitted、Updated或registered单独签公开日。本记录不授整日DAY。

## 实际核验范围

实际读准备包 [SUP_EVIDENCE_10323_HANDOFF.md](./SUP_EVIDENCE_10323_HANDOFF.md)，但结论由原件核验而非直接采纳包内判断。精确身份是Jesse Yu、Nicholas Wei的 *The Orthogonal Vulnerabilities of Generative AI Watermarks: A Comparative Empirical Benchmark of Spatial and Latent Provenance*，arXiv:2603.10323。

- [v1官方PDF原件](./SUP_HANDOFF7_SOURCE_10323_PDF.raw)：https://arxiv.org/pdf/2603.10323v1，608754 bytes，GET200，2026-10-10T04:34:01.641541Z，见[结果](./SUP_HANDOFF7_PDF_FETCH_RESULT.json)。实际读提取文本pp3–8的§3–6方法、主对照与直接限制；必要摘要主张亦回原文。HTML404不替代证据，也不导致全论文/附件扩审。
- 原件中公式部分被文字提取遗漏，因此按PDF阅读技能将v1完整pp4–5渲染并实际目视，核§3.3公式/Fig2、§3.4公式与全部Fig3十行；没有认证运行实现、复现实验、完整攻击探针或全参考文献。
- [当前官方abs](./SUP_HANDOFF7_CURRENT_10323.raw)的完整题摘、Comments/history已实际核；当前v2，没有可见withdrawn信号。为处理具体门槛变动，实际核[v2原PDF](./SUP_HANDOFF7_CURRENT_10323_PDF.raw)的必要pp4–5文字及完整页面视觉，https://arxiv.org/pdf/2603.10323v2，607989 bytes，GET200，2026-10-10T04:37:53.638077Z，见[结果](./SUP_HANDOFF7_REVISION_FETCH_RESULT.json)。不作整版diff或由修订提交时间倒灌本窗日期；修订不重复评分。
- 实际顺读[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)当前190–218完整局部，特别是组件水印、regeneration transformation与10504解释重用两个完整段。唯一owner为ROADMAP的`PLATFORM-SECURITY`，不写Books或共享账本。

## 原证允许的局部结果

§3采用DiffusionDB 2M-first-1k prompts、SD1.5生成4000图，分别两种水印2000图；原文不足认证两组逐图同prompt配对。实验是隔离变换类别、30个强度区间，不是已测复合/自适应威胁。Tree-Ring的survival为`max(0,1−MSE/σ²)`，σ²是约5000的empirical pixel variance；RivaGAN为byte accuracy。共同0–1标尺与CET=.20并未校准成相同误报/敏感度工作点。

v1成功条件是survival<.20且OpenCLIP ViT-B32余弦分数（缩放至0–100）>70。它只定义这一检测信号/内容代理联合人口，不是严格语义、身份、来源或不可伪造证书。实际Fig3十行是RivaGAN control0、brightness22.00、crop22.67、Img2Img67.47、inpainting66.80；Tree-Ring control0、brightness0、crop43.20、Img2Img17.73、inpainting10.27。仅保留该门槛、两种实现、所测SD1.5人口下作者报告的方向与数值，不认证所有空间/latent水印或生产风险。

§5明确架构/生成模型、几何遮罩与inversion局限；§6双层组合、不干扰null-space和复合威胁仍是未来研究，不是已经测试的防线。评估与生成均付费，没有普遍或端到端防御费用保证。

## 中心争议与反证资格

1. §4的严格数学正交/互斥不能由Fig3推出。相同变换类别两组均有非零AER，不支持类别层面的互斥；原证又没有定义对应内积对象、证明或配对joint-failure。这里不能把两组非零汇总误说成同一图像两种水印同时失效已测。方向差异仍是局部经验结果，并不因理论主张过强全部作废。
2. §3.4固定估计标准差.20、n100得到`1.96*.20/sqrt(100)=.0392`，算术正确，但这只是估计条件下的近似，不是任意成功率、所有区间的数学95%保证。若解释为AER的Bernoulli比例，标准差需绑定p，例如p=.5时为.5；此例仅指出普遍保证缺前提，不冒充实际人口p=.5。实际采样方差/区间依赖与多重比较未给出，不能补出所有CI、n3000独立样本或“inversion drift已完整计入”的桥接。
3. v1正文与Fig2均为70；v2正文与Fig2均为75，图文一致，不能报为v2图文冲突。实际v2 Fig3十行数值仍同v1。门槛改变了成功人口，必要页面未给出重算或所有被计入样本均>75的说明，故不能认证v1/70数字已验证为v2/75；数值不变也可能来自同一筛选人口，不能断言必然造假。这一具体纠错信号已定点审阅，不要求全历史版本比较。

## 评分、owner与最终裁决

**2+1+2=5成立。** 新增对象是现代生成式编辑/几何变换与semantic proxy联合检查对两种检测接口的局部失效对照，能够改变只测传统扰动便继承持久性的选择（Design Delta2）；范围仍是两个实现与局部SD1.5负载（System Reach1）；威胁、效用与检测权限的有限分责可复用（Durability2）。不借水印、CLIP或数学正交成熟概念抬分；中心安全/统计/修订信号已深入核必要内容。

实际Ch72组件段已限制generator/decoder/message/update身份和bit accuracy≠authentication；其regeneration段明确传统pixel/frequency鲁棒不覆盖重构、CLIP/FID代理不认证严格语义/来源、SD backbones不外推全变换。10504相邻段又实际分开detector operating-point、配对身份、来源和费用。它没有声称空间与latent失败严格互斥或dual-layer必需。因此本文中心争议不要求改写有效正文，也不把新Fig3数据称已被Book吸收。

**结论：受限事实核验及“争议/暂缓Books新写0”处置通过；中心严格正交、泛化、普遍统计保证与门槛迁移未通过。** 不是EX、不是新实验已有覆盖NC，也没有PRE/实际POST。保留本窗候选与5分，不以中心争议缩池或降分。仅请求足以重开相应主张的明确定义/证明与paired joint-failure、可比detector工作点和实际采样不确定性，以及70→75人口/重算说明；不要求全代码、全部图片或全版本。被隔离部分不能支持正面安全保证、Books或“无遗漏”。

修改范围仅本独核文件；不改Report/Books/State，不stage、commit、push。
