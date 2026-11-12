# procdetect module

System process detection: Cheat Engine, streaming/recording software, multiple game instances, the count and command lines of processes with any given name, plus system-wide CPU / memory / GPU usage.

By default, detection runs asynchronously on a background thread (results are cached for about 0.5 seconds). The detection functions only read the cache, so they are safe to call every frame from a Step event; `qiumingdll_procdetect_set_sync_mode(1)` switches back to the old synchronous, real-time enumeration mode.

10 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md) | Detects whether Cheat Engine is present on the system (a Cheat Engine process). |
| [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md) | Detects whether the current game is running as multiple instances (returns 1 when there are ≥ 2 processes with the same name). |
| [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md) | Detects whether a process with the specified name exists on the system. |
| [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md) | Detects whether common streaming/recording software processes (such as OBS, Streamlabs, etc.) are present on the system, to determine whether the game is being streamed or recorded. |
| [qiumingdll_procdetect_count_by_name](qiumingdll_procdetect_count_by_name.md) | Counts the number of processes with the same executable file name currently running on the system. |
| [qiumingdll_procdetect_get_commandline](qiumingdll_procdetect_get_commandline.md) | Retrieves the command lines of all matching processes by executable file name (JSON array). |
| [qiumingdll_procdetect_set_sync_mode](qiumingdll_procdetect_set_sync_mode.md) | Switches the process detection mode: 1 = old synchronous real-time enumeration, 0 = asynchronous cache (default). |
| [qiumingdll_sys_get_cpu_usage](qiumingdll_sys_get_cpu_usage.md) | Gets the system-wide CPU usage (percentage). |
| [qiumingdll_sys_get_memory_info](qiumingdll_sys_get_memory_info.md) | Gets the system's physical memory usage (JSON). |
| [qiumingdll_sys_get_gpu_usage](qiumingdll_sys_get_gpu_usage.md) | Gets the system-wide GPU usage (percentage). |



[Back to documentation home](../README.md)
