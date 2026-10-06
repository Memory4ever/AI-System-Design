# 2025-10-07 bounded screening

作者Huygens；BJT `[2025-10-06T09:00+08:00,2025-10-07T09:00+08:00)`。own请求代码acquire/repair及每次receipt保存真实URL/时间/分页。年份/提交日是发现范围，不充当first-public。

## 实际入口与停止

四主题均为UTC submittedDate `[202510060000 TO 202510062359]`、start0/max40、submittedDate升序，完整表达式在acquire原请求。本窗模型主题第三次export恢复11/11；系统、Agent、多模态三次恢复仍429/timeout，非零命中。最后再有限简化：`ti:agent AND (all:LLM OR all:language)`、`ti:inference AND (all:LLM OR all:transformer)`、`ti:vision-language OR ti:VLA OR ti:world-model`，同submitted范围/start0/max40，未指定sort，均timeout；URL/时间见fallback receipt，不误记升序或零结果。CL首25三次失败；CV首25/total95、DC8/8、PL3/3、IR8/8恢复，相关标题共44；未下载其余70CV作为队列。submitted范围只是发现切片，不是public-event窗口覆盖证明。

模型11去重；CV16相关标题（含模型已命中MedCLM）、DC OptPipe1、IR3，合并30精确v1完整题摘/可见history实际读完。标题补检不是44条逐项题摘，更不是所有分类全文队列；30 AB不是Evidence完成。初次失败raw/receipt与恢复结果均留存，重试不覆盖原失败记录。

## 已关闭4身份

均实际完整题摘、可见history读到，不发现摘要页明确withdrawn/correction安全说明。首次公开未核实不影响以下具体贡献关闭，不再为它们请求时间。

- [2510.04479v1 VaseVQA-3D](https://arxiv.org/abs/2510.04479v1)：664古陶器数据及域适配改善领域识别/lexical similarity；原题摘没有修正通用3D融合/推理机制的具体增量，不由“3D VLM”主题相关准入。
- [2510.04536v1 3Dify](https://arxiv.org/abs/2510.04536v1)：Dify+MCP/RAG/CUA操作DCC与偏好选择的应用组合；没有新协议约束、执行一致性或机制成立条件。不能借成熟权限原则凑评分。
- [2510.04631v1 Process industry adaptation](https://arxiv.org/abs/2510.04631v1)：将既有SciNCL图邻接对比学习用于工业日志/PITEB；报告9.8–14.3%域指标与更小encoder，但没有新增图学习机制或通用有效性边界。
- [2510.04704v1 AtomWorld](https://arxiv.org/abs/2510.04704v1)：CIF晶体编辑/属性建模与材料研究基准，属ROADMAP暂缓AI for Science；保留其结构错误反侧，不把materials应用经Evaluation重新引入。必要反侧只读相关错误与限制，不展开科学附件。

## 26日期潜力，不排除贡献

各原v1题摘已读。仅submitted/Atom时间不能证明当窗首次公开，无评分/正面Evidence/Books。下列具体增量如果真实落窗可继续准入，而非因小模型、局部任务、负面结果或Books主题已有而排除。

| v1 | 需要重新考虑的具体选择 |
| --- | --- |
| 04401 | 几何受控组合计数失败，颜色/大小/提示混杂需分开 |
| 04428 | 高质量VLM深查询分析与小批迭代选帧成本取舍 |
| 04450 | generator/tokenizer一致性正则，非单纯更好tokenizer |
| 04477 | lesion box显式→隐式→弱监督CoT curriculum；临床宣称需要必要核验 |
| 04483 | pattern shifting和consistency enhancement分模块/数据两阶段，局部电商不自动排除 |
| 04504 | 像素异步去噪时间提供清晰非目标上下文，改变同步采样假设 |
| 04514 | 去文字捷径后的图表视觉工具推理，评价shortcut反侧 |
| 04533 | 轨迹切向放大与一阶近似，hallucination-resistant措辞需限制 |
| 04539 | GT单view与多view不同LoRA，控制与一致性冲突 |
| 04547 | encoder outliers不同于语言，middle-layer registers/token deletion的量化边界 |
| 04564 | 描述语义basis投影VLM表征而非昂贵定制微调 |
| 04573 | VAE thought-block空间/双向latent diffusion revisable reasoning |
| 04576 | conditional GAN真实性/匹配分投影与自适应权重，保留生成机制潜力 |
| 04587 | 日常专家view日志转where/why行为监督；专家验证和临床指标不可外推 |
| 04633 | 单topic/assessor LoRA预测未判文档，保留人类gold与排名相关性边界 |
| 04637 | 双人AR-diffusion协调gesture与高层语言引导，保留多模态生成潜力，不当物理闭环 |
| 04773 | token分布偏好unlearning方向一致性不等不可恢复删除 |
| 04800 | inter-/intra-layer attention/SSM融合系统比较，不由题目称全替代 |
| 05024 | 训练期请求坏行为限制未请求泛化，SFT局部对齐反侧 |
| 05069 | entropy趋势切latent/explicit，switch上限与预算质量取舍 |
| 05077 | SLM互补选择及协作test-time scaling，不因模型小排除 |
| 05087 | authentic→synthetic student/dialogue微调与评价，教育领域下测量/隐私边界需核 |
| 05186 | memory/activation reuse/bubble联合优化PP，非只offload更大模型 |
| 05288 | adaptive clipping的DP条件与Adam归因，synthetic小实验不自动排除 |
| 05364 | attention/SSM/hybrid比较的设计反侧需核，综述名称不自动准入或排除 |
| 05396 | interdocument block sparsity+query/document contrastive training改变ICR成本 |

## 官方事件与首批

Petri同slug Research/原事件页time10/06 11:10UTC；Apps RSS10/06 10:00UTC。Curie有效FIRST已通过，10:11:24独立记录已核Petri深入完成1/Apps标准完成1及具体owner处置，两仅报告、Books差额/提案/写入0；最终DAY仅待作者两窄同步写后回核，不作者自审。Codex GA/AMD两贡献关闭维持，SDK功能与容量合作不能直接当机制证据。Google S2R只有Oct7日期/未知时区，先隔离潜力，不取submitted推发布。

RSS AgentKit10/06 GMT00即BJT08早于起点1h；整份恶意使用报告10/07 GMT03即BJT11晚于终点2h，窗外归属线索；不混七case身份。网页后续Nov13 update与当前导航不归于历史Oct6变更。

注意：`petri-report.raw`实际是原页面关联的Claude4 May2025 System Card（首页面），文件名失配保留原下载，不当Petri报告/全文已读证明。真正技术说明`https://alignment.anthropic.com/2025/petri/`必要方法/评价/反侧已实际读完，不遍历全SystemCard/附件。13必要arXiv核心与S2R核心实际边界见[CORE_BOUNDARIES](CORE_BOUNDARIES.md)，已由Curie定点独立复核。S2R从本日own October page2标题恢复，正文Oct7无时区；独立查漏恢复后28论文加此官方家族共29日期潜力，不评分/正面采用。

## Curie独立有界查漏恢复（作者同步2026-10-05T10:18:16+08:00）

原作者30完整题摘/26潜力不变；以下两项由Curie独立额外实际读完整精确v1题摘及可见history，见[FINAL](FINAL_INDEPENDENT_REVIEW.md)，不回填作者阅读。归并共32身份、28论文潜力，另S2R1共29日期隔离。

- [2510.04417v1 Partial Information Decomposition via Normalizing Flows in Latent Gaussian Distributions](https://arxiv.org/abs/2510.04417v1)：高维连续模态PID估计成本/准确性约束→Gaussian PID替代优化及保信息encoder→多模态协同测量与模型选择潜力。最优性/保信息摘要主张未核证明；submitted `2025-10-06T01:08:34Z`非first-public，缺完全落窗公告/bounds，不评分/正面Evidence/Books。
- [2510.04506v1 GRACE: Generative Representation Learning via Contrastive Policy Optimization](https://arxiv.org/abs/2510.04506v1)：静态encoder丢弃生成路径→contrastive信号作rationale policy reward后mean-pool→生成/检索表征训练目标与成本选择潜力。可见rationale不等内部推理faithful，摘要性能未核不采用；submitted `2025-10-06T05:46:56Z`非first-public，同样缺完全落窗公告/bounds，不评分/正面Evidence/Books。

同次独立标题外SPEGNet04472/LLVM04890两完整AB关闭样本分别仅特定camouflage detector组件方案、通用SIMD/IR未建立模型计算关系；不混原作者四关闭分母，不扩44标题/CV余70为队列。Curie共实际17完整题摘样本（原集合13加标题外4），并非二次全读30AB。仅外部隔离项具名恢复，不由局部/小模型/负面或已有主题统一排除。
