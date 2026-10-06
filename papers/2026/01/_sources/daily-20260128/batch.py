"""Fetch an explicitly selected, finite set of exact-version abstracts."""
import concurrent.futures,json,pathlib,subprocess,sys
root=pathlib.Path(__file__).resolve().parent
def one(number):
 return subprocess.run([sys.executable,str(root/'fetch.py'),'abs-'+number+'.json','abs','https://arxiv.org/abs/2601.'+number+'v1'],capture_output=True,text=True).stdout.strip()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for result in pool.map(one,sys.argv[1].split(',')): print(result,flush=True)
