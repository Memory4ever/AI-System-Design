# Dec20 Qwen-Image-Layered release：Source / owner / PRE

## 1. 准入、日期、评分与必要范围

官方原[目录/发布路由](https://qwen.ai/blog?id=qwen-image-layered)本日两真实元数据响应及[仓库News](https://github.com/QwenLM/Qwen-Image-Layered)明确Dec19 release，细节见SUP_SOURCES§1；paper first不由README Dec18自述或v1的Dec17submitted补造。Newton§4原repo层已实际校准窄准入：平面整图编辑牵连无关内容 → image-to-multi-RGBA分解后选择层操作 → 可编辑存储接口与分解/合成质量分别验收。不以宣传“fundamentally/infinite”入选。

评分拟2+1+2=5：重要的可变层分解/输入状态机制；单生成组件，不把可联想到的所有编辑工具抬Reach；可复用的表示/条件/验收边界。必要具体长期缺口受影响深入。release与同家族2512.15603不加家族；未运行模型/代码、未复现、不授速度或生产SLO。

作者本次实际读[exact-v1](https://arxiv.org/html/2512.15603v1)完整题摘、§3.1–3.3、§4.1–4.3/T1–3、§4.4/5及当前repo Note/部署/Showcase。官方Blog动态壳无正文不冒读到。论文支持方法，不把论文submitted当release日期，也不因此扩成当日论文首公开。

## 2. 证据与直接反侧

RGBA-VAE同一latent接口处理RGB与RGBA，RGB alpha置1、首尾卷积扩4通道，新增权重零/alpha bias1初始化；逐层编码，不沿层轴压缩。VLD-MMDiT对clean输入图latent和待生成各层拼接attention，以新增layer位置轴区分，输入条件layer index=-1、生成层0起。训练先适配RGBA，再text-to-multi-RGBA，末阶段加入image condition做I2L，不把发布I2L权重当全部T2L能力。

PSD提取/过滤、去不贡献层、合并空间不重叠层及MLLM整体caption改变训练人口和层定义，不是唯一“真实语义层”标签。论文训练最大20层，不能授递归无限质量或费用。§4.3的Crello评价再finetune该训练集，按order-aware DTW且允许邻层合并消解多解性；RGB L1只按GT alpha加权，与alpha soft-IoU分账。逐步加入L/R/M的消融不是全因子/相同总训练费下独立因果证明；RGBA重建比较还用不同base，不能独归codec。§4.4编辑多为定性/手工层操作，不证明所有复杂语义分解/遮挡补全都正确。

当前repo明确prompt描述整体输入含遮挡内容，不是逐层语义指令；I2L发布权重的T2L有限。固定其它层文件只隔离存储写入，不保证新合成图每像素不变、alpha/遮挡正确或语义保持。RGBA codec、多层token/attention、PSD处理、多阶段训练、采样和独立层/合成/编辑验证全部付费；未披露端到端延迟/硬件预算不补造。

## 3. 当前owner比较与完整锚点

唯一owner拟 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。作者已实际读当前120–155完整邻接，Newton§4实际读120–152；现两段LaDe2603.17965处理合成图/多RGBA共同去噪、层文字与冻结条件、分桶packing和训练/测试层域及合成/编辑分验。可承载可编辑状态的通用边界，但没有本项“共享RGB/RGBA latent＋clean输入独立layer index＋I2L发布权重不授逐层文字控制”的具体分工，不因同层主题而全判已有覆盖。Ch23决定representation/codec，Ch24承载生成/条件/消费；不再写Ch23重复codec方法。

最小插入拟在完整LaDe第二段末“不要用联合生成名称替代可编辑性和完整成本证据。”后；下完整段以“迭代路径的验收还不能只看沿途点的density：”开头，至2602.22122 family marker。两完整段作者已实际读，位置保持现有LaDe原文/marker不动。root协调实际当前差额后才能授窄位。

## 4. 逐字PRE / 本人末note

逐字单自然段草案：

既有平面图像也可先转为可编辑层，而不要求用户给每层文字命令。[Qwen-Image-Layered的受限分解路径](https://arxiv.org/html/2512.15603v1#S3)以共享RGBA codec编码输入图与各透明层，不沿层轴压缩；共同Attention读取干净输入和待生成层，再用独立layer位置区分条件图与输出层。它把编辑对象从整张重新采样的图改为可选层，却不让分层存储自动认证语义、遮挡补全或alpha合成正确：发布I2L权重的整体caption并非逐层控制，论文Crello评价还经过该域finetune、DTW对齐与允许邻层合并，编辑展示主要是定性操作。各层文件保持不变也不保证重新合成后的可见像素不变；RGBA适配、多层token/Attention、PSD制备、多阶段训练及采样/编辑验证都付费，递归展示不授无限层质量或成本保证。仅需平面成品或层结构不可核时，保留原生成/局部mask编辑与较少固定层，分别验收分解、合成和目标编辑结果。

逐字本人末note草案：

- `SF-2025-QWEN-IMAGE-LAYERED` — Daily2025-12-20补Dec19 release；[exact-v1](https://arxiv.org/html/2512.15603v1)§3–4.4/T1–3及[官方repo Note](https://github.com/QwenLM/Qwen-Image-Layered)，2+1+2=5，I2L条件/层存储与验收具体缺口深入。保整体caption非逐层命令、Crello finetune/DTW/合并、定性编辑/递归边界与全费，不授无限层、唯一语义分解或合成一致保证。Boyle作者；实际Source/PRE及写后状态仅按随后真实发生记录，未核代码/复现，不授DAY。

本项交Newton实际必要Source/评分/owner/PRE；没有root写锁，不写Books、不预POST或已整合。作者继续其余本日有限准入/date/six，不等全源才交单篇。

## 5. root3窄许可后真实保存 / 作者完整顺读

Newton6已实际Source/评分5/唯一owner/逐字PRE通过；root3实际完整Ch24 120–158及Ch25边界后授本单段和本人note窄位。作者实时复看完整LaDe两段、后一density完整段及末前注，实际unstaged6/cached40与root基线927c0a8一致，外部DepthVAR正文/末注不动。随后apply_patch只保存§4逐字单自然段及本人末note，未增标题/marker、未改LaDe或他文。

作者已实际全文顺读保存后147–157：LaDe完整两段→Qwen新段→完整density段至marker及DDPM下节开头；末前注及本人note全文实际顺读。新增正文逐句同PRE，保codec不沿层压缩、clean条件/输出位置、整体caption/I2L与有限Crello/DTW/合并、定性/递归限制及全费回退，不将层存储隔离当可见像素/语义保证。两层diffcheck exit0，实际unstaged10/cached40，净本人4add/0del；未stage/commit/push或写State/index/其它书。

随后已发生：Newton11实际完整新增/两侧/本人note POST通过，root4实际完整读保存包/Newton11/当前新段/完整两邻接/本人注及重做两层检查，已接纳整合并释放该窄位。作者仅同步本人note与本保存包的已有行政状态，不改正文/他注，不再Source/PRE/POST循环；三项新正文实际整合已闭合，当前无本项余锁，不授DAY。
