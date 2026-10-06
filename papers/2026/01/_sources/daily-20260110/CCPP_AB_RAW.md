# Constitutional Classifiers++ 原题摘

Blog与论文一个家族，不计两项。提交不等公开，blog已取实际时区字段；优先原paper v1必要审阅。

[2601.04603] Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (https://arxiv.org/abs/2601.04603)
citeturn26788view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn26783view0","id":5}); Total lines: 159
L8: [Submitted on 8 Jan 2026]
L9: # Title:Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks
L10: Authors:cite5†Hoagy Cunningham , cite6†Jerry Wei , cite7†Zihan Wang , cite8†Andrew Persic , cite9†Alwin Peng , cite10†Jordan Abderrachid , cite11†Raj Agarwal , cite12†Bobby Chen , cite13†Austin Cohen , cite14†Andy Dau , cite15†Alek Dimitriev , cite16†Rob Gilson , cite17†Logan Howard , cite18†Yijin Hua , cite19†Jared Kaplan , cite20†Jan Leike , cite21†Mu Lin , cite22†Christopher Liu , cite23†Vladimir Mikulik , cite24†Rohit Mittapalli , cite25†Clare O'Hara , cite26†Jin Pan , cite27†Nikhil Saxena , cite28†Alex Silverstein , cite29†Yue Song , cite30†Xunjie Yu , cite31†Giulio Zhou , cite32†Ethan Perez , cite33†Mrinank Sharma L11: View a PDF of the paper titled Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks, by Hoagy Cunningham and 28 other authors
L12: 
L13: cite34†View PDF cite35†HTML (experimental) L14: > Abstract:We introduce enhanced Constitutional Classifiers that deliver production-grade jailbreak robustness with dramatically reduced computational costs and refusal rates compared to previous-generation defenses. Our system combines several key insights. First, we develop exchange classifiers that evaluate model responses in their full conversational context, which addresses vulnerabilities in last-generation systems that examine outputs in isolation.
L15: Second, we implement a two-stage classifier cascade where lightweight classifiers screen all traffic and escalate only suspicious exchanges to more expensive classifiers. Third, we train efficient linear probe classifiers and ensemble them with external classifiers to simultaneously improve robustness and reduce computational costs.
L16: Together, these techniques yield a production-grade system achieving a 40x computational cost reduction compared to our baseline exchange classifier, while maintaining a 0.05% refusal rate on production traffic. Through extensive red-teaming comprising over 1,700 hours, we demonstrate strong protection against universal jailbreaks -- no attack on this system successfully elicited responses to all eight target queries comparable in detail to an undefended model.
L17: Our work establishes Constitutional Classifiers as practical and efficient safeguards for large language models.
L18: Subjects:  | Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)
L19: Cite as:  | cite36†arXiv:2601.04603 [cs.CR]
L20:    | (or cite37†arXiv:2601.04603v1 [cs.CR] for this version)
L21:    | cite38†https://doi.org/10.48550/arXiv.2601.04603†doi.org arXiv-issued DOI via DataCite
L22: ## Submission history
L23: 
L24: From: Mrinank Sharma [cite39†view email ]
L25: [v1] Thu, 8 Jan 2026 05:16:12 UTC (116 KB)
L26: 
L27: Full-text links:
L28: 
L29: ## Access Paper:
L30: 
L31: View a PDF of the paper titled Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks, by Hoagy Cunningham and 28 other authors
L32: 
L33:   * cite34†View PDF L34:   * cite35†HTML (experimental) L35:   * cite40†TeX Source L36: 

