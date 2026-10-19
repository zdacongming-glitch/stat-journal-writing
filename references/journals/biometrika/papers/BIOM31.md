# BIOM31 · Improving efficiency and robustness of the doubly robust estimator for a population mean with incomplete data

题录：Weihua Cao; Anastasios A. Tsiatis; Marie Davidian（2009），*Biometrika* 96(3)，723-734。[DOI](https://doi.org/10.1093/biomet/asp033)。

文章类型：regular methodological and theoretical article; published PDF read through web extraction。方向：missing-data, doubly-robust-estimation, causal-inference。

全文：[公开来源](https://academic.oup.com/biomet/article-pdf/96/3/723/38625237/biomet_96_3_723.pdf)。版本：published Biometrika 2009 PDF pp.723–734; full 746-line extraction obtained through web PDF reader, original PDF byte download unavailable。

阅读范围：All published PDF pages 723–734, complete extracted lines 0–745 preserved: summary, sections 1–6, all method explanations and comparisons, two simulation tables, discussion, misspecification heuristic appendix and references. Original PDF bytes unavailable; hash covers complete extracted UTF-8 text. Algebra not independently verified. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有302次引用，已有至少八年观察期；实际阅读全文后，作为missing-data, doubly-robust-estimation, causal-inference方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，302次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要从既有双重稳健估计的两种具体弱点进入：两个模型均错时偏差及极端权重，随后给替代估计的比较目标。用可比较的表现说明改进，未暗示双重稳健能容许任意两个错模型。

## 引言的推进

§1 pp.723–724先把缺失结局和因果均值放到同一问题，简述单模型估计与增广IPW来源，再定义双重稳健。最近邻模拟反例具体指出失效机制，贡献句因此自然落在改进估计而非泛称新框架。

## 方法、定义与理论的依赖

§2 pp.724–725重建公共增广形式，区别两个模型均对、只一者对时辅助参数估计的重要性。§3 pp.725–728先固定倾向得分，比较OLS与经验方差最小化各自丢失哪个目标，再给加权方程同时实现；放松为估计得分后，明确影响函数多出投影项并推导联合估计方程。与Tan方法在同一形式下精确比较，最后交代sandwich方差。§4 p.729另解极端权重，以额外约束构造增强得分模型。

## 数值、应用与证据

§5 pp.729–730及表1–2 pp.731–732复现触发争论的两套近似错设场景，交叉四种模型正确性和两个样本量。偏差、RMSE、绝对误差、估计与实际标准差、覆盖率分开，明确两个模型均错时某些区间仍欠覆盖；没有把点估计改善说成推断问题已经全部解决。

## 结尾与主文分工

§6 pp.730–733把单处理均值推广到均值差时区分线性与非线性结果模型，不能简单相减时另需推导；再比较权重稳定化，指出某一模型正确时已无可获效率收益。附录p.733只给局部错设下的启发式偏差界，并明说较小上界不保证逐点偏差更小。

## 可迁移写作动作

改进型论文可先在简化情形隔离两个设计目标，再显示自然做法各缺一个目标，最后推广到现实估计环境；把稳定性改进与效率改进拆成两个具体任务。对最近邻反例直接复现，使模拟回应引言问题。

## 不能泛化的特殊安排

“最优”限定于指定估计类及倾向模型正确时的渐近方差。启发式错设界不等于一般鲁棒性定理；均值差的简单相减结论受线性结果模型条件约束。当前未取得PDF原字节，不宣称其散列。
