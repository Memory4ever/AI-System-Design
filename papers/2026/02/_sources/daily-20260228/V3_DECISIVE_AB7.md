# AB7六项含糊准入：一次决定性原v1检查

仅六个已具名、准入事实尚含糊项；完整原v1题摘已实际读，精确HTML必要core与直接对照如下。获取见V3_FETCH_AB7_ONCE.json（2026-10-05T19:35:08～10Z），每项abs-v1/HTML-v1/current-abs均200；当前官方comments仅22745 project page，未见撤回说明，不声称完整版本历史已审。不扩发现范围，不把这些一次准入核写成完整Evidence/Books Gate；root裁决后，仅明确IN继续必要方法/控制/边界和实际owner。

## 22683 SuperGlasses/SuperLens：拟窄IN5，不按新benchmark或agent组合准入

原31–38/48–55/140–146。已有对象检测+query拆分+web RAG/cache/rerank是成熟组合；本次值得保留的是Table4的**对象/文本同样可检索不等所有query都该强制检索**控制：Qwen7B direct32.82，mandatory双路且有detector/decoupler32.04，mandatory缺两者16.45，而adaptive双路44.10；同adaptive下去detector/decoupler、forced分支对应反侧可修正“接检索即增能力”判断。141–145错误modality选择/未定位作者实体的失败链进一步说明局部object identity必须先于外部lookup，retriever正确不补错误query identity。准入是这个受限条件与消融，不是smart-glasses排行榜或声称首个；需后续绑定evaluator/route成本，不授全agent因果或生产收益。

## 22698 KGT：拟成熟组合EX，请root一次裁决

原5–11/22–55/69–76。实体/关系注册special tokens、预训练sentence/TuckER embeddings、投影+relation temperature/noisy softmax gate、两独立MLP head/LoRA score与learnable logit mixture改变KGC接口，但新增部件均是已知special-token/embedding warm start/mixture/untied output原则。69/71确有dual-head/feature/ICL对照，说明此KGC配方受益而非没有实验；然而未给超出这一配方、改变foundation表示取舍的新的有效性条件/失效反证。不能仅“granularity mismatch”“full-space”或MRR声称长期增量；也不把训练效率/无需candidate filtering包装成新authority机制。若root认为**input知识注入不足、必须协调output映射**的直接control确实新增独立条件，只重开这一具体理由，不要求全文/全部proof。

## 22703 GeoDPO：拟窄IN5，translator与oracle权限界面

原53–63/67–81。直接GeoDSL SFT受permutation-equivalent programs序列监督干扰；保持NL输出，由独立NL→DSL translator转成可检查元素/约束，再与生成器已知G_true评分形成DPO pair。这与泛称DSL+RL组合不同，实际改变**格式同构的监督目标与perception-vs-reasoning分账**。Translator7B LoRA rank4/3epochs/4H800、validity100但circlesF1随复杂度85.1→65.9，说明语法valid不等reward语义oracle。DPO/SFT同rank8/1epoch/4H800，但DPO额外10samples与translator准备成本，不能称等总预算；Table3/4有类别负侧，OOD只有100 diagrams，MathVista203subset不是普遍几何智能。继续必要指标/生成器验证边界与Ch23/66具体owner，未授所有DSL truth或通用OOD定律。

## 22733 Pixel2Catch：拟窄IN5，受控sim→real反侧，不按catch场景/MA组合准入

原21–23/31–53/88–99。pixel中心+尺度差分、SAM2、MAPPO arm/hand分责本身均成熟。决定性增量是real TableIII（每object30throws）**only-center虽sim强，real保持抓取只13/3/23%，只有width-height则0**；full center+scale63/43/43，single shared-policy33/20/20。tracking和稳定grasp并非同一success，real deform/aerodynamics与sim randomization错配是明确边界；改变是否可从模拟tracking胜出选择视觉接口/共享控制的判断，而非通用MA更好。UR5e/Allegro/D435 RGB、30Hz/120Hz sim、zero real finetune所测条件；不授只凭pixel就有3D真实位置或安全catch保证。后续只必要observation/reward/population控制及具体Ch26 owner。

## 22742 ProjFlow：拟窄IN5，线性可行与生成自然度分离

原44–65/115–119。给定线性A、R≻0、Gaussian observation covariance，以R^-1 A^T(AR^-1A^T+Sigma)^-1修正clean endpoint；R为kinematic graph Laplacian+lambdaI，couples邻接关节而非Euclidean逐坐标最小改动。Table3**所有variant线性约束误差同为0，Euclidean/no-noise/plainmasking FID1.152/3.429/.880而full .097**，证明exact observation并不决定naturalness；采用此质量条件不是所有动作安全。Topology metric+stochastic recomposition/pseudo-observation的局部控制有效性足准入；不把已知closed-form projection本身算新机制。119明确不能原生表达nonlinear条件；其“joint above plane”例是inequality、并不因此变非线性等式，保其支持范围只线性equalities，不把不支持不等式改成所有线性约束可处理。后续必要sampling/noise/timing与owner，不遍历全MAP proof。

## 22745 SpatialAlign：拟窄IN5，reward proxy失配与reference anchor

原50–64/81–96。DSR geometric score vs VLM评价不是仅空间任务分数更高：58–64 VLM对低geometry score仍大量YES；86改用两VLM reward竟坏于unfinetuned，是明确reward blindspot。51–57 pureDPO可通过winner/loser一起降而满足margin，SFT noise-target anchor虽稳却过饱和，reference-noise一致性anchor与其区别是局部新controlled条件。800steps/500trainprompts/30testprompts有限ablation，threshold.8更准确但CLIP-IQA natural更坏，不能采零阶regularizer硬防reward hacking/完整身份质量保持。96 detector/tracker在blur/复杂scene会给错/invalid reward，only oneanimal+oneobject/LEFT-RIGHT-TOP；几何oracle也是proxy不是世界truth。继续必要score定义/control与Ch24/34实际owner，不看alltheory作为准入义务。

目前只拟五IN/一EX，root独立准入尚未授，不计safe、不冻结日级分母。

后续必要方法/控制/owner已整理第十二包。22703等长constraint score有重复交叉项而不具顺序对称，22745 DSR声称0–1范围与可实现端点/gap不相容；均只隔离受影响子式/保证，不自动全项D。22733 zero real finetune不等未使用real system identification，22742 hard constraint普通inverse须合法row-rank/可行条件，均已收窄采用范围。
