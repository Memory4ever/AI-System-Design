# 11076 / 11078 / 11080 / 11082：有限日期独立复核

复核者：mar13_admission_review，非准备者。仅 2026-03-13 已有 Daily 补充 2026-03-12 北京时间自然日。恢复已重读 AGENTS、当前研究/来源 Daily 与 arXiv 范围/Report/Prompt、ROADMAP、本日停点；不移动冻结窗口/旧候选/评分/§4，不读其他日期研究，不授 DAY。

## 实际原件范围

已实际逐份核 [准备包](./SUP_ROOT_FOUR_DATE_CLOSURE.md)、四 `SUP_ROOT_OAI_<ID>.raw` 的 identifier、title、全部 version/date、header datestamp，及 [OAI GET 结果](./SUP_ROOT_FIVE_MANIFEST_RESULT.json)。四份都是唯一 v1、Submitted 2026-03-10 UTC、header datestamp 2026-03-13；两者不是正文首次公开日。

实际核 [11076 DATE3](./SUP_DATE3_11076.raw)、[11078 DATE3](./SUP_DATE3_11078.raw)、[11080 DATE4](./SUP_DATE4_11080.raw)、[11082 DATE3](./SUP_DATE3_11082.raw) 的 DOI/官方 URL、`arxiv.content`、`findable`、created/registered 及全部 dates：registered 分别为 Mar13 01:47:11 / 14 / 17 / 20 UTC，Available 只到 2026-03、Issued 只到年份，Submitted 为 Mar10、Updated 为 Mar13。注册支持已公开上界，但不单独支持 Mar13 首公开；复用既有正常公告/不可预分配 ID 下界后仍只得到 Mar12～13 BJT，跨补充窗边界。

实际回四份本日精确 v1 ABS 的 title/author/Comments/history 身份：DIVE 14 作者、CR-Bench 4 作者、SELF-VLA 4 作者、QoT Yen-Ku Liu / Yun-Cheng Tsai 两作者；只复用已有效的完整题摘/11080 决定 core 准入，不新增机制研究或分数。

## 具名普通路径与停止依据

- **DIVE / 11076**：实际核 [repo](./SUP_ROOT_DIVE_REPO.raw) 与 [正确 master README](./SUP_ROOT_DIVE_README_MASTER.raw)、[fallback 结果](./SUP_ROOT_FOUR_DATE_FALLBACK_RESULT.json)、[分支修正结果](./SUP_ROOT_DIVE_BRANCH_FIX_RESULT.json)。repo 创建于 Mar10 不等于同稿公开；README 同题、14 作者、2603.11076，但 Updates 只写 2026/03。错误 main 的 404 已纠正，不能以错误分支当外部阻断。复核发现 README 另有具名同稿作者项目入口，实际打开并回核保存的 [项目原响应](./SUP_ROOT_DIVE_PROJECT.raw)、[文本](./SUP_ROOT_DIVE_PROJECT.txt)、[GET 结果](./SUP_ROOT_DIVE_PROJECT_RESULT.json)：GET200、29093 bytes、2026-10-10T04:31:30.273454Z，当前标题/14 作者/原 arXiv 链接/BibTeX eprint 同稿；页面未提供日级公开日期，BibTeX 只有 2026。至此这一可执行普通入口也已核，不扩大项目图库、模型/data 或其他作者全库。
- **CR-Bench / 11078**：本日官方 v1 完整题摘/Comments 未给具名 dated 作者稿入口。OAI 仅提交日、注册仅上界，本包当前可用原件不能给 Mar12 日级公告。不是“无贡献”，也不要求证明全网不存在早稿。
- **SELF-VLA / 11080**：官方 v1 视频入口的 URL 月份不是稿件公开日；本包 OAI/注册无法确定 Mar12 或 Mar13。已核 sentinel / resume 机制及算法反侧仍保留，日期缺口不清除这些有效记录；不为日期读全部视频/动作实现。
- **QoT / 11082**：实际核 [repo 原响应](./SUP_ROOT_QOT_REPO.raw) 与 [README](./SUP_ROOT_QOT_README.raw)。API 转向 `yenkuliu/questions-of-thoughts`，创建于 2025-02-11，README 确有 goal→steps→question-answer chains 等框架，却没有本稿精确标题/ID及三域新评价的 dated 公开正文。因此不能把 repo 创建日签作本稿首次公开，也不能由旧框架直接消除本稿局部反退条件的潜力。

以上是四个具名材料的有限必要日期检查，不是全月/全站召回。搜索命中日、OAI 修改 stamp、Submitted、Updated、项目 repo 创建或 BibTeX 年份均未补造成公开日；旧官方历史公告恢复限制有效复用，不再次遍历全月列表。

## 裁决

**四项必要日期终态隔离提案通过；四项本窗日级归属本身未通过。** 保留原潜在贡献，不计确定当窗候选、不评分、不授 Source/Books/无遗漏。它们是必要日期原件无法区分跨窗区间的保留项，不是把尚未读必要正文的普通研究待办外部化。

每 ID 只请求一次：同稿身份明确的官方 arXiv 日公告，或作者原始 dated 公开正文，足以判断 Mar12 本次事件即可；不要求时分秒、全部代码/评审/完整版本史。取得哪一项只重开哪一项日期；窗内再进入最低必要评分/证据/owner，早稿/窗外则按具体事件归属和去重处理。此裁决不替代后续本日报六部分验收。
