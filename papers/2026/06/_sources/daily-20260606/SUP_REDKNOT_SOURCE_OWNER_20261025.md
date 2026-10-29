# RedKnot 2606.06256v1 必要缺层 / actual owner / 最小PRE

作者`jun06_continue`，2026-10-25。[exact-v1](https://arxiv.org/html/2606.06256v1)。A6/R4完整题摘、身份与Jun05联合日证复用，不重日期；保原`3+3+3=9`，不新评分或搬旧候选归属。

## 复用与补读范围

定点读旧Jun05 V2archive仅本ID review/benchmark/Books：head-aware reuse、segmented paging及三model/H800/六QA与长上下文条件有效复用。旧Books existing摘录却为idle-HBM借用，不承载head-conditioned PIC有效性；actual Ch45同ID仅旧trace的一句增量，没有承载完整机制/退路，不能视为实际I或NC。未改旧日文件。

本轮实际读精确v1 §2.1/3–6、Algorithms1–2及5.1–5.5直接反侧，未核图像素、代码或复现实验；支持与关键反侧足以限定下面两段，不为全部headline继续扩附件。

## 必要支持与限界

§3.1/3.4指出token共同修复会合并各head的重要集合；这是细化恢复单位的动机，不证明所有token-level PIC都不可用。§3.2依NIH等有限profile辨global/local，不能把模型内角色稳定性升为所有输入定律。§4.1–4.2将RoPE相对旋转和context mismatch分开；位置对齐只移除位置因素，不能恢复已变前缀的上下文。局部head重用/有限window修复、深层global恢复及partial FFN是近似策略，不是数学等价性。

直接反侧：§3.3一处讲active neurons，§4.2/Alg1实际是选token执行完整FFN、其余residual identity；本次采用后者，不混成channel稀疏。Alg1 shallow分支只显式LocalAttention，未明确global heads如何处理，和正文“global头重算”的普遍措辞不能合成完整执行recipe；不照录调度或宣称完整恢复。Role比例在NIH与部署表不同、Qwen前48层full/后16层window也不同于统一layer策略，故不取固定比例/普适window或无损承诺。

§4.3 head segment标识(layer,KVhead,segment)，页映射及ragged长度可让kernel看到异构长度；此处只作有效性合同的执行交接，不在Ch45重复Ch47 allocator推导。Alg2遍历segment写同一head输出但没完整展开多segment softmax聚合，不能照录为独立实现或完整正确性证明。原文的相同sparse pattern数值接近，不证明该pattern等于原dense模型。

§5.1：8×H80080GB单server、2×Xeon8468V、2TB、NVMeRAID，Ubuntu24.04/CUDA12.9/PyTorch2.9.1/Triton3.5.1；Llama3.3-70B TP8、Qwen3-32B TP2、Mistral7B TP1，六QA、context7.9K–65K。全实验统一precision未披露；5.4 microbench bf16不能移给整服务。原文SGLang/vLLM fork措辞混杂，不能推唯一已核engine实现。输出长度、完整在线arrival/并发、生产SLO、质量样本/独立置信区间未披露不补；CoV定义不自动证明每项独立重复完成。

§5.2作者F1/EM及首token logits/TopK切片支持局部quality–latency取舍，首token接近非完整生成等价；未看图像素不采精确点。TTFT排除offline segment prefill，重用不足时准备成本需重算；§5.3 FLOPs为解析计数，不是独立实测吞吐。5.4固定halfglobal/halflocal及320window是microbench，与deployment profile不同；dense+mask的dispatch罚时只在作者backend条件内成立，不把其null-mask限制提升为所有现代SDPA规则。Fused-varlen与per-head launch也不能合并归head算法。

§5.5 PD在同一8卡server分GPU组，并明确未集成SegPagedAttention；burst当前dense+mask端到端结果与5.4的物理布局microbench不同，capacity-bound吞吐是模型投射而非已观测fleet。Byte减少仍可能由packing/setup抵消transfer-time节省。无单独matched-work消融足以把全部收益归唯一head恢复，故不采用headline倍率、跨机可扩展性、零fee或SLO。§6 native per-head engine/默认PIC仍是未来方向，不当完整产品已交付。采用命题仅为应按head判断可复用与待修复，不依赖未闭recipe。

## actual Books比较与最小PRE

实际读Ch45 Prefix reuse身份段、Structured knowledge相关完整head/selector段、KVCompose两段及“从Chunk命中到有上下文的选择性重算”完整两段/两侧；Ch44/46开篇交接与Ch47本日实际页表/head-group/Kernel语义已读。未找到同family真实正文；trace一句不计。KVCompose是不同位置打包但同head长度、QCFuse是query-conditioned token选择、Tangram是retention形状/物理页，它们均未承载同一chunk换prefix后的headwise有效性/repair合同。唯一`INFER-KV-CACHE` Ch45小gap成立；页布局/kernel只交接Ch47，不双写。

拟精确插入位：Ch45 QCFuse第二完整段末（含`SF-2026-ARXIV-2604-08585` marker）之后、H3“条件 Anchor 与时序预算不是同一种淘汰对象”之前。只插以下完整两段与独立marker，原两侧不改。尚待唯一reader首次必要/actualowner/PRE、root本轮fresh新窄授，未保存Books。

选择待重算token还隐含一个粒度假设：同一位置的所有head一起恢复。如果不同head需要修复的位置不一致，共同token集合会合并各自需求；另一条[受限head-aware复用分支](https://arxiv.org/html/2606.06256v1#S4)因此把同一chunk在新前缀下的有效性拆到layer/head：对前缀敏感的部分作更多恢复，对经校准的局部head保留较多旧状态并作有限修复。RoPE位置对齐与上下文恢复仍是两件事，离线global/local角色也只是受测分布的配置，不是未来query的有效性证明；chunk命中不能作为所有head共同的可直接读取许可。

执行层还须携带head角色、原/新位置、有效范围与修复状态，让分页和kernel按已声明的异构长度读取，而不是仅给dense tensor附一个mask就记下物理节省。该分支也可对部分token跳过FFN更新，但这改变的是近似恢复路径，不能继承相同稀疏pattern的数值接近作为原dense模型无损保证。离线预填/profile、位置变换、修复、packing和传输都计费；原文物理布局microbench、未集成该布局的服务切片及容量推算须分开验收。角色漂移、上下文依赖、质量或全费不合时，扩大恢复集合、保留普通prefix复用或完整Prefill，不由少FLOPs/bytes放行端到端收益或服务SLO。<!-- source-family:SF-2026-ARXIV-2606-06256 -->

本人注拟：`SF-2026-ARXIV-2606-06256` — jun06_continue，Daily2026-06-06补Jun05；exactv1 §2.1/3–6及Alg1–2必要，保原3+3+3=9/唯一Ch45。只headwise PIC有效性与repair合同，页执行交Ch47；保shallow global/segment聚合未闭、不照录recipe，FFN为token选择而非neuron稀疏，位置对齐非上下文恢复。5.4micro/5.5dense-mask服务/容量投射分开，offline准备与全费、质量及退路保留；未核图像素/代码/复现，不授无损/跨机/生产SLO。必要/PRE/新窄授/SAVE/唯一POST按后到事实记，不预I/DAY。
