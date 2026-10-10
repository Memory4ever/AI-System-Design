# 必要证据与actual owner：单篇即推进

作者supp_jan15；root已实际校准四篇完整题摘。原52不动，未获任何新共享Books锁。精确arXiv v1，45项DataCite中的本四项原字段均正常Submitted cohort，正式ID registered Jan14T02:55:23–03:00:45Z；结合已核ID/普通公告规则限定BJT Jan14，不把Submitted/registered单独当首次公开。RAVEN原文仅说code will be available，无早dated正文项目链接。其余直接项目轻量较早信号待必要定点，不展开全部history。

原件：method1/2在[increment-j15bench_method1](./increment-j15bench_method1-20261007.txt)、[method2](./increment-j15bench_method2-20261007.txt)；method/评价必要补段在[core3](./increment-j15bench_core3-20261007.txt)、[core4](./increment-j15bench_core4-20261007.txt)、[core5](./increment-j15bench_core5-20261007.txt)、[core7](./increment-j15bench_core7-20261007.txt)、[finish8](./increment-j15bench_finish8-20261007.txt)，RAVEN费用在[find6](./increment-j15bench_find6-20261007.txt)。其他三项普通必要证据/actual owner仍继续，不把本包建立视为完成全部。

## 08620 ViDoRe V3 — 正式稿evaluation重要差额；2+1+2=5 标准完成，root具体Existing通过

实际exact-v1 §3.3–3.5/§4.1–4.3/Tables3–5、AppH/J与Limitations。拟采用仅正式稿新增端到端RAG/grounding评价：retrieval NDCG、oracle上下文answer及bbox分开；visual page成功不意味着可指出证据。Qwen2.5VL32B预过滤且跳过>30候选pages，76人/13senior/12k标注小时；GwetAC2 .760、人bbox IoU .497/F1 .602，不能把标注当穷尽全部支持。8公开2私有，私有不做E2E，EN/FR语料及6语言翻译非全球范围。

§4.2同Gemini3Pro image hard +2.4 oracle/+2.8 ColEmbed是局部；hard为六model至少一个no-ground失败的cohort条件，并非天然不可答/记忆证明。generation hybrid top5visual+top5text不去重，54.7 vs54.5/52.1且context预算变，不授质量等价单因果；AppE retrieval hybrid才去重且unrankedF1，两个pipeline不混。§4.3 Qwen30A3B/Gemini3Pro best-over-annotators bboxF1 .089/.065 vs人.602，页索引/框粒度影响分数，不解释内部因果。AppH fixed Gemini输出5judge runs mean72.09 σ.22 α.91是consistency不是truth；两domain5E2Eruns65.74 σ.94 α.80不是全队列seed。H1003000h评测与12k人标费用，precision/batch/concurrency/SLO Not Disclosed，未复现。

直接项目轻核：[HF org](https://huggingface.co/vidore)→[作者Blog](https://huggingface.co/blog/QuentinJG/introducing-vidore-v3) Published Nov5,2025，明确更早dataset/annotation/retrieval发布。当前mutable顶部‘preprint now available’列新增extensive retrieval、end-to-end RAG、VLM grounding，不能据mutable告示给Jan14发布日期，更不把dataset第二次计首次贡献。正常arXiv正式稿ID已核Jan14界，只采用§4.2/4.3新的evaluation命题而不采用早dataset机制；若不能确立这一重要差额的当窗事件，则单项精准日期隔离，原件/Existing留恢复，不搬旧日。原始直接项目与Human G补段在[directhuman](./increment-j15bench-directhuman-20261007.txt)，博客dated原件已保存在[increment-j15vidore-datedblog](./increment-j15vidore-datedblog-20261007.txt)。

actual Ch66:1065–1100完整顺读已有pipeline身份/阶段receipt、oracle非生产、retrieval/navigation/grounding/effort分账、answer正确≠多模态evidence且reference非全部合法链；本次局部反证不改这些判断。root实际核§4.2/4.3必要原证及该完整邻接，标准审阅/具体NoChange—Existing通过，无书稿写入。只本次正式稿evaluation事件，Nov5旧dataset不重计、mutable blog不授日期。

## 08611 VeriTaS — 2+1+2=5 标准完成，root必要原证/Existing通过

实际exact-v1 §3七阶段/§4.1–4.4/Table3/4、§7、AppE/F.1/G.1–2。ClaimReview371k→credible/appearance/media链，7阶段自动重写/对齐verdic与media、四judge ensemble、分歧过滤及gold-conditioned rectification；不能称全自然分布，24k balanced Q1'20–Q4'25每季1k，longitudinal2.4k。真实性、contextualization、veracity/contextcoverage先后判定，Integrity min只含2–4不含authenticity；负侧早停后的空白未测，不把边际分数当独立概率。连续[-1,1]certainty不是校准概率。

63人审claims≥2native/C1，MSE .034/Acc96.8仅该过滤样本；G.1有12人/372annotations/9语言，先读同一fact-check article且丢分差>1与<2labels，不授四模型独立真值或全库无误。Single-run六models，Gemini两种native video vs其他fiveframes不matched；search top10、抓top3/max5queries，before-claim-date/domainblacklist只是泄漏缓解不证明无答案曝光。post-KCD MSE变差即使text-only仍有内容/选择分布替代解释，不授唯一记忆因果/refresh即免污染。季度更新到2028是未来承诺不是已经全完成。无严谨crosslingual去重，rectified句式shortcut，$14.9k/$600quarter是估计、2700GPUh/8H100标注非训练，precision/batch/concurrency/SLO Not Disclosed；code未来/数据gated，未核实现/复现。当前abs/本文无明确更早完整正文链接，本次正式ID普通公开日期界已核。

actual Ch66:141–147明确标签生成链/轨迹粒度/缺失标签与人工模型分工；3177–3185已明确provenance、一次未检出不证明无污染、refresh实例/基础来源身份及标签/重抽费用，不因新benchmark名字/季度承诺加书。root实际核§3.1–3.6、rectification/季度平衡/§4.2过滤样本及actual对应正文，标准审阅/具体Existing通过；属性min聚合/NEI协议保报告具体case，不自造长期新机制，无Books diff。

## 08623 SafeRedir — 2+2+2=6 安全/具体接口差额深入完成，root实际POST通过

实际exact-v1 §III、IV-B/C/TableIII/IV、V配置/对照/transfer/cost、D-B/C/Alg1–2、E-A。text+latent+timestep detector触发tokenmask归一方向/alpha redirection与K-step cooldown，改cross-attention conditioning而base冻结；不是参数知识删除，也不是opaque API无需hooks。D-C明确需prompt encoder产物、U-Net latent/encoder_hidden_states与scheduler hooks，no backbone retraining≠辅助头无训练。120k实例来自300pair+300adversarial×2seeds×50steps random80/20，未证明prompt-family split，TextLatT IGMU99.73/MMA74.72是标准accuracy非校准保证。

IGMU unsafe/safe prompts各fiveimages，NSFW NudeNet/EraX_NSFW/MultiClf、style及Church另detectors，FSR=未检出不等真实安全；ASR标注up-arrow与实际lower-is-safer相反，按数值/对象解释不照箭头。benign CSDR/LPIPS/FID/QAlign多维不同，alpha强化可损FID、mask保留又降低FSR。I2P .70/MMA1.73不是全优于AdvUnlearn1.03 MMA；主动攻击NSFW9.38 vs4.69，style50.16残留。八A100 server、50MB/<1.5%延迟局部作者称述，precision/batch/concurrency/fullSLO Not Disclosed，不授端到端常数开销。transfer same-text-encoder v1.4→v1.5/community局部，v2需改dim并重采dataset不是通用零样本。Current直接repo README只artifact/code配置，无dated更早完整正文，轻核停止不扫7commits；不声称实现已核验。Hook/评价原件在[increment-j15saferedir-hook-eval](./increment-j15saferedir-hook-eval-20261007.txt)，本文关键全文补段此前原件可复核。

actual Ch72:376–378 suppression与substrate observer已承载‘非知识删除’，565–590已output-time和训练modular分工；尚未承载**sampling-time safety detector消费latent/timestep，并通过版本化embedding hook/cooldown干预，检测资格与hook覆盖分开**。拟仅在376后单段接prompt/context substrate：冻base时可另训风险头、每step proposal及cooldown修改conditioning，保aux权重/encoder/latent/timestep/hook/schedule身份，预测accuracy/未检出不是全路径安全；变化模型需重采/重标定，费用/误拒与残留同验，hook不覆盖/资格不足回原拒绝/过滤/人工不发布。不写算法配方，不宣称状态安全或遗忘，root必要source/actual owner PRE通过后已窄写Ch72:380及自身note4333；root实际376–386完整邻接/正文/自身note POST通过，窄锁释放。

## 08832 RAVEN — 2+1+2=5，水印安全反侧/确认gap深入完成，root实际POST通过

实际§3、§4.1/4.2、§5/Table2–5、§9：威胁只需一张带水印输出和公开img2img，无key/detector查询/weights/clean-watermark pairs。替代表示重构结合reference attention保持部分内容代理，却可损坏检测；不能由常见pixel/frequency扰动robustness签发这种生成重构下的持久性。拟保留防御验收对象，而不是操作配方或声称已证明3D真实新视角。

SD2.1、512²生成数据来自COCO5000/DiffusionDB1001/SDprompts8192；检测1000pairs/TPR@1%FPR，bit-based另测accuracy，不能合并为统一accuracy/risk。Table2平均COCO TPR .026 vs UnMarker .078是作者所测schemes设置，不授所有水印失效；abstract15/method14/Table16/Conclusion14数量口径不一致，不报统一方案总数。FID/CLIP均proxy且小视点变化允许内容变化，不证明严格语义身份或合法所有权；同图pair完整identity未公开核验。strength升高损FID，取消correspondence attention仅qualitative结构坏，color处理改善FID，不能归因全部收益唯一几何机制。三SDbackbone局部迁移非全部architectures。single A10040GB/固定seed/约6s每图是局部运行，precision/batch/concurrency/SLO Not Disclosed，不把zero-shot写成免费或与所有基线matched训练预算。代码仅将来公开，未实现核验/复现。采用最小反证不需要重读全部qualitative附件。

actual PLATFORM-SECURITY Ch72:185–195原邻接：187权重watermark取证非预防；189可替换decoder/generator及更新身份；文本unforgeable recovery/严格编辑模型为下一分支。已在189后正文191窄补**输出重新生成形成内容近似派生物，pixel/frequency扰动与内容proxy不定义同一水印持久性合同**：冻结原watermarked output/派生artifact/transformation class与detector identity，分别核信号持久性、内容/任务保持，不由高CLIP或未检出签发origin/authentication或判非AI；生成重构付费，超出威胁模型回退签名originrecord/provenance及人工取证，旧水印仍sensor。原文支持该受限压力，工程记录/回退是作者推断。root实际必要source/owner PRE、185–201完整邻接/正文191/自身末注4325 POST通过；窄锁释放。
