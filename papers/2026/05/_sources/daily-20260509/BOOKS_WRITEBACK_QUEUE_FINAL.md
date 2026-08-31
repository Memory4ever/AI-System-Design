# 2026-05-09 Books Writeback Queue — Final Prewrite Challenge

状态：`Root-serialized / not written`。独立 current-content challenge 将 21 项 evidence-complete provisional Integrate 收紧为 **3 项**；其余 18 项均由当前 Books 主线完整承载。本文件不表示 Books 已修改。

## Owner-merged narrative

三项只形成一条 `TRAIN-DISTRIBUTED-TRAINING` 演进链：训练通信最初把 payload 当作无类型 bytes；规模、异构拓扑与解耦 rollout 使真正需要维护的是 **typed communication state**。policy 发布应绑定 base checkpoint、稀疏 update、target epoch 与重构验证；Context Parallel plan 应绑定 sequence/head ownership、topology、buffer 与 plan epoch；loss recovery 应理解 collective message/round ownership，但仍保持 exact completion 和可靠 fallback。三者不能被写成三个产品段落。

| Source Family | Durable delta | Required boundary |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-07330` | Trainer→Rollout 从完整 weight copy 演进为可验证重构的 sparse policy update。 | 稀疏性漂移、index/bucket/control overhead 或重构失败时回退完整 snapshot；不外推作者压缩率。 |
| `SF-2026-ARXIV-2605-08524` | CP 从固定 All-to-All 演进为 topology-aware fully-connected exchange plan。 | fabric/buffer/ordering/plan epoch 不满足时回退规则 collective；不外推特定 topology throughput。 |
| `SF-2026-ARXIV-2606-20582` | recovery 从 transport-byte retransmit 演进为 collective-semantic-aware round recovery。 | 语义/round identity 不完整、loss 超界或恢复证据不足时回退可靠重传/整轮 retry；模拟不构成生产 tail 保证。 |

## No Change closure

其余 18 项的逐 family current-content comparison 位于 `books-current-content-comparison.json` 与 `books-prewrite-challenge.json`。它们不是低分或被忽略，而是经 owner+adjacent 重读后判定现有正文已覆盖长期机制。
