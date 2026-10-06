# 2026-03-06 补查：官方 API 停止范围

本轮只补 BJT 2026-03-05 自然日；不改变原窗口或候选日期。下列为本轮真实获取，不把站点当前目录等同整个历史。

## Qwen

GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`。原始响应 [SUP_QWEN.raw](./SUP_QWEN.raw)，40 个 `data.articles`，逐条题名及 `extra.date` 检查；邻接 February 16 Qwen3.5 → March 19 Qwen3.5-Max-Preview，无 March 5。响应没有提供本轮继续分页 token；停止此可见返回，不猜测隐藏页。

## Seed

GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false`。原始 [SUP_SEED.raw](./SUP_SEED.raw)：14 行，total82、has_more=true、next_page_token=40。逐行将 PublishDate 毫秒转 BJT（UTC+08:00）：Feb27 CUDA Agent/Steerable Instruction、Mar01 How RL Unlocks Aha/Learn the Hard Way → Mar12 Permutation，再至 Mar26。没有 Mar05；停止 next40，不读全年82。列表日期只用于目录筛选，不代替所链论文 first-public 日期。

同端点 `article_type=2&publish_year=2026&page_token=0&count=100&order_desc=false` 原始 [SUP_SEED_BLOG.raw](./SUP_SEED_BLOG.raw)：9 行，total23、has_more=true、next20。BJT 为 Feb12 Seedance2、Feb13 Seedream5 Lite、Feb14 Seed2 → Apr01 recruitment、Apr09 Full-Duplex，随后至 Jul08。停止 next20；邻接覆盖目标日但不证明未列/删除内容不存在。早先临时 UTC 显示 Feb28/Mar11 不能作为本日停止依据；这里采用实际 +08:00 转换，不改旧候选日期。

## Hunyuan

补核（root，2026-10-09）：同一Seed论文请求增加 `x-tt-locale: US` 后实际返回18条，total82/next40/has_more true；BJT目标邻接为Mar01、Mar02、Mar12，仍无Mar05。默认locale的14条是真实返回但不是所有语言可见条目，不以14条推零历史；仅采用本日目标段有限检查。

POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":20,"renderType":0}`，headers Content-Type application/json、accept-language zh、Origin https://hunyuan.tencent.com。原始 [SUP_HUNYUAN_LIST_ZH.raw](./SUP_HUNYUAN_LIST_ZH.raw)，code0、totalNum11、list11；一页即全部当前返回，无续页。

实际逐行 BJT 对读：

| ID | 标题 | publishedAt | displayPublishTime |
| --- | --- | --- | --- |
| 100119 | Hy Image3.5 preview | 2026-09-21 | 2026-09-22 |
| 100116 | Batch Size Scaling | 2026-09-19 | 2026-09-22 |
| 100100 | Hy4 preview | 2026-08-28 | 2026-08-28 |
| 100091 | From LR to ELR | 2026-08-13 | 2026-08-11 |
| 100087 | Hyra | 2026-07-15 | 2026-07-21 |
| 100064 | Hy3 | 2026-07-02 | 2026-07-06 |
| 100041 | Hy-MT2 | 2026-05-21 | 2026-05-21 |
| 100039 | Real life is where context gets hard | 2026-04-27 | 2026-04-30 |
| 100061 | Hy3 preview | 2026-06-24 | 2026-04-23 |
| 100015 | Stabilizing RLVR | 2026-02-13 | 2026-02-13 |
| 100025 | Learning from context | 2026-02-03 | 2026-02-03 |

无 Mar05 行；两日期字段不互当 first-public，也不对不影响本窗筛选的不同日期扩大恢复。旧空壳和本轮浏览器访问超时已由上述实际公开 API 有限恢复，不继续当永久缺口。
