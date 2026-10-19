# BIOM06 · Model selection and estimation in the Gaussian graphical model

题录：Ming Yuan; Yi Lin（2007），*Biometrika* 94(1)，19-35。[DOI](https://doi.org/10.1093/biomet/asm018)。

文章类型：methodological article; early author preprint, final issue category not verified。方向：gaussian-graphical-models, penalized-likelihood。

全文：[公开来源](https://www2.isye.gatech.edu/~brani/isyestat/05-08.pdf)。版本：author preprint dated 2005-06-01, public Georgia Tech archive; DOI matches 2007 journal paper; corrupt font map recovered with English OCR。

阅读范围：All 17 PDF pages via complete OCR: abstract, introduction, methodology, optimization and lemmas, tuning, quadratic comparison, eight simulation structures, four data examples, conclusion and references; OCR mathematical symbols not treated as reliable proof transcription. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有1631次引用，已有至少八年观察期；实际阅读全文后，作为gaussian-graphical-models, penalized-likelihood方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，1631次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要围绕稀疏、收缩和正定三个同时需求写方法，再解释约束带来的计算难点、maxdet实现、调参及比较证据。

## 引言的推进

§1 pp.2–4先把精度矩阵零元、条件独立和图边对应起来，随后指出逐步选择的多重比较与计算成本；再定位同时估计与选择、正定约束的贡献。后部把算法和邻域选择比较提前预告；这是早期稿组织，不推广其长预告。

## 方法、定义与理论的依赖

§2 pp.4–5从高斯似然及普通逆样本协方差的不足导出约束优化。§3 pp.5–9按maxdet联系、算法、有限终止引理、已有可靠初值时的garrote扩展、调参安排。§4 pp.9–10用二阶近似精确解释与邻域回归的联系，区别损失与对称/正定约束。

## 数值、应用与证据

§5 pp.10–13覆盖八种结构，并同时评估KL损失与假阳性/假阴性；承认BIC可能带来较多假阳性，转而显示解路径的信息。§6 pp.13–16的小型经典数据用交叉验证，大型股票例用年度划分预测，比较基准随数据场景明确。

## 结尾与主文分工

§7 p.16只有短总结，强调选择与估计结合及凸优化实现；没有额外罗列未来全部可能性。

## 可迁移写作动作

方法目标有多个约束时，先用对象解释各约束的统计意义，再给统一优化问题；与近邻方法的差别可通过共同形式推导，而非只列优缺点。模拟里的不利指标应保留。

## 不能泛化的特殊安排

2005早期稿不能代表2007终版全部结构，也不能以其‘预期更有效’措辞替代新稿证据。OCR只用于恢复叙述，数学核查必须回到PDF图像；图模型不自动带因果解释。
