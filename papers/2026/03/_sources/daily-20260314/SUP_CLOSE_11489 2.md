# AutoVeriFix+：必要core / 局部增量最低关闭提案

仅03-14补Mar13 BJT，准备者mar14_supplement。11完整Atom题摘独核复用。实际exact-v1完整ABS/Comments（text overlap2509.08416）与同四作者旧2509.08416v1完整官方AB实读；当前B31明确扩展旧two-stage，不以admin overlap当抄袭/自动EX，也不说全文没有增量。旧AB只有Python reference→RTL/differential repair；当前新增Stage3 branch-ID/每clock register state反馈、concolic输入与coverage-driven trial-pruning，识别为重要扩展事件需保当前受影响证据，不把旧first-public迁到Mar13。旧全文/所有revision不读。

**拟窄P、1+1+2=4最低关闭/仅报告Books0。** 原black-box mismatch不够定位时序错→CFG branchID+cycle register snapshot绑定指定失败输入/expected/observed→局部trace-debug输入配方。Design1只计原文当前新增的反馈表示/循环；concolic原算法明确继承[28]，不借solver、分阶段或oracle优越性加分。Reach1限定RTL生成组件，Durability2为可复用的受限debug接口；不是领域名、模块数、旧两stage或Books覆盖导致EX。

实际当前必要原证B1–100（Stage1/2及instrumentation）、B129–137（concolic接口）、B135–215（测试/trace/pruning及必要oracle反侧）、B267–293（I/O-vs-trace受控比较与FPR条件）已读；本次没有读全代码/全Tables/全部Fig图像。B178–190 debug prompt含current code、failure test/expected/observed、每clock触发branch及state；repair后重建Full Input再验。§IV-D局部matched去Trace反馈基线RTLLMv2 pass@1 74.6→79.0支持该受测反馈增量，不把4.4点解释为内部因果识别/所有场景必有效。

Python reference并非独立规格真值，作者自己§IV-E承认非100%正确且通过testbench仍有false positives。FPR分母为通过differential的design而非所有任务；RTLLMv2作者2%不是零错误certificate。B193–195 solver timeout/state explosion可把合法branch标potentially unreachable，trial deletion再跑同有限oracle/input suite不证明defensive FSM/default全状态语义保持；“ensures no false deadlogic removed”强保证不能采用。这里直接核安全/正确性相关受影响内容，不借“coverage≠correctness”成熟原则算新增重要机制。Figure11全部代码/完整formal验证不需要也没有核验；作者未给safe-pruning独立证明或生产芯片安全。

## 日期 / 家族边界

SUP_CORE_EVENT_REM11_MANIFEST_RESULT.json：2026-10-10T03:16:38.916602Z exactDOI GET20010616B。SUP_DATE_REM11_11489.raw真实ID/URL、owning arxiv.content/findable/全部dates：SubmittedMar12T03:15:57Z、UpdatedMar13T00:21:11Z、Available2026-03/Issued2026，RegisteredMar13T01:56:44Z。复用有效正常公告下界与官方ID不可预分配/owning公开上界同Mar13BJT，当前arXiv事件日成立，不单拿Submitted/Registered/Updated当公开。旧2509.08416v1已公开正文是具名家族先稿；本稿是作者明确的Stage3扩展，不称Mar13首次论文。不遍历旧全文，无强无早稿声明。

本次仍须非准备者actual原证/日期/最低处置独核后正式。若报告计当前扩展家族，只计一次，旧家族不重复评分；不制造新Books缺口，不签生产正确性/全state equivalence或DAY。首次helper调用错误把repo相对路径再拼ROOT，零请求本地FileNotFound，检查helper实际参数后改为manifest basename，5精确GET均成功；不是官方来源外部受阻。
