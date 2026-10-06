# 11/13 新方向有界准入校准

仅新增具体方向与一项代表性排除，不重复首批七项和 Project Fetch。首五项精确v1完整题摘已读：[原题摘/身份/历史字段](./raw-exact-ab-2511-07776v1.json)；有界标题补检选取的七项精确题摘同样实际读完：[原题摘](./raw-exact-ab-2511-07689v1.json)。逐篇HTML同目录可核。来源是system/multimodal窄主题查询及月表定点查漏，不是月表全量队列。当前首公开链未完全闭合，以下仅校准贡献，不授落窗，不进正式§3；只有满足日期条件才能采用。本轮不因日期缺口先展开这些全文。

| 精确材料 | 原有判断 → 实际增量 → 重考选择 | 拟评分与边界 |
| --- | --- | --- |
| [STeP 2511.07776v1](https://arxiv.org/abs/2511.07776v1) | dataflow抽象将动态shape/control静态化或隐藏调度信息 → routing/explicit memory/symbolic shape暴露动态率并支持tiling/parallel/time-multiplex → 动态LLM traces应否交给不同执行抽象 | 2+1+2=5；标准。2.18/1.5/2.57倍仅cycle-approximate simulator，不是真硬件/端到端服务 |
| [Autospeculation 2511.07869v1](https://arxiv.org/abs/2511.07869v1) | 顺序conditional oracle sampling与draft token speculation → 同一oracle构造sequence-level speculative rejection，理论并行复杂度由n^(2/3)到sqrt(n) → 无独立draft时可否采用另一并行采样分支 | 2+2+2=6；标准。any-order条件边际或diffusion条件均值oracle、bounded support等前提待核；不是decoder-only实测加速 |
| [HipKittens 2511.08083v1](https://arxiv.org/abs/2511.08083v1) | tile primitive可移植常被混为schedule可移植 → CDNA3/4明确tile接口通用与AMD实现算法差异、assembly/compiler对照 → 跨vendor kernel应复用哪层 | 2+2+2=6；标准。作者博客显示Nov11日期而timezone未知，不能由Nov12论文批次掩盖更早公开；先定点恢复该家族首公开 |
| [Dynamic Sparsity 2511.08086v1](https://arxiv.org/abs/2511.08086v1) | 全局/时间稀疏因果先验被作为dynamics learning设计依据 → MuJoCo ground-truth dynamics显示局部state-dependent/contact clusters与全局不稀疏 → 改用何种局部先验 | 2+1+2=5；标准。负证据直接指模型先验，不是只换机器人领域。v2在Nov14提交，不用其正文替代v1 |
| [Cross-modal composition 2511.08113v1](https://arxiv.org/abs/2511.08113v1) | 各模态单项能力常代替组合能力 → 同一模型direct与两步cascade在三任务出现gap，CoT/finetune未消除 → end-to-end composition须独立评价 | 2+2+2=6；标准。cascade的信息/预算公平性待核；v2 submitted Nov12 08:52Z不等本窗public，不静默采用v2 |

## 有界补检七项新增方向

以下题摘为精确v1，不采用当前晚版本；题摘未见撤回标记，history版本增长本身不认证重要修订。潜在增量已明，不因摘要欠缺实验配置关闭；日期未闭合仍不授候选。

| 材料 | 具体增量 / 重考选择 | 拟评分 / 必要反侧 |
| --- | --- | --- |
| [2511.07689v1 Stress Testing Factual Consistency Metrics](https://arxiv.org/abs/2511.07689v1) | meaning-preserving perturbations及claim density使short-form judge对长摘要不稳定；长文factuality指标迁移须独立验证，不只沿用名称 | 2+2+2=6；标准。七类变换是否真正保义、retrieval预算及原文分母待核 |
| [2511.07691v1 CAPO](https://arxiv.org/abs/2511.07691v1) | relative-reward confidence动态缩放preference loss，针对噪声/低margin多语pair；训练应否统一pair权重 | 2+1+2=5；标准。confidence校准、reward accuracy不是人类生成偏好收益，训练预算待核 |
| [2511.07732v1 ViPRA](https://arxiv.org/abs/2511.07732v1) | actionless video中联合future observation/motion latent，perceptual/flow约束后由chunked flow decoder绑定robot actions；跨本体预训练与动作解码分工 | 2+2+2=6；标准。100–200示教与22Hz不等零shot/闭环可靠，latent实际消费与对照待核 |
| [2511.07772v1 SALT](https://arxiv.org/abs/2511.07772v1) | final output安全仍可由CoT泄漏，targeted activation steering新增test-time干预；泄漏人口须覆盖reasoning trace | 2+2+2=6；隐私命题必要深入。CPL定义、utility、层选择与未见数据/泄漏反侧待核，不由18–31%改善授安全 |
| [2511.08525v1 CoT Monitorability](https://arxiv.org/abs/2511.08525v1) | 区分true factor verbalization与monitor sensitivity，检查CoT干预对检测的影响；监测成功不能反推faithfulness | 2+2+2=6；安全/设计反证必要深入。真因oracle、sensitivity/false positives、structured evidence不等真实因果待核 |
| [2511.08389v1 Model and Layer Fusion for Speech Foundation Models](https://arxiv.org/abs/2511.08389v1) | 统一cross-model/cross-layer接口且效果依赖upstream selection；多模型融合收益是否可独立归因接口 | 2+1+2=5；标准。参数/预算与选模分离、fusion消融待核，不只因语音应用准入 |
| [2511.07931v1 SpeechJudge](https://arxiv.org/abs/2511.07931v1) | naturalness人类偏好与既有指标/AudioLLM judge明显失配，GRM两阶段训练和@10比较；需要验judge人口而非普通语音accuracy | 2+2+2=6；标准。99K pair的annotator一致性/划分、BT公平预算及@10成本待核 |

## 代表性排除待校准

[3D4D 2511.08536v1](https://arxiv.org/abs/2511.08536v1)：完整题摘及决定性 System Framework/Evaluation 已读，[原必要核心](./raw-web-18.json)。实际四模块是生成图像/视频后产生PLY序列、WebGL/Supersplat交互编辑；VLM importance map驱动foveated rendering。当前拟关闭的具体理由是增量在可视化/graphics front-end，没有新增foundation生成目标、action-conditioned transition或模型运行时机制；60fps与CLIP alignment不能补这个关系。不是因DemoTrack、小幅收益、无完整实验摘要或“World Model不够像”排除。若root判断semantic rendering资源策略本身改变模型系统核心接口，定点重开该模块，不重扫其引用/作者历年研究。

## 查询/停止与日期保留

四主题API的submitted范围只作发现；精确提交字段不能授public。官方月表当前边界 `[2511.07555,2511.08579]` 有81标题，其中33未见于四个主题结果，仅读这个切片的去重标题；选7个明确失效/机制方向定点读v1摘要，不把33或92变全量题摘。该ID边界不是公开日期切片，不能宣称“当日81篇”。

首公开有限恢复：已有 exact-v1、部分 DataCite/OAI，历史一般schedule不足；raw-web-29三条历史检索为空，raw-web-30尝试的日list/updates路径失败且接口语义未获证实，不能当官方日列表或空命中。停止这些空路径，精确重开需要2025真实公告+该版本官方当日list身份及可对齐的公开上界，或作者精确发布原字段。DataCite registered只保留注册事件，不独自授正文首公开。

只请求本表具体新增方向及3D4D关闭理由的独立校准。已通过的首批未变化内容复用；此文件不授Evidence/Books/日级完成。
