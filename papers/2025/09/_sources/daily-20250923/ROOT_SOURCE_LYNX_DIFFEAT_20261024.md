# Sep23 补 Sep22：Lynx / Diff-Feat 必要证据首包

## 范围与角色

作者 A33 明示两项尚未开始必要 Source；root 明确接受后，作者 A36 确认互斥让域。这里只准备两个原 5 分命题的必要机制、直接对照、费用与关键反侧，不改日期、评分、候选表或 Books，不代 owner 判断。AB/N 与 R16 日门有效复用，不第三初筛；准备完成后由作者回原件一次实际采用，Sartre 复用此角色结果，不再第三 Source。

两次唯一精确 v1 HTML 请求均已实际 exit0/HTTP200，独立原件与请求记录保存，无在途：

| 材料 | 实际请求 UTC | 原件/回执 | 字节 / SHA256 |
| --- | --- | --- | --- |
| [Lynx v1](https://arxiv.org/html/2509.15496v1) | 2026-10-23T22:09:51.177220+00:00 | [raw](./SUP_curl-ROOT_CORE_LYNX_20261024_20261012.raw) / [request](./SUP_curl-ROOT_CORE_LYNX_20261024_20261012.request.json) | 137867 / `e92b0420f69932c3648472edf7de9d04235bedfb7f51d29c6275a080104a6bbf` |
| [Diff-Feat v1](https://arxiv.org/html/2509.15553v1) | 2026-10-23T22:09:51.739282+00:00 | [raw](./SUP_curl-ROOT_CORE_DIFFEAT_20261024_20261012.raw) / [request](./SUP_curl-ROOT_CORE_DIFFEAT_20261024_20261012.request.json) | 409049 / `18d7fcac71f12dc6ef0f74192f3ea293f04878aee67794c50fc4aeaabc76bed3` |

文件名末尾 20261012 来自已有 capture 工具命名，不是实际请求日期；采用上表与回执原字段。字节/SHA/status/exit_code 已实际复算匹配。HTML 用结构化 section/MathML alttext 读取，不把公式的重复视觉渲染当不同公式。没有核代码、复现实验或看全部示例图/视频像素；这些不作为本次有限命题的缺口配额。

## Lynx：两类条件的 producer 与访问接口

实际完整读 §3.1–3.2.2、§4、§5.1–5.3/完整 Tables1–2 与必要图注、§6；另定点核 §1 架构说明。拟命题只是在视频个性化中区分紧凑身份与 dense 参考细节的 producer/consumer，不认证身份永远不漂移或两组件独立优越。

底座为 Wan2.1 DiT/Flow Matching：普通 block 先时空 self-attention，再消费文本 cross-attention。ID-adapter 由 ArcFace 派生 512 维 face vector，经 Perceiver Resampler 成 16 个 5120 维 tokens，再与 16 个 register tokens 拼接；新增 cross-attention 后加回主分支。不能把脸向量、16 个可读条件和完整参考特征当同一个压缩对象。

Ref-adapter 不只是把 VAE feature 直接放在 noisy latents 前：参考图经 VAE 后，再由冻结的底座副本在 noise=0、固定 `image of a face` 条件下产生每层参考 activations；每层各有独立 cross-attention 消费对应参考 tokens。冻结指这一 reference pathway，不由描述补造所有训练参数清单；adapter-based 而非 full-model finetune，也不等没有第二份 backbone 权重/参考前向/activation 费用。该设计沿既有 identity adapter / ReferenceNet 思想，不能为借用成熟原理另计突破。

训练还改变了数据与初始化：每样本独立 3D-RoPE 与 attention mask 后，把不同尺寸/长度的视频 tokens pack 到长序列。物理拼接不允许跨样本 attention，不等任意混合样本语义；原文没有完整吞吐/显存 matched 测量。单图当单帧；从零训练 Resampler 长时间无明显面部相似，改用 InstantID 图域初始化后约 10k iterations 有可辨相似，首阶段共 40k；仅图训练常静态，第二阶段视频训练 60k。10k 是观察，不是达到同一质量目标的速度对照或任意模型收敛保证。

§4 总计 50.2M pairs：21.5M single-scene、7.7M multi-scene、21.0M augmented single-scene。X-Nemo 表情编辑、LBM 重照明/背景、同人 face similarity 过滤与 weighted sampling 都是额外监督/选择。合成表情、同一 recognition family 的过滤与评价不能自动成为独立 identity truth；多场景稀缺/裁脸导致表情照明过拟合是设计约束，不由数据量证明已消除。

评价为 40 subjects × 20 prompts = 800 test videos：10 celebrity、10 AI portraits、20 in-house licensed；GPT-4o 产 prompts 的“unbiased”是作者意图，不是已验证人口公平。三种 face cosine 分别 facexlib、insightface、in-house，另 Gemini-2.5-Pro 对 prompt/aesthetic/motion/overall video 评分，不把多个 proxy 当真实身份、动作或独立人审。Table1 Lynx .779/.699/.781 高于所列方法；Table2 prompt .722、aesthetic .871、video .956 为最高，但 motion .837 低于 VACE .851。文字“四个指标中四出五”与实际四列/三项最高不一致，按原表保反侧，不照录所有维度最佳。

没有逐组件删去 ID/Ref、匹配 50.2M 数据/初始化/训练预算的直接消融，也无相同预算下 freeze 副本与直接注入的隔离对照。因此完整系统优势不能唯一归因两通道互补，no facial resemblance 等训练描述也不补成量化因果。必要域未披完整 base size、hardware、precision、batch、分辨率/输出长度、sampling steps、重复 seeds/CI、逐请求参考处理与生成 walltime 或并发/SLO；不能由“lightweight adapters”批准端到端省时/省显存。

全部数据收集/授权、编辑/过滤/加权、初始化来源、两阶段训练、reference backbone/activations、两类 cross-attention、完整视频采样与独立评价都计费。有限机制可作为条件访问分支继续 owner 对照，原 2+1+2=5 保持；不要求读无关引用/全像素来证明未采用的通用身份保证，不预 NC/I。

## Diff-Feat：读出位置与噪声不是统一的表示资格

实际完整读 §3.1–3.3/Algorithm1/公式，§4.1–4.3/完整 Tables1–2、§5–6，以及必要 A/B/D/G、A5–A6 的完整 Tables5–6 和 A9 输入长度协议。只为反侧补这些域，不遍历 C/H/J 全部图表、所有像素或代码。拟命题为同一 pretrained diffusion 的 block×timestep 读出依赖 modality 与 classifier consumer，不认证通用“第12层最语义”或融合必优。

图侧为 null class 的 DiT-XL/2，28 layers/width1152/16 heads，256² ImageNet pretrained 与 SD VAE/8× downsample；文侧为 Plaid 1B（实际约1.3B），24 layers/width2048。特征冻结后以 BCE/CE 训练单层 classifier；若融合另训练 projection/fusion，不能把没有 finetune backbone 叫没有训练。每模态单独扫描 timestep/block，再在单模态 optimum 的邻域搜融合，O(|T||B|) 只是固定邻域相对全笛卡尔 O(|T|²|B|²) 的评价配置数量，不是免 probe 训练/全 pipeline 时间，更不保证全局 optimum。

原 mAP 表支持有限读出差异：Table5 图侧 (50,12)=60.48，(50,24)=46.86；文侧 t0/b24=93.41，而 t0/b8=82.51，t30/b24=92.36。最优融合使用文 b20 而非单模态 b24，(image30/12,text0/20)=98.57，换 text0/24 为98.09；VG500 同一图30/12却以文0/24为45.71，高于文0/20的45.30。不能把单模态局部 optimum 自动等于组合 optimum，也不能把 layer12 解释成已证因果模块。A7 明示仅离散扫描，未穷举10–11/13–15层，深层“overfit”只是解释假设。

严格单调/所有指标共享趋势也不成立：Table5 text b8 的 OR 在 t0/10/20 为61.24/61.27/61.40，CF1从62.05升62.11；Table6 b8 mAP t0=25.23、t10=25.24。Table5图b20的mAP到t100仍增长而b12更早见峰。有限小差未给独立训练 CI，不夸大成显著反转；但正文的全指标严格 monotonic 不能作为定律。A9 明示 text length45 更好而主协议选60，VG500用600并改投影维2048；长度/截断、modality 与 fusion width 必须一并绑定。

**关键输入权限反侧：** A 明确为 MS-COCO 每图 caption 追加所有 gold category names，并对 rare labels 再强调。§4 在无 test gold 下把 validation 当最终评价，未声明该 augmentation 只用于训练，更未交独立不含标签的同人口 matched 对照；Table1 一边 MS-COCO image-only 旧方法，另一边 MS-COCO-enhanced 的 image+augmented-text。作者说“aim is not label leakage”不消除 gold-derived answer-bearing input。98.6% 不能当普通只看图的无标签泛化/公平 state-of-the-art，也不能唯一归因 diffusion 表示或 fusion。A9 只说长度分布由 train统计，不自动修复最终输入 gold 权限。这里保留精确可见协议，不猜代码额外泄漏或宣称所有结果作废。

VG500 文本为已有 region descriptions 的拼接，非同一 gold-name追加方式；仍有第二模态额外信息/600 tokens/不同 projection。Table2 的45.7不是对 image-only baseline 的同输入预算纯架构因果；有限数据的 modality-specific 读出观察可以保留，不借 VG 解除 COCO 权限问题。全模型反证与局部可用命题须分责，不用改低5分/删候选来避开。

融合式按 column vector h∈R^(d×1) 书写，而给出的 QKᵀ 形成 channel×channel 对象，不足单凭该式认定标准 token-axis cross-attention；不替作者补序列形状。Table3/训练 loss 曲线只能比较所测收敛，不授最优融合/语义对齐。A4 确定/随机 noising 的 t-test 以配置成对比较，未给独立训练重复；同一数据/层/时刻相关，不能把14.75/p<.001推广独立复验或普遍文本加噪规律。噪声“deterministic/DDIM”叙述本身亦不提供可执行全部 forward recipe。

§4 classifier Adam/lr1e-3/cosine40epochs/batch128，实验4×RTX4090/DDP/AMP；A/B 只给单4090 image batch128时363.52 samples/s、text batch64时104.32，两个 workload/batch不同，既非融合吞吐，也不含全部 offline grid/probe。完整 extraction、VAE/两个 pretrained artifacts、所有层时刻候选、projection/fusion/40epoch classifier、标注/文本构造、选择/独立最终测试都付费。未披全搜索 walltime/缓存与部署 latency/concurrency/SLO，不从渐近搜索数或部分 extraction rate 签服务加速。

标准必要支持与关键反侧已足，原 2+1+2=5 保持。可支持的只是经过上述输入/搜索权限限定的读出选择与融合消费者差异；金标辅助协议下的高分、全局最优/普遍严格单调/公平因果性能不获采用。owner、具体 No Change/整合或中心未决须由作者对当前正文继续判断，不在本首包预签，更不代本日 DAY/FINAL。
