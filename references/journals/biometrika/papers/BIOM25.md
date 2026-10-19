# BIOM25 · Going off grid: computationally efficient inference for log-Gaussian Cox processes

题录：Daniel Simpson; Janine B. Illian; Finn Lindgren; Sigrunn H. Sørbye; Håvard Rue（2016），*Biometrika* 103(1)，49-70。[DOI](https://doi.org/10.1093/biomet/asv064)。

文章类型：regular computational methodology article; revised author manuscript。方向：spatial-point-processes, log-gaussian-cox-processes, computational-approximation。

全文：[公开来源](https://arxiv.org/pdf/1111.0641)。版本：arXiv:1111.0641v3, 2015-10-30, 22 pages; formal publication 2016; author version contains visible drafting residues and unresolved conjecture。

阅读范围：Complete main narrative pp.1–14, likelihood and random-field constructions, convergence statements, three examples, discussion, all captions; appendix pp.15–21 read for approximation roles, fixed-hyperparameter scope and conjecture, not independent proof verification; references inspected. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有215次引用，已有至少八年观察期；实际阅读全文后，作为spatial-point-processes, log-gaussian-cox-processes, computational-approximation方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，215次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要把直接近似似然与连续场连接，再分清积分误差、格点计数误差及SPDE近似；示例由标准点模式推进到非均匀采样和复杂海洋边界。

## 引言的推进

§1 pp.2–3从真实观测窗口和采样缺口进入，说明经典矩形完全观测设置不足，再定位格点INLA现法。关键贡献不是笼统加速，而是将场近似与似然近似分开。早期重复句和模板文字不作为写作范例。

## 方法、定义与理论的依赖

§2–3 pp.3–4先写点过程似然，指出格点同时近似随机场和精确位置这两个角色，后者迫使过细计算；§4 pp.4–6用一般有限基展开和确定性积分拆解两项，转成可由既有软件处理的Poisson形式。§5 pp.6–8才给首选SPDE、边界和网格实现；§6 p.8将两个近似的理论分别写出。附录固定超参数，且A4/A5后保留关于完整联合逼近的猜想，不能忽略这一版本的理论范围。

## 数值、应用与证据

§7 pp.8–12的三个例子逐一对应原有难点：雨林作规则窗口校准，缺采矩形显示局部粗化节省，海洋模拟显示复杂拓扑与边界先验如何改变不确定性。明确海洋风险图是模拟，海岸方差升高来自先验边界，不能当作真实灾害发现。

## 结尾与主文分工

§8 pp.12–14讨论其他非局部基会产生稠密矩阵、边界建模、超参数近似及非高斯扩展；每项都指向已展示方法的一项具体依赖。未把固定超参数的收敛改写成完整实践算法所有近似均有保证。

## 可迁移写作动作

计算近似论文应先拆分不同误差来源，再给统计与计算表示；样例按方法新获得的能力递进。边界条件影响科学结论时必须解释其来源，不能只报告漂亮地图。

## 不能泛化的特殊安排

所读2015稿的摘要/主文与附录的收敛说法存在需要终版复核的范围差异，另有明显草稿残留；只据其论证依赖学习，不作为终版措辞规范。高阶积分收敛受场光滑性限制；无点与未采样不是同一个观测事件。
