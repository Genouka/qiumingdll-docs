# qiumingdll_procdetect_count_by_name(processName)

Counts, by executable file name, how many processes with that name are running on the system (case-insensitive, matching the full `.exe` name).

## Signature

```gml
qiumingdll_procdetect_count_by_name(processName)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| processName | String | yes | Executable file name to count. Matched exactly against the full exe file name, so pass the complete form such as `"notepad.exe"` or `"chrome.exe"`. Case-insensitive. An empty string is treated as an empty parameter |

## Returns

| Value | Description |
|----|------|
| ≥ 0 | Number of matching processes on the system (including all running instances) |
| -1 | Empty parameter (empty string or no argument passed) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: only takes effect on Windows; other platforms always return 0 (non-Windows never enters the counting branch, but the GML wrapper returns -1 by default on non-Windows).
- Behavior: internally walks the system process snapshot and compares each process's executable file name with `processName` using a case-insensitive exact match, accumulating the number of hits.
- Matching rules: same as `qiumingdll_procdetect_process()`, matching by **full file name (including the `.exe` extension)** by default; a name without the extension usually does not match.
- Async mode: reads from the background cache by default, so count changes can lag by up to about 0.5 seconds; safe to call every frame from the Step event without stuttering.
- Typical use: counting how many instances of a program are open, and combining that with a threshold to detect more concurrency than expected.
- Difference from `qiumingdll_procdetect_multiinstance()`: this function counts processes with **any given name**; the latter only counts instances with the **same name as itself** and takes no parameters.
- Detection is snapshot-based: a process started/ended after detection does not affect this result; poll the function if you need real-time monitoring.

## Example

```gml
qiumingdll_init();

// Count how many notepad processes are running on the system
var n = qiumingdll_procdetect_count_by_name("notepad.exe");
if (n > 0)
{
    show_debug_message("Found " + string(n) + " notepad processes");
}
else if (n == 0)
{
    show_debug_message("No notepad is running");
}
else // n == -1
{
    show_debug_message("Process name parameter is empty");
}
```

## Related functions

- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_get_commandline](qiumingdll_procdetect_get_commandline.md)
- [qiumingdll_init](qiumingdll_init.md)
