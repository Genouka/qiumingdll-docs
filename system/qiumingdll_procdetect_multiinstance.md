# qiumingdll_procdetect_multiinstance()

统计当前正在运行的同名进程数量（含本游戏自身），用于反多开检测。

## 函数签名

```gml
qiumingdll_procdetect_multiinstance()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 只有一个本游戏实例在运行（正常单开） |
| 大于 1 的整数 | 正在运行的实例数量（含自己），例如返回 2 表示已有两个游戏窗口，即存在多开 |
| -1 | 获取自身可执行文件路径失败时返回（罕见） |
| 0 | 非 Windows 平台调用时返回 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；其他平台固定返回 0。
- 行为细节：内部先获取本进程可执行文件的完整路径（`GetModuleFileName`），取其文件名（如 `game.exe`），再遍历系统进程快照统计同名进程数量。本进程自身一定在统计之内，因此正常单开时返回 1。
- 注意：统计的是**可执行文件名相同**的进程——如果两份游戏拷贝位于不同目录但 exe 文件同名，也会被计入。
- 典型用途：限制多开（数量大于 1 时提示并退出）、统计在线实例数等。
- 检测为快照式，进程在检测后被启动/结束不会影响本次结果。
- 与 `qiumingdll_procdetect_process()` 不同，本函数不需要也不接受进程名参数，完全基于自身文件名自动判断。

## 示例

```gml
// 启动时禁止多开
qiumingdll_init();

var count = qiumingdll_procdetect_multiinstance();
if (count > 1)
{
    qiumingdll_show_error("检测到游戏已有 " + string(count) + " 个实例在运行，\r\n同一时间只允许运行一个游戏窗口");
    game_end();
}
else
{
    show_debug_message("当前实例数量: " + string(count) + "（正常）");
}
```

## 相关函数

- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_init](qiumingdll_init.md)