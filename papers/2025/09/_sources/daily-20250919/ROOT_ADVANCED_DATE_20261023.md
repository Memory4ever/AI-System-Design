# arXiv Advanced 的公告日期只有年月精度

作者明确单让Advanced参数语义/SAIL14033正控首准备，root接受；作者与reader不并行本域。不使用catchup，不重DataCite/公告日程、池或Methods。以下为本次实际查询和原始依据，不将旧空结果补写成成功。

## 已有记录实际核对

本日旧`SUP_arxiv-announced_20261012.request.json/raw`是all-language-model/CS-crosslist、announced_date_first、Sep18→19；HTTP200并确有“query returned no results”。旧15个paper_id OR corrected查询同样实为成功列表，但只显示originally announced September2025。第一份OR字符串错误的identity查询不替正确查询，既存raw不删改。

## 本轮实际验证

1. 只一次精确已知SAIL`2509.14033`，保持旧日期条件Sep18→19/announced_date_first，GET200/10719B/SHA `3f23ec6440d3f9f3db647ce6944d716cafec85a349a55c1d0f1632fce3e1939a`，仍为真正no-results。原件`REPAIR_ROOT_ADV_SAIL_POSITIVE_20261023.raw/request.json`，请求2026-10-23T15:31:16.000191Z，真实exit0。本日已有作者Sep18公告/精确身份有效，不第三其Source或全部发布日期。
2. 实际完整读当前官方Advanced表单的日期区及说明：`https://arxiv.org/search/advanced`，GET200/28653B/SHA `9486eb8cf37682f634e46fff0bc6e196ac2fd6927d0f0d4218ae5bc6fa9703b3`，原件`REPAIR_ROOT_ADV_FORM_20261023.raw/request.json`。467行明确 **“announcement date supports only year and month granularity”**；563行明确排序使用v1公告的year/month。输入from/to允许YYYY[-MM[-DD]]，并不使所有date-type都拥有日精度。当前表单反映当前查询能力，不假装是2025网页快照。
3. 官方`arXiv/arxiv-search`只为解释该参数读取一次tree及三个必要文件，固定树SHA `f53ed1707d80a877e72ec989b2156c2e7bb01d87`，不是拉取完整仓库或检查私有生产索引。tree原件`REPAIR_ROOT_ADV_TREE_20261023.raw`。官方代码[DateForm](https://github.com/arXiv/arxiv-search/blob/f53ed1707d80a877e72ec989b2156c2e7bb01d87/search/controllers/advanced/forms.py#L195)重复同一精度说明；[_date_range](https://github.com/arXiv/arxiv-search/blob/f53ed1707d80a877e72ec989b2156c2e7bb01d87/search/services/index/advanced.py#L61)对ANNOUNCED使用`%Y-%m`，其它日期用完整timestamp，lower为gte、upper为lt。同月的两端转换后可以成为相同月份而形成空范围。原件`REPAIR_ROOT_ADV_FORMS_20261023.raw`8943B/SHA `f252505002fba31e1d95d4d1d8bc0ce8fbf19721b212cdc87cec22e6f8419c9c`；`...BUILDER...raw`4095B/SHA `a3c69622aaefcc28fcb293dcef5f31ae4bf1e70c9b6da3c3852f57e14223f08d`；`...DOCUMENT...raw`3760B/SHA `93e6dc198aa356642546581f92048fd2fce8c74edafd3843732d2f19aee09f74`。请求均实际exit0，bytes/SHA/时刻各在同名request。当前代码与live表单相合，但未取得生产build SHA，不把当前develop当2025部署版本。

## 修正范围

**本日旧按日Announcement空查询不能提供日级零命中、无遗漏或日期缺口已穷尽的证据；精确SAIL正控同样失败，且官方表单明确只有年月精度。** 官方代码解释这种表现，不从这次观察声称所有空响应同一原因。月份精度是入口能力限制，不证明2025年论文公开日期永远不可恢复，也不授Submitted或DataCite created为公开日。

本轮正确submitted代理主题发现、完整题摘、组合日界及直接作者公告等既成有效层不被推倒；仅改该错误查询的能力/覆盖解释，不扩大月度库存逐项筛选，不重复整池/Methods，不重做原公告与DataCite规则。已有候选日期/评分/原窗口不改；未入选且日期跨日的材料仍需其具名可用证据，不能因该公共入口失败把79+23全部改终态。后续各日若继承同一按日Announcement空查询，只复用本参数语义修正其具体覆盖声明，不将其空结果当日期证据。

交本日不同角色只一次实际采用live日期说明、精确正控响应及必要代码段；未采用前不自签来源Gate/DAY，不要求第二人重取原件。此次不修改公共合同/Books，也不顺带修改其他日期的报告。
