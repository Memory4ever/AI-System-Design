# Hunyuan / GradLoc 本日精确日期核验

本日窗口：2026-02-12T09:00:00+08:00 ～ 2026-02-13T09:00:00+08:00。

官方动态详情页 `https://hunyuan.tencent.com/research/100015` 的浏览器恢复多次超时；没有把空页面称为正文已读。已公开页面所链接的官方静态 JS 仅作为只读接口定位：`index-I3I3bCf9.js` 给出生产域 `https://api.hunyuan.tencent.com`，detail route 关联 `index-DnHw8aHy.js` / `index-cEoitnb7.js` 给出 `/api/blog/publicDetail` 及 `{id}` 请求。未执行下载的 JS。

实际只读查询 `POST https://api.hunyuan.tencent.com/api/blog/publicDetail`，JSON `{"id":100015}`；HTTP 200，code=0。响应 data.detail 字段原值：

```json
{"id":100015,"title":"Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping","status":2,"publicVisible":1,"publicAt":1770971794,"createdAt":1770209041,"updatedAt":1770971794,"publishedAt":1770971794,"displayPublishTime":1770971794,"publishVersionId":"d67dsus2c3m0lbl55udg"}
```

四个一致公开/显示时间字段转为 UTC 是 `2026-02-13T08:36:34Z`，北京时间 `2026-02-13T16:36:34+08:00`，晚于本报告截止。createdAt 是 `2026-02-04T20:44:01+08:00`，不是首次公开。故本博客事件不列本窗候选、不评分、不用其正文为本窗 Books 正面证据；归属后续真实窗口恢复。获取响应不等于已做正文方法审阅，日期已足够关闭本事件。

同响应相邻旧条目 id=100025 “Learning from context is harder than we thought”：displayPublishTime/publishedAt/updatedAt=1770092288，即 `2026-02-03T12:18:08+08:00`。本次只取相邻日期作为研究目录有界停止辅助，不审其旧日研究池。其他迁移条目 createdAt 与 displayPublishTime 可能不一致，因此没有用内部创建时间替代所有材料首次公开。

GradLoc GitHub 的普通 README 更新提交只支持 artifact 修改事实，commit created 不等于首次公共 push；本轮未将普通 README 更新自动视为重要修订，也没有据其扩扫历史版本。
