# BIOM22 · An efficient Markov chain Monte Carlo method for distributions with intractable normalising constants

题录：Jesper Møller; Anthony N. Pettitt; Robert W. Reeves; Kasper K. Berthelsen（2006），*Biometrika* 93(2)，451-458。[DOI](https://doi.org/10.1093/biomet/93.2.451)。

文章类型：regular computational methodology article; repository author manuscript。方向：bayesian-computation, intractable-normalising-constants, auxiliary-variables。

全文：[公开来源](https://eprints.qut.edu.au/7869/1/7869.pdf)。版本：20-page QUT repository author manuscript including cover and separate end figures/tables; linked to published 2006 pp.451–458。

阅读范围：All 20 PDF pages: cover, summary, full sections 1–4 narrative, Metropolis–Hastings cancellation derivation, auxiliary-density choice, Ising implementation, analytical and empirical checks, discussion, references and all table/figure captions. Algebra not independently verified. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有352次引用，已有至少八年观察期；实际阅读全文后，作为bayesian-computation, intractable-normalising-constants, auxiliary-variables方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，352次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要把不可算且依参数变化的归一化常数写成具体障碍，立即给辅助变量、接受比中相消及可精确抽样的条件，最后用Ising模型定位证据。

## 引言的推进

§1 PDF p.3列出同一障碍出现的应用，随即区分已有近似路线与本文扩充状态后精确相消的构造；只有两个主要段落，不建立一般计算推断宏大背景。

## 方法、定义与理论的依赖

§2 pp.3–6先写原后验和无法计算的接受比，再加入辅助条件密度、给联合提议与消去常数的比率。随后用单样本重要性/bridge sampling类比解释辅助密度应接近什么，以及固定参数近似何时可能有效。统计正确性与混合效率依次处理。

## 数值、应用与证据

§3.1 pp.6–7给Ising模型、伪似然初值、提议、完美模拟和先验支持。§3.2 pp.8–10先在可解析小格点上比较，再扩大格点并报告黏滞、拒绝长串、滞后100相关及临界慢化；不把轨迹看似合理说成严格收敛证明。表1–2与图1–2位于末尾独立页。

## 结尾与主文分工

§4 p.10把精确抽样条件收回方法可用范围，指出与ABC/层次模型的联系；困难混合机制已在相关数值段解释，没有结尾重复多遍。

## 可迁移写作动作

计算构造先暴露无法实现的旧接受比，再给最少扩充使之可算；在推导旁解释辅助分布的设计目标。验证分为可解析校准和大规模诊断，并保留变慢的具体表现。

## 不能泛化的特殊安排

这是Møller等辅助变量方法，不可改名成后来的exchange algorithm。消去常数的正确性要求提议中的似然样本满足规定条件，普通未混合MCMC替代不保留精确性；精确平稳分布也不保证快速有限次收敛。
