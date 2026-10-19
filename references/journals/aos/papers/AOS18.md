# AOS18 · Controlling the false discovery rate via knockoffs

题录：Rina Foygel Barber; Emmanuel J. Candès（2015），*The Annals of Statistics* 43(5)，2055-2085。[DOI](https://doi.org/10.1214/15-aos1337)。

文章类型：Original variable selection and finite-sample inference methodology research; IMS electronic reprint。

全文：[公开来源](https://arxiv.org/pdf/1404.5609)。版本：IMS electronic reprint arXiv:1404.5609v3, 2015-10-14; 33 PDF pages; formal 2015 AoS 43(5), pp.2055–2085, pagination differs。

阅读范围：已读PDF pp.1–31摘要及§§1–6全部主文叙述、knockoff与knockoff+定义和不同保证、交换性证明及证明提纲、模拟、HIV应用和序贯检验连接；pp.31–33文献定位。未逐行审查外部补充证明或重现实验。 阅读日：2026-10-19。所有PDF页码均指实际读取版本的自身页序，非正式印刷页序。

入选线索：Crossref当日记录561次引用，结合观察年限、实际全文贡献及方向覆盖保留；不称唯一test-of-time排名。

## 摘要的信息选择

摘要先以变量发现的科学需求定义FDR，再介绍构造型方法和有限样本目标、未知噪声及相关设计，最后区分统计量的普适框架与lasso实现的经验功效。严格范围须结合主文：knockoff+控制FDR，原knockoff控制modified FDR；p<n<2p估计方差扩充另有近似。

## 引言的推进

§1.1 pp.1–3先定义线性模型、选择集合和期望误选比例，解释与检验语言的对应。§1.2 pp.3–8直接给构造、统计量、阈值三步及两个主定理，以几何图解释原变量和副本竞争。方法已有完整可运行轮廓后才给路线图，未让历史综述挡住主贡献。

## 方法、定义与理论的依赖

§2 pp.8–15由Gram结构存在条件进入具体equi-correlated与SDP构造，再抽象出统计量的sufficiency和antisymmetry。交换性两引理推出零假设符号独立对称，随后给停时证明提纲；一般序贯理论暂后置，明确为保持回归主线。§5 pp.27–30才定义SeqStep/Selective SeqStep及其加一版本，再把按幅度排序后的符号视作one-bit p值，闭合早先主定理。

## 数值、应用与证据

§3 pp.15–23先用置换变量破坏交叉相关的反例说明为何不能随意替换构造，再对齐BH及保证修正的代价。表1同时标经验FDR、功效和是否有理论保证；相关性强时原knockoff误选超标如实报告，并回扣modified FDR。§4 pp.24–27逐药分析HIV：明确稀有变异筛选、去重复列、无交互假设，TSM面板来自不同研究且只近似真值、按位置核对。重尾噪声的半模拟另标经验稳健性。

## 结尾与附录分工

§6 pp.30–31由one-bit信息解释低信号保守性，提出多副本；明确本文没有理论研究漏选率，功效仅有经验分析。最后从可辨识性进入p>n的筛选拆分设想，维持待研究语气。补充材料承担完整停时等技术细节。

## 可迁移写作动作

先给完整特例算法与主保证，再提炼保证所需的抽象性质；一般工具可在应用和机制之后补齐，以免主线被泛化打断。对照表应区分经验成功和已证明保证，失败情形回连定理精确定义。外部验证必须交代参照名单与研究目标的差异。

## 特殊条件与不能泛化之处

此篇为固定设计高斯线性模型的原始knockoff框架，不能套成后来的model-X或任意p>n保证。n≥2p的基础构造不需噪声方差；p<n<2p插入估计方差的扩充只是近似。FDR控制是期望保证，不能解释为给定一次选择结果后已知其中恰有某比例错误；TSM名单也不是真实效应的完整标签。
