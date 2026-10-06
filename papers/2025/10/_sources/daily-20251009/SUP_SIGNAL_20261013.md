# 2025-10-09 Search-R3具体当前纠错信号

后段当前Atom的07048v2/updated2026-04-09 comment实际写完成Large训练、corrected error formulation、added Discussion；这是真实具体信号，不是版本号触发。只为它定点读精确v1/v2的§4.2/§5，不启动2026报告或全版本/附件研究。原件在[supplement](supplement-20261013/)。

获取实际：`signal-searchr3-v1`200/exit0/358901B；v2为200但**exit28/310724B截断**，不是完整成功HTML。HTML parser实际核所需`S4.SS2`及`S5`在两原件均有完整section结束，故只采用这两个实际完整局部，后段未完整内容/Discussion/图形不授阅读，当前必要局部足够，不机械重复整份失败下载。两段正文与公式实际已读。

v1 Eq7写标量S乘rank求和，邻文却定义每rank相似度Sk，scope/定义不一致；v2 Eq7改为Scale并明确query与groundtruth document的cosine，不能反填为v1已披露的同一奖励定义。v1 Eq8负例写`n_i subset D`而正文称单个hardnegative，v2改`n_i in C`；embedding函数定义由vertex域改document域，Algorithm1去掉未消费queries input并澄清重编码范围。只核这些实际差额，不声称全部公式无误、code实现已核或作者进行了同预算复现实验。

两版本§5同保留：query autoregressive reasoning、document固定模板singlepass；以positive/hardnegative的HNSW kNN及2hop邻域、batch再编码与localjoin替代每step全库重建。故原窄P可保这个**选择性刷新消费者**，不以改定义授全局索引陈旧误差界、最优搜索或端到端budget保证。旧v1reward/集合/映射争议不删，v2不能追认v1有效实现；新增Large结果/Discussion不采用。

日证另看[日期包](SUP_DATE_20261013.md)：官方repo的Oct08创建、Oct09 preprint/model发布是不同事件；此2026修订不是Oct08重要新事件。root已实际[§13](SUP_INDEPENDENT_20261013.md)直接核两原件必要section及上述日期角色，通过本有限signal层；不再待独核或重复读取。没有formal/评分/Books正面采用，本包不代完整DAY，作者不自签。
