# 2604.16090v1 AW-PSP：Ch36 最窄 Books 判断提案（作者侧，待独立采用）

## 实际 owner 与差额

[官方 exact-v1](https://arxiv.org/html/2604.16090v1) §2、§3.2–3.3、§4.2/Table 5 描述：设备 availability 与其非 IID 标签支持相关、多个设备又共同不可用时，受影响类别可整组缺席。作者并非只把快 worker 计入更多次；它指出单轮被选集合的支持集本身会变化。`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 现有 1137–1151 行把 worker sampling probability、arrival frequency、intended global weighting、stale direction 分开，能承载边际到达偏置，却没有明确“共同故障 × 类别支持”使单轮/有限时段的类别覆盖失效。仅凭现有到达频率段判为完整 Existing 或无须改变 Books，差一条条件性边界。

原分数仍是 `2+1+2=5`；由于此处提出真实长期知识缺口，按研究合同 §4 触发**只围绕该命题**的深入审阅与独立 source→owner 核，而不是把整篇升成 7 分或全附件队列。若该核通过，拟从原 Standard/Only 调整为 `Integrate`。建议在 Ch36 的边际频率校正段之后补最短两句：

> 按单 worker 到达频率重加权只校正已观察到的贡献；若共同故障让持有相近非 IID 数据的 worker 同时缺席，单轮或有限时段会失去整类支持，边际权重不能凭空恢复未观察到的梯度。同步/采样策略还须检查共同可用性；若协议允许取得适当的聚合标签统计，再分开报告被选数据的类别覆盖与缺失类分母。在支持不足时应延后聚合、调整参与集合或承认本轮只覆盖子目标，而非宣称无偏收敛。

这里的“不能”限于当轮没有该类数据、只对已到更新施权重的场景；若有充分长时覆盖、正的 inclusion probability 和恰当的联合设计，不能由本文断言任何总体估计都必然有偏。建议沿 Ch36 现有异步/同步并存链写，不采用论文的 EWMA/Markov/DHT 实现，也不把 FL 受限 ResNet/CIFAR-10 模拟外推 LLM 集群。该句是本项目对原文现象的条件性系统推论，不是论文给出的普适定理。

源中 §4.2 的 selector 直接按可见类别最大化覆盖；这不等于所有 federated/private-data 协议都能向 coordinator 暴露客户标签。若只有可用性 trace 而无允许的类别统计，正文只能明确“本轮类别覆盖不可证”，不能把类别感知重排写成默认可执行建议。上述报告口径还需分别保留作者的 selected-label accuracy、未见类别数与 client-participation Gini，不以后一指标代替类别公平。

## 必须随写入保留的反证与评价边界

- §3.3 Eq.15 用 `(1−ρ)` 调 sampling probability，却未在所读主文交代 `ρ` 的全部 clamp/归一合法条件；不把该式作为可直接运行的生产策略。
- §2 的10个实际 worker、§4.2.4 单机分波模拟100–3000逻辑 clients，不证明千设备真实同步或生产吞吐。
- 准确率计算只覆盖所选标签；缺失类另计，不能把 covered-label accuracy 当全标签质量。Table 5 噪声 c0→c40 下本法33.75→29.78（−11.8%）相对降幅大于 PSP 27.85→26.84（−3.6%），不采“所有维度更 robust”。
- §4.2.3 Gini 式的对象是 client participation，邻近文字又解释为 class representation；不以此指标证明类别公平。

此为作者侧 source→actual-owner 提案，不是独立采用、真实 Books 写后或 04/20 日级 Gate。共享 Ch36 写入需 root 协调窄锁；在此之前 README 仍保持既有处置，不计新的 Integrate 数。

## 后续实际结果（上文为历史提案态）

root 已按必要原文和 Ch36 邻接取得窄写锁、实际写入共同故障×非 IID 类别支持的条件边界，并更新章末 Review；[apr01 的非书稿作者真实写后核](./V3_APR01_AWPSP_CH36_WRITE_AFTER_INDEPENDENT.md)再读官方 exact-v1 §3.2–3.3/§4.2/Table5、正文前后及 Review，明确 PASS。正式日报现将 16090 计为已落地整合；原5分不变，深入只围绕真实 Books 缺口。这不等于日期、十四来源、其他候选或本日独立 Gate 通过。
