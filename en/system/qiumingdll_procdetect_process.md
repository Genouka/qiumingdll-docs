# qiumingdll_procdetect_process(processName)

Detects whether a process with the given executable file name exists on the system.

## Signature

```gml
qiumingdll_procdetect_process(processName)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| processName | String | Yes | Executable file name to detect. Matched exactly against the full exe file name; passing the complete form such as `"notepad.exe"`, `"chrome.exe"` is recommended. Case-insensitive (both `"NOTEPAD.EXE"` and `"Notepad.exe"` match). An empty string is treated as an empty parameter |

## Returns

| Value | Description |
|----|------|
| 1 | The process exists on the system |
| 0 | The process does not exist on the system, or called on a non-Windows platform |
| -1 | The parameter is empty (empty string or not passed) |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: Windows only; other platforms always return 0.
- Behavior: internally walks a snapshot of system processes and compares each process's executable file name with `processName` using a case-insensitive exact match, returning 1 on a hit.
- Matching rule: by default it matches the **full file name (including the `.exe` extension)**, consistent with the "Name" column shown in Task Manager. Without the extension (e.g. only `"notepad"`) the match usually fails, so always pass the full file name.
- It only detects whether the process exists; if you need to count processes with the same name, use `qiumingdll_procdetect_multiinstance()` (for itself) or poll this function as needed.
- Detection is snapshot-based: processes started or terminated do not affect the current result; poll the function if you need real-time monitoring.
- Typical use: checking prerequisites (e.g. whether a game launcher is running), detecting external programs (macro tools, helper utilities), etc.

## Example

```gml
// Check whether Notepad is open (for helper-program coordination)
qiumingdll_init();

var r = qiumingdll_procdetect_process("notepad.exe");
if (r == 1)
{
    show_debug_message("Notepad is running");
}
else if (r == 0)
{
    show_debug_message("Notepad is not running");
}
else // r == -1
{
    show_debug_message("Process name parameter is empty, cannot detect");
}

// Case-insensitive: the following is equivalent to the above
qiumingdll_procdetect_process("Notepad.EXE");
```

## Related functions

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_init](qiumingdll_init.md)
