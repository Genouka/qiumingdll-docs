# qiumingdll_procdetect_multiinstance()

Counts how many processes with the same name are currently running (including this game itself), for multi-instance detection.

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
| 1 | Only one instance of this game is running (normal single instance) |
| Integer greater than 1 | Number of running instances (including itself); for example, 2 means two game windows already exist, i.e. multiple instances |
| -1 | Returned when obtaining its own executable path fails (rare) |
| 0 | Returned when called on a non-Windows platform |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: Windows only; other platforms always return 0.
- Behavior: internally obtains the full path of this process's executable (`GetModuleFileName`), takes its file name (e.g. `game.exe`), then walks a snapshot of system processes and counts the processes with that name. This process itself is always counted, so a normal single instance returns 1.
- Note: it counts processes with the **same executable file name** — if two copies of the game sit in different directories but their exe files share a name, both are counted.
- Typical use: limiting multiple instances (warn and quit when the count is greater than 1), counting online instances, etc.
- Detection is snapshot-based: processes started or terminated after the check do not affect the current result.
- Unlike `qiumingdll_procdetect_process()`, this function does not need and does not accept a process name parameter; it is determined entirely from its own file name.

## Example

```gml
// Forbid multiple instances at startup
qiumingdll_init();

var count = qiumingdll_procdetect_multiinstance();
if (count > 1)
{
    qiumingdll_show_error("Detected " + string(count) + " running instances of the game;\r\nonly one game window may run at a time");
    game_end();
}
else
{
    show_debug_message("Current instance count: " + string(count) + " (normal)");
}
```

## Related functions

- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_init](qiumingdll_init.md)
