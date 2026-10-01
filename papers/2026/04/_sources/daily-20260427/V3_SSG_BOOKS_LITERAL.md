# 2604.22438v1 SSG：Ch72 最窄写前提案

这只是作者给 root 的 Books 采用材料，不是共享章节写入、非作者写后或整日 Gate。日期按[当日筛选记录](V3_SCREENING_NOTES.md#否定侧新发现260422438-水印注入分组待独立准入)中的官方公告规则、同批 ID/OAI/DOI 原字段有界推断为 04/27 08～09 北京时间，不把 Submitted 或 Updated 单独称为 first-public。[apr20 非作者有限审阅](V3_APR20_SSG_INDEPENDENT.md)已确认准入与窄 Ch72 缺口，root 仍须给共享章采用决定和写锁。

**Owner 与位置：** `PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，现有“生成内容的 provenance 也不能由单一 watermark 承担”中多 bit CDF 消息区间段落之后、watermark 信任根 PRNG 段落之前。现文的低熵容量与 CDF 多 bit 分支没有明确 KGW 式单 bit keyed green/red **等词数不等概率质量**的注入侧失效；不改 Ch75 Context，也不把输出 detector 升格为事实权威。

**拟正文：**

> 单 bit 的 keyed green/red 注入还有一道与多 bit 消息容量不同的边界：随机把词表按 token 数等分，不会把当前 next-token 分布的概率质量等分。在代码或数学推理等少数 token 占主导的位置，高概率候选碰巧落在同侧时，固定 logit bias 能移动的概率质量可能趋近零；检测器即使知道 key，也不能从近乎没有注入的序列中恢复稳定信号。一个有条件的替代是在当前 logits 上把相邻概率的候选配对，再由 key 给每对分边，并使生成端的模型、tokenizer、context、候选集合与检测重放使用同一版本身份。配对是在注入前调节概率质量，不是提升输出统计为来源真值。<!-- source-family:SF-2026-ARXIV-2604-22438 -->
>
> 全词表配对会增加每 token 排序成本，实际实现只配 top-k、其余随机，不能把全词表推导的质量下界当作部署保证；当 top token 概率趋近一时，该理论下界也会退化。受限 code/math 实验有质量下降切片，无原 prompt 的检测有正有负，paraphrase 后 TPR 下降。低风险场景仍可沿用便宜随机分组与统计 detector；若需要强归属或跨改写保证，回退签名元数据、原始 origin record 与独立审计，保留 inconclusive verdict，而不是用水印分数独自作授权。

**证据定位：**[官方 exact-v1](https://arxiv.org/html/2604.22438v1) §4.1 Eq.5–6、§4.2 Alg.1、§4.4 Eq.7–10、§5.1/5.4–5.5；[非作者审阅](V3_APR20_SSG_INDEPENDENT.md)给出 top-k 实现不继承全词表理论界的明确离散反例。拟正文把“版本身份共同保存”标为本书工程推断，非作者已验证的防御；不写 WaterMod 唯一首创或任意低熵正检测下界。
