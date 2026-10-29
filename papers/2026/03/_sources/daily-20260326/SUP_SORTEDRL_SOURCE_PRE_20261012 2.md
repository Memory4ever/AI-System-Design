# SortedRL23414 exact-v1 — Source / PRE

作者supp_mar26_fresh，03-25自然日新增。首批准入/日级门已经supp_mar26_reader独校，原2+2+3=7不改。必要原证：https://arxiv.org/html/2603.23414v1 §3.1–3.3、§4.1–4.4/Table1/Fig5–6，实际读取；不审无关references/全附件。

## 源证与采用边界

§3不靠offline长度预测：oversubscribe→到阈值harvest completed/partial，group pool全部消费前不接新prompt，避免无限短轨迹优先。完全on-policy只保prompt，discard旧partial后重生成；partial保tokens及逐段真实behavior logprob，续写后拼接这些分母作importance ratio，不能把新policy重新评分当旧采样概率。对齐metadata与ratio只是可计算，不保证旧prefix无偏或稳定。

§4是LLaMA3.1-8B-Instruct/LogicRL Reinforce++、Qwen2.5-32B/DAPO-Math PPO，verl/SGLang补丁、H100/MI300X混合集群与96core CPU；各分支具体GPU数量/precision未披露，性能SLO不适用。512 samples/四batch/max8K且固定生成长度的Fig5是rollout throughput而非全训练成本；Figure bubble denominator是queue occupancy而非MFU。重生成、缓存、训练和评分均付费。

直接反侧：只harvest先完成样本的oversubscription ablation失败；group n→∞/n8损害质量，n2接近baseline；partial在LogicRL长度爆炸/退化。Math Table1的GSM8K baseline95.15高于onpolicy91.96，AMC partial63.05低于baseline63.13。§4.3叙述AIME三分支的数值顺序与Table1冲突，不能把正文排列直接当结果身份；只采用有界机制、明确反退，不采用普遍质量提升、无成本微课程、near40%全训练加速或strict-on-policy对所有算法保证。

## Owner差额

已完整读当前Books适用PROJECT_CONTEXT/学习/写作、ROADMAP与最新本日LS路由。Ch33『Partial Rollout』已有persistent prefix/policy/reward/terminal和staleness，却未在此处区分discard/restart与逐段真实behavior-prob恢复及finite pool anti-starvation；1435–1460的同步长度预测/complete-group，1532–1557 trajectory version窗口和相邻Ch32采样ratio定义保留。Ch34接偏好pair，不接管runtime。不是追加独立SortedRL摘要。

## 拟原文两段（未写，等待Source/PRE独核与root窄锁）

放在Ch33『Partial Rollout』现有最后段之后、『从Opaque Harness Call』之前：

这种暂停还须区分两条采样合同：只接纳当轮 current-policy 完整新轨迹的分支只保留未完成请求的 prompt，权重更新后丢弃旧 partial tokens 再生成；恢复分支则保留 tokens 与生成它们时的逐段 behavior log-prob，续写后把各段真正的采样分母拼回训练证据，不能用新 policy 重算旧前缀概率来冒充原采样路径。暂停/恢复解决资源长尾，逐段 ratio 只让混合版本轨迹的目标可计算，并不保证历史 prefix 的分布偏差或训练不稳定已经消除。<!-- source-family:SF-2026-ARXIV-2603-23414 -->

先完成先训练也会改变训练人口和 batch normalization：若不断补新短请求，慢 prompt 可能始终不能进入更新；有限 prompt pool 应在已接纳请求全部处理前限制新进入，资源队列长度与同题算法 group 仍是不同边界。[受限原证](https://arxiv.org/html/2603.23414v1#S3)中，单独 oversubscription、过大 grouping 和 partial 恢复都出现质量反退，数学任务亦非全面改善；重生成、缓存与更新成本不能由 bubble ratio 或 rollout tokens/s 抹去。长度接近、严格 on-policy、存储概率/恢复语义失配或质量没有独立通过时，回退完整同步 trajectory 或丢弃旧 partial 后重采，而不以更低 idle 批准改变训练分布。

本人静态来源注拟：`SortedRL arXiv:2603.23414v1 §3/§4.1–4.4/Table1/Fig5–6；只采用discard-vs-partial真实behavior分母与finite prompt pool接口，保LogicRL partial退化、grouping反退、GSM8K/AMC反侧及AIME叙述/Table身份冲突，混合集群不推全训练成本或普适on-policy保证；未复现。Source/PRE/写后独核状态依实际结果填写。`

上文PRE是写前快照。实际终点：reader/root必要Source→actual owner→修后两PRE通过，root授sole family窄锁；作者已按批准两段与纯静态本人注写，reader真实完整1996–2085、新2025/2027及本人3266来源注/邻注逐字POST通过并交root释放。未授本日日级DAY，不把此单篇接纳视为全日完成。
