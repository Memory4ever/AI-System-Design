# 12/23 首批准入校准请求

窗口[Dec22 09,Dec23 09)+08；四主题Submitted[Dec21,Dec23)缓冲192/12/33/47行，227去重identity，各页无Next。不是公告池。以下实际精确v1完整题摘已读，均未确定个体firstpublic，不先评分/入选。需要非作者校准具体增量而非落窗；作者继续普通扫描。

| identity / 原始链接 | 明确潜力或代表性负侧 |
| --- | --- |
| [Remoe 2512.18674v1](https://arxiv.org/abs/2512.18674v1) | potential：MoE专家输入相关且内存驻留昂贵→nonexpert GPU/expert CPU并把低频专家拆serverless函数，语义相似预测路由+最坏内存SLO预分配+memory/replica联合优化→需要比较激活预测失误/冷启/端到端成本边界，不按57%宣传确认机制。 |
| [SmartSight 2512.18671v1](https://arxiv.org/abs/2512.18671v1) | potential：greedy隐藏低幻觉候选→Temporal Attention Collapse评分多候选、Visual Attention Vanishing早停→注意力信号作为成本/误差筛选，而非事实正确证明。 |
| [ChronoDreamer 2512.18619v1](https://arxiv.org/abs/2512.18619v1) | potential：接触/动作未来预测不只RGB→depth-weighted Gaussian force splat作为camera-aligned接触表示，MaskGIT多头预测接触/关节/视频+VLM碰撞拒绝→可核接触表示与模拟器闭环，但摘要只有qualitative，不能授安全。 |
| [Reflective Confidence 2512.18605v1](https://arxiv.org/abs/2512.18605v1) | potential：低置信轨迹早停丢失已算路径→反思触发后继续修正、与earlystop预算比较→需要区分修正vs追加token预算。 |
| [PII 2512.18608v1](https://arxiv.org/abs/2512.18608v1) | potential窄反侧：标签标准化跨两架构改善、实时口语输入退化与结构输出/延迟取舍，可修正只看AI4Privacy离线实体F1的交付判断；不是仅PII应用高分。 |
| [IntelliCode 2512.18669v1](https://arxiv.org/abs/2512.18669v1) | close初判：共享versioned learnerstate/singlewriter/puretransform是成熟状态纪律，示例和simulatedlearner任务成功未独立新增执行机制/可靠性边界；决定准入是否藏有具体新机制可窄核，不因教育领域自动关闭。 |
| [Does It Tie Out 2512.18658v1](https://arxiv.org/abs/2512.18658v1) | 未决需必要正文：摘要称stricttraceability/deterministicoutputs失败与worldmodel提案，但未披露具体失效证据/独立机制；不能由legalworldmodel命名直接入选或关闭。 |

初始明确领域外题名：2512.18653thermoelectricmaterials为AIforScience暂缓；2512.18661cryptocurrencyforecasting为领域预测，不将价格指标等同模型系统贡献。其余含糊题名仍读完整摘要，未据日期失败删除。

## 新增官方事件校准（21:08实际轮次后）

- [OpenAI Atlas](https://openai.com/index/hardening-atlas-against-prompt-injection/)：potential具体增量为RL攻击者在思考中反复调用counterfactualvictim simulator、取得完整reasoning/actiontrace后修订并最终commitattack，随后adversarialcheckpoint与系统防护分层。原文只有具体demo/过程披露，无对照成功率/训练预算，不授确定安全或全防御因果。正文核心/限制实际已读，原站直接HTTP403、web可读但只Dec22日精度；精确public不可得另隔离。
- [MiniMax M2.1同事件card](https://huggingface.co/MiniMaxAI/MiniMax-M2.1/blob/main/README.md)及[VIBE](https://huggingface.co/datasets/MiniMaxAI/VIBE/blob/main/README.md)：原Blog只有图片/能力清单不足，但实际card披露runtimeAgent-as-a-Verifier三层build/interaction/visual、OctoCoding单违例失败；Terminalbench移除timeout与systempromptoverride、4runs等可比限制。VIBE实际仅200promptspec releasedDec23，rubric/sandbox/verifierpipeline仍comingsoon，与“开源benchmark”授权不同。保留具体评价机制/披露边界potential，当前card不等2025精确原稿、日精度不授09前，不先入选/Books。必要当前卡可读任务完成，不以图片恢复web失败/浏览器超时关闭潜力。
