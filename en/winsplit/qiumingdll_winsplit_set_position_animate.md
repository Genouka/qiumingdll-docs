# qiumingdll_winsplit_set_position_animate(splitId, x, y, totalMs, intervalMs)

Smoothly moves the split window from its current position to the given screen coordinates. The animation is driven by an internal timer and the window stays at the target position when it ends.

## Signature

```gml
qiumingdll_winsplit_set_position_animate(splitId, x, y, totalMs, intervalMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| x | Real | yes | Target X coordinate (screen coordinate system, in pixels), i.e. the screen position the top-left corner of the window moves to |
| y | Real | yes | Target Y coordinate (screen coordinate system, in pixels) |
| totalMs | Real | yes | Total animation duration in milliseconds; passing 0 ends the animation immediately and jumps to the target position |
| intervalMs | Real | yes | Refresh interval in milliseconds; clamped internally to a minimum of 1 ms (0 or negative values are treated as 1 ms) |

## Returns

| Value | Description |
|----|------|
| 1 | Animation started |
| 0 | splitId is invalid (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- The movement uses the window's current easing curve (see qiumingdll_winsplit_set_easing_curve, default ease-in-out).
- Calling this function immediately stops any normal animation currently playing on the window (including path animations), then interpolates from "the position at the moment of the call" to the target instead of continuing from the remaining target offset.
- The source region stays unchanged during the animation (this animation forces the source animation mode to none internally).
- The time base is system time, not the game frame rate; the smaller intervalMs, the smoother the animation — around 16 ms is recommended.
- When the animation ends the window stays at the target (x, y); poll qiumingdll_winsplit_is_animating to detect the end.

## Example

```gml
// Create event: initialize and create the split window
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);

// Key event: slide the window from its current position to (400, 300) within 800 ms, refreshing every 16 ms
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 400, 300, 800, 16);
}
```

## Related functions

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
