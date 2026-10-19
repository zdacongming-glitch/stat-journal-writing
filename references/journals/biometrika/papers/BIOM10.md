# BIOM10 · Square-Root Lasso: Pivotal Recovery of Sparse Signals via Conic Programming

题录：Alexandre Belloni; Victor Chernozhukov; Lie Wang（2011），*Biometrika* 98(4)，791-806。[DOI](https://doi.org/10.1093/biomet/asr043)。

文章类型：regular methodological and theoretical article; revised author version with supplementary appendix。方向：high-dimensional-regression, pivotal-regularization, square-root-lasso。

全文：[公开来源](https://arxiv.org/pdf/1009.5689)。版本：arXiv:1009.5689v5, 2011-12-18; 35-page PDF combining main article and supplementary appendix。

阅读范围：All main narrative pp.1–12 and supplementary narrative pp.19–25, conditions/theorem statements, conic formulation, all numerical and computational comparisons, end figure captions; proof organization pp.13–17 and 25–30 consulted without independent algebra verification; references inspected. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有635次引用，已有至少八年观察期；实际阅读全文后，作为high-dimensional-regression, pivotal-regularization, square-root-lasso方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，635次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要围绕未知噪声下的pivotal调参、与已知噪声lasso同阶风险、非高斯可用条件以及凸锥计算四件实质信息，统计与计算目标各自有随后结果。

## 引言的推进

§1 pp.1–3从稀疏线性模型直接进入，先给已有lasso保证及其中未知噪声的位置，再定义平方根损失和无噪声参数的罚水平；最后交代两项主结果及固定设计记号。未用长篇应用重要性铺垫。

## 方法、定义与理论的依赖

§2 pp.3–6用score为何pivotal解释调参原则，再给正态模拟分位数与非正态精确/半精确/渐近选项；不同矩条件带来的维度增长代价紧邻结论。§3 pp.7–9先讲受限特征值的几何意义和可满足例，再给有限样本界及渐近推论。§4 pp.9–10以强对偶定理把估计器连接可计算锥规划，同时解释对偶变量的统计含义。

## 数值、应用与证据

§5 pp.10–12首先用已知噪声不可行lasso作为理论校准，随噪声变化比较风险、漏选与多选，并解释更重有效惩罚的偏差及选后OLS改善。补充B–C pp.20–25细分算法实现，承认没有统一初始化/停止规则就不能比较求解器优劣；还报告交叉验证风险可胜默认调参，但选模与计算成本不同。

## 结尾与主文分工

无独立Discussion，§5尾部用额外实验和后续非参数工作收束，随后说明补充材料分工。主理论证据与更广数值比较分开，不能将补充的经验调参当主定理默认。

## 可迁移写作动作

方法变换应由被消去的未知量解释，定义之后立即展示它如何改变score和可行调参；把统计有效性与求解可行性分别做成结果。比较时区分不可实现oracle、实际竞争法、后处理和不同目标。

## 不能泛化的特殊安排

pivotal针对噪声尺度，并不等于任意误差分布完全无条件分布自由；非高斯增长条件及固定设计角色需保留。半罚水平的经验优势没有得到默认罚水平的同一保证。
