# 04/28 五项 Existing Coverage 的非作者 source→body 有界核验

本记录只核已列出实际正文的五项身份、必要机制和 Books 命题。它不冻结 04/28 候选分母、不能代替来源/日期 Gate，也不因书稿中已有文字倒推当窗首次公开。官方 exact-v1 访问日期：2026-09-29。

| Family | exact-v1 中可核的机制与边界 | 当前 Books 正文对照 | 判定 |
| --- | --- | --- | --- |
| `2604.22981v1` | [§4、§5 与 §9](https://arxiv.org/html/2604.22981v1) 将 prefix reward 输出以 lookahead/MC、TD coherence regularizer 联系到当前 continuation policy 下的终局分数条件期望；作者在 §9 明言中间输出并非精确条件期望。 | `TRAIN-PPO` Ch32 的“Final-only Reward 到 Temporally Coherent Prefix Value”实际写出 final-only 合理性、prefix proxy 的状态 owner、off-policy 漂移与回退，不把 token score 等于真值。 | Source→body 通过；拟 Existing Coverage；日期另审。 |
| `2604.23036v1` | [§3 与 §6](https://arxiv.org/html/2604.23036v1) 的 biased routing 与 always-active gated condenser 针对长尾 expert 梯度饥饿；§3.2 明列 condenser 数量与容量/梯度集中取舍。 | `MODEL-MOE` Ch21 的“长尾 Expert 低频不等于无知识”保留旧 load balancing 的成立条件，并区分 route、条件容量和共享通道，限制于所测 MoE SFT。 | Source→body 通过；拟 Existing Coverage；日期另审。 |
| `2604.23073v1` | [§IV](https://arxiv.org/html/2604.23073v1) 冻结 VLA，把 RL token 作为小 actor–critic 的状态接口，replay 汇合 VLA/在线/人工干预，human 标注 sparse terminal reward。 | `MULTIMODAL-EMBODIED-VLA` Ch26 的“Online RL 应通过受限 Action Interface 接入 VLA”实际分离 VLA prior、局部 action head、controller/safety 与人工接管，并未宣称无监督自主学习。 | Source→body 通过；但当前 OAI 可能反映后修订，first-public/date Hold，未准许正式当窗。 |
| `2604.23080v1` | [§5](https://arxiv.org/html/2604.23080v1) 的 Kademlia 与 Cyclon/Vicinity 对比按 node churn、agent cooling、maintenance 预算及 useful availability 分条件，作者明确只用模拟。 | `AGENT-PLATFORM` Ch84 的“Agent Discovery 是可修复的路由状态”实际区分 node membership、Agent readiness、overlay soft state 与身份/权限，保留中心 registry 条件。 | Source→body 通过；拟 Existing Coverage；日期另审。 |
| `2604.23205v1` | [§3、§5、§8](https://arxiv.org/html/2604.23205v1) 的 64B AXI burst、address-derived AES-CTR 与片上 SRAM 明文边界是参考架构；§5 大量吞吐为 proxy/model projection，§8 承认 CTR 无完整性。 | `PLATFORM-SECURITY` Ch72 的“Weight Streaming 的保密边界”实际描述 at-rest→ingress→on-die 路径、nonce/隔离条件及未制造芯片边界。family marker 在机制段末，仅 marker 位置不证明正文；机制正文确实存在。 | Source→body 通过；拟 Existing Coverage；日期另审。 |

五项均未发现“只有 Review note 或 source marker、没有正文机制”的虚假 Existing。不得由此将作者的 benchmark 泛化为生产结论，或把 `2604.23073v1` 的日期疑点抹平。其余三个晚字段 Existing 候选不在此记录内，维持 Date Hold。
