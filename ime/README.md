# ime 模块

输入法集成：合成文本、候选词、内嵌编辑与轮询；需在绘制事件中调用输入绘制函数以显示候选区。

共 23 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md) | 修复输入法冲突：把系统 IME 组合窗口移动到不可见位置，防止输入法候选框遮挡游戏画面。 |
| [qiumingdll_ime_get_candidate](qiumingdll_ime_get_candidate.md) | 获取指定索引的候选词文本。 |
| [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md) | 获取当前候选列表中的候选词数量。 |
| [qiumingdll_ime_get_candidate_selection](qiumingdll_ime_get_candidate_selection.md) | 获取当前候选列表中选中的候选索引。 |
| [qiumingdll_ime_get_commit](qiumingdll_ime_get_commit.md) | 简化版提交文本获取：内部自动检查状态位 0x02，有提交则返回提交文本，否则返回空字符串。 |
| [qiumingdll_ime_get_commit_text](qiumingdll_ime_get_commit_text.md) | 获取本次输入确认上屏的提交文本，读取后该文本会被清空。 |
| [qiumingdll_ime_get_composition_cursor](qiumingdll_ime_get_composition_cursor.md) | 获取组合文本中光标的位置（字符偏移，从 0 开始）。 |
| [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md) | 获取当前输入法的组合文本（拼音/笔画等尚未确认上屏的字符串）。 |
| [qiumingdll_ime_get_mode](qiumingdll_ime_get_mode.md) | 获取当前输入法的输入模式（英文/中文）。 |
| [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md) | 返回 IME 状态变化标志（位掩码），用于判断接下来该读取哪些数据。 |
| [qiumingdll_ime_input_cleanup](qiumingdll_ime_input_cleanup.md) | 清理输入框资源：销毁候选列表 ds_list，DLL 模式下取消内联模式。 |
| [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md) | 创建"IME 输入框"一站式解决方案：初始化输入框并创建全部 `ime_` 前缀实例变量。 |
| [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md) | 绘制完整的 IME 输入框：背景 + 边框 + 已确认文本 + 组合文本 + 下划线 + 光标 + 候选框。 |
| [qiumingdll_ime_input_draw_candidates](qiumingdll_ime_input_draw_candidates.md) | 仅绘制候选列表（候选框背景 + 边框 + 候选项 + 选中高亮），可指定绘制位置。 |
| [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md) | 仅绘制输入框的文本部分（已确认文本 + 组合文本 + 下划线 + 光标），不绘制背景与候选列表，适用于自定义渲染。 |
| [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md) | 在 Step 事件中轮询 IME 状态并更新输入框内部数据（文本、组合、候选、回调）。 |
| [qiumingdll_ime_is_composing](qiumingdll_ime_is_composing.md) | 查询是否正在组合输入。 |
| [qiumingdll_ime_poll](qiumingdll_ime_poll.md) | 一次性轮询所有 IME 状态，解析为 GML 的 ds_map 并返回。 |
| [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md) | 销毁 `qiumingdll_ime_poll()` 返回的 ds_map，并同时销毁其中的候选列表 ds_list。 |
| [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md) | 一次性轮询所有 IME 状态并返回 JSON 字符串。 |
| [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md) | 取消内联模式，恢复系统输入法窗口的默认行为，并清空全部 IME 状态。 |
| [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md) | 把 IME 组合窗口与候选窗口内联到游戏窗口客户区的指定位置，并启用内联模式。 |
| [qiumingdll_ime_switch](qiumingdll_ime_switch.md) | 切换当前输入法：切换到英文/中文模式，或在系统已安装的输入法之间切换。 |

[返回文档首页](../README.md)