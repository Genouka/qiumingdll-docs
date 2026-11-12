# qiumingdll_winsplit_set_easing_curve(splitId, curve)

Sets the easing curve of the given split window; the curve applies to all subsequent normal animations of that window (position/size/region/path animations).

## Signature

```gml
qiumingdll_winsplit_set_easing_curve(splitId, curve)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 (same number as returned by qiumingdll_winsplit_create) |
| curve | Real | yes | Easing curve enumeration, value range 0~11, see the table below |

Easing curve enumeration (shared with `qiumingdll_winsplit_batch_set_easing`):

| Value | Name | Description |
|----|------|------|
| 0 | linear | Linear, constant speed throughout |
| 1 | ease-in | Quadratic ease-in (slow first, then fast) |
| 2 | ease-out | Quadratic ease-out (fast first, then slow) |
| 3 | ease-in-out | Quadratic ease-in-out |
| 4 | in-cubic | Cubic ease-in |
| 5 | out-cubic | Cubic ease-out |
| 6 | in-out-cubic | Cubic ease-in-out |
| 7 | in-back | Overshooting ease-in (pulls back first, then overshoots the target) |
| 8 | out-back | Overshooting ease-out (overshoots the target, then swings back) |
| 9 | in-out-back | Overshooting ease-in-out |
| 10 | bounce-out | Bouncing ease-out (bounces a few times on landing) |
| 11 | elastic-out | Elastic ease-out (oscillation settles down) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | splitId is invalid (outside the 1~16 range or the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize with qiumingdll_winsplit_init() first, then create a split window with qiumingdll_winsplit_create().
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- This setting is persistent state: set it once after creating the window and before starting an animation; later calls to set_position_animate / set_size_animate / set_region_animate / move_path_animate reuse the curve until it is changed again.
- The default curve is ease-in-out (value 3); when this function is not called, animations also use that default.
- Only affects normal animations of that window, not batch animations; for batch playback set the curve separately with qiumingdll_winsplit_batch_set_easing (although batch_begin takes the window's current curve as the initial batch curve).
- Do not pass values outside 0~11; the value is assigned internally as an integer and out-of-range behavior is undefined.

## Example

```gml
// Create event: create the split window and configure the bounce-out curve
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
if (global.splitId > 0)
{
    qiumingdll_winsplit_set_easing_curve(global.splitId, 10);  // bounce-out
}

// Key event: start a position animation; it flies out using the bounce-out curve
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 800, 600, 1000, 16);
}
```

## Related functions

- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
