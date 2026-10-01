# Apr24 四项 Books 写后有限独立复核

复核者：root（未写入下列四项机制正文）。仅核 exact-v1 必要段、实际正文、邻接论证、owner 与事实边界；这不是 04/24 日期 Gate，也不代替来源覆盖和剩余候选审阅。

- `2604.21724v1` → `MODEL-EMBEDDING` Ch12：实际正文的频率感知 row 分配、混合 hash、局部提取、按层注入能接在静态 lookup 的容量与碰撞问题之后；保留 2×/4× 非单调、host/device 搬运和后续层开销。写后 PASS。
- `2604.21632v1` → `MODEL-EMBEDDING` Ch12：实际正文区分输入 embedding 的符号可辨识性与输出 copy 读出，softmax 对未见 label 行的影响有 GD/SGD 小步长等条件，不向 AdamW 外推；冻结行 C4 代价仍在。写后 PASS。
- `2604.21343v1` → `MULTIMODAL-REPRESENTATION` Ch23：实际正文把 projector 后 latent 腐化与中间层 clean-teacher-feature 恢复放在表示监督的演进分支；不称为 pixel 鲁棒保证，保留 clean 退步与 CKA/kNN 非因果边界。写后 PASS。
- `2604.21741v1` → `MULTIMODAL-EMBODIED-VLA` Ch26：实际正文将 world-model 缓存/回滚限定为模拟状态，人工纠正片段进入 post-training 后仍需真实机器人验收；未把有限相关或总体对照外推为 rollback 独立因果收益。写后 PASS。

四项的来源入口分别为 [21724](https://arxiv.org/html/2604.21724v1)、[21632](https://arxiv.org/html/2604.21632v1)、[21343](https://arxiv.org/html/2604.21343v1)、[21741](https://arxiv.org/pdf/2604.21741v1)。未复现实验，未判断 04/24 整日 Complete。
