# qiumingdll_winsplit_end_shape(splitId)

End shape recording and apply the collected polygon vertices to the split window: the window immediately becomes that polygon shape, and areas outside the polygon are no longer displayed.

## Signature

```gml
qiumingdll_winsplit_end_shape(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must match the splitId of this begin_shape group |

## Returns

| Value | Description |
|----|------|
| 1 | Shape applied successfully; the split window now has the polygon appearance |
| 0 | Failure: splitId is invalid, this window is not in shape recording state, or fewer than 3 vertices (the points recorded this round are discarded); on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_begin_shape` was called first for the same splitId, and at least 3 vertices were added.
- With fewer than 3 vertices no polygon is formed; this function returns 0 and clears this round's buffer.
- After applying, the window's display area is the source content clipped to the polygon outline; the part outside the polygon becomes a transparent "pass-through" area (the desktop is visible).
- The shape overrides any previously set shape (ellipse, rounded rectangle, bitmap shape, etc.), because each shape application replaces the window region.
- The recording state ends automatically after calling end_shape; you can immediately start a new shape recording for another window.

## Example

```gml
// In the Step event of a controller object: press D to clip split window 1 into a diamond, press C to restore the rectangle
if (keyboard_check_pressed(ord("D")))
{
    var _w = 640;
    var _h = 360;

    qiumingdll_winsplit_begin_shape(global.split_1);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w / 2, 0);      // top
    qiumingdll_winsplit_add_shape_point(global.split_1, _w, _h / 2);     // right
    qiumingdll_winsplit_add_shape_point(global.split_1, _w / 2, _h);     // bottom
    qiumingdll_winsplit_add_shape_point(global.split_1, 0, _h / 2);      // left

    if (qiumingdll_winsplit_end_shape(global.split_1) == 1)
        show_debug_message("Diamond shape applied");
}

if (keyboard_check_pressed(ord("R")))
    qiumingdll_winsplit_clear_shape(global.split_1);
```

## Related functions

- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_add_shape_point](qiumingdll_winsplit_add_shape_point.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)
