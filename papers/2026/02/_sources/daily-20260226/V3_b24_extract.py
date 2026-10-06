import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20450': ['S6.SS2.SSS2.p3.1', 'S7.SS1.p4.1', 'S7.SS2.SSS2.p2.1'],
    '20981': ['S4.SS4.p3.1', 'S4.SS4.p4.2', 'S7.p2.1', 'S9.p2.1'],
    '21078': ['Thmremark1.p3.1', 'S6.SS1.p2.1', 'S6.SS3.p10.1'],
    '21092': ['S4.SS1.SSS0.Px1.p1.1', 'S4.SS1.SSS0.Px2.p2.1'],
    '20673': ['S3.SS3.p3.1', 'S3.SS4.p1.1', 'S4.SS4.p1.1'],
    '21039': ['S3.p2.1', 'S3.SS1.p2.4', 'S4.SS2.p3.1', 'S4.SS1.SSS0.Px2.p3.1'],
}
out = ['# B24 — 六项必要原证 / actual owner；非作者待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    assert not set(ids) - {line.partition(' | ')[0] for line in lines}
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '20981':
        out += ['Table4原机械段：', '\n'.join((ROOT / 'V3_CORE_2602.20981.txt').read_text().splitlines()[1989:2008]), '']
    if short == '21039':
        formula = r'T_{\mathsf{SHT}}\mathinner{\left(\epsilon,\delta\right)}=O\mathinner{\left(\log\mathinner{\left(\frac{1}{\delta}\right)}\min\mathinner{\left\{\frac{1}{\epsilon^{2}},\frac{d}{\epsilon}\right\}}\right)}'
        assert formula in (ROOT / 'V3_CORE_2602.21039.txt').read_text()
        out += ['Theorem4.3原TeX（fixed binary RCN 1/4 setting）：', formula, '']
for path, ranges in [
    ('books/part-04-training-system/36-distributed-training.md', [(76, 83)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(890, 896), (1032, 1036)]),
    ('books/part-04-training-system/27-data.md', [(318, 324)]),
    ('books/part-01-worldview/05-what-neural-networks-learn.md', [(253, 266)]),
    ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', [(48, 58)]),
    ('books/part-01-worldview/04-why-models-learn.md', [(41, 47)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B24_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B24 words', words)
