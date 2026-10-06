import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20396': ['S3.Thmtheorem2.p1.1', 'S3.SS1.SSS0.Px2.p1.1', 'S3.SS2.SSS0.Px3.p1.1', 'S3.SS3.p1.1', 'S3.SS3.p2.1'],
    '20419': ['A2.SS3.p3.1', 'A2.SS3.p7.2', 'A2.SS3.p7.3', 'A3.SS1.p3.1'],
    '20467': ['S3.SS0.SSS0.Px2.p1.1', 'S3.SS0.SSS0.Px2.p3.2', 'S4.p1.1'],
    '20549': ['S3.SS2.p2.1', 'S4.SS1.p3.1', 'S5.SS0.SSSx1.p1.1'],
    '20593': ['S3.SS1.SSS3.p1.1', 'S3.SS3.p1.1', 'S5.SS4.p2.1'],
    '20629': ['S3.SS3.p2.1', 'S4.SS3.p2.1', 'S4.I9.i1.p1.1', 'S4.I9.i2.p1.1', 'S5.SS1.p3.2.1', 'S5.SS1.p3.3', 'S6.p5.1'],
}
out = ['# B20 — 六项必要原证 / actual owner；独立复核待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    found = {line.partition(' | ')[0] for line in lines}
    assert not set(ids) - found, (short, set(ids) - found)
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '20419':
        core = (ROOT / 'V3_CORE_2602.20419.txt').read_text().splitlines()
        selected = [line for line in core[5850:6060] if line.startswith(('t=', '\\mu_', '\\Pr', 'By design', 'Take', 'Therefore'))]
        assert any(line.startswith('\\mu_') for line in selected)
        out += ['A2.SS3.p4.2 的 < 号导致 paragraph 投影损坏；CORE 5850–6060 原 TeX/文本行：', '\n'.join(selected), '']
    if short == '20467':
        core = (ROOT / 'V3_CORE_2602.20467.txt').read_text().splitlines()
        selected = [line for line in core[1320:1740] if line.startswith(('\\displaystyle', '\\widetilde', '&='))]
        assert len(selected) >= 5
        out += ['CORE 1330–1730 的 scalar Eq4/5/6/7 与 vector-output 完整原 TeX；scalar E[∂b y]^2 不自行改成 E[(∂b y)^2]：', '\n'.join(selected), '']
    if short == '20549':
        core = (ROOT / 'V3_CORE_2602.20549.txt').read_text().splitlines()
        selected = [line for line in core[2380:2450] if line.startswith(('\\mathbb', '\\tilde', '\\Theta'))]
        assert len(selected) == 3
        out += ['CORE 2394–2441 两个条件 iid draws 与平方 score 偏差的完整原 TeX：', '\n'.join(selected), '']
for path, ranges in [
    ('books/part-01-worldview/05-what-neural-networks-learn.md', [(389, 394), (491, 492)]),
    ('books/part-06-ai-infrastructure/72-security.md', [(184, 189), (97, 114), (2123, 2125)]),
    ('books/part-05-inference-system/49-tensorrt-llm.md', [(509, 513), (1038, 1042)]),
    ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', [(156, 162)]),
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(124, 126), (309, 310)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B20_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B20 words', words)
