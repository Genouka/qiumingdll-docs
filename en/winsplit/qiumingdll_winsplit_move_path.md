# qiumingdll_winsplit_move_path(splitId)

Without animation, moves the given split window immediately to the last path point of the current path and clears the path point list.

## Signature

```gml
qiumingdll_winsplit_move_path(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Jump succeeded; the window has moved to the last point |
| 0 | Jump failed: invalid splitId, or the path point count is 0 (no point to jump to); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create), and add at least 1 path point with qiumingdll_winsplit_add_path_point.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- This function is a "teleport": it moves the window immediately to the last path point, leaving the window size unchanged.
- After a successful jump the path point list is cleared (pathCount returns to zero).
- This function does not stop a normal animation that is currently playing. If a position animation is running, its subsequent progress keeps overwriting the window position, so call qiumingdll_winsplit_stop_animation or qiumingdll_winsplit_clear_path first.
- For smooth movement use qiumingdll_winsplit_move_path_animate.

## Example

```gml
// Key event: teleport to the end of the path
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_clear_path(global.splitId);
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);
    qiumingdll_winsplit_add_path_point(global.splitId, 800, 500);
    qiumingdll_winsplit_move_path(global.splitId);  // jump to (800, 500) immediately
}
```

## Related functions

- [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md)
- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
