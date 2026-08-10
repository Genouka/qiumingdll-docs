# qiumingdll_procdetect_process(name)

检测系统中是否存在指定名称的进程。

## 函数签名

```gml
qiumingdll_procdetect_process(name)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | String | 是 | 要检测的进程名，可带 `.exe` 后缀（如 `"notepad.exe"` / `"cheatengine-x86_64"`），不区分大小写 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 系统中存在匹配的进程 |
| 0 | 未找到匹配的进程，或非 Windows 平台 / 未初始化（此时返回 0） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：比 `procdetect_cheatengine` / `procdetect_streaming` 更通用，可检测任意自定义进程名，用于与修改器、辅助工具等联动判断。
- 注意：传入空字符串时通常不会匹配任何进程；进程名匹配为完全匹配（不含模糊前缀/后缀）。

## 示例

```gml
/// 检查玩家是否开着某个修改器
if (qiumingdll_procdetect_process("some_trainer.exe"))
{
    show_debug_message("检测到修改器，已禁用成就");
    achievements_enabled = false;
}
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)