# qiumingdll_winsplit_set_region_animate(splitId, x, y, w, h, totalMs, intervalMs)

Smoothly moves the split window from its current position and size to the target position and size (combined position + size animation); the window stays in the target state when the animation ends.

## Signature

```gml
qiumingdll_winsplit_set_region_animate(splitId, x, y, w, h, totalMs, intervalMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| x | Real | yes | Target X coordinate (screen coordinate system, in pixels), target position of the window's top-left corner |
| y | Real | yes | Target Y coordinate (screen coordinate system, in pixels) |
| w | Real | yes | Target width (client-area width, in pixels) |
| h | Real | yes | Target height (client-area height, in pixels) |
| totalMs | Real | yes | Total animation duration in milliseconds; passing 0 ends the animation immediately and jumps to the target region |
| intervalMs | Real | yes | Refresh interval in milliseconds; clamped internally to a minimum of 1 ms (0 or negative values are treated as 1 ms) |

## Returns

| Value | Description |
|----|------|
| 1 | Animation started |
| 0 | splitId is invalid (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Position and size are interpolated together throughout the animation; it is equivalent to combining set_position_animate and set_size_animate, but occupies a single animation state, so the two do not overwrite each other.
- The source-region coupling is determined by the window's current source animation mode (see qiumingdll_winsplit_set_src_anim_mode): mode 1 stretches proportionally, modes 2~10 crop by anchor.
- Interpolation uses the current easing curve (default ease-in-out).
- Calling this function immediately stops any normal animation currently playing on the window, then interpolates from the state at the moment of the call to the target.
- When the animation ends the window stays at the target (x, y, w, h); poll qiumingdll_winsplit_is_animating to detect the end.

## Example

```gml
// Create event: initialize and create the split window
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);

// Key event: smoothly move from (100,100,320x240) to (50,50,800x600) within 1.2 seconds
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_region_animate(global.splitId, 50, 50, 800, 600, 1200, 16);
}
```

## Related functions

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
