# 12/31 机构原始材料与准入停点

检查2026-10-02T18:57:36+08:00，后续收尾2026-10-02T19:23:52+08:00；窗口[2025-12-30T09:00:00+08:00,2025-12-31T09:00:00+08:00)。作者记录，不是日Gate。启动时尚有后续扫描，当前普通题摘/准入补读已完成，详见SCAN，不把ready当非作者验收。

## Qwen-Image-2512：贡献前关闭，待root负侧校准

[官方Blog](https://qwen.ai/blog?id=qwen-image-2512)直接动态空；限定官方搜索实际返回2025/12/30与完整核心；[官方HF卡](https://huggingface.co/Qwen/Qwen-Image-2512)Introduction、Model Performance、Quick Start、Showcase、Citation全部核心实际读取。三项变化为人物真实感、自然细节与文字排版；一万余盲评轮与同prompt示例没有公开新增训练/采样算法、受控机制归因或旧方法的新适用边界。Quick Start仍DiffusionPipeline、50步、CFG4、seed42使用例，引用仍August的2508.02324。因此本材料仅产品能力更新，不借成熟生成原则凑贡献；不是因Books主题已有覆盖而排除，也不把缺实验细节普遍当初筛排除理由。无发现的安全/兼容性机制变化。Showcase幻灯片prompt内部“12月31日开源发布”不是原始公开时间证据。该贡献关闭不依赖精确日期，不另请求上线时刻，不评分、不进候选/Books。

## HY-MT1.5：potential，必要日期外部保留

[官方仓库](https://github.com/Tencent-Hunyuan/HY-MT)、[官方HF](https://huggingface.co/tencent/HY-MT1.5-1.8B)Related News仅2025.12.30，不给时区/时刻；current HYMT2公告、Transformers v5等后续兼容性文字不当Dec30事件。[精确v1题摘](https://arxiv.org/abs/2512.24092v1)与[HTML](https://arxiv.org/html/2512.24092v1)§2.1–2.4实际读：CPT/SFT明确复用旧Hunyuan-MT；GRPO/学生on-policy reverse-KL是成熟原则，不能单独凑准入。具体潜在差额是§2.4针对小模型分布的2-bit QAT offset、带bias对称量化与per-channel粒度，宣称缓解极低比特退化；其受控归因、表示/执行成本和权重尚未核验，不采纳产品排名或90/95%泛化结论。§2.2 rubric reward也须区分任务维度细分与真正新评价约束，不先称长期机制。

arXiv v1原始Submitted=2025-12-30T09:06:37Z，仅提交；官方Dec30 release日范围与本窗相交而不完全落窗。仓库PDF原始raw一次内部失败，arXiv精确HTML已经恢复正文，不再把正文当外部失败。日期仍需官方首次公开时刻/完全落窗的范围或历史new公告批次；当前不评分、不用于正面证据、不进Books、不授Coverage/Evidence/零事件。定点重开2512.24092或该版本公开release，不能按2025延期排期硬赋个体日期。

请root校准：Qwen的具体负侧理由；HY-MT仅2-bit offset/QAT差额是否达到潜在贡献门槛（非把整个翻译任务移入Books）。若日期恢复且准入成立，唯一owner优先INFER-TENSORRT-LLM/Ch49量化表示与校准，届时实际对读owner及相邻，不提前宣称已有覆盖或整合。
