# 混元本轮有限目录原字段

执行2026-10-12T10:06:58Z，窗口仅03-25BJT。官方Research动态入口CLI先恢复其官方bundle，实际loader `/blog`→`index-CUQAWQeM.js`→`index-cEoitnb7.js`，后者公开调用 `/api/blog/publicList`；主bundle请求base由Ji映射hunyuan.tencent.com→api.hunyuan.tencent.com。不是猜API或继承旧9项标签。浏览器两次timeout与visibility不支持不当页面核验成功。

实际POST `https://api.hunyuan.tencent.com/api/blog/publicList`，Content-Type application/json，accept-language zh，X-Source web，body `{pageNum:1,pageSize:20,renderType:0}`，HTTP200/code0/data.totalNum11/list11；相同参数pageNum2，HTTP200/code0/totalNum11/list空，停止。Research使用displayPublishTime优先、其次publishedAt、createdAt的展示规则在实际chunk确认；展示与publish不互代首公开。

| id / title | publishedAt原秒 | displayPublishTime原秒 | 两字段BJT日 |
| --- | ---: | ---: | --- |
|100119 Hy Image3.5 preview|1789959110|1790006400|09-21/09-22|
|100116 RL batch size scaling|1789749798|1790006400|09-19/09-22|
|100100 Hy4 preview|1787896648|1787846400|08-28/08-28|
|100091 LR→ELR|1786592588|1786377600|08-13/08-11|
|100087 Hyra|1784110327|1784599200|07-15/07-21|
|100064 Hy3|1782959528|1783320600|07-02/07-06|
|100041 Hy-MT2|1779340747|1779346800|05-21/05-21|
|100039 Real life context|1777228775|1777532400|04-27/04-30|
|100061 Hy3 preview|1782308557|1776873600|06-24/04-23|
|100015 RLVR gradient/layer clipping|1770971794|1770971794|02-13/02-13|
|100025 Learning from context|1770092288|1770092288|02-03/02-03|

均2026，全部11原title与两字段实际对读；无03-25显示/publish项，无相关纠错/撤回信号项。可称当前公开Research全返回范围本日未发现新增事件，不宣称已删除历史项/全机构无遗漏，不扫描窗外核心或历史release。必要性不依赖createdAt，因此未把后台创建当公告。
