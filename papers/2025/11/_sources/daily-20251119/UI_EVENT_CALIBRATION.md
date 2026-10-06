# Generative UI：官方推出事件的定点日期恢复与准入请求

作者Dalton，2026-10-04T16:21:30+08:00。这是既有Generative UI缺口的有限恢复。以下请求保留当时判断；后续root实际准入/日期/最小core及OnlyReport通过见 [独立裁决](./UI_AND_TRAINING_INDEPENDENT_CALIBRATION.md)，采用Gemini3同家族命题，不授日级完成。

## 可核日期与事件身份

实际打开Research原说明，沿其正文dynamic-view链接到[Gemini app官方公告](https://blog.google/products-and-platforms/products/gemini/gemini-3-gemini-app/)。[原HTML](./google_gemini_app_date.html) L49–56：L55 `datePublished=2025-11-18T16:00:00+00:00`，L56 `dateModified=2025-11-18T16:00:04.244953+00:00`；即BJT19日00:00，完全落窗。receipt记录HTTP200/376944bytes，传输成功不代替上述字段实际核验。

原HTML L4949及L5131明确这是visual-layout/dynamic-view首次产品实验并当天rollout，动态界面由prompt时模型代码生成，且直接链接Research同篇机制说明。web完整核心见 [APP公告raw](./WEB_UI_APP_ANNOUNCEMENT.txt)网页L260–266，[Research定点raw](./WEB_UI_DATE_TARGET.txt)网页L118–153。可以归属的是这个有精确日期的官方推出事件；**不把它当论文首次公开，亦不由链接自动认证当前22页PDF为发布日快照**。Research原日期仍只有Nov18无TZ；同路径两次超时不重试。当前项目50%及2026 arXiv稿不回填。

## 需要root校准的最小命题

静态markdown/固定widget保留低等待和可控接口 → 当时官方实际推出prompt条件的完整可执行交互界面，并在研究说明中公开生成分钟级等待/偶发错误与不计生成速度的偏好评价 → 是否值得保留为输出交付对象改变后的局部质量/等待边界，而不是“prompt+tools+postprocessors组合新颖”。不采用排行榜、普遍质量优势、内部emergence因果、性能/安全保证。

初送时UI尚待贡献校准；现root已通过官方推出事件的最小core/OnlyReport，作为Gemini3同家族受限命题，不增加第二家族。家族原5分保持，API受兼容性变更深入，UI按官方最小core标准；版本/实例事实不借成熟评价分账抬Durability。未绑定论文数值不采用。

## 已读必要支持与反侧

Research正文§How implementation works只公开server tools、系统指令与postprocessors，并没有逐组件独立归因；§evaluation明确生成速度不计；§limitations实际承认一分钟以上生成和偶发不准确。因此发布事件支持“交付对象改变+有限现实限制”，不支持组合收益归因。

[原22页稿raw](./WEB_DATE_PAPER_03.txt)文件L145–305对应PDF§2–6：输出single page及assets；100 LMArena prompts排除8、每结果2raters、pre-cached展示；82.8%对markdown是该人口的作者偏好，不是在线任务成功或SLO。PDF 44%是摘要“comparable”陈述，Table2对expert实际win43.0%/expert56.0%，不能把44%都解释为strict win。生成1–2分钟、部分渲染约减半、JS/CSS/HTML错误是作者限制；没有工具总成本或在线受控体验试验。精确endpoint/backend/precision/concurrency/full cost Not Disclosed；本次未复现。PDF初公开与发布日版本绑定未定，故其数值只保留作版本待核，**不作为正式历史评价结论**。

## owner具体比较与建议

实际重读Books context，ROADMAP定位`PLATFORM-EVALUATION-SYSTEM`；读Ch66开头L10–76及Resource Budget段L456–462，Ch65/67开头交接。Ch66实际承载scorer测偏好还是outcome、环境/执行身份、延迟成本是否恶化，以及质量/利用率/延迟/violation联合报告；Ch67承接TTFT/TPOT与SLO，不让measurement替代质量定义。

这不是因没有Generative UI名称而制造缺口。当前建议**仅报告**：已公开的发布/输出格式与局部限制提供具体案例，但不改既有评价分账原则；论文版本未绑定，更不据其分数申请长期写入。成熟质量/成本分账原则不计本项增量，不请求共享Books写锁。若root认为具体局部新证据足以准入，继续标准审阅仅采用同期官方可支持范围；若需要采用论文实验，最小外部请求为发布时原22页稿快照/可靠版本绑定，而不是补造首次公开。
