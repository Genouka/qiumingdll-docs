# qiumingdll_show_error(message)

弹出带调用栈的阻塞式错误对话框（样式类似 GameMaker 崩溃报告），用于向用户展示错误信息。

## 函数签名

```gml
qiumingdll_show_error(message)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| message | String | 是 | 要显示的错误文本。可为多行文本（用 `\r\n` 或 `\n` 换行），将显示在对话框的文本框中 |

## 返回值

| 值 | 说明 |
|----|------|
| 3（IDABORT） | 用户点击了 "Abort" 按钮。注意：此时 DLL 会直接结束整个进程（等同于程序退出），不会返回 |
| 5（IDIGNORE） | 用户点击了 "Ignore" 按钮，关闭对话框，游戏继续运行 |
| 2（IDCANCEL） | 用户直接关闭了对话框（点窗口 X 或按 Esc），等价于忽略 |
| 0 | 对话框创建失败时返回（极少发生） |
| （无返回值） | 非 Windows 平台调用时改用 `show_message_async` 弹窗，无返回值 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：Windows 上弹出原生错误对话框（标题为 "Code Error"，含 Abort / Ignore / Copy / Clear 四个按钮）；非 Windows 平台自动降级为 `show_message_async(message)` 异步弹窗。
- 行为细节：
  - 对话框为阻塞式模态窗口，弹出期间游戏完全暂停，直到用户操作后才继续。
  - 除了 `message` 文本，对话框会自动附带调用栈信息（内部取 `debug_get_callstack` 拼接到文本中），帮助定位错误来源。
  - Abort：立即结束进程（DLL 内部执行进程退出，退出码为 1），适合让玩家在崩溃时迅速关掉游戏。
  - Ignore：关闭对话框并继续执行游戏。
  - Copy：把当前文本复制到剪贴板，方便玩家反馈错误信息。
  - Clear：清空文本框内容（仅影响显示）。
- 注意：务必确认 `message` 不能为 `undefined`，建议用 `string(...)` 包裹非字符串值。
- 适用场景：捕获到脚本异常、存档损坏、配置缺失等需要玩家知晓的情况，作为替代 `show_error` / `show_message` 的展示方式。

## 示例

```gml
// 模拟一段需要提示用户的错误
qiumingdll_init();

var errText = "检测到存档损坏！\r\n无法读取 save.dat";
var choice = qiumingdll_show_error(errText);

// 只有选择 Ignore（返回值 5）或直接关闭对话框（返回值 2）才会执行到这里
// 选择 Abort 时进程已直接结束
if (choice == 5 || choice == 2)
{
    show_debug_message("用户选择忽略错误，尝试恢复默认存档");
    // 继续游戏逻辑……
}
```

## 相关函数

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_fixflash](qiumingdll_fixflash.md)