import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '21059': ['S3.SS3.p3.1', 'S4.SS1.SSS2.p2.1'],
    '21061': ['S1.p7.1', 'S5.SS2.p2.1', 'S6.SS3.p1.1', 'S6.SS3.p7.1'],
    '21064': ['S3.SS1.p1.1', 'S3.SS3.p1.1', 'S4.SS4.SSS1.p1.2'],
    '21103': ['S3.I2.i2.p1.1', 'S5.SS2.p2.1', 'S5.SS2.p3.1'],
    '21127': ['S4.SS1.p7.1', 'S4.SS4.p2.1', 'S5.SS3.p2.1', 'S6.p4.1'],
    '21133': ['S2.SS2.p2.1', 'S2.SS2.p3.1', 'S3.SS3.p1.1', 'S3.SS4.p1.1'],
    '21140': ['S3.SS2.p2.1', 'S3.SS5.p1.1', 'S4.SS1.p1.1', 'S6.p2.1'],
    '21143': ['S4.SS1.SSS0.Px2.p1.1', 'S5.SS0.SSS0.Px4.p1.1', 'S5.SS0.SSS0.Px4.p2.1'],
}
out = ['# B17 — 八项必要原证与 actual owner（独立复核待核）', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    found = {line.partition(' | ')[0] for line in lines}
    assert not set(ids) - found, (short, set(ids) - found)
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
for path, ranges in [
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(51, 60), (132, 136)]),
    ('books/part-04-training-system/28-pretraining.md', [(245, 260)]),
    ('books/part-07-agent/74-prompt.md', [(132, 134), (218, 218)]),
    ('books/part-06-ai-infrastructure/72-security.md', [(3052, 3061)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(198, 198), (206, 208)]),
    ('books/part-05-inference-system/52-dynamo.md', [(346, 357)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B17_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B17 words', words)
