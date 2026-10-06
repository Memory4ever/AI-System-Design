# 2601.08893v1 — continuous-field architectural proposal, not a verified LLM replacement

[精确HTML](https://arxiv.org/html/2601.08893v1)，必要原段PRIMARY_08893_CORE.md。2+1+2=5，准入对象是field/wavelet/local operator+projection+score training的生成替代规范，不是physics命名或无benchmark的新模型排行。实际§4、§6.1–6.4、§7.1、§9.1、§11.7及B.5/B.8支持架构假设，未遍历无关物理证明。拟标准审阅完成/仅报告，待root实际原源核。

§4连续field经wavelet系数、local transport/viscosity/learned forcing及Helmholtz–Hodge projection，score training与可选physical correction；§7.1将x模糊容许token order/discourse coordinate/latent position，最终learned vocabulary projection，但没有可实例化text codec、模型配置、训练数据、参数、hardware、precision、sampling schedule或可比评价。§11.7明确大规模实测尚待进行，物理约束可能过度限制语言/creative novelty。divergence-free只约束所定义field；没有证据将该约束映射到真实语义守恒或hallucination suppression，未采用这两宣传命题。

§6.1 Eq17 dc=√2dW+sθdτ，同时Eq18 sθ≈∇logp；§6.4 Eq21 reverse drift写−sθ+∇logp，Eq22又写近似−sθ。在其Eq18同一定义下，Eq21两项接近抵消，不支持直接把Eq22当该近似采样recipe。此为当前采用边界，未据此声称全部替代架构不可能；无正面收缩/稳定/分布正确性保证采纳。B.5 learnedforcing只有local或指定globaloperator复杂度条件，B.8的O(NlogN)是单步且依赖scoreoperator成本，并非质量匹配、包含步数/codec/训练的end-to-end成本。不能把global transformer-like score自动写成一般O(NlogN)证明。

拟Books OnlyReport：具体可识别接口仍是proposal，缺text实例化与实测，且score映射未形成可执行一致配方；不改变当前长期模型/生成选择。无需把成熟projection/score原则再计durability或全部物理附录深算。精确重开条件：同版本可核text↔field codec和训练/采样配置、Eq17/18/21/22一致的time/score映射及质量匹配的任务与全链资源评价；到达时仅重开这些子命题，不默认revision diff。
