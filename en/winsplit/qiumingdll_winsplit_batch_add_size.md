# qiumingdll_winsplit_batch_add_size(splitId, w, h, durationMs)

Adds a "size scale" command to the batch recording: during playback the window scales from its current size to the target size (w, h) within durationMs milliseconds (the source region follows the source animation mode in effect at that time).

## Signature

```gml
qiumingdll_winsplit_batch_add_size(splitId, w, h, durationMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
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
- This command does not change the window position, it only scales the size.
- Source region follow is decided by the source animation mode set when the command was added (see qiumingdll_winsplit_batch_set_src_anim_mode): 0 = none (picture stretches to fill), 1 = proportional stretch, 2~10 = crop by anchor.
- Easing is taken from the batch easing curve set when the command was added (see qiumingdll_winsplit_batch_set_easing).
- The start state of a command is the window state at the moment the command begins; commands join end to end in order.

## Example

```gml
// Key event: record a "zoom up - short wait - restore" sequence (this function provides the two scale commands)
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_set_src_anim_mode(global.splitId, 1);  // source region stretches proportionally with the window
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 500);   // zoom up to 640x480 within 500ms
    qiumingdll_winsplit_batch_add_wait(global.splitId, 200);             // stay for 200ms
    qiumingdll_winsplit_batch_add_size(global.splitId, 320, 240, 500);   // shrink back to 320x240 within 500ms
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
