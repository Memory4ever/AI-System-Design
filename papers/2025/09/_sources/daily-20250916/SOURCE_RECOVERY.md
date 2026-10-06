# 2025-09-16 有限恢复与停止位置

作者 Tesla；执行至2026-10-06T11:48:17+08:00。仅服务本日窗口，遵循当前研究合同§2–6/Report合同§3–4，不授无遗漏。

## 原始入口恢复

- Anthropic `official-anthropic.html`：JSONDecoder解析self.__next_f.push中的JSON字符串与RSC记录，得到172个唯一publication身份。只检查本窗切片：Economic Index两篇原值分别2025-09-15T09:00:00.000Z、2025-09-15T20:33:00.000Z，均在窗内；核心内容为地理/企业采纳和经济估算，不是模型或系统机制，关闭本项目贡献。其余历史数组只用于日期定位，不变成全文队列。
- Google Research实际web恢复`/blog/2025/09/`，第1/2页日期序列到Sep11，已越过Sep15本日下界；Sep16的Learn Your Way与Sep12的VaultGemma夹住本窗附近，不把当前首页当历史覆盖。原记录`16reopen.json`。另一个curl路线25秒超时，web路线成功，保留差异。DeepMind Research原web/curl故障与日期补检未恢复确定历史列表，隔离，不称Google双入口全覆盖。
- Seed type2：`/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true`，`seed-blog-api.json`。实际15条、total49、has_more=true、next_page_token20。区分置顶/非置顶，非置顶日期从Oct23跨Aug21并下到Jul14，本窗附近无目录条目；跨过下界停止，不遍历全年正文。Unix毫秒PublishDate原值保留，ArticleID不作公开时间。
- Seed type1同参数：`seed-paper-api.json`与CN Locale重试`seed-paper-cn.json`；total94、has_more=true但无sub_article_list。公开论文页当前20/242、1/13只到2026May；不把94计为已读或0论文，历史论文切片隔离。
- Hunyuan：POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":100,"renderType":0}`，`hunyuan-api.json`实际9条，displayPublishTime最早1770090898（2026年），没有历史覆盖保证。Research壳保留；浏览器子线程被拒绝可见性/两次超时，GitHub/T1有限入口见`16fallback.json`，当前仓库不能补齐历史“全部”。
- Z.ai：Research首页Next数据15条、nextPage2、hasMoretrue；从真实client `zai-research-client.js`确认按钮是设置page后路由跳转，实际取`/zh/research?page=2`。第二页累计18条、nextPage3、hasMorefalse，最早createAt2025-12-07T16:00:00.000Z。页内createdAt/updatedAt不是论文首公开。历史九月论文目录仍缺，发布说明Sep30/Aug11夹窗不能替代Research。
- ERNIE实际第二页已跨本日：Sep12 PLAS、Aug14 FastDeploy；页面2只剩前页导航。MiMo保留Paper8行，Sep19Audio/Jun4VL夹本日；Qwen保留列表Sep23Guard/Aug19ImageEdit夹本日。Kimi保留Blog全日期序列，Sep16折扣与Sep5模型更新夹本日。各自只声明该有限目录，不声明全站修订覆盖。
- MiniMax技术Blog当前目录与Agent Tech Blog/llms.txt均实际打开，后者已为当前Code文档且无目标历史研究列表；US/CN博客/组织有限补检没有恢复九月完整切片。DeepSeek当前主页无日期归档，未把首页当历史阴性证据。OpenAI页面curl403但web可读本日附近GPT5Codex；官方Blog显示Sep15无时区，不能擅自设北京时间或UTC。

## arXiv

`arxiv-theme.xml`229条提交区间线索；`arxiv-systems.xml`补查attention/quantization/kernel/collective/communication/accelerator/MoE/RAG/retrieval/memory/compiler并限定清单12分类，start0/max100/ascending，66条全部与首查身份重复。无新增全文队列。

`arxiv-revision-theme.xml`是lastUpdatedDate同区间主题查，218条，没有published早于区间的条目；只记录该实际查询结果，不授所有修订已覆盖。月CL列表1–2000/2214仅新命名查漏；日路径报无效时段、直2509路由404，年份月份路径可取。版本history的submitted与APIpublished均不能替代本日公告。官方历史日公告/单篇原首发目前没有取得；不计零论文。

## 重开条件

仅补相应来源的2025-09-15T09:00+08至09-16T09:00+08历史列表、真实公告或作者原始首发证据；必要范围须完全落窗。对单篇用确切Source Family/版本定位，不扩月。目录到达后只查本窗标题与含糊项题摘，不能把总库存当全文队列。
