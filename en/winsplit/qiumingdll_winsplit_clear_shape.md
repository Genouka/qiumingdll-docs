# qiumingdll_winsplit_clear_shape(splitId)

Clear the shape region of the specified split window and restore it to a complete rectangle (showing the entire client area).

## Signature

```gml
qiumingdll_winsplit_clear_shape(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |

## Returns

| Value | Description |
|----|------|
| 1 | Shape cleared successfully (returns 1 even if there was no shape before) |
| 0 | Failure: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully, and the split window for splitId exists.
- Undoes any shape setting (polygon begin/end, ellipse, rounded rectangle, bitmap shape); the window returns to a complete rectangular display.
- Clearing the shape does not change the window position, size, source region or any other property.
- Safe to call repeatedly: it is still 1 when the window never had a shape, without error.
- The recorded "shape point buffer" (an unfinished one after begin_shape without end) is unrelated to this function and is still cleared automatically by the next begin_shape.

## Example

```gml
// In the Step event of a controller object: press X to toggle between "circle mode" and "rectangle mode"
if (keyboard_check_pressed(ord("X")))
{
    global.round_mode = !global.round_mode;

    if (global.round_mode)
        qiumingdll_winsplit_set_shape_ellipse(global.split_1);
    else
        qiumingdll_winsplit_clear_shape(global.split_1);
}
```

## Related functions

- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_shape_roundrect](qiumingdll_winsplit_set_shape_roundrect.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
