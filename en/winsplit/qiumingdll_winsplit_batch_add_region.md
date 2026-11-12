# qiumingdll_winsplit_batch_add_region(splitId, x, y, w, h, durationMs)

Adds a "region transform" command to the batch recording: during playback the window moves to the target position and scales to the target size within durationMs milliseconds (the source region follows the source animation mode in effect at that time).

## Signature

```gml
qiumingdll_winsplit_batch_add_region(splitId, x, y, w, h, durationMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| x | Real | yes | Target X coordinate (screen coordinate system, in pixels) |
| y | Real | yes | Target Y coordinate (screen coordinate system, in pixels) |
| w | Real | yes | Target width (client area width, in pixels) |
| h | Real | yes | Target height (client area height, in pixels) |
| durationMs | Real | yes | Duration of this animation segment, in milliseconds; pass 0 to skip the transition and snap into place when the command starts |

## Returns

| Value | Description |
|----|------|
| 1 | Command added successfully |
| 0 | Add failed: invalid splitId, not recording, or the command count has reached the limit of 32; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: `qiumingdll_winsplit_batch_begin` must have been called to enter recording state, and `qiumingdll_winsplit_batch_end` must not have been called yet.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- This command is equivalent to combining batch_add_position and batch_add_size: position and size interpolate together the whole time, but it uses only one command slot.
- Source region follow is decided by the source animation mode set when the command was added (see qiumingdll_winsplit_batch_set_src_anim_mode).
- Easing is taken from the batch easing curve set when the command was added (see qiumingdll_winsplit_batch_set_easing).
- The start state of a command is the window state at the moment the command begins; commands join end to end in order.

## Example

```gml
// Key event: record a complete "fly in + zoom up -> restore" sequence
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_region(global.splitId, 400, 300, 640, 480, 600); // fly in and zoom up
    qiumingdll_winsplit_batch_add_wait(global.splitId, 400);                       // stay for 400ms
    qiumingdll_winsplit_batch_add_region(global.splitId, 100, 100, 320, 240, 600); // fly back and shrink
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_add_wait](qiumingdll_winsplit_batch_add_wait.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
