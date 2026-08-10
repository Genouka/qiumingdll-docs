# qiumingdll_fixflash()

修复游戏窗口的闪烁问题：将窗口类的背景画刷置空，消除窗口重绘时的闪烁。

## 函数签名

```gml
qiumingdll_fixflash()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数。内部自动获取当前游戏窗口句柄（`window_handle()`），无需也无法手动指定窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 修复成功（窗口句柄有效，背景画刷已置空） |
| 1 | 无效窗口：获取到的窗口句柄不是有效窗口，未做任何修改 |
| （无返回值） | 非 Windows 平台调用时无操作、无返回值 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台无效果。
- 行为细节：内部将游戏窗口所属窗口类的背景画刷（`GCLP_HBRBACKGROUND`）置空，使 Windows 不再先绘制灰色背景再绘制游戏画面，从而消除切换窗口、调整大小等场景下的闪烁。
- 注意：该修改作用于整个窗口类，效果在游戏运行期间持续有效；由于 GameMaker 窗口通常有且仅有一个实例，一般无需恢复。
- 建议在游戏窗口创建完成之后（如 `game_start` 事件）调用一次即可，频繁重复调用无额外收益。
- 与其他系统函数互不冲突，可配合 `qiumingdll_disable_system_menu()` 等一起使用。

## 示例

```gml
// 游戏启动时修复窗口闪烁
qiumingdll_init();

var r = qiumingdll_fixflash();
if (r == 0)
{
    show_debug_message("窗口闪烁修复成功");
}
else
{
    show_debug_message("修复失败：无效窗口（返回 1）");
}
```

## 相关函数

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_disable_system_menu](qiumingdll_disable_system_menu.md)
- [qiumingdll_restore_system_menu](qiumingdll_restore_system_menu.md)