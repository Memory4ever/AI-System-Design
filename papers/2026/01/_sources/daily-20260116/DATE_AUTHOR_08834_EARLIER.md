# 08834 author earlier-publication witness

Actual author page https://github.com/DocTron-hub/FD-RL News lines165–168: `2025.11.26` released paper (linked assets/FD-RL_paper.pdf); `2025.11.17` modelweights. 日期为作者当前明示历史release，不由repo创建/commit推public；日期整天在Jan16窗前，仍须root核当前作者声明/正文同家族权限，不证明具体首次时刻或所有version同一。

Link followed to https://github.com/DocTron-hub/FD-RL/blob/main/assets/FD-RL_paper.pdf . Web raw-PDF cachemiss，有限一次in-memory读取authorraw用pypdf：

URL https://raw.githubusercontent.com/DocTron-hub/FD-RL/main/assets/FD-RL_paper.pdf PAGE1_TITLE_ABSTRACT Reading or Reasoning? Format Decoupled Reinforcement Learning for Document
OCR
Yufeng Zhong∗ Lei Chen∗ Zhixiong Zeng† Xuanle Zhao Deyang Jiang Liming Zheng
Jing Huang Haibo Qiu Peng Shi Siqi Yang Lin Ma ‡
Meituan
Emails: <zengzhixiong@meituan.com, forest.linma@gmail.com>
Project: https://github.com/DocTron-hub/FD-RL
Abstract
Reading text from images or scanned documents via OCR
models has been a longstanding focus of researchers. Intu-
itively, text reading is perceived as a straightforward percep-
tual task, and existing work primarily focuses on construct-
ing enriched data engineering to enhance SFT capabilities.
In this work, we observe that even advanced OCR models
exhibit significantly higher entropy in formatted text (e.g.,
formula, table, etc.) compared to plain text, often by an
order of magnitude. These statistical patterns reveal that
advanced OCR models struggle with high output uncertainty
when dealing with format sensitive document, suggesting
that reasoning over diverse reading pathways may improve
OCR performance. To address this, we propose format de-
coupled reinforcement learning (FD-RL), which leverages
high-entropy patterns for targeted optimization. Our ap-
proach employs entropy-based data filtration strategy to
identify format-intensive instances, and adopt format de-
coupled rewards tailored to different format types, enabling
format-level validation rather than token-level memoriza-
tion. FD-RL achieves an average score of 90.41 on Om-
niDocBench, setting a new record for end-to-end models
on this highly popular benchmark. More importantly, we
cond
PAGE 5 SCORER Format Decoupled Reward.To better guide the model
in learning to parse formulas and tables and prevent the
model from overlooking them in documents with lengthy
text, we calculate rewards separately for different content
types: string matching reward for plain text, expression
correctness reward for formulas, and structural coherence
reward for tables. Specifically, we use regular expressions to
5


标题/作者/项目以及format decoupled reward对象和v1同家族；不是仅weights发布时间。未diff各版本/遍历repo历史，具体score recipe未获新日期证据权限。若root采纳作者所陈2025.11.26正文release，则firstpublic事件至少窗前，Jan16不收此family首次公开；本日已发生Ch31技术整合/实际非作者POST保留为知识已写、Jan16事件归属不能倒填，窗外恢复线索标注而不重跑该日期。作者statement若有回填/链接换版争议，需original dated announcement/archive 或发布时PDF identity重开；不以已写书强授Jan16。

root非作者实际重新打开官方News及当前同typed reward Pipeline，并核保存PDF身份，确认窗前作者正文公开见证；Jan16首次公开事件排除，仅留窗外恢复线索。作者日期精度是2025.11.26整日（时区未明，但整日无论通常时区均远在本窗前），不补造时刻，不以arXiv首次收录另评分；如出现实质修订证据仅定点重开该事件。既有Ch31有效技术段与POST保留，不计Jan16整合。
