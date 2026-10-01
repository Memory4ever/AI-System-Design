# 04/22 三项单篇必要命题的非作者有限复核

复核者：root，非本日日报作者。实际重开以下官方 exact-v1 的方法、关键反向表与边界，并对读实际 Books owner；复用作者未变化的样本/配置记录，不复现实验、不签日期、来源、负侧或整日 Gate。

## 2604.19264v1 — DR-MMSearchAgent

[官方 v1](https://arxiv.org/html/2604.19264v1) §3.1 Eqs2–9、§3.2 Eq10–11、§4.3 Tables3–5：SPAI 先把 terminal reward 放到 trajectory 位置并在 batch×rollout 的时间轴上归一，按相对正/负理想位置得到 `F_i`，然后以 `A'=A(1+W_i)` 乘原优势。`A=0` 仍为零；这不是环境所有中间动作的独立因果 credit，跨 prompt 的长度分布也影响所学权重。BGAS 的 Gaussian tool-call 目标依已知答案正确与否切换；真实线上未知正确性时只能用于训练的已验证标签，不能把它当部署期间 oracle。Table3 是从 57.7 到 59.7/60.8/63.4/64.9/66.8 的组件递增，Table4 的 160/200/225 steps 不匹配总训练 compute，Table5 的 10% 注入低于 5%。实际 Ch33 已区分同 prompt GRPO、verifier 对象及 trajectory artifact；此训练配方的跨 batch 权重尚不足以形成新的长期 owner 责任。**6 分标准、仅报告的窄处置通过**，不采通用探索提升、因果 step credit 或同成本优越。

## 2604.19267v1 — Multimodal embodiment-aware navigation transformer

[官方 v1](https://arxiv.org/html/2604.19267v1) III-A–F/Eq14–25、IV-A–D/TableII：image/LiDAR、goal、robot size 汇合后 diffusion 生成有限 waypoint candidates，另一个按机器人宽/长条件化的 clearance head 对每条候选打分，再由规则选择发往低层 controller。预测 clearance 与可验证碰撞证书不是同一对象；LiDAR/ground removal、sensor calibration 与动力学失配仍在 controller/safety owner。TableII 的 TEB-Elev 在三环境的碰撞率全为 0 且两环境成功率高于作者方案，不能从对 image-only policy 的胜出推广为传统 planner 已过时；文中的真实 85%/15% 未披露样本数。实际 Ch26 已建立 perception/proposal/controller/safety 分权及 embodiment/action-schema 合同，尺寸条件排序可作为受限案例，不必新增一般结论。**6 分深入必要范围、仅报告通过**；不采“safe candidate”是形式安全保证或所有任务收益。

## 2604.19292v1 — Location Not Found

[官方 v1](https://arxiv.org/html/2604.19292v1) §3–5.2、Limitations：44 个语义平行问题经 12 语言/49 地区扩成 2156 locale-specific QA，16 annotators 双审；explicit locale prompt 测已知事实，locale-ambiguous prompt 测默认选择，是两个不同的 Eval 对象。Global US-answer excess 要扣 gold collision；Regional lift 按语言内地区计，不等实际部署人群公平目标。Gemini 2.5 Flash judge、GPT-5 mini 交叉与 80 人工 92% agreement 只支撑该受限测量；answer multiplicity 与 global bias `r=.95` 是相关，不能证明 instruction tuning 单独引起地区偏置。实际 Ch66 原跨语言段只拥有派生题的语义/标签保真，未有“语言≠地区、显式知识≠未指定地区时的选择”这一稳定评价分母。**5 分但触发真实知识缺口：改为 `Integrate — Ch66 实写待作者外写后复核`**；正文仅增加 paired explicit/ambiguous eval 与产品澄清策略的工程推论，保旧显式测试和事实时效边界。此处不预支写后或整日 Gate。
