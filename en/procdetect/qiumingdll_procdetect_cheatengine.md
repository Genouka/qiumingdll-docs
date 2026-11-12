# qiumingdll_procdetect_cheatengine()

Detects whether Cheat Engine is present on the system (a Cheat Engine process).

## Signature

```gml
qiumingdll_procdetect_cheatengine()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | A Cheat Engine related process is running |
| 0 | Not detected, or a non-Windows platform / not initialized (returns 0 in that case) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: Windows only; relies on permission to enumerate system processes (administrator rights are usually not required).
- Behavior: detection is done by matching process names; useful for anti-cheat, prompting players to close debugging tools, and similar scenarios.
- Note: the result is only valid at the instant of the call; after the process state changes, call it again. For continuous monitoring, poll it periodically from the Step event.
- Async mode: by default it reads from the background cache, so a process that has just started/just exited may take up to about 0.5 seconds to show up in the result; call `qiumingdll_procdetect_set_sync_mode(1)` if you need real-time results. It is safe to call every frame from the Step event without stuttering.

## Example

```gml
/// Step event (check once every 60 frames)
if (frame % 60 == 0)
{
    if (qiumingdll_procdetect_cheatengine())
        show_debug_message("Cheat Engine detected");
}
```

## Related functions

- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
