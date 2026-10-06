# PACEvolve 10657v1 — 6标准必要提案

精确v1原题为Enabling Long-Horizon Progress-Aware Consistent Evolution，不用currentDOI改名。实际§3.1–3.3及主线§4.1.2 KernelBench/§4.2 ModdedNanoGPT必要方法/评价；缓存method/eval-necessary.txt。SymbolicRegression科学应用不作为贡献与成果采用，未遍历kernel代码附录。

HCM分conceptual idea/具体hypothesis，超cap压缩并持久化pruned失败；MBB以(s_previous−s_current)/(s_previous−r) EWMA衡量进展，低于阈值按偏向早迭代的power-law回退context；CE在backtrack/crossover中按island绝对进展权重选。不把heuristic momentum当真实local-minimum证明；依赖可信lower-bound r、分母非零及可比较score，预算不自动增加。

KernelBench16 operators/kernel、1000iterations每kernel、Gemini2.5Pro统一主模型/支持ensemble者用Flash，A10040GB/max频率、L2flush与reward-hacking修正；昂贵故未多run，逐kernel结果不是消除搜索随机性。Single在MLP/large-K matmul不胜PyTorch，不能用所有kernel/全面机制保证。NanoGPT v40在8H100/FineWeb validation3.28到达时间、Gemini3Pro，142.8→140.2s串行多个pipeline/model/超参变化，不能把各改动或搜索策略独立归因。精度/完整LLM token/评估费用未披露。

Ch79 L179–215 search-based planning把候选、verifier、budget/stop分开，固定搜索保留；Ch77 failed memory/phase compaction并不授模型summary为事实。这里stagnation-trigger+失败历史是受限search controller配方，未证明跨任务阈值/可靠回退/相同端到端预算替代已成立的长期gap。拟6标准完成→OnlyReport，无新Books，待root实际终裁。
