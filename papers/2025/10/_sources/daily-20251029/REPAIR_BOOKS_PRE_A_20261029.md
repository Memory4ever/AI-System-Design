# Books整体PRE A · writer完整稿

本稿为R26三处修正后的完整版本，仅请求以下精确新增段/独立marker/本人Review note；同锚点按本稿顺序插入，彼此亦为后到邻接。尚未SAVE，不申请全章ownership；现有并发dirty/staged保护，精确gap变化先核是否冲突。每段采用精确v1和已读必要证据，支持/直接反侧足停；原文性能数字不进入长期正文。自读包括完整新文/marker/本人注及完整必要邻接，未授POST。

## 22026

文件：`books/part-02-model/17-transformer-layer.md`

插入于唯一锚点前：`## 一次完整 shape 流`

### 完整新增正文

Norm位置还会改变前向表示运动的速度，而不只改变反传路径。把非零token写成半径r与单位方向theta，连续深度下方向导数是原更新在球面切空间的投影再除以r；归一化放在读取前、相加后或更新支路内，便可能产生不同的token依赖速度，而非把同一条轨迹统一加快或减慢。[受限attention-only分析](https://arxiv.org/html/2510.22026v1)由此比较Pre/Post/Peri-Norm的聚类动态，但其tied或identity矩阵、随机初始化与终端窄cone等假设不能迁给有FFN的训练后decoder；局部多项式/指数速率也不是训练梯度或任务质量排名。半径增长会改变有效更新，应与角向变化分开诊断，仍支付完整训练与有限深度回归；模型或假设不合时保留已验Norm/residual配方，不从球面解释推出Peri普遍最佳或checkpoint可互换。
<!-- source-family:SF-2025-ARXIV-2510-22026 -->

### 本人注

- `SF-2025-ARXIV-2510-22026` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22026v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。完整新论点为径向/角向及token依赖速度，不重复既有Jacobian或随机共享噪声；不照录受限速率为通用优化定理。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

完整新论点为径向/角向及token依赖速度，不重复既有Jacobian或随机共享噪声；不照录受限速率为通用优化定理。

### 当前完整必要邻接

```markdown
Pre-Norm 并非无条件优于 Post-Norm。两者的表达、训练动态、初始化和最终性能要在具体架构中比较。稳定结论是：Norm 放置改变了梯度路径，不能在加载 checkpoint 时任意互换。

前向尺度与反向传播还可以采用不同的局部规则，而不只是给 residual 乘一个普通系数。一条[受限训练分支](https://arxiv.org/html/2506.22049v1)从子层相加后的状态中减去带 stop-gradient 的门控副本：前向改变该状态的尺度，反传到这份状态的局部 Jacobian 却保留 identity，门参数仍按自己的路径学习。这改变了 block 的训练合同，不等于原网络的全部梯度或优化轨迹保持不变；初始门为零时的首轮相同，也不保证之后等价。门可放大而非始终压低 activation，数值域、归一化的 epsilon、反向路径和 checkpoint 中的门/optimizer 状态必须共同定义实现，不能从尺度较小推信息无损或稳定证明。局部对照中固定门、替代插入位置与部分下游任务反而更差，门更新还可能产生梯度尖峰；简化理论中的上界也不能证明实际梯度永不消失或爆炸。额外逐层算子、门训练、监控/裁剪和达到同质量目标的完整训练均计费，较少 steps 不自动等于较低墙钟费用。质量、门域、数值稳定或净预算不成立时，保留原 Pre-Norm、已验初始化/学习率与普通梯度监控，而不是给现成 checkpoint 任意加尺度门。<!-- source-family:SF-2025-ARXIV-2506-22049 -->

## 一次完整 shape 流

假设：

```text
B = 2
T = 4
d_model = 8
H = 2
d_h = 4
d_ff = 32
```

Pre-Norm layer 的逻辑 shape：

```text
X                         [2,4,8]
Norm(X)                   [2,4,8]
Q/K/V reshape             [2,2,4,4]
Attention scores          [2,2,4,4]
Head outputs              [2,2,4,4]
Concat + output projection[2,4,8]
U = X + attention_output  [2,4,8]
Norm(U)                   [2,4,8]
MLP up / gate             [2,4,32]
MLP down                  [2,4,8]
Y = U + mlp_output        [2,4,8]
```
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19491` — Jun20补Jun19；writer首次exact-v1§2–5/A1.1–2/A1.6必要，2+2+2=6，仅Prop2独立有效代数与centered/Gram诊断差额深入，actualCh17 Norm完整两肩/Ch16–18交接已读。保非零γ/β/epsilon/人口与精度地板；不采中心Schur ratio0/0→1/训练更深核、无条件residual界、Fisher/rate或功能缺陷，中心H与重开留本日A15。未核artifact/复现；完整PRE已过，SAVE后selfread/actualPOST只本日实际层，不以本注预签。

- `SF-2026-ARXIV-2606-18246` — Daily06-18补Jun17，2+2+2=6，作者首次必要完整v1§2–3/4.4T4/5/AppA；仅active坐标/最近恢复与bulk参数、cache及完整执行成本分账。保round/endpoint/MoEactive差、任务/投影反退、global残差非均宽内存、fit非墙钟及全费；未采4.1–4.3因果解释/完整scaling定律，未核代码/复现。root唯一REVIEW§47整体PRE通过，按批准稿实际保存，作者完整自读；actualPOST仅后到唯一非writer记录，不预签。
```

## 21956

文件：`books/part-02-model/22-long-context.md`

插入于唯一锚点前：`### SSM：把累加器推广为有动态的状态`

### 完整新增正文

有限核状态的长度线性还须兑现到训练IO。对可分离的因果核，前向可累积prefix状态，反向则从末端累积suffix贡献，按需重算而不让通用autograd保存每个位置的完整外积；这是同一受限算子的物化选择，不是把softmax精确改成线性。[一项CUDA前后向重排](https://arxiv.org/html/2510.21956v1)使用单位化Q/K与1+qk核，支持比较状态驻留、重算和线程数据复用；仍有维度、输入/输出与投影费用，论文求和索引的表面不一致也不能代实现等价证明。相同步数收敛较慢而墙钟较快是两种结果，不能把A6000/FP32的局部倍率借给所有精度和服务。应分别验算子数值、同质量训练时间与真实内存，维度、质量或kernel支持不合时保普通显式Attention、成熟线性核或hybrid，而非只按O(L)选型。
<!-- source-family:SF-2025-ARXIV-2510-21956 -->

### 本人注

- `SF-2025-ARXIV-2510-21956` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.21956v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增为线性核prefix/suffix的训练图物化接口；前面的S/z公式和后面的SSM仍各自完整，明确不是softmax无损替换。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增为线性核prefix/suffix的训练图物化接口；前面的S/z公式和后面的SSM仍各自完整，明确不是softmax无损替换。

### 当前完整必要邻接

```markdown
固定状态也可以只接管远历史，而不是替换全部精细访问。视频的 chunk 内及相邻边界对运动连续性敏感，一条受限混合分支在局部和重叠区域保留 softmax，在更早历史用可学习 kernel summary，并对两部分共同归一化；重叠 token 必须从远历史集合排除，不能计算两次。因果边界按 chunk 而非每个空间 token 定义，所以 chunk 内双向访问不等于读取未来 chunk。这里购买的是不同距离的表示精度分配，不是原 softmax 的精确压缩。

已有双向 teacher 也不能直接换上因果 summary 就保持行为。可先固定原 block，只学习 query/key feature map 去匹配 teacher activation，再以全模型目标修复局部适配留下的跨 chunk 偏差；后一步增加训练费用，并让这条路径区别于单纯 runtime cache 优化。ReHyAt 的视频受限对照支持这一适配分支，但递归公式把全部远历史重复加入累计状态，字面上不足以证明与并行形式等价；也仍保留部分 full-attention block，不能据局部状态定长宣布全模型无限时长定内存。物理控制与人偏好并非全面改善，mobile block 时间也不等端到端生成 SLO。精确回读、适配质量或递归一致性不满足时，原 full attention、局部窗口及直接训练的 recurrent 路径继续共存。<!-- source-family:SF-2026-ARXIV-2601-04342 -->

### SSM：把累加器推广为有动态的状态

纯累加不区分新旧信息。结构化 State Space Model 为旧状态增加演化规则；以一个输入通道 u_t、N 维状态 h_t、零初态说明：

```text
h_t = A_bar h_(t-1) + B_bar u_t
y_t = C h_t
y_t = sum_(i=1..t) C A_bar^(t-i) B_bar u_i
```

当 A_bar、B_bar、C 跨位置不变时，展开式是只依赖距离的卷积：训练可并行计算整段，逐 token Decode 可用递推。这两种执行方式承载同一算子；实际模型通常约束 A 的结构，避免每步密集 N×N 状态转移。连续时间参数的离散化是构造 A_bar、B_bar 的一种方式，不是所有递推都必须采用的定义。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19849`，Jun20补Jun19；消费sole§110唯一exact-v1必要，2+2+2=6，actualCh22 ThinkStream完整两段/StreamingVLM完整前链与Anchor后肩、Ch42/56交接已读，仅vision持续写近窗-v-query旧archive双visibility差额深入。保选后有界非全hist、trainthreshold/runtime topk资格、ingestion-v-query TTFT起点/瓶颈迁移/反退及全费ND；未核实现/复现，不授无限记忆/实时SLO，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2025-ARXIV-2510-19315` — Volta，Daily2025-10-24补Oct23；exact-v1§3/4完整正文构造证明，readerR14 §2.2/2.5/5/6限制复用，2+1+3=6，表示简洁度/读取成本的具体gap深入。仅UHAT/B-RASP有限形式模型、随model poly且input固定精度/含RNN精度编码、最坏succinctness与nonemptiness；不采用current更强版本、全部附录证明认证、softmax训练或实机性能推断。未核代码/复现；PRE/SAVE/自读/sole实际POST只按本日canonical。
```

## 22109

文件：`books/part-02-model/22-long-context.md`

插入于唯一锚点前：`### SSM：把累加器推广为有动态的状态`

### 完整新增正文

有损时间分辨率也可以在进入第一层前分配，而不要求每层维护递推记忆：按embedding通道用一组因果、对数间隔的时间滤波器汇聚远历史，再与近期未压token拼接，交给原Transformer消费。[SITH的有限输入分支](https://arxiv.org/html/2510.22109v1)保留近细远粗的时间结构，但滤波槽不是原文token，无法承诺任意旧事实精确回读，也不是固定状态的免费在线更新。槽数、时间尺度、近期窗口、位置解释及仅近期计算loss的训练人口应共同绑定；小模型per-word PPL不能与不同分词的token PPL直接排序。滤波、历史输入访问与适配训练都计费，远程细节、未知查询或总成本不合时保完整/更大窗口与原文检索，不由对数槽数推出无限记忆。
<!-- source-family:SF-2025-ARXIV-2510-22109 -->

### 本人注

- `SF-2025-ARXIV-2510-22109` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22109v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。输入滤波与前段层内状态、后段SSM分开；不把近细远粗称逐字可逆或恒时，原窗口/检索继续成立。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

输入滤波与前段层内状态、后段SSM分开；不把近细远粗称逐字可逆或恒时，原窗口/检索继续成立。

### 当前完整必要邻接

```markdown
固定状态也可以只接管远历史，而不是替换全部精细访问。视频的 chunk 内及相邻边界对运动连续性敏感，一条受限混合分支在局部和重叠区域保留 softmax，在更早历史用可学习 kernel summary，并对两部分共同归一化；重叠 token 必须从远历史集合排除，不能计算两次。因果边界按 chunk 而非每个空间 token 定义，所以 chunk 内双向访问不等于读取未来 chunk。这里购买的是不同距离的表示精度分配，不是原 softmax 的精确压缩。

已有双向 teacher 也不能直接换上因果 summary 就保持行为。可先固定原 block，只学习 query/key feature map 去匹配 teacher activation，再以全模型目标修复局部适配留下的跨 chunk 偏差；后一步增加训练费用，并让这条路径区别于单纯 runtime cache 优化。ReHyAt 的视频受限对照支持这一适配分支，但递归公式把全部远历史重复加入累计状态，字面上不足以证明与并行形式等价；也仍保留部分 full-attention block，不能据局部状态定长宣布全模型无限时长定内存。物理控制与人偏好并非全面改善，mobile block 时间也不等端到端生成 SLO。精确回读、适配质量或递归一致性不满足时，原 full attention、局部窗口及直接训练的 recurrent 路径继续共存。<!-- source-family:SF-2026-ARXIV-2601-04342 -->

### SSM：把累加器推广为有动态的状态

纯累加不区分新旧信息。结构化 State Space Model 为旧状态增加演化规则；以一个输入通道 u_t、N 维状态 h_t、零初态说明：

```text
h_t = A_bar h_(t-1) + B_bar u_t
y_t = C h_t
y_t = sum_(i=1..t) C A_bar^(t-i) B_bar u_i
```

当 A_bar、B_bar、C 跨位置不变时，展开式是只依赖距离的卷积：训练可并行计算整段，逐 token Decode 可用递推。这两种执行方式承载同一算子；实际模型通常约束 A 的结构，避免每步密集 N×N 状态转移。连续时间参数的离散化是构造 A_bar、B_bar 的一种方式，不是所有递推都必须采用的定义。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19849`，Jun20补Jun19；消费sole§110唯一exact-v1必要，2+2+2=6，actualCh22 ThinkStream完整两段/StreamingVLM完整前链与Anchor后肩、Ch42/56交接已读，仅vision持续写近窗-v-query旧archive双visibility差额深入。保选后有界非全hist、trainthreshold/runtime topk资格、ingestion-v-query TTFT起点/瓶颈迁移/反退及全费ND；未核实现/复现，不授无限记忆/实时SLO，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2025-ARXIV-2510-19315` — Volta，Daily2025-10-24补Oct23；exact-v1§3/4完整正文构造证明，readerR14 §2.2/2.5/5/6限制复用，2+1+3=6，表示简洁度/读取成本的具体gap深入。仅UHAT/B-RASP有限形式模型、随model poly且input固定精度/含RNN精度编码、最坏succinctness与nonemptiness；不采用current更强版本、全部附录证明认证、softmax训练或实机性能推断。未核代码/复现；PRE/SAVE/自读/sole实际POST只按本日canonical。
```

## 21986

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`

插入于唯一锚点前：`## 一个统一的成本模型`

### 完整新增正文

同一个denoiser内部的token预算还可按深度分配：保留浅层和末层的dense空间路径，只让中层处理结构化稀疏子集，再把回填后的深层特征与浅层细节经残差/投影融合。[SPRINT的受限DiT分支](https://arxiv.org/html/2510.21986v1)以局部组内留点减少全局随机删选的空洞，并用短full-token阶段缓和训练/采样差异；它不是任意checkpoint直接删中层或无条件支路的资格。更高drop会退步，路径消融仅支持这套互补计算，不证浅层/深层唯一语义分工。稀疏选择、回填、融合、适配与完整采样均计费，FLOPs下降不自动成为墙钟倍率；细节、布局或质量回归时保dense网络、较低drop与原CFG路径，不能由中层token少批准无损或服务SLO。
<!-- source-family:SF-2025-ARXIV-2510-21986 -->

### 本人注

- `SF-2025-ARXIV-2510-21986` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.21986v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增层内深度预算及dense旁路交接，放成本模型前，不另写模型史；保训练适配/高drop反侧和计算量与墙钟分责。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增层内深度预算及dense旁路交接，放成本模型前，不另写模型史；保训练适配/高drop反侧和计算量与墙钟分责。

### 当前完整必要邻接

```markdown
```text
condition + target set
→ sample multiple candidate matches
→ score under frozen matching contract
→ select one training trajectory
→ update generator
```

这让 exploration 成为除模型规模和每样本计算之外的第三条训练计算轴，但没有创造更可靠的 ground truth。候选数增加
会线性或超线性放大生成与筛选成本，选择器偏差还会把某种 mode 固化成训练偏好。固定单匹配在数据近单峰、预算紧或
scorer 不可信时仍合理；多候选探索只在候选多样性、selection contract 和单位训练预算收益一起验证时成立。作者的
受限 scaling curve 不能证明它会普遍替代 AR、diffusion 或 masked generation，只说明 training-time sampling policy
本身也需要被版本化和计量。

## 一个统一的成本模型

端到端时间不能只数模型 forward 次数：

```text
T_total = T_queue
        + T_encode
        + T_proposal
        + T_verify_or_correct
        + T_state_management
        + T_decode_output
```

吞吐也不能只报告 tokens/s。对于 mutable generation，应同时报告：

- committed tokens/s，而非 provisional updates/s；
- quality 在同一 scorer 下是否等价；
- block/tree/correction 使用的额外 memory；
- batch、concurrency、length、precision、hardware；
- TTFT、inter-token latency 或最终 completion latency；
- rollback、cache compaction 和 scheduler overhead。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19894`，Jun20补Jun19；消费sole§120首次必要，writer定点§3/AppD与actualCh24 posteriormean/有限Gaussian/经验支集及分噪声记忆完整链，2+1+2=5，唯cover→oracle localmean-mixture表示-v-可学习性接口差额深入。保VE/t0/显式cover域、pt平均非逐点/clean密度、维度与全部费；独校φ e^-x调用negative logit只隔离打印softmax/精确rate，不授已反证存在性或已修构造。未核全B/C/实现复现，PRE/SAVE/selfread/actualPOST仅本日真实层。

- `SF-2026-ARXIV-2606-19876`，Jun20补Jun19；消费sole§111唯一exact-v1必要，2+1+2=5，actualCh24 noise-law/score完整两段与finiteGaussian/经验读取完整后链、Ch29目标交接已读，仅score积分人口/measuregradient及mean-v-modeweight差额深入。保固定GMM精确GD/初始化separation域、驻点/TV权重/有限数值与全费ND；未核全E/F或实现复现，不授任意神经SGD/一步全训/全密度，PRE/SAVE/selfread/actualPOST仅本日实际层。
```

## 22201

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`

插入于唯一锚点前：`从可采样条件目标代替不可得的边际目标时，还须说明等价保护了什么：`

### 完整新增正文

Guidance的参照也可以来自同一模型中被破坏的依赖，而非另训classifier：在action-token自注意力中临时屏蔽跨时间交互，取得较弱的速度场，再以(1+lambda)v-lambda*v_bad组合，引导原采样远离这份局部退化。[受限action-coherence分支](https://arxiv.org/html/2510.22201v1)改变的是采样提案；差分场不自动是精确density-ratio score，较平滑也不等物理可执行。坏支路构造、层位、强度与solver须共同保存，额外前向和缓存复用全部计费；有限机器人模拟/少量实机的jerk与成功应分报。生成分布、动作细节或时限不合时保原flow/较弱引导，真实动作仍由第26章的controller和safety envelope验收，不用采样一致性批准物理安全。
<!-- source-family:SF-2025-ARXIV-2510-22201 -->

### 本人注

- `SF-2025-ARXIV-2510-22201` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22201v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。只在生成owner解释参照场和费用，控制权明确交Ch26；不照录精确density比、平滑=安全或零费用。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

只在生成owner解释参照场和费用，控制权明确交Ch26；不照录精确density比、平滑=安全或零费用。

### 当前完整必要邻接

```markdown
```text
a_s = 1 - (1-sigma_min) s
X_s = a_s epsilon + s y
u_target = dX_s/ds = y - (1-sigma_min) epsilon
L_CFM = E ||v_theta(X_s,s,c) - u_target||^2
```

sigma_min>0 时终点仍含少量噪声；趋近零才得到常见的噪声—数据直线插值极限。训练知道 y 和 epsilon，所以目标可计算；部署只见当前 x、s 和条件 c。平方回归在给定当前状态后学习条件目标的平均速度，在论文的密度与正则条件下，这与匹配边际概率路径的目标有相同参数梯度，而不是要求模型复原每个训练配对。

从可采样条件目标代替不可得的边际目标时，还须说明等价保护了什么：若两个loss只差与模型参数无关的常数，它们可有相同训练梯度，却不因此证明有限模型、数值sampler或最终分布正确。对同一不随条件标签另变的被优化密度，可分Bregman目标也可满足这份条件一致性，不能仅凭它宣布KL唯一；在光滑、非退化的可分密度divergence等分析前提下，再要求密度divergence对可逆坐标重参数化不变，才得到[受限分析中的KL选择条件](https://arxiv.org/html/2606.17465v1#S3.SS3)。条件一致与坐标不变是两条不同要求，不应拿一个名称替代二者。本材料另把一般随机Markov kernel下的二次transport目标宣为等价，但其证明改用了确定可逆映射，条件期望不能直接穿过平方；此子主张暂缓，不作上述目标选择的推论。条件数据、密度/目标拟合、积分与独立终态检查均付费；实际support、坐标或数值条件不合时，保留原CFM平方回归、已验目标与solver，不由较低训练loss或低维例子批准通用等价和加速。<!-- source-family:SF-2026-ARXIV-2606-17465 -->

即使路径与单样本velocity标签不变，按clean endpoint重权训练也可能改变学到的速度场。若每个样本乘权w，给定当前插值状态后的平方回归最优值是`E[wΔ|Y]/E[w|Y]`，不再必为原来的`E[Δ|Y]`；权重与条件速度的相关性正是这份target位移。[受限决策加权分支](https://arxiv.org/html/2606.16790v1#S5.SS2)用固定reference decision对endpoint的损失敏感度提出权重，让生成器更关注下游consumer，却不是恢复原人口的importance correction，也不保证减少实际regret。拟合加权target与保持原目标间的tilt必须分账，正权floor不自动覆盖learned ODE经过的区域；reference、可微loss和路径/敏感度覆盖仍是条件。相同sampler和decoder也不会撤销训练目标变化，有限网络与一步积分更不继承精确终态保证。Reference求解、endpoint梯度、全部训练/调参、多scenario采样与下游solver均付费；权重、支持或独立分布/决策质量失配时，回普通FM、较弱重权与原consumer验证，不由原标签未改或局部加权loss更低批准无偏、无损和真实决策安全。

<!-- source-family:SF-2026-ARXIV-2606-16790 -->

把监督从velocity换成endpoint的likelihood后，还须重新检查训练目标是否识别了采样器真正需要的条件速度矩，不能把“几何上自然”当作等价证明。在一个[内禀平坦圆环的离散反例](https://arxiv.org/html/2610.31981v1#S3.SS1)中，两条相反路径在同一点相遇，正确平均速度为零；端点距离目标的全局最优预测却可位于另一侧，经log map解码得到非零速度。这不否定上面的欧氏平方回归，而是说明先求非线性端点中心再解码，不一定等于先求条件速度再平均；仅训练loss更低也不证明transport更正确。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19894`，Jun20补Jun19；消费sole§120首次必要，writer定点§3/AppD与actualCh24 posteriormean/有限Gaussian/经验支集及分噪声记忆完整链，2+1+2=5，唯cover→oracle localmean-mixture表示-v-可学习性接口差额深入。保VE/t0/显式cover域、pt平均非逐点/clean密度、维度与全部费；独校φ e^-x调用negative logit只隔离打印softmax/精确rate，不授已反证存在性或已修构造。未核全B/C/实现复现，PRE/SAVE/selfread/actualPOST仅本日真实层。

- `SF-2026-ARXIV-2606-19876`，Jun20补Jun19；消费sole§111唯一exact-v1必要，2+1+2=5，actualCh24 noise-law/score完整两段与finiteGaussian/经验读取完整后链、Ch29目标交接已读，仅score积分人口/measuregradient及mean-v-modeweight差额深入。保固定GMM精确GD/初始化separation域、驻点/TV权重/有限数值与全费ND；未核全E/F或实现复现，不授任意神经SGD/一步全训/全密度，PRE/SAVE/selfread/actualPOST仅本日实际层。
```

## 22969

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`

插入于唯一锚点前：`从可采样条件目标代替不可得的边际目标时，还须说明等价保护了什么：`

### 完整新增正文

条件化采样还可能受通信限制：各节点无法交换全部邻居轨迹时，可以只用一跳邻居的均值观测构造条件drift，再把它与完整条件drift的差异单独核算。[一项受限mean-field diffusion分析](https://arxiv.org/html/2510.22969v1)在邻轨迹spread、条件noise/classifier误差有界、同diffusion与密度/唯一解正则等条件下，把局部drift误差转为含初始分布项的生成终态KL上界；条件误差须直接核验，原文Lipschitz到输出界及常数口径不完全闭合，不照录为一般可执行误差公式。均值会丢掉异质性和相关性，界不因节点多就自动归零，端点可积性亦是条件。这提供通信压缩与采样偏差的比较接口，不保证任务全局收敛或真实系统QoS。全部消息、条件模型训练与采样均计费，长horizon、异质邻居或假设失配时保更丰富条件、较短规划与完整信息基线，不把无线模拟迁为LLM serving保证。
<!-- source-family:SF-2025-ARXIV-2510-22969 -->

### 本人注

- `SF-2025-ARXIV-2510-22969` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22969v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。仅采条件摘要误差进入生成终态KL的比较接口，保初始项、密度正则、可积性与原常数不闭合；不称完整路径测度KL，不授全局收敛或serving。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

仅采条件摘要误差进入生成终态KL的比较接口，保初始项、密度正则、可积性与原常数不闭合；不称完整路径测度KL，不授全局收敛或serving。

### 当前完整必要邻接

```markdown
```text
a_s = 1 - (1-sigma_min) s
X_s = a_s epsilon + s y
u_target = dX_s/ds = y - (1-sigma_min) epsilon
L_CFM = E ||v_theta(X_s,s,c) - u_target||^2
```

sigma_min>0 时终点仍含少量噪声；趋近零才得到常见的噪声—数据直线插值极限。训练知道 y 和 epsilon，所以目标可计算；部署只见当前 x、s 和条件 c。平方回归在给定当前状态后学习条件目标的平均速度，在论文的密度与正则条件下，这与匹配边际概率路径的目标有相同参数梯度，而不是要求模型复原每个训练配对。

从可采样条件目标代替不可得的边际目标时，还须说明等价保护了什么：若两个loss只差与模型参数无关的常数，它们可有相同训练梯度，却不因此证明有限模型、数值sampler或最终分布正确。对同一不随条件标签另变的被优化密度，可分Bregman目标也可满足这份条件一致性，不能仅凭它宣布KL唯一；在光滑、非退化的可分密度divergence等分析前提下，再要求密度divergence对可逆坐标重参数化不变，才得到[受限分析中的KL选择条件](https://arxiv.org/html/2606.17465v1#S3.SS3)。条件一致与坐标不变是两条不同要求，不应拿一个名称替代二者。本材料另把一般随机Markov kernel下的二次transport目标宣为等价，但其证明改用了确定可逆映射，条件期望不能直接穿过平方；此子主张暂缓，不作上述目标选择的推论。条件数据、密度/目标拟合、积分与独立终态检查均付费；实际support、坐标或数值条件不合时，保留原CFM平方回归、已验目标与solver，不由较低训练loss或低维例子批准通用等价和加速。<!-- source-family:SF-2026-ARXIV-2606-17465 -->

即使路径与单样本velocity标签不变，按clean endpoint重权训练也可能改变学到的速度场。若每个样本乘权w，给定当前插值状态后的平方回归最优值是`E[wΔ|Y]/E[w|Y]`，不再必为原来的`E[Δ|Y]`；权重与条件速度的相关性正是这份target位移。[受限决策加权分支](https://arxiv.org/html/2606.16790v1#S5.SS2)用固定reference decision对endpoint的损失敏感度提出权重，让生成器更关注下游consumer，却不是恢复原人口的importance correction，也不保证减少实际regret。拟合加权target与保持原目标间的tilt必须分账，正权floor不自动覆盖learned ODE经过的区域；reference、可微loss和路径/敏感度覆盖仍是条件。相同sampler和decoder也不会撤销训练目标变化，有限网络与一步积分更不继承精确终态保证。Reference求解、endpoint梯度、全部训练/调参、多scenario采样与下游solver均付费；权重、支持或独立分布/决策质量失配时，回普通FM、较弱重权与原consumer验证，不由原标签未改或局部加权loss更低批准无偏、无损和真实决策安全。

<!-- source-family:SF-2026-ARXIV-2606-16790 -->

把监督从velocity换成endpoint的likelihood后，还须重新检查训练目标是否识别了采样器真正需要的条件速度矩，不能把“几何上自然”当作等价证明。在一个[内禀平坦圆环的离散反例](https://arxiv.org/html/2610.31981v1#S3.SS1)中，两条相反路径在同一点相遇，正确平均速度为零；端点距离目标的全局最优预测却可位于另一侧，经log map解码得到非零速度。这不否定上面的欧氏平方回归，而是说明先求非线性端点中心再解码，不一定等于先求条件速度再平均；仅训练loss更低也不证明transport更正确。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19894`，Jun20补Jun19；消费sole§120首次必要，writer定点§3/AppD与actualCh24 posteriormean/有限Gaussian/经验支集及分噪声记忆完整链，2+1+2=5，唯cover→oracle localmean-mixture表示-v-可学习性接口差额深入。保VE/t0/显式cover域、pt平均非逐点/clean密度、维度与全部费；独校φ e^-x调用negative logit只隔离打印softmax/精确rate，不授已反证存在性或已修构造。未核全B/C/实现复现，PRE/SAVE/selfread/actualPOST仅本日真实层。

- `SF-2026-ARXIV-2606-19876`，Jun20补Jun19；消费sole§111唯一exact-v1必要，2+1+2=5，actualCh24 noise-law/score完整两段与finiteGaussian/经验读取完整后链、Ch29目标交接已读，仅score积分人口/measuregradient及mean-v-modeweight差额深入。保固定GMM精确GD/初始化separation域、驻点/TV权重/有限数值与全费ND；未核全E/F或实现复现，不授任意神经SGD/一步全训/全密度，PRE/SAVE/selfread/actualPOST仅本日实际层。
```

## 22067

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`

插入于唯一锚点前：`Circuit probe 依赖所测模型、层选择和干预定义，不能把相关 activation 当成唯一原因。`

### 完整新增正文

视觉选择的代理也可来自问题加入前后的变化，而不是单看较大的attention：比较query阶段对image位置的正向attention变化，选择相关heads/layers，再同时增强视觉与query读出，避免只把固定sink放大。[GIFT的有限分支](https://arxiv.org/html/2510.22067v1)仍需校准样本与信息词规则，模糊或不相关query会给错saliency，强度过大也会损任务；变化量并不认证事实或因果重要性。全部校准、attention读取、bias处理及生成均计费，局部32token延迟不授全服务成本；query、架构或正常能力失配时保原图/原读出和独立grounding，不由更低幻觉指标批准视觉证据充分。
<!-- source-family:SF-2025-ARXIV-2510-22067 -->

### 本人注

- `SF-2025-ARXIV-2510-22067` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22067v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增query差分而非静态强attention选择；邻接随后展开写入/读取诊断，明确仅代理且有强度反退。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增query差分而非静态强attention选择；邻接随后展开写入/读取诊断，明确仅代理且有强度反退。

### 当前完整必要邻接

```markdown
### Object Hallucination 需要分开视觉写入与语言读取

对象幻觉常被压成一个端到端错误率，但同一错误可能来自视觉证据没有进入表示，也可能来自证据存在却被语言 prior 覆盖。Dual-pathway circuit analysis 用层级定位和因果干预区分 visual-evidence write path 与 language-prior read path，使“看不到”和“不采用”成为不同故障。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13156 -->

Circuit probe 依赖所测模型、层选择和干预定义，不能把相关 activation 当成唯一原因。诊断不稳定时，应回退输入/输出级的证据对齐、反事实图像和行为评测，不据单个 circuit 自动修复模型。

幻觉sensor还要比较从哪类token读信息：已消费图像的instruction hidden states可能比原image-patch states更便于读出对象，但不表示语言位置拥有新的观察。一个[受限detector分支](https://arxiv.org/html/2605.12258v1#S4)以instruction的object-token读出调节局部视觉分数，再比较选中instruction states与生成对象state的一致性；logit lens、同义词与first-subtoken规则都影响结果，概率与表示接近不是事实校准。Q-Former架构存在image读出更好的反侧，较长指令检测更好也可同时生成更多幻觉，检测与修复不能合并。Hidden保存、词表投影、阈值和完整生成均付费；架构、读出或旁侧质量失配时，保留image/外部grounding、原输出与独立对象标签评价，不由某位置AUROC批准无幻觉或实时SLO。<!-- source-family:SF-2026-ARXIV-2605-12258 -->

表示经过 contextual encoder 后，原文中哪个词说出了关系，并不决定内部哪个 token 承载它。在受控两物体生成中，随机文本 embedding 加位置的分支可由 relation head 把关系写成 image-position tag，再由 shape head 读取 tag 生成对象；T5 contextual embedding 则可把同一关系吸收到 object token 中。于是，遮掉显式 relation word 后输出关系不变，不能单独推出模型没有消费关系。应绑定 text encoder、position、token 类别与实际干预单位，再比较 head-specific ablation、tag 的 VO 注入或 object-token relation vector 替换，而不是只看 attention 强度。<!-- source-family:SF-2026-ARXIV-2601-06338 -->

[必要干预原证](https://arxiv.org/html/2601.06338v1)支持这种受限路径差异，权限只到三种 shape、两种 color、八种 relation 的 toy DiT 与所测 encoder，不能宣布所有自然图像或多物体使用同一电路；variance partition 和 attention synopsis 本身仍只是定位工具。相近 ID 关系准确率也不保证相同提示鲁棒性：添加 filler 的切片中，T5 分支关系准确率约下降40%，随机表示更稳，不能由“已有语言语义”推定关系组合一定更可靠。表示读取、白盒搜索、干预和独立质量回归均付费；未披露的完整硬件/运行预算不补成部署优势。路径或人口失配时，保留原 encoder、输入级反事实与可核对象/关系评价，不让较易解释的随机表示成为通用替代。<!-- source-family:SF-2026-ARXIV-2601-06338 -->
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19915`，Jun20补Jun19；writer首次exact-v1§2–4/A/B/C1–2必要，2+2+2=6，actualCh23 GR3D完整前肩/COCO-Tree完整后肩、几何监督与Ch25交接已读，仅多层显式depth/ray/point训练-v-辅助读出解释资格差额深入。保teacher伪GT/坐标依赖、probe/QA相关非causal、目标/半监督负侧/单行配置与全费ND，不授worldstate或零费；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-19828`，Jun20补Jun19；writer首次exact-v1§3–5/A/B/C/E–I必要，2+1+2=5，actualCh23 pooling/PointLinguist完整前链及稠密Gaussian/按需query后肩、maskcodec词表交接已读，仅3Dslot词表标签-v-连续结构marker双向consumer差额深入。保本输入ID/固定K/筛后人口、五inference非五trainseed、rawmarker/双refine负侧、全LLM训练与全部费，不授真实parts/精确mask；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。
```

## 22603

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`

插入于唯一锚点前：`新的dense消费者也可以同时读取几个深度的patch`

### 完整新增正文

多模态特殊token的sink还可能在适配中形成，而不是只有预训练BOS这一处。可保持hidden范数不变，旋转中间token朝向或远离BOS，分别检查sink与巨大activation是否随之出现/消失；再把BOS与非BOS方向的相关性作为训练正则。[受限音视频识别对照](https://arxiv.org/html/2510.22603v1)支持这套局部干预，在高压缩条件改善WER、低压缩近原模型，却不证方向对齐是任意架构唯一根因或全部sink都有害。正则层位、强度、压缩率和适配版本须共同绑定，训练/诊断及原任务回归仍付费；低压缩、旁侧质量或迁移不合时保原模型与较弱正则，不把sink消失当完整理解或事实grounding。
<!-- source-family:SF-2025-ARXIV-2510-22603 -->

### 本人注

- `SF-2025-ARXIV-2510-22603` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22603v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。置DIYSink之后、dense多层patch消费者之前；新增BOS方向的范数保持干预与高压缩适配，不放Object Hallucination小节，不把WER当事实grounding。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

置DIYSink之后、dense多层patch消费者之前；新增BOS方向的范数保持干预与高压缩适配，不放Object Hallucination小节，不把WER当事实grounding。

### 当前完整必要邻接

```markdown
视觉高范数候选进入语言模型后，还要追踪它来自哪里、由谁读取，而不把所有attention sink当成同一种状态：ViT传播来的token与语言模型原生sink可占不同hidden方向，阈值、层与归一化不能跨模型直接复用。[DIYSink的受限分支](https://arxiv.org/html/2510.08510v1#S3)分别比较将候选连同位置表示前移、以独立projector承接两组再联合适配，以及用query条件重加权；这些都改变语言consumer，不是纯删除或原函数无损置换。进入因果序列后的先后可见性要与视觉probe可读性分验，RoPE也不提供普遍单调衰减定律；只读query embedding的路由器不能声称按当前图像难度选组，soft缩放全tokens更不免前向。应保存来源/组index、position、双projector与LLM快照、路由输入和global/local任务回归。全部诊断、重排、分路训练/联合适配、query编码与多轮推理均费，部分任务仍退步，路由亦可比原模型更慢更占内存；身份、位置或质量预算失配时，保原序列/投影、专用dense读出与真实局部监督，不由高norm、干净热图或冻结ViT批准普遍语义完整和净加速。

<!-- source-family:SF-2025-ARXIV-2510-08510 -->

新的dense消费者也可以同时读取几个深度的patch，而不只接最后一层或重新安排所有预训练监督。一个[受限视觉迁移对照](https://arxiv.org/html/2509.02379v1)将多个block的patch特征拼接给轻decoder，并在保持patch大小时提高输入分辨率，再做目标域自监督适配；取层、token网格/对齐、拼接宽度、decoder和训练阶段共同定义新接口，不能由沿用foundation backbone批准原消费者无损。多层读出与更高分辨率分别增加activation/decoder和整条前向费用，域数据/teacher训练也另计；较好DSC并不保证边界指标同步改善。借用早期teacher的patch相似关系约束在该域未带来额外收益，不能因此宣布它处处必要或永远无效；可视化更稳定也不替代独立dense任务与原全局行为验收。应保留来源与volume划分、分辨率、各层/阶段及全部适配预算，标签或输入域、净质量/费用不合格时，退回原末层/单尺度读出、较低分辨率和已验证专用监督，而不由多尺度名称签发通用迁移或部署能力。
<!-- source-family:SF-2025-ARXIV-2509-02379 -->

选择少数heads干预时，还要分清删除计算与重分配读取：一条[受限CLIP分支](https://arxiv.org/html/2507.00537v1)保留原Q/K/V和head输出路径，只把选中head已经归一化的patch列权重缩小，再逐行归一，使读取相对偏向CLS。它不是把这些heads变成零输出，也不因检索变好证明其中只有噪声、对应区域无用或可省去原Attention计算。选择可由有标签图文校准上的搜索或小量可训练抑制系数提出，选择域、head/层、系数、归一规则和encoder版本必须共同保留；全局静态选择不等每张图都获益。校准、搜索/反传、重编码和新旧consumer回归均付费，非自然图像及组合任务已有反退，平均召回不能代替局部语义与完整费用验收。领域、分母或质量/成本不合格时，关闭抑制并保留原encoder、独立局部读出与真实监督，不从“ablation”名称批准物理剪头、无损或通用部署加速。
<!-- source-family:SF-2025-ARXIV-2507-00537 -->

全局聚合不稳时，也可以让learnableanchors读取已有的中间patch，再按图像形成局部匹配读出，与原globalfeature互补；候选anchor放在textspace，并不证明它具有可读人体语义。应把遮掉原signal与加入语义confusingdistractor分成两种压力，固定backbone后再检验aggregation，而不将两者都叫信息缺失。[SAGA的受限CLIP对照](https://arxiv.org/html/2604.22190v1)中，freeanchors与显式语义后缀的结果限制了语义解释，强遮挡耗尽signal或低覆盖时局部分支仍会退步；干净gallery与合成query也不代表真实camera变化。额外anchor/读出训练、约30M参数、patch读取和完整回归均计费，局部FLOPs估算不授净时延或免费适配；cue、覆盖或原任务失配时，保留原global聚合、融合路径与专用dense监督，不让更强retrieval或可视化attention认证唯一因果位置。<!-- source-family:SF-2026-ARXIV-2604-22190 -->

保留局部patch人口，还可以反过来让文字在这些patch之间竞争分配，而不是用少数文字或learned anchors先汇聚视觉。一条[受限分类分支](https://arxiv.org/html/2509.06336v1#S3)把同图的全局CLS广播到patch后，以这些状态作queries、正负类的多份paraphrase作keys/values；先沿patch-query维归一使同一文字竞争分配，再按每patch的文字权重和归一，以聚合文字值更新原patch的GRU状态并加残差MLP，最终仍池化分类。这些“多视角”是同一观察的多种措辞，不是新相机或独立证据，保留patch数量和GRU旁路也不保证局部信息无损或attention具有真实像素语义。训练另按样本标签选择正类或负类的均值文字anchor，对patch相似度作软权重并交辅助分类loss；它与部署主读出分责，不得把已知训练标签变成线上可用oracle，亦不能将样本类监督说成逐patch真假标注。文字encoder权重冻结仍训练prompt，视觉encoder也更新；需共同绑定候选类/措辞、patch坐标/CLS混入、归一轴与循环状态、标签支持和两条消费者，而不照录原文未闭的迭代/数值实现。有限两套跨域对照有HTER/AUC切片反退，更多文字和逐个anchor也可能更差；mean与联合模块的改善不证明属性真值、独立因果或真实认证安全。措辞生成/审核、所有编码与视觉微调、patch×文字关联/多轮GRU、辅助监督、阈值选择及真实新旧域回归全计费，ROC固定点不是线上风险或完整时延保证。类别支持、局部细节或净预算失配时，保原CLS/global读出、简单一对文字/较小词池和可信局部监督，独立验真实攻击/人群与外部权限门，不让热图或分类概率批准身份及行动。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19915`，Jun20补Jun19；writer首次exact-v1§2–4/A/B/C1–2必要，2+2+2=6，actualCh23 GR3D完整前肩/COCO-Tree完整后肩、几何监督与Ch25交接已读，仅多层显式depth/ray/point训练-v-辅助读出解释资格差额深入。保teacher伪GT/坐标依赖、probe/QA相关非causal、目标/半监督负侧/单行配置与全费ND，不授worldstate或零费；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-19828`，Jun20补Jun19；writer首次exact-v1§3–5/A/B/C/E–I必要，2+1+2=5，actualCh23 pooling/PointLinguist完整前链及稠密Gaussian/按需query后肩、maskcodec词表交接已读，仅3Dslot词表标签-v-连续结构marker双向consumer差额深入。保本输入ID/固定K/筛后人口、五inference非五trainseed、rawmarker/双refine负侧、全LLM训练与全部费，不授真实parts/精确mask；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。
```

## 22127

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`

插入于唯一锚点前：`Serving 侧还要面对 modality-specific admission：`

### 完整新增正文

部署时的轻量适配也须声明哪些状态在样本间延续。在预训练图文encoder上做域移分类，可以只适配少量Norm参数，按当前预测给伪标签、维护跨batch类均值与全局均值，以总方差减类内方差估计类间方差并最大化；每batch重置encoder和optimizer，却延续mean与gradient统计，是一条不同于持续累积全部权重的状态路径。[MintCLIP的受限corruption对照](https://arxiv.org/html/2510.22127v1)支持局部表示修正，但错伪标签会污染统计，更大类间方差也不认证伪标签语义正确；独立corruption序列也不证明连续漂移或自适应攻击鲁棒。统计人口、reset时机、层/梯度积累与预处理必须绑定，适配及回归全计费；类别支持、统计或正常效用失配时保原zero-shot表示、清除派生统计并退回固定参数，不由无人工标签批准安全在线学习。
<!-- source-family:SF-2025-ARXIV-2510-22127 -->

### 本人注

- `SF-2025-ARXIV-2510-22127` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22127v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增少量Norm适配、最大化估计类间方差，以及reset参数/optimizer而延续mean与gradient统计；不把主干冻结误作表示不变或无状态，伪标签与真实漂移边界保留。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增少量Norm适配、最大化估计类间方差，以及reset参数/optimizer而延续mean与gradient统计；不把主干冻结误作表示不变或无状态，伪标签与真实漂移边界保留。

### 当前完整必要邻接

```markdown
多种专用视觉能力也可以只作为表示训练目标，而不在每次请求执行全部teacher：为不同任务保留独立query组，让其读取同一图像，再经各自对齐头拟合冻结视觉模型的特征；部署使用这些已学query及语言消费者。[VaCo的受限分支](https://arxiv.org/html/2510.14349v1#S3)用组间attention mask限制信息流，但隔离query不证明teacher目标互不冲突，较低特征loss也不认证真实几何或下游答案。Teacher/取层、query组、mask和两阶段适配应共同版本化；专用teacher与训练对齐头不必进入普通推理，额外query及语言前向仍有成本，全部teacher制备/特征、对齐训练与独立任务回归也付费。目标支持、组间竞争或净质量失配时，保留原encoder/projector、较少可信teacher或专用在线组件，不由训练时知识迁入的名称签发无损通用视觉能力。

<!-- source-family:SF-2025-ARXIV-2510-14349 -->

Serving 侧还要面对 modality-specific admission：一张高分辨率图像、十秒视频和一段文本不能仅按请求数计费。runtime 应在 encode 前估计 token expansion、decoder/refiner 成本、deadline 与 cache policy。具体 batching、KV 和 SLO 归 Part V，但其输入 contract 由本章产生。

端侧共享 embedding 还可以把模型常驻容量与索引容量分开选择：保持一个文本 backbone 和共同输出空间，只加载任务需要的视觉或音频 encoder；混合输入仍消费同一上下文预算，并由显式 media placeholders 保留输入顺序。与生成模型共享 tokenizer 或 audio encoder 是组件复用机会，不代表 encoder 已可无条件热换或整条 RAG 不再计费。一个公开的模块化接口把 text-only、text+vision、text+audio 与完整模型区分为四种装载配置；装载哪组 encoder 改变计算与常驻权重，截短输出向量则主要改变索引存储与检索质量，两者不能用同一个“更小模型”标签代替。<!-- source-family:SF-2026-GOOGLE-EMBEDDINGGEMMA2 -->

[该表示接口的公开限制](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)要求截短后重新 L2-normalize，query 与 corpus 采用相同维度；其 128 维多模态结果明显退于完整 768 维，不能把六倍向量压缩写成通用近乎无损。数值 dtype 又是独立正确性条件：作者明确排除因 activation 范围溢出而出现 NaN 或静默降质的 FP16 路径，规定 BF16/FP32；这不等于任意量化 bundle 已通过同一质量评价。应把模态集合、采样/token 预算、任务 prefix、维度/归一化与 dtype 同时绑定到 encoder/index 身份，分别回归检索质量和真实总费用；缺模态、索引或数值不相容时回完整维度、受支持精度与原专用 encoder，不能从 active-weight RAM 推出整 pipeline 内存、隐私或可靠性保证。

### Edge split 把 fused latent 变成通信接口
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19915`，Jun20补Jun19；writer首次exact-v1§2–4/A/B/C1–2必要，2+2+2=6，actualCh23 GR3D完整前肩/COCO-Tree完整后肩、几何监督与Ch25交接已读，仅多层显式depth/ray/point训练-v-辅助读出解释资格差额深入。保teacher伪GT/坐标依赖、probe/QA相关非causal、目标/半监督负侧/单行配置与全费ND，不授worldstate或零费；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-19828`，Jun20补Jun19；writer首次exact-v1§3–5/A/B/C/E–I必要，2+1+2=5，actualCh23 pooling/PointLinguist完整前链及稠密Gaussian/按需query后肩、maskcodec词表交接已读，仅3Dslot词表标签-v-连续结构marker双向consumer差额深入。保本输入ID/固定K/筛后人口、五inference非五trainseed、rawmarker/双refine负侧、全LLM训练与全部费，不授真实parts/精确mask；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。
```

## 22101

文件：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

插入于唯一锚点前：`### KV 从生成私有状态演进为受约束的下游读出接口`

### 完整新增正文

共享prefix还可以在同一批次的一次前向内物化，而不先独立执行一轮prefix Prefill：先让公共token产生各层KV，再让每个suffix分别读取这份公共KV与自身causal部分，以log-sum-exp合并两份归一化读出。两个集合必须不重叠且mask/位置与原序列一致，不能直接相加已归一化的attention输出。[生产SLM评分路径的受限案例](https://arxiv.org/html/2510.22101v1)把这种in-batch复用用于最后token的相关性logit，不等任意聊天生成或不同context可共享。公共/私有layout、batch组装、identity与合并kernel应共同验数值；tokenization、gather/CPU同步、全部suffix计算和质量回归均计费。作者参数/上下文压缩及流控联合收益不单归prefix kernel；共享少、布局不合或质量/SLO回归时保普通单序列Prefill与成熟prefix cache。
<!-- source-family:SF-2025-ARXIV-2510-22101 -->

### 本人注

- `SF-2025-ARXIV-2510-22101` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22101v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增同forward内prefix/私有suffix的LSE交接，与前段跨请求兼容性及后段下游KVconsumer分清；不借10x宣称单因子。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增同forward内prefix/私有suffix的LSE交接，与前段跨请求兼容性及后段下游KVconsumer分清；不借10x宣称单因子。

### 当前完整必要邻接

```markdown
这条路径获得的是已有 context state 的 mobility，不是任意模型间兼容。现有证据不计 source prefill，只有 116 个
within-family 样本和两组 cross-family pair，部分 runtime overhead 未分离，长 Context 质量还会下降；因此不能把
局部 handoff latency 外推为端到端收益或通用转换保证。

<!-- source-family:SF-2026-ARXIV-2608-30963 -->

### KV 从生成私有状态演进为受约束的下游读出接口

KV Cache 最初只是生成器自己的加速状态：同一个模型继续 Decode 时，复用已经算过的历史表示。若另一组件需要评价一条 trajectory，最稳健的旧方案仍是把文本交给独立 verifier 重新 Prefill。这个接口与 generator 的内部布局解耦，允许异构模型与不同信任域，也保留一定错误独立性；代价是每次评分都会重新编码已经由 generator 处理过的长度 (L) 历史。

当长 trajectory 在 test-time search 中被反复评分，而且 generator KV 仍然存活时，可以增加一条更紧耦合的 Alternative Branch：compatible verifier 切换到同一 base architecture 上训练的 readout adapter，追加一个 verify query，直接从现有 K/V 读取 reward proxy。此时被消除的是重复 Prefill，不是评分本身；单次 readout 仍需遍历历史状态，也不能把作者报告的 scoring FLOPs 或单次 latency 比例外推成端到端 Agent 加速。

这项优化改变了 KV identity contract。过去只需证明 cache 与当前 request 的 model、token、position 和 layout 相容；跨组件读取还必须绑定：

```text
generator checkpoint
+ verifier adapter / readout head
+ tokenizer and position / RoPE semantics
+ dtype, cache layout and kernel contract
+ search branch lineage
+ allocation generation and lifetime
= reusable verifier input identity
```
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19667`，Jun20补Jun19；消费sole§66唯一exact-v1必要，2+2+2=6，作者actualCh45 prefix预测/驻留完整前肩及TempoKV/workflowhint后肩、Ch76顺序consumer交接已读，仅同组docs主动生产可复用prefix差额深入。旧Jun18仅trace不授body；保metadata非allocator、set非ordered等价、A/B p95与public无locality反侧、NQ无grounded质量/全费ND，不授净SLO；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。 sole§79完整PRE通过，SAVE/实际POST仅本日canonical真实层。

- `SF-2025-ARXIV-2510-12872` — Daily2025-10-17补Oct16；exact-v1 S3.1–3.4/S4/6.1由R10唯一必要，2+2+2=6，仅同checkpoint/模板slot的anchor近似offset与fallback差额。保pool20/gamma.3/顺序、98.2%reuse伴3.3%质量损、H100/两7–8B/2–5agents/gen512和HF重实现CacheBlend20%非原vLLM全栈；未采两附录完整误差proof、任意异权重兼容或SLO，未核代码/复现，PRE/SAVE/完整自读/solePOST按实际canonical。
```

## 22556

文件：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

插入于唯一锚点前：`### 跨 Turn Eviction 必须保留 Surviving-row Identity`

### 完整新增正文

同一KV预算还可在token与连续块之间选择粒度：先按标点等低成本边界分段，用段统计修正token分数，再以全局Top-B给每段隐式预算；段内从大块向小块搜索，只要其保留分数达到token基线的阈值便接受，最后超额块仍可裁成token。[SABlock的有限对照](https://arxiv.org/html/2510.22556v1)因此用选择代理换连贯访问，但分数比例不是语义保真，标点也非所有语言/代码的真实边界。近期保护区、段/块、实际保留数与logical positions须共同保存；Prefill后压缩、分段/搜索、gather及全部生成均计费。单A100、无batch的TBT改善不认证完整请求或并发，罕见细节和质量回归时保更细粒度/较宽预算、FullKV或offload，不由块更大批准无损。
<!-- source-family:SF-2025-ARXIV-2510-22556 -->

### 本人注

- `SF-2025-ARXIV-2510-22556` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22556v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增预算隐式分配与块粒度搜索，不重复普通eviction；与后段surviving-row身份自然交接，严格区分score与语义。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增预算隐式分配与块粒度搜索，不重复普通eviction；与后段surviving-row身份自然交接，严格区分score与语义。

### 当前完整必要邻接

```markdown
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25475:start -->
Learned importance 可以把固定窗口或手写分数改为逐 token 保留提议，但 eviction 仍然是不可逆状态删除。一个更保守的分层方案让 indexer 只决定 KV residency，同时把被逐出 token 压入在线更新的 latent memory，后续以 residual readout 提供有损召回。这样把“有限显存中的精确 KV”与“较小的派生远程记忆”分开，不能把 latent state 冒充原 KV。

代价是 indexer 训练、latent update、额外 readout 和更复杂的 cache identity；importance miss 或 latent collision 仍会造成不可逆退化。高风险或低置信请求应回退 FullKV、静态窗口、offload 或逐出后重算。作者模型与压缩预算只证明这一分层在所测范围内可行，不证明任意长上下文都能无损压缩。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25475:end -->

### 跨 Turn Eviction 必须保留 Surviving-row Identity

多轮对话若只按当前 turn attention eviction，可能删除后续 intent 仍需要的历史 token；反过来保留全部历史又让
KV 线性增长。一个受限分支维护跨 turn `QueryMemory` 作为 retention proposal，并用 sentinel/slot map 把 surviving
K/V rows 重定向到紧凑布局，同时保持 logical position、RoPE phase 与 prefix-cache identity：

```text
current query + versioned cross-turn intent state
-> keep/evict proposal
-> sentinel slot remap
-> compact physical rows with unchanged logical identity
```

QueryMemory 不拥有事实或授权，只影响派生 cache retention；误判时必须能回退重算。新增 state 带来 intent drift、
slot-map correctness、metadata 和 eviction overhead。作者 Qwen3-8B/Qwen2.5-14B、BCP 与 8k budget 只支持所测
quality/memory slice，`8k` 不是 latency SLO，也不证明任意 prefix sharing 安全。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19667`，Jun20补Jun19；消费sole§66唯一exact-v1必要，2+2+2=6，作者actualCh45 prefix预测/驻留完整前肩及TempoKV/workflowhint后肩、Ch76顺序consumer交接已读，仅同组docs主动生产可复用prefix差额深入。旧Jun18仅trace不授body；保metadata非allocator、set非ordered等价、A/B p95与public无locality反侧、NQ无grounded质量/全费ND，不授净SLO；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。 sole§79完整PRE通过，SAVE/实际POST仅本日canonical真实层。

- `SF-2025-ARXIV-2510-12872` — Daily2025-10-17补Oct16；exact-v1 S3.1–3.4/S4/6.1由R10唯一必要，2+2+2=6，仅同checkpoint/模板slot的anchor近似offset与fallback差额。保pool20/gamma.3/顺序、98.2%reuse伴3.3%质量损、H100/两7–8B/2–5agents/gen512和HF重实现CacheBlend20%非原vLLM全栈；未采两附录完整误差proof、任意异权重兼容或SLO，未核代码/复现，PRE/SAVE/完整自读/solePOST按实际canonical。
```

## 22210

文件：`books/part-07-agent/76-rag.md`

插入于唯一锚点前：`切分还决定知识更新时的重算放大，而不只是一次查询的证据范围：`

### 完整新增正文

代码的片段边界还可由语言服务的符号定义/引用关系给出，而不是只靠embedding相似：先在明确workspace内定位符号，用最小包围语法单元扩展上下文，再按定义/引用补足依赖；语言服务诊断可驱动后续修订。[LSPRAG的受限三语言对照](https://arxiv.org/html/2510.22210v1)让边界producer与semantic retriever分责，仍受静态分析、动态语言和索引版本限制，找到definition不证明测试意图或代码行为正确。Source revision、workspace、LSP/AST、符号位置与返回原文应共同绑定，文中mutation score只支持有限故障发现，诊断无错、覆盖率与需求/测试oracle正确性另验；启动索引、查询、repair/编译与全部生成都计费。符号不可解、跨revision或净质量失配时保lexical/普通结构chunk、原文回读与独立运行测试，不让语言服务接口替最终正确性签字。
<!-- source-family:SF-2025-ARXIV-2510-22210 -->

### 本人注

- `SF-2025-ARXIV-2510-22210` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22210v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增LSP定义/引用作为chunk边界producer，不把已有结构切分泛称足够；最终测试正确性保持独立。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增LSP定义/引用作为chunk边界producer，不把已有结构切分泛称足够；最终测试正确性保持独立。

### 当前完整必要邻接

```markdown
- embedding 表示混合多个主题；
- 无关 token 占 context；
- 精确 citation 困难；
- Prefill 成本增加。

更合理的策略结合 document structure、semantic boundaries、overlap 与 parent-child retrieval。没有对所有语料通用的 chunk size。

切分还决定知识更新时的重算放大，而不只是一次查询的证据范围：即使encoder冻结，文档前部的小段插入也会移动固定长度边界，使未改文字落入不同payload而必须重编码。可在新旧revision间只复用严格相同的chunk输入，并将source/segment身份、chunker参数与encoder版本共同保存；评价同时测重编码输入token比例和相同检索预算下的质量，而不从原文编辑比例推算embedding费用。[相邻修订的受限对照](https://arxiv.org/html/2610.31019v1)支持这种边界漂移压力，不证明内容感知切分普遍最优：recursive与content-defined边界的成本排序随长度/语言翻转，失败项不能从分母静默删除，小recall差额的区间触零也不是等价证明。边界检测、比对、重编码、索引发布及质量回归全要付费，输入token重算率不等金钱或服务延迟；更新少时简单固定切分仍合理，复用身份或质量不稳时保留完整重编码和原始证据检查，不以少重算批准支持完备。<!-- source-family:SF-2026-ARXIV-2610-31019 -->

固定小块适合局部问题，却可能把同一问题所需的多条证据拆散。文档内层级可靠时，可以先用小叶子匹配，再根据已命中的兄弟覆盖和剩余token预算，决定是否改向reader交付完整父段；这改变的是最终消费的原文范围，而不是让树节点获得事实权威。[HiChunk的受限分支](https://arxiv.org/html/2509.11552v1#S4)支持把检索粒度与交付粒度分开，但过粗的父层也会降低召回，末尾截断仍可能切掉合并后所需的证据，不能从层级完整或预算检查推导支持完备。评价应同时保留少量句子即可回答的问题与需要分散证据的问题，在相同context预算下分别看证据召回和最终答案；合成问题的长度、来源和模型筛选也在改变，不能把差额唯一归于证据密度。结构标注、边界模型训练、索引、原文展开与reader生成都付费，较低分块耗时不等全链更快。层级、证据支持或净预算不稳时，保留原文小块/hybrid与独立支持核验，不靠更大的父段补造缺失事实。
<!-- source-family:SF-2025-ARXIV-2509-11552 -->

不想整段展开时，也可只检查命中块的有限相邻块：邻块对 query 的相关性决定它是否可能有用，与命中块的连续性只作为附加罚项，再将门槛相对当前命中块的 query score 设置。[受限扩展对照](https://arxiv.org/html/2606.16661v1#S4)以此在固定窗口和不扩展之间提供可调分支，而不是让“相邻”自动获得交付权。非零连续性罚不会随相关性刻度同步缩放，跨 encoder 仍须验门槛；主块弱相关时降低门槛，也不证明其邻居更可信。该分支用较少上下文换取了可测的召回损失，表格续行等独立相关性弱的片段尤其可能被误删，非相邻或主检索未覆盖区域也不会自动补回。应绑定 chunk/encoder revision、邻域半径和去重规则，分别测证据召回、最终支持与完整编码、评分、生成费用；连续性或门槛失配时，保留静态窗口、父段展开或重新检索，不从更高每块效率批准答案完备。

<!-- source-family:SF-2026-ARXIV-2606-16661 -->
```

### Review notes邻接

```markdown
## Review notes

本人注：`SF-2025-ARXIV-2510-18204` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §2.1–2.2支持，reader R12 §3.1/3.5/B.3关键反侧，2+1+2=5，抽象指南/依赖slice双载荷与多facet消费者差额深入。保总结漏信息、SecurePass同sample交集/非全输入安全、反馈工具非truth及多draft/调用全费；未核实现/复现。PRE/SAVE/全自读/sole actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-19719` — Jun20补Jun19；消费sole§17唯一必要§2–5/AppD/F及中心反侧，作者actual Ch76受影响semantic-body/trace和完整两肩已读。3+2+2=7；仅纠正实际正文，保GT-pair与selected-top1 valid-fire的对象分责，撤去未闭calibration decomposition/CRR正面采用；严格单调不变与finite-grid解释待unique-threshold核，中心H不进入Books。原旧日期/身份保留，未核artifact/复现；完整PRE按sole§19实际层，SAVE后selfread与actualPOST据本日canonical，不以本注预签。
```

## 22118

文件：`books/part-04-training-system/27-data.md`

插入于唯一锚点前：`### 递归合成语料要先分清 Corpus Recursion 与 Parameter Recursion`

### 完整新增正文

当监督依赖空间关系时，可以先选可核对的较低层primitive，再把它realize成问题，而不先让模型补出不可见的完整三维世界。例如从2D检测框计算左右、包含等谓词、先筛合法关系，再生成问答，可缩短伪标错误链。[受限空间QA对照](https://arxiv.org/html/2510.22118v1)支持这条数据生产顺序，但bbox、对象检测和题义仍会错，2D大小/距离不等真实3D量；小样本人审有效率不是整库无误差。图像/框、谓词版本、筛选人口和语言实现须共同保存，人审、检测、realization与训练均计费；遮挡、深度或真实尺度必要时保可信3D/人工标注和原图核验，不用便宜primitive扩大标签权限。
<!-- source-family:SF-2025-ARXIV-2510-22118 -->

### 本人注

- `SF-2025-ARXIV-2510-22118` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22118v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增先选可核primitive降低监督链复杂度，承接synthetic编译不等真实3D；保检测误差和人审分母边界。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增先选可核primitive降低监督链复杂度，承接synthetic编译不等真实3D；保检测误差和人审分母边界。

### 当前完整必要邻接

```markdown
这种检测会增加 persona slice、对照集与训练 canary 成本，也可能把语气、角色相似度或 evaluator 偏差误判为隐含机制；
样本稀少、mixture 被大量真实数据稀释时，单篇叙事的影响可能不可测。回退不是禁止故事，而是限制未知生成来源、降低
mixture 权重、使用中性/反向角色对照，并在 canary 失败时撤回对应 partition。`arXiv:2609.10883v1` 只证明其合成故事、
模型和微调设置中存在条件行为与偏好转移；角色亲和度对学习率敏感，实验也不能证明某种隐藏表示或生产模型的普遍风险。

<!-- source-family:SF-2026-ARXIV-2609-10883 -->

### 递归合成语料要先分清 Corpus Recursion 与 Parameter Recursion

一次 synthetic-data 更新只需要回答“这批样本会把当前 checkpoint 推向哪里”；当模型输出继续成为下一代训练语料时，
数据系统还要回答“变化究竟由语料分布反复自举，还是由权重、优化器与训练状态跨代累积造成”。如果每一代直接继承上一代
checkpoint，两条因果路径会缠在一起：坏结果不能唯一归因于 corpus contamination，好结果也可能只是旧参数保留。一个更可辨识的
实验分支，是每代都从同一 clean base weights 重新训练，只让共享语料池随代际变化；这样牺牲了对真实 continual-training
流水线的还原度，换来对 corpus recursion 的隔离。生产系统不能二选一，而应在 lineage 中分别保存
`base checkpoint / optimizer state / supplier mixture / human-text fraction / generation / seed`，让数据链与参数链都可回放。

受损数据的迭代修复还应区分“生成得更干净”与“监督已经干净”。一条 diffusion 数据分支不把上轮修复图直接作为下一轮 clean corpus，而是每轮重新从同一个原始受损集合 `D0` 出发，由当前模型恢复到更低、但仍非零的 residual-noise level；训练继承前轮模型，却只在高于每个样本残余噪声的区间消费该样本。这样原观测 anchor、修复 producer、样本 corruption label 与 parameter inheritance 分别可追溯，合成输出不会只因视觉改善就获得 clean-label 权限。Lineage 需保存原样本、初始/残余噪声、round、restoration model 与实际训练 eligibility；这不同于重训 clean-base 来隔离语料递归，也不替代可信人工 anchor。

[有限的 dataset-model co-evolution 对照](https://arxiv.org/html/2601.15417v1#S3)支持这种渐进修复接口，但重复读取 `D0` 不会创造新的观测信息，更不保证任意 self-training 不 collapse。Restoration 太快或太慢都可破坏训练，残余噪声标注失准也会让样本进入不合法的学习区间；逐轮重建、继续训练与按质量选择 checkpoint 的总 compute 没有与普通训练完全匹配。它适合数据受损、可校准 corruption 且新数据有限的条件，而不是无条件优于取得 fresh 数据。噪声不可识别、质量/多样性回归或总费用不值时，保留原受损数据的稳健目标、可信 clean mixture、固定人工 anchor 与独立 held-out 检查，不把模型自评质量当数据放行证书。<!-- source-family:SF-2026-ARXIV-2601-15417 -->
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19625`，Jun20补Jun19；消费sole§65唯一exact-v1必要及currentv5仅F1cohort具名notice域，2+2+2=6，作者actualCh27 lineage/SAEridge/attributionspec完整前肩与futuremeasurement后肩已读，仅taxonomy区域聚合×任务contrast×同topic定向/random接口差额深入。保Base/Instruct/SFT近似、去重均衡非重复exposure、z/cohort与SocialIQA身份、J1局部强/零/负反侧、非真实删除/全部费，不授唯一因果/隐私闭合；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。 sole§67–68原整体稿PRE通过，实际SAVE与POST仅本日canonical真实层。

本人注：`SF-2025-ARXIV-2510-18583` — Locke，Daily2025-10-23补Oct22；exact-v1 §3.1–3.2/4.1–4.3必要，2+1+2=5，跨协方差/边缘feature两约束差额深入。保局部线性内层非完整InfoNCE最优、online encoder统计坐标、冻结文本基线混杂和真实/合成/下游全费；未核实现/复现，不采通用无损。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。
```

## 22332

文件：`books/part-01-worldview/05-what-neural-networks-learn.md`

插入于唯一锚点前：`如果目标还包括让内部计算更容易拆解，另一条分支是把约束前移到训练，`

### 完整新增正文

学习解释字典之前，还应把原模型的FF激活/value方向作为同对象基线，而不是只与随机向量比较：在相同层、输入和稀疏度下读取原生单元，再控制Top-K、幅度与方差，检查所谓可解释优势是否仍在。[受限FF/SAE对照](https://arxiv.org/html/2510.22332v1)显示人可辨认一组feature可能来自展示幅度，去掉该artifact后判断会变；这不证明所有SAE无用，也不让原神经元自动成为独立真实概念。字典宽度、层位、稀疏度、归一化与annotation人口共同定义比较，采集、训练和独立干预回归都计费；解释优势或行为支持不稳时保原activation、匹配基线与定向因果检验，不从可读描述批准完整机制。
<!-- source-family:SF-2025-ARXIV-2510-22332 -->

### 本人注

- `SF-2025-ARXIV-2510-22332` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22332v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增FF原生feature与幅度匹配这一具体解释器控制，非重复泛probe警告；不将单人/有限宽度实验外推。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增FF原生feature与幅度匹配这一具体解释器控制，非重复泛probe警告；不将单人/有限宽度实验外推。

### 当前完整必要邻接

```markdown
线性reader的局限，也不要求干预只能沿原空间的一条直线移动：可以先学习可逆的非线性坐标变换，在变换后的空间交换少数坐标，再映回原hidden state。这把“怎样读出”进一步分成“用哪份坐标定义编辑”与“编辑后下游实际怎样变”，却不让可逆坐标自动成为独立语义因子。没有直接输出标签时，可用对比输入的下游表示差异构造训练proxy；它仍依赖输入类别与筛选，不是从无标签发现了真实概念。[受限干预对照](https://arxiv.org/html/2605.14749v1)只支持局部非线性选择，单点编辑与多点累加的范数不直接可比，也未证明非目标能力或安全边界不变。数值求逆、激活采集、坐标训练、层位选择和独立行为回归均计费，近似谱估计不能认证全局精确可逆。坐标、数值残差或消费者回归不可靠时，保留原表示、线性/局部probe与已验干预，不由更小编辑量签发更忠实解释、无副作用或部署权限。<!-- source-family:SF-2026-ARXIV-2605-14749 -->

同一可逆坐标也可用于平移而非交换：先把当前activation映入latent，沿训练对比样本的差均值移动，再对这个新点求逆。小幅平移在原空间约为局部inverse-Jacobian作用于latent方向，因此通常随输入变化；只有affine变换或该作用恰好恒定，才等价于一份固定原空间方向。[受限coupling-hook分支](https://arxiv.org/html/2606.08454v1#S4)给出零shift恢复和同一层反shift的代数条件，不保证数值稳定、整条生成可回滚或语义不受影响；logdet正则也不控制全部条件数。归一统计、层位、坐标artifact、对比标签和强度须一起绑定，训练/搜索与每个受干预activation的forward/inverse均计费；目标回答概率提高仍可伴随PPL退化。坐标或消费者质量失配时，保原模型、较弱线性干预与独立行为回归，不由可逆性签发无副作用、安全或更快部署。<!-- source-family:SF-2026-ARXIV-2606-08454 -->

如果目标还包括让内部计算更容易拆解，另一条分支是把约束前移到训练，而不只分析已经形成的 dense 表示：训练时迫使大量连接权重为零，让网络在较少的连接中组织计算。这与事后用 sparse decomposition 提取特征不同，也不证明一个神经元只承担一种知识。在受限的简单算法任务中，可以继续剪除连接，检查留下的小 circuit 是否仍能完成任务，再删除其中关键边检验失效；这种充分性与必要性只相对于具体任务和干预成立，不证明它是唯一实现或完整解释。

连接约束又把能力、解释性和成本放到同一个选择中。固定模型规模下，更强稀疏可能损害能力；扩大模型可以改善所测能力—解释性前沿，却不等于等算力收益，更不保证更低的训练或部署成本。[稀疏网络的早期公开实验](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/)只解释了小模型的一部分简单行为，复杂计算仍有未解释部分。因此 dense 模型与事后分析继续是有效路径；只有解释需求足以承担容量及实现代价时，才值得考虑训练时连接约束，不能从局部 circuit 清晰直接推出前沿模型的可解释性或安全保证。
<!-- source-family:SF-2025-OPENAI-SPARSE-CIRCUITS -->

<!-- source-family:SF-2026-ARXIV-2605-00842:start -->
这种干扰不只发生在推理时，也会进入参数更新。若两个功能特征在共享表示空间中并不正交，针对其中一个方向的微调梯度就可能沿几何相似性同时放大另一个方向；原本为了节省维度而成立的 superposition，因而把“只修改目标行为”的局部假设改成了耦合更新问题。它解释了为什么窄任务数据可能在训练 loss 正常下降时，引起表面无关的行为变化，也说明只监控目标任务 accuracy 或参数距离不足以拥有微调安全结论。

这个机制把微调验收从单任务改成受影响行为集合：训练系统应保存数据、checkpoint 与更新范围，在提交新 artifact 前重跑目标能力和关键安全切片；几何邻近或 SAE feature 可以用于定位风险样本和提出诊断，却不能单独证明因果或替代行为回归。现有证据只在 Gemma、Llama 与 gpt-oss 的若干开放模型上，以共享 SAE basis、cosine similarity 和 LLM judge 检验局部几何假设；它没有证明所有表示都遵循同一坐标、所有邻近特征都会共同更新，或几何过滤能跨模型稳定校准。信号失配时，应回到隔离或移除可疑数据、缩小更新范围并执行完整安全回归，而不是把一个可解释性 proxy 升级为自动发布门禁。
<!-- source-family:SF-2026-ARXIV-2605-00842:end -->
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19831`，Jun20补Jun19；writer首次exact-v1§2–7/10/B1/3/E采用必要，2+2+2=6，actualCh5球面两段完整前肩/learnedsensing与prototype完整后肩、Ch17/72交接已读，仅signed归一幅度-v-行为/连贯/内容/rollout时限测量差额深入。保15个11判对近majority、family/depth/c0/后norm域、失败predictor/词面误判和全部费；未核全部S8/附录机制/实现复现，不授普遍law/扫描全召回/安全或攻击recipe，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-19668`，Jun20补Jun19；消费sole§70唯一exact-v1必要，2+1+2=5，作者独核Eq7–8/H3与actualCh5 coverage/RedirectQA完整两前肩、泛化后肩及Ch74pivot交接已读，仅frame×lexicon/两prefill访问候选差额深入。保English输出/F1、γ非anchor距离、identity翻转与sourceheavy负反侧、跨题相关/量化/双pass全费，不采用语言侧数学/单语安全保证；未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。 sole§79完整PRE通过，SAVE/实际POST仅本日canonical真实层。
```

## 22366

文件：`books/part-06-ai-infrastructure/72-security.md`

插入于唯一锚点前：`若标记落在生成文字上，优化时还须使用检测器真正计数的证据单位，而不只累计“绿色token”：`

### 完整新增正文

生成图像的标记还可放进初始噪声而不改生成器：一条通道由master key引出每次生成的session key，另一通道绑定payload；沿声明的正交方向作tail-truncated采样，再通过指定逆过程读取。[受限噪声水印分支](https://arxiv.org/html/2510.22366v1)把密钥复用、样本多样性与检测分开，但截尾会改变噪声分布，逆过程也有误差。常规裁剪/压缩后的检出不证明能抗proxy inversion或自适应伪造，数百null/攻击样本不能实测认证百万分之一误报；未显著画质差异亦非分布等价。Key/session、payload映射、sampler/inverter和null人口应共同留档，生成、反演、校准与质量回归全计费；信号或威胁超界时保Unknown、签名origin与独立取证，不由一次检出批准授权违规或法律归属。
<!-- source-family:SF-2025-ARXIV-2510-22366 -->

### 本人注

- `SF-2025-ARXIV-2510-22366` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22366v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增初始噪声/session分层与逆过程consumer，连接已有水印生命周期；低FPR/伪造与法律权限不混。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增初始噪声/session分层与逆过程consumer，连接已有水印生命周期；低FPR/伪造与法律权限不混。

### 当前完整必要邻接

```markdown
共享验证权与追查哪份发行副本外泄，是两种不同问题。若可疑服务只允许黑盒查询，另一条分支可先在服务器训练通用 trigger 的 embedding，再把同一向量映射到每个 client 的不同 token 行；客户端只更新 PEFT modules，服务器聚合并用通用 trigger 强化这些共享 modules，随后重新发行个性化 embedding。[EmbTracker 的受限联邦对照](https://arxiv.org/html/2603.12089v1)据此避免为每个 client 单独重训 watermark，但持久性依赖 embedding 在客户端更新中保持冻结，不是任意 full fine-tune 的承诺。这里归因对象是发行给 client 的 model instance，不是该 client 的私有训练数据、前述门限 key 的完整性或被阻止的泄漏。<!-- source-family:SF-2026-ARXIV-2603-12089 -->

验证须同时要求本 client 的 trigger 响应达到阈值、其余 client 的响应各自低于阈值；其他 client 的平均响应低，不能替代逐个排除。签名 message、有限词表中的 trigger 映射、发行模型与 PEFT 更新身份、验证样本/阈值及后续变换应绑定留档，这些是据接口推导的验收要求，不是作者已认证的发行协议或不可伪造证明。当前原研究依赖可信 server、遵循本地训练且不串谋的 clients；新增 overwrite 测试仍保留新旧水印并存，timestamp/CA 排序只是建议。初始化与每轮强化、个性化发行存储和逐 client 查询均付费，VQA/部分联邦优化及量化质量反退保留；超出冻结 embedding、攻击或校准人口时保留 Unknown，回退签名 origin/provenance、访问控制与独立取证，不由高 VR 认定法律责任、零误报或完整 confidentiality。

若标记落在生成文字上，优化时还须使用检测器真正计数的证据单位，而不只累计“绿色token”：非顺序unmask时，当前候选的左context可能未定，它又会改变后邻的context和预测。[一条受限DLM水印分支](https://arxiv.org/html/2610.32205v1)因此只奖励新增的distinct(context,token)单位，并估计候选放置后的邻居belief；对已计单位将中心化贡献归零，减少为重复文本付费的压力，不保证永不循环。另把不依密钥学习的词表band与密钥选择green band分开，平衡的是候选概率mass而非词数。检测对同context的各band单位数建立分布，再跨distinct context卷积；其精确性依赖随机函数假设及文本/partition不依密钥，不是每unit独立binomial，也不保证固定key在任意corpus上恰有相同误报率。单次KL最优tilt只针对估计的commit score，不授整篇最终检出最优；近似belief和有限order重算仍会错。主实验支持所测检出/质量取舍，域外高强度、替换和改写仍退步，style/consistency judge也不是事实或完整语义保持。Predictor虽不进检测器，却增加生成权重、候选forward与校验成本，EOS处理改变长度也会改变可检人口；全部trace/teacher、band和predictor训练、tilt/order、重新分词与独立null校准均计费。解码器、tokenizer、key/band、检测单位或分布变化时，重做相同人口的误报/检出/质量验收，保原采样与适用旧水印、签名origin和Unknown，不由一次检出批准内容真实、授权违规、抗移除或法律归属。
<!-- source-family:SF-2026-ARXIV-2610-32205 -->

学习文字水印时，检测器还可能只学到攻击留下的风格：冻结生成backbone，用语义mapper学习green/red分配，并同时优化原水印、改写及恶意编辑后的检测，必须另放“同样受攻击但从未加水印”的负对照。[受限RL水印分支](https://arxiv.org/html/2510.21053v1#S3)据此分开provenance与hate/paraphrase特征；四项AUC平均不认证所有攻击鲁棒，PPL也不等语义保持。原检测式mean(log p)非正，却与正0.5 reward锚点冲突，不能据印式补成可执行训练recipe。每backbone重训、攻击与负控、检测/质量和独立新攻击回归均付费；符号、质量或攻击人口不合时，保原水印/无水印基线与明确Unknown，不由攻击风格可识别批准来源认证或内容安全。

<!-- source-family:SF-2025-ARXIV-2510-21053 -->

音频水印还要面对生成与检测的tokenizer不一致：同一波形再token化后，原token身份可能改变，可先对token embedding聚类，再在较稳定cluster上对齐inverse sampling与检测。[Aligned-IS的受限分支](https://arxiv.org/html/2510.21115v1#S4)中的distortion-free是对secret key期望的分布等式，不保证每条音频无损或必被检出；prefix/ngram、历史去重和key条件也属于身份。Binomial/Hoeffding误报界依独立null/有效code，十三种单通道改动不认证任意相关、组合或自适应攻击。聚类、encoder、key治理、全部生成/检测与独立音质/语义回归均计费；再token化或null条件失配时，保原载体、明确未检出与独立来源证据，不由cluster命中批准音频真实性或法律来源。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-21877` — primary `arXiv:2606.21877v1`；exact-v1 URL=`https://arxiv.org/html/2606.21877v1`；Method=`https://arxiv.org/html/2606.21877v1 — §III AgentRiskBOM Design; §IV Implementation`；Evaluation=`https://arxiv.org/html/2606.21877v1 — §V Evaluation`；Non-proof=`https://arxiv.org/html/2606.21877v1 — §VII Limitations`。
- `SF-2026-ARXIV-2606-22019` — primary `arXiv:2606.22019v1`；exact-v1 URL=`https://arxiv.org/html/2606.22019v1`；Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it moves auditability; §7 Mitigations by channel`；Non-proof=`https://arxiv.org/html/2606.22019v1 — §8 Discussion, limitations, and related work`。
- `SF-2026-ARXIV-2606-22263` — primary `arXiv:2606.22263v1`；exact-v1 URL=`https://arxiv.org/html/2606.22263v1`；Method=`https://arxiv.org/html/2606.22263v1 — §III Design of Revelio; §III-C Hypothesis Confirmation by PoV Construction`；Evaluation=`https://arxiv.org/html/2606.22263v1 — §V Evaluation`；Non-proof=`https://arxiv.org/html/2606.22263v1 — §VI Discussion and Limitations`。
<!-- daily-20260621:platform-security:end -->

### 从边界隔离到受限条件下的可证明执行
```

## 22475

文件：`books/part-02-model/20-sampling.md`

插入于唯一锚点前：`## Logit penalties 与约束的边界`

### 完整新增正文

下一token也可由同一prefix下的多份条件logits合成，而不只过滤单一分布。例如给同一模型不同persona及neutral条件，按各路径confidence重权后再softmax；这增加的是条件前向，不等独立agent已有不同观察。尤其max-probability接近不代表token分布一致：两路径都以0.9押不同token，标量confidence仍相同；logit求和还改变有效temperature，权重可能为负时更不能叫凸共识。[CHOIR的有限对照](https://arxiv.org/html/2510.22475v1)支持局部多条件解码选择，未证互补知识或公平性根因。所有路径/KV、权重和采样顺序都计费，条件改变语义或质量/预算不合时保neutral单路径与已验采样，不让标量一致性认证答案正确。
<!-- source-family:SF-2025-ARXIV-2510-22475 -->

### 本人注

- `SF-2025-ARXIV-2510-22475` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22475v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增同prefix条件logit聚合与标量confidence反例；不把persona当独立证据，也不照录其权重公式为概率混合。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增同prefix条件logit聚合与标量confidence反例；不把persona当独立证据，也不照录其权重公式为概率混合。

### 当前完整必要邻接

```markdown
候选集合还可由离线参考token的统计来收窄，而不把高不确定性一律解释为应多探索：在固定模型、温度与logit处理下，按最大概率bin和rank统计teacher-forcing参考匹配率，再供动态rank上限或概率cutoff消费；低confidence处直接greedy是另一条不依赖该校准表的策略。[Correctness-first的受限对照](https://arxiv.org/html/2510.05987v1#S3)支持比较这些截断分支，却不让单一参考措辞的匹配率变成语义正确概率，gold-prefix统计也不自动迁移到自身错误prefix。Bin内均值乘积、稀疏零值与最大合格rank的处理须独立核对，不能由较好拟合宣布每个保留token安全；固定正斜率映射本质仍是概率阈值，不是在线语义verifier。闭答案多数票的收益与代码pass@k/创意质量不同，局部也有反退。参考/teacher制备、校准与阈值搜索、全vocab处理、全部样本/投票及独立答案核验均费；参考支持、温度或任务目标失配时，保原top-k/top-p、greedy或更宽独立候选，不由低confidence强制选择认证正确、安全和净降费。

<!-- source-family:SF-2025-ARXIV-2510-05987 -->

## Logit penalties 与约束的边界

Top-k 与 top-p 依据当前分数删减候选；如果任务还要求减少已出现内容的重复，或只允许合法格式，就需要把历史与任务约束也带入这一步。

Repetition、frequency、presence penalties 会根据已生成 tokens 修改 logits；grammar-constrained decoding 会屏蔽不符合语法的候选。

它们都发生在 token selection 层，却解决不同问题：penalty 是启发式偏好，grammar mask 是硬候选约束。它们可能改善格式或减少重复，也可能屏蔽正确 token。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2025-ARXIV-2510-13285` — Banach，Daily2025-10-17补Oct16；writer exact-v1 §3–5及Hegel R25必要复用，2+1+2=5，仅参考activation椭球/方向编辑与真实支持分责差额深入。保PCA40%/Mahalanobis95%、负判别式最近点仍可在外/a=0与奇异协方差未闭、SPI负向/MMLU拒答反退、同人口F1/PPL非事实及全费；不采always-ID/完整配方或实现复现，完整PRE/SAVE/自读/solePOST据canonical。

- `SF-2025-ARXIV-2510-12343` — Herschel，Daily2025-10-16补Oct15；消费Cicero R32 exact-v1 §1.2/2.1–2.2/3.1–3.3/4.1–4.4首次必要，2+2+2=6，仅近似onehot混合/坐标排序与embedding consumer差额。保plaintext非HE、诚实但好奇非恶意安全、TSP/PP式和cosmetric未闭、LoRA混杂及O(V²)/训练/加密全费，不授隐私部署或精确误差定理。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。
```

## 22489

文件：`books/part-05-inference-system/49-tensorrt-llm.md`

插入于唯一锚点前：`### 两种稀疏性必须共享地址合同，却不必共享 Kernel`

### 完整新增正文

剪枝校准也可同时问通用域与目标域，而不把一种activation统计当所有负载的重要性：比较两域channel范数，按差额提出exclusive/shared分区，再对共享部分混合两份保留分数。[受限task-aware pruning对照](https://arxiv.org/html/2510.22489v1)使校准人口进入mask选择，却不证明这些channel就是可分离的语义知识；未归一的范数差会受样本量/尺度影响，两份分数相加也不天然精确加倍。Domain、样本量/归一、阈值、pruning范围与最终pattern须共同保存，质量/通用保留与实际kernel分别验收；校准、搜索和恢复全计费，无实测执行不能由稀疏率推速度。域统计、保留质量或后端不合时保通用/混合校准、更保守mask或原dense，不由task标签批准无遗忘。
<!-- source-family:SF-2025-ARXIV-2510-22489 -->

### 本人注

- `SF-2025-ARXIV-2510-22489` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22489v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增通用/目标校准分区是重要性提案非语义真值；不采用原文重叠不等式和期望拆分作严格证明。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增通用/目标校准分区是重要性提案非语义真值；不采用原文重叠不等式和期望拆分作严格证明。

### 当前完整必要邻接

```markdown
因而投影回对称子空间，只能消除重建后额外引入的非对称分量；若错误本来就在共享代表值上，展开后仍在该子空间，第二次投影不会纠正它。[受限 codec 与反侧](https://arxiv.org/html/2604.17371v1)的更小 payload 可以改善特定独立丢包模型下的完整接收概率，却没有建立任意信道去噪或相同总 bit 预算下普遍优于剪枝。训练函数限制、CRC/零填充、索引与包头、重建和实际执行均须计费，分类质量反退或信道假设不合时，保留原稠密/结构化模型、成熟编码和可靠传输，不以参数数或模拟链路时延替代质量与部署验收。<!-- source-family:SF-2026-ARXIV-2604-17371 -->

压缩权重还可以改成原生执行的张量结构，而不只保存因子、运行时先还原dense矩阵。先按声明的bond维度将输入reshape（必要时padding），让多个local tensor分支分别作用于部分坐标，再平均合成原输出接口，是一种受限dense-linear替代；分支数、tensor化维度和被替换block共同决定可表达函数与执行成本。[MixT精确v1的Methods/Results](https://arxiv.org/html/2605.25344v1)保持这种operator直接前向，并在固定3000步恢复后沿不同block深度/顺序测MMLU退化边界；它不是原函数恒等改写、通用容量阈值或v2的理论叙述，直接压缩的退步与Qwen/Llama不同转折均须保留。权重匹配、恢复训练、padding/收缩布局及专用kernel均计费，FLOPs减少不等吞吐增加，H200实测峰值低于24GB也不等24GB设备已运行；质量、布局或恢复预算不合时，保较浅替换、普通低秩/稠密权重与成熟kernel，分别验完整任务和实际执行，不以一个稳定MMLU区间批准全部能力无损。<!-- source-family:SF-2026-ARXIV-2605-25344 -->

### 两种稀疏性必须共享地址合同，却不必共享 Kernel

非结构化小权重剪枝能直接表达“哪些参数不重要”，却不一定生成硬件可消费的稀疏布局。一个中间演进是联合优化权重与
soft mask，用局部二阶敏感度定义保留目标，再通过 progressive annealing 把连续 mask 收敛到明确的 `2:4` pattern。
训练侧拥有 mask 演化和最终权重，compiler 只接收冻结的结构化 artifact；runtime 还必须证明目标设备确实选择了对应
sparse kernel，否则参数稀疏只是文件属性而不是执行收益。

逐步硬化减少一次性剪枝的质量冲击，却增加 Hessian 近似误差、annealing schedule、重训练成本和 pattern lock-in。
作者实验支持其模型与稀疏设置下的质量恢复，不证明所有 layer 都应共享敏感度或任意硬件都能提速。若目标 backend
没有成熟 `2:4` 路径、恢复失败或 shape 太小，稠密权重与稠密 kernel 仍是正确 fallback；训练过程的 mask/optimizer
状态归第 28 章，本章只拥有可执行 artifact 与 kernel admission。<!-- source-family:SF-2026-ARXIV-2605-06402 -->

固定2:4 core之外，也可在其输入、输出两侧保留较小的block-diagonal变换，以三个算子共同近似原dense线性层。[受限压缩分支](https://arxiv.org/html/2510.05528v1#S3)用校准activation加权的逐层重构目标，交替优化连续wrapper和组内稀疏mask；one-shot只是不做全网重训，不是无校准、无迭代或一个forward。它用额外表达能力缓解硬pattern的损失，也增加参数、乘法、存储与kernel交接；只让core走稀疏tensorcore，不能把整层按半参数或峰值稀疏吞吐结算。局部proxy的收敛不授全模型质量或实际joint Adam同保证，受测任务/PPL仍可差于dense，wrapper又可比普通2:4更慢、更占内存。校准、搜索、三个算子/metadata与完整生成回归都付费，matvec与大batch generation的收益不合成通用SLO；block/shape不兼容、质量或净成本不合时，保留普通2:4、较保守剪枝或原dense，不由更好的重构分数批准无损和生产加速。
<!-- source-family:SF-2025-ARXIV-2510-05528 -->
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19565`，Jun20补Jun19；消费sole§48唯一exact-v1必要，2+2+2=6，作者actualCh49梯度/局部bit表/conditionalartifact与embodiedphase/DyQ完整两肩已读，仅global×worstprogressbin四边界静态量化artifact差额深入。保teacher-forced proxy非causal/闭环risk、组合低FP/过强temporal反侧、校准/trial/seed/完整latencyND与WbAb b²边界及全费；未核实现/复现，sole§57整体PRE通过，SAVE/selfread/actualPOST仅本日实际层。

- `SF-2025-ARXIV-2510-13757` — Banach，Daily2025-10-17补Oct16；writer exact-v1 §II–IV/TI–II与Hegel R23唯一必要复用，2+2+2=6，仅时间离散/62step导出/延迟buffer与训练部署差额深入。保1ms/62ms受限约差5%、GPU FP32五seed/Loihi int8一seed、单输入片上重复与Jetson batch/L2状态不同；NxKernel成员请求未核，不采250x全请求能耗、实现复现或TensorRT原生SNN，完整PRE/SAVE/selfread/solePOST按canonical。
```

## 22543

文件：`books/part-04-training-system/33-grpo.md`

插入于唯一锚点前：`### 正负 Advantage 不必共享同一 Clipping Contract`

### 完整新增正文

最终答案正确的人口内部，也可以再按过程错误分配reward，而不将全部positive同权：训练critic定位first error，对被判flawed-positive的完成追加惩罚，再由同题组中心化优势决定当前更新方向。正负人口随训练变化，同一额外惩罚便可能在早期仍给某些样本正优势、后期转为负优势；不是手工到某一步就删除所有自我纠错。[FAPO的有限对照](https://arxiv.org/html/2510.22543v1)支持这条分布依赖的reward设计，但GenRM继承自动过程标注错误，答对/first-error检测与真实内部faithfulness仍分责。Critic版本、标注来源、惩罚、组人口及异步服务应共同绑定，全部标注、rollout/critic和训练都计费；过程标签或正常探索不可靠时保可信outcome、较弱惩罚和独立trace审核，不由更短推理认证更真或fully-async训练已成立。
<!-- source-family:SF-2025-ARXIV-2510-22543 -->

### 本人注

- `SF-2025-ARXIV-2510-22543` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22543v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。已选reward正文中Video-VER之后、正负advantage clipping之前；先改变reward人口再解释更新路径，不章末追加，不采用first-error为内部真值。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

已选reward正文中Video-VER之后、正负advantage clipping之前；先改变reward人口再解释更新路径，不章末追加，不采用first-error为内部真值。

### 当前完整必要邻接

```markdown
过程奖励还可由两层不同权限的模型生产：离线视觉teacher在视频、问题和已知正确答案下生成支持描述，文本judge再比较该描述与当前推理，只有答案本已正确且被判引用证据时增加reward。[Video-VER的受限分支](https://arxiv.org/html/2510.06077v1#S4)把训练证据与部署policy分离，却不让文字引用成为独立像素验证；原judge只见描述和trace，GT条件teacher也可能为答案事后编造依据。Binary判分不保证错误teacher必得零，题目条件caption胜过generic也不排语言线索或信息权限的混杂。更多frame、CoT或证据细化仍有任务反退，原采帧缺失更不能由奖励补回。全部离线teacher/答案制备、judge、SFT/rollout/reference、长度控制及独立原帧/事实和终局质量回归均付费，test不带teacher不等全费更低。证据、judge或净质量失配时，保原DA/短CoT、原视频密集回读与可信outcome，不由matching text或更长reasoning批准全事实grounding、因果推理或无幻觉。

<!-- source-family:SF-2025-ARXIV-2510-06077 -->

### 正负 Advantage 不必共享同一 Clipping Contract

对正负 advantage 使用同一旧策略 ratio，优点是保守且容易解释；但它也把“继续放大已变好的动作”和“阻止坏动作
突然变得过小”绑定在同一 trust-region 规则中。一条实验性分支让正 advantage 使用当前 policy 的 detached
probability 作为分母：前向 ratio 数值为 1，但分母停止梯度，因此梯度仍推动当前 token probability；负 advantage
继续使用 behavior-policy ratio 与 clipping，KL、rollout provenance 和 freshness 约束保持不变。

```text
A > 0: current probability / stop_gradient(current probability)
A < 0: current probability / behavior probability, with clipping
```

它把 exploration 与 stability 分成两条控制路径，却会削弱正样本相对 behavior policy 的显式边界，并让 stale rollout、
极小概率 token 和长度归一化更敏感。对分布漂移小、方差控制优先或 freshness 难保证的训练，标准对称 clipping 仍是
更稳妥基线；作者结果只支持其特定 RL workload，不构成通用替代。
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-21884` — primary `arXiv:2606.21884v1`；exact-v1 URL=`https://arxiv.org/html/2606.21884v1`；Method=`https://arxiv.org/html/2606.21884v1 — §4 Method: Solver-Grounded Synthetic CoT and the Experiment Ladder`；Evaluation=`https://arxiv.org/html/2606.21884v1 — §5 Results; §6 Anatomy of the Failures`；Non-proof=`https://arxiv.org/html/2606.21884v1 — §8.2 Threats to validity; §10 Limitations`。
- `SF-2026-ARXIV-2606-22043` — primary `arXiv:2606.22043v1`；exact-v1 URL=`https://arxiv.org/html/2606.22043v1`；Method=`https://arxiv.org/html/2606.22043v1 — §2 Setup — Task and model; Visual-hacking diagnostic (VHS); Held-out OOD evaluation; Trajectory fleet`；Evaluation=`https://arxiv.org/html/2606.22043v1 — §3 Onset is real and seed-robust; §4 Reward strength: a monotone dose–response with formation–reversal asymmetry; §5 A critical intervention window; §6 What changes inside: representation probe; Appendix A Reproducibility and diagnostic details`；Non-proof=`https://arxiv.org/html/2606.22043v1 — §8 Discussion and limitations — Limitations`。
- `SF-2026-ARXIV-2606-22164` — primary `arXiv:2606.22164v1`；exact-v1 URL=`https://arxiv.org/html/2606.22164v1`；Method=`https://arxiv.org/html/2606.22164v1 — §2 Preliminaries; §3 The Signal Dilution Problem`；Evaluation=`https://arxiv.org/html/2606.22164v1 — §4 Experimental Setup; §5 Results`；Non-proof=`https://arxiv.org/html/2606.22164v1 — §7 Discussion; Appendix A assumptions; Appendix B Diluted Doors`。
<!-- daily-20260621:train-grpo:end -->

同一 prompt、同一 role、单个 final-answer verifier 时，sequence-level reward 简洁且可复算；当 trajectory
包含多个角色、多个目标、草稿—修订阶段或可迁移中间产物时，把一个标量复制到全部 tokens 会混合不同
conditional state。演进方向不是无条件增加 reward model，而是先让样本身份跟上真正的决策边界：
```

## 22641

文件：`books/part-05-inference-system/48-speculative-decoding.md`

插入于唯一锚点前：`MTP 把候选预测头放进目标模型训练或 checkpoint，省去寻找另一套小模型并提高架构一致性；`

### 完整新增正文

另一种同模型分支让浅层直接承担draft，但先冻结已适配好的完整backbone，再训练小imitation网络将浅层hidden映到末层附近的表征，复用原LM head；浅层KV则供full verifier继续执行。[受限VLM自投机对照](https://arxiv.org/html/2510.22641v1)用末四层融合及CE/cosine/KD改善proposal，保住目标权重并不让浅层预测本身正确。Greedy逐token验证/首错纠正仍决定commit，sampling分布保持须另证，拒绝后provisional KV也须回收。Imitation训练、共享状态管理、起草与完整验证全计费；短一两token回答难摊销，平均per-token倍率不是tail-SLO。接口、接受率或净收益失配时保普通target、独立drafter或较保守层数，不因来自同一backbone就省略验证。
<!-- source-family:SF-2025-ARXIV-2510-22641 -->

### 本人注

- `SF-2025-ARXIV-2510-22641` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22641v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增冻结target/浅层imitation及共享KV的替代分支，置已有EAGLE到MTP之间；与既有nativeMTP及deepfeature读取不合并。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

### 自读注

新增冻结target/浅层imitation及共享KV的替代分支，置已有EAGLE到MTP之间；与既有nativeMTP及deepfeature读取不合并。

### 当前完整必要邻接

```markdown
多模态 target 的不同深度还可能保留不同类型的条件，固定抽取少数层未必最适合容量较小的 drafter。一个替代接口把同一 token 在各 target 层的只读特征作为一组 key/value，让跨 token 共享的 learned queries 沿深度轴聚合，再经独立的中间 decoder 转成 draft 输入；随后才由轻量 draft 层递推候选。这不是扩大时间历史，也不把聚合结果当作已验证的 target KV。[受限多模态分支](https://arxiv.org/html/2509.18824v1#S3.SS1)还用 residual、零初始化和 target 分布加硬标签监督来降低接口适配难度，但接受长度只说明 proposal 更容易被消费，不证明每个组件独立有效或任意采样分布不变。全部层特征的提取、临时存储与搬运、中间聚合、draft 训练和验证仍须计费，target 版本、层集合或模态输入改变时要重验接口；生成分支换成少步模型后，即使恢复原理解权重，变化的图像及 latent 上下文也不能自动继承原质量。接受量、状态兼容或净收益不合适时，保留固定少数层融合、较小独立 drafter 或普通 target decoding，最终输出与 prefix 提交仍由原验证合同决定。

<!-- source-family:SF-2025-ARXIV-2509-18824 -->

MTP 把候选预测头放进目标模型训练或 checkpoint，省去寻找另一套小模型并提高架构一致性；
旧的独立 drafter 仍适合没有原生 MTP head、需要独立更新或跨 runtime 复用的 target。两者都
必须由 full target verification 决定 accepted prefix，不能因为 drafter “来自 target”就绕过
sampling correctness。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-36590:start -->
同模型复用还有一条不同于 early exit 或新增 MTP head 的分支：完整 verification 已为前缀产生深层 KV，下一轮只让末端薄层读取这份 cache，并把最新 token 的 raw embedding 直接送入薄层起草，避免重新执行大多数前层。SEED 在所测模型中使用最后两层；这里的“cross-attention”只是标准 self-attention 读取缓存的描述，不是新加的 encoder–decoder 模块。浅输入起草态仍属 provisional，完整 verifier 只提交 accepted prefix 对应的深层状态，拒绝后的候选及 cache 不能进入下一轮 committed prefix。

这也不是 training-free 跳层：AR cross-entropy 与 block-causal speculative loss 联合训练，才让薄层适应“已验证深前缀 + 当前浅输入”。Verification authority 因而是重新训练后的 target，不保证保持原 checkpoint 分布。薄层加深能改善候选却增加 draft 成本；深表征 probe 是动机而非因果证明。Qwen3-1.7B/4B-Base、逐任务 SFT、greedy、单 A6000 的实验不证明大模型或生产并发收益，代码未复现；无法重训、兼容身份变化或收益不足时，仍选独立 drafter、原生 MTP 或普通 target decoding。[exact-v1 §4.1–4.3、§5、AppA](https://arxiv.org/html/2609.36590v1)
<!-- semantic-body-binding:SF-2026-ARXIV-2609-36590:end -->

候选来源还可以更轻：不训练独立 drafter，也不新增原生 MTP head，而是从 target model 的 hidden
state 在 embedding space 探测未来 token，再交给 target exact verification。它把 proposal-source
演进补成三条并列分支：

```text
independent draft checkpoint
| target-coupled learned MTP head
| training-free latent / embedding probe
→ exact target verification
```
```

### Review notes邻接

```markdown
## Review notes

- `SF-2026-ARXIV-2606-19755`，Jun20补Jun19；消费sole§97唯一exact-v1必要，2+2+2=6，actualCh48仲裁/CLP完整前链与WISV/分布contract后链、旧trace和Ch72权限交接已读，仅同forward boundary安全-v-末端质量/风险慢路差额深入并纠正trace。保head通过非安全、generation非effect回滚、良性/对抗成本与质量反退/全费ND；未核实现/复现，不授targetlaw/生产安全，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2025-ARXIV-2510-19779` — Volta，Daily2025-10-24补Oct23；[AdaSPEC exact-v1](https://arxiv.org/html/2510.19779v1)§3/4.1–4.6/5/A.2，2+1+3=6，采用reference loss-gap选监督位置及完整训练成本。保RKL/TVD反退、validation epoch搜索与单A100/greedy局部墙钟，不把acceptance当SLO。未核代码/复现；PRE/SAVE/selfread/solePOST只以本日canonical实际记录为准。
```


