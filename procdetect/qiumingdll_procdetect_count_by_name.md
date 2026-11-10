# qiumingdll_procdetect_count_by_name(processName)

按可执行文件名统计当前系统中同名进程的数量（大小写不敏感，匹配完整 `.exe` 名称）。

## 函数签名

```gml
qiumingdll_procdetect_count_by_name(processName)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| processName | String | 是 | 要统计的可执行文件名。按完整 exe 文件名精确匹配，建议传完整格式如 `"notepad.exe"`、`"chrome.exe"`。大小写不敏感。传入空字符串时视为参数为空 |

## 返回值

| 值 | 说明 |
|----|------|
| ≥ 0 | 系统中匹配到的同名进程数量（含正在运行的全部实例） |
| -1 | 参数为空（空字符串或未传参） |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 0（非 Windows 不会进入统计分支，但 GML 包装在非 Windows 下默认返回 -1）。
- 行为细节：内部遍历系统进程快照，将每个进程的可执行文件名与 `processName` 做大小写不敏感的完全匹配，累计命中个数。
- 匹配规则：与 `qiumingdll_procdetect_process()` 一致，默认按**完整文件名（含 `.exe` 扩展名）**匹配；不带扩展名通常匹配不上。
- 异步模式：默认从后台缓存读取，数量变化最长有约 0.5 秒延迟；可安全放入 Step 事件每帧调用，不会卡顿。
- 典型用途：统计某个程序开了几个实例、配合阈值判断是否超出预期并发。
- 与 `qiumingdll_procdetect_multiinstance()` 的区别：本函数可统计**任意指定名称**的进程数量；后者仅统计**自身**同名实例数，且不接受参数。
- 检测为快照式，进程在检测后被启动/结束不会影响本次结果；需实时监控时请轮询调用。

## 示例

```gml
qiumingdll_init();

// 统计系统中运行了多少个记事本
var n = qiumingdll_procdetect_count_by_name("notepad.exe");
if (n > 0)
{
    show_debug_message("发现 " + string(n) + " 个记事本进程");
}
else if (n == 0)
{
    show_debug_message("没有记事本在运行");
}
else // n == -1
{
    show_debug_message("进程名参数为空");
}
```

## 相关函数

- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_get_commandline](qiumingdll_procdetect_get_commandline.md)
- [qiumingdll_init](qiumingdll_init.md)
