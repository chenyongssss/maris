# MARIS：三个可复现的演示任务

**Understand · Verify · Decide｜理解、验证、决策**

MARIS 面向 Agent 高速执行后出现的“理解债务”：**并非所有输出都需要你逐行阅读，但影响正确性、证据与最终责任的部分必须让你看清楚。** 三个案例使用不同领域、不同证据级别；它们是可展示的技术任务，**尚未构成真实用户研究或 Agent 模型优越性评测**。

## Demo 01｜Coding：记录了 30 天，为什么还需要审查？

[阅读完整案例](01-coding/README.md) · [真实 RevAgent 初始提交](https://github.com/chenyongssss/revagent/commit/42ab1cb4488051a6c4066b3053deea548d47be27) · [真实后续修复](https://github.com/chenyongssss/revagent/commit/40b48733b1d8e9b0641dbb750c488b1f77bae2f1)

- **真实任务：** 开发 RevAgent 的授权式历史记忆机制，包括导入、脱敏、审批、全文检索和删除。
- **关键观察：** 初期代码把 `30_days` 保存为保留规则，但在该历史版本的搜索和索引逻辑中尚无到期自动清理。之后真实提交增加了基于批准时间的到期清理，并用回退时间戳测试。
- **普通总结容易停留在：** “新增历史记忆流程及测试”。
- **MARIS 的审查重点：** “**数据保留规则是否只是被声明，还是实际执行？**”区分审批、脱敏、到期和索引删除四个条件。
- **画像作用（虚拟画像）：** 对熟悉 Python 但不熟悉数据保留法规的用户，用“时间不变量”解释这个问题；不重复 Python 基础。*高风险审查不会因为熟悉代码而被跳过。*

注意这不是当前 RevAgent 存在缺陷的声明，更不是用户数据发生泄漏的证据。针对特定历史提交所做的可审计回顾。

## Demo 02｜Research：有限点观测真的能保证 Poisson 解唯一吗？

[阅读完整案例](02-research/README.md) · [精确算术脚本](02-research/evidence/poisson_checker.py) · [完整数学论证](02-research/evidence/argument.md)

取 \(\Omega=(0,1)^2\)，\(a(t)=t(1-t)\)。设

\[
 u_0(x,y)=30a(x)a(y),\qquad f=60[a(x)+a(y)],
\]

并构造

\[
 u_1(x,y)=u_0(x,y)+(x-\tfrac12)^2-(y-\tfrac12)^2.
\]

- **相同 PDE：** \(-\Delta u_0=-\Delta u_1=f\)。
- **相同有限观测：** 在 \(\{0.3,0.7\}^2\) 的四个点上，\(u_0=u_1\)。
- **不同的场：** 在 \((1/2,1/4)\)，差值为 \(-1/16\)。
- **重要边界：** 如果完整的 Dirichlet 边界已知，这一反例不再适用；如果在真正的开子域上无噪声地知道解的全部值，唯一延拓也不受此反例否定。

执行：

```bash
python demos/02-research/evidence/poisson_checker.py
```

**已真实执行**：精确分数计算通过。该验证证明了上述构造，不证明任何 PINN 训练性能，也未使用未公开论文中的审稿意见或原文。

- **MARIS 的核心介入：** 优先提示“有限采样算子未必单射”，而不是泛泛建议“补充唯一性分析”。
- **画像作用（虚拟 PDE 研究员）：** 无需讲解 Poisson 定义，直接关注观测拓扑、函数空间、条件稳定性、正则化与有限噪声数据。

## Demo 03｜Decision：Simulink、CAD、EDA 的开源突破口，先做谁？

[阅读完整案例](03-decision/README.md) · [公开资料证据台账](03-decision/evidence/source-ledger.json) · [可修改的假设权重](03-decision/evidence/option-scores.json)

- **真实问题：** 从现有开源工程软件生态中寻找“范围小、技术可验证、可以公开发布”的首次演示项目，而非立刻替代完整商业软件。
- **公开事实：** FMI/SSP 是动态模型交换/协同仿真的开放路径；FreeCAD/OCCT 提供 STEP 几何交换基础；OpenROAD 生态提供开源 RTL-to-GDS 流程。详细 URL 在证据台账中。
- **不能从事实推出：** 哪个路线最有客户、哪个最赚钱、哪个工具已经实现了专有软件格式完全兼容。

对同一份公开资料，给出三种**明确标为假设**的评分偏好：

| 假设目标 | FMI/SSP | STEP/CAD | Open EDA | 排名前列 |
|---|---:|---:|---:|---|
| 不带画像的通用权重 | 3.90 | 3.30 | 3.60 | FMI（仅临时） |
| 侧重 PDE 数值软件、8 周原型 | 4.30 | 2.70 | 2.70 | FMI |
| 具备 EDA 工程经验和芯片用户 | 2.55 | 2.25 | 4.30 | EDA |

**这些分数是人为设定的情景分析，不是市场事实或实测性能。** 可以直接修改 JSON 权重重新计算：

```bash
python demos/03-decision/evidence/score_options.py --scenario all
```

**MARIS 的核心介入：** 在 Agent 准备推荐时，设置“用户确认 Checkpoint”：究竟服务谁？现有团队拥有什么领域能力？能提供何种合法、可公开验证的测试资产？缺失这些信息不能做不可撤销的资源承诺。[查看人类决策节点](03-decision/checkpoint.md)。

## 一次执行三个 Demo 的本地检查

```bash
python demos/run.py --verify
```

查看对应的参考审查结果：

```bash
python demos/run.py --case coding --mode personalized
python demos/run.py --case research --mode personalized
python demos/run.py --case decision --mode personalized
```

上面这条 `run.py` 是**参考展示回放器，不调用大模型**，不应把打印出的三种参考输出包装为 MARIS 在 Codex 或 Claude Code 的真实运行成绩。想进行真正的 Agent 对照实验，按 [统一实验协议](EVALUATION.md) 在相同模型、相同输入和权限下运行并保留原始记录。

## 用户历史数据怎么处理？

三份演示画像均为**虚构的明示样例**，没有读取或推断真实用户的历史对话。正式使用的画像必须由用户指定历史来源、允许模型处理、先查看候选画像、明确批准后保存；随时可以关闭或删除。详见 [画像工作流](PROFILE_WORKFLOW.md) 和 [隐私说明](../docs/PRIVACY.md)。
