import pathlib,re,html,sys
ROOT=pathlib.Path(__file__).resolve().parent
for short in sys.argv[1:]:
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 out=[]
 for attrs,q in re.findall(r'<p\b([^>]*)>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  s=re.sub(r'\s+',' ',s)
  ident=re.search(r'id="([^"]+)"',attrs)
  out.append((ident.group(1) if ident else 'no-id')+' | '+s)
 (ROOT/('V3_PARA_2602.'+short+'.txt')).write_text('\n'.join(out)+'\n')
 print(short,len(out))
