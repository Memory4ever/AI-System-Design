# 2604.25783v1 Subliminal Steering：必要原文与 owner 差异

作者侧有界审阅，非正式冻结候选、独立 Books Gate 或日级 Gate。[官方 exact-v1](https://arxiv.org/html/2604.25783v1)题名 *Subliminal Steering: Stronger Encoding of Hidden Signals*。本窗 arXiv 公告归属仍需与同家族更早公开例外联合核，页首 `28 Apr` 和提交字段不能单证首公开。作者 [GitHub 仓库](https://github.com/GMorgulis/Subliminal-Steering-2026-Code) `created_at=2026-04-18T02:41:53Z`，该日最早可见 [commit `72aa8c8`](https://github.com/GMorgulis/Subliminal-Steering-2026-Code/commit/72aa8c885785ba8b1b837732e396e327f91929f7) 的 README 已有同家族摘要、teacher steering→数字→LoRA student、layer-local imprint、vector recovery 和四模型清单；[04/23 commit `a647ab2`](https://github.com/GMorgulis/Subliminal-Steering-2026-Code/commit/a647ab249a3d85d9e9cbbb580b93e7508c75b4e4)又已有带结果图的 blog HTML，但树内未见完整论文 PDF/TeX。当前仓库是 public，不能由创建/commit 时刻证明当时 public；也不能无视早期实质方法披露而直接以 arXiv 公告冻结本日首公开。日期 Gate 须具名隔离此例外并取历史可见性或独立发布记录，若无可得证据则按合同给准确终态。

## 机制与准入

旧 prompt-subliminal 方法让 teacher 在无关数字任务中输出数据，student 用这些数据微调；本篇 §4 把 teacher 偏好改由冻结权重上的 learned residual steering vector 产生，再仅筛出纯数字 completion，取 10,000 条做四轮 rank-8 LoRA student SFT。四个模型、八动物与八复杂短语、每题两 seed 中，对照包含 base、无偏数字 Control、prompt-subliminal 和 steered-subliminal。动物偏好量为前五 token pick-rate；复杂短语量为目标短语 per-token log-probability，**不是**实际有害回答/行为的频率。§5 用 student 与 base 的同 prompt 最后 token activation 差的均值对原 vector 取 cosine，改 teacher 注入层窗口时 student 对齐峰随之移动；这支持受限 layer-local imprint，而非证明同一向量作为一般因果安全后门完整迁移。§6 冻结 base 模型，只在已知相同 steering 参数化下重新拟合一个 vector，原向量 cosine 多数高于 0.5，再用强度扫描和 LLM 摘要/judge verbalize；该恢复流程不是未知来源数据的通用 detector。

Ch27 [合成数据与 provenance](../../../../../books/part-04-training-system/27-data.md) 已要求保存 generator/persona、mixture、row lineage 和独立非叙事 behavioral canary，但现有例子为有语义叙事的隐含偏好。Ch72 [风险清单](../../../../../books/part-06-ai-infrastructure/72-security.md) 已有训练前 subliminal-learning probe 的 channel/alignment 限制，Ch31 只拥有部署端 activation intervention 的效果/权限。因此潜在唯一 owner 是 Ch27：**即使 row 只含数字且文本审核不见目标偏好，带已知 teacher-intervention identity 的合成 partition 仍须独立评估其对 student 目标概率/行为与层表示的迁移**；provenance 应能区分普通 prompt-conditioned teacher 与 hidden-state-steered teacher，而审计 probe 只能在其假设覆盖的表示通道解释。此是现有 Ch27 叙事语义例之外的窄条件，不应把论文 vector-recovery recipe 写成必需上线检测器。

拟 `2+2+2=6` Standard 候选、Ch27 窄 Books gap 提案，待非作者 source→actual-owner 与 root 锁；未写共享 Books。安全相关不自动 Deep；目前没有需要中央保证纠错的印刷不可能命题。

## 直接反证与范围

- §4.3–4.4：复杂短语在 student 的 surface probability 仍低，主实验只是 log-prob shift。四模型/两 seed 条件下，原 prompt baseline 在 Qwen 已有信号，不能称“只有 steering 才会传递”；不同 prompt 实现也非统一最强 baseline。
- §6.2 / Appendix A.7：正文称 20 个短 neutral prompts，附录实际列 **19** 个固定 prompts；本审核隔离提示数量口径，不让它变成 20-item 严格协议。verbalization 依赖固定词/短语 signal、强度扫描与 LLM judge，作者 §6 Scope 明言未知条件触发的偏好未显示同样可自动 verbalize。
- Appendix A.2/A.4/A.6：teacher 共生成 40,000 数字样本，student 用过滤后 10,000；student 是 LoRA，不是 full fine-tune。Appendix A.6 确有仅针对**向量恢复**的 ground-truth 层窗/强度固定、禁用 normalization 的 SGD 控制消融，不能称主 student 用 plain SGD。该附录还称 recovery 在 fp16 收敛、非 fp16 失败/停滞，实施对数值身份敏感。
- §7：固定单向量、跨层统一注入不是任意复杂行为；模型差异、复杂偏好弱效和 verbalization 的假设限制必须保留。不从本研究推出受限生产模型已有可利用漏洞，也不以纯数字 row 就判所有合成数据危险。

旧初筛曾把 “Llama/Phi 和 plain SGD 来自 v2”写成过宽版本差异：**v1 §4.4 本来就含 Llama/Phi；v1 Appendix A.6 本来就含上述 SGD 消融**。只需隔离 `full fine-tune` 与“主训练 plain SGD”等错误身份；准入方向不变，分母仍是已读 106 篇中的一条潜在线索。
