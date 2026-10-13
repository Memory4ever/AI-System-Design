# Sep14必要准入与直接反侧

作者Meitner。实际10个exact-v1必要局部：9HTML200；10423HTML404后PDF200/10页，结构抽取可读但PDF对象指针有警告，不声称图像或逐字完整。不是10全篇或Evidence完成。原六风险有效层不重复扩大。

| 身份 | 实际读层 | 实际新增/裁决与未读边界 |
| --- | --- | --- |
| 2509.10397v1 | §2、§3/3.1/3.2 | C：dual-view模拟用户/推荐者，think/action/mindset与retention reward、文本/MM/semanticID是既有sim/reflection/RL组合，§2明确没有experimental results，只有评估设计和单GPT4.1例。没有独立新执行/真实性条件；不是仅因无实验关闭。首个多篇输出§4/5中途截断，不称读完；未读全部related work。 |
| 2509.10401v1 | §3/4完整、§5 Tables1–4/正文与§6 | P：真实单pass提示并非实际do干预；但step numbering移除使step accuracy47.46→17.78而agent64.29/65.40近似，5run说明建立具体输入格式/时间归因评价盲区，不能仅组合C。gpt-oss120b同rerun/184日志/48batch/20k max；三步预测仅模型模拟，不授因果证明/生产可靠性，图2像素未读。 |
| 2509.10408v1 | §3.1.3/3.2.1、4.3.1–4.3.5 | P：零初始化γ是learnable vector而非每样本显式可靠门；RGB-easy/hard条件评价揭示LiDAR-only hard改善44.06 vsRGB37.93却easy反退55.49 vs57.07，asymmetric fusion同时保持easy/hard；symmetric更差。改变辅助模态注入/评价选择，不只是adapter名字。易难为训练RGB网络预测后人工看GT划分，不能当无偏分区或普适97%；未读全主榜/Appendix代码。 |
| 2509.10417v1 | §2.7、§3、4、5 | P：没有same-model full/truncate组织rubric控制，不采用“长context更忠实”或架构比较因果；但§3.1明确Mamba全模型finetune容易collapse，冻结SSM/gate/convolution、只embedding/Lin/Lout能工作，形成具体状态空间适配条件潜力。0.797 vs0.790等榜单不独立证明优越；全freeze理由是作者perhaps，未核重复训练/实现/全model综述。 |
| 2509.10426v1 | III-A/B/C、IV-C | P待独核确认桥：masked history/future/map→siamese latent regression对齐/空间+motion双任务→joint multi-world scene futures而非各agent独立轨迹；mask过低退为interpolation/过高损prior，未来只在pretrain输入、finetune无future，形成环境scene representation与joint预测条件。不能从名称授action-conditioned World Model/实际防碰撞，prediction无ego行动干预；若此只领域forecast不足，按独核具体桥裁决，不用日期逃避N。未读全benchmark或推测closed-loop安全。 |
| 2509.10436v1 | IV与V-G/V-H、VI | C：Guide/Solver相同fine-tuned deepseekcoder7b、GPT4oJudge，QLoRA与既有三步prompt；“ablation”只有问题类型/answer类别并无模块移除，latency只三角色均值/宣称两倍，没有新资源/部署边界或独立evaluation反例。格式不符即使code正确记错是自设protocol，不当新证明；MoE题名与base未展示路由，不能采用。未读全qualitative案例/Appendix，no code核。 |
| 2509.12267v1 | §2、3、4 | P：20M RWKV7/Aria-MIDIpruned/32epochselected在8prompt双盲20参与者/14全完成，与780M Anticipatory同组、胜1.2BMuseCoco，具体有限small/task-specific反侧，不由音乐标签或榜单自动C。各team8sample cherry-pickbest，data/train/architecture不控，不能归因小模型/“data alwaysbetter”或普适匹配FM；未核音频、权重/代码或复现。 |
| 2509.10416v1 | III-B/C/D、IV-B、V | 维持P：VLMinteraction triplet→GroundedSAM+calibratedRGBD worldpose→Bayes intent→orientation，保留human translation以免feedbackbias；gripper-close触发后translation/rotation完全autonomous，不能授始终human control。关节objects drawer stage拆分不适用；realworld成功只rightjoystick可以完成，没有安全证明/所有scene普适。未读全sim/图像/代码。 |
| 2509.10694v1 | §3、5.1、7.3、8 | 维持P：single/distributed IR equivalence/egraph+soundrule条件；17/19复现bug，2个graph外不检；layerpartition失去crosslayer机会，不complete，context/pipelineparallel需extra support。§3“verified排除软件bugs”被§8的runtime/data race/graph外限制收窄，当前只inferenceIR，soundness依赖重写rule本身sound；不授numeric/hardware/runtime全正确。§5.2.3未输出实际正文，不称已读；未核完整proof/代码/厂家bugfix。 |
| 2509.10423v1 | PDF p3 III-A–F、p4 IV-A/B、p5部分、p6/7 V-B/C、p8 V-F | 维持P：PPO PandaReach continuous10bin×7action离散计数，4seedqualitativelyconsistent只展示代表seed，cumulative5k training与2kslidingmonitor，frozenpolicy两位置Gaussiannoise差异MI；诊断条件是finite controllednoise，而非精确故障因果/自治修复。III连续bin和IV已离散grid描述不一致，stationarity/fullyobservable/singleagent及bin估计限制已读；V-C没有实际对CUSUM等新对照不采用uniqueness。p5/6首输出中段截断，不称整IV-D/图表读完；无真实robot hardware/复现。 |

作者7N收敛5P/2C，新25为19P/6C。Cicero已实际方法/关键对照独核同意该裁决，10426只保留latent regressor分离encoder与pretext decoder、masked history/future/map对齐及downstream joint-scene预测改变预训练表示选择的窄P；可由TRAIN-PRETRAINING/环境表示桥承载，不授action-conditioned闭环安全。正式候选0/date未知不评分，Books尚不采用。所有C的安全/正确性宣称实际在必要方法里收窄，没有把N未读写成外部受阻。表中“P待独核”是作者读时状态，最终裁决以本段及Cicero实际独核为准。
