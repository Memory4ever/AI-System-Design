# 10210 Delta-K：非准备者必要 Source / owner / PRE 独核

复核者：mar13_admission_review。仅 Daily 2026-03-13 补充窗口 2026-03-12 北京时间完整自然日；2026-10-10 执行。准备者为 mar13_supplement，本复核未准备该 Source/PRE、未写 Books。只拥有本文件，不改 Report、State 或共享 ledger。

## 上下文与原件

恢复实际重读当前 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、RESEARCH_SOURCES 使用说明/Daily 组/arXiv 范围、ROADMAP；LEARNING_STATE 只取最新 03-13 路由及本日 README §1/§5 停点。原 09:00 窗口、0 候选及连续 §4 冻结；31 正式处置与普通未决范围只是本日停点，不把宽发现转为全文队列，不加载 03-14 研究内容。10210 有效完整题摘/日级日期夹证复用，不重新裁日期。

实际完整读准备包 [SUP_EVIDENCE_10210.md](./SUP_EVIDENCE_10210.md)，再由 `SUP_CORE_10210_MANIFEST.json` 与 `_RESULT.json` 确认真实名称 `SUP_CORE_10210`、精确官方 URL https://arxiv.org/html/2603.10210v1，GET200 / 362435 bytes / UTC 2026-10-10T01:32:20.471034Z / final URL 同 v1。直接检查 `SUP_CORE_10210.raw` 原 HTML 题名，并读对应 `SUP_CORE_10210.txt` 必要正文，不照准备包结论签章。本包实际是 CORE 原件，不存在必须另猜 DECIDE 路径的需求。

`SUP_ABS3_10210.txt` 实际题名、五作者、完整 AB 与 history 对回：v1 Mar10T20:23Z，latest v2 Sep30。所读官方页面未显示撤回/纠错提示；这只是当前保留原件可见信号，不认证 v2 修改内容或无限期无纠错。日级 registered Mar12 原独核有效复用，不把 submitted 当公开日。

必要原件实际范围：Algorithm 1 全部（512–740）；§4.1–4.2 / Eq3–9（896–1336）；Tables1–2（740–895）、§5.1–5.4 / Tables2–7 及直接 §6–7 限定（1337–1945）；App A 配置与 active-window 口径（2947–3138）；App B 的 fixed-Q / single-block 前提、Thm1–2 与直接推导（3139–3698）；App C/D 的有限 backbone 分析和实际 VLM prompt（3699–3761）。未读 E/F 全图集、代码、旧版本，不看图像 pixels，不宣称复现；这些不是两段采用命题的必要缺口。

## Source：受限 PASS，不签精确 recipe 或强保证

1. Alg1 与 §4 实际建立：完整原 prompt 基线生成 → VLM 分 present/missing → missing 短语遮罩 → 原/遮罩 `K_input` 差 → baseline present-token 平均 attention 目标 → 在线强度优化并更新 key 后继续 denoising。App D 只取短实体/修饰短语、忽略 broad actions / complex clauses；错误属性或视觉模糊也算 missing。因此是模型提出的遗漏/属性 proposal，不是全部 prompt 真值、物体空间位置或因果证明。PRE 第一段准确采用此接口，且把模型判定和表示差的资格收窄。
2. Eq4 在 to_k 输入取差，Eq5/9 又写更新 K，需明确投影/每层映射才成为同坐标可执行 recipe；contextual encoder 不保证未遮罩 token 全不变。Main MASK 与 App A 的 CLIP/EOT、T5/PAD 等实际 placeholder 不同。PRE 的“同一表示坐标”是必须满足的消费条件，而不是声称原实现已无歧义地满足。
3. Eq7 拟合 attention loss，Eq8 却求跨层求和梯度范数平方的最小值，Alg1 直接 Adam(loss)。驻点/梯度抵消不等于 loss 全局最优。§5.1 最大强度 .04 与 Table8 的 SDXL .03 / SD3.5、Flux 3 不同；Main constant throughout、50-step 对照与 A 总步数40/28/28、共同 active window 也未统一。PRE 第二段已明确不补造精确执行配方，故这些不阻挡概念接口的采用，却阻挡认证算法可逐字执行。
4. 固定 Q、单 cross-attention block，省略跨层 LN/FFN，是 B 的真实前提。Thm1 的 sub-Gaussian/弱相关文字不提供实际 masked 差与 query 独立、居中或各向同性的证据；norm 随维度增长也不能直接推出高维必无干扰。更直接，保持 present logit=0，仅把另一 logit 0→1，present Softmax 概率仍从 1/2 变为 1/(1+e)。此反证针对严格 attention 保持，不证明所有实际图像均退步。PRE 只采用共同分母的干扰可能，不借成熟正交/集中性质抬新理论分。
5. Thm2 假定正确 region 全正 logit shift、背景近不动；原 attention 按 key 归一与证明跨 spatial 归一之间未桥接。Eq22 逐 i 分母还需其他 shift 为零，不能独立套用同时多目标变化。真正同一归一分布且目标均正移、背景不动时，总目标 mass 可以提高；本复核不把这个条件性事实一并否定。PRE 未采用真实 region / 普遍集中定理。

## 关键正反评价与费用

直接 Tables1–2：SDXL spatial .2111→.2466、complex .3230→.3532；GenEval overall .55→.58，但 single .98 与 position .15 未变。SDXL color .6371 低于 A&E .6400、non-spatial .3175 低于 SynGen .3249、complex 低于 Playground .3613。ConceptMix SDXL k6 .01 不变、Flux k7 .03 不变。Table3/6 支持这组 SDXL 配置中动态/首10步分支的局部收益，不支持所有 generator 或唯一语义几何归因。

Table5 直接反侧与提案一致：SDXL CLIP .79→.77 / MUSIQ70.67→70.12 / 时间11.71→14.92秒；Flux .78→.77 / 70.62→70.19 / 32.43→42.11；SD3.5 AES5.33→5.28 / CLIP .81→.79 / IQA .67→.65 / MUSIQ69.82→69.53 / 14.49→16.52。没有给 CI，不夸大显著性；“部分质量下降和生成变慢”是实际表中有限点估计，不是普遍退化。

App A 实际披露 RTX4090/A100、FP16、三 backbone、temperature0、JSON/tokenizer、每步100迭代及 LR 等。完整 baseline / VLM / online optimization 是否全部包含 Table5 时间，batch/并发/全部输入分辨率/seed-CI/驻留内存等未由所读表格闭合。PRE 的完整费用分账是工程验收要求，不是把作者 timing 认证为完整生产 SLO。Table7 多 VLM 近同的 .3402/.2352 等也不是 Table3 .3532/.2466 的自动相同人口或 VLM 无误证明。

## actual owner 与评分

ROADMAP 唯一 owner `MULTIMODAL-GENERATIVE-PARADIGMS`，实际 Ch24 完整174–221 顺读：噪声/经验 aggregation 与记忆 → reference subspace / 总注入范数 → TP-Blend 两段的位置迁移和 style K/V → reference 频率替换 → 后续 reference 编辑分支。另完整1536–1565 的 CFG、运动条件、reference field、视频 event-time 路由与邻接直接读。已有内容确实分开 amount/where/operator、attention proposal 与真值/最终验收，不把这些共有边界算新增。

但现 TP-Blend 是双 prompt 对象运输与 style K/V replacement，不是基线图遗漏判定后构造 masked-prompt key 差，再以已生成概念 attention 拟合早段强度；event-time 分支是给定事件区间的条件读取路由，也没有这一遗漏修正协议。检索当前 Ch24 无 10210 / Delta-K 命中，与实际完整 local 对回一致，不能只用无同名证明 gap。Ch23 实际章首表示 identity 及 Ch25 章首生成/世界状态区分确认相邻 owner；Ch66 实际255–286 的 evaluator/sensor 与行为验收局部只作测量 handoff，不新建第二 owner。

独立接受 **Design2 + Reach1 + Durability2 = 5**：Design2 是 attention 后缩放之外、由实际遗漏判定产生 key proposal 的重要替代接口；Reach1 限定单生成 conditioning 路径，不因调用 VLM 算跨平台；Durability2 只计 baseline/judge、两 prompt、token/投影/层-step 与在线强度共同匹配的稳定消费约束，不计 Adam、Softmax、正交或通用 identity 原则本身。真实 owner gap 与强无干扰/费用外推使必要局部深入成立；不是按“已读很多”倒推分数。

## PRE：两段逐字 PASS

同意在当前 TP-Blend 完整两段后、reference 频率替换前窄写下列两段。实际与完整上下文并存，不覆盖原位置迁移/风格接口或原方案；第二段紧邻保留收益、代价、失效和回退。无需最小修正。此 PASS 仅两段的受限命题，不将原强理论争议整体升级为已吸收。

对象遗漏也可以通过 key 的消费接口提出修正，而不只把已有 attention weights 放大。一条受限分支先按原 prompt 生成基线图，由视觉语言模型提出 present 与 missing 短语；将 missing 短语替换成占位符，与原 prompt 在同一表示坐标里取差，作为缺失条件的 key 更新 proposal。早段去噪再用基线 present 短语的平均 attention 作目标，在线调注入强度。图像与判定模型、两份 prompt、token 映射、投影位置、层与 step 都须绑定；contextual 表示差不一定只含一个概念，模型称 missing 也不等真实遗漏或目标位置。

[Delta-K 的有限对照](https://arxiv.org/html/2603.10210v1)支持这条条件消费分支，但改一个 key 也会经 Softmax 分母影响其他对象；固定单层 query 的局部假设不能签整条轨迹无干扰。原文投影前后位置、强度优化目标与若干配置未统一，不据此补造精确执行配方；注意力拟合仍需独立验收目标完成、既有对象和原画质。局部组成分数提高伴部分质量下降和生成变慢，完整基线生成、VLM 判定、表示与 map 驻留、在线优化都计费。遗漏判定、坐标或预算失配时，保留原 prompt、已验证的固定 guidance、区域条件与独立输出检查，不用更集中的 attention 批准语义保持。<!-- source-family:SF-2026-ARXIV-2603-10210 -->

Source（受限）、5分与 actual owner gap、逐字 PRE 通过；Books 尚未由本复核者写入或验证实际新稿，**无 POST / DAY**。恢复只接这两段实际写后局部与作者末注，必要原证有效复用，不展开全附件/旧版差异。
