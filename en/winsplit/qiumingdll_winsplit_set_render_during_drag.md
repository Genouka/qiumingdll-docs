# qiumingdll_winsplit_set_render_during_drag(enable)

Sets whether the window content keeps rendering while a split window is being dragged (global setting, enabled by default).

## Signature

```gml
qiumingdll_winsplit_set_render_during_drag(enable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| enable | Real | yes | 0 = do not render while dragging, non-zero = render while dragging (default value 1) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: preferably called after qiumingdll_winsplit_init (it is a global setting, so calling it at any time works).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- This function is still effective (it is not a deprecated API): it controls whether the content keeps rendering while the user drags a split window (draggable windows, see qiumingdll_winsplit_set_draggable).
- The default value is 1 (render while dragging). Passing 0 makes dragging cheaper, but the picture then reflects the frame from after the drag ends.
- Global setting that affects all split windows.
- This setting is a low-priority tuning option: generally it is not recommended to change the default.

## Example

```gml
// Create event: initialize, enable "render while dragging" and create the split window
qiumingdll_winsplit_init();
qiumingdll_winsplit_set_render_during_drag(1);  // render normally during dragging

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
qiumingdll_winsplit_set_draggable(global.splitId, 1);  // allow dragging
```

## Related functions

- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)
- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md) (deprecated)
- [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md) (deprecated)
