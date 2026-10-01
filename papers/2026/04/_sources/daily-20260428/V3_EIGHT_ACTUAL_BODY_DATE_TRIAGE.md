# 04/28 八项已有 Books 正文的身份／日期定点对照（作者提案）

本页只对旧 111 `retained` 中已能在实际 Books 找到同 Source Family **机制正文**的八项做有界定位；不是仅用 `rg` 标记证明 Existing，也不是继承旧日报的评分/公开日。确切原文的必要方法与局限可复用各章 Review note，后续仍需非作者 source→body 复核、当窗日期与本日候选 Gate。未证明日期的条目不得因“书稿已写”而直接列正式 §3。

| Family | 实际知识 owner／正文承载的最小命题 | 尚未自动通过的边界 |
| --- | --- | --- |
| `2604.22981v1` | [Ch32 约 116 行](../../../../../books/part-04-training-system/32-ppo.md)：prefix score 是沿当前 continuation policy 的终局 reward proxy 条件期望；MC/TD coherence 不给过程正确性，off-policy 时回退 final-only。 | 本书已承载该机制，拟 `Existing Coverage` 而非重复写入；需独立比原文§方法/实验。receipt v1 Updated 00:08:18Z，日期仍靠公告槽组合而非此字段单证。 |
| `2604.23036v1` | [Ch21 约 625 行](../../../../../books/part-02-model/21-moe.md)：biased sparse routing 与 always-active gated condenser 分担长尾 expert 保留／共享巩固，保额外常驻成本。 | 拟 `Existing Coverage`，只限 GPT-OSS/DeepSeek MoE SFT；Updated 00:11:19Z 不是公告秒点。 |
| `2604.23073v1` | [Ch26 约 192 行](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：预训 VLA 的 RL token/小 actor–critic 局部动作更新与 human/controller authority 分离。 | 窄 `Existing Coverage` 的原文→正文已获 root 独立核验；[日期独立判定](./V3_ROOT_23073_DATE_BOUNDARY_INDEPENDENT.md)以官方公告规则、相邻 ID 和早字段有据推断 arXiv v1 落本窗 08～09，不把 OAI 05/04 后修订当首发，也不证明别处无更早全文。 |
| `2604.23080v1` | [Ch84 约 513–520 行](../../../../../books/part-07-agent/84-agent-platform.md)：node membership、agent warm/cold、routing overlay 与 cryptographic identity／权限分离，SimPy Kademlia/Gossip 的条件结果就近。 | 拟 `Existing Coverage`，不能以旧 V2.1 标签自动通过；Updated 00:13:56Z。 |
| `2604.23205v1` | [Ch72 约 122–132 行](../../../../../books/part-06-ai-infrastructure/72-security.md)：64B AXI burst 内联 AES-CTR 解密、plaintext 限制在隔离 NPU SRAM；静态 at-rest 不覆盖最后 ingress。 | 拟 `Existing Coverage`，proxy/idealized 评估不证明 fabricated NPU、物理侧信道或生产 SLO；Updated 00:25:07Z。 |
| `2604.23853v1` | [Ch69 约 221–234 行](../../../../../books/part-06-ai-infrastructure/69-trace.md)：child trace+逐步成本+rule type 的 TraceCard，preserve/prune/repair 须留行为与成本 receipt，不把启发式当因果。 | 拟 `Existing Coverage`；Updated **01:06:13Z** 已晚于 04/28T01Z 截点，当前 OAI 05/26 又受 later metadata 影响。必须查到先公告后更新的具体依据，否则 Date Hold，不可把已写正文倒推 04/28。 |
| `2604.23932v1` | [Ch36 约 352–363 行](../../../../../books/part-04-training-system/36-distributed-training.md)：长 RTT OTN 的 pseudo-ACK、segmented feedback 与 destination rate budget，错误预算回退常规 congestion control。 | 拟 `Existing Coverage`，ns-3/AICB 仿真非生产；Updated **01:10:56Z** 截点后。当前 OAI 04/28 单日记录不能证明 09:00 前公开，须日期例外。 |
| `2604.23987v1` | [Ch66 约 118–135 行](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：continual fine-tuning 后 model+task calibration artifact 一起版本化，accuracy 与 coverage 双 Gate，`m=200` 只限分类／MCQ。 | 拟 `Existing Coverage`，官方 pinned-v1 §4–8 与正文口径相符；Updated **01:13:56Z** 截点后，OAI 04/28 日精度不足以证明本窗，先核日期例外。 |

上述五条早字段与三条晚字段均位于原有连续 ID 工作段，不能据整段 ID、submitted、DOI created、OAI datestamp 任一单字段把八项一律写作 `08:00～09:00`。三条晚字段只在真正保留且有更早公开依据时回表，否则精确隔离。此表不改变 70/41 工作漏斗、88 上限或现有两项正式 Integrate；非作者若发现某章正文只是主题相近，应逐项撤回 Existing 提案，而不是增加相似摘要。

`.23073` 版本链定点补核：[官方 v1 摘要页](https://arxiv.org/abs/2604.23073v1)列 v1 submitted 04/24、后续 v2 04/30；旧 receipt 的当前 OAI datestamp 05/04 可能反映后修订，而非 v1 首次公告日。root 已在[有限独立日期审计](./V3_ROOT_23073_DATE_BOUNDARY_INDEPENDENT.md)综合官方公告槽、连续 23072/73/74 和 v1 早字段，将 **arXiv 路径**从 Date Hold 改为本窗 08～09 的有据推断；不是精确逐篇日志，也不排除同族其它平台更早公开。
