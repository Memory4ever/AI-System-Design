# Label cosine `2603.29488v1` — 必要理论 Source

root 完整 AB 与必要 Source 已通过；最终 `3+1+3=7` 指「未固定输出坐标的 label cosine 不能认证 softmax 行为」设计反侧，reach 仅独立输出组件，非把已知 softmax shift invariance 重新计突破。[精确 v1](https://arxiv.org/html/2603.29488v1) §2 Lemma2.1–2.3/Theorem2.4、§3具体例子和§4边界已实际读，原件[本日必要核心](SUP_CORE_2603-29488v1_20261013.json)。无实验性能或代码验收。

## 可采用的证明链

Eq1 模型类固定 input representation `f(x)`、允许独立 output label vectors `g(y)`。将同一向量 `v` 加到所有 label vectors，使每个 logit 同增 `f(x)^T v`，在 softmax分子分母约去，故每个input全部概率不变。对不同的两个output vectors `a≠b`，取 `v=−(a+b)/2` 得两非零相反向量、cos=−1；取 `v=−a+(b−a)/2` 得 `(b−a)/2` 与 `3(b−a)/2`、cos=1。Theorem2.4的不同向量条件确保构造不为零；不采用Lemma2.3对相等零向量的未定义cos特例。

因此，相同条件概率函数可对应不同未中心化label-cosine。它反驳的是行为解释的普遍可识别性/保证，不证明在固定训练架构、规范化和输入分布下 cosine 永远没有统计相关。Centric处理去掉common translation ambiguity，也不能凭角度独自推任意输入的概率；概率仍由input方向、norm及其它竞争labels决定。

## 直接边界和局部不一致

- 原文§4明确不论input embeddings cosine或普通retrieval/CLIP语义相似度，不把这里的反例推广为所有embedding距离都无用。
- 该证明固定`f(x)`且改变独立输出头；若系统强制input/output tying，直接改同一共享权重会同时改变input路径，原证明不提供保持该tying架构的drop-in等价改造。不得把输出头gauge与整模型权重不变混同。
- Eq6末写`p(y|v)`而前面的约消实际为`p(y|x)`；此处只采用已独立代数确认的共同logit平移，不照录该记号。
- §3.3文本Eq20/21的两个所列vectors与其声称约0.8 cosine不协调；当前不据此授「单位norm＋centered全部形式反例」的完整证明。§3.2的centered几何例子也应注明非零输入，零input使全labels平分，不能把“无法top-tie”写成无条件。两侧原文保留，不擅自改论文坐标。

## 待独核、日期与Books

Submitted Mar31T09:33:12Z与2603首次announcement月符合root复合日门的常规边界，尚待当前官方页轻量先公开/纠错信号确认，不凭Submitted或created单独定窗。Source独核后再比较 `MODEL-EMBEDDING` 输出读出/坐标解释与相邻Attention/学习表示的实际正文：若已有固定输出坐标与行为检验，可已有覆盖；否则只补输出头gauge、基于条件概率/任务行为核验的窄分支，PRE/锁前不写。
