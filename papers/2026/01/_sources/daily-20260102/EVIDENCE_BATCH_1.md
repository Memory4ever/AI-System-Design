# Jan02 首四项必要正文证据（非作者原源与Books写后复核通过）

日期原值见DATACITE_25.json；四项v1 Submitted均在holiday缓冲，ID/DOI注册2026-01-01T03Z，结合官方holiday/noadvance-ID界定[01:00Z,created+1秒)，均完整本窗；不把注册当精确公开。各项仅作者实验，无复现/生产保证。root实际原源、限定命题及Ch36/54/27/35正文、相关邻接、末注写后已通过；这不是Jan02日级完成。

## [R2CCL — 2512.25059v1](https://arxiv.org/html/2512.25059v1)

评分2+3+3=8。§4 failure diagnosis/recovery：OOB通知和独立QP probe区分NIC/link；同GPU buffer预注册备用NIC、chunk completion/ACK边界要求发送端退回首个未完成chunk，接收端重置到最后确认的进度，再迁移重传；不消费未完成RDMA，才可同participant迁移。§5 single-failure scheduling、§6 multi-failure scheduling的AllReduce部分/全局重分解和Balance适用消息尺寸不同，不能用固定32MB阈值跨硬件。故障域不含GPU/NVLink/NVSwitch或无存活路径的分区。§8 evaluation：两节点各8H100/8×400G IB实机，与32–1024 A100 Spectrum-X模拟分开；GPT-3 2.7B DP与13B TP/PP训练恢复只能支持该NIC失效。Serving以Llama3.1 70B/405B合成2000prompt、≤256 output和5sTTFT/0.4sP95TPOT作QPS约束；precision Not Disclosed。47×是与DéjàVu在指定故障恢复实验的额外overhead比，不是吞吐加速。新增长期命题是transport部分故障可保留rank/group，前提是完成/重传边界受runtime拥有，不由诊断自动授权局部继续。已在TRAIN-DISTRIBUTED-TRAINING（Ch36，Legacy32）elastic→SPARe交接处融入两段。

## [MSched — 2512.24637v1](https://arxiv.org/html/2512.24637v1)

评分2+3+3=8。§5–6：offline NVBit profile建fixed/linear/strided launch-argument模板，online按页预测；prediction error通过原demandpaging fallback，pointer-chasing未由三模板覆盖。Scheduler公开task timeline，让memorymanager在context switch按未来访问顺序重排driver eviction，并双CE迁移、依赖页ready后early compute；OPT受已知时间线/延迟/working-set条件约束，不是任意动态负载全知最优。§7 RTX5080 16GB、Intel285K/96GB DDR5、Ubuntu24.04/driver580.95.05/CUDA12.9/XSched RR；int8 Llama3-8B llama.cpp多process在150/200/300%显存申请，相比UM thrashing而不是优化serving，33.6–57.9×不能跨协议。预测消融把allocation误迁移与template分开；control-plane随task数增长。作者将消费卡显存称HBM，不采其存储类型措辞。新增是context还需随scheduler移交真实working-set，而不只arch state。

## [Data Recipe Proxy — 2512.24503v1](https://arxiv.org/html/2512.24503v1)

评分3+2+3=8，评价反证深入。§3–5/Tables/Figs与Appendix理论：同一learningrate不是dataset公平比较，因为各recipe optimum不同；低但非任意趋零的proxy LR降低曲率影响，使早期gradient-alignment排序更接近各recipe独立调优的target。23 recipes、GPT2/Pythia/OPT70M–1B、单epoch1024context、proxy FP32/target BF16、AdamW/WSD grid；tiny更新会被FP32舍入，不能推越小越好。理论是random-feature宽度、小η、rankgap/curvature条件，不是Transformer普遍证明；未支持多epoch/curriculum外推。新增长期命题是固定训练配置的data排序与joint data/config最优是不同被估计量。

## [Checkpoint I/O — 2512.24511v1](https://arxiv.org/html/2512.24511v1)

评分3+2+2=7，benchmark可比性反证深入。§2–3/Figs3–12：tensor/logicalobject、read request与file粒度不同；preallocated aligned contiguous liburing microbench不含framework metadata/serialization/hostallocation。真实BLOOM3B/LLaMA7/13B checkpoint layout在4/8/16 ranks有大量小且不齐buffer，aggregation需padding/offset协调，不能由singlelargefile直接保证端到端最优。Polaris每node4A10040GB/512GB DDR4，Lustre64MBstripe，liburing2.12/gcc13.3.1。§3.4 direct/cached I/O：孤立小读microbenchmark的cache收益不足以授权混合路径；作者实测O_DIRECT write/buffered read没有改善，至多比write/read均direct差3×。§3.5 restore allocation/framework比较：扣除allocation显著缩小差距，不能把差全归IO backend。长期命题是flush bandwidth、tensor restore pipeline和可恢复checkpoint不是同一cost contract；perf未披露precision/训练输入长度不影响I/O粒度分析，不能据此宣称训练加速。
