# JASA06 — The Bayesian Lasso

作者：Trevor Park; George Casella。正式发表：2008，JASA 103(482)，681-686。类型：Theory and Methods。

[DOI](https://doi.org/10.1198/016214508000000337) · [全文](https://people.eecs.berkeley.edu/~jordan/sail/readings/park-casella.pdf) · [影响记录](https://openalex.org/W1982652137)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引2935次；正式发表至今至少八年，作为覆盖bayesian-computation, regularization的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读全文叙述及附录的解释性文字：正式版pp.681–686（§1–5、Appendices A–C）；公式推导未逐行核算。

全文核验：PDF 6页；SHA-256 `b2394394cd1a644ae03fb985dea1bbd99e04fc56f152750b1ea50892529f74b7`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引2935次，正式发表至少八年。覆盖Bayesian lasso的层次表示与简短计算方法稿，提供长理论稿以外的篇章尺度。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要从lasso的后验众数联系进入，接上正态尺度混合、可采样全条件、区间与调参，最后才提扩展（p.681）。每项都对应正文具体产物。

## 引言的推进

§1用熟悉线性模型和lasso目标建立最小符号，解释对误差尺度条件化的重要性，随即用糖尿病系数路径和可信区间展示完全贝叶斯分析的可见用途（pp.681–682）。例子先于采样细节。

## 方法、理论与章节依赖

§2给层级表示与全条件分布；§3将实际必须解决的lambda选择分成经验贝叶斯与超先验；§4靠替换层级分布解释bridge与稳健扩展；§5讨论用途及计算成本。unimodality和EM推导移至附录（pp.682–686）。

## 数值与应用如何提供证据

主文反复回到同一糖尿病数据，比较路径、区间和lambda方案；没有为了凑形式单列模拟节。p.682明确后验中位数并非精确稀疏，p.684承认bridge层级是否能高效采样尚不清楚。

## 结尾承担的任务

讨论解释区间如何改善常见标准误困难，区别Bayesian lambda与普通lasso调参，并指出GLM扩展可能改变计算比较（pp.684–685）。这些是新增判断。

## 可迁移写作动作

当模型机制可紧凑解释时，用一个贯穿例子逐步回答估计、区间、调参，不为每种证据建立重复背景；把实现所需分布写清，把验证性代数移后。

## 不能泛化的特例与反例

不能称Bayesian posterior median为“variable selection estimator”而省略它通常不等于零；也不能将credible interval写成frequentist confidence interval。此短文的无独立模拟节不是期刊统一要求。
