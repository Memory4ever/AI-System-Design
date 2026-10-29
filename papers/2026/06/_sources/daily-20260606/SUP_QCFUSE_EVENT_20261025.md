# QCFuse同family本窗事件差额与必要限界

作者`jun06_continue`，2026-10-25。精确事件[2606.05875v1](https://arxiv.org/html/2606.05875v1)，具名更早[2604.08585v1](https://arxiv.org/html/2604.08585v1)。A7/R4的题摘、Jun05联合日证与早稿家族线索有效；只有限比较受影响机制/证据，不为所有历史版本做diff。

## 家族与事件判断

本轮实际读早稿§3.1–3.3及新稿§3.2–3.5、4.1、4.4–4.6直接反侧。两稿同QCFuse、同首作者与多作者重合，同anchor-conditioned query→critical-layer token选择→layerwise recompute机制；旧稿指向QCFuse-Demo、新稿指向同作者QCFuse项目。按项目与核心设计将其归同一Source Family，而不是由新arXiv ID再开独立首公开家族。当前[作者项目](https://github.com/uYanJX/QCFuse)README也承载同一pipeline，但含Sep/Oct后续news，不作为Jun05实现或性能签证、不追后续release。未发现将此事件视作撤回/纠错的notice。

**拟判：同family重要扩展事件，不是新family，不重复评分。** 新稿不是仅多模型/改标题：早稿用高Key-norm anchors/单个关键中层及平均ROUGE，未定义当前的span-label固定预算校准；新稿新增将回答证据位置覆盖作为诊断，比较anchor规则/压缩比与critical-layer预算。实际改变“少量anchors与某一中层天然足够”的配置依据，值得保留其校准合同与证据边界。早稿主机制和原Books两段不重审；旧Jun05对05875的2+2+2=6仅保历史字段，不当本事件新评分或加总。不把旧归属搬到本日。

## 本事件必要支持和关键反侧

§3.2.3在SQuAD/NewsQA/NaturalQuestions上把答案span映到原context位置E；先固定Top10%选区P，Recall@10%=|P∩E|/|E|。原文说在端到端QA前固定default，校准集不同于主评测集合。固定10%是profiling selection budget，不是anchor保留率，也不是线上recompute ratioρ。答案位置覆盖只是一种证据诊断，不能证明multi-hop支持链完整、未来query充分或输出正确；完整样本数/分割种子/CI和跨域安全没有披露，不补造。

§3.3对比Sink/Knorm/KVzip，在同all-layer scoring与Recall@10%协议下选择KVzip@10% anchors；KVzip用repeat-context reconstruction probe收attention，不是旧Knorm改名。取每chunk ceil比例，必须保anchor原顺序和request position，query仍位于完整C之后；compact anchor view只condition query，最后评分和重算位置仍来自全部原context，不把anchor subset当context eviction。离线KVzip准备和profile不是线上免费或总状态10%。

§3.4先测每层定位Recall再取最高k层、合分，profile叙述用Top3为default；§3.5明确query probe须运行至选区最深层、预取这些层的完整context K后才启动fusion，因此仍付序列化selection与cache加载，不是只读anchors就开始。完整PIC依旧按正常流水加载，压小的是pre-fusion view，不是取消fullcache/所有IO。

§4.6.1是ρ0.1–0.5的平均质量，LongBench与RULER对更多anchors趋势不同，不由近10%一处推普适最优。§4.6.2列举first/fixedmiddle/final/all/Top1；文字和Fig16caption明确Top1最高，却称支持defaultTop3：它只支持有用信号集中在profiled中层，不能证明Top3较Top1端到端最优或实现一定用Top3。本次不照录固定KVzip/10%/Top3为通用recipe，不由all-layer attention相似度签gold质量。支持与这项关键反侧足够，停止，不重读无关全部倍率图。

§4.1/4.4–4.6条件：SGLang0.5.4/BF16，同服务栈、2H20/128GB DRAM/1TB NVMe/标称10GB/s；Mistralv0.3-7B、Llama3.1-8B、Qwen3-8B/14B，LongBench三QA及RULER mq/mv/vt，每集200样本、512chunk/主20chunks、ρ0.1–0.5。未把当前repo后加500样本/32B等回填exactv1。比较器在同stack隔离selection规则，不是各原系统全能力；TTFT含线上selector/加载/recompute/firsttoken，不含offline准备/profile。正文只给server两卡，不推每model的TP；输出长度、batch/arrival分布、SLO/独立重复/CI未披露不补。Stress固定ρ0.5且为质量相近区域，不是每任务exactparity；NVMe低带宽对照与均值TTFT/吞吐也不认证tail或生产。未核图像素、代码或复现，无headline数字采用。

## actual owner与最小PRE

实际Ch45“从Chunk命中到有上下文的选择性重算”完整两段确已承载早稿主机制/全费/退路；不重写它们。其高Keynorm/关键中层是旧分支的具体描述，不让新稿静默覆盖；当前第二段有代表性/selector miss，但没有明确将anchor/layer作为经独立标签校准的artifact及profiling预算/线上预算分责。现有不同机制的budget搜索/selector proxy也不承载这次压缩view的差额。唯一`INFER-KV-CACHE` Ch45只需自然补一段；Ch44/46交接沿本日实际已读有效层复用。

拟位置：QCFuse旧完整第二段及08585marker之后、紧接RedKnot首段“选择待重算token还隐含一个粒度假设…”之前。只补以下一段，旧两段与RedKnot两段不动；尚未保存Books，待唯一reader首次事件/必要/actualowner/PRE及root本轮fresh窄授。

Anchor与关键层也可以是离线校准的配置，而非永久固定的高Key-norm与单中层规则。一条[同家族扩展](https://arxiv.org/html/2606.05875v1#S3.S2.SS3)用带答案位置标签的独立材料，在固定token选择预算下比较证据覆盖，再选择anchor评分/比例与少数关键层；这个覆盖率只诊断选择器，不能证明多跳支持链完整或最终答案无损，也不等线上重算比例。配置须绑定模型、校准人口、anchor规则与层集合，保留原位置；query仍要运行至所选最深层、读取这些层的完整context Key，完整PIC的驻留和后续加载也未消失。原文Top-3默认与Top-1端到端消融并未闭合为统一最优配置，因此不照录固定recipe；准备/profile、selector、传输与独立质量回归都计费，分布漂移或净费用不合时，保留原已验规则、扩大观察/重算或完整Prefill。<!-- source-family:SF-2026-ARXIV-2606-05875 -->

本人注拟：`SF-2026-ARXIV-2606-05875`，与2604.08585同QCFuse家族重要扩展事件，不新family/不重复评分；jun06_continue，Daily2026-06-06补Jun05。exactv1 §3.2–3.5/4.1/4.4–4.6受影响必要，只离线span证据覆盖校准/预算及artifact责任；保Top3 default与Top1消融未闭不照录recipe，原Knorm/单层分支保留。两H20/BF16/四model/六任务200样本仅作者v1，非当前repo扩充；offline费/最深层probe/完整PIC/质量与退路保留。未核图像素/代码/复现，不授无损或SLO；事件/PRE/新窄授/真SAVE/唯一POST按后到事实记，不预I/DAY。
