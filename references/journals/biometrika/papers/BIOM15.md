# BIOM15 · A sequential particle filter method for static models

题录：Nicolas Chopin（2002），*Biometrika* 89(3)，539-552。[DOI](https://doi.org/10.1093/biomet/89.3.539)。

文章类型：regular computational methodology article (published PDF)。方向：sequential-monte-carlo, bayesian-computation。

全文：[公开来源](https://luiarthur.github.io/padawan/assets/ams268/notes/chopin_2002_smc.pdf)。版本：published Biometrika PDF pp.539–551, public university-course repository。

阅读范围：All 13 published PDF pages: complete narrative, particle definition and efficiency, degeneracy discussion, asymptotic theorem statement, full algorithm and seven implementation subsections, both numerical examples, appendix regularity conditions and references; external technical-report proof not read. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有569次引用，已有至少八年观察期；实际阅读全文后，作为sequential-monte-carlo, bayesian-computation方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，569次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要把原属动态问题的粒子方法迁移到静态后验，解释部分后验探索为何节省计算，再给算法范围和两类例子。价值与数据处理顺序直接相连。

## 引言的推进

§1 pp.539–540先解释重复MCMC处理一串后验的浪费，再提出在单一最终后验下人为建立部分后验序列；记号在这一思想之后出现，读者先知道为何需要新的序列。

## 方法、定义与理论的依赖

§2 pp.540–542依次给粒子系统、重要性权重、效率与退化，再说明重抽样为何不能消除退化、move怎样补救。§3 pp.542–543给批量重要性更新及相对精度定理，随即解释批量比例与所需粒子数；§4算法后按核、批量、粒子数、并行、复用计算、潜变量逐项解决实施决策。

## 数值、应用与证据

§5 pp.547–550用probit说明规则后验下move效率随数据增加的变化，并报告重复运行变异和成本；混合模型例进一步检验多峰、高维参数情形。每个例子对应前文计算障碍，不是增加应用数量。

## 结尾与主文分工

无独立Discussion，第二个数值例之后接致谢与定理正则条件附录。全文把限制放在相关计算选择处：例如边际似然不可算时不能直接套用。

## 可迁移写作动作

算法论文先解释为何构造计算路径，再给必要背景与核心效率结果；完整算法之后按真实实施选择分小节。用‘退化仍存在’这种限定阻止读者误用，有实际信息就不能删作冗言。

## 不能泛化的特殊安排

历史粒子数经验和硬件时间不可作为今日阈值规范。正则条件在附录、证明在另一个技术报告，不等于新稿可省掉自己主要理论依据；本次不声称验证该外部证明。 出版社与Crossref题录列539–552，而所读正式PDF页眉及作者书目列539–551；该公开PDF末页551为参考文献结尾，未见叙述缺页。题录保留出版社页段并说明差异。
