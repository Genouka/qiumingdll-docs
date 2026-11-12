# qiumingdll_winsplit_add_shape_point(splitId, x, y)

Adds a vertex to the polygon shape currently being recorded, between begin_shape and end_shape.

## Signature

```gml
qiumingdll_winsplit_add_shape_point(splitId, x, y)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, 1 ~ 16, must match the splitId of the begin_shape call of this group |
| x | Real | yes | Vertex X, in pixels, relative to the top-left corner (0,0) of the split window client area, usually 0 ~ client area width |
| y | Real | yes | Vertex Y, in pixels, relative to the top-left corner (0,0) of the split window client area, usually 0 ~ client area height |

## Returns

| Value | Description |
|----|------|
| 1 | Vertex added successfully |
| 0 | Failed: invalid splitId, this window is not in shape recording state (no begin_shape), or the vertex count has reached the limit of 256; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_begin_shape` has been called for the same splitId and `end_shape` has not been called yet.
- Vertex coordinates are pixels inside the split window client area and are unrelated to the source region. Coordinates beyond the window size are still recorded, but the corresponding part of the window will not show a valid shape.
- At least 3 vertices are required (for end_shape to succeed), at most 256; additions beyond the limit are rejected and return 0.
- Vertices are connected in the order they were added to form a closed polygon (Windows polygon regions handle self-intersecting parts by the default even-odd (ALTERNATE) fill rule).
- What is added are polyline vertices; the engine closes the figure automatically, so there is no need to repeat the first point manually.

## Example

```gml
// In the Step event of the control object: press F to clip split window 1 into a hexagon (vertex coordinates relative to its client area)
if (keyboard_check_pressed(ord("F")))
{
    var _w = 640; // assume the split window client area is 640x360
    var _h = 360;

    qiumingdll_winsplit_begin_shape(global.split_1);

    qiumingdll_winsplit_add_shape_point(global.split_1, _w * 0.5, 0);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w, _h * 0.25);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w, _h * 0.75);
    qiumingdll_winsplit_add_shape_point(global.split_1, _w * 0.5, _h);
    qiumingdll_winsplit_add_shape_point(global.split_1, 0, _h * 0.75);
    qiumingdll_winsplit_add_shape_point(global.split_1, 0, _h * 0.25);

    if (qiumingdll_winsplit_end_shape(global.split_1) == 1)
        show_debug_message("Hexagon shape applied");
}
```

## Related functions

- [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md)
- [qiumingdll_winsplit_end_shape](qiumingdll_winsplit_end_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)
