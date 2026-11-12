# qiumingdll_sys_get_memory_info()

Gets the system's physical memory usage, returned as a JSON string.

## Signature

```gml
qiumingdll_sys_get_memory_info()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

Returns a JSON string: `{ "total": total physical memory in bytes, "used": used bytes, "free": available bytes, "percent": used percentage }`.

| Field | Type | Description |
|------|------|------|
| total | Real | Total physical memory installed on the system (bytes) |
| used | Real | Physical memory currently in use (total - free, bytes) |
| free | Real | Physical memory currently available (bytes) |
| percent | Real | Used percentage, rounded to two decimal places (0.00 ~ 100.00) |

Returns `{}` when the call fails (non-Windows).

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: only takes effect on Windows; reads physical memory via `GlobalMemoryStatusEx`.
- Behavior: read in real time on every call, with no delta sampling like CPU/GPU, so it can be called at any time.
- To parse the returned JSON you can use `qiumingdll_json5_decode()`.
- Typical use: showing memory usage on the settings screen, prompting the player to close other programs when memory is low.

## Example

```gml
qiumingdll_init();

var json = qiumingdll_sys_get_memory_info();
var mem = qiumingdll_json5_decode(json);
if (is_array(mem))
{
    var totalMB = mem[? "total"] / (1024 * 1024);
    var usedMB = mem[? "used"] / (1024 * 1024);
    var pct = mem[? "percent"];
    show_debug_message("Memory: " + string(usedMB) + " / " + string(totalMB) + " MB (" + string(pct) + "%)");
}
```

## Related functions

- [qiumingdll_sys_get_cpu_usage](qiumingdll_sys_get_cpu_usage.md)
- [qiumingdll_sys_get_gpu_usage](qiumingdll_sys_get_gpu_usage.md)
- [qiumingdll_json5_decode](../json5/qiumingdll_json5_decode.md)
- [qiumingdll_init](qiumingdll_init.md)
