# qiumingdll_procdetect_set_sync_mode(enabled)

切换进程检测的工作模式。默认使用**异步模式**：后台线程持续枚举系统进程并缓存结果，检测函数只读缓存，可以放心放进 Step 事件每帧调用。将 `enabled` 设为 1 可切回旧版**同步模式**（每次调用都实时枚举，结果永远最新，但每帧调用会明显卡顿）。

## 函数签名

```gml
qiumingdll_procdetect_set_sync_mode(enabled)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| enabled | Real | 是 | 1 = 使用旧的同步实时枚举模式；0 = 使用异步缓存模式（默认） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 当前处于同步模式 |
| 0 | 当前处于异步模式 |
| -1 | 请求切换到异步模式但后台线程启动失败（自动保持同步模式） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：
  - **异步模式（默认）**：后台线程每 500ms 枚举一次系统进程，`procdetect_cheatengine` / `procdetect_streaming` / `procdetect_multiinstance` / `procdetect_process` / `procdetect_count_by_name` / `procdetect_get_commandline` 都从缓存读取；检测结果最长有约 0.5 秒延迟。
  - **同步模式**：与旧版本完全一致，每次调用实时枚举全部系统进程；单次调用约需 5~30ms（取决于系统进程数量），放进 Step 事件会掉帧。
- 切换模式是全局的，立即对所有进程检测函数生效；切换到异步时后台线程会立即刷新一次缓存。
- 无需为"是否使用异步"单独初始化：DLL 加载后默认即为异步模式，未调用任何检测函数前不会创建后台线程。

## 示例

```gml
qiumingdll_init();

// 默认异步模式：Step 事件里每帧检测也不会卡
// （Create 事件）
alarm[0] = room_speed * 3;

// （Alarm 0 事件）
if (qiumingdll_procdetect_cheatengine()) {
    show_message("检测到作弊工具！");
}

// 需要绝对实时、无延迟的检测结果时（例如结算界面做一次性校验）
var prev = qiumingdll_procdetect_set_sync_mode(1); // 返回 1，表示已切到同步
if (qiumingdll_procdetect_multiinstance()) {
    game_end();
}
qiumingdll_procdetect_set_sync_mode(0);           // 返回 0，切回异步
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_count_by_name](qiumingdll_procdetect_count_by_name.md)
- [qiumingdll_procdetect_get_commandline](qiumingdll_procdetect_get_commandline.md)
