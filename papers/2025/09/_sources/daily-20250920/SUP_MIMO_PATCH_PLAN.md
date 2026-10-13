# MiMo 音频 patch 窄写逐字稿

作者Meitner，2026-10-12。只准备稿，不写共享Books。root先协调Sep17 Ch24另一窄段及POST；释放后另授本音频范围。必要设计Evidence/实际owner PRE已由Cicero独核§5通过；以下两段及末注全文、live完整音频邻接已由Cicero§9实际逐字PRE通过，不预写POST通过。

Owner：`MULTIMODAL-GENERATIVE-PARADIGMS`，Ch24。

## 当前邻接和范围

前接当前音频交错输出/执行深度两段（`SF-2026-ARXIV-2603-09215`），后接以“若任务只需生成语音，另一种粗细分解也不能与 RVQ 的 residual codebook 层级混同。”开头的时间分辨率链。只在两者之间插以下两段，保留两侧正文；章末Review notes只追加自身来源末注。写入前再读live锚点与完整邻接，不依赖行号，保护Sep17及并发2026改动。

## 拟写正文（两段）

降低大主干的执行深度之外，还可以改变它负责的时间粒度。让大主干逐帧消费和预测完整 acoustic codebooks，接口简单、时序责任集中，在短音频或模块耦合不值得时仍合理；声学帧率较高后，长历史会增加主干位置数。一条替代分支由局部 patch encoder 把连续多个时间帧的全部 RVQ 表示聚合为一个主干位置，再让局部 patch decoder 用 delay 自回归恢复这些时间帧的完整码层。[固定发布版架构说明](https://github.com/XiaomiMiMo/MiMo-Audio/blob/3b278795224cae06bd70cb4438633b2934b8367f/README.md)中的 codec 是 25 Hz、八层 RVQ，四帧合一使主干按 6.25 Hz 前进；改变的是大主干位置的时间跨度，不是把 codec 降到 6.25 Hz，也不是只保留少数残差层。同帧码层深度、patch 内时间依赖与跨 patch 的主干历史各有消费者，不应混作一种并行化。<!-- source-family:SF-2025-XIAOMI-MIMO-AUDIO -->

时间依赖只是移给局部模块，并未消失。patch 大小和时间边界、全部 codebooks 的顺序、encoder/decoder revision 必须共同定义接口；多帧聚合还增加缓冲、局部自回归和跨 patch 错误传播的压力。主干位置数减少不签发等比例总加速，仍须把 codec、两个 patch 模块、主干、排队及实际播放提交计入端到端成本，分别验收首包、音质、内容和尾延迟。公开说明没有同预算 patch-size 消融或完整硬件、精度、并发与 SLO 对照，不能把跨模型排行榜归因于这个分工，也不据位置比授无损或实时保证。接口不兼容、质量退步或首包/总预算不成立时，保留逐帧主干、较小 patch 或独立 speech decoder；已播放音频的不可回滚边界仍由提交管线负责。<!-- source-family:SF-2025-XIAOMI-MIMO-AUDIO -->

## 拟写来源末注

- `SF-2025-XIAOMI-MIMO-AUDIO` — Daily `2025-09-20`补Sep19完整自然日；[官方Paper目录](https://mimo.xiaomi.com/)具名Sep19发布日与[固定README](https://github.com/XiaomiMiMo/MiMo-Audio/blob/3b278795224cae06bd70cb4438633b2934b8367f/README.md) Introduction/Architecture内容身份分责，commit不独证public，不用December报告顶Sep版本。2+2+2=6，必要设计及Ch23/24具体差额经Cicero PRE通过；仅采用多帧patch压主干位置、局部delayAR恢复完整codec的factorization。current Demo/两图只补说明，不倒填Sep19实验，不采32倍总加速、29倍成本、全任务领先、因果质量或生产SLO；缓冲/局部AR/全成本与回退近正文。未核实现、听测或复现。写后非writer POST及DAY/FINAL尚未通过。

## 写后流程

得到root明确窄锁才编辑Ch24上述两段及自身末注；作者顺读live完整邻接、核其他修改保留、局部链接与diff。Cicero实际非writer POST通过后，只更新本日日报§1/3/5/6和新§4追加段，不动旧连续§4；收到实际六部分DAY再写完成态，跑V3/链接/冻结/限定cached+unstaged检查，交Cicero FINAL。真实FINAL通过后精确通知root并fresh Sep22；本稿不授Books、DAY或验收。

## 实际落地差额

root释放Google窄锁后明确仅授音频“一段+自身SF末注”；作者重读live锚点，把上方两段原词合成一个连续段落（去中间重复SF marker），只在“若任务只需生成语音…”前插入，末注在Review notes内追加自身身份。实际写后快照检查仅两处插入，没有删除/替换，local links及限定cached/unstaged检查通过。Cicero§10实际正文/完整邻接/自身注及固定原证nonwriter POST通过；作者同步自身末注实际POST，不再改共享正文。旧两段准备稿保留为PRE内容依据，不表示最新授权允许两段或当前待写；后续仅本日DAY/完成态FINAL。
