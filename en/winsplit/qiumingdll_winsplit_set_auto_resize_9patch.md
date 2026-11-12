# qiumingdll_winsplit_set_auto_resize_9patch(splitId, mode, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)

Enables 9-Patch auto-follow for a split window: two guide lines define the 9-Patch grid, and two opposite corners of a rectangle define the target. When the main window is resized (or moved), the layout is remapped automatically according to the rules.

## Signature

```gml
qiumingdll_winsplit_set_auto_resize_9patch(splitId, mode, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, value range 1 ~ 16 |
| mode | Real | yes | Follow mode: **0 = window scaling**, **1 = content scaling** (both must be supported, see below) |
| gridX1 | Real | yes | Vertical guide line 1 (left), design coordinate system |
| gridY1 | Real | yes | Horizontal guide line 1 (top), design coordinate system |
| gridX2 | Real | yes | Vertical guide line 2 (right), design coordinate system |
| gridY2 | Real | yes | Horizontal guide line 2 (bottom), design coordinate system |
| rectX1 | Real | yes | Rectangle top-left X (design coordinate system, may be out of bounds) |
| rectY1 | Real | yes | Rectangle top-left Y (design coordinate system, may be out of bounds) |
| rectX2 | Real | yes | Rectangle bottom-right X (design coordinate system, may be out of bounds) |
| rectY2 | Real | yes | Rectangle bottom-right Y (design coordinate system, may be out of bounds) |

The grid and the rectangle share the same **design coordinate system**: the size of the main window's client area at the moment this function is called (recorded as the design size). Requires `0 <= gridX1 <= gridX2 <= design width` and `0 <= gridY1 <= gridY2 <= design height`; the rectangle's opposite corners may be given in any order (they are sorted out internally).

## Two follow modes (mode)

| mode | Name | What rect defines | Behavior when the main window is resized |
|------|------|-------------------|--------------------|
| 0 | **Window scaling** | Target rectangle of the split window (main-window client-area coordinates) | The split window's position and size are remapped via 9-Patch (including following the main window's movement); at the same time the source region is scaled proportionally to the client area, so the split window always shows the same piece of game content |
| 1 | **Content scaling** | Source region (main-window client-area/backbuffer coordinates) | The split window's own **position and size stay unchanged**, and the source region is remapped via 9-Patch — the split window acts as a fixed viewport whose displayed content range changes as the main window is resized |

Both modes are supported; choose whichever fits. Parts of the source region that exceed the capture buffer are clamped automatically.

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully: auto-follow is enabled and the layout is applied once immediately as defined |
| 0 | Call failed: invalid id, winsplit not initialized, invalid main-window handle, zero client area, illegal mode, or a guide line out of bounds/in reverse order |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- 9-Patch mapping rule (horizontal axis as an example): `[0, gridX1]` and `[gridX2, design width]` are fixed regions (the distance to the edge is preserved), `[gridX1, gridX2]` is the stretch region (scaled proportionally); the vertical axis works the same way.
- If the main window shrinks until the fixed regions on both sides no longer fit, the mapping degrades to proportional scaling of the whole axis.
- After the call, normal animations and batch animations currently playing on that window are stopped, and then the layout is applied once immediately using the current main-window size.
- In mode 0 the source-region baseline is the source region at the moment of enabling; when the main window is resized it is converted proportionally from that baseline. To change the baseline, call this function again.
- After enabling, manual changes made with `set_position` / `set_size` / `set_region` / `set_source_region` are overwritten by the 9-Patch result the next time the main window changes; use `qiumingdll_winsplit_clear_auto_resize` to disable following at any time.
- In the compatibility case where the main window is moved off-screen by `hide_original` (Win7 fallback path), the split window does not follow the main window (to avoid moving the whole group off-screen); hiding via DWM Cloak on Win8+ is unaffected.

## Example

```gml
/// Create a split view: show the top-left quarter of the main window's client area,
/// placed at screen position (900, 80)
splitId = qiumingdll_winsplit_create(0, 0, 480, 270, 900, 80, 480, 270);

/// Mode 0 (window scaling): design resolution 960x540
/// Grid: x 96/(960-96), y 54/(540-54); rect: bottom-right quarter panel, scales with the window
qiumingdll_winsplit_set_auto_resize_9patch(
    splitId, 0,
    96, 54, 960 - 96, 540 - 54,
    640, 270, 960 - 20, 540 - 20);
```

```gml
/// Mode 1 (content scaling): the window is a fixed 320x180 "viewfinder",
/// and the source region is remapped via 9-Patch when the main window is resized —
/// content in the four fixed corner regions stays put, while the middle content range
/// changes with the window
qiumingdll_winsplit_set_auto_resize_9patch(
    splitId, 1,
    120, 80, 960 - 120, 540 - 80,
    100, 80, 420, 260);
```

## Related functions

- [qiumingdll_winsplit_clear_auto_resize](qiumingdll_winsplit_clear_auto_resize.md)
- [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_webview_set_auto_resize_9patch](../webview/qiumingdll_webview_set_auto_resize_9patch.md)
