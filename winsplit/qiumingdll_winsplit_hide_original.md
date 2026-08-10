# qiumingdll_winsplit_hide_original()

隐藏原游戏窗口（保留分裂窗口继续显示画面），用于"只让分裂窗口显示、主窗口不露脸"的典型窗口分裂用法。

## 函数签名

```gml
qiumingdll_winsplit_hide_original()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数，作用于 init 时记录的游戏主窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（若原窗口不可用或已经处于隐藏状态，也返回 1，无副作用） |
| 0 | 原游戏窗口句柄无效（理论上仅当 init 后主窗口被销毁时发生）；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用。
- 隐藏方式与系统有关：
  - Windows 8 及以上：使用 DWM 窗口遮蔽（Cloak）隐藏，窗口保持原位继续渲染，分裂窗口画面照常更新，性能不受影响；
  - Windows 7：DWM Cloak 不可用，窗口会被移动到屏幕外（-32000,-32000）。
- 隐藏后游戏主窗口视觉上消失，但游戏仍在运行、仍可响应键盘等输入（分裂窗口的鼠标事件也会转发给主窗口）。
- 可重复调用：已隐藏时再调用不会报错，也不会重复记录状态。
- 使用 `qiumingdll_winsplit_show_original()` 恢复原窗口，恢复后位置与隐藏前一致。
- 游戏退出前若忘记恢复，`qiumingdll_winsplit_cleanup()` 会自动恢复原窗口显示。

## 示例

```gml
// 在控制对象的 Step 事件中：按 F9 隐藏原窗口、F10 恢复
if (keyboard_check_pressed(vk_f9))
    qiumingdll_winsplit_hide_original();

if (keyboard_check_pressed(vk_f10))
    qiumingdll_winsplit_show_original();
```

```gml
// 典型用法：创建分裂窗口后立即隐藏原窗口，屏幕上只有分裂画面
if (global.split_1 > 0)
    qiumingdll_winsplit_hide_original();
```

## 相关函数

- [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md)