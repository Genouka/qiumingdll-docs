# qiumingdll_ime_get_mode()

获取当前输入法的输入模式（英文/中文）。

## 函数签名

```gml
qiumingdll_ime_get_mode()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 英文模式（输入法未启用中文转换） |
| 1 | 中文模式（输入法已启用中文转换） |
| -1 | 获取失败：找不到目标窗口或无法取得 IME 上下文。非 Windows 平台始终返回此值 |

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 -1。
- 本函数是只读查询，不会修改输入法任何状态。
- 目标窗口：优先使用已记录的窗口（由 `qiumingdll_ime_fix_conflict` / `qiumingdll_ime_set_inline_position` 设置），否则使用当前前台窗口。
- 用法：可在每帧轮询用于显示当前模式标签；或配合状态位 0x08（输入模式变化，见 `qiumingdll_ime_get_state`）在模式变化时才读取，避免频繁调用。
- 实际含义：中文模式表示输入法转换状态中包含"原生中文"标志（如中文输入法的中文状态）；英文模式下键盘输入直接输出英文字符。
- 结果可能与系统输入法托盘图标显示一致；若系统没有开启任何中文输入法，通常返回 0。

## 示例

```gml
// 每帧显示当前输入模式
var mode = qiumingdll_ime_get_mode();
if (mode == -1) {
    draw_text(10, 10, "IME: 未知");
} else if (mode == 0) {
    draw_text(10, 10, "IME: EN");
} else {
    draw_text(10, 10, "IME: 中");
}
```

## 相关函数

- [qiumingdll_ime_switch](qiumingdll_ime_switch.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)