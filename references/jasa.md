# JASA：让文章的主要贡献决定叙述重心

核查日：2026-09-30。区分 Theory and Methods（T&M）、Applications and Case Studies（ACS）及 Review；不要将某一栏目的说明用于整个期刊。

## 官方来源与尚未核实的项目

**当前作者页未能完整读取。** [Taylor & Francis 官方投稿指南](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=uasa20)在本次核查中返回访问限制。摘要字数、关键词数、现行匿名方式、通用版式及 T&M 页数规则，均不得标记为“已按 2026 年现行指南核实”。

[JASA 的旧 Overleaf 模板](https://www.overleaf.com/latex/templates/journal-of-the-american-statistical-association-jasa-template/tmwhhgvxwwvc)明确提示可能过时，原始来源链接失效。它可解释旧文件结构，不能作为上述项目的现行依据。

**官方发布、具有日期边界的 ACS 说明。** ASA 社区 2024 年的[编辑通知](https://community.amstat.org/discussion/important-update-and-resources-for-jasa-acs-submissions-1?hlmlt=VT)及其[副编辑指导附件](https://community.amstat.org/HigherLogic/System/DownloadDocumentFile.ashx?DocumentFileKey=8fa8c189-1433-4ce5-8b47-01925d146838)已读取：传统 ACS 稿件限 35 页；新列出的数据基础设施等类别限 25 页，两者包括图表与参考文献；综述限 50 页并走综述栏目。将这些数值标为 **2024 ACS 指导**，正式提交前再核对，不能转作 T&M 限制。

**可复现材料。** [JASA 官方编辑团队维护的指南](https://jasa-acs.github.io/repro-guide/)说明 ACS 与 T&M 的可复现审查；[ACC 表格说明](https://jasa-acs.github.io/repro-guide/pages/acc.html)用于记录计算产物及复现信息。准备稿件时保留代码、数据可得性及计算说明；按当前指南确认首次修订时的提交材料。

## 署名编辑建议，不是统一硬性政策

Michael L. Stein（2023）的[编辑文章](https://www.tandfonline.com/doi/full/10.1080/01621459.2023.2173458)讨论什么构成有力的 ACS 论文。文章明确代表作者观点。可用于写作判断的要点是：实际问题必须驱动文章，数据来源与测量过程影响结论，分析应带来领域认识，稳健性和失败情形值得呈现。不要把其中的篇幅倾向或个人偏好当成拒稿阈值。

## 从论文到编辑动作

以下为本技能的判断，经典依据见 [P01–P03](classic-papers.md#jasa)。

| 稿件的主要贡献 | 组织正文时优先解决的问题 |
| --- | --- |
| T&M：新方法、新性质、新统计认识 | 为什么已有方法的具体权衡需要改变；新机制如何改变它；哪条结果支持这一点 |
| ACS：实质性应用发现或复杂数据分析 | 领域问题为何重要；数据怎样生成和进入样本；分析改变了什么判断；不确定性如何影响判断 |
| Review：整合已有方法或争议 | 读者面临哪些决策；不同方法在同一比较轴上如何选择；关键分歧及证据在哪里 |

T&M 不能因为有一个真实数据集就自动写成 ACS。ACS 也不必以一个复杂定理证明自身价值。对于跨类型稿件，找出没有它文章就失去意义的那项贡献，再确定标题、摘要和引言的重心。

Fan–Li 的可学之处是先说明好方法应满足什么，再解释构造；Li 的可学之处是把难以估计的整体目标替换为有统计意义的低维对象；Kass–Raftery 的可学之处是让前面的应用问题在后面得到回应。这些是论证方式，不是篇幅或摘要格式模板。

## 改写时的检查

- 方法稿：贡献句要指出改变了什么估计、选择、推断或计算行为；不要只写“提出一个新框架”。
- 应用稿：摘要和引言应出现实质性问题及可解释的发现；不要仅列算法、数据规模和评价分数。
- 模拟结果：解释何时有效以及何时失去优势；不把“若干场景胜出”概括成全面优越。
- 面向广泛统计读者解释研究意义，同时保留让结论成立的条件。

投稿检查时先重新访问作者页；如仍受限，逐项标记未核实，并继续完成文字与论证修改。
