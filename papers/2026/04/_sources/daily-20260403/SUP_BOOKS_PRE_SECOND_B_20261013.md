# 第二批后四项唯一owner差额、完整锚与逐字PRE

## actual PRE / nonwriter POST

root实际owner完整邻接与逐字PRE通过后授四项窄锁；作者已按下列PRE正文及本人静态注写入并顺读完整局部。root实际nonwriter POST核Ch49 1489～1507/2394（00821）、Ch66 4225～4243/4845（00208）、Ch72 2229～2253/2525～2544/3356/3358（ball/latentbackdoor），PRE与原证限制吻合，旧段完整、无末注后追加机制。四项窄锁全部释放。此实际单篇层不授全日完成。

四篇必要Source root已实际核过；本packet只申请窄ownership，不授锁。当前Books上下文完整读，下面实际owner/完整邻接及相邻章节开篇已读，不改其它family。

## 00821 / INFER-TENSORRT-LLM / Ch49

文件`books/part-05-inference-system/49-tensorrt-llm.md`。实际1475–1505及Ch48/50开篇：现有activation-whitened SVD与原块保留，缺输出loss-gradient统计同时进入rank目标的两侧近似，不重复静态rank/运行时router。完整锚以“分层预算需要记录原块/近似块的切分”开始至“统一 rank 或原始 dense matmul 仍更简单。”完整段后，下一“单一 SVD 子空间便于固定 rank 和执行布局”前。拟两段：

输入 activation 的 whitening 优化的是指定输入分布上的重构，未必保留任务 loss 对不同输出方向的敏感度。另一条条件分支同时收集输入二阶统计与输出 loss-gradient 二阶统计，在局部二次目标中以两个正定因子对权重做双向 whitening，再对变换后的矩阵截断 SVD、映回原坐标。输入侧回答误差在什么输入上出现，输出侧回答哪类误差在该校准目标下更敏感；两者不能互换，也不能把每个输出方向等权的重构目标直接称为任务最优。

这里的闭式低秩解只对所选 surrogate 成立：忽略一阶项、以 empirical Fisher 和 K-FAC 独立近似替代完整曲率，再用 damping 保持可分解矩阵；一般 empirical Fisher 不等于 Hessian，更不保证全模型任务 loss 最优。[有限压缩对照](https://arxiv.org/html/2604.00821v1)中，双侧优于所列单侧不代表输出侧独自更好，输出-only 表行反而明显差于输入-only。校准/backward、damping、分解与质量验收都有成本，artifact 应绑定两统计、目标、rank 与数值条件；统计漂移、近似不稳或没有有效低秩执行路径时，保留输入重构、较高 rank 和原 dense 权重，不由离线 loss-aware 标签批准运行时替换。<!-- source-family:SF-2026-ARXIV-2604-00821 -->

本人注：v1§3～4/Eq3～17/§5/Tables3～6，2+1+2=5、具体近似资格深入；C4 128×2048、10%平均diag damping、Llama2/3局部；Table5 output-only Avg39.56<input52.69<double54.23，邻文相反描述不采，未核实现/复现。

## 00208 / PLATFORM-EVALUATION-SYSTEM / Ch66

文件`books/part-06-ai-infrastructure/66-evaluation-system.md`。实际4210–4260及Ch65/67交接；现activation audit消template/mean并分probe与intervention，却没说明**相同latent feature的不同superposition geometry会反转alignment排序**。完整锚为“表征审计必须先消除模板混淆，再谈因果”下完整段及`<!-- source-family:SF-2026-ARXIV-2605-24583 -->`后、下一`### Explainability 的 Release Claim 存在不可兼得边界`前。拟两段：

模板和均值相同后，表示相似度仍会混入编码几何。若 latent features 被线性混入较少神经元，RSA、linear CKA 或回归分数同时依赖 feature overlap 与混合矩阵的 Gram 结构；跨不同压缩维度比较时，拥有更多共同 features 的一对表示也可能得分更低。这个反侧不意味着分数毫无价值：固定压缩维度的受限构造仍保留 overlap 的单调关系。评价应分别声明比较的 feature 内容、编码宽度与混合几何，而不是把一个 raw alignment 排名直接解释成知识或能力相似程度。

[受限 superposition 理论与合成验证](https://arxiv.org/html/2604.00208v1)假定独立、零均值且 identity covariance 的 latent features 及独立随机 projection；ratio-of-expectations 还需 concentration/渐近资格，不能推广为任意有限 LLM 的精确期望。低 alignment 也不自动表示信息已丢失，recoverability 另需稀疏性、足够维度与 RIP 等条件。控制几何、提取 features 和独立任务干预会增加费用；实际模型不满足这些条件时，保留 raw score 的描述角色与 matched-width/任务对照，不由低分否认信息存在，也不由可恢复性替代当前路径的行为验收。<!-- source-family:SF-2026-ARXIV-2604-00208 -->

本人注：v1§2～5必要Gram、fixedm overlap与compression排序反侧，3+1+3=7；synthetic1000features/8192samples、zeroMean/iid/identityCov与RIP资格；未授实际LLM causal feature或复现。

## 00770 / PLATFORM-SECURITY / Ch72

文件`books/part-06-ai-infrastructure/72-security.md`。实际2510–2558及58–100、Ch71/73开篇；现白盒trajectory sensor/漂移与artifact provenance已有，但未拆**latent trigger的可见token检查与oracle-labeled hidden probe资格**。完整锚`<!-- source-family:SF-2026-ARXIV-2604-28129 -->`后、下一“安全 probe 还要区分危险能力是否存在与具体 policy boundary 是否已经被跨越。”前。拟两段：

隐式多步 reasoning 还可能把触发藏在正常 token 的 embedding lookup 中：具有训练写权限的攻击者联合优化模型权重与触发向量，再把向量写入词表行，使普通 lexical token 进入 latent 多步轨迹后才产生目标行为。这里需要受污染的训练 artifact，不是任意部署用户靠一次向量扰动就能改写模型；没有显式中间文字也不意味着 embedding 行或 hidden trajectory 原理上不可检查。[受限 latent-backdoor 对照](https://arxiv.org/html/2604.00770v1)中，若干 token-based 防御失效仍不排除 reference embedding-row drift 检查及合适的行为诊断。

诊断必须保留 observer 权限与标签来源：没有 trigger knowledge 的 centroid/聚类失败，不能由已知 clean/trigger 标签训练的高 AUC probe 补签为部署 sensor。其线性读出命题只保证给定成功/干净行为条件下至少存在一对可线性区分的 latent，不保证整个新人口都可分；强 clean fine-tuning 也能削弱所测后门，持久性并非无条件。训练、reference 对照、hidden 采集、标注与独立 clean-utility/攻击评测都计费；访问、参考或校准不足时，保留 Unknown、artifact 隔离、可信 checkpoint 与最终 output/effect gate，不由未检出或 oracle probe 的分数放行。<!-- source-family:SF-2026-ARXIV-2604-00770 -->

本人注：v1§4～6/必要A4,D20，3+2+2=7；joint全部weight+embedding、Prop1existential、5active非all、oracle label不部署、lr1e−4/wd.1可擦反侧；Coconut/SimCoT124M～3B有限，无实现复现。

## 00072 / PLATFORM-SECURITY / Ch72

同文件另一不冲突段。实际2216–2244及Ch71/73交接；现输入邻域证书/CAGE拥有typed-return授权，但没有**参数更新ball复用→重新中心认证**责任，不从action ball类比填充。完整锚“证书强度受完整 mediation、type constructor、邻域可枚举性和预算校准限制；预算外输入、跨动作累计风险与错误 safety map 仍需要传统隔离、审批和补偿。确定性规则能完整覆盖时，普通 policy-as-code 更简单，也更容易解释。”后，下一`#### Proof of Equation Satisfaction 不等于 Proof of Expended Work`前。拟两段：

若被检验对象是模型参数更新，而不是一次 action 输入，安全域可以采用另一种复用方式：先在当前参考参数上取得指定 evaluation domain 的安全 margin，并确认该域内相应 Lipschitz 上界，再以 margin/上界定义允许更新的球。球内 proposal 只需便宜的范数检查；想把中心移到新参数、继续沿下一球训练，就须重新核对 oracle、margin 与上界，不能由连续小步推导无限安全演化。这里认证的是所声明的参数邻域和条件，不替代完整输入/行为与 effect-time 授权。

[受限理论与 LLM 实验](https://arxiv.org/html/2604.00072v1)应分开读：分类器下的结论带分布与误差衰减假设，而 LLM 分支使用有限 prompt oracle、finite-difference Lipschitz 估计和放大因子，并非 analytic 上界认证。扩大 oracle 后发现新的 violations，chaining 也有 false accepts 和终点安全退步，故不能承诺一般模型零风险或 classifier 本质不可能。Margin/oracle 调用、上界校准与换中心重验都计费；域、oracle 或上界资格不足时，缩小更新、保留参考 checkpoint 与独立安全测试，不能让便宜 normcheck 自授安全事实。<!-- source-family:SF-2026-ARXIV-2604-00072 -->

本人注：v1§2/4.4～4.6/5/6.3/必要B1～B2/A12，6分安全深入；r=m/L前提，Qwen2.5-7Bq/vLoRA4NF4/BF16/200steps，expandedoracle20新增violations、Safe-at-end No(.98)/五seed一项6FA，未授formalLLM或复现。
