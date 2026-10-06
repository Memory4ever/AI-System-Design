import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20999': ['S3.SS1.p2.1', 'S4.SS2.p2.1', 'A8.p2.1'],
    '21013': ['S3.SS1.p2.1', 'S5.SS2.p3.1', 'S5.SS3.p3.1'],
    '21015': ['S2.SS2.SSS0.Px2.p1.1', 'S3.SS5.p2.1', 'A1.SS1.p2.1'],
    '21035': ['Sx4.SSx3.p10.1', 'Sx5.SSx1.p2.1', 'Sx5.SSx3.p6.1'],
    '21042': ['S4.SS2.p1.3', 'S5.SS1.p2.1', 'S6.p1.1'],
    '21044': ['S4.SS1.SSS0.Px3.p1.1', 'S5.SS2.p3.1', 'S6.SS2.SSS0.Px2.p1.1'],
    '21045': ['S5.SS4.p2.1', 'S6.SS1.p1.1', 'S8.p2.1'],
    '21054': ['S5.SS3.SSS0.Px1.p2.1', 'A1.p1.1', 'Sx2.p1.1'],
}
out = ['# B16 — 八项必要原证与actual owner（独立复核待核）', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    found = {line.partition(' | ')[0] for line in lines}
    assert not set(ids) - found, (short, set(ids) - found)
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
for short, positions in [('21035', [908, 997]), ('21042', [395, 448]), ('21054', [711, 910, 957])]:
    lines = (ROOT / f'V3_CORE_2602.{short}.txt').read_text().splitlines()
    out += [f'### {short} 原display公式TeX', '']
    for position in positions:
        assert '\\' in lines[position - 1], (short, position)
        out += [f'L{position}: {lines[position - 1]}', '']
for path, ranges in [
    ('books/part-06-ai-infrastructure/72-security.md', [(1241, 1252), (600, 600)]),
    ('books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', [(548, 550), (555, 555)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(101, 103)]),
    ('books/part-04-training-system/30-lora.md', [(215, 217), (295, 295)]),
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(74, 74), (199, 199), (244, 244), (3671, 3673)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B16_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B16 words', words)
