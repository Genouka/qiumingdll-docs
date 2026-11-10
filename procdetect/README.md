# procdetect 模块

系统进程检测：Cheat Engine、直播/录屏软件、游戏多开实例、任意指定名称进程的数量与命令行，以及系统 CPU / 内存 / GPU 占用率。

检测默认在后台线程异步进行（结果缓存约 0.5 秒），检测函数只读缓存，可安全地放入 Step 事件每帧调用；`qiumingdll_procdetect_set_sync_mode(1)` 可切回旧的同步实时枚举模式。

共 10 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md) | 检测当前系统中是否存在 Cheat Engine（Cheat Engine 进程）。 |
| [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md) | 检测当前游戏是否被多开（同名进程 ≥ 2 返回 1）。 |
| [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md) | 检测系统中是否存在指定名称的进程。 |
| [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md) | 检测当前系统中是否存在常见直播/录屏软件进程（如 OBS、Streamlabs 等），用于判断游戏是否正在被串流或录制。 |
| [qiumingdll_procdetect_count_by_name](qiumingdll_procdetect_count_by_name.md) | 按可执行文件名统计当前系统中同名进程的数量。 |
| [qiumingdll_procdetect_get_commandline](qiumingdll_procdetect_get_commandline.md) | 按可执行文件名获取所有匹配进程的命令行（JSON 数组）。 |
| [qiumingdll_procdetect_set_sync_mode](qiumingdll_procdetect_set_sync_mode.md) | 切换进程检测模式：1 = 旧的同步实时枚举，0 = 异步缓存（默认）。 |
| [qiumingdll_sys_get_cpu_usage](qiumingdll_sys_get_cpu_usage.md) | 获取系统整体 CPU 占用率（百分比）。 |
| [qiumingdll_sys_get_memory_info](qiumingdll_sys_get_memory_info.md) | 获取系统物理内存使用情况（JSON）。 |
| [qiumingdll_sys_get_gpu_usage](qiumingdll_sys_get_gpu_usage.md) | 获取系统整体 GPU 占用率（百分比）。 |



[返回文档首页](../README.md)