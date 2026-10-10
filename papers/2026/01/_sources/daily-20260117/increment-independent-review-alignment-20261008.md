# Jan17 独立必要复核：10160 Alignment Pretraining

复核者：review_jan15_delta，非报告作者。仅 root 已授的本日 ready 10160；启动独立 Jan17 上下文，重读 AGENTS、当前 Research/Report 合同、Prompt、ROADMAP、来源使用说明/Daily组及本日 supplement/停点；Books 判断前读项目背景、学习方法、写作指南和实际目标/邻接。不采用 Jan14/Jan15 判断；固定 BJT Jan16 完整自然日补窗，原105/原窗口/评分不动。只有审计文件 ownership，不写 Report/Books/LS/索引，不 stage/commit/push，不授 DAY。

## 身份与事件边界

本日 increment-ab-batch2a-20261008.json 中 exact-v1 完整题摘实际读。采用 [2601.10160v1](https://arxiv.org/html/2601.10160v1)，不默认 current v2 替换。increment-align-current-early-20261008.json 当前官方 abs 轻核显示 v2/Feb19，没有已见具体撤回/纠错/安全说明；不因版本号推重要修订或展开全版本史。

实际读 [official project](https://alignmentpretraining.ai/) 与其直链[同题作者博客](https://www.lesswrong.com/posts/TcfyGD2aKdZ7Rt3hk/alignment-pretraining-ai-discourse-causes-self-fulfilling)。同题、同作者、Dec21'25公开日期以及6.9B/discourse/4174 binary/同SFT+DPO链明确是早公开家族，不能把 arXiv Jan16 当该机制或论文家族首次公开。博客当前内容与页面日期不证明每一段当时就存在，项目 bibyear2025 也不单独证明日期。

本次只采用 Jan16 正式 exact-v1 的扩展方法/评价事件：约14.94M/11B合成、E2E/Mid/CPT分工与协议、当前 benign-tampering 与 EM 边界；不是早机制再次发现。DataCite原件 increment-datacite-10160-20261008.json 实际读 Submitted Jan15 07:59:31Z / Updated-v1 Jan16 01:27:55Z / registered Jan16 02:48:39Z，结合本日已核正常公告/ID界限定正式 v1 事件归 BJT Jan16。注册或 Submitted 单独不授首公开；不证明上述每个结果第一次被写下恰为 Jan16，不移动早博客归属。报告需明确这个事件身份。

## 准入、必要支持与反侧

独判 2+1+2=5，标准完成；早基本机制不重复评分，评分描述本次需要处理的扩展评价/适用边界。准入链：只在 post-training 评价行为会忽略初始化与数据干预；扩展稿把同后训练、不同阶段数据插入、能力退步和窄 harmful 再训练放回同一评价链，若成立会改变是否仅靠单次后训练分数采用安全数据分支的判断。不是成熟 SFT/DPO 或名称映射计分。

实际读本日原件 increment-align-method-project /eval /validation /current-early /project /blog-20261008.json 的 adopted exact-v1 §2–5、§6.4、Appendix G/I/J 与 E2/E3。各为官方必要原文恢复，不把 prepared 摘述当原证。首轮过宽输出截断的 §2、限制与 EM setup 已定点完整补读；未读无关附件、完整旧稿或模型库/artifact实现。

四6.9B dense English models，500B DCLM+50B mid；filter9.30%/7.88%，retained replacement维持总量；synthetic≈1%插入。4174=2671 Articles（按场景生成合成训练）+1503 Textbook（未生成相应合成）；8 prompt/answer-order均值与SEM不是8独立训练seed。45→9和Textbook40→6只为当前persona单回合binary选择率，非真实执行、内在intent或安全保证；negative upsampled Textbook40→40不支持同样泛化。

同SFT/DPO后 positive 相对差异可持续，但自身可退，negative-upsampled E2E 后训练反比baseline较低，不能只讲单向故事。SFT2.15M conversations、2epoch≈4B tokens；DPO正文270k、附表259922、附文另150k的口径不偷偷合并成无冲突精确数。2k DPO长度保87%完整response，6B200/5h/BF16仅该阶段；SFT64H100另有成本，不代表全流程账。

Mid插500M；CPT额外1B=500Msynthetic+500Mreplay；E2E约5.5Bsynthetic不等阶段预算配比。post E2E13.2/CPT15.2不支持late必最好/阶段最优。Table3平均2–4pp代价同时PIQA .66→.55等局部明显退，DCLM已针对部分能力指标优化、E2E data order不同；无多训练seed，不能把8 prompt SEM当训练稳定性证据。

Appendix G当前728,499,145 MCQA/Python tokens/1,857,677 conversations、同SFT超参但较短training duration，局部未见回到base/elasticity；早博客当前约120M且不同训练构造呈现reversion，两者不是matched实验，不用它们互相否定，更不宣称任何benign training不会退。Appendix I 四条件在三窄harmful数据后均EM：all-attention/MLP rank32 RS-LoRA，GPT4o judge alignment<30/coherence>50只定义该构念，不给独立现实安全真值。模型在原EM问题与自有集一起升高仅支持相应敏感性，不赋pretraining免疫。

Appendix J 的GPT5.2 HHH<1%/misaligned persona≈99%验证选项方向与elicitation，不证明真实人格、行为truth或无歧义标签。Claude生成存在ambiguous alternative、hallucinated source/弱关联，Textbook未合成不等独立真实行动gold。§6.4明言behavioral propensity而非execution，小English dense/简单SFT+DPO、无RLVR/更多targeted posttraining/无多训练seed局限保。

每E2E约20k GH200 GPUhours；11Bsynthetic估$4–8k是相近生成质量估算，不是全run费用。生成/filter、阶段模型、所有prompt/回归和再训练都计费；完整totalpipeline/hardware配置/precision全账、SLO或生产验证不全披露，未核实现/复现。

## Books：标准 Only Report PASS

实际独读 Ch28:1407–1448、Ch27:225–255。Ch28 spec/rationale训练→posttraining→held-out conflict链已明确理解规则≠始终遵从、语料policy真值另属owner、runtime deterministic enforcement不可替代；Ch27已承mixture/控制字段identity与filter选择偏置。没发现“必有elasticity”或“必抗EM”的待修正正文，不能为当前实例造一段。

这不是本文exact discourse配方/验证已完整 Existing；处置 Only，因为当前新增是受限方法/评价实例与协议条件，尚未建立更强可迁移的持久性充分条件，不改变已有长期分工；局部有贡献仍保报告。早公开与正式事件、benign persistence/EM易感及全费用应在Report证据链同写。无 Books 写入或锁、无 POST。

已将终判通知 root 与作者；本项完成不等来源/筛选收束或整日通过。其他普通具名工作与 DAY 仍由本日主流程路由，本文件不验未变105全文或其他新篇。
