# qiumingdll_wineffect_cleanup()

解除窗口绑定：停止特效、移除窗口子类和定时器、还原窗口位置/区域，并释放保存的原始区域。

## 函数签名

```gml
qiumingdll_wineffect_cleanup()
```

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 已清理 |

## 使用说明

- 建议在游戏结束/房间清理事件中调用，尤其是换窗口或重载 DLL 之前。
- 清理后窗口保持可用；再次使用需要重新调用 `qiumingdll_wineffect_init()`。
- 重复调用是安全的。
- 如果窗口已经销毁，函数仍会安全返回，不会访问无效句柄。

## 示例

```gml
/// Cleanup 事件
qiumingdll_wineffect_cleanup();
```

## 相关函数

- [qiumingdll_wineffect_init](qiumingdll_wineffect_init.md)
- [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md)
