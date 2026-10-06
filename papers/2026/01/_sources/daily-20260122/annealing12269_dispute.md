# 12269 精确v1中心公式争议

实际原源：https://arxiv.org/html/2601.12269v1 Methods Eq6，原返回[standard_ready3](./standard_ready3.txt) L3。作者与root均定点实际确认：x是current、x′是proposal，但印刷比为 target(current)q(proposal|current) / target(proposal)q(current|proposal)，是标准MH接受比的倒数，非本地抽取错误。不能替作者静默改公式，也不据此猜代码实现。

原文随后明确annealing samples不来自fixed target posterior。exact-power-sampler保证及该公式支持的正确目标分布为本窗中心争议终态保留项，不作正面证据、不Books；取得对应精确版本勘误/实现确认及相应目标分布证据时，仅重开此命题。已读取支持+直接反侧足够，不扩代码考古/完整proof。

独立可采用的范围仅是具体退火schedule接口及作者有限BigToM观察，仍绑定额外MCMC预算/小模型/合成任务。准确率或个别推理例子不证明真实mental-state representation，也不作为中心数学保证的替代证据。
