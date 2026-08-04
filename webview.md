# webview 模块

WebView2 浏览器嵌入模块。在游戏窗口中嵌入 Chromium 浏览器控件。

## 前置要求

- WebView2Loader.dll（位于游戏目录或系统 PATH）
- Microsoft Edge WebView2 Runtime

## API

### 初始化

#### qmWebViewInit

```c
QM_EXPORT QM_Real qmWebViewInit(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 主窗口句柄（字符串形式）

**返回值：**
- `0` - 成功
- `1` - 无效窗口句柄
- `2` - WebView2Loader.dll 加载失败
- `3` - COM 初始化失败
- `4` - 内存分配失败
- `5` - WebView2 环境创建失败

---

### 创建/销毁

#### qmWebViewCreate

```c
QM_EXPORT QM_Real qmWebViewCreate(QM_Real x, QM_Real y, QM_Real w, QM_Real h);
```

**参数：**
- `x, y` - 窗口位置
- `w, h` - 窗口大小

**返回值：** WebView ID（1-16），0 表示失败

---

#### qmWebViewCreateChild

```c
QM_EXPORT QM_Real qmWebViewCreateChild(QM_Real x, QM_Real y, QM_Real w, QM_Real h);
```

**说明：** 创建子窗口 WebView，自动调整父窗口大小

---

#### qmWebViewDestroy

```c
QM_EXPORT QM_Real qmWebViewDestroy(QM_Real webviewId);
```

---

#### qmWebViewDestroyAll

```c
QM_EXPORT QM_Real qmWebViewDestroyAll();
```

### 导航

#### qmWebViewNavigate

```c
QM_EXPORT QM_Real qmWebViewNavigate(QM_Real webviewId, QM_String url);
```

---

#### qmWebViewNavigateToString

```c
QM_EXPORT QM_Real qmWebViewNavigateToString(QM_Real webviewId, QM_String html);
```

**说明：** 直接加载 HTML 字符串

---

#### qmWebViewExecuteScript

```c
QM_EXPORT QM_Real qmWebViewExecuteScript(QM_Real webviewId, QM_String script);
```

**说明：** 执行 JavaScript 脚本

### 显示控制

| 函数 | 说明 |
|------|------|
| `qmWebViewShow(webviewId)` | 显示 WebView |
| `qmWebViewHide(webviewId)` | 隐藏 WebView |

### 位置和大小

| 函数 | 说明 |
|------|------|
| `qmWebViewSetPosition(webviewId, x, y)` | 设置位置 |
| `qmWebViewSetSize(webviewId, w, h)` | 设置大小 |
| `qmWebViewSetRegion(webviewId, x, y, w, h)` | 同时设置位置和大小 |
| `qmWebViewResizeToParent(webviewId)` | 调整为父窗口大小 |

### 外观设置

| 函数 | 参数 | 说明 |
|------|------|------|
| `qmWebViewSetOpacity` | opacity(0-255) | 设置透明度 |
| `qmWebViewSetTopmost` | topmost(0/1) | 设置置顶 |
| `qmWebViewSetTitle` | title | 设置标题 |
| `qmMWebViewSetTitleBar` | hasTitleBar(0/1) | 设置标题栏 |
| `qmWebViewSetDraggable` | draggable(0/1) | 设置可拖拽 |

### 关闭控制

| 函数 | 说明 |
|------|------|
| `qmWebViewSetClosable(webviewId, closable)` | 设置是否可关闭 |
| `qmWebViewSetCloseTriggersMain(webviewId, triggers)` | 关闭时是否关闭主窗口 |

### WebView2 设置

| 函数 | 说明 |
|------|------|
| `qmWebViewSetDevToolsEnabled(webviewId, enabled)` | 启用/禁用开发者工具 |
| `qmWebViewSetScriptEnabled(webviewId, enabled)` | 启用/禁用脚本 |
| `qmWebViewSetDefaultContextMenusEnabled(webviewId, enabled)` | 启用/禁用右键菜单 |
| `qmWebViewSetStatusBarEnabled(webviewId, enabled)` | 启用/禁用状态栏 |
| `qmWebViewSetZoomFactor(webviewId, zoomFactor)` | 设置缩放比例 |

### 导航控制

| 函数 | 说明 |
|------|------|
| `qmWebViewReload(webviewId)` | 刷新页面 |
| `qmWebViewStop(webviewId)` | 停止加载 |
| `qmWebViewGoBack(webviewId)` | 后退 |
| `qmWebViewGoForward(webviewId)` | 前进 |

### 状态查询

| 函数 | 返回值 | 说明 |
|------|--------|------|
| `qmWebViewGetIsActive(webviewId)` | 0/1 | 是否就绪 |
| `qmWebViewGetCount()` | 数量 | 活跃 WebView 数量 |
| `qmWebViewExists(webviewId)` | 0/1 | 是否存在 |
| `qmWebViewIsChild(webviewId)` | 0/1 | 是否为子窗口 |

#### qmWebViewGetInfo

```c
QM_EXPORT QM_Real qmWebViewGetInfo(QM_Real webviewId, QM_Real infoType);
```

**infoType：**
- `0` - X 坐标
- `1` - Y 坐标
- `2` - 宽度
- `3` - 高度
- `4` - 是否就绪
- `5` - 是否为子窗口

---

### 清理

#### qmWebViewCleanup

```c
QM_EXPORT QM_Real qmWebViewCleanup();
```

**说明：** 销毁所有 WebView 并释放资源

## 使用示例

```c
// 初始化
qmWebViewInit(parentHwndStr);

// 创建 WebView
int id = qmWebViewCreate(100, 100, 800, 600);

// 导航到网页
qmWebViewNavigate(id, "https://example.com");

// 执行 JavaScript
qmWebViewExecuteScript(id, "document.title = 'Hello'");

// 显示
qmWebViewShow(id);
```
