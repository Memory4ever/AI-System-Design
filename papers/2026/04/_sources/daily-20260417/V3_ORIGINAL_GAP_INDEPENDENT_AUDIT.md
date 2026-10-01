# 2026-04-17 V3：三项原始缺口提案独立复核

## 范围与结果

非作者复核仅限 `2604.14403v1`、`2604.14512v1`、`2604.14561v1` 的必要证据与现有 owner 最窄差异。已读本日作者 notes/README 对应记录，实际核验 exact-v1 及目标正文；不触及 14170/14246/14268，不扩展本日分母，不扫描全部附件或版本差异。当前合同沿用已实际阅读的 AGENTS、研究合同、报告合同及统一 Prompt。三项 `2+2+2=6` 可成立，均因确认知识缺口进入必要深入；CBCL 另有安全触发。

| Family | Source→owner 裁决 | 唯一 owner / 拟插入位置 | 当前 Integration 状态 |
| --- | --- | --- | --- |
| SF-2026-ARXIV-2604-14403 | PASS — 共享 retrieval/context 表示的耦合分支确有缺口 | AGENT-RAG，Ch76 compression net-benefit 后 | 提案通过；本审阅未写 Books |
| SF-2026-ARXIV-2604-14512 | PASS — 动态 dialect 安装/展开边界确有缺口 | AGENT-MCP，Ch83 Server Admission 后 | 提案通过；本审阅未写 Books |
| SF-2026-ARXIV-2604-14561 | PASS — readiness 重排与 stale cache 两种合同确有缺口 | TRAIN-DISTRIBUTED-TRAINING，Ch36 CP buffer 后 | 提案通过；本审阅未写 Books |

这里只证明以下受限提案有必要证据及真实章节增量。实际整合、整合后的独立复核和整日日期/覆盖/分母 Gate 仍分别待验收，不据本文件宣布日报 Complete。

## 14403 — ECG：一份持久化表示，同时承担检索与 reader 输入

### 必要证据与反证

实际读取[官方 exact-v1 PDF](https://arxiv.org/pdf/2604.14403v1) §3–5、Tables 1–4；复用[Apr16 缓存](../daily-20260416/exact-v1-bodies/2604.14403v1.pdf)，核页头/标题，另将页4表示公式与页21 Table4渲染后视觉核对。PDF页头的 `15 Apr 2026` 证明版本身份，不单独证明 first-public availability 或本日日界。

§3.2 的关键不是一般 soft compression：共享 decoder 编码后先投影为多向量 `Eret`，第二投影直接从 `Eret` 得到 reader 消费的 `Ecomp`，所以文档只需持久化一份向量。训练联合检索损失与 reader 蒸馏；Table4 去掉 learned temperature/teacher-score scaling 后，SmolLM 的 NQ top1 EM 从 .343 降到 .173，是该训练配方的任务竞争反证，不是多任务一定有害。

SmolLM2 135M/Gemma3 1B、pooled Wikipedia NQ/TriviaQA 与主结果 top1 document 限制外推。预算只计 document vectors，不计 query/format；存储表只计 embeddings，不含完整 index/原文。更多文档可退步，ECG reader 本身也不总优于普通 reader。因此采用“共享表示可减少双份向量与编码路径”这一条件性机制，不采用普遍更强 reader、精确信息保持或手机能耗/latency/SLO 已测的说法。

### 实际缺口与采用边界

[Ch76](../../../../../books/part-07-agent/76-rag.md) 当前 compression 段从 query/evidence/provenance、device/precision 出发选择 retain/compress/bypass，正确保留转换开销、fidelity、原文回取与 realized outcome；但没有同一持久化 retrieval vector 再变换成 generation context 的耦合替代分支。一般压缩 net-benefit 不等于已经承载 index/reader 的共同版本责任。

建议就在该段之后加入有限分支：独立 retriever+compressor 可分别升级与回退；当重复编码和双份文档向量成为主约束，联合训练可用一份表示同时服务 late-interaction retrieval 和 compressed reader。Corpus/index owner 持有文档与向量身份，模型/projection revision 决定 reader 兼容性；这是本项目对状态责任的推导，不是作者已经交付生产版本协议。收益是少存一份和减少重复路径，代价是任务梯度竞争、重新编码/索引维护、reader 耦合与域外 fidelity 风险。分布变化、decoder 升级或质量失败时回退原文/独立索引与压缩器；原文仍须可回取以支持证据、删除和重建，latent 相似度不拥有事实 authority。交接到 Ch75 的 Context packing 和 Ch77 的持久状态仍保持明确，不为论文另建 owner。

## 14512 — CBCL：受治理的语法演化，不是工具能力授权

### 必要证据与反证

[exact-v1 HTML](https://arxiv.org/html/2604.14512v1) §III-B–D、§IV-A–G、§V–VI、§VII-D–E 实际核验。Dialect definition 是可接收的消息，但先经独立验证安装；`lang`/唯一 dialect name 显式分派，template dependency 去环、core 不可重定义，展开受 depth/size/fuel 与 runtime timeout 约束。语法扩展不是未经治理地改变解释器，终止/拒绝和资源上界属于 parser/expander 责任。

作者报告 Lean 模型与 Rust 镜像、差分/fuzz 测试；本轮没有构建 artifact 或复跑证明。Apple M4/macOS15 的 Criterion 微测与 fully-connected gossip 不是生产网络或 Agent 安全验收。§VII 明确 semantic agreement、tool backend/action semantics、密钥分发/撤销与部署级 dialect churn 不在这些保证内；编码/Unicode 实现仍可分歧。不采用 TableI 的端到端能力分类来断言“MCP JSON 输入必然 RE/不可验证”，也不从 parser termination 推出工具无副作用。

### 实际缺口与采用边界

[Ch83](../../../../../books/part-07-agent/83-mcp.md) 现有 Server Admission 校验 identity/tool allowlist/attestation/version，effect-time authorization 再检查 principal/参数/业务 policy；“受限 Tool Program”也已有 type check、sandbox、budget 与 commit。这些不是空白，但尚没有**运行时解释规则自身可安装**的 registry/dispatch state，以及 installation checks 与每次 template expansion 资源执法的分离。

建议紧接 Admission 增加条件性协议分支：固定 schema/静态 adapter 易审计且仍是合理基线；只有多方需要运行时演化词汇时，接收者才持有独立 dialect registry，以 name/content identity 拒绝冲突，并在安装时检查核心语义保留、无循环依赖与声明资源界限，在调用展开时继续执行计数/fuel/timeout、耗尽即拒绝。随后产生的业务请求仍走原授权/effect gate；不能由 dialect 声明自授权限。它用解释规则约束与 registry 生命周期换安全可拒绝性，代价是表达能力上限、版本/命名冲突、安装成本与 churn 管理；需递归/聚合或跨消息语义时交应用层，静态 schema 或拒绝未知 dialect 仍可回退。只采用 bounded language evolution 的机制，不把 CBCL 写成 MCP 新规范或替代全部业务授权。多 Agent 传播交接 Ch82，最终执行控制交接 Ch84/安全层，不复制 grammar owner。

## 14561 — CoCoDiff：精确的通信重排与近似的跨步缓存要分账

### 必要证据与反证

[exact-v1 HTML](https://arxiv.org/html/2604.14561v1) §III-B–E、§IV-A–F 实际核验。TAPA 重排 tile/head/sequence 交换；V-First 利用所测 DiT 的 V 无 QK normalization/RoPE、较早 ready 的窗口先发 phase1，并不因此删掉本步 QKV。V-Major 是另一机制：用 V 变化作 Q/K/V 共用选择 proxy、all-gather 一致索引，接收端 scatter 活跃值并保留旧值；warmup 和周期 full refresh 不能使中间选择步变成 exact。

证据绑定 Intel Max1550/Aurora、12–96 tiles、PyTorch2.10/IPEX/oneCCL2021.17、四 DiT、50 denoising steps、三次运行；大 batch 可暴露通信，cache 可触发 OOM，Ulysses head 饱和后 Ring 通信未优化。TableII 的脑片 inpainting 已有 SD3.5 center PSNR 23.65→21.95、SSIM .8390→.8075 退步；不采用作者“noise floor/影响可忽略”作为质量保证。此结果不是自然图像全质量、production concurrency/tail SLO，也不是训练收敛等价证明。

### 实际缺口与采用边界

[Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) CP buffer 主线已有一次性 all-head→head-stage→bounded buffer 重用，也有低维 projection 的有损通信分支。前者按 head 切容量，后者传本步近似值；都没有按 **Q/K/V readiness** 提前启动交换，亦没有跨 denoising step 的 age/mask/refresh 状态。故具体 gap PASS，而不是只因现有章含 Ulysses 即判 Existing。

建议在 CP buffer 段后分两层说明：先保留当前 tensor 的 exact topology/layout 重排，runtime 仍负责顺序、完成与 attention-ready；可隐藏部分由通信与 QK 计算窗口的相对大小决定。这里 exact 指不删去或替换本步 tensor 值，不声称实际重排 kernel 已证明逐 bit 重放一致。再显式标注 **DiT 推理的近似分支**：缓存身份绑定 step/layer/token/head，所有 rank 使用同一 mask，scheduler 控制 refresh/fallback，模型质量验收决定 stale budget 是否可接受。V 稳定不证明 Q/K 同样稳定，也不证明 error bounded；full refresh、停用 cache、原始 all-to-all 都是合法回退。代价包括额外 tensor 驻留、mask/all-gather/scatter、staleness 和未优化 Ring 瓶颈。由于 Ch36 的主线仍是训练语义不变量，不能把推理期近似缓存无标记移植进训练；后续 Inference 章节只交接 workload/quality/SLO，不再次拥有 collective 原理。

## 验收与后续

三项确认真实窄缺口，提案可进入作者必要 Books 写入；本文件不代表它们已经整合。作者写入后，应核实际机制、负面结果、旧路径共存与相邻交接，再更新报告处置。只修改本独立 audit；日期归属仍交整日 lane，本轮没有重新启动发现、扩池或无关复审。
