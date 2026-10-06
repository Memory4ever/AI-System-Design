# LogitMatch 2601.16946v1：定点重开

原贡献关闭未识别 input-binding constraint state。jan27_gate实际读 [exact-v1 HTML](https://arxiv.org/html/2601.16946v1) 的方法、任务/模型协议、Results与Limitations；root另行实际读取必要机制、评价与直接反侧。网页是原源，本笔记是判断定位，不替代原文。准确段位：§4.1 Preliminaries、§4.2 Algorithm、§4.3 Tokenization，§5 Experiments、§6 Results及Limitations。

DEFAULT/SELECT/COPY：普通输出状态在进入 text value 后选择输入候选位置，复制状态只沿匹配的输入前缀或结束引号推进。不同 tokenization 不能只允许源 token 的单一 successor；包含文本尾部与引号、或闭引号与下一字段开头的合并 token 需要处理边界。连续输入 substring 合法不等于标签正确，也不解决多处同文的 occurrence identity。

NER/GEC/ESAMT/CPL是不同协议；hard F1要求精确 span，soft F1不能替代identity。Qwen3-8B/Mistral-Small24B/Llama3.3-70B 可用于 logits mask，GPT5-mini API分支不能运行 LogitMatch。非标准空格标点的 span mismatch是直接采用对象；GEC tagging反侧与 occurrence index仍不完美保留。某些 JSON约束可能损伤任务推理质量、loop仍可耗尽输出预算，重复文本和类别判断不是已解决的保证。

准入原分数2+1+2=5不重打；因 INFER-SGLANG Ch51 structured-output 原正文只有 grammar/语义prefix，没有输出与输入序列复制状态，具体 owner gap 定点深入。新增正文134–138及Review notes由jan27_gate写，root非作者实际原源→正文/邻接POST独立验收通过，不自验。单项首公开原字段见 identity-16946.json；不是读取后来v2替换v1。
