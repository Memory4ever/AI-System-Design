# 2604.22550v1 ArmSSL — 有界非作者准入核

**裁决：恢复具名候选，建议 2+2+2=6，标准审阅；Books 暂作 Ch72 最窄缺口待深入/独立 source→owner，不直接宣布 Integrate。** 原“非 LLM、视觉 SSL IP 局部优化”不能作为前分母关闭的完整理由；本项也不能凭 IP 安全名词无条件升 Deep 或采作者通用鲁棒性宣传。此记录只对该 ID 作互审，不改变 04/27 正式分母、README、Books 或日级 Gate。

我实际重读了当前 `AGENTS.md`、研究合同 §3–6、ROADMAP 的 `PLATFORM-SECURITY` owner、[官方 exact-v1](https://arxiv.org/html/2604.22550v1) 摘要/§I、§III-A–C、§IV-A–C、§V-A–G 主对照和 §VI 最强自适应反例，并顺读 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 827–850 的生成内容 provenance/watermark 段及该章 model-extraction 附近的 watermark/canary 回退。委托消息称 `V3_SCREENING_NOTES.md` 有新增 ArmSSL 段，但我本轮在 04/27 日内该文件及其它 Markdown 中以 `22550`/`ArmSSL` 检索未命中；因此没有声称读到尚不可见的作者段，也不凭其做裁决。若后续落盘，按受影响命题定点对照即可。

## 为什么值得进分母

既有 Ch72 827–850 主要讨论**生成内容**的 metadata、embedded signal、public verifier 与 seed/sampling trust root；model extraction 段仅把 watermark/canary 列为一种回退传感器，并未展开**模型权重/encoder 身份经下游 head 和任务迁移后，验证者只能读黑盒预测**这一操作边界。[原文 §III-A/IV-C](https://arxiv.org/html/2604.22550v1)区分能见 encoder embedding 的 EaaS 与只可见 classifier confidence vector 的 MLaaS；前者的信号不能直接当后者可验证。作者用同一来源样本的 clean/trigger probing pairs、下游置信向量差异和检验阈值构造有限 black-box sensor，而 §III-B 显示旧 SSL watermark 样本在表示空间形成 OOD 密簇，会给 DECREE 触发器反演、MM-BD 下游异常检测提供攻击面。§IV-B 的“配对差异保留 + 向其他簇纠缠/SWD 分布对齐 + 干净 encoder 参考约束”是具体冲突设计，不只是给旧内容水印换一个视觉应用名称。

可迁移的项目命题是：**模型归属 watermark 的被观察对象与后续适配/暴露接口一起定义；检测信号若在表示空间形成可分离 OOD 簇，会把归属传感器本身变成攻击者的定位/移除线索。** 这对 foundation encoder 的发行、下游微调和服务黑盒审计有直接选择意义，故 Design Delta 2、System Reach 2（encoder→下游服务/安全验证）、Durability 2；不是因为碰巧能映射 Ch72，也不声称所有 LLM watermark 服从同一表示几何。若后续 Books 源→owner 深入通过，可在 Ch72 model provenance/盗用审计的唯一 owner 中补这一条件分支，不能把输出水印、模型水印和法律权属合为一谈。

## 主对照与不得采用的保证

- §V-B/Table II 的主要 direct-theft 协议是**冻结 encoder、训练下游 classifier**；全层 fine-tuning、pruning 属另列攻击，不能把 direct-theft 主表改称任意改写后仍可验证。四种主文 SSL、CIFAR-10/Imagenette/ImageNet 与多视觉下游构成受限支持；DINOv2 在附录，不能把“5框架/9数据集”写成主文完全同一协议。
- §IV-C 的 MLaaS verifier 要能取得 confidence vector 和同源 clean/trigger probes，`τ` 取 0.15/0.2、`λ=0.05`。只有硬标签、输出被截断、未知查询过滤或没有匹配 shadow 样本时，主实验不构成通过保证。其 Proposition 1 的 `if and only if` 和由 p-value 直接推“非法派生/法律归属”超过已测独立负模型范围；Table III 的 64 个 SimCLR-based negative 中观测 FPR 0%，不是总体 FPR 永为 0。p-value 是此协议下的统计证据，须与模型/发行/授权记录分账。
- §V-F/Table VII 中 MM-BD 对 64 clean 的 FPR 0%，对 64 ArmSSL watermarked 的整体检测 accuracy 约 50–53%；DECREE 在相应受限集约 54.69%。这只说明**所测攻击器**难以区分，不证明所有 OOD 检测或自适应移除失败。
- §VI 最强攻击在 `ψ=0.1` 的 GTSRB/SVHN 分布迁移上**成功移除**且 accuracy 约损失 20%；`ψ=0.5` 又使模型不可用。作者“只要模型仍可用就能验”的宽保证不能据此采纳。§V-E 的 99% 剪枝使准确率跌至约 10–25%，那时无法验也不能当作实用对手成功的唯一边界。Table II 亦有 ImageNet→SVHN clean 67.93 对 watermarked 66.14 等效用退步；不能写“零代价”。训练水印嵌入 4.07–7.66% 时间开销是作者 SimCLR 所测，不是生产总体成本。

**Books 建议：**不是直接 `Existing`，因为 Ch72 未有“encoder→下游 classifier→黑盒 confidence 接口”及“水印 OOD 密簇成为攻击面”的具体命题；但本核只为准入与必要主证据，不授权写书。保持 6 分标准候选，若 Ch72 的长期差额经真正必要深入与非作者采用核成立，再申请共享锁写最窄机制/反证；若独立复核认定这只对视觉 SSL 局部 IP 配方成立，退为有具体原因的 `Report Only`。该选择不依赖当前无法见到的作者筛选段，不扩大其它水印家族。
