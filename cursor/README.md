# cursor 模块

全局光标反向：开启后系统光标与鼠标的物理移动方向相反（例如鼠标向右移动，光标向左移动）。适合整蛊、恶作剧关卡、隐藏彩蛋等场景。

- 实现方式：`WH_MOUSE_LL` 全局低级鼠标钩子 + `SetCursorPos` 反向改写光标位置；光标到达屏幕边缘时会环绕到另一侧继续反向移动，不会卡死。
- 取消方式：`qmCursorSetInvert(0)`、效果生效期间 1.5 秒内连按 **8 次 F12**（全局热键，无需游戏获得焦点）、或 DLL 被卸载 / 游戏退出时自动还原。
- 还原行为：关闭效果时会把光标放回开启前的位置，并立即恢复正常鼠标移动，不残留任何系统级修改。

共 2 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_cursor_set_invert](qiumingdll_cursor_set_invert.md) | 开启 / 关闭"光标与鼠标移动相反"效果。 |
| [qiumingdll_cursor_get_invert](qiumingdll_cursor_get_invert.md) | 查询当前是否处于光标反向状态。 |


[返回文档首页](../README.md)
