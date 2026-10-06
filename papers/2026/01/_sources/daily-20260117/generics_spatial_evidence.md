# 09852 / 09954 标准审阅与拟 Books 处置

root已实际决定性准入5=2+1+2。本批均未复现/核artifact；下面拟仅报告不是贡献前排除或为工作量改分，仍保留候选与标准审阅事实，待root终裁。

## 09852 — 无任务/跨词面对照下的量词表示

actual exact `2601.09852v1-primary.txt` §2 L86–94、§4 L215–231、§5 L232–263/limitations263–279、C2/D/E L690–727。十模型category/all-some预筛后仅Qwen3VL4/8B进induction；只选择双模型全部20问题通过的100categories。40template/propertyvariation、12k text/60kvisiontext，relativeYes在Yes/No词面集合内normalize非无约束回答概率。all>generic>some的混合效应/95%CI只对promptvariation人口，不能授人类认知或未知concept泛化。视觉200pairs人工剔60→140/840stimuli，$17仅生成credit不含全部probe/人工成本。

核心新证据 §5.2 L249–260：无task proposition-only、all/every、some/certain、bareplural/indefinite六surface，每type250 animate/nonce，Qwen3VL8B末token各层hiddenstate/PCA；近义两surface比异meaning近，排除这组纯单词surface解释。E二维PCA距离不是原highdim语义度量或causal mediation，句式/长度不同仍未全factorial；作者明确无causal implication、English/WEIRD/预筛局限。precision/hardware/seed/totalwallclock ND。

拟仅报告：真实新局部语义控制保留报告，不扩大成独立quantifier circuit/可部署机制。actual `WORLDVIEW-REPRESENTATION` Ch5 L28–40已有坐标不天然semantic identity、可读≠因果使用；Ch12 L109–122明确contextual hiddenstate≠input/sentenceembedding，不将后期量词PCA塞inputowner。新证据目前只补这一具体English/model/nonce population的经验实例，没有可独立采用的表示变换、跨域验收或新的使用机制；不声称已有正文已经覆盖全部六surface实验。若后续有高维/干预/跨模板失效改变readout设计，再定点重开Ch5因果使用接口。

日期raw SubmittedJan14T20:16:10Z、UpdatedJan16T01:04:43Z、createdJan16T02:40:59Z/registered02:41:00Z；normalcohort+无先行全文条件区间BJTJan16[09:00:00,10:41:01)。不审Jan26v2无关diff。

## 09954 — 同 encoder 的 2D-RoPE 局部混合效果

actual exact `2601.09954v1-primary.txt` §3 L85–94、Table2 L189–323/4.1–4.2L323–353、§5–6 L549–552。同LLaVA recipe内CLIP/SigLIP/SigLIP2/AIMv2各±2DRoPE，将PE加Q/K非rawpatch，256平方两stage；8A40×48GB，projectionpretrain LR1e−3 B256，fulltuneLR2e−5 B128/AdamW/cosine。epoch/trainsteps/LLM与encoder完整variantidentity/precision/seeds/全部预算未披露，不补厂商配置。

必要paired Table2：CLIP CountBenchQA .468→.290/CV2D .490→.443/VSR55.810→57.201；AIMv2 MMVP .513→.560/VSR56.219→60.311但Count.739→.719/CV2D.466→.432；各任务不同涨跌，不授2D增量普胜或失败纯来自flatten。换encoder的数据、objectives、分辨率适配没有独立factorial，不能将CLIP→AIMv2收益归denseobjective或将Gemma3单样本错方向归pan&scan信息loss。frontier与LLaVA规模/data/token不同不合排行因果，作者conclusion明确非apples-to-apples。

拟仅报告：同encoder局部反侧保留，不用未全披露recipe给通用PE设计追加新定律。actual `MODEL-POSITION-ENCODING` Ch13 L186–192已有lattice/function/precision identity与task失配、质量Gate和2DRoPE退路；`MULTIMODAL-REPRESENTATION` Ch23 L75–81已有layer/readout/config身份、同pixels换config/同config换pixels、输出失败不能推encoder信息缺失。这里没有新可复用PE算法/新的可核控制失效边界，只有若干固定LLaVA/encoder组合的局部nonuniform validation；不声称现正文包含该Table2，也不以已有Books抹除已准入命题。若完整matchedrecipe或因果factorial改变具体grid/PE选择，再重开Ch23/13边界，不无限等配置而冒外部Blocked。

日期raw SubmittedJan15T00:30:34Z、UpdatedJan16T01:11:37Z、createdJan16T02:43:26Z/registered02:43:27Z；条件BJTJan16[09:00:00,10:43:28)。不审Jan22v2无关diff。
