# Apr20 两项有限非作者 source→owner 核验

复核者：apr02，非本日作者。仅核必要 exact-v1 方法、评价/反证及当前具体正文；未写 Books，不核全日来源/日期/分母，不代表日级 Gate。两项拟7分深入的主线贡献成立，不因边缘硬件、日志场景或已有大主题关闭。

## 15357 FLAME：窄采用 PASS，待实际写后

实际打开[官方v1](https://arxiv.org/html/2604.15357v1) §III-A/B、IV、V、VI-A与VI-B消融、VI-C/D；对读 Ch70「资源时间是共同底座」「执行中闲置与 Deep Idle」「GPU Power Budget」及 Minos 双近邻曲线。现文已有频率/功率、驻留压力与实测回退，却没有 CPU launch 与 GPU execution 的频率依赖重叠→跨层 timeline 聚合这条成本预测分支。支持在 profiling 曲线论证附近窄补两段：先分开主机提交和设备执行，再估计耦合及跨层重叠；不同频率改变等待/重叠，不能独立缩放或逐层时延相加。保留离线采样、计数器/层类型失配、校准与实测回退；第49章仍拥有 kernel 实现，第56章拥有实际调度。

Eq2/4是拟合，Fig16两消融支持受限必要性，不是所有 runtime 定律。Eq13/14是先固定 CPU 最大再选 GPU、再降 CPU 的 greedy，不是全局功耗最优证明。Eq10–11自引用 EWMA 不自行补成已验证实现。评价 Jetson AGX Orin/Orin NX、所列 DNN/GPT2/Qwen2 decode、PyTorch/Transformers、上下文至1024、INA3221；平均 MAPE 与 rate-ratio QoS 不能升级 tail/deadline 成功概率。precision、并发及生产SLO未披露的不能补造。未复现实验。

## 15368 LogJack：窄采用 PASS，待实际写后

实际打开[官方v1](https://arxiv.org/html/2604.15368v1) §III–VII 的必要方法/主表/限制；对读 Ch72「从文本是否恶意到谁获得行为控制权」及 monitor/确定性 tool policy 段。已有 authority 分离不能说明该证据已完整承载：同 payload 的裸文本与日志包装检测差异，以及删 exfil URL 后仍提 SSM 修改动作，是值得进入原论证的具体失败边界。窄补包装配对测试和清洗后 action 再授权；不新增一套安全架构，也不声称 sanitizer 全无用。

§V-A明确扫描只记录、action tool 拦截/分类而不执行；因此作者“RCE”表仅支持危险 proposal，不能写真实远程效应。32攻击+10良性、8模型、三prompt、每项5次/temperature0.7、最多8轮且首危险动作后停。verbatim 与其他危险命令分账；regex 未外验，Llama良性44%限制攻击归因。Bedrock未扫描tool result不应同其他provider零检测合并，清洗案例没有频率估计。安全改动只支持该受限失效与 effect gate 责任，不是生产防御保证。未复现实验。
