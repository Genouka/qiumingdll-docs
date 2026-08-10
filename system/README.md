# system 模块

核心函数：初始化与释放（调用任何其他函数前必须先调用 qiumingdll_init）、版本查询、Flash 控件修复、系统菜单控制、错误提示框与外部程序执行。

共 9 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_disable_system_menu](qiumingdll_disable_system_menu.md) | 禁用游戏窗口的系统菜单及窗口操作，防止玩家通过系统菜单干扰游戏。 |
| [qiumingdll_execute_program](qiumingdll_execute_program.md) | 同步执行外部程序或命令行，等待其运行结束后返回退出码。 |
| [qiumingdll_execute_program_async](qiumingdll_execute_program_async.md) | 异步启动外部程序或命令行，立即返回，不等待其结束。 |
| [qiumingdll_fixflash](qiumingdll_fixflash.md) | 修复游戏窗口的闪烁问题：将窗口类的背景画刷置空，消除窗口重绘时的闪烁。 |
| [qiumingdll_free](qiumingdll_free.md) | 释放 qiumingdll 扩展：卸载 DLL 并撤销初始化状态，使其余所有 qiumingdll 函数失效。 |
| [qiumingdll_get_version](qiumingdll_get_version.md) | 获取 qiumingdll 扩展的版本号整数，可用于运行时判断扩展能力。 |
| [qiumingdll_init](qiumingdll_init.md) | 初始化 qiumingdll 扩展：在 Windows 平台加载 DLL 并绑定全部外部函数，是所有其他 qiumingdll 函数可用的前提。 |
| [qiumingdll_restore_system_menu](qiumingdll_restore_system_menu.md) | 恢复游戏窗口的系统菜单及窗口操作，撤销之前 `qiumingdll_disable_system_menu()` 的拦截效果。 |
| [qiumingdll_show_error](qiumingdll_show_error.md) | 弹出带调用栈的阻塞式错误对话框（样式类似 GameMaker 崩溃报告），用于向用户展示错误信息。 |

[返回文档首页](../README.md)