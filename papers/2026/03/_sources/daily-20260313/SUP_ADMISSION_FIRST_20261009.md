# 2026-03-13 补充窗口首批准入校准包

报告原窗口/候选/§4冻结；本包窗口为 2026-03-12 BJT 完整自然日。未获非作者校准前不计确认候选、不评分、不扩全文池。

## 来源与日期原件

实际查询及响应：`SUP_DISCOVERY_FIXED_MANIFEST.json`、`SUP_DISCOVERY_FIXED_MANIFEST_RESULT.json` 与四份 `SUP_FIXED_*.raw`。四个主题返回69/2/35/51，start0/max150，总量均小于150；已实际浏览全部返回标题，只把明确相关/含糊题名送完整题摘。初次使用方括号日期的四份 `SUP_TOPIC_*.raw` 范围不正确（各返回150、total13628/915/8211/11951），保留诊断，不支撑覆盖或候选。

本批10项精确v1官方题摘原件为 `SUP_ABS_<尾号>.raw`；8份日期原件为 `SUP_DATE_<尾号>.raw`，实际入口与检查时刻见 `SUP_FIRST_MANIFEST_RESULT.json`。DataCite registered仅提供公开上界，不冒充精确发布时间；Submitted不直接作公开日期。官方availability的截止/公告机制已实际取得 `SUP_ARXIV_AVAILABILITY.raw`。本批Submitted均在Mar10 18Z之后至Mar11 17:59Z之前，按官方最早正常批次对应Mar12 BJT；registered全部在Mar12 BJT当天，形成当日夹证。先稿/早公开信号须另核，不凭窗口夹证抹除。

| 精确材料 | 完整题摘后的窄贡献理由 | 日期/身份注意 | 拟处置 |
| --- | --- | --- | --- |
| 2603.10123v1 Lost in the Middle at Birth | 通常把U形归因于学得softmax或RoPE→作者提出causal Cesàro矩阵+residual在初始化已形成primacy tail/recency delta→需核“位置编码不是唯一原因”的受限架构解释 | registered03/12T01:54:04Z；没有把理论摘要当结论 | 拟潜力，MODEL-LONG-CONTEXT/MODEL-SELF-ATTENTION唯一owner待必要证据 |
| 2603.10899v1 LookaheadKV | draft surrogate未来响应提高eviction质量但引入prefill成本→训练轻量层模块预测未来KV重要性、不显式生成draft→需核quality/TTFT取舍及训练分布依赖 | registered03/12T02:12:34Z；Comments ICLR2026，必须定点核会议先稿是否早公开 | 拟潜力，INFER-KV-CACHE |
| 2603.10126v1 AR-VLA | chunk head随新观测重置动作历史/快控制慢感知错频→持续AR动作历史+refreshable视觉语言prefix、re-anchoring补staleness→需核历史连续性与感知陈旧成立条件 | registered03/12T01:54:09Z；只读v1而非当前v2 | 拟潜力，MULTIMODAL-EMBODIED-VLA |
| 2603.10165v1 OpenClaw-RL | next-state通常仅作环境状态/标量reward→从同一next-state抽scalar PRM与directive hindsight OPD，异步serving/judge/train→需核token directional监督和policy滞后边界 | registered03/12T01:55:02Z，但DataCite Updated-v1为03/17，不能偷换Updated作公开上界；精确v1当前可得 | 拟潜力，TRAIN-RLHF/AGENT-REFLECTION唯一owner待必要证据 |
| 2603.10391v1 Variance-Aware Adaptive Weighting | noise level loss方差失衡→按log-SNR观察方差动态调权，CIFAR小模型多seed负侧→可能修正“固定权重即可”的优化边界；小模型不构成排除理由 | registered03/12T02:00:20Z；不外推大规模通用收益 | 拟潜力，MULTIMODAL-GENERATIVE-PARADIGMS |
| 2603.10785v1 Quadratic Geometry of Flow Matching | FM残差跨样本干扰通常隐式处理→NTK动态interaction matrix及语义granularity residual干预→需核理论假设、收敛/quality与预算归因 | registered03/12T02:09:46Z | 拟潜力，MULTIMODAL-GENERATIVE-PARADIGMS |
| 2603.10577v1 CUAAudit | final-state VLM auditor常被当可信success evaluator→三OS benchmark上校准/复杂环境退化/模型间分歧→需核自动终态判定的可靠性边界 | registered03/12T02:04:54Z；v2后窗，不以版本号触发或迁入 | 拟潜力，PLATFORM-EVALUATION-SYSTEM |
| 2603.10749v1 AttriGuard | input语义过滤难泛化IPI→teacher-forced shadow replay+层级control attenuation+fuzzy action survival作toolcall因果归因→需核反事实语义保留与自适应攻击/开销边界 | registered03/12T02:08:56Z；v2后窗，只核v1 | 拟潜力，AGENT-TOOL-CALLING/PLATFORM-SECURITY唯一owner待必要证据 |

代表排除均完整读v1题摘及可见Comments/Subjects：

- 2603.11025v1 LLMGreenRec：可持续电商推荐应用，通过agent分析用户意图/迭代prompt提高领域推荐结果，题摘未提出足以改变大模型/Agent系统解释的新执行机制或有效性条件；不因“减少energy”宣传收为系统成本机制。关闭，不为无关日期开恢复请求。
- 2603.10245v1 Over-the-Air Formation Control：无线模拟叠加形成控制的communication-rate/geometry收敛证明有自身价值，但并非模型训练/推理/GPU collective或LLM Agent，不能经通信横轴类比重新引入。范围关闭，不否认理论贡献。

首8没有看到撤回/安全更正提示；“没有看到”仅指实际当前事件页Header/Comments，不证明全版本史。必要正文尚未读，不授Evidence或Books。

## 停点

待root实际读取10份题摘及8日期原件进行准入校准；其余有限标题中的相关项仍普通初筛待办，未伪造外部blocked。已发起14每日源的19个官方GET入口；所得目录仍需实际范围与停止整理。此包不是DAY验收。
