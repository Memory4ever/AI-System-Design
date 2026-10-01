# Apr20 SoTo / StoSign / HarmfulSkill 三项窄 owner 提案

作者apr20_resume，均未写Books。必要证据位置与局限见[恢复记录末批](./v3-reopen-notes.md)；日期联合原始批链仍需日级非作者核。本包只请求有限source→当前owner审阅，不以题名安全/基础标签普遍抬深度。

## 2604.15453v1 SoTo：Ch24 AR 生成段

拟2+2+3=7深入。实际Ch23离散表示段123–133已讲nested dropout诱导可截断ordering；Ch24 AR段35–55讲表示可预测性/历史误差滚动，却未承载partial prefix能否有效让verifier筛beam的算法分支。唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`，拟在RAE-AR证据段后、append-only edit branch前写两段，Ch23只交接表示前提。

最小正文：逐token概率可预测，并不等于部分prefix已能被质量sensor辨认。coarse-to-fine图像token经训练形成早期全局语义时，可将每个候选prefix重建成中间图，再用verifier保留beam；grid/raster prefix只覆盖局部，填补后的中间图可能误导评价，更适合完整BoN或付费lookahead再判断。因此representation ordering、partial reconstruction与search protocol须一同选择，不是把任意一维序列称语义有序。

这一分支支付重复detokenization、branching和verifier成本，NFE中的一次生成与一次评判并不具有相同wall-clock；flow decoder多步重建可成为主要瓶颈。更多搜索还可能提高自身verifier分而降低外部质量，缺失语义prior也不能被无限预算恢复。ordered prefix不稳定、解码成本无法摊销或verifier未在独立指标验收时，保留普通AR、完整BoN或grid/lookahead路径。受限FlexTok matched2D比较/300COCO图支持这条选择，不证明视频文本普遍收益或无预训练生成。

必要原文：[v1](https://arxiv.org/html/2604.15453v1) §3/4/5.1–5.5、§7、D.3、E.4、G；不采用AppendixB形式界，故不为本命题读其全部证明。

## 2604.15416v1 StoSignSGD：Ch28 Sign Step 条件段

拟2+1+2=5，具体知识缺口深入。实际Ch28 Sign Step优势382–393已把norm/noise条件与排名分开，低比特EMA748–754已讲编码误差，但未讲有界随机sign在期望保持preconditioned update。唯一owner `TRAIN-PRETRAINING`，拟在Sign Step条件段后、可行域前补两段。

最小正文：确定性sign便宜，却把不同幅度映成同一方向；一种受限随机分支在逐坐标包络覆盖更新幅度时，先加包络缩放的均匀噪声再取sign，使其期望等于原更新除以包络，而非原梯度无偏。包络如何由历史max或momentum构成会同时改变预条件几何、状态与方差，必须记录zero handling和checkpoint语义，不能把加噪直接当收敛保证。

代价是采样与包络状态、有限步更新方差以及对尺度估计的依赖。它在粗粒度FP8 state实验中可避开平方梯度先underflow的路径，但该对照仍保留BF16 master/nonlinear，AdamW失败绑定E5M2梯度/E4M3 state及特定GPT2运行，并非所有FP8训练必然失败。条件不满足、历史尺度过保守或质量/成本验收无收益时，回退高精度state与AdamW/SGD；理论的范数/矩有界条件不能升级大模型通用加速。

必要原文：[v1](https://arxiv.org/html/2604.15416v1) §2/3.1–3.2、B.2；不采用摘要精确speedup（token分母/顺序不一致）或普适排名/所有理论proof。

## 2604.15415v1 HarmfulSkillBench：Ch72 SkillPoisoning入口

拟2+2+3=7安全深入。实际Ch72 SkillPoisoning1414–1436只区分隐藏payload、合法任务与真实sideeffect；2571–2575强调description≠code，没有承载用户主动使用公开声明有害functionality但代码未藏payload的threat-model区别。唯一owner `PLATFORM-SECURITY`，拟SkillPoisoning标题/既有开段前两段，不改既有effect oracle责任。

最小正文：Skill admission不能只查描述是否与代码一致。用户可主动安装功能描述本身就违反平台policy的skill，再以“读取并规划执行”调用它；这里不是用户被隐藏payload欺骗，第三方才是受影响对象。平台需把declared capability的内容policy与代码隐藏effect分开审阅，并将裸task、安装skill下同task和被动plan作为不同评价切片；描述透明或用户愿意都不自动赋予平台授权。

此检查增加policy版本、人工复核与误拒绝成本，不意味着所有高风险用途都非法或所有技能需要相同限制。文本benchmark只测有害规划意愿，建议HiTL/AI disclosure不等真实批准或外部告知已发生；judge与policy taxonomy亦是评价条件。受限200自然语言skill/6API模型未执行脚本，不能将harm score或注册表分类率当现实事故率、效果验证或有效防御证明。低风险可信skill可保留较轻内容审查，实际动作仍由scope、approval和effect-time授权控制。

必要原文：[v1](https://arxiv.org/html/2604.15415v1) benchmark construction/evaluation、Tables5–7、results与§8limitations；只采用planning条件差异，不采用检测器真实groundtruth/生态总体风险率或法律结论。

尚待独立采用核与root授锁，未真实写回；普通其余源审阅继续，不等待此包。
