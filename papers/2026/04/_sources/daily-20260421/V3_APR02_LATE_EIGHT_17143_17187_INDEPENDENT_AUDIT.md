# Apr21 晚批八项必要范围独立审计

复核者：`/root/apr02`，非本日日报作者、非这些 Books 正文写者。访问：2026-09-27。
本次实际重读当前 AGENTS、Research/Report 合同及四批作者记录，定点打开八篇官方 v1 必要方法、评价与反例；Existing 同时顺读实际章节及相邻论证。窗口仍为 `[2026-04-20T09:00:00+08:00,2026-04-21T09:00:00+08:00)`；本审计不重新认证日期、每日来源覆盖或整日 Gate，不扩大原始库存、版本史与附件队列。

## 结论

八项采用范围通过：四项已有覆盖、四项仅报告；没有新增 Books 写入提案。七项维持标准审阅；17159 的安全评价采用边界已实际深入核，作者记录的“6 标准完成”应同步为“6 深入完成”，评分与 Existing 决定不变。这里的通过只指以下具名命题，不代表论文全部主张、实验复现、真实书稿新增或日报完成。

## 17143 — SeekerGym：已有覆盖，6 = 2+2+2

实际读 [official v1](https://arxiv.org/html/2604.17143v1) §2.1–2.4、§3/Table3 与 G.3 的决定性限制。固定 article 的 goal passages 是分母，阈值检索与累计集合测 corpus-relative completeness；oracle 的未发现位置结构属于特权信息。校准实验的 belief 来自随机子集，真实检索轨迹存在相关与分布差异，因此不能采用在线自适应停止的无条件覆盖保证。

实际对读 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L729–747 的 expected-fact Inventory、来源 revision/unknown/粒度限制，及 L440–451 的覆盖假设与失效降级。两项拟采用长期判断均已有真实正文，不冒称具体 benchmark/停止器全部已实现。标准 Existing PASS；120/80 篇、六模型及三 seed 只属于作者合同，不外推开放网页完整性或 API SLO。

## 17145 — Negative Momentum：仅报告，5 = 2+1+2

实际读 [official v1](https://arxiv.org/html/2604.17145v1) §1 Eq1.3、§3 Theorem3.1–3.2、§4 Lyapunov 状态与归纳用途。第二变量梯度使用刚更新的第一变量；负 momentum 与交替顺序不可任意拆换。凸凹结论是平均平方梯度范数/均匀随机停止的速率；强凸强凹另给距离收敛。smooth、saddle 存在、确定梯度和零初始 momentum 等前提不能省略。

标准 Only PASS：该有条件优化机制值得保留，但没有非凸 Transformer/随机 Adam 的训练选型证据；不能将随机停止结果改写成 last-iterate objective 同速，亦没有 wall-clock 优势可进入一般训练结论。不因理论或局部范围而删除其贡献。

## 17147 — ScenarioControl：仅报告，5 = 2+1+2

实际读 [official v1](https://arxiv.org/html/2604.17147v1) §3.1–3.4 Eq6–8、§5 与 Table3。dense conditioning 到 variable-length scene tokens 的直接 cross-attention与 learned-global-latent 分支共享 conditioning K/V，以零初始 tanh gate 合并；不是仅换应用名称。场景生成、行为 simulator、wireframe 对 Wan2.2-5B 的视频条件是不同阶段，不证明真实 transition 或安全控制。

标准 Only PASS。具体 conditioning 工作点及受限对照可以报告；AP/collision 与控制代理不支持每列最优或通用首选。实际顺读 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 开头 video/predictive/action-conditioned 对象与 simulator 共存边界；这里不是把双分支算法判为已覆盖，而是尚不足改变长期状态权威或控制结论。额外 attention、depth/count 模块有成本，无部署 SLO 采用。

## 17159 — Offensive Cyber Tasks：已有覆盖，6 = 2+2+2，必要深入

实际读 [official v1](https://arxiv.org/html/2604.17159v1) III-A–C、IV-A–C、V。单 Gemini3Pro 的八配置、各200任务比较中，提示收益随环境翻转；Kali 同时加入工具集及 discovery，不能归因纯 OS。planner/executor 配对也是受限反证，不是同模型永远优于异构。单 trial、温度1、30/100 rounds、10分钟与名义成本限额都属于合同；多厂商排行混有 API/parser compatibility，不能认作纯 weights 攻击能力。

实际对读 Ch66 L173–193 的 subject 身份、adapter semantic equivalence、harness/environment/scorer 分权和稳定脚本共存。该机制与保护评价边界确由正文承载，深入 Existing PASS。**作者 batch 的标准标签需同步深入完成**；不抬评分、不新增 Books。CTF 成功不是生产权限、安全证明或真实攻击普遍能力；也不采用作者关于共同数据暴露使相对比较必然可靠的泛化。

## 17172 — CCCL：已有覆盖，6 = 2+2+2

实际读 [official v1](https://arxiv.org/html/2604.17172v1) §4.1–4.5、§5 的 CopyReducePacks/阶段选择与边界，§6.1–6.4 关键反例。局部 exponent 表与原 sign/fraction 路径、GPU 内融合改变 codec/collective critical path；all_reduce 每阶段重复编解码导致实测慢于两 NCCL 基线。压缩后仍驻留 GPU 的带宽上界不能当实测互联吞吐。§6.2 实际是 prefill→decode KV 传输，不随“parameter disaggregation”措辞虚构权重迁移。

实际对读 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) L1260–1277：tensor 分布、bit-exact/误差、codec 身份、完成顺序、fallback 和端到端验收均有正文。标准 Existing PASS，不宣称 per-block 实现全已写。L40S/A100/H200 与 NCCL2.23.4 default/4SM matched 条件不混，缺少完整应用配置不外推 SLO；官方 v1 CCCL 不继承旧库存 UCCL-Zip 名称与机制。

## 17177 — Depth Profile：仅报告，5 = 2+1+2

实际读 [official v1](https://arxiv.org/html/2604.17177v1) §3.1–3.2、§4.1–4.4/Table1、§6，并定点核尺度 equal-step 的必要说明。post-AdamW 相对更新范数等化保留方向，不等于 Fisher 功能影响等化；标准189/190的表示斜率不能当功能保持。equal-step 的架构/目标交互、参数尺度变化及 encoder 的不同 epoch 预算都限制归因。

标准 Only PASS。实际 Ch29 L575–584 的 trainable-subspace/更新深度 identity 足以阻止一般深度选型外推，但本文具体诊断不假称全部 Existing。保留新干预证据而不把层表示变化曲线直接写成 placement/冻结规则；无实验复现或成本优势验收。

## 17182 — Routing Locality：已有覆盖，6 = 2+2+2

实际读 [official v1](https://arxiv.org/html/2604.17182v1) III-A–E、IV-D、V-E–F 的必要配置/覆盖/反证。Qwen3.5-35B-A3B-FP8、SGLang0.5.9、GH200、thinking skip 和单 C 任务仅支持路由局部测量。route Jaccard 重合不证明 hidden/expert 输出相同；O0 assembly 相同不等一般语义正确。851 completed 是部分搜索，691 compiled、189 groups 与20 sibling pairs 的分母不同，67%不能换成 completed 分母。

实际对读 `MODEL-MOE` [Ch21](../../../../../books/part-02-model/21-moe.md) L298–310：router scores 权威与 batch 执行集合 proposal 分离，quality/fallback/identity 明确。标准 Existing PASS，仅指这个长期边界；不是画像/compile 技术全已写。作者 V-F 明确尚未将 locality 转成 offloading throughput，不能据 route 重合采用 exact forward 共享或性能保证。

## 17187 — React-ing to GH200：仅报告，5 = 1+2+2

实际读 [official v1](https://arxiv.org/html/2604.17187v1) §2、§3.2 与 §6。whole-file parser 把解释文字/结束标记及文件名组成的整行当路径，项目入口无法解析，是实际接口失效案例；无需从单任务推普遍训练缺陷。单 prompt/seed、发布方采样与不同量化混合、特定 aider/backend、trace on request 均限制结论。

实际对读 `AGENT-TOOL-CALLING` [Ch78](../../../../../books/part-07-agent/78-tool-calling.md) L68–84 的 raw output→parse/schema/canonicalization/authorization/effect 与语义校验。标准 Only PASS：保留具体新症状，不伪称此实现已完整 Existing，也不重复写一般链条。没有复现 parser 修复充分性；低利用率不证明 sampling hang 因果，未实测排行榜不能支持 matched hardware 成本。

## 交付与检查

只新增本独立审计文件；未改作者 README/notes、Books 或共享索引，未 stage/commit/push。来源为上述官方 exact-v1；没有全附件、版本差分或全日日期审计。交作者同步17159的必要深入状态及具名复核，其他七项决定无需改变。本组不产生任何新整合项，不替代未完成的 Books23 实际写入或日级 Gate。
