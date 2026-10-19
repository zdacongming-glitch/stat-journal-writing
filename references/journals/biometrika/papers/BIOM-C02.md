# BIOM-C02 · Flexible control of the median of the false discovery proportion

近期校准：2024，*Biometrika* 111(4)，1129-1150。[DOI](https://doi.org/10.1093/biomet/asae018)。

Jesse Hemerik; Aldo Solari; Jelle J Goeman。

近期方向样本，用于校准核心经典库的术语与叙述安排；不占核心25篇，不声称已通过长期检验。

文章类型：regular methodological and theoretical article; revised author version with supplement。

全文：[所读公开稿](https://arxiv.org/pdf/2208.11570)；arXiv:2208.11570v4, 2024-03-13, 37-page author PDF including supplement; formal 2024 Biometrika volume 111(4), pp.1129–1150。

阅读范围：Complete main narrative PDF pp.1–21, all main definition/assumption/theorem interpretations, running examples, algorithm explanation and simulations; supplementary general-estimator discussion pp.33–37 additionally read. Supplementary detailed proofs and RNA-seq application not fully read or counted. 阅读日：2026-10-19；页码为所读PDF页序。

## 摘要的信息选择

摘要先给中位数FDP控制及数据后选阈值的自由，再说明输入、同时中位数上界、依赖条件和复杂度；不把中位数与均值控制混称FDR。

## 引言推进

§1 pp.1–3从常用误差目标进入，再说明相关下FDP变异、高置信方法功效代价、研究者数据后改阈值的实际需要。术语名称明确说明既有Schweder–Spjøtvoll–Storey不同叫法，并给关联引用；最近邻按可用输入、同时性和适应性比较。

## 方法、定义与理论

§2 pp.3–6先给固定阈值下真零/假发现数量的中位数上界；§3.1–3.3 pp.6–10解释点态不蕴含同时，再由嵌套候选包络构造同时界，接closed testing与可容许性。§3.2单独用两个简例证明BH数据后调水平的问题。§3.4–3.6 pp.11–16从默认包络、贯穿例、可选择阈值到调整p值和线性计算实现；每个定义都有随后使用位置。

## 数值与应用

§4 pp.16–20同时检查所有阈值上的错误事件，而不是只检查某个固定水平；独立、同相关、分块和负相关设置分开，基准的保证和输入条件先说明。报告小目标水平时竞争法可更强、BH固定水平功效略高及成本差异，方法优势落在允许的使用方式。

## 结尾

§5 pp.18–21回到探索性使用、包络选择及功效分配，明确中位数可能不如均值目标吸引人，未知依赖下也无普遍保证；鼓励额外报告FDP区间，并分清新估计量与完整误差控制程序的后续工作。

## 可迁移动作

当创新是新的数据使用自由时，先给一个旧法失效的最小例，再证明同时性如何补足；复用同一running example贯穿中间估计、包络和最终拒绝决定，减少重复背景。

## 特殊范围与限制

不需独立性不等于允许任意未知依赖；中位数控制不等于FDR控制。所读接近录用时的作者稿有个别术语/调整p值表述需以正式版定理为准，只迁移逻辑安排。两篇近期论文只作方向和年代校准，不称test-of-time经典。
