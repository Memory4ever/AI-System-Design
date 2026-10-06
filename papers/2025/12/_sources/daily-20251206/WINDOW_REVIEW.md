# 12/06 独立窗口与筛选记录

执行：2026-10-02北京时间18:35起，18:43恢复上下文至18:50。独立重读AGENTS、研究/Report合同、每日来源使用说明与arXiv主题边界、Prompt、ROADMAP；本日无既有README或checkpoint。窗口为 `[2025-12-05T09:00:00+08:00,2025-12-06T09:00:00+08:00)`，即Dec5 01Z至Dec6 01Z。

## 十四源原始范围

本轮逐段重读[实际恢复的固定历史原始目录](../daily-20251201/RECOVERY_NOTES.md)，只按本日相邻段重新判断，不借任何别日报的候选/完成标签。有限失败入口不反复探；这些原始段是有界检查，不是全机构零事件证明。

- [OpenAI RSS](https://openai.com/news/rss.xml)：本轮原生XML成功1243 items，按Dec4至Dec9邻接筛字段。实际Dec4 19GMT Australia，下一研究报告Dec8 04GMT enterprise AI，中间Dec5至7未见该feed条目。Dec8 00GMT Virgin Atlantic是客户故事，非机制增量。较早一次请求未取得可观察输出，未计成功，随后一次有限恢复得到本结果。
- [Anthropic Research](https://www.anthropic.com/research)：原生publicationList已实际读的邻接Dec4 17Z Interviewer、Dec18下一项；前者早于本日左端，不复收。仅该Research切片，不声称全站无事件。
- [Google Research Blog](https://research.google/blog/) / [DeepMind第3页](https://deepmind.google/research/publications/?page=3)：原始2025 Blog Dec4 Titans/MIRAS→Dec10 DP框架，DeepMind Dec3 Reward Features→下一Jan9邻接重新比对本窗。无相交目录项；Google pubs年字段没有归日权限。
- [Meta第4页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4)：原始Dec12/Dec1/Nov19段，无本窗收录项，不扩到别类研究。
- [Qwen](https://qwenlm.github.io/)：旧站Sep23终点，新站空正文及部署/README有限替代均不能恢复2025历史。原始缺口本日隔离，不能据此声称无事件。
- [DeepSeek API Docs](https://api-docs.deepseek.com/news/news251201/)：正确原始Dec1 V3.2 release在本日之前，历史发布对象创建时刻不等于公众可见。未发现本窗具名新事件，不重试错误官网news路由，不采用Dec1性能。
- [Kimi Blog](https://platform.kimi.com/blog)：原始完整26项最近Nov7、changelog Nov6，重新按本窗判定该入口无相交列表项。
- [Hunyuan Research](https://hunyuan.tencent.com/research)：原始All API11项均2026，旧Research页面/浏览器有限失败；2025目录不可恢复，隔离不作覆盖保证。
- [Z.ai Research](https://www.zhipuai.cn/zh/research)：原始两页末端Dec7 GLM4.6V/Dec8 AutoGLM、没有更多，release Dec8/Sep30。现目录未保存本日前旧段；本窗外Dec7日编码不提前挪入Dec5/6。历史缺口隔离。
- [Seed papers](https://seed.bytedance.com/en/public_papers) / [Blog](https://seed.bytedance.com/en/blog)：原始官方2025 API首段paper Dec15/Dec2/Oct22，Blog Dec24/18/16/Dec2/Nov27；跨本窗后停止，不读94篇库存。Dec2 GR-RL不借submit重收本日，日编码精度限制保留。
- [ERNIE Blog](https://ernie.baidu.com/blog/zh/)：原始2/2至Nov7，前页Nov21/Dec9邻接，无相交列表项。
- [MiMo](https://mimo.xiaomi.com/)：原始Paper8项Oct21/Jan8，部署路由HSS Dec19/Safety Dec18；无date条目及More历史不全，隔离，不借相邻route时间。
- [MiniMax Blog](https://www.minimax.io/blog)：原始13项及中文Oct27/Dec23邻接，无本窗该目录项；无具名触发，不扫额外Agent Tech Blog。
- arXiv：如下独立主题日期检索及有界官方月表补检；first-public缺口不转换成零事件。

## arXiv 发现与准入

四条实际query：`site:arxiv.org "5 Dec 2025"`，分别加（transformer/pretraining/mixture of experts）、（GPU/kernel/KV cache/inference）、（multimodal/world model/VLA）、（agent/retrieval/evaluation/reinforcement）。返回SALP-CG 2601.09717 Dec25和quantum decoder 2512.15689 Dec17等，不是本窗证据；后一decoder不是LM解码。相关窗外项不扩审本日。

官方[cs.RO 2025-12首1–25](https://arxiv.org/list/cs.RO/2025-12?skip=0&show=25)网页Cache miss，原生替代成功，总876，仅浏览首段25标题并停止，不翻月库存。主线可能相关19项精确v1完整题摘实际读取；第一次大输出中段截断的四项00041/48/49/50定点重新读取，才计完整摘要。六个明确不属于基础模型/学习机制切片的标题不转队列：00019外科数字孪生综述、00033工业工程概览、00034工业臂设计、00051微机器人磁力建模、00057果园遗传排程、00072auxetic器件结构；不是对全部cs.RO的领域质量判断。

### 十二项保留的具体潜在增量

| 精确材料 | 原有约束 → 实际增量 → 需要核验的选择 |
| --- | --- |
| [XFlowMP 2512.00022v1](https://arxiv.org/abs/2512.00022v1) | 泛生成轨迹难同时满足任务语义与高阶动态 → task-conditioned Schrodinger bridge/score motion field → 生成动作与动态可行性的联合条件；不采用降能耗数字作普遍结论 |
| [Learning from Watching 2512.00024v1](https://arxiv.org/abs/2512.00024v1) | 仅手/物体pose丢失交互线索 → 视频foundation model与point tracking提取全任务相关密集关键点轨迹 → 人类视频的动作监督粒度与可迁移边界 |
| [DRIQN 2512.00030v1](https://arxiv.org/abs/2512.00030v1) | 观测噪声异方差/跨环境改变，普通DistRL未建模异质组 → replay subgroup与DRO/implicit quantile worst-case目标 → 鲁棒训练需保护何种shift；不把USV成功率当LLM保证 |
| [ICD-Net 2512.00037v1](https://arxiv.org/abs/2512.00037v1) | 分析IMU模型与视觉退化使状态估计失配 → 学习displacement与covariance并按不确定性加权优化residual → 物理感知/模型融合的置信度条件；不称通用foundation encoder或已校准不确定性 |
| [VISTAv2 2512.00041v1](https://arxiv.org/abs/2512.00041v1) | 离散全景想象缺少在线动作条件值，远程目标替换规划器脆弱 → 短程条件视频rollout转value map并与base planner score融合 → world model辅助而非替代规划器的边界 |
| [SpeedAug 2512.00062v1](https://arxiv.org/abs/2512.00062v1) | 重解释动作时间引入示范外shift，直接RL探索低效 → speed-augmented demos形成tempo prior再RL微调 → 加速执行如何先扩大behavior support；不采用后续v2 |
| [AFRO 2512.00074v1](https://arxiv.org/abs/2512.00074v1) | 静态3D识别目标/几何重建未约束控制动态 → shared-latent forward/inverse dynamics、feature difference/inverse consistency抑制动作学习特征泄漏 → 可控表示与重建优先级。v2 Dec4只是版本线索，没有具名实质修订依据，不冒称v2新事件 |
| [Arcadia 2512.00076v1](https://arxiv.org/html/2512.00076v1) | 静态sim与末端成功标签难定位部署错误 → §3.4将task/scene/robot三路反馈回写资产、动态与监督，§3.3导航/操作共享backbone → 保留真实→模拟→真实的具体反馈路径，不仅“生命周期”措辞。必要决定段实际读，未证明其不可分解/持续改进普遍主张 |
| [Humanoid SL 2512.00077v1](https://arxiv.org/abs/2512.00077v1) | 外加肢体质量/运动扰动学习步态 → learned gait与model-based主动平衡解耦，对照static payload → 保留physical controller边界潜在线索，不泛化为任意VLA安全，模拟结果未采用 |
| [Hyper-GoalNet 2512.00085v1](https://arxiv.org/abs/2512.00085v1) | 固定网络goal-state conditioning → goal解释生成policy参数，state分支执行，latent forward dynamics/单调距离约束 → 参数条件化与输入条件化的替代设计 |
| [Why the face 2512.00262v1](https://arxiv.org/abs/2512.00262v1) | 显式反馈可能遗漏旁观者反应 → 下颏观测/3D facial reconstruction提供robot error检测侧信号 → 保留人类反馈可观测性线索；within-participant泛化不等于跨人可靠，反应不是任务失败真值 |
| [RealAppliance 2512.00287v1](https://arxiv.org/html/2512.00287v1) | 外观资产无程序反馈容易掩盖计划失败 → §3.4 manual-aligned state/program，§4.1固定扰动且完整流程使用magic manipulation隔离低层policy错误 → 保留评价执行/计划分母区分，不只新增100器件。已读必要协议；不把模拟规划成功当真实机器人完成 |

### 四项明确关闭与三项局部重开

完整v1题摘均已读：00021是37方法taxonomy/开放度catalog，00027约200篇VLN方向倡议，00049总结social metrics/sim2real已知问题，题摘未指明新的具体测量协议或对照误判证据；维持这三个窄贡献关闭，不因综述类型自动排除。

[00048v1](https://arxiv.org/html/2512.00048v1)先前补读Algorithm1及因果设计段不足以支持关闭。依据[Mill实际精确v1核心审阅](ROOT_ADMISSION_REVIEW.md#普通差额4项与准确最小修改)，定点补正三项，不宣称作者重新完整读取全文：

| 精确材料 | 实际核心证据与补正 | 采用限制 |
| --- | --- | --- |
| [DREAMer-VXS 00005v1](https://arxiv.org/html/2512.00005v1) | VI-C消融、VI-F成本、VII-B失效段区分好奇心探索与碰撞口径；高不确定窄通道有过度自信导航，省交互仍付额外计算/内存。撤回成熟CVAE/RSSM组合自动关闭，保留窄质量/资源/不确定性反证potential | 模拟与具体评价协议限制归因；不授导航安全、普遍MBRL优越性或first-public |
| [00069v1](https://arxiv.org/html/2512.00069v1) | §3及Algorithm1、§3.2–3.4、§4.2.6区分solver-first Review与失败后Repair；LLM fixed plan直接写cache/return，未再formal solve；signature仅initial+goal，未含domain/environment revision。撤回流程组合关闭，保留窄执行/验证条件potential | 这是文本路径的局部静态缺口，不是实际运行失败；不授缓存计划已验证或变化环境安全，小soft-goal消融不证明普遍性能 |
| [00048v1](https://arxiv.org/html/2512.00048v1) | Appendix A Figures11–15中持续DAG指导测试比RL-only低return/更高low-return；训练加速prior不等于执行时应持续保留bias。撤回临床应用自动关闭，保留训练/执行条件反证potential | 18状态/7动作模拟、PC/LiNGAM/EconML的具体条件不证明通用因果优势；不引入临床效果或科学应用结论 |

这三项连同原十二项共十五项potential，全部尚缺个体first-public；未因此变成落窗候选、评分或Evidence完成。路由分别为Ch25/26、Ch79（物理action仍由Ch26拥有）及训练/执行条件；必要命题实际采用前还须对读唯一owner与相邻段落，不以主题相近授已有覆盖。

[00050v1](https://arxiv.org/abs/2512.00050v1)官方admin标记与[2507.13171v1](https://arxiv.org/abs/2507.13171v1)大量文本重叠。已定点完整读取旧v1摘要：同作者EEG ErrP预训练decoder→概率reward、MuJoCo Kinova任务与同样核心结果，当前摘要无改变该机制的修订说明，按重复事件关闭；不称withdrawal、抄袭或安全已证。

## 日期、Books与停止条件

上述v1 histories的submission横跨Oct6–Nov29、月身份为2025-12，恰好说明不能从ID或Submitted归日。各精确页未提供个体first-public。定点official域查询00062/00074/00076/00085公告线索实际空；已实读官方月/announced年月权限及历史catchup/Atom有限失败原始记录，不能再用同接口证明日。十五项为本窗终态保留项：不评分、不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证，不声称Evidence/Coverage通过。

必要重开材料：具名精确v1官方历史new公告/RSS/email或可信原始正文首次公开范围，必须完全落窗；恢复后逐项按准入校准和分数投入必要阅读，不能以摘要替代审阅。旧Qwen/Hunyuan/Z.ai/MiMo目录需2025原始邻接段；只定点恢复本窗。必要日期缺口是真外部项，不是尚未做的题摘判断。Books为暂缓日期/证据，不写成仅报告或已有覆盖；无共享写入。

本日作者侧普通扫描及四项准确差额已补正，普通待办0；十五项potential、四项关闭。确定落窗候选0不等于零事件。交Mill仅复查受影响集合及终态措辞；本记录不覆盖其§6未通过结论，也不自授日级完成。
