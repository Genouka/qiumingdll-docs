# qiumingdll_winsplit_set_capture_mode(mode)

Sets the capture method of split windows. **Deprecated**: the new implementation always reads the backbuffer directly from the GPU, so calling this function has no effect (the return value is always 1).

## Signature

```gml
qiumingdll_winsplit_set_capture_mode(mode)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| mode | Real | yes | Capture mode parameter of the old implementation (such as "screen capture / PrintWindow"). It is ignored in the new implementation and any value is accepted (0 is recommended) |

## Returns

| Value | Description |
|----|------|
| 1 | The function executed successfully (fixed return value; does not mean anything took effect) |
| 0 | Non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- **Deprecated, calling it has no effect**: the new D3D11 GPU capture pipeline always reads the frame from the IDXGISwapChain backbuffer; the "screen capture mode" switch no longer exists.
- The API is kept only for compatibility with legacy callers: even if called, the capture behavior does not change.
- Global setting with no splitId parameter; it applies to all split windows (in practice it does nothing).
- New code should not call this function; simply remove it from the project.
- Platform support: Windows only; on other platforms the GML wrapper returns 0.

## Example

```gml
// Legacy-code migration example: the call below has no effect in the new implementation and can safely be deleted
if (variable_global_exists("__qiumingdll_winsplit_set_capture_mode"))
{
    qiumingdll_winsplit_set_capture_mode(0);
}
```

## Related functions

- [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md)
- [qiumingdll_winsplit_set_render_interval](qiumingdll_winsplit_set_render_interval.md)
- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)
- [qiumingdll_winsplit_set_render_during_drag](qiumingdll_winsplit_set_render_during_drag.md)
