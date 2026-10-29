# Dec19 Google具名差额：官方日期与准入提案

## 1. Flash精确事件去重

实际打开[官方Flash release](https://blog.google/products/gemini/gemini-3-flash/)的redirect原页，标题/日期字段为Dec17,2025。仅核同一release身份和日期，不搬Dec18日报的池、评分、证据或源成功，也不按旧09点界重新建立候选。原T5完整行/日期/6分不动。

## 2. SynthID视频验证：核心实际读取后的排除提案

[原官方发布](https://blog.google/technology/ai/verify-google-ai-videos-gemini-app/)明确Dec18,2025，正文全部core实际读：Gemini应用对上传视频音频/视觉两track查SynthID并用reasoning生成分段回应，限定Google生成/编辑来源及100MB/90秒。原文没有披露新的水印算法、检测校准或与既有detector的实证差额。作者提案C：这是现成检测器接入产品的接口发布，不由多模态/安全主题或分段UI自动获得机制贡献；不评分/Books，不把未检出授非AI/真实来源。请Newton核发布/安全信号是否还有必要受影响域；未把读core当新水印Evidence。

## 3. FunctionGemma：实际release与具体准入待校准

此前有限列表未明确覆盖本条；辅助搜索中具体命中后回到[官方Dec18 release](https://blog.google/technology/developers/functiongemma/)，实际完整core。其为Gemma3 270M function-calling专用基座，面向定义清楚API的进一步微调，结构call与自然语言交接，edge独立执行或转大模型的部署分工。发布给出Mobile Actions held-out的微调前后比较，但“production-grade/deterministic/total privacy”不由该分数或本地运行成立。不是仅凭270M/排行榜准入。

又实际读[作者当前card](https://huggingface.co/google/functiongemma-270m-it)的description/basic usage、训练类型、evaluation与limitations：架构同Gemma3但chat format不同，不用于直接dialogue，特定单/多轮仍须再训练；函数声明进入chat template，输出仅待developer执行的调用。Card列不同BFCL子任务分数，不能称同任务反退或微调的负因果，单设备小context数据不是任意调用链性能。当前card是必要限定补证，不宣Dec18不可变快照。Blog的[cookbook](https://github.com/google-gemini/gemma-cookbook/blob/main/FunctionGemma/%5BFunctionGemma%5DFinetune_FunctionGemma_270M_for_Mobile_Actions_with_Hugging_Face.ipynb)网页只返回导航壳，未读notebook实现/未运行，不为新材料重试旧失败入口。

作者暂保P待Newton首批准入校准：通用对话零样本与狭窄API专门训练不是同一交付选择，原对照可能提供小模型专用接口的可行性/失效条件。若仅是已有fine-tune在Mobile Actions应用提分则应C，不能为拟owner或local隐私愿景保留；此事实决定准入，尚未评分/Books，不扩大Google全站或继承旧T5证据。后续只围绕该具体差额做最小决定，不用整份新recipe/所有版本拖延其它六节。

Newton§21已实际原Blog完整core/当前必要card独立校准：SynthID产品接入C通过，FunctionGemma就本包拟贡献改C。专用格式/窄任务SFT与局部held-out提分没有区分主线设计的受控对照，执行/路由也未披露新机制；作者接受具体改判，不因card/代码访问或Books覆盖关闭。不评分/Books，不重recipe。card通用6T/TPU/VLM措辞不授专门后训练配置，local/58→85不授privacy/determinism/production-grade；保原发布上下文，不扩Google目录。

## 4. 触发范围与停止

上述两条新具名release与原T5、Genesis/yearreview的处置分责；辅助搜索不是当天全量论文。ChunkySeal作者域查询没有恢复可靠官方先公开日，Meta同core身份/事件角色hold已在META§1/5修正，不因搜索无命中判旧O。未扫描Weekly来源或全部OpenReview；一次搜索出现OpenReview PDF只作身份线索，尚未取得forum公开日期，不声称已完成该触发的正文/日期核验。

