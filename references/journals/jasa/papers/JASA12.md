# JASA12 — Empirical Bayes Analysis of a Microarray Experiment

作者：Bradley Efron; Robert Tibshirani; John D Storey; Virginia Tusher。正式发表：2001，JASA 96(456)，1151-1160。类型：Applications and Case Studies。

[DOI](https://doi.org/10.1198/016214501753382129) · [全文](https://genomics.princeton.edu/storeylab/papers/ETST_JASA_2001.pdf) · [影响记录](https://openalex.org/W2074089196)。核验与阅读：2026-10-19。

入选依据：OpenAlex查询时被引1734次；正式发表至今至少八年，作为覆盖empirical-bayes, multiple-testing, genomics的长期影响原创论文。此数值用于候选发现，不构成最经典的唯一排序。

阅读范围：已阅读全文叙述：正式版pp.1151–1160（§1–6，含A–F实际分析备注）；未复核原生物实验或重新跑数值。

全文核验：PDF 10页；SHA-256 `3b66ac9cfeec075763408996d647c713712c70442e81bc7231ae2990b4d71c54`。本卡仅保存原创篇章分析，不分发全文。

选读定位：OpenAlex当日被引1734次，正式发表至少八年。覆盖local false discovery rate和微阵列的empirical Bayes分析，展示应用驱动的推断目标。该判断由影响计数、论文原始贡献与方向覆盖组成，不是已核验的唯一经典排名。

实际读取版本：Published journal typeset article, publicly hosted institutional copy; printed page numbers recorded in note。

## 摘要的信息选择

摘要直接给辐射实验、数千基因的数据缩减及同时推断两项问题，经验贝叶斯模型同时解决两项，并交代与FDR的联系（p.1151）。

## 引言的推进

§1先说明比较处理/对照的科学任务，简评已有分析路线，再解释microarray测量与八阵列实验设计。生物背景服务于后面的pm/mm、细胞系和技术重复区别（pp.1151–1152）。

## 方法、理论与章节依赖

§2先把320数/基因拆成probe、gene和inference三次映射；§3建立两组混合与算法；§4用保留Bayesian信息比较数据缩减；§5才解释与frequentist FDR的关系；§6集中操作性备注（pp.1152–1160）。

## 数值与应用如何提供证据

同一实验贯穿处理前后，独立Northern Blot验证补充可信度；FDR模拟按同样数据结构检验校准，且展示更有效缩减可随数据改变。bootstrap专门回应数据择优的过拟合问题（pp.1155–1159）。

## 结尾承担的任务

§6短总结后附具体实验、亮度处理、密度比估计、null构造和p0上界；每条备注提供复用所需信息，而非反复宣讲局限（pp.1158–1160）。

## 可迁移写作动作

应用驱动的新方法可按数据变成结论的统计映射组织；把每个预处理选择连接至保留信息或推断有效性。

## 不能泛化的特例与反例

这是ACS原文但有新方法与理论解释；早期技术介绍不能照搬到今日成熟领域。2001 local fdr包含p0，与Efron2004本文采用的上界式用法须区分。
