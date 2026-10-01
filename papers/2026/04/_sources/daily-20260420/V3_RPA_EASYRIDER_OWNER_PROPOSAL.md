# RPA / EasyRider 两项有限 owner 提案

作者：apr20_resume；两项均2+2+2=6，实际缺口触发必要深入。Ch49/Ch70 最小两段及 Review notes 已实写，root 真实写后通过并释放锁；本文件下列文字保留为写前提案，最终状态见 `V3_ROOT_FINITE_INDEPENDENT.md`。未签整日Gate。

## 15464 RPA → INFER-TENSORRT-LLM Ch49

[official exact-v1](https://arxiv.org/html/2604.15464v1) §3.1–3.7/Algorithm1/§4.1–4.4。实际读Ch49:1471–1498：SGLang-JAX已有scheduler/backend ABI及离散shape预编译，缺少固定capacity shape与有效ragged分布、HLO layout survival分责。拟接SGLang-JAX段后、现有“算法结构也会决定compiler...”前两段：

> 后端预编译需要固定 tensor capacity，却不代表有效请求长度也固定。对有 tiled memory 和静态 vector-register compute blocks 的 TPU，可以把 ragged 维移出被硬件平铺的末维，增加 packing 维并合并 K/V，让有效页数据由动态 DMA 取得，再把 KV 更新与 Attention 流水线重叠。Compiler 的 layout assignment 仍可能重排投影后的中间张量，因而离线 weight reshape 不当然消除在线 preprocessing；plan 必须验证 custom-kernel 边界的真实 layout，并保留转换成本，而不只保存逻辑 shape。
>
> 启动时将最大 token/sequence 数作为 capacity envelope，padding 到静态 shape 可避免 JIT 重编译进入请求关键路径，但动态 DMA 不会消除静态 compute tile 的浪费。同一 capacity 下，不同有效长度分布仍需不同 decode、fixed-chunk prefill 或 mixed block 配置，调优与预编译应共同绑定该分布。受限 [RPA v1](https://arxiv.org/html/2604.15464v1) 的 TPU7x/Llama3-8B/BF16 测量只在足够长 context 或 prefill 饱和时取得高利用率；prefill preprocessing 仍占约2%～8%，其 d=128 MFU 分母还按50%最大MXU使用率调整，不能当成全芯片或全请求收益。高度 ragged、未覆盖shape或layout改变时，成熟 padded/general kernel 与重新编译验证仍是回退，不从历史后端吞吐演进推通用生产SLO。

Review拟仅保存source family15464/Experimental、必要§3/4、上述配置、firstpaper不重计2025 artifact release、mixed优化future及全请求/质量/CI限制。与15408是不同ID/正文，不按名字近似合并。

## 15522 EasyRider → PLATFORM-COST Ch70

[official exact-v1](https://arxiv.org/html/2604.15522v1) §3/4/5.3–5.4/6/7.1–7.4/8/B.2。实际读Ch70:250–286及既有能耗/actuator段，power-delivery静态capacity已有，尚缺瞬态波形与总energy/训练控制分责。拟接“Installed Power不是可部署AI Capacity”段及原source-marker之后、“水耗从事后...”之前两段：

> 可部署功率还不能只用峰值或总 energy 描述。同步训练、checkpoint 与启停会使机架瞬时功率迅速变化；设施侧的 ramp-rate 和频谱预算可能先于平均功率触限。一个替代分支不改变训练步骤，而在机架电源边界分开处理时间尺度：被动滤波吸收较快变化，双向辅助储能吸收或释放较慢的功率差，慢速 controller 再纠正损耗与偏置造成的 state-of-charge 漂移。储能需要的容量由功率差对时间的积分决定，波形平滑不是能量免费，也不等于平均功耗减少。
>
> 这条分支用额外硬件、转换损耗、热与寿命管理换取训练控制和设施瞬态之间的解耦；过滤只在额定功率、电流、SoC 与可用 headroom 内成立，软件离线后也不能无期限忽略漂移。受限 [EasyRider v1](https://arxiv.org/html/2604.15522v1) 的400VDC、10kW原型及两TitanX/125M训练trace对照支持局部波形与能量取舍，不证明完整MW级电网合规或电池寿命；低电压受25A上限限制，慢controller实验只核inner-loop恢复而非长期aging。Headroom不足、设施接口不相容或额外损耗无法摊销时，原有power cap、负载协调和保守容量预算仍共存，成本账本应同时记录波形条件、buffer损耗与训练完成成本。

Review拟保存family15522/Experimental、原型/trace/normalized演示spec与burn条件、outer-lifetime未验、SoC/headroom、GB200成本仅推算；不采用B.2任意初始状态下全局QP保证或全部grid通用规则。

两项 root 源→actualowner、literal 与真实写后均通过，见 `V3_ROOT_FINITE_INDEPENDENT.md`；本文件不替代独立整日验收。
