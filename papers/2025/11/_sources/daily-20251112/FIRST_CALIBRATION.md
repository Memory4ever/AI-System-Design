# 2025-11-12 首批准入校准包

作者：Noether。准备时间：2026-10-04T19:29:35+08:00。以下为首交历史；最新独立结果与owner决定见末段。
窗口：`[2025-11-11T09:00:00+08:00, 2025-11-12T09:00:00+08:00)`。
这是一个家族、两项方向，不是两篇已落窗候选；原日期资格交独立定点核验。普通来源仍继续。

## 1. 原始身份与日期问题

- 家族：[GPT-5.1 发布](https://openai.com/index/gpt-5-1/) 与 [System Card Addendum](https://openai.com/index/gpt-5-system-card-addendum-gpt-5-1/)。实际原 [RSS](./openai.xml) 两条均为 `Wed, 12 Nov 2025 00:00:00 GMT`，换算 BJT 11/12 08:00，字段时刻落窗。不能删掉该字段或写成没有日期原证据。
- 官网发布页、Addendum、[Safety Hub](https://deploymentsafety.openai.com/gpt-5-1) 均只显示 November 12, 2025，未给正文发布时区/时刻；它们本身不能证明这个相交自然日完全落窗。
- 当前需要独立确认：官方 RSS 的午夜 pubDate 能否支撑本次首次公开归属，而不是站点日期规范化字段。目前没有已取得的原材料证明 RSS 错误，也没有更精确的官方发布时刻；不声明已证日期冲突，也不凭记忆把事件移到后一天。
- 有限恢复：原博客 native 请求 403（[响应](./gpt51.html)）；两批精确 official X/官网日期查询未恢复 OpenAI 账号可用时刻；研究者 Adi Ganesh 的原搜索结果显示 `1:23 PM Nov 12` 但时区未知，直接打开 [原帖](https://x.com/_adiganesh/status/1988689155057148376) 403。停止重复搜索，不推算平台 ID。原 query/失败见 [第一次](./12-gpt-date-source.txt)、[第二次/PDF](./12-gpt51-pdf-date.txt)、[最后一次](./12-date-final.txt)。最小重开材料是官方具有时区的首次公告、未规范化 published 时间，或能够将首次公开上下界完全夹在窗口内的原始证据；不是全部实验附件。

## 2. 拟准入方向：自适应推理的实际质量/成本分配

原约束：固定 thinking budget 会在简单与困难请求间浪费或不足 → 本次 Instant 可自行决定先思考，Thinking 对不同问题更细地分配思考时间；厂商在代表性 ChatGPT 任务上报告最快约两倍快、最慢约两倍慢，两者同为 Standard thinking → 可改变“新版本推理速度单向改善”的判断，不能改写为 runtime SLO 保证。

暂拟 `2+1+2=5`，不将品牌、路由一般原则或可关联章节计分。已实际读发布页对应核心（原响应 L156–160、L403–421）；没有公开 gate 算法、训练目标、硬件、prompt/output 长度、并发/SLO 或 endpoint 对照，均为 Not Disclosed。Auto 是继续既有路由，不当新 router 机制；API 是 later this week，不采用后来 API 的配置补造本窗机制。

Owner 仅路由线索：`INFER-REQUEST-LIFECYCLE` / `INFER-SCHEDULING` 中质量成本行为边界，不因没有 GPT-5.1 名称就提出长期缺口。现阶段没有 Books 写入请求；日期若通过，仍需证据独立核验并与 owner 具体正文比较，可能只保留版本报告。原文见 [发布/原页](./12-first-original.txt)。

## 3. 重要反侧：baseline 更新不能简化为安全整体提高

原约束：换代模型被笼统解读为安全提高 → 本 card 提供逐基线、逐风险项的新旧比较，离线困难生产样本与线上稀有 prevalence 可能方向不同 → 要保留具体退步与低样本/置信区间，而不是用单一总榜消除反侧。

暂拟 `2+1+2=5`，因安全/设计反侧，已深入读受影响核心：Hub 全文及原 PDF 五页文本，未遍历不相关附件。PDF [原文](https://cdn.openai.com/pdf/4173ec8d-1229-47db-96de-06d87147e07e/5_1_system_card.pdf) 来自 Hub 的 View PDF 链接，实际原响应见 [全文与表](./12-gpt51-pdf-date.txt)、[Hub](./12-core-headers.txt)。截图接口只返回引用文本，**未作像素表格目检**，不把截图请求当实际视觉核验。

具体有效反侧：Table 1 的 not_unsafe 越高越好；Thinking harassment `.815→.747`、hate `.883→.839`、sexual `.906→.895`。Instant 与 Oct3 比：sexual `.951→.917`、violence `.953→.938`、mental health `.944→.883`、emotional reliance `.986→.945`；与 Aug15 比较则多个方向改善，不能混用 baseline。离线是刻意挑选以前出错的困难生产问题，不是总体线上流行率。线上稀有事件的小样本/宽误差与离线困难集不是同一问题；Instant mental health 线上轻微低置信改善不能抹掉离线退步。

StrongReject 与 vision 表已读，包括 Thinking StrongReject `.974→.967`、vision self-harm `.976→.936`；它们只支持该评价配置，不代表全攻击保证。新风险评估类别在原文明确来自此前 sensitive-conversations addendum，不能当本次首次机制；Preparedness mitigation 基本延续 GPT-5，也不表述为新消除全部风险。

Owner 路由线索：`PLATFORM-EVALUATION-SYSTEM` 的 baseline/protocol 与局部安全反证；现阶段未读 Books owner，不声明已有覆盖/缺口，不请求共享写入。

## 4. 代表性不采用侧写与未核范围

- 页面里的“更温暖/更聪明”整体措辞不是独立机制；只采用具体适应性行为和有配置边界的表，不把聊天展示样例当 production 证据。新增 personality 控制与 ongoing preference 的产品行为不自动推出训练算法变化；未作该方向长期采用判断。
- Auto `will continue` 路由不是本次首次事件；本条原声明足以关闭“本次新增路由算法”这一命题，不等于否认所有质量/成本增量。
- 不将官方 PDF 中完整 baseline 表转换为每个风险项各一个候选家族。
- 待独立：日期字段语义、上述两项方向的准入、表列/数值及限制归因。尚未核 Books owner；普通其他14源尾项/arXiv仍在继续，日级尚不 ready。

## 5. 接手位置

请 root 分配 Ohm/Carver 非作者校准本文件和上述原 raw；作者未进行独立验收。准备一批即交，未等待11 DAY，也未停止12其他来源。

## 6. 最新权限同步

2026-10-04T21:00:17+08:00实际读[Ohm FIRST](FIRST_INDEPENDENT_REVIEW.md)：20:33:29同家族准入、官方RSS落窗及2025必要核心通过，20:53:26重申无需继续日期空查。上面的日期待核为过程历史，现已解除；真实时区冲突原件后来到达才定点重开。Thinking退步不止上列三项，Table1其余下降亦保留；厂商prose不是全表。必要owner正文与相邻已实际比较，两个方向最终仅报告，完整差额/停止依据见[EVIDENCE_OWNER_NOTES](EVIDENCE_OWNER_NOTES.md)；随后实际读[Ohm THIRD §3](THIRD_INDEPENDENT_REVIEW.md)21:02:19独立owner对照支持该决定，非DAY完成。
