# 2025-11-20 首批准入校准包

作者 Dalton；2026-10-04T16:53:00+08:00。窗口 BJT [11/19 09:00, 11/20 09:00)，UTC [11/19 01:00, 11/20 01:00)。这是5个潜在方向的首批准入请求，不是5个确定落窗候选，也不是 Evidence/Books 通过。原始题摘、官方无摘要材料的核心说明实际读完；未用19日候选或 Weekly 倒推。

## 查询与原始材料

实际首查 OpenAI Research、Anthropic Research、DeepMind Research、Meta Research：前三为当前目录，Meta入口0可读行，均不足以证明历史覆盖。首轮辅助查询各1页、未翻页：`site:openai.com "November 19, 2025" Codex`、`site:anthropic.com "Nov 19, 2025" research`、`site:research.google "November 19, 2025"`、`site:ai.meta.com "November 19, 2025" research`。随后原源打开命中，不采用搜索片段性能数字。

第二轮各1页、未翻页：`site:anthropic.com/research "November" "2025" "19"`、`site:research.google/blog "November 19, 2025"`、`site:ai.meta.com/blog "SAM" "November 19, 2025"`。Google官方2025博客页1实际到11/12，并未翻全年9页；Meta publication页4/Blog页2仅作为本窗恢复线索，日期非单调，不称完整历史目录。

真实工具原始返回保存为 [核心](WEB_FIRST_CORE.json)、[完整题摘与S2ST核心续段](WEB_FIRST_ABSTRACTS.json)、[SAM 3D完整题摘/商业负例/发现查询](WEB_FIRST_NEGATIVE_AND_DATES.json)、[官方发布/晚版变更/Google年页](WEB_META_RELEASES_GOOGLE_LIST.json)。失败下载也保留receipt，不把403或超时文件当正文。

## 五个拟继续方向

### 1. [Real-time speech-to-speech translation](https://research.google/blog/real-time-speech-to-speech-translation/)

原官方页面时间仅`November 19, 2025`，时区/精确公开尚未恢复，暂不确定落窗。实际核心L104–108、124–192，含支持与反侧。

原约束是级联ASR/翻译/TTS错误累积、语音与语义时序错位；原文新增三层对齐重叠mask指导训练loss、ground-truth右移控制lookahead、流式encoder10秒历史与RVQ分层输出。因此可核验“翻译语序所需前视如何成为训练及推理的显式延迟/质量选择”，不是因为多模块组合或产品上线而准入。初步owner `MULTIMODAL-REPRESENTATION`（时序对齐及codec身份），实时生成交接Ch24；未读owner、不声称知识缺口。

中心反侧：L169明确2秒内部delay之外还有inference latency；硬件、并发、model size未披露，不能写2秒端到端SLO或比级联普遍降低一半。L184–185不同产品策略不同，Pixel同时用cascade扩大语言覆盖；L191–192当前五组拉丁语系，Hindi和动态lookahead属于未来方向。应核必要图/评价可比条件，不为日期未定遍历所有音频附件。

### 2. [SAM 3: Segment Anything with Concepts](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/)

完整官方题摘为原始返回L44–50，日期仅`November 19, 2025`。不能把提交时间或Meta自然日直接转BJT整天。

固定标签/单目标定位无法表达开放概念的全部实例，原文新增PCS任务、presence head解耦概念存在性与定位、共享backbone的detector与memory tracker；若成立会改变“有概念线索时为何仍产生不存在实例/漏实例”的解释。初步owner `MULTIMODAL-REPRESENTATION`，需核presence head及hard negatives的实际新证据，不能仅凭SAM名称或2×数字。

当前[原博客URL](https://ai.meta.com/blog/segment-anything-model-3/)已变为2026-03-27 SAM 3.1；L49–63的16对象multiplexing、32fps/H100等晚版不能归本日。L66起保留原SAM3正文可辅助身份，但必要机制/数字须绑定精确历史论文，不以当前网页所有内容为2025版本。更新信号已记录，不称撤回或原结论纠错。

### 3. [SAM 3D: 3Dfy Anything in Images](https://ai.meta.com/research/publications/sam-3d-3dfy-anything-in-images/)

完整官方题摘已读，保存在发现原始返回；官方发布日期仅`November 19, 2025`。不是把任意3D应用整体纳入World Model。

旧约束是自然图像遮挡/背景复杂，而3D训练ground truth多为孤立合成物；实际新方向是model生成多个mesh供非专家排名、难例路由3D专家，再以synthetic pretrain→real-image posttrain闭环扩增。若对照支持，会改变3D标注的成本与sim-to-real覆盖取舍。初步owner `TRAIN-DATA`（生成/校验/难例标注），表示交接Ch23；不是把LLM posttraining术语移植本身当新机制。

[官方发布](https://ai.meta.com/blog/sam-3d/)L64–79已读关键反侧：单对象逐一预测、不训练接触/穿透等物理交互，不能写成action-conditioned world model或物理一致场景；5:1 human preference需真实evaluator与对照，几秒shortcut需历史精确版本及运行配置，不正面采用未绑定数值。

### 4. [SAM 3D Body: Robust Full-Body Human Mesh Recovery](https://ai.meta.com/research/publications/sam-3d-body-robust-full-body-human-mesh-recovery/)

完整官方题摘L42–48已读，日期同上未核。旧的身体表示纠缠骨架/表面，MHR显式分离，并加入keypoint/mask提示修正。潜在命题是表示因素解耦和外部视觉证据约束如何影响交互修正，而不是人像应用或SOTA本身。初步owner `MULTIMODAL-REPRESENTATION`；请root校准是否实际增量足以改变当前表示解释，不能因为较专用模型自动排除，也不因为新mesh名称自动准入。

原发布L81–92反侧：每个人独立处理，不支持多人/人-物交互推理；手部不超过专门hand-only模型。先核解耦及prompt refinement必要证据，不把它与Objects机械算同一个论文，也不因同一发布文章增额外release家族。

### 5. [Building more with GPT-5.1-Codex-Max](https://openai.com/index/gpt-5-1-codex-max/)

本日重新原源发现并读核心L46–85及[card入口](https://openai.com/index/gpt-5-1-codex-max-system-card/)L23–27；原日期`November 19, 2025`，未核精确时区。card内部日期/版本与发布事件可能不同，须定点恢复，不把二者自动算同日或两家族。

跨window训练与runtime自动compaction的行为有版本事实价值，但压缩/保留重要信息的成熟原则、内部24h演示及30%token宣传本身不足以证明新长期机制。拟继续核明确受影响的协作训练/防用户修改破坏机制及可比评价，若历史精确card支持，可改变“运行中用户更改如何纳入训练状态分布”的局部解释。初步owner `AGENT-CONTEXT`，授权交接Ch78；没有深读card或owner，不直接宣称已有覆盖/整合。

官方L77–78安全限制已读：restricted sandbox与用户review不构成模型安全保证；API“coming soon”不能写GA。Card必要安全/冲突反侧不能因日期未明省略；此前独立校准如对应身份/版本/命题未变可由root定点确认复用，不由作者自授通过。

## 代表性负侧校准

1. [Microsoft/NVIDIA/Anthropic partnerships](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships)，实际核心L17–28：商业投资、Azure访问与未来工程协作愿景，没有披露可采用的模型/训练/推理机制或可比实验。原日期Nov18时区未核；贡献明确不符后不另建日期请求，不将其称确定窗外。发现不等于本日新候选。请root抽检“未来协作优化目标不等于已实现系统机制”的排除理由。
2. 同一SAM发布的Marketplace View in Room/Playground应用（L52–59）不增加机制家族；不因此排除SAM的实际表示、训练新证据。原博客新增的SAM3.1性能事件为明确2026-03-27晚版，隔离不采用，不能作为SAM3 v1的安全/性能证据。这是应用/晚版归属两层负侧，不伪称第二个被全量审过的论文排除项。

## 17:13 日期增量

[官方RSS与外部测试单项包](RSS_DATE_AND_INCREMENT.md)恢复Codex发布/card入口 `Wed, 19 Nov 2025 00:00:00 GMT`；这个声明时刻早于20日起点，待root定点核19事件归属，不采用社区转发改时刻。此前只有自然日的描述为较早快照；其余四项日期仍未确定。新增本窗12:00Z外部测试协议具体访问/发布反侧，以及11:00Z Business evals、06:00Z Target代表性排除可现在校准。

## 当前请求与可执行停点

请root现在校准上述5个具体准入命题，尤其Body表示解耦是否足够、SAM3 presence head与3D排名/专家路由是否真实增量，以及两层负侧是否误漏局部贡献。日期全部保留原字段；可查HTML元数据的有限恢复正在执行，不授确定当窗。

普通工作：其余10每日来源及arXiv窄主题/标题补检尚未完成；此包不支持完整Coverage。待首批准入反馈后只展开受影响必要证据；无关来源初筛继续。尚未比较实际owner，Books写入0，无POST义务；不把“暂未读owner”写成Books长期缺口。
