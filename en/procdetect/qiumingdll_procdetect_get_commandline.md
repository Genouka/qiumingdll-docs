# qiumingdll_procdetect_get_commandline(processName)

Retrieves the command lines of all matching processes by executable file name, returned as a JSON array.

## Signature

```gml
qiumingdll_procdetect_get_commandline(processName)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| processName | String | yes | Executable file name to query. Matched exactly against the full exe file name, case-insensitive. An empty string is treated as an empty parameter |

## Returns

Returns a JSON array of strings, each element being `{ "pid": process ID, "cmdline": "command line string" }`:

| Case | Return value |
|------|--------|
| Process matched | `[{"pid":1234,"cmdline":"C:\\game\\game.exe -fullscreen"}, ...]` |
| No match | `[]` |
| Empty parameter | `[]` |

Double quotes, backslashes, line feeds, carriage returns and tabs in the command line are automatically escaped into characters valid in JSON.

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Async mode: the PID list comes from the background cache (up to about 0.5 seconds of latency), while the command line content is still read in real time at call time; the process behind a PID may have already exited, in which case that element's `cmdline` is an empty string.
- Platform limits: only takes effect on Windows; internally read through `NtQueryInformationProcess(ProcessCommandLineInformation)`. Requires `PROCESS_QUERY_INFORMATION` (or `PROCESS_QUERY_LIMITED_INFORMATION`) access to that process; a normal user process can usually read itself and most processes, while some protected processes may fail to be read (the corresponding element is skipped).
- Behavior: first collects all PIDs matching `processName`, reads each one's full command line, then returns them as a JSON array.
- Typical use: determining whether a process was launched with specific arguments (such as debug flags), or, when preventing multiple instances, telling real instances apart from wrapper processes of the same name.
- To parse the returned JSON you can use `qiumingdll_json5_decode()` (this extension has built-in JSON5 parsing).
- Detection is snapshot-based: a process started/ended after detection does not affect this result.

## Example

```gml
qiumingdll_init();

var json = qiumingdll_procdetect_get_commandline("game.exe");
var arr = qiumingdll_json5_decode(json);
if (is_array(arr))
{
    for (var i = 0; i < array_length(arr); i++)
    {
        var item = arr[i];
        show_debug_message("PID=" + string(item[? "pid"]) + " CMD=" + string(item[? "cmdline"]));
    }
}
```

## Related functions

- [qiumingdll_procdetect_count_by_name](qiumingdll_procdetect_count_by_name.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_json5_decode](../json5/qiumingdll_json5_decode.md)
- [qiumingdll_init](qiumingdll_init.md)
