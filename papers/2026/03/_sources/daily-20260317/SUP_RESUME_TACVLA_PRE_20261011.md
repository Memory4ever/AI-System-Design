# TacVLA12665：必要Source/actual owner与逐字PRE拟案

仅本17补03/16，已核完整AB/日级夹证/具名同稿去重复用。resume_mar17实际[exact-v1](https://arxiv.org/html/2603.12665v1) III-A–C、IV-A–E/TablesII–III、V与直接反側。拟2+1+2=5，具体contact-input接口与安全反側深入；未核artifact/复现。

## 必要机制/限制

15×8实测taxel→36tokensMLP/fixed2Dpos，sigLIP双camera+language/proprio及pi0.5 flow动作expert。contact检测超过压力阈值的taxel数量再过count门；固定token topology同时attention mask与embedding归零，不是变长删除tokens或只零embedding。二元threshold值/同步/延迟/mask实现未披露不补造；gating只输入参与不是controller安全。tactileencoder冻结，LoRA pi05_base10kstep；五task各50demo/10Hz，Franka/Panda每task20trials；DP200epoch/trainfromscratch与pretrainedVLA不等预算/因果。TableII 3DDP task2为0/20(40%)及8+0+9+0不合31.25%，不采用该比较数字；gating同底座消融83.75→71.25/70→40局部，Task3无gate60低纯vision65。不把平均成功/遮挡frontcamera涨幅或定性human恢复当安全或全部硬件故障。V二元heuristic/低分辨率/短horizon限制明确，hardwarecompute/precision/batch/concurrency/deadline ND；无CI/seed信息。

## actual owner/PRE

actualCh26 421–443：远端latent的新旧观测匹配→未来触觉forecast/current+futureprefix→joint生成；未承载当前实测contact决定固定prefix能否参与attention。actualCh23 1070–1080只承载tactileevent独立rate/calibration，非physicalpolicy参与gate；Ch25 rawsensor/estimate/forecast分责与Ch27数据生产交接保持。唯一MULTIMODAL-EMBODIED-VLA，拟remote-condition两段后、现未来触觉forecast两段前，不复制tokenizer详表。以下需reader/root正式PRE与窄授权，未写未POST：

触觉进入动作条件前，还应区分“传感器已有读数”和“当前接触使它值得参与融合”。持续拼接在固定任务中简单；另一条受限分支先按超过压力阈值的taxel数量提出二元contact flag，在保留固定token布局的同时关闭相应attention参与并归零embedding，接触后再开放当前触觉条件。它改变policy所读模态，不是预测未来触觉，也不是把未接触改写成未观察；threshold、sensor与时钟需要共同保存，contact flag不能签发夹持、碰撞或执行安全。<!-- source-family:SF-2026-ARXIV-2603-12665 -->

[TacVLA的局部消融](https://arxiv.org/html/2603.12665v1)说明持续注入触觉也可能在具体任务退步，按contact条件化可形成可比较的输入分支；有限短horizon和二元heuristic不授未知物体或全部遮挡鲁棒。固定token布局也不自动省去sensor、编码和模型计算，mask/同步、训练与实际闭环回归仍付费。压力漂移、漏触/假触或控制deadline失配时，应重观测、重校准，保留经验证的持续融合或vision/direct policy并交回独立controller，不让局部成功率替代真实反馈。<!-- source-family:SF-2026-ARXIV-2603-12665 -->
