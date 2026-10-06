# 本日分层准入样本（非冻结分母）

完整题摘原证：V3_TOPIC_ABSTRACTS.md；此文件只保存具体准入链和校准问题，不替代证据审阅。

## 2602.12445 RBCorr: Response Bias Correction in Language Models

闭选题分数常混入选项偏置→跨model/dataset/prompt的LogProbs校正迁移不稳→能力评价要用本协议校正而不共用bias常量。拟评分2+1+2=5，owner PLATFORM-EVALUATION-SYSTEM；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12445v1。

## 2602.12468 Continuous Diffusion Models Can Obey Formal Syntax

连续latent采样不能逐token枚举合法后继→从regex接受概率解析score导引连续过程→形式约束选择需区别latent guide与离散hard legality。拟评分2+1+2=5，owner MULTIMODAL-GENERATIVE-PARADIGMS；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12468v1。

## 2602.12480 MXFormer: A Microscaling Floating-Point Charge-Trap Transistor Compute-in-Memory Transformer Accelerator

短序列固定model的weights重复外存搬运→CTT密度支持全权重驻留、静态12block流水与动态attention数字路径分工→容量固定/精度成本下可重新选择stationary部署；不从FPS授LLM长decode。拟评分2+1+2=5，owner INFER-TENSORRT-LLM；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12480v1。

## 2602.12521 Opus: Photonic Rail-Optimized Fabric in ML Datacenters

电rail all-to-all有功耗且OCS只有瞬时1:1→parallelism不重叠通信phase边界重配同端口→训练通信要按phase同步与reconfiguration成本选光rail。拟评分2+2+2=6，owner TRAIN-DISTRIBUTED-TRAINING；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12521v1。

## 2602.12532 CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning

vision/language高熵可能压过低熵force→早期VIB压高熵模态再恢复→接触控制fine-tuning应检验force利用的curriculum而不只加传感token。拟评分2+1+2=5，owner MULTIMODAL-EMBODIED-VLA；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12532v1。

## 2602.12587 Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers

稀疏/均衡expert仍可forget→head混合产生pre-router composition collision，headwise routing与Neff反侧→路由粒度需要看输入组合而不只看负载均衡。拟评分2+1+2=5，owner MODEL-MOE；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12587v1。

## 2602.12806 RAT-Bench: A Comprehensive Benchmark for Text Anonymization

直接identifier移除率不等re-ID风险→按统计人口从间接属性及变体估re-ID→隐私评价需要风险人口/utility而不只NER召回。拟评分3+1+2=6，owner PLATFORM-SECURITY；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.12806v1。

## 2602.13165 Asynchronous Verified Semantic Caching for Tiered LLM Architectures

单similarity门槛静态命中/错误reuse冲突→近阈值异步judge后promote curated static response到dynamic而不改当前response→缓存选择可把background扩覆盖与critical path分离。拟评分2+2+2=6，owner AGENT-MEMORY；仅准入，必要机制/配置/反侧尚待读，未采摘要性能数字。完整题摘来源https://arxiv.org/abs/2602.13165v1。


