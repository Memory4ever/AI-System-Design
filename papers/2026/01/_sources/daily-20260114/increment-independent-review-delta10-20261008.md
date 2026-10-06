# Jan14 PlaM 独立必要终判 delta10（2026-10-08）

复核者：review_jan15_delta（非作者）。root在delta9后明确单独授权07645必要标准源/actual owner终判，不等作者prepare；作者停止重复准备，仅报告/Books写入仍归作者。本轮只07645，不扩全附件，仍BJTJan13完整自然日补窗/原17与窗口保留。未写Books/Report/LS/索引、未stage/commit/push，无DAY。

完整AB本日五份increment-abstracts对应行实际读，潜力准入复用root校准并确认：视觉读入的cut-layer干预所示plateau，用来缩窄base-LM与MLLM合并的位置，相对uniform early/mid/full merge改变了实际参数选择；不是只有视觉任务与merge主题关联。评分2+1+2=5、标准审阅，不由Only反推降分。

## 必要证据与身份

独立原证保存 [PlaM必要原文](./increment-independent-plam-necessary-20261008.json)：官方exact-v1 HTML §3–6/限制；原HTML纯文本漏掉mask处的<k之后部分，已由官方PDF第3页补齐；HTML Table1只有caption，已实际读PDF第6页全数；第13页Table2核best超参/尺度。未读整份附件或将inventory当实际阅读，不采用全部mask曲线/案例为因果证明。

日期复用本日已核公告/正式ID界，读increment-date-bounds-rest对应行v1 UpdatedJan13 02:29:13Z→registered04:07:51Z；归BJTJan13，不以Submitted/registered独证。独立轻读当前officialabs：v1 / under review，未见明确撤回/纠错说明；不比较全历史。

## 5 / OnlyReport PASS

§3的cut k只在l≥k移除visual位置作为attention K/V的读入口，保早层正常融合与text pathway；早层已写入text state的视觉信息仍在。它不是从原始输入拿掉图片、冻结visual update、证明整个模型不依赖图像，亦不授权缓存或永久剪枝。§5.2据性能–k曲线plateau邻近搜索k0，然后只合并k0到最后层的Q/K/V/O，同backbone/architecture的base-LM与MLLM权重按λ1/λ2组合；encoder/projector固定。Merge新artifact与诊断mask是两种操作，不宣称部署必须保持mask。

Table1给有限正面支持及替代反侧：LLaVA的PlaM MMStar35.29 vs33.77、RealWorldQA56.34 vs56.08；full-layer MME_P1396.5884低于base1516.0553，晚合并为1522.4614。其他模型/任务也有局部改善，但§4与Table2是每model-task最佳超参，不能当单一部署配置全5×9保证。GQA/POPE仅小幅改善、不同merge分支结果非单调；未披露多seed或不确定性，不由小数优势签普遍质量。正文称grid[0,1]，§3范围[0,1.5]、Table2有λ2=1.3/1.2等，不能暗修完整搜索recipe；λ1+λ2并未要求1，不能当标准convex averaging。

Late visual-read mask的plateau不唯一识别语言能力受损或已恢复；attention mass/所选heatmap与结果关联不能证真实grounding、因果功能恢复或充分视觉知识。作者§6自身承higher vision attention不是reasoning quality保证。Adopted statement仅限stage-guided参数合并的局部替代，未以恢复性语言作为正证。Per-task k0/λ校准、每层mask评测、两checkpoint装载/merge及任务回归都付费；training-free不是全生命周期免费，没有完整search/hardware/precision/延迟预算则不授性能保证。

实际Books判断读Ch23:544–596（截断570后必要内容另完整重读570–590），以及Ch30:413–442、580–627完整局部。Ch23:558–580具体区分stage删除、替换、停止更新但继续K/V读取，582–588将内部sensor与证据/访问权限分开；Ch30:595–627已有同坐标composition proposal、calibration身份、merge后行为回归与回退。这里不冒称现有正文已有PlaM完整cut→merge配方或原数表，也不借主题映射授preciseExisting。

本篇新增的是当前5个checkpoint/任务人口下的plateau-guided late-attention合并与局部验证，而不是已成立的语言功能恢复条件或可迁移merge admission合同；既有read/update/delete及mergeproposal/evaluation长期边界无需增补。故仅报告实际策略/限制与验证，Only不取消贡献、不否定局部正面结果，也不以控制未完美直接贡献前关闭。若后续取得不依赖同一任务择优、清楚披露选择/验证预算的泛化协议或恢复性干预，按实际命题再核，不泛请求全附件。

## 停点

已通知作者/root本项5标准Only终判，可同步；无Books锁或POST。新ready07200/07411另按root授权处理，不由本项通过推其通过或DAY。
