# qiumingdll_winself_set_shape_ellipse()

Set the game's own window to an elliptical shape (an ellipse inscribed in its client area); the four corners of the window become transparent. Suitable for circular minimaps, circular avatar windows, etc.

## Signature

```gml
qiumingdll_winself_set_shape_ellipse()
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

No parameters.

## Returns

| Value | Description |
|----|------|
| `1` | Ellipse shape applied successfully |
| `0` | Failure: invalid window handle; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: call on Windows with the game window already present. The function automatically uses `window_handle()` as the target window.
- The ellipse is inscribed in the window client area: its width is the full client-area width and its height the full client-area height. The window must be sufficiently "square" to approach a circle; to get a true circle, resize the window to a square first.
- Areas outside the ellipse become transparent, and mouse clicks on transparent areas pass through to the desktop.
- The ellipse size does not follow window size changes automatically: if you change the window size later, call this function again to refresh the shape.
- This shape replaces any shape set previously; `qiumingdll_winself_clear_shape` restores the rectangle.

## Example

```gml
// Clip the whole game window to an ellipse (inscribed in the client area)
qiumingdll_winself_set_shape_ellipse();
```

## Related functions

- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_set_shape_from_bitmap](qiumingdll_winself_set_shape_from_bitmap.md)
- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
