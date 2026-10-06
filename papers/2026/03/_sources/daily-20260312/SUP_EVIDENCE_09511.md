# 2603.09511v1 — TrainDeeploy

作者实际必要Source：2026-10-09；[exact-v1 HTML](https://arxiv.org/html/2603.09511v1) §II-B、§IV全部、§V全部、§VI全部、§VII实际读。完整题摘及当前history无withdraw/correction说明；DATE2026 accepted不是先公开证据，v1首页明确最终版将出IEEE Xplore。arxiv公开日按本日availability下界+owning findable DOI上界同BJT03-11夹证，不以Submitted/registered单独充公开日期。

准入：MCU的参数高效适配仍卡住activation/完整反向与搬运 → 把ONNX前向符号微分、optimizer subgraph、完整forward/backward tensor liveness与kernel tile约束联合静态调度，并配FP32 GEMM offload → 必须重新比较trainable state下降与实际accelerator吞吐，而非按rank比例承诺加速。2+2+2=6；具体TRAIN-LORA owner差额须深入必要内容，非所有设备通用最优。

方法：§IV把完整训练图静态表示后以constraint programming联合tiling/liveness，2D bin-packing static allocation，L1 active tiles/L2 weights-activation-gradient/L3 spill；backend C code安排布局转换、CPU与accelerator同步。LoRA减少weight gradient/optimizer，不取消input gradient或原activation。文中TetriSched与MiniMalloc的具体职责命名不完全统一，本轮只采用联合静态调度机制，不补实现细节或解最优性。

条件与反侧：§V-B是GVSoC event-based模拟，不是本轮核实硅片部署；8RV32cores共享4FPUs、128KB L1/2MB L2/32MB HyperRAM L3、FP32扩展RedMulE 12×4 systolic，以360MHz假定频率。CCT-2为0.28M vision Transformer、rank4、冻结conv tokenizer；不是LLM端侧训练验证。设备性能为SGD/batch1单样本step；transfer accuracy另为SGD/batch8/100epochs/50-shot/30重复、取末5epochs均值，两协议不能合并为同一线上质量-吞吐证明。

§VI-B/fig5–6同硬件8核无RedMulE vs有RedMulE为2.3–3.5x模拟runtime；FT-2与LoRA-2 trainable0.76MB→0.05MB，动态L3 footprint减19–23%、transfer0.62x，dynamic memory不含固定1.12MBweights/input。重要反侧：加速后LoRA可能略慢于FT，因为许多小矩阵利用率较低、频繁低秩transfer overhead。TableI EuroSAT FT-2 81.52±.36高于LoRA-2 80.50±.41；MNIST LoRA更高。FullFT冻结范围不同，不用FullFT64.85→LoRA80.50宣称结构净收益。TableII不同模型/硬件/稀疏与paging参数，3–10x不作统一公平跨框架速度保证；同Deep-AE PULP comparison只支持其给定模拟配置。

采用：完整graph调度与低秩small-GEMM实际执行分账这条窄可行性边界。未执行artifact或复现；SLO/concurrency/能耗与真实硅片训练未由本轮验证。拟Books owner TRAIN-LORA的“为什么会节省训练显存”已明确freeze仍需input gradient、activation/workspace及trainable比例不等FLOPs；缺额是编译时full-FW/BW tiling/liveness与小矩阵accelerator利用率可能反转FT/LoRA速度。读取现Ch30该小节及前后参数化/轮流层更新内容；拟两段与必要末注另交非作者PRE，不先声称已整合。
