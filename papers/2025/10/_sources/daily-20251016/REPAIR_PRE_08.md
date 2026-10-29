# 第八包：更新规则与联邦适配三个精确差额

仅整体PRE，未SAVE。本轮Books上下文/完整ROADMAP有效复用；writer实际读Ch28更新/optimizer状态及完整SGTM前后、Ch30聚合相关完整段及相邻Ch27/29/31交接。必要首次审阅归Cicero R18/R19/R49，writer只消费实际证据和比较owner，不回填成自己第一Methods。三项正文/独立marker/本人注整体审，无全章锁，未核代码/复现。

## 12402 CWD / 2+1+3=6 / TRAIN-PRETRAINING Ch28

R18/19完整必要Alg1–2/§3.1–4/§5表2、4及Remark2：按优化器update与weight同号mask decay，momentum mask非rawgradient；随机同稀疏率反退。只采decay适用坐标与真实objective更新分责，不采有限噪声固定batch精确驻点或不变收敛率、免调参/零成本。

actual Ch28已有SGTM前向/样本梯度mask与optimizer一二阶统计顺序，但未把**decoupled decay自己的写入支集**独立出来。唯一插位在完整`eta_s 是第s步...Adam 类optimizer...训练状态远大于单份权重。`之后、完整`同一训练步还可以按数据标签改变参数的学习责任...`（SGTM首段）之前；不插SGTM两段之间。上方更新代码/Adam段、下方SGTM完整两段及其后归一顺序两段已实读。

正文：

优化器给出的任务更新与把权重拉向零的decay，也不必在全部坐标上始终相加。可按本步更新统计与当前weight的方向关系，只让指定坐标接受decay，保留原任务更新路径；[一条受限条件衰减分支](https://arxiv.org/html/2510.12402v1#S3)由此把“在哪里正则”与“怎样根据梯度学习”分开，不是将不利坐标的任务梯度一并删掉。Mask读取raw gradient还是含历史的momentum会改变规则，参数、optimizer状态、mask时点与衰减系数须共同保存；相同稀疏率的随机mask也不等同这份方向条件。连续时间的驻点解释不能直接保证有限步、带噪Adam训练达到原loss的精确驻点，学习率、batch噪声和光滑/有界条件仍需核；沿用一份系数的有限实验也不是任意任务免调参。Mask计算、状态维护、完整训练和新旧任务/匹配预算回归均付费；方向统计、数值条件或质量失配时，保留普通AdamW/固定decay与独立调参，不由少量被衰减坐标或更低训练loss批准全局收敛、能力保持和净加速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12402 -->`

本人末注：

- `SF-2025-ARXIV-2510-12402` — Herschel，Daily2025-10-16补Oct15；整体消费Cicero R18/19 exact-v1 Alg1–2/§3.1–4/§5表2、4/Remark2首次必要，2+1+3=6，decay支集与任务update/历史统计分责差额深入。保随机mask反侧、eta/batch噪声条件及全费，不采固定batch精确驻点/完整连续理论或免调参。未第二Methods/代码/复现；整体PRE/真实SAVE/完整自读/solePOST仅本日canonical后到真实层。

## 12078 FedLoDrop / 2+2+2=6 / TRAIN-LORA Ch30

消费R19首次必要II-B/C/III-B/V-B/C/VI-A表I；mask作用A输入列与B输出行，不是rank删方向，server已知mask补零聚合因子，不授无交叉项。PHS资源代理需原条件，B&B最坏指数、MRPC/STS与高dropout反退、重建/基座计算/通信全部费保留，不采隐私或原理论完整recipe。

actual Ch30完整SF2510-04601段/独立marker已有稀疏交换→各端BA重建→dense平均；下方Fed-PLoRA完整段是rank项子集训而初始完整函数。这两条都没有承担**固定rank的输入/输出坐标mask及零填因子聚合**。唯一插位在SF2510-04601独立marker之后、完整`异构 rank 还可用另一种分支分开...Fed-PLoRA...`之前。上方共识projector两段、完整04601、下方完整Fed-PLoRA和个性化历史增量段已读。

正文：

端侧资源不同时，还可保持低秩方向数而缩小因子的输入列和输出行，将训练/交换支集限制在各client的坐标mask内；这与删掉若干rank-one项是两种预算。[受限联邦dropout分支](https://arxiv.org/html/2510.12078v1)让server按已知位置补零再聚合因子，补齐shape却不恢复未训练信息，也不使平均A、平均B的乘积等于各端BA的平均。Mask、因子坐标、参与人口、优化状态和资源选择须共同绑定，分别验端侧训练、聚合后的实际更新与各client质量，而不是把代理资源最优当任务最优或隐私证明。较大dropout和部分任务仍会退步，资源分配的光滑/局部相似条件也不授任意non-IID泛化。全部基座前反向、mask/补零、资源求解、因子驻留与真实通信和独立回归均付费；mask支持、聚合误差或净预算失配时，保留同构adapter、更低dropout、独立适配或逐端完整delta聚合，不由少上传元素批准无损联邦训练。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12078 -->`

本人末注：

- `SF-2025-ARXIV-2510-12078` — Herschel，Daily2025-10-16补Oct15；整体消费Cicero R19 exact-v1 II-B/C/III-B/V-B/C/VI-A表I首次必要，2+2+2=6，A输入列/B输出行mask与零填因子聚合差额深入。保非rank剪枝/乘积交叉项、PHS条件、指数求解/任务反退及全费，不采non-IID普遍保证/隐私或精确recipe。未第二Methods/代码/复现；整体PRE/SAVE/完整自读/solePOST只本日canonical实际层。

## 12741 FedOPAL / 2+1+2=5 / TRAIN-LORA Ch30

消费R49首次必要§2/3/4/B；两adapter同时训只global FedAvg，A正交罚与feature abs-cos是不同软约束，非BA正交/语义或隐私独立。印式归约与零范数未闭不补投影recipe，ViTtiny/静态6或5clients/患者人口非patch独立，部分client反退/完整双路训练通信费保留。

actual Ch30当前完整个性化历史增量段（SF2509-12697）为各client保上次聚合base再按peer增量相似混合，下方SF2509-15087是指定expert更新/读取支持集；没有**本地personal路径保留、global路径唯一上传与双层软分离**这份状态权限。唯一插位在完整Fed-PLoRA段之后、`参与者也不一定每轮回到同一份全局模型...`之前；与上项FedLoDrop隔着完整Fed-PLoRA，不占同一gap，不改任何旧完整段/marker。

正文：

个性化也可保留两份同时学习的增量，而不让每份本地适配都进入全局平均：冻结base，分别维护global与personal LoRA，本端前向共同消费两者，通信只聚合global路径、personal状态留本端。[受限双adapter分支](https://arxiv.org/html/2510.12741v1#S3)还在单因子坐标与输出表示上分别加软分离约束；因子接近正交不等完整BA更新正交，feature相似度低也不证明功能、信息或隐私独立，不能由本地驻留取得保密保证。应绑定base、两份adapter/optimizer、参与者与轮次及各软罚定义，分别验共享收益、个人回归和组合consumer，而不只看跨client平均。有限静态参与实验里仍没有所有client共同最佳，未闭的归约与零范数规则也不补成hard projection。双增量的前反向、personal常驻、全局交换、选参和独立各端验收均付费；共享/本地分工、数值或质量失配时，保留单global adapter、独立personal适配或完整本地基线，不由少通信参数和软正交批准普遍解耦与任意新client迁移。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12741 -->`

本人末注：

- `SF-2025-ARXIV-2510-12741` — Herschel，Daily2025-10-16补Oct15；整体消费Cicero R49 exact-v1 §2–4/B首次必要，2+1+2=5，global/personal双增量的上传权限与因子/feature软罚分责差额深入。保staticclient/患者人口、未闭归约/零范数、逐端反退及全费，不采BA硬正交/信息隐私独立或任意新client。未第二Methods/代码/复现；整体PRE/真实SAVE/完整自读/solePOST只本日canonical后到真实层。
