# 2604.26622v1 → Ch77 有界来源与正文比较

- 审阅者：root；对象仅为本 Source Family 的 Books Decision，不是 04/30 日级 Gate。
- 原始来源：[arXiv exact-v1 HTML §4–6、Tables 3/6/7、Limitations](https://arxiv.org/html/2604.26622v1)。作者在 §4 式(5)–(10)明确存储图像、verbatim text segments 与 metadata；视觉模型选择 `(image, segment)`，`Fetch` 从日志返回文字。低清命中后的高清图来自原日志重新渲染（§4 Multi-Resolution），不是从已失真的缩略图无损恢复。
- 原 Ch77“视觉压缩”段正确指出 OCR/布局失误，却将图像分支整体收敛为难以 exact dereference、仅适合概览。原文给出了条件性反例：图像只做低 token 定位，原文日志保留证据真值与确定性回读。根本变化是视觉索引与证据状态的 owner 分离，而非图像本身无损。
- 可采用的窄结论：精确回读取决于选中索引与原文日志 revision 的绑定；选中后文字相同不证明片段相关或 Agent 回答正确。授权、删除和旧索引失效仍是系统必须补验的推论，不是作者已实验解决的安全保证。
- 作者 Table 6 的 `100% faithfulness` 仅测已选片段与存储原文一致；Table 3 动态低清的 Step SR 46.1%，略低于静态高清 46.5%；Table 7 在 Mind2Web 连续日志条件下，Text-RAG 对比的磁盘 18 KB→1.47 MB/episode、检索 0.3→1.7 s/step，虽然主 Agent 文本注入 3,980→596 token/step。模型、数据及预算限于论文 §6 设置；不能推出生产 SLO、全历史可扫或普遍成本优势。
- 当前实际正文在 `books/part-07-agent/77-memory.md` 视觉压缩段后插入了“视觉定位 + 原文确定性回读”的条件分支，保留纯图像路径及低成本旧方案。已检查相邻前后论证与 `git diff --check`。独立写后审查已请求 `apr01`；其返回前不得把此项标为验收完成，更不能提高日级计数。
