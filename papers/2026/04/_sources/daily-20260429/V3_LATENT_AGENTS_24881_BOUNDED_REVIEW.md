# 2604.24881v1 Latent Agents：有限证据与贡献准入（作者侧）

本项仍属 `V3_REOPEN_NOTES.md` 中旧 60 篇完整题摘的 **69 项潜在线索之一**，不是新增原始命中、冻结候选或日级通过。官方身份与必要正文：[exact-v1 HTML](https://arxiv.org/html/2604.24881v1) §2.1–2.5/Table 1、§3.1–3.3、§4.1–4.3、§6 Limitations，以及决定性反证 Appendix P/Q；[v1 身份页](https://arxiv.org/abs/2604.24881v1)。HTML 页眉的 `27 Apr 2026` 是版本日期，不独证首公开；本日归属须连同 checkpoint 所载 arXiv 官方公告/相邻 ID/DOI 代理窄批次链判断，不能把提交字段当发布时间。没有扫旧版或所有附件。

## 贡献问题与实际证据

在多 Agent debate 需三人两轮长文本、而只蒸馏最终答案可能丢掉中间交互的条件下，作者将 **944 条算术 debate 完整轨迹**（而非仅最终答案）作 SFT，再以递减 format reward 和 2000→500 token 的正确答案长度截断 reward 做 RL。这提供一个可核的训练—推理选择：用离线轨迹生成、SFT 与 RL 成本，换在线少写完整辩论；若成立，不能把单模型短答的运行成本直接与现场三 Agent 辩论比较而不计前置训练与质量回退。它不是新的多 Agent runtime，也没有给内部角色真实独立的权责、证据或 verifier。

Table 1 采用 LLaMA-3.1 8B、Qwen2.5 7B、Mistral Nemo 12B，各在 GSM8K、MMLU-Pro、BBH 抽 1000 题、三次运行。IMAD 的 token 用量约为显式 Debate 的 6.3–21.1%，但准确率**不是同样都保持或超过**：LLaMA MMLU-Pro `62.00` 低于 Debate `64.60`，Qwen GSM8K `89.67<91.37`、MMLU-Pro `52.87<57.67`，Mistral MMLU-Pro `38.97<41.30`。LLaMA 的 SFT-only MMLU-Pro `75.60` 经 RL 降至 `62.00`，故“短轨迹”本身未带来无损知识保留。Table 1 也没有匹配离线 teacher 三人轨迹、SFT/RL 的总计算成本、wall-clock、真实多用户 serving；`up to 93%` 只能是显式 Debate 相比的受测在线 token 极值。作者 §2.5 的“LLaMA 全三项优于 debate”、以及 Qwen “相近/略好”的概括均与相应主表部分指标不合，不能沿用作总胜出。

§3 对 CoT/Self-Critique/Program-of-Thought 三种预设角色构造 500 train/100 test trace，用 SFT checkpoint 的 contrastive mean-difference activation 干预；受测 ROUGE 与示例说明**输出风格**可被条件性推向预设角色，但不证明三个相互独立的推理 Agent 存在、仍执行了隐形多轮交互或因这些“子空间”导致正确率变化。§4 恶意/幻觉 persona 干预在单一 LLaMA-3.1 8B、每条件 100 test questions 上由 LLM judge 打 0–100 trait 分；“evil”大负系数分数到零，而 hallucination 基线约 65、两模型均未完全压低。Appendix P 在轻度负系数也有 IMAD 重复循环的反例，不能用平均 PPL/单一 GSM8K 推通用安全或无副作用。Appendix Q 的两名人工评判只在预先挑选的 judge 高分 `>80` 与低分 `<20` **成对输出**作相对强弱判断，193/200 同意不校准所有中间分数、不验证真实有害 effect；§4.2 还写用于 steering-vector extraction 与 evaluation 的 500 train/100 test question 集合相同，需保留问题级独立性疑问。本文 §6 自认固定三 Agent 两轮、算术训练，且其它模型有 structure-learning 失败。

## 真实 owner 与作者侧暂定处置

`ROADMAP.md` 的 `AGENT-MULTI-AGENT`→[Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 已区分显式文本 handoff 的可审计性、通信 token 与接收方重建成本，且要求 latent channel 不能取代 authority/task state；[Ch31](../../../../../books/part-04-training-system/31-rlhf.md) 已把 probe 可读、输出方向对齐与实际 steering 效果分账。与这些相邻命题相比，**完整辩论轨迹蒸馏＋递减格式/长度约束**是受限训练配方与在线成本取舍，而不是缺失的长期通信/授权合同；§3/4 的角色方向和安全结论不够支持新增 Books 机制。拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5/9`，`Standard`、`Report Only / No Change — Existing Coverage`，待非作者复核贡献准入、表格反证、真实 owner 与 first-public。此处 `No Change` 是作者侧提案，**不宣称独立通过**；若非作者定位到非同义的训练—推理责任缺口，可再提窄 Books patch。主张“只有内部多视角推理这一种可行策略”是作者从长度奖励推导的解释，现有行为/风格代理无法排除单路径短答或旧知识调用；只隔离该解释，不把整篇受限性能观察标成安全定理争议或反过来抹掉。
