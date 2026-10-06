import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20804': ['S4.SS1.p4.1', 'Thmdiagnosticbold1.p1.2', 'S6.p3.1', 'S6.p4.1', 'S7.p6.1', 'S8.p1.1', 'S8.p2.1'],
    '20921': ['S3.I1.ix1.p1.1', 'Thmtheorem5.p1.1', 'Thmtheorem7.p1.1', 'S4.SS2.p14.2', 'S4.SS2.p14.3'],
    '20967': ['S2.SS1.p3.2', 'S3.SS2.SSS2.p1.1', 'S4.SS1.p1.1', 'S4.SS3.p1.1'],
    '20971': ['S3.p3.1', 'S9.SS4.SSS1.p2.1', 'S9.SS5.p3.1', 'S10.p1.1'],
    '21020': ['S4.SS2.p4.1', 'S4.SS3.p1.1', 'S6.SS1.p7.1', 'S6.SS1.p8.1', 'Thmlemma3.p1.1', 'Thmlemma4.p1.1', 'S6.SS3.SSS0.Px1.p1.1'],
}
out = ['# B26 — 最后五项必要原证 / actual owner；非作者待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    assert not set(ids) - {line.partition(' | ')[0] for line in lines}
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    core = (ROOT / f'V3_CORE_2602.{short}.txt').read_text().splitlines()
    ranges = {'20921': [(3695, 3695), (3743, 3743), (4143, 4260)],
              '20967': [(195, 201), (396, 400)],
              '20971': [(861, 985), (3444, 3444), (3617, 3617)]}.get(short, [])
    for start, end in ranges:
        if short == '20921' and end > start:
            excerpt = '\n'.join(line for line in core[start - 1:end] if line.startswith('\\'))
        else:
            excerpt = '\n'.join(core[start - 1:end])
        out += [f'CORE L{start}–{end} 原式/原段（不是修补）：', excerpt, '']
for path, ranges in [
    ('books/part-01-worldview/04-why-models-learn.md', [(41, 55)]),
    ('books/part-01-worldview/05-what-neural-networks-learn.md', [(242, 267)]),
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(36, 47)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(37, 47)]),
    ('books/part-04-training-system/29-sft.md', [(214, 221)]),
    ('books/part-07-agent/82-multi-agent.md', [(62, 74)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B26_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B26 words', words)
