# Whack-a-Mole20957必要安全Source/实际已有覆盖提案

次批准入/日期root已核，3+2+3=8不改。作者实际读[exact-v1](https://arxiv.org/html/2603.20957v1) §3/Alg1、§4.1～4.4及footnote3、§5.1直接反侧、A.1/A.3/A.4、B.4～B.5。采用只限微调后可提取性与审计protocol，不采§6法律论断、特定非法语料来源或所有provider机制因果；不扩读81书逐行结果/受保护原文实例，不核artifact/复现。

实际新增数据不含target作品仍可提高target verbatim extraction：同author heldout、Murakami→32otherauthors、五随机pair、Woolf publicdomain→Handmaid一书以及synthetic反侧。Synthetic随机5736条300～500word匹配Murakami样本数，不保证各arm token、梯度、文体或总compute完全匹配；Woolf与synthetic不能唯一辨识pretraining overlap因果，也不证明任何author/数据都可重启所有作品。

Prompt从heldout原文由GPT4o-2024-08-06生成半长summary，另含author/targetwordcount；不是无target信息的free recall。每paragraph100采样T1，wholebook≥k连续word匹配，去prompt mgram再取剩余≥kspan，bmc跨paragraph/100draws汇总不同位置，并非一次逐字重构全文；最长contiguous-covered与one-generation-untrimmed span不同。m≥5/短k和prompt细节影响解释，不能将headline coverage当单请求泄漏概率。baseline81本仅完整测alignedGPT4o（footnote3因cost），Gemini/DeepSeek只有preliminary samebehavior，不把三provider微调结果/GPTbaseline倍率当三份同模型pre-post因果。

GPT4o/Gemini2.5Pro API default finetuning，DeepSeekV3.1 TinkerLoRA lr5e-4/b16/rank32/maxlength2048；精确API训练revision、epochs/精度/hardware/总query费用/多seed不披露，未采performance/SLO命题。Gemini RECITATION过滤是返回结果的一部分，应分拒答/被挡/可见输出，不推出公开filter实现或必存整本原文。§5.1匹配web两corpora不完整且soft normalization恢复很多“未找到”span，也不能判定实际训练来源。

## 实际Books对照

Books适用docs/ROADMAP/相关LS已完整读；Ch72实际525～570与附近masked extraction段、Ch71/73交接顺读。PLATFORM-SECURITY正文已明确memorization与adaptive-extraction分账、posttraining新增数据不含秘密仍可改变可提取性、同family pre/post audit记录reward/prompt budget/interface/revision、量化probe失败不证明删除。该书稿没有本paper实测或版权case，不能拿主题相似声称每实验已覆盖；但拟采用的长期设计选择“本次finetuning语料无target不授可提取性安全、输出alignment非删除、采样/拒答/已知target预算必须重验”由上述实际正文承载，具体BMC/一书最佳配置不宜升级长期阈值。

## root 非准备者必要安全 Source / 具体已有覆盖（2026-10-12）

实际重新打开官方精确 v1 §3/Alg1、§4.1 footnote3、§4.3～4.4/B.5 与 §5.1；只读协议/必要反侧，不采用法律章节和受保护文学片段。核对跨采样/paragraph 的 BMC 聚合不等单次全文恢复，完整 baseline 只为 GPT-4o，public-domain/synthetic 对照未唯一控制训练 overlap 及全部 compute。必要 Source 通过，原 8 分保持。

实际顺读 Ch72 542～570 的 memorization/extraction 区分、post-training 数据不含秘密仍改变可提取性、同 family pre/post 审计、白箱/量化/生成路径各自测量权限。拟采用的长期判断已由这些具体正文承载；新协议及受限反证保留报告，不把未见记录称已删除或推模型训练数据/法律结论。已有覆盖通过，Books0、无锁，不添注制造 diff，不预 DAY。
