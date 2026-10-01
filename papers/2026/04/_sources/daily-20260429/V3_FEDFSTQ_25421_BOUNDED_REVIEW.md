# 2604.25421v1 FED-FSTQ：本日作者必要证据与印刷数值审阅

按 [官方 exact-v1 HTML](https://arxiv.org/html/2604.25421v1) 的 §III-C／IV-A–E、§V-B–D、§VI-A–E 以及真实 Ch30/36 命题定点审阅；旧日报的 `9/deep_complete/No Change` 不自动继承。此项在现有 70 个潜在线索之内，不新增分母。日期仍沿本日 arXiv 公告联合链，若有早于 arXiv 的独立正式首发另核。

## 贡献与有效证据

联邦 LoRA 的每轮上行压缩不能仅最小化 byte 数：非 IID 客户端上的稀有负词/代码分隔符若被压掉，固定精度压缩会改写训练贡献。作者先以 token embedding loss gradient 平方形成 sensitivity，按 token mask 过滤本地损失，再把所得 adapter 参数梯度平方 EMA 与本轮 `Δθ²` 相乘得到逐参数 importance；在 `{0,2,4,16}` bits 中选稀疏/混合精度，并上传 index、bit tags、scale 与 value。这是 token evidence 影响**参数更新传输**的耦合，不是直接把 token 本身发往服务器。Table VII 的 Fed-Med matched `150MB/round` 下，round50 ROUGE-L `36.15` vs uniform-Fisher `31.50` vs random support `18.05`，且关闭了 inference-time pruning；可作为受限机制证据，但不能单独证明任意数据上的最佳位分配。

建议 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，Standard **基础评分**；由于下列印刷中央系统数字冲突，按实际 conflict override 对速度/能耗/资源可行性部分深入、窄 `Disputed`，并非论文所有机制无效。Ch36 当前已具体规定通信压缩须计 codec critical path、matched convergence 与端侧资源；Ch30 已写 DP federated LoRA 的选择器/会计状态。若数值争议未释，最稳的 Books 决策是 **No Change — Existing Coverage／争议暂缓新整合**，不把可疑倍率或“2GB 可部署”写入长期知识。真有超过 Ch36 的非同义条件，需非作者 source→owner 先定点裁决。

## 直接可算的中央冲突（只隔离相应保证）

1. §V-C 将 Table II 的受控配置明定 `R=20 Mbps` 且 `T_comm=bits/R`。Table II 对 FedAvg `1024MB→409.60s` 恰合 `1024×8/20`，对 FED-FSTQ 却列 `153.60MB→55.20s`，同式应是 **61.44s**（若 MiB 口径更长），而 `55.20s` 隐含 `138MB` payload 或 `≈22.26 Mbps`。其总计 `55.20+5.85=61.05s` 虽内部相加正确，基于表列 payload 与协议应为 **67.29s**，相对 FedAvg `414.60s` 是约 **6.16×** 而不是其 headline 6.8×。不能仅凭印刷表签“受控 20 Mbps 下 6.8×”；不推断原代码实际运行或其它异构链路实验必错。
2. 同一 §V-C 默认 `P_tx=2W`、通信能量 `E_comm=P_tx×T_comm`。Table II 的 FED-FSTQ `T_comm=55.20s` 使**仅通信**已有 `110.40J`，却报告总 `98.50J`，不可能与正的 compute energy 同时成立；Table III 对 `2W` 的 FED-FSTQ 总能量又报 `133.80J`。FedAvg 在 Table II 是 `634.40J`、Table III `2W` 是 `839.20J`。因此“sub-100J per round”与默认 radio model/两张表不能同时作为已验证系统数字。Table II 的 energy summary（平均或 straggler）也未在其 caption 精确标注，进一步限制比较。
3. §V-D 指定 Llama-2-7B/Llama-3-8B、QLoRA-style 4-bit backbone、Jetson Orin Nano 8GB，却以 Table V `1450MB` 称 FED-FSTQ 在 **2GB IoT/Mobile** 完整运行。仅 7B 权重的理想 4 bit 存储下界就约 `3.5GB`（未计 scale、LoRA、activation、optimizer）。若 Table V 只计某 buffer，论文须明确 offload/分片或计量范围；在印刷身份下不能把 `1450MB` 解释为全模型端侧峰值。此只隔离完整设备可行性 headline，不否定稀疏消息本身可小于 2GB。
4. §IV-E Algorithm 1 将 mask `z_i` 对一 minibatch 的 token positions 做 TopK，随后跨下一批样本的 `H` steps 重用，而新 batch 的 token 身份／长度可变；印刷算法未说明跨 batch remap 或 mask refresh 对齐语义。不能凭此断言实现实际错，但“保留稀有语义 token”的**具体控制路径**仍需源码/配置与对照释疑。§IV-D 声称可组合 secure aggregation／DP，§VI 说明两者只作部署背景且未来才强化相关 metadata/packing/privacy；因此不能写成已验证隐私兼容，更不能从 FedAvg 加权式直接推密码协议成立。

## 保留与停止条件

可以保留 Table VII matched-budget 的局部 ROUGE-L 对照、Table VIII 的 token recall（它按 uncompressed Fisher top-p 定义，非独立人类语义 truth）、Table IX 的受限 Fed-Med quality，以及通信瓶颈下必须比较固定目标质量的**原则**。但 `46× cumulative uplink`、`52% time-to-accuracy` 分属异构虚拟链路与质量轨迹，不等于 Table II 单轮倍率；上述中央印刷矛盾使绝对能量/内存/受控单轮速度不能作 Books 正面数字。只读决定性原文已经足以具名隔离这些保证；不要求复现全部实验，不称真实实现故障。

下一步：请 root/非作者就算式与 Ch36 实际 owner 作有限核；若官方 exact-v1 或原始作者 artifact 给出 `153.6MB`、`55.2s`、`98.5J` 和 2GB 全模型的同一协议分账，才重开相应保证。未写共享 Books、未签日级 Gate。
