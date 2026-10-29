# Jun03 MODEL尾三项必要层与实际owner差额

只用Jun02 BJT首公开已通过的exact-v1；不新增发现池。当前官方abs有限notice核三项均只见v1、未见withdrawn/removed/erratum，不能据此保证全网无更正。本文未核代码、图像素或复现。00467/R179及另外三项已同步Report127＝99I/20NC/4Only/1close/3争议；本包尚未正式采用，不预I。源自己的增量按状态→决策→执行闭环校准，不以GPU/owner关键词或一般“cache有成本”准入。

## 01839 ConServe — 必要完成，Ch56原组中单段差额提案

[v1](https://arxiv.org/html/2606.01839v1) / [原件](SUP_CLOSE_2606.01839v1_20261025.html)。实际读§2–5、§4.1容量式、全部实验设置与反侧；未核图像素/代码。3+2+2=7提案：不是泛会话pinning，而是**首turn长prefill/后续追加的可测相位差，选择一次transfer后本地append，而非每turn预测迁移**。实际Ch56“Conversation Placement用已观察状态替代逐Turn预测”完整两段目前承担冻结placement、KV收据、热点/tenant skew与迁移失败，但未交代首次prefill分离和两个观测量如何形成这条分支，更未限定所谓predict-free只到placement而非容量规划。

SWE-bench/swe-agent轨迹由Qwen3-Coder-30B生成却在Qwen3-.6B bf16、4A40回放，不是30B真实端到端Agent。1prefiller/3decoders故意overprovision后者令prefiller先饱和；容量式N·Td≥R·Ld及N·B≥R·W仍须profile平均decode、驻留时间/峰值KV，不能授任意流量无预测。首输入长度→prefill曲线离线profile，完成后按当前活会话KV占用选decoder，后续不再逐turn判断；tool wait仍属活会话占用，不是free memory。No future-turn model不等no workload assumption。

AMPD为best-effort模拟双向transfer stall并后处理trace，主图人为10%错误、0%时与ConServe一致；不能说击败最佳真实AMPD。Poisson .5–1.5与1.634人工精确饱和分开；5×unbatched SLO为局部定义。FullPD最后turn TBT比ConServe更低（1.35vs2.49基线），不能全指标优越；51.08% p95TTFET属上述AMPD设定。所谓heterogeneous只同A40的300→200W powercap，不是实测旧架构；tokens/J固定回放无任务质量/生产SLO。全部曲线profile、驻留/transfer、append争用和tool工作计费。

唯一`INFER-SCHEDULING` / [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)。拟在Conversation Placement首完整段结束“runtime/cache owner仍拥有真实KV和完成状态。”之后、现“pinning减少预测误差…”完整段之前增加以下一段；其余不拆，尚未写Books：

> 这条分支还依赖会话内的实际相位差，而非只把pinning周期拉长。若首次输入很长、后续只追加少量tool结果，可把首turn送到prefiller，完成一次KV交接后才按当前活会话KV占用选decoder，并让后续append与decode留在该处；首输入的离线prefill曲线回答入口负载，KV占用回答长期驻留压力，等待tool的活会话也不能从后者消失。[受限ConServe回放](https://arxiv.org/html/2606.01839v1#S4)支持这一机制，但其decoder有意过配、对照的逐turn误路由是模拟设定，容量规划仍依赖decode/驻留profile，不是任意流量无需估计；全分离还可取得更低最后turn TBT。长append、驻留偏斜或prefill/decode容量失衡时，应重验split与admission，保留collocated或逐turn迁移，而不由较低会话TTFET批准所有tail指标。<!-- source-family:SF-2026-ARXIV-2606-01839 -->

## 01065 Leyline — 必要完成，具体NC提案

[v1](https://arxiv.org/html/2606.01065v1) / [原件](SUP_CLOSE_2606.01065v1_20261025.html)。实际读§2–8/Limitations、T2、责任清单C1–4；只用正文所需边界，不宣读完A–W/代码。2+2+2=6提案：增量是span/replacement/mode接口把policy意图与cache变换解耦，非把成熟RoPE旋转本身认作新方法。`amortize`删除直接KV可见行、保留后继旧Knope/V及旧影响、只旋转Kpe；`forget`走prefix-trimmed完整后继re-prefill。前者明确不是以stub替换后的prefill等价，更不能保证始终等于完整旧prompt：直接可读原行已不存在，本文有限argmax/工具名agreement非完整分布证明。RoPE pairing、signed delta、多edit顺序、radix slot引用寿命与prefix身份是执行资格，不是语义忘记。

正文48/50 first-token与不同模型common-prefix强退化不删；near-tie/bf16不替所有分歧免责。§5政策gain在**标准re-prefill**两臂，kernel另是synthetic/trace微基准，不能把14.3pp归splice或声称组成ablation已做。T2行加总为baseline10/32、treatment14/32，文字15/33包括额外counter；不能把表Overall当同一对称N的人口。并发/tenant扩展多处candidate=0、warm-start可能加驻留，已复用KV字节不是峰内存下降；已有prefix很友好时0.6%更慢。单阈值/4seed/八任务、不同H100/H200/模型配置及所有diff、rotation、重算/查找、warmup/校验费保留，不采用“production scale”等生产保证。

实际完整读Ch45“Token Replay Identity必须包含KV Construction Path”三段：首段绑定construction provenance；第二段明确append/drop/repos顺序、旧hidden影响、drop非隐私删除、K旋转非删减文本重prefill；第三段绑定copy-on-write/引用回收/分段query恢复及不兼容fallback。另读局部编辑repair三种决定和非prefix位置修复组。现文已经具体承担本文可支持的长期语义选择：**保旧影响的cache mutation与真正删减文本re-prefill分两条合同**，并非仅泛“缓存应正确”。span接口/新命名不产生额外机制owner，故拟标准完成、已有覆盖，不写Books。PIN/SHARE/跨instance/RDMA议程未由本文实测自动准入。

## 00866 MORI — 必要完成，Ch45原组中单段差额提案

[v1](https://arxiv.org/html/2606.00866v1) / [原件](SUP_CLOSE_2606.00866v1_20261025.html)。实际读§3–7、Eq1/T1–2与全部设置/反侧；2+2+2=6提案。实际Ch45“Agent Idle Window要按Program Horizon决定Tier”完整两段已承担相对空闲排序/GPU CPU双tier admission、transferfence与预测/公平成本，但尚未承担**测量剔除scheduler自造等待，program标签在GPU/CPU必须用相反保留次序落到block LRU**，否则同一排序不会成为一致物理策略。

k5近期acting/(reasoning+acting)，包含ongoing tool elapsed但明确排除gating等待；5s tick/sticky仅容量失配迁移。瞬时Acting不等长期idle phase。GPU优先淘汰inactive→idle→busy，CPU反为inactive→busy→idle，同type再LRU；Reasoning victim当前step结束才lazy demote，CPU affinity与GPU affinity不同。Promotionpriority先已完成tool的CPU，再返回waiting，再新到达，不能简化为全池纯idleness排序。论文把“Best-Fit-Decreasing”同时写选最多空位，不据此补唯一binpackrecipe。

SGLang.5.10/ThunderAgent/HiCache；186/200 Claude Sonnet4.6 SWEbenchPro完整trace，14 rate-limit/timeout排除，不能由“avoid bias”证明无选择偏差。闭环20/50/80每DP slot、一小时固定(input/output length,toolgap)回放，非重跑真实自由生成/任务成功。H20080GB为cap模拟容量而非真实H100；Qwen2.5-7B、Qwen3-30B MoE单卡，B200 Llama70B TP2，另H200 DP3；CPU:GPU容量1/2倍。Table2标50program而正文80不齐，21.5→23.8ms只保局部CPU开销，不授全部关键路径免费。原文称单调136→191→189实有退，低并发差距约2%、完整trace质量/precision/tail未齐均保。SSD/RDMA/heterogeneous是未来，不冒部署。所有timing、控制loop、block标签、transfer、CPU容量/affinity、重算/回归计费。

唯一`INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。拟在既有首段结束“scheduler只读取residency与代价，不拥有page真值。”之后、现“这种分层减少长期等待占用HBM…”成本段之前补以下一段，保既有两段；尚未写Books：

> 相对空闲度还必须避免由控制器自己制造：可用近期tool等待占实际tool等待与推理时间的比例作phase代理，但将scheduler的gating/排队时间排除，不能把被延迟的程序反过来判成天然不活跃。[MORI受限回放](https://arxiv.org/html/2606.00866v1#S4)把program placement的busy/idle/inactive标签传到KV树节点，在GPU优先保busy、在CPU优先保idle，同类再用LRU；两层若沿同一优先序独立淘汰，就会驱逐上层刚交下来的状态。进行中推理先到安全step边界再迁移，CPU-resident状态也参与replica affinity。这个反向保留次序不取消实际容量/transferfence，也不证明短期phase代理准确；其闭环trace吞吐与平均TTFT不是自由生成质量或tail保证，phase反转、控制延迟或容量不合适时仍回到原no-move/LRU与重新验收的admission。<!-- source-family:SF-2026-ARXIV-2606-00866 -->

## 交付

三项ready交root第一次必要/actual owner独核；只请求上述Ch56、Ch45各单段/本人注的具体位置。NC不是工作量或篇数配额所致，I也不由owner存在自动授予。原MODEL18已全部有必要小批，batch2–4及本批尚待独核/实际写后；定义02358/00289和CRAM02502/ProtoAda02576仍普通。有限stop另准备、不扩池。
