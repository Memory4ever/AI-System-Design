# Nov27 首批可独立准入校准

作者Aristotle，本日BJT[Nov26 09,Nov27 09)，UTC[Nov26 01Z,Nov27 01Z)。fresh实际重读全部适用合同/来源/ROADMAP/checkpoint；本日14入口native独立首查已返回，尚需有限历史边界整理，没有继承26 Coverage/候选或旧Weekly。

## 日期已支持的安全事件拟项

[Mixpanel security incident](https://openai.com/index/mixpanel-incident/)，本日RSS1245项/缺pubDate0，唯一窗内项`Wed,26Nov2025 19:00GMT`=BJTNov27 03:00；原页日期Nov26。实际原核心L19～60及FAQ64～105已读，raw-security-boundary2.json。拟采用是局部安全反证：模型/API主系统未被攻破的厂商范围断言不能自动覆盖已导出的第三方frontend analytics身份数据；系统资产边界需包含账号/粗粒度位置/referrer及org/user identifiers的关联面，不是因为有“安全”标签就收，也不采用成熟MFA提醒作增量。拟2+2+2=6，安全受影响内容深入必要范围，准入与Books尚待root。

Nov9发现/Nov25共享dataset是厂商描述的事故/调查节点，不重定本窗公告首公开。当前原页有**Dec19 clarification**将受影响用户从API用户补到少量help-center/platform登录ChatGPT用户，实际已读受影响段，不把晚更正伪装Nov26最初文本。FAQ亦为当前版：content/prompts/keys/tokens未受影响均只是厂商调查断言，不能授已独立取证或全无安全风险。No evidence outside Mixpanel不是证明不存在任何其他影响。原文phishing/social engineering是风险，不说明成功攻击数量。只考虑事件边界与账号analytics暴露，不扩附件/所有vendor审查。

表外Mixpanel原通告[Our response to a recent security incident](https://mixpanel.com/blog/sms-security-incident/)已由本日精确query发现，官方日字段Nov27、时区未知；Nov8检测与OpenAI说Nov9aware可为不同节点，尚需原核心定点对照，不能把日字段整天落窗/补精确时刻。这个后续通告不能证明本窗新family，也不能独立认证所有OpenAI数据范围。Books拟定位PLATFORM-SECURITY，**尚未实际owner对读，不先提出缺口或写入**。

## 八项 exact-v1 完整题摘的潜在方向

本日四组窄API提交发现区间[Nov24 19Z,Nov25 19Z]，start0/max50分别30/5/2/26；短页到末。全部只是发现线索，关键词/可能词干非项目语义保证，submitted非public。raw-first-exact3与raw-first-fullabstract4保留8个完整题摘及history；当前页未见撤回，未遍历全版本史：

- [QiMeng-Kernel](https://arxiv.org/abs/2511.20100v1)，submittedNov25 09:17:47Z：全kernel生成的策略与code空间耦合→RL探索macro优化策略、通用LLM逐步micro实现→需核correctness/性能与搜索budget的归因，不照录near100/34x保证。不是一般“分层planning”类比收录。
- [Beluga](https://arxiv.org/abs/2511.20172v1)，Nov25 10:51:43Z：CPU channel限制/RDMA pool语义成本→CXL switch共享load/store池与GPU访问characterization→需要核address/一致性、native访问与KV路径/测定条件；89.6%/7.35x只作者局部。v2Nov27 06:20Z在终点后，不借。
- [Softmax Transformers are Turing-Complete](https://arxiv.org/abs/2511.20038v1)，Nov25 08:08:39Z：hard attention已知而softmax CoT表达力条件未齐→CoT C-RASP unary/letter-bounded与relative position extension→需要核precision/长度/语言限制，不扩成真实LLM可学习任意程序。
- [Directional Optimization Asymmetry in Transformers](https://arxiv.org/abs/2511.19997v1)，Nov25 07:03:20Z：function class对称不保证优化路径对称→synthetic entropy-floor forward/inverse控制与GPT2/MLP/LoRA对照→可审局部学习反证，不能因简化关，也不采“根本架构必然限制”因果措辞。引用的reversal-invariance基础需实际核条件，不靠别日结论。
- [In-Context Compositional Learning via Sparse Coding Transformer](https://arxiv.org/abs/2511.20194v1)，Nov25 11:19:58Z：context组合泛化的inductive bias不足→encoder/decoder learned dictionaries+sparse coefficients/context线性组合→需核attention与task/capacity公平对照；NeurIPS2025标记非first-public日期。
- [Mosaic Pruning](https://arxiv.org/abs/2511.19822v1)，Nov25 01:24:41Z：单corpus expert pruning跨域退化→跨任务similarity cluster+Activation Variability Score选代表→潜在一般选择条件，不拿7.24/8.92指标本身评分。
- [CafeQ](https://arxiv.org/abs/2511.19705v1)，Nov24 21:15:16Z：calibration数据不可得→proxy loss优化structured single/dual transformations与adaptive rounding→潜在quantization成立条件，需核Gemma2/GPTQ对照/额外计算，不因4bit改善小关闭。
- [ParaBlock](https://arxiv.org/abs/2511.19959v1)，Nov25 06:09:21Z：block-coordinate本地计算仍受通信→两个parallel threads及与标准BCD同收敛rate条件→需核staleness/资源/异步条件而不借成熟overlap原则收；v2Jun2026不借。

日期未定仅minimal restore官方公告/原v1公开字段/作者真实事件上下界，不预设这些8篇属于本日，不扩63返回全题摘/全文队列。相关新主题另有界查漏。

## 代表性负侧与未关闭

[Image2Gcode](https://arxiv.org/abs/2511.20636v1)完整题摘实际读(raw-negative-and-recovery5)：slice-wise cue+DDPM G-code直接绕CAD是制造流程特定mapping，没有摘要主张新增通用foundation/训练推理机制或成立条件，拟范围/贡献关闭；不是因为DiT成熟。v2/3晚版不借，submittedNov25 18:55:12Z不当public，日期不决定此关闭。请root核此负侧是否漏掉通用原生trajectory机制，若需要只定点重开其原core。

[KyrgyzBERT](https://arxiv.org/abs/2511.20182v1)完整题摘亦读：35.9M+custom morphology tokenizer、翻译SST2/人工test、与5倍mBERT的F1对照。**暂未关闭**，先定点确认tokenizer或资源对照是否实际提出可复用新条件，不能仅按低资源应用或小BERT标签关闭；不因无实验细节关。其他明确MRI/材料应用标题只范围线索，不宣称已全题摘筛选。

## 当前停点

Mixpanel原公告核心/晚更正已准备，先送root单项准入及安全范围校准；8篇潜力不需要全附件。普通仍为本日14入口有限历史边界、Mixpanel原厂商对照/owner比较、相关有界查漏与具名日期恢复。Hunyuan本日浏览器因subagent visibility不支持后改默认，再30s timeout/kernel reset，实际失败不继承别日；publicList返回需本日读字段。未写Books/shared/index/state，不stage/commit/push。

## 最新停点（2026-10-04T18:33:50+08:00）

上述是首批时停点，不再代表当前普通待办。作者14源有限边界/筛选、Mixpanel原对照与Ch72/71/73具体Existing、具名最小日期恢复已收束；见SOURCE_CHECK、MIXPANEL_EVIDENCE_OWNER和BOUNDED_CANDIDATE_FINDINGS。46潜力保留包括必要相关尾部exact-v1题摘，不扩全部正文。当前只待root单项及日级有限独立核；报告进行中、Books0，作者继续fresh28，不等全部日期材料到达。Beyond初步拟关闭经实际core局部表示取舍证据已撤销，现为日期潜力；晚版不冒充v1。历史目录/日期保留不授正面采用或无遗漏。
