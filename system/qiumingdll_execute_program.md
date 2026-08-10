# qiumingdll_execute_program(path)

同步执行外部程序或命令行，等待其运行结束后返回退出码。

## 函数签名

```gml
qiumingdll_execute_program(path)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| path | String | 是 | 要执行的程序路径或完整命令行。可为可执行文件的完整路径（如 `C:\tools\app.exe`），也可附带参数（如 `C:\tools\app.exe /silent`）；传入 `%PATH%` 中存在的命令名（如 `notepad.exe`）也可以 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 子进程正常退出且退出码为 0（成功） |
| 非 0 整数 | 子进程的退出码：退出码为负数或非 0 的整数通常表示失败或被外部终止 |
| -1 | 启动失败（路径无效、文件不存在、权限不足等），或非 Windows 平台调用 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 -1。
- 行为细节：内部通过 `CreateProcess` 创建子进程并等待其完全结束（无限等待），随后返回子进程退出码。
- 重要警告：本函数是**同步阻塞**的——调用期间游戏完全冻结，直到子进程退出。切勿用来启动玩家交互类程序（记事本、浏览器等），否则游戏会在玩家关掉程序之前一直卡住。
- 适用场景：静默调用命令行工具（如自动化脚本、压缩工具、截图工具）时使用；需要并发执行时请改用 `qiumingdll_execute_program_async()`。
- 路径含空格时建议整体加引号写入参数，例如 `"C:\Program Files\Tool\tool.exe" --work`。
- 返回的退出码即程序自身的返回值：0 表示成功，非 0 依程序而定，可据此判断执行结果。

## 示例

```gml
// 用记事本静默等待退出是不推荐的用法（会卡住游戏），以下为建议的场景：
// 调用一个自动化工具等待其完成，并根据退出码判断结果
qiumingdll_init();

var exitCode = qiumingdll_execute_program("C:\\tools\\patch_apply.exe -p game");

if (exitCode == 0)
{
    show_debug_message("补丁应用成功");
}
else
{
    qiumingdll_show_error("补丁应用失败，退出码: " + string(exitCode));
}
```

## 相关函数

- [qiumingdll_execute_program_async](qiumingdll_execute_program_async.md)
- [qiumingdll_show_error](qiumingdll_show_error.md)
- [qiumingdll_init](qiumingdll_init.md)