# QUAD `2603.29535v1` — 必要标准 Source 与量化反侧

root 完整 AB 准入潜力已校准，拟 `2+2+2=6`。本作者实际完整读精确v1§3方法/§4部署评价/§5直接precision反侧，原件 [必要核心](SUP_QUAD_CORE_20261013.json)。未读别附件/代码，未复现；Source/day/Books仍待root，非终态候选授权。

## 方法与实际新增

固定graph不是每task merge/recompile：§3.2把各LoRA A/B作为input tensor，`Wx+αA(Bx)`，base常量图只编译一次，runtime bind buffer。编译器原本静态quantprofile不能随adapter分布随便变化；§3.3先用full-vs-quant输出divergence选择最敏感adapter的profile（同敏感fallback合并distribution），再把其它adapter放进这个profile的QuantSim，以各自fullprecision teacher输出和原taskloss distill，使其适配冻结profile。这里可采用的是adapter、graph、quantprofile与适配训练共同定义部署产物，不是任意新adapter不训练即可无损替换，也不是所有硬件都同一binary。ONNX→vendorIR/operator/placeholder/scale folding/runtime loader仍属各hardware适配。

重要原文不协调：§3称W/A/B shared scale/zero-point，但§5实际base INT8、LoRA INT16、activations INT16，跨dtype的literal同quant参数兼容条件未完整披露；Eq5将zero-point写成quant坐标，Eq6又在division前减它、Eq7重构亦不同标准affine定义。本次不照录这些式子为正确实现，只采用固定profile需逐adapter适配/回归的窄机制，具体encoder/dtype/shape/rank仍必须按实现验收。

## 可测范围与关键反側

§4真实ondevice为SD1.5类1.1B的promptguided transform/object removal两adapter，在Qualcomm/Exynos GS25、MediaTek TabS11；Table3另0.7B四usecases。采样器/step分别OLSS8、LCM或ED4，不合并成相同质量吞吐协议；LoRA ROM31–134MB、peakRAM约1.2–2.35GB，不将ROM节约当RAM节约。模型/image人口、resolution、repeats/uncertainty与切换基线细节未披露，不能授统计或生产SLO。

§4 FID5.5287是FP32-server与quantized-device的output比较，不是与真实图像population的quality guarantee；10adapter 15GB→2.6GB/6×仅示例估算，非实测10任务。1.5s end-to-end switching节约没有独立控制表/明确该hardware/热冷条件，本次不采用确切通用收益。

§5 Table4 prompt任务allW8A8 FID599.07、SSIM0.2324，对W8A16 FID12.23/SSIM0.9808，低activationprecision有大反退；90%W8A8也明显退。Table5 ObjectRemoval在TabS11 0→30%低bit时execute469→405ms、FID25.884→27.108、SSIM0.8064→0.7941，省ROM/执行仍付质量。更低LoRA precision和activation precision不是相同干预，保各人口/指标。共享profile不能自动消除adapter分布变化或精度质量风险。

## 待独核/owner

拟独核Source的必要命题是一个编译图外露adapter参数＋固定quantprofile需distill校准/回归，而非shared scale公式完整正确、6×RAM或任意新LoRA通用chipset零成本。日期用本日normal公告复合门及必要官方事件，不用created代理。Books尚未读现owner决定，不自动将graph/adapter已知原则作新增。
