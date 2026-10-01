# 04/22 四项 Only 的有限非作者核

复核人：`apr20_resume`，非 04/22 作者。范围仅为 2604.18946/18970/19001/19108 官方 exact-v1 中决定安全或纠错命题的机制、评价反证与真实 Ch29/72 相邻责任；不核全附件、日期/来源、其它候选或日级 Gate，不写 Books。作者必要审阅见本日 `V3_EVIDENCE_REVIEW.md` 相应 ID 节。

## 2604.18946v1 — AltTrain：6 分深入，窄 Only PASS

[官方 §4.2–4.3、§6.4–6.5/Tables 5–7](https://arxiv.org/html/2604.18946v1) 确实把 problem understanding → harmfulness assessment → conditional reasoning 写成训练序列，并以删除步骤/改写模板作局部对照，因此不应作为普通 SFT 换任务而贡献前关闭。但同一 Table 5 中去 PU 的 R1-7B harmfulness 1.7 对 full 14.3、over-refusal 20.4 对 31.6，去 CR 的 R1-8B harmfulness 4.1 对 full 4.8；不能复述“每步对全部安全/能力指标均必要”。Table 6 换 HA 生成模型的拒答与危害取舍反向，Table 7 benign 数量改变训练支持；权重、内容和结构一起变化，不识别“结构是所有安全失败根因”。受限 distilled 模型的拒绝/能力改善可报告，外推全模型、安全保证或所称通用训练时长不可采。

真实 [Ch29](../../../../../books/part-04-training-system/29-sft.md) 已解释 SFT demonstration schema、loss/目标身份；[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 已要求训练 stop/parser 与监测/授权分离。该分段训练 recipe、Table 5 的非单调 trade-off 尚非独立长期责任缺口；判整篇算法 `Only`，不是称 Books 已有完整 AltTrain，也不让模板取得执行授权。

## 2604.18970v1 — Functional Attribution：6 分安全深入，窄 Only PASS

[官方 §4/Eqs 4–6、§5/Table 2、App C.1/D.4](https://arxiv.org/html/2604.18970v1) 以可信参考样本驱动局部 SGLD，比较权重扰动下 reference/test 的 loss trace；test 标签是冻结模型自身 prediction，不是 gold，也不是训练样本因果归属。参数邻域 coupling 与 activation-space probe 是不同白盒 sensor，Table 2 在已呈现正常/触发行为的 LLM 子集上确有受限排序变化；sharp/flat 的说明依赖参考 support/局部几何，不能升级任意隐藏机制的充分检测。DER 按最大值选 operating point，offline UMAP 又使用 test batch，不等固定线上低误报阈值；App D.4 的 Gemma/Llama 939 样本、1000 draws 分别约 3h10m/6h45m，是批处理成本，不是单请求 latency。

真实 [Ch72 sensor/reference monitor](../../../../../books/part-06-ai-infrastructure/72-security.md) 已分配风险读数、校准与授权 owner。此 estimator 本身并非既有正文完整算法，但有限白盒诊断不改变该 authority 边界；`Only` 合理，不写新的普遍安全控制机制。

## 2604.19001v1 — HarmThoughts：5 分保护深入，窄 Only PASS

[官方 §3–6、App A.1](https://arxiv.org/html/2604.19001v1) 对同批句标签从 16 类逐级合并为 6/3/2 类，实测 Macro-F1 随粒度变化；这比再加一种 jailbreak taxonomy 更具体，足以否定“binary 成绩可直接代表细行为监测”。但 1,018 条/56,931 句原先只选 harmful 或 partial harmful trace，13 trace/691 句人工校准后整库机器标注；JS 分布接近不是逐句正确率。白盒 best layer/component 是事后 sweep，black-box parse failure 改变可比较分母；七个输出判断反转中的两个内部比例反向只是受限案例，不证 RLHF 必然学成隐藏危害。

真实 [Ch72 learned sensor 与执行分层](../../../../../books/part-06-ai-infrastructure/72-security.md) 已规定 sensor 建议不授予执行权；句级 granularity 是有限评测证据而非新 gate。`Only` 合理，不能把 probe 高分解释为运行时真实意图。

## 2604.19108v1 — SAFER：5 分保护深入，窄 Only PASS，需修正作者 owner 行号

[官方 §4–5/Eqs 7–13、§6/Tables 1–3/Figs 2/6](https://arxiv.org/html/2604.19108v1) 把当轮 forget 与既往 forgotten 分开、用 retain cluster 与旧样本 negative class-logit margin 控制连续更新，属于局部保护反证，不因 ResNet/ViT 而硬拒。CIFAR-100/VGGFace2 的 class-aligned 三轮与 MUFAC individual-delete/attribute-classification 并非同一删除语义；作者 §5.2 明说 MUFAC 仍有 reversal，retrain 的 margin 也可为正。Eq 12 后一项用下一轮**累计** forgotten 集合，对单个旧请求不是配对恢复量；class margin/DBI/accuracy 更不能代替参数影响或跨通道隐私删除。

真实 [Ch72 unlearning observable channels](../../../../../books/part-06-ai-infrastructure/72-security.md) 约 265–268 已分 secret substrate/observer 与 retain/独立攻击验收，约 2673–2675 的 concept suppression 明说行为抑制不等参数擦除；作者 note 所引“2667–2677”过宽，2667–2671 实为 persuasion，应精确改为上述位置。该特定 class-margin recipe/三轮图表仅报告，不把整个算法说成 Existing 或认证删除；`Only` PASS。

四项均仅为单篇 source→实际 owner 的有限裁决。04/22 日期、来源、全候选及日级 Gate 均未验收；作者同步正式表时应保持以上反证，不以本文件代替原文。
