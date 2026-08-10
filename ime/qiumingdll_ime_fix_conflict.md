# qiumingdll_ime_fix_conflict()

修复输入法冲突：把系统 IME 组合窗口移动到不可见位置，防止输入法候选框遮挡游戏画面。

## 函数签名

```gml
qiumingdll_ime_fix_conflict()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数。窗口句柄由包装层自动获取（Windows 上会自动传入当前游戏窗口的句柄） |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：组合窗口已被移到不可见位置，且内部记录了目标窗口，供后续 IME 函数使用 |
| 1 | 无效窗口：无法取得有效的游戏窗口句柄。非 Windows 平台始终返回此值 |
| 2 | 无法获取 IME 上下文：窗口有效，但无法取得（或创建）该窗口的 IME 上下文 |

## 使用说明

- 平台限制：仅 Windows 有效；macOS、Linux、HTML5、UWP 等其他平台始终返回 1。
- 功能：修复"输入法冲突"。中文输入法（如微软拼音、搜狗输入法等）在输入时弹出的候选框/组合窗口会遮挡游戏画面，调用本函数后系统组合窗口被设置到不可见位置，画面不再被遮挡。
- 行为细节：成功后内部保存当前窗口句柄，后续 `qiumingdll_ime_switch`、`qiumingdll_ime_get_mode`、`qiumingdll_ime_set_inline_position` 等函数会优先操作该窗口（找不到已记录窗口时才回退到前台窗口）。
- 建议在游戏启动时调用一次即可；进入需要中文输入的场景时也可再次调用。
- 本函数只隐藏系统的组合窗口，并不启用内联模式；若需要在游戏内自行绘制候选框，请配合 `qiumingdll_ime_set_inline_position` 使用。
- 无需初始化即可调用；但如果 DLL 扩展尚未初始化（包装层找不到外部函数），将直接返回 1。
- 非 Windows 平台调用无副作用，可在跨平台代码中直接调用而不需要平台判断。

## 示例

```gml
// 游戏启动时调用一次，消除输入法候选框遮挡
if (os_type == os_windows) {
    var result = qiumingdll_ime_fix_conflict();
    if (result == 0) {
        show_debug_message("输入法冲突修复成功");
    } else {
        show_debug_message("输入法冲突修复失败: " + string(result));
    }
}
```

## 相关函数

- [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md)
- [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md)
- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)