# SIMART necessarySource / sole Ch23两PRE

2026-10-12，[2603.23386v1 PDF](https://arxiv.org/pdf/2603.23386v1)，原2+1+2=5/date25保持。HTML404后原PDF正文仍可读取，非必要材料故障。actual PDF文字必要§3(pp4–6)/§4/T1–3(pp6–9)、§5/6(pp9–10)、B sparsecodec/T4和C output(pp15–16)、D benchmark/T6(pp18)；web截图未向当前工具返回可视图像，局部下载尚未完整，不冒已看图/完整visualPDF独审。不需要复现/所有图与视频，必要公式/表文字和直接反侧已足。

## 可采用接口 / 直接反侧

Qwen3VL8B输入image/mesh/text：3DUnet编码64³→16³，B明确将每八相邻tokens沿channel聚为8³/64dim，桥实际已披露，不误记16/8矛盾。对空位置指定codebookzero，occupied只从非zeroentries最近邻量化；把非空项序列化为<voxel> [xyz] [codebookK]，8³坐标xyz=64x+8y+z、K0..4095，模型输入与part输出需explicitaddress，不因短序列默认保密集位置身份。Decoder重建完整grid仍需要zero/default补齐，未披露重复地址/invalidcode/边界处理，不照抄完整recipe或称surface拓扑硬保持。

MLLM输出part-specificgeometrytokens＋JSON-like jointparent/type/origin/axis/limits/materialdensity等，parttokensdecode sparsepoints，再按originalmesh vertex到partseed Gaussian→graph smoothing/majorityface labels分割并保originaltexture。不是直接decoder无损生成高精度mesh/物理参数true；σ/graph迭代细节未给，纹理保原不授part边界正确。C252²45°iso image给语义/scaleprior，语言模型推real scale/density不是实测单位/力学真值；sim-ready输出格式只proposal，不批准真实dynamics或机器人安全。

训练39.6Kobjects=5.6Karticulated+34Kstatic/20states各训练实例、URDF/part各960KQA；codec500Kobjects/TRELLISprior/每stage60K×2/8A100，MLLM30K/32A100。precision/B/lr/完整objective/最大context/infersteps/runtime/B/concurrency/tailSLO未披露，不从A100或零token推出净内存/实时。D AIbenchmark仅36资产、>10categories，P3SAM初6–10fragments人工merge2–4与轴/joint手标GT；独立重标误差/跨assettrain/test去重/seedCI未披露，不称36个真实control场景。

T3 denseOOM4138outputtokens vsforcesparse862 vszero516，包含partgeometry+symbolicoutput、平均四parts，不是仅inputvoxeltoken数或所有complexparts永不OOM；516/4138减约87.5%不是摘要70%同分母，不擅统一。Vision叠加后metrics更好同时增加图像信息，不能把全部差额归zero；T4更高16×8×8 MSE1.15/CD2.27好于8³1.84/4.19但tokens倍，原8³是memory/fidelitytradeoff，不授最优/无损。较大codebook8192 CD4.56反退，forceNoZero CD56.10显示该局部资格反侧，有限VQreconstruction不认证所有thinpart拓扑/URDFphysics。T1多数baseline不接受rawmesh，geometry信息/训练预算与pipeline不同，Particulate也非singlemodule唯一因果。simulation/VRAR只是demo，无closedloop任务统计/real-to-sim安全证明；生成/制备/meshvoxel/VAE/LLM_AR、sparseaddress重建/graph分割/URDF组装与验证全计费。

必要反侧纠错（作者非准备者actual定点回exact-v1 PDF B571–618/C645–647/Table5 664–669）：B的16³→8³聚合桥有效；但C称Table5为train/infer complete prompt，Table5却写16×8×8、x0–15/xyz0–1023、K0–8191，与正文/B选定8³/4096不同。原配置与系统prompt身份未闭，不将二者修成统一exactrecipe；局部zero/default、显式地址和part共同身份接口不依赖哪套数字成立，不整体HOLD或降5。两PRE不复制冲突数字，仍可独立采用；具体部署需核实际codec/grid/codebook与prompt绑定。

## actual Ch23 gap / 锚

actual Ch23完整1125–1205 Native3D现sidecar→nativegeometry→fragmentjoint→partbudget→camera→tracks，OpenVoxel/City/partialbinding完整块亦读；Ch24/25开篇有效复用。16745共同token/revision保持几何身份没有声明丢空位置后address/default重建与partgeometry-symbolicmetadata的接口，OpenVoxel是实例dictionary不等可生成codec。sole MULTIMODAL-REPRESENTATION Ch23，不复制Ch24采样或Ch26physicalcontrol。

拟nativegeometry16745完整两原段+standalone marker之后、下一“碎片位姿与整体shape…”22629原段之前两PRE+本人纯静态证据注；原sidecar/精确工具回退与joint分支完整保留。未独核/锁/实际写/POST。

## 两逐字PRE

几何进入可生成的 token 接口后，空区域仍可能消耗每个 part 的输出预算。一个受限 codec 分支给空位置保留专用 zero/default，只对非空几何量化，并在可变长序列里显式携带坐标和 codebook 身份；重建时再恢复完整网格。这样节省的是向语言模型读写的序列，不是让几何本身不再需要空间地址，也不保证薄结构和 part 边界无损。模型还可联合提出每个 part 的几何 tokens 与关节层级等符号 metadata，两种载荷须以同一 part 身份关联，不能由较短表示自动认证关节、尺度或材料属性。<!-- source-family:SF-2026-ARXIV-2603-23386 -->

稀疏重建仍有自己的预算边界：更细 latent 网格能改善几何却加长序列，零 token 的默认填充和不合法/重复地址也需验收。原流程还用重建的 part 种子在输入 mesh 上传播分割并继承纹理，分割与 kinematic proposal 并非一次解码就取得物理真值。有限对象和输出-token 统计、人工标注及不同输入能力的基线，不能证明任意复杂资产不再 OOM；模拟展示也不认证真实控制。Voxel 制备、codec/语言训练、所有 part 生成、完整重建、图分割与 metadata 验证均计费；地址、边界或关节不可信时，保留较密几何、原 mesh、专用分割/重建和显式运动学检查，不让 sim-ready 标签批准世界状态或行动。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23386` — [SIMART exact-v1 PDF](https://arxiv.org/pdf/2603.23386v1)必要§3–6/T1–3、B/T4/C/D/T6；仅zero/default与occupied地址codec、partgeometry/symbolicmetadata共同身份接口。B选定8³/4096与Table5系统prompt16×8×8/8192身份未闭，不采统一配置recipe。保输出token人口/网格fidelity代价、meshgraph分割与参数非物理真值、36人工资产/异输入baseline与全费；不授通用recipe、无损/OOM消除或真实控制安全，未核code/全部图视频/复现。
