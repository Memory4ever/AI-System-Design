# Safety Bug Bounty — 实际官方原页读出

实际2026-10-02 web open https://openai.com/index/safety-bug-bounty/ 成功155行；no-slash曾Timeout、urllib403仅恢复过程。下方是当次原响应header/core26–55，不是作者重写或launch snapshot。

Introducing the OpenAI Safety Bug Bounty program | OpenAI (https://openai.com/index/safety-bug-bounty/)
citeturn25507view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://openai.com/index/safety-bug-bounty/","lineno":null}); Total lines: 155
L0: cite0†Skip to main content L1: 
L2:   * [Button: Research]
L3:   * [Button: Products]
L4:   * [Button: Business]
L5:   * [Button: Developers]
L6:   * [Button: Company]
L7:   * cite1†Foundation(opens in a new window)†openaifoundation.org L8: 
L9: cite2†Try ChatGPT(opens in a new window)†chatgpt.com [Button: Login]
L10: 
L11: OpenAI
L12: 
L13: March 25, 2026
L14: 
L15: cite3†Safety cite4†Security L16: # Introducing the OpenAI Safety Bug Bounty program
L17: 
L18: Testing for safety and abuse issues across OpenAI
L19: 
L20: Share
L21: 
L22: Program overview
L23: 
L24:   * cite5†Program overview L25:   * cite6†How to participate L26: Today, OpenAI is launching a public cite7†Safety Bug Bounty⁠(opens in a new window)†bugcrowd.com program focused on identifying AI abuse and safety risks across our products. As AI technology rapidly evolves, so do the potential ways it can be misused. Our goal is to ensure our systems remain safe and secure against misuse or abuse that could lead to tangible harm.
L27: This new program will complement OpenAI’s cite8†Security Bug Bounty⁠(opens in a new window)†bugcrowd.com by accepting issues that pose meaningful abuse and safety risks, even if they don’t meet the criteria for a security vulnerability. Through this program, we look forward to continuing to partner with safety and security researchers to help us identify and address issues that fall outside conventional security vulnerabilities but still pose real risks.
L28: Submissions will be triaged by OpenAI’s Safety and Security Bug Bounty teams, and may be rerouted between the two programs depending on scope and ownership.
L29: ## Program overview
L30: 
L31: The new cite7†Safety Bug Bounty⁠(opens in a new window)†bugcrowd.com program focuses on AI-specific safety scenarios listed below:
L32: 
L33: Agentic Risks including MCP
L34:   * Third party prompt injection and data exfiltration: when attacker text is able to reliably hijack a victim’s agent (including Browser, ChatGPT Agent, and similar agentic products) to trick it into performing a harmful action or leaking the user’s sensitive information. The behavior must be reproducible at least 50% of the time.
L35: 
L36:   * An agentic OpenAI product performs a disallowed action on OpenAI’s website at scale.
L37:   * An agentic OpenAI product performs some potentially harmful action not listed above. Valid reports here must indicate plausible and material harm.
L38: 
L39:   * Any testing for MCP risk must comply with the terms of service of any third parties.
L40: 
L41: OpenAI Proprietary Information
L42: 
L43:   * Model generations that return proprietary information related to reasoning.
L44: 
L45:   * Vulnerabilities that expose other OpenAI proprietary information.
L46: 
L47: Account and Platform Integrity
L48:   * Vulnerabilities in account integrity and platform integrity signals, such as bypassing anti-automation controls, manipulating account trust signals, evading account restrictions/suspensions/bans, and similar issues.
L49: 
L50:   * Issues that allow users to access features, data, or functionalities beyond authorized permissions should be reported to the cite8†Security Bug Bounty⁠(opens in a new window)†bugcrowd.com .
L51: While jailbreaks are out of scope for this program, we periodically run private bug bounty campaigns focused on certain harm types, such as Biorisk content issues in cite9†ChatGPT Agent⁠ and cite10†GPT‑5⁠ . We invite interested researchers to apply to these programs when they arise.
L52: Outside of the categories listed above, if researchers identify flaws that facilitate direct paths to user harm and actionable, discrete remediation steps, these may be considered in scope for rewards on a case-by-case basis. General content-policy bypasses without demonstrable safety or abuse impact are out of scope for this program. For example, “jailbreaks” that result in the model using rude language or returning information that is easily findable via search engines are out of scope.
L53: ## How to participate
L54: 
L55: Researchers interested in participating can apply through our cite7†Safety Bug Bounty⁠(opens in a new window)†bugcrowd.com program. We look forward to working alongside researchers, ethical hackers, and the safety and security community in the pursuit of a secure AI ecosystem.
L56:
