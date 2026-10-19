# BIOM03 · Extended Bayesian information criteria for model selection with large model spaces

题录：Jie Chen; Zehua Chen（2008），*Biometrika* 95(3)，759-771。[DOI](https://doi.org/10.1093/biomet/asn034)。

文章类型：regular methodological and theoretical article (author manuscript; historical issue category not separately verified)。方向：model-selection, high-dimensional-regression。

全文：[公开来源](https://www.stat.ubc.ca/~jhchen/paper/Bio08.pdf)。版本：author manuscript at Jiahua Chen's UBC site; 27 PDF pages including end tables; DOI matches 2008 Biometrika publication。

阅读范围：All main narrative pp.1–17, assumptions and theorem, computational procedure, three simulation cases, appendix proof narrative pp.18–20 and end tables pp.24–27; references inspected; displayed derivations consulted, not independently verified. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有2013次引用，已有至少八年观察期；实际阅读全文后，作为model-selection, high-dimensional-regression方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，2013次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要先指出大模型空间下BIC偏宽，再引出同时惩罚参数数目和空间复杂度的新准则，接一致性与模拟中的真选择/假发现权衡。不是简单宣布一种更强惩罚优越。

## 引言的推进

§1 pp.2–3由基因组研究的候选维度与样本量失衡进入，解释‘太宽’具体表现为伪变量，然后定位Lasso一致性与已有BIC修正。贡献句随后解释为什么保留BIC的简单形式，同时改变其模型空间先验。

## 方法、定义与理论的依赖

§2 pp.3–7先重建BIC的贝叶斯来源，再用1000个候选变量的一元/二元子模型数量说明均匀模型先验的后果，顺势导出新项。§3 pp.7–11先定义渐近可识别条件，比较sparse Riesz条件及共线例子，再给一致性定理、参数取值解释和失效机制。

## 数值、应用与证据

§4 pp.11–16把计算可行性放在模拟前：惩罚路径和分组tournament用于产生候选子集；随后小维、大维及真实遗传协变量三个情形逐层加难。记录正选择与假发现两指标及重复变异；真实协变量设计不是直接宣称真实基因发现。

## 结尾与主文分工

p.17先讨论如何选gamma，再区分已证明的正态线性情形与更广泛可用性，最后指出对原BIC适用范围的新认识。后接附录与独立表页。

## 可迁移写作动作

修改准则型文章时，用一个可数的模型空间例子揭示额外惩罚的来源；定义、可识别性、理论保证、实际候选搜索、性能权衡依次安排。比较时写出具体误选和真选的代价。

## 不能泛化的特殊安排

作者稿中‘最弱’等评价和推广猜测不能无证据照搬。本文一致性不等于任意设计或任意搜索算法都能找到真模型；统计准则与候选搜索分工必须保留。
