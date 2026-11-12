# qiumingdll_winsplit_clear_path(splitId)

Stop the animation currently playing on the specified split window and clear all path points that have been added.

## Signature

```gml
qiumingdll_winsplit_clear_path(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Cleanup succeeded |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Preconditions: you must first initialize and create a split window (`qiumingdll_winsplit_init` / `qiumingdll_winsplit_create`).
- Platform limit: Windows only; on other platforms this GML wrapper returns 0 directly.
- This function stops the window's currently playing normal animations (position/size/region/path animations) and clears the path point list.
- The window stays at the intermediate position where the animation was stopped and does not jump to the target or the end of the path.
- Call this function before recording a new set of path points to avoid leftover old points.
- Does not affect the playback state of batch animations.

## Example

```gml
// Key event: reset the path and record it again
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_clear_path(global.splitId);   // Clear the old path (and stop any path animation)
    qiumingdll_winsplit_add_path_point(global.splitId, 100, 100);
    qiumingdll_winsplit_add_path_point(global.splitId, 400, 100);
    qiumingdll_winsplit_move_path_animate(global.splitId, 600, 16);
}
```

## Related functions

- [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md)
- [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
