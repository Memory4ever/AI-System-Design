# 12/09 作者侧筛选与外部保留

检查时间：2026-10-02T18:03:46+08:00。只处理本日窗口；以下潜在材料不等于确定落窗候选，不评分、不正面采用。

## 普通入口收束

在 SOURCE_SCAN 初始入口之外，实际补读：Kimi changelog 全文最新 11/06 后向到 2024/04；MiniMax 中文目录 13 条由 2026/08 向下到 2025/01，目标邻接为 12/23 M2.1 与 10/27 M2；Agent llms.txt 当前目录，以及所链 techblog.md（网页工具不可访问）；Seed 官方组织固定六仓库和当前十仓库。Hunyuan 浏览器 Research 的“全部”实际渲染十一条，最早 2026/02/03，页底无分页；Seed 目录第一页当前 1–20/242、13 页，材料为 2026/08/18～05/14，浏览器进入目录超时且会话重置。不再重复同一失败接口。

ERNIE 12/09 Preview 排行说明实际核心是名次/评分，无新架构、训练或对照协议说明，按贡献关闭；日字段无时区，不用于认领本窗。DeepSeek 正式 V3.2 原文 12/01 在窗外；SGLang 14691 已按主线程官方 API 原字段关闭本日触发，归 12/10。

GLM-4.6V 与 AutoGLM 博客 HTTP 原页尝试提取 date/publish/time 元数据及 JSON-LD，未取得带时区的历史公开字段。GLM-V/Open-AutoGLM 官方 GitHub releases API 分别返回空列表，只表示没有 release 条目，不能证明没有发布。GLM-V 精确历史 README 已取得；Open-AutoGLM 当前 README 已读核心（VLM screenshot、ADB action、敏感确认、人类接管），当前新增 iOS/Harmony/Midscene 等内容不能当 12/08 artifact。日期缺口因此隔离而非用 commit 或日标签补时间。

## arXiv 有界原始补检

主题覆盖 language/foundation model、Transformer/MoE、训练/RL、inference/quantization/speculation、agent/retrieval/evaluation、multimodal/generative/world model/VLA。四组 `site:arxiv.org "2025-12-08"` 主题检索及四组 `"Submitted on 5 Dec 2025"` 辅助检索不能作公开批次证明，空响应不作零事件。

官方 2025-12 月列表实际读取的相关邻接段：CL 167–218；DC 25–40；LG 451–525；CV 601–675；RO 151–175；AR 26–50。另读早段 LG201–225、CV401–425、RO101–125、AR1–25 只作定位，较晚 AR51–75 亦不形成本窗事件。网页 Cache miss 时本机 HTTP 取得上述列表，不能泛称列表全部不可得。列表没有逐日公告标签，只恢复材料身份。宽列表不是逐项关闭队列；不把无关化学、生物、医学应用、遥感和经典控制标题转成全文库存。

## 完整题摘后保留的潜在贡献

下列每项均实际读精确 v1 完整题摘，原始链接统一为 `https://arxiv.org/abs/<ID>v1`。增量仅为待核验命题，不能与证据审阅或采用混同。新增题摘通过本机官方 abs HTTP 取得；轻量观察题摘页未见撤回说明，不据此保证全版本历史无变化。

| 精确 ID | 原文潜在增量及可能改变的选择 |
| --- | --- |
| 2512.05665 | ILVR：动态交错 latent cue 与 teacher 视觉目标选择，不等同静态输入压缩；方法与 Books 草案另记 |
| 2512.04746 | SignRoundV2：梯度与量化误差联合层敏感度、scale 搜索，改变量化预算分配 |
| 2512.04753 | EtCon：teacher-forcing 编辑与 AR rollout 的差异、受约束训练，改变训练轨迹选择 |
| 2512.05858 | persona 准确率反证：expert persona 无一致收益，低能力 persona 常下降；不能外推到语气用途 |
| 2512.05501 | SEA-Safeguard：英语/机器翻译不能代表本地安全规范的评价盲区 |
| 2512.05959 | M4-RAG：检索收益可能随模型规模转为损失，不能默认更多检索必然更好 |
| 2512.04987 | Nex-N1：层级配置、自然交互多样性与真实动态环境轨迹生成的 RL 环境机制 |
| 2512.05012 | CER：事实 rationale 与主观 hard-negative 的对比学习检索表示；临床评价不自动排除通用机制 |
| 2512.05033 | Arbitrage：按模型相对优势路由 semantic speculative verification，区别固定接受阈值 |
| 2512.05105 | SSB：同模型有上下文教师的解释分布监督裸题学生，区别仅结果奖励 |
| 2512.05318 | CoT Recipe：过量 meta-CoT 示例对低 CoT ICL 的反效果及混合控制 |
| 2512.05325 | LYNX：犹豫节点隐藏态 probe 与 split-conformal 提前退出，需核覆盖假设 |
| 2512.04545 | EvoEdit：潜在扰动增强与参数融合处理连续编辑遗忘 |
| 2512.04550 | AdmTree：信息密度切分、gist 与树形聚合压缩，而非只扩大 context |
| 2512.04555 | ADAPT：最差验证任务驱动的 meta-gradient 课程分布，改变固定采样 |
| 2512.04748 | Model Whisper：冻结模型、连续输入向量的测试时熵最小化适配 |
| 2512.04838 | DAMASHA：混合作者边界定位、对抗改写与人工交互的检测可靠性问题 |
| 2512.04844 | SSU：源语重要列冻结与无标注目标语适配的遗忘取舍 |
| 2512.04868 | SEAL：受限可执行核心语言、问题类型校准与分层反思的运行机制 |
| 2512.05331 | Pink Slime：已读2025.ranlp-1.128出版PDF并对读精确v1，攻击/重放/评价对应，未发现归档新增机制或纠错；旧公开论文后续归档关闭，见TARGETED_REPAIR |
| 2512.05379 | 作者匿名化：风格中和后自识别偏差可能恢复，不能把文字匿名化视为盲评保证 |
| 2512.05387 | SCRPO：自批评/修正生成训练偏好对，区别仅测试时反思 |
| 2512.05409 | SQ format：静态稀疏与量化联合格式需要对应硬件，不宣称现有 GPU 普遍加速 |
| 2512.05681 | 噪声标签：弱标注、阈值和语料漂移可能改变评价结论 |
| 2512.05700 | faith metric fusion：人类标注监督下的多指标融合，需核跨域独立有效性 |
| 2512.05732 | CICLe：conformal ICL 类别缩减在数据/不平衡条件下的验证边界 |
| 2512.05100 | FormatRL：结构树相似度、局部文本与结构错误面积分开计奖/评价 |
| 2512.06443 | VecLUT：跨并行 token 的 1→N 向量查表和 cache-aware 布局；提交较晚亦不能凭编号归日 |
| 2512.05542 | RoBoN：reward 与答案 agreement 驱动的在线多模型采样路由，区别单模型或均匀 portfolio |
| 2512.05591 | ERC：熵比双向软约束补充仅 sampled-action PPO clipping，改变全局探索漂移控制 |
| 2512.05865 | 稀疏后训练：损失约束下稀疏 attention 简化因果 circuit；不是直接计算加速证据 |
| 2512.05962 | Filtering：正确答案保相对概率的目标与 alpha divergence 控制精度/多样性 |
| 2512.05134 | InvarDiff：时间/层/模块 cache plan 与重采样纠漂，需核计划校准成本 |
| 2512.05145 | 自训练 VLM judge：预设质量层级筛选自生成 judge 轨迹，需核偏差闭环而非采用宣传 |
| 2512.05150 | TwinFlow：自对抗 flow 避免固定教师与附加 GAN；1-NFE 不等于端到端 100 倍提速 |
| 2512.05198 | PELC：VAE 全局耦合令线性 latent mask 不等价像素合成，通道权重加残差修正 |
| 2512.05385 | ShaRP：浅层因位置 bias/交互不足失效，因果 mask、去 bias 与去重联合选择 |
| 2512.05391 | LoC-Path：局部 merger、预训练 resampler 与路由压缩的通用视觉机制，非按医学标签排除 |
| 2512.05394 | SSVAE：重建质量之外的 latent 频谱与 channel eigenspectrum 影响 diffusion 可学性 |
| 2512.05422 | ParaUni：多层视觉语言特征并行融合及 layer-wise reward 调整 |
| 2512.05513 | Know-Show：回答语义与时空证据定位分离评价；细粒度选择和 timestamp 编码 |
| 2512.05546 | Conscious Gaze：视觉-文字交互感测触发中层 attention 控制，区别纯 logit 干预 |
| 2512.05564 | ProPhy：语义/局部物理专家与 VLM 对齐用于世界视频生成，不等于真实 dynamics 已成立 |
| 2512.05597 | Fast SceneScript：结构 MTP 的 confidence-guided self-speculation 和参数开销 |
| 2512.05651 | EXIF 自监督：camera-induced 表示与 one-class 检测，不把 metadata 视为来源认证 |
| 2512.05746 | HQ-DM：单 Hadamard 避免权重 outlier 放大并支持 INT convolution |
| 2512.05754 | USV：attention/token/step 联合稀疏优化，必须区分 denoising 与端到端收益 |
| 2512.05774 | AVP：query-conditioned 像素交互和证据充分性停止，不是完整预 caption 全视频 |
| 2512.05802 | CCVD：旧概念保留、task-aware adapter 聚合和区域噪声控制的持续视频定制 |
| 2512.05809 | World-model verifier 反证：random score 也降熵、空间断言及 imagined view 信息瓶颈 |
| 2512.05853 | VRSA：跨图序列聚合有害意图，单图/单步安全评价不能自动覆盖序列 |
| 2512.05693 | HiMoE-VLA：动作层级专家显式处理 embodiment/action/frequency 异构 |
| 2512.05430 | ArtistMus：固定1024 token预算下chunk/TopK、FT后context score退步与RAG指令失败，恢复局部反证，不外推音乐领域因果 |
| 2512.05580 | Bengali ToT：1024 cap、Groq API、final-answer-only设置下reasoning/shot收益不单调，8B ToT退步；Colab不等API后端硬件 |
| 2512.05747 | Classic Author GRPO：style提高而completeness退步、弱judge评分饱和/零方差及beta权衡，不是独立人类质量验证 |
| 2512.05372 | FedGMR：缺失坐标不应作为有效零平均、早期稀疏更新频率与晚期容量/时延权衡；test-set触发有泄漏风险，非生产验证 |

这些材料的公开归属均未授。v2 或后续发表不自动是本日重要修订，不混入 v1 题摘。ILVR与05858/05501/05959有root具体潜在校准，四项误关及FEEDBACK_C受影响集合另有Popper实际题摘/必要正文校准；各次范围见ROOT_ADMISSION_REVIEW，不升级为全面Evidence。日期隔离意味着无当窗正面采用，不意味着降分或删候选。

## 有依据的普通负侧

- Greek 2512.05647：完整题摘的领域语料/抽取/基线 RAG，无独立通用机制或反证；root 已校准。
- Dynamic Alignment 2512.05464：除题摘外，已读 §2 方法、§3 评价和 §5 future。固定自生成目标、self-reward GRPO 及新的 CA 规范，本稿未新增足以改变通用训练/Agent 设计的执行或优化机制；目标规范本身不作主线突破。作者建议排除贡献，不把单 seed 或未来消融单独作排除理由。
- ArtistMus、Bengali ToT、Classic Author GRPO、FedGMR原关闭理由撤销：复用Popper实际必要正文校准（分别§4.2/4.3、Tables4/6；IV-C/D/E、TablesI/V/VI；§5/Table3；§3/4.1/4.2、Algorithms1/2），同步上表具体反证/机制及边界。作者没有冒称本次全读四稿，不用成熟组合、局部任务或摘要控制不足否认潜在增量。各项公开仍未授，不评分、不采用，不要求日期受阻项全面深审。
- 明确科学应用/领域预测/经典控制标题按范围止步，临床 2512.05537 只标题判断，不声称完整题摘。

## 外部隔离及精确重开

1. 上表除已按旧公开归档关闭的Pink Slime外，arXiv v1缺实际首次new公告或可核正文公众时间。官方abs/版本史、月列表、主题日期查询及有限历史替代未提供有效个体公告；ARXIV_DATE_RECOVERY确认advanced月粒度、API/OAI提交/修改语义，不重复无效日查询或依一般排期补造。恢复条件为ID+v1匹配的官方new历史RSS/email/list，或可核正文公开范围完全落窗；只重开对应ID。可读题摘已筛选，缺日期不转回普通未读队列。
2. GLM/AutoGLM：官方日标签跨 09:00，metadata 与 release 替代未提供时间，历史 commit 不证明 first-public。重开需要带时区公众公告或可证明公开性且界限落窗的 artifact；AutoGLM 采用实现还须相应历史版本。具体时间缺口不支持 Books。
3. OpenAI/Anthropic/Google/Qwen/Hunyuan/ZAI/MiMo/Agent Tech的滚动/动态历史目录：原始入口、窗口搜索及有限官方替代的可见段不提供目标窗口完整历史切片。隔离目录未恢复部分，不认定零事件；恢复条件为对应12/08–09原始历史段。Meta/MiniMax/ERNIE/Kimi只支持实际显示目录。Seed已由两类2025 API恢复显示范围，撤销其过宽历史隔离，见TARGETED_REPAIR。

反馈C四项误关已恢复；同一原有界段的额外63份精确v1题摘及必要正文反馈后59潜在/4负侧见[FEEDBACK_C](./FEEDBACK_C.md)，LexGenius/CALAMITA原关闭撤销，与本表共同构成本日原始筛选停点。普通作者可执行待办已收束；外部项不授 Coverage/Evidence/Books 通过。维持进行中，交Popper非作者检查。
