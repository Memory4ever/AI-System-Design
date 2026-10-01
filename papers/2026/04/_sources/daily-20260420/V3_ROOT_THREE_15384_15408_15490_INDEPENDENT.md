# 04/20 三项非作者必要证据与 owner 复核

本记录复核三项已入候选的必要官方 exact-v1 方法、反证及实际 owner，不替代这一天的日期、来源、其余单篇或负侧 Gate；论文数字仅按作者实验配置解释。

## 2604.15384v1 — LinuxArena

[官方 v1](https://arxiv.org/html/2604.15384v1) §3–6：20 个 Docker Compose 多服务环境包含合法 main tasks、恶意 side tasks；主任务能否完成、side-task capability、攻击成功与 monitor 识别分别计，不是单一“安全率”。Step-wise FPR 与整段 deployment 风险不同。LaStraj 的人类轨迹经过最多 8 小时构造及针对指定 monitor 的迭代；同任务/side-task 条件下比较 model 攻击还过滤为成功 side-task。结论只说明当前已激发模型攻击未饱和，不能把人工轨迹当最坏上界；合成数据、无 CI/CD/代码审批中介、有限环境及 scorer 干扰限制真实生产外推。当前 `PLATFORM-SECURITY` Ch72 已明确 generator、quality estimator、submission policy、attempt opportunity、audit budget 与“未充分激发仅为已见攻击下界”的合同。本项的实证是这条合同的高价值受限验证，但没有改变它；**7 分深入、Existing Coverage 成立**，不声称 Ch72 已收录整套 benchmark 或特定 GPT-5-nano 数字。

## 2604.15408v1 — Dispatch-Aware Ragged Attention

[官方 v1](https://arxiv.org/html/2604.15408v1) §III–V：DeiT 短、双向、无 KV attention 的 FA2 varlen API 有输出/workspace 与 pybind dispatch 路径；作者的 Triton 路径可避开部分包装，但 packed layout 也需要索引、copy 与 CPU 同步。Table II 将最低观测总时间当 floor 再减为 residual，不是独立仪表直接量出的纯 CPU 调度时间。核原文端到端对照：相对 FA2 varlen，在 batch≥32 两条 pipeline 收敛至约 1% 内，小 batch 是约 5–8% 差；相对 padded SDPA 才有最高 2.24×，分母不可互换。论文明确不实现 causal mask、dropout 或 KV-cache，不可把 pruned ViT 的速度搬到 LLM decode。当前 `INFER-TENSORRT-LLM` Ch49 已区分 launch-bound profile、TaxBreak 三层诊断、WebGPU 估计残差、device-bound fallback；该 paper 的受限执行点没有改变 owner 判断。**6 分标准、Existing Coverage 成立**，只采用 FLOPs/单 kernel/整请求不可混算的既有命题，不声称具体 ragged kernel 已写入 Books。

## 2604.15490v1 — Think Multilingual, Not Harder

[官方 v1](https://arxiv.org/html/2604.15490v1) §3–4/Appendix A.15：translation-only SFT 的训练样本将 reasoning 留空，随后受测模型的生成 trace 中 code-switch 行为指标也改变，支持“推理文本的语言行为不只受显式 reasoning-trace 监督影响”这个有限跨任务观察。其 token budget matched 不等样本数或语言质量 matched；不同 tokenizer、模型、语言与 teacher/filter 混杂，英文作为 matrix language 与准确率的联系不能外推为“必须英语思考”或“切换越多越好”，作者的 Integration Index 甚至呈反向关联。`TRAIN-SFT` 的监督目标与 trace 行为责任能容纳这项经验，但当前证据没有建立跨语种稳定训练配方、独立机制 owner 或足以改变现有设计结论的效果边界。**5 分标准、Only 成立**，保留局部现象，不强写 Books，也不因局部实验自动前关闭。
