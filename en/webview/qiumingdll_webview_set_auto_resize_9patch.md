# qiumingdll_webview_set_auto_resize_9patch(webviewId, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)

Make a **child window** WebView follow main window scaling automatically using 9-Patch rules: first define the 9-Patch grid with two guide lines, then define the child window position and size with the two corner coordinates of a rectangle. When the main window size changes, the rectangle is remapped by the 9-Patch rules and applied automatically.

## Signature

```gml
qiumingdll_webview_set_auto_resize_9patch(webviewId, gridX1, gridY1, gridX2, gridY2, rectX1, rectY1, rectX2, rectY2)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id (must be a child window created by create_child) |
| gridX1 | Real | yes | Vertical guide line 1 (left), design coordinate space; `[0, gridX1]` is a fixed region |
| gridY1 | Real | yes | Horizontal guide line 1 (top), design coordinate space; `[0, gridY1]` is a fixed region |
| gridX2 | Real | yes | Vertical guide line 2 (right), design coordinate space; `[gridX2, design width]` is a fixed region |
| gridY2 | Real | yes | Horizontal guide line 2 (bottom), design coordinate space; `[gridY2, design height]` is a fixed region |
| rectX1 | Real | yes | X of the window rectangle top-left corner (design coordinate space, may be out of bounds) |
| rectY1 | Real | yes | Y of the window rectangle top-left corner (design coordinate space, may be out of bounds) |
| rectX2 | Real | yes | X of the window rectangle bottom-right corner (design coordinate space, may be out of bounds) |
| rectY2 | Real | yes | Y of the window rectangle bottom-right corner (design coordinate space, may be out of bounds) |

The grid and the rectangle share the same **design coordinate space**: the main window client area size at the moment this function is called (recorded as the design size). Requires `0 <= gridX1 <= gridX2 <= design width` and `0 <= gridY1 <= gridY2 <= design height`; the rectangle corner coordinates may be given in any order (they are normalized internally).

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully: automatic following enabled and the layout applied once immediately |
| 0 | Call failed: invalid id, not a child window, invalid main window handle, zero client area, or grid guide lines out of bounds / reversed |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- 9-Patch mapping rules (horizontal axis shown):
  - `[0, gridX1]` and `[gridX2, design width]` are **fixed regions**: rectangle edges inside them keep a constant distance to the left/right edge;
  - `[gridX1, gridX2]` is the **stretch region**: rectangle edges inside it scale by their ratio within the stretch region.
  - The vertical axis works the same way.
- Typical usage: set `grid` to "large stretchable middle, fixed margins around the edges", then set rect to "fill everything except the margins" to get an adaptive layout with margins; place rect entirely inside a fixed region to get a small window pinned to a corner.
- If the main window shrinks so much that the fixed regions on both sides no longer fit, it degrades to proportional scaling over the whole axis.
- Mutually exclusive with `resize_to_parent`: calling this function first disables `resize_to_parent`; calling `resize_to_parent` also disables this following.
- The layout is applied once immediately using the current main window size (when the current size == design size, the rect is used as-is).
- The rect recorded by this function is the layout baseline; to change the baseline layout after enabling, simply call this function again. `set_position` / `set_size` / `set_region` do not update the baseline, so the next main window change returns to the 9-Patch result; `qiumingdll_webview_resize` cancels following instead.
- Removed automatically on cleanup / main window destruction.

## Example

```gml
/// Create event: initialize and create the child window
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(0, 0, 800, 480);

/// Step event: enable 9-Patch following once ready
if (!started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    started = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com");

    // Design resolution 800x480 (current client area):
    // Grid guide lines x: 64 / (800-64), y: 48 / (480-48)
    // Rectangle: fill with a 16px margin (rect lies in the stretch region, so it scales with the window)
    qiumingdll_webview_set_auto_resize_9patch(
        webviewId,
        64, 48, 800 - 64, 480 - 48,
        16, 16, 800 - 16, 480 - 16);
}
```

```gml
/// 200x120 small window pinned to the bottom-left corner: the rectangle lies entirely
/// in the left fixed region (x < gridX1) and the bottom fixed region (y > gridY2),
/// so it never moves when the window is scaled
qiumingdll_webview_set_auto_resize_9patch(
    webviewId,
    300, 200, 800 - 300, 480 - 200,
    10, 480 - 130, 210, 480 - 10);
```

## Related functions

- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
- [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md)
- [qiumingdll_webview_resize](qiumingdll_webview_resize.md)
- [qiumingdll_winsplit_set_auto_resize_9patch](../winsplit/qiumingdll_winsplit_set_auto_resize_9patch.md)
