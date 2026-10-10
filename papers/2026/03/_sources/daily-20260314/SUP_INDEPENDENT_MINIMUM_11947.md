# 11947 PE-FT：非准备者最低处置复核

复核者：`mar13_admission_review`；准备者：`root`。仅03-14/补充Mar13 BJT本日上下文，当前合同与停点已在本次小批前重读。完整题摘、具名身份、Mar13日级归属及纯Submitted venue门有效复用，不重查会议/时分秒。不写Report、Books、主ledger或LEARNING_STATE，不授DAY。

实际读`SUP_MINIMUM_11947_ROOT.md`后直接核`SUP_NECESSARY_11947.txt` §3合成child-safety人口、§4.1–4.3层诊断、§5 Eq9–11具体训练接口、§6.1–6.3/Tables2–6/评价定义、§8限制。截断的§6.2/Table3–4另恢复；未读图像pixels、全部附录/引用、代码或复现。`SUP_ROOT_11947_MANIFEST_RESULT.json`实际官方exact-v1 GET200，228491bytes，2026-10-10T01:30:06.599040Z，final URL为`https://arxiv.org/html/2603.11947v1`。

## 实际机制及评价边界

原文用mean-pooled audio hidden进行三类线性probe、intent与年龄条件cosine分析，另以最后hidden的top3是否包含最终层top1做logit-lens测量；这些是可读出/一致性证据，不识别唯一因果功能层。原文将0–6与7–14作为所测两backbone的经验区间，§5据此只在LLM0–14层加载/训练LoRA，冻结audio encoder及其余LLM层。层14平均audio hidden输入category头与三个attribute头，**训练用真category标签路由attribute头**，总损失SFT + .5×(category CE+attribute CE)，推理丢弃辅助头。不是新增部署分类/权限门或独立安全monitor。

训练1500 text/category×两声学实现，共9000合成音频，GPT-4.1依内容及属性生成SFT target；两A100、10epochs、batch128、LR8e-5、约70min。完整checkpoint/precision、LoRA rank与slots、输入输出长度、推理并发/完整费用与latency/SLO在必要段未披露，不由参数减少/70min认证与全层同资源降本。

评价1200 audio中含gender200条私测，不纳入§6.2主结果，不能把全部1200当所有表格分母。PA-score是GPT-4.1判断{-1,0,1}的均值，PA-rate是+1比例，ParaS2S是1–4分，VoiceBench HS另测一般能力；这些不可互换，也不作真实危险概率。均值近零不自证随机猜测或完全不能读声学属性。

本次直接保留的支持和反侧：

- Table2局部调优收益成立，但Qwen完整PE-FT age .945低于0–14无头.960；Kimi完整PE-FT gender .965低于无头.970。Qwen/Kimi VoiceBench HS为72.34/76.06，低于vanilla73.42/76.91，不能采用无损保留。
- Table3 Kimi仅0–6层age .920高于0–14层.915；Table4 Kimi全层加头gender .940低于无头.950；Table5第14层不在全部属性最好，例如Kimi layer7 age .955高于layer14 .940。它们限制原文统一“optimal combination”/每项优越，不抹掉emotion与其他局部收益。
- Table6 Kimi gender PA-rate由原Google-TTS96.5退到Typecast68.5/GPT-TTS75.0；Qwen也由96.5降到92/90。对应跨category speaker与新speaker协议，不是全人口无损泛化。
- §3七类×10问题/70文本配对Typecast child/adult声；child-only PA-rate改善评价的是属性条件回答，非真实年龄识别、实际未成年人伤害降低或发布安全许可。§8明示gender声学二元标签不等自我认同，不升级为真实身份判定。

## 分数与处置

**通过：Design1 + Reach1 + Durability2 = 4；最低关闭、仅报告，Books新写0。** 新增命题是所测两音频语言模型中的经验层区间、选择性LoRA与辅助监督头配方，而非LoRA/probe/双头的成熟原则。改变的是这一audio interaction路径的局部适配选择，非跨平台权限/执行接口；可复查的条件响应、一般能力与speaker/TTS分账保留稳定边界价值。评分不由阅读投入、是否容易写书、访问状态或本文安全名称倒推。

原约束“内容中心适配可能忽略声学用户条件” → 原文实际“固定经验层范围+训练时属性监督及相应切片实证” → 本次改变“这条局部层选择/辅助头配方需要按旁侧效用与语音人口取舍”，当前不足另承诺统一功能划分、普遍更低成本或真实用户安全。认可4分不要求普遍质量定理、完全成本实验或开源后才准入，必要原证已足够结束本项最低判断。

实际对回ROADMAP `MULTIMODAL-REPRESENTATION` Ch23音频159–169完整局部：明确声音内容/非语音信息、encoder/readout/层可见性与probe预算分账、learned层权重不作因果解释。这只定位长期开口与避免重复成熟原则，**不是宣告PE-FT新实验已有覆盖**；本项是低分不进一步采用，不造NC、不新写或要求PRE/POST。必要Source与最低评分/处置复核通过，日报其余普通工作和DAY仍未结束。
