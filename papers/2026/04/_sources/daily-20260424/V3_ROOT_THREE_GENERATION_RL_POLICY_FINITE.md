# 2026-04-24 三项仅报告候选的有限非作者核

复核者 root；核官方 exact-v1 正文与现有 owner 命题。本文只决定下列三项的受限证据与 Books 处置；不代替本日剩余候选、来源、日期和否定侧的日级 Gate。arXiv 首页 submitted 日期不是首次公开时间；本组未据此单独签发窗口归属。

## `2604.20902v1` Frequency-Forcing：仅报告，具体实现边界待澄清

[官方正文 §3.1–3.4、Algorithm 1、§4](https://arxiv.org/html/2604.20902v1)保留 pixel flow-matching 的原始插值路径，另建早成熟的低频 latent 流作软条件。§3.3 一方面称同网格 pixel/frequency embeddings 相加，另一方面称联合 key/value 上有按流单向 block-causal mask；原文未交代相加后如何保留分别可寻址的流 token，因此不能从描述构造可执行 attention 布局。实验还同时改变训练预算、流数和辅助提取器；所测 FID 不能唯一归因于频率引导，也不能外推端到端时延。`MULTIMODAL-GENERATIVE-PARADIGMS` [第24章](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)已有连续扩散/条件生成的状态与训练代价链；此处精确分支在身份与实现桥未清前不足写成长期机制。维持 2+2+2=6、标准审阅、仅报告。后续若有代码或勘误解释流身份/attention mask，可定点重开；不否定双流数学对象与作者局部实验。

## `2604.20933v1` IRIS：理论主张收窄后仅报告

[官方正文 §3.1–3.3、Appendix B、§4](https://arxiv.org/html/2604.20933v1)的 self-play objective 分别对 real/synthetic 样本赋 log-ratio 权重，随 Rényi order 改变更新权重；这不是通常的 chosen/rejected pair label。作者稿 Eq8 在 `α→1` 时 synthetic weight 含 `pθ/pold`，一般不趋 uniform；Appendix B.1 对 `0<α<1` 的一个指数不等号方向有误。后者的具体反例和可保留的 fixed-point 边界已写在 `V3_EVIDENCE_NOTES.md`，不能因此否定整篇经验结果。所测是固定 target、单轮生成、至多 7B、启发式 order 调度，不证明在线目标收敛。`TRAIN-RLHF`/`TRAIN-GRPO` 已有偏好目标和 reward/reference 分权；在公式勘误及可复用的 objective 条件未确定前，不把“统一自对弈散度”写成书稿结论。维持 2+2+2=6、深入审阅、仅报告；若精确公式或实现补充澄清再定点重开。

## `2604.20911v1` Omission Constraints Decay：格式 proxy 不升级成安全阈值

[官方正文 §2–4.5](https://arxiv.org/html/2604.20911v1)观察有限模型在长对话里省略类格式规则比追加类规则更易失效，并以六个采样深度插值出所谓 Safe Turn Depth。§4.5 明言八条均为格式 proxy，凭据泄漏等语义安全规则未测试；自强化混杂、Arm C 覆盖和每轮 token 差异也限制了因果归因。论文建议的重复注入/截断会增加 token 与维护成本，尚无对应生产安全验收。`AGENT-PROMPT` [第74章](../../../../../books/part-07-agent/74-prompt.md)和 `PLATFORM-SECURITY` [第72章](../../../../../books/part-06-ai-infrastructure/72-security.md)已将自然语言指令与外部权限分开；该结果是有用的受限反证，而不是可直接部署的安全 session 阈值或注意力机制证明。维持 2+2+2=6、深入审阅、仅报告；真实安全规则与独立防御验收出现时再比较。

本组没有 Books 写入，也没有把有限非作者核扩称全日完成。
