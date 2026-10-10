# 10695 RandMark：独立必要 Source / 统计桥接争议复核

复核者：mar13_admission_review（非准备者），2026-10-10。仅 03-13 补充窗口 2026-03-12，北京时间完整自然日。

## 上下文、身份与实际投入

已重新读取 AGENTS、当前 Research / Report / Prompt、Sources 使用说明与 Daily / arXiv 分组、ROADMAP、本日 LEARNING_STATE 路由和 README 停点，不加载其他日期候选。本 ID 既有完整题摘准入与日级日期夹证有效复用；不把 submitted 当 public，不搬原候选、评分、窗口或 §4 前缀。

先读 [准备者证据包](./SUP_EVIDENCE_10695.md)，再直接解析 [精确 v1 官方 HTML 原件](./SUP_CORE_10695.raw) 的 §3.1–3.5：统计定义、Eq1–32、Lemma1 的明确独立性假设及必要 proof；实际读 §4、§5 完整主 Tables1–2 / 直接反侧 / 两图 caption 与作者解释、§6。MathML alttext 直接保留原式，不以准备者摘要代原证。没有展开旧水印论文、Supplementary、代码、图像像素或全版本比较；原核心支持和中心桥接争议已足够。

[响应 manifest](./SUP_CORE_10695_MANIFEST_RESULT.json) 为 `https://arxiv.org/html/2603.10695v1`，GET200 / 251794 bytes，UTC2026-10-10T02:43:13.441955+00:00。实际 [本日 ABS 原件](./SUP_ABS3_10695.raw) 的完整题摘、具名作者与 history 匹配 *RandMark: On Random Watermarking of Visual Foundation Models*、Anna Chistyakova / Mikhail Pautov；可见唯一 v1，无显示的 venue / withdrawal / correction 说明。这不是全网无早稿或全历史无勘误证明。

## 增量与评分

Classifier-output 水印不自动适用于下游 head 改变的 VFM → 本稿共同训练 source VFM 与辅助 encoder/decoder，用秘密图像的随机变换和 decoded bit 统计检测 functional copy → 需要分开位、图像/变换和模型总体的随机单位及其低误报资格。

**2+1+2=5 合理**：Design Delta 2 计表示适配后的随机检测接口及所声称概率适用边界，Reach1 是局部检测组件，Durability2 是统计单位/相关性/变换约束的可复用条件。不把版权、法律、CLIP+DINO 的模型个数、成熟 Chernoff 或 Hoeffding 身份计作额外贡献。中心资格冲突触发受影响内容必要深入，保持候选与评分，不因暂缓或花费降分关闭。

## 原协议实际可描述的范围

Eq2 联合表示保持损失与 K 次 decoded message 的距离；Eq3/4 实际测平均 **Hamming errors** 与其样本方差，尽管邻句称 matching bits。Eq6 的每图判定是 `rho=(1/K) sum_j sum_i 1[mi!=m'ji] <= tau`，Eq7 为 N 张秘密图像 pass indicator 的归一化平均。随机性来自图像 Gaussian 变换、decoder 表示及所抽模型，不能不加说明合成一个 bit accuracy。

接口文字亦有必要限制：§3.1 将 e 输出声明为 R^k，Eq2 又把其交给输入 R^s 的 VFM；Eq1 把 R^k 的 w 与 n-bit decoder 输出作差，概率阈值 γ1≪γ2 本身也不编码强正/负分离。只记录精确版本未给足的路径/类型条件，不猜唯一可执行实现，不由这些披露疑问否定有限实验已经得到的数字。二值输出如何用于连续训练、取整/梯度具体过程未披露，不声称 artifact 或训练复现已验。

## 中心概率桥接：独立校准

### 相同边际不足以得到 Eq8 的 binomial tail

Eq8 前只写所有位具有相同 match 边际 r，没有给出同一次 decoded message 各位相互独立。取 n=32，固定秘密 message，令所有 match indicators 等于同一公平 Bernoulli Z；全部 match 或全部 wrong 各半。它满足 **Eq8 明写的 equal-marginal 条件** r=.5，error count 是 0 或32；对 tau5，pass 概率 .5，非 binomial tail。

这是统计假设的反例，不是检测攻击、真实独立 VFM 的已实现构造，也不声称实际训练位完全相关、真实 FPR=.5。它不满足 §3.5 的明确独立 Bernoulli 假设，**不能拿它去否定那个条件化集中界**。需要补足的只是 Eq8 从位边际到整条消息事件所需的独立性或可替代相关界。

Eq8 左边写 `rho<tau`，求和却包含 j=tau；实际 Eq6 用 <=。本项不静默统一边界，但该一位差异不消除上面的相关性或统计单位问题。K 次变换平均 error 也不是未经桥接就等于一条 n-bit 消息的计数分布。

### 即便独立位，bit-r 也不是 Eq14 的每图参数

Eq11 明确定义 bit collision 概率 r，Eq14 却把每图 `1[rho<=tau]` 的 Bernoulli 参数直接写成 r。这缺少 bit→image-pass 映射，不只独立性疑问：在合法特例 K=1、n32、每位 IID 公平 match 下，r=.5，而按 Eq6 tau5 的每图 pass 概率为

```text
q = sum(j=0..5) C(32,j) * 2^(-32)
  = 0.00005653710104525089 != 0.5.
```

该数由原检测定义独立计算，不来自额外实验；K=1 是公式未排除的特例，不声称本文实测 K=1。即便另满足跨图独立，也不能将 bit-r 代入对应图像事件的 Poisson-binomial 参数。多图固定同一 suspect model，又会共享模型层面的变化；独立图像/变换不能自行给出 **模型抽样总体上的** pass-event 条件独立性。Eq14 可作为额外独立计数模型讨论，但必须说明实际协议为何满足，不能称其原条件下所有计数定理都错。

### Rate / count 与条件化集中界保留

Eq7 R∈[0,1]，§3.4 Remark1 却用 Rbar750 / Runder600；§3.5 转为未归一化 sum，并把 N 项改记为 n 项，而 n 前文是消息长度32。可明确重定义为图像 pass 计数后再作理论分析，但本复核不替作者自动修复人口、计数和阈值，也不将 Remark 的 10^-6 / 10^-4 宣传授给实测总体。

§3.5 真的显式假设 xi/eta 独立，且阈值分处真实均值两侧；在这些条件下，Chernoff 乘积、Jensen 凹性和 Hoeffding 步骤可保留。末步 Eq32 另须 `p_hat-epsilon>d/n`；单有真实 pbar>d/n 不保证每次估计落在该域。域外需要保守上界或清楚分支，置信端点也须位于有效概率区间；不能把缺少这些条件写成无条件低 FN/FP，也不凭此全盘否定成熟集中界。

## 完整主表与直接经验反侧

§4 使用公开 CLIP / DINOv2，ImageNet N1000 秘密图，每图随机32-bit；所列 E-commerce18175/9类、FoodSeg1037118/100余类。正文称三个 domain datasets，项目列表仅两类、后文另有 ImageNet classification head，不静默合并人口。全部 VFM 层下游 AdamW10 epochs，unstructured l1 pruning20/40% 明确只是修改 baseline，不代表已覆盖有意移除、蒸馏/抽取或未知 adaptive attacks。

**Table1 全表**：CLIP segmentation fine-tune1/3/5 epoch，RandMark segmentation / WM 为 .32/1、.52/.99、.55/.97；randomized smoothing 为 .14/.27、.36/0、.46/0。有限 matched epoch 支持局部 task adaptability / watermark extraction 的取舍，不证明与 clean unwatermarked VFM 的效用无损，也不承诺所有下游任务保真。

**Table2 全表**：DINOv2 positive 的 classification .870、segmentation .750、pruning20/40% 均1；negative DINOv2-registers 与 CLIP 为0。它报告 Eq7 **按秘密图像平均的检出率**：可说相应协议有13%/25%图像未 pass，不能说已测模型人口 FN 概率13%/25%。pruning20% 与 ADV-TRA 同1，也不是全部场景严格领先；有限两个 negative 配置的0不能认证未知模型总体零误报或 Remark 的概率界。

Fig2 caption 指平均同1000张用于水印的图，不改称未参与注入的独立 secret-image holdout；Fig3 只读 caption/作者 covariance 解释，不从近0的有限 covariance 判断推出全部位或跨图独立。分类 head 的 CLS+patch mean / norm / dropout / linear、ImageNet 训练与 VFM 表示方案有接口差异，不能只归因于随机水印机制。经验结果保留对应模型/变换/阈值与人口，不因理论桥接或排版问题全部删除。

主要训练/检测的实际 tau、sigma、K、lambda、auxiliary architecture、完整训练预算、硬件/precision、seed/CI、全 query 成本、功耗和 SLO 未披露；Remark 的示例 tau5 不冒充主表全部操作点。Supplementary 成本只是引用而未在本次取得，不为已能限定的局部描述造永久受阻。联合训练、秘密图/bit 留存、K 次变换、多图 model queries、decoder 与独立下游效用验收全部有费用；不授法律所有权、防复制或防泄漏保证。

## 实际 owner 与终态

实际顺读 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 当前187–222的模型泄漏 / 水印、门限 shares / null 校准、逐 client 验证、组件 lifecycle、soundness 与 unforgeability、行为取证完整有关局部（分段恢复输出），并读 Ch71/73 入口。唯一 owner 为 PLATFORM-SECURITY；统计评价只能交接，不另造平行 owner。

現正文明确有限 null / query / 模型人口不能推出任意模型固定误报，取证不等防泄漏或法律责任，发行/变换/detector 身份和独立取证回退应分责。**没有吸收本稿随机表示接口、主表数字或新概率证明**；故不以主题接近签 NC，也不把尚未成立的统计保证作为已确认长期知识缺口写入。

**独立裁决：5分，必要受影响内容深入完成；中心统计桥接争议 / 暂缓，Books0。通过的是有界机制描述、局部经验结果与隔离处置，不是强低 FP/FN 定理。** 不是贡献 EX、低分关闭或所有实验无效。原候选和投入保留；没有 Book PRE / 修改 / POST，不授 DAY。

精确重开条件：提供一致 encoder–VFM–decoder 类型/取整规则，明确 bit / K-transform / image-pass / model-population 的随机单位及其映射，相关性或条件独立性原证、rate/count 与阈值统一，以及适用于实际操作点的有效置信端点/域外界和费用/效用人口。届时只重开 Eq6–16 / Eq17–32 与相应主表，不扩旧水印证明或完整版本史。本有限单项到此停止；只新增本独核文件，不改共享 Report / Books / State / mainledger。
