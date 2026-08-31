# 2025-05-03 Independent Audit Access Receipt

## Phantora false-negative recovery

- Source Family: `SF-2025-ARXIV-250501616-PHANTORA`
- Window identity: arXiv Atom snapshot title `Phantora: Maximizing Code Reuse in Simulation-based Machine Learning System Performance Estimation`
- Exact-v1 primary: https://arxiv.org/html/2505.01616v1
- Exact-v1 rendered title: `Phantora: Live GPU Cluster Simulation for Machine Learning System Performance Estimation`
- Artifact: https://github.com/QDelta/Phantora
- Access result: arXiv HTML 可访问，已复核 §3、§4.1–4.2、§5、§6.1–6.4 与 §7；本地 `curl` 镜像返回 connection reset，未伪装成冻结本地副本。

Atom snapshot 与当前 exact-v1 renderer 的标题不同，但 arXiv identifier、作者、摘要与机制 identity 一致；本次以 `arXiv:2505.01616v1` 作为 primary identifier，不把标题字符串当成新的 Source Family。

## VideoHallu unresolved dispute

- Source Family: `SF-2025-ARXIV-250501481-VIDEOHALLU`
- Exact-v1 primary: https://arxiv.org/html/2505.01481v1
- Unresolved boundary: §4.2 的 GRPO 命名与公式形式不能由公开 exact artifact 唯一消歧。
- Consequence: Evidence 与 Books Gate 最高为 `Conditional Pass`；benchmark taxonomy 可保留，mitigation mechanism 不进入 Books。
