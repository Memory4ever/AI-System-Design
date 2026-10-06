# 10583v1：LIDA最低实际增量及出处资格

仅03-13新增Mar12 BJT。完整题名/四作者/AB/To appear CVPR2026已实际读本日 `SUP_ABS3_10583.txt`；准入主独核§第三包窄P和DATE3 §23含本ID的Mar12 arxiv事件夹证复用。Accepted/To appear未指具名dated早全文，当前无需全网无早稿证明，不从注册/提交单字段授日期。无撤回/更正说明，本包不重读其他日期。

exact-v1 https://arxiv.org/html/2603.10583v1 GET200/410523bytes，`SUP_HANDOFF7_SOURCE_10583.raw/txt` / `SUP_HANDOFF7_FETCH_RESULT.json`。实际§3–4/Eq1–8（285–858）、§5.1核心人口/T1必要正反行（859–1060）、implementation1793–1815、§5.3–5.4/Table5及必要反侧（2071–2275）、§5.5直接patch实现与结论（2953–3005）。不遍历全9tables、所有visualization/附录、代码或先前模型历史。

actual新配置是有label的registered exemplar bank、低三bit plane继承阈值操作、改ResNet50取消早downsample、pretrain后center-loss/real-prototype contrastive适配，再按nearest exemplar的generator label归属。Lowbit检测输入、center loss与contrastive本身已有文献，retrieval与维护bank也不由名字升级为新长期原理；本稿局部价值是具体搭配在所测generator人口上的区别与快速注册配置。

注册新generator需要一/少数**已知source label的样本**加入bank；few-shot实际还100epoch适配，不是任意未注册generator被自动恢复来源。§4.2“unsupervised”pretrain实际用ImageNet category pretext；Eq4下文q/s label与predicted probabilities的说明和通常CE顺序有披露歧义，不猜代码或据此判实验全错。先binary real/fake、再known registered generator retrieval是两个资格；zero-shot表5只是与real prototype/.85手选门槛的real/fake判别，不是zero-shot精确generator归属、校准FPR或签名证明。

必要反侧：T1一shot整体Rank1/mAP改善，但SDV5 Rank1 1.5低于ResNet9.5及DIRE15.1；不授每generator支配。Table5总体86.3的zero-shot detection仍在Wuk/SDV4/SDV5/GLIDE等列低于某基线，不合成全population无误判。λ=.9最佳，继续加大会伤害fake之间区分；Gaussian blur改变lowbit分布，JPEG95–85的局部稳健性不签强重编码/生成编辑。原GenImage/WildFake固定train/test/exemplar抽样不是真实开放generator全生命周期认证。

实现/费用：RTX4090/Ubuntu22.04/PyTorch2.0.1，1/5/10shot bank、batch32、100epoch；既有大pretrain非免费。§5.5实际32×32patch，对query每patch与bank所有image所有patch比较、最高score patch再送encoder；规模增长的检索/更新成本不能从ResNet轻量或binary操作转为常量端到端速度。正文millisecond没有完整database规模/SLO/p95计量，不认证生产服务时限。Retrieved neighbors解释相似性，不证明legal origin、所有权或伪造不可行。

拟 **1+1+2=4 / 已关闭 / 仅报告Books新写0**：实际lowbit/encoder/loss/注册检索的局部实现配置(1)、受测单forensic模块population(1)、可复用注册与代理边界但本稿没有建立新的普适不变量(2)。保持原P，不因图像forensics领域排除、不强做已有覆盖NC/PRE，不把成熟principles或bank能映射Ch72算新机制分。具体理由已支持最低处置，后续不扩全量tests/附件。待非准备者实际源/评分独核与root采用，不授DAY。
