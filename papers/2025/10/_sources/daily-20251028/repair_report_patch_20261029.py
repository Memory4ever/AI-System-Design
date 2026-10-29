"""Print a narrow README patch from approved prose; never write the report directly."""
import datetime as dt
import difflib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

sources = Path(__file__).resolve().parent
root = sources.parents[4]
report = root / 'papers/2025/10/28/README.md'
old = report.read_text()
baseline = (sources / 'REPAIR_BASELINE_20261029.md').read_text()
prefix = '../_sources/daily-20251028/'
evlink = f'[必要证据笔记]({prefix}REPAIR_EVIDENCE_20261029.md)'
rvlink = f'[sole实际读点]({prefix}REPAIR_REVIEW_20261029.md)'


class Title(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'h1' and 'ltx_title_document' in dict(attrs).get('class', ''):
            self.active = True

    def handle_data(self, text):
        if self.active:
            self.parts.append(text)

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.active = False


def title(ident):
    if ident == '20963':
        return 'Towards Scalable Oversight with Collaborative Multi-Agent Debate in Error Detection'
    raws = list(sources.glob(f'*CORE_2510_{ident}V1_20261029.raw'))
    assert raws, ident
    p = Title()
    p.feed(raws[0].read_text())
    value = ' '.join(''.join(p.parts).split())
    assert value, ident
    return value.replace('|', '/')


def owner(file):
    t = (root / file).read_text()
    return re.search(r'Stable Knowledge Node ID:\*\* `([^`]+)`', t)[1]


def chapter(file):
    return int(Path(file).name.split('-')[0])


def booklink(file):
    return f'{owner(file)}，[Ch{chapter(file)}](../../../../{file})'


entries = {}
for num in range(1, 7):
    suffix = '' if num == 1 else str(num)
    draft = (sources / f'REPAIR_BOOKS_PRE{suffix}_20261029.md').read_text()
    contexts = json.loads((sources / f'REPAIR_BOOKS_CONTEXT{suffix}_20261029.json').read_text())
    files = {ident: c['file'] for c in contexts for ident in c['id'].split(',')}
    for sec in re.split(r'(?m)(?=^## I\d+ )', draft)[1:]:
        ident = re.match(r'## (I\d+)', sec)[1]
        code = re.findall(r'```markdown\n(.*?)\n```', sec, re.S)
        assert len(code) == 2, ident
        body, note = code
        arxiv = re.search(r'SF-2025-ARXIV-2510-(\d{5})', body)[1]
        file = files[ident]
        t = (root / file).read_text()
        assert t.count(body) == t.count(note) == 1, ident
        score = re.search(r'\d\+\d\+\d=\d', note)[0]
        prose = re.sub(r'\n*<!--.*?-->\n*', '', body, flags=re.S).strip()
        entries[arxiv] = dict(name=title(arxiv), score=score, file=file,
                              claim=prose.split('。', 1)[0]+'。', body=prose,
                              depth='深入完成', decision='整合', evidence='本日exact-v1必要支持/直接反侧与差额采用深入已完成；'+evlink+'及'+rvlink+'保留精确节/图表、配置、反证及未复现范围。',
                              result=f'已真实写入{booklink(file)}；具体段以本节首句定位。I1–I49均已sole actualPOST通过，不行政重存。')

assert len(entries) == 49
tr = 'books/part-04-training-system/'
mm = 'books/part-03-multimodal-world-models/'
ag = 'books/part-07-agent/'
pf = 'books/part-06-ai-infrastructure/'
coverage = [
    ('20963','2+1+2=5',ag+'82-multi-agent.md','标准完成','竞争说服不等协作监督，盲从弱peer可退化。','Peer/Debate及DebateQD已区分个体胜辩/团队judge正确、同源共错与全部调用成本；v1不借v2新题名/扩展，理论Bayes judge条件不授任意prompt。R13/R27实际比较通过。'),
    ('21122','2+2+2=6',tr+'33-grpo.md','标准完成','注入noise的行为policy与clean分母不天然相同。','“On-policy来源不等于Conditioning State一致”及Gaussian elite proposal完整段已承载行为条件/state/可见性与ratio/KL/无偏分责；不采用未闭更新recipe。R27实际通过。'),
    ('21175','2+1+2=5',tr+'30-lora.md','标准完成','低能量更新方向不等严格零空间或旧函数不变。','forward正交补及OPLoRA双侧指定三元组已区分参数约束/函数保持、SVD残差、容量与旧任务回归；有限持续学习结果不新增普遍保证。R27通过。'),
    ('21513','2+1+2=5',ag+'82-multi-agent.md','标准完成','代码候选覆盖增大仍可能让最终selector变差。','同题独立采样/modal bias/oracle覆盖与selector完整论证已承载共同错误和全部费用；100→10并不免前100生成/平方相似度成本。R27通过。'),
    ('21603','2+1+2=5',ag+'76-rag.md','标准完成','文档相关、页面定位与真正layout证据资格不能合并。','文档revision/atomic layout单位及Claim–Evidence/page/bbox/逐hop链和retrieval miss分层已有承载；planner多功能消融不识别单因果，多Agent非必要性定理。R27通过。'),
    ('21618','2+2+2=6',ag+'75-context.md','标准完成','显式fold三JSON不保语义无损，action-mask不等逐call因果credit。','typed retention/raw source authority/三层handover已有精确控制状态与原件回退；工具发现由Ch78、action/token credit由Ch33各自承载，不重复三处整合。R21/R27通过；模拟API非现实权限。'),
    ('21667','2+1+2=5',mm+'24-multimodal-generative-paradigms.md','标准完成','Gaussian velocity读出与uncertainty-guided search不自动保持FM边缘分布。','velocity mixture及随机分支/trajectory身份已区分point mean、概率law与未校准epistemic；统一成本要求N8/16/32全轨迹/CLAP选择费，不采实时或原边缘等价。R27通过。'),
    ('21696','2+1+2=5',mm+'24-multimodal-generative-paradigms.md','标准完成','identity-video缓存复用须匹配目标位置及前背景角色。','source→destination映射段已有source key目标坐标重编码、cache身份、背景替回非像素硬保证及驻留全费；未闭softmax后mask式不补recipe，identity制备不免费。R27通过。'),
    ('21120','2+2+2=6',pf+'66-evaluation-system.md','深入完成','定向safe/unsafe图像pair仍需独立核非目标保持。','ProtoBias具体段已经冻结同prompt干预条件、生成/过滤/独立标注人口；1510pairs中72%未过VQA、过关后23%人审不一致不授真标签。R10/R24实际通过。'),
    ('21144','2+2+2=6',pf+'72-security.md','深入完成','直接把poison放prompt绕过retriever，末代population成功非端到端攻击率。','RAG poisoning正文已固定retrieval exposure/content reasoning/contradiction/non-answer、clean twin与failure taxonomy；IG/GA局部白盒构造不授唯一神经因果或全部90%。R10/R24通过。'),
    ('21180','2+1+2=5',ag+'82-multi-agent.md','标准完成','更一致正向的多角色聊天不等真实人群分布。','RepPop完整段已分代表性与团队正确、agent可达集合与human/synthetic权限；4400聊天非独立社会，VADER/LIWC相关不证明RLHF唯一致因。R10/R24通过。'),
    ('21182','2+1+2=5',pf+'66-evaluation-system.md','标准完成','图谱知识/推理hop重选同时改变知识需求和长度，不能叫去污染证明。','Benchmark generator→过滤→可答/保留集合及SANE段已有变换人口/关系与同源oracle共错；GPT提取/生成/判alias不等独立gold。R11/R24通过。'),
    ('21189','2+2+2=6',pf+'72-security.md','深入完成','word-interleaving混合文本仍可能被重建出危险语义。','“安全检查必须覆盖模型会重建出的语义”与controlled-release段已有guard/generator可恢复性、分母和全部构造/解码费；ASRO/过滤/ASRE不混，“并发”非真计算并行。R11/R24通过。'),
    ('21190','2+2+2=6',pf+'72-security.md','深入完成','先输出unsafe示例再批判不能撤回已交付内容。','Streaming Guard完整sentence最小commit与后段已有未交付尾部修复/不可逆交付边界；99%无拒答非77%语义ASR，v1对近期Claude失败反侧保留。R11/R24通过。'),
    ('21322','2+1+2=5',pf+'72-security.md','深入完成','末层reset/repair后不输出identifier不等从参数删除。','Refusal≠知识删除、minor components及concept suppression完整正文已有行为压制/残留/再学习与旁损；blacklist仍可进context、rare词反增，不授DP或全部抽取免疫。R12/R24通过。'),
    ('21524','2+1+2=5',pf+'66-evaluation-system.md','深入完成','会背规范不代tool argument的行为合法性，丢弃no-call改变分母。','PrincipalHierarchy/task framing及完整subject/analysis-audit分母段已有知识/advisory/action与有效请求分责；60→600改写/10trial非独立规范，全法律认证/真实effect不采用。R12/R24通过。'),
    ('21310','2+2+2=6',pf+'66-evaluation-system.md','深入完成','多样性proposal改变后仍须估原model概率，而非直接用新样本频率。','稀有错误/轨迹proposal已有逐token p/q、支集/权重尾/自适应条件，NLI DAG已有语义proxy及二次费；Eq14/15同权中心化使CV项恒零，不采印刷降方差recipe。R19/R25通过。'),
    ('21323','2+1+2=5',mm+'23-multimodal-representation.md','标准完成','共享稀疏坐标与soft alignment不认证唯一概念或致幻因果。','SAE净化完整段已有配对dictionary、归一code软约束、重建/原encoder分验及全费；VL-SAE连续distance界只在pre-TopK，不能跨不连续TopK继承coactivation。R19/R25通过。'),
    ('21339','2+2+2=6',tr+'31-rlhf.md','标准完成','多轮训练、只末轮credit与多轮推理是不同资格。','多轮Credit/Prefix污染与交互RL/simulator段已有outcome/逐步监督、反馈人口和恢复分责；固定wrong反馈非真人新事实，T0 pass8/每步test与打印式不授普遍human反馈无用。R19/R25通过。'),
]
for ident, score, file, depth, claim, body in coverage:
    entries[ident] = dict(name=title(ident),score=score,file=file,depth=depth,claim=claim,
                          body=body,decision='已有覆盖',evidence='采用exact-v1；'+rvlink+'对应R9–12/R18–19/R24–27给出实际节/行、支持与直接反侧；writer域另见'+evlink+'。',result=f'具体已有覆盖：{booklink(file)}。未新增正文或marker，不因Books不写而撤候选/降分。')

low = [
    ('21059','1+1+2=4','DR-IKE在既有Copy/Update/Retain中以线性head和单阈值选例，属局部实现。','CounterFact300/100及同源近邻/标签依赖，不采用逐次采样/排序未齐的部署recipe。'),
    ('21448','1+1+2=4','UTR拼RTG/state/previous action与已有causalconv，属局部offline-control接口。','简化linear/iid上界不认证非线性Transformer泛化或实时；不无根据迁移LLM/VLA。'),
    ('21581','1+1+2=4','Foley Control在冻结视频/音频骨干间插已有cross-attention adapter，属局部接口。','43倍数据非同底座净计算，冻结权重不保函数，任意encoder零重训不采用。'),
]
for ident,score,claim,body in low:
    entries[ident] = dict(name=title(ident),score=score,file=None,depth='已关闭',claim=claim,
                          body=body,decision='仅报告',evidence='exact-v1身份/日期/重复与关闭所需局部核心已核；'+evlink+'及'+rvlink+'R14/R20实际通过。',result='仅报告局部实现，不改变长期机制；4分按新增命题预先给定，非因Books/访问或工时倒改。')

entries['M2'] = dict(name='MiniMax M2', score='1+2+1=4', file=None, depth='深入完成',
    claim='历史assistant think原样回传改变该版本输入兼容性，关键算法尚待披露。',
    body='官方Oct27发布与历史README精确commit e304e33a34c9f403d2d5bb3e1a7d900ebcbda87c共同核。230B total/10B active不等10B HBM；Blog top_k20与历史card40不拼recipe。8%价/2x速度缺matched workload/hardware/precision/长度/batch/concurrency/SLO，为Not Disclosed，不授普遍收益。',
    decision='仅报告',evidence='4分仍因兼容性实际变化深入必要；'+evlink+'、'+rvlink+'R2/R7/R9已通过。',result='仅版本输入合同与发布事实，算法未公开，不构造长期Books差额。')
assert len(entries) == 72

rows = []
details = []
for ident, x in sorted(entries.items()):
    url = 'https://www.minimax.io/blog/minimax-m2-en-1748600000' if ident == 'M2' else f'https://arxiv.org/html/2510.{ident}v1'
    books = x['decision'] + (f'：{booklink(x["file"])}' if x['file'] else '：见§4具体理由')
    claim = x['claim'].replace('|','/')
    rows.append(f'| [{x["name"]}]({url}) | 2025-10-27 | {claim} {x["score"]} | {x["depth"]} | {books} |')
    details.append(f'### [{x["name"]}]({url})\n\n{x["evidence"]}\n\n{x["body"]}\n\n{x["result"]}')

def getsection(text, n):
    return re.search(rf'(?ms)^## {n}\. .*?(?=^## [1-6]\. |\Z)',text)[0]


sec1 = f'''## 1. 结论

本轮在旧1家族之外新增72个确定当窗家族，当前表共73：新增49项已有真实Books SAVE/sole actualPOST、19项具体已有覆盖、4项仅报告（含M2兼容性4分深入）。这些已处理事件的必要支持/直接反侧、准入/评分及实际Books层均有效；未运行实现/复现实验，也不授生产性能、安全或全球无遗漏。

尚有普通工作：后到25条具体题摘线索由sole互斥贡献/首必要，21060由writer已完成必要待sole及Books，随后更新本表/§4并作真实DAY→writer完成SAVE/全稿自读QA→sole actualFINAL。**本稿仍进行中，不以49处书稿或一批完结提前验收。**

主要长期变化涉及物理稀疏布局/结构化递归、危险识别与最终服从、评分尾部、训练/生成状态接口及可核测量/执行权限；不是论文名称目录。原七主题registered/created各251唯一线索、差额0不等零论文，也不等251篇候选或Methods。Google年主题37/Hunyuan中文All11均只授其实际可见范围，2025日级缺段隔离。具体查询、贡献关闭、停止与后到分工见[有限筛选]({prefix}REPAIR_SCREENING_20261029.md)、[canonical]({prefix}REPAIR_20261029.md)及{rvlink}。

旧OpenAI候选整行/日期/2+2+2=6、原小时窗与连续§4逐字保留；旧Peirce独核仅复用该事件与旧有限来源，不能代本轮DAY。窗外SRPPO/PLAN/SpecTokenizer/VAP及CGoT只保精确恢复线索，不启动其归属日；九个具体外部首公开缺额不用于正面Evidence/Books。

'''
sec2 = getsection(old,2)
sec2 = sec2.replace('各实际URL、请求时间与失败见','新增自然日查询/停止与当前原件见[有限筛选]('+prefix+'REPAIR_SCREENING_20261029.md)，旧有效层继续复用。各实际URL、请求时间与失败见',1)
replace_rows = {
    'SRC-GOOGLE-AI': '| SRC-GOOGLE-AI | 旧DeepMind/Blog有限邻接复用；本日Google pubs category2025/search language model三页15/15/7，真实form/data-page/max3与disabled尾页停止，未把年度37条变Methods/日级first | 受阻 | 年/主题导航恢复，Oct27日级pubs/DeepMind历史first仍缺；HTTP200不授Coverage |',
    'SRC-TENCENT-HUNYUAN': '| SRC-TENCENT-HUNYUAN | 实际research共Blog route及bundle API核；中文Accept-Language zh，publicList pageNum1/pageSize100/renderType0 All，code0/total11/list11且lang全zh；条目全2026，当前页已到尾 | 受阻 | 中文All已核，不借en9/别日数字；当前2026目录不授2025零，历史日段仍缺 |',
    'SRC-MINIMAX': '| SRC-MINIMAX | 旧英文12/中文13有限邻接与Agent独立TechBlog复用；M2 Oct27 08BJT虽在旧小时窗前，现属授权自然日补差；官方发布正文及Oct27精确README历史blob已读，R7/R9通过 | 已检查 | M2只版本兼容性/局部披露；Agent2025历史缺段仍隔离，current card不倒授 |',
    'SRC-ARXIV': '| SRC-ARXIV | 旧submitted99只作旧线索；本日7主题title/description的registered与created各366含重复、去重各251且同集；language100+40尾、其余64/58/1/16/56/31各尾页。233精确唯一v1/2025发号规则/arxiv.content/findable/registered联合区间同BJT27，18跨日按贡献分责 | 已检查 | 有限主题发现/差额完成，不授全学科召回；GLVQ/DD2具体更早正文日期及7跨日first外部隔离，后到25/21060仍普通工作；created不是公开上界 |',
}
sec2 = '\n'.join(replace_rows.get(line.split('|')[1].strip(),line) if line.startswith('| SRC-') else line for line in sec2.splitlines())+'\n\n'
sec2 = sec2.replace('按需会议/协议未触发，不扫描每周来源。OpenAI原链接Hub及arXiv具体v1/PDF为必要材料恢复，未扩站点日常库存。辅助搜索不能补成原pubs或历史公告覆盖。','按需OpenReview已为具名早稿触发；CVF/ISCA仅PLAN/SpecTokenizer，DataCite/2025官方公告与日期定义只作有限发现/日门组合。未触发的协议不扫，不扫描每周来源。辅助搜索/年会/Submitted不补成日级first；各具体原件和权限见有限筛选及earlier-public记录。')
sec3 = getsection(old,3).rstrip()+'\n'+'\n'.join(rows)+'\n\n'
sec4 = getsection(old,4).rstrip()+'\n\n以上连续原块仅保旧OpenAI事件的有效范围；不代本轮整日验收。以下为授权Oct27自然日新增，原件与必要层仅按本日实际复用。5–6分若整合，深入限真实长期差额，既有支持/关键反侧足即停，不为名词重复全文。\n\n'+'\n\n'.join(details)+'\n\n'
sec5 = f'''## 5. 缺口与下一步

可执行剩余：后到25项sole互斥贡献/首必要、writer21060的sole校准/Books，必要改动真实SAVE/自读/POST，更新全部六节后真实DAY与完成SAVE/全稿QA/actualFINAL。它们是普通工作，不计终态H。

本窗外部保留项（不支持正面Evidence/Books、零命中、无遗漏或性能/安全保证）：

- [GLVQ](https://arxiv.org/abs/2510.20984)/[DD2](https://arxiv.org/abs/2510.21003)：具体OpenReview全文家族的首次公开日期，精确两代API/id/title实际403、forum challenge；需要具名Published/Readers历史、官方日公告或作者正文发布记录，不要cdate/created或venue日程。仅重开这两个家族。
- [20856](https://arxiv.org/abs/2510.20856)、[20860](https://arxiv.org/abs/2510.20860)、[20867](https://arxiv.org/abs/2510.20867)、[20877](https://arxiv.org/abs/2510.20877)、[20878](https://arxiv.org/abs/2510.20878)、[20886](https://arxiv.org/abs/2510.20886)、[21501](https://arxiv.org/abs/2510.21501)：合法联合区间跨BJT Oct23/24–27。官方advanced只支持announcement年/月、精确日请求为表单错误非零；可得primary只月级/Submitted或较晚事件。需具名历史日公告/当时RSS或足以缩整个区间的精确发布界，取得后只重开相应身份，不全Methods/新日报。
- Google pubs/DeepMind、Meta、Qwen、Hunyuan、Z.ai、MiniMax Agent的2025日级历史缺段：旧有限入口失败/邻接与本轮Google三页、Hunyuan中文All恢复均保实际权限；需该机构当时官方历史列表/RSS/导出或具名原始发布，不拿当前壳/年目录授零。仅恢复受影响源/窗口。

每项完整路径、原字段、失败与替代/重开条件集中在[日期恢复]({prefix}REPAIR_EARLIER_PUBLIC_20261029.md)，不重复发多份请求。普通可执行仍继续，本表不先授完成。

窗外恢复线索（不属于本补窗，不启动其他日）：SRPPO官方primary搜索PublishedJuly8；PLAN作者PublishedOct21/出版方printOct19均早于27，保口径差异不猜全球first；SpecTokenizer publisher onlineAug17，不启动暂缓八月；VAP官方Oct24 technical report发布；CGoT2510.22235最早公告/registered均Oct28。各已得材料只支持其排窗范围，不写本日Books或重新计候选。

'''
sec6 = f'''## 6. 复核

复核者：01a186ed-2158-7010-8780-63ea8935ce2e（sole reader，非作者）。

结论：未通过（仍有普通后到必要/Books及完整日报DAY/FINAL待办，不是前批失败）。[独核记录]({prefix}REPAIR_REVIEW_20261029.md)R3–7核本日有限来源/日期/首批准入，R9–21覆盖已处理全部新增必要支持与直接反侧；R24/25/27实际比较全部已成Books判断，R15/22/26/30/33在真实SAVE后读完整新增/完整两侧/本人注，I1–I49累计49 actualPOST通过。各层复用，不重Methods或行政重存；九个精确外部缺额与后到25/21060继续独核，不预签DAY。

原Peirce FIRST/DAY/FINAL仅复用旧OpenAI与当时14有限来源/15信号的未变层，详见连续原§4及[旧独核]({prefix}FINAL_INDEPENDENT_REVIEW.md)。不是当前全部73及后到线索的独立验收。普通排除的来源/主题/理由分层样本、机器V3/引用/冻结/限定diffchecks待本轮全稿形成后落实际结果；不称全251题摘/全附件独核。

'''
new = old
for n, sec in [(1,sec1),(2,sec2),(3,sec3),(4,sec4),(5,sec5),(6,sec6)]:
    new = new.replace(getsection(new,n),sec,1)
stamp = dt.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')
new = re.sub(r'^\*\*检查时间：\*\* .*$', '**检查时间：** '+stamp, new, flags=re.M)
old4 = getsection(baseline,4).rstrip()
assert old4 in new
oldrow = next(x for x in baseline.splitlines() if x.startswith('| [GPT-5'))
assert oldrow in new
assert '2025-10-27T09:00:00+08:00 ～ 2025-10-28T09:00:00+08:00' in new
print('*** Begin Patch')
print('*** Update File: '+str(report))
for line in list(difflib.unified_diff(old.splitlines(),new.splitlines(),n=2,lineterm=''))[2:]:
    print('@@' if line.startswith('@@') else line)
print('*** End Patch')
