import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20427': ['S3.SS1.p5.1', 'S3.SS3.p3.1', 'A1.SS2.p1.1'],
    '20901': ['S4.SS2.SSS0.Px1.p1.1', 'S4.SS2.SSS0.Px2.p1.1'],
    '21188': ['S3.SS3.p2.1', 'S3.SS3.p6.1', 'S4.SS3.p2.1', 'S5.p1.1'],
    '21193': ['S5.SS4.SSS0.Px1.p1.1', 'S5.SS6.p1.1'],
    '21196': ['S3.SS3.p2.1', 'S3.SS3.p4.1', 'S5.SS4.p1.1'],
    '21198': ['S3.SS2.SSS1.p4.2', 'A2.SS1.p2.1', 'A2.SS3.p1.1'],
    '21202': ['S5.p1.1', 'S6.SS3.SSS0.Px2.p1.1', 'S6.SS4.SSS0.Px2.p1.1'],
    '21204': ['S5.Thmtheorem1.p1.1', 'S5.Thmtheorem1.p1.2', 'S6.SS2.p2.1', 'S6.SS1.p8.1', 'S7.p3.1'],
}
out = ['# B19 — 八项必要原证 / actual owner；独立复核待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    found = {line.partition(' | ')[0] for line in lines}
    assert not set(ids) - found, (short, set(ids) - found)
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '21204':
        core = (ROOT / f'V3_CORE_2602.{short}.txt').read_text().splitlines()
        equations = [line for line in core[830:1512] if line.startswith(('o=', 'o_{t}=', '\\hat{q}=', '\\hat{v}_{i}='))]
        assert equations
        out += ['原Theorem 5.1–5.3 CORE 830–1512 的完整TeX行：', '\n'.join(equations), '']
for path, ranges in [
    ('books/part-05-inference-system/49-tensorrt-llm.md', [(28, 30), (113, 115)]),
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(132, 134)]),
    ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', [(85, 87), (1430, 1432)]),
    ('books/part-04-training-system/27-data.md', [(542, 560)]),
    ('books/part-04-training-system/36-distributed-training.md', [(591, 606)]),
    ('books/part-07-agent/80-reflection.md', [(26, 44)]),
    ('books/part-07-agent/76-rag.md', [(411, 430)]),
    ('books/part-02-model/22-long-context.md', [(650, 657), (517, 519)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B19_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B19 words', words)
