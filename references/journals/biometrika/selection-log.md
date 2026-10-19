# Biometrika 核心筛选与获取记录

日期：2026-10-19。候选池为OpenAlex来源Biometrika的2000年后article，按当日累计引用检索前100条；原始API响应、DOI题录、全文和获取日志保留在本地研究缓存。文章经典性按高引用线索、观察年限、实际全文贡献与样本覆盖判断，没有宣称完成系统的历年引用及综述认可交叉验证。

核心25篇包括方法与理论、计算、因果识别、试验设计、形状约束、非参数检验及矩阵工具，正式年份2000–2018。讨论回复和仅摘要没有计数。近期2020/2024两篇单列校准库。

## 高影响候选未纳入的实际原因

| 候选 | DOI | 获取结果与处理 |
| --- | --- | --- |
| Testing the number of components in a normal mixture，2001 | 10.1093/biomet/88.3.767 | 出版社PDF403，其他公开来源未取得可核验全文；不依据摘要入选。 |
| A new family of power transformations to improve normality or symmetry，2000 | 10.1093/biomet/87.4.954 | 出版社与JSTOR未取得完整公开稿；不计数。 |
| Predicting the output from a complex computer code when fast approximations are available，2000 | 10.1093/biomet/87.1.1 | 作者公开页只有摘要，历史链接失效；不计数。 |
| A simple and efficient simulation smoother for state space time series analysis，2002 | 10.1093/biomet/89.3.603 | 出版社403，机构记录无全文，发现的第三方阅读笔记不是原论文；不替代。 |
| Conditional Akaike information for mixed-effects models，2005 | 10.1093/biomet/92.2.351 | 只找到请求全文页及不同的短会议版本；不冒充期刊全文。 |
| Principal component models for sparse functional data，2000 | 10.1093/biomet/87.3.587 | 历史Stanford源TLS失败或404，尚未取得原论文完整文件；不计数。 |
| Improving generalised estimating equations using quadratic inference functions，2000 | 10.1093/biomet/87.4.823 | 出版社403，现作者页未找到全文；不以题录推测写法。 |
| A note on composite likelihood inference and model selection，2005 | 10.1093/biomet/92.3.519 | 作者/机构稿未能下载，聚合源超时；不计数。 |
| Efficient balanced sampling: the cube method，2004 | 10.1093/biomet/91.4.893 | 历史RERO全文410，新机构记录未暴露可用文件；不计数。 |

补入的九篇不是机械的引用序号顺延，而兼顾可取得真实全文和方法方向：SCAD调参、多个图联合估计、MaxPro设计、pseudo-marginal效率、稀疏协方差、双重稳健估计、重排、距离秩独立性检验、自适应核范数。它们的引用线索、题录、原文版本及实际阅读范围均在core-corpus.json及逐篇卡片。

## 获取与题录的特殊情况

- BIOM31原PDF直取403，但网页PDF阅读器提供完整12页；已保存全部746行及三个原响应，散列明确只覆盖提取文本。
- BIOM06 PDF字体映射损坏，完整17页用系统英文OCR恢复叙述；公式符号未作为可靠证明转录。
- BIOM08仅取得作者官方站30页早期稿。另尝试出版社、FSU作者教学PDF、UT作者旧站及CiteSeer公开副本，未取得正式16页正文；该篇不得提供终版风格强证据。
- BIOM15出版社题录列539–552，实际公开正式PDF和作者书目列539–551；末页551为参考文献结尾。题录与所读版本分别记录。
- BIOM33正式卷100(2)为2013，OpenAlex快照2012及arXiv2012属上线/预印本时间；核心采用正式卷期年。
- BIOM12题录来源拼写indentification已按全文标题纠正为identification，未改变DOI。

后续取得更可靠版本时，保留旧版本和旧分析，逐项复核差异，再更新卡片与指南；不能仅更换URL就声称终版已读。
