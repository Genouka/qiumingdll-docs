# specmessage 模块

自定义错误对话框。提供可复制、可清除的错误信息显示窗口。

## API

### qmShowError

```c
QM_EXPORT QM_Real qmShowError(QM_String hwndParam, QM_String message);
```

**参数：**
- `hwndParam` - 父窗口句柄（字符串形式），可为空
- `message` - 错误信息文本（UTF-8 编码）

**返回值：**
- `IDABORT` (3) - 用户点击"Abort"按钮
- `IDIGNORE` (5) - 用户点击"Ignore"按钮
- `IDCANCEL` (2) - 用户关闭窗口或点击关闭按钮

**说明：**
- 创建 800x600 的模态错误对话框
- 显示只读的多行文本框（支持自动换行）
- 提供四个按钮：
  - **Abort** - 终止程序（调用 `exit(1)`）
  - **Ignore** - 忽略错误继续执行
  - **Copy** - 复制错误信息到剪贴板
  - **Clear** - 清除文本框内容
- 自动居中显示在父窗口或屏幕中央
- 禁用父窗口直到对话框关闭

**使用示例：**
```c
int result = qmShowError(parentHwnd, "发生了一个错误：\n文件未找到");
if (result == IDABORT) {
    // 处理终止
}
```
