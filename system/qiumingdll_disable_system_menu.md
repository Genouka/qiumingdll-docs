# qiumingdll_disable_system_menu()

禁用游戏窗口的系统菜单及窗口操作，防止玩家通过系统菜单干扰游戏。

## 函数签名

```gml
qiumingdll_disable_system_menu()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数。内部自动获取当前游戏窗口句柄（`window_handle()`） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 禁用成功（窗口句柄有效，已挂接拦截子类） |
| 0 | 无效窗口：获取到的窗口句柄不是有效窗口 |
| （无返回值） | 非 Windows 平台调用时无操作、无返回值 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台无效果。
- 行为细节：内部对游戏窗口挂接窗口子类，拦截并吞掉一系列系统操作，包括：
  - `Alt+Space` 弹出窗口系统菜单、回车触发系统菜单；
  - 标题栏右键弹出的系统菜单；
  - 任务栏右键菜单（SC_TASKLIST）；
  - 鼠标拖动标题栏移动窗口；
  - 双击标题栏最大化 / 还原；
  - 非客户区（标题栏、边框）的右键/中键菜单。
  窗口本身并未被修改为无边框，只是这些系统交互被屏蔽。
- 与 `qiumingdll_restore_system_menu()` 成对使用：调用恢复函数后，上述系统交互全部还原。
- 注意：该效果作用于当前游戏窗口，窗口销毁后子类自动移除，无需手动清理。
- 建议配合 `qiumingdll_fixflash()` 在启动时一并设置，打造"干净"的游戏窗口体验。

## 示例

```gml
// 全屏模式游戏启动后锁定窗口，禁止玩家拖拽/弹出系统菜单
qiumingdll_init();
qiumingdll_fixflash();

var r = qiumingdll_disable_system_menu();
if (r == 1)
{
    show_debug_message("系统菜单已禁用");
}
```

## 相关函数

- [qiumingdll_restore_system_menu](qiumingdll_restore_system_menu.md)
- [qiumingdll_fixflash](qiumingdll_fixflash.md)
- [qiumingdll_init](qiumingdll_init.md)