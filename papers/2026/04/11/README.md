# Daily Research — 2026-04-11

**规范：** V3
**窗口：** 2026-04-10T09:00:00+08:00 ～ 2026-04-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T15:50:00+08:00

## 1. 结论

本轮重新核了14个每日来源，不继承旧稿基于DOI-created代理的“零候选/Complete”。已恢复目录中有4个当窗发布条目：Seed Protenix-v2、MiniMax CLI v1.0.6/v1.0.7、Kimi CLI 1.31.0；前者属当前暂缓的AI for Science，其余是客户端局部correctness/UX修复，均有具体前分母关闭理由。目录全表数量只是查询停点，不是当天新论文或有效贡献数量。

本窗冻结贡献候选0、正式候选证据审阅0、Books新增0；**今日未发现足以修改核心知识库的重要进展**，但这只限已恢复入口，不表示全源无遗漏。arXiv官方常规公告槽不落本窗；旧OAI里03263的一条可变日期已找出，不能被旧receipt的零记录掩盖，也不能改判成当窗首发。非作者日级复核已通过，普通待办为0；来源历史缺口与具体日期问题见§5。[本次查询和关闭记录](../_sources/daily-20260411/v3-reopen-notes.md)保留实际入口、停点和原始字段，[旧稿](../_sources/daily-20260411/v2.1-report-before-v3.md)无损保留，不作为V3验收。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)、[Index](https://openai.com/research/index/)只有现行首屏至08-18/Load more；[News RSS](https://openai.com/news/rss.xml)1230项按UTC筛窗，04-10T00:00Z→04-13T06:00Z；Research/Publication sitemap读过身份清单，不用lastmod当首发 | 受阻 | RSS无当窗条目；历史Research分页未恢复，隔离该子入口，不能称全源无更新 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)170个publishedOn元数据；04-09T16:34Z→04-14T13:01Z跨本窗，无当窗条目 | 已检查 | 仅此可恢复官方研究目录，不含未列作者稿 |
| SRC-GOOGLE-AI | [April Blog](https://research.google/blog/2026/04/)整月9条，04-13→04-09→04-08；ConvApparel原文/ACL身份已核；[DeepMind selected publications](https://deepmind.google/research/publications/)264项首屏已跨04-22→03-22 | 受阻 | Google Publications只有年级facet，日级历史停点未恢复；ConvApparel日戳无时区，论文为March2026既有身份，不冒充本窗新稿 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)实际返回0可读行，不能恢复历史日期停点 | 受阻 | 缺官方Research/Publications当窗归档；空页面不是零命中 |
| SRC-QWEN | [动态列表](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项与[静态配置](https://qwen.ai/api/page_config?code=research.research-list)60项，动态04-02T04:00+08→04-15T10:00+08，静态全早于2026 | 已检查 | 官网Research合并列表无当窗条目；不证明全体作者稿不存在 |
| SRC-DEEPSEEK | [研究与动态](https://www.deepseek.com/news/)可见研究06-24→02-25、动态04-24→2025-12-01，越过本窗 | 已检查 | 结论限可见官方目录，不扩张为未列作者稿零遗漏 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)所见最新2025-11-07；Kimi-K2.5官方release API空；kimi-cli全release分页超时/截断，但已直接恢复[1.31.0 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.31.0)，04-10T14:45:26Z在窗内，完整说明和5项贡献消歧PR已读 | 受阻 | 已知release逐项局部关闭，不用分页失败掩盖它；April完整Blog/CLI发布停点仍缺，隔离后不检普通commit |
| SRC-TENCENT-HUNYUAN | [官方Research](https://hunyuan.tencent.com/research)publicList，page1/size100/renderType0，total9/list9；displayPublishTime04-30/04-23→02-13 | 已检查 | “全部”目录无当窗条目，不表示全体作者稿无命中 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)日期04-29→04-07→04-01，之后03月/2025年；已越过日窗 | 已检查 | 04-07未标时区但不与本窗相交；不用CMS createdAt证明首发 |
| SRC-BYTEDANCE-SEED | [Papers](https://seed.bytedance.com/en/public_papers)官方API type1/US locale，total242，页0/20/40越过04-10T16:00Z→04-09T16:00Z；[Blog](https://seed.bytedance.com/en/research)type2页0/20，total95，页0实际15条，页20实际18条，04-22T16Z→04-08T16Z→03-31T16Z，页20已到2025年 | 已检查 | 当窗目录Protenix-v2按范围关闭；目录PublishDate不是外链首次公开权威；未称全242/95条逐全文 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)04-15→02-06，之后2025年；[ERNIE releases](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100)1条2025-06-30 | 已检查 | 所查Blog/release无当窗条目，不代替全部百度作者论文 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper06-29→03-13→02-03；MiMo/MiMo-VL/MiMo-V2-Flash官方release API均0 | 受阻 | Paper/release已处理；Blog无可靠历史日期，隔离该子入口 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)05-26→03-18，[中文Blog](https://www.minimaxi.com/blog)跳转官方minimax.cn，04-27→03-18；CLI release26条含当窗v1.0.6/1.0.7已读发布说明及后者2-commit发布差异 | 受阻 | 两个当窗CLI事件已具体关闭；M2/M2.5 release API空；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)与llms.txt只有现行无日戳文档，历史日期缺口隔离 |
| SRC-ARXIV | [公告规则](https://info.arxiv.org/help/availability.html)周五/六无常规发布，前槽北京时间04-10T08:00、后槽04-13T08:00均窗外；旧Apr11 OAI cs里03263、stat/eess空，已重开该项官方v1/history及DataCite字段 | 已检查 | 没有将周末未排公告推成异常公开不可能；03263的Apr11 OAI日戳/Updated不是首发，具体不确定性隔离在§5 |

## 3. 候选与判断

冻结候选为0；这不是从空网页或旧receipt推出的零，也没有把全部目录项保留为候选。四个当窗目录/版本条目已在§4按贡献门槛关闭；日期保留线索不进入本窗分母或正式评分。没有候选，因此不虚构评分与Source Review，不为产生Books diff强行整合。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

**Seed Protenix-v2**：官方论文目录PublishDate=1775836800000，即2026-04-10T16:00Z（本窗内的目录事件），外链为[生物分子结构预测与设计v1](https://www.biorxiv.org/content/10.64898/2026.04.10.717613v1.full.pdf)。该标题已明确是当前暂缓的AI for Science；不是大模型Training/Inference/平台机制研究，前分母关闭，不评分、不全文深审、不修改Books。目录时刻不当作论文首发证明；范围处置已确定，无需另建日期请求。

**MiniMax CLI v1.0.6**：[正式release](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.6) published_at=2026-04-10T05:15:40Z。发布说明为默认音频输出文件扩展名、SSE流解码成raw audio与EPIPE处理（PR63/60）；是具体客户端correctness修复，不改变模型推理状态、长期流控/协议或平台设计结论，前分母关闭。不能因“stream”关键词而保留或推成新的serving机制。

**MiniMax CLI v1.0.7**：[正式release](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.7) published_at=2026-04-10T08:31:19Z。[发布差异](https://github.com/MiniMax-AI/cli/compare/v1.0.6...v1.0.7)共2提交，只删除重复SKILL.md与package.json版本号更新；无长期机制增量，前分母关闭。没有把缺release正文等同材料受阻，也未扫描全部普通commit。

**Kimi CLI 1.31.0**：[正式release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.31.0) published_at=2026-04-10T14:45:26Z。完整发布说明中的有歧义条目已定点打开原始PR：[todo](https://github.com/MoonshotAI/kimi-cli/pull/1742)将root/subagent计划状态分开持久化、加查询模式与保存时刷新，模型重复调用的背景是空输出和Shell禁用，PR手工无storm验收仍未勾选，不能证明通用Agent控制已解决；[凭证刷新](https://github.com/MoonshotAI/kimi-cli/pull/1822)使用进程内锁→跨进程advisory文件锁→重新读token，锁失败仍无协调刷新，不能升级成可靠性/安全保证；[断流](https://github.com/MoonshotAI/kimi-cli/pull/1800)是特定SDK异常守卫与启发式分类，[think-only](https://github.com/MoonshotAI/kimi-cli/pull/1801)是不把不完整模型输出静默算TurnEnd；[启动升级提示](https://github.com/MoonshotAI/kimi-cli/pull/1826)保留继续/跳过选择，不是后台强制安装。它们分别修复一个客户端的状态存储、token-rotation race、错误分类与交互提示；未给出新的长期机制、受控设计反证或新的发布/安全保证，前分母关闭。持久化事实状态与确定性提交/重试分权在[Ch81](../../../../books/part-07-agent/81-workflow.md)主线已成立；这里不是凭章节相关性自动保留，也不把已有通用原则的局部bug修复全部升为研究候选。

以上是前分母关闭说明，不冒充候选已读全文。没有正式候选，Books判断终态为无必要改动；不调整既有设计结论，不新增知识owner。

## 5. 缺口与下一步

普通可执行工作：无。非作者日级复核与最终校验已完成。以下是**本窗终态保留项**，不用于正面证据、Books采用或无遗漏断言；每项具有下述定点重开条件，不以这些缺口无限重扫其他日期。

- OpenAI Research Index：首屏止于08-18，历史Load more未恢复；RSS和sitemap身份不能提供完整Apr日级停点。可接受替代为官方带日期的历史分页/完整本窗Research归档，到达后仅重开该子入口及其family。
- Google Research Publications：只有年级facet，无法证明Apr10～11公开目录完整；DeepMind精选不是全作者稿。可接受替代为官方带首发日期的历史结果/本窗归档，定点补查。
- Meta Research/Publications：Research正文为空，无历史日期停点；可接受官方可读本窗目录或当窗公告存档，定点重开，不能把无响应记无命中。
- Moonshot：Blog停在2025-11、kimi-cli release分页超时/截断，无April历史停点；官方当窗Blog索引/有效release分页到达才重开，不扩扫普通commit。
- MiMo Blog：现行卡片没有可核历史公开时间；官方单篇日期或April完整历史索引可重开，Paper/空release不足替代。
- MiniMax Agent Tech Blog：现行techblog/llms.txt仅无日戳目录；官方当窗历史归档或精确版本公开日期到达才重开，不从现行网页倒推。
- [LPC-SM 2604.03263v1](https://arxiv.org/abs/2604.03263v1)：官方当前history仅v1，旧OAI有Apr11日戳；DataCite created Apr07T02:37Z、Updated/v1 Apr11T04:37:54Z（已晚于本窗截点）、Available仅2026-04，任一单字段都不证明当窗first-public。其方法已在[Apr07](../07/README.md)日期保留项处理，本日不重复申请或重审；只有官方具体公告或可核更早public上界/重要修订证据到达，才定点恢复真实owner，不机械迁移。
- [ConvApparel](https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/)：Blog仅April9无时区；[ACL身份](https://aclanthology.org/2026.eacl-long.244/)已是March2026论文，本次是宣传线索而非确定当窗新family。若有带时区的当窗公开事件且独立机制增量才定点重开，不仅凭发现日重评分。

## 6. 复核

复核者：root（非本日报作者）
结论：通过

root独立重读14来源行的实际停点与限制、四个关闭理由、八项隔离边界及空Books集合；定点重新取得KimiCLI正式release（04-10T14:45:26Z、17项变更）、原始PR1742/1822，并对读Ch81 activation/持久化/重试实际正文。确认本次关闭基于具体实现和证据边界，不是因“bug fix”标签；advisory锁失败降级与无通用storm/可靠性保证没有被隐藏。来源检查记录的复核不是逐一重新抓取全部机构外部目录，零候选不表示全网零遗漏。旧OAI数量矛盾已纠正为具体身份隔离，未伪造首发时刻、未复现实验。

本次scoped validator与Markdown/链接、git diff --check已通过；必要Books改动为空集且独立确认。修改范围仅本日报与日内来源记录，保护其他既有修改，未 stage、commit 或 push。
