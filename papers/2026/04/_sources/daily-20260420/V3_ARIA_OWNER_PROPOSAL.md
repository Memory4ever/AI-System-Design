# Qwen3.5-Omni ARIA 有界 source→owner 提案

作者：apr20_resume。仅针对 `2604.15804v1` 的 ARIA text/speech token 交错约束；下文是写前原提案，不能单独作为已采用收据。后续实际状态：root [写前有限核](./V3_ROOT_ARIA_INDEPENDENT.md)通过，Ch24 已按两段最窄写入并附 Review note，root [实际写后核](../V3_ROOT_FIVE_WRITE_AFTER_20260928.md)通过；本日日期、来源与全集 Gate 仍未通过。必要原文与反证在同日 `v3-reopen-notes.md` §15804。

原始正文：[exact-v1](https://arxiv.org/html/2604.15804v1) §2.4/2.5、Tables1–2。当前 `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24:330–334 已有 speech/reasoning token 交错，Ch24:393–409 已有 Thinker→performer 两级流式交接，但二者都没有说明同一输出序列中的 **text/speech token 数率**如何限制可提交 prefix。拟在 Ch24:334 后、`Self-revision` 前接两段，不改旧机制：

> 交错生成还须问清两种可见输出能否按同一节奏前进。文本 token 与语音 codec token 的编码率不同；固定交错步长或等待强制对齐，会让某一通道被另一通道拖住。一个条件分支把 text 与 speech 放进同一生成序列，并对已生成 prefix 限制累计 speech/text token 比不超过该样本的全局比例，使文本可以先给出可解释前缀，后续语音再跟进。它处理的是输出单位的单调次序，不把逐词文字与声学帧变成精确一一对应；具体比例若依赖完整样本统计，在线未知终点时仍须声明估计或回退，不能凭训练约束直接宣称生产硬保证。

> 单流布局可减少两条生成轨之间的同步状态，却把 codec、type delimiter、prefix 缓冲、取消与回退放进同一提交合同。受限 [Qwen3.5-Omni exact-v1](https://arxiv.org/html/2604.15804v1) 的 ARIA 采用这样的 prefix-rate 约束，Talker 仍以 RVQ/MTP 与因果 codec 生成波形；Table2仅给内部 vLLM/compile/CUDA Graph 设置下的 theoretical first-packet latency，且8并发时视频首包明显变长。它未单独消融 ARIA，也没有证明在线全局比率已可知、任意语言都低延迟或真实 tail SLO；比率失配、对齐质量不稳或跨模态回退复杂时，固定chunk/双track的旧分支仍合理。Thinker与Talker的状态交接依然是后文独立的部署问题。

拟 Review note 保存输入video约160ms temporal-ID、AuT6.25Hz/40M小时为不同表示/训练分支，不把全部质量或 latency 归ARIA；Table2 Flash音频/视频1并发235/426ms、8并发352/1625ms，Plus为435/651→955/1980ms，均 theoretical。硬件/precision/完整队列SLO、ARIA单独消融与在线全局比率取得方式未披露；不采用跨模型/语言全胜或产线保证。

请求非作者仅核 §2.4/2.5、Table2 与 Ch24上述两处相邻论点是否真实增量，以及 literal 对“全局比率在线未知”的保守限定。若不通过，回归标准Only并保留受限机制；不为名字或厂商身份强写Books。
