# JASA14 — Gibbs Sampling Methods for Stick-Breaking Priors

作者：Hemant Ishwaran; Lancelot F James。正式发表：2001，JASA 96(453)，161-173。类型：Theory and Methods — original research。

[DOI](https://doi.org/10.1198/016214501750332758) · [全文](https://people.eecs.berkeley.edu/~jordan/sail/readings/archive/ishwaran-stickBreaking.pdf) · [影响记录](https://openalex.org/W2072169887)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引1515次；正式发表至今至少八年，作为覆盖Bayesian nonparametrics, Monte Carlo computation的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读正式排版pp.161–170摘要及§§1–6全部主体叙述、表图和算法；附录pp.170–173未逐行验算。

全文核验：PDF 13页；SHA-256 `d29650c5e57463dce77b2c07d27d9f3ab5bd2bc8a9e489dae8ee42a44583d750`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引1515次，正式发表至少八年。覆盖一般stick-breaking先验的blocked Gibbs计算，补充贝叶斯非参数算法比较。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要以两种抽样器和所适用的stick-breaking先验为骨架，直接交代边缘化Pólya urn与有限截断blocked Gibbs的联系及后者的计算用途（p.161）。

## 引言的推进

§1先定义有限与无限随机概率测度及权重，再解释后验计算为何取决于预测分布或可直接更新的先验表示。§2将两参数Poisson–Dirichlet先验作为具体重要实例，避免只在抽象符号中介绍算法（pp.161–164）。

## 方法、理论与章节依赖

§3的截断误差和矩结果给有限近似的计算选择以依据；§4解释Pólya urn边缘化、加速和后验泛函计算的限制；§5才给blocked Gibbs的完整更新顺序。先明确抽样对象和后验量，再比较算法（pp.164–169）。

## 数值与应用如何提供证据

§6特意改变基分布方差，使新类分配概率变小，从而显露逐点更新的混合问题。比较普通Pólya urn、加速版本和blocked sampler，承认小型共轭Dirichlet例中加速Pólya urn略占优，而其他先验下blocked方案有优势（pp.169–170）。

## 结尾承担的任务

结论在§6末直接作有条件的算法建议：简单加速通常值得采用，但两个较强方案的相对表现依赖先验与模型；无需另加一节复述贡献。

## 可迁移写作动作

算法论文应先说明需要抽样的后验对象，再让理论界、更新步骤和比较设计服务同一计算障碍；保留对手获胜的情形能界定推荐范围。

## 不能泛化的特例与反例

stick-breaking不是Dirichlet过程的同义词，Pólya urn与blocked sampler也不能被表述为无条件优劣关系。本文篇幅中的权重与预测分布细节是算法可复现所必需，不应被一般性的删繁规则删掉。
