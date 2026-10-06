# 12/17 原始来源停止记录（增量）

本轮实际检查 2026-10-02，Asia/Shanghai。只记录必要入口、停止点和判断，不是独立验收。

## 增量停止点

- Z.ai：[Research 第2页](https://www.zhipuai.cn/zh/research?page=2) 实际累计18条，底部“没有更多”；目标附近为2025/12/21 GLM-4.7，随后12/10 GLM-TTS、12/09 ASR-Nano、12/08 AutoGLM、12/07 GLM-4.6V。研究目录已越过本窗，未发现12/16条目。release notes 的12/22与12/11邻接切片单独保留，不替论文目录。
- Seed：`article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true`，实际15行，`total:49,has_more:true,next_page_token:20`。目标附近12/24 SeedProver1.5、12/18 Seed1.8、12/16 Seedance、12/02 GR-RL、11/27 DepthAnything3，继续下至7/23；已越过窗口，停止在本页相邻段，不扩全月。Seedance Blog 原始 `PublishDate=1765882058000`，精确转换12/16 18:47:38+08，见 SEED_DATE_REQUEST；论文目录展示日期不替论文公告。
- GitHub 精确提交区间 `[2025-12-16T01:00Z,2025-12-17T01:00Z)`，API使用until=00:59:59Z、per_page=100：QwenLM/Qwen3、deepseek-ai/DeepSeek-V3、MoonshotAI/Kimi-K2均返回空数组，只证明指定仓库提交切片无记录。Tencent-Hunyuan/HunyuanAvatar只有依赖版本约束变更（transformers>=4.50、gradio>4.42），无新增机制/安全理由，按普通兼容性维护关闭；T1为空。HunyuanVideo-1.5一项“update sp communication”及HY-WorldPlay 27项、MiMo-V2-Flash两项已触发定点历史版本阅读，未以提交时刻证明公开。
- OpenAI Images 正文已再次检查全部正文链接：没有该版本 system-card 链接；补检 `site:openai.com "GPT Image 1.5" "system card"` 未恢复独立材料，不能宣称安全卡不存在或已审。其发布正文负侧结论不扩大到独立安全报告。官方日期补检 `site:openai.com "December 16, 2025" research -site:community.openai.com` 返回已读两项科研应用及产品 Images；索引补检的覆盖限制保留，不当历史原始目录完备证明。
- Anthropic 当前Research列表只显示前10项，历史publicationList原始HTML恢复在本轮出现SSL EOF；网页替代仍只有前10项。本窗已取得alignment-faking原文且必要正文已读，未得到历史目录停止点；不能由有限搜索无命中改写为来源零事件。
- DeepMind `?page=4` 实际返回当前首页，不能当历史第4页；改用原站页面明确的 `/blog/page/4/` 恢复。这条修正保留，避免查询参数未生效产生伪覆盖。

以上时间是本轮记录检查时间，不是材料公开时刻。

## 目录收尾

- Google DeepMind正确历史页 `/blog/page/4/`：24条跨Feb2026至Nov2025，December研究/模型切片逐个回原站字段；Gemma Scope2 `datePublished=2025-12-19T12:00Z`、Genesis `2025-12-18T19:00Z`、UK AISI `2025-12-11T00:06:40.959Z`、UK government `2025-12-10T14:59:21.093Z`、FACTS `2025-12-09T11:29:03.922Z`。外链Gemini3Flash JSON-LD `2025-12-17T16:00Z`（属12/18窗口）、audio updates `2025-12-12T17:00Z`，均不挪入12/17。科学作物项范围明确暂缓，年度回顾不是新增独立机制事件。Google Research publications首屏年字段不授论文首发；按窗原始论文发布日期仍缺，不把Blog检查升格为全部publications通过。
- Anthropic Alignment Blog December原始相邻段：Bloom/Activation Oracles原文Dec19，alignment-faking Dec16，Auditing replication原文Dec12，Fellows招聘不属研究贡献，Selective Gradient Masking原文Dec8；向下November即停止。Research主目录动态历史部分仍未恢复；Alignment切片不替经济/其他研究目录。失败的publicationList一次SSL EOF及网页替代10项已经记录，不重复请求。
- Moonshot持续更新[changelog](https://platform.kimi.com/blog/posts/changelog)本机全文可读：最新明确记录Nov6 K2 Think，随后Oct27→Sep5等；没有Dec段。结合26条Blog与指定Kimi-K2 repo切片，当前约定入口已作有界检查；不据此证明未公开研究不存在。
- OpenAI Research news原始网页仅9条当前2026项加Load more；RSS有限替代HTTP403，精确date+topic辅助搜索仅恢复已读两项科学/Images。历史目录段保留外部缺口，不能用当前9条给本窗全源零事件。重开条件为官方历史目录分页/带窗口过滤的可读响应或历史RSS，不重复相同失败入口。
- arXiv具体系统词组14行与ML上下文AND查询46行均实达页尾，无Next；ML上下文仍命中领域应用，已按标题排除确定的超声/天文/地质/农业/传统任务应用，非基础模型系统。决定准入事实含糊的回精确v1全文题摘。旧179/107语言及49多模态宽缓冲只作线索，非本窗公告池或逐项队列；未把240裸kernel库存转成候选。新潜在贡献、反证和普通负侧见ADMISSION_ADDITIONS；历史first-public窄恢复依根线程ARXIV_DATE_RECOVERY的实际路径，不能从submitted或月归属证明落窗。

- MiniMax：[官方研究 Blog](https://www.minimax.io/blog) 当前公开页共 12 个研究条目；目标附近相邻 `2025-12-23 M2.1` 与 `2025-10-27 M2 & Agent`，可读页面无 Next/load-more。本窗未发现研究 Blog 条目；不替其他未公开材料证明绝无遗漏。M2.1 是后续日线索，不挪入 12/17。
- ERNIE：[官方中文 Blog](https://ernie.baidu.com/blog/zh/) 第 1 页 10 条，已读到 `2025-12-23 ERNIE-5.0-Preview-1203`、`2025-12-09 Preview-1103`，尾部 `2025-11-21 Preview-1120`，链接为下一页 2/2。有界停止于已越过本窗的 Nov 21，不逐项读窗外产品结果；本窗未发现该目录条目。
- DeepSeek：[官方 Change Log](https://api-docs.deepseek.com/updates) 原始 HTML 本机成功，网页工具超时不影响已取正文。顺序在 2026-04-24 与 2025-12-01 V3.2 之间无 Dec 16/17 记录；Speciale 临时 endpoint 在 `2025-12-15 15:59 UTC` 到期，早于本窗起点，不误计本窗事件。页面目录到 2024-05-17，无分页。此停止只覆盖官方变更表，GitHub 本窗实质研究变化仍需有界检查。
- Moonshot：[Platform Blog](https://platform.kimi.com/blog) 当前列出 26 条，最新 `2025-11-07 新功能发布记录`，再到 Nov 6 K2 Thinking；末条2024-05-29，无 Next。已打开持续更新的新功能记录，仍须区分本窗研究机制与普通产品变化；组织入口不等于历史事件处理完。
- Google Research：[2025 年 Blog 页](https://research.google/blog/2025/) 第 1 页目标相邻 Dec 18 年度回顾、Dec 15 Paper Assistant Tool，向下到 Nov 12。目录切片没有 Dec 16 条目；DeepMind 与 publication 首公开恢复另处理，不能由 Blog 给全年论文零命中证明。
- Hunyuan：Research 网页读取及浏览器有限恢复失败后，实际读取官方公开前端的 `/blog` 路由；入口模块 `index-cEoitnb7.js` 指向 `POST /api/blog/publicList`，主模块 host mapping 为 `https://api.hunyuan.tencent.com`。本轮请求 `{pageNum:1,pageSize:20,renderType:0}`，响应 `code:0,totalNum:11,list长度11`；`renderType:0` 是“全部”。当前 11 条仅2026，最早 Learning from context is harder than we thought（显示时间1770092288）；不据此声称2025无条目。保留历史目录缺口，并继续 Tencent-Hunyuan 与 T1 官方替代入口。没有遍历管理接口。
- Seed：官方公开前端实际调用 `GET /api/get_article_list_v2`，分页字段 `page_token/count`，支持 `publish_year`。本轮 query `article_type=1&publish_year=2025&count=20&page_token=0&order_desc=true`，`x-tt-locale:US`，响应 `has_more:true,total:94,next_page_token:20`、实际18行。前两条置顶是 Seedance 与 GR-RL，随后 Seed3D Oct 21 向下到 June 25；置顶不是全体时间排序，不能把首两项自动当最新公告。Seedance `PublishDate=1765728000000` 编码为 Dec 15 北京00:00，且网页 Blog 标 Dec 16；此人工展示日字段不证明个体论文首公开。Blog 类型与真实排序仍在检查。
- arXiv 收窄系统主题：[ARXIV_SYSTEM_FOCUSED.md](./ARXIV_SYSTEM_FOCUSED.md) 实际一页14行，无有效 Next。查询以具体 GPU kernel/collective communication/LLM inference/distributed training/speculative decoding/MoE 词组恢复线索，时间字段仍是 submitted_date_first [Dec 14,Dec 16)。已实际读 gpu_ext、Janus、SIGMA、SonicMoE、EARS、DTop-p 精确 v1 完整题摘；未授个体公告归属。SonicMoE 实际 v1提交 Dec16 04:39:10UTC、DTop-p Dec16 01:28:57UTC，搜索日期与精确 abs 不一致，后者身份字段优先但仍非公开时刻。
