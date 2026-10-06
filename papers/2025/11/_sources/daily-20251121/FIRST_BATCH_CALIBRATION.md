# 2025-11-21 首批准入校准请求

作者Dalton；2026-10-04T18:16:00+08:00。窗口BJT [2025-11-20T09:00:00+08:00,2025-11-21T09:00:00+08:00)。仅本日新取原源；不继承别日候选/覆盖。此包是首批，不是日级完成。独立校准尚待root。

## 拟入选与潜在项

### Nano Banana Pro：发布事件与来源验证边界

原源：[launch](https://blog.google/innovation-and-ai/products/nano-banana-pro/)、[developer](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-pro-image-developers/)。同一材料家族。

日期实际恢复：新取HTTP200 [launch HTML](nano_pro_launch.html) 和 [developer HTML](nano_pro_developer.html) 的NewsArticle JSONLD均为 `datePublished=2025-11-20T15:00:00+00:00`，name=published_time同值；BJT20日23:00，落窗。article:published_time仅 `2025-11-20`，不冒充时刻。canonical/mainEntityOfPage对应各原页。dateModified分别 `2026-03-19T17:48:07.338034+00:00`、`2026-01-07T18:57:17.794706+00:00`，当前正文不能冒充逐字2025快照；修改字段本身不证明中心重要修订。receipt分别保留实际请求/响应/获取时间。

实际核心：[首批原文](WEB_FIRST_POTENTIAL.json) launch的完整搜索提取及L245起核心，[developer后半](WEB_NANO_DEVELOPER_CORE.json) L230–278；前半亦在[定点原文](WEB_FIRST_TARGET_CORE.json)。launch尾部网页重开两次timeout，已转新取HTML200，不重复空路径。

准入问题：原先可见标记与生成来源容易混同；本次推出Gemini app英文图像SynthID验证，同时Ultra/AI Studio移除可见标记而仍保留嵌入标记；因此需要限定“可见标记缺失”和“是否Google AI生成/编辑”的证据含义。只把真实新可用验证入口及厂商声明的覆盖对象作为局部发布/安全边界，不把成熟provenance原则加分，不声称通用AI检测、变换鲁棒性或误报率已验证。拟2+2+1=5，安全/发布约束受影响内容须深入。root请校准是否足以改变本项目解释，还是仅发布上下文。

developer核心新增Search grounding可选、paid preview与较高cost/latency的定性取舍。检索接入不自动证明图像事实正确；14输入/5人、2K/4K或SOTA图不作为机制/受控比较结论。暂不为组合本身再造第二家族。当前核心未见明示撤回/纠错；没有遍历版本史。必要后续只围绕上述验证覆盖/限制，不先读所有guide/cookbook/model card。

Owner路由待核：PLATFORM-SECURITY（来源验证的信任/安全边界）；不因SynthID名称缺位申请Books。尚未实际对读owner，暂无具体写入请求；校准后才必要对读。

### OpenAI CVE assignment policy：潜在边界，日期未定

原源：[policy](https://openai.com/policies/openai-cve-assignment-policy/)。[实际全文核心](WEB_FIRST_TARGET_CORE.json) L27–58已读，原字段 `November 20, 2025` 无时区/时刻。新取 [HTML](cve_policy.html) HTTP403 anti-bot，不当正文；[receipt](cve_policy.html.receipt.json)。两条定点日期查询在[日期恢复](WEB_CVE_DATE_RECOVERY.json)，首页只恢复同一原页自然日期，其他命中不扩池；当前不能确认落窗。

准入问题：CVE记录可能被误用为完整安全问题清单；实际政策把model safety行为/内容排除，通常不为server-side分配，reserved还未公开；因此没有public CVE不能证明这些问题不存在。只是该厂商登记对象和公开状态边界，不以一般治理原则冒充新机制，不声称漏洞发生率/法律保障。若日期确认，拟2+2+1=5并深入受影响安全内容；此时不列确定当窗候选、不正面采用、不开展全CVE清单/Trust Portal扫描。有限尝试已做原网页、curl、两精确查询；重开只需同身份官方首公开时刻或完全落窗上下界。保留必要安全反侧，不因日期未定把方向删除。

Owner潜在PLATFORM-SECURITY；未实际比较现有正文，暂无Books差额。root请核这是具体适用边界还是仅制度上下文。当前核心无明示撤回/纠错。

## 三项代表性排除

1. [Foxconn合作](https://openai.com/index/openai-and-foxconn-collaborate)：新取[RSS](openai_rss.xml) `Thu, 20 Nov 2025 14:50:00 GMT`，BJT22:50落窗。[核心](WEB_OPENAI_NEGATIVE_CORE.json) L21–31实际读；仍是初始设计/制造准备，无购买或财务义务，后续采购选择。没有提出可核的rack执行机制、可比资源取舍或失效边界，拟关闭；不是因为硬件不在主线。
2. [Small Business AI Jam](https://openai.com/index/small-business-ai-jam)：RSS `Thu, 20 Nov 2025 06:00:00 GMT`，BJT14:00落窗。核心L24–49读；培训、workshop和应用推广，无模型/系统机制增量。当前页L24明示 `December 15, 2025 Update`，晚于本窗的后记不反填20日，不额外打开其after-action附件。拟关闭。
3. [Group chats](https://openai.com/index/group-chats-in-chatgpt/)：原页11月13日发布，L35标 `Update on November 20, 2025` 全球推广；[核心](WEB_FIRST_TARGET_CORE.json) L35–58实际读。此更新是可用范围扩大，未新增实际执行/隐私协议。原发布的memory/privacy与未成年条件不改挂20日。日期精度未核但贡献关闭不另造日期请求。拟关闭Nov20更新，不声称别日作者已审原事件。

以上当前核心未见明示撤回；Small Business晚更新明确隔离。三项是分层代表性负侧，不代表全日全部排除已独立核。

## 查询与当前停点

OpenAI Research当前入口与完整新取RSS仅筛本窗，RSS两事件如上；policy/group-chat更新另由定点原页发现。Anthropic新取Research Flight publicationListPosts=171，仅日期/身份核目标边界，窗内0，邻接Nov21T14:32Z晚于终点、Nov12T18:19Z早于起点；不是171全题摘队列，也不证明删除/未列项目没有。

Google入口及pubs目前仅原入口/部分条目；仍有历史目录普通工作/缺口，不能授覆盖。四条原日期发现query与首页停止在[记录](WEB_DATE_DISCOVERY_01.json)，仅新命中Nano继续原文；没有扩全年或Weekly。14每日来源、arXiv有界主题尚未完成，普通待办继续。

请求root现在独立核：Nano准入/同家族/当前晚modified的采用边界；CVE具体局部价值与日期隔离；三负侧理由及晚更新归属。包未授Evidence/Books或日级完成。共享Books零改动，无stage/commit/push。
