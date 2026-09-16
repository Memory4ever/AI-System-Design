# 2026-05-22 root Books writeback — 7 Security items

写入时间：2026-09-15T22:45:00+08:00

作者 repair queue 中七项长期机制增量已由 root 串行写入 `PLATFORM-SECURITY`，没有由日期作者直接修改共享 Books。

| Source Family | 写入位置 | 实际采用的长期增量 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-22481` | Backdoor Evaluation | 将 trigger strength、poison rate、train/test strength 与 direction 拆为矩阵，阻止单点 ASR/clean accuracy 形成宽安全结论。 |
| `SF-2026-ARXIV-2605-22373` | Membership Signal | 将 safety-classifier MIA 扩展到 decision-boundary、harm 与 conversation/user-history privacy-unit 切片。 |
| `SF-2026-ARXIV-2605-21780` | Differential Privacy | 增加 joint training–test neighboring relation 与实现同构的组合 robustness certificate，保留条件半径与 fallback。 |
| `SF-2026-ARXIV-2605-21938` | Privacy Accountant | 明确 accountant 上界与 empirical RDP audit 下界的证据方向；双侧/上界需要额外 bounded-loss 前提。 |
| `SF-2026-ARXIV-2605-22005` | Parameter Path | 将 `lm_head` SVD/VCS 限定为静态 triage sensor，禁止推断训练数据、行为或自动删词/发布。 |
| `SF-2026-ARXIV-2605-21609` | Closed-loop Safety | 增加人群特定的 detect → rewrite → independent validation 分支，最终 authority 保留给 policy/human。 |
| `SF-2026-ARXIV-2605-22737` | Extraction Budget | 将防蒸馏评测升级为 adaptive-student operating frontier，teacher-side sampler 不拥有 confidentiality 结论。 |

每项均写在相应机制主干、首个主 `## Review notes` 之前，保留旧方案、约束变化、state/control owner、证据边界、代价、failure mode 与 fallback；没有复制论文摘要或建立论文列表。

七个 Source Family 各有唯一一对 `semantic-body-binding:<family>:start/end` marker。当前只声明 root 写入完成；仍须由未执行本次 Books 写入的 reviewer 逐项重读正文和相邻过渡，才能从 queue 移除并进入日期最终 Gate。
