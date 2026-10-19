# JASA03 — Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California’s Tobacco Control Program

作者：Alberto Abadie; Alexis Diamond; Jens Hainmueller。正式发表：2010，JASA 105(490)，493-505。类型：Applications and Case Studies。

[DOI](https://doi.org/10.1198/jasa.2009.ap08746) · [全文](https://www.mit.edu/~jhainm/Paper/ccs.pdf) · [影响记录](https://openalex.org/W3125057276)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引5486次；正式发表至今至少八年，作为覆盖causal-inference, comparative-case-studies的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读全文叙述：正式版pp.493–503（§1–4）；数据来源附录A和技术附录B仅查看组织，未逐行验算。

全文核验：PDF 13页；SHA-256 `899dd55ab6e5d093e1cf0efbbd6493f824e36935880006a55fa4d10d27393169`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引5486次，正式发表至少八年。覆盖synthetic control的政策案例、识别论证与placebo证据，补充JASA ACS因果研究。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要给出方法来源、Proposition99问题、26包的实质效应和推断贡献，末尾说明适用研究设计（p.493）。没有先列算法指标。

## 引言的推进

§1由聚合层级政策问题和已有案例进入，定位两个具体障碍：对照组选择含糊、聚合数据并不消除反事实不确定性。随后用组合对照、透明权重和不依赖处理后结果的设计解释解决思路，再预告加州结论（pp.493–494）。

## 方法、理论与章节依赖

§2.1界定比较案例，§2.2用因子模型解释何时拟合处理前轨迹有意义，§2.3才给权重实施，§2.4区分参数抽样误差与反事实可信度并构造placebo推断。§3按政策背景、数据与样本、结果、推断推进（pp.494–503）。

## 数值与应用如何提供证据

§3先展示美国其他州整体并非合适对照，继而比较协变量与处理前轨迹，再呈处理后差距。干扰、跨境购买、供体排除和placebo拟合差异都在影响解释的位置讨论；post/pre MSPE比率解决任意删placebo阈值问题（pp.499–503）。

## 结尾承担的任务

§4用两段连接可复用方法与政策发现，并给软件入口；不重讲每个权重或每张图（p.503）。

## 可迁移写作动作

应用稿先让读者看到估计对象及可信反事实的障碍；以诊断证据建立对照可信度，再解释估计效应；把稳健性放在它改变结论的位置。

## 不能泛化的特例与反例

正式版标Applications and Case Studies，但包含充分方法创新，不能把ACS等同没有理论。placebo秩并不无条件等于经典随机化因果检验；原文§2.4明确随机分配才有该解释。
