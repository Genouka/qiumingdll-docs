# qiumingdll_sys_get_cpu_usage()

获取系统整体 CPU 占用率（百分比 0~100）。

## 函数签名

```gml
qiumingdll_sys_get_cpu_usage()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 100 | 自上次调用以来的系统 CPU 占用率百分比 |
| 0 | 首次调用（仅建立基线，无差值）；或采样间隔内完全空闲 |
| -1 | 调用失败（非 Windows 或无法读取系统时间） |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；基于 `GetSystemTimes` 两次调用的差值计算。
- 行为细节：第一次调用只记录基线并返回 0；后续调用返回**距上一次调用**这一段时间内的平均 CPU 占用率。因此请保持一定调用间隔（如每 500ms~1s 一次），间隔过短会导致数值不稳定。
- 典型用途：在设置界面显示系统负载、在性能不足时降低画质或提示玩家。
- 该值为**系统整体**占用率，不是单个进程的占用率。

## 示例

```gml
qiumingdll_init();

// 在步进事件中每隔约 1 秒采样一次
if (cpu_timer <= 0)
{
    var cpu = qiumingdll_sys_get_cpu_usage();
    if (cpu >= 0)
    {
        show_debug_message("系统 CPU 占用: " + string(cpu) + "%");
    }
    cpu_timer = game_get_speed(gamespeed_fps); // 约 1 秒
}
else
{
    cpu_timer -= 1;
}
```

## 相关函数

- [qiumingdll_sys_get_memory_info](qiumingdll_sys_get_memory_info.md)
- [qiumingdll_sys_get_gpu_usage](qiumingdll_sys_get_gpu_usage.md)
- [qiumingdll_init](qiumingdll_init.md)
