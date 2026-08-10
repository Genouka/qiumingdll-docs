# qiumingdll_restore_system_menu()

恢复游戏窗口的系统菜单及窗口操作，撤销之前 `qiumingdll_disable_system_menu()` 的拦截效果。

## 函数签名

```gml
qiumingdll_restore_system_menu()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数。内部自动获取当前游戏窗口句柄（`window_handle()`） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 恢复成功（窗口句柄有效，拦截子类已移除） |
| 0 | 无效窗口，或当前并没有挂接过拦截子类 |
| （无返回值） | 非 Windows 平台调用时无操作、无返回值 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台无效果。
- 行为细节：内部从游戏窗口移除 `qiumingdll_disable_system_menu()` 所挂接的窗口子类，此后以下操作全部还原：
  - `Alt+Space` 弹出系统菜单、回车触发系统菜单；
  - 标题栏右键、任务栏右键菜单；
  - 鼠标拖动标题栏移动窗口；
  - 双击标题栏最大化 / 还原；
  - 非客户区的右键/中键菜单。
- 在尚未调用过 `qiumingdll_disable_system_menu()` 的情况下调用本函数，属于安全无操作：返回值 0，不产生任何影响。
- 适用场景：游戏在锁窗口与允许拖拽两种模式间切换（例如设置界面里提供"锁定窗口"开关）。
- 注意：游戏窗口被销毁时拦截自动失效，无需也不应再调用本函数。

## 示例

```gml
// 设置界面中的"锁定窗口"开关
qiumingdll_init();

window_locked = false;

if (keyboard_check_pressed(vk_f9))
{
    if (window_locked)
    {
        // 解锁：恢复系统菜单与窗口操作
        qiumingdll_restore_system_menu();
        window_locked = false;
    }
    else
    {
        // 加锁：禁用系统菜单与窗口操作
        qiumingdll_disable_system_menu();
        window_locked = true;
    }
}
```

## 相关函数

- [qiumingdll_disable_system_menu](qiumingdll_disable_system_menu.md)
- [qiumingdll_init](qiumingdll_init.md)