# 10512v1：必要增量、结构去噪反侧与最低处置提案

仅续接03-13已有停点，新增窗2026-03-12 BJT完整自然日。有效P准入及DATE4独核的Mar12 arxiv事件日复用，不从Submitted或Registered单字段再授日期。本文没有具名dated早稿信号，不扫描全网版本史。

精确原文 https://arxiv.org/html/2603.10512v1 ，GET200/260501bytes见 `SUP_HANDOFF9_FETCH_RESULT.json`；保留 `SUP_HANDOFF_SOURCE_10512.raw/txt`。本次实际读§3.2.1–3.4（txt1038–1509，Eq6–12）、§4.1–4.4/§5.1–5.2/§6（1510–1650），完整题摘/作者见本日 `SUP_ABS4_10512.txt`。不读v2、不遍历参考文献或重跑代码；没有独立目视loss图，采用正文披露的值和限制而非自估曲线。

当前实际新增是resource-limited Amazons的局部训练/搜索配方：GPT-4o-mini生成局面评分，既有AE/UCT/GAT与SGGA组合；两个AE分别处理movement/placement，根四节点临时合成super-node；Eq6–8为奇偶深度不同递归累积后按 Hmax+1-height 归一，Eq11 shifted-tanh评分，SGGA有softmax选择、偏置变异与披露的node/generation上限。不能把MCTS、GAT、information bottleneck本身记作本文新机制分。Eq8的深度分母随height增大而减小，单凭该式不能认证作者文字所称一般linear discount或任意深层噪声抑制；其不同累积状态也不能从分母单独推全算法必反向。

直接关键评价与反侧：§4.1省略极早训练loss，moving-average窗口50；movement/placement不仅选样策略不同，任务与目标也不同，正文“policy was the only variable”不能认证同一监督人口的受控去噪因果。F-test仍保留符号占位 F(d1,d2)=Fvalue，p=.035不补成完整统计复现。每对手200局、N30对GPT为45%、N50为66.5%；胜局比较涉及搜索与规则约束，不是teacher逐标签错误已纠正的对照。N20→30的UCT-AE对手胜率79.5→73.5、GAT-AE62→57.5，不能授所有更大搜索单调提升或同总模型费用优势。§5承认弱于领域专用Invader；§6仍将训练何时完成与最终选择策略列未来工作，部署最终选择采用随机分支。

§5.1–5.2把student胜过teacher推为结构过滤，并声称GAT不能记忆随机噪声、有效纠正teacher错误；必要方法/评价未给容量、噪声分布、可靠gold与独立噪声干预条件，不能据更高棋局胜率签一般denoising保证。这不是因棋类领域、模型规模或费时否定P；保留其局部实测胜率与混合方案可行性。没有把上述限定升级为“全部图网络不能去噪”或整篇算法无效。

实际owner旁证只为判断投入、不写Books：已顺读Ch29当前Distillation连续272–308。其gold可信条件、teacher margin/geometry只是代理而非正确性、监督人口与held-out行为验收等明确存在。本文强去噪措辞没有经必要原证建立一个新的普适有效条件，不能借这些现有成熟原则反向给本文新增分或强做NC。

拟 **1+1+2=4**：局部训练/搜索及递归评分配置(1)、受测Amazons与当前低node人口的影响(1)、可复用工程配置而无本稿已证新的长期去噪原理(2)。保持原P，最低已足，拟已关闭/仅报告Books新写0；不是EX或新实验已吸收的NC，无PRE/POST需求。若非准备者认为本文新增强命题确实达到5+，应仅重开该去噪/归一条件的必要受限审阅，不扩全图/版本/代码。待root非准备者实际原证与评分裁决，不授正式状态或DAY。
