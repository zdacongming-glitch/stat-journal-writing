# JASA02 — The Adaptive Lasso and Its Oracle Properties

作者：Hui Zou。正式发表：2006，JASA 101(476)，1418-1429。类型：Theory and Methods。

[DOI](https://doi.org/10.1198/016214506000000735) · [全文](https://pages.cs.wisc.edu/~shao/stat992/zou2006.pdf) · [影响记录](https://openalex.org/W2020925091)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引7463次；正式发表至今至少八年，作为覆盖regularization, variable-selection的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读全文叙述：正式版pp.1418–1425（§1–5），并查看附录安排；附录证明未逐行验算。

全文核验：PDF 12页；SHA-256 `1f23df1fb0dff1f062299edca08a709e9c421727c8b44af596055a9c87fec75a`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引7463次，正式发表至少八年。覆盖adaptive lasso及其相对普通lasso的必要修正；展示失败条件如何引出新方法。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要先交代lasso的既有优势，立即提出选择一致性的必要条件，继而给出加权修正、oracle性质、算法可复用和GLM扩展（p.1418）。结果按回答研究问题的顺序出现。

## 引言的推进

§1先把预测与变量发现分开，定义oracle性质，再比较子集选择与lasso；已有正面理论与大系数偏差形成一个真实未决问题，随后给出“能否修复、如何修复”的贡献（pp.1418–1419）。这不是逐篇罗列相关工作。

## 方法、理论与章节依赖

§2先用必要条件和具体相关设计证明问题确实存在；§3依次定义adaptive lasso、给oracle性质、风险界、与garotte的关系、计算及标准误。理论紧跟各自解释的对象；§4才扩展GLM并明确高维尚待解决（pp.1419–1425）。

## 数值与应用如何提供证据

§3.7先模拟Corollary 1的失败情形，再按少数大效应/许多小效应及信噪比比较预测，另检验变量选择和标准误。p.1424明确不同方法各有优点，lasso在低信噪比有优势。模拟承担理论诊断与权衡解释。

## 结尾承担的任务

§5简短回收自适应权重与计算优势，并指出oracle性质不自动保证最佳预测；不是逐条再列全部定理（p.1425）。

## 可迁移写作动作

先给会改变方法选择的失败证据，再引出最小结构修正；数值场景对应前文机制。使用oracle property这一既有术语时同时保留其定义和渐近设定。

## 不能泛化的特例与反例

真实对比是论证核心，不能因为出现however就删；原文固定p的理论不能改写成任意超高维保证。§3的多条Remark是信息确实不同的实例，不是要求每个定理后都配Remark。
