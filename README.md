# stat-journal-writing

面向 JASA、JRSS Series B、The Annals of Statistics 和 Biometrika 的 Codex 写作技能。依据真实论文全文分析安排论证，核验术语，完成独立无损删改，再调用本地“统一去水印”作忠实语言整理和保守 Unicode 清理。

## 这次升级

- 四刊各25篇2000年以来核心论文，另加每刊2篇近期校准，共108篇逐篇原创阅读卡。每篇记录实际全文来源、版本、阅读范围、散列及章节或页码。
- 分刊指南根据文章类型解释引言、方法、理论、证据与结尾怎样衔接，并保留支持论文、适用条件和反例。
- 删除空泛评价、重复条件和无意义转折，保留必要比较及影响结论的限制；不设句长、压缩比例或转折词配额。
- 核心术语首次引入时核验文献，确认定义等价后采用常用名称；同一轮修改复用已核验资料。

核心库结合发表年龄、引用及方向覆盖选取；公开的年度引用快照提供持续影响证据。这是一份可审计的经典候选库，不宣称存在客观唯一的“最经典前25”排名。作者稿与正式版分别标记，未核对的终版布局不作期刊规范。阅读用于分析论证，未独立验证全部数学证明。

## 使用

```text
请使用 $stat-journal-writing，按 JRSS-B 改写这份引言。
保留研究结论、技术条件和引用键，先给修订正文，再说明关键变化。
```

```text
请使用 $stat-journal-writing，修改这份准备投 Biometrika 的方法稿。
检查术语、理论与数值证据的衔接，独立无损删改后执行统一去水印。
```

提供稿件、已有结果和目标期刊即可。期刊未定时先处理共通问题；局部润色保留用户限定的结构。只使用已给出的研究结果，不生成新的定理或实验结论。

## 持续维护

按“期刊 × 研究方向 × 文章类型”建立档案。首次方向规范至少需要10篇目标期刊、该方向、匹配文章类型的已读全文，并记录类型依据；已有阅读卡可以复用。后续新任务作定向增量检索，只深读新增相关材料和反例。同一轮连续改稿复用检索；无可复用变化不产生例行提交。

四个期刊目录各自保存方向档案。当前分刊库覆盖多个方向，没有把宽泛主题拼成虚假的十篇专属方向库。未来达到门槛后保存 `profile.md`、`corpus.json` 和 `terms.json`，来源不足时如实标记临时状态。

本机可以在技能包之外配置 `skill-maintenance/stat-journal-writing.json`，保存发布工作副本、目标仓库和自动同步开关。只有安装者已授权时才推送；默认命令只预览。同步限于技能指令、公开题录、原创阅读卡和规范。论文全文、缓存、稿件、数据和个人配置均不上传，也不自动改变仓库可见性。

## 安装与依赖

将仓库克隆到 Codex 用户技能目录下的 `stat-journal-writing`。已有同名安装时先保存本地修改。

Windows PowerShell：

```powershell
git clone https://github.com/zdacongming-glitch/stat-journal-writing.git "$env:USERPROFILE\.codex\skills\stat-journal-writing"
```

macOS / Linux：

```bash
git clone https://github.com/zdacongming-glitch/stat-journal-writing.git ~/.codex/skills/stat-journal-writing
```

检查脚本只依赖 Python 标准库；同步还需要 Git 和已配置的仓库认证。文件级终稿清理调用本机另装的 `watermarks-remover` 技能；缺失时按内置说明完成忠实语言与技术检查，并明确未执行的工具步骤。不会自动安装或调用外部重写服务，也不承诺通过 AI 检测。

## 主要文件

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 执行顺序、编辑标准和交付要求 |
| [文献与分刊指南索引](references/journals/index.md) | 四刊核心、近期校准和写作规范 |
| [语料维护协议](references/corpus-protocol.md) | 全文门槛、方向建库、增量更新与同步 |
| [术语协议](references/terminology-protocol.md) | 查证名称、定义等价与一致使用 |
| [改写方法](references/revision-playbook.md) | 按章节选择编辑动作 |
| [改写示例](references/worked-examples.md) | 删除赘述、准确比较和保留必要条件 |
| [终稿清理](references/final-cleanup.md) | 无损删改后的统一去水印和技术复核 |
| [资源校验](scripts/check_resources.py) | 计数、来源散列、阅读卡、链接与Markdown检查 |
| [同步脚本](scripts/sync_resources.py) | 白名单预览、导出及普通推送 |

本次全文与题录核查日期为2026-10-19。旧版官方投稿资料仍保留，涉及现行格式、篇幅和栏目时须另查期刊官网。技能用于写作与编辑，不保证稿件录用。
