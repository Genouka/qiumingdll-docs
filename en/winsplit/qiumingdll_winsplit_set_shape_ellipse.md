# qiumingdll_winsplit_set_shape_ellipse(splitId)

Set the specified split window to an elliptical shape (an ellipse inscribed in its client area). The four corners become transparent, making it suitable for circular minimaps, circular avatar windows, and similar effects.

## Signature

```gml
qiumingdll_winsplit_set_shape_ellipse(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | real | yes | Split window ID, in the range 1 ~ 16; the window must exist |

## Returns

| Value | Description |
|----|------|
| `1` | The elliptical shape was applied successfully |
| `0` | Failure: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window identified by `splitId` exists.
- The ellipse is inscribed in the window's client area: a full ellipse whose width equals the client width and whose height equals the client height (a horizontally oriented ellipse). The window must be sufficiently "square" to approach a true circle; for a true circle, first use `set_size` to make the width and height equal.
- Areas outside the ellipse become transparent. Mouse clicks on transparent areas pass through to the desktop.
- The ellipse size does not update automatically when the window size changes. If you later change the window size with `set_size`, call this function again to refresh the shape.
- This shape replaces any previously set shape; `qiumingdll_winsplit_clear_shape` restores the rectangle.

## Example

```gml
// In the Step event of a controller object: press M to create a 400x400 circular minimap split window
if (keyboard_check_pressed(ord("M")))
{
    // Create a square window first, then apply the ellipse => a true circle
    if (global.split_minimap == 0)
        global.split_minimap = qiumingdll_winsplit_create(0, 0, 500, 500, 30, 30, 400, 400);

    qiumingdll_winsplit_set_shape_ellipse(global.split_minimap);
}
```

## Related functions

- [qiumingdll_winsplit_set_shape_roundrect](qiumingdll_winsplit_set_shape_roundrect.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)
