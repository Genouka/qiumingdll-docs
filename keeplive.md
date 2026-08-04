# keeplive 模块

窗口保活功能。通过安装 Windows 钩子防止目标窗口被关闭。

## API

### qmKeepAliveInit

```c
QM_EXPORT QM_Real qmKeepAliveInit(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 目标窗口句柄（字符串形式）

**返回值：**
- `0` - 成功
- `1` - 无效窗口句柄或无法获取线程 ID

**说明：**
- 安装 `WH_GETMESSAGE` 钩子拦截窗口消息
- 安装 `WH_CALLWNDPROC` 钩子处理系统命令
- 拦截 `WM_CLOSE` 消息防止窗口关闭
- 拦截 `WM_SETCURSOR` 显示等待光标

---

### qmKeepAliveCleanup

```c
QM_EXPORT QM_Real qmKeepAliveCleanup();
```

**返回值：**
- `0` - 成功

**说明：**
- 卸载所有已安装的钩子
- 清理保活状态

---

### qmKeepAliveIsActive

```c
QM_EXPORT QM_Real qmKeepAliveIsActive();
```

**返回值：**
- `1.0` - 保活功能处于激活状态
- `0.0` - 保活功能未激活

## 使用流程

```c
// 1. 初始化保活
qmKeepAliveInit(hwndStr);

// 2. 检查状态
if (qmKeepAliveIsActive()) {
    // 保活已激活
}

// 3. 清理
qmKeepAliveCleanup();
```
