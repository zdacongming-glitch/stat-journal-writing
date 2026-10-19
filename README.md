# stat-journal-writing

面向 JASA、JRSS Series B、The Annals of Statistics 和 Biometrika 的 Codex 写作技能。依据真实论文全文分析安排论证，核验术语，完成独立无损删改，再调用本地“统一去水印”作忠实语言整理和保守 Unicode 清理。

## 写作依据

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

其他安装者也可贡献自己的方向规范、术语核验和原创阅读卡。开启后，Codex 从选定材料准备独立贡献分支，经个人 fork 提交 PR；维护者审核合并，再由各安装者更新本地技能。贡献不足十篇也可提交，方向状态保持临时，不因此降低完整档案门槛。

默认只在本地积累。公开贡献需要安装者本人明确开启，不会继承维护者的配置或授权。同步只包含公开题录、原创阅读卡和规范；论文全文、缓存、稿件、未发表结果、数据和个人配置留在本地。详见[贡献指南](CONTRIBUTING.md)。

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

检查脚本只依赖 Python 3.10 或更高版本的标准库；同步还需要 Git 和已配置的仓库认证。文件级终稿清理调用本机另装的 `watermarks-remover` 技能；缺失时按内置说明完成忠实语言与技术检查，并明确未执行的工具步骤。不会自动安装或调用外部重写服务，也不承诺通过 AI 检测。

## 开启社区协作

安装后在 Codex 中说：

```text
请为 stat-journal-writing 开启社区协作。以后可以在我的授权范围内，
把公开文献的原创阅读分析和方向写作规范整理成 PR，提交前检查具体差异。
稿件、未发表结果、数据和个人配置留在本地。
```

Codex 在技能目录执行一次：

```bash
python scripts/collaborate.py enable --enable-public-contributions
python scripts/collaborate.py status
```

这一步只保存当前安装者的本地选择，不上传文件。真正提交需要本人的 GitHub 账号、已设置提交身份的 Git，以及 GitHub CLI `gh`：先运行 `gh auth login`，需要配置 HTTPS 推送凭据时再运行 `gh auth setup-git`。首次提交时再创建或复用 fork，无需预先 fork 或拥有官方仓库写权限。以后可以说“把本次 JASA 因果推断方法稿中得到的可复用规范整理成社区 PR”。Codex 会选定具体路径，预览差异，校验后按已有授权提交；PR 由维护者审核，不自动合并。

也可手动使用 `prepare --path <方向目录>` 预览、加 `--apply` 建立独立工作副本，再用 `submit --title <标题> --body-file <正文文件>` 预览、加 `--apply` 提交。具体命令、贡献白名单、全文证据和基线冲突处理见[社区贡献协议](references/community-contributions.md)。停止公开贡献运行 `python scripts/collaborate.py disable`。

## 更新安装

在技能目录执行：

```bash
python scripts/update_installation.py
python scripts/update_installation.py --apply
```

第一条预览官方最新版本，第二条才更新本地。Git 安装及 fork 安装要求工作树干净且可快进，保留原 `origin`；复制式安装按外部版本记录核对文件，保护本地修改和新增方向材料，冲突时停止。旧复制版没有版本记录时，可能需要提供可信安装提交 `--base-revision <commit>`；不能猜测版本号。更新不上传内容，也不改变协作开关。

## 主要文件

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 执行顺序、编辑标准和交付要求 |
| [文献与分刊指南索引](references/journals/index.md) | 四刊核心、近期校准和写作规范 |
| [语料维护协议](references/corpus-protocol.md) | 全文门槛、方向建库、增量更新与同步 |
| [社区贡献协议](references/community-contributions.md) | 本人开启、贡献白名单、PR审核与安装更新 |
| [贡献指南](CONTRIBUTING.md) | 证据要求、评审准则和提交方式 |
| [术语协议](references/terminology-protocol.md) | 查证名称、定义等价与一致使用 |
| [改写方法](references/revision-playbook.md) | 按章节选择编辑动作 |
| [改写示例](references/worked-examples.md) | 删除赘述、准确比较和保留必要条件 |
| [终稿清理](references/final-cleanup.md) | 无损删改后的统一去水印和技术复核 |
| [资源校验](scripts/check_resources.py) | 计数、来源散列、阅读卡、链接与Markdown检查 |
| [同步脚本](scripts/sync_resources.py) | 白名单预览、导出及普通推送 |
| [社区协作脚本](scripts/collaborate.py) | 个人协作开关、准备差异与 fork PR |
| [安装更新脚本](scripts/update_installation.py) | 预览官方更新、保护本地成果并更新安装 |

本次全文与题录核查日期为2026-10-19。旧版官方投稿资料仍保留，涉及现行格式、篇幅和栏目时须另查期刊官网。技能用于写作与编辑，不保证稿件录用。
