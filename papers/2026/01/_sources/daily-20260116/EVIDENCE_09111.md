# 2601.09111v1 — structured experience to fast visual policy

[精确HTML](https://arxiv.org/html/2601.09111v1)，必要原段见PRIMARY_09111_CORE.md及PRIMARY_09236_HUMAN_09111_EVAL.md。2+1+2=5；不是快慢模块名称准入，实际§2.5把LLM反思执行记录变成结构经验S_t/C_s/T_n，各embedding拼接经MLP，当前visual feature为query、经验为key/value cross-attention，再融合至DUET动作特征。ISC指令风格转换是另一组件，不把联合收益全归经验。root实际必要接口/Table4因子和Table5容量分支已核。

GSA模拟150场景/600路径的七种指令风格；DUET及CLIPViTB16/textencoder9layers、slow Llama3.2 vision，实际尺寸/hardware/precision/全反思调用与经验维护预算NotDisclosed于必要核心。Table4 baseline TestNScene SR42.4/SPL42.8与其SPL路径长度惩罚SR定义不一致，不采用baseline量化增量，尚无同口径修正。Table5 K是经验库容量，200不是全部slice单调退步，不能称通用最优K；有限模拟不能授开放泛化、全链尾延迟、实机闭环或物理安全。局部分组件对照只支持交接分工可行性。来源/策略/适用环境/寿命身份与fresh observation校对是工程边界，不冒称作者完整实现了该契约。

实际owner MULTIMODAL-EMBODIED-VLA：当前episode-derived latent memory/read gate原有内容未表达语言结构反思经验作为fast visual cross-attention对象，root实际Ch26目标段/必要原源通过窄差额写前批准。Ch26 L505–507两段与L1790末注已写；root实际POST将‘反思间隔’纠正为‘经验库容量’，单点实际再核通过、锁释放。深入完成并整合，不授本日日期冻结/日级Gate；未运行代码或复现实验。
