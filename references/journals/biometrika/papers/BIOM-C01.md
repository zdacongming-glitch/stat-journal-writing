# BIOM-C01 · Bayesian cumulative shrinkage for infinite factorizations

近期校准：2020，*Biometrika* 107(3)，745-752。[DOI](https://doi.org/10.1093/biomet/asaa008)。

Sirio Legramanti; Daniele Durante; David B Dunson。

近期方向样本，用于校准核心经典库的术语与叙述安排；不占核心25篇，不声称已通过长期检验。

文章类型：methodological contribution; short main article, final issue category not established from author PDF。

全文：[所读公开稿](https://arxiv.org/pdf/1902.04349)；arXiv:1902.04349v3, 2020-09-10, ten-page author version; formal journal paper published 2020。

阅读范围：Complete ten-page PDF narrative, definition, propositions and theorem interpretations, both Gibbs algorithms, sensitivity and personality-data example, appendix proof organization and references; algebra not independently verified. 阅读日：2026-10-19；页码为所读PDF页序。

## 摘要的信息选择

摘要由维度未知进入，定义逐步增加收缩的对象及spike-and-slab机制，再给理论、计算、数据与代码；目标不是泛泛更稀疏，而是区分活跃项的先验与冗余项消除。

## 引言推进

§1 pp.1–2只有两个主要段落后就给Definition 1。第一段将无自然顺序的回归收缩与有顺序因子扩张分开，并承认MGP的既有作用；第二段解释新过程及参数含义，定义后立即说明stick-breaking和有限截断，不另列长贡献清单。

## 方法、定义与理论

§2 pp.2–3按支持、总变差解释、期望、分布递增、活跃项数的先验均值、截断误差组织，每个结果回答一个建模选择；§3 pp.3–6把一般先验嵌入因子模型，再给合法性/支持与共轭更新，自适应截断直接利用spike标签，避免额外数值零阈值。与BIOM20的差异精确到递增收缩的性质和活跃项分布。

## 数值与应用

§4 pp.6–7比较三种维度、后验均方误差、因子数、ESS及时间，另表检验超参数敏感性。§5 pp.7–8的人格问卷例说明相近协方差拟合可对应极不同因子数及成本；不把少因子直接说成绝对真实人格结构。

## 结尾

无独立Discussion，应用的相关结构、因子数、不确定性与运算代价承担结尾；pp.8–9证明附录短，技术线不挤占方法解释。

## 可迁移动作

新过程先以最一般且可解释的对象定义，再用一个重要模型说明具体选择与计算；形式结果后立即给参数含义。近期短稿仍然依赖清楚的统计目标与实施连接。

## 特殊范围与限制

这篇短方法稿不能替代所有近年方向的风格证据；两篇校准远不足以推出全刊写法变化。递增期望与递增分布是不同保证，不能只因都叫increasing shrinkage而合并。
