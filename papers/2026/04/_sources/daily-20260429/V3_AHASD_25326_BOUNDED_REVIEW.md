# 2604.25326v1 AHASD：异构异步草稿与预验证的条件边界

## 贡献与必要机制

[官方 exact-v1](https://arxiv.org/html/2604.25326v1)题名 *AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices*。旧 60 完整题摘的具体问题成立：原 NPU/PIM 的 operator-level 同步方案在 adaptive draft 长度波动时会互等；单纯改 task-level 异步虽然重叠计算，却让尚未被 target 验证的 draft 越跑越远、接受率下降。§4.1 将 PIM/DLM proposal、NPU/TLM verify、反馈与 pre-verification 三队列分权；§4.2 用 entropy history 加领先未验证 batch 数估计继续 look-ahead 的价值，target 实际验证后更新/回滚；§4.3 以双方近期 cycles、剩余 NPU verification time 与至少一批新 draft 的保留预算，决定何时让 PIM 提前验证短批。若成立，长期选择不再是“异步总比同步快”，而是把 draft lead、acceptance、两设备剩余时间与回滚成本同写入异构调度条件。作者侧建议 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9` 标准候选；小模型/端侧不是硬拒理由。

## 评价、旧路线与停止条件

§5.1 不是量产 NPU-PIM 实板：作者联结 ONNXim 与 SAITPublic-PIMSimulator 两个 cycle-level 模拟器，CPU 控制逻辑接入 Xiangshan；Table 2 定 16 TOPS NPU、16 个 PIM 单元、LPDDR5 带宽/时序。三组 draft/target 分别是 OPT 1.3B/6.7B、LLaMA2 7B/13B、PaLM-like 8B/30B，均 INT8；四种 adaptive draft 算法、Alpaca、batch1、输出长 1024。§5.2 消融的纯异步分支**接受率平均下降 25.1%**、吞吐相对基线平均增至 `2.2×`，加入 AAU→`2.7×`、EDC→`3.4×`、TVC→`3.8×`；这给新增控制件的方向性证据，但不能把 4.2×／5.6× 最大值当每模型平均，也不能把 NPU+PIM 与 GPU-only 的芯片/功耗条件视为 matched hardware。§5.3 对 SpecPIM 的最多 `1.5×` 吞吐、平均约 `1.24×` 能效同样是作者重建的 GPU+PIM baseline 与其模拟平台之间的比较，不是同一硅片仅开关调度器。§5.4 的 `2.68%` area 是 28nm 合成估算，不代表制造良率或真实 DRAM 周边面积已验。

Target 模型而非 DLM 是 accept/commit owner；§3/4.1 明说 PIM 预验证时可切到存有 **TLM 参数的 rank**，故不能误写成“PIM 仅用 draft 模型做启发式过滤”。但论文没有独立给出 PIM/TLM 预验证和 NPU/TLM 主验证在量化、采样及状态交接上的逐 token 等价证明，平均接受率亦不构成 target distribution 保真证明；任何直接提交必须另受同一 target-verification 合同约束。若短输出、低预测精度、PIM 小批验证比当前 NPU 余时更慢、三队列通信/刷新过重，operator-level 同步或普通 target decode 可继续合理。作者没有实测多并发/长上下文、端到端移动设备功耗与尾时延；其 `4.2×` 最大吞吐不是生产 SLA。

## 真实 owner 与首公开例外

[Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md) 已分别有 exact acceptance/commit、acceptance 与成本分账、按 request 的 async draft/verify 混合调度（约 282 行）以及 stale proposal 绑定 prefix/version、取消、回退（约 699 行）。现文尚未具体说在 NPU/PIM **异构双资源**中应按领先批数/接受率与剩余 verify window 共同调度 PIM pre-verify，且 pre-verify 要留至少一批新 draft 的时间；这是可能的最窄长期 gap，不能只凭“Ch48 谈异步”声称已有完整覆盖。但其三硬件模块与 1024-token 模拟数字未必值得正文。非作者若确认日期与真 gap，可在 async/state 段后补一条条件性异构分支：proposal/verify/commit 分权，预计 acceptance 与双设备剩余时间一起决定继续草稿、暂停或预验证；实际 target 仍最终确认；短输出/低命中/transfer 成本高时回同步。共享 Ch48 未授锁，当前不写 Books。

**本项当前存在强的早公开线索，不能签 `new_in_window`：** [作者 GitHub 仓库](https://github.com/MAdrid1011/AHASD) API 记 `created_at=2025-11-09T07:17:27Z`；[11/09 初始提交](https://github.com/MAdrid1011/AHASD/commit/089e3086249b)只有 AHASD 模拟器一句简介，但[11/14 文档提交](https://github.com/MAdrid1011/AHASD/commit/203a3f64c61d)的 README 已写异步 NPU/PIM、EDC entropy-history、TVC time-aware pre-verify、AAU 与和论文一致的最高 `4.2×/5.6×` 数字，[11/17](https://github.com/MAdrid1011/AHASD/commit/819c18da9799)又更新到论文主标题。**若仓库当时 public，中心机制很可能属于 2025/11 而非本日**；但 Git object/作者时钟、现时 public 属性不构成历史公共可见性证明，也不能直接判其当时方法与最终论文逐细节同一。当前唯一已核正文仍是本日 arXiv ID 公告批；需要仓库早期 public archive/平台日志或当时作者正式发布页才能判例外。此单项日期具名隔离，不拖住其它 04/29 工作，也不因未证日期冒写 Books。
