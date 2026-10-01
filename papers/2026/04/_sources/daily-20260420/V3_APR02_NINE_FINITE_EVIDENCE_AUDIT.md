# 04/20 九项有限非作者 Evidence→Owner 复核

范围：仅下列九个具名 family 的 official exact-v1 必要方法、关键反证与当前 Books 实际命题；未重审来源日期、整日候选分母、全部附件或复现实验。本文不替代 04/20 日级 Gate，不改作者正式报告和共享 Books。

## 首四项

| Family | 实际核验与现有 owner | 有限独立结论 |
| --- | --- | --- |
| [2604.15805v1](https://arxiv.org/html/2604.15805v1) | §III–IV/Table III 确有 panorama→静态 3DGS/collision mesh→digital cousin 的 real-to-sim 数据支撑路径；同为 100 条训练数据时 50 real+50 sim twin 在两项汇总指标 .33/.35，低于 100 real 的 .37/.35，另一个 50 real+100 sim 比较不等预算。Ch26 [Sim-to-real 不只是视觉 domain gap](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已把视觉、物理参数、接触、延迟和真实控制验收分开。 | **6 分、标准、Only PASS**：保留具体仿真数据分支及受限相关性；照片/离线场景相关性不升级为物理交互或单场景真实成功保证。此处没有改变 Ch26 的行动提交权和真实反馈合同。 |
| [2604.15809v1](https://arxiv.org/html/2604.15809v1) | §3/Eq1–5 与 Table7 是额外一步读 attention、跨层 entropy 排名和 text-query→visual-key 读边 mask 的局部路径，非删视觉 token；同 mask ratio 的随机/逆排序更差，但不识别 attention 唯一因果。Ch23 当前 [融合与视觉读路径](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 已区分证据表示、text 访问、mask/position/KV 和任务输出；该特定 entropy/mask 配方不改变其长期责任。 | **5 分、标准、Only PASS**：不因视觉局部应用直接排除，也不采无成本或普遍 grounding 的强句；额外解码、mask 统计和未披露生产 SLO 限制写在作者证据中。 |
| [2604.15827v1](https://arxiv.org/html/2604.15827v1) | §3–5 将 relevance 与 decision usefulness 分标；21.9% 高相关文档仅部分有用是具体反例。但三位分析员、15 份报告、10 行业/未标全文档当负例限制标签外推，启发式排序分数不成为已校准决策概率。Ch76 [相似不等于有用或真实](../../../../../books/part-07-agent/76-rag.md) 已把 retrieval、evidence、answer 与 task success 分账。 | **5 分、标准、Only PASS**：论文数据集/排序代理是受限测量实例，不改现有长期 RAG 权责；不把全部方法误称已有覆盖。 |
| [2604.15829v1](https://arxiv.org/html/2604.15829v1) | §3–4/Eq3 与 Appendix B.5 的温度方向需区分印刷正文；凸 embedding 组合、合成视觉 latent 和 nearby-concept 质量都是真实机制，但 embedding hull 不保证语义/安全覆盖。Table3 有模块去除后的局部反向。Ch72 [Unlearning 的 substrate/observer 与 concept-wide 目标](../../../../../books/part-06-ai-infrastructure/72-security.md) 已要求参数、行为、恢复攻击及 retained utility 分账。 | **6 分、保护深入、Only PASS**：仅保留 text-image 协同擦除与有限保留切片；不能从合成图和部分指标推出永久/全部概念擦除，也无新长期安全 authority 要写 Books。 |

上表锚点分别是 Ch26 `Sim-to-real`、Ch23 `Cross-attention fusion/视觉读路径`、Ch76 `相似不等于有用或真实`、Ch72 `Unlearning`；实际段落在本次复核时已读取。

## 后五项

| Family | 实际核验与现有 owner | 有限独立结论 |
| --- | --- | --- |
| [2604.15923v1](https://arxiv.org/html/2604.15923v1) | §4.1–4.4/§5.4 把同一 speech codec 的低层 r1–2 接 lip/identity、高层 r3–12 接 expression/prosody；训练期 identity/emotion 条件由 ground-truth acoustic features 替代，推理才仅用视觉。Table6/7 的有限 OOD 与移除项非一致全面优势。Ch24 [语音生成粗细分解](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 已区分 RVQ residual codebook 层级与时间分辨率链，且要求 codec/条件/迭代成本分别验收。 | **6 分、标准、Only PASS**：保留视觉条件分配的具体实现，不把训练说成纯视觉端到端，也不称条件可无损、完整解耦或由该论文重写 Ch24 主线。 |
| [2604.15944v1](https://arxiv.org/html/2604.15944v1) | IV-A/B、V-A/B 是 SRAM CIM 双 bank+固定点 LUT split softmax 的真实硬件映射。官方明确 26.1 TOPS/W 为 post-synthesis、面积为 post-layout；33% 是 1024 token/head64/encoder-only 配置相对 32b nonsplit LUT 的局部延迟；TinyLlama 精度用 PyTorch 模拟，片上容量不足以装完整模型。Ch49 [数值与 softmax 路径](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 与 Ch54 [片上容量/IO](../../../../../books/part-05-inference-system/54-gpu-memory.md) 已要求数值、层级流量、layout、实际执行分母共同冻结。 | **6 分、标准、Only PASS**：这是值得保存的实现 operating point，但并未证明 fabricated chip 实测、完整 LLM 的端到端能效或通用部署 SLO；不把静态后端案例追加成书稿长期必选分支。 |
| [2604.15948v1](https://arxiv.org/html/2604.15948v1) | 官方 Eq10 的 `ReLU(A_s−A_e)` 可为零，Eq11 对正 `A_e` 直接取 `log 0`；Alg2/Eq16 有 `std(h_d)=0` 未定义路径，latent refinement 又把 `h_d` 直接加回，mask 不能证明背景不变。撤销旧提取文本对 Alg2 的误读，不否定两分支实测。Ch24 [编辑目标与背景保留分责](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 已要求目标、重建、mask 成本与质量分开。 | **6 分、中心公式窄争议、Disputed PASS**：仅隔离印刷 entropy/normalization 的有限可执行性与由它推出的背景保证；实验表仍可作受限观察，不上升 Books。重开需作者实现的 epsilon/zero-std/zero-norm 规则及实际 mask 路径说明。 |
| [2604.15958v1](https://arxiv.org/html/2604.15958v1) | §2 的 PRE 在进入 embedding/generation 前匿名，POST 则使原文先过上游服务；两者 output PII 少不代表暴露面相同。§2.2 的 TO 为正的非负比值，单凭 `TO>0` 不能证明 privacy gain 大于 utility loss；几种 DP 的 epsilon 单位/预算不同。Ch72 [匿名化与泄漏边界](../../../../../books/part-06-ai-infrastructure/72-security.md) 与 Ch76 [检索证据/答案分账](../../../../../books/part-07-agent/76-rag.md) 已明确各阶段身份和最终答案不是同一对象。 | **5 分、标准、Only PASS**：保留 PRE/POST 不同暴露点的案例和指标反例，不采端到端匿名、跨预算最优或实际攻击成功保证。 |
| [2604.15967v1](https://arxiv.org/html/2604.15967v1) | §3–4 的样本以单独概念安全、二者组合危险构造；MDR/SCR 分账且 Table2/3 的固定 ontology、三个 classifier 的乘积代理和测试过滤器不能变成生产事故率。Table3 文字明确 text filter 的 recall 在此集合较高，并非一切现有防线均失效。Ch72 [组合风险与重建语义 Gate](../../../../../books/part-06-ai-infrastructure/72-security.md) 已要求原子输入/组合语义和独立授权分层。 | **6 分、保护深入、Only PASS**：保留原子安全不推出组合安全的受限基准反例；不采用独立潜在概念、普遍 erasure 失败或开放域安全保证，未出现需改写 Ch72 责任的新桥。 |

九项均是本文限定范围内的具名非作者 Evidence→Owner 结论；没有核 04/20 其余候选、来源日期或完整日级 Gate，也没有把所有局部方法称为已有算法。
