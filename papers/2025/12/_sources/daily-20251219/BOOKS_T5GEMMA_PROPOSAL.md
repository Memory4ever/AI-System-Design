# T5Gemma 2：精确证据与 Ch18 局部提案

作者拟准入 2+2+2=6，标准必要审阅已达；新 architecture branch 对现有解释有明确增量，提请 root 准入/源审及 Books 协调。未修改 Books，未宣称整合完成。

## 事件与精确版本

[官方 Blog](https://blog.google/innovation-and-ai/technology/developers-tools/t5gemma-2/) `datePublished=2025-12-18T18:30:00+00:00` → 12/19 02:30+08，落本 release 窗；当前 `dateModified=2026-03-19T17:48:17.592801+00:00`，不是不可变旧文。精确方法材料 [2512.14856v1 HTML](https://arxiv.org/html/2512.14856v1) §2、§3.1–3.3、Table1–5 实际读取；release 时间不授论文 first-public。

## 必要支持与反证

- §2：encoder input、decoder input/output embedding 全共享，非只 tie decoder LM head。decoder Q=XWq，K/V=[X;H]Wk/v，共享 attention 投影且 logits 联合归一化；source 与 causal target 的可见性由 mask 管理。不能把两个独立 softmax 的输出相加当相同机制。
- Table1 是 **Gemma2 2B 初始化的 T5Gemma2B-2B**、400B tokens、PrefixLM+KD 的架构消融，不是最终 Gemma3 全配置消融。baseline 47.8；tie 47.7、embedding 1180M→590M；merge 47.5、nonembedding 4417M→4049M；只每六层 global cross-attention 46.5。这些是局部平均分，未披露此表 repeats/error bars，不能称严格非劣性或每任务无损。
- 最终 §3 是 Gemma3 初始化、约 2T tokens、UL2 五 denoising 比例 1:1:1:1:4，视觉用 prefixLM/frozen SigLIP；pretrain 无 KD。Table3 小型号 UL2 与 UL2+KD 接近，没有一般“蒸馏无用”结论；posttrain 有轻量 distillation、无 RL。
- Table4/5 跨模型并未完全隔离架构、数据、训练量与后训练：有些 text-only vs multimodal，DocVQA/InfoVQA marked approximate 不可跨文比。T5Gemma2 4B-4B pretraining reasoning平均60.8 比 Gemma3 4B 62.4 低，故非全任务支配。128K 多项提高不证明不受长度/上下文分布影响。
- 参数节约可核；**端到端推理加速/节能没有可支持受控数值**。hardware、precision、batch、concurrency、SLO、输入输出分布在拟采用参数命题不适用；若推成 throughput claim 则 Not Disclosed。本次无代码运行/生产验证。

## 实际 Books 覆盖/差异

Owner `MODEL-DECODER-ONLY`，`books/part-02-model/18-decoder-only.md`。
实际 41–50 行现有段落说明 encoder 双向 source、decoder causal self-attention + cross-attention，两套 stack/接口成本；50 行断言“至少两类模块和 cross-attention 接口”。该表述作为标准基线合理，但不承载共享投影/联合归一化可以合并两类 attention 的分支。31–39 encoder-only 及52–60 decoder-only 邻段亦实际读取。
Ch17 开头至95行层/残差/normalization 接口，Ch19 开头至85行 cache state 已对读：前者不拥有架构组织路线，后者不应接管 seq2seq 参数共享；只在 Ch18 添分支，其他仅链接交接。

## 局部替换草案

目标仅替换 Ch18 Encoder-decoder 小节最后一段（当前50行），保留标准结构图与相邻 decoder-only 推理。

> 这种结构显式区分输入与输出，适合 sequence-to-sequence 任务。标准实现分别运行 decoder self-attention 与 cross-attention，因此要承担两套 stack 和额外接口的参数与执行成本；但输入/输出的信息流边界不要求每种 attention 永远由独立参数实现。一个条件分支是共享 encoder/decoder embedding，并让 decoder query 同时读取 encoder states 与 causal target prefix：K/V 由两段状态经共享投影构成，联合归一化后由 mask 保留可见性约束。这与两个独立 softmax 再组合不同，减少模块也不等于保留原函数。
>
> T5Gemma 2 的局部架构消融展示了这种冗余/质量取舍，也给出反例：仅在少量 global 层保留 cross-attention 的更激进方案损失更大。该结果支持 encoder-decoder 仍有设计空间，不证明它普遍取代 decoder-only，也不从参数下降直接推出端到端加速；跨模型比较还要分离数据、训练预算与后训练配方。下一章再讨论固定 source 与 causal target 状态各自能缓存什么，不能用参数共享替代状态身份。

原始出处附在局部段末即可；不把整论文数表搬进主书。若 root 认为现有另段已承载此精确分支，请给实际段落后改已有覆盖；不得仅主题相同判覆盖。
