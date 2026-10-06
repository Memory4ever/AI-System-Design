# May3：18个具名旧潜力项的日期与当前事件记录

检查：2026-10-16 13:29:33 +08:00。只处理Noether修复记录§20末交接的18个精确身份，不扩分类、月份或候选池；不评分，不作Source/Books判断。

## 请求与原件

- [第一次DataCite回应](ROOT_DATE18_20261016.raw.json)及[头](ROOT_DATE18_20261016.headers.raw)：HTTP200/935bytes/exit0，但将client-id写入query字段导致0条。这是查询构造错误，无论文缺失或窗外权限。
- 对照本轮已成功的50 DOI请求，只将client-id改为独立filter，精确18 DOI OR及page[size]=25一次GET：[正确原件](ROOT_DATE18_CORRECT_20261016.raw.json)及[头](ROOT_DATE18_CORRECT_20261016.headers.raw)。HTTP200/82835bytes/exit0；meta.total18、page1/totalPages1，无next，精确身份集合一致。完整query保存在links.self。
- [arxiv.org API入口](ROOT_CURRENT18_20261016.raw.xml)及[头](ROOT_CURRENT18_20261016.headers.raw)实际302指向export，不是论文内容。按同一精确查询访问HTTPS export：[当前Atom](ROOT_CURRENT18_EXPORT_20261016.raw.xml)及[头](ROOT_CURRENT18_EXPORT_20261016.headers.raw)，HTTP200/45480bytes/exit0，total18/start0/18唯一entry。未重试失败查询或使用catchup，所有请求均已结束。

## 逐项字段与联合界

root实际结构读18项resource.id/doi、完整题名/作者、publisher arXiv、client arxiv.content、findable、created/registered、所有Submitted/Updated及版本、URL和relatedIdentifiers。唯一v1 Submitted全部位于Wed Apr30 18:00Z之后、Thu May1 18:00Z之前；America/New_York为EDT，最早公告界统一为Thu20EDT，即May2 00:00Z/BJT08:00。各精确DOI registered给条件最晚界，不改名实际公开时刻；created/Updated/月份不参与界。

| v1身份 | Submitted原UTC | registered原UTC |
| --- | --- | --- |
| 2505.00091 | Apr30 18:02:45Z | May2 01:30:55Z |
| 2505.00134 | Apr30 19:01:06Z | May2 01:32:00Z |
| 2505.00209 | Apr30 22:34:52Z | May2 01:33:50Z |
| 2505.00216 | Apr30 23:19:37Z | May2 01:34:00Z |
| 2505.00284 | May1 04:12:41Z | May2 01:35:58Z |
| 2505.00304 | May1 04:55:29Z | May2 01:36:28Z |
| 2505.00334 | May1 06:17:33Z | May2 01:37:12Z |
| 2505.00350 | May1 06:50:30Z | May2 01:37:35Z |
| 2505.00364 | May1 07:22:51Z | May2 01:37:56Z |
| 2505.00367 | May1 07:37:18Z | May2 01:38:00Z |
| 2505.00389 | May1 08:27:14Z | May2 01:38:32Z |
| 2505.00415 | May1 09:26:40Z | May2 01:39:10Z |
| 2505.00416 | May1 09:27:13Z | May2 01:39:11Z |
| 2505.00426 | May1 09:54:12Z | May2 01:39:26Z |
| 2505.00467 | May1 11:43:27Z | May2 01:40:28Z |
| 2505.00472 | May1 11:54:49Z | May2 01:40:35Z |
| 2505.00482 | May1 12:21:23Z | May2 01:40:49Z |
| 2505.00488 | May1 12:41:35Z | May2 01:40:58Z |

逐项L≤U、整个区间均在May2 BJT；最早U09:30:55、最晚09:40:58。人工规则核对后只读时区程序复算相同，不由程序替代原件。此项仅限定首次arXiv v1公告事件；不证明全球first、历史逐字内容或贡献。

## 当前官方事件层与先稿信号

root实际完整读18个Atom的题名/作者/完整摘要、comments、published/updated和DOI，身份与DataCite一致；Atom published是原提交口径，不作新公开日。当前后版为00091v4、00284v3、00334v3、00367v2、00467v2、00472v2、00482v3，其余仍v1；current摘要只用于轻量变化检查，不回填各v1的贡献或Methods。所见域没有明确withdraw/correction标记，不认证全渠道无变化。

00364明确Accepted ICLR2025、00467明确回顾2024Aug15活动，是已有具名先稿/事件线索，交作者定点处理，不以May2 arXiv合证抹去。00389 SIGIR、00426 IJCAI、00334 IJCNN和00482 ICCV的接纳状态不独自确定更早正文日；00334给出版DOI，按必要命题再定点使用，不扩会议全站。00467 DataCite中v1 Updated为Jun5，与Submitted/registered不同；不能用它撤销已核界或把未知更新内容写成纠错，必要说明保留真实角色。其他后版日期本身不触发双版全文比较。

交Ohm独立核日期/current的这一有限层，再由作者继续精确v1必要证据、贡献与Books；不将18个日期通过写成18篇Source完成或日报完成。

## 下一18：仅作者修复记录§39的精确身份

2026-10-16 07:47:54 UTC开始，两次有限GET均已exit0：[DataCite原件](ROOT_DATE_NEXT18_20261016.raw.json)/[响应头](ROOT_DATE_NEXT18_20261016.headers.raw)，HTTP200/76434bytes/5.735202s；[当前Atom](ROOT_CURRENT_NEXT18_20261016.raw.xml)/[响应头](ROOT_CURRENT_NEXT18_20261016.headers.raw)，HTTP200/41655bytes/1.515307s。DataCite精确DOI OR、独立client-id filter及page[size]=25，query可在links.self复查，meta.total18/page1/totalPages1无next；Atom精确id_list/max_results25返回total18/start0/18个entry。逐项集合与作者指定18完全相同，无新发现池或catchup。

root实际结构读全18的resource.id/doi、完整题名/全部作者、arXiv publisher、arxiv.content client/findable、created/registered、全部Submitted/Updated/版本及relatedIdentifiers；再读全18 Atom当前身份/全部作者、published/updated、comments/DOI/journal。当前题摘未作新Source或v1重筛，后版不回填。唯一v1 Submitted均为May1 13:00:56–15:47:03Z，属于Wed14EDT后/Thu14EDT前，最早公告界May2 00:00Z/BJT08:00；每个registered给同日条件最晚界：

| 精确v1 | Submitted原UTC（May1） | registered原UTC（May2） |
| --- | --- | --- |
| 2505.00500 | 13:00:56Z | 01:41:15Z |
| 2505.00503 | 13:14:07Z | 01:41:19Z |
| 2505.00509 | 13:25:37Z | 01:41:28Z |
| 2505.00515 | 13:33:34Z | 01:41:37Z |
| 2505.00527 | 13:52:19Z | 01:41:55Z |
| 2505.00533 | 13:59:13Z | 01:42:04Z |
| 2505.00540 | 14:05:46Z | 01:42:14Z |
| 2505.00546 | 14:20:48Z | 01:42:23Z |
| 2505.00551 | 14:28:35Z | 01:42:30Z |
| 2505.00557 | 14:33:47Z | 01:42:39Z |
| 2505.00562 | 14:40:07Z | 01:42:46Z |
| 2505.00568 | 14:51:30Z | 01:42:55Z |
| 2505.00580 | 15:11:46Z | 01:43:14Z |
| 2505.00582 | 15:14:32Z | 01:43:16Z |
| 2505.00590 | 15:24:48Z | 01:43:28Z |
| 2505.00603 | 15:35:01Z | 01:43:46Z |
| 2505.00610 | 15:40:58Z | 01:43:56Z |
| 2505.00615 | 15:47:03Z | 01:44:04Z |

实际人工核L<=U且全区间均落May2 BJT，再用共用只读函数复算18项同日/无reasons。created/Updated不作界，00540的Updated2026也不改首次登记；不是18篇贡献/Source完成、全球first或历史逐字认证。

当前后版为00503v3、00527v2、00533v2、00546v2、00551v3、00568v3、00580v2、00582v2，余十项v1；所见非AB说明未给具名withdraw/correction，不认证全渠道无变化。00509 ICLR workshop、00610 AAMAS extended abstract沿已有具名先稿另责；00580/582分别IJCAI2025/四作者与同名部分作者不合并家族/不从会议名授窗前。00540新增出版DOI只作精确关系线索，其他ICML/RAL接收说明不独立供首次日。以上日期/current有限层交Ohm一次独核，作者继续必要精确v1与具体owner，不重请求或强送18全文。

## 00509具名论坛日期的最后有限补检

2026-10-16恢复后，root先从本日精确v1 HTML实际核四作者Jeremias Ferrao、Luhan Mikaelson、Keenan Pepper、Natalia Perez-Campanero Antolin及Apart Research机构。只对该稿搜索官方OpenReview题名/两作者与Published字段，三查询仍只返回既知forum `QcmEb490bK` 的PDF/attachment索引；同题四作者和完整摘要可核，但索引的相对“last year/1.5 years”不作日期。没有读取新PDF全文或将已读Source重复计算。

随后实际打开官方题名search、Jeremias Ferrao作者search与该forum：两search为工具不可访问，forum重定向到官方challenge，未得到目标记录的Published日期或Readers字段。这是web工具的实际返回记录，不是原始HTTP字节存档或论文零命中；没有绕过验证、重试API/attachment或使用catchup。旧作者§44已知workshop活动日期与PDF标头仍只约束具名发表关系，不能由此补造目标记录的公开日。

本次没有新的收紧界或可执行日期线索；与作者已有原件/有限角色恢复合用，可将此**单稿早公开角色**作精确外部保留提交Ohm裁决，不将十八项已核May2 arxiv事件一起变未知。不改贡献C、不评分或写Books；必要Source及反侧按Ohm§84真实有效层保留。重开条件是该forum可核的Published/Readers记录、绑定同完整正文的官方公开日公告或作者dated public release；无需证明全球最早渠道或历史same-bytes，其他普通工作继续。

## 第三18个既有潜力项：14同日，4跨日

2026-10-16 17:19BJT，范围仅作者§56交接的18个ID。第一次DataCite查询再次误将client-id放query并用id字段，HTTP200/917bytes但total0，原件`ROOT_DATE_THIRD18_20261016.raw.json/headers.raw`保留为构造失败，不作零论文/窗外依据。对照已成功的links.self后，只将client-id设独立filter并按精确doi OR查询，page[size]25，一次HTTP200/83657bytes/3.017521s/exit0；正确原件`ROOT_DATE_THIRD18_CORRECT_20261016.raw.json/headers.raw`，meta18/page1/totalPages1、无next。完整查询在links.self，不扩大主题或月份。

同18裸ID一次HTTPS export id_list/max_results25取得当前Atom，HTTP200/46190bytes/1.674215s/exit0，`ROOT_CURRENT_THIRD18_20261016.raw.xml/headers.raw`，total18/start0/18唯一。两个集合与请求18完全相同。root实际结构读全18精确DOI、完整题名/作者、arxiv.content client/arXiv/findable、唯一v1 Submitted与所有其他版本日期、created/registered、关联DOI及非AB说明，并对回Atom每个published/作者/题名和current说明。首次包含长AB的合并打印截断后，已重新完整打印必要身份/日期/关系字段；不把未读完的current长摘要当新准入或v1正文。

全18 Submitted-v1都在Apr30 18Z之后/May1 18Z之前，非精确cutoff；已核2025适用EDT规则给下界May2 00Z。下表保原UTC字段，不改名实际公告时刻；各界有序。

| v1身份 | Submitted原UTC | registered原UTC | 联合区间归属 |
| --- | --- | --- | --- |
| 2505.00624 | May1 16:05:08Z | May2 01:44:16Z | 同May2 BJT |
| 2505.00627 | May1 16:06:17Z | May2 01:44:21Z | 同May2 BJT |
| 2505.00631 | May1 16:12:12Z | May2 01:44:27Z | 同May2 BJT |
| 2505.00649 | May1 16:48:37Z | May2 01:44:53Z | 同May2 BJT |
| 2505.00661 | May1 17:02:27Z | May2 01:45:11Z | 同May2 BJT |
| 2505.00662 | May1 17:03:17Z | May2 01:45:12Z | 同May2 BJT |
| 2505.00663 | May1 17:07:01Z | May2 01:45:14Z | 同May2 BJT |
| 2505.00681 | May1 17:41:49Z | May2 01:45:40Z | 同May2 BJT |
| 2505.00684 | May1 17:45:59Z | May2 01:45:44Z | 同May2 BJT |
| 2505.00685 | May1 17:47:44Z | May2 01:45:46Z | 同May2 BJT |
| 2505.00687 | May1 17:48:25Z | May2 01:45:49Z | 同May2 BJT |
| 2505.00693 | May1 17:55:05Z | May2 01:45:58Z | 同May2 BJT |
| 2505.00703 | May1 17:59:46Z | May2 01:46:13Z | 同May2 BJT |
| 2505.00704 | May1 17:59:57Z | May2 01:46:15Z | 同May2 BJT |
| 2505.00751 | May1 03:24:28Z | May5 01:25:28Z | May2～May5 BJT跨日 |
| 2505.00759 | May1 17:47:55Z | May5 01:25:40Z | May2～May5 BJT跨日 |
| 2505.01456 | May1 01:54:00Z | May6 02:29:42Z | May2～May6 BJT跨日 |
| 2505.01459 | May1 12:06:39Z | May6 02:29:46Z | May2～May6 BJT跨日 |

人工核完整区间后，共用只读函数复算同14 bounded/4 cross，Atom全18published与唯一Submitted-v1相同。00703/704只晚于截止前14秒/3秒，仍是严格早于cutoff，不与恰好端点混同。created/Updated/Available月份不替登记上界；尤其四晚登记不能因v1 Updated在May5/6就直接改公告日。当前后版00624/661/693/759为v3，00631/684/685/703/704/751为v2，其余v1，当前题摘不能回填后版机制。

00649关联ACM `10.1145/3726302.3730216`只作具名出版关系；00663/685的ICML、00684/704的ICCV及00661窗后workshop名不独立授早公开或强迫全版本史。00693/703/704/01456已有精确项目URL可作必要定点恢复线索，不扩全机构。所见非AB说明无具体withdraw/correction，非全渠道无变化。14同日可继续原已校准v1必要Source；四cross保原潜力，仅做有限原公开事件/日期恢复，尚不签终态隔离或正面Evidence。以上交Ohm一次实际独核，不重前两18或让18自动变全文队列。

## 2026-10-18：最后十四个既有身份的日期与当前事件

范围仅作者 §62 的十四身份，无月份/分类扩池。一次精确 DOI OR 查询，独立 `client-id=arxiv.content` 与 page[size]=25：[DataCite 原件](ROOT_DATE_LAST14_20261018.raw.json)/[头](ROOT_DATE_LAST14_20261018.headers.raw)，HTTP200、61056 bytes、1.812413秒、exit0，meta.total14/page1/totalPages1、无 next。一次 HTTPS export 精确 id_list/max_results25：[当前 Atom](ROOT_CURRENT_LAST14_20261018.raw.xml)/[头](ROOT_CURRENT_LAST14_20261018.headers.raw)，HTTP200、33698 bytes、0.887235秒、exit0、total14。两集合与指定十四身份一致，没有 catchup。

root 实际核全部精确 DOI/题名/作者、arXiv publisher、arxiv.content client、findable、唯一 Submitted-v1/registered/其他日期角色与关联 DOI，并核当前题名/作者、published/updated、comments/出版关系。首次大输出中段被截断，随后单独打印并完整读十四项紧凑身份/原字段和全部当前说明。不是下载成功即审阅完成。按 2025 EDT 日程，全部 Submitted-v1 均严格在 Apr30 18Z 后、May1 18Z 前，条件下界为 May2 00Z/BJT08；registered 仅作条件上界，不改名公告时刻：

| v1 身份 | Submitted 原 UTC | registered 原 UTC | 联合界 |
| --- | --- | --- | --- |
| 2505.00302 | May1 04:50:00Z | May2 01:36:25Z | May2 BJT |
| 2505.00307 | May1 04:59:05Z | May2 01:36:32Z | May2 BJT |
| 2505.00382 | May1 08:19:24Z | May2 01:38:22Z | May2 BJT |
| 2505.00490 | May1 12:45:09Z | May2 01:41:01Z | May2 BJT |
| 2505.00560 | May1 14:36:33Z | May2 01:42:43Z | May2 BJT |
| 2505.00586 | May1 15:16:59Z | May2 01:43:23Z | May2 BJT |
| 2505.00690 | May1 17:52:29Z | May2 01:45:54Z | May2 BJT |
| 2505.00752 | May1 05:24:14Z | May5 01:25:30Z | May2～5 跨日 |
| 2505.00757 | May1 12:10:04Z | May5 01:25:37Z | May2～5 跨日 |
| 2505.03788 | Apr30 19:19:21Z | May8 01:44:30Z | May2～8 跨日 |
| 2505.03790 | May1 09:40:45Z | May8 01:44:33Z | May2～8 跨日 |
| 2505.03792 | May1 14:17:53Z | May8 01:44:35Z | May2～8 跨日 |
| 2505.03793 | May1 15:07:32Z | May8 01:44:37Z | May2～8 跨日 |
| 2505.14845 | May1 15:10:15Z | May22 01:52:04Z | May2～22 跨日 |

人工核有序全区间，再用共用只读函数复算七 bounded、七 cross。没有取跨日区间中的目标日；Updated、Available 月份与 created 不替代 registered。只能支持 arXiv 事件层，不证明全球 first、历史逐字或贡献。

当前后版：00307v3、00586v2、00752v2、03792v2、03793v3，其余九项 v1。00307 的 ICML workshop、00490 RSS、00560 SIGIR、00586 IROS、00690 CVPR 与03792/393 ICML 接纳说明不独自给更早正文公开日；00560 绑定 ACM DOI `10.1145/3726302.3729963`。00690 有精确项目页 `https://metadriverse.github.io/urban-sim/`，03792/393 摘要指向精确代码/项目，可按具名关系定点恢复。没有从所见非摘要说明发现明确撤回/勘误，不签全渠道无变化；后版题摘不能回填 v1 方法。七同日可继续已有准入对应必要证据，七跨日仍需有限具名恢复，不能直接终态保留或归零。交 Ohm 一次独核，作者继续具体贡献/Books，非十四项 Source 已完成。

### 七跨日身份的有限定点恢复与剩余外部缺口

仅对七个精确题名/作者/已有项目执行有限检索，再打开所见原入口。检索相对日期、二手 Submitted 日期和后续引用不作公开依据。下列是本次 web 工具实际可见结果，不冒 HTTP 字节原件或已读全文；没有 catchup、整类/整月扫描或绕过验证。

- **03792 CoSo**：[官方 PMLR 条目](https://proceedings.mlr.press/v267/feng25n.html)同题八作者与 Jul13–19 会期、原文及代码链接；会期不是 May2 首次公开证据。[作者代码仓库](https://github.com/langfengQ/CoSo)同题/作者/arxiv ID 可核，没有绑定本次正文的 May2 dated release；[作者主页](https://langfengq.github.io/)只给 2025.05 accepted 月份。具名 [OpenReview H76PMm7hf2](https://openreview.net/forum?id=H76PMm7hf2)一次打开导向 challenge，未得 Published/Readers，不重试/换 API。仍缺足以收紧 May2～8 界的原公开记录，不是正文不存在。
- **03793 LENSLLM**：[作者仓库](https://github.com/Susan571/LENSLLM)实际重定向 LENSLLM-ICML2025，题名/六作者/arxiv ID 对应，当前 README 无可用 May2 发布记录；不把 git author/commit 日期当 public push。具名 [OpenReview om0CcjvEQh](https://openreview.net/forum?id=om0CcjvEQh)一次导向 challenge。检索可定位该 PDF，不由 PDF 可索引或“accepted ICML”推此前公开日。仍缺该 forum 的公开时间/版本对应或原 dated 正文发布，保 May2～8 界。
- **03788 Grounding UQ**：精确题名/作者与 ID 检索找到[作者 CV](https://trilokpadhi.com/cv/)的同 ID/别名 Seeing is Believing 线索；一次打开 cache miss，未取得 dated 正文。实际[精确 v1 事件页](https://arxiv.org/abs/2505.03788v1)同题十作者、唯一 Apr30 Submitted，不含独立公开日或项目链接。没有借别名扩找全部作者历史；所见不足收紧 May2～8 界。
- **00752 DARTer**：实际[精确 v1 事件页](https://arxiv.org/abs/2505.00752v1)三作者/唯一 Submitted 与 Accepted ICMR2025 可核，无公开日期或代码入口。[作者公开 CV](https://huuuuusy.github.io/files/CV-EN.pdf)的检索片段只定位 ICMR2025/页码，不冒读完整 PDF。会期、二手 May1 卡片和 current v2 都不收紧 May2～5；需要同正文的原公告或日期级作者公开记录。
- **00757 Hailo**：从[作者实验室目录](https://ave.kaist.ac.kr/category/publication/international-conferences/page/2/)进入[唯一目标条目](https://ave.kaist.ac.kr/2026/02/11/efficient-on-chip-implementation-of-4d-radar-based-3d-object-detection-on-hailo-8l/)，同题四作者/2025/ITS Asia Pacific/同 arxiv 链接。Month 空白，URL 的 2026 建页路径不等论文公开日；[官方会议程序](https://www.itsap2025.org/program/06.html?sMenu=06)仅给报告身份与场次。没有 May2 绑定全文的公开记录，保 May2～5 界，不把雷达场景本身作范围或贡献裁决。
- **03790 time-series augmentation**：实际从[作者实验室目录](https://isensing.u-aizu.ac.jp/author/admin/)打开[同题三作者条目](https://isensing.u-aizu.ac.jp/2025/05/27/a-time-series-data-augmentation-model-through-diffusion-and-transformer-integration/)，日期 May27，只引同 arxiv 预印本，晚于当前最晚上界，不能恢复更早实际公告。二手 May8 线索不是官方日期；保 May2～8，缺同正文的原 dated 记录。
- **14845 personality**：精确题名/五作者/日期检索只恢复同 ID 与后续引用；实际[精确 v1 事件页](https://arxiv.org/abs/2505.14845v1)五作者/唯一 Submitted，无额外项目、评论或公开日。不能用 Submitted May1 或 May22 DOI 登记点替代整个 May2～22 区间；缺实际公告或作者绑定正文的日期记录。

上述七项有相关研究潜力，日期缺口未被新材料消除，**提请独立复核作为各自精确外部保留项**：不列确定本窗候选、不评分/写 Books，不支撑零命中、全覆盖或“七项无贡献”。当前已观察到的原入口和具名关系已有限处理，无新可读且尚未使用的日期证据；不是要求无限证明全球 first。重开条件按每项所列原 dated 记录、同 forum 可读 Published/Readers 或可核实际公告；原件到达只重开相关身份。七同日及其它普通证据/书稿工作继续，不因本节为整日签完成。
