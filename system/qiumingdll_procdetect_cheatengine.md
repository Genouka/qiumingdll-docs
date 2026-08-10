# qiumingdll_procdetect_cheatengine()

检测系统进程中是否存在常见作弊与调试工具，用于反作弊或提示环境异常。

## 函数签名

```gml
qiumingdll_procdetect_cheatengine()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 检测到至少一个作弊/调试工具进程在运行 |
| 0 | 未检测到任何目标进程，或非 Windows 平台调用 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 0。
- 行为细节：内部遍历系统进程快照，按进程名（大小写不敏感，精确匹配 exe 文件名）逐一比对内置名单，命中任何一个即返回 1。内置名单包括：
  - 内存修改/作弊工具：Cheat Engine（cheatengine.exe、cheat engine.exe、cheatengine-x86_64.exe 等）、ArtMoney（artmoney.exe）、GameConqueror（gameconqueror.exe）、scanmem.exe 等；
  - 调试器/反汇编工具：x64dbg、x32dbg、x96dbg、OllyDbg（ollydbg.exe、ollyice.exe）、WinDbg（windbg.exe）、IDA（ida.exe、ida64.exe、idag.exe、idaq64.exe）、Ghidra（ghidra.exe）等；
  - 系统监控工具：Process Hacker（processhacker.exe）、Process Monitor（procmon.exe、procmon64.exe）、Process Explorer（procexp.exe、procexp64.exe）等。
- 检测方式是"按名单比对进程名"，只对名单内工具的**默认可执行文件名**有效；工具被改名后可能检测不到，同时可能误报（如存在同名文件的其他程序）。
- 注意：本函数不做任何阻止动作，仅返回检测结果；是否需要警告玩家或退出游戏由调用方决定。
- 检测为快照式，进程在检测后被启动/结束不会影响本次结果；需要实时监控时请按帧或按间隔轮询调用。

## 示例

```gml
// 游戏启动时检测作弊工具，发现则提示并退出
qiumingdll_init();

if (qiumingdll_procdetect_cheatengine() == 1)
{
    qiumingdll_show_error("检测到作弊/调试工具在运行，游戏将退出");
    game_end();
}
else
{
    show_debug_message("环境干净，游戏正常运行");
}
```

## 相关函数

- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_init](qiumingdll_init.md)