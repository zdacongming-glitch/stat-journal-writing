# 十二篇经典论文的叙述阅读卡

本组论文每刊三篇，覆盖目标重定义、方法构造、理论短文、计算框架、综述、因果识别及稳健估计。选择用于展示不同的论证任务，不是引用量排名，也不是对四刊文风的随机抽样。不能由这些案例推断每位编辑的偏好。

核查及阅读日期：2026-09-30。以下笔记依据论文正文，集中阅读摘要、引言、关键方法过渡、结果解读和结尾；定位处标明最有用的章节。没有逐行验证全部证明，也不把本文件作为定理适用条件的完整清单。部分旧扫描件借助 OCR 阅读叙述，数学公式和书目信息不以 OCR 为唯一依据。

只保存简短分析与原始来源链接，不将论文全文或 PDF 打包进技能。引用的 DOI 对应正式发表版本；作者或高校托管 PDF 用于阅读，遇分页差异以正文节号定位。

## 按写作困难选择范例

| 要解决的写作困难 | 优先阅读 | 学习的动作 |
| --- | --- | --- |
| 方法看起来像任意拼装 | P01、P05 | 先明确设计标准或权衡，再解释构造 |
| 问题很难，技术却显得绕路 | P02、P07 | 解释目标转换为何降低困难 |
| 宣称统一框架却没有说服力 | P04、P03 | 让不同问题确实通过同一结构得到回答 |
| 新贡献是改变评价目标 | P06、P08 | 先论证值得优化或控制什么 |
| 定理出现突然 | P09、P10 | 在正式结果前建立问题与自然语言解释 |
| 稳健性或改进被写得过宽 | P11、P12 | 明确不变的是哪个目标，改进的是哪个指标 |
| 讨论只会重复摘要 | P05、P11 | 说明方法选择随条件如何变化 |

## JASA

### P01 · Fan & Li（2001）：先提出设计标准

Fan, J. and Li, R. *Variable Selection via Nonconcave Penalized Likelihood and its Oracle Properties*. JASA, 96(456), 1348–1360. [DOI](https://doi.org/10.1198/016214501753382273)；[作者 PDF](https://fan.princeton.edu/papers/01/penlike.pdf)；[高校副本](https://pages.stat.wisc.edu/~shao/stat992/fan-li2001.pdf)。

**定位**：§1–2、§3.2、§4–5。

**推进方式**：从变量选择的估计与计算问题，转向大信号少偏差、稀疏性、连续性三个标准；先用正交情形和阈值图解释惩罚的作用，再进入一般似然、理论与数值证据。新构造因满足标准而显得有理由。

**可迁移的编辑动作**：把“我们提出某惩罚”前移为“需要同时满足哪些性质”；图服务于机制解释。不要照搬结尾较强的比较措辞；oracle 性质有正则条件和调参要求，也不自动保证算法找到相应局部极值点。

### P02 · Li（1991）：通过目标转换解释方法

Li, K.-C. *Sliced Inverse Regression for Dimension Reduction*. JASA, 86(414), 316–327. [DOI](https://doi.org/10.1080/01621459.1991.10475035)；[研究机构托管 PDF](https://mistis.inrialpes.fr/docs/sir_li1991.pdf)。

**定位**：§1 的问题设置，§3–4 的逆回归与算法，§7 的解释。

**推进方式**：从高维非参数回归的困难，缩小到有效降维方向，再解释逆回归为何保留所需信息。算法后逐步说明切片、加权和变换的用途；结尾把输出重新解释为有意义的描述统计量。

**可迁移的编辑动作**：先告诉读者“不必估计整个复杂对象”，再说明替代对象保留了什么。简单估计器的合理性可以来自目标只需要部分信息。不要省去线性条件，也不要把子空间包含关系直接写成总能恢复全部方向。

### P03 · Kass & Raftery（1995）：问题先出现，工具随后回答

Kass, R. E. and Raftery, A. E. *Bayes Factors*. JASA, 90(430), 773–795. [DOI](https://doi.org/10.1080/01621459.1995.10476572)；[作者 PDF](https://www.stat.cmu.edu/~kass/papers/bayesfactors.pdf)。

**定位**：§1–2、§3–5 的组织、§7、§10；这是综述型文章。

**推进方式**：先提出多种应用中的比较问题，再给定义、解释、计算和先验选择，随后回到先前的问题。读者知道技术段落最终要回答什么；先验敏感性和争议并未被方便性叙述抹去。

**可迁移的编辑动作**：让贯穿案例在后文得到实质回应，用共同决策问题组织综述。不要把综述的宽幅铺陈、旧版条列摘要或篇幅作为原创方法稿的现行模板。

## JRSS-B

### P04 · Dempster, Laird & Rubin（1977）：统一来自共同结构

Dempster, A. P., Laird, N. M. and Rubin, D. B. *Maximum Likelihood from Incomplete Data via the EM Algorithm*. JRSS-B, 39(1), 1–22. [DOI](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x)；[MIT 托管 PDF](https://web.mit.edu/6.435/www/Dempster77.pdf)。扫描版另含后续讨论，整份文件页数不是主文篇幅。

**定位**：§1 的数值例子，§2 的一般化，§3 的性质解释，§4 的不同应用。

**推进方式**：先区分观测数据与完整数据，用小例子让迭代可见，再抽象出统一计算形式；不同应用逐一映射回相同结构。已有工作的归属帮助界定“统一”的贡献。

**可迁移的编辑动作**：统一框架需要具体映射，不能只列一串应用名称。小例子既用于引入也可用于解释后面的收敛行为。单调性不等于任意初值到全局最大值；原文收敛论述也不能替代对当前算法的证明核查。

### P05 · Tibshirani（1996）：用权衡贯穿提出与讨论

Tibshirani, R. *Regression Shrinkage and Selection via the Lasso*. JRSS-B, 58(1), 267–288. [DOI](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x)；[教授网站托管的期刊 PDF](https://hedibert.org/wp-content/uploads/2018/05/tibshirani-1996.pdf)。这里使用发表版，不与较早技术报告混用。

**定位**：§1–2，§3–7 的顺序，§11 的讨论。

**推进方式**：以预测准确性和可解释性定位问题，通过子集选择与 ridge 的权衡引出方法；正交情形和几何解释回答为什么会出现零系数，再讨论应用、调参与计算。

**可迁移的编辑动作**：结尾回到开头的权衡，解释不同信号结构下哪些方法占优。保留有用的失败或劣势情形。不要把特定模拟中的比较写成无条件理论排序，也不要将后来发展的性质追认给这篇原始论文。

### P06 · Benjamini & Hochberg（1995）：先证明问题值得重定义

Benjamini, Y. and Hochberg, Y. *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*. JRSS-B, 57(1), 289–300. [DOI](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)；[作者 PDF](https://www.math.tau.ac.il/~ybenja/MyPapers/benjamini_hochberg1995.pdf)。

**定位**：§1–2、§3 的程序及保证、§5。

**推进方式**：先说明某些多重检验任务为何不必追求一例错误都不发生，再定义替代指标并讨论它适合的应用，随后给出程序、理论和功效比较。算法之前，评价目标已获得统计理由。

**可迁移的编辑动作**：如果贡献改变了损失或错误指标，先解释新指标为何符合决策任务。保留原始理论中的独立性条件；期望错误比例的控制不是每一次实际错误比例都被界住。

## AoS

### P07 · Efron（1979）：让新概念先变得可操作

Efron, B. *Bootstrap Methods: Another Look at the Jackknife*. The Annals of Statistics, 7(1), 1–26. [DOI](https://doi.org/10.1214/aos/1176344552)；[高校托管 PDF](https://blogs.helsinki.fi/bk-club/files/2012/05/Efron_Bootstrap_AS1979.pdf)。

**定位**：§1–2 的问题与步骤，§5 的方法联系，§8 的 remarks。

**推进方式**：从估计统计量的抽样分布出发，较早给出重抽样步骤，再用例子解释用途，并把 jackknife 放入新的理解框架。结尾同时讨论计算和推断上的细节。

**可迁移的编辑动作**：抽象思想可以先通过操作被理解，再讨论与熟悉方法的关系。不要把近似分布的构造自动说成任何置信区间都有效；不同推断步骤仍需各自依据。这也不是“所有 AoS 文章必须以长定理开场”的范例。

### P08 · Schwarz（1978）：短文也有完整论证链

Schwarz, G. *Estimating the Dimension of a Model*. The Annals of Statistics, 6(2), 461–464. [DOI](https://doi.org/10.1214/aos/1176344136)；[高校托管 PDF](https://sites.stat.washington.edu/courses/stat527/s13/readings/ann_stat1978.pdf)。

**定位**：全文四页，特别是开头的准则和随后模型、渐近展开的连接。

**推进方式**：点出直接最大化似然偏向复杂模型的问题，与已有选择思路比较，在前部给出准则，再用明确模型和渐近展开解释其来源。技术细节服务于一个集中问题。

**可迁移的编辑动作**：当贡献足够集中，可以先给读者主结论，再完成推导。精简重复与旁支，不精简假设；不要据此宣称同一展开无条件适用于奇异模型或增长维度，也不必为模仿常见结构硬添模拟章节。

### P09 · Barber & Candès（2015）：直觉与精确保证相互对照

Barber, R. F. and Candès, E. J. *Controlling the false discovery rate via knockoffs*. The Annals of Statistics, 43(5), 2055–2085. [DOI](https://doi.org/10.1214/15-AOS1337)；[arXiv 上的 IMS 电子重印版](https://arxiv.org/pdf/1404.5609)。阅读版本为 2015 年 v3；重印件页码与期刊不同。

**定位**：§1.1–1.2、Theorems 1–2，§6。

**推进方式**：先定义错误率问题，再用三步程序和竞争直觉说明构造，早早给出核心保证，随后一般化。讨论明确区分已建立的错误率结果与数值考察的功效。

**可迁移的编辑动作**：用读者能追踪的对象讲机制，同时保留不同版本的差别：原始 knockoff 控制修正指标，knockoff+ 给 FDR 保证。固定设计、高斯误差等原文条件不能省略，也不能与后来的 model-X 理论混用。

## Biometrika

### P10 · Rosenbaum & Rubin（1983）：自然语言给出理论路线

Rosenbaum, P. R. and Rubin, D. B. *The central role of the propensity score in observational studies for causal effects*. Biometrika, 70(1), 41–55. [DOI](https://doi.org/10.1093/biomet/70.1.41)；[高校托管 PDF](https://www.stat.cmu.edu/~ryantibs/journalclub/rosenbaum_1983.pdf)。

**定位**：§1 的定义，§2.1 的结果概述，§2 的定理与解释。

**推进方式**：先建立因果问题、平衡分数及相关条件，再用自然语言预告关键结果，正式定理随后说明它们的依据。概念被分开，读者才能判断一维分数究竟解决了什么。

**可迁移的编辑动作**：定理前用简短解释建立阅读目标，之后说明实际后果。观测协变量平衡与因果识别是不同层次；不得把倾向评分写成自动消除未观测混杂，也不能抹去重叠等条件。

### P11 · Liang & Zeger（1986）：先给基线，再解释改进

Liang, K.-Y. and Zeger, S. L. *Longitudinal data analysis using generalized linear models*. Biometrika, 73(1), 13–22. [DOI](https://doi.org/10.1093/biomet/73.1.13)；[高校托管 PDF](https://www.maths.usyd.edu.au/u/jchan/GLM/Liang%26Zeger1986GEE.pdf)。

**定位**：§1–3 的推进，§6 的讨论。

**推进方式**：明确总体均值关系的目标，先给工作独立估计及其优缺点，再引入一般工作相关结构，最后讨论效率和使用边界。读者先有基线，才知道推广带来什么。

**可迁移的编辑动作**：把目标模型与辅助结构分开；比较不能只说“更一般”。讨论回到研究目的：若相关过程本身是科学目标，文章的侧重点可能不合适。稳健方差不意味着均值误设、任意缺失或任意依赖下仍有效。

### P12 · Firth（1993）：把改进放在估计机制内部

Firth, D. *Bias reduction of maximum likelihood estimates*. Biometrika, 80(1), 27–38. [DOI](https://doi.org/10.1093/biomet/80.1.27)；[高校托管 PDF](https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GibbsFieldEst/BiasReductionMLE.pdf)。

**定位**：§1、§2 的几何解释、§3、§5。

**推进方式**：先规定要减少的偏差项，并解释事后校正的困难，再改造产生估计量的方程；几何解释帮助读者理解形式推导，随后考察不同模型。

**可迁移的编辑动作**：说清改善发生在哪个环节、针对哪个指标。偏差减少不能改写成均方误差必然下降；参数化会影响表述，特定指数族中的惩罚解释不能无条件推广为一般结论。

## 如何使用这些观察

这些范例支持一种可迁移的编辑判断：让思想出现的顺序接近读者理解它所需的顺序。它们并不支持固定的句长、段数、语态或完整章节清单。

出现冲突时，当前官方规范决定格式，原稿证据决定结论力度，用户要求决定修改范围。可以学习老论文先定义问题、解释机制、承认边界的做法；不沿用其历史排版、今日已变化的规则或缺少当前证据支撑的强烈评价。
