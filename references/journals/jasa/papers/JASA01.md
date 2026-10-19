# JASA01 — Variable Selection via Nonconcave Penalized Likelihood and its Oracle Properties

作者：Jianqing Fan; Runze Li。正式发表：2001，JASA 96(456)，1348-1360。类型：Theory and Methods。

[DOI](https://doi.org/10.1198/016214501753382273) · [全文](https://fan.princeton.edu/sites/g/files/toruqf5476/files/documents/penlike.pdf) · [影响记录](https://openalex.org/W2074682976)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引8907次；正式发表至今至少八年，作为覆盖regularization, variable-selection的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读全文叙述：正式版pp.1348–1358（§1–5）；查看附录条件位置，证明未逐行验算。

全文核验：PDF 13页；SHA-256 `a272b43fd56175da5443eeb840f756678f81d6aa1b9a62e88363491237eeaac2`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引8907次，正式发表至少八年。覆盖非凹惩罚、oracle性质和选择准则驱动的方法构造；与后续自适应惩罚作并读。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要依次写出选择问题、惩罚设计、计算、oracle性质与数值检验，重点是同时选择与估计的可操作结果（p.1348）。

## 引言的推进

§1先定位逐步/子集选择的不稳定与难以追踪抽样误差，再提出连续性、稀疏性、近似无偏三个设计需求；第二层叙述才解释非凹目标、算法及性质，最后扩展至样条与小波（pp.1348–1349）。

## 方法、理论与章节依赖

§2用正交设计将惩罚转成可见的阈值函数，逐项解释需求如何约束惩罚，再定义SCAD；§3一般化模型、给抽样性质与oracle定理、统一算法及标准误；§4调参与比较（pp.1349–1357）。直觉建立在具体可解子问题上。

## 数值与应用如何提供证据

§3.5用有闭式解的正交设计检验算法输出；§4分别考察线性、污染误差、logistic及烧伤数据。线性模拟明确承认高噪声小样本时lasso最佳，低噪声时SCAD占优（pp.1355–1357）。

## 结尾承担的任务

§5回收同一设计为何同时支持选择、估计与计算，指出lasso在噪声高时仍有价值；未重新展开附录条件（p.1358）。

## 可迁移写作动作

构造新方法前给读者可核对的设计准则，并用简单情形说明这些准则如何共同决定形式；让每项数值结果回答一条性能或计算主张。

## 不能泛化的特例与反例

经典原文仍有重复解释和笼统优越措辞，不能逐句模仿。oracle只属于其固定维度、调参及局部极值条件下的渐近性质，不能扩大为有限样本或一致风险保证。
