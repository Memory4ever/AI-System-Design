# RVV/xDSL2603.17800：本20最小必要Source与PRE准备

准备者resume_review17_18，仅本03-20补03-19自然日，原1+2+2=5/date及准入复用独核§30。此处不是自身Source/PRE PASS或I/DAY；author非准备者裁后root协调窄锁。未写Books/Report/LS。

## 1. 原证与实际停止范围

[Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings exact-v1](https://arxiv.org/html/2603.17800v1)。actual current [abs](https://arxiv.org/abs/2603.17800) L8–29同题三作者、完整AB、Comments12pages/11figures/1table、单v1无具名纠错或withdrawal；Submitted03/18不作firstpublic。既有日级夹证和贡献评分保持，不重开版本史/新query。

actual必要读取：§2.1 L74–105只是packed GEMM接口背景，§4.1–4.3 L122–360包括论文展示的IR/生成C片段，§5.1–5.2/Table1 L361–398，§6 L399–404直接范围/后续限制。没有读所有references、外部repo/代码、完整toolkit发行史、图像像素或跑实现；嵌入正文的代码片段是paper证据，不冒artifact核验。

## 2. 支持的具体接口

- 原Goto/BLIS-style outer宏循环及packing继续存在；核心更新packed A/B上的小C tile。本文自动生成的是可替换micro-kernel，不是BERT整体编译器、整个GEMM自动packing或一套Serving引擎。
- §4.1作者在LLVM22.0观察arith→emitc可用而dynamic-array memref→emitc不完整；这支持该精确环境的缺段，不能泛化今天全部MLIR、任意dialect/ABI都缺失或这套pass自动正确。
- 用户先指定mr×nr、dtype与目标vlen，xDSL生成scf/memref/arith和自定义rvv混合IR。展示FMA接口包含C accumulator、packed B pointer/offset、A vector和vector-length bound，SSA iter_args/yield保持跨k循环累积。
- MemRefToEmitC在该packed-memory约定内改成C指针；SCFToEmitC把SSA loop-carried state变成mutable variables/assignment；RVVToEmitC把typed rvv operation改成opaque target type和RVV intrinsic call，其中B memref+offset先得到scalar，最终FMA从五个IR输入变成四个C intrinsic参数。然后仍使用官方mlir-translate输出C/C++，native g++编译到目标板，并生成harness/Makefile、部署/测量。
- 因而可分采的增量是**缺失lowering段的显式memory/control/vector ABI责任与已有C工具链/宏kernel共存**，不是泛泛“typed IR可验证”成熟原则。默认memref可描述复杂stride/布局，不等flatten任意memref都正确；源码仅给此GEMM路径，没有足够证据授全部alias、任意rank/layout或任意RVV指令转换。

## 3. 关键对照、资源边界与直接反侧

§5真实两板：K230仅RVV-capable C908单核1.6GHz/RVV1.0/vlen128/L1D32KB/L2256KB；BananaPi F3的SpaceMiT K1同1.6GHz、每核L1D32KB/四核簇共享L2512KB/vlen256，虽有八核实验仍单核。环境Python3.13.9/xDSL0.54.3/LLVM22.0/g++14，flags `-march=rv64gcvzfh -mabi=lp64d`；比较OpenBLAS0.3.31各目标RISCV64_ZVL128B/256B。FP32 micro-kernel1500次、GEMM200次平均，未给不确定性/CI、完整浮点误差容差/验证人口与搜索总预算。

性能人口分三层，不合并峰值：micro-kernel单独计时；嵌入既有cache-aware GEMM（含其outer/panel路径）；BERT-Large派生的五个GEMM shape只是模型算子负载，不是全文模型推理、问答质量、端到端batch/concurrency或SLO。Table1的B1–B5有1024/4096/384/64不同维度；不机械把384当token上下文协议或假定真实Transformer流水线。Square S1–5为1000–5000维，未覆盖所有小矩阵、任意tail和布局。

对照同时改变所选microtile与library实现：OpenBLAS的8×8/16×8，与作者K230 square20×6、BPI square32×7及逐BERT-shape选择不同tile。不授只有compiler lowering造成全收益。独立microkernel最优BPI16×15与完整square32×7不同，说明microkernel峰值不能替代含packing/cache的整kernel取舍。作者在有限shape报告优于基线，但摘要10–35%不是所有层上界：§5.2 BPI B2约5.1→12.2GFLOPS、§6最高2.4×；拟正文无统一性能数字，不拼成通用portable speedup。

源码/harness生成可供verification但本次未运行，也没有本项目数值/性能验证。平台cache/vector width、tile、compiler/flags与library版本共同绑定artifact，不能把target-dependent C输出说成一个binary自动在任意vlen最佳执行。额外kernel集合生成、native编译、部署/tuning、packing、边界处理及全应用执行付费；生成器“几分钟”无完整workflow测量/总fee，能源/多核扩展/batch/concurrency/SLO/全模型质量Not Disclosed。§6明确additional kernels、mixed precision、automatic packing仍future，不纳为已有功能。

## 4. actual唯一owner/具体差额/原逐字PRE

sole owner `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)。actual完整1–52图优化/typed plan、89–118lowering commit boundary/HLS/回归身份/PIM与低精度交接、2326–2335typed schedule/source-kernel IR分支已读；Ch48开篇1–28、Ch50开篇1–30明确decoder speculation与serving不接管此kernel lowering。既有GPU/HLS/source-to-source原则未实际承载**scf/memref/rvv→emitc→现有C native工具链**缺段补齐与目标vlen/tile重新选择的接口，因此拟两最小段，而不是新增端侧/编译收纳章。其他family只作为已有论点/邻接，不重读其Source。

拟位置当前Ch49通用lowering完整marker（2605.13864，L96）后/HLS protocol段前，保留原CUDA与FPGA两分支。

### 正文PRE 1

高层IR到目标指令的路径也可以只补缺失的一段，而不替换整个应用工具链。对packed GEMM，一条受限分支先声明microtile、数据类型和目标向量长度，在IR中显式保存内存指针/offset、跨循环accumulator与vector-length bound；再把memref地址、SSA loop-carried state和目标vector操作分别降为C指针、可变循环变量及opaque intrinsic调用，交给已有C编译器生成RVV执行代码。外层packing和宏kernel继续复用原实现。这样可移植的是生成与接入路径，不是任意layout自动等价、所有向量宽度共用最佳tile或一个binary适配全部平台。<!-- source-family:SF-2026-ARXIV-2603-17800 -->

### 正文PRE 2

[MLIR–xDSL的有限实机对照](https://arxiv.org/html/2603.17800v1)只在两种RVV1.0宽度的单核FP32上比较microkernel、完整GEMM及BERT派生矩阵shape；自动lowering与tile选择共同变化，不能把GEMM收益授为完整BERT服务加速。独立microkernel的最佳配置与含packing/cache的宏kernel不同，须按最终workload重新验收数值和性能，并绑定compiler、flags、目标宽度与内存布局。生成、搜索/native编译、部署和packing都付费，混合精度、其他算子与自动packing仍不在已证范围；类型/地址或最终回归失败时，保留原BLAS、手写intrinsic和已测target-specific kernel，不凭可编译C签发跨平台质量或SLO。

### 静态来源注PRE

- [RVV/xDSL2603.17800 exact-v1](https://arxiv.org/html/2603.17800v1)：必要§4.1–4.3、§5.1–5.2/Table1与§6。只采用packed GEMM下memory/control/vector lowering分责及既有C工具链接入；保两实机单核FP32、microtile/library对照混杂、microkernel/全GEMM/BERT shape权限与全部费用，不授任意memref/指令兼容、混合精度、全模型服务加速或生产SLO。未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2603-17800 -->

## 5. 非准备者裁决待执行

请resume_mar17只上述必要支持/直接反侧、actual唯一owner与两literal/static独核。未获裁与root窄锁不写Books，未actualPOST不计I。原5/date不变；支持足即停，不扩附件、版本或query。

## 6. resume_mar17 非准备者有限 Source / PRE 裁

2026-10-12：actual exact-v1 §4.1–4.3 L120–360（含正文IR/C片段）、§5/Table1 L361–398和§6 L399–404独读；有限Source/PRE PASS。五IR输入到四intrinsic参数、memref/offset到Bc scalar、SSA iter_args/yield到mutable loop变量与RVV opaque类型的降级路径真实，已有macro GEMM和native C编译器继续共存。两FP32单核板、向量宽度、compiler/flags、平均1500/200次及BERT派生shape范围核实；微内核BPI16×15和全square32×7配置不同，native BLAS/tile共同变化，不把有限kernel收益外推整个BERT、任意layout或通用SLO。完整packing自动生成和mixed precision仍future，未核外部artifact/所有图像或复现。

实际顺读Ch49完整1–52、83–122及2326–2342，Ch48/50开篇；既有generic source-to-source CUDA与HLS protocol没有承载此受限memory/control/vector ABI→emitc→native C缺段接入。原两literal/static逐字核准确，sole genericlowering SF2605-13864 marker后/HLS前差额成立；原5/date不改。root授family窄锁后落实、一次非writer actual完整局部/本人静态注POST再计I，不预授DAY，也不以“可编译”认证全部语义。

## 7. reader实际窄写（writer，不是POST）

2026-10-12 root明确soleCh49授权后，写前实际83–124完整genericlowering→HLS→compiler回归/PIM两侧和最后14行源注顺读；只按已通过两literal/static写新98/100和自身2897。写后实际完整83–123和2886–2897本人/ZipServ/SVOO/Relative/QIG邻注逐字回PRE一致，旧分支均保留。章numstat47新增/1删除→53新增/1删除，此family只六新增行，scoped diff为两正文+静态注，diffcheck0。没有改其他family、报告/LS或stage；static无过程验收身份。

交resume_mar17一次nonwriter实际83–123完整邻接/新98,100及2886–2897自身静态源注/邻注POST，根接纳后才计I/释放。原5/date有效复用，writer读回不自授POST或DAY。

## 8. resume_mar17 一次非writer实际POST

2026-10-12 实际顺读Ch49完整83–123、新98/100及2886–2897本人/ZipServ/SVOO/Relative/QIG邻注，回对§4两literal和静态注、§6已独核必要原证，有限POST PASS。generic CUDA lowering→受限RVV memory/control/vector ABI接入→HLS protocol分支衔接准确；packing和宏kernel继续共存，两板单核FP32/微内核与完整GEMM的不同配置、BERT仅派生shape和全部费用边界近文保留，不授任意layout、全模型服务收益或生产SLO。本人静态注与PRE逐字一致，无过程身份；限定diffcheck0。没有另改Books或重开有效Source；交root接纳/释放该family锁，本次单项POST不授DAY。
