import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20670': ['S3.SS3.p3.1', 'S3.SS3.p4.1', 'S4.SS2.SSS0.Px1.p1.1'],
    '20672': ['S3.SS1.p1.1', 'S3.SS3.p1.1', 'S4.SS3.SSS0.Px2.p1.1', 'S4.SS1.SSS0.Px3.p1.1'],
    '20680': ['S3.I1.i2.p1.1', 'S4.SS0.SSS0.Px4.p1.1'],
    '20685': ['S3.SS5.p2.1', 'S4.SS4.p1.1', 'S4.SS2.p3.1'],
    '20687': ['S3.SS3.p3.1', 'S3.SS3.p5.1', 'S3.SS4.p3.1', 'S4.SS4.p1.2', 'S4.SS5.p3.1'],
}
out = ['# B25 — 五项必要原证 / actual owner；非作者待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    assert not set(ids) - {line.partition(' | ')[0] for line in lines}
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '20680':
        out += ['决定性Table1与原metric文字，直接CORE；不使用吞掉未转义<的PARA结果：', '\n'.join((ROOT / 'V3_CORE_2602.20680.txt').read_text().splitlines()[726:812]), '']
for path, ranges in [
    ('books/part-07-agent/80-reflection.md', [(45, 56), (199, 214)]),
    ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', [(48, 58), (97, 99)]),
    ('books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', [(14, 27)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B25_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B25 words', words)
