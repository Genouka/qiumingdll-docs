# qiumingdll_procdetect_process(name)

Detects whether a process with the specified name exists on the system.

## Signature

```gml
qiumingdll_procdetect_process(name)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| name | String | yes | Name of the process to detect; the `.exe` suffix is optional (e.g. `"notepad.exe"` / `"cheatengine-x86_64"`), case-insensitive |

## Returns

| Value | Description |
|----|------|
| 1 | A matching process exists on the system |
| 0 | No matching process found, or a non-Windows platform / not initialized (returns 0 in that case) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: Windows only.
- Behavior: more general than `procdetect_cheatengine` / `procdetect_streaming`; it can detect any custom process name, e.g. to decide behavior in combination with trainers or helper tools.
- Note: passing an empty string usually matches no process; process name matching is exact (there is no fuzzy prefix/suffix matching).
- Async mode: by default it reads from the background cache, so a process that has just started/just exited may take up to about 0.5 seconds to show up in the result; safe to call every frame from the Step event without stuttering.

## Example

```gml
/// Check whether the player is running some trainer
if (qiumingdll_procdetect_process("some_trainer.exe"))
{
    show_debug_message("Trainer detected, achievements disabled");
    achievements_enabled = false;
}
```

## Related functions

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
