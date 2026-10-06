# 2025-09-22 Qwen 窄差额独立准入

复核者：root，非作者James。实际读取本日qwen-window-config.json两个完整对象、两份core全文、scan相关记录及下载身份；没有读全部性能图片或精确技术报告，不能授证据完成或DAY。

结论：局部校准通过，Omni继续必要审阅；TTS当前贡献关闭。

原官方date分别为Omni Sep21T21:00Z、TTS Sep21T20:00Z，对应22日05:00、04:00北京时间，完全落本窗。绑定原id/title/tokenLinks，不从Git提交或arXiv submitted伪首次公开。

Omni：整段speech等待完成带来串行交付压力 → Thinker的高层表示驱动Talker，主codebook自回归、同帧残余codebooks由MTP产生，Code2Wav增量解码 → 必须区分时间帧依赖与帧内codec依赖，才能判断首帧输出及流水化成本。准入2+2+2=6；拟长期知识的具体差额及性能解释需深入受影响部分，不为改书升分。实际双MoE、音频表示与跨模态数据混合是同配方变化，不能由SOTA声明单独归因；211/507ms没有完整hardware/batch/SLO绑定，不普适外推。已取精确Git artifact ae5dbf9可继续读架构、streaming latency定义/评价及直接反侧；该版本身份本身不证明所有内容在Blog首发时已相同。先读实际多模态owner和邻接再决定已有覆盖、仅报告或窄整合，不把本准入当必写。

TTS：实际核心全文以语言/音色/方言范围、样例与WER/similarity、首包/RTF数字为主，称architectural upgrades但没有披露具体新机制。两GPU满并发12对6、首包音频时长320对190也改变协议，不能由表中数字证明同负载新质量/资源边界。当前材料没有足够的具体新增解释，不评分、不写Books；不是因为TTS领域、模型大小或负面结果而排除。若明确披露改变codec/streaming机制或可比对照，再仅重开此家族。未试听全部音频或独核图，故不授质量真实性或跨语种稳定保证。

FSF局部有效校准不重复，本记录不验收其Books；其余必要风险/反侧、代表排除、14源停点及最终六部分仍待DAY。未改模型、共享状态或Books，未stage、commit、push。
