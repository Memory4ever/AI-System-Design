# 11331：采样预算与攻击风险，必要Source及具体已有覆盖

root，本日只补Mar13北京时间自然日；实际精确v1原件`SUP_ROOT_CORE_11331.raw/txt`，GET200/569720B/2026-10-09T15:41:18.443282UTC。实际读完整题摘与当前可见history、§2模型/teacher安全标签/student匹配假设、§3 Result1–2与Remarks、§4–5，以及E.2–E.4评价和采样协议；未重做无关spin-glass完整证明/查看图像精确点/运行代码。当前v4存在不表示本次需全版本比较；未见具名撤回或明确影响本窗v1的勘误说明。

## 准入、日期与最低投入

单次拒答表现不能代表多次攻击的累计风险→模型族与注入长度改变k-sample至少一次成功曲线，并比较拒答字符串和内容judge→安全验收应同时限定attempt人口、预算和实际有害内容判据。新命题是这份受限scaling证据与机制代理，不把“多试风险升”成熟原则重复算分。拟2+1+2=5标准；读相关理论资格和直接评价已足够，未把类比当实际LLM内部机制。

精确`SUP_DATE_11331.raw`实核DOI/official abs URL/arxiv.content/findable及Mar13 01:53:03UTC上界；v1Wed21:48:03UTC明确晚Wed截止，沿已核官方公告及ID不可预分配规则夹Mar13 BJT公开日，不单拿Submitted/registered决定first-public。现有日级去重有效复用，未识别具名先稿，不声称查尽外部版本。

## 支持与边界

§2以Gaussian输入、特定权重协方差、large-N低温cluster、人为选定unsafe cluster、匹配teacher/student参数与等field作可解代理；token=spin、field=注入强度和cluster-depth=reasoning都是解释性映射，未在真实Transformer中识别同一phase transition或校准参数。§3 weak-field joint limit给相应gap近似；strong Result2是特定m=1/fixed-k leading-order下的单侧界，Remark3明确Theta(k)仔细理论仍未来。不能将泛型拟合Eq17或这个单侧界当所有LLM已证exact指数律；本次不据此判整个spin理论错误。

§4/E.4使用AdvBench与four-model设置（论文写GPT-Turbo4.5名称，具体API endpoint未披露，不自行校正产品名）、Vicuna7Bv1.5/Llama3.2-3B/Llama3-8B；注入0/14/20token、k1–125步长4、temperature.6、Mistral7BInstruct-v0.3 judge≤4为unsafe，5为incoherent/unrelated。不同judge/拒答字符串下ASR相差，说明判据影响测量；不是独立人类有害真值。正文Figure6称高注入直线含代码数值限制，不将该形状独立证明真实指数机制。E.3 GPT4有害打分与E.4 Mistral scaling判据不合并；稿内例子fake-news被低危害打分也显示具体taxonomy会漏风险类别，不能将低ASR认证普遍安全。

有限模型/固定威胁/公开样本与judge观察支持本次预算敏感性，不授生产发生率或所有强模型天然更安全。Hardware、precision、完整攻击搜索费用、输入输出length、并发/SLO、CI和拟合可比人口不足，不补造；没有查看像素或实现，curve截断/数值floor保留。停止采样、缩预算或增加独立effect检查是工程设计选择，不是论文验证防御。

## actual Books差额判断：已有覆盖，待独核

实际顺读唯一`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)790–855的run-centric安全评价完整局部与936–963的monitor/attempt opportunity局部。现有run identity显式绑定attempt/turn/history、target/attacker/judge、预算与final outcome；明确raw ASR不能代有害effect/真值、局部安全sensor无authority，949–953实际已有多次尝试风险放大及parser/grader预算声明。它们完整承载本次可采用的系统判断，**不声称现书承载新的spin-glass理论或具体指数拟合**。具体代理和受限curve尚不足要求书稿改变设计结论，拟标准完成/已有覆盖、Books新写0；可在精确模型/独立判据下出现改变预算策略的可信新界时只重开该差额。待非作者必要Source与实际owner独核，不授DAY。
