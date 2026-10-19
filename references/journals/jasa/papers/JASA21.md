# JASA21 — Distribution-Free Predictive Inference for Regression

作者：Jing Lei; Max G’Sell; Alessandro Rinaldo; Ryan J. Tibshirani; Larry Wasserman。正式发表：2018，JASA 113(523)，1094-1111。类型：Theory and Methods — original research。

[DOI](https://doi.org/10.1080/01621459.2017.1307116) · [全文](https://www.stat.cmu.edu/~ryantibs/papers/conformal.pdf) · [影响记录](https://openalex.org/W2964060211)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引930次；正式发表至今至少八年，作为覆盖predictive inference, conformal prediction的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读公开作者稿PDF pp.1、3–39摘要及§§1–7全部主体叙述、算法、理论说明、模拟图表；p.2目录及pp.40–41参考文献用于定位。pp.42–50技术证明和额外实验未列为已完整精读，未逐行核验公式。正式期刊年份为2018。

全文核验：PDF 50页；SHA-256 `1d614380e87c358e563706ba0bb04e288ec7e51321cbd06eaafbbcc034b52d5c`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引930次，正式发表至少八年。覆盖conformal regression、边际覆盖和预测式变量重要性，补充无分布预测推断。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Public author manuscript from Ryan Tibshirani institutional site, 50 PDF pages including appendices; undated title page; JASA print 2018。

## 摘要的信息选择

摘要把无分布预测带与基估计器可分离的性质置于首位，再说明full/split/jackknife的精度计算权衡、样本内和局部变宽扩展、LOCO及软件。有限样本边际覆盖与附加条件下的精度保持有明确分工（author manuscript p.1）。

## 引言的推进

§1直接定义数据、未来响应和边际覆盖目标，再以高维回归说明需求。Related Work把conformal与高维系数推断分别定位，Summary按结果及用途组织贡献并给定理编号；并未将原有conformal基本有效性据为新贡献（pp.3–6）。

## 方法、理论与章节依赖

§2以秩的可交换性解释核心机制，比较full、split、多次划分和普通jackknife；§3另立统计精度问题，按oracle比较、稳定性、一致性和稀疏回归例推进。§§5–6扩展到样本内、异方差和预测式变量重要性，每项都重新说明覆盖对象（pp.6–21、26–39）。

## 数值与应用如何提供证据

§4先比较经典参数区间，再改变基估计器和调参，把覆盖、长度、误差及运行时间分开。模型正确时保留参数区间较短的结果；异方差例直接显示边际覆盖相似而局部覆盖不同，不让总体有效性掩盖局部失配（pp.21–28、31–33）。

## 结尾承担的任务

§7重申边际覆盖和基估计器精度的关系，未来工作围绕样本划分随机性、较有效的聚合与LOCO条件目标；这些方向由本文已有代价自然导出（pp.37–39）。

## 可迁移写作动作

先定义究竟覆盖哪个随机量以及概率对哪些随机性取值，再陈述方法保证；将有效性、统计效率和计算成本分开，分别布置理论和实验。扩展节必须再次核对目标是否仍相同。

## 不能泛化的特例与反例

无分布不等于无独立或可交换性条件；边际覆盖不是对每个特征点的条件覆盖。局部LOCO同时预测集与全局均值/中位数区间的多重性、矩条件和条件目标不同；普通jackknife也不能替代后续jackknife+。本卡未将论文中的历史性能或软件状态当作当前指南。
