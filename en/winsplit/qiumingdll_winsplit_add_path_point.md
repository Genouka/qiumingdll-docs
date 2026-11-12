# qiumingdll_winsplit_add_path_point(splitId, x, y)

Appends a path point (screen coordinates) to the path list of the given split window; the points can then be used with move_path / move_path_animate.

## Signature

```gml
qiumingdll_winsplit_add_path_point(splitId, x, y)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| x | Real | yes | Path point X coordinate (screen coordinate system, in pixels) |
| y | Real | yes | Path point Y coordinate (screen coordinate system, in pixels) |

## Returns

| Value | Description |
|----|------|
| 1 | Path point added successfully |
| 0 | Add failed: invalid splitId, or the path point count has reached the limit of 256; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Path points accumulate in call order; each window supports at most 256 points, and calls beyond the limit return 0 and are ignored.
- Adding path points only records coordinates; it does not move the window.
- Path animation requires at least 2 points (see qiumingdll_winsplit_move_path_animate); with fewer than 2 points you can still use qiumingdll_winsplit_move_path alone to jump to the last point.
- It is recommended to call qiumingdll_winsplit_clear_path to clear the old path before adding a new set of points.
- Path point coordinates are absolute screen coordinates, not relative offsets.

## Example

```gml
// Key event: record an L-shaped path (3 points)
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_clear_path(global.splitId);
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);  // start point
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 100);  // end of the horizontal segment
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 300);  // end of the vertical segment
    // then call qiumingdll_winsplit_move_path_animate(global.splitId, 600, 16);
}
```

## Related functions

- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
