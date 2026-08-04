# fixflash 模块

修复窗口闪烁问题。通过移除窗口背景画刷并发送 `WM_NULL` 消息强制刷新。

## API

### qmFixFlash

```c
QM_EXPORT QM_Real qmFixFlash(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 窗口句柄（以字符串形式传入）

**返回值：**
- `0` - 成功
- `1` - 无效窗口句柄

**说明：**
- 移除窗口背景画刷（`GCLP_HBRBACKGROUND` 设为 NULL）
- 发送 `WM_NULL` 消息触发窗口重绘
- 用于解决某些窗口背景残留或闪烁问题

**使用示例：**
```c
// 传入窗口句柄字符串
qmFixFlash("12345");
```
