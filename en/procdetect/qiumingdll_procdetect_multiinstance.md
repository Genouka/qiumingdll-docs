# qiumingdll_procdetect_multiinstance()

Detects whether the current game is running as multiple instances (2 or more processes with the same name exist on the system).

## Signature

```gml
qiumingdll_procdetect_multiinstance()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Multiple instances detected: 2 or more processes with the same name as the current game exist on the system |
| 0 | Not running as multiple instances (only the current one), or a non-Windows platform / not initialized (returns 0 in that case) |
| -1 | Failed to get the executable file name of the current process |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: Windows only.
- Behavior: gets the current executable file name (exe name) and counts processes with the same name on the system; the count includes the current process itself, and **only when there are ≥ 2 same-named processes does it return 1**.
- Note: if players run multiple instances by renaming the exe file, this function may not detect it; in async mode the result comes from the background cache (up to about 0.5 seconds of latency), see [qiumingdll_procdetect_set_sync_mode](qiumingdll_procdetect_set_sync_mode.md) for details.

## Example

```gml
/// Check at game startup
qiumingdll_init();
if (qiumingdll_procdetect_multiinstance())
{
    show_message("Multiple game instances detected. Continue?");
}
```

## Related functions

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_set_sync_mode](qiumingdll_procdetect_set_sync_mode.md)
