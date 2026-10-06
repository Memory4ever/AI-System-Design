# Nov20 LIT/Video/Kandinsky 最低决定域

## 1. 范围与层次

作者Noether；仅完成主题差额包LIT/Video及TOPIC3 Kandinsky的三个最低事实域，原精确v1 AB有效层不重。原件`SUP_WEB_MINIMUM3_20261015.raw`，实际必要§/行号如下；这是作者2窄P/1C提案，未独核前不改通过数量，不授公开资格/评分/完整Evidence或Books。

## 2. LIT 14903：具体C提案

实际精确v1§3.1–3.2 L86–105及必要4.2–4.3 L119–131。cost由用户按robustness/debuggability/argument complexity指定，solution为所用tool cost总和；给5few-shot，LM最多先生成4个sequential候选，自己算各cost再选较低者并执行，Finish只收尾/类型。已明确最小机制，不是未读正文就按inspectable词关。

必要域实质是已知多候选生成/按预设启发式cost择优的task prompt模板，没有辨明新的可靠性估计、可验证执行约束/失败回退或使cost获得独立证据的机制。把低cost工具称reliable不是实际分布校准；可调tool优先级、1300题与该表cost结果不单独建立主线增量，拟C。不是因few-shot/prompt天然无价值、工具常见或缺新模型关闭；若reader在原域辨出具体新条件/反证只恢复该事实，不扩全部题/8工具实验。没有采“Calculator总正确/代码完全透明”等强描述，也不为未知日另开请求。

## 3. Video14719：窄P提案，反演/条件不授严格保真

实际§3.1–3.2 L110–148及必要4.5/Limitations L198–239。原Cosmos-Transfer ControlNet从depth/semantic/Canny条件出发；此分支另从source latent做DDIM-style inversion，用原内容prompt建立初始化，再保持spatial maps、换realism prompt重生。不同于仅把多个map叠在pure noise上，具体初始化/条件消费与global composition取舍有潜力；其CFG/加blur条件反侧显示更像原视频与更photoreal不总同向，保这一局部设计选择，不按“组合”自动C。

Euler逆步/EDM与有限步重生不证明unique latent、严格反演或所有语义保存，σ=0起步等完整recipe未在此域闭合；从估计器取得map亦不使GT可得。DINO/CLIP/LPIPS及MLLM偏好不是真实小物体身份/traffic safety，+blur alignment最好却photoreal19.2%、增CFG fidelity退步保留。121frame窗口/chunk边界、冲突prompt、额外caption/map/inversion/regeneration均有费用；原文下游训练效用仍future work，不采已闭sim-to-real或控制安全。只读必要规则/反侧，不扩900视频/全部可视化。

## 4. Kandinsky14993：窄P提案，采用具体接口而非系列名

实际精确v1§5.2–5.4 L850–914。CrossDiT把visual self-attention与text cross-attention分开，不再MMDiT样式直接拼接两种tokens，为不同video长度/稀疏visual mask形成单独接口；NABLA将Q/K按64token块平均，reduced attention按head用CDF选择块，再可选与local Sliding-Tile mask取union，fractal flattening/inverse保持输入输出位置身份。这是明确的粗proposal/原块执行及local/global支持取舍，不仅6B/2B/19B模型发布，拟窄P。

块平均不证明原tokenattention严格可恢复，CDF保质量和union费用需必要Evidence；2.7倍/等质量宣传不采作已核E2E、硬件通用或全部训练收益。所读原文引用另NABLA工作，属于采用/系统组合而非宣Kandinsky首次发明；其首次公开/同事件去重仍由必要日门另核，不因paper晚版或模型名字直接加家族。LTF去positional bias也非本域已验证的普遍解释，不展开全报告2217行/三模型recipe。

## 5. 交接

请root转Ohm真实核这三个最低域2P1C及反侧，不能用包/标记代实际语义审阅。LIT具体C若获核无需为不影响处置的日期再请求；Video/Kandinsky仍保必要公开资格及版本权限，不把上述读到的实验片段等全部Evidence。Objects/SAM3/S2ST正文/POST/root与本人注admin已闭合，不重；97/132不含Nov20，其余主线题摘/安全/日门和six继续，无普通消息/共享写/stage/commit/push。
