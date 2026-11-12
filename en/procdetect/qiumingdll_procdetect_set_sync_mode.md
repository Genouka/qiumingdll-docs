# qiumingdll_procdetect_set_sync_mode(enabled)

Switches the working mode of process detection. **Async mode** is used by default: a background thread keeps enumerating system processes and caches the results, and the detection functions only read the cache, so they can safely be called every frame from a Step event. Setting `enabled` to 1 switches back to the legacy **sync mode** (every call enumerates in real time, so the result is always up to date, but calling it every frame noticeably stutters).

## Signature

```gml
qiumingdll_procdetect_set_sync_mode(enabled)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| enabled | Real | yes | 1 = use the old synchronous real-time enumeration mode; 0 = use the asynchronous cache mode (default) |

## Returns

| Value | Description |
|----|------|
| 1 | Sync mode is currently active |
| 0 | Async mode is currently active |
| -1 | Switching to async mode was requested but the background thread failed to start (sync mode is kept automatically) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: Windows only.
- Behavior:
  - **Async mode (default)**: the background thread enumerates system processes every 500 ms, and `procdetect_cheatengine` / `procdetect_streaming` / `procdetect_multiinstance` / `procdetect_process` / `procdetect_count_by_name` / `procdetect_get_commandline` all read from the cache; detection results lag by up to about 0.5 seconds.
  - **Sync mode**: exactly as in older versions, every call enumerates all system processes in real time; a single call takes about 5~30 ms (depending on the number of processes), and calling it from the Step event drops frames.
- Switching modes is global and takes effect immediately for all process detection functions; when switching to async mode the background thread refreshes the cache once right away.
- There is no separate initialization for "whether to use async": the DLL is already in async mode after loading, and no background thread is created until a detection function is called.

## Example

```gml
qiumingdll_init();

// Default async mode: checking every frame in the Step event causes no stutter
// (Create event)
alarm[0] = room_speed * 3;

// (Alarm 0 event)
if (qiumingdll_procdetect_cheatengine()) {
    show_message("Cheat tool detected!");
}

// When you need absolutely real-time, zero-latency results (e.g. a one-off check on the results screen)
var prev = qiumingdll_procdetect_set_sync_mode(1); // returns 1, meaning sync mode is active
if (qiumingdll_procdetect_multiinstance()) {
    game_end();
}
qiumingdll_procdetect_set_sync_mode(0);           // returns 0, back to async
```

## Related functions

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_count_by_name](qiumingdll_procdetect_count_by_name.md)
- [qiumingdll_procdetect_get_commandline](qiumingdll_procdetect_get_commandline.md)
