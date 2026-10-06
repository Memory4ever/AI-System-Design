# Nov20 Body 单段与本人末注逐字 PRE

## 1. 已发生范围

作者Noether；root已实际读Ohm20–22并转达Body受限静态消费/5分/唯一Ch23差额通过，作者已读相应独核。原Source/owner采用命题见BODY_RECOVERY§7–8，只复用该层，不重方法/未来全文。此处只待逐字PRE独核/root窄锁，尚未写Books/未POST，不授DAY。

## 2. 实时锚点与范围

唯一owner `MULTIMODAL-REPRESENTATION`，文件`books/part-03-multimodal-world-models/23-multimodal-representation.md`。实际完整重读AssemLM两段、独立3D sidecar/mesh-state两完整段及其marker、后完整part codec两段，并读当前章末notes。拟在完整sidecar第二段及`SF-2026-ARXIV-2605-16745` marker之后、以“几何进入可生成的 token 接口后”开头的part codec首段之前插一自然段；保全部既有正文/marker/其他notes，末尾仅追加本人一注。现无本项写锁，不能据此直接写。

## 3. 拟插入一个自然段（逐字）

单图重建需要用户修正时，也不必先把几何改成统一生成序列；另一条分支保留图像特征，将归一化2D关节点、上一轮预测与参数化rig读出分开。[原机构说明](https://ai.meta.com/research/publications/sam-3d-body-robust-full-body-human-mesh-recovery/)披露骨架/表面分工与提示路线，[初始实现的调用方](https://github.com/facebookresearch/sam-3d-body/blob/4e33ae485b2ea0ecc38328fa39b16b75dd3e79c0/sam_3d_body/models/meta_arch/sam3d_body.py)则把点提示和上一轮pose/shape等预测映成不同条件token；点交互复用已保存图像特征，却仍从learned初值构造residual读出，而不是把上一轮预测当硬约束或递归数值初值。Mask在特定配置下另加到图像特征，不与点提示共用同一sparse入口。Rig把pose、shape、scale等字段分开交mesh/keypoint消费者，表示职责分开却不保证统计独立、改一组不影响另一组，用户2D点也不是新增3D观测。这里只解释静态接线，不采纠错效果、训练采样或泛化结论；原head中face置零、单位/相机转换及配置限制也不允许从full-body名称推出全部自由度已测得。图像编码、提示编码、每轮decoder与rig读出均付费，特征复用不等零成本；crop、坐标或rig版本失配、遮挡使几何不可识别时，保留原图、可信多视角/专用拟合及人工核验，不由提示或参数化输出批准物理状态与行动。<!-- source-family:SF-2025-META-SAM3D-BODY-NOV19 -->

## 4. 拟追加本人一条末注（逐字）

- `SF-2025-META-SAM3D-BODY-NOV19` — Daily2025-11-20补Nov19；[Meta原机构](https://ai.meta.com/research/publications/sam-3d-body-robust-full-body-human-mesh-recovery/)Nov19事件门与受限AB有效，官方repo初始commit `4e33ae485b2ea0ecc38328fa39b16b75dd3e79c0` README/head/prompt encoder/decoder及主调用方289–516、766–789、1057–1177、1649–1682只补静态接口，不由git时间授每blob当日公开同bytes，不用2602.15989未来全文倒填。2+1+2=5，唯一Ch23差额深入；只采点/上一估计条件token、独立residual初始化、mask图像支与分组rig输出职责，保配置/face置零/坐标限制、非独立控制/3D真值、全费与专用拟合退路。原PDF/初始raw失败不作证，MHR辅助晚一天文档与正确BJT边界空返回不证明当时未公开。未采用SOTA/纠错有效性/训练recipe/性能安全，未运行代码或验权重制品。Ohm20/root必要Source/5分/owner已通过，本逐字PRE待核，未授写锁/保存/POST/DAY。

## 5. PRE 自读与交接

正文在前mesh-state分支之后引出“不改统一序列也可交互”的并行接口，再接part codec；不说旧sidecar错误，不把现有shape/pose与真值限制抹去。采用差额不是泛identity/cache原则，而是上一估计条件与residual初始化的具体区别及点/mask/rig消费者。预案不要求训练sampler或SOTA对照来支持未采用的效果，不扩大到Ch24/25/26或书索引。

请root转Ohm实际核§3完整单段/§4本人注和当前两侧；通过后由root决定唯一窄锁。写前仍重读实时锚点/末注与cached、unstaged两层diff，保护外部并发；真实保存/self-read后再交实际非作者POST/root接纳释放，不预签。三已闭合Books不重，97/132不含Nov20，其余source/日期/six继续。

## 6. root7窄位下实际保存与 self-read

以上§1–5是写前PRE，现Ohm26逐字PRE/root§7实际通过并授唯一窄位。实际`git ls-files`返回小写tracked `books/part-03-multimodal-world-models/23-multimodal-representation.md`；写前完整cached/unstaged diff及实时完整两侧/章末注已读，真实unstaged32新增/cached14新增，不沿用Ohm26空返回。外部及本日已闭合各段/notes全部保护，不重其Source/POST或认领。

作者已真实按§3逐字插一个自然段，当前L1333；按§4追加本人一注L2208，仅行政尾同步Ohm20/26、root7授锁、实际保存/self-read与POST/root尚待。随后实际完整读新段/前完整sidecar两段及marker/后完整part codec两段与本人完整末注/前Pi-Seg注；点/prev条件与learned residual初值、mask分支、rig读出/配置/face/坐标和费用/专用拟合退路均与PRE一致，无纠错/SOTA/物理真值越权。

实际正文与PRE§3字符串相等；去掉本人新段/注连新增空行后，`git hash-object --stdin`还原写前blob `91817062f2b9802404f55f9c534c5b1ccf05251f`，只作外部原有内容保护的形式检查，不替语义self-read/非作者POST。当前unstaged36新增0删＝既有32＋本人4，cached14新增0删不变；两层限定diff-check无诊断，不冒全仓clean。只写Ch23本窄位与本包，无index/State/他注/stage/commit/push。

交root转Ohm actual完整新增/两侧/本人注回PRE作POST；root实际读回后才接纳释放，作者不自行释放或预签。root现98/132不含Nov20，本单项真实保存仍不是DAY/FINAL，其余来源/日期/six继续。

## 7. 已发生 actualPOST／root8 行政同步

作者实际读回Ohm28与ROOT§8：完整新增/两侧/本人注actualPOST通过，root实际读回接纳并释放Body窄位，四处本日整合现均已接纳。本人只同步自有note行政尾为Ohm28/root8，机制正文/采用边界与其它notes未改，不重Source/PRE/body/POST；同步输入时“与”一字误作“與”已立即还原，最终非行政note前缀逐字不变。

同步前再次实际定位本人note，此时外部已另有P3T等并发新段/注，本人note为L2212，不挪外部内容或用旧L2208作覆盖锚。请root直接读此行政差额闭合，不等重复POST。README/six另按实际层归并，本项不授DAY，98/132不含Nov20；后续不再碰此注。
