# 2025-10-07 necessary boundaries

作者Huygens。本日实际读取13份精确v1必要安全/反侧段落，不是26日期潜力的正面Evidence完成。位置对应本目录`core-2510.<ID>v1.text.txt`及原HTML同节。未运行artifact/复现；抽取整页不代表逐行读完附件。

| v1 | 实际必要位置与限定结果 |
| --- | --- |
| 04401 | §3.1–3.3/4.1–4.2/Conclusion：8 API模型、200图/level、三level、640×480不重叠几何形；accuracy按object type非整图全对。颜色/大小可正可负，不宣称所有视觉计数无用；模型参数表未官方披露数不采用。 |
| 04477 | §3.1–3.2/4.1/4.4/6：人类lesion box+自动organ IoU形成seed，再VLM CoT，不是逐rationale医生验证。显式→隐式→answer-only课程；Hard数据敏感，Easy→Medium仍可靠默认。无前瞻临床验证、未完整等规模13B对照。 |
| 04514 | §4/5.3–5.4/7：ChartBench3800/ChartX1152，30轨迹tool recovery样本非全任务安全率。主实验单图/GPT4o，无严格新held-out验证泄漏；轴/OCR/工具选择失败保留，不授普遍agnostic或取消关键任务人审。 |
| 04533 | §4.1 Eq8–15/5/6 Eq21：光滑log-density、小步一阶增益非全局似然/无幻觉保证；匹配NFE非端到端成本实测。η过大径向校准受扰并降质量；图像artifact非语言事实幻觉。 |
| 04547 | §3–4/5.1–5.2/Limitations/Appendix E：middle-layer cached register+删token；50k训练图/20候选/1–15重复grid有成本。5 encoder/8或6bit PTQ；DINOv2-B有退步。FLOPs为pseudo-quant估计，非实际低比特kernel延迟。 |
| 04587 | §2.3–2.5/3/4.1–4.5：8医生、137WSI/25case、10.6h、921session/5222round；草稿经专家accept/edit/reject确有验证。日志监督非专家真实推理，作者明确AI anchoring bias与search-and-find跨任务限制。LNCO2 1245WSI的69.4%acc/62.9%precision/97.6%recall非临床部署认证。 |
| 04633 | §3–4/5.3/6：单topic/assessor刻意拟合，human qrel与ranking相关分开；只扩指定topic未判文档，跨topic/蒸馏进ranker相当训练test set。100–200标签建议限本实验。 |
| 04704 | §3.4/4.1–4.2：format/structure/matching三级success；max_dist只在结构有效且容差通过者计算。旋转/交换失败与parse分开；Table2 caption称unreadable比例与正文不一致，不替作者修正。科学应用仍暂缓，只保留必要反侧。 |
| 04773 | §4.2–4.3/5/Appendix A：KL标量坐标偏导非耦合参数下每个KL单调保证；top5%logits非敏感信息oracle。TOFU/MUSE不等不可恢复删除，作者承认MIA/PrivLeak困难与hallucination。 |
| 05024 | §2–3.6/5：SFT请求坏行为限制未请求泛化，至少5runs、sentiment10runs；selection在Qwen2 base不遵从时失效，2/6模型坏行为请求服从增加，Qwen2.5 StrongReject反侧。未测on-policy RL，长训练可能减效，不授安全免疫。 |
| 05087 | §3.2/4.1–4.3/5–6.2/Outlook：录音明确同意/去PII；10student×10=100模拟对话，六指标只是proxy。训练项目ID激活非新学生泛化；human评价是内部成员扮学生且有限，严格大规模human评价未来工作，不授真实学习效果。 |
| 05288 | §4.1–4.2/Algorithm1/6–8/Appendix C Algorithm6：原始preclip norms驱动C/γ，RDP只列q/σ，未给原始数据依赖适配的额外privacy证明；microbatch阈值C×size、noiseσC，record-level sensitivity未被此accountant单独证明（核验推断，非已构造违反DP实例）。无可比DP-SGD/DPAdam基线；synthetic10k×2/T4/64token/0.5B与2B不同scale，不授ε2/4/12保证或架构普胜。 |
| 05364 | §6/7.1–7.2/8/Limitations：理论受depth/precision/context假设，CoT额外步改变对象。比较训练/数据不同、主要English；frontier预测不是证明，压缩状态/lookup与quadratic成本各有边界，不宣布SSM全部替代或必然劣于attention。 |

## Petri必要安全核心

真正技术说明为[Alignment /2025/petri/](https://alignment.anthropic.com/2025/petri/)，原件`petri-technical.raw`。实际读Method/Design、Broad-Coverage Pilot、Whistleblowing controlled ablations、Limitations、auditor/judge可靠性段落，停止这些命题，不读所有seed/payload/system card。

Auditor模拟用户/系统/工具响应，可rollback/prefill/early stop；初版无真实code execution/realism filter。111seed×5auditor=555轨迹/target，五judge产生2775scores，非2775独立场景。25组合有同族偏好，相关0.75–0.85非human gold校准；Gemini auditor角色/格式失败与Sonnet4.5 awareness影响可比性。Whistleblowing的agency/leadership/真wrongdoing与叙事cue分开，harmless情景也可能泄露；风险发现不提供生产发生率/安全认证。尚待非作者校准，不授正面Evidence。

`petri-report.raw`实际是关联的Claude4 May2025 system card，不是Petri技术报告，保留真实下载和身份纠正，不作Petri读完证明。

## Google Speech-to-Retrieval

`google-s2r.raw/text.txt`实际读官方Blog全文核心：音频/文档dual encoder共同训练，直接候选检索后仍有多信号ranker；SVQ17language/26locale，ASR WER与retrieval MRR不能互代。groundtruth文本cascade揭示机会，不是S2R全部收益归因。预算/硬件/完整数值CI Not Disclosed，动画0.8/0.7不当实测。Oct7无时区日精度未证完全落窗，为第27日期潜力隔离；不评分/采用/扩MSEB全目录。
