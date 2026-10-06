# 2026-01-12 独立发现与准入停点

窗口：`2026-01-11T09:00:00+08:00`～`2026-01-12T09:00:00+08:00`；执行时间：2026-10-02。Root 作者；不读取旧 Daily/Weekly 判断。仅每日14源与实际触发线索，不扫描每周组。

## 发现入口与有限停止

已打开每日官方入口：OpenAI Research及Research Index；Anthropic Research及See more（仍返回同一最新页）；Google DeepMind Research及Google Research `blog/2026/01/`；Meta Research（无可读内容）；Qwen旧站及其官方新站`qwen.ai/blog`（新站无可读列表）；DeepSeek主页；Kimi Blog；Hunyuan Research（无可读内容，隐藏浏览器调用30秒超时）及具名HY-WorldPlay官方仓库News；智谱Research可读2026/01/13～2025/12/10边界；Seed Publications第一页（1–20/242，13页，目标页未恢复）；ERNIE中文Blog第一页及下一个旧页边界链接；MiMo Paper/Blog；MiniMax英文及中文Blog（中文重定向minimax.cn，同样未恢复历史列表）。不把当前最新页/搜索无命中记为历史完整目录。

有界补检使用以下组合，各只处理返回结果、不扩全年：

- `site:openai.com (research OR "technical report") "January 11, 2026"`；`site:anthropic.com (research OR "Jan 11") "2026" "January"`。
- `site:deepmind.google OR site:research.google "January 11" "2026"`；`site:deepmind.google "January 11, 2026" OR "11 January 2026"`。
- `site:ai.meta.com/research "Jan 11" "2026"`；`site:ai.meta.com OR site:qwen.ai OR site:deepseek.com "Jan 11" "2026"`。
- `site:hunyuan.tencent.com "2026-01-11" OR "2026-01-12"`；`site:github.com/Tencent-Hunyuan "Jan 11, 2026"`。
- `site:platform.kimi.com OR site:zhipuai.cn "2026-01-11"`。
- `site:seed.bytedance.com "Jan 11, 2026" OR "January 11, 2026"`；`site:seed.bytedance.com/en "January 11" OR "2026-01-11"`。
- `site:minimax.io OR site:minimaxi.com OR site:mimo.xiaomi.com "2026" "January 11"`；`site:qwen.ai/blog "January 11" OR "2026-01-11"`。
- arXiv线索：`"2026" "Jan 11" (transformer OR "language model" OR inference OR MoE)`；官方cs.CL月列表请求`2601?skip=0&show=2000`返回406，未将其变为全分类队列。

搜索不是召回完整性证明；正文中隔离未恢复的历史入口，不能以这些搜索结果保证零事件。

恢复时补查MiniMax官方Agent Tech Blog及`https://agent.minimax.io/docs/llms.txt`：当前可读50行文档索引，只给当前Tech Blog入口与Agent Team文章，没有目标窗历史列表或原始发表字段。没有把当前文档反推为Jan11事件，也没有为恢复目录扩大到全部产品文档。

2026-10-03定点恢复两官方原入口，结果由root本日独立GET，不继承另一日的计数：DeepSeek`https://api-docs.deepseek.com/updates`实际可读，原`Date: 2026-04-24`紧接`Date: 2025-12-01`夹住本窗；只支持这条changelog切片无落窗事件，不证明所有仓库事件不存在。Seed`https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&publish_year=2026`，header`x-tt-locale: US`，page_token=0/20/40/60/80实际返回18/20/18/19/2，共77项、total=82；仅末页has_more=false。最早返回`PublishDate=1768838400000`，晚于本窗，未把UpdateTime当首次公开。相同type2 Blog返回14、total19、has_more=false，最早2026/02/11。列表计数差额5+5及当前索引是否完整保留历史未知，隔离为覆盖限制；不是77/14个本窗论文或待审队列，不扫描其窗外摘要。

## 日期与题摘判断

### 原入口字段定点恢复（root fresh，2026-10-03）

以下为实际返回的最小字段投影，不复制窗外正文，不继承其他日期计数：

- Qwen `GET https://qwen.ai/api/page_config?code=research.research-list` root fresh actual60条；最新原`date=2025-12-23T05:08:30.000Z,id=qwen-image-edit-2511,title=Qwen-Image-Edit-2511: Improve Consistency`；其次12/22T16:00:45Z qwen3-tts-vc-voicedesign与12/19T05:08:30Z qwen-image-layered。可用旧配置停止而非API无参数空响应授零；未恢复2026实时retrieval历史，源仍精确隔离。

- OpenAI `GET https://openai.com/news/rss.xml` HTTP200，当前1244项仅metadata；定点Jan8–15八项实际原字段桥接：`Fri, 09 Jan 2026 11:00:00 GMT | OpenAI and SoftBank Group partner with SB Energy | https://openai.com/index/stargate-sb-energy-partnership` → `Tue, 13 Jan 2026 16:00:00 GMT | Zenken boosts a lean sales team with ChatGPT Enterprise | https://openai.com/index/zenken`。相邻01/08 Netomi/Healthcare、01/09 Datadog、01/14 Cerebras、01/15 supply-chain/Merge亦实际定位；未读1244正文，保留删除/未索引历史未知，不授全网无遗漏。

- Anthropic `GET https://www.anthropic.com/research` 原HTML：`publishedOn=2026-01-09T17:17:00.000Z, slug=next-generation-constitutional-classifiers`；下一条 `2026-01-14T00:00:00.000Z, property-based-testing`。January其余字段为01/08、15（两条）、16、19、22、28、29；December相邻19/18/04/02/01实际读到。所读切片未见本窗事件；“See more”提取失败不再是唯一停止依据，不授删除历史完整。
- Hunyuan `POST https://api.hunyuan.tencent.com/api/blog/publicList`，JSON `{"pageNum":1,"pageSize":1000,"renderType":0}`，`Content-Type: application/json`；en-US与zh-CN均code0/totalNum9/list9且`lang=en`。实际原字段如下，单位秒，不能拿显示日期替换publicAt：

| id | 原title（简写仅导航） | publicAt | publishedAt | displayPublishTime |
| --- | --- | --- | --- | --- |
| 100116 | When Do Larger Batches Help Scale LLM Reinforcement Learning? | 1790150728 | 1789707529 | 1790006400 |
| 100100 | Introducing Hy4 preview | 1787896874 | 1787896672 | 1787846400 |
| 100091 | From LR to ELR | 1787231073 | 1785989409 | 1785945600 |
| 100087 | Hyra | 1784563044 | 1784111171 | 1784599200 |
| 100064 | Introducing Hy3 | 1783348861 | 1783319811 | 1783440000 |
| 100039 | Real life is where context gets hard | 1777554399 | 1777227059 | 1777532400 |
| 100061 | Hy3 preview | 1783313906 | 1782369407 | 1776873600 |
| 100015 | Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping | 1770971763 | 1770971763 | 1770971763 |
| 100025 | Learning from context is harder than we thought | 1770112927 | 1770090898 | 1770090898 |

- arXiv正确 `GET https://arxiv.org/list/cs.CL/2026-01?skip=0&show=25`：原 `<title>Computation and Language Jan 2026</title>`，`Total of 2168 entries`、`<span>1-25</span>`、`href=/list/cs.CL/2026-01?skip=25&show=25`。首25标题实际读到，不补造全月审查；首ID2601.00086（当前HTMLv3链接），末ID2601.00543，不能由当前版本链接推当日重要revision。短格式406仅保留为前次入口失败，不授正确入口不可访问。

负侧可复查位置：第三方[HY-MT推荐Issue189](https://github.com/bquenin/interpreter/issues/189)，Jan11请求替换翻译模型、借用官方旧仓库及宣传数字，没有原始新系统研究；[音频输入参数PR12510](https://github.com/Comfy-Org/ComfyUI/pull/12510/files)核心是新增局部audio_cover_strength输入，独立fresh官方API核`created_at=2026-02-18T04:46:08Z`，是窗外误命中，页面列旧commit不能当本窗PR公开。未审669 changed files/250 commits，不授全PR审查；[安装报错11801](https://github.com/Comfy-Org/ComfyUI/issues/11801)为Windows PyAV编译缺libavcodec header，不提供新系统机制。这是具体贡献前关闭，不是“凡PR都排除”。三位置已由jan01_v3 actual独立抽核。

[官方公开时刻规则](https://info.arxiv.org/help/availability.html#announcement-schedule)说明新稿、replacement及withdrawal等随公告公开，周日～周四20:00美国东部时间。该日为冬令时：周日01/11 20:00 EST = 01/12 09:00 BJT，恰为本窗排除的终点；前一次常规公告为01/09 09:00 BJT。规则不证明作者没有更早在其他原始入口发布，也不替代特殊延迟/历史revision恢复。

- [Solar Open 2601.07022](https://arxiv.org/abs/2601.07022)：完整摘要已读，102B MoE、低资源语言合成数据/课程与SnapPO可有具体训练机制贡献；v1字段为**Submitted** `2026-01-11T18:33:09Z`，按周末公开流程不由该字段归入本窗。其更早作者正文/项目公开若能恢复才重新判断；不评分、不称已经审读重复。
- [CLIMP 2601.06891](https://arxiv.org/abs/2601.06891)：完整摘要已读，双Mamba表示与高分辨率资源边界有潜在主线贡献；Jan11 submission同样不是本窗公开证据，保留日期恢复线索。
- [PenForge 2601.06910](https://arxiv.org/abs/2601.06910)：完整摘要已读，运行时构建专家Agent是潜在机制，但局部12/40和三倍数字不是通用保证；Jan11 submission不授当窗身份。
- [Cognitive Trojan Horse 2601.07085](https://arxiv.org/abs/2601.07085)：完整摘要已读，主要认知/社会假设与testable predictions，未建立改变当前模型/基础设施设计的原始机制或反证，贡献前关闭；不为其日期继续追查。
- Google Research月目录的`NeuralGCM ... global precipitation`：标题明确为当前暂缓AI for Science/领域气候模拟，贡献前关闭；没有把Jan12无时区日期补造成09:00前。
- 搜索出现的第三方HY-MT推荐issue、普通TNN编译说明/前端组件PR、ncnn通用参数表、ComfyUI外部集成音频节点PR及用户安装报错，不构成当前系统设计研究增量；关闭，不按仓库Updated时间创造发布事件。
- HY-WorldPlay官方News：01/06训练/轻量权重、01/03量化工程、2025/12/17报告，均非当前公开事件；搜索的Jan11 Updated不改变这些事实。
- MiMo Paper目录：01/08技术报告，后续02/03稀疏Attention；智谱目录01/13与2025/12/10边界；ERNIE第一页01/15与01/08边界。只证明所读目录切片无确定落窗事件，不保证全部Blog/revision无遗漏。

## 唯一拟入选：原始安全披露

`SF-COMFYUI-GHSA-95pq-hr8p-f5g7`：[仓库原始公告](https://github.com/Comfy-Org/ComfyUI-Manager/security/advisories/GHSA-95pq-hr8p-f5g7)。实际读取官方[repository advisory API](https://api.github.com/repos/Comfy-Org/ComfyUI-Manager/security-advisories/GHSA-95pq-hr8p-f5g7)：`published_at=updated_at=2026-01-11T15:47:18Z`、`withdrawn_at=null`，折合BJT23:47:18，完整落窗。不要用global advisory数据库的06/22收录日期，也不把已有patch当本日新release。

已读原公告Impact、Affected Configurations、Patches/Requirements、What the Patch Does、Fallback Protection与Workarounds。配置文件和custom node/snapshot管理数据置于普通user目录时，网络API形成绕过管理权限的alternate channel；迁移到受保护system目录须与宿主保护API的版本共同成立，旧宿主只强制strong模式是受限退路，不等已消除全部路径。原公告称localhost默认配置不受所述远程路径影响；未复现攻击、未核所有代码、未证明生产防御完备。

初始准入提案（历史停点，已由下述复核收束）：原本按主要管理界面授权→原公告暴露另一数据API可修改管理策略/来源→必须按敏感资产及全部可达路径检验权限和兼容迁移，Owner `PLATFORM-SECURITY` Ch72，3+2+3=8，安全受影响命题必要深入。现有owner缺少普通用户数据接口、宿主版本与迁移/回退的联动说明；后来独立核准并实际补两段，不再是普通待办。

## 恢复位置

本轮已由jan01_v3 actual独立校准唯一入选、必要公告/API日期、四完整AB与具名负侧；原公告足够支持窄命题，未采用代码实现/完整防御保证。Root已实际写Ch72主体后两段及末注，jan01_v3实际POST通过；五入口最小字段及正式来源限制已同步。最终六部分独立日Gate通过，1正式=1深入=1实际整合/POST，普通0；完成态以正式README为准，不重复未变附件审阅。
