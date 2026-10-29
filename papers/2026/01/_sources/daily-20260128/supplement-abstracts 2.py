"""Exact v1 abstracts selected from bounded relevant title checks."""
import concurrent.futures, pathlib, subprocess, sys
base = pathlib.Path(__file__).resolve().parent
identities = '17172,17471,17717,17705,17676,17292,17910,17915,18067,18089,18129,18137,18157,18175,18125,18195,18207,18241,18255,18261,18271,18285,18302,18321,18345,18346,18393,18401,18415,18418,18467,18468,18483,18486,18491,18492,18510,18527,18533,18543,18554,18572,18579,18580,18588,18595,18631,18642,18681,18692,18698,18699,18702,18722,18730,18731,18734,18735,18751,18753,18760,18771,18777,18778,18779,18785,18790,18795'.split(',')
def one(number):
    filename = 'supplement-abs-' + number + '-20261008.json'
    return subprocess.run([sys.executable, str(base/'fetch.py'), filename, 'abs', 'https://arxiv.org/abs/2601.'+number+'v1'], capture_output=True, text=True).stdout.strip()
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for result in pool.map(one, identities): print(result, flush=True)
