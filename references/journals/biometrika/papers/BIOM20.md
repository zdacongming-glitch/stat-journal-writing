# BIOM20 · Sparse Bayesian infinite factor models

题录：Anirban Bhattacharya; David B. Dunson（2011），*Biometrika* 98(2)，291-306。[DOI](https://doi.org/10.1093/biomet/asr013)。

文章类型：regular Bayesian methodology article; complete PMC author manuscript。方向：bayesian-factor-models, shrinkage-priors, covariance-estimation。

全文：[公开来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC3419391/)。版本：complete author manuscript in PMC, linked to 2011 Biometrika publication; includes proof appendix。

阅读范围：All HTML main narrative sections 1–5, summary, prior/property statements, Gibbs steps 1–6 separately inspected in HTML lists, adaptive computation, stochastic EM, all simulation and clinical application narrative/captions, appendix proof organization; algebra not independently checked. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有414次引用，已有至少八年观察期；实际阅读全文后，作为bayesian-factor-models, shrinkage-priors, covariance-estimation方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，414次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要按稀疏协方差目标、新先验、顺序收缩与参数扩展、共轭计算、自适应截断、理论及预测应用推进；信息丰富但没有把无限模型与实际有限计算混为一谈。

## 引言的推进

§1由因子模型协方差分解进入，区分解释潜在因子与高维降维用途；再指出常用识别约束的顺序依赖、既有采样混合及因子数推断困难。核心认识是目标若为协方差/预测就未必要识别载荷，随后给扩展参数及递增收缩的具体作用。

## 方法、定义与理论的依赖

§2.1先定义无限载荷的合法空间及到协方差的映射，再给先验；§2.2依次论证合法性、截断误差、支持与弱一致性、顺序不变和矩，结果围绕模型能否定义、能否计算和覆盖哪些目标组织。§3先固定截断的共轭更新，再自适应增删因子，交代递减适应要求；近似MAP另列为快速工作估计。

## 数值、应用与证据

§4先估计因子数与协方差，再用同一生成设置转到预测、回归系数和变量选择；明确真载荷没有从所提先验生成，另做相关因子/误差和超参数敏感性。与elastic net预测相近，同时给预测区间，这是能力差别而非均方误差全面优势。§5对淋巴瘤删失生存时间说明移位、变换、插补及训练验证划分；承认基因只解释少量变异，区间很宽且预测误差与lasso相当。

## 结尾与主文分工

无独立Discussion，以应用的有限预测能力及敏感性结果结束，随后证明附录。文章最后保留不令人兴奋但科学上关键的预测限制。

## 可迁移写作动作

贝叶斯模型论文可把先验合法性、逼近误差和计算更新排成一条依赖链；应用必须允许科学问题给出有限预测价值，不能因为方法新就把相关组选择写成可靠预后。

## 不能泛化的特殊安排

载荷不可识别可接受是因为目标为协方差与预测，不能套到需要解释单个因子的研究。连续收缩先验没有真实点质量，变量选择另需阈值。原文随机递增和适应算法相关数学主张仅作历史叙述观察，未作独立正确性复核。
