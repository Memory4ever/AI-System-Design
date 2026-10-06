# 12/02 独立窗口记录

执行：2026-10-02T18:05:02+08:00 至18:07:05+08:00。启动已重读AGENTS、研究/Report合同、每日来源组、Prompt、ROADMAP；本日原无README/checkpoint。窗口Dec1 09:00至Dec2 09:00BJT，即Dec1 01Z至Dec2 01Z。

## 原始来源范围

固定历史目录可以复用原始邻接字段，不能复用前日报结论。本轮实际重读[原始目录恢复记录](../daily-20251201/RECOVERY_NOTES.md)中各源的原始邻接段，对本日边界重新判断；没有从01候选表复制日期或分数。另实际重新请求Anthropic、DeepMind第3页、Google2025Blog、Meta第4页、Qwen旧站、Kimi Overview、ERNIE首页、MiniMax首页，均取得原生HTML。OpenAI RSS原生403、网页XML不支持，停止重试并仅复用先前成功的原字段。

- OpenAI：已实际成功的RSS邻接原字段Dec1 05GMT商业合作（Thrive/Accenture），本日落窗但题名明确是合作消息，无新增模型/训练机制，关闭。原始feed本日其他非研究消息不等于机构研究无遗漏；当前403是读取受限，不能零事件。
- Anthropic：本轮HTML317670字节publicationList实际再见SCONE `publishedOn=2025-12-01T00:00:00.000Z` 和下一条Dec2 18:58:43.576Z。后一条在本窗右端后；SCONE仅日编码精度疑点，保留同一家族已有必要日期请求，不借00Z证明窗外，也不授本日。
- Google：DeepMind第3页、Blog2025原站HTML已取得；重新比对固定原始Nov21/Dec3邻接，均与本日不相交。pubs年字段不归日。
- Meta：本轮原始第4页连续Dec12/Dec1/Nov19；Dec1 AdvancedIF对应2511.10507v1已有相同rubric机制，没有本日新release/重要修订依据；不是用目录收录证明首公开。
- Qwen：旧站17283字节，固定Sep23边界；新站与部署/README有限恢复的历史不可见限制沿原始入口保留。隔离旧目录，不称无事件。
- DeepSeek：正确API Docs原始Dec1 release与官方HF card已实际打开；HF模型对象createdAt `2025-12-01T02:34:49Z` 属本窗，但创建不证明当时公开可见，也不证明API首发。新增工具思考与大规模任务合成有潜在设计增量，日期隔离，不采用比较性能。复用具名原始请求，不反复探主页错误news路由。
- Moonshot：重新取得完整Overview，固定最近Nov7及changelog Nov6，未有本窗列表项；只声明这些入口范围。
- Hunyuan：重新比对原始All接口11项全2026、Research浏览器/原网页失败；2025目录不保留，必要历史隔离，未扫普通仓库提交。
- Z.ai：重新比对原始Research第1页至Dec9、第2页Dec7“没有更多”，release Sep30/Dec8；本日旧段不被现All保留，隔离。
- Seed：重新比对原始2025paper首段Dec15/Dec2/Oct22、Blog Dec2/Nov27，跨本日邻接停止。Dec2 GR-RL的日编码可能与本窗最后9小时相交，具名精确v1题摘另读，不能以日期文字自动移到09前。
- ERNIE：本轮首页26083字节，原始2/2至Nov7及Nov21/Dec9邻接无相交条目；无全机构保证。
- MiMo：原始Paper8项Oct21/Jan8及部署路由HSS Dec19/Safety Dec18重新比对；无date路由、旧More保留不全隔离，不套零事件。
- MiniMax：本轮英文134584字节再见Dec23，原始完整13项与中文Oct27/Dec23邻接；本日无该目录项。

## arXiv 有界发现与贡献

实际四条query以`site:arxiv.org "1 Dec 2025"`加（transformer/MoE/pretraining）、（KV cache/GPU/inference）、（world model/VLA/multimodal）、（agent/evaluation/RL）执行，均空；又换三条单主题日期拼写，仍空。仅检索受限，不证明没有公告。官方cs.LG十二月列表首25标题补检成功；cs.CV同范围Cache miss；catchup/cs.CL/2025-12-01同样失败。未翻整月。月表不能归日，官方announced字段/OAI/假日原始依据只作权限限制和条件排期，不授个体。

首25相关具名完整v1摘要实际读取：

| 精确材料 | 实际增量与处置 |
| --- | --- |
| [Fact-storing MLP 2512.00207v1](https://arxiv.org/abs/2512.00207v1) | 事实/参数容量度量、构造与梯度训练的对应及容量/Transformer可用性冲突，可能修正MLP=无限事实存储的直觉；潜在准入，日期隔离 |
| [FaVeX 2512.00164v1](https://arxiv.org/abs/2512.00164v1) | 批/序列验证重用与将验证器不完备纳入解释定义，可能修正“无反例=解释完备”的设计判断；潜在准入，日期隔离 |
| [Geometry 2512.00196v1](https://arxiv.org/abs/2512.00196v1) | pullback度量区分离散化与逻辑运算、rich/lazy学习几何，潜在表示/学习边界；日期隔离，不按神经科学交叉分类排除 |
| [Orion-Bix 2512.00181v1](https://arxiv.org/abs/2512.00181v1) | 双轴注意力与标签路由/合成表元训练提供小样本表示设计，非仅表格任务排名；潜在准入，日期隔离 |
| [WARP 2512.00272v1](https://arxiv.org/abs/2512.00272v1) | 保持预测的参数对称变换以减少前后unlearning差分泄露；明确安全边界潜在增量，日期隔离，不采用最大AUC数字 |
| [Adaptive prediction 2512.00342v1](https://arxiv.org/abs/2512.00342v1) | 强相关/分布移位下离线估计界与meta-LMS在线漂移，潜在训练/适应条件；日期隔离，不将非线性系统定理外推LLM |
| [ME-Nash-QL 2512.00351v1](https://arxiv.org/abs/2512.00351v1) | 表格两人零和自博弈内存/采样界有潜在资源边界，但官方admin说明与他文大量重叠且ICLR2024，不能当已验证2025原创；日期及来源关系隔离，非撤回，不采用 |
| [RTZ-VI-LCB 2512.00352v1](https://arxiv.org/abs/2512.00352v1) | 部分覆盖+环境不确定条件下robust value迭代与Bernstein惩罚/下界；潜在RL支持条件，日期隔离 |

以上submission为Nov28/29，不等于公告；无个体公开依据，不评分。原来仅按应用题名概括的句子不足以关闭含糊材料：Mill所指11项及GR-RL现已逐项补齐，见[局部补齐记录](./TARGETED_REPAIR.md)。BioArc由必要设计原则段确认科学路线后才关闭；PolyNSD、FiCoTS及安全/反证项具体保留，不以领域、非LLM或小模型作为排除依据。宽目录未扩池。

## 外部处置与Books

日期恢复仅有限替代：官方v1提交/版本、月列表、历史catchup，以及已实读官方字段帮助/OAI原始观察；均不能给个体首公开。新具名项在本窗隔离，不支持正面候选、无遗漏、性能/安全和Books。恢复条件是精确v1官方历史new公告或可核实原始正文发布，只重开真实归属日。DeepSeek/SCONE/GR-RL日精度请求各家族一次，不多日报反复搜索。

MLP候选潜在owner `MODEL-FFN`，实际Ch16开头“Attention决定去哪里找信息、MLP对聚合表示作非线性变换”及两层FFN矩阵段已读；未承载新容量界。相邻Ch15/17仅需在日期恢复且采用命题确定后精确对读，不声称已有覆盖/整合。其他隔离命题同为暂缓，没有新增机制一律仅报告，没有共享Books改动。

作者已补齐本次指出的十二项普通判断/身份缺项；旧普通0声明曾被Mill否决，当前补齐结果待其局部检查，不能当验收。确定落窗候选仍0（不等于零事件）；新增潜在准入与必要日期分别保留，外部项不得升级为Evidence/Coverage通过。继续后续日期，不等局部核验。
