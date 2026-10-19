# BIOM33 · A consistent multivariate test of association based on ranks of distances

题录：Ruth Heller; Yair Heller; Malka Gorfine（2013），*Biometrika* 100(2)，503-510。[DOI](https://doi.org/10.1093/biomet/ass070)。

文章类型：regular methodological and theoretical article; author version with supplement。方向：nonparametric-testing, multivariate-independence, distance-ranks。

全文：[公开来源](https://arxiv.org/pdf/1201.3522)。版本：arXiv:1201.3522v3, 2012-05-31; formally published in Biometrika volume 100, 2013; PDF includes supplement。

阅读范围：Complete main narrative pp.1–8, theorem cases and computational explanation, all simulations and HapMap example; main proof narrative pp.8–11, supplementary cases, inversion-count algorithm explanation and additional simulations/application pp.12–19. C code inspected for role, not executed or independently verified. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有244次引用，已有至少八年观察期；实际阅读全文后，作为nonparametric-testing, multivariate-independence, distance-ranks方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，244次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要直接给任意维向量独立性检验、对备择的一致性、简单统计量和数值例；正文随后将“所有备择”细分为密度连续性和离散支持情形，不能只保留摘要口号。

## 引言的推进

§1 pp.1–2用基因组/脑成像需求引出明确零备择，再给距离秩对象，最后只比较少数同样具有一致性的现法。创新比较对象由所需性质选定，不列与任务不相关的全部相关系数。

## 方法、定义与理论的依赖

§2 pp.2–4先假想oracle找到局部依赖点和球半径，把问题变成2×2表；再用每对样本轮流充当中心/半径并累加统计量，最后给置换p值、四种一致性情况。§2后部pp.4–5把表计数改写为排序逆序数，使朴素三次复杂度降为二次对数；算法细节放补充。

## 数值、应用与证据

§3 pp.5–7解释为何以distance covariance为主基准，按非单调几何、多维非线性、混合重尾逐步增加困难，报告重复数和误差；重尾例同时说明竞争法矩条件的范围。§4 pp.7–8交代HapMap预处理导致样本降至43，仍有数万维，两个检验均显著，未以更小p值声称科学结论不同。补充另用飞机设计例和重复子样本。

## 结尾与主文分工

§5 p.8说明似然比替代可产生相似结果，真正的新问题是定位哪些子向量/局部区域依赖，并承认仍属后续研究。主文没有重复所有功效表。

## 可迁移写作动作

可用一个理想oracle先解释统计量要聚合的局部信息，再把oracle选择换成可观测枚举；复杂度改进由同一计数表达推出。高维应用先交代清洗与样本量，显著性不冒充效应定位。

## 不能泛化的特殊安排

固定维度下一致性不自动保证维度随样本任意增长时一致；必须保留混合/连续情形的局部条件及距离由范数导出。当前论文标题和正式2013年已核对，arXiv2012年不能替代正式年。 出版社卷100(2)及正式PDF年为2013；OpenAlex快照2012是提前上线年份，不作卷期年。
