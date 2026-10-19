# BIOM24 · Identifying causal effects with proxy variables of an unmeasured confounder

题录：Wang Miao; Zhi Geng; Eric J. Tchetgen Tchetgen（2018），*Biometrika* 105(4)，987-993。[DOI](https://doi.org/10.1093/biomet/asy038)。

文章类型：Miscellanea (running header in author version)。方向：causal-inference, proxy-variables, identification。

全文：[公开来源](https://arxiv.org/pdf/1609.08816)。版本：arXiv:1609.08816v4, 2018-06-28 author version; journal publication 2018。

阅读范围：Author PDF pp.1–8: complete main narrative, graph/table, identification formulas, conditions, theorem statements, testing argument, discussion, appendix proposition and references; supplementary proofs and simulations not retrieved or counted as read. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有231次引用，已有至少八年观察期；实际阅读全文后，作为causal-inference, proxy-variables, identification方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，231次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要直接给未观测混杂、两个代理和秩条件，核心认识是因果目标可识别并不要求整个测量误差机制可识别；不足以识别时另给零效应检验。

## 引言的推进

§1 pp.1–2按普通代理调整仍有偏差、外部误差信息、双代理识别三步缩小最近邻文献。图1与表1把六个因果结构和条件独立对应起来；引言末明确更一般结构下目标可识别而中间机制不可识别的缺口。

## 方法、定义与理论的依赖

§2 pp.3–4先离散矩阵关系，再秩条件、消去潜变量的识别公式及二元特例；§3 pp.4–5把秩条件提升为完备性，写出积分方程后给定理。一般机制不必识别的解释只放在关键消去位置。

## 数值、应用与证据

§3 Example 1用正态代理结构给可计算的半参数例，并说明与最近邻正态模型的关系。§4 pp.5–6在识别不满足时转向因果零假设检验，先解释残差变异再给极限分布。数值检验的完整设置在补充材料，本文笔记未从主文一句话推断其细节。

## 结尾与主文分工

§5 p.7将目标识别与潜在类别全模型识别联系，给负控制解释、观测协变量和多混杂扩展，同时明确非参数积分方程估计留待后续。结尾贡献是定位可用范围及下一真实难题。

## 可迁移写作动作

识别论文先决定究竟需要识别哪个量；用可消去的中间量组织代数，少写一般性背景。不能把识别、估计与检验合写成一个模糊的‘推断框架’。

## 不能泛化的特殊安排

这是短篇识别贡献，正文不展开完整估计算法；其留待后续的边界有实质作用。代理的条件独立、秩与完备性不可为简洁而删除。
