# 2604.25699v1 NVLLM：3D NAND 内计算的负载分工与纠错时序

作者侧必要审阅，非独立 Gate。[official exact-v1 HTML](https://arxiv.org/html/2604.25699v1) §2.2、§3.1–3.5、§4.1–4.5；[v1 身份](https://arxiv.org/abs/2604.25699v1)。页眉 28 Apr/提交字段不单独证明首公开；本日 `24765–25918` 官方公告批次联合链见 [检查点](./V3_REOPEN_NOTES.md)，有更早独立公开正文时仍须按家族重开。本篇已在 106 份完整题摘的 70 项潜在线索中，不增加分母。

## 贡献、机制与受限证据

这不是把普通 GPU 推理换个“edge”应用。作者面对单请求、长 decode 的低算强度和 NAND 原始读错误，把相对规则且权重占大的 FFN 放在 3D NAND/CMOS 内执行，把不规则、随 KV 增长的 attention 与 Q/K/V/O 权重保留在 NPU/LPDDR；plane cluster 的 page-buffer 宽度与 PE lane 消费宽度共设计，错误检测走常见快路径、纠正入 scoreboard/共享慢路径，再以 KV 负载改变一部分 projection 的执行位置。这把**权重搬运、介质错误时序与 phase-specific 工作集**置于同一端侧执行方案，较 Ch54 一般 memory hierarchy/静态 offload 有具体分支。作者的 Algorithm 1 对待纠错 segment 不先 MAC，纠正后从 scoreboard 补加；这能解释为何“直接算 raw read”并非无条件容忍错误。

§4.1 不是流片产品：3D-FPIM＋Ramulator2/DRAMPower＋cycle-accurate C++ 模拟，28nm RTL synthesis 用于部分 CMOS 面积/功率估计；OPT 1.3B–30B 与部分 LLaMA INT8，注入 NAND RBER。base 32 planes/8 clusters，`NVLLM-16C` 64 planes/16 clusters，不能把各配置数字交叉拼成同一原型。Fig. 6 的 decode 测例固定 64-token context；摘要 `16.7×–37.9×` 对 A800 **out-of-core / GPU-SSD** 路径，§4.3 的 `22.4×–37.9×` 亦明确相对此瓶颈，不是相对同容量 in-memory GPU 的通用加速。SSD-like AiF 对照 `1.3×`，显著小于最高 headline；Fig. 7 的端到端 `1.9/7.5/30.3/124.3 s` 是给定 32/128/512/2048 token pair、且缺 Cambricon/AiF prefill 数据的 GPU 对照。§4.5 的 `5.63×` 是 **data movement energy** 对 Cambricon-LLM，不是整机每 token 能耗。

误差/性能验证仍有空白：正文称常见错误可异步纠正并保持 MAC，§3.3 又把连续错误概率低当作无 stall 解释；没有据此得到任意老化/RBER/温度/长上下文下的确定吞吐。Attention 在 LPDDR 路径，KV 增长与调度 bitmap 可能把原 FFN 带宽收益搬成 attention/纠错拥塞；Fig. 8(a) 只支持作者模拟点。未提供真实 3D NAND+CMOS 样片的制造、热、寿命、firmware 与 tail-SLO 验收；不能称其“已在端侧设备部署”。

## 评分与实际 owner

拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`、Standard。它给出具体硬件—算法分工及受限设计点，但未建立跨硬件/真实硅性能定律。`ROADMAP` 的 `INFER-GPU-MEMORY` → [Ch54](../../../../../books/part-05-inference-system/54-gpu-memory.md) 在 memory hierarchy/phase-specific working-set、PIM logical view、HBM ECC exception path 和 Compute-in-Flash KV 表示分别已有论点；不过**FFN 权重在 NAND 内执行时，raw-read 错误检测/纠正是否阻断 PE，与 attention/KV 的 LPDDR 工作集如何共同决定瓶颈**没有作为同一可执行分支出现。Ch49 已涵盖 GPU/NPU kernel 与 PIM 执行布局，不宜以产品/论文名复制这套方案；唯一候选 owner 更接近 Ch54 的 memory placement/可靠性分账。

最窄 source→actual-owner 写前提案（需非作者核、root 授共享锁后才可写）：在 Ch54 memory hierarchy/phase-specific working-set 与 HBM 可靠性之间加两段，先说明常规权重 offload 先搬数据再算、在单请求 decode 下可能受介质—总线搬运限制；若重量级 FFN 留 3D NAND 内、attention/KV 留 DRAM，执行权应以 page/PE 配宽、纠错异常路径、KV 增长三项共同验收。第二段说明它以专用 W2W 硬件、ECC/scheduling 状态、老化/热/精度风险换掉重复 weight movement；§4 模拟与部分 RTL synthesis 只提示候选设计，未满足真实 silicon、同容量/成本/功率及端到端尾延迟合同，条件失败回退普通 DRAM/GPU 或 SSD offload。**不采用任何 headline 倍率作一般正文承诺**。若非作者认为 Ch54 已具体承载同一物理分工及错误时序，应按真实段落裁 `Existing`；不能以“可讲 memory hierarchy”替代实际比较。

本项 Books 暂记 `拟窄 Integrate／待非作者 source→owner`，不是已整合、不是日级完成；无共享文件修改。
