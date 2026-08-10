# keeplive 模块

系统保活：持续唤醒系统，防止游戏运行期间进入休眠、锁屏或黑屏。

共 3 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_keeplive_cleanup](qiumingdll_keeplive_cleanup.md) | 卸载窗口保活的消息钩子，停止对目标窗口的保活保护，并清空内部记录的目标窗口状态。 |
| [qiumingdll_keeplive_init](qiumingdll_keeplive_init.md) | 安装"窗口保活"消息钩子，防止目标窗口被系统判定为"无响应"而被关闭或清理，用于网页版游戏的全屏/无响应保护。 |
| [qiumingdll_keeplive_is_active](qiumingdll_keeplive_is_active.md) | 查询窗口保活钩子当前是否已安装，返回 1 表示保活生效中、0 表示未安装。 |

[返回文档首页](../README.md)