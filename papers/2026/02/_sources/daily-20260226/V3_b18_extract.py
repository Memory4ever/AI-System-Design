import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '21144': ['S4.SS1.p3.1', 'S4.SS3.p3.1', 'S4.SS3.p4.1', 'S5.SS4.p2.1', 'S5.SS3.SSS3.p7.1'],
    '21157': ['S3.SS2.p2.1', 'S3.SS3.p1.1', 'S4.SS3.p2.1'],
    '21158': ['S3.SS2.SSS0.Px2.p1.1', 'S3.SS3.SSS0.Px1.p1.2', 'S4.SS3.SSS0.Px2.p1.1'],
    '21172': ['S4.SS2.p1.2', 'S7.p1.1'],
    '21175': ['S2.SS2.p2.1', 'S4.SS4.p1.1'],
    '21185': ['S3.p1.2', 'A1.SS2.SSS0.Px3.p1.2', 'S5.SS2.SSS0.Px3.p1.1'],
    '21186': ['S3.SS2.SSS0.Px1.p1.1', 'S3.SS2.SSS0.Px2.p1.1', 'S3.SS2.SSS0.Px3.p1.1', 'S4.SS4.SSS0.Px5.p1.1'],
}
out = ['# B18 — 八项必要原证 / actual owner；独立复核待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    found = {line.partition(' | ')[0] for line in lines}
    assert not set(ids) - found, (short, set(ids) - found)
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '21185':
        core = (ROOT / f'V3_CORE_2602.{short}.txt').read_text().splitlines()
        for lineno in [2317, 2664]:
            out += [f'原Eq11/12 L{lineno}:', core[lineno - 1], '']
    if short == '21158':
        core = (ROOT / f'V3_CORE_2602.{short}.txt').read_text().splitlines()
        for start, end in [(658, 660), (695, 697)]:
            out += [f'原reward公式 L{start}–{end}:', '\n'.join(core[start - 1:end]), '']
out += ['## 2602.21189v1', 'https://arxiv.org/html/2602.21189v1', '']
core = (ROOT / 'V3_CORE_2602.21189.txt').read_text().splitlines()
for start, end in [(816, 816), (9491, 9496), (9527, 9530), (9552, 9555), (9710, 9710), (9713, 9713)]:
    out += [f'原CORE L{start}–{end}:', '\n'.join(core[start - 1:end]), '']
for path, ranges in [
    ('books/part-05-inference-system/49-tensorrt-llm.md', [(392, 402), (234, 236)]),
    ('books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', [(133, 135)]),
    ('books/part-04-training-system/31-rlhf.md', [(414, 416), (955, 957)]),
    ('books/part-04-training-system/33-grpo.md', [(558, 565)]),
    ('books/part-07-agent/76-rag.md', [(73, 75)]),
    ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', [(422, 427)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(876, 878)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B18_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B18 words', words)
