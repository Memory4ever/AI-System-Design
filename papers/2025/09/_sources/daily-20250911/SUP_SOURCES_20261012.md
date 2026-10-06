# Sep11补Sep10：每日来源有限检查

作者Schrodinger；执行2026-10-12 BJT。新补2025-09-10完整自然日，不catchup/小时、Weekly、2026或全年度目录。每个`SUP_<name>_20261012.request.json`保留实际URL、method/query/body、UTC执行时间、status、bytes/SHA及同名raw；正文按这些原件实际读取。旧有效原件只作具名身份/停止复用，不拿旧完成标签作本轮结果。

## 十四来源与真实停止

| ID | 实际入口/主题/分页与停止 | 本轮结果与权限限制 |
| --- | --- | --- |
| SRC-OPENAI | `SUP_openai`官方news RSS，1287 item全部日期/相关title读；Sep9 SafetyKit、Sep11公告夹住Sep10 | 有限RSS已检查，无该feed Sep10相关事件；不是全部删除/未列研究证明 |
| SRC-ANTHROPIC | `SUP_anthropic`Research RSC解析174唯一publication，publishedOn/相关title读；Sep5→Sep15两条 | 该有限目录无Sep10条目；174库存不作全文队列，旧172计数只是历史 |
| SRC-GOOGLE-AI | `SUP_google-month`→`SUP_google-month2`实际Sep2025 blog1→2/2，12+1=13，Sep30→Sep11→Sep9；DeepMind `SUP_deepmind5`24卡Nov→Jul，六Sep卡有限主题查漏。旧有效Sep17/22/25三原文日期复用；新VaultGemma原稿`SUP_vaultgemma-date`paragraphs8–10为Sep12。fluid/universe两个科学标题明确范围EX，日期不影响关闭，无需科学全文 | Blog有限切片已检查；月标签不是精确日。Google Pubs `SUP_google-pubs`首页775页/可见year与theme filter，不能作全年queue；补检实际两查询 `site:research.google/pubs "September 10, 2025" (language model OR transformer OR inference)`与同义`"2025-09-10"`仅有限搜索线索，没有必要公开日目录，不授Pubs无漏。SimpleQA具名原发布通过日期，不依赖Pubs搜索 |
| SRC-META-AI | `SUP_meta-results5`真实publication results page5 Nov18→Sep15，`SUP_meta-results6`同type=publication page6 Sep8→Sep2→Jun13，相关title/date实际读；旧Blog1→3及旧非作者page6有效观察按同身份复用 | 实际两个publication页跨窗停止，不用错误generic page6小响应作0；pin/非严格顺序不授全历史 |
| SRC-QWEN | `SUP_qwen`完整config中精确Qwen3-Next title/id/date/tokenLinks对象字段同旧；`SUP_qwen-next`200/101627 bytes与旧官方token正文逐字相同。ASR Sep8、Next原UTC Sep10T20/BJT Sep11 | 旧候选/publicdate/三图/Ch22有限机制证据分别复用；不搬Next到Sep10，不重计新family；没有新的本窗配置事件 |
| SRC-DEEPSEEK | `SUP_deepseek`官方更新表Sep22/29→Aug21，实际title/date | 本窗口更新切片已检查，无该表Sep10；不扫所有repo |
| SRC-MOONSHOT | `SUP_moonshot`实际有限26项，Sep16→Sep5日期/相关title | 列表跨窗停止；无具体本窗release触发，不枚举GitHub全部artifact |
| SRC-TENCENT-HUNYUAN | `SUP_hunyuan`Research shell→实际正确host POST publicList pageNum1/pageSize1000/renderType0，`SUP_hunyuan-list`EN9/total9；必要`accept-language:zh`的`SUP_hunyuan-list-zh`11/total11全部id/title/displayPublishTime转换BJT Feb3→Sep22 2026 | EN不能替全部ZH，双语不计20独立事件。当前有限11家族是2026，不授2025历史；旧浏览器恢复失败只历史观察。历史全部目录本窗片段仍受阻，已穷尽本接口当前语言返回，不扫2026正文/全部repos |
| SRC-ZAI | `SUP_zai`RSC `blogsItems15/nextPage2/hasMoretrue`→`SUP_zai2`累计18/nextPage3/hasMorefalse，实际全部id/title/createAt；尾3为Dec2025且非严格排序，未跨Sep2025。`SUP_zai-notes`当前仅Models docoverview | 页2有真实3条差额，不称两页同18。Research历史Sep10未恢复；旧release-notes Sep30/Aug日期层保留，不冒当前page事实，不授Coverage0 |
| SRC-BYTEDANCE-SEED | 官方论文/Blog shell→US locale真实get_article_list_v2，publish_year2025/count20/order_desc=true；type1 `SUP_seed-paper-us`page0返回18/total94/next20/more，page20 `SUP_seed-paper20`返回20/next40/more；type2 page0 `SUP_seed-blog-us`18/total45/next20/more→page20 `SUP_seed-blog20`18/next40/more。所有返回title/publishedDate原值读并转BJT，paper非pin Sep22→Sep2/1，blogOct23→Aug21，再两页到Jun/May及Jun/Feb | Sep10相关切片跨窗有限停止，不说hasMorefalse/94或45全部读。Seedream pinned Sep9不独立作为停止依据；论文旧缺数组已实际恢复，不继续沿旧type1 hold；没有本窗条目 |
| SRC-BAIDU-ERNIE | `SUP_ernie`→`SUP_ernie2`真实blog1→2/2，Sep12 PLAS→Aug14 FastDeploy→Jun30 | 日期/相关title有限读完，不扩ERNIE所有repo |
| SRC-XIAOMI-MIMO | `SUP_mimo`首页8paper/15blog；实际runtime route registry `SUP_mimo-main/index`，landing `en/index.mdx`8557+shared6159原件已读。Paper8 dates完整，Sep19Audio↔Jun4VL无Sep10。8557 Blog15数组、initialVisible8；6159两slice8+7已全部map，More只state toggle，无网络分页。`/blog/`127→62150/7210是产品长正文，非目录，身份误路已纠正 | More普通恢复已闭合，不再标“More未读”。15blog目录自身无日期且2025删除历史不可恢复；隔离历史datedBlog缺段，不授全历史无漏。不读2026正文/全chunk；runtime metadata既有Dec2025/2026字段只日期识别 |
| SRC-MINIMAX | `SUP_minimax-en`12卡末Oct27、CN13卡末Jan15；EN `SUP_minimax-en2`same12无历史恢复。`SUP_minimax-agent`当前三TechBlog标题2026Oct8/Sep22/Sep19；必要`SUP_minimax-agent-index`官方llms.txt完整索引只这三TechBlog，无另旧历史entry | CN有限切片跨窗；EN/pagination/Agent Sep2025历史仍受阻，不能由当前同页/索引说0或不存在。不读全部产品docs、仓库或2026文章 |
| SRC-ARXIV | capture helper四明确主题model/system/LLMagent/multimodal限定12类；新submittedDate UTC202509091600～202509101559，每组start0/max150/total=returned55/22/25/47，149出现/114唯一，无tail页；精确v1 114完整AB已读。旧有效256 ID带标题及有限月列表仅查漏/日期恢复线索，不扩全类 | submitted不等公开。当前`SUP_arxiv-day`实际429/14bytes Rate exceeded；export同日期URL实际400/7392bytes，提示subject/time-period参数无效，不能当已确认正确day-list的空结果。旧实际有限月入口不能给精确首公开日、截断/失败及DataCite/API不等first-public的限制复用，不重扫整月。SimpleQA作者原发布独立补足日证；余潜力按精确日期请求隔离，不把全源判0或未审全文称完成 |

## 触发与遗漏权限

没有扫描Weekly组。确实发生的必要原件触发：SimpleQA作者/官方Kaggle具名首发、当前google官方HF dataset单行纠错；四新安全核心和当期算法争议；精确先稿身份PMLR/OpenReview、ExRAP NeurIPS2024及TA-VLA作者项目；09723当前withdrawal和19648重叠说明。仅服务这些family，不由链接扩全部会议、评审、LinkedIn、HF或代码history。

机构可用有限slice已实际读；Pubs、Hunyuan2025、ZAI2025、MiMo历史datedBlog、MiniMax EN/Agent历史与arxiv官方Sep10批次不支持正面Coverage或无漏。恢复需相应历史主题/日期列表或具名作者原发布；新材料到达只重开受影响源/家族。可访问且尚未读的必要位置不是这些保留项，本轮普通Books协调和DAY仍继续。
