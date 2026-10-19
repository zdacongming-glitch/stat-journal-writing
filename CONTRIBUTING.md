# 贡献指南

欢迎贡献四刊公开文献的原创阅读分析、方向规范、术语纠正及反例。可以从一篇论文开始。完整操作及安装差异见[社区贡献与安装更新](references/community-contributions.md)。

## 贡献内容

以“期刊 × 研究方向 × 文章类型”组织材料。优先扩充已有档案，方向目录示例为 `references/journals/jasa/topics/causal-inference--original-methods/`。目录含 `profile.md`、`corpus.json`、`terms.json`；字段与门槛见[语料协议](references/corpus-protocol.md)及[术语协议](references/terminology-protocol.md)。

- 规范写清具体写作动作、适用条件、来源论文及章节或页码，并记录反例。
- 逐篇卡基于实际阅读全文的原创分析，记录真实版本与阅读范围，不复制论文叙述。
- 不足十篇的方向标为 `provisional`，允许多位贡献者逐步补充。十篇同刊、同方向、同稿型、不同 DOI 的已读全文及类型依据，才支持 `complete`。
- 先按 DOI 检查已有记录，复用现有 ID 和卡。额外新论文 ID 为 `doi-` 加规范化 DOI 的 SHA256 前十二位，卡放同刊 `papers/`，元数据放方向 `additional_papers`。规范化规则和引用路径见社区协议。
- 原稿观察、论文经验、编辑意见、官方现行要求分别标记。一篇文章的偏好不自动成为全刊规则；缺乏反例检索或跨作者证据时保留有限适用范围。

只提交公开文献元数据和有权公开的原创内容。稿件、未发表结果、数据、论文全文、提取文本、下载缓存、个人配置及凭据留在本地。PR 公开前由贡献者核对具体内容；仓库安装行为不等于公开授权。

## 通过 Codex 贡献

安装者明确要求开启社区协作后，在技能目录运行：

```bash
python scripts/collaborate.py enable --enable-public-contributions
python scripts/collaborate.py status
```

这只记录本人的本地选择。准备与提交均先预览，只有加 `--apply` 才执行相应动作：

```bash
python scripts/collaborate.py prepare --path references/journals/jasa/topics/causal-inference--original-methods
python scripts/collaborate.py prepare --path references/journals/jasa/topics/causal-inference--original-methods --apply
python scripts/collaborate.py submit --title "补充 JASA 因果推断方法稿写作观察" --body-file /path/to/pr-body.md
```

将示例路径替换为实际材料。`prepare --apply` 创建独立工作副本和暂存差异，不提交、不上传。审阅具体文件及差异后，若本次公开内容已获当前任务或既有授权，在 `submit` 命令加 `--apply` 才提交、创建或复用个人 fork 并发起 PR。需要 GitHub 账号及已登录的 `gh`。脚本不自动合并；新准备轮次使用新分支，先检查是否已有相关 PR。

自动贡献白名单限于四刊 `topics/<topic-id>/` 中的 `.md`、`.json` 以及同刊 `papers/*.md`。修改已有文件使用真实安装基线进行三方比较，双方冲突时停止。没有基线的复制式安装只允许准备上游尚不存在的新路径；修改已有路径时须提供可信 `--base-revision`。

没有 `gh` 也可手动 fork，建立贡献分支，仅提交相关文件并创建 PR。核心库替换、全刊指南、技能指令、脚本或仓库配置的变更，请走普通维护 PR，不塞入方向贡献流程。

## 校验与评审

从仓库根目录运行：

```bash
python scripts/check_resources.py --require-complete
```

PR 和主分支有同一资源校验。`--require-complete` 保护既有百篇核心库及近期校准库；社区方向不足十篇仍可保持临时状态。脚本检查数量、引用关系、必需字段、链接和 Markdown，不能证明实际阅读、来源解释正确或学术概括合理。

维护者按证据评审：

1. 来源能否定位，正式版本、作者稿和阅读范围是否准确。
2. 是否匹配方向与文章类型，术语定义是否等价，规则适用范围是否超过证据。
3. 是否补充独立作者证据和反例，是否与已有规则重复或有条件兼容。
4. 是否为原创分析，是否含不应公开的稿件材料，技术条件和结论是否被误改。

反向证据可以缩小、修订或取代规则，记录原因和来源；有条件的不同写法可以并存。CI 通过后仍需维护者评审，自动流程不合并 PR。合并只更新官方共享库，其他安装者需执行安装更新后才能获得变化。

## 更新个人安装

在技能目录运行 `python scripts/update_installation.py` 预览，确认后加 `--apply`。直接 Git 或 fork 安装须工作树干净且可快进；复制式安装依据外部版本记录和文件散列核对，遇本地修改或同名新增路径冲突时停止。旧复制版缺少状态时，需要可信安装提交 `--base-revision` 并通过核对。具体处理见[社区协议](references/community-contributions.md#获取合并后的更新)。

更新不会公开内容或开启贡献。停止贡献使用 `python scripts/collaborate.py disable`。
