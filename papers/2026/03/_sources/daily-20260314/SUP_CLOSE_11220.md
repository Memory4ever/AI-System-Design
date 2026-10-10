# 11220 FMVR：实际新增命题最低评分/关闭提案

mar14_supplement。完整题摘已root准入校准，当前[精确v1](https://arxiv.org/html/2603.11220v1)原件`SUP_NECESSARY_11220.raw`；实际只读§3.1–3.3/Eq1–7与完整题摘/身份/当前说明，得到评分所需实际delta即停止，不把HTML200当标准全文审阅。UTC/status见`SUP_NEXT_SOURCE_MANIFEST_RESULT.json`。三作者、仅v1、Comments无具体纠错/修订或具名先稿信号；日期官方Mar13上下界由`SUP_DATE_11220.raw`/`SUP_DATE_SECOND.md`，v1Wed18:33:52UTC明确晚截止，registered同日owning/findable，不单用submitted或注册作first-public。代码仅will be open，不声称已核artifact。

实际增量：继承MRL共同训练多个token尺度（CLIP24×24→12/6/3/1），在每2×2压缩处加入两个局部pooling-residual unit；AvgPool支取X−AP(X)、MaxPool支取X−MP(X)，channel-wise learned weights与residual×X项相加，两支求和。Frequency/saliency/anti-saliency是作者对局部特征的解释，不是删除内容已被事实恢复的证明，没有引入新token可变尺度原理、输入证据或独立信号。

最低评分拟 **1+1+2=4，已关闭/仅报告**：Design Delta1只计压缩处局部learned residual配置，不把继承MRL或常见pooling/attention概念加分；Reach1仅视觉压缩组件，不把LMM话题或联想inference整层当跨系统变化；Durability2为有限预算下训练压缩特征的可复用工程选择。仍保留其准入窄贡献，不因耗时或Books已有覆盖撤销筛选，也不以多个benchmark/89%摘要数字倒推重要设计变化。

不进一步采用的具体理由：当前新增命题是模块配置/特征调制，没有已识别改变token压缩长期有效性条件、quality/资源可行界或模型/系统解释的证据；所谓细节恢复未提供独立内容/事实验证，故不把“每个小模块若成立”都写入Books。具体正文gap/纠错/安全变化等强制深入未触发。摘要少token平均accuracy不是逐任务无损或生产TCO，核心读过的可学saliency maps也不认证视觉因果；未读取全表/benchmark/附录，不能声称标准评价或论文全结论已验证。

root可实际核Eq2–7必要局部和身份/date后裁决评分/关闭。若后续有独立信息恢复或新的预算可行性边界证据，只重开那项命题；当前不展开全十任务/PDF、不造owner gap，无Books写入。
