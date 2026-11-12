# qiumingdll_sys_get_cpu_usage()

Gets the system-wide CPU usage (percentage 0~100).

## Signature

```gml
qiumingdll_sys_get_cpu_usage()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 100 | System CPU usage percentage since the previous call |
| 0 | First call (only establishes the baseline, no delta); or completely idle during the sampling interval |
| -1 | Call failed (not Windows, or system time could not be read) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: only takes effect on Windows; computed from the difference between two `GetSystemTimes` calls.
- Behavior: the first call only records the baseline and returns 0; subsequent calls return the average CPU usage over the interval **since the previous call**. Keep a reasonable interval between calls (e.g. once every 500 ms~1 s); too short an interval makes the value unstable.
- Typical use: showing system load on the settings screen, lowering visual quality or warning the player when performance is insufficient.
- This value is **system-wide** usage, not the usage of a single process.

## Example

```gml
qiumingdll_init();

// Sample about once per second in the Step event
if (cpu_timer <= 0)
{
    var cpu = qiumingdll_sys_get_cpu_usage();
    if (cpu >= 0)
    {
        show_debug_message("System CPU usage: " + string(cpu) + "%");
    }
    cpu_timer = game_get_speed(gamespeed_fps); // about 1 second
}
else
{
    cpu_timer -= 1;
}
```

## Related functions

- [qiumingdll_sys_get_memory_info](qiumingdll_sys_get_memory_info.md)
- [qiumingdll_sys_get_gpu_usage](qiumingdll_sys_get_gpu_usage.md)
- [qiumingdll_init](qiumingdll_init.md)
