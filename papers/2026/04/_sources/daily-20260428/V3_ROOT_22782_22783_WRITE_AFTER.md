# 2026-04-28 两项 Books 写后非作者核

复核者 root。此前已以官方 exact-v1 做必要 source→owner 核（`V3_FIRST_TWO_SOURCE_REVIEW.md`），本次顺读实际正文、相邻段和 Review notes，且 scoped `git diff --check` 通过。两项的 first-public 属公告批次组合推断，不能用官方 v1 submitted 的 04/03 取代；整日日期/来源/候选 Gate 尚未通过。

## `2604.22782v1` → `INFER-KV-CACHE` Ch45：写后 PASS

实际正文在固定训练期跨层混合后引入“训练随机跨层来源→部署确定留存集合”，然后交给现有 basis/residual 路线；没有把随机性写成 runtime oracle，也没有宣称既有 checkpoint 无训练可删层。第515–517行保留 1.7B 训练 loss 退步、有限 QA/单卡 batch1/8K 观察、MoE/量化/时间淘汰及生产 SLO 未证和 FullKV 旧方案成立边界。Review note 对应 `SF-2026-ARXIV-2604-22782`，不把作者 benchmark 泛化。未发现 owner 冲突或跳跃。

## `2604.22783v1` → `TRAIN-LORA` Ch30：写后 PASS

实际正文接在 LoRA 权重/梯度/optimizer/activation 分账之后，只将 adapter-specific 激活从 `O(BSRL)` 收到 `O(BRL)`；显式保留基座激活、其他 workspace 和总峰值仍随长度变化。第133–135行说明 fixed/learned pooling 的成本与 token-local 信息损失，并交接到下一节逐层更新分支；普通 LoRA 与 checkpointing 仍是条件性回退。Review note 对应 `SF-2026-ARXIV-2604-22783`，没有把“参数少”误写为“全部显存少”。未发现 owner 冲突或无条件 Pareto 结论。

本核仅确认两处实际写入质量，不替代 04/28 Daily 整日验收或实验复现。
