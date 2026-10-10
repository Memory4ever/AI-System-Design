from pathlib import Path
import re,html,subprocess
root=Path('papers/2026/02/_sources/daily-20260223')
ids=set('2602.20191 2602.19041 2602.18993 2602.18931 2602.18755 2602.18750 2602.19008 2602.18968 2602.18922 2602.18734 2602.18813 2602.18742 2602.18849 2602.18851 2602.18896 2602.18904 2602.18739 2602.19043 2602.18782 2602.18733 2602.19017 2602.18948 2602.18997 2602.18846 2602.18746 2602.18940 2602.19016 2602.18920 2602.18918 2602.18916 2602.18955 2603.06623'.split())
seen=set();out=['# 02-23 有界标题补检后的具名完整题摘','', '发现日期字段是Submitted Feb21–22，不是首次公开；仅具名相关/含糊条目进入此记录，不把宽列表全部变为候选。','']
clean=lambda s:html.unescape(' '.join(re.sub('<[^>]*>',' ',s).split())).replace('△ Less','').strip()
for path in sorted(root.glob('supplement-*20261008.raw')):
 if 'ARXIV_DISC' not in path.name and 'TOPIC_' not in path.name:continue
 for item in re.findall(r'<li class="arxiv-result">(.*?)</li>',path.read_text(),re.S):
  m=re.search(r'arxiv.org/abs/([^"<]+)',item)
  if not m or m[1] in seen or m[1] not in ids:continue
  seen.add(m[1]);title=re.search(r'<p class="title is-5 mathjax">(.*?)</p>',item,re.S);full=re.search(r'<span class="abstract-full[^>]*>(.*?)</p>',item,re.S)
  out.extend(['## '+m[1]+' — '+clean(title[1]),'',clean(full[1]) if full else 'ABSTRACT MISSING',''])
assert seen==ids,(ids-seen)
text='\n'.join(out);subprocess.run(['apply_patch'],input='*** Begin Patch\n*** Add File: '+str(root/'supplement-selected-abstracts-20261008.md')+'\n'+''.join('+'+x+'\n' for x in text.splitlines())+'*** End Patch\n',text=True,capture_output=True,check=True)
print('Saved complete abstracts:',len(seen),'Characters:',len(text))
