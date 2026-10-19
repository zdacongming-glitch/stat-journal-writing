# BIOM34 · Reduced rank regression via adaptive nuclear norm penalization

题录：Kun Chen; Hongbo Dong; Kung-Sik Chan（2013），*Biometrika* 100(4)，901-920。[DOI](https://doi.org/10.1093/biomet/ast036)。

文章类型：regular methodological and theoretical article; revised author manuscript。方向：reduced-rank-regression, matrix-regularization, adaptive-nuclear-norm。

全文：[公开来源](https://arxiv.org/pdf/1201.0381)。版本：arXiv:1201.0381v2, 2012-09-23, 28 pages; formal journal publication 2013。

阅读范围：Complete main narrative pp.1–19, matrix approximation and convexity/closed-form results, regression construction, rank and risk bounds, ridge extension, both simulation designs and genomics application, discussion; appendix proof narrative pp.19–24 and references inspected without independent algebra checking. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有247次引用，已有至少八年观察期；实际阅读全文后，作为reduced-rank-regression, matrix-regularization, adaptive-nuclear-norm方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，247次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要先定义自适应奇异值权重，突出自然排序下非凸但仍有显式全局解，再连接低秩回归、连续路径、统计界和实例；计算可解性是本篇实质结果。

## 引言的推进

§1 pp.1–3从多响应回归和低秩结构进入，在统一惩罚形式下比较秩惩罚与核范数，借SVD坐标解释硬/软阈值的取舍。贡献由两项设计选择组成：自适应权重，以及惩罚预测矩阵而非直接惩罚系数矩阵。

## 方法、定义与理论的依赖

§2 pp.3–6先在矩阵逼近的简化问题复习硬软阈值，证明权重顺序决定凸性，再给非凸问题全局显式解。§3 pp.6–8用投影恒等式迁移至回归，紧接路径和CV。§4 pp.8–11将秩恢复归约为最小信号与最大投影噪声，给一致性与风险界，再解释两类权重；§5 pp.11–12的ridge扩展为效率及相关设计服务，理论明确留待后续。

## 数值、应用与证据

§6 pp.12–18同时报告预测、系数、秩和成本，分开大独立验证集上的理想调参与实际CV；信号与相关性变化揭示核范数或秩惩罚何时更有利，承认新法秩选择有时稍差。基因组应用比较CNV→表达与反向预测，解释科学目的差异并承认第一种设定接近零信号。

## 结尾与主文分工

§7 pp.18–19把直接惩罚系数、迭代重加权、额外ridge理论和广义模型列为具体后续问题；没有把已计算出的扩展自动授予主定理。

## 可迁移写作动作

当自然设计破坏凸性时，正面给出条件和仍然可解的原因，比回避非凸更有说服力。先解简化问题再投影回归，定义与证明依赖清楚；比较理想方法潜力与实际调参应分别呈现。

## 不能泛化的特殊安排

“adaptive nuclear norm”是论文既有术语，但自然权重下数学上已不再是矩阵范数，这一明确说明不能为术语整齐删掉。预测风险与系数误差需不同设计信息；ridge扩展的理论并未在本文完成。
