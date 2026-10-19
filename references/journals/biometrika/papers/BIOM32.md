# BIOM32 · Improving point and interval estimators of monotone functions by rearrangement

题录：Victor Chernozhukov; Iván Fernández-Val; Alfred Galichon（2009），*Biometrika* 96(3)，559-575。[DOI](https://doi.org/10.1093/biomet/asp030)。

文章类型：regular theoretical and methodological article; author manuscript。方向：shape-constrained-inference, rearrangement, confidence-bands。

全文：[公开来源](https://arxiv.org/pdf/0806.4730)。版本：arXiv:0806.4730v3, 2008-11-07; 24-page author version corresponding to 2009 Biometrika publication。

阅读范围：Complete main narrative pp.1–18, univariate/multivariate propositions and interpretations, confidence-band argument, growth-chart application and simulation; proof organization pp.18–22 and full simulation design pp.22–23; references inspected. Inequalities not independently verified. 阅读日：2026-10-19。页码均指所读PDF自身页序；HTML以节号定位。

## 入选依据

OpenAlex所取2000年后本刊高被引候选中有204次引用，已有至少八年观察期；实际阅读全文后，作为shape-constrained-inference, rearrangement, confidence-bands方向及其贡献类型的代表保留。这里实际核验的是引用快照、发表年龄、全文贡献与样本覆盖，未系统核验逐年引用或综述认可，不能据此宣称客观test-of-time排名。
引用线索：OpenAlex，2026-10-19，204次；不据此宣称唯一的‘最经典25篇’。

## 摘要的信息选择

摘要将保持单调、改善点估计距离及缩短同时置信带且保持覆盖分开，末句给生长图例；弱改善与严格改善的条件在正文分别处理。

## 引言的推进

§1 pp.1–2先列具有同一形状约束的对象，承认重排已用于单调化，再把“误差也改善”及“区间也改善”作为新增认识。最近邻isotonic方法只讨论直接可比较及可组合者。

## 方法、定义与理论的依赖

§2.1–2.2 pp.2–4从现有全局/局部估计的非单调性进入，用排序定义一维重排后给弱/严格改进，再解释Lorentz不等式。§2.3–2.4 pp.5–8推广逐坐标重排与顺序平均，以二点图解释与isotonization的不同并承认没有统一赢家。§3 pp.9–11先分清真正目标与错中心estimand，再给端点重排、保序和距离缩减分别如何支撑覆盖及长度。

## 数值、应用与证据

§4.1 pp.12–16用同一生长图比较四类原估计、年龄与分位数的二维约束和同时置信带。§4.2 pp.14–18按应用拟合生成模拟，报告多范数误差、覆盖与长度，承认重排/等序/平均无统一优胜。原始带先校准90%整体覆盖，清楚隔离后处理收益；附录B给完整生成设计。

## 结尾与主文分工

主文以哪些原估计获得覆盖改善或长度改善的具体差异结束，无额外Discussion；证明附录先有限步函数排序再推广，紧接模拟设计。

## 可迁移写作动作

后处理改进论文应先承认旧操作已有什么性质，再证明新增性质；“不变差”与“严格更好”分开。置信带的覆盖对象与端点操作必须明确，应用和模拟可围绕同一真实形状特征组织。

## 不能泛化的特殊安排

目标为常数时重排的距离可完全不变；错中心置信带覆盖的是被重排的estimand，不自动获得真实单调函数覆盖。置信带弱缩短是在指定积分范数下，不能说每一点都更窄。
