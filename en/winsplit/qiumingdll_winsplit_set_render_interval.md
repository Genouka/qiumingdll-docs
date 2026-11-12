# qiumingdll_winsplit_set_render_interval(intervalMs)

Sets the render refresh interval of split windows. **Deprecated**: the new implementation renders every frame in sync with the game's Present call, so this function no longer limits any render rate (calling it has no effect and the return value is always 1).

## Signature

```gml
qiumingdll_winsplit_set_render_interval(intervalMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| intervalMs | Real | yes | Render interval of the old implementation in milliseconds (e.g. 16 means roughly 60 fps). It is ignored in the new implementation and any value is accepted (16 is recommended) |

## Returns

| Value | Description |
|----|------|
| 1 | The function executed successfully (fixed return value; does not mean anything took effect) |
| 0 | Non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- **Deprecated, calling it has no effect**: the new implementation drives rendering from the Present hook in sync with game frames and no longer uses the old 1 ms timer and frame rate cap.
- The API is kept only for compatibility with legacy callers: even if called, the render cadence does not change.
- Global setting with no splitId parameter; it applies to all split windows (in practice it does nothing).
- New code should not call this function; simply remove it from the project.
- Platform support: Windows only; on other platforms the GML wrapper returns 0.

## Example

```gml
// Legacy-code migration example: the call below has no effect in the new implementation and can safely be deleted
if (variable_global_exists("__qiumingdll_winsplit_set_render_interval"))
{
    qiumingdll_winsplit_set_render_interval(16);
}
```

## Related functions

- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md)
- [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md)
- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)
