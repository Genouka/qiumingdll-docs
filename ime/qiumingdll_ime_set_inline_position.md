# qiumingdll_ime_set_inline_position(x, y)

把 IME 组合窗口与候选窗口内联到游戏窗口客户区的指定位置，并启用内联模式。

## 函数签名

```gml
qiumingdll_ime_set_inline_position(x, y)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| x | Real | 是 | 内联位置在游戏窗口客户区中的 X 像素坐标（取整使用） |
| y | Real | 是 | 内联位置在游戏窗口客户区中的 Y 像素坐标（取整使用） |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：已设置内联位置并启用内联模式 |
| 1 | 无目标窗口：找不到有效窗口。非 Windows 平台始终返回此值 |
| 2 | 无 IME 上下文：窗口有效，但无法取得 IME 上下文 |

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 1。
- 前置条件：建议先调用 `qiumingdll_ime_fix_conflict` 记录目标窗口；若未调用，本函数会自动查找前台窗口并使用它。
- 功能：启用"内联输入法"模式——系统的组合窗口和候选窗口被隐藏（不再由系统绘制），其位置被固定在你指定的客户区坐标处；同时底层会挂接窗口消息处理，把组合文本、提交文本、候选列表等信息记录到内部状态中，供状态轮询 API（`qiumingdll_ime_get_state`、`qiumingdll_ime_poll` 等）读取。
- 组合框与候选框的相对位置：二者都由底层在指定坐标附近布置（候选窗口显示在组合位置下方约 20 像素处），游戏无需关心具体像素偏移。
- 坐标体系：x/y 是游戏窗口**客户区**坐标（不是屏幕坐标，也不是房间坐标）。游戏窗口移动或缩放后，需要重新调用本函数更新位置。
- 典型用法：每帧（Step 事件）调用一次，把位置跟随到当前输入光标/文本末尾，让组合窗口"贴"在输入位置。
- 每次调用都会更新内部记录的位置；组合过程中底部也会用最近一次设置的位置重新定位。
- 对应取消操作：调用 `qiumingdll_ime_reset_inline` 恢复系统默认行为。

## 示例

```gml
// Step 事件：把系统组合窗口跟随到文本末尾
var posX = input_x + 6 + string_width(text);
qiumingdll_ime_set_inline_position(posX, input_y + 4);
```

```gml
// 简单场景：固定在屏幕中央
qiumingdll_ime_set_inline_position(room_width / 2, room_height / 2);
```

## 相关函数

- [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)