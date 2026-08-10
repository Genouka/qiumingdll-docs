# qiumingdll_execute_program_async(path)

异步启动外部程序或命令行，立即返回，不等待其结束。

## 函数签名

```gml
qiumingdll_execute_program_async(path)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| path | String | 是 | 要执行的程序路径或完整命令行。可为可执行文件的完整路径（如 `C:\tools\app.exe`），也可附带参数（如 `C:\tools\app.exe --flag`）；传入 `%PATH%` 中存在的命令名也可以 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 启动成功（子进程已创建） |
| 0 | 启动失败（路径无效、文件不存在等），或非 Windows 平台调用 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 0。
- 行为细节：内部通过 `CreateProcess` 创建子进程后立即返回，不等待子进程结束，游戏继续正常运行。
- 与 `qiumingdll_execute_program()` 的区别：本函数只负责"启动"，不关心启动后子进程的退出码，适用于打开外部关联程序、启动服务器进程、拉起工具窗口等无需等待结果的场景。
- 注意：返回值仅表示"进程是否成功创建"，不代表子进程后续是否正常运行或崩溃——例如程序启动后又立即报错退出，本函数依然返回 1。
- 路径含空格时建议整体加引号写入参数，例如 `"C:\Program Files\Tool\tool.exe" --listen`。
- 连续异步启动多个程序互不阻塞，适合批量拉起外部进程。

## 示例

```gml
// 异步拉起外部工具，游戏无需等待
qiumingdll_init();

// 打开背景音乐播放器
var ok = qiumingdll_execute_program_async("C:\\music\\player.exe D:\\songs\\bgm.mp3");
if (ok == 1)
{
    show_debug_message("播放器已启动");
}
else
{
    show_debug_message("播放器启动失败");
}

// 批量启动两个服务进程，互不阻塞
qiumingdll_execute_program_async("C:\\server\\web_server.exe");
qiumingdll_execute_program_async("C:\\server\\db_server.exe");
```

## 相关函数

- [qiumingdll_execute_program](qiumingdll_execute_program.md)
- [qiumingdll_init](qiumingdll_init.md)