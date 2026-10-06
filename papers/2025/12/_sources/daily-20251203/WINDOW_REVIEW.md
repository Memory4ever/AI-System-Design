# 12/03 独立窗口与证据

执行起点2026-10-02T18:09:50+08:00，必要阅读至18:12:06+08:00。本日空停点已核，启动重读全部合同、每日组、Prompt与ROADMAP。窗口Dec2 09至Dec3 09BJT（Dec2 01Z至Dec3 01Z）。

## 14源原始邻接

实际重读[固定目录的原始观察](../daily-20251201/RECOVERY_NOTES.md)逐源邻接，重新用本日边界判断；不读/复制其他Daily结论。OpenAI本轮重新成功解析RSS：Dec2 01Z至Dec4 01Z返回Dec3 08Z基金、10Z Neptune收购、10Z Confessions；三者均在本窗之后。Anthropic原始publicationList Dec2 18:58:43.576Z工作研究完全落窗，下一条Dec4 17Z；本文核心、使用协议和Appendix限制实际读取。

Google固定Blog/DeepMind第3页Nov21/Dec3边界：Dec3条目仅日精度可与本窗尾段相交，不用目录日文字授09前；必要日期保留。Meta固定第4页Dec1/Dec12夹本窗，没有新release依据；Qwen旧Sep23/新动态历史不可见；DeepSeek官方release Dec1/下一2026固定邻接，已有日精度请求不重新搜索；Kimi全Overview Nov7及changelog Nov6；HunyuanAll11项2026且旧Research不可见；Z.aiAll第2页Dec7终点/release Dec8；Seed2025paper首段Dec2 GR-RL/Oct22、Blog Dec2/Nov27，GR-RL仅日编码；ERNIE2/2 Nov7、相邻Nov21/Dec9；MiMoPaper8项Oct21/Jan8及路由HSS Dec19/Safety Dec18、无date历史限制；MiniMax13项及中文Oct27/Dec23。旧目录限制不升级为覆盖通过。

## arXiv

四条实际query：`site:arxiv.org "2 Dec 2025"`分别加transformer optimization、GPU inference cache、multimodal world model、agent evaluation reinforcement。命中越过日期的Gate-Norm/医疗SALP/Bitcoin等；检索未严格落实日期，停止扩页。SALP明确医疗治理应用、Bitcoin的MoE是货币概念，范围外；不组成候选。Gate-Norm精确v1实际读完整摘要及版本：submitted Dec3 07:47:49Z晚于本窗截止，权重QK耦合剪枝的潜在增量只作窗外恢复线索，不授first-public。

官方cs.DC/cs.CV十二月首段网页失败后原生有限替代成功，实际显示并浏览到第23条（输出停止位置），不是全月。只把模型/系统相关具名项回精确v1完整摘要，未把整段变为逐项关闭队列：

| 精确v1 | 原文潜在设计增量与本窗处置 |
| --- | --- |
| [IslandRun 2512.00595](https://arxiv.org/abs/2512.00595v1) | typed placeholder可逆匿名化穿越不同信任域，同时路由到数据；潜在语义/隐私边界，日期隔离，不采用“新范式”自评 |
| [SmartFed 2512.00902](https://arxiv.org/abs/2512.00902v1) | LoRA rank作为细粒度专家，按输入/预算激活并跨矩阵分配quota；潜在训练复用机制，日期隔离 |
| [Joint Partitioning 2512.01039](https://arxiv.org/abs/2512.01039v1) | 分割与placement运行时联合解析，模型容量profiling驱动重新分配；潜在执行取舍，日期隔离，未证明算法/生产效果 |
| [Tangram 2512.01357](https://arxiv.org/abs/2512.01357v1) | tensor级参数共享、按需KV分配与GPU亲和调度减少冷启动传输；潜在状态/调度机制，日期隔离，不采用最大加载加速 |
| [Fantasy 2512.02278](https://arxiv.org/abs/2512.02278v1) | 超单卡图索引以GPUDirect Async重叠搜索和传输；潜在RAG检索系统增量，日期隔离 |
| [Adapter Shield 2512.00075](https://arxiv.org/abs/2512.00075v1) | 图像embedding可逆密钥变换与多目标扰动，授权恢复与未授权生成分开；潜在生成安全机制，日期隔离，不用摘要证明任意攻击安全 |
| [SemImage 2512.00088](https://arxiv.org/abs/2512.00088v1) | HSV多任务解耦及语义边界行作为表示替代分支，非仅分类排行；日期隔离，不把可视化当可解释性因果证明 |

SIMPLE为具名同一家族定点去重，已校准理由未变化且仍日期未决，不重新评分。[TokenScale 2512.03416v1](https://arxiv.org/abs/2512.03416v1)和[FFTrainer 2512.03644v1](https://arxiv.org/abs/2512.03644v1)完整摘要读到token velocity+convertible decoders、富余网络状态保存；提交Dec3 03:45:32Z/10:27:35Z在截止后，仅窗外线索。没有将宽月列表号归到Dec3。

公告必要替代有限停止：精确abs、官方月身份、历史列表/API/帮助/OAI均没有个体first-public；受限性质已有原始记录，未循环同接口。接受具名历史new公告/RSS/email或可核实首发正文，重开真实归属日，不跨月扩扫。

## Anthropic作者证据判断

[原始研究](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)官方字段`2025-12-02T18:58:43.576Z` = Dec3 02:58:43.576BJT，非午夜日编码，完全落窗。

准入命题：用自主动作数替代可委派/成功会混淆评价对象 → 本研究同时报告更长连续工具调用与仍依赖验证的调查口径 → 自治活动与可靠任务完成要分开测量。评分只对此局部证据：Design Delta 2 + System Reach 1 + Durability 2 = 5。

实际证据位置：Key findings、How much work can be fully delegated、Claude Code usage trends/Figure3、Appendix Limitations。研究使用132人调查、53访谈及20万Feb/Aug轨迹；轨迹指标为每段最大连续工具调用均值，不是任务正确率。调查“完全委派”定义解释不统一，便利/目的采样、非匿名与回忆偏差并存；轨迹比例采样只支持任务类型相对变化，不支持绝对工作量。没有随机或配对质量对照，不把行为趋势当因果生产率。标准审阅作者侧已读够这一窄命题，准入/证据仍待非作者校准；不证明监管能力衰退必然发生。

Books实际对读：`PLATFORM-EVALUATION-SYSTEM` Ch66“从目标到证据，而不是从指标到目标”（约79–101行）从intended use/risk定义对象、群体、failure及裁判，不以可采metric反推成功；相邻Ch67开头区分观测与质量决策。`AGENT-PLATFORM` Ch84“Serving结束不等于Agent任务结束”（约50–88行）要求terminal evidence满足contract，Ch81 State Machine段保留Verifying/approval，不以模型文本授状态完成。该命题已有覆盖，不新增正文；本地趋势仍是局部上下文，不新增机制一律仅报告。无Books实际改动。

作者普通待办0。外部日期/目录项仅安全终态；准入与作者证据/Books判断待root核验。继续下一日。
