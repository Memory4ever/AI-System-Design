# 2026-04-30 Ch54 两条 KV 分层 Books 写前包（作者提案，未获锁）

`26557` 改变同一 NVMe 容量的 I/O **路径**，`26837` 改变多种稀疏 attention 与 KV offload 共用的 **职责接口与元数据工作集**；二者都不重定义 KV 语义、内容真值或 Ch22 算法本身。以下仅供 root 非作者 `exact-v1 → 最新 Ch54` 判断，不能由“同章有 tiering”机械判 Existing，也不能在 shared Ch54 未授权时当已整合。

## 2604.26557v1 Dual-Blade：page-cache 与 direct-LBA 双路径

- 必要来源：[官方 exact-v1 §III-D、§IV-A–C、§V-B–E](https://arxiv.org/html/2604.26557v1)。初始化估计 host page-cache budget，再以 layer K/V unit 将 NVMe extents 配给文件页缓存路径或跳过文件系统的顺序 LBA 路径；后者仍通过 pinned DRAM buffer，不是 SSD→GPU 直达，也不是运行中任意 hot migration。
- [Ch54 当前层级段](../../../../../books/part-05-inference-system/54-gpu-memory.md)已有 host/NVMe/CXL 容量、page-cache 管理与 SPDK 直 I/O 的一般选择；缺同一存储资产的 **按 layer KV unit 两路径共存、extent identity 与初始化预算**。若现有两段已足以指导该选择，报告 Only 即可；若不够，建议落在 NAND/CXL 计划与一般 offload 的相邻位置，不把它写成新增 cache tier。
- 拟正文：`同一 NVMe 后端也可能需要两种不等价的取回路径。Host DRAM 富余时，文件页缓存可复用被读取的 layer K/V units 并交给成熟回收机制；预算紧、顺序读取更可预测时，按 LBA 管理对齐 extent、用 pinned DRAM 缓冲和异步队列跳过文件缓存，可能减少双重缓存与软件开销。运行时需在初始化时绑定 unit→path、extent 版本和持久/回收责任，再决定何时预取，而不能把“SSD 空间足够”当作可消费 KV 已就绪。`
- 代价/反证：`双路径引入 extent 对齐/不重叠、空间回收、写持久性和 I/O 队列的维护；全 direct 在作者 DRAM 富余切片反而最慢。Edge OPT、两 SSD、2–11GB host cap 的测试不足以证明多请求生产尾延迟或在线热迁移；页缓存命中稳定时保留单一路径，设备/驱动不提供必要能力时保留普通 staged read。`

## 2604.26837v1 SPIN：稀疏算法与运行时分页职责拆分

- 必要来源：[官方 exact-v1 §4–6](https://arxiv.org/html/2604.26837v1)。不同 sparse attention 方法被拆为 `Index/Select/Attention` 的算法职责，与 `Offload/Retrieve` 的物理运行时职责；head-wise 稀疏状态若按 `max_batch × max_context/pages × layers × heads` 全量预留 page metadata，可先于 KV bytes 成为 HBM 压力，故做活跃页的 GPU/CPU 两级 metadata 工作集。
- [Ch54 当前内存层级](../../../../../books/part-05-inference-system/54-gpu-memory.md)已描述 KV paging/offload 及一般 metadata 成本，Ch22 拥有 sparse attention selector；当前未将两方的 **选择身份/版本、物理页映射与 active metadata 容量** 作为可复用接口。建议 Ch54 在 KV tier/allocator 段窄写，Ch22 不复制论文算法。
- 拟正文：`稀疏 attention 先选“哪些历史位置可读”，offload runtime 再决定“这些位置的页何时在哪层可用”；二者若在一个 kernel 中混成隐式状态，每换一种 selector 就可能重写分页与 fault 恢复。更稳定的接口让算法提交带版本的 Index/Select 结果，物理层据此 Offload/Retrieve，Attention 只消费已 ready 且与请求、层、head 身份相符的页。Selector 可以变，但物理映射、完成顺序和缺页回退仍由 runtime 拥有。`
- 元数据与边界：`稀疏不意味着页表可忽略：按最坏 batch/context/head 全量预留 metadata 可能吃掉本要节省的 HBM，应把活跃物理页的映射留在 GPU，冷页目录下沉 host，并将查找、resize、fault、迁移和质量一起计入预算。作者 4×A100/4×B200、所列 sparse 算法/LongBench 与生成测试支持受限系统效应，但与 dense vLLM 的差值同时混入算法选择；在线大负载 TTFT 因排队可能下降，TPOT 反高于 dense。稀疏质量不达标、元数据或 PCIe 延迟主导时，保留 dense/full-resident 路径。`
- 决定点：最新 Ch54 若已有同一稀疏算法/分页 adapter 与 active physical metadata 工作集的完整链，应判 Existing。否则只采用上述职责/成本条件，不借 throughput 数字宣称任意模型的 sparse serving 优越。
