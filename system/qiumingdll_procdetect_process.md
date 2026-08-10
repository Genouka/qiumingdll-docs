# qiumingdll_procdetect_process(processName)

按指定的可执行文件名检测系统中是否存在对应进程。

## 函数签名

```gml
qiumingdll_procdetect_process(processName)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| processName | String | 是 | 要检测的可执行文件名。按完整 exe 文件名精确匹配，建议传完整格式如 `"notepad.exe"`、`"chrome.exe"`。大小写不敏感（传 `"NOTEPAD.EXE"` 或 `"Notepad.exe"` 均可命中）。传入空字符串时视为参数为空 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 系统中存在该进程 |
| 0 | 系统中不存在该进程，或非 Windows 平台调用 |
| -1 | 参数为空（空字符串或未传参） |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 0。
- 行为细节：内部遍历系统进程快照，将每个进程的可执行文件名与 `processName` 做大小写不敏感的完全匹配，命中即返回 1。
- 匹配规则：默认按**完整文件名（含 `.exe` 扩展名）**匹配，与任务管理器「名称」列显示一致。不带扩展名（如仅传 `"notepad"`）通常匹配不上，建议始终传完整文件名。
- 只检测进程是否存在；若需统计同名进程数量，请使用 `qiumingdll_procdetect_multiinstance()`（针对自身）或按需求轮询本函数。
- 检测为快照式，进程被启动/结束不会影响本次结果；需实时监控时请轮询调用。
- 典型用途：检查前置依赖（如检测游戏启动器是否在运行）、探测外接程序（按键精灵、辅助工具）等。

## 示例

```gml
// 检查记事本是否打开（用于辅助程序联动判断）
qiumingdll_init();

var r = qiumingdll_procdetect_process("notepad.exe");
if (r == 1)
{
    show_debug_message("记事本正在运行");
}
else if (r == 0)
{
    show_debug_message("记事本未运行");
}
else // r == -1
{
    show_debug_message("进程名参数为空，无法检测");
}

// 大小写不敏感：以下写法与上面等价
qiumingdll_procdetect_process("Notepad.EXE");
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_init](qiumingdll_init.md)