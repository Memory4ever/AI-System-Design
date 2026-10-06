import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20370': ['S3.SS1.p5.1', 'S3.SS3.p5.1', 'S3.SS3.p8.6'],
    '20517': ['S3.SS2.SSS2.p3.1', 'S3.SS2.SSS2.p7.1', 'S4.SS2.SSS3.p3.1', 'A6.p2.1'],
    '20567': ['A2.SS2.p2.1', 'A2.SS2.p9.2', 'S6.p2.1'],
    '20624': ['Sx2.SSx1.p2.1', 'Sx2.SSx2.SSSx1.p4.1', 'Sx2.SSx2.SSSx2.p2.1', 'Sx3.SSx1.p2.3'],
    '20585': ['Thmdefinition4.p1.1', 'S3.SS1.p2.1', 'S3.SS1.p3.1'],
    '20646': ['S3.SS3.p4.1', 'S4.p6.1', 'S7.SS2.SSS1.p3.1'],
}
out = ['# B22 — 六项必要原证 / actual owner；非作者待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    assert not set(ids) - {line.partition(' | ')[0] for line in lines}
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '20567':
        out += ['B.2 Eq41/52 原 TeX，中心限定问题而非自修：',
                r'\|\bm{H}^{t}\|_{\infty}\leq C_{H}\lambda^{t},\quad\forall t\geq 0.',
                r'\sum_{s=0}^{t-1}\gamma_{s}\leq\sum_{s=0}^{t-1}\lambda^{t-s}\gamma_{s}/(\min_{1\leq k\leq t}\lambda^{k})', '']
        core = (ROOT / 'V3_CORE_2602.20567.txt').read_text()
        assert out[-3] in core and out[-2] in core
    if short == '20646':
        core = (ROOT / 'V3_CORE_2602.20646.txt').read_text().splitlines()
        selected = [line for line in core[6080:6210] if line.startswith('\\displaystyle')]
        out += ['Theorem2 Eq23 的原 TeX两侧；条件均值与fourth moment分开：', '\n'.join(selected), '']
    if short == '20585':
        core = (ROOT / 'V3_CORE_2602.20585.txt').read_text().splitlines()
        out += ['Definition4 完整原 TeX：', core[307], '']
for path, ranges in [
    ('books/part-01-worldview/04-why-models-learn.md', [(41, 47), (342, 348)]),
    ('books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', [(139, 143)]),
    ('books/part-04-training-system/36-distributed-training.md', [(79, 87)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(154, 157)]),
    ('books/part-04-training-system/28-pretraining.md', [(1315, 1325)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B22_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B22 words', words)
