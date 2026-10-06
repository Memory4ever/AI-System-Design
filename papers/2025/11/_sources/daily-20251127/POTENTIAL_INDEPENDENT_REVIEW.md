# Nov27 潜力及重要反侧独立复核

复核者：Carver；作者：Aristotle。实际分批复核截至2026-10-04T19:06:27+08:00。本日fresh治理及ownership见[MIXPANEL独立记录](./MIXPANEL_INDEPENDENT_REVIEW.md)；不重复20/15/07，不写Books/state/index或作者完成态。

结论：作者原46项潜力的完整exact-v1题摘准入方向、有限日期隔离及下列重要反侧通过；不是46篇全文或本窗Evidence通过。独立来源复核另发现DeepSeek Research遗漏一项，见[必要局部修正](./SOURCE_INDEPENDENT_REVIEW.md)，该项不混进原46核验数量。

## 全部46完整题摘

实际读raw-first-exact3/raw-first-fullabstract4、raw-negative-and-recovery5、raw-bounded12/13/18等原exact-v1题摘块，以及[Batch原生AB](./batch-denoising-abs.html)与[25篇尾部完整AB](./remaining-exact-v1-abstracts.json)。后25逐一对原生`abs-IDv1.html`的blockquote独立解析：15项直接一致，9项投影附加Comments但AB相同，另1项Agent0-VL仅TeX链接花括号内空白差异，已定点读原AB确认，不是正文增量或缺文。没有以API当前晚版摘要替代v1。

原21项：2511.20100、20172、20038、19997、20194、19822、19705、19959、20182、20644、20439、20095、19878、19861、19676、20710、20737、20494、20507、20736、19847。

尾部25项：2511.20196、20531、20641、2512.03057、2511.20344、20333、20315、20273、20072、19935、20713、19785、20648、20330、20325、20156、20721、20720、19912、19900、19820、19647、20099、20090、2512.03053。每项身份及具体增量对应[作者有限筛选表](./BOUNDED_CANDIDATE_FINDINGS.md)，不把以上省略共同前缀的列举当不同ID。

这些题摘实际提出表示/优化/量化/剪枝/通信/生成传输/工具证据/评价取舍，不因非LLM、小模型、局部反证、benchmark或成熟模块名称自动关闭。仅支持继续核验方向，实验优势、因果、预算公平、真实部署和安全效果尚未因此成立。

特别校准：Softmax Turing限unary/letter-bounded C-RASP及relative-position extension，不等于真实LLM可学习任意程序；Directional Asymmetry的表达类对称不等于优化路径对称，摘要局部反证不授无条件训练方向等价或架构必然因果；Conditional PAC v1是non-atomic distribution-free pointwise不可能性/几乎总expert的边界，没有晚版setwise router方案；Invertible check的roundtrip比较不授lossless或全正确；Scanford部署OCR数据局部反证不因library应用名关闭。没有读这些论文全部证明/附件，也未提前作46项owner缺额判断。

## 日期实际核

独立将[46项日期投影](./exact-date-fields.json)逐项与原`date-ID.json`的DataCite attributes.created/registered/dates比较，46项差异0。Submitted不是public；Available月精度、元数据Created/Registered/Updated不证明正文首公开下界。2512.03053/03057的Available为2025-12，不能由Nov submitted倒填Nov公开。其余仍缺使全球first-public上下界完全落入UTC[Nov26 01Z,Nov27 01Z)的必要原证据；没有用常规schedule补时刻。

实际读[Agent0原项目](./raw-bounded24.json)News L174–176：Nov25 arXiv release、Nov26群组、Nov29 code是不同节点，日字段无时区、不用Nov26群组重造论文事件。当前arXiv submitted时间不替代公告。日期隔离不撤销潜力、不评分、不进Books、不证明全分类召回或无遗漏；重开仅需对应原公告/作者首次公开事件或完全落窗上下界，不要求46篇全附件。

## 必要反侧实际范围

| 材料 | 本次非作者实际读取与结论边界 |
| --- | --- |
| Neuroprivacy 20710v1 | raw-bounded15/16 III threat L135–142、评价L227–280、消融L342–354；只image/caption query，无params/gradient且不限query，400member/400nonmember、80/20拆分、MPNet/ROUGE2/ROC-AUC；granularity与BLIP NoCaps的tau反侧不一致，caption utility不等全部VLM能力或DP保证 |
| CANVAS 20737v1 | raw-bounded16 L265、324–333、1248–1266；开放模型多turn失败/空白排除，重试三次后跳过，Flash 7/100 turn0 malformed排除；长轨迹退化/波动使final score不等过程稳定。未授所有模型全样本端到端成功 |
| Adversarial Confusion 20494v1 | raw-bounded19–22 §2/3/4、相关Table3/4与限制；next-token entropy扰动、clean/noise/cross-family与有害内容成功率不同；epsilon .01的proprietary transfer失败，large noise可见，compression/render/geometry及复杂multi-step Agent尚为未来工作。negative entropy文字与公式(3)加梯度的符号疑点保留，不自改公式或授实现复现 |
| Complicit Responses 20736v1 | raw-bounded20–22 Study4 L201–208、Methods L269、judge L282–284、训练L351–358及补充L782–783；两地各300人工样本、GPT4o局部judge对照、两8B模型/不同语言安全混合/SFT-DPO。EVIL与SafetyBench跨协议不直接成为同条件下降，stereotype相关不授因果/群体真实性，不能外推安全训练普遍有害 |
| SMFA 20196v1 | raw-bounded23/24 §3 L98–135、Table2 L206–223及评价L225–249；retain anchor上的方向冲突AND相对幅值mask，only-one mask保留恢复却forget弱；两7B LoRA和合成profile输出评价。refusal/FactScore零不证明参数信息删除、抗再提取或formal unlearning |
| Beyond Generation 20531v1 | raw-bounded25 §3表示、Table1 L176–178、L187–205必要反侧；hierarchical空间验证与bullet coherence取舍支持撤销旧误关闭。100图55→38按手工KG absence/阈值/验证失败口径，不授开放域事实真值或混合31.8/27%不同协议 |
| KyrgyzBERT 20182v1 | raw-bounded8/10 III/IV；普通WordPiece/fromscratch、35.9M vs177M、translated train/native1821test，F1 .8280 vs .8401；保留局部size/quality，不造morphology新算法、tokenizer因果或五倍运行效率 |
| DA3旧事件/当前纠错 | raw-bounded11 原项目News L183–188、受影响model card L313–318：Nov14 paper/project/code/models released；当前1.1 retrained/training bug/original deprecated。README限定窗commits原响应200/[]只限该path/API，不能证明全repo无改动；不采旧性能或将修复倒填本窗，修复时间仍具名保留 |

## 分层关闭

Image2Gcode 2511.20636v1完整AB实际读：制造slice cue/DDPM到G-code绕CAD的领域mapping，没有题摘新增通用foundation/训练推理机制或成立条件，范围/贡献关闭合理，不因DDPM成熟关闭；不声明读全方法。Qualitative Laboratory完整API AB实际读：社会科学persona访谈/climate-reception假说方法，不新增模型/Agent系统机制，范围关闭合理，不授人类模拟真值。

MRI/PET、材料、病理、抑郁/医学错误等只按明确领域标题分层，未读全AB/全文；窄API63返回/59身份不是全分类或全月筛选，DC338只是两个50标题段查漏。没有把安全/修订样本混作普通标题关闭，上述八项必要反侧均实际核，未变化单项Mixpanel结论复用独立记录。

本批不授日级完成。原46准入/隔离可复用；剩来源修正和六部分同步属于普通可执行工作，不包装external。Books写入0，无POST对象。
