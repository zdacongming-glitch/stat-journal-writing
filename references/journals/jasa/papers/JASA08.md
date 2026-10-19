# JASA08 — Comparison of Discrimination Methods for the Classification of Tumors Using Gene Expression Data

作者：Sandrine Dudoit; Jane Fridlyand; Terence P Speed。正式发表：2002，JASA 97(457)，77-87。类型：Applications and Case Studies。

[DOI](https://doi.org/10.1198/016214502753479248) · [全文](https://www.stat.rice.edu/~cscott/stat699/dudoit.pdf) · [影响记录](https://openalex.org/W1966701961)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引2672次；正式发表至今至少八年，作为覆盖classification, genomics, comparative-evaluation的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读全文叙述：正式版pp.77–86（§1–6）；参考文献及在线补充未作为已读材料。

全文核验：PDF 11页；SHA-256 `316598c6de6b4882171f7169e47858fba2ecd8fcdc588f4a178d0ed4744b3a6a`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引2672次，正式发表至少八年。覆盖微阵列肿瘤分类的比较性原始研究及数据标准化和误差评价，补充ACS基准设计。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要先给肿瘤分类的科学需要，再界定多种分类器在三个公开表达数据上的比较，避免将研究写成单一新算法（p.77）。

## 引言的推进

§1由诊断不确定性进入表达测量，明确类发现、已知类别预测和marker选择三个任务，再指出既有“一法一数据”缺乏系统比较。本文只承诺解决比较任务（pp.77–78）。

## 方法、理论与章节依赖

§2按共享分类记号解释方法，§3给测量来源、缺失处理、标准化及基因筛选，§4独立说明比较设计，§5先总误差再个体困难样本、基因数量；§6解释原因和下一步决策（pp.78–86）。

## 数值与应用如何提供证据

重复LS/TS划分内进行基因筛选；2:1划分是为了比较而非精确估计generalization error。结果既比较平均误差，也追查困难样本的取材、样本类大小等来源（pp.82–85）。

## 结尾承担的任务

§6把简单法优势解释为小样本协方差估计困难，随后权衡解释性、交互、预处理、未覆盖方法及marker的生物意义；具体而较长（pp.85–86）。

## 可迁移写作动作

比较稿应明确选择设计服务于哪项问题；先报告整体排序，再解释排序为何随样本结构和任务改变，最后以困难样本回到科学含义。

## 不能泛化的特例与反例

不能把本语料中的小样本简单法优势移作今日普遍结论；本文未纳入SVM等有具体时代和训练成本背景。可借鉴设计解释，不复制过时性能推荐。
