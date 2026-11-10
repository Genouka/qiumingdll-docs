# qiumingdll_procdetect_get_commandline(processName)

按可执行文件名获取所有匹配进程的命令行，返回 JSON 数组。

## 函数签名

```gml
qiumingdll_procdetect_get_commandline(processName)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| processName | String | 是 | 要查询的可执行文件名。按完整 exe 文件名精确匹配，大小写不敏感。传入空字符串时视为参数为空 |

## 返回值

返回 JSON 字符串数组，每个元素为 `{ "pid": 进程ID, "cmdline": "命令行字符串" }`：

| 情况 | 返回值 |
|------|--------|
| 匹配到进程 | `[{"pid":1234,"cmdline":"C:\\game\\game.exe -fullscreen"}, ...]` |
| 未匹配到 | `[]` |
| 参数为空 | `[]` |

命令行中的 `"`、`\`、换行、回车、制表符会被自动转义为 JSON 合法字符。

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 异步模式：PID 列表来自后台缓存（最长约 0.5 秒延迟），命令行内容仍为调用时实时读取；PID 对应的进程可能已退出，此时对应元素的 `cmdline` 为空字符串。
- 平台限制：仅 Windows 生效；内部通过 `NtQueryInformationProcess(ProcessCommandLineInformation)` 读取。需要对该进程有 `PROCESS_QUERY_INFORMATION`（或 `PROCESS_QUERY_LIMITED_INFORMATION`）权限，普通用户进程通常可读自身及多数进程，部分受保护进程可能读取失败（对应元素被跳过）。
- 行为细节：先收集所有匹配 `processName` 的 PID，逐个读取其完整命令行，再以 JSON 数组形式返回。
- 典型用途：判断某进程是否以特定参数启动（如是否带调试参数）、反多开时区分真实实例与同名包装进程。
- 解析返回的 JSON 可使用 `qiumingdll_json5_decode()`（本扩展内置 JSON5 解析）。
- 检测为快照式，进程在检测后被启动/结束不会影响本次结果。

## 示例

```gml
qiumingdll_init();

var json = qiumingdll_procdetect_get_commandline("game.exe");
var arr = qiumingdll_json5_decode(json);
if (is_array(arr))
{
    for (var i = 0; i < array_length(arr); i++)
    {
        var item = arr[i];
        show_debug_message("PID=" + string(item[? "pid"]) + " CMD=" + string(item[? "cmdline"]));
    }
}
```

## 相关函数

- [qiumingdll_procdetect_count_by_name](qiumingdll_procdetect_count_by_name.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_json5_decode](../json5/qiumingdll_json5_decode.md)
- [qiumingdll_init](qiumingdll_init.md)
