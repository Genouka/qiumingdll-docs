# qiumingdll_ime_reset_inline()

取消内联模式，恢复系统输入法窗口的默认行为，并清空全部 IME 状态。

## 函数签名

```gml
qiumingdll_ime_reset_inline()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：内联模式已取消，全部 IME 状态已清空 |
| 1 | 无目标窗口：找不到有效窗口。非 Windows 平台始终返回此值 |

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 1。
- 功能：撤销 `qiumingdll_ime_set_inline_position` 的一切效果：
  - 组合窗口与候选窗口恢复系统默认样式与默认位置（系统可能重新在屏幕下方/光标附近弹出候选框）；
  - 卸载窗口消息处理（不再拦截输入法消息）；
  - 清空全部内部状态：组合文本、组合光标、提交文本、候选列表、选中候选、状态标志等。
- 适用场景：输入框关闭/切换窗口/退出游戏时调用，避免残留内联状态影响其他界面。
- 与 `qiumingdll_ime_fix_conflict` 的区别：本函数恢复系统默认行为（含修复前被隐藏的组合窗口）；若游戏中还需要隐藏系统候选框，请重新调用 `qiumingdll_ime_fix_conflict`。
- ime_input 系列封装中，`qiumingdll_ime_input_cleanup` 在 DLL 模式下会自动调用本函数，无需手动重复调用。

## 示例

```gml
// 输入框关闭时取消内联
if (input_box_closed) {
    qiumingdll_ime_reset_inline();
}
```

```gml
// 切换输入框位置前，先重置再重新内联
qiumingdll_ime_reset_inline();
qiumingdll_ime_set_inline_position(100, 200);
```

## 相关函数

- [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
- [qiumingdll_ime_input_cleanup](qiumingdll_ime_input_cleanup.md)