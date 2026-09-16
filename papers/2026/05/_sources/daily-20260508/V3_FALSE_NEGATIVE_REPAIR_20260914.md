# 2026-05-08 V3 false-negative 修复（作者侧）

## 角色与范围

本记录只修复 2026-09-14 独立终审指出的 9 个 closure false negative。它是作者侧 Evidence Review 与 Books Decision，不替代新的独立复核，也不表示共享 Books 已写回。

9 个 Source Family 均属于 `2026-05-08T08:00:00+08:00` official arXiv announcement batch，落在本日报窗口内。逐项检查 exact-v1 页面，均显示 `v1` 首次公开于 2026-05-07，未见 withdrawn 标记。8 项使用 arXiv HTML，论文 `2605.06014v1` 同样使用 HTML；没有材料缺口。

## 逐项 Evidence Review

### SF-2026-ARXIV-2605-05594 — The Cost of Context

- **Mechanism：** 论文先构造“原本回答正确、加入 oracle text 后反而错误”的 recorruption 样本，再把失效定位为视觉 token 的 attention mass 与 sharpness 同时下降，以及文本位置偏置。BAIR 在 prefill 使用辅助 reference pass 恢复视觉注意力，并惩罚位置文本偏置。
- **Evaluation contract：** IU-Chest、FACET、NWPU；MedGemma-4B、CheXagent-8B、Qwen2.5-VL-7B、DeepSeek-VL-7B、SkySenseGPT-7B、EarthDial；论文披露 RTX A5000 与 AMD EPYC。结果只证明这些模型、数据与配置中的 recorruption/缓解。
- **Artifact：** `https://github.com/HoinJung/BAIR`。
- **Non-proof / trade-off：** 需要额外 reference pass；`alpha` 依任务调节；不保证答案正确，也不能修复错误 retrieval、歧义图像或强模型先验。
- **Score V2：** `3 + 2 + 2 = 7`，Deep。
- **Owner 对读：** `AGENT-RAG` 已区分 retrieval support、claim entailment 与 answer uncertainty，但没有明确说明“oracle 文本也会压制视觉证据”这一跨模态融合 failure。相邻 `MULTIMODAL-REPRESENTATION` 拥有 modality identity 与 fusion 机制，不应重复拥有 RAG evidence admission。
- **Books Decision：** `Integrate — Queued → AGENT-RAG`，并向 `MULTIMODAL-REPRESENTATION` 建立短 handoff。

### SF-2026-ARXIV-2605-05657 — RGAO

- **Mechanism：** 从层次代码索引抽取结构复杂度向量，再选择 multi-agent topology；以六维资源预算描述 Agent 消耗，并在执行前对 DAG 做守恒检查。只读节点可并行、写节点串行，contract、budget 与 artifact handoff 分别设 gate。
- **Evaluation contract：** 报告 sub-millisecond DAG 构造、线性 tree-index 扩展和 10 个 synthetic SWE-bench issue；这主要验证编排开销与可执行性，不足以证明真实软件任务质量。
- **Non-proof / trade-off：** theorem 依赖 deterministic tool cost、bounded retrieval depth、finite action space。成本随机时只能得到期望/高概率松弛，必须回退到 runtime accounting；外部有效性弱。
- **Score V2：** `3 + 2 + 3 = 8`，Deep。
- **Owner 对读：** `AGENT-MULTI-AGENT` 已覆盖 task-topology matching 与预算化 fan-out，但没有把执行前的 resource algebra 与守恒证书写成独立控制面责任。
- **Books Decision：** `Integrate — Queued → AGENT-MULTI-AGENT`。

### SF-2026-ARXIV-2605-05700 — ProCodeBench

- **Mechanism / data：** 从 1,246 名开发者三天内约 4M 条真实 IDE trace 构建 proactive coding benchmark；intent pipeline 组合 LLM sliding-window inference、启发式/语义过滤和双专家人工复核，形成 5,492 样本，并按时间切分 3,576/1,142/774。
- **Evaluation contract：** 比较 13 个 LLM、RAG 与 Agent baseline。真实 trace 与 simulated trace 在多样性、时间结构和探索行为上不同，simulation-only 评估会高估可用性。
- **Non-proof / trade-off：** developer intent 不可直接观察；LLM/proxy label 可能漏掉有效 intent；采集只覆盖三天和受控人群。exact-v1 未发现公开 artifact。
- **Score V2：** `2 + 2 + 3 = 7`，Deep。
- **Owner 对读：** `PLATFORM-EVALUATION-SYSTEM` 已明确 synthetic evidence 只有在 task exchangeability 成立时才可外推，simulator/replay 不拥有 deployment truth，真实 shadow/canary evidence 必须分层。该论文强化已有命题但不改变设计结论。
- **Books Decision：** `No Change — Existing Coverage → PLATFORM-EVALUATION-SYSTEM`。

### SF-2026-ARXIV-2605-05818 — LeakDojo

- **Mechanism：** 将 RAG、攻击与防御模块拆开配置，并保留跨轮 extraction state；实验把 query generation 与 adversarial instruction 识别为可独立组合的泄露因素。
- **Evaluation contract：** 6 种攻击、14 个 LLM、4 个数据集；论文还显示更强 instruction following 可能伴随更强泄露，部分 faithfulness 组件可能恶化安全。
- **Artifact：** exact-v1 链接第一方 GitHub 实现。
- **Non-proof / trade-off：** 固定 `N=200`、英文任务；成本只由固定预算近似，rewriter/reranker/summarizer 覆盖有限。结果不能外推到所有 RAG pipeline。
- **Score V2：** `3 + 2 + 3 = 8`，Deep。
- **Owner 对读：** `PLATFORM-SECURITY` 已有 prompt injection、membership leakage 和累计隐私，但缺少 modular stateful extraction evaluation，以及 faithfulness 与 confidentiality 可能冲突的 release contract。
- **Books Decision：** `Integrate — Queued → PLATFORM-SECURITY`。

### SF-2026-ARXIV-2605-05838 — MDN

- **Mechanism：** 为 delta linear attention 引入二阶 momentum recurrence；通过代数重排得到保持 causality 的 chunkwise parallel training，同时维持 recurrent decode。反向传播重建 correction value 而不是完整 state，并用特征值/象限条件约束稳定性。
- **Evaluation contract：** 400M 与 1.3B 模型，在 language modeling、long-context、retrieval 与 needle 任务上比较 Transformer、Mamba2、KDA/GDN 等；论文报告 throughput 接近 Mamba2/KDA，并给出多项质量改进。
- **Artifact：** `https://github.com/HuuYuLong/MomentumDeltaNet`（Triton）。
- **Non-proof / trade-off：** 未验证 7B 以上；训练吞吐仍低于高度优化 GDN/Comba；增加 momentum state 与 correction values；TP 兼容性未验证，hybrid ratio 范围窄。
- **Score V2：** `3 + 2 + 3 = 8`，Deep。
- **Owner 对读：** `MODEL-LONG-CONTEXT` 已拥有一阶 gated/delta recurrent state。MDN 增加的是不同的二阶 update/state 与 train-parallel/decode-recurrent 一致性，不应归到 serving cache owner。
- **Books Decision：** `Integrate — Queued → MODEL-LONG-CONTEXT`。

### SF-2026-ARXIV-2605-06014 — Randomized Hadamard Transform quantization

- **Mechanism / theorem：** 两次 RHT 对任意输入提供固定坐标的高斯近似，足以支撑 scalar quantization 与 DRIVE/QUIC-FL 的渐近 guarantees；对 sparse input 的 block VQ，两次 RHT 仍可能保留条件相关，三次 RHT 才为固定有界 block 给出衰减 covariance。论文用 `l3` 与 `linfinity` moment 的 `O(d)` 检查在运行时选择一、二或三次变换。
- **Evaluation contract：** 这是 theorem 与 algorithmic evidence；没有经验实验或公开实现，因此不能声称实际 kernel acceleration。
- **Non-proof / trade-off：** 定义依赖 Hadamard-compatible dimension；结论针对 fixed bounded block/codebook 与渐近 additive terms。adaptive/non-fixed block 可能需要更强保证，额外 transform 也有实际执行成本。
- **Score V2：** `3 + 3 + 3 = 9`，Deep。
- **Owner 对读：** `INFER-TENSORRT-LLM` 已覆盖 rotation scope 与 quantization group，但没有把 transform 次数与 scalar/vector quantizer 的分布假设、moment check、正确性边界绑定。
- **Books Decision：** `Integrate — Queued → INFER-TENSORRT-LLM`。

### SF-2026-ARXIV-2605-06311 — VISER

- **Mechanism：** 以 shadows、specular highlights 与 clean PBR material 构造视觉真实性 contract，并使用 MLLM 做 material segmentation/retrieval，形成超过 1,000 个资产的仿真环境。
- **Evaluation contract：** 14 个 curated、8 个 reconstructed 及生成任务；Google Robot 与 WidowX 两种 embodiment；Octo/OpenVLA 的 sim-real matching 平均 Pearson 相关系数报告为 0.92；OOD 部分每任务 5 次并加入 X-VLA。
- **Non-proof / trade-off：** 任务多样性不足、只覆盖两个 embodiment，policy 与真实机器人范围有限；相关性不等于可替代实机安全验证。exact-v1 未发现第一方 artifact。
- **Score V2：** `2 + 2 + 2 = 6`，Standard。
- **Owner 对读：** `MULTIMODAL-EMBODIED-VLA` 已把 camera、lighting、texture 列入 sim-to-real gap，要求 real calibration 与 real-world denominator，并明确仿真成功不产生 physical authority。VISER 量化已有 contract，但不改变 owner 或结论。
- **Books Decision：** `No Change — Existing Coverage → MULTIMODAL-EMBODIED-VLA`。

### SF-2026-ARXIV-2605-06326 — Tool-Integrated Reasoning recipe

- **Mechanism：** tool-enabled evaluation 即使很少真实调用工具也可能损害 reasoning；tool-use SFT 需要可学习的 teacher trajectory 与适合工具的任务，并与 text-only trajectory 混合以避免遗忘。checkpoint 需同时看 `pass@k` 与 response length，随后才进入带 mode-collapse safeguard 的 RLVR。
- **Evaluation contract：** Qwen3 4B/30B thinking models、competition math 与 4,325 个 RLVR examples；论文观察到 SFT 的 `form → substance → noise` 动态，且 4B/30B 的最佳路径不同。
- **Non-proof / trade-off：** 主要是数学工具任务，只覆盖 4B/30B；更广 Agent workflow、透明 trace 与人类/领域验证仍未建立。exact-v1 未发现公开项目仓库。
- **Score V2：** `3 + 2 + 3 = 8`，Deep。
- **Owner 对读：** `TRAIN-SFT` 已覆盖 tool-use demonstration 与 forgetting，但没有把 tool-suited task admission、trajectory learnability、mixture ratio、SFT checkpoint 和 RL handoff 连成一个条件化 recipe。`TRAIN-GRPO` 与 `AGENT-TOOL-CALLING` 只接收短 handoff。
- **Books Decision：** `Integrate — Queued → TRAIN-SFT`。

### SF-2026-ARXIV-2605-06631 — Task-aware audio compression

- **Mechanism：** 将 compression release 判断从信号重建或平均 accuracy 改为压缩引入的 excess answer error，尤其是 worst query family；同时要求对 query-conditioned frontier 给出统计置信区间。
- **Evaluation contract：** 在固定 LALM 下配对比较 raw/compressed audio；5 个英文 prompted multiple-choice audio-QA 数据集，Qwen2-Audio-7B 与 Qwen2.5-Omni-7B。selector、backbone 与 semantic family partition 会显著改变结果。
- **Non-proof / trade-off：** 聚合平均会掩盖 family-specific harm；v1 keyword partition 不能充分表达原生任务结构；Appendix J 明确没有直接测量真实音频的 rate-theoretic frontier，也没有证明统一收益。
- **Score V2：** `3 + 2 + 3 = 8`，Deep。
- **Owner 对读：** `PLATFORM-EVALUATION-SYSTEM` 已有“Compression Release = Accuracy + Calibrated Uncertainty”，但缺少 worst-family excess answer risk 与 family partition refinement；应扩展既有 release contract，而非新建音频方法段。
- **Books Decision：** `Integrate — Queued → PLATFORM-EVALUATION-SYSTEM`。

## 修复后账本

- `619 raw = 97 retained + 522 pre-denominator closures`。
- 97/97 已完成 Evidence Review；`Review Pending = 0`；没有 withdrawn 或 exact-v1 material gap。
- Score V2：46 项 `7～9`，51 项 `5～6`。
- 深度：57 Deep，40 Standard。
- Books：37 `Integrate — Applied`、7 `Integrate — Queued`、53 `No Change — Existing Coverage`。

## Gate

- **Coverage：** Closed with declared source limitations。
- **Evidence：** 作者侧修复完成；尚需未参与本次修复的新 reviewer 复验。
- **Books：** 7 项等待 root 按唯一 owner 串行写回并执行 post-write semantic audit；2 项 No Change 已指向具体既有命题。
- **Completion：** Ongoing。作者侧修复不能自签独立 Gate。
