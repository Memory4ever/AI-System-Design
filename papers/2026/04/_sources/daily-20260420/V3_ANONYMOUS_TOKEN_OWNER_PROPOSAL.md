# 15637 匿名token：必要 source→actual owner 窄采用提案

作者apr20_resume；7分保护深入，必要原文见[v3-reopen-notes 接续四项](./v3-reopen-notes.md)。只防御机制、不执行攻击/获取凭据；未非作者采用/写Books，不计I或日Gate。

## owner与实际差异

唯一`PLATFORM-SECURITY`/Ch72。实际Ch72“三层Security”末句（约94）要求每层identity/integrity/authorization，后接HardwareAttestation；528多跳delegation区分issuer signature与delegate亲签，530保存token生命周期/撤销/replay压力。现有链没有明确**anonymous unlinkability与holder non-transferability独立、一次子token不消除长期rootcredential转移**。拟在三层Security末与HardwareAttestation之前嵌两段：

> 隐私友好的匿名访问还要把“服务不能关联身份”和“凭据只能由合格持有者使用”分开验收。一个两阶段方案先凭硬件资格签发长期兑换凭据，再以它获取一次请求token；一次性消费能阻止该请求token重复使用，却不能阻止已泄漏的兑换凭据继续生成新的token。有效签名证明发行方准入过某个凭据，不自然证明当前请求仍来自原合格设备或用户；计费、quota与滥用责任也可能沿被盗凭据落回原资产。
>
> 因而storage访问控制、持有者/请求绑定、rootcredential生命周期与撤销需要分别定义。缩短签名key寿命和收紧客户端secret访问能减少暴露期，却增加重新认证、服务负载与恢复成本，也不自动让bearer token不可转移；绑定设备又需要避免破坏匿名性并处理迁移和丢失。[受限内置AI服务分析](https://arxiv.org/html/2604.15637v1)只验证作者自有旧版本设备、且依赖用户允许keychain访问的攻击模型；磁盘加密不等授权API永不返回plaintext，后续storage补丁也不等协议已具备non-transferability。无法证明holder binding或及时撤销时，应收窄quota与scope、隔离根凭据并增加独立滥用审计，不让“匿名”或“一次性”自签整条授权链安全。

## 必要来源与反证

官方v1 §3/4.1/威胁模型、§5.1/5.2、§6/Ethics；macOS26.0(25A353)/M4Macmini作者自有设备，需受害者允许keychain访问非silent零权限，TGT多days/OTT约12h非全系统SLA。§6.1作者分析26.2迁iCloudkeychain/appleaccessgroup只是storage mitigation，后续绕过不当独立复现/当前漏洞普遍保证；§6.3原文明确keychain磁盘加密而授权API可取明文，不能照录§4.1“plaintext keychain”的粗表述。

[Apple官方26.2安全公告](https://support.apple.com/en-ae/125886)Networking/CVE-2025-43509与论文同四作者，确认宽敏感数据访问问题以data protection改进，Released2025Dec12。仅vendor公开修复事实，不确认作者所有机制/残余结果；不是Apr20新fix/firstpublic日期证明。这里只借受限实例说明授权设计分责，不改生产设备配置、不运行攻击、不采全系统漏洞/“所有root可绕”证明，不展开所有artifact。

## root 有限非作者采用复核

实际打开官方v1 §3、§4.1、§5.1/5.2、§6、§7/Ethics及Apple公告Networking条目与Released字段；实际对读Ch72三层Security→Hardware Attestation和既有多跳delegation交接。两段窄提案通过：一次消费的OTT与可继续兑换的TGT承担不同状态，签名资格、匿名性、当前holder绑定与撤销不能互相替代。保留作者旧设备、用户授权访问及未独立复现限制，不将§4.1的plaintext粗述写成磁盘未加密，也不把2025修复/当前网页修改时间记作本窗发布。不采纳所有设备当前可利用或后续mitigation普遍无效的结论。可按上述literal嵌入并补章末来源说明；实际写后仍需复核，本条不是日报Gate。

实际写后通过：root实际顺读Ch72三层Security末至Hardware Attestation开头及Review notes，两段已写于96～98行，状态区别、用户授权、旧版本与防御建议/实验结果分界保留。不是孤立章末摘要，未覆盖原硬件证明论证；该family可同步为真实整合，日报其他普通工作和最终Gate仍未完。
