# Gauge — 独立输出头等价类的窄 PRE

Family `SF-2026-ARXIV-2603-29488`；`3+1+3=7`。root 已实际核 exact-v1 §2–4 与 distinct 非零 pair 的 ±1 反例，Source 通过；本文件仅申请写前/窄锁，不是写入或 POST。

## 唯一 owner 与差额

`MODEL-EMBEDDING` — `books/part-02-model/12-embedding.md`。当前95–107只有训练目标塑造几何、近邻不等语义与 continuous-target collapse；152–175定义输出头/tying/左逆接口；323–356诊断几何只给近邻/维度测量限制，没有 independent output head 的 common-shift 等价类及保持所有预测却改变 cosine 的反例。新增是 softmax 输出坐标不可辨识的严格条件，不是泛化所有输入 embedding/CLIP 或重写现有几何诊断。

已读 Books 规定上下文、当前 Ch12 的表示/输出/geometry 主线与 Ch11/13 交接；只在 output tying 架构选择后插两段，保留原 PIT 左逆与输入表论证。邻接先说明模型配置，再区分独立头与 tied 表，最后原 PIT 承接需要主动耦合的另一选择。无结构候选。

## OLD 完整正文锚

```markdown
Weight tying 是架构选择，不是 Embedding 的定义。不同模型可能使用独立矩阵、额外 normalization 或不同 bias。加载 checkpoint 时必须以模型配置和权重布局为准。

普通转置共享适合参数预算优先的路径；若还要求线性 hidden→logits→embedding 的往返恢复，可将输入表与输出头耦合为下面的左逆构造，其中 `Z [V,d]` 列正交，`T [d,d]` 可逆，作者以 SPD 参数化学习 T：
```

## NEW 完整替换（只插两段）

```markdown
Weight tying 是架构选择，不是 Embedding 的定义。不同模型可能使用独立矩阵、额外 normalization 或不同 bias。加载 checkpoint 时必须以模型配置和权重布局为准。

独立输出头还会留下一个容易误读的坐标自由度。固定产生 hidden vector 的整个函数 `h=f(x)`，令输出类别向量为 `e_i`、logit 为 `h·e_i`；给所有类别共同加同一个向量 `v`，新 logits 只多出所有类别相同的 `h·v`，softmax 的分子、分母同时乘相同因子，因而每个输入的预测分布完全不变。这个等价类只改独立输出头，不改输入表和 `f`；如果头与输入 tying 后一起平移，`f` 也可能改变，不能直接沿用证明。额外 normalization 或非 softmax 读出也须另核，不能把它搬到任意表示或相似度模型。

保持预测不变，却不一定保持类别向量的 cosine。对不同向量 `a≠b`，共同平移 `v=−(a+b)/2` 后两者为相反的非零向量，cosine 是 `−1`；选择 `v=−a+(b−a)/2` 后两者为同向非零向量，cosine 是 `+1`。[精确输出头反例](https://arxiv.org/html/2603.29488v1)因此排除了不说明参数化便把 cosine 当作预测概率或语义关系的普遍保证，而没有证明某个固定 checkpoint 的所有 cosine 统计都无用。解释时应明确测的是输入还是输出、头是否独立及坐标约定，并用预测概率、任务行为或受控干预验证；这些诊断仍有采样/评价成本，也不替代原来的 lookup、共享权重或已验收模型。<!-- source-family:SF-2026-ARXIV-2603-29488 -->

普通转置共享适合参数预算优先的路径；若还要求线性 hidden→logits→embedding 的往返恢复，可将输入表与输出头耦合为下面的左逆构造，其中 `Z [V,d]` 列正交，`T [d,d]` 可逆，作者以 SPD 参数化学习 T：
```

## 本人末注完整锚与 NEW

当前最后项不动：

```markdown
- `SF-2026-ARXIV-2610-10533` — Daily `2026-10-09`；[EngramEdit exact-v1](https://arxiv.org/html/2610.10533v1) §2–4/6及A.3/B.2/B.4必要范围，2+1+2=5；多表达共享ngram联合更新/精确sequence overlay差额深入，加性/gated边界、保留反退/人口与全费近文。review_mar11_continue非作者必要Source/actual Ch12 owner/逐字PRE通过，root授本段与本注窄锁；作者实际写后完整邻接和本注已顺读，root非writer实际288–315完整邻接、新298及本人403注actualPOST通过，锁释放。未核全证明、像素、代码或复现，不授DAY。
```

其后只追加：

```markdown
- `SF-2026-ARXIV-2603-29488` — Daily `2026-04-02`补`04-01`；[exact-v1](https://arxiv.org/html/2603.29488v1) §2/common-shift proof、§3–4 反例与界限，`3+1+3=7`。只采用 fixed `f`/独立输出头的 softmax 等价类与 distinct 非零 pair 的 cosine ±1 构造，不授输入表/tying/CLIP 通用不变性、所有固定参数统计无用或概率-语义保证。单位向量 toy 与符号错误不采用，v2 sigmoid 扩展不回填；未核代码或复现实验。
```

申请只有上述两段与本人末注的 Ch12 窄写锁；root 必须实际 PRE 后才写。写后本作者读完整邻接与注，root 非 writer 再实际 POST；无 DAY。

实际写入与非writer复核：root已actualPRE核150–175邻接后授权仅两段/本人注窄锁；作者apply_patch实际写168/170两段及注424，顺读150–187完整邻接/尾注，限定diff-check通过。root已实际nonwriter读160–181 tying/gauge/PIT完整邻接与注424，确认fixedf、distinct非零pair、normalization边界和最终3+1+3=7，POST通过、Ch12锁释放。未授本日DAY。
