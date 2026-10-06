# 2603.10342v1 AgentServe 必要 Source / 已有覆盖提案

窗Mar12 BJT；准入/本arxiv事件日级日期复用第二包。`SUP_CORE_10342.raw` 精确v1 GET200，2026-10-09T13:27:42Z。作者实际读III-A/B全部设计与Algorithm1、理论三个主要资格假设，III-C全部执行设计、IV-A–E全部评价文字及TableI；未读全部竞争比证明/图像点值，不采用理论最优或精确曲线。GPU能力的必要反侧仅定点官方CUDA12.4.1 Green Context及550.54.15发布说明，不扩大research source范围。

## 决定方法/评价

- 三phase：cold独立queue/thread，resume长度小于token budget进decode queue，长resume进cold；step TPOT两阈值反馈同时缩放resume预算和decode SM floor。Algorithm1 `decode OR req.len<=B`未显式限resume，和主文cold始终分开表述不完全一致；只有实际实现能澄清冷短prompt归类，不把此伪代码当已复现scheduler。
- 10个预建GreenContexts10%→100%，按目标向上选slot、用补集prefill；共享GPU memory pool、CPU mutex保护allocate/free，cudaEvent等prefill完成才decode消费，readonly标注仍须实机KV生命周期验收。理论假设throughput单调、SM overshoot有界/可行SLO、control overhead有界，不授任意burst保证。
- llama.cpp扩展；Qwen2.5-3/7B、Llama3-8B，3–6并发ToolBench-derived ReAct/P&E短生成。TableI cold2.5–3.5k，ReAct resume30–127平均56、decode约21–127；P&E resume125–421平均251、decode22–141。不是长coding/reasoning或production多GPU。
- IV报告TTFT/TPOT p50/p95、throughput、session联合TTFT/TPOT SLO；阈值按isolated profile乘固定factor，但未给factor/绝对阈值。2.8×是对llama.cpp重负载TTFT，不是所有baseline/端到端任务。NoAlg静态SM、NoGreen移除预建slot且decode reservation，非只变一个实现成本；baseline版本、quantization、请求统计总分母/重复区间未完整披露。

## 原能力/身份反侧

官方[CUDA12.4.1 Green Context API](https://docs.nvidia.com/cuda/archive/12.4.1/cuda-driver-api/group__CUDA__GREEN__CONTEXTS.html) 原件 `SUP_AGENT_SERVE_GC124.raw` 实际读概要/partition粒度/forward-progress段：disjoint SM也不保证并发或forward progress，HW connections等可产生依赖；SM粒度受architecture约束，不是任意精确10%分区。论文III-A称uninterrupted compute **and memory bandwidth**、III-C“not starved”不可作硬保证。

IV-A给两平台皆CUDA12.4/driver550.54.15，并把5090写16384CUDAcores/128SM。官方[5090产品](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)直接正文定义Blackwell32GB，当前完整Specs又明确CUDA cores21760，与稿中16384不同；原件 `SUP_AGENT_SERVE_5090.raw` 已保存（web直接全文Specs也已读）。[550.54.15说明](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-550-54-15/index.html) 原件 `SUP_AGENT_SERVE_DRIVER550.raw` 实际支持架构列至Ada、没有Blackwell。这不能验证该5090实验平台身份，须作者精确硬件/driver与编译/运行日志澄清，不推造假或全部A5000观察无效。官方570页面仅搜索结果能显示产品列表、当前直接raw shell未返回列表，**不把索引当软件兼容原证**，不声称最低版本已核；同理旧CUDA toolkit的PTX前向兼容不由以上否定。

## actual唯一owner与Books判定

ROADMAP `INFER-SCHEDULING` Ch56。作者实际读840–875完整局部（10335之后行号可能平移、正文不变）；原858完整AgentServe段已有**同精确v1**三phase、TPOT→resume budget/SM floor、GreenContext资源分区、oscillation/fragmentation/调参成本、无拥塞回退、单consumerGPU/不证明多GPU生产隔离、工具effects交Ch81。不是仅同题名或同主题。

新增必要Source揭示的是实验身份/硬保证资格，**不把新数字或未核driver吸收成Books结论**。当前Book受限机制及无生产隔离边界可承载，不需重复两段/再次owner。此处同family在Book不自动证明Report重复事件，不另读跨日报。

拟2+1+2=5；必要设计/系统资格深入已完成。提案 `已有覆盖`，Books0，具体位置上述AgentServe受限段；中心完整性能/硬隔离保证仍不采用。若root认为现“隔离GPU资源”措辞会签发forward-progress/带宽硬保证，仅请求该句澄清，不创建第二机制段/无根据新Booksgap。待非作者独核才能formal，非外部blocked。重开仅精确身份、控制流/slot实现及匹配SLO证据。
