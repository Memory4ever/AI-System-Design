# Jun13 补遗漏：有限来源检查

作者 `supp_jun13`；执行原件时间见 `SUP_FETCH_RECEIPT_20261026.json`。补充窗口仅 Jun12 BJT，旧小时窗不迁移。raw保存是恢复依据，不表示已审全文。来源初取阶段经 using-agent-skills 的范围/证据约束，未改共享Books/State/index；后续必要/Books实际进度只在本日NECESSARY及报告/唯一root review维护，不将初取阶段这句外推成全轮无Book改动。

## 官方每日入口与停止位置

| 来源 | 实际入口与停止位置 | 结果及限制 |
| --- | --- | --- |
| SRC-OPENAI | `https://openai.com/news/rss.xml` 单XML，Jun12 pubDate UTC10 Academy courses、UTC00 Preply；邻段Jun11四项后停止 | 两条为课程推广/语言学习产品案例，标题明确无新模型或系统研究；贡献前关闭。不把Jun11部署采购、收购或科研案例移来。 |
| SRC-ANTHROPIC | `https://www.anthropic.com/listing/research/default/2`，24posts/hasNextPage=true；Jul28至Apr23，Jun12 PublicRecord之后Jun08跨目标即停，无第3页。具名 `/research/anthropic-public-record` 完整核心及Method/Limitations已读 | 51,993美国人late-2025态度调查；希望、担忧、治理偏好是公众意见，不是模型可靠性/能力证据，也未提出新训练或执行机制，贡献前N。不是标题/机构过滤。 |
| SRC-GOOGLE-AI | `https://research.google/blog/2026/06/`月份一页，Jun12 skin与retired phones，Jun10 unlearning跨目标。phone完整core已读；`https://deepmind.google/research/publications/239142/`官方Jun12完整摘要已读；GooglePubs主入口raw已保存 | skin为健康应用、无新机制标题线索；phone是退役手机general-purpose cloud/课程CPU矩阵作业与Kubernetes编排，不含foundation/LLM计算新机制，N。From AGI to ASI是四路径/瓶颈与开放研究问题展望，未提供改变本项目机制解释的可核验证据，N；不继承旧“邻日已审”标签。Google Publications日级目录不能从当前主入口恢复，受阻隔离、不零命中，等待有日期官方列表或具名Jun12原始论文定点重开。DeepMind Blog当前page2未给Jun12段，仍需有界补检，不宣称全站覆盖。 |
| SRC-META-AI | `https://ai.meta.com/research/`当前HTML未给Jun12日级历史目录 | 历史目录受阻隔离；未见具名Jun12新材料不能证明完整目录零发布。可接受官方当日列表/具名原文，只定点重开，不授无遗漏。 |
| SRC-QWEN | 官方retrieval `type=qwen_ai&language=en-US`与`zh-CN`各40articles，无分页字段；June1→June16Robot→June23AgentWorld完整响应相邻段 | 无Jun12列项；正确参数非空响应，不用无参数空数组授零。 |
| SRC-DEEPSEEK | `https://api-docs.deepseek.com/updates`单页日期邻段2026-04-24→2026-07-31 | 无Jun12列项，越目标停止，不遍普通commits。 |
| SRC-MOONSHOT | `https://platform.kimi.com/blog`可见末新2025-11-07；orgs/MoonshotAI/repos?per_page=100&sort=created单响应42repo | 当前可见档案及新建项目有限检查，不代表2026完整发布；created不作论文公开日。本窗具体新事件仍待有界日期补检。 |
| SRC-TENCENT-HUNYUAN | POST `https://api.hunyuan.tencent.com/api/blog/publicList` body pageNum1/pageSize100/renderType0，accept-language:zh；code0,totalNum11,list11；id100041May21→100064Jul06相邻 | 中文All无Jun12列项，无下一页；不是默认英文9条冒充全部。 |
| SRC-ZAI | `https://www.zhipuai.cn/zh/research`时间排序首屏Jun16 GLM5.2→May20 ZCube | 跨目标停止，无Jun12卡片。 |
| SRC-BYTEDANCE-SEED | `/en/public_papers`首屏1–20 of247/Page1 of13，Jun19→Jun11化学反应网络→Jun4 | 跨Jun12停止，无当日卡片，不遍其余12页。 |
| SRC-BAIDU-ERNIE | `/blog/zh/`首屏最新May9文心5.1，早于目标即停 | 无Jun12列项，不翻旧页。 |
| SRC-XIAOMI-MIMO | 官方`https://mimo.mi.com/docs/en-US/updates/model`日期Sep22→Jun02ASR→Apr23；官方blog实际资源4752.2908c99e.js双语frontmatter Jun10 Code→Jun08 TileRT→May30 | 有日期目录无Jun12列项；不补造无日期route的时间，不使用错误主机TLS故障。 |
| SRC-MINIMAX | `https://www.minimax.io/blog`单目录目标邻段Jun09 MaxProof→Jun01 M3 | 无Jun12 Blog卡片；本窗MSA技术论文13392另由arxiv发现，不能据Blog未列排除。 |

## arXiv 导航与当前停点

合法DataCite查询 `client-id=arxiv.content`、`query=registered:[2026-06-11T16:00:00Z TO 2026-06-12T15:59:59Z]`、page[size]=1000、page[number]=1/2。meta total1274/totalPages2；实际1000+274，未发P3。两页原件完整保存；这是注册时间发现范围，不直接等于当日新论文数。

按模型/Attention/MoE、训练/蒸馏/优化、推理/KV/GPU/通信、Agent/工具/记忆、foundation multimodal/world/VLA主题导航，使用常见同义词标题线索及有界相关标题浏览；原宽标题不是全量待办。首批实际完整8份exact-v1 AB/history，5拟准入、2代表性排除、PhaseQuant12487跨日潜贡献隔离，详见 `SUP_ADMISSION_20261026.md`。随后20份相关机制AB已实际获取，尚未全部校准，不称审阅完成；未扩Methods队列。日期联合界逐项核v1/同精确DOI/findable，created不作界。

普通待办：root首批准入校准、实际有界补检、后续准入/必要证据/Books与最终日级复核。外部日级目录隔离不替代普通未做事项。

## 后续有限补检与去重校正

- 辅助检索实际查询 `site:deepmind.google "June 12, 2026"`、`site:moonshot.cn OR site:kimi.com "2026-06-12"`、`site:ai.meta.com "June 12, 2026" research`，仅结果页有界补线索。DeepMind返回已读FromAGItoASI，未用它证明整个Publications零；Meta恢复 `/global_search/?page=3`（2953混合结果）当前一页，Publication日期July17→July13→July03→Jun29→Jun05，混有people/blog，不是完整历史日级目录，故不解除原具名隔离。
- Moonshot补检发现官方`https://www.kimi.com/code/docs/en/kimi-code-cli/changelog.html`的0.14.1/0.14.2均Jun12，已实际读该两版core全部变更（下邻0.14.0Jun10即停）。本地取消/后台子进程退出、overlap active-agent绑定、环境透传等是具体runtime正确性修复，不因为版本号或Fixes标签自动准入；但其中是否改变可复用生命周期设计仍待根作者准入校准，未记零发布。其他通知、配置容错、流式stdout和autocomplete是局部交互实现，不构成模型/系统机制贡献。
- 初次错误形状官方月路径 `/list/cs.CL/2606?show=2000` 与cs.LG同式均404，只是入口形状错误，不是历史分类目录不可用。root§42已恢复合法 `/list/cs.CL/2026-06?skip=0&show=2000` 与cs.LG同式各200：实际各首页2000身份，仅已知日期线索所在12505–13680导航带有界比对，CL66/LG106次出现均在原1274NAV，无新身份。该编号带只定位浏览区域、非日期证明；CL整月2722另页未扫，不授全月/全类召回或将1274变AB队列。
- 具名去重实际查旧Jun11/Jun12正式候选表，A1/A2有18同精确v1事件已属Jun12，保旧日期/评分/有效层，原23拟准入校准不是23新增候选。剩余七与A4十六已在2026既有Daily README作精确ID候选行检索（排除_sources/Weekly），无其他旧归属；不读全年论文或重审其他日。
- 截至这一停点，A1/A2实际28AB=7新准入/3前N/18具名同事件。B3实际19份AB已取，其中3身份重复只查身份未再读AB、其余16完整AB已读；13400timeout未算排除。A4的13已root校准准入/1日期隔离，WEAVER/Interleave各决定点窄读，不把三目标SOTA或成熟pipeline组合当贡献。所有进度以后续ADMISSION/NECESSARY与root canonical为准，不用本段冻结未来分母。

## 来源筛选冻结：2026-10-26 10:20 BJT

实际有限补检与ADMISSION A1–A11现已完成：90份完整论文AB＝53新候选/18具体前N/18旧Jun12同精确v1事件/1日期隔离，另Kimi当日0.14.1/2同家族两release具体正确性说明以4分关闭，正式54families。root§24/30/32实际独核已通过相应原件/日期/准入。只冻结发现/筛选层，不授53篇Methods完成、Books完成或DAY。

导航实际围绕模型/Transformer/Attention/MoE、训练/优化/蒸馏/解释、推理/KV/GPU/通信、RAG/检索/Agent工具/记忆/评价、foundation多模态/codec/diffusion/world/VLA，相关标题含糊或可能有贡献的读完整AB；末组A8是RAG/Agent/评价的有限补检。题名与相关subject只导航，非正则准入；1274宽列表及未进入这一有界切片的标题，不转成全类逐篇关闭配额。第一次完整28后、后续增量与五个决定点各保过程及改判，不以候选数量反推覆盖。

DeepMind当日窄backstop已经是上节官方Jun12出版页/完整AB加具名日期搜索，结果是展望前N；不再因当前Blog page2不含Jun12而扩机构年目录。Google Publications与Meta的历史日级目录仍真正隔离、恢复条件不变；它们不获得零发布/正面Coverage或全网无遗漏。Kimi只用exact两Jun12核心，不再扩repo/changelog邻日。原13400/12789 timeout均一次有限恢复200，解除普通来源缺层；不是外部H。

当前信号按已有页面轻量复用：本日53候选exact-v1官方事件页的Comments全部实际读；前批28已取current官方页Comments也实际读，未出现指明本轮采用命题受影响的撤回/纠错/重要修订说明。可见的页数、code/projectlink、accepted/workshop等不作贡献或重要修订信号；Drop current51页/v1注37页及其他v号差异也不自动触发全版本比对。此为已有页面可见说明的有限检查，不担保无任何未标注修改；如后续必要读发现具名实质冲突，只重开受影响命题，不重新扩Source或全版本遍历。

冻结后root§42纠正上述月入口并实际补该导航带，无新身份/AB/候选，54保持；这项修正不解除GooglePubs/Meta真正历史日级目录限制，也不据整月页替代逐项联合日证。

### 当前信号缺层补齐：10:39 BJT

root指出exact-v1 Comments不能替代后批当前说明。实查原28 current包含18旧dup/3N，只覆盖53候选的7项，故仅补另46当前abs页，均200且本地 `SUP_RAW_CURRENT_2606.<ID>_20261026.raw` 存在，未重复原28。46份当前Comments/短显式撤回纠错提示已实际读；页数、录用、code/projectlink不触发版本比对。**12830 PERIA** 当前Comments明确“Camera-ready version with additional experiments, analyses, and clarified methodology”，不以v号本身触发，但该方法澄清可能影响原OR-GIGPO组资格采用，故仅定点核该当前短说明及其直接方法层；候选家族/Jun12归属不新增、不重分。除此之外未见明确受影响的纠错/撤回说明；这不是无未标注改动保证。

root§53已实际独核53/53当前事件页信号，§57独核PERIA current-v2 §4.3/C3受影响方法澄清通过：明确按动作后resultingobservation分组、无sameprestate要求、tokenratio排toolobs且完整history/span分责。N21/N27保存该窄恢复与必要评价；不再让前段仅7新current的历史停点冒充最终53检查，也不声称版本无任何未标注变动。

来源层最终收束：上述初取阶段“普通待办/仍需补检/待校准”已由后续finite补检、root§30/32/42/53/57及本节覆盖。没有新窗、新候选或全类逐篇队列；真实GooglePubs/Meta目录限制和12505跨日身份保留，不授零发布或无遗漏。PERIA当前受影响方法/评价及真实BookPOST§66已完成，其余53 current短说明不为v号遍历全史。必要/Books的实际终态只由日报与root canonical维护，不以此来源冻结预授DAY；下一日须新鲜上下文，不能继承本日候选池。
