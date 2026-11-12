# qiumingdll_winsplit_is_animating(splitId)

Queries whether the given split window is currently playing a normal animation (position/size/region/path animation).

## Signature

```gml
qiumingdll_winsplit_is_animating(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | The animation is playing |
| 0 | No animation is playing; or splitId is invalid; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly (indistinguishable from "not animating").
- Reflects only normal animation state, not batch animations; use qiumingdll_winsplit_batch_is_playing for batch playback.
- An animation ends automatically and resets to zero once totalMs has elapsed; no manual reset is needed.
- Typical use: poll in the Step event and trigger follow-up logic when the animation finishes (for example playing the next action or destroying the window).

## Example

```gml
// Key event: start a 2-second position animation
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 600, 400, 2000, 16);
}

// Step event: run cleanup logic once the animation has finished (only once)
if (global.move_anim_done == false && qiumingdll_winsplit_is_animating(global.splitId) == 0)
{
    global.move_anim_done = true;
    show_debug_message("Move animation finished");
}
```

## Related functions

- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
