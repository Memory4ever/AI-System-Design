# Nov20本轮arXiv首批有限准入提案

## 1. 查询、去重与阅读分层

作者Noether；2026-10-15T15:38+08。本轮仅Nov19 BJT补窗，当前95/132不增。实际先读官方Advanced表单并保存SUP_ARXIV_FORM及web原件；按表单字段发五次非legacy Advanced GET，submitted_date_first Nov18–19只作发现，不认证public，announcement只月粒度。MODEL/LEARNING/SYSTEM/AGENT/MULTI完整query与起止/HTTP/bytes在各receipt，不使用catchup/API/RSS/OAI或旧失败重试。

MODEL首50/total64、LEARNING首50/77，应用与泛Transformer噪声较多，停0不翻余页，将收窄这两主题；SYSTEM24/24、AGENT12/12、MULTI19/19。五返回155次/去重115身份只为本日发现量，不是115篇当天论文或题摘已全读，更不是冻结全文队列。与本日本来30身份重合16，原有效准入层按精确身份/版本/命题复用，不搬邻日78/62。115题名已作相关性浏览，明确范围外只作入口噪声，不把应用词硬排含糊贡献。

HTMLParser生成的SUP_ARXIV_SEARCH_FIELDS_20261015.json只是原字段投影，脚本不作语义判断/自动关闭。当前完整题摘实际新读14身份；其中六个搜索返回晚版本，另各一次普通abs精确v1并实际读完整v1题摘（15098/15015/14712/14582/14476/14465），不据晚v4等回填。其余八搜索abstract-full原id为精确v1，全文摘要已实际读。搜索卡显示v1 Submitted Nov18/originally announced November；但15098/15015精确v1的title/citation/dateline/history另给Nov19，不能概括全部Submitted18，冲突及权限见§5。所有这些字段仍不授Nov19首次公开或当天重要修订。

## 2. 十个明确潜力提案／未评分未Evidence

| 精确v1 | 旧约束→实际潜在增量→需重考虑的选择与采用边界 |
| --- | --- |
| 2511.15098 Visual Token Redundancy | 视觉token pruning不等各类dMLLM同样冗余→from-scratch/AR转diffusion与long-answer、late-denoising恢复的局部反侧→按架构/任务/时步分选skip/prune。先保信息损失及条件，不采所有dMLLM加速/恢复保证。 |
| 2511.15015 DynaExq | 静态expert bitwidth不能跟随hotness变化→在线精度controller、async promotion/demotion及hybrid memory pool→精度变资源选择。v1没有晚v4的stable-handle/2.73×recipe，不回填；HBM/质量/切换正确性仍需Evidence。 |
| 2511.14981 Feature KD without logits | feature和logit loss可能相互限制→仅feature训练backbone及teacher层quality选择→是否必须并用logit CE。小CNN/ViT与三图像集不阻止机制潜力；不外推LLM或15%普效，尚未核实际目标/geometry证明。 |
| 2511.14761 VARC | ARC以语言串解释不是唯一接口→canvas视觉image-to-image、从ARC训ViT并test-time training→表示与适配预算分责。不是benchmark换名，须核canvas与TTT机制/对照，不采60.4%跨协议优胜。 |
| 2511.14760 UniGen1.5 | 图生/编辑共训reward与instruction理解相混→共享reward联合RL、Edit Instruction Alignment先建立指令理解支持→RL收益的成立条件。支持潜力而非直接宣唯一因果，实际stage/ablation与预算后责。 |
| 2511.14712 FreeSwim | 简单local window重复内容/丢全局→保持训练尺度感受野、full-receptive-field支路cross-attention override及cache→局部细节/全局一致与计算取舍。训练free不等部署free，不采普遍一致/优于训练版。 |
| 2511.14691 Spiking STDP Transformer | 普通spiking attention仍依赖显式相似矩阵→把query-key相关写入STDP突触权重→事件驱动状态与内存计算接口。不是因生物类比准入；CIFAR与估算能耗不授真实硬件/LLM或GradCAM因果解释。 |
| 2511.14650 AutoTool | 逐步重复LLM选tool高费→历史trajectory有序转移图及参数信息旁路部分推理→tool usage inertia何时可替代重新规划。需核分布漂移/错误路由/回退与总体成本，不把graph置信当授权/成功。 |
| 2511.14582 OmniZip | 独立audio/video压缩不能表达跨模态信息密度→audio anchor/每时间组保留分数指导video pruning及交错时空压缩→压缩预算需按时间/模态条件。原v1支持此潜力，3.42×/1.4×未采用，静音/音画不符反侧后责。 |
| 2511.14476 Pluralistic Values | majority/binary偏好聚合不保证保留群体分歧→群体、rating scale与disagreement处置的局部对照→评价人口/监督选择改变alignment解释。保US/Germany、多个值维度与DPO/GRPO配方混杂，不把demographic关联当个人特质或安全普效。 |

## 3. 三个准入含糊点／只需最低决定域

- 2511.14823 Dynamic Nested Hierarchies：摘要明确声称能调层数/嵌套/频率及convergence/regret，但尚未见具体动态选择机制与假设是否实际推出该变化。只补定义/更新准则及关键定理假设，不因理论/小实验关闭，也不由宏大自主进化措辞直接授P。
- 2511.14465 nnterp：原HF实现/NNsight+rename+打包validation可能解决真实数值兼容问题，但摘要未给不同实现造成的具体反证或新接口语义。只核实际validator/映射及数值等价边界，不能因是library关闭，也不能只凭“验证测试”授新长期机制。
- 2511.15074 Rogue One：完整摘要有qualitative feedback/flooding-pruning与19classification/9regression的通用tabular入口，不因biomarker例子自动Science范围关闭；但是否只RAG+三角色迭代仍含糊。只核flood/prune具体规则和反馈改变哪个控制选择，不展开领域实验或附件。

## 4. 一个代表性具体关闭提案

2511.15061 Beyond GeneGPT/OpenBioLLM，完整v1题摘已读：其实际任务/评价均genomic QA，主要是开源backbone替换、tool-routing/query-generation/validation的role decomposition及该域得分/延迟结果。摘要没有独立通用新执行/信用/验证机制或主线反证，且具体scientific-domain问答按ROADMAP暂缓；拟C，不因生物标题替代阅读，也不借Agent/评价重新纳科学应用。保当前search comments仅SIGIR-AP2025/ACM分类，未见本返回明示纠错/撤回/安全变化，不声称遍历版本史。贡献关闭后不为其缺日另建请求。

## 5. 当前/日期权限

十四current搜索原字段实际轻读：15098v2 June2026、15015v4 Sep2026、14712v2 Dec1、14582v2 Apr2026、14476v2 Nov25、14465v2 Dec14，其余八v1。comments多为接受/页数/代码，无本返回明示withdrawn/correction；不把未显示标记认证全史无标记。版本号本身不触发全稿/双版对比，晚版不纳本窗；若当前具体变化影响将来采用，才定点恢复对应说明。两份原日期冲突已由Ohm§10.4实际核，作者也实际读回本地dateline/history：15098v1为Wed,19Nov2025 04:13:36UTC，15015v1为Wed,19Nov2025 01:27:54UTC，其citation_date/citation_online_date均Nov19；搜索卡各仍为Submitted18/announcedNovember。两端原值并存，只记提交/索引字段冲突，不由citation_online_date、提交时刻或月公告推实际公开日。其余项按各自原字段，不再写“全十四均Submitted18”。潜力项先留公开资格，不评分/列确定表或Books，也不以未知日期改C。

## 6. 交首批准入校准／普通继续

请root转Ohm实际首批十P/三最低域/一C准入校准，原件在本日SUP_ARXIV五HTML、SEARCH_FIELDS与六精确v1 abs；不要把投影/脚本或本表当真实独核。两宽主题将收窄，剩本日相关标题补检/新题摘差额与必要当前/日门仍普通；已有本日30有效层不重全池。三最低域准备好单独交，不等全Sources。三SAM必要核心/原PDF限取得分责仍普通，S2ST已真实POST/root接纳释放不重。无书锁/legacy在途/stage/commit/push或普通thread/UI消息；本日尚未DAY/FINAL。

## 7. 已发生三最低域归并（覆盖§3/6的未决状态）

作者已实际完整读Ohm§13，root亦实际读回：14823/14465两个窄P与15074具体C通过，见本日`SUP_MINIMUM_20261015.md`。因此首十四贡献层现为**12潜力/2具体C**，不再保三minimum普通决定待办；原十P和15061C不重。14823只保具体更新规则假设，Eq5/12/momentum证明项/固定delta保证及v1header与正文2026日期冲突保持隔离；14465只保HF4.54 tuple→tensor消费者静默错误和sanity各属性分验，不授形式等价；15074按现成generate-test-prune分工无独立增量关闭，不因生物例子/非硬规则关闭，不扩28数据集。

这是贡献准入有效层，不授12项日期资格、评分、正式候选、Evidence或Books。15098/15015的两原日期冲突继续按§5保留，提交/citation_online_date不变公开日。当前root96/132不含Nov20；SAM3已按唯一窄锁实际保存/selfread交真实POST，S2ST完全闭合不重，其他普通工作继续。
