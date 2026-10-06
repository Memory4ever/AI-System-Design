"""Read only explicitly named evidence blocks; never expand a paper review."""
import pathlib, re, sys

path = pathlib.Path(__file__).resolve().parent / ('V3_BLOCKS_2602.' + sys.argv[1] + '.md')
ranges = []
for part in sys.argv[2].split(','):
    bounds = [int(value) for value in part.split('-')]
    ranges.append((bounds[0], bounds[-1]))
for block in re.split(r'\n\n(?=\[\d+\])', path.read_text()):
    match = re.match(r'\[(\d+)\]', block)
    if match and any(lo <= int(match[1]) <= hi for lo, hi in ranges):
        print(block + '\n')
