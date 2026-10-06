import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[4]
KEYS = {
    '20294': ['S3.SS1.p3.1', 'S3.SS2.p2.1', 'S7.SS0.SSS0.Px2.p1.1'],
    '20650': ['S3.SS2.p1.1', 'S3.SS2.SSS2.p2.1', 'S4.SS2.p1.1'],
    '20652': ['S3.SS3.p3.1', 'S4.SS1.SSS1.p3.1', 'S4.SS2.p1.1'],
    '20731': ['S3.SS1.p1.1', 'S3.SS1.p2.1', 'S4.SS1.p5.1', 'S4.SS2.p2.1'],
    '20758': ['S3.SS2.p3.6', 'S4.SS1.SSS1.p1.1', 'S4.SS1.SSS5.p2.1'],
    '21160': ['S2.SS5.p2.1', 'S5.SS2.SSS0.Px2.p1.1', 'S6.p3.1'],
}
out = ['# B23 — 六项必要原证 / actual owner；非作者待核', '']
for short, ids in KEYS.items():
    lines = (ROOT / f'V3_PARA_2602.{short}.txt').read_text().splitlines()
    assert not set(ids) - {line.partition(' | ')[0] for line in lines}
    out += [f'## 2602.{short}v1', f'https://arxiv.org/html/2602.{short}v1', '']
    for line in lines:
        if line.partition(' | ')[0] in ids:
            out += [line, '']
    if short == '21160':
        core = (ROOT / 'V3_CORE_2602.21160.txt').read_text()
        formula = r'C_{k}(x)=\tfrac{1}{2}\,\mathrm{Var}[p_{k}](x)\,/\,\mu_{k}(x)'
        assert formula in core
        out += ['原 TeX仅二阶近似，不作为exact MI：', formula, '']
for path, ranges in [
    ('books/part-06-ai-infrastructure/66-evaluation-system.md', [(140, 156), (309, 314)]),
    ('books/part-03-multimodal-world-models/23-multimodal-representation.md', [(137, 149)]),
    ('books/part-04-training-system/27-data.md', [(353, 355)]),
    ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', [(157, 159)]),
]:
    lines = (PROJECT / path).read_text().splitlines()
    out += [f'## actual owner — {path}', '']
    for start, end in ranges:
        out += [f'L{start}–{end}:', '\n'.join(lines[start - 1:end]), '']
out += ['## 20731 PRE — 在Ch23当前141后/143前两段；没有写入或lease', '',
        '固定长度的离散 message 也可在多次观察中更新，而不是每个新 crop 都增加一段 tokens：同一表示模型消费旧 message、当前局部 crop 与相对位移，再将新 message 量化并送回下一轮；最后才以这份状态条件生成整图。训练随机化 crop 数，避免预先给未来观察保留固定槽位，并只对最后一次更新回传梯度。这把预算从“每帧生成多少 codes”转成“有限状态怎样重新分配已观察信息”，不意味着被覆盖的细节仍可恢复，后续 token 也不是独立的对象真值。', '',
        '语义对齐与重构需分别验收：[COMiT的受限对照](https://arxiv.org/html/2602.20731v1)用DINOv2语义对齐、flow reconstruction及local-crop训练形成可读结构；更大模型可继续改善重构却降低语义probe，单global crop已成本最低，增加local crop只有部分任务的有限增益。最佳IoU token由gold mask离线选择，不能当在线实体定位或内部因果；32 GH200/200epoch训练、循环编码及adaptive policy的额外decode都计费。存储/encoder/decoder与probe identity应一起版本化；语义退步、细节丢失或循环费用不合算时，保留一次性codec、更长message或独立encoder/decoder，不从重构保真批准生成状态的事实用途。', '']
words = len('\n'.join(out).split())
assert words <= 3500, words
(ROOT / 'V3_B23_CORE_OWNER_PACKET.md').write_text('\n'.join(out) + '\n')
print('B23 words', words)
