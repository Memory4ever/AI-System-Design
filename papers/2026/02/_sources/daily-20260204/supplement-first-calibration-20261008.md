# 2026-02-04 增量首批准入校准包

新增窗口唯一2026-02-03北京自然日；旧17行/旧公开时间/评分/连续§4冻结。独立复核尚待root，不自授通过。

## 拟入选

HySparse家族2602.03560v1：MiMo官方Paper目录明确February 3, 2026（supplement-arxiv1）；arXiv abs仅支持精确身份/v1，无撤回或纠错标记，本次归属依据为MiMo作者机构公开日期，不以Submitted或HF标签替代。官方事件是论文首次公开，未发现重要修订声明；不是把arXiv后公告回填。

完整题摘实际读于supplement-ab1及hysparse0。旧动态稀疏选择每层代理及全KV保留→原文全Attention层输出选择和KV供后续稀疏层共享、另保独立SWA局部分支→需将减少访问计算与减少持有状态拆开，并重新评估跨层源/消费兼容及局部表征缓存。拟评分2+2+2=6，标准审阅；属于训练时架构，不称即插即用无损推理。Ch22已有同家族源注，仅是否具体覆盖还待原文必要机制/对照和正文相邻实读，不以源注判断No Change。

## 代表排除

GLM-OCR Feb3 API release：supplement-native2的官方release条目实际核心、supplement-hysparse0中的guide完整核心与input/output/API调用说明已读。Feb2初始公开与Feb3 API上线同家族不同事件；release只给CogViT/GLM0.5B/连接层与CLIP等既有组件，guide给文件大小/100页/输出格式与layout_parsing调用，没有宣称此前接口被改变、权限或执行语义修订，也无新增成立条件对照。常规服务规格不是新的系统机制，不因API上线或SOTA单榜准入；贡献前关闭，不评分。不把当前guide所有内容当Feb3不可变版本。

Google Feb3 virtual-care：官方月份目录和原文标题明确临床领域研究计划；AI for Science暂缓，不借Evaluation回收。保旧关闭依据。

2602.00279v1完整题摘：虽然科学QA背景，但其拟贡献是UQ测量混杂（instruction tuning极化token置信/ECE盲区/consistency相对校准），不是直接以科学应用指标准入；潜在主线贡献待核公开日，不因AI for Science一概排除，也不评分。00300v1完整题摘：Patchscopes解释被decoder prior压倒，BALOR patched/unpatched logits对比抑偏，潜在表示解释faithfulness边界，亦待官方公开日。00459v1完整题摘：length-controlled summaries得到importance分布及attention/head/family相关性，是局部机制证据潜在贡献，不能因未有因果干预直接排除；00594v1完整题摘：单流token隔离acoustic constants、保phonetics/prosody替代辅助disentanglement，潜在representation设计，待公开日。上述均不使用submitted/索引做公开证据，尚非确定候选。

## 有界入口

arXiv主题查询拟为model(CL/LG language model/Transformer/MoE)、multimodal(CV/RO foundation/world model/VLA/diffusion)、system(DC/AR/PL/OS/PF GPU/inference/compiler/cache)、agent(AI/IR/MA agent/memory/tool/retrieval)，本窗缓冲提交仅定位。已实际model API取文失败；本日CL首100/AI首25相关标题浏览、DC/CV首25失败仅作有限查漏，不转为整月/整分类逐项队列。搜索Feb3/F​​eb2日期是线索而非公开证据。必要定点日期入口后续继续，不运行90天catchup。
