# PROSFI 唯一 owner 窄 PRE

Owner `TRAIN-RLHF`；路径 `books/part-04-training-system/31-rlhf.md`。root已实际必要Source通过，真实`2+1+2=5`；因明确长期接口差额加深必要命题，不借通用原则重评分。尚未授写锁，未写Books。

实际比较Ch33 54–94 verifier人口/奖励与Ch31 899–906 reference-derived子问题curriculum，均未承载policy自身输出typed scaffold与后置验证资格。只由Ch31 reward/producer/verifier owner整合，不改GRPO estimator或跨两章。完整右邻仍为Learning Progress Reward。

## 当前完整局部

~~~~markdown
终局 reward 在任务短、成功条件明确时最少引入人为结构；长推理链里，它却把 credit 全部压到最后一步。若 reference chain 本身可审计，可以由 curriculum builder 把终局任务派生为有边界、可判定的 subproblems，verifier 只提交这些局部判据的 credit，再由训练控制面决定是否进入 policy update。这里 curriculum builder 拥有难度与分解边界，verifier 不拥有策略提交权。

更密集的反馈换来 reference bias、子问题捷径和“局部全对但整体失败”的新风险；因此必须保留未分解的终局任务作为 held-out gate，分解失真时回退终局可验证训练。arXiv:2605.22074v1 只支持作者 reference-derived curriculum 与受测任务中的实验结果，不证明任意 chain decomposition 都保持原目标。

<!-- source-family:SF-2026-ARXIV-2605-22074 -->

#### Learning Progress Reward 必须绑定 Sealed Audit
~~~~

## 拟新完整局部（只新增一段）

~~~~markdown
终局 reward 在任务短、成功条件明确时最少引入人为结构；长推理链里，它却把 credit 全部压到最后一步。若 reference chain 本身可审计，可以由 curriculum builder 把终局任务派生为有边界、可判定的 subproblems，verifier 只提交这些局部判据的 credit，再由训练控制面决定是否进入 policy update。这里 curriculum builder 拥有难度与分解边界，verifier 不拥有策略提交权。

更密集的反馈换来 reference bias、子问题捷径和“局部全对但整体失败”的新风险；因此必须保留未分解的终局任务作为 held-out gate，分解失真时回退终局可验证训练。arXiv:2605.22074v1 只支持作者 reference-derived curriculum 与受测任务中的实验结果，不证明任意 chain decomposition 都保持原目标。

<!-- source-family:SF-2026-ARXIV-2605-22074 -->

当任务已有可核验的 premises 和 target，而模型难以生成完整证明脚本时，还可让 policy 先不中断地生成整段回答及类型化 scaffold：每个原子步骤声明 id、dependencies、conclusion 和 rule，限制依赖数量；rollout 完成后再提取子命题交给形式工具，最高序列奖励要求末目标正确且所有步骤通过。这里 producer 提议待验的分解，verifier 只拥有所提命题的有效性判定，reward 不把它扩为整段自然语言的忠实性或 soundness。[PRoSFI 的受限对照](https://arxiv.org/html/2603.29500v1)支持这一格式与验证接口，但遗漏的文字推理仍不在证明范围，GPT soundness 也只是另一个代理；其 Hard 对照中的完整 Lean 分支并非全面劣于 outcome reward。后置验证可以与生成解耦，却未证明异步净吞吐，rollout、翻译、形式检查、judge 与独立终局评价都须计费。Scaffold 覆盖不足、解析或验证失准时保留原 outcome 检查、可审计 reference curriculum 与明确的未验证状态，不用最高 reward 签整条推理正确。<!-- source-family:SF-2026-ARXIV-2603-29500 -->

#### Learning Progress Reward 必须绑定 Sealed Audit
~~~~

## 本人静态注

保留当前末注：

~~~~markdown

- `SF-2026-ARXIV-2603-30036` — Daily `2026-04-02`补`04-01`；[exact-v1](https://arxiv.org/html/2603.30036v1) §3–4 reward-pair概念、§6–7必要实测/直接反側，`2+2+3=7`。只采task/monitor条件下output/CoT奖励相容关系；transparentbias为假设，监控是文本分类非内部真值。sweep选最好、正交semanticdrift、长度空trace、aligned初始完美未主动提升等反側保留，不授一般lengthpenalty安全/危险、任意optimizer或部署透明保证。未核代码或复现。
~~~~

仅后追加：

~~~~markdown
- `SF-2026-ARXIV-2603-29500` — Daily `2026-04-02`补`04-01`；[PRoSFI exact-v1](https://arxiv.org/html/2603.29500v1)必要§3–4/§5.1–5.4/§5.6，`2+1+2=5`，model-emitted scaffold/后置verifier与序列reward差额。仅采所提formal命题的资格分责，RewardHit不涵盖全部NL；保Hard direct-Lean反側、GPTjudge proxy、769/7B/8Hopper/960steps人口和CPU验证/总费用未闭，不采异步净吞吐或整体soundness保证；未核artifact/复现。
~~~~

申请只新单段与本人静态注窄锁；保持全部原正文/其它family，root逐字PRE/授权前不写，实际写后由root nonwriter POST。

