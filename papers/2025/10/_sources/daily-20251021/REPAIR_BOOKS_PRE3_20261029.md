# B9–14 完整 PRE 提案

只申请以下精确新增自然段/独立marker/本人完整末注；尚未写Books。必要证据已在R14/R15/R16逐项key复核。实际读取Ch34:174–196、Ch29:448–489、Ch17:475–531及624–652、Ch36:1138–1162、Ch48:409–457和相邻Ch16/18/35/37；Ch28/30/32/47/49交接在本轮实际补读后记录canonical。不申请整章锁或root第三批准。

## B9 15061 / TRAIN-DPO Ch34

文件：`books/part-04-training-system/34-dpo.md`，在原TKTO完整段/独立`SF-2025-ARXIV-2510-05799`marker后、`## Reference Policy 仍然存在`前。原段解释局部credit和mask不保旧能力；新增差额为把推理期回退/抑制得到的局部token事件蒸成target/non-target logit不同目标。

完整新增正文：

局部反馈还可来自采样器实际拒绝过的表达，而不是先比较两份完整回答：检测到目标短语后回退到其起始token，降低该选择的概率再采样，据此收集原token与替代token的局部监督；训练时只对这两类位置施加相应偏好压力，并以参照logits约束未针对的词表坐标。[Antislop/FTPO的受限分支](https://arxiv.org/html/2510.15061v1#S5)将昂贵的backtracking尝试移入离线目标，不把词表局部MSE当成所有prompt的分布保持，也不等原sequence DPO。Soft escape仍可能放过目标表达，作者backtracking有明显吞吐代价，适配后原任务也可退步；表达更少不认证事实或安全。目标pattern/边界、原模型、重采人口、loss与reference须共同保存，全部废样本、LoRA/调参和原能力回归均计费；模式、质量或净预算不合时，保可审计普通解码、可信pairs与原checkpoint，不由局部抑制率批准无损或普遍净速。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15061 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15061` — Daily2025-10-21补Oct20；writer首次exact-v1§4/5/6.1/6.3/T2/7，Lorentz R15 key，2+1+2=5，sampler事件→局部logit训练差额深入。保softescape、69–96%吞吐代价、Gemma能力反退、Llama70B head-only及不等配置；不授完整分布保持/硬安全/净加速。未核实现或复现。

## B10 15516 / TRAIN-SFT Ch29

文件：`books/part-04-training-system/29-sft.md`，`### Distillation 不是“Teacher 越强越好”`后、以“同词表、同prefix的概率蒸馏还要联合选择KL方向”开始的原段前。现有论证分KL方向/温度/target人口，没有明确teacher预训练数据量与student蒸馏数据量的联合比较轴。

完整新增正文：

比较teacher之前，还应把它见过的数据与student实际消费的蒸馏数据分开：固定student训练配置，分别改变teacher训练人口和student数据比例，才可判断收益来自更好的目标分布、更多监督，还是额外teacher计算。[受限数据量对照](https://arxiv.org/html/2510.15516v1#S4)表明，较少student样本也可能让KD比直接监督更低效，不能把teacher更大或已有完整预训视为免费；二者数据量相同也不证明每个软标签更可靠。Label smoothing不能解释全部观察，却不足以宣布所有KD理论被否定，表示CKA差异亦不是迁移收益的原因证明。Teacher预训/前向、数据选择、student全部训练与域外回归应共同结算；任务、数据比例或总预算失配时，保留可信直接监督、原student与已验证的小teacher，不由较少蒸馏样本或单个相似度签发普遍样本效率。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15516 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15516` — Daily2025-10-21补Oct20；writerexact-v1§3/4.1/4.2T1/5.1T2/5.2–3/7，Lorentz R16 key，2+1+2=5，teacher/student数据人口与总费差额深入。限CIFAR与Languini-GPTmini等作者条件，保2/3数据效率反侧、FOOD退步与CKA仅相关；不授任意KD规律或完整实现/复现。

## B11 15304 / MODEL-TRANSFORMER-LAYER Ch17

文件：`books/part-02-model/17-transformer-layer.md`，现有删除边界线性alignment两段及`<!-- semantic-body-binding:SF-2026-ARXIV-2605-15491:end -->`后、以“硬件和请求预算持续变化时”开始的原段前。原来整子模块替换/删除后坐标修复，不覆盖跨相邻层择channel再concat、随后蒸馏的压缩单位。

完整新增正文：

减少顺序层数也可以保留来自不同原层的部分channel，而不直接平均权重或只删除整层：先用校准activation与权重范数提出channel重要性，再按block影响分配相邻层各自保留比例，将所选channel拼成较少的新block，最后用原模型恢复训练。[CoMe的受限分支](https://arxiv.org/html/2510.15304v1#S4)改变参数来源与层边界，不由相似hidden或拼接保存的参数证明原函数等价；蒸馏正是新增适配成本。逐段恢复与联合恢复的内存/预算不同，合并更多层、太少校准样本或换校准域都可恶化质量，不能按压缩比例承诺无损。Checkpoint、校准人口、channel集合/比例、拼接布局与teacher须共同版本化，全部统计、重构训练与生成回归都计费；映射、关键切片或实测费用不合时，保原层、保守剪枝/坐标修复与完整模型，不从参数保留或相对accuracy批准服务净加速。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15304 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15304` — Daily2025-10-21补Oct20；Lorentz R14首次exact-v1§4.1–3/5.1/5.3–4，writer核§4.2 SBI与concat，2+1+2=5，layer/channel重构差额深入。保小校准/跨域/>2层反侧、mp/sp预算及symmetric-KL印式不闭，不采完整loss/83%绝对精度/无损。实际owner为Ch17，未核实现/复现。

## B12 15425 / MODEL-TRANSFORMER-LAYER Ch17

文件同B11，在现有Parallel Tracks完整论证及独立`SF-2026-ARXIV-2602-07306`marker后、`## Parameter Depth 与 Execution Depth 可以分离`前。旧tracks各维护连续state并周期融合；新增branch均读同一x0、聚合器渐进纳入分支，不等原层的代数并行化。

完整新增正文：

并行分支也可以不继承上一分支的hidden，而共同读取最初的输入，再由聚合器渐进接纳各分支结果。[ParaFormer首版的受限设计](https://arxiv.org/html/2510.15425v1#S4)把分支计算与聚合依赖分开，区别于各track连续演化后周期交换；但这是重新训练的架构，不是把既有顺序checkpoint原样切卡。存在可表达目标函数的宽度构造，不证明有限模型收敛、相同函数保留或所有深度无用；分支数增加也会改变容量、设备和通信预算。有限视觉任务有较少分支的精度反退，更多GPU的时间收益不等同硬件同质量收益。聚合拓扑、启用日程、全部训练/通信与任务回归都计费；跨分支信息、质量或净预算不合时，保标准顺序stack、原TP或已验证periodic tracks，不从并行可表达性签发普遍加速与替代资格。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15425 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15425` — Daily2025-10-21补Oct20；writer首次exact-v1§4/Alg1/5.1/5.3/5.5，Lorentz R16 key，2+1+2=5，共输入branch/渐进聚合差额深入。仅v1 ParaFormer，不混当前TeamFormer；保300epoch/8A6000最多6rank与架构预算混杂、PF1反退/UAT非收敛，不补渲染伪码为实现。未核代码/复现。

## B13 15596 / TRAIN-DISTRIBUTED-TRAINING Ch36

文件：`books/part-04-training-system/36-distributed-training.md`，“Straggler与同步放大”中原“平均GPU utilization…”完整段后、以“异构切分也不能只用整题耗时的倒数分配rows”开始的原段前。现有per-rank分布观测和确定性shape成本，不覆盖如何将局部随机延迟沿训练DAG组成预测分位。

完整新增正文：

若局部时延会抖动，规划器还可把算子成本保存为分布，而不只把平均值代入关键路径：按训练DAG组合串行和并行部分，再通过采样处理pipeline重叠，比较放置与局部波动对整体分位的影响。[PRISM的受限模型](https://arxiv.org/html/2510.15596v1)用Gaussian近似及独立性简化方差相加与CDF乘积，相关网络拥塞、共同降频或非Gaussian尾部不自动满足；平均误差小也不表示分布误差小。64H200上的验证与更大规模投影必须分开，模拟减少某个kernel方差或更换节点位置不是实际部署收益。Profile人口、DAG/并行计划、分布/相关假设与预测版本须共同保存，采样、拟合和真实回放回归均计费；相关性、尾部或调度身份失配时，保留实测per-rank/collective分布与保守计划，不从模型p95签发集群SLO或任意规模净速。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15596 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15596` — Daily2025-10-21补Oct20；writer首读exact-v1III/IV/V-A1–2，Lorentz R16关键核，2+2+2=6，随机算子→DAG分布差额深入。保独立Gaussian、mean与KS指标不同、64H200实测/64k+sample20rank投影分责、反事实非部署；不授all-scale tail保证，未核实现/复现。

## B14 15312 / INFER-SPECULATIVE-DECODING Ch48

文件：`books/part-05-inference-system/48-speculative-decoding.md`，原量化替身起草完整段/独立`SF-2025-ARXIV-2509-18344`marker后、`## Drafter 的演进：从辅助模型到受治理的 Serving Artifact`前。现有驻留/rollback不覆盖固定NPU图渐进加载与拒稿匹配子段仅保候选的共同计划。

完整新增正文：

固定NPU图还会使“稍后可能接受的长draft”与“当前可驻留并执行的图”成为两个预算：可先让小chunk图运行，再按profile渐进加载后续prefill/decode图；检索到的draft经目标prefill分布校准，拒绝后若仍有匹配子段，可暂存为下一轮待验证候选。[CoordGen的受限分支](https://arxiv.org/html/2510.15312v1#S3)不沿用原前缀下的接受资格，重新分词或修正前缀后仍须由target重新verify；语义相似不能让旧子段直接提交。图调度是profile下的贪心选择而非全局最优，短或无关draft仍可能不回本。三款手机上的时延与A100接受率实验分账，校准、retokenization、候选状态、全部图加载/驻留及CPU/GPU残留算子都付费；图/状态支持、热条件或净收益失配时，保短固定draft、原串行加载与target-only，不从更高接受率批准任意采样exactness或移动端实时SLO。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15312 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15312` — Daily2025-10-21补Oct20；Lorentz R14首次exact-v1§3.2–4/4.1/4.3–5，writer核§3.4拒稿子段仅重新提案，2+2+2=6，图驻留/候选资格差额深入。保Qualcomm12/16/24GB、QNN/mllm、Qwen0.5/1.5B及Llama3.2-3B、CPU/GPU敏感算子、profile贪心与额外校准/状态费用；不采无条件随机采样精确性或SLO，未核实现/复现。
