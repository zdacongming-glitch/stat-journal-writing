# BIOM11 · Adaptive approximate Bayesian computation

题录：Mark Beaumont; Jean‐Marie Cornuet; Jean‐Michel Marin; Christian P. Robert（2009），*Biometrika* 96(4)，983-990。[DOI](https://doi.org/10.1093/biomet/asp052)。

文章类型：methodological correction and computational contribution; historical category not established from author version。方向：likelihood-free-inference, monte-carlo。

全文：[公开来源](https://arxiv.org/pdf/0805.2256)。版本：arXiv:0805.2256v9, 2009-03-28 author version; generated template header is not publication metadata。

阅读范围：Author PDF pp.1–8: complete narrative, weight derivation, algorithm, both illustrations, computational comparison, conclusion and references; derivations read for dependencies, not independently proved. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有613次引用，已有至少八年观察期；实际阅读全文后，作为likelihood-free-inference, monte-carlo方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，613次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要先承认顺序ABC的效率潜力，指出特定权重偏差，再说明重要性采样修正和自适应尺度，最后报告群体遗传示例的比较。批评对象精确，不把整个SMC框架判错。

## 引言的推进

§1 pp.1–3从似然不可计算切入，给拒绝ABC的精确与容差目标；介绍MCMC版本后，混合分布例子区分链收敛慢与容差近似误差。随后写出被检验的权重式(1)，才提出偏差判断及本文修正。

## 方法、定义与理论的依赖

§2 pp.3–4先在零容差、前代样本正确的有利情形分析偏差，再回到非零容差图示，防止把错误归因于近似目标。§3.1 pp.4–6由实际混合提议密度导出正确权重，再给尺度选择和可执行算法。

## 数值、应用与证据

§3.2复用混合例证明修正击中原缺陷；§3.3 pp.6–7的群体遗传问题明确只报告可识别参数组合。比较统一先验、最终回归调整和计算时间，图2报告重复运行稳定性，未把单例优势宣称为普遍优越。

## 结尾与主文分工

§4 p.8增加实际停止思路：核参数稳定与容差序列控制分别处理。没有逐段复述推导。

## 可迁移写作动作

纠错型文章把被纠正公式、目标分布与一个隔离混淆因素的例子前置；同一例子在修正后复用，可缩短论证而不牺牲说服力。算法复杂度之后解释实际主要成本。

## 不能泛化的特殊安排

文中对比很多，因为偏差修正是贡献本体；不能以转折密度评价机器味。该作者稿页眉年份有模板残留，只以DOI题录核定2009发表年。
