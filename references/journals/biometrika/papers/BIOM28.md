# BIOM28 · Maximum projection designs for computer experiments

题录：V. Roshan Joseph; Evren Gul; Shan Ba（2015），*Biometrika* 102(2)，371-380。[DOI](https://doi.org/10.1093/biomet/asv002)。

文章类型：regular methodological article; published Advance Access PDF。方向：experimental-design, computer-experiments。

全文：[公开来源](https://www.asc.ohio-state.edu/statistics/comp_exp/jour.club/max_projection_designs_roshan2015.pdf)。版本：published Advance Access PDF, 2015-03-18, ten pages; journal volume 102, pp.371–380。

阅读范围：Complete ten-page published PDF: summary, all five main sections, criterion and theorem statements, optimization description, both numerical comparison suites and figure captions, appendices and references; proof organization read, calculations not independently checked. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

2015年提出的maximum projection设计成为持续使用的计算机试验设计准则，作者维护的MaxPro软件及CRAN文档仍将本文列为基础来源（https://cran.r-project.org/package=MaxPro）。OpenAlex查询有336次引用；保留该文也使核心库覆盖试验设计，避免高维回归独占样本。
引用线索：OpenAlex，2026-10-19，336次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要把全空间距离最优与低维投影质量之间的缺口说清，再以少量活跃因子的实际需求引出所有子集投影，最后强调新准则的计算成本。

## 引言的推进

§1 pp.1–2先定义已有maximin准则和边界聚集问题，再介绍拉丁超立方只能保证一维投影；effect sparsity说明为何中间维度也重要。最近邻投影准则的计算成本构成明确缺口；均匀差异度适合积分，并不自动保证函数逼近表现。

## 方法、定义与理论的依赖

§2 pp.2–3由未知因子重要性下的加权距离进入，对单纯形权重作贝叶斯平均，以特殊幂次的可积性得到乘积距离准则；定理之后解释不同水平及MaxPro命名。§3 pp.3–4区分准则便宜与高维非凸搜索仍难，随后给拉丁超立方模拟退火、连续局部修正、梯度及软件。

## 数值、应用与证据

§4 pp.4–6用九个样本量/维数组合比较不同投影的maximin、minimax与中心化差异度，明确均匀设计在其目标上更好，MaxProLHD是一种折中。§5 pp.6–9先给GP相关矩阵的期望非对角相关解释，再用界与数值把它连接到熵、条件数和预测方差；不把期望界直接说成精确熵最优。

## 结尾与主文分工

§5 p.9以选择建议收束：MaxPro适用于本文函数逼近情境，若均匀性重要可选MaxProLHD。没有独立Discussion，随后两个证明附录。结束段回答如何选，而非重述全部结果。

## 可迁移写作动作

设计准则的文章可沿实际未知因素、可计算平均、解析准则、搜索实现、多个决策指标的证据链组织；诚实报告基准在其擅长指标上胜出，比泛称新法优越更清楚。

## 不能泛化的特殊安排

适用背景是确定性计算机试验及少量活跃因子；不能把该文对均匀性与函数逼近的区分搬成所有积分任务的通用结论。本文没有同时统治全部指标。
