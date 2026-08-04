# spectitle 模块

系统菜单管理。禁用或恢复窗口的系统菜单和标题栏交互。

## API

### qmDisableSystemMenu

```c
QM_EXPORT QM_Real qmDisableSystemMenu(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 目标窗口句柄（字符串形式）

**返回值：**
- 非零 - 成功
- `0` - 无效窗口句柄

**说明：**
- 禁用以下系统菜单操作：
  - `Alt+Space` 打开系统菜单
  - `Alt+Enter` 打开系统菜单
  - 鼠标右键标题栏菜单
  - 中键标题栏菜单
  - 标题栏左键点击
  - 标题栏左键双击
  - 右键上下文菜单
- 使用 `SetWindowSubclass` 实现子类化

---

### qmRestoreSystemMenu

```c
QM_EXPORT QM_Real qmRestoreSystemMenu(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 目标窗口句柄（字符串形式）

**返回值：**
- 非零 - 成功
- `0` - 无效窗口句柄

**说明：**
- 恢复窗口的系统菜单功能
- 移除子类化处理

## 使用示例

```c
// 禁用系统菜单
qmDisableSystemMenu(hwndStr);

// ... 游戏运行中 ...

// 恢复系统菜单
qmRestoreSystemMenu(hwndStr);
```
