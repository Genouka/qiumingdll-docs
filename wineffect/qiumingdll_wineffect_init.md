# qiumingdll_wineffect_init()

绑定游戏窗口，准备窗口特效。只记录目标窗口，不启动任何效果。

## 函数签名

```gml
qiumingdll_wineffect_init()
```

> 窗口句柄由包装层自动传入 `window_handle()`，无需显式提供。

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 绑定成功 |
| 0 | 失败：窗口句柄无效（或非 Windows 平台） |

## 使用说明

- 前置条件：先调用 `qiumingdll_init()`，并在游戏窗口已创建后调用。
- 本函数只做绑定；还需要调用 `qiumingdll_wineffect_set_enabled(1)` 才会开始运行。
- 若已经启用特效时用另一个窗口再次调用本函数，会先停止并还原旧窗口，然后绑定新窗口；新窗口需要重新调用 `set_enabled(1)`。
- 重复绑定同一个窗口是安全的，正在运行的特效不会中断。
- 模块不修改窗口样式、不创建后台线程；动画由窗口自身的 `WM_TIMER` 驱动。

## 示例

```gml
/// Create 事件
qiumingdll_init();
qiumingdll_wineffect_init();
```

## 相关函数

- [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md)
- [qiumingdll_wineffect_cleanup](qiumingdll_wineffect_cleanup.md)
