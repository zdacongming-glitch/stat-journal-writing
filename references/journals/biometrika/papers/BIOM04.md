# BIOM04 · The role of the propensity score in estimating dose-response functions

题录：Guido W. Imbens（2000），*Biometrika* 87(3)，706-710。[DOI](https://doi.org/10.1093/biomet/87.3.706)。

文章类型：Miscellanea (verified in published PDF running header)。方向：causal-inference, multivalued-treatment, propensity-score。

全文：[公开来源](https://www.math.mcgill.ca/dstephens/SISCR2017/Articles/Biometrika-2000-Imbens-706-10.pdf)。版本：published Biometrika PDF pp.706–710, hosted in McGill course readings; separate longer 1999 NBER version retained only in research cache。

阅读范围：Complete published five-page article: summary, all five sections, two definitions, theorem, conditioning arguments, implementation paragraphs, closing insight and references. Earlier NBER narrative also read for comparison; proof correctness not independently audited. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有1777次引用，已有至少八年观察期；实际阅读全文后，作为causal-inference, multivalued-treatment, propensity-score方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，1777次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要从多协变量调整困难进入，直接定位二元倾向得分及多处理推广，不在摘要枚举全套性质。

## 引言的推进

§1 p.706仅一段：调整困难、二元得分已有作用、多处理缺口、本文关键认识。末句把‘每个潜在结果均值可估’与‘组内直接因果比较可做’区分，这个区别驱动后文，不是装饰性转折。

## 方法、定义与理论的依赖

§2 pp.706–707先定义目标均值、观测量及弱无混杂，再解释其与既有更强条件和MAR的关系。§3 pp.707–708压缩复习二元调整与加权。§4 p.708定义广义得分，给单个主定理，紧接三步实施及离散/有序处理的区别。

## 数值、应用与证据

无模拟和数据分析。证据是期望恒等式、条件独立与目标平均的构造；p.708强调响应回归最终必须在指定处理水平的得分上平均，避免把观测到的处理得分误代进去。

## 结尾与主文分工

§5 pp.709–710详细比较二元与多处理的条件集合，以一个最终段落解释经过不同得分分布平均后如何恢复因果解释；无独立重复性Discussion。

## 可迁移写作动作

短篇概念推广可以用一条贯穿全文的区别组织；最近邻旧方法只复习新结果真正依赖的性质，主定理后立即给实施含义。不要因为压缩而把条件集合的不同删掉。

## 不能泛化的特殊安排

正式五页版本与22页NBER稿结构明显不同，因此只用正式版作该刊篇章依据。没有数值研究反映其概念短文类型，不能推出一般方法稿也无需模拟。原文采用的标记和历史拼写不自动替代现行作者指南。
