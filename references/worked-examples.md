# 改写示例：补清论证，删去无用解释

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

给定事实：假设 A1–A4 与固定维度已在本节设定中明确给出，定理 2 证明每个固定参数处的渐近正态性。目标、必要定义与这些设定在正文中已有充分信息，读者不必查补充材料才能理解结论范围。

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

语境：正文已明确要求均值模型正确，并充分给出一致性的其余条件、目标及结论范围；结论允许工作相关结构误设。以下删减以只读正文即可理解这些信息为前提。

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

在用户未明确要求保留的前提下，若经当次核验的目标刊风格要求不使用此类预告，或此段不帮助理解，删除整段。只有确实缺少逻辑衔接且有给定事实时才补过渡，不用同样长度的另一种预告代替。用户明确保留导航段时按其要求处理；投稿风格检查可在正文外说明已核实的差异，不把旧建议当作删除授权。

## I. 成熟句子保持不变

给定事实支持以下陈述，且上下文已清楚定义模型和估计量：

> The estimator is invariant to changes in measurement units.

保留原句。不要为展示修改幅度加入 importantly、a key property 或重复解释，也不强行换成更长的同义表达。

## J. 独立删改后接入统一去水印

按 [final-cleanup.md](final-cleanup.md) 对选定正文做一次忠实语言整理，文件另经 inspect 和保守 Unicode 清理；保留原件与独立结果。核对术语、公式、引用和数值，再选定终稿。

隐藏字符清理与语言整理分别记录实际效果。没有可验证的统计水印检测器时，不把流程完成写成统计水印已被验证去除。

## K. 交代新对象的构造及其用途

给定事实（虚构教学场景）：$X_1,\ldots,X_n$ 为独立同分布观测，总体均值为 $\mu$，样本均值为 $\bar X_n$。本段首次引入 $S_n$，用于分析样本均值的缩放误差；此前尚未给出其构造。

问题写法：

> The analysis proceeds through a summary $S_n$ of the random variation in the data.

修订：

> Define $S_n=n^{-1/2}\sum_{i=1}^n(X_i-\mu)$. Since $S_n=\sqrt n(\bar X_n-\mu)$, its distribution describes the scaled estimation error of the sample mean.

修订给出观测怎样形成对象，以及该对象为什么进入当前分析。它没有仅用另一个抽象名称替换 summary。

何时应保持不改：若前文已经给出上述构造及用途，后文的 “We next study the distribution of $S_n$.” 可以保留，不必再次展开求和或重复解释随机性来源。

## L. 在需要解释新关系时保留推导桥梁

给定事实（虚构教学场景）：已有 $\sqrt n(\bar X_n-\mu)\to_d Z$，其中 $Z\sim N(0,\sigma^2)$、$\sigma^2>0$。对当前光滑函数 $h$，已得到 $h'(\mu)\ne0$ 及一阶展开

$$
h(\bar X_n)-h(\mu)
=h'(\mu)(\bar X_n-\mu)+o_p(n^{-1/2}).
$$

本段承担说明变换怎样影响极限方差的任务，尚未向读者展示这一联系；上述展开是本例给定输入，不是写作时补出的新结果。

问题写法：

> Therefore, the limiting variance is $h'(\mu)^2\sigma^2$.

修订：

> Multiplying the expansion by $\sqrt n$ gives

$$
\sqrt n\{h(\bar X_n)-h(\mu)\}
=h'(\mu)\sqrt n(\bar X_n-\mu)+o_p(1).
$$

> The leading term converges to $h'(\mu)Z$, whose variance is $h'(\mu)^2\sigma^2$.

这里保留了中心、缩放和极限变量之间的联系。不能仅把 therefore 换成 hence，便认为补上了缺失推理。

何时应保持不改：若这一展开已在紧邻上文出现，或本段只需调用已经说明的 delta method，简短给出结果即可；不为每次标准定理调用增加教学式推导。

## M. 正文保留判断区间有效性所需的条件

给定事实（虚构教学场景）：$X_1,\ldots,X_n$ 的均值为 $\mu$，样本均值为 $\bar X_n$，重抽样均值为 $\bar X_n^*$。正文已定义普通非参数 bootstrap：从经验分布有放回抽取 $n$ 个观测，并用 $B_n$ 个条件独立重抽样所得的 $\sqrt n(\bar X_n^*-\bar X_n)$ 的分位数构造双侧 basic bootstrap 区间。两目标概率为 $\alpha/2$ 和 $1-\alpha/2$，其中 $0<\alpha<1$。本例已给定并证明：在独立同分布、有限正方差条件下，缩放均值误差及其条件 bootstrap 分布具有同一正态极限；$B_n\to\infty$ 时两经验分位数一致。正文尚未解释这些条件及其作用。

问题写法：

> The supplement establishes the validity of this bootstrap construction.

修订：

> For independent identically distributed observations with finite positive variance, the conditional distribution of $\sqrt n(\bar X_n^*-\bar X_n)$ approaches the same normal limit as $\sqrt n(\bar X_n-\mu)$. The limiting distribution function is continuous and strictly increasing, and $B_n\to\infty$ makes the two empirical quantiles consistent. The resulting interval has limiting coverage $1-\alpha$; the proof is given in Supplement S1.

必要条件及分位数为何稳定留在正文，完整条件论证与证明仍可在补充材料。不能把本例的 bootstrap 有效性推广到未给定的重抽样方案或统计量。

何时应保持不改：若正文已经说明采样、矩条件、分位数稳定性及模拟次数要求，单独的证明出处可以保持简短。无需在每次提及该区间时重列这些条件。

## N. 描述方法组合，不把组合简称当成标准名称

给定事实（虚构教学场景）：有 $G$ 个独立聚类，$\widehat\theta_G$ 估计标量目标 $\theta$。正文已定义按聚类贡献计算的方差估计 $\widehat V_G$，并给定学生化极限 $(\widehat\theta_G-\theta)/\sqrt{\widehat V_G}\to_d N(0,1)$。区间采用标准正态分位数 $z_{1-\alpha/2}$，其中 $0<\alpha<1$。未给出 cluster-Gaussian 是固定方法名的依据；本例不声称已核验任何特定文献。

问题写法：

> We apply the cluster-Gaussian method.

修订：

> Our benchmark is the Wald interval

$$
\widehat\theta_G
\ \pm\ z_{1-\alpha/2}\sqrt{\widehat V_G},
$$

> where $\widehat V_G$ is computed from the independent cluster contributions defined above.

修订说明区间形式与方差估计的关系。真实稿件若采用已有构造，应核验其公式和原始出处；不能由两个常见词自行合成一个公认方法名，也不能编造引文。图表需要 CG 等短标签时，应声明它只是本文对该区间的标签。

何时应保持不改：已有名称与定义经可靠来源核验，或图注已经清楚定义局部标签时，可以沿用。不能因为名称含连字符或图中使用缩写就机械改名。

## O. 准确归属性质，并保持表示的名称承接

给定事实（虚构教学场景）：在约束 $\theta\ge0$ 下最小化样本平方损失，得到 $\widehat\theta_n=\max(0,\bar X_n)$。实函数 $t\mapsto\max(0,t)$ 是投影到非负半轴的映射，连续且分段仿射；平方损失 $(x-\theta)^2$ 对 $\theta$ 光滑。

问题写法：

> The squared loss has a kink at zero. The estimator has the projection form $\widehat\theta_n=\max(0,\bar X_n)$. This clipping law simplifies its computation.

修订：

> The constraint $\theta\ge0$ gives the projection formula $\widehat\theta_n=\max(0,\bar X_n)$. The projection changes slope at zero; the squared loss remains smooth in $\theta$.

后文可用 this projection formula 承接，不另起一个未经说明的 clipping law。参数约束是条件，投影公式是由约束及准则得到的表示；二者不应为统一措辞而混成同一个对象。对损失的错误性质应纠正，并在修改说明中明示。

何时应保持不改：正文已分清损失与投影，并用稳定名称指代该表示时，无需再次增加一段区分。若另有技术操作采用不同名称，应保留其准确名称并说明关系，不作全篇词语替换。

## P. 让理论层级和标题服务于具体推断任务

给定事实（虚构教学场景）：前节给出一般估计方程的渐近展开；当前节将其用于独立同分布观测下的总体位置参数 $\theta_0$，所用得分函数 $\psi(x,\theta)$ 已定义。本例给定 $E\{\psi(X,\theta_0)\}=0$、$a=-E\{\partial_\theta\psi(X,\theta_0)\}\ne0$、$b=\operatorname{var}\{\psi(X,\theta_0)\}>0$，已证明 $\sqrt n(\widehat\theta_n-\theta_0)\to_d N(0,b/a^2)$，且 $\widehat a,\widehat b$ 一致。这里 $z_p$ 为标准正态分位数，$0<\alpha<1$。一个更一般的余项验证引理已有完整证明，但不是当前节的主要贡献。

问题写法：

> **Computational inputs and theoretical checks**
>
> We introduce the location estimator, state a general remainder lemma for estimating equations, and then return to the location problem to construct an interval.

修订：

> **Confidence intervals for a location parameter**
>
> For this location score, $a=-E\{\partial_\theta\psi(X,\theta_0)\}$ and $b=\operatorname{var}\{\psi(X,\theta_0)\}$. Substituting these quantities into the preceding expansion yields asymptotic variance $b/a^2$. Using the consistent estimates $\widehat a$ and $\widehat b$, we obtain

$$
\widehat\theta_n
\ \pm\ z_{1-\alpha/2}
\sqrt{\frac{\widehat b}{n\widehat a^2}}.
$$

标题对应位置参数的推断任务。正文沿一般结果的具体使用推进；一般验证工具可在理论部分提前建立，或连同完整证明放入合适的补充位置，不在应用途中无解释地切换层级，也不随正文删减而丢弃。

何时应保持不改：若一般引理本身就是主要创新，保留主文的完整证明可能正是合适安排；若本节真正解决计算问题，计算导向的标题也可以成立。不能把本例推广成“所有引理都移到补充材料”或“所有标题都改成置信区间”。

## Q. 使搭配对应模型、拟合和损失的实际层次

给定事实（虚构教学场景）：训练数据 $D$ 包含正的持续时间观测。拟合程序将 $D$ 映射到指数分布的参数估计 $\widehat\lambda=1/\bar X_D$，拟合密度为 $p_{\widehat\lambda}(x)=\widehat\lambda\exp(-\widehat\lambda x)$，$x>0$。评价一个新观测 $x$ 时，计算负对数损失 $-\log p_{\widehat\lambda}(x)$。

问题写法：

> We estimate the procedure $p_{\widehat\lambda}$ and fit its negative log loss at a new duration $x$.

修订：

> The fitting procedure returns the rate estimate $\widehat\lambda=1/\bar X_D$ and the fitted density $p_{\widehat\lambda}$. At a new duration $x$, we evaluate the negative log loss $-\log p_{\widehat\lambda}(x)$.

修订区分了从数据到拟合的程序、估计出来的参数、拟合密度与计算得到的损失；没有把 procedure 简单换成 model。

何时应保持不改：若上下文已定义上述程序，句子 “We evaluate the prediction risk of this fitting procedure over repeated training samples.” 可以保留，前提是该任务确实评价对训练样本再平均的程序风险。不能因同时出现 procedure 和 risk 就改成单次拟合的条件风险。

## R. 用已有观测记号补足关系

给定事实（虚构教学场景）：前文已经定义向量观测 $Z_i$ 的各分量。已知实值评分函数 $s$ 将一个这样的观测映射为标量，用于计算 $\bar s_n=n^{-1}\sum_{i=1}^n s(Z_i)$。当前段落只引入平均评分，不需要研究整个函数类。

问题写法：

> A summary $s$ of the measurements produces the average response $\bar s_n$.

修订：

> For the real-valued score $s(z)$, define the average score $\bar s_n=n^{-1}\sum_{i=1}^n s(Z_i)$.

已有观测定义与新公式共同说明输入和输出。无需重新拆开观测向量、引入另一套参数或为这个有限和增加函数空间假设。

何时应保持不改：上述评分及平均公式已清楚给出时，可以直接写 “We report $\bar s_n$ for each sample.” 若后续确实需要期望、函数类或可测性条件，应在相应位置准确陈述；不能把本例理解为这些条件永远不需要。

## S. 明确相似的是哪个量

给定事实（虚构教学场景）：两个估计量为 $A=\mu+\varepsilon$、$B=\mu-\varepsilon$，其中 $E\varepsilon=0$、$\operatorname{var}(\varepsilon)=\tau^2>0$。本段比较它们的期望与差的随机波动，不讨论渐近速率。

问题写法：

> The estimates match closely, so their difference has negligible variation.

修订：

> Both estimators have expectation $\mu$, but their difference is $A-B=2\varepsilon$ and has variance $4\tau^2$.

“期望相同”不能替代“随机变量之差很小”。这里的转折承担实际比较，应保留；发现原句结论与给定事实冲突时，应在作者说明中指出纠正。

何时应保持不改：若给定材料确已证明两个估计量之差在所述尺度上可忽略，且正文已交代尺度和条件，可以简短沿用该结论，不再重复上述反例。某个充分条件不满足，也不能单凭这一点宣布估计量之差必然不可忽略。

## T. 删除没有作用的公式重复，保留数学依赖

给定事实（虚构教学场景）：$a_1,\ldots,a_m$ 是固定正数，权重为 $w_i=a_i/\sum_{j=1}^m a_j$，后文使用 $T=\sum_{i=1}^m w_iY_i$。这里的任务只是定义加权统计量，没有后续交叉引用指向权重求和等式；后续方差结果要求权重固定。

问题写法：

> For fixed positive $a_i$, set $w_i=a_i/\sum_j a_j$. Hence $\sum_i w_i=(\sum_i a_i)/(\sum_j a_j)=1$. Signed or adaptively chosen weights could also be considered. We compute $T=\sum_i w_iY_i$.

修订：

> For fixed positive $a_i$, set $w_i=a_i/\sum_j a_j$ and compute $T=\sum_i w_iY_i$.

删去的是没有承担当前推导任务的代数复写和未研究的分支；固定权重的条件仍在。不能因两者都属于“限定”就一起删除。

何时应保持不改：若当前段落正利用 $\sum_iw_i=1$ 解释常数再现性质，或后文证明明确引用该等式，应保留所需关系及定位。是否简单不是删式标准；有用的解释也不必被迫改成正式定理。

## U. 让引用随论点移动，保持贡献连续

给定事实（虚构教学场景）：文献 A 说明不等概率抽样中估计中位数需要处理抽样权重；文献 B 已提供保守区间。本文在抽样概率已知为正及正文所列抽样设计和密度条件下，证明另一种总体中位数区间的渐近名义覆盖，但没有证明其宽度优于 B。A、B 只是教学占位符，不对应真实文献。

问题写法：

> We construct intervals for a population median. A explains the role of sampling weights in median estimation under unequal-probability sampling. Our intervals attain asymptotic nominal coverage. Existing research does not provide interval procedures for this problem; B studies conservative intervals.

修订：

> A explains how sampling weights enter median estimation under unequal-probability sampling, and B provides conservative intervals. With known positive sampling probabilities and under the stated design and density conditions, we construct intervals for the population median that attain nominal coverage asymptotically.

修订承认已有办法，把抽样背景置于其作用位置，连续说明本文对象与结果；没有凭措辞增加宽度优势或全局首创性。真实稿件还应依据实际证据说明与最邻近工作的具体差别，不能从本例补造差别。

何时应保持不改：引言已按论证任务组织、文献就近支撑判断时，保留现有顺序。为准确说明本文构造所需的出处可以留在贡献段；不把“贡献连续”执行成该段不能引用文献，也不规定每篇文章都必须按本例顺序写。

## V. 把开放问题限定到实际目标和保证

给定事实（虚构教学场景）：本文区间针对总体中位数，对每个固定的分布在给定条件下具有渐近名义覆盖；没有建立它在分布类 $\mathcal P$ 上的一致覆盖。其他工作已有总体均值的一致有效区间。若允许总体中位数趋近分布支撑边界，本文的分位数近似误差尚需额外控制；这指总体参数，不是观测到的样本中位数。

问题写法：

> Uniform intervals remain unavailable. When the estimated medians approach a boundary, our theory fails and an improved method will solve the problem.

修订：

> Uniform coverage of our median intervals over $\mathcal P$ remains unresolved. Allowing population medians to approach the support boundary requires further control of the quantile approximation error.

修订限定了开放问题，指出给定材料支持的困难；未把“尚无证明”写成“方法已被证明失效”，也没有预告未经建立的解决办法。均值推断的其他结果不因此被否认。

何时应保持不改：Discussion 已准确限定目标、分布类和保证，并指出实际障碍时，保持简洁即可。作者已确认保留或删除的段落按最新要求处理，不因历史草案出现过一段模拟总结就将它恢复。
