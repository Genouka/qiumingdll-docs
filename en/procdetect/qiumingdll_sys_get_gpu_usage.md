# qiumingdll_sys_get_gpu_usage()

Gets the system-wide GPU usage (percentage 0~100).

## Signature

```gml
qiumingdll_sys_get_gpu_usage()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 100 | System GPU usage percentage since the previous call (peak across engine nodes) |
| 0 | First call (only establishes the baseline, no delta); or the GPU was idle during the sampling interval |
| -1 | Call failed (not Windows, no usable display adapter, or the driver does not support the statistics interface) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: only takes effect on Windows; based on WDDM's `D3DKMTEnumAdapters` + `D3DKMTQueryStatistics` (NODE type), it reads the accumulated running time of the engine nodes of all display adapters and diffs it against the previous call.
- Behavior: the first call only records the baseline and returns 0; subsequent calls return the average GPU usage over the interval **since the previous call**. Keep a reasonable interval between calls (e.g. once every 500 ms~1 s); too short an interval makes the value unstable.
- The usage is the **peak** usage across all engine nodes, reflecting the load of the busiest engine on the GPU, so it is not inflated by multiple engines running in parallel.
- Typical use: showing GPU load on the settings screen, lowering visual quality or effects when the graphics card is under too much pressure.
- This value is **system-wide** GPU usage, not the usage of a single process.

## Example

```gml
qiumingdll_init();

// Sample about once per second in the Step event
if (gpu_timer <= 0)
{
    var gpu = qiumingdll_sys_get_gpu_usage();
    if (gpu >= 0)
    {
        show_debug_message("System GPU usage: " + string(gpu) + "%");
    }
    gpu_timer = game_get_speed(gamespeed_fps); // about 1 second
}
else
{
    gpu_timer -= 1;
}
```

## Related functions

- [qiumingdll_sys_get_cpu_usage](qiumingdll_sys_get_cpu_usage.md)
- [qiumingdll_sys_get_memory_info](qiumingdll_sys_get_memory_info.md)
- [qiumingdll_init](qiumingdll_init.md)
