# 改写示例：删去无用解释，保留技术含义

以下均为原创演示。给定事实是示例输入，不是文献原句或实际研究结果；不能移植其中的结论和编号到真实稿件。示例用于判断具体改法，不作固定句式模板。

## A. 无损删除同义复述

语境：正文已定义估计量，并说明其单位变换不变性。

原稿：

> The estimator is invariant to changes in measurement units. This means that changing the units in which the variables are measured does not alter the result of the estimation procedure.

修订：

> The estimator is invariant to changes in measurement units.

第二句没有新增信息，直接删除。若面向非统计读者确实需要说明，改用有用的具体例子；不在重复定义后再追加一层解释。

## B. 删除虚设对立

给定事实：论文刻画一个已知估计量的极限分布；当前段落无需澄清该估计量的贡献归属。

原稿：

> Our contribution is not a new estimator, but a characterization of its limiting distribution.

修订：

> We characterize the limiting distribution of the estimator.

若估计量由哪篇文献提出影响贡献判断，应在文献比较中准确归属；不通过虚设对立制造重要性。

## C. 保留有作用的比较

给定事实：指定模拟中，方法 A 在三种设定中的两种预测误差较低，第三种较高；没有一般风险排序定理。

原稿：

> Method A has lower prediction error than method B in two of the three settings, but higher error in the third. These results indicate that the relative advantage of the two methods depends on the setting under consideration.

修订：

> Method A has lower prediction error than method B in two of the three settings, but higher error in the third.

保留承载真实结果差异的 but，删除重复总结。若作者提供第三种设定的机制证据，可以解释原因；不凭结果编造机制。

## D. 定理后的文字由上下文决定

给定事实：假设 A1–A4 与固定维度已在本节设定中明确给出，定理 2 证明每个固定参数处的渐近正态性。

原稿：

> Under Assumptions A1–A4 and with the dimension fixed, Theorem 2 establishes asymptotic normality at each fixed parameter value. It provides a basis for pointwise asymptotic inference; uniform validity and growing dimensions are not covered by this result.

在这组上下文中可以写：

> Theorem 2 establishes pointwise asymptotic normality of the estimator.

如果定理本身已经清楚表达这一结论，而且此句只作复述，连这句也可以删去。若原稿曾错误声称有限样本保证或一致有效性，须纠正该实质错误，并在作者说明中解释；不能将纠错用的限制清单变成所有正文的默认尾句。

没有给定方差估计条件时，不从渐近正态性擅自增加某个置信区间有效的主张。

## E. 摘要把活动换成已有结果

给定事实：独立观测在随机缺失条件下估计总体均值；观测概率已知且有正下界，满足规定的矩条件；已证明渐近名义覆盖，报告的模拟中区间比逆概率加权区间短、经验覆盖相近。

原稿：

> We propose a novel and powerful method for missing data. Theoretical properties are established, and extensive simulations demonstrate its superiority.

修订：

> We construct confidence intervals for a population mean with observations missing at random. With known observation probabilities bounded away from zero and under the stated moment conditions, the intervals attain nominal coverage asymptotically. In the reported simulations, they are shorter than inverse probability weighted intervals and have similar empirical coverage.

这些限定承载本例的实际理论范围，不能为简洁删去。也不补写没有提供的最优性或有限样本保证。真实摘要依其重要结果和目标刊要求另行组织。

## F. 条件引用清楚时，避免再次铺开

语境：本节的假设已经明确要求均值模型正确，并给出一致性的其余条件；结论允许工作相关结构误设。

原稿：

> The estimator remains consistent when the working correlation structure is misspecified, provided that the mean model is correct and the remaining assumptions hold.

可以收紧为：

> The consistency result allows misspecification of the working correlation structure.

脱离上述上下文时，这个短句可能缺条件，应恢复必要设定。删除依据是语境已经提供信息，不能据此将所有条件移出正文。

## G. 术语相近时先查定义

给定事实：定理控制 false discovery rate，数值表记录每次实验的 false discovery proportion。

处理：核验原始定义，保留 FDR 与 FDP 的区别；表题和结果叙述使用对应对象。不能为保持同一英文词而将两者合并，也不能为了避免重复给同一个量轮换名称。

若没有已核验来源，先按 [terminology-protocol.md](terminology-protocol.md) 检索。来源和核对过程进入资料表，正文只使用准确名称与必要引用。

## H. 删除导航段后不自动补一段

原稿：

> The rest of the paper is organized as follows. Section 2 introduces the model. Section 3 presents the estimator. Section 4 gives the theory, and Section 5 reports simulations.

目标刊的当前风格要求不使用此类预告，或此段不帮助理解时，删除整段。只有确实缺少逻辑衔接且有给定事实时才补过渡，不用同样长度的另一种预告代替。

## I. 成熟句子保持不变

给定事实支持以下陈述，且上下文已清楚定义模型和估计量：

> The estimator is invariant to changes in measurement units.

保留原句。不要为展示修改幅度加入 importantly、a key property 或重复解释，也不强行换成更长的同义表达。

## J. 独立删改后接入统一去水印

按 [final-cleanup.md](final-cleanup.md) 对选定正文做一次忠实语言整理，文件另经 inspect 和保守 Unicode 清理；保留原件与独立结果。核对术语、公式、引用和数值，再选定终稿。

隐藏字符清理与语言整理分别记录实际效果。没有可验证的统计水印检测器时，不把流程完成写成统计水印已被验证去除。