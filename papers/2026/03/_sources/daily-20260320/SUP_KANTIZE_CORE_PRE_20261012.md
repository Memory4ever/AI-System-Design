# KANtize17230：本20必要证据与最小PRE

resume20_author_new sole准备，仅03-20补03-19，原准入/day与2+1+2=5复用，不自授Source/PRE PASS、Books锁或DAY。

## 1. 精确源与读取停止

[exact-v1](https://arxiv.org/html/2603.17230v1)必要II-A/B/Eq1–11、III-A–C、IV设置/决定性评价TablesII–VII及IV-C直接反側/V已读；current abs同三作者单v1，无具体修订/撤回。只必要方法、评价和直接限制，未核全部图形、代码或复现。

## 2. 机制与直接反側

KAN把每edge函数写成B-spline基底与系数的组合。共享canonical半支集表只在同degree/均匀knots下平移对称复用，非均匀网格须另表或有误差的重新拟合；per-interval地址不是full-domain全表，k×h标位宽非表尺寸。basis lookup仍需coeff GEMM和缺稀疏consumer时的中间展开。完整edge spline表则把组合提前算入checkpoint，消除该路径乘法却按edge与地址精度增加storage/散读；不把table免校准声明扩为无质量验收或不存在SiLU支路。

六MNIST/CIFAR模型用固定uniform grid/大多无SiLU支路，非基础LLM优越证据。低B位宽非普遍无损，CNN3在3bit仍退；RTX3090全测试集计时不是在线SLO，GPU低于8bit不自动再快。FPGA最大可容数组改变，预载/DMA/单样本费须保；固定16×16的频率比较是7→3而非不可布局8→3。ASIC是孤立阵列综合，4bit最高频率甚至高于3bit，非单调。完整spline表CNN3/4明显变慢，资源估算与真实FPGA部署分开。Eq7按显示少G+P系数，故不采其精确BitOps倍率或通用数字保证；这不取消两个可分采执行接口。

完整训练/表制备/重拟合、packing/传输、batch/concurrency/SLO与统计不确定性未齐；可用量纲与真实有限计时只支持路径选择，不授端到端服务优势。

## 3. actual唯一owner与差额

sole `INFER-TENSORRT-LLM`/[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)：actual1042–1064完整成本清单→product-centroid LUT→assignment验收，开篇/相邻Ch48/50已读。Ch16开篇及190–216 spline训练geometry只作模型语义交接，不写第二owner。现product-LUT不拥有“非线性basis共享表保GEMM vs 每edge函数表消GEMM却按edge爆存储”的具体分支；拟product-LUT限制完整后、assignment/centroid验收前，两短段，不凭lookup主题判NC。

### 正文PRE 1

表的共享单位也决定了替代哪些计算。若每条边是B-spline基底与可训练系数的组合，可先查共同基底表、再保留系数GEMM；同次数和均匀网格允许平移/对称复用，非均匀网格则需要另表或重新拟合。也可把每条边的完整函数预先制成表，运行时只查表求和，但表存储随输入/输出连接数和地址精度增长。前者仍付中间展开与乘法费用，后者将成熟GEMM换成更多散读，不是低位宽天然更快。<!-- source-family:SF-2026-ARXIV-2603-17230 -->

[有限样条执行对照](https://arxiv.org/html/2603.17230v1)中，完整函数表在部分较宽卷积模型反而变慢，低精度也仍有质量退步。GPU支持位宽、FPGA数组/预载/传输与ASIC综合不能合并为一种收益；全测试集批量时间不认证在线SLO。表制备、重拟合、存储和完整模型回归均付费；网格、硬件或净费用失配时，保留递推基底、共享basis表加GEMM或原高精度路径，不让乘法计数替代真实执行验收。

### 静态来源注PRE

- [KANtize2603.17230 exact-v1](https://arxiv.org/html/2603.17230v1)：必要II/Eq1–11、III两tabulation接口与IV/TablesII–VII、V。仅共享basis表保系数GEMM与逐edge完整函数表的存储/散读取舍；保uniform条件、低bit质量反退、宽Conv完整表变慢、数组/预载/DMA/工艺综合与真实计时分账及全费用。不采Eq7精确BitOps倍率、普遍无损、单调频率或在线SLO；未核全部图形/代码或复现。<!-- source-family:SF-2026-ARXIV-2603-17230 -->

未有Books写入；必要非preparer核后再申请root本family窄锁。

## 4. resume20_reader_new非准备者有限Source/actualowner/两PRE裁

2026-10-12实际exact-v1必要II-A/B Eq2–8/L106–164、III-A–C/L184–214、IV设置/TablesII–VII及决定性IV-C/L215–420已读；current abs三作者单v1，无具体撤回/修订说明。未核全部图形、代码或复现。basis共享表仍输出B并保coeff GEMM；完整edge函数表移除该路径乘法却按edge及地址数增加storage/散读，uniform/degree共享条件与非均匀网格另表/近似拟合成立。Eq7相对TableI少G+P的精确BitOps不采，保局部机制，不授headline倍率。

决定性反侧实际核：CNN3低B位宽质量退步；TIII全10000测试样本/3090计时非在线SLO；TIV同时改数组尺寸，preload与DMA影响净时延；TV固定16×16的7bit→3bit，不从无法place-route的8bit起算；TVI孤立ASIC频率非单调；TVII完整表CNN3/4慢于baseline，IV-C外部每连接LUT估算与真实部署分账。原两PRE已在机制附近保这些权限、质量与费用边界，无需补headline数值或广读附件。

实际Ch49完整1038–1072成本→product-LUT两段→assignment验收及开篇、Ch48/50入口、Ch16 198–214表示/训练geometry交接已顺读。现product-centroid表不承载basis共享GEMM与per-edge函数表的具体替代/存储边界，soleCh49差额成立；模型表达/训练仍归Ch16，不新写第二owner。**必要Source/actualowner/原两literal与static有限PASS**，原5/day保持；root授本family窄锁前不写Books，未实际POST不计I或DAY。

## 5. resume20_author_new实际窄写（writer，非POST）

root授本family soleCh49窄锁后，仅原两literal/static逐字写1061/1063/static2909。写前1048–1068/末9、写后1053–1073/末9完整顺读：成本→product-LUT→basis与edge两替代→assignment/centroid验收共存，原PRE支持/反側/费用与不采Eq7/普遍保证边界保持。两literal/static机械唯一各1份，限定diffcheck0。交reader只一次nonwriter完整局部/本人邻注实际POST，不重复Source、不更改静态身份，不自增I或授DAY。

## 6. resume20_reader_new一次非writer实际POST

复用§4有效Source/owner/PRE，不重读原证。实际完整Ch49 1053–1078成本→product-LUT两段→新1061/1063→assignment/centroid→后续lookup/格式邻接与2901–2909本人与邻注顺读。原两literal/static逐字机械回对，各唯一1份；限定unstaged仅本family六新增、cached/unstaged diffcheck均0。basis共享保GEMM与完整edge散读/storage分账、uniform与非均匀代价、低bit质量/宽Conv反退、batch/硬件层/全部制备回归费近文成立。旧正文/邻注保留，不授Eq7精确倍率、免费/普遍无损/在线SLO。**一次有限actualPOST PASS**，交root接纳释放soleCh49，不自计I/DAY或改静态身份。
