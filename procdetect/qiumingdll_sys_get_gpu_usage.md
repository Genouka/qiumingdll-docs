# qiumingdll_sys_get_gpu_usage()

获取系统整体 GPU 占用率（百分比 0~100）。

## 函数签名

```gml
qiumingdll_sys_get_gpu_usage()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 ~ 100 | 自上次调用以来的系统 GPU 占用率百分比（取各引擎节点峰值） |
| 0 | 首次调用（仅建立基线，无差值）；或采样间隔内 GPU 空闲 |
| -1 | 调用失败（非 Windows、无可用显示适配器或驱动不支持统计接口） |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；基于 WDDM 的 `D3DKMTEnumAdapters` + `D3DKMTQueryStatistics`（NODE 类型）读取所有显示适配器的引擎节点累计运行时间，并与上次调用做差。
- 行为细节：第一次调用只记录基线并返回 0；后续调用返回**距上一次调用**这一段时间内的平均 GPU 占用率。请保持一定调用间隔（如每 500ms~1s 一次），间隔过短会导致数值不稳定。
- 占用率为所有引擎节点的**峰值**占用，反映 GPU 中最繁忙引擎的负载，不会因为多引擎并行而叠加虚高。
- 典型用途：在设置界面显示 GPU 负载、在显卡压力过大时降低画质或特效。
- 该值为**系统整体** GPU 占用率，不是单个进程的占用率。

## 示例

```gml
qiumingdll_init();

// 在步进事件中每隔约 1 秒采样一次
if (gpu_timer <= 0)
{
    var gpu = qiumingdll_sys_get_gpu_usage();
    if (gpu >= 0)
    {
        show_debug_message("系统 GPU 占用: " + string(gpu) + "%");
    }
    gpu_timer = game_get_speed(gamespeed_fps); // 约 1 秒
}
else
{
    gpu_timer -= 1;
}
```

## 相关函数

- [qiumingdll_sys_get_cpu_usage](qiumingdll_sys_get_cpu_usage.md)
- [qiumingdll_sys_get_memory_info](qiumingdll_sys_get_memory_info.md)
- [qiumingdll_init](qiumingdll_init.md)
