# GLM-TTS必要证据与共享Books提案

2026-10-02T20:19:36+08:00作者同步实际落实：root已在Ch23第83行、理解侧音素两段后/阶段三前写入生成侧混合输入自然段，绑定`SF-2025-ZAI-GLM-TTS`。作者本次实际读取65–95行及925行原始来源末注；末注明确Popper于2026-10-02T20:15:20+08:00对原文Phoneme-in/评价、固定早期README、新段与前后/Ch24/25完成非写入者POST。长期知识缺口触发深入必要审阅，评分5不变；Books决定为整合，不再是待写草案。下文保留原提案过程，不覆盖此实际状态。没有作者自行改共享Books或授日级通过。

实际检查2026-10-02T18:25–18:30+08:00；作者侧，不是独立验收。

## 日期与版本

[官方文章](https://www.zhipuai.cn/en/research/147)的原始HTML `time datetime="2025-12-10T16:00:00.000Z"`，对应2025-12-11T00:00:00+08:00，落本窗；显示`2025/12/10 16:00`不能当北京时间。此字段支持文章事件，不证明仓库/权重恰在同刻首次公开。

官方GitHub API repo.created_at=2025-12-06T04:50:56Z，只是仓库创建；当前README称12/11开源，日标签无时区。有限恢复取得截止12/11T01:00Z最近commit `40cf8f3f2c0e2bb035f479051d3d1a0aa4421730`，committer.date=2025-12-10T15:59:18Z，message=`release test`；commit时间不等公众可用。通过[固定README](https://github.com/zai-org/GLM-TTS/blob/40cf8f3f2c0e2bb035f479051d3d1a0aa4421730/README.md)及contents API完整阅读核心，避免把当前12/17论文或后续实现偷渡到本日。固定README已有Phoneme-in与未启用phoneme评价；RL优化权重仍Coming Soon。

## 支持范围

采用命题限于厂商披露的条件输入设计：局部随机G2P训练使纯文本与音素混合；推理先G2P，再按词典替换目标发音，保留其余文字。这是局部内容接口，不是全局情绪/说话人控制，也不是GRPO新算法。没有核验代码执行、训练复现或发音字典的实际覆盖。

标准审阅的关键限制：Evaluation Results为seed-tts-eval zh且明确without phoneme；基座与RL的CER/SIM对照不能归因局部发音接口。多奖励仍可能冲突，词典错误与G2P错误可能改变内容。hardware、precision、输入输出长度、batch、concurrency、SLO及流式真实首包评价均Not Disclosed；不采用提速/生产承诺。后续技术报告与后续权重需另定事件，不追加本窗。

## 对读与目标owner

唯一owner `MULTIMODAL-REPRESENTATION`，Ch23 [现有79–81行](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：已有理解侧显式音素/词界接口与连续projector的条件，明确不能替代音色/韵律。该段没有文本到语音的局部混合输入训练/词典控制选择。

邻接Ch24 [466–478行](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：拥有语音生成factorization、文本/音频交错和时间层级，G2P用于总长度责任，不拥有输入表示的局部发音覆盖。Ch25 [14–27行](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：action-conditioned环境转移，不接收该TTS接口。未修改Books。

## 条件性局部草案

建议由root核准后在Ch23音素接口段之后补以下段落，而非新增孤立模型小节：

> 生成语音时，局部发音选择也可显式进入条件输入：纯文本保留语境，目标词用音素替换，训练用局部随机G2P让模型见过这种混合序列。它区别于整体声音风格或音色提示，把多音字/罕见词的选择交给可审计词典，却也引入G2P、替换规则与词典版本责任；不需要精确读音时，纯文本输入仍更简单。公开的GLM-TTS早期说明提供这一接口分支，但其展示的CER/SIM评价未启用音素控制，不能用该数字证明局部控制或自然度已改善；须另外验收目标词准确性、上下文韵律与未替换词的回归。

这是整合提案，不是已经整合；准入、日期及证据仍需非作者核验。
