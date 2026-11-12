# qiumingdll_winsplit_stop_animation(splitId)

Stop a normal animation (position/size/region/path animation) currently playing on the specified split window midway; the window stays at the position where it was stopped.

## Signature

```gml
qiumingdll_winsplit_stop_animation(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (regardless of whether an animation was playing) |
| 0 | `splitId` is invalid (the split window does not exist), or the platform is not Windows (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: the library must be initialized and the split window created first (`qiumingdll_winsplit_init` / `qiumingdll_winsplit_create`).
- Platform limit: Windows only; on other platforms the GML wrapper returns `0` directly.
- After stopping, the window stays at the current interpolated position; it does not jump to the target value or the path's end point.
- Stopping also resets the path animation state (path points are not cleared, but are reused when `move_path_animate` restarts).
- Only affects normal animations; batch animations must be stopped separately with `qiumingdll_winsplit_batch_stop`.
- Calling it while no animation is playing also returns 1; it is safe to call repeatedly.

## Example

```gml
// Key event: start a long move
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 800, 600, 5000, 16);
}

// Key event: stop midway (stays at the current intermediate position)
if (keyboard_check_pressed(vk_x))
{
    qiumingdll_winsplit_stop_animation(global.splitId);
}

// Step event: print the state after the animation ends
if (qiumingdll_winsplit_is_animating(global.splitId) == 0)
{
    show_debug_message("Animation stopped or finished");
}
```

## Related functions

- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
