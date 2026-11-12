# qiumingdll_winsplit_set_size_animate(splitId, w, h, totalMs, intervalMs)

Smoothly scale the split window from its current size to the target size. The source region can follow according to the source animation mode, and the window remains at the target size when the animation ends.

## Signature

```gml
qiumingdll_winsplit_set_size_animate(splitId, w, h, totalMs, intervalMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | real | yes | Split window number, starting from 1, maximum 16 |
| w | real | yes | Target width (client-area width, in pixels) |
| h | real | yes | Target height (client-area height, in pixels) |
| totalMs | real | yes | Total animation duration in milliseconds; passing 0 ends the animation immediately and jumps to the target size |
| intervalMs | real | yes | Refresh interval in milliseconds; clamped internally to a minimum of 1 ms (0 or negative values are treated as 1 ms) |

## Returns

| Value | Description |
|----|------|
| `1` | Animation started |
| `0` | `splitId` is invalid (the split window does not exist), or the platform is not Windows (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: the library must be initialized and the split window created first (`qiumingdll_winsplit_init` / `qiumingdll_winsplit_create`).
- Platform limit: Windows only; on other platforms the GML wrapper returns `0` directly.
- Sizes refer to the window's client area. The top-left corner stays fixed during scaling; if the window has a title bar, the outer window rectangle is recalculated internally.
- How the source region follows is determined by the window's current source animation mode (see `qiumingdll_winsplit_set_src_anim_mode`):
  - Mode 0: the source region stays fixed and the picture is stretched or compressed to fill;
  - Mode 1 (stretch): the source region scales proportionally, so the picture content grows or shrinks with the window;
  - Modes 2~10 (crop): the source region expands or contracts toward the anchor direction.
- The scaling uses the current easing curve (default ease-in-out).
- Calling this function immediately stops any normal animation currently playing on the window, then interpolates from the size at the time of the call to the target.
- The window position does not change during this animation.
- When the animation ends the window stays at the target `(w, h)`. Use `qiumingdll_winsplit_is_animating` to poll for completion.

## Example

```gml
// Create event: initialize, create the split window, and configure the "stretch" source animation mode
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
qiumingdll_winsplit_set_src_anim_mode(global.splitId, 1);  // Source region scales with the window

// Key event: enlarge to 640x480 within 1 second (source region scales in sync)
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_size_animate(global.splitId, 640, 480, 1000, 16);
}
```

## Related functions

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
