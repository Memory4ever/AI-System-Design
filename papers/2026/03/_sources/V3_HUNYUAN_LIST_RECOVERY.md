# 混元 Research「全部」目录恢复

检查时间：2026-10-01（Asia/Shanghai）。root 只读访问；不证明目录从未删除条目或所有历史公开时间。

`https://hunyuan.tencent.com/research` HTML 是空壳；root 浏览器创建也在30秒超时。官方页面引用
`https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-I3I3bCf9.js`，其中 Research 路由加载
`index-CUQAWQeM.js`，后者的目录调用由 `index-cEoitnb7.js` 定义为 `POST /api/blog/publicList`；主脚本的生产 baseURL 是 `https://api.hunyuan.tencent.com`。

按页面实际参数只读查询 `https://api.hunyuan.tencent.com/api/blog/publicList`：
`{"pageNum":1,"pageSize":20,"renderType":0}`，请求头 `Content-Type: application/json`、`accept-language: zh`、`Origin: https://hunyuan.tencent.com`。
响应 `code=0`，`totalNum=11`，返回11项；`renderType=0` 是页面“全部”分支，当前公开目录本页已读完，不需要把普通GitHub活动扩大成第二个目录。

下表保留实际原值（epoch秒），而非猜测首公开时刻。目录显示日期与 `publishedAt` 有不同语义：例如 Hy3 preview 的显示日期为4/23而当前 publishedAt 在6月，不能将后者当作该研究的首次公开日期。对3月检查而言，下列目录条目的显示日期和当前publishedAt均无3月值；这只支持当前目录中没有3月条目，不证明全机构历史无遗漏。

| ID | 标题 | publishedAt | displayPublishTime |
| --- | --- | --- | --- |
| 100119 | Hy Image3.5 preview 发布：为专业创作提供高性价比模型 | 1789959110 | 1790006400 |
| 100116 | 当大模型强化学习走向规模化，Batch Size Scaling 有什么不一样？ | 1789749798 | 1790006400 |
| 100100 | Hy4 preview 发布 | 1787896648 | 1787846400 |
| 100091 | From LR to ELR: A Better Heuristic for Pretraining Dynamics | 1786592588 | 1786377600 |
| 100087 | Hyra: 简单有效的科学发现智能体 | 1784110327 | 1784599200 |
| 100064 | Hy3 正式发布 | 1782959528 | 1783320600 |
| 100041 | Hy-MT2：面向实际应用场景的高性能多语言翻译模型 | 1779340747 | 1779346800 |
| 100039 | Real life is where context gets hard | 1777228775 | 1777532400 |
| 100061 | Hy3 preview : 混元大模型重建的第一步 | 1782308557 | 1776873600 |
| 100015 | Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping | 1770971794 | 1770971794 |
| 100025 | Learning from context is harder than we thought | 1770092288 | 1770092288 |

3月邻接显示条目为2/13（100015）与4/23（100061），二者均不落入3月任何Daily窗口。未打开这些窗外全文，也未评分或新增Books。各日只有在限定本日窗口对读上述原值后才能引用这份原始来源记录，不继承其他日报的判断。
