# 10584 Marigold-SSD：实际增量最低关闭提案（待非作者）

只03-13补Mar12自然日。第三完整exact-v1准入及DATE3日级夹证有效复用；直接重对题名/六作者/完整AB/history，v1 SubmittedMar11T09:40:03Z/registeredMar12T02:05:05Z，无当前可见withdraw/correction/具名venue。May2v2不因号码触发比较。官方 https://arxiv.org/html/2603.10584v1 GET200/370006bytes/UTC2026-10-10T01:36:21.120574Z，SUP_CORE_10584.raw/txt与manifest/result保存。

## 评分对象与具体关闭

先前窄准入“single-step/late-fusion与sparsity对照改变推理取舍”保留，不按3D标签排除、不追求固定保留率。直接决定核心后，新增是**已有Marigold-E2E单步近似上增条件decoder、不同稀疏密度训练范围和late/early局部比较**，不是新扩散路径、single-step发明或稀疏sensor真值资格。§3.2明确修scheduler/单步蒸馏来自前作；ControlNet式条件初始化/conv和已知L1/尺度拟合不另计贡献。

拟 **Design1+Reach1+Durability2=4**，最低关闭、不进一步采用Books0。1：局部条件decoder实现/训练配方，single-step来自已有基线；1：只depth-completion模型与其RGB/sparse条件负载，没有新增训练runtime/物理执行跨界机制；2：相同DDAD常用较密输入下简单interpolation已可更好、低密度才更依赖模型的具体新比较，限定评价人口与prior费用解释可复用，但不抬为普遍新理论。只按新增命题给分，不借diffusion prior、ControlNet、零shot名字/4.5GPUdays和一般input-coverage原则抬分。该局部配方不进一步采用，不称EX/现章节已吸收新实验；不是因为缺代码/全部图或工作量降分。

## 实际最低必要证据

直接§3.1–3.2完整（605–1189），implementation/setup训练有关段（1547–1616），Table1全部及稀疏/训练数据有关头部（1180–1350），Table2全部（1450–1546），§4.2–4.5全部（2178–2312）、Table3实际caption/人口+ensemble/DC/两SSD行（1617–1769、2000–2177），Table4全部及§5限制/直接密度反侧（2313–2557）。没有重建Table3每一外部模型/整数据附录/图pixels/代码，源足支持最低关闭而非完整标准Source。未看图的精确密度曲线不采用。

机制actual：fixed t=T/zero xT→Marigold-E2E UNet输出depth latent，frozen VAE encoder保留，UNet与五scale条件decoder一起task L1 fine-tune，sparse C最后进入decoder；metric depth还用valid sparse C*拟合全局a,b，不是RGB生成的relative depth自动metric真值。原文concat后1x1“zero conv preserves behavior”未说明原feature passthrough/identity权重块，不补造精确code或宣布现实现必错；不采用bitwise初始化保持承诺。稀疏train density是条件人口而非true zero-shot无训练：Hypersim/VirtualKITTI9:1、20ksteps/gradacc32×1、decoder LR3e−5/UNet3e−6、warmup100，一H100每模型4.5天，两个density range .16–5%与.16–.5%。真值或scene深度不在稀疏C的range会失准；天空bias作者明确承认，不能批准机器人碰撞/安全。

Table1 RTX4090 SSD .38/.53/.45秒、平均.42/2.4FPS，DC无ensemble约27.49秒；66×是作者这份compare，660×是按10sample近线性推算，不是实际所有配置端到端measurement。Table2部分外部runtime/性能来自他文，不能全部同平台budget归因；模型预训练、E2E基线训练和每模型4.5day也非完整新系统生产成本。Precision/batch/concurrency/tail SLO与实机闭环 Not Disclosed，不借仅2.4FPS批准实时任务。

Table3 ensembleDC avgRMSE1.469更好SSD1.500而avgMAE.510较差.474，VOID SSD.182/.590较DC.157/.557差；原窄density SSD⋆ KITTI2.443/4.070、DDAD3.870/7.841弱于wide .454/1.496与2.066/6.524，源直接承认窄密度域外退步。六domain米制算术平均不是统一dataset人口的全局RMSE。Table4wide early frozen-VAE+interpolation IBims.054/.175较SSD.060/.185更好、ScanNet.024/.070与SSD.027/.068有取舍，不能late总优；early frozen与conditional的trainable参数、输入precomplete及LR也不同，不唯一归因fusion时刻。

最具体新评价反侧：§4.4/5报告DDAD常用5000points时simple barycentric可超过较复杂方法；§5给MAE1.598/RMSE6.831，对SSD2.066/6.524是MAE胜/RMSE负而非每metric都胜。低密度500/1500优势只原文有限负载观察，本次未读figurepixels不签精数/普遍threshold。它改变“常用密度分数证明大prior有净价值”的局部判断，保留可复核数据身份，不推广为所有稀疏观测无需模型。

## 精确停点

最低4分/已关闭不进一步采用Books0提案ready待root非准备者实际决定core/关键反侧复核，不先formal。ROADMAP表示/感知责任可路由MULTIMODAL-REPRESENTATION，Ch26只动作消费、Ch24只生成prior来源；本项不写新owner、也不泛说已有覆盖。无PRE/POST需要，材料没有必要外部缺失。未来新通用机制/匹配预算或重要修订才定点重开，不授DAY。

## 后续非作者裁决（覆盖上述准备停点）

root已实际必要§3.1–3.2/§4.2–4.5和主表直接反侧复核，主SUP_INDEPENDENT_REVIEW_20261009.md的10584节支持1+1+2=4、已关闭/仅报告/不进一步采用Books0，PASS。正式第33项；不改准入、不称新实验已吸收、不授通用实时/所有指标普胜，未写Books、无PRE/POST需求。DAY仍未通过。
