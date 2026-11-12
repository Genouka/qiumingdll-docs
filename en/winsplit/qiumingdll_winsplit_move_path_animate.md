# qiumingdll_winsplit_move_path_animate(splitId, totalMs, intervalMs)

Moves the given split window smoothly along the recorded path, segment by segment; when the animation ends the window stays at the last point of the path.

## Signature

```gml
qiumingdll_winsplit_move_path_animate(splitId, totalMs, intervalMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| totalMs | Real | yes | Total duration of the movement along the whole path, in milliseconds; the duration is divided evenly among the segments (segment duration = totalMs / (point count - 1)) |
| intervalMs | Real | yes | Refresh interval, in milliseconds; internally clamped to a minimum of 1 ms (0 or negative values are treated as 1 ms) |

## Returns

| Value | Description |
|----|------|
| 1 | Path animation started |
| 0 | Start failed: invalid splitId, or fewer than 2 path points; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create), and add at least 2 path points with qiumingdll_winsplit_add_path_point.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- The window size stays unchanged while moving along the path; only the position changes.
- Each segment uses the window's current easing curve (see qiumingdll_winsplit_set_easing_curve, default ease-in-out); think of the path as "several consecutive sub-animations".
- Calling this function immediately stops any normal animation currently playing on that window and starts moving from the current position (usually the screen position of the first path point).
- When the animation ends the window stays at the last path point, but the path point list is kept (clear it with qiumingdll_winsplit_clear_path when needed).
- Path point coordinates are absolute screen coordinates; the animation is timed by system time and is not affected by the game frame rate.
- During the animation you can query the state with qiumingdll_winsplit_is_animating, and stop it midway with qiumingdll_winsplit_stop_animation.

## Example

```gml
// Key event: record a polyline path and move along it
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_clear_path(global.splitId);
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);  // point 1
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 100);  // point 2
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 300);  // point 3
    // total duration 600 ms, 2 segments, 300 ms each
    qiumingdll_winsplit_move_path_animate(global.splitId, 600, 16);
}

// Step event: poll whether the animation has finished
if (qiumingdll_winsplit_is_animating(global.splitId) == 0)
{
    show_debug_message("Path animation finished; the window stays at the last point");
}
```

## Related functions

- [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md)
- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md)
- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
