# BIOM17 · Scaled sparse linear regression

题录：Tingni Sun; Cun-Hui Zhang（2012），*Biometrika* 99(4)，879-898。[DOI](https://doi.org/10.1093/biomet/ass043)。

文章类型：regular methodological and theoretical article; revised author manuscript。方向：high-dimensional-regression, noise-level-estimation, scaled-lasso。

全文：[公开来源](https://arxiv.org/pdf/1104.4595)。版本：arXiv:1104.4595v2, 2012-06-21, 20 pages; template copyright/year placeholders not used as metadata。

阅读范围：Complete PDF narrative pp.1–20: summary, all main sections 1–5, algorithm and convex equivalence, oracle bounds and interpretations, post-selection least squares, both simulations, real-data evaluation, discussion, appendix proof strategy and references. Displays consulted, not independently proved. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有444次引用，已有至少八年观察期；实际阅读全文后，作为high-dimensional-regression, noise-level-estimation, scaled-lasso方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，444次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要先说系数与噪声联合估计及迭代平衡，再区分算法成本、凸性、理论风险与噪声渐近正态、选后扩展及数值证据；没有把所有性质都无条件赋予每一种凹惩罚。

## 引言的推进

§1 pp.1–2由未知噪声导致罚水平难选进入，比较交叉验证的目标；随后完整交代已有迭代、并行提出的Huber损失联系和缺少理论的空白。贡献是补足理论与证据，承认等价square-root lasso及独立工作，避免虚报首次提出。

## 方法、定义与理论的依赖

§2 pp.2–4先一般惩罚的平衡算法，再聚焦lasso的联合凸损失及尺度等变；§3.1 pp.4–7从粗噪声界到精细速率/正态，再把已有固定罚oracle界迁移，最后解释证明如何控制profile导数。§3.2 pp.7–9因lasso偏差引出选后最小二乘，明确只需控制假阳性而非完全选模一致性。

## 数值、应用与证据

§4 pp.10–15两个生成情形分别暴露调参过大/小和弱信号相关设计的困难，未掩盖scaled lasso噪声估计仍有偏；还标明借用既有模拟结果的部分没有重新实验。真实基因数据分开模型稳定性与预测误差，并保持各方法训练/验证划分可比。

## 结尾与主文分工

§5 pp.15–16讨论理论常数偏保守及设计条件下可模拟校准的更小罚水平，再列统一已有界的技术结果，证明附录承接。不是在Discussion才第一次提出关键目标。

## 可迁移写作动作

等价方法和同期工作应直接承认，贡献句聚焦自己新增的保证与使用范围；定理后解释界允许什么情形，再给下一更强结果。后处理理论可以利用弱于完全模型恢复的条件，需明确。

## 不能泛化的特殊安排

scaled concave penalty在算法与数值中出现，不等于本文为其全部提供了lasso同样的理论。噪声估计正态与系数推断不同；模板2008页眉不能改写2012正式发表年。
