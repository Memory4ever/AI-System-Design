# 2604.25132v1：指令数据的 ICL influence 代理

本日作者有界证据审阅；不是独立复核、正式候选冻结或日级 Gate。身份为 [official exact-v1](https://arxiv.org/html/2604.25132v1) *What Makes Good Instruction-Tuning Data? An In-Context Learning Perspective*。本日 arXiv 公告窄批次链支持 v1 归入北京时间 04/29 08:00 批；检索所见 ACL 2026 正式版为后续出版，未见足以改判的更早同家族全文，但单篇更早公开例外仍待独立日期核，不能拿页眉 `28 Apr` 充当首公开时刻。

## 贡献与必要机制

对固定 instruction-tuning 数据预算，只按样本自身困惑度/难度选高分，不等于其能帮助相邻指令。§3 以当前模型把候选作为 one-shot demonstration，先取语义近邻、分簇并挑高复杂度 probe，再计算 probe 的 instruction-following difficulty 前后差；式 (8) 用语义距离加权这些差，最后以相似度门槛贪心组 coreset。这个分支从“样本本身难不难”转到“在相关而不同的 probe 上是否减轻困难”，是 Ch27 数据选择可核的代理差异。它不是 ICL 和参数微调等价证明，也不直接测出单样本训练因果价值；NUGGETS 已用 one-shot anchor 评估，本文主要改变动态局部 probe、权重与选择成本。

§4–6 的训练对照固定 10% 样本预算，用 Llama-3.1-8B、Mistral-7B-v0.3 在 Alpaca-GPT4/WizardLM 上全参 SFT。Table 1 的四组 pairwise 分数里，作者法对 full data 均大于 1，但并非各组最优：Llama/Wizard 作者 1.169，IFD 1.186、SelectIT 1.176；Llama/Alpaca 的 AlpacaEval WR Table 2 作者 7.50，IFD 7.58。Table 4 的去 probe 聚类与去选样多样性消融均弱于 full method，仍高于 full-data pairwise reference。Appendix C Table 6 的 16 forward/sample 对 NUGGETS 2000 是作者按调用数的估算，未同口径量 embedding、cluster、reward-model scoring、token length、实际 wall time 或每种方法的训练总成本，不能称生产成本胜出；IFD 只有 2 forward/sample。

**印刷反证必须隔离：** 摘要声称 difficulty 与 in-context influence **负相关**，但 §6.1 Table 3 列出的全序 Spearman 是 Alpaca-GPT4 **+0.3947**、WizardLM **+0.2568**；top-10% 交集 10.06%/14.42% 只说明高难度与高影响并不高度重合，不支持负相关。保留“高难度不可靠地等于高影响”的窄结论，不继承负相关方向。§6.4 医疗迁移只作受限补充：Table 5 中 Llama 的 MedMCQA/MMLU-med 作者 39.63/65.33 仍低于 full 40.53/71.33，Mistral MMLU-med 50.00 低于 full 51.67；这里 30% vs full 并非同训练样本预算。Limitations 明确未测 70B、大语料或 DPO/PPO。

## 与实际 owner 比较及作者处置

唯一长期 owner 为 `TRAIN-DATA` [Ch27](../../../../../books/part-04-training-system/27-data.md)，SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md) 是更新/能力验收相邻。Ch27“Coverage Contract”已区分语义与 feature coverage、当前难度；“Post-training Data Selection”已要求 checkpoint 相关 proxy、held-out outcome、额外观测成本和冻结 mixture 回退。Ch29 已要求固定预算下 tail/能力切片与回归验收。本文的 one-shot peer-influence 是对已有 proxy 选择合同的受限实现和反证，不新增 selector 提交权或通用数据价值定律。作者侧拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard，`Report Only / Books No Change — Existing Coverage`；需另一审阅者核其 exact-v1 正负证据与真实 owner，不能由本作者自签。该项原在 106 工作题摘中的潜在线索，不改变 `64+41+1` 工作分账，也未成为正式当窗候选。
