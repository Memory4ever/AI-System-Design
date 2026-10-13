# RSP v3.1 / 04-02 Roadmap：受影响版本审阅

作者 `supp_apr03_20261013`；本文件是必要 Source 与拟 Books 裁决，不是独立验收。

## 事件、版本与停止

官方 [RSP Apr02日志](https://www.anthropic.com/responsible-scaling-policy)明确当日更新3.1；[v3.1干净PDF](https://www-cdn.anthropic.com/files/4zrzovbb/website/bf04581e4f329735fd90634f6a1962c13c0bd351.pdf)封面标Effective April2、p19自带同日日志，官方承诺公开不晚于生效（p15§4.7）只能辅助不晚于日值，不虚构公开时刻。自然日补窗不需要旧09:00门；旧§5请求仍原样保留并由增量处理覆盖其必要日级部分。

已读受影响p8阈值与脚注、p12§3.4 review/approval、p15 AppendixA开头、p19当次changelog；[官方redline](https://www-cdn.anthropic.com/files/4zrzovbb/website/64cb0ac5eb0f8030187131f490827323e3d53308.pdf)的相同受影响文本辅助定位，不把flattened redline旧/新混排当干净正文。截图接口返回空引用，未取得可检查图像，不声称视觉diff核验；clean v3.1和明确changelog已经支持以下范围，无需遍历20页、全附件或代码。

## 实际增量和反侧

1. p8 Automated R&D：阈值(2)的估计对象是AI总体能力进展率，并需其加倍可合理归因自动化研发/工程，而非增加headcount、compute或一般productivity。脚注用原本一年9×effective scaleup、加倍进展变81×举例，明确不等于研究者产出翻倍。它澄清版本合同，不证明现实中的加速已发生，也不提供测量算法/置信区间。不能用某次研发人员效率数字自动断言触发阈值。
2. p12§3.4：内部反馈用于指出方法弱点、分析缺口或缺证；可据此改善报告，Report与反馈交CEO/RSO，最终判断仍由其作出，并向Board/LTBT共享。p19将internal feedback明确列为当次修订，HTML短日志只列另两点，因此以精确PDF为准。不把反馈征集等同独立批准、外部审查完成或证明风险已低。
3. p15 AppendixA开头：competitor-contingent commitments不排除其它情况下自愿停止训练/部署。它保留谨慎措施的权限，并非当次恢复一条所有阈值触发即强制pause的新承诺；不能把未触发AppendixA理解为必须继续，也不能把“会认真考虑”改成已暂停。
4. [Roadmap archive](https://www.anthropic.com/responsible-scaling-policy/updates)明确Apr02版已选并开始两个moonshot项目：极端安全基础设施的小尺度原型探索（phase1原May15）与权重归属的provable inference原型（Sep30目标）。内部retention报告完成日Mar29在Apr02公告；这不证明部署了新retention政策。May5改期/Jul修订不回填。这里只支持公司自述的goal状态和计划，未披露实现/实验，无安全保证。

## 拟评分、结论与 Books

拟 `2+2+1=5`：评分仅对阈值估计对象与该版本risk approval/pause边界的澄清；不为借用成熟治理原则加长期基础分。虽5分，因安全/实际版本修正，必要受影响内容已深入读取。RSP/Roadmap为一个官方policy家族的两个关联当日事件，不数成两个独立家族。

拟 `仅报告`，Books新写0。已读取ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE，以及PLATFORM-PRODUCTION Ch73的具体production contract、readiness、事故后freeze/mitigate/rollback与相邻Ch74交接；没有把整套RSP移入平台书稿。此次证据支持的是Anthropic的精确定义/承诺澄清和研发目标状态，未提供新的可验证通用治理执行机制或风险测量方法；把公司具体deadline/组织权限写成全平台必需，会越过证据范围。此处不是声称Ch73主题相似就已有覆盖；未来若其估计器或provable-inference具体机制公开，再按真实新事件定位唯一owner。

## 非作者 Source / Books 独核回执

root 于本轮实际独读官方 clean PDF：p8 行350–427核 aggregate progress 9→81、非 productivity；p12 行534–549核 internal feedback 与CEO/RSO最终批准，marginal case另需Board/LTBT；p15 行658–671核公开不晚effective及未触发也可谨慎pause；p19 行806–813核三项修订；archive 行35–44核April2原May15/Sep30目标并与May5变更隔离。非作者裁决：Source通过，`2+2+1=5`与仅报告通过，可正式新增一个家族的两个关联事件、Books0。此回执不冒称DAY或完成态独核，不声称空截图响应为visual pass。
