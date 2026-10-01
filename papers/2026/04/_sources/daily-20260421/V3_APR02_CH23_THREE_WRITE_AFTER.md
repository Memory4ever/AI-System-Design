# Apr21 Ch23 三项实际写后独立复核

复核者：`/root/apr02`（非本轮三处 Books 作者）；访问日期：2026-09-27。

范围：仅实际 Ch23 三处正文、相邻交接和支持这些命题的官方 exact-v1 必要局部。沿用未变化的准入记录；本次没有重扫来源、复核日期分母、遍历附录或复现实验，不代替 Apr21 日级 Gate。未修改作者 README、作者笔记或 Books。

## 2604.16479v1 — 通过

实际位置：`books/part-03-multimodal-world-models/23-multimodal-representation.md` 的 `SF-2026-ARXIV-2604-16479` 两段（本次约226/228行），语义/声学信息压缩之后、Codebook Capacity 之前。

本次重开[官方 v1](https://arxiv.org/html/2604.16479v1) §4.2 Eq5–7、§4.3、§5.2 Tables1/3 与 §5.3 Table4。固定保留 LLL/LLH/LHL/HLL、其余置零、逆变换后 learned decoder，以及训练期适配与部署后过滤的区别均符合原文。实际正文没有将低频当语义真值、压缩量当等价质量或把 PSNR 外推为生成优势。Table1 WebVid 部分 rFVD、Table3 Sky/UCF 部分 FVD 的不利结果已留在边界中；Table4 只支撑受测训练责任差异，非普遍后处理不可行。新增段接回 codec 身份/下游生成验收，成本与原 codec 回退就近，衔接通过。

## 2604.16503v1 — 通过

实际位置：同章 `SF-2026-ARXIV-2604-16503` 两段（约290/292行），模块化 understanding/generation 分工之后、Full-duplex 在线状态之前。

本次重开[官方 v1](https://arxiv.org/html/2604.16503v1) §3.3 Eq2–4/Figure5、§6.2 与 §7.2。零输出初始化只保起始函数；后 self-attention 视频状态生成新 Q，同层 pre-attention 文本状态使用既有 K/V 投影并复用 tensor，两者分工准确。实际正文未把联合改变 Q 与 K/V 的对照归因为仅 K/V，也不采用普遍 manifold 保证；复用投影不等 cross-attention 免费、后续训练不保持原函数及整配方无全面组件消融的限制均保留。嵌入已有接口/模块化论证而非单列产品总结，回退和相邻论证通过。

## 2604.16462v1 — 通过

实际位置：同章 `SF-2026-ARXIV-2604-16462` 两段（约388/390行），视觉删改协议反证之后、decode-stage 备用重选之前。

本次重开[官方 v1](https://arxiv.org/html/2604.16462v1) §3/Table2 与 Appendix A.1 Eq8–11。视觉更新终止但 K/V 仍由全部 token 计算、文本仍读取视觉，实际正文没有偷换成完全删除读路径；Qwen 深层仅少量候选继续更新的分支与 LLaVA 不同。Table2 OCR 读路径撤去退步和统一更新抑制的架构反差支持条件化选择，几何熵仍只是代理。实际段落区分更新/读取成本，不用删除比例代替全部 Attention/KV 收益，并将生命周期交给 Ch45。上下两侧保留完整输入与备用恢复分支，衔接通过。

## 交付边界

三项本轮实际正文及邻接写后复核全部通过；论文实验未复现。本结果允许作者同步这三项写后状态，不能据此声称本日来源零遗漏、冻结分母或整体完成。
