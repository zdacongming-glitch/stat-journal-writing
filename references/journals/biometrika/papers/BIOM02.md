# BIOM02 · Adaptive linear step-up procedures that control the false discovery rate

题录：Yoav Benjamini; Abba M. Krieger; Daniel Yekutieli（2006），*Biometrika* 93(3)，491-507。[DOI](https://doi.org/10.1093/biomet/93.3.491)。

文章类型：regular methodological and theoretical article; author manuscript。方向：multiple-testing, false-discovery-rate。

全文：[公开来源](https://www.math.tau.ac.il/~ybenja/MyPapers/bkymarch9.pdf)。版本：25-page author manuscript on Yoav Benjamini’s university site, including separate end tables and figures; bibliography incorporates 2006 work。

阅读范围：Complete narrative of all 25 author-PDF pages: summary, sections 1–8, definitions of compared procedures, FDR bound derivation and theorem statements/proof narrative, simulations, two biological examples, discussion and end tables/figure captions; algebra not independently checked. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有3219次引用，已有至少八年观察期；实际阅读全文后，作为multiple-testing, false-discovery-rate方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，3219次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要先给原线性step-up方法的精确保守因子，才引出估计真零个数的两阶段修改。独立性下的证明与正相关下的模拟分开表达；没有把一个依赖结构中的表现说成一般控制保证。

## 引言的推进

§1 p.3用FWE与逐项检验的两个实践代价引出FDR，随后直接写出原方法保守因子及可改进位置。§2 pp.3–7先形式化FDR、旧算法与调整p值，再围绕同一未知真零个数比较现有估计路线，文献排列服务于后文统一分析。

## 方法、定义与理论的依赖

§3 pp.8–9给两阶段算法、直觉及多阶段变体；§4 pp.9–10对一般单调估计量推导公共FDR上界，再于§5 pp.11–13证明两阶段和分位数方法，解释既有方法所需的有限样本修正。直觉、算法和有效性各有明确位置。

## 数值、应用与证据

§6 pp.13–17先列十个程序并区分新法、旧法、不可实现oracle，再报告重复次数、蒙特卡洛误差及相对oracle的方差缩减。独立与正依赖分别比较FDR及功效；指出不满足控制的方案不能只凭功效取胜。§7 pp.17–18以临床多终点及QTL说明新增发现，同时承认依赖时采用更保守选择。

## 结尾与主文分工

§8 p.19收回主要收益来自自适应本身、其间细微差异次之；明确真零比例接近一时优势不实现。最后把相关环境下的理论理解保留为真实未决问题。

## 可迁移写作动作

先把旧法的保守性写成可操作因子，再统一多个算法的理论分析；数值研究把有效性与功效分开，比较之前说明oracle只作参照。实施中看似自然的截断可能破坏保证，必须保留。

## 不能泛化的特殊安排

长篇作者稿的摘要和背景重复不应照搬为成熟稿的长度规范。独立性证明不能扩写成任意正依赖保证；估计真零个数时是否允许超过总检验数是方法细节，不能随意为直觉整齐而截断。
