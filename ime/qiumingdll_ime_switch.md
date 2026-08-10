# qiumingdll_ime_switch(action)

切换当前输入法：切换到英文/中文模式，或在系统已安装的输入法之间切换。

## 函数签名

```gml
qiumingdll_ime_switch(action)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | Real | 是 | 要执行的动作：0=切换到英文模式；1=切换到中文模式；2=切换到下一个输入法；3=切换到上一个输入法 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：已切换模式或已切换到其他输入法 |
| 1 | 无目标窗口：找不到有效的前台窗口或已记录的窗口。非 Windows 平台始终返回此值 |
| 2 | 无 IME 上下文：窗口有效，但无法取得（或创建）该窗口的 IME 上下文 |
| 3 | 无效 action：传入的 action 不在 0~3 范围内 |

## 使用说明

- 平台限制：仅 Windows 有效；其他平台始终返回 1。
- action 0/1：直接修改输入法的中英文转换状态。action 1（切中文）等价于让输入法进入"中文输入"状态（可能需要已安装中文输入法并处于开启状态）；action 0（切英文）则关闭原生中文转换。
- action 2/3：通过系统键盘布局切换（下一个/上一个输入法）。切换时会释放当前输入法上下文并重新激活键盘布局，属于系统级行为，播放器/游戏窗口本身不受影响。
- 目标窗口：优先使用 `qiumingdll_ime_fix_conflict` 或 `qiumingdll_ime_set_inline_position` 记录的窗口；未记录时使用当前前台窗口。
- 如果用户正在组合输入（正在打字）时切换输入法，可能会中断当前组合；建议在合适时机调用。
- 切换输入法可能触发系统输入法切换提示（如任务栏图标变化），这是系统的正常行为。

## 示例

```gml
// 输入框获得焦点时强制切到中文模式
if (box_focused) {
    if (qiumingdll_ime_get_mode() != 1) {
        qiumingdll_ime_switch(1); // 切到中文
    }
}

// 用户按 Tab 轮换输入法
if (keyboard_check_pressed(vk_tab)) {
    qiumingdll_ime_switch(2); // 下一个输入法
}
```

## 相关函数

- [qiumingdll_ime_get_mode](qiumingdll_ime_get_mode.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)