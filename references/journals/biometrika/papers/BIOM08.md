# BIOM08 · The horseshoe estimator for sparse signals

题录：Carlos M. Carvalho; Nicholas G. Polson; James G. Scott（2010），*Biometrika* 97(2)，465-480。[DOI](https://doi.org/10.1093/biomet/asq017)。

文章类型：early working paper corresponding to regular 2010 journal article; final narrative not obtained。方向：bayesian-shrinkage, sparse-normal-means, horseshoe-prior。

全文：[公开来源](https://faculty.chicagobooth.edu/-/media/faculty/nicholas-polson/research/horse.pdf)。版本：30-page early 2008-era working paper from Nicholas Polson’s official university research archive; final 2010 abstract and DOI checked separately; early version differs materially from final article。

阅读范围：All 30 author-PDF pages: complete introductory argument and model, density-bounds theorem, shrinkage taxonomy and motivating example, estimation and classification simulations, hyperparameter discussion, conclusion, references and proof appendix. Final published 16-page narrative not available and not claimed read. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有1391次引用，已有至少八年观察期；实际阅读全文后，作为bayesian-shrinkage, sparse-normal-means, horseshoe-prior方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，1391次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

早期摘要强调一组模型与二组稀疏问题的联系，同时使用“几乎普遍优越”等强措辞；这类宣传性措辞不进入现稿规范。正式版摘要则另列尾稳健与密度收敛两个定理，说明版本已发生实质变化。

## 引言的推进

§1 pp.1–7先把信号估计和分类分开，再定义局部/全局尺度及horseshoe命名，图形展示尾部与零点行为。早期稿包含读者群列表、长预告和大量立场对比；只借其目标分辨与定义顺序，不将篇幅和语气当已接收稿风格。

## 方法、定义与理论的依赖

§2 pp.7–9以全局收缩、离散混合、局部收缩统一比较对象；§3 pp.9–15将尺度混合改写为收缩权重，解释零附近与大信号两端需求，用同一小例对应直觉与数值，再比较离散混合的权重机制。早期稿只有密度界定理，不把正式摘要提到的另两个定理冒充本次已读证明。

## 数值、应用与证据

§4 pp.15–19用强/弱稀疏及多种损失检验估计，不从参评先验自身生成真值；§5 pp.18–24把分类阈值与后验纳入概率区分，并在固定信号数和改善信噪比两种机制下对比。§6 pp.24–27用极小例说明未知噪声下的超参数缩放及积分/代入差别，单例用于解释机制而非普遍结论。

## 结尾与主文分工

§7 pp.27–28的长立场性结尾属于早期稿，包含对double-exponential先验的宽泛否定；本库明确不把这种语气当Biometrika成熟稿的规范。尾部只迁移按数据情形选择默认先验、区分模型与算法的思考。

## 可迁移写作动作

新先验可以通过共同收缩坐标解释与已有方法的差别；密度形状、收缩规则、估计风险与分类规则要分别给出依据。权重形似概率时尤其要明确它不是后验概率。

## 不能泛化的特殊安排

本篇对论证逻辑有参考价值，对最终期刊段落、摘要、理论安排和语气均属低置信证据。horseshoe后验均值不自动产生精确零元；早期分类模拟不能写成一般FDR控制定理。正式终版仍列待补读。
