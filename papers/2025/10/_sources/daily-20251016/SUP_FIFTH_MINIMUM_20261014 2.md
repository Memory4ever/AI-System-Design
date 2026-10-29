# Oct16第五批最低决定域准备包

最新root独核§13已实际完整核24 AB/八最低/两必要强命题局部，17P7C/noN通过；本文原“待独核”提案阶段被此实际结果覆盖。必要bound/真实gap、近邻/分类/provenance分母限制保持，不重第三审/全P methods，未授日证或采用。

作者Kierkegaard，2026-10-14T13:58+08:00。只本日已识别八N最低决定事实；以下为作者提案，待root实际独核，不授日期/评分/正式候选/完整Evidence/Books。原件均精确v1，实际读取必要节点而非下载即读；不扩其余P全文。

## 已准备六项

| 身份与实际读取范围 | 最低决定与提案 | 必要反侧/不采用 |
| --- | --- | --- |
| [2510.12224 MedKGEval](SUP_CORE_12224_V1.raw)：S4含Table2、5.3/Table6/7、S7 | N→窄P，仅KG Director控制可披露事实、Patient未知事实生成补位、Judge消费KG oracle的信息人口条件。相同DeepSeek doctor有/无Director的entity alignment和评分同时改变，评价并非只由doctor固有能力决定；可改变Agent模拟评价的信息暴露与判分分责。 | Table6 alignment91.4/95.26 vs63.4/59.6、Table7 correctness48.88vs37.62/HT68.94vs33.42是该模拟人口，不授独立人truth、临床安全或四Agent本身新机制。Director改变信息供给，不能单归因doctor能力。 |
| [2510.12428 BiasedAttention](SUP_CORE_12428_V1.raw)：III-C/D、IV-D/TableIII、IV-E | N→窄P仅风险预测/奖励消费资格与实际collision反侧：balanced两类episode标签训练的risk score不是自然策略下校准概率；风险模块无bias虽改善队列/等待，collision CT却.076劣于无risk .068。 | B_ij=beta(j-(N-1))是静态key列recency，值非正但文称positive additive，不静默修正。full .061是另训练policy/三seed/1000simsteps，不证同固定controller因果；一个手工状态score更敏感不等风险更正确，不采safe/普遍效率。 |
| [2510.12477 HRC](SUP_CORE_12477_V1.raw)：III-A/B/C与IV-D比较域；压缩恢复后补读完整III-B/Algo2 | N→窄P仅连续目标位置→最近剩余task映射保持action维数、低层re-RRT*真实success/replan反馈决定task提交与reward的接口条件。不同task总数不必重建离散action维数；抽象10×10×3观察不等精确geometry。 | re-RRT*检未来waypoint、goal占用失败/FCL检查与RL规划分责，20次比较都用同guard，不授真实人安全/通用VLA。replan count/文称time口径不合并；频率改变length/failure有成本，无同预算全因果控制。 |
| [2510.12750 VQArt](SUP_CORE_12750_V1.raw)：3.1/3.3/3.4、4.1与完整Table1/2 | N→窄P仅question/distractor人口决定cross-dimension测量：原文明确count题有更多plausible distractors，故计数低于高层reasoning不能直接解释能力层次；construction/validation资格而非新增艺术数据集准入。 | 七维借用既有SEED维度；25%随机人审98%不授全14463题无幻觉/全标签真。Table2各model维度与overall不同对象，InstructBLIP count .10与overall .24不外推所有模型或因果；metadata参与grounding不等纯视觉oracle。 |
| [2510.13978 InstantGaussian](SUP_CORE_13978_V1.raw)：完整S2 | N→窄P仅动态位置改变使原static GPU排序缓存失效、mesh/bone相对坐标预计算→每frame更新splat并以bone groups降低重新排序费的renderer消费边界。不是avatar领域名或fps本身准入。 | bone-group排序是质量/移动端预算取舍，不授exact全局深度序/无损；Scaniverse扫描和重建排除于30s，40–50fps/iPhone13Pro与RTX capped240非等配置比较，无受控quality/latency表或通用新训练机制。 |
| [2510.12308 HybridGaussian](SUP_CORE_12308_V1.raw)：完整3.1/3.2/4含Fig3/Table1 | N→窄P仅训练视图与外推视图收益分责、corrupted/clean跨traversal人口与动态物体mask资格的测量反侧。COLMAP约30K→180K→5.6M点主要持续改善source；target score .319→.343→.346接近饱和，不能以训练重建收益代表novel-view有效。 | masked loss总score仍.462、SSIM .522→.523/LPIPS .229→.230，不能统一全优；pseudo-view iterative refinement视觉似好却quant未反映并被最终提交排除。参考按camera距离取、source/target不同动态对象需mask；完全不同trajectory仍失败，额外重建/40K enhancer训练/高res费用不零。不把SD-Turbo+3DGS组合名称或challenge排行当贡献。 |

## 后两最低与必要强命题局部

| 身份与实际范围 | 作者提案与实际依据 | 不能采用的主张 |
| --- | --- | --- |
| [2511.07421 A3GNN](SUP_CORE_251107421_V1.raw)：完整III-A/B/C及IV-C含Algo2/3、TableIII | N→窄P：cached-node加权reservoir直接改变training sample人口，sequential/并行sampler+batch/仅并行sampler三模式使batch复制与GPU context开销不同，超出一般pipeline名称；固定40MB cache/简单sequential消融显示throughput与accuracy取舍。 | gamma=1回随机、cache bias增大约1%accuracy损失，partition远端信息不可访问也是精度因素，不无损；f1–f5只是建模函数，PPO以surrogate预测约束不是真实硬件feasibility保证。部分对照由旧论文估计、默认配置不等完整可比，R2 .7303–.8841不授精确性能/全局Pareto；搜索/性能标签采集有费。 |
| [2510.12325 CaMRec](SUP_CORE_12325_V1.raw)：完整3.2/3.3/4.1/4.2/5.2含Table2 | N→具体C提案：已知conditional diffusion恢复feature→VQ codebook分层→MLP edge mask/InfoNCE组合，本文所示推荐指标/移除模块消融未建立新识别条件或可迁移测量失败证据；不能凭back/front-door命名把成熟组合授因果新机制。 | C与G独立/简化sole parent为作者假设，cross-modal恢复共有feature不证明是latent confounder；front-door代理的截断/无混杂条件未由数据检验。Table2每消融同时改变组件/参数，不独立证truecausal identification。He/Hc/e/c记号与Figurexx/AppendixG引用未补实现，不以这些排版问题单独C。若原证给可识别假设/新adjustment算子或匹配反证，只重此身份。 |
| [2510.12939 pruning](SUP_CORE_12939_V1.raw)：完整3.1/3.2、4.1/4.3/4.5及B.1 effect-of-pruning节点 | 保P，仅pure elementwise mask使Frobenius/row-column surrogate norm非增与clean/attack/pruning三项界分责；必要强理论采用仍隔离。 | 固定正定Gaussian covariance或categorical/Lipschitz/bounded reward/perturbationball是条件。两个upper bounds大小关系不能推出实际gap非增/收益必升；训练gradient可增范数，非全程monotone，strict decrease也非任意mask保证。B.1声称local bound always不大于global含二阶项而条件未闭合，不采该普遍句；“Sec5/Thm1”指向口径不修。五seed/三MuJoCo/四攻击只限定人口，walker2d>50%崩、value-guided较弱，未授real安全/全部证明或复现。 |
| [2510.17854 EmbedAIDetect](SUP_CORE_17854_V1.raw)：完整II-B、III-A/B/D含TableI/II/III/V与外部confusion数字 | 摘要阶段C→窄P修正提案，仅评价盲区：原图扰动近邻回原图的accuracy与真假来源分类不是同一分母，内部SD3.5 vs art近99%不可投外部生成器/脸；CIFAKE real6194/fake4792各10000，faces fake仅236/10000，与近邻“robust”明确不同。 | immutable embedding hash只证预注册记录匹配，不证原生成来源/上传者真实；partial chain注册失败与classifier假阴性不同。Hybrid自己说no newclassification/no separateeval，不能授安全/可靠auth。新P不是blockchain+vector成熟组合或模型排名，是有原外部反证的measurement consumer范围；未核原所有代码/gas/攻击。不执行图片检测。 |

本批24作者修订提案为17P7C/noN（八N→7P1C、17854C→测量窄P），仍待root独立校准，不改旧有效组/原候选。SIDE12245最低与14058必要measurement另包，日期出口/Source终表/six普通；没有全P methods要求。
