# 2026-04-09 三处 Books 写后独立复核

审阅者 apr03；检查于2026-09-26。只复核主任务指定的三项新增正文、必要官方 exact-v1 段落及相邻交接，不重新审阅全日库存，不替代日期/来源/全日报 Gate。

- `2604.06836v1`：独立读取[官方 HTML v1](https://arxiv.org/html/2604.06836v1) §3.2–3.5/Algorithm1/§4.1/Table4，再对读 Ch39“分片与低比特状态压缩是两条不同的轴”及 Stage1→Stage2。RMS、离散度、二阶统计相对全局 EMA 的精度提议与一阶线性/二阶对数量化有原文依据；不是学习率调整。Table4 去掉 Spatial 的平均 bit 上升、PPL 下降支持正文的容量—质量取舍。正文没有采用 near-optimal、常数辅助内存、万亿规模收敛或生产吞吐保证；Review notes 明确 CV 在正文与算法的不同定义。PDF 入口本次工具 cache miss，未冒称 PDF 已读；可读官方 HTML 的必要证据充分支持当前窄正文。结论：写后通过。
- `2604.07023v1`：独立读取[官方 PDF v1](https://arxiv.org/pdf/2604.07023v1) §3、§4.5、Limitations 与 AppendixA 的必要训练成本段，对读 Ch24 因果 masked-block 小节和后续 commit 交接。clean stream/causal mask/right shift、左到右连续接受、cache block 同步准确；单 token 模式是新 checkpoint 的 AR，不是原分布等价。正文未把相同 epoch 叫真正 compute-matched，并保留多 token 质量损失、batch/cache 慢例。結论：写后通过。
- `2604.07173v1`：独立读取[官方 PDF v1](https://arxiv.org/pdf/2604.07173v1) footnote1、§3–5、§6.3/6.4 的必要部分，对读 Ch52 adapter 独立远程执行段及 KV-aware routing 交接。base/KV 与 adapter 计算分离、activation 往返依赖、GPU 发起 RDMA 的运行时责任成立。正文正确隔离 decode-first-token 的 TTFT（不含 Prefill），不将 IAR≥95%当一般 P95 保证；同总 GPU 却减少 base instances、朴素 disaggregation 增加尾延迟和 server cache 饱和均有原文支持。没有宣称精度、生产隔离或任意 workload 收益。结论：写后通过。

这三处真实正文均在 Review notes 前、源标记可定位，旧方案与 fallback 继续保留。未验证 artifact，不把写后复核称全日完成。

## 06613 推理早停：补充独立写后复核

apr03 独立读取[官方 PDF v1](https://arxiv.org/pdf/2604.06613v1) §3.1–3.2、§4.4–4.5、Appendix B，对读 Ch66“推理早停要区分可恢复性与强制读出”两段及 Review note。同 prefix 下自由 continuation 与 forced suffix 属不同协议；PSC 原定义依赖正确性标签，不是部署时无监督真值。正文只保留行为可恢复性，未采用“已经知道”的内部状态断言。共同解出样本、无 prefix 对照与持出阈值有对应证据；串行长度降低而 continuation 总 token 上升、完整轨迹比例的离线依赖和跨任务校准边界也已准确隔离。正文没有采用 HTML 异常日期或 headline 数字；API 并发/预算记录为评价建议，不宣称实测生产延迟。两段在章末证据区前，前后衔接未改成普遍早停保证。结论：写后通过；不代替全日日级验收，未复现实验。
