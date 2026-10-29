# SeGP-CL：必要Source / actual owner差额与PRE提案

mar14_supplement准备，仅03-14补Mar13 BJT。root11题摘及七exact-v1身份/日级日期已独核复用；current latestv3不倒灌首稿。SUP_SOURCE_REM11_12055.raw精确v1 GET200435270B/2026-10-10T03:22:50.971591Z；完整AB及必要§III-A–E B41–117/Eq1–32实际读，必要§IV/TablesI–VI B118–223包含直接反侧/成本实际读，不宣称全部Fig像素/附录/代码复现。

准入→命题：没有旧images时新数据distillation可不覆盖旧新semantic边界→frozen上一task双tower以旧text和旧raw prototype双目标PGD制造新image局部anchors，分别保cross-modal分布与reset-LoRA文本参考，再用同anchor估raw漂移移旧prototype→选择保留接口不只保护参数，还要区分训练reference和部署readout的更新身份。**拟2+1+2=5标准；具体持续训练state/readout接口gap触发必要定点深入。** Design2只计exemplar-free边界anchors与两reference/旧readout递推这一具体替代接口；不借PGD/KL/LoRA/KNN成熟原则、5benchmarks或SOTA加分。Reach1限VLM-CIL训练/readout组件，Durability2为受限可复用保持接口。不是直接证明全部旧功能/全部模态几何不变。

## 实际机制与关键反侧

任务类不交叠，train仅newclasses。冻结上一task teacher(Ft-1,Gt-1)，按该teacher对old-text相似度从新image为每oldclass选5seed；Eq13文本旧类softmax目标与raw视觉旧prototype余弦距离联合、10步Linf PGD。raw空间与投影CLIP空间分开，不把projection后的语义相似当真实旧image。用anchors蒸馏teacher/student旧类分布(Eq18)，student视觉与text两tower LoRA只训B、A冻结。TSGR却以reset-LoRA的预训练G0作另一teacher，新类root选seenclasses中的10neighbors、只在固定该neighbor-set配KL；不是跟Gt-1漂移同步，非全seen geometry硬等价。

训后保存oldprototype state，用相同anchor在前/后rawencoder的差估位移，proximity-weight/gain后归一旧prototype，newclasses由本taskimages计算；deploy用CLIP logit加beta .5 raw-prototype logit。readout漂移估计是teacher诱导proxy，不恢复旧数据，也不自动证明旧原型真实位移；Eq26 cosine权重分母/符号须数值有效，未另读代码不补造clip/softmax为safe recipe。anchor错误、旧语义遗漏或负/零权重不稳定时保旧prototype、旧encoder/真实replay与独立retain评价。

TableIII同两tower backbone上new-dataCGD -0.8Avg/-0.5Last，而5seed与5adversarialanchors +1.2/+3.1和+3.3/+5.8，支持监督人口选择有局部差别，不认证合成anchor是真旧人口。TableIV raw视觉branch提高Last同时Forget从CIFAR4.3到4.5/UCF6.3到6.8，TSGR对UCF88.2→88.0/F6.6→6.9，不授每component都改善。TableVFood84.5低于zero-shot85.1，old task仅tested classes/域，不保全部zero-shot能力；TableII FWT定义是未来taskimage在global全class set的准确率而非扣base的标准gain，不混协议。

成本：2RTX4090、10epochs/task、batch128、rank32 K,V+FFN3.44M、424ms/iter(+79 over其baseline)与MG-CLIP rank32 2.02M/343ms不是同trainable预算；anchors搜索、oldteacherforward、两KL及prototype移位都计费。TSGR new-root |Cnew|k只是每步selected关系数，不等KNN构图/O(allseen)或全system成本消失。§IV-D说明更多PGDiteration可反退，近prototype不自动更好；不拿未目视Fig幅度作定量证据。不签生产SLO或通用免遗忘。

## 实际owner差额 / 两段逐字PRE

已实际顺读TRAIN-SFT Ch29 910–949：trainable-subspace identity→rotation/safety/dynamic-mask→historical realanchors gradient/virtual softprompt gradient分支连续局部，并读Ch28/30入口；Ch23 mapped-space与current continual-projector只是表示/消费者交接。现Ch29真实anchors分支保护更新方向、syntheticsoftprompt分支保护局部gradient；没有上一task双tower与reset-LoRA text两份reference的职责分离，也没有同syntheticanchors以before/after raw位移迁移oldprototype的部署readoutstate接口。拟唯一ownerTRAIN-SFT，放Trainable Subspace末段后/Rotation-preserving前，新独立小标题和两段；不改现mask/rotation段，不在Ch23重复写。无共享Books写授权，待root实际Source/PRE独核与窄写。

### 逐字提案

#### 无旧图像时，保持监督与旧读出须保存不同参考

持续适配双塔模型时，只在新图像上蒸馏旧类分数最省事，却可能没有探测到旧新语义交界。一条无旧图像的受限分支冻结上一任务的视觉与文本编码器，从新图像中为每个旧类选择接近旧文本语义的种子，再以旧文本目标和已保存的原始视觉原型共同约束小扰动；这些 anchors 是旧 teacher 诱导的边界探针，不是恢复出来的旧样本，旧类文本和原型仍是历史 memory。训练在它们上保持旧类图文分布，同时另用撤去 LoRA 的预训练文本参考固定新类根节点的近邻关系；上一任务的模型快照与预训练的文本坐标因此是两份不同 state，本任务训练期间不能随着当前 student 一起漂移，也不由较小 KL 宣告全空间几何或旧能力不变。<!-- source-family:SF-2026-ARXIV-2603-12055 -->

训练后的部署读出还要接受同样的漂移检查：用相同探针在更新前后原始视觉空间的位移估计，提议迁移旧类原型，再把原型分数与图文匹配分数组合；它不等于真实旧类均值位移，也不授每个原型都被正确恢复。[受限 CLIP 类增量对照](https://arxiv.org/html/2603.12055v1)中，新数据上的直接蒸馏会退步，目标化探针局部较好，但加入视觉分支可同时提高准确率与增加遗忘，某些零样本域仍低于原 CLIP。探针搜索、冻结 teacher 前向、两份参考、原型更新与回归都付费；近邻覆盖、权重分母或漂移估计不稳时保留旧原型、原 encoder、真实 replay 或独立 adapter，并以目标和 retain 切片分别验收，不把 synthetic 监督与小 KL 当作无遗忘证书。
