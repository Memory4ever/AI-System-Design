# Sep20补Sep19：QuizRank与AutoEdit首次有限必要证据

作者218明确两首次必要域未开始/无CORE或请求在途，root本轮明确接受后唯一capture/首备。AB123/联合日180/各2+1+2=5有效复用，不第三准入、日期或评分。Aristotle唯一另一角色回具名必要原域实际采用后才闭合此Source层，Einstein只复用已闭角色链，不第三Methods。未给本两项Books判断、写位或DAY。

## 原件与实际范围

- [QuizRank exact-v1](https://arxiv.org/html/2509.15059v1)：[raw](ROOT_CORE_QUIZRANK_15059_20261024.raw)/[request](ROOT_CORE_QUIZRANK_15059_20261024.request.json)，GET 2026-10-24T07:23:55.055433Z～07:23:57.869073Z/200/exit0，274527B，SHA256 `328de843bc80869f56f1770fddfaf52a66c864d08eddb59278ee921d74f1a4f2`。实际完整Design全部四步、Evaluation全部六组/整T1/F2–6文字caption、Discussion/Limitations/Conclusions与A三份必要prompt。未读全部relatedwork、B模型长推理case或图像素/代码/复现，不以解释文本认证内部推理忠实。
- [AutoEdit exact-v1](https://arxiv.org/html/2509.15031v1)：[raw](ROOT_CORE_AUTOEDIT_15031_20261024.raw)/[request](ROOT_CORE_AUTOEDIT_15031_20261024.request.json)，GET 2026-10-24T07:25:09.007179Z～07:25:13.853678Z/200/exit0，356902B，SHA256 `815a564023cd83241e72a5a0673d2917ba7bc9e752d80b9e7896ab9141dd0475`。实际完整§3.2/式1–4与四子节、§4.1–4.4/整T1–6/F3–5文字caption，A完整离散超参与prior、B整T7/随附T8、D指标、F两完整算法、G限制与H人评。未核全部样例/图像素、C/E/I完整扩展、实现或复现；不因可选附件未读造必要外阻。

## QuizRank15059：把整体图像判断拆成可回答性，不等于测出了学习增益

### producer、读出与排序

从文章的视觉属性生成带答案的MCQ，同一组题分别交VLM看不同候选图，按答对比例排序；保留image×question矩阵可支持发现信息缺口。它评的是给定题/选项/答案和模型的可回答性，不是直接优化审美、图像真实身份或读者长期理解。

初始题隐去概念名、要求只用可见信息并允许无法回答，但prompt与输出解释不能强制模型忘掉已有知识或证明视觉因果。Wikipedia生成的correct_answer也不是独立可见事实标注，选项/描述可泄漏概念。无图、换图和text-only等独立控制未形成完整识别；共同提高分数底线也**不保证排名不变**，图像识别与先验会对不同图产生不同作用。

若target与distractor基础分接近，再从两文章差异生成contrastive问题。Design说仅相似distractor才触发，Data Methods写差<2，结果写差<=2；边界不擅统一。题目分母随concept/文章长度而变，contrastive更换了测量题集，不能把新分数变化直接归为图像或模型能力提升。加权题、相关题聚类、最优图组是future，不冒已实现优化/完整覆盖。

### 样本、直接对照与反侧

94原concept中去5非视觉/太短，89每类三正确图+一相似错类图，且每图已被Wikipedia某语言文章使用；这是精选英文候选，不是所有开放图片。GPT4o作出题与VLM评分，Llama4Scout17B复测；精确snapshot仅8对图记忆控制明确gpt4o-2024-11-20，其余sampling/temp/完整费用ND，不按厂牌授独立性。

40concept human评价，Methods称320人、每人5concept、每image2人，后者40x4x2=320是image-level评价次数而非与前两句兼容的总人次；未交完整分配/去重/排除流，不能补成1600或320独立观测。T1 n120/40是image聚合，concept、共享题及每人多题相关，不当每问答独立样本。Pearson r约.6125/.613是有限总体相关，不是逐concept最优图选择正确率、校准或因果教学收益。Llama与GPT32/40 strong、26/40 perfect仍有8concept非strong，不授所有模型一致/新模型必改善。

非distractor human均.44对VLM.66、distractor.26/.30保实际population，不从VLM分更高推人类学习增益或真实推理更好。89concept基础57correct>distractor、26平、6反；51触发contrastive后34较好/16平/1反仍未完全分离，且按原分选择/重出题而无独立human复验该全部新题人口，不称全部稳健。

8concept新旧图控制只按Commons上传前2019-08-01与后2024-08-01区分，4平/1旧较好/3新较好各一题。上传晚不证明图此前未在别处存在或语义未被预训，样本少/未显著不认证无记忆或等价；原文也承认更强grounding需模型透明/架构约束。人工选“视觉内容相近”不是严格配对无混杂。

13concept各20图的popularity与按类zscore weak趋势，不能由一个未经独立验证的QuizRank分定义证明Wikipedia既有选择错误。非零类内方差只说明会区分，不证明区别正确；6题对10题近.9 Spearman是对同一十题reference的内部rank稳定，不是六题完整/真值或统一最优。真图内容、候选、题集/答案、无法回答人口、评分与最终编辑决定应分责。

全部文章制备/出题与contrastive重出题、每图每题VLM/解释、失败与弃选、人工320人口/付费$1–1.25的实际任务分配、部署复验均付费；未给API token、成本/延迟/并发或净SLO，不由“减少问题”授端到端省费。范围外/稀少图或题不可靠时保原图/人工编辑、直接图文与原证据检查，不把自评分替最终教学/真实性裁决。原5/局部可回答性接口正侧与全部限制保留，owner后续另做。

## AutoEdit15031：训练轻量控制器摊销超参选择，不是每张图无代价求全局最优

### 状态、动作与两阶段

给定冻结编辑器/denoiser，把每个denoising step的超参选择作为action：source/edit prompt选择、attention替换bit、离散attention weight或CFG等。网络读当前latent、t及source/edit条件的U-Net encoder特征，K个head产动作；value另输出scalar。只训练新增层，改变的是**采样控制器**，不是用PPO重训生成主干或优化所有图像任务。

Phase1从预设合理范围采完整超参轨迹，用逐step CE模仿；Phase2用最终编辑图的背景MSE/CLIP或LVLM proxy reward、固定Phase1 KL和PPO更新actor/value。终态reward的credit须由value/advantage构造，不能把它说每步独立即时真值。prior缩探索不是可证明覆盖最优，也不是总state空间被准确算成N^T；N^T只是离散序列组合的粗类比，不是连续latent状态数。

原式s=(x_t,t)省prompts，network实际补入；完整editing环境还依source、mask、inversion和缓存，应保条件身份，不据简写授完整Markov充分性。逐step独立binary开关能表达比单一threshold更广的schedule；“第一次选edit定义r”不自动限制之后不切回source。A prior attention ratio[.2,.6]与主文[.2,.8]、inversion范围例子不完全一致，不补统一代码recipe。

F算法把同一终态R写进每步delta，未解释terminal-only分配与potential dense等价；policy ratio省已采动作索引、old-policy冻结/求各head联合概率和符号需实际实现闭合，不能照印式发布完整PPO。F中beta=.02为KL，reward又beta30，gamma .999为discount而D又gamma为MSE权重，须分别解释，不把同名量混为一个。D写Rnoedit=1−gamma*MSE后说alpha5最佳，系数对应未闭；MSE单位/是否按全图或mask面积归一影响尺度，也不私补。

### 对照、停止与代价

训练源EditBench经ChatGPT source/edit prompt与SAM mask制备2000，评PieBench700；精确split去重/ChatGPT snapshot、mask质量和完整人工验证未披。T50、Adam5e-5、reward alpha=beta30、KL.02；训练曲线前3000episode在2500后回退，选择2500/约15epochs是此reward观察，不是PPO已收敛或所有模型最优证明。主文无完整GPU/precision/batch/seedCI/总训练时长，不能从Table6推定其他测试环境。

T1 DDIM/DDPM背景更好同时CLIP edited/whole下降，SDXL也23.0→22.9/27.11→26.7，不能把“CLIP不敏感”自动洗掉目标退步。T2两阶段对P2only的CLIP22.5/25.8仍低23.2/26.3，虽背景/总reward好；T3 beta40背景更好而CLIP更低，30是设定的折中，非同一预算下Pareto全局最优。T4 LVLMreward提高LLMscore还可能更低CLIP，reward与评价同源；QwenVL2.5-7B yes/no与背景MSE合分不是独立人类质量或每个局部像素真值。H50人/30组/82.78%偏好是有限用户实验，未给完整候选挑选、有效响应与不确定性/人口，不外推所有编辑。

T5 AutoEdit与有限候选oracle3次reward接近，DDIM6.09仍低3次6.11/Optimal6.17，其他方法亦低表列Optimal；“Optimal”只在所搜设置和proxy中，不是所有schedule的全局最优、真实质量或普遍收敛。baseline正文说取最高reward设置，qualitative又说default，应保各自协议，不把图例当同oracle基线。各编辑法/骨干的适配结果不证明同一未再训policy跨栈zero-shot迁移。

T6 20.89→21.03ms是所测single image-prompt U-Net操作点，非完整50step、inversion/VAE/搜索/训练/评判或在线请求；87.1M−86M=1.1M、相对86M约1.28%，与表+0.6%不符，时间约.67%可近似，两个百分比不能互借。每步两个条件encoder特征、actor/value/reference、实际可复用feature和驻留身份须分别核；O(T)随步数仅在单步shape/actionspace固定时计调用阶，不授每步O(1)运行费/几乎免费。Phase1/2所有inversion、全部rollout、reward前向、搜索/失败和每种编辑器适配费用应按真实复用次数摊销。

T7 flow局部结果保留，Fireflow whole25.2持平，不据此授任意flow；G明确底层编辑器做不了的任务控制器同样失败。旧固定schedule/合理prior/有限grid或随机搜索仍可共存：目标/条件/代理失配、校准或摊销不合时回原编辑器/人工参数及独立实际质量检查，不让更高reward或“optimal”名称签无损/零风险/净SLO。原5不降删，具体owner由writer后续新层核。

## 停点与交接

两首次有限必要首备已完成，无root GET/exec在途。支持、直接控制、关键反侧与全费足停；Aristotle只回上述必要原域作唯一非准备者实际采用，Einstein随后只角色复用，不第三必要/PPO/统计或扩所有图/案例。当前未核实现/复现、未给Books位或日级验收；可执行普通层继续。
