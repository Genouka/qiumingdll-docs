# qiumingdll_procdetect_multiinstance()

检测当前游戏是否被多开（系统中存在 2 个及以上同名进程）。

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
| 1 | 检测到多开：系统中存在 2 个及以上与当前游戏同名的进程 |
| 0 | 未多开（只有当前实例），或非 Windows 平台 / 未初始化（此时返回 0） |
| -1 | 获取当前进程可执行文件名失败 |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：获取当前可执行文件名（exe 名），统计系统中同名进程数量；统计结果包含当前进程自身，**只有 ≥ 2 个同名进程才返回 1**。
- 注意：若玩家通过修改 exe 文件名的方式多开，本函数可能无法识别；异步模式下结果来自后台缓存（最长约 0.5 秒延迟），详见 [qiumingdll_procdetect_set_sync_mode](qiumingdll_procdetect_set_sync_mode.md)。

## 示例

```gml
/// 游戏启动时检查
qiumingdll_init();
if (qiumingdll_procdetect_multiinstance())
{
    show_message("检测到游戏已多开，是否继续？");
}
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_set_sync_mode](qiumingdll_procdetect_set_sync_mode.md)