# RelativeRanks17917：有限控制命题与PRE

resume_mar17，fresh03-20补03-19，仅既有准入5分家族。AB/date独核§2有效复用，不重复同稿日期。必要[exact-v1](https://arxiv.org/html/2603.17917v1)§II–V/Eq1–5/T1–5、必要B评价口径及C两执行路径反侧已实际读；不精确拟合图，不核repo/复现或全附录。支持与直接反侧够此命题即停止。

## 采用命题与关键原证

固定assignment而改变centroids，把“码分配保持”与“重构值/顺序/幅度保持”分开；仅采用作者有限扰动实验暴露的联合验收边界，不授rank-only充分条件/普遍安全变换。Llama3.1-8B-Instruct、SmolLM2-135M与私有CompactifAI预压缩3B；attention/MLP投影被聚类，embedding/norm/head保持。逐层K按PPL增量≤.5选，但全模型目标不由此自动保证。T1主要l10 gate K32，T3真实早/中/晚层直接反侧；T2保序非线性变换也可坍塌。III.2仅Figure3文字说明分层替换及mean/variance纠正延迟、未消除退化，不采精确曲线值或唯一因果归因。

内部WikiText2 lm-eval batchauto与vLLM0.7.3的PPL不能合并。Repeat/randomseed、聚类/selection/healing数据与全部制备预算、不确定性未充分披露；不将单WikiTextPPL授全部能力。A/C分别internal H200 batch1 prompt50/gen50 greedy与vLLM512→128/concurrency1，后者表未绑定具体GPU；rebuild-to-dense实际仍占denseGPU memory，LUT更慢，precompression速度不可归因clustering，不采throughput headline。

## 保留的中心反证（不带入正面Book）

- T3 Llama early l1保序signscramble117.39，保sign破序9.64，直接反驳原文“每行两破序均比两保序更坏”；Smol晚层gaussmono39.40/27.52也非≤1.1倍。T1随机替换同时改变L2/频率加权统计，不能把粗方向比较授sole-rank因果或必要性定理。
- Eq5正a的线性输出顺序公式正确，但SiLU在负域并非全局单调、SwiGLU乘积与residual不保通用顺序；Llama/Smol RMSNorm不作LayerNorm式减均值，不能将其说明授affine gauge。取两个负输入−2、−1，SiLU约−.2384、−.2689即反序；这是本书数学反例，不称作者运行失败。
- Eq2/3的加权均值/方差同时保持，正affine在非零方差下只能a=1、b=0；原结论不能把任意a>0映射说成同时保统计。III.2校正随机向量的统计与从原centroids任意affine变换不是同一命题。
- C Eq6代数重组正确，但每output的label分组不同，一般不能只算共享DK后获得DK+KO成本；作者同节亦认plain分块scalar布局reuse不足。这不授任意LUT加速。

这些冲突不删除已准入潜力或降5分；若reader认为有限扰动边界也依赖未闭合中心，按中心隔离保反证，不假NC。若要采用普遍rank充分/affine-gauge/唯一scale原因，一次精确请求固定加权统计和扰动幅度的paired控制、真实norm/非线性图与逐层trace，及完整制备/执行费用；当前最小采用不依赖这些保证。

## actualowner差额

actualCh49 `INFER-TENSORRT-LLM`完整930–1067（格式/校准到非均匀codebook+productLUT）与1233–1285（代数变换/量化不等义），Ch48必要交接与Ch50开头1–70已顺读。1045/1047已有centroid/assignment/kernel共同身份、1079另有重分配与centroid更新自由度，但没有固定assignment扰动centroids时“顺序保留仍不能脱离跨层幅度/offset验收”的此具体试验边界；主题覆盖不是NC。不新node；拟1047既有nonuniform-LUT边界之后、MoE共享输入分支之前一短段，未授锁。

## 逐字PRE（待非准备者）

码本还应分别验收 assignment 与 centroid 值：固定索引后只替换代表值，可以测试顺序、幅度与 offset 的作用，却不能由“保序”自动批准压缩产物。受限的[权重聚类扰动实验](https://arxiv.org/html/2603.17917v1)中，部分中层保序替换较温和，早层、非线性重标定及多层联合替换仍可明显退化；按实际 cluster 频率修正均值与方差只延迟了跨层崩溃，不证明 rank 是充分统计量或通用 affine gauge。应冻结原 assignment、变换、实际 normalization 图与层段，用完整模型的 held-out 质量检查联合误差；局部统计、PPL 和磁盘 bytes 不能替代全部能力或执行验收，离线选择与恢复预算仍计费。状态或质量不匹配时，保留原 centroid、成熟校准或高精度，而不是把保序当成免费替换权。<!-- source-family:SF-2026-ARXIV-2603-17917 -->

静态注：`SF-2026-ARXIV-2603-17917` — Daily2026-03-20补03-19；[exact-v1](https://arxiv.org/html/2603.17917v1)§II–V/T1–5、必要B/C。仅fixedassignment的centroid扰动/跨层联合验收边界；不采rank-only充分、SiLU/RMSNorm affine-gauge或统计唯一归因。内部/vLLM分母分开，磁盘压缩非resident/服务加速；未核代码或复现。
