# DiagSafe Oct22 README corrections — exact official commit excerpts

{
  "url": "https://github.com/Tencent-Hunyuan/DiagSafe/commit/041bc5ac42de853c9846150d42e5af1cefd85df6",
  "sha": "041bc5ac42de853c9846150d42e5af1cefd85df6",
  "author_date": "2026-10-22T04:54:23Z",
  "committer_date": "2026-10-22T04:54:23Z",
  "message": "Revise rubric-based judging statistics in README\n\nUpdated the agreement percentage for rubric-based judging and clarified the evaluation results.",
  "files": [
    {
      "filename": "README.md",
      "patch": "@@ -80,7 +80,7 @@ Against 236 human-annotated responses as the gold standard:\n | Label-specification prompt + LLM | 82.63% – 86.86% | 0.532 – 0.802 |\n | **Prompt-level rubric + LLM (DiagSafe)** | **89.41% – 95.34%** | **0.828 – 0.864** |\n \n-Rubric-based judging reaches up to **95.34%** agreement with human annotations and stays above 93%\n+Rubric-based judging reaches up to **95.34%** agreement with human annotations and stays above 89%\n agreement across judge models, while the two prompt-based paradigms vary markedly between judges.\n Human review further finds 96.4% of prompts genuinely harmful and 99.6% of rubrics reasonable and\n actionable."
    }
  ]
}

{
  "url": "https://github.com/Tencent-Hunyuan/DiagSafe/commit/9b7fc486b541e69b623834556d43d43c037115e1",
  "sha": "9b7fc486b541e69b623834556d43d43c037115e1",
  "author_date": "2026-10-22T04:53:35Z",
  "committer_date": "2026-10-22T04:53:35Z",
  "message": "Revise consistency rates in README_zh.md\n\nUpdated consistency rates for rubric evaluation with different judges.",
  "files": [
    {
      "filename": "README_zh.md",
      "patch": "@@ -77,7 +77,7 @@\n | 标签标准 prompt + LLM | 82.63% – 86.86% | 0.532 – 0.802 |\n | **Prompt-level rubric + LLM（DiagSafe）** | **89.41% – 95.34%** | **0.828 – 0.864** |\n \n-Rubric 评估与人工标注的一致率最高可达 **95.34%**，换用不同 judge 时一致率始终保持在 93% 以上；\n+Rubric 评估与人工标注的一致率最高可达 **95.34%**，换用不同 judge 时一致率始终保持在 89% 以上；\n 另外两种 prompt 方式在不同 judge 之间波动明显。人工复核还显示，prompt 有害性合格率为 96.4%，\n rubric 合理且可执行的比例为 99.6%。\n "
    }
  ]
}


