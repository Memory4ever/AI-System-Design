# 04/20 窄批次联合日期证据（作者检查，非独立 Gate）

窗口为`[2026-04-19T09:00:00+08:00,2026-04-20T09:00:00+08:00)`。本轮`/root/apr20_resume`实际读取[official availability](https://info.arxiv.org/help/availability.html)的ID assignment、announcement schedule和2026 holidays，并实际解析旧原始OAI文件与owner库存。下文不把DOI created、Submitted、Updated或OAI单独改名first-public。

## 必要窄链

1. 官方规则明确永久ID在自动公开公告过程分配，不能预先生成或回拨；常规Sunday20:00 EDT公告对应04/20 00:00UTC/08:00北京，04/19–20无所列holiday。
2. 原始[OAI cs响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)保存`verb=ListIdentifiers;metadataPrefix=arXivRaw;from=2026-04-20;until=2026-04-20;set=cs`，`responseDate=2026-09-03T03:30:59Z`，没有resumptionToken。它是metadata日批次印证而非网页公开瞬时证明。本轮实际读出15351、15357、15368、15461、16224、16231的header datestamp均04/20、无deleted标记。
3. [原库存](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)447个相关分类身份位于15314～16299，与前批04/17相关库存末15312、后批04/21相关库存首16301交接；跨分类不按号缺口制造待审任务。本轮实际核字段边界：15314的v1Updated=04/20T00:00:05Z；16299=04/20T01:04:41Z；下一批16301=04/21T00:00:05Z。原447中330有同日OAI直接印证，117有后改/恢复，不继承它们的旧贡献/完成标签。
4. 首次题摘工作集合中的125额外线索，原v1Updated全位于本日00～01Z；这个字段只作与ID相邻批次、官方公开槽及OAI一致性的交叉检查，不是独立first-public规则。已知后改OAI（如15367=05/04、15451=04/23、16076=05/22）不将原家族移日；真正有早于该批次的官方正文或未能确认的事件按家族定点消歧。

联合链支持将该有限工作集合归入04/20 08:00公开公告槽，使用`[2026-04-20T08:00:00+08:00,2026-04-20T09:00:00+08:00)`作为报告中的公开时间范围；不把Submitted Apr11/16/17当首发，也不对每一篇遍历全部旧版本。43个晚Updated身份不是43个必须迁日/候选；它们若有题摘贡献才定点确认，不能将其余宽库存全部挂pending。独立复核仍须检查本日集合、边界与具体事件身份。

### 2604.15549v1 的具名日期复查

[官方 exact-v1](https://arxiv.org/html/2604.15549v1)页眉 `16 Apr 2026`是版本/提交身份，不当作当日公开。原始[04/20 cs OAI 响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)该 header 为 `oai:arXiv.org:2604.15549`、`datestamp=2026-04-20`、`setSpec=cs:cs:LG`；[原库存](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)保留 `v1_submission=2026-04-16T21:56:57Z`、`v1_updated=2026-04-20T00:11:12Z` 及 `official_arxiv_oai_direct`。与上方官方 Sunday 20:00 EDT 公告、公布时赋 ID 规则及 15314～16299 相邻批次联合，支持 v1 首公开落本窗北京时间 04/20 08:00 公告槽；不把 Submitted、Updated、OAI 或 DOI-created 任一孤证称 first-public。本项原贡献前闭已因具体主线增量由 root 有界非作者纠正，日期仍待整日独立 Gate。

### 2604.16004v1 / 2604.16007v1 的具名日期复查

[官方 AgentV-RL exact-v1](https://arxiv.org/html/2604.16004v1)与[官方 MemExplorer exact-v1](https://arxiv.org/html/2604.16007v1)页眉均为 `17 Apr 2026`版本/提交身份。原始同一[04/20 cs OAI 响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)分别含 `oai:arXiv.org:2604.16004`、`datestamp=2026-04-20`、`cs:cs:CL` 及 `oai:arXiv.org:2604.16007`、`datestamp=2026-04-20`、`cs:cs:AR`；[原库存](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)保留前者 `v1_submission=2026-04-17T12:27:36Z`/`v1_updated=2026-04-20T00:46:00Z`、后者 `12:29:54Z`/`00:46:03Z`，均 OAI direct。与官方 Sunday 20:00 EDT 公告和 15314～16299 相邻 ID 批次联合，支持两份 exact-v1 处于本窗 08:00 北京公告槽；不把上述任何单字段称首次公开或据页眉移至 04/17。整日独立日期 Gate 仍待核。

### 2604.15660v1 的具名日期复查

[官方 abs](https://arxiv.org/abs/2604.15660)给出的 `Submitted`/v1 历史是 `Fri, 17 Apr 2026 03:27:27 UTC`；[官方 HTML](https://arxiv.org/html/2604.15660v1)页眉 `17 Apr 2026` 属同一提交/版本字段，**二者均不单独证明 04/17 已公开**。现存原始[04/20 cs OAI 响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)的该 ID header 为 `oai:arXiv.org:2604.15660`、`datestamp=2026-04-20`、`setSpec=cs:cs:CR`，并非后改 datestamp；[owner 原始库存记录](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)保留 `v1_updated=2026-04-20T00:22:02Z`、`v1_submission=2026-04-17T03:27:27Z`、OAI direct，与本日 15314～16299 的相邻 ID 批及官方 Sunday 20:00 EDT 公告/ID 分配规则一致。[官方 cs.CR 2026-04 月目录](https://arxiv.org/list/cs.CR/2026-04?skip=0&show=2000)亦列该 v1 身份，但仅作身份补证、不把整月目录说成本日时间戳。联合证据支持把首次公开定位本窗 04/20 08:00 北京公告槽，不将 Submitted、Updated、OAI 或 DOI-created 任一孤证改名 first-public。该具名判定仍交整日独立 Gate 检查。

### 2604.16198v1 的具名日期复查

[官方 abs](https://arxiv.org/abs/2604.16198)的 v1 history 为 `Submitted Fri, 17 Apr 2026 16:08:05 UTC`，这是提交字段而非公开时间。原始同一[04/20 cs OAI 响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)的该 ID header 为 `oai:arXiv.org:2604.16198`、`datestamp=2026-04-20`、`setSpec=cs:cs:SE`；[owner 库存记录](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)的 `v1_updated=2026-04-20T00:58:24Z`、`v1_submission=2026-04-17T16:08:05Z`、OAI direct 亦在本日 15314～16299 批。与上方官方 Sunday 20:00 EDT 公告及自动 ID 分配规则联合，这一具名 family 属 04/20 北京08:00公告槽，不依赖任一孤立 Submitted/Updated/OAI/DOI 字段。非作者日级日期 Gate 仍未签。

### 2604.15663v1 的具名日期复查

[官方 exact-v1 abs](https://arxiv.org/abs/2604.15663v1)列 `Submitted Fri, 17 Apr 2026 03:35:35 UTC`，仅是投稿历史。现存原始[04/20 cs OAI 响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)中该 ID 的 header 为 `oai:arXiv.org:2604.15663`、`datestamp=2026-04-20`、`setSpec=cs:cs:SE` 与 `cs:cs:AI`；[owner 库存](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)保留 `v1_updated=2026-04-20T00:22:28Z`、`v1_submission=2026-04-17T03:35:35Z` 及 OAI direct。联合本日相邻 ID 批、官方 Sunday 20:00 EDT 公告与公布时自动赋 ID 的规则，支持该 v1 首公开落 04/20 北京 08:00 公告槽，而不是将 Submitted、Updated、OAI 或 DOI-created 任一字段孤立当作 first-public。日级非作者日期 Gate 仍待执行。

### 2604.15672v1 的具名日期复查（Books 写前待核项）

[官方 exact-v1 abs](https://arxiv.org/abs/2604.15672v1)列 `Submitted Fri, 17 Apr 2026 03:52:23 UTC`，不据此迁到 04/17。原始[04/20 cs OAI 响应](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)有 `oai:arXiv.org:2604.15672`、`datestamp=2026-04-20`、`setSpec=cs:cs:LG` 与 `cs:cs:CL`；[owner 库存](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)给 `v1_updated=2026-04-20T00:23:03Z`、`v1_submission=2026-04-17T03:52:23Z` 及 OAI direct。与该批相邻 ID 边界、官方 Sunday 20:00 EDT 公告及其自动赋 ID 规则联合，支持该 v1 落本窗 08:00 北京公告槽，不把任一代理字段独称首公开。此日期检查不预支该项 source→Ch48 采用核或整日 Gate。

### 六项旧入口中三个非同日 OAI 的窄版本消歧

apr01 已通过**准入**而仍待独立 Evidence 的六项中，15351/15614/16090 的原[04/20 cs OAI 批](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-20-cs.xml)可直接印证该日 datestamp；15414/15451/16076 的[原库存](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)分别显示 OAI 空、后改至 04/23、后改至 05/22，不能把当前 OAI 当作三篇原始公开日证据。定点再看[15414 exact-v1 abs](https://arxiv.org/abs/2604.15414v1)、[15451 exact-v1 abs](https://arxiv.org/abs/2604.15451v1)和[16076 官方版本页](https://arxiv.org/abs/2604.16076)：v1 `Submitted` 分别 04/16T17:06:54Z、04/16T18:10:18Z、04/17T14:04:14Z；后续 v2 分别在 06/09、04/21、05/21，不能把后改版本写成本日原始内容。原库存的 v1 `Updated` 分别 04/20T00:02:27Z、00:03:42Z、00:51:34Z，仅与本日相邻 ID 15314～16299 的公告/赋 ID 批次相互印证。结合官方 Sunday 20:00 EDT 公告及 ID 公布时分配规则，支持三篇 v1 的本窗归属，但不把 Submitted、Updated、DOI created 或后改 OAI 任一孤证当作首公开。后续若有更早的官方正文/公告或具体修订信号，只重开相应家族；六项 Evidence 与整日日期 Gate 仍未签。

## 发现覆盖边界

本轮实际访问`https://arxiv.org/list/cs.AR/2026-04?skip=0&show=2000`得到200、227个整月条目；这是补检目录不是日归属证明。Web工具对cs.CL同请求429，不据此写零命中。既有447完整标题浏览用于有界查漏，150完整题摘为贡献工作，不声称全447题摘/全文或全学科召回。仍需处理具体准入消歧、精确版本当前事件信号与必要正文，普通未读不称外部受阻。

Seed `AgentWorld/2604.18292`的CMS卡片04/19T16Z与后来arXiv Submitted04/20T14:01:10Z不构成当时正文已公开的证明；`15483`同family早发与`16009`实际v1/修订信号仍需定点核，未借上述通用批次规则解除身份问题。本文件未完成独立语义验收，也未冻结候选分母。

后续作者状态：16009 已按 exact-v1/仓库必要源作受限标准处置，旧社交摘要修复线索未当已核事实；15483仍维持单项首公开身份隔离。150题摘中作者逆向准入最初拟88/61/1，之后16171/15609/15809因受限条件替代设计自纠恢复为91/58/1；再经[root 八项独立重判](./V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)恢复15351/15451/15614/16076/15705/15706/16079/16135，现拟冻结99候选/50贡献前关闭/1日期隔离，见[反向审计后记](./V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)与正式日20§3–6。这些贡献处置不增强本文件原有的 first-public 证明力，最终日期和候选分母仍需非作者日级核。

**同日后续工作态：**上段99/50/1为当时阶段数。root 又对15675/15583/15771作[必要原文逆向准入裁决](./V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)，本日作者同步为102候选/47贡献前关闭/15483日期隔离1；三项均以官方 exact-v1 家族进入原本的窄04/20公告批次推定范围，未把论文页眉、Submitted、Updated或单一OAI当作独立公开证明。贡献恢复不增加日期证据，故首公开联合链及十四来源仍交独立日级 Gate；15483与Seed AgentWorld的身份隔离不变。
