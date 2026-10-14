# stat-journal-writing

面向统计学四大期刊的 Codex 写作 skill：Journal of the American Statistical Association（JASA）、Journal of the Royal Statistical Society Series B（JRSS-B）、The Annals of Statistics（AoS）和 Biometrika。

根据已有稿件与研究结果，诊断和改写摘要、引言、方法、理论结果、模拟、应用及讨论。先调整论证，再润色句子，保留数学内容、技术条件与结论的证据边界。

## 适用任务

- 局部英文润色，保留原有论证结构和技术含义。
- 重排段落和贡献叙述，解释统计问题、现有障碍、新思想及证据。
- 根据已有研究材料起草正文，不编造定理、实验或引用。
- 对照目标期刊的当前官方要求进行投稿前文字检查。
- 参考经典统计论文，学习与当前稿件论证任务相近的写法。

JASA 的应用论文与方法论文分别处理。官方要求、署名编辑建议、经典论文观察和本 skill 的编辑建议保持区分。

## 安装

将本仓库克隆到 Codex 的用户技能目录。目标目录应尚不存在；已有同名安装时，请先保留自己的修改。

Windows PowerShell：

```powershell
git clone https://github.com/zdacongming-glitch/stat-journal-writing.git "$env:USERPROFILE\.codex\skills\stat-journal-writing"
```

macOS / Linux：

```bash
git clone https://github.com/zdacongming-glitch/stat-journal-writing.git ~/.codex/skills/stat-journal-writing
```

安装后重新打开 Codex，在技能列表中选择“统计学四大期刊写作”，或在消息中使用技能名。

## 使用示例

```text
请使用 $stat-journal-writing，按 JRSS-B 的目标读者重写下面的引言。
保留研究结论、技术条件和引用键，先给修订正文，再说明关键修改与待核实事项。
```

```text
请使用 $stat-journal-writing，检查这份准备投 Biometrika 的稿件。
重点检查摘要是否明确、定理前的动机是否充分、模拟结论是否超出证据，
并核对当前官方投稿要求。
```

提供目标期刊、文章类型、待改正文和已有结果即可；期刊未定时，skill 会先处理共通的论证与语言问题。

## 文件说明

| 文件 | 内容 |
| --- | --- |
| [SKILL.md](SKILL.md) | 工作范围、改写流程、交付要求与技术含义检查 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 展示名称、简介和默认提示词 |
| [references/jasa.md](references/jasa.md) | JASA 写作与投稿资料 |
| [references/jrss-b.md](references/jrss-b.md) | JRSS Series B 写作与投稿资料 |
| [references/aos.md](references/aos.md) | The Annals of Statistics 写作与投稿资料 |
| [references/biometrika.md](references/biometrika.md) | Biometrika 写作与投稿资料 |
| [references/classic-papers.md](references/classic-papers.md) | 经典论文索引与写作观察 |
| [references/revision-playbook.md](references/revision-playbook.md) | 各章节改写方法与检查要点 |
| [references/worked-examples.md](references/worked-examples.md) | 前后改写与证据边界示例 |

## 资料时效与边界

参考资料的来源核查基准日为 **2026-09-30**。需要当前格式结论或投稿前核查时，应重新访问目标期刊的官方作者页面、文章类型说明和模板。

本 skill 不替代研究创新评估、定理证明或实验结果生成，也不保证稿件录用。完整工作要求见 [SKILL.md](SKILL.md)。
