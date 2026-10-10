# 2603.10985v1 Discrete Charm of the MLP：必要证据与中心跳过桥接争议

准备者 mar13_supplement；仅03-13既有日报的03-12 BJT补充自然日。沿用本轮完整重读AGENTS/Research/Report/Prompt/SourcesDaily/arxiv/ROADMAP和本日停点。只准备，不自授独核、formal或DAY，不写Books。

## 身份、日期与实际原件

[完整exact-v1题摘/history](./SUP_ABS3_10985.txt)：The Discrete Charm of the MLP: Binary Routing of Continuous Signals in Transformer Feed-Forward Layers，Peter Balogh，唯一显示v1、无Comments撤回/纠错/具名同稿先公开信号。相关Balogh2026a/b工作稿以不同题名作为前序引用，不把成熟线性化结论借作本稿新增贡献，不扩这些旧稿。

本次实际回[DATE3原件](./SUP_DATE3_10985.raw)：created/registered/updated Mar12T02:14:35，arxiv.content/findable，Submitted Mar11T17:14:57；与原独核§23正常公告批次夹证可复用Mar12日级。本Updated不是公开日依据，也不排除全网先稿。

[官方exact-v1 HTML](./SUP_CORE_10985.raw)、[请求](./SUP_CORE_10985_MANIFEST.json)/[结果](./SUP_CORE_10985_MANIFEST_RESULT.json)：https://arxiv.org/html/2603.10985v1，GET200225920 bytes，2026-10-10T04:02:07.918920Z。实际§1–5全部必要方法/解释、完整T1–8、§7限制/总结、AppA–C/T9–12直接人口反侧；§6仅相关已有机制边界。HTML段B号只作提取定位，不当页码。图1只读正文/caption，不读像素；没有代码、复现、其他模型重分析或旧版diff。

## 实际新增命题、评分及加深触发

旧FFN结构可讲activation选择但不能知道哪组实际token可安全省计算→所测GPT2-Small七default-ON/一exception及阈值分组，用整层MLP消融测不同组功能影响→需要分开二值可预测nonlinearity、内部神经元因果使用和真的可跳过。不是重新发明GELU或把Shannon/quorum比喻当机制。

拟 **2+1+2=5**：D2是由实际学得的coactivation/分组消融提出条件线性化/绕过选择的接口与适用边界；R1限FFN解释及同域局部负载，不借MoE/分布式quorum扩Reach；Durability2是预测proxy、功能干预和真实执行省成本应分别认证。中心“共识下noise→bypass有益”与其直接T7反侧冲突，深入受影响内容已经完成，不因争议/小模型降低投入或退EX。

## 有效支持及必要反侧

- §2 original GPT2-Small124M、12层/3072隐层、WikiText103 50K/500K tokens，50.4%词表覆盖不是模型全知识覆盖。先least-squares线性fit，再以残差norm划bottom25%/50–70%/top5%；阈值GELU>.1、按组firing差挑neuron，再probe。分组label是该fit残差，不是直接的“该token必须非线性”oracle。
- §3/T1–2/AppC：PCA、degree2–7与有限Ridge/五cluster处理的heldout拟合弱；L9最高.062而L11达到.262，paragraph-boundary cubic .45且.1%PPL方向内noise。有限投影/函数类不能排除所有平滑函数或数学上证明非平滑离散计算。GELU本身是平滑函数，严格piecewise-affine characterization针对piecewise-linear activation，不原样证明GELU的精确划分；本文§1.3又明确非理想binary gate/非formal Boolean，本次采用近二值描述而非强数学互斥。
- §4.2–4.4/T3–5/AppA：learned complement比独立marginal cofire少，但T4仍有8522–22756共同fire，不是hard IF/ELSE绝对互斥。1000random neuron split的exclusivity有220更强，gradient无随机匹配；random-weight control不存在该gradient，支持具体组合不是纯activation形状。bootstrap10000次CI是本500K token人口（相关token/文段独立性未充分规定），不认证跨语料/训练seed置信域。阈值.01–1变化仍有局部单调，但高阈值range缩小。
- §4.5–4.7：binary vscontinuous预测top25% nonlinearity准确率79.2/78.8，而连续预测norm R².36>.22；binary tree80.7对应baseline74.7，非完整路由oracle或无损丢掉连续信号。语义标签是posthoc top-token描述，§5.8明确未独立验证。L4–6没有consensus/显式gateway，L9–10无清晰quorum，不称全层都实现同样投票。
- **中心桥接断点§4.8–4.9/T7–8及§5.6**：整层MLP置零，0/7组PPL5.4→7.7(+43.3%)，7/7组39.5→43.5(+10.1%)，总体32.3→37.7(+16.9%)。相对损伤不同是有效功能分组观察，仍不能支持“full consensus无用/绕过有益”。T8 7/7正确词boost均值.85及rank+4.9，并不能替代T7的实际NLL；正文§4.9/5.6将这些平均proxy直接解释为noise、确认out-right bypass有益，至少与同稿明确报告的该分组PPL增加不协调。boost的精确平均/ratio口径未定义，**不从此指控两张表造假或重算整个实验**；只不采用从平均概率proxy到总损失收益的桥接。必须按同人口NLL和真实bypass策略验收，不能由“较小伤害”升级“无害/收益”。
- §4.9明示单独N2123 ablate或clamp无可测PPL影响<.1%，它是diagnostic而非causal；整层干预不能证明该neuron独自触发全计算或定位唯一内部算法。所有3072 dense神经元照常执行，§4.4明示fast path只是informational，不是硬件更快。没有已实现提前低成本gate/skip路线/端到端速度测试；先算完整activation再决定跳过没有免费计算保证。
- §5.8与AppB必要收紧：主文“larger不复制”实际附录用**相同index**2123及七consensus neuron IDs搬到不同模型，明确不同学得weights、未重新发现各自handler。因此只能说按index直接迁移失败，不能认定所有GPT2-Medium/Large没有此结构或capacity因果已证。Table11是Large Layer35，不混主文Layer11说法。跨GELU之外SwiGLU/GeGLU未测；无需追加全模型搜索才结束本单篇。
- 训练/推理hardware、precision、上下文窗口/序列采样、完整probe选择/费用、真实skip内核与跨域/旁侧质量在必要原段Not Disclosed；token规模/局部CI不代全预算或SLO。Shannon、quorum、MoE比喻与已有ReLU/spline结果分开。

## actual唯一owner与处置

ROADMAP `MODEL-FFN` [Ch16](../../../../../books/part-02-model/16-feed-forward-mlp.md)实际顺读开头1–165逐位置FFN/activation、165–230 dense计算/gating/替换代理完整局部及MLP知识解释/相邻Ch17开头残差责任。现文把activation条件选择与实际dense FLOPs分开，神经元语义/读出与因果使用分开，并要求原层/投影/代理/删层对照；没有本稿的consensus实验证据，不能签“新实验已吸收”。

拟**争议/暂缓Books0**，不是主题NC。保留coactivation/独立与随机控制、局部分组消融及binary/continuous差异；隔离“full-consensus无用所以bypass有益”、所有平滑函数失败、普遍binary必要/规模无consensus及免费skip。理论/收益中心桥接尚不适合作正面长期证据，不以一般原则造两段书稿。重开只需同人口NLL与boost口径、真实条件线性化/bypass策略的质量/成本或明确收窄更正；若要跨模型推广另需各模型重新发现而非按index转移。当前实际支持与直接反侧已足，普通余项继续，不要求代码/全图/附加复现作为本窗单篇结束前提。
