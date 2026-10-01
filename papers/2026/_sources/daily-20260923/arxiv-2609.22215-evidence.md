# `2609.22215v1` — 隐蔽性状迁移与早期锚定

- 身份与日期：官方 09-22 arXiv New 公告批次属于 09-23 北京时间日报窗口；[摘要及版本页](https://arxiv.org/abs/2609.22215)的 `v1 Submitted 02 Sep` 是投稿历史，不能替代首次公开。审阅 [exact-v1 HTML](https://arxiv.org/html/2609.22215v1) §3–4、Limitations；访问 2026-09-23。未核实更早作者公开渠道或代码 commit。
- 问题与旧方案：teacher 输出的可读内容可能不涉及某偏好，student 仍可能从输出分布习得该性状。文本过滤、只测终态或普通 SFT 在目标任务明确且无此迁移时仍合理；但它们不能证明训练途中没有附带偏好。旧研究已有输出头相关与迁移先例，本篇并非发现 subliminal learning 的首篇。
- 机制与状态：以 frozen base model 为 reference，在 completion token 上加入 `KL(base || student)`，前三 epoch 中首 epoch 权重为 `1.0`、之后线性降为零；training owner 决定 schedule，teacher 负责监督数据，base reference 拥有锚点 identity，独立 evaluator 分别测目标任务和 trait。训练时检查多个 checkpoint，不把终态损失或一个动物 token probe 当广义安全证书。
- 评价边界：作者使用 Qwen2.5 1.5B/3B/7B、Gemma 3 4B、Llama 3 8B 的数字序列和 GSM8K CoT 蒸馏，三 seed；另有 French response-style 一个实验。early-weighted KL 与固定、late-weighted、paraphrase、layer freeze、early stop 对照显示受测 task–trait 折中，但 KL 强度过大牺牲任务学习。作者明确未识别内部作用机制，也未能可靠诱导 misalignment；未测广义安全、校准、鲁棒或生产部署。
- Trade-off 与 Books：Ch29 原有“无关内容不等于蒸馏安全”与 output-head 共同偏差，本篇增加**约束时间**和中途 trait 轨迹的评价合同，正文以旧方案边界→早期 KL 分支→任务收益与附带性状的代价展开，未把特定训练 recipe 写成通用防护。V2 评分 Design Delta 2、System Reach 1、Durability 2，合计 5/9；独立写后审阅通过。本笔记只验收单项，整日报状态以日报为准。
