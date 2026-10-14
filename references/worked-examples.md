# 改写示例：依据事实改变表达

以下英文均为本技能原创示例，**不是经典论文原句，也不是实际研究结果**。每例的“给定事实”是用于演示的假设输入，只能据此理解修改动作；不能将这些事实、结论或编号复制进真实稿件。对未提供的事实，不用范例代填。

## A. 摘要：从活动清单变成结果

**给定事实**：研究独立观测下存在随机缺失时的总体均值区间；观测概率已知且有正下界，另有规定的矩条件；证明的是渐近名义覆盖率；所考察模拟中区间比逆概率加权区间短，经验覆盖率相近。没有有限样本覆盖或最优长度定理。

原稿：

> We propose a novel and powerful method for missing data. Theoretical properties are established, and extensive simulations demonstrate the superiority of our approach.

改写：

> We study confidence intervals for a population mean when independent observations are missing at random. With known observation probabilities bounded away from zero and the stated moment conditions, the proposed intervals attain their nominal coverage asymptotically. In the simulation settings examined, they are shorter than inverse probability weighted intervals and have similar empirical coverage.

**为什么这样改**：明确对象、条件和证据；将没有定义的 superiority 拆成区间长度与覆盖率；不增添最优性或有限样本保证。此版本没有缩写、引用或公式，可作为进一步适配 JRSS-B 或 Biometrika 摘要的起点，但不是所有论文的固定三句模板。

## B. 引言：用比较轴连接文献与方法

**给定事实**：当前问题是估计纵向数据的均值参数；工作独立法在指定条件下一致，某些相关结构下效率损失大；新方法估计一个受约束的工作相关结构；没有证据支持其普遍更高效。

原稿：

> Many methods have been proposed for longitudinal data. However, existing methods have several limitations. To overcome these limitations, we develop a flexible new framework.

改写：

> Working independence permits estimation of the mean parameters without specifying the within-subject correlation. It can, however, lose precision when observations within a subject are strongly correlated. We therefore estimate a restricted working correlation structure and use it to construct the estimating equations. This construction aims to recover precision while limiting the number of nuisance parameters.

**为什么这样改**：先承认已有方法解决了什么，再指出与本文有关的限制，并说明新构造的目的。“aims to”没有把目标冒充已证明的普遍性质。真实稿件还须在相应位置补上作者已核实的文献与证据，不能编造引用键。

## C. 定理解读：保留渐近与点态范围

**给定事实**：定理仅在假设 A1–A4、固定维度下，对每个固定参数给出估计量的渐近正态性；没有一致覆盖结论或增长维度理论。

原稿：

> Theorem 2 guarantees valid inference for all dimensions and all sample sizes.

改写：

> Under Assumptions A1–A4 and with the dimension fixed, Theorem 2 establishes asymptotic normality at each fixed parameter value. It provides a basis for pointwise asymptotic inference; uniform validity and growing dimensions are not covered by this result.

**为什么这样改**：限定词承载数学含义。真实任务中应说明原句扩大了定理范围，而不将这项修正伪装成普通语法润色。若连方差可估计性等推断条件都未提供，不进一步声称某个具体区间已有效。

## D. 数值结果：优势、反例和统计显著性分开

**给定事实**：三组模拟中，方法 A 在两组的平均预测误差小于方法 B，在第三组较大；未提供 Monte Carlo 标准误；没有一般风险排序定理。

原稿：

> Method A significantly outperforms all competitors and is robust across a wide range of settings.

改写：

> Method A has lower average prediction error than method B in two of the three settings examined, but higher error in the third. These results indicate that its advantage depends on the data-generating setting.

**为什么这样改**：删去没有依据的显著性、比较对象扩张与稳健性；保留负面结果。还需要作者提供误差的不确定性及第三组设定，才能解释差异是否稳定、机制是什么。

## E. Biometrika：删除章节预告，不制造替代内容

原稿：

> The rest of the paper is organized as follows. Section 2 introduces the model. Section 3 presents the estimator. Section 4 gives the theory, and Section 5 reports simulations.

**编辑动作**：删除本段。这依据当前 Biometrika 风格说明，不是因为所有期刊都禁止导航。

只有在给定事实确实需要一个逻辑衔接时才补句。例如，若作者已说明“识别只需均值约束，计算另用工作相关结构”，可写：

> We first separate the assumptions needed to identify the mean parameters from the working correlation structure used for estimation.

这句话解释后续顺序的统计理由；没有对应事实时不添加。历史经典论文含有章节导航，不能推翻当前官方说明。

## F. 稳健性与因果：把容易混淆的对象说清楚

**给定事实**：估计方程在均值模型正确及其余规定条件下，允许工作相关结构误设；未允许均值误设。

原稿：

> The estimator is robust to model misspecification.

改写：

> The estimator remains consistent when the working correlation structure is misspecified, provided that the mean model is correct and the remaining assumptions hold.

**为什么这样改**：稳健的对象是工作相关结构，不是整个模型。这种对象层面的改写比增加 generally、potentially 等模糊词更准确。

另一个常见原句是 “Covariate balance ensures unbiased causal estimates.” 若给定材料只有观测协变量的平衡诊断，可改为：

> The adjustment improves balance in the observed covariates. A causal interpretation additionally requires the stated identification assumptions.

应在修改说明中指出：若稿件尚未给出识别假设，第二句仍需作者补充依据；不得替作者假定无未观测混杂、重叠性或其他研究所需条件。

## G. 未知 JASA 现行限字：继续改写，不伪称核实

用户要求“将摘要按 JASA 现行要求压缩”，但官方作者页无法访问。

**正确处理**：先给内容准确、明显更精炼的摘要并报告实际词数；在正文外说明现行限字尚未核实，链接官方作者页。用户已经指定 200 词时，可以按用户给定约束完成，不必再次询问，但不能把这称为已核实的官方要求。

**错误处理**：从标注过时的 Overleaf 模板读到一个数值便称其为现行规定；或因此停下所有文字修改。

## H. 只要求语言润色：尊重修改范围

用户要求“保留结构，只修改英文”，原文统计含义清楚而语言冗长。

原稿：

> It is important to note that the proposed estimator has the property that it is invariant under a change in the units of measurement.

改写：

> The proposed estimator is invariant to changes in measurement units.

无需重新安排章节、补模拟或输出完整投稿清单。若不变性本身尚无依据，在正文外提示需要核对，不擅自删除或改成一个不同的数学性质。
