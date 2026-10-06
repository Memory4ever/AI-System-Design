# 2025-11-15 首批准入校准包

作者Planck；窗口BJT [Nov14 09:00,Nov15 09:00)。本包是首批增量/负侧校准，不是日级或Books完成。actual fresh合同/每日来源与本日原源已读；不从14或旧Weekly反推。

## 入口与实际原源

12适用分类，四组窄主题submitted `[20251112190000 TO 20251113185959]`仅发现；start0/max100/ascending，返回training51、inference6、agent12、multimodal10，未去重，不叫本日79篇。真实query/时间/响应与stop在各`raw-arxiv-{topic}.xml.request.json`，均未满100，停止start100；宽标题不全量送题摘。选10家族恢复一次精确v1，[完整题摘raw](raw-arxiv-first-exact-v1.xml)全部已实际读取。初始最新version不倒填v1；Harli晚编号11729更须独立核首公开。

## 三个先交方向

| 身份/精确版本 | 旧约束 → 原文增量 → 待核设计选择 | 最低审阅与反侧 | owner路由，不是缺口结论 |
| --- | --- | --- | --- |
| [Echoing 2511.09710v1](https://arxiv.org/abs/2511.09710v1) | 单Agent任务表现不能直接证明Agent间交互可靠 → 60配置/3领域/2000+对话中角色逐步镜像，推理投入增加也未消除，定向结构化回复部分降低 → 需分别评价任务完成与角色/委托目标保持，而非把完成率当忠于principal。 | 初筛拟2+2+2=6；属于设计反证，深入只读评价定义、同模型推理档位/提示与对话长度对照、结构化干预残余。不外推所有模型、所有协议；v3的66配置/2500+和当前Salesforce Nov25 Blog不倒填v1。 | `AGENT-MULTI-AGENT` Ch82，具体差额待校准后对读，不因名称未出现就整合。 |
| [UGCS 2511.09864v1](https://arxiv.org/abs/2511.09864v1) | RL checkpoint高方差，末点/全验证有局限 → 用每样本不确定度选hard QA，短窗口中高不确定样本reward平均形成排序信号且摘要称不增加forward → 需核是否可替代validation排名及其失效边界。 | 拟2+1+2=5；核uncertainty定义、选择窗口/数据泄漏、三模型三数据对照及选择代价；摘要generalization不是普遍保证。 | `TRAIN-CHECKPOINT` Ch35路由；不把成熟早停原则算新增。 |
| [TawPipe 2511.09741v1](https://arxiv.org/abs/2511.09741v1) | 长序列activation通信随长度增长；weight-passing仍冗余P2P → 拓扑设备分组、固定weight/gradient shard及overlap收敛跨节点传输 → 需在序列/模型/拓扑条件下比较activation与weight两条通信路径。 | 拟2+2+2=6；核24GPU以内的实际硬件/预算、WeiPipe/FSDP/PP对照、长序列交叉点、内存及拓扑限制。不能仅用throughput数字证明通用优势。 | `TRAIN-PIPELINE-PARALLEL` Ch38路由；Ch36通信交接，不重复写两个owner。 |

## 代表性负侧与保留

- [PALMS+ 2511.09724v1](https://arxiv.org/abs/2511.09724v1)：完整题摘实际读。Depth Pro现成单目深度、scale-aligned点云、几何floorplan convolution和particle filter组合，80观测/4楼/33轨迹支持基础设施无关的定位实例；未给改变foundation model表示、训练、VLA控制或运行时设计的机制/边界。当前按项目范围关闭，不称局部实验无价值，日期未核实不另建无意义请求。WACV2026 accepted comment是状态字段，不当2025窗内会议发布触发。
- [Introducing OpenAI for Ireland](https://openai.com/index/openai-for-ireland)：本日fresh RSS `Fri, 14 Nov 2025 04:00:00 GMT` = BJT12:00落窗。实际核心L22–37仅合作、技能培训、workshop、mentor及青年创业支持，没有模型/训练/推理/Agent执行的新机制或纠错。关闭；[raw网页](raw-web-04.json)、[rawRSS](raw-openai-rss.xml)支持，不拿机构声望准入。
- **不关闭** [Compact CED 2511.09748v1](https://arxiv.org/abs/2511.09748v1)：完整题摘中英语→德语translation error场景确有限域，但约1B资源前沿与0.6B实体/数字漏检、质量/VRAM/延迟联评有潜在设计证据。不能因成熟calibration/vote或领域应用自动关闭；仅核可比条件后定贡献与owner，暂不宣称所有SLM“sweet spot”。
- 另外6份题摘已读：Audio-VLA（contact audio/过程评价）、GAD（黑盒on-policy discriminator奖励）、CP-WBFT（confidence probe加权及故障模型）、Harli（decode/PEFT共享memory与SLO预测调度）、BuddyMoE（完整API摘要只写问题、缺具体新增机制）、Compact CED。均未以摘要实验细节不足排除；BuddyMoE需要定点核心解释标题的expert redundancy。下一批只送新增方向，不重复前三项。

## 日期与轻量信号停点

三精确原页已核submitted原值：Echoing Nov12 20:17:10Z；UGCS Nov13 01:46:58Z；TawPipe Nov12 21:06:37Z。提交!=公开。[raw05](raw-web-05.json)保留当前原页/一般availability；[raw06](raw-web-06.json)实际官方精确日期/ID及作者路径queries，未得到本日官方公告身份。一般schedule与“ID在announcement分配”不能单独认证本日lowerbound；不补造Nov14 09时刻，不把晚版本comments/标题变动本身当重要修订。当前三项都不是确定落窗候选。

第一次旧month路径GET404，随后实际原页month链接click指向canonical `/list/cs.AI/2025-11`；已按这个真实身份修正CL入口，属于有限接口纠正，不沿空路径无限猜。canonical月表仅为本日相关ID切片标题查漏/列表身份，若无dated announcement仍不能授日期。作者Blog恢复只得到Nov25 Salesforce页面，隔离，不采用其新架构结论或扩本窗。

**请求root**：先核三条具体准入增量、两负侧是否理由过严、CED的局部资源/失效因子是否应保留，以及评分对象是否误含成熟原则。日期尚缺官方历史公告/list身份或作者精确首次公开范围，不请root凭schedule放行。校准前作者继续无关来源尾部、其余已选题摘与有界列表补检，不先读所有全文。

## 后续实际修复，不代独立结论

BuddyMoE接口摘要截短已用HTMLv1 L62–67完整摘要及L136–220必要机制补齐，原raw10持久保存。coactivation conditional buddy不是functional equivalence；TAE低于阈值禁替、CPU residency fraction绕过、缓存候选排序后替missing expert是近似执行。门控阈值文字及algorithm是否覆盖门控仍需必要反侧核验，不授无损。新增方向另送有限包，不重复上述三项。

四主题及有界标题查漏后实际选36精确v1完整题摘，35保留潜在贡献、PALMS+范围关闭；[逐项具体理由](ARXIV_SCREENING.md)、[来源停点](SOURCE_TAIL.md)已落盘。当前metadata轻量信号已读，不把晚版本/accepted状态自动作重要事件。仍非日级/Books完成。
