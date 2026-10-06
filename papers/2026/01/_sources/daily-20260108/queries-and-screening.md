# Jan08 原始查询与停点

窗口固定 `[2026-01-07T01:00:00Z,2026-01-08T01:00:00Z)`，北京时间01/07 09～01/08 09。2026-10-02独立启动，完整重读AGENTS、研究/Report合同、统一Prompt、Daily14来源及arXiv主题、ROADMAP与最新相关checkpoint；checkpoint只路由，不继承旧Report候选、分数或完成标签。只own本日README与本月_sources/daily-20260108，不扫描Weekly；共享Books先申请具体owner锁，apply_patch编辑，不stage/commit/push。

当前普通工作：按Daily14顺序fresh原入口与窗口邻接日期切片，arXiv仅主线主题/同义词和有界标题补检。Submitted Jan5T19～Jan6T18:59只发现缓冲，待原公告/首次ID规则和具体日期恢复合取，不当public时刻；registered/Updated单独也不是public。宽metadata不是逐项关闭或全文队列。首批完整题摘具体增量+代表性负侧先交root校准，准备好的项只读拟采用命题必要核心/反证，不等待无关项。

## 首轮实际入口与发现停点

已实际请求15入口页面（13机构、Google双入口/MiniMax双语各有限页面）；`official-entry-0..3.jsonl`保存当前入口返回（其中OpenAI403，其余HTTP200不等于历史恢复）。另在`official-entry-supp.jsonl`保存Google一月博客、DeepMind publications、Qwen新博客、ZAI发布说明、MiniMax AgentTech入口。它们是有限目录恢复线索，不是机构历史无遗漏验证。系统/现成Python的bs4缺失发生在联网前；改用标准库HTMLParser后实际获取，无安装。

arXiv `arxiv-initial-metadata.jsonl`四条窄主题查询采用提交缓冲`202601051900..202601061859`，不是报告窗/公开日期条件：model 105（只取前80，尾25未读/非逐项待办）、system7、multimodal22、agent19。返回latest metadata，题名与摘要可能已更新；所有需要准入判断的材料另取exact v1，不能把latest题名或Submitted当事件。四查询第一轮仅显示未完整保存，第二轮同查询保存原字段；均metadata-only，重复去重不加分母。原始命中不作候选，不设153篇逐项关闭队列。

本窗起点2026-01-07T01Z是周二Jan6 20EST；可用官方availability排程（周一14ET～周二14ET通常周二20ET）和holiday只new-submission具体条件作日期下界背景；仍需具体首公开上界与作者先行线索。未使用不支持的lastUpdatedDate filter；旧public revision/mirror召回仍需明确限制，不等于零事件。

首批定点完整v1题摘：03067跨request/chunk block融合（潜在2+2+2=6）、03044执行/干预→异步policy的物理fleet闭环（潜在2+2+2=6）、03089控制retained-information的归因测量比较（潜在2+2+1=5）。02677金融多任务head、02757遥感task识别→领域工具链作代表性负侧，读完整题摘后判断具体增量，非领域标签排除。日期未放行不计正式候选。首批必须root独立校准后深化。

root已实际独立读上述5份完整exact-v1题摘，三正侧原6/6/5准入潜在贡献通过；02677、02757具体组合/域评价未改变项目机制或可靠性边界，贡献前关闭通过。后续先读必要core/直接反证，非整篇附件。

官方日期fresh恢复：RSS1243条仅抽Jan1–12元数据（不读全年摘要），本窗Tolan Jan7T10Z、Netomi Jan8T00Z；Health Jan7T00Z为起点之前，同事件定点去重，无旧报告评分读取。Anthropic Research HTML174 publishedOn仅Dec/Jan字段，本窗critical-infrastructure-defense Jan8T00Z。Kimi releases page1 100元数据日期贯穿Sep22到2025Oct24，本窗无该页release，邻接0.72 Jan4T06:01:07Z和0.73 Jan8T16:54:15Z均窗外，非created_at。HunyuanPOST当前9条rawmetadata保publicAt/publishedAt/displayPublishTime/createdAt/updatedAt；不能恢复Jan历史。Seed四slice仅ArticleMeta日期/pin/状态+Title/TitleKey及pagination，未读全年题摘；2026paper最早Jan27，blog最早Feb，2025两slice最新Dec24/15，有限目录无本窗确认研究事件但非archive无遗漏。

日期抓取初版输出包含API article content导致工具截断（不当完整raw/不当证据）；已删本日临时截断诊断文件，改只日期/title原字段并fresh重取，valid `official-date-slices.jsonl`为实际8行完整元数据，未修改其他来源/用户文件。

## 恢复后的有限推进（2026-10-02T12:05Z之后）

完整重读当前AGENTS、研究/Report合同、Prompt、Daily14与arXiv主题、ROADMAP及当前相关checkpoint（仅路由）。恢复时第一次合并工具输出截断，合同/ROADMAP/Books指南分别补读到EOF；不把截断算完成读取。

model原查询仅补start80/max80，实际余25元数据已读，保存`arxiv-model-tail.jsonl`。它们只作为窄主题标题线索，不升为25项候选/必审队列。既有四query返回latest metadata的更名/版本不同，所有准入题摘仍取exact-v1。

实际新增完整v1题摘4份，存`batch-B-abstracts.md`，本日当前16份独立AB（first5+A6+MiMo1+B4），尚未冻结最终分母。root独立校准A6均有待核原增量，B中DIP/LTX2原6、MMErroR原5准入通过；DiffBench只补Sx3决定性三stage/constraints后拟贡献前关闭，待非作者负侧核。03178首次按S3/S4抓取只取得heading、core空，保存diagnostic；据actual heading Sx3定点恢复，不将空core称方法已读。普通审阅仅原增量和关键反侧，不默认全附件。

03067实际paper链接是`sef1/kv_fast_fusion`，此前推断错误URL不属于原sourcegap。correct repo fresh200及5个README提交字段/Sept18精确README存`kv-project-correct.jsonl`/`kv-artifact-history.jsonl`。2025-05/09作者/committer及GitHub verified_at字段不是当时public证明，且已知artifact与首次论文正文不同事件；保留BFF/CFF早期实现线索并定点核有无更早正文，不声称已确认作者先行、不无限追所有历史。

四机构窄日期补检已fresh执行，query为`site:qwen.ai/blog "2026/01/07"`、同Jan8、`site:hunyuan.tencent.com "2026-01-07"`、`site:ai.meta.com "January 7, 2026" research`。Qwen实际恢复官网qwen3-vl-embedding完整核心（Jan7 date-only/无tz）；其余无确认本窗primary正文不等零事件。初次宽一些January7相关search返回Meta当前Research/Google当前blog及窗外候选，仅定位原入口，不读全年AB。Qwen拟按现有EOS dual-tower/yes-no joint reranker在多模态基座上的适配关闭，保text-only退步但不授独立归因，待root准入负侧校准。

上述为16AB时的过程停点，不覆盖以下24AB及两项实际POST；没有把剩余metadata设为默认队列。

## 当前有限停点：24题摘、两项POST通过

具名C组8份exact-v1完整题摘已实际读并保存`batch-C-abstracts.jsonl`；本日实际24AB（first5/A6/MiMo1/B4/C8），未冻结正式分母。root已校准的首三、A6与B三项可执行必要核心；C组及决定性贡献前关闭提案待独立校准。当前不扩发现或新题摘库存，仅处置这24项和已定位官方事件。

SOP与Grad各一正文/首注已按root窄授权实际写入；root实际核Ch36:1205–1220及Ch66:2836–2851前后和两末注，POST通过，锁已释放。只采物理episode提交边界与归因预期遮挡预算，不授strict on-policy/faithfulness。日期与整日Gate仍待核。

`necessary-dispositions.md`记录实际必要core、决定性反侧及受限提案。SimpleMem仅补§2方法、InfiAgent仅补§3/4/7决定性接口；DIP只§4/5/Limits与Eq5/6/Alg2、LTX2只§3.1/4.1/6/7、MMErroR只§2/3/4.3–5/Limits；没有声称长cache的全表/附件已读。LoRA-Drop必要schedule/KV身份中心冲突、ACL局部安全recipe、book extraction近逐字对齐测量和Green能耗边界均保留实际源/尚待非作者结论。

`selected-date-registration.jsonl`为15个既有家族一次定点原字段恢复，不是新发现。13项注册上界在Jan7T03Z之前，须合取原公告规则/ID非advance/提交过前批cutoff/无更早正文；registered或Updated不等public。03305与03331的updated/registered均Jan8T01Z之后，不能用Jan6Submitted把它们放进Jan08；保留相邻窗线索，03305不再开方法附件。03067更早OpenReview与MiMo/LTX2更早正文身份仍分别核，不假定arXiv镜像是首公开。

普通下一步：已校准必要core/owner与定点日期身份、既有负侧独立裁决及有限来源停止收束。外部精确缺口不用于正面Evidence/Books/覆盖或无遗漏；日级仍进行中，不等待无关材料。

进一步定点实际停点：MiMo release精确旧PDF已通过bundled pypdf内存读取成功，只保printed p18§4.4必要MOPD identity（Eq5–9）不审完整31页/图/表；LTX2只初始README与决定性跨模态/selectedpipeline字段，不扩repo树或所有history。厂家Jan6T00:30ET宣布即刻公开架构/代码是窗前事件，质量/隐私营销未采用。两家族的具体首body/新披露差额见`prior-body-identity-stop.md`，不把commit=public。

Replay已补exact-v1 §2/5/6，实际原局部maxheap/retest/exploration recipe拟4；Lil已与Ch45:400–404实际较读，原6拟具体已有覆盖；两处原源/score/反侧提案见necessary-dispositions，待root非作者，不是作者自授。Book extraction只必要§3.3完整matcher/control和相关有限productionAPI设置，未读书籍正文；Ch66 stringmatcher小节尚缺唯一位置/单调对齐计数与merge跨度分账的窄measurement身份，已向root申请，不擅自写共享文件。

进行中README当前V3校验与限定diff-check PASS；此前abs/html两处小标题URL不一致已改同候选URL，没有变判断。机器通过不授语义完成。fresh打开官方availability L170–186/2026holiday表只核公告/ID规则，误探不存在的submit/holiday.html不称真实官方历史档案故障。

最新实际停点：root完整校准C8题摘，并实际决定SimpleMem/InfiAgent/DiffBench贡献前关闭；Green原5具体Existing、ACL原4安全必要审阅后OnlyReport、LoRA原6中心schedule/cache身份隔离均通过。Book原6必要源→Ch66具体matcher缺口→1875单段及4315末注actual POST通过；当前三项实际正文、三项非作者POST，不是日级完成。root实际范围见necessary-dispositions；其余finite必要处置继续，不增加题摘/来源库存。

C四项实际必要缓存为02867/03066/02989/02643-necessary-core.jsonl；Homotokens A2/A3设置/评价与Prune B4 teacher/pruner/SFT的必要补段已保存C-necessary-settings-extra.jsonl。AWARE Table6实际核三类分母，保存02643-metric-identity.md；未把条件relax-correct车匹配当总体成功，也未扩提示附录。后续root实际必要源与具体owner核通过：Homo窄正文Ch11:331/420注POST通过；Prune/Counting/AWARE/SDServing原5标准仅报告、Replay原4局部配方关闭及DIP决定性Eq5/6/Alg2中心隔离通过。当前四项实际正文/四POST，不是日Gate。

官方标题补检actualstop见arxiv-title-backstop-stop.md：月目录2168/前2000仅作已知相关ID的局部标题路由，root授权四完整题摘，当前合计28AB，不把2000当本窗新论文/逐项队列。四份必要方法/反侧均已实际完成，title-backstop-dispositions.md记录root实际通过的02674贡献前close、02695/02906原5OnlyReport和02872原5specificExisting，无进一步新增发现。

最终Qwen原文恢复：此前直接web读取官方blog的核心没有本地raw；恢复后exactblog返回0行，不冒称缓存存在。仅同家族官方repo current README overview/features/architecture完整原段fresh读取并固定SHA，保存qwen-official-core-recovery.jsonl的core字段；没有读取安装/runtime示例或repo history。current官方core支持EOS dual tower与yes/no pointwise单塔适配组合判断，但不是Jan7 exactrelease archival证据，也不采用当前性能/文本退步数字为历史反证。root实际此core贡献前关闭通过，不授first-public或无遗漏。

最终本日停止：28份完整exact-v1论文AB = 17本窗formal + 6贡献前close + 3priorbody/新披露差额保留 + 2dateupper越窗；官方五core另记，不混论文AB分母。17formal = 4整合actualPOST + 3具体Existing + 8OnlyReport + 2center保证隔离，全部必要非作者处置通过。root实际日期三原字段逐项、MiMo旧body、LTX公告/有限源码、JointKV403与六部分/14source有限停点核后允许完成；普通0，不再新增发现/书写。准确复核范围见README§6，未全metadata/fullappendices/互联网验证；终态不授Coverage/Evidence无缺口。完成态validator和scoped diff-check实际PASS，没有stage/commit/push；不自动开其他日期。
