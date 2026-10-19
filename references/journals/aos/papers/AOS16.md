# AOS16 · On asymptotically optimal confidence regions and tests for high-dimensional models

题录：Sara van de Geer; Peter Bühlmann; Ya’acov Ritov; Ruben Dezeure（2014），*The Annals of Statistics* 42(3)，1166-1202。[DOI](https://doi.org/10.1214/14-aos1221)。

文章类型：Original high-dimensional inference theory and methodology research; IMS electronic reprint。

全文：[公开来源](https://arxiv.org/pdf/1303.0518)。版本：IMS electronic reprint arXiv:1303.0518v3, 2014-06-23; 37 PDF pages; formal 2014 AoS 42(3), pp.1166–1202, pagination differs。

阅读范围：已读PDF pp.1–26摘要和§§1–4全部主体叙述、条件与定理含义、GLM扩展、全部数值讨论和真实数据；§5 pp.26–29读证明依赖结构，其余技术证明及外部补充未逐行阅读验算。未重现实验。 阅读日：2026-10-19。所有PDF页码均指实际读取版本的自身页序，非正式印刷页序。

入选线索：Crossref当日记录757次引用，结合观察年限、实际全文贡献及方向覆盖保留；不称唯一test-of-time排名。

## 摘要的信息选择

摘要明确低维目标在高维参数中的推断，承认线性模型构造与Zhang–Zhang实质相同，再写自己的效率分析、广义模型和设计范围；贡献不靠重复命名既有估计器。

## 引言的推进

§1 pp.1–3先把点估计进展与区间/检验障碍分开，指出稀疏估计极限分布和非一致性问题，再按保证性质比较拆分、稳定选择、bootstrap等路线。最近邻比较具体到已知协方差、估计逆矩阵、设计尾部与效率目标，承认同期独立工作；§1.2很长的路线图属于此历史理论稿，不当固定模板。

## 方法、定义与理论的依赖

§2.1 pp.4–6从lasso KKT近似反演导出非稀疏估计，nodewise回归用于控制所需余项，而不是泛称估精度矩阵；§2.2–2.3 pp.7–14按固定设计分解、随机设计余项、uniform/honest推断、条件讨论、半参数效率、非高斯推广递进。§3 pp.14–20先把步骤推广到凸损失，再给高层条件、验证nodewise随机加权矩阵及具体GLM结果，抽象结论与可检验条件分开。

## 数值、应用与证据

§4 pp.20–26详细交代原回归与nodewise回归的不同调参，分清单参数区间和多重检验。模拟按真实非零/零系数分别报告覆盖和长度，揭示bootstrap的零点超效率；明确较密及等相关设计下误差控制差，logistic小样本并不可靠。核黄素数据没有显著单基因，文末解释组推断可能更有力，不制造发现。

## 结尾与附录分工

没有独立Discussion或Conclusion；每一理论范围的解释嵌在对应小节，数值各类结果有局部Discussion，主体以真实数据的低功效及组目标解释结束，再接证明。

## 可迁移写作动作

高维推断稿须区分估计准确与可用推断、点态与一致保证、目标系数与选后模型目标。先给估计的主项/余项分解，再按各环节验证条件。强理论论文也应报告自己方法覆盖失败和真实数据零发现。

## 特殊条件与不能泛化之处

本篇目标为真高维模型低维系数，与AOS22所选模型投影系数不同。渐近效率依稀疏、设计和正则条件，不能当小样本可靠性承诺；同一主张须同时看不利模拟。GLM高层条件不是对所有凸损失无条件成立。
