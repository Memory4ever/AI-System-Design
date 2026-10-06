# 2610.02665v1 独立必要证据与 owner 差额复核

复核者：oct04_daily（非本项主作者、非拟 Ch24 写入者）。检查时间：2026-10-05T16:25:15+08:00。
范围：仅 Large Language Continuous Diffusion Models 的 embedding/readout、必要低 NFE/高阶 ODE 反侧及 Ch24 现有论点/相邻 owner；不扩池、不比较旧版、不改 Books。结论是来源与拟差额 PRE，不是实际写后 POST 或 Daily 总 Gate。

## 必要原源与独立结论

原源：[2610.02665v1 HTML](https://arxiv.org/html/2610.02665v1)。实际阅读 §2、§3.1/3.2、§4.1、§5.1–5.3、App B，以及定点 G7 的设置、Table 16 和几何诊断。主作者保存的必要切片是 [a](cl-core-2610.02665-a.json)、[b](cl-core-2610.02665-b.json)、[few-step](cl-2610.02665-c.json)、[limits](cl-2610.02665-limits.json)；独立补取 [G7 设置与 Table 16](independent-02665-ode-setup.json)、[G7 反侧与诊断](independent-02665-ode-counter.json)。这些是作者公开机制和实验，不是本地复现或生产验收。

- §2 的 `e=xE` 是 token embedding lookup，E 行约束在单位球面；Gaussian corruption 作用于连续 embedding。`x_theta` 输出每位置的 V 类别分布，`x_theta E` 是连续 posterior-mean embedding。§3.2 实际使用 16D diffusion embedding、另一个干净 AR embedding stream 与独立 readout head。它不是图像 VAE encoder/decoder，也不能因为 NELBO/variational diffusion 名称就等同 VAE codec。App B 的 VAE-style readout pretraining 仍是未来建议。
- §3.1/§4.1 自回归组织 block，当前 block 内连续联合去噪，已提交的干净 prefix 用 AR embedding 和 causal KV 跨步复用；最终类别 readout 后才能进入 committed prefix。不是全响应同时完成，也不是 masked diffusion 在中间步骤按部分 token unmask 的同一 commit 合同。
- §5/App B 保留 DDIM-4/8 相对 DDPM-256 的明显质量损失；embedding 几何正则与 PDD 有局部帮助，不给充分质量恢复或统一端到端加速保证。当前 PDD teacher 关闭 self-conditioning；如何蒸馏 self-conditioned model 仍未解决。少步、强 guidance、distillation 的连续端点可能离开 readout 的训练分布；clean final embedding 为主的 readout 训练是作者给出的瓶颈诊断。
- G7 固定 Sigma-3B、block32、uniform-gamma、SC on，并沿用 DDIM 选出的 CFG/ST（8-step w=3/tau=.8，16-step w=3/tau=.5），不是每个 solver 独立最优调参。对比匹配采样 loop 的 8/16 次 denoiser 调用；加最后类别 argmax 求值为总 NFE 9/17。midpoint 两次求值/transition，不能把 outer transition 数当成调用数。每题十个 responses，表内 mean±2SE。高阶没有稳定优势这一局部负证据成立；不能推成高阶 ODE 普遍失败。
- G7 对相同 prompt/noise 的几何诊断以 DDIM-512 作数值参照，不是真实轨迹 oracle；低步数的 off-sphere 与最近 embedding cosine 是诊断代理。作者由此建议外推可能落到 clean embedding 流形之外、强 CFG/ST/SC 下有效场不够平滑；这是受限解释，不是已证明的唯一因果或全局流形定理。

§4.1 的最终 readout 叙述出现 `argmax(x_theta E)` 形式，依 §2 的 V→16D 维度不宜照录成 token ID 公式；拟正文采用“类别 logits/readout 后提交”，不把 mean embedding 的坐标 argmax 当成词表读出。

## 实际 owner 与最小差额

[ROADMAP](../../../../../ROADMAP.md) 的唯一 owner 是 `MULTIMODAL-GENERATIVE-PARADIGMS`，当前 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际读 Ch24 的 diffusion/DDPM 入口（119–158）、flow/solver 与 decoder 范围（173–205）、文本 masked/block commit（335–369）、全成本与 Output Decoder（989–1050），以及相邻 Ch23/Ch25 的 owner 入口。

Ch24 在 DDPM 前已要求固定数据空间，并允许像素或 latent；Output Decoder 段明确以“视频生成中 VAE decoder”为具体分支，未声称所有 latent 都经过 VAE。已有正文还承载 NFE≠wall-time、高阶/历史求解的适用条件、decoder 半径与质量边界。因此不得全局把 latent 替换成 VAE，也不需要重复通用求解器/成本段落。

建议仅新增两段语言生成条件分支，放在连续 diffusion 入口附近：

1. 从语言的稳定 prefix/离散输出约束解释为什么 continuous token embedding 是另一种 diffusion 数据空间：单位球面 token lookup、Gaussian corruption、当前 block 去噪、干净 AR prefix KV 复用、最终类别 readout 才 commit。明确这条路径不依赖图像 VAE codec，不替代已验收 AR 或 masked/block 分支。
2. 将少步预算与离散读出训练域相连：低 NFE 与强 steering 可能产生 readout 不熟悉的连续端点，局部 embedding regularization/PDD 不能消除质量和训练成本；高阶求解的局部反侧及最终读出额外调用保留。几何正则、指导、蒸馏训练、readout、KV 反复查询计入成本；质量/支持域失配时保留更多步、AR 或 masked 路径，不由低 NFE 宣告全流程加速。

这些是实际现有正文之外的具体差额，不是论文清单。Ch23 仍拥有一般表示/codec identity，Ch24 拥有本项生成状态与 readout/commit；Ch25 不接未来 multimodal/world-model 推测。已将以上结论与边界发送给 oct05_daily 和 root；实际写入与 POST 留给主作者和非作者复核。
