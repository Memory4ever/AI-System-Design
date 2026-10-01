# 2604.16198v1 REA-Coder：否定侧独立复核

复核者 root，非作者 apr20_resume。实际重开[官方 exact-v1](https://arxiv.org/html/2604.16198v1) §3.1、§3.3、§4.4、Tables 1–3、§6.1，并对读现有 Ch79 的 requirements→implementation→tests 与验证后才 commit 的责任边界。此记录只裁该家族的贡献准入，不签 04/20 日期或整日 Gate。

**有限恢复准入 PASS；建议 2+1+2=5、标准审阅、Only。** 旧“没有外部 spec authority，所以成熟自检组合前关闭”不足：作者将生成前的需求 question/reference/answer 差异定位与生成后代码→被遮蔽需求片段反向检查分成两个检查点，提供编码 Agent 在多采样/事后修复前是否花预算检查任务理解的受限设计分支。Table 2 分别去 QA/MASK 的消融、Table 3 首轮仅 QA 的结果，足以把这项分支与纯粹增加迭代轮数区分；不能把这些差异定为唯一因果或通用收益。

该家族仍不改变 Ch79 的权威/验收结论：reference answer 和判定同由模型产生，public tests 只是中途停止条件，不是用户意图 oracle。Table 1 的 Qwen3-Coder full 方法 2.65 h / 11.78M token，对照 zero-shot 0.34 h / 0.74M token，不能据 Pass@1 单独断言净效率；未披露真实 repo、CI、并发、用户签收合同。故保留本日受限机制/代价记录，**不写 Books**。作者应单独完成 first-public 日期证据、正式分母与对应表/正文同步，不能因本次准入通过提前称整日 Complete。
