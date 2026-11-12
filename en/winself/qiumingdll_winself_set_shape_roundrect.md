# qiumingdll_winself_set_shape_roundrect(cornerW, cornerH)

Set the game's own window to a rounded-rectangle shape (each of the four corners is cut with the specified corner radius); the common shape for a "borderless rounded panel".

## Signature

```gml
qiumingdll_winself_set_shape_roundrect(cornerW, cornerH)
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| cornerW | real | yes | Width of the corner ellipse (pixels), typically from 0 to half the shorter side of the client area |
| cornerH | real | yes | Height of the corner ellipse (pixels), typically from 0 to half the shorter side of the client area |

## Returns

| Value | Description |
|----|------|
| `1` | Rounded-rectangle shape applied successfully |
| `0` | Failure: invalid window handle; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: call on Windows with the game window already present. The function automatically uses `window_handle()` as the target window.
- The rounded rectangle is inscribed in the window client area; the four corners are cut with the ellipse corners specified by (cornerW, cornerH).
- If cornerW / cornerH are too large (more than half the shorter side), the system handles them within the valid range; it is recommended to use smaller common values (e.g. 16, 32).
- The shape is based on window client-area coordinates and does not update automatically when the window is resized: call this function again after changing the window size.
- This shape replaces any shape set previously; `qiumingdll_winself_clear_shape` restores the rectangle.

## Example

```gml
// Give the game window 32px rounded corners
qiumingdll_winself_set_shape_roundrect(32, 32);
```

## Related functions

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_from_bitmap](qiumingdll_winself_set_shape_from_bitmap.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
