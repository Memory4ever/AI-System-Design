# IndexCache 实际非写入者 POST

mar14_supplement，2026-10-09；root为Ch45两段/本人note写入者。实际顺读当前Ch45完整175–215：只读verifier身份→structured accessplan→低维selector→dense-head map继承→新增196/198→层级page/物理布局→因果repair/wrapper前后论证，以及1728本人Review note。不是提案复核代替真实正文。

回对本次已实际读精确v1 §2–4/关键Tables1–4/C/D，正文Full/Shared是indexer role，不是KV共享或full attention；最近F初始化、固定LM-loss校准、层间相似不等下游质量、平均目标耦合不保证充分、全部Prefill不变linear、增加F/独立选择fallback一致。没有照录普遍无损/速度，原head-role训练、KV row manager、gather与物理生命周期条款未覆盖或移除。新两段与cache manager旧路径衔接成立，末注不称复现/生产SLO。POST通过；root可同步本人note/释放窄锁，再正式单项同步。不是本日报DAY。
