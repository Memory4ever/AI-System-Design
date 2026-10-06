# Auditing replication必要证据与条件Books比较

作者Plato；实际必要阅读/owner对读至2026-10-02T20:04:11+08:00。首公开未授，不能作为12/13正面采用，也不把12/12日标签证明为12窗外。原始链接：[官方精确研究页](https://alignment.anthropic.com/2025/auditing-mo-replication/)；本日source已记精确日期有限替代与隔离，不重复接口。

## 实际方法与关键反证

实际读Introduction、Replication Procedure、Evaluation、Non-assistant Persona、SAE、Discussion以及Appendix A/B/C相关训练/评价段。LLaMA3.3-70B model organism先SFT biased documents，再DPO与adversarial DPO；数据52 bias documents，held-out 5 of 51的应用/适用过滤与reward的applicable-and-applied并不相同。每prompt四prefilled/二unprefilled completions，选高二/低二；LoRA256、batch32，学习率2e-5/5e-7/5e-7，旧adapter冻结求和。这里是作者披露配置，未核源码/运行，不推出硬件/precision/batch serving/concurrency/SLO或生产安全。

普通模型中可用的non-assistant persona途径在新model与adversarial training后近乎失灵；原0/1.2/11.4%等差异不构成同model同训练的因果对照，本报告不采数字排行。100次temperature1 persona采样与100次三轮red-team所含prefill是不同攻击方式，不能用一个检测率宣称全部攻击不可见。Appendix C中SFT/DPO泛化差异还受classifier未识别适用bias的混杂影响，不能推出DPO必然更隐蔽。SAE assistant-token feature30277相关，但仍在原先技术/化学句激活，polysemantic不等内部目标真值；本研究未运行human auditing game，不授审计成功。

## 实际owner及相邻比较

唯一条件owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：实际164–174把observed behavior、elicitation与supervisor ceiling拆开，训练elicitation不证明真实最大能力；实际203–216要求绑定adapter-generation method/分布、跨方法holdout，内部SAE/probe随模型/层/训练方法变化，不由阴性放行；实际626–635明确测量仪器需已知contrast、sensitivity/variance/扰动稳定且不授安全认证。不是“已有Evaluation章节”主题判断。

相邻Ch65开篇是GPU资源公平，Ch67实际14–17只承担observed state/质量趋势，不替评价规范。该材料的persona可迁移性与SAE阴性边界已经由上述具体论证承载，若日期与独立证据复核恢复，可作已有覆盖/No Change的限定新验证，不必另造机制章。此处条件比较不是本日正式Books采用、不是全稿已覆盖；没有修改共享Books，也没有把所有新机制一律仅报告。

如root认为需要把persona行为探针这个具体反例补入，最小局部方案是在Ch66现有跨adapter制造方法/SAE sensor段后加一句案例而不改主论证：`在新model organism及adversarial training下，原有效persona审计可能失效；检测阴性只限定该模型、训练法、攻击mode与预算，不是隐藏目标不存在。` 仅由date授窗及非作者证据核验后决定是否采用，不预写source-family或审计通过。

## 停点

日期/历史目录外部缺口见SOURCE_SCREEN的具名终态保留项。正文可读必要内容已处理，未复现实验、未声称通用安全、因果识别或所有bias覆盖；本报告仍待Popper独立验收。
