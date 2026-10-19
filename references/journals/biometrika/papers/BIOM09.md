# BIOM09 · Dealing with limited overlap in estimation of average treatment effects

题录：Richard K. Crump; V. Joseph Hotz; Guido W. Imbens; Oscar A. Mitnik（2009），*Biometrika* 96(1)，187-199。[DOI](https://doi.org/10.1093/biomet/asn055)。

文章类型：regular methodological and theoretical article; forthcoming author manuscript。方向：causal-inference, overlap, estimand-selection。

全文：[公开来源](https://public.econ.duke.edu/~vjh3/working_papers/overlap.pdf)。版本：23-page author manuscript marked forthcoming in Biometrika, public Duke faculty working-paper archive; formal publication 2009。

阅读范围：All 23 PDF pages: summary, complete introduction and sections 2–4, binary-covariate motivating example, assumptions, theorem/corollary, beta-distribution numerical study, clinical reanalysis, proof sketch, references and end tables/figure caption; external working-paper extensions not read. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有1002次引用，已有至少八年观察期；实际阅读全文后，作为causal-inference, overlap, estimand-selection方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，1002次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要把缺乏重叠导致的方差与敏感性、惯常任意修剪、最精确子总体的优化准则、条件下的倾向得分区间及经验近似依次连接；0.1规则被写成近似，不是普适定理。

## 引言的推进

§1 pp.2–3先定位已有估计方法及实际修剪的任意性，再明确本文改变的是目标子总体，方法不依赖某个特定估计器。倾向得分的作用由准则推出，随后立即交代外部有效性的代价，而不是在结尾才补免责。

## 方法、定义与理论的依赖

§2 pp.3–8先分清样本与总体平均效应，以二元协变量例子展示条件方差选择；两条Remark解释为何不优化无条件方差，以及随机选择集合下究竟覆盖哪个目标。§3.1–3.2 pp.9–11接半参数效率界、一般异方差最优集合、同方差倾向得分推论和两步实施。

## 数值、应用与证据

§3.3 p.12用Beta倾向得分家族量化最优阈值与0.01/0.10近似的差异，检验的是准则的含义。§4 pp.13–14重析导管治疗数据，完整交代样本、72协变量、得分模型、重新拟合、条件bootstrap及两种标准误；报告舍去18%样本与方差下降36%的取舍。

## 结尾与主文分工

主文以实际估计和方差结果收束，无独立Discussion；附录pp.15–18先推广加权目标再给交换集合的证明思路。引言已交代精度与外部有效性的代价，后文不反复重复。

## 可迁移写作动作

目标选择型文章先把目标变化说清，再用小型可精算例解释优化对象；一般定理之后立即突出更易实施推论。数值和应用须同时报告所得精度与丢失样本，不能只说更精确。

## 不能泛化的特殊安排

不同子总体的效应并不是原总体同一目标的更好估计。忽略第一步不确定性的论述针对条件于所选集合的目标，不能省去该目标定义。0.1至0.9规则的依据是所考察分布族与实例。
