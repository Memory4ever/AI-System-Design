"""Print the final bounded-lead report patch after all nine actual saves."""
import difflib
import json
import re
from pathlib import Path

s = Path(__file__).resolve().parent
root = s.parents[4]
file = 'papers/2025/10/28/README.md'
old = (root / file).read_text()
prefix = '../_sources/daily-20251028/'
rv = f'[sole实际读点]({prefix}REPAIR_REVIEW_20261029.md)'
draft = (s / 'REPAIR_BOOKS_PRE8_20261029.md').read_text()
contexts = {c['id']: c for c in json.loads((s / 'REPAIR_BOOKS_CONTEXT8_20261029.json').read_text())}
titles = {r['doi'].split('.')[-1]: r['title'] for r in json.loads((s / 'REPAIR_DATE_BOUNDS_20261029.json').read_text())}


def booklink(path):
    node = re.search(r'Stable Knowledge Node ID:\*\* `([^`]+)`', (root / path).read_text())[1]
    chapter = int(Path(path).name.split('-')[0])
    return f'{node}，[Ch{chapter}](../../../../{path})'


entries = []
for sec in re.split(r'(?m)(?=^## I\d+ )', draft)[1:]:
    ident = re.match(r'## (I\d+)', sec)[1]
    body, note = re.findall(r'```markdown\n(.*?)\n```', sec, re.S)
    arxiv = re.search(r'SF-2025-ARXIV-2510-(\d{5})', body)[1]
    c = contexts[ident]
    actual = (root / c['file']).read_text()
    assert actual.count(body) == actual.count(note) == 1, ident
    prose = body.split('\n\n<!--')[0]
    entries.append(dict(arxiv=arxiv, path=c['file'], body=prose,
                        score=re.search(r'\d\+\d\+\d=\d', note)[0],
                        claim=prose.split('。', 1)[0]+'。', decision='整合'))

entries += [
    dict(arxiv='21326', path='books/part-02-model/11-tokenizer.md', score='2+1+2=5', decision='已有覆盖',
         claim='表面字符乱序可读不识别人类式字符恢复，many-to-one词形坍缩、clean-context消歧与重训tokenizer必须分开。',
         body='exact-v1§3–6必要与直接反侧见R38：BE/FULL排序的type/token与长度设置不同；clean BERT用已知word候选和平均subword logit，只测clean-context判别，非joint word probability或全scrambled输入保证。各自重训WordPiece/miniBERT及同预算、延长训练反侧均保，English/BNC结果不外推AR/现代LLM或全部语言。全部重训、分词和候选打分费计入，硬件precision未披露，未复现。R39实际已有覆盖为Ch11“Normalization与可逆性”的信息丢失/碰撞不可逆及原始输入回退，和“Tokenizer与checkpoint联合行为接口”的同decoded string不等embedding/position/path、扰动增强需重训回归。该具体论证已承载本次可逆性/输入行为分责，不新增同义类人鲁棒警告。'),
    dict(arxiv='21652', path='books/part-06-ai-infrastructure/66-evaluation-system.md', score='2+2+2=6', decision='已有覆盖',
         claim='Agent得分混合底模、证据/工具权限和预算，日期受限corpus与同一冻结价表重算仍不等环境全冻结、无污染或完整净费。',
         body='采用实际PDF exact-v1，HTML404不伪称已到；R38仅读§3–6与必要B/C定义和表注，不把88页下载等于全读。Standard/Custom-interface/Fully-custom工具和openness分层、按同一costmap重算token usage含cache，可缩小比较混杂；corpus cutoff不认证ranking/index/训练污染均已冻结，五分钟cell timeout不是全部walltimeSLO，token价也不含工具/硬件/研发、batching与latency-tier净费。部分模型未datepin/数月执行、57实例非57独立架构、macroaverage/独立同率步骤示意和LLMjudge边界均保，不扩科学应用或逐11benchmark Methods。R39实际已有覆盖：Ch66 model×benchmark×harness×environment×scorer交叉面板和失败分母、query时钟/payload/state fixture、独立tool权限treatment、完整费用及Benchmark Completion的evidence/action范围；Ch70相邻责任已区分price/workload漂移与全部失败/资源费用，不再拆写第二owner。全部检索/执行/重试/评判及价表更新后全重算仍需计费，无代码执行或复现。'),
]
assert len(entries) == 11
rows = []
details = []
for e in entries:
    i = e['arxiv']
    url = f'https://arxiv.org/{"pdf" if i == "21652" else "html"}/2510.{i}v1'
    assert url not in re.findall(r'^\| \[.*?\]\(([^)]+)\) \|', old, re.M), i
    name = titles[i].replace('|', '/')
    rows.append(f'| [{name}]({url}) | 2025-10-27 | {e["claim"]} {e["score"]} | 深入完成 | {e["decision"]}：{booklink(e["path"])} |')
    result = (f'已真实写入{booklink(e["path"])}；R39实际gap、PRE8整体PRE、writer真实SAVE/全新增完整邻接及本人注自读、sole actualPOST依本日canonical后到实际层，不以marker替验收。'
              if e['decision'] == '整合' else f'具体已有覆盖：{booklink(e["path"])}，R39实际承载论证已核，不为记录审批改书。')
    details.append(f'### [{name}]({url})\n\n采用本日精确v1，受限必要支持/直接反侧见{rv}R36–39；未第二Methods、未执行代码/复现实验。\n\n{e["body"]}\n\n{result}')

new = old.replace('\n## 4. 证据与知识整合', '\n'+'\n'.join(rows)+'\n\n## 4. 证据与知识整合', 1)
new = new.replace('\n## 5. 缺口与下一步', '\n\n'+'\n\n'.join(details)+'\n\n## 5. 缺口与下一步', 1)
new = re.sub(r'(?m)^本轮在旧1家族之外.*$', '本轮在旧1家族之外新增84个确定当窗家族，当前表共85：59项真实Books整合、21项新增具体已有覆盖、4项仅报告（含M2兼容性4分深入）；加旧OpenAI已有覆盖1，全部85个家族均有受限证据与具体Books处置。未运行实现/复现实验，不授生产性能、安全或全球无遗漏。', new, count=1)
new = re.sub(r'(?m)^尚有普通工作：.*$', '有限后到26线索已收口：8贡献关闭、21110具名早稿排窗、5具体早稿外部日门保留、12准入（含writer21060）。源/日期/必要与实际Books层已成后，仍须实际全日报DAY→writer完成SAVE/全稿自读QA→sole actualFINAL；此稿在该真实尾链之前不标完成。', new, count=1)
new = new.replace('九个具体外部首公开缺额', '14个具体外部首公开缺额')
new = new.replace('后到11普通Books/5具体早稿日门仍继续', '后到必要/Books及具名日门已按实际层收口')
new = new.replace('后到五件仍有限恢复', '后到五件已逐件有限恢复后隔离')
new = re.sub(r'(?m)^可执行剩余：.*$', '候选/Books无普通未处理项；仍须整份六节的实际DAY、writer完成SAVE/全稿自读QA及sole actualFINAL，未走完不提前标完成。外部日期/历史缺段已按R41/R43逐项核定有限停止，不借其缩池或授零。', new, count=1)
new = new.replace('- Google pubs/DeepMind、Meta、Qwen、Hunyuan、Z.ai、MiniMax Agent', '- [20903](https://arxiv.org/abs/2510.20903)、[20994](https://arxiv.org/abs/2510.20994)、[21267](https://arxiv.org/abs/2510.21267)、[21311](https://arxiv.org/abs/2510.21311)、[21542](https://arxiv.org/abs/2510.21542)：具体同家族OpenReview正文已出现，五件两代API精确ID各403、forum各challenge，限定title/author primary搜索无Published；Brunel复制Submitted的issued不授first。分别需要forum 3IbKbmNci3/72CEG36B0Q/ckq032sarb/unMwI4JLrP/KYlIC6sLhw可核Published/Readers历史或作者同正文明确公开记录，仅重开该身份，不第二Methods/扩日。\n- Google pubs/DeepMind、Meta、Qwen、Hunyuan、Z.ai、MiniMax Agent', 1)
new = new.replace('普通可执行仍继续，本表不先授完成。', '14家族仅日期权限保留，不支持正面Evidence/Books；整份DAY/SAVE/FINAL普通尾层仍继续，本表不先授完成。')
start = new.index('结论：未通过', new.index('## 6. 复核'))
new = new[:start] + '''结论：未通过（当前待整份六节实际DAY、writer完成SAVE/全自读QA及actualFINAL，不是已成层失败）。[独核记录](../_sources/daily-20251028/REPAIR_REVIEW_20261029.md)R3–7核有限来源/日期/首批准入，R9–21及R35–38覆盖全部新增必要支持/直接反侧；R24/25/27/39实际比较具体Books判断，R15/22/26/30/33/38及后到PRE8实际SAVE后的独核承载完整新增/完整两侧/本人注，不由源层预签POST。已成层复用，不重Methods或行政重存；后到真实读点以同日canonical记录为准。

R40–43分层排除：原5代表、首必要后7、后到8均实际独核；30条writer题摘表独核13/30、未独核17；跨日范围/贡献10项抽5/10、未独核5；另R31的20930/21508两项，共40个独立关闭身份。21207因具体理论潜力重开必要后修正理由关闭，未发现需重开整类的共同错误；标题明确的其余范围外条目未逐项独核，不声称全251题摘/全部附件验过。14家族外部日门与机构历史缺段均隔离，不授Coverage/Evidence正面通过。

旧Peirce FIRST/DAY/FINAL仅复用旧OpenAI与当时有限来源的未变层，连续原§4逐字保留，不能替当前85家族整日验收。机器V3/全部引用/冻结/限定diffchecks在最终完整稿实测后记录，不由中途74行初检预签。
'''
assert len(re.findall(r'^### \[', new, re.M)) == 85
diff = list(difflib.unified_diff(old.splitlines(), new.splitlines(), n=1))
print('*** Begin Patch\n*** Update File: '+str(root / file))
for line in diff[2:]:
    print('@@' if line.startswith('@@') else line)
print('*** End Patch')
