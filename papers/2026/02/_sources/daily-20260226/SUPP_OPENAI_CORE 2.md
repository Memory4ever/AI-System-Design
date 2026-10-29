# Feb25 aggregate必要准入核心（只读PDF pp3-4）

官方事件：https://openai.com/index/disrupting-malicious-ai-uses/ ，网页日期2026-02-25；RSS同事件Wed,25 Feb2026 00:00GMT。官方链接PDF：https://cdn.openai.com/pdf/df438d70-e3fe-4a6c-a403-ff632def8f79/disrupting-malicious-uses-of-ai.pdf 。网页直接读取403，web原页成功，web PDF正文因60516265 bytes过大失败；curl必要PDF原件成功，system pdftotext不可用，改用bundled pypdf。没有读37页为完整深审。


## PDF page 3

E x e c u t i v e  S u m m a rOur  mission is t o ensur e tha t artificial gener al in t elligence bene fits all o f  humanity .  W e advance this 
mission b y  deplo ying our  innova tions t o build AI t ools tha t help people solve r eally  har d pr oblems.  
I n the tw o y ear s since w e began publishing these thr ea t r eports,  w e have gained importan t insigh ts 
in t o the w a y s thr ea t ac t or s a tt emp t t o abuse AI models.  I n particular ,  the case studies in this 
r eport,  as in our  earlier  r eports,  illustr a t e ho w  thr ea t ac t or s typically  use AI in combina tion with 
o ther ,  mor e tr aditional t ools such as w ebsit es and social media accoun ts.  Thr ea t ac tivity  is seldom 
limit ed t o one pla tf orm; as our  r eport on a Chinese in fluence oper a t or  sho w s,  it is no t alw a y s 
limit ed t o one AI model.  R a ther ,  thr ea t ac t or s ma y  use diff er en t AI models a t various poin ts in their  
oper a tional w orkflo w .  W e shar e these insigh ts in our  thr ea t r eports so tha t our  industry ,  and wider  
socie ty ,  can be be tt er  placed t o iden tify  and avoid such thr ea ts.  
These ar e the k e y  insigh ts fr om our  la t est thr ea t disrup tions:
The scale and scope o f  covert in fluence oper a tions (IO ) fr om China: W e banned a Cha t GP T  
accoun t link ed t o an individual associa t ed with Chinese la w  en f or cemen t.  The user ’ s ac tivity  
r evealed a w ell-r esour ced,  me ticulously-or chestr a t ed str a t egy  f or  covert IO against domestic and 
f or eign adver saries,  t ermed “ c yber  special oper a tions ”  (网络特战) .  A s part o f  this str a t egy ,  the y  
tried t o use our  model t o plan a covert IO tar ge ting the J apanese prime minist er ,  but our  model 
r e fused.  The y  also used Cha t GP T  t o edit periodic sta tus r eports on the conduc t o f  “ c yber  special 
oper a tions ”  mor e br oadly .  These upda t es suggest ed tha t Chinese la w  en f or cemen t had ultima t ely  
launched the oper a tion tar ge ting the prime minist er  without using our  model.  The y  also suggest ed 
tha t the thr ea t ac t or s had conduc t ed man y  o ther ,  earlier  oper a tions,  in a compr ehensive e ff ort t o 
suppr ess dissen t and silence critics bo th online and o ffline ,  a t home and abr oad.  This e ff ort 
appear s t o be lar ge-scale ,  r esour ce-in t ensive and sustained,  engaging a t least hundr eds o f  sta ff ,  
thousands o f  f ak e accoun ts acr oss scor es o f  pla tf orms,  and the use o f  locally-deplo y ed AI models,  
especially  Chinese ones.  The user  described the oper a tions as using do z ens o f  tac tics,  r anging 
fr om abusive r eporting o f  dissiden ts ’  social media accoun ts,  thr ough mass online posting,  t o 
f or ging documen ts and imper sona ting US o fficials t o in timida t e critics.  Thr ough open-sour ce 
analy sis,  w e w er e able t o iden tify  online ac tivities tha t w er e consist en t with some o f  the tac tics this 
user  described,  tar ge ting no t just people in China,  but also dissiden ts and critics ar ound the w orld.  
Semi-aut oma t ed r omance fr om Cambodia: one common f orm o f  scam since long be f or e the da y s 
o f  AI is the r omance scam,  which tries t o trick  people in t o handing over  mone y  t o a non-e xist en t 
r oman tic partner .  This r eport de tails the pa tt ern tha t such scams typically  f ollo w .  I n one case ,  w e 
banned a ne tw ork  o f  accoun ts tha t used AI t o pose as a f ak e da ting agenc y  tar ge ting y oung men in 
I ndonesia.  U nusually ,  this scam ne tw ork  combined manual Cha t GP T  pr omp ting and an aut oma t ed 
AI cha tbo t t o try  t o en tr ap its tar ge ts.  
0 Disrup ting malicious uses o f  our  models: an upda t e ,  F ebruary  202

## PDF page 4

Ex ecutive Summar
A  con t en t f arm link ed t o R ussia: w e banned a clust er  o f  Cha t GP T  accoun ts tha t w er e link ed t o the 
R ussia-origin “Rybar ”  ( “Рыбарь” ,  in R ussian,  “fisherman ” ) ne tw ork.  This clust er  tr ansla t ed and 
gener a t ed con t en t tha t w as post ed on “Rybar ”  social media accoun ts,  but it also appear s t o have 
served as a con t en t f arm f or  a wider  ne tw ork  o f  accoun ts on X  and T elegr am tha t bor e no overt 
r ela tionship t o the “Rybar ”  gr oup .  On some occasions,  the thr ea t ac t or  used Cha t GP T  t o gener a t e 
ba t ches o f  short social media commen ts,  and these w er e then post ed b y  accoun ts on X  and 
T elegr am tha t appear ed t o origina t e fr om diff er en t parts o f  the w orld.  
A c t or ,  behavior ,  con t en t: the scam and in fluence oper a tions described in this r eport all used AI-
gener a t ed con t en t,  but the y  achieved very  diff er en t r esults.  F or  e x ample ,  some AI-gener a t ed social 
media posts r eceived t ens o f  thousands o f  vie w s,  while o ther  posts cr ea t ed in the same ba t ch 
r eceived almost none ( see an e x ample in oper a tion “Fish F ood” ,  belo w ) .  The use o f  AI-gener a t ed 
con t en t on its o wn does no t appear  t o have been the decisive f ac t or; r a ther ,  o ther  f ac t or s w er e 
lik ely  the main driver s o f  engagemen t,  no tably  the popularity  o f  the accoun ts which did the 
posting.  Similarly ,  in the scam case “Da t e Bait” ,  tar ge t ed ads on social media appear  t o have been 
a k e y  driver  o f  engagemen t.  This under scor es the importance o f  studying the na tur e o f  thr ea t 
ac t or s and the w a y s in which the y  behave ,  as w ell as the con t en t the y  gener a t e
0 Disrup ting malicious uses o f  our  models: an upda t e ,  F ebruary  202
