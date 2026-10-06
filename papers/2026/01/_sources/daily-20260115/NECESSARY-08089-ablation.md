# Exact-v1 Q-realign decisive ablation

Primary https://arxiv.org/html/2601.08089v1 ; native text length67380. Actually read §2.2–3.2/Eq1–5,4.1–4.6/6 limits, AppendixD probe identity and AppendixE near60900–64500; unrelated implementation/baseline lists not mandatory.

AppendixD uses500 benign Alpaca and500 harmful BeaverTail,80/20 split and per-layer frozen SLR probe from aligned model. Accuracy>90% is probe discrimination, not behavioral safety truth.

AppendixE varies class mix in calibration: 100% malicious/no benign reconstruction gives harmfulscore0.34 but accuracy25.43 with incoherent generation; 75% malicious/default gives8.65/47.77;0% malicious/reconstruction-only42.11/48.12. Lower harmfulscore alone cannot certify safe-capable output. Moderate W8A8 gives8.65/47.77 vs FP16 44.23/48.30; aggressive W4A4 yields2.88/28.36 with incoherence. Same-format0%calibration control supports a role for behavior-targeted objective locally, not generic quantization safety repair or cost-free capability retention. Actual low-bit deployment kernel/throughput/latency independent and not verified here.
