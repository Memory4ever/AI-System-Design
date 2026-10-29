# Dec19 其余具名单篇 Source / owner

## 1. Wellbeing：安全评价角色与精确历史数值分开

实际读[官方Dec18报告](https://www.anthropic.com/news/protecting-well-being-of-users)完整core及四脚注/编辑说明；Newton§3已实际同域，原Feynman精确必要层复用。准入为单轮/从头生成不能代表从旧不良历史恢复→真实旧对话prefill、无system prompt及机会/全对话分母不同→重估产品安全和跨行为分数的解释。拟2+2+2=6，安全/纠错域深入，非临床效果研究，不扩医疗池。

必要反側：prefill是在既有轨迹中续写而非从头表现；该组without-system-prompt不能等Claude.ai产品条件；全对话分母使不同behavior的发生机会不同；内部realism filter未进公开Petri，公开工具同名不等完全复现内部测量。当前纠正70为91并称earlier Opus4.5版本，编辑行又印Feb3,2025早于Dec18，年份不擅改2026；不采用当前91或旧70为2025精确比较，不以日期合格清除版本争议。精确历史数值只接受官方旧版本/可靠更正版本身份定点重开；方法域可独立采用，不因数值hold假装未读。

actual owner：Ch66开篇Claim contract/Evidence production/Measurement inference/Decision分层、条件分布与系统prompt/evaluator身份，以及§Prefill是Harness输入不是自然历史完整两段及前后局部已读。真实承载拟采用的“受控续写非从头能力、harness身份非产品条件、测量条件不授部署”的长期命题；拟已有覆盖PLATFORM-EVALUATION-SYSTEM该节及开篇四阶段，不把通用prefill当本日首创。分母/内部filter只在本报告保具体条件，不另造一般评价机制或跨行为排名。未核实现/复现，作者百分比不作临床/生产保证，判为已有覆盖尚待Newton具体校准。

## 2. U18 ModelSpec：条件规范发布与执行实现分责

实际打开[Dec18发布说明](https://openai.com/index/updating-model-spec-with-teen-protections/)与[datedSpec](https://model-spec.openai.com/2025-12-18.html)，读定义metadata/U18及该节全部规则、adult/U18对照与不确定时谨慎条件；原Feynman必要层和Newton§5实际日期/意图规范层有效复用。规范声明13–17人口的额外root级内容边界；Blog明确age判断不确定/不完整时默认U18且成人可验证。不是要求追秒/时区，也不是推断训练方法/age predictor算法已披露。current overview明确production尚未完全reflect，规范样例不是模型实测，误判/隐私/验证成本未量化。

准入：一个默认行为规范不足以表达同请求对不同人群的风险边界→系统metadata条件下额外约束及未知年龄的保守默认→考虑把适用人口/判定资格与行为合规分验。拟2+1+2=5，实际安全约束变化深入本域。拟唯一PLATFORM-SECURITY Ch72，actual读开篇主体/资产与信任转换段、Ch71tenant identity及Ch73production交接；它们尚不具体讲normative人口条件与未知资格fallback，不写age分类算法，不迁移Ch31训练或Ch66评价owner。

逐字PRE，待Newton/root（无锁不写）：拟放Ch72“主体包括用户、service accounts、controllers、training code、model server、model output和external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。”完整原段后、完整“不过，按主体保护主要管理接口……”段前。

行为规范的适用条件也应由可信会话状态承载，而不让模型从一段自述自行取得改变规则的权力。同一请求可对成年人允许、对未成年人施加额外限制；规范版本、适用人口与人口判定的不确定性因而是三个不同对象。[具名规范更新](https://model-spec.openai.com/2025-12-18.html)给出按U18条件生效的意图规则，其[发布说明](https://openai.com/index/updating-model-spec-with-teen-protections/)另声明年龄不确定时采用较保护性的默认并允许成人验证。这是规则与分群条件的披露，不证明年龄识别准确、模型已经完全遵从或实现了新的训练算法。判定、验证与合规回归带来隐私、误拒和维护成本；资格或执行证据不足时，保留保守默认及可信验证/人工处理，而不以规范文本代替实际安全验收。

本人末note逐字拟稿：

- `SF-2025-OPENAI-U18-SPEC`：Dec19补Dec18；[datedSpec definitions/U18](https://model-spec.openai.com/2025-12-18.html)及[发布说明](https://openai.com/index/updating-model-spec-with-teen-protections/)。Boyle拟2+1+2=5，限定规范版本/适用人口/未知资格分责，保意图非已部署遵从、age预测实现未披露及验证/隐私代价，不授临床或安全效果；Source/owner/PRE尚待Newton/root，无书锁/写入/POST/DAY，未核artifact或复现。

## 3. Skills：更新日已恢复，旧schema增量不倒签

实际[redirect后官方文章](https://claude.com/resources/articles/skills)Update明确December18,2025：open standard/cross-platform、组织管理与partner目录。更新日通过，不沿用旧offset门；原October16机制、三阶段disclosure不重算Dec18新机制。原Feynman实际现行spec核心有效，但当前compatibility/experimental allowed-tools等无精确Dec18 schema，不能冒充旧版新增。Ch84当前168–209 Skill contract/registry及Ch83连接/权限分责实际已读：它们不代源证恢复。保留“跨平台标准的具体兼容/执行差额”潜力为精确历史规范hold，不评分/列确定候选/写Books；组织目录和发布标准本身是上下文事实，不由声望/版本名确认新机制。旧失效入口不重试，不扫MCP周源；恢复只接受官方精确2025标准或清楚变化说明，非全部产品新API。

## 4. Seed1.8：只采用VideoCut轮廓，card另责

实际读[原官方Dec18 Blog](https://seed.bytedance.com/en/blog/official-release-of-seed1-8-a-generalized-agentic-model)core/Video理解/预算及限制性图注。Newton§5日期与旧Feynman已核相同核心/比较条件可复用，原cardredirect失败不重试。准入是整段低帧率读取的细节/预算限制→VideoCut选定片段慢放以观察高帧率运动→重新考虑何时支付局部重读预算，拟2+1+2=5，标准必要域完成；实际采样/触发/训练或cost算法未披露，不能从headline或三种thinking mode补造。VideoMME带字幕/跨模型预算和WorldTravel best-of-five不是等预算机制因果，token更少不授端到端更快，不用原card缺失取消Blog已给轮廓。

actual owner Ch23长视频从固定输入到可回读视觉记忆完整局部1141–1182已读：原“与先为所有clip写压缩记忆不同，主动观察由当前问题决定下一次读取时间段、帧率、模态”完整段，以及下一段读取动作同时决定窗/密度/分辨率与额外tool round-trip/遗漏/固定读取回退，具体承载本日可采用的较窄VideoCut选择性高密度回读。拟已有覆盖MULTIMODAL-REPRESENTATION，不把后续paper全部归Seed1.8；本日不写书/旧note，不采用精确倍率/最佳参数。待Newton实际具体覆盖/5分校准。

## 5. 表外TRELLIS.2：有界原域身份与未定日

后续已发生的窄校准：Newton§15实际通过U18 Source/5分/唯一Ch72/逐字PRE，待root写前许可，不预保存/POST；Newton§16/17实际通过Wellbeing6分/Ch66具体已有覆盖与Seed1.8的5分/Ch23具体已有覆盖，不写书或原注，不再重复这些Source。采用域和历史数值/card角色按各节保持，非DAY。

中国源有限搜索噪声中第三方目录声称Dec18release，只用作线索。实际回到[官方repo](https://github.com/microsoft/TRELLIS.2)、[项目](https://microsoft.github.io/TRELLIS.2/)、其[2512.14692v1身份/完整题摘](https://arxiv.org/abs/2512.14692)及作者首页。O-Voxel几何/材质及SparseCompressionVAE是主线表示机制潜力，不因图形领域关闭；no withdraw/currentv1，未深读不称Evidence。项目无明确日，repo当前核不到公开发行日；GitHub Pages Dec16build/commit不是public release证明，arXiv submitted16不是公告日，第三方Dec18不授日。四必要原域定点后停止，保留具体first-public/release日hold，未评分/确定候选/Books；不把它擅断窗前或回扫Microsoft/CS.CV。重开只需官方具名公开日/announcement或可用公开区间，不需秒/TZ。

## 6. U18真实保存 / 作者self-read，待actualPOST

后续真实Newton19完整新增/两侧/本人注POST已通过，root§6已实际读回接纳并释放U18窄位。Boyle只改本人注尾同步已发生self-read/POST/root读回释放，实际完整读回该注/限定tracked小写路径diff-check0；不改正文/他注，不重Source/PRE/POST。待root直接读本人注行政差额，本日五项实际整合已接纳，非DAY。

2026-10-15T17:05:16+08:00实际时钟。Boyle已实际读root§5许可；写前重新读Ch72开篇主体完整段与后管理资产两段、本人拟追加位置/前两水印注。按git ls-files核实tracked路径为小写books/part-06-ai-infrastructure/72-security.md，实时两层numstat为unstaged8add/cached空，完整读这8行水印差额后保护，不操作index。

按本包§2逐字仅插一自然段于主体完整段后/“不过，按主体保护主要管理接口”完整段前，末追加U18本人一注；注只记录已发生Newton15/root5及真实保存，不预POST。保存后实际完整顺读22–40行，主体→新增全文→管理接口/迁移完整两段，实际完整读本人注及前两水印注；保可信会话/意图规范/适用人口/资格分责，识别准确/已遵从/新训练未证，费用和保守默认/可信验证/人工退路近文。与逐字PRE一致，无标题/marker、原段/他注/Draft修改。

实际完整限定diff为原水印8+本项4=12add/0del，cached空；tracked小写路径两层diff-check均exit0。作者真实self-read不是非writer POST；待Newton实际完整新增/两侧/本人注POST，再root真实读回接纳释放，本项未称已整合/DAY。当前root给出的98/132来自Oct21接纳，不含Dec19。

