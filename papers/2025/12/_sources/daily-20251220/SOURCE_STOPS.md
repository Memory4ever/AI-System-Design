# 12/20 原始范围与停止记录

本日窗口[2025-12-19T09:00,2025-12-20T09:00)+08；2026-10-02实际。独立读取原始固定历史目录`../daily-20251217/SOURCE_STOPS.md`具体字段及停止段，不复用别日评分/完成结论；新主题查询与repo原始响应只写本日。固定历史相邻段可复用，不表示它们已证全网无事件。

## 14每日源

- OpenAI：原Research当前9项/LoadMore、RSS403已有限失败；原Dec18 Codex/U18仅日精度与必要正文已有明确身份，非20新公开。目录历史未恢复，本日终态隔离，重开要求官方历史分页或RSS精确窗；不重复同接口，不用辅助无结果证明零。
- Anthropic：原Research10项/publicationListSSL EOF及有限网页替代不恢复2025历史；AlignmentDecember原段Dec19 Bloom/Activation→Dec16AF→Dec12Audit→Dec8Mask。本日两个Dec19核心/方法/限制可读已定点读，Bloom评价补段继续；HTML一次默认UA403，采用原有效researchUA成功，meta中没有published/date/modified字段。既有官方mainBlog日粒度替代仍不授09边界；不无限探date。重开精确公开时刻或全落窗的官方上下界。通用历史目录缺口不升级零事件。
- GoogleAI：原DeepMind正确`/blog/page/4/`24条Feb2026→Nov2025，精确本日Scope2 release官方12Z。GenesisDec18T19Z此前窗且science范围；FlashDec17T16Z/T5Dec18T18:30Z都是旧事件。GoogleResearch2025原12条anchor Dec18yearreview→Dec15PaperAssistant→Dec12→Nov12，本日无新增目录项；Publications首屏年字段非first-public，历史缺口隔离。Scope必要PDF/Books差异另见提案，不等同旧论文首公开。
- Meta：原Research global_search?page3混合24条中的Dec18四水印原题摘身份未变（posthoc为2512.16904v1，本日arXiv再次发现按精确identity去重，不重复算家族）。本日没有明确新release时间；不得从Dec18整天设定20落窗。lidarDec15原页/Dec17目录明确传感器数据应用关闭；SAM/PEAV失败路径不重探。四水印日期隔离，接受官方individualfirst-public/公告上下界后定点重开。
- Qwen：原旧BlogSep23迁移，动态新站历史缺口有限恢复已穷尽；本日Qwen3 commitroute空hasNextfalse，不代目录。缺口仅官方历史事件页到达时重开。
- DeepSeek：原官方updates2026Apr24（当前亦有Sep10）→2025Dec1→2024May17，无分页；本日V3 repo空无Next。Dec15临时endpoint结束早于窗口，不挪为新机制。
- Moonshot：原Blog26条Nov7/6→2024May29无Next；原changelogNov6→Oct27→Sep5；本日KimiK2 repo空无Next。
- Hunyuan：原publicList全部renderType0响应code0,total11/list11仅2026，历史2025缺口隔离；本日T1空、Video1.5三、WorldPlay四精确committedDate在窗内，patch见下，pushedDate=null不授首次公开。
- ZAI：原Researchpage2累计18，底部无More；Dec21GLM4.7→Dec10TTS→9ASR→8Auto→7V，当前本日相邻段没有目录项。GLM4.7后日线索不提前读以免扩窗。
- Seed：原BlogAPI type2/year2025/count20/page0/orderdesc 15行total49/next20，目标相邻Dec24Prover1.5→Dec18Seed1.8→Dec16Seedance→Dec2；paperstype1同分页18行total94，pinSeedance/GRRL后Oct21→Jun25非严格排序。Seed1.8原1765987200000是Dec18午夜日编码，旧card当前重定向Seed2.1；真实精确旧材料缺口隔离，不授20事件。不要把Seedance论文submitted补别的Blog时间。
- ERNIE：原Blogpage1 10条Dec23→Dec9→Nov21，Next2/2更旧；已越本日，不扫描后日。
- MiMo：Dec16官方家族不是本日新公开，本日V2Flash repo空无Next，已发生SGLang必要源触发身份没变，不按周级扫描。
- MiniMax：原Blog12条Dec23M2.1→Oct27，无Next；本日邻接没有条目，不外推全网无事件。
- arXiv：四本日查询submittedfirst[Dec18,Dec19)各1页无Next，language171/system9/multimodal30/MLcontext37、跨组191identity；完整相关题摘和官方窄ID段补检仍继续。不得把其中Jan/Feb公开ID、Submitted/OAIupdated/monthmembership移为本日。历史first-public已有限路径穷尽参见`../ARXIV_DATE_RECOVERY.md`，只隔离具体potential，不解除可读ordinary。

## 本窗artifact精确差异

本日[GITHUB_WINDOW](./GITHUB_WINDOW.md)记录sinceDec19T01Z/untilDec20T00:59:59Z，7仓库各hasNextfalse，逐条按实际committedDate核，不仅相信until。

Video1.5三个patch核心实际全读：36916f8c VAE context临时启用slicing/tiling并恢复原flag；**yield后恢复没有try/finally，异常退出恢复不保证**，不得宣传完全安全。85c5343c FA3可能返回tuple(output,lse)时取output，具体backend接口正确性；40d5b27f支持preencodedlatents同时提供pixelvalues给i2v、SPsync对应pixel，dummydata/doc从batched说明改datasetitem，不拿示例变化证明模型质量。三个有局部兼容/状态边界潜力，未运行无性能保证；仅committer时刻无法证明artifact公开，隔离而非删掉。

WorldPlay c914f2a只加contact；76f5eaf完整原patch重取不截断，删bestquality/real-time宣传列、整理run.sh/模型路径的中英说明，不新增生成机制。86cfe35.merge包含18已读download_models.py同302行/README/requirementsprotobuf，原有效阅读按同identity去重，无新的模型算法；a8f09f2.merge.patch展开6个Dec18已读commit，旧SP/cache路径不重算20修订。README维护关闭，不能把merge时间当新researchrelease。

普通题摘/列表收束更新：官方cs.CL月长页1302，只浏览2512.16171–17299相关标题，补10完整题摘；四组191中172完整题摘、19明确titleclose，共182具名题摘处置见ADMISSION_ADDITIONS。Bloom最后Limitations/Conclusion定点已读，无可读ordinary未做项。此后只有独立Scope准入/证据/Books协调与真实外部隔离，不授全源无遗漏。
