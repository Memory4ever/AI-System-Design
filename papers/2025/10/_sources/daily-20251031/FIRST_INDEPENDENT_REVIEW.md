# 2025-10-31 FIRST Independent Review

复核者：Mill（非作者；作者Curie）。窗口BJT [2025-10-30 09:00,2025-10-31 09:00)。不写作者README/共享Books，不授DAY通过。

## Aardvark：贡献校准关闭，不按Books覆盖排除

实际解析本日openai-rss.raw目标item：Thu, 30 Oct 2025 11:00:00 GMT；实际官方 [原页](https://openai.com/index/introducing-aardvark/) 日期October30，L41–72私测披露与L37–39 March6,2026更新分别读。支持官方披露日期身份，不据RSS独自证明全网最早公开。

原文给出full-repo threat model/commit检查、sandbox触发与人审patch；没有公开可验证的新搜索/控制算法、可利用性判定条件或受控比较。私有golden recall缺数据/分母/预算，不能把92%反推上述机制的增量。校准关闭此次贡献，不保留1+2+2评分，不把已有sandbox/HITL原则计Durability/System Reach；不是因Books已覆盖、厂商身份或小效果而删候选。官方当前页没有原论文链接；有限两query `site:openai.com Aardvark October 2025 paper technical report`、`site:arxiv.org Aardvark OpenAI security researcher`只恢复原声明/其他报告，无Aardvark必要原论文，不将不相关gpt-oss-safeguard报告补证或扩扫新池。安全原core已核，发布事实留SCREENING并隔离2026更新，未核实现/复现/生产安全。

实际对读PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)780–808、Ch71/73开头、Ch66 78–108：已有trace与deterministic predicate、crash/exploit/severity/人审patch分账、repo-first与SAST-seeded输入边界。该正文比较只说明为何不需要改书，不作为准入排除的理由；实际Books提案/写入0。Stargate仅容量/设施公告的处置未发现需改机制结论。

## 代表性排除需要局部恢复

实际读取本日arxiv-v1-abstracts.raw五份完整精确v1题摘：26615、26339、26144、26788、26692。后两项FP16数值反证/Kimi Linear保留日期潜力正确，不因负面或混合attention/小模型排除。

前三项目前“只有组合/没有执行条件”关闭理由不足，应恢复为日期待定潜力，先不评分/不授Evidence，也不默认全篇队列：

- 2510.26615v1 SlideAgent：query-agnostic三级表示先构建、推理时选择激活Agent，涉及前置表示与在线问题依赖的执行分离，不能仅从层次分解属于旧主题关闭。先保留这一具体可能差额，若后来日期确认再核控制/成本归因。
- 2510.26339v1 GLYPH-SR：完整题摘有冻结主SR分支、训练text control及交替text/scene guidance，实际改变生成路径与可读性/感知质量的取舍，不只是拿现有VLM做领域指标。是否足够改变主线选择需围绕该生成机制判定；当前不要用泛视觉或OCR主题标签关闭潜力。
- 2510.26144v1 FM Agent：题摘明确新evolutionary sampling与分布式异步执行，包含GPU kernel/MLE主线，不能被Science应用一并排除，也不能因摘要未展开Ray执行细节就断言没有机制。只恢复主线异步搜索/评估这部分，Science数学应用继续暂缓；不为Ray或expert初始化本身评分。

本次是3个关闭理由的共同“组合即无增量”错误，不重开17个明确领域应用或全部61线索。以上原v1题摘已足够保留潜力；first-public尚未确认，暂不形成新候选/Books或全附件队列。作者须在SCREENING/README§5保留具体恢复原因，不能把从3变0关闭数当新增Evidence。

## Google参数窄修与精确停点

year/query不是当前正确历史过滤参数。复核者对本日独立执行category=2025/search=language model有限请求：curl max20实际exit28、20.006s、HTTP000/0bytes；同URL一次web不可访问。没有响应正文，不制造raw；没有沿用30失败为31执行。只修该源措辞/有限停止，年级成功也不能日级化。

FIRST校准停点：Aardvark关闭此次贡献、3项原排除恢复日期潜力，正式候选预计0（需作者同步实际分母）；Books提案/写入0。继续本日18项必要v1反侧、PPI隐私core、14源停止及分层标题样本，DAY未通过，不等整批。

## DAY抽检追加的局部恢复

2026-10-05T07:45:00+08:00：实际打开[2510.26104v1 OneTrans](https://arxiv.org/abs/2510.26104v1)完整题摘L16–18及版本历史L26–28。标题不能单独证明只是推荐应用：原摘要提出顺序/非顺序token统一，参数共享与token-specific参数分开，causal attention使跨请求KV预计算可用；可能改变表示可复用与在线请求依赖的系统选择。尚未核其对foundation/LLM主线的实际适用条件，不把推荐GMV改写为LLM效果，也不因当前无owner直接排除。

恢复为第四项日期/贡献范围待定潜力，不评分、不授正面Evidence/Books。提交2025-10-30T03:30:12Z仅发现字段，不证明first-public落窗。只需保留上述可能差额与日期重开条件，不形成全文队列、不重开其余16个明确领域标题。作者同步时将原17标题关闭改为16，额外完整v1题摘的实际读取归于本非作者抽检，不虚称作者先前已读。
