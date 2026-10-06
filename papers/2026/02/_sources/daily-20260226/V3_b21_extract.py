import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20422': ['S4.SS1.SSS1.p1.1', 'S4.SS2.p2.1', 'S5.SS2.p2.1', 'S5.SS0.SSS0.Px3.p1.1'],
    '20424': ['S5.SS3.p1.1', 'A1.SS4.SSS0.Px2.p1.1', 'S7.SS2.p1.1', 'S8.SS0.SSS0.Px1.p1.1'],
    '20426': ['S3.SS2.p5.1', 'S4.SS1.SSS0.Px1.p1.1', 'A3.p1.1'],
    '20457': ['Thmassumption1.p1.2', 'Thmassumption2.p1.1', 'S4.SS1.p3.5', 'S4.SS1.p3.8'],
    '20461': ['A2.SS1.p1.5', 'A2.SS1.p1.6', 'A3.SS1.SSS0.Px1.p1.1', 'A4.SS1.p2.1'],
    '20520': ['S4.SS0.SSS0.Px5.p1.1', 'A4.SS0.SSS0.Px2.p1.1', 'A4.SS0.SSS0.Px3.p1.1'],
}
out = ['# B21 — 六项必要原证 / actual owner；独立复核待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    found = {line.partition(' | ')[0] for line in lines}
    assert not set(ids) - found, (short, set(ids) - found)
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '20457':
        core = (ROOT / 'V3_CORE_2602.20457.txt').read_text().splitlines()
        selected = [line for line in core[2137:2455] if line.startswith(('R(\\theta', 'L^{W}_{\\rho}(\\theta)='))]
        assert len(selected) == 3
        out += ['CORE 2138–2455 Eq12/13 完整原 TeX；只采用此受限分解，不授其余stationarity定理：', '\n'.join(selected), '']
    if short == '20461':
        core = (ROOT / 'V3_CORE_2602.20461.txt').read_text().splitlines()
        selected = [line for line in core[11779:12070] if line.startswith(('\\displaystyle-', '\\displaystyle o', '\\lim', '\\displaystyle\\lim'))]
        assert len(selected) == 4
        out += ['A2.SS1 proof 决定性乘积与lim两侧，CORE 11780–12070 原 TeX：', '\n'.join(selected), '']
for path, ranges in [
    ('books/part-03-multimodal-world-models/25-multimodal-world-models.md', [(89, 90), (122, 124)]),
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(63, 76)]),
    ('books/part-07-agent/78-tool-calling.md', [(57, 63)]),
    ('books/part-04-training-system/31-rlhf.md', [(578, 584)]),
    ('books/part-04-training-system/27-data.md', [(1081, 1085)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(26, 36), (85, 86)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B21_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B21 words', words)
