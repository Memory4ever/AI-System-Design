# TEAM08404：必要Source与唯一owner PRE请求

TEAM: Temporal-Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration，2602.08404v1。2+2+2=6；完整AB与Feb10北京日上下界已root逐项通过。必要原件 `supplement-20261008-team-core.json` [0].data.sections：完整S3(14709char)与S4(9533char)，truncated=false，作者实际完整读。官方HTML275行没有Appendix，不另造附件待办；未运行artifact或复现。

S3.1/3.4：per-token nominal top8不等block-forward expert union，更不等每个accepted输出token的摊销。三类token：accepted后再过一次forward才缓存且不refresh；hot按高confidence/decoded位置近邻，四候选branches并行decode+verify（具体acceptance/verifier recipe未披露，不能授exact distribution）；新accepted/hot首先在全128专家中route，union为EA，cold只在EA中route。后者改变cold原top-k/weight并非精确复用。Eq4 forall j近邻与正文“close to decoded”歧义隔离，不写可执行判据；EA空集合fallback未给，不授完整安全算法。单GSM轨迹/代表layer相似性不证明全模型因果或双向KV必不drift。

S4 SDAR30B-A3B/singleA10080GB/官方baseline协议，block32、unmask.95、hot.7/距离3、branches4。LLaDA2无官方HF pipeline未成为主要验证平台；precision、I/O长度、batch/concurrency/SLO、repeat/CI未披露。T1平均APF54.99→34.48/TPF3.14→5/APT17.66→6.92，APT是expert-union除accepted tokens，非每token实际routing8变6.92或FLOPs。Human79.27→79.88/speed2.20，MBPP65.76相同/2.08，GSM90.6→90.3/1.83，Math76→75.4/1.64，avg77.91→77.84/1.94，不能称严格同质量或生产系统2.2×。

T2 refresh-free avg77.57<refresh4的77.84，MBPP65.76<66.15、GSM90.45<refresh8的90.6、Math74.2<refresh4的74.8；不授无refresh普遍质量保持。T3阈值与距离同时变，不能分离单一阈值因果；.8/2 Human77.44/MBPP62.65低.7/3的79.27/66.93；.6/4 avg73.68高default73.10，default非所有质量最优。仅联合预算取舍，支持已足不展开全proof或修算法。

实际MODEL-MOE Ch21 98–119（per-token active vswhole compute）、849–877（batch expert union/sharing）、565–579（masked diffusion expert-choice容量）与Ch20/22入口已读。既有batch共享以gatingmass/请求相关性压union，既有denoise容量按maskratio重分配，均没有token acceptance population×重复迭代、先new/hot后cold的双轮受限集合。具体差额可落唯一Ch21 batch-sharing段后/phase-specific expert前（当前source-family07265后）；不再Ch24复制缓存机制。正文只把延后缓存作为冷/热union为何变化的必要背景，generation/cache一般权限仍由Ch24承接。

拟一段最小正文（待root必要Source/PRE与写锁）：共享集合还要与“这一轮究竟提交了哪些输出”一起测量。块扩散每轮处理许多位置，却可能只接受少数token；每个位置各取少量expert，整轮并集与每个已提交token摊销的weight activation仍可能很大。一条受限分支先让新接受位置及可能近期提交的hot位置选择完整experts，再把剩余cold位置的路由限制到该并集；accepted位置延后一次前向才缓存，hot候选探索则用额外计算尝试提高每轮提交数。此时expert并集、accepted token数与真实质量/时延必须分账：cold路由已被近似改变，缓存稳定和hot判定不是正确性概率，额外候选也不等于分布精确的speculation。有限单GPU块扩散模型对照存在数学任务退步，无刷新并非所有任务质量保持；分类、分支验证、缓存状态与路由预算应随版本验收，质量或净成本退化时回退完整路由、受控刷新或原生成路径，不由摊销expert指标授端到端SLO保证。

请求root实读必要S3/S4与上述owner邻接，决定受限整合或更窄处置；当前未写Ch21，未获整日DAY。
