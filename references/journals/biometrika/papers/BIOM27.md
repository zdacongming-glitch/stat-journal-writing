# BIOM27 · Joint estimation of multiple graphical models

题录：Jian Guo; Elizaveta Levina; George Michailidis; Ji Zhu（2011），*Biometrika* 98(1)，1-15。[DOI](https://doi.org/10.1093/biomet/asq060)。

文章类型：regular methodological and theoretical article; complete PMC author manuscript。方向：gaussian-graphical-models, joint-estimation, heterogeneous-data。

全文：[公开来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC3412604/)。版本：complete PMC author manuscript, issue date March 2011; main article and proof appendix。

阅读范围：Complete HTML summary, sections 1–5, local-minimizer equivalence lemmas, iterative algorithm, model selection, consistency and sparsistency theorem interpretations, all three simulation networks, webpage application and appendix proof narrative; external omitted lemma proofs not read. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有433次引用，已有至少八年观察期；实际阅读全文后，作为gaussian-graphical-models, joint-estimation, heterogeneous-data方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，433次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要先定义多类别共享变量及部分依赖结构，再以混合成单图和完全分开估计的代价引出联合估计，随后说明层次惩罚、理论与应用；这里两种比较对应实际可选方案。

## 引言的推进

§1依次澄清图、协方差/精度零元，回顾单图估计的最近邻，再把异质数据的共享与特异边作为缺口；癌症亚型和网页类别不是任意两个例子，而分别显示共享结构的科学及实际含义。

## 方法、定义与理论的依赖

§2.1先给分开估计这个共同基准；§2.2分解公共因子和类别因子，以两条局部极小值等价引理将双调参降为单调参并改写为可计算形式；§2.3用局部线性近似转成加权graphical lasso，给初始化与数值截断。§3先解释特征值与信号强度条件，再给两类理论保证，逐一讨论调参上下界能否兼容及最佳/最差稀疏情形。

## 数值、应用与证据

§4不只更换网络形状，还系统增加个别边/共有边比例，以检验共享信息的收益何时消失；明确异质性高时分开方法略胜。ROC、估计损失、误识别共有零元及BIC/CV选参分别呈现。§5交代文本预处理、词选择及边含义，再用常用短语和类别特异搭配解释共同/不同图。

## 结尾与主文分工

主文以网页中可解释的类别差别结束，无独立Discussion；附录承接局部邻域的存在性和导数符号证明。结束没有把图解释扩张成因果主张。

## 可迁移写作动作

多任务方法应围绕共享程度设计压力测试，显式报告借力何时不再有益；统计重参数化的每一步都交代如何减少调参或调用成熟求解器。理论条件的兼容性比笼统说条件温和更有信息。

## 不能泛化的特殊安排

定理表述为存在具有性质的局部极小值，不能等同于任意初值算法都找到它。共有零元与共有非零边不能混称；单一高斯设定上的语义解释不证明因果。
