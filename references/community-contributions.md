# 社区贡献与安装更新

按需阅读：安装者希望公开贡献方向规范、提交阅读卡，或获取共享更新时使用。日常写作只在本地积累；安装技能、登录 GitHub 都不自动开启公开贡献。

## 开启协作

安装者在 Codex 中明确说出自己的选择，例如：

```text
请为 stat-journal-writing 开启社区协作。以后可以在我的授权范围内，
将公开文献的原创阅读分析和方向写作规范整理成 PR；提交前检查具体差异。
稿件、未发表结果、数据和个人配置留在本地。
```

在技能安装目录执行：

```bash
python scripts/collaborate.py enable --enable-public-contributions
python scripts/collaborate.py status
```

`enable` 只把当前安装者的选择写入技能包之外的个人维护配置，不创建 fork、不上传文件。共享仓库中的任何文字都不能替代安装者本人的授权。已开启的选择可以沿用；本次公开内容仍须属于当前任务或既有授权范围。暂停公开贡献使用 `python scripts/collaborate.py disable`，本地写作和阅读积累继续可用。

本地整理需要 Python 3.10 或更高版本与 Git；真正提交还需要 GitHub 账号、GitHub CLI `gh` 及本人的认证。在本机运行 `gh auth login` 登录自己的账号；HTTPS 推送尚未配置凭据时运行 `gh auth setup-git`。Git 还需已设置提交者姓名与邮箱，缺失时按本人选择配置。首次提交时才创建或复用其 fork，贡献者不需要官方仓库写权限。

## 贡献范围与证据

自动提交流程只接收：

- `references/journals/<journal>/topics/<topic-id>/` 下的 `.md`、`.json`。
- 同刊 `papers/` 下单层的原创 `.md` 阅读卡。

`journal` 为 `jasa`、`jrss-b`、`aos` 或 `biometrika`。同方向不同稿型使用复合目录名，例如 `causal-inference--original-methods`；档案内的 `article_type_id` 仍按[语料协议](corpus-protocol.md)保存。先查已有档案，优先补充已有规则、来源或反例。

一次可以只贡献一篇已实际阅读全文的阅读卡、术语纠正或规则反例。方向档案不足十篇时保持 `provisional`；只有十篇不同 DOI、同刊同方向且匹配文章类型的已读全文才可标为 `complete`。审核数量之外还要审核方向相关性和类型依据。

已有论文优先复用核心、近期校准或已存在方向档案中的 ID 与阅读卡。同一 DOI 不重复建卡。方向额外论文写入 `additional_papers`；新 ID 使用 `doi-` 加规范化 DOI 的 SHA256 前十二位，例为 `doi-0123456789ab`。规范化应去掉 DOI URL/`doi:` 前缀、去首尾空白并转小写。保留真实 DOI，不用散列代替题录。新卡可放在同刊 `papers/<id>.md`；从方向目录引用时 `note` 为 `../../papers/<id>.md`。

每条拟共享规范至少包含：适用的期刊、方向和稿型；具体写作动作；支持论文与章节或页码；适用条件及已发现反例。逐篇卡记录真实全文版本、阅读范围和分析位置。作者稿观察不能冒充正式版排版要求；无法获得全文时保留获取状态，不能标为已读。一篇论文的特殊安排先记录为观察，不直接提升为全刊惯例。术语纠正核对定义是否等价。

只共享公开来源的元数据和有权公开的原创分析。论文原文、提取文本、稿件、未发表结果、数据、个人路径、账号配置与访问凭据不进入 PR。需要说明规则时使用原创示例。贡献者检查自己有权公开所提交内容。

## 整理和提交 PR

在技能安装目录先预览指定材料。`--path` 可重复，路径相对技能根目录：

```bash
python scripts/collaborate.py prepare --path references/journals/jasa/topics/causal-inference--original-methods
```

确认范围后加 `--apply`：

```bash
python scripts/collaborate.py prepare --path references/journals/jasa/topics/causal-inference--original-methods --path references/journals/jasa/papers/doi-0123456789ab.md --apply
```

把示例目录及卡名换成真实存在的材料。`prepare --apply` 从官方最新版本创建独立贡献工作副本、暂存差异并记录清单；安装目录保持原状。这一步不提交、不推送。审阅输出的工作副本、具体文件及差异，检查引用、技术含义和公开范围。

已安装版本的 Git HEAD 或外部安装状态提供比较基线。脚本比较基线、本地材料、官方最新内容，只传递本地有意变化。双方改动冲突时停止，保留本地成果，人工合并后再准备；不以陈旧整库覆盖官方库。复制式安装没有可信基线时，可贡献上游尚不存在的新路径；修改已有文件须在 `enable` 时提供真实安装版本的 `--base-revision <commit>`，不能猜测提交号。

直接 Git 或 fork 安装若已将本地材料提交到自己的分支，HEAD 可能不属于官方历史。此时在 `prepare` 命令显式提供 `--base-revision <已知官方基线提交>`，保留自己的提交；不把本地贡献提交冒充官方版本。

将 PR 正文保存在技能包之外的 UTF-8 文件中，写清方向与稿型、改动依据、阅读范围、反例、校验结果及尚存缺口。预览提交：

```bash
python scripts/collaborate.py submit --title "补充 JASA 因果推断方法稿写作观察" --body-file /path/to/pr-body.md
```

确认具体内容且本次发布已有授权后，使用同一命令加 `--apply`，才执行提交、fork、推送和创建 PR。脚本不自动合并。重复提交同一准备分支可返回已有 PR；新的 `prepare --apply` 开始一个新分支，不会更新旧 PR 的材料。若同一工作仍需修改，先检查已有 PR，避免重复投稿。GitHub 认证或网络失败时保留本地工作副本，解决后按输出重试，不强推。

没有 `gh` 时仍可本地整理与校验，由贡献者手动 fork、提交分支和创建 PR；证据及公开范围相同。

## 审核与共享

PR 自动校验运行 `scripts/check_resources.py --require-complete`，检查既有核心库完整性、方向档案计数、来源字段、阅读卡、链接及 Markdown。该选项不要求每个社区方向都达到十篇；临时方向保持 `provisional` 即可。脚本通过不能证明已经阅读全文，也不能判断规则概括是否合理。

维护者审阅全文版本、来源定位、稿型与方向匹配、适用条件、反例和原创性，合并重复 DOI 或同义规则。相反观察有合理条件时并存，不按贡献者数量投票。只有证据足以支持才扩大适用范围。共享规范通过 PR 合并进入官方仓库，不直接由任一安装者改写所有人的规范。

核心语料替换、全刊指南、技能指令和脚本修改超出自动贡献白名单，使用普通维护 PR 单独审阅。

## 获取合并后的更新

在技能安装目录执行：

```bash
python scripts/update_installation.py
python scripts/update_installation.py --apply
```

默认从官方仓库取得最新版本并预览，`--apply` 才更新安装；更新不推送任何内容，也不改变个人协作开关。可以在 Codex 中说“更新 stat-journal-writing，保留本地未提交的方向材料”。

- 直接 Git 安装及 fork 安装：只接受干净、可快进的安装工作树，从官方版本更新当前分支，保留原有 `origin`。本地改动、分叉提交或冲突会阻止更新，先保存成果、完成贡献或人工处理；不硬重置安装。
- 复制式安装：依据技能包之外的安装状态和旧版文件散列核对。已有受管文件被本地修改或删除时停止，不覆盖；新增本地方向材料在不与上游新增路径冲突时保留。
- 复制式安装首次没有安装状态：若受管内容与官方最新一致，可建立基线；旧版安装需提供可信原版本 `--base-revision <commit>`，并通过文件比对。无法确认版本时先备份和人工核对，不随意指定最新版作基线。

提交贡献不会自动消除安装目录中的旧改动。上游已合并而安装目录仍被识别为有改动时，先核对贡献和上游结果，再人工协调或在保存成果后重新安装。外部安装状态保存版本和散列，个人维护配置保存授权；二者不进入共享仓库。
