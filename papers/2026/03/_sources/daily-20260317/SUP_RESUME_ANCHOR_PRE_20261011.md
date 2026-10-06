# AnchorVLA4D12730：必要Source/actual owner与逐字PRE拟案

仅本17补03/16，完整AB/日级夹证/具名同稿去重复用。resume_mar17实际[exact-v1](https://arxiv.org/html/2603.12730v1) III-A–D/IV-A–B/V-A–D/TablesI–V/VI必要支持与反侧；官方abs只见v1、未显示具体纠错/撤回说明，轻查不证明全网没有。2+1+2=5，历史原图条件与当前belief分责的具体差额深入；未核artifact/复现。

## 支持与收窄

固定episode首帧I0与当前Ii同时进入VL，Any4D spatialencoder也读取两帧；冻结pretrained SE、训练后接dimension adaptation，再与VL最终hidden concat给ScaleDP400M动作head。Qwen2.5VL3B/BridgeV2预训练8Ascend910B64G30kstep/global512，finetune15k/global256；不是不经robot训练或额外rawgeometry sensor。SE来自图像prior而非独立几何真值；static I0也不是当前scene/derivedsummary。VI明确执行远离初态会使anchor成为过期bias，incremental refresh只是future remedy，未实测/实现。

Simpler四任务各24trial/120step，单A800，predict5/execute1。平均.185→.215s约16%额外延迟、4.65Hz；Vanilla broader table50采样step vs anchor10，不能授13.6pp单机制公平归因。TableII64.6→59.4差5.2pp非表写6.2；TableIII首帧55.2与主文60.4口径不一，仅保留各具体配置有限反侧。额外三帧stride1/20反退，SE放decoder前/动作head crossattention反退，不认证concat普遍最佳。retry overall1.54→1.40但failure1.66→1.68，不由次数证明early-retry时间或空间理解真值。proprio simulation40.6→51、实机drawer60→50，不能普遍移除状态。

xLeRobot三任务各30demo/10trial，三当前RGB+一anchor4图320×240，300ms、predict50/execute5≈17Hz不是观察或推理频率；pi0.5 execute50不同openloop条件、Bridge6D→jointspace7500额外步，不授零样本或80vs50单模块归因。作者写RTX4090Ti只是未核硬件标签，不回填已确认产品；precision/batch/concurrency/tailSLO、CI/seed未披露。有限原证支持历史输入接口，不支持无代价/安全或刷新有效保证。

## actual owner与逐字PRE

actual Ch26 535–575完整ActionMemoization空间对应→state ownership/freshness→think-gated derivedsummary→单调primitive：尚缺固定原I0与当前图像共同作为action条件、图像几何prior与staleanchor的分支。现267–280 action-facing latent中介不承载该时间身份；Ch25 598–635 environment/rawsensor/belief/prediction和Ch27采集交接保持。唯一MULTIMODAL-EMBODIED-VLA，拟在State ownership七条之后、think-gated memory之前；不重复拥有Ch25 dynamics或Ch77派生memory。以下需root/reader逐字PRE及窄授权，未写未POST：

保存历史并不只有派生summary或action cache两条路径。在短episode、初始布局仍有参考价值时，另一条受限分支把首帧原图与当前图像同时交给policy，图像几何encoder也读取这一对帧，再把其特征与当前VL表示接到action head。历史原图保留曾经看见的内容，却没有获得当前事实身份；冻结的几何encoder只是预训练prior，不是新depth/pose测量。episode、camera、首帧和当前帧timestamp与encoder revision应一起保存，不能因初态和当前图像被共同编码就称状态已经校准。<!-- source-family:SF-2026-ARXIV-2603-12730 -->

[AnchorVLA4D的有限对照](https://arxiv.org/html/2603.12730v1)支持比较这种固定历史条件，但更多近帧、改变特征注入位置或解冻几何encoder均可能反退；额外输入和encoder也增加平均推理延迟。执行离初态越远，旧anchor越可能把policy拉向已经失效的布局；论文提出逐步刷新，但本次不把未验证方案写成已解决freshness。预训练/微调、双帧编码、几何适配与闭环回归都付费，单次生成后执行多动作不是同频新观察。历史、坐标或deadline失配时，应保留current-only、经验证的近期窗口/可信几何与短horizon controller，不让有限成功率、重试减少或首帧来源替代真实outcome。<!-- source-family:SF-2026-ARXIV-2603-12730 -->
