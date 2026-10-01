# 2026-04-30 五项中心争议的非作者定点核包（作者，未冻结）

这不是五篇均已入本窗候选的声明：`25931/26130/26525` 在现有 33 家族未冻结工作集合内；`26809/26467` 是负侧高风险恢复项，**尚未计入分母**。只请求非作者核中心可采用保证/算法桥；不须重读全部附件、版本树，也不因争议自动否定全部受限实验。

| exact-v1 | 原文需核的中心位置 | 最小反例/缺桥 | 可保留的窄证据与处置 |
| --- | --- | --- | --- |
| [2604.25931v1 PHC](https://arxiv.org/html/2604.25931v1) | §3 Theorem 1、§4–5/Appendix B,E；`G*` 与 PHC 定义 | 声称任意后生成信号 `U(Q,A)` 对 `G*` 的互信息都不低于任意先生成 `g(Q)`；取常数 `U` 而 `g(Q)` 含有标签信息，结论立即不成立。RAG `G*` 是 GraphRAG 相对 VanillaRAG 升级收益，不是逐题 wrong-answer 标签；0/1/2/3 gold sub-answer 注入的 PHC 非单调不等逐题错误率同幅变化。 | 受限检索升级/置信诊断与调用预算曲线可报告；不采用普遍 post-gen 优越定理，不写 Ch76 正面阈值保证。详证见 [筛选笔记](V3_ARXIV_SCREENING_NOTES.md)。 |
| [2604.26130v1 reward-lens](https://arxiv.org/html/2604.26130v1) | §3 Eq(2)–(3)、§5.4/Table3、Appendix B/D | 正文把逐层残差投影的和写成 exact reward 重建；Appendix B 明言 reward head 前有非线性 final LN，而 lens 对中间项不施 LN。一般 `wᵀLN(Σh_i) ≠ Σwᵀh_i`，故需核源码的 score-head 与 sanity assertion；不能同时采精确分解与非线性实现。 | 同一首对答案上观测归因与 patching 排序相关性受限且多为负，说明 probe 不自动获因果 authority；不否定 patching 本身或作者 visualizer。 |
| [2604.26525v1 PRAG](https://arxiv.org/html/2604.26525v1) | §V-C/Alg3、§VI-A Lemma VI.4、Appendix B-A、§IV-A trust boundary | 两分数各误差严格小于真 gap 一半时按三角不等式**不能**反序；仅有误差差值上界和真 gap 较小，不给“排序近随机”的误差分布，取误差恒零即可反例。Alg3 用邻向量加权和作 `ep`，下一层再 `Neighbors(G,ep,l)`，虚拟向量到图 node/邻接表的映射未给。客户端解密 context 后还交 LLM，不是对全链路所有方保密。 | 可报告非交互近似 HE vs client-assisted 精度/轮次的受限取舍；不正面采 OEE 排序/复杂度与 end-to-end confidentiality 保证。 |
| [2604.26809v1 异步联邦遗忘](https://arxiv.org/html/2604.26809v1) | §III-B–D/Algorithm1 第17行、Eq4；§IV/Table I–III | 旧 snapshot 上求出的删除更新被服务器直接赋成下一全局权重，未给并发 retained update 的版本比较、合并或重放；标量 0→1 的保留进展可被旧快照回传 0 覆盖。`KL(f(x),f(Φ(x)))=0` 也可由恒等 `Φ` 或原模型已不变达成，单独不能推永久删除。 | 5–20 客户端 CNN/医学影像、10轮行为/参数距重训及后门成功率只是受控评价；不采一般 async correctness 或 feature erasure。只请求定点裁是否形成候选纠错，不因医疗场景拒绝。 |
| [2604.26467v1 DP-GCL](https://arxiv.org/pdf/2604.26467v1) | §3.2.1 随机分组、Algorithm1、Appendix A Theorem2（PDF v1 与 HTML v1 对齐） | Theorem2 `2C` 证明要求邻接数据集其余 pair 完全保持同组；算法只写每个 batch 随机划成大小≤`S` 的组，未定义跨增删邻居可保持旧成员组且维持原随机边际的 coupling。`S=2` 旧两 pair 只能同组；新增第三 pair 的均匀随机二人组+单人组中，新 pair 单独的概率仅 1/3，证明固定旧组的桥不自动成立。 | Group-limited InfoNCE 依赖图→clip/noise 单位是潜在长期隐私条件；ResNet18/ViT-B32 LoRA 的效用不因此否定。未有稳定 grouping/accountant 桥前不把所报 `ε` 当生产证书，暂不写 Ch72 正面保证。 |

核验顺序建议先查两个安全隐私保证 `26467/26525`，再查 `25931/26130` 数学恒等式与 `26809` 发布版本。即使具体反例通过，也只给相应**命题** Disputed，不声称整个实验/系统无效。若原文另有未读条件可修补，记录条件及相应实现身份后收窄，不扩到所有论文的完整版本差分。
