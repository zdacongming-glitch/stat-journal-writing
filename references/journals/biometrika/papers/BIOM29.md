# BIOM29 · Efficient implementation of Markov chain Monte Carlo when using an unbiased likelihood estimator

题录：Arnaud Doucet; Michael K. Pitt; George Deligiannidis; Robert Kohn（2015），*Biometrika* 102(2)，295-313。[DOI](https://doi.org/10.1093/biomet/asu075)。

文章类型：regular computational theory article; repository accepted manuscript with supplement。方向：pseudo-marginal-mcmc, monte-carlo-efficiency, likelihood-estimation。

全文：[公开来源](https://wrap.warwick.ac.uk/104955/1/WRAP-efficient-Markov-chain-unbiased-likelihood-estimator-Pitt-2015.pdf)。版本：WRAP author-accepted pre-copyedited manuscript, explicitly marked accepted after peer review; 35 PDF pages including cover and supplement; formal publication 2015。

阅读范围：Complete main narrative PDF pp.2–14, all assumptions and bound interpretations, stochastic-volatility analysis; main proof organization pp.14–18 and supplement introduction inspected; supplementary quantitative discussion and numerical implementation pp.27–31 plus all end captions pp.33–35 read. Detailed auxiliary proofs pp.22–26 not read line by line or independently verified. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有266次引用，已有至少八年观察期；实际阅读全文后，作为pseudo-marginal-mcmc, monte-carlo-efficiency, likelihood-estimation方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，266次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要直接给粒子数与渐近方差的计算代价权衡，再把正态、方差反比粒子数、与参数无关三个近似假设放进建议的适用条件；没有把推荐常数说成普适最优。

## 引言的推进

§1 pp.2–3承认pseudo-marginal已有精确目标，真正未解是每次多少样本。最近邻最优结果分别受完美提议或高维特殊结构限制，因此本文改为一般提议下可计算上界；数值建议在引言已概括，但范围同句明确。

## 方法、定义与理论的依赖

§2 pp.3–4重建增广目标与对数似然噪声，解释参数无关假设不严格满足但何时可近似。§3 pp.4–11从Peskun支配的辅助链到jump-chain方差表示，再分离参数与噪声贡献，给复杂精确式及较简单界；§3.5才加正态假设，将界转成计算时间与可用粒子选择，严格区分原链和bounding chain。

## 数值、应用与证据

§4 pp.11–14先定义波动模型及粒子滤波，再实际检验两条关键近似假设：短序列不近似正态且噪声随参数变化，较长序列较好；最后才比较粒子数、低效因子与成本。补充F pp.28–30用Kalman可算真似然校准，明确真值在主例只能估算。图形不只展示最后性能，也审查理论假设。

## 结尾与主文分工

无独立Discussion，正文以成本与接受概率的检验收束，附录2进一步夹住最优区间；补充G交代常数如何数值计算。建议是带损失评估的折中，非必须恰等某个值。

## 可迁移写作动作

调参理论先定义需要最小化的实际资源，再说明优化真对象还是其界；若建议建立在近似假设上，数值应直接检查假设随样本和参数如何变化。可解析特例承担校准，复杂实例承担适用性。

## 不能泛化的特殊安排

似然估计须非负无偏，日志估计无偏不是同一要求。原链上界与辅助链下界不能混用；约1.2的对数似然噪声标准差建议依假设和成本模型，不能写成所有MCMC算法的标准。
