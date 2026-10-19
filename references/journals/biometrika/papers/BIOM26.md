# BIOM26 · Tuning parameter selectors for the smoothly clipped absolute deviation method

题录：Hansheng Wang; Runze Li; Chih-Ling Tsai（2007），*Biometrika* 94(3)，553-568。[DOI](https://doi.org/10.1093/biomet/asm053)。

文章类型：regular methodological and theoretical article; complete PMC author manuscript。方向：model-selection, penalty-tuning, semiparametric-regression。

全文：[公开来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC2663963/)。版本：complete author manuscript in PMC, linked to 2007 Biometrika DOI。

阅读范围：Complete HTML narrative: summary, sections 1–6, conditions, lemma/theorem statements and explanatory text, partially linear extension, simulations and labour-supply example, discussion, appendix proof narrative and regularity conditions. Equations consulted without independent verification. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有768次引用，已有至少八年观察期；实际阅读全文后，作为model-selection, penalty-tuning, semiparametric-regression方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，768次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要从SCAD的吸引力转到保证依赖调参这一具体缺口，再写GCV过拟合、新BIC选择的一致性和证据；摘要目标与后文定理同为识别真模型。

## 引言的推进

§1四段按欠/过拟合代价、传统分离选择的不足、SCAD同时估计与选择、其调参理论缺口推进。背景不是泛列全部正则化，而只保留解释本问题为何未被oracle性质解决的材料。

## 方法、定义与理论的依赖

§2先复习SCAD、自由度和GCV，由GCV对数近似AIC解释不一致性动机再给BIC。§3.1分别说明五个条件用于哪个结果，§3.2用不欠拟合及正概率过拟合两个引理合成结论；§3.3用一个能产生真模型的参考调参序列排除其他模型，明确它并不等于数据选出的最优调参。§4把同一比较推广至部分线性模型，带宽与惩罚分开选择的依据紧邻实施。

## 数值、应用与证据

§5.1交代局部二次算法、数值零阈值及为何未重复既有比较；§5.2同时衡量模型误差和选模复杂度，拆分欠/正确/过拟合。§5.3劳动供给数据报告具体变量、带宽、系数及删除五个观测的稳定性例，应用结论围绕所选模型。

## 结尾与主文分工

§6只有一段，提出广义线性、半参数及单指标的具体扩展；没有重复主要定理。证明集中附录，欠与过拟合分别处理。

## 可迁移写作动作

已有性质依赖理想调参时，要把“存在一个良好序列”与“数据选择能找到它”分清。条件后逐项说明作用；模拟同时评估准则真正追求的目标和其他实际代价。

## 不能泛化的特殊安排

固定维度线性/部分线性的一致性不能无条件推广到任意高维或任意损失；应用中选后系数显著不自动给出选择调整后的推断。历史引言对方法的概括需以今日文献重新核验。
