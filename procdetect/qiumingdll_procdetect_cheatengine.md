# qiumingdll_procdetect_cheatengine()

检测当前系统中是否存在 Cheat Engine（Cheat Engine 进程）。

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
| 1 | 检测到 Cheat Engine 相关进程正在运行 |
| 0 | 未检测到，或非 Windows 平台 / 未初始化（此时返回 0） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows；依赖系统进程枚举权限（通常无需管理员权限）。
- 行为细节：通过进程名匹配进行检测，可用于反作弊、提示玩家关闭调试工具等场景。
- 注意：检测结果只在调用瞬间有效，进程状态变化后需要重新调用；如需持续监控请在步进事件中定期轮询。

## 示例

```gml
/// 步进事件（每 60 帧检查一次）
if (frame % 60 == 0)
{
    if (qiumingdll_procdetect_cheatengine())
        show_debug_message("检测到 Cheat Engine");
}
```

## 相关函数

- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)