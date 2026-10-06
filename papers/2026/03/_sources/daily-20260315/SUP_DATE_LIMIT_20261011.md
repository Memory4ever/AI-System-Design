# 本日公开日期恢复的权限边界

2026-10-11实际官方advanced HTML路径：https://arxiv.org/search/advanced 。公开form实读行447–458含三个date filter：submitted_date（most recent）、submitted_date_first（original）、announced_date_first（Announcement date）；帮助文本明确announcement只支持year/month粒度。行554说明按announcement排序取original v1的年/月。不是能以Submitted替代公开day的接口。

实际官方月列表请求 https://arxiv.org/list/cs.CL/2026-03?skip=0&show=2000 返回2138总数与1–2000页，但web本轮可见片段只到开头两条，未实际读2千标题；相同官方月列表的skip800/show200请求cachemiss，缺本窗相关历史slice。此结果仅恢复有效monthly入口，不能说无日档即无论文，也不创建全月逐项关闭任务。

三个具体v1原页12529/13423/13426只显示Submitted3/13；完整题摘已读，原证SUP_AB_SAMPLE_20261011.txt。辅助旧march-2026-arxiv-announcement-recovery.json.gz定点三行：12529派生3/16、13423/13426派生3/17。该旧映射由DataCite创建/registered+官方slot派生，并非本轮实际逐日公告原证，保留线索性质，不当当前日期验收。当前DataCite单DOI web不可访问，也不会无限重试。

官方availability无Friday/Saturday regular announcement（BJT3/14为周六）已实际读，其通常相邻3/13与3/16的公开日只能限定常规公告。作者另处原始公开/异常事件未由此证明为0。三potential必要门是可核first-public公开日或本窗作者原event，不要求精确时刻；当前均隔离且不支持确定候选、Books或覆盖无遗漏。
