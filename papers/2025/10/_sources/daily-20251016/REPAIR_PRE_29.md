# 第二十九包：近似采样载荷、黑盒sentinel与冻结表示消费者

Books/ROADMAP有效。actual Ch20完整softmax/簇抽样两段及固定logits例子，Ch72取证/预防、AWM完整段及门限共享两完整下段，Ch23 SEMI全文/独立marker及dense-head完整下段，Ch12 CTRL-Rec全文/独立marker与输出头自由度两完整下段均读。邻章交接沿有效未变层，只消费R32/R34/R36，不第二Methods/实现/复现。

## 12343 HE token ordering / 2+2+2=6 / MODEL-SAMPLING Ch20

簇候选分布未承担近似onehot混相邻embedding时的词表坐标排序/多项式后处理；插完整SF2603-14591第二说明段后、固定logits例子标题前。

正文：

抽样结果若不是精确onehot，而是若干相邻坐标的混合，词表顺序也会进入下一步的语义载荷：可按embedding邻近性重新排坐标，再以低阶多项式压低残余混合，最后仍由对应embedding表消费。[受限近似采样分支](https://arxiv.org/html/2510.12343v1#S3)要求采样坐标、token ID映射与表行一起绑定，不能只改一个数组顺序。其实际实验为plaintext，不是密文执行、隐私部署或HE净速证明；honest-but-curious也不覆盖恶意参与方。邻近cosine不是所有语义的metric保证，未闭多项式/误差式不补完整recipe，额外LoRA改变分布亦须分账。全词表两两比较/重排、适配、后处理及加密执行的独立验证都计费；映射、质量或实际加密费用不合时保精确onehot/普通采样及可信映射，不由较低邻居误差批准原分布不变、内容保真或机密性。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12343 -->`

本人末注：

- `SF-2025-ARXIV-2510-12343` — Herschel，Daily2025-10-16补Oct15；消费Cicero R32 exact-v1 §1.2/2.1–2.2/3.1–3.3/4.1–4.4首次必要，2+2+2=6，仅近似onehot混合/坐标排序与embedding consumer差额。保plaintext非HE、诚实但好奇非恶意安全、TSP/PP式和cosmetric未闭、LoRA混杂及O(V²)/训练/加密全费，不授隐私部署或精确误差定理。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12119 ImageSentinel / 2+2+2=6 / PLATFORM-SECURITY Ch72

现AWM白盒对齐/检测未承担可预置训练样本sentinel的黑盒响应支持与非命中资格；插完整AWM inline段后、共同训练门限水印首段前。

正文：

黑盒查询还可以检验预置训练样本是否留下特定响应，而不读取权重水印：将随机字符key与参考属性生成的sentinel配对置入受控数据，再以查询输出和参考的表示相似度提出消费线索。[受限图像sentinel分支](https://arxiv.org/html/2510.12119v1#S4)不是持久watermark、加密授权或所有权证书；命中只支持这份sentinel关联，不能推及整个数据子集，不命中也不证明从未使用。触发率、Hit@k和阈值下TPR/FPR须分开，更多参考命中不保证优于语义基线；检测后inpaint等适应性处理可显著移除信号。Key/合成来源、可见查询、encoder/阈值、null人口和变换应共同留档，全部造数、训练、重复查询/相似度与质量校准均付费；信号、误报或威胁超界时保Unknown、签名数据谱系和独立取证，不由低误报下检出签发法律未授权、隐蔽性或无损保护。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12119 -->`

本人末注：

- `SF-2025-ARXIV-2510-12119` — Herschel，Daily2025-10-16补Oct15；消费Cicero R34 exact-v1 §4.1–4.5/5.1–5.2/limits首次必要，2+2+2=6，仅预置sentinel/黑盒响应的消费线索差额。保非watermark/授权/所有权、Hit5弱semanticbaseline、detect-inpaint五query使TPR@1% .98→.15、100query非全检、8V100/10k30k库/100×5和全费，不授stealth/生产维权。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12681 CoRA / 2+1+2=5 / MULTIMODAL-REPRESENTATION Ch23

SEMI生成projector权重不是冻结多模态特征先对齐/soft covariate加权再调原forecast head前后shift-scale；此为跨模态载荷与消费者差额。插完整SEMI独立marker后、dense-head首段前，不采领域预测结论。

正文：

冻结模态encoder后，还可以让对齐后的特征只控制原预测head的读写尺度，而不把所有条件拼进主干：先形成多模态协变量的soft组合，再在head前后产生shift与scale。[受限条件适配分支](https://arxiv.org/html/2510.12681v1#S3)区分特征生产、条件选择与原输出消费者；零初始化只保证初始接口等价，不证明适配后无遗忘，相关性权重也不是intervention因果。跨snapshot均值会丢时间顺序，未来已知协变量与未来不可见信息必须分开，不能借多模态名称扩大部署可见性。Encoder/对齐、协变量时间、head/调制和选点人口须共同保存，单一长horizon切片仍可反退；全预训、特征制备、adapter训练/验证和真实任务回归均付费。条件可见性、时间支持或原质量失配时保原head/原模态、较窄可靠协变量与独立持出，不由冻结或zeroinit批准无损接入、真实因果和通用预测能力。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12681 -->`

本人末注：

- `SF-2025-ARXIV-2510-12681` — Herschel，Daily2025-10-16补Oct15；消费Cicero R36 exact-v1 §3/4.1–4.2/A.3/D首次必要，2+1+2=5，仅冻结模态特征/soft covariate与head shift-scale载荷差额。保zeroinit非适配后无遗忘、GCE/Granger非干预因果、mean丢时间/future权限、Sundial2880lookback/A100B128/50epoch及ECL720反退、全费，不采领域预测或SLO。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12014 EmbeddingTeacher / 2+1+2=5 / MODEL-EMBEDDING Ch12

CTRL-Rec teacher item-value不是按当前student score分层抽候选、teacher小组排序成pairwiseBT的标签生产机制；插完整CTRL-Rec独立marker后、输出头自由度首段前。

正文：

教师偏好还可以通过当前学生的score分层来选取训练比较，而不一次给全库打分：从各score区间抽候选，交给较重teacher在小组内排序，再转成pairwise目标更新embedding消费者。[受限表示教学分支](https://arxiv.org/html/2510.12014v1#S3)冻结文字端、适配图像端，改变的是比较标签的生产与学生度量；teacher tournament的赢家percentile不是真人满意或top-1成功，偏好不传递时还依赖配对顺序。Persona/候选库、分层区间、teacher/排序转pair与encoder版本须共同保存，未闭bin端点或对比数量不补默认recipe；validation选点和独立test分开。全部teacher/API、候选制备、训练、全库重编码与独立真人/任务回归均付费，不由少量分组推算精确总调用预算。教师量尺、分层支持或净效用失配时保原embedding/普通配对标签、较窄库与独立用户评价，不由赢过教师挑出的对手批准真实偏好、无损泛化和部署净速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12014 -->`

本人末注：

- `SF-2025-ARXIV-2510-12014` — Herschel，Daily2025-10-16补Oct15；消费Cicero R36 exact-v1 §2/3/5/D首次必要，2+1+2=5，仅student-score分层候选/teacher排序→pairwiseBT标签生产差额。保50val/50testpersona/三catalog、teacher tournament非真人/top1、bin与4096/8191pair计数冲突、3090Ti/1000APIstep及全部制备/训练/重建费，不授独立质量或精确调用预算。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

请sole reader整体核四正文/独立marker/本人注和完整邻接；未SAVE/不预POST。
